SIG: Android SIG
Date: 2026-10-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Vishwan aranha** 02:43 Hey guys, morning.
**Cesar Munoz** 02:48 Hello.
**Jason Plumb** 02:49 Hello!
**Cesar Munoz** 02:50 boring.
Hey, Jason.
**Jason Plumb** 02:56 How's it going?
**Cesar Munoz** 02:59 Good.
**Jason Plumb** 03:13 Alright, we've got a very light agenda, so please add yourself and any items you may wish to discuss today.
I will put a link to the doc in the chat.
While we're getting set up, in case anybody didn't have it handy.
And we'll start in just… oh, we're already 2 minutes in. Okay, so… Yeah, we're at that time of year, aren't we?
What, yeah.
**Vishwan aranha** 03:56 So next 25th, I think it's… for Europe, it's, daylight savings time, and for US and North America, it's, like, November 1st, so that week is gonna be… that's why my… all my meeting schedules are messed up at Grafana, so I don't know about you guys.
If you have the same stuff, but I probably won't be attending this meeting because I have some important meetings conflicting with this one next week, so… Okay.
**Jason Plumb** 04:22 Yeah, that's gonna happen for, like, I think there's, yeah, there's this window where stuff is shifted.
Yeah, let me verify when it is in the US.
I think… What you said for November 1st sounds right.
**Vishwan aranha** 04:35 Yeah.
**Jason Plumb** 04:42 No, why would… why would my Outlook calendar show something as important as daylight savings? Like, outlook? No. Okay.
Let's just go with it, yeah.
In about a week.
And Vishwan, are you in Europe, or you're in the US, right?
**Vishwan aranha** 05:09 I'm in the US, I'm in Syraca Springs, New York, so… Okay.
**Jason Plumb** 05:13 That's right, East Coast.
Okay, cool. Thanks for pointing it out, yeah, it's… I forget every single year.
Okay, Cesar new API.
**Cesar Munoz** 05:27 Yeah, just created that PR.
And, if you have some time to take a look, because… Well, it's based on a proposal that I created a couple of weeks ago.
to add a way to extend, OpenTelemetry ROM without actually extending OpenTelemetry ROM.
**Jason Plumb** 05:49 Yeah, cool, okay.
**Cesar Munoz** 05:50 That's pretty much it, we have. Because I think Vishwan… Needed something like this? Well, after what we discussed in… one of, the PRs created.
So yeah. Any questions? I know this might be a bit, maybe a controversial API, probably? So, please go ahead.
And let me know.
**Jason Plumb** 06:19 Cool. It is part of the… it's part of the agent API. Does it have changes in the agent? It looks like it doesn't.
Cool, so these are extensions.
Is there an example of how to use this?
**Cesar Munoz** 06:35 in the… Yes, but not in this PR. I'll update the description. It's in the other one.
**Jason Plumb** 06:41 That's cool. Yeah, if there's, like, a concise little description, like, I see some code down here, that might be helpful in the other PR.
**Cesar Munoz** 06:49 Yeah.
**Jason Plumb** 06:50 Or even in, like, the… if there's a README, or… I don't know, if there's a relevant, like, API README.
**Cesar Munoz** 06:57 Yeah, well, it's got documentation, but I'll add the code examples. I think that helps a lot in the description.
**Jason Plumb** 07:03 Cool. Yeah, yeah. That's awesome.
Okay, are we ready to move on from that one? Sounds like it. Ben has a question about Android TV, slash Fire TV.
**Ben Joseph** 07:21 Yeah.
**Jason Plumb** 07:22 Google TV, it might be the same.
**Ben Joseph** 07:25 Yeah, probably. I, yeah, I just wanted to, like, ask if, Have we… have any of you tried this with TV products? Any experience, Do we claim support?
Yeah, just, just want… just curious, anybody have ever tried it?
**Jason Plumb** 07:46 No, but if your employer wants to send me a Fire TV, I'll try it.
**Ben Joseph** 07:50 I haven't got one yet.
**Jason Plumb** 07:53 I haven't heard of anyone successfully having tried this yet, but I'm also really curious.
**Cesar Munoz** 08:01 Yeah, me too.
**Ben Joseph** 08:06 Okay.
**Jason Plumb** 08:07 Anyone else on the call have any experience or have tried this with either of these platforms?
**Vishwan aranha** 08:12 There's an Android TV emulator. I can try with that, but I don't have a TV. I used to work for a company in the past, in 2018-19 where Android TV and Fire TV were a must.
And it was challenging. I had devices then, but I don't have any more, but I can try with my Android TV.
**Jason Plumb** 08:33 Cool, yeah, interesting. I'm very curious how it's gonna work out.
**Ben Joseph** 08:39 Yeah.
Okay, that's good to know we have emulators and… Yeah, I'll also probably test this out, yeah.
**Vishwan aranha** 08:48 You can…
**Ben Joseph** 08:48 together.
**Vishwan aranha** 08:49 Yeah, you can try the Pixel or other Android TV emulators that are available. It's never the best resolution, but it's… It's there, so it's free.
**Ben Joseph** 08:58 Is this available within the Android Studio?
**Vishwan aranha** 09:02 Yes, it's available in Android Studio, you can create one, and play with it, yeah.
**Jason Plumb** 09:07 So… I guess, from a technical standpoint.
in my brain, I've always just compartmentalized those things as being like, oh, well, they're just Android, but is it, like, it's a customization of Android? Is that right? Like, is there a place to find details about how Android TV differs from the Android platform?
**Vishwan aranha** 09:27 Android.
**Jason Plumb** 09:28 work out.
**Vishwan aranha** 09:29 It's basically… Android TV doesn't have as many customizations, it's almost the same, but Fire TV has some custom… I can send you guys the links, so you guys can go through it. I'll send it in the Slack channel.
**Jason Plumb** 09:43 Okay, cool. Yeah, it is… I'm just curious, because I don't… I haven't ever seen those kind of enumerated, and it would be nice just to understand how… how they're customized, or how they're different.
**Vishwan aranha** 09:55 Let me send… yeah, it's easy to set them up, but I don't think there is as many differences. But the only problem is the way it's set up, so… let me see.
I haven't set up an Android 2 emulator in 6 years, I don't know if anything has changed since.
**Ben Joseph** 10:16 All right, yeah, I was just curious if anybody had any experience, sounds like Vishwan does, at least with generic Android TV.
So I'll follow up.
Yeah, if I test this, I'll report back how it goes.
**Cesar Munoz** 10:34 Good.
**Jason Plumb** 10:34 Sounds good to me.
**Ben Joseph** 10:36 That's all I had, thank you.
**Jason Plumb** 10:38 Yeah, yeah, so it sounds like Marius… Hey, is this your first time joining us?
**Marius Constantin** 10:43 Yeah, so I wanted just to introduce myself first.
**Jason Plumb** 10:46 Yeah.
**Marius Constantin** 10:46 My name is Marius, I'm from Datadog, so I will be attending your meetings from Datadog behalf.
on behalf of Datadog, so… I wanted to actually introduce myself first, and second, just because I wanted to figure out the code a bit on OpenTelemetry, I found out some fixes to do, so one of the fixes was this one. So I wanted just to discuss with you guys if you think that this is something that you might need it.
we can drop it, there's a draft in there. I actually… actually open, share this on a channel, on OpenTelemetry, Android channel.
In Slack, there were some interests… reviewers in there, but I didn't get any review yet on that one, so I was just wondering if we should just go ahead with this one, where… Where we just drop it.
**Jason Plumb** 11:42 Cool, so what this… it sounds like,
**Marius Constantin** 11:45 Yeah, so basically, you want me to give you, like, a gist of it? Like, just…
**Jason Plumb** 11:49 That would be great, I think, yeah.
**Marius Constantin** 11:50 So basically what has… what's going on, because I was trying to figure out, like, okay, let's… let me look inside the project, let me see how it works and everything, how it's different than what we have in the dog, and what we can support with, and so on, so… This thing, in particular, it's a problem whenever, you know, like, you're providing some network information.
For example, the network type, if I'm not mistaken, which you cannot read without the permissions in the latest Android versions. So, because of that, because it's a lazy… way of, of getting this information. Once you get it, you always provide it in the traces, spans, and in the spans information.
If the prevention is not set from the moment the application, the process was started.
that information will always not be there, like, will always be missing. So, the reason that happened is that the permissions were not there. So, what I have in there is not a very easy-to-solve problem, because it requires a lot of things around.
You need to be very careful, you need to apply some race conditions. If you had a blocker, you might block the main thread, so I wanted to avoid that, so I have some questions for you there into the PR to actually debate on, because there are some tricky parts that I would rather not add lockers on, just because there is why it might be a very slight chance for race condition, which I think is less… problematic than having to block the main thread. But yeah, just have a look, let me know if you… if you… if you… if you think we should go ahead with this.
**Jason Plumb** 13:30 Okay, great. Yeah, we can certainly chime in on this. It's kind of a lot to absorb.
Also, I'm still on my first cup of coffee, so… you know, this is a lot, but cool. No, thank you, thank you so much for contributing this. Did you… did this come up because you have a concrete example of something that's not working, or it's working, like, later?
**Marius Constantin** 13:52 This was an open issue on your, on your repository.
**Jason Plumb** 13:55 It was, okay, so this one, yeah.
**Marius Constantin** 13:59 Well, there were not too many commenters on this issue, but I thought this is an information that if we can provide it, we should be able to provide it, because.
**Jason Plumb** 14:08 Yeah.
**Marius Constantin** 14:08 so many times.
But not sure how important it is, to be honest. Like, if you have more complaints about this, we can actually figure out and merge this. If you don't have more, I mean, enough complaints, maybe you should let it go.
Aww.
It's a debate that I'm not able to… They… I mean, to answer right now?
It's just one guy that opened this… this issue, I think.
**Jason Plumb** 14:36 Yeah, this is one of my colleagues. So yeah, they must have seen that when… yeah, early in the lifecycle… so we have this thing called the Network Attributes Span Appender, is that right?
**Marius Constantin** 14:49 Yeah, yeah, that's the one. It's a… you have, like, a mapper or something that you provide from this module, which appends the network information to the SPAN. It's actually what we have also in Databog in our decorators for the spans, so… this one, if the permissions are not there when the moment is created, is going to keep that network information forever, for the long… for the whole process lifetime. So if it's taken once and it's not there, it's always going to not be there, no matter what is going to happen after.
**Jason Plumb** 15:22 Oh, help me understand that, because the… I think that the intent of the design is to have an abstraction around a way to get the current network, right?
**Marius Constantin** 15:32 Yeah, basically what's happening is, like, if you go into the network provider, you can see that there is a… I think, if I'm not mistaken, I did this a while ago, like, one week, two weeks ago.
It should be a setter or something like that, so once you figure out that information, you will keep it there, and it's going to always be provided from that.
I think it's an atomic… Reference or something like that, or maybe not, but it's… for sure, it's something that is… Once fetched, and then always provided from that value.
So, it's…
**Jason Plumb** 16:07 Yeah, no, that seems wrong. So there should be listeners that attach to update that state when.
**Marius Constantin** 16:12 Yeah, this is what I did in this PR. Basically, you have a listener that lists… oh, you don't have listeners on the permissions, that's the thing, you cannot have listeners whenever the permission was set, so you need to have a checker. So I have a checker that always goes and checks With a rate limiter on the time, because you don't have to check all the time, because it's very expensive to actually check the system permissions.
So, you'll see in the PR, a looper to check, because you don't know when the user is going to give you the permission, right? So, for that checks and everything, but in the same time, you might have network changes listeners. So you see, this is where the race comes in, because the network change can actually update that information at the same time as you require it from the system.
**Jason Plumb** 17:00 But I thought you… I think you also just said, that these network change listeners, if they're registered before the permission is given, then they're never activated?
**Marius Constantin** 17:09 Yeah, there's a… no, they are activated, but they're not going to give you that information.
**Jason Plumb** 17:14 Until the permission is granted.
**Marius Constantin** 17:16 Yup.
**Jason Plumb** 17:17 Right. So after the… so after the permission's granted, then they will be invoked, and then the network attribute span appender, when it calls current network provider, current network, will get the updated view. It's just like it's delayed.
**Marius Constantin** 17:33 Not quite. Let me tell you exactly what's happened.
**Jason Plumb** 17:35 There's some gap that I'm not quite…
**Marius Constantin** 17:38 Basically, there are two things, right? So you have the permissions to read the specific information from the system regarding the network, that you have to provide it yourself by opening a dialogue to the user, saying, okay, I need you to grant me this permission from the app.
In order to read that piece of information. On the same time, in your… in your provider, network information provider, you have a listener that listens for the connection change whenever you switch from Wi-Fi to… a mobile LTE or something like that, so every time this happens, the network information is already… it's fetched again and updated in that provider, right? So you have two things, right? But… Without the granting permission, Whenever the network changes.
you're not going to get that information. Whenever the granted permission is set from the user, the network information is not going to pick this up, because you don't have the listener being called back, right? So you have a… you need to have, like, some sort of a looper that goes and checks for the permission During the process lifetime, while also coordinating with this thing, which can happen at the same time.
**Jason Plumb** 18:49 And I think you suggested that it gets stuck, or that it holds onto the same state for the rest of the hour?
**Marius Constantin** 18:54 It holds to the same step, unless you have a networking change in the meantime, right? So if the permission was set, and then in the meantime you have a network change, then it's going to pick up the new state, right? But if this doesn't happen, you're going to set to be… Defaulted on the previous state.
**Jason Plumb** 19:13 Okay.
**Marius Constantin** 19:15 Which is wrong, right?
**Ben Joseph** 19:16 Sorry.
**Jason Plumb** 19:17 And that's…
**Ben Joseph** 19:17 And…
**Jason Plumb** 19:18 Go ahead.
**Ben Joseph** 19:19 Sorry, I had a question, I forgot how this works. Like, so what happens if you don't have the permission and you register for the network listener? Does it provide an error, or it just doesn't give you callbacks?
**Marius Constantin** 19:33 If you don't register for the network listener.
**Ben Joseph** 19:36 No, no, if you register, but, like, the app doesn't have the permission yet.
**Marius Constantin** 19:40 Yeah, so what happens… so, basically, there are different scenarios. So, right now, you register early.
Right? This is what happens when you register early.
But the app doesn't have permissions yet, because it takes time, you don't control the app, so you don't know when the user is going to… I mean, when the app is going to ask the user for the permission.
So, in that moment, you're going to have a race condition in a way.
is, like, the network listener is coming back to you, saying, okay, that's the new network, but you cannot read that network state, because you don't have the permission yet. So you're reading it, but with a false information, like, not false, but… not entirely… Complete information, and you will not be able to recover, because when the permission is set by the user.
You don't have a callback to tell you, okay, download permission is set, let me get it back.
**Cesar Munoz** 20:34 I think I have a… I think I have some context also there.
**Jason Plumb** 20:38 Yeah.
**Cesar Munoz** 20:38 And by the way, welcome, Marius. I hope I pronounced it correctly.
**Marius Constantin** 20:44 It's fine, it's fine, it's smart.
**Cesar Munoz** 20:46 Thank you.
So my… if I remember correctly, the… the permission was… Only needed to get a specific part of the network.
**Marius Constantin** 20:56 Yeah, yeah, only.
**Cesar Munoz** 20:57 So, so…
**Marius Constantin** 20:57 Not old enough.
**Cesar Munoz** 20:58 Yeah, so if the permission is not there, you still get the network, the current network, when it changed to cellular data. It's just that without the permission, I think you cannot get, like, the carrier name.
**Marius Constantin** 21:12 Yeah, it's exactly that, it's exactly that. You have the good information, yeah. So…
**Cesar Munoz** 21:17 So that would be…
**Jason Plumb** 21:18 So we kind of cover that here, right? It's like, you need to give your app this permission. But I hear what you're saying, is like, that permission is not always granted immediately. There could be some delay, or there could be some activity that then prompts the user.
**Marius Constantin** 21:32 Yeah, it's a race question in a way, right? Yeah.
burst.
But the permission is controlled by the application developer, so whenever it's requested to the user. So you might request it late, or early, doesn't matter. But if it's early, it's fine. It's fine. It's going to cover it. But if it's late, you're going to lose that, and it's not going to be Only by accident, if the user is changing the network, or something changes in the network, you can get the listener back, is going to resolve by itself.
**Jason Plumb** 22:02 Yeah, thank you for taking the time to explain that. I think, it does sound like a thing that we ought to try and address. I'll have to read the PR to see what the complexity looks like and what the trade-offs are, but.
**Marius Constantin** 22:14 Like I said, he's not simple, right? So, think about it, you have different lay listeners, conditions you have to take care of, be careful with the system also, so yeah, read the PR, please, and tell me what you think. Because I have a specific question in the PR.
for you guys, where I'm not sure either if I should go with a locker, what with what I propose, like, Like, some sort of, Way to treat the race conditions, but without a locker.
**Cesar Munoz** 22:42 Yeah, thanks for taking a look.
I, I do, in my, in my opinion.
I… I think it's… it's nice to address it, It's just that… If it's too complex, I haven't taken a look at the PR, but if it's too complex, like, let's say that, you know, create a new thread pool that, you know, is looping for the whole process, just to know what the carrier of the cellular connection is.
It could be a bit overkill, unless we create some sort of system that That could… that could be centralized and probably help with other future use cases where we need permissions or the like.
But, so… we'll see. I guess another option could be to have an API that users can call when they enable some permissions, so that They can just let us know.
But yeah, I guess it depends on the complexity. I need to have a look. I haven't, because… I usually don't take a look at drafts, just wanted to mention it, so… because I feel like people are still not ready for reviews then, but if you think it is, I can have a look as well.
**Marius Constantin** 24:04 Yeah, this is ready for review, so I cleaned it up, I tested it myself, I did a lot of testing on my end, because I didn't want to throw this in… Just like that.
But yeah, I totally agree with you. Depends on how you find it, as complexity. I don't find it too complex, to be honest. It's not that complex, to fix, but it's like… complexity versus value it brings, and I totally agree with you. But be careful with providing APIs, because if you provide APIs, you're going to end up in the same state. You don't know when that API is going to call. So as long as you don't control the under system.
You're always going to have users that are going to miss this information, because you don't… they don't really know whenever this is… would be called.
**Cesar Munoz** 24:48 Yeah, yeah, makes sense.
**Jason Plumb** 24:51 Well, if you didn't see me, I just made this ready for review, because you said it was ready for review, so…
**Marius Constantin** 24:56 Gaia, it's ready for you.
**Jason Plumb** 24:58 Cool. Yeah, in general, I think people tend to not review draft PRs, because they're often in flux, or people are just trying stuff, so… Yeah, just… just for future, it sends a signal to people that, you know, is ready for a look.
**Marius Constantin** 25:12 To be honest, I got warnings that I should not open PRs ready for review directly, so I wanted to make sure I don't disturb your way of working and your workflow, so that's the reason why I did the drafts. I didn't know even if we should be able to open drafts, so I just checked.
**Jason Plumb** 25:27 Thank you for being thoughtful about that. Do you know where you saw that warning?
**Marius Constantin** 25:31 Well, I've been warned by my… Members in the browser hotel team.
**Jason Plumb** 25:37 Okay.
**Marius Constantin** 25:37 I guess there was some guy from Datadog that opened a PR in Android and was… Actually, he was questioned about it, and I think that was the… That was the… the route.
where this came from, like… Okay. I'm not sure.
**Jason Plumb** 25:55 Well, you can help… you can help spread that knowledge that PRs are welcome. Okay. You can open… you can just open regularly.
**Marius Constantin** 26:01 I found it a bit weird, to be honest, like a rule. Yeah. Because I guess, you guys, you expect people to contribute, right? So, you should not…
**Jason Plumb** 26:08 I think we're pretty… I think we're pretty welcoming. I don't think we're… yeah, I don't think we shut people down too quickly. I mean, we're… sometimes we… sometimes we're sensitive about certain things, but I think… Pull requests are welcome.
**Marius Constantin** 26:19 Great.
**Jason Plumb** 26:22 Cool.
That's a good discussion. It looks like we've kind of run out of topics right now. How are we doing on a release schedule? Are we behind again? Probably?
Alright, so September 4th, yeah, we're a little behind, because we say we're gonna release monthly.
And this… do we… yeah, so this was… 231 of Upstream and 165, so where are those at?
So 232 is out, so we're behind a version on… Instrumentation, and then 165… So we're two versions behind a core. So I think we should do a release, and I want to do one before instrumentation goes to 3.0, which is gonna happen next week.
So… you know, we depend on… we still depend on a few packages from instrumentation. I don't know that we're getting a lot of value out of them, to be honest, but we still have that as a dependency for a couple of the HTTP instrumentation modules.
So I will do a release today, how about that? Or at least I'll get it started, and… Whoa.
Yeah, I'll try and get it done today.
**Cesar Munoz** 27:40 Sounds good. Thank you. I just wanted to…
**Jason Plumb** 27:43 Is there anything that we think we want to get into that release that is still pending?
Like, does anybody on this call have a pet PR that they want to see merged?
**Cesar Munoz** 27:55 I don't have a PR that I want to see merge, but I do want to raise that… It's probably not an issue here.
But… on the latest version of OTL Java.
I think they added some reflection regarding resources.
I think it's to get entities.
And…
**Jason Plumb** 28:20 Yes.
**Cesar Munoz** 28:21 in the… in the… in the case of Elastics.
We saw that this reflection caused Well, when it's unified, the application.
cost a no, no API, no found something class method.
**Jason Plumb** 28:38 I believe it, yeah.
**Cesar Munoz** 28:40 And yeah, I just wanted to… maybe… I don't know, I don't remember what… what do the, Oteelandry Protard rules look like today, but… Just wanted to mention it in case, you know, wanted to double check that this is not a problem.
Here.
But I haven't, I haven't… Check.
**Jason Plumb** 29:01 It might be this one. I think I reviewed this as well, if it's the one I'm thinking of, yeah. Yeah, I reviewed this one.
And there is a bunch of reflection in here, and the intent of that… I think the reason why there's a bunch of reflection is it allows them to do this extended thing where it's like.
It's… it's Java… It's the wrong thing.
That's the wrong thing. It's a way for Java to, like, add extension… Points… While being backwards compatible, without these being, like, first-class methods.
**Cesar Munoz** 29:40 Yeah, yeah, yeah, MX… and it's… it's something they've done before, also, with that.
**Jason Plumb** 29:44 Totally.
**Cesar Munoz** 29:45 Despite that.
**Jason Plumb** 29:46 I…
**Cesar Munoz** 29:46 It's fine.
**Jason Plumb** 29:47 It's so complicated, and there's, like, a bunch of steps that they're going through to, like, maintain the stability, but I get it.
And yeah, that's certainly gonna.
**Cesar Munoz** 29:56 I'm warned that… Probably. Probably would… I don't know, it depends on how the rules that we have here look like right now. So, if you can take a look at a local run with… with… minification enabled.
just to make sure that it reaches the endpoint, I think that will be… How do… that will be it.
**Jason Plumb** 30:19 Yeah, do we have a configuration for the demo app, or any of these… we don't have any, like, test automation around minifying, do we? I thought we did at one point.
**Cesar Munoz** 30:29 I don't remember. Need to check.
**Jason Plumb** 30:32 Yeah.
**Cesar Munoz** 30:32 We had a smoke… Smoke test, maybe, with minification? I don't remember right now.
**Jason Plumb** 30:39 Minified app smoke test. That sounds plausible.
**Cesar Munoz** 30:45 Yeah.
**Jason Plumb** 30:48 So, if that passes with the new version of Java, like, I bet you we're on the new version of Java already.
She said it was 6.7? Oh, God. 1.67.0 or something.
it's… I think… it's hard to see, because I think we get… Java Core through this package.
I think we get this package.
And then this bomb… wait, where's the bomb?
Yeah, so I think we get… OpenTelemetry Core Bomb… oh, no, so it's through this one.
But the version is resolved through the Alpha bomb.
the instrumentation Bomb Alpha.
or the instrumentation bomb. One of these provides the dependency on core, that's how we get that resolved.
But if we haven't made the jump yet to the latest version of… So we are in the latest version. I bet you that we're using the latest Java.
Which is 6-7, but let's make sure.
I think this should, in the release notes, say what version of core it's using. Okay, so no, it's at 6.6.
Interesting.
So this release… Right now, the tip is pointed at… I've got too many tabs open. The tip is pointed at 232.
Which depends on core 166, so it would not have this change in it yet.
**Cesar Munoz** 32:41 Yeah.
**Jason Plumb** 32:42 I think it's safe, but you're good to bring it up, because the next version might be broken.
In which case, hopefully that minified test catches it, right?
**Cesar Munoz** 32:51 Yeah, yeah, let's see.
And if it's not, if it does not, then we know that we have to fix it.
At least add that use case into the smoke test.
Yeah.
**Jason Plumb** 33:02 Yeah.
**Cesar Munoz** 33:02 Yeah.
**Jason Plumb** 33:03 Cool.
Good to be thinking about.
**Cesar Munoz** 33:14 Yeah, I don't think…
**Jason Plumb** 33:15 I don't think anything in Android is using entities yet, right? We want to eventually, but we're not yet.
**Cesar Munoz** 33:21 Not that I'm aware of, no.
Also, just… Renovate, take care of these bombs.
**Jason Plumb** 33:30 Yes.
**Cesar Munoz** 33:30 because… I mean, it's been a while, and… Unless he has a PR open, I missed it.
**Jason Plumb** 33:39 Amen.
**Cesar Munoz** 33:41 Since the latest, upstream release.
So I'm kind of, like… I'm kind of wondering why I still… Using the… the previous one.
**Jason Plumb** 33:52 So, 232 is the latest instrumentation.
**Cesar Munoz** 33:56 Oh, I see. We'll get it from…
**Jason Plumb** 33:57 And 232 depended on 6-6, because 6-7… Was only released recently. Two weeks ago.
**Cesar Munoz** 34:07 I see, we get it from the instrumentation releases.
**Jason Plumb** 34:11 We do.
**Cesar Munoz** 34:11 the cable. Got it.
**Jason Plumb** 34:13 Yeah, because we want to keep those aligned, and so the instrumentation is the higher level BOM that we depend on.
That locks all the other versions.
**Cesar Munoz** 34:21 Fair enough.
**Jason Plumb** 34:25 And I don't… think there's anything breaking in 3-0 for us, but I guess we'll find out.
Okay, so…
**Cesar Munoz** 34:38 Just out of curiosity?
**Jason Plumb** 34:39 Yeah.
Can we what?
**Cesar Munoz** 34:41 You know, when is it due, you know?
**Jason Plumb** 34:43 next week.
**Cesar Munoz** 34:44 Next, the, the, 3 to O.
**Jason Plumb** 34:46 Yeah.
**Cesar Munoz** 34:47 Oh, it's fast.
**Jason Plumb** 34:49 Yeah.
**Cesar Munoz** 34:50 Well, nice.
**Jason Plumb** 34:51 I mean, they were gonna release it early… early summer was the initial date, like, June or July or something, so it's been pushed.
**Cesar Munoz** 34:57 stock.
Got it.
**Jason Plumb** 35:02 Are there any PRs that we need in this release?
It sounds like no.
Okay, I will start that today.
And hopefully… so, Jason, where are your friends today?
They're not here.
**Jason Morris** 35:30 Yeah, Jamie's… Jamie's not available, and Hansen's dropping and picking up kids.
**Jason Plumb** 35:37 Okay, so I can probably leverage Hansen to approve the PRs for the release. That's what I'm getting at. I'm like… I need approvers on the West Coast. Ben, are you West Coast?
**Ben Joseph** 35:48 No, but I'll be around late.
**Jason Plumb** 35:52 Okay.
**Ben Joseph** 35:53 Okay.
**Jason Plumb** 35:56 Yeah, my main thing is, like, I know that, it's the end of the… it will be the end of the day for both Cesar and Jamie before I get to this, so… having some… having some comrades, at least in the US, is helpful.
**Ben Joseph** 36:12 Yeah, you can ping me, I should be around.
**Jason Plumb** 36:15 Okay, cool.
Yeah, awesome.
Okay, does anyone have anything else they want to look at, talk about, address?
**Marius Constantin** 36:26 Well, I don't know if it's, if… I mean, maybe you'll find it unusual, but wanted to ask you, I don't know how these things work, so I'm just discovering, so sorry if you're interrupted.
**Jason Plumb** 36:36 fine.
**Marius Constantin** 36:37 Yeah. Just, like, one idea that we kind of have requests from our customers is, like.
And I want to ask you, I don't want to propose anything, I want to ask you just, like, what do you think about this, and what do you think about this feature?
I didn't see yet, and we have this request from our customer.
For, let's call it application launch performance metrics.
like… Time to initial display, time to… first row, or stuff like this. Have you thought about this already for bringing it into… because right now, we kind of give our customers at the use hotel, we have to… we had to actually instruct them to use some sort of a custom instrumentation on their end to actually provide these metrics, because they want it, but I was thinking, like, I don't know how many customers do you also have on your teams or orgs that are requesting for this, this feature, and if you ever discuss about this, and you think about a solution about this.
**Cesar Munoz** 37:42 I do remember that… a while ago.
somebody was actually… was creating PRs on this.
Yeah.
And… So I remember I had a lot of com- questions there.
Because these PRs were created in tandem with some semantic conventions PR, because I remember that they wanted to create, like, a… Global, universal, if you will.
semantic convention that will work across all platforms, not only Android.
**Marius Constantin** 38:23 Yep.
**Cesar Munoz** 38:24 And that was the tricky part, I think, to… to come up with a… You know, universal consensus.
So, at some point, if I remember correctly, they just stopped, you know, answering the questions, so… it's kind of there. It's stopped.
I guess… In my… in my experience, what has been difficult so far has been… if you want to define something that works the same across platforms.
Is to define a good abstraction That actually covers what's important per platform.
And… but then the other question is, what is actually possible to capture per platform?
Based on the environment.
And… and it's… it's usually that tricky… I guess… If you already have a use case, it would be very helpful to know Like, exactly what they need, because sometimes… I guess we can track… the first, you know, the time to display the first, I don't know, frame on screen.
But also, there could be, like, another approach where… They want to track the time that, I don't know, the application object it takes to create?
Or things like that, or maybe they want both, or maybe they wanted… another thing that we didn't know back then was How do users… want to see it? Is it like a… like a… like a span?
Or they just want to have some sort of metrics or events which show the… the end time?
Yeah, it's just a difficult thing to… know what to do, because as far as I remember, there was not a specific use case, and we also wanted to create this universal stuff that was difficult.
**Marius Constantin** 40:40 To be honest, yeah, I totally agree with you, and… honestly, what I would define as a standard right now, if I have to discuss cross-platform, like Android, and let's call it mobile platforms, in a way, I would define only the format, or how you do send this.
what's the format of the events, right? Because you guys are using events, like logs, more particularly, so… or metrics. How do you… so, define the JSON schemas for that? But I would not be able to tell you If you can actually standardize this across platform, because a TTID in Android can mean different things than a TTID in iOS.
So, the way we do it in Datadog is, like.
we've created different things, right? So, a TTID, it's an equivalent in iOS for something that is totally different in Android sometimes. And the TTID for Android, for example, is the moment from… the moment the Delvik process started, and it can be cold or hot, until the first view appear, but own create of the view, so the view was created, not resume, and we called it TTFD, like, the same time until the onResume was called, or own view created was called, or something like that. So you see, it's like… but it's… I mean, you cannot be 100% correct on this, right? So, we are kind of a… anticipating some things in there, like, it can change from platform to platform. But what I would see as a solution in Autel, for example, I would see, like, an instrumentation module like you already have for other things, which is for Android. This is the way you do it for Android, this is the way you do it for iOS.
and you plug it in as an instrumentation, extension, like you have it in your SDK builder.
just for people to say, okay, if I want application performance metrics, I'm going to get this module and plug it in. And this is the way I send it. This is the way I would see it in a hotel world.
Scalable.
**Jason Plumb** 42:41 Yeah, so…
**Marius Constantin** 42:41 It's just a discussion, so I'm not proposing anything, I'm not trying to push anything.
**Jason Plumb** 42:45 Yeah, totally, I mean, it's a great discussion. There's definitely been interest in this in the past, as you can see from the PRs. You know, there's someone that took an attempt at it, and is also related to and based on a pretty long discussion that happened in the semantic conventions around this stuff, right? So this is someone who had proposed adding time to first draw span for the app screen. Also, you know, something we don't have strong semantic conventions around yet in OTEL across any of the platforms, like, what is an app screen? And so there was a lot of discussion. This ended up stalling out. I tried to reopen it back in January, and it stalled out again. So I was like, no, please don't close this!
But it didn't continue. So it… what I was… what I was hopefully, suggesting here is that maybe… so we have this dedicated client semantic conventions group that just… Started up, like, a month ago.
And so maybe that's a good… maybe this is a good opportunity to revisit that, like, in addition to some of the other things, like sessions. Like, maybe… maybe we can… maybe we don't reopen this, but at least we reopen the idea of… hey, can we start to get some semantic inventions around time to first draw, time to first screen, time to first whatever? And there's gonna be a lot of bike shedding. I don't think that it necessarily blocks or stops us from having a straw man implementation in Android. We can do that.
We just have to mark it experimental and make sure that people understand that the semantic conventions are subject to change.
So if we want to do those two things, often having a strawman implementation will help to support semantic conventions getting codified.
So you're supposed…
**Marius Constantin** 44:25 with experimental.
Instrumentation, and say, like, let's see how it goes, let's see the reaction of the users, let's see the comments on that.
**Jason Plumb** 44:32 Exactly.
**Marius Constantin** 44:33 I would love that, I would love that to have. It's like, if you want, we can invest some time in here. We can provide the module for you guys as an experimental module for you to actually… To just have a look on it, and tell us what you think, and then we… we just… we just experimented with users.
Because right now, it's hard for us to tell, like, everyone, like, okay, do your own thing, because we have a lot of requests on that.
Because we have customers that are using Hotel, but they would love to have this, because they see it in the Datadog SDK, but it doesn't exist in Hotel, so we tell them, like, okay, build this module with this implementation, so I don't see why not having just an experimental module in there.
**Cesar Munoz** 45:12 Yeah, I think what I'm getting from… from… from Marius.
and if I understand correctly, is that we can probably start within Auto Android.
**Marius Constantin** 45:26 Yeah, yeah, yeah.
**Cesar Munoz** 45:27 And… and to provide something… because… I know, ideally, this should be something that we add to the client's income.
It's just that I fear that in a topic like this, where we don't even know what we want in Android, it's difficult to then also define what's needed that doesn't clash with everybody else, you know?
So… I do like the idea of having something in Android that is definitely not gonna be perfect.
And… but… but I… but I guess he could open the… Feedback window for us, so that users start complaining because it doesn't work the way they want, or maybe they don't complain, and then we know that we have a strong candidate for the semantic convention.
repo.
**Marius Constantin** 46:14 I would love to… scratch my… my… my… the dust from my Android Kotlin programming skills, and actually try to build this for you as an experimental module, if you all agree, because I would love to go to my customers and say, okay, this is what you have to use from now on.
Use it from hotel, this is the way you send the events, so they don't have to go through all this fast all the time. So then, if it works for them, then we can actually build it together here for the entire community after.
**Jason Plumb** 46:46 Yeah, I think getting a… I think getting a start is good. I would… the only caution I would… I would… exercise there is that if we have an experimental module when people are using it, and we end up changing the names of things, or the semantics of those slightly, then that can impact people that depend on the experimental behavior. That's why we have to be very clear about how we label it.
But I do think it helps to have that to demonstrate, like, oh, here's how we do it in Android. We measure from the time the Dalvik process is started to the time that the first screen begins painting, or ends painting, or whatever, right? If we can demonstrate that, then we have talking points to codify semantic conventions.
**Marius Constantin** 47:27 I totally agree.
**Cesar Munoz** 47:27 Yeah, yeah.
**Marius Constantin** 47:28 like this.
**Cesar Munoz** 47:28 hunt.
**Marius Constantin** 47:29 experiment.
**Cesar Munoz** 47:30 And it would be great if you have the time, Marius. For me, it would be awesome if you can…
**Marius Constantin** 47:36 Yeah, yeah, for sure.
**Cesar Munoz** 47:37 Take a look at it.
**Marius Constantin** 47:38 What's the time and date.
**Cesar Munoz** 47:39 By the way, all of the instrumentation modules by default, are not stable. So, I think… Users should, you know, should be… She'll be a… she'll know what they're getting into if they add a non-stable stuff.
**Marius Constantin** 47:56 We all know that nothing is stable in instrumentation, so… More or less, let's say, network information is stable.
**Cesar Munoz** 48:06 Yeah.
**Marius Constantin** 48:07 But yeah, there are other things that are not stable, so yeah, I totally agree. We'll market as experimental, we also inform our customers, so… but I don't see why. I don't see why not, because I think it's a very good thing to have as metrics.
**Jason Plumb** 48:23 Yeah, I mean, it's something that app developers care about, and… Yeah, I mean, we get people every few months that bring up, strict mode stuff, so people are definitely looking at and caring about startup time. Yeah. Still very much a thing.
**Marius Constantin** 48:39 I don't know why, to be honest, but…
**Jason Morris** 48:41 It's also… it's also a subject that's nuanced enough that you don't necessarily want to write the whole implementation yourself every time, especially if you've got, like, transition reactivities on launch where, you know, it's not visible to the user, stuff like that.
There's enough nuance there that you definitely don't want to sit and implement. You ideally just want an instrumentation that you can pull in.
**Marius Constantin** 49:07 Yeah, that's actually what… and the way we do it, actually, we also had to provide an API entry, a public API entry, for you to actually call to override the moment when TTFD is called.
Because we say maybe it's own view created, maybe you say it's not that, but because you have a different activity where, I don't use composables or stuff, which is hard to get.
And… you don't know, right? So you provide them an open door to say, okay, this is when the moment… when I consider that the moment is when the first view was wrong.
That's hard to catch, actually.
**Jason Plumb** 49:43 Yep.
Yeah, so having something that the community kind of is opinionated about, I think, can also help to steer those long-term across the ecosystem. Meaning, if OTEL comes up with, like, something that's, like, opinionated, that works across the three platforms, then people, I think, will start to accept that.
it just takes time to get there, you know? To get that consensus takes time, and I don't think we want to… Prevent an implementation from happening.
We just have to be careful about it being too dependent on.
Until it's stable.
**Marius Constantin** 50:18 Yeah, for sure.
**Jason Plumb** 50:18 Which'll be… who knows when that'll be.
**Marius Constantin** 50:22 Maybe never.
**Jason Plumb** 50:23 Yeah, cool discussion. I mean, it's really good. I think, yeah, I think people definitely still want that.
Okay.
I think we're out of topics for today. It was a good discussion. Again, thanks, Marius. Nice to see you, and thanks for joining.
Please review those PRs, and I'll see you in the comments.
**Cesar Munoz** 50:49 mute.
**Jason Plumb** 50:50 Bye, everyone.
**Cesar Munoz** 50:52 Okay.
