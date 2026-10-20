SIG: Kotlin SIG
Date: 2026-10-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Jamie Lynch (Palo Alto Networks)** 03:27 Morning.
**Jason Plumb** 03:30 Ayyyy… Certainly, I have a more Halloween-based background somewhere, right?
**Jamie Lynch (Palo Alto Networks)** 03:38 Yeah, it's getting close, isn't it?
**Jason Plumb** 03:41 I think I just… I don't use Zoom… like, internally, we use WebEx, and so I don't have as much Zoom coolness anymore.
It is getting close.
**Jamie Lynch (Palo Alto Networks)** 04:06 Oh, that's a good one.
**Jason Plumb** 04:08 Yeah, there we go.
**Jamie Lynch (Palo Alto Networks)** 04:11 No wonder if everyone, who joins after this will know what that is.
**Jason Plumb** 04:17 I think I have another one that has the twins in it, but… yeah.
It's a good one.
**Hanson Ho** 04:30 Hello?
**Jamie Lynch (Palo Alto Networks)** 04:38 We'll just, paste the link to this doc in the chat for anyone who doesn't have a link to it. Feel free to add items to the agenda if you have something you want to discuss.
And I'll just give it a minute, and then we'll get started.
**Hanson Ho** 05:17 Jason's either in a hallway or has a really cool background, I can't tell.
**Jason Plumb** 05:23 I'm in a hallway.
No, I found the good one. No, that's not the right one, dang it.
**Hanson Ho** 05:31 Yeah, tough.
I… Which movie is this? Some David Lynch thing?
**Jason Plumb** 05:50 The Shining.
**Hanson Ho** 05:51 Fair enough.
**Jason Plumb** 05:54 But I thought I had one with the twins at the end of the hallway, but I can't find it right now.
**Jamie Lynch (Palo Alto Networks)** 06:00 Right, cool. I'm just gonna make a start on my first topic, but feel free to add stuff as we go along. So this is kind of a follow-up from last week. I've created this ContribFest label, and I've added a few issues so far. Two of them are just docs issues.
Like, we need to kind of update our release process a little bit and define some versioning, but then… I… For goods.
I created a bunch of tickets around the entity specification, and I thought this was a reasonably self-contained task.
So… yeah, I can try and add some more issues this week, if that would be helpful.
**Jason Plumb** 06:55 Yeah, it's a great start, thank you. I think… Entity Merge might be a little ambitious for someone new to the project, if they're like, what's an entity? Like, let me tell you about a resource. They're like, what's a resource? You know, maybe it's a little involved, but maybe not.
I think it's a great start.
Cool, yeah, I mean, a few more would be helpful, probably, but that's great.
Thank you for doing that.
**Jamie Lynch (Palo Alto Networks)** 07:24 No problems.
Yeah, the other item… Oh, next item is… I just wanted to… Well, I guess coalesce doesn't seem to be… on the call yet, but I wanted to… Well, maybe we can talk about this later, and I'll just… Go to this issue first.
Yeah, so… someone opened up… This issue, suggesting that they want The ability to implement Oh, the ability to target Linux.
And there's a few PRs which kind of do go ahead.
And implement some of the foundations for that.
Like, yeah, I think it's, like, setting up a CAI target, and adding Linux-specific code.
So… I guess.
The question I wanted to bring to Versaika is, how do we feel about adding that support, and… Do we want to add any kind of more explicit?
guidelines for how to add support. Because I know we just added support for TVOS.
**Jason Plumb** 08:45 Linux seems like a natural thing that we would want. Go ahead, Hanson.
**Hanson Ho** 08:50 No, go ahead. I was thinking that, I think it's a good idea to add continued support, just because we don't know where this is… we don't know what… who might be interested in taking this on, and where this direction this goes.
The main concern would be, incrementally, how much work is it to make sure these things, keep up, and don't, you know, drag down CI, or… dev velocity. I think you should be permissive and allow folks to kind of… or rather, accept, contributions to expand this, so long as, folks that contribute, contain me to maintain, these kind of scenes, to… to actually do this, and we reserve the right to turn it off, especially if no one is using it. And to that end, I think having some sort of guide to folks to add more platforms makes sense. And hopefully in a way that doesn't require a lot of, modification of central… centralized code. It's almost like, hey, I have a new platform, I need to do these three things, and it's clear. When it's done, things automatically kind of work.
That's the ideal, lots of hand waving, but That'd be nice if we could get to that point.
**Jamie Lynch (Palo Alto Networks)** 10:15 Cool. Yeah, that aligns pretty much with… what I would like, I feel like this is a good one to accept, as I can imagine people wanting to… run on Linux, I guess the only deal-breaker for me would be, like, if it takes… if it adds on loads of time to CI, or… Give us some sort of complication.
Introduced to the project because of having to adopt this.
**Hanson Ho** 10:49 Like, it may not be feasible for someone to run all the platforms locally.
there may be a point where, you know, the support is so vast, and the amount of hardware and kind of, like, emulation or whatever it is, is just, you know, too broad. But certainly CI should be throttled, or not throttled, should be… checking everything is good to go. So, you know, if we can't verify certain esoteric platforms locally, that's cool.
But CI needs to do all of it.
**Jason Plumb** 11:22 Is there any sort of, like… existing… Post-build verification of… native or target platforms on those platforms… yet.
Like, I could see us, you know, there are Linux runners, obviously. Are there tvOS runners? Probably not. Like, on… at least not on GitHub? Like, do we try and run some of these through their paces?
**Jamie Lynch (Palo Alto Networks)** 11:47 Yeah, that's a fair point.
Zoe, go ahead.
**Viorel Alexandrescu** 11:51 Sorry… sorry, Jamie. Well, arguably anything Apple-related for a target, I think if you just have a Mac machine.
wired into the CI. Usually, Xcode brings you all the simulators you need to run on any environment virtually.
from what I know, I popped up a Kotlin multiplatform project at some point, and just targeted everything, and because I'm… I own a Mac, it didn't really bother, but… it killed my system, because it opens up Xcode, and then runs a small virtual machine for any target at that point, any simulator, so… iOS, macOS, you name it, it'll just simulate it, so it should be fine, but it's… quite… it's quite a heavy load to pick up on the CI, so… it might be good to keep them paralyzed or something, you know, just so it doesn't break the main… the main pipeline. At least that's my take on it. Sorry, sorry, Jamie.
**Jamie Lynch (Palo Alto Networks)** 12:57 Yeah, that… that is effectively what I was gonna say. There's MacOS runners on GitHub, where we could run this. Currently, we just check that it compiles, But… that's it.
**Jason Plumb** 13:12 Yeah, I mean, that seems like a good use case for, like, a nightly job, you know? It's not something we need to necessarily do… all the time, but, like, running it, like, once a day to get, like, full, like, yep, we were able to actually bring up some code that was instrumented and get spans out, like, that… even just, like, as a starting point, that seems really useful.
It seems silly to, like, to have a macOS… like, sure, macOS runner's great if you're running native… if you've compiled the native macOS code, but then just to use that to run simulators seems a little… I mean, if that's the only way to get the code running on a platform, it's kind of like a fake test anyway, but, like, we… there's… like, we do that for sure, like, with Android. There's not, like, an Android runner, so we, you know, have to run a simulator.
Emulator.
**Viorel Alexandrescu** 13:56 Arguably, I think the same applies for Linux targets on embedded. You know, you don't need an actual board to run the code, so if you can spin up a VM which, which virtualizes AMD, Oh, not AMD, ARM. Yeah. I guess it's the same thing, but it's more lightweight.
**Jason Plumb** 14:20 Fair, fair point.
**Jamie Lynch (Palo Alto Networks)** 14:22 Cool. So, I feel pretty happy to… take a look at… or start taking a look at some of these pull requests, and if other folks get the time, it'd be great to get your input too. And I'll write up some of this, probably converting into issues.
**Viorel Alexandrescu** 14:39 Have you left a message with them on the channel by any chance?
**Jamie Lynch (Palo Alto Networks)** 14:44 Nope. This just came in, I think, Eva. I saw it this morning, so…
**Viorel Alexandrescu** 14:50 Okay, okay.
**Hanson Ho** 14:54 I think if folks are serious about not just adding support, but using it, they should be adding more robust verification if they so require. It's… probably not, reasonable to ask, like, everything to be, like, end-to-end, but if you're adding support, you know, on their side, they should figure out what's good enough for them to work. Like the tvOS, whoever's adding tvOS, for instance. I assume they have an app that uses it, so, It'd be nice if we could have that ported, you know, the verification ported here, but, I would say that's a pretty high bar beyond… to go beyond, like, emulation.
**Viorel Alexandrescu** 15:35 Yeah.
just so I can get the full picture, this is all within the bounds of a Kotlin multiplatform project. So the whole point, they bring the library in their project, and they wanted to work on different targets where their app might be… Built for, right?
**Jamie Lynch (Palo Alto Networks)** 15:54 Yeah.
**Viorel Alexandrescu** 15:55 Okay.
Yeah, you're right, it's pretty much BYOB.
**Jamie Lynch (Palo Alto Networks)** 16:05 Cool.
**Jason Plumb** 16:07 I think that having a guide for people… I mean, I don't… it's probably not that often that we actually add new targets, you know, over… over time, that should probably taper off.
But this guide, I think, might be nice in the early stages, because, like.
If someone asked me to go add support for X, and X doesn't exist yet, I wouldn't… I wouldn't even, like, know what pieces might need to be touched.
**Jamie Lynch (Palo Alto Networks)** 16:30 Sure.
**Jason Plumb** 16:31 Yeah.
**Jamie Lynch (Palo Alto Networks)** 16:34 Okay, well, I'll try and write something up, and I'll have a look at those PRs.
**Jason Plumb** 16:40 It's also kind of funny that the person that submitted the Linux targets, their little summary on GitHub is, I mostly do Android development.
**Hanson Ho** 16:53 KMP, that's the power.
**Jason Plumb** 16:56 Yam.
**Jamie Lynch (Palo Alto Networks)** 16:59 Cool. So the next thing I just wanted to bring up… fairly quickly, as I've, been making progress on making the propagation API not require an OpenTelemetry instance.
So I put together this… stack of PRs on the OpenTelemetry Kotlin repo.
And… I think it… Should address most of the issues, apart from… The question of… Like, supplying an actual context object, and, how we manage that.
So, yeah, I think, Carlos, if you're able to take a look at this, I could ping you, for PR, If you don't have time, then I think Hanson's already taken a verbal look.
**Carlos Alberto Cortez (Dash0)** 17:55 Yeah, I will review that before the end of the day.
**Jamie Lynch (Palo Alto Networks)** 17:59 Awesome.
Thanks very much.
And I guess this week I'll try and find some time to… Have a think about what we're gonna do with, like, Managing the contacts.
**Hanson Ho** 18:19 What do you mean, managing beyond what we do now?
**Jamie Lynch (Palo Alto Networks)** 18:22 Well, we're currently… context is tied to an OpenTelemetry instance.
Whereas, I think, one of the things that was kind of highlighted in Collis' reviews, is that, we should… Have the ability to manage context.
Before the, actual OpenS Laboratory SDK is, like, initialized.
**Hanson Ho** 18:56 Okay, I have to… Deep in… dig into that in my head.
How do you have contacts? I guess… how do you manage it, I should say? Because the context existing makes sense, but… Yeah.
**Jamie Lynch (Palo Alto Networks)** 19:10 I think that one will probably make more sense when there's, like, a concrete proposal out there.
**Hanson Ho** 19:17 Okay.
**Jamie Lynch (Palo Alto Networks)** 19:21 Okay, farewell. File export feature.
**Viorel Alexandrescu** 19:28 Yeah, so regarding that, thanks, Jamie, for having another look over it. Right now, the pipeline should be… should be passing, guys, just change the visibility of those functions, of those API functions.
I did have a thought… I did have a thought about what you said to cater the user's process to be able to pass a sync, effectively to the API creation DSL.
To actually have them write to a file, but to be honest, it's a bit confusing how we might help them.
Because at the end of the day, the DSL just wants a sync, so they should know what that is and where it should point to. But I'm also tempted to say maybe I could add a few more things, like a type radius, you know, which they may use, when creating the DSL to return a sync, and they just pass, like, a path or something like that, I don't know. Yeah. Something to cater for it a bit, but we can leave that for later and have a thought. I don't know, whatever you think is advisable right now.
**Jamie Lynch (Palo Alto Networks)** 20:39 Yeah, so… I think I'll try and sum this up properly on my PR when I get to review it tomorrow morning.
But, yeah, I think probably having a path supplied via the DSL Would be the way to go, as that's… That would… configure a directory where you can write telemetry files into,
**Viorel Alexandrescu** 21:06 Instead of passing directly a sync instance, and just keeping that as an internal implementation detail.
**Jamie Lynch (Palo Alto Networks)** 21:15 Yeah, I think that'd be the way to go.
I can take a bit… a bit more of a look at that tomorrow.
And just for context for everyone else, this is a PR for, implementing file export for OTLP exporters.
**Jason Plumb** 21:35 Specifically in Protobuffs.
**Viorel Alexandrescu** 21:38 No for Jason.
**Jason Plumb** 21:41 For JSON, okay, perfect.
**Viorel Alexandrescu** 21:43 Yep.
**Jason Plumb** 21:51 Java doesn't even have that.
**Viorel Alexandrescu** 21:55 No way.
**Jason Plumb** 21:57 It doesn't.
**Viorel Alexandrescu** 21:59 Huh.
Okay. Now it makes it feel way more cool.
**Jason Plumb** 22:05 Yeah.
It is cool.
**Hanson Ho** 22:08 Well, Java just wants Protobuff, right?
**Jason Plumb** 22:12 Yeah, mostly.
I think there's an issue, like, it's out there, I think it's been out there for a long time.
**Hanson Ho** 22:20 Yeah, this is… this is cool, because, Trying to do stuff right now, try to inspect the payload, go out, and…
**Jason Plumb** 22:28 You have to…
**Hanson Ho** 22:28 set up a fake server to get the data, and basically parse it, and doing a little… This would be much nicer to just have a… have a parallel thing, just write to disk!
**Jason Plumb** 22:41 I think one of the other challenges is that every single Java JSON library gets popped, like, every week. So, like, there's zero days. Every single library has zero days on it, so… I think… It's been nice not to have to deal with that.
And I think… I think in some cases, they also wrote their own serializer, but I don't think it's for a JSON export, because I don't think that doesn't exist.
For something else.
**Jamie Lynch (Palo Alto Networks)** 23:13 Cool. Is there anything else that folks want to discuss while we're all together?
**Rafael Nicolau** 23:20 Well, very minor thing. Basically, a PR I submitted was approved, but it wasn't merged, so I just assumed you forgot, or something like that. Just wanted to bring that up.
**Jason Plumb** 23:33 Can you link to it? Do you know which one it is?
**Rafael Nicolau** 23:35 Yeah, just a second.
**Jason Plumb** 23:45 Is it 1269?
**Rafael Nicolau** 23:48 Yeah, exactly.
**Jamie Lynch (Palo Alto Networks)** 23:54 I can take a look at that.
Okay.
**Jason Plumb** 24:04 Cool.
**Jamie Lynch (Palo Alto Networks)** 24:04 I can wrap it over.
Thanks, everyone.
**Carlos Alberto Cortez (Dash0)** 24:09 I do.
**Jason Plumb** 24:09 Thanks.
**Viorel Alexandrescu** 24:10 Thanks, have a good one.
**Rafael Nicolau** 24:11 Thanks.
Chill.
