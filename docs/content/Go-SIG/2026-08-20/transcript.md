SIG: Go SIG
Date: 2026-08-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Robert Pająk (Splunk Inc.)** 00:19 I thought that was Tyler, can you hear me?
**Tyler Yahn (Splunk)** 00:21 Yeah, I can hear you, can you hear me?
**Robert Pająk (Splunk Inc.)** 00:23 Yes, awesome.
**Tyler Yahn (Splunk)** 00:25 How's it going?
**Robert Pająk (Splunk Inc.)** 00:27 Fine.
OSU.
**Tyler Yahn (Splunk)** 00:30 It's okay, yeah, got some allergies for some reason, I don't know why, but yeah.
**Robert Pająk (Splunk Inc.)** 00:34 Oh, strange for this.
Part of the year, I will say. What happens?
**Tyler Yahn (Splunk)** 00:40 Yeah, it's like, the Pacific Northwest will always have… Potential. There's always just stuff in the air around here.
**Robert Pająk (Splunk Inc.)** 00:46 But yeah, who knows?
**Tyler Yahn (Splunk)** 00:48 Yeah, it's usually not bad, but… I don't know.
**Robert Pająk (Splunk Inc.)** 00:51 Pedrique as well?
**Tyler Yahn (Splunk)** 00:53 What's that.
**Robert Pająk (Splunk Inc.)** 00:54 Headache as well.
**Tyler Yahn (Splunk)** 00:56 A little bit, yeah, not too bad, but yeah, yeah.
Are you still, away?
**Robert Pająk (Splunk Inc.)** 01:07 Yeah, until next Tuesday, probably, I'm not sure if I'll be able to join Tuesday's meeting. It depends how well the drive back to home takes, because.
**Tyler Yahn (Splunk)** 01:17 Oh, yeah.
**Robert Pająk (Splunk Inc.)** 01:18 A 7-hour drive, and you never know how it goes into things, packing, etc. Wow.
**Tyler Yahn (Splunk)** 01:24 Yeah, yeah, yeah, do you have your…
**Robert Pająk (Splunk Inc.)** 01:26 Your kids, I think?
Yeah, yeah, exactly. I used to, like, driving 5 at 5 AM, So, we went when the… when the… when my daughters were still sleeping, I was just putting them in the car, and then they were sleeping all half of the… half of the, you know, half of the way. But right now, they are too old, and they wake up anyway.
**Tyler Yahn (Splunk)** 01:49 Yeah, it's definitely a lot harder, yeah. So you gotta stop all the time, yeah.
**Robert Pająk (Splunk Inc.)** 01:55 It's not that bad. It's pretty easy, to be honest.
Like, one of our friends, a cousin, told us that probably right now is the easiest part of our life as parents.
**Tyler Yahn (Splunk)** 02:14 Yeah, right? I guess they're… they're old enough to kind of do their own thing, but they're not so old, they're gonna give you a hard time. Exactly. Yeah.
**Robert Pająk (Splunk Inc.)** 02:20 That's exactly… they are all… they can do everything by themselves, but yeah, exactly. We just have to know.
Yeah. Rolling issues, etc.
**Tyler Yahn (Splunk)** 02:30 Yeah, yeah, exactly.
**Robert Pająk (Splunk Inc.)** 02:32 yet.
Hello?
**Puneet Singh** 02:38 Hello, Robert Turner.
**Tyler Yahn (Splunk)** 02:40 Hey, Puneet, how's it going?
Beautiful.
**Puneet Singh** 02:44 A bit slow week, I would say. Yeah.
Yeah, so… the GitHub outage was a bit of surprise.
**Tyler Yahn (Splunk)** 02:51 Ugh, dude, it's brutal.
**Puneet Singh** 02:56 I was… I was seeing some updates on GitHub, you know, that someone updated this issue. I was like, let's, you know, in solidarity, stop… everyone stop developing on GitHub until it gets stored on this side also. So… so yeah, but… but… but it was, like, it lasted more than I thought, actually, so…
**Tyler Yahn (Splunk)** 03:14 Yeah, it was, it was just all day for me on Monday. Yeah, it was rough. I, I was, like, kind of getting some stuff done with the CLI, but then I was just like, this is just… I'm just done. Like… like, CI was just so down that it was, like, it didn't even matter if you got something merged, it was, like, it's never.
**Puneet Singh** 03:30 be up.
**Tyler Yahn (Splunk)** 03:30 Actually, yeah, so… yeah, so, it was rough.
Yeah, it would have been a better day to have taken the day off and just gone outside or doing something else, yeah.
**Puneet Singh** 03:41 Yeah, you could say that, yeah.
**Tyler Yahn (Splunk)** 03:42 It's tough when you're, like, sitting there waiting, you're like, do I just give up, or do I… And of course, that was, like, also the day we were trying to get a release out, so…
**Puneet Singh** 03:52 Yeah, you kind of, expect that, yeah, it might be one or two hours, so just, you know, let's take a break for one hour and come back, and it lasts for, like, 3 or 4 hours, I think? So, yeah.
**Tyler Yahn (Splunk)** 04:04 Yeah, it was a rough one.
Well, we're coming up on… 5 minutes in, so we could probably start in here.
If you haven't yet, please go ahead and add your name to the attendees list.
And I will start sharing my screen.
Cool.
**Robert Pająk (Splunk Inc.)** 04:34 I think my items will be the last.
**Tyler Yahn (Splunk)** 04:37 You wanna go last? Is that what you're saying?
**Robert Pająk (Splunk Inc.)** 04:41 Yes, I think it's okay.
Pretty cool, less…
**Tyler Yahn (Splunk)** 04:44 Okay.
Well, if that's the case, I think I see Florian here, so we can, start… There… Yeah, Florian, you wanna, take us off? You wanna talk about a issue?
**Florian Lehner** 04:58 Yes, hello, everyone. I think not everyone on the call knows me that, hi, I'm Florian. I'm working especially on profiling, and whenever there is a profiling topic, I pop up in different SIGs.
And today, I want to talk about, Process Context. Process Context is an OTAP that was merged, for some time ago, and we have, readers in OBI and, eBPF Profiler, and, the idea is to make it more accessible for, for users. And so this, SDK idea came up, hey, how can this be done? And so the proposal is to, introduce a new SDK process context for the Go part.
That, uses this protocol and, publishes, publishes the information store, resources, resources accordingly. The overall idea is so that people, auto-instrument their application, with the Go SDK, this should be automatically, working, so, everything they have as a resource resource should, then also be published via, this, resource, this, process context.
And, yeah, that's why I'm here and, would probably ask for, feedback.
**Tyler Yahn (Splunk)** 06:32 Yeah, thanks, for opening this. This is… it's great. I mean, I definitely… I totally missed this, so, yeah, thanks for bringing it up.
Can you walk me through how this, like, actually gets integrated into the SDK? Like, where does this publisher integrate?
**Florian Lehner** 06:48 So, the idea would be that, an SDK just, adds this publisher, and the publisher, receives via the update, function, resources, resources, everything that, ends up at, resource attributes on, on the proto level, so, logs attribute, resource attributes, span, and, the others. And, this update function receives them, takes them, and, publishes them via the, via the, socket. That's, that's the rough idea.
**Tyler Yahn (Splunk)** 07:26 Yeah, so the part where you said, like, the SDK gets the publisher, like, where does the SDK get the publisher? How does that interaction look?
**Florian Lehner** 07:35 I… I'm not sure I get the… Get the question correctly, so, I'm not an expert on the outer SDK for Golang. That's… that's the part where I'm not familiar with, good, in a good way. That's… probably the… Whenever someone initializes, Go Auto instrumentation.
then a publisher should be called in this context.
**Tyler Yahn (Splunk)** 08:06 The Go Auto instrumentation.
Okay, yeah, I'm a little bit more confused now. So, so we have, like, the Auto SDK in, like, the global package, is that what you're talking about, or are you talking about.
**Florian Lehner** 08:22 I think, the, the Alto SDK, I would say.
Okay. Sorry for the, for the wrong, term, terms,
**Tyler Yahn (Splunk)** 08:34 Hmm… maybe I'll come at this from a different angle. Who passes something to the update? Is this something in, like, the process chain? So, like, as the SDK is processing records that are coming down, or is this something that, like.
Yeah, because, like, a resource is an SDK concept, right?
**Florian Lehner** 08:52 Yep.
**Tyler Yahn (Splunk)** 08:53 Yeah. So, is this, like, in an export path? When… an export is getting fired, then this resource is passed to the update, or is this only, like, when, like, a tracer provider is created that, like, has a resource, right? Like, then it's passed here.
**Florian Lehner** 09:09 When the trace provider is created and gets this information.
**Tyler Yahn (Splunk)** 09:14 Okay.
I think I see. So, on the creation path, for any sort of provider type, some meter provider.
provider, whatever, logger provider.
In that init function, they also will then need to create a publisher, and then… pass that publisher. So our resources are static, but, like, anyways, like, so we're gonna, we're gonna pass that update to this once.
**Florian Lehner** 09:43 I'm a sure…
**Tyler Yahn (Splunk)** 09:44 Sure.
It's going to handle all of the, you know.
delivery or, sorry, like, bubbling up of that information to the correct location, and then, like, the SDK.
**Florian Lehner** 09:55 He hasn't.
**Tyler Yahn (Splunk)** 09:55 to care about at that point. So, it's more like, this is… this is something that's going to be called, and then… created, by the SDK during the creation. The lifecycle… It's an interesting one, though, for us.
So, yeah, okay, if that makes sense.
The lifecycle of the SDK Does the publisher need to exist the entire time that that… just because it has to respond to any sort of request? Okay.
**Florian Lehner** 10:27 Yes, yes, yes, it also, is the… It's the… it manages the socket.
So, that's why I need to exist.
**Tyler Yahn (Splunk)** 10:45 Okay, yeah, I mean, that makes sense to me. I don't know if others have questions on it, but I would probably say that we would want to put this in an experimental package, like an X package,
**Florian Lehner** 10:57 And…
**Tyler Yahn (Splunk)** 10:58 do a dependency on that, because I definitely don't want to, like, stabilize this beforehand.
But otherwise… Yeah.
I'm also interested why… new publisher accepts a resource at the start, and it also has an update method? Is that just because, like, if the resource, or the resource that we're just gonna change is the thing?
**Florian Lehner** 11:19 It could change, yes.
**Tyler Yahn (Splunk)** 11:21 Yeah.
**Florian Lehner** 11:21 That's, that's the idea.
**Tyler Yahn (Splunk)** 11:24 Okay, and then, so what happens when… I'm sorry, it's been a while since I looked at this OTEP, but, like, what happens when, like, somebody creates a trace provider and a meter provider? Like, how does that… Get, like, surfaced at this one socket.
**Florian Lehner** 11:44 It should be done via the prox bitmaps, so… That's a.
**Tyler Yahn (Splunk)** 11:52 Okay, yeah.
**Florian Lehner** 11:53 What happens if two… a form process 2 opens two sockets?
I think… The OTAP does not cover this at the moment.
There should be only one Socket per process?
If… There's a trace provider and a logs provider, there should… there could be two.
I don't have a… clear answer to this at the moment. I need to go back…
**Tyler Yahn (Splunk)** 12:36 Yeah, no, that's fine.
**Florian Lehner** 12:36 No.
**Tyler Yahn (Splunk)** 12:38 But yeah, I mean, I… I… Yeah, if we can solve, like, that… problem, like, this API seems fine to me. Like, the location, I would put this in an experimental package, and we can… iterate on it. Behavior-wise, like, yeah. And then as this stabilizes upstream in the sophistication, We'll have to find a home for it, I don't know exactly where, maybe even, like, the top-level SDK package is the best place for it, but… We can see, yeah. Any other thoughts from Robert or Puneet?
**Robert Pająk (Splunk Inc.)** 13:11 I have, well, probably more clarifying questions, or maybe regarding the scope.
Do I understood correctly, Florian, that you said that the resource will be created by OB and then injected?
Okay?
**Florian Lehner** 13:29 No. No, the other way around, the other way around. Obei will be in receiver.
**Robert Pająk (Splunk Inc.)** 13:37 So, it's about manual SDK, and you'll be publishing this process context using manual SDK. It will be not Auto SDK, right?
**Florian Lehner** 13:48 Ideally, it would be Auto SDK, so that, people enable, use the Auto SDK, in their application.
It should be pulled in, that's… that would be the probably natural next step, and OBI and profiling can benefit from this information and can read this information.
**Robert Pająk (Splunk Inc.)** 14:14 Okay, because I think these are different paths when Obi creates an SDK, and when Go creates an SDK. Am I wrong, Taylor, or… Yeah.
**Tyler Yahn (Splunk)** 14:23 No, you're right.
**Robert Pająk (Splunk Inc.)** 14:24 Oh my gosh.
**Tyler Yahn (Splunk)** 14:24 Florian is also saying. Like, it's not meant for…
**Florian Lehner** 14:26 Whatever.
**Tyler Yahn (Splunk)** 14:27 Like, like, the idea is that, like.
Right now, like, the SDK, like, the hotel SDK itself has a lot of, like, context around the process discovery and that kind of thing.
**Florian Lehner** 14:36 thing, right?
**Tyler Yahn (Splunk)** 14:37 like, Obi may just be like, I don't know, I'll do my best to find out, like, what this process is, like, or it can't even figure it out. So yeah, what Florian is describing is, like, it just… it needs to… that information needs to pass one away to Obi, right now for…
**Robert Pająk (Splunk Inc.)** 14:49 Yes, okay, so I go to somewhere, yeah.
So, a few tips, maybe I can put it in the issue, when I was doing Lux API SDK, to create the design, I first created, you know, we also had an issue like that, but when we were creating… first, we had a prototype, which was a draft PR, just, you know, have a feasibility study to check if it's working end-to-end, and we also created, design doc in Markdown.
Because it's easier than discussed in, you know, than in an issue. But what it's… what was recently also, also, showed as an additional benefit.
is that when you have the design MD, it also helps the AI when you're working, because you have the decisions.
codified, you know, in the same repository, and then in future, it's more or less likely that when you'll be, you know, using AI to code something, it will make something which is not aligned with the design.
So, yeah.
So, just…
**Florian Lehner** 15:54 Yeah, thank you, makes perfectly sense. What I did not link, here is, I know.
**Robert Pająk (Splunk Inc.)** 16:01 R.
**Florian Lehner** 16:01 draft PR around this, and this draft PR was also used, with the implementation, with OBI. So, the OBI reader, can already make use of it, and, this draft PR was used, to instrument, an application, really.
**Robert Pająk (Splunk Inc.)** 16:19 Oh, cycling.
type.
**Florian Lehner** 16:21 Yeah, yeah.
**Robert Pająk (Splunk Inc.)** 16:22 processing, what do you mean?
**Florian Lehner** 16:23 Yep.
**Robert Pająk (Splunk Inc.)** 16:23 Awesome.
**Florian Lehner** 16:24 But it's really just a very, very simple, very, very simple, HTTP, web server that does nothing except for a Hello World, and, OBI was, Reading all their resource attributes.
I was using, this publisher and manually writing the, the resources, so, the part for the auto instrumentation, so I did not pull in, the Go, hotel auto instrumentation, but, manually used this, this API.
That's… that's… this was the, my testing, basically.
**Robert Pająk (Splunk Inc.)** 17:05 Last question, maybe I'm wrong, maybe my experience outdated, but I think that initially, in the OTEP, there was some idea of not using sockets, but some member… shared memory, or am I wrong?
**Florian Lehner** 17:20 Yeah, just… Yeah, this was, this was some, ideas in the, in the, at some point.
I'm not sure at which point this was changed, but the reasoning to go with sockets in the end was that it's compatible with every language.
**Robert Pająk (Splunk Inc.)** 17:40 language.
**Florian Lehner** 17:41 points.
**Robert Pająk (Splunk Inc.)** 17:41 Yep, I agree.
**Florian Lehner** 17:42 there is, so the Profiling SIG has also a proposal for the Process Context API for the Rust part.
And, someone is working also on the Java part, to cover these three topics, but I don't remember.
**Robert Pająk (Splunk Inc.)** 18:03 I, I…
**Florian Lehner** 18:03 language.
**Robert Pająk (Splunk Inc.)** 18:04 I mean, no, I think… I think it makes sense. There are also other, I think… I already know that Tyler was also looking, you know, at support for eBPF in Windows.
So, probably it can also be then easier to reuse, you know, if it will use sockets, not, you know, short memory, because I also expect that it may be troublesome between, you know, different operating systems.
So, I think it makes sense, I just wanted to make sure if we are on the same page, because I remember this shared memory often, because I was reviewing it, so just… just good to know.
**Florian Lehner** 18:36 Yep, yep.
**Robert Pająk (Splunk Inc.)** 18:36 No more questions. Thanks, Florian. Awesome work.
**Florian Lehner** 18:40 Thank you.
**Tyler Yahn (Splunk)** 18:44 Cool. Alright, yeah, so we've got next steps on that, Florian, we wanna… talk about the synchronization, but I think, like, even just getting a PR together to start on this is also, appropriate, so, yeah.
**Florian Lehner** 18:57 Yep, thank you.
**Tyler Yahn (Splunk)** 18:58 Cool.
Excuse me. Alright, next up, Puneet, you want to talk about, meter configurator PR.
**Puneet Singh** 19:07 Yeah, I mean, yeah, the bug has been going on for a while, so I think this was raised slightly before last week.
But the implementation is looking, like, stable, so would like, you know, if you get time to have a look on this PR, that would be great.
**Tyler Yahn (Splunk)** 19:27 Yeah, why did… Oh, this must be, like, your first PR.
**Puneet Singh** 19:31 So, yeah, I mean, it was surprising for me also that, you know, this… This is the first PR in the Go SDK.
**Robert Pająk (Splunk Inc.)** 19:38 You too.
**Puneet Singh** 19:39 a complicated.
**Robert Pająk (Splunk Inc.)** 19:40 You need to find some typo, and create VPR for some typo, really.
**Puneet Singh** 19:46 Yeah.
**Robert Pająk (Splunk Inc.)** 19:46 Okay.
**Tyler Yahn (Splunk)** 19:47 Yeah, that's, cool. Alright, so this just needs review, is what you're saying, though?
**Puneet Singh** 19:53 Yes, yes.
**Tyler Yahn (Splunk)** 19:55 Alright, Yeah, cool. Alright, yeah, put that on the list of things to do. Thanks for, thanks for putting this together. Looks like David's already reviewed it, so it really just needs one more, so Robert and me to… to come in.
So yeah, that'd be great.
**Puneet Singh** 20:09 food?
**Tyler Yahn (Splunk)** 20:10 Okay.
Awesome. Alright.
Last up, Robert, you want to talk about… Getting… just the next release, right?
**Robert Pająk (Splunk Inc.)** 20:19 Yeah, exactly. Two reasons. First is that there's a new version of Go, so we can, you know, when we make this release, we can sooner drop the next… the 126 version of Go just after the release. That's one reason. And second, I think there are, like, I think there's one PR left.
and I'll probably finish the auditing of stable logs, because if I understand correctly, after making a next release.
then I can make an RC release with, with this, with these, headers, you know, with these comments that do not change, and with adding to the hotel package the global logger provider, if I'm not mistaken, and then making of it an RC.
probably I will tailor-sync with you before, you know, doing everything for Darcy, but I think that was the workflow we did for Metrics, which was a few years ago.
**Tyler Yahn (Splunk)** 21:13 Yeah, it was. Does that mean that this needs to be in the next milestone, then?
**Robert Pająk (Splunk Inc.)** 21:18 all… yeah, all kind of RC Mine Stone, if we have an RC Mind Stone, that's how I understand it.
**Tyler Yahn (Splunk)** 21:24 Yeah, I mean, I think we need to create one. So, yeah, we can… Yep.
**Robert Pająk (Splunk Inc.)** 21:28 I have created a next milestone, we can put it there. I haven't created a dedicated RC milestone, I can do it after the meeting.
**Tyler Yahn (Splunk)** 21:34 Well, problem is you can't do two milestones, right? But, yeah.
Okay, I put it… put it in there. Okay.
And then… These can go…
**Robert Pająk (Splunk Inc.)** 21:46 marker?
**Tyler Yahn (Splunk)** 21:47 Yeah, these can go in this… this one, for sure. That sounds… sounds good.
You mean this one?
**Robert Pająk (Splunk Inc.)** 21:54 go to the current release, that's what you mean, or also to one for.
**Tyler Yahn (Splunk)** 21:56 Yeah, why not, right? I mean, like.
**Robert Pająk (Splunk Inc.)** 21:58 Okay.
**Tyler Yahn (Splunk)** 21:59 I mean, I… I mean, technically, we could still change them, so it's not gonna be completely accurate, but, like.
**Robert Pająk (Splunk Inc.)** 22:04 I don't know, but we are so close to that.
**Tyler Yahn (Splunk)** 22:06 Anybody who knows, knows, so I think that that's fine. Yeah, don't worry about that.
These audits, these need to get done. This is… This is probably next.
**Robert Pająk (Splunk Inc.)** 22:17 Listen.
**Tyler Yahn (Splunk)** 22:18 2, right? Yep. Okay, let's move that.
This PR… what's going on here?
**Robert Pająk (Splunk Inc.)** 22:35 I asked for… I kept asking a question before I went for a walk, and I think there was some movement, because I see that, or maybe it's just my comment.
Okay, so next milestone, I think.
**Tyler Yahn (Splunk)** 22:55 Mmm, no, like, this needs to get closed.
We need to open Initia if we need to actually track this.
With.
**Robert Pająk (Splunk Inc.)** 23:05 We don't have an issue for this.
**Tyler Yahn (Splunk)** 23:06 Okay.
**Robert Pająk (Splunk Inc.)** 23:07 It's just about configuration. Right now, I think it's static. I'm not sure if it's needed for the next release. It's just about adding configuration for this responsibility site limit. Right now, we are using some you know, value, which was set by default, and the specification says that it may be configurable, if I remember correctly.
That's why I suggest just, you know, not postponing, or at least because of that.
**Tyler Yahn (Splunk)** 23:39 Okay.
**Robert Pająk (Splunk Inc.)** 23:41 Okay.
**Tyler Yahn (Splunk)** 23:42 Yeah, and then… This is just the reach checklist, count limits, press… this… there's a PR for this, right?
**Robert Pająk (Splunk Inc.)** 23:53 Yeah, I addressed your comment, just… Pew.
Meetings ago?
**Tyler Yahn (Splunk)** 23:59 Okay.
Okay.
And then this is also just PR, waiting for approval. Okay, so yeah, it looks like we're pretty close. It's really these audits, and then… I think that's it, outside of this PR, right? There's nothing else really blocking…
**Robert Pająk (Splunk Inc.)** 24:35 Yep.
**Tyler Yahn (Splunk)** 24:36 Okay, are you gonna take the action item? Well, actually, let's go to contribute first.
**Robert Pająk (Splunk Inc.)** 24:44 We contribute, there's a bigger mess.
**Tyler Yahn (Splunk)** 24:48 Yeah.
Add docket resource container. This is… oh, that's why…
**Puneet Singh** 24:53 And I was like.
**Tyler Yahn (Splunk)** 24:54 I've seen PRs from you, like, how do you not have PRs? I was like, oh, because they're all in Katrip, that's why, okay.
**Puneet Singh** 25:01 I think the issue with this one is that it ports the logic as it is from the collector, but I think during review, one of the things… that was quoted, that it doesn't reliably read the container IDE. It depends on the os.host name, which is, like, bit.
You know, not a very reliable way to determine.
**Tyler Yahn (Splunk)** 25:23 I'm gonna…
**Puneet Singh** 25:23 Lehner ID.
**Tyler Yahn (Splunk)** 25:24 Yeah.
**Puneet Singh** 25:25 So, so yeah, I mean, it's, it's… totally up to the, you know, that, do we want to keep this or ship this and let her fix the issue? So, yeah.
**Tyler Yahn (Splunk)** 25:38 I see what you're saying.
Well, I mean, the whole project was to try to get things offloaded from the collector, right? And so, I guess, if that's the case, like, I'm okay if we wanted to just create an issue to track that work, and then we can say, like, look, this is just trying to get us parity from what's in the collector, and then we can go forward with that.
As long as we plan to, you know, follow up on it eventually, like, that sounds good, and we can unblock this PR, if that's… that's helpful.
**Puneet Singh** 26:08 Yeah, I'll create the issue, because the fix that we are going to make here will also be neat in the, in the code detector, so, yeah.
**Tyler Yahn (Splunk)** 26:16 Right, right. Yeah, that makes sense. Okay, let's… let's do that. That's a… that's a good point. I totally forgot that we were just porting.
Yeah.
Okay, Yeah, that sounds good. These are related to other issues that were fixed in, like, I think it was OTEL Echo or something like that? One of these? Essentially a bug that was found in all of them. These should be pretty straightforward, looks like there's not… movement from… Is there PR?
**Robert Pająk (Splunk Inc.)** 26:56 So…
**Tyler Yahn (Splunk)** 26:56 Oh.
**Robert Pająk (Splunk Inc.)** 26:57 I think there's so… I think there are… I think there are PRs for a lot of them, but I think all of them have some issues and some comments which are not addressed.
And I was even… looking before at 1PR, and… Yeah, there were problems there still.
Yeah. Maybe it was in this PR, maybe it was another one, I'm not sure.
But it does not look… Close to being merged.
**Tyler Yahn (Splunk)** 27:27 Okay, so what's your suggestion here?
**Robert Pająk (Splunk Inc.)** 27:30 What's the criticality of this issue?
I suggest moving to the next milestone, but yeah.
That's my suggestion, to be honest.
Unless someone finds this critical.
**Tyler Yahn (Splunk)** 27:54 I mean, isn't this producing invalid telemetry?
**Robert Pająk (Splunk Inc.)** 27:58 Yep.
And similarly.
**Tyler Yahn (Splunk)** 28:15 Yeah, I mean, I… I think…
**Robert Pająk (Splunk Inc.)** 28:20 The fact… the fact that it is… spans for this error, I think it's correct. The only missing part is that it has no error type.
So, in my opinion, it's not a critical bug. You know, the status is still correct.
**Tyler Yahn (Splunk)** 28:38 Yeah, I, I mean, I… Like, it's not crashing people, but, like, like, what sort of… maybe it's worth maybe doing more maintainer triaging things, and asking people in the PRs if they're able to get it out in a reasonable timeline, and trying to help shepherd those things through.
And if that's not the case, closing them and having other people work on it?
Is that something that you can take on, Robert?
**Robert Pająk (Splunk Inc.)** 29:10 Yes, I can.
**Tyler Yahn (Splunk)** 29:11 Okay.
And I think… I think you're… you're right, like, if no one's… actively working on if we can show that, like, people are, you know.
opening PRs, but they're not actually being followed up on, like, let's move it to the next milestone, but if it's just people are new to the project, and they're not really… They need help, let's provide that help.
**Robert Pająk (Splunk Inc.)** 29:31 Yes, so, I do not say that I want to abandon this kind of work, I just want to say that do not book the release, because only of these issues, that was what I wanted to message.
And I think we shouldn't…
**Tyler Yahn (Splunk)** 29:43 I think we should block the release if people are actively working on it, and, like, they're just stuck.
**Robert Pająk (Splunk Inc.)** 29:49 That's true as well.
**Tyler Yahn (Splunk)** 29:49 I don't think that we should actively block the release if, like, it's just… Work that needs to get done, and nobody's working on it, yeah.
**Robert Pająk (Splunk Inc.)** 29:57 Okay.
**Tyler Yahn (Splunk)** 29:58 Yeah.
So let's… let's try to help on that one, and then, yeah, I agree.
**Robert Pająk (Splunk Inc.)** 30:03 Everything applies to all of them.
**Tyler Yahn (Splunk)** 30:05 Agreed. Yeah, agreed. Yeah.
Okay, cool. But, so, yeah, if you can just maybe even just message, because it sounds like I've already messaged a few times, but just saying something in there, like.
you know, are you stuck? Like, are you able to keep working on this, and then we can… we can… Prioritize that.
Okay.
Because otherwise, I think that that's it, like, that's all the rest of the,
**Robert Pająk (Splunk Inc.)** 30:28 Also, for the auto echo, I remember there was some issue that we found out that there's an official OpenTelemetry instrumentation maintained by ECHO.
And we… I think we agreed on deprecating, and I also want to follow on this issue, so I'll probably find this issue and assign myself and try to work on that. It will, you know, decrease our maintenance burden on all accordance.
**Tyler Yahn (Splunk)** 30:54 That sounds great, actually. And then we could also close this issue here, if that's the case.
**Robert Pająk (Splunk Inc.)** 30:58 Yeah.
**Tyler Yahn (Splunk)** 30:59 Yeah, yeah, absolutely, yeah.
Yeah, so that… let's… let's do that. Yeah, I think that might have got dropped. I can't remember what you're talking about now, so, yeah, I'll have to take a look.
Okay, but otherwise, this looks good. I'm guessing that means that we're looking at a release next week then, Robert? Is that what you're thinking as well?
**Robert Pająk (Splunk Inc.)** 31:17 Yeah.
**Tyler Yahn (Splunk)** 31:18 Cool, alright.
**Robert Pająk (Splunk Inc.)** 31:19 Exactly. I thought about tomorrow to start working on it, but we must be optimistic.
**Tyler Yahn (Splunk)** 31:26 I mean, who knows? Like, maybe I'll…
**Robert Pająk (Splunk Inc.)** 31:28 I can start preparing. I can start preparing the release, but yeah, we can merge later.
**Tyler Yahn (Splunk)** 31:33 Yeah, that sounds good.
Okay, cool.
Alright, let's… let's do that. Anything else?
On that one, Robert?
**Robert Pająk (Splunk Inc.)** 31:44 That's all from the side.
Cool. Thank you.
**Tyler Yahn (Splunk)** 31:46 Yeah.
Okay, that's the end of the written agenda. Any other topics folks had that aren't on the agenda that you want to talk about?
**Puneet Singh** 31:59 I wanted to… sorry, go ahead.
**Tyler Yahn (Splunk)** 32:02 No, no, no, I got a totally different announcement, so, yeah.
**Puneet Singh** 32:06 I wanted to ask, regarding the, there seems to be some sort of community membership for OpenTelemetry, and, you know, what does it… Mean, actually?
**Tyler Yahn (Splunk)** 32:21 Yeah, good question. So, the community membership is just, essentially, you are part of, like, the hotel org, which gives you, like, read permissions, and, like, the main thing is that I can assign things to you, without you having to comment on an issue or something like that.
It's a little badge on your GitHub profile, you are a part of the community at that point. It takes… Not much, if you're not a part of the community at this point, like… you could be. You've already committed, you know, multiple weeks, integrating with us, PRs, there's a lot of stuff. You'll need two sponsors, from people at different companies, so I'm happy to sponsor you as somebody from Splunk. I'm sure if you pinged… other, you know, people, I think Florian's on the call, but David also, like, other people that you've interacted with, they'll… I'm… We're pretty open to getting people involved in the community.
it's kind of a first step. So from there, then there's, like, additional roles of privilege of being an approver in a project, or being a maintainer in a project, but yeah, just being a part of the community is the first step, yeah.
So… Yeah.
**Puneet Singh** 33:29 You mentioned that thing. Sorry, go ahead, Robert.
**Robert Pająk (Splunk Inc.)** 33:32 The process, there's a dedicated template, issue template in the community repo, on the TS3 Community.
And also, I think there's some documentation about how to get the membership, what are the requirements. But in short, there's… there's… you know, you create… you click New Issue in the community repo of OpenTelemetry, and there's something like New Membership.
and you just add your… your… you just proof… as a proof of your contribution, some PR, some issues that you'll be working on… on, and, say what SDKs are you working on? Oh, Tyler is sharing.
And, yeah, and you ask for sponsors, which could be, for instance, you know, Tyler and David, just make sure to ping, you know, when you pay the issue, also ping on Slack whenever one agrees to be your sponsor.
**Puneet Singh** 34:26 Got it.
**Robert Pająk (Splunk Inc.)** 34:28 Ripple.
**Puneet Singh** 34:28 Organization.
**Robert Pająk (Splunk Inc.)** 34:29 should request.
Okay.
**Puneet Singh** 34:35 Sorry, I totally missed that, you know what button you clicked, actually.
But, yeah, okay.
**Tyler Yahn (Splunk)** 34:40 Yeah, I will…
**Robert Pająk (Splunk Inc.)** 34:41 the top.
**Tyler Yahn (Splunk)** 34:42 I'll put this in here, yeah.
**Puneet Singh** 34:46 Tyler, you mentioned one interesting thing that, That once you become a member, you can assign things to me, but what does it mean? Like, it's… is it like that, yeah, I mean, there's privilege, but there is also responsibility comes with it, so the responsibility part, I want to understand, actually.
**Tyler Yahn (Splunk)** 35:05 The responsibility part comes really at the maintainer level. Like, there's a little bit more at the approval level, but, like, no, there's no responsibility Other than… it's just privilege.
you know, it's not… Yeah, like, I think, like, go look at the official docs in the community repo for it, like, I may be… it may have changed, but it's more, no. It's just access to the org.
You need to follow the, you know, appropriate behavior. You're, you're, you know, required to be, you know.
a good standing community member, meaning that you're not a jerk and, like, you're, you know, that kind of thing, but, like, no, that's not, like, you don't get kicked out if you don't, like, participate in, like, 3 months or something like that. No, it's more just, like, Yeah, you've just been a part of the project, and I get to assign things to you… I can assign things to you right now, it's just that you have to, like, comment on those issues, and you have to be a part of the discussions, because I can't just, like, link random people in GitHub to, like, certain things.
Yeah, the next steps are, like, if you want to, have your, like, reviews on PRs go from, like, a gray checkbox to a green checkbox, you need to be an approver.
which can give you elevated permissions, and that does come with responsibilities, meaning that, like, you need to participate in active reviews, you need to, you know, join SIG meetings, you know, like, things that you're actually already pretty close to doing. Like, you just need to be an active member at that point, and, like, when you drop off of that active membership, then you can lose that responsibility, but, like, it's not, like, critical. And then… The real one is the maintainer, where, like, you are literally then in charge of the success of a SIG.
Which sounds great, but it's a lot of work.
**Puneet Singh** 36:46 I can see, you know, the work that you… David and Robert do, so, you know, it's… it's, it's not… doesn't look easy, actually, especially the release part and looking at things end-to-end, actually, so… so, yeah.
Yeah, it will take some time.
**Tyler Yahn (Splunk)** 37:01 Yeah, absolutely. But, yeah, I mean, like, no, from the community membership perspective, like, it's… it's… there's no… no. There's no… there's no real responsibility other than, like, yeah, being a good community member, yeah.
**Puneet Singh** 37:14 Got it. X.
**Tyler Yahn (Splunk)** 37:16 Yeah.
Yeah, and we love adding more people. I think, It's all a GitHub thing as well, like… Obviously, like, a community member is just also, like, the social side of things, so that, that you don't need to… access to. You're already… you're already doing that. So, but yes, on that note, like, if you wanted to if you're showing up to KubeCon in North America, which you should, it's gonna be great.
Then, like, that's a great place to, like, also continue, like, that being a part of that community. We're gonna meet in person, there's gonna be a lot of really good events and that kind of thing, so… Yeah, if you have access and you have the ability and means to be able to do it.
next year's also in Barcelona for KubeCon EU, you should join that as well.
**Puneet Singh** 38:07 Yeah, let's, let's see how, you know, that's a bit in, like, distance, so we'll see, how next year turns out.
But yeah, I think the reason for asking this question was that I was seeing just multiple things. One is, like, there is CNCF membership, then there is OpenTelemetry, and I think being an approver or maintainer, I had, like, much more clear idea that what needs to… happened there, so that part I'm still… I don't have any issues with that, with my current… and there is a lot to learn and adopt to before, you know, But yeah, I mean, the membership regarding OpenTelemetry, that part wasn't clear, so yeah, that's fine.
**Tyler Yahn (Splunk)** 38:45 Yeah, yeah, it's just org… it's just GitHub organization membership, is what that is. The CNCF stuff is, I think it's just signing up on it for an account on that, technically, but I don't think actually it's that hard to do that. Like, I don't think you even need approval for that.
But, yeah, it… if you're a part of OTELO, that is a part of the CNCF, so it's also, yeah.
Just what access you want.
I think… I think also, if you're a member.
Don't quote me on this, I think you can see, projects.
and, like, all the projects in the org, and not… like, non-members can't see projects, which is kind of a weird thing. Like, we've tried to fix that. Like, by default, I think they're private to only org members, which is a problem, because we try to share these things publicly. But yeah, it shouldn't be the case, but it is sometimes, yeah.
**Puneet Singh** 39:37 I think, with respect to the amount of projects, I'm pretty happy with what I'm seeing, actually, within the… I don't want to… I mean, there is… there is already so much context to…
**Tyler Yahn (Splunk)** 39:47 Yeah, absolutely.
Well, cool. Yeah.
I think also, like, one thing… the thing I was going to mention is the KubeCon stuff, like, you can also think about, like, you know, start thinking about submitting talks. The KubeCon EU is open for the CFP, so if you wanted to talk about work that you're doing in the hotel.org, like, that's another great place, and other people on the call, like, start thinking about talks to submit there. I think it goes… Till October is when the CFP closes, so yeah, we've got some time, yeah.
**Puneet Singh** 40:24 That's good.
**Tyler Yahn (Splunk)** 40:25 Yep.
But cool. Any other topics, ideas, questions, concerns from folks?
**Marc Schäfer (T&A SYSTEME)** 40:32 Maybe just to add, the scholarship for KeepCon North America just opened, I think, 2 days ago or so.
Yep.
**Tyler Yahn (Splunk)** 40:39 Oh, nice. Yeah, I didn't know that. That sounds great. That's a great way to get funding to get to go, so thanks for bringing that up, yeah.
**Marc Schäfer (T&A SYSTEME)** 40:46 Yep, so that you don't need to pay the full Full price? Oh, the ticket price at all.
**Tyler Yahn (Splunk)** 40:54 Yeah, it's really nice when your company, or whoever you can work for can do it, but, like, if that's not available, like, it's really nice to be able to go, just for the community building stuff, so it's good to see that sort of thing.
**Marc Schäfer (T&A SYSTEME)** 41:05 for example, myself, I don't have the possibility to go from company, because I'm doing this all in my free time, so, Aye.
Applied for funding, the same as last year.
**Tyler Yahn (Splunk)** 41:18 Nice. Yeah.
Yeah, so definitely… That's great to know. Yeah.
Puneet where… you said you're based out of India, right?
**Puneet Singh** 41:28 I'm in India right now, yeah.
**Tyler Yahn (Splunk)** 41:29 Yeah, they also have a KubeCon India, as well. It's a little bit smaller, I think it's only, like, a day, or maybe two days, or something like that, but yeah, just a heads up. I know we've had other community members go to that as well, so there's also a community there.
**Marc Schäfer (T&A SYSTEME)** 41:41 I think that was just recently, I think a few weeks ago or so.
**Tyler Yahn (Splunk)** 41:44 Yeah, it's, yeah, it's, it's in the summer, for sure, yeah.
**Puneet Singh** 41:51 Cool.
**Tyler Yahn (Splunk)** 41:54 Cool.
Awesome. Well, if there's no other topics, we can end the meeting here.
It's good seeing you all. Thank you all for joining. We will talk again, next week, or asynchronously. Till then, bye.
**Marc Schäfer (T&A SYSTEME)** 42:08 Alright.
