SIG: Governance Committee
Date: 2025-12-03
Duration: 24 minutes
Zoom Recording URL: https://zoom.us/rec/share/lz79LJG3RgeM1hXwkpJ8k9DnQxKiksXiRvqxUUkkack19plfigFxh5RCP4vDPnhf.VSyZlEdwS_37XQ19
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:53 Hey, Ted.
**Ted Young** 00:59 What's up, man?
**Trask Stalnaker** 01:01 I have a…
**Ted Young** 01:03 Jersey for you.
**Trask Stalnaker** 01:05 Next time we get… next time we, get lunch.
**Ted Young** 01:08 Yeah.
Well, we're, you know, right heading into… Lunch season.
**Trask Stalnaker** 01:15 Yeah, exactly.
**Ted Young** 01:18 How was KubeCon?
**Trask Stalnaker** 01:22 It was good. Always nice to be stateside.
**Ted Young** 01:29 No… no sleep.
**Trask Stalnaker** 01:32 Problems.
**Ted Young** 01:34 Yeah.
**Trask Stalnaker** 01:34 yeah, I think everything… Went pretty smooth, I thought.
**Ted Young** 01:44 Yeah.
I always have FOMO when I miss them, but I was very glad not to be traveling.
**Trask Stalnaker** 01:50 Yeah…
**Ted Young** 01:52 What's up, Pablo?
**Pablo Baeyens** 01:56 Hey, hey.
**Trask Stalnaker** 01:58 Hey, I'm getting a weird rattling in my headset, so I'm gonna drop and rejoin.
**Ted Young** 02:03 You're.
**Trask Stalnaker** 02:03 Fuck.
**Pablo Baeyens** 02:08 I'll remove my t-shirt from the background for the benefit of the people watching the recording.
**Ted Young** 02:13 Yeah.
**Trask Stalnaker** 02:29 Let's see if this is better…
**Ted Young** 02:31 Yeah.
**Trask Stalnaker** 02:32 Yay… The old reboot trick.
Oops, that's…
**Ted Young** 02:41 Just flush that state.
Who needed it?
It seemed like, from the chatter in Slack, like, people are gonna be late, or not here.
At least a chunk of people.
**Pablo Baeyens** 02:57 Yo…
**Ted Young** 02:58 I wonder who else Gonna show up.
Seemed like Morgan said he'd be late, Austin can't come.
And… Severin said he'd miss the first half.
**Pablo Baeyens** 03:13 And Marilla and Jerusi are out.
**Trask Stalnaker** 03:16 Oh.
**Pablo Baeyens** 03:18 So…
**Trask Stalnaker** 03:20 Do we have any…
**Pablo Baeyens** 03:20 baby.
**Trask Stalnaker** 03:21 Anything we need to do?
**Ted Young** 03:26 Yeah. Mmm… Well, we don't have quorum, that's…
**Trask Stalnaker** 03:32 Yeah.
**Pablo Baeyens** 03:33 But…
**Ted Young** 03:34 But yeah, is there anything we can do with that forum? Pablo, you want us to…
**Pablo Baeyens** 03:40 I had the, yeah, the project submission, but, you already reviewed it, so, nothing to do there.
And then the other is, we said at some point, we may want to check in with the collector's sake about…
Graduation and that kind of thing, I don't know if… We want to schedule.
**Ted Young** 04:03 Well… How are things feeling with the V1 and the latest push?
**Pablo Baeyens** 04:12 Right, so we have… Let me… Okay, let me…
hide all my tabs, and I'll share my screen.
I should just… Close all my tops and start over.
Sorry, my… Browser is freezy.
This is terrible.
Alright, I can turn my screen now.
So, I try to reflect what we… I've talked about on… this issue… So there's…
This, which will depend on the OTEP, on, ensuring that unstable components are opt-in only.
There's a bunch of work being done on automating benchmarking or documentation, that kind of stuff.
There's a few issues here.
**Ted Young** 05:30 Nice.
**Pablo Baeyens** 05:30 Ensuring… Sorry.
It's not…
**Trask Stalnaker** 05:36 You're using sub-issues.
**Pablo Baeyens** 05:39 Yes?
Ensuring end-user focus?
**Ted Young** 05:45 component implementation is available on our tool.io. That's mostly going to be.
**Pablo Baeyens** 05:49 part of the Ecosystem Explorer project, but I opened this to track any…
Anything that they may need from us, which, we already have one, sub-issue.
And lastly, we spend a lot of time working on a list of
Components that we will focus on, to mark a stable first.
apart from… we have the OCLP receiver and exporter, those that we're already working on, but we have this list based on…
The collector surveys, and then…
Yeah, just what different, approvers and maintainers thought would be most important. And so…
We have a bunch of people working on these components.
So that's… Mostly what we…
agreed on after the meeting we have with the governance committee.
**Ted Young** 06:52 Yeah.
I think that's great, by the way. I think that's…
A great way to move forward with the collector.
And I know from talking to Arthur, like, the Prometheus stuff, we actually feel is, like.
Pretty important to get into…
**Pablo Baeyens** 07:10 Yeah, yeah, so the Prometheus receiver is very widely used.
Yeah, I think Arthur and David are… Working hard on… On that component.
**Ted Young** 07:22 Yeah. The kind of review I got from them was that…
you know, the Prometheus ecosystem basically has a ton of sources of infrastructure data. If, you know, we're trying to not just look at host monitoring and Kubernetes, but also, like, MySQL and Postgres and, like, databases and, like, all these things, right? Like…
There's already a lot of that in the Prometheus world.
And… but actually, the kind of, like, support for that stuff in the collector was kind of, like, sort of ad hoc, maybe some stuff some users had been doing.
And if, like, they come in and do, like, a kind of coherent, cohesive
Approach to it, then, you know, we can just…
Glue into all of those things?
**Pablo Baeyens** 08:10 Yep, yep. Like…
**Ted Young** 08:13 Yeah. Anyways, I think… my point was… I'm rambling, but my point was not just to be like, hey, this is, like, a cool plugin, but maybe to maybe… and this is getting back to the GC biz of, like, making it a little more official, that, like, our approach, potentially, for dealing with
all of the, like, kind of non-APM data, like, all the infrastructure out there that Prometheus has that we don't yet, like, maybe even make it official that we're just gonna work with them to maintain that set of stuff, rather than start to…
**Pablo Baeyens** 08:46 bridge between them.
**Ted Young** 08:47 Right? Right, instead of being like, eventually we're gonna duplicate all of this stuff, like…
That's… that's, like, a whole other, like, hidden kingdom of, like.
Stuff that has to get maintained, so… you know.
That is, like, as a broader approach, I'm looking for ways to make Hotel and Prometheus play better.
And…
you know, if we could just be like, we're just gonna share these, and maybe help clean them up, or come up with, like, some translations from what they produced at Hotel, or…
you know, O'Til Smith or something.
Anyways, random thought, but…
**Pablo Baeyens** 09:25 I think, I think that would be cool. I mean, there are some core info monitoring things that, I think we have quite good, in-house solutions, and I mean, a couple of these are, like, the host metrics receiver and the Kubernetes attribute processor.
**Ted Young** 09:41 Right, there's, like, the core bit of, like, monitoring the virtual machine and the container schedule, like, the, you know, Kubernetes…
**Pablo Baeyens** 09:50 There's definitely, like, a long tail of things that Prometheus would be.
**Ted Young** 09:53 It's like, do we want to keep going down that path, and have, like, now there's, like, two flavors of host metric-y stuff floating around, or for the rest of it, do we want to start
with the path of being like, well, if Prometheus already does it, and we can already just integrate it, should we just take what's there and say, like, our data is, like.
this, or some, like, translated variant of what this thing does, and we're just gonna help maintain this thing.
You know, or work with them to… to make it emit two kinds of things, or something.
Because it's just, like, it's like a lot of… there's a lot of work being hidden under that Prometheus receiver, it seems to me.
Because we're talking also… because it's a generic nozzle to talk to all of these different Prometheus components that are out there.
We'd have to start maintaining all of that stuff.
But maybe there's a way to take that stuff and start baking it more directly into the collector, and maybe that's some of the Prometheus receiver work.
Anyways, again, I'm rambling, but that's… that is one place where talking to the collector people would be interesting to me.
Just…
The… the strategy is around all of that stuff.
**Pablo Baeyens** 11:07 Okay.
Yeah, I guess the last thing I'll mention here is,
the system semantic convention sig, and the…
Kubernetes and containers, semantic conventions, I mean, they are aligned with this work, and they are prioritizing the.
**Ted Young** 11:25 Great.
**Pablo Baeyens** 11:26 Semantic conventions that we need for these components.
**Ted Young** 11:28 Great.
Yeah.
I don't know, I don't personally feel like the GC needs to meet with the collector people right now, like, that…
So, like, I could report back. But if they're feeling like they want more direction or support or something…
**Pablo Baeyens** 11:49 Oh, no, I don't think that's the case. It's more, like, we said that I put a reminder, and I wanted just to check, but it's fine if we don't want to meet. Right.
**Ted Young** 11:58 Don't… Yeah.
**Pablo Baeyens** 11:59 it maybe makes sense once we have the OTEPs, if the OTEPs are difficult to land, it makes sense to land.
**Ted Young** 12:06 Yeah.
**Pablo Baeyens** 12:07 do a tour around at 6, but… Right now, maybe not.
**Ted Young** 12:11 Yeah, I don't know, we could check in with Austin about…
Does the TOC wanna… do we need to… do we want to poke them at some point and be like, FYI, this is the collector's…
This is what the collector's chewing through.
you know.
I don't know if we want to bring that to their attention or not.
That's maybe an Oscar question.
It'd be annoying to go and have them be like, that's not what we wanted.
**Trask Stalnaker** 12:44 I got the impression that they were…
Okay with just a very high-level, like…
From the governance committee, sort of, direction.
**Ted Young** 12:55 Yeah.
**Pablo Baeyens** 12:55 Hmm.
**Ted Young** 12:56 If they're satisfied with what they got, you know, from our post about it, then… Yeah.
I would say the collector's quickly becoming the least of our worries, because you guys are doing a good job there.
**Pablo Baeyens** 13:11 Aye.
**Ted Young** 13:13 I guess thank you for the part out.
**Pablo Baeyens** 13:15 I'm responsible for.
**Ted Young** 13:18 Yeah.
**Pablo Baeyens** 13:20 Should we call it a day? I mean, even if…
**Trask Stalnaker** 13:27 Yeah.
**Pablo Baeyens** 13:28 Severin joins we are opening up Quorum, so…
Well, if Severin and Morgan join, we will…
**Ted Young** 13:35 Yeah. I don't know that we are.
**Pablo Baeyens** 13:36 topics.
**Trask Stalnaker** 13:39 I actually think that technically quorum is 6, but…
**Pablo Baeyens** 13:43 Oh, right, yeah, it's two-thirds, yeah, okay, so then, yeah, no way.
**Ted Young** 13:48 Pablo, you had brought up, you know, like, code of conduct stuff, and like, you know, should we start a separate working group, maybe, for some of this stuff, and…
I did want to address a little bit of… have a little bit of a follow-up somewhere, I don't know if you have GC members, but structurally, I just want to mention, there's, like, two big things when we designed OpenTelemetry based on…
like, the… there's a lot of the structure of OTEL that's kind of based on the failure modes and, like, problems that we saw in, like, prior open source
You know, that we worked on that we wanted to make sure we didn't encounter again. So there's, like.
And, like, everything in OTEL, though, we don't write down, like, our reasoning behind our design decisions, so I realize that's not written down. But one of the things around the GC being elected, like, the two things that we probably don't…
like, or we really don't want to hand off to unelected things. The problem with unelected, appointed groups are mostly show up around code of conduct stuff and around…
project roadmap? Like, what's the roadmap for the project kind of stuff?
Like, keeping those things elected avoids this failure mode where…
we get a lot of, like, political pressure potentially put on us, right? Like, if we're a group of, like, 6 to 9 people who appoint people to who gets to drive the project, and who gets to handle this or that.
Then what happens is, like.
the heavies at the vendors in other places will come to us. And this even happened in, like, the early days of hotel.
get into the details, but will come to us and be like, you're gonna put me and two of my cronies from these two other companies on your board over here, and then we're gonna… we're gonna drive the project in that direction. And if you don't do it.
we're gonna threaten you, we're gonna put personal pressure on you people, because this is personal now, right? I want it, and you individuals told me no, and you're probably doing that because you work for these other companies and stuff, so I'm gonna put all this political pressure on you to…
To put me… install me on this thing.
And if your answer to all of that is, like, sorry, there's no board, there's no thing.
there's just the elected GC. If you want to, like, set the direction for the project, you have to, like, convince this community to elect you.
That actually gets… that, like…
We no longer… there's no longer any pressure point people can come apply to us to force us to…
appoint people to do things like that. So that's one thing.
The other thing is, like, those people tend to be more, like, figurehead-y people anyways, when…
Because they're too high level. Like, we had this on the open tracing side, we had more of, like.
Like, the board that was supposed to drive the project ended up feeling more almost like a vendor advisory board.
And it was, like, people who were, like, maybe interested, but not very engaged.
And the code of conduct's kind of, like, in the same thing, of, like, you'll start to get people who we really don't want to be on there, like, putting pressure campaigns on us, and then they'll go, like, public, because it's, like, the kind of weird person who wants to be on…
the Witch Hut Committee.
**Pablo Baeyens** 17:17 I guess.
**Ted Young** 17:18 No, that's just…
**Pablo Baeyens** 17:20 3 years.
**Ted Young** 17:20 It was like.
**Pablo Baeyens** 17:22 Yeah, yeah, this is very useful context, and, like, I appreciate you taking the time to tell me. The thing that,
makes me…
hesitate a bit about that argument, or part of that argument is we are the witch hunt committee right now, and .
**Ted Young** 17:42 You end up with one, no matter what, it really sucks.
Right? Like, you can't escape it.
**Pablo Baeyens** 17:47 I mean, it…
It may not be perfect, but, like, it's not terrible. I don't think we're doing a terrible job when it comes to code of conduct.
**Ted Young** 17:57 I actually think we're doing fine. I mean, you know, if we're doing anything wrong, right, like, the lesson I keep learning is, like, we should be more aggressive about, like, warning people.
So that when something does happen, we feel like we can…
Move on it in that moment, and not feel like, well, we never even warned them.
that this.
**Pablo Baeyens** 18:20 Hmm.
**Ted Young** 18:21 Are we being bad? Like, we sometimes have that. That would be our one thing where I'm like, I think we should be more aggressive about
warning people, and I've started to get that way when people are being not to…
**Pablo Baeyens** 18:32 No, yeah.
**Ted Young** 18:33 I'm just starting to be a little disruptive, or like, it's not working. I've been a little more aggressive, being like, hey, this isn't working! Like, you need to, like, we need to change how these dynamics work, because it's not working.
**Pablo Baeyens** 18:44 I guess, like, when I thought about it, I saw two parts. One was the committee part, and I think… I still think there's…
possibly some way and shape where we could all be happy with it, but, like, I haven't talked with, all of the Kubernetes people yet. But, the other part was informative guidelines. We don't have a guideline on what to do, on maybe having some sort of
Probably vague, probably not very prescriptive, but guidelines on, like, the different levels of, intervention that we could have, the different, kinds of
offenses that could happen, or things that are in scope. That could be useful. That could be useful, not only for us, but, like, for the community to understand how we apply color content.
**Ted Young** 19:30 I think you're getting into more interesting territory there. If you're like, are there failure modes in, like.
our system, where we basically have, like, one giant band hammer for, like, really bad behavior. But actually, more what we deal with is someone feeling like someone's being just, like, a bit of a pest for some reason, or, like, microaggressions, where we're like, you didn't do one big thing, it's just, like.
you're…
Sand in the gears, son! Like, you know, every time… we're trying to move forward, but you're opening, like, 40 PRs a day, and driving people crazy, or, like, you're…
that your tone when you talk to people is, like, making them wonder about X or Y, right? We do end up sometimes with stuff in, like, that category, where we feel like it's not really code of conduct. They didn't, like…
Aggressively, over the top, do something that's obviously.
**Pablo Baeyens** 20:24 Hmm.
**Ted Young** 20:26 super inappropriate. It's more just, like.
A death of a thousand paper cuts.
I don't know what we do there more differently from what we currently do, but I do feel like we sometimes are in that situation where we're like, the code of conduct doesn't quite handle this.
But then we just handle it by…
Just warning the person, usually, being like, hey, cut it out.
I just think we can't hand it off to another group. If we want to go to the community and be like, are there, like, better processes for handling… are there, like, failure modes or something? Like, do you see other communities doing things better?
But I would be very, very wary about even raising the idea of, like, hey, we want to form, like, a standing jury to judge people. Like, that…
you know, it either needs to be us, or if we get into, like, a big enough community, then it's, like, a randomized jury, you know, of your peers.
**Pablo Baeyens** 21:28 produce.
**Ted Young** 21:29 But a standing jury of people just signing up to be the jury…
We've just seen that as, like, such a really bad failure mode, and…
In other situations, like, you have to be careful about who ends up on those committees, and it's…
It's usually not the people… that's why, like, the random jury kind of works, almost.
It's because it's like, you're actually looking for people who don't want to be there.
**Pablo Baeyens** 21:55 Yep.
**Ted Young** 21:59 Anyways, anyways, that's the background. But the other thing is project management, which is, like.
That seems a little more harmless. Like, what's the harm of, like, a project management SIG? But we've actually had way more trouble.
on that front. More in the early days, but, like…
where people want to really put pressure on OpenTelemetry to go in some random direction, and they see that as, like, a…
A way to do it.
**Pablo Baeyens** 22:24 Hmm.
**Ted Young** 22:25 And because they have to get elected, it never happens! Like, their crazy… their, you know, their crazy stuff doesn't… doesn't, like, push us. And again, I don't… I have some, like, actual stories I could tell, like, an unrecorded call, like, really bad behavior from both this project and prior projects, you know?
Then when those people from those organizations were told, it's like, that's not even a thing, you can't have that thing, because it's not even a thing. Then they tend to be like, and then they come back with a shovel and just start helping.
So it's actually been, like, the degree to which we've had to deal with weird stuff like that. When we tell them, it's like, the only way it works is to, like, like, do work in the community, and then, like, you'll become maintainers and stuff, and then maybe get elected and stuff, but, like, the only way in is, like, with a shovel.
Their response is usually to, like, go back and get a shovel, and then come back and start helping.
So… versus being, like, oh, we just got appointed to this project SIG.
Which is what we wanted. And now we just tell you what to do.
**Pablo Baeyens** 23:30 Fair. Oh, yeah, that's fair. Yeah, I'd be… I'd be interested in hearing the stories, maybe back to you, Con.
**Ted Young** 23:36 Maybe at the next QCon.
Yeah, anyways, I don't want to take any more of your time, but I wanted to add a little bit of color to… to where that was.
**Pablo Baeyens** 23:43 Yeah, no, thank you, thank you.
**Ted Young** 23:46 Yep.
Hmm. Okay.
That's all I got.
**Trask Stalnaker** 23:53 Alright. Well, good to see you.
**Pablo Baeyens** 23:56 Yep.
**Trask Stalnaker** 23:57 Till next time.
