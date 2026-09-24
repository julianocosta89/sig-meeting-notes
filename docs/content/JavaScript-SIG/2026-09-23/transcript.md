SIG: JavaScript SIG
Date: 2026-09-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:59 Hello.
**Hector Hernandez** 01:02 Hey, Mark.
**Marylia Gutierrez** 01:14 Oh.
**Marc Pichler (Dynatrace)** 01:16 Newton.
I'm sorry if my audio is working.
No.
Nope.
I'm seeing some thumbs up. Hey, everyone.
**Marylia Gutierrez** 01:48 Thank you.
**Marc Pichler (Dynatrace)** 01:49 Sorry, e.
**Trent Mick** 01:49 I can hear you.
**Marc Pichler (Dynatrace)** 01:50 couldn't… Couldn't hear you earlier, I had, my… My AirPod's connected to the wrong.
Bing.
Alright, I will share my screen.
D.
I guess we can kick it off with, David's topic, the changes about how trace state is handled in the API.
**David Luna Bistuer** 02:29 Yep.
Okay. Yeah, so basically, long ago, we did some changes in the… There's, there's a state class.
But, there we have… turns out that we have two implementations, one on the API and one on the… The SDK, we decided to leave the API as is.
To not change the behavior, but now we're getting this… Prs.
So, I wonder if we should revisit our… think our decision, or maybe just, you know, would I just say that we are not going to do it?
**Marc Pichler (Dynatrace)** 03:08 I don't exactly record anymore, why we did the other thing. Was there a security reason to do it, or was it just, housekeeping?
Preferring the trace that validation was… No, I remember it was, like, a performance thing as well, right?
**David Luna Bistuer** 03:31 Yeah.
**Marc Pichler (Dynatrace)** 03:34 I'm… Fine, I don't wait.
To be completely honest,
**Trent Mick** 03:43 Have we deprecated those things in the API already, or not?
**Marc Pichler (Dynatrace)** 03:49 I think so, yeah.
**Trent Mick** 03:55 like, I don't have a strong opinion, but if we've depicated already, I'm inclined to just, like.
Don't need more changes, especially if it's not for a correctness issue.
**David Luna Bistuer** 04:09 Former PR duplicates the… the implementation on the API, yeah.
**Marc Pichler (Dynatrace)** 04:21 Yeah, I guess we could just, State on here that people should not use it.
Or maybe we just add a comment here to say this will not receive any fixes or updates.
And we can just leave it at that.
And then we closed the two OPRs that are open right now. Because… Core is what's supposed to be used, and we should be good.
**David Luna Bistuer** 04:55 Okay.
**Trent Mick** 04:56 Is this, like, this person was… Do you get the sense that they're fixing some problem, or they're just… Looks like these things were inconsistent, so let's carry it over.
Dunno.
Hmm.
**Marc Pichler (Dynatrace)** 05:19 Yeah, of course, I'm not sure.
I'll put the comment on here, and…
**David Luna Bistuer** 05:35 So, in a way, maybe it's something where it's talking about truncating, which is defined in the spec.
So, yeah, you can argue that it's a bug fix, because, you know, the implementation in the API doesn't determine the proper truncation based on the spec.
But then, also, we're changing behavior, so… one PR is doing the truncation, and the other one is just also with the truncation is… Affecting the order of the, of the entities.
So… It's a fuzzy line.
It's a broader lines.
**Marc Pichler (Dynatrace)** 06:20 there.
Are there any interactions where using one or the other?
could cause things that are difficult to debug, maybe?
But because the behaviors are different, maybe there's two apps running different versions of the same thing, one is using the deprecated Thing, and the other one is using the one that we changed, and then people are wondering Why things are slightly different.
Depending on these versions.
Well, Subaru, right?
Yes, if it's easy to just copy things over and adapt the tests, we could just… Verify that it's the same.
merge it in, and then do a bug fix release.
If it changes behavior, the next release for the API will anyway be 1.10.0, so it's a feature bump.
Wouldn't… be… Cool.
Bad if, like, some of the behavior changes.
I would say. So… I'm gravitating towards, just merging it in and having the things aligned, and then if somebody checks it in the future, they won't see that it's different and raise another PR, and then we should be hopefully done for good with this.
But, we'll see.
I'll review these, and make sure that everything's in order, and then I'll merge those in.
So that's okay with everybody.
**David Luna Bistuer** 08:25 Yeah, that's okay.
**Marc Pichler (Dynatrace)** 08:27 Sure, as soon as I've done.
Should be… Fairly straightforward to get these in, I think.
I just want to just… Sent myself to… explore that myself, too.
Yep.
Right.
there's no additional comments to this here, then I guess we can move on to the next one, which is, Enough.
Adding support for…
**Pranav Sharma (Google LLC)** 09:15 Sweet.
**Marc Pichler (Dynatrace)** 09:15 locations in the genre used to say.
**Pranav Sharma (Google LLC)** 09:18 Yeah, this is just a request for reviews, just wanted to bring this to other people's attention. This is the work required for the GenAI Utals Library, and I think this is the second last PR, and the last one is going to be very small, so we're almost wrapping up the work here.
So, just wanted to get some reviews.
**Marc Pichler (Dynatrace)** 09:43 Yes, thank you for working on this. I'm not sure I would have time, but I see Jackson is already on it. Yeah.
I think the last one I merged in… after Jackson gave his approvers, so, I'm…
**Pranav Sharma (Google LLC)** 09:57 Right.
**Marc Pichler (Dynatrace)** 09:57 just going to do the same here.
**Pranav Sharma (Google LLC)** 10:00 Okay.
**Marc Pichler (Dynatrace)** 10:00 you see the approval and it's not merged, please feel free to ping me and I will merge that as soon as possible.
**Pranav Sharma (Google LLC)** 10:06 Alright, thank you, Mark.
**Marc Pichler (Dynatrace)** 10:09 Thank you for working on it.
Alright, any questions or comments about this, Jenny or YouTube's work?
If not, then we can move on to the next one, which is… A topic by Trent, a pull request… Widen the attribute values.
It's not ready for review.
Looks like Jackson also already reviewed this one. I will also give that one a go.
We need at least one maintainer approver.
Additionally for it, because it's an API change.
Yeah, I will, look into that and see if the failure mode that I was talking about could happen with this.
And… yeah, we'll also put my comments on this PR, if that's the case. Maybe somewhat related to that, we can also… probably doing a pre-release of the API, because I… changed the release PR workflow to also allow pre-release versions, and I did a little fix-up in the… Rosa.
Bundler tests to… Use the development version.
There, so we can actually… Let people try this out if they want.
Which I think would be a good idea in this case for this change.
**Trent Mick** 12:01 On that, I would love to get an API release that had the API, or the attributes widening.
In it. And then maybe also the… I'm happy to update the PR or do a new one to move API logs into API, if we're considering that, at least to try it as a pre-release and see if things look okay there. If we're agreed that we want to do that for the September release, like stabilized logs.
**Marc Pichler (Dynatrace)** 12:26 I think it would make sense to do it, if we can get it in, I'd also be fine with delaying for a week or so to wrap up extra work. Like, at this point, I think we might also have to consider, like, all the documentation and stuff that needs to be done.
So, maybe we push back the actual release date for a week or so.
**Trent Mick** 12:58 Do you mean specifically for logs, or do you mean all the, like, OpenTelemetry I.O. changes for…
**Marc Pichler (Dynatrace)** 13:03 Yeah.
**Trent Mick** 13:03 3.0 and SDK Trace.
Stuff. Okay.
**Marc Pichler (Dynatrace)** 13:07 Since we have to do that anyway, we might as well also use the remaining time for… The log stuff and get that in.
Okay. I wouldn't be… too unhappy about that, I think.
As long as we… Then make it land sometime.
Before mid-October, I think we should be good.
**Trent Mick** 13:33 Okay. I mean, I'm happier to be more aggressive. I think I could get the… If someone's able to look at the one that you're highlighting on there, the attributes one, I got an approval from Jackson.
If we could get… Turn around from that in the next little bit, or another review.
At least on that one, it'd be great. And then, I could do the… work on the PR for… moving API logs and API soon, so we could have, like, theoretically have that this week, or early next week.
**Marc Pichler (Dynatrace)** 14:05 Artex, I said earlier, I will take some time to have a look into this and see if the things that I'm concerned Or that I was concerned about, are addressed by this or not, okay.
And,
**Trent Mick** 14:19 I mean, I know even with this, you're still gonna have the lingering concern that we are widening the type, and…
**Marc Pichler (Dynatrace)** 14:24 Yeah, the potential.
**Trent Mick** 14:24 Central.
**Marc Pichler (Dynatrace)** 14:26 If one of the other… if one of the other maintainers gives it a review, I might just look the other way and merge it.
**Trent Mick** 14:39 And I'll do the same for removing the re-exports from SDK node when you do that.
**Marc Pichler (Dynatrace)** 14:46 Alright, dear.
Yeah, so if anybody else wants to have a look at this, I'd be very happy if you do.
And… Do you think we should wait for the API pre-release until this is merged?
Or, should we do an API pre-release in the meantime?
**Trent Mick** 15:14 I'd kind of lean on you for that. I don't know how painful it is for you to do another pre-release. Would you prefer to wait, or would you prefer… happy to do a second pre-release?
**Marc Pichler (Dynatrace)** 15:24 I'd be happy to do a second pre-release, so, I… just made Autobot create this PR here, and then I just pushed one more commit that adds the overrides for… oops.
That's the overrides for, Next.js, because they depend on OpenTelemetry API 1.1.0, with a caret version, but the pre-release version does not match Carrot, so… It needs to override here. Other than that, the PR is… Or auto-created, and… And I'll adds these… Let's see additional things to it.
when we finalize, these will be removed again, so… It's not a lot of work, we just need to merge this in, and then, run the release workflow, and that's it.
**Trent Mick** 16:27 Yeah, I mean, I'm totally fine having two if you're… I'm not confident I can run these mechanics on my own, but… Without screwing something up, but… yeah.
**Marc Pichler (Dynatrace)** 16:38 should RP automatic, there's no way, I think, to…
**Trent Mick** 16:45 Oh, you gotta catch yourself.
You say that, there's no way to screw it up, yeah, right.
**Marc Pichler (Dynatrace)** 16:49 There probably is a way to do it, I just haven't run into it yet. I'm hoping that it will stay that way.
But… yeah.
**Trent Mick** 17:00 While we're here, can I ask you one question on the diff for the widening the attributes PR?
If you can open up the changes… Not this one.
Yeah, that guy.
Go look for package.json files changes.
Okay, so there I have a question. If the changes I'm making here to the open So this is an update to the dependency and or peer dependency on the API package for any packages that are using the new attributes type. Does that look right, what I'm doing here? Obviously, we'll have to update that from… to 1.10 when we have a 1.10 release, but…
**Marc Pichler (Dynatrace)** 17:47 Yeah, I like that.
**Trent Mick** 17:48 This is kind of expressing that the latest state in the repo, you need that to…
**Marc Pichler (Dynatrace)** 17:54 I think that looks right. I haven't looked into how these changes are structured exactly, so… I suppose they're using this new any value type, right?
**Trent Mick** 18:07 Basically, attributes now uses any value, so anyone that was using.
**Marc Pichler (Dynatrace)** 18:11 Thank you.
**Trent Mick** 18:11 And… Yeah, needs to cope with any value needs to update.
**Marc Pichler (Dynatrace)** 18:17 If we're not using any value directly.
I think we wouldn't even need that.
Because… Any value is unknown.
So… If we update our implementation, it will work for any previous type as well.
Because we are treating it as unknown.
**Trent Mick** 18:49 So the implementation is fine. I can't remember if I had a… like, so I tried… I created a side test case where I had an app.
That was… now I have to go check again exactly how much I… but using an older API?
Installed.
And the newer… I have to check what I… okay, I mean, if that's the case, then maybe great, but… I'm a bit hesitant.
But certainly for the ones that are using AnyValue directly.
And I think a lot of them end up doing so.
**Marc Pichler (Dynatrace)** 19:30 Yeah, certainly the ones that use any value will need the…
**Trent Mick** 19:37 dependency update, yeah.
But as we said, for this release, having the dependency update is fine, right?
**Marc Pichler (Dynatrace)** 19:45 Yeah, should be.
**Trent Mick** 19:46 in nature, if it needs a new API, so be it.
**Marc Pichler (Dynatrace)** 19:54 Alright, I will have a look at that. Overall, I think the bump is okay. We can still play around with relaxing that later if we need to, or if we see that it would work, there's nothing that prevents us from Widening the range into the past.
It just… It won't break any… anyone.
Additionally, if VIN 3.1, for example, we decide to hey, we… see that it would actually work with 1.3.0. We can just widen that later without… too much pain to everybody, so… I think it should be fine.
The next topic,
**Trent Mick** 20:53 I'm muted, sorry. The next point, the one without a link that you're hovering on.
I started on changes to… get rid of the usage of SDK trace node in the contrib repo, and it's basically all in examples. And some of those examples, boy, they're old, they're still using SDK1.x.
So, this is for everyone in the house. How… Unhappy would you be if a bunch of those examples just got removed?
I started working on the Redis example, for example, updating it, and it's quite a lot of change to get it Updated to work, with 2.x, and then basically in prep for 3.x, just means not using a skeetrace.
But if a bunch of them just went away, is that gonna make anyone too sad?
The Express one I'm keeping, I think that's important. That one was already updated to 2.x. The other ones are all basically up for debate. Okay, I got lots of hearts and claps, so I think people will be fine with it, just…
**Marylia Gutierrez** 21:55 Yeah, just one question.
**Trent Mick** 21:56 That's too much work.
**Marylia Gutierrez** 21:57 Do they… any of these exist on the, .io?
Just saying, like, if there's anything that needs to be removed there to keep everything in sync.
**Trent Mick** 22:06 Okay, that's fair. I'll make sure to check. So I was doing this as a first step, and then next step is going to Opentelemetry.io and updating docs. They're using SDK Trace Node or SDK trace base to get ready for just the SDK trace.
So I'll… I'll… That's the next step, is looking there, too.
I'll make… I don't know if any of those are pointing to specific examples in OpenTelemetry I.O, I doubt it, but I'll make sure that we don't create a dead link for the OpenTelemetry I.O. docs.
**Marylia Gutierrez** 22:33 Yeah, yeah, so yeah, that was the only thing that I would say, just keep things there as well.
**Marc Pichler (Dynatrace)** 22:41 I was just looking into if there's an example category in the… registry, but also doesn't seem to be that way, so…
**Marylia Gutierrez** 22:51 No, I would say it's more like, yeah, if you go, like, right here, there you are, go to, yeah, languages and API SDK.
**Trent Mick** 22:58 Also, under the zero-code instrumentation, there's.
**Marylia Gutierrez** 23:01 Yeah, and then you're gonna have, like, yeah, getting started by example, example, so that would be the place that…
**Trent Mick** 23:06 Where does that examples link go to? It links out.
**Marc Pichler (Dynatrace)** 23:15 That's,
**Marylia Gutierrez** 23:16 Okay, yeah.
**Marc Pichler (Dynatrace)** 23:17 Examples in core. Yeah, but I think it's still worth checking. I'm fine with removing them, ideally all of them.
**Marylia Gutierrez** 23:26 Yeah, if you're gonna, like, break, we're gonna have, like, the link itself is sort of gonna start breaking when people open, like, new PRs, so we will catch that, but it would be… yeah.
Something to keep.
**Trent Mick** 23:40 Yep. Okay.
I'll check for that. Because I know we don't actually catch that stuff with link checks.
Either anyway, because that's hard now.
Because link checking DOS is GitHub, so GitHub links are basically not checked, so… yeah.
**Marylia Gutierrez** 23:53 Yeah, it's more like on the .io, we have a bunch of, like, the cache for, like, all the references and stuff like that, that we need to make sure that it's, like, updated, so depending on where it's pointing, it might then give the error or not.
**Trent Mick** 24:07 That's the Lychee cache file? Yeah. That lychee cache. Okay. Do you know how to update that properly? I didn't…
**Marylia Gutierrez** 24:14 Oh, you just, like, whenever you get an error, you just comment, like, fix, ref cache, and then it's gonna fix for you. So, if you hit the error, it's gonna, like, click, and usually tells you which comment you have to add.
**Trent Mick** 24:28 Okay, cool, thank you.
Right, David, so you talked about web, that's two bullet points later in the agenda. Maybe we'll skip the 6999 one for now.
move to the next one. So yeah, when I was in Contribo trying to remove SDK Trace Node and SK Trace Usage, there are lots of SK Trace Web ones, which are hard to replace right now. The best we can do is stage it, because any usage of The web tracer provider is using the stack context manager, which we haven't yet had a published release of something that does it, so we can't move those examples over yet. So I'm guessing maybe the state we're in is that SK Trace Web cannot go away unless we stage it all to happen at, like, close together. That or SK Trace Web I don't know.
**Marc Pichler (Dynatrace)** 25:23 Oh.
**Trent Mick** 25:23 Actually, maybe what can happen is we don't publish skraceWeb 3.x.
And we do the 3.0 release, And the examples in Contrib and some tests are still using SK2Sweb 2.x, but the process of us doing 3.x-enabled stuff in Contrib is going to move all those things over, so maybe that's stuff that has… Yeah, I guess Contribo can't move up to 3.x until we do the 3.x release anyway, so maybe it's just we need to do that later and relatively quickly, so maybe it's all fine.
We just can't do it ahead of time.
**Marc Pichler (Dynatrace)** 26:00 Yeah, one thing that we could do ahead of time is… Change the setup to be without register.
And still importing the stack, context manager from SDK TraceWeb.
**Trent Mick** 26:19 I got you, then it's clear, there's less of a death.
**Marc Pichler (Dynatrace)** 26:21 Yeah, then the last step is just changing the SDK trace web import.
to SDK Trace.
And we can still continue to release from Contrip in the meantime.
Without running into trouble. One of the other things that we can do to prepare for the 3.0 release is we can start a PR that pulls in the Pre-release that we have out right now.
Earlier this year.
**Trent Mick** 26:53 Just run tests against that, yeah, yeah.
**Marc Pichler (Dynatrace)** 26:55 Yeah, so we can run tests against it, we see what breaks.
And we can start fixing these things, in that PR already.
And then once we're ready to release, we merge that.
And… then we do another PR that just updates the versions to remove the… pre-release identifier.
**Trent Mick** 27:22 Yep. Okay. Do you know… sounds good. Do you know if we have a pre-release with the stack context manager moved over to SDK Trace yet, or not? I'll go check.
**Marc Pichler (Dynatrace)** 27:31 Thanks.
**Trent Mick** 27:32 I don't know if… I don't know if we'd do.
**Marc Pichler (Dynatrace)** 27:33 It should be already in there, but… I'll say no.
**Trent Mick** 27:56 No, it's… oh, yeah, we do, actually. The development.zero has it, so we're good.
Perfect.
**Marc Pichler (Dynatrace)** 28:02 Yes.
So, yeah, maybe, as an FYI to everybody on the car, You can now install this, canary version of… To read it all, and test things out if, you're looking to see how changes behave.
In your apps, or… or… Tests, or whatever you have.
Outside, of that repo.
The idea was mostly to help Pondrip move along, but also, Might be interesting for browser… for the browser repo.
to see if there's anything that breaks, and also get the PR started to update so that it's a bit more smooth when we actually get to releasing through the door.
**Trent Mick** 29:01 Okay, so backing up one for a second to 6999.
Review's welcome on that one, that one's been stalled for a while.
**Marc Pichler (Dynatrace)** 29:12 Yes.
I'm sorry.
**Trent Mick** 29:14 I need to spec it in.
**Marc Pichler (Dynatrace)** 29:15 I was missing, too.
Look into that one, but… Didn't have time, unfortunately.
**Trent Mick** 29:23 This doesn't need to happen for 3.x, so I understand why there's a delay now, so… And if Matt Ware's on the call, or if he or Rage quit earlier, I still haven't done the config provider.
Next review.
Okay, so then on the SK Trace refactoring stuff, which I think is kind of the majority of the remaining tickets on 3.0, so that's why I'm… Hammering it with multiple bullet points here.
Do you think we could delete?
trace, node, base, and web from main now? Like, we're not gonna publish them in 3.x, right?
And by delete, I'm thinking I'll probably put a placeholder README file there, so that people that land there at the top page have something like, what the hell's going on?
At least for a while, so say, hey, this stuff's… gone, here's Y, here's the pointer SK trace, and here's the pointer to the… to the last… release sources.
**Marc Pichler (Dynatrace)** 30:38 Yeah, I think we can, go ahead and delete it.
I'm not sure if there was a PR for deleting one of them already,
**Trent Mick** 30:51 Oh, okay, I'll check, yeah, I can't remember.
**Marc Pichler (Dynatrace)** 30:55 Yeah, I think we can just get rid of them. We might need to call it out in the… migration dock.
But I think the document that you wrote print, on migrating to SDK trace is already a good… Resource to point people to.
Was it… I'm not sure if I misremember.
I think it was you, right?
**Trent Mick** 31:22 Okay, I actually feel a little bit stupid, because I think I had the PR that deleted SDK Trace Node recently. It was the first one, did it. So yes, I did. SDK Trace Node is gone already. SDK Trace, the README, had docs that I wrote for migrating from each of the other three to SDK Trace. When I delete a SK Trace node, I move the migration doc for… I'm migrating from SK Trace node from the SK Trace README over to the migration doc that has been started. And I'll do the same for the other one, so that, like, that's the natural place for people learning how to migrate stuff.
And I'll make… I'll put the placeholder READMEs I guess I'll add one for SK Trace Node, because it's gone now, so, because I just deleted it. Anyway, yes.
And it got in my face.
Okay, so I can start following through on that. I'll do some sanity checking on base first, because… I don't know why I haven't done it yet. Node is… there's no SK Trace Node usage in Core at all right now, I don't know about base. I assume not, but…
**Marc Pichler (Dynatrace)** 32:27 Sorry, I think I didn't get the last part.
**Trent Mick** 32:33 I'll… I'll have to… before I remove SDK Trace Base, I'm gonna have to sanity check why I hadn't done it already. SDK Trace Node was the easiest one to remove, because… Yeah. Go ahead, David.
**David Luna Bistuer** 32:47 Talking, talking about removing the Z Gutierrez vase.
And I've seen that there is a lot of things on examples, maybe you can update two examples to use the browser SDK.
Then we just completely get rid of any… SDK, trace, whatever.
Import, and there's examples, and we are showing.
How it's done right now, with the… Within a browser package.
Is it?
**Trent Mick** 33:14 Hold on, I'm checking.
Something.
**David Luna Bistuer** 33:17 They didn't contribute, you have, 4 or 5 instrumentations for browser.
they're compatible with the… with the browser SDK.
**Trent Mick** 33:28 That are compatible or incompatible?
**David Luna Bistuer** 33:30 compatible.
They can be used.
now that I'm thinking out loud, maybe we'll be incompatible in the future.
I don't know.
Something that we need to maybe to discuss in the browser SIG, but for now, it's compatible.
instrumentations, former instrumentations and instrumentations in the browser both have the same API right now, and they extend The instrumentation base.
So…
**Trent Mick** 34:19 Wait, so, I go look in Contrib and look at anything using SDK Trace Base.
And it's only examples, and none of them are browser examples.
Other than the examples of React Load, which is what PR asked about in… or I…
**David Luna Bistuer** 34:35 Or do you have to come in loads a long task?
**Trent Mick** 34:41 But, I mean, those are using… so… instrumentation, long task.
**David Luna Bistuer** 34:47 Well, at least they see in the Redmi, they're using.
**Trent Mick** 34:50 So… SQ.
**David Luna Bistuer** 34:52 Truth Web.
**Trent Mick** 34:54 Yeah, which… which she uses space, granted. And tests.
So yeah, that was the kind of stuff that I expected after we do 3.0 release, getting the big PR, or PRs, following up quickly in Contrib is to get them all moved over.
Because when they move up to 3.x, there won't be an SDK trace web.
So… to move to something, and we're confident we have this thing to replace, so we can do that middle ground prep work, stop using the .register method that Marc said, but…
**David Luna Bistuer** 35:26 Yeah, maybe then we can just queue up those PRs, and then go through this.
Yeah. Okay.
**Trent Mick** 35:32 the thing where I think it's worthwhile to look at updating docs to move to the browser SDK, and this is maybe a question for whether the… for all the browser folks, and whether you guys feel it's ready, do we update the OpenTelemetry.io docs for browser instrumentation and usage over to the browser SDK now.
away from SDK Trace Web.
Are we ready for that?
**David Luna Bistuer** 35:57 Let me do this.
That's a good question.
**Trent Mick** 36:01 Okay, I was hoping for an emphatic yes there, but… Jared?
**David Luna Bistuer** 36:10 I think that we need… still… there's still work to be done. Maybe we're close, maybe?
**Jared Freeze (Palo Alto Networks)** 36:15 Yeah, there's a lot in flight this week.
Including interactions with register instrumentations.
So, saying compatible or incompatible may not be the same answer next week.
**Trent Mick** 36:29 Okay.
**Jared Freeze (Palo Alto Networks)** 36:30 There's a lot… there's a lot in flight, including docks, so, probably next week we'll have a better answer.
Even emphatic.
**Trent Mick** 36:42 I think that's cool. Like, I mean, I don't think it's the end of the world if OpenTelemetry.io docs for web are still using 2.x stuff for a short period of time, so that's fine.
Okay.
Thanks.
**Marc Pichler (Dynatrace)** 37:02 maybe… If we delay the release of 3.0 by… A week or so.
We might be able to… See where things are headed and, make a different decision as well.
We'll see how far we get.
**Trent Mick** 37:28 Do you think, so… With Marc what you're saying, and Jared, your thumbs up, do you think it's possible that we would want to keep SDK TraceWeb alive in 3.X?
**Marc Pichler (Dynatrace)** 37:45 So, my understanding was SDK TraceWeb goes away anyway.
Okay, and that's…
**Trent Mick** 37:50 Just, people can use the old-style instrumentations, but they do it by manually using SDK Trace.
**Marc Pichler (Dynatrace)** 37:57 Yeah, exactly.
That was what I was thinking about, and then, like, as a stretch goer, if, like, documentation is ready for the browser SDK and instrumentation stuff.
Instead of recommending people, hey, switch from this… to, like, a manual setup with SDK Trace.
consider migrating to Browser SDK.
**Trent Mick** 38:25 Instead of two changes.
**Marc Pichler (Dynatrace)** 38:27 Yeah, instead of doing two changes, because then, like, you're already on the thing that's gonna be… The way to do it in the future.
Okay.
**Trent Mick** 38:39 Okay, gotcha.
**Marc Pichler (Dynatrace)** 38:39 And, yeah, we don't need to tell them again to move over. We can still have, we can still push it in a way to say you can use the browser SDK if you absolutely have to keep the old way around, this is how you do it with SDK Trace.
But… I would prefer having the browser SDK as the main path of migration.
**Trent Mick** 39:17 Okay.
That's good.
**Marc Pichler (Dynatrace)** 39:43 milestone where we're talking about Riddle.
Unless anybody else has something they would like to bring up.
Oh, the Jager Export, at a PR, I think,
**Trent Mick** 40:11 I saw the last PR for OpenSelectree I.O. dropping… That package from the… registry thing.
Is that something you could review, Marylia, or…
**Marylia Gutierrez** 40:37 Lisa.
**Trent Mick** 40:37 I'm not even sure how relevant it is, but…
**Marc Pichler (Dynatrace)** 40:46 Looks like I don't have any power there.
**Marylia Gutierrez** 40:48 So, I'm just saying, like, where… which folder you're trying to change? Can you just…
**Trent Mick** 40:53 Oh, and the data registry, which I'm not even sure… there is a script that's undocumented for updating these entries, and I also saw there's some discussion about, like, just freezing this and not.
**Marylia Gutierrez** 41:04 Yeah, so this is what I'm saying, like, yeah, so this is what I'm saying, like, I don't think I… we are merging anything related to the registry, we just froze everything, so this is… Probably, we're gonna get… this is gonna just get closed.
**Trent Mick** 41:20 Is, okay, is there… Not that we need to know that here, but do you know offhand if… what the plan is for changing the registry?
The whole thing.
**Marylia Gutierrez** 41:30 Then…
**Trent Mick** 41:30 before I'm playing.
**Marylia Gutierrez** 41:31 So yeah, depending on the area, so, for example, if it is just, like, third-party tools, they want to say they are, like, hotel native, we are not planning to do anything about this. Like, if people are interested, they can create something new, because we just don't have people to actually maintain this.
And then, so for the things like internal, we do have Ecosystem Explorer that we're planning to have a bunch of things there. There is a blog post that will come out that we are explaining what is the next steps here for things that will move to… to that one. But yeah, that is kind of the, like, nothing will exist on this repo anymore related to the registry.
**Trent Mick** 42:13 Okay, so I think I'll… Going back to our 3.0 milestone issue, Mark.
I'll write a comment on there, but we don't need to wait for this thing, because…
**Marylia Gutierrez** 42:24 No.
**Trent Mick** 42:24 things going on with data registry, and I think we can just… then I'll close this issue, because I think we're done. That one.
**Marc Pichler (Dynatrace)** 42:32 Thank you.
That dropped. There's this… amethois thing, which I haven't gotten to refining the issues yet. I was talking… Last week about, Making sure that we do the large breaking changes first, and then defer the rest to after 3.0.
I haven't gotten around to refining that yet.
Yes, sir.
**Trent Mick** 43:13 Is there anything that needs to happen for 3.0 here?
**Marc Pichler (Dynatrace)** 43:17 I think the one that needs to happen, we already merged, which is… Default host to localhost.
**Trent Mick** 43:27 I remember.
**Marc Pichler (Dynatrace)** 43:28 That's the thing.
We might also want to look into removing environment variable configuration, because the Prometheus Exporter can be set up via declarative config.
**Trent Mick** 43:40 That went in earlier this week.
**Marc Pichler (Dynatrace)** 43:43 Perfect. Then…
**Trent Mick** 43:44 I didn't… I didn't know if there was an entry here, I don't think it's been updated here, but yeah, someone had a PR to update that. For the new Node SDK path, the current state of the Configuration package generating config for… Environment variables does the right thing.
And my… ER waiting in the wings, the 6999, I think does the right thing as well.
So… so we're good there for that one.
**Marc Pichler (Dynatrace)** 44:12 Right.
Yeah, I think the rest is, Or something that just adds to… Compatibility.
Make this version and format.
Thing with the… Negotiation.
Art.
To just increase compatibility. And then we have this, Host thing, which is now fixed.
I think this also was changed already, I have to check, But in any case, this is also, Like, additive change that doesn't break anybody.
This content negotiation thing is also something that… Just widens the features that exist, so that should also be fine.
That's not applicable. So, I think there's… not really anything to do anymore for this. I double-check, and then I… Move it out of the meristone.
Yeah, this one should be fairly simple. I'll remove these. I actually do that right after this meeting, so that I don't forget about it.
Once… the PRs are merged to remove the SDK trace packages, then this is also done.
the consolidate SDK configuration. I don't recall exactly what this was about.
Looks like we talked about it 3 weeks ago.
**Trent Mick** 46:12 I think this is basically covered by the whole… Declarative config work.
I think, but I'm in the same state. This is an old one that I haven't looked at in forever.
Yeah, I think this is talking about… For any of the declarative config.
Work wisdom.
**Marc Pichler (Dynatrace)** 46:36 Oh, the only thing that will be still reading environment variables is, are the exporters, right?
**Trent Mick** 46:45 Yeah, so there's the… there's a separate issue on the milestone for that.
And I'm thinking that we leave that one as a known issue, and we'll come back to it.
where I'm guessing after the dust settles here, one of the top-pinned issues is gonna be… because we talked about major issues that we wanted to do was… Stabilizing the exporters, so that means some serious work there.
**Marc Pichler (Dynatrace)** 47:10 Agreed.
In that case, I'm… I would consider just closing this.
And saying, like, putting a note on there that we have decided that no packages should read environment variables directly, Anything… configuration related should happen in SDK node.
And, SDK configuration.
we… Like, if there's work to remove stuff, then that is the decision that we made.
And… You can just go ahead with it.
Write it down, in later as well. So then we should also be done with that.
And we have this ad network.
Span events thing.
We just need to mark these as deprecated in a webcommon.
So, it looks like there's just… Fairly small things that need to be done still.
Then this one is new, this is the thing that we talked about last week, removing the… The browser field…
**Jared Freeze (Palo Alto Networks)** 49:07 Yeah, so this is… this is already in flight, I have it on a branch. I think it's also assigned to me, hopefully.
**Marc Pichler (Dynatrace)** 49:15 Yeah, it's assigned to you, so, yeah, looking forward to that, and then we can also merge that in.
**Jared Freeze (Palo Alto Networks)** 49:23 Yeah, I want to try to catch the next release, so I can test it on the… two SDKs we've got.
On the vendors.
**Marc Pichler (Dynatrace)** 49:33 Yeah, sounds good. The… publishing a pre-release is actually fairly quick, so once we merge it in, I can just… Cut, release should be fairly… Very quick to-do, so…
**Trent Mick** 49:50 Or if it's my time zone, I can try to do it too, Jared.
**Marc Pichler (Dynatrace)** 49:55 We just need… we just need two people online at the same time, which is the main, main, difficulties sometimes.
Alright.
I guess that's Arden.
This one we already talked about.
And I also added the fine to remove the overrides.
When we published the 3.0 release, and that's it for 3DL.
**Trent Mick** 50:32 Thanks.
**Marc Pichler (Dynatrace)** 50:36 Actually, a lot less work left than I thought, but…
**Jared Freeze (Palo Alto Networks)** 50:42 There is one other thing, I'm not sure if it's documented exactly, but, you recommended we mark everything as deprecated?
All the web packages in… Contrib, as well as Core, is deprecated right now, even without updating docs and, like, linking to the new one.
Since they are different data models.
I'll go ahead and do that. I don't mind doing that, unless David wants to pick it up, but… I don't… I didn't see it on the list, so maybe it never got an issue.
**Marc Pichler (Dynatrace)** 51:17 Yeah, that's true.
**Trent Mick** 51:18 discussed.
**Marc Pichler (Dynatrace)** 51:18 That's an issue.
**Trent Mick** 51:19 Does the instrumentations we're talking mostly, right? Instrumentation, fetch, XHR, that kind of thing? Yeah.
**Jared Freeze (Palo Alto Networks)** 51:25 That's exa- yeah.
**Trent Mick** 51:28 Okay, yeah, agreed. Sorry, I was gonna do a slightly related point.
the plugin React load?
thing that I asked about on Slack the other day, I seem to get general agreement from people that we don't need it, and Martin, for example, saying deprecated. Now, do we… delete that for 3.X?
Or is that too harsh to deprecate them or delete within a week?
Like, seriously, is anyone using that thing? I can't imagine.
**Jared Freeze (Palo Alto Networks)** 51:58 I don't think it gives you useful information, not to denigrate the entire content of it, but the lifecycle of every component on a given page, is a lot of information, and I'm not sure how useful it is. I think it's better to sort of pinpoint, like, what exactly you're trying to figure out. So, how long it takes something to render is… on its own, I'm not sure how useful it is. Also, you said it's, like, 200 a week, so… I think anyone who's upgrading, and if we're also saying, hey, go to the browser SDK, That's not compatible anyways.
So, I think it's… I would say delete. That would be my choice, is just let it go.
**Trent Mick** 52:45 Cool. I'll do a separate issue for that, what the argument's for, and then… That's the handle people can use to revive it if we need. Can always bring it back.
Thanks.
**Marc Pichler (Dynatrace)** 52:57 Okay, sounds good.
Hold on.
It looks like, we have global topics, and milestone.
**Marylia Gutierrez** 53:15 Actually, let me just provide… I want to share just a few updates. I don't remember if anyone here asked about this, but it's something that keeps coming up on other SIGs and from other maintainers. We do have the official list of, like, maintainers, the list, like, on CNCF.
It's usually, like, list only GC and TC.
But people wanted to see all the maintainers listed there, because it also can help with, like.
submission on stuff in, like, maintainer summits and stuff like that, you have to be part of the list to submit. And there was, like, some limitations on… because of, like, service desk that could not… we could not add everything. But now I just have the PR up that now all maintainers will be listed as OpenTelemetry maintainers, officially for CNCF.
Not sure if this gives you anything, any particular access and things like that, but at least it's good to have the recognition and also be able to, I guess, send talks on Maintainer's Day and things like that.
And the other dates, just freshly news, we do have new TC members that were backfilling the two that recently left. They just got elected, PRs are up, so is Alex Bolton and Robert. So… they… it's not affecting this SIG, because Carlos is the TC for this SIG, so it's not gonna affect, but in case you work on other SIGs, it might change who is your sponsor. If yours was one of the people that left, you might get one of the new ones coming up.
**Marc Pichler (Dynatrace)** 54:57 Thanks for the updates there. I thought Robert was already a TC member, so it's very fitting that he got elected to the TC.
Nice.
Alright.
What topics?
M… Thank you, everybody, for joining.
Have a nice week, and see you next week.
**David Luna Bistuer** 55:31 Yeah. But…
**Marc Pichler (Dynatrace)** 55:33 Right.
