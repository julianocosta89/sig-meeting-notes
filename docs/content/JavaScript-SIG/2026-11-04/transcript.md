SIG: JavaScript SIG
Date: 2026-11-04
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:04:35 Hello?
Aditya Reddy 00:04:37 Yay.
Sorry, I've… Handicarved on these SIG codes.
I can't open GitHub for her.
Google it, work.
Marc Pichler (Dynatrace) 00:04:53 Sorry, wait, I didn't hear the first word, I think you were cut off.
Aditya Reddy 00:04:57 Oh, it's… no, I'm… I'm… I'm pretty handicapped at the SIG call, because I can't really open… Gitubler.
Google Docs at work.
Marc Pichler (Dynatrace) 00:05:07 Oh, no.
Aditya Reddy 00:05:09 Whatever… whatever's being updated on the document is me asking cloud on my phone to do it on my PC, which is at home running.
Marc Pichler (Dynatrace) 00:05:22 Alright, we'll make it work somehow.
If there's anything you would want me to update while we're talking about it, please also feel free to just let me know, and I type it in there.
Aditya Reddy 00:05:37 Yeah, I just saw the update. Thanks for that.
Marc Pichler (Dynatrace) 00:05:41 Yeah, sure.
I'll share the screen real quick.
All right.
Welcome, everybody? I guess we can get started right away.
The first topic here is, aditya requesting reviews for…
Aditya Reddy 00:06:26 They've just been… It's already checked. I think it was even reviewed by Jack.
Marc Pichler (Dynatrace) 00:06:32 soon.
Aditya Reddy 00:06:34 But yeah, they're just things that are left hanging from a vial that I put out there.
Marc Pichler (Dynatrace) 00:06:40 One question, is this something that you ran into, somewhere, or did you just see it and,
Aditya Reddy 00:06:49 I'm just sorry.
Marc Pichler (Dynatrace) 00:06:49 I do believe.
Aditya Reddy 00:06:50 information.
Marc Pichler (Dynatrace) 00:06:52 Alright,
Trent Mick 00:06:55 general request, because I know you're coming up with lots of PRs, I presume.
AI-driven stuff, if you just… See a thing, as opposed to… A particular problem was hit in actual usage.
Could you please point that out? Because there's a big difference.
Aditya Reddy 00:07:12 Okay.
Trent Mick 00:07:13 in helping with prioritization, especially when we have gobs of PRs coming in, because we definitely want to get real user issues Dealt with first.
We can't.
Thanks, sir.
Aditya Reddy 00:07:22 That's good.
Marc Pichler (Dynatrace) 00:07:25 Yeah, also the reason why I was asking about this is… these, as opposed to touches, Batch log record processor, right?
Sorry, GitHub is not loading right now, so… And one of the things that always happens is there's a lot of, edge cases that, One can run into with… Dispatch exporters, dispatch processes, and… Almost every time we change something here, it leads to another bug. So, we need to be very careful in reviewing this.
The spec is unfortunately fairly complex in, Like, about the timing of things.
And… It's clearly written for languages that are multi-threaded.
Which we're not, and that makes it all the more complicated.
So, I tried to have a look at this, I think I was the last person to change this as well. So, Make sure to have a look at… Oh, what's going on here?
And then hopefully we can fix that. Probably if it's a bug in the logs SDK, it might also be a bug in the… In the trace SDK, because the way that these work is… pretty much the same. The spec is also pretty much the same for the lock,
Trent Mick 00:09:07 So that top comment.
Marc Pichler (Dynatrace) 00:09:08 Excellent.
Trent Mick 00:09:09 that was, in the removed lines, explicitly points this out and says, implying that that was a decision, which I vaguely remember when I was reviewing your last PR.
On this, Marc.
Is that we just decided subsequent flush was coming in. I don't know if that's just because we didn't want to… Deal with the complexity there, or we decided it wasn't important enough.
Marc Pichler (Dynatrace) 00:09:30 I don't record anymore.
what it was, I think that… I recall that the reason why I wanted to change it is because, We had recently changed the, Alto PX part isn't very recently, I mean… Like, not very recent, it's probably 4 months ago at this point, to retry.
properly. And what's happening on shutdown is that, Took way too long to actually finish.
I think the change that I did might have done… might have had something to do with it.
It's very likely that I thought this through and decided it was okay, but I need to double-check, I think. I need to get into it again.
Alright, I'll assign this to myself.
Aditya Reddy 00:10:42 The second one is just a soft deprecation package.
Marc Pichler (Dynatrace) 00:10:49 Yeah, let's do a web exception packaging content.
Looks like there's… Browse a repo issue of this…
Trent Mick 00:11:03 I would defer to the browser guys on this, on when they wanted to do that, I guess. David, do you happen to know? Or should we ask Jared or someone else?
Aditya Reddy 00:11:14 The initial review was Martin?
Trent Mick 00:11:18 Yeah, Martin would definitely know, yeah.
Marc Pichler (Dynatrace) 00:11:25 I guess, Martin would also be able to… moved the PR here since…
Trent Mick 00:11:36 Yeah, it looks like you've asked for a re-review from Martin, so that's probably the appropriate next reviewer.
Aditya Reddy 00:11:42 Cool, yeah, that's all I had. The third one was the issue that Marc… but he merged it in already.
Marc Pichler (Dynatrace) 00:11:50 Oh yeah, thanks for updating the docs there.
This was, just a note that, About how the peer dependency stuff works with, 3.0 and 2.0.
Guess that kind of leads us into the next topic as well.
By going through issues earlier today, I saw that, somebody failed this issue here.
That the OTRP expert has, still declared the wrong, Your dependency range.
when I changed the pure dependency ranges, I assumed that it would be okay to keep the OTLP exporters at this range.
But actually, what's happening is, NPM doesn't complain enough.
If, you try to install that with an old API version, and…
Trent Mick 00:13:00 So I like the way you carefully said that, it doesn't complain enough. Yeah, so NPM sucks here, or at least I don't understand.
Peer Dependencies has grown over the lifetime of MPM.
I have a… if you scroll down, I have a comment on this one that I just added right before the call.
So, if you do the original NPM install those packages, that's the first code block there, NPM gives you a bunch of useless kind of warnings, like, oh, something, something, you resolve, which 99% of people ignore and move on. NPM LS looks fine.
NPMLS-A, it shows, shows a whole bunch of warnings, and… or errors, actually, it errors out, saying, whoa, whoa, transitive dependency has an issue with the top-level API version that was installed.
Which, I guess, is a long way of saying NPM just kind of shrugged its shoulders and gave up on the original install.
If that was our intention, or, like… so, part of it makes me… okay.
I'm probably cool with us just bumping the pier depths and moving on, because that's… that's the hammer that we're using right now. But part of it, I wouldn't mind discussing for a little bit here to help my understanding or not, is whether we're… we're using it wrong.
So the breakage is actually in a peer dependency. In this case, it's an OTLP transformer.
I think is the name of the package. So, it has the… correct peer depth range on the API to get the newer version, because it's using, logs.severity number.
But… Taken another way, the OTLP transformer package is using the API, but it only has a peer depth, not a dependency on the API, which strikes me as… may be wrong. Like, if it's using the API, it should have a dependency on it, and I'm not sure if we can be relying on peer dependencies. Like, maybe there was a hope at some point that peer dependencies… since NPM7, they're installed by default, so things will shake out, but certainly doesn't look like the case when they're transitive.
Your dependencies, right?
So, like, the peer dependency on the package in question here, the… the… one of the trace exporter packages, it doesn't… it's fine, it doesn't use the API, so it's… it's… peer depth ranges, okay, it's issue at transitive peer depths. So, just for discussion, if people know quickly, I think it breaks my brain a little bit. If we had set the OTLP transformer to have a dependency on the API, The minimum version range that it needs.
What starts breaking for users?
We start getting multiple API versions installed in user's tree.
node modules tree. What's that gonna break?
Or will it?
Marc Pichler (Dynatrace) 00:15:50 anything.
Aditya Reddy 00:15:54 When it resolves to the first one it hits?
Marc Pichler (Dynatrace) 00:16:02 Could be a…
Trent Mick 00:16:04 So, like, one concern will be what gets globally registered for API, and whether users will surprisingly get a no-op. Instrumentations will surprisingly get a no-op.
That's one, and then another one, which would be more severe, both of them are bad, but the other one is if it can cause crashes somewhere, I don't… I think it can, though.
Marc Pichler (Dynatrace) 00:16:26 You know.
I don't think it can, as long as you… As, as, as long as a user… Or… package author.
properly specifies the dependency range. So if we go in and have 130 there as a dependency, it will still break, of course, because people might be able to install 130, but if we have a proper dependency on 1 to 10.
Then… we're good.
Unable.
Trent Mick 00:17:03 packages. On all the packages, you mean, or…
Marc Pichler (Dynatrace) 00:17:05 On all of our packages, We just need to specify the minimum properly, that's, Just the same as with any other package, really.
I think the reason why it is a peer dependency is to… Kind of completely give the user the choice, which API package is going to be installed.
Or at least that was the idea.
I think in, like, as you said earlier, in old NPM versions, it didn't install manually, it didn't install it automatically on the.
Trent Mick 00:17:44 The peer depths, yeah.
Marc Pichler (Dynatrace) 00:17:45 It would be a dip.
So… I assume that was the original intent.
I think these days… It's less important to do that.
Trent Mick 00:18:04 So, like, for now, I expect we're gonna do what the PR is doing, is all of our packages, and maybe all the ones in Contrib as well, we're gonna be bumping.
Marc Pichler (Dynatrace) 00:18:11 Yeah, I mean.
Trent Mick 00:18:12 I can't remember.
Marc Pichler (Dynatrace) 00:18:13 Yeah.
Trent Mick 00:18:13 Yeah.
Marc Pichler (Dynatrace) 00:18:14 the… it's not only a problem in the OTLP experts, but it's also a problem in the instrumentations, because they depend on The instrumentation-based package, and the instrumentation-based package uses the logs, export from the… API package.
So, we also need to pump all the instrumentations.
And…
Trent Mick 00:18:43 So that, if I have a third-party instrumentation that just uses tracing or metrics, doesn't touch logs at all.
I wouldn't feel like I needed to bump my API dependency here, right?
Marc Pichler (Dynatrace) 00:18:54 Right.
It was,
Trent Mick 00:18:57 But I would get this same potential crash, right?
I think.
Marc Pichler (Dynatrace) 00:19:05 You would, yeah. You would always get the crash, because it is actually used in the base class for instrumentation.
Since it uses logs.getLogger, I think.
It will always complain about it. It will complain sooner in… ESM, because you actually have an import there.
Where it imports logs, and if that's not there, then it will immediately crash.
For common JS, it takes a bit longer until you actually use it, which is even worse.
Jamie Danielson 00:19:51 I guess a question I have, just as sort of, like, a foundational thing, is my… Interpretation here is that, like, so we have peer dependency instead of direct dependency, so that someone else could potentially install a different package.
But… The reason why we would want to have it as a direct dependency anyway is to be that explicit of, like, what's happening here, where… we… it doesn't work, because it's looking for something in a newer API. Like, so I feel like it does kind of go together of, because we need something in 1.0, that's why some of, some things, like, fail, right? Like, if you don't add your transitive dependency as a regular dependency, a lot of tooling systems fail now because they say you're… you're not doing it right. You should be very explicit. So I think even… Like, that's kind of just what we're running into here, is… There's an idea of someone else being able to have a different version, but… That negates the reason why versioning exists for things like this.
Aditya Reddy 00:20:55 isn't, direction, like, or the good way to… like, you should know if… do you need it in production? Does your… Code break without it in production, then it's a main dependency, not a peer.
Jamie Danielson 00:21:14 So then I guess, like, the question ends up, like.
If we… if we keep the import as it is, then we have to bump… we have to have it as a true dependency, and therefore bump the minimum.
I guess the alternative is, do we need to import this from the API, or can we import it?
From something else, or… hardcode it.
2… I guess, further punt the… Although, I don't know what other issues come up then.
As far as, like, code mismatches and mismatched signatures.
Marc Pichler (Dynatrace) 00:21:58 Oh…
Trent Mick 00:21:59 Hey, I don't know if it'll work for me, sir, you might have to ignore me.
I had lost power here, so…
Jamie Danielson 00:22:05 Wow.
You missed a whole explanation of things.
Trent Mick 00:22:09 I know, I know, that was… it was a Hollywood moment.
And the big reveal is… ka-tune.
So yeah, I don't want to hold up everything, if you had an answer.
Burr.
Like, I'm guessing the answer is, let's revisit maybe how we want to do this, because if you're always going to potentially have that crash for downstream users, then maybe we want to change to using dependencies set up here depths, but I'm not sure if I missed the explanation.
But for now, let's… Bump the peer depths and get new versions out.
Jamie Danielson 00:22:40 Well, so, what I had just noted was that if we're using it, and, someone else had just mentioned also, like, if it's something that's required in production, then that should be a direct dependency, not a peer dependency. Like, the idea, you know, kind of makes sense of being able to install a different version depending on what you need, but… It's not… that's not how dependencies are intended to work, and versioning is intended to work, so… I think that if we're going to import this from API, then we have to do a direct dependency on it, and therefore bump the minimum.
And if not, the question was, is there a way to use this without importing the API and getting it in a different way?
I think that was… Generally.
Trent Mick 00:23:23 To use… sorry, for what to use this?
Jamie Danielson 00:23:26 let's say a hard-coded severity number, but then I don't know how it's used in here, if that still ends up in, like, signature mismatches and things like that. It might not be feasible.
Trent Mick 00:23:37 Yeah, I think that this is just the first symptom of the general problem of you depend on the new version of the API, so you need to… you need to have the new version of the API there. Yeah.
Yeah.
Jamie Danielson 00:23:53 Marc, were you gonna say something before?
Marc Pichler (Dynatrace) 00:23:56 I'm not sure if it's an actor, Problem or not, but, I think it might, like, actually using it as a dependency might run us into some issues with… what we are allowed to do in the API package, and what we are not allowed to do in terms of widening types and such.
But I think in general, it should always be possible to have, let's say we… bump the API version and actually have it as a dependency in the SDK.
We implement new features, and then the user registers it with an older API version.
That should always be possible. So… That's not the problem.
Trent Mick 00:24:58 Yep.
Marc Pichler (Dynatrace) 00:24:59 Yeah.
Trent Mick 00:24:59 I was agreeing with you, yeah.
Marc Pichler (Dynatrace) 00:25:01 I wonder if there's some edge case that… This might break.
But I can't come up with anything, so…
Trent Mick 00:25:16 Yep, so… I think we should do what this PR is doing, do it in Contrib, get new releases out, and then have another issue to talk about in… try to move to dependencies instead of peer-to apps for the API.
Marc Pichler (Dynatrace) 00:25:30 Yeah, maybe we can start trying that with instrumentation packages.
And see if anything breaks.
Before actually doing it with all of them.
Just to make sure that, not everything breaks at once.
Because adding back the peer dependency is gonna be a pain.
Possibly breaking to folks.
So we don't want to end up in that situation.
Trent Mick 00:25:59 So we need the OpenTelemetry 2… NPM org.
Marc Pichler (Dynatrace) 00:26:03 Yeah.
Trent Mick 00:26:04 Release everything there, get people to use that for a while.
Okay.
Marc Pichler (Dynatrace) 00:26:12 Yeah, I'll review the PR later and, proceed to merge it, and then I… Or do I move another Luna trip tomorrow?
Alright, I guess let's move on to the next topic. So, before this meeting, I was going through the focus topics.
thing, and I think we've kind of reached the limit of what the current framework can do in terms of, like, including people in discussions and whatnot. With the previous one, I just had them defined, And we just executed on those, but, The topics that are remaining now.
actually need a lot more discussion, I think, because they're not as straightforward anymore.
So, what I'm thinking of is, I would like to move this whole focus topic definition workflow to the doc directory.
And actually have markdown files where we… can then discuss on PRs, what we're gonna do, and kind of… End up with… Kind of a letter of intent to say, like, this is what we're trying to do, merge that in to main, and then we move on from there.
So that also people can, contribute to the discussion that usually can't make it to the SIG meeting.
And then we can also have these discussions, async, so not everybody has to hop onto the SIG core to actually leave their… their opinions there.
Does it sound like an okay approach for everybody?
Trent Mick 00:28:06 Yeah, that sounds great.
I thought… I don't know, is anyone with any other SIG had any… wasn't the hotel maintainers doing something like wanting roadmaps from the SIGs at some point, or proposing some ideas for roadmaps there? I don't know if there's any ideas to steal from that, or… it's an easy change to whatever the markdown format is for this thing that we can also satisfy that, might be nice. But, otherwise, I think this… this is a good idea.
Jamie Danielson 00:28:37 I feel like we can try to look at what some other ones are doing, like, I remember, like, a few of them have published the roadmap on the blog, like, I think Go… Maybe OB, but I can't remember anymore.
the question is more, I guess, ahead of it, like, before deciding, here's what our roadmap is, or here's what our focus is.
Where are other people having those conversations before deciding on?
the topics?
like, in Gen AI stuff for a little bit, that was primarily SIG-focused. It might still be, I haven't been there in a little bit.
Where it was discussed mostly during the SIG, and then we put something together.
Marc Pichler (Dynatrace) 00:29:24 Yeah, I will look through the other six, And maybe we can find some… predefined, workflow already that they have written down. I would be… Very happy to just take whatever works and implement that.
Yeah.
We don't need to come up with new stuff, if we… if something already exists.
Jamie Danielson 00:29:49 I agree.
Trent Mick 00:29:50 I don't know if this .roadmap repo that I just linked to is related to the… roadmap page on OpenTelemetry.io, but if it is, then I wonder if This is already a thing that they tried and deprecated, but… So, just to be aware.
Marc Pichler (Dynatrace) 00:30:07 Bye-bye.
Where did you link that? I'm sorry.
Trent Mick 00:30:11 Oh, and… In chat. In Zoom chat.
Jamie Danielson 00:30:15 It doesn't seem like in that particular one, though, like, that seems more of, again.
The publishing of the roadmap versus the debating and determining the roadmap.
Which I think is the thing we're trying to solve.
I think.
Trent Mick 00:30:35 Okay, cool.
Whatever, this is archived, so I assume ignore this, but yeah, if there's something you see from other SIG… That's good.
Marc Pichler (Dynatrace) 00:30:44 Then over… Go looking, and if not, then just come up with something, and we might have to figure it out ourselves.
Whatever I have in mind is fairly simple anyway, it's just, we have PRs for the topics, we discuss them, we merge them to a backlog, and then we have a work-in-progress limit.
Where we say, like, there's, like, maybe two of those that are inactive.
or in an Active Directory… not Active Directory, that's… that's not what we want to use here. But, like, there's a folder that's called Active, and remove it there, so… Yeah.
Alright.
Jamie Danielson 00:31:37 I guess, is that sort of how, like, OTEPs worked?
That was kind of like a PR, went into OTEP, and then that was like, okay, now it can go into spec.
Marc Pichler (Dynatrace) 00:31:47 Hmm.
It's very similar to that, but… Yeah, maybe a little bit less former,
Trent Mick 00:32:02 Right.
Speaking on statements of intent, just… my… Short-term focus will probably be on… getting declarative config stuff over the line. So, the stuff in SDK node… Start node SDK is, I think, almost ready to say Go as the alternative to new Node SDK.
So one of the tests there will be to… actually put docs for it and promote that. I don't know if we take it off experimental. It's experimental in an experimental package, so I'm not sure how more experimental you can get than that thing.
then the… I think the major two things following up on declarative config work is… is Matt's config provider PR, so that we can integrate, instrumentation config. So instrumentations can pick up configs, and declarative config is one. And then the other one is… I was gonna take a stab at what you'd… you'd taken a stab at, Marc a while ago, as the component provider, the plug-in component provider, and having support for that, because I think that that's the only clean way that auto-instrumentation's node, for example, or other distros can be part of declarative config. So, auto-instrumentation's node.
If you want to think through it, and wanting to use a declarative config file, it's the auto-instrumentations node package that's got to provide those extra resource detectors.
And the only way to… Get a declarative config file to be able to refer to those… the names of those resource detectors is for auto-institations node to use something like a plugin component provider that's in the config spec to say, hey, here's the implementation for those. So, I was going to take a stab at that, too.
And then, hopefully with those two things, then… We could say declarative configs go.
And what I'd like to work on, but won't have time for, is on instrumentation.
interface and cleaning all that stuff up, and then I would love someone to nuke all of our exporters and re-implement them as just one thing, because there are, like, 7,000 issues open on exporters, but… I won't have time for that one.
Marc Pichler (Dynatrace) 00:34:17 Yeah, while looking through the, focus topics that were defined, I was also looking through the exporter stuff, and there's so much, so many issues as well that I created that are outdated that I need to get rid of, somehow.
So, yeah.
Trent Mick 00:34:36 There's lingering stuff there. So the exporters are the only things that are still using environment variables that can get picked up, even if you're doing declarative config. So that's one edge.
That's what I was gonna say something else, too, for them.
Marc Pichler (Dynatrace) 00:34:51 Maybe on the topic of, the… Expert focus topic, and stabilizing these.
Since we used the, environment variables there.
I wonder if… it would be better to just completely re-implement the exporters, and just have, like, all the exporters in a single package, rather than having them spread over, I don't know how many there are, like, 12 now, 12 different packages.
Do any of you have any preference?
One way or the.
Trent Mick 00:35:36 So… the only part I wasn't sure on was… okay, so I'm… I mean, the way we have it now is the way it breaks down if you want to offer two features to people. One is… I can get it for just a signal, one signal, and I don't have to take the install size for the other signals. I'm not sure install size there is a big issue. And then the other one is the gRPC dip.
It used to be the protobuf deck, but we don't have that anymore, because we have the manual. So the GRPC one might still be augmented, in that people might prefer to not install that dependency. I'm not sure that that… really… is a big thing, though. One interesting side note on that is the… If… are people all aware of Microtel?
This is a repo on the Node.js org that's looking at implementing a small subset of hotel inside Node Core, so this is a JS package that would then get bundled into Node.js 27 and later, I think.
That would provide, basically, you get a little init thing to turn it on to define your endpoint, basically, and then it'll do… instrumentation for HTTP and Indige, so for Fetch.
Basically.
Just tracing.
the only reason I bring this up is there's a PR that was just taking a stab at doing a… gRPC client implementation locally without using the gRPC JSDEP.
Which is something that we could consider stealing to do the same thing that we did for Protobuff, but… Anyway… circular, to get back to what you're saying, I think, yeah, we could possibly just have one or two packages for exporters. And one could be the node, all the node exporters, and the only second one that I would think is the browser one. Like, I think the browser exporter should be totally separate. There's no reason to cross those things over.
And I guess if the browser guys are gonna do it, they just do it in their repo, so… Maybe we just have one.
Marc Pichler (Dynatrace) 00:37:46 Yeah.
I think one of the benefits of doing that is also we can… move quickly.
Implementing these things without having to consider, breaking changes to users.
Where we go through of all of these things, and then there's one clean migration path to a new… package.
Trent Mick 00:38:10 Yeah.
Agreed. We can get that work… work on for a while until it's… we feel it's kind of solid, and then start recommending it, and deprecate the old ones, and then remove them in V4, yeah.
Marc Pichler (Dynatrace) 00:38:23 then whatever thing I'm going to propose for the focus topic, exporter stabilization is going to go that route.
Having a separate package.
I think it also helps with reducing the public API, because… We ended up with this, Pretending to be internal packages that are still published to NPM.
Trent Mick 00:38:47 Yes, that's gross.
Marc Pichler (Dynatrace) 00:38:48 cheaper than start using.
Trent Mick 00:38:52 I think most people here don't even… aren't even aware of it, but… Yeah.
Marc Pichler (Dynatrace) 00:38:56 Yeah, I found that a lot more people are aware than I would like.
Trent Mick 00:39:01 I think it's called internal, right? It's an export called internal.
Which is awesome.
Marc Pichler (Dynatrace) 00:39:07 Might be,
Trent Mick 00:39:10 I might be wrong.
Marc Pichler (Dynatrace) 00:39:11 I think… I think that might be in… The core package, which is another one of these, but yeah.
Alright.
Anything else, any of you would like to discuss?
If not, then, I guess we can do… some bug triage.
Matt Wear 00:39:45 this is probably not worthy of much of a discussion, or really an agenda item, but, I think the… the packaging SIG does want to, like, come up with a, supported support a way the injector can auto-inject JS going forward, so I think, Michaela, who I work with, is gonna come up with some… Some proposals, and it'd be nice if we can kind of work together to, to come up with something that we can consider stable going forward. I know the way that Boom.
injection was being done before, probably nobody had any idea about until it broke, so…
Trent Mick 00:40:28 Matt Dior Organizcio.
Matt Wear 00:40:29 I do.
Trent Mick 00:40:31 Okay, so you're talking about Michelle?
Sorry.
Matt Wear 00:40:33 Yeah,
Trent Mick 00:40:33 Or is that how you pronounce his name? I'm sorry.
Matt Wear 00:40:36 It's a hard seat. Mikhailov.
Trent Mick 00:40:38 Michaela, okay, sorry, I've been getting it wrong.
So is this about the auto-instrumentations node and the need for the injector to use a deep path?
Matt Wear 00:40:49 Yeah, so…
Trent Mick 00:40:50 And that changed. Yeah. I'm not sure if other people are aware of that.
Matt Wear 00:40:54 And looking at that, I wasn't aware of it either, and I don't know how anybody really would have been aware of it until this breakage occurred, but… but having, like, a contract, I think… Yeah, I think the packaging SIG and the injector in general just needs to make sure that whatever contract they're using needs to be explicit with the SIGs so that, we all know not to break it, and Yeah, this one we're kind of addressing, retroactively, but… Yeah, I… I was just gonna say that.
we'll be coming up with some proposals, I guess, and if you have some too, let me know and I can help.
Trent Mick 00:41:38 Yeah, I'm not exactly sure what the… like, I know one way I could fix that issue. Our… Oop.
people aware of what the issue was here? Not Jamie, Marc? Do you know it?
Marc Pichler (Dynatrace) 00:41:48 I'm not aware, I'm trying to find it now, but it's probably this, right?
Trent Mick 00:41:54 There you go.
Yeah. So, well, okay, so I brought that up just as I was working through, okay, 3.0, what's gonna change? And I know I was looking at Lambda, and the injector, and the operator, and all the places that are using the SDK.
And yeah, sure enough, this was an issue, but I was just looking for issues and found it, rather than… Being a user of the injector and having it broken. So yeah.
to use… so normally we would think auto-instrumentations node, to use the zero code thing, you just need to use dash dash import, auto-instrumentations node slash register, right? And that's using an entry point, and that should work fine. Whatever the implementation file is underneath the dist or build directory is an implementation detail, you don't need to worry about it. The way the injector works.
And the way Lambda could work, but it does it a different way, is it installs… the auto-instrumentations node in all its depth in some other directory that's outside the user's Notepath.
So they can't use the entry point. They have to do dash dash require or dash dash import of the full path to the thing.
Well, when they updated AutoInstrumentation's node, the full path to register.mjs is now a different path, so that broke.
For them.
And, yeah, I said normally that's the implementation detail, and… In this case, it isn't, so I'm not sure what the exact… Right answer is.
If it wasn't an entry… if it was the top-level entry point, then you could get away with it, because you can do dash dash require to an absolute directory, and I'm not sure if it readspacks.json does the main file or not, but it'll… it would pick it up, so you could get away with that, if we had another package that was just… anyway, you know what I mean? If it wasn't dash slash register, but it was the top level of the package, you could get away with it.
That, or we just say, like, unfortunately, this is a break that we had, because we changed what we're using internally, and we could just say, like, distregister.cgs will be stable going forward.
I don't know.
Matt Wear 00:43:58 I was just thinking, what about one, like, at the root?
just a registered JS that lives there, would that…
Trent Mick 00:44:05 Yeah, we could maybe do that, and that defers to whatever the actual current build dist implementation is right now. Yeah, I think that could… is that what you're saying?
Matt Wear 00:44:14 Yeah, that's what I was thinking. It could just be the contract, and then, that can, internally do whatever needs to be done, but…
Trent Mick 00:44:22 That probably sounds more reasonable, yeah.
Matt Wear 00:44:25 Oh, Cool, yeah, I think Michaela does have a PR open in Contrib to at least restore that temporarily, so I think kind of bridging that gap might be something that would be good to do, just so that existing injectors can work with newer releases.
Trent Mick 00:44:54 Okay.
Matt Wear 00:45:01 So, yeah, like, I think, like, a perfect solution would be if we can kind of bridge this gap for a few releases, until injectors, yeah, until we agree on the new format, and then, kind of, injectors can update. Injectors can do both for a little while, and then just switch to the kind of supported one.
With minimal disruption.
Marc Pichler (Dynatrace) 00:45:24 Yeah, I think that sounds good.
I might have to play around with that whole thing a little bit, too.
Fully understand how it, oh, it would work.
like, the other approach that we were talking about now, but bridging the gap, I think, is a good idea. Anyway, if we're gonna bump the API version now on all the country packages.
We should make sure to also include this fix here in the release, so that, We restore functionality quickly.
I also put that on my list of PRs, so… I'm already assigned anyway.
So we don't forget about it. Thank you.
merging that… Right.
Maybe a question to everybody. Did anybody notice any, problems that we didn't discuss yet about the 3.0 release? Anything that came up?
That doesn't have its own issue yet, maybe.
Trent Mick 00:46:53 Now, there's one that has a PR that's merged, so we should get a release for it, the forwarded parse.
inside instrumentation HTTP was, I think, the… maybe the only package that's doing a lazy require.
Yay. Go in.
Raphaël Thériault 00:47:08 There is, like, everything, and it's the only one left.
Trent Mick 00:47:12 Awesome, okay. So yeah, that's another reason to get a release out.
Marc Pichler (Dynatrace) 00:47:19 Let's just… Pure here.
Alright, then I'll look to… I'll look into having a release tomorrow, so that, bill Get it out this week, still.
Permit.
Looking into backtriage, we have nothing here in the corrible, and… Nothing new in the country repo, let's just check really quick if there's anything that looks like a bug, but… Actually… It's not filed through the… Proper template… Oh, this looks like a park.
Ticket to me… What's the impact of that?
That's probably leading to… the loss of telemetry, so that's P2.
That's the SDK Freeze package.
That also looks like… a bug report.
RSOP2, and… The implementation for that is in… GRP exporter base.
It also looks like a bug,
Trent Mick 00:49:55 Oh, I definitely knew about this one.
Though maybe I've been keeping that on my private list for a long time.
Marc Pichler (Dynatrace) 00:50:04 I seem to remember that we had an issue, Ported somewhere.
This is the fair silently, then this is Arsenal.
into… I guess this… Is a problem with… another, instrumentation.
Face… think.
Trent Mick 00:50:45 Yep.
So this is one of the issues that I would like to solve in the… Eviscerate the instrumentation.
Package.
Thing.
Of course, I'm… Any stabs I've taken at it so far are invariably only have a… Instrumentation 2 interface.
Which is kind of gross, because there'll be a long migration process where we have two kinds of instrumentations out there, because the interface is a bit gross right now. Anyway, the answer for this one is that, sorry, I did air quotes there, but I realized my video's off.
for this is that the… patcher, so require in the middle or import in the middle. One instance is created by the SDK that is shared by all the instrumentations that are registered with it.
Instead of what we have right now, is that each instrumentation can create its own.
Import in the middle.
Patcher, which, if they have two separate installs of import in the middle, you get exactly this problem.
So if there's only one and one wins, then… You know which one you're talking about, and they sh… they have the same global state, so you don't get the issue here.
If that makes sense. Anyway.
Vaporware.
Marc Pichler (Dynatrace) 00:52:17 We're talking about vaporware, there's also… be tracing general instrumentation, work that I'm… Looking into now that we have contacts attached and detach.
Could have maybe in some of these cases, because then we can avoid having input in the middle at all.
Trent Mick 00:52:43 Some of them, yeah. There was, Yes, and there was some effort by a guy in the community, Bridger, I think it works at Datadog, to get Modules in the ecosystem to export diagnostic channels, so that you can use that for instrumentation.
Marc Pichler (Dynatrace) 00:53:10 Bone?
That also looks like a bucket part.
I'm gonna also label that as part of E2.
Of course, it has a PR already.
That's also gonna be in Exporter Place.
Is… is… Oh.
Expected behavior… Or at least we intended that to happen.
Trent Mick 00:54:31 That's the one that I think… Adity added that.
Doc note for it in the migration guide, saying… Sorry.
If you're on 2.x, don't use the latest.
API.
Marc Pichler (Dynatrace) 00:54:46 Yeah.
I think I would like to, Keep the issue around for now, to see if other people also run into trouble with this.
just to get a feeling of… How many people run into the same thing, and if… we actually need to change something on the 2.X line. I'd like to avoid, if at all possible, changing the 2.X line to also include, support for this version of the API, but, yep.
Trent Mick 00:55:24 Okay.
Marc Pichler (Dynatrace) 00:55:25 If somebody runs into that, they can, use the thumbs-up thing.
Interestingly, it's missing the user, I think usually when people open issues. It has this small note that says… break your thumbs up.
But that one's missing from the issue.
Oh, no, it's… there later.
Alright, I guess, we can… stop going through the issues here now, let's give Contrape a quick look.
is ours is a bug report, but doesn't have the labors on it. I wonder if all of these are created with… Some sort of agent that ignores the templates.
Jamie Danielson 00:56:48 Probably.
Marc Pichler (Dynatrace) 00:56:50 Yeah.
There's a P2 label on here? I'm not exactly sure if that's, like, an express… instrumentation Express issue, or instrument.
Trent Mick 00:57:27 Yeah, I think it is.
Marc Pichler (Dynatrace) 00:57:28 the issue.
Trent Mick 00:57:30 Okay, well, yeah, I'm not sure what the solution is, but I think Express 5 changed to be using router for its routing.
And we were already instrumenting router.
Express 4 users could use separately if they wanted to as a router, so… Yeah, it… This should make sense.
I'm not sure what the proposed fix is.
Marc Pichler (Dynatrace) 00:57:58 I guess if it's, optional on… Express… 4.
And included always in Express 5.
We could just not instrument that path.
in Express 5, and just rely on instrumentation rather being there.
One of the downsides is that then people will need both, and they might not know to install both of them and register them.
So…
Jamie Danielson 00:58:33 Yeah, like, if they're just… like, this is for the auto-instrumentations node, but… If they are just saying, yeah, just install HTTP and Express instrumentation, they're not gonna get the instrumentation they expect.
Marc Pichler (Dynatrace) 00:58:50 What actually happens if… So, I never tried.
But what happens if you register the same instrumentation twice?
It probably won't patch it again, right?
Trent Mick 00:59:05 Yes, I think you're correct.
I think, actually, what it might do is unwrap and then rewrap again, so the second one will win.
So, in the… Instrumentation evisceration project.
I wanted to kill… I wanted to kill unwrapping.
Jamie Danielson 00:59:23 I was about to ask about that, yeah, I remember.
Trent Mick 00:59:26 So that… that unintended behavior would change, but… Yeah.
So that you would probably get double instrumentation, which I don't think is totally unreasonable if you register an instrumentation twice.
With potential conflicts and stuff happening.
I think the browser guys deal more with this, don't they? Where two instrumentations wrap the same web API?
I'm gonna have to deal with that, or… You get webpages that have 7,000 megabytes of… JavaScript and 7 different agents that are all wrapping the same thing, so, like, they've given up on Unwrap, basically.
David Luna Bistuer 01:00:08 Yeah, that's right.
Marc Pichler (Dynatrace) 01:00:20 this is appropriately labored now, so I guess we can come up with the… Solution to that, and another…
Jamie Danielson 01:00:27 I'm at a discussion label.
Oh, you don't have, you don't have to do that. That's my thought right now, is discussion label, because I don't know the exact answer.
Trent Mick 01:00:42 how would users discover that and know that? Like, do you just… would we want…
Jamie Danielson 01:00:49 I mean…
Trent Mick 01:00:49 Like, say we had documentation, like, hey, you're an Express user and you want to use OTEL, and so you're going to do this. And here's a thing to be aware of, you're going to get double, so what you probably want to do, and only you, because you're an Express 5 user, is disable the router instrumentation, because you're going to get it from the Express 5.
Jamie Danielson 01:01:06 Well, Java has something like that, because there are scenarios where you basically get duplicate spans for things, and so they have things like I don't know, it's something about choosing one, Like, that is a flag that other people may not have to do, but you might have to do if this applies to you.
So we might end up having something like that. There's an extra configuration knob for it.
Trent Mick 01:01:34 I mean, it looks like the configuration… a reasonable one in this case exists, so you do the… to… Theater.
Jamie Danielson 01:01:41 It does accept that.
Trent Mick 01:01:42 a writer instrumentation.
Jamie Danielson 01:01:44 But then, doesn't that make… what if you have router instrumentation instrumenting something else that isn't Express?
You've just turned it off for everything, right?
Trent Mick 01:01:52 In the same app?
Jamie Danielson 01:01:54 I don't know. Do people do that? That's sort of a devil's advocate question, really.
Trent Mick 01:01:58 Yeah, I understand. I don't know.
Marc Pichler (Dynatrace) 01:02:03 Everything that can happen will happen. Right.
Jamie Danielson 01:02:07 Like, maybe you're halfway through switching from Express to, you know, something else.
I don't know how that works, ignore me.
Raphaël Thériault 01:02:16 I just noticed, too, that there's been, like, a long-standing PR on the router repo to add diagnostics channel support, and it's merged now.
So, and that supports, like, basically everything that the express instrumentation does.
So I'm wondering, maybe, do we just want to, say, disable the Express 1, the Express instrumentation for Express 5, and just use Router?
Jamie Danielson 01:02:41 Right, so the opposite…
Raphaël Thériault 01:02:42 In the perfect future, yeah. And then you don't have the issue if someone's using router for stuff that's not express.
Jamie Danielson 01:02:49 That's nice, because that's also more generic than, to your point. It's not just, here's an express-specific problem, it's anything that's using router.
Marc Pichler (Dynatrace) 01:03:06 I just had an interesting thought about the core instrumenting, diagnostics genre.
instrumenting based on the diagnostic channel thing is… We would probably need some mechanism to determine whether We've already instrumented something or not.
To avoid generating duplicate spans and stuff.
Which… haven't considered.
Before.
Trent Mick 01:03:38 You mean for this case, or for other instrumentations?
Marc Pichler (Dynatrace) 01:03:42 For other instrumentations, mostly. Because there might…
Trent Mick 01:03:46 like, an instrumentation would do one or the other, so I wouldn't think you'd get duplicate.
Marc Pichler (Dynatrace) 01:03:53 Usually you wouldn't.
Unless there's some overlap… overlapping instrumentations.
Yeah, it's probably not… Not something to be considered for a first version, but, yeah.
Anyway, I think we're out of time, so… Thank you, everybody, for joining.
Have a nice week, and see you next week.
Jackson Weber 01:04:19 Yep, have a good one, y'all.
Matt Wear 01:04:21 X.
Marc Pichler (Dynatrace) 01:04:21 Thank you, bye.
