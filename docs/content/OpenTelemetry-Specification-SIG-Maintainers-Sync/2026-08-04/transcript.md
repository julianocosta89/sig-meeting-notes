SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-08-04
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang (Microsoft Corporation)** 03:32 Hello, Era.
**David Ashpole (Google LLC)** 03:36 Hey, Reiley.
Everyone.
**Reiley Yang (Microsoft Corporation)** 03:40 How you doing?
So, let's start in 2 minutes.
Okay, can folks see my screen?
Yep. Can you see my share screen? Okay.
**Jason Plumb** 05:45 Yep.
**Reiley Yang (Microsoft Corporation)** 05:47 Let's wait for one more minute to get started.
Meanwhile, Tigran said he cannot join, so… If you have the time, please review the PR from him.
For folks who haven't put her name, please do so right now.
We'll start here a minute.
Okay, let's get started. Hello, everyone. Welcome to the meeting. So let's start with, Josh and Dan.
**Josh Suereth (Google LLC)** 06:41 Okay, yeah, so this is a continuation of a discussion apparently happened yesterday around scheme URL and behavior with entities. Not yesterday, sorry, last week.
We discussed this briefly in the entity SIG, this is, Is this the right… yeah, this is the right one.
So, I think there's concerns around the behavior of schema URL for resource. There's an open bug about how schema URL behaves, and then, discussions about the, hotel entity's opt-in, like, flag that we want to use to kind of turn it on and off, and whether or not things are stable. So… To start with the discussion, I'm just gonna ground some things first. One is, There's a bug around resource schema Euro.
If you… the bug is linked somewhere in these discussion notes, or in here, but the bug basically calls out that No OpenTelemetry SDK really abides by the specification, and if you were to abide by the specification, the behavior's kind of poor. Sorry, not no, Python still does, but most other SDKs have moved off of the actual specified behavior for resource schema URL.
Thank you, Daniel. You're Dan.
So… That's the… that's the issue linked to chat.
what this means is, effectively, if you have a resource that defines a schema URL, and you have one that doesn't.
The behavior is undefined, what happens.
It is up to implementations to decide now.
So some actually drop the resource.
that doesn't have a schema URL and consider it a merge conflict, some don't and keep it.
**Robert Pająk (Splunk Inc.)** 08:31 Really, if you scroll down a little, there'll be a quite new table.
Not… not Tyler's comment, but other comments.
**Josh Suereth (Google LLC)** 08:40 Yeah, Robert did a survey of this, yeah.
So…
**Robert Pająk (Splunk Inc.)** 08:47 A little below, really.
**Josh Suereth (Google LLC)** 08:48 Yeah, it's further down.
**Reiley Yang (Microsoft Corporation)** 08:56 This one?
**Robert Pająk (Splunk Inc.)** 08:57 Yes.
**Daniel Dyla (Dynatrace LLC)** 08:58 S.
**Josh Suereth (Google LLC)** 09:00 So you can see what the behavior here is, right?
Now, the issue is that today, with schema URL, it's actually somewhat problematic, because we have resource detectors that are in different libraries.
And so, if you… have a resource detector in, say, the Go Standard SDK, and then you have a resource detector in, say, an instrumentation library, or Go Contrib, the version number might be different. And by specification, that means, by default, if you get different version numbers.
Across any of your resource detectors, you have to drop the data.
Of the conflicting thing.
Which is really bad for users. And so, none of the SDKs do that anymore based on user feedback and bugs, and we're trying to kind of fix that, right?
**Daniel Dyla (Dynatrace LLC)** 09:49 Except for Python.
**Josh Suereth (Google LLC)** 09:50 Except Python, yeah. Python is… still abides by the spec. And I… I have some theories for why they can get away with it, but we can… we can go into that later.
They… So… what we have in entities now is instead of defining one single schema URL for the whole resource, we have schema URLs for each entity, which is a group and set of attributes. And so what we want to do is allow this to succeed in the future. So if you have a resource that used to drop data by spec.
Now, by spec, you're allowed to join these things, and the schema URL is actually found in a new location in the protocol.
Okay?
Technically today, most of the behavior here is kind of undefined behavior, or violates the spec.
So, what we'd like to do in entities is kind of make that successful now, and our proposal initially was the schema URL that's reported.
Unless that schema URL accurately represents every attribute in the resource, It is dropped.
So that's how the current schema URL merge algorithm is listed to behave, and that is what this particular PR is proposing.
And we think that's a reasonable compromise of, we're going to allow mergers that you could not do previously by spec, or had undefined behavior.
We're gonna make sure that if a schema URL exists, that it's accurate, and if it doesn't exist, we remove it, which means, you know, it doesn't mean there's no schema, it just means we don't know what it is.
And if you need to engage with entities, because Entities, gives you the fine-grained schema, you can do all of the fancy, things that you need in, like, Weaver Live Check, compliance testing, all that kind of stuff, because the original schema URLs are preserved in this new field.
We also plan to eventually deprecate schema URL and resource completely, and say, don't use it.
So, we need to define what the behavior will be going forward for schema URL for resource, and what we consider breaking changes.
And we can go into various details here, but I'm gonna posit something forward. I think we have two real options here. The behavior that's defined today is meant to give you the most accurate schema URL possible in OpenTelemetry, given how things actually work, right? The schema URL will be accurate when it exists, and when it doesn't exist.
cool. Like, what you would have gotten before was non-accurate, so it's, like, not super useful, and could fail compliance validation checks.
The second option we could do, and this is one we were talking about in the entity SIG, is we actually from an entity standpoint, to some extent, we don't give a crap about schema, URL, and resource, because we plan to deprecate it, want to remove it. So if we want to just say it keeps the existing behavior you would have had anyway.
That's fair. The complication is we're allowing merges that weren't allowed before, so we have to define what happens for those merges.
But otherwise, like, from a user standpoint, practically, if you look at this behavior that's happening, we don't think there's any breaking change outside of there might be places where schema URL no longer exists, where before it existed but was wrong.
Okay, with that, I'll leave it for questions and things. Go ahead, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:14 Alright, so you mentioned…
**Reiley Yang (Microsoft Corporation)** 13:15 time check. We don't have a lot of topics, I think it's fine to give additional 5 minutes.
**Josh Suereth (Google LLC)** 13:22 Okay.
Oh, I took too long in my intro, I'm sorry.
**Reiley Yang (Microsoft Corporation)** 13:25 No worries, John.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:26 Reiley, can we make that 10 minutes? I can just kind of see where this is going.
**Reiley Yang (Microsoft Corporation)** 13:31 I'm doing that.
Yeah, please go ahead.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:34 Josh, you said something in there, towards the end. You said, when talking about, like, you know, another option you could do is to, You said it… what did you say? Like, update the merge definition of resource, because we're doing merges that weren't previously allowed.
And so, I guess, the thing that was confusing about that for me is we all agree that, like, resource merge is broken today.
And so, like, why does entities… why should entities need to fix it?
Like, I agreed with the first option that you gave, which is just, like, you know.
Entities doesn't care about resources. Entities wants to deprecate resource schema URL once entities is stable, and so just, like, leave it as is. Sort of, don't try to fix the mess, you know, just, you know, let it continue until we ultimately deprecate it, but don't make it your responsibility to fix these long-standing problems.
**Josh Suereth (Google LLC)** 14:38 I mean, so… so the answer there is the reason… one of the reasons SIG exists is because of this bug. Like, we designed entities to solve this problem.
So then, like, if you're.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:48 You are gonna solve this problem.
**Josh Suereth (Google LLC)** 14:50 That's our charter. Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:52 But you fix the bug, through, basically having… going from having one schema URL that attempts to define, like, you know, lots of different components of the resource, to having entity-specific schema URLs. So that's the way that you fix it, right? So don't… right, so, like, don't try to, give the impression that you can fix this at the resource level, where there is only one schema URL for the whole resource.
**Josh Suereth (Google LLC)** 15:17 Right, for context, we never intended to fix schema URL, but… but, like, from… and it's unfortunate Tigran's not here, because he asked us to do this. As a best effort.
We're trying to give you a valid schema URL where we can, but we don't really care about it, or will recommend its usage, right? Because we think it's just fundamentally broken.
So, that, like, that's kind of our stance right now, is, like, the merge algorithm we have defined, and again, Tigrin approved it, was its best effort It is, when it's there, it's accurate.
But, it will not be there very often, and we think that's okay, and actually better for users.
Go ahead, Robert.
**Robert Pająk (Splunk Inc.)** 15:59 Okay, so I think my comment, Jack's comment is kind of in line with my, with my feedback that I give you, you know, on DPRs and also privately on Slack. So, my thought on that is that, you know, once you have this, schema URL on each entity, then you know the systems that ZRA entities do not care about the schema URL.
And my feedback was basically, make the schema URL, You know, behavior similar to what the languages already have.
So my feedback was basically that the specification that is right now, is, is saying, you know, you said it to an empty null, but, you know, in these languages like Java, Go, there are other, you know, mechanisms that also report there is a conflict.
just to… and I think this behavior could be retained for backwards compatibility, and right now, you know, if you literally read the spec, you'll just, you know, you'll just skip this kind of additional notification that there was some, some… so it was mostly, like, a neat comment, and I was not sure if, you know… So, if it was that much important to, you know, to say what should be the schema URL, it should be more, like, less, you know, keep the previous behavior from the schema URL Probably except Python.
**Josh Suereth (Google LLC)** 17:30 This goes into my question, because the behavior you're mentioning is actually unspecified.
It's, like, part of the spec that says we don't specify what to happen here, if you read that, when we get one of these conflicts. Like, it was left unspecified. So, like, I don't think there is a spec for us to hold to here, like, we could do whatever the hell we want, honestly.
But the second thing would be, is the error reporting important to you? Because again.
One of the things entities does is it's no longer an error.
to have two pieces with different schema URLs, because we can successfully merge them and understand enough about resource that that is now okay, and I don't want it to admit an error, because it's not an error. It's actually a thing people did legitimately, and that's what the bug in the original resource merge was, was it considered it an error when it should not have.
**Robert Pająk (Splunk Inc.)** 18:22 Okay, so if… if the backend understands entities, then yes, it's not a problem.
But if there's an instrumentation that, you know, that user make this error, and the backend doesn't understand to rely on the resource and the conflicts, then I think it might be a problem. Probably is an edge case.
But I can imagine a scenario that can be a problem, you know, when the backend is basically not up to date with the instrumentation.
**Josh Suereth (Google LLC)** 18:53 So, I… if you can give me an example of, like, what that failure would be, that would help, but, like, the, So previously, like, the use case we're talking about is not allowed by spec, right? Where there's two different schema URLs. So if we agree that wasn't allowed by spec, what we're proposing is entities would allow the merge to happen with no schema URL, which is in line, like, I think that should not break backends.
**Robert Pająk (Splunk Inc.)** 19:19 So, the only difference was the behavior of merging with something which had empty schema URL, so people are often adding, you know, these attributes, which I call, you know, they have this, you know, hidden schema URL, which was not possible to add, you know, before entities, but right now you made it possible.
And the problem is if there are some existing, you know, processors, some existing detectors, which rely on this behavior. And I think this is the thing which may be breaking some users.
**Josh Suereth (Google LLC)** 19:50 That's kind of what I'm going to argue, is I don't think it is actually breaking. I think the behavior was completely undefined by the spec.
The spec says you do best effort. It doesn't matter what you do here. What we're doing with entities is we're saying, like, if schema URL exists, it should be accurate. And again, I don't need to care here, because I don't… I don't… honestly, if schema URL is wrong on resource, because we're saying we think it's broken, don't use it, and it's going to be deprecated, cool.
But what we're seeing now is there are some…
**Robert Pająk (Splunk Inc.)** 20:20 I go here.
**Josh Suereth (Google LLC)** 20:21 Are you thinking?
**Robert Pająk (Splunk Inc.)** 20:22 here, because the specification was not… was not specifying merging with empty SQMRL as an error. It was a legitimate use case. I would agree with you.
**Daniel Dyla (Dynatrace LLC)** 20:34 The spec does allow that.
So, there's 3 branches of the spec. One is schema URLs match, everything is good.
The other is one schema URL and one empty. You take the populated one.
And merge.
**Josh Suereth (Google LLC)** 20:52 You keep the.
**Daniel Dyla (Dynatrace LLC)** 20:53 And then the third branch is two…
**Robert Pająk (Splunk Inc.)** 20:55 And that's my concern.
**Daniel Dyla (Dynatrace LLC)** 20:56 URLs, and that's the undefined part.
**Robert Pająk (Splunk Inc.)** 20:59 And the second branch is the problem mapping.
**Daniel Dyla (Dynatrace LLC)** 21:02 Why is it a problem?
**Josh Suereth (Google LLC)** 21:04 if you want to keep that, we can keep it. I think that's actually broken behavior. Like, I actually, like, when that was in the spec, I called this out as well.
I don't think that's a legitimate use case, I think that's actually broken, because now the schema URL is invalid. You can't actually… like, if somebody doesn't specify a schema URL, the only thing you can assume is that you don't know what the schema is. You don't really know if it's a mergeable schema.
And what we made the allowance for in the spec was to fix a bug where we were rejecting too many resource merges.
Which, again, goes into the fundamental issue that schema URL at the resource level is wrong, it has to be at a sub-resource level, which is what Entities is trying to fix. So it comes down to, like, dependency on schema URL. Anyway, if you want us to change the merge algorithm to protect the existing behavior, all we have to do is specify what happens for the new use case.
And that's okay, but, like, I… I still think the behavior is broken today with that. I would rather see it be an empty schema URL, because what you're saying is, I haven't specified a schema URL.
You know, like, there is nothing that I could use to validate. If we start adding compliance tests that use schema URL to validate compliance to schema, they would break.
**Robert Pająk (Splunk Inc.)** 22:19 There's an important… I don't disagree that it would be better. I'm just worried that, you know, ship has sailed and people rely on it.
**Daniel Dyla (Dynatrace LLC)** 22:30 There is an important use case that, like, and I think this… the… I don't remember which SDK we were looking at in the entities meeting yesterday, that there are… Like, vendor, Distros that want to add like… This is the district, like, the vendor-specific information to the resource.
And… if, like, they can't use the upstream schema URL because they don't know what schema URL you're using.
And their vendor-specific stuff won't be defined there anyways. If they define a vendor-specific schema URL, that's a conflict, and, you know, Python would drop it.
And we don't have a recourse for them, so right now, they just don't define a schema URL. Those attributes get added, and then the validation Skips them, or you don't do the, you know, whatever… the validation behavior could be, whatever it is.
**Josh Suereth (Google LLC)** 23:31 Yeah, let's talk about what we want in the entity world there. Those vendor-specific telemetry things do have a schema URL. We know what that schema URL is in that vendor. Like, they've decided to go to, like, semantic convention version X.
So they would make an entity that has the schema URL, it'd be preserved on the entity.
And then, because those attributes are disjoint from the other entity that has a different schema URL, we would actually keep both schema URLs, so you know one's on version 1.x and one's on version 1.y, but they're still both Semconv schema. That's the behavior we want in the long term, because you know that you're abiding by semantic conventions in both sides.
All the compliance tests pass, right? But by default, then, we now have a version conflict.
So, the schema URL will become empty, in that case, on resource, going forward, right?
So, like, we… again, this… if you assume we're going to keep this notion of schema-less, great, but I don't want to. We want to move to entities, where that thing actually provides an entity, which is the telemetry distro, which has a schema URL. So now I have a conflict. So this use case we're talking about disappears in the entities world.
**Daniel Dyla (Dynatrace LLC)** 24:39 Yeah, and instead of just adding attributes to the resource, they would add a vendor SDK entity, or something like that.
**Josh Suereth (Google LLC)** 24:47 Yeah, I think it's called Telemetry SDK, is the name of the entity in Synconf, yeah.
**Daniel Dyla (Dynatrace LLC)** 24:51 Right, but there might be stuff that's not in our semantic conventions that a vendor wants to do, and they would just put that in their own… I can make… mine.
**Josh Suereth (Google LLC)** 25:00 100%, yep.
So that's where, like, we can go through… like, I think it will take… the reason I'm saying this is I think it requires us to jump through hoops to keep the existing behavior.
Whereas, the thing we're defining is very simple around Schema URL. If they all line up across entities, you put it there. If they don't, you make it empty. Done.
Simple, easy to understand, accurate for users, and in the future, when we want people to use schema URL and resource.
we will start to see more conflicts, whereas before we… people aren't using Schema Reyall because they can't. Like, that use case of the Splunk, the Splunk schema-less attributes. You would use schema URL if it didn't lead to a conflict. Is that accurate?
Okay, well, cool. I want to get to that future of, like, where you will use this, so we can do the validation, so we can do all that, right? Like, that's the goal, yeah.
**Robert Pająk (Splunk Inc.)** 25:53 like, I'm also not so much, you know, so much concerned about, you know, our distro, because we'll update it anyway. I want some more concerned about other stuff. I also do not remember how the algorithms will work when you have, you know, because I'm okay with I remember.
Yeah, okay, nevermind.
**Reiley Yang (Microsoft Corporation)** 26:14 Can we park this topic now, because we already used 20 minutes, I want to make sure we have time for the other… other topics. And if we do have time, in the end, we can come back and continue the discussion. But meanwhile, I think folks brought a lot of ideas during the discussion that's not… probably not captured in the PR, so I would suggest if you have those, like, additional contacts you haven't added to the PR yet, please add those comments. I think that would help to encourage more feedback.
So let's move on, Robert?
**Robert Pająk (Splunk Inc.)** 26:48 Next one is Jax PR, which I think you can open, and I was just, yeah, this one?
And I was just thinking that it may be a good last goal for us to review, and probably it will be good to match tomorrow.
I will not be able to merge tomorrow, because I'll be on vacations, and I'm not taking my laptop.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:11 I'll merge it tomorrow if there's no conflicts. Yeah, this… this should be uncontroversial.
**Carlos Alberto Cortez** 27:21 By the way, out of curiosity, I didn't see that, although this looks correct, especially that it has mentioned in the protocol repo. But the people discuss what happens when you have split that because of this? I know that there's already language in the spec about this.
They want people to be aware of that, of the potential ramifications.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:42 If I remember correctly, if you exceed one of these limits, we essentially error.
So we don't attempt to split.
**Robert Pająk (Splunk Inc.)** 27:56 That's weird.
**Carlos Alberto Cortez** 27:58 Okay, I will follow up in case I think it's not clear. I mean, in case it's more like it needs, like, a bigger text or something, but thank you for the clarification.
**Reiley Yang (Microsoft Corporation)** 28:09 Okay, next topic, also yours.
Over.
**Robert Pająk (Splunk Inc.)** 28:14 This one was about, the depth land, the depth limit of the attributes.
And I saw, that Jack made a prototype in Java and approved, but later… but I saw also today that his… your prototype job was closed.
But I guess it was just the reason that it was not the way that you think it's efficient to implement, not that you are not accepting the specification. I just want to make sure that this is the reasoning, and to double-check, so if it's still approved by you or not anymore.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:52 Yeah, that's correct. The prototype that I built was trying to conflate a couple of things. It was trying to add this new limit and also try to converge a couple of different attributes implementations that we have in Java. I closed the PR because I think the convergence is a dead end, but I think this new limit is specced correctly and is implementable in a reasonable way.
in Java, so…
**Robert Pająk (Splunk Inc.)** 29:19 So it's similar to Go. It's also not something that is similar, it's also, like, exploration of implementation things, and also trying to tackle two things at once.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:29 Correct, correct. They were sort of related topics, so, I was trying to do two things at once.
**Robert Pająk (Splunk Inc.)** 29:34 Same.
And also, you asked Tigran, who is unfortunately absent, to take a look, but if I remember correctly, he even a few times said that, in his opinion, a lack of limits is just a but, and everything should have a limit. And I think it was pointed out a lot of times by Tigran.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:55 You know, ironically, a couple of weeks ago, when we talked about this at the spec, it was Tigran who brought up the point that, like, maybe this shouldn't go straight to stable, maybe this could go through the normal maturation process, and so I'm not sure where he falls today. It seems like he's taken both sides.
So, I'll leave it to you, Robert, in terms of, you know, deciding when it's been enough time for Tigrin to potentially, object to this dissent. You know, you have merge rights now, so,
**Robert Pająk (Splunk Inc.)** 30:31 Would it help for you if I will merge it right away? Because probably I will… I will be also, like, 2 weeks out, so I'm not in a rush to, you know, to merge it and also please go.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 30:42 Yeah, I think that's… I think that's fine. Does anyone else disagree? I mean, you know, we can always, I guess, technically revert before the release if Tiburin comes back and has a strong feeling otherwise.
**Carlos Alberto Cortez** 30:52 Well, this is the start of the month, so we'll be releasing hopefully this week, so… I don't know. Or we can merge right after we do the release, on your behalf, even if you're gone, Robert. I don't know, are you going next week, or this week?
**Robert Pająk (Splunk Inc.)** 31:06 So, I think, Carlos, you can just merge it after the release.
**Carlos Alberto Cortez** 31:09 So, can we leave a comment there, so we don't forget, instead of it going instead of something? Yeah, thank you.
**Robert Pająk (Splunk Inc.)** 31:14 Thanks, Reiley.
**Reiley Yang (Microsoft Corporation)** 31:39 Okay, thanks.
Let's move to… Martin, it's yours.
**Martin Kuba** 31:44 Yeah, hi, I'm here on… On behalf of the browser SIG, I've been asked to… Give an update.
And I just… I can do that either today, or I can get on a schedule, I've kind of estimated about 10 minutes for this.
**Reiley Yang (Microsoft Corporation)** 31:59 We have time.
**Martin Kuba** 32:00 We have time, okay, great.
**Reiley Yang (Microsoft Corporation)** 32:02 Do you want to share?
**Martin Kuba** 32:03 Yeah, I'll share.
**Reiley Yang (Microsoft Corporation)** 32:04 Okay.
Okay, I can see your screen.
**Martin Kuba** 32:20 Okay, okay, great. So, yeah, so I have, some list of talking points here, so, Yeah, so I want to just talk about really quick of what we have done, what we're working on right now, where… what's our plan, working on… what to work on in short term, and I also have a few things that I think we might need help with.
So what we have done, the browser SIG has been, now active for about a year. We have… a dedicated repository for browser, and we have, kind of converged on, the maintenance and governance, approach. We have a release process, versioning process. We have… We have worked on instrumentations, we have now a package on NPM that, that's for the instrumentations. It contains 7 new instrumentations.
We also have, published a package for an SDK, or initial version of browser SDK.
That's a separate, package on NPM.
And we have also been working on, making it, easier for users to see what kind of, data we are producing. So we have this sandbox, which is, which can be run locally, or it can be, accessed on, GitHub pages, the, The… I think the main thing is the instrumentation, so as I said, there are 7 new instrumentations, they're all event-based, and they cover most of the important telemetry from browsers that we thought was the most important, yeah.
We have also had a lot of discussions about, different things like API direction, widget process we should support, the data model, which links to the instrumentations, we… I think we have made a lot of decisions here. We have probably some gaps in documentation that we're currently working on.
I can get into details if anyone's interested, but I'm gonna move on here.
For now, currently what we're working on So we have… I mentioned the instrumentations, we have still two, instrumentations we're working on. That's the Fetch and XHR, which… have existed historically in the GS Core repo, we are moving them over to the browser repo, and we're also making them compatible with the new resource timing instrumentation.
We're working on improving our documentation, and also, we have this, PR… Open for, a roadmap, that we think for the, for the, for the near future.
We have… we feel like we have accomplished what we wanted to over the last year, as far as, like, the phase one project. So this roadmap… It also talks about, like, our vision going forward. It's not merged yet, so if you're interested in this, please go ahead and, you know, comment. I'll link this in the notes.
What's next? So… We are working on package consolidation, so historically, Browser has been… part of the JS JavaScript SDK, and there have been a lot of different packages in the core repo and in the contrib repo. We want to consolidate everything into the new browser repo.
So that's, like, the single place where users can find everything related to browser. We have still some work here, we want to finish the FetchXHR, and we want to then go and deprecate the old packages.
We want to continue working on semantic conventions, so… Yeah, so none of them are currently… well, there are two that are part of the semantic conventions repo, but most of them actually are not documented, so we want to work on this.
the SDK, we want to, continue iterating on the… on the published package, and work towards stabilization. And then, kind of big topic is sessions, and… Potentially page context, we think that these should be modeled as entities.
That's something that we want to work with, also with the other client SIGs, like, like the mobile SIG, to align on our approach to man, handling sessions.
Yeah, so what'd we need?
there are kind of 3 big buckets that I can think of, that we might need help with.
One is, I just mentioned sessions.
We… sessions is a kind of a big topic for us. We believe that should be the… they should be modeled as entities. That has impact on the SDK. Sessions can essentially change during the lifetime of the SDK, so we need to have a, We need to support changing entities and changing resources in the middle of the SDK lifetime.
Metrics, this is somewhat related to sessions.
We currently… Don't… are not focusing on supporting metrics, because we feel like the main signal is events from client SDKs, but we got some feedback that having some support for metrics would be good.
And so we were kind of thinking how to approach this long-term.
One idea that we've had is, is maybe have, like, an API for metrics that actually, behind the scenes, just produces measurements or events, and the aggregation happens in the backend. I think this is a big area we might need help with.
From this group, just see if there's something that we can diverge.
From the spec, or if we, if you need to somehow document it here.
And then, semantical mentions is a big, big area for us, like, as I mentioned.
We, we need to document, Will be the data that we produce, and so we are planning to follow this new federated semantic conventions model.
Yep, and… just, yeah, just, just might need help with direction here and the details.
I'm gonna stop here for now.
Any questions?
**Carlos Alberto Cortez** 39:24 Do you dirty Sorry, Goka, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 39:27 Yeah, no, I'm just… I'm absorbing.
So, the, the sessions as entities piece, I guess, like, which parts of the what we need do you view as, like, maybe controversial, or risky, or taking a long time, and, you know, thus would benefit from being set in motion sooner rather than later?
**Martin Kuba** 39:59 So I think from just the implementation, implementation perspective, We, we have a prototype for… for how to handle it in the log… log provider.
And… so I think there was some work done in, in, you know, in support changing entities, but it doesn't exactly work for us, so, Yeah, so, like, if… I don't know, I don't know, like, if the implementation of the provider that would handle, like, changing entities behind the scenes is something that we need to spec out. And also, then, the metrics.
would be, like, I think that's the biggest, biggest, probably, question.
Like, the metric provider aggregation, yeah.
**Josh Suereth (Google LLC)** 40:49 Yeah, I'm gonna jump in and say I think, 1 and 2 are related. Like, the reason we couldn't give you a good, entity-based SDK thing was because metrics are really hard, but if you're streaming events… You can do… like, we had a prototype for logs and spans that worked well, that would work for metrics as events, where you aggregate downstream.
that I think gives you what you need. So, like, just for some of the things of, like, sessions as entities, does session as an entity make sense? I think 100%, but the SDK doesn't work well for you there. Yeah. And so that leads to two is a big issue. So, yeah, I… I have… I have some questions on that, of, like, what… where your prototypes are, whether I can look at them and help, but yeah, this seems… this seems right to me, and the metrics thing. I really like the… the way you're going with that, and what you're thinking there. So I'd be… I'd love to see, like, what what your plans are, but the notion of a metrics SDK that emits events that are aggregated downstream, super interesting to me. I think that's the right way to go.
And I think lines up with sessions as entities, too.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 42:01 So, So there's… there's a prototype, in the browser repo that sort of embodies how, you know, the SIG could… envisions, entities and sessions working together in a way that the session can be updated at runtime and new data emitted with the new entity. What I would love to see is, like, somebody to take a crack At, taking that prototype, which works for you all.
And in mutating the spec, modifying the spec to suit. Like, what is the minimal set of changes that would be needed to change the phrasing of the spec to be able to, like, allow that prototype to be compliant?
Because, you know, I guess, you know, I haven't taken a close look at, at the prototype, and… And, you know, I guess that's the thing that worries me, is like… is, like, how… how, like, aligned or disaligned is it with the entities piece? How… how, how abrasive is it? Is, like, the idea to, like, what the rest of the SDK maintainers would consider? And, you know, if there is going to be, like, a long argument about it, let's start that sooner.
**Martin Kuba** 43:31 Yeah, so I guess check out, I don't know, like, if the help that I would… Could use with is, like, the direction of, like, what exactly we need to specify, or what kind of thing we would need to, update the spec with.
Like, do we need, like, a new spec for client SDK specifically, or, like, do we update… the existing spec, like, with some clause for client applications, or how exactly to approach this?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 43:59 I think it depends on what the implementation is doing, like, Whether you can… you can carve out the language in a way such that, like, you know.
only logs and spans, the non-problematic signals are affected, and thus, like, whatever ideas you come up with can, you know, are applicable across all languages for logs and spans, or if, you know, you need to carve out the exception specifically for browser.
I'm not… I'm not sure, like, you know, somebody has to do that analysis of what the entity spec says, what the various SDK spec says, and, you know, just… Just, you know, figure out how the prototype conflicts with those, and what language would need to be changed so that the prototype does not conflict.
And I don't think the direction is obvious or intuitive. Whoever's making those prototypes sort of has to… Just to run with that.
**Martin Kuba** 45:02 So what would be the next step here? Like, should I, should we, like, create an issue, like, in the spec for this, or should we unlink the prototype, or should we just go ahead and try to draft this?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 45:16 issue, or if there's an existing issue that embodies the problem, like, latch onto that. And, you know, a really… a really clear, concise, you know, description of what the problem is with, like, code snippets, I think, is helpful. You know, obviously linking to the prototype is helpful, but, like, what is the code flow that you imagine?
The sort of pseudocode that would allow you to accomplish your goals, and that sort of paints the picture for everybody to easily understand.
**Martin Kuba** 45:48 Okay.
Okay.
Sounds good, thank you.
**Reiley Yang (Microsoft Corporation)** 45:54 Okay, we're 4 minutes past, let's take the last two hands.
Did Milla, I guess you'll go for it.
**Liudmila Molkova** 46:01 Yeah, Martin, thanks for coming. I want to check, like, if… if we can do something to… to collaborate more on semantic conventions, because, like, you have questions about federation and… There are a lot of things, we could share about the, okay, if we define this metric… Sorry, if you define the semantic conventions, you can actually use the formal definitions, and life check your instrumentations against them.
There are a lot of cool things we can do, but we didn't have a lot of browser folks in the semantic conventions meeting.
like.
How can we collaborate more? Is the meeting time bad, or, like, what can we do to work more together?
**Martin Kuba** 46:45 Yeah, unfortunately, I do have conflict, like, standing conflict for that time, but I can… maybe I can see if I can, Either, either try to change, change that, or maybe some of the other maintainers from the browser SIG can make it. I'll bring it up in the SIG.
**Liudmila Molkova** 47:04 Awesome, and I think we are out of time, but I would love to learn more about the browser SDK. Why do we need it? What are the design choices that led to it? Maybe we will reserve it for some other time?
**Martin Kuba** 47:18 Okay, we can do that.
**Liudmila Molkova** 47:21 Yeah, thank you.
**Reiley Yang (Microsoft Corporation)** 47:23 Okay, Josh?
**Josh Suereth (Google LLC)** 47:24 I'll be very brief, I promise. So, Martin, I think we should work on an OTEP. It looks like you're writing entities to a context, and then using that in the processor to update the resource. I love it. I think this is actually the extension to the OTEP we had previously for multi-resource.
SDKs, that makes sense. The metrics is gonna be the hardest part, which is your number 2. So, yeah, like, it might make sense to start working on OTEP, pull in some of Carlos' context scope attribute stuff.
But I would call it maybe context-scoped entities, and go from there. But I really like that direction, I like your prototype, and we should continue. But I think getting an issue and getting an OTEP is the next step.
**Martin Kuba** 48:06 Okay. Yeah, I might, I might need some, some help or some direction there. Jackson, maybe I'll, I'll, I can share some early drafts with you.
**Reiley Yang (Microsoft Corporation)** 48:17 Okay, thanks, Ara. Thank you, Marty.
De Miller.
**Liudmila Molkova** 48:25 Oh yeah, this is a quick update, maybe, we will do it fast. So if you… Martin just gave an update, that's awesome. But we got kind of slow on, updating… updates from other SIGs.
So, what would be… Great, if we… Had more volunteers, but also we could have rules that are a bit more… Interesting, so if you… there is a second tab here, SIG Updates.
And, it will be a log of the… Updates that people were given, but there is also some context there.
In a short, it would be awesome if every time the SIG starts, or the project starts, the people would come and present the scope of the project, the things they want to achieve.
And just to introduce… themselves to everybody else, or their project, so we just know what happens around.
And when somebody hits a major milestone, that would also be a great time to give an update.
So, for example, it would be great to learn about what, led to JavaScript SDK 2.0, and what are the findings? Like, how did it go? Or the Java Agent major release approach?
How does it work, and what are… when it happens, how do we know that we want to cut a major version release? And, all the other things, you can find, like, some ideas in the SIG Updates tab, in this document.
And you can either sign you up yourself in the schedule here, or you can… it will be the TCU on call responsibility to maybe look ahead and find some possible, SIGs to present.
essentially, if you're a TC sponsor or GC sponsor, we would love you to nag your SIGs, well, maybe nags gently, to present in this SIG… in this pack, so that just we have some common understanding of what's going on across the project.
That's it.
**Reiley Yang (Microsoft Corporation)** 50:58 Yeah, thanks, Li. I think the idea is great. Do you have some, like, proposed doc or something that you can share here? And also, Martin, for the doc that you shared before, it'll be nice if you can put a link in the meeting notes.
**Liudmila Molkova** 51:13 But there is a tab here, SIG updates.
It's essentially there.
**Reiley Yang (Microsoft Corporation)** 51:19 The last one, or…
**Liudmila Molkova** 51:21 the tab.
So you asked if there is a dock.
There is a tab in this document.
And I don't know about the Martins…
**Reiley Yang (Microsoft Corporation)** 51:31 Oh, yeah, okay.
I can copy the link here.
Anyways, I'll fix the formatting issue later.
Okay, so you want people to review this and add comments?
Good.
**Liudmila Molkova** 51:51 Yeah, but mostly I want people to be interested, and if people are not interested and have thoughts why… how we can make it better.
Communication across the project, send them my way, or leave a comment there.
**Reiley Yang (Microsoft Corporation)** 52:05 Okay.
Okay.
This is great. Let's move on. David?
**David Ashpole (Google LLC)** 52:33 Great, just quick update on composable views. I think it's got the approvals?
To merge, but I'm not in any rush, so I'll probably wait to the end of the week. I did want to call out one update, I think, since the last time I walked through this, but, initially I had it as first wins to match some of the other, behavior in the SDK.
But all the people I talked to, Including myself, thought that Last one's was more intuitive, so… I think going with our gut is probably… Probably good here.
If you're interested, please review. Once it merges, I'll start working on experimental implementation in Go, so looking for other… other language maintainers that are interested in helping out.
And then, after that, I will probably resurrect the opt-in instrument.
Proposal from earlier this year, and… Yeah, continue on.
But that's it.
**Reiley Yang (Microsoft Corporation)** 53:42 Thanks, David.
Yep. Yes, for folks who haven't got a chance to look at the PR, please do so before the end of the week.
Thanks.
Okay, Lilmila?
**Liudmila Molkova** 53:54 Yeah, I started talking about the spend type last week.
And I've got some support, but I've got some, comments, and… Concerns around the… Spans having a single pipe?
So, in a brief, what this setup does is adds a unique name… well, the identifier, identity of a span definition onto a span. It's similar to instrument name or event name. The event name is the closest analogy because it's optional.
This allows us to do things, like, with our life checks, because we can match the span, to its definition. We cannot do it today.
And, there is more. Users can query response by type.
the… I think Tigran and Michele and maybe David, sorry, not David, Dylan, talked about maybe Spanish having multiple identities, like, for example, the… HTTP and database.
So I've added a section on this. I want to push back, for several reasons. The first one is that I think the key definition of the span is its scope. Like, what duration does it measure?
if it's a duration of an HTTP call, you would put one SLI on it.
If it's the duration of your operation after all tries, or error rate after all tries, it's a completely different metric and a completely different number. They can differ in order of magnitude, like if you talk about P95 or something.
Two orders of magnitude, so we should not mix these two.
there are maybe some legit cases where we could consider, because the scope is the same, and if this is mostly on the server, for example, the FAS, the Lambdas.
The HTTP trigger and, like, HTTP request and, fast trigger are… have the same scope. But still, it's a very minor case, and besides the scope and bag of attributes.
Spans are… Different in their name and status codes, and… Moreover, when we see in practice how, let's say, our repo for AWS Lambda, how they describe the span, well, it's not formal, but more importantly, they say.
they give special meanings to, HTTP attributes, they don't populate them, as HTTP semantic conventions say, and they are de facto different. So, it's… Having the multiple identity for spans would be so different from everything we have otherwise.
It's only useful in some H cases, and not having them doesn't break anything. So in OpenTelemetry, if we define semantic conventions, we would have one identity. It doesn't cost you much to have one identity for spend.
For people who don't care about single identity, they either don't populate spend type at all, like, for logs, they would not populate event name if they have more than one identity, or they… create a mixed identity. Worst case, I don't know, you can string concatenate them if you absolutely want it.
Having multiple identities, Creates a lot of questions, like.
what you do as metrics? For fast, we define, like, for spends, we usually define corresponding metric.
When you report makes the identity for fuss.
Trigger.
do you report the metrics? Do you report a new metric with mixed identities? Like, there are so many, weird cases it introduces, and it only saves someone a few, Keystrokes to properly define the span where metric and say what they want it to be with all the attributes.
So I think this is, not a great feature, and I don't think we should support it.
**Reiley Yang (Microsoft Corporation)** 58:34 Okay, any comments, feedback?
**Liudmila Molkova** 58:44 Cool, so it's open for review, I appreciate your feedback, and… yeah.
Thank you.
**Reiley Yang (Microsoft Corporation)** 58:54 Okay, thanks, Limil.
Yeah, folks, please help to review. We have 3 minutes left, I guess we probably don't have enough time to come back to the… the schema URL and the behavior topic. So, I highly encourage everyone who, actively discussed about this during this meeting to, like, dump yourself as a form of a comment in the PR.
So please do that, and we can give 3 minutes back to everyone.
Okay, thanks, Laura. We'll see you next week.
Bye.
