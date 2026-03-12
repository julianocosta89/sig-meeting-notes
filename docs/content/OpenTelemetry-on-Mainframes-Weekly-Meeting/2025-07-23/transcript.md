SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-07-23
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**Jim Porell** 01:04 Hey? Greg thought it might be just you and me.
**Greg Shriver** 01:08 Hey, Jim, how you doing? I'm just.
I'm just trying to catch up here on slack.
**Jim Porell** 01:16 Yeah, I just, I just post all that stuff into the. I moved it from slack into the document. Today's.
**Greg Shriver** 01:21 Okay.
**Jim Porell** 01:21 And oh, so
**Greg Shriver** 01:23 Perfect.
**Jim Porell** 01:24 I figured if you and I wanna just go over it. We can.
Yeah.
**Greg Shriver** 01:29 Sure.
**Jim Porell** 01:30 Idea. So I'll share the screen accessing your screen. Yeah, that's all right. Share and go to Google.
Yeah, see? I already guessed it would just be you and I.
**Greg Shriver** 01:50 Guessed you guessed we were it. Yeah.
**Jim Porell** 01:52 Yeah.
Yeah. Rudiger, anand rudiger.
Yeah, I had already talked to Anan and cause I had a meeting with them. It was weird. We had a 1 on one at one, anyways, and.
**Greg Shriver** 02:04 Oh, okay.
**Jim Porell** 02:05 Later, and he told me I couldn't make it so.
I don't even care about any of this. I'm more interested in what the results are.
**Greg Shriver** 02:16 Okay? Oh, and this is the open tulero mainframe survey. Okay.
**Jim Porell** 02:19 Right. So I think the rest the beginning of this. I'm not too worried about it.
background and purpose, and that we can read later, I'm more interested. What do you get as results?
**Greg Shriver** 02:34 Yeah.
Oops.
Insights? Yes.
**Jim Porell** 02:59 Wow! Metrics more important than traces. That's not the Ibm priority.
They're way more focused on traces.
**Greg Shriver** 03:11 Where do you see that.
**Jim Porell** 03:12 That's bullet 2.
**Greg Shriver** 03:14 Going to okay.
**Jim Porell** 03:21 Oh, wait! No, no, I'm sorry. Where did I see that
**Greg Shriver** 03:28 Yeah, it did say.
**Jim Porell** 03:28 Oh, priority prioritize for metrics that actually makes sense. Yeah.
**Greg Shriver** 03:33 Up.
**Jim Porell** 03:34 Cause, I think, to be honest with you, they're still gonna be, for they're gonna apply to traces equally to metrics. So.
**Greg Shriver** 03:41 Right.
**Jim Porell** 03:42 When you name something.
Okay.
**Greg Shriver** 03:47 That's interesting.
Java and Python sdks develop a cobol. SDK, I you know I I'm surprised at that cause. I just can't imagine anybody actually taking advantage of that.
**Jim Porell** 04:03 I've heard just the opposite, but.
**Greg Shriver** 04:06 Really oh, good!
**Jim Porell** 04:07 And and the reason is.
I'm gonna call it there's probably 10 customers in the world that want it, and their finance industry customers whose bread and butter is on cobol kicks or ims applications.
I believe. And and I know Ruger presents it this way is that we're trying to get the subsystems to do it transparently, you know, on the applications behalf. But there's some bleeding edge guys that you know, on this particular application. They want to be able to trace it earlier than the subsystems can do it themselves.
so that makes sense.
**Greg Shriver** 04:48 But they could do that, I mean, but they would be into it for developing their own. I mean they. They could emit metric spans and.
**Jim Porell** 04:57 Oh, yeah, yeah, but they'd like, but they'd like a A an SDK to just bury it into their code. So.
**Greg Shriver** 05:03 Sure. Yeah, no, I guess I guess that makes sense.
I mean in easier.
**Jim Porell** 05:10 My bet is, though, my bet is, though, people don't understand that. Unlike distributed environments, it's the system that's gonna take responsibility here. And so you probably don't need it as much on the Z side as you would on a Linux unix windows side.
**Greg Shriver** 05:28 Hmm, that may be true.
**Jim Porell** 05:29 I don't know but we'll see.
**Greg Shriver** 05:33 I mean in Java, I mean, Java has its own runtime environment, so that makes it kind of easier.
**Jim Porell** 05:41 Oh!
**Greg Shriver** 05:43 Not I, you know, and I'm not a cobol expert, but I don't think it has a Co. I don't think there is. No, I don't think there's a cobal runtime environment.
**Jim Porell** 05:51 No, but they need a they need a callable interface. So call whatever the Java or something, you know.
Yeah.
the wherever the collector is some some way to call out that they can easily add to their program.
**Greg Shriver** 06:04 Yeah.
**Jim Porell** 06:04 You're right. It's not in a runtime, but it's more of a callable service.
**Greg Shriver** 06:09 Le anything Le might be able to.
**Jim Porell** 06:12 Right, right.
**Greg Shriver** 06:13 You know, to do that stuff.
**Jim Porell** 06:15 Yeah.
**Greg Shriver** 06:17 All respondents wanting. Java. Okay, well, we already there is already is a Java SDK.
**Jim Porell** 06:22 Yeah, I think there's a python one, too.
But I do think Ibm is working on a cobalt one. So.
**Greg Shriver** 06:31 Okay. Alright. Well, hey?
**Jim Porell** 06:34 That's that's great.
Hello!
**Greg Shriver** 06:37 That's great. I mean to the extent that people the extent that people will consume that will be interesting to see.
**Jim Porell** 06:47 Oh!
**Greg Shriver** 06:50 You know, like you, said the bleeding edge.
The small 10 customers that you know absolutely want this. They'll probably adopt it.
**Jim Porell** 07:00 Right.
I don't know the rest of this. I oh, here's comprehensive responses coming up, but ways to contribute whatever you know.
Yeah, you can go help build one. Yeah, so.
But I guess you tell me when and I'll shoot down.
**Greg Shriver** 07:25 Yeah, I'm good.
**Jim Porell** 07:26 Okay, alright. So.
**Greg Shriver** 07:30 Oh!
**Jim Porell** 07:31 Mostly managers. Looks like.
**Greg Shriver** 07:33 Yeah, it architects. Software architect.
**Jim Porell** 07:37 Frog.
**Greg Shriver** 07:39 That makes sense.
**Jim Porell** 07:40 What's this? One observability engineer, mainframe, developer, devops, engineer, sre, and then all onesies.
Alright!
**Greg Shriver** 07:49 Okay.
**Jim Porell** 07:51 User experience.
Mainframers, not a mainframers. Okay.
**Greg Shriver** 07:58 Was that
**Jim Porell** 07:59 Well, it's either 10 years more than.
**Greg Shriver** 08:01 That Terry.
**Jim Porell** 08:02 Years, and then less than 3 years. So I was going main farmers, Newbies.
**Greg Shriver** 08:07 Newbies, yeah.
**Jim Porell** 08:09 Yeah.
Well, 7 to 10 and 7 to 10. But it's still, that's this number. So it's.
**Greg Shriver** 08:16 Yeah.
**Jim Porell** 08:17 Like 8 or something.
Make this a little bigger, by the way. So let's see.
that's 1 better.
Primary industry, financial services.
**Greg Shriver** 08:32 Service.
**Jim Porell** 08:32 Oh!
**Greg Shriver** 08:33 Yeah, there, you go.
**Jim Porell** 08:34 Rainer Yup and insurance insurance, but that's all finance. So.
**Greg Shriver** 08:42 Isv, that's the.
**Jim Porell** 08:43 That's kind of.
**Greg Shriver** 08:44 Us, yeah.
**Jim Porell** 08:45 Yeah, Isv insurance. So service provider. Okay.
**Greg Shriver** 08:51 I can see that.
**Jim Porell** 08:52 In healthcare.
**Greg Shriver** 08:54 Yeah.
**Jim Porell** 08:56 Yeah, well.
**Greg Shriver** 08:56 So it's based finance, finance, insurance and Isvs and everybody else.
**Jim Porell** 09:02 Yep.
**Greg Shriver** 09:03 Yeah, yeah.
**Jim Porell** 09:04 Not not surprised. There.
**Greg Shriver** 09:06 Not a surprise.
**Jim Porell** 09:10 One Vsc. Alright Zos and Linux. All right.
**Greg Shriver** 09:14 Okay, zvm, too. Yeah.
**Jim Porell** 09:17 Yeah.
alright. 82. Okay. Where's that? Wow? I mess right down here.
**Greg Shriver** 09:26 Ims zos connect is close to Ims connect.
and and coming up on Mq. As well.
**Jim Porell** 09:32 Yeah.
**Greg Shriver** 09:33 Was liberty.
**Jim Porell** 09:36 It is. So you guys got you guys got covered here.
You guys own Datacom. Also.
**Greg Shriver** 09:43 We do? Yeah.
**Jim Porell** 09:44 Okay.
**Greg Shriver** 09:45 And Hb. Dot, Js.
**Jim Porell** 09:46 What is that? I don't know if that one's.
**Greg Shriver** 09:48 Hostbridge.
**Jim Porell** 09:49 Oh, yeah. Okay.
**Greg Shriver** 09:51 Let's host Bridge. Yeah.
**Jim Porell** 09:53 Okay.
yeah, expert. Let's hire those 3.
Probably our own team.
**Greg Shriver** 10:05 Yeah, yeah.
**Jim Porell** 10:06 Segments.
**Greg Shriver** 10:07 Yeah.
**Jim Porell** 10:08 Did you do the survey? I didn't do it because.
**Greg Shriver** 10:10 I didn't. I didn't take the survey.
Yeah.
Oh, none of that familiar with oh, wow!
**Jim Porell** 10:20 Right in the middle.
**Greg Shriver** 10:23 Wow!
**Jim Porell** 10:23 Where's tracing, distributed, tracing down here.
**Greg Shriver** 10:26 Are you familiar with metrics? Open telemetry, collector logging? Okay.
**Jim Porell** 10:32 That's interesting.
OP. Amp, yeah.
Well, alright. Observer. Visibility of performance. I'm on the camera.
Oh, thanks.
**Greg Shriver** 10:45 Both distributed and mainframe. Okay, only for mainframe platforms.
Not at all.
**Jim Porell** 10:51 Impressive.
**Greg Shriver** 10:53 Yeah.
**Jim Porell** 10:54 Absolutely.
Then what'd you take the survey for us? That's interesting.
**Greg Shriver** 11:00 Well.
oh, okay.
**Jim Porell** 11:10 Oh, okay.
not a lot. So who's a lot? 81 to 100?
It's still not a bad amount.
**Greg Shriver** 11:22 One to 80, now.
**Jim Porell** 11:23 Got 1111 versus what? 19 there?
Yeah.
**Greg Shriver** 11:28 Yeah.
**Jim Porell** 11:29 Okay.
they still got better than half is.
1112, 13 out of whatever there is. But okay.
hold on. Hold on. One second, Greg.
**Greg Shriver** 11:47 Sure.
**Jim Porell** 11:48 I got.
Yeah, I see that. Yeah, I will.
Okay, alright. I got it. I gotta do this call for an hour. So not a problem. Thank you.
My lunch has been delivered. So that's what.
**Greg Shriver** 12:08 Nice.
**Jim Porell** 12:09 You don't.
You don't need them right away.
All right, I'm going to town.
**Greg Shriver** 12:18 Characteristics, real time and then available standards. Context.
carbon accounting. I'm not.
**Jim Porell** 12:28 Sure what the hell that is I don't know.
**Greg Shriver** 12:30 I don't know what that is.
**Jim Porell** 12:32 Oh!
**Greg Shriver** 12:33 These other things make sense.
**Jim Porell** 12:39 That's a scary one for us. Vendors.
**Greg Shriver** 12:44 Yeah. But is it, though, is it? Is it really? I mean, you know, haven't. If the customers have the choice, they're probably more likely to, you know they're probably more likely to embrace it, you know, if they don't feel locked in.
**Jim Porell** 13:00 Yeah, that's true, too. I I honestly I I was. I did a pitch to Kindrell on this topic today.
You know the pendulum mainframes in vogue mainframes out of vogue.
**Greg Shriver** 13:12 Sure. Yeah.
**Jim Porell** 13:14 I think this is huge.
because if you know how much is management by magazine of executives, where? Where, if, if open telemetry is only distributed. Well, then, the answer is distributed. Move the applications again. If they see the mainframe connected.
**Greg Shriver** 13:32 You bet!
**Jim Porell** 13:32 This, I think we're locked in. This makes us sticky again, and.
**Greg Shriver** 13:37 Yeah, I.
**Jim Porell** 13:39 Well, go ahead!
**Greg Shriver** 13:40 I agree with you.
**Jim Porell** 13:41 Yeah.
**Greg Shriver** 13:42 I think this is really big in that regard, and I 100 agree with you. In fact, I think that you know we I mean, people have been talking about the death on Mainframe, as since I've as long as I've been on the platform.
you know, and and I have a lot of gray hair. So you know, people have been talking about this for years and years, and.
**Jim Porell** 14:02 Yeah.
**Greg Shriver** 14:03 And you know it's it's still there. I get it that people want, you know, are are interested in moving things off. But you know I I get that. But I think that the single biggest thing that we can do to prolong the life of the mainframe is embrace open telemetry.
**Jim Porell** 14:26 Yeah, I really do.
**Greg Shriver** 14:28 And that's why I'm that's why I'm here.
**Jim Porell** 14:31 Yeah.
now, that was a revelation I actually had. It came out of my mouth. And I'm like, Oh, my God, that's right. And this could really preserve mainframes forever. I I don't. I don't particularly agree with the way Ibm's implementing it with their native emissions. I think that's gonna throw the meter off, but I think between us as vendors, we can really make this awesome. So.
**Greg Shriver** 14:56 Alright. Yeah. Yeah.
**Jim Porell** 14:59 Alright!
**Greg Shriver** 15:02 What do you look at this 1st metrics?
**Jim Porell** 15:05 Logs and traces. But this is Ibm's focus, which is really crazy. But I actually think the span stuff is really important, because that gives you the app right now, we're doing subsystem stuff.
This is application focused and everybody wants to manage by application. So I'm not. Gonna I'm not gonna disagree with them at all.
**Greg Shriver** 15:26 Agree.
**Jim Porell** 15:26 Application. Topology is really the secrets. It's the secret sauce of open telemetry.
**Greg Shriver** 15:32 It is it? It is. And you know the the focus here has been on traces, you know. I mean, I I've been pushing logs, but nobody else wants logs right?
**Jim Porell** 15:43 Yeah.
**Greg Shriver** 15:43 But but but traces. And you know the customers that we've talked to when you show them a trace with their application. They're like they're they're in, you know. They're they're they're in.
Yeah. That's.
**Jim Porell** 16:03 Okay.
**Greg Shriver** 16:04 That's interesting.
**Jim Porell** 16:05 Yeah, I love the topology. I love topological views of apps. It's just amazing that you can do. There.
**Greg Shriver** 16:11 Yeah.
**Jim Porell** 16:12 Primary users.
**Greg Shriver** 16:14 Primary use of the main.
**Jim Porell** 16:16 Sres. Okay, app devs. This is devops.
**Greg Shriver** 16:21 Okay.
**Jim Porell** 16:22 That's not bad. Yeah. Security.
**Greg Shriver** 16:24 Sense, though.
**Jim Porell** 16:25 Yeah, I'm surprised. Business stakeholders wasn't higher, but because I could. To me, business stakeholders is an executive and and all they're interested. They want to see green, no red, no yellow, just green, so.
**Greg Shriver** 16:36 Right, which, which, for multi-platform applications, open telemetry feed, you know.
**Jim Porell** 16:42 Yeah.
**Greg Shriver** 16:42 Facilitates that.
**Jim Porell** 16:43 Right, exactly.
**Greg Shriver** 16:44 So I agree with you. I I think the business stakeholders should have been higher, but.
**Jim Porell** 16:48 You know what? There were probably no business stakeholders doing the survey so true it might be true.
They probably lowballed it.
**Greg Shriver** 16:56 I'm surprised to see mainframe option so high, I mean, but I think that's probably going up.
**Jim Porell** 17:03 And I think again, it's catering to who who took the survey. There's not a lot of people that took the survey so.
**Greg Shriver** 17:10 That's true performance. Metrics, too.
**Jim Porell** 17:18 Oh, this is what what Rudiger summarized up above in the questions.
**Greg Shriver** 17:23 Okay.
**Jim Porell** 17:25 That makes sense.
**Greg Shriver** 17:27 Database. Metrics make sense application. Metrics, I think, is the.
**Jim Porell** 17:31 That's an interesting one.
That's the one that everybody wants. I would think like you said everybody wants to manage by application.
But I think that's really where it comes down to traces is the means to that end. So not necessarily metrics. But we'll see.
**Greg Shriver** 17:46 Sure. But if there are metrics that are specific to an application, I think.
**Jim Porell** 17:50 Oh, yeah, no. True. True. Yep, yep, yep.
yeah. I can give you a graph on any app you know, inside of kicks region that would be very interesting. Yeah.
Oh.
**Greg Shriver** 18:03 Supporting, oh, interesting and divisible.
**Jim Porell** 18:06 Yeah, makes sense.
**Greg Shriver** 18:07 Crude incident management, sure.
**Jim Porell** 18:08 Yeah, that's the whose problem is it?
**Greg Shriver** 18:12 Yeah. Oh, yeah.
**Jim Porell** 18:13 Because right now, we're the ones to blame for 90% of problems.
**Greg Shriver** 18:17 Cause we're you mean we, the mainframe.
**Jim Porell** 18:20 Yeah, we the mainframe. Yeah, we're guilt guilty till proven innocent.
**Greg Shriver** 18:23 That's right.
**Jim Porell** 18:24 This will help. So.
**Greg Shriver** 18:26 Yes, enhance collaboration.
**Jim Porell** 18:40 Say, one.
**Greg Shriver** 18:41 Carbon, accounting.
**Jim Porell** 18:42 Yes, exactly.
Still, don't get that. Yeah.
Yeah.
**Greg Shriver** 18:45 Yeah.
**Jim Porell** 18:46 I'm gonna make it, you know, I'm putting that in the notes. Hold on.
**Greg Shriver** 18:48 Yeah, what's carbon accounting.
**Jim Porell** 18:51 Exactly.
**Greg Shriver** 18:51 Or or is, is carbon? Are are they actually talking about?
carbon accounting in terms of environmental.
**Jim Porell** 19:03 And energy.
Oh, yeah.
**Greg Shriver** 19:11 I mean, there's a whole. There's a whole when I went to Cubecon last year.
no, not last year it was 20, anyway. I went to Kubecon. There's a whole project.
**Jim Porell** 19:21 Yeah, yeah, yeah.
**Greg Shriver** 19:22 In Cncf. That's that's talking about. You know the.
**Jim Porell** 19:25 And credits and stuff.
**Greg Shriver** 19:26 The carbon credits. And and you know, being able to being able to demonstrate that your your electricity footprint is smaller.
You know all of that stuff. So.
**Jim Porell** 19:41 Okay, that's probably I think you just nailed it. That's what it is.
Okay, go back to it.
Oh.
**Greg Shriver** 19:53 Rotation for which application deployment models.
**Jim Porell** 19:58 Online, batch database.
**Greg Shriver** 20:05 It seems like everything.
**Jim Porell** 20:07 Yeah.
**Greg Shriver** 20:08 You know. That's you know.
**Jim Porell** 20:11 I mean this makes sense so Oltp, for sure.
**Greg Shriver** 20:14 Sure. Yeah, for the mainframe. Yeah, you bet.
**Jim Porell** 20:18 Well, standalone applications. I don't know about that. I'd like use the old stuff for that.
**Greg Shriver** 20:24 Yeah.
**Jim Porell** 20:25 Whatever.
**Greg Shriver** 20:30 Export. Java, Python, C. Go.
None of them. Javascript, swift.
**Jim Porell** 20:36 That's I gave up on the mainframe.
**Greg Shriver** 20:40 Yeah.
**Jim Porell** 20:42 Okay, interesting.
**Greg Shriver** 20:44 For the open telemetry Sdks, does your organization require mainframe support?
Okay? So these are all of the existing open telemetry sdks. This is not, hey? There's there's no cobal. There's no bulb.
That's gonna be the next while we're there. Yeah.
**Jim Porell** 21:00 Yeah, okay, here you go.
**Greg Shriver** 21:04 Additional Languages.
**Jim Porell** 21:05 Yeah. Rex. Oh, Jcl, nice.
Your batch jobs.
**Greg Shriver** 21:12 You know, Rex would be possible, because Rex is I mean it is, it can be compiled. But most of the stuff that we vendors pump out is interpreted. Rex.
**Jim Porell** 21:24 Yeah, agreed. So I think that is definitely possible. And like all the automation scripts, that kind of stuff that's all written in Rex. You might want to see that be instrumented. So.
**Greg Shriver** 21:34 For sure. Yeah.
**Jim Porell** 21:36 Alright, Jcl, that's to me is a bunch of batch jobs that you wanna measure.
**Greg Shriver** 21:42 Yeah.
**Jim Porell** 21:43 But I was again existing. Tools do that, but I don't see that included in a span, for example.
**Greg Shriver** 21:53 Mainframe operating systems, us Linux on Z Zptf, and yeah.
**Jim Porell** 21:57 That's interesting. Vsc. Came up as one before. Not anything this time.
**Greg Shriver** 22:02 Yeah.
Collector is most important for your to enable the process distribution of mainframe telemetry data collection at this local to the source. Oh, that's interesting data aggregation that makes sense data collection from any system, data export filtering, batching, processing.
**Jim Porell** 22:32 This is true, this is.
**Greg Shriver** 22:34 Sampling! Oh, boy!
**Jim Porell** 22:35 If I go back to, and I've got it. Here, hold on! Let me just find it.
This is this thing.
You know, this is the collector. It's basically who sends it to off to.
you know, wherever observability platform, you're doing so again. Their goal, you know.
part of Ibm's goal is this native emissions that goes out through the protocol.
**Greg Shriver** 23:09 Sure.
**Jim Porell** 23:10 But this is, they're kind of thinking of this as Z. Linux right now. I think I don't. I don't think they're doing a native collector on zos, because the MIPS I I know we do ours. We do this all in Java.
so that way at least, we're zip eligible.
**Greg Shriver** 23:26 That makes sense. And and we're doing something similar, right? So so. And and and I don't think the native running a native collector on on z I mean, I don't. I don't want to say it doesn't make sense. But you know, I I agree. I think you know you're probably gonna want that that 1st open telemetry collector hop to be close.
**Jim Porell** 23:52 Yeah.
**Greg Shriver** 23:52 You know. And the the one thing we've learned is that, like the open telemetry collector is not just a 1 thing. There's a there's a, there's a big.
there's a there's a whole chain upstream right yep.
**Jim Porell** 24:10 Alright.
Well, there's so many different sources. That's the problem. So.
**Greg Shriver** 24:15 And so many different places where you can, where you can deploy the open telemetry collector like if I want it. If I want it deployed close to my source. I might wanna I might want that to be doing local collection, but I might be doing a whole lot more. I might be doing a whole lot more transformation downstream, you know.
**Jim Porell** 24:39 Oh, that 100% agree with you. Collection has to be local transformation. Yeah, I don't want to burn a lot of mainframe MIPS doing that unless unless they're free. MIPS. No, but you have no choice but to collect it. Local.
**Greg Shriver** 24:54 Right. Yeah, there's some things you can't collect if it's not local.
**Jim Porell** 24:57 Right, right.
**Greg Shriver** 24:59 Yeah.
**Jim Porell** 24:59 But I think the aggregation aggregation transformations that could be anywhere right.
**Greg Shriver** 25:06 Off. Yeah.
**Jim Porell** 25:07 Yup.
Okay.
**Greg Shriver** 25:13 12 reflector on the mainframe for some platform system. Logs wow, mainframe support resources.
**Jim Porell** 25:22 Kubernetes, and trend.
**Greg Shriver** 25:25 Okay? Well, I guess that that makes that makes sense. If your if your Kubernetes is running on Mainframe, I guess.
**Jim Porell** 25:34 Yeah. But yeah, I mean, if you've got Kubernetes, remember, there was a bunch of people that spoke for Linux. Obviously. So that's true. That would be key to them, and this can hit Zcx as well as Kubernetes. Openshift stuff.
**Greg Shriver** 25:48 Sure, sure.
**Jim Porell** 25:52 That's it.
**Greg Shriver** 25:53 That's it.
**Jim Porell** 25:54 Cool. Let's do the other one. What what do you have in that?
**Greg Shriver** 25:58 That's pretty cool.
**Jim Porell** 25:59 Yeah, that's cool.
Oh, okay, this is going back.
Been a while since I looked at the spreadsheet, but that's good. I'm glad he reposted it.
So.
**Greg Shriver** 26:18 I don't remember ever seeing this.
**Jim Porell** 26:20 I remember seeing something like this.
I'll just look at an example. Yeah. So again, I wasn't in the last call. I think you were with Rudiger last week.
**Greg Shriver** 26:33 Yeah.
**Jim Porell** 26:34 Where he said they wanted proof.
The they didn't want to just have these new names identified. But they wanted proof and examples. And I think that's where he's trying to get to. Here.
**Greg Shriver** 26:46 Yeah.
**Jim Porell** 26:47 And entities. That's so. This is a very deep. This is more at the hardware level.
**Greg Shriver** 26:54 Okay.
**Jim Porell** 26:58 Yeah, I think this is still the Wild West.
I think he just started this just to have something to share.
**Greg Shriver** 27:06 Yeah.
**Jim Porell** 27:08 All right.
Yeah, all that. The stuff that used to be in the Google Docs thing. We gotta move some of that stuff into here, and I probably wanna wait for him to weigh in on that. So.
**Greg Shriver** 27:21 Yeah, makes sense.
**Jim Porell** 27:23 Yeah. Alright, alright, very good.
Sure. Yeah.
**Greg Shriver** 27:28 I I have nothing new for today.
**Jim Porell** 27:31 No, I didn't either. So.
**Greg Shriver** 27:32 Yeah.
**Jim Porell** 27:33 Oh, good! All right. But this is good.
I think if we focus on, you know, moving some of that stuff into the spreadsheet that might help, so.
**Greg Shriver** 27:41 Yeah.
**Jim Porell** 27:43 Might have to come up with other categories. I'm not sure about that. So yeah.
**Greg Shriver** 27:51 That's right.
**Jim Porell** 27:51 Alright! I'll add that to the summary. Alright! Good talking with you. Yup.
**Greg Shriver** 27:55 Yeah. Good. Talking with you.
**Jim Porell** 27:57 Bye-bye.
