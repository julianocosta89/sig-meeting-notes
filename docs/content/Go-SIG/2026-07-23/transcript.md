SIG: Go SIG
Date: 2026-07-23
Duration: 47 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 01:14 Hey.
**Puneet Singh** 01:18 Hello?
**Tyler** 01:20 How's it going?
**Puneet Singh** 01:23 Pretty good, actually. The weather has been somewhat decent today.
**Tyler** 01:28 Oh, yeah? Where are you based out of?
**Puneet Singh** 01:30 I'm in India.
So usually the temperature's around 38, 39, but… Yeah, it's, it's, like, 32, 33, so yeah, relatively that's… Yeah.
**Tyler** 01:43 Yeah.
Are you, are you southern India, or…
**Puneet Singh** 01:46 No, northern.
**Tyler** 01:47 Oh, okay, alright, still, yeah, wow.
Yeah, 38.39 sounds like my worst nightmare, so, yeah.
Yeah, couldn't do that.
I see David. David's back.
**David Ashpole** 02:03 Yep, I'm back.
**Tyler** 02:05 Vacation?
**David Ashpole** 02:07 Yeah, it was nice, it was nice.
**Tyler** 02:09 Oh, nice. Yeah.
Did you do a staycation, or did you go somewhere fun?
**David Ashpole** 02:13 We went up to Maine, it was nice.
**Tyler** 02:16 Oh, it's like that.
Yeah, no, sounds like a lot of fun.
Did you get out any water bodies, or, you just hang out on land? No.
**David Ashpole** 02:25 Oh, just hung out on land. Yeah.
**Tyler** 02:27 Duh.
**David Ashpole** 02:28 there were a couple opportunities to do, like, you know, a ferry. Actually.
I did… we did have a dinner on a restaurant boat, so I guess that counts.
**Tyler** 02:38 I never left.
**David Ashpole** 02:39 the dock.
**Tyler** 02:40 I'm pretty sure you're a salty captain at this point, based on that, so, yeah.
Yeah, that sounds cool.
Yeah, all the lakes up there are just phenomenal. I love… Little pond… well, ponds sometimes, but yeah.
**David Ashpole** 02:56 a lot.
**Tyler** 02:56 fun.
That's cool.
Well, cool. Let's see, we're a few minutes in. If, you have not yet, which includes me, added your name to the attendees list, go ahead and do that, and if you have agenda items you wanted to talk about… Please go ahead and do that as well. And then, you know, we'll probably wait just a little bit.
I don't know if Robert's, able to make it.
I guess I don't have it on this. But we can wait just a little bit longer.
Yeah, I think that might be working again.
You can all see my screen, right?
**David Ashpole** 04:03 Yep.
**Tyler** 04:05 Alright, it's not just a black. Okay, cool.
Well, cool. Yeah, let's, let's jump in here. So, awesome. Welcome everybody.
I think I wanted to start this off by just talking about, this next milestone. We're pretty overdue for, another release.
So, I wanted to go through and just see what's going on. There's definitely, I think this is a blocker for us, so start us off here.
One of these, it just looks like it… looks like it's ready to go. I don't know if there's any other folks on the call that wanted to give this a review, otherwise I'll plan on merging this later on today. I was asking… Yep.
**David Ashpole** 04:52 Have we thrown Copilot at it yet? Why don't you request that review? I…
**Tyler** 04:56 I think Robert…
**David Ashpole** 04:57 Or did Robin.
**Tyler** 04:58 Tried… Yeah, he might have been out of credits, I think, actually.
Somewhere in here. No, yeah, I think he… I think he might have been out of credits at this point. So, yeah, Yeah, if you want to click the button to…
**David Ashpole** 05:16 Is it…
**Tyler** 05:16 I don't yeah, I mean, it's whatever GitHub account you have,
**David Ashpole** 05:23 Oh, interesting.
**Tyler** 05:23 Oh, here you go. I can just do it myself. Alright, yeah.
Yeah, I mean, you get, like, a bunch of free… tier stuff, so… yeah.
I think that that should work.
Yeah.
**David Ashpole** 05:36 For some reason, I thought our… like, Open Telemetry itself had the credits.
I guess…
**Tyler** 05:44 It does… I don't know how to use them. I would like to know how to use them, if that's the case. I think… I mean, I feel like it might, But, yeah, I don't know. I do know that, like.
There's also some severe limitations, which we're not running into. I think it's something like, 10,000 lines is the max number of changes, ask me how I know. So, yeah, there's, like, definitely some hard limits, I think, with the free accounts that, like.
cause some frustration, so if we could get, I think the hotel one, but… But yeah, I… kick that off.
We'll see how it goes. Otherwise, yeah.
Wait on that one.
**David Ashpole** 06:25 I was gonna do a review, but, it already has two approvals, so, Don't block on me. I'm sure there's also other things that need review.
**Tyler** 06:36 Yeah, speaking of that, So, here's a few PRs, that need some review.
Include forced flush in built-in processor shutdown? I thought I reviewed this, Maybe I just took a look at it, but this also is needing review, Yeah, so this is, I think, a cleanup where… The built-in for the logging, edges, like, the force flush.
was not being called when shutdown was happening, so there was just stale logs, if I remember correctly. So, this should be pretty straightforward. I think when I originally looked at it, it was… had some concurrency issues, but, Robert… I think went down a rabbit hole and has addressed them in here, so, yeah, I think this looks ready to go.
Next up is also a Robert P.R, consolidate the attribute normalization in the adder norm. This is added to the milestone, I don't know if it's strictly required, but, it's there. I know, it has already, one review, so yeah, thanks, Puneet, for that.
This just needs, I think, more… more ease.
**David Ashpole** 07:45 Good.
**Tyler** 07:55 Let's see… next one, optimizing the batch process using SIG pool for buffer. Again, also, this is in the milestone.
This.
has a co-pilot review, and Robert's reviewed, but I don't think that there's anything beyond that. I think it… this had a few rounds of feedback.
Yeah, it does look outdated at this point, so… Looks like Robert actually has already reviewed it. He says that maybe this isn't worth including.
**David Ashpole** 08:30 I think we need a new benchmark.
Or.
**Tyler** 08:35 Yeah, it does look like that.
**David Ashpole** 08:36 Okay.
**Tyler** 08:37 Close this thing.
Yeah, I think it's just a new benchmark, it's actually what he's calling for here.
Yeah, let's see…
**David Ashpole** 08:53 I would consider booting this from the milestone. I don't feel like we're… I don't feel like it's… Likely to be a big enough… change that I would hold anything for it.
**Tyler** 09:06 Sounds good.
**David Ashpole** 09:06 But I'm also happy if it's included.
**Tyler** 09:09 Yeah, I thought it was closer than it is. I didn't add it here, but I agree. Let's just move it to the next milestone, and let's not block on this.
Yeah. I mean, I'd rather get the… The milestone completed.
Okay, and then the last one I identified, was something from Robert this morning, where the new SUMCOM package, another new SumCount package has come out, and this has been updated, this is just missing another, review from… A maintainer. Or approver, actually.
I don't know if there's a difference in that anymore, but otherwise, yeah, this, I think, this is definitely one we want to get in.
Okay, also in this, though, I wanted to bring up some of these That are included, that maybe we want to drop.
This is configuring response body size limits. Robert's blocked this. I haven't taken a look at this in… weeks, so I don't know actually where this is at.
But yeah, I don't know if this should be a blocker for, mmm… Just kind of hoping Robert was here so I could find out what was going on here, but I guess he's not. I'm gonna pull this out of the milestone, unless there's opposition to doing that.
I guess, Robert, if you're… Watching this, you could also fix it afterwards.
That's not what I wanted.
Okay.
**David Ashpole** 10:58 Yep.
**Tyler** 10:59 And then, there's still a few more issues in the milestones, I don't know if we wanted to just move these forward.
So, the, export of Prometheus, migration to the new configuration options, I… I don't know where we're at on this one.
**David Ashpole** 11:21 I don't remember. I'd have to look at this. Just kick it out of the milestone for now.
**Tyler** 11:26 I… I feel like… Yeah, we could do that. Like, I feel like this just needs to get closed, like, this is… I feel like… Almost up to 2.
**David Ashpole** 11:35 That's a bit.
**Tyler** 11:36 full year… yeah, even if it's just, like, another tracking issue after the fact, but, like…
**David Ashpole** 11:44 We do have the new config options. I think the question has been, like, do we want to deprecate the old ones? But honestly, that belongs in the spec.
We both.
Like, a tracking issue for… If we want to remove the old ones.
**Tyler** 11:57 Yeah.
Yeah, I mean, at this point, like, it's also been… If we had deprecated them, it would have been, like, more than 6 months.
So, like, I don't know, like, maybe it's just worth keeping them now that, like, it's just… it's been there for so long, but… Okay, I'll move this, I don't know what we're gonna do here, but let's maybe on the next milestone, not just keep moving it down the road, and we'll try to close it or do something, even if it's just, like, creating a tracking issue in the spec to follow this. Right now, like, this is not gonna help the spec right here, so… Okay, and then, kind of similarly here, this is… close to being done. I don't know if it's gonna get done, this one.
There's only one more issue… that has a PR.
David is, reviewed. This actually should have been in the list of things, I think, that needed… to get reviewed. Yeah, let me… let me add this, actually.
It'd be nice to close this.
**David Ashpole** 13:12 This is a lot of fun, right?
**Tyler** 13:14 Yeah, it's the last one, so… Yeah, let me… let me take a look at this after this call. So this is just looking for more reviews at this point.
Yeah, it looks like CI's passing, so… yeah, okay. I think this actually may be worth… getting in this, because I think we could probably get this done, so… Yeah, let me add this.
Okay.
Awesome.
Okay, that's what I have identified for the next milestone. I think that, like, that's a pretty good triage. I'm hoping to get this out sooner rather than later. It's been delayed for about a month now.
So, I guess I'll also try to sync with Robert and see if, like, there's things that I missed here, but yeah, let's try to… let's try to move this forward.
Okay, next up, also wanted to check in on the 2026 goals, coming up on the last third of the year here.
So, we have a bunch of issues tracking this, it's not really a project board.
How do you do… Yeah, let's do that.
So the logs API, I know… Robert, I thought this was way closer than 2 out of 9.
Is it just, like, a bunch of…
**David Ashpole** 14:33 audit tasks.
**Tyler** 14:33 Oh, okay, yeah, yeah, okay, yeah.
Good.
definitely just audits, it looks like. But it also is kind of blocked on this release, because we need to migrate over the attributes package before we're really able to, I think, say that we're… we're auditable. So, yeah, I think that this is… this is a next milestone. Let me actually put this in the next milestone.
Let's get aspirational here.
Yeah, but I mean, I think this should be… I'd love… I'd love if we could get this done before November. I don't see why not. Like, this seems like we're pretty much there.
modulo some, like, features that maybe are being actively developed in the spec, so, like, let's try to… let's try to get this done.
Release 1.0 of the exporter Prometheus. I know this has been blocked on quite a few things, mostly on the spec, I'm guessing. I don't know if you have any update on this one, David.
**David Ashpole** 15:28 Not recently, no. We're…
**Tyler** 15:30 Yeah.
**David Ashpole** 15:31 We're deep in some random discussion about things that aren't particularly relevant to SDK Express.
**Tyler** 15:36 orders.
Okay.
Yeah. Yeah, I don't think this is as… burning, as a priority, but I do think it'd be great to get it done, but obviously… We don't control a lot of the blocking issues here, so… understandably.
Optimized Metrics SDK, this is a good question as to where we're at here.
It's a little bit of an open-ended issue, but… We got a lot in here. It looks like everything's done.
Except for this new set, stuff.
**David Ashpole** 16:10 Yep.
**Tyler** 16:12 how about… how much more?
I think the sync map exponential histogram maybe…
**David Ashpole** 16:23 But there's two… I think there's two reviewable ones right now. One is the sync map for exponential histograms.
the… And then the other one is… the filtered attributes?
I actually, if you want to click on that, I'm… I'm pretty pleased with If you remember, there was… I was gonna add some really ugly function that returned a bitmap.
And I'm kind of glad we didn't do that.
The proposal here is actually to make some of the hasher functions public that we have, so that we can actually do the hashing from within the metrics SDK and keep all of the, like.
bitmap nonsense internal there. And now that I've written this, like, it feels way more, Like, ergonomic and correct than any of the previous iterations.
it isn't…
**Tyler** 17:19 Okay.
**David Ashpole** 17:20 It isn't quite as fast.
I forget why it… I couldn't tell if it actually is as fast, but the benchmark was buggy last time, but… Yeah, I think this is probably the solution I'm happiest with.
I guess it's good that I took 2 months to figure it out.
**Tyler** 17:48 Yeah, that's just sometimes how that works.
I'm gonna add this to the next milestone so we don't lose track of it, but I also add this to my list of things to review. Like, yeah, this has just slipped through my… leaky bucket of reviews. Yeah, it's been on my agenda. But, okay, cool, yeah, this actually looks great. I love this idea. Like you're saying, I think this looks really ergonomic. It also provides, like, primitives for what we're trying to accomplish and doing internally, so… Yeah, that sounds good.
**David Ashpole** 18:20 Hitler wouldn't.
**Tyler** 18:21 one.
**David Ashpole** 18:22 Yeah, the exponential histogram one… oh yeah, I forgot there's the histogram reservoir.
Which is also… Like, good to do.
**Tyler** 18:35 Do you want me to pull that one up, or this one?
**David Ashpole** 18:38 both into the next… I mean, I think they're all ready for review. It's…
**Tyler** 18:43 Yeah, yeah, I meant, sorry, just talking about it, but Include this in the… Issue as well.
**David Ashpole** 18:52 Yep.
And then after those, There is the… so, I added the API for with unsafe attributes at one point.
And… I'm considering focusing on bound instruments instead.
And trying to push that forward.
It exists as an API surface and works, but it's not optimized.
And… Yeah, I'm not… I'm not sure if you have thoughts on which… if we should do one or the other, or both.
**Tyler** 19:22 I think I prefer the bound stuff, especially if there's a concerted push in the spec to try to support it.
That would be my preference.
I remember we were looking at both.
We thought that maybe there'd be use cases for Either of them, but… No, I think I… I think I'd rather just go with that, the bounds, approach.
Personally.
**David Ashpole** 19:50 Okay, yeah, I… that was what I was going to do as well. So I have been working on the bound instrument one, Part of it's, like, figuring out what the right… Interfaces are.
And, like, Yeah, trying to encapsulate the… the whole, like… Cardinality tracking outside of… Collection piece,
**Tyler** 20:13 Yeah.
**David Ashpole** 20:14 I posted a little… Thing here, just on, like, why it's… why it's been a lot harder.
Which is maybe interesting.
I, you know… I'm not sure if I should go back to the spec and say, like, hey… But interestingly, I… I assume that Java and Rust must have just not had this issue, but they do, and it has made their implementations also very complex. So… Like, maybe it's just that actually the behavior that is specified there is actually something that… the other… Languages really, really want.
**Tyler** 20:53 Oh, I see.
Yeah.
That's a good question. I mean, I mean, I think it's worth asking, at least, at the speed level.
**David Ashpole** 21:09 ask, but I think I'm close to a point where… I'll be able to open this up for review, maybe another week. We'll see.
**Tyler** 21:16 Okay.
Yeah, that sounds good. Perfect.
Okay, cool. I added this here.
I think that means… Sorry, go ahead.
**David Ashpole** 21:29 Nope, nope.
**Tyler** 21:31 Okay.
That means I think this is, I don't know what's going on here.
**David Ashpole** 21:39 So this is… Solved by either bound instruments, or… by… well, so… the issue doesn't… And it's like a lazy…
**Tyler** 21:50 Okay, yeah.
**David Ashpole** 21:52 So the… The mo- the main thing is… Yeah, if you have to create the new set every time you pass attributes, then you incur this… This is, like, the thing that escapes from… I don't know if you remember, like, with attributes always escapes.
**Tyler** 22:16 Yeah, right, right, yeah.
**David Ashpole** 22:17 Right? So, it's like trying to figure a way around it, and So, yeah, I added with unsafe attributes, but it doesn't… it's not performant. And… The filtered part, or the lazy filter part, does… address part of this issue, which is that if you have a filter, you actually call newSet twice, right?
**Tyler** 22:41 Yep.
**David Ashpole** 22:42 Like, really, really expensive.
So, but… and bound instruments would be, like, probably the… probably the best solution to this, so I… I would consider this closed if we added bound instrument support, or if we optimized With unsafe attributes, so that you don't have any allocations.
I don't think either of those would close this.
**Tyler** 23:05 Okay, yeah, alright.
Alright, so we have a path forward, and a line of sight on trying to get this done to this, this year, then. Perfect.
**David Ashpole** 23:12 Yep, for sure.
**Tyler** 23:14 Okay, cool. Where were we at?
Logs, SDK, observability, batch processor, metrics.
Don't know where we're at on this one. Robert's not on the call, so…
**David Ashpole** 23:28 I think this is the last… Pull request that's open, right?
**Tyler** 23:33 No, it…
**David Ashpole** 23:34 the SDK observability?
**Tyler** 23:37 Is it?
Oh, sorry. Yes, yeah, you're right, sorry.
Yes.
Yeah, okay.
Yeah, alright, so it's technically, I think, the last two are kind of the same here.
**David Ashpole** 23:54 Yeah.
**Tyler** 23:55 Yeah, okay, cool. Well, then that's almost done.
So… Yeah, cool, alright, so, looking really good, actually, for the planned goals for the year.
Awesome.
At least in this repository. There was also this Go runtime metric stabilization, I think from the other repo, contrib… did not get the Agentic complete beforehand, but, I don't know where we're at on that. I think that was blocked on a lot of semantic conventions, right, David?
**David Ashpole** 24:24 Which one?
**Tyler** 24:26 Let me see if I can find it…
**David Ashpole** 24:30 Runtime metrics?
**Tyler** 24:32 Yeah.
**David Ashpole** 24:34 I don't remember what that was blocked on.
Did I add… Did I add the new metrics we were discussing.
Oh, I wanted to do… I wanted to do… I wanted to do, opt-in metrics.
And then…
**Tyler** 24:52 Yo.
**David Ashpole** 24:53 to do view matching mode, to fix views so that I could have opt-in.
**Tyler** 24:59 And then that was also blocked on, like, the view, mergeability, right?
**David Ashpole** 25:04 So, right, the view mergeability. So I wanted to do view mergeability, and then I wanted to do opt-in metrics.
And then I wanted to do runtime metrics.
Tom.
But it looks like ViewMergability now has approvals.
**Tyler** 25:23 God, this guy.
Yeah, okay. I'm not exactly sure, yeah, this is, I think, what I was thinking of.
**David Ashpole** 25:57 I mean, the alternative is we can… If we're happy with the other metrics.
Like, not the new ones that I… recently proposed and added, we could potentially stabilize those.
Because if all we're saying is, like, oh, there's some extra metrics that are still going to be experimental.
Like, I feel like we've had the new ones out for quite a while now.
**Tyler** 26:21 Yeah, I think that's a good point.
I do, like, as long as we have a path forward on, like, trying to add more in the future, in some sort of, like… I guess it has to be, like, an opt-in kind of way for experimental.
But I don't see why you couldn't stabilize what we have, and then just move… Move forward.
It's also instrumentation, so, like, a V2 on that isn't really as,
**David Ashpole** 26:43 True, true.
**Tyler** 26:44 Haunting, I guess. So, yeah.
Okay, cool. Let's, let's… keep that on the back burner there, and I'll try to pay attention.
Okay, start sharing again… Next up, Lewis, you wanted to… talk about Azure resource sectors.
**Lewis Lewis** 27:09 Very simple. I have two Azure Resource Detector PRs. Would be great to get review. I see you guys also are about to upgrade to semantic conventions 1.4.3. If you do that, I will modify these to use the semantic conventions that have been added that are currently… I'm using a string constant.
**Tyler** 27:26 Oh. Oh, sweet. Okay.
Yeah, that'd be great. Actually, you should be able to do that, currently. I don't think it should conflict with Robert's PR, unless he… Hmm. Maybe… maybe he did… yeah, I'll merge that one, and then… then you can update, like you're saying. That'd be… that'd be a great idea.
But, yeah, so this is just looking for review.
Me.
So this is a new, detector?
**Lewis Lewis** 27:56 You guys did not have an existing one. A lot of the other SDKs do have one, and where relevant, I have included citations on what they're doing.
**Tyler** 28:03 Yeah, I gotcha. The only reason I ask is that we'll need a code owner.
If you would like to be the co-owner, that sounds great, but just you would need to change the code owner's file, and… Sure.
**Lewis Lewis** 28:16 I'm completely willing to do that.
**Tyler** 28:19 Yeah, awesome. I think that's… I think that's the only thing that I'm seeing… At a top level, like this, as well.
And these are… oh, interesting, yeah.
Yeah, we didn't have either of these, huh?
Yeah, but I mean, I think that looks great. I mean, yeah, same here, just the code owner, but otherwise, I don't think this is blocked.
Cool.
**Lewis Lewis** 28:52 Fans.
If you merge that other, the semantic convention upgrade, and I will add the co-owner, should I tag you?
Boo.
Review?
**Tyler** 29:02 Yeah, yeah, go ahead and tag me. That sounds good. It's… yeah. Reviews are a little tough these days, but I'm happy to put this on and try to get this.
**Lewis Lewis** 29:11 I have tried to make it as easy as I possibly can, because, sympathies.
**Tyler** 29:15 Yeah, no, it's just, yeah, absolutely, and I apologize for how long it takes to get things reviewed sometimes. But yeah, we'll… we'll get to it, for sure. I don't know if it's gonna get out in this next release, is the only thing I might say, but… That's fine.
Okay.
David, sorry, you were gonna say something?
**David Ashpole** 29:34 I was gonna say, there's also some of the new folks that have come in from the collector, so there's an effort ongoing to make the collector's resource detection processor use the GoContrib detectors, and so some of the code owners have come over from there. So, you might be able to get some… some reviews from, I think it's, like, Paulo… something, this is GitHub, but… Yeah.
**Tyler** 30:00 Well, and Puneet is on the call as well, yeah.
**Puneet Singh** 30:03 I can have a look at all.
**Lewis Lewis** 30:05 Wonderful. Thank you.
I, I did come over from, David, where you, you pointed me at GoContrib on, the original collector, so…
**David Ashpole** 30:14 That's right, right. There's so many new detectors coming in, I mixed them all up, so apologies.
**Tyler** 30:23 Yeah, perfect, okay.
Let's actually… I don't wanna lose these, I'm gonna… Picture… They're in the next milestone, so don't forget that.
I'm not saying there are going to be. If they're reviewed fast enough, we could get them in this one, but yeah, just don't want to lose them.
Okay, next up, you also wanted to talk about… Docker Detective Review.
**Puneet Singh** 30:51 Yeah, I mean, this has undergone multiple cycles of review, but every time it comes for a review, I think there's some much conflict issue or another issue, so this time I've made sure that, you know.
Before I ask, everything is green, actually, so…
**Tyler** 31:07 Yeah, I gotcha. Looks like… I'm guessing this is me? Yeah. Yeah, okay.
Yeah, I will also put this on… Why did I unlock this one?
Yeah, yeah, yeah, okay, cool.
Yeah, sorry, just reloading the context in my head. Yeah, this looks good, this just needs another review, then. This looks, again, also… I don't want to lose this.
This is something we could get done probably sooner, but… Cool.
Yeah, I will, I will take another look at this one.
**Puneet Singh** 31:39 Thank you.
**Tyler** 31:40 Yeah, and then I'm guessing, last thing is kind of what we talked about last time, right?
**Puneet Singh** 31:45 Yeah, so yeah, I wanted to discuss, because David is also here. So, I think in the last meeting, I brought up this idea because Meta Configurator has this external component which actually watches for change in the config and triggers that function within the SDK.
And I was looking for the use case that what kind of components are there in the ecosystem that might fit. Opm looked like an interesting case, because… It is also being used to apply the policy, open Telemetry policy, which is, I think, something new, and I think the trace-lated configuration is being… undergoing some progress in Java SDK, I think.
So… but the… how it is being applied is called dynamic control, which is why I thought this might be, make sense for me to configure, but later I realized that the kind of information The use case is entirely different. In case of policy control, it's more related to content. For example, receivers, processors, exporters. And even in SDK also, you don't have anything which is, like, instrumentation scope-specific.
all SDKs can apply that policy uniformly. While in case of meter configurator, it's looking for instrumentation scope-specific config.
Which appears like a standalone use case. So, I'm thinking of now dropping this idea of OPM, unless, you know, enough interest comes up to, you know, look for this option.
Any, any… Concerns or questions on that part?
**David Ashpole** 33:31 Yeah, no questions or concerns there. Do we know if there are any other languages successfully using Meter Configurator for dynamic use cases?
**Puneet Singh** 33:41 So, the only SDK I've seen is the Java helping implementation for this, but it is still in the… it is not fully exposed, actually. It is, in the protected mode inside the Java package, which means it cannot be used outside, so… I'm… I think it is not, I'm not sure how users can use and test that functionality. That is not clear to me.
**David Ashpole** 34:10 Yeah, I… I… I probably would not… I think that if I… if I was interest… if… if I was interested in trying to drive this forward, I would probably, like.
I don't know if an implementation is, like, the most useful Thing for this?
Right now, I feel like it's still… I don't… I feel like it's kind of half-baked at the spec level.
Like… it's not… it is nice for us to have the config surface in an experimental directory, so we can give feedback if it… If it does, like, if there's a push to stabilize it.
I wonder if… It's more likely that this is, like.
superseded by some of the policy stuff, rather than, like, integrated. Like, policies… Are kind of meant to be… Things that aren't, like, specific to… the SDK or specific to the collector, like, you can do consistent probability sampling at any point.
**Puneet Singh** 35:20 Yep.
**David Ashpole** 35:21 the same, and you can apply that, or you could, like, do a filter pretty much anywhere. This is, like.
I guess this is sort of a filter that could be pushed down?
But the… at the Spec SIG last week, when… or on Tuesday, rather, when… Right now, it was the TC meeting. At the TC meeting on Tuesday.
I'm getting all mixed up. It was the TC meetings.
**Puneet Singh** 35:42 Tuesday, I think.
**David Ashpole** 35:44 At the TC Meeting on Wednesday, when Jack and I were discussing this.
It's like, the high-level sketch is… that there might be, like, specified SDK components, like.
a policy log processor or something that would integrate with OpAMP or some other remote protocol.
to receive policies.
And that it would be an SDK component that would be available.
kind of similar to how, like, a Jaeger remote sampler is something that could exist in Contrib, or… Right?
And that… that set of SDK components would be specified, would be added through the normal Like, spec.
Prototype stabilization process.
And those would… speak in terms of policies, and at the same time, collector components that can understand policies will start to exist. So I… I think they're two distinct things. I… I doubt that there's gonna be, like, a… a need to… Do the configurator stuff via policy.
it could still be useful over op-amp, like… We've talked previously about making you know, collect… or SDK config.
Dynamically changeable, so it could be more like… HotelConf watches the file instead of just opens it, or something like that, and you can only change this one field, otherwise it breaks. That seems like… Yeah, I don't know, that seems like it has its own issues, too.
**Puneet Singh** 37:19 So, so policy control document does talk about that, what are the alternatives of OPAMP, and it talks about the changes that can be monitored at file level or HTTP endpoint.
But those are not implemented, so it only talks and use about op-amp, actually. But yeah, a simple use case would be simply a file watcher, which watch for the file changes and triggers the configurator, actually. That would be much more simpler to start with, I think.
Yeah.
**David Ashpole** 37:49 But I don't think that would, like, necessarily interact with the policies.
**Puneet Singh** 37:53 Yep, yep.
**David Ashpole** 37:54 Yeah.
**Puneet Singh** 37:56 All right, so, so next thing is the declarative config, but… again, the same thing, actually, that, adding support in declarative config is just adding options in config to start with the configurator option, and for the same reason, I want to hold these changes, you know, until I find the sufficient traction. So, the meter configurator example as an implementation would provide a good example in case you want to implement stuff like policy control later on, but I want to hold the changes Like, supporting it via declarative config and, same argument as OPM, I think.
Does that sound?
Reasonable.
**David Ashpole** 38:44 I didn't quite follow that.
you could… I think it's the intent that… Like, you'll be able to someday serve declarative config via op-amp.
Right, so those, like… it's just a YAML file, in the same way that, like, you could manage your collector config with op-amp, like… I could imagine people managing their SDK configs via OpAMP. So I don't… I don't think those two are, like.
Like, op-amp is just the transport.
for… a config.
And some additional, like, tooling around it to… Proceed.
**Puneet Singh** 39:20 Not that. I mean, the reason was purely the… the adoption and traction for the feature itself, actually. That if there is enough I mean, I'm not saying in terms of overlap with OPM, but more in, like, if there are enough takers for the… for the feature, I will add the support in the declarative config as well.
**David Ashpole** 39:44 for the configurator. Yeah, I think that's… that's reasonable, like… I don't know anyone who's actually asked for the configurator in Go yet, so some of this is, like.
Like, I think the main reason we would want to implement it is to make sure that, like, there aren't any issues with it if it does go stable.
But I haven't seen this as, like, a particularly high-demand feature. If it's something that you care about for your own uses, then that's maybe a different story.
And I'd be interested to hear about them as well.
**Puneet Singh** 40:16 Got it. And just as a part of following up, you know, with the overall spec, I had a discussion with Jack from.
JavaS SIG, and I was just following up that, you know, we… when we use meter configurator and disable meters, we stop emitting those data, but there's a producer side of it also, which keeps collecting data.
And what happens in the case where meters have ran for some time, and then you disable the meter, actually. So, there are specific cases in which data, aggregate data.
aggregated data is left with the meter. And why, on the reader side, you should keep reading those data?
That was the caution, actually.
So, to which, Jack suggested that the… that was definitely overlooked when the suspect was getting written, so that part is definitely adding, and… Slightly worth heading later on for the completeness of a spec, but yeah.
That was another find.
**David Ashpole** 41:24 Cool. Yeah, anything you find is worth documenting somewhere in the spec repo, so if there is a tracking issue for stabilizing the features.
Then it's good to at least leave it as a comment there, or make it its own… own issue if there's, like, something that's missing from… The configurator spec that we would need to address before stabilizing it.
**Puneet Singh** 41:46 Order.
Yeah, I think that's… that's more or less ahead. Thanks for… answering this.
**Tyler** 41:57 Awesome.
Okay, cool. I'm looking at the agenda, it looks like that's the end of the written agenda. Any other topics folks have?
That aren't on the agenda? Any other burning questions?
Things to take a look at.
Pretty sure KubeCon talk announcements come out, I think it's next week? Maybe the week after, so I'm pretty excited to hear people's talks got accepted.
But, yeah.
I'm excited. Hopefully folks are able to join, in the KubeCon North America.
But, yeah.
We'll see. Fingers crossed.
**David Ashpole** 42:44 Should be there.
**Tyler** 42:46 Yeah. Oh, I guess on that note, the Maintainers Summit is accepting talks right now, for CFPs. If you're gonna be there, definitely worth, if you have some ideas. If you're not.
Planning to talk, also worth attending.
A little awkward, because it usually is, like, on a Sunday, but, yeah, it's always fun.
**David Ashpole** 43:06 Cool. It was good last year.
**Tyler** 43:07 Yeah.
Yeah, actually, it's, like, surprisingly, like.
I don't know, it's worth… it's worth going on Sunday, I'd say, as well.
**David Ashpole** 43:16 Yep.
**Tyler** 43:19 Well, cool. Alright, if there's no more agenda items, we can end the meeting here. Thanks, everyone, for joining. Good to see you all. I will see you all in a week's time, or, asynchronously.
Bye.
**Puneet Singh** 43:30 Into…
**David Ashpole** 43:31 Bye.
