SIG: Configuration WG
Date: 2026-01-05
Duration: 41 minutes
Zoom Recording URL: https://zoom.us/rec/share/Uz7pkMtEZ7XjAm_ZRLhEyzXQ9mdDAYn5QCNuKoKcjwKI16RXDNuoNRPj1-loK_cK.055Js5XD1656iuxz
============================================================

## Zoom Recording Transcript

**Jack Berg** 01:11 Hey, Gregor.
**GZ Gregor Zeitlinger** 01:18 Mo.
**Jack Berg** 01:20 Happy New Year!
Yeah, Happy New Year.
**GZ Gregor Zeitlinger** 01:32 Do we have any issues?
Or today.
**Jack Berg** 01:39 Let's see.
I think so.
**GZ Gregor Zeitlinger** 01:59 I have one question that is half Java-related, since I don't have so many things, I can just add it here.
Hi, Alex.
**Alex Boten** 02:26 Hello.
**Jack Berg** 02:30 Hey, Alex.
**Alex Boten** 02:37 That's the first… Meeting of 2026?
**Jack Berg** 02:41 The first hotel meeting, were we lucky enough to have it?
**Alex Boten** 02:44 I don't know. I think there's, like, 6 meetings at this time, so…
**Jack Berg** 02:50 There is a project triage meeting.
Earlier… They beat us for the first meeting of 2026.
**Alex Boten** 03:00 And here, I thought we were starting off the year well.
Achieving our goals, but we're already… we're already behind.
**Jack Berg** 03:10 Yep.
So, we got a couple of items that are, sort of, Popping up on the agenda.
There's sort of this category of things, which is, like, it's still a goal of mine to stabilize extremely early in 2026, and so…
you know, I think maybe we can do a quick, like, status roundup on what's going on with that. Like, what are the things in flight, just to make sure we're all on the same page about those? And which, if any, are sort of blockers to stability?
I think this other topic from Gregor, what if there's no declarative config?
maybe we want to go first with that? I know it's a Java-specific topic, maybe we could go after the stability topic from that perspective, because if it's Java-specific, I don't know, maybe we can give Alex a chance to drop off.
But I'm not sure where this is going.
**GZ Gregor Zeitlinger** 04:25 Just… had to grab my tea, sorry.
**Jack Berg** 04:31 No worries.
Let's do the blockers for stability first. I just wanna…
Maybe let's rephrase this to, status of stability.
Okay, so there's… there's a couple things going on in my head, related to stability. So, there's this PR over in the specification.
I have this… I had this draft PR,
To mark declarative config as stable. This is really old, right? I opened this back in June.
**Alex Boten** 05:10 And.
**Jack Berg** 05:12 Robert gave a pretty thorough review on this.
And, which I appreciated. And, this PR is the result of one of his comments. And so, you know, basically, his, you know, he had a number of comments that were
not just sort of simple things that could be done in the PR to stabilize. They needed to be broken out as separate PRs, and so, now we're sort of dependent on those changes, if you will.
And this is an example of one of those. It's just, like, getting consistent with our language with how we refer to, components and plugins. So this should… there should be, like, no functional change here, just, like, editorial inconsistency.
But if we try to stabilize
I don't think Robert will, you know, let this go until this is resolved.
And I think that's good feedback, too, so…
**Alex Boten** 06:09 Just reviewing this… PRL, probably…
I'll probably leave a comment in here, but…
If you look at the change in the template, it doesn't…
Doesn't match the change in the exp…
In the, different language, for the spec compliance matrix.
Pieces, so if you look at the template change…
**Jack Berg** 06:33 Oh, so is that out of date?
**Alex Boten** 06:36 Yeah, so it says here, register a plugin component provider, but if you look at the Swift and Rust implementation, or Swift and Rust definitions, it doesn't say that for the line 528 there.
**Jack Berg** 06:52 Well, okay, I'll go make sure to resolve that. That's, that's,
That's interesting that the build is not failing.
**Alex Boten** 07:00 Yeah, I don't know if it's just out of…
Out of date, or what… what is happening?
**Jack Berg** 07:06 Yeah, okay, I'll look into that. Thanks for that.
**Alex Boten** 07:08 Yep.
**Jack Berg** 07:13 The other thing, this is, this is something that I've… it's been on my mind for a while. What does this ID field mean, and what do we need to do around this? And so…
right now, in our, in our schema.
This is our compiled schema. We just have ID as, like, a static URI, That, you know.
it's, like, the OpenTelemetry domain, and it's, like.
I don't know, but what this idea is supposed to be, is it's supposed to be a sort of unique identifier that, it assists in, like, schema resolution across files, right? So, like, you know, another schema could reference the OpenTelemetry schema by ID,
And reference resources within this schema.
Other types within this schema, you know, using, like, a hashbang and whatever the syntax is for, you know, to reference relative definitions within this, this top-level resource.
And so, I'm nervous about this, because it's supposed to be a unique identifier, and we publish multiple versions of our schema, and you know, there's nothing in this URI that, you know, differentiates between versions.
And so, like, there's basically… I left a comment
here, or I opened an issue here that talks about this, and I think there's, like, two things we could do. We can either remove ID altogether, or we can embed versioning information in this ID.
**Alex Boten** 08:52 Yep.
**Jack Berg** 08:52 And, like, I think the simpler thing to do is to just remove ID for now, because it's not required, and we don't actually need it for anything, because we can always add it back later.
And if we need it, we can go to this type of strategy where we add it back later and embed version information in it. But for now, like, this is just one more thing that can… it's like another step needed in the release process, it's one more thing we can forget and…
And kind of screw up… screw up along the way. And so, I guess, like, my suggestion for now is to go with the simpler thing of just, like, dropping it until we need it.
But I do think we need to get this done before we stabilize, because, you know, I think what we're doing now is just, like, it's not correct.
**Alex Boten** 09:40 Are there any… Have you noticed any differences with any of the CodeGen stuff without having the IDE?
defined, or have you tried it without it? Does it do anything different?
**Jack Berg** 09:52 That's a good question.
**Alex Boten** 09:55 I suspect the answer is no, but it would be interesting to know if something else changes or not.
**Jack Berg** 10:16 I'll, I'll follow up with that.
I suspect no, but, you know, for example,
one in this PR, where I drop the ID, it's not the only thing I do. Like, so, over in this validate snippets, you know, build tooling, verification check, you know.
it was using, it was referencing the ID to, you know, resolve schemas and sub-schemas, right? And so, like, I did just that logic a little bit to get the tool that we use to do schema validation in JavaScript to continue to work, and, you know, that tool's called AJV.
And, you know, so basically, the workflow that we did around AJV had to be adjusted, and it's possible that, you know, Go's tooling or Java's tooling would have to be adjusted similarly.
**Alex Boten** 11:08 Yep.
**Jack Berg** 11:08 And I hope that none of the tooling… my impression is that none of the tooling will
break from ID not being present, because, like, the spec's very clear that it's not required, and if you go look at something like Schema Store, you see all sorts of examples where ID is not present. So it's like… it's almost like a coin flip, whether, you know, any particular schema decided to include or exclude ID, so…
That's, like, you know, some…
An argument for, it shouldn't matter, but, you know, we should go see for ourselves.
**Alex Boten** 11:40 I feel like that's been my experience with JSON schema as a whole.
As, you know, you get an example of things in very different ways all over the place, and you just never know what the tooling will support.
**Jack Berg** 11:51 Yeah.
**Alex Boten** 11:52 Unfortunately.
**Jack Berg** 11:53 It's like, it's…
it's kind of annoying that JSON schema seems to be the best tool available for this type of thing, and it's just so… it's not… it doesn't really inspire confidence.
Right? There's, like, there's all these different versions of JSON schema with all these different vocabularies, and none of them are, like, stable, right? The best we got is, like, Graph 20-2012, or something like that. That doesn't…
That doesn't really inspire confidence.
And, like, even if you go to something like Schema Store, you know, it has guidance that says, like, use the draft from, like, 2025 or something like that, and it's like, yikes. The guidance is to use something 10 years old when there's, like, 3 versions later than it.
**Alex Boten** 12:41 10 years old, that's a draft.
**Jack Berg** 12:43 Right, exactly.
**Alex Boten** 12:45 Right, yeah.
**Jack Berg** 12:47 So, yeah.
That's what we got, though. Okay, so that was, this is the last thing on my mind that's, like, schema-related that I think we ought to resolve before stabilizing. And then, you know, the last thing is update implementations to the RC3, right? So,
you know, just to, you know, give us another chance to find any issues with that. I've done this for Java already. Everything looks good from my side, but yeah, we just want to make sure everybody's on board.
Anything else come to mind?
I, like, what I want to do is I want to, like, at some point, open, change the PR,
in the specification, this PR to mark is stable, I want to promote this from a draft to, you know, ready for review. And, like, I want everybody in the declarative config sig to go give a thumbs up. I want us all to be, like, give it a checkbox, right? A green checkbox.
And then, you know, like, you know, like, we'll see what happens with the broader community, but we should at least all be aligned.
**Alex Boten** 13:59 Yep.
Yeah, I mean, I don't…
I don't know that the only… the only concern I have is not related to this specifically, it's to do with the Prometheus exporter. And the only reason that's a concern for me is that my… my thin line across the implementation of configuration was to use the collector as, like, the… the guinea pig of… of the goal implementation, and…
that… that is not currently possible with… with the RC3 because of the Prometheus exporter. At least not yet. I… there's… there's a chance I might…
hack some code in the collector to support both, but it's… it's gonna be pretty gross if I do, so…
**Jack Berg** 14:42 Right, and so that's, like, a priority.
of…
yours, and it's a priority of, like, mine as someone that works for Grafana. So, like, you know, my team is actively, you know, working on and interested in the stabilization of the Prometheus OpenTelemetry compatibility, so.
**Alex Boten** 15:04 Yep.
**Jack Berg** 15:05 Yeah.
I'm gonna do what I can to help that.
**Alex Boten** 15:10 Cool. Yeah, it sounds like, David Ashbold is already working on it, and there's a few…
He's… it's… you know, he's…
link the issue that he's opened in the specification around marking… around the stabilization, so… but it sounds like all of this is currently behind,
some other work, that's around stabilizing, I think, the Prometheus definitions and the specifications, so…
I think once that's done, then it sounds like then they'll be able to work on the export configuration.
But yeah, otherwise, I think the rest of the configuration all makes sense, and I mean, other than removing the slash development in the key of the Prometheus exporter, I don't know that there's anything else that will really need to change.
At least from the Go implementations.
**Jack Berg** 16:03 Yeah, and on that front,
The removal of the slash development.
So, we've been talking in the JavaSig, and you know, let's say you're using something that's in development, and then it gets promoted to stable.
It's kind of a bad user experience to require you to go and remove that slash development suffix.
And so what we've been talking about is, can we, like, provide tooling to automatically do that, like, in the Java implementation, right? So, like, you know, if you are an instrumentation library, and… or any component that's trying to configure itself, like, can we…
if you ask for Prometheus slash development, or Prometheus, can we make sure that you, like, are configured accordingly, right? That we make a best effort to look for the presence of, like, the lack of that slash development suffix.
Even though, like, you know, maybe you as, like, a tool, expect that slash development suffix.
And, you know, we're… we've been thinking about that, And…
you know, I think it's… it's possible that, like, you know, what we should do around that should be specified, so that, like, every language should do something similar there, because, you know, this will be a recurring pain point as things go from, you know, in development to stable.
**Alex Boten** 17:31 Yeah, I mean, this is also…
This will also vary on a case-to-case-by- basis. Like, I think our expectation is that the Prometheus exporter config won't change too drastically between now and when we mark it as stable.
**Jack Berg** 17:46 Yeah. But, you know, there's a good chance we're going to have.
**Alex Boten** 17:49 Other features that are completely, like…
In development, and we can't make any guarantees, and so having any language implementation, the best guess, the, you know, the…
configuration under that… under that, stanza is going to be, you know, messy at… messy at best, unpredictable at worst, and…
I don't know if that's something that we'll be able to really support or not, but I agree, the end user experience is not great.
But we kind of made that decision to say, well, if you're using a development
Functionality, like, you should just expect it's going to be kind of bumpy and…
**Jack Berg** 18:30 Yeah, and we'll have to think that through, but you know.
the… I'm just trying to think through, like, what the user experience is for
somebody that's, you know, because every implementation of declarative config is, like, pinned to a particular minor version of the schema. Let's call it, like, 1.0.0RC3 for Java, for example. Like… like, let's say 1.2 comes out, and Prometheus is stable.
Like…
or let's say 1.2 comes out and Prometheus is… continues to be experimental with some breaking changes in the schema. I'm just trying to decide, like, what the difference is from a UX standpoint, if we, like.
If we add some smarts to, you know.
Look for configuration with or without that suffix.
Versus, like, are more strict about it, like, and, you know, explicitly require the user to update their configuration to remove that suffix. Like, what's the difference, actually? Because the user's already, like, exposed to, you know, breaking changes.
as, you know, the Java implementation goes from 1.0 to 1.1 to 1.2.
And, you know, eventually, like, Prometheus will stabilize in there, and…
Is it really, like, a worse experience for them to just, like, omit that suffix and maybe be exposed to some sort of,
Property mismatch type of thing.
I think I need to write down the different cases to, like.
In the different scenarios that we could encounter before I, like, form an opinion on that.
**Alex Boten** 20:15 Yeah, and I mean, it could be the case where we…
We suggest implementations offer a migration path from one version to the other.
like, the implementations themselves would be able to know, oh, okay, well, this looks like it might be, like, a 1.0, it's RC3 config file, so I'm gonna try and…
translate one into my current version. This is what we do in the collector for migrations. This is what I implemented between, like, 0.2.0 and 0.3.0. Like, a user can come in with either configuration, and it still works.
But I…
I don't know how much we want… how long we would want to support this. Like, from an end-user standpoint, it's a much better experience, right? Because I can upgrade…
My config without necessarily being… Breaking my code.
And from an implementation standpoint, we can warn users, hey, it looks like you're still using an old config style, you're going to have to do something about this.
Which is what we do in the collector, but it's…
It's messy from the implementation standpoint, but…
**Jack Berg** 21:24 Yeah.
Okay.
So, that's an interesting sort of tangent.
We can… we can talk about that more.
But I don't think it's, you know, blocking or anything for going stable, so…
**Alex Boten** 21:42 Right.
**Jack Berg** 21:44 Alright, if there's no other comments on, you know, the status of stability, do we want to move on to Gregor's topic?
What's up, Gregor?
**GZ Gregor Zeitlinger** 21:57 Right, so, the question that is not Java-related is, how do we,
think about an OpenTelemetry SDK object,
Where declarative configuration is not used.
I don't know if this is…
relevant in other languages. At least in Java, we have an object that gives access to the config provider.
And once, we move to stability.
We, will have a method to access the config provider, even if declarative configuration is not used.
And we could return a null , or we could return something else.
And that's what the issue is basically about.
**Jack Berg** 22:52 Yeah, so is this kind of the question in a nutshell? We've got this thing called config provider. This is how instrumentations, you know, access, you know, content from declarative config. What should its behavior be when declarative config is not used?
**GZ Gregor Zeitlinger** 23:06 You have already, decided on one option.
by asking the question. You have already said that config provider is still irrelevant. From reading the spec, I couldn't figure out one way or the other, because the spec simply says, here is configuration, but
When reading the specification, I got the impression that this only applies to when declarative configuration is used.
**Jack Berg** 23:36 In which part of the spec? The spec related to, like.
You know, all the different providers, like meter provider, tracer provider, or are you talking about, like, config providers specifically?
**GZ Gregor Zeitlinger** 23:47 Let me just open… Alright, so if you go under specification,
Then it's configuration, I think then API.
And then API, it says…
No, actually, it does not say,
How to get the config provider, because here it just says how config provider should behave.
**Jack Berg** 24:25 It's supposed to be sufficiently decoupled from declarative config that there could be other config provider implementations, just like, you know, tracer provider allows for alternative implementations, and…
**GZ Gregor Zeitlinger** 24:38 You know, the SDK implementation of.
**Jack Berg** 24:41 config provider, which is based on the declarative config file.
That's sort of, like, the default, but others are possible.
**GZ Gregor Zeitlinger** 24:51 Well, that's not how I'm reading it, the first sentence.
The instrumentation Configuration API is part of the declarative configuration interface that… that seems to make,
A statement that this only applies when declarative configuration is used.
**Jack Berg** 25:13 I see that… I see that interpretation.
I don't think… I think that…
Like, the intent is, like, of this sentence.
Is, you know, within this configuration directory, we have a bunch of different files, and a number of them are related to each other.
the API, the SDK, and the data model documents are all about declarative config, and, you know, they sort of are, like, read together. And…
And that's kind of, you know, they're different from the, you know, the SDK environment variable document.
And so I think, like, I think this is, like, an attempt to be, like, a grouping mechanism, to say, like, hey, like, despite this directory having a bunch of files, a few of them are logically connected to each other.
like, and you can kind of see this if we go to SDK, it starts with the same sentence.
**GZ Gregor Zeitlinger** 26:13 Right.
**Jack Berg** 26:14 And if we go to… let's see if data model starts with the same sentence. It does.
So, like… Yeah, it's a bit confusing, but
I don't think the intent is to say that, Config provider.
Is only meant to be used in declarative config.
**GZ Gregor Zeitlinger** 26:38 I also couldn't find any explanation of how config provider
Should behave when declarative config is not used.
Did I miss anything?
**Jack Berg** 26:50 No, I don't think you did, right? So, well, maybe.
Let's see. So… Config provider's really simple, right? It just has, like, one operation. Get Instrumentation config.
And so it says, if the instrumentation node is not set.
This must return nil, null , undefined.
So that, that in a way, is…
Maybe you can interpret that as a statement of what to do if declarative config is not used.
Right.
**GZ Gregor Zeitlinger** 27:26 I would say this means if the part of the YAML file is not present, it's how I read it.
**Jack Berg** 27:34 Yeah.
Yeah, I… I see that.
But, I mean, we could decide that we want to change the meaning to mean that
We could… we could, like, clarify it. I think, you know, if…
you know, just kind of reflecting on conversations we've had in the Java SIG with Trask, Gregor, you know, I've made, like, the point a number of times of, like, hey, why should get instrumentation config return null instead of empty?
And, like, the reason I keep asserting is because, like, maybe some instrumentations find it relevant to know if, you know, declarative config was or was not used. And so, like.
I've been… I've been treating null , a null response for get instrumentation config, as, like, a signal that declarative config was not used.
So, like, this has kind of been my interpretation of it, but, like, it's not… it's not perfect, right? Because, like, you know, it could… it would return null if declarative config is not used, or if the instrumentation node is not set, right? So it's, like, it's sort of overloaded, and it's not really a clear signal, to your point.
**GZ Gregor Zeitlinger** 28:45 Right.
**Jack Berg** 28:49 And I don't think there's anything else in the SDK
portion that would describe this. So, like, no, that's not the right section. If we go to SDK config provider, where's that?
Why is that not… oh, confirm provider.
Wow, yeah, there's basically nothing in here. This is as much as we say about the SDK implementation of it.
So there's no… there's no language in there about what to do.
If, declarative config isn't used.
And, yeah. Oh.
Go ahead.
**GZ Gregor Zeitlinger** 29:39 So, do I get you right that,
Config provider would make sense, and we should just, add more
description there, how it should behave when you don't have declarative configuration, and how you should, like, I don't know, map environment variables to…
The config provider, methods? Or is that not the direction that you're… Proposing.
**Jack Berg** 30:11 I think a little bit of that. So, my intent with Config Provider was to have one API that instrumentations could access for all configuration needs. And, you know, I think the intent was to decouple it from the declarative config
implementation? Like, sufficiently that, like.
things like what you're describing are possible. That, like, you could provide alternative implementations of config provider that, you know, still implemented this contract, but using different sources.
And, like, kind of where I'm not really sure is, like, should the specification standardize how
environment variables are… environment variable configuration is exposed through config provider. That's the part I don't know about.
**GZ Gregor Zeitlinger** 31:07 Yeah, we have some… we have some experience, while working on the Java agent.
That suggests… It's really helpful.
Because, we want to have…
Probably longer period of time where you can use both, but you don't have to
code against two APIs when writing an instrumentation.
**Jack Berg** 31:38 Yeah. And the mapping of.
**GZ Gregor Zeitlinger** 31:41 Environment variables to, the, pre-structured way of YAML files.
Did not seem Java-specific when we worked on it.
But at the same time, I'm not sure if it would be too much to put it into
Like, formal specification.
More… maybe a recommendation would be sufficient.
**Jack Berg** 32:07 Right? Like, it's very convenient to, like, what we're doing in Java, where the agent is coalescing on config provider as its access point for all things config, whether that be, like, environment variables or, you know, declarative config. And, you know, the question is.
you know, should we standardize that across other languages? Is that, like, a tool, a pattern that, like, others would benefit from?
Right.
I don't… like, I definitely agree that we, like, what we're doing in Java is useful, and I just… I don't know how other, maintainers would react to it. Like, whether they have the same types of needs we have, and, like, you know.
But, you know, it's a… I think it's a worthwhile question to throw out there.
If we were to specify that type of behavior, like how environment variables map to config provider, I think the place to do it would be in the SDK document.
Right? Like, keep the API documents sort of clean… clean and free from these details about how, like, you know, what we're essentially saying is, like, there's multiple configuration sources which are,
You know, commonly exposed.
Through Config Provider, and, you know.
the SDK document, which is very brief right now, could elaborate on that. Like, maybe there could be two config providers, one for, you know, environment variables,
or… let me just put it back up. Maybe there could be two SDK config provider implementation options, one for environment variables, one for YAML.
Or maybe there could be just, like, one SDK config provider with, like, you know, that can retrieve information from both sources and has some sort of prioritization-like logic between them.
**GZ Gregor Zeitlinger** 34:03 from both, I…
I think this is what you advocated against in the past. Like, if you have a YAML file, then it should be the only source of truth, and merging seems to go against that.
**Jack Berg** 34:17 I just mean, like, there's, like, I'm not trying to say, like, merge if there's, like, conflicts, but, like, you know how we have, OTel Java Agent enabled?
Like, we have some sort of, like, Java agent options, which are,
I don't know, I'm just thinking out loud here. I'm trying to decide if there's any case where, you continue to want to look, like, at environment variables when declarative config is used.
And as I'm saying that out loud, yeah, I think I'm starting to agree with
with what you were saying and with what I've said previously, which is just choose one or the other.
**GZ Gregor Zeitlinger** 35:00 In the agent, this is really only done because of weird class loading things, not because we have decided that this is the best possible pattern.
**Jack Berg** 35:19 Well, so… Okay, so let's say we agree on that, that it's either environment variables or YAML, not both.
well then, I think you could still kind of update this document to describe two different config… SDK config provider
You know, implementations.
**GZ Gregor Zeitlinger** 35:43 Right, and… Would that mean, that,
We would change the sentence that says, return null if the instrumentation node is not set.
to say, Return null if declarative configuration is not used.
**Jack Berg** 36:06 We gotta figure out what to do about that. Yeah. I'm not sure.
**GZ Gregor Zeitlinger** 36:10 Well, this is really key, because,
as an instrumentation author, it doesn't help me to know if the instrumentation node has said what I really want to know.
If instrumentation node… if declarative configuration is used.
If at all, maybe I… I just don't need to know that, because I can just
say, give me a structured list, and the structured list is only possible in declarative configuration. This is kind of how we do that in the agent.
By doing… by having the implicit knowledge, but…
I agree that explicit would be better, but just knowing that the instrumentation node is set doesn't give me this type of information.
**Jack Berg** 37:04 Yeah.
like, what do I want to do as an instrumentation author? Like, so…
I want to know if the user has made, like, any attempt to configure
Instrumentation at all. And then, like, my specific instrumentation library.
And if they haven't made any attempt to configure it, then I want to use, like, defaults. If they've made an attempt to configure it, regardless of whatever that mechanism is, environment variables or YAML,
I want to, you know, I want to parse those options, and I think what you're saying is, like.
Maybe it's important to the instrumentation author to know whether the user is
Attempted to configure it with environment variables, or…
Or YAML, like, maybe that difference is meaningful, because you kind of have a different configuration interface for the instrumentation library based on, you know, environment variables or YAML, but, like, I'd hope we could avoid that.
And… And it just, like, it doesn't matter what the source is for the instrumentation library.
**GZ Gregor Zeitlinger** 38:13 In the agent, we have achieved that so far.
So for all the existing configurations, we don't need to look at this explicitly.
So, from that point of view,
We could get rid of this,
Distinction, and we could say it would never return nil, and it would still work.
**Jack Berg** 38:39 Right.
**GZ Gregor Zeitlinger** 38:57 So I'm not sure… I'm not sure really what this… what this line is doing, if.
**Jack Berg** 39:02 What the sentence is doing, if, like, you know, instrumentation doesn't actually need it.
I'm open to deleting this line or, like, or modifying it and having, like, a conversation about, like, what the actual needs are for instrumentation. This was, like, written
sort of,
before these… any of the things that we've been doing in Java existed, and we've learned a lot since then. And so, like, you know, this is a document in development, and we should treat it like that, and update it to suit our needs.
Yeah, so if this isn't serving… if this was, like, a misguided idea, like, yeah, we can get rid of it.
**GZ Gregor Zeitlinger** 39:52 Okay, yeah, I think that's,
good feedback, I will, write that down in the…
And the issue, and then also create a separate issue to,
to have different implementations of config provider,
I'm not sure if we should…
Specify also the mapping of environment variables to config provider.
Maybe leave that as a next step to see if…
There's a need from other lang… from other languages before we, add that here.
**Jack Berg** 40:38 Yeah, I think we need to decide if, like, other languages want standardization around that.
You know, if they do, then, like, yeah, let's try to standardize. If they don't, then, like.
you know, why write something down in the specification that only Java wants?
Like, we can just do that thing.
**GZ Gregor Zeitlinger** 40:57 I had…
**Jack Berg** 40:58 So, don't waste the effort, essentially.
Alright.
**GZ Gregor Zeitlinger** 41:08 Cool, thanks!
**Jack Berg** 41:09 Thank you.
All right, that's all on the agenda. Any other topics before we go?
Alright.
Thanks for your time, everyone.
**Alex Boten** 41:24 Thanks, everyone.
**GZ Gregor Zeitlinger** 41:25 Bye.
**Jack Berg** 41:26 See ya.
