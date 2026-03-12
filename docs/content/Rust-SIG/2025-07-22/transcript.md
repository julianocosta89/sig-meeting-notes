SIG: Rust SIG
Date: 2025-07-22
Duration: 47 minutes
Zoom Recording URL: https://zoom.us/rec/share/VQRFLYrjtj-AT9B9PAXb5UBWdYqENUo_2jwLrojudhqUIWot0IT3cHfuzipSMSg5.gjC56AGxf3RbzSQU
============================================================

## Zoom Recording Transcript

**Scott Gerring** 00:47 Hey? How's it going.
**Cijo Thomas (Microsoft)** 00:49 Good! How are you?
**Scott Gerring** 00:51 A bit tired, but otherwise well.
**Cijo Thomas (Microsoft)** 00:54 Okay. Let me share my screen.
Yeah, I'm not sure if anyone else would be joining.
**Scott Gerring** 01:24 I know Bjona's on holidays at the moment.
**Cijo Thomas (Microsoft)** 01:27 Oh, yeah. Okay.
**Scott Gerring** 01:28 Which is a bit of a bummer, because I would still like to see an end to the tracing issue.
**Cijo Thomas (Microsoft)** 01:34 Yeah, yeah.
Okay, let's maybe wait one more minute and then just go over few open issues and release milestone.
**Scott Gerring** 01:46 Yeah, we can. We could talk about the Otlp thing a little bit between ourselves, if interested.
So I.
**Cijo Thomas (Microsoft)** 02:00 Yeah, I think let's start like we. If there was someone rejoining, they would have joined.
**Scott Gerring** 02:06 Yeah, I mean, with the Otlp thing. We're probably the only 2 people that are particularly interested at the moment. I think.
**Cijo Thomas (Microsoft)** 02:12 Think Ladith was looking at it like at some point, but then he got so busy with other work stream so I'm hoping that he will also be helping as and when he gets some free free cycles.
**Scott Gerring** 02:26 Cool.
Yeah. So I think I think those ones at the top. I I agree with you with the severity number. I think there's no easy way of adding.
sorry. Go down a little bit.
**Cijo Thomas (Microsoft)** 02:38 Oh, yeah, I did see that I was just looking at it like this, before.
**Scott Gerring** 02:43 So I think the the retry info retry after compression and partial success of the big ones that are missing. From what I can say.
**Cijo Thomas (Microsoft)** 02:53 Yeah, that would be.
Do you know, if the libraries have any built in way, like either tonic or request has any.
**Scott Gerring** 03:03 Nice.
**Cijo Thomas (Microsoft)** 03:04 Doing it, or.
**Scott Gerring** 03:05 Certainly hope so, but I haven't had a look in detail yet, but I will.
I guess my idea is that once you guys, or you in particular, I think, have a look and say, like, Yeah, this seems roughly accurate.
Then I would create tickets for each of the things underneath, and see how we can do them.
**Cijo Thomas (Microsoft)** 03:23 Yeah.
**Scott Gerring** 03:24 So in Java, for instance, the the retry is handled by the Java client. I saw that at least it would be nice if we could get the same thing for at least some of our clients here.
**Cijo Thomas (Microsoft)** 03:33 Yeah, this is must. So we need.
**Scott Gerring** 03:36 Yeah.
**Cijo Thomas (Microsoft)** 03:37 Okay.
There was an old Pr from.
**Scott Gerring** 03:42 Oh, yeah.
**Cijo Thomas (Microsoft)** 03:43 Yeah, is like, now, quite stale to handle like retries, yeah, this one.
Let me see.
**Scott Gerring** 03:54 7, 2, 7, 2, 7, 2, 7.
**Cijo Thomas (Microsoft)** 03:57 Yeah, let me see, what's the latest? Yeah, this was 4 months ago. Yeah.
**Scott Gerring** 04:02 Yep.
**Cijo Thomas (Microsoft)** 04:03 Okay, yeah, this is so only attempt. I believe they're required, like some refactoring.
Yeah, I'll share the link here, like, when we actually try to work on it. We should be able to like. See if we can steal something from here.
**Scott Gerring** 04:19 Yeah, for sure. I that's that's a good start, at least.
Yeah, cause it. It feels like you could imagine pretty easily that you, you would end up with one of the clients supporting Retry, but not all of them, and then it becomes kind of a more abstract concern. I suppose.
**Cijo Thomas (Microsoft)** 04:35 Yeah, yeah, I was hoping that the the libraries which we use they have built in support. But it looks like it's not there. That's why we are wrapping it, and we are doing it by hand.
**Scott Gerring** 04:47 Yeah.
**Cijo Thomas (Microsoft)** 04:49 That's cool.
**Scott Gerring** 04:50 That's good. I think I I'll I'll add it quickly to here.
2, 7. 0, there's actually already a link to it in the book a bit further up Gzip and Z. Standard. I can't imagine that's going to be very hard. I think that's just going to be a feature flag, and then an option on the clients themselves. But again, I haven't looked in any detail.
**Cijo Thomas (Microsoft)** 05:12 What? One second?
Yeah, I was just closing my windows. It's too much outside today.
**Scott Gerring** 05:22 No worries.
Yeah. So I think 3 shouldn't be too hard. I don't know if anyone's tried that before, but it feels like it's just going to be a matter of toggling the right flags on when the user asks for it.
**Cijo Thomas (Microsoft)** 05:32 It. It's only for Http for Grpc. We do have it already.
**Scott Gerring** 05:37 Yeah, I think it's only the Http like non-grpc clients that don't 4 feels like it's probably going to be a bit hard.
There's like. There's also partial retry responses where I gather, depending on the thing you're exporting. You have to retry a subset of it that feels like it's going to be a pain.
but again, I haven't looked at it in any detail yet.
**Cijo Thomas (Microsoft)** 05:59 Yeah, partial part of the data. The server must be the same.
Yeah.
**Scott Gerring** 06:06 So I think we have the. We have the messages already generated for that. But we're just not doing anything with it.
**Cijo Thomas (Microsoft)** 06:14 Yeah, this looks non-trivial. Yeah.
**Scott Gerring** 06:17 Yeah.
**Cijo Thomas (Microsoft)** 06:18 Anytime we have to like, unpack the payload.
do something based on it. Then that's that's not trivial.
It.
**Scott Gerring** 06:27 Yeah, it's gonna be fun. It might be even one where it's worth doing a bit of a design proposal firsthand in the issue that spins off from it. I think.
**Cijo Thomas (Microsoft)** 06:34 Yeah, okay. And it would work.
**Scott Gerring** 06:38 One there is interesting. I saw that you've you've had a ticket before on the.net.
**Cijo Thomas (Microsoft)** 06:44 Repository, but it's really old.
No, daughter does not send concurrently, I know, for sure we don't send it.
**Scott Gerring** 06:53 That's why I looked there, because I thought you'd probably have an opinion about it.
**Cijo Thomas (Microsoft)** 06:55 Not really a this won't be like something we. We will solve in the exporter, because as of now.
the batch, span processor and batch log record processor. They limit concurrency. They only have, like one one export call at any given point in time. It's for that to complete before it triggers another one.
**Scott Gerring** 07:19 Yeah, so we don't need it for the moment. Then the next one is a bit gnarly. The enum ambiguity.
basically like you can ask for things in a certain combination that don't make sense, and something else will happen.
**Cijo Thomas (Microsoft)** 07:37 Okay, okay, with, then to select encoding, which is protocol.
Okay, get it. Yeah. I mean, we still have opportunity to like, rename it to like.
**Scott Gerring** 07:57 Encoding, maybe, or something. But yeah, I think it's it's just kind of like the 2 things are conflated like the with Http with Grpc. Which is more protocol, but it also kind of mixes down to this layer of protocol as well, and then with the feature flags as well.
**Cijo Thomas (Microsoft)** 08:17 Yeah, this is so here, like the user would start with which with Http, and then, if they want like Json, then they will specify like with protocol. Http. Json.
**Scott Gerring** 08:27 Yeah, but they could also say with Http grpc, for instance.
But then that will be an invalid one.
But that that treat. I think it treats that as protobuf. So then it's if you called the enum the second enum format or encoding or something, then it would be protobar. Http.
boy. Yeah, yeah, it's a bit of a mess, but I don't think it's going to be super hard to fix. We just have to think a little bit.
**Cijo Thomas (Microsoft)** 08:53 Yeah, even though, like, we mark like otlps, release candidate. I think if we can support like obvious improvements, let's accept the breaking change cost, and do it rather than like leaving with the confusing thing forever.
**Scott Gerring** 09:10 Yeah, I'll for for each of the ones that seem like they matter. I'll make sub issues and write a little proposal for them, and then we can be a bit more detail oriented about it.
**Cijo Thomas (Microsoft)** 09:22 Yeah. Looks like you already. Did that study already. So that's very good.
**Scott Gerring** 09:26 Yeah, sort of roughly, I like to convince myself that I found something by writing it down before speaking about it.
**Cijo Thomas (Microsoft)** 09:33 Yep. Yep.
**Scott Gerring** 09:35 Hey, Lalitt, by the way.
**Cijo Thomas (Microsoft)** 09:37 Yeah.
**lalit** 09:38 Hi, guys, I'm just driving on the way. So I'd be mostly listening.
**Cijo Thomas (Microsoft)** 09:42 Okay, no worries, no worries.
You.
**Scott Gerring** 09:45 And then I found this compliance matrix. So I just went quickly through and checked some of them. And some of the things we're doing now, which is cool, so we can go back and pr that and fix them up.
**Cijo Thomas (Microsoft)** 09:57 Yeah, I mean, some of things like don't make sense in our current implementation. Like, for example, like, we don't have anything to flush in the exporter itself, like we don't. I mean, if we had like multiple requests in flight, or like queuing up of request, then it would make sense. But yeah.
**Scott Gerring** 10:20 Because it's a synchronous thing driven by the layer above.
**Cijo Thomas (Microsoft)** 10:23 Some things don't make sense. So we can like, maybe market as not applicable or something.
Okay, yeah, it's schema urls partial where we temporality preference. Okay?
Interesting. Yeah. Okay, aggregation sector is missing.
Yeah. But this is another weird area like this should be more like SDK or reader things not really an exporter thing but unfortunately.
**Scott Gerring** 11:00 Yeah, I mean, in this case, I've just popped it out of that document. But I mean, if we decide that we don't want to do it as part of Otlp.
**Cijo Thomas (Microsoft)** 11:06 Yeah, I think we did expose it like some already. So it may be very hard to remove it.
Yeah, with temporality is exposed in the exporter which is read by the metric reader to influence the temporality decisions. It feels a bit weird because exporter shouldn't be in this business. But anyway, like this, since the spec already right side, we just follow it. Yeah.
**Scott Gerring** 11:33 Yeah. Well, I mean, do you wanna when, when you have a moment, just chuck the ones that you don't think we should do as part of the Otlp on the list as a comment on the bottom. And then I'll go. Add another comment, another column rather, and say, this is for something else. This isn't relevant.
**Cijo Thomas (Microsoft)** 11:49 Yeah, yeah, I can do that right after this. Yeah.
**Scott Gerring** 11:53 Cool thanks.
**Cijo Thomas (Microsoft)** 11:55 Like some of the things I believe, like e-, even though like Spec says it's needed like we didn't have it like for like so long, and nobody complained. That kind of tells me it's not that important.
So we should be able to like keep focusing on things which really matter like retry would definitely like, people are already asking. So we know that it's very important and then like anything about things which people are not asking like flush, we should be able to deprioritize. So I had a comment.
**Scott Gerring** 12:25 I think that's great. And I mean, this is the sort of institutional knowledge you folks have about what makes sense and what doesn't. We can overlay that on the top, and then pop the important ones off.
**Cijo Thomas (Microsoft)** 12:35 Yeah. There were, I think you created. Yeah, there is this shut down.
There was.
**Scott Gerring** 12:43 That. So I didn't create that one. I just linked it up when I saw that somebody had started working on it.
**Cijo Thomas (Microsoft)** 12:47 Yeah, we did like, if you search for like exporter or Dlp, there are like quite few.
Yeah, some of them already have like issues opened like export or retry pain. I don't think we will have the technical means to enforce it.
Yeah, actually, let's write it.
Yeah, I mean when we actually work on it. We can like, because we did face some challenges earlier. So I put like whatever knowledge we had at that point. And then.
**Scott Gerring** 13:18 Yeah.
**Cijo Thomas (Microsoft)** 13:18 Okay, whenever we try to do it like we can. Take a look at it and shut down. There is one deadlock issue this.
**Scott Gerring** 13:26 That one that one's interesting, because on that one it looks like it's not an issue.
**Cijo Thomas (Microsoft)** 13:32 Yeah, yeah, I think.
**Scott Gerring** 13:33 You come back and say, actually, it seems fine, and I had a look, and it seemed fine to me as well. It didn't look like you were awaiting across.
Correct? Yeah, yeah.
Before.
**Cijo Thomas (Microsoft)** 13:42 Yeah, it took like some time, because we did have a block issue in the beginning.
But then we reflected, and then it's kind of gone. But then I was partially like thinking about the old implementation. But yeah, I mean.
**Scott Gerring** 13:57 Then you can.
**Cijo Thomas (Microsoft)** 13:58 Then 1 1 less thing to worry about.
**Scott Gerring** 14:00 I mean that one can be close, right like. I also went through it today to convince myself that it was fine, and that it really doesn't look like it's holding the mutex across in the white point.
**Cijo Thomas (Microsoft)** 14:11 Yeah, this is Sep separate ones. I'll ask this person to open a separate issue.
Yeah, we did have like deadlock. By the way, like that. We, I remember, like there was an issue earlier but that issue was not in the exporter, but it was in the metric periodic reader.
So we were like that looking that was fixed so this, yeah, I'll keep this open. So I don't forget. There is one thing which you probably would want to spend lot of time, too.
Design. Let me open that issue like there are few. Yeah, this is the only thing which I really want to like, discuss a bit more.
**Scott Gerring** 14:50 Oh, this is the self, the kind of self recurring thing! Hey?
**Cijo Thomas (Microsoft)** 14:55 This is quite hard problem to solve. But we do have techniques to avoid this.
**Scott Gerring** 15:02 You have the context suppression. Now, I think right.
**Cijo Thomas (Microsoft)** 15:05 Yeah, so problem here is like, we designed the context suppression like we. So if you start doing something which can potentially generate more telemetry, so you can suppress you. Start the suppress straight while you're doing that, and when you're done you drop that guard that would work. But the only challenge is someone. If you are crossing a sync boundaries, then you need to like manually propagate it.
So this only works if that propagation works. And unfortunately, when we do the tonic hyper, all those libraries, when they switch across threads for their Asin corporations, they don't propagate our context.
There is no globally agreed context and sub interest. So what we have is our context. Hyper uses their own context. Maybe they use Tokyo's context.
So this is indeed an issue. So I believe there are like few like workarounds.
One of them is what we actually show right now in our examples like our.
If you ever looked at our example. There is a very think you probably commented on it like sometime ago, maybe like someone else. So we have this commend says, like, you're basically adding a filter for all those libraries like hyper tonic. H, 2. Request. So it's not contextual filtering. It's like flat. You turn off logs from these libraries period, which means, if you use these libraries outside of Otlp, you would pretty much miss.
**Scott Gerring** 16:39 Yeah.
**Cijo Thomas (Microsoft)** 16:40 Everything. So that's not the app thing. But this is the best way to prevent that. Infinite loop. Live loop kind of thing. And there is a there was another issue, I believe.
The open for the same issue, and I I'll have to find where it is. So other. Another option which we were trying for that option or to prevent this issue is so. When we create otlp exporter, we instantiate a client.
either tonic or request, and they require a tonic. Sorry, Tokyo Runtime to operate.
So what we currently do is if you look at our example, we don't explicitly do anything we are creating like in it logs, which basically means we'll come and build the tonic exporter. So this -oh tonic client captures the current runtime. Since we are operating in an Async main, which means we are already in a Tokyo context, it just captures it and uses that so the workaround which someone suggested. And it thing. I tried that, and it did work. So what we do is instead of capturing the Async runtime context or async runtime we create a new runtime like a different instance of the Tokyo runtime and set it to run on exactly one thread and then for that thread we put the context suppression.
and then we know that no matter what tonic does underneath, it will only be running on exactly one thread where we have completely suppressed it.
I'm trying to find like who suggested that. But it was definitely like suggested and try. I think I tried. Maybe I can find the issues. It's not circular.
**Scott Gerring** 18:40 Yeah, I remember seeing this. I guess there's also interesting implications on that for the user. In some cases people probably want to control all the threads running their application, for whatever reason, maybe.
**Cijo Thomas (Microsoft)** 18:53 Hmm.
**Scott Gerring** 18:53 On lower resources.
**Cijo Thomas (Microsoft)** 18:55 Be able to find this one. So to do.
Yeah, somewhere, it was mentioned here. Like, it's, oh, yeah, maybe this one, I think, yeah.
yeah, we did attempt like several options. It was not very easy.
But yeah, one of this has to be, because this seems like a very important thing.
I don't know whether we can even call Otlp exporter a stable unless we solve this problem. It it may be like non-trivial, but I think I feel like this is a very important one to be.
**lalit** 19:47 Like sold cool.
**Cijo Thomas (Microsoft)** 19:50 Yeah, hey, this?
**lalit** 19:51 Yeah, sorry. Just. I don't think we should make it as a blocker, right? Because it's not a rush specific issue Internet. Every language will have this issue if if they have, if I mean if their Otlp exporter is having some dependency on the Async libraries.
that's kind of issue with most of the languages right.
**Cijo Thomas (Microsoft)** 20:12 But I don't think any language is unsolved, like every language has solved it.
And python, I know for sure, like we sold it even before our 1st release. So.
**lalit** 20:23 It could be that some languages may have tech school task local variables which is missing interest. Probably that's would be one of the reasons I know, in C plus we haven't really done. We could not really have any solutions. We even called it stable without fixing.
**Cijo Thomas (Microsoft)** 20:37 In your in c plus plus. There is a difference like the libraries which you are using in Otlp is not instrumented.
They're not natively instrumented, but.
**lalit** 20:45 They have started happen. That started happening now. And we do see the challenge. And I don't.
**Cijo Thomas (Microsoft)** 20:51 Difference and then timing. So you'll eventually face that problem. But for rust we already have this from day one, because these libraries are already instrumented with tracing for a long time. So we have this problem from like day one. And the workaround is like quite ugly, like. We just suppress the entire telemetry from those crates which is like, I would say, it's like we are suppressing useful telemetry for preventing this problem, because that may have mask, like some other genuine problem. So that's why I feel like it's.
**lalit** 21:25 You know.
**Cijo Thomas (Microsoft)** 21:26 It's really ahead.
**lalit** 21:26 I mean that that's suppressing. I mean, I understand, like some a user may be using having a direct dependency on those libraries. And we don't want to suppress those.
**Cijo Thomas (Microsoft)** 21:35 Yeah, yeah.
**lalit** 21:36 And that's not possible to do it. With this approach.
**Cijo Thomas (Microsoft)** 21:39 How is the like? You said that c plus plus otlp like is having this problem. What are they instrumenting with? Are they instrumenting with open elementary C plus plus logs? Or are they using some other library.
**lalit** 21:52 They have started using Portal C plus plus at least the Vrpc library has started using that. And now they're facing the issue.
**Cijo Thomas (Microsoft)** 22:00 They are using the open Elementary's own library, which means they can at least propagating open elementary school.
**lalit** 22:06 Yeah, yeah, so it's solvable from that perspective, at least in C, plus plus.
**Cijo Thomas (Microsoft)** 22:11 Yeah. But the problem we have is like.
**lalit** 22:13 I understand. Here, this is.
**Cijo Thomas (Microsoft)** 22:14 Like Tony can request their instrument with tracing, and they don't get they don't do anything with our context.
**lalit** 22:21 That's that's what makes this more challenging.
**Cijo Thomas (Microsoft)** 22:26 Yeah, yeah, I mean, personally, I think this is a like very bad issue, like we, we shouldn't be like calling ourselves stable. If we cannot like.
prevent this one. But I also understand the challenges.
**Scott Gerring** 22:40 The issue closed. If it's if it's still an issue by the.
**Cijo Thomas (Microsoft)** 22:44 So this was a general issue, open like, for not just otlps was a general one, so we sold it with the suppression, and we opened the a separate issue specifically for or Del P.
That is not close. So this is the overall, like we solve the issue by creating this thing called, Excuse me.
Let me open this one. Otlp. Yeah, for Otlp. It is still an issue.
**Scott Gerring** 23:13 Cool.
But yeah, I'll just. I'll link it onto the bottom of the other one. So I don't lose it, because it would be good to say, like all of these things, represent the stabilization.
**Cijo Thomas (Microsoft)** 23:21 Link back here. So it's easy.
Yeah, so I believe the best way we can solve is based on what like.
I was trying to save earlier. Like thing. Yes, single threaded export which I believe I tried once. I don't remember like whether it was a Pr or some place here. Basically, the idea was we, instead of relying on so instead of relying on sorry instead of hyper and request and tonic, these clients capturing the current runtime.
We have an option for them to create a brand new runtime with just one threads.
and in the startup of that thread we call like suppress.
that did work actually. In but I'm trying to find like where, where? Exactly. I tried that. It's somewhere here I might be able to find it. Maybe this one like Apm. Client, which they're oh, yeah, actually, this one.
So what they're doing is, instead of capturing the client Runtime. They create a new Tokyo runtime with just one thread.
and use that runtime to create the Http and Grpc client. So we know for fact that.
**Scott Gerring** 24:49 Prior art.
**Cijo Thomas (Microsoft)** 24:50 Yeah, yeah. And what we do is, yeah, yeah, inside the like, we So for the Tokyo tracing, there is this set default on that thread local.
So what this does is on that thread.
The subscriber will be like, no open, so it won't even get fit to the open elementary.
Yeah. So there is some prior art. Yeah, I think I copied video and it works. I can.
**Scott Gerring** 25:14 Mind picking that link either into the slack or into the doc, and then I'll add this stuff onto the bottom of the big issue. So it's all in one place. But yeah.
**Cijo Thomas (Microsoft)** 25:32 I may have a Pr like some I mean draft or something, because I do know that I did try this one. I don't remember like, why, I didn't even make it a Pr. Yeah. Forgot, like too many things.
Yeah, this may be the best, I think. Lalith already concluded this like when he tried this like long ago, like how we can handle this one we tried, like all the other options which are like all of them have some downsides this is probably the only one. We show some promises, and again, like we need to make it configurable. So if users don't want us to create a brand new runtime.
then we should make it like a optional thing. So users can accept the self-induced telemetry, and they can do like filtering or something.
Oh.
yeah, I think like, like, score, if you ask me like, this is like along with Retry. This is probably the most important one for Otp, and this is cross cutting. It applies to all.
**Scott Gerring** 26:29 Sweet.
**Cijo Thomas (Microsoft)** 26:30 It's.
**Scott Gerring** 26:31 Cool sounds good. But yeah, it seems like, otherwise it's I think we filtered down all the obvious ones that don't fit like sipkin, so I'll I'll pull it down to the next level for the Retries and have a look at that as well. Yeah.
**Cijo Thomas (Microsoft)** 26:43 Some config issue, environment variable. Those are like, you can somehow leave it.
But yeah, I mean.
that's the major thing. Hey, Lily, do you have any like other things in mind for hotel.
**lalit** 26:58 Bleach no, I mean not specific to the specs compliance. But I created one issue that was more of a clean up for proto, and that will need some changes in Otmp also.
**Cijo Thomas (Microsoft)** 27:14 Something to do with renaming tonic right?
**lalit** 27:16 Yeah, it's more of a yeah, more of a structural changes to.
I think. Probably search for cleanup, or I don't know the name, or maybe search for.
**Cijo Thomas (Microsoft)** 27:25 And do.
**lalit** 27:25 Deleted by me.
**Cijo Thomas (Microsoft)** 27:26 It's on.
**lalit** 27:27 Yeah, this, this, basically it was.
**Cijo Thomas (Microsoft)** 27:33 And Grpc.
**lalit** 27:36 So so I think, basically moving the transformations from pro proto to I mean from hotel proto to the Otlp great.
**Cijo Thomas (Microsoft)** 27:48 Oh!
**lalit** 27:50 And most of the things are cleanup of proto. But I think one of the changes like moving the transformation from proto to otp.
**Cijo Thomas (Microsoft)** 27:56 Okay, yeah, yeah. This, I think, like, Scott has already marked.
**lalit** 28:00 Okay, yeah. Then, that's fine. Yeah.
**Scott Gerring** 28:01 Yeah, I'll I'll check it out as well.
**Cijo Thomas (Microsoft)** 28:03 Yeah, I will do label for Otlp, so it will be easy to see.
**Scott Gerring** 28:10 My wife is shouting at me in the background to come.
**Cijo Thomas (Microsoft)** 28:13 Alright. Yeah. Thanks.
**Scott Gerring** 28:15 Good, good speaking to both, and that was really helpful. Thank you.
**Cijo Thomas (Microsoft)** 28:18 Alright. Thanks any other thing you want. I have like one cute topic to cover which is what we do for the immediate next release.
so you may have seen, like we did merge a Pr like earlier or not merge. We. We have this Pr for refactoring.
Trace the global get set matrix so this is indeed a breaking change.
**lalit** 28:52 Yeah.
**Cijo Thomas (Microsoft)** 28:53 I mean, we are changing the returning. So this is clearly a breaking change. I'm wondering like then, because we haven't decided whether the next release will be.
**lalit** 29:00 Here.
**Cijo Thomas (Microsoft)** 29:00 3, 1 or point 3 0 dot one so what I want to discuss is we have like 2 options. One is, make it clear that the next release is 0 point 3 0 dot one. So it's it's a minor one. We cannot take any breaking and then refrain from merging this or any pr which would result in breaking.
That's 1 option. Second option is stick with point 3 1, which means we can accept this pr, and then any breaking change which we expect in the I think we can only do break and change in tracing, because logs and metrics are anyway stable.
**lalit** 29:33 Yeah.
**Cijo Thomas (Microsoft)** 29:34 But then we probably want to.
Make sure we do all the breaking changes in the next release to avoid like continuous cycle of breaking people which I don't know whether it's feasible in time. So that's the thing which I want to discuss, and unfortunately like beyond is not here, because.
**lalit** 29:53 Hmm.
**Cijo Thomas (Microsoft)** 29:53 Because we need like lot of breaking change in the tracing depend on this issue being resolved because we cannot remove those Apis this is taken care.
So do you have any thoughts or like? We can differ it for another week.
**lalit** 30:13 I mean, do you think like it's if you differ for one more week like, I mean, what's the realistic like?
We have all the different changes.
**Cijo Thomas (Microsoft)** 30:21 Once this Pr is merged. That means the open element. The tracing open, elementary create will no longer depend on the.
**lalit** 30:31 Questionable Apis in our, I mean. In fact, I don't think they will even depend on SDK. They'll only depend on Api.
**Cijo Thomas (Microsoft)** 30:39 Once this is done. So then we can go ahead and do the. We have like plenty of issues which require cleanups. And we are just holding on to that thing simply like waiting. For like, for example, like this.
yeah, it's in this milestone, like fixing Api stable. All these things are like we need to wait for this Pr to be done so once, that is, and we should be able to. Most of them are like simple, clean up. We should be able to like quickly, go through it like span builder should not have like chatter sampling. All these are like relatively small changes, we should be able to like quickly. The numbers are high, but there is no very challenging problem there.
so yeah, my preference is like we do all of them in one shot, so that the next release, whenever that happened, we should be able to call tracing Api stable, and the one. After that we should call tracing St. Kos, or also stable, so in the next to release will be declaring all 3 signals as stable.
Because, like changes are like already, a pain. And people are like, quite frustrated and seeing, like many forums complaining. Yeah, that's why I'm okay with like accepting this. Sorry this pr but then, like, accept everything and delay the release until we are confident that we are done with breaking change.
**lalit** 32:03 Yeah, I think I agree. Probably let's delay it and ensure that all the breaking changes go at one at one go.
And then, yeah.
**Cijo Thomas (Microsoft)** 32:13 And one last thing is, the tracing Api. I was trying to look at like some example. Use case of how we are using tracing. I do have like some like So if you remember, like, we have like 2 ways to create a span like one is you use the tracer.
you obtain a span builder, and then you add all the with attributes.
and then you start it. And then you can optionally activate a context with that. So this is one option, and then the other. Option is the tracer.in span.
which I believe we show here. Yeah, this one. So we have this way of like in span tracer.in span, which creates a span and automatically activates a context in that closure. So users can just access the span and then do like what they would normally do.
So 1st question is like, Do we need like 2 ways to do it, and if you do it like this, this approach I was trying to modify everything, to like one approach the in span one. But then I realized this approach does not allow you to customize anything other than the name, so we cannot even start.
**lalit** 33:34 Yes.
**Cijo Thomas (Microsoft)** 33:34 Span. With this you can only start an internal span with this option.
Which is very limiting, and you cannot do like links or initial attributes, or anything. So everything has to be done after.
**lalit** 33:47 And so, yeah.
**Cijo Thomas (Microsoft)** 33:47 Which is like not really.
not really a good approach, because you you wouldn't even be able to like sample based on any useful links or other things.
I mean, I don't have a solution. I was just wondering like, is it like really worth having all the different ways to it feels more like a convenience thing.
**lalit** 34:10 Yeah, it's more of a convenient.
**Cijo Thomas (Microsoft)** 34:12 It's convenient, but it's only like very limited like it's it's limited to people creating named spans with internal span type. That's the only time where.
**lalit** 34:21 It's more like they have an estate kind of. They can have some kind of.
**Cijo Thomas (Microsoft)** 34:26 Have a parent spend like somewhere.
**lalit** 34:28 And they just.
**Cijo Thomas (Microsoft)** 34:28 To like, add few things. Yeah, this feels bit old, I. And the reason why I bought that is because I was writing the like some document out like a a north star goal of how open, elementary and tracing plays along. Once beyond Spr. Is done in the tracing repo. So one of the recommendation, I haven't shared it yet. I will share it like very shortly, is that we need to like, make some firm recommendations on how to create span. So number one thing which I was right writing in my to be shared document is, you'll always show this way of creating span by using open elementary meant. This is mainly for edge spans, like either the receiving server span or the outgoing called Http. Client or SQL. Client spans.
but for anything within that oh.
we mean, of course we can. I mean, of course, users can use the same Api instead of creating server. They just create the inner span and go ahead and do it, or they can use the Tokyo tracing Api. They have these nice instrument things which by default can only create like internal spans like they have the same problem as this Api. They don't have a way to specify a server, span or client, span or remote parent or anything. This is more closer to the Tokyo tracing span. So I'm thinking, like, if we are anyway going to nicely interrupt with them. We can potentially ask people just for a convenience purpose. Just use the tracing macros. But for the edge spans where you really want to specify span kind, remote parent, or those things like use the open elementary. I haven't like fully thought through it. But, like, do you see? Like some value like pursuing this further, because this may be a very popular Api. So if you're breaking it, that may come back with some pushbacks.
**lalit** 36:31 Do we see more of a maintainable maintainability like if we.
**Cijo Thomas (Microsoft)** 36:35 It's always like that thing like, if you have like, 2 ways of doing one thing that's that's always feels like a concern to me, and I'm not sure of the perf implications either. The reason is like here.
if you think this is a boxed span, what we are getting back, and I believe it takes a log or something.
So when you call it and think it takes us like local something I need to look at like where we are doing it.
so that may have, like some implication on the performance as opposed to this one. Where you have the span with you. You don't share it with anyone you can like. Do anything with it without having to worry about logs or something.
**lalit** 37:24 I mean, my only concern is like, I mean, I'm okay. I'm like for me. I think it. It looks good to have only one Api, but then, recommending them to use a mixed approach like you're saying that use a Tokyo macros.
**Cijo Thomas (Microsoft)** 37:37 Yeah, that's okay.
**lalit** 37:37 Sort of.
**Cijo Thomas (Microsoft)** 37:38 Yeah, yeah, I see, it's your point. Yeah, yeah.
Yeah. And there is one more issue which I found with even with this Api again, like, I haven't written down it completely. But the issue here is once you create this fan. And if you want to activate a context with that span. You basically give up the span ownership, because once you call context with span span, you cannot get span back. And then you have to ask the context, hey? Can you give me a rough to the span back.
**lalit** 38:12 Okay.
**Cijo Thomas (Microsoft)** 38:13 Yeah, and also feels a bit old.
because I believe this one is quite expensive getting the next.
**lalit** 38:23 Okay, yeah, I have to see the quote, just to be very sure. But.
**Cijo Thomas (Microsoft)** 38:26 Yeah, you need to look at. Yeah, somewhere, I did see like it was.
yeah. So that's what I spent my case going to be like a huge contention problem if it's going to do like mutex or logs.
Oh, like creating like spans. And like, just because you entered a span context. Now you have now that if you want to retrieve the span now, you need to take a.
**lalit** 38:54 Have to use a context here on.
**Cijo Thomas (Microsoft)** 38:56 That feels a bit awkward, but I don't know what else.
**lalit** 38:59 And ideally like I mean in most probably once we set the span, or it's expected. Once you set the span in a context, you won't be updating or adding, but they can add the attributes right.
**Cijo Thomas (Microsoft)** 39:13 Yeah, they want to like.
**lalit** 39:13 They want to add that to me too.
**Cijo Thomas (Microsoft)** 39:15 You start a parent span and you activate. And then you do about your actual thing. And while doing that you want to add more things to the existing span. You don't have any interest in creating a new span. So you just want to look at what's the current span? Let me add, like couple of attributes based on what I'm seeing that very common thing it may require, like some redesigning. Because, do we need to? We need to probably challenge the fact that why do we need to give up the whole span for attaching to a context? Is it sufficient to just attach the span context alone, the immutable of span which we can easily give up not the span itself. Yeah. Anyway, like, I didn't finish my research. I felt like.
or that this Apa has this challenge, and in span has its own challenge.
Yeah. Anyway, like, I just like throw some random thoughts so only thing which I plan to do like between now and next week is, I'll modify the benchmarks to show both ways of creating spans like the in span one and see if the performance cost is like visible so once we measure, it's significant. Then we can talk about okay, what's the best way to handle it.
**lalit** 40:33 Yeah, I agree. I think. Let's let's have some some benchmark.
and then probably we can take a call.
**Cijo Thomas (Microsoft)** 40:40 Yeah, you might might remember, like we did discuss this long ago, like the whole.
the open elementary module for trace has this weird boxed spanner. Sorry, tracer.
**lalit** 40:53 Yeah, yeah, I know what I mean.
**Cijo Thomas (Microsoft)** 40:54 The yeah, because it was not.
think it is. Yeah long ago. This is the tracer one, and then the pretty much mimic that I believe in here or in the context. I think it's in the context that.
yeah, we have this synchronized span.
which has the yeah. This is a mutable.
We have a. So anytime people want to do anything they have to take a lock.
**lalit** 41:23 Okay.
**Cijo Thomas (Microsoft)** 41:25 That's yeah. So this is what I was. Yeah, sorry. This is what I if you want to add an event or record error like pretty much anything you want.
**lalit** 41:34 Oh, okay.
**Cijo Thomas (Microsoft)** 41:35 Attribute. You had to go to the inner mute with inner muting.
**lalit** 41:38 Yeah, which will lock it here.
**Cijo Thomas (Microsoft)** 41:40 This is what I was trying.
**lalit** 41:41 Okay.
**Cijo Thomas (Microsoft)** 41:42 This feel safe.
like fundamental like design issue. It's okay but like, I'll see if I can show some benchmarks and see if it is actually an issue or not. I don't know the solution. I just felt it very awkward to have 2 Aps, and even with that we we still have some performance challenges. Yeah. Anyway, I'll measure it and share it.
Speak, and then we can decide what's the best course of action.
**lalit** 42:09 Yeah, sure you. I think it's probably to have more numbers here. Then you can discuss.
**Cijo Thomas (Microsoft)** 42:14 Oh.
okay, yeah, I think I don't have anything else. I do have like couple of open Pr, so if you get a time like, just take a look at it one is very simple, like it's improving the bug template like, it's very easy. So take a look at that.
**lalit** 42:33 Thank you.
**Cijo Thomas (Microsoft)** 42:34 I think, and then there is a tutorial for eager. I am still waiting for other maintenance to also share their opinion, because only if everyone agrees that we need to maintain such tutorials, then only it makes sense. For me to continue working on that.
**lalit** 42:47 What was that? I I didn't go through that. But yeah, that would be similar to Otlp. Right? What's the difference? We have it here.
**Cijo Thomas (Microsoft)** 42:53 Yeah. So it's more like, I'm trying to write more like a tutorial which you start like step by step, you'd start a hello world app you, add something to it, and then you install Jaeger as a docker or exe, and then you export it, and then you visualize it. Then like incrementally build on it. So now that you've seen traces, let's see.
child, across, the process would look like and then incrementally build it into a quite deep tutorial the challenge is like, every time we are adding tutorials. It's it needs some runnable code which means cargo file program, file everything. So we're adding more and more examples. So that might be a concern but I don't know. I'm personally, I'm okay with that. This is necessary showcase like how, even even for we don't have like tutorials per se, like we have like examples which show it so people can just look at the example and figure out things of their own. But I don't.
**lalit** 43:56 I mean. The only thing is that the docs I mean, like you, have to be in sync with the code all the time you have to ensure that any change which we do in the code.
**Cijo Thomas (Microsoft)** 44:04 Exactly. So. That's why.
**lalit** 44:06 Yeah.
**Cijo Thomas (Microsoft)** 44:06 It comes with an example. So even though I called it as ad tracing tutorial Doc, it's really adding to the examples folder which has. So we ensure that it is buildable all the time. And also that's why that's why it is extra maintenance thing, anyway, like, see like, look at the Pr. And share your. You don't need to look at the actual content like, see if the direction is acceptable, because I expect to like, continue with logs and metrics, and do a thing like, because, as of today, like many people, complain that there are no such tutorials for rust. So it's more.
not something from Otlp, something from the SDK docs and something from our examples and users manually teaching together all those information, which is, why let's do this.
Yeah, anyway.
**lalit** 44:57 We have. Do we have these things in corporate also, I mean, like.
**Cijo Thomas (Microsoft)** 45:00 Yeah, yeah, we do maintain, yeah, we do maintain like, multiple tutorials in, it's even complex. Maybe like, it will be same interest. So in.net we maintain, like 2 set of tutorials for each signal, and the reason is, one is with the symbol, control, style, application, and then one with the web application which has dependent and all. So we actually maintain 2 examples for all 3 signals.
**lalit** 45:28 Perfect.
**Cijo Thomas (Microsoft)** 45:29 Yeah, I mean, based on my experience. Not that difficult, because once you are declared like one dot 0. You don't change that often, right. In fact, you cannot change at all. So the question of dependency is mostly keeping up the dependency update which depend about and renovate is doing a nice job already.
**lalit** 45:49 Yeah, I think it's 1 way, it's good that we won't get very basic issues in in the in our Github as issues, or maybe discussions.
**Cijo Thomas (Microsoft)** 45:56 Yeah, the the one like I did cover it in like some of the document, like people still don't have a good idea of like.
how they should create a measurement.
The entire entire steps involved in creating a measurement is like you had to obtain the global provider. Then you create a meter, then you create an instrument, then you call the corresponding Api. So which which of these should be like one time versus like hot path. Those are like not very easy to convey. Like in our example, we did show that like counter is created once, but it's nowhere like we mentioned as a tutorial that you should do it once and then.
**lalit** 46:39 Did you use it yet?
**Cijo Thomas (Microsoft)** 46:41 Same for tracer. Also, like you.
**lalit** 46:42 Yeah.
**Cijo Thomas (Microsoft)** 46:43 Even in, like many like non non official docs, I have found that people are repeatedly trying to acquire a global tracer and then create span from it. So that tells that our dogs is not. Our dogs are not very good at conveying that. Okay, obtaining a tracer is something you should do like one time, not repeatedly. So that message is very hard to convey without writing tutorials.
**lalit** 47:07 That makes sense really.
**Cijo Thomas (Microsoft)** 47:10 Anyway, like I'll work on like some like benchmarks. And meanwhile I'll wait for more feedback on the tutorials.
**lalit** 47:19 Yeah.
**Cijo Thomas (Microsoft)** 47:20 Alright. Yeah, thank you. I'll put something in the notes. So people who missed can see if they want to listen or not.
Thank you.
**lalit** 47:27 Yeah, thank you.
What?
