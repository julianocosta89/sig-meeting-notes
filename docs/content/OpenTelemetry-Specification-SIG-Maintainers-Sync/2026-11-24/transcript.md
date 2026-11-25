SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-11-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang (Microsoft Corporation)** 01:20 Laura.
**Alex Boten** 02:25 So we can give it another… Minute, or should we just get started?
Guess we can get started here. Me.
Share my screen.
My… first time running this meeting, so… If it's not what you expect it to be, please feel free to raise your… Raise your comments, voice any concerns, or interrupt me as you go.
Okay, so we have a bunch of topics already.
We also have a recurring topic around the post-graduation roadmap.
Do we… do we have anything to cover in the post-graduation roadmap?
If not, then I guess we can start with the first topic, which, Florian, you say one minute, but it's gonna take me more than one minute to read this.
**Florian Lehner** 04:18 Okay, I tried to keep it short. So, we at the Profiling SIG were looking into what is the correct, identification we can put on auto profiles.
to name the producer of hotel profiles. We did come along the OTL semantic conventions around telemetry distro, and, I was unsure about, if it's a good fit, as eBPF is, an outside viewer on… on… as an observability solution.
And, so, yeah, as Robert pointed out with the, feedback, there's TrioArt with OBI, And, I think the eBPF profile will just, adopt this, from the semantic convention around, telemetry distro.name. It was not clear if the eBPF use case is also covered by this, but it seems like, so, we would just follow this.
If this makes sense.
**Jason Plumb (Splunk Inc.)** 05:26 I'll jump in on that one. It seems like this would work for something like eBPF, where you have, like, a separate process that's profiling another process, but I don't know that this works for, like, embedded profilers that are part of an existing distro, or an existing instrumentation library.
So, like, in the case of Java, for example, if we add a profiler that runs in process in the Java agent, we can't reuse distro name, because we already have something in there.
**Florian Lehner** 05:51 Yes, but, this… but this, for example, the Java… profiler should use a telemetry SDK, probably, then.
**Michele Mancioppi (Dash0 Inc.)** 06:04 But if the, if the profiler is part of the SDK, Why wouldn't it use the same, the same, resource attributes as the, on the tracers and the… The metrics providers, whether we need to specify what a profiler built in an SDK would do, it's just another instrumentation.
**Florian Lehner** 06:28 The UPF profile is not, just another SDM,
**Michele Mancioppi (Dash0 Inc.)** 06:31 I agree.
**Florian Lehner** 06:32 magnets.
**Michele Mancioppi (Dash0 Inc.)** 06:33 I was… I was confused by Jason's remark on this, not by yours.
**Florian Lehner** 06:39 Okay, sorry.
**Jason Plumb (Splunk Inc.)** 06:41 So the proposal is to use DistroName.
For the name of the profiler.
In the case of existing agents, like the Java agent, we already have a distro name.
I believe.
And correct me if I'm wrong, I think we used Astronium for something.
**Michele Mancioppi (Dash0 Inc.)** 07:00 I get it. Yeah. Wouldn't we use the instrumentation scope name to say this is coming from profiler XYZ?
**Jason Plumb (Splunk Inc.)** 07:10 That makes sense to me, but that's not what's being proposed here.
**Michele Mancioppi (Dash0 Inc.)** 07:13 Okay, now I get it, thank you.
**Jason Plumb (Splunk Inc.)** 07:15 Yeah.
So, do… do profiles have an instrumentation scope, or something that scopes it, where this might be a better fit?
**Florian Lehner** 07:26 The scope is the full system.
So, it's not limited to.
**Jason Plumb (Splunk Inc.)** 07:31 I see.
**Florian Lehner** 07:31 process, but,
**Jason Plumb (Splunk Inc.)** 07:32 EV system. Yeah, yeah. Yeah.
Yeah, I don't have a great idea or solution on top of my head right now, but I just see… I see that conflict, and maybe it warrants a different attribute.
**Trask Stalnaker (Microsoft Corporation)** 07:53 This would only be stamped on the profiling data, Florian?
**Florian Lehner** 07:59 Yes, correct, only profiling data.
**Trask Stalnaker (Microsoft Corporation)** 08:04 And, I mean, it is essentially… I mean, you install OB separately.
It's not… we're not embedding that inside of, like, another distro.
**Reiley Yang (Microsoft Corporation)** 08:18 you committed.
**Trask Stalnaker (Microsoft Corporation)** 08:19 It feels like you do have two different distros going on at the same time, which… Seems okay.
**Florian Lehner** 08:27 I think for the eBPF profiler, it's a little bit different, because it can be part of the OTA collector, it's just another receiver.
But,
**Trask Stalnaker (Microsoft Corporation)** 08:43 So, Jason, does that make sense, or were you…
**Jason Plumb (Splunk Inc.)** 08:48 It does in the case of OB, but I guess if the… if the question that's trying to be answered is, I have this profile that was handed to me, which profiler generated that?
If it came from a Java, like, JFR profiler, I don't know where you'd look in that profile to see that.
From this proposal.
**Trask Stalnaker (Microsoft Corporation)** 09:09 This wouldn't cover, would this… is this trying to cover all profilers?
Florian?
**Florian Lehner** 09:17 No, no, no, I was just looking into, eBPath Profilmila, I'm…
**Jason Plumb (Splunk Inc.)** 09:22 Okay.
**Florian Lehner** 09:22 Okay. I can talk to other profiling people, but specifically, I wanted to solve it first for the UPEF profiler, because we don't have anything attached yet.
But for a profiling backend, in the end, the backend needs to be able to distinguish between, hey, I'm having a runtime profiler, like.
Java Flight Recorder, Go Flight Recorder, or it comes from a system profiler, like the EVP provider. So, this makes… this makes a difference, and yeah, this, should be distinguishable at some point.
I think we overestimated the one minute, sorry for that.
**Jason Plumb (Splunk Inc.)** 10:00 Yeah, and you literally put eBPF-based observability in the question, so I'm sorry for taking that off the rails. I'll shut up now. Thank you.
**Trask Stalnaker (Microsoft Corporation)** 10:11 Yeah, I think it's fine. It's a separate package, separate installable, separate distro, separate, yeah, distro version.
Makes sense.
**Florian Lehner** 10:22 Cool. Thank you, everyone.
**Alex Boten** 10:28 Thank you.
The next item didn't have a name next to it, so I don't know if anybody in this call wants to own talking about this spec issue around… Entities and defining scope.
**Josh Suereth (Google LLC)** 10:44 This was from last week, so I can take ownership of this, even though I was out yesterday, so I didn't hear the entity SIG discussion of it, but this is, This is supposed to resolve one of the issues with entities where we have resource detectors that can provide an entity that is not globally unique with its ID. So, that's just a thing that plagues, you know, instrumentation and open source, is, we have these IDs that we need to be able to observe that we don't know if they're actually unique.
So, what this is adding to the entity data model is explicitly telling people whether or not an entity's identity is unique globally, or needs to be referenced in context to some other entity to be considered unique.
The example here is Kate's Containers. They're usually referenced by name.
There is no, like, UUID for a container?
But for a particular pod, since it can run multiple containers, you can tie a container and pod UUID together to say, okay, I know that this is uniquely this container, because I have the pod ID and the container name, right?
That's an example of how this is used. So this has been open for a while, it's approved from… I think there's… it looks like Limila added comments that I didn't have a chance to look at, but we were just looking for feedback and comments and concerns from the overall specification SIG.
**Liudmila Molkova** 12:14 You're going to finish driving it forward, Josh? Or Dmitry would be back?
**Josh Suereth (Google LLC)** 12:19 I think this now falls on me or someone else in the SIG, like Nathan or Daniel.
So, my plan was to pick this up myself and continue pushing it, which is why I wanted to talk about it here.
**Alex Boten** 12:47 But Mila, do you want to bring up any of your comments and talk about them here, or do you want to do it all, I think?
**Liudmila Molkova** 12:54 Let's do tasty, I think the… the substantial comment I had is that I'm not sure I understand how… The ID scope can be inferred from relationship events.
But maybe it's me not understanding.
**Josh Suereth (Google LLC)** 13:13 Oh.
Yeah, we can talk about it here. So, so the ID scope is not inferred from relationship events at all.
**Liudmila Molkova** 13:21 Okay, so then maybe the language should be cleaned up, because there is some language that it is.
**Josh Suereth (Google LLC)** 13:28 Okay, okay.
Yeah, I think conceptually, from relationship.
you can infer what your ID scope is, but in practice, oh, are you talking about the notion of inferring what your ID scope is when somebody sends a… unknown ID scope?
**Liudmila Molkova** 13:48 So here, there is the text,
**Josh Suereth (Google LLC)** 13:59 Can you zoom in? Sorry, my eyes are really tiny.
**Liudmila Molkova** 14:06 So, it just says here that the consumer computes the entity, global identity, blah blah blah.
In entity relationships, based on the entity type being equal, maybe this paragraph can just go…
**Josh Suereth (Google LLC)** 14:23 to it being equal.
**Liudmila Molkova** 14:31 So, it currently says it can be either from relationships or from the definitions.
**Josh Suereth (Google LLC)** 14:38 Oh, oh, oh, I see. So, the… Yeah.
I think the… the confusing part here is the notion of… The global identity does not have to imply a specific relationship type.
So, if I use some Like, for example, let's say I am trying to uniquely identify a Kate's cluster.
and I have, like, a name field.
And then, to make it unique, I need to know, like, what cloud it's on and what region.
I would have a scope that says, like, you need to know the cloud region of this cluster to make it be unique, right?
But it could be that there is some other hierarchy in the middle between me and that thing.
So, it's not an immediate relationship, necessarily.
The goal here is we're trying to give people the ability to synthesize a completely unique UUID.
From discoverable res… like, attributes.
So, yeah, I get what you're saying. This is confusingly worded.
And I think the concept is generally confusing, so probably need to do some education here.
And fix the wording.
**Liudmila Molkova** 15:44 Yeah, thanks. And the other… like, I suggested some, wording cleanups, but I think the one substantial comment is, would it make sense to only… Send the scope, if it's… So, we have two properties, the scope… Kind, global local.
Unspecified. And the entity type.
And by… under… for… for the scope.
And if we say send entity type, it implies local, right?
So, can we optimize some bandwids, and maybe never send… Unspecified, or maybe it doesn't matter.
**Josh Suereth (Google LLC)** 16:33 So, yeah, the, The problem with unspec… so, if we didn't… it's a ternary is the problem, so we either have global, local, or unspecified. And yet, could we get rid of the terinary and just have global and local? I like… I like what you're suggesting, because I think it's way more efficient in the protocol.
Specify when something's local.
The problem is that means we infer that everything is global for entities, and in practice, that's not safe.
Right now, with most of the entities we saw.
**Liudmila Molkova** 17:06 Oh, you can send… you send global.
You just don't send local if you send the entity type, where you… Send local when you know it's local, but you don't have the parent entity type.
Anyway, these are minor tweaks, we can handle them offline. I… I'm fine either way.
**Josh Suereth (Google LLC)** 17:30 I like the direction, we'll take a look, because I think that, like, anything we can do to optimize the protocol would be ideal here.
And it could be we just change how we deal with unspecified, so… but that's… that's a good, a good comment, like, we'll take a look at that, because I… I do… this has protocol implementations, it has data model implications. I do want more eyes on this so people understand what we're actually trying to do and why.
**Liudmila Molkova** 17:56 Great.
Sounds good. And I could not, not include comment about dot versus underscore.
**Josh Suereth (Google LLC)** 18:04 About what?
**Liudmila Molkova** 18:06 Dot versus underscore for the semantic conventions.
**Josh Suereth (Google LLC)** 18:10 Oh, no, no, you, you should make that, I… yeah.
Those are things that I ignore when I'm focused on high level, and then when I get into details, I care. So I think I just missed that.
Okay, that's all I needed for that discussion. Thanks, everybody.
**Alex Boten** 18:31 Thank you.
Next up, Liudmila.
Talking about span-type follow-ups.
**Liudmila Molkova** 18:37 Yeah, there are a couple of trivial ones. The first one is included in data model. I think I have the approvals. I think Robert left a comment I didn't have a chance to look at.
The one in the middle is explains why the third one is here.
Pass.
So… David brought up a good concern, that in the original PR, that we say things like span name must be something, or low cardinality or span type must be something, and in the API doc.
It's not essentially enforceable, it's the… Kind asks to the users to not put high cardinality data there.
So, David had a good suggestion to put it maybe in the semantic convention requirements, where we can say that the semantic conventions must always Guarantee that spend type has low cardinality.
And… I decided to look around and check what we have.
Across the spec that are… is effectively requirements for semantic conventions.
And consolidate them in the semantic conventions doc.
And I tried to do this with absolutely minimal, disturbance to the existing ones. I don't think we should take span name away from, the API. It's still useful for users. But this is the attempt, I kind of want to hear your thoughts, if it's a good idea.
And… like… How many things would go there versus to this pack itself?
But I think it's still a decent list, like, Alex, if you scroll, if you open the changes, and you open the doc.
Yeah.
So, just, this.
There's a decent amount of requirements that we have.
That, for sometimes were applied to semantic conventions, and here they are.
But, like, things like that's the… Semantic conventions should only do events, not logs.
Or what the… Spend… sorry, event name is… And maybe we can even put some of the things about events here, instead of keeping them in semantic conventions.
**Michele Mancioppi (Dash0 Inc.)** 21:31 I think that there is, a, A few more rules.
that, have similar… very similar to this in the instrumentation score Specification.
that Jurassi and I and a few others have done a terrible job of evolving over time, because we're all super busy.
It might make sense to backport, some of them.
Like, for example, some more… be more stricter about instrument units. Like, you should not use unitary ones, unless you really have to, things like that.
I overall like very much the idea of, documenting these, I think we can add a few more points there.
**Liudmila Molkova** 22:22 Yeah, sure, I… like, this step is to collect what we already have.
That should be the requirements, the semantic conventions.
Okay, this is, to collect high-level feedback, and it's still in draft.
**Robert Pająk (Splunk Inc.)** 22:45 I just have one… I just have one quick question. Maybe you… if you called it out already, then sorry. I thought that some kind of requirements for the semantic conventions were already semantic conventions repo, or not?
I'm just not sure if you are not duplicating stuff that you already have in semantic conventions, and then you will not need to just copy-paste the same text in both places.
**Liudmila Molkova** 23:07 So this, I didn't invent any of these things, they are already in the spec.
So, I took them away from the places where it was okay.
And, yes, some of this.
Could be duplicated in semantic conventions, but we're usually Put a link, so for example, when we talk about spend time, we're saying, sorry, spend name, we're saying, okay, go look to the spec for the spend name requirements.
So I don't think I'm duplicating, but there probably is.
**Robert Pająk (Splunk Inc.)** 23:45 I'm good.
**Liudmila Molkova** 23:45 And we can…
**Robert Pająk (Splunk Inc.)** 23:46 I mean, remember, if I'm not mistaken, I think exactly in Tracing Sync API, we are just refer… instead of refer… I think we are referencing semantic conventions Repo, that you know, that if you create something, you need to follow the semantic conventions. Yeah, and I think if you go to the row right now, Alex.
I think it was about… Yay.
Mmm…
**Liudmila Molkova** 24:18 If this span, look for the span status.
When the state is set to error by instrumentation libraries, description document and predictable, according to the rules defined within the semantic conventions.
Somewhere at the bottom.
**Alex Boten** 24:52 Right in the air.
**Liudmila Molkova** 24:54 Yep.
So, this is a main.
So in my PR, I'll replace it with a link to the file.
And here, we use should lowercase.
And in the semantic conventions requirements, we can use should uppercase.
**Trask Stalnaker (Microsoft Corporation)** 25:31 I always find that semantic conventions… I mean, I find that the semantic conventions markdown file in the Specification repo confusing.
I feel like.
**Liudmila Molkova** 25:47 I think this…
**Trask Stalnaker (Microsoft Corporation)** 25:48 A couple of times, and some circular loops of, like.
Whether it was around stability requirements or some other things that… We kind of mix between the two.
**Robert Pająk (Splunk Inc.)** 26:01 So, Alex, so in the middle, we have the status development, refers to recording errors document, or the details, how to report error signals, and this just refers to semantic conventions. I just thought about adding hyperlinks like that.
Or the semantic conditions, that maybe it will be just easier.
**Liudmila Molkova** 26:20 Yeah, I think the motivation we added this file was that like… SDK, semantic conventions is pluggable to a certain extent.
And no matter what semantic conventions are, they must do this.
And they… this is the way to keep them.
controlled.
But… We might not need this, and if we say, okay, We… Include the wording… the wording for signals in the… let's say API docs or data model.
We can do… I think we can do this if people agree.
**Trask Stalnaker (Microsoft Corporation)** 27:14 I think that, like, cardinality warnings in the spec API are important, because it's for general consumers of the API, sort of.
things that… Their backends are probably expecting… But something like… Following semantic conventions.
For, you know, error descriptions or something like that.
Like, it feels like you've… you follow the spec.
I mean, you use the API as a spec.
You can use it without following semantic conventions, or… You can use it, or you can go to semantic conventions and follow our semantic conventions.
**Liudmila Molkova** 28:12 Yeah.
For something like span type must have low cardinality.
what is the place where it exists? In API, it cannot be normative, we cannot enforce it.
**Trask Stalnaker (Microsoft Corporation)** 28:27 I feel like the… what we've done before is, say that the API must document But… the… It should be low cardinality.
**Liudmila Molkova** 28:39 Yes, is this enough? Because it's not inversible.
**Trask Stalnaker (Microsoft Corporation)** 28:45 Not enforceable, though.
by the SDK, not enforceable, period, by the SDK, I think.
**Liudmila Molkova** 28:52 And this is why it's a requirement on semantic conventions, so it doesn't do something stupid. Well, for the spend type, of course it would, but for the spend name.
It could.
**Trask Stalnaker (Microsoft Corporation)** 29:05 Right, so in the semantic conventions, we document that the… All semantic conventions must do this, at least that we define.
**Liudmila Molkova** 29:21 So we would document it in semantic conventions.
**David Ashpole (Google LLC)** 29:25 I mean, I think documentation on the API is slightly more general than… Documentation on the conventions.
Like, there may be things that don't follow our conventions, but should still, like… follow the API documentation.
But maybe that's… Yeah.
**Liudmila Molkova** 29:49 Okay, so… I'm fine… say Naki just lives in the API as the… indirect.
Wei.
**David Ashpole (Google LLC)** 30:01 Sorry, I meant, the API spec says you must document X.
**Liudmila Molkova** 30:07 Yes, they… yes.
**David Ashpole (Google LLC)** 30:09 Okay.
And I'm happy with that, by the way, in case… yeah.
**Liudmila Molkova** 30:16 I'm not super happy, I feel it's weak.
But that's the existing practice we've been having, and…
**David Ashpole (Google LLC)** 30:23 I think putting in the semantic conventions is also good.
Because that's… Where… you know, people look when they go to define things in the semantic conventions.
**Liudmila Molkova** 30:34 In the semantic conventions repo.
**David Ashpole (Google LLC)** 30:38 like, I would be okay seeing it in both places, some… some things on the API documentation itself, and then… I would be okay having some things repeated in the semantic conventions.
repo itself.
**Liudmila Molkova** 30:55 Okay, so then, essentially, what I hear is that this… Doc.
Or at least the new parts of it.
That are necessary, would make sense in the semantic conventions repo.
**Trask Stalnaker (Microsoft Corporation)** 31:14 But anything that you want that you kind of more generally for… API users to always, you know, to know about.
for example, even, like, a standard error structure, or I don't know, something that we think that, you know, ideally API users should be doing this because backends Are sort of generally optimized for this.
We could document it.
you know, have the API doc Call that out.
We don't necessarily have to link through semantic conventions, or even call it semantic conventions. These are just, like, kind of… this is the ideal way to use the spec.
APIs.
**Liudmila Molkova** 32:02 Yeah, we already have it.
**Trask Stalnaker (Microsoft Corporation)** 32:04 Okay.
**Liudmila Molkova** 32:05 So this is the next trail, and then… I've got my high-level feedback, that is. Probably not. I take it. Not here.
Wonderful. Then, the last part is… There are parts of this dock.
Even if we don't like it, that we can call stable.
And this changes the attributes to stable. I have the approvals. I want to merge it. If you have any objections, let me know. Otherwise, I'll merge it in a couple of days.
Let's say by the end of the week.
That's all I had.
**Alex Boten** 32:57 Thank you.
And Trask, you're next.
**Trask Stalnaker (Microsoft Corporation)** 33:02 Yeah, so GitHub released a feature on Friday that we have all been… many of us have been dying for, which is the giving Maintainers access to security advisories, or an ability to do that. Before, you had to have admin rights to be able to look at… do anything with security advisories, which was a pain, and why we had that. You know, you could ask late to admin in the Terraform repo and whatnot.
So that, I tested out yesterday on the Java instrumentation, and I just… I clicked merge earlier. Let's see, did it go… Yes, yes, it did merge just during this meeting, so that should be across all repos now. Maintainers should have access to their own security advisories.
For their repo.
And there's a couple things that you still cannot do with those rights. One is merge a fix from a temporary private fork.
The… I… that… Doesn't really seem to be the… current practice anyways, though, because, private fork, temporary private forks are pretty useless. You can't run GitHub actions in them, so you can't test your, your patches.
And anyways, even if you do, you think you're being sly by merging from the temporary private fork into main, bypassing a PR.
But, supposedly, it is a… I've heard it's a well-known, thing, and scanners are scanning repos for, commits that show up.
that don't come through PR.
So, it's not really… Saving… any, like… It from being released and known about.
If anything, maybe it makes it more visible.
So, anyway, there's discussions going on in Robert's PR here that I linked to, just… I think the current practice is, when you're, create the temporary private fork to create the PR there, review it amongst the maintainers to get agreement there, that's still very useful.
And, then right before you're ready to set a release, open a PR that doesn't say anything about security vulnerability, merge that, make the release.
There's some discussion, we discussed in the SIG security yesterday, you know, we'd like for potentially to be able to do that better in the future, where potentially we could have Not temporary private forks, but real private forks, or a private org, or something where you could actually… do it all in private, and even release in private, potentially, for, like, something that was, like, you know, a super high security, vulnerability. But anyway, that discussion's still going on. And the only other thing you can't do is manually delete the temporary private fork, but… That doesn't seem very important. We can clean those up from time to time.
**Alex Boten** 36:50 Yeah, I guess as a… as a side note, if you haven't looked at this, conversation, please go and… Review and add your comments if you have any.
Because I think this is trying to maybe standardize how we… how we handle these moving forward across the org, because I guess it's been inconsistent so far, so…
**Trask Stalnaker (Microsoft Corporation)** 37:19 Cool, and that's it, unless there's any questions about it.
**Carlos Alberto Cortez (Dash0)** 37:21 Now, I just wanted to say that, yeah, I'm happy that that conversation happened with the SIG security group. I was concerned about that. Thank you so much.
**Alex Boten** 37:38 That was the last thing on our agenda.
Are there any other thoughts, conversations people want to have?
**Jason Plumb (Splunk Inc.)** 37:52 Is there any way to clear a meeting from the calendar for tomorrow?
Or we just let it… we just let it ride.
like a SIG meeting.
**Josh Suereth (Google LLC)** 38:04 Dude you can go in and delete it from the calendar if you have read-write access.
What I do, though, because I don't trust it, is I just change the title to be canceled.
And hope that people notice that the invite has now canceled the meeting, you know?
**Jason Plumb (Splunk Inc.)** 38:21 Yeah, that's cool.
We also put a notice at the top of the dock, but…
**Josh Suereth (Google LLC)** 38:28 People will join no matter what, because some people duplicate the calendar entries, so there's not a lot you can do with that, yeah.
**Trask Stalnaker (Microsoft Corporation)** 38:38 We could cancel… I mean, I could automatically cancel, like, all Thursday and Friday meetings this week, potentially, if there's… No.
**Jason Plumb (Splunk Inc.)** 38:51 And assuming… assuming that we… Cancel all the ones during that week of shutdown.
**Trask Stalnaker (Microsoft Corporation)** 38:58 Yeah, we usually do that. Yeah, those two weeks, yeah.
**Jason Plumb (Splunk Inc.)** 39:02 Yeah, yeah.
**Trask Stalnaker (Microsoft Corporation)** 39:08 I'll post in the Maintainer channel about Thursday, Friday. If nobody objects, I'll just wipe them all out.
**Alex Boten** 39:26 Alright, guess everybody gets, 20 minutes back.
Thanks, everyone.
**Liudmila Molkova** 39:33 Thank you.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 39:34 Yep.
