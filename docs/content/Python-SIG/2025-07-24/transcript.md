SIG: Python SIG
Date: 2025-07-24
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Riccardo Magliocchetti 00:02:39 Hello! Everyone.
Keith Decker 00:02:46 Hello!
Riccardo Magliocchetti 00:02:47 Okay, welcome to this week, Python Weekly call.
and we'll wait a few more minutes for more people to join, and in the meantime, please add yourself to the list of attendees in the notes.
and also, if you have any last minute topic, please add it to to the notes.
and if you don't have the link, I've shared it to the Zoom chat.
Okay? So 5, I think we can start welcome again.
And 1st topic from today is from Aaron.
Aaron Abbott 00:06:35 Yeah.
Riccardo Magliocchetti 00:06:36 Cool.
Aaron Abbott 00:06:37 Yeah, I'm here.
I think this is so. So I think there was a question slack about this, too.
but our current logs, Api and SDK are marked Alpha they've been around for, I think, about 2 years.
so I wanted to. We could discuss the project board and see what tasks we wanna get through before.
But I wanted to see how people are feeling about it and check in.
And then figure out what the actual process is which I think is mostly just updating the open telemetry. I/O, kind of landing page for python.
So yeah, anyone have any thoughts.
Emídio 00:07:24 From what I what I'm seeing in open telemetry. I/O. Page, we are saying, logs are in development.
Aaron Abbott 00:07:37 You mean the spec or oh, you mean on our our side.
Emídio 00:07:42 In the web page like, Yeah. This one.
Aaron Abbott 00:07:55 Yeah, okay, so maybe we need to market. Alpha first.st
Emídio 00:08:02 Yeah.
maybe. Can we set like a if established shoppers like a.
Aaron Abbott 00:08:12 If we have.
Emídio 00:08:14 80% of the issues solved like, we can move to another maturity level, like like some something like that.
Aaron Abbott 00:08:28 I'm actually also looking at the spec page. Somebody pulled it up. So it seems like, there's basically just development stable deprecated, removed.
I guess there's no such thing as Beta necessarily.
Emídio 00:08:46 Oh!
Aaron Abbott 00:08:48 I feel like that's something we had previously. But that's okay. I guess. Kind of regardless.
How are people feeling about logs? Api SDK, and like, I mean, eventually we get to the point of doing release candidate and such. But yeah, how are folks doing.
Riccardo Magliocchetti 00:09:15 Like for me. I'd like, before changing the status, to start managing the renamings and stuff like that.
And you know, when we are quite confident.
but most of the stuff is done. Start, maybe signal that we want more testers, and so the signal is like Alpha Beta, or whatever. But.
Aaron Abbott 00:09:47 Yep.
yeah, I I definitely agree. I think we want to get the naming changes out of the way and fix some of the Api stuff.
Maybe we could also take a look at the Project board, Ricardo, that you have.
Riccardo Magliocchetti 00:10:33 Yeah, we have a ton of stuff there.
Aaron Abbott 00:10:37 Yeah, yeah.
So I don't think all of them are necessarily part of the log stability. So like, for example, moving the the log handler out of the Api and SDK or out of the SDK. Would make it a bit easier, I think, because there's kind of some outstanding behavior questions we have.
and it's not really tied to the core. Api and SDK, But yeah, there's definitely a fair number here.
A lot of them are related to auto instrumentation right now. So yeah, I feel like, kind of untangling. The auto instrumentation from the actual core implementation would be really helpful.
Riccardo Magliocchetti 00:11:31 Yeah, like a lot of stuff that I don't recognize at the moment.
But yeah.
like, do you want to go like one by one. Or maybe we can take a look and just decide what to move and consider for.
Yeah, like, the board. Yeah.
Aaron Abbott 00:12:00 Yeah, I mean, we could do that online. If people want, I think we should probably if we do that, we should move it to end of the agenda for today.
But I'm also happy to kind of go through. We could like make a milestone.
or probably remove some of these from Api, SDK, Rc, and move them to like a different post. Ga, kind of thing or or something like that.
But yeah, let's let's definitely move it to the end. I guess I just wanted to to know also in terms of priorities, if if this was important to people like planning to work on it.
If this is a Sig goal.
do you feel like? It's a good effort, and we can contribute to it and make progress.
All that.
Riccardo Magliocchetti 00:12:50 Yeah, makes sense.
So if you have time later, just come back to this as a comment for an opinion or whatever.
Yeah.
Hector Hernandez 00:13:07 I think the locks stabilization is a very high priority for Microsoft. At least we have been wanting to have this stable for a while.
So we're happy to help to move this forward. And I think it's a great idea to do this cleanup. And let's just if we're going to start getting some people to focus on that. It will be awesome.
Aaron Abbott 00:13:31 Okay. Yeah.
Paulo Vital 00:13:34 Just just one note regarding the logs as well. Ibm is is starting to use a lot of the logs coming from hotel, so would be interesting to have those coming from the the python applications as well.
And yeah, we would love to contribute with the effort to have that stabilize it as well.
You can count on those.
Aaron Abbott 00:14:04 Okay. Awesome. Thank you.
So I think maybe myself, we could definitely go through the the board at the end. And you know, kind of do the stuff that we need to do as maintainers to come up with what the what the actual important ones are.
we we could save that for the end. I'm okay to move on unless anybody else wants to share their 2 cents.
Riccardo Magliocchetti 00:14:36 Okay, okay, thank you, Adam.
And the next topic is from Paulo.
which links to a select discussion.
Paulo Vital 00:14:51 Yeah. I asked about this yesterday or 2 days ago. We have an internal project at Ibm that their customer is an Us. Government client. And they need to run their application with the Fips mode on. And yeah, one of the components. They have dependencies on the open telemetry, Api, the SDK, and also the exporter for the Grpc.
And they asked us if they are pips compliant, and then I I I was looking for, and I did not find any information about that.
And I would like to know then, if you guys, if if there is any fips work already done, if we can.
Tell them that. Yeah, there is no compliance issues or something else. I saw that in immediate about certification it's not the case to be certified, but only to guarantee that we are compliant. It's not necessary to run and got any certification for the project, but only to confirm that we can run with the on top of a system that that is fips compliant.
So does anyone have any experience or test project on that matter that then I can provide the information for the internal project here, or would be interesting to the project to the Sig.
Do like Estra work on effort to make sure that we can guarantee at least Api and SDK are fibs compliant.
Riccardo Magliocchetti 00:17:29 Like. As a media said, I don't think we have any Fips issues in our code, because, like, we don't provide crypto, and they don't remember any code that is using some flucky algorithms or stuff like that.
but like, it would be nice maybe, to run some of our tests under a Fips enabled distro. I don't know if images available or not, but my suggestion would be like, try to run the test suite on on both for repo on fibs enabled repos enable images and see what happens like, I don't expect any issues, but until we test we don't know. Like.
Dan Gomez Blanco 00:18:25 Is there a requirement as well for Fips compliance on the python SDK on the python packages? Or I guess you know, I guess from the customer perspective. Or you know, if you feed that through.
Collector, and the collector passes that.
Compliance.
Then that's okay. I mean, I know nothing about Febs, I have to say, but you know it's just my question on that.
Paulo Vital 00:18:51 Yeah, if it. If if they need a a whole system to be compliant, then also the collector needs to be tested and inspected.
But here the guy that asked me. They they are responsible for only one part of the huge project.
and they have the open telemetry as dependence as they are using open telemetry to to collect the tracers and the dispense and metrics and sent to to instanta sona is fips compliant.
So hearing in the year, in this case they are using the the python package to collect the metrics and the tracers, and then using instant as the collector. Yeah.
Dan Gomez Blanco 00:19:58 Yeah. So I think looking at that thread on slack as well. The I agree with Antoine as well, saying that there is probably a wider effort. Maybe you know, and And the way that these wider efforts normally work in open telemetry is with a you know, if someone wants to like work on it is to create what's called a project, and basically get some people behind us across cutting project where we can. You know we can work on it. Or you know, whoever like volunteers to work on a project to? Yeah, to say, okay, so how do we? How do we think about fips compliance across open telemetry, right?
But it all starts with a proposal in the community. Repo. If someone wants to start that wider.
I will say as well that there are quite a lot of things on the pipeline, for.
because that normally requires, like a sponsorship from the Technical Committee and and Governance Committee. So you know, there are quite a lot of things in the pipeline at the moment, and I can't promise that that will be.
I guess, prioritized, but it does sound like it would be a wider and wider issue than the python alone. I guess.
Paulo Vital 00:21:15 Yeah, yeah, yeah, completely agree. Yeah.
yeah, thanks. Anyway, I will try on on my side to run the tests on clips system. And then I can give back the information for for you guys as well.
Riccardo Magliocchetti 00:21:40 Thank you. Paula.
Paulo Vital 00:21:44 So.
Riccardo Magliocchetti 00:21:45 Okay.
This topic is from Keith.
Keith Decker 00:21:52 Okay.
keep here. So we're looking to add Weva instrumentation to the python. Currently, the there is a weva instrumentation out there under trace loops repository, but it doesn't support metrics and events. So we're looking to add that here.
So this Pr is just the structure around it. I think I wanted to come here because the the name of the package would clash with trace loops.
Aaron Abbott 00:22:25 Hey, Keith? So yeah, we've we've had this kind of discussion going on a while with Traceloop so for some of our other packages we were able to kind of do like a split versioning where we'll use the same package name, and we would publish to like a 2 Dot X version branches.
kind of under the assumption that eventually everything would be moved into hotel or things that we want in hotel would be transferred over so so near from Traceloop is probably your best contact there. I would try to get in touch with him on slack, but he's usually pretty open to this kind of thing, but I don't want to speak for him. So for the vertex AI instrumentation, and for I think, Lane chain, we got a go ahead for those.
See? I would get in touch with near.
And yeah, also, we have the Gen. AI Sig on day is that it's on Tuesdays at noon, eastern and sometimes near, can make it and usually discuss stuff like this. But yeah.
Keith Decker 00:23:41 So for for next steps for me, that would be just getting name resolution done with near, and then continue implementation of the instrumentation in this Pr. Or or where do I go from? Here?
Aaron Abbott 00:23:57 Oh, yeah, that sounds about right. Are you? Are you aware of, like the semantic conventions and kind of the difference between them in in our repo versus in the open elementary repo.
Keith Decker 00:24:07 A little bit. I I've been looking at those so.
Aaron Abbott 00:24:11 Okay, cool. Yeah, that's the main thing. I would definitely recommend coming to the Gen. A. Isig and kind of share that you're working on this.
We're. We're generally really interested. And I think there's a some other folks have have some proposals for moving things over, and we have kind of like a master spreadsheet for tracking this stuff. So yeah.
Keith Decker 00:24:32 Okay.
Riccardo Magliocchetti 00:24:44 Okay.
And so this was, thanks, Keith, and this was the last topic. So we should go back to the logs boards if you have time since we have time.
Aaron Abbott 00:24:59 I actually sorry I forgot to add it here, but I was hoping we could discuss. Hector's Pr. Also.
I'll I'll put it in the doc now.
Riccardo Magliocchetti 00:25:10 Thank you.
Aaron Abbott 00:25:12 This one sorry about that.
So I spent some time kind of reading through the the spec for logs.
and I think it's probably a bit closer.
Sorry.
It's probably a bit closer to trace than I initially realized. So I just wanted to raise some of that. Did you want to say something. Dylan.
not really. Okay. Okay. So sorry. So so the main thing is, there's kind of like this. Read, read, write, read, write, log record and readable log record, which is pretty similar to what's in the spec for trace. And I think the way we ended up implementing it for traces. We have Api spin.
which is what the instrumentations use, and they program against that Api.
And then there's a SDK span, and that one is kind of, I think, the equivalent of the read, write, span.
and then finally, there's something called readable span, which is the read-only one which gets passed to exporters, I think also, for for trace it gets passed to the on end in the span processor. That's a little bit different for logs.
And that that would be like something immutable, basically. So I I took a quick look at this Pr, and I think we renamed the log record to SDK log record. But we don't have anything quite. We don't have like this the distinction between the immutable one and the mutable one Spr. You want to split the SDK log record in 2 and or yeah, and have one that's readable and one that's readable and writable.
Yeah, just just because it's it's it's in the spec, but also it would match our tracing implementation. I'm trying to dig it up here.
I just put a a link in the meeting, doc to the part of the spec.
I don't know if you're around Hector, or you have any thoughts on that, otherwise I can. I can just leave some comments on the Pr. But I I kind of think maybe I've seen your name around. I feel like you've seen the tracing implementation.
Hector Hernandez 00:28:16 Yeah, I'm happy to make the changes. Just add the comments. And if every everyone agrees, and I just want to move this forward so. But it makes sense. I think Javascript have do the exact same thing right? They have this readable and a credible lock record. So, yeah.
I'm I mean in making these kind of changes.
Aaron Abbott 00:28:41 Okay. Great I was wondering, like, if you have a specific reason to do something different. That's I'm totally open to opinion. So I, if there was a discussion. Otherwise I can. Just yeah, I'll leave some comments on the Pr.
okay, great. Yeah, that. So that will. That will change the the export interface a little bit.
But I guess we're already making that change because we're renaming logs data in this Pr, anyway. So okay, I'll follow up offline, then thanks.
Hector Hernandez 00:29:16 One quick thing. Now that we're talking about this Pr, this Pr comes with really big breaking changes right?
we talked last time, like 2 weeks ago about having all together so we only break people at once. Is there like, do you guys use like some kind of branch? How do we want to do that? And how do we want to let customers know that this breaking changes are coming? I realize that python change log doesn't have this like icons, or anything that says this is breaking or not feature bug, fix, or anything like that. So I'm just wondering about what the what's the process that you guys have been doing before.
Aaron Abbott 00:30:07 Yeah, that's a good question. Honestly. So, just when we did metrics, we just made breaking changes because the the entire kind of development cycle only took maybe about a year. I would say, like we didn't have to have like, I feel like people have started depending on this because it's been around for at least 2 years, maybe almost 3 or something like that. So it'd be kind of kind of a new territory for us. I I would be open to a branch. But of course it's it's kind of tough, because you know, there's dependencies, and then you have to re rebase stuff. So
Hector Hernandez 00:30:45 Yeah, we can also coordinate right? Just merging at the same time. That's kind of things that's not a big deal. It's more about the breaking thing.
Aaron Abbott 00:30:54 So people are aware. At least we can just start doing this in the change lock right? I think it makes a good idea.
Hector Hernandez 00:31:01 Most other languages are doing that kind of things.
Aaron Abbott 00:31:07 Yeah, actually, imedio had, like a had a Pr to kind of overhaul our change log process.
It was using some tool.
But but I think it kind of stalled out. Maybe maybe it's my fault. I didn't take a look. But, Emilia, do you remember if that kind of made the change a lot more obvious when there was breaking changes.
Emídio 00:31:25 Yeah, I remember we we are using like, Tom Crowe is the name of the tool. We generate the change log from fragments.
But I would say, when we released some breaking chains, I was adding, like in caps, lock the wording breaking before the the message.
Aaron Abbott 00:31:50 Yeah.
Emídio 00:31:52 So.
Aaron Abbott 00:31:55 So we could also make this generate like a like, it's basically a template, I assume, so we could do something like add emojis to all breaking changes.
Maybe we could do that.
Emídio 00:32:05 Okay.
Aaron Abbott 00:32:06 Things change a lot, too. But.
Dan Gomez Blanco 00:32:10 Question on the the I guess the comment of you know, we'd rather have a big I can release with a lot of breaking changes then than others. You know that basically couldn't have that spread over time.
I'm not, I mean, is that the approach that was taken before Amazon? I'm not convinced. That's the the I mean, if I'm a user of a library, that's an alpha again, here is like we've got the talking about the logs SDK, and an Api, and that's an alpha.
Then wouldn't that be more preferable, I guess, to have like perhaps there's more breaking change.
But you can so like fix forward, because you know that you're using off it, you know, an off SDK, rather than like a bunch of them that you're going to have to go and address, otherwise you won't be able to upgrade like I'm not sure if you know I've got the right.
If I've caught the if I'm so convinced convinced that, you know, having a big one with a lot of breaking changes is better than another one, and the other approach.
Aaron Abbott 00:33:21 Yeah.
Dan Gomez Blanco 00:33:23 I mean, I don't know what people think. I'm not. Yeah.
Aaron Abbott 00:33:27 Yeah. No.
Dan Gomez Blanco 00:33:27 The other way.
Aaron Abbott 00:33:28 Yeah, I think we should have a discussion like like so one concern was just that it's kind of de facto stable like once we've had something sit around for long enough. People stop pretending that it's unstable, kind of like the collector, I guess. Right like.
Dan Gomez Blanco 00:33:44 Yeah, yeah.
Aaron Abbott 00:33:45 You know, people get very upset when there's breaking changes, even though it's technically mostly unstable. So but yeah, I mean, I'm sure there's definitely counterpoints like if if we did, you know, kind of like really regular releases, and only a couple of breaking changes per each one.
Maybe it would be less disruptive. But does any anybody else have any thoughts.
jeremy 00:34:10 I was. Gonna say, it's also like our our packages are all like tied one to one version wise and like.
So if someone were to like treat, this package is actually Alpha, that would basically mean that they would like probably like PIN a version or do something like that to avoid breaking changes, but that would mean they would have to do that to all of open telemetry as well.
And like that's just I I don't like I I don't think like any of our customers, at least are are doing that, like everyone is doing like a Tilde equals, which effectively means that they're all risking like a a log breaking change.
But because people can't like just just constrain logs while keeping other things more loose. Yeah, it's kind of effectively stable.
Dan Gomez Blanco 00:35:07 Yeah, makes sense.
Aaron Abbott 00:35:15 Yeah, does anybody else have thoughts on this? I think I definitely want to get this right and not.
you know, piss off as few people as possible if we can.
Riccardo Magliocchetti 00:35:28 I don't know, like I think we can maybe try to merge more breaking changes together as possible.
like, for example, like once we have. This logs. Pr ready manager, like we send the events deprecation together.
But yeah, like, I don't think we can target like to have just one release breaking stuff, but doing breaking changes.
and you know, and get it right in one shot like a bit, you know.
Don't have to break stuff later. And so like, I think, like like moving forward is better than like looking for a perfect solution.
So yeah, like, don't try to to not break like every release. But like we.
I guess, like, for people that want to be stable.
being able like to test some stuff, or at least adapt.
you know, being able to you to test the changes we introduce.
It's probably more beneficial than having, like, just one time to to require to to update stuff. So yeah, like to say, like, I want to be like outline, or just doing one brain chase. But title be as nice as possible to use a media.
Emídio 00:37:21 Yes, I agree with that, I would say like in the last release, we had some pressure to to release the protobuf. 6 support.
So people were pushing to have that that feature. But I would say, if you can have like more time for that, the next release. So we can review the Aprs and have more eyes on Fpr. To manage all of them together and introduce the big big change in the next release like A.
We can wait until the next release. That's what I'm proposing the set of.
I don't know when it it will be the next release in the next week since we agreed to have more monthly release, so maybe we can wait 2 or 3 weeks to release the next one.
Riccardo Magliocchetti 00:38:29 Yeah. But like, if you want to add to the change log, some preview of breaking changes, we should probably cater at least before.
Bring the baking changes right.
Emídio 00:38:44 Night.
Riccardo Magliocchetti 00:38:51 But yeah, like, I think that probably like we should revise this once we have the Ector Pr ready.
And also we have the head.
Dylan prs and stuff like that already. But Jeremy.
jeremy 00:39:09 Hey? I was. Gonna say, there's a lot of. There's a lot of little logging tasks remaining. Do we think pretty much? All of them are gonna be breaking changes, or just some of them, because, like we, there might be a much, because, like handling and creating and handling another branch.
It'd be really difficult, especially for like testing so I'm wondering if there's like a middle approach where we make all the we sort of identify all the changes that we don't think are going to be breaking changes. We do all those first, st and then only do the the last few at the end. Like at that point, we could basically get the same benefit of having them all together without like, nearly close to as much work developing this like other branch. But that only would make sense, if like. There's only a like a you know, a few of those tasks that we think are breaking. Hector, other people do. Do we think that those tasks are like almost all gonna be breaking? Or what do we think.
Hector Hernandez 00:40:10 I think I grabbed the the ones that are have the biggest changes right?
naming. But yeah, most of the other ones are more about changing some behavior, not doing a lot of Renames, so I don't expect all of them to be like this.
Oh.
Aaron suggested. We go through all the the board and see what we want to consider for stabilization. So maybe we can just look at at the actual issues. There.
jeremy 00:40:39 Yeah, that makes sense cool.
Riccardo Magliocchetti 00:41:05 Amelia, you read, you have your hands up.
Emídio 00:41:09 Cause I'm sick. Sorry.
Riccardo Magliocchetti 00:41:19 Okay, please double check The notes are added to the document are correct.
And so like, I'm not sure what was the the outcome of this discussion again.
Hmm.
Aaron Abbott 00:41:38 Yeah, I guess we can wait on it a little bit and decide. But you know, we can't read people's minds.
I think what Jeremy said is pretty a pretty good point like.
if we make people take manual action to do minor version upgrades just because they are using the experimental logs, you know. Api or SDK, I would. I feel like it would be easier to do it once, and it would be less annoying. But if it's a if it's a slow trickle of really small things of I don't know. Maybe they would be like, Oh, yeah, I'm using the I'm using this unstable thing. So just part for the course, it's it's pretty hard to say. Obviously, as a Maintainer, it's easier to just do things with no coordination.
But yeah, let's let's Let's think on it.
Riccardo Magliocchetti 00:42:42 Okay. So any other comments like, should should we take a look at the board, or we just do it offline.
Aaron Abbott 00:42:59 Yeah, maybe let's do like a like a 5 or 10 min time box, because I don't want to just make everybody do this.
Riccardo Magliocchetti 00:43:08 Good, so I don't know where to start like.
Aaron Abbott 00:43:15 Yes.
Riccardo Magliocchetti 00:43:18 Like.
Aaron Abbott 00:43:19 Maybe the in progress.
Riccardo Magliocchetti 00:43:21 Yeah.
okay, okay, this is open since September.
I don't think.
Aaron Abbott 00:43:39 Which is the actual Api right. This would just be the kind of auto this is auto instrumentation, behavior.
Riccardo Magliocchetti 00:43:46 Yeah.
Aaron Abbott 00:43:48 Maybe we could just add a label to them. Does that seem reasonable?
Or I guess we could just add a label to the ones that are breaking.
Riccardo Magliocchetti 00:44:01 Okay.
okay, the next one.
Okay. I don't think if this is related to the Api. But this may be breaking.
yeah, I don't remember the details.
but it's again, November 2024.
Okay?
Alright.
yeah. I don't think it's related to the Api. This is just like the implementation of the end or and this one, okay, this is the one that Hector is fixing.
As, so this one is big.
Okay, we don't tell.
Okay.
okay, this one.
And yeah, also, this one, of course, is breaking Chinese.
Aaron Abbott 00:45:55 So one of these Prs is just to add the deprecation warning.
and then, yeah, separate Pr is needed to actually like, remove the events. Api and SDK, and yeah.
Nope, I think to actually.
yeah, to actually deprecate and get rid of the events. Api and SDK, I need Hector's Pr to go in.
So.
Riccardo Magliocchetti 00:46:52 Okay.
Aaron Abbott 00:46:53 Yeah, probably need a separate release.
But that's okay, because it's well.
yeah, it's separate from logs. But yeah, we talked about wanting to group together. The breaking changes. So that's kinda yeah. It'll have to be a separate release, though. I think.
Riccardo Magliocchetti 00:47:18 Oh, shit.
Okay. But.
Aaron Abbott 00:47:27 Have at least 2 releases of breaking changes.
or, like this, 1st one would be advisory, and then we'd have a follow up that would actually remove it.
Right?
Yeah, that's I think that's good. As long as we have the Api, the Api changes done right. If the logs have to be ready. Yeah.
Riccardo Magliocchetti 00:47:52 Okay, so let's see what you having to do. Column. Now.
Aaron Abbott 00:48:03 Okay, yeah, Jeremy, what do you? What do you think of this bug? It's is, is everything like split into sub issues? And in the project board. Maybe we could close this one out.
jeremy 00:48:26 Which book? Oh, take a look! The one where I say, where I'm saying, take a look.
Aaron Abbott 00:48:30 Just to stabilize bug.
jeremy 00:48:35 Oh, you mean like the issue.
Aaron Abbott 00:48:36 Yeah. Like,
jeremy 00:48:37 Oh, oh, gotcha! Gotcha!
Aaron Abbott 00:48:38 Can we just put it all in this board instead.
like, it seems like most of these issues, are.
jeremy 00:48:43 Oh, I see what you're saying. Yeah, yeah, we can do that.
Well, I mean, like, yeah, I guess I mean, if if that's if that makes more sense to people.
Yeah, because I guess we yeah, we don't want to. Also just be constantly updating that issue that makes sense.
Aaron Abbott 00:49:01 Okay.
jeremy 00:49:01 Yeah, I can. I can close in favor of just like using the board.
Aaron Abbott 00:49:05 Okay. Sounds good. Thank you.
Riccardo Magliocchetti 00:49:07 Thank you.
Then we have, okay, this is about exporters.
So.
Aaron Abbott 00:49:19 I'm pretty sure I fixed this deadlock one.
I could not get the repro to work, so I'm not 100% sure. But I think that Pr fixed it.
Riccardo Magliocchetti 00:49:37 Okay, this is okay. The locker and log. Okay.
Aaron Abbott 00:49:41 All right.
Riccardo Magliocchetti 00:49:45 So this was like merge recently, right? This is not already in a release.
Aaron Abbott 00:49:51 Right. It's an unreleased merged changes, but it's not breaking.
Riccardo Magliocchetti 00:49:59 Okay.
So I don't know. Maybe we should close it. And if it happens again, just throw, you know.
Aaron Abbott 00:50:10 Yeah, that sounds good.
Riccardo Magliocchetti 00:50:12 Oh.
okay, okay, this is about, no. Okay.
Aaron Abbott 00:50:47 Yeah, I think, okay, every time I see the head of dates.
this is pretty much what Hector's Pr is doing right? I mean? It's not we. I guess we're taking a stance not to match the proto, and it's gonna look more like the the format that we use in the in the trace. SDK, but I think this one can be closed out in favor of that one if that's yeah. Like once Hector's Pr is merged, I think we could mark this one as fixed as fixed by it.
Riccardo Magliocchetti 00:51:19 But we can mark it as the duplicate of this one right.
Aaron Abbott 00:51:25 Sure, yeah, no, not not duplicate of that one.
Riccardo Magliocchetti 00:51:31 Ok, the one like this is like the change that you asked for the readable and writable right.
Aaron Abbott 00:51:42 Yeah, maybe maybe the bugs don't completely convey the the full story. I think this one was.
Hector Hernandez 00:51:49 Yeah, my other Pr is on the left is the one that says, yeah. The 3rd one, consider removing lock data and extending SDK, log record.
Aaron Abbott 00:52:02 Yeah. Let's go.
Hector Hernandez 00:52:02 This one is in progress, actually.
Riccardo Magliocchetti 00:52:07 Okay.
okay, so we should do it.
Okay?
And then what instrumentation? But again, not breaking changes. I hope.
Aaron Abbott 00:52:47 Great.
Well, there'll be one breaking change. I think we have a separate bug to move the the logging handler out of the SDK, so that would be the one breaking change. Then everything else would be in that instrumentation instead.
I don't know if that's in the board. If it's not. I'll pull it in.
Riccardo Magliocchetti 00:53:12 Okay, this is also about looking at the configuration.
Okay? But again, nothing related to Dpi changes.
And this is also configuration.
But, like again, not if you're related.
Okay, this may be another issue that has been fixed by Dylan.
Aaron Abbott 00:54:01 Yes, I have an open Pr to address this kind of yeah endless logging or recursive logging stuff.
Riccardo Magliocchetti 00:54:11 Okay, okay. They were filtering. Okay.
Aaron Abbott 00:54:14 Yeah.
Riccardo Magliocchetti 00:54:16 And so Lisa's movies, too, in progress.
Okay?
And super for autolog level.
Yeah.
Aaron Abbott 00:54:38 Right.
Yeah, I guess this one's not breaking. I don't. I don't know if we wanna do.
I don't know if it's actually in scope, though.
Riccardo Magliocchetti 00:54:47 Yeah, so we can skip this for now.
what kind of we have this question.
can you tackle a greater processes to the photologger provider.
Okay, this is, I think, a colleague of mine. So I probably should take a look.
Yeah.
Aaron Abbott 00:55:09 Yeah, I I mean, I don't think we're gonna do anything here. It's just I think the problem is just the Api doesn't know about spam processor, and there's nothing we could do about it.
Riccardo Magliocchetti 00:55:18 Yeah.
okay, I remember this one.
And yeah, still, not not related to Api.
This is about going into infinite loops, logging our own logging failures.
Okay, this one looks like more on topic.
Aaron Abbott 00:55:49 I think this is fixed by Hector's change. This one's about the the SDK, requiring you to use a SDK log record instead of the Api log record. So.
Riccardo Magliocchetti 00:56:04 Okay.
Aaron Abbott 00:56:10 Some.
Riccardo Magliocchetti 00:56:14 Maybe we should just add a reference to this in Ector Prs.
Aaron Abbott 00:56:19 Yep.
Riccardo Magliocchetti 00:56:24 And look at the.
Hector Hernandez 00:56:37 It was the other Pr.
Riccardo Magliocchetti 00:56:39 Okay, okay, so maybe it's no.
Hector Hernandez 00:56:47 This one, this one.
Riccardo Magliocchetti 00:57:09 Okay?
And so move into progress. This one, too.
Okay, this is more about.
okay. But we are you. We are attaching some attributes to our logs, but are not specified.
Aaron Abbott 00:57:33 Yeah, I think this is the logging handler again. So.
Riccardo Magliocchetti 00:57:36 Yeah.
So again, we can skip this.
Okay, this is again logging handler. And this is like the one, yeah.
Aaron Abbott 00:57:46 Yeah.
Riccardo Magliocchetti 00:57:50 And then we have.
Aaron Abbott 00:57:51 Instrumentation.
Riccardo Magliocchetti 00:57:53 In probably log instrumental.
But okay, oh, for shit.
I think this is just a clean up regarding code.
Aaron Abbott 00:58:13 This one's not needed, for we could probably remove it from the board.
He's just a contributor.
Riccardo Magliocchetti 00:58:20 Okay.
Aaron Abbott 00:58:21 Okay. I wish I think you have to hit the gear button. Maybe.
Riccardo Magliocchetti 00:58:38 is this delete from project? Right.
Aaron Abbott 00:58:42 It's a scary button. I don't know.
Riccardo Magliocchetti 00:58:43 Yes.
Aaron Abbott 00:58:47 I think that's right.
Riccardo Magliocchetti 00:58:49 What? Okay, this is scary.
I'll fix.
Aaron Abbott 00:58:56 You the one that's consider at consider removing logging handler out of SDK, can we mark that one as breaking it should this should kind of capture all the other ones, I guess, because once once it's moved out, it'll be.
you know, not part of the SDK as well.
Riccardo Magliocchetti 00:59:16 Yeah.
okay. And this is a think, something that was already fixed by Pablo, is this the same change?
Yeah, more or less.
So this may be a dupe.
Oh, this is the same change. What Pablo did to the SDK done today.
Aaron Abbott 01:00:09 Log installmentation.
Hmm.
In any event, we can remove it from the board right.
Riccardo Magliocchetti 01:00:20 Yeah.
Oh.
okay. So at least, we have like 6 items less. Yeah.
Aaron Abbott 01:00:38 Yeah. Now, now I'll go add a bunch after the meeting.
Riccardo Magliocchetti 01:00:41 Yeah.
Aaron Abbott 01:00:44 Alright. Well, thank you, everybody for sitting through that. I know that's not fun to do. But.
Riccardo Magliocchetti 01:00:48 That was helpful.
Okay, let's just like, go over time.
So yeah, thanks everyone.
I'll see you next week.
Aaron Abbott 01:01:03 Thank you all.
Hector Hernandez 01:01:04 Thank you.
Riccardo Magliocchetti 01:01:04 Bye.
Emídio 01:01:05 Thank you. Bye-bye.
