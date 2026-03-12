SIG: Semantic Convention SIG
Date: 2026-01-12
Duration: 22 minutes
Zoom Recording URL: https://zoom.us/rec/share/xBGcGFAfh95pk_73-8hII-4WFVM1TdbD1igNEVKTeZnaWghiMVDAURkyK6Ssb1G8.4TTzTiNrDuEBpwF6
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 01:39 Hi, Josh.
**Josh Suereth** 01:41 Hey, can you hear me?
**Christophe Kamphaus** 01:42 Yep, I can hear you.
**Josh Suereth** 01:48 My new laptop finally, came, and… The dead one's gone. So now I can, I can talk with my laptop instead of calling in.
**Christophe Kamphaus** 01:57 And you're all set up.
**Josh Suereth** 02:01 That's always fun, the, the whole, like, restarting experience, right?
**Christophe Kamphaus** 02:07 Yep.
**Josh Suereth** 02:09 Alright, I'm gonna pull up the notes… I assume we're getting a slow start today.
**BhupinderSingh** 02:34 Okay.
**Josh Suereth** 02:39 Sweet.
**BhupinderSingh** 02:43 Just myself, who've been there, and I have joined this meeting first time, and just joined TNCF as well.
I'm looking forward to contribute.
And to, you know, a good first-issue tasks.
11.
**Josh Suereth** 03:01 Yeah, welcome, welcome.
**BhupinderSingh** 03:02 Thank you.
**Josh Suereth** 03:03 Yeah, we might have a, Smaller day today, so we could, We could go into some question and answer if you want. Normally, what we do is we spend the first bit kind of triaging And then there's a document, you know, with agenda items that you're free to add to.
But yeah, let's see, let's give it another minute for some folks to join.
And then… We'll get started.
Okay.
I think… I don't know if we have enough folks for this discussion, but I'm gonna bring up the first topic here.
which is deprecating RPC message events. I don't know if folks saw this, but… there's a PR to remove the RPC message events that currently exist in SEMCOV.
For context, this is, like, when you're tracing.
You would send a me- you'd send an event that would say, like, hey, a message was sent, and here's how many bytes were included in that message.
as an event to debug that messages were going back and forth, like in streaming RPCs. So, the… Depending on the instrumentation, you might only know the on-the-wire size, it might be difficult to know uncompressed.
there's a bunch of other things around it. So the proposal here is that they want to deprecate these events as they exist, and new instrumentation will not emit these messages at all.
I made a comment, which is basically, like, in practice, when we do RPC tracing.
The thing that we find most valuable is when you actually… Put the whole message there, like, the structure of the message, the contents.
In the trace as well, so you can see what the heck was being sent back and forth.
Obviously there's complications of that. You can't just necessarily do that by default, or you need, like, storage where you can… Keep sensitive data, so… I'm personally a fan of us moving this direction, and moving towards the new RPC semantic conventions, and maybe changing, you know, getting rid of what we have now, and then moving to something better in the future.
Anyone have thoughts or comments they want to make?
**Christophe Kamphaus** 05:40 What about retries? I think that was also… A related topic to this, or to… Model set.
**Josh Suereth** 05:52 Good question.
Let me make this a little bigger. I don't remember if this actually calls out retries, client-side. In the case of retries, messages can be re-sent. These should be attached to a per-try span, so they're actually going to have a different span per retry.
It's a good question. Feel free to ask on the, on the thing as well.
Okay.
I'm gonna move on.
Mmm… So… consider cutting a new SEMCOM for lease. I think this is actually something, we need to do. I'll take an AI.
I don't know if any of the other maintainers are on the call.
Just for context, semantic conventions, we don't… we release kind of on an ad hoc basis.
So we don't necessarily just, like.
have a timer that releases, the maintainers have to decide to cut a release, and I think we took a little break over the holidays.
So, I believe we're a bit stale right now, so it makes sense to cut a January release. I'll throw out, a call-in chat for folks. This is a notice to people in the SIG, or people watching the video, that, yeah, if you have anything you want to get in the release, please let us know. I'll put out a CL to cut a release this week, and we'll try to get that through.
Alright, Christoph, do you want to talk about guidance on OTEL SimConv?
**Christophe Kamphaus** 07:49 Yeah.
It came up in relation to adopting CICD SAMconf.
**Josh Suereth** 07:55 And, I opened this ticket for it, and…
**Christophe Kamphaus** 07:59 As examples, how other Six did it, I linked here to Gen AI.
And the question I have is… Usually, the 6 also say, as of this sum conversion.
And, I'm not sure what that's about. Is that when it has first been introduced, or is it as Random or an arbitrary version from which they want to remain stable.
**Josh Suereth** 08:29 Yeah, so that… that relates to… we had a lot of semantics conventions get added to OpenTelemetry, like, 4 years ago, and they never change for 4 years.
And people got the idea that they were stable.
But we had never actually looked at them and decided to commit to them, or that they were good.
They were just, like, the first implementation. They were marked experimental and stable for 4 years.
Even though they're still marked experimental. So, those de facto stable ones that lots of people rely on.
You picked the version before you started breaking them.
So, it's not quite arbitrary, there's, like, there's a thought behind it. So, like, with RPC, for example, they decided to start making changes to RPC to fix it. But RPC has been stable since they were submitted. I think I submitted them back in, like, 2020, or something like that. So, they're old, is the TLDR.
But we have learned a lot since then, and we're kind of changing them. So, what you do is you pick that version where you're gonna start breaking something that a lot of people might rely on, even though it's marked unstable.
And you say, cool, we are not gonna break anyone who's using that. What we're going to do is provide a migration path to the thing that we're gonna define where we want to be.
So, you're effectively treating that old set of things as stable.
For CICD, since you are brand new.
You might never have gone through that, like.
issue where people are treating an old version as de facto stable.
So you might not need to do this.
**Christophe Kamphaus** 10:07 For us, it's more… there might already be some vendor, some conf, That were… Used.
And so it would be a breaking chain for them to adopt the hotel sum conversion.
**Josh Suereth** 10:22 I see… like, there might be a vendor that had some sort of CICD thing that they were using, and then OTel Semcom's different. That's fine. That's on the vendor, then, to provide a migration path, if they want.
So, like, that's not… that's not on you to provide that for OpenTelemetry itself. I guess my question would be, like, has CICD progressed fast enough? Do you have a lot of people depending on things that will break when you go to stabilize?
**Christophe Kamphaus** 10:48 We haven't had any real breaking changes yet.
**Josh Suereth** 10:52 Yeah.
**Christophe Kamphaus** 10:54 It was… we had a few breaking changes, but that was… before CICD SAMConf really started.
There was a deployment name, if I remember right.
**Josh Suereth** 11:06 Oh, God, that one. Yeah, that was one… that was one we probably should have put… Behind a flag, but that's a different story.
**Christophe Kamphaus** 11:16 So, yeah.
So if I say… I guess we wouldn't yet need the… environment variable, some kind of stability opt-in.
**Josh Suereth** 11:30 I… I don't think you need that.
Yet.
there is… there is a change coming to OTEL around stable by default, where all features that are unstable have to be opted in.
Right? So, if you download a distribution of anything.
The default stuff that's turned on can only be something that's stable.
So, but that hasn't landed yet. That will impact you.
Unless you're stable before that hits, in which case everything's fine.
But the reason for that stability opt-in is, like, when you have two versions of your semantic conventions, the de facto old and the new, you need to give people the migration path to go from de facto stable to new stable.
**Christophe Kamphaus** 12:26 And so you need that opt-in to have them go from A to B.
**Josh Suereth** 12:29 For CICD, I don't think you guys have that. I think you just have experimental and you're going stable.
And so I think you're fine. From my perspective, you're basically doing a 1.0 of CICD stuff, right? So you're doing a release where you're gonna mark things that were beta is stable.
**Christophe Kamphaus** 12:48 Yeah.
**Josh Suereth** 12:49 Right. If you ever make a 2.0 of CICD, then you would use an opt-in to control when to go from one to the other. But I don't think you need one right now.
be… and that's my rationale. But, happy to hear from others if anyone else has thoughts here. I saw Armin join the call, I don't know if you… Have thoughts about stability here.
**Armin (Dynatrace)** 13:12 Oh, sorry, I missed the beginning, I joined a bit late.
**Josh Suereth** 13:15 Oh, it's fine, it's fine. We're talking about, wait, what am I… Sharing the wrong.
**Christophe Kamphaus** 13:21 You are not sharing CM.
**Josh Suereth** 13:23 Yeah. We're talking about guidance on some kind of stability opt-in.
I'll put some notes here of what we said.
Wait, why is this not… Whatever.
**Christophe Kamphaus** 13:43 Yeah, and my question was here, if a vendor was already using OpenTelemetry with their own conventions.
And they wanted to migrate and adopt the open telemetry semantic conventions for CICD.
Could we, propose there?
An opt-in for that?
Knowing that we are still… experimental in CICD.
**Josh Suereth** 14:17 I mean, you…
**Armin (Dynatrace)** 14:18 We're trying to.
**Josh Suereth** 14:18 Good.
**Armin (Dynatrace)** 14:20 Experimental to a stable version, right?
**Christophe Kamphaus** 14:23 Yeah, we are in the process of, getting vendors to adopt.
our CICD convention so that we can move towards stability.
**Josh Suereth** 14:46 So, I think the reality here is that that opt-in is going to be vendor-specific. So, this opt-in that we call out is for instrumentation that OpenTelemetry provides. So I'm going to say that again, right? Like, if a vendor's providing instrumentation that did CICD, They control their migration guide, they control their flags, they control all that. You don't need to provide that for them.
They figure that out.
when you are making changes that will involve OpenTelemetry itself, like our project, our stuff, that is where this flag comes in. So if you're going to do something that affects the Java instrumentation agent, the collector, whatever, that's where you have to provide that path from A to B for OTEL instrumentation. But the vendor… we don't control the vendor.
All we can do is say you're compliant or you're not.
**Christophe Kamphaus** 15:31 Okay.
Good to know.
Thank you.
**Josh Suereth** 15:38 Cool.
Alright, and then next we have, Sudarshan Soma. I don't know if you're on the call?
Sorry, I can't see the call at the same time.
**Sudarshan S** 15:52 Hi, hi Josh. Hi, Adaste. Can you hear me now?
**Josh Suereth** 15:56 Yep.
**Sudarshan S** 15:58 Yeah, so, yeah, I'm just, so this was a PR on, database, oracle database semantic conventions.
So, the initial version, the semantic spec was in… not at stable.
So meanwhile, So, I got some inputs on… from Ludimila, I got some input. So, based on those inputs, I raised this PR to modify Are they namespace definition and some other… So, I mean, I had an internal review with Oracle, our team, and… So, finally, I drafted this mail, this PR, with all the changes, so requesting… Whenever I get time to review.
Yeah, this would help us to…
**Josh Suereth** 16:56 Is there anything you want to call out? Like, is there any contention on it so far, or comments that you addressed that you think are relevant for us to know?
**Sudarshan S** 17:05 So initially, the DB namespace had a definition wherein I mean, it was defined so that it has the service name, so we appended service name and instance name, so those parameters now, currently, now in this PR, it was separated. Earlier, they were merged in a single DB namespace, the instance name, service name, and PDB name.
So, now they are separated as per the inputs, given.
So that is the main change. I mean, to separate it is also an input.
from Ludim… Ludi Milan, so… That's where, I raised this PR.
**Josh Suereth** 17:58 Okay.
Cool. Do we have an active database semantic invention group, or is this on the general maintainers again?
I don't think Trask or Lyd Miller are here to answer that, unfortunately.
**Sudarshan S** 18:15 Yeah… Yeah, the initial one, yeah, it was merged. I mean, it was reviewed from, mainly… Ludimena, she has reviewed… So… Yeah, she has all the context about this, so… Just, I thought I would just request her if she get… A chance, she can take a look at this.
**Josh Suereth** 18:46 Alright, I'm gonna mark you in awaiting Code Owner's approval.
So that you actually are part of the triage process. This was triage declined.
And I think it was because… yeah, we don't have an active SIG. Okay.
So, actually, I need to move you to, Needs more approval, because we need general maintainers to look at this.
**Sudarshan S** 19:11 Okay.
**Josh Suereth** 19:12 Yeah, we did, like, yeah, what happened was, we don't have, the Oracle we don't have a database SIG that's active right now that are reviewing PRs and, like, taking changes, so we had discussed this, and you, like, you need sponsorship from general maintainers, and that's fine, it's just, I think this fell afoul of the PR process there, where it got… it got cut, That was in December, yeah. Alright, so you're now… it needs more approval, which means, when we go through and do triage, one of the general approvers should look at it. You still need to get two of us to approve before it goes through.
Cool.
Thanks for raising it.
**Sudarshan S** 19:53 Yes, yes, sure.
Yeah, thank you. Thank you. Thanks for your time.
**Josh Suereth** 19:58 Alright, and then, We don't have anything else on the agenda, so… wanted to throw out, you know, if anyone wants to ask questions or has general things to say, I know, we have at least one one new member joining who might want to discuss things or ask questions about how this works, feel free. Otherwise, we'll call it.
**BhupinderSingh** 20:31 So, I'm good, I think.
I'm just observing the meeting, so I'm good, no questions.
**Josh Suereth** 20:41 Awesome. And how do I pronounce your name? Is it Bupinder?
**BhupinderSingh** 20:44 Open this thing, yeah.
**Josh Suereth** 20:45 Upinder Singh. Okay, awesome, nice to meet you, thanks for joining, and Yeah, look forward to your contributions going forward, man. Let us know if you need any help.
**BhupinderSingh** 20:55 Sure, thank you.
**Josh Suereth** 20:56 for everyone else, I'm gonna take the time that this meeting, isn't, and try to cut a release for Semantic Convention. So I will send a PR out. If you all have a chance to take a look at it.
**Michele Mancioppi** 21:08 Wait, wait, wait, wait, wait, wait a second. I'm almost there with the service that appears the name.
I'm literally merging in the branch to ask things, please don't do that to me.
**Josh Suereth** 21:20 I can… I can still make the PR, with, like, possible changes, and you can say blocked on this, but yeah, I'll wait until… so you… you have the ability to merge it?
**Michele Mancioppi** 21:30 No, I mean, UN Trust both approved, and there is a last draft of, Of comments that I'm addressing.
**Josh Suereth** 21:37 Okay, ping me… ping me on Slack then, once those comments are addressed, and I'll merge it, and then I'll cut the PR. But yeah, we're just looking for… yeah, I like to send the PR out and just ask people, like, what… what you want to see in the release, and if there's anything close, you can block my PR on your PR.
Cool.
Yeah, and it's good to see that one go out, too. Alright, thanks, everybody.
Have a great day.
**Christophe Kamphaus** 22:03 You too.
See you.
**Sudarshan S** 22:07 Thank you.
