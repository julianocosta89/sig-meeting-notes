SIG: OpenTelemetry on Mainframes Weekly Sync
Date: 2026-08-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jim Porell (Rocket Software, Inc.)** 02:25 Whoa, who's… who's this stranger?
**Matt Hogstrom** 02:28 Yeah, how are you doing, bud?
**Jim Porell (Rocket Software, Inc.)** 02:30 Good, Matt. What's going on?
**Matt Hogstrom** 02:32 Too much. How's life at Rocket these days?
**Jim Porell (Rocket Software, Inc.)** 02:35 I can't complain. You replacing, Greg, or just… Subbing in, or additional?
**Matt Hogstrom** 02:42 I think, yeah, we… You know, like, you guys probably do the same thing. We were kind of rearranging the deck chairs on the Titanic.
**Jim Porell (Rocket Software, Inc.)** 02:51 Yeah.
**Matt Hogstrom** 02:52 the best quote, but, no, it was really more of, he's moving into a different area, still related, so I think he'll… he'll be continuing to participate.
But since it's more of a standards thing, it was probably more appropriate for me to do it.
**Jim Porell (Rocket Software, Inc.)** 03:10 I don't know if we're really gonna meet, I'm just looking at the agenda, Rudiger Schultz at IBM is on vacation for the month of August, so…
**Matt Hogstrom** 03:19 Okay.
**Jim Porell (Rocket Software, Inc.)** 03:19 he's the fearless leader. If he's not here, nothing really happens. So, my guess is I just updated the Google Drive to put this meeting notice out there, but… I don't see anybody else joining. Usually, it's pretty timely.
**Matt Hogstrom** 03:34 Alright, well, let's see, Couple things, last time I met with him was 2 weeks ago. I think you didn't make it, it was just Greg.
**Jim Porell (Rocket Software, Inc.)** 03:42 No.
**Matt Hogstrom** 03:43 Rudiger. He has a pull request out, I think it's number 20.
**Jim Porell (Rocket Software, Inc.)** 03:48 Yeah, I saw that on the agenda, yeah.
**Matt Hogstrom** 03:50 And I, I started going through it, and, he's looking for feedback.
what he wants to be able to do is to basically… I think he wanted to submit it right away, but he said, well, I think we need to do a little bit of time to go through it.
And… he wants to get feedback, have debate, and try to wrap it up by the end of September, so that it can be submitted.
Which I think is fair. One of the things that I made the observation on, I… I don't know if we're… you guys have been doing this longer than I have, so maybe this is how we're looking at it, but it felt like we're kind of looking at all the possible data that we could just, you know, push out there, and… In a lot of the data, I'm asking myself, well, is this really interesting to, say, an SRE, right? What… who's the consumer persona?
For the data that we're… we're gonna be sending out, and how much of the data is truly… relevant to them. So I don't know if we've taken that into consideration.
Yeah.
**Jim Porell (Rocket Software, Inc.)** 04:56 Not… not yet. Honestly, not yet.
**Matt Hogstrom** 04:59 And then the other thing I was thinking of in terms of the consumer, the namespace, I think we call it Mainframe. I would even prefer we called it S390X.
Because then it's consistent with x8664, ARM64, and it would be more familiar to people, right? And then that way, we could then say S390X HMC, S390X ZOS, X390X, and so we now have kind of a high-level qualifier.
**Jim Porell (Rocket Software, Inc.)** 05:27 Yeah, that makes sense, yeah.
**Matt Hogstrom** 05:29 Would be, you know, it would just be more, familiar.
And we can then focus on the various areas, so we're not kind of overloading the terms.
**Jim Porell (Rocket Software, Inc.)** 05:39 Yeah, to your, to your point.
what's been going on so far? And it's been slow going. There's a gentleman from Splunk,
**Matt Hogstrom** 05:49 Morgan.
**Jim Porell (Rocket Software, Inc.)** 05:49 No, not Morgan. Morgan's kind of like the high-level leader. What happens is, Wells Fargo, I think, has… has bought this, and it's Antoine Tolme.
**Matt Hogstrom** 06:00 Oh, Antoine. Okay.
**Jim Porell (Rocket Software, Inc.)** 06:01 Yeah, he's excellent, and he really gets the process, and he's more involved on the non-Z side, so… we all agree that this has been… we've been doing this for 2 years now. It's slow, slogging and stuff, and the community is kind of weird, but IBM is also weird, because IBM has adopted, in quotes.
OpenTelemetry and all this, but they don't even have the naming standards defined, so… you know, it's kinda… it's kinda weird.
**Matt Hogstrom** 06:29 I think, to a certain extent, everybody's kind of in the, the race. It's almost like the AI race, let me get open.
**Jim Porell (Rocket Software, Inc.)** 06:35 Yeah.
**Matt Hogstrom** 06:35 data out there.
**Jim Porell (Rocket Software, Inc.)** 06:37 Yeah.
**Matt Hogstrom** 06:37 even though we haven't defined the standard, we're not exactly sure what that means. But, you know, I think that's just part and parcel of the.
**Jim Porell (Rocket Software, Inc.)** 06:45 Oof.
**Matt Hogstrom** 06:46 velocity. I think we only got one actual semantic convention documented, which I think was the host name.
**Jim Porell (Rocket Software, Inc.)** 06:52 Yeah, yeah.
**Matt Hogstrom** 06:53 Yeah, so I'd…
**Jim Porell (Rocket Software, Inc.)** 06:54 Pretty… pretty lame.
**Matt Hogstrom** 06:55 Yeah, so, anyway, so I'm hoping, that we could make, we could make some… Accelerated process, progress.
**Jim Porell (Rocket Software, Inc.)** 07:03 Yeah. So, what has been happening, though, just to give you a feel, was… We knew what the other systems had done, so, you know, if you've got a database system, how close is that to DB2? So… Let's… let's try and map what is…
**Matt Hogstrom** 07:19 Yeah.
**Jim Porell (Rocket Software, Inc.)** 07:20 And then what's unique? And Splex is an area that's definitely unique.
But it's clustering with a twist because of the shared data model. So, we looked at those kind of things. Now.
to Rudiger's credit, he's a Linux guy, so he doesn't really know ZOS that much either, but… Right. So we did things like that, MQ, same kind of thing, you know, Kix and Tomcat look similar. IMS is kind of the weirdo, because it's got both transaction management and database.
**Matt Hogstrom** 07:49 database.
**Jim Porell (Rocket Software, Inc.)** 07:49 you can make similarities. But then they get into the process model, and that's where this kind of bogs down, because… You can look at the process model as an address space.
But then when you drop… when you drop into, is it a kicks process, a batch process, USS process, DB2 store procedure, now you're getting into some variations that are unique to the mainframe. So… And so we've been debating that. To your point, you know, and I know, you know, you're on… you're on the, you know, CysView type stuff, I'm on the… Omegamon stuff, put out gazillions of metrics. But the reality is, when it comes to analytics.
it's always a curated set. It's always… it's always a small subset, so we don't have to define everything, for God's sakes. I mean, that would be a nightmare, but… but the goal has been, let's be consistent with what the distributing community's done.
**Matt Hogstrom** 08:49 I… so I'm totally in agreement. In fact, I think we start with what are the metrics that they're using for Postgres, or they're using for ActiveMQ, or Kafka, right? And then if we can align at that kind of course level from a metric perspective.
let's do that, because quite honestly, I think… In… at least in my head.
if we're sending it off to Datadog, etc, those are macro-level kind of signals, right? And if somebody really wants to get in and start looking at coupling facility statistics or channel statistics and things like that, they're going to go back to Omegamon or…
**Jim Porell (Rocket Software, Inc.)** 09:28 It could be an RF could be an RFE.
**Matt Hogstrom** 09:31 Exactly.
**Jim Porell (Rocket Software, Inc.)** 09:31 to that, yeah.
**Matt Hogstrom** 09:33 And so, you know, if we focus on it that way, I think it solves two problems. One, it becomes familiar, it becomes immediately almost usable.
And… And then, we're not over… overloading people with terms and things that just don't make any sense to them, right?
**Jim Porell (Rocket Software, Inc.)** 09:51 The other thing… the other reality is some customer complained that the hotel collector on Linux for ZVM was, too slow.
And they wrote up a PR, and they came in to us.
you know, as a standard body, it got closed because there's no documentation or anything like that, but… but I asked Rudiger.
Did anyone try it on x86?
Because my bet is, Whoever turned it on…
**Matt Hogstrom** 10:21 here.
**Jim Porell (Rocket Software, Inc.)** 10:21 We got so much volume.
that no.
**Matt Hogstrom** 10:25 Single.
**Jim Porell (Rocket Software, Inc.)** 10:25 collector could ever keep up with a mainframe. And that's my theory right now, is that, I know, you know, if you turned on collection for kickstream, SDB2, ZOS Connect, all that stuff, you know, OpenTelemetry, that you're screwed.
**Matt Hogstrom** 10:41 Niagara Falls with a teacup.
**Jim Porell (Rocket Software, Inc.)** 10:43 Yeah, yeah, yeah, yeah. And, the net effect is customers are really gonna have to choose the specific applications.
that they want to do OpenTelemetry on. They're not going to do everything. And the other interesting aspect of all the OpenTelemetry stuff is you know, there's an SDK to add into your applications. Well, you've been on the mainframe for 100 years. Security, reliability, and even this kind of stuff is going to be the system responsibility, you know? There'll be a couple of bleeding-edge financial customers that'll put it into a legacy COBOL app.
But 99% of their customers want KICS, IMS, Store Procedures, WebSphere to do it for them.
**Matt Hogstrom** 11:26 Well, I think most of them are gonna say, yeah, we'll take the span data that comes out of the runtime.
KICS, DB2, right, MQ, etc. That'll probably be good enough, and anything you want outside of that's going to be some kind of post-processed, annotated kind of work, right?
And, yeah, I don't… I don't see them doing that. In fact, I just related, but not related to this work group, are you… are you, I missed the formation of the… Work group to talk about…
**Jim Porell (Rocket Software, Inc.)** 11:56 For OpenTele Project, yeah, because I… for some reason, I think Greg… Greg was in it, and he kind of said, yeah, show me the business case, and I'll come back to you, because he was like, you know, I put all this money into CLI, and it was Zoe, and nobody did squat, you know, besides.
Besides Broadcom, so…
**Matt Hogstrom** 12:16 Oh, dude.
**Jim Porell (Rocket Software, Inc.)** 12:16 Do you say that?
**Matt Hogstrom** 12:16 Dad on the call?
**Jim Porell (Rocket Software, Inc.)** 12:17 Oh, yeah, pretty much. Okay, good. Yeah, no, he was very clear, and he goes, we need, you know, we need a business view of this. You know, there's got to be an ROI, both to the vendors and to the customers, but you're, you know, and part of the… part of the reason for this whole thing was.
all the vendors have reduced their contribution to the Open Mainframe project, and guess what? Who do you think pays John? So, John's like, I gotta get a paycheck, so now he's a development director, I gotta figure out other things that these people can invent so that I continue to get paid.
No, that's the way I do.
**Matt Hogstrom** 12:56 I get it.
**Jim Porell (Rocket Software, Inc.)** 12:57 club.
**Matt Hogstrom** 12:57 I get it. Well, when we first did Zoe back in, I guess, 2018, I think we were doing it with Rocket in 2017, when Cho was there. You could look at it, and Rocket had its interest, which was the desktop.
Yup. And… Broadcom, or CA at the time, had interest in their CLI.
**Jim Porell (Rocket Software, Inc.)** 13:18 A lot.
**Matt Hogstrom** 13:18 Right? And IBM, was interested, but they really… we didn't really bring a whole lot to the party, because I was… I was running it on the IBM side back then.
**Jim Porell (Rocket Software, Inc.)** 13:28 Oh, okay.
**Matt Hogstrom** 13:30 And so… at this point, I think that probably the most popular thing that I can see out of Zoe is the extensions for VS Code.
Yeah, definitely. That's huge.
**Jim Porell (Rocket Software, Inc.)** 13:43 Well, I'll give you one exception. I was the USS architect, and what they did on the desktop for the terminal session, where you didn't have to do split-screen TSO anymore.
**Matt Hogstrom** 13:55 Oh, oh, okay.
**Jim Porell (Rocket Software, Inc.)** 13:57 That's huge in terms of getting portability, but the rest of it, yeah. And it could have been a lot better, but…
**Matt Hogstrom** 14:04 Yeah, well, and I wasn't… I wasn't throwing stones at any of the technology. My point was, each company that came together brought their kind of thing, and I think… I think everybody universally said, well, we have this cool thing that we can't sell. There's just no way to monetize it, right? So maybe we can all give our stuff away. And, like, we tried to get IBM to be interested in API ML, because we thought, hey, if everybody registered to a common discovery service.
**Jim Porell (Rocket Software, Inc.)** 14:33 But that's really good, yeah.
**Matt Hogstrom** 14:36 Yeah, well, maybe you can help rally the troops, because I would love to see that in. That should be SMF, from my perspective, right? Because then it's part of the platform, a common registration management thing and whatnot, so… But anyway, the, back to the OTEL. I… are you guys… I've already compiled the OTEL collector on ZOS, and I'm starting to play around with it.
I… I haven't… I don't think we've actually kicked off the group yet, or not. So I… I was gonna join, even though Greg said we're not committing resource, I don't think participating is really a problem. I think he just… we're not… I'm not committing 10 new developers to it, right?
**Jim Porell (Rocket Software, Inc.)** 15:21 And we're kind of in the same boat, so… yeah. That's why I was asking Rudiger, is IBM… what's IBM's skin in this game? You know, are you guys gonna contribute software? And he's like, it doesn't get done by the community. Yeah, no. No.
**Matt Hogstrom** 15:35 No, that's… and I think it's the same thing. I think it was funny, well, you worked at IBM, right, like I did.
**Jim Porell (Rocket Software, Inc.)** 15:40 Yeah.
**Matt Hogstrom** 15:41 It was like, well, IBM, you know, said it's good. I'm like, well, no, you spoke with Mike Fulton.
Fuck.
But he's one of many IBMers, right?
**Jim Porell (Rocket Software, Inc.)** 15:51 Yeah, yeah, yeah.
**Matt Hogstrom** 15:52 We'll see where that goes, so… Alright.
**Jim Porell (Rocket Software, Inc.)** 15:55 Yeah, if they're gonna contribute bodies, that's… that's what's important. But not only bodies, but worker bodies, not watcher bodies, so…
**Matt Hogstrom** 16:04 Well, the other thing is, quite honestly, it's the business case, and it's the go-to-market.
**Jim Porell (Rocket Software, Inc.)** 16:10 No, I hate it.
**Matt Hogstrom** 16:11 nobody's downloading anything from OMP. They're getting.
**Jim Porell (Rocket Software, Inc.)** 16:16 Right.
**Matt Hogstrom** 16:16 Rocket through your delivery channel, or through our delivery channel.
So, we're almost, like, doing it in the open, and we're still the distribution network because customers want a throat to choke.
**Jim Porell (Rocket Software, Inc.)** 16:28 No, no, they need…
**Matt Hogstrom** 16:30 points.
**Jim Porell (Rocket Software, Inc.)** 16:30 They want support. Nobody's… you know, that all works on individual x86 platforms, but when you're talking Mainframes with thousands of, you know, consumers and stuff.
You don't… you know, and I had a customer, by the way, just complain about, oh, you're putting open source in. I think we're using ClickHouse with, Omegamon as a time series database.
**Matt Hogstrom** 16:52 Oh, are you?
**Jim Porell (Rocket Software, Inc.)** 16:53 Yeah, yeah. Why, are you guys using it too?
**Matt Hogstrom** 16:56 Yeah, we use Click House. Oh, cool. Well, are you actually running it on ZOS?
**Jim Porell (Rocket Software, Inc.)** 17:00 No, we're gonna put.
**Matt Hogstrom** 17:02 Everybody runs eLinux?
**Jim Porell (Rocket Software, Inc.)** 17:03 and Linux, and ZCX, yeah. Okay.
**Matt Hogstrom** 17:05 Okay. So, yeah, well, we use it off-platform.
**Jim Porell (Rocket Software, Inc.)** 17:09 Yeah, yeah, well, where you… right now, it's Bring Your Own Click House, but, we're… we got a 390 deliverable, and by the way, there's 3 products that'll ship with it, just to give you the heads up. It's Instana, IntelliMagic, and Omegaon, so…
**Matt Hogstrom** 17:25 Oh, that makes perfect sense. Okay.
**Jim Porell (Rocket Software, Inc.)** 17:26 What we're not gonna do is pay.
like we paid for Grafana, or I got IBM to pay Grafana to do the 390 deliverable there, but here's… Let me send you my chat, and for some reason, we are recorded here. Yeah. So, Let's go offline.
**Matt Hogstrom** 17:49 Yeah, that's fine.
**Jim Porell (Rocket Software, Inc.)** 17:54 There you go. So, yeah, give me a holler after, you know, we can drop from this, and then, give me a holler, we can continue the call.
**Matt Hogstrom** 18:01 Yeah, okay, that's probably a good idea. All right, Matt, I'll talk to you in a few minutes.
**Jim Porell (Rocket Software, Inc.)** 18:05 Bye. Yep, bye.
