SIG: Go SIG
Date: 2026-09-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Tyler Yahn (Splunk) 00:01:16 Ebony.
Puneet Singh 00:01:18 Oh, better.
Tyler Yahn (Splunk) 00:01:20 How's it going?
Puneet Singh 00:01:22 Not bad, overall okay.
Yesterday I was thinking that Hmm.
Previewing more code than writing, actually, so… initially, I thought that I'll, I'll, you know.
The plan was to write some code and get… but yeah, it's slightly… Doing different from the… The initial thought, but it's not bad, actually.
Because it kind of forces you to look into the ADS code, which, you know.
You could go quite longer without looking at it, so it gives some perspective, actually, so…
Tyler Yahn (Splunk) 00:02:03 Yeah, yeah, absolutely, yeah.
Yum.
Do a lot of code reading.
Yeah.
Are you talking, so are you working on the, the, the configuration stuff?
Puneet Singh 00:02:21 Yes, the meter curator.
Tyler Yahn (Splunk) 00:02:23 Damn.
Did you see the, the… the work I did with, David's stuff?
Puneet Singh 00:02:31 Actually, I was a bit late in, you know, following up, actually.
I started today only, and the only thing I got that there is a bit of overlap between the work that David is doing.
And, the work that you are doing, which is related to OBI, but that's more or less… I still have to go through the thing in detail to…
Tyler Yahn (Splunk) 00:02:58 Yeah, so, the… we talked last time at the SIG meeting about, like, experimental features and, like, essentially, like, an experimental SDK, because, like, we wanted to provide these sort of things.
But we didn't want to expose, you know, like, methods that are going to be on a stable SDK that may change or something like that, so… We wanted to do this.
But I think that, like, so I went in and prototyped some things, and, like, one of the things that, like, I did come to was that, like, you could, like.
accomplish all that with options, and not have to duplicate an SDK.
And I think, like, that would definitely be applicable to what's going on with the configuration stuff as well.
If we wanted to provide an option. I think that's the way we should go in, like, an experimental package that could be ingested, is kind of the idea, but yeah.
Yeah, I… yeah, so there's, like, a prototype as well. I see David Sears now, as well.
David Ashpole (Google LLC) 00:03:58 8.
Puneet Singh 00:04:00 So… so what you're saying is that the work that happened in the meter configurator Mmm… I mean, the similar approach is being followed for the… For the work that you are doing for…
Tyler Yahn (Splunk) 00:04:14 Well.
Puneet Singh 00:04:14 OBI stuff?
Tyler Yahn (Splunk) 00:04:17 Kinda, yeah.
Puneet Singh 00:04:19 I mean, in a way, the options… the way the options are being used to add a new feature in the SDK without
Tyler Yahn (Splunk) 00:04:29 Yeah.
Puneet Singh 00:04:29 affecting the… the stability of the current public API.
Tyler Yahn (Splunk) 00:04:34 Yeah, right, exactly. So I mean, it's also just, like, a, a prototype.
I don't know where the prototype went. Oh, here it is, yeah.
David Ashpole (Google LLC) 00:04:51 Let me find your prototype.
Tyler Yahn (Splunk) 00:04:53 Yeah.
So yeah, this is… is this right?
Yeah, I think this is right.
It's been a few days since I looked at it, but the idea is that, like, here you have some sort of, like, option pattern, like, with binding, essentially, which is, like.
what… what'll… What'll provide, essentially, like, you can use it, so if you go to… Had an example… yeah, here we go.
So something like this is kind of how it gets used. So, like, the SDK metric is here. The SDK metric X, is also this import, and then there's, like, the API itself. This is, like, a good split, because you're going to need something specifically for the instrumentation, right? Like, this is definitely important.
So, yeah, like, to set up the provider, it's just like you would do normally. The only thing is that you're mixing in these experimental, options patterns here, and so then, like, it's explicitly saying to the user, like, hey, by the way, like.
You're turning on an experimental feature literally because you're providing an experimental option to this meter provider.
Which should be pretty explicit. Then what happens, like, is this returns a provider that does implement these interfaces. If you don't provide these, it doesn't return an implementation that, like, does, provide those interfaces, so… When you go… yeah, go ahead.
David Ashpole (Google LLC) 00:06:20 Oh, that's interesting. I was… at first, I was like, why not just have, like, the environment variable-based thing?
Rather than options. I guess the options let you have a single meter provider that is the experimental one, and a different one that's… Not experimental?
But…
Tyler Yahn (Splunk) 00:06:38 Yeah.
Yeah. And I think that, like, The environment variable I think the environment variable could work. I think that's actually an interesting idea as well. You do have to worry about, like, concurrency issues, though, right? So it's like, you have to make sure the environment variable is set, then create the meter provider, because it's gotta read that, so, like, there's gotta be, like, a dependency thing there, whereas this is, like, explicit in code, but… Yeah, I mean, I actually didn't think that through. Yeah, because, like, the thing is, is, like, I found out a way to, like, to hook in, essentially, like, like, these, like, creation functions, let me see if I can find it, like, where essentially, like… it is, like, when… yeah, you have, like, this… these, like, binding things, so essentially, like, these binding, like, properties are now, like, passed into the meter, and whether, like, you pass in that option or not essentially, like, turns it on and off. But there's nothing saying that, like, you couldn't, like, instantiate, like, these functions, for their binding Like, without, you know, I don't know.
like, having… Yeah, like, there's definitely, like, ways you could do that with environment variables as well, but… But yeah, to your point, like, I think that that's an interesting thing, like, to have it explicitly be… options, it does help, because it, like, it clears that up. Like, it helps you say, like, yeah, this is, this is definitely gonna be this.
Like, versus, like, I want another provider that doesn't have these, like, features, in it as well.
David Ashpole (Google LLC) 00:08:05 How do you solve the, like, whether the binding function is available or not? Does it return two different versions of the… like, instrument structs, basically. One that's, like…
Tyler Yahn (Splunk) 00:08:15 Yeah. Yeah. Yeah, exactly. Yeah, and then, like, like, I think, here, I actually have it two different instruments, but, like, you can always have it, like, be one instrument that implements it, the whole thing.
No, actually, we shouldn't do that. Like, you could have it be one implement instrument, and then, like, kind of, like, remove that method from the return. Like, there's definitely a way to do that, we've done that in other ways. But,
David Ashpole (Google LLC) 00:08:38 Remove the method.
Tyler Yahn (Splunk) 00:08:39 Yeah, for… it's a… it's a… it's a bad idea.
David Ashpole (Google LLC) 00:08:42 embed, embed in, like…
Tyler Yahn (Splunk) 00:08:44 Essentially, yeah, you do that.
David Ashpole (Google LLC) 00:08:45 Yeah.
Tyler Yahn (Splunk) 00:08:46 You can disappear these things, but like… But the problem with that is that, like, you will have, the implementation, like, living mixed in to the other implementation, so, like, then you have much more of a chance of, like, performance impact to, like, the stable path that, you know, because of this experimental feature, versus, like, something that's, like, wrapping it, is, like, totally isolated, and it's not gonna actually, like, cause… like, you're guaranteed to not have, like, performance degrad… well, you're not guaranteed… you have a higher confidence that it's not gonna provide performance degradations.
Like, by not mixing in as much, like, and trying to use, like, primitives all the way down into, like, the, you know, the pipeline or something like that to actually, like… or aggregation to isolate that kind of stuff, yeah.
David Ashpole (Google LLC) 00:09:26 Interesting. Like…
Tyler Yahn (Splunk) 00:09:29 I mean…
David Ashpole (Google LLC) 00:09:29 Of two minds there, because… On the one hand, I like to keep experimental things separate, but on the other hand, like, especially for these performance-sensitive features, like.
the whole point is to prove out that we can not kill the performance of the SDK by introducing them, you know?
Tyler Yahn (Splunk) 00:09:47 So, I don't know… specifically about the finish, I don't think I measured that in this, but, like, the bind I did. And I was able to get, like, the zero allocation with, like, very minimal, like, overhead, and, you know, much more reduced overhead than what we currently have, but, like, I don't know if it's exactly equivalent, like, CPU, like, computation overhead.
But, like, allocation-wise, it looked exactly the same with what the implementation was in here, versus, like, your prototype that did, like, completely just build it all together, so… Yep.
David Ashpole (Google LLC) 00:10:18 Which is totally… like, it is totally fine. It's more like…
Tyler Yahn (Splunk) 00:10:21 Yeah.
David Ashpole (Google LLC) 00:10:24 I'm… I'm curious… I'm more curious just, like, how we… if we view this as… We're doing what is more or less the final implementation of what we want the bind thing to look like.
Tyler Yahn (Splunk) 00:10:36 Yeah.
David Ashpole (Google LLC) 00:10:37 and then when it goes stable, we'll just remove the experimental tags. Or if it's like, this is just a prototype that happens to coexist But when we actually do the real thing.
Then we'll need to spend all this… All this time, you know what I'm…
Tyler Yahn (Splunk) 00:10:54 Yeah, I know what you're saying, so, like, then you gotta, like, refactor and clean it up and all that kind of stuff, and, like.
Yeah, and I, honestly, I think that it's a little bit in the second category, but also not entirely, like… Yeah.
Like, it also… Excuse me.
it really depends on, like, how we actually go about this. Like, in this prototype that I have here, like, it's nice and, like, isolated, so, like, there, like, the functionality to do, like, the binding and that kind of thing, like, it's not nearly as, like, intrusive as, like, the finished stuff, where, like, you're reaching deeper into, like, the maps that we have, right? So it's a little bit, like.
David Ashpole (Google LLC) 00:11:28 possible for Finnish to not interact with the existing…
Tyler Yahn (Splunk) 00:11:31 Yeah.
David Ashpole (Google LLC) 00:11:32 That's right.
Tyler Yahn (Splunk) 00:11:33 Exactly, yeah. So, like, the binding stuff is actually, like, the isolation… like, I don't think we're gonna have two different instrument types when we, like, stabilize this, or if it gets stabilized, right? Like, I think you're probably gonna have one instrument type that you could return… And, like, well… Yeah, because it'll be a stable anyways, like… Yep. But, like, so that means that we would probably need to refactor afterwards, like, you'd maybe have to, like, move a method to a different, like, host or something like that, but, like… I don't know… Too much more than that, though, because it actually, like, the implementation is very much like what you did, it's just isolated into a different instrument type, but, like, yeah, the finished one may be a little bit more, like, there's gonna be some, like, refactors that you would need to, like, clean in, but… But again, like, I honestly, this was a prototype, and I just wanted to show, like, the API more than the actual implementation, and I… outside of the performance stuff. Yeah. Yeah.
David Ashpole (Google LLC) 00:12:26 I do… I do like the… I like the idea of… Being able to either globally, or via an option, turn off the existence of the function. I feel like that's… an extra layer of protection for us, and backwards compatibility and stuff. Well, you're never.
Tyler Yahn (Splunk) 00:12:50 We're gonna be able to globally do that. Like, once you return a meter provider, like.
David Ashpole (Google LLC) 00:12:54 Oh, I just mean that, like.
Right, I mean that either it's an option or it's an environment variable, and environment variables are… global, right? Yeah. So, like, and you're right that if you swap it back and forth, you don't get to turn on and off the behavior. It's more like… At some point, someone had to have opted in to… this thing existing. And that feels like… like a good step forward from what I was initially proposing, I think.
Yeah, whether we do it as, like.
I'm still more on the side of, let's try and implement this the way we would want it to be, so that when we go back to the spec and say we're happy with it, like.
We mean it, you know?
But I… I also… like, it would be very painful to go through all of that.
And then to be like, oh, actually, we're gonna back out all these changes. So… Yeah, it's like, if we feel like…
Tyler Yahn (Splunk) 00:13:56 Well, I… so, like.
I don't think there's too much separation for the Bind stuff, like, to be honest. Like, if you want to take a look at that PR that I have, like, I honestly think that, like.
that implementation looks great to me for, like, an initial, approach, like, maybe not… like, because it does mix in the finished stuff as well into that PR, just to show that, like, they were both possible, but, like, But yeah, take a look. If you think the implementation can get better, I'm totally on board for, like, evaluating what we want to do there. And like, yeah, from the spec perspective, I think that, like, it's more about just saying, like, I do want to get these things through.
David Ashpole (Google LLC) 00:14:31 Yes.
Tyler Yahn (Splunk) 00:14:32 But to be perfectly honest, if the spec… doesn't accept this, doesn't accept it within a year, two years, I don't ever, right? Like… I…
David Ashpole (Google LLC) 00:14:44 It's mostly waiting on us, just by the way.
We have two other languages that have implemented this.
Tyler Yahn (Splunk) 00:14:50 I think tombstoning and other… yeah, I think there's, like, a bunch of other things. I'm sorry, that was the finish. No, you're right. Okay, I see what you're saying.
David Ashpole (Google LLC) 00:14:59 I think… If we get this across the finish line, and we're happy, Yeah. I don't think… Rust and Java are going to say.
Let's change everything. I think.
Tyler Yahn (Splunk) 00:15:10 Yeah.
David Ashpole (Google LLC) 00:15:11 like, there are aspects of it I'm not… Super happy with, but we've shown that we can work around them, which is the whole, like, the… cardinality… Overflow decision has to be made at the first bind. It is never remade.
Tyler Yahn (Splunk) 00:15:30 Yeah, that thing is a… that thing is… Yeah.
David Ashpole (Google LLC) 00:15:34 Which is what makes this so complicated, right? So, I think… But all that is to say, it is waiting on… it is waiting on us to get it in. So I think as soon as it's in and we're happy, if we're not happy with how it looks, then we should push back before we go through all of this, probably.
-Oh.
Tyler Yahn (Splunk) 00:15:50 Well, the only thing that, like, I wouldn't be happy about is, like, the use of the API. Like, I don't actually think that, like, our implementation of this.
David Ashpole (Google LLC) 00:15:59 Yeah.
Tyler Yahn (Splunk) 00:16:00 Because, like, honestly, you've shown that, like, you can be very performant.
even if, like, I think that we can get a performant implementation of what we're doing, like, just what I laid out right there, even if that's not performant, say there's, like, an extra allocation or something like that we can't avoid, which… It's not the case, but let's just say it is. Like, I don't think that that's actually what I need to do to evaluate for the specification. It's more about, like.
what's the return type gonna be from this bind method? You know, and what's the options passed to this bind method that I care about more? Because that's the stable side of things, right?
David Ashpole (Google LLC) 00:16:33 Having looked at this, Do you feel like we should have new… Instrument types that don't have… that don't accept options?
Tyler Yahn (Splunk) 00:16:44 Dude, don't accept options.
David Ashpole (Google LLC) 00:16:47 Or that accept… A set of options that is different from the standard options.
It's like, if we return… so the alternative world, right, is where we have bind, and it takes… attributes.
Or potentially takes attributes and some other bind options, right? I don't know if we need to… but let's set that aside. Bind takes attributes and returns… instead of an N64 counter, it would return a bound N64 counter, and that would not… The thing that you could do with that would only take context and a number.
It wouldn't take the… Options that come after it, right?
Tyler Yahn (Splunk) 00:17:32 Yeah.
David Ashpole (Google LLC) 00:17:33 Maybe it has to take… maybe it has to take options. I don't know. That's weird, then, because… Maybe we would… like, it feels like it's hard for us to evolve it if there is ever, like, a different thing to pass, I don't know.
Tyler Yahn (Splunk) 00:17:46 Yeah, like, like, the first thing that stands out is, like, with timestamp, right?
Like, if you needed to change the start time of a bound, like, measurement, like, you wouldn't be able to do that, yeah.
David Ashpole (Google LLC) 00:17:57 So I… I guess it's like, if we didn't accept the same interface, then we would need to accept one that is exactly the same as our current one, minus the with attribute one.
Tyler Yahn (Splunk) 00:18:09 Yeah.
David Ashpole (Google LLC) 00:18:10 Which would just be, like, a ton…
Tyler Yahn (Splunk) 00:18:14 Yeah, that's just… yeah, yeah.
David Ashpole (Google LLC) 00:18:16 So it's like, that's the only other API I could see.
It would be nice if it were… Like, I don't love the spec being written as, like, do A or B, because…
Tyler Yahn (Splunk) 00:18:26 Yeah, because then all those different implementations are like, I liked A, but you have B, like, why can't you have… Yeah, yeah.
David Ashpole (Google LLC) 00:18:34 Why can't you do what Java does?
Or… actually, I would rather be in our position, though, where we're more lenient. It's probably more like Java's gonna be like, hey, why don't… can you add attributes to the bind? I really like how in Go I can, you know, bind, and then throw in my error.type at the end when it goes wrong, right?
Tyler Yahn (Splunk) 00:18:54 Yeah, yeah, exactly.
Which I do like, but yeah.
David Ashpole (Google LLC) 00:18:58 But it… right.
Tyler Yahn (Splunk) 00:19:02 I also like… but it's also, like, one of those things where… Java's probably gonna have a more performant implementation, because it's like, well, the people that are throwing in that error type are not knowing that, like, they're causing, like, a recalculation of these attribute types and things, so…
David Ashpole (Google LLC) 00:19:16 But error type is… At least from my… Error type is usually dynamic, right? You don't know how much instrumentation is gonna, like, pre-compute it, so it's not like you could pre-bind all of your error types ahead of time.
Good, I suppose.
Tyler Yahn (Splunk) 00:19:32 There's a few. I think we do that in, like, I feel like we tried to, at least. There's, like, you know, 3 known errors that we're gonna return, and, like, if there are those, then we do it, but…
David Ashpole (Google LLC) 00:19:42 Yep.
Tyler Yahn (Splunk) 00:19:43 we were really, anyways, not really relevant. But, but yeah, so, like, that's kind of, I think… I don't know, I think that, like, returning the instrument that we have seems… seems valid.
The only other downside that I would… Say there, though, is that, like, I might… it might be cool to tie the finish into a bound instrument, is kind of the thing.
David Ashpole (Google LLC) 00:20:11 Bind to attributes, and then… Yeah, I… There was another…
Tyler Yahn (Splunk) 00:20:24 Right? Because, like, the finish…
David Ashpole (Google LLC) 00:20:26 I know what you mean.
Tyler Yahn (Splunk) 00:20:27 Yeah, okay.
David Ashpole (Google LLC) 00:20:29 It's like, bind, and then… Well, originally there was this desire to have an unbind, Like.
It's kind of like how in a, When you register a callback, you get an unregister… an unregisterable thing back. So it's like, you would bind, and you would get an… unbind… unbind back, right? That, like, basically can tell the SDK to go… I don't… I don't need this anymore, go clean it up. Which… it's like, I like… But I feel like I need to be able to finish instruments that are not… bound. Like, one thing that… I was thinking with the finish method was, like.
could we add a shutdown function to all of our instrumentation libraries? So I can, like, have my… HTTP client, and I can use it for a while, and then be like, oh, I'm actually done with this.
Let me shut it down.
And, like, let everyone know that, yeah, I'm not calling this destination anymore, for whatever reason.
Hmm. And, like, is there… is there a way that we could have that Be like, yep, let's finish all of our instruments.
Before we, you know… right now, I think we unregister our callbacks, maybe.
And that would probably be it. But it'd be nice if we could also be like, yep, these counters and stuff are not going to be incremented anymore.
in an ideal world, like, OTEL supports Nice little, staleness markers, or something like that, so that the lines in my graphs stop at a very natural place, you know, when the client disappears, like…
Tyler Yahn (Splunk) 00:22:17 Yeah, but, like, why wouldn't you just shut down the provider?
David Ashpole (Google LLC) 00:22:22 Will it… the whole provider?
Tyler Yahn (Splunk) 00:22:24 Yeah.
David Ashpole (Google LLC) 00:22:25 It might just be, like… I feel like there are applications where What's… what's a good example?
It would have to be where I have I know we got some bugs about this, especially with gRPC, for whatever reason, where people were, like, dynamically creating gRPC clients.
For whatever reason.
There were some, like, memory leaks reported a while ago, is what I remember.
But, like, it… the provider…
Tyler Yahn (Splunk) 00:23:05 I remember later.
David Ashpole (Google LLC) 00:23:05 Biden.
The provider's tied to the lifecycle of the application, though, right?
Tyler Yahn (Splunk) 00:23:10 Yeah, yeah.
But, like, why wouldn't… Why would… so, oh, so you're saying that, like… That your client may not be tied to the application lifecycle?
David Ashpole (Google LLC) 00:23:25 I'm… I'm pretty sure we've seen that out in the wild. I… I don't… I've never written anything that does that.
Tyler Yahn (Splunk) 00:23:32 Yeah.
David Ashpole (Google LLC) 00:23:33 But that would be the, like… To me, that would be one of the ideas. It's like, it would be nice if… if, like, yeah, I could have a client or something that's… Short-lived, or that lives for a day or two.
And then, I don't need it anymore, and I can… Destroy it, or something.
Tyler Yahn (Splunk) 00:23:58 I mean, I'd… I, I…
David Ashpole (Google LLC) 00:24:01 I guess I feel like that's one of the things missing from… one of the reasons why I want Finnish is, like.
Tyler Yahn (Splunk) 00:24:07 Hmm.
David Ashpole (Google LLC) 00:24:07 I'm either monitoring… I'm monitoring a bunch of stuff, and then all of a sudden, for whatever reason, I don't need to monitor anymore. Whether it's, like, a bunch of… Like, a client seems like an easy example, because it's like…
Tyler Yahn (Splunk) 00:24:23 Yeah, like, I get the idea that, like, you want to, like.
turn off telemetry. Like, that makes a lot of sense to me, like, I don't… usage pattern changes, like, you know, time-wise, things, you know, come or go, or something like that, like, but, like.
Yeah, the fact that, like, you would have an application that no longer uses a client, and you're like, well, this would just no longer exist anymore, I don't know, like, I'm not opposed to it. I do think that the finish method is warranted, though, like, for that exact reason, because you do want telemetry to, like, go away. But going back to, like, the bind question, though, it's like, it's more about, like.
I guess saying that, like, for… I don't know, I know that this, like, user has come in, and they're gonna ask me for all these things, and that, like, there's going to be, like, another 20 minutes of me doing some, like, really intense work, right? So I'm gonna bind this instrument really quick, and I'm gonna, like, do that here. But at the end of that, I just wanna say, like.
hey, all this behind instrument stuff, like, I'm done with it, so, like, destroy it, like… I don't know, in some ways. So essentially, like, calls to it afterwards would be no ops, But, like, you can't do that currently, right? Like, because if we return an instrument… I guess we could, right? We could do the same thing, we could play around with, like, returning an, you know, an additional method that's not really exported, but you could do an interface satisfaction and say, like, hey, actually, this can be destroyed, or something like that, right? Like…
David Ashpole (Google LLC) 00:25:50 Okay, the what happens if you continue to call it after you've… you know.
Tyler Yahn (Splunk) 00:25:54 Yeah, that's, that's, like, I don't know, that seems pretty obvious, like, just, ignore it.
David Ashpole (Google LLC) 00:26:01 Yeah.
Tyler Yahn (Splunk) 00:26:01 Right, right.
David Ashpole (Google LLC) 00:26:02 We already have that, yeah.
Tyler Yahn (Splunk) 00:26:03 Yeah, like, but honestly, actually, maybe that's actually a good point, because, like, This could be a part of the bind interface.
Right? Like, this could be a part of, like, the metric interface that, like, we're… debating right now in the PR on, like.
the, you know, not only does, like, the bind take, like, a, you know, this option to create the instrument, but, like, that also could be, like, a finish or something like that, like, included in that. Like, there'll always be something that is going to be callable for that particular thing.
David Ashpole (Google LLC) 00:26:34 You know what? You know what I would really love?
But everyone's gonna hate me for it, is, like… I would like… To be able to bind on a set of attributes?
And then, sometimes still record It would be cool if I could double bind. So I could, like, bind to one set of attributes, and then sub-bind to a different set.
Tyler Yahn (Splunk) 00:26:59 Absolutely.
David Ashpole (Google LLC) 00:26:59 But then if I finish the first set, it all goes away.
Tyler Yahn (Splunk) 00:27:03 Oh, even the second one?
David Ashpole (Google LLC) 00:27:06 Right, so it's like, if I bind to…
Tyler Yahn (Splunk) 00:27:09 Yeah, like, some…
David Ashpole (Google LLC) 00:27:10 odd name or something. Yeah. And then later, I'm like, oh yeah, and bind to, like, some HTTP server stuff, and… Like, whatever other attributes exist. Yeah.
But then if I go and nuke the original binding, it's all.
Tyler Yahn (Splunk) 00:27:23 like, the pod gets, like, deleted. You're like…
David Ashpole (Google LLC) 00:27:25 pod gets deleted, and there's 7 million series underneath that pod that have been bound in various ways for performance, but I can say, oh, this thing here that I originally bound is, like, gone now. And then all of that just gets marked stale and stopped.
It's like, that… that would make me pretty… pretty happy if I could have that, but it requires… It requires multi-bind support.
Which…
Tyler Yahn (Splunk) 00:27:51 Which I think would be great. I think we should do that, but yeah.
David Ashpole (Google LLC) 00:27:54 Right. Which is one of the things that the… if you embed the original instrument, you would get, right? Because you can always… or… Yeah, you can always, like, if you can find an instrument, then you can bind it again.
Tyler Yahn (Splunk) 00:28:06 Yeah, yeah, exactly, yeah.
David Ashpole (Google LLC) 00:28:09 Yeah, I… I like… I like that.
Hmm.
Tyler Yahn (Splunk) 00:28:16 I've always thought that that was a good idea, like, I've thought… I've considered doing exactly that.
In fact.
I wrote that extra package that does binding on top of our existing API, but just isn't performant. I think I implemented it there.
David Ashpole (Google LLC) 00:28:30 Yeah.
Tyler Yahn (Splunk) 00:28:31 Yeah.
So, like, yeah, I definitely think it's a feature we want, like, yeah. Although the deletion from the top down, I don't think is there. It's more just of, like, the rebinding concept was there.
David Ashpole (Google LLC) 00:28:43 I mean, I would… It's like, I know if we want to talk about, like, the Finnish, stuff, and… it's like I… I do like the idea of… It's like, I understand the performance concern with hey, I'm finishing… And it has to do a search to find the things. I feel like this is one way that we can solve that, is if… if… If an SDK wants to be performant with an unbind that targets 1,000 series, then it It can, like, keep a reference to something that has… that knows.
Tyler Yahn (Splunk) 00:29:23 It was all mysterious within.
David Ashpole (Google LLC) 00:29:24 or… right?
Tyler Yahn (Splunk) 00:29:26 Yeah, because then what you could do is you could even, like, just bind to nothing, and then you get something that can be… essentially act as the node. You can be like, give me an empty bind, but then, like, this just acts as, like, a finished node, where anything below it, like, I can just kill it immediately.
David Ashpole (Google LLC) 00:29:39 Yeah, yeah, well, that would… that would kill everything globally, right? Or, like.
Tyler Yahn (Splunk) 00:29:42 Early on what…
David Ashpole (Google LLC) 00:29:43 That's on the instrument, right?
Tyler Yahn (Splunk) 00:29:44 Yeah, exactly, yeah.
David Ashpole (Google LLC) 00:29:45 But if… like, the Finnish use case that I… have always, like… or that keeps… like, I did a bunch of stuff with CAdvisor, right? And so, like, the classic CAdvisor thing is, like, my container goes away.
But… it has 75 different time series with a variety of labels that I can't be bothered to… cash and keep track of, right? Okay. So it's like… It's like, it'd be nice if I had a handle to say.
this container with this ID, and maybe this PID or whatever, went away.
At least finish all the stuff associated with it.
It's like… if I have to finish all the series individually, then that's a ton of work, right? Because I have to… I have to have, basically, a copy of the sync.map keys that are sitting in the SDK, which, like, I don't.
Tyler Yahn (Splunk) 00:30:40 Well, or you could be Obi, and you have, like, two copies.
David Ashpole (Google LLC) 00:30:42 Or you… or you're Obi, and you… Yeah, and you've got lots of maps all over the place.
Tyler Yahn (Splunk) 00:30:47 Yeah, yeah.
David Ashpole (Google LLC) 00:30:48 Which, right, so… So there's that part of it.
But if I was able to, when I first discovered the container.
bind to a set of attributes and keep that handle for, like, the container destroyed.
then, like, I… yeah, I don't… I don't need a finish method that's fancy.
I just need it to be able to undo the binding. Yeah. And I think… so, I like this.
I would be happy to prototype it and put it in the SDK if your goal is to unblock OB.
I think the pushback that we would get from… So, for whatever reason, for Java and for… Rust, I think, was the other one, right?
They, in the discussions, they really didn't want One, they didn't… they wanted Bind to be able to return an interface that only lets you record measurements, that doesn't let.
Tyler Yahn (Splunk) 00:31:48 Right.
David Ashpole (Google LLC) 00:31:48 Right? So, I think there's that hump to get over.
Maybe we could sell it if we talked about how Unbind could work?
And then the other hump, I think, is… There's multibind, but then there's… Oh, goodness.
Is that it? I think that might be it.
I think we would need to require, like, Oh, they… they don't want… I think they were weary of Bind becoming the… generic, you should always use this to record things, like, It is.
Tyler Yahn (Splunk) 00:32:26 So, like, if you wanted to record with an attribute instead, you're gonna, like, bind first, record, and then just delete it, kind of thing?
David Ashpole (Google LLC) 00:32:32 Well, right, so that's what you would… That's what you would do if you wanted So, in their mind, they want Bind to be reserved for the use case where You know this is going to exist for… Forever, and you want to… Record this attribute set.
really quickly, right? Like, basically, kind of like a pay a high upfront cost for the bind function, pay a lower per measurement cost later.
Yeah.
Like, for us.
it would actually be more performant, even if you were rebinding every time. And so, one of the reasons they wanted it called bind in the first place, instead of, like, with attributes or something like that.
is because they wanted to make it clear that, like, this is bad if you're calling bind every time. Like, you should think of this as, like, big, heavy, stateful function, not… lightweight.
I'll bind and increment, whatever.
Tyler Yahn (Splunk) 00:33:36 It kind of is, though.
David Ashpole (Google LLC) 00:33:38 Can we… if we return… if we return an unbind, that can be, like, a trivial struct, right? It doesn't… it doesn't need to allocate or anything like that.
Because that would kill it.
That would kill me.
Tyler Yahn (Splunk) 00:33:54 No, I mean, I don't think it does.
Like, it needs to keep a reference to its pipeline, and it needs to keep a, like, some sort of… preference to… Honestly, I think just a distinct, I don't even think… well, actually, maybe multiple distincts, if there's, like, views involved, right? Because there could be fan out, that it could actually be unbinding. But, like.
the reference to the pipeline's already in memory, so, like, that actually isn't an allocation. The, The reference to the distincts is maybe a slice.
David Ashpole (Google LLC) 00:34:29 It would be crazy to prototype it, but I…
Tyler Yahn (Splunk) 00:34:31 Yeah.
David Ashpole (Google LLC) 00:34:32 I think it takes the… I think it takes Bind further away from what CJO and Jack have in mind, so I think…
Tyler Yahn (Splunk) 00:34:42 Yeah, but I, like, I don't know.
Like, I think that's great for them.
I think… I think that Bind has, like, a really good use case in their world, and, like, their worldview on, like, how it works, but, like.
we have some serious limitations in the Go ecosystem around performance, right? And, like, functional, like, usage, right?
David Ashpole (Google LLC) 00:35:07 I think the, like, width pattern, or, like, the do excellent Dubai is, like, very… good performance, generally, for Go.
Tyler Yahn (Splunk) 00:35:18 Yeah, I agree, and like, yeah. But if you wanted to get on the order of Rust.
like, just as an example, if you wanted to get on an order of, you know, Rust's measurement thing, like, they're like 3 nanoseconds per measurement, right? Like…
David Ashpole (Google LLC) 00:35:34 It's not that far from where we are for an atomic counter. All my benchmarks are contended, so I think goes… the thing with Rust is that you can have I think you can have thread locals, which we don't have, so, like.
Tyler Yahn (Splunk) 00:35:47 Exactly.
David Ashpole (Google LLC) 00:35:48 Under contention, they can still keep that 3 nanosecond.
Tyler Yahn (Splunk) 00:35:51 Yeah, yeah.
David Ashpole (Google LLC) 00:35:51 Right? Whereas under contention, we go up to, like, 20 nanoseconds.
Tyler Yahn (Splunk) 00:35:55 Exactly. And it's like, in 20, 20 seconds is great, like, honestly, like, yeah, it's like, I'll take it, but, like, I don't know, like, if you're doing things, like, trying to compete with Rust, like, yeah, like, how do we get lower? Like, I think that, like, the bind… world starts to, like, make sense for us at that point, as just a performance reason alone. So, like, if we need functional elements there that Rust doesn't need, then, like.
okay, maybe they don't get stabilized and put into, like, the stable API, but, like, at least we have some solution space where we're like, hey, look, this experimental feature is here, like, it's not stable, but, like…
David Ashpole (Google LLC) 00:36:29 It's more that I think if we implemented finish the way we're talking about doing finish as being, like, a return type on bind.
Tyler Yahn (Splunk) 00:36:36 Yeah, yeah.
David Ashpole (Google LLC) 00:36:37 That… I don't know if that would fly as well for other languages, because it… it means that in order to get your finish function, you have to use bind.
Tyler Yahn (Splunk) 00:36:48 Oh, why don't you do both?
Yeah.
David Ashpole (Google LLC) 00:36:51 No, no, I agree, I'm just saying, like.
I don't know if they would like that design for finish, because it requires them to do things with vines.
Tyler Yahn (Splunk) 00:37:01 No, I, like, so I definitely don't think that, like, we should have it be, that's the way that you finish, is because you have, like, an additional bind. I definitely think we should have, like, the finish… function as I have it laid out, but then also, I think that the binds instrument itself should… should have this finished, like, capacity as well.
David Ashpole (Google LLC) 00:37:20 You think it needs both?
Tyler Yahn (Splunk) 00:37:22 Yeah, yeah, I definitely do.
David Ashpole (Google LLC) 00:37:24 I was thinking if we had… if we had, like, finish as a thing that was returned from bind.
that… We wouldn't hear from the finish. I think that.
Tyler Yahn (Splunk) 00:37:34 No, I think we still need the original for all the people that are still just, like, not gonna use the bind instrumentation. I think that, like, you're still gonna have people out there that are just, like.
I'm gonna do all these measurements, like, like, Obi, like, I don't… Well, I mean, I guess we could try to do this bind thing.
David Ashpole (Google LLC) 00:37:52 I mean, it's just a different way to pass attributes, right? It's like, it's not rocket science.
Tyler Yahn (Splunk) 00:37:57 No, it isn't, and, like, we could also try to do this, like, finish thing. The only, the only problem is, is that, like, right now, Obi tracks the attributes, and it would have to start tracking these instruments, right?
Because, like, right now, it's like, oh, like, look, I know that this… this thing is about to end, like, I'm done, kill this attribute, so it calls the finish with the attributes. Instead, it would have to be, like, I know this thing's about to finish, do the lookup, get me back the instrument, and then call the finish on that instrument instead.
David Ashpole (Google LLC) 00:38:28 So it would need to… the way to think… the way I would think about it, in terms of code design, is that when you first start interacting with something that you're gonna monitor.
You do a bind.
And so then you've got a whole bunch of bound references that you use for measuring things, and you hold on to those, right? Because you're doing increments with them and stuff.
And then when it goes away.
Then you do all your finishes.
Tyler Yahn (Splunk) 00:38:55 But that's the thing, it's like, but when it goes away is the hard part for us, right? Because, like, so I have these references, but essentially what I have to do is I have to hold those references in a map, right? Because, like, I have one probe fire for Obi, and it's like, start something, and then the other probe is gonna fire late, like, totally, maybe even a different thread, and it's gonna go, like, hey, this thing's ending, now get rid of it. So I need to do some sort of way to, like, synchronize those and look those up. And the only way we know how to do that, right, is, like, to recreate the attribute set. So I, like, that's fine. Like, currently, right now, though, that means it's just, like… Yeah.
David Ashpole (Google LLC) 00:39:27 I was thinking, you know how we do… Like… It… for our providers, how we tell people to, like, make a shutdown function, essentially, and it's just, like, wraps.
bunch of individual ones. So if, like, if you discover a new thing, and you're like.
I've got 6 metrics I'm… like, gonna measure for this new thing, and so you do, like, bind, bind, bind, bind, bind for all your instruments, and you get back your six unbind functions. I think then you just, like.
Wrap that in a shutdown and hang on to it.
Tyler Yahn (Splunk) 00:40:05 But that's still not, like… it's not a number of instrument problem for us, it's a… it's a mapping problem for us, right? Because, like, what you just said is, like, you get back an instance, and then you have to hold on to that instance, and then call finish on it, right? For us, right now.
like, we get back… we don't get back anything. Like, the map is pushed down into the SDK, is the thing, right? We would have to hold on to that mapping if we got the instance back.
David Ashpole (Google LLC) 00:40:31 how would you… how would you use Bind? I guess is my question, because… you're, you know, you discover a process. Yeah. You discover a process, and you're like, okay, we're gonna… we wanna be able to make increments for… metrics on this process really quick. So you're like, okay, I need to… I've got this… I do my bind, and then I get my instrument back. What do you do with that instrument today?
Or what would you do with that instrument if you had a bound instrument?
For a particular metric, for a particular, like, process.
Tyler Yahn (Splunk) 00:41:03 Well, that's what I'm saying, like, we don't. Like, we essentially create the instrument ad hoc as, like, we have, like, an event come by, and we're like, hey, this event happened, so, like, this is what the instrument name is.
David Ashpole (Google LLC) 00:41:13 So you're, like, looking up the instruments by passing all the stuff in.
Tyler Yahn (Splunk) 00:41:17 Yeah, yeah.
David Ashpole (Google LLC) 00:41:17 So… If you wanted to have.
Tyler Yahn (Splunk) 00:41:25 I mean, essentially what we're gonna have to do is recreate what the SDK does and just hold on to that instrument map. It's just that they're gonna be bound instruments, not.
David Ashpole (Google LLC) 00:41:31 So… Right? It's like, I don't actually think… because so… Here's my, like, mental model, is… there's a map inside the SDK, and when you call bind, it's… More or less equivalent to you saying, please perform a lookup inside your map.
And if this thing doesn't already exist, create it, otherwise return what's there, right?
Tyler Yahn (Splunk) 00:41:55 Yeah.
David Ashpole (Google LLC) 00:41:56 bind is a map lookup on a set of attributes. So, like, you doing… Your own map to do a map lookup.
To find a bound instrument handle.
is re-implementing exactly what the SDK It's supposed to have implemented with the bind function.
Tyler Yahn (Splunk) 00:42:13 Yeah.
David Ashpole (Google LLC) 00:42:14 what I would probably say is, I would… I would treat your stuff as dynamic, meaning I would rebind every time.
But then you're right, you don't… You wouldn't have, like, a… if you wanted to finish.
What you would hilariously do would be.
Tyler Yahn (Splunk) 00:42:31 Finds an instrument.
David Ashpole (Google LLC) 00:42:32 You would bind to get the instrument back, and then… so you'd do, like, instrument.bind.finish, right? And then that would be your, like…
Tyler Yahn (Splunk) 00:42:40 Yeah.
David Ashpole (Google LLC) 00:42:40 thing, right? Which would kind of be… But would… it would also… It would work.
In the sense that if you wanted to finish Like, let's say you had bound to something, and then Rebound a second time.
with… Like, a whole bunch of different… Sub-attribute sets.
As long as when you do the bind and then the finish, as long as it then finishes all the things that are pointed to from that.
You could get, like… A maybe more performant version of, like, finish all these things at once.
But yeah, it's like…
Tyler Yahn (Splunk) 00:43:21 Hmm.
David Ashpole (Google LLC) 00:43:21 It's really… Hurts.
Tyler Yahn (Splunk) 00:43:24 I see, so, like, if Obi is instrumenting, like, your C-Advisor stuff, like… And it was just like, you know, here's this event from C-Advisor, so, you know, Binds… Actually, I don't know how you would do that.
David Ashpole (Google LLC) 00:43:38 if… Think about it this way. If we treat the bind function as a map lookup, That gives you… An add function that's fast?
And a finish function.
Then it all kind of makes sense.
Tyler Yahn (Splunk) 00:43:54 Yeah, but the problem there, though, is that, like, you have to recreate the hierarchy every single time, is the problem. So, like, I get some event from a CA advisor that's like, on this container, there's an HTTP request. So you're like, cool, alright, I need to bind first to the CAdvisor pod ID, and then I need to bind again to the…
David Ashpole (Google LLC) 00:44:11 into this.
Tyler Yahn (Splunk) 00:44:11 host, but, like, maybe I don't have the CAdvisor pod ID as the problem.
David Ashpole (Google LLC) 00:44:17 Well, right.
Tyler Yahn (Splunk) 00:44:19 So how do I know that, like.
Yeah, like, I guess that's kind of my question, is just, like.
David Ashpole (Google LLC) 00:44:24 Yeah, you would have to have everything. I mean, today, right, you're just doing a regular with attributes, and you're passing all the things in, right? So, like, you would have to have all the information, but… and doing two bind lookups would probably be prohibitively expensive compared to doing one, like, just to get your finished function.
Tyler Yahn (Splunk) 00:44:42 Well, no, not even to do that, to get a measurement function, right? So I… I'm just talking about the measurement side.
David Ashpole (Google LLC) 00:44:46 Right, well, I would say…
Tyler Yahn (Splunk) 00:44:48 And then, so then afterwards, I go to the finish, and I'm like, okay, here's an event for the CAdvisor, like, node ID, or the pod ID is going down. Do the bind and finish on that, but, like, every time I did a measurement, I'd have to reconstruct that hierarchy of, like, get my pod ID into this, yeah.
David Ashpole (Google LLC) 00:45:02 I think that that doesn't work well for your use case, and it also… I think the constraint of having to rebind in specific ways to get proper finish behavior is maybe a bad API.
So maybe we've talked ourselves out of… out of that design.
And I also think, honestly, landing two features that don't Have this kind of explicit interaction with each other is probably going to be way easier.
Tyler Yahn (Splunk) 00:45:28 Yeah, but I… I do… I… yes, and I… I can't agree more. I think we should land them both. But then, I think we should continue that conversation about, like, how do they interact? Maybe… maybe before we stabilize, even, like… Because, like, I don't think this is appropriate for Obi, that's why I'm thinking, like, if you had both of them side by side, like, I think Obi could use, like, the finish method.
And then the buying plus finish may be very helpful for the actual C-Advisor, but, like.
Yeah, like, so that… I think that's my question, is like, could they live side by side?
David Ashpole (Google LLC) 00:45:58 I… I guess the… They could live… so, they could live side by side, but the advantage of the finish method that comes from bind, right.
Tyler Yahn (Splunk) 00:46:07 Yeah.
David Ashpole (Google LLC) 00:46:07 We just try and, like.
Assume that the rest of it is all set in stone, right? We have our separate finish method and our buying method.
Tyler Yahn (Splunk) 00:46:14 Okay, yeah.
David Ashpole (Google LLC) 00:46:15 Do we want to add bind to… or sorry, finish to the bind return?
Like, the advantage is potentially Performance-related.
Tyler Yahn (Splunk) 00:46:26 Yeah.
David Ashpole (Google LLC) 00:46:27 or the finish method, where I can finish a large number of series at once without having to do a scan of the whole thing, right?
Tyler Yahn (Splunk) 00:46:35 Yeah. Which… Yeah.
David Ashpole (Google LLC) 00:46:36 Is certainly an advantage.
But the… the drawback would be, one, the second return argument from bind makes it way less ergonomic.
Like, if I… if right now, I can do foo.bind.add, right? And it's fine. If I get two return arguments, I can't do that anymore, which is more an annoyance than.
Tyler Yahn (Splunk) 00:46:57 But, so, so don't have two return arguments. Just have that, like, instrument that you're returning have a method that's finish on it.
David Ashpole (Google LLC) 00:47:05 So, instrument in general has finish.
Tyler Yahn (Splunk) 00:47:08 Well, I mean, like, yes.
And, yeah, right, so, like, yeah, and it's, like, it's an implicit interface, right? Like, it may just be like, oh, you just got the spec, but this is, like, a special instrument that has a finish method on it, and you can just call finish on this, and it will do that whole hierarchy thing.
David Ashpole (Google LLC) 00:47:23 I… I like it, but I don't know if we can make it perform it that way. I'm… I'm intrigued. Of course, if instrument has a finish method, then a bound instrument should finish only the things that are bound to it.
Tyler Yahn (Splunk) 00:47:44 Yeah.
David Ashpole (Google LLC) 00:47:45 But… I think the question is.
Tyler Yahn (Splunk) 00:47:47 What if we… huh.
David Ashpole (Google LLC) 00:47:48 Would we be able to… would we be able to avoid a scan, is the real question.
Right?
Tyler Yahn (Splunk) 00:47:55 I don't… I don't want that, yeah.
David Ashpole (Google LLC) 00:47:57 So, because… If someone has… If we do a bind.
And then someone re… like, there's the whole, like, you could bind 6 different times, and we can't maintain the caches of, like, all the ways that… all the paths that someone has taken to get to a particular attribute set.
Tyler Yahn (Splunk) 00:48:19 Well, I mean…
David Ashpole (Google LLC) 00:48:20 end up having to scan. But it's nice, it's convenient, it's more a convenience because you bind, you get a thing back that has a finish method on it, and if you finish.
Tyler Yahn (Splunk) 00:48:30 Yeah.
David Ashpole (Google LLC) 00:48:30 then it… intuitively is, like, already doing all of the… yeah, I think that's fine. It matches everything that it's already been bound to.
Tyler Yahn (Splunk) 00:48:39 I think you're right. I don't think you can get away from the scan at that point, but, like, that just may be kind of what you're saying, is, like, that doesn't… It's just, it is what it is, right?
Especially if you have views interacting here at this point, or dynamic views eventually, but, like, yeah, like… but I think that might be the way to do it, like, if you don't want this scan, if you want, like, a, you know, deterministic like, finish method, you could just use the finish method itself.
But, okay, I don't… I think we're… I do want to double-check, we are, like, 10 minutes to the end, and Puneet did want to ask about the meter, configuration as well, and so I did want to, like, pause. A lot of this has been relevant, but, like, I just wanted to double check we're including that in the discussion.
David Ashpole (Google LLC) 00:49:26 Oh, did you want to merge the Bound Instrument API PR?
Tyler Yahn (Splunk) 00:49:30 Yeah. Yeah. Okay. Let's do that. I'll hit it.
David Ashpole (Google LLC) 00:49:33 Hmm.
Tyler Yahn (Splunk) 00:49:34 Yeah, I definitely think that's, like.
Let's… let's keep going on that one, yeah, for sure.
On the Finnish one as well, like, I responded to you, but, like.
I'd like it if we could also scope it to just, like, this simple case. I do think that, like, this fan-out, like, scanning stuff.
After this discussion, maybe worth exploring the interaction with the bind instrument, but it also, like, is not saying that, like, we can't add another method for finish, like… Finish fuzzy, or finish function, or finish… like, an additional, like, way to finish.
Yeah. That could actually, like, accomplish all of this. I just… I just wanted to try to do the simple case first, is kind of my idea.
David Ashpole (Google LLC) 00:50:12 I… well, I was… I was trying to decide… If I… like, my gut reaction was actually, I would rather that this only finish the exact attribute set, regardless of filtering.
Tyler Yahn (Splunk) 00:50:24 Hmm, okay.
David Ashpole (Google LLC) 00:50:25 If you applied a filter, it wouldn't…
Tyler Yahn (Splunk) 00:50:28 Finish.
David Ashpole (Google LLC) 00:50:29 But then it leaks memory, is the problem. If you… if you filter out the wrong attribute set.
Tyler Yahn (Splunk) 00:50:34 Oh, right, yeah, yeah, right, okay, yeah, because then if you did do a filtering, then it would just always sit there, yeah. It's like… Yeah, I did think about this, yeah, that's right, yeah.
Yeah, also, the overflow set is really… it's a thorn in the claw on this one as well. Yeah, because that'll also leak memory, because if you start clearing this out, it'll just have a no-op, because it can't… it has no idea what it… Related to eventually. So, yeah.
Although the memory leak is literally just going to be the overflow set, but that's just gonna be what it is, yeah.
David Ashpole (Google LLC) 00:51:05 I don't think we… I think that's fine.
Tyler Yahn (Splunk) 00:51:08 I think you're just gonna have to deal with it, yeah.
But yeah, if you could take another look at that, I don't know… Yep.
I'm also, like, fine… further discussing the implementation, but on the API side, like, if you want me to just remove docs saying, like, what the implementation's gonna do until we actually have the implementation, I can also do that, and, like, we can…
David Ashpole (Google LLC) 00:51:28 Oh, the only other… so I wanted… I felt like this was the more important discussion, but… How would you feel about making this a slice of attributes?
Instead of…
Tyler Yahn (Splunk) 00:51:39 Thought about that. That's the other. I don't want to do that.
David Ashpole (Google LLC) 00:51:42 What? No! Why don't you want to do that?
Tyler Yahn (Splunk) 00:51:45 Cause you duplicate a slice of attributes.
David Ashpole (Google LLC) 00:51:51 Don't… How is it better, like… Tell me, tell me about… So… If you know the slice of attributes ahead of time, obviously, then you just have it and you store it. But that's the same with the set, right?
like, I feel like the set lets you take a slice of attributes.
And then do some extra work on it.
Am I…
Tyler Yahn (Splunk) 00:52:19 I'm just saying that, like.
At the end of the day, you give me a slice of attributes, that's great. I'm gonna have to convert that to a set.
David Ashpole (Google LLC) 00:52:30 You… you will have to hash it.
Tyler Yahn (Splunk) 00:52:33 No, no, because there's also, the filter function.
David Ashpole (Google LLC) 00:52:39 Right, you will have to hash it, so… The key thing to keep in mind is that You can compute the hash of a filter.
with the changes that I merged.
Tyler Yahn (Splunk) 00:52:52 Yeah, yeah, with the lazy set, yeah, I'm with you. But, like.
You gotta, you gotta get it set eventually, right?
David Ashpole (Google LLC) 00:53:01 will not… so, for Finnish, it never records any data, right?
So, you never need to make a set.
you just need to find the thing that you're supposed to find. You're doing a bunch of lookups, and you're saying, this gets deleted, right?
Tyler Yahn (Splunk) 00:53:15 for, like.
David Ashpole (Google LLC) 00:53:16 Like, you market, or whatever.
Tyler Yahn (Splunk) 00:53:17 Okay.
David Ashpole (Google LLC) 00:53:18 The thing never gets stored. We only need-need the set if it's gonna get stored in the, like, data structures in the SDK. If all we're doing is like, marking a Boolean or something somewhere.
Tyler Yahn (Splunk) 00:53:31 Yeah.
David Ashpole (Google LLC) 00:53:31 we need to be able to compare it to what's already in the SDK, But new set is… new set does a copy, and it's kind of heavy. So if we can have it take a slice.
If that's at all a possibility, that's what I would like us to do.
Tyler Yahn (Splunk) 00:53:48 I mean, it is, and I definitely evaluated it. It's in the issue.
David Ashpole (Google LLC) 00:53:53 Okay, I continue.
Tyler Yahn (Splunk) 00:53:54 But, yeah, take a look.
I thought I looked through this, and I thought for the filtering, you still needed the… the set, because, like, the filter function was there, but I might have just missed, like, maybe there's a way we can get around this. Like, obviously, yeah, in fact, like, I had even considered, like, just accepting a distinct, would be great, but that… that won't work with the filter function. But…
David Ashpole (Google LLC) 00:54:18 Well, you could do that, right? Because we now have the primitives, in…
Tyler Yahn (Splunk) 00:54:22 Yeah…
David Ashpole (Google LLC) 00:54:23 the attributes package for someone to do that if they wanted to. It's just a terrible API for users.
Tyler Yahn (Splunk) 00:54:29 Yeah, exactly, right? And, like, the moment that our implementation changes, then, like, I think we could do that even if we… yeah. Yeah, I… yeah, I don't think it… yeah, agreed, yeah.
David Ashpole (Google LLC) 00:54:38 Okay.
Tyler Yahn (Splunk) 00:54:40 what happens when the set is not ordered, and, like, we have to sort the set in… I'm sorry, in the attribute slice?
David Ashpole (Google LLC) 00:54:46 So… I forget what we have to do.
I need to look at.
Tyler Yahn (Splunk) 00:54:56 Do we just use, like, a sink pool for that? Well, no, that's even a bad idea, because it's going to be very blank.
David Ashpole (Google LLC) 00:55:00 I'm trying to remember what we… because we have… so… To… just to, like… we'll have the same problem with bind, right? Bind is extremely similar, where we just need to do a lookup.
Tyler Yahn (Splunk) 00:55:13 Oh, right, yeah.
David Ashpole (Google LLC) 00:55:14 In the lookup case, and so… like, we will have… we will have exactly the same sets of problems, just the things we want to do to the aggregation are different, right? And I thought I had worked through this with Bind.
But I haven't… I don't remember it off the top of my head, because it's been a while, yeah.
Tyler Yahn (Splunk) 00:55:32 I approved it.
David Ashpole (Google LLC) 00:55:33 You do need to… you do need to do some sorting in order to properly compute the hash. I don't remember if it's, like… I don't remember if we just… require that You know, we can sort your…
Tyler Yahn (Splunk) 00:55:51 So we can mutate whatever you give us, yeah.
David Ashpole (Google LLC) 00:55:52 Like, you give us a slice, we'll sort it, and then discard. Like, it seems… It seems like that would be appropriate.
But it also means that you can't do concurrent bindings.
with the same slice. If, like… I see.
That, that feels like… like a reasonable trade-off for performance.
Conscious API.
But…
Tyler Yahn (Splunk) 00:56:20 I'm trying to read your docs on this, but passing the attributes at a record time can be… Yeah, it doesn't really say if this can mutate it, but… Hmm.
Anyways, like, I'm open to changing, like, if there's not a performance, Hit to passing…
David Ashpole (Google LLC) 00:56:41 benefit overall.
Tyler Yahn (Splunk) 00:56:43 Yeah, if there's a performance benefit, like, I'm fine switching this. Like, that… the only reason I chose the set was just because I thought it was the performance one, based on, like, allocations, but if that's not the case, then I'm happy to switch.
David Ashpole (Google LLC) 00:56:54 This, this is, like, our, our, what is it, perennial?
Problem is that we… We've pushed a lot of the allocations onto the users, like.
provisioning of the set, and so it makes our SDK look really good, but actually, like, end-to-end, it's better to push this complexity into the SDK, because we can… do smarter things. Like, if the if the finish… Or… if the bound thing already exists, then we can just return it, right? And we never need to actually create the set. Like, we can be.
Tyler Yahn (Splunk) 00:57:26 Yeah, I gotcha. Like, but I definitely think there's ways that users can also optimize with our original API design that, like, we couldn't in the SDK, but, like, I think here, if we can get away from, like, ever creating a set and just only create, like, hashes, then I agree, let's just do that. But it's just a matter of, like, how possible is that, I guess, is the question, yeah.
So I can take another look, and then we can iterate on this. But yeah, that's good feedback. I'm happy to… Yeah.
David Ashpole (Google LLC) 00:57:53 I… yup.
Tyler Yahn (Splunk) 00:57:53 I do think that, like, we need to do one. What we just merged either needs to switch to a set, or we need to switch this out of a set, so…
David Ashpole (Google LLC) 00:58:01 I, I agree.
Tyler Yahn (Splunk) 00:58:02 I didn't think… I didn't think about that, but, but yeah, let's… let's… let's try to come to an answer, which I think is going to be this periodic attribute sounds reasonable, so, yeah.
David Ashpole (Google LLC) 00:58:12 Okay.
Tyler Yahn (Splunk) 00:58:13 Yeah. Okay.
Sorry, Puneet, we're almost at time here. I'm guessing that wasn't that helpful.
Puneet Singh 00:58:22 That's alright.
I mean, I can, I can just quickly iterate if you guys have, like, 2 or 3 minutes.
David Ashpole (Google LLC) 00:58:30 I can stick around.
Puneet Singh 00:58:32 Yeah, so I think based on the feedback from Tyler, I think, he pointed out some issues with the configurator, that if it tries to self-instrument, like, try to use same meter provider.
It can result into a deadlock, because the meter creation path is like building the they configure it.
Changed the implementation to version stamping, rather than holding the lock on the… So apart from other things I've addressed, I think two things I wanted to raise is the definition of no-op meters, that expects that when the meter is disabled, it should be no-op.
But in case of meter configurator, I think there's also an enable case also, that you want to hold the machinery, the pipeline that is attached to the meter when it gets enabled, and that means, in some cases, also holding its accumulated state, so… I lean more towards that the meter has to hold its internal… machinery, that it cannot be simply converted to no-hop, so that's where I think the… spec needs to be improved, as in what no-op means. Is it exactly no-op, or it is like no-op? That is one aspect.
Another is that the scope just simply doesn't cover the… the reading side of things. It's not that I disagree with the feedback, but because the spec doesn't cover the reading side, I would like to fix the spec first, then come to the code.
It takes the scope of the PR.
It works now.
reading the… I mean, writing the metrics, getting that part.
That's… that's…
Tyler Yahn (Splunk) 01:00:16 Yeah, I'll… I'm… it sounds like… some spec issues are in order, and maybe some PRs at the spec level, right?
Puneet Singh 01:00:23 Yam.
Tyler Yahn (Splunk) 01:00:23 Yeah. Do you have time to… I don't know what time it is for you.
it's probably… if you can make this meeting, you can probably make this spec meeting on Tuesdays. It's also worth discussing there.
I think it's an hour before the meeting would have been today, on Tuesday, though.
So, yeah, that's a great place to, like, have more detailed discussions. You can have a whole group that is dedicated to, like, thinking about these things. So, yeah, if you can create some issues and then just raise them in that meeting, like, that's a great way to, you know, like.
Get some feedback outside of this group, because, like, we can't make universal decisions here, like the spec can, though.
Puneet Singh 01:01:00 Great.
But yeah, I mean, in case… I've mentioned these things in the PR also, so in case… I mean, I just wanted to know that what is your viewpoint regarding this observation, like… Do you think that it should be exactly no-op?
Or, or, you know, that… It doesn't make sense to build no op, because as soon as it is enabled, it needs to… Reconnect with the aggregator state and start writing the, metrics, so… Have a look.
Tyler Yahn (Splunk) 01:01:31 Yeah, I mean, I think it should be no up, but that's just because… I don't think there should be any performance overhead, and I don't think that the configurator makes a lot of sense for the Go SDK. But, like, in the Java world, like, they obviously probably already have a solution, or have a different opinion on this, because, like, they have an implementation, they're using a lot of this, so yeah, I would want to know.
David Ashpole (Google LLC) 01:01:51 It would be… I would love to know what they're… what they do in this.
Tyler Yahn (Splunk) 01:01:55 Yeah.
David Ashpole (Google LLC) 01:01:55 I… It reminds me a little bit of, like, the delegating global we had to implement.
Where… It's not a no-op.
Yeah. But it's sort of a no-op, and…
Tyler Yahn (Splunk) 01:02:08 Yeah.
David Ashpole (Google LLC) 01:02:08 I don't know if I want to take on that complexity twice.
Because… It was hard enough to get that right the first time.
Tyler Yahn (Splunk) 01:02:17 Agreed. It still is a challenge. By the way, the global is a thorn in this, complete Implementation of the interfaces that we just discussed for all the experimental stuff, but… We don't have time to talk about that now. Go see the issue.
David Ashpole (Google LLC) 01:02:32 Yep.
Tyler Yahn (Splunk) 01:02:33 Yeah, it's a disaster. But anyways, yeah.
Pretty… definitely worth… I think bringing to the spec meeting, because I'd love to hear more from other groups on this one, for solutions, is probably what I would want the answer to be, so, yeah.
Puneet Singh 01:02:45 Hello?
Tyler Yahn (Splunk) 01:02:46 Okay, cool. We are at time, over time. I'll see y'all in a week. Bye.
David Ashpole (Google LLC) 01:02:50 Nope.
Thanks.
