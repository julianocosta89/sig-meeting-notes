SIG: Service and Deployment SemConv
Date: 2026-02-26
Duration: 53 minutes
============================================================

## Zoom Recording Transcript

**Braydon Kains (Google)** 02:14 Trask, do you happen to have permission to kill the note-taker?
**Trask** 02:19 You know, I've given up.
I do, but, like, they've just… they've defeated me.
as…
Because Zoom doesn't make it convenient, like, I have to… I have to look up the code, and then…
Take meeting ownership, and then boot them.
**Braydon Kains (Google)** 02:43 the gall of this thing to say, buy Romania on the line.
**Trask** 02:46 Right.
**Braydon Kains (Google)** 02:47 This recording is unbelievable.
**Trask** 02:49 I know, I know, it pisses me off.
There… there's another note-taking bot that joins that's actually flight, and says… allows you to opt out. Like, you can just… it'll… in chat, you can type opt out, and it'll go away.
**Braydon Kains (Google)** 03:07 I did that before everybody joined.
**Trask** 03:10 Yeah, that feels to me like the minimum, but…
the… yeah, so I fully blame the, the note-taking bot.
Awesome.
**Anthony Mirabella** 03:22 Who owns… who owns that, and why have we not banned it if we don't want it?
**Trask** 03:28 We've tried.
**Braydon Kains (Google)** 03:29 We've tried.
**Trask** 03:31 Slack… I mean, we've reached out to Zoom, we've… I've submitted multiple, complaints, but they're just like, nope, doesn't…
You know, not a problem with our terms of service, like, if you don't want them, you have to make the meeting private, and…
**Braydon Kains (Google)** 04:01 My headcanon theory for how these things work is that people have, like, it attached to their calendar to automatically add to their meetings, and then they add the public OpenTelemetry calendar, and then it just adds it to every single meeting on there, whether they go to the meeting or not.
That's… I'm pretty sure what happens.
**Trask** 04:19 Yeah, Pablo was able to…
Figure out one of the people at one point, and reached out to them, and they didn't even know that it was happening.
**Braydon Kains (Google)** 04:31 Yeah.
**Anthony Mirabella** 04:32 Well, Andrew, for your notes, you're bad, you should feel bad, stop doing this.
**Josh Suereth** 04:42 What's crazy is, don't we… don't we keep recording somewhere where we could just say, hey.
Go look at this, like, tell your agent, go look at the sheet.
grab the recording, get all the information you need from it, like, don't we even have notes that we're keeping from, like, a CNCF thing?
**Anthony Mirabella** 04:59 Yeah, absolutely. Like, all of the meetings are recorded, there's a spreadsheet that has the links to all the recordings, there's notes for each of the SEGs.
**Josh Suereth** 05:06 Let's make an agent.md for the OpenTelemetry org trask that just says, hey, if you want to do agent things in OpenTelemetry, point at this, and and yeah, you get everything you need, and then we don't have to have 10,000 of these, like, people joining all the calls.
Because I think in the entity SIG, we had 3 the one time.
**Trask** 05:27 Yeah, I've been outnumbered by bots before.
**Josh Suereth** 05:39 Should we get started?
**Janhvi** 05:43 Yeah, I can, I can quickly share my screen. One second.
We have a few items on the agenda. Feel free to add more if you have something you'd like to discuss.
Okay, let's start. Do we have Arnav on the call?
**Arnav Bansal** 06:09 Oh, yeah. Hi, Jandvi. Hello.
**Janhvi** 06:13 Yeah, Nev, do you want to go first?
**Arnav Bansal** 06:15 Yeah, so, this is regarding the deployment environment.name, attribute that we were discussing to stabilize. During, I think, in the last week's call, we discussed that, maybe making… having some enums values for this
attribute makes more sense. So, based on that discussion, I have added, four values on…
In this PR itself.
It would be great if you guys could maybe take a look.
on this PR.
**Janhvi** 06:48 Got it. I love, so…
**Arnav Bansal** 06:50 I think we still want to get a consensus on the enum values that you've added, right? Do you want to… That's correct. That is correct. So right now, like, I have added 4 basic values, that is production, staging.
Development and test.
This aligns with the values that we have in GCP AppHub as well.
And, basically these values are sort of parent values.
You can always use them. And this is an open enum field, so people can always use their own values, along with these four predefined values.
Oh, yeah, does anyone have any questions or suggestions around the values?
**Trask** 07:32 Arna, can you, then this'll need to be a separate PR that's not marking it as stable.
Right? Like, because this is the change, we need to make the change first, and then let it propagate a little bit before we market… decide to mark it stable, I think.
**Arnav Bansal** 07:53 Yeah, I think trust that makes sense. I'll update the PR show.
Anything else about the values, or… Railing.
**Janhvi** 08:05 I think to me, it looks okay. Even in all the other open source places we see, these are the most commonly used values, and given this is, like, an open enum, people are still allowed to use anything else if they have any special use cases, so, looks okay to me.
**Anthony Mirabella** 08:25 I'm not quite sure on the must language. If one of them applies, then the respective value must be used.
What does it mean for one of them to apply? Should it be should?
**Josh Suereth** 08:37 That language is across all the semantic conventions, Anthony. That is not anything specific to this PR. Every single and Newman semantic conventions has that.
But if you have questions about, like, what that means, like, we can walk through that, but that's actually… yeah, by making it a NUM, we're saying if you are doing something where it's similar to development, you have to use this enum. If you have something that's not modeled by the enum, you're allowed to use a new value.
**Anthony Mirabella** 09:04 Okay.
**Trask** 09:08 You could always use whatever, but it wouldn't be SEMCOM compliant.
**Arnav Bansal** 09:17 Cool, I'll split the two PRs, and maybe send it out, send it out for review.
**Janhvi** 09:26 Cool. Thanks, Arnulf.
Okay, I see there are two things from Ayushi. Ayushi, do you want to go ahead?
**Ayushi Asthana** 09:37 Yeah, sure. So for the criticality attribute, right, the demo PR is raised, I've followed up with the author about getting this merged, so it's been raised for a while, there were some changes made.
earlier, So…
I have pinged him, I think, earlier this week to know if there is an ETA for getting this merged, but we will have this demo
In hotel ready.
After that, maybe we can discuss about whether we want to stabilize it now, or do we want to wait, for any other feedback?
But we do want to wait for this demo to be in before we talk about stabilizing this attribute, if I'm…
Right.
Is that, like, the plan?
**Janhvi** 10:30 Yeah, I think that's what we agreed upon earlier. We'll have at least this demo checked in, and then we'll go ahead with the stabilization.
Folks, correct?
**Ayushi Asthana** 10:40 I didn't…
**Janhvi** 10:41 Yep. Yeah.
**Ayushi Asthana** 10:45 I think we can follow up on the thread itself, in the channel, or if we don't have any traction on the PR by next week, I can…
Probably…
copy it over, I don't know. I would like if there is any suggestions, but there is already a demo PR, so, how can we move it along if there is no traction by next week? I'd like suggestions on that.
**Janhvi** 11:14 I think maybe if you don't get… Sorry.
**Josh Suereth** 11:17 I was gonna jump in. There is a… there's a SIG that owns the demo, and there's a CNCF Slack channel for them, so it might be that you just… we need to just raise some awareness and kind of ping them on Slack, or… or, if we can put it on the SIG agenda, even if you can't attend the SIG, just say, hey, FYI, we're doing this in the, you know, deployment and service SIG, and we wanted you to take a look at this, because this is a thing that we are…
pushing, and give them some background. Like, give them some context on why it's useful, why we want it, what it does, that sort of thing. Yeah.
**Ayushi Asthana** 11:51 Okay. The, the demo seg… okay, I'll look at the time slots for the demo seg, but… okay. We can try that out next week if we don't get interaction on the, like, on Slack or on the PR itself. Thanks, Josh.
**Josh Suereth** 12:07 Yep, I haven't looked at the demo SIG, so I don't know how…
long it takes for them to take a look at PRs, but some areas of OpenTelemetry are different than others, and there's a… always a grab bag for everyone's attention, kind of like social media, if you will. So finding a way to advertise yourself for what you're doing, why it's important, get people to care, that…
always a fun thing in OpenTelemetry, but that would be my recommendation to get that particular PR looked at.
**Janhvi** 12:33 Josh, quick question. So, is this demo SIG, like, a common SIG which kind of approves all the demos that are added in SEMCONF? Like, what's the agenda?
**Josh Suereth** 12:42 So, for the
No, no, no. So, like, there is a… the demo SIG owns that demo repository of getting OpenTelemetry demo together, and there's a set of people who can review and approve stuff on there. So, the SIG is just meeting to talk about, like, what to do in that repository, and I don't remember if they're still active or not. Trask…
I don't know, I'm gonna throw you under the bus as a governance committee person. Do you know?
**Trask Stalnaker** 13:10 I assume…
**Josh Suereth** 13:12 Yeah, I assume, I just… I don't know when they meet or anything. I just know they exist, or they.
**Dotan Horovits** 13:17 Are you talking about the Auto Community demo, or something more specific?
**Josh Suereth** 13:21 Unit Demo application, here they are.
**Dotan Horovits** 13:24 Yeah, yeah, it's definitely active, actually. I think the meeting took place yesterday, or day before that, and I also caught up with them at Hotel Unplugged Europe in Brussels, for those who were at Fostom. So yeah, it's pretty active. Actually, there's an active discussion now about whether to go for a lightweight version of the demo.
And all of that, so, yeah, live and kicking, and definitely worthwhile bringing it up with the, with the demos link.
**Josh Suereth** 13:51 Yeah, actually, Doughton, if you're… if you're available, would you mind, talking to them about this PR and, like, what we're trying to do with Criticality, and… and, like, the value of the PR and things with the SIG?
I actually think it may be worthwhile… I'm wondering if to bring it up async, or just.
**Dotan Horovits** 14:08 talking, but I think just bringing it up async with them, would be best to start it. The hotel demo, let me just find, I think it was auto demo, but I'm just checking quickly the, the Slack, hotel-demo, right? Or community demo, sorry.
**Josh Suereth** 14:25 The link I sent has the Google Doc, it has the Slack, it has the.
**Dotan Horovits** 14:28 Oh, okay, okay, yeah, so, yeah, so, I'm just wondering if, if it needs…
discussion, or first just presenting it on the Slack and seeing if there's any, initial responses there before, taking it as an agenda item. What's your, thought?
**Josh Suereth** 14:46 My suggestion would also be to, like, ping them… ping them on Slack, and then if it… if it doesn't get any attention, then take it to them, like, in person, in the discussion part, yeah.
**Dotan Horovits** 14:59 Okay, so I can, I can definitely look into that. I'll follow up with you, Josh, just to make sure that I adequately, have all the context to, to relay there, and, happy to take the time.
**Ayushi Asthana** 15:19 I think there was also the proposal for introducing data entity.
in a hotel, similar to a service entity, and I had put together, some items.
Around what it means in different… for different cloud providers, and how it could help in the observability community. The only issue that I did face, for
Just, like, briefly was finding enough data in observability around this, but there is definitely a lot of use cases in compliance and security space.
So, I'm still looking for some more links and some more, documentation for Dynatrace and New Relic, and how they handle data. There were some, some, like, details for Datadog and Splunk that were heavily available. So, I'll quickly go over it,
So, right now,
We do not have a system for tagging the cargo that databases and services are dealing with in a service ecosystem.
And how this could help, eventually, if we start tagging this in OTEL, is setting up automated retention, setting up automated security guardrails and observability platforms for SecOps providers.
And having compliance mapping for both observability platforms and SecOps providers around data storage, data retention, and also data transmit.
So, right now, Janvi, can you scroll down?
How cloud providers are doing,
Data tagging or data cataloging. Aws has something called as AWS MACI. I think, we have folks from AWS on the call today, and they can talk about Macy and Glue Data Catalog.
I have added here what I could find about how they do automated discovery for S3 buckets and prioritize security recommendations based on tagging.
And data catalog that, stores metadata about assets and categorizes it by domains for discovery by other, platforms, right?
In GCP, we have something called as SDP that enables a similar service for data discovery, classification, and protection.
We also have DataPlex that does similar business-based tagging on, and, like, storing metadata about the data that's present in, for example, BigStore or other data storage services inside GCP.
Oh.
And there are listed similar,
services in Azure and Alibaba that deal with either data sensitivity or data categorization and some use cases of it. And I've attached links inside this document. We don't need to go into the details.
But we are targeting two main use cases here. One is data categorization for businesses, and the other one is
Data sensitivity for security use cases, and how it's important, and how it can help.
John, I'm gonna go scroll down. So, in Kubernetes, there is no native way to build data classification, but it is largely, like, sort of achieved via labels and annotations.
Or having, like, persistent volume claims, which sort of map to sensitivity in Kubernetes, but there is no native vein gates at this point to have data categorization or data sensitivity annotations.
Can you scroll down a little bit? There is a, like, sample YAML that shows how these labels could look like inside the PVC, but again, there is nothing that comes out of the box with Kubernetes.
Kubernetes uses some plugins, though, that I think I've listed.
You scroll… Rewrite. So there are a bunch of plugins that customers can use on top of
if they have a KH infrastructure, like Kaverno, Sentinel-1, Silium, HashiCorp, and they all serve as, either some form of, data protection or policy, or, managing metadata about their volumes, or managing metadata about their data stores.
So, there is a lot of plugins, there is no native way for KH also to manage this, so all of these plugins sort of help in managing data storage, data categorization, and data security for Kubernetes.
Janav, if you scroll down now, we discuss in this section, the potential for the data labels in observability, since it is not, like, general for KHS also to do this. So, even, the observability platforms have…
currently have limited scanning, masking, and retention-based use cases with data. So, for example, there is Datadog… Datadog has some security
Offerings that use…
scanning engines or masking engines that can utilize these labels, data sensitivity labels, that can be attached to certain data stores or certain services, and run on top of this. This is a potential. There is, like.
Currently, no usage, so this is all configured by the customers inside observability platforms. There is no way to transmit this from, like, the servers to the platforms natively, as far as I could understand.
So currently, all of these scanning capabilities, all of these masking capabilities, they exist inside Datadog, and you can go to Datadog and configure them in the platform, but you cannot transmit these details from your server to Datadog.
So I've talked a little bit about the potential of having these data sensitivity or data categorization labels.
And how it could, sort of.
Translate into what we do in observability.
I won't go into, like, a lot of detail about every single observable platform, what they are doing, and how it could be impacted, but you guys can go over it, offline, and then…
Comments and feedback is welcome.
I'll stop here.
Was I audible?
**Janhvi** 22:35 Yeah, yeah, I see, we could hear you.
Any high-level feedback? I know in observability, we don't have a lot of use cases, or we've not standardized it yet, but there is, as Ayushi mentioned, there is potential to kind of standardize it and build use cases on top of it.
And in the other areas, in, for example, cloud, we're already seeing a lot of use cases for it.
So, that's why we thought it'd make sense, but we just wanted to get, like, generic feedback from you on how you guys think about it. Josh, go ahead.
**Josh Suereth** 23:09 I was just gonna ask a few questions. So…
we had the motivation around, like, having a sensitivity criticality for the service itself, and then this is about data. What I'm looking at these use cases that's kind of interesting is, like, the anomaly detection here, where you get an alert.
and then if you notice something interesting, and it's against sensitive data, you bump the criticality of it, that automatically happens, that means we have to tag the data in some fashion to say that this is part of a critical system, right?
So the idea here would be, in observability, we'd make sure our signals have that tag.
So that downstream systems can just use that and say, oh, I have to take, like, this thing that was interesting is now really interesting, I need someone to look very quickly.
**Ayushi Asthana** 24:01 Yeah, yeah.
Also, also masking is, like, another important use case that came up over and over, where, if you have a data store that is labeled sensitive, you would want to
Perform certain masking operations on the logs or telemetry that that service is generating, or that data store is generating.
And so that was another interesting thing that, these labels could be used for proper masking in observability.
**Josh Suereth** 24:32 So, in OpenTelemetry terms, that'd be like, we would have an automatic, you know, sensitive data redaction processor that could… basically, you might have different levels of redaction that you have, where maybe if the data is considered very sensitive, we really don't log much.
But if it's less sensitive, we'd log less. Okay. That is a problem that, like, Trask, I know, there was discussions at one point about, in semantic conventions, about, like, opt-ins and what we report by default.
Do you think this plays a role there?
**Trask Stalnaker** 25:06 Sorry, I wasn't fully paying attention,
I mean, if it's sensitive data, we are… it should be opt-in.
**Josh Suereth** 25:17 Yeah, sorry, this is, this is about,
So I can open this up to everyone, but, like, this is about… we're trying to figure out the level of how much data to include by default. And I think what this is proposing is if we start tagging
The sensitivity of the datastore itself.
we could have, like, an actual tiered set of layers of, like, okay, if the data's very sensitive, we actually include less information, in, in, like, public space, and if it's less sensitive, we can include more information by default. Is that… is that… am I reading this right?
**Ayushi Asthana** 25:53 Yeah, I think the intent is that. I was also, by the way, talking about not just, like, sampling, or low sampling, or higher sampling, but explicit masking of logs.
Where we redact data when it enters the platforms, or when it is collected by observability platforms. At that point, is it being masked? Does it need to be masked? That sort of setup that can exist on collection side of things.
**Anthony Mirabella** 26:25 So, kind of to that point, I guess the thing that's not super clear to me is… I think, as Josh was kind of just describing this, it sounds like this applies to
like a data store or someplace that data lives, not necessarily the data that's flowing in the telemetry that's being produced, right? So we're not saying that the telemetry is highly sensitive or confidential, we're saying that this is telemetry about a system that stores confidential data.
Right, so that wouldn't necessarily lead me to think that we need to do additional redaction of logs necessarily based on that. Like, if you're logging out of a system that stores highly confidential data.
Should you be putting that confidential data in the logs in the first place?
Or…
**Josh Suereth** 27:08 That's the problem, Anthony, is right now, we have one set of things we do in instrumentation. So let's say, let's take, like, a database instrumentation, right?
If a database is sensitive, we should probably include less information by default.
But OpenTelemetry has one default.
What if instead of one default, we let you tag
the database and say, this is sensitive, and then OpenTelemetry could have A tiered set of defaults.
Based on that.
**Anthony Mirabella** 27:41 How would that information flow to the instrumentation that needs to react to it, then, though?
**Josh Suereth** 27:47 that's my next question about this proposal. Where do we put this information, and how do we… how do we flow, that information there? Like, going through this, it… it absolutely, like.
you know, you want to tag the database itself, and say, this is… this database has sensitive data, or this thing has sensitive data to it, right?
Where do you see us getting access to that information?
I know on a GCP perspective, I was kind of curious with other things, where do you see us in OpenTelemetry getting access to that information to tag data appropriately?
**Anthony Mirabella** 28:27 Sorry, was that question to me, or to Aishi?
**Ayushi Asthana** 28:31 Yeah.
**Josh Suereth** 28:31 Too easy, yeah.
**Ayushi Asthana** 28:33 Okay, so,
So, if I understood correctly, the question is, where is this tag living? Is it living on the servers that's handling the data, database that's storing the data, or wherever the logs are being emitted? Is that right, Josh?
**Josh Suereth** 28:53 Yeah, so, like, I guess I'll rephrase it, you know.
This has a lot of value if we can… again, this is a resource tag, so let's all make sure everyone's clear. This is not tagging a spin, this is not tagging a log, this is tagging the resource of the log, saying, this log is generated about something that has sensitive data.
In OpenTelemetry. So we're tagging the resource.
how do we make sure OpenTelemetry has access to that tag?
And where does it get that notion, the sensitivity notion? Like, how does a user specify it in their system? And then how does OpenTelemetry get it and associate it with the data where we can make these decisions around masking, or these decisions around, you know, filtering or alerting and that kind of stuff?
**Ayushi Asthana** 29:43 Okay, okay.
**Janhvi** 29:44 How would that be different from, like, any other metadata tag that the users attach in their ecosystems and then observability gets it from? That should be the similar flow, no? Or you think something specific needs to happen in this case?
**Josh Suereth** 29:57 I mean, it could be, but again, we've designed those, like, for service, right? Right now, service information generally comes from environment variable.
Is this something we'd expect people to put in an environment variable? Is this something we want to go after those Kubernetes annotations?
Where we might have to be flexible, right? Like, like…
on systems where someone can tag the resource directly, like in GCP, is there an API we call to get it? That's kind of…
**Janhvi** 30:24 Got it.
**Anthony Mirabella** 30:25 Well, there are two levels there, right? That's talking about how do you get information into the resource in… say we're talking about an application that's doing logging, or metrics or spans, right? How do you get information into the resource that the SDK is going to use?
The second level question, though, to get to, if you want the instrumentation to adapt to the sensitivity level of the data that the system is working on, is how does instrumentation get the resource?
from the SDK that it's currently working in. I don't believe, like, meter provider provides access to the resource that's attached to the SDK. That's, you know, something that just gets attached, you know, as data flows through the SDK, but is never really exposed through the API, right?
**Ayushi Asthana** 31:08 I'm sorry, I'm sorry, I did not follow the…
**Anthony Mirabella** 31:12 So… Fair?
**Ayushi Asthana** 31:13 doc.
**Anthony Mirabella** 31:13 If you want instrumentation to be able to say, this is a system whose resource has data sensitivity of
confidential attached to it. I want to reduce the amount of information I'm putting into the logs or metrics or traces that I'm generating at instrumentation time.
how does that instrumentation get access to this resource attribute value to know that it should do that? I think typically that would be done through configuration of the instrumentation.
**Josh Suereth** 31:39 So, I think we're solutioning there, Anthony. You might not need that level of granular. So, for two things. One is, how does instrumentation get access to resource? That's an overall problem in OpenTelemetry.
So, if we assume that this gets attached to resource, we actually are, as part of the entity SIG, proposing API-level access to that, because instrumentation doesn't have access to it today, and it makes a lot of things really awkward.
Like, there's a… there's a system in Java instrumentation that re… like, duplicates the resource, so you have access to it in instrumentation.
Because you don't… you can't get it through the API, you can only get it through the SDK, but let's pretend, like, that's a problem that we can solve somewhere else. It's also true that you might interact with this in the collector.
Like, you might actually have a collector thing that actually understands the sensitivity.
of the resource and looks it up on your behalf, and that's the thing doing the redaction, right? Doesn't have to be necessarily an instrumentation.
**Anthony Mirabella** 32:38 Yeah, I think that use case is a lot clearer, right? Because then it's got the full view of the data and can operate on that.
**Josh Suereth** 32:45 Right, and I think taking these use cases that we want to target and writing them down.
like, you're mentioning them in person, having them in the document of, like, alright, if we want to add sensitivity in OTEL, here's the set of use cases we think are, like, the number one things for us to target now, and then we can walk through, do we have all the pieces in place to make it successful? It'd be awesome.
Because everything you're saying makes sense to me, but if we can write it down and agree, this is a valuable use case, I think that'll…
That'll help us out here.
Sorry, Neil, you had… was it Neil who had his hand up? I… we were talking over you, I don't know if you want to…
**neil yashinsky** 33:20 That's a great segue, Josh, because that's kind of what I was wondering about the process, because it seems like, you know, as much as I know about OTEL, and there's a lot that I do, there's a lot that I don't, and it kind of seems like this is a situation where we're defining new capabilities
And there's gonna be a lot of, in the beginning at least, variations in approach to implementation, just because of where people are starting from.
And so I was just really curious, like, does OTEL have a process by which, hey, this is how something should work, functionally speaking? And then, you know, Ayushi and other folks can say, well, for us, this is the path to implementation, and then kind of…
compare that, I guess, and most importantly, kind of start with our functional requirements as defined as a goal, or whatever, and then it seems like the conventions, or where in the conventions that gets refined should ideally
flow logically from that, but again, it's kind of a very… it's a question as much as a statement, for sure. Is that how it works, I guess is the question?
**Ayushi Asthana** 34:24 Right.
So, Jami, if you'll scroll to the last part of the doc, right, I have mentioned, and I think we'd need to come to this sooner than later, is,
an important feature for this, semantic is going to be cross-resource correlation when data flows across the system. Can you scroll up a little bit? So, this is something that maybe we would want to solve in how
we are going to, sort of, propagate this entity, where is it going to lie? I think it talks to, I think, what Josh, you were getting at. Where is this,
Basically, tag, or this semantic going to be attached?
Is it going to be the database? Is it going to be the service? Is it going to be the pipeline? Where will we attach this annotation, and then who understands it, in order to handle the logs correctly? So, we would, we would want to…
Like, define what this, semantic will mean, where it's attached, and then how… can we do cross-resource
risk or category allotment. We might want to, like, define that, because data is, like.
Unlike service, data is, like, an entity that will flow across the system, and to do, like, a proper risk allotment or a proper category allotment, we might want to, like, think about that a little bit more. Where do we want this to live?
Yeah. Josh, does that speak to what you were asking, what you were getting at?
**Josh Suereth** 36:06 Yes, yeah, I think… I think it's… it's definitely in the direction I think we need to go. I think, again.
writing down, like, that… that use case, what we're targeting, what the architecture would be that would support this, I think that's… that… in my mind, that's a big next step for us to all kind of see and grok this well. Dimitri, you have your hand up. I don't want to jump in front of you.
**Dmitrii Anoshin** 36:28 Yeah, I'm struggling to, like, actually understand, like, what the data entity would be if I'm, like, coming…
if not… if I don't know the context, and I come from the outside, and data, as an entity.
it just can be too confusing. So I… I'm not sure why it has to be an entity. It can be just a generic descriptive attribute that we can apply to the, like, to all the telemetry, and to any entities, essentially, and that generic…
Set of attributes would be kind of data sensitivity or something like that.
Because we cannot attach any telemetry specific to the… to that kind of category of data sensitivity, right?
So I'm not… I'm not sure I understand why do we have to introduce an entity here.
And especially, like, first of all, why it has to be an entity, and second, like, the data to summarize what my thoughts are.
Data naming itself is pretty confusing, because, like.
I can think about data as an entity is just, like.
Not related to sensitivity and security context at all, it's just, like, just some kind of… Daytime.
**Ayushi Asthana** 37:58 Yeah, yeah.
I think Josh proposed, like, a alternate just now in the chat, data source, if data source makes sense, and you can definitely put it on the table and discuss, but I think what you're saying makes sense in terms of data as an entity, like, what would that mean? And what would we…
mean if we call it data source, so… I think that's a valid point, and we'll talk about that.
**Josh Suereth** 38:24 One quick thing to Dimitra's comment. We don't have…
You can blame me for this, by the way. It's a discussion we're having in semantic conventions. We don't have a way to just, like, have raw attributes that you tag on things in SemConv. Everything's a signal.
Right now?
So, we kind of have attribute groups, but they're really awkward, and it's not well modeled. So I think I agree with you that, like, this is a… this is not really an entity, this is, like, an annotation on an entity, like, it's an annotation on a resource.
But we don't have a way to express it yet. We only have entity. Yeah, if everything looks like a nail, you know, or no, if all you have is a hammer, everything's a nail.
It might be that we need to expand some of those discussions around, like, the… in cement convention specifically, having a way to discuss things as annotations on entities versus just straight-up entities, yeah.
**Dmitrii Anoshin** 39:22 But we do have that problem in other fields. We have cloud. Cloud is not an entity, but we use it, like, extensively everywhere.
**Josh Suereth** 39:28 Oh, God, yeah, that one's the worst… that's probably the worst offender, right there.
**Dmitrii Anoshin** 39:33 Exactly, and we need to do something with that.
**Josh Suereth** 39:36 But a cloud… a cloud is an entity.
**Dmitrii Anoshin** 39:38 Which one? What is the entity in that case, then?
**Josh Suereth** 39:43 Yeah.
It's just not a useful entity, but it totally is one.
**Dmitrii Anoshin** 39:47 Yeah, it's pretty similar here, I would say. So we might need to introduce some kind of concept of generic descriptive attributes.
**Josh Suereth** 39:57 Yeah, Dimitri, why don't we take that to talk about, more in the entity SIG, about what we'd want to do there.
**Dmitrii Anoshin** 40:02 Yeah. Because I think, like, this is a…
**Josh Suereth** 40:05 I… by the way, thank you for these documents. I think they really help outline, like, what we're talking about, and how things are used, and the value. I think we want to think about that use case and how…
how it would fit, and, like, the best way to model it. So, we can go into the entity SIG and help you figure out for that. For now, let's stick to, like, figuring out the use cases and the raw attributes that would have to get attached, and we'll figure out what the thing is that bundles them together is later.
**Ayushi Asthana** 40:32 Go ahead. Yep.
So, I think…
I remember at least a few, but I don't know if we have notes. I would invite all of you to please add comments also, if there is anything else that we should cover.
But I will address some of the comments that we've discussed today in the doc.
Thanks. I… Janvi, that's…
**Janhvi** 40:59 Thank you. I think, we have about 6 minutes. There are 3 more points. I know, I think, Trask, you added it down, but it probably got mixed up with the dates. Do you want to go first? I think this one we can skip for now, and then we can discuss, service name and instance ID.
**Trask Stalnaker** 41:19 Sure, I just wanted to follow up. I left, I created an issue for it, and I kind of documented there, but not sure if folks have, had a chance to think about this.
I tried out the proposal from Josh, and,
Ran into a wrinkle on it that…
is sort of that it doesn't quite feel as good as the client address, server address, because we have modeled service.name is…
a resource attribute, right, as itself. It's not tied into span connections, so we sort of ended up with
it's almost… it's sort of a peer relationship.
In that we have service.name is always yourself.
And… Peer is always the other one.
As opposed to quite as clean as the client address, server address, where it… that's always how it's… it's always in the context of a connection.
Now, it doesn't mean we can't have all of the above, it just,
was… I just wanted to point out the… bring up the… less…
The thing that didn't work out as nicely.
As I was hoping.
And I think we lost… I saw Michele, joined initially. I think he was hoping to be here for this discussion.
**Josh Suereth** 43:18 Maybe we need to talk about this more,
offline and next week. So, so the…
The one that you ran into was this notion of client Versus consumer, is that right?
**Trask Stalnaker** 43:35 No, I'm not…
**Josh Suereth** 43:36 The one that you said was not as nice. Yeah.
**Trask Stalnaker** 43:38 Has client… so, client address, server address.
The client and server namespace work really nicely. Whichever direction you're looking at it in a, of the interaction, it's the same. Client is the same in both cases, no matter where you're observing it from.
So that has some very nice properties, which is one of the reasons we went to that originally.
In the case of service name.
We are stamping it on the resource. We have service name already. It is on the resource. It is who you are.
So, the only other one that is interesting, right, is gonna be who the other side is.
So, we can do, you know.
On the client, we would have service.peer… I mean, on the client side, we would have service.name and server.service.name.
And on the server, we would have client.service.name and service.name.
**Anthony Mirabella** 44:56 And in the case of a proxy or other intermediary, you would have all three?
Potentially.
**Josh Suereth** 45:09 Yeah, if you're reporting from the middle, you would have both. Like, if you're making a log or something, that would be talking about both in a proxy.
That was the idea why Service.peer might not be good enough, was that… that use case. That's what motivated this initially.
**Trask Stalnaker** 45:26 Yeah, but Anthony's saying all three. I think he's talking about, he's talking about a different use case where you're observing from yourself, you're going through a proxy to a remote
And so, would you stamp all three? And in that case, that's where we… that's where we would use peer, network peer address, is the proxy server, is your direct peer.
And server.address is your logical.
server.
**Josh Suereth** 46:03 In the case you're going through a proxy that's about yourself, would the server be different from the resource to the proxy? Like, I don't think you would need to record it, because the name should be the same.
If the proxy's part of your service, but if the proxy's some other service, the name would actually be different.
In the resource.
**Trask Stalnaker** 46:21 Yeah, I'm not sure if service.name makes a lot of sense.
Or capturing a service.name on a proxy itself.
**Anthony Mirabella** 46:40 I don't want to get us bogged down into the details. I think it might. I'm kind of thinking the same direction, that it looks like Thompson made a comment on here that says the same sort of thing, of, like, if you're in the middle of an interaction, and you know… you've got yourself service.name that identifies the thing that is in the middle of that interaction.
It might want to record both the service and the client, or the upstream and the downstream, however you kind of name that. But it's got two things that it's talking to that are the actual actors that are talking to each other and may not even be aware of that intermediary.
**Josh Suereth** 47:23 Yeah, like I guess…
it might be useful to do what we had in the HTTP, some kind of here at Trask, where we actually draw it out of, like, here's scenario one, service A talking to service B,
Yeah. Here's what comes out of service A, here's what comes out of service B. Then we can do man in the middle, and say, here's what service A writes, here's what service B writes, and here's what logs or events or metrics coming out of the proxy would send.
And then we can evaluate the proposal that way. I still don't know if I… like, it still seems to line up in my head, I'm not necessarily seeing the problem. Like, I agree with,
The notion of using source and destination versus client server, I think that's okay, but, like, not necessary either. I think we should be able to determine.
Client and server, in most cases, in traffic that we're dealing with that is at that semantic level. Where we need source and destination is if we're doing craziness with, like, UDP or, like, other protocols where it's really complicated to determine that.
And we don't have a solution for that overall yet in semantic conventions, I'd argue.
Like, I don't… anyway.
But yeah, let's outline the use cases. I think that'd be good. Go through the same exercise HTTP went through.
**Trask Stalnaker** 48:44 Okay.
Sounds good.
**Janhvi** 48:50 Who'd…
I think we are over time. Anything else? I know there are two more things left, maybe we can take that up next time in the next meeting, but anything, important that anybody wants to discuss quickly before we wrap it off?
Okay, I think Braden Ankit, can you guys put these issues in the Slack thread that we have? Then folks can review it offline before the next SIG meeting.
**Braydon Kains (Google)** 49:20 I'm hoping to get mine resolved before the next SIG meeting, so maybe we'll just discuss in the Slack.
**Janhvi** 49:26 Sounds good.
Cool.
Thanks, everyone.
**neil yashinsky** 49:31 Thanks, Johnvi. Thanks, everyone. Adios.
**Janhvi** 49:33 Bye.
