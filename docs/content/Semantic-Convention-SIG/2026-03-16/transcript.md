SIG: Semantic Convention SIG
Date: 2026-03-16
Duration: 49 minutes
Zoom Recording URL: https://zoom.us/rec/share/jTrHVQkzrSe0KH12DcgQhGtSUL2avXjQEOgHRquIUN9x8WUBsGHLGK0e5gcyTwef.MQGR58qe_WnHuZuE
============================================================

## Zoom Recording Transcript

**Josh Suereth** 02:39 Hey, everybody.
**Trask Stalnaker** 02:43 Hi, ya.
**Josh Suereth** 03:05 Trask, do you know whose turn it is to run everything?
**Trask Stalnaker** 03:11 No, but I haven't run it in a… Few weeks, so… I can volunteer.
**Josh Suereth** 03:18 Sure, I'll run… I'll run the one during KubeCon, then. If we have one.
We might want to think about canceling that one.
**Trask Stalnaker** 03:26 Yeah, I think we usually cancel the KubeCon week.
**Josh Suereth** 03:31 Okay.
**Michele Mancioppi** 03:34 Are you folks going to be at KubeCon?
**Josh Suereth** 03:40 I won't be able to make it this year.
**Trask Stalnaker** 03:41 I will not.
**Michele Mancioppi** 03:44 PT.
**Trask Stalnaker** 03:47 Have fun without us, though.
**Michele Mancioppi** 03:50 Oh yeah, it's gonna be great fun.
**Josh Suereth** 03:57 You guys all wearing the tracksuits again?
**Michele Mancioppi** 03:59 Naturally. People get started to wear it, right?
**Josh Suereth** 04:03 Good.
**Michele Mancioppi** 04:05 But this time, I'm daring to do a… did you know the internet show called Hot Ones?
That I'm sure I'm going to regret it.
**Josh Suereth** 04:19 What's, what's the, what's the show about?
**Michele Mancioppi** 04:22 It's, effectively, like, an interview.
I have two guests. One is, Jurassi, and the other is, Severin Neumann.
And, we talk about observability as we eat increasingly spicy sources.
to… Insanity level spiciness.
**Josh Suereth** 04:45 That's pretty fun, yeah.
**Michele Mancioppi** 04:47 Huh?
**Josh Suereth** 04:47 I look forward to hearing that one later.
**Michele Mancioppi** 04:50 I, I hope it's not going to be regrettable.
**Trask Stalnaker** 05:03 Let's see if my camera cooperates today.
Come on… I think… Not… I forgot to reboot. It was failing on me on Friday, too.
Alright, no camera, but I can share. Let's see… Wee… Have no agenda, but that's okay. Let's start with triage.
**Liudmila Molkova** 05:51 Hello. Hi, everyone.
**Trask Stalnaker** 05:53 Hey, hey.
Block… Did we… I don't think we talked about this in… Oh, wait, no, this is blocked on… yes, this is just blocked on the other PR.
That's fine.
Browser URL…
**Liudmila Molkova** 06:36 Oh, I think I blocked it, and there is more details, seems… Somebody dismissed my review, and it's the right thing.
Thing to do.
**Trask Stalnaker** 06:49 Okay, cool.
What, move it back to… waiting code owner approvers.
Alright, let's look at… Some needs more approvals… C-spell… Alright.
I think these are link check failures, maybe.
And maybe unrelated.
Yeah.
**Josh Suereth** 07:28 a massive number of link check failures, and I think partly we're just spamming.
HTTP servers with link checks, like, all the frickin' time.
I think this is across OpenTelemetry, too, like, I see this in the spec, I see this in anyone who does link checks for the… for OpenTelemetry I.O. Would it make sense to propose, like, there be a big global cache?
Of links that's generated, like, weekly.
And then Link Checker is forced to use that cache.
And not ping the internet for everything, like it's trawler.
Over and over and over again.
**Daniel Dyla (Dynatrace)** 08:12 Also, most of these links I'm looking at here, these are all in the repository you're actually checking. They're, like, local links. It may be possible to do these checks locally.
**Trask Stalnaker** 08:30 These are tags, though.
I mean…
**Daniel Dyla (Dynatrace)** 08:35 Well…
**Josh Suereth** 08:36 Yeah.
**Daniel Dyla (Dynatrace)** 08:36 It is, and it isn't. I mean, it's… it goes to the tag, but, like, in the, the document itself, it's just a, Alright.
whatever not an absolute link is, sorry, it's a Monday, a relative link.
**Trask Stalnaker** 09:03 Link check. Failures…
**Liudmila Molkova** 09:09 One good way could be to run full-link check weekly, and I think we already have this job The… but the PR checks could run on the PR changes only. They don't need to check the rest.
**Trask Stalnaker** 09:33 Yeah, we actually did this in the Java repos recently.
Gregor… and Gregor did some… Nice work around integrating into kind of a standard tool.
Mize, niece, M-I-S-E… I could share that.
**Liudmila Molkova** 10:03 Did you like, like, did it bring the good results?
**Trask Stalnaker** 10:08 We… I don't think we saw all the last… because last week, with all the GitHub problems, they, like… the reason why it showed up recently across all the repos is because… They had a lot of, problems, and so they did more serious throttling, temporarily, at least.
Might be permanent, I don't know.
And we didn't see these failures in the Java repos, so I think it's working, but also we don't have as many… we have a lot of links in the instrumentation repo, but we don't have as many as the spec.
repos. I think those are, like, the most massively linked repos.
**Liudmila Molkova** 10:55 Yeah. Thanks, it would be cool to see details.
**Trask Stalnaker** 11:00 Yeah, yeah, I'll ping Gregor, might be something he would be interested in.
proposing.
**Liudmila Molkova** 11:09 Thank you.
**Trask Stalnaker** 11:11 Yeah The caching… I'm trying to remember why we didn't do… caching… Because you can do, with our link checker, it does support caching, and we could even push that cache to GitHub Actions cache.
**Josh Suereth** 11:37 Yeah, I think we're not caching GitHub, like.
github.com, if… but, like, we probably should, and given all the API limits GitHub is putting on itself, like, that would be very helpful.
**Trask Stalnaker** 11:55 Yeah, I'll… I will take a peek at that, because I'm not remembering right now.
Why… We didn't try that before.
Because I know I've… looked at the… the capability… the caching capabilities of the link checker before.
**Liudmila Molkova** 12:23 The one on OpenTelemetry I.O, I don't know how to work with. It, it, it always fails.
**Trask Stalnaker** 12:31 Oh yeah, they do some complicated stuff there.
Yeah, I'd rather not… yes, I'd rather not do that.
Alright, let's see, what else do we got here? Oh yes, so the CISPO, This is for Gen AI crew… Does this have… Code owner, approver, and… Okay, but you're on that, thank you, Lydmilla.
Gen AI crew, Gen AI Crew… Oh yeah, this is a… Simple, simple-ish one. We did get a… Fast stig… approval, it's just not green. So if somebody else who does have a green checkmark could look at that, it's basically the same as these other four. Not super creative.
Oh, and that's probably just a simple… Huh.
Hit merge, alright.
I will.
Wait for that to finish.
Let's see if we've gotten anything on the agenda… Weaver. Release… And, alright, it is… Happening.
**Josh Suereth** 14:28 We got past our, our URL checker. That was literally why it failed.
**Trask Stalnaker** 14:36 Let's see…
**Josh Suereth** 14:40 Yeah, this is an FYI for folks, that the latest Weaver release has a bunch of cool stuff in it.
**Trask Stalnaker** 14:46 It actually has, just a heads up, it actually has not, oh, but it did get queued. Okay, so these are must not be required status checks.
**Liudmila Molkova** 14:57 Yes, link checks are not required.
**Josh Suereth** 15:01 Oh.
**Liudmila Molkova** 15:02 Oh, and those, but they are not required, but maybe they should be, because they… they check pretty much.
**Trask Stalnaker** 15:08 other things.
**Liudmila Molkova** 15:09 Yeah.
**Josh Suereth** 15:11 the make default target docker, the failure was just, like, the tool was not available, so I don't know what the heck that was.
It, like, it didn't have anything to do with Weaver, from what I could tell. Just said, tool not available.
So I asked it to re… rerun them, but… It was blocked from merging. I just put enable merge, like, when it was ready, I thought.
Huh.
**Trask Stalnaker** 15:40 Yeah, it's, they're not… if they're not required status checks.
It will merge… it'll send it… it'll merge it right away, it won't wait for them to finish.
**Josh Suereth** 15:52 Gotcha.
Yeah, so it's trying to run the required ones there.
I have a link to the latest Weaver if you don't mind talking about some of the things that were added.
Yeah. And some breaking changes.
Cool, so this one, There's a bunch of crap here, but let's talk a little bit about LiveCheck. There are a few fixes to LiveCheck to let you use it in a, test containers kind of environment, so there's now a health endpoint that you can use to confirm it's ready before you start sending data.
We have a new feature that, if you set this output HCP, you can have it send its report as a response to a slash stop.
Command, so you can call slash stop.
to end your test and get your report straight up in that HTTP call, which is really nice. Did we… Ludmel, I don't know if you know this, I don't think we actually documented a how-to for using Weaver in test containers yet, did we?
**Liudmila Molkova** 17:02 No, we didn't. So, we… I played with desk containers. Ricardo and Python 6 independently played with, just, POPEN.
And we realized that test containers are just unnecessary complication.
**Josh Suereth** 17:18 Okay, so P open's better.
**Liudmila Molkova** 17:20 Yeah, you don't need to deal with all the volume mapping and everything.
And logs, container logs are awful. Like, you gain nothing by test containers here.
**Josh Suereth** 17:31 Interesting. Okay. Yeah, so, but you can run it as a… run it by itself, run it as a container, whatever. Yeah. Alright, we'll keep going through a few things. So, we actually fixed up the registry subcommand, so if you use JSON, YAML, or JSONL, you should get more consistent output. What was happening before was we were running JSON YAML and JSONL through a, a thing that was intended to render the JSON inside of a web page, so it was like… making the format so it would look good inside of a web page, which means it would do weird escaping things that people didn't want, they just wanted raw JSON. So now that's what you get.
Right, EmitOTLP logs is… you can have live check, emint OTLP logs, that's great. New feature that's kind of amazing, registry infer. You can open an OTLP endpoint, shove a bunch of data on it, and you'll get out the, YAML syntax for what Weaver should have.
This was, they used this to do Prometheus Weaver.
configuration, which is kind of awesome. So, thank you, Arthur, for that.
Couple fixes around that.
Then, the next thing we did, which this is actually semi-breaking, but not breaking, it's just might break output that you had expected, but we're moving from calling something a registry URL or registry name to calling it schema URL.
So going forward, we're gonna be tracking things by schema URL consistently across all of Weaver, instead of this, like, name, this version, and then schema URL, all as separate things, they're all now the same, it's just schema URL. Thank you, Lyudmila.
**Trask Stalnaker** 19:13 And so that, aligns with the schema URL that you would emit in your telemetry. Nice.
**Josh Suereth** 19:19 Exactly, yeah. So now, inside of any registry, you'll know what the schema URL should be emitted in the telemetry, and you can link the two.
This also helps when we federate. We're gonna have more schema URLs available.
Some breaking changes. So, because we fixed the templates, we also changed autoscaping to be off, or default to none.
If you want to turn autoscaping on for HTML and things, the easiest way to do that is to name your Jinja template, like.html.j2, and it will auto-escape for that scenario, but there's also, like, opt-ins that you can set in Weaver YAML to auto-escape.
Autoscaping is that capability where it will take the JSON you want to write and make it pretty for the web, and so if you ever got weird-looking JSON or YAML out of Weaver, that's why, because of the autoscaping feature. It's now just something you have to fully control.
Another breaking change. For version 2 syntax, we're actually trying to consistently use the OTEP from Libila now, so if you haven't looked at the OTEP, about schema URL changes, there will be a file format field that will be consistently used across all of Weaver.
and across schema URLs. So file format defines the type of file and the version of that file.
Definition 2 means this is the V2 of Weaver. If file format doesn't exist, we assume that it is definition V1.
So, from now on, you want to start moving, if you were using the version 2 syntax, to use definition 2 instead of version 2.
Cool. So… Oh, some fixes to JSON schemas, so you can use Weaver to inspect what the JSON schema is and dump it. I actually have my AI agents use this, so they understand how to interact with schemas, and it's really nice.
When you want to, like, go have them do a quick fix, they can actually figure out what's going on.
The other big one, and this is around Federated SEMCOM, is Weaver Registry Package. So now if you want to publish your repository.
This is… this is not a finished thing, this is still, like, a prototype preview feature, but you can use Weaver Registry Package, and it will create a bundle of your data in one file that's easily consumable. This is what we want the new schema URL to be.
is this package, where it's a manifest and a file, and then you can distribute and share this. So that's… that's the big thing. It's currently behind… I don't… is that one actually behind the V2 flag, or it just has the V2 warning, Lugmella?
**Liudmila Molkova** 21:53 It is behind V2 Flag, you cannot use it without V2.
**Josh Suereth** 21:58 Without V2, yeah. So it's still… it's still part of the experimental V2 stuff, which, we… we really want to get out of. I think that this release is actually our MVP for V2. But now that we have packaging, you can package these things, distribute them, and resolve them separately.
And all of that registry thing works. That's actually one of the other things that was done in this release, was you can actually, resolve from registry instead of having to resolve from definition. Now you can package and publish.
Cool, that's, that's a big one, and then adding all the JSON schemas for this. I think we were missing policy finding before. Other important thing, we can now… we had this thing for imports, where you could import, signals from a dependent registry that you had, so if you're depending on semantic conventions, you can import certain things to put in your own.
Registry. Or you could use this flag that said, just import everything.
Well, we were missing attribute groups, and we're missing spans in imports. So those have been added. So now you can use the import feature for everything, you do not have to rely on that flag that says import everything. You can actually fully control what you want.
And then… The V2 syntax now also supports refinements, so we have this notion of, I want to take the semantic convention for HTTP server clients, I want to extend it and make some changes to it, that's a refinement. We now support refinements for everything.
And the refinements work the way you'd expect. You do not have to repeat the name, or sorry, you don't have to repeat the names, you don't have to repeat notes, you don't have to repeat all the things. You only have to actually change the things you're changing.
So that is fully supported now in V2.
And there was some ordering issues with publishing in the past.
That no one ever ran into, because I don't think anyone was publishing, except possibly Michelle. But if you publish the resolve schema.
not the definition schema, the resolve schema. The order of the attributes would constantly shift, because we're using hash maps, and they have an element of RNG into them in Rust. And so, what we do now is, before we export, we actually fully sort The attributes and things, so that everything is consistent, not impotent.
**Michele Mancioppi** 24:19 Thank you, that really upset me.
A fun half hour.
**Josh Suereth** 24:24 Do you know how long it took me to realize where the problem was? That's… that's the real disturbing part.
I think Lyudmila also ran into it, and it took… it was… it was not fun.
Yeah.
**Michele Mancioppi** 24:37 Yeah.
**Josh Suereth** 24:39 Cool. Alright. The… Oh yeah, Ludmela fixed a few issues with resolution, so if you're resolving from V1 or V2, attribute lookup is now correct. So that means if you're resolving from V run, it will look for a group that has registry in the name. If you resolve from V2, you don't have to do that, that's implicit.
And… Yeah, just other fixes and stuff. Oh, yeah, WeaverServe, sorry. This is another big one.
We have a UI.
you run WeaverServe, okay? It will actually open up a web browser, and it has a UI, that you can go to, and you can inspect everything, and you can run commands and stuff. We plan to, like, improve this over time. There are features in WeaverServe that are not implemented in the UI. For example, you can actually run JQ expressions on your registry and see what the resulting JSON is.
via the UI, and you can use the UI because we have, OpenAPI, I think it's called?
It's called, like, Utopia or something locally, or Oitopa, in, in Rust. It's like Utopia spelled wrong.
But you can actually call API things directly without the UI having been implemented. So, the UI is implemented for a piece of things that's useful.
But there's also just a regular old API you can call on Weaver if you need to use it programmatically as a tool, or you want to wire it into your agent to call it, or whatever. So, please try that out. It's, it's pretty cool.
I think that's it. That's all the things I wanted to highlight for people to try. For semantic conventions, I think that this… shouldn't change much yet, outside of eventually we need to talk about Weaver Package for Semconv.
and schema URL. But, we're not quite there yet.
**Liudmila Molkova** 26:33 What do you think we are missing from… Is there something in viever?
That is not there yet. That would stop us from… Publishing some conf schema.
**Josh Suereth** 26:46 No, I think your OTEP just needs to get merged.
**Liudmila Molkova** 26:49 I see, yeah, yeah.
**Josh Suereth** 26:50 That's… I think it's literally, let's get approval, like, the final approval and the commitment to then… like, I actually think we could start that migration now.
I am adding the lineage tracking, so you know what schema URL things came from, and you tag everything with the schema URL it was from.
I do want to get that out before we fully commit, but that… I don't think there's anything preventing SEMCOM from trying out V2 for everything.
**Liudmila Molkova** 27:18 Right, and for the OTAP itself, I really want to, show the coolness of it to Trask, or somebody from the collector, so people who will use the federation would have a chance to approve it. Traskal, I'll ping you, I wanna… Or maybe we can discuss it here, like, what would be a good scenario to demonstrate that app in the context of Java.
**Trask Stalnaker** 27:46 I think the, the Java… metrics… that are in SUMCOM already might be the easiest, since we already have them and we just want We're just, like, talking about how would we move them out.
**Liudmila Molkova** 28:07 Right.
I think, yeah, this, and I can pair it with… I think what's the important aspect is that there is more than one convention in the repo.
we will… we will want… if we publish conventions for Java, it should be one convention, not per library.
And that I will pick the second one, I don't know, just random… JMX metrics or something.
**Trask Stalnaker** 28:39 Yeah, yeah, I can, yeah, ping me. I can think of, like, you want an instrumentation that has… Additional attributes that aren't in semantic conventions.
**Liudmila Molkova** 28:52 Yeah, something else, whatever it is.
**Trask Stalnaker** 28:55 Sure.
Yeah, yeah. We've got lots to choose from.
**Liudmila Molkova** 28:59 Wonderful.
Thank you.
**Michele Mancioppi** 29:02 I have a question about… Modeling stuff in Weaver.
That… Maybe you can answer me.
So, I was using the… in the semantic conventions for this data, we… we have introduced Effectively, a model for log events, and those log events have a specific meaning.
And, the way we did it was, with a file like this.
To say, it's an event, so log event.
And, it can have… A bunch of attributes.
But this would fail validation.
Whoa, whoa.
That would sell validation without having something like this, where I would specify the resource attributes.
And I'm not sure I understand the rationale of that.
**Josh Suereth** 30:12 I mean, you don't know why you need to have a resource attached to everything, or you don't know why it would fail validation if you aren't validating a resource?
**Michele Mancioppi** 30:21 I don't know why it fails validation if I don't have an entity for that.
**Josh Suereth** 30:27 That's it. I think if your entity list is empty, so in… under… under your, your event, if you go back to that, there should be an associated entity somewhere.
Right?
**Michele Mancioppi** 30:39 No, I, I had to remove it because, this would be… too generic. It would allow me to, by putting something like this, it would allow me to put these attributes at all levels.
**Josh Suereth** 30:55 It would line up with those attributes at all levels.
**Michele Mancioppi** 30:58 Yeah, I could, I could put service.namespace on, On, the log attributes, and it'll still count as working.
**Josh Suereth** 31:07 It shouldn't. That sounds like a bug, actually.
So, if you're running into that, that might just be a bug in live check that we need to discuss and open, but, like, if you say, I rely on NXT Association and I want service, that means that, you know, we expect to find service and its attributes in the resource when we see this event.
Except entity associations is a one-of, so we expect any one of those. It doesn't have to be all of them.
So you want to pick the most specific when you do that, if… that you need, right? But yeah.
If you say, like, this could be a service or a deployment, great, we expect one of those two.
And as long as I find the attributes of one of them, everything should be validated appropriately. If that's not how LiveCheck is working, it's a bug, so just give us… give us a… open a ticket, and we can look into it.
**Michele Mancioppi** 31:59 And if I want to have, multiple entities?
**Josh Suereth** 32:04 multiple that are required. Yeah. We don't support that right now in the model. So that would be another thing to say, hey, I'd like to find a way to require multiple.
**Michele Mancioppi** 32:16 And I cannot extend entities by saying this entity has both that and the other.
**Josh Suereth** 32:22 Yep.
**Michele Mancioppi** 32:23 That is also not a thing.
**Josh Suereth** 32:26 We don't have extends for entities yet, because we're still sorting out the full data model. Entities are, like.
The bits that are modeled are stable, but we haven't, like, finished the modeling. So, if you have, like, use cases, just open tickets and things for us so we can see what they are, so we can get a better idea for how to model this stuff.
**Liudmila Molkova** 32:48 Are we even… Supposed, like, would one entity… is supposed to include a different one. My understanding that you had them independently most of the time were…
**Michele Mancioppi** 33:01 It depends, right? So the, I think that here I'm trying to misuse entities. We're actually making, bags of, Or is those attributes defined somewhere else?
Because I cannot make the differentiation between log attributes So, log record attributes and resource attributes.
I think that the concept of entity, I mean, that it's purely risk levels.
It's hard for me to imagine a use case where I want to talk about a deployment without talking about a service in the deployment, but… Technically, in that case, the entity would be the service, not the deployment.
**Josh Suereth** 33:44 Right, that's why, like, when there's a relationship between entities, like, pick the specific one. So pick… if service is a thing that you care about tagging to, tag to service, and then there should be a different way to say, hey, when I have service, I should see deployment.
**Michele Mancioppi** 33:59 Yeah, but…
**Josh Suereth** 34:00 That second part… yeah, that second part doesn't exist yet in SEMConf, but that's kind of, like, a way to think about that, of something that we want to figure out how to model. So basically, anytime you see a service, I also want to see a deployment, should be something I can define as a rule and enforce.
**Michele Mancioppi** 34:15 I believe that we came… we spoke about this a number of times in the past, because it keeps coming up, at least when I'm in the room.
Yep.
Which may be a Michele problem, to be honest, but… Why can't I say here at which OTLP level I want it?
Optionally. Why can't I say I expect the deployment status at the log record level?
And I expect service.name and service.namespace and deployment.environment.name in the resource.
**Josh Suereth** 34:49 Yeah, so right now, the way the model works is, because the group is of type event, everything is at the log record level.
If the service type is span, everything is in the span attribute level.
If the service is of type metric, everything is at the metric attribute level.
Right? And then if it's an entity, everything is in the resource level.
Yes. That last bit, like, if we ever have entities in more places than resources, yeah, that gets a little awkward, and we'll have to figure that out. And entity association might change.
might become deprecated with something new about entity association, or we might expand its capabilities to let you support that. That is something we can, like, again.
Use cases that you're struggling to model, or awkward, or don't live check correctly. Give us all the examples so we can start, like, making.
**Michele Mancioppi** 35:43 This is the example that I have at hand, and it reminds me what exists in OTTL, where, depending on the scope that you pick.
you may be able to modify attributes at lower levels or not, or higher, depends which version you think hoist is, yeah? So if you're working at the resource level, you cannot modify the span attributes, but if you work at the span attribute, or at the span level, you can modify the resources.
And this has the functional gap, where if I specify a group that is at a level higher than resource, I cannot specify anything about the resource.
**Josh Suereth** 36:20 No, so entity associations is supposed to be how you talk about your resource. If you say, look, this thing depends on this other group for its resource information.
That's what that's supposed to be. If it's not working out for you, it could be that the way we're doing associations isn't quite right.
Or that we need to rethink how we do entity relationships with associations, right? So, I think that maybe both of those are true.
But, like, writing down what you ran into, like, what error you saw, what you want to see.
and how you expected this to work, I think, is, like, the thing that we need. We have an entities modeling guide that I don't know if you read through in semantic conventions under docs. There's, like, a how to write conventions and how to deal with entities that tells you how we're thinking about the problem right now. But what you want to do, I think, is a legit use case we should support in some fashion.
how to model it here, the idea in SEMCOMF would be you define the signal at the signal level, and you define the relationship to the resource at the signal level.
And then you can define things about the resource and things that you need in, like, a set of groups. And that should be how we think about that problem there.
We might not have gotten it 100% right.
So, that's, like… the more you try this out, the more you run into problems, the more you report issues, the better we can make it. What you were saying with live check, where it was literally failing, though, or, like, allowing the attributes to be anywhere.
in the signal and not just on the resource, that is legitimately just a bug that we should go fix, and I think I know why that's happening.
But…
**Michele Mancioppi** 37:59 exactly how it failed at this a few weeks ago. I'll check it out again.
**Josh Suereth** 38:04 Yeah. Yeah, if you could get us some test cases and things, just say, like, anytime you see, hey, this is weird, at least, at least bring it up for discussion with Weaver, or open bugs for us, because we'd love to fix it and get it, get it, like, corrected. It probably just is weird and not intended.
**Michele Mancioppi** 38:21 Let me, let me run a thought experiment.
Yeah. If I do not find an entity that I find descriptive enough, so it either has only the service or the deployment, I want both.
Is the intended way with the model to define my own entity with these bags, and then point at that?
**Josh Suereth** 38:43 Yep.
**Michele Mancioppi** 38:45 Okay.
**Josh Suereth** 38:46 Now, what… That is true.
**Michele Mancioppi** 38:49 It will break like a brick the moment people start using entities to validate entities sent by the SDKs.
**Josh Suereth** 38:58 Yeah, I mean, so… I guess the question is, you have a set of things that you want to see in resource, right?
**Michele Mancioppi** 39:06 Yeah.
**Josh Suereth** 39:06 And you're saying there's not an entity that's specific enough, or that you have dependencies between entities you need to see in resource? Like, which of those two is it?
**Michele Mancioppi** 39:14 It does… in the auto-sematic conventions, there isn't… all the entities are too specific. They are too limited in scope. I want something that is actually the union of two or three of them.
**Josh Suereth** 39:29 The union meaning all of them together, or, like, it could be any one of them?
**Michele Mancioppi** 39:35 The union set of attributes.
to be the mean requirement. Like, you must have both service.name, optionally service the namespace, and you must have deployment.environment.name.
**Josh Suereth** 39:47 Okay.
I gotcha. You're unioning the attributes, not the entities. I'm still thinking of type theory.
**Michele Mancioppi** 39:54 Oh, we can talk about that. So, it's not a disjunction of types.
**Josh Suereth** 39:58 Yeah, it's an intersection. Yeah. Yeah.
Yeah, that's… that's… that's what… you want an intersection of the types, and it… which would be un…
**Michele Mancioppi** 40:06 Types would actually be the minimum common denominator. I want the types to be merged.
**Josh Suereth** 40:12 Sure.
Okay.
**Liudmila Molkova** 40:15 Sorry for a stupid question, so why listing multiple entity associations doesn't work?
Because there is no…
**Michele Mancioppi** 40:25 I want all of the attributes.
this…
**Liudmila Molkova** 40:29 Do you want to see?
**Michele Mancioppi** 40:29 pass… would pass the match if I have either service.name or deployment.environment.name, and I want to record both.
**Josh Suereth** 40:38 Yeah, so Lydmillet, we define entity associations as one of, not all of.
**Liudmila Molkova** 40:42 Oh, I see.
**Josh Suereth** 40:45 Yeah.
**Michele Mancioppi** 40:46 No worries.
It took me a while to figure it out, because it was… the name, quite frankly, this I read as Olaf.
Okay. Not as a penny off.
**Josh Suereth** 40:56 Yeah. Before, we had… we had this thing where underneath it, you would have one of and all of as separate, like, subcategories. It just… it gets really junky in YAML.
To make that not look like crap.
But that is something we could actually move towards. Daniel, you're here. I don't know if you're paying attention from the entity's sake. What do you think about allowing one of and all of modeling?
**Daniel Dyla (Dynatrace)** 41:21 I haven't been paying maybe as much attention as I should have, but… Yeah, I… can you, can you… Clarify the question a little bit?
**Josh Suereth** 41:34 Okay, so right now, when you define a semantic convention for a signal.
You have an entity association. The entity association is one of, for all entities that you list there.
Yeah. What Mike Kelly's saying is he would like to have the ability to have all of Instead of one of.
And what I'm thinking is maybe we just change the syntax to support allof and one of together.
**Michele Mancioppi** 42:03 I would also be fine by, by saying, by providing as a first-class citizen in the model, the fact that I want the entity that has all the requirements coming from these three.
**Josh Suereth** 42:16 Yeah.
I mean, there's…
**Michele Mancioppi** 42:18 the model thing… I think that the key… reads wrong. I think the key needs some experimentation.
Okay.
**Josh Suereth** 42:27 the lady.
**Michele Mancioppi** 42:27 entity association, like, I never would have read it as a disjunction.
**Josh Suereth** 42:33 Okay.
**Liudmila Molkova** 42:34 Plus one.
**Josh Suereth** 42:36 Yeah, I… so the default… It has to be a disjunction, so you can have disjunction and union work together, right?
**Michele Mancioppi** 42:45 Yeah, I think it's a problem of the key that was picked, you know?
**Josh Suereth** 42:48 The name, yeah, very bad.
**Michele Mancioppi** 42:50 Yep.
**Liudmila Molkova** 42:51 Do we actually need one-off? Like, if you… like, why would you want one-off?
**Michele Mancioppi** 42:58 Now, for example, there are situations that think about the Kubernetes metrics, where you may want a semantic convention to apply both if it is a Kubernetes pod or a replica set.
And that would be, that would be any off, right?
**Liudmila Molkova** 43:12 The way we model them, they are specific to the resource.
**Michele Mancioppi** 43:16 Yeah, that's why I picked that use case. So, imagine you have a log coming in with Kate's body ID equals 1, and Kate slash replica side.udid equals 2.
And, you have another log event, like a Kubernetes event, like, from the Cates, event receiver, comes with just Cates replica set UID 2.
I may want to say, if it has… if it has the replica set UID, I also expect it to have replica set.name and namespace.name, and it gets really hairy to model it If I have to… if I can only make conjunctions in that case.
gets really chunky. So the disjunction is important to have.
I think could even be enough, provided that the model gives me a way to create my own merge entities.
without going mad, and I think that there is a problem in the key that was picked, because when I read it, I thought it was a conjunction, but it isn't. It took me a while to figure out.
**Josh Suereth** 44:20 Okay, so I… if you can put all of this into a bug so we can track it, I do think we need to… we should address this, because I… I think you're right, and we… we're starting small with entities.
Yeah.
the… a few… a few thoughts there. One is, We can… we can probably support… both in the same syntax, where you could say, this entity could be one of these things, and then… or my entity association could be one of these things, and then one of the things can be a, you know, all of these, right? So you can have ORs and ANDs together.
So I think we can probably do that.
The other things that you were talking about, I think we need to check live check to see what error you ran into, and make sure that it's not accidentally, like, doing attribute, Allocation against the wrong level.
I think that's actually possible, because I think it's trying to erase the level very quickly in how it does with Rego. Last thing I want to say is you can write your own custom live check rules today, so you could actually make a Rigo policy today, where you would have your entity association be like service, right?
But you can have a REGO policy that says anytime you see service, you should also see deployment blah blah blah blah blah that comes out of us. And so you can make sure your live check enforces that for your system.
**Michele Mancioppi** 45:48 Yeah, but it's not, it's not, prescriptive in the model.
**Josh Suereth** 45:51 No, no, no, but I'm just saying as, like, an interim thing. Like, if you wanted to make sure that you're doing it today, you can still do that with Rego, but then, as we start trying to fix the model to make it so that everyone knows you're doing it.
If that makes sense.
**Michele Mancioppi** 46:05 Yeah.
Okay.
I'll, I'll see what I can dig up, and I'll run again my tests.
And then I'll open tickets.
Yeah, thanks.
**Josh Suereth** 46:18 I'd also be curious if you wouldn't… V2 syntax might change still.
to clean stuff up, but I would be curious if you wouldn't mind trying B2 syntax and see if you like it better. It should just be more natural.
But if we got any names wrong, or unintuitive, I'd love to get some feedback there.
**Michele Mancioppi** 46:37 I'll, I'll put on the to-do list for when I'm on the train to Amsterdam.
**Josh Suereth** 46:42 Yeah. I mean, what I did was I just asked AI to convert everything and get all my tests to pass, and then I'd look at it and see if it looks terrible, and I'm like, oh, okay, that looks fine, but sometimes it lies to you.
What?
**Michele Mancioppi** 46:55 That's also what I planned.
**Josh Suereth** 46:57 Yeah, yeah, yeah.
**Michele Mancioppi** 46:57 backlog.
**Josh Suereth** 46:59 Yeah.
**Liudmila Molkova** 47:01 You can give it the schema file, so it figures it out properly.
**Josh Suereth** 47:06 You don't even have to give it the schema file, you just give it a Weaver binary and say, here's the command you run to get the schema file, and it'll do it.
**Liudmila Molkova** 47:13 Or this.
**Josh Suereth** 47:15 Yeah.
Anyway, cool. I think that was it for the Weaver discussion. Was there anything else on the agenda?
**Liudmila Molkova** 47:25 I love it Yeah, I wanted to see, you think Mikael will be at KubeCon? Will anybody else be there?
Should we do some office hours?
For some conf… Weaver?
**Michele Mancioppi** 47:46 I mean, there is going to be, the, observatory one day in the project pavilion.
**Liudmila Molkova** 47:52 Turns out…
**Michele Mancioppi** 47:54 In the Project Pavilion, there is one day there. This time, organizing the pavilion did not work, because… reasons.
But there is going to be one booth one day.
**Liudmila Molkova** 48:08 The booth, it's just two people, right? It's not the office hours. Office hours will be held somewhere at some tables, and somebody will reserve them.
I'm going to put something on the agenda, but it sounds like nobody between you and Mikael and me are coming.
From this group.
**Daniel Dyla (Dynatrace)** 48:28 Me neither.
I… The booth is also not a great place to, like, gather more than, like, 4 people. You don't have a lot of space there.
**Liudmila Molkova** 48:38 Yeah, there will be some tables that we can reserve right now. Well, some are… some way to reserve things. And it's not booths, it's separate.
Okay.
Then I'll ping you, Mikael, we'll put something.
**Trask Stalnaker** 49:01 Alright.
Thank you all.
**Josh Suereth** 49:04 Thanks, everybody.
**Trask Stalnaker** 49:06 Bye.
**Liudmila Molkova** 49:07 Bye.
