SIG: Kubernetes Operator SIG
Date: 2026-02-12
Duration: 42 minutes
============================================================

## Zoom Recording Transcript

**Mikołaj Świątek** 01:32 Hi there. I just kicked out the AI meeting notes thing.
**ploffay** 01:42 Hello, honey, Glenn.
**Mikołaj Świątek** 01:54 Did Jacob say anything?
Doesn't look like it.
Maybe he'll be here, let's give it, like, maybe 2 more minutes?
Hmm, alright, do you want to get started?
**ploffay** 03:21 Yeah, let's get started.
**Mikołaj Świątek** 03:23 Right, we don't actually have anything on the agenda, aside from our, kind of, normal items. Do we have anything new to discuss at SIG? It doesn't seem like it.
**Arthur Silva Sens** 03:38 Mmm.
**ploffay** 03:39 I was… Sorry, go ahead.
**Arthur Silva Sens** 03:43 I was gonna say that I'm pretty new here, literally my first SIG meeting.
**Mikołaj Świątek** 03:48 Welcome.
**Arthur Silva Sens** 03:49 I agree.
Yeah, thank you.
And I would have something to discuss, but I don't want to reject the meeting.
Especially since it's my first.
**Mikołaj Świątek** 04:01 Let's… let's go. We only have, like, we only have… it looks like we only have, kind of, organizational items. The feature gates, I don't think anything has changed in there, so there's no real reason to look at them, so your stuff will be next, if you want to go.
**Arthur Silva Sens** 04:23 I have a feeling that That it has been discussed before, using the hotel operator to install a pentelemetry injector.
And if, yes, if that's true, I would love to help moving that forward.
But… I would love to move this forward by, like, discussing with the group, finding ways that this makes sense to the operator.
yeah, let's start with that. Any discussions happened before?
**ploffay** 05:00 Yeah, actually.
**Mikołaj Świątek** 05:01 I believe we… yeah. So, please go ahead, Paul.
**ploffay** 05:04 Yeah, I was looking into this recently. We are planning some major changes to the instrumentation CR.
We would like to introduce V1 Beta 1 for the instrumentation, and kind of… improve the CR structure based on the learnings from the V1 Alpha-1.
And… As well, introduce the declarative config.
And for injecting the libraries, look at the injector as a way to… You know, to do it.
**Arthur Silva Sens** 05:45 Hmm.
Okay.
So this is two separate things, right?
also instrumentation CR, and… instrumentation CR.
Or they're the same, CR?
**ploffay** 05:59 No, it's the same… it's the same CR, we just want… like, are you familiar with the hotel operator and the instrumentation process that we have right now?
**Arthur Silva Sens** 06:07 I… being very honest, I used to maintain the Prometheus operator, and I was familiar years ago, when I was maintained a Prometus operator, but it… I don't know what more advanced in the hotel operator Since 2 years ago.
**ploffay** 06:26 So in the auto operator, we have the instrumentation CR, you can find it in the README.
And… this is… essentially… It has a similar functionality to what the injector does. So the instrumentation implementation, it… Injects the auto-instrumentation libraries to the pods that are starting in the cluster, and configures the a runtime to pick them up, so it will configure the Java 2 options and the Python and Node.js environment variables to… to start the instrumentation process. And this is essentially what the injector does, right? And so… This is something that we build in the auto operator, and we as well kind of built the auto-instrumentation images.
And… There is a lot of effort going into maintaining this approach, and so we would like to simplify it by using the injector.
And it will as well solve the problem with overriding the… the environment variable to configure the runtime, right? Like, the tool options can be kind of hard-coded in the… in the Docker file, or it can be hard-coded… or not hard-coded, but it can be provided in the config map, and… With the current approach, there is no way for us to kind of catch that.
It will be only possible by… Using the injector with the LD preload approach.
So it will solve, as well, some of the, kind of, reliability of instrumentation issues.
**Arthur Silva Sens** 08:16 Hey, you see it as… This strategy with the injector as a replacement to the… to the alto instrumentation that exists today, or, like.
**ploffay** 08:28 To some degree, yes. Yeah, I think for the current version of the instrumentation CR, we… We should keep what we have.
Probably.
And for the new version, use the injector.
However, I think the… the injector doesn't support all the languages that we support, right? So it will be only for the subset.
**Mikołaj Świątek** 09:05 So, there's, like, two different… from our perspective, there's two different aspects of this, right? One is the… just the implementation.
We kind of manually do what the injector does, and we do it worse than it does it, because we only have, like, the ability to set environment variables.
on the, on the container running the application. So… and this causes some problems. For example, we don't deal… don't… can't deal with, settings like Java tool options or node tool options, because we don't have the ability to merge that, you can only replace it, so if somebody sets it We're breaking their application, potentially, by messing with it.
And the injector does that, so that's a feature. And in that respect, this is just, like, an implementation detail, like, we wouldn't change anything about our API or anything happens, we would just take our current existing instrumentation images, add the injector to them, and then change the implementation of how the injection process actually happens.
So that's, like, an implementation level change.
an alternative.
is, and perhaps parallel thing, is to create a… kind of a dual image, let's call it, or contain all image. That's kind of the approach, I think, that the injector project may be taking for some stuff, or at least that was the approach that the Dash Zero people, who originally donated that idea, or I guess Splunk donated it, but the Dash Zero people were the ones who really kind of… Used it heavily in production before it made its way anywhere else.
So… and the approach they have is that they bundle everything into a single image, and just kind of instrument everything by default.
And that's just, like, from, like, a application logic perspective, that's a different thing than we do. We are very… our current logic for instrumentation is very opt-in, so it… you… in order for us to instrument your pod, it has to be annotated in a particular way.
And that's it.
Whereas it's possible that what we want to add is some kind of… collective instrumentation object that's gonna work this way, where it's just going to be automagical per user, where they won't have to, like, worry about, like.
oh, you know, oh, this is a Python application, so I have to set these and these things here, and figure out how to do the Python, and you just kind of have… The one injector that you just put in there, and the injector figures things out for you.
And you're done. So it's possible that's also going to happen. So I'm wondering if you came here to talk about, like, that bit, or just the implementation?
**Arthur Silva Sens** 12:02 Like, I… I am… I want to do the implementation That the maintainers… would give the blessing. I don't want to convince you Which approach is better?
I understand that you are already using opt-in approach?
Like, you mentioned Python. Python… You also have to give the architecture, annotation, something.
**Mikołaj Świątek** 12:34 Yes, and that's another… that's… and for .NET as well, that's another thing that we would like to… the injector to do for us, because right now, the user has to care about this.
**Arthur Silva Sens** 12:43 Yeah.
**Mikołaj Świątek** 12:44 They built the application with libc or Muzzle, and…
**Arthur Silva Sens** 12:49 So we could… we could do just one single annotation, like, I don't know, injector? Sounds a little bit weird, but… And then you don't need to care about your language, you don't need to care about your architecture, the injector will be smart enough to capture that and do the right thing.
**Mikołaj Świątek** 13:09 I think that if you want to try using the injector, the numerous annotations, we want to use labels. We'll use labels for performance reasons, but that's, like, for… because it's a mutating webcook. If it's an annotation, it has to get all the pod changes from the whole cluster, and that's just, like, not a good time for anyone. But that's an orthogonal change. I think that, like, if you want to try to dip your, kind of, toes into it, and see if it's going to work, then what I would would do is to… I would try to take a programming language that is well supported in the injector right now. I don't know what that is. I guess Java probably is usually the best… the most supported language in these kinds of discussions.
So just take, take, take, let's say, Java, and do, like, a proof of concept. A proof of concept where you take the injector, you stick it into our Java instrumentation container, and you change the implementation so that it uses the injector in terms of our current approach. Like, that is, like, the minimal change.
That works, and it would validate that it works.
the way we think it works. If what you want to do is… like, provide some kind of new functionality for the operator. Like, have the operator do something new instead of, like, doing what it does right now and just using the injector under the hood.
then we have to talk about what that's gonna look like, because then you're proposing a new public API, and, you know, you maintain the project, you know, that, like, that's a much more, much more careful, careful decision.
**Arthur Silva Sens** 14:46 I feel like just replacing what we couldn't have with Injector is already a good… a good improvement, and we can start with that. Like, this is small enough, and we can discuss If… if needed, in the future, changes. I… I honestly, I… I like the opt-out.
But I don't like… like, just… I just said, like, this is my first meeting, I don't want to just jump in and change the whole thing by myself.
**jea** 15:19 Arthur, what I would say is you should start With a new… You can keep it internal, don't… you don't need to expose it, but I would try to not modify the existing injector code.
I think that that code is really… Brought with a lot of, like, foot guns. A lot of things that could go very wrong.
And so…
**Arthur Silva Sens** 15:44 The injector code, you mean the mutating webhook?
**jea** 15:48 Yeah, like the existing, the things that we do today for injecting the SDKs.
**Arthur Silva Sens** 15:56 Like, the operator's current code for doing this.
**jea** 15:59 I would say you should start a new package in internal.
And then add in a flag onto the CR that, gives us the opt-in for this.
And then the mutating webhook can be changed, To have an optional filter Or, workloads with the label that we want to use.
That way, it's, like, all net new.
which I think will make this a lot easier to review, and a lot less likely to just… to break Anything existing, as well.
It expands the scope of your work a little bit, but I do think it increases its safety.
One of the things that I… I really don't like doing, and I… I'm gonna… I don't think I'm speaking for myself here. I think other maintainers here also feel the same. Reviewing the current instrumentation code is really difficult.
And I think adding and modifying anything to that, package is only going to make it harder to review. And so I think starting from net new, will help keep the scope limited so that we can actually review it effectively.
**Arthur Silva Sens** 17:18 Alright, thanks for the tip.
**ploffay** 17:22 I agree, that's why I was suggesting that we wait with the injector until we have the V1 Beta 1.
That it's gonna be, kind of.
A clean implementation, and maybe start with the injector, and then… For the languages that are not supported by the injector, kind of… At them in a clean way, with a kind of clean implementation of the current approach.
**jea** 17:49 Yeah, I think, Pablo, that if we were to do… I think that, is fine, but I also want to… If Arthur has the cycles to, like, get this logic in now, before we merge in and figure out the V1 beta, I think we should just do that with, like, a Boolean flag on the CRD itself, not a feature flag, so that it's, like, a user opt-in thing, and then it's clear that they need to add a label. And then, when we move to the V1 beta one, we basically… we don't need that flag anymore, this is… we just say, this is the way that it works.
And then if you already are doing it with the label that we want you to use, then it will just continue to work as, like, a little carrot to… to have them move to that approach.
**Arthur Silva Sens** 18:33 Yeah, I think I lost something there. You… You said a flag, not a feature flag? What's the difference?
**jea** 18:42 Like, like an actual, additional field on the existing instrumentation CR that's just called, like.
I don't know, new injector opt-in, or something that is, more… What's the word?
you would call it, like, Use Experimental Injector, or something like that. And then… That is the… that is the way that we'll know to actually hit that code path.
Because what we don't want to do… the reason that we can't just use a normal operator feature flag.
For this is that if we were to do that, then it would potentially hit that code path for all instrumentation, and we'd have to do a check for all instrumentation. Whereas, if we were to use a… experimental flag on the CRD, then a user, you know, or you just doing your testing.
Could just set that flag to true.
And then only that instrumentation object is going to go down that code path, which I think increases the safety and blast radius here.
**Arthur Silva Sens** 19:49 Okay.
**ploffay** 19:51 I'm wondering if we… if we need a kind of change to instrumentation CR, maybe just adding the… Kind of new label to inject.
**jea** 20:02 Oh, that's a good idea, too.
Yeah.
Yeah, because then you won't need to make any instrumentation changes, it's just if you're using the label, then we'll migrate you to this… this new internal code path. I like that, Pavel.
**Arthur Silva Sens** 20:16 I was a little bit worried that if we add a new field to a CR, Like, removing them in the future is a breaking change, right?
**jea** 20:26 Yes, but we're gonna be moving to a V1 Beta 1 anyway, and that's… that's when we are sort of allowed to do these braking changes, so it's… it's totally fine to add in, a field that we're going to remove, but I think with Pavel's approach, we won't even need to do that.
**Arthur Silva Sens** 21:02 Okay, I feel like this is… enough information for me to start a POC. Thanks.
**jea** 21:11 Cool. Yeah, thanks so much. Really appreciate it. And, if you run into, problems with either the injector or the operator, I'm a maintainer for both projects, so… Oh, awesome.
let me know if you run into any issues there. Awesome. The Dash Zero folks also have their own, like, version of the operator, that uses the injector.
And that's also open source, so you can, like, check that code out as well.
**Arthur Silva Sens** 21:36 Yeah, I did, I did.
**jea** 21:38 But… yeah, let me know if you run into anything.
**Arthur Silva Sens** 21:43 Alright, thank you.
**jea** 21:44 Yup.
Next on the list, Pablo?
**ploffay** 21:52 Yeah, I wanted to talk about the pull request. Let me just open… It's about the… the TLS profile, I think this combines two features in a single PR.
One feature is… the TLS profile, and the second feature is that we auto-configure TLS in the… Collector components and the target allocator.
So, for the TLS profile, the… What does it mean? It actually means that the… the operator gets TLS settings from the cluster.
it works only on OpenShift right now, and it queries the API server CR, and it gets the TLS min version, and… ciphers from that CR, and then uses this two fields in all TLS settings that the operator and operands do.
We have already flags on the operator for the ciphers and min version, but we were… Not sure if we are using them consistently.
But what I added is another flag that will get the, the ciphers and TLS version from this OpenShift CR, and then it uses this… Fields, in the parsers and configures the collector components.
**jea** 23:35 Yeah, it seems fine. It seems like it's in the realm of the OpenShift things we do today. The one comment I had on this, Pavel, was that I think we should use the option pattern for this type of thing. I could imagine there being more… of these, things that we want to drill down in the future, beyond just TLS.
Something like, pieces of configuration for other… like, collector components. You could imagine we could use this for configuring a Prometheus receiver.
Right. Totally different feature, but kind of the same type of drilling, where we might get something from a Prometheus CR that we want to read, and then drill that down to the Prometheus receiver helper method. And so I think, were we to use the option pattern, we could do that In a much cleaner way, without sort of extending the… The signature.
**ploffay** 24:34 Yeah, I will take a look, but it's something, at least in this case, and for the premise as well, it's something that happens dynamically at runtime.
**jea** 24:46 Yup.
I think the option pattern should still work for that. You'll just have to make the option dynamically, and then pass that down to the method.
But I think that also then allows… I think we already have an interface for, where this config would come from, right? Like, where do we pass in TLS settings initially? Oh yeah, this, like, TLS profile provider.
Get passed into the webhook.
Right, you could, make another interface, which is, like, I don't know, something in the, Components.
Package, which is, like, option provider.
Right, which just returns a list of options.
And then you could have as many of these as you want.
Does that make sense?
**ploffay** 25:36 Because if… yeah, I think right now the parsers for components are configured statically.
Yeah. In it, and this sort of changes the approach that it's done dynamically.
and can…
**jea** 25:54 Yeah.
**ploffay** 25:55 Across the, the reconciliation groups.
**jea** 25:58 Yeah, I think that this would work if we do that options approach, and then you just dynamically create those in the reconcile loop… the reconcile loop.
and maybe you have a cache of them or something, so we're not, like, hammering memory, but…
**ploffay** 26:29 Yeah, I'll take Luke. Maybe I ping you if I… Coop.
**jea** 26:33 Yeah, I think I have an idea of how this… of how this would look, so, let me know if you… if, Of your implementation, like, it doesn't fit neatly into that.
**Mikołaj Świątek** 26:46 I… I just have one question about that, PR. This is something that I don't fully understand.
Do we… isn't there value in just having, like, an option per collector CR to set it?
Because, from my perspective, a lot of the value of what's happening in there is that you're… Setting it for the user in all of the components that we support.
And normally, if they wanted this, they would have to go in and do it manually.
But… being able to set it… and the code for this already exists, right? Like, all the code paths for this to do… to actually do this injection of these TLS settings in there already exists, because that's what the PR does, it's just that you only allow it to be configured her operator.
Essentially. And I'm wondering if there isn't, like, if it's not… Nicer to just expose it per collector.
Although, like, I don't know if there's a use case for this, it just, like, kind of seems… More elegant to do that way?
**ploffay** 27:57 That's a little bit, maybe, different use case, because… Primarily, we want to source the TLS config from the clustering.
If we put it on the CR, that's not gonna work for this use case, to get this automatically from the cluster.
**Mikołaj Świątek** 28:17 I mean, the… what you get from the cluster can just be the default.
Yep. And this is just an override.
**ploffay** 28:24 in the PR as well.
Like, users can still override the… the main version in the CR, in the TLS spec.
But it's gonna be per component, it's not gonna be, like, global only.
**Mikołaj Świątek** 28:38 Yeah, which is why I'm saying, from my perspective, the whole thing would be nicer if you had, like, a attribute on the collector.
saying, put these TLS settings in all the components, and then what the global flag on the operator would do is just change the default of that field.
**ploffay** 28:59 I see.
What do you know?
**Mikołaj Świątek** 29:02 I don't know if that's actually useful for anyone, though. It just, like, stood out to me that the… you're adding a feature that sounds like it could be useful, but as a… it's not even a question of how this is, like, where this is. I just feel like this might be useful to a bunch of people, and we put it as a operator Command line flag, which means it's going to be much less discoverable.
Like, the CR in general is more discoverable than anything else that we have, right? So maybe the answer is to just add a little bit more documentation somewhere?
Saying that, hey, you can do this.
**ploffay** 29:42 I think, in general, we should improve the… Feature gates, like docs.
**Mikołaj Świątek** 29:49 I mean, it's not a feature gate, right? It's… it's, permanent command line option.
Right?
**ploffay** 29:56 Yeah, yeah, in this case, yeah.
**Mikołaj Świątek** 30:06 But anyway, I don't… I've read… from what I've read of it, I don't really have objections to it, so if you want to merge it as is… Without waiting for me to figure my stuff out, and feel free.
**ploffay** 30:23 I think the issue that I had with your approach… with, kind of, not your approach, but about, kind of, exposing global TLS in the collector CR… Is that we would probably… Apparently, people will be asking for more stuff, like, they would like to then, as well, default the certificate, maybe.
In my case, it's just the mean version in Cypress.
**Mikołaj Świątek** 30:55 I mean, if we're… if we're letting them do this, then do we mind that much? How many things are there that they could want to set?
How many fields are there in that TLS config?
**ploffay** 31:16 I don't know, like, 5.
**Mikołaj Świątek** 31:19 It's not that many.
Anyway, like, this isn't… this isn't really something… that we have to think that deeply about. Like, we can add this… this… Park… Collector field later.
**ploffay** 31:43 Yeah, I think it can be added later as well.
**Mikołaj Świątek** 31:46 So it's fine. I just wanted to understand if you had, like, some important reason to not do it that way.
Okay, do we need to discuss anything else aside from this?
We have issues to discuss.
issues to discuss on SIG are two, one of which we did discuss already and didn't remove the label, and the other is about Maybe I added this at some point, is that right?
No, Israel added it, so maybe we should look at it. We have a… If you look at this here.
I'm gonna put it in Zoom chat for… Here it is. We have an issue open about people not liking the fact that our API package imports.
a YAML parser.
They don't even get… I'm sorry.
**jea** 33:25 Say that one more time? I missed that.
**Mikołaj Świątek** 33:29 There is a complaint about our API packages importing stuff, in particular about them importing a YAML parser.
The complaint is that these packages shouldn't do this.
you shouldn't have dependencies like this. Which is fair enough, I suppose.
Our solution to this would be to… Just… stick the conversion webhook logic in a different package, but… I recall this being some kind of problem, personally.
I have, like, a…
**jea** 34:09 Yeah, I also remember there being an issue here. I'm kind of of the opinion that if you're using our package as a external dependency, like, these things happen in projects. I guess it's kind of… I don't know. There's some amount of, I don't know how much of a real issue this is, you know?
But maybe I'm being too, what's the word?
Thoughtless, I guess?
**Mikołaj Świątek** 34:44 opinionated.
**jea** 34:46 Yeah.
**Mikołaj Świątek** 34:47 you know, not sensitive to users' problems.
They have an argument that a lot of operators do this thing, where they have a separate module for their API definitions, which I kind of agree, that if you want to depend on somebody else's APIs in this way, which we do, for example, we depend on Prometheus operator, for example, in this way.
it's nicer if you don't pull in their whole dependency tree. So I am… somewhat sympathetic to the idea of making that its own module.
Even if it's kind of going to suck a little bit to maintain it, most likely.
**jea** 35:28 Yeah.
Okay, I mean, I'm not opposed to it, I just… I'm surprised, maybe.
**Arthur Silva Sens** 35:40 I… I remember… when I was part of the Prometus Operator team, we… we made a lot of changes to our codebase, just so the OpenCelebrity codebase could use it.
I guess that's fair, fair-esque.
**Mikołaj Świątek** 35:58 Liam, in Prometheus Operator, that might have been us. I don't think OpenTelemetry Collector or any other projects uses Operator. Did you, did you make, did you make changes? Yeah, yeah, yeah, sorry. I meant, I meant hotel operator, so you could use our CRDs as well.
Really, that was for us. I thought that you just did that, for in general, to be nice.
I don't even remember how that went out.
**Arthur Silva Sens** 36:24 Yeah, it was a long time ago. I remember discussing a lot with hotel folks.
**jea** 36:30 It might have been me. I feel like I remember this.
**Arthur Silva Sens** 36:35 Yeah, at the time, I was not… I was not involved with Notel at all. Very long time ago.
**Mikołaj Świątek** 36:40 Wow, Jacob, you're such a hypocrite, you see?
And if it's operator and ask them to make, to, to, to.
**jea** 36:47 Yeah.
**Mikołaj Świątek** 36:47 And now somebody else is coming in for us, Do they really need this?
Well, yeah, but the…
**jea** 36:54 I think the difference was that at the time, it was not a YAML… it was not a zero-dependency YAML dependency. There was another… Larger dependency that was causing issues I'm forgetting exactly what it was, but there was, like, another dependency that was heavier, if I'm remembering correctly.
But… alright, I'm proven wrong. I'll take the… proven wrong by my own… my own history. I'll take the… I'll take the L.
**Mikołaj Świątek** 37:26 So, the… the issue… I… I like the issue, in… in Zoom chat. If you have opinions on it, because there's a… there's a, There's a contributor here who is saying they're gonna put up a PR showing how it could be, made into its own module, which I am quite happy to look at, personally.
I am…
**jea** 37:52 Yeah, I support it.
**Mikołaj Świątek** 37:54 Is anyone, like, here clearly against at least trying it?
To see how.
**jea** 37:59 I'm not against trying it.
If it isn't terrible to maintain, I think it's fine.
I remember, I think when we looked at this last time, Mikolai, there was, like, some, recursive, dependency thing that we couldn't figure out. We might have sorted that out now, but I remember that being something that happened with this path.
**Mikołaj Świątek** 38:24 I… I… so… I don't think we tried to make it its own module. I think we tried to move some of the logic out of it somewhere else, and that was problematic because of, like.
the code gen, like, the Kubernetes API code gen was doing, yeah. Controller tools were… wasn't happy about some of these being…
**jea** 38:48 Yeah, yeah, that was exactly it. Yeah, that was exactly it. But there was also a recursive thing where, this is why I split out all of those config generator things, because all of that was in, the webhook… the APIs package before. And then we moved that to internal To depend on it, and then this was breaking. Arthur, did you have a comment on that?
**Arthur Silva Sens** 39:19 No, my chat somehow clicked. I have no idea how that happened.
Sorry.
**jea** 39:26 No worries. All good. But either way, I'd support it.
**Mikołaj Świątek** 39:34 Alright, I'm gonna comment. I'm gonna comment.
On this issue, and tell… tell this person that we will happily, happily look at their proposal.
**jea** 39:57 Cool. Well, do we have anything else?
**Mikołaj Świątek** 40:00 I don't think so.
All right. Thanks, thanks, guys. Have a… have a nice evening slash morning slash afternoon.
Everyone.
**Arthur Silva Sens** 40:16 Likewise. Bye-bye.
**Mikołaj Świątek** 40:19 Cheer.
**ploffay** 40:19 Next day, bye.
