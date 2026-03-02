SIG: Semantic Convention SIG
Date: 2025-09-08
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/6CKv_6oPkpf-XS_fdMlEvPb87lYykcLk2HD-G3SVb_DEzquhqcESP7eVZAtK3NZq.5zOClfbu8Y469Q_Q
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:45 Hello, hi everyone.
**Christophe Kamphaus** 02:50 Hello.
**Bertrand (MetricsHub)** 02:52 about hype.
**Florian Lehner** 02:53 Bonjour.
**Liudmila Molkova** 02:54 Okay, I think Josh will be 30 minutes late, and I'll need to drop off at 84… sorry, in 45 minutes.
Let's get started, though.
Try to drive, and for the last 15 minutes, maybe somebody will take over?
Let me share my screen…
**Trask** 03:23 I'm currently, experiencing internet problems, so I'm on my phone, sorry.
**Liudmila Molkova** 03:29 Oh.
**Trask** 03:30 I am sorry.
**Liudmila Molkova** 03:32 But maybe Josh will take over once he joins.
**Trask** 03:36 Oh, yes.
**Liudmila Molkova** 03:42 Okay, so let's,
If you have any topics, please add them to the agenda. It seems we're all light so far.
I might have a topic if we have time.
Let's start with the… Courage board.
We have quite a few… Oh.
Nothing that's ready to be merged, everything is merged, wonderful.
There is a pull request that needs more approval. I approved,
So if somebody… oh, it's also ready to be merged, and there is one discussion.
**Joao G. (Dynatrace)** 04:25 Yeah.
the discussion, but I looked at the latest… the state that I looked, I think this is fine, but I saw that you asked for them to… if the…
discussions can be resolved. Not sure why it didn't be resolved yet, but I looked and I think it's all good, so…
**Liudmila Molkova** 04:46 Okay, so…
**Joao G. (Dynatrace)** 04:47 I was unsure if I should resolve the conversation myself, or if they want to wait, do something. The author didn't come back, I think, in the latest comments.
**Liudmila Molkova** 04:57 Right, I think the question is, whether…
Let's say if the parameter name starts with a special character.
Whether the special character is included, I think that the current… Text introduced there.
Suggest to take it as is.
So, we can always improve examples if they're not clear.
Later.
So, my intention is to then probably resolve and let it be merged, and then…
**Joao G. (Dynatrace)** 05:36 Yeah, I think there's not even the character anymore in the examples.
I think they removed it.
**Liudmila Molkova** 05:43 Oh, it's never been there.
**Joao G. (Dynatrace)** 05:45 Okay, the discussion was if we're supposed to add, okay, got it.
Yeah, I think it's fine. I didn't want to close it because,
They didn't come back, but I guess… Should be fining.
**Liudmila Molkova** 06:23 Alright, so I'm going to merge it…
And, let's spend a few more minutes looking at what else we have here.
There are a bunch of blocked pull requests.
I don't know, what should we do with them? James, if you can pick one or two to talk about, we can talk about it.
**James Thompson** 06:55 But… Nope.
Nothing's urgent to look at in them. Like, the main thing is, how do we progress to adding the DB systems?
**Liudmila Molkova** 07:09 We don't.
So, the problem with DB systems, that adding a constant has very little value.
And unless somebody else does a research.
to actually look into this database, and also document how this conventions apply to this database, and also working on the instrumentation prototypes. That's quite a bit of work, and adding systems of just the constants, I…
I don't see a value in this.
**James Thompson** 07:42 So, this one is actually already used by the Ruby implementation that's been released.
**Liudmila Molkova** 07:48 Does…
First, this needs to be documented fully, and it needs to be maybe implemented somewhere else, but it needs to be documented fully. I'm not suggesting that you should document this. I'm suggesting to work on impactful things that actually move something forward.
**Trask** 08:09 For the database constants, do… I mean, it is an open enum, Right, so, like, it…
I think it… I mean, it's okay for instrumentations to…
Used, you know, to have their… to be using
Additional constants that aren't in this list.
**James Thompson** 08:33 But what we just had is the .NET entity framework provider drop half a dozen
DB providers, because they weren't in the list, for example.
Right.
Because they wanted to go to a stable instrumentation.
And because that they're not listed in here, they've actually removed support for those database providers, because they're not listed.
**Liudmila Molkova** 08:58 So it's okay to release them as experimental.
**James Thompson** 09:03 But they're not even defined in the list here, so…
**Liudmila Molkova** 09:08 That's fine.
**James Thompson** 09:10 Because the .NET…
the .NET contribute actually went and deleted them out of the codebase, because they weren't in the list.
**Liudmila Molkova** 09:18 They even… they didn't need to do this. They could keep releasing them as experimental.
**Trask** 09:26 Yeah, that's what we are planning to do in Java.
**James Thompson** 09:31 Yeah.
Okay, Chris. Yeah, because that's part of the reason why I put some of the issues in, is because the .NET have gone and removed them.
Yeah.
**Liudmila Molkova** 09:45 Okay, I'm going to create an issue here in semantic conventions that we document the strategy for the system constants, that we are
Discouraging getting constants one by one, and that we're recommending instrumentations, or especially external ones.
to define
To either define the whole conventions here, or, they, they are free to release, and work with, for other databases.
At least with experimental status.
**James Thompson** 10:16 Nope.
But in the case of the .NET, they're using entity framework.
Alright, and because they wanted to stabilize it, the Entity Framework Library works across 10, 12, 14 different providers.
That's where the part of the problem came in as well.
**Liudmila Molkova** 11:30 They can, I think Java uses, enable experimental attributes, or, there could be some other experimental feature flag that allows them to only enable this instrumentation when this flag is enabled. They could solve it.
**Trask** 11:46 Yeah, it's the same problem, James, for JDBC instrumentation.
**James Thompson** 11:53 Nope.
**Liudmila Molkova** 12:10 Okay, so, thank you, great discussion. Let's move on to the agenda we have just two topics there.
Hi, Mike, Meg, Lauren and Bent.
Okay, so let's get started. Florian, do you want to talk about profiling?
**Florian Lehner** 12:36 Yes, hi everyone.
I want to talk about the 25…
to, PR for the semantic conventions.
The idea is to add, PPROF-specific, attributes to semantic conventions. These, PPROF-specific attributes are…
necessary to provide, conversion between PPROF for profiling and hotel profiling, and, yeah, that's…
Thus, we want to have a feedback. There was a question in the PR, why not using the PProf namespaces instead of ProfileProf?
I answered, but didn't get any
feedback on this, so, we went with the profile, PROF, namespace, because it's really just, converting these protocols from one to the other, and,
we don't see the point that anyone else will ever be able to use the PPROF attributes in some other cases, like logs, metrics, or traces, as these attributes are one-to-one mappings with the PPROF protocol.
And, yeah.
**Liudmila Molkova** 13:55 There is no correlation between the prefix and the place where the attributes are used. So, all I'm saying is that it's essentially redundant. When you say PROF, you mean profile.
**Trask** 14:10 Yeah, so we don't… we don't have, like, a span, you know, a traces, top-level namespace, and a metrics top-level namespace, and…
We just try to, like, as long as it's unique.
And uniquely describes. Then the shorter the better.
**Florian Lehner** 14:29 Okay, so it doesn't matter, does this attribute will never be able to be used with logs, metrics or tracers?
It's just, for conversion, converting between… protocol types.
**Liudmila Molkova** 14:47 Yeah, it doesn't matter, and it's hard to imagine that somebody would accidentally use PPROF prefix for something else.
**Florian Lehner** 14:55 Yeah, okay, cool, then I will update the PR and hope for progress. I think for us, as profiling, it's significant that we can show that there is a successful conversion between hotel profiling and PTROF.
And so… Yeah, hope to bring this firm. Thanks.
**Liudmila Molkova** 15:16 Yeah, thanks.
So one thing here to pay attention to, you probably are the co-owners for the profile, holder.
And you probably will need to add yourself as code owners for the APPROF folder.
**Florian Lehner** 15:45 I will try to do the same.
**Liudmila Molkova** 15:47 Yeah, thank you.
Cool, anything else? I think that there was a… I had a comment on…
Is there some doc that describes the mapping, this one?
Can we link it?
**Florian Lehner** 16:13 Not really. At the moment, there is no SDK for, hotel profiling, and no API for hotel profiling, so it's hard to map something to it. That's why I added this in the general overview for profiles, that, there are compatibility with PProf.
But it's not stated somewhere else.
**Liudmila Molkova** 16:36 I mean, you probably have some strategy in mind on the full mapping.
And I'm not asking for implementation, just for the document that describes it. If we don't have it, I mean, that is what it is, but if we have it, it would be useful to link
Some documentation on this.
**Florian Lehner** 16:54 I think that does not exist something like this at the moment. Otherwise, both protocols can be mapped.
Quite easily one-to-one.
There are some nuances, but, generally, quite… One-to-one met bubble.
**Liudmila Molkova** 17:13 Yeah, you're probably talking as an expert, and you know that my question doesn't make sense, but people might have this question in general.
**Florian Lehner** 17:22 No, man.
**Liudmila Molkova** 17:23 Correct other people to implement it.
**Florian Lehner** 17:25 Yep, makes sense.
**Liudmila Molkova** 17:28 Okay, so then, it seems it's the last comment for me. If folks… if anybody else wants to take a look, please go ahead.
Other than that, once the changes are done, I'm going to approve.
**Florian Lehner** 17:44 Cool, thanks.
**Liudmila Molkova** 17:52 Okay, should we move on to the next topic?
CICD logs.
**Christophe Kamphaus** 18:01 Hi, everyone!
I wanted to get started defining semantic conventions for logs of CICD systems.
And I took a look at CSSAMConf.
I could not really find any area where…
There were semantic conventions defined for logs beyond the one for general log conventions.
And from previous discussions here, My understanding was that
We cannot distinguish between different logs, so we have only defined semantic conventions for events.
**Liudmila Molkova** 18:39 Right.
**Christophe Kamphaus** 18:40 My understanding here, right?
**Liudmila Molkova** 18:43 Yeah, so since logs don't have a name, they are unidentifiable, and you cannot define the structure.
**Christophe Kamphaus** 18:53 Okay, so we would have to define events instead.
**Liudmila Molkova** 18:58 Right, but events are logs.
just blogs with a name. So, you can call it logs, you can call it events, event terminology would apply to semantic conventions.
**Christophe Kamphaus** 19:11 Okay, so, as long as we say the event has named CICDELog, Something like that.
We could define some comfort.
**Liudmila Molkova** 19:24 Could you maybe, guide us, and what are the…
logs, because CICD log as event might not make much sense.
Y-you probably would be more specific than that.
**Christophe Kamphaus** 19:37 Yeah, so, we would require that it's associated to a pipeline run.
And of course, associate other resources for… CICD.
It's basically the build logs that we,
Want to say, the system has emitted these logs, and we want to be able to
Links them to a specific build.
**Liudmila Molkova** 20:05 So these are the logs. Go ahead.
**Christophe Kamphaus** 20:07 Yeah, and we want to be able to distinguish, has it been,
is it really the build logs of any process that is executed as part of the build? Like, for example.
a Gradle build, or… a GoBuild.
a test, logs.
Or is it from the system itself, where it says, provisioning worker, or something like that?
**Liudmila Molkova** 20:32 Oh, I see, so the CICD instrumentation is not the source of data.
for the slogs, they were coming from somewhere else.
**Christophe Kamphaus** 20:43 Yeah, usually it's the standard out or standard error of any process that is launched as part of the build.
**Liudmila Molkova** 20:53 And the goal of defining the conventions is to…
say which entities they should be associated with, or augment these logs with some CICD information.
**Christophe Kamphaus** 21:08 Yeah, I think so. I think at least we should be able to say that
The resources of CICD conventions should be associated to these events.
**Liudmila Molkova** 21:21 I don't think we should define conventions for the logs themselves.
We should document, probably, that instrumentations would augment this.
Was… associated them as entities, but…
What's the benefit of defining conventions for something that could be anything?
**James Thompson** 21:44 Does this tie into the discussion we're having about attribute groups, where I think what's being sought is the ability to define a group of attributes which can be used on logs.
Right? Which is similar to what we have for feature flags, for example.
Right?
Christoph, is that what you're thinking? Is you want to be able to say.
These logs will come with these… these sets of attributes.
**Christophe Kamphaus** 22:12 Yes.
**James Thompson** 22:13 So this group of attributes should appear on logs.
I think that's what you're looking for.
**Christophe Kamphaus** 22:19 Or basically just say, We could have…
Just regular logs where these entities are associated to them.
Would it make sense to say it like that?
**Liudmila Molkova** 22:33 I would start there.
Right, boom.
You cannot define semantic conventions for logs, and artificially saying that the log… that the event name should be something?
It… it defeats the purpose of the event. You should… Have the constant structure.
Which is meaningful.
**James Thompson** 22:57 You know, what I'm thinking about is, do we define just a group of attributes, right?
Alright? And say… CICD logs It's suggested to have these group of attributes associated with it.
**Liudmila Molkova** 23:14 If I understand Christoph correctly, he's interested in entities, those are… defined things.
And yeah, I think attribute groups are also meaningful here, but, the first ask is association with entities.
**Christophe Kamphaus** 23:31 And as I understand it, in SAMConf, we can apply any entity as long as it's valid.
So we would not need to, say it explicitly.
But here I was wondering if we want to make CICD some conf…
**Liudmila Molkova** 23:48 As discoverable for regular people, or…
**Christophe Kamphaus** 23:52 Instrumentation implementers as possible.
We might want to adjust states that for CICD build logs, or adjust logs in CICD, you might want to associate
the applicable CICD resource conventions.
**Liudmila Molkova** 24:10 Yeah, and I think you already have it documented for other signals, right? For all signals.
You can definitely have an additional page for the logs, where you… Explain how to report.
Logs captured during pipeline run, and add stuff on top of it.
**Christophe Kamphaus** 24:33 Okay, yeah, I think it should be easy to just describe that in a short paragraph.
Okay.
**Liudmila Molkova** 24:46 Yeah.
**Christophe Kamphaus** 24:47 I'll prepare a PR for that.
**Liudmila Molkova** 24:51 Thank you.
Alexandra, do you want to talk about, device namespace.
**Alexandra Konrad @Elastic Security** 25:19 Should be a quick question, probably. So,
As also, for reference, the device.
I put here in the chat. For everyone, so in our description of device, it's pretty generic, just about the device, but if you look into, let's say, examples or, notes.
It looks like device is about, mobile browsers, or, oh, sorry, mobile phones,
And, we at Elastic, we wanted to use… so, like, some of our engineers came back to me with a question if they could… could use the device, like, in generic, as a generic device, for example, I don't know, for any device, yeah? And they were…
A bit, worried about those notes that had links to specific mobile phones, information.
So my question was, because I don't know the history, yeah, of creating, is the device a generic one, or was it maybe in the beginning used for…
Some specific, For specific use cases, but we could generalize it,
Because we don't need to create a new one, yeah? We could just maybe remove those notes or update them to be a generic one, and
Yeah, remove this uncertainty about, what is device then.
Because I could create a PR and, like, remove it, but I wasn't sure, like, maybe I'm missing here something.
**Trask Stalnaker** 27:13 I'd recommend… well, we've got Daniel here. I was gonna recommend, discussing with the,
What is the group?
It's called, now.
Browser SIG, mobile, client instrumentation.
Because devices still… would still fall under client instrumentation, right? Even generic Devices.
**Daniel Dyla (Dynatrace)** 27:45 Yes, I would expect so.
**Liudmila Molkova** 27:52 Would we need a different, namespace for, let's say, in the data center?
My computer is also a device, does it make sense?
**James Thompson** 28:03 But we also already have the hardware namespace as well, where we have an enclosure, which is… it can be a switch, it can be…
It provides examples there of switches, for example.
So, that's my question is, where do we draw the line between what's hardware and what's a device?
**Liudmila Molkova** 28:22 Right, because…
**James Thompson** 28:24 That's also vague as well.
**Trask Stalnaker** 28:30 Alexandra, could you describe the use case a little bit more that you're wanting to address?
**Alexandra Konrad @Elastic Security** 28:38 Yeah, in our case, we just want to describe the device where some security-related, events has happened, and, we need to describe, like,
They wanted to add more fields because, they need not only some names and manufacturer, but a bit more, and therefore, they asked, like.
can we update? Because we have the same in the ECS device, and it was ported from, OpenTelemetry to the ECS,
And we could update the ECS as well, but they were hesitant to do so because of, this limitation from OpenTelemetry side.
So yeah, just to describe, let's say,
Any, let's say, computer or any other mobile as well, but it should be any device, so to say.
It could be also some errors, maybe, I don't know…
hard to say right now, because I wasn't, like, the one who, who raised that question, but, the people came to me because they didn't know what to do, if they could use the device for their needs or not.
**Trask Stalnaker** 30:12 What about, as James suggested, the hardware namespace? Does that fit what… You're looking for?
**Alexandra Konrad @Elastic Security** 30:22 Then, I think we have a question about the difference, because device is a pretty generic name, and if you look into description, they are also all generic. The only… you only see in notes that it's about,
mobile, yeah, devices. So that's why I wasn't sure if the notes, they just came from that specific use case where we used them in the beginning, and we should maybe remove it, because device for me is also a pretty generic one. It's not mobile devices, the namespace, but just a device.
maybe hardware would be also fine, but I think that, we also still need to answer that question.
How to distinguish between them for anyone who would like to use it.
**Trask Stalnaker** 31:21 Yeah, it would be interesting to know if the client instrumentation SIG is…
Or even planning to use the device namespace?
Because, yeah, I agree, it's, at least in my terminology, which I…
Totally understand is not everybody's, device, to me, means,
not, like, a data center or something, it means, like, mobile or something that you deploy, you know, on the edge that, you know, can move around, something like that. But that's very vague, and I don't know if that's even…
That…
**Daniel Dyla (Dynatrace)** 32:05 See?
**Trask Stalnaker** 32:05 Would fall under the client instrumentation.
is kind of what I think of it as.
But I wonder if they're even…
Planning to use that, or using that, or if we can…
Just remove it and avoid that confusion, and use hardware namespace for
Hardware, like, if you really need hardware information.
**Alexandra Konrad @Elastic Security** 32:38 I don't know, background is also here, maybe you could add something from your experience?
of the hardware.
So I just also looked into our PR inside Elastic. We need the devices just for device tracking, inventory management, and security monitoring for the things happening on those devices.
**James Thompson** 33:14 So, it's also… I'm just remembering now, the device namespace is used for events.
for app launching.
Currently.
Apps life cycle.
Alright, so that's one scenario where it actually is implemented.
**Liudmila Molkova** 33:36 It's interesting, they don't use attributes, but they use device.
As a prefix for the event name.
**James Thompson** 33:45 Yeah.
**Liudmila Molkova** 33:51 So, it sounds like we need to talk to the client instrumentation.
And figure out what are their plans and thoughts on the device.
**Alexandra Konrad @Elastic Security** 34:10 Okay, so it's not an easy question after all.
**Trask Stalnaker** 34:13 No, I don't…
**Alexandra Konrad @Elastic Security** 34:14 I thought it's like, we could make it more generalized and not related to the mobile one.
But yeah, okay.
**Trask Stalnaker** 34:28 Yeah, maybe you could open an issue, kind of…
Just to kick off the discussion.
**Alexandra Konrad @Elastic Security** 34:35 Yeah, I did, I did, I posted it here.
**Trask Stalnaker** 34:40 Thanks.
**Liudmila Molkova** 34:42 And do we still have clients here? Do they have a role, or do they… how do they work?
**Trask Stalnaker** 34:51 Daniel, are, is the client SIG still meeting, or has that been folded and the browser SIG has replaced it?
**Daniel Dyla (Dynatrace)** 35:00 I believe that the client SIG is still meeting separately. I'm only joining the browser SIG, but I am…
like, 80% confident that the client's SIG is still meeting.
**Trask Stalnaker** 35:14 Okay, that was my impression also, thanks.
**Liudmila Molkova** 35:30 Okay, there is just one more item on the agenda, and I would actually need to drop off in 10 minutes.
So, I can… I'd like to start showing what we…
our thinking with, schema V2.
And… It's weird, but you folks would continue the discussion after I drop off.
And I would need somebody to take over the sharing,
Okay, so give me one second that I will prepare.
**Trask Stalnaker** 36:22 Sorry, still troubleshooting local internet problems, so I'm still on my phone.
**Liudmila Molkova** 36:30 Bye.
**Trask Stalnaker** 36:32 Josh is here, though, hopefully.
**Liudmila Molkova** 36:35 Hi, Josh!
**Josh Suereth** 36:36 Yeah, sorry I'm late. I can, I can share when you're done. No problem.
**Liudmila Molkova** 36:40 Things.
So there are parts of this PR which, which of the commit, which are questionable, and we don't have a consensus on.
there are parts that we… we do have a consensus on, so I will explain which or which,
And I will try not to get you confused.
Okay, so, the schema V2…
Let me scroll down to HTTP conventions, and… Let's look here.
So, ignore attribute group for a second. This is where we don't have a consensus. So, what I want to show you is this friend.
So remember how we represented metrics?
And, schema V1.
Let's actually open exactly the same metric.
Okay.
Here we go.
So what do we have here? We have an AD, right? We have a type, I have a metric name.
We have extense, the…
There are a couple of things here. First, we always mix ID and metric name.
Everywhere we go. Second, we kind of have the same structure for all signals.
And, as a result, we have some weird problems with,
terminology, and also on the implementation side, it kind of looks ugly. Also, on the resolution side, you kind of need to first understand what you're dealing with, and then you apply certain properties.
Okay, so how does it look in schema V2?
We only have metric name here.
And this thing actually aligns with the Prata, its name on the Prata.
If you look into attributes, you… which we will do in a second, you will see key here, which aligns with the product.
So the principle, we identify these things in the same way as they are identified on the product.
Span is a caveat.
We'll fix it over the time, but yeah.
This is not agreed upon, I'm just showing it because I didn't prepare a separate example, but essentially there will be some way to associate attributes with a metric. You can definitely do this.
But maybe we can… we can do better, and don't repeat ourselves.
Okay, one more thing I wanted to show the registry, how registry looks like.
Okay, registry, it's just one
set of attributes? Well, you can have as many as you want, right? You can declare attributes
Multiple times in multiple groups, but this grouping is meaningless. Like, it's just the way to break things down into multiple files, if you want.
Here we just list attributes, and you can see the attribute has key.
The rest is pretty much the same as, what we have today.
If we look into spans, the spans are fun. Okay, so…
For the spans, we are using type, which does not exist on the Prada.
But I hope it will at some point.
That says, okay, I'm this span. This, like, the event name or metric name, it uniquely identifies the span structure.
And it also has a kind, and all the things that we like so far. Also, it has a section for name. Over time, it will get more structured, hopefully. For now, we only support a freeform text saying how to, populate the name.
Yeah, and that's essentially it for the part We agreed upon.
I would love to hear any feedback or thoughts, if anybody has them.
Okay.
So now… to the part that, I'm actively seeking feedback on.
The part that's in the prototype.
stage.
Okay, so what we see here, let's actually look into our… Existing stuff.
So, we have a bunch of common, today. We have some common attribute groups, we have some definitions for, let's say.
Server address. It's a bunch of things that we specify for server address that's specific to HTTP.
Even more precise, HTTP client and HTTP server.
And, when we define conventions, especially those that apply to multiple systems, like database or messaging, or gen AI, whatever.
It's useful to… Document some attribute once, And… or more than one.
and then reuse it in all the conventions that are relevant, right? So…
Sql Server uses the same definition of
database query text as MySQL. We should not repeat ourselves, but the… there could be variations.
Okay, so, today we use attribute groups for this. So we have an attribute group.
One attribute group can extend another one, and you can extend this attribute group in another signal, which actually means just bring the attributes from that group, nothing else.
But it's very weird to be able to extend metric in your span. It does not make much sense.
Okay, so, the… how can we,
apply this to the schema V2.
The problem we have there is that when we define
HTTP client spend, right? We still need to…
include certain definitions from, common HTTP thing. And, approach…
I'm proposing, is that we still have common groups. We define attribute groups. They are…
internal. Like, you can reshuffle them, you can do whatever with them, they would not even appear in the results schema. So this is the internal implementation detail.
of the HTTP spec, And,
We, can include multiple of them.
Here. They don't have any intersection, like, you cannot include the same attribute in multiple groups, there is no conflict resolution this way, but you can refine
The attributes included in this group.
Here, when you define the span.
I want to stop here. I want to hear your thoughts. I know Josh has some, concerns with this, and I.
**Josh Suereth** 44:29 Super excited to find a better way.
So, you, you need to leave, I think, in 7 seconds.
So, I…
**Liudmila Molkova** 44:36 I can hear one thought, and I will listen for recording.
**Josh Suereth** 44:39 I think… so, my concerns are not about the addition of groups. I think, actually, we need groups, absolutely. Like, I have no problem with groups themselves. What I think we need to talk about is the specifically where sampling relevant shows up.
and then how to, like, how to just name something that's not public versus something that is, so it's clear to people, right? So, my concern is not necessarily about aggregating and grouping, because I think we absolutely need that, and I think this proposal's awesome.
up to the sampling-relevant part, where we had some discussions. What you're doing here, I think, makes a lot of sense with the sampling relevant, but also…
I don't think you like it as much as what it could be if we had better reuse, and neither do I. And I think we have to talk about how to make sampling relevant feel better.
In the… in V2. That's actually… so, like, my focus is more about when we define attribute groups, right, how do I make them safe so default inclusion doesn't accidentally pull in problems?
And sampling relevant is my biggest concern overall with V2. How are we gonna address that to make sure I can't screw it up, it does the right thing, and if I reuse stuff, it's accurate and fine, right? It's only relevant to spans, it's not relevant to anything else. That's my… that's my main… so when it comes to contention on this, it's not about having a group.
It's about how to make sure groups are safe, and I think that's the subtle difference that we needed to talk through. But overall.
I think we should have groups. I think having private by default and figuring out which ones we make public.
Absolutely a fan of.
But let's figure out how to make this
Make it so that if people naively just write stuff, they don't shoot themselves in the foot.
That's my main goal.
And I think that's yours as well, we just aren't sure how to deal with sampling ref together.
**Liudmila Molkova** 46:28 Okay, well, yeah, that's a useful context. I need to drop now. I would love to hear more thoughts from people who write semantic conventions, and I'll…
probably ping you more to discuss stuff. Thanks a lot, and see you later.
**Josh Suereth** 46:44 Okay. I'm gonna share notes now, since Lyudmila has to leave, and we will,
Oh, man. Come on, computer. And I will write down… I'm curious what folks think, if there's any, any, thoughts, quick. It looks like we have one more topic.
But I just want to open up, if anyone has any feedback right now that they'd like to add after the demo, we'll record it, and we can share it later with the, tooling sig on Wednesday.
Okay, cool. If you're curious about Schema V2 or any of the things, there's a few bugs, we'll add them there. You can take a look at the current state and progress of what's happening. Ludmila's demo, by the way, you can already start to try to use today, if you wanted to. There's some support in Weaver.
Alright, cool. James, do you want to, talk about pull request 2422?
**James Thompson** 47:46 Yep. So, I don't want to discuss the content, I just want to discuss how information's being presented. So, can you go to the…
Entities. They're always entities.
**Josh Suereth** 48:00 the OS entity.
**James Thompson** 48:02 Yep.
And bring up the pretty view.
Alright, so we have a lot of information here that's being sourced from a couple of locations.
Okay, alright, so we're describing where each of the information is coming from.
Okay?
Traditionally, what we've heard Is… we've put a note in saying this comes from here, this comes from here.
But as you can see here, we have a lot of information coming in.
Alright, so if you scroll down… As you can see, there's…
I think there's 9 different notes?
Right? Right.
And it's very fractured if you're looking at it, right? Because…
for me, I find it fractured. So, an idea I had was, do we summarize it in a single table saying, sourcing values, and have that as a annotation for documentation?
Right?
So it's not code generation, it's… so if you scroll down further.
Alright, you can see I've summarized, there's one table sourcing attribute values. You can see what attribute it is.
which implementation is it for Linux, and where you can get it from.
So you have a single gla…
Single table to see sourcing information.
Or do we stick with the notes approach?
**Josh Suereth** 49:38 It's… it's a good question. I mean, So, I…
the real thing that I'd like to see…
if I think about this a little bit, is we talked about description examples. You almost want a nested table up here.
Right? I mean, the main problem with notes, the reason why we throw it down further is we're dealing with Markdown, and having nested tables is not possible, or easy.
**James Thompson** 50:05 Me too.
**Josh Suereth** 50:06 And what you're saying is if we can consolidate the information, put it in one place, it's better. I agree.
this… This is kind of where the information is and lives, but we can't really, like.
Put it there, you know?
**James Thompson** 50:21 Yeah. Practically.
**Josh Suereth** 50:23 So…
I'm not… I mean, I'll let other people discuss. It's not clear to me that this makes it more obvious what's going on.
I do think we probably want to call attention to notes in this table, so people pay more attention. The main problem we have is people look at this table and might not see the rest of it.
**James Thompson** 50:47 But that's not unique to…
**Josh Suereth** 50:50 these notes, and that's not unique to other things, because if you look at these OS-type values, the list of values that may be used, they come as a separate table after the fact. I think they're also somewhat problematic in the same way, right? And that, to me, this is more an issue with
our ability to generate markdown.
Versus, like, HTML, and limitations in Markdown.
Because I would also love to fix this here with an enum, where, for example, up here, when you see the enum.
And you know it's an Inum.
We could, instead of just examples, we could actually just splat a subtle.
You know? And you can see it right there.
with the specification. I think that could be powerful.
So I…
I like the problem you're trying to address. I'm not 100% sold on the solution, because I think that it's,
If I understand correctly, This here requires some sort of annotation.
In the… in the markdown to then generate this table, right?
**James Thompson** 51:55 It… so, it's an annotation per attribute.
I'd say… so… the Linux one is an annotation on that attribute.
**Josh Suereth** 52:05 Right.
And then that's how you build and generate the table, yeah.
**James Thompson** 52:10 So it's not one bulk definition, it's actually built based on the attributes there, so that if we put it on the attributes and reuse only some of the attributes, you get a condensed table.
**Josh Suereth** 52:23 Right.
**James Thompson** 52:25 Right, because the other thing I thought about is, could we potentially somehow have a Linux-specific page?
for the attributes, and filter the annotations to only show the Linux implementation.
Which you can't obviously do with notes, because it's…
freeform text, but having it as an annotation, you do have that flexibility to potentially filter it on a Linux page.
**Josh Suereth** 52:50 Yeah.
I mean, the question is, is it just about Linux versus Windows as well?
Like, how many of these… Divert… it's… yeah.
How many of these can you divide?
**James Thompson** 53:15 Yeah, it breaks…
**Josh Suereth** 53:16 Yeah, that's by OS, but, like, in other places, it's not by OS. It could be by database, for example.
**James Thompson** 53:22 Yeah, and that's why, like, I didn't… the annotation I used was the generic naming. It was implementation. So, if you looked at a cloud provider, you would have your GCP, you'd have your Azure, you'd have your AWS, for example.
**Josh Suereth** 53:36 Yeah.
Anyone else have thoughts on this? Wanna say anything?
**Braydon Kains** 53:46 I guess it's kind of a matter of taste, whether you prefer one… Table format or the other.
Personally, I'm… More in favor of…
the structure of notes. Like, the… how it's, like.
You have the attribute, like the build ID, and then a table of 3 operating systems.
I find that clearer to read than the matrix style of the full table.
But I don't… Have a solution for how the notes are… are broken away from the table.
I think the…
Actually, what this has in the note right now. So was that done by, like, putting a markdown table into the note, like, in the YAML?
**James Thompson** 54:38 Yes.
**Braydon Kains** 54:39 Okay, that's a little awkward.
**James Thompson** 54:42 And what makes it even more awkward, you have to leave empty lines in between them so it renders correctly.
**Braydon Kains** 54:47 Oh, yuck, yeah, makes sense. I would love to see this built into code generation, because there's a lot of places in…
in the system namespace, or the process namespace, where it's, like, on Windows you get this val… you get this metric this way, or in Linux you get another way, and it's just kind of, like, written manually. It's being able to…
throw in, like, some sort of annotation of, like, how the implementation works in the different operating systems. I hope we can get that into the YAML.
**James Thompson** 55:17 So, that's certainly possible. I went… for me, I liked it having the single table.
But if we wanted to, we could certainly… Have it under a heading.
Right? Similar to the current notes, and use the annotation to power it.
If we wanted to.
Yeah. That's the option.
**Braydon Kains** 55:38 have a…
a technical reason against the Matrix, it's mostly a matter… it's a matter of taste. I'm not a big fan of the Matrix-style table versus, like.
Seeing an attribute, and then seeing how it's implemented on the three operating systems, but… .
**James Thompson** 55:54 They…
**Braydon Kains** 55:55 the general idea of being able to annotate attributes or metrics with, like, how you instrument that on each system, I think, is…
would be very helpful to have in multiple places. So, however, it gets
Produced in the… in the markdown.
**James Thompson** 56:15 Right.
**Braydon Kains** 56:15 it's… either way is fine. I like the idea, though.
**Josh Suereth** 56:24 Yeah, are there… so… I like the idea of making this more structured.
So that we can,
We can actually do fancy things with it. I'm also with Braden that I'm not sure if the current rendering or throwing it separately is… again, my take is the main problem we have is the information can't fit in the same area. If we had, like, collapsible windows and things around the attribute and had it all in one big table.
That would be my take on reference docs, is to find a way to fit it all together better.
But our limitation is marked down there.
This… this… actually, what you've done here with docs and sources, I feel like these names, we would… we'd want to figure something out here.
Because if we're using it for generic tables, it's… it's different. And you can see, if, like, to Braden's question about how this was done before, you can… this is where the previous table showed up, right? We're literally embedding tables and notes, and it's… it's awkward.
So, having a better way to do that, and having a way to interact with it programmatically, having the ability to have some sort of filter where I say, cool, I want to, you know, generate for Linux, I want to generate for Windows, that makes sense to me.
So I think there's… there's definitely pieces of this that we should… we should continue to look at. The,
overall rendering, I think maybe we want to discuss more of, like, what's our goal, and what do we consider better for users here? Because I don't think there's a clear win of this.
Versus… this?
like, to me, that's a matter of preference. But what would be a clear win is if, say, these notes, right, if you hovered over and it popped up.
the HTML right there, so I don't have to scroll around to see things. To me, that's a more clear win. Or just having, you know, expand, collapse, pull the table out here.
to me, that actually is a bit of a win from consolidating information. But this doesn't solve the problem of you have to look in two different places for the same attribute to find information, right? That's still… that's still the case here.
So… so this part… this part I'm not sold on, but the idea that we could say, generate Linux-only docs, I do really like that idea.
Anyone else have other thoughts? I think we're running out of time.
Okay?
Thanks for sharing, hopefully that was helpful. If folks have a chance to check out the Schema V2, work… oh, I forgot to put the bug there, because I was presenting. I'll do that after the meeting, and thanks, everybody. We'll see y'all next week.
