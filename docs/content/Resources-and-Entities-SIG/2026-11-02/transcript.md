SIG: Resources and Entities SIG
Date: 2026-11-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Matthieu Noirbusson (Sensor Factory)** 00:48 Hi, Josh.
**Josh Suereth (Google LLC)** 00:55 Hey, sorry, I was muted.
How we doing? Can you hear me?
**Matthieu Noirbusson (Sensor Factory)** 01:03 I'm… Sorry, I have,
**Josh Suereth (Google LLC)** 01:06 Can you hear me now?
Okay.
Alright.
Just going through our notes to figure out what an agenda can be.
Right.
I wanted to talk about Dmitrii's PR. Did any… do you have anything you want to talk about?
Oh, I'm not presenting the… Agenda, am I?
Let me fix that.
**Dmitrii Anoshin (Splunk Inc.)** 02:17 Everyone?
**Josh Suereth (Google LLC)** 02:23 Alright.
I think we have enough people here to have the first conversation. Should we cancel next week due to QCon?
**Dmitrii Anoshin (Splunk Inc.)** 02:33 I will be at KubeCon, so… For opioid relief.
**Josh Suereth (Google LLC)** 02:38 Right, I'm wondering how many people are either going to be there or busy. Things for it.
**Dmitrii Anoshin (Splunk Inc.)** 02:46 Are you… are you coming there?
**Josh Suereth (Google LLC)** 02:48 I couldn't make it happen this year, so I got approval last week to come, but I couldn't, like, get my personal schedule, so I'm not gonna be there for KeepCon today, sorry.
Yeah.
Anyway, I'll probably be at the EU one.
**Dmitrii Anoshin (Splunk Inc.)** 03:05 Oh, nice.
**Josh Suereth (Google LLC)** 03:12 let's see… We have… let me get this… Copy link… I had a few things to talk about. One was… did Milla has a question for us here.
Which I need to copy over, and then reduce.
Which was… Here.
Alright, let me copy over the notes from this so we can talk about it. Anyone else have any other topics they want to talk about today?
So this is specifically… That's in this version.
Okay.
So for context, this first one, it's a topic from Lyudmila in our Slack channel.
And it is about… whether or not version should be considered identifying. And specifically, I think it is on… fast. And so this is actually somewhat nuanced, if I understand this one correctly. So… In our Entity Modeling Guide, we talk about identifying already.
And how, the lifespan must not change Right, the identity has to survive the whole lifespan, And so… This is talking about whether or not a version is identified, and we have Two places where version Actually, is identifying in Semcov, and we have a bunch of places where it's not. So, service.
It's not identifying. OS, it's not identifying.
Telemetry SDK, it is not identifying.
It's descriptive. Telemetry Distro, the version's not identifying. The web engine, it's not identifying, and LTEL scope, the version is not identifying. I actually forget Do you remember what Hotel Scope is? I kind of forget what that one is at all.
**Daniel Dyla (Dynatrace)** 05:40 I think that's meant to be, like, instrumentation scope?
**Josh Suereth (Google LLC)** 05:44 Okay.
Oh, right, this is where instrumentation scope shows up in the thing. I don't know why it's an entity, necessarily, but it is. Okay.
And then, for identifying attributes, we have container runtime version and process runtime. So… There's a comment here.
about a service outliving a single version, and a deploy doesn't create a new service, so version is descriptive, right? So, when you deploy something, you deploy it, and yes, there's a version attached to it, but you identify it by the deployment, not by the version.
Apparently, we didn't clear this out explicitly.
I nearly made web engine version and OTel scope version identifying. It came up in this comment, which proposes a fast version.
We talked about fast version, by the way, because they were talking about making that identifying.
Anyway, they were wondering if we could add a note with version and whether or not it is considered identifying.
And then Nathan, who I don't think… I don't think he's been to the actual in-person SIG, but he's been commenting on things, kind of talks about this.
Hmm.
So this is basically talking about what the lifetime of these things are, like, when is… the entity for a container different? Is it when you reboot or not? And so, if it's not when you reboot, version is not identified as descriptive, etc, etc.
And basically saying, I don't think versions should be identified in any of these cases.
And so we could make a recommendation to always agree that version is not identifying.
I have one hesitation, which is around FAST, but I think it's because I'm thinking of fast revision, not… Fasts.
**Dmitrii Anoshin (Splunk Inc.)** 07:51 I think a fuzz, like, let's call it function definition.
and function instance, right? Function… whenever function is being run, let's call it, like, container being run, execution, or something.
Yeah. That it will likely have some kind of identifier… ID, which is generated somehow, I would imagine. But if you… if we speak about… function as a, like, defined version, kind of checked in in code, let's say. It likely had just a name, and I guess in that case, a version would make sense. So I… my point here is that I don't believe we… there is an option to have a strict… strict guidelines around version, whether it's part of identity or not, it just depends on the… depends on the entity itself. In some entities, we were… ID can't be, like, generated during the life cycle, it makes sense, but if… After upgrade, it just changes its version, and that's it.
In that case, it makes sense to keep it as part of identity, right?
**Josh Suereth (Google LLC)** 09:06 Yeah, yeah.
I think this goes to the use case. So, for… specifically for Fast, I'm thinking, like.
When I upload a function, it has a name and it has a version.
And I rolled out by version. And, like, if I want to do a comparison of… you know, version A to version B.
I actually have to look at the instances of that function, and compare their values and aggregate back to the version, right?
So it could be, like, in their data model, they model a… Name and version as both identifying, because that's the thing that you aggregate against, but…
**Dmitrii Anoshin (Splunk Inc.)** 09:44 Right.
**Josh Suereth (Google LLC)** 09:44 maybe they… the name is the identifying bit in some of their aggregations, right? So it's almost like they have 3 levels of aggregation there.
name, version, and then instance ID.
**Dmitrii Anoshin (Splunk Inc.)** 09:55 If name… if name changes between… between changes of the function, if it's some… Right.
identity being associated with the name function revision, if that makes sense, but if it's not… If it's just, say, the same as this, between versions, then we need to add version as an identifying attribute, right?
**Josh Suereth (Google LLC)** 10:19 Yeah, I think name stays the same in some of these. That's what makes it awkward for Fast.
Because they're trying to abstract across, like, Knative, and AWS, and Cloud Run and Azure's… I forget what they call theirs, But you get what I'm saying, like, there's, like, subtleties between all of them.
**Dmitrii Anoshin (Splunk Inc.)** 10:39 Because…
**Josh Suereth (Google LLC)** 10:40 I don't think everyone follows the Knative standard.
So it's not like you can just model Knative and then everything is gravy. AWS Lambda is kind of its own beast.
**Dmitrii Anoshin (Splunk Inc.)** 10:49 Yeah, and here, where I'm… Thinking whether we should standardize them under the same entity, or we should have a separate, more specific entities for every cloud provider.
**Josh Suereth (Google LLC)** 11:02 That's actually part of… if you look at… I think it's this one, yeah, where they're trying to define FAS Entities.
**Dmitrii Anoshin (Splunk Inc.)** 11:09 So these are…
**Josh Suereth (Google LLC)** 11:10 There's a lot of back and forth on this.
Right now, it's a request for change.
But we actually think that this, this, the whole fast thing probably needs more attention.
Because I… let me look at this in code view, that might be easier.
I think what they did was they were… Where are the entities? Here we go.
This one is creating… The function definition as an entity?
**Dmitrii Anoshin (Splunk Inc.)** 11:43 Yeah.
**Josh Suereth (Google LLC)** 11:44 And inside of that has an ID, and a name, which is descriptive.
And then a version which they listed as identifying.
And that doesn't make sense to me at all, because if you have an ID, you already have an ID, right? Version doesn't make sense.
**Dmitrii Anoshin (Splunk Inc.)** 12:01 Right.
**Josh Suereth (Google LLC)** 12:02 So this I agree with, like, version doesn't make sense, but then they also have the fast instance, and from what I understand, I think… I didn't think that you had an independent ID.
from the instance… like, I thought you either had name inversion Name and version represent, like, the outer thing, and then you have, instance ID, but you didn't really have this, like.
How do I want to phrase it?
This is a question, I guess, for the FAS SIG, but…
**Dmitrii Anoshin (Splunk Inc.)** 12:32 I want to look.
**Josh Suereth (Google LLC)** 12:32 I already lost it. Come on, come back.
I didn't think that this actually exists in real life, that we would be forcing people to synthesize that.
Anyway, you know what I mean?
But I need to go re-read the Knative spec to see what… what that says. I do feel like we should fall back to… making things work well with Knative, and then making them be, you know, easily understood in AWS Lambda is kind of my de facto stance.
Anyway, okay, so from the SIG… there was a question of, are they interpreting like, is this interpreting what we say here wrong? And I think that's not… like… I think this is the correct interpretation. Versions should not be identified here, right? That's what we're saying?
**Dmitrii Anoshin (Splunk Inc.)** 13:24 Yeah, if… If other identity attributes are unique enough, and if they change across versions.
across version changes, across revisions. And I think that should be the case. At least, I have experience with AWS, Lambda, at least, and in that, as far as I remember, in that space, it's the case.
**Josh Suereth (Google LLC)** 13:50 Okay, so then the question is, regarding this…
**Dmitrii Anoshin (Splunk Inc.)** 13:54 venture.
**Josh Suereth (Google LLC)** 13:55 Should we have any kind of guidance about version, or maybe call out an example?
of when version's identifying versus when it's not identifying. I think…
**Dmitrii Anoshin (Splunk Inc.)** 14:07 It doesn't make sense to me to have specific guidelines for the version itself, it's just, like, we… we have a definition for the… Identifying attributes, if we have some.
So… Guidelines for those, and this is one of the attributes that we… thing can be identified or not, and it should be dependent on the use case.
I think… Oh, they're entertaining.
**Josh Suereth (Google LLC)** 14:33 Hold on, that's… that's actually just the comment here, isn't it?
Is this the same 4265 yet?
I think… The reason I think we add… we add specifically for version is because it's come up so often that it confuses people.
**Dmitrii Anoshin (Splunk Inc.)** 15:01 Yeah, that's fine, okay.
**Josh Suereth (Google LLC)** 15:02 Like, I agree with you, Dmitrii, we should just have general, like, what identifying, what non-identified means. What I'm proposing is, like, we just specifically call out version.
As a… as a thing.
Because I think in this change, no version became identified, they're all descriptive.
I'm just taking a look at, like, the Heroku one.
Yeah.
So… So I agree with you, like, it… Lyudmila came to the right answer based on what our guide already covers.
this probably needs to get cleaned up or discussed in some fashion of, like, why this is identifying, so that we don't confuse people. But yeah, I just think it'd be… it'd be helpful to have, you know, non-normative language that helps describe, like, how we look at versions, so people know whether it should be identity or not. That's all.
**Dmitrii Anoshin (Splunk Inc.)** 15:56 Okay.
**Josh Suereth (Google LLC)** 16:00 I can… I can try to take a crack at this if no one else has time or… or… Interests, but this, yeah, there's a… there's a thread on SEMConv today as well, like, in the, I mean, that happens an hour before this?
where we walked through a bunch of PRs that Lyudmila had around moving to V2. For context, every single entity in SEMCOV will now have identifying attributes defined.
Because it's a requirement for us to move to the V2 schema, since we actually made it now a hard blocker, that you cannot have an entity without identifying attributes defined on it.
Those entities are still not stable, so, like, they could still break, people can still change them, but every single entity defined in SEMCOMF, has identified attributes. Things that looked weird are now what we call these public attribute groups.
So that's why this is kind of hitting the head, is people are running into questions and, looking for guidance from us. Okay. I think I agree with… I agree with what you said, Dmitrii, and I kind of agree with Nathan here on this thing.
But I'd have to look at, do you know why Container Runtime has a version as identifying?
**Dmitrii Anoshin (Splunk Inc.)** 17:14 Hmm, no, I don't know.
**Josh Suereth (Google LLC)** 17:17 Alright, let's take a quick gander at it before we… Call this topic.
Where's Container?
We have… so what do we have as identifying? We have container ID.
**Dmitrii Anoshin (Splunk Inc.)** 17:38 But it's container and container itself, when it runtime.
**Josh Suereth (Google LLC)** 17:42 Oh, it's the runtime. Yeah, so the runner… the runtime is a description, a name.
And a version, I see. So they're saying that if you install a new version of Docker, it's a different runtime.
**Dmitrii Anoshin (Splunk Inc.)** 17:55 Okay, that makes sense. That pretty much, follows what I was assuming.
If you have name which doesn't change across the revision… revisions, you need to add version 2.
**Josh Suereth (Google LLC)** 18:09 Because you want to track which revision was doing something so you can aggregate at that level. Gotcha.
Yeah.
We should… we should actually probably change the brief here to say the versioned runtime.
Or the runtime and its version being used to run the container.
Then that… that means there's no question, right?
Of what you've modeled here.
**Dmitrii Anoshin (Splunk Inc.)** 18:30 Probably.
I guess it's similar. Let's think about Docker image, right?
a version of an image is an important part of a Docker. You never think of a Docker image as Without aversion, right?
**Josh Suereth (Google LLC)** 18:46 Yeah, but for a Docker image, though, we… is the ID the version? I guess it is.
**Dmitrii Anoshin (Splunk Inc.)** 18:51 Should be, yeah. It should just include in that case.
**Josh Suereth (Google LLC)** 18:56 Because it's almost like the GitHub SHA, right? Because you can have a tag, which would be like V1, V2, and the tag we have here, which is descriptive, but there is an actual ID, which is like the unique SHA of the Docker container image, right?
So… Okay.
So, but again, that's because for a container image, we have a unique ID that represents, like, the version… Yeah, but the other thing is those tags can change. I don't know if you've… I'm kind of annoyed by this personally, but where Docker, like, V1, right, where you publish new images against that V1 tag, and so you actually have different versions, so tracking by ID, I think, is the right thing, because you might have different vulnerabilities and that kind of crap.
**Dmitrii Anoshin (Splunk Inc.)** 19:44 Makes sense, yeah. Cool.
**Josh Suereth (Google LLC)** 19:46 Yeah, so I think that that is in line with what… like, using ID here is in line with having both name and version here.
**Dmitrii Anoshin (Splunk Inc.)** 19:53 Huh?
Okay, thanks.
**Josh Suereth (Google LLC)** 19:55 Alright, cool.
**krajo (Grafana Labs)** 19:57 Just one question. So, but then, if you are going to, you know, explain this in the note or whatever, in the not normative language, you're going to go back to the same thing that the, you know, it already says, that it depends.
**Josh Suereth (Google LLC)** 20:14 Yes.
**krajo (Grafana Labs)** 20:15 Yeah, I understand why you want to do it, it's just to stop people asking, yeah, so…
**Josh Suereth (Google LLC)** 20:20 Well, we're gonna make it apparent why sometimes it's in and sometimes it's out, right? So, like, the idea would be, where do we have our…
**krajo (Grafana Labs)** 20:27 Yeah, I get it, I get it.
I'm supporting.
**Josh Suereth (Google LLC)** 20:30 docs now? How to write… yeah, here it is.
Resources and Entities. Yeah, so in here, where we talk about how to define identified attributes, multi-observer guidance, what we have here, I think, is sufficient. What we can add after multi-observer guidance is we can add, like, a, you know, what to do with version, and talk about, like, you know, version might need to be identifying if you're modeling like this, and it doesn't need to be identifying if you're doing it like that, kind of a thing.
**krajo (Grafana Labs)** 21:01 Yep.
**Josh Suereth (Google LLC)** 21:02 Okay.
That was what I was planning to do.
Cool.
Alright, let's come back to… here.
So… That's version ID.
occurrence.
Funneling with her shit.
Thank God. They're sorry.
Identifying and not.
So, okay, and choice.
Meetings… True.
Work.
Priority… clarity.
put the modeling documents. Okay.
Alright, next, Dmitrii, do you want to take it away, or I can present your PR?
**Dmitrii Anoshin (Splunk Inc.)** 21:49 Yeah, you can present. I haven't made a lot of updates. The reason is that… You, you, you said that we want examples, but I… I run into issues that we don't have enough entities to… create a compelling example, essentially. So, we already have… we already have, some example there. And it's, like, minimal, and I guess it's enough, because you mentioned that we might have a process within container, within, like, hypervisor VM, and everything. We don't have… few of them, and if we go from process to container, it's already kind of… we're done at that point, it's already global. So I just replied to a few Comments, and added, like, addressed one of your comments that require… that needed some note.
And, interestingly discussion, I'm not sure when… Tomo… where… they're coming from, like, the pushback… I don't understand the pushback, essentially.
They're working on… Boss… I understand that.
And as far as I get it, it… matches, it helps, but it… I don't understand the pushback to guys. That's…
**Josh Suereth (Google LLC)** 23:13 Yeah, you can, you can talk to us in the maintenance group. This, this also happened with, other fast things.
I can read this comment and push back. That's kind of somewhat common with a lot of that feedback.
if it… if the feedback makes sense and is good, like, let's incorporate it. If not, like, feel free to push back.
Yeah, fast… Trying to understand what this means.
**Dmitrii Anoshin (Splunk Inc.)** 23:40 Same thing, I'm… I'm a little bit confused.
**Josh Suereth (Google LLC)** 23:44 We can't indicate which refinement of that entity… oh, this is about entity refinements, which kind of aren't really a thing.
**Dmitrii Anoshin (Splunk Inc.)** 23:52 Yeah, and I also looked into the refinance, and you've seen, apparently, I didn't even know about that, but… It doesn't create new entities.
No. Somewhere. And that's… yeah.
Go ahead.
**Josh Suereth (Google LLC)** 24:08 Yeah, yeah, so do you know what refinments are in Weaver in general?
**Dmitrii Anoshin (Splunk Inc.)** 24:13 Yeah, I got it. I got the idea, yes.
**Josh Suereth (Google LLC)** 24:15 Yeah, but so by definition, what that means is a refinement lets you automatically generate code for AWS where any of the optional attributes don't get filled out.
for the FAS identity, That are only needed for other… implementations, right? So if I have, like, a GCP Cloud Run, AWS Lambda instrumentation, and Knative instrumentation, right? I might have refinements for each one, and the refinements will get rid of attributes that I can't fill out from where I am, or it might have documentation that's specific to tell you exactly what the GCP thing is, or how to get the GCP, you know, attribute.
**Dmitrii Anoshin (Splunk Inc.)** 24:55 Yeah.
**Josh Suereth (Google LLC)** 24:55 So, refinements are really specifically tied… like, the idea is you can take the generic thing, and then you can document very specifically, on GCP it looks like this, on AWS it looks like this, on Azure it looks like this, on Alibaba it looks like that. You know, on, your homegrown system, you could make your own refinement and, like, optimize So that's what a refinement is. It's not a new entity.
**Dmitrii Anoshin (Splunk Inc.)** 25:16 Yeah, I get that. I'm wondering, like, should we allow, in that case, overriding… we don't allow overriding identified attributes in refinements.
But do… because we don't change type, if we want… if we… if we were to change type, then we can override them. But what about, Identity… I guess that one should be overridable in the requirements in that case.
**Josh Suereth (Google LLC)** 25:45 We don't allow you to override identity.
**Dmitrii Anoshin (Splunk Inc.)** 25:47 Sorry, not identity. I'm sorry, I meant scope, I meant scope. Because let's say one… in one environment, identity would be global.
like, based on the values, right? The values would be generated globally. And another one, it can be only unique within, let's say, cloud.
So we… let's put it this way. One cloud generate host ID globally unique, another cloud generate host ID only within, like, availabilities only.
**Josh Suereth (Google LLC)** 26:21 a regener of billboards.
**Dmitrii Anoshin (Splunk Inc.)** 26:22 Region, yeah, yeah.
**Josh Suereth (Google LLC)** 26:25 I think we… we actually… Google might be in that scenario. I think there's some IDs that we have for VMs that are only unique Guaranteed in a… Availability zone. But everyone treats them as if they're global, because they don't read the docs, so then they get surprised.
**Dmitrii Anoshin (Splunk Inc.)** 26:42 Right. So I made that assumption, and I replied to this comment with this assumption that we will need to make that change to viewer, and I think I can… It's not even blocking, right? It's kind of whether we do that or we don't do that, but I don't believe it's a blocker for this PR, so…
**Josh Suereth (Google LLC)** 27:04 No.
I… and that… this is something we have to decide. I can see… this goes into one of my comments, I think I had that somewhere as well, about, like.
Can we have, for the same entity, a different outer scope, right?
Yes.
**Dmitrii Anoshin (Splunk Inc.)** 27:20 And that should be allowed. In semantic conventions, I think we should specify whether it's global or local, but maybe, like, we can specify options, essentially, and that's where I think refinements could be pretty handy. So, we can say that… One process can be part of the host, or it can be part of the container in that case.
**Josh Suereth (Google LLC)** 27:46 Yeah, so the baseline thing would basically allow anything that a refinement might need, and then a refinement could say, actually, I'm always global, or I'm always local.
**Dmitrii Anoshin (Splunk Inc.)** 27:56 Yeah.
**Josh Suereth (Google LLC)** 27:56 That makes sense to me. That would help with hosts, too, because you could make, like, a, you know, AWS-specific host one that uses the ARN.
That is global, right? Arms are globally unique, right?
**Dmitrii Anoshin (Splunk Inc.)** 28:12 Irelands are globally unique, yes.
**Josh Suereth (Google LLC)** 28:14 Okay.
Yeah.
Alright, and then… I think this one's answered, right?
**Dmitrii Anoshin (Splunk Inc.)** 28:32 Yeah, it looks like.
**Josh Suereth (Google LLC)** 28:33 Oh, this is specifically around DPE. There's a lot of good DPE questions.
And then you added some examples at the bottom, is that… Do I need to…
**Dmitrii Anoshin (Splunk Inc.)** 28:46 I already had some examples. Yes, this one, I mean…
**Josh Suereth (Google LLC)** 28:53 Yeah, let me render it so I can actually view it, I cannot read Markdown tables, you know what I mean?
**Dmitrii Anoshin (Splunk Inc.)** 29:00 Makes sense.
**Josh Suereth (Google LLC)** 29:01 Come on.
Right, this, this here, right?
**Dmitrii Anoshin (Splunk Inc.)** 29:07 Yes.
**Josh Suereth (Google LLC)** 29:08 Okay.
So, container ID is global, because the ID should be globally unique.
Host ID… ID scope is global when host ID is machine ID, local when… Cloud. So this is kind of what we'd write in SEMCOM, and then you think we'd use refinements to be able to say, okay, this one is global and this one is local?
**Dmitrii Anoshin (Splunk Inc.)** 29:27 Yeah, I think so.
**Josh Suereth (Google LLC)** 29:30 Okay.
Global, global, makes sense.
Local within Kate's pod, that makes sense as well. Logan service. Okay. Yeah, this is looking good to me. How many approvals do we have on this so far?
Is it just… just me?
**Dmitrii Anoshin (Splunk Inc.)** 29:50 do, yeah.
**Josh Suereth (Google LLC)** 29:51 Okay, Let's… let's advertise this a bit in spec, because I think this involves changes to Weaver, which I'm happy to help make happen.
And it involves changes to the proto.
Yes.
**Dmitrii Anoshin (Splunk Inc.)** 30:05 And I have PR for… I have a PR for Proto, it's simple, maybe I can submit an issue for Viva if you want to, or… Yeah, actually.
**Josh Suereth (Google LLC)** 30:14 Open an issue so we can track it. We are about to stabilize the V2, like, state schema.
So we just have to decide if we're going to consider that a blocker for stabilizing V2, or if we think we can add it as a non-breaking change later.
**Dmitrii Anoshin (Splunk Inc.)** 30:31 Makes sense.
**Josh Suereth (Google LLC)** 30:32 Yeah. So if… here's a question for you.
For the Weaver side, if we want to add it as a non-breaking change, what that means is there'd be a default for all existing Entities for how to treat their scope, and what their scope is. So, should we default… I think you already implicitly have this in the way you wrote the data model document. The default is unknown, right?
**Dmitrii Anoshin (Splunk Inc.)** 30:58 Yes, unspecified, yes. And it's gonna be default for the proto as well.
**Josh Suereth (Google LLC)** 31:05 Yeah.
And so, then, unless you provide a scope, you don't need a default. So we don't really need to have force people to have a scope defined yet, it just means it's unspecified. But we should probably have a program to go in and give everyone scope.
**Dmitrii Anoshin (Splunk Inc.)** 31:19 Adjustment.
**Josh Suereth (Google LLC)** 31:22 That's reasonable to me.
**krajo (Grafana Labs)** 31:24 Just a wrong question. So, if you put for example, global scope into the semantic commercials.
Will that restrict people implementing things?
Meaning that… Somebody wants to implement some new convention, or a new product, or whatever, and they say, it must be global, and then they… Like, maybe stuck, saying, you know, I cannot generate something global. Then… They will create their own.
thing and will not follow the 70 Convention, or is it the case that Global will be just in the center of motion, kind of a… Suggestion, and then you can still do local.
**Josh Suereth (Google LLC)** 32:08 I think if we put it in CENCOM, it's going to be part of your CENCOM conformance score, so you'll be dinged and say that you're not semantic convention compatible. If you don't provide… like, if we say this has to be global, and you don't provide a global, then we… you'd get dinged. But, I… I, you know, for things, like, where there's any kind of flexibility, we're going to say in SEMCOM that it could be any, you know what I mean? Like, there'll be…
**krajo (Grafana Labs)** 32:34 Okay.
**Josh Suereth (Google LLC)** 32:35 Like, I think… so, the proto will say it's either global, local, or unspecified. SEMConv would be unspecified, global, local, or global, or local, as an option, right? Like, and any option, so that you can, we can be flexible. Like, host ID, for example, which I think is… am I… am I… That'll take me a while to get there. Host ID could be global or local, we don't know. And we're gonna let you provide either, so in SEMConv, we'll just put that as any, you know?
**krajo (Grafana Labs)** 33:05 Okay.
**Josh Suereth (Google LLC)** 33:09 Cool.
Yeah, so Dmitrii, if you… since… since KubeCon's coming up, I know everyone's gonna be slightly distracted, but let's see if we can get some attention on this, for, For tomorrow's, spec meeting. Sound good?
**Dmitrii Anoshin (Splunk Inc.)** 33:26 Sure, you want me to join and present that, or… Not sure, I'll probably have a… Something else.
**Josh Suereth (Google LLC)** 33:35 If you're not available at that time, I can present it. That's fine.
**Dmitrii Anoshin (Splunk Inc.)** 33:38 Okay. Yeah, I can join tomorrow, I can join.
**Josh Suereth (Google LLC)** 33:40 Okay.
Cool. I don't know if you guys saw, by the way, the spec meeting is doing this rotating, what do they call it? Spotlight or something? No, what do they call it?
Anybody remember? To, like, focus on different SIGs and have them tell you about their roadmap and what they're up to?
**Dmitrii Anoshin (Splunk Inc.)** 34:02 Interesting.
**Josh Suereth (Google LLC)** 34:03 Yeah. So, at some point, we probably want to be on the queue, but…
**Dmitrii Anoshin (Splunk Inc.)** 34:08 I see.
**Josh Suereth (Google LLC)** 34:11 Alright, let's go back to our… agenda. My own… Okay.
Kidding.
It's good. Please review.
On top of that aspect, Okay, so I think this is… I want to hold off on any other… I want to hold off on more prototyping work until this lands, because this will impact both the proto and some more prototypes. But I did want to do a quick check, since, Dan's here. How's the JavaScript prototype going?
**Daniel Dyla (Dynatrace)** 34:53 I have not touched the JavaScript prototype in… Couple of weeks, at least.
It is… Man, trying to… I'm struggling to remember.
I think it's mostly up-to-date. There was one change… That we made during… Yeah, I don't even want to guess. It is not quite up-to-date, but it's very close.
**Josh Suereth (Google LLC)** 35:23 Okay.
Okay.
the Java one's out, getting feedback, and then, I haven't had a chance to talk to David Ashbel about the Go side. He's been a bit more focused on stable by default, and I don't know if you saw, he has an OTEP with a whole bunch of experiments for all the SDKs for stable by default. I… I would recommend, actually, Dan, to take a look at that as a JavaScript maintainer, because I think that's, Possibly more urgent than what we're doing.
also, like, I wish it had come out last year around this time, but it's what it is.
If I take a look at that one. So, in terms of the Go one, I think we're looking for, a helper.
Right?
Either that, or I need to suck it up and stop doing some of the Weaver work I'm doing and work on Go, which might come relatively soon.
once Weaver… 2.0 is stabilized, or sorry, Weaver 1.0, it comes out, with the version 2 of semantic conventions, and all of the federated SEMCOM work lands, so we're actually pretty close to that. I was hoping to have a lot of that done before KubeCon.
As always, didn't quite make it.
So… Okay.
Anyone here have, like, would have time or interest in picking up the Go prototype and adding Entities to the Go SDK?
**Daniel Dyla (Dynatrace)** 37:03 I'd love to volunteer for this, I just can't.
Hey.
But I barely have enough time to do the things that I already have promised to do.
**Josh Suereth (Google LLC)** 37:15 I would throw tokens at this, but my problem is I know Go well enough that I would have to really spend a lot of my time and attention to make sure that I got good code out. It's not like it's Java or Rust, where I can just throw tokens at it and be like, no, this is BS, and throw it away.
I would probably end up with something horrible and inflicted onto the world, and I wouldn't have time to pay attention. So, I don't think, for me, this is a token thing. I think I actually need to spend time on it.
Okay.
Cool. Well, I'll leave and need help here. Alright, I think that's it for the agenda. In terms of next steps, is once Dmitri's PR lands, I think we can start, really working on getting the prototypes out, and trying to land the spec, and getting some feedback.
I have not heard from the Java maintainers whether or not there are any, like, major problems with our current implementation, which actually makes me really happy, because I think if entities were going to break the world, and people would complain, and they'd have to revert the change, they would have told us by now.
Since it's been in, what, 2 releases at this point?
So, the notion that we can add entities in a non-breaking way, I'm pretty confident in, because that's not a small ecosystem. I would like to see it in at least one other SDK, though.
So… Cool.
Alright, I hope you all have fun who are going to QCon. Good to see everybody, and no meeting next week.
**Dmitrii Anoshin (Splunk Inc.)** 38:50 Yeah, I need to tell you some… tell you something. So, I'm, leaving Splunk, and, I likely will not be, you know, Dell anymore as well, so it's… that's uncertain, yeah, maybe I'll be able to spend some time, but I'm sure.
I'll be at KubeCon, I'll join one call after that, but since that, I'll be… I'll be out. And whenever I… I… if it's possible for me to stay at the hotel, I'll join, but likely will not, so… And from… from our side, from Splunk, there will be… one… My colleague from my team, Gina, she's pretty good, she's, like, Kubernetes expert.
And she might be able to help with implementation in the collector. She is, enthusiastic about it, and she already did some, like, investigation, like, she worked on some related things to Entities, so she'll be able to help on the collector side, at least.
**Josh Suereth (Google LLC)** 39:48 Okay. Wow. I guess if you're saying this on a recorded meeting, you're okay sharing.
**Dmitrii Anoshin (Splunk Inc.)** 39:54 Yeah, it's… it's a public calendar.
**Josh Suereth (Google LLC)** 39:57 Yeah.
Where are you going, man? Anywhere fun?
**Dmitrii Anoshin (Splunk Inc.)** 40:00 It's… it's an AI startup.
**Josh Suereth (Google LLC)** 40:04 Nice.
**Dmitrii Anoshin (Splunk Inc.)** 40:06 I live in the Bay Area.
**Josh Suereth (Google LLC)** 40:08 Yeah, that's fun.
**Dmitrii Anoshin (Splunk Inc.)** 40:10 I should try that.
**Josh Suereth (Google LLC)** 40:11 Is it still Dark Launch Startup, or can you tell us what you're actually going to be doing? I'm just curious.
**Dmitrii Anoshin (Splunk Inc.)** 40:16 It's, it's Resolve AI, have you heard about it?
**Josh Suereth (Google LLC)** 40:20 That sounds super freaking familiar, yeah. What… go ahead.
**Dmitrii Anoshin (Splunk Inc.)** 40:23 It's AIRE.
Okay.
**Josh Suereth (Google LLC)** 40:26 Okay, I think I have heard of that, yeah.
**Dmitrii Anoshin (Splunk Inc.)** 40:29 Yeah.
**Josh Suereth (Google LLC)** 40:29 Interesting, Ben. Okay. So, kind of related to what you're doing, but completely different.
**Dmitrii Anoshin (Splunk Inc.)** 40:34 Related, yes. Related with… like, I can apply a lot of expertise, but I'm not sure if it will be, A lot of observability side, yeah.
**Josh Suereth (Google LLC)** 40:44 If your AI bots can't figure out what machine is broken, you know who to talk to.
**Dmitrii Anoshin (Splunk Inc.)** 40:50 Exactly.
Yeah, it was great working with you, like, this, Entities SQ was one of my favorite.
**Josh Suereth (Google LLC)** 41:00 Okay.
**Dmitrii Anoshin (Splunk Inc.)** 41:01 Part of the whole work.
**Josh Suereth (Google LLC)** 41:03 Sure.
Man, oh, now I'm really sad I'm not going to be at QCon to… because I assume you might be going to different conferences in the future.
**Dmitrii Anoshin (Splunk Inc.)** 41:13 Maybe, yeah. We'll see. But still, like, it's, industry is not that big. Maybe we'll… Sure. We'll meet somewhere.
**Josh Suereth (Google LLC)** 41:23 True, well, best of luck, and yeah, We'll… we'll have to do some kind of virtual send-off next week. Or, not next week, but the week after. Yeah.
Yeah, okay.
**Dmitrii Anoshin (Splunk Inc.)** 41:34 Cool.
**Josh Suereth (Google LLC)** 41:35 Cool. Good luck, man.
**Dmitrii Anoshin (Splunk Inc.)** 41:36 Thank you, thank you, folks.
**Josh Suereth (Google LLC)** 41:39 Great to see y'all.
**Dmitrii Anoshin (Splunk Inc.)** 41:40 Sure, bye.
