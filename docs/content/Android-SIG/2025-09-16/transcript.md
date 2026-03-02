SIG: Android SIG
Date: 2025-09-16
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/di0RROvf_BqMJc-YPLp9h_0VbTEbo18Zwc2PoxoF_uTwMj0eI36zIKNTinJEDRlK.6uLL4P0QLJCVT_Ws
============================================================

## Zoom Recording Transcript

Jason Plumb 00:00:30 Hey, Manuel.
Manoel 00:00:33 Hello.
Jason Plumb 00:00:34 Good morning, good evening, yeah, how's it going? Long time no see.
Manoel 00:00:38 Yeah, pretty good.
Quite a lot of work, but…
I think that's a good thing. I had a long summer break, so… Nothing to come to.
Jason Plumb 00:00:49 Yeah. It's finally winding down, though, isn't it?
Manoel 00:00:53 Exactly.
Still warm enough, but yeah, it's getting colder day by day already.
I go…
Jason Plumb 00:01:03 higher.
That's the template. Okay.
Well, it might appear on the surface that we have a light agenda today, but I think it's actually gonna be a big discussion, maybe, if we're talking about 1-0 and the roadmap to get there.
Which we started on this a little bit, last week.
So I bumped it up. If you have other agenda items, please feel free to add them, and we'll get to them today.
Yeah, so this discussion came up last time, just to sort of recap.
Right, so, like, what's the roadmap look like for a 1.0? There's some hesitation. We have a chicken and egg problem, right, where users are maybe hesitant to…
to use a version or a product that they feel is not stable, or that might change out from under them, or hasn't been battle-tested. And so…
that's the chicken part. The egg part is we also want feedback from people that are using this so that we can, adapt and make changes to the APIs and fix bugs and do all that good stuff to make it more stable, right? So we've got this, like, kind of…
challenge here. But I think it's… I think it's time for us to develop a roadmap.
Which means, what qualities, what features do we think need to be in place for us to deem something a 1-0? Because our next release, we could just call it a 1.0. Like, we have that autonomy, we have the ability to just call it a 1-0. It would be a little bit irresponsible, I think we want to be thoughtful about it, and…
Include feedback from the community at large, and… and that's… that's this group, so… Aside from…
Maybe starting a milestone. We certainly have that label.
Let's see…
I have everything that's not OpenTelemetry Android in my quick suggest.
Okay.
We have some issues that are labeled.
And required is… maybe we should rename this, because required, you know, is very strict. This is, like, what we're considering for 1.0 right now.
It's pretty short, and some of these are kind of high level, but I think that's our first list to talk about. Let me just link to this…
We don't talk about RCs yet.
So I think Cesar brought up a very good point last time, and that's, I think, the main…
The main thing is around the initializer and the agent APIs, like, that's… if that's kind of the main thing we expect people to be using, that's also maybe the… the newer, younger API out of the entire surface, maybe. With probably in the…
Instrumentation initialization being a close second.
But, yeah, what are people thinking about this list so far?
Some of these are pretty old.
Cesar Munoz 00:04:58 I think some of them are also already done.
Jason Plumb 00:05:01 Like, this one's.
Cesar Munoz 00:05:02 We just haven't closed them.
I think that one is done.
Jason Plumb 00:05:07 Yeah, like, if you use the agent initializer, you get OTLP by default.
Cesar Munoz 00:05:11 Yeah.
Jason Plumb 00:05:13 Okay Yeah, I think we can close this one.
Cesar Munoz 00:05:19 Yeah, me too.
Hanson Ho 00:05:22 I think we should figure out what things we want to prioritize as qualities for this, in terms.
Jason Plumb 00:05:28 down.
Hanson Ho 00:05:29 What we mean by stability, what we mean by…
guarantee API not changing, or at least without a major version. And then…
go through the lists that we have, of things, and basically trim them. I think…
like, to me, like, features really shouldn't be part of it, because I feel like
as long as it's viable, we can declare 1.0, and if it's a feature that we think is so important that we don't have, and we still don't have it.
I don't think a feature like that exists. I think you've been in production for long enough that really stability and API surface is really the two things we should think about.
Given that, I would say there's, like, probably a few things off the list that we saw that we could drop.
And maybe we should think about, what we can do to review, the existing code to make sure that we won't likely break, you know, the API, next week.
Jason Plumb 00:06:34 Yeah. Okay, I think, I think this is actually really important, because,
features… features that are missing are things that can be added, you know, later. Even with 1.0, it's not going to be breaking to add features, right? So, I think this is a great thing to keep in mind.
Mustafa Haddara 00:06:58 Yeah, I mean, to Hanson's point, like, if it was critical, we would have had it by now.
Jason Plumb 00:07:04 Yeah.
Yeah, okay.
But…
something like… I'm just gonna throw this out there, because I know it's a little in flux, something like disk buffering…
Like, if that is kind of a first-class feature, we would want to enable it by default, and if disk buffering isn't yet stable.
Should we call it stable?
So, do we want to work toward a stable disk buffering? I think the answer is yes. And then, once that's stable.
and we're confident in it, then, you know, but I guess, you know, features like this, can we consider other, things that we depend on? Can we be stable while depending on non-stable components?
Cesar Munoz 00:07:50 I think… we can… as long as the API
if I understood correctly, from what Hanson mentioned, which is at least what I
I thought he meant, and, and I, and I, and I…
Kinda like that idea. Is that the…
Well, or at least to me, the stability means that the API won't change.
We'll have breaking changes in, in, in the near future.
So… With that, my understanding would be that we can go we've… Even if we have
Not necessarily talking about this buffering, but even if we already have some features that Haven't been…
I don't know.
Battle-tested, if you will.
So, they might… they might have books, And, in, in their behavior.
I think it's still fine to go with a… to use it for a stable version, as long as
The way that you configure it.
won't change, you know, by fixing the bug in the future. It's like, if there's a bug and I fix it in a further version.
if that doesn't break the API, then… then we still can go, with version 1.0.
Hanson Ho 00:09:21 Yeah, I think for me, there's two levels of stability. One is API stability, which is, you know, I think what you're talking about Cesar. Another is just, like, the code implemented by default is battle-tested enough.
Not saying it's gonna be bug-free, because, you know, it's mobile, there's nothing that you could actually guarantee that. But we feel confident that enough people have used it in production.
And that we have enough test cases for the majority of usage, that there are no major issues that are left outstanding.
So, in terms of disk buffering,
Actually, it's a larger question that Jason's talking about. There's,
I think we can depend on something that is technically unstable, if we're confident that our usage of it is stable in terms of it does not crash, it works as advertised.
and that the API surface that we use to configure it is, stable. So, if… if…
If there's something to do with, yeah, I'll stop there.
So are we confident about the implementation, how much it's used? I think that's the question we should ask ourselves for this quote-unquote, not-yet-stable component, which is not the same as unstable, at least, you know, implication, I should say.
Jason Plumb 00:10:53 Yeah, so taking and borrowing your… what you were saying, Hanson, got me thinking about how some other projects handle it, and, you know, we have… we publish, you know.
A dozen, or 15, 16 different modules from this project.
They're all versioned together currently, and something that happens in, like, instrumentation, for example, is that…
Manoel 00:11:18 The instrumentation is at a stable version.
Jason Plumb 00:11:21 But, the individual instrumentations, I think, are not. Like, some components are published as alpha. Maybe I can find a way to show that.
Cesar Munoz 00:11:31 Like, country, you mean?
Jason Plumb 00:11:34 No, I think in the main… in the main instrumentation as well, I think there are alpha versions, not SemCom as a bad example.
But, like, just pick one of these.
Right? Even the… even the two O's, they have an alpha suffix, so someone who wanted to use, like, the Armyia library instrumentation, for example.
They're gonna be downloading something that's clearly marked as alpha.
And that's a component of the instrumentation, but if you go to, like, the agent itself.
You know, there's no… there's no alpha suffix on these.
Right, so the agent itself is more stable. The individual instrumentations have not yet been determined to be stable. I think the instrumentation API… do we have… I think we have an API?
Yeah…
Is it in here?
Yeah.
So, I mean, even with an API, there's a bunch of different components, but the API…
is stable. Like, the way you can tell that is by the alphas. I don't know if it's just listed in the repo anywhere, if you can just see in one… in one go, like, what components are alpha and which ones aren't, but this is…
I'm bringing this up because I think it's an… it's something that we should consider for this as well.
If we think that the instrumentation might be subject to change, certainly with
semantic conventions not being stable, and certainly with the shape of, like, certain events and stuff not being stable, it would be hard to claim that the telemetry produced is… is stable, and by stable, I mean not subject to change.
So, maybe in a first pass, we would consider adding alpha to some of these components, instrumentation being maybe an obvious candidate.
But I think our goal, I mean, the main goal in my brain is to get agent and core
You know, marked as non-alpha 1-0 stable.
And then…
the rest of it, you know, we can pick and choose. So maybe we should have a tracking issue for which components we think we want to be alpha? Does that make sense?
Hanson Ho 00:13:51 Yeah. Yeah.
By default, all of them.
Jason Plumb 00:13:55 Well, so that's… that leads into, like, this, like, we should… we should definitely have a period of, like, RC1, RC2, hey, we think we're… like, we're not gonna have any disruptive… we're trying to limit the amount of disruptive changes now that we're in RCs, like, release candidates.
And then, once we're happy with, like, RC1, RC2,
RC3456, like, there's no limit to that, but we should probably think about how many months.
We want to do that. In my brain, once we're happy cutting the first RC, I think, you know, no more than 3 would be ideal.
If we're doing monthly releases?
Oh yeah, this…
We also have to talk about that. So does that seem reasonable to people? Like, like, like, 2 to 3 RC?
versions… Assuming no surprises.
Hanson Ho 00:14:49 Maximum.
Jason Plumb 00:14:50 Yeah, okay.
Yeah.
I like that.
Are people feeling, like, pretty confident? Like, in general, I'd like to hear if people are feeling confident about this. Do you feel like it's being forced or rushed? Or do you think it's like, no, it's like, it's time to, like, really get serious about, you know, making this stable?
Cesar Munoz 00:15:12 There are a lot of modules. The only one that I feel confident about
Marking a stable is the agent.
Because it's got the… smallest API surface.
And so that means that we can expand it.
And I wouldn't have to mean breaking changes.
The one I'm the least confident about is Core.
Jason Plumb 00:15:38 Yeah.
Cesar Munoz 00:15:39 Because it's, it's quite messy.
But… I mean… I, I, I would think that if…
Most of users are… are gonna just… just want the… just want the, the, the, kind of, like, the plug-and-play experience, or the… the most straightforward experience. They will go.
To use the agent.
And if that's the case, I think…
Yeah, I'm pretty confident about that.
One, becoming probably one of the first stable modules.
there is just one part of it that I think it's… Not narrow enough.
Which is that… I think we provide the… I mean, If I were to…
Set one of these modules stable tomorrow.
it will be the Andri agent, but after Shrinking it a bit.
By removing the config object, That belongs to core, because right now, one of the parameters for the initializer
Is the core configuration.
Jason Plumb 00:16:56 Okay.
Cesar Munoz 00:16:56 I think it's kind of like a… it's a… it's a bit of a… it's a bit of a big ham, I think.
So, it's not like we might… we will never add it, but right now.
it's there. That would be the only thing that I would remove, and…
Jason Plumb 00:17:12 to this hotel room config?
Cesar Munoz 00:17:15 Yeah.
Jason Plumb 00:17:16 Okay.
Cesar Munoz 00:17:18 That will be the one change that I will add to the… well, and the PR that I have open, which makes the instrumentation config more straightforward.
So that's the one that I'm pretty confident about. The rest of them…
You know, I'm not sure.
Jason Plumb 00:17:35 Okay, that… I… yeah, I think I understand where that's coming from. So, you are hesitant…
To use this in a stable version.
Cesar Munoz 00:17:46 Like, to expose it in the… in the agents.
Upfront, yes, because it… Has a lot of stuff.
So…
Jason Plumb 00:17:57 Yeah, so this is the config that also contains the other configs. Well, really, right now, it's just disk buffering, but then some features that you can turn on and off, right? So this is a way for a user who's using the agent to decide
Yeah, I do want screen attributes, or I don't want screen attributes. And so, if that… if you don't want to include this in stable, there's got to be some other way of… for them to… to specify these things, right? Because not everyone wants screen attributes.
Cesar Munoz 00:18:23 Like, I will,
configs into the initializer, specific ones for the ones that we want to expose. So, for example.
If we decide that we want this buffering to be enabled in the agent by default, which is not the case in Core.
Right. Then… I will make the initializer
Set the disk buffering as enabled.
Jason Plumb 00:18:48 In the config, when, you know, when using the core builder,
Cesar Munoz 00:18:53 And then, probably, I will add a Boolean to the initializer to say… This buffering enabled.
And… which is by default, true.
in the initializer, and so that people can just at least disable it. But I…
I would be hesitant about allowing them to provide the whole disk buffering config object up front, at least.
Jason Plumb 00:19:17 On a stable API, because you're worried about that changing.
Hanson Ho 00:19:21 Can we mark certain APIs as experimental or alpha? Because I'm worried about how many of these things we have to expose in order for it to just…
obscure this object, because there are so many things in here that, we could potentially do, and I think, unfortunately, it's one of those things that's gonna continue to be in flux for a while as we decide how and, like, what is necessary for folks to configure. And…
In that sense, it may never get to stable, quote-unquote. But also, this is almost…
Almost everybody will want to use this, who want to do things that's slightly outside what the initializer gives them.
Jason Plumb 00:20:05 Right.
Hanson Ho 00:20:06 like, I think we talked about this, like, early on, like, we either go with
having, like, these one-off config methods, or we expose the whole object, and I think we decided to expose a whole object.
And I think if the only reason is stability, quote-unquote, I think we should just try to get away around it and say, hey, this config object is not stable. You either have to, like, use an annotation to opt-in to use it, or just know that this aspect of it is… is not stable. So,
so use at your own caution. At the same time, I feel like…
at least on Android, our mobile apps in general.
breaking changes that are effectively one or two methods, generally isn't that bad, especially when it's a config thing. It's when, like, you know, the API to create spans change, or something like that. You know, I think that's more problematic
So, even stability… even instability or breaking changes, there are degrees of badness. So I feel like if we… if we make it clear that this object is not stable, but everything else is,
that may be good enough. At least as a first step. And then maybe, like, 6 months later, people are okay with it, and then when we declare it stable, we're good to go. Because I feel like that object has changed quite a bit.
Mustafa Haddara 00:21:32 How are we… how are we gonna know?
when… People are okay with it.
Like, what's gonna be the signal that tells us, oh, this config object that we haven't touched in 6 months.
Looks good, and we should… we should lock that down.
Jason Plumb 00:21:50 I…
I have an answer from that bit that's based on my experience with OpenTelemetry Java and the way that it's done over there. It's a good question, though. How do we know or declare.
Cesar Munoz 00:22:07 I know what Hansen… mention, because I think that's also the Google
does a lot, especially probably with Compose… Compose APIs. I've noticed
There are a lot of tutorials that you have to annotate a composable with experimental something something, because
They're gonna break it at some point.
But it's a good question. I also don't know how they know when it's ready.
if I mean, we can go that… with that route. To be honest, I'm fine.
The other route, which is kind of, like, seems like it's… that when I was…
suggesting of going with the smallest API surface as possible.
I know that the feedback there will be clear, because people will be probably mad that they cannot change something, and then that's when we know that the API has to
growth.
but if we provide everything, Already at once.
you know, I was kind of discussing this the other day,
Within Elastic, which is… it's kind of funny.
That we enable telemetry for Our customers, but we don't… we have no way of getting telemetry.
Out of them, you know, because that would be a… that probably… that would be a way to know
If they are happy with the current API.
Jason Plumb 00:23:42 By finding, like, some usage numbers.
Cesar Munoz 00:23:45 Yeah.
Jason Plumb 00:23:46 Yeah.
Hanson Ho 00:23:49 Well, in terms of API stability, we can just go back on, like, a number of breaking changes in the last, like, 6 months or whatever, and just see, has it been changed? Because…
like, maybe I'm overseeing. I know this changes quite a bit, but maybe it's just additions instead of removals. And additions are always fine.
But I think I would be hesitant right now to declare that part of it.
To be stable, versus, like, the Asian. I'm like, yeah, go ahead. But I also wanna… I'm also reluctant to hide the fact that you can use it, simply because of stability. So, I'm kind of trying to do the, you know, have my cake and eat it, too. So, make it usable,
but not, like, necessarily included as part of stability. That's… that's kind of my thinking about it.
Cesar Munoz 00:24:39 I mean, it's always usable if you're fine with using Core directly.
Which is… which is… Cumbersome to use.
But, yeah.
I guess that was my plan, if you can call it a plan, is to wait until people,
ELs.
at us, asking for us to allow… enable these configurations from the agent API.
And then we know that they need it, and then we find a way to add it, to keep on expanding the…
Agent API.
As needed.
Jason Plumb 00:25:21 I was gonna call out how Upstream Java Core does this, and the way they do it is by marking things as incubating.
And there are features like,
I don't know what's incubating currently. I think the, parts of the declarative config I think you're incubating, but definitely the, extended… it's the thing we have to use for events, extended log…
Builder, this thing, I think is in incubating.
Yeah, incubator.
And so that's a…
So, what that allows you to do is to use these incubating classes, as long as they adhere to the same
interface, you can use these classes in the implementation, so they're wired up as the implementation.
And so callers of existing APIs don't break. They're using this extended thing under the covers, and then if they want to, like, in our usages that use this for events, you have to cast, and…
it's a way forward, right? It's a way to not break stability. It's a way to allow new features to be tested, you know, by users, but it's also a lot of work to have
Incubating packages and to manage this stuff, and, like, when it comes time to grad… like, graduate, or when it comes time to, like, mature these into, like, the real implementation, it's, like, a ton of work.
So…
That's one way to do it, that's how it's done in Java. I don't… I don't have a better idea right now for how we could sort of, like, pick and choose which parts of which APIs are stable and which aren't, but that's one strategy that's been used in Java.
Hanson Ho 00:27:02 I hate having to cast it to…
Jason Plumb 00:27:05 Yeah, yeah. And when it moves out of incubating, that will go away, and, you know, we're a user of that. If we like it enough, we could encourage them to move it out of incubating.
But Java's also understaffed right now.
Hanson Ho 00:27:21 I would… Go ahead.
Cesar Munoz 00:27:24 But, no.
Hanson Ho 00:27:25 Okay. I would propose not to do that. Okay. I hate… I hate… there's so much overhead. New artifacts, new classes, every consumption location has to do it. The equivalent of a cast…
No, that just feels gross. So, I mean, I think…
going well as Cesar said, having a minimum kind of thing, I think, is one way. But then, if someone immediately asks, then what's our deal? I mean, we're still gonna have to confront this question. So,
We might as well…
do it now, and think about what we want to do when someone says, hey, I want this part of stable, I don't want to use core, because then we're just basically pushing people to use an unstable core, which is a much bigger surface area. At least this is limited from an API surface area. It is, like, you know, set
you know, these values, so it's a lot more controllable versus importing core and configuring from scratch.
kind of…
doesn't allow you to use the thing that is stable, which is the agent initializer API. So I'd rather be like, everybody go there, and if you want to kind of configure something different, use this unstable object, rather than input this entirely unstable project, and then initialize everything on your own. I feel like that's the lesser evil, in terms of introducing instability.
And again, I think we need to, like.
talk about, API instability, which is effectively just
You know, ideally just a build time fix, versus…
this component has never been used in scale, so use at your own risk. That level of, you know, code stability, quality stability, that is, I think, what I'm more concerned about, that we ensure we don't have. And I'm…
mostly confident, since there's several companies shipping this to customers. And, you know, one would imagine if there are common issues, it would be discovered by now.
Jason Plumb 00:29:34 Okay.
Manoel 00:29:36 I would rather go into, let's say, a faster release lifecycle, so just cut 1.0 and fix everything that's broken kind of right away, so priority over
Thinking over, thinking, overthinking and never doing it.
Jason Plumb 00:29:49 Yeah.
The challenge, though, if we cut a 1.0 today, and we need to make an API change, then we have to move to 2.0.
Like, if there are people that depend on 1.0 as a stable version, then we have to decl… if we make it a breaking API change, we have to, you know, do a major version change, which is not the.
Manoel 00:30:07 I'm not…
Yeah, we want to cut 1.0 consciously, knowing that we have to do breaking chains right away, but let's say we release 1.0 and we learned, because what we know now, we didn't know before, and something has to change, then we just cut 2.0, right? So, I think that's quite normal in software engineering, lots of.
Jason Plumb 00:30:27 Totally.
Manoel 00:30:28 fibers, do the next major.
Bites.
Jason Plumb 00:30:31 Yeah.
Manoel 00:30:32 So, I don't consider that to be a biggie, to be honest.
Jason Plumb 00:30:36 Okay, I appreciate that. I just want to make sure that we're not cutting, major releases every month.
Manoel 00:30:42 Yeah, it's… I mean…
Jason Plumb 00:30:43 I'm not actually concerned about that, but that, you know, you have to be careful. There's some… there's some… there's some middle line, and I… yes, we can get into analysis paralysis, and hopefully we're not doing that. I think I'm ready to, like, push this forward, so…
Manoel 00:30:56 Yeah.
Cesar Munoz 00:30:57 I think it's… I think it's fine.
As long as we… Start with a…
small API surface. I mean, so, for example, Hansen. The,
Maybe this is something that you don't have to answer right now, but…
Is there something in hotel ROM config, which has a lot of configs?
That you think, you know, is a must for, probably.
You know, everybody who might need to use the agent.
Hanson Ho 00:31:37 I think so…
Cesar Munoz 00:31:37 That's goodbye.
Hanson Ho 00:31:38 Like, suppressing instrumentation, I think, is probably important.
the network attributes, there's a lot of them, I believe, so there's a bunch of overhead that it could, provide, or, you know,
create. Global Attribute Supplier seems like something that
Folks will want to use.
So…
I think this is… this is… this is more me speculating, in terms of…
Cesar Munoz 00:32:15 But that's a valid point, and I'm not saying let's not provide them, I'm just saying that there are a lot of stuff here.
So then, why don't we strip down this… if we think that this config object is something that is very useful up front.
By the first release, then at least let's strip it down.
Of the things that we don't think are a must right now.
Or, at the… kind of like… mappings…
That are directly added into the initializer function that Then, you know.
Modify these values inside here in a way that we don't have to strip this config.
But we kind of exposed some of its…
capabilities via the initializer cotling function.
Jason Plumb 00:33:11 So, I want to call out something that I think is…
a bit of an API problem, and some of this is historical, and some of this is because we're coming from Java originally, but the OpenTelemetry OTel Rum config, in concept, like, in its name even, the idea is to be able to configure
various operational aspects and features of OpenTelemetry Rum, right? That's great.
But we also have the OpenTelemetry Rum Builder.
which uses the config. And at least in Java, the builder pattern is used kind of as, like, a, kind of as a config object until you call build, right? Like, you're setting different features, you're configuring different aspects, and then you call build.
And so we have two different ways of, kind of, supplying configuration. And they do work in concert, but I think that both of those are configuration. Like, what's in the hotel room config, or hotel room builder, rather.
like, these things, if you're building… if you're using Core and manually building an instance of OTel Rum, then…
you can set all of these different things, you can call all of these methods and do these things, and we also have, like, a sub-config, which contains more stuff, right? So I think we should probably figure out… I'm gonna call this a problem, and I think we should… we should make this more consistent before we ever can call core stable.
Right? And this does play into what you were saying, Cesar, about the config object.
Cesar Munoz 00:34:39 and also core not being my…
you know, favorite module to market stable, at least not right now.
there… there are… I don't know if you've seen the… PR that I created.
To add instrumentation config.
To the initializer.
But it uses, Kotlin…
Mustafa Haddara 00:35:02 Okay.
Cesar Munoz 00:35:03 of way of doing builders. They call it TypeSafe builders.
In the cutting work.
And he kinda, like… At the end of the day, it's…
I guess it kind of behaves like a builder, but when you write it, it looks like a DSL.
Kind of language.
Jason Plumb 00:35:25 Yeah, I've looked at this, I've looked at this twice, and I'm like, I don't understand this, and I'm gonna come back to it when I have more time, and then I haven't, so,
I saw a good conversation happening around this.
Cesar Munoz 00:35:37 It's… It's a way to… At least to me, it's a way to make the instrumentations config.
More scalable, without having to, you know, add a hundred, you know, arguments to the initializer function.
Because it's just one, which is kind of like this… TypeSafe builder.
Kotlin stuff.
maybe that's a way that we can expand this config, but in that case, then it wouldn't make sense to expose this stuff, like the objects, such as auto-rum config, because are more, like.
targeted to the builder use case of Java, as you mentioned. So, you know, there are ways that we can play with
With the initializer.
But if we, like… Decide to,
For example, right now, I'll just expose
other ROM config in the initializer, then…
I don't see a way to pull it back in the future if, you know, people think that it's not.
Kotlini… Enough.
Jason Plumb 00:36:47 Does this PR, get rid of hotel room config in the initializer? It doesn't.
Cool.
Cesar Munoz 00:36:56 No, it only touches on the instrumentation concept.
Jason Plumb 00:36:59 Okay, okay.
And does… does this change not break the demo app?
Cesar Munoz 00:37:07 No.
Jason Plumb 00:37:08 Okay.
From reading this initially, like, in the various small time I've spent with this, I can't see how it's used yet.
Like, it's not clear to me how you use this versus the existing way, which was just to specify all the parameters, right?
Cesar Munoz 00:37:27 There's a small example in the description.
Jason Plumb 00:37:31 Okay.
Cesar Munoz 00:37:32 I can enhance it.
It's like, you pass another… a parameter called instrumentations, and then inside it, you have each instrumentation by its name.
Jason Plumb 00:37:45 Okay.
Yeah, this does look very DSL-y, doesn't it? Cool.
Cesar Munoz 00:37:49 them.
Jason Plumb 00:37:50 Okay.
I think Jamie was stoked on this, right? Yeah.
Jamie Lynch 00:37:55 Yeah, I think…
Yeah, I think this would definitely be a nice way of, like, initializing the SDK, just speaking generally.
Jason Plumb 00:38:03 Yeah.
Jamie Lynch 00:38:04 Zoo.
Yeah, you don't have to…
know too much about what's actually going on under the hood, necessarily. You can kind of separate your API out from
Yeah, how the sausage is made.
Jason Plumb 00:38:20 So I… I'm asking… I'm asking this question, but my… I already have my answer for this, and that is, I don't want us to expose
Java classes, like, in our main API that we're declaring stable, because that's gonna require us… I mean, we can build the Kotlin one in parallel or next to it with a different name, but then that sucks. We've just doubled our API surface. We can't delete the Java one if people are using it.
At least if it's not compatible. So I'm more comfortable if we just move stuff to Kotlin that's on the public API surface.
But we don't… we don't have those identified yet.
Hanson Ho 00:38:57 Well, I think the… the TypeSafe
builder, will basically force us to say what we want to include in our DSL.
which is probably going to be very similar to what the builder has, or what we would consider to be API-stable from the builder. I mean, at the end of the day, it just does what, you know, a builder does, but it just does it in a nice, nicer, you know, syntax… it's a syntaxy way.
So, if the idea is that the config object is,
too big, and we already have this builder that we've already kind of, quote-unquote, blessed with, these are the things that we should have methods for. If we reimplement that, in the agent.
and basically expose that as the agent API, which then internally uses whatever unstable core, you know, config object or builder, then I think we're good. We just have to know that the API that we're exposing
do represent things that we don't want to remove, or fundamentally change. So,
I think that would be a way forward.
Jason Plumb 00:40:10 Okay.
I'm on board with that. I'm worried that Cesar might think it's too big of an API surface, then.
Cesar Munoz 00:40:18 No, I think it's… I think that kind of aligns with what I was mentioning. Okay.
Yes, it's kind of to have the API in the company side that then… that later translates internally into the
builder. Now, I'm not sure if… like, everything?
Up front, but yeah, at least it's stuff that…
We think are, are, are useful.
Hanson Ho 00:40:44 And I think… and I think that's what made… that's what… so, initially, what I kind of, like, balked at was, like, having another config object, like, or, like, a bunch of methods, in the agent, but if we're already doing this.
so we can do a Kotlin EDSL, then we might as… because that will bring it… bring along, you know, some benefits in terms of configuration and usability. We might as well tag this along.
So it's almost like it wouldn't be worth it on its own, but, like, combined with this kind of new feature, especially if we can make it, like, start small.
like, just include a set of configurations that we for sure wanna expose. And then if we miss one, okay, that's not bad, we'll add it in again, as long as we're not going to remove it.
So, I think this gives us a more incremental path into introducing more and more stuff into the stable API, which is the agent, leaving core, you know, untouched.
Jason Plumb 00:41:46 Yep.
Cesar Munoz 00:41:47 Sounds good.
Jason Plumb 00:41:49 Okay, so that… your expectation then is still that core will be alpha?
Hanson Ho 00:41:54 Yeah. We're all on the same page there, okay.
Cesar Munoz 00:42:05 Well, and broadly, instrument… modules, too.
Jason Plumb 00:42:09 Yes, also instrumentation.
Hanson Ho 00:42:12 Everything else, basically.
Other than agent.
Jason Plumb 00:42:16 Yeah.
And then we can talk about the roadmaps for each of those individually, then. Yeah, okay.
Hanson Ho 00:42:22 The point of this is to get started, and to make people, like, freak out less. At the end of the day, it's the same code.
Jason Plumb 00:42:29 Yeah, and people don't forget about the agent instrumentations being alpha, so, you know, that's a… like, if someone… if we decided to break the instrumentation API, which is Mark Stable, people would definitely notice that. And we don't have a separate package for that, do we?
I don't think so. Oh, maybe we do, actually. It's just instrumentation, right? It's like API or Core or something?
Is it this one? Yeah. Yeah, yeah, this is where the API is, right? So…
I'm assuming, to start, we would also have this be alpha.
Hanson Ho 00:43:04 Yeah…
Jason Plumb 00:43:05 Because this one has… this one has the… this is… and this is being the main interface, yeah, okay.
Okay, we have… we used 43 minutes already, that's pretty… pretty exciting, so this is a good discussion. I appreciate everyone's feedback on this. We need to go through, maybe not on this call, but at some point we need to go through those issues, and maybe relabel them, and…
Remove the feature-based ones that we think are not important to 1.0.
You know, like this one, for example, like, really nice to have, would help.
Cesar Munoz 00:43:42 stability.
Jason Plumb 00:43:43 We could add it later, right?
Cesar Munoz 00:43:45 Yeah, I agree, probably we can remove the label.
Jason Plumb 00:43:48 Let's do… let's do that.
Cesar Munoz 00:43:49 That's nice.
Jason Plumb 00:43:50 side effort, if that's okay, because I want to make sure that,
that we talk about the release, and also I wanted to… whoever wrote this one, I wanted to give time for that, and then I also wanted to acknowledge… I think there's someone on the call called Grace Lim, who I don't recognize, so welcome. We're a very open and welcoming community, and if you want to put your name and where you're from in the agenda, that's great. If you have items you want to discuss,
You know, say hi or add stuff to the agenda.
Grace Lim 00:44:22 Hi, morning. Yeah, actually, I'm the one who wrote the semantic conventions for screen views, so yeah, I can definitely add my name there, but I have added myself to the registry.
Jason Plumb 00:44:31 Okay, cool.
Yeah, welcome. I… have you joined before? Sorry if I don't remember you having been here.
Grace Lim 00:44:38 Oh, I don't know if I joined the Android SIG before, but I have joined, I think, the client sick, so I see some familiar faces, but yeah, thank you for the welcome.
Jason Plumb 00:44:48 Yeah, cool. Yeah, we can move on, I think. Is everyone else ready to move on?
Cool. Yeah.
Semantic conventions.
Grace Lim 00:44:58 Okay, so maybe sharing my screen might be a bit better? Do you mind if I…
Jason Plumb 00:45:03 No, no, go for it.
Grace Lim 00:45:04 It grew up. Nice.
Jason Plumb 00:45:06 Where are you from, Craig?
Grace Lim 00:45:08 Who are you with? So, I'm… I'm from AWS. I'm on the CloudWatch run team. We're currently looking into, kind of, mobile solutions.
For, like, real user monitoring, because right now we only support web. So, yeah, that's… that's the big project going on, yep.
Jason Plumb 00:45:25 Okay, so…
Grace Lim 00:45:27 there's a bit of telemetry that we're trying to kind of align on, at least internally, and then we figured we should do it kind of across the board and upstream as well, since we're in this space anyways, and we want to kind of make sure the proposals are future-proof. So, with that being said, I think my first, like, kind of high-level
Let me take a step back. So I want to start today by reviewing…
conventions for, like, screen notes and app launches, and, like, I already have APR open to kind of define the attribute we want to use for said screen name. I brought this up during, I think, client config, and originally we decided on
app.screen.name, and then in the PR, there was a bit of pushback on whether we want to use that or something else. So that's kind of the first
not point of contention, but first thing I wanted to discuss, because I think that kind of changes how the other attributes are defined, and then second is…
kind of where to define these. I've been looking through just, like, the app semantic conventions, but then there's also, like, Android and iOS, and then, you know, there's also, I heard
the…
like, web side is also pretty active these days, so I wanted to kind of make sure I'm in the right space to make sure
yeah, to make sure it's in the right place and see if it can accommodate all three platforms, or if they should be, like, split out individually. So yeah, I wanted to start there, and then if we have time, we can go into, like, the specifics, but I figured this might change depending on how our discussions go.
Jason Plumb 00:47:01 Great, yeah, this is a, this is a big… a big topic of interest for us, is defining the semantic conventions. So, yeah, I linked to what I think is your pull request, 2744.
Grace Lim 00:47:18 Yeah, sorry, I meant to link… yes, that is the correct one.
Jason Plumb 00:47:21 Okay, cool. It looks like it has one approval already, from Cesar.
Grace Lim 00:47:26 Yeah, no, it got approvals, and then… so, last week, I went to…
iOS, like, the SwiftSig. And then there, there was pushback on, oh, I don't like app.screen.name, because, like, for some people, they might…
first understand this as the device display, and so, he didn't like that too much, and so he proposed Surface. But to me, Surface is not very intuitive, so…
Billy and I, we were talking about what we might, want to propose as a compromise, and we were thinking, like, view.name. So that's kind of what I've landed on for now.
But we can see how… how that goes.
Hanson Ho 00:48:04 So, hi Grace, I commented on the thing, and I think the fact that Surface was chosen is because it wasn't intuitive.
There are a lot of words here that have overloaded meanings. View, for instance, have different meanings in iOS and in Android. So, screen, obviously, has, a very specific meaning, especially, you know, on a single device. It's very one-on-one. And in the description, there was,
there was, you know, an idea of wanting to have multiple of these. So, it's…
like, I, you know, I don't want to be, you know, spending forever debating, you know, a specific name, but the noun that I think we choose has to be sufficiently
Useless, but also kind of connotes
in an ethereal way, that it is what it is. so, I think the… the one versus many is important. I don't know if you've decided to… because I think in the description,
there wasn't really differentiation between widget and, because you basically define a widget as, like, a fragment. So then… then you're basically, you know, up in this territory. So, if there is something generic.
That isn't, view, activity, or, or scene. Things that have, like, specific meanings in the, in the platforms. Totally open. It's just view very… does have a very specific meaning. It's too meaningful, is the problem.
Grace Lim 00:49:51 I see. So, what… in the Android world, so I'm… I've mostly been looking at the Swift SDK, so, like, I know definitely it has meaning there, and probably the meaning…
aligns with what I was proposing, but then in Android, like, what is the connotation there for views?
Hanson Ho 00:50:11 a view is a piece of thing that contains some UI. Basically, there's a view tree. I see, okay. And the view tree's attached to the window, and an activity could have a view tree. So the…
Grace Lim 00:50:24 Okay, I see, I see.
Hanson Ho 00:50:25 It is stupid, but, you know, it is what it is.
Cesar Munoz 00:50:29 I think an Android view might be the…
might be kind of like what we define widget in the semantic conventions. Probably it's the closest, I would say. Oh, I see, okay. But it's kind of like legacy one, so it's complicated.
Jason Plumb 00:50:46 So… Okay.
Grace Lim 00:50:47 So, view's definitely overloaded then, okay.
Jason Plumb 00:50:50 I personally like screen. I think it's the right word. I mean, we're never gonna get… I think we'll never get consensus on this, but I think screen is great. If people are confused about the difference between a screen and a physical display, I think that's the… I think that's the distinction, is that if you're talking about the actual, like, piece of glass, that is your display, it's not your screen. Screen is the abstract, like, conceptual thing you're looking at.
Grace Lim 00:51:14 If someone says… sorry, if a user says.
Jason Plumb 00:51:17 oh, your stupid app crashed, the first thing you're gonna say is, what screen were you on? Right? I think, like, to me, that's, like, conventional. But, you know, there's also language differences here, so…
Hanson Ho 00:51:28 So, I think I would be okay with screen if…
the semantic definition is more specific to say that there is one screen, because it would be really weird if there are multiple screens that are active at one time, which in the description says it's possible. So I think…
like, surface has a similar, but it's even more nebulous, even more, even a crappier word, but because it's more nebulous, it's almost like, sure, you can have multiple surfaces, so if… if…
Cesar Munoz 00:52:02 I just want to clarify that I think the current definition here in this PR of screen
It might be my fault, because I noticed that
It was kind of, like, quite generic at first.
And then I knew as soon as I saw the word screen, that some people might have the confusion around, is it something that covers the whole device's screen, or…
Or not, because it's also confusing in Android that you, in a mobile phone, An app might split
two screens into… into two different, actually, screens, but then if you put the same application on a tablet, for example.
you might see two screens in the same one. It is actually very common for the settings screen that you see is split in smaller devices, but in the settings, you see the left side of the panel will have the list of settings, and then the right side will have the details.
So, it's confusing, and that's why I added the comment, and I think that's why now the description says that screen doesn't have to take the whole
You know, device screen.
Grace Lim 00:53:11 Yes, please.
Cesar Munoz 00:53:12 Yeah.
But, to be honest, I don't… I don't know about a better word either. And I like the description right now better than
What it was at first, because it might be confusing, and that could cause other issues in the future.
Hanson Ho 00:53:38 So, if we could constrict The description to the areas that the application is responsible for.
And we're saying, basically, it maps to all the things that the application, you know, is responsible for, even if there are dual screens. If you're on the settings page and there's a sidebar that's effectively a different fragment or something like that, if we can say that's the same thing.
then I think… I think screen will be fine. It's basically app… the screen of the app, just like the, just like the convent… just like the namespace says, app.screen. You're not talking about, you know, if you… if you're using a partial, you know, of the device display, you're not talking about, you know, an area that's not controlled.
So as long as… as long as… as long as the semantics and the description differentiates it from a widget, in terms of, like, the… the coverage and the number that can have.
I think screen is fine. I think screen and surface, as you pointed out, or somebody did, very similar. One just means… one has a more nebulous meaning, and the other has more specific meaning. And if we're gonna go with a more specific meaning, the definition should also be locked down to be a little bit more specific.
And it's also, I think, it matches well with the other, the other, attributes in that subdomain. I think coordinates is in there. So when you have a coordinate.xy,
you don't really expect to have to know what the framing is in order to know that. Or at least the implication is that, you know, there is only one grid, where the XY coordinates are located. So in that way, I think making a screen be
you know, one at a time, also makes sense. Otherwise, the coordinates one will be…
Which screen are you talking about, for the coordinate?
Talking Samurai reply.
Grace Lim 00:55:35 Oh, one quick question. So this app.screen.coordinate.x, this is not, like, the display coordinate, right? So in… if I had one device.
display, it's not like an XY on that singular device, but it's on the specific Screen.
Like, application screen?
Hanson Ho 00:55:55 I believe so, Jason.
Cesar Munoz 00:55:58 Whether if it's absolute, coordinate, or relative to the…
Grace Lim 00:56:02 Yes.
Cesar Munoz 00:56:03 to the screen.
I think we haven't actually defined that.
Jason Plumb 00:56:07 Yeah, I think the way it's implemented right now, I think Cleverchuck did our implementation, I think it's… I think it's based on the display.
Do you remember, Cleverchuck?
cleverchuk 00:56:19 I think he is absolute, I'm not entirely sure.
Jason Plumb 00:56:23 Absolute, but relative to the display, and not necessarily the…
The window or the application activity.
Anyway, I think that actually might be…
I mean, it might be incorrect, we might need to change that to display.
If that's the intent. I don't…
I used screen to mean the… probably the display, so that's on me.
Hanson Ho 00:56:52 Anyway, this is… we can resolve this later, but the fact that there are other things kind of, you know, in there, they should at least, conceptually the match, and maybe we actually got it wrong, but, you know, let's try to do that.
Jason Plumb 00:57:08 Blake, while I'm… Go ahead.
Grace Lim 00:57:10 Please, go ahead. No, I mean, like, while I'm in the space, I can, like, update this to be app.display, that… that I can take up as well. But yeah, I think definitely, to me.
At first glance, this looked like the display coordinates, like the physical device's coordinates.
Jason Plumb 00:57:27 I agree with that. I think this probably got it wrong. I think it's all… yeah, I agree with what Hans was saying, too. It's important to have alignment with the other existing semantic conventions. I also linked to the current name that we're using for screen name in Android.
And sometimes, it helps to be able to reference from your semantic convention PR existing or prior art that aligns with that, and so what we call it right now in Android is just screen.name.
But, that clearly should change and align with semantic conventions, so a PR in both of those to align them would be awesome. And I would do those as separate efforts. You know, if you're gonna change that coordinate one, the…
Screen coordinate, I would.
Grace Lim 00:58:07 At DisplayPortnite, do that as a separate PR.
Hanson Ho 00:58:09 Yeah, and also, I wouldn't touch that yet. I think… I think the… the screen coordinates aren't as useful as the relative coordinates to the application window, so we may want to actually change the implementation to match what that says. But we'll take that on as, like, something, you know.
Off to the side, don't worry about it, it's part of this.
Cesar Munoz 00:58:32 The thing… can, can, can we say that…
Because I… we have two different things, and we need two different names, so that they don't overlap.
And right now, they seem they overlap with screen.
And I think it's just fine, whatever name, so…
I guess the consensus is that we will define display as the actual device screen, and then screen as
Could it be…
Grace Lim 00:58:59 A UI.
Cesar Munoz 00:59:01 On the…
Jason Plumb 00:59:01 Application conceptual component, yeah.
Cesar Munoz 00:59:04 For me, that works, yeah.
Jason Plumb 00:59:06 I have to… I have to play time police here a little bit, sorry, we have one minute or less. We are due for a release this week, and we didn't get to talk about it. I would like to get Cesar's PR in there, in this release, so that people can start using that API. Are there any other PRs that people are aware of that they want?
To get in this release.
Okay, sounds like nowhere.
Alright.
Sorry for kind of rushing through that, Grace.
Grace Lim 00:59:38 No worries. So, is the consensus, like, still at that screen, that name?
Jason Plumb 00:59:44 You got an approval from Cesar, and I like it, I can go give an approval as well.
Grace Lim 00:59:47 Okay.
Hanson Ho 00:59:48 I'd want to change in the description of what that means first, I would say, but I'm generally okay with that.
Grace Lim 00:59:57 Description… which part of the description?
Hanson Ho 01:00:01 there's a disc… there's a part that says there could be multiple… I think I made a comment under, on it, saying that screen maps seems to map one-to-one, and then… and then, you know, if… if you need to have multiple, it should be something more nebulous, or…
I'll do a follow-up comment, and I'll make sure to mention.
Jason Plumb 01:00:22 Yeah.
Grace Lim 01:00:23 Alrighty, sounds good. Thank you.
Jason Plumb 01:00:25 Thanks, everyone. We're at time.
Thank you, buddy.
Grace Lim 01:00:28 Thank you, bye.
