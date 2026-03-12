SIG: Client Instrumentation SIG
Date: 2025-10-28
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/HPq1intzL0hhoaJdzr-tqrqyz6HOqqfBsc6s2jDuEukBAO1--kQgUm4DlVjBsaQX.muNm5vws5IxhfpnZ
============================================================

## Zoom Recording Transcript

**João Oliveira** 00:11 mention it…
**Maciek Grzybowski** 00:13 That is wrong.
How are you?
**João Oliveira** 00:17 you're the nukes.
**Maciek Grzybowski** 00:18 I'm good.
**JP Jason Plumb** 01:14 This, this bi-weekly meeting's getting weird. Like, I never know who's gonna show up, it's, like, almost different every time.
**Maciek Grzybowski** 01:20 You enjoyed the right one.
Have you wanted her?
So we are from Datadoc, Masek and Joao.
**JP Jason Plumb** 01:32 Nice to meet you, I'm with, I'm with Splunk.
Yeah, yeah. So this, is an interesting SIG meeting now, because it used to be, and you can just tell me to shut up if you already know this, but, like, this client SIG was meeting for, like, a couple of years, and it was a combination of iOS, web, and Android.
Most of the momentum being around web.
And then once Android, you know, has been picking up momentum, there's been some more influence there, but they've peeled off the web kind of client stuff into its own web-specific SIG, and they meet weekly, I believe. Android also meets weekly.
This is meeting every two weeks, and it's only 30 minutes, and the idea is to, like, still have a forum, still have a way face-to-face, to share ideas or important things that might be coming up that span all three, or have similarities, or concerns that impact all three.
**Maciek Grzybowski** 02:30 Yeah, that's something that we kind of figured out. So, yes, the client SIG was split into… maybe not split, but it was reframed to work more on the semantic convention, to my understanding, versus browser Sik and Android sync, those are more… more on the implementation side of the thing, right? That's… that's the right… is this the right take?
**JP Jason Plumb** 02:53 I think that's pretty fair. Yeah, I mean, I think there's always gonna be semantic convention work, though.
Yeah. It's a big… it's a big part of all three.
Martin's our fearless leader over here.
de facto.
**Martin Kuba** 03:06 I don't know about that, I…
**JP Jason Plumb** 03:08 Seems like… seems like… feels like I haven't been here in a long time.
I was commenting before you joined that this is, like, getting to be a weird meeting, because I never know who's gonna show up. It seems like different people every week.
**Martin Kuba** 03:21 Hmm.
**JP Jason Plumb** 03:23 Yeah, I haven't opened the agenda yet. Is there an agenda? Probably not.
**Martin Kuba** 03:31 There's nothing on the agenda.
**JP Jason Plumb** 03:32 Okay.
**Martin Kuba** 03:38 Yeah.
**JP Jason Plumb** 03:41 So I will share something, I will, Let me put myself on the agenda for today.
We don't even have one yet.
Okay, 28th, man, October is flying by.
Hey!
There's Mr. Gomez Blanco.
**Dan Gomez Blanco** 04:13 Hello, hello, how's it going?
**JP Jason Plumb** 04:16 Good. You just came for our votes, didn't you?
**Dan Gomez Blanco** 04:20 No, no. Sorry, what's happening?
**JP Jason Plumb** 04:23 No, no, I was just gonna point out that, so we don't have an agenda.
**Dan Gomez Blanco** 04:27 Yep.
**JP Jason Plumb** 04:27 For today, the attendance to this meeting has been very weird. It's kind of mishmash, like, who shows up when has, like, been pretty chaotic. I was going to say, and maybe make a note in the agenda that, There is… an effort on Android to release a 1.0.
To release a stable Android agent, and our intention was to follow the pat… so I… I published a blog post maybe two and a half or three weeks ago on this topic. There was some… Added interest from some, like, real-world, like, large customers, vendors.
asking about stability on Android. They're like, it's been out there for a while, when's it going to be stable? Like, we've evaluated it, we want to use it, but we're hesitant because it's not marked stable.
**Dan Gomez Blanco** 05:17 So…
**JP Jason Plumb** 05:18 Cool, let's, let's market stable. Let's get to a 1-0. So I published a blog post about this, like, a few weeks ago. We have an issue that a few folks have chimed in on. It hasn't gotten tons of traction, but, like, we've had a few users ask questions there and, you know, give some feedback.
And we were about to cut a RC1, last week.
And… Currently, there is a blog post in progress from Austin, which is talking about having stability mean stability all the way through your stack, which was not something that we were planning on doing. We were trying to stabilize our topmost agent initializer, and then have our core and instrumentations remain alpha.
like, indefinitely, until we are more confident that we're not going to change them. And that follows the pattern that's been established for years in the Java agent, right? The Java agent itself It might be more 2.0, 2.1, whatever, stable, but the instrumentations that are underlying it are able to change, meaning the… I think the instrumentation API is also stable, but the telemetry emitted from them, and what they do, is definitely not stable. And so I think this blog post is more encouraging every component in a stack to be stable. So I put the brakes on it, and I said, we're not going to release one RC1 last week.
Until this kind of sorts out. So, we… we're looking for some… I mean, I'm looking at you, Daniel, and you can't tell, but I'm looking for… at you for some… we, Android, will need some guidance around this, as far as what direction we should take.
**Dan Gomez Blanco** 06:53 Yeah. Because we're not prepared to call the entire stack on Android.
**JP Jason Plumb** 06:57 stable yet?
**Dan Gomez Blanco** 06:58 Yeah, but I don't think the intention either is to, you know.
the intention is to say, well, you can, you know, you can have the API, SDK stable, and the instrumentation, any instrumentation that is considered an instrumentation library that's considered unstable to not be enabled by default, rather than, like, you know, the opposite, which is currently the case in Java, right? Everything's enabled by default.
Regardless of the state of the instrumentation library.
**JP Jason Plumb** 07:28 Yeah.
**Dan Gomez Blanco** 07:28 I guess that is probably where the compromise is, is to say, you know, your instrumentation packages don't all need to be stable. Even within instrumentation packages, there's discussion, they're to say.
Can we mark instrumentation packages as stable when the semantic conventions that they're based on are not stable yet?
Which is another one. I think, you know, the idea here is, like.
the answer will be, yes, we want to be able to do that. Mark a package as, like, stable, but then, say, the semantic conventions may be in, you know, developing or experimental. Yeah. But I do think that the intention is that you should be able to, say, for Android.
you know, and probably this requires more discussion, it's like, but I do think that's the… that's the way forward to say, you know.
you can have the API and SDK stable, marked as stable, but instrumentation packages that are unstable are disabled by default when you initiate, when you… M… I guess, you know, when you enable it.
**JP Jason Plumb** 08:36 So, at least on Java.
I think when we talked about it last week in the JavaSig, I think… I mean, we kind of ran out of time, but, like, the idea was, like, okay, the HTTP instrumentations, we could probably include them. They're… they're probably mostly stable because the SEMconf is stable.
**Dan Gomez Blanco** 08:55 Yeah.
**JP Jason Plumb** 08:55 But everything else kind of isn't, and I think most users expect to get all this rich telemetry, whether it's stable or not. And at least on Android, I mean, for an RC1 or a first release, I mean, I don't think we're prepared to call any of our instrumentation stable.
And what that would mean is that there's very little benefit in using… like, you would have to use the initializer, our top… Our top agent, but then you would have to manually configure all of the instrumentations, which is, like, one of the main benefits of using the agent, is that you kind of get a sane set of defaults.
**Dan Gomez Blanco** 09:31 Yeah, yeah. But there could be a… You know, a flag that one could say, you know, enable.
all the unstable. I think there's something that the… I know from the collector side, there was something that they were thinking about doing with collector, like, contrib components, which is start to basically, from the current Like, not do it completely… like, just… disable all components that are not stable right now, but I start with, you know, with levels of stability, and then go, like, right now, start to, like.
It made a log when you start up, basically saying, this is currently experimental, or this is in alpha at the moment.
we will… in the next release, we will, you know, we will start looking alpha, and then you do, like, an incremental approach. So, like, in a future release, what you do is, like, you start to, like, not include alpha components, and the next one not include, like, beta components, and so on. So I think that's… that's another, like, that's a more incremental approach.
So I think, ultimately, what we want to end up is in a place where, like, someone comes in, there's a new experimental component, and it's enabled by default in stable workloads. I think that's what we're trying to… to stop, right, is, like, more experimental stuff that can… that comes enabled by default with… when someone is already running something stable. I guess that's the… that's the thing. So here… if it was a… maybe a flag that could say, well, you know, by default, we're gonna be… only enable the stable ones, the stable instrumentations, none of them are stable. So you're gonna have to have this… pass this flag right now that says, well, enable unstable instrumentation.
**JP Jason Plumb** 11:22 I know, but I want to talk to this user who is uncomfortable using Android because it's not yet hit 1.0, it's not stable, yet is willing to add the flag, which is like, give me all the experimental shit. Like, I want to talk to that person.
**Dan Gomez Blanco** 11:35 Yeah.
**JP Jason Plumb** 11:36 Because they seem like a good time. Yeah.
**Dan Gomez Blanco** 11:38 But yeah, I know.
I wouldn't stable by tomorrow, by the way, yeah.
**JP Jason Plumb** 11:43 Oh yeah, yeah, and tomorrow, yeah, probably yesterday.
Okay, I follow what you're saying. Is there, do you know, are you aware of, or is there, concurrent specification work on this as well?
**Dan Gomez Blanco** 12:01 Not that I'm aware of. There's one thing that I'm aware of, which is the… even defining what… if we should use enable or disabled, I think that was being discussed. I was not in the spec call that was before this call, but I saw a thread of, like, you know, the fact that we still have, like, enable and disabled.
In different places.
**JP Jason Plumb** 12:24 Sure.
**Dan Gomez Blanco** 12:25 Yeah. So, like… It should be enabled, rather than disabled, like, you know, we shouldn't have, like, double, like, negate or, like… Not double negatives, but the… whatever the name is.
**JP Jason Plumb** 12:34 Yeah. Yeah. So…
**Dan Gomez Blanco** 12:37 that's one thing, but the other one is, I'm assuming that… and this is what Austin, with that draft of a blog post, was trying to get to, is like… I would yeah, I would say that there should be some type of, like, config option, That is… Or some way of approaching this that is, like… Standard across all languages and across all components.
So I think, you know, this type of a, you know, instrument… especially for instrumentation, right? Instrumentation packages.
the, you know, the way that… to approach this, as, you know, we talked about, like, is it a common flag for every instrumentation? Is it all disabled?
by default, and then we enable them one by one, but then we've got the… yeah, so I think that is something that should be defined.
I also…
**JP Jason Plumb** 13:32 Being a spec.
**Dan Gomez Blanco** 13:34 Yeah.
**JP Jason Plumb** 13:35 Yeah. That can't just be a blog post that defines that.
**Dan Gomez Blanco** 13:37 It needs to be there, yeah.
**JP Jason Plumb** 13:39 And we're not aware of anybody currently actively working on that?
**Dan Gomez Blanco** 13:44 I don't… no, I've not seen… I was doing triage on this bag this… This week, and nothing that was… no new issue that was raised.
Towards that.
Okay. But now that you mention that, you know, let me check. I'll check with, with Austin, maybe he's got something in mind.
I do think that the way to approach this should be in the specs somewhere.
**JP Jason Plumb** 14:06 Okay.
**Dan Gomez Blanco** 14:07 Either in the spec, Or in… well… I was just thinking the clarity of config, and then… now that we've got a moratorium for the environment variables.
But maybe we can… just get one… one more in. I don't know, something that basically allows us to do that sort of thing across multiple… multiple languages, but yeah.
**JP Jason Plumb** 14:30 Yep, okay. I have a couple more, kind of, specific use cases that I'd like to talk about, but I also… I mean, the agenda's empty, but I want to give room, because I will hog this whole 30 minutes, otherwise… I want to give room for other people if they have stuff they want to talk about specifically.
**Dan Gomez Blanco** 14:46 I wanted to raise one thing, but I also don't. Yeah.
It was shared by… so the technical committee is trying to find better ways of sponsoring… sponsoring sakes.
And that have not.
had anyone from the TC, like, almost like, in a guiding capacity, or like, you know, the TC went through a redefining what the TC sponsor is for a sake. And there are multiple levels, there is… Ty, you know, certain… SIGs that will require a TC member that is actively guiding it and leading it, or the SIGs that are, you know, in BAU, so like, you know, they're already ongoing, and the TC will just be there as an escalating, like, type of role, right?
And then Lyudmila reached out about the… I think she reached out in the client size channel, right? About… Yeah, so, discussion about the… one, if this SIG is active, and I, you know, I spoke to Lyudmila about this.
And, you know, how does it relate to the browser sig, for example? I think, Yeah, so there was that… this P… I'm linking here in the chat.
this discussion.
And… Related to… Yeah, aligning ADS of ownership.
And so, browser… Semantic conventions will be… Owned by browser.
But the browser's sick, but the new browser's sick, I think that's… I don't think that's contentious, that the browser sig, or, you know, people in the browser sig who owned, like, semantic conventions for browser. And basically, one of the things that… as well, implementation, right? For browser. I think that's a… as a language… not a language sig, but an implementation SIG.
And… for this SIG, I think we talked about moving this to strictly, basically, semantic… almost like being a semantic… a semantic convention SIG.
And I wanted to raise that.
**JP Jason Plumb** 16:56 With a mobile focus… or, sorry, with a client focus, or… With a client focus. Because there is already a semantic convention SIG, right?
**Dan Gomez Blanco** 17:03 Yeah, but there is, multiple semantic revision SIGs underneath, right, that are, like, normally temporary. Yeah. So, system metrics, Kubernetes, you know, Gen AI, although, you know.
GenAI is one of those that is like, when will it finish? Who knows? But, The… you know, the thing is, at the moment, if you look… if you go through… the list. Well, it's listed as, like, specification 6, but if you go through the list of, in the community, of list of SIGs, this one appears as, like, client instrumentation.
Which… maybe better rephrased as, like, semanticconventions.client site, or something like that, because… I don't think the aim of this SIG anymore is to actually work on instrumentations for…
**JP Jason Plumb** 17:58 I'm just sharing so that we're all looking at the same thing.
**Dan Gomez Blanco** 18:00 Yeah, yeah.
So if you scroll down, yeah.
**JP Jason Plumb** 18:05 Yeah, so you're talking about this, right?
**Dan Gomez Blanco** 18:07 Yeah, and then basically, I think at the moment, the… Yeah, so see how there is no TC… Sponsored there, right?
**JP Jason Plumb** 18:18 It's true.
**Dan Gomez Blanco** 18:20 So, yeah, so I think… what I wanted to propose is… Say, call this… The SIG.
Semantic convention sake, for client site.
And the next… I'm assuming that the… The focus could be on standardizing the cross-cutting elements of, of semantic conventions for client-side, like session, or…
**JP Jason Plumb** 18:48 Yeah.
**Dan Gomez Blanco** 18:48 brother.
Does that sound like a… like a good idea?
**JP Jason Plumb** 18:54 That seems completely reasonable to me.
**Dan Gomez Blanco** 18:59 And, and I guess, you know, put that in mind.
If we were to call out… What would be the… What would be the, the main focus, currently, of the SEC.
So I think maybe this is something that we're currently… probably the… the fact that we're having less people join, or, like, you know, discussion is, like, a bit stalled, is, like, identifying what the main focus should be. If it's session… if it's trying to work on the session ID, Or session attributes, basically.
M… Or any other that someone wants to raise that's cross-cutting across.
Mobile and browser.
And then we can probably put together, you know… Mmm… A new project proposal, that is scoped to not that many things, but…
**JP Jason Plumb** 19:56 Yeah, I can tell that's what you're getting at, is like, you want… there's a… it's… it appears that there's a need or a desire, and I think this is good, to make this, much more specifically scoped. Like, let's… let's say… this SIG is also maybe shorter-lived. Like, it exists to solve these three things. When it's done, we can… we can shut it down and think about maybe starting a new one when that initiative is there.
**Dan Gomez Blanco** 20:23 Yeah. Right. Yeah, that's correct. Yeah. A good example of this is what's happened to the CICD SIG. They had a Phase 1, which is completed, now they're in Phase 2. So, like, their project was… the SIG still remains.
But they moved on to another set of goals, right? So, like…
**JP Jason Plumb** 20:44 Okay, yeah.
**Dan Gomez Blanco** 20:44 So, like… It doesn't mean that, you know, client side, say, finishes after these three duns are done, but, like, you know, there is a current focus, and then move on to other things later.
**JP Jason Plumb** 20:57 M…
**Dan Gomez Blanco** 20:59 That's my…
**JP Jason Plumb** 21:00 God.
**Dan Gomez Blanco** 21:00 Yeah, that's my pitch.
**JP Jason Plumb** 21:02 I will suggest that if we're doing that, then we should probably meet weekly. Like, if we redefine the focus, and we get someone to kind of… if we get TC sponsorship that's like, here's… here's the… here's the 5 things we want to solve, people, then… then let's meet every week, because I think the two-week cadence is a little… I think it's hard just to keep momentum.
**Dan Gomez Blanco** 21:25 Yeah, that makes sense.
on that, I think, you know, one of the things I would like to call out, I'm not sure… Mmm… Yeah, for this, for example, for sessions, right? If the work on entities is a pre-requirement for this to, like.
To even start?
Or if we can start with this.
With, you know, stabilizing sessions.
While the work on entities is still ongoing.
And… beside… Right now, I think it's almost like a… you can take it either way. You can basically wait 4 sessions, and basically… or 4 entities.
And… you know, have a… a sort of, like, more stable ground to move on to, or I believe that, was it, Josh was saying that there may be… Able to provide a resource, like a resource API to be able to change elements of a resource or a resource. A way to basically be able to change not identifiable… Mmm… properties of, or attributes of… of the resource, so… Maybe that's all we need. I don't know. Right now, basically, I'm just… Not sure if we are in a position to to start stabilizing session, but maybe, maybe we are. So maybe that's something that we can discuss.
And the requirements for it.
**JP Jason Plumb** 22:56 Maybe.
**Dan Gomez Blanco** 22:58 And also get help from, like, get a review from the entities, so I can… I can raise that, basically, I can take an action and raise that with them as well.
**JP Jason Plumb** 23:13 Yeah, I just wanted to pull this up for a sec. So we have… we have attributes that are in development. We have an event, a couple of events that are in development.
I'm sure that web people hate this stuff.
like, having a session ID on any telemetry is, like.
At least it used to be a deal-breaker for anything on the web, like, oh, that… we can't put a session ID on every piece of telemetry, it's way too much data.
So yeah, I think… I think having a clear… decision about session would be great. This is where we landed, whatever, like, 2 years ago, and this is what we've been using since, but it is still in development, and getting these to migrate to stable would be awesome.
**Dan Gomez Blanco** 23:58 Yeah, I'd support that.
**JP Jason Plumb** 24:00 whatever that looks like. Yeah. If it's a readable resource, that's fine. That's a huge implementation concern in Java, but I would support Helping make that happen somehow.
**Martin Kuba** 24:11 So, a quick question on this, like, what… What would it, mean to, like, Take this to stable.
Because, like, the attributes themselves right now are pretty straightforward.
**Dan Gomez Blanco** 24:24 Yeah.
**Martin Kuba** 24:24 They can be added… they can be added either on individual events, or signals, or they can be added on… could be… could go on the resource, right?
So are we… Look into, like.
provide, provide, like, the, you know, finish, help the entity's sake, like, finish the work on… on sessions, like, maybe, like, help them with prototypes, and kind of guide, you know… Like, what would that mean to, like, take this to stable from this, sake perspective?
**Dan Gomez Blanco** 24:57 Yeah, I think it would be helping with the… Helping with the prototypes for, let's say, you know, we're to do it with entities and, you know, with a resource.
**Martin Kuba** 25:09 And… Okay.
**Dan Gomez Blanco** 25:10 with the new resource functionality, basically. And how we… and I guess one of the things that would be interesting to… stabilizing, that is how you… So at the moment, that's an attribute. In the semantic conventions, are we saying this is a… an attribute of… Spans, logs, blah blah blah.
Mmm… But then that would change, right? That would change into the resource. So, I guess… That's… that's what this double… I think we all know, in a way, that it's probably not the right thing, not the right place to put a session ID in every span attribute, or in every, you know… we know that it's not the right… the ultimate place where we want it to be, right? We want it to be somewhere more high level, which would be the… non-identified properties of a resource. So I think that would be the… To me, to call it stable, that would probably be what needs to happen.
And, yeah, so probably something to… agree on is what is interaction with, with entities say. It's like, are we waiting on them?
How can we start? Is there anything out there already that we can start to build on?
Even if it's, like, you know, prototypes for that, or… yeah, or completely blocks.
**JP Jason Plumb** 26:32 I mean, I think… I think that the short answer is this is our starting point, because that's what we have today, and this is currently the implementation in Android. I'm not sure if anybody else is using it, but it's a starting point. And then, there are prototypes, there are two prototypes, one that Josh built and one that I built.
That are… I mean, mine is definitely crusty and dying on the vine, like, by design, around entity, changes. Like, I kind of did that as a favor to Ted way back when, and I don't know, I've completely left that alone, and I have no idea where it stands, but, like, having some amount of mutability in the resource is… like, if that landed tomorrow, then we would… I think we would definitely want to, like, reevaluate this situation.
**Dan Gomez Blanco** 27:19 Yeah.
**JP Jason Plumb** 27:21 And, I mean, that is reinventing a conversation from 3 years ago, you know? Like, mutable resource.
**Dan Gomez Blanco** 27:28 Yeah, perfect.
**JP Jason Plumb** 27:29 With the sole intention of handling session.
**Dan Gomez Blanco** 27:33 Yeah, because I think it's actually happening…
**JP Jason Plumb** 27:36 Okay.
Well, we have 2 minutes left. What do you think are the next steps on this?
**Dan Gomez Blanco** 27:43 M…
**JP Jason Plumb** 27:43 Are you gonna write something up, or… What do you think… what's the next step?
**Dan Gomez Blanco** 27:48 Probably won't have time to write anything up until after KubeCon.
**JP Jason Plumb** 27:52 Yeah.
**Dan Gomez Blanco** 27:52 But…
**JP Jason Plumb** 27:53 Yeah.
**Dan Gomez Blanco** 27:54 But, yeah, if anyone has any bandwidth before, I'm happy to… to what with… with anybody, but, like, otherwise, you know, I will… Yeah, I'm planning to write something up in…
**JP Jason Plumb** 28:06 Okay.
**Dan Gomez Blanco** 28:07 In the next few… Weeks, month and a half.
**JP Jason Plumb** 28:11 Oh, which, you reminded me, we got a slot, we, client Sig, got a slot at the observatory.
**Dan Gomez Blanco** 28:19 Oh, yes, you're right.
**JP Jason Plumb** 28:21 Let me make a quick… yeah, let me make a quick note of that, so…
**Dan Gomez Blanco** 28:25 That would be a great place to discuss this.
**JP Jason Plumb** 28:27 Yeah, so here… That's a weird pace that just happened, but okay.
Cool.
**Dan Gomez Blanco** 28:41 even gone.
**JP Jason Plumb** 28:41 I love that it brought… I love that it brought…
**Dan Gomez Blanco** 28:43 Excellent.
**JP Jason Plumb** 28:44 the Slack-specific emoji over? How did it even do that?
**Dan Gomez Blanco** 28:48 Yeah.
**JP Jason Plumb** 28:49 Like, I couldn't do that again if I wanted to, like, that's brilliant. Okay.
**Dan Gomez Blanco** 28:55 Right. Cool, yeah, so for those who will be at KubeCon, we are meeting on Wednesday, from 11 to 12, so… but we will also be around, and it'd be good to chat about this stuff. Yeah, I think that would be a great place to… Maybe, like, a goal for that is, like, come up with a… with… With a set of, like.
goals, or a sort of focus, Items, yeah.
**JP Jason Plumb** 29:18 Yeah.
**Dan Gomez Blanco** 29:19 For the sake.
That'd be great.
**JP Jason Plumb** 29:20 Cool.
**Dan Gomez Blanco** 29:23 Q. Sorry, I took… All the time between these two things, but, like, hopefully that was useful.
**JP Jason Plumb** 29:30 Yeah, and Datadog folks, if you have stuff, you know, that's topical to client instrumentation, feel free to add it to the agenda for two weeks from now.
Which, actually, that is it, that's the middle of KubeCon, isn't it?
It's gonna… we're gonna cancel that one. We're gonna cancel a lot of SIGs due to KubeCon, I imagine.
**Dan Gomez Blanco** 29:50 Yeah, yeah, absolutely. We're not going to cancel all of them, I think.
**JP Jason Plumb** 29:53 Yeah.
**Dan Gomez Blanco** 29:54 I'm gonna put that in the notes, I just put it in Zoom there, but that's the… that's the PR that Josh raised with the Resource Provider SDK.
**JP Jason Plumb** 30:02 Yep.
**Dan Gomez Blanco** 30:03 Which…
**JP Jason Plumb** 30:04 Cooling.
**Dan Gomez Blanco** 30:05 Failed home.
**Maciek Grzybowski** 30:05 Yeah, just to say, on our side, yes, indeed, the session ID is, like, very central to us, and it's in the center of our interest, so we'll be following and trying to help contribute On this. I kind of understand what are the prerequisites in there. Sounds very interesting. So, yeah, stay tuned.
**JP Jason Plumb** 30:26 Cool.
Alright, it's nice to see everyone. See you at KubeCon, hopefully some.
**Dan Gomez Blanco** 30:32 Yep. See you there.
**JP Jason Plumb** 30:33 Alright?
**Dan Gomez Blanco** 30:34 Bye-bye.
**JP Jason Plumb** 30:35 Bye.
**Maciek Grzybowski** 30:36 Caps?
