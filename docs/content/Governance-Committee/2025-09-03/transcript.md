SIG: Governance Committee
Date: 2025-09-03
Duration: 24 minutes
Zoom Recording URL: https://zoom.us/rec/share/x7UE0zJyRT3wnqysXAIqlv_GxjWsYFr7Vap1HsPc7iOzgtWkFykQfEp1BDq7FoPt.An9_MZmV48nxV7Lx
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:26 Hey, Severn!
**Severin Neumann** 00:33 Hey, Toss, good morning.
**Trask Stalnaker** 00:37 Good afternoon.
Good morning. Hi, Alida!
**Severin Neumann** 00:44 Good morning, good morning.
**Alolita Sharma** 00:46 Hi, Severin, how are you?
**Severin Neumann** 00:48 I'm fine.
**Alolita Sharma** 00:49 Good to see you.
Did he have a good vacation?
**Severin Neumann** 00:53 Yeah, definitely, we had, we had some good time.
But Burke has me back already, so that's like…
**Alolita Sharma** 01:00 I know, I know.
No, we just, Trask, hopefully you had a nice long weekend.
**Trask Stalnaker** 01:07 Yes, I did. Well…
I actually got my, shingles, my first shingles vaccine shot on Saturday morning, so I was actually, pretty out of it on Sunday. Yeah.
**Alolita Sharma** 01:26 Oh my gosh, it was… hopefully it wasn't too… too strong.
**Trask Stalnaker** 01:31 Necessary, but yes.
**Alolita Sharma** 01:36 Good to… good to be up-to-date on all your vaccines before this.
**Trask Stalnaker** 01:41 I promise that's only one, that's only the first. So, I mean, I don't know how many of you are over 50, but once you're 50, you're supposed to get the shingles vaccine.
**Alolita Sharma** 01:51 In the US, yeah, definitely.
**Trask Stalnaker** 01:52 Yeah, and it's a two-part, like, you have to do it, like, 3 months apart.
That's not… It's… yeah, it's a lot.
**Alolita Sharma** 02:06 Yeah, exactly.
Hey, Ted.
**Ted Young** 02:10 Yo!
**Dan Gomez Blanco** 02:11 Hello?
**Ted Young** 02:15 Yeah, well, I'm glad I have that to look forward to, Trask.
**Alolita Sharma** 02:19 Can't wait.
**Trask Stalnaker** 02:24 Did they think…
**Severin Neumann** 02:24 Because you're excited when you get older, right? Like, all these amazing medical appointments in front of you. Yeah!
Only getting better.
**Alolita Sharma** 02:36 Only.
**Ted Young** 02:40 What I mean…
**Alolita Sharma** 02:43 Jurassi, by the way, I have to compliment you on your, article on, you know, which you had written a while back on Medium.
Which a couple of my engineers were reading through on,
how to build custom processors for collectors, and I think that's the only documentation, literally, that exists on hotel custom processors.
**Juraci Paixão Kröhling** 03:10 For custom processors, that might be true, yeah. I converted a few of…
**Alolita Sharma** 03:15 It's really good. It's a very good article, so thanks.
**Juraci Paixão Kröhling** 03:19 Thank you. Thank you. That's kind of old, so I'm surprised that they found it useful. But thank you. We converted a few of them to OpenTelemetry's website. I think Pablo just linked a couple of them.
**Alolita Sharma** 03:31 Yes.
**Juraci Paixão Kröhling** 03:32 Yep.
**Alolita Sharma** 03:33 Or today?
**Juraci Paixão Kröhling** 03:34 I mean, I haven't checked the link. But we have a few… we converted a few, like, yeah, building a receiver, building a connector, and building the extension. They were also blog posts before.
**Alolita Sharma** 03:44 Yes.
**Juraci Paixão Kröhling** 03:45 And I don't know why the processor is not there, so it should be. I don't know.
**Alolita Sharma** 03:49 It was a… it was really the best documentation that I could… they could find on the web, so we should totally add it to the, project website also.
**Juraci Paixão Kröhling** 04:00 True.
Yep.
**Alolita Sharma** 04:05 Oh, cool, Pablo, thank you. That's… that's very helpful.
They didn't go and look, so… but.
**Pablo Baeyens** 04:13 Yeah, we've been trying to add some examples to the Go API, because, you know, people…
**Alolita Sharma** 04:17 Awesome, awesome.
**Pablo Baeyens** 04:19 Find them useful.
**Alolita Sharma** 04:20 I mean, it's amazing how useful custom processors are, actually.
Because when you're working in different… different platforms, you know, it's just, very helpful.
Because everything is not Kubernetes. Believe it or not.
Okay, I'll not forget… Link for Jurassi's article added.
Okay, very cool.
**Ted Young** 05:09 Okay… Any more topics, or should we dive in? Looks like we've got quorum.
**Alolita Sharma** 05:18 Yeah, let's dive in.
Okay, it should be shared… let's see.
**Severin Neumann** 05:24 I moved the topic from last week around the election. I think Morgan put it there last week, and we did not get to that.
Or, like, how we were saddened.
What do we need to do?
**Morgan McLean** 05:35 Good idea. Yeah, I added that last week, because I was away for… I was on vacation for 2 weeks, and so I didn't know if we'd moved on anything or not.
So, yeah, we can cover that.
**Trask Stalnaker** 05:45 We have not… But, yes.
We need to…
**Morgan McLean** 05:50 Alright, cool.
**Trask Stalnaker** 05:51 Probably.
**Alolita Sharma** 05:55 Yeah, it's time.
**Pablo Baeyens** 05:58 Boop.
**Alolita Sharma** 05:59 realistic.
**Pablo Baeyens** 06:00 Pony dot?
I think we spoke about that.
**Alolita Sharma** 06:03 No, I… I think… I think we need to determine that, right, Pablo?
Like, who are…
**Trask Stalnaker** 06:11 I did already, I think.
**Morgan McLean** 06:12 Okay, we did a few weeks ago. Go ahead, Trask.
**Trask Stalnaker** 06:16 Yeah, I think it was Morgan, myself, and maybe Dan?
**Dan Gomez Blanco** 06:22 I'll be… I'll be running for re-election, so I'm not sure I'm…
**Trask Stalnaker** 06:25 Oh, not Dan.
**Morgan McLean** 06:27 Man.
**Alolita Sharma** 06:27 I can, I can help this one.
**Dan Gomez Blanco** 06:29 But I, I run the… I run the You know, if you need.
**Alolita Sharma** 06:32 Yeah, damaged.
**Juraci Paixão Kröhling** 06:34 I guess that's what we talked last week. Oh, yeah. I think what we…
**Pablo Baeyens** 06:38 Right, I guess it should be me, since I'm not running on.
**Juraci Paixão Kröhling** 06:42 Yeah, I guess. Good.
I guess what we talked last time was, me or Dan can unofficially help in setting things up, because we've done it in the past, but we would not be part of the commission, like, not officially, just shadows, or…
**Dan Gomez Blanco** 06:56 Yeah.
**Alolita Sharma** 06:59 To Morgan, Trask, and Pablo.
**Trask Stalnaker** 07:03 Yeah… Awesome.
Yeah, just copied in from our… previous notes.
**Dan Gomez Blanco** 07:12 Let me share… I'll share some, like, the…
let me see, the project from… so I created a project board for the last one, and it should have all the… all the different issues in it.
Mmm.
Yeah, and then we can take it from there.
**Alolita Sharma** 07:27 Cool.
**Morgan McLean** 07:42 Did we want to create a… I'm trying to remember how we did in the past. Did we want to create a separate Slack channel for it? I think we ran things on the main Slack channel, right?
**Alolita Sharma** 07:50 Yeah, but I think, I think the… did we decide on the date?
**Morgan McLean** 07:58 Checking.
**Juraci Paixão Kröhling** 08:02 I think we agreed on, looking in… Yeah, look at KubeCon dates, and then, we announce one week before, and then walk back the timeline from that.
**Alolita Sharma** 08:14 Okay, okay, yeah, that's a good idea. I think UPCON is November… dense.
**Juraci Paixão Kröhling** 08:19 10 to 30.
**Alolita Sharma** 08:21 Yeah.
**Juraci Paixão Kröhling** 08:21 Yep.
**Morgan McLean** 08:22 So, one week before, that's the 7th. Okay.
**Juraci Paixão Kröhling** 08:25 Yeah, I think what we also talked was confirm that information based on the previous election, so see if this is really one week or two weeks, I don't recall, like, but we've done something similar last time.
I was confused about one week after or one week before KubeCon, and I think we found out that it was one week before.
**Morgan McLean** 08:45 It was definitely before.
**Alolita Sharma** 08:46 Yeah.
tour.
**Juraci Paixão Kröhling** 08:48 Yeah.
**Morgan McLean** 08:50 Yeah, I think…
**Juraci Paixão Kröhling** 08:50 We'll see.
**Morgan McLean** 08:51 The intent of, like, avoiding any… not that this would necessarily happen, but, like, campaigning and things at KubeCon.
**Juraci Paixão Kröhling** 08:56 Yeah.
Yeah, exactly.
**Alolita Sharma** 08:59 I mean, we've always used the KubeCons for announce… announcing.
**Morgan McLean** 09:04 Yep.
**Alolita Sharma** 09:04 the new GC, so…
**Morgan McLean** 09:07 Alright, I will take a look at the process from last year, because we'll want to start queuing up announcements and things. There's basically two tracks to this. There's the actual procedure of setting up all the voting stuff.
But then there's also just making sure the community knows, and making sure that people have enough time to submit their candidacy. So, I can take point on this. I have not run an election previously, so it'll be a good learning experience.
**Alolita Sharma** 09:35 Cool, cool.
I think Trask has. I'm impressed more than you have not.
**Morgan McLean** 09:43 I was gonna say, let's say, like, Trask, I think you've run one before, so it's probably my turn.
**Trask Stalnaker** 09:47 So… You haven't?
**Alolita Sharma** 09:48 dress?
**Trask Stalnaker** 09:49 Oh, you haven't? No. Okay. No. Oh, okay.
Share in the Slack channel, or privately with me and Pablo what you're doing, so we can jump in and help out.
**Morgan McLean** 10:00 Perfect.
**Alolita Sharma** 10:01 Cool.
**Dan Gomez Blanco** 10:01 Yep.
**Alolita Sharma** 10:06 Well, Morgan, even I have, with Dan and Liz.
**Morgan McLean** 10:10 Yeah, this is funny, it might be the three of us who haven't.
**Alolita Sharma** 10:14 That's amazing.
**Morgan McLean** 10:15 This can only end well.
**Alolita Sharma** 10:17 Yes, exactly.
**Morgan McLean** 10:18 It'll be fun.
Got lots of guidance from years past.
Yes.
**Alolita Sharma** 10:24 Yes, yes, at least now we are pretty organized.
**Dan Gomez Blanco** 10:27 To be honest, like, yeah, when I did it last year, it was just almost like copying everything that Jurassic had done before.
**Alolita Sharma** 10:33 Yeah, dressing.
Thorough. Yeah, so good.
His Germanness kicks in here, so this is very good.
**Morgan McLean** 10:46 Organized.
**Juraci Paixão Kröhling** 10:47 I have to wear my passport.
**Morgan McLean** 10:53 Alright, that probably covers the election for now. I'll send out some messages on Slack about when I propose… when we should do things.
**Alolita Sharma** 11:03 Okay, cool. Should we look at the project board?
**Juraci Paixão Kröhling** 11:11 Should we go to the private?
Part…
**Alolita Sharma** 11:16 Is it hot?
**Pablo Baeyens** 11:17 We can do, like, the project board for them.
**Juraci Paixão Kröhling** 11:20 Okay. 5-10 minutes. It should be quick.
**Pablo Baeyens** 11:31 Sorry, there's… I can share my screen, but I need to move my tabs around, so if anybody else is ready…
**Alolita Sharma** 11:43 You need the link.
**Pablo Baeyens** 11:59 Good.
So… Yeah, I don't know, like…
Mmm…
I mean, looking at this, the only one, maybe, is there anything about degradivation that we should talk about?
I saw the… the TOC review, PR was approved, but I don't know if there's anything.
**Austin Parker** 12:28 Yeah, so…
Where are they at? I think they've been doing adopter interviews still. I think they're up to 3 or 4 that are done?
**Alolita Sharma** 12:42 Yeah, they're doing adopter interviews still. That's my understanding from the TOC.
And the tab is helping also there, so…
**Austin Parker** 12:52 Yeah, so…
**Alolita Sharma** 12:53 References?
I assume… I think… so we're just in a holding period, as far as I can tell. I think the…
**Pablo Baeyens** 13:00 I believe the next steps are… they finish the adoption reviews.
**Austin Parker** 13:05 And they finish their report.
And then there's a public comment period.
And then a vote.
**Pablo Baeyens** 13:14 Okay, is the report just…
This… is this one of the reports?
**Austin Parker** 13:21 I think the governance review is one of them. That's a part of the report.
I think they basically do a recommend… there's basically a recommendation.
If you look at TOC… Let me pull up the repo, I'll try to find an example.
**Pablo Baeyens** 13:51 Would that be, maybe, projects?
**Austin Parker** 13:53 I thought it was an issue…
**Pablo Baeyens** 13:59 Any project that's going to be… In native, maybe?
Okay, native?
**Austin Parker** 14:04 There's like a… Public Institute for the PR News, draft TOC evaluation.
Okay, so if you look…
Ain't… Excuse me.
I think it's a PR? Yeah, so it's a PR. If you look at, like, if you go to pull requests…
**Pablo Baeyens** 14:34 And then, like, there should be a Knative one? Yeah.
**Austin Parker** 14:38 And then you look at the files changed.
**Pablo Baeyens** 14:47 Okay, and this is the doctor interview sent.
**Austin Parker** 14:50 Yeah…
So this is all what gets published.
I think once this is done, then it goes into public comment, and then… Voting?
I really hope we're not gonna miss the…
Okay, so… Generically irritated if we miss the…
**Alolita Sharma** 15:28 Yeah, that's absolutely…
**Austin Parker** 15:31 Atlanta.
**Pablo Baeyens** 15:32 Is there anything we can do? I think we just have to wait, so…
**Alolita Sharma** 15:35 Yeah, we have to… I think they're also trying.
**Austin Parker** 15:37 to finish it, but… I think they're trying to finish it for Atlanta, but…
**Alolita Sharma** 15:40 That's…
**Austin Parker** 15:42 I mean, I think it's what… what's… is it, like, 4 weeks?
the… I forget what.
**Alolita Sharma** 15:46 That's Hmm…
**Austin Parker** 15:49 There's a buffer on either side.
**Alolita Sharma** 15:51 I think there's, at least 3-week moratorium, I think.
**Austin Parker** 15:56 Yeah…
**Alolita Sharma** 15:57 before.
**Austin Parker** 15:59 Yeah.
So, 3 weeks? That's pro- we'll probably… we'll probably make it.
**Pablo Baeyens** 16:07 Well, let's cross our fingers.
**Alolita Sharma** 16:09 Yeah, I'll chat with Emily and see what's happening.
**Pablo Baeyens** 16:13 Okay, I guess then… I mean… This one was something that…
**Dan Gomez Blanco** 16:21 Yeah, don't know if we want to just close that as done, but I… yeah, there was a question there for Emily, I guess, from Austin.
Yeah, so I guess we're still… still waiting on this?
We have…
**Austin Parker** 16:39 I haven't heard anything…
**Dan Gomez Blanco** 16:41 Yeah.
**Austin Parker** 16:42 Back from her, so…
**Dan Gomez Blanco** 16:46 I guess, you know, rather than closing it without a review, probably.
Worth waiting.
**Pablo Baeyens** 16:52 Can I close it then?
**Austin Parker** 16:59 I mean, I don't think we should close it… until…
**Dan Gomez Blanco** 17:03 Yeah, I think I would probably…
**Pablo Baeyens** 17:05 That's… that's incredible. Yeah.
**Dan Gomez Blanco** 17:08 One thing that I would say related to that is, if you look at the… just post to the link there for the Old Tail Roadmap.
M… Sorry, not in there.
**Pablo Baeyens** 17:19 Yeah, on the chat, yeah.
**Dan Gomez Blanco** 17:21 In the chat, yeah. So, this is now… yeah, this is looking good. The only thing that we're missing is those four…
Projects, they're at the… at the bottom that don't have dates on the… You know,
As in, like, timelines.
If we could. I think I've not reached out to… to these SIGs. I reached out to all the others, apart from those.
**Pablo Baeyens** 17:51 I can handle the system semantical mentions one.
**Dan Gomez Blanco** 17:55 But yeah, everything's working now as I'm… it's… Automatically synced from the…
from the individual project boards. So as long as they update the dates, the… so, like, target dates in the project board, it should just come up in here.
**Pablo Baeyens** 18:12 Okay.
Okay, anything else from any other issue in…
To do or in progress that we should look at.
**Severin Neumann** 18:27 Maybe assign the Create Slack channel to me and you, Pablo? I think since this is… Related to…
contributor experience.
At least you and I should have an eye on it.
**Pablo Baeyens** 18:42 Okay, I'll keep it in to do on one number.
**Severin Neumann** 18:45 Yeah, I would give it in to-do, but…
**Pablo Baeyens** 18:47 Meeting date, we can discuss it.
**Severin Neumann** 18:49 Yeah.
**Dan Gomez Blanco** 18:50 Just also a quick update on the Hotel.net contrib.
license… I've not posted it there, but I reached out to Daniel.
crook, and yeah, apparently this is waiting approval from the legal committee, but,
Yeah, so, it should be… Approved soon.
There's, exception.
There's a license exception.
**Pablo Baeyens** 19:17 Okay.
Yep, I think… We can move into the private topic, then.
I'll mention something I just thought about, which is, we can now…
I don't know if that's important for the project board, probably not, but we can now mark things as blocked by,
Or blocking other issues.
So long as they are within the OpenTradio, so that's…
**Ted Young** 19:45 Nice.
**Pablo Baeyens** 19:46 pool, at least.
May 4th.
Collector predictor.
Alright, so… I don't know, Austin, could you create a link for the private?
Zoom chat.
**Alolita Sharma** 20:00 Yeah, sure, Pablo. Do you want to share?
**Austin Parker** 20:03 Yep, one second, or I'll…
**Alolita Sharma** 20:06 Oh, Justin.
**Austin Parker** 20:07 Yeah, I got it once. Oh.
**Alolita Sharma** 20:11 Austin, are you in the Bay Area next week?
**Pablo Baeyens** 20:15 Austin?
He just left for…
**Alolita Sharma** 20:18 Oh, yeah. I'll ask him there.
**Dan Gomez Blanco** 20:22 Neverland.
**Alolita Sharma** 20:22 Pablo, I didn't even notice. See you there.
**Severin Neumann** 20:26 Yeah, dear.
