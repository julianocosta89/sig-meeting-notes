SIG: Android SIG
Date: 2025-07-15
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/fQ6LbJCyBREjQ6jD0mvYNMqd_5GPfWknyPwszsRy4-R9Jyq6CA_DlzaKcDKtsVWI.FIjgFvajm2vVliqb
============================================================

## Zoom Recording Transcript

Cesar Munoz 00:00:23 Hello!
Jason Plumb 00:00:25 Good morning.
Let me get set up here.
Great, almost ready.
How's that looking.
Cesar Munoz 00:01:14 It's looking good.
Jason Plumb 00:01:15 Okay.
Cesar Munoz 00:01:17 Yeah.
Hanson Ho 00:01:22 Hello!
Cesar Munoz 00:01:25 Hey! Hanson!
Hanson Ho 00:01:28 Catching up on stuff.
How's it going.
Jason Plumb 00:01:34 Pretty good, pretty good.
Cesar Munoz 00:01:36 Maybe it's.
Hanson Ho 00:01:39 Jason. I was looking at your jank, pr! And a bunch of other commits got tagged with it, so it was difficult to isolate the changes I was going through one by one, and I don't know what happened.
Jason Plumb 00:01:52 Oh, yeah, I don't know what the F word happened with that, because, let's see, I think I referenced it from this one.
Yeah.
So.
Cesar Munoz 00:02:03 Rebased.
Jason Plumb 00:02:04 I rebased, but it went badly. I don't know what I did, but yeah it it got it got real bad on this commit.
Cesar Munoz 00:02:14 I think it rebates from a fork usually does this with. I think it's a Github issue to be honest.
Jason Plumb 00:02:21 Well in any way. This this pull request was not going very well anyway. So instead, if we want to revisit this, we certainly can. I feel like we do need to represent Cenk in some way. I think it's an important part of mobile ROM mobile instrumentation. We'll figure that out.
This green rectangle around the window I'm sharing keeps flashing, so let me know if there's any problems with my sharing alright. So the 1st item on the agenda. And please add agenda items if you wish and I'll just jump into the 1st one. So I put this in a few days ago. I don't think it's gotten any real attention yet, but this is A. This is in response to that jank semantic conventions. Pr, and as part of that discussion.
I think Cesar made a pretty good point, which is, if it looks like a metric.
and it walks like a metric, and it quacks like a metric. Maybe we should just use a metric instead of trying to let me find it.
Hanson Ho 00:03:33 So open a can of worms here.
Jason Plumb 00:03:34 Yeah, so okay, so and I think this person, Thompson Tomo, who has opened issues in both the Android Repo. And I think the semantic conventions repo, saying, Look, we need, we need some consistent, like real use of semantic inventions around some of this stuff. And like, what are these 0 duration events that I keep seeing like, you know, it's like open to these issues and noticing some real shortcomings. So They started chiming in on this one as well and have some opinions. And we're like, why don't we use a metric? So with with those 2 things, I'm like, okay, let's take a step back, plus the the fact that I screwed up whatever that rebase was. I'm like, what if we could use metrics and do it in a way that allowed us to emit stuff that was low cardinality. And we've we've talked about this before. The reason on Mobile. One of the reasons the cardinality is so high is because of sessions. But it's also because of a like unique device ecosystem. Right? You've got a hundred different models of telephone in people's hands running a bunch of different flavors of operating system on a bunch of different networks and blah blah! Blah, right? So there's all of these resource attributes. I'm like, well, how bad is it? What does it actually look like?
So here is what a resource attribute in our demo app out of the box looks like.
So a lot of this stuff is not high cardinality, right? Like the string android.
you know, providing little value. But also, you know, lets you identify that this re, that this came from an android app.
And OS, you know, it's going to be interesting if we ever see a combination of Android, and not Linux. But whatever I think, we're hard coding those. But someone else certainly doesn't have to.
Anyway. I, in looking at this, a lot of these are not high cardinality.
but some of them I figured we could drop. So I invented this harebrain thing which strips resource attributes from metrics, so it allows you to use metrics and strip down the resource attributes to some minimal set.
And what this does is it allows you to ingest metrics like for things like Jank. We could. We could certainly build Jank now, if if this if this lands, then we could build Jank as a histogram, for example.
which is great. That's how the data is provided to us from Android. In the 1st place, right? If you look at the implementation right now.
we basically get a histogram from the platform, and then we reduce it down to like these 2 things like above a threshold and above a different threshold.
And there's a little bit of code and a little bit of work involved in doing that. But if if this landed we could send a real histogram that would only identify these things.
So the fact that it's android. And then what version of the OS you're on and the name of your service now, that's real, real, minimal right? If I'm if I'm looking at my my rum providers aggregated dashboards, and I see that there's a certain I don't even have. I guess screen would probably be an attribute of the metric data points and not on the resource. But if I if I see that there's some jank happening with some histogram curve on some screen.
and I want to do something about it.
I'm not sure where to start. So prior to this jank effort prior to this pull request.
The idea was that if you're looking at a real user session, right? You're looking at a rum product, and you're seeing sort of their flow through an application that you could. You could demarcate times in which that user experienced jank or experienced slow rendering. You could tell where in their workflow they were, and that's for all the way down to a specific session.
And we used events for that. I mean, before events. We I mean, they're still implemented right now as 0 duration spans.
But the idea is that on on your rum, timeline, you could see those, and then that would be pretty actionable, because you could see what they did after experiencing Jank, or you could identify. Okay, in in these these 20 example sessions that I audited, lots of users experience jank around the same time. Maybe we need to do some optimization there. So that's a lot of words. I would ask that people look at this and give it some real consideration. I'm not convinced it's a good idea.
but it is what it is. So this I will just talk to the go ahead.
Yeah, please.
Cesar Munoz 00:08:16 Which is what?
Well, I just wanted to say that I don't see right now. I really don't see an issue with just removing some resources if I understood correctly. That's what you essentially, that's a a summary of what's done here is reducing the resources only for metrics.
Jason Plumb 00:08:39 Correct.
Cesar Munoz 00:08:42 I don't see an issue with it right now.
To be honest, I think it makes sense. What you what you said.
what I'm not sure is which ones should we keep, you know, if we do? If we did that.
Jason Plumb 00:08:57 So.
Cesar Munoz 00:08:57 For example.
Just one example. I noticed that one of the resources removed was manufacture rare name.
and I know back from when I why I used to develop boundary apps.
I know that it was kind of common to get issues from one manufacturer more than from others, even though they were using the same OS version, you know, and it usually was Samsung. I don't know why.
but I remember having issues only with Samsung and things like that. So I'm not sure if that's, you know.
helpful to give at least that one. Anyway, I don't know. I I as a as a general idea, I don't see an issue with it. But yeah, sorry, Hanson. I think you were. Gonna say something as well.
Hanson Ho 00:09:52 Yeah. So it's very attractive to look at Jank and say we should add this shit up But when it comes down to it. Even if you don't consider the hotel metrics aggregation requiring cardinality being an issue.
How do people want to use this?
It's totaling it up. Doesn't mean anything. Even if you look at screens, even if you look at device sessions, the runtime of the device depends on so many more things. So you're you're gluing together a bunch of things that are unrelated to get a number the way it's currently set up. When you see what happens before it happens and see it as it progresses. You know, in a timeline is how people use it.
So, even though it's attractive to look at. Screen drops or frame drops things like that, and to add them all up. These are a qualification in terms of magnitude for certain events. Users see freezes. That is an event.
Now the freeze could be one second 10 seconds, you know, 20 frames, 80 frames, whatever it is, that is metadata on the event of Jank.
So as a as a metric.
If you add these events up, it is the same as adding different errors and saying actually even more useless than that, because there's so much context embedded within what is causing it? And when it's happening, what is preceding it? What is after it? When a jank happens? What did the user do? Did the user close the app? Was there a crash like that's that's the important part.
So.
Jason Plumb 00:11:37 When I mean the the when gets lost. When you go to metrics, it's metrics are a contiguous data stream, and you're just reporting them over time, and hopefully, it's 0 most of the time, right? And then there's some interval, the default recording interval for metrics being 1 min.
There's a 1 min window in which you know it. It went non-zero for a while, and then it came back so like the and the histograms nice because you get granularity, but you don't actually know where in the app and what the user is doing. And I think it's a little bit I think it defeats some of the value of of having, like point in time, notification about this stuff.
Hanson Ho 00:12:16 Yeah. So I think the implementation is right in that. You can do this type of filtering to reduce the cardinality. But what you're effectively doing is turning it into mush. It's useless. This data cannot be used. No one looks at this data and says, Oh, yeah, by these dimensions that we could aggregate by things go up.
Why did a new version get introduced? So many versions should be in there? Oh, okay.
where there was an important feature that was shipped. That increased the ability for people to scroll. Because Jank only happens if you have a lot of a very specific type of rendering. So scrolling is basically janky.
Most other actions don't tend to be janky, they tend to be. They manifest differently. So this is capturing a very specific thing, and I think people focus on this because a lot of people who work on this stuff originally came from apps that scroll me being one of them, I wrote the listen to choreographers to count the number of drop frames because Twitter, Facebook pinterest all all these other they they care about Jank. But if you're if you're if you're a crud app jank is generally not a problem unless you're like rapidly scrolling so. And and Google also presents this jank metric. So people were like, Oh, yeah, Jank must be important. And people kind of, you know, went around it. But at the end of the day the implementation right now is what's useful. So if anything, we should standardize Jank as an event, and then add things like duration or frame drops as a as a metric. There's really not as much as as metadata in there.
Here's where it becomes a little bit interesting. It would be nice if we could add up metadata within an event, and kind of, you know.
Turn that into a metric.
But that is not part of hotel right now.
and I think, 1st standardizing a semantic convention around Jank as event, or even jank as a span, if you know when it started and when it ended you can record it as a span, but at the end of the day it's a thing that happens, and the temporal aspect is very important. So if our implementation currently uses logs or or uses a span, or uses a 0 degrees. Whatever it is.
we can figure that part out, but it ought to be one of those things, and the standardization should be towards a jank event. Users see a screen freeze.
When did they see it? What is the magnitude? How long did it take so which I think, Jason, you kind of came to that at the end. Right? Because I think at the end you were talking about. Yeah, I did this, and I'm like, I don't know. This doesn't seem like.
Jason Plumb 00:15:15 Oh, yeah, I know I'm not.
I'm not convinced. It's a great idea, but I wanted to at least put it out there, and so people could play with it or see what it looks like. Go ahead.
Cesar Munoz 00:15:25 So right. So I think this kind of discussion that what you just mentioned, Hanson, it's it's a discussion we did have in the Pr. That the Jason created first.st And the thing about the way that it was defined is that it was adding a number every time a frame was was not performing, you know, the way it should. So essentially it was a. It was a counter is something that we already have in matrix.
Also, the thing about logs is that you know they they the way it was looking is like every single frame that will have.
You know it. It will spend like a more time based on a threshold that is, on a constant that we define there as well.
Will will be counted as as one, you know.
slow rendering or I don't know what what the name a jank event. If you, if you will, will mean that you know how many frames are we talking about like in a regular app that can have this kind of situation, and how how much space or how much time it could be between those 2 events, and then the the the same issue of you know, cardinality that Jason is bringing up about about metrics.
and then it would also play out there for logs.
Because then we will be talking about at like a a huge amount of logs, just for one device.
because we don't know how many frames will be dropped in that device in a single screen in like a second, because I don't know how many frames we can. You can get per second. So is like, if if it's defined that way.
I think it should be a metric because of the whole.
because this is essentially will be a metric like the way it's defined. It will make more sense as a metric. One of the stuff that I mentioned in the Pr. I don't remember the exact words, but it was some somewhere along the lines of well, if we decide that, you know, within a second one Jank event happened based on our our criteria.
Let's say that within that second, you know. In reality they were. There were, I don't know.
10 frames that dropped over over the the threshold that we set. But let's say that because all of them happen within the same second, we would only send one event.
Jason Plumb 00:18:26 Correct.
Cesar Munoz 00:18:26 And probably we will say, Okay, well, there was a jack here like, and maybe we can take the value of the 1st event that happened during that second. Or maybe we can just take the the the amount of time of the the longest. Maybe I don't know. We can decide that later. But the point is like they wait.
It's defined that we need to count them all, and and we need to track them all and all the stuff at the end of the day. It all it kind of shapes as a metric.
in a way that it would be feasible and and and and not wasteful of of this phase, either. So.
but then we will have to redefine it, and and we will have to be kind of very opinionated, I would say on this kind of stuff, because.
you know, some people will come and say, Well, but I don't want to lose any kind of frame that was dropped. I want to know about them all things like that, and they will say, no. You just get one events telling you that a frame dropped. You don't know exactly which one I mean within that second, or may maybe within a minute a frame dropped, and that's the only event that you get, and there might be hundreds of frame drops within that same amount of time.
You just get one event. I think that will make sense. I think that will be useful. But the other thing is that at least not that I'm aware of.
We actually haven't gotten like somebody asking for something like this.
So it's kind of tricky to kind of guess, you know, because it's like, what do they need?
To me would be helpful. What you just what I just mentioned.
But then but then I wouldn't know details of what else to add, and the other stuff that this Pr. Had was that it was adding other attributes that you know. On the surface it looked like pretty good. I don't know contextual information, but I'm also not keen on the idea of just adding stuff for the sake of having more information, because then I see that I don't know how to deal with. I don't know the fact that maybe we decided to add an attribute within a type of data format that then in the future, we realize is not the right one. And then we're all breaking changes. Or maybe it's just adding, I don't know clutter or unusable data, and somebody complains, and it's gonna be difficult to remove it later that rather than having to add something that it's missing.
So so if we're gonna go with an event.
I think we will have to be very opinionated and probably start very simple, just adding the bare minimum stuff that we don't even know exactly what is needed, but just having very, very minimum stuff that we think might be useful, and then just wait for people to ask for more stuff. But this was like a lot of stuff, and it was like I don't know. I saw like a complicated approach which made sense as a metric.
But yeah, it makes sense. What you said, too. Is it like as a as a log event. We can get all that information. That's.
Jason Plumb 00:21:52 The best.
Cesar Munoz 00:21:52 And how they're gonna read it.
Jason Plumb 00:21:54 I want. I want to respond to some of that.
So what's proposed here is essentially what we're doing today already in Android, it's just really changing it from a 0 duration span to an event with a couple of changes as requested in this discussion. So when you were describing the bare minimum, the bare minimum. The only thing that's required is the number of times that the rendering exceeded some threshold. Ideally, you would also include the threshold right, because it might be helpful to know, like what what threshold was exceeded when I when this, when this happened, and there will be some sane defaults in every implementation. Maybe we could even evolve this into describing those same defaults, but depending on the platform.
But to me this, this felt pretty minimal. Right. It's it's an event, an account of the number of times you exceeded a threshold optionally, you can include the threshold. There was an ask for the period so like, how long like? And this is, this is a good point, because I think, Hanson, I think you asked for this. It was like a hundred slow renders over a second is much different than a hundred slow renders over a minute right? So the period in seconds for which you've sampled and our current implementation that is configurable.
We do poll the platform for these these values on an interval.
and so that maps over pretty nicely. And then the type. You know, we could throw the type out. I don't actually care about the type. It's just like.
Cesar Munoz 00:23:27 That's the one that I comment on. Yeah.
Jason Plumb 00:23:29 If you read the Google Documentation, they very clearly classify 2 types of Jank, and I wanted to make sure that that was accounted for here, because I assume that android developers reading these Google documentation will care about this. But we can throw a type out. I actually don't give a crap about type. So that's where this was coming from.
The as far as like being wasteful, or like high bandwidth or disk space. All of that.
it's not polling.
Presently I think we would have at worst 2 events per polling interval, which is currently defaulted to one second. And so, if the app is really, really misbehaving. We're gonna generate 2 events per second, which doesn't feel that bad to me.
And maybe you should fix your app. But that's what we're trying to help them do.
I guess.
Cesar Munoz 00:24:23 Events per second per device.
Jason Plumb 00:24:25 Yes, yeah, absolutely as far as aggregating. I think the thing that maybe has also not been mentioned, but I think needs needs to be worth calling out is that we're not currently expected to be including session id on metric data points. So when you get these metrics, they are not tied to a session. They're aggregated across all of your users, and you just have to go to like if you're looking at a real user session. And there's Jank. Those things are not tied together. There's a different screen in your product somewhere, that's gonna show you, you know, slow renders aggregated across some kind of arbitrarily chosen set of fields, attributes right so.
Cesar Munoz 00:25:14 That that's fair enough. But if if you go back to your Pr.
Jason Plumb 00:25:18 What's that?
Cesar Munoz 00:25:18 Point is, if you go back to your Pr.
Jason Plumb 00:25:21 This one.
Cesar Munoz 00:25:22 Yeah.
My point is, count, you know, count definitely something that you have in metrics.
Period of time.
Also something that you have in metrics. Actually, the default for Java is a minute. So you're just counting stuff and aggregating stuff locally for a minute before you start exporting stuff.
Hanson Ho 00:25:47 But that's not what this is.
Cesar Munoz 00:25:49 What is this? And.
Hanson Ho 00:25:52 This.
This? Well it is, but it's not done for aggregation. It's done for quantification. How badly is the jank happening during that period! The count, and the period allows you to kind of do some math to say, Oh, this is a big spike within, you know. A particular second, or this is spread out so.
Jason Plumb 00:26:17 I agree with Cesar on this one. I think the period is the same thing as like the metric polling interval, and this count is aggregated over that period. I think the difference is that we have, or this, this affords, the implementer a more customizable period, whereas the period is, I think per per meter provider.
Hanson Ho 00:26:37 Yeah.
Jason Plumb 00:26:37 It might even be per SDK. But, like the period in metrics, is like you, you get one period per meter provider.
Hanson Ho 00:26:44 And that means, if you want to have different periods for different things, you need to have different meter providers. So correct me. If so, go ahead.
Jason Plumb 00:26:52 No, and it might even be per SDK. I forget it. It's at least at the meter provider. It might be all the way up at the SDK.
Hanson Ho 00:27:00 So, as far as I know, the the period for a metric provider is done so that data could be chunked to be sent over in a reasonable manner.
Jason Plumb 00:27:11 Not could be. It is I mean, it's aggregated client side.
Hanson Ho 00:27:14 Right. So the reason why this exists is so that it could be chunked, and the period has no semantic meaning. It is like whatever whatever. However, the however, frequently you want to send the data, you just set the period versus the period here is effectively saying.
during this duration, I want to know how many of these things happen, and within that threshold.
given those 2 values, it is either perceivable, perceived as a problem or not perceived as a problem. So you would never want to even like, if your scale is able to do this, you never really want to have short, really, like really short periods nor really long periods. So there's a function to the period for this versus the other one. The function is more meta, more about scale and.
Jason Plumb 00:28:03 Is user centric like it needs to.
because we're dealing with human perception here. It's not just like a meter that's like sending us a continuous signal. It's like over this perceivable time. Also, you know, the time in which a user can do some stuff in an app right. There's only a limited number of things you're gonna do in one second.
Hanson Ho 00:28:22 So I'm probably missing some context. I hadn't read through the entire Pr, so I'll do that. But I feel pretty strongly about this about that. This is not an hotel metric as it is now. It can be an hotel metric. If we could start putting basically everything in the resource. So if we could start aggregating by a user device, Id and a session.
Then it becomes a bit more meaningful as a metric. Assuming these, the the actual samples could also be.
could also be a time dimension. But if if the sample itself cannot have a time dimension, then a lot of what this is going to be used for will be blown away. So even if you aggregate by everything here which should probably include app version, device, id session, id screen things that just gonna it's gonna blow out the cardinality even within the device. Id, it's going to have a bunch of different histograms potentially.
So even so, there's like 5 different things. Why, it doesn't make sense. As a hotel metric.
We could talk about one of them, but there's still the other 4. So if if the Pr. Is trying to do too much, maybe we can slim it down. But I think the original thing that you had that I looked at a long time ago that forgot about the comments I even made as as a thing that happens stapled to a time. So whether it's a span. Whether it's an event. I don't care that much. They could be both, but it should have a time dimension, and that's the most important part.
If if we want to do something that that counts and aggregates, basically using the same underlying data to produce some sort of aggregateable metric that is independent from the the events. That that we're gonna fire with this, that up to be a separate instrumentation, because you're trying to do different things. Because if we're trying to do like contextualize a user session. And you don't have a time component. That is a deal breaker.
Cesar Munoz 00:30:38 Got it. So okay, if I understood correctly, it could be a metric. But it doesn't work well as such, because it doesn't have all the contextual information that will be helpful. For you know, later.
you know, relating this data with the with with other stuff.
That's that's that's a fair point the in in terms of these other Pr.
How does log event avoid this issue?
Hanson Ho 00:31:14 Log of it has a timestamp, you know, when it happened.
Jason Plumb 00:31:18 And it has a session.
Hanson Ho 00:31:19 Yeah.
Jason Plumb 00:31:21 They're not called out explicitly here because they're like they're assumed to be part of every event. Every span generated from mobile telemetry.
Hanson Ho 00:31:29 It is. It is a basically a a property of no, no pun intended, but of of the signal that we choose. It's almost like, Do you need to know when this happened? And you answer, yes.
then metrics, as we currently understand it in hotel, is inappropriate.
because, you know, a jank happening in the beginning of the session, happening at the end of the session, happening before some other event or after one other event is crucial to understanding and using it. Yeah.
Cesar Munoz 00:32:01 No, I think that's completely.
Jason Plumb 00:32:02 I don't think that's really fair, because.
Cesar Munoz 00:32:05 I like. I like the idea of seeing there was a jack here in this screen, and when the user I don't know clicked on this.
What? I really probably not. I don't know if it if it is that I don't know, maybe that I probably didn't properly understood understand from from from this proposal was.
what I really don't like is the idea of of having to, you know, send hundreds of log events in in general, you know, just for a single app, just because it's installed in different devices. And then, now we're gonna get. I don't know a million log events in in an hour, because we're our app is big. And then we we and we have a lot of junk events.
which might be because of stuff that probably is quite ex expectable in some cases which is like scrolling or things like that. So it's like I, unless we set like a limit of. I don't know one junk event per.
I don't know. Mean it.
Jason Plumb 00:33:13 I don't think that this.
Cesar Munoz 00:33:14 And I wouldn't.
Jason Plumb 00:33:15 Sorry to jump in, but I don't think this prevents us from like limiting in implementations like some maximum verbosity like we could, we could certainly, in the implementation set limits, and this could be expanded on to say, like, Look, don't send a gazillion of these or implementation should. But this is, you know, we're trying to like, just get the shape of the event first, st before we talk about implementation.
Hanson Ho 00:33:37 So so the.
Cesar Munoz 00:33:38 Giving a lot of a lot of flexibility upfront, you know, and it's like where it's gonna be difficult to remove that in the future rather than just being very opinionated. And then, you know.
Hanson Ho 00:33:52 So I think we should probably separate this Pr into 2. 1 is just a semantic invention, devoid of implementation, and the other is is, whatever change the inflation we want to make, because so I definitely think there should be some throttling. There should be some throttling, I think, overall here, but the idea is that, Jank, you're not recording all instances of jank anytime. There's 3 drop frames. You record it. No, no, you want to. You want to record Jank, that is impactful that you feel like you want to include as something extraordinary.
So if you're using low end devices, and there's a lot of scrolling. There's always gonna be Jank. It's it's it's not preventable.
Cesar Munoz 00:34:32 Yeah.
Hanson Ho 00:34:32 What you want to do is look at the Delta, or look at Jank when it's unexpected. So the threshold that we define, I think will give. Sorry. We, as in like the Santa Convention defines, will give the ability to basically ratchet that up to basically get the data down to a place where it has to exceed a fairly high bar in order for that to be recorded. But if if it happens that it just keeps on doing this. If it's frozen, then it's just gonna spit out events. And maybe the instrumentation will basically say, if we have 5 contiguous events, or if an A and R is happening. So we know the screen is frozen, you know. Don't admit all those events. Emit something else, or throttle, or something like that. So there are means that we could do things that we could do in the instrumentation to basically address some of these concerns. But the semantic convention, I think just has to be flexible enough so that we could. We could, you know, describe what is happening in the event, and I think what I saw briefly. There, I think it does. I think that's probably as good to go. As for the.
Cesar Munoz 00:35:40 So we're gonna so we're gonna essentially give a lot of responsibility to the implementation of making these feasible events. I guess in a way, if that's what I understood.
Hanson Ho 00:35:53 Yeah, yeah, like, like, I mean, we, we could stop. We could put stuff like recommendation, like up atop and say, like, you know, don't fire every don't fire at one of these events, for every frame that's dropped, because, you know, you plug it in. It's going to be ridiculous.
and so think.
Jason Plumb 00:36:08 I think right now, there's basically like no spec around like mobile Api or anything. So I think there's some opportunity to start introducing some of that, and like start describing some behaviors. But you know, that's I think I I think, that the implementation is still a separate concern. I mean, they're of course they're related, and of course 1 1 affects the other. But, like I I really would just was bait like my whole goal in doing this was to take our our 0 duration span, which was called out by a user. I will like recently by a user and just turn that into an event. And I was like, Oh, we don't have semantic convention around that. Let me try and make one based on what we're doing today. And that's kind of how we ended up here. I want to do a little bit of time check.
Cesar Munoz 00:36:48 I didn't know I didn't know. It's something that the android already had. So so yeah, essentially, you're just trying to totally copy and paste that here and in a semantic convention.
Jason Plumb 00:36:59 Totally.
Cesar Munoz 00:36:59 So, yeah, I I.
Jason Plumb 00:37:00 Take a look at the correct implementation and what it provides. And the implementation is like, pretty basic. You know, it's it's 2 classes. So have a look at that and look at what it does and how it really pretty simple it is.
I do want to do a time check. And I wanna also give room for the other voices on this call to chime in on this topic before we move on. So if if anybody else here wants to jump in. Now's a pause from the 3 of us.
and you don't have to.
If you're just over there eating popcorn, it's also good.
Hanson Ho 00:37:39 So early, for oh, no, wait! It could be the afternoon for some of you.
Jason Plumb 00:37:43 Okay?
Well, in the interest. I mean, I feel like we haven't come to resolution on this. But please take a look at this pull request and give some considerations to this. I think I'm going to just right now. I'm just gonna make this a draft.
because it's I think I'm scared of it, so.
Cesar Munoz 00:38:03 So yeah, don't.
Hanson Ho 00:38:04 Don't! Don't merge that.
Jason Plumb 00:38:06 It's.
Hanson Ho 00:38:06 Yeah.
Jason Plumb 00:38:07 But I'm glad I'm glad we got a chance to talk about this and some of the some of the ramifications of the 2 approaches. And you know, I think this might be a topic for the client Sig next week as well. It's I mean, we've clearly spent 40 min on it already. We're gonna blow away that whole meeting.
Cesar Munoz 00:38:26 40 min!
Jason Plumb 00:38:27 Talk about this again. Yeah, it's been 40.
Didn't realize it. Yeah, I know.
Hanson Ho 00:38:32 That we can burn.
Cesar Munoz 00:38:32 It was a fun conversation. You see that?
Okay.
Jason Plumb 00:38:37 So I want to move on, and that we discuss other stuff. So, this is happening. This is kind of a little bit of housekeeping here.
Hanson Ho 00:38:47 Again.
So the permissions for the Github token changed. This is in the community, repo, right? So.
Jason Plumb 00:38:58 right now. It currently has read and write, and so it will be restricted. And there's a there's a larger security effort happening across all of open telemetry to sort of do best practices work that limits the blast radius and tries to limit the possibilities. For, you know, supply chain attacks. This being one of them.
So the Github Token right is owned by opentelemetry, and right now any workflows have permission. This changes the default to being read. Only so. Most of the workflows in all of opentelemetry don't need right access to the repo but you can still per workflow specify that it does need permissions, like, I think.
Let's see, is there an example, anyway?
Cesar Munoz 00:39:54 It's only changing the default. So so it's fine. If we need the right permissions.
Jason Plumb 00:40:00 So that's my. That's my question is, I think the answer is probably yes.
And then which workflows. So this is the thing I don't. I don't remember, or I'm not. It's not clear to me right now, is which of our workflows.
Cesar Munoz 00:40:16 Didn't trust. Create a Pr. Already in address.
Jason Plumb 00:40:19 It's the same thing because he's doing a ton of stuff. Maybe I I merged one yesterday, but I don't think it was about the token. It was this one that I merged yesterday.
Different issue.
Hanson Ho 00:40:29 5.
Cesar Munoz 00:40:30 Yeah.
Jason Plumb 00:40:31 The name of the bot is changing, and then there's also permission stuff related to that. But I don't think that it was related to the token. Was it?
He did, or someone did the Github Bot did.
Hanson Ho 00:40:49 2 weeks ago.
Jason Plumb 00:40:50 Okay, well, I'm sure it's related.
So okay, so it took away right.
Hanson Ho 00:40:58 Oh!
Jason Plumb 00:40:59 In.
Cesar Munoz 00:41:00 That's default.
Jason Plumb 00:41:00 Build, and added it just on the notification that's good. So this is an example of like constraining the the permissions down right? So it used to have right for every step in the jobs, and now it only has right when it needs to create the notification that's great.
And so this bot must have gone through and done that work already. Okay.
thank you for talking this through with me.
Cesar Munoz 00:41:30 And, thanks to Trask, if he's watching a recording.
Jason Plumb 00:41:37 Okay.
I think that answers that. I think I think I think we're not concerned. I'm no, I'm no longer concerned about this. I think we're good.
and if something breaks just, I mean, I guess we're now aware of this, and you know we can address it when that if and when that comes up. Okay.
next thing, Mustafa is asking about the Android SDK, and whether it should be a Singleton. And I kind of like quickly put in the word. Yes. But where are you coming from?
Mustafa Haddara 00:42:08 Yeah. So I was talking to users yesterday, using our honey, our SDK, which which uses the Android SDK, and they have a span processor that like hooks into some stuff in their dependency injection system. And so anytime the user logs out, they want to tear everything down and then recreate it.
and.
Jason Plumb 00:42:36 Okay, interesting.
Mustafa Haddara 00:42:38 So there's there's no like. There's no like shutdown mechanism that they found on the Android SDK. And so they're trying to just like create a new instance of the Android SDK. And then they're getting errors because it's already been initialized.
Yeah, so we could come at this as like, oh, is this supposed to be a Singleton? Yes, okay. So then I think we need. And I can. I was. I can open like issues and and write this up formally, but I wanted to talk it through 1st of of like, oh, is it a problem that it's erroring? Or do we need like an explicit shutdown mechanism to tear things down so that they can properly recreate it.
Jason Plumb 00:43:20 Oh, that's so. That's super interesting.
Cesar Munoz 00:43:22 It. Is it like? I will say that.
as far as I'm aware, we haven't don any specific word towards making it closeable if you will.
but personally I think we should. I mean I I think it should be something that you can close and and create a new one, and there shouldn't be an issue. That's there'll be new on it.
Hanson Ho 00:43:50 The the problem. There's a couple of problems. One is that telemetry could be recording. What do you do when you are in the middle of a span, or things are delayed. You are.
you know, you've recorded it, but it hasn't gone through the exporter. There's a whole bunch of edge cases to this. So the embrace Se, for instance, initially, was stoppable and restartable. But there are so many weird edge cases, especially for things that we had to do Biko instrumentation, for there's a ton of like state checks that happened.
So what we ended up basically doing is, I mean, the Hotel SDK itself is very much built around the Singleton notion.
So for us.
the process is tied to the instance of the SDK. If you want a different instance. Well, you gotta kill the process because it's very useful to tie those 2 things together. So, Mustafa, for your customer when they're talking about tearing the SDK down. Is it because they want to change the resource that they want to tear it down, or there's something else.
Jason Plumb 00:44:59 They want to inject processors is what it sounds like.
Mustafa Haddara 00:45:03 Exactly. So. The specific example is, they wanna inject a new span processor. Their spam processor hooks into something else that like pulls in their like business specific user id, and when you log out, you're gonna not have that same user logged in. So you wanna remove that And then if a different user logs in, you're gonna have a new store or whatever, and they need to hook up a new spam processor to to re into. That gets the new one re-injected. Yeah, thanks.
Hanson Ho 00:45:32 Got it. So so there's some hard coded logic in the spam processor instance that they have that needs to be re initialized at some point, you know, whatever it's user, log out, whatever it is. Is there another way for them to just do it in in an indirect manner, have a delegate, and basically kill a delegate.
Mustafa Haddara 00:45:50 Yeah, that's the workaround that like I was discussing with them. But I wanted to figure out in this setting. You know, whether this was intentional, and it is, and what the limitations were. Okay. There's no like a bunch of edge cases like you brought up and.
Cesar Munoz 00:46:08 To be another thing. We really haven't thought much about it, honestly.
Oh, yeah. Wouldn't exactly solve it.
Hanson Ho 00:46:15 1st time it's come up as far as I. As far as I know.
Cesar Munoz 00:46:18 Yeah, so so so it's a, it's a good, you know. It's a great topic to be honest, because it's like, well, we have the opportunity to spend another 40 min we can today. But.
Hanson Ho 00:46:29 You know.
Cesar Munoz 00:46:29 Discussing. I I really like the idea of being able to close it and to your to your comment earlier, Hansen, what will happen if there's a span ongoing or stuff like that.
to be honest, I I don't know. But the thing is like my understanding is that everything in the Java SDK is designed to be closed.
There are. I would just I would just close it. And then, whatever the SDK the job SDK decides for those remaining spam. So you know that will be the SDK behavior.
Hanson Ho 00:47:01 The the problem.
Jason Plumb 00:47:01 Certainly challenges around instrumentation, though, like like, we're calling like install on a bunch of instrumentations. Now, we want to call like uninstall. We don't have that notion at all yet.
Hanson Ho 00:47:12 There's it's also done asynchronously. And and the fact that you're injecting a bunch of stuff at the different levels. So unless you're able to be like, Okay, I'm stopping now. So for for this period of time, until everybody tells me you're stopped. I'm not recording telemetry.
If if you want to do that. Then I think that's okay. But you you lose telemetry, and, in fact, and I think the work the delegate pattern is something we already do like the way we do. Session injection in the spam processor is effectively this, there's a mutable thing that we reference, and the processor itself isn't hard coded to it. It's hard it points to a delegate. You can change the delegate, and therefore the delegate will do you know the right thing. You can make the delegate a spam processor.
you know, and and then, you know, at least, their code doesn't change. But at the end of the day it's it's it's about managing.
Cesar Munoz 00:48:08 For for this. For this use case, I agree the delegate pattern should be the best option that that's like. Generally speaking, though I'm I'm talking about the fact that it should be close able. The the agent. I think it should. Maybe we don't have to do it right now, but, like. Generally speaking, I think it should be closable, and I know that like not send in telemetry because you close it.
I know that that's possible. That's that's 2 of them, and I will expect that if a user calls close they they should know that, you know they won't get any more telemetry because of that. So it is. But yeah, for your use case. Mustafa. Yeah, I think the the delegator pattern. It's it's it's yeah.
Jason Plumb 00:48:58 I'm I'm curious if you can give any more details about what was happening when they're currently calling shutdown or what they're what they're trying to do that was causing errors like, are, have they.
Mustafa Haddara 00:49:07 Yeah.
Jason Plumb 00:49:07 Have they tried calling close in the open telemetry instance.
Mustafa Haddara 00:49:12 I don't. I don't know exactly what open telemetry things they're calling when they shut down. They basically said, Oh, we're using this dependency injection framework. They're using dagger and they have.
They have it set up so that when their users log out they recreate their entire dependency tree. Everything that daggers and managing is gonna get torn down and reinitialized, and they were hitting. I could paste in the stack trace that they pasted to me.
Which was this coming? This actually is coming from the disk exporter.
So they were recreating a new instance of the open telemetry. SDK.
Jason Plumb 00:50:00 Yeah.
Mustafa Haddara 00:50:00 Setting up all of their processors and exporters and whatnot. And then this was the stack trace that they were getting. This was not the one I was expecting them to see, because.
Jason Plumb 00:50:11 Put this in the Doc.
Mustafa Haddara 00:50:13 Sure go for it.
I was looking at the Hotel Java SDK library, and there's an open issue on that repo about Java being the that SDK being a Singleton, and there's like an explicit catch for it much earlier in the tree like it's not tied to a specific exporter. So I I was surprised, Jason, when you wrote the Java SDK is definitely closable, and would allow creating several instances, because from what I can see, that thing is is definitely
Hanson Ho 00:50:47 So, Singleton.
we can have a Singleton and make the internal implementation replaceable. So those are those are so from from the user's perspective, it's a Singleton. But internally, when we close, we basically recreate the instance. So that's probably possible. So what you're seeing may just be something in the android package that is, making certain assumptions that it probably shouldn't. But I would suspect that they're going to get issues down the line, maybe more subtle issues if if they go with the the what they are currently doing like, I would definitely recommend a delegate. But I guess on on our side we may want to take a look at this as well in order to to figure out what's going on, because we should be as single tinny as as the Java SDK, if that means anything.
Jason Plumb 00:51:37 Challenge is that the Ap. The interface? The open telemetry interface does not expose it.
but the SDK does like. There's a shutdown. It's public, you know, on the open telemetry. SDK, the the thing is, we don't expose the SDK, because we don't want to like most users should not be interacting with the SDK, they should be interacting with the Apis.
So there's a there's a disconnect there. We Android definitely uses the we use the SDK in several places.
because we're considered in like an implementation. We don't purely cleanly go through the Apis.
Hanson Ho 00:52:16 But we don't ever call shutdown right? So there's no.
Jason Plumb 00:52:19 No, no, and we don't expose any means of doing that.
It is. It is. Yeah, we. I mean, there's a bunch of stuff we'd have to shut down. The the thing that is reading from the buffered data on disk would also have to be shut down. So it doesn't try and read stuff and export to a system that has no exporters anymore. Like, there's a bunch of subtleties there.
Yeah, it's a real.
Cesar Munoz 00:52:42 It will be a lot of it will be a lot of work.
Hanson Ho 00:52:45 Yeah.
Jason Plumb 00:52:45 Use case there. There was a discussion like a year ago in the client Sig, about the distinction between real user monitoring and application monitoring. And what a user session is, and is it an application session? And this kind of touches on that a little bit too right.
Hanson Ho 00:53:04 What? What? When a user logs out, what happens is there should probably be a new session created. But the underlying SDK should be agnostic to that, and it should have a session provider. It says, What's my session?
Jason Plumb 00:53:14 Yeah. And people have asked for a way to to to roll the session.
for I think for this reason.
Mustafa Haddara 00:53:20 Yeah, this this would be a big reason to rule a session as well.
Use that.
Hanson Ho 00:53:25 A session is a really really cool and useful abstraction to have at an Api level.
Cesar Munoz 00:53:35 By the way.
people should not be able to provide their own session ids and change it whenever they want to. So.
Jason Plumb 00:53:42 This one.
Cesar Munoz 00:53:42 To mention it.
Hanson Ho 00:53:43 Oh!
So. So I think I think fundamentally the your customer probably should tie stuff to the session and not to the application instance. So instead of expecting the entire and, in fact, if we don't expose a call to shut down, it'd be interesting what your customer was doing to to try to shut, to do what they think would be a shutdown.
because the Api, at least on the Api level, the Android package doesn't, doesn't expose that.
Cesar Munoz 00:54:17 But this issue is about global open telemetry.
Jason Plumb 00:54:19 Yeah, this is, this is slightly different. But yeah, there is. There is a side effect right now.
In that you can make as many open telemetry instances as you want. But there's only one global open telemetry.
Cesar Munoz 00:54:32 It might, only said it once.
Jason Plumb 00:54:33 Yeah, it can only get set once. And it it might actually like this SDK, builder build might actually complain if you've done that before. I forget.
Mustafa Haddara 00:54:44 I think.
Jason Plumb 00:54:45 That's good.
Mustafa Haddara 00:54:46 Registered global that hits this.
Cesar Munoz 00:54:50 Okay. Yeah, okay.
Hanson Ho 00:54:52 Yep.
Jason Plumb 00:54:53 Yeah, that this one, yeah, is there build with, is there build without register.
Cesar Munoz 00:54:59 That's yeah.
That's just the bill one.
the the I know that in in upstream Java. SDK, they don't like global open telemetry.
yeah, you should causes trouble, because some instrumentations might want to get the open directory instance from there, and if they call, get before the initialized, then they will, initializing No. OP. Instance, and then that will be it for the rest of the applications, you know, for the rest of the process. So it it I I don't. I really like. Generally speaking, I don't think single tons like a proper single ton. It's it's like generally a good idea, you know, to have.
Hanson Ho 00:55:46 So Singletons are useful. If you want to have an easy way to reference it. I think the problem is not Singleton. The concept is the implementation of that Singleton with the static and basically lazy Init. So if it's not initialized, you call it, and it that, I think, is the problematic thing. If you have a way to gate access to the Singleton, that shouldn't be a problem. And with dagger, theoretically, you don't even have to worry about that the Singleton could be injected at the very top of the graph and get persisted throughout. I think what they're trying to do is reset something that is fundamentally not resettable. An Api perspective. The Android SDK, the Android package is not resettable.
And I suspect the reset for for Core Hotel might actually be if we're testing rather than rather than runtime, you know, needing to recreate the instance. I suspect.
Jason Plumb 00:56:42 So I think that this.
I think this topic is worthy of an issue. I think, having an issue in place, will allow people to upvote it and or comment, hey, I want this, too, and we'll see where it goes.
Because this is the 1st time I've heard of it, and there are workarounds. I'm not inclined to prioritize this, but I think having an issue would be good, Mustafa. If you want to file one, I think that would be awesome.
Cesar Munoz 00:57:07 It. Probably just wanna mention it probably might even be something useful upstream, too, you know, because at some point I'm guessing you know, if remote configuration via opamp is added upstream.
Probably there's gonna be we were, we're gonna need of of of. We're gonna need a way of, you know, changing. I don't know processors and and parameters and and whatnot at Runtime, and maybe the upstream core SDK will have to support that. So so maybe that's even.
There's even a you know, a a bigger talk to have. It's it's it's very interesting.
Mustafa Haddara 00:57:54 So I guess what I'm what I'm hearing here is like.
yes, it's intended to be a Singleton. The feature request like I could have opened an issue that was like, Oh, I can't. I can't re initialize it. But then that's just gonna be like, no, this is the intent. And so the issue needs to be framed, as there is no way to tear this thing down or reset it before, in order to start up a new one.
Jason Plumb 00:58:18 And and what the issue would be like. Can we build this like? What would it take for us to have this and do.
Mustafa Haddara 00:58:23 And and yeah, work is it gonna be.
Jason Plumb 00:58:26 Yeah, are you? Are you okay with me asking you to file that.
Mustafa Haddara 00:58:30 Yeah.
Jason Plumb 00:58:31 Okay, I can definitely do that.
Okay.
Mustafa Haddara 00:58:33 Yep.
Hanson Ho 00:58:34 Exposing a call to to that method is easy, but dealing with the fallout is.
Mustafa Haddara 00:58:40 Absolutely.
Hanson Ho 00:58:41 I think so. So if you, if you tell your customer that that this is not a workaround, this is what we do on android already. They should. They should be amenable hopefully to to making the change, because eventually they do. Wanna if if we have a more robust session Api this would be something that they might want to tie to a session or other people.
Yeah, want to do this as well. So.
Mustafa Haddara 00:59:04 The the vibe I got from them was not, oh, the like! The hotel side of things fine, whatever they can work with it just the way their code base is structured with dagger and the inject like they were like, oh, on our side, this is gonna be really janky. And so if there was a better solution, it'd be nice. I don't think there is and so they're just gonna have to deal with it.
Hanson Ho 00:59:27 The app. The application graph will effectively initialize the delegate, which will then be added to the okay hotel instance that will have to be, get, get the the changes. So if if that effectively has a has a settable dependency or a a setable provider that effectively gets the the chunk of the data.
Mustafa Haddara 00:59:48 Yeah.
Hanson Ho 00:59:48 That then you call they should be you should. They shouldn't need to do anything weird. All they have to do is when they do the switch. Get access to the Singleton already with the delegate and call set.
and then they should blow it up. So I.
Mustafa Haddara 01:00:04 Yeah.
Hanson Ho 01:00:05 I, alright.
Any. Yeah.
Jason Plumb 01:00:07 We're at time. Please review open Prs and add comments and approvals, or whatever is needed. I appreciate everyone being here.
Mustafa Haddara 01:00:16 Thank you.
Jason Plumb 01:00:17 That hour flew by.
Alright! Take care!
Cesar Munoz 01:00:21 Bye.
