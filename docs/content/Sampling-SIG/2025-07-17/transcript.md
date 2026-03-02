SIG: Sampling SIG
Date: 2025-07-17
Duration: 10 minutes
Zoom Recording URL: https://zoom.us/rec/share/ff9_nooSZ1oTExdJqb9mlPxz5BH6-8sxqJ0JRSZY-boyHjvLMtsAtbWqTjKng9au.E3EhziuUl3_nfs-q
============================================================

## Zoom Recording Transcript

**Kent Quirk (he/him)** 00:50 Hey, Peter, I'm just dropping in to say that my team is called a meeting I need to go to. So I'm not gonna be here. So just thought I'd say Hi! And bye. Sorry, bye.
**Yuanyuan Zhao** 01:08 Did the curve just leave.
**Peter Findeisen** 01:12 Yes, he has an important meeting.
He couldn't attend, really.
**Yuanyuan Zhao** 01:22 How are you doing, Peter?
**Peter Findeisen** 01:23 I'm I'm good. How are you?
**Yuanyuan Zhao** 01:26 I'm fine getting busy at work.
You are in the South California.
**Peter Findeisen** 01:43 Central California, near Sacramento.
**Yuanyuan Zhao** 01:46 Oh, okay.
that's Cisco. Right?
Cisco. Yes. Yeah.
So you've been with Cisco for a long time, or you're part of.
**Peter Findeisen** 02:03 Yeah. So I joined up dynamics 7 years ago. It was already acquired by Cisco.
**Yuanyuan Zhao** 02:12 Okay.
**Peter Findeisen** 02:13 So you know.
**Yuanyuan Zhao** 02:15 Where were you previously.
**Peter Findeisen** 02:17 Hewlett, Packard.
**Yuanyuan Zhao** 02:19 Oh, I should be.
**Peter Findeisen** 02:21 Yep.
**Yuanyuan Zhao** 02:22 You know.
Have you been with HP. For a long time?
**Peter Findeisen** 02:27 Yes, 20 years.
**Yuanyuan Zhao** 02:30 Wow!
**Peter Findeisen** 02:31 Yeah.
**Yuanyuan Zhao** 02:33 I. I spent 16 years in my previous company.
**Peter Findeisen** 02:38 Which was.
**Yuanyuan Zhao** 02:40 Google.
**Peter Findeisen** 02:41 Oh, okay. Yeah. Yeah.
**Yuanyuan Zhao** 02:43 And
it's a yeah. It's you know, when the place you stayed for so long, it's
like leaving became a bit sentimental.
**Peter Findeisen** 03:04 Right?
Yeah, it's yeah, long time.
**Yuanyuan Zhao** 03:13 Is everyone else joining.
**Peter Findeisen** 03:16 I don't see anyone, but I didn't see any.
**Yuanyuan Zhao** 03:23 Installation right, and I'll see that.
**Peter Findeisen** 03:30 I don't see anything in the Channel. No one is declaring their absence so hopefully. They will join.
**Yuanyuan Zhao** 03:41 Okay.
I want mute or a while.
No, they are not showing they are not showing as participants, so they haven't joined.
**Peter Findeisen** 04:00 Okay.
**Yuanyuan Zhao** 04:12 Do we have a set topic for the next set of things to work on.
**Peter Findeisen** 04:18 So I added 2 items to the agenda. They are both related to what I have been working on. One is
So there. There is a change to the Otep, 2 50, which talks about composite samplers. The I made the clarification and a small fix really.
It.
It was debated whether it's appropriate to change an autop. I
I think it's it's it is right. So it is a small change, not not
changing the idea. It's it's just clarification. And Josh.
I think, he said, that he would be supporting this change, but unfortunately
this pull request got expired. It got it got
Well, I don't know. I'm not sure what the right term is. It's frozen, not frozen. Something else
it can be reopened, apparently, but I do not have any way to do this on my my page doesn't show any option to reopen
this pull request. Oh, Carlos, thanks for for joining I'm discussing
my pull request, which got closed because of inactivity, and we would like to reopen it and.
**Carlos Alberto Cortez** 05:59 Let's do that. Yeah, give me a second
to check which one it was.
**Peter Findeisen** 06:11 It. It was open telemetry. Specification, pull, request 4, 5, 6, 9.
**Carlos Alberto Cortez** 06:21 Yeah, correct.
Okay, it reopened us.
**Peter Findeisen** 06:27 Okay. Great, thank you.
Yeah. Josh hasn't joined yet. But during the previous meeting he was saying that he would support merging it
because it it is a small change. Small clarification doesn't change the whole idea. It is. It just makes things a little more clear.
**Carlos Alberto Cortez** 06:49 Yeah, I guess that the obvious question, if we merge this tab or this amendment to the tab is whether we will need to also update something in the specification itself
is that something required there or.
**Peter Findeisen** 07:07 Yes, I think this this should proliferate to the specification. But so far we haven't, really.
I completed our work on the specification. So it it's still work in progress.
**Carlos Alberto Cortez** 07:24 I see. Okay, yeah, okay, that makes sense.
In that case, I would like that to have. Then.
yeah, if you could get Kent is not here either or audmar. But get, you know, their approvals. You know you're fine. Yeah.
**Peter Findeisen** 07:44 Yes, I will ping them.
Kent, unfortunately had has another meeting, so he wouldn't stay.
He showed up for a minute.
**Carlos Alberto Cortez** 07:53 Yeah.
**Yuanyuan Zhao** 07:54 Oh, I'm fairly familiar with the sampling topic in general. Is there anything I can help.
**Peter Findeisen** 08:03 Well, there is another pull request which.
**Yuanyuan Zhao** 08:07 Help review that one.
**Peter Findeisen** 08:08 Okay, okay, yeah, this is this is actually the prototype which which I modified to reflect the
clarification and small change that was required.
Yeah. So I I think I got already approval from Jason. Plump
we need more approvals. There.
**Carlos Alberto Cortez** 08:31 Yeah, I see to approval. By the way.
**Peter Findeisen** 08:34 Oh!
**Carlos Alberto Cortez** 08:34 No sorry. 1. 1. Sorry. Yeah.
**Yuanyuan Zhao** 08:36 That's the 2022, right?
**Peter Findeisen** 08:43 Yes.
**Yuanyuan Zhao** 08:43 Code change.
Yes, yes, that code would change.
I can help take a look at this one.
**Peter Findeisen** 08:48 Thank you.
**Yuanyuan Zhao** 08:49 Okay.
**Peter Findeisen** 08:55 So most of the changes adding a test
which, which which is a kind of corner case, right? But but so the test is a little bit elaborate because it needs to simulate
inter process behavior.
So we we have a parent span which is sampled with specific conditions. And then we have a child span which takes
input from the trace state and the sampled flag. So the test is a little bit long, but that it. It tests exactly the scenario that is discussed
in in the 1st pull request for the clarification. And there is also an issue
filed for that which is linked just just to follow the the regular process.
Usually we want to have an issue open for any change that follows.
So I try to be compliant with this.
**Yuanyuan Zhao** 10:12 I'll take it over after this meeting.
**Peter Findeisen** 10:14 Okay. Thanks.
**Yuanyuan Zhao** 10:15 I think those are the things we've discussed extensively on doing that.
**Peter Findeisen** 10:21 Yes.
**Yuanyuan Zhao** 10:30 If nothing else. I think we are done, or.
**Peter Findeisen** 10:34 No wait, number.
**Yuanyuan Zhao** 10:35 I don't think they're gonna show up.
**Peter Findeisen** 10:36 I don't think so. Yeah, I think you're right. I think we should call it good day.
**Yuanyuan Zhao** 10:44 Yeah, I use the time to look at yours.
Have a great weekend, everyone.
**Peter Findeisen** 10:50 Yeah, thank you. Guys, bye.
**Carlos Alberto Cortez** 10:53 Joke.
