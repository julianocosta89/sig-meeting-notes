SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-03-25
Duration: 19 minutes
Zoom Recording URL: https://zoom.us/rec/share/SBHUR0F5u6nz6qltky9xA6CFMZVQTSitEefU1oL6EPUaJAwcCBocr-W6TRicbN25.m-cZlPfbUowNyK1c
============================================================

## Zoom Recording Transcript

**Jim Porell** 00:24 Hello there!
**Greg Shriver** 00:28 Hey, Jim, how you doing?
**Jim Porell** 00:31 Not too bad, Greg.
**Greg Shriver** 00:34 Good, good, good.
**Jim Porell** 00:36 I was looking at, sorry about last week, I just joined 10 minutes late and everybody's gone already.
**Greg Shriver** 00:43 Yeah, that was a quick meeting.
**Jim Porell** 00:45 No worries, but, I don't know if any… if you looked at what I wrote on that PR, you know, trying to explain it, if that was good enough or not.
**Greg Shriver** 00:55 but I thought it was… I did, I thought it was perfect. I mean, I thought it was perfect and kind of, you know, followed the contours of the discussion that we had last week.
**Jim Porell** 01:04 Right.
**Greg Shriver** 01:05 I mean, I was… I… you know, I'm still kind of hoping that, you know, that Rudiga is able to make today's call. I thought he was… I thought he said that he would be able to make today's call.
**Jim Porell** 01:16 With that?
thing on the Slack channel saying otherwise?
**Greg Shriver** 01:21 I didn't even look at the Slack channel, see? That's how bad.
**Jim Porell** 01:23 Yeah, nobody had anything there, so we're…
**Greg Shriver** 01:25 Yeah.
**Jim Porell** 01:26 Yeah, I find that's kind of important.
**Greg Shriver** 01:29 Well, yeah.
**Jim Porell** 01:30 Is it a quick meeting or a no meeting?
**Greg Shriver** 01:33 Right, right, right.
So, I mean, I only have one agenda item, but, you know, we… probably want to tick through the open PRs, open issues, and I think… Who was it?
I saw it a couple days ago.
**Jim Porell** 02:00 I'm also very curious about the performance of the collector. That came up as a customer issue, but I asked, did anyone try that on x86? Because my hypothesis is it sucks there, too.
Just because we've got too big a volume.
There's just too much data.
**Greg Shriver** 02:16 Yeah.
**Jim Porell** 02:18 So I met with Kendrell the other day… yesterday, in fact.
**Greg Shriver** 02:22 Okay.
**Jim Porell** 02:23 they wanted to get into open telemetry, and I gave them the heads up by… Wait a minute, you know, figure out what you want to use it for first, before you go just diving into it.
**Greg Shriver** 02:46 Antoine opened up.
**Jim Porell** 02:48 in the AIX fund last week.
**Greg Shriver** 02:52 Yeah That's in the OpenTelemetry space.
So, I guess, do we… do we, Do we include AIX as, like, a mainframe platform? I guess we do, huh?
**Jim Porell** 03:13 I don't.
**Greg Shriver** 03:15 Okay.
**Jim Porell** 03:16 It's, it's, it's a… It's in the LUW space, Linux, Unix, Windows space, versus mainframe, I think.
**Greg Shriver** 03:23 Versus mainframe. Okay.
**Jim Porell** 03:25 Yeah.
Hell of a lot more synergy with them, you know, than it is with a mainframe.
Yeah.
**Greg Shriver** 03:33 I would agree.
But I, I, you know, I share your, I share your curiosity as to, you know.
what the issue is with the CPU usage on the OpenTelemetry Collector.
You know, is it… is it… is it literally just volume?
**Jim Porell** 03:53 Yeah.
**Greg Shriver** 03:56 It's also kind of interesting, This is just a sort of an, you know, an overtime kind of, kind of discussion, but… You know, we talk about how much data, you know, has to… you know, basically, how much data we have to send.
You know, from an OpenTelemetry perspective.
And the thing is, you want, you know, you want to send You want to send everything, because you don't know what you're going to need.
Right?
And… but sending everything, of course, has cardinality, you know, introduces cardinality and data volume problems and all that stuff.
And I'm wondering if… you know, I know that… I'm wondering… I'm wondering if AI, you know, could change that.
in… Yeah, I know, it sounds like, gee, everybody thinks AI can change everything, but what I mean by this is.
**Jim Porell** 04:57 That's an amazing… I mean, we're seeing some amazing things, so it's really cool.
**Greg Shriver** 05:03 I mean, in the case of… You know, would we have to send as much data If we have the ability to go back and grab the data that we need when we need it.
**Jim Porell** 05:18 If it's collected, correct, you know.
**Greg Shriver** 05:22 Yeah.
**Jim Porell** 05:23 That's one of the things we've been wrestling with, is there's a cost of collection.
Sure. And, and so… And then there's a cost of distribution.
So, kind of the point that you're making, KPIs are what you make decisions on, KPMs are the diagnostic things. And so, if you can… transmit the KPIs and then reach back for the KPMs, that all works. If you're not collecting the KPMs, then you're hosed. So…
**Greg Shriver** 05:57 For sure.
**Jim Porell** 05:58 You know, so… One of the questions that's come up to us is, do you want to dynamically turn on KPMs? And the question there was, is it too late? You know, it's now past the issue, so you might not have it.
The other thing I'm… You know, I… when it comes to OpenTelemetry, when I coach people on it, I talk to them about development environment, there's usually low transaction rates, and probably the most valuable time to use it, because you can put all the pieces end-to-end together and capture everything.
the problem is in production, and if you turn it on for everything… because my hypothesis is, you know, you've got IMS kicks transactions that are very, very tight.
You know, very small.
But now, when you add a TCP IP flow.
And I don't care what you're sending, but the introduction of a TCP IP call Or every transaction is, you know, astronomical.
You know, and so… again, I don't… I didn't look at how they implemented this, but even if it's, you know, they start by writing a record, you know, supposedly in memory to, The system trace, or syslog, whatever it is.
I still need to get that transmitted from there to… or make that accessible to, you know, the collector that's not on ZOS, so even if it's a hypersocket that gets it there.
TCP, like, one is its general purpose, and… It's got latency associated with it, so… Already, I gotta start thinking about filtering. You know, what are my key apps? You know, in a production environment, I'm gonna… I'm thinking I'm gonna wanna limit open telemetry to critical applications, because I can't afford to do them all.
**Greg Shriver** 08:16 It's an interesting perspective.
And, you know, we've heard similar sort of discussions with, like, head sampling, tail sampling.
Yeah. You know, to… to limit… to limit that, and… and they all have their… they all… they all have their.
**Jim Porell** 08:33 Well, what do you miss?
**Greg Shriver** 08:34 Plus and minus, right, yeah.
**Jim Porell** 08:36 Right, and when you're doing tracing.
And again, I'm going to make the distinction between the tracing and the metrics, because the metrics are more about the subsystem, or maybe a little bit about the application, but the tracing is what gives you the topology stuff end-to-end, and I definitely want to see that.
You know, for my applications, and then find the bottlenecks associated, regardless of where they are, because it might not be on the Z side, it's, you know, on the front end.
Yeah, just, you know, so filtering to me is really important.
I only want to do collection. I had this question. We were doing analytic work with a customer, and… We had tons of information about that customer.
But we had no clue.
what was important to them. So they told us. And once they told us, Mmm.
Put all our analytics on those critical applications, and boy, did we save a lot of MIPS. You know, you know, a lot of… a lot of crunch time, response time, everything, in terms of what were they really focused on. Other things, payroll, they didn't care about. They wanted… you know, in their case, it was, money.
**Greg Shriver** 09:57 care about payroll.
**Jim Porell** 09:58 No, I do too, but… They cared about money transfer.
**Greg Shriver** 10:02 Right, right, right.
**Jim Porell** 10:04 That was their key thing, and it was bank-to-bank, bank to government, bank to consumer.
You know, if that doesn't work.
Then somebody's getting hosed, you know, so…
**Greg Shriver** 10:16 Right, right, right.
**Jim Porell** 10:17 Most important things to them.
It's kind of like your WLM service classes, but, you know, I want to focus on the highest service class, you know, you start… you can… all different ways of filtering it, so…
**Greg Shriver** 10:31 That's… that is an interesting… I mean, is there a way that we could, you know, leverage the WLM service policy.
You know, to try and have some sort of qualities of service based on… not qualities of service, but basically to try and do some of that decision.
**Jim Porell** 10:47 Yeah. Well, you would think if… you would think those transactions are going to be in your highest service class, you know, if they're that important, so…
**Greg Shriver** 10:56 They're that important. Yeah.
**Jim Porell** 10:58 We start, you know, all different ways to think about it, but…
**Greg Shriver** 11:04 Hey, Kai.
**Kai Kirsch** 11:05 Hey, Greg. Hi, Jim.
**Jim Porell** 11:07 America.
**Kai Kirsch** 11:07 June, one question. Did you have the chance already to measure the impact of some hotel traces, like from IMS or Kix?
**Jim Porell** 11:16 No, no, not at all, and… but that's why I was asking the question. Somebody… somebody complained, and I think it was a customer, one of their POC customers, complained about the Linux on Z collector. It wasn't performing well enough, and we started this conversation with… my assumption was, doesn't matter where the collector was gonna run.
It was probably getting flooded.
And… can't keep up, and that's why I was interested to see, did they have the same experience on x86?
**Greg Shriver** 11:47 Yeah.
**Jim Porell** 11:47 Because I'm really afraid that the buy… you know, if you turn this on in a production system, you're just… one is your MIPS are going to dramatically go down because of the CPU time spent transmitting to the collector, and then… Can the collector actually keep up, or do you need a cluster of collectors in order to accommodate the volume of data?
I think those are operational issues, you know, from an IBM perspective. I'm hoping to get some answers on that at some point.
Ty, what do… I'm not sure what your interest in this. I certainly know Greg's, and he knows mine. Where are you coming from?
**Kai Kirsch** 12:36 Now, practically also, right, coming from the… from the same view as Greg, just looking at, right, IMS, if this is… if the hotel traces there are a viable option for customers, because, of course, right, we have this high transaction rate.
There as well, and then it would be curious to see if there's an impact, or… If there's really, then, the option, right, to do some filtering or some sampling?
**Jim Porell** 13:02 Okay.
Hello, Richard, we're just… Chatting about volumes and rates of hotel transactions.
**Richard Nikula** 13:18 Yep. It's definitely an interesting topic. I just was on a call yesterday with a customer, and they were all going on about volumes and things. It was, yep, a very pertinent topic.
-
**Greg Shriver** 13:35 Really cool.
**Jim Porell** 13:36 Jeff Rudiger's Slack, and he's offline, so I know he's.
**Greg Shriver** 13:40 Decision.
**Jim Porell** 13:40 Usually when he's driving his kids around to different things, so…
**Greg Shriver** 13:44 Yeah.
Yeah, and it's… it's quarter after, so we should probably… So let's tick… let's tick through the open PRs. The 1898, the TPS PR, Jim, you replied to Ludmilla, which… and I thought… I thought your… your reply was perfect.
I still do think there's more discussion that we need on the TPS namespace, and… and I was really hoping to, you know, get more color, from Rudiga on… on what… what feedback came… what other feedback came back from, you know, from the semantic conventions group.
The SEMCOM SIG.
And, so… but we'll have to… we'll have to wait until Rudiga is able to come back and… and give us an update on that.
**Jim Porell** 14:34 Rudiger just responded, he got a conflicting call, so he can't join.
**Greg Shriver** 14:39 Okay.
Thanks.
Thanks, Jim. The doc PR, it's still sitting on my… on… I have the next action on it, I just haven't had a chance to investigate the code spaces, and… and the… to… I need to do the code spaces to figure out how to do the automated checks for the dock PRs when you… when you, For the GitHub Actions.
So, I… I just… I need to… I need to dig into that a little more. The open issue, that was the one… that was the one we were just discussing, so we pretty much have all that.
So that's pretty much the… status of open PRs and issues. I'm not aware of any new PRs or issues. Is anybody else?
The one item that I had for the agenda was… Just kind of talking about, you know, What would we think about suggesting an open telemetry on Mainframe SIG panel at SHARE Pittsburgh?
So I just kind of want to throw that out there. The deadline for, call for proposals is 14th of April.
And I'm kind of wondering, like, who from the SIG thinks that they might be able to attend SHARE. We were to… the thought on this would be that we would have, you know, kind of like.
you know, discuss, you know, have… have some pre-planned topics if there's no… if there's no… if there are no questions, but the panelists would be basically, you know, the… I guess, the regular contributors to this… to this group, you know, to this SIG.
And that we would have a panel session, and maybe have some seated, topics to talk about, and to hopefully talk about with customers.
So… So I have two asks, I guess. One, you know, who… who, from the SIG thinks they might be able to attend SHARE Pittsburgh in, August?
And two, would anyone be willing to, you know, submit a share session proposal?
Crickets.
**Jim Porell** 17:06 So, I can give you the negative, I will not be a chair, so…
**Richard Nikula** 17:10 I could give you that answer, too. I don't anticipate being at share this year.
**Greg Shriver** 17:15 Okay.
Okay, so… Well, maybe we'll… maybe we'll bring it up again. We could see if we could, Well… We'll bring it up again and see if, so… so you guys can't go, Kai, I'm not sure about you.
You planning on being able to make it to Share Pittsburgh?
**Kai Kirsch** 17:42 It's not decided yet, we have to… we have to check internally, so…
**Greg Shriver** 17:46 Yeah, I know, we have to do the same thing, so yeah, for sure.
Okay.
So… I think we'll just, we'll… I'll… Probably pop it on the agenda, you know, on maybe a future call, and see if, if any of that changes.
So, I know.
Now, I will note here, not Jim.
**Jim Porell** 18:12 Not joking.
backwards.
**Greg Shriver** 18:15 Not Richard. Not Richard.
Nicola.
Because we have multiple Richards now.
We'll make sure we're clear.
Alright.
So, cool. Does anybody… does anybody else have anything they'd like to bring up?
Alright, hearing nothing, Maybe… is it a good time to wrap, then? And oh, I… I will not… I cannot attend the call next week. I will be out.
So, hopefully, you know, hopefully Rudy goes back, and… So I'll pop that on the Slack channel, too, so that everyone's aware that I can't make next week's meeting.
Alrighty Going once.
Going twice.
Alright, thank you all for your time, and I look forward to talking to you in, well.
In… in a couple weeks.
**Jim Porell** 19:34 Alright, see you guys.
**Kai Kirsch** 19:35 Thank you.
**Greg Shriver** 19:36 Cheers. Bye-bye.
