SIG: Go SIG
Date: 2026-01-15
Duration: 66 minutes
Zoom Recording URL: https://zoom.us/rec/share/EY0k2dd80Edxs5YVU-qlp8nN72lx6qclzlR5tmrynhMb7XK73D1yjshxV0te7NnA.i3OgS3yA0PBIsjvW
============================================================

## Zoom Recording Transcript

Bryan Boreham 00:01:00 Hello.
Owen Williams (he/she) 00:01:03 Hello.
Tyler 00:01:14 Hey.
Are y'all able to hear me by chance?
Bryan Boreham 00:01:25 Oh, yeah, sure, hi. Sorry, I just.
Tyler 00:01:27 Yeah, no, no worries.
Been having troubles with Zoom lately, so yeah, just double checking.
Bryan Boreham 00:01:35 That seems to be working.
Pellared 00:01:38 Hello?
Tyler 00:01:40 Hey, how's it going?
Pellared 00:01:42 Fire, my headset is working.
Tyler 00:01:45 Right?
I'm not the only one having troubles with, technology.
Let's see, where are we at? Minute 29. So yeah, if you haven't yet, go ahead and add your name to the attendees list.
If you have topics you wanted to talk about, please go ahead and add them. There's a fair amount of, like, goal preparation stuff we wanted to talk about this today, but hopefully we can get to them, I think, some other issues if they're not too big.
At the end of the meeting.
But yeah, we can probably wait. I know that the European cohort, besides, Robert, may not be able to make it. I think Damien doesn't show up on days like today, but maybe we can wait for David to show up.
I haven't seen Sam in a while, is he back? He's back, right?
Okay.
There's David. Cool. Well, I will start trying to share my screen.
We can jump in here.
Because I think there's gonna be a fair amount to talk about.
Cool. Okay, so we talked a little bit last time about brainstorming some 2026 goals. In the last meeting, essentially, we had what we had before, one other thing as well, so… Yeah, I wanted to go through some of the things that I've come up with, and I kind of wanted to get next steps in finalizing our goals for the year here.
So, going through what we had last year, I wanted to just kind of get, like, an understanding of, like, what we're gonna be able to accomplish this year, based on no changes in our developer capacity, being the assumption. So, to do that, I kind of just went through all of the goals that we had stated that we were gonna do.
This obviously doesn't, include non-goal accomplishments, which are considerable, so just kind of keep that in mind.
I made up numbers here, so I'm looking for feedback, because the only one I'm confident in is this 78%, and the 100% here.
Pellared 00:04:01 HTTP is not 100% for sure.
Tyler 00:04:04 Yeah, actually, that's… it is. And the reason behind that, I don't know what happened, but, like, our goal wasn't to actually stabilize it, it was to migrate it. So, I don't, like, this actually got changed at some point, I don't know what happened here, but this is… this is a SEMCOM migration, was the actual goal.
Pellared 00:04:21 Okay.
Tyler 00:04:23 oh, I don't know if I wrote this wrong, or it got changed, or whatever it was, Yes, I do think… good call. You're smart on that one. But no, I do think that we actually did accomplish what we set out to do at the beginning of the year. I remember it being the migration, and so, yeah, I would say 100% on that one.
Weaver support, I also know, is 100%. The SDK, self-observability signals, I think it's probably higher than 78, because there was a lot more minutiae that, included here, but I essentially just looked at all the sub-issues and did a, division, I think it was like 14… yeah, 14 out of 18, so that's where I came up with that number.
I also, don't know what 5% is here. This is a completely made-up number. David, I'd love some help if you think this is wrong on the runtime metric stabilization.
David Ashpole (dashpole) 00:05:11 I actually think it's close, I just… I'd like to get the opt-in parameter first, because the…
Tyler 00:05:19 No, I agree, yeah.
David Ashpole (dashpole) 00:05:20 The remaining stuff is like, hey, we've got some metrics we'd like to add as opt-in.
But we don't have a mechanism to mark them as such in the API, so…
Tyler 00:05:29 So, based on the start of 2025, and what we had set out to accomplish with this, and what we still have to accomplish, where would you say we're at in that roadmap?
David Ashpole (dashpole) 00:05:37 It… Well, in terms of stuff done, I feel like we did 80%.
Tyler 00:05:46 Okay. And in terms of work left.
David Ashpole (dashpole) 00:05:48 there's also 80% of the work left, if that makes sense. Like…
Tyler 00:05:51 Substitution then, right?
David Ashpole (dashpole) 00:05:55 the metrics that I wanted to add are there, and the feedback seems to be good on the existing metrics.
Tyler 00:06:00 And, like…
David Ashpole (dashpole) 00:06:02 The last… but the path to stabilization is, like, the hard 20% of, like.
add a new thing to the metrics API, and then define a couple extra metrics, right? And then…
Tyler 00:06:13 I… yeah, I agree. Like, I think that, like, the hard part is… I'm trying to capture that here as well. Yeah.
David Ashpole (dashpole) 00:06:19 So, 50% is fine.
Tyler 00:06:21 Okay.
David Ashpole (dashpole) 00:06:21 Yeah. Yeah.
Tyler 00:06:23 Okay.
And… I… yeah, we'll talk about size in just a second. The logs API, similarly, Robert, I put it 50%, because I think that there's, like… Obviously, we got a lot done.
But…
Pellared 00:06:35 Yeah, but stabilization, unknowns, unknowns, yep.
Tyler 00:06:38 Yeah, okay.
The… some kind of, yep, the file-based configuration, I guess I'm the one that would say this, I don't… 60%, I think, is kind of where… this is a little bit more of a guess, because it wasn't, I think, really well defined. There's still a lot of stuff I think we have… identified before we would stabilize it. I guess I don't know why this is showing merged as well, but Yeah, I still think there's a lot more. We are still waiting on the stabilization of upstream, so I put it at 60%, just cause… like, it's kind of a rolling thing, but from what it has accomplished, I think there's still more to be done here.
Out of the sizing, though, I do think that I wanted to kind of get, like, a little bit of a breakdown. I don't know how to, like, compare a small to a medium to a large.
there's probably something we could do here, but I just kind of wanted to give, like, a size of how big each one of these efforts is.
Weaver, I definitely think, was a smaller one by comparison. It was done within, like, 2-3 months. The self-observability signals one was much larger. I don't know if it's a medium or larger. I originally had medium.
comparatively to, like, the logs, API stabilization, and the file-based configuration, I figured it was kind of bigger. It's got 18 identified subtasks, it's probably got more tasks than that, because we had documentation around it, so I put it at large.
The Go runtime stabilization, I put it medium.
I don't know if this should have been a large, given the fact it has… okay, I'm getting a thumbs up. As you can tell, it's kind of arbitrary, but… Okay. Log stabilization, I definitely think is much larger, given the work in the specification, as well as, like, prototyping here, so… Correct me if you think that's different, Robert.
The Simcov migration stuff, I don't think was actually too bad. It was, 3 or 4 PRs, so I put it at a medium. They're pretty big PRs.
And then the file-based configuration, as it's still going, I definitely thought it was large, so… Happy to adjust that, but essentially what that comes down to is what we accomplished out of, like, the goals that we set out to is a small task, one and a half medium tasks, and almost two tasks, large tasks at this point.
In the goal-oriented things, so… I just wanted to, like, kind of put some numbers to it as we go into the next year, and talk about, like, what we want to accomplish.
We can obviously come back and revise this stuff, but… I'd also like to, if we do eventually talk about a blog post, maybe our accomplishments track the non-goal accomplishments here as well? That'd be interesting to look at, just because… It might also give us a metric of how good we are as an open source community to target goals, which is something I'm very interested to know the number on.
David Ashpole (dashpole) 00:09:17 How good we are at… Coming and putting them all down at the beginning of the year.
Tyler 00:09:23 Right, yeah, like, I think there's some learning to be done there. So, yeah, I definitely would be interested in some numbers.
Okay, So then, based on that, I've looked into, the stuff from last time that isn't done, and I've moved that forward like we talked about last time. So the SDK self-observability signals, we still have, you know, a fair amount left. The Go runtime metric stabilization, still, the logs, API stabilization.
the migration, slash, now we're gonna call it the stabilization of hotel HTTP is included here. File-based configuration is also included here, and then there's some more that I came up with. So, obviously, there's more. The instrumentation stabilization. So, one of the things is, like, a big push upstream in OpenTelemetry in general is default stable… stuff? I don't know. Anyways… I think that regardless of what's going on upstream, like, some of these things have been around for years at this point, with very little to no changes, So, these are de facto thought to be stable. We should probably work on trying to, like, officially and make them stable, I think is kind of the idea here. So I've identified all of these different packages that are currently not at a 1.0, but… I… you know, there's some question marks in here of whether or not they should be. You know, I think that there's always a question of, like.
do we want, you know, is something in here worth stabilizing? Obviously.
the runtime stabilization is already tracked somewhere else, so that's not appropriate, probably shouldn't be there.
But yeah, Brian, go ahead.
Bryan Boreham 00:11:01 Yeah, so I… it's maybe not the exact right time to bring it up, but you're kind of in the area. I asked around… What my colleagues might want from… This year in this area. And, SEMCON's metrics for HTTP was one thing that came back.
So Autel HTTP… implements a bunch of stuff for tracing, and as far as I can see, exactly one metric.
Which is the number of bytes.
Whereas SemCont defines, like, 10 different metrics. So, sorry, that's… that was… I just wanted to kind of throw that in at this point as a question.
Tyler 00:11:50 Yeah, it was a good question.
David Ashpole (dashpole) 00:11:51 Have all the metrics defined.
Bryan Boreham 00:11:54 You think it does today?
David Ashpole (dashpole) 00:11:56 I think it does today.
Tyler 00:11:57 I do too, but… Robert, yeah, that's… Robert, go ahead.
Pellared 00:12:06 I think we are not implementing all the metrics in the sem code, but maybe I'm wrong. I think we just migrated the semantic condition. I'm not sure if we added New things that are… Can you hear me?
Tyler 00:12:18 Yep.
Pellared 00:12:20 Yep.
Tyler 00:12:23 Okay.
I…
David Ashpole (dashpole) 00:12:26 prediction.
Tyler 00:12:28 Sorry, go ahead, David.
David Ashpole (dashpole) 00:12:29 Can you look for duration? Or…
Tyler 00:12:31 Yeah.
No…
David Ashpole (dashpole) 00:12:37 Nope.
Pellared 00:12:37 It's in the internal SMConf package, very…
Tyler 00:12:40 Oh, right, right, right, right, yeah.
David Ashpole (dashpole) 00:12:52 Request response. Yeah.
Tyler 00:12:55 So it's definitely here. Body size… Response size, I guess… There's definitely some… hmm.
I think there's a request count and a response count that we're missing, though, right?
David Ashpole (dashpole) 00:13:10 Active? Was there an active?
Tyler 00:13:12 Yeah, I think there's an active as well.
So, how do I do?
Bryan Boreham 00:13:20 Okay, well, that's one thing, I managed to not find that. So there's… I think there's a meta point, which is… It's… it's not neces… it's not easy to find these things.
So the thread, when I asked my colleagues, about half of what came back, I was able to find what they said was missing.
Tyler 00:13:42 Okay.
Bryan Boreham 00:13:42 So this is a case where I was not able to find it, so I think my general point is… It's hard to find things.
And maybe we need more pointers.
David Ashpole (dashpole) 00:13:57 that, this.
Tyler 00:13:57 proposal.
David Ashpole (dashpole) 00:13:58 Add metadata files.
Consistently across a hotel. That's, part of the… stable by default OTEP, so that something like that may come, in the near future.
Tyler 00:14:10 Well, I think, to Brian's point, though, even just, like… Even though, yeah. Yeah, documenting it at, like, the top level here in, like, a README would just… That seems really appropriate, especially for something that's, like, gonna go stable. Maybe we already do? I… no, we definitely don't. So, like, even package docs or something, something like that, I think is… Yeah, that… I agree, like, a metadata file would be great for tooling and stuff, but, like… Yeah, okay.
So that's really great feedback, Brian. Thanks for bringing that up. I think that, I would definitely… I think it's worth adding to the existing issue for the hotel, stabilization. I think that the semantic convention metrics may be able to get split off, because I don't know if you'd need them, because we could always add them at a later point.
But I do think that it may be worth including in the stabilization, because it's like, Yeah, if you're gonna say something is, like, hotel compliant, like, it should probably be hotel compliant, and have what semantic conventions defined for it, so… Yeah, I think this is something that should be added here to the OTEL HTTP stabilization, In fact, maybe just, really quick here, a little side tangent.
David Ashpole (dashpole) 00:15:56 while you're writing, I'll just, state what I was gonna, say.
Why I raised my hand, sorry.
I do… so a lot of this, I think, assumes that we'll be able to stabilize these packages without their semconf being stable.
That is what's proposed in the OTEP, but that isn't, like, actually, hotel policy yet. So, if it does go that way, where we can stabilize our APIs without providing, like, stable SEMCOM, then I think all of these, like, definitely should be in scope, and we should push for them, but… If they're not, then I guess we probably won't be able to stabilize a lot of these.
And you can throw in the GCP detector, or I'll throw that in.
Tyler 00:16:43 Gcp detector… Where did I miss that? Oh, yeah.
Wait, is it… Maybe I missed it because it's already stable?
David Ashpole (dashpole) 00:16:55 Oh yeah, that's right.
Tyler 00:16:57 Yeah, okay.
David Ashpole (dashpole) 00:16:58 Somebody just made it staple, I forgot.
Tyler 00:17:00 Yeah, okay, alright, that's… I was like… I thought I looked through this, but, yeah, what do we have?
Yeah, AWS, GCP… Jaeger… oh, okay, these are all stable, okay.
Yeah, we already have V2. Okay, no, that's a good point.
So, HTTP's definitely stable, gRPC is… Like, that's a good point, like, this is still working on being stabilized, like, what the semantic conventions for this are, right?
David Ashpole (dashpole) 00:17:29 So, but in the OTEP, The proposal is that people will be able to mark their stuff 1.0 Based on unstable semantic conventions, and that the actual indicator of the conventions will be separate, right? It's like, oh, this is a 1.0 library, it's not gonna break the APIs.
Tyler 00:17:46 But… You might get different telemetry.
David Ashpole (dashpole) 00:17:50 As a way to… sort of combat the, like, everything is beta because we only have 3 stable Spanish conventions, or whatever it is, right?
Tyler 00:18:00 Yeah, okay.
David Ashpole (dashpole) 00:18:01 So, that's a proposal.
But it's not, like… a thing yet, right? So, if that happens, then I think a lot of these are on the table. If it doesn't, then I think we're kind of… Stuck, like, where we are for some of these.
Tyler 00:18:17 I gotcha.
Let me get that proposal, man.
David Ashpole (dashpole) 00:18:26 But I think maybe the most effective thing, Tyler, would be for us to trim this list down to things that use only stable semantic conventions, and then, next week.
try and see who's interested in signing up to champion different components. I feel like that's… like, those are the two… as long as it's ready to go, we just need people to drive.
Driving. Yeah.
You know?
Tyler 00:18:58 Well, I mean, I still think that we wanna, Yeah, I think we need to prioritize as well, because there's a lot more still to talk about here. So, yeah, okay, we need to determine if…
David Ashpole (dashpole) 00:19:23 I think today, the answer is no.
Or at least that's how we've…
Tyler 00:19:27 Yeah.
So, okay, then based on that, I think… we'll… The only ones that would be above the line are the HTTP ones, right? Like, database semantic conventions?
stabilize?
David Ashpole (dashpole) 00:19:55 Yes, they did.
Tyler 00:19:56 So, like, the Mongo… is Mongo included in there?
David Ashpole (dashpole) 00:20:00 But… I don't know who the… I've never looked at this.
Tyler 00:20:07 MongoDB.
Status development, go.
David Ashpole (dashpole) 00:20:12 Okay.
Tyler 00:20:15 Yeah, good question. So, let's do this. So, OTL gRPC, definitely not. That's… I know that one is actively being worked on.
David Ashpole (dashpole) 00:20:25 Yep.
Tyler 00:20:25 So let's move that down.
MUX is, HTTP, HTTP, HTTP, X-rayconf.
David Ashpole (dashpole) 00:20:33 No clue.
Tyler 00:20:34 Yeah, yeah, almost certainly not. So these… these… these are really definitely not. These are very specific to a…
David Ashpole (dashpole) 00:20:43 Maybe. Host would be cool.
Tyler 00:20:46 What's that?
David Ashpole (dashpole) 00:20:47 I said host would be cool. I feel like those are at least close.
Tyler 00:20:51 Yeah… let's see… is that, like, system?
David Ashpole (dashpole) 00:20:56 Yeah.
Tyler 00:20:58 Maybe system and runtime, actually. So systems development… Runtime is development as well.
David Ashpole (dashpole) 00:21:05 like, where… go back to System.
Tyler 00:21:09 Sorry, yeah.
David Ashpole (dashpole) 00:21:11 And then go to System Metrics.
Because we're not doing, like… or maybe it's process metrics, but… I'm… I'm pretty sure this one is close, because I know Braden from Google has been working on this for the host metrics receiver for a while.
Tyler 00:21:28 Okay.
David Ashpole (dashpole) 00:21:29 Yeah.
Tyler 00:21:36 Yeah, okay, I'm gonna put it in the unstable for now, but yeah, I mean, obviously, like, that'd be great.
ZPages is an interesting one.
David Ashpole (dashpole) 00:21:45 We should probably just stabilize it, honestly. I don't think it's going to change.
Tyler 00:21:50 No. The collector uses it, so I don't think we're removing it.
David Ashpole (dashpole) 00:21:53 So… and I'm pretty sure I'm the code owner, so you can probably just sign me up.
As the person that will… Audit and tick the box.
Tyler 00:22:07 There's no semantic conventions around this, right?
David Ashpole (dashpole) 00:22:11 I don't think so, it's all, like… Just web pages.
Tyler 00:22:16 Yeah, and it's just… yeah, exactly.
Okay.
Okay.
So yeah, this is, this one, though, is interesting.
OTL HTTP Trace. I don't think there is ever gonna be submit to conventions for this, because this is, like, this is, like, a very Go-specific package that has, like, way more details about OTL HTTP.
David Ashpole (dashpole) 00:22:40 Is there a way that it could be integrated into OTEL HTTP? I always forget the purpose of the package.
Tyler 00:22:46 Me too.
David Ashpole (dashpole) 00:22:48 Yep.
Tyler 00:22:49 I mean, I think it only exists just because, like, hotel… like, there's a… There's an HTTP trace package in Go, and this instrument's that package.
David Ashpole (dashpole) 00:22:58 -Oh.
Okay, then it'll probably be its own thing. That's fine.
Tyler 00:23:03 Yeah, I just don't…
David Ashpole (dashpole) 00:23:05 Let's leave it on the list, then. It… we may need to make our own conventions for it, but it feels like…
Tyler 00:23:16 Well, it says DNS in it.
That's interesting.
Obi's doing DNS stuff as well.
So this might actually have… Some semantic conventions around that that could get stabilized.
I do think… yeah, okay. Well, whatever it is, I think we should probably include it down here, though.
David Ashpole (dashpole) 00:23:52 Where did.
Tyler 00:23:58 Okay.
So, okay, then we have, ZPages, Hotel Restful, Hotel Echo, Hotel Jin, and Hotel Mux, potentially. So I think this is another one where, like, if we're gonna include these, we definitely need to have conversations with, like, owners here, because, like, we definitely want to stabilize it, unless there's new owners.
We have one owner on the call. Hotel HCP, we also know that Damien is looking to try to stabilize this. I think these two are, like, ready to go as goals. These other… I think, 4 would be potential goals as well.
David Ashpole (dashpole) 00:24:25 I think I own RESTful, I… this would be… I'm open to stabilizing this, it just depends if I have time or not.
Tyler 00:24:36 It's not gonna be, like, top of my list, I'll be honest.
Yeah, yeah, we're… so yeah, we're not… I think, okay.
Agreed, yeah.
So then, I think what we can do is also, yeah.
David Ashpole (dashpole) 00:24:50 Kubernetes uses it. It's the only reason I own it.
Tyler 00:24:56 Really? Uses RESTful? Okay.
David Ashpole (dashpole) 00:25:00 the keyboard, I think.
Tyler 00:25:02 That's interesting.
It's true.
David Ashpole (dashpole) 00:25:06 The detectors, if we can move on, all depend on cloud, and I don't think cloud is stable. Auto-detect, we can probably stabilize.
Tyler 00:25:15 Yeah, this is a… yeah.
So that was kind of, so all of these auto packages were kind of experiments? Like, are we good with these experiments being useful at this point? Like, auto-detect, auto-prop, auto-export? Like, obviously, maybe not the APIs, but just, like, are we good at pursuing, stabilization?
David Ashpole (dashpole) 00:25:36 The only thought I had is that I… I almost feel like this should be bundled as part of the Hotel Konf.
package? Like, the… and hear me out before you make that face, Tyler.
Tyler 00:25:54 No, I… that's an agreement.
David Ashpole (dashpole) 00:25:55 more like.
Tyler 00:25:55 Sorry, like…
David Ashpole (dashpole) 00:25:56 Yeah, I'm just… I'm kidding.
it's like… All they do is, like, take a string and give you a… A propagator, or, like, an exporter or something?
But it's almost better to be able to just give it, like.
a JSON string and be able to configure more of it if you want to. Like, it's… it's not that far removed from exposing, like, the propagator or exporter portion of OTelConf, and I think that would be a cool way, potentially, to, like.
allow it to be used. I don't know what people think.
Pellared 00:26:36 I just thought that, if you would like to, have this, I don't know how it's called, plugins or components implemented.
David Ashpole (dashpole) 00:26:45 This auto-conf, etc, and auto prop will not handle it.
Pellared 00:26:50 Because it's just on this environmental variable level, like David already described. And we will just, you know, basically to make it for auto-config, it will be just, you know, deep nested, etc.
And I am not sure… if we want to keep this autoprop, or we should abandon them. I know that we are using it at least in as blank distribution, but we can always vendor it. It's not a problem, I think.
It doesn't… it may not make sense to, you know, just have it in auto repository and maintain this here.
David Ashpole (dashpole) 00:27:29 they're definitely…
Tyler 00:27:32 I mean, I kind of like the idea… I like it here. Like, it's not just, I think, us, and I think there's a lot of people who are, like, come to us and go, like.
Pellared 00:27:43 That's true. Why don't you support this?
environmental variables, yes, that's…
Tyler 00:27:48 Yeah, and we can go, like…
Pellared 00:27:49 the receipt.
Tyler 00:27:49 You can't, but here's how you could, yeah.
Pellared 00:27:53 Yep.
So I think they serve a different purpose. The thing that we are right now dogfooding in AutoConfig is because we do not have anything bitter in AutoConfig right now.
Tyler 00:28:02 Well, and so that's, I think, maybe my… my take on this, is it should be a sub-package of OTELConf.
David Ashpole (dashpole) 00:28:08 Yeah, I'm fine with that. I think it would be… actually, I'll revise my earlier statement. I think it would be cool if There was a single new SDK entry point in OTELConf, And all the various… Config-related environment variables were respected there.
Maybe. I don't know, we can come up with ideas, but… I feel like we should bundle this work somehow with the hotelConf work.
And have a, like, sane configuration story.
Tyler 00:28:41 Yeah, I, I think so, like… Yeah, I like the idea of bundling it.
Because it kind of shows up together. I don't like the idea of flattening it into it, just because then you can't, like, really use it independent of it. Like, I think there's a lot of, like… reuse use here. Like, if you wanted to do your own configuration thing, you can use, like, the processing pipelines that we have in all of these things. If you wanted to use environment variables, it just works. If you wanted to, like… yeah, I mean, I think, like, there's extensibility that is already built into this package, and I'd hate to lose that. But from a user's perspective, like.
you know, that's kind of an advanced user. When a third-party user comes along, and they're just like.
I want, like, the full suite of OTEL in, like, all the specification niceties of how to configure things, and, like, you're saying, like, it'd be cool if I could just import one package and go, like, give me an SDK, and if I give it environment variables, it works. If I give it a file-based configuration, it works. If I give it, you know, something else, it would work, yeah.
David Ashpole (dashpole) 00:29:37 Yeah, well, my thinking is, like, the new SDK entry point in OTelconf already is environment variable based, right? Because you give it an environment variable telling it where the file is.
Tyler 00:29:52 That's a hot take.
David Ashpole (dashpole) 00:29:54 Am I wrong?
Tyler 00:29:56 I think that kind of skips over the whole discussion of whether environment variables should supersede, or whether they should be integrated to the OTELConf, like, file base, but yeah, like… Yes, in theory, like, it does support environment variables, and I think that, like, by default, the default file-based configuration also, like, does the environment variable interpolation, in it. So, like, if you set an environment variable, it should… Revert back to what that is. With a default value.
So yeah, I mean, like, I think… I think we're saying the same thing. Like, I would really love it if just a user came along and they're like.
look, this new SDK from, like, the main repo is great, but I want, like.
give me all the bells and whistles, I want the Cadillac of this one. So I'm gonna use this SDK setup, and it's just, like, if some of my users want to provide environment variables, if they want to provide a file config, it'll just work, and it does everything the SDK wants. And yeah, okay, I get, like, a dependency tree that's longer than Moby Dick, but, like, whatever, like, I don't care.
David Ashpole (dashpole) 00:30:56 Yeah, let's open an issue. I don't know if we… I think maybe the conclusion is, like, we should not stabilize auto-detect and auto-export as is.
Tyler 00:31:05 Does that feel… .
David Ashpole (dashpole) 00:31:08 bus.
Tyler 00:31:09 So I… I… I agree. I don't think it should be stabilized as is. I don't think any of these should be stabilized as-is, is what we're saying now. I think it's more just about, like, we should start to target that, yeah.
David Ashpole (dashpole) 00:31:18 Do you think that these should be their own… module at the current location. That's more my question, like…
Tyler 00:31:25 I… yeah, I think there's an issue and discussion on that. I do think that one of the… yeah, you're right, sorry. To… it's a yes-and, is what I'm saying. Like, I think that there is a… a reason that we should prioritize trying to resolve where this lives in this next year. Like, how that looks… And then, you know, wherever it goes, I think that we should try to then keep pursuing its stabilization, if that's the case, yeah.
David Ashpole (dashpole) 00:31:49 Sure. Okay.
Tyler 00:31:50 Yeah.
David Ashpole (dashpole) 00:31:51 As for the rest of the detectors.
Tyler 00:31:54 Like, I don't, maybe just say this.
David Ashpole (dashpole) 00:32:05 The longest meeting notes we've ever had.
Tyler 00:32:07 Yeah, right.
David Ashpole (dashpole) 00:32:11 And you can remove GCP since it's stable.
Tyler 00:32:13 Sorry. Oh, right. I just felt left out.
You felt left out, but you're actually ahead of everybody. Yeah.
Cool. Then, similar, I think, for the auto-export package, we want to talk about, this moving into the AutoConf.
David Ashpole (dashpole) 00:32:30 I think I would like to see that.
Tyler 00:32:32 Yeah.
Er, not AutoConf, O'TelConf.
David Ashpole (dashpole) 00:32:39 Rumplers.
Tyler 00:32:41 And then there's one other one, Autoprop. Yeah, let's just do this.
David Ashpole (dashpole) 00:32:46 You gonna remove Jaeger Remote?
Tyler 00:32:48 What's that?
David Ashpole (dashpole) 00:32:51 Oh, sorry, reading ahead.
Tyler 00:32:52 Oh, yeah, yeah, keep… yeah. Jaeger Remote, I think, can stay. I think it should probably get stabilized. I don't think that's going away, right? .
David Ashpole (dashpole) 00:33:01 Pretty cool. I like it.
Tyler 00:33:03 Yeah. The other one, though, I don't think should stay. I think that there was actually… there might even be an issue open to remove this. I think that this consistency probability thing, like.
switched with this new W3C randomness flag, that was enabled, but, like, I think this… I don't think we should pursue stabilization on this one. We need to get confirmation from JMACD and other people around this, though.
David Ashpole (dashpole) 00:33:27 This is going on.
Tyler 00:33:27 I'm more about.
David Ashpole (dashpole) 00:33:28 There may be a case where people are using this until the new one exists, so we may just want to leave it alone, but… I recall it being pretty trivial to keep around.
We… I guess we could mark it as deprecated or something, just to warn people and then leave it that way for a while.
Tyler 00:33:47 I mean, I'm fine, like, keeping it until there's a replacement, like, I'm not, like, I just want to say, like.
Are we pursuing stabilization? No. Or not? Like, yeah.
Yeah. I thought that this is… maybe it was a removal, but I couldn't remember.
David Ashpole (dashpole) 00:34:02 Open census.
There's an Open Census propagator.
Oh.
Tyler 00:34:08 I would love it if you're the owner of that. Yeah, I think, let me see…
David Ashpole (dashpole) 00:34:17 I mean, I'm normally the owner of all things OpenCensus, but…
Tyler 00:34:21 Right.
Yes, there's definitely this.
OC gRPC Plugin…
David Ashpole (dashpole) 00:34:27 There is indeed. I see, this is specifically for GRPC, for the binary format propagator.
Tyler 00:34:34 Yeah.
David Ashpole (dashpole) 00:34:38 I've… I say we leave it around, and then… until we want to get rid of all the OpenCensus stuff.
There's been discussions now that people are talking about getting rid of.
What was it?
Jaeger Propagator or something.
No.
Pellared 00:34:58 Yes, I think Jaeger… Jaeger propagated is only deprecated, but I think you're correct, David, that there was also an issue to deprecate the OpenSys one.
David Ashpole (dashpole) 00:35:08 Once that happens, we can do it.
I think we just leave this one as is.
Tyler 00:35:14 Okay, so not a goal of 4… 26, okay.
File-based configuration.
there's a stabilization effort. This is obviously a prototype, the collector's using it. I definitely don't think it's not a goal for 2026. Just, I think a clear definition of what that goal is, I think, is gonna be, more helpful here, if that makes sense. Like, obviously, we ran into that problem earlier, where we kind of, like, had a… squishy feel around how far this is. Maybe we want to, like, shore up what this definition is going to be.
But, anyways, I don't know if there's much more to say there.
David Ashpole (dashpole) 00:35:50 Definitely in.
Tyler 00:35:52 Yeah, yeah, yeah.
Next was the enable method for metrics. This was added last time, but I, found… I mean, like, I saw this PR get merged. Is this done?
David Ashpole (dashpole) 00:36:02 Yep, so it's done.
Great job.
Tyler 00:36:05 Alright, extra small, done.
David Ashpole (dashpole) 00:36:09 should use it everywhere, I think, is… I really, would be a helpful thing.
Tyler 00:36:14 Like, in our instrumentation?
David Ashpole (dashpole) 00:36:16 Yeah, like… a little bit. There are a lot of allocations that comes along with using the API.
Tyler 00:36:25 Oh, 100%, yeah. Yeah, is this just a documentation task that's missing, or is it, like, a…
David Ashpole (dashpole) 00:36:31 hotel HTTP.
Yeah. Should check to see if something is enabled before it constructs all the attributes and the options, and… Whatever, right?
Tyler 00:36:39 Yeah.
So maybe the 2026, goal is, documents, and… Use this. Okay.
So this, again, maybe this is just… I don't know.
I don't think it's a ContribFest and EU, KubeCon, unfortunately, but this would be a great task for… do users, unfortunately. But, okay.
the… that sounds good. Let's do that, I think that's a great goal.
Yes, to the… He was.
David Ashpole (dashpole) 00:37:11 No to the bridge.
Tyler 00:37:14 Sorry, go ahead. What was that?
David Ashpole (dashpole) 00:37:15 Yes to the Prometheus exporter, no to the bridge.
Tyler 00:37:19 Okay.
Is this something you're saying you would like to commit to? Yeah.
David Ashpole (dashpole) 00:37:25 Yep.
I feel like I'm the only one signing up, but that's okay. I think these are important things.
Tyler 00:37:32 Yeah, I haven't asked specifically for people to sign up, that was kind of my next phase, but you're doing a great job, just keep going.
David Ashpole (dashpole) 00:37:39 I'm happy to have others help with any of these, but this should happen this year.
Tyler 00:37:44 Okay.
David Ashpole (dashpole) 00:37:45 Maybe make the bridge its own thing?
It's not part of the export or anything there.
Tyler 00:37:52 Yeah, okay, that's a good point.
So is this… what's the plan with this bridge? Like, do… we want to keep it, it's just we want to wait on… actually, it may stabilize.
David Ashpole (dashpole) 00:38:02 But it's just not a priority for me.
That's… like, I'm open to stabilizing it, but it also has a dependency on the same…
Tyler 00:38:12 Yeah, that's fine. I just wanted to make sure it's not sitting in limbo. Yeah, okay.
So other ones, these are all just more small tasks. So to support the new W3C random flag, I think this is related to this open sensor… No, sorry, the probability consistency, yeah.
David Ashpole (dashpole) 00:38:29 Yeah. Is that a stable thing now?
Tyler 00:38:32 Yes. In the spec, at least.
David Ashpole (dashpole) 00:38:34 Amazing, okay.
Tyler 00:38:36 Related to the…
David Ashpole (dashpole) 00:38:39 I would love to see that happen.
We should definitely find an owner for it. Shouldn't be too crazy hard, right?
Tyler 00:38:45 No, it's a single issue, like, I think this is a pretty small task, honestly.
Maybe more than one PR, but, yeah.
David Ashpole (dashpole) 00:38:53 Very excited.
Tyler 00:38:54 Yeah.
David Ashpole (dashpole) 00:38:55 And can you click on the link?
Tyler 00:38:57 Yeah.
David Ashpole (dashpole) 00:38:58 I just wanted to make sure it was stable and not, like… Added to the… Spec is experimental or something.
Tyler 00:39:07 I, like, I thought I saw this merge, yeah.
David Ashpole (dashpole) 00:39:12 Yep, cool.
Tyler 00:39:13 I'm sure, yeah.
David Ashpole (dashpole) 00:39:14 I'm happy.
Tyler 00:39:17 Sampling… well, I guess this is development.
David Ashpole (dashpole) 00:39:25 Okay. We might have to… make sure that that goes stable first. I mean, someone can prototype it.
Tyler 00:39:31 Well, yeah, at least add an experiment, I think, to maybe just.
David Ashpole (dashpole) 00:39:34 Yeah, let's add it as an experiment.
Tyler 00:39:38 Well, where am I?
Oh, okay.
David Ashpole (dashpole) 00:39:44 True, true, true. This is probably easy to put behind an environment variable.
Tyler 00:39:47 Right.
Okay, I also put down Optimize the metrics SDK, because you're doing a lot of work here that is not captured in our goals, but it definitely should be. So, I mean, obviously I don't have a breakdown of this. You have more to do around, like, I say you.
We have more to do around the, you know, histogram, dynamic, or, exponential histograms and other, other optimizations, so… I think this should just be included. We need a breakdown of, like, what these tasks are, yeah.
David Ashpole (dashpole) 00:40:29 Okay, I should probably just open issues, instead of just, pRs.
I mean, the only thing left is exponential histograms and any changes we make to the how attributes are passed. Those are the two things remaining.
I guess there's a fixed size reservoir.
And the, time-weighted histogram reservoir change.
Which isn't really an optimization. It is a little bit.
Reservoir.
Tyler 00:40:58 Yeah.
And then… fixed size.
David Ashpole (dashpole) 00:41:09 And then a blog post.
Tyler 00:41:12 Yep.
I definitely want a blog post with you, your picture right up front.
Okay, cool. And then… Support environment variable propagation… Oh yeah, this is just another one that's in our milestone that I think is a pretty small, thing.
This frickin' shrib.
Sorry, go ahead.
David Ashpole (dashpole) 00:41:35 That's still experimental, right?
Tyler 00:41:38 Oh, sure, yeah, but this is just for.
Pellared 00:41:39 trip.
David Ashpole (dashpole) 00:41:39 Adding, adding… Yeah, that's fine.
Pellared 00:41:42 I question if it's needed even in country. I haven't seen anyone expect from Ariel, I think, who was asking for it.
Okay.
Tyler 00:41:58 So, low priority is what you're saying?
Pellared 00:42:00 Yeah. Okay.
Cool.
Tyler 00:42:06 Awesome. Alright, so we got through all the things that I added.
Anything else that people can think about for, maybe, goals we're trying to accomplish here?
Before we go back through and… oh man, we only have 20 minutes.
David Ashpole (dashpole) 00:42:20 I'd kind of like to get to some of my discussions, if that's okay.
Huh.
Tyler 00:42:24 Yeah, okay, then let's… let's do this. I… what I want to do, then, is I want to create a project board, and what I'm going to try to do in that project board is capture all of these.
And even the ones that we don't think are going to be included, like low-priority ones, just to track issues there, if we already have an issue or not.
I wanted something to track it.
in the priority… in the project board, and then, I think in one column we'll just have, like, a catch-all, like, these are the things below the line, and then next week we can go through and review each one of those and say, like.
this is gonna be above the line, we want to tackle this, and then we get a sponsor for each one of those things that we move across, and then we get some sort of, like, I think, maybe understanding of size, if that makes sense.
David Ashpole (dashpole) 00:43:06 I think the main thing is just, we should put them all out, all the ones that we think are candidates, and then just get, like, owners for each. So if people want to sign up.
They can sign up for the ones they want to drive.
I mean, it's fine to say, like, as a SIG, we think this is really important, but hopefully that just means, like, somebody signs up for it, you know?
Tyler 00:43:24 Yeah, so that's kind of what I envisioned. So, I just mean, like, yeah, like, I'd like that. I want owners, so yes and, like, I want owners, like, I don't… I definitely don't want… a single one of these issues to go and say, like, we're gonna accomplish this and not have a single person to say, like, I'm going to work on this. Like, that, I don't think, is realizable.
I… but I just wanted to… how… how do we do that? Right? Because, like.
putting your name in this doc is not really that helpful from a visibility perspective of the project, and so I want to make sure that, like, these things are visible external to the.
David Ashpole (dashpole) 00:43:57 Or, like… Like, put out a list on Slack.
And just ask people if they're willing to help own and drive things, and then… Once we have a list of things that have staffing, then we publish that list.
Tyler 00:44:14 Yeah.
David Ashpole (dashpole) 00:44:14 If that makes… like, you can also be a project board, that's fine. And then.
Tyler 00:44:18 Yeah, I envision doing exactly what you just said as a project board. So I'm happy to link in Slack and communicate this in multiple places. My goal is to, like, say, like, cool, like, go to the project board, find issues that you find important.
put your name down as ownership, and then what we'll do is next week… because then there's also the other things, like, I think there's a lot of things on here that are important.
maybe I'll say that I would like to, like, work on them, but I don't know if I can get all of them done in the next year, based on, like.
David Ashpole (dashpole) 00:44:44 Right, exactly.
Tyler 00:44:45 this, so…
David Ashpole (dashpole) 00:44:47 Yeah, for me, that's gonna be, like.
I'll make my personal, you know, priority list, and then I'll sign up for whatever, right? Like…
Tyler 00:44:54 Okay.
David Ashpole (dashpole) 00:44:55 Yeah.
Tyler 00:44:56 Cool, then let's… let's do that. I will take the task and put it into project boards. I like the idea of a project board because it's a little more fluid than an issue, and formatting in the issue last year was a large issue.
So, what we'll do is then, yeah.
David Ashpole (dashpole) 00:45:11 We can do a blog post after we have, Decided, like, everything that we're gonna…
Tyler 00:45:16 Oh, I agree. Yeah, I don't think we should have a blog post until the end of next week, or something like that, yeah, because I definitely want more feedback on what is above the line, because the other thing is I want some rationale around, like.
Hey, David, you've taken on, like, 10 issues, and I don't think that's… I don't think that's gonna happen. Or, you know, Tyler, we're, like, 20 issues is not gonna work. So, yeah, something like that. We can get some ideas there.
Okay.
David, you want to talk about the API and performance updates?
David Ashpole (dashpole) 00:46:08 Yes, okay. So, I've spent pretty much the entire week since last meeting doing prototypes and stuff.
I put down the ones that worked out to some extent, but actually.
My end finding is that I can't really do much better than the current… API.
You can do maybe a tiny bit better, but without introducing some way for people to pass attributes directly and not inside an option, like the go escape analysis.
just always… allocate stuff on the heap. So, like, the… that actually number 7777 doesn't have one allocation, it has two. And it adds an allocation, or adds allocations to other.
Calls in order to do it.
So neither of the two other ones that I thought were viable actually turned out to be viable.
And… I did… I was just, like, trying to figure out any way to eke out any extra performance, and the only way I could do so was by changing every use of attribute… or, like, attribute key-value slices to pointers to it.
Which seemed to get me down to only a single allocation. But all of that, I think, is… not even really worth considering. So I'm back to the point where I think, I think there's… there's two things I maybe want to talk about. One is, I'd like to go through the benchmarks I wrote, just… to get feedback on those, because I think settling on… The cases that we want to consider is actually important.
And if there's discussion, then I think that would be useful.
And the other is, I can present, like, some of the results.
That I do have for… so these… I'll be clear, actually, these results are from the… Add with Attributes function, prototype.
but a… Bound instrument would be exactly the same.
But with better pre-computed.
runtime, basically.
I don't know if that makes sense.
Tyler 00:48:22 Sorry, say that one more time, the bound attributes are better with pre-computed? What?
David Ashpole (dashpole) 00:48:27 So, so the addWithAttributes function.
Tyler 00:48:31 This is a method, right, you mean?
David Ashpole (dashpole) 00:48:33 Yeah, the addWithAttribute method function.
Tyler 00:48:37 Yeah.
David Ashpole (dashpole) 00:48:37 It is… what I've prototyped.
And… The reason why it's good is because you're providing your attributes.
As a slice, or, like, as a variadic argument.
At the same time, or prior to… Basically, with bound instruments, you can get the same performance as add with attributes.
Because in one, you just perform… like, there are two steps, right? You do a map lookup based on the attributes.
Tyler 00:49:13 Wait, what's the difference?
David Ashpole (dashpole) 00:49:15 In terms of performance?
Tyler 00:49:18 No, like, I feel like it's just a name. Add with attributes sounds like a bound…
David Ashpole (dashpole) 00:49:23 Yeah, so let me… I'll… if I can share my screen.
Tyler 00:49:27 Yeah, sorry, I'll stop sharing.
David Ashpole (dashpole) 00:49:28 I'll do that just so I can… Let me find… Just the one?
So… Bound instruments, you can see this, right? Bound instruments is where you have a withAttributes function that gives you a new counter that's bound to a certain set of instruments. So, when you use it, it looks like… MyCounter.with attributes, and then you call add, and you don't provide any attributes in the add function itself.
So this is what it looks like.
The add with attributes Function is actually just An add function that takes attributes.
Or, like, it's an add function that has attributes built in, so, Right? Like, it replaces, essentially, the add function with just a… Version that includes the attribute slice directly.
You're muted.
Tyler 00:50:32 Yeah, okay, sorry, I see, yeah.
David Ashpole (dashpole) 00:50:33 You can see how they have equivalent performance.
Tyler 00:50:35 Yeah, yeah, that makes more sense, yeah.
David Ashpole (dashpole) 00:50:38 So, all I'm doing is saying that I don't want to write another prototype till I'm, certain that it's actually useful, right?
The… the only diff… so the… these results… are all results from the addWithAttributes function.
Right. As soon.
Tyler 00:50:54 Yeah, yeah.
David Ashpole (dashpole) 00:50:54 With the exception of… In the pre-computed cases, I make an assumption that The bound attribute can have just a counter increment performance, because That's how it would work.
So you'll have to trust me. So, there are two steps in a… in incrementing a counter, right? One is doing the sync map lookup.
Based on the attribute set. And one is… Doing the atomic increment.
Tyler 00:51:25 Right.
David Ashpole (dashpole) 00:51:26 And so, in the bound pattern.
Those two are broken up into separate functions, where with attributes.
Performs the lookup in the map.
and the increment… all it does is, like, atomically add to a counter. And so this is just the performance of atomically adding to a counter.
But… And the other… time is just what's spent on the map… or on the map lookup. But… The addWithAttributes function is the same, except this is actually 70 nanoseconds, and this is 70 nanoseconds.
Tyler 00:52:02 Just because it goes into a single operation with the map public as well, is what you're saying?
David Ashpole (dashpole) 00:52:08 Bound instrument is, like, slightly more performant and, in my opinion, much more ergonomic than add with attributes.
Tyler 00:52:14 Yeah, I agree. What's this no filter and filtered?
David Ashpole (dashpole) 00:52:18 Okay, so, one of the things I discovered as I was prototyping is that Whether you pass an attribute set.
Or whether you pass a list of attributes.
Has very different performance, particularly in the filtered case.
So, one of the disadvantages of using Like, these pre-computed attribute sets.
Is that when you apply a filter, you essentially end up creating a new set.
Tyler 00:52:46 Right, yeah.
David Ashpole (dashpole) 00:52:47 When you filter it, right?
Tyler 00:52:48 Yeah. And so…
David Ashpole (dashpole) 00:52:50 any of the costs associated with making the new set, right? Like, the copies and allocations and stuff.
get, like, Way worse any time we're using like, the… With attributes set.
As opposed to if we have a way of passing in a slice.
Tyler 00:53:09 Hmm.
David Ashpole (dashpole) 00:53:09 So… all I was trying to show here is that today, right.
If you have, even in this case, right, where you have, like.
A pre-computed ad option that has a… with… attribute set.
Argument already in it.
Right? And that's passed directly to the API.
If you apply a filter to it.
it gets way worse, and it gets some allocations, right? So that's all I'm trying to demonstrate, is that when we add filters today, if you've written everything using with attribute set, which is the more performant way, you do have some, like.
Relatively poor performance. And this isn't the end of the world, right? The real… Like, in terms of which one of these matter to optimize, this is obviously the most important.
Tyler 00:53:58 Right? Right, yeah. To be able to get some reasonably good performance.
David Ashpole (dashpole) 00:54:01 And then this is the next most important… important, right?
Yeah.
And then all these are, like, kind of just informing, right? So, but I… this is something I found interesting, and I included it because It's, like, one input to how we… if we're considering changes to how we pass attributes that we might want to think of, right?
And I also… I kind of wanted to capture the default experience of, like, if people use the SDK and the API in the way, you know, like, oh, I have attributes, I want to give them to it.
In the simplest way possible.
I just wanted to understand, like, what their performance would be.
So they're not doing any pooling or anything like that, they just, like… use the simplest function, right?
Tyler 00:54:48 Yeah.
David Ashpole (dashpole) 00:54:48 So, I wanted to capture that. It's not like… a game changer, in terms of, like, how we should design our stuff, but I think it's, like, helpful for informing, like.
For the average user that just uses the package, like, what are they gonna get in terms of performance?
Before I'm gonna read our docs, right?
Tyler 00:55:07 One of the things I wanted to ask you, though, David, is, like, I do see a use case that's missing here in these benchmarks, and that's if you have, like, this, I guess it's not the ad with attributes, so maybe it's hard to kind of actually do this here, but, like, if you have the bounds, bound instrument approach, right? What happens when you have a bound instrument approach, but you also want to add an additional attribute after the fact?
So, like, if you, like… because that, I think, is the more common use case that I saw when writing the observability stuff for ourselves.
David Ashpole (dashpole) 00:55:37 That's interesting to capture. It's hard for me to benchmark, because I would have to actually go implement bound instruments, but.
Tyler 00:55:45 It should be no worse.
David Ashpole (dashpole) 00:55:48 then… All the attributes being fully dynamic, right?
in my… the way I would think about it is that you would be able to call with attributes multiple times, so you would bind it to the base set of attributes.
And then… You would call with attributes one more time with, like, arrow.type equals whatever.
Tyler 00:56:10 Yeah.
David Ashpole (dashpole) 00:56:10 And what that with… that second with attributes call would first do a map lookup.
And that would allow it to find the previous Set of attributes that it has already been bound to.
then it would append the new one to that list, and then it would do a second lookup, so…
Tyler 00:56:30 I mean, it would only do a distinct, though, right? Like… Well, I guess I'd have to create a slice on the distinct, so maybe there's a… yeah, okay, so there's definitely that, and then there's a cache hit or miss after that, yeah, okay.
David Ashpole (dashpole) 00:56:41 Yep, so there's… there's some stuff to it. It's not… it won't be worse than, this case, right? I guess it will be slightly worse, because it needs to call 2Slice.
On the attributes that are already there.
Unless we do some extra storage, right? So, we could work around it, but it should be approximately the same as the dynamic case.
Tyler 00:57:02 Yeah, because, I mean, like, that's… that's the thing I wanted to know based on, like, our existing patterns for what we could do external, with, like, our own caching. If, like, you remember we were talking about, like, if you're holding your own cache external, can you do better? And I don't…
David Ashpole (dashpole) 00:57:16 immediately.
Tyler 00:57:17 you know if you can. So I think what you're saying is I don't think you can. I think it'll be equivalent or better.
David Ashpole (dashpole) 00:57:22 It's the equivalent… no, it would be equivalent, I think, to that, caching. Well, it would be better than that caching, because the only problem with doing the caching external is that it's duplicating work that the SDK is already doing, right?
Tyler 00:57:34 In the, in the map.
David Ashpole (dashpole) 00:57:35 already maintaining that map lookup, so you do one map lookup instead of two map lookups, and if you have to compute the distinct twice, then.
that cost is also paid twice. So, yes, it would be… this is strictly better than… than that.
Tyler 00:57:51 So… I'm jumping on you here, but we're also getting to 3 minutes to the end of the meeting, and I wanted to make sure that, like, we are, respectful of people's time. So, I think what I've asked for, you've done, and, like, you've gone through all of these other things, and it seems like your findings are that, like, that's not really viable to go in these other directions, so it seems like can I, like, am I hearing you right? The recommendation is just to go with this bound instrument approach, and then maybe even work on, like, shimming in the bound instrument around, like, some of these options or something, but, like, go with the bound instrument approach?
David Ashpole (dashpole) 00:58:22 That's… certainly my recommendation. I… the only thing I was hoping to settle on in this meeting, like.
do these benchmark scenarios make sense? Do you feel like I'm testing the right thing?
But you can also…
Tyler 00:58:39 So…
David Ashpole (dashpole) 00:58:40 the PR. I know we had some disagreements about the dynamic case, where this is not A new attribute set each call.
I did implement, like, 1,000 cardinality benchmark.
But it's the same benchmark, right? Because the benchmark keeps running it until… I don't know if I'm making sense, but the cardinality doesn't actually end up mattering as long as it's bound, because you end up repeatedly incrementing… you end up incrementing a counter that already exists, right?
So this is not… this dynamic case is not where it's a.
Tyler 00:59:18 Yup.
David Ashpole (dashpole) 00:59:19 Each time, yeah.
Tyler 00:59:20 I'm not, like, I think there's an argument to be made around, like, 50 to 100 nanoseconds in, like, this map lookup. I don't think that, like, it's not impossible to have similar performance improvements external with the exact same API, But the… the… the problem is, is that it's just… it's just untenable, like… like you're saying, like, you have to maintain all these caches, you have to, like, do all these other, like, sync maps or something like that, like, so there… I think… I think that's more the point that I was… I was concerned about, because I… I'd rather… So there's that bad aspect, and then there's, like, let's have two methods to add attributes in the same way. Like, that… those are the two things I wanted to evaluate.
David Ashpole (dashpole) 01:00:04 I think your benchmarks here are great. I think the one that I was missing, you've identified and we've talked about in this meeting, so I don't think that that's… there's no concern, I think, have in that.
Tyler 01:00:12 It was more around, like, what's the user story here? Like.
like, is it better for users to not be confused by the API?
And to do performance optimizations via their own, like, caching and that kind of stuff? Or is there a way that we can make the API like, more performant the way it is. And I think your answer is we can't make the API more performant the way it currently is. You need to add something to make it better. What that… what that is, is either… this other method for the add with attributes, or I think the bound instrument, thing.
Is what I'm hearing.
David Ashpole (dashpole) 01:00:47 And bound instrument is better in the pre-computed case, and equivalent in other cases.
Tyler 01:00:53 Yeah. And I think there is a desire at a high level at the specification to also adopt this. So, what I've asked for, you've done, and I think that the answer is, like, we need something better than what we're doing, especially from the user's perspective, to try to get performance.
So let's… let's go that direction. I would like to pursue the bound instruments over the add with attributes, just based on ergonomics, but we can continue that discussion if you feel opposite, like, I'm happy to talk more about that.
David Ashpole (dashpole) 01:01:21 I explored ad with attributes, As an alternative to bound attributes.
Tyler 01:01:27 Yeah.
Okay, we are at time, so I do want to be respectful of people's time. I think this is great, thanks for putting in all that work. I did ask a lot of you, so I appreciate you jumping in on that. Let's keep going.
David Ashpole (dashpole) 01:01:41 If there's more discussion, let's have it in Slack or in those issues. But yeah, let's keep talking about it.
Tyler 01:01:47 Cool. Okay, everyone.
Bye.
David Ashpole (dashpole) 01:01:49 Bye.
