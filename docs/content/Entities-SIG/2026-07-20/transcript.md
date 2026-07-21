SIG: Entities SIG
Date: 2026-07-20
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 05:18 How are we all doing?
**Daniel Dyla (Dynatrace)** 05:23 Good, how you doing?
**Josh Suereth** 05:27 You know, just trying to keep up with the pace of change these days, right?
Alright. Thanks.
**Daniel Dyla (Dynatrace)** 05:44 Is that my PR, the one that's on the agenda there?
**Josh Suereth** 05:47 No, this is… this is my PR.
**Daniel Dyla (Dynatrace)** 05:50 Right.
**Josh Suereth** 05:51 Yeah, which I would love if you took a look at. And then I need to add a bunch of the work that Jack Berg has been doing on our behalf.
Why don't we jump into it quick?
Okay, so this is a minimal entity SDK specification. It, oh, hey, we have… we have 3 approved… so we can actually merge it. For context, Daniel, this is… this is, like, the minimum from the Java… prototype, to get the Java prototype through. There was only one decision made here.
That changes anything. So basically, we call out the merge behavior as experimental, and it uses merging resources from the data model.
which I think is totally uncontentious. And then it adds a retrieve Entities method to match the retrieveResources method on resource. I don't know if you have that in JavaScript, or if you care.
I listed here, I don't know if it's a must-have, or a nice-to-have, or whatever. It's in the Java prototype, so that's why I listed it. The decision here was to call these things unassociated attributes, to differentiate from retrieve attributes, which gives you all of them.
In Java, you know, there was a, why are these raw? What the hell does raw mean?
So… when we talked about it, we just decided Own Unsociated was a better name to make it less… they're both semi-ambiguous, but at least it's more clear that, like, hey, these aren't associated with an entity. And since we always said I'm not associated with an entity, and we called them raw, that's what we're calling them here.
So you know which attributes are loose and, like, legacy versus which ones are in the entity.
**Daniel Dyla (Dynatrace)** 07:38 Yep I have a quick question about this, I guess? Like, the retrieving entities and attributes.
I… A long time ago, I had the same question about resource, so I guess I'll raise it now. It was probably addressed then.
Why do we specifically define retrieval for these and not, like, anything else?
like, there is no retrieval for span attributes, for example. I assume this is for the export pipeline, but…
**Josh Suereth** 08:09 This is the SDK specification, which I think the SDK actually does. Let me check. Let's take a quick gander, because it's a good question.
**Daniel Dyla (Dynatrace)** 08:20 The reason I'm asking is because way back in the day with Resource, we had a bunch of people asking us to add, like.
Back in the early, early days, people asking us to add ways to, like, read resource in the API and things like that, and this was always the part of the spec they pointed to, and it's SDK spec, not API spec, I get that, but it always just struck me as confusing, like, why do we define this, like, operation.
**Josh Suereth** 08:49 I think it's the same reason readable span exists.
**Daniel Dyla (Dynatrace)** 08:54 Yeah.
**Josh Suereth** 08:55 SDK Span. It's basically, like, if you don't define it, how does a exporter get access to it? And I think that's why it's defined, you know.
That's why it was defined first, that's why it's defined here. If you want me to update the… the… you know.
We don't have an API to fall back on to say all the information added in the API should be readable by the SDK, because I would have written that, it's just there is no API for right yet, right?
**Daniel Dyla (Dynatrace)** 09:21 Yeah, it's just always struck me as kind of weird, like, a bit, you know, it's a specification, so I guess maybe it's intentional, but it's, like, a bit… tautological, I guess? Like, if you… if the exporter can't read something, then why are you adding it in the first place? Like, it's weird that we have to specify it at all, but it doesn't bother me that much.
**Josh Suereth** 09:45 specifications are, yeah. One thing I haven't had a chance to throw tokens at is, like.
hey, AI, go take this specification and implement an SDK and see how terrible it is. Just as a, like, as an estimate of how good our SDK is at being interpretable by something dumb, you know what I mean?
**Daniel Dyla (Dynatrace)** 10:03 Yeah.
**Josh Suereth** 10:07 Anyway…
**Daniel Dyla (Dynatrace)** 10:08 In any case, I didn't mean to derail this, it's just a…
**Josh Suereth** 10:11 No, it's a good question. I mean.
**Daniel Dyla (Dynatrace)** 10:13 It always strikes me.
**Josh Suereth** 10:15 Yeah, that's pretty much all that's there, is basically we say this is experimental since 1.60, which is the next release of the spec, that you would… oh, yeah, sorry, I forgot to mention, you can add entities Take them in as their own parameter when you define a resource.
And then it links to the data model spec, and it marks this as experimental. The merge is marked as experimental, and links to the thing that we already had, and then, Why is that highlighted like that? Stop that.
Okay, whatever.
Then, for retrieve Entities, we have this, retrieve and retrieve associated. Those are kind of, like, the main set of changes.
So… I don't think this conflicts with what you have, because yours is more about async and that sort of thing, so I think they should be able to.
**Daniel Dyla (Dynatrace)** 11:09 No, it definitely doesn't.
**Josh Suereth** 11:11 Together, yeah.
I would like to get this through, because, once this is in, I think we can merge the Java prototype, and then make some progress there.
So, if you wouldn't mind taking a look, this has been open long enough, and I think I can click the merge button.
once I update it, if folks here have a chance to take a look, I think by end of day would be ideal, because I think tomorrow morning I'll probably merge this prior to the spec meeting for some of the further discussions. Oh, hey, cool.
I'll still be the…
**Daniel Dyla (Dynatrace)** 11:42 now, I mean, it's only, like, a 20-line change, it's not… oh, 30. It's not like it's… Seems fine.
**Josh Suereth** 11:49 I was really happy at how small I could make it to allow the prototypes to work, by the way, because we have all the hard work in the data model side.
Okay.
Related, I'm gonna just link to it here.
Author… Bird. Is that… is it Jack Berg 6?
No, it's Jack Burke, okay. Okay. So this one, it's good Dmitri's here. This is a PR from Jack.
based on, OTL Entities and SDK environment variables and things that we found in, as he was reviewing the OpenTelemetry Java. So what this does… Right now, is it removes… It changes a few things. So, it removed OTEL SDK, or OTEL Entities from the SDK configuration part of the spec, because that was confusing track… er, confusing Jack.
About, like, hey, we're not making configuration changes, why are you adding configuration environment variables?
we have a policy about not doing that. So I showed him the end propagation thing, and he's like, okay, cool.
It's fine that you have end propagation, but let's remove it, and let's make one caveat around enabling experimental entity support. So, what we have in the Java prototype, and what Jack is working on.
is we add an experimental-enabled thing, where if you flip this, suddenly entities all work in the SDK. If it's false, you get existing behavior, right?
That's… that's the configuration parameter that we have. So that's what this thing is all about. And I think because it's a table, this is just all reformatting because one of the widths changed.
Markdown tables are wonderful for that, right? Like, I need diffs because of whitespace.
**Dmitrii Anoshin** 13:46 It seems like the hotel entity got removed, is that… am I reading that correctly?
**Josh Suereth** 13:52 It got removed as a configuration parameter, yes.
It's not… it's not a configuration parameter, it is an environment variable propagation format.
For which, when you, there's a resource detector which reads it.
**Daniel Dyla (Dynatrace)** 14:08 It's not configuring anything.
**Josh Suereth** 14:11 Yeah, it doesn't configure anything. You have to have a configured N-variable resource detector for it to work.
**Dmitrii Anoshin** 14:18 Oh.
But how to pass the actual entities in this, con… yeah, yeah, like, format?
That we defined, which is not…
**Josh Suereth** 14:31 You still, you still use, you still use OTEL Entities, right? Okay. How do… how do you turn on resource detectors?
**Dmitrii Anoshin** 14:39 I mean, yeah, I know how to turn on resource detectors, it's n-detector, right? But, that environment over… that value is still under Attel Entities.
Is that correct?
**Josh Suereth** 14:52 No. No, hotel… so if you specify a resource detector for ENV, then it will look up OTEL Entities, yeah, yeah, yeah, if that's what you're saying.
**Dmitrii Anoshin** 15:03 But, yeah, but why is that removed in that case?
**Josh Suereth** 15:06 It's not… that's not the configuration parameter. OTEL Entities is the… environment variable that's used to propagate entities, it's not the configuration used.
**Dmitrii Anoshin** 15:15 Oh, I see.
**Josh Suereth** 15:16 I guess the way to do it.
**Dmitrii Anoshin** 15:17 Okay.
**Josh Suereth** 15:18 The configuration used to tell the SDK to do it is this, hotel entity experiment enabled thing, which will turn that on, right?
**Dmitrii Anoshin** 15:26 Okay, and that… this flag will also enable adding entity by the other detectors as well, out of the box, is that correct?
**Josh Suereth** 15:36 Yeah, so this should enable it for all detectors, is basically what it's saying. Resource detectors should produce resources with entities.
**Dmitrii Anoshin** 15:43 Yeah.
**Josh Suereth** 15:44 That's what this is saying.
**Dmitrii Anoshin** 15:45 That makes sense.
**Josh Suereth** 15:46 I took a first review and made a few comments here, and would love to get other folks to take a look and see, like, if you have concerns about this, Dmitrii, like, please ask questions.
**Dmitrii Anoshin** 15:55 No, sir, just clarification, for example, in the changelog, saying that it's, like, it's not like we are removing the environmental variable completely, it's just now it's behind this flag, and then…
**Josh Suereth** 16:07 just removing it from this spec. The specification that defines it, how to parse it, all that stuff is still there. And the Java implementation of the parser is actually about to be merged once we merge that first PR. So, like, we'll have the ability to read it. The other thing I want to call out.
related to this that Jack did, oh, I'm in the wrong. Here, let me come here. Is it open telemetry configuration? I think it is, right?
Okay. There's a pull request here around entity.
Right. So this is actually adding… so, along with the hotel experiments enabled, this adds a, Entities Enabled property to resource detection.
in… in configuration, so there'd be an Entities Enabled, which there… there's a question here of whether it should default to true or not, because we normally default everything to true. This is the first one that's defaulted to defaults, but this would just configure whether or not you get entities and resources, and then all the existing… I have another PR for this as well, for the spec, but all the existing resource detectors just kind of silently get upgraded to produce entities in a non-breaking way, and you have a flag flip that works both with an environment variable or with config.
**Dmitrii Anoshin** 17:33 Makes sense.
**Josh Suereth** 17:34 Okay.
This one I haven't had a chance to do a review on, but I, like, I think this is… no, maybe I did already approve this. Hold on.
Yeah, I did. Let me put a link in our notes so that you guys can take a look. It'd be good to have the Entity SIG, you know, mark this as something we approve.
So configuration… configuration spec.
And we had, they're both.
Jingles.
Let me put the other one here, too.
Let's do the query config… the month.
Okay, so we have a lot of good movement here, I think, on some of these.
So, I'm hoping that we can get more of the SDK prototypes in then.
Let's take a quick gander here on all the other SDK-related ones.
I don't think any of these are stale. Let's see… Let's see… So we have, Preserve job instance when translating Prometheus to OTLP. That is still draft. David's on vacation, I'll check with him later. The SDK startup specification from Daniel, I believe… Does this one… Did you get a chance to account for any of the discussions here, Daniel?
**Daniel Dyla (Dynatrace)** 19:05 I think so, yeah, I think this is all up to date.
**Josh Suereth** 19:08 Alright, because I think I can probably approve this right now, then. This just adds… Hmm.
That's the difference between current and other future. Entity descriptions take precedence.
resource, and then this is NTescribes, NC has type host… detecting NC information from the environment.
Alright, so the only thing here is… I think we're planning to actually… Still call them resource detectors.
**Daniel Dyla (Dynatrace)** 19:42 Okay.
**Josh Suereth** 19:52 That was one of the things we were talking about with the Java SIG, about how it's going to be easier for us just to reuse a resource detector. So basically, what we would do instead was, in here, it talks about a resource detector package, where it has to live, how it runs, all that kind of stuff.
Was actually just add a development thing that says if… so what we would change here is just say, you know, if, that hotel experimental Flag is there, resource detector should, and then everything you specified.
Instead of having two separate… interfaces.
**Daniel Dyla (Dynatrace)** 20:32 Yeah, okay.
What do you think? Yeah, I can update this.
**Josh Suereth** 20:37 Okay.
Cool, because then I think… I think what you have here is what we need, it's just we… thought we could get away with doing things a little bit better. And then resource provider is still something we want to… have, and have that in development. Okay.
Cool. Do you need me to make a comment on that? Because I might do that after this meeting.
If you need it.
**Daniel Dyla (Dynatrace)** 21:01 Sure, yeah, it's probably helpful, because I probably won't get to it until later, just to make sure I don't forget what's going on.
**Josh Suereth** 21:08 Okay.
**krajo (Grafana)** 21:09 Sir, just one question. I… my eye code something in this which said that the descriptive attributes can be detected asynchronously.
**Daniel Dyla (Dynatrace)** 21:22 They can be, yes.
**krajo (Grafana)** 21:24 But, still, they would be… you know, present when you send the OTLP message, right? So it's not like…
**Daniel Dyla (Dynatrace)** 21:32 Yeah.
Okay. The… the export pipeline essentially needs to await them before actually exporting. The biggest problem with it is the, the spam processors. So, your spam processor may not have access to it on first process.
**krajo (Grafana)** 21:56 Okay, thank you.
**Josh Suereth** 22:05 Alright, so then this is the last, spec PR that I think converges with all of them.
I think there's maybe a few changes I have to make. What this one did was just… Talk about the resource detector aspect.
of, So, it just updates the language, so instead of attributes, it says attributes and Entities, and then talks about, you know, an OS thing populates OS Entity with the OS star attributes, instead of saying OS populates OS star, and then this updates to actually say.
what entities each thing is meant to provide. Now, if I recall correctly, this part… of the… yeah, it's still in development, the resource detector name part of the specification. So this is, like, not… Not the same area you were touching, Daniel, it's like the section underneath it.
So, what I'm doing is just expanding the… since this is still in development for config, these are the named resource detectors config relies on that I don't think have rolled out to all the languages yet. This is just saying, hey, since it's still in development, we're gonna hijack it and say it has to produce entities. We can do that in a non-breaking way.
We need to make sure that the entities it produces produce the same set of attributes That were previously produced, so we don't break anyone.
And, yeah, so that just describes what they are.
So, like, service will populate service and service instance entities, Should probably do service namespace, too, I should probably update that.
And then, what was this concern? You might play… Pulling the line and leading the users. Okay, this is another one for… based on some of Dmitrii's concerns, but, The end… this adds the end… Detector.
And the current Java PR adds the end detector as described by this PR, which is the end detector never looks at hotel resource attributes, it only looks at hotel entities.
Always.
**krajo (Grafana)** 24:27 sorry, a question. Does that mean that it doesn't validate that an entity points to an existing attribute?
**Josh Suereth** 24:37 No, no, when you specify OTEL Entities on the command line, you're specifying both the entity name and the attribute key-value pairs to add at the same time. So you add them as a button. Yeah, yeah.
**krajo (Grafana)** 24:49 Okay, thanks.
**Dmitrii Anoshin** 24:54 I was saying that if this one is enabled, the hotel underscore resource attributes just ignore it.
**Josh Suereth** 25:01 That's still TBD. The… when all of these specs land… when all the spec changes land.
Daniels, mine, and Jack's.
We still have, basically, an ambiguity in the spec over… this interacts with Oh, tell resource attributes.
that OTEL Entities flag means that we'll use the end thing, but we don't actually specify what happens to OTEL resource attributes at all.
in any of the PRs, I think, unless yours has it, Daniel, which I don't remember, because it's been too long.
You're muted.
**Daniel Dyla (Dynatrace)** 25:41 Unless mine has what?
**Josh Suereth** 25:43 Unless yours has spec for how to interact between hotel entities and hotel resource attributes.
**Daniel Dyla (Dynatrace)** 25:49 It does not.
**Josh Suereth** 25:50 It doesn't, okay.
So, so I think we probably need to do a follow-up specifically for that point.
Dmitrii.
Yeah, given these are all in, development portions of the spec, what I'd like to do is try to push for these to get merged, hopefully with this week, if possible, where we can get approval on all them, Daniel's, mine, Jack's, and get things through. And then.
I want to do an evaluation once they all land of, like, okay, where are the holes? That's a hole I know of that I think we have to cover.
Does that sound good? Or would you rather see changes to the PRs before they merge?
**Dmitrii Anoshin** 26:43 Sounds reasonable.
**Josh Suereth** 26:45 Okay.
Alright, I think that was all for this one, is just… Pretty much, it just describes env, and then it updates the… named resources for what entities they produce. Okay, and I think that was it for… spec PRs that are pending. Come on.
Yeah, that's that one.
So we have Jax, we have these two for me and Daniel's. Okay.
Cool.
That was mostly what I wanted to get through. So, again, the minimal spec, I think I'm gonna merge tomorrow morning, if no one has any things. Resource detection being entity aware, if we could get… how many more do we need for this? And then Daniels.
We have no approvals on this one, so if we could get Shulks to review this, that'd be good. Let me know if you have any concerns.
On the, the first resource detection one. This one here, Daniel, if you… I'll make my comment, and then as soon… like, ping me and CNCF Slack whenever you make an update, if you can, so I don't miss it.
Cause we'll see if we can push this one through as well this week.
I think this one's been hanging for a while, yeah.
Okay.
Cool.
**Dmitrii Anoshin** 28:13 Sorry, one more question about this hotel entities environmental variable. We enabled that through the YAML config explicitly, but we… looks like we still don't have a YAML way to define those entities at the same time.
Should it be a configuration option under environment detector?
kind of detector, so instead of using environmental variable, you just actually specify entities in YAML.
**Josh Suereth** 28:43 I think we can actually… Do that without… needing it to be the end resource detector, yeah, like, just specify the entity straight in YAML?
**Dmitrii Anoshin** 28:52 Yeah, because it seems like we're going from YAML back to environmental variables, and then back to environmental…
**Josh Suereth** 29:00 The environment variable is not meant to be configuration. The environment variables, so, like, if I go to, like, GCP and say, hey, can you provide OTEL resource attributes in the environment before you spin up Cloud Run?
Here's the spec.
they can go do that. And then OpenTelemetry just gets the, like, Cloud Run IDs and all that kind of stuff by default, right? That's what the end variable's for. From a configuration standpoint, if I want to add a bunch of crap, yeah, I think we should have that in the file system as well.
Right? Like, the end variables are, what do you call it? Emergency escape hatch, if you will, or, like, a platform-provided thing, you know? Yeah. Maybe we could talk to Kubernetes and have them provide all the CAITS attributes in the environment by default, or we can have the operator do that?
Which it does today with hotel resource attributes, but…
**Dmitrii Anoshin** 29:57 Yep.
**Josh Suereth** 29:58 Yeah.
**Dmitrii Anoshin** 29:59 Yeah, but, like, custom environmental variables, for example, those are not gonna be part of a specification. Currently, the only way is to specify them in the As hotel Entities Environmental Variable, But we should have a configuration interface in YAML to specify them instead, right?
**Josh Suereth** 30:21 Yeah, yeah, yeah, that's, if we look at… Let's just be very explicit.
I'm gonna open it up now.
So if we look at… Is this easiest to read if I go to schema or Docs? I forget.
Give a schema.
Nope.
That one's… Where's the human-readable thing? Human-friendly… It's rendered here.
Okay, so if we look at resource… Those are the experimental resource detectors.
Resource detection. Okay, so in resource detection, you get an array of detectors, of which one would be ENV, If you're gonna use hotel entities, but this, like, array, this attributes thing.
I think we can… it's an include-exclude of, like, what attributes to pool and which ones to ignore. I think we could literally have an Entities here, and, like, have whatever configuration we want. So you could directly, in the config file, say, this thing is entity X, or this thing pulls from this And variable, because if I remember right, you… in the file-based config, you can have, like, placeholders that pull from the environment, is that right?
**Dmitrii Anoshin** 31:43 Yeah.
**Josh Suereth** 31:44 Yeah.
So yeah, I think that's a task, Okay. That we can have to just add it, and here's where I think it goes.
**Dmitrii Anoshin** 31:52 So, essentially, it's gonna be a replacement, entity-aware replacement for attributes section.
**Josh Suereth** 31:58 Yep. Okay. And we can have a thing where we could make… I don't know if you can have constraints where we'd say, like, you either have attributes or entities, maybe we allow both, but I'd prefer if you pick one, you know? Yeah. That kind of thing.
Yeah.
Okay.
Cool.
Alright.
Related to that, what did I want to do? Open showometry… we'll go back one.
If you guys don't mind, I was going to do, a projects… Clean up here.
for entities.
So we can actually get things on track and figure out what we need for Phase 1.
I think we're rapidly closing on a point where we have a prototype people can try and use. We have a set of hard-locking issues we need to talk through for host ID, but I know that you guys are working that in Systemconf. I think, Dmitrii, you have that interesting, proto-proposal.
around scope I want to walk through, but what I want to do is, is, figure out when we feel like Phase 1 can be, kind of, put into… People's hands to play with and toy with, and get feedback on them actually trying out entities and using them in anger.
like, as quickly as we can. So, that's my current goal. So if we go… if everyone's agreeable, can we actually go through the project list and say, like, move things out of in-progress into, like, not needed, or, like, later stages, and kind of figure out what we have to do, to get there? Sound good?
**Dmitrii Anoshin** 33:45 Sounds good.
**Josh Suereth** 33:46 Okay. Dmitriri, we were just talking about this, so I'm going to type it in now. Add Entities to resource.
detection.
portion of open telemetry.
Config. Iteration.
spec.
Alright, I'm gonna create that as a draft, because I think we opened that in the OTelconfig rep repo?
Which I don't… no, I probably have access to, but… yeah.
Okay, let's go through in progress. Generate entity configuration interface for metric scrapers. That's collector-based things, right?
Do you think… is this… this is still needed for our initial, hey, people, try this out?
**Dmitrii Anoshin** 34:34 No, I didn't think so.
**Josh Suereth** 34:35 No? Okay.
Can I move this into… Should I move it into Phase 1, or should I move it somewhere else?
**Dmitrii Anoshin** 34:45 We don't have a probably good column here for that, I guess. No status, maybe?
**Josh Suereth** 34:50 I'll move it to no status for now, and we can… we'll re-triage these then.
Okay, add support for new resource entity references proto-message. I think…
**Dmitrii Anoshin** 35:00 Yeah, this one is about scope.
Oh, oh, sorry, it's support for new Entities. Yeah, it's, actually, like, overarching issue for the collector work in general.
**Josh Suereth** 35:12 Yep.
**Dmitrii Anoshin** 35:14 What… is that needed for them to try? You don't have to have a collector to try, right? You can just… you can use SDKs only.
But…
**Josh Suereth** 35:23 I like that we have both, though, and I think you're landing this pretty well.
**Dmitrii Anoshin** 35:29 The thing is…
**Josh Suereth** 35:30 help with… go ahead.
**Dmitrii Anoshin** 35:32 The thing is, Collector already emits Entities with the Kubernetes cluster receiver, so… It's like, it's half… Done, I would say.
**Josh Suereth** 35:44 Okay. I'm gonna leave it in to-do, and what we might… maybe what we do is we, figure out what scope we want. Like, if there's anything you feel like we need in the collector for a preview, we'll, update the bug. Otherwise, we can move it into untriaged and, close out the work that you did do. I mean, you did a crap ton of work here, man. Like, all this stuff?
All the purples, yeah.
**Dmitrii Anoshin** 36:09 All right.
**Josh Suereth** 36:11 Resource entity merge logic prevents fine-grained detectors. This is basically how are we gonna work for Go? Interesting story, David Ashpole has a prototype entity supportive Go SDK.
So, I am gonna leave this… well, actually, what I might do is move this over into, no status, and then I can follow up with David on that Go prototype, and see if we can push on that, because it might be we actually don't have to solve this if we take the approach David took.
But, he's on vacation this week, so I didn't have a chance to ask him before the meeting.
Any concerns with that?
Cool. Alright.
Let's the case.
**krajo (Grafana)** 36:59 Sorry.
**Josh Suereth** 36:59 Good.
**krajo (Grafana)** 37:00 So, just one question. So, I'm actually working with David on a bunch of stuff, but I didn't know about this one. So, potentially, I could just point his SDK prototype against, like, from a two sort of endpoint, and I would receive entities, right?
**Josh Suereth** 37:15 Yep.
**krajo (Grafana)** 37:16 Awesome. Okay, thanks.
**Josh Suereth** 37:18 Yeah, one of the issues we looked at has a link from David with a link to his prototype.
Like, he has a comment on one of the PRs we're reviewing for the spec today, I don't remember if it was Daniel's, if it was mine, if it's Jack's, one of them, he commented with the Go prototype.
I forget which one, though, but… Oh, it's not that proven.
**krajo (Grafana)** 37:38 Okay, it's not that urgent. I just want to, you know, visualize in my head, like, how we would do that left-hand navigation that we keep talking about, because it sounds like a nice thing, but then how you actually do it and what you actually show is… Is what I'm trying to figure out, but okay.
**Josh Suereth** 37:52 And when you get real data, it's gonna be way easier for us to figure this out, yeah.
**krajo (Grafana)** 37:57 Yeah, yeah, exactly.
**Josh Suereth** 37:58 Okay, so Daniel, you're on the startup thing as well. Strategy for asynchronous Resources Entities, I think these are both the same PR, so that's beautiful. Add local versus… so you're still working on this, Dmitrii, the local ID and universal ID details to the entity model.
**Dmitrii Anoshin** 38:16 Not actively, unfortunately, I just don't have time, but I guess it's, yeah, it's on my plate. But, do we… Need that?
for…
**Josh Suereth** 38:26 I think… I think I'm gonna move this to Entity as signal, if that's okay, because I think that's where, when we hit Phase 2, I think we really need to nail it. I do expect us to solve that issue… prior to really getting into Phase 2, I think it, like, what you're working on there, what you're hinting at is super critical. Just, I don't think it's needed for us to call, hey, we have a demo, we want people to try it out.
**Dmitrii Anoshin** 38:50 Great.
**Josh Suereth** 38:50 or not a demo, we have prototypes, we have our first experimental implementation, you can opt in, here's how to use it, here's what they are. Yeah. I don't think we need it for that, but I do expect that as people try it, we'll get more feedback on this.
Okay, show demo of how collector processors differentiate remote versus local.
**Dmitrii Anoshin** 39:13 similar. It's kind of more associated with the collector, essentially.
**Josh Suereth** 39:19 I'm gonna leave this, because I actually think if we were to go to the spec SIG and say, hey, we have working prototypes of entities, what I would do is I would, have a collector running on a different IP address, send you a bunch of host metrics.
Or find a way to have an entity ID that's different, and then show the collector not adding a bunch of attributes it shouldn't, because the entity merge logic.
So, I still view this task as, like, our, one of the demos we're gonna have when we're ready for people to try it out. Like, we can show, like.
the entity model in practice, you know what I mean?
**Dmitrii Anoshin** 39:58 Huh.
Interesting. I see. Based on the… based on the data that collector is seeing, it should have a different… association.
**Josh Suereth** 40:12 If the SDK is sending you an entity ID, and the collector would detect a different entity ID, then the attributes don't get merged, right? So, like, if I'm sending from host 1 to host 2, we can have it so the SDK gets the host ID and sends it to you, and then your host ID is different, and so you know not to shove, like, all that same on when the SDK didn't do it.
**Dmitrii Anoshin** 40:35 Makes sense, makes sense. Oh, that's a good one.
**Josh Suereth** 40:38 So, I'm gonna update this… we're gonna update the name.
To be… show demo of… Different mode versus local, Actually, I don't have to change the name.
Okay, yeah, discard that. We'll do… This collector icon… the goal of… Sorry, my cat disconnected me. Am I back?
Okay.
goal of this is to, have a… Work demo, you can use to highlight.
That's another problem, this… And she songs with this.
Firsts.
Boston.
preview with SDK and Electric work.
Okay.
We will find scope.
Based on that demo. Alright.
Cool.
So then… I think we go back to… that's… that was all the in-progress stuff. We need to communicate a breaking change in the specification around resource allowing non-mutable attributes, which we can do once we are ready to start talking about entities and this thing people can try. I think that goes into the communication, I'm leaving that in.
Finish SDK specification so we can, bean? I think it's supposed to be begin implementing Entities and SDKs against beta or experimental spec.
Our prototypes are already kind of there.
So, I might actually mark this one as… I mean, this is about finishing, but I think… We're kinda done.
What's this saying?
Oh, do we need… do we need an API for resource detectors so you can do them without an… SDK.
That's an open question.
Did you catch the question on here?
I don't know, Daniel, if you're still there, do you think we need an API for resource detection instead of an SDK-only thing?
**Daniel Dyla (Dynatrace)** 43:15 I think the… Probably… Yes, I, I… I don't remember why. I remember we talked about this, and we talked about having an API for entities.
But I don't remember… why? What did it solve? Maybe no. I… I can't remember why we… why we were talking about doing it.
**Josh Suereth** 43:45 There's a few things it can solve. I think I'm gonna… If we want to reduce scope, I think we don't do that now. But the API would be… I want the ability to make a resource detector that doesn't depend on the SDK.
So my resource detector just detects entities, right?
Why is it depend… an SDK is stable for one year.
an API stable for 3 plus years, you know?
**Daniel Dyla (Dynatrace)** 44:12 Oh, yeah, okay.
**Josh Suereth** 44:13 Yeah, so it's…
**Daniel Dyla (Dynatrace)** 44:14 Yeah, it was because we were gonna have something more akin to instrumentations producing entities.
Yeah, I remember.
**Josh Suereth** 44:23 detector, like, even in Java, the resource detectors it uses are defined in Java instrumentation, for the most part. So, like.
Treating resource detection as a form of instrumentation makes sense.
I think we're gonna… that might be a phase 1.5 or something, you know?
Alright, I'm gonna leave it here, and… and we'll re-triiage, because I still think it's an important question for us to answer. But let's… let's finish up.
Information from Dash on how we solve some merging with entity-like system. This was, Yeah, McKelly added this and had rules about how to… basically come up with unique identities for resources in lieu of entities, and we need to, like, look through this and see, what makes sense for us, but this is basically around how to pick, a unique ID.
And I think, if I remember right… We know it cannot be the same process unless the same Excel SDK. Yeah, this is… you might want to read this, Dmitrii. You know how you were talking about how entity keys have, like, a context relationship, where, like, you know, this ID is a subset of this one, which is a subset of this one, and you take all three to make a universally unique identifier?
**Dmitrii Anoshin** 45:52 Yeah, but it's just one additional… how I was proposing that is just additional, scope, like.
**Josh Suereth** 46:00 field, yeah.
**Dmitrii Anoshin** 46:01 Another entity, essentially.
**Josh Suereth** 46:03 These are the rules that Dasho uses to do that same work on resources today.
**Dmitrii Anoshin** 46:09 Okay.
**Josh Suereth** 46:09 So, like, what they're saying here is basically, Kate's container would be the scope for process, is what this is saying, right?
**Dmitrii Anoshin** 46:20 That makes sense, exactly, yes.
**Josh Suereth** 46:23 Yeah.
So, I think that's kind of… I don't know if this helps you at all or not. I'm gonna leave it here, since you're still… actually, no, I should move it with that. I'm gonna move it over to right next to where you have your local ID thing.
Okay.
Since they're related. Okay.
Alright, resolve resource configuration with Entity Data Model.
Oh, this is the issue. I did open an issue in the configuration spec. This is the one that we need. It's still assigned to me.
Dmitrii, you said you wanted to update the SDK config spec, right? To have, You know, detection slash entity or something.
I opened this up in June of last… oh, no, just a month ago.
to do that work, and I totally forgot I did.
Okay, cool.
So that's the issue. Do you want me to assign this to you? Are you able to pick it up?
**Dmitrii Anoshin** 47:23 I'm… I don't have any time these days, unfortunately, well, we… I cannot work on anything.
I'm sorry.
**Josh Suereth** 47:32 That's okay. I'll leave it assigned to me, but we'll… we'll… I'm gonna remove this, because I think then… Come on. We'll archive.
Is this the body of work where we think we can go and say, hey.
Once we finish this, we think people should start previewing.
**Dmitrii Anoshin** 47:57 It seems to be roughly the body, but potentially we might add something else on top, I would guess.
**Josh Suereth** 48:04 I'm fine adding stuff, I do think we want to be careful about scope, like, that's why I wanted to go through and remove things. But, For the most part, outside of, like, little tidbits around releasing, is there any, like, feature work that we need to land before we think we're ready to do a preview?
**Dmitrii Anoshin** 48:23 Oh, sounds good.
**Josh Suereth** 48:25 Cool.
Alright, I'm gonna have to… we were supposed to… apparently we were gonna have release in November 24th of 2025, if you remember. I'm gonna update that, since it's July of 2026. Maybe we'll go for November, I don't know, but, I'd like to… Keep pushing on this every week, and get to the point where we have that preview, and we can do an announcement, and maybe write a blog.
How's that sound?
**Dmitrii Anoshin** 48:55 Sounds good.
**Daniel Dyla (Dynatrace)** 48:56 Seems good to me.
**Josh Suereth** 48:58 Alright, thanks everybody. I think we're gonna call it here, unless anyone has, any topics that weren't added.
**Dmitrii Anoshin** 49:06 Thank you.
**Josh Suereth** 49:08 Okay. Alright, we'll see ya.
**krajo (Grafana)** 49:11 Yep.
