SIG: Go SIG
Date: 2026-09-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 01:19 Hey, Damien.
**Damien Mathieu** 01:26 Hey, good morning.
**Tyler Yahn (Splunk)** 01:28 Morning, how's it going?
**Damien Mathieu** 01:30 Good, how are you?
**David Ashpole (Google LLC)** 01:31 Good to see you. Is this your first SIG meeting back?
**Damien Mathieu** 01:34 Yes.
**David Ashpole (Google LLC)** 01:34 I think so, right? Awesome, welcome back.
**Damien Mathieu** 01:36 Thanks.
**Robert Pająk (Splunk Inc.)** 02:19 Hello? What's the crowd?
Nice to see you all.
**Tyler Yahn (Splunk)** 02:23 Hey.
**David Ashpole (Google LLC)** 02:23 Yeah, it's… it's a rave today.
**Robert Pająk (Splunk Inc.)** 02:26 Yeah.
**Tyler Yahn (Splunk)** 02:31 Yeah, I'm looking at the agenda, it doesn't look like there's too much, Robert, looks like you wanted to talk about, The next release, I see most people, if you haven't yet, I guess, go ahead and add your name to the attendees list.
Yeah, we could probably get started here. Actually, I think we probably are at a quorum. Robert, did you want to go ahead and start, sharing your screen, and we can talk about your item?
**Robert Pająk (Splunk Inc.)** 02:55 I will try.
Okay, add everyone to attend this list.
Let's see how custom will work for me.
Alright, so I think we are good to start creating a new release, and I just want to make sure that if there are any, you know… so this is, like, the milestone for the autogo, so is there any PR issues that you think should land as soon as possible, then just please add them to the milestone, because even if I start preparing the release, it will not happen, you know, in one day. So, I think you can just… unless you know right now If there's something missing here, anyone.
**Tyler Yahn (Splunk)** 03:40 Robert, I don't know if you are looking at the milestone, but we're seeing the Zoom meeting.
**Robert Pająk (Splunk Inc.)** 03:44 17.
Oh, that's… I clicked pause. Thanks. So, right now, you're seeing the correct screen, my real screen. So, right now, we have only one issue, which is release the version of the Lux API, which was, like, just double-check that we're actually released this table, which is really not… not any more work, if I remember correctly, I will double-check it.
But if there's any missing issue here, then… I do not speak now, or add it later to the milestone.
**Tyler Yahn (Splunk)** 04:17 So there's stuff in the Contrip Milestone, right?
**Robert Pająk (Splunk Inc.)** 04:20 Yep, indeed. And here… I'll probably ask.
Damien?
If these are things that… Maybe.
So, there is this resource detector, improved container ID, It's from you.
Puneet right?
**Puneet Singh** 04:42 Oh…
**Robert Pająk (Splunk Inc.)** 04:43 Yep.
Okay, I.
**Puneet Singh** 04:49 Yeah, so… Just a blocker.
**Robert Pająk (Splunk Inc.)** 04:51 Is it a blocker for the release? This is the first question.
**Puneet Singh** 04:54 No, I don't think so. I mean, this was… This is a follow-up, essentially, for both Docker as well as the container ID resource detector, but, yeah, yeah, it's not a blocker, essentially.
**Robert Pająk (Splunk Inc.)** 05:12 So I'll just put it to the next milestone. If you want, you can still, you know, try creating APR, it can land into the thing, just to make sure it's not a blocker. I'll just remove from this one.
Mom. Okay.
Let me refresh this view, and cross also other windows, taboo.
**David Ashpole (Google LLC)** 05:32 Remind me.
**Robert Pająk (Splunk Inc.)** 05:33 This is P.
**David Ashpole (Google LLC)** 05:33 this is the RC for logs, or is this the stable release? Stable.
**Robert Pająk (Splunk Inc.)** 05:38 stable.
**David Ashpole (Google LLC)** 05:39 Baby.
**Robert Pająk (Splunk Inc.)** 05:40 Predict signal. There you go.
**David Ashpole (Google LLC)** 05:44 No, it's good. I just… I can't keep track of things, so I know you do.
**Robert Pająk (Splunk Inc.)** 05:52 Next one is the client-initiated request termination for 500 response status error bug, which was opened July 25. I saw just before the meeting that the PR, still not, it's still not… it still has comments, and, even the latest comment from, David 3 years… sorry, not 3 years, 3 days ago, was not addressed at all. So, the question here is, one, the… I don't know, Damien is also with us. Is this something that you find Damien as a blocker? Because I think your default order of local HTTP, and this is something that you maybe want you to think about addressing maybe yourself, because it takes ages with other contributors.
**Damien Mathieu** 06:43 Frankly, I don't have an opinion. I just came back.
**Robert Pająk (Splunk Inc.)** 06:50 Okay, so maybe you can just, you know, take a look tomorrow? Yes, I can.
**Damien Mathieu** 06:55 Take it tomorrow.
**Robert Pająk (Splunk Inc.)** 06:56 Besides, I can also, you know, we can also have a chat what to do in our time, so it will be easier just to discuss this. And I think the same… the same is for AutoMax. Right now, AutoMax has also… I also checked that right now, AutoMax has no code owners.
And, they also need to probably create an issue for duplicating and removing it. Also, maybe check if there's maybe… maybe there's something else. I don't know, David, is some… is Oculus used anywhere in Kubernetes or anywhere? I don't know.
I don't think it's important.
**David Ashpole (Google LLC)** 07:27 which one? There's one of them that's used in Kubernetes. I think it's.
**Robert Pająk (Splunk Inc.)** 07:31 I think it was the rest of lunch.
**David Ashpole (Google LLC)** 07:33 Is it… oh, is it restful? Yeah, yeah, okay.
I could believe both are. But I remember at the RESTful, you guys made me step up as a code owner.
It's weird.
stepped up because Kubernetes needs it.
**Robert Pająk (Splunk Inc.)** 07:45 That's what I remember. I just want to make sure that it's not the same for, you know, for the other one.
I mean, you know, the config Azure Ethereum… Yes, you're in the auto arrest form.
**David Ashpole (Google LLC)** 07:57 Okay.
**Robert Pająk (Splunk Inc.)** 07:58 And this one has none.
**David Ashpole (Google LLC)** 08:01 I mean, I can check if Kubernetes needs it, and then you can… Put my name in there, but…
**Robert Pająk (Splunk Inc.)** 08:06 Okay.
Hmm.
And… And this is the end of our issues for this one, so we'll probably decide tomorrow if these are blockers or not.
Anyone wants to add something here?
**Puneet Singh** 08:22 I just wanted to ask about what's the cutoff date for the release? Is it September 20th?
No, that can't be.
Is it September 21st?
**Robert Pająk (Splunk Inc.)** 08:35 Probably, this is what I will aim, probably, September 21st. Is it some holidays, or some bad day, or…
**Puneet Singh** 08:43 Okay.
**Robert Pająk (Splunk Inc.)** 08:46 Okay.
Alright, so I'll stop sharing.
**Tyler Yahn (Splunk)** 08:56 I had a question, Robert, on that. What's the version that we're going to be releasing the logs? And this is just for the API, not the SDK, right?
**Robert Pająk (Splunk Inc.)** 09:03 Both.
**Tyler Yahn (Splunk)** 09:05 We have them both at the same time. Okay, what are the versioning? What's the versions we're gonna do for both?
**Robert Pająk (Splunk Inc.)** 09:09 I thought about using the same versions as for metrics and traces.
**Tyler Yahn (Splunk)** 09:14 Cool, yeah, that's what I would do as well. Okay.
**Robert Pająk (Splunk Inc.)** 09:16 It will be in the release… it will be in the release anyway, so… We'll have to review it and double-check.
**Tyler Yahn (Splunk)** 09:23 Yeah, I would just… yeah, I just wanted to make sure, while we're synchronously discussing it, but that sounds like, I think, the plan I would have, so yeah, that sounds good.
Cool, alright.
Yeah, that's super exciting.
we're definitely gonna have something to announce at KubeCon, which, Yeah, I'm… I'm pumped about. That's… that's great.
**Robert Pająk (Splunk Inc.)** 09:46 I was also.
about making the OTLP exporter stable, but I just didn't want to put too much on the plate, just to be sure. I also do not remember if we… I don't remember if for metrics we had RC for OTLP exporters, right? We just went, I think, directly.
Stable.
**David Ashpole (Google LLC)** 10:06 I could see an RC for them, just so that if we do wanna… like, day before KubeCon, make it stable or something, we have that, but…
**Robert Pająk (Splunk Inc.)** 10:15 Yep.
**David Ashpole (Google LLC)** 10:16 I mean, I guess there's still plenty of time, regardless.
**Tyler Yahn (Splunk)** 10:22 Yeah, I definitely think that… we do think OTLP is pretty important, right? Because that's, like, the lingo franca of, open some industry, so, like, we want to do that, but we don't have any other log exporters, right?
**Robert Pająk (Splunk Inc.)** 10:34 This is the outs.
**Tyler Yahn (Splunk)** 10:36 Yeah, yeah, sorry, yeah. Okay.
Yeah, I mean, I think… I would probably break them up, just to reduce the complexity. I don't know if it's actually been reviewed, the OTLP one, as much, so maybe the RC makes a lot of sense, so… Yeah, I would probably wait on that, and then we also would probably want to look at the logs bridges stuff as well, and maybe we can even get that out before KubeCon? That'd be really cool. So yeah, I mean, I think there's… there's still some work, but, like, this is just a huge milestone, so, like, the other stuff is… You know, definitely icing on the cake, for sure.
Awesome. Yeah, great work.
Cool.
With that, that's the end of the written agenda. Any other… I'm guessing there's other things people are working on, obviously, but, like, anything else people wanted to talk about?
**David Ashpole (Google LLC)** 11:33 I don't think so. I don't think I've seen… Are there any open discussions we need to have for, either… you got your PR merged for the initial… like, Finnish implementation, right?
**Tyler Yahn (Splunk)** 11:52 Yeah.
**David Ashpole (Google LLC)** 11:53 We…
**Tyler Yahn (Splunk)** 11:54 Question.
**David Ashpole (Google LLC)** 11:54 We're still waiting on… or we still need someone to implement the Bind API, right? The API exists, but there's no implementations.
**Tyler Yahn (Splunk)** 12:04 Yeah, correct. The Bines stuff is just implementation right now, like… or, sorry, like, it's just an API, yeah, that you can technically have, but… Yeah, I, I… I… I totally… space, I've been deep in, The… Obi-World, but yeah, the canonical, attribute identity, I guess that, actually, maybe we could talk about that. It looks like… There has been some feedback that I did not get back to, from Damien yesterday. Maybe I can take a look at this really quick.
Start sharing my screen.
**David Ashpole (Google LLC)** 12:46 Sorry, I didn't mean to put you on the spot, I just figured we've had…
**Tyler Yahn (Splunk)** 12:50 No, no, it's good.
**David Ashpole (Google LLC)** 12:51 We mostly talk about this stuff.
**Tyler Yahn (Splunk)** 12:53 Yeah, right? No, definitely. So… Yeah, this is… this is true. We are gonna order, go through these twice. The idea is that, like, we try to do this in, the fast path being that, like.
Any happy path, we don't do that twice, If you can explain to me how to do this not twice, I'm happy to update this, but you are gonna have… At some point, you're going to have to degrade performance, so, like, this is,
**Damien Mathieu** 13:24 Yeah, yeah, I'm…
**Tyler Yahn (Splunk)** 13:25 I don't know how you would do that subtle.
**Damien Mathieu** 13:27 I have a specific solution, I just wanted to point it out, I guess.
**Tyler Yahn (Splunk)** 13:34 Yeah, I mean, it was, it was definitely understood, and that's why this try unfiltered distinct, exists.
Because it was already doing that beforehand, but, like, if you are passing it something that is literally in the form that it needs, and it's already… the only thing that it does is if there's any, like, duplication, it'll… it'll still preserve that, even at a single pass. So, like, this is a pretty… You know, happy path, but, like.
Otherwise, like, once you have proven that it is not something that you can actually do in one single pass, like, you kind of have to do multiple passes at this point, because you're doing a sort, at that point, or you're verifying if you have to do a sort or not.
It is not, it's still order… N, right? It's not n log n at that point.
N log n comes up after this, when we do a sort on the stack.
But, yeah, this is still just, like, a two… you know, a multiplicative factor of how many it's going through. The other ones are a little bit more distinct. And then, obviously, like, the last one, when we're actually allocating is going to be way more. Yeah.
trying to do this the same… it's actually not the exact same logic. There are very, subtle differences here, specifically around, like, the exit cases, so that's not, it's not actually something we could do. I did look into this, it's not something, that we can try to… Resolve.
But I can respond a little further into the PR,
**Damien Mathieu** 15:00 Yeah, and, I mean, Those are… I don't think those are blocking either, so I can approve.
**Tyler Yahn (Splunk)** 15:05 Okay.
Yeah, and so… Another thing to keep in mind is that this isn't really, like.
The final form, Yeah, like, I do want to keep in mind, I do want to think about benchmarking, obviously, like, it's definitely important, because this is going to be something that's used on the FastPath, but, It also is for the experimental feature, just for, you know, context for folks that are maybe listening to this as well, like, this isn't, I think, ultimately where we want this to live, in this add-onorm package, this is an internal package. If… we can get this final, API to actually stabilize, then we would probably move this to the attributes package.
So, at that point, I think that's where we could also look at a lot more, further optimizations.
This is, like, I don't know. It's probably pretty over-optimized at this point, for what we're trying to do, but I… I've worked with attributes so long that it's hard to just not do some of these things that, you know, we've done in other places, so I just have done them. But, yeah, like, further iteration on this is definitely, welcome after this is merged as well, so, like, there's definitely not, I think, the finish line being here.
But that being said, like, this is split off from a larger PR, where, we started to get into, like, the thousand line, range, but this is kind of like the meat and potatoes that I'm actually trying to get merged over here, which is the actual implementation that we're gonna… hook in the finished counter for the N64 counter. But yeah, this is just kind of breaking that off.
yeah.
Important in case folks also missed it, this does introduce an interesting, like, version incompatibility thing, where… like, if we do introduce a behavior change into, like, our set filter, or our set construction of a distinct, like, for some reason we switch to first value wins instead of last value wins, which I don't think we'd ever do, but, like, just say we did that, like.
an upgrade would mean that we have incompatible implementations of this, so that's why I ultimately want this to live in the attribute package, that we have, like, a single implementation for some, like, canonical representation here, but, like.
I think for the experimental prototype phase of this, like, that seemed reasonable, so that was the trade-off that I made there. But yeah, just… A lot of thought went into this PR, that's kind of just getting washed over.
So, maybe I'll spare you all and just keep moving on that one. But yeah.
Definitely some eyes on that, it'd be great. I do want to get that further push, that's something that OBE could definitely start to adopt, which I'm super excited about.
For, like, a whole host of reasons, But yeah, that'd be really cool. And then, yeah.
**Robert Pająk (Splunk Inc.)** 17:42 Alert.
**Tyler Yahn (Splunk)** 17:42 David, I… yeah, go ahead.
**Robert Pająk (Splunk Inc.)** 17:44 Would you want to add it to the milestone? So you can… No, it's not…
**Tyler Yahn (Splunk)** 17:47 It's not blocking.
And it's one of those things where it's like, both of those PRs don't actually I'm, like, 90% sure the second PR also doesn't add an option yet to, like, the public interface, so, like, anything that merges doesn't actually get accepted.
**Robert Pająk (Splunk Inc.)** 18:05 feasible.
**Tyler Yahn (Splunk)** 18:05 end user. Yeah, yeah, so it's not, it's not really, like, yeah, timing critical to get something in or out. Yeah, but… But it will be soon, and then it can just kind of be like what we did with the metric stuff, where, you know, one, you know, will break off by aggregation. It'll actually, I think, go a lot faster once we get the first, like, steel thread through all the way through, so, yeah.
But yeah, that's, that's where it's at.
David, did you want help on the Bind stuff? I just kind of have been doing the finished stuff based on.
**David Ashpole (Google LLC)** 18:35 I think we both had prototypes up. I wasn't sure if you wanted to try and land yours, because you were gonna, like… do some big SDK refactors, or if you… Or if you wanted to imp… do you feel like we've settled on the question of whether we should implement it in the current aggregators, or do the weird… or, I won't say weird, do the split where we have the SDK However you were going to reorganize the SDK and pipeline so that it could live separately.
**Tyler Yahn (Splunk)** 19:11 Yeah, right now, the way that I'm doing the finished stuff is a separate implementation, where there is, like, this experimental, tracer provider that kind of wraps the existing tracer… I'm sorry, not tracer… meter, Meter provider stuff, and it will, will, like, kind of, like.
do things on top of it. So, it's not a separate it doesn't do a full implementation of the meter provider or the meter. It literally is just… yeah, but it's more of an extension, and I think that's the way that I would continue wanting to do that, just so that it isolates, so that, you know, the fast path of people having, you know, enabled experimental features are literally not touched.
**David Ashpole (Google LLC)** 19:51 Yep.
**Tyler Yahn (Splunk)** 19:52 So yeah, I would go that route. I mean, that's a good point. Maybe we try to land this next PR that I have lined up, which does introduce that experimental meter provider, and then we can start to add in the buying stuff. I think that maybe that's a good way to do it.
**David Ashpole (Google LLC)** 20:07 I'm still… I haven't had time to dig into your prototype, so if that's the next step, then I can,
**Tyler Yahn (Splunk)** 20:14 Yeah.
**David Ashpole (Google LLC)** 20:15 I can do that.
**Tyler Yahn (Splunk)** 20:15 Trying to make it, like, smaller, but yeah.
**David Ashpole (Google LLC)** 20:18 Yeah, I… I like… I like what you did with Finnish, how it's kind of a… an add-on with stuff that's clearly… it's delineated, but it's not, like, in different packages, and it doesn't… Have a lot of duplication, so… I… I'm… tempted to take a stab at trying to do something more akin to that than the whole, like, full meter provider split, but if… If that sounds good, then I'll just move forward with that approach. Otherwise, I can take a look at your prototype that you did, and see if… See what I, like… Yeah, I haven't taken a deep look, you know, even just the lines of code makes me a little, like, about it, but… I don't know if there's…
**Tyler Yahn (Splunk)** 21:06 Yeah.
**David Ashpole (Google LLC)** 21:06 There's no, like, perfect answer, and it's just experimental stuff, right? So, on the one hand, like, maybe it's okay to duplicate a lot of things.
**Tyler Yahn (Splunk)** 21:14 That, like, pipeline code is just… every time I get into it, it's super… like, I'm just like, what does this even represent? But, yeah.
It's… it's, I understand the hesitation. It's not an easy code. So, yeah, I… I think… I might say just, like, wait until we get to that other PR. In fact, I might even split that other PR again, just to try to, like, isolate that pipeline refactor stuff, because, like, that's… we're… there's a lot of complication there.
So, yeah, maybe we just wait on that stuff, then.
Yeah, this… PR for the attribute stuff, I think, is probably the easiest step to review, just because everyone's familiar with attributes, but yeah.
**David Ashpole (Google LLC)** 21:57 Yeah, I do wonder if we're gonna end up with… and this is not a bad thing, right? Like… Like, 6 different internal implementations of, like, Hashing in different ways.
**Tyler Yahn (Splunk)** 22:07 Yeah.
**David Ashpole (Google LLC)** 22:08 Different uses, like, that's kind of where we've been trending, and… they're pretty performant, so it's actually not a bad thing, and I'm kind of glad they're not in the attributes package itself. I think that, like.
Hasher thing that we added is hopefully gonna be powerful enough.
But yeah, maybe…
**Tyler Yahn (Splunk)** 22:27 again.
**David Ashpole (Google LLC)** 22:27 I think we can…
**Tyler Yahn (Splunk)** 22:28 Still it.
Yeah, like, I do want to canonicalize it, like, once… because, like, the other thing is, is I think that you're hashing… Because you actually need the full set eventually, so, like, there is a tied coupling with the hash to the set, so, like, that doesn't exist in the finish. So, like, yeah, I actually need, like, a secondary intermediary to, like, what's there. So, like, I think that we do eventually need to update the AshDes package, because… Because, again, like, it comes back to that, like, you know, we have 6 different implementations with the hashing, like, what happens when there's drift? Like, oh, we catch a bug in one location, like, and it doesn't get fixed in the others, like, that could be very problematic. Not because, like.
Well, okay, let's say we catch it in one area, we update it in all the other areas. Like, if somebody doesn't do an upgrade on all of the different modules, then that actually causes drift in itself, right? Like, it has nothing to do with what we're doing, it's more about, like, end-user behavior, so… like, I think we want to trend towards unifying everything in the attributes package, but I also, like, do not want to be putting stable API into the attributes package for experimental features like this. Like, that's… That's what got us to having the set in the attribute package, which is… still one of my greatest regrets for this project. Yeah, like, I think that that's, like, something we can work on as it comes up, yeah.
Awesome. Alright, yeah, thanks for reminding me about that. I will take a look at this, folks on the call, if you want to take a look at that, canonical asteroid identity, and then I will try to get the wire experimental, N64 counter finish stuff out after that.
Other than that…
**David Ashpole (Google LLC)** 24:05 does not use OTelMux, so I won't be… Roped into it this time. Sorry.
**Tyler Yahn (Splunk)** 24:13 Yeah, I kind of feel like… Hotel Mux.
doesn't have hotel input integration yet?
That's kind of surprising, like… I don't know.
I kind of wonder also if we can use some of those, like.
instrumentation tools that, like, auto-instrument things and try to help build the instrumentation, but, Yeah, I don't know. It'd be cool if we could get some… some things moved into those projects.
I think it's one of those things that nobody's really excited to have transportation accepted if we're just gonna drop it and then leave it, for the same reason we aren't excited to have it, so, yeah.
Okay, cool. Any other topics folks want?
Still have a little bit of time, quite a bit of time.
**Puneet Singh** 25:01 I just wanted to ask that, you know, is it, like, a common practice that if you don't have any owners for a component, that Eventually being considered for dropping from the instrumentation.
**Tyler Yahn (Splunk)** 25:12 Yeah, you can go look at the docs for the transportation, package itself, top-level transportation. We document this pretty clearly. Without any ownership, like, we don't… We don't own it. So, like, and we also don't lie to our users saying that, like, it's supported pieces of code, just because it isn't. And so, yeah. Like, they can always use an archive version, but, like, we don't provide forward support if we don't have an owner, yeah.
**Puneet Singh** 25:36 I mean, because that could be very different from the adoption, but it's… Primarily towards the ownership, that if it doesn't have owner, irrespective of the adoption, it won't be supported.
**Tyler Yahn (Splunk)** 25:47 Yeah, correct.
**Puneet Singh** 25:48 Okay, okay.
**Tyler Yahn (Splunk)** 25:50 Yeah, and usually that's, like, the case is, if you have a lot of adoption, there's a pretty good chance that when you come across with an issue saying that this is going to be deprecated, or when you actually go through the deprecation process, somebody comes in and goes, like, fine, I will… I will step up and own this.
But if that's not the case, like… that's just reality, right? Like, if nobody… if literally nobody wants to step up and own it, then… then it literally becomes unowned, and we'll remove it, yeah.
**Puneet Singh** 26:17 Yeah, in a way, it's correlated, actually, that if something is being adopted, then it will get some support, actually. Yeah. All right.
**Tyler Yahn (Splunk)** 26:25 Or, if it's in some mission-critical thing like Kubernetes, then you get people like David that are gonna step up. So, yeah.
**Puneet Singh** 26:32 Okay.
**David Ashpole (Google LLC)** 26:34 Users are the best owners.
**Tyler Yahn (Splunk)** 26:38 It is true. It is true.
Well, cool. Alright, yeah, we could probably end the meeting early here. Thanks, everyone, for joining. We will see you all in a week's time, or asynchronously. Until then.
Bye.
