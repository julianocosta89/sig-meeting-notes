SIG: .NET Auto-Instr SIG
Date: 2025-10-29
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 03:00 Hello?
**Igor Kiselev** 03:07 I'm Lativ.
**Mateusz Łach** 03:09 There you go.
**Yevhenii Solomchenko** 04:17 Hi, guys.
**Mateusz Łach** 04:24 Hello?
Okay, it's been 5 minutes. PR3 is definitely not going to join today, neither is Zach. I'm not sure if you want to…
proceed with the meeting, or do we want to sync offline? Any preferences? Any topics you'd like to discuss?
In our current, hello.
In our current, standards.
**Yevhenii Solomchenko** 08:00 Maybe one important is about the MongoDB support new version.
**Mateusz Łach** 08:06 Okay.
**Yevhenii Solomchenko** 08:08 It should be in that version.
Automation? Like, nearest 3Ds.
Next one.
**Mateusz Łach** 08:20 Yeah, so I think it might depend on the…
depend on the effort that is required to support it. Based on Pyotr's comment, it seems like it might be, like, non-trivial.
Right?
So… I don't know. I think there were already…
There were already requests to release the… to release a new version with fixes that were done in the last few weeks.
So, I… and I think I'd responded that we want to basically release soon after .NET 10 release.
So, taking all that into account, I'd say…
Depending on how much of an effort it is to support the new version of the bytecode instrumentation, we might want to postpone it.
To the… And do it in some later release, in order not to, you know,
Delay release any longer.
**Yevhenii Solomchenko** 09:22 Does that make sense?
Yep.
**Mateusz Łach** 09:29 Okay.
Yeah.
I don't know, do we want to go over the standards,
standard agenda? I'm not sure if there is,
Considering there is only 3 of us, if we want to do it right now, or…
Or do we want to, I don't know, do it, but I'll sign, or…
**Yevhenii Solomchenko** 10:02 Okay, perfect.
Do it, in the next week.
**Mateusz Łach** 10:08 Okay, any preferences from your side, Igor?
Okay.
Yeah, so in that case, let's,
let's finish early today and sync offline on Slack, or…
Elsewhere, or on GitHub, and yeah.
Okay, in that case, see you next week. Oh, okay, Chrissy's here.
Hello.
**Chris Ventura** 10:49 Hello.
If you'd give me a moment, I can get set up.
**Mateusz Łach** 10:56 Sure.
Yeah, we were discussing, finishing early, but, glad you joined.
I'm not sure we can expect anyone else. Piotr and Zaka are definitely not joining today, and…
Not sure about that.
**Chris Ventura** 11:20 Yeah, is there anything in particular you want to talk about?
With the smaller group, or… Otherwise, I can just run through the agenda.
**Mateusz Łach** 11:31 Yeah, I don't think there are any other topics apart from the standard agenda.
We briefly discussed support for a new version of MongoDB client. Pot created an issue. Basically, it seems like we need to adjust the bytecode instrumentation, and again, he was asking if we want to do it in the
Basically, in 1.13 release, or some later release.
And, you know, considering there were already requests on Slack to release the current version, And,
based on Piotr's comment, it seems like it might be a non-trivial change to support the new version. I think it might make sense to add the support in some later release.
**Chris Ventura** 12:21 Yeah, I think at this point in time, we're spread too thin to commit to adding something like that with the next release. I think there's enough work to be done
With the current things that are in flight.
**Mateusz Łach** 12:37 Yeah, that makes sense.
**Igor Kiselev** 12:40 From my point of view, I'd like probably to share early
Heads up, so we plan to… fake.
So… I found some solution of, on assembly loading, for .NET.
NET applications. So, our current idea, while, we agree that proper fix would be probably to move us to a separate assembly loading container that work already started, but for the meantime, what we plan to do, create some options that would be opt-in features through environment variables, through other means, I don't know yet.
what, own, application startup to look through all trusted platform, assemblers list, the .NET form, so it would have a full list of assemblies that can be loaded in current application. Validate the version.
And for any version of assembly that we also have dependency to, where the version is not satisfy our requirements, we would preload our assembly in application
that very, very early stage, before area assemblies from Trusted Assembly, from Trust Platform Assembly list was able to be loaded. So, in that way.
it should… So, we hope that it would solve a problem, so…
Just sharing an idea right now, so we would plan to do it.
We'll see how it would be.
**Chris Ventura** 14:13 Okay.
Yeah, it probably makes sense to finish up the .NET Framework side of things first, try to get that out the door, and then…
dig into that idea that you just shared.
**Igor Kiselev** 14:28 Sure, it's… maybe at some point would be in parallel, because it may be not done by me, but by some other team members in our cases, so…
**Chris Ventura** 14:38 That would be fair.
**Igor Kiselev** 14:39 Yeah.
**Chris Ventura** 14:39 Yeah.
Yeah, I wasn't sure how many people you had available.
**Igor Kiselev** 14:46 Just a heads up.
**Chris Ventura** 14:54 Okay. Yeah, I'll just keep things short today, since we don't have the other maintainers available.
So…
Seems like we've made good progress on the .NET Framework story you've been working on, Igor. I haven't taken a look today to see if the,
Kyotar has responded to some of the comments that he's left, and that, with the changes that you've worked on recently.
But if… once those are resolved, I think it's looking pretty good.
And then, on the file-based configuration,
I think it's just, a matter of…
Going through some of the comments and some of the recent changes there.
**Igor Kiselev** 15:48 Thank you.
For your review.
Brief.
**Chris Ventura** 15:52 Yep.
Anything else you want to bring up, given some of the current PRs? I think I'm just gonna keep the meeting short today.
**Yevhenii Solomchenko** 16:09 Maybe one important pair is, firebase configuration at night.
implementations?
**Chris Ventura** 16:17 Okay, so that's the next priority.
**Yevhenii Solomchenko** 16:19 Yeah, and I've heard about, Like, specification stuff.
So…
**Chris Ventura** 16:28 Okay, if you give me a sec, I'll pull up that PR.
Oh gosh, why am I not seeing it?
Okay, if you're able to just send me the link in Zoom, I'll… I'll pull it up.
**Yevhenii Solomchenko** 17:10 Yeah.
Good job.
**Chris Ventura** 17:12 Yeah, thank you.
Okay…
Okay.
So… Yeah, instrumentation configuration…
Yeah, there's some… Debate on this.
spec side for… the behavior that Zach mentioned.
**Yevhenii Solomchenko** 17:54 Yeah.
**Chris Ventura** 17:55 Go ahead.
**Yevhenii Solomchenko** 17:57 I also like the presets.
Actually, about… Spectra.
Not agree with that, for now.
**Chris Ventura** 18:06 Yeah, my… Assumption is that most…
Auto instrumentation vendors today have the behavior where You enable as many…
Instrumentations as possible out of the box.
And, as a…
customer upgrades their version of Auto instrumentation, they automatically get the new instrumentations available without having to modify their configuration.
And so… With the way the… Declarative-based configuration has been defined.
It's kind of a deviation from that precedent.
So, Igor, I'm assuming that,
Your… your vendor's auto instrumentation solution.
Has that similar behavior, where you don't require configuration changes in order to… enable…
Some new library that you instrument?
With the new release.
**Igor Kiselev** 19:27 So… our proprietary software, we have a list of, just
how it may be used. We have a list, of instrumenters, most of the instrumenters are to enable always. Some of that, instrument… some of that instrumentation may be auto-disabled by default, and a user have a flag saying that they suggest enabled, where he could enable,
Enable or disable to overwrite our behavior by default.
So, it… it's in some cases, it may… it may be good to opt in into instrumentation if we are talking about some… a little bit more risk instrumentation, and in some cases, it…
So…
**Chris Ventura** 20:11 Yeah… So… I think… the… like, the main difference there is…
So, we have this instrumentation list.
And… You have to include it in your declarative configuration file.
If you do not, then you get no instrumentation.
But if you do, you only get the instrumentations that you've included in the list.
And so… As you upgrade.
if somebody doesn't add the new instrumentations to their configuration file, they won't get those new instrumentations automatically. And so for some people, that's desired behavior, and for others, it's unexpected.
And there's no way to opt in at this point into, say.
I just want the automatically available list.
If you're using declarative configuration, You'll only get the fixed list that you define.
**Igor Kiselev** 21:34 At the same time, it may be useful for some customers to fix a list which
We would like only so…
**Chris Ventura** 21:42 Exactly.
Exactly. So, there is a linked… Issue for the spec.
In this PR… So…
Yeah, I think it's this… this link here.
And Feel free to take a look at it.
comment on it.
But it's a way to… It's at least an option for people to opt into which behavior they want.
So… I've put some comments on here…
A few others have as well.
But, jack, explained… Some of the why the configuration behaves as it is.
Which makes sense.
But this is where there's a deviation from what a lot of vendors have done in the past.
So, it's just something to be aware of.
Let's see… Anything else you think should be called out in this PR?
**Yevhenii Solomchenko** 23:18 No, no.
**Chris Ventura** 23:24 So anyways, as you're reviewing it, it's just something to keep in mind, that this is the behavior, it aligns with the spec.
It may not be desired, from a vendor perspective, But it's where it's at.
Okay, well that's everything I have.
So let's get some time back today.
**Mateusz Łach** 24:02 Okay, thank you.
See you next week.
**Yevhenii Solomchenko** 24:05 No.
