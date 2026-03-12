SIG: Rust SIG
Date: 2025-09-16
Duration: 18 minutes
============================================================

## Zoom Recording Transcript

**Scott Gerring** 03:07 Sorry, Bjorn.
**BA Björn Antonsson** 03:11 No worries.
**Scott Gerring** 03:18 I don't know if any of our Microsoft colleagues are joining.
Should we have a real quick chat, then, seeing as not many other folks are joining?
**BA Björn Antonsson** 05:21 Sure.
**Scott Gerring** 05:24 The first point on the list, the circular dependencies between Tracing OTEL and OpenTelemetry append tracing.
Which one of you was that?
**BA Björn Antonsson** 05:35 That's me. Of course.
**Scott Gerring** 05:37 It's always you.
**BA Björn Antonsson** 05:39 Yes, when it's tracing open telemetry, it's always me. So I'm trying to clean up the fields and the methods in the span builder.
And, of course, I can't run LIN, because the, the OpenTelemetry appended Tracing is including the old… tracing OpenTelemetry Create, which uses fields which don't exist, because I just removed them.
Even though I can… I can compile the main branch of that project with my changes, because, yeah, that works.
So, I mean, I don't know how to proceed. I can't open a PR, Because I can't depend on, on, on, the bike… the OpenTelemetry appended Tracing Create can't depend on anything that's not been released yet.
when we do a release. I mean, I don't know why it's in there. I said that before. It shouldn't be.
Or we should just have a tracing OpenTelemetry bridge inside OpenTelemetry as well, so we can do all the changes ourselves.
At the same time, but… Yeah, that's where I'm at.
**Scott Gerring** 07:07 Unsurprisingly, I don't have any deep insight for you on that one.
**BA Björn Antonsson** 07:13 Circle dependencies, yay!
**Scott Gerring** 07:16 Yeah, it's not a… it's not a thing that I've solved in my free time, unfortunately. Yeah.
it's still… It's still a really big mess with the tracing stuff,
**BA Björn Antonsson** 07:28 Yes.
Have they… Sorry.
**Scott Gerring** 07:32 Has the other side been released since that PR was merged of yours?
**BA Björn Antonsson** 07:36 No, it hasn't.
I guess they're waiting for a new.
**Scott Gerring** 07:45 OpenTelemetry release.
**BA Björn Antonsson** 07:47 Yeah.
**Scott Gerring** 07:49 Yeah, and you're trying to do the interface cleanup on the span builder, hey, that's got that long-running ticket open?
**BA Björn Antonsson** 07:54 Yes, exactly. And it's also interesting because, I mean, there are things being done in the appender that won't… that you can't do anymore, since some of the data it's pulling out is now… Not public.
After the changes that… that I did.
And the changes that, blood I wanted.
**Scott Gerring** 08:24 I'm still… and this is probably just because I've lost context a lot, the existence of the two different bridges still confuses me a bit.
**BA Björn Antonsson** 08:35 Yeah, I think so as well. I think there should be one… one layer with features for all the different things. You can turn on and off whatever you want.
**Scott Gerring** 08:47 That would certainly be a bit more intuitive.
And it would be easier if it had the same release lifecycle as OpenTelemetry itself, huh?
**BA Björn Antonsson** 08:56 Yeah.
**Paul Le Grand des Cloizeaux** 09:01 Hey.
**BA Björn Antonsson** 09:02 Yeah.
Hey, Paul.
**Scott Gerring** 09:04 Hey, Paul.
What should we do for this?
Do you… have you written it on the issue?
**BA Björn Antonsson** 09:13 No, I haven't. I'm gonna write it on the cleanup issue.
**Scott Gerring** 09:17 Yeah, that's… I mean, yeah.
I think it'll be interesting to see Joe, because he cares deeply about cutting back public API surface area, and…
**BA Björn Antonsson** 09:28 Yep.
**Scott Gerring** 09:29 Yeah.
Probably worth flagging it there and hoping that we end up with him on one of the calls again soon.
**BA Björn Antonsson** 09:37 Yep.
**Paul Le Grand des Cloizeaux** 09:39 Hmm.
**Scott Gerring** 09:41 Just trying to find the cleanup issue quickly.
**BA Björn Antonsson** 09:49 I have it.
1988 to 6.
I'll write something.
**Scott Gerring** 10:03 Cool.
Well, that's that one not dealt with. The thing I wanted to speak about briefly was that we probably should do a better job at issue and PR triage, I think. There's just a lot that is open effectively forever, and hasn't even really had, kind of, like, basic tag.
triage done over the top of it, I think it would probably be in everyone's interests, including the communities to kind of burn through all of that as a priority, but I think it's probably also something that needs a bit of buy-in from the Microsoft folk.
What do you all think about that?
I take silence to mean everyone feels not very strongly about triaging things.
**Paul Le Grand des Cloizeaux** 11:02 Honestly, as someone who opens issues.
But he's not a maintainer here.
Or an approver, or anything. Probably that would be a good idea.
But, yeah.
I don't have any strong opinion.
**Scott Gerring** 11:23 Yeah, fair enough.
it's very hard for me to see the wood for the trees, like, there's a lot of stuff that ends up left open because of some kind of implicit context, like, oh yeah, Scott will actually pick this up again in the future for whatnot. But again, yeah, there's probably not much to be done with it, apart from talking to CJO and the Microsoft folks and working out.
What their mental model is in trying to… Kind of hone in on that.
**Paul Le Grand des Cloizeaux** 11:50 Yep.
**Scott Gerring** 11:58 Oops.
**Paul Le Grand des Cloizeaux** 11:59 Hmm…
**Scott Gerring** 12:09 And my other one was my never-ending quest to get the OTLP back-off retry stuff merged, but I… also the Microsoft folk for that.
Does anyone have anything else to talk about? Paul, you're here. Christian, you're here.
**Christian Leghadjeu** 12:26 No, I've been there for, like, 2 meetings.
But I'm kind of new to the… to the… to the… to the community.
Can you…
**Scott Gerring** 12:43 What was that story?
**Christian Leghadjeu** 12:45 I say, I mean, I'm kind of new, new to the community, so…
**Scott Gerring** 12:52 Are there any issues that you're having with OpenTelemetry that you would like help with, or are you keen to contribute, or…
**Christian Leghadjeu** 12:58 Yeah, I came to contribute. I say contribute.
**Scott Gerring** 13:04 Cool. I would suggest that you pipe up in the Slack channel.
in and say, like, hey, is there anything I can work on? And if you have particular areas of interest, that'd be a good place to flag it as well.
And then those of us in the maintenance group can think a bit about what's currently open and unblocked, and point you in the right direction.
**Christian Leghadjeu** 13:28 Yeah. Okay, alright.
**Scott Gerring** 13:36 Paul, how are you going these days?
**Paul Le Grand des Cloizeaux** 13:38 Good, good, good, good.
I haven't come in a while. I still… I think I still have some PRs open, right? The span processor reflector.
I guess, know that the minor release Has been done, right? The 0.30.1.
I've seen tags… Things being tagged, no?
**Scott Gerring** 14:04 I am a bit out of touch with the last release, to be honest. I've started missing these because of, family things, so I'm not quite sure.
**Paul Le Grand des Cloizeaux** 14:11 Yeah, you've got two that have been opened for Yonks.
Yeah, yeah, no, actually, the old 13th one hasn't been released. Well, anyway… What we said about them was that we would wait for the next breaking… release, the next, major release to merge them, and so, yeah.
**Scott Gerring** 14:36 I think they both need rebasing at this point. The second one certainly does.
**Paul Le Grand des Cloizeaux** 14:43 Mostly. Of course, of course.
But, but yeah, honestly… I am neutron.
Yeah, let's, lyrics… I'm not sure what he's… And then, yes.
But, he bumped… The… some packages to 0.30.1.
Release 2025, September 11. Oh, actually, they only released OpenTelemetry Protos and OpenTelemetry OTLP and not the rest, so yeah.
Interesting.
But yeah, it's been a while since I've been here, since I've come to the Sikh, so… I'm not up to date with it.
Thanks.
**Scott Gerring** 15:34 Yeah. Yeah, let's… maybe worth raising it in the meeting notes as well, and then we can ping it up to CJ so that he's kind of aware that there's a bunch of stuff that's… Open, that would be good to get in.
**Paul Le Grand des Cloizeaux** 15:49 Mmm… I think… I think so… Tell me, Bjorn, I think Igor also opened… a PR or an issue recently.
**BA Björn Antonsson** 16:04 Yes, he opened a pretty small PR to be able to… Iterate over parts of the tray state.
We're not doing copies, I think, so…
**Paul Le Grand des Cloizeaux** 16:20 And I, like… Us to be able to get, keys and resources without having to copy them.
I mean, to copy them, so that's, like, two small API changes or additions.
But, that's what you'd like to mention.
**Scott Gerring** 16:47 Oh, shocker on the list, I guess.
**Paul Le Grand des Cloizeaux** 16:50 Nope.
Hmm…
**Scott Gerring** 17:03 I guess if there's nothing else to discuss, I will wish you all a lovely evening.
**Paul Le Grand des Cloizeaux** 17:08 Yep, have a good day.
**Scott Gerring** 17:10 So…
**Christian Leghadjeu** 17:11 Have a good day.
