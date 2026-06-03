SIG: Event WG
Date: 2026-06-02
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:08 Hello, hi Robert, how are you?
**Pellared** 01:11 Hello, good just have a sore throat.
**Liudmila Molkova** 01:16 Oh.
**Pellared** 01:16 Yeah.
How about you?
**Liudmila Molkova** 01:22 I'm fine.
It's my fourth meeting of the day. It's 3AM.
**Pellared** 01:32 Nice to meet you.
Of course.
I tried to address your comments, thanks for your review. I started the day morning, you'll need to double-check it, but yeah, it was great feedback.
**Liudmila Molkova** 01:48 Thanks, I'm sorry for Simon, you need to kick in.
**Pellared** 01:52 No, no, it was good. I actually thought that… I usually, yeah, I did a bad job. So yeah, I'm happy.
And this is the only thing which I added, this PR.
**Liudmila Molkova** 02:08 Yeah.
I'm sharing the wrong… Yeah, should we drop this guy? Should it help anybody?
**Pellared** 02:35 I have added a comment. We have a similar thing for, for metrics.
And I thought that it would be probably easier to do it in a separate PR.
**Liudmila Molkova** 02:49 Hmm.
**Pellared** 02:51 So, I'm not against doing it, but I think it's better probably to do it for, you know, a separate PR for metrics, and for this one as well.
And there's all sorts of.
**Liudmila Molkova** 03:04 I see.
**Pellared** 03:05 So I'm not against it, I just think it will be, you know, Easier to separate it.
**Liudmila Molkova** 03:14 Yeah.
**Pellared** 03:22 At the same time.
I think that this documentation about how to contribute, or I don't remember, you know, this doc, has also metrics to be defined.
**Liudmila Molkova** 03:35 Yeah.
Okay. Oh, th-this? This at least looks… Like, it contains some… something useful, so maybe for metrics.
Maybe for a metric, so we should not drop it.
And maybe from the future metric… metrics page.
Sorry, metrics… how to define metrics will be linked to the sections, because otherwise the document will… be giant.
Maybe the long-term story is that we… Break down this how to write conventions, and we… into… individual things.
Yeah. I'm curious to ask, what do you think, if you're ready to participate?
**Trask** 04:33 I missed the, the context.
**Liudmila Molkova** 04:38 Yeah, so, Robert has the SASAM PR on how to write, events.
And… if we look here… It's amazing.
**Pellared** 04:49 The only not-at-risk comment, by the way.
**Liudmila Molkova** 04:53 Oh, cool, yeah, but I don't think it's a civil-looking one, but… This document is inevitably going to be joined.
But for events, we have this… Small document, which is essentially how to write events.
And semantic conventions.
And… After we write, like, after Robert's PR, this content is almost fully duplicated in this other place.
So…
**Trask** 05:34 in the… in the big… Writing. Yeah.
**Liudmila Molkova** 05:40 the better and I think maybe long-term, we should have… This is a registry of how to write individual things and move things out.
So, like, what if we take what Robert did here?
And let's say, put it in the events MD.
And just link from the How to Write Conventions to this doc.
**Trask** 06:10 And…
**Liudmila Molkova** 06:11 Later on, we would do the same for metrics, because we already have something for metrics here.
And we probably take spans and move them out as well, otherwise the… this dog becomes… It's already joined.
**Trask** 06:24 And what's the, is this… this has normative language, like, it's considered a normative part of the semantic conventions, how to write conventions?
**Liudmila Molkova** 06:38 So there are some normative parts here, but they are relatively small. So I think this is… all the section is best practices.
And there are just a few things that are normative. We can keep normative things here.
**Trask** 06:57 And if… in the other document.
**Liudmila Molkova** 06:59 Huh.
**Trask** 07:00 or events… Where is that? Is that under docs, also?
**Liudmila Molkova** 07:08 Yup. Oh, Dogs General.
**Pellared** 07:16 I think both are using Hamptic language.
**Trask** 07:19 Okay.
Yeah, I mean, I… I like… the idea of… That could go either way, really.
Don't mind large… Mence with… Different stuff in there.
searching… Ctrl-F to find stuff.
But I also don't mind the, splitting it out.
**Liudmila Molkova** 07:49 The only thing I'm worried is that the… Oh, sorry.
**Trask** 07:53 Oh, yeah, yeah, no, we should fix the duplication. Either way, I agree.
Good.
**Liudmila Molkova** 08:03 Cool. And other than that, Robert has the PR. I made the first pass, and yeah, if you want to take a look.
That would be awesome.
**Trask** 08:16 Cool. Yeah…
**Pellared** 08:21 I am back. Is there any conclusion, or not yet?
**Liudmila Molkova** 08:26 I think me and Trask, we are both worried about duplication, and we should fix it, but how, either in this document or in the new document, it's fine.
**Pellared** 08:36 Okay.
**Liudmila Molkova** 08:36 Pleasure.
**Trask** 08:41 Yeah, I mean, if you wanna… if you prefer to just… I guess the most consistent at this point is just to put it in the big dock and delete the other doc, maybe?
11.
We wanna…
**Pellared** 08:53 for me.
**Trask** 08:54 Split. So…
**Liudmila Molkova** 08:57 I don't think it's the most consistent, it's actually.
**Trask** 08:59 Sure, you have a few…
**Liudmila Molkova** 09:00 precedence, so if we look here, it's a little bit of mixture, so for events, it's now here. The metrics are TBD, but effectively there is a file with some of information for separate one, then the response, which are here, and then there are entities, which are Separate.
**Trask** 09:22 Oh, okay, so… Almost the more consistent as separate.
**Pellared** 09:28 Okay?
So, let's put it separate, or not.
**Liudmila Molkova** 09:31 Let's put it separate, yeah?
**Pellared** 09:33 Okay.
**Liudmila Molkova** 09:37 Sorry.
**Pellared** 09:38 It's okay.
**Liudmila Molkova** 09:44 Cool.
So, and then, it becomes… Pretty straightforward.
Anything else we need to discuss?
We can… Spend a little bit of time reviewing the PR, if you want.
**Trask** 10:21 I'm gonna be at my desk in just a second, and then I can… participate in reviewing the PR.
**Liudmila Molkova** 10:28 Okay, we can wait for you.
**Pellared** 10:31 By doing a lot of things… for addressing your feedback was removing just, you know, stuff which was misleading or not necessary, if I understood correctly.
**Liudmila Molkova** 10:47 Yeah, I also, like, felt that just what you had is awesome, it's just that there is maybe too much of it.
Too much awesomeness.
**Pellared** 10:57 I did, I think I just removed one-third, or something like that, of the document, or 1 fourth, I do not remember right now.
One of the things was about the severity.
I removed one part, which was the sentence, which I feel that caused confusion.
Regard, but I have kept the existing one, and I'm not sure if we need or do not need anything more for the severity part. If you just find it as severity, maybe just add this hash in the beginning, so you find the section.
In search.
Oh, yeah. So this one. Yes.
Thank you.
**Liudmila Molkova** 12:09 I remember that the comment I left was the… The default severity.
**Pellared** 12:19 No, it was a different severity, the comments were reported. It was something like.
**Liudmila Molkova** 12:27 Yeah, here.
It's like, if two diff- if two… It's something… oh, if it don't… yeah.
Oh, you had a point on… When there is already a similar event.
**Pellared** 13:14 Yes?
**Liudmila Molkova** 13:15 And I think it was there, and I think he removed it with Tri Support, so it was gone, yeah.
**Pellared** 13:21 Yeah.
ratios.
**Liudmila Molkova** 13:39 Okay, I'll just start over.
**Trask Stalnaker** 14:22 I like the… trying to define an event without using the word event.
**Liudmila Molkova** 14:29 Right.
I almost thought we should… we should have some… a special way of writing events. I think, Austin used capital E.
**Trask Stalnaker** 14:39 S.
**Liudmila Molkova** 14:39 events.
**Trask Stalnaker** 14:40 Yeah, and lowercase e.
**Pellared** 14:53 I changed the application interactions to user interactions, because I think it models good for browser.
**Liudmila Molkova** 15:02 Yeah.
**Trask Stalnaker** 15:12 What does standalone event… mean.
Line 348.
**Pellared** 15:38 I do not remember why. You mean the term standalone?
**Trask Stalnaker** 15:42 Yeah.
**Pellared** 15:43 I'm not sure if I have picked it in some… Other place where we'll spend a loan?
Stand alone.
No, we can remove it.
Let me check other places.
**Trask Stalnaker** 16:04 Probably will get cleaned up there when you move, because it seems like it's something compared to…
**Pellared** 16:11 Okay, I see.
in general, I don't think, which was pure my things, was almost the same stuff, Yeah, so I have taken it from the Docs General EventsMD.
**Liudmila Molkova** 16:28 Hmm.
**Pellared** 16:32 Yeah, but, put the comment, I will probably agree on this one here.
**Liudmila Molkova** 16:36 Okay.
**Pellared** 16:39 I just have to remember that it's unnecessary.
**Trask Stalnaker** 16:44 I'm still laughing at you. Oh, sorry. Sorry, say that again?
**Pellared** 16:50 And maybe the standalone was also in the specification?
And what are you laughing at?
**Trask Stalnaker** 16:56 I'm just laughing at the use of the word occurrence.
As a synonym for event.
Again, try not to define events. Like, when to define events.
**Liudmila Molkova** 17:19 Do we want a bike shed, and how to call them?
**Trask Stalnaker** 17:22 I can live with a current, yeah.
The bullet point lists on 3-4… 3.54.
Is this… this reads to me like… All of these things should be true.
And I'm wondering about the…
**Pellared** 19:02 Unnecessary.
**Trask Stalnaker** 19:04 No, well, I was just… oh yeah, and maybe that gets to Lyudmila's earlier comment about… Potentially could reduce the amount of things.
But also, I was… Represents a checkpoint, staging point, or… outcome… oh, okay, never mind, I just didn't read it.
**Pellared** 19:26 But I think, maybe wrong with the first one.
We can remove the first one.
**Liudmila Molkova** 19:32 I'm thinking… so I think you got it from the spans, and it's there.
**Pellared** 19:39 Probably.
**Liudmila Molkova** 19:41 Significant. Maybe… And maybe it's a part of refactoring that There is a lot in common in defining things across signals.
And, like, maybe in this guide, we should just mention that on defining telemetry, that's not important for your observability needs.
**Pellared** 20:05 Yeah.
**Liudmila Molkova** 20:11 But, like, you can think about it as common guidance being in this doc, and if we're moving to events, we can drop it from the events doc, and I can take an action item of refactoring this one to provide…
**Pellared** 20:26 It's going this way.
**Liudmila Molkova** 20:27 Common considerations.
**Pellared** 20:30 So, yeah, just as a suggestion to remove this one.
One second.
That's good.
Beautiful This is it.
Let's go to the floor.
T-la!
**Trask Stalnaker** 22:36 Line 396, event names must be low cardinality.
What does that mean?
Are we saying that event names can be parameterized somehow?
**Pellared** 22:57 I think mostly they should not, and this is what this point number 3 tries to say as an example.
I think in some cases, It could use runtime, but only if you know the set But it's just my guess, if the set, you know, is an annum with a known value.
**Trask Stalnaker** 23:22 I see.
So, one day.
**Pellared** 23:25 unbelie.
**Trask Stalnaker** 23:26 Nava.
**Pellared** 23:27 Yep.
**Trask Stalnaker** 23:29 One semantic convention definition of an event.
You're… could… the event name could be… It could have multiple event names, could be parameterized by an enum.
I don't know if our weaver really supports that, though.
**Liudmila Molkova** 23:54 No, no.
But, like, event name is a synonym of metric name, right?
Like, we don't say metric name should be of a low cardinality.
**Trask Stalnaker** 24:05 Right.
I'll just leave a comment.
And…
**Liudmila Molkova** 24:29 Should we remove it?
Should we have some language that… What's expectations.
And maybe, Robert, to the conversation we had here, maybe we keep this and remove this.
**Pellared** 24:49 I think that's fine.
Since you asked here about fully qualified name.
But I haven't found anything like that also for… For metrics.
But I, in the naming guidelines, there was something about namespacing, which the naming guidelines only like, have to be fine, so I thought that probably this is good enough, so I'm not sure if we have any, yeah.
Any preferences here?
**Liudmila Molkova** 25:55 Yeah, I think we demand it to be unique within our registry, and I think that that's enough, because the schema URL Is qualifying them further.
**Trask Stalnaker** 26:14 Lemuel, I noticed you, resolved the one about should not include runtime values. Wondering… Similar to metric name.
It's… it's already… or at least it's enforced by Weaver.
But you can't…
**Liudmila Molkova** 26:41 Oh, right. So, okay, so I think, like, there is the double mind.
This document targets semantic convention authors, not the instrumentation authors. So, instrumentation authors can make them dynamic. Semantic convention solders cannot.
And Dan… It's… this point is, yeah, irrelevant. You cannot do this.
**Trask Stalnaker** 27:18 Oh, I see. So, maybe, Robert, that's what you were getting at, the low cardinality.
That's almost more like a… Back.
thing for people using writing their own stuff, yeah, as opposed to semantic conventions. Okay.
Makes more sense to me now.
**Liudmila Molkova** 27:45 But then, if it, if it targets semantic convention authors.
**Trask Stalnaker** 27:49 Yeah, I would just remove it.
I think.
Kind of similar, like, line 406, When recording events from an existing system… Would we have… does this target semantic convention?
Is this relevant to semantic invention?
authors… I mean, I guess it could be, like, if we're defining bridging… Trying to think what we've done for bridging stuff before.
**Liudmila Molkova** 29:21 For bridging, we would not define an event, because we're not defining event name, right?
**Trask Stalnaker** 29:28 Right.
**Liudmila Molkova** 29:32 So, I'm almost thinking, okay, there is some, let's say, platform that Provide some platform-specific events.
I don't know, connection established, or something removed.
**Pellared** 29:44 But I think there's one thing. One is bridging local libraries, and second is bridging some systems which are about eventing.
So I think it's a diff… and here, we can bridge the event names.
**Liudmila Molkova** 29:58 Then they would just follow the existing guidance.
**Pellared** 30:01 Yes.
**Liudmila Molkova** 30:01 How to define the conventions for their.
**Pellared** 30:04 Exactly.
**Liudmila Molkova** 30:07 What do we have there? Like, should we just…
**Pellared** 30:10 Exactly what… I think exactly what you, Sassy, or what you told.
**Liudmila Molkova** 30:17 But then, it's, it's like…
**Pellared** 30:19 even…
**Liudmila Molkova** 30:19 Okay? Just, just… It's already there.
It's nothing special.
So this, this provides no value, right?
Just when you define event.
Pick a good event name based on whatever properties of the… of the thing you want.
**Pellared** 30:57 The value of it is that It's allowed to breach events.
I think that's the only value. That's… it's acceptable and allowed, that you can have some, I don't know, a collateral component which does it.
And people would not ask, oh, can I do it? Can I, you know… Change something from external and marketers event.
**Trask Stalnaker** 31:24 So I guess it… the… Question that we're kind of getting around is… is semantic conventions.
just what we define in Weaver.
Going forward… Or is semantic conventions… a little bit.
broader… Right, like, Weaver definitions couldn't cover this.
**Pellared** 31:53 I covered.
**Liudmila Molkova** 31:53 What, like…
**Pellared** 31:54 I think that this sentence could be moved to the spec.
I think we have some information about the bridging, even of the locks in this pack, if I'm not mistaken.
**Liudmila Molkova** 32:07 And then if you're bridging something, let's say there is no weaver in the picture, you are bridging some events, like OS events.
Yep. You can write a play in English to express how you map OS events to Telemetry. How you record this on telemetry.
And you still can use this guidance.
to say, Okay?
For OS event identified by these three different properties in the OS event, I'm… Putting this thing says event name.
**Trask Stalnaker** 32:46 Right, and so is that… And is that… a semantic convention…
**Liudmila Molkova** 32:55 It is, semantic convention that's documented in… plain English, so it lacks… it's a documentation, right, not a semantic convention, but you can follow the guidance We have and still produce decent documentation.
and telemetry.
**Trask Stalnaker** 33:27 Yeah, I guess I was kind of getting back to the… or the similar question we had with the event name of… Like, there's… You can define a convention To have, like, a num-parameterized event names, like, like this mapping could be the event name Here, says that it could be a combination of dynamic things.
And… So far, we have… I agree that this… blah, this has so far been under our definition of the semantic mentions repository.
But I'm… Just kind of curious.
as we go forward, like, and as we're leaning more and more, more into the tooling, Weaver tooling.
Policies, enforcement, all of that stuff.
Do we want to… restrict… What we mean by open telemetry semantic conventions, To specifically mean… Something that is modeled via… Weaver YAML.
And that's not necessarily a question for… Us now, or this group, or anything, just kind of the topic made me… Think about that for the first time.
So I had to verbalize it.
**Liudmila Molkova** 35:12 And I, I think the… The Weaver is a tool, right? We had built tools, and now we have Weaver, and maybe there will be something else in the future, but the formal schema that's validatable and checkable Kinda makes sense to me, because… Yes, you can express it as a documentation, but you cannot test against it, you cannot have it on your schema URL, right?
And then it kind of means that your documentation is not… it's just a documentation, and not… not… not a convention.
Yeah.
**Trask Stalnaker** 36:07 Currently, log bridging is… Robert, you were saying log bridging is defined in the specification repo?
**Pellared** 36:16 I think it's the only place, if it's defined, I think it's only there. And I also think that this sentence would fit very well in the logs data model.
**Trask Stalnaker** 36:29 It would be what in the logs data model?
**Pellared** 36:31 I think… I think we could move this, like, this paragraph to the logs data model, the event name, or somewhere.
Yeah, I think even in this appendings, there was something about bridges as well, and here I thought about, I think I…
**Liudmila Molkova** 36:56 Yeah, sorry, I'm…
**Pellared** 36:56 I think we could just, if you have this event name here, you could find it.
CS field.
I've… I think we could even add this paragraph here.
Could you check if there's something about bridging, or is it only in the appendings?
**Liudmila Molkova** 37:14 There is a mapping, yeah, and there is…
**Pellared** 37:16 But these are just examples.
I think there may be some guidance here, even in this data model.
I think the data model, there was also something about bridging… about bridging separities and things like that.
Nothing. Oh, that's interesting.
**Liudmila Molkova** 37:37 I think it's in the SDK.
**Pellared** 37:40 Mate.
**Liudmila Molkova** 37:42 Is it just the infancy?
**Pellared** 37:44 and I don't think there's any comment.
I think there's only the appendix then.
**Liudmila Molkova** 37:51 for appenders… Mmm…
**Pellared** 37:59 For sure in the overview.
**Liudmila Molkova** 38:03 Alright.
**Pellared** 38:06 Good afternoon.
**Liudmila Molkova** 38:08 Yeah.
To build Vogue appenders. Okay, this is a glossary.
Listen.
**Pellared** 38:22 But there is nothing normative here, as far as I remember.
**Liudmila Molkova** 38:26 There should be a normative… Normative thing on the logger name, if I remember correctly.
**Pellared** 38:34 I don't think it's normative, and for the name, I'm pretty sure it was the data model.
Or maybe SDK or API.
When we are getting…
**Liudmila Molkova** 39:06 Oh, standalone logs, by the way.
And the one is probably a spec, but the spec language at the.
**Pellared** 39:12 Yeah.
**Liudmila Molkova** 39:13 distinguish it from span events.
**Pellared** 39:19 instrumentation scope, was there?
**Liudmila Molkova** 39:24 Oh, the instrumentation, right.
**Pellared** 39:28 Artificial data model.
All the females were tricky to the parallel.
**Liudmila Molkova** 39:35 In the data model.
Yeah.
**Pellared** 39:42 So, probab- so probably it's not here, so… maybe using the API?
API MD.
Yes, I found it. I'll put it in Zoom chat.
Oh, you have it already. Logger provider, and here, get a logger, and name.
For log sources, would you define a logger name? The logger name should be recorded as instrumentation scope name.
**Liudmila Molkova** 40:25 Should we… should we just have a section?
That just tells how to implement login breach, or maybe it's… it has a low value because everybody already did.
And maybe it will be an enormous bike-sharing discussion with listing all the different caveats That in different places, would it be helpful?
**Pellared** 40:51 I kept.
**Liudmila Molkova** 40:52 Five years ago.
**Pellared** 40:53 worthy? Yes.
Yeah, I created an issue for it.
And I never got energy to write it.
**Liudmila Molkova** 41:06 Yeah.
And that's also a hairy problem with the log bridge name, or instrumented library name, or instrumentation library name, and everything of the sorts. Yeah, and the… All the other things, the unnamed parameters.
**Pellared** 41:25 Gotcha.
**Liudmila Molkova** 41:26 other things, yeah.
Yeah.
Okay, rolling back to the… events. The spec would be a good place to say that the event name is, I don't know, compile time constant.
Or…
**Trask Stalnaker** 41:47 low cardinality.
**Liudmila Molkova** 41:48 Low cardinality, yeah.
**Pellared** 41:51 Yep.
**Liudmila Molkova** 41:54 And that… The bridges are not expected to do anything about it. If user provided it through attribute, then we have this hotel event name thing.
But if it's a low cardinality, then it also means that mapping from something external However you map it, even if it's in runtime, you should produce something, must produce something of a low cardinality.
Wow.
In theory, you can produce metric… metric pain.
**Trask Stalnaker** 42:27 What do we even say about cardinality in the spec, or… like… I guess we do say things, like, span names should be low cardinality, like… .
**Liudmila Molkova** 42:41 And then yes. Non-enforceable.
**Trask Stalnaker** 42:43 non-enforceable.
Stuff.
I remember there being a lot of discussion about That the spec should or shouldn't include things that are… Not enforceable.
Or there should be documentation.
**Liudmila Molkova** 43:00 Yeah, I don't think we even say it should be of a low cardinality. We say it's significantly, oh, sorry, statistically… Whatever, the grouping key.
**Trask Stalnaker** 43:10 Oh, yeah, yeah, yeah.
**Liudmila Molkova** 43:41 I think… I don't know, but I don't think we say it. I think it's gonna be kind of implied by… Like, you would normally hard-code the value.
But if, if we, if we do… say that. We probably should say it for the Everything.
the… every identity.
Future span type, magic name, event name, entity type.
And so on.
**Trask Stalnaker** 44:36 Hey.
I think it's… I hope… I think it's… find, Punt a little bit on it.
Hmm.
I don't think it necessarily has to be said, but if… Do you want to, Robert, wherever you think that makes sense.
There is some more stuff about… there's a few more sections in here about external systems.
And… So… Wondering again about.
**Pellared** 45:12 sessions or specification.
**Trask Stalnaker** 45:14 Yeah, whether… or, you know, just… even here, even if we want to have it in semantic conventions as a separate section about map… ex… mapping external systems, And I guess there's kind of a… Like, the… say the part about, severity, I was just… Reading over the severity text piece.
And how, you know, that could be from an external system.
And yes, if we're bridging.
I would expect that, but, like, say an external system has, like, a schema, an event schema defined, and we're just mirroring that event schema in… Open telemetry, I'm trying to think if we would… why would… Would we want to use the severity text originally?
Or do we even have the severity text?
**Pellared** 46:26 I think, One reason… Is that, There may be not a 1-1 correlation.
I mean, not… they may be, you know, a wider range of the severity, it can be also multidimensional.
in some systems, they may be, you know, different, you know, aspects of the severity, the MB2, for instance.
I remember that somewhere, in some system, there was something like urgency, and… you know, urgency, impact, stuff like that, you know. Like, one was saying, like, what is the impact? If it's, like, say, similar to the risk analysis, like, you have something, like, kind of probability and, you know, impact, and I think I saw something similar to existing system.
Other thing is that someone who reads it You know, reads, you know, the logs somewhere, maybe more familiar with this kind of information, with this, you know, bridge data model.
Oh.
Java.
**Liudmila Molkova** 47:35 The Android has WTF?
That's funny.
**Trask Stalnaker** 47:42 honey.
What a terrible failure.
**Liudmila Molkova** 47:46 I like it.
**Trask Stalnaker** 47:47 For sure.
**Pellared** 47:49 Monitorable.
**Liudmila Molkova** 47:52 I was thinking SEV0, or something like that, but it probably deserved its own attribute, not a tag.
**Trask Stalnaker** 48:03 Yeah, just, again, trying to draw this distinction between if it's a bridge something versus if it's a… If we're really modeling it in semantic conventions… as a… as an event.
**Pellared** 48:26 I am really leaning towards, you know, describing it in… the appendix of specification or the data model, because I feel that it's better to focus here, not on the bridging, because I think otherwise this document will be too confusing, and even if someone will use, you know, LLM to generate some new events may mistakenly use it for some things.
And the more, you know, the more precise this document will be, the probably better it will be for the readers, and I think…
**Trask Stalnaker** 49:00 Yeah, we can always come back, and if we do… want to define semantic conventions for bridged, or some bridged events, we could… Address it at that point.
**Pellared** 49:15 Agree.
**Liudmila Molkova** 49:17 Yeah, so one of the approaches I thought about this document is that the guidance we already know.
And we can… Oh, almost always add more guidance once we know something else.
**Pellared** 49:32 I added this one only because the events MD section contains something about external events. That was the only reason why I started focusing on this.
That's for the completeness.
**Liudmila Molkova** 49:48 Yeah.
**Trask Stalnaker** 49:50 Let's remove it all.
**Liudmila Molkova** 49:56 If I will manage to do this… oh, what's going on?
**Trask Stalnaker** 50:02 Too much AI.
**Liudmila Molkova** 50:04 Not too much AI, also too much new keyboard for me.
**Trask Stalnaker** 50:10 I get weird.
**Liudmila Molkova** 50:13 browser.
**Trask Stalnaker** 50:13 or AI.
pop-up-y things that I'll like.
I did not ask for you.
**Liudmila Molkova** 50:35 Cool!
Anything else?
**Trask Stalnaker** 50:41 I left a couple of… Hmm… comments, I think they were small, I don't remember now.
Oh, you know, one was about external, so that's irrelevant now.
They were both about external, look at that. So, they're both irrelevant now.
**Pellared** 51:05 elephants.
**Liudmila Molkova** 51:06 what I meant here is that, let's say we record Something like, important operation ended.
Then you would add error type to the definition, not to the occurrence.
So this is about…
**Pellared** 51:24 Thank you.
**Liudmila Molkova** 51:25 define.
**Pellared** 51:27 I see.
Okay.
I see. That needs to be documented as part of the semantic conventions, but not included in the telemetry.
when I say…
**Liudmila Molkova** 51:40 Yeah, that… yes,
**Pellared** 51:42 I see. Makes sense.
And, yeah, important thing to us.
**Liudmila Molkova** 51:58 Sorry.
**Pellared** 52:10 Yep.
**Liudmila Molkova** 52:16 God, Pilot didn't like it.
I mean, must not, but we have the escape hatch for the… Diagnostic ma- the, the user… Friendly version of event representation.
**Pellared** 52:50 Yes.
**Liudmila Molkova** 52:54 So, they couldn't say… so, like, let's say we def… we're defining internal open telemetry SDK, misconfiguration event.
it would have maybe a structure, and it could be… it sometimes is written to a CD out or some other Place where users would consume it from, like, like, a text.
And it would make it…
**Pellared** 53:23 Is it only about recording, or do you want to define these somatic conventions what the body should, I don't know, represent, or I don't know what should be put there, because this is something which I was not sure, because I also found this other issue where you wanted to remove this, you know, usage of body, so I was just not sure.
once you want to have the semantic convention? Is it only about instrumentation, that if an instrumentation library wants to, you know, oh, I just want to add this body addition to addition… in addition to the semantic conventions.
Or is it something that the semantically says, oh, additionally, you can put a human-readable, you know, version Of this event, you know.
Sink straight.
Okay, your time.
**Liudmila Molkova** 54:08 I, I feel like, like, Okay, wait… So, we can start with this.
And eventually, change must not, because allowing something that didn't exist is okay.
on the other side.
Eventually, I think it would be good for semantic convention authors to think, oh.
Is this event mostly consumed in, like, aggregated version? Is it… should it just be structured, or there are important use cases where people will read it? Like, if I'm writing a console application, then my events could be both.
And then they could say, okay, it's actually also recommended to provide a body that is formatted in this way.
**Pellared** 54:59 then I might change it to the previous version which was in EventsMD, that must not define a value for body, except, you know, just copy-paste what we have already, the general EventsMD.
**Liudmila Molkova** 55:15 Yeah, I would prefer that, but also, if you want to start with must not, I don't mind. I think we should capture… we should keep the decision that we fought so long for that it's okay.
**Pellared** 55:29 Yes, let's, let's… then I bring it back the same language, which is in the Eternal Events Indies.
**Liudmila Molkova** 55:36 Yeah, nice.
Things.
**Pellared** 55:41 Could you put a comment, just in case I do not… I do not… I don't forget?
Let's use the language, yeah.
That's insane.
**Liudmila Molkova** 56:15 Okay, we managed to spend a whole hour on it, I hope. I think it was very useful. Thanks a lot.
**Pellared** 56:21 Thank you for your help.
**Trask Stalnaker** 56:22 Yeah.
**Liudmila Molkova** 56:23 Okay, thank you.
**Trask Stalnaker** 56:25 Thanks for driving.
Both of you.
**Liudmila Molkova** 56:27 Okay.
Yeah, thanks, see you.
**Trask Stalnaker** 56:30 Fear.
**Pellared** 56:31 See you next time.
