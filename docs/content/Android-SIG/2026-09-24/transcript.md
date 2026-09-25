SIG: Android SIG
Date: 2026-09-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 02:46 Hey, David.
**DavidGrath** 02:52 Hello.
**Jason Plumb** 02:57 Thanks for joining.
**DavidGrath** 03:02 Thank you.
Jamie and Hansen said they'd be out today.
**Jason Plumb** 03:33 Yeah, okay.
Thanks for the heads up.
I just… I'm just logging on, it's 8 o'clock in the morning here, so I haven't seen anything yet.
Yeah, they must have a company thing going on.
Hey, Ben.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:07 Hey, guys.
**Cesar Munoz** 04:10 Hello.
**Jason Plumb** 04:11 Hello, Cesar.
I guess I'm gonna turn video on.
We'll give it one more minute.
If anyone has some topics that they would like to throw into the agenda, it's pretty open, so please feel free to do so.
Alright, well, it sounded like, Jamie and Hanson would not be able to join today, because they have a conflict, but let's go ahead and just peek into this one, because maybe it's something we can discuss without Jamie, or… Hanson here.
Yeah, custom processors and samplers. The question is, what would the DSL look like?
It's cool.
Yep.
**Cesar Munoz** 05:56 Yeah, I think, I think… That's fine. I mean, we've already discussed this a couple of times ago.
And before…
**Jason Plumb** 06:05 Yeah.
**Cesar Munoz** 06:09 I do remember why we needed the processors.
I'm not sure if the sampler… well, it's probably also nice to have it there.
**Jason Plumb** 06:32 Yeah, so they've proposed kind of, like, the two approaches, right? The way that Core does it is CORE says.
We're not going to give you configure methods for every little single thing that you might want to customize. Instead, we'll give you one that allows you to customize the tracer provider, and one of the ways you can do that is by adding processors.
Right, so it's a much higher level API.
**Cesar Munoz** 06:53 summer.
**Jason Plumb** 06:54 Much bigger hammer, yes.
And the other option is to provide individual, more granular configuration items.
Which, over time, ends up becoming a lot of… A lot of stuff to carry along.
a lot of API surface. This is a smaller API surface with the noted, maybe, problem in that it could leak some other builder interfaces into the DSL. I think this is manageable, and I think that we might be able to put a facade around those APIs if we wanted to.
**Cesar Munoz** 07:33 Yeah.
My only concern with the first one At least, if it is exactly as we have it for the builder, is that… somebody can essentially… I think they can override everything that we add in the agent.
That way.
**Jason Plumb** 07:53 And then you worry about ordering.
Right?
**Cesar Munoz** 07:56 Yeah… Yeah.
**Jason Plumb** 08:02 Yeah, it's true.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 08:03 I mean… if you're exposing the API via the agent, we can, ensure the ordering, right? But…
**Jason Plumb** 08:11 We can, but we have to document it, right? Because if you're reading how a user is using the DSL, it could be confusing if they both set a tracer provider customizer and do some other thing that conflicts with their previous thing.
Okay. Right? Because this is… this is a pretty high level…
**Cesar Munoz** 08:30 Yeah, essentially, you can, for example, use the DSL to configure the session, something about the sessions that we do. In the agent, And then, if you… add a Treasury provider customizer that Doesn't return the… The… the item that it… That you should customize, and it still returns a new one.
then essentially nothing else that you add into the DSL matters, because this will override it all.
**Jason Plumb** 09:05 It's true.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 09:06 Right.
Is there a way for us to do it, like, in a chain fashion, where, like, we apply all the previous processing, like, and then hand over the object where they can modify it, but… I mean, in that case, like, they would have to deliberately remove something to mess up.
**Jason Plumb** 09:34 Are you suggesting that the implementation of the initializer would do all of the internal stuff first, and when… before we are kind of done, then we pass it to the user to do extra customizations on?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 09:48 Yeah.
As a last step.
**Jason Plumb** 09:54 Maybe, but that… I think that central thing, whatever that… object is, I don't know that it exists, other than it might be the Roam Builder, and we didn't want to expose the Roam Builder.
**Cesar Munoz** 10:10 I will lean more towards the second one.
**Jason Plumb** 10:14 Yeah?
**Cesar Munoz** 10:16 Because I think it's easier to… It's more difficult for people to make a mistake That way, and also… It's probably easier… Later to migrate.
to… to… to the Kotlin APIs, too.
That way.
**Jason Plumb** 10:44 Okay, so you're thinking about the Kotlin APIs. I wonder if Jamie is as well.
Why can I not find a tracer provider customizer in Core?
Is that not the right name?
Tracer Provider Customizer? Let me just check an IntelliJ, because that's usually faster for me.
**Cesar Munoz** 11:06 Sometimes GitHub doesn't… return stuff that I… that is there, you know? I've seen it happen before, so maybe it's the case.
**Jason Plumb** 11:16 Oh, it's an… yeah, because it's… it's probably this thing. Let me show you.
It might be… it might be… this thing. Auto Configuration Customizer Provider.
Which gives you one of these.
I think this is the highest level.
**Cesar Munoz** 11:36 Right. But this is not the one that we use in Android, though.
**Jason Plumb** 11:41 What's the one that we use?
**Cesar Munoz** 11:42 I think it's custom.
Let me see.
Yeah, no.
**Jason Plumb** 11:51 So it's, it's Ban Exporter… is it this one?
Now it's export.
**Cesar Munoz** 11:58 I think it essentially is the same, but I don't think we just use this type.
There.
It's just kind of like… Copy-pasted that.
Or maybe that… that was before, I don't know which came first, but, you know.
**Jason Plumb** 12:15 So, do we have a tracer provider customizer?
**Cesar Munoz** 12:21 I'm looking for it.
**Jason Plumb** 12:24 No.
**Cesar Munoz** 12:35 Yeah.
It's here.
**Jason Plumb** 12:43 Let me see… Got it, yeah, so that… that maps onto, I think… So we… the builder… oh, we do return the builder… Tracer provider customizers, yeah, so that is… I think we end up hitting that SPI that I was just in.
Yeah, it's this. That looks the same, right?
**Cesar Munoz** 13:15 It looks similar, but I don't think we use this class from Java.
**Jason Plumb** 13:21 Right, right.
**Cesar Munoz** 13:25 Like, at all. I don't think there's any SPI or anything that we use later.
**Jason Plumb** 13:35 Yeah, I don't… I don't think we use auto-configure.
But it is… it is basically the equivalent of this. Yeah. Okay, so… You're inclined, Cesar, to go with the more granular approach.
And the question I… the question I wonder is… If we took the sum of everything you can do through this, and the sum of everything that you can do through this, how bad is it?
How many of these additional methods are we talking about?
Right? So one of the things you can do to customize the tracer provider is you can add a span processor. You can add a sampler. To the log one, you can add a log record processor. But my question is, what else is in here that I'm not aware of?
So it's, like, this class. We need to look at the surface of that class, I think.
**Cesar Munoz** 14:26 Yeah.
I think you can also add a clock… And what I… and
**Jason Plumb** 14:34 Oh, that's the wrong project.
**Cesar Munoz** 14:40 In the context propagator.
**Jason Plumb** 14:43 Yeah, so it's probably, like, a dozen?
Yeah, clock, ID generator, resource stuff… span limits… Span processor… Tracer Configurator… I don't even know what's in there.
There's a lot of stuff in here.
And while I agree.
**Cesar Munoz** 15:16 One way to say it is that we will expose all of that.
At once.
**Jason Plumb** 15:20 No, not at once, for sure, but over time. That's what I worry about.
**Cesar Munoz** 15:25 I mean, if we go with option one.
**Jason Plumb** 15:28 No, if we do… if we go with option one, we sort of get all that stuff.
to start with, I think.
**Cesar Munoz** 15:34 Right, which essentially would mean us exposing it all.
**Jason Plumb** 15:40 Yeah.
**Cesar Munoz** 15:41 At once.
**Jason Plumb** 15:42 Yeah.
I guess what I… I guess what I also like about number 2 is that it's more fluent. Like, part of the DSL is to be, like, human-readable.
Like, to make… like, you should be able to read it and just say, like.
hey, I can tell what it's configuring. And with these, I feel like the… I don't know, like…
**Cesar Munoz** 16:05 go deeper.
**Jason Plumb** 16:06 the kind of, like, stacked nomenclature, like, you know, like, you already have to have, like, a mental context for what a tracer is.
And then you have to have a context in your brain, like, for what a tracer provider is. And then you have to say what a tracer provider customizer is, and then you have to think about what the customization's actually doing, and it's, like, this weird, like, abstraction stack that… can be complicated to read, I think. Versus, here's my sampler, right?
**Cesar Munoz** 16:34 Yep.
**Jason Plumb** 16:39 So there is another issue, apparently.
No, it's just the same issue. What are they linking to?
Linking to the same issue.
**Cesar Munoz** 16:56 What I do remember… Let's just… Off the top of my head, people asking for are ways to filter signals.
Or,
**Jason Plumb** 17:07 Yeah.
**Cesar Munoz** 17:07 Black stuff, and… I think probably sampling.
But aside from those use cases, I don't… think… I also don't see… Like, if I've seen people asking for other stuff that is in the customizer, then maybe… We can say, well, probably, but then if we have to keep on adding stuff.
Over and over in the future, then what's the point of Going slowly… Item by item, but… really, I think mostly what I've heard is people asking for a way to add processors.
So I don't think there will be much else.
to ask.
**Jason Plumb** 17:53 Okay.
Yeah, there's no reason that we need to maintain this parity either, right? Like, we're a different project. Even though we're layered on top of it for now, we expect to be layered on top of Kotlin, and so… Was that… was that also one of your points, Cesar, as you think that this is probably leading us down a better path to be…
**Cesar Munoz** 18:13 Yeah, I mean, if there is a very niche… niche… niche?
niche. Use case that… people, thank you. That people need the first option for That, for whatever reason, is not… We can have it. …align with whatever… the Kotlin… APIs allow for configuring later, or not in the same way, then… You know, it will probably save the, discussion around, you know, but this was working in Java, or why don't we have the same, exact same thing in Kotlin? Which… I guess another way… A counterargument to that would be, well, it's an opportunity to know what we can add to the Kotlin API.
But, you know, it's… I just don't see… I don't know, I see more problems than benefits.
Exposing it all at once.
**Jason Plumb** 19:16 I think you've talked me into it. I think I like 2 better.
What does anyone else think, if you have an opinion?
**DavidGrath** 19:32 I also agree with Sue, because I also think it more closely aligns with eventually moving over to costly.
**Jason Plumb** 19:43 Cool, yeah, okay, so, sounds like we've got alignment so far.
Just adding a few notes… Okay, so I'll take that as a follow-up item, too, to just sort of comment that we talked about it a little bit, and if anyone else wants to add their two cents, that'd be a cool place to do it.
**Cesar Munoz** 20:31 Thank you.
**Jason Plumb** 20:34 Cool, and… you know, Jamie might have some other opinions. He, you know, he kind of instigated this, so maybe he has thought about it longer, and… More thoroughly than I have with my 8 AM brain.
But, yeah, sounds good. I think we're… I think we've gotta start.
Cool, let's move on to David's thing.
This was out there for a long time, wasn't it?
**Cesar Munoz** 21:01 Yeah.
**DavidGrath** 21:03 Oh, yeah, that's a wrong sign.
**Jason Plumb** 21:08 Cool, yeah, this is great. I'm glad you were able to come back to this. We should give it a review.
Because we talked about this a long time ago, yeah, so it was reorganizing the gesture instrumentation, so there was a… there was, like, name clashes between Click and Common, because there was some other restructuring that may have happened at the same time.
**DavidGrath** 21:30 Not exactly. The issue back then was different from now. So the issue is that… It most likely clashes with Compose Click, because the last segment shares the exact same name.
And it also has that same issue with the top-level common API. These issues are particularly with the demo app, I think, not with the… Not with the modules themselves, but specifically with the demo, I couldn't try to build.
**Jason Plumb** 21:56 Okay.
Oh, and then Ben's already looked at it, that's great. Okay. Cool.
**DavidGrath** 22:02 Oh, new comments, I didn't check. I checked them out.
**Jason Plumb** 22:06 Yeah, I mean, in due time, no worries. Yeah, that's awesome. Thanks for letting us know about it.
**Cesar Munoz** 22:13 Just one thing that I… Saw from Ben's comment.
Yeah. Just… I… it's… I haven't taken a look at it.
It's just that from seeing this line, it sounds like… David… Managed to create a subfolder.
For the view-related, yeah, input stuff in there. That was actually something I suggested.
Cool. Just to try and keep, things… Tidier, at least for somebody… someone taking a look at the, and the project.
But… but yeah, it does… it does cause it that… thing that Ben has mentioned, that then the artifact ID is still… Do you dash something?
Which, I think it's fine.
But, yeah, it's up for debate.
It's been a while since I didn't take a look at this.
And frankly, this week has been… Why BC? I really haven't had a chance to take a look at it.
NEPRs, really. Sorry about that.
Sorry, Ben, you were gonna say something?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 23:23 No. I think… I just wanted… I just brought this up because I don't know if this is the problem we are trying to solve. I did not have background, like, what was the original issue.
But, like, just David mentioned that, like, there is some conflict in the demo app, so… Yeah, that's… I think if the other one is named Compose Click, I think we are covered here. We don't really need to change anything, like the, directory structure changing Definitely helps, but yeah, the conflict, I don't think that's changing with this particular change. We have not done anything for that.
**Cesar Munoz** 24:04 Got it.
**Jason Plumb** 24:08 Well, yeah.
**Cesar Munoz** 24:08 That was it.
**Jason Plumb** 24:09 This is… this is still a really unfortunate thing in the demo app, but it allows the two projects to be truly separate projects, but only depend on… these modules from the parent when needed, but this sucks. I mean, it is what it is, but… And I've never loved this.
And I think you can… I think you can call it any name you want, right?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 24:34 It works.
But defeats the idea of, like… It works if you are always substituting, but that's not the idea. We want to be able to, you know, point to the Maven artifacts also, right?
**Jason Plumb** 24:47 Totally. Yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 24:49 So, one thing I've seen is, like, in a lot of these kind of scenarios, the demo app is a top-level module. I think we have it as a subfolder, so that's why, where all this comes from, I think. If we can have it as a top-level, parallel to all the other, modules, I think we can have a direct dependency, and then, like, more like an Excel condition, where do you… do you want to point… build it from source, or from Maven Artifacts? I think that… that would be a cleaner approach.
Right, maybe. I think?
**Jason Plumb** 25:22 Yeah, I totally follow what you're saying. I… I think one of the original intentions was to move this out, and so by having it as a separate project, we were trying to minimize the number of dependencies, and that stupid mapping is, like, where we've made the concession. Like, all of the sort of dependencies are here, and you can kind of see them.
And… I don't know, I mean, I don't know.
**Cesar Munoz** 25:51 Yeah, moving it outside of this project will… Allow us to remove that.
pack.
**Jason Plumb** 26:02 Yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 26:03 Do we want to do that, though? I think that is, like, it helps to run this demo or build as part of the CI, and, like, I think that… make… it's… I think it's good value, keeping it here. What is the reason to move it out?
**Cesar Munoz** 26:21 There's good questions.
**Jason Plumb** 26:22 go ahead. I can, I think I can answer it if you want me to, but go ahead.
**Cesar Munoz** 26:28 Well, what I remember is that there's, there's an OpenTelemetry demo repo, which is, like, nice for people to see everything, every demo for OTL there.
And… I think that was… that's the one that I remember, to be honest.
**Jason Plumb** 26:47 Yeah, that's the main… the main… well, so there's… I think there's two goals. One is to, like.
reduce the overall size of the Android project. Like, the demo app is, like, a chunk of code now, and while it is really useful to, like.
Try new features, and see what the telemetry looks like, and all that stuff.
there's this whole other OpenTelemetry demo that's mostly a web front end. I don't know that they have any other front end, and so… Putting the mobile app in there would allow people to really see additional depth for the OpenTelemetry project, especially when it comes to client telemetry.
So that was the idea, is to let it interop with all of the real services, too, because, like, if you go… if you dig down into the code, a bunch of that stuff is faked out, right? It's not hitting real services, and so we're missing some instrumentation that we could let… could have leveraged, specifically, like, HTTP stuff.
Because we…
**Cesar Munoz** 27:40 That's…
**Jason Plumb** 27:40 Because we didn't want to repeat all of the service infrastructure that exists in this other project.
We repeated some of it. Like, we have a collector, and we have…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 27:49 Yeah.
**Jason Plumb** 27:50 Jaeger.
Yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 27:52 I ain't… Yeah, go ahead, Cease.
**Cesar Munoz** 27:56 Also, I think it will make the demo app, Like, more realistic in the way that… because right now, what we're doing is essentially hard-coding its dependencies, but we probably don't do them all, and if we don't, then things break.
And… I mean, there are other approaches, probably… Like, detach the two… Projects, even though they are in the same repo.
and then do first a local Maven deployment, and then that way, kind of, we have the… local deployment available for the demo app.
It's a two-step process.
It sounds a bit overkill to me, but it's fine.
I mean…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 28:50 No, no.
**Cesar Munoz** 28:50 Yeah, I think it's nice to have.
at least the… We have some end-to-end tests.
Forever PR, with the demo app.
If we do that, that's probably worth keeping.
That could be one reason to keep it here, but…
**Jason Plumb** 29:06 I don't… yeah, I don't remember those. Do we? I don't… I don't know that we do.
Do we?
**Cesar Munoz** 29:13 I, I, I don't remember.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 29:18 So, some of the reasons we just talked about, I think we can still do it. Like, we can achieve those by still maintaining this in the repo. I'm concerned to move it out because it's a purely Android you know, code, that we don't want to put in another repo and then maintain it separately. I also feel like having a demo app, you know, definitely helps us to make sure that we are not breaking any APIs. If there are any issues, that then CI will catch it.
you know, if some public API surface change, or some incompatibility with some versions, we… it kind of serves as a QA for us. I found it helpful while making changes.
we… the… the local may even publish, like, it, that, that we can still, do with, the project in our repo, I think, just maybe, move around some Gradle configuration.
But yeah, I understand the desire to integrate with the, larger, like, the backend.
But yeah, I think it also depends on, like, what is the real use case for this.
It serves as more of an integration test.
That's how I saw it, because it was originally part of the repo.
But, like, if you really want to have a demo, you know, showcase, yeah, maybe then moving it out, is a better idea.
**Jason Plumb** 30:50 Yeah, I mean, it's kind of serving two purposes. It's a showcase, but it's also, like, a contributor tool, like, and we use it, like, contributors presumably use it, and I think also people that are curious about the project, they come into Android, and they see it, and they're like, oh yeah, I can just spin up this demo app and see how it works, and… get… get very, like, good examples of how to use the DSL and the other components right in the same codebase as the… as the agent, right?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 31:19 Yeah. Like, putting it somewhere else, I think… you will… you're… as you're making changes, this… you'll have to publish a version to update the… if it's in other… some other repo, right? Like, you have to update it once the release happens, and then… there's always that gap, like, somebody has not yet updated it, and then it goes out of sync, so that is the risk. And I feel like when you're publishing a source demo, like.
who has the expertise to run that, if it's not totally Android-related, right? Like, if it's in a common demo repo, like, are Android folks gonna find it there and run it there? Or, like, is it better, you know, package within the Android library repo.
**Jason Plumb** 32:07 Yeah, that's a good point, and then I think to… just to add on to that, I think one of the challenges right now is that this demo is starting to get a little top-heavy. Like, it has… So many different moving pieces in it that, you know, one more… until they've, like, really kind of figured it out.
I don't know that there's a good… I don't know that it's yet a good time to throw another project in there. Like, they were really open to this idea, and they were stoked to see that, like, we have a demo, and it would… it kind of… it follows the same UI pattern that they've established, like, it's the same astronomy shop, and it's got the same backend service… we faked them, but same idea for backend services.
But, like, there's so many moving pieces that maybe… I don't know, we should talk to them again about it.
**Cesar Munoz** 32:59 I think you…
**Jason Plumb** 33:02 Yeah.
**Cesar Munoz** 33:02 Yeah, I think you two kind of have just convinced me to not move it.
**Jason Plumb** 33:08 What… what do we think about opening a tracking issue for this? Does somebody… can someone do that?
**Cesar Munoz** 33:14 I… I can do it. I think there is an issue already.
**Jason Plumb** 33:17 Oh, yeah?
**Cesar Munoz** 33:18 Let me check.
**Jason Plumb** 33:18 Okay.
I'll just say that you'll open one if there isn't.
**Cesar Munoz** 33:25 Yeah.
**DavidGrath** 33:29 There is one, I think. It's quite old, I remember.
**Cesar Munoz** 33:38 Yeah, there is one.
It's here.
**Jason Plumb** 33:43 Okay, you have it. Good, lovely.
Yeah, cool, that's great. Okay, let's just do that, and then we can continue discussion there.
I want to make sure we have time to look at these other PRs.
We ready to move on from demo app?
And we will look at David's thing. That's how we got talking about this, was the demo app.
was through David's PR. For the view click stuff.
Alright, I'm gonna do some housekeeping, this tab's out of control.
Okay.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 34:23 Yeah, so this, this, I think, started off, as a request to, filter, some, you know, filter some URLs.
From HTTP instrumentation, that was the original issue raised.
And I was, I think initially a little ambitious, trying to modify the instrumentations, but then, like, I understand, the challenge with that, so I kind of settled on, like, having the most value with the least amount of changes. So, what I, what this new PR… So last week, I had Come up with a plan to… a plan that involved updating the instrumentation, so since then, I've opened a new PR that just filters the spans.
**Jason Plumb** 35:09 Okay?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 35:10 That… that's what this changed us.
it, it exposes a DSL to, Allow only certain hosts to record spans.
And this is done without, like, we have an API to reject spans for any, given post, and that's what it uses, so there is no instrumentation change. This PR is, fully self-contained for that.
Yeah, I think I have a couple of approvals, but I would, typically like to collect feedback on… so, the, the naming here, it says HTTP telemetry, But it just filters out the spans, so if you have any better suggestions on how to name this, I'd appreciate that.
Any, any other questions? I don't know if I… Because we discussed this in the past, and so I, brief explainer.
**DavidGrath** 36:12 It was a very minor.
**Jason Plumb** 36:16 Go ahead.
**DavidGrath** 36:17 Lizard.
There's a very minor issue that I know this is going to be addressed in the future, but it's still at the back of my head. As it is right now, will it potentially break redirects? I'm not sure if it will, but I'd like to confirm that.
**Jason Plumb** 36:31 That's a good point. Does it break redirects?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 36:35 It, it does not, I, I think, Okay, I need to check that. Like, the initial, PRI was handling redirects, because, like, I had access to the extermination. So in this case, I think, I, I think it, does not… So, if, if… where the actual telemetry, or which is the actual endpoint you hit, I think that's based on… the spans are created based on that.
So, the actual, traffic goes through, and then you create a span, and then you get an option to whether to keep that span or not. And that's where I, plugged this in, so I think the redirects are included.
But I can, I can verify.
**Jason Plumb** 37:23 That would be, yeah.
**DavidGrath** 37:24 It's a good…
**Jason Plumb** 37:24 point. I think it would be good to verify. Go ahead, David.
**DavidGrath** 37:28 Yes, but I saw that in your discussion on the issue, that's what made me bring it up.
Say that out.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 37:33 Yeah.
Yeah, because I was, you know, limited by the API here. I did not… there. In the last discussion, I was, like, trying to work on the instrumentation, so there, definitely had the opportunity to, you know, support redirects.
**Jason Plumb** 37:59 Yeah, that's really good to think about. Thanks for bringing that up.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 38:04 Yeah, I'll add it to the…
**Jason Plumb** 38:06 Yeah, I wanted to make sure that this was both inclusion and exclusion. So, this is inclusion, right? You can say, I only want Is there a way to exclude yet, or do we think that's an add-on later?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 38:21 If you, if you think that's nice to have right now, I can add that.
I thought the most common use case would be just to allow specific Because, like, exclude list, like, that can, like, quickly grow out of control, like.
**Jason Plumb** 38:37 I thought it was the other… so I honestly, I thought it was the other way around, because I thought it was, like, you have some analytics, like, SDK that's, like, sending stuff to Google or whoever, and that's what you wanted to exclude from being, traced.
So you have all of your, like, domain-specific, like, application-specific microservices, and they could be behind a bunch of different URLs, but then the analytics one, you don't want instrumented, because it's, like, wasted telemetry.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 39:01 So then, in that case, I would need to understand what all APIs, or, like, what all hosts, like, my third-party SDKs are getting. But in this case, I just need to know what my services, what is the endpoint for my services. So, easier to track that than, like.
you know, track all the third-party SDKs and what their, posts are.
**Jason Plumb** 39:22 I hear you, but I think the use case was, I look in my dashboard and I see a bunch of spans going out to… I'm just gonna say Google Analytics, but it's whoever, right?
And I'm like, oh, well, I'm just wasting my telemetry budget on that… on those things, because it's happening from all these apps all the time, so let me just get rid of those spans. And that's one filter, then, like… That, like, you see it in your dashboards or in your data, and then you go and add this one filter, and then you're… you just eliminate that one source, without having to, like, allow list a whole bunch of other stuff.
So it's like, deny list versus allow list.
But I don't want to expand… I don't want to expand the scope of this, because I think both use cases are valid.
**Cesar Munoz** 40:08 My concern with both… Let's say that we then add a deny list later.
Is, you know, which one takes precedence once there's a clash?
Yep.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 40:21 I think, like, it has to be either one. I think, like, that… yeah, that can definitely complicate things. Even in the initial design, it was either of those, like, either a allow list or a deny list.
Or, like, allow everything.
**Cesar Munoz** 40:37 What if we… don't… it's an idea, really, it's not a blocker, and so far, the way it looks like, I think it's fine.
But now that we're discussing about this, What if we don't… Like, an idea could be that we don't go with any kind of list.
And instead, we allow users to provide a predicate.
You know, and then we provide them with the… with the URL, probably, or just the domain.
And then they return true or false.
for each.
And true, meaning… Trace it.
And that way, we kind of have both Mechanisms in a single… Place.
That's an idea.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 41:29 Yeah, definitely. Yeah, I was trying to keep it simple, but, like, if you feel like there's a use case for that, definitely, yeah.
So, just… do you prefer to give the… I think we just get the host address, it's a server.address field, so I think we can expose that to the, Yeah, developer, and then get a value out of it, like, get a response.
**Jason Plumb** 41:58 And where does the actual filtering happen again?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:01 It's in the initializer.
**Jason Plumb** 42:04 Okay.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:06 yeah.
**Jason Plumb** 42:08 So we create one of these, and then… Where did we use that?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:14 It's in line 90, so…
**Jason Plumb** 42:21 Okay… Sorry, so we have this thing… And we created… oh, because the instrumentation is in here.
Oh, so it does touch the instrumentation, but this was already there.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:38 Yeah, I agree. No modifications, yes.
**Jason Plumb** 42:42 Got it.
Yeah, so it's still wired in through the instrumentation, it's just there's a DSL for it now.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:51 Yeah.
**Jason Plumb** 42:52 Great.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 42:54 No, this is the instrumentation configuration that, like, the agent exposes. When you're talking about instrumentation, we didn't want to modify the upstream instrumentation. That's what we're talking about, right?
**Jason Plumb** 43:07 Yes.
So, where… so where does the actual filtering happen?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 43:14 so the filtering happens within the host filter, That… Yeah.
**Jason Plumb** 43:24 And then, who calls rejects?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 43:28 That, that was in the previous file. So we get this, we get, like, I pass in the span data.
And, like, look at the… post.
**Cesar Munoz** 43:39 There is…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 43:40 Yeah. Lightning.
**Cesar Munoz** 43:41 So this essentially looks like what I was mentioning.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 43:45 Yeah, it's just,
**Cesar Munoz** 43:46 it receives the spam data. Spanish.
We don't want to provide the whole thing.
**Jason Plumb** 43:52 Yeah.
**Cesar Munoz** 43:53 That could be… Yeah, I was essentially… Proposing… exposing something like this, but instead of providing this whole span data, just… whatever we think is needed to filter an HTTP spam.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 44:12 So, given that, like, we already have a way to get the span and filter this, like, do you still suggest having that predicate mechanism, or, like, a simpler API where we accept or, like, accept an allow list or a deny list.
**Jason Plumb** 44:32 Yeah, the predicate would allow you to do both.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 44:36 Okay.
**Jason Plumb** 44:37 But with more burden on the user to implement that, right?
But it's not that… I don't know, it's not that much work.
Is it?
Let's see, so… We get spam data.
Which is read-only, right?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 45:01 Yeah.
**Jason Plumb** 45:02 And…
**Cesar Munoz** 45:03 Yeah.
**Jason Plumb** 45:06 Only for client spans, only for…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 45:12 So this, this we can do. Yeah, we can… All those checks we can do, and then expose just the server address.
Even then, like, I do some Unicode conversions, just to normalize it between the OKHTTP and the HTTP URL connection.
**Jason Plumb** 45:35 Alright, where does this come from? I've never encountered puny code before.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 45:41 This was, brought up in review by Vishwan. I, I think… This is something we are, like.
I don't think anywhere else we are doing this, but, like, I added it here because, like, the failure could be silent, or, like, you know, everywhere else, like.
when we accept a URL, for example, where all we want to send out, traces to, right?
we definitely validate that before we launch our… it's caught immediately in testing, but if somebody's doing some sort of dynamic, you know, whitelisting, or, like.
allow listing, based on some configuration they pulled from the backend. I want to make sure that, like.
they see the error, or, like, at least we flag it as a… as a log, at least. That's why I added this.
**Jason Plumb** 46:35 Cool.
Is there a way to… Sorry to keep belaboring this, I know we're a little bit low on time, there's a few more things on the agenda. Is there a way to mark parts of the DSL as… experimental, or as new, like, incubating? Like, we have incubating and upstream. Do we have a way to mark certain parts of the DSL as… I think we have an experimental?
**Cesar Munoz** 47:04 We do, and I think there's another PR, probably from Vishwan, where… We already do that.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 47:12 Okay.
**Cesar Munoz** 47:14 It's an incubating… Annotation.
I think.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 47:24 Yeah, I'll definitely update that.
So, are we, So I should implement the predicate model.
Or…
**Vishwan aranha** 47:36 Yeah, that's the 2061. I think everybody has reviewed it. Just, yeah, that's on the agenda, too.
**Jason Plumb** 47:43 Dude.
**Vishwan aranha** 47:47 Sorry to interrupt.
**Jason Plumb** 47:49 No, no, you're good. So, for custom storage.
**Cesar Munoz** 47:54 So… I'm not gonna block it on the predicate.
Ben, I'm just mentioning it in case.
you know, after the discussion with the allow list, deny list, what I would think is that if in the future we do need a denial list.
Having them both, coexist. I think it's… it's… it's painful.
So… That's… that's essentially why I'm mentioning this, but… Yeah.
Yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 48:26 I can.
**Cesar Munoz** 48:27 Honestly, don't know what's the most common.
Need for users, either to deny stuff or allow stuff, so…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 48:36 Yeah, this was just based on my intuition. I… we don't have users or, like, any feedback, so, I'll not pretend that I know. I can go with the predicate model.
**Jason Plumb** 48:48 I think the original issue was filed by one of my colleagues, and I think that she explained it as, like, an analytics thing that they were trying to avoid. I don't know any more details other than kind of what was said maybe a month or two ago.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 49:01 Okay.
**Jason Plumb** 49:02 I also don't want to block this, but I do want us to be… And I hate to, like, put friction in the way, but I do want us to be a little bit thoughtful about new API surface in the agent, specifically because it is marked as stable.
And so users that have that have an expectation of stability, and if we add a new API to the DSL that we then want to change, it becomes much more difficult. So that's why I'm suggesting maybe experimental.
So we get it in with experimental that allows us to make breaking changes to it in a way that's, like, you know, the user would have to opt in and acknowledge, like.
very purposefully kind of acknowledge that they're using an experimental API that can change.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 49:45 Absolutely.
Yeah.
Yeah, with that, I think it makes sense to use the predicate model, so I'll go ahead and change that.
**Jason Plumb** 49:53 Awesome, sounds good. Love it. Thank you.
**Cesar Munoz** 49:55 Thank you.
**Jason Plumb** 49:56 Yeah.
So, Vishwan, what are we talking about?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 49:59 sorry, like, I would also appreciate some feedback, like, I currently named HTTP Telemetry, if there's any other names.
**Jason Plumb** 50:07 Oh, yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 50:07 Please let me know. Thanks.
But just cover spans.
**Jason Plumb** 50:15 That's… that's probably all you wanted to talk about today, and we went off the rails, sorry.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 50:21 But, like, good feedback, thank you.
**Jason Plumb** 50:23 Yeah, I think I agree with Jamie, but I don't have a good name off the top of my head, so we'll talk about it.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 50:28 Okay.
**Jason Plumb** 50:29 Cool.
Okay, Vishwan, what's up with this one?
**Vishwan aranha** 50:33 So, I've got, like, two quick items, like, first 2061, which kind of is piggybacking on the conversation, like, it adds, like, the custom session storage through DSL, and I'm not incubating with the existing defaults unchanged, so… It has, like, all the… I think you guys had the chance to review it, most of the approvals are there, so is there anything else needed before it can land?
**Jason Plumb** 50:58 I assume that we are just dragging our feet intentionally, because this is, like, you know, a new API surface, and I have been very inattentive due to other stuff happening on my end at my company, so it's probably just waiting on me. But also, it's had some time to cook, and there's probably nothing Preventing it from being merged.
**Vishwan aranha** 51:20 I just wanted to bring it to you guys' attention, that's it.
**Cesar Munoz** 51:24 Thanks, thanks for bringing it up. To be honest, I… I… I forgot… I didn't… I thought this was… was merged, so… yeah, I think it's fine to get merged, and… And yeah.
**Jason Plumb** 51:36 do…
**Cesar Munoz** 51:36 And it's also… you marked it as incubating, so it's… It's fine.
**Jason Plumb** 51:42 Is that the one?
**Vishwan aranha** 51:44 Yes, that's the one.
**Jason Plumb** 51:45 Yeah, yeah, so, okay, so let's get that terminology consistent, because that's experimental.
Let's do that, right?
And I was gonna ask this question, it looks like it's already done, so yeah, that's great. If you guys have looked and reviewed it, and it's incubating, I'm good with that.
**Cesar Munoz** 52:01 Okay, so I… I can just merge it.
**Jason Plumb** 52:04 Sweet.
**Cesar Munoz** 52:05 Right away.
**Jason Plumb** 52:06 That sounds great.
**Vishwan aranha** 52:08 And this one was a behemoth, like, huge PR, with so many lines, and so I divided it into smaller chunks so it's easy to review, and hope that approach works well. I have, like… We cannot have, like.
branching strategy, so that's why, hopefully, the mermaid diagram and everything kind of explains it well. If any questions, feel free to raise it. Like, if you guys get a chance, you can review this when you have time.
**Jason Plumb** 52:41 Is there some C code in here?
**Vishwan aranha** 52:44 So…
**Jason Plumb** 52:45 This builds on top of it, though.
**Vishwan aranha** 52:47 Yeah. So, one behavior that I would like to confirm for this, like, if we can't acquire the lock, or, like, read the saved recovery state, a new crash that captures saved disabled to protect the, protect the, like, existing report.
So, are we comfortable with that, or should we, like, agree on a way to resume capture after, like, repeated failures?
**Jason Plumb** 53:11 So, like, you launch, or you're using the app and it crashes, and you launch it again, and it crashes again before the previous tombstone's been recovered?
**Vishwan aranha** 53:21 Yes, so, yeah, so that's basically what's happening. I have explained, the basic details, like how everything was panning out. So, if anything is unclear… Man.
**Jason Plumb** 53:35 Okay.
**Cesar Munoz** 53:44 And… and you're ready to… I see, it's still marked as draft.
**Vishwan aranha** 53:50 Oh, some of them, because I divided it into several chunks.
And, Jamie requested to make it smaller because it became a huge PR. And, so I made, like, 4 different drafts, and I added the order for that, like, I think 2081 is the first one to review.
And, from there, you can go to the other ones.
**Cesar Munoz** 54:16 I see.
**Vishwan aranha** 54:17 I think in the mermaid diagram as well, like, I have added the flow for it.
**Jason Plumb** 54:21 So, the contents of this PR are spread across these three.
**Vishwan aranha** 54:27 Yes. Got it. Because it was… originally, this was, like, a one behemoth of a PR.
**Jason Plumb** 54:32 Yeah.
**Vishwan aranha** 54:32 But then I divided it into smaller chunks so it's easier to review, because Jamie requested it would be easier for him.
**Jason Plumb** 54:38 That's great.
**Cesar Munoz** 54:39 Sounds good, and, and, and so you will… Prefer to, yeah, us to add the comments in those other three.
PRs.
**Vishwan aranha** 54:49 Yeah, feel free to add comments throughout, if it makes sense, because it's, like, distributed across.
And if you find anything, I can update that in a train. Like, it's basically a chain, but it doesn't appear to be as… because I kept it draft, but even… because… even by mistake, I don't want the draft to be merged in.
In out of order, so that's why I kept it like that.
**Jason Plumb** 55:12 Makes sense.
On that topic, we have a couple of minutes left. On that topic, Do you… are you all using the PR stacks in other projects, and do you like them?
**Vishwan aranha** 55:26 I saw them popping up, but I never used it. I was, like, afraid it might mess things up. That's what I can… Yeah, I see that popping up in GitHub every now and then.
**Jason Plumb** 55:36 Yeah.
**Cesar Munoz** 55:37 I haven't.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 55:38 I, I think it helps, But, yeah, sometimes if there is additional maintenance work once you merge, like, sometimes branches diverge. It's… it's a good visual… I mean.
aid, I think. Like, you can, see what's coming next.
But… Still definitely has the problems of, like, doing it how we used to do it traditionally.
**Jason Plumb** 56:02 Yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 56:03 But, like, in this case, I think it would have, like, provided us clarity what is the order, and, like, what we should have, checked first, I think.
**Jason Plumb** 56:15 Yeah. Yeah, because it's maybe less obvious when you see it like this.
Like, you kind of have to make… I don't know. It's not a feature that I've used, I'm curious about it.
We do have an option to add it to this repo.
And it changes the workflow slightly, though, because we're all used to pushing branches to our fork, and then submitting PRs off the fork.
you would have to push branches to the repo, which you're not currently allowed to do. But there is a setting now, like, across OpenTelemetry, that we could opt into.
That would allow approvers and maintainers to push branches for this purpose.
Which I'm like, I don't know, I don't see a… maybe enough benefit to do that. I know that Hansen really likes it.
But…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 57:04 It's not open to all, it's just the program.
**Jason Plumb** 57:07 Yeah, it would only be for maintainers and approvers.
Okay. To be able to push branches and create stacks. Because, the stacks thing doesn't work across forks.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 57:17 Yeah.
**Jason Plumb** 57:18 Yeah.
**Vishwan aranha** 57:19 And for my PR, I can make the review and, like, merge order cleaner in the descriptions, if that helps.
And I'm happy to keep the current fork workflow. We don't need to, like, change repository permissions just for this stack, I believe.
**Jason Plumb** 57:34 I mean, now that you've explained it, it makes sense to me, but maybe just a small comment here that's like, you know, this one will never get merged. 208.1 is ready to be reviewed, these other two are in draft until 208.1 merges. Just a small comment, maybe?
**Vishwan aranha** 57:48 Okay.
**Jason Plumb** 57:49 I think that's fine.
But had I come in here and not heard that from you, if I just came in blind, I would maybe not understand that.
**Vishwan aranha** 57:55 Yeah.
That's why I, like, wanted to raise it in the SIG, so… I saw GitHub uses this stack as well, but I kind of have a trust issue with GitHub, where it goes down every other day, so I don't trust what it offers.
**Jason Plumb** 58:10 It is true, it's been struggling lately, hasn't it?
**DavidGrath** 58:15 I mean, you would notice the break, but you had to go to get a discussion where Jamie told him to space it.
**Jason Plumb** 58:25 I didn't fully catch it, David.
**DavidGrath** 58:28 I said, you would notice you have harpotis.
You would see this split, but you have to go all the way down for the context.
**Jason Plumb** 58:37 Yeah.
Yep.
Okay, well, we are basically at time. We try and stop, like, 5 minutes before, just to give people a few minutes between meetings. Sometimes we're good at it.
We almost did, we almost got there today.
**Cesar Munoz** 58:59 Nice. Well, thank you.
**Jason Plumb** 59:02 Thanks to everyone, that was an awesome discussion.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 59:03 Guys.
**Jason Plumb** 59:04 Appreciate all the help.
**Vishwan aranha** 59:04 prospects.
**Cesar Munoz** 59:05 Isaac?
**Jason Plumb** 59:05 Yep. Bye.
