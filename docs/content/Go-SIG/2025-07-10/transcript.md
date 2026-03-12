SIG: Go SIG
Date: 2025-07-10
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 01:47 Hey! Damien!
**Damien Mathieu** 01:49 Hey! How are you?
**Tyler Yahn** 01:51 Doing? Well, how about yourself?
**Damien Mathieu** 01:53 Good.
**Tyler Yahn** 01:56 It's coffee time over here.
**Damien Mathieu** 01:58 Interesting.
**Tyler Yahn** 02:02 Is that a 3D printer I see behind you.
**Damien Mathieu** 02:05 It's a laser cutter.
Oh, a laser! Oh, cool!
Feel free to pinterest here.
**Tyler Yahn** 02:11 Oh, even better. Yeah, both of them.
Yeah, that's awesome.
**Damien Mathieu** 02:15 Yeah, I'm not using the laser pretty much.
**Tyler Yahn** 02:18 No. Oh, okay, yeah. I I feel like, I think when I 1st used a laser cutter, it was like way back in college. And it was like, this is the coolest thing in the world. Then you start to like, realize, like.
yeah, it's kind of limited, like, it's very like 2 dimensional like that's.
**Damien Mathieu** 02:34 Very specific. Yes.
**Tyler Yahn** 02:35 Yeah, yeah, yeah.
**Damien Mathieu** 02:38 I mean it's why it's not with this one. But for my wedding like 8 years ago, I actually took some like fine pieces of woods, and I cut the wedding like the dinner menu onto them, which which was pretty pretty nice and impressive.
**Tyler Yahn** 03:00 Oh, yeah, that is really cool. That's that probably would have cost a lot of money if you had to pay somebody to do.
**Damien Mathieu** 03:05 Oh, yeah. Yes.
**Tyler Yahn** 03:07 Yeah, that's really cool.
Yeah, see? Like, things like that are just like, really fun little projects. But yeah.
hey, Sam, how's it going.
**Sam** 03:19 Okay, very good. I wonder what would you do to that 3D printing machine?
**Damien Mathieu** 03:29 Sorry what I'm doing with a free printer.
**Sam** 03:31 Yeah.
**Damien Mathieu** 03:33 Many, many things like like like this one. It's like for this headset.
Very simple. But yeah, lots of like small things are like house repairs because it's 3D. It's much easier to find uses for it than the laser cutter.
**Tyler Yahn** 03:54 Yeah, right? Like, it's hard to not find uses for it.
You want to.
That's something you could also just make it right.
**Damien Mathieu** 04:01 Yes.
**Tyler Yahn** 04:02 Yeah. Yeah.
Hey? Robert.
**Robert Pająk** 04:06 Hello!
**Tyler Yahn** 04:08 How you doing.
**Robert Pająk** 04:12 Don't ask this morning I have broken my teeth.
**Tyler Yahn** 04:19 Oh, oh!
Oh!
Oh! Sorry to hear that man that's.
**Robert Pająk** 04:23 Yeah, that's not yeah. It's just fun. But there were things that could could go worse always.
All right.
**Tyler Yahn** 04:33 Well, cool. Alright! We could probably jump in here if you haven't yet. Please go ahead and add your name to the attendees list. If you have agenda items that you want to talk about, please go ahead and add them here as well. There's not too much going on right now.
But yeah, we can get started. So yeah, I guess one of the things that I wanted to follow up on last week that I didn't get around to is also a canceled meeting last week, but just wanted to call out that this open telemetry specification for the stabilization of the declarative configuration. It was on me to get something together for an issue. I still haven't gotten it together. It's still in my queue. It is still in my queue. It's not dropped. So I just top of mind. I have been looking at it.
This is also related. One of the things we talk about is like instrumentation config and like support.
I think it became more relevant the Ebpf sake. Actually, we were talking about that as well like, that's something that we would want to try to support there. So like trying to do that with hotel Conf is like a good proof of concept. So there's probably more of that to come.
But the actual verification, and making sure that, like we actually have the parts that are going to be stabilized, implemented is, is still something I'm working on and creating an issue for you, David, but I haven't got around to it yet. So yeah, so yep.
**Robert Pająk** 05:50 I could have some time tomorrow. Do you want me to work on it? I just will need to know which parts of the config. SDK, because I think it's mostly about the config SDK and model right. The Api is not going stable. If I understood correctly, from some specification meeting.
**Tyler Yahn** 06:06 That's my understanding as well. And so essentially, it's just doing like an audit or building an issue for an audit. So finding what is going to be stabilized and finding what parts of our implementation exist, that work there and then, like the goal is to then, you know, do that audit, and David had said he wanted to take a look at it. But I'm I'm guessing if you have time. That would also work.
**Robert Pająk** 06:29 Yeah, I can. I can work on it.
**David Ashpole** 06:31 Wanted someone who hadn't like done too much with it before. Take a fresh look. So that's why I volunteered. But I'm happy to have help as well.
**Tyler Yahn** 06:44 Yeah, I mean, Robert, if you would like, cause I know that you've also been a big part of like the audit.
I'm sorry. The the review of Prs. But it's up to you.
I just would like somebody with new eyes to look at the specification and then also look at the implementation. I guess if you've already looked into implementation, it's not too critical.
It's more just about like seeing the specification and reading it without content.
**Robert Pająk** 07:07 Is so.
**Tyler Yahn** 07:08 Make sure that, like it's it's clear.
**Robert Pająk** 07:10 Yes. So when I was doing the Peer reviews, I was not very attached to the specification, because I was thinking more that we know it's a development stage. And we just need to, you know, build some stuff.
So I, even yesterday created a few, I think 2 issues or one issue. So yeah, I can follow up from there. And I can create issues for the specification compliance. Maybe I'll just also ask Jack explicitly what parts of the specifications are going to be stabilized because I'm sure it's defined. Or maybe it's in the Pr, I do. I will need to double check in this declarative. But yeah, I can work on this tomorrow.
starting tomorrow.
**Tyler Yahn** 07:51 Okay, yeah, perfect. I appreciate that. Cause it's in my queue. I won't get it to it tomorrow. Obviously, the declarative config would appreciate this. So yeah, that that'd be great.
Okay, cool moving on. Robert. You have an issue here in the specification repo.
**Robert Pająk** 08:10 So yeah, I think it's mostly almost a personal ask to. Basically, Tyler, David and Mattia, because I think you were the ones that were mostly implementing the metrics. SDK, today, I mean, certainly the Damien to basically check, because I think you were the ones who mostly implemented the metrics. SDK, when I, if I'm not mistaken from my reading, is basically okay, I think it's just kind of hard to implement it for us.
So that's the only the only reason I have not approved. It is because I failed to prototype in few hours. I just thought that it requires more changes in our data, types, etc, passing passing stuff more further to the pipeline. But maybe maybe I missed something, so I would just love to have David or Tyler, or Damien's eyes on it.
**Tyler Yahn** 09:04 No, I don't think you missed anything. I remember thinking about this and it being it's gonna be a little bit of a challenge to to plum this in. I don't think it's impossible.
but I haven't put a lot of thought effort into this yet.
I'm not exactly sure I understand the motivation either. So that's going to be the 1st step is kind of my my problem.
**Robert Pająk** 09:27 So the motivation. I'm not sure if it's explained the issue because I was talking with Lukash previously.
was, basically, he wanted to have some. The baggage processor also in the in the metrics, pipeline when he's basically adding synchronous measurements to add some information through the context and baggage, basically.
or some kind of it was it was a very kind of specific scenario not usual to normal application segmentation. Basically, he was doing some tooling for making load tests.
And basically, he was using observability just to get the insight on the test execution results getting metrics from low testing. So he was having different, basically baggages for different types of environments.
**Tyler Yahn** 10:27 I see.
**David Ashpole** 10:31 It feels like a very large concept for just supporting baggage.
**Tyler Yahn** 10:39 But yeah, I, that's my problem as well.
**David Ashpole** 10:43 This is a big hammer.
It's a cool like.
I feel like there could be other use cases for sure.
but I don't know how speculative that is right. Now.
**Tyler Yahn** 10:57 Yeah, I mean, like, the idea that you're like messing with the measurements is from a mathematics background. And like looking at statistics like this is just asking for trouble here that does not seem like an appropriate thing to be doing.
But The modification of attributes seems like the the main, ask for a lot of this and like around the baggage and things.
And so like.
Yeah, I'm kind of with David as well. Like, I just like this seems like a huge design change in like the metrics processing pipeline for maybe something that I don't know if it's as needed as this is making it out to be.
**Robert Pająk** 11:39 Yep.
**Damien Mathieu** 11:41 It's been a long time since I looked at this, but I feel like dropping individual measurements is something that could be interesting to some folks based on the questions that we often get, such as like folks using Hotel Http and not wanting some things, and or wanting some things without some attributes and views do not allow you to do that.
It's a question that we get rather.
**Tyler Yahn** 12:11 Yeah. But I mean, is that dropping measurements? Or do they want different partitioning of a telemetry stream?
**Damien Mathieu** 12:19 We? I mean, I've seen cases where they want to like drop a metric on 30, and also they want to drop attributes.
**Tyler Yahn** 12:28 Yeah, but that's what I'm saying. Like, you can already drop a metric right? Like that's that's something a view does.
**Damien Mathieu** 12:33 Yes, but not, and then you cannot drop an attribute.
**Tyler Yahn** 12:38 Yeah. But again, like that goes back to like the attributes, though right? So like, if you wanted to do like a reaggregation of attributes. Then that's I don't know. Like like Prometheus has a post processor down the chain, right like the collector can do something like this like
**Damien Mathieu** 12:56 The answer is, often folks saying, Yeah, but we don't use a collector, and to be fair, we don't force people to use the collector.
**Tyler Yahn** 13:07 Yeah.
And again, like that goes back to like the attributes. Question right? Like this again. Seems like something we could address. It doesn't require an entire processor. I still don't have a good understanding of why you would want to drop. Measurements like like metrics, are supposed to be a statistical sampling of of something right.
**David Ashpole** 13:26 We filtering out health checks, or something like I feel like this is.
**Tyler Yahn** 13:32 But that's like an instrument, though, right like that's that's a partitioning of a of an instrument.
**Robert Pająk** 13:36 Holy crap!
**Tyler Yahn** 13:41 Right? So like, if you have a health check for like a request coming in like, that's a route based thing it's not like it's not like cool. I got like 5 of the health check measurements like that sounds great. But the 6th one.
I think that this one is too long. So I want to drop this measurement like that. That doesn't make any sense to me.
**David Ashpole** 14:02 Right it. It's too powerful. I I feel like this. The use cases may be pretty similar to what like we had at 1 point talked about like making Labeler more generic or.
**Tyler Yahn** 14:12 Right.
**David Ashpole** 14:13 Like allowing people to stick span, start options in context.
like things like that feel like you could do something similar with this, because it's giving you a call back where you have access to the context and the final thing. And you can decide if you want to override stuff so like this would replace our labeler concept potentially.
**Tyler Yahn** 14:39 That makes sense.
Yeah, I mean again, like, I think it's like, it's it all has to come back to these attributes.
**Robert Pająk** 14:46 I think, yeah, I think the author was only concerned about adding attributes, if I remember correctly, and I think basically others were just finding. Yeah, there was this previous processor concept which was removed, revive it, etc. I think that that was how it landed.
or maybe he even found this concept previously and just thought that it's something similar, and maybe it will be the easiest after the donation.
**Tyler Yahn** 15:13 Yeah, that was the is the latter. That's how it came about.
But yeah, I don't know.
This is the most amount of time that I've really had to like Dedicate to talking about it. I don't. I don't plan on having a lot to talk about in in the next. You know I don't know. Maybe not the bandwidth to look at this.
If others are are willing to look at this, I don't know, like I'm skeptical of it to be honest. But yeah.
So I yeah, I don't know what to say. Like, I can look at this in weeks. But I'm not gonna be able to look at this in the next week.
**Robert Pająk** 15:54 I can try to say our feedback on the next specification meeting that, and maybe I'll also check the fix the issue, etc. If there are case, if there are real use cases for modifying measurements.
if this functionality is needed, if we just do not want the ability just to, you know, have the ability to modify the attributes.
**Tyler Yahn** 16:23 That seems reasonable.
And I think if that's the case that like, I don't know like, because kind of like what David said, like our concept of, like a labeler or something, there may be a different approach to try to solve this.
**Robert Pająk** 16:37 Yeah, this just seems like.
**Tyler Yahn** 16:39 A lot of yeah, a lot of a lot of.
**Robert Pająk** 16:44 Comer, foreign leap.
**Tyler Yahn** 16:46 Yeah, exactly.
Okay. Yeah.
All right, Robert, you also wanted to ask about this pull request in the go repo.
**Robert Pająk** 16:55 Yeah, basically, I want to put your eyes, because if anyone doesn't like it, I would like to have you know I do not want to propose anything in the contributing guidelines that someone will disagree. So this is just proposing to add the code Re code review, go, code, review comments from the go team which I personally use very often when I'm doing code reviews. And I'm when I'm basically saying that I do not like something or to change something. It helps me a lot, and I think that maybe putting in your country Pmd, maybe may be easier if someone reads it, or at least I could reference it with more confidence that at least we mentioned contributing Md.
And because this also mentions the Go test, I also added this one line just that we are low because additional comments related to testing can be found. Blah blah is in the Code Review comments which you were opened. I just added also this kind of one line that we are okay.
This is on your screen right now in the middle go test comments additional comments rating to testing can be found in go test comments. It's it's in the header paragraph. Yeah.
**Tyler Yahn** 18:07 Here, okay. Yeah.
**Robert Pająk** 18:07 So because of it. I also added this one line that we are okay using testify.
**Tyler Yahn** 18:17 So alright! This is bringing in this document as well, is what you're saying.
**Robert Pająk** 18:21 I will. Yeah, I would say that someone can interpret it because it's it's written that additional comments related to testing can be found here. So I just wanted to play safe and also explicitly say, just in case that we are all in testify.
**Tyler Yahn** 18:37 Yeah, I mean, there's also, like Google has published a longer ghost style guide like, I don't think that implies that this is. This is no, sir, style guide. So that's true.
**Robert Pająk** 18:45 If it's needed. But I think that we can say explicitly that we are okay using testify. I don't think it's bad to put it or do.
**Tyler Yahn** 18:52 I'm not disagreeing at all. No, I think that that sounds good.
I do wonder if we should include it in Api still, but that's that's maybe another discussion.
**Robert Pająk** 19:04 Yeah.
**Tyler Yahn** 19:06 So yeah, so I there's a lot that comes in in here as well.
I guess I guess I've looked through this a few times. But you're asking if we can read this thing and make sure that we're okay with the whole thing.
**Robert Pająk** 19:21 Mostly about the pre about this one. Yeah, correct.
**Tyler Yahn** 19:31 Much of this is covered by our linters.
**Robert Pająk** 19:35 I would say about guessing a half like you know the initialisms, etc, if the linters can find some of them. But, for instance, there are some things related to the design, like how interfaces should be used.
etc. This kind of things are, you know, something which linters cannot create. It's more about, you know, designing stuff about receiver types that you should use them consistently.
I think it's also listed here. I think. There, we do not have a linker for it.
But I know that this is usual, our practice, that we are often asking, you know, to use consistently the same receiver type when you're having a strike. So I I do not think there's anything controversial here.
**Tyler Yahn** 20:24 I see I don't either. I just get worried about the frustration that this kind of includes.
But that's maybe something we can work on.
**Robert Pająk** 20:40 Because I think I've looked at this before. This seems like we've something we've already reviewed right
**Tyler Yahn** 20:48 Yep, okay.
Any other comments on this.
**Robert Pająk** 20:56 Nope.
**David Ashpole** 20:57 I'm I'll just say, like, Google obviously uses this all the time. So it's there's nothing radical for me.
**Tyler Yahn** 21:07 Yeah, I don't think there's like like I said, like I've looked through this.
I probably referenced it multiple times, but I just don't know what it contains. Does it change at all?
**Robert Pająk** 21:18 Almost not.
**Tyler Yahn** 21:21 That's almost.
**Robert Pająk** 21:23 Was almost some typos. You.
**Tyler Yahn** 21:26 Oh, okay, alright.
Yeah. Okay.
Sure. I mean, I just like, I think that if this is going to be something we adopt like. We probably want to dedicate some time for each Maintainer to understand it right, because this is something that you're going to need to reinforce.
**Robert Pająk** 21:41 Think this synchronous. I think crypto run, and synchronous functions may be the new things, if I remember correctly.
**Tyler Yahn** 21:48 Okay.
**Robert Pająk** 21:48 I do not remember them, but these are, you know, things which are added. For instance, we know.
and they just added.
**Tyler Yahn** 21:56 I see.
Oh, it's like Wiki. So it's in here is where the repo is for this. Okay.
**Robert Pająk** 22:07 Yep.
**Tyler Yahn** 22:09 Interesting. Cool, all right. Yeah, I've been. It's I've read through this like twice now. Well, I've started to read through it twice. I just haven't gone through the whole thing yet. So yeah, it's on my list. I mean, I think that the testify things that was great.
Yeah.
Cool anything else on that one, Robert.
**Robert Pająk** 22:35 No.
**Tyler Yahn** 22:36 All the other maintainers. Who else has reviewed that already?
I think David.
**Damien Mathieu** 22:43 I have, and David has.
I read the document, but I've not thoroughly gone through it.
**Tyler Yahn** 22:53 Yeah, I mean, I that sounds good. I'll I'll read through it.
Well, cool, all right. That's the end of the agenda.
I can stop sharing my screen here. Any other topics people want to talk about.
**Robert Pająk** 23:05 I have just a question. Do you want to maybe go for the mice, the our goals yearly goals, if we want just to have some quick check.
**Tyler Yahn** 23:13 Yeah, thank you. That was something I wanted to add, I totally forgot.
Yeah. Robert and I were talking about this yesterday, so I totally spaced, adding this, let's see, yeah. So we were talking about it because we're also like, we're past the halfway point in the year. And we're making slow progress on some of these. So wanted to check in and see if we can maybe identify anything that we can help move along here so SDK self observability signals. David, this is something that you had been working on. I think there's a Pr. There's definitely a lot of work on here. You want to give us an update on this one.
**David Ashpole** 23:54 Haven't haven't gotten back to it. I probably won't be able to pick it up before I go on leave again, and my leave is kind of thrown a wrench into this. So I was.
**Tyler Yahn** 24:02 Oh, are you? When are you going back on leave? Sorry I didn't.
**David Ashpole** 24:05 In 2 weeks, so.
**Tyler Yahn** 24:09 Are are you going on for like another 9 months, or something like that? Or I'm sorry, like 3 months.
**David Ashpole** 24:14 Another month.
**Tyler Yahn** 24:14 Another month. Okay.
**David Ashpole** 24:17 But I so that means I'll probably maybe have something on this by like end of September.
Ish.
**Tyler Yahn** 24:27 Yeah, I mean, that sounds that sounds good.
What is there? Something that you can? Can you hand this off.
**David Ashpole** 24:36 I suppose it's a.
It's basically like there's a bunch of metrics defined. And we just need to figure out how to implement them. I. The only thing I remember is that because users end up creating a lot of like, I'd imagine that there would be one like with meter provider option that would be passed so that everything could like. So that configuration and setup would be really simple if you wanted to provide a different meter provider, but like actually, because everyone because you create your own processors and because you create like.
I forget what the other pieces are that end up being instrument, but the like. The Batch processor and the simple span processor get instrumented. And there's some other components. I think the exporters.
like, I think the setup code ends up being kind of ugly. So I'm not. I wasn't sure what to do about that. The initial stage should be pretty easy, because it's just We'll just use globals and gate it behind one of our feature gates, although we'll have to copy that feature gate into like 6 packages.
But it's not a big deal.
**Tyler Yahn** 25:50 Okay.
but that's just to get like, the essentially the beta started. And then we'll use like an environment variable to gate. It is what you're saying.
**David Ashpole** 25:59 Yeah, yeah, and just use the global when that environment variables turned on that. Like, that's the point I'm trying to get to next.
**Tyler Yahn** 26:06 Okay, did. Did. Am I like misremembering, or did you have a Pr open for this.
**David Ashpole** 26:12 I did. I think it was just the batch span processor one.
and I don't remember what I what problem I ran into.
**Tyler Yahn** 26:25 Okay, okay, so there is. There is, is this linked?
See?
Just make sure it's linked here.
Cool. Alright. So I think that sounds like a I mean, that sounds like a great starting point. Actually, it sounds like you're much further than you gave me yourself credit for in my mind? So I think this is actually something. Maybe we could try to like.
get over the line. Would you be okay if somebody just took this branch, and like started working from it to try to like get it over the line. Then.
**David Ashpole** 27:04 Yeah, I I don't remember why.
Why I abandoned this or what?
yeah, I I don't remember what the current status is.
**Tyler Yahn** 27:15 Yeah.
**David Ashpole** 27:16 That's okay.
**Tyler Yahn** 27:16 Yeah, I mean, that's obviously.
**David Ashpole** 27:17 Work in progress, or something.
**Tyler Yahn** 27:21 Yeah, it's right? Yeah. So I mean, I think I think it's just requires some audit here. But I think you've done a lot of great work. So I just want to like keep it going. I think it probably also coincided right when you left. So then, just picking it up. Probably got dropped, I think, is probably the only thing.
**David Ashpole** 27:37 Yeah.
**Tyler Yahn** 27:38 Yeah.
Okay. Well, if that's the case, then we could try to prioritize this.
I think a good way to try to prioritize. This is maybe just add this to the milestone.
so we don't lose track of it. I don't think we're gonna get it done in this milestone, but I do think that we can make some.
**Robert Pająk** 27:58 The words on it.
Do we have, David? Some sub issues that maybe if we put some help wanted, etcetera. Do you think it will help, or you think that we will just consume more time for us to review stuff and work.
**David Ashpole** 28:11 Yeah, I think it would help.
I think it would help, especially if we want to split up work, because we should probably implement this one like cause. There's processor. There's SDK metrics, and there's exporter metrics. If I remember correctly. So we should have an issue for each one.
I assume the exporter. One will be scoped to just the Otlp exporters, not like standard out, or whatever. Maybe so.
**Robert Pająk** 28:41 I guess I guess if we have one Pr. Which could be as a reference, then other even newcomers probably would be able to implement others? Or do you think, do you think it makes sense or not? Really.
**David Ashpole** 28:54 For yours.
**Robert Pająk** 28:56 Yes, I think, for if you have, you know, for processors, or for whatever I think, this stuff for the exporters have similar design or not.
**David Ashpole** 29:04 Expanded in flight. Yeah, right. I think I consider this succeeded. When the Otlp exporters have this metric.
**Tyler Yahn** 29:18 I mean, I think that's a great place to start, at least right like maybe we want to add it to the Jaeger one. But I don't think we want to do that right off the bat right like I think this is a good place to just start with the Otlp.
And so like, because we also have multiple otlp exporters right like. So there's I think there's like 9 or sorry that'd be 6 exporters right there. Right? So like I mean, there's already.
**Robert Pająk** 29:41 Are experimental, which.
**David Ashpole** 29:43 This is only for the trace. SDK, right.
**Tyler Yahn** 29:48 Okay.
**David Ashpole** 29:50 All span ones, so that the initial scope of these, obviously like copy paste, will probably have similar ones for metrics and logs.
But the initial scope is just for the trace SDK.
**Tyler Yahn** 30:04 Yeah, okay, So I try to keep some notes here. So we have the this is like the the tracer, then then the processor. So this is going to be the batch span processor and the simple processor right.
**David Ashpole** 30:23 Yep, although the simple span one is maybe less useful, but we should still do it.
**Tyler Yahn** 30:43 Okay, so yeah.
I think that sounds good.
Oh, I meant to add that this is, yeah, whatever let's just go. I think it's captured there.
yeah, okay, I mean, that sounds like something we could start to work on. I think at this. Your Pr is just for this batch processor. Right? Yeah.
**David Ashpole** 31:25 Yes, I may have done the simple span one here, too.
No, it looks like just the batch processor. Yep, okay, okay.
So we could split it up into batch versus simple. In terms of like issues.
**Tyler Yahn** 31:59 Okay, yeah, I think if that sounds like a good idea, I mean, I think having something like this, I mean, all the foundation is actually the semantic convention work. This is just implementation. So that sounds good.
Okay, cool. Thanks for the update on that one. The go runtime metric stabilization is also something that is in your wheelhouse.
**David Ashpole** 32:19 Has been flipped on by default. So, and Josh Mcdonald also had one additional. There's a few metrics that we that would be nice to add.
to make disabled by default. But let people enabled enable I opened an issue at 1 point about allowing us, or allowing instrumentation to specify a default.
**Tyler Yahn** 32:46 One time.
**David Ashpole** 32:47 Or something like basically support disabled by default metrics. I don't know if you remember that discussion.
**Tyler Yahn** 32:54 Yeah, yeah, with like advice or something like that. Right?
**David Ashpole** 32:58 Yeah, right? Right? But I don't have time to pursue that. So I think the best thing we could do is probably just add some optional ones to the semantic conventions, and add like options to the package.
**Tyler Yahn** 33:12 Oh, I see what you're saying. Okay.
where? Where? Where? Where's where are those missing metrics?
**David Ashpole** 33:18 Missing runtime metrics.
This was the like long discussion with someone.
**Tyler Yahn** 33:27 Okay.
**David Ashpole** 33:30 And then I think we came up with.
yeah, so 2 opt-in metrics.
Gc, pause and released memory.
Yeah. So I I don't think we should block on that. Maybe it's.
**Tyler Yahn** 33:55 Yeah, I think you're right. I think I think the only way it happens is, if, like.
**David Ashpole** 33:59 Somebody that does a lot of spec work drives it, and seems like everyone's busy these days.
**Tyler Yahn** 34:07 Yeah, I think this is a great addition.
But I also think that, like for defining done for this, like, I don't think this is required, like these optional metrics, to be honest like, I think these can be added to a stable package right.
**David Ashpole** 34:21 Yes, they could be and Josh Mcdonald also has a metric he's interested in adding,
**Tyler Yahn** 34:29 Okay, go provides a CPU usage metric, which is.
**David Ashpole** 34:34 Apparently an overestimate of CPU usage. So it's not exactly accurate, but it lets you split between CPU usage of, like the of various different things.
**Tyler Yahn** 34:48 Hmm, okay, so is, is it just like we need to partition it more, or we need to not use it like what was his. Ask.
**David Ashpole** 34:59 A new metric.
**Tyler Yahn** 35:01 It's a new metric. Okay?
**David Ashpole** 35:03 Yeah, it would be a new metric. Let me let me link that.
**Tyler Yahn** 35:11 That's weird.
Rename, or remove the runtime. No, this is definitely not. It.
**David Ashpole** 35:27 Okay.
**Robert Pająk** 35:30 Not sure if it was not mentioned in his draft. Pr.
**Tyler Yahn** 35:35 Oh, okay.
**David Ashpole** 35:39 Okay, I linked the the comment from the meeting notes.
But yeah, I also agree. It's probably not a blocker. But we we just bumped it to enabled by default. So hopefully, we'll get a lot of feedback or issues if people are very upset by the new metrics.
**Tyler Yahn** 36:11 Oh, okay.
**Robert Pająk** 36:13 At the Runtime.
**Tyler Yahn** 36:16 Yeah.
okay, well, that's yeah. So this. So this is included by default. Then in our current implementation, or this is something that's going to be included in the the go space, and we're going to start adding it.
**David Ashpole** 36:38 Completely unclear! This is.
**Tyler Yahn** 36:40 Okay.
**David Ashpole** 36:41 I haven't looked into it. I asked if you scroll up to my comment like.
**Tyler Yahn** 36:45 Yeah.
**David Ashpole** 36:46 Is it useful?
Like, basically like did trying to figure figure out if this is just like Josh really likes this metric for some reason, or if it's like something the Go team thinks is generically useful to most users.
**Tyler Yahn** 37:08 That's a good question. That's a really good question.
I mean, CPU, time is already an estimate like, but yeah, okay.
**David Ashpole** 37:18 Yeah, I guess.
**Tyler Yahn** 37:20 Yeah.
okay, well, we've got it documented. I think if that's helpful in understanding our our progress here, I think this is also something that.
I think, yeah, I think it's just about the stabilization of this. So it's more about just auditing what we have and and maybe going through and finding out. If, like what we have can be expanded. What we have is compliant does this, I'm guessing. This also requires the stabilization of the semantic conventions, though prior before prior to us. Releasing this, though right.
**David Ashpole** 37:48 Yep, I think stabilization. Yeah. So I, yeah.
But it's kind of just up to us. Right? We will roll these out by default and see if we get any feedback, and then.
if feedback seems mostly positive and and we give it some time, then I think we just remove the old implementation and stabilize the conventions and go from there.
**Tyler Yahn** 38:17 And the current state is that the new stuff is defaulted on right.
**David Ashpole** 38:21 Yes, and the old stuff is defaulted off.
Yeah. Okay? And then how long?
Like a week or 2? Right?
**Tyler Yahn** 38:28 2 weeks ago. Yeah, okay. And so we're looking, maybe for like a 3 month window here. So essentially, when you get back.
**David Ashpole** 38:35 Sure. Yeah, we can do it like October or something.
**Tyler Yahn** 38:38 Yeah, okay, maybe. Just add this, here.
**David Ashpole** 39:08 Oh! Another interesting call out, was, we once.
once these are stable, we should recommend that the collector adopt them.
**Tyler Yahn** 39:20 Oh, okay.
**David Ashpole** 39:23 It was brought up at the collector's egg, and people were surprised that they existed.
**Tyler Yahn** 39:28 Wait. Really.
Okay. Well, hmm.
**David Ashpole** 39:35 Like, oh, this is really cool.
**Tyler Yahn** 39:36 That's.
**David Ashpole** 39:37 Tell us about the cool stuff you do.
**Tyler Yahn** 39:39 Yeah, that's not great. I wish we were better communicating. But we'll work on that.
Okay, next up is log stability, stabilization. Robert, you want to give us an update on this.
**Robert Pająk** 39:52 Yeah. But even from this view, yeah, we can go for go 1st here.
So there are some in progress, new in progress stuff, but these are just low hanging fruits. The big still, the biggest one, is the blocker on the specification and complex attributes. But I think we can go Tyler, to the previous window and just focus on the high level.
and we can remove the 1st 2 blockers. The event signal is done at the spec level. The enabled is.
Yeah, we can cross it out or remove whatever the 1st 2 blockers.
**Tyler Yahn** 40:33 Double, or once.
**David Ashpole** 40:35 Oh!
**Robert Pająk** 40:36 That's a good.
**Tyler Yahn** 40:38 Adding enabled at the spec level. Okay?
**Robert Pająk** 40:40 Yes, like, it's being released right now. This is the release notes that in the upcoming release.
And this one.
And this last one, yeah, is a can of worms right?
**Tyler Yahn** 40:53 Indeed it is.
Yeah.
yeah, okay. I mean, we're working on it. I, I think if there's still obviously like, if you're not aware on this call. Or if you're gonna read this afterwards, like there's the Otep for extended complex attributes. Looks like it's progressing. Lunall is trying to shepherd that through after the Otep is there. They're looking at implementations. We have a proof of concept in. Go to support this. It'll require changes to the logs. Api. Something that Robert's already prototyped like this looks pretty straightforward. It's just it's all dependent on the spec work which needs to then get stabilized after the fact. So if you have opposition that you don't want the complex attributes, please go, voice, that if you have support for the complex attributes, please go, voice that the only state that we don't want to be in is the one we're in now where there's indecision. So yeah, I think, having a decision from Otel is the only thing that's blocking this. So yeah, you can help that by voicing your opinion.
**Robert Pająk** 41:55 David, I have. I have also a question because I was not involved in almost none any of the before.
If the auto is merged. Does it mean that it's already, like, you know, accepted or just pre accepted design.
**Tyler Yahn** 42:12 Accepted.
**Robert Pająk** 42:13 That's what I feared so.
**Tyler Yahn** 42:14 Welcome to the value of Oteps.
**David Ashpole** 42:20 I think it.
It's accepted in principle is what I would call it.
**Tyler Yahn** 42:27 Yeah, I agree. So I think, I think it's kind of like here, how we have this policy where you need to pull request reviews, and you need 24 h right like to to get a pull request merged. I think the Otep is kind of like. You know us, saying, It's it's it's a pre discussed issue. So if we have a lot of discussion on this, I think that immediately from the Otep you can start adding it to the specification, and then the path to stabilization should be much quicker.
So I do think that's that's the benefit of the Otep. I think it provides an onboarding path for new features to be accelerated.
I think this is a controversial one, so I don't know if that's gonna happen. But.
**Robert Pająk** 43:05 Yes, so my only question is, I haven't. I have never seen such thing when a note was accepted. So if it's a possible that you know, division and ideas, the strategy, or whatever I would say, the high level design will be later, you know, said, Oh, I disagree. I changed my mind.
**Tyler Yahn** 43:24 I think that a good example that's recent is the events signal that once you got, the Otep accepted, you started seeing changes in the spec to reflect that pretty quick, and I think that has to do, maybe, with the people who are involved in the Otep also, not getting burnt out in the process. And I think the same people are involved in this complex attributes. Otep. Cool.
It's speculative, but I don't think that that's gonna be the case.
**Robert Pająk** 43:47 Low risk.
I see that's a lot.
**Tyler Yahn** 43:49 Well, it's yeah, lower than normal. I don't think that there's a low risk. But yes.
**David Ashpole** 43:58 I see.
**Tyler Yahn** 44:01 Okay, next up is the Hotel Http stabilization project. So this is still something 2025. We're working on.
yeah. Is Damien, still on the call. Sorry on my zoom.
**Damien Mathieu** 44:14 Yes, science on the call.
Yes, I'm sure.
So for the same configuration, basically, we're waiting because we have to wait, I think it's 6 months before. We can remove the old version and then we can get rid of SIM and everything.
So it's kind of in a state of limbo, just waiting for the vaccine configuration. I don't know if we could say that we.
**Robert Pająk** 44:43 That that we need to wait 6 months. It was our own policy.
**Damien Mathieu** 44:48 It's the semantic conventions. Ask.
**Robert Pająk** 44:52 Yeah, we we abandoned that a while ago, though.
Yeah.
**Tyler Yahn** 44:56 That was the ask back in 2023, I think that was the ask when it initially came out, and we've gone through and revised that a few times, and we've changed it to just being released, based on our end.
And we proposed it up as well to the spec meeting, and they've there was 0 opposition to us, deciding a different path.
**Damien Mathieu** 45:15 How many how many releases.
**Tyler Yahn** 45:18 Well, last we talked about it. It was well, I thought we wanted 2, but I think that I mean I've always just wanted one, so I have no.
**Damien Mathieu** 45:28 I mean, we've had 2 already. So if it's whether it's 1 or 2 matters not, if it's more than 2 we need to wait. But yeah.
**Tyler Yahn** 45:36 So let's see if we can find this issue.
yeah, I mean, I think it was just gosh, there's so much here.
Oh.
yeah, I don't. I don't know. I don't know where it is.
but yes, I think if it's 2 like, and by 2 you mean that like the default is, the new Http. Semantic conventions are are defaulted right now. We've had that for 2 releases.
You're muted.
**Damien Mathieu** 46:17 Yes, the default conventions are defaulted. So I just pasted 70 conventions for migrations of Http in the zoom chats. And that does still mention 6 months in this symmetric conventions, repository.
**Tyler Yahn** 46:39 Yeah. But like, I said, though, like, that's something that was initially there, I think the 6 months was really critical when they started breaking things.
and we've had a lot of talk with the semantic conventions group since then, and the semantic conventions have been long stabilized past 6 months, and so they they wanted that stability going forward for implementations. During that timeframe.
We have an issue. Let's see if we can find it here.
might actually be a specification issue?
Maybe not.
Yeah.
Oh, my God.
yeah. So I think this, is it so?
**Robert Pająk** 47:52 I think the the thing was also that the semantic conventions were assuming that the instrumentation are stable. That's why it says about major versions, if I remember correctly.
**Tyler Yahn** 48:03 It? It does. Yeah. And that was a big part.
That was also why, like.
**David Ashpole** 48:08 People like Python don't even do this migration.
**Tyler Yahn** 48:12 Because they don't have a stable release. And this is why it was controversial since the beginning, because I don't know if we should have been doing this.
Yeah, like.
**Damien Mathieu** 48:20 I mean, I'm fine removing the old version. I just figured we had to wait. But yeah, I can do that next week.
**Tyler Yahn** 48:31 Okay, yeah, I'm if I have very low appetite for trying to hold on to something that's not stable, especially if they can just use the old version of contrib and provide the the feature that they want.
I'm I'm happy to move forward, or, as they they say in the industry fall forward.
So yeah, I think if that sounds, I would prefer we do something like that and move this to some sort of closed, because there's a lot of cleanup tasks as well that follow up to this right like there's a lot of cleanup tasks. So I think I think the sooner we could do that the better. And I think getting this stage for the next release sounds like a great idea. So yeah.
**Damien Mathieu** 49:15 Okay? So I will be doing that. The start of that cleanup next week, removing simcom.
**Tyler Yahn** 49:35 Awesome.
Okay, file based configuration this is kind of what we started off on. So at this point, like, we obviously need to work on our implementations. But the 1st step is also to looking at, making sure that we're compliant with the stabilization.
which is something that Robert's going to be working on tomorrow. So I guess that's kind of the update. It depends on the stabilization. So yeah, we're in this process.
**Robert Pająk** 50:01 The biggest part from the implementation specific from the implementation is that we do not have this register. Component provider functionality.
**Tyler Yahn** 50:13 Yeah.
**Robert Pająk** 50:13 This is.
**Tyler Yahn** 50:14 We have an issue tracking that, too. So.
**Robert Pająk** 50:17 That it's unless I have not created a duplicate.
**Tyler Yahn** 50:23 You might have. But that's it's it's captured, I think, is the important part.
Okay?
yeah, all right. So that's all of our yearly goals here. Yes, okay. I've seen that. Thanks for bringing that up, Robert. So at that point, I think that's something we can pause on any other topics people want to talk about for the rest of the meeting.
See if there's anything added to the agenda. Nope, not there.
**Damien Mathieu** 50:52 I just noticed that I have the same shirt as Robert.
**Robert Pająk** 50:58 Curious? Why.
**Tyler Yahn** 51:02 The.
**Robert Pająk** 51:02 Colleagues.
**Tyler Yahn** 51:04 Does the back say? Git clone.
**Robert Pająk** 51:07 I think it's from traffic right? If I remember, it's it's traffic labs.
**Tyler Yahn** 51:11 Yeah.
**Damien Mathieu** 51:12 We? Yeah, we we actually got it together at coupon. So.
**Tyler Yahn** 51:18 That's pretty great.
Well, okay, yeah. So please make sure to send out the email for next week's dress code, and we'll all show up with the same shirt then, but otherwise. Yeah, we could probably end this meeting here. All right. Well, thanks everyone for joining. Appreciate all the hard work. Still a lot to do. Yeah, I'll see you all in weeks, time, or asynchronously, bye.
