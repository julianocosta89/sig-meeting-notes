SIG: Specification SIG
Date: 2026-03-10
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:00:25 Hello, hi, Bob.
Bob Strecansky 00:00:39 Doing alright?
Ted Young 00:02:14 Lolo.
Liudmila Molkova 00:02:18 Hello, good morning.
Jack Berg 00:02:20 Hello.
Liudmila Molkova 00:02:27 It's my turn to run this call.
And let's give people a few more minutes to join, and then let's get started.
We have profiling SEEK today to talk about profiling State TA.
And I think what we discussed is that if there are any topics, we probably would discuss them first.
And then we would spend the second half, or whatever part of the meeting, on the SIG review, SIG updates.
things. So if you have any topics, feel free to add them before.
Ted Young 00:03:14 And by the way, I can't quite remember where we landed, but I know we wanted to keep a drumbeat up on the stabilization effort here.
But just to let you know, I'm gonna be, out for the next 3 weeks after this, so I won't be able to do those presentations. But other people could.
Liudmila Molkova 00:03:38 It seems our agenda…
Austin Parker 00:03:40 Could we do, like, 5 minutes at the top for stylization?
I know we brought it up at… last week.
At GC.
Ted Young 00:03:53 Yeah, so we've been doing standing… were you here at the spec meeting last week, Austin?
I think you were.
Austin Parker 00:03:59 No… of a…
Ted Young 00:04:02 Yeah, we've got these standing topics now, that are report backs, and I kind of pasted in everything last week about stabilization.
Austin Parker 00:04:11 Okay.
Ted Young 00:04:11 But it feels like we need to actually, like, drill into the individual things on some cadence in this meeting to kind of flush them out and turn them into Like, how do we turn these work streams into actionable stuff? Seems like…
Austin Parker 00:04:28 Yeah, I… yeah, the specific thing I wanted to talk about, like, right now is that We… we… I would like to just get the OTEP.
over the line, so that we can say, hey, we agree, these are the work streams, and then we can move forward into splitting that and doing stuff, so my reason I want 5 minutes right now is just to kind of Ask people to go look at 48, 13, and re-review…
Ted Young 00:04:59 Yeah.
Austin Parker 00:05:01 It… it…
Ted Young 00:05:03 And… I think we… we had, like, a brief discussion about it. I mean, so part of it is, yeah, the OTEP's not getting, you know.
It's definitely getting, like, responses, but part of it is, like, it's a very big, high-level thing, and there's maybe some concern that, like, maybe some people are kind of, like, crashing out in terms of giving feedback on something so large, so it might be… good if we to… Go through some of the individual work streams so that people understand what they are.
If… if we can't get… get enough traction directly on GitHub.
Austin Parker 00:05:45 Yeah.
Ted Young 00:05:45 Everyone go look at this thing and respond, and if that's not working, then I think we just need to start breaking it down in this meeting.
Austin Parker 00:05:52 Yes, my ask is, again… If… if it is truly impossible for us to… agree on this document in its current form, then please just write that under the document, and we will move forward, like, this has been sitting open for a couple months now.
you know, we've gone through several rounds of review. I would like for us to at least all, you know… again, the goal is to agree that these are the high-level goals, and that These are the work streams that result in those, and then Merge this, and then move on into the actual individual parts, not that… not anything else, so… I would like for us to… and if that is impossible, then that's impossible, and if it's impossible, please write it on the thing, and we'll move forward from there, but I really would like for us to at least go into KubeCon all agreed on… So that's my only… point in this.
And I'll be here Next week.
If we wanna talk about specifics.
Ted Young 00:07:03 Okay.
Liudmila Molkova 00:07:06 Anyone wants to bring anything specific?
Okay.
Then, I… Put it here, it's a quick FYI.
Kubernetes SIG are stabilizing semantic conventions for Kubernetes. They just reached realistic in the date.
And if, it's interesting to you.
Please take a look, this is the great time to share feedback.
Okay, moving on. Jack, should we merge up in telemetry configuration into spec? Do you want to talk about this? Do you want to present?
Jack Berg 00:07:54 You can present. I'm mostly gonna talk. I don't need to go to anything in particular. So, the context is that, declarative configuration is stable as of a couple of weeks ago. That's great.
Declarative configuration in the specification has a number of documents that lay out the data model requirements and the API and SDK requirements, and those documents, or major portions of them, are stable, but the data model links out to this other repository, OpenTelemetry Configuration, and that is where the actual JSON schema representing the data model lives and is maintained. And so, you know, I was bringing up this, this idea, there's this PR open in the spec, where I want to propose that we change the spec contribution process to be declarative configuration first, where, you know, if you propose a change to the SDK specification that introduces or changes configuration surface area, you should simultaneously propose how the declarative config schema is going to change, so that they can be evaluated in lockstep.
you know, the declarative config schema is going to end up being a really important user-facing part of our ecosystem, and so let's consider these things holistically. So, on that PR, a couple of people, Carlos and, And Daniel Dilla suggested, hey, why don't we just merge the configuration repo into the spec?
And, you know, that way, when you make your spec change, you can simultaneously, and in lockstep, make your change to the configuration schema.
And that's a… that's a good idea. That has, like, some merit, but there's… there's some downsides to it, and so I thought we could discuss it here.
the… the main downsides that I see are that the, the maintainer expertise required for the schema are different than the maintainer requirements for the specification. The maintainers for the specification are the TC right now.
That's just the way it is. We've talked about changing it, but for now, it's the TC, and maintaining the configuration schema requires knowledge about, like, modeling stuff, and JSON schema, and a bunch of rules that we've kind of built up about how we model common scenarios.
It also requires knowledge of the tooling that we've introduced for, you know, compiling and validating the schema. So, yeah, the maintainers that we have over in the configuration repo have developed some expertise in that.
And then the other reason why it might not be a good idea to merge it is because they're versioned differently.
The configuration schema just, you know, published a 1.0 tag, and we want to be able to version that separately than the specification.
And so it kind of is reminiscent of breaking out the semantic conventions from the, from the specification a while back. I think the versioning was a major reason why that was done. So yeah, that's some of the context behind this. Wondering if anybody else has thoughts.
Liudmila Molkova 00:11:10 Remember how we've done… Oh, sorry.
Remember how we've done the merging, sorry, separation of semantic conventions? We have a section in the spec that says that Semantic conventions must provide something, and then there are sections in semantic conventions that have nothing to do with the spec.
And maybe it's the… a similar story, where the spec could link to, Configuration, and if you modify that file, you inevitably have to go and modify the configuration as well.
Tigran Najaryan 00:11:49 Jack, can you maybe show an example of what you think needs to be modified in a lockstep, in two places, so that it's clearer?
Jack Berg 00:11:59 Yeah, here's an example. So, David Ashball has a PR open right now to modify views.
to, add a new field that's called disabled. He wants to, where's this PR? I see Loud Mill is navigating to it.
Liudmila Molkova 00:12:17 the opt For metrics?
Jack Berg 00:12:19 Yeah, yeah, the metrics opt-in stuff. Yeah, so the way that this is currently proposed, and it's going through some iterations, I think, so I don't think it may have reached its current… its final form, but the proposal is basically, yeah, like, there's an enabled flag on the view stream.
And, you know, look, look what… how David is proposing this. He's using declarative configuration in the PR description to show how this is, like, gonna change. It's a communication tool. And so, you know, it would be great if that could be done in lockstep with the change to the specification text.
Or maybe not in lockstep, like, what I was proposing in my PR is that they're considered together, and we… maybe we don't have to be so rigid that they're merged, like, you know, simultaneously, but, you know, it's clear that when you propose a spec change, you propose a corresponding config change, and they're merged around the same time as each other, without being so, maybe, rigid.
Ted Young 00:13:18 Honestly, to some degree, I feel like we've always done this, right? Like, we never had a config file like this, but anytime you defined an SDK component or something like that, you would have to define… The baseline of how it was configured, and that would turn into environment variables, and then people would steadily want to tack more on.
more of those environment variables on. So, in a way, like, that work's always kind of gone through the spec.
It's just never been organized enough and presented so well as declarative config, so maybe it just didn't feel like we were doing it.
Jack Berg 00:13:52 Yeah, and a long time ago, the environment variables stopped staying in sync with the configuration surface area of SDKs, just because it became impractical, because the complexity we wanted to encode.
Ted Young 00:14:03 You'll see that there'll be an initial set of, like, new component or a new change and config that needs to come along with that, and then over time.
People want more configuration.
Right? Like, that's the pattern we see. We give people some amount, and sometimes that additional configuration is like, could you literally let me… drive it through the config, but I feel like that part is gone, right? That was the discrepancy where we didn't want to add MVARs.
So the idea that you can't drive it now, that's just gone away. So it feels like we should be tightening these things up. And the only time you should be trying to add configuration is because you're literally trying to add a feature, right?
Jack Berg 00:14:48 Yeah, a feature to the SDK specifically, and a feature that, that has configurable surface area to the SDK. There's many things in the spec that do not have this.
Ted Young 00:14:59 Right, right. But it's almost always probably some kind of SDK code change that would be going along once we're settled into this kind of config. It's not like MVARs, where we might be tacking them on later on their own.
So… This really makes sense to me, I guess what I'm saying is it seems like after we do a big lift, you're not talking about config unless you're also talking about, like, a spec change of some kind.
Jack Berg 00:15:23 Yeah, yeah, no, that's how the config schema is. There's basically… now that we've caught up to the spec, and there's nothing in the spec that isn't modeled in the configuration schema, like, future changes to that schema, like, they're not going to happen unless there's a corresponding spec change.
Ted Young 00:15:39 Daniel?
Daniel Dyla (Dynatrace) 00:15:41 Yeah, so what the… Jack's last point there is kind of… what I felt was the crux of this issue when I originally made that comment on the PR.
Is that every change from configuration, or most changes in configuration will come from spec and be driven by spec in some way.
In that way, it's quite different than semantic conventions, where semantic conventions evolve almost entirely separately from the spec. I think it's much more similar to the protocol.
To me, it seems like the downsides are mostly… Process and tooling driven.
And there are ways around that. For example, you can use the code owner's file to say the configuration maintainers own this section of the spec.
And so on.
As far as versioning goes, Is there… A specific reason not to have the version?
be the same as the specification version, because you're… you're configuring specified features. It seems to me actually pretty reasonable to have them share a version, because you say this configuration, you know, configuration 1.
64 is compatible with an SDK that implements version 1.64 of the spec.
To me, that actually seems like it would potentially reduce some confusion around… I'm trying to configure either, an experimental spec feature that's not implemented yet, or vice versa. You know, an SDK implements some feature, but it's not, covered by the version… the version mismatch problem.
Jack Berg 00:17:33 I think is a little bit alleviated if they're the same.
Yeah, yeah, I… I haven't thought about that before. That's… that's a good point. So… I have some thoughts off the cuff, but I think I would need to sit down and marinate in that a little bit, Dan, to come up with coherent thoughts, but like, you know, so one thing that comes to mind is that, you know, so there's a property in the config schema called file format, and you say… you're stating what file format your schema is conforming to.
like 1.0, 1.1, and it's just the major and minor version, because the idea is you exclude the patch because there's, you know, patches don't include features, so it's just, like, noise for users and for consumers of that. But, like, there's these semantics about how SDKs are expected to interpret this file format and, like, you know, accept or reject incompatibilities between the version they are conforming to and the version specified Specified by the user.
So, and it's basically, like, if the major version aligns, like, the SDK will make a best effort to interpret the contents.
But so, like, if the SDK is… if the specification is producing minor versions on a monthly basis, that's, like, a lot of file format versions, and, like, I don't know, it may increase the perception of that there's, like, incompatibility, and that you'd, like… and just confusion around what this, the file format actually needs to be from the user's perspective.
That's one. And then the other thing is we, we register the JSON schema with this thing called Schema Store. Schema Store is this open source project that collects JSON schemas, and IDEs integrate with Schema Store to automatically provide, like, auto-completion features when you're typing out JSON or YAML documents, which conform to JSON schemas. So, like, the churn that the specification has in its versioning with, like, a monthly release.
would mean, like, lots of versions over in Schema Store. So those are two things that come to mind, but it's an interesting point.
Liudmila Molkova 00:19:39 I wanted to challenge that the spec, sorry, the config is only about the spec. There will be a lot of config about specific languages, and a lot of config related to semantic conventions.
And, hosting it in the spec would mean that, ideally, we would have to break it down into multiple parts and host configs for a specific component in the corresponding repo.
Jack Berg 00:20:03 I did forget about that, yeah. So, like, you know, there's this whole instrumentation section of the spec, or the config schema, which is, You know, based off of semantic conventions. So, you know, we encode the configuration options that semantic conventions writes out, and the idea is that we have standardized configuration for instrumentation libraries as well.
So yeah, that challenges the notion that config schema only changes when the spec does.
Ted Young 00:20:36 But that, to me, sounds like… you've got… you've got an extensible configuration spec, right? So you're gonna have some things that are versioning along with that, and other things that are out there and have nothing to do with us, right? Even written against this, this config file, but not even part of OpenTelemetry and coming to these meetings.
Jack Berg 00:20:58 Well, let's hope it's all part of OpenTelemetry. Like, right now, I don't know of any scope which is, like, outside of OpenTelemetry, which would need to be encoded in the schema. Like, I don't want to encode in this schema or have extensibility for, like, your application framework. Like, that's…
Ted Young 00:21:11 Oh, no, I just meant someone else has, like, a library, right? And they need to add internal library or something, and they add instrumentation for that thing, and then they want to add instrumentation config, so they can config that thing, because they've gotten used to that pattern. And… So you're gonna have people outside of our core group having to follow along with whatever our patterns are, I guess is what I'm saying. So maybe part of moving it into this spec is about having some people, including the TC, having at least like, maybe everyone on the TC isn't, like, the biggest expert on, like, JSON schema structure and things like this, but there needs to be some locus where The people who do have those expertise are hanging out somewhere and are getting pinged on these things, and it feels to me like the spec… And the TC slash spec maintainers, however, we're evolving that, seems like the right place for… for that stuff.
And then for the parts of the config that need to live elsewhere to be just attentive about those extension points and how they work.
Jack Berg 00:22:17 Yeah, just a real quick note on, like, you know, configuration properties that may be specific to a very particular library. So, you can have those, you can read those properties as, you know, an author of a configura… as an author of an instrumentation library, but we're not encoding those in the schema. The only things we're going to encode in the schema are things that are common across, you know.
languages, or common across, like, a particular domain, like, so, you know, HTTP, or… but, like, you know, for those… for properties specific to a single library, the idea is you validate the schema on read. So as you're reading those, you're validating that the schema matches your expectations.
Ted Young 00:23:00 I guess, yeah, I'll let Daniel talk, but it feels to me like, like, the spec and having, like, everything you're saying seems to make sense that this should be in the spec to me, and we need to have the TC or spec maintainers, or someone… it's a requirement that there be expertise around how to model this stuff fundamentally, that we don't lose all that expertise that got generated in that config sig, that that doesn't just… evaporate around, like, the design philosophy behind why we modeled everything. To me, that's, like, the important thing to preserve centrally, and then maybe using tooling and things, which we seem to be getting better at as things are evolving with AI to, like, keep Keep other groups in sync with the spec group.
Yeah, let's… spoke wherever we put it, I guess is what I'm noting, so might as well put it in the spec.
That's all I had to say.
Jack Berg 00:23:59 Daniel, can you take us home? Let's cap the conversation at 3 more minutes, so we can hand it over to Florian.
Daniel Dyla (Dynatrace) 00:24:06 Yeah, yeah, I, I had some things that I was gonna say, but most of them were probably unimportant. I think the core is that all of the things you talked about continue to be process and tooling things, which I think can be fixed with process and tooling. I didn't hear anything that's impossible to do.
The most difficult, I think, probably sounds like… Things coming in from semantic conventions.
But… to… I'm not familiar enough with the configuration process. If something changes in semantic conventions, do you then have to go make a PR in the config, or is it automatically pulled over, or is it just referenced?
Jack Berg 00:24:49 It's manual for now, but we want to make it automatic in the future. We want to add tooling for that.
Daniel Dyla (Dynatrace) 00:24:54 Right, and so the change is automatic, or it's just a reference to the semantic conventions in, like, a more federated way?
Jack Berg 00:25:02 Right now, semantic conventions describes its config options in just prose, and so somebody has to do the work to go and model those in the JSON schema of the config.
And so, at some point, we hope to model those config properties, you know, in JSON schema or equivalent in a structured manner over in semantic conventions, and have tooling to automatically bring them in.
Daniel Dyla (Dynatrace) 00:25:25 Yeah, so to me, that sounds like the most difficult problem to solve if you move it over to the specification, but you still have to… you have to solve it in a separate repo also. So, I mean… It… to me, it sounds like it's all process and tooling, and if we want to make that investment, then great, and if we decide it's too big of a lift, and that the advantages of having it be a single repo aren't big enough, then also fine. I don't think that I feel strongly that this must happen. It just struck me as a matter of convenience. And to me, I would say that the way that I would want to make the decision is, like.
long-term, 5 years from now, what would be the most convenient? Because if we're only making lockstep changes for 6 months, and then we expect the configuration to evolve independently, then it doesn't make sense to merge them for that 6-month time period. But if we expect them to evolve together essentially forever, then I think Emerge makes more sense in that case.
Liudmila Molkova 00:26:31 I'm sorry I have to call time, on this, because we… turns out we have quite a few topics. I'm wondering, We… Carlos, how do you feel about talking about context scoped attributes next time, so we have enough time for the profiling?
To share their status.
Carlos Alberto Cortez 00:26:53 I don't mind.
That profiling, you know, provides an update first.
Regarding time, probably can do a summary, 5 minutes instead of 10, as well.
Liudmila Molkova 00:27:04 It deserves 15.
Okay, so maybe we can put it at the end, and then, if we have time, we will go through it, otherwise we will… we will spend enough time on this next, call.
Thank you.
Okay, okay, Eva, do you want to talk about this one? Process context sharing?
Ivo Anjo 00:27:36 Yes, so, kind of a quick update on that one. We've been, talking about this for some of the… in the past meetings, and I… I've been trying to kind of reply to all of the feedback, so I believe the only thing that I have not yet replied to is the… a question of multiple resources, which we discussed in having, kind of a default resource, as it's been done in some of the other, hotel specs.
And so, kind of, so, sorry, I'm getting lost. What I want to say is, like, please give it a look, give us feedback, because I'm happy to cover more feedback and see if we can land this one, so let me know what I can improve on to help lend this one.
Liudmila Molkova 00:28:28 Thank you. Is there any discussion that you want to call out? Any specific people that you would like to take another look?
Ivo Anjo 00:28:37 To be honest, like, I'm not sure who… So we already got a lot of approvals from folks, so I'm not even sure right now who I… who I need to convince next that, that we are good, or get feedback from next, so I think that's part of the question.
Carlos Alberto Cortez 00:28:57 Oh, by the way, Bo, I did review that, and I am just checking that you did answer my… my previous questions. I guess that I… I wanted to make sure that This remains as an optional feature for SIGs that don't want to.
Ivo Anjo 00:29:12 I mean.
Carlos Alberto Cortez 00:29:12 Even though you, as a group, provided actual prototypes for different, languages. But yeah, as long as this stays optional.
I'm happy with, approving this one myself. And thank you so much for answering that.
the question.
Ivo Anjo 00:29:29 Yeah, I think, at least from our side, I think the whole point of having this in the specification is just so that we don't kind of diverge on this, so that if anyone wants to implement it, let's implement this one, and let's agree on a one that everyone that wants to implement, but anyone that, like.
can't implement, or there has, like, some restriction that really doesn't want to implement this, yeah, I think it makes very much sense to keep this optional.
Liudmila Molkova 00:30:04 Cool. Thank you.
Ivo Anjo 00:30:06 Thank you.
Trask Stalnaker 00:30:08 We can skip my topic, I can take it to Slack or… and or the issue.
Liudmila Molkova 00:30:14 And essentially, Maintainer Summit is happening at KubeCon.
Or maintain our meeting topic.
Okay.
Trask Stalnaker 00:30:20 I meant it as, like, normally we have spec Meeting topics here, but it's also technically the maintainer meeting.
Liudmila Molkova 00:30:31 Okay, thank you. Oh, Florian, do… should I… Hand it over to you, who do you want to present?
Florian Lehner 00:30:41 Yes, look nice, I tried to.
So… you should start seeing my desktop, and at the moment, we see… the current agenda. If not, please scream, otherwise I will start.
Liudmila Molkova 00:31:04 Can you please zoom in a little bit?
Florian Lehner 00:31:08 Short, short, sorry.
Liudmila Molkova 00:31:10 Thank you.
Florian Lehner 00:31:13 So, I will keep the format of the profiling sick update as we did see it last week, so there's no fancy slides or this.
I would just go with you about the profiling signal at the current status.
Especially pointing out what is different to the existing signals, like logs, metrics, and traces.
Changes to common parts of the protocol that Will not affect you at the very moment.
Then, what is the part of profiling in the semantic conventions?
what are our guarantees, in particular, looking into PPROF, and then, just briefly mention current implementation, because there are already implementations using hotel, profiling, and the current status where we are. This week was already quite busy, and we are working to keep it busy for KubeCon. So, to start with, if you have any questions, I'm happy to answer anytime. Otherwise, I will have our eye also a little bit on the chat.
To answer it there. The first link, I provided in the Slack.
In the document is… is the link to the profiling signal, I hope the zooming is fine for you.
And, in the profile itself, we have a little bit of overview of all the messages with the profiling signal, and I think every one of you will just notice, hey, that's very, very different, to what we know, from logs, metrics, or traces. The first thing that points out is usually, hey, there is a dictionary on the profile, on the data level, so next to the resource profiles, what you probably know from resource logs, resource, traces, or resource, metrics, there's a profiles dictionary, and this is really important for profiling.
Profiling itself is, we have very… a lot of stuff that is repetitive, so profiling reports, usually stack traces, stack traces in a text format, so you can, Build nice, fancy flame grass, for example, that's the idea.
And, in flame drafts, depending on the depth, you have multiple, you have often the same information, for example.
the file of the source code is the same, or even the function is called, multiple times in the same stack trace because of a recursive call.
just ideas like that. And for that reason, to keep it compact, Profiles is using a dictionary. So instead of, writing 10 times hello world, function, or a function hello world, or a func main.
we just write func main once into Profiles Dictionary, and then point every time in the respective collection into Profiles dictionary. So if we go a little bit into the… into the… into the profile.
It's really like, profiles data, resource profiles, and scope profiles. These are the common parts, from OTEL that you know everywhere, and then we have the profiling-specific parts. I don't want to go into much details into Into much details in… What exactly are the fields within the… Within the respective, messages, like profile, sample, stack, locations, but from the connection, from the diagram, I probably, you probably see the connections, how they are related to each other.
And, yeah, that's the important part. One thing I want to point out is, the dictionary. We don't have just one dictionary, we have multiple dictionaries. And, The most easy one is the string table, so every string is just represented once in the profile, but also mappings, locations, functions, links, and attributes and stacks.
same for stacks, for the same idea. If we see the same stack multiple times, we just store them once, and Reference it, multiple times.
One thing that is special for the, for the… Profile signal is, key value and, key value and unit.
From other signals, you probably know key and value without a unit, but from the profiling side, we see the need that we need to attach some kind of unit information to key and value.
That's the current status. There is a discussion ongoing, and I have linked this later on, in hotel… proto, an issue in Auto Proto, where we want to go, or where… what are possible options going in the future, making this maybe available to others in a backwards compatible way. But yeah, at the moment, it's, it's a profiles message, in the profiles.
Protocol, and, so there's not a one-to-one compatibility, with key, key value, as it's known for the rest of, profiles.
Yes.
Are there questions so far?
I don't see questions, or I don't hear any questions.
I did speak about the protocol, and, especially, Josh, I see your hand.
Josh Suereth 00:37:10 Yeah, I just wanted to… to make sure that we take some time to, like, get people to see some key things here, but the… the attributes part, where you have units, I just want to call out the importance of that. Like, we… we have had, folks ask for units on attributes just across OpenTelemetry, and I think it's, When you have a dictionary, it's a little bit better. And I just want to make sure people are aware of that discussion that's going on, make sure they're aware… we've had people ask to have units on, like, attributes in semantic conventions.
Right? Where we could model it that way. I think this is something for everyone to kind of… think about it a little bit, of, like, you know, how do we get attributes in your UIs? For profiling, we have to have it on the wire for PROF compatibility, which is why it's here. But anyway, a few interesting things. Did you share the benchmark, or, like, the showing how much volume you save with your dictionary table, because I think that's also kind of cool.
Florian Lehner 00:38:08 Yeah, we're coming to this, we're coming to this.
Yeah, next is the… Part of the protocol, or the idea of the next part is the protocol.
That are… is in common, so, you probably recognize, ProtoCommon.
And, we have here the NE value as an example.
And, with… Thanks, Josh, for cutting the release yesterday. There is now a new field. A new field that is only used by profiles, so not available for logs, metrics, and traces.
Because it relies on the existence of a dictionary.
We have, or we introduced, to, any value, string value index, string index, that points to something in the… to the… that points to the dictionary, in the string table in the dictionary, and so we are able to, have multiple any value, and compress them quite efficiently. The same goes to… Keevel you?
Key value? Yes.
Key value, this is also new since, yesterday.
the same idea, instead of having a string multiple… repeated multiple times, we just have a reference to the dictionary and the string table in the dictionary, and use it from there. Same for this field, at the moment, only usable by, profiles, not blocks, metrics, or traces.
And as Josh pointed out, there must be a reason to add these fields in the common part.
And the justification, that's… we have, done extensive tests.
Thanks for… to the people from Datadoc, to name, Felix, and, Felix and, And his team.
They did some, some benchmarking. What's the impact of having these, references in any value and, key reference?
We have here 3 bars. Baseline is basically, basically, at the moment, what profiling does. Profiling, at the moment, before yesterday, was… not compatible, I would say, with OTEL, in the sense that, not all resource attributes were in the… on the resource level, but on the sample level, because, Things change too much, and, if we go… if you move everything to the, to the… from the… from the sample level.
to the resource level, then the profiles, explode, basically. So, here, split by process is, the status. If you move all the resource attributes.
from message sample to resource attributes, and have them accessible like every resource attribute in, in Oter. And these, as you can see, if we make this move from attaching it to sample to resource attributes, be more than double the size of the protocol.
Now, with 733, so the resource attribute dictionary approach, where we used changes in any value, and the changes in key value, key value, that we reference, the… or that we, just have references to repeated strings, we see that we cut roughly, the size of the… of the data in half, and that's… that's really what we are needing. I would try to have it side by side. So.
I hope that's… Fine. So… to summarize it again, on the base… on the baseline is what was done before yesterday, the baseline, having everything, all the necessary, information that is really essential for, having a stack trace information, so is the stack trace related to a container? Is it a process? All this information was all on, all on the sample level, not on the resource level.
And, since the merge yesterday, we are now with 733, having these level, having this information of the resource, level, on the resource profiles level. I hope this makes sense.
Other questions?
I don't see questions.
then I…
Jack Berg 00:43:07 I can ask you a question. So, I guess, maybe this has been mentioned, but just, like.
maybe we could hammer it home. So, right now, there's these index fields.
You know, talk about being exclusively used for the profiling signal.
What… what's the expectation or the likelihood that they, they expand to… to be use… used or recommended in other signals as well?
Florian Lehner 00:43:34 I might be biased on this. I see a high potential and benefit in other signals as well.
I think, especially that we, on the resource attributes level, you see a high repetitive information, that is sent over and over again. And, I think this, is happening on logs, metrics, and, traces as well.
Yeah, but what is missing, logs, metrics, and traces is a dictionary, and I don't have an answer, to be honest, how a dictionary can be done.
For these… signals in a backwards compatible way, because logs, metrics, and traces, do have a different, different guarantees as a stability than profiles. Profiling Sig is aiming for alpha announcement, in KubeCon in around 2 weeks.
And, yeah, logs, metrics and stables… Logs metrics and traces are stable declared, so making a change there is very… it's a different story and needs to be done carefully.
Yeah, I see… I see the benefit there, to summarize it. I hope this helps or answers this.
But I don't know how this can be done, to be honest, at the moment.
Tigran Najaryan 00:45:02 Maybe I can chime in a bit, Jack. We looked into that, right? We were… we looked into the possibility of supporting the dictionary encoding for Other signals for all signals in the same way, and we see difficulties there, particularly in introducing it in a way that is backwards compatible, that doesn't break anything there.
There are… Possible ways, but they are complicated.
So, we decided against doing it now, but we leave the door open.
Or possibly doing that in the future. That's where we stand right now. But because we didn't have an easy and quick way of doing it for all signals.
And we didn't want to block profiling, we said, okay, let's introduce it for profiling now.
And do it in a way that leaves the door open, really, for other signals to audit later. But at the same time, it's done in a way for profiling, such that you can't… It's very difficult to mistakenly try to use it for other signals. So it's essentially profiling only right now, with the possibility of adding other signals in the future, which requires more work and ways to try to find out how do we do that, either in a non-breaking way for for the current OTLP, or maybe for the next version of OTLP.
Florian Lehner 00:46:33 Thank you.
Yeah, maybe I can share this a little bit, and that's also maybe interesting to know. Otecollector and AutoCollector contribute using a lot of, making a lot of use of resource attributes in multiple ways. Thinking about the filter processor, or any other processor that is… that is handling A signal. For prose files… it would have been a, I would say, really a mess if everything had to need to be touched to make support of these new fields. So what profiling is doing, if a signal comes in and gets un-martialed or marshaled to get out, these, these new fields, string value, string index, is happening at, is happening at the marshall and unmarshalling. So, existing, components, like, filter processor, or other processor, or other, contribute, components of OTEL, will not notice this difference, and I think that's really important to know.
there doesn't need to be a change, for other component… components in Autel to be compliant with this. So they just work on profiles, resource attributes, just like working on, logs, resource attributes. So, there's no difference for… for the different, components, as we do a… In a transparent way when we, when we use P data, or martial and un-martial into P data.
That's… that's… that's, I think, the trick that helped us, quite… Quite a lot going forward.
any other questions?
As you can see, I have linked, or I go back always into the agenda, so if you say, hey, I'm talking too fast, or you cannot follow, we can go just in there. You can go back to the agenda and click on these links as well.
making use of profiles comes also with a lot of changes in semantic conventions. I just have here the general overview of the profiles.
At the moment, we can do, or we can differentiate stack traces from a lot of different languages, not only native languages, but also interpreted languages, which is really nice. I'm really happy about this.
And, we also have, so we… we just, barely touched.
the information that we are PProf compatible in a forward way, meaning if you have PProf, transform it into OTLP profiles and transform it back, we promise that you will not lose data, and that's totally fine.
For this, we have, specific sections just for, PProf attributes that are not used otherwise.
Yeah, that's… that's working fine, I would say. That is really nice. So, thanks from everyone work… helping, getting the semantic convention, not all the semantic conventions, but also our specifications around this, working.
Prof compatibility, same link again, will not open. At the moment, I'm, I'm… there are at least 3 well-known, implementations of the OTLP Profiles protocol, so EMPF Profiler.
EBPath profiler who doesn't know, is a little bit different than other OTEL components. It should use, should be deployed as a daemon set, you can deploy the OTA collector with the profiling receiver as a daemon set, and then you get for all the containers and all the information. This is one implementation.
Then we have… the PPROF receiver in hotel, Contra. Yeah, so, if you have any PPROF format, you can just, scrap it here. This works also, just fine.
And last but not least, what I'm really happy about is, about it's not an hotel project.
But, Java is still a major, major, topic in the industry and important for everyone. So, if you're using async Profiler, in Java, this is also… or async Profiler has the capability to also output, hotel, OTLP profile. So, I'm really happy about this work, and, also, thanks to people working on this.
Last but not least, the current status.
Yesterday, just, thanking… thanks to, Josh, we have a release, a new release from the OTLP protot, so, today we are very busy, making the changes, or bringing the changes in, into the OTL collector, because there were some breaking changes, for, for profiles.
That need to be some attention, and, this will… probably settle today, tomorrow, in the OTEC Collector, and we are aiming for the alpha, announcement for KubeCon. So, Felix, Felix Geisendorfer from Datadoc and I have a presentation at KubeCon 22 weeks, basically. If you are there, we are happy to welcome you.
You will probably hear a lot of repeating stuff from today, but also say hi.
The goal is, and, I wanted to ask this group as, if everyone is, is everyone, would be fine, bringing profiling to an alpha state, so making this announcement.
this would be the ask to the group, basically. And last but not least, this was the discussion we just touched.
at the beginning with Josh, key value and unit, there is an ongoing discussion, how can we make use, not only inside of, inside of, profiles, but also make use in other signals in the backwards compatibility way?
This will result in a change in some way, how is not defined yet. This is… but this… this is the work we are currently working on.
For profiles, this should not be a blocker. This should, be fine, regardless what is the outcome of this, this discussion. But this is what we are… will go next to.
And, just repeating what, Evo said just a few minutes, or just before I started talking.
He was doing a lot of great work with, help from his teammates at Datadoc, about, context or cross-information sharing.
I think… maybe also just a personal few, correlating signals is really key, important, and so sharing, information across all components is really important. That's why I think the work IVU is doing, is really important, and will bring all a little bit more together, and, make it easier to, To correlate this information.
Yes.
So, this concludes… The overview of the profiling signal.
Do you have questions?
I didn't follow the chat closely, as I was speaking quite a lot.
Liudmila Molkova 00:55:06 I have a question, is there… a way to try it all out. Like, if it's an alpha state, we should have a prototype, at least, and some application that can report profiling, and maybe, there are some backups that could support it.
Is… is it, is there something like this?
Florian Lehner 00:55:27 Yes, so you can use already, OpenTelemetry EVPF Profiler. We now have a target, I need to zoom out a little bit.
we have a new target that will command auto-collector EVPF profiler. So, if you just run this on your system, and send, the OTLB data somewhere, already works.
Command OTC Collector EVPath Profiler is not intended for deployment into, into production. This is just for, for development purposes, but if you want to run it, it's already there. Then we have, OpenT Collector Release.
So, if you are… on the release side, we have already eBPath Profiler on collector release, so if you want to give this a shot, this already also works.
whatever you prefer, so it's… it's already working fine with the collector, and the idea is really, making it possible with the collector. I know there's work going on on the Hart of… Helm chart site, eBPF Profiler and… probably all other eBPF projects are making heavy use of extended privileges, so… That's the difference to the SDK approach. You need a little bit more insights into the system, so, host PIT is the most famous information usually that needs to be set, an element that needs to be set in, hand charts, so there's, work going on. And OTA collector, auto collector eBPF profile, like.
really important to know if you want to give it a try already. Profiles is in the OTEC Collector behind the feature flag, so If you, use this old tech collector eBPF profiler, you need to start it with, feature flag support, profiles… I have to look it up exactly, I don't have it in mind, I usually just… Browse my bash history. but there's a feature… feature gate flag that you need to do, need to use if you give this a try.
Hope this helps.
Liudmila Molkova 00:57:43 Yeah, thank you. Would it be able… do you have a demo at KubeCon that people can try?
Florian Lehner 00:57:48 Kubecon will be there, yes.
Liudmila Molkova 00:57:51 Awesome, thank you.
Florian Lehner 00:57:56 Other questions?
Again, thanks, Josh from Tigrant for the help. I think they did great work helping us as profiling, Most of the profiling sick people were not part of OTEL before joining Profiling, so, thanks to both of them doing great work guiding us and providing all this feedback and giving us the right notes and hints where to look at and where to go. That was really helpful, thanks a lot.
Otherwise, I will stop sharing my screen.
Jack Berg 00:58:34 Thanks so much for your time today and giving this presentation.
Florian Lehner 00:58:41 I haven't done so long.
Josh Suereth 00:58:42 tries profiling after this. Please do. I've, I personally will, because I have had a need to profile something, and I really want to try it.
Florian Lehner 00:58:51 Yes, please, please go on.
Peace Coron, feedback has always become, I can at least speak for the… for the Elastic side, so, it's running more than just in a small development environment, so it scales. That's really fun, and, yeah, that's… Love it.
Josh Suereth 00:59:18 Thank you for all the hard work, and to the whole profiling SIG, like, this is… this is great to see.
Florian Lehner 00:59:23 Yeah, important to note that, I'm just speaking here alone, but, that's, that's a multi-company effort. It's not just, one Elastic, or Datadog, or… and there are so many people involved, and, thanks to everyone that's… that's really, really spent… we have… I don't remember when we joined Auto, but it's more than… A few weeks.
Liudmila Molkova 00:59:51 Definitely more than a few weeks, and thanks a lot for bringing it along. Great presentation, by the way.
Florian Lehner 00:59:59 Thank you.
Liudmila Molkova 01:00:02 Cool, so we have 2 minutes left, and let's end on this awesome note, and yay to Profiler!
Jack Berg 01:00:12 See you next time, everyone. Bye.
Florian Lehner 01:00:13 Thank you.
Ivo Anjo 01:00:14 Thanks, everyone.
Liudmila Molkova 01:00:15 Thanks.
