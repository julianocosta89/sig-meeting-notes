SIG: Android SIG
Date: 2025-07-29
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/jSGf8K25Y-U_x2onlgLcNy3P_VMxbJT-m7-k__Pyjm7kYE1UumcP1B2mSRRWyUE.Tju42IXOfT6stTu-
============================================================

## Zoom Recording Transcript

Jason Plumb 00:01:32 Good morning, west, coast.
Hanson Ho 00:01:34 Yeah. Hello.
Jason Plumb 00:01:36 West coast is the best coast.
Hanson Ho 00:01:39 Yeah, it's gonna be a hot ghost this week, though.
Jason Plumb 00:01:43 Yeah, I think we're hitting 90 today.
Hanson Ho 00:01:46 Goof.
Jason Plumb 00:01:46 Which is what? 32.
Hanson Ho 00:01:49 Yep.
Jason Plumb 00:01:50 North of 32.
Hanson Ho 00:01:53 Yeah, it's UN. When it starts with a 9. It's like when it starts with a 3. It's just it's it's uncomfortable.
Jason Plumb 00:02:03 Yeah.
we'll give it another few seconds in case people are trickling in. There's Cesar.
Cesar Munoz 00:02:18 Hello!
Hanson Ho 00:02:19 Hey!
Jason Plumb 00:02:21 Bean still waking up over here.
Yeah. I wanted to start off by saying, thanks for all of the work around the build enhancements.
yeah, that seems to be a considerable improvement down from 40 min or something to like 20.
So yeah, much appreciated. Thank you. Experts.
I wanted to move on from that and say that I noticed over the last week or so since we last met.
3 issues that are kind of related to each other. One of them is something that Mustafa brought up last week.
Which I'll just start out with this one and maybe they're related. Maybe they're not, we'll see. But I think I think that he was working with a customer, and they wanted to be able to shut down the span processor, basically reboot strap the SDK again with a different span processor because they're doing some custom stuff when the user logs in and it's not currently possible. And then this other request came up about supporting multiple rum instances. And actually, I'm kind of going out of order. I think I think this one was next.
yeah, I've got these out of order. This one came in next open by 50 cent and so they want to be able to change the endpoint, and or Api token right. So I think some vendors have an Api token that rotates every end, requests, or every end days, and so on on like one of your last sends. It might give you some other data back, or maybe you periodically pull a new Api token. Or maybe there's some mechanism, for, like load balancing, whatever it is, they need to be able to change their exporter.
And then this person came in after and said, yeah, I have the same kind of problem. I want to have multiple ROM instances. So they're they're just trying to use the either the initializer or the builder. I'm not sure which.
It looks like. They're using the builder directly.
and they're trying to do it more than once.
And it's blowing up, and it's blowing up in disk buffering.
And it's not really surprising because these were not. These 3 use cases were not something that we had ever designed for.
And so mostly I just wanted to bring up this as a question as to what we think of it.
Do we think it's a good idea in general, should we allow people to do this? Is it a goal that we should work toward? And then with that in mind, I mean, I I think it. It's a little I'd be hard pressed to recommend to a user building an app, to make a bunch of instances of open telemetry rum. It's not incredibly lightweight, and I think there's some pitfalls there. So I'm just curious what people think about this.
I have an opinion, but I want to hear what people's opinion is. First.st
Hanson Ho 00:05:31 So I think I think these are. These are separate. But these are related but separate. I think the the multiple instances that's almost like a definite no just because there's the Java SDK, or, frankly, any SDK, there's too many implications of there only being one and also when you're capturing telemetry, it's it's expensive sometimes to to kind of listen to these and platform calls, and for disk buffering, and for other things you don't expect there to be multiple and the use cases to work around to support multiple. It's not impossible. But I think the utility will be very low for how much work it would be, and how potentially, you know, bugs there are.
With respect to the other 2. I think unless I'm missing something.
delegate patterns could probably be used for changing the state of like the URL that gets requested or or tokens things like that. We have patterns throughout that uses suppliers, and I feel that that is the recommended idiom. And so for any time you have to rotate anything, even if it's a spam processor, or or you know.
I think you could use that pattern to solve it.
shutdown is interesting, and we reinstantiation.
that's the case that I think we may want to look at, if if nothing else, just to to clean up things a bit.
I think in theory, if the SDK Java SDK supports shutdown.
we should do no worse now. We may not recommend it because there's a whole bunch of issues when you're shutting down, you know telemetry collection. But at least for testing that should be something that's possible. So I think of the 3 I would, I would probably look into to that 1st one and and see what the issues are. But for the other 2. I think it's either explicitly no, or you could do it this other way.
Jason Plumb 00:07:54 Okay, thanks for sharing that, Hanson. What else do people think.
Mustafa Haddara 00:08:00 Yeah, I'm just looking at that last one now, and it seems very similar to the the 1st one, the one I opened a few a couple of weeks ago, where?
Jason Plumb 00:08:09 This one.
Mustafa Haddara 00:08:11 The yeah, they wanna update. No, no. The 1st 1 1st tab you have update exporter after initialization.
Jason Plumb 00:08:16 This one. Okay? So I was like one of these, I was like, it might even be your customer.
Mustafa Haddara 00:08:22 Yeah, I don't know if it is. They haven't told me that they're doing this. But it's it's basically the same use case right? Like it's we have some config that's changing at Runtime that we we are going to change after the fact. And I think it's it's coming up. Enough that we need to figure out how to support it. Whether that is yeah. You're gonna do a full shutdown and restart, or some of these classes and configs are, gonna be a little more mutable.
I think we need to pick one direction and and go with it. But it is definitely a use case.
Hanson Ho 00:09:04 So are the things that are modified part of the resource, or are they? Are they not.
Mustafa Haddara 00:09:12 Well, the in this case it was like here they're talking about. Oh, Api key endpoints.
in. In my customer's case it was like user id user. Id, I think, would be an attribute like a span attribute, not a resource attribute.
Hanson Ho 00:09:36 Can you feed? Yeah, it. It could eventually be an entity. But that's that's we don't have that yet. Can you feed it a supplier and then basically change it at the supplying source.
so that you don't explicitly pass in the hard coded Id or key, or URL or token, and basically just say, Hey, you know, every time you need it, you know, get supplier. You can even have some cachings if it's expensive to get, or something like that, but that could probably be built at the at the app level. And and or yeah, well, the app or or your distribution level rather than having to restart everything because you're basically you'll be lose. Well, yeah, I'll stop there.
Mustafa Haddara 00:10:21 I mean, I think the supplier pattern is a good pattern, but if we want to encourage that, then we would need to feed that through a bunch of the standard exporters and and whatnot that.
or at least provide a sample.
Jason Plumb 00:10:38 There was.
Mustafa Haddara 00:10:39 If you need. Yeah. Sorry.
Jason Plumb 00:10:40 Spilling over a little bit into my next topic, because when I was looking at this, I was like.
I wanna recommend they have some sort of delegating exporter. And then I looked, and I was like, Wait, we have one. It's just internal users can't use this, anyway. I put together this really simple example to kind of show them what they could do. And it's just this, the main thing is the swappable order, and all it does is, take a delegate, and as a swap function shuts down the existing one and sets the new one right. So if you, if you had this class available. It's easy to tuck in any of your own exporters, and anytime you want and swap where it goes there. There's a little bit of subtlety, though, because it needs to be on the outbound leg. Right? This needs to be the exporter that's wired up. The wiring here is actually, I think, quite complicated inside of open telemetry. Run, builder, because we have an exporter that's going to disk. Then we have another one that's coming back and reading off of disk and then delegating to. Presumably it would be this thing which is then going out.
Otlph, or whatever. But the wiring of this also needs to be pointed out that like, you can know if you're doing this, you have to use the builder like. There's no way to plug in your own exporter directly, right? Because the purpose of the initializer is to like do the same reasonable, easy defaults that most users we think want.
And so if you're gonna do this special case.
weird, swappable, exporter thing you have to use the builder, which is fine. But what's not shown here is probably another 30 lines of configuration, right? So like, if you're gonna do this, you probably have a lot more code that's in here. So so I did that for them. But you know, we could maybe make that use case easier if it keeps coming up. I just wanted us to think it be thinking about that.
cleverchuk 00:12:22 I'll I'll I'll ask the question. So is there like any technical limitation to be able to like? Allow them being able to like recreate the room, because, like in mobile things that like should be easy to like, tear down and recreate it. Think of like android activities and stuff.
I, those things get killed every single time. So so are we just like trying to limit the ability to like recreate this thing just based on an opinion? Or is it like a actual technical limitation on doing that.
Hanson Ho 00:13:00 Well, the application doesn't killed share preferences. There's a whole bunch of things that are effectively Singletons. Activities are part of the life cycle. So yeah, those are fairly discardable. So whether the SDK, you know, is one or the other is hard to say.
But I think that goes to the 1st point I was making, which is, we should do what the SDK. Is supposed to do. If if the SDK. Allows for a public resetting and reinitialization, there's no reason why we shouldn't allow that caveat issues. I think the problem Mustafa and his customers are having. That's I think it's a separate issue that we should, you should figure out how to fix whether it's exposing the swappable exporter or encouraging the supplier pattern in a more fundamental way.
I think you know what Jason has is probably the easiest thing right now. You can control everything by swapping in a new instance. You gotta make sure you shut down orderly and all that fun stuff. But you know.
it's up to you.
Jason Plumb 00:14:09 I, I appreciate clever Chuck's question. So I I think what's being asked is like, are we doing this just because.
conceptually, like or technically like, it's really hard to like. There's technical hurdles. Or is it just like conceptually? No, you shouldn't be able to. And I'm I'm inclined to say that at least like what you were calling out here is that the shutdown use case?
I think we should be able to support that. And if you have shut down. If we have managed to shut down the thing completely, cleanly.
ignoring disk like there could. There could still be telemetry on disk.
But if we've shut everything down cleanly.
Then recreating the SDK should also not be a problem.
And so I'm inclined to say that if people want this, it's something we should work toward. And that's why I wanted us to think about pitfalls right? So there's and there's and there's there's more than one ball in the air here, and sorry if I'm combining like 3 kind of separate topics. But they all seem related, and they're related to like lifecycle having multiple concurrent instances. I wanna I I think that's bonkers. And I don't know why you would want to do that. Being able to shut down and then recreate it. I think there is some utility in that, especially for apps that maybe are long lived like a kiosk situation, where you only care when a user is interacting with it, and the rest of the time it's just sitting there idle.
like, maybe for long stretches of time. So I don't know. There's probably other use cases, too. But I'm inclined to say that like shut down and restart is a good idea. Does our does our instrumentation currently have a shutdown.
Cesar Munoz 00:15:50 No.
Jason Plumb 00:15:52 So that's a shortcoming. That's a pitfall I didn't think about.
Hanson Ho 00:15:56 So what does.
Cesar Munoz 00:15:57 Still, it's still technically possible, like.
yeah. And I guess to clever Chuck's question, like everything that we've discussed here, I think it's possible, technically speaking, it will be a lot of work, and I guess what we are trying to find out is if it's worth it or not, or or if you know, or if we're gonna do people more harm than than good by providing these instead of because it also depends on what they need.
So in terms of having parallel instances of open telemetry roam. I I agree with with Jason.
It's it's most likely not needed. Maybe you have a use case where you need to contact or send data to different endpoints. And you can do that with just multiple exporters, and that that would be pretty much it. Things like that that are that are possible without multiple.
I mean, you will have multiple instances of an exporter, but at least it wouldn't be the whole thing.
But the shutdown. I think it kind of makes sense as well, because it's it's what it's also available upstream.
So it's kind of like. It's all kind of following the same 5, if you will. So I think that will that will be worth doing.
and probably a fun challenge of that will be the instrumentation stuff. That's for sure, because we will have to figure out a mechanism to detach an instance from an instrumentation which is also probably good in terms of I don't know. Maybe maybe there could be a use case.
as Jason mentioned, where maybe an app needs to release memory for a period of time, for whatever reason, and for better or worse, even though we try to make the the ROM Sdks as as a good a good citizen as possible. It's still, it's it's still consuming resources. So maybe that's that's a worth point of view. I guess it's a valid point of view.
Yeah, that's that's my take on this.
Jason Plumb 00:18:08 Cool.
Yeah, it seems it seems pretty pretty pragmatic to me.
Hanson Ho 00:18:13 The the Java SDK supports restart. So I think I think. Shut down, shut down, you know. That's that's that's reasonable. But the the re. The restart is the one that I that unless certain everything works as expected.
Jason Plumb 00:18:29 It doesn't have an explicit like semantic restart operation, but if you have shut down cleanly, then creating another one should be perfectly viable.
Hanson Ho 00:18:39 Okay.
Jason Plumb 00:18:40 With with the caveat, maybe of that global open telemetry instance being a problem. We've been talking about that a lot lately.
Yeah.
And.
Hanson Ho 00:18:49 And the instrumentation. You're also putting more burden on the instrumentation to be able to like.
cleanly, shut down and cleanly restart.
Jason Plumb 00:18:57 Yeah, yeah. No instrumentation is something else entirely that that cannot be uninstalled.
Like, if you're using the Java agent know that you're not, gonna you're not gonna take out the byte code. We've.
Hanson Ho 00:19:09 So yeah.
I was just gonna say, cause like, you're attaching things like listeners to to things that's like, to to remove. And okay? All right. So instrumentation, then, has a contract of sometimes it has access to a working SDK, and sometimes it doesn't.
Jason Plumb 00:19:30 Yeah. I mean, if if the SDK is shut down, I think it just gets replaced, all of those calls should get replaced with a No. OP is what happens. So there's still that works being done, but it goes nowhere.
Hanson Ho 00:19:43 There's no caching of any SDK, or anything provided by by the SDK resources or things things like that. It has to kind of be.
Jason Plumb 00:19:51 It's it's a weird use case. I don't know that anyone's really flushed that out.
Hanson Ho 00:19:55 Cool.
Jason Plumb 00:19:56 Like getting an agent up and then shutting down just the SDK. I I've no, I I would expect problems. Yeah.
Hanson Ho 00:20:02 Back end apps support that because, like mobile life, mobile application, lifetime should be a lot shorter than than you know. A service. I'm I'm so I'm trying to figure out whether, there's an expectation to be able to do this for, like, you know, just a a back end.
app, and if there isn't, then I would ask something that is more short lived with, you know, more tricky Apis to build off of? Do we want to go that extra mile of supporting restart? So I think shutdown is fine. It's a restart that I you know. It's a little bit.
Jason Plumb 00:20:45 Yeah, that's fair. I mean, yeah, we'd we'd cross that when we get there. I guess.
I agree. That might be challenging to be able to start again.
Hanson Ho 00:20:57 Mustafa, is this something you want to take a look at, and just like, do some investigation about about? You know, you know if you if you you know kind of cleaned up the Api to start up and shut down and and start up. What kind of issues. You might get into.
Mustafa Haddara 00:21:15 Yeah, sure. So like, specifically around.
yeah, okay, shutting it down and then seeing what happens when you start it back up.
Hanson Ho 00:21:26 Yeah, I mean.
Mustafa Haddara 00:21:27 Yeah.
Jason Plumb 00:21:28 Would say, I mean.
this person did a little bit of of some legwork toward this end. So they were trying to create a second rum instance, which is not quite the same thing, but it points out where there are these Singleton bottlenecks, and one of them is very clearly in the in the exporter, and so they had some ideas on how to mitigate this, and I didn't completely follow it, to be honest, but they, you know they did a little bit of research here about some changes that could be made to allow more than one.
I I think if you're gonna have more than one thing reading to disk and and right writing to disk and reading from disk.
They need to be partitioned. They need to have like separate directories, and I don't. I don't. Wanna I don't. I really don't want us to have to build some sort of fancy coordination effort between concurrent exporters working on the same telemetry data set on disk. I think that's a nightmare waiting to happen. So if we can, if we can partition them, which involves like some sort of guid, or some other sort of structural on disk thing that's I don't know. And then, after a restart, what do you do like? That's complicated, right, because there could be multiples left behind. Yeah, it's I would prefer not to mess with it at all. But there might be. I don't know some some of the research they did might help to this end of figuring out how to allow them to make multiples if they were so inclined.
Hanson Ho 00:22:52 Yeah, it looks like they're talking about web views and and creating an instance for a web view, maybe because the resource is different. I don't. I don't think doing it at the app layer is a good idea, but.
Jason Plumb 00:23:05 Yeah.
Hanson Ho 00:23:06 Yeah, that's that's a different question.
Jason Plumb 00:23:10 Okay, does anybody think having the ability to shut down is a terrible idea.
Hanson Ho 00:23:15 Shutdown seems reasonable.
Jason Plumb 00:23:18 Does anybody think that having multiple concurrent instances is a terrible idea.
Hanson Ho 00:23:23 Yes, that's a terrible idea.
Jason Plumb 00:23:24 Okay.
Cesar Munoz 00:23:26 I don't think it's like, I don't think it's terrible. I also don't think it's good. I I will just I just I will just wait for a use case.
Actually, you know, because to me it's kind of like.
most likely, whatever they want to try to do can be solved differently.
It's kind of it's it's overkill, if anything.
so maybe they can solve it in another way.
But if we come up, if somebody comes up with a use case that that really, that's the only way to deal with that.
Jason Plumb 00:24:01 Yeah, then we gotta think about it.
Cesar Munoz 00:24:02 I? Yeah, I wouldn't be like completely close to it. Because if if there's really no other way for a specific use case that I don't have right now.
you know, at the end of the day.
if if they know that what they're doing is gonna be bad for their their app performance, and yet they still have want to do it, because reasons I also won't be like kind of like the policeman here, you know, it's like, well, you know it's a SDK is your app.
You shouldn't do it.
But there you go. But but like I don't see right now a valid reason why it could be needed. I mean.
it may be just a matter of time right now. I don't see why multiple instances should be needed.
Hanson Ho 00:24:46 Does the Java Ck. Supports that support that.
Jason Plumb 00:24:50 So I I asked this question too. I was like, Why do you need multiples? I haven't read the response yet, because I was not awake 2 h ago. But there's a lot of text here, I guess. Okay.
Cesar Munoz 00:25:00 Oof.
Jason Plumb 00:25:01 So I will do that after this meeting and respond to it. Yeah.
Hanson Ho 00:25:07 Well, honestly, if the core Java SDK doesn't support multiple instances, this is a nonstarter for us. So And I, I don't think it does, unless unless there's another way to to to initialize that I'm not aware of.
Jason Plumb 00:25:26 Give me a.
Cesar Munoz 00:25:27 Java SDK, or the agent.
Hanson Ho 00:25:29 Java SDK.
Cesar Munoz 00:25:31 But the thing is that the SDK, I think it's pretty.
It's pretty generic. So maybe it's not.
Probably the the problem will be in the agent because of what we were discussing earlier, that you cannot uninstall an instrumentation. You know you cannot undo the bike weaving stuff but like the just like initializing an SDK to send data through an exporter.
I think you can like technically do that.
cleverchuk 00:26:04 Yeah, it's like global stuff. If you.
Hanson Ho 00:26:08 Yeah.
cleverchuk 00:26:08 Set as global should be able.
Cesar Munoz 00:26:10 Yeah, the global is.
cleverchuk 00:26:11 Nice.
Cesar Munoz 00:26:12 Yeah, the Google is is, it's it's the only caveat there. But if you, if you're not using the global stuff, you can initialize as many instances as you want. As far as I'm aware, the problem you would you will have will be with the instrumentations. That's for sure. So that's that's why I was asking if it's the agent, or just a plain SDK.
Mustafa Haddara 00:26:32 So I skimm their their response to Jason's message. And their use case is basically they're building a library. They want to collect usage telemetry from that library, and if they initialize open telemetry inside their library and have it sent getting sent to some hotel backend that they control the app, that their libraries installed can no longer set up open telemetry.
Jason Plumb 00:26:54 A library should never set up open telemetry.
Mustafa Haddara 00:26:57 Well, then, we should just talk.
Jason Plumb 00:26:59 Yeah, yeah, yeah, no, because.
Mustafa Haddara 00:27:01 So they're trying to use hotel to collect usage metrics and telemetry about their own library.
Jason Plumb 00:27:05 Which is great, they they should instrument it right. And if that's the gap like, if we don't have a robust instrumentation. Api, that makes sense for library developers. Then that's.
Mustafa Haddara 00:27:14 No, no, I think they want their usage instrumentation for their library to go to their own hotel back end, and then the application.
It's collecting its own usage telemetry for its own purpose.
Jason Plumb 00:27:30 Okay. Okay.
Cesar Munoz 00:27:31 Got it.
Jason Plumb 00:27:32 Yeah, that's weird. I had an I had an internal customer who used to work on open telemetry, ask about something about routing in the Java agent today as well cause that's really what that is right is like, you're routing some signal one place and some the other.
Hanson Ho 00:27:45 Are they providing a distribution, or are they just taking the SDK that the their customer gives them, and trying to to do that.
Mustafa Haddara 00:27:55 I think they're using the SDK inside their library, and they don't want to expose that fact to their customers.
Jason Plumb 00:28:02 Yeah, that's what it sounds like, huh?
Hanson Ho 00:28:07 Oh!
Jason Plumb 00:28:09 It's an interesting use case to like, try and initialize it in a library, but I think we should frown on that as well. It's not the design.
But we also need to provide a way to have.
because this use case is a library reporting its own metrics to somewhere else or its own telemetry to somewhere else.
Hanson Ho 00:28:28 It's it's.
Jason Plumb 00:28:28 I don't wanna say metrics.
Hanson Ho 00:28:31 If the library were the one actually providing the the opentelemetry instance, then it could. I mean, that's what we do. And so this does. Basically. Then we could, you know, route the exporters and processes how we want. But effectively, if they're trying to hide the fact that they're using open telemetry and a customer unrelated to those in initializes an open telemetry instance. Then you have. You have an app in a process with with unique unique sandboxes. Basically and very natural.
Cesar Munoz 00:29:05 Interesting.
Hanson Ho 00:29:06 Yeah.
Jason Plumb 00:29:07 You're not gonna hide anything on mobile ever. Okay? So you're hiding.
Yeah, being very.
Mustafa Haddara 00:29:13 I mean in the description. They say it sounds like like, I don't know what they're building. I don't know what library they're building, but they're gonna offer like a collect telemetry, Boolean flag config option for their users.
Jason Plumb 00:29:24 Yeah.
Mustafa Haddara 00:29:24 And if the user wants to opt in or opt out, however, they structure that then, like the the Devs installing that library, understand, this library is collecting its own usage, telemetry.
Jason Plumb 00:29:36 It doesn't seem unreasonable. Yeah.
Cesar Munoz 00:29:39 Well, I mean I guess it. It boils down to the question of our libraries, allowed to generate telemetry, and I I I wouldn't say strictly, no, probably not. Not. Probably what they want to avoid is not not necessarily hide stuff from the app, but but just not send kind of, like, you know, useless data to the app because it's like this, data is only meaningful to to the library developers. So it's kind of like, why, sending it to the app apps, you know. Open telemetry. Instance.
That could be a good argument, I guess.
Hanson Ho 00:30:29 Tab.
Jason Plumb 00:30:33 So I think you can do this with a S. Exporter customizer. So if in, if the library exposed a hook where it could return an exporter customizer that is then put into the SDK initialization by the app.
So we're there's a lot of there's there's a lot of moving pieces here. But if you follow my my thinking, I think I'm onto this. So the app is going to use the initializer or the run builder. And one of the things you can do is have an exporter customizer. If that exporter customizer was returned by the library, it could return a customized exporter that sends only certain criteria data to a different location. Right? So it could be like a like it could be a an exporter that has multiple delegates, but only uses one of them, if it's internal usage, telemetry, and it uses the other. For the rest.
Mustafa Haddara 00:31:27 How would that work if I had 2 of these libraries doing this.
Jason Plumb 00:31:31 They'd have multi if I advisors. Yeah, they would need to.
Mustafa Haddara 00:31:33 Takes most of all.
Jason Plumb 00:31:34 Yeah. So you check for your library specific thing 1st and the data and then send it. If if so, and then you do nothing otherwise.
Are you delegate.
Cesar Munoz 00:31:42 Practical from from a practical point of view, then the application owner will have to pass the builder to the library's initialization.
Jason Plumb 00:31:51 It may be.
Cesar Munoz 00:31:52 I agree.
Jason Plumb 00:31:52 Jim, or I mean the the exporter customizer. That interface, I think, would be the the Api right now. Yeah, you. They shouldn't have to pass the builder. That sounds like.
Cesar Munoz 00:32:02 Or at least get, or at least get, a customizer.
that it's compatible with the builder.
Jason Plumb 00:32:07 Yes. Yeah.
Cesar Munoz 00:32:08 Goodbye!
So that got it.
Mustafa Haddara 00:32:11 Okay. But okay. So if I'm writing this library, and I want to collect my own open telemetry. And I know that other people are going to install this library into their app. I need to be able to account for the fact that they may or may not be using hotel.
and if my only way to get telemetry is for them to set up hotel and pass in an exporter customizer that I give them.
then I'm I'm shit out of luck if they're not using hotel.
Jason Plumb 00:32:40 That's true. I mean they. If they're generating usage telemetry, and they want to send it somewhere.
they're using something right? It can be bespoke it could be another library. It could be open to like.
Mustafa Haddara 00:32:52 They might, the app might. The client App might not be doing any telemetry at all, and I still want to collect usage information about my library and my my library might be like a component library, or like a date library.
Jason Plumb 00:33:03 Oh, I see your point.
Mustafa Haddara 00:33:04 Related to it.
Jason Plumb 00:33:05 Yeah, yeah, maybe the yeah, maybe the app.
Cesar Munoz 00:33:06 Maybe the.
Jason Plumb 00:33:07 Blind.
Okay.
Cesar Munoz 00:33:09 Maybe maybe in that case you could say like, Well, if you don't pass if you don't, if you don't if if the app doesn't have any use for open telemetry itself.
Then there should be a way that the library knows that either because of, you know, one of its initialization calls to press to provide a open telemetry stuff wasn't called, maybe, or something like that. And in that case, when the library knows that the host app is not using open telemetry. Then he he can just create its own open telemetry instance, without.
you know, fearing it, for of any kind of issues that it could cost to the app.
maybe because it will be the only.
Hanson Ho 00:33:57 But again, now, now that I think about it, if another library does the same, if another. Yeah. Now, now we have to. Yeah.
a library. That's not a distribution creating its own instance feels wrong. It should be asking for an instance as if it were instrumentation. Now, the the issue is where you said in telemetry to, because, as you said, there could be multiple libraries doing this, and you don't want, you know, and different instances, and and trying to coordinate in a reasonable manner, will require some logic to kind of tie it all together.
Jason Plumb 00:34:35 So I'm sorry to jump in on this, but I think the I think what the answer is is, they should just be using the Java SDK.
Hanson Ho 00:34:43 Yeah.
Jason Plumb 00:34:45 Right like. And like this android ROM thing that we have set up is really geared at at real user monitoring of applications. And if they're doing it. A library they should just use. The Java SDK is my is my instinct.
Cesar Munoz 00:34:59 Well, but what if they say, well, we want to have the this buffering stuff that comes with auto number and not with the Javascript.
Jason Plumb 00:35:07 I mean that we.
Cesar Munoz 00:35:08 Which is fair enough because they're working.
Jason Plumb 00:35:10 This buffering exporter is a span exporter, and they're happy to wire it up to their hotel. SDK.
Hanson Ho 00:35:16 But there's still the issue of 2 libraries trying to instantiate Java SDK on its own.
Mustafa Haddara 00:35:25 The Java SDK. Singleton.
Jason Plumb 00:35:27 I don't think so. I think I think you can make multiples. You just have to be careful about the usage of global open telemetry.
but like that block I was showing before. I think I think you can do this multiple times.
Cesar Munoz 00:35:42 I will, I will verify this. It's it's probably in.
Jason Plumb 00:35:45 Think of the builder. Go ahead!
Cesar Munoz 00:35:48 I think you can do that multiple times. Yeah, definitely, it's just a, it's just a a yeah, no.
Hanson Ho 00:35:55 No, I think.
Cesar Munoz 00:35:56 Any problem. That sorry, Hanson. Go ahead.
Hanson Ho 00:35:58 Oh, no, I was gonna agree with Jason. I think I think you're right, takes over the application and provides instrumentation for the lifecycle of the application. Somebody who is a library, who does not own the application should not be initializing the application unless it's a library that is, instrumenting applications so in which you shouldn't install 2 of them at once.
Jason Plumb 00:36:25 Build and register global, it's just called build. If you call, build and register global, it, it'll do that.
And if you don't, you just get the instance.
Cesar Munoz 00:36:33 I'm pretty sure in in the upstream Java. SDK, they they really don't like global open telemetry.
Jason Plumb 00:36:38 No, it's a it's a it's a challenge right now. There's some. There's some you should we? We just actively discourage people from using it.
Cesar Munoz 00:36:45 I bet they will like to get rid of it. Probably.
Jason Plumb 00:36:47 We want to. Yes.
Cesar Munoz 00:36:50 Yeah.
Jason Plumb 00:36:51 That ship is sailed. But yes, we we would love to not have that anymore. Okay. So I think I think the answer is, yes, you can do this multiple times, and if the library does this and have has its own SDK, so it can generate an export using disk buffering or not, then that's its own thing. It's self contained. They don't need anything from the android instrumentation or the android SDK.
The rub is if they're using our instrumentation Apis or something else. Right? That's kinda coupled.
Cesar Munoz 00:37:22 Yes, the instrumentation. I think it's another as as a whole, another kind of warmed, but.
Jason Plumb 00:37:28 Yeah.
Cesar Munoz 00:37:28 I guess, in conclusion.
this, this is this, is it this, this is the use case. I mean definitely, whether they use hotel Landry or plain Java. Ck.
there will be still multiple instances of open telemetry running in the same app, even though you know that that won't wouldn't be known to the application code itself.
Jason Plumb 00:37:52 Right.
Cesar Munoz 00:37:53 I mean, it's it's not impossible or not unreasonable for this to happen. Overall like at Runtime, because of libraries perfect about the libraries, use cases to be.
Jason Plumb 00:38:04 No me, neither.
Cesar Munoz 00:38:05 Interest.
Jason Plumb 00:38:06 I think it's the 1st time it's come up, and Mustafa helped me for thanks for helping me get my head around that that's helpful.
Mustafa Haddara 00:38:12 Yeah, no. Problem.
Jason Plumb 00:38:14 I wanna make sure. So we're at 37 min right now. I want to make sure we have time for some other topics, because there are a few that have stacked up. I think this is a really good discussion, and I appreciate people giving kind of thoughtful, careful consideration to these kind of new use cases. And hopefully, as people get more excited and continue getting excited about the project, more of these things come up, too.
Okay, let's skip over mine. We've basically talked about using delegation for exporting. I still think there's room to maybe make this easier for users. I don't know what that looks like, but maybe we'll sleep on it.
Let's open it up to Serbie.
Surbhi 00:38:48 Don't get better.
Jason Plumb 00:38:48 Serbie.
Cesar Munoz 00:38:50 Survey.
Surbhi 00:38:51 Hello, thank you.
So I we wanted to like, discuss this particular thing right? If you have this permission, it is sort of a high severity permission because it lets you access phone number know the exact device. And when you have this permission, the app user will be prompted. If they want to grant this permission.
I think we use it for gathering network carrier info and network type subtype info.
So I was thinking there was a suggestion of a solution in that issue itself wherein it mentioned that wherever our code needs it, we check if it has the permission, and we remove adding the permission by default to our manifest files in our SDK, and instead document it for the apps who consume us.
Add this, if they wanted this, these particular features.
And then it would be out of our like. It would not be compulsory right for consuming apps to have to have this permission.
Jason Plumb 00:40:11 Can we do this based on detecting which instrument instrumentation is going to be installed?
In other words, if it's only used by one instrumentation? Can we only request that permission in the case that that instrumentation is is around, is is being set up.
Surbhi 00:40:28 The manifest needs to have it. That's the problem.
Jason Plumb 00:40:33 Okay. So you can't do it conditionally. It's just like declarative.
Surbhi 00:40:36 Y'all.
Cesar Munoz 00:40:38 Is, isn't the existing current the existing use case for stuff that we send in as resource attributes.
Surbhi 00:40:50 No.
Jason Plumb 00:40:51 No.
Surbhi 00:40:51 Not resource. But yeah, that's true that these attributes there is a network span appender. So by default, these attributes can also get added to all these spans if the network service is on.
But I think I'm not sure if hotel rum has a config to suppress that, so you might be right, Caesar, it might be getting by default. Added to all these fans, the network attributes.
Jason Plumb 00:41:23 I mean, that's part of the network instrumentation. So if you have network instrumentation, then you get those.
I think that's the design. Right now.
Mustafa Haddara 00:41:32 Do we know that we need it for cause? Like, if you went back to that manifest, we were doing access network state Internet, read phone, state.
Hanson Ho 00:41:43 Yeah.
Mustafa Haddara 00:41:43 Do we know that we need read phone state for the network stuff given that we have those other 2.
Hanson Ho 00:41:48 I'm pretty sure we don't need read phone state.
Surbhi 00:41:51 We do actually, actually, yeah, that's the weird part. So excess network state just gives you access to whether the network is Wi-fi or cellular. And then, if you want to know the subtype, lg, 5, g. Then you need the read phone state and we also gather carrier information. The carrier Iso, the carrier name. Those require the read phone state.
Hanson Ho 00:42:15 That's yeah. That is dangerous. It's Pii a little bit as well it.
If we want to keep the instrumentation reporting this, then I think your solution works as as a as a, you know.
enable this, otherwise we don't collect it.
But I would be. I would I would. I would.
I'm yeah. I'm not sure about collecting all this information.
Jason Plumb 00:42:45 Serbie so well before I ask that question, Hanson, I wanted to respond, because, yeah, some of that is a little bit touchy to gather. But certainly, if you're looking at a rum session and a user walks out of their house off of Wi-fi and switches over to Lte, and something happens like you want to know that right? Like knowing that they switch networks is like super valuable to a room session.
Hanson Ho 00:43:06 No, you can know that. You just can't know between 5G and Lte.
Jason Plumb 00:43:10 Yeah, that doesn't seem that sensitive to me, though. But whatever
Hanson Ho 00:43:13 It's it's the care. It's the carrier information.
Jason Plumb 00:43:15 Yeah, yeah.
Mustafa Haddara 00:43:16 Care.
Jason Plumb 00:43:17 Yeah.
Hanson Ho 00:43:18 Carrier permissions is a sensitive one. The Lte versus 5G is is the one that's like, you need a lot of permissions to get that? Do we really want to get that is.
Jason Plumb 00:43:28 Yeah, no separate.
I think it's a good. I think it's a good question. So we did this come up through a customer situation.
Surbhi 00:43:35 I'm not fully aware of that. But yeah, it came up in my team, and they wanted me to figure this out.
Jason Plumb 00:43:43 Yeah.
Cesar Munoz 00:43:44 The the current state of it is that we don't collected unless this permission has already been granted to the host. App right.
Surbhi 00:43:56 Yeah, we won't be able to, but we add it by default to the manifest. So yeah, if the customer on the prompt says, no, we won't be able to collect those.
But instead of.
Cesar Munoz 00:44:08 It, it.
Surbhi 00:44:09 Yeah.
Cesar Munoz 00:44:09 And we we don't even launch the prompt right? It's like the app owner has to do that if they want to. If they want us to get this data for them.
Surbhi 00:44:20 Oh!
Cesar Munoz 00:44:20 So they're.
Surbhi 00:44:22 Android automatically does that. If this is there in any of the android manifests of your app or the dependencies you have.
Hanson Ho 00:44:31 But if it's if it's not.
Mustafa Haddara 00:44:34 It.
Hanson Ho 00:44:34 Then does it just not collect that information, or does it do it the prompt, without without the app having to like implement that.
Surbhi 00:44:43 Oh, I didn't get your question.
Hanson Ho 00:44:46 So if you didn't have it in your explicitly stated, will your app ask for the permission.
or does your app have to like do something to ask for permission, or is it? Is the prompt automatic.
Cesar Munoz 00:45:01 No, I think.
Surbhi 00:45:02 Problem.
Cesar Munoz 00:45:02 Do something.
Surbhi 00:45:04 I think the prompt is automatic. If the manifest file contains this permission, added users, permission.
Cesar Munoz 00:45:12 Well, last time I check. I know last time can add stuff in the manifest.
But there are some permissions. So, for example, Internet is one permission that doesn't need a prompt like, it can be on the manifest. And then that's it. It works. Yeah. But there are some others more explicit ones that I think the app, then, has to not only define it in the manifest, but also run some code that launches the the dialogue.
I think that's the case.
Hanson Ho 00:45:46 Putting in the manifest will make it prompt for you to ask for the permission, but removing it.
does that automatically, just shut it down so you'll never be prompted, or will will it be prompted?
Because I think I think I don't think.
Surbhi 00:46:07 I don't think it won't be prompted.
Cesar Munoz 00:46:10 I I think the only thing that you will get from adding into the manifest and and nothing else.
is that if you go to the apps app settings in in the android.
in the Android OS settings. And then you go to the apps and you get into a specific app settings. You can see that that app might need that permission. That's the only thing that it will do just by set, just by adding it into the manifest.
But the prompt that you get when the app is running, I think, is is something that the app has to write that code to to for that to actually happen.
That's my understanding.
Hanson Ho 00:46:48 Specify in the manifest.
Cesar Munoz 00:46:51 Broad.
What we could do.
Jason Plumb 00:46:52 We do right now, we currently do have read phone state in this manifest and the application. I haven't tested this in the the network stuff in the demo app in a while. But the only thing the demo App declares is Internet.
And I think that the network stuff works. But someone should try it. It's been a it's been a few weeks for me since I've looked at any of the network stuff.
Cesar Munoz 00:47:15 The thing is that when, when you combine an app, it merges the manifest files from the android libraries that you added to it. So in the apps manifest, you see on the Internet. But then, once it's compiled, you will get all of this stuff plus everything. So.
Jason Plumb 00:47:30 So I guess you know what I'm I think. Why, it exists in the 1st place, is to make that experience easy for the user. Right? We have network capabilities that we currently try and read and put on to our telemetry. And if that permission wasn't here in our manifest.
they would not be able to get some amount of data without adding it manually into their manifest right.
Cesar Munoz 00:47:56 And also launching the Bronx. Not on. It's not only adding stuff in the manifest for some permissions.
Surbhi 00:48:02 I think now.
probably the dialogue is automatic, Caesar like, whenever the app needs uses that permission, Android automatically determines that it needs to put that prompt up and ask the user. If that's okay.
Cesar Munoz 00:48:20 I mean it probably have. It might have changed. I know it was not the case a couple of years ago.
but I haven't checked recently.
Surbhi 00:48:28 Okay.
Hanson Ho 00:48:31 So the the original question is whether this is okay. To ask for right.
Surbhi 00:48:37 One thing is also, it is added into Android manifests. Let's say to Jason's point that our network instrumentation needs it. That's why we add it, so we don't have to document it, and the customer doesn't have to follow the documentation to be able to be aware of adding it. But then Core also has it. So maybe we can remove it from core. I'm not sure some part of network instrumentation bits are in the core and some are in the network services module right? So like by by default, adding it to the services module makes it, and like required for and unnecessarily there, even though you don't require it. Does that make sense.
Jason Plumb 00:49:22 It does. Why do we have it in? Why do we have it in both at all?
Hanson Ho 00:49:25 Probably because it was in one, and it was factored out. I would definitely delete it in the place. That's I'll definitely delete in the place. That's not part of the instrumentation it should be part of. You know the the module that the you actually need it on.
Jason Plumb 00:49:40 Network, I think, and network doesn't have a a module at all, or a manifest at all.
Hanson Ho 00:49:45 Yeah.
Cesar Munoz 00:49:46 What if? What if we just don't add any dangerous permission at all?
And then we say, Well, you, we have to stay in the docs of of Hotel Android, and say, if you want these attributes or this functionality to to work, then you will have to enable this permission, and they will have to do everything they have to set the stuff in the manifest. They would also have to do whatever code changes they need. In that case.
maybe that would be a better way, so that everything's clear for the consumers.
Jason Plumb 00:50:18 So that's what's being asked. Here is like, I like that.
So I'll be using that thing you just described, Cesar, and like, I understand where it's coming from. But I'm hesitant to say yes so quickly because people don't read docs. People just want it to work.
Hanson Ho 00:50:33 And and if if and if they don't get the the fine grain telemetry I think that's a it's, it's it's okay. Because I think the the refine permission. Sorry refund state does a lot more. You can access the phone accounts with that. So it's not just giving it like the detailed network information. It's actually really weird that you know, you're you're you're getting network in detail network information. And you're asking for the phone state. So I think I actually like that, for you know, and if people don't get it and they miss it, the workaround is, you. Add it to your app manifest.
Jason Plumb 00:51:09 I think I think you know, it's nicer to the end user to not over ask for permissions like, that's been a rule of thumb in software development in general for a very long time. So I you know, I still want to make it easy for people.
But I think you know, adding, pasting a line into your apps manifest to enable this sub feature is probably fine, so I I welcome a Pr for this. If you want to take that on Serbia. I can assign that to you.
Surbhi 00:51:37 Yeah, I can do that. That sounds great. I wanted to also add that, suppose that's a better solution, because if suppose we added it here.
And the customer doesn't know. So Google Store also has this requirement that you have to clearly document it in the privacy documentation of yours that we'll be collecting this permission for these reasons. So the app definitely does need to know.
Jason Plumb 00:52:08 Oh, interesting. Yeah. Okay, so even though it's kind of transitive because the manifest get blended, they would still need to declare that in their privacy statement.
Surbhi 00:52:16 Yeah, otherwise store can take actions against the app. If.
Jason Plumb 00:52:21 Yeah, okay.
Surbhi 00:52:22 That they are doing it. Yeah.
Jason Plumb 00:52:24 Yeah. So then, we want to make that developer experience better. So it sounds like, it sounds like it's a win win. Then, okay, comment on this.
Cesar Munoz 00:52:30 Wait!
Jason Plumb 00:52:31 Comment on this one, please, and then I can assign it to you.
Cesar Munoz 00:52:34 On on top of all that, if we are concerned about the possibility, very likely possibility that people will miss stuff in the docs.
which is, I think it's fairly common.
Maybe one more thing that we could do is to print a log when we.
when we notice that this permission is not enabled, so that at least they can see elsewhere, too, that you know this is happening because they didn't do something in case they.
Surbhi 00:53:05 Yeah, that makes sense. Yeah.
So we decided to remove it and add it to the documentation and add a log where the attributes are not getting populated because of so and so reason.
Cesar Munoz 00:53:22 It could also be helpful for debugging. I think if some some customer complains and say, Well, I'm not getting these attributes.
and then you can say, Well, give me your logs, and then we'll see the log. This is this, permission is not granted. So we're not adding this attribute that may be should be a debug log, though.
Surbhi 00:53:42 That makes sense. Yeah.
Hanson Ho 00:53:44 Do we have a place where we describe the feature, the the data that gets recorded.
Jason Plumb 00:53:51 We we do for each instrumentation.
Hanson Ho 00:53:54 So if if in the instrumentation description about what gets recorded we explicitly say there to get out to get like detailed carrier information and connection type. You need this permission. Otherwise they wouldn't even know what is gonna show up right? So they'd have to like go somewhere to find find this so you know, I think putting documentation here would would.
Jason Plumb 00:54:18 Yeah, agree.
Hanson Ho 00:54:21 Like. I don't think people will miss it to be honest unless they like. Have something that's, you know, depending on it. But I don't know what information you know, what whatever helps you can use hopefully, else you could slow, you know, 3 G could be faster. You can't really tell by by type. So.
Jason Plumb 00:54:44 Cool. It looks like Leonardo didn't join, but had a couple of things here like.
Hanson Ho 00:54:49 Joined, but he had to. He had to bail. So in the chat we can respond. We can. We can discuss it and then put it in the in the notes, and we can respond to him. You know, back in slack.
Jason Plumb 00:55:00 Good sounds good. We have a few minutes, so let's just try and and and address these. So this idea is to add the trace Id for Http requests to not.
There's already trace context that's propagated. So if you have an instrumented Okhtp client and you make a request, it already has a header. It's not.
Surbhi 00:55:25 I mean, it's already in the request. I'm not sure what this is asking.
Jason Plumb 00:55:29 Does anyone know what he means by this.
Surbhi 00:55:32 Maybe the server timing header thing that we do in Splunk Hotel Android.
Hanson Ho 00:55:38 This is treeside treeside.
Mustafa Haddara 00:55:40 Yeah, this this might be, trace propagation.
Surbhi 00:55:44 Is already there, right.
Jason Plumb 00:55:45 Yeah, which is different than server timing. Do you think he really is asking about server timing.
Surbhi 00:55:50 No server timing header is something that contains the Apm. Trace. Id.
Jason Plumb 00:55:58 Right.
Surbhi 00:56:00 But yeah.
Hanson Ho 00:56:01 What's that choice of.
Surbhi 00:56:04 It's to relate the client telemetry with the Apm.
Cesar Munoz 00:56:11 We? We said, we already have trace context propagation set up in Andre. Do we.
Jason Plumb 00:56:17 I think so.
Mustafa Haddara 00:56:19 Happens, and by default.
Jason Plumb 00:56:21 Really.
Cesar Munoz 00:56:22 Oh!
Mustafa Haddara 00:56:25 I could be wrong, but.
Jason Plumb 00:56:28 The instrumentation for okay. Http should do that right.
Cesar Munoz 00:56:33 But I think that's set in the illustrate context stuff should be set during the initialization of the hotel instance.
I don't think it has nothing to do with the instrumentation. I think.
Jason Plumb 00:56:46 There's default propagators. Right? The default propagator is W, 3. C trace context that way. Yeah, yeah, yeah.
Hanson Ho 00:56:54 And.
Jason Plumb 00:56:55 So if it doesn't work. Yeah, let we absolutely need to fix this. But you do have to use the instrumented clients right?
Cesar Munoz 00:57:04 Yeah.
Jason Plumb 00:57:05 So I can spell.
Hanson Ho 00:57:24 Are they?
So the trace Id for the network request is injected into the network requests when it's made. That's what this does.
Jason Plumb 00:57:37 Yeah, but it also. Yeah. I think the instrumentation creates a new span, which will be a root span most of the times on on client side, and then that span that span id and trace Id will get propagated in the W. 3 C. Trace context to the server.
and then that span is also just reported as part of the normal telemetry reporting process, so like there would be a span that gets ingested.
Cesar Munoz 00:58:06 It seems like we do set it just sent a link.
So it's either that it might not be working. Or maybe the question was about something else.
Jason Plumb 00:58:20 Oh, okay, let's put that in the comment.
Surbhi 00:58:25 Oh!
Jason Plumb 00:58:25 Or maybe.
Surbhi 00:58:26 Remember the use case I was talking about now so like when the request goes from client to server, the server sends a response in response the server attaches its own trace. Id to the server timing header, and we add it to link, dot trace, id, and link dot span id, so that from the client span you can go to the server span in the Ui via a click.
Jason Plumb 00:58:51 That's right is the user. Do you think that that's what Leonardo is asking about.
Surbhi 00:58:57 No, I just wanted to point that that could be a use case like adding extra trace id to the span.
Jason Plumb 00:59:03 Yeah, yeah, which I think we're not doing it on mobile yet, right?
Surbhi 00:59:09 We are doing in Splunk Hotel, Android, in open telemetry. Android. We are not.
Jason Plumb 00:59:14 Right right. Did. Do you know if John Bly's pull request landed for that stuff in the spec?
Was it an otap?
I forget.
Surbhi 00:59:27 I'm not sure.
Jason Plumb 00:59:30 You had something like this. There it is a.
Hanson Ho 00:59:33 Wow, 2, results.
Jason Plumb 00:59:35 Oh, I imagine, search works. They're trying to replace it with this complicated thing that doesn't work. Yeah. So this one, it's not a Pr, it's basically an otap. I think I forget where I landed.
Anyway, I'll ask on. I'll ask in the dock if this is what they're talking about I it doesn't seem like it. But maybe oh, yeah, whatever. Okay. And then something about we're almost out of time. Configuring disk exporter to flush on app close. That should happen right.
Hanson Ho 01:00:20 What do they mean by app? Close? Do they mean the process termination? Or do they mean backgrounding.
Jason Plumb 01:00:27 They probably mean close, like exiting.
Hanson Ho 01:00:34 I thought we'd do a best effort when we detect on Java Shutdown.
Jason Plumb 01:00:40 But that.
Hanson Ho 01:00:41 That's not the only cause I was talking about. There's a whole bunch of process terminations that you don't know about, but then, for the ones that do.
Jason Plumb 01:00:52 So the span exporter has a flush method and a close method that like that's on the interface. So those should be closed like the SDK should call flush and close on all exporters. I think that's the short answer.
Cesar Munoz 01:01:07 I I agree, it's just that we currently don't have a shutdown method. So I think they have no way to signal that they're gonna close their app.
So I'm saying is that probably if we add the shutdown method to the wrong instance, maybe that this will automatically solve that other issue, because once people call it whatever whenever they want to.
Yeah, it should flush everything. Yeah.
Jason Plumb 01:01:31 Okay, we're overtime. Sorry about that. Y'all. I should be better about staying honest, because we all have other meetings to go to. Thanks for being here. I appreciate your help. Please review Prs. We need help reviewing. Prs. Please do that, and we'll see you next time.
Cesar Munoz 01:01:46 Thank you.
Thank you. Bye.
Surbhi 01:01:48 Bye-bye.
