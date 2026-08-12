SIG: Arrow SIG
Date: 2026-08-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Laurent Quérel 00:01:52 Hey, everyone.
Aaron Marten 00:01:58 beep.
Tom Tan 00:02:03 Hello?
Laurent Quérel 00:02:04 Hello?
Joshua MacDonald (Microsoft) 00:02:12 Hello.
Laurent Quérel 00:02:16 Okay… Soon.
Maybe I will reduce it a bit the size of this window to… Make it a little bit… more visible.
big enough?
Okay, so I encourage everyone to add their name to the attendees list.
And, to add some, A topic for discussion into the agenda.
Okay… Joshua, do you have any, maybe initial, Thoughts to mention, or we go directly to the triage?
Joshua MacDonald (Microsoft) 00:03:19 I… Don't think I do. As you know, I'm still working on the multi-tenant design, and I'm not ready to present anything.
Laurent Quérel 00:03:31 Yep.
Okay, so, I was surprised, when I click on this link, usually we have all the… the… the new GitHub issue that needs discussions.
And, I don't know if we changed the way that this, the authorized segment of the need distribution label Is done now or not, but I think we have much more, if I am looking at… these lists… And if we have, Drew, or maybe Tom is aware of that. Do… or maybe Aaron, do you know why… Some of the entries that we have here are not… Labeled with the need… need discussion?
I don't remember what we… How we assign automatically this label, because now we have this list with only, or maybe the…
Joshua MacDonald (Microsoft) 00:04:39 I think someone's been triaging.
Laurent Quérel 00:04:40 Oh, okay, so now it's better… Huh.
Okay.
Joshua MacDonald (Microsoft) 00:04:47 Is the link broken? Because the… Triage needs discussion label is working, as you see.
Laurent Quérel 00:04:55 Yes, and I opened… basically what I did before, in preparation for this meeting, let's say 30 minutes ago.
I opened the link that is there.
And and before the… I refreshed this page a few seconds ago, I only observed two, these two. So I don't know how we… All those things have been, automatically assigned, but that happened…
Joshua MacDonald (Microsoft) 00:05:18 Hub is having a bad day.
Laurent Quérel 00:05:20 Yes.
Okay, so much.
Tom Tan 00:05:23 Yeah, I think the problem is I just added some of them, put them at the label maybe half an hour ago, so maybe that's maybe…
Laurent Quérel 00:05:31 Oh!
Joshua MacDonald (Microsoft) 00:05:32 Oh, there we go.
Okay, one minute.
Laurent Quérel 00:05:35 Okay.
Okay, so, so I think we all… this one is still an ongoing effort. I'm not sure that we have to spend, for now, too much time on that.
Structure security repo RNS for Dataflow Engine. I don't remember if we talked about that last week.
I think we left this one open because SIGO was not with us, if I remember correctly.
Yeah, looks like Siju is not with us today. Do you know, Joshua Droux, or any other one from Microsoft, if you have some update on that.
Oh, we, we can keep it, in discussion.
Tom Tan 00:06:25 We can keep in mind. I will follow up with the draft and I…
Laurent Quérel 00:06:28 Okay.
Tom Tan 00:06:29 To charge on this.
Laurent Quérel 00:06:30 Okay.
Define consistent policy resolution, a variety, so let's see this one.
Oh, yes, this one is, yeah, we try to… We have two models, basically, for the policies, policy resolution, overriding, and how to… To specify a specific policy for a node, Lalit, are you with us? I'm not sure.
Tom Tan 00:06:58 I checked with Lalit, I think he said you can present the, the, the issue.
Laurent Quérel 00:07:05 Okay, okay. Yeah, I think I can.
Try to just… yeah, so the… Until recently.
the only model that we supported for policies was the ambient approach. At least what… that's what… the name that, Lalit, gave to this, to this approach. So, basically, we… We have a multi-level policy system, The top level, which are applied to the entire engine.
Then the group level, then the pipeline level, and then the node level.
And basically, what we had, each policy… entry into this. So here, for example, we have, It's not a good example. That's the new model. Try to see if there is something else.
Yeah, so basically the… The channel capacity, the… the… I think the TrollSport editors… Were examples of policies that, will be applied Usually globally, but we can refine them per group or per pipeline.
And the inheritance is automatic, but we can override, at a sublevel.
And I think Lalit, was proposing, a complementary model where we can name policy, like, here.
And when we name it, then we can… make reference to a specific policy by name in order to disambiguate. So if we have multiple, let's say, rate limiter.
And we want to, to use different combinations depending on the receiver. Making referrals to them by name was, I think, the goal.
that's valid, try to follow.
I'm not sure that I'm giving the proper explanation, but that's at least my understanding. Having the ability to do this explicit name biling.
or policies.
As opposed to the one that is, more implicit, and, and we could, And I think this table is trying to… let's see… Family au references model.
Accept its cup. Omission, explicitancy.
Not sure to interpret correctly this table. I was thinking that this table will show which policies are Naturally ambient, and which one are… Let's say, named policies.
Joshua MacDonald (Microsoft) 00:10:13 My understanding is that he's, categorizing each column on the right, except for the first column, is a type of… override that might happen when we interpret a policy. So, when you have a group-level policy and the Pipeline level is omitted, that's the omission column.
But if it's ex… it's present but empty, what happens? That's the explicitly empty column.
This… the environment in which you have nested configurations and templates mixed together always produces this type of chaos. I don't… Have an answer to it.
Laurent Quérel 00:11:01 Okay, I guess it probably needs to…
Joshua MacDonald (Microsoft) 00:11:06 I guess another way to put that, maybe if it helps, is that we can Probably, or the way that the model is expressed in configuration, we can set these policies at four different levels, and it's hard to determine without tracing through the code in several different crates.
what's gonna happen when I set one or two or three or four of those all at once, and whether they are set with empty braces, making empty YAML structs, meaning present, but with no… no explicit settings, versus absent.
So, con… Absence and presence combined with the four different levels.
And then having fields within each one of those policy objects, which may be composed, is what creates that table, but it's complicated.
Laurent Quérel 00:12:02 Yeah, I have the feeling that we need to, To continue the conversation on that, to make sure that we are not, Because… we are not making things too much complicated for anyone to understand it. For me, the previous model was easy to understand, but not without problem. I agree. And I probably didn't… fully understood the final approach that we… I mean, I understand the… what Plalit, proposed.
That this, referencing policies by name, but I also understood that he was saying, oh, we could have These two models… together, and that's where I'm… I'm not fully, I don't necessarily fully understand this aspect of the… of the proposal. So let's maybe, Keep this one open, and, ideally, if we can have, a follow-up with Lalit, and making sure that we, We end up with something that we all understood.
So I suggest to keep this one open, and and we continue on that.
The controller level extension point… oh, okay, this one.
I think we already talked about this one.
Joshua MacDonald (Microsoft) 00:13:44 Correct, because Thursday was 5 days ago.
Laurent Quérel 00:13:47 Yeah, yeah, so, I think this one can be just, Okay, add receiver declared listener identities for controller planning.
Introduce receiver, only, listen, oh, okay, declaration, so controller planning case.
Okay, I think it's related to…
Joshua MacDonald (Microsoft) 00:14:14 NUMA or whatever routing.
Laurent Quérel 00:14:17 Yeah, and also the… all the… the work that, Ladit is doing with the IDPF optimization.
If I remember well.
Which is, yeah.
Joshua MacDonald (Microsoft) 00:14:28 connected with the NUMA topology, yes, that's correct.
Laurent Quérel 00:14:31 Yeah.
Yeah, because right now, the… the listening endpoint.
Or, are like, an OPAC configuration inside the receiver. It's not something that the engine Can easily interpret.
And I think what, Lalit is trying to achieve is… is making, those endpoints visible by the engine, so we can… we can reason about them.
And detect when there is a collision, when there is… And on which we can also, sorry for my, for my dog… on which we can also, configure some low-level stuff, like the EDPF, load balancing optimization.
Which will require to… to very… to understand well those endpoints that are available.
Yeah, it's all about that.
Joshua MacDonald (Microsoft) 00:15:34 It sounds like listener policies.
Laurent Quérel 00:15:40 Yay… At least declaration. A way to make sure that those listeners are Are visible and understood by the engine.
And we could imagine that we have policies that will be applied to them, but there is this declaration and potentially policies.
Okay, I did my best to present the concept. I'm not sure that it's perfect, but, yeah, the receiver declared, yeah, listener IoTs. I think that's… yeah, we are on the right direction.
I definitely agree, personally, with the fact that we need that.
The food detail, I don't have necessarily the full detail in my mind, but At least, overall, I think that's an important aspect that we need to, to address.
Joshua MacDonald (Microsoft) 00:16:32 Actually, now that I see it, it sounds like we don't need to modify configuration. This is just a mechanism that the nodes use to declare what they are and who they are, and…
Laurent Quérel 00:16:41 Yeah, yeah, yeah. We, we, we have some, example of that already. This, I think it's name, try to remember.
Where the node can basically declare, Some capabilities, or some, some requirement.
So we already have this kind of protocol between the node and the engine. We could imagine that we use a similar approach.
to declare, things, that will be understood by the engine.
Okay, so let's move on and make that… Accepted.
Tom Tan 00:17:26 Was the item just to be accepted, or we need more information on that? Just want to confirm.
Laurent Quérel 00:17:35 Sorry, where do you sit on?
Tom Tan 00:17:36 The, the last item, the issue, should, should,
Laurent Quérel 00:17:41 Do this one?
Tom Tan 00:17:41 The last chat, not the.
Joshua MacDonald (Microsoft) 00:17:44 3687, should we leave these?
Tom Tan 00:17:48 The tragic Statement…
Laurent Quérel 00:17:50 Oh, no, I think we… Let me refresh, yeah. I just removed the triage needs discussion. I think it's.
Tom Tan 00:18:00 Sure.
Laurent Quérel 00:18:01 I think we agree that it's an important concept on which we need to work.
My goal here is just to identify new GitHub issues.
that we… We think will not be, interesting to, to integrate into the… the list of things that we want to achieve. So, for me, this one is definitely something that we… on which we need to To find a solution.
We… and we can use this entry to continue the conversation.
I don't think at this level we need to go in more detail.
Add configurable balance sharing for exhausted core cone placement.
Yeah.
So that's… that's part of the… it's a follow-up, conversation to… these, copic of being able To specify constraints on… Pipeline instance placement on cores.
Until recently, we were only able to follow explicit policies, where we say, okay, this pipeline will go on Core 1, Core 2, Core 4.
And then we added, options to specify a number of calls without specifying their ID.
Which, bring some flexibility, obviously, and then, We identify that, because our system is highly dynamic, we can reconfigure things on the fly.
So we, we need some additional… a specific… Let's say, flags that will specify what happened if we… We, We have concurrency on the same core for different pipeline instances.
So, do we… do we fail? Or do we accept, Multiple pipeline instances on the same core, and that's… What this thing is about.
So… And then, basically, the placement engine, and, yeah.
the controller.
We'll take that, and when we are in a position where we have to assign two pipeline installs, so basically two threads to the same core.
Depending on that, either the deployment will fail.
Or it will be accepted, and then we know that multiple threads or multiple pipeline instance can share the same core.
Definitively useful for me. Any concern with that?
Joshua MacDonald (Microsoft) 00:20:58 That sounds good to me.
Laurent Quérel 00:21:01 Great.
Okay,
Tom Tan 00:21:05 The issue is accepted, right, or…
Laurent Quérel 00:21:09 Yup.
Tom Tan 00:21:10 Okay.
Laurent Quérel 00:21:11 Yeah, and
Drew Relmas 00:21:14 I think it's… it's… The difference between removing needs discussion and actually adding accepted.
Laurent Quérel 00:21:21 Oh, yeah, sorry, yeah. I just,
Drew Relmas 00:21:23 That's what's causing…
Laurent Quérel 00:21:24 Forget that. Sorry. Okay, my bad. I'm not, Following the process properly today, sorry for that.
Can you, Drew or Tom, Just, making the corresponding corrections.
Tom Tan 00:21:42 Okay, yeah, I think we went with that.
Laurent Quérel 00:21:44 Great, thank you.
So, okay, this one is new. I can talk about it because I just created it.
So…
saroj 00:21:55 Oh…
Laurent Quérel 00:21:56 We support two main, memory allocators, GMalog and Emalog.
The default one is GMalloc.
It's not necessarily the fastest, it's not necessarily the most maintained memory allocator.
I will say that, based on these two criteria, GMALOC will be better, but, Gmalloc has or exposed, by default, a nice, API to capture per thread.
saroj 00:22:28 It's great, but…
Laurent Quérel 00:22:29 The number of, Bite allocated, and… and… And their location, right? They're located.
So, we rely on that to… Determine the memory usage per thread, and so indirectly per pipeline instance.
And then we are able to report this, Memory usage directly in the metric, which… make,
saroj 00:22:55 Hello.
Laurent Quérel 00:22:56 In my opinion, it's a very useful set of metrics when we want to monitor pipeline instances.
I try to see if, basically, we can support the same thing with Mimaloc.
And I discovered recently that there are… A very interesting, low-level, API, into the Mimalog, operate, in fact, into the Memalog implementation, C or C++, I don't remember, probably C, which are the, the, the Memalog, the MIP new, and, and basically those, those three, function.
which are exposed with the version 3 of Inmalog.
And basically, that will give us a way to… to implement these kind of things, so… We… we pin every, so we have one thread per pipeline that is pinned to a specific Coral.
Some… depending on the property that we sold just before, we can have one, exclusive, thread per core, or multiple.
But then, once we have that, with this new approach, we can basically instruct the allocator that we want to create a dedicated app.
For, a specific thread.
And if we do that with Vimalog, then we get, for free, this kind of, Matrix.
And, and we, And we get an additional advantage, which was not super visible, I mean, an issue that was not super visible in the previous approach.
I think it's summarized here… In the previous approach.
When, let's say, you have an ingest pipeline and a processing pipeline connected with a topic.
The way that, for example, GMadoc is working, let's say you instantiate a set of buffers for Apache Arrow records.
Into the ingest pipeline.
And then these are basically the reference on this subject will traverse the topic, we'll end up into The, the Sigong pipeline, the way that, by default, GEMalloc is working.
When we free this, when Rust decides to free the corresponding Apache Arrow records.
That will affect the matrix of the pipeline, the second pipeline, not the first. But… the, The number of bytes allocated will be assigned to the first pipeline.
So we, we, we could observe some, invalid measurement.
And, and if we follow this, what is described there, We can basically correct that.
When something is allocated into one thread, one heap.
Even if the deallocation happened into another thread, When we follow this model.
The location will be reported to the… where the object has been allocated.
Which… does not solve everything, but at least make the memory usage accurate, and we will not observe things that are negative or something like that, even when we are in a multi pipeline deployment.
So that's one reason why I think it's interesting to move there. And I think, That will give us a way to do, a memory limiter, not only at the… At the process level, like, has been implemented, A few months ago, but also at the pipeline level, with one drawback, the memory usage is based on who is at the origin of the allocation. So, it's not perfect in the sense that when the ingest pipeline initialize, for example, we, we have the receiver, whatever is the receiver, it will allocate a set of Apache Arrow records, and then we… let's say we go directly to a topic exporter.
That will, broadcast or load balance that to different pipelines, downstream.
So the, and let's say that this set of Arrow records are for a specific tenant.
And the downstream pipelines are pertinent.
for the… the… one of the models, the multi-tenancy model on which Joshua is working.
So it's not perfect in the sense that This specific allocation will stay attributed to the first pipeline, the ingest pipeline, but Once it's entering into the tenant's… Specific pipeline, so the downstream pipeline, one of the downstream pipelines, we… Once, because we… everything is immutable, so if we do any kind of transformation, we will allocate a new a new set of Arrow records, then that will be attributed to this subong pipeline.
So the imperfection is only on… when… when we transit between the topic exporter to the topic receiver, most of the time. So for me, it's not a big deal.
And that brings us very close to the perfection for… not for a lot of, work, in terms of memory usage measurement pertinent.
I'm not sure that my explanation was perfectly clear, but I did my best, at least. So, yeah, that's the… Yeah, the origin of this, proposal, Improving, basically, the memory, Memory usage measurement, and, and, having a clear, IP definition per thread, per pipeline.
Joshua MacDonald (Microsoft) 00:29:49 Is there some magic that is required to make this work? Like, do you have to wrap an object of heap A in some special container?
Laurent Quérel 00:29:56 So, what you have to do… so once you… We already do some of that, but not all of that. So when we pin a thread to a specific core.
We can say, okay, every allocation that will happen after this point In that case, will be associated to the corresponding thread.
And that's what… it was a little bit implicit before, it's becoming explicit with this approach. And that's the… The… I think it's, somewhere… yes.
That's what is described here.
we have to call explicitly those low-level functions, both from gmailoc and Mimaloc.
Before that, it was not explicit. We… and both Gmail and Mimaloc are already a little bit Numa-aware.
But with that, we help the system to do a better job.
And more importantly, we get something from Mimalog that we were not able to get with the generic approach.
not so much improvement with, for the GMOC approach, because for the GMOC, we were already able to… to get those metrics per thread.
That was not possible with the Mimaloc, which, if someone wants, for example, to switch from Gmail lock, which was the default, to Mimaloc.
implicitly, and it's not super visible, it will basically, lose the corresponding metric.
With that, we will get the same level of, Low-level metrics for the memory usage.
Which is, in my opinion, great. And… and we will, inherit also the, I did some tests, it's significantly faster in terms of memory allocation to use Mimalok.
with the… The negative punt is… it's, Using a little bit more memory to do its job.
So if your only criteria is minimizing as much as possible the memory usage.
Probably Gmail Lock is a better approach, if you are looking at optimizing the throughput, in general, Memalloc will be better.
So, I think we can document that, but at least we can now switch from… we could, if we implement that, we could switch from GmailOC to Mimaloc constantly without losing anything.
Joshua MacDonald (Microsoft) 00:32:42 This requires the topic exporter to, like, do a special memalloc thing to fill.
Laurent Quérel 00:32:45 No.
Joshua MacDonald (Microsoft) 00:32:46 region.
Laurent Quérel 00:32:47 No.
You know, the… for the topic, we… if we want, like I said, the… accounting… the accounting of… when we migrate an object from pipeline A to pipeline B, With this communication across topic.
This thing does not solve magically the, let's say, the attribution of the corresponding message from A to B.
it's still assigned to A.
So that's the… the limit.
before that, it was not also… before that, we… it was the same thing, except that the delegation was attributed to B, now it's attributed to A.
But it means that you have some object in B, that are reported in delivery usage of A, But at least it's reported accurately.
I think I need to describe that better. It's relatively clear in my mind, but I'm not sure that it's perfectly clear with my current explanation, but…
Joshua MacDonald (Microsoft) 00:34:00 I was just trying to follow whether… so Laurent has some work that is either pending or already merged that gives you a way to Track, like a…
Laurent Quérel 00:34:09 Oh, yeah, I think it's orthogonal, yeah. I think what Lalit is doing in terms of At the Mondari, so the topic, trying to account for this migration, and make a correction on the downstream side, I think it's totally orthogonal, I'm not… Making…
Joshua MacDonald (Microsoft) 00:34:29 And how long.
Laurent Quérel 00:34:29 there. I think I'm just making the memory usage a little bit more accurate. But we still need to make this mechanism if we want to have a perfect A perfect accounting in terms of, memory usage tournament.
Joshua MacDonald (Microsoft) 00:34:51 I think I'm starting to understand.
Sounds good.
I know we have two items on the agenda.
Laurent Quérel 00:34:57 Yeah, maybe we have to.
Sorry for that.
Joshua MacDonald (Microsoft) 00:35:02 Oh, okay.
Laurent Quérel 00:35:03 Okay, so, Guillermo… You were… you want to talk about the AI code review PR, Maybe I can open it, or you want… do you want to share your screen?
Guillermo Calderon 00:35:15 Yeah, for sure, if you can, open it, please. Thank you.
Laurent Quérel 00:35:19 Oh, oh, okay, so,
Joshua MacDonald (Microsoft) 00:35:23 First, let's find it.
Laurent Quérel 00:35:25 Yes. Do you remember the number of this PR?
Guillermo Calderon 00:35:28 Yeah, it's… 3… I have it… 3, 7, 10… I can also put it on the chat.
Laurent Quérel 00:35:37 2710? Oh, okay, that's… no, that's… 3710 is… doesn't look like the…
Kennedy 00:35:44 That's it. This one?
Guillermo Calderon 00:35:45 That's the one.
Laurent Quérel 00:35:46 Oh, okay.
Guillermo Calderon 00:35:50 Okay, I can, just go ahead a little and explain it. So, talking with Kennedy, he mentioned this part of having, like, a baseline here for the AI, review. So… this is just, like, mentioning, it's a baseline, there are, like, a lot more things we can build on top of it later. Right now, what happened, most of you should know, like, in… it's, like, Copilot reviews a PR here, but it was just giving, like, a generic, like, Rust advice, mostly. So, it was… It doesn't really know, like, the stuff that we care, like, in this project.
just to put, like, an example that I was, scanning through, like, using, mutex, like, we want to justify why are you using this? So, examples like that is something that it's not, getting reviewed.
So, when I started working on this, I found out it was actually something that you, Lauren, have done, some months ago, like.
if I remember correctly, it was, like, around May, that it was, like, the AI-assisted PR Review Guide, so… the only thing that I was seeing, it was that that was just never connected, actually, to Copilot, so it was not actually, like, reading it. So my PR was… at first was, like, to try to look, like, to small, rules, and then to make it this, start, and then from there we can go on.
But since I saw that you already have that, the PR is, like, really just connecting, the files, and it will not be, like, new rules. It's, like, more, like, plumbing and connecting what you have already done there. So, the point of the PR will be, like, save time on both sides, like, the reviewers, don't have to catch, like, this stuff.
And also for the contributors, we'll help, like, in the feedback that they can get, like, right away, instead of, like, waiting for a review slot.
One thing… yes, sorry.
Laurent Quérel 00:37:52 Yeah, I was saying, nice. So, yeah, you dated this file in order to connect, to make this link to this, AI-assisted PR review.
And then automatically now, we will get the benefits of this thing.
Into the, recommendation for the review process.
Guillermo Calderon 00:38:14 Yeah.
Laurent Quérel 00:38:14 I'm good.
Guillermo Calderon 00:38:15 The only part that it's important that I also mention is, like, I couldn't, like, fully test it, like, yet, because basically my docs, or the things that I put, it's only, like, docs, it's not, like, any ROS files. So we will really see it working, like, on the first, like, ROS PR app after this one got merged, like, once this got merged, I can even go ahead and do, like, some small PR there to see if this is working. So it's, like, just a bit of a tooling gap right now, but yeah, when the PR goes there.
It will be… we can test that. Then… other thing that it's worth mentioning, it's, like, as I mentioned, this was just, like, a baseline, and there are, like, a lot of things that we can build from here. So, some things that I talked with Kennedy, and it will be, great maybe to have, like, in next phases will be… the first one is one that it's kind of, like, profiles, that it will be, like, kind of… make AI go to, like, old, like, review comments, find the ones that keep coming up, and kind of bring them back here. So, like.
we see, like, what are, like, some patterns that normally, like, tend to appear, in those PRs, and we can add it, like, as rules. So that is one thing, and the other part that we were also thinking about was, like.
once we throw maybe a lot, like, AI on reviews, we can have, like, okay, we have this list of rules that we always want to check. For example, it happens sometimes that I remember when I do, like, my first PR here, like, this thing of the CLA, it's signed, so I think by now, most of us have already done that, but maybe people that are new to contributing didn't know this.
So.
kind of having a tag that basically, until, like, PR passes all of these rules, it doesn't get a tag.
like, as ready for review. So basically, the… the reviewers will only spend their time on PRs that actually, like, need their, like, their help there, instead of the ones that maybe are missing, like, some… some basics. So… so yeah, this was, mainly what I want to… to talk about today.
Laurent Quérel 00:40:33 Okay.
Yeah, make a lot of sense for me.
Thank you for that.
Any, feedback on, on this work?
Homozers?
Drew Relmas 00:40:46 It's… that's just interesting to me. I didn't think of possibly tying draft status to this review process. I mean.
Hi.
I guess that could work, but, I mean, there will always also be the manual button, unless I can figure out a way, with Trask to disable permissions for people to convert between draft and…
Kennedy 00:41:10 It would be a tag, I think, so we could have a tag.
Drew Relmas 00:41:13 Oh, okay, okay.
Guillermo Calderon 00:41:14 Yeah, I was going to say that, Tag, yeah, my bad.
Drew Relmas 00:41:18 Tag, not actual PR state. Okay, that makes more sense.
Laurent Quérel 00:41:21 Oh, okay. And, and, I think we need to see… How that will interact with.
Drew Relmas 00:41:29 Yeah, how it would interact with a dashboard, that was my next thought.
Laurent Quérel 00:41:32 Yeah, yeah,
Drew Relmas 00:41:34 I actually had… I had a feature ask out to Trask to allow persistence of certain defined labels on this dashboard. So you could imagine we have a label Like, not ready for review, for example.
That would potentially also make its way to this, view.
Laurent Quérel 00:42:02 Yeah, Guillermo or Kennedy, were you aware of this, pull request dashboard?
Because I think, based on what you said, I think we need to see how to maybe update. I think that is a set of script, I don't know exactly the technical detail behind this, GitHub issue, basically, that is updated, periodically, but… We probably need to take into account the… potentially the labels that we… you will assign.
Kennedy 00:42:35 Yeah, so that's a future phase. We are aware of it, but, you know.
Laurent Quérel 00:42:39 Okay.
Kennedy 00:42:40 So basically, there's a couple things that we see happening next. One is we want to start seeing this exercise, see that we all trust it over the next week or two, and then we're therefore ready to add a label like this.
Because it also would require a behavior change from maintainers to ignore the PRs that are not in that state to kind of enforce that behavior and everything. And when we get to that point, we'll… we'll either create an issue or discuss and… in here, You know, what label do we use, and then how do we plumb it to this, and, you know, kind of all the next level hooks.
One other thing that I wanted to bring up is, we… he… it's like, when we initially discussed this, I… I completely forgot about the fact that you had created that, like, AI review guide that kind of has a bunch of these rules already codified.
And Guillermo found that. So, we currently have, in his PR, there's 3 rules that he picked that, kind of came up often, but it also links your guide, so it kind of has both.
So, we can decide whether or not we keep them explicitly defined in these instruction files, or just keep it in one place in that AI review place, or if we even do two, because there's always, like, context limits, so maybe there's, like, always check this, but then also try to get through that… that other document and, you know, to do the best you can, because depending on which model it picks with context windows, it may forget some, so by having these, like, top three.
At least those shouldn't get forgotten. So we can play around over time which rules end up in either place, or if they all go in one, or… You know, kind of how we tune from there.
Laurent Quérel 00:44:30 Yeah.
I was thinking… And I don't know if, how… efficient, and how that will be followed by the agent, but we… Maybe we could imagine that we have, this kind of, guideline… I mean… document to guide PR reviews, but… One that is specialized for documentation, for example, one that is specialized for Coding re… code review, and… and maybe some other for, I don't know, configuration things?
And maybe that will give… if we consider that the GitHub Copilot Reading that, seeing the… for what this review process has been optimized, and depending on the content of the… of the PR, decide which one to use first. I don't know if that's something that's.
Kennedy 00:45:35 That's actually there, even with this. So if you look, it's the… one of those is called Rust Review Instructions, and it.
that file, at the top, it says, like, under this path, and if it's .rs files, you run this.
Laurent Quérel 00:45:49 That applies to.
Kennedy 00:45:50 So we can absolutely do… that type of stuff. You can even… you can… it's a glob, right? So you can do really crazy things, like, say, if it's a crate under here, then it has these additional rules. Like, core modules, for example, might have a higher bar than contribib if they were all in this repo, and things like that. So, yeah, the foundation's set to… To do that, too.
Laurent Quérel 00:46:14 Okay.
So… I guess, if I understand well, now, we already have, in some way, this kind of, a routing mechanism.
So we can, based on a few weeks of observation, seeing if it's working well or not, and deciding if we combine that Into a single file, or if we keep it as it is today, in a multiple, in multiple files.
Am I understanding correctly your conclusion?
Kennedy 00:46:48 Yeah, yeah, I…
Laurent Quérel 00:46:50 I'm kidding.
Kennedy 00:46:50 Unfortunately, there's not a way to exercise this without it being checked in, as far as I can tell. You can run the reviews and everything locally, but that all ends up being harness-based. Like, I… for example, I don't think you can run sub-agents as part of the auto-triggered co-pilot review, but you can absolutely do that in your local harnesses.
So… This is a test in broad scenario, unfortunately.
Laurent Quérel 00:47:19 Yeah, okay.
Joshua MacDonald (Microsoft) 00:47:22 Oh, you say we merge it right now, and then, run it on Drew's PR that we're about to discuss?
Laurent Quérel 00:47:31 Let them eat… look… look good.
to us.
Joshua MacDonald (Microsoft) 00:47:35 to,
Laurent Quérel 00:47:36 LGTM.
Yeah, but…
Kennedy 00:47:41 There's one comment.
Laurent Quérel 00:47:42 me, but to us, this time. Okay, approved. And then, Let's try to merge it and see what happens.
Okay, and the next one is, Drew.
Drew Relmas 00:48:03 Hey, so yeah, we can talk about specifically the common thread, that I linked to right here. So, a little bit of context for everyone else. I started down what seemed like a very small piece of work was Which was, looking at the OTLP, HTTP, and gRPC exporters, I wanted to add byte attribution.
to their exports.
And then I… this turned into a much deeper thing. I looked at an issue that, Josh had opened a long time ago. Actually, Laurent, if you scroll up to the PR description, there are two issues mentioned that I think are relevant here. Scroll down, down, down, down… Those two.
So… We have observed, two problems. One is we've done some work on opt-in item counting at the node level to kind of match the GoCollector Universal Telemetry RFC.
However, Bytes has… been difficult for us so far because, we don't have a great bytes representation for OTAP.
I know Lily added recently, like, the estimated, reserve size, which isn't actually the size of the payload, but rather the size of the full arrays, that we use, so it's not really an accurate, bytes representation.
So, the other thing is, from Josh, or the next… if you go to the next tab down, cash item. So, this is one way to kind of reduce the impact of Adding… both num items count.
As well as potentially paying the cost of doing bytes-sized calculation.
Which is, we should cache its information somewhere. If a single node, pays the cost to count number of items, for example, and it flows through a pass-through node that doesn't modify the data.
That item count should still be valid to be reported at that next node, because there was no change in the underlying data.
And this cache should be invalidated when we reach a node that constructs and… that modifies the payload, in a certain way.
Laurent Quérel 00:50:37 But if we modify it, then usually that will be transformed in a type representation, right?
Drew Relmas 00:50:43 Yes, correct.
Laurent Quérel 00:50:44 And then the new item is… Closed to be free.
Drew Relmas 00:50:49 Yes.
So, in the PR, I had a potential solution for how we would cache item count, as well as, size bytes. And Lalith and Josh had some ideas about… Who should actually own this… who should actually own the… this cache? How do we make it in such a way where, like, one thing I want to avoid is every, like, needing active participation from every node that transforms data.
like, I shouldn't… I, as an author of the attribute processor, shouldn't need to remember to go add a line to invalidate the cache because I modified data. So how do we build in the safety of every time data is transformed, we obviously get a cleared, empty cache. And then from that point on.
If item count or bytes is requested, it's a fresh calculation.
So if you scroll down to that thread, Josh had some ideas about putting it on the context.
But I actually… it's, the next one up. Josh had some ideas about putting it on the context.
I… I was doing a little bit more reading, and I think it actually belongs on the OTAP payload.
Itself?
Because… That part seems like… You know, what is… Newly constructed every time data is transformed inside a note.
So, I don't know, Josh or Lalitz, do you want to add anything here?
Joshua MacDonald (Microsoft) 00:52:40 That's… so that's a good summary. I, I've… As for whether it belongs in OTAP payload, or… context.
I could probably be convinced either way. I guess I was hoping to see us adopt some sort of safe API that would do the right thing. So that might mean that we invalidate or that we… because there are pass-through nodes that just leave the OTAP P data object alone, and there's some which… take apart the OTAP P data, and then put it back together. So anytime you put together a new OTAP P data, you might say, I'm invalidating the context, because we don't know if the data changed or not. And I don't know at what level we have… we can couple the pre-computed size with the fixed data, or the immutable data.
I don't know the right Rust idioms here, but I feel like there exist rust idioms here.
Drew Relmas 00:53:39 Yeah, I mean, those are kind of the three options. There's the OTAP P data, which is one, like, where this current iteration of the PR put it. There's the context, and there's the actual payload object itself.
So those are kind of the three options, I guess you would say.
Laurent Quérel 00:53:58 logically, Not thinking about necessarily the easiest way, but… We are talking about… a cache that… Will be related to something into the payload, right?
Drew Relmas 00:54:14 Correct.
Laurent Quérel 00:54:15 Okay.
So, yeah, I think this cache attached to the payload will make sense for me, because… If it's a different payload, yeah.
Drew Relmas 00:54:27 That's the, thing that I… if you look at my most recent comment from right before the.
Laurent Quérel 00:54:33 Meetings.
Drew Relmas 00:54:33 started. I was leaning this direction. I think it's the most correct alternative.
And then constructing a changed payload just automatically has an empty cache again, so…
Laurent Quérel 00:54:45 Because the context… is… following the flow, but the payload can change along the flow, so I think Having that attached to the payload.
Will… will make the system less error-prone, because if we put this information into the context.
Drew Relmas 00:55:05 And every node is responsible for modifying.
Laurent Quérel 00:55:07 Yeah, so that's why I think it's potentially problematic. So, yeah, I think if… Because what you do, usually, we get, we get, an incoming pdata object, we extract the two components, payload and context.
Sometimes we just observe what is inside this payload, and we reuse it to construct the new PDAT object.
So in that case, because we didn't update the payload.
automatically the cache that was inside will be integrated. And if we… if we transform this payload into a new… a new version of it, independently of the nature of this payload, either OTLP or OTAP, the… when we do this transformation, OTAP to a tab, then automatically the Numitem will be, no longer be based on the, on the cache, but based on the real, Apache Arrow record representing the main table.
And if, and I don't think we do that… maybe… I don't know, that's… I think we do that for… in the batch?
we have, in the batch processor, we can combine multiple OTIP bytes together.
And that's where we will have to… in this situation, we create a new payload that is still OTLP, And that's where… the… the cache has to be, removed, or deleted, and if we need to recompute, then we have to… to retroverse this entire, batching? Yes.
Drew Relmas 00:56:49 Batching is an interesting topic because in one sense, if you were just combining a number of payloads, could you sum them together and not need to recompute the whole thing?
Laurent Quérel 00:57:00 We could, and that could be… but still, the cache has to be updated or removed.
Yeah, I think it's better, like you said, maybe to recompute it.
Because we have all individual information to compute it without road traversing, which will be, Yeah, a nice optimization.
I don't, I don't believe we have any other… Sorry, go ahead.
Drew Relmas 00:57:25 Oh, I'm sorry.
I was gonna say one other point, if you scroll up to the PR description, is there's a certain situation where the caching actually adds unexpected overhead. Like.
And actually, the OTLP note here is outdated because Lily pointed out something about the OTLP wire format versus the protobytes, so I need to fix that. But for example, take OTAP item count. If we have the OTAP representation, we can just do, like.
We don't really have to cache that, it's an immediate access.
Right?
Laurent Quérel 00:58:04 Excuse me.
Drew Relmas 00:58:04 Because we have the… the count…
Joshua MacDonald (Microsoft) 00:58:08 for metrics.
Drew Relmas 00:58:10 Except for metrics.
Joshua MacDonald (Microsoft) 00:58:13 Metrics have an additional level of hierarchy and OTLP, so to get item count from a metrics payload, you have to sum the sum of all the different metric type data point, unfortunately.
Drew Relmas 00:58:24 You're right. Okay, so in that case, we should throw all these benchmarks I have on the screen right out, and I need to go back to the drawing board.
Laurent Quérel 00:58:34 Yeah, that's definitely a good one.
Drew Relmas 00:58:37 I think we're moving in the right direction. And just to be clear, I think I envision the first PR is just exposing this at the right, data object. The second PR, we can expose opt-in with telemetry policies the same way we did with item counts.
Laurent Quérel 00:58:52 Yeah.
Sounds good. What is encouraging is that… is… close to what we do already for a tap.
Is there any,
Joshua MacDonald (Microsoft) 00:59:07 But… but why do we need the arc and the lock here? Like, and I'll say that I said it, maybe it could go in context, merely as a matter of convenience. You're gonna have, like, to me, because the OTAP P data is two parts, it's… all the data of the request, and it's all the other stuff, which is context, including, in my opinion, it would be okay to put a cache of sizes in the context, because when you want to talk about taking it apart, you get two pieces, the data and the metadata.
But I don't mind seeing it go in the OTAP P data.
Laurent Quérel 00:59:43 But how do you determine that you have to reserve?
Joshua MacDonald (Microsoft) 00:59:46 Every time you construct a new OTAP P data, you invalidate the cache, because you took it apart.
Laurent Quérel 00:59:50 Yeah, but you don't take it apart.
Joshua MacDonald (Microsoft) 00:59:51 You invalidate the cache, basically.
Laurent Quérel 00:59:53 Do you have access to the context at this time?
Joshua MacDonald (Microsoft) 00:59:57 Users also do mutate context, but when you set up the new con… the new OTAP P data, you copy it, so it, like, it's… Changing the context, not at that point.
Laurent Quérel 01:00:10 Maybe I'm wrong, but I don't see… yeah, I'm not sure that, We use the context each time that when we update the… the payloads, And to refresh my memory on that.
Joshua MacDonald (Microsoft) 01:00:26 Well, you can't pass a new request without constructing a new OTAP P data, so once you take it apart, you're going to call OTAP.
Laurent Quérel 01:00:32 That, that's the only thing.
Joshua MacDonald (Microsoft) 01:00:33 2.
Laurent Quérel 01:00:34 but the… Function, creating a new payload from another payload, I'm not sure that they are taking a context.
as a parameter. So what I'm saying is, when you all create the OTAP data, you get the contact that you had initially, you get the OTAP They would… And you put that together.
The context does not know that the payload is necessarily new.
Or not new? And how do you make sure that the counter representing this, that the cache representing this number of items is accurate?
I think we need to go into the… I mean, intuitively, I think it's… it will be easier to maintain it into the payload, but I could be wrong.
Drew Relmas 01:01:20 Ben, do you have your hand up?
Kennedy 01:01:23 Yeah, I think this goes back to that conversation we had kind of a long time ago about how Arrow record batches kind of have intermediary states, like, especially in, like, transform scenarios, where Or… let's not even, like, create a straw man. But you have perf scenarios where you might create an… a… a… Arrow record batch that's in memory, not technically valid, because you're, like, swapping columns in some weird way or whatever, and we had talked about how OPL might be able to help solve that and enforce it along boundaries, it's at least accurate. I think we're, like, this is another, like, reason why codifying that concept becomes important, because then you can say, like, hey, this is dirty, it needs recalculated.
Because it's been messed with.
In some way that that cache is now invalidated and needs reset.
And don't need to do it.
Laurent Quérel 01:02:24 Yo.
Kennedy 01:02:24 single, like, mutation, right? It's just…
Joshua MacDonald (Microsoft) 01:02:27 We don't ever mutate data. That's what… I was trying to kind of make the point that whenever we… whatever we do when we have the OTAP P data, we take it apart, and we put it back together. But the moment where we put it back together is we have control at resetting caches, so that anytime you.
Laurent Quérel 01:02:42 Yeah, but we don't want to let this option… that's exactly the point, Joshua.
We want to… make sure that the system is not error-prone. So… Oh…
Joshua MacDonald (Microsoft) 01:02:53 But always invalidating is safe, for sure. I'm never giving you a way to set the size when you put it together and do OTAP P data, it's… the cache is invalid, you're gonna have to recompute your size now.
Drew Relmas 01:03:07 But then why have a cache?
Joshua MacDonald (Microsoft) 01:03:09 Because when you pass it to the next node… well, so for example, you put together a new OTAP P data.
it invalidates the cache, you then send it through the channel. On the way out, it counts how many bytes have you been sending out. So, that's the first point. It modifies the context, now it sets the cache, now it goes through the channel, it arrives at the next node, you have the pre-computed size.
on that node, which has been computed after the invalidation on the way out of the previous node.
Laurent Quérel 01:03:40 I think we, we, you know… I'm not convinced by the approach, but I think it's more natural to attach this counter to the payload, because if we don't change the payload, we don't have to think about it. It's… the cache is already there. If we create a new one, we know that it's zero, or the specific case of the batch processor.
And we don't have to have any coordination with the contacts in that case.
Joshua MacDonald (Microsoft) 01:04:10 Well, there's no coordination. The coordination is entirely in the OTAP P data object, which controls the pairing of both. So I… I guess I… maybe those are… these are just two ways of framing the same idea. I… I find it…
Laurent Quérel 01:04:23 Technically, yeah, technically, I don't want to argue anyone with that.
Joshua MacDonald (Microsoft) 01:04:26 But are you talking about wrapping the OTAP payload? So the OTAP payload currently is an enum that contains the two different types of data.
Right. Are we going to have a struct that contains the two different types of data and a cache, or are you adding a.
Laurent Quérel 01:04:41 No.
Joshua MacDonald (Microsoft) 01:04:41 to the OTAP P data, which in which case I'm saying it's identical to putting it in the context, you're just.
Laurent Quérel 01:04:46 No, no, no, no, I think what was, suggesting Joe was to attach the stunter to the… to the OTAP pillow, the, the… yeah, I think it's named OTAC Pillow,
Joshua MacDonald (Microsoft) 01:04:58 be data.
Laurent Quérel 01:04:59 load, or… sorry.
Joshua MacDonald (Microsoft) 01:05:01 Take it.
Laurent Quérel 01:05:02 Where it is, I think it's there.
Yeah, the OTAP payload, that's where the counter will go.
Joshua MacDonald (Microsoft) 01:05:09 That's the enum that's either records or bytes, so what I'm hearing.
Laurent Quérel 01:05:13 that you should.
Joshua MacDonald (Microsoft) 01:05:13 I replaced that with a struct containing an enum and another field called a cache.
And I believe we could lift it up one field, or push it back into the context, all the same, it's just a matter of, conceptually, where you put it.
We control it at every transition.
Laurent Quérel 01:05:27 Yeah, so we can continue the conversation later, but I disagree with that. Because the way that, if you look at the processor.
you basically destructure, so you split, like you said, you split the contacts on one side, and you put the OTAP payload on the other side.
Then the developer of this processor has access to these two information.
And, what I'm saying is that when you reconstruct the OTAP data, when you take the context and the OTAP payload together.
You don't know what happened in between.
There is nothing guarantee you that your tap payload didn't change.
So you don't know if you have to change into the context the corresponding counter.
That's… That's where I was going on with validating.
Joshua MacDonald (Microsoft) 01:06:15 Right there. Same point.
Laurent Quérel 01:06:19 I think we need to go on the code and see, but that's where I think we have a divergence. I don't think it's possible.
Okay? To do that.
Hopefully, I mean.
Joshua MacDonald (Microsoft) 01:06:30 We can… okay, I promise.
Drew Relmas 01:06:32 Thank you for the discussion.
Joshua MacDonald (Microsoft) 01:06:33 Disagree.
Drew Relmas 01:06:34 You can keep going offline. Yep.
Laurent Quérel 01:06:37 Okay, great. I think we covered all the… the second topic.
Any last, minute, comment or something?
Otherwise, I think we are good… we are good to go.
Great, thank you.
Have a good day of the week.
Kennedy 01:07:00 Thanks, all.
Drew Relmas 01:07:02 Bye-bye.
Tom Tan 01:07:03 Right.
Guillermo Calderon 01:07:06 Thank you.
Laurent Quérel 01:07:08 too. Bye.
