SIG: Go SIG
Date: 2025-09-11
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/r6aH7CUmuT5VCWxV3dfFfsk9gL_28PshGkI9GB9-tMPNSoMmm_U6ob_uTaMDbXtq.W5Hb5201t1hRWheh
============================================================

## Zoom Recording Transcript

Tyler Yahn 00:00:41 Hey, Brian.
Robert Pająk 00:00:58 Hello.
Tyler Yahn 00:01:01 Hey, how's it going?
So I think we could probably get started here in just a second, I don't think some of the other folks are gonna make it, so I think this might be the quorum for today.
If you haven't yet, please go ahead and add your name to the agenda, or sorry, to the attendees list, and if you have agenda items you want to talk about, go ahead and add them there as well. I can start sharing my screen.
And we can jump in here. So, first off, I wanted to get started. I wanted to talk about this last week, but nobody was, here to discuss it, so we postponed it to this week. We have, release, 138, the prior week, so 2 weeks ago. So, the 139 milestone is still, fresh, and I just wanted to kind of ask… If there are things that people know, we have open, or issues we have open, or topics we wanted to include in these.
And make sure that we have them included so we can try to target that work, over the next few weeks.
So yeah, we can take a look here at the, the 139. I don't think I see too much outside of, a few open PRs that maybe we could talk about in a second, but We have this expose metrics transform function. This is something that was opened, In July?
It looks like this got added, I don't know… how it got added, but, so this looks like something that's still here. Is this agreed upon that we wanted to try to include this?
I guess it looks like I was the one that added it. It looks like there's also, like, not a clear proposal here, so I'm wondering if this needs to get removed prior to it being added to the milestone?
Robert Pająk 00:04:05 I think I proposed, somewhere, just to expose these functions, and I didn't, like, this was a separate proposal to introduce the client interface, which was interesting.
And I think both me and Sam did it like this approach of creating this, this kind of, you know, interface and, structs, which only basically has something like a shutdown, and I don't remember the exact implementation, but that's basically almost nothing.
So, I think I was proposing just to extract this metric transform function, basically.
What do you think, Taylor?
Tyler Yahn 00:04:47 Yeah, Yeah, I mean, it's not the first time somebody's asked for these transform functions. It's always been something that we're a little hesitant to do, because, I mean, you can always copy the code and do whatever you want, and it kind of locks us into… a structure, so I think we'd want to pay some attention to it. I do think we don't want to do this client thing, like… No, no.
Robert Pająk 00:05:15 Yep.
Tyler Yahn 00:05:19 But yeah, I mean, I think we'd want to probably think through what we do have for the transform functions, because I think, I mean, they were just kind of… put together. They weren't really used in anger, so, like.
They work pretty well for our use case.
But we might want to rethink, like, the public API that we exposed for this, just to make sure that, like, it works for folks.
It might be fine. I just haven't taken a look at it in a while. We'd also want to make sure it's consistent across all signals in how we're going to do that.
I mean, that's another… Yeah, how… where… where would we expose it?
Robert Pająk 00:06:04 So I was thinking about support module of TLP metric, specifically a conversion.
Also, I was thinking only about exposing one function, only for transforming the resource metrics.
So, like, you know, like, the aggregate, not all the… You know, these little steps below.
Just the aggregate roots, basically, and not everything below the leaves, etc.
Tyler Yahn 00:06:35 So, okay, so, I mean, it's… Yeah, what about resource traces?
And resource logs.
Robert Pająk 00:06:46 We will do the same for consistency.
Tyler Yahn 00:06:49 Okay, are they all gonna be in the same package?
Robert Pająk 00:06:51 Mmm… So here, I propose to have it differently, so that's why it's metric, metric conf.
What European?
I think, in theory, they could be the same module, because they have the same dependencies? No, not really.
Because one, yeah, they have different APIs.
Tyler Yahn 00:07:15 Well, I mean… Same dependencies on the same modules.
It's just the OTLP module.
Robert Pająk 00:07:25 Could you scroll to the bottom? Just, I just do not remember… To the bottom.
Yes, so… transfer resource metrics, so, resource metrics, I think, was accepting a struct for, from… could you just click it? I think it's, Yeah.
Yeah, so it was basically accepting metric data. So the reason why I thought about creating a separate module for each metrics, you know, SDK, for metrics, for logs and traces, because it accepts, basically, a type from a different module.
Tyler Yahn 00:08:18 Yeah, I see.
Robert Pająk 00:08:21 So here, it depends on the metric SDK. The traces will depend on, trace SDK.
which kind of also couples it to the SDK.
Admit to the API.
Yeah.
Tyler Yahn 00:08:54 Yeah, so I mean, I think there's a lot to think through about, like, how we'd actually want to structure this. I'm still not 100% sure we want to just expose one function. I think that's nice because it reduces the blast radius, but I don't know if it's actually gonna.
Robert Pająk 00:09:05 That's what's my idea.
Tyler Yahn 00:09:06 Yeah, the problem is, is it's not composable, and it's not really that useful, right? Like… If I go and I'm, like, trying to use this for, like, testing or something like that, and I just want to test something with… something deep into the internals of the Proto.
Robert Pająk 00:09:21 Yes, Lord.
Tyler Yahn 00:09:22 yeah.
Robert Pająk 00:09:27 But the others, on the other hand, the other functions could be added later.
Instead of putting everything at once.
Tyler Yahn 00:09:35 Yeah Yeah, this is kind of what I'm talking about, though, is, like, I think that, like, we should probably think through what needs to be added.
Because, like, I think that that makes sense. I think also, like, things like this were… if you're gonna accept a pointer to resource metrics, like, is that really what we want, or do we want to actually accept the struct itself, right, the value type? So, I mean, I think there's a lot to go through in, like, a design doc phase here.
Okay.
Okay.
Also, we have, deprecate and Rename SchemaX types package.
Is included in this next milestone?
I'd rather not touch this, to be honest.
Yeah, I don't, Yeah, I mean, I think the entire schema package being experimental is fine, and I think changing it is fine, but, like, changing it just to change the name is gonna be churn. Like, we actually don't have a… I think there's a… there's a path that looks forward where we're gonna have an entities idea, and, like, this entire package isn't… going to get changed, it's going to get dropped. Like, I don't think it needs to exist in the long term.
I don't think this is in the same line as where OpenTelemetry's trying to go. Working schemas is pretty much… On a permanent pause at this point, at the specification level, as entity work is being developed, so… I might even say we want to close this, but… I definitely don't think we want to include it in this next milestone.
Okay.
Alright, remove that.
I think, we have wise carnality limit ads, performance overhead to metric measurements, Why? Why… Why does? Why…
Robert Pająk 00:13:32 That's, yeah.
David Ashpole 00:13:41 I can probably partially answer this, So… Map accesses are very expensive.
I'm not sure… without the, hashing PR.
It may become much cheaper after we use a hash for distinct.
And we have to check as part of attribute limit whether the attribute set already exists.
Just a hypothesis, though.
Bryan Boreham 00:14:13 So the… The… the person who raised this, they're… What they're saying is it shouldn't change the cost of, like, bumping a counter.
It should only cost when you add a, A new series, or a new metric.
Tyler Yahn 00:14:34 Robert's the one that opened this, so I don't have to ask him.
Robert Pająk 00:14:37 I think it was CJ who created it, just created based on his comment, but I think it was related to… to the place when the cardinality limit is applied, if it's, you know, added on the measurement level, or on the… on the place when it's being exported.
And I think Raz did it on the other way, when it was… so they were not applying it on, you know, during measurements, if I remember correctly. But yeah, it was… It was July, and I do no longer remember its conversation.
But I think it was related to this kind of, you know, place where you apply the continental limit, which was unspecified. I'm not sure if it's specified right now in specification.
Yeah, it's…
Tyler Yahn 00:15:22 It is.
David Ashpole 00:15:23 Yep. I thought it was specified.
Tyler Yahn 00:15:26 It's recommended, at least. And the reason why it's recommended is because it's… like, if you do it the way that Russ… you just described Russ doing it, which is how we originally had it, which is where they got it from, so there's a little bit of a… anyways, but like… Then you don't actually limit the memory footprint during the measurement cycle, and so that was the whole reason we changed to this. And so, yeah, there's still, like, that open question of if we want two different limits.
Robert Pająk 00:15:51 decide.
Tyler Yahn 00:15:52 One day.
Robert Pająk 00:15:52 Yep.
Tyler Yahn 00:15:53 Yeah, but…
Robert Pająk 00:15:54 Yes. So I think that's the only reason why we have this issue.
Tyler Yahn 00:15:59 Yeah, and I think to David's point, I think he's right, because, like, what you're doing when you do this is you have to verify, like, do these attributes already exist? And if they don't do, then you need to, you know, do some limiting. If they don't, then don't worry about it, but you have to do that check first.
So, yeah, I mean, I think it… what's this, 19%? Yeah, I mean, that's reasonable, or not reasonable, it's a… appreciable,
Robert Pająk 00:16:25 Yes.
Tyler Yahn 00:16:27 So, yeah, I mean, I think that, to David's point, like, especially attributes 0 to 32… Oh no, there's no attributes.
David Ashpole 00:16:36 That… It still is actually quite expensive, given our current set of notation for no attributes.
The only other thing… Because we're holding, A full lock?
during the call to attributes, we're holding the lock for longer. I don't think this… was measured using a parallel benchmark. I think this, you probably… wrote this issue before I changed the benchmark to parallel, but I expect to talk.
Robert Pająk 00:17:03 Beautiful.
David Ashpole 00:17:04 I expect it's much worse when the benchmarks are run in parallel.
Fyi.
Tyler Yahn 00:17:38 So is this something that we're trying to address in this, next milestone?
Robert Pająk 00:17:45 Okay, go on, David.
David Ashpole 00:17:48 Well… Like, I think this is just a symptom of the general problem that we're trying to fix in the distinct one and in my follow-up PR, which tries to change how locking works.
I think we should revisit this after this PR and after the locking change.
And just remeasure, and hopefully it'll be negligible in that case.
Tyler Yahn 00:18:13 organizationally, like, and maybe even aspirationally, like, the idea that I'm getting from you is, like, we want to include this in this milestone, and then we would keep that other issue in the milestone, right?
David Ashpole 00:18:24 I think this is a big change.
So if it misses because we're not sure of it, or because there's still work to be done, then that's fine.
I don't know when we're planning on doing this milestone. I'm just getting back today, so I will have more time to work on that.
Tyler Yahn 00:18:40 Sorry, yeah, let me just catch you up, like, so we just had a release, like, not last week, the week before, and so we're trying to get a plan for, like, the next two to four weeks.
David Ashpole 00:18:49 I definitely want this included.
Tyler Yahn 00:18:52 Yeah, yeah.
And I think this is pretty close, honestly. I think there's some…
David Ashpole 00:18:57 I do too. I haven't looked at your comments yet.
Tyler Yahn 00:19:00 Yeah, I wanted to talk about this later, so maybe we can talk about this one, because I can't actually remember what I put.
Oh, yeah, plus testing, and then I think Robert found something?
Oh, yeah, just, oh, yeah, this is minor… This is kind of important.
David Ashpole 00:19:19 Go… 123 or something?
Tyler Yahn 00:19:24 Yeah, we dropped 123 so we can do this now, which is great.
Robert Pająk 00:19:28 What's another form, yes.
Tyler Yahn 00:19:31 This, I think, is just an improvement on the fuzz testing. There's actually some testing there. And then this is a, Frustrating bug is what I called it. So, yeah, it's a little bit… So, the empty set is actually immutable, so we probably shouldn't use the empty set.
Just a heads up on that one.
David Ashpole 00:19:54 Okay, I just… I just kept the existing empty set logic everywhere.
Tyler Yahn 00:20:01 Really? Ugh.
David Ashpole 00:20:02 Well, I mean, this is already how, the equals, or the distinct creation works.
Like, if you call the distinct function, this is what gets called, you check nil, you check 0, And then you default to the empty set in those cases, so… Interesting. Okay. Okay.
Tyler Yahn 00:20:22 If that's the case.
David Ashpole 00:20:23 I'll look at it.
Tyler Yahn 00:20:24 We can address them later, yeah.
David Ashpole 00:20:27 Before we can address it before we do this, that could also work.
Tyler Yahn 00:20:30 That also could… yeah, that's not a bad idea.
Okay.
So… I got those, that's great, I think we got some more things here.
Any other things that we wanted to try to make sure we include here?
I think maybe we can pop open these issues here.
Alex Kats 00:20:53 There is this new temporality selector PR. I just started looking at it, but… I don't know if anyone else has taken a look at it yet.
Robert Pająk 00:21:05 Yeah. It's from stopping.
Tyler Yahn 00:21:10 Took a look. It's a little bit, I think, flawed in some ways.
So, one of them is that none of this stuff is actually exposed in any of these… exporters.
As far as I can tell. But the other thing is, like, I'm not exactly sure, like, what this is doing, like, it's just adding… An enum type for something that you could already accomplish by passing in your own Custom selectors, so, like, it just seems like it's adding additional code to achieve the same thing.
Which seems a little odd for me.
David Ashpole 00:21:44 I think it was that… My understanding is that they are building something that is similar in purpose to the config file format that we're working on, but specific to their application and code structure. And so… they don't want to have to rewrite or copy all these functions, and they feel that it would be useful, generally, to be able… like, as a user today, for example, I cannot easily say, I would like this reader configured with delta temporality.
What you end up doing is you end up, either just using the environment variable, Or… Rewriting or, like, copy-pasting this particular temporality selector function from… The OTLP exporter?
And so, I think the ask is just… If, given that these are defined in the spec.
And are potentially generally useful for others.
Can we expose them publicly?
Yeah. Right.
Tyler Yahn 00:22:48 So… But this is, I think, kind of my question is, like.
David Ashpole 00:22:52 Do you provide a temporality selector here?
Tyler Yahn 00:22:54 Or are you providing… A temporality preference.
David Ashpole 00:23:01 Oh, this is interesting. I don't know if I like exposing those strings.
Right.
Tyler Yahn 00:23:08 Good preference.
David Ashpole 00:23:09 I'm okay with the selector functions, because these strings are specific to our environment variable.
spec, not to the SDK spec. So I, like, that's probably where I would draw the line as well.
You're right.
Tyler Yahn 00:23:23 Yeah.
Yeah, I mean, I could definitely see the reuse factor here, like, if a lot of people are using it, like, that makes sense to me, but, like, this seems a little, okay.
David Ashpole 00:23:34 I would prefer that if we were going to expose this, that this be made Part of the public interface in the hotel conf.
package or something, like, where you'd be able to say, give me a temporary selector from a string, and someone could, yeah, whatever.
Tyler Yahn 00:23:51 Yeah.
David Ashpole 00:23:52 If they wanted to use that.
Tyler Yahn 00:23:52 then there would only be one choice, right? Like, yeah, exactly, yeah.
David Ashpole 00:23:57 Yep.
Tyler Yahn 00:24:01 But, okay, so going back to Alex's question, should we include this in the milestone, I guess is the question? Try to prioritize it over the next few weeks?
David, you seem to have background on this. Was this a pretty… This is a Slack fold, this is, oh, what project is this? Knative?
David Ashpole 00:24:19 This is Dave… I'm not gonna try and say that. This is Dave, who's been posting in our Slack.
a whole bunch. He's… what project is he from? Knative. So this is another large CNCF project that's migrating to OpenTelemetry. I think it would be very good to support them.
In whatever way we can.
But… Yeah, okay.
Tyler Yahn 00:24:48 than…
David Ashpole 00:24:48 I would like to at least decide whether we want this in the next milestone.
Tyler Yahn 00:24:53 Okay.
Yeah, I mean, adding it to the milestone is…
David Ashpole 00:24:57 It doesn't…
Tyler Yahn 00:24:58 Yeah.
Yeah.
David Ashpole 00:24:59 It's, it's a…
Tyler Yahn 00:25:00 aspirational.
Okay.
Anything else, Alex?
Alex Kats 00:25:08 Yeah, this one's just top of mind.
Tyler Yahn 00:25:11 Yeah, okay.
David Ashpole 00:25:13 I would like to just… I don't know how many people have looked at it, but I have a, optimized locking for metric aggregations as well, that I think would be good to look at.
I will do this after the… the distinct PR lands, because I'll focus on that one first, but this is a… another pretty significant improvement on top of the, using a hash indistinct.
And this basically splits our current… Lock into, or our current mutex into a read-write mutex.
And has some pretty… and then uses atomics.
And compare and swap for the individual counters and stuff.
Which… and it looks like it has some pretty significant performance improvements.
In the multi-threaded, or in the parallel benchmarks.
The single-threaded benchmarks are more of a mixed bag. There's some improvements and some places where it gets worse, but overall, this seems like Yeah, you can see, overall, I think this is a direction we should at least consider, but I'm still working on Exactly how to do this best.
Tyler Yahn 00:26:30 So add it to the milestone?
David Ashpole 00:26:33 If that's okay. I plan to work on it as soon as the hash one is merged, and I hope that that's merged in the next one.
Tyler Yahn 00:26:39 Sorry, there wasn't any… yeah, judgment in that, it's just…
David Ashpole 00:26:42 Yeah. Question, yeah.
Tyler Yahn 00:26:44 Yeah, just do it. Okay.
Okay, and then… I think that was… Any other ones that people have, in mind?
I guess the question is these self-observability or observability questions. We have a lot of these PRs. Should we try to…
Robert Pająk 00:27:06 I would like Tyler to have, your two, your two PRs to be merged. I didn't have a chance to read them for the processor and the tracer, because this showed just, you know, different patterns that can be used for, for observability.
Yeah, those two. I think these are.
Tyler Yahn 00:27:26 Yeah.
I was just gonna ask for a review for these later on in the meeting.
Robert Pająk 00:27:29 Oh, they're older than my stone. Yeah, that's good.
Tyler Yahn 00:27:33 Yeah, they're already there.
So, yeah, if you have time, please take a look. Looks like David's already reviewed this one, so thanks.
Yeah, I… that'd be great. I don't think they have to merge before we asked about the other observability ones, though, I guess that's kind of the question.
David Ashpole 00:27:51 Could… Can you find the tracking issue that has all of the PRs linked? Yeah. I just want to see how close we are to… Actually having, sort of, feature-complete status.
Tyler Yahn 00:28:04 Sorry if I'm going the roundabout way, this is how I always do it.
David Ashpole 00:28:07 It's funny.
Robert Pająk 00:28:08 I do it the same way.
And then parents.
David Ashpole 00:28:19 SDK observability, there we go.
Robert Pająk 00:28:22 I think there's a lot, you know.
David Ashpole 00:28:27 So we've got the credible.
Tyler Yahn 00:28:28 view.
Robert Pająk 00:28:29 But most of them have already PRs opened.
Tyler Yahn 00:28:34 Yeah, and all of them have an assigned, right, yes.
David Ashpole 00:28:46 It's exciting.
Tyler Yahn 00:28:49 It is. It's also daunting.
There's a lot of review that's required for a lot of these. So, I mean, I'm fine with adding them, and we could try to get these all in and try to prioritize these reviews. It would kind of be, like, the main… bulk of work we're doing outside of what we've already included in the milestone, I think, is trying to get all of these in.
David Ashpole 00:29:11 I… It, it feels…
Tyler Yahn 00:29:15 I'm okay with that, I just… it would require more than me, is kind of the question.
David Ashpole 00:29:19 Yeah, so I'm back now, so I can start reviewing things. I know I haven't been on the ball there, obviously, but…
Tyler Yahn 00:29:25 Oh, that's… yeah, that's crazy.
David Ashpole 00:29:27 It feels like a lot to try and… get them all in for this milestone, so I'm also okay just not putting any of them in.
And assuming that we'll have them all by, like, the next milestone after that or something. Like, that feels maybe more realistic.
I don't know how people feel about that.
Like, we're not gonna have… Feature completeness, the milestone, anyways.
Robert Pająk 00:29:52 I think the… I think the main point here is that we should prioritize reviewing those PRs, at least these ones where the contributors are really healthy for us.
That's fair.
Tyler Yahn 00:30:04 I kind of agree, like, some of them… I think some of them should definitely be in, but I also think that we have a little bit more of a foundation to measure these against as well now, so, like, it should be a little bit easier to point to, like.
you know, follow this pattern, follow this pattern. Yeah, or something like that. So I think it should be a little bit faster, But yeah, I agree as well, like, things like this where they're assigned, but they don't actually have PRs yet, and they're, you know, probably just working on something else, is… It's a little bit tough to say that we're gonna try to accomplish that in this next, milestone.
But yeah, maybe what I'll do is I'll go through afterwards and, like, all the ones that have open PRs, I'll try to add them, and then we can… essentially, then we'll have a tracking list for what we actually want to try to do. I think for… Milestones for this, we probably want to put this into, V140.
Robert Pająk 00:30:58 Yep.
Tyler Yahn 00:31:01 Yeah.
Okay, and so then, yeah, from there, I think we can, like David said, try to maybe get this done in the next cycle after that, so yeah. Okay, I'll follow up on the rest of these then, though.
Going back to issues, though, I don't, Okay, I don't know what else… if there's anything that stands out that people want to talk about around including in this milestone here.
I think he's a lot.
Robert Pająk 00:31:32 What about… what about the Exporter premieres and these new… Strategies, David.
Maybe we should follow up on this one? Is it important?
Sweet.
David Ashpole 00:31:46 Did that not already merge?
Robert Pająk 00:31:49 I don't think so.
I just remember.
Tyler Yahn 00:31:53 Oh, it didn't? I thought this did merge.
David Ashpole 00:31:55 Yeah, can you scroll down? Did we just not mark it fixed or something?
Wait.
Tyler Yahn 00:32:05 No, I guess so…
David Ashpole 00:32:06 Well, there's no linked PR. Yeah, I thought Owen… O, W, yeah, O and whatever.
already merged a PR for this.
Robert Pająk 00:32:20 I also… maybe it's just a follow-up to remove the deprecations and stuff like that, because I remember that some of the things were deprecated.
Without units, etc. The question is, do we have the follow-up?
And is it now, or next milestone?
Just to make sure that we… we just keep the momentum and not have any leftovers.
I remember in the changelog, we had this notification about the changes of the default behavior, and this has been merged.
And we are also saying that the future release will change the strategy. So maybe it's now the point when we need to change the default strategy.
Or something like that.
David Ashpole 00:33:02 You're right. Has there been a release since that one was merged?
Robert Pająk 00:33:07 I think it was… I think it was one for two.
Tyler Yahn 00:33:10 It's funny.
Robert Pająk 00:33:10 38.
David Ashpole 00:33:12 Okay. So now we need to update.
Robert Pająk 00:33:13 Beer?
Yes, here. So, yeah, I think it's the follow-up right now. Thanks for the follow-up.
David Ashpole 00:33:22 There it is, yep. You're right.
Tyler Yahn 00:33:27 So this is including… this just means the things that haven't deprecated need to be removed? Is that… is that what's left?
David Ashpole 00:33:32 No, so.
Robert Pająk 00:33:33 And change the default.
David Ashpole 00:33:35 Yeah, so there's 3 tasks, and I… got the author to split them to make sure that they were properly split across releases to give users time, but basically, 1PR introduced the new options and deprecated the old ones.
And gives people a warning.
If… their current… Options are going to basically break in the next release.
The next one after this release, so right now, basically, we should change the default to the default that we want to have eventually.
And then eventually we want to remove the old options.
Tyler Yahn 00:34:16 Okay. But there should be a few releases, probably, between that.
Like, there's no reason to rush. I think the declarative config still depends on the old options.
Yeah, that's a thing they're trying to change as well.
David Ashpole 00:34:30 Yep.
Tyler Yahn 00:34:31 Yeah.
David Ashpole 00:34:32 I guess…
Tyler Yahn 00:34:34 Oh, I see what you're saying, but also, like, the V2, or V02 or the V03 will always depend on those old options.
David Ashpole 00:34:41 Yes.
I don't… so I don't know how we do that. I… we can keep the options around for a while, like, we're not really looking at stabilizing this module just yet.
Tyler Yahn 00:34:52 Okay.
Should we try to tackle the changing the default in this next release, or are you saying we want to do.
David Ashpole 00:34:58 That should be a very small change.
Tyler Yahn 00:35:25 Okay, and then.
David Ashpole 00:35:28 This one here…
Tyler Yahn 00:35:31 Is this also one you were talking about, Robert?
David Ashpole 00:35:33 That's not…
Tyler Yahn 00:35:35 Okay, this is a different thing, okay.
David Ashpole 00:35:37 Yeah.
This is just, like, a nice-to-have, the Prometheus client provides some nice… Error handling, Config.
That you can configure on the handler to say, like, whether it should fail a scrape or what it should do. And we don't… make use of that today. We use the hotel.handle, which is, in my opinion, significantly, like, it doesn't have nearly as nice tooling and options and stuff around it. So, I think using the Prometheus one, is… makes more sense here.
Tyler Yahn 00:36:11 Okay. For, like…
David Ashpole 00:36:12 code.
Tyler Yahn 00:36:13 Can I add this to the milestone?
David Ashpole 00:36:15 We can try to find some help. I don't plan to work on it, but you can mark it as help wanted, and I'm happy to help someone.
Tyler Yahn 00:36:26 That sounds good to me. I think that's… Agreed. I agree. The hotel handle is not ideal. It is a last case thing.
scenario, sort of thing.
David Ashpole 00:36:38 Okay.
Tyler Yahn 00:36:53 I think that's.
David Ashpole 00:36:55 Yeah, okay.
Tyler Yahn 00:37:01 Okay, this is probably good for looking at this milestone. We could take a look at the contribrib one. Right now, we just have remove the deprecated, inject, and extract functions from OTelGRPC.
This has an assignee.
This is from August 7th?
Right, so we've just released the deprecations, because they weren't… correctly formatted, but I think this is, Formatted at this point, so we can, say it's not blocked at this point.
Anything else in the contributor repository that people want to talk about?
Alex, I know you're a little more active here. Is this something that you have open, maybe?
Alex Kats 00:38:08 No, I don't think so. Nothing that comes through right now.
Tyler Yahn 00:38:14 Okay.
Okay, I'm also looking at the time, this has taken up a fair amount, so if you have other ideas or other issues, comment on them, or just put them in the milestone if you think them They're needed, but cool. Looks like we made a lot of progress there.
Alright, next up, Robert, should we try this, SIG security issue? Maybe we could sign the tarballs with, I'm guessing this is a signing solution here?
Robert Pająk 00:38:45 So, you have made a preview, or some people… I think immutable releases?
Which is, I have not tried it. I'm not sure if I can try it on my private repositories, maybe I should.
But basically, it uses the GitHeroFi, which is, Business, I do not remember, but I was reading some time ago about this tooling.
And, yeah, I just wanted to ask if we want to try it for Auto Grow.
Tyler Yahn 00:39:21 Yeah, I mean, I think opening an issue to track… trying it sounds great. I wouldn't want to… Just turn it on on the repository without, Yeah, maybe, like, creating another repository and verifying it there that it works is good, and how to check that verification.
Is, I think, gonna be important.
Robert Pająk 00:39:39 Yes, okay.
Tyler Yahn 00:39:42 Yeah, I agree.
Robert Pająk 00:39:42 on it, and collaborate with Trust. I just want to double-check if it's something that we are open to work on before doing anything.
Tyler Yahn 00:39:52 Yeah, I mean, I think that is great, especially if it pulls into the toolchain. I'd want to… Yeah, I think there needs to be a way to, like, verify it in the same way that we're already verifying where you have some sort of trust chain? Like, I guess there's going to be some sort of, like, GBG keys that are managed by GitHub at that point? Yes, so this is.
Robert Pająk 00:40:18 Yes, this is basically all handled by the GitHub CLI.
If I remember, it was under the Cut using callsign.
And they're touring in their truss plane.
So, yeah, so basically it's easier for the end user, because basically everything is built in into the GitHub Verify CLI.
Tyler Yahn 00:40:41 Yeah.
Robert Pająk 00:40:42 It uses basically the GitHub signatures.
Tyler Yahn 00:40:47 Yeah, I think when we do look into this, we probably want to, like, see if we can… I think verify those keys is kind of important.
Because what I see is, like, if you're using the tooling that has the keys themselves and the tooling itself is corrupted, like, that's gonna be a problem, right? So… I don't know, just some way that you can actually, like, verify that there's a third-party check, and that, like, if you have an attacker come in and… Corrupt one thing, it doesn't… ruin the whole thing, I guess.
If that makes sense.
Robert Pająk 00:41:28 Yes, and I think that there is one problem to it right now, because I think that a release can be done by any approver at this point, right?
Tyler Yahn 00:41:41 In… in the Ghostig?
Robert Pająk 00:41:45 I mean, I mean anywhere, any repository.
Tyler Yahn 00:41:50 No.
Robert Pająk 00:41:53 So what is blocking?
to create a release. I think you just un…
Tyler Yahn 00:41:59 need to be able to push a tag, and you need to be able to click the make a release on the GitHub,
Robert Pająk 00:42:05 I think it's only about… so, it's only about creating the make a release. So, yeah, so… an approver can… cannot create a tag, but can create a release, if I remember correctly.
Tyler Yahn 00:42:19 I don't think so. I think you need write permissions to the repository to be able to do that.
Robert Pająk 00:42:24 Okay.
You can ask…
Tyler Yahn 00:42:27 our approvers to verify for you, but this is something I think we've looked… I mean… This is something we looked into years ago, so, you know, obviously things change over that time. If that has changed, it's probably a problem to raise up to the GC or the TC, even.
Robert Pająk 00:42:43 I think I was rising gear a few times.
Because if I remember correctly, our maintainers have right permission, approvers have right permission.
That's me?
Tyler Yahn 00:42:56 Well, that's changed. That was not the case in the past, so if that's changed, I think that needs to be re-evaluated.
Robert Pająk 00:43:06 There we go…
Tyler Yahn 00:43:26 Okay, well, Robert, I don't know, I can't really see you, so I'm guessing maybe you're looking… Yeah, okay.
Robert Pająk 00:43:32 Yes, sorry, I turned off my camera by mistake.
Yes, less possible, Nate, that's… yep.
Tyler Yahn 00:43:40 Okay.
Next up are two PRs asked for, he's on, no worries here. Robert, you wanted to talk about the Spec Make Configurator SDK feature optional?
Robert Pająk 00:43:53 Yeah, so basically, the NASC Or the whole… Go seek?
I think we're talking about… a few months ago. I'm not sure if it's still true, or if… if I understood correctly, or also if our opinion was go through. So basically, right now, the SDK, Has for all of the trays.
Trace SDK, Matrix SDK, Logger SDK, has this kind of tracer configurator.
And if you read the specification, it look… it… it is not kind of… it's hard to say if it's a requirement that the SDK should support this configurator, or if it's optional. So.
I… I could even say that if you read the specification, you could even… think that, given the metro provider must compute the relevant material config, it has such statements, you could assume that it's a requirement, but I'm not sure if anyone was… who was even approving these PRs when this was initially added, was having this way. I think, Tyler, you thought that it's an optional, that some languages would want to provide, but probably we didn't want to provide this metric configurator, because it's a second way of configuring, basically, the pipelines apart from the views from the metrics SDK and processors for the logs and trace SDK. So I… so basically here, I tried to make it, Explicitly as optional.
that SDKs do not have to support it.
And… yeah, so first question… do I understand our position as auto-go-seq, and is it still the same? And second, do we want this PR?
Feel free to refresh what I said, because… I know it was a little bit Celtic.
Tyler Yahn 00:46:03 Yeah, I'm trying to remember, because, like, I feel like there was… So the configurator, I think.
Is… is kind of important for… for the configuration, like, declarative configuration?
But I think that there was another thing that we were talking about, like, I don't, I don't…
David Ashpole 00:46:30 Does this allow changing the configuration after creating the meter provider or something?
Robert Pająk 00:46:35 This is optional.
This is… this is for sure and should. It also… there is some statement that it's possible to change the configuration after it is created, but this is for sure not required.
Tyler Yahn 00:46:53 I don't…
Robert Pająk 00:46:56 Yes, this was this PR when it was introduced.
Tyler Yahn 00:47:00 Yeah.
I think this is something different than what we were talking about before here.
But I'd have to maybe take a little bit more of a closer look, because I thought that this was something that we wanted, because Maybe, maybe I'm missing… there's a few different configuration things. One of them was, like, a meter provider Or a logger provider, like, config for enabling and disabling it.
So there was, like, some programmatic way, and, like, we… we were definitely… were more in the favor of using, like, processors there, right? Having some sort of processor tell you whether it's enabled or disabled, based on, like, the… the… the SDK and how it was configured, not based on, like, some sort of, like, config that's passed to the SDK, I think.
The configurator, though, I thought was something different, though. This has more to do with the… the config… like, determining the… what the… was passed to it via, like, a… static configuration, I guess.
Robert Pająk 00:48:07 So this is, I think, described differently. This is something that the configurator gets something like, kind of Lambda with logger config, or something like that.
So you can see that, yeah, logger config record is a function which computes the logger config.
Tyler Yahn 00:48:29 Yeah, and so that's, I think, kind of the thing is, like, the logger config is, like, a function which computes the logger config, so it's a thing that takes as an input the… Well, I don't know, this is kind of weird, it accepts the following parameter logger scope. Well, yeah, okay, I guess it is set up… the logger config is, like, I guess, maybe it would be more of a factory or something like that, where it's set up from the declarative config, and from there, it will produce a configuration based on what that is set up to be?
But maybe, maybe I'm misunderstanding that, so I'd have to read this a little more.
Robert Pająk 00:49:02 The thing is that, you see here, the function must return null ified blocker config.
Tyler Yahn 00:49:08 Yeah, and I think that that's a little bit… confusing, because I… I don't… that's the thing I don't really want. Like, I don't… I don't really want to implement the logger config.
So, yeah, I'm a little confused there.
Robert Pająk 00:49:21 The current specification tells you that you have a configurator and you have something which returns the logger config, which is, you know, basically a struct, which the other part of this SDK needs to kind of, you know, handle.
It almost tells you how to implement this stuff.
Tyler Yahn 00:49:39 Yeah, exactly, and I think… I think you're right. I don't think that that's appropriate.
Right, because, like, yeah, like, this… this… this assumes that the logger config is going to be a part of the… the SDK, and there's not really a guarantee that we want… that's the thing that we want to try to avoid here, to having two different ways to configure the same thing.
Robert Pająk 00:49:58 If…
Tyler Yahn 00:49:59 So, yeah, in that sense, I think that makes sense.
But I think it… the logger config also probably needs to be made clear that this is not something that's, like, required by the SDK.
David Ashpole 00:50:13 Yeah, this feels like a means to an end.
That… Might not make sense for…
Tyler Yahn 00:50:22 For all implementations.
David Ashpole 00:50:23 Yeah.
Tyler Yahn 00:50:25 Agreed, yeah.
So yeah, I think coming back to this, you're… this looks good. It may not go far enough, is, I think, maybe what I'm saying, though. It was also… Like, we may need to include the log, Yeah, the logger config itself, as well as the configurator.
Robert Pająk 00:50:45 The thing is that if you don't have the logger… I initially did it this way for both.
But if you do not have the logger configurator, there's no place you have logger… when you can compute the logger config, basically.
Tyler Yahn 00:50:59 I think there's an imp… yeah, but I think that that may just be because… The specification doesn't…
Robert Pająk 00:51:06 Specification's kind of poorly written.
Tyler Yahn 00:51:08 Yes. We have all these, like, normative requirements and, like, recommendations and things for, like, components, but we actually don't… we're really bad. Like, there may be, like, one or two places I've seen where it tells you whether that component itself is required or recommended or optional.
And so, based on that, I think people may just imply that they think that it's required, in the same way that, like, this is implied that they think that this is required, and you're making it explicit that it's not, it's an optional thing.
So I think it, like, that may be… I think this is good, is what I'm saying, but we may need… Yeah, we may need to make it a little more specific… explicit for the logger config, but… Yeah, I mean, I think this… to answer your question, I think this is a good reflection of what the GoSig's desire is to… for the specification.
Robert Pająk 00:51:55 Okay. From the specification author or spec…
Tyler Yahn 00:51:57 perspective, there's probably gonna be more cleanup here that we need for these, like, development config types.
But yeah, anything else you want to say on this one?
Robert Pająk 00:52:15 Nope.
Tyler Yahn 00:52:16 Okay, thank you for your feedback.
Yeah.
Okay, that's the end of the written agenda.
I can stop sharing my screen here. Anybody else have topics they wanted to talk about, or other issues?
Top of mind?
Bryan Boreham 00:52:36 I'll mention it in the meeting, because I just posted a comment on a GitHub issue.
the hashing thing using FNV1A definitely led to collisions.
In Prometheus, and I… I… sorry, I commented without realizing Julius Volts had already said that. But he didn't say that we… Prometheus uses XXHash.
In almost every place.
Specifically because it is better it is less likely to give you a collision.
So, I've written that in a thing, but I… Felt I would say it to your face.
David Ashpole 00:53:21 Cool. Yeah, I'm… I think the… like, there's a little bit of discussion there, I'm not sure how much you read, but we… I don't think that anyone has seen hashes in the Go client. I know that there have been… or, sorry, hash collisions in the Go client. I know that there have been documented cases in the Prometheus server itself.
I think part of that is because… like, the… Name is actually just a label.
And so… pretty easy to get, like, a million series in Prometheus, but maybe… in our case, it's a little bit harder to get a million series on a single instrument.
Bryan Boreham 00:54:01 Yeah.
David Ashpole 00:54:01 the, like, collision.
Bryan Boreham 00:54:02 I guess…
David Ashpole 00:54:03 that we won't get.
Bryan Boreham 00:54:04 It depends on how much time you have, but the XXH hash function… This was tested quite exhaust… well, not exhaustively, but a lot. The… this sort of thing that you get where people… where, like, machines have names that are ASCII strings that are very, very similar.
the FNV hash tends to give a collision when you just change that string very slightly, whereas the other hashes Do more work to not do that, to not collide.
Tyler Yahn 00:54:43 Is that FNV1 or FNV1A?
Bryan Boreham 00:54:45 Yeah, it doesn't matter. The 1AS4…
Tyler Yahn 00:54:48 Well.
Bryan Boreham 00:54:49 or.
Tyler Yahn 00:54:49 That was… that was a really big distinction between the two.
David Ashpole 00:54:52 sub…
Tyler Yahn 00:54:54 classifications of the algorithm was, like, that… that close, initial condition was pretty sensitive for the FNV1, but the FNV1A was, like.
Specifically designed to handle that exact case.
Bryan Boreham 00:55:07 Well, it's a, yeah, it's a pretty subtle change.
Anyway, that's what I… I mean, I… numerically, Prometheus uses XXHash almost everywhere.
David Ashpole 00:55:20 It's… I think it still uses FNVA in the Prometheus Go client. Right. I'm not sure if it's just because they haven't gotten around to it, or…
Bryan Boreham 00:55:28 Yeah, I think that's because if you change that hash, then things behave differently in a user-visible way.
David Ashpole 00:55:36 Okay.
Bryan Boreham 00:55:37 the Go Client one, if I… I could be wrong about that.
Tyler Yahn 00:55:45 They have, collision detection and resolution in the…
David Ashpole 00:55:50 client, as well, so I would hope that… It's not user visible, but…
Tyler Yahn 00:55:59 the Go client for Prometheus does?
David Ashpole 00:56:01 Yeah, so they, they do… they store a list They store a map of slices.
Tyler Yahn 00:56:08 And then… Yeah.
David Ashpole 00:56:10 Search through the… the list of the ones that all hash to the same value to find the exact one.
And do a full, equals on it.
Tyler Yahn 00:56:21 PR to do that as well.
I think you might have also been exploring it.
I looked into it, and it was…
David Ashpole 00:56:27 Very expensive.
Tyler Yahn 00:56:29 Because of our… Yeah.
David Ashpole 00:56:31 Attribute set definition.
Tyler Yahn 00:56:35 That and the life cycle of… of something, and how to find out if you're gonna need… when you can clear that, I think becomes extremely hard.
Yeah, I looked into finalizers as well, but, like, that became a very troublesome, like, approach.
David Ashpole 00:56:51 So, I… I agree. Like, Brian, do you… did you, in your comment, did you leave, like…
Tyler Yahn 00:56:56 You said there was extensive testing for the XS Flash. Do you have, like, a link to that? I mean, I'm super interested.
Bryan Boreham 00:57:02 I can go look.
Tyler Yahn 00:57:05 Yeah, like, cause I… that's definitely something… I've definitely looked at a lot of comparisons, But specifics of this to, like, telemetry, I think would be way more relevant, so I would love to see, like, the details on, like, the ECHASH discussion.
If he could find it.
Bryan Boreham 00:57:22 Yeah… I know, because we actually have colliding labels in a unit test, and so somebody had to Write a program to find labels that collide.
David Ashpole 00:57:34 I did, unable to.
Bryan Boreham 00:57:36 Well, I know we sort of have a.
you know, circumstantial evidence that it was very hard to create those collisions, or, you know, it took a certain amount of compute time to do it.
Anyway, yeah, I'll go on the loop.
Tyler Yahn 00:57:58 Okay. Cool.
Yeah, I'd be interested in seeing those.
David Ashpole 00:58:01 But, yeah, I think…
Tyler Yahn 00:58:04 From, from, like, the standpoint of, like.
a first draft on this one? Like, I don't… is this something you think that we should block the rollout of this on, Brian?
Bryan Boreham 00:58:19 Like I say, I have no idea what your timescale is. I… Yeah, based on this thing that I'm gonna try and find the evidence for, I would just, like, search and replace the FNV algorithm with the XX hash algorithm, as far as I remember, but it also goes faster.
you know, I wish I had shares in it, or a meme coin, or something.
Anyway, yeah, that's what I was thinking, that it would be a simple thing, you could just swap out the algorithm. Maybe it's not a simple thing, I… I agree that these things are quite unlikely, but.
Tyler Yahn 00:59:03 Another thing is also, we've tried to isolate it, so I am also interested in finding out, because, like, we don't actually expose this hash value to end users, with the point that, like, if we ever need to change it for these sort of things, like, that was the idea. But I'd also like to know, like, how that manifests, I think, in the Go client, because, like, for Prometheus, because, like, if that is… something that we aren't thinking about right now, I think that also, I'd like to see that.
Yeah… It could also just be behavior, like you're saying, like, maybe, like, the bug of it colliding, people are relying on at this point, but I don't know.
Bryan Boreham 00:59:38 No, the… I think the reason not to change the hash algorithm is where people use it to… like, subdivide… they… they use it as, like, modulo, take the hash and then modulo to subdivide sets of metrics. So if… if I'm remembering that right, it… the FNV… Number shows up there, so the modulo… so things would kind of rehash if you changed the algorithm.
Tyler Yahn 01:00:05 Okay.
Bryan Boreham 01:00:05 And… and for… A certain amount of time during the rollout, that would be chaos.
So in… in general, that's the kind of… bottom… Level reason why we don't change the hash function.
Yeah, that's what I was referring to.
But that, obviously.
Tyler Yahn 01:00:29 Okay.
Bryan Boreham 01:00:30 matter for this PR that we're talking about, this…
Tyler Yahn 01:00:32 Right, yeah.
Bryan Boreham 01:00:33 Me rumbling.
Tyler Yahn 01:00:35 No worries, yep. Thanks for bringing it up. I look forward to seeing the evidence. I see we're also over time, so I don't want to, waste too much more. Thanks, everyone, for joining. We'll see y'all next week.
Bryan Boreham 01:00:44 Thanks.
