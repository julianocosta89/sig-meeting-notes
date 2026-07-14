SIG: Semantic Convention SIG
Date: 2026-07-13
Duration: 68 minutes
============================================================

## Zoom Recording Transcript

Michele Mancioppi 00:09:00 Hello!
Josh Suereth 00:10:00 Hey, everybody.
How are we all doing?
Kathie Huang 00:10:05 Good, how are you?
Christophe Kamphaus 00:10:07 Why not you?
Josh Suereth 00:10:09 Not bad, not bad. I do have a, stop about 30 minutes in, so I was thinking, there's two topics, Lavilla has the one, she's not here yet, but I'll, I'll get it started, and then, We can see how things go. It's a Happy Monday!
For some the morning, for some the evening.
Where's my present? Let's see.
Okay.
All right.
Azure Container App Replica VR. Let's start with this, get into V2, and we'll do triage after. Sound good?
Kathy, do you want to kick us off with this? Pr.
Kathie Huang 00:10:54 Yeah, sure. First of all, this PR got closed automatically because there's no Azure SIG group. So I was wondering if this PR could get another look at, but some people did review it. But essentially, it adds semantic conventions for Azure Container Apps replica name and revision ID.
for the replica name that arose out of but… realizing that the go resource detector SDK automatically populates the service instance ID resource attribute. So we had to use a separate Azure container app instance ID attribute to identify the replica of an Azure container app.
But then someone suggested also adding revision id to track different revisions of an azure container app where you can think of like a replica as an instance.
And so that sparked a longer discussion down below where we were discussing what would be like the identifying attribute of the azure container app entity. Yes, that one up there. There's a couple of comments from the Github bought about the PR getting closed, but… Basically, like the… we're using the revision as an attribute of the Azure Container App entity, but, I guess apparently we need an identi… a role identifier for the Azure Container App entity, and we were discussing if the revision ID would be appropriate to use as the identifier. And then I looked at a couple other, like, precedents, like.
Kubernetes, AWS, and GCP, but, I learned that the AWS and GCP, precedents are, in dev mode, they're, like, legacy, so, it doesn't quite make sense to follow what they're doing, which what they're doing is they don't have an identifying role. So I was going to just drop that role. So Yeah, and I think Thompson suggested using the or we were thinking about using the azure container app name as the identifier. But the resource detector is using service instance name as the identifier, and I was wondering if that would be appropriate to use as the identifying role for the azure container app entity, since That's an attribute from a different entity.
Josh Suereth 00:13:25 So I think there's, there's a few things here to kind of figure out. So one is, your, we're doing an entity design here, which I think means folks who are familiar with Azure. I can speak on behalf of GCP. I think Trask is here. I think I saw you on the thing, so I'm going to call you out for Azure. Let's take that independently of, like, the process of getting this approved and things.
I… I'll… I'll ask quickly, like, for Azure specifically, does it make sense for us to get a set of folks who own the Azure namespace so that we can make changes and update these things? for context, I've been trying to organize the same thing for GCP, internally, but, I think… I think… that might make sense. You're doing the right thing by escalating a PR here. We have a process for Making changes to something where a change is needed. Where there is the sick So this is the right thing to do. One of the some kind of maintainers can reopen your pull request. Getting it past the auto close phase.
So I just wanted to, like, call out, you know, process things first. Then in terms of how to design entities, we can talk through that. I do want to take a quick look, but I'm gonna first ask Trask I'm gonna call you out, or anyone from Microsoft, or who works on Azure. What's your thinking on this? Like, it does sound like instance and Azure, or, revision need to exist.
I'll let you take it away.
Trask Stalnaker 00:14:59 Yeah, so, Kathy had submitted a previous PR, that also for Azure, a couple of Azure, attributes, and, you know, went through the same thing of getting auto-closed, and we got it reopened, and… Did end up merging that, under… without a group.
With the idea just that there was a couple of basic things that made sense to add.
I can definitely… see if that's something that we can do. I like the… I mean, I do like the idea of… the… each of these cloud providers having… I mean, they are important conventions, and if we can have groups From them that can support that.
It is a hard thing, I think, for our… Unless it's obvious, it's hard for the general SEMCON folks to support it.
on their own.
Yeah, I'.
Kathie Huang 00:16:16 Excellent.
Trask Stalnaker 00:16:17 I can definitely look at this specific one and see if it's something that I feel we can move forward.
without that group, but Josh, I like the idea of, maybe we can… Try to coordinate a, A cloud provider, semconf, SIG…
Josh Suereth 00:16:46 At least get a set of owners, so that these things don't get auto-closed, and there's a set of people reviewing, yeah. Lewis, you've had.
Lewis Lewis 00:16:54 I wanted to say hi. I work with Kathy. I am here to talk about another 3 Azure providers. If that adds any urgency to starting a group, and I would be happy to support this in some way, if I can.
Josh Suereth 00:17:06 I don't That absolutely does. That's a good data point. Yeah.
Okay, so, so… To answer first question, like, yeah, the first question I asked was, it sounds like we should probably get together, some set of owners around Azure, so we can, like, move these changes through quickly, or, you know, have the right set of folks discussing these. Regarding entities, I was going to take a quick crack at kind of describing the goal of entities. I don't know if you've seen, like, the design of entities in OpenTelemetry and how they're changing resource and things.
Generally, we expect… like, service and service instance to have a… is a relationship with cloud-based things, so you wouldn't reuse service instance ID, right? You would have an independent cloud identity, and then the service would… is it like a layer on top of?
the cloud identity. So, like, I can have a service and declare it and have a service name with instances. Those instances might run on Azure, they might run on-prem, they might run somewhere else, right? Maybe I use a namespace with service to, like, figure those things out, but you don't… Like, I wouldn't reuse service instance ID. I don't think that's, necessarily in line.
we have this thing with, with entities where, particularly with OpenTelemetry, right, you might have a, A thing that's reporting about itself?
you know, I'm running inside of Azure, and then Azure has some sort of asset inventory thing that tells you about, like, all the assets in Azure or its API, kind of like VMware has vSphere, you know, and I have a thing that can describe all these and their relationships. So, entities is about those relationships and being able to untangle them.
So the important thing here is not necessarily… like, when we pick identifying attribute.
The important thing is so that when I need to look at those relationships, I can identify something, I can identify where they're the same.
It's not as rigid as I think some of the comments are making it.
And you have a lot of flexibility here, right? So, the thing I always encourage when we ask these questions is just Think about the use case that you're trying to provide, and think about what gives the best observability experience.
It… it doesn't mean… like, when we say these have to be unique and identifying, that doesn't mean that, anytime any change happens to an Azure resource, I have to have a unique ID.
outside of what Azure provides. If Azure gives me an ID that it expects to be unique, and that's what's used in all the Azure websites and things, that's your ID. Don't make something new. Don't use something different, right? That's how people identify stuff in Azure. And I think what you have here is the thing… like, if I were to go to Azure's you know, dashboards or API, and ask a question about a container app.
is revision the way that I'm going to find out about something? Is instance the way I find out about it? Like, it… Is it both?
You know?
So that's… that's how I would start answering the question. I actually don't know, because I don't use Azure, so apologies, but, that… that's how I'd answer this question of, like, do you need something different? Do you need something that is not identified? My suspicion, given what I know about, like, Cloud Run, we… we would put both instance ID and revision in an identifying… like, both of them would be identifying attributes together, and you'd provide both.
So, like, Cloud Run revision is the… I can show you what GCP does outside of OTEL, but the way we do identifying attributes for Cloud Run is we put both of them together.
they're both required, and then they make an identified thing. So I don't know if that helps or not, but… but I'm hopefully giving you the tools you need to answer the questions and push back on some of this feedback you're getting.
Kathie Huang 00:21:03 Gotcha. Thank you so much. That helps a lot. Yeah, having both be identifying definitely makes sense and gives a more holistic view of the entity itself. But yeah, I'll look forward to any reviews coming up and I'll revise the PR a little bit with that information.
What's the process of, like, getting together in SIG for Azure? Like, what would the next steps be for that?
Do we have enough people to.
Josh Suereth 00:21:32 That's generally what the next step is, is we have this PR that you make where you put all the people who are interested, and then we look at that and say, is this a healthy amount of people or not?
That's what the process is meant to be. It is… it is a little bit heavyweight, Travis, I'm going to call you out again since you're a governance committee fellow.
Trask Stalnaker 00:21:51 Yeah, yeah, I'm looking for…
Josh Suereth 00:21:54 Yeah, do we have something lighter weight, or do you think doing a proposal, project proposal, is the right next step here?
Trask Stalnaker 00:22:01 I think it depends on if we want to do, like, a cloud provider SIG, and try to combine those.
Or if we just want to kind of… do a… You know, one-off for… an Azure group.
Of people, code owners.
I think… Both would be… Okay.
Lewis Lewis 00:22:34 It sounds like cloud providers would have a healthier number of people and could be, I don't know, further split if it needed to be.
Trask Stalnaker 00:22:44 Yeah, I, I also think the cloud, like.
We would learn a lot from each other, and it would be nice to have some consistency across them, so that… would be nice.
Josh Suereth 00:22:59 All right, so then the next step is probably we make a proposal for cloud provider.
We describe what the scope that we want to tackle is, which I think is just, modeling all of the cloud provider resources that we know exist today.
And then eliciting time for, like, Alibaba, for AWS, for GCP, for Azure, to, like, bring people in, you know? Sorry, and their users. I should not say that it's just them, right? To come in to, like, get an expert group that we put together.
But the hardest thing generally for these is to pick a scope that everyone's happy with. That's where I think you'll get all the nitpicking. So if you have a set of things you absolutely want to make sure get done, I would list those first in the scope, or I'm gonna propose this, because I think this is more work on possibly Trask and, like, those of us that are maintainers, Keep making your changes through this, this exception process for now.
while we try to build out the cloud group. I think that… that's probably the right thing to do.
Kathie Huang 00:24:01 Gotcha. That makes sense. Thanks Appreciate it.
the time.
Trask Stalnaker 00:24:09 Yeah, thanks for pushing on this.
It's a good topic.
Kathie Huang 00:24:13 Thanks.
Josh Suereth 00:24:20 Alright, I'm gonna type up the notes of what we said out loud, and then, Ludmilla, do you wanna kick off V2 migration discussion?
Liudmila Molkova 00:24:32 Yeah, finish typing and done.
Either stop sharing or open the issue.
Josh Suereth 00:24:43 Opening the issue.
Liudmila Molkova 00:24:44 Thank you.
Yeah, so we've got a good discussion last time, on V2 migration.
And we decided, okay, that we will first migrate the output.
And then we will migrate the definitions.
I've been, there are some tricky places there.
And it sounds like there are a couple of small caveats here.
I… First is some of the.
Things, cannot be expressed as we want properly. So, for example, oh, sorry, some of the things cannot be Converted to V2 later. It's better to separate them. So for example.
In messaging, we define attribute groups, we don't define spans.
Really, maybe we define something, but mostly groups.
And in order to migrate things properly.
We kinda have to convert them to proper spends and spend refinements.
And we can do this before we convert outputs.
I'm… like, 90% confident it should work. I didn't try that part yet. I've tried the one for hardware, where we use metric and metric refinements.
And it should work pretty well.
And there is FAS, which has the same problem of attribute groups instead of spans.
This don't need anything, but there is a interesting case of ZOS entities which have refinements for host entity.
And we currently doesn't really work.
I have a PR here.
To make it work?
But it's kind of blocked right now.
It's a it's a stack of 3 PRs, actually. This is the middle of them, but it unblocks the.
The first… the… And, refined entities in… Multi-registry.
Okay, so I'm thinking all of these things can and should probably happen before we do the templates.
But we can also split templates into parts. The one One would update registry, and the other one would update the update markdown.
And… I it probably doesn't matter. It's just that the amount of changes, like, if I take I I've been playing with it, and the full list of changes is around 300 files.
And it's impossible to review and it contains substantial things. So if we do the updates of YAMLs independently, we'll have much easier time otherwise.
Yeah, so the…
Josh Suereth 00:28:11 The entities thing is interesting.
Are they doing refinements in a way that violates the entity model?
Or are these refined, like, are they just, is it actually a refinement of ID or are they changing the ID significantly? Because that would break entities if you actually add attributes to identity for the same host ID, right?
Liudmila Molkova 00:28:32 Yeah, so I think this is a pure refinement, but everywhere where we… Do.
where we didn't have refinements. We kind of have to… we didn't… we missed some parts, so, Rudiger is here. We can actually take a look, at ZOS, Entities, but I'm thinking like was the missing feature in Weaver, I think, that I'm proposing, is that we're allowed to refine The attributes within identity.
and description, but don't modify the list of attributes itself.
Josh Suereth 00:29:14 Yeah, that makes sense. So basically, you can change the description, but you can't actually change the name or which ones are there.
Liudmila Molkova 00:29:21 Right. You can add to description.
Josh Suereth 00:29:30 Yep. Okay.
I'm, Rudiger, I don't know if you want to say anything about what you guys are doing. I'm trying to pull up on a different tab, the… the definition, just so we can take a quick look.
Ruediger Schulze (IBM) 00:29:41 Yeah, I think what we did there with the host ID or with one of the IDs was that we gave a different description.
In terms of what the COS value should be?
So… Possibly.
Josh Suereth 00:30:01 Yeah, where… where is your, the host one that you guys have defined? Is that… is it in-host, or is it somewhere else?
Ruediger Schulze (IBM) 00:30:09 Oh.
Josh Suereth 00:30:11 Increase.
Ruediger Schulze (IBM) 00:30:12 That's.
Liudmila Molkova 00:30:12 Then DocsRegistryEntityZOS.
Right.
Oops.
Josh Suereth 00:30:22 Interesting. See you.
So this, this is the definition though with Weaver, right?
Liudmila Molkova 00:30:32 Oh, sorry, this is, there's the.
Ruediger Schulze (IBM) 00:30:34 This is just a software.
and that supposedly, anyway, will go into the federated I mean, all these COS-related Definitions will go into the federated repository.
as we… as we go through this currently, so we would deprecate them. I'm not exactly sure what that would mean for… for the… for the V2 migration discussion, but, We would be moving them over into the federated repository.
Liudmila Molkova 00:31:10 Yeah, Josh, sorry, it's in the docs resources, ZOSMD, in the resources, not the entities.
Josh Suereth 00:31:19 Oh.
Liudmila Molkova 00:31:19 It's not an entity, yeah.
Josh Suereth 00:31:22 Oh, it's not an NCF, but we would need to make it one. I see what you.
Liudmila Molkova 00:31:26 Right, yeah, this one. So this is the, the first one is the same and then there is host.
Josh Suereth 00:31:37 I see, and it's just a… again, this is just… these are all things that are already on host, and this is just the refinement.
Ruediger Schulze (IBM) 00:31:43 Right.
Josh Suereth 00:31:44 Gotcha, gotcha.
Liudmila Molkova 00:31:47 Interesting, so this… the host ID is opt-in, I didn't notice it yet, but for… if it's an identity, it would have to be…
Josh Suereth 00:31:54 It has to be required, yeah.
They're also having discussions about host ID right now, because we… Don't know if we can actually consistently make an identifier for a host generically across any possible regime.
Which might be why you have an opt-in router, because, it's actually… identifying the machine is a really, really hard problem if you don't have an external thing to identify it.
and, you know, the… the folks, you know, working on Systems MConf basically don't think they have that. I don't know if any of them are here and want to talk about that more deeply, but, Yeah, that's currently the problem they're trying to resolve. So, we have an entity that needs a unique identifier so you can figure out what a host is, but you literally can't figure that out from the host itself.
So… we use proxies, right? We use, like, the AWS ARN, we use an Azure ID, we use a GCP ID to figure out what a host name is. We might use VMware vSphere and that kind of thing, but we, We don't have a generic way to do it And so, what does that mean for all of OpenTelemetry? That's one thing we're working on, but it doesn't mean that it wouldn't be required, it just means it takes more work for the user to figure out what the host ID to make this useful.
Good.
Ruediger Schulze (IBM) 00:33:19 We had similar discussions just to say this when we tried to put a reasonable value there.
Yeah, so…
Josh Suereth 00:33:32 Go ahead, Macall.
Michele Mancioppi 00:33:34 Oh, since we have people from Microsoft in the chat.
umm… Do you know, folks, that you're using a completely bespoke azure.resource.id?
That is 100% what cloud.resource_id should be.
This is the time for the that you export, and that I need to normalize on my side.
It would also help here, you know, because the, for example, the same value for host ID could be used for the cloud resource ID.
It would be a perfectly legitimate use case, for example, in AWS, to use also the value of the ARN for the host ID on EC2.
This remark of mine is meant by complete silence. I'll mute myself.
Trask Stalnaker 00:34:29 Yeah.
Josh Suereth 00:34:31 Go ahead.
Trask Stalnaker 00:34:32 Yeah. Can you open an issue?
Michele Mancioppi 00:34:36 Yes, but where? Because the problem is the data that is coming out of Azure Monitoring Service.
It's, it's telemetry that is streamed, I think, about, from… I can look it up, but it's not auto.
Trask Stalnaker 00:34:54 Okay, you can DM me. I need more context.
Michele Mancioppi 00:34:59 Will do.
Josh Suereth 00:35:10 Okay.
Alright, so, for this one specifically, I think, Supporting entity refinement where the identity basically can't be touched, but description can be… description of an attribute on an identity could be changed, makes sense to me.
We just need to make sure we don't break the entity model Yeah, okay, and… and so that's… that's what that one is. Cool. Was there anything else here? I have to drop in 3 minutes, so apologies. Was there anything else? So… so feel free to take over presenting. Is there anything else here that was, like, significantly difficult we should talk through?
That's a good one.
Liudmila Molkova 00:35:54 Yeah, no, I don't think there is anything significant, it's just a lot of… there will be a lot of changes. Okay, so one thing I think it's worth discussing. Messaging and FAS are both… they don't have, actually, the… the… The owners, maybe FaaS has, but messaging pairs are are already closed. I wanna get maintainer okay to actually do this structural refactoring without changing the conventions much.
Trask Stalnaker 00:36:26 Yeah, I.
Josh Suereth 00:36:26 That's something we would be signing up for as maintainers, right? Go ahead, Tra.
Trask Stalnaker 00:36:30 Yeah, definitely, if you can… send — I mean, I know splitting up a huge work into small work means lots of PRs, and that can take its own churn time. But I can definitely sign up to give quick reviews on small Structural PRs.
Maybe if you create a… a thread in the, the public semconf, Slack channel.
And just… Just add… each time you send a PR, just add it to that thread.
And those of us who can Sort of approve quickly, review quickly, approve quickly, can watch that thread.
Liudmila Molkova 00:37:24 Okay.
Sounds good. Thank you.
Trask Stalnaker 00:37:28 Yeah, so the more — the more of the small, like, low-controversy things that — yeah, I can — Help get those turned around quickly. But we need two. We need two approvers. So somebody else, hopefully.
Josh Suereth 00:37:43 I can, I can stand up to help here, Ludmilla.
Good to be on the Weaver side, too.
Liudmila Molkova 00:37:49 Awesome. Review my viewer PRs, please.
Josh Suereth 00:37:52 Yeah, yes. I'm still… I took off Friday, and I'm still not through my email this morning from everything from Friday. So, when I get there.
Anyway, cool. I gotta drop, so feel free to continue without me. We didn't do triage for context for those who might have been late, but see y'all.
Liudmila Molkova 00:38:11 See ya.
Do we have anything else on the agenda? We can do the triage. Do we have other topics we want to discuss?
Lewis Lewis 00:38:25 I will probably be opening the issues for Azure app service functions, and possibly logic apps, since they all overlap in Some of their hosting.
But I would also just, I saw that this thing has functions as a service as part of the migration you're doing.
And, if it would be useful, and if that would be a good first issue, I would be happy to contribute also, since that overlaps with Azure Functions, and I want to learn more about OpenTEL, process.
Liudmila Molkova 00:39:05 This one, well, it, okay, I'll, I'll send the.
probably the PR for messaging, and you can see. I don't think it's a good first issue. I I think it's it's very hairy and very tooling specific, and you you you won't learn much.
Lewis Lewis 00:39:24 I will trust you.
Then I will just come next week, probably with several PRs.
Liudmila Molkova 00:39:32 Yeah, sounds great.
And… Dude!
Do you have any, do you need any guidance, anything we can help you with this process?
Lewis Lewis 00:39:43 Other than the…
Trask Stalnaker 00:39:45 Get their PRs auto closed.
Lewis Lewis 00:39:48 That was that was the main one. So I'm looking at talk about how app services and functions, depending on their hosting plan, are running on the same infrastructure.
or at least I have the same environment variables. I obviously don't know exactly what's going on at Microsoft.
So… how to explain this. Azure App Services, Azure Functions, Azure Logic Apps are all different services, right?
and cloud provider things that we are sold. Sometimes they provide the same environment variables. Sometimes they have different ones, depending on kind of what Sort of payment you're doing.
What plan you have?
So, there would be cases where I would have a… potentially, like, an Azure… app services instance ID. That does not take the same exact variable as container apps, because this is a different behavior. This is like a sort of a scaling thing.
That would apply to Azure Functions, so I don't feel like that's a clear name.
If I follow the azure naming, I get website id, which I feel like is also maybe not a clear name.
And then if I follow just instance ID, we get the conflict with the, Go collector.
So… considerations there.
Michele Mancioppi 00:41:11 The the 1st question is.
Of the services that you mentioned, which ones are naturally covered by the functions-as-a-service namespace, and which not?
Lewis Lewis 00:41:25 Azure Functions would be covered by Functions as a Service, and App Services, I would say And Logic Apps, I don't have a strong opinion on. That's down the road for me.
Michele Mancioppi 00:41:35 When you say that the service instance idea of the collector Clashes.
Is it because, you are, You're having… you're assuming the sidecar scenario?
Where, you have in Azure App Services, the collateral you set aside with the application, or…
Lewis Lewis 00:42:00 So this is something that Kathy ran into. So it's in the go collector. They are assigning a UUID. It's not related to the Azure behavior, as far as I know.
Michele Mancioppi 00:42:09 Yeah, but that is used for the internal telemetry.
Trask Stalnaker 00:42:14 Or the default.
I think that that's the default, but you should be able to override it.
Michele Mancioppi 00:42:21 I don't know about that, because the, yeah, I don't know if in the collector you can use a transform processor.
to the writer's resource attributes.
But ultimately here.
Trask Stalnaker 00:42:31 Oh, in the collector.
Michele Mancioppi 00:42:33 Yes, but here the problem is twofold. On the one hand is… The sidecar collector has a different service instance ID than what you would expect looking at The other runtime.
But that does not apply to any of the pipelines that you would use to receive telemetry from the application in the runtime through the collector.
And you're having there two different processes.
the application.
And the collider side column.
In… you actually do not need.
A collector sidecar, in most cases.
So, for example, if if we had resource detectors.
for the different Azure services, then the resource detector for Azure, using some metadata endpoint, would go and set up in the application the service instance ID, and then the application could automatically flush the data out.
in these kind of services, having a self-calculator is necessary only if you want to do batching or sampling set aside.
or if you want to collect application runtime metrics, for example, in in Ecs.
It exposes through on, the metadata service, it exposes Docker, Docker metrics, and if you want to collect those.
There is no resource detector for that application. So you tend to put a collateral sidecar.
What I'm trying to say is that Having a sidecar collector is not a given. You do not always need it.
So, your problem with having to…
Lewis Lewis 00:44:20 In this case, I am not specifically asking about the sidecar. I am asking about the semantic convention for when this particular identifier is across multiple cloud providers. One of the things we've done is use the name of the cloud provider.
But I do think that bringing up functions as a service was a good point. So possibly we can use an app service instance for app.
Azure App Services, and just use the functions as a service for Azure F.
Michele Mancioppi 00:44:48 And additionally, you should set service instance ID.
for the application itself.
It's, it's a very good idea. There are, I'm not aware of.
Anybody specifying how that is supposed to look like on Azure.
But it is never a mistake to do it.
from inside the application with a resource detector.
Trask Stalnaker 00:45:13 Luis, for the, for the PRs that — or the issues PRs you're going to send, do — is there an implementation? So that, like, with Kathy's PR, there's a go contrib implementation there that always helps us a lot. Okay.
Lewis Lewis 00:45:34 There will be.
Trask Stalnaker 00:45:36 Perfect.
Liudmila Molkova 00:45:39 Have a…
Trask Stalnaker 00:45:39 Helps make these discussions concrete.
Liudmila Molkova 00:45:44 I have a naive question. So at least Azure Functions and App Service are instrumented natively. There's a tell. I'm not sure if it's it became Ga. Or if it's in the public preview.
But maybe it's the pain for the Azure Functions team.
To set things properly and actually set the resource attributes for everybody to use rather than trying to detect things.
It might be worse.
Check in.
I think it's Azure functions pause.
There could be some issues related to… OpenTelemetry And I know they've been looking into.
how to set the resource attributes properly.
So maybe there is some prior art there, and if you need a connection.
I might try to connecting you to some pinging some folks.
Oh.
I've been working on it from the inside.
Lewis Lewis 00:46:47 That would be very appreciated. Thank you.
Liudmila Molkova 00:46:50 Okay, so if, like, I would imagine, when you send a PR and semantic conventions, it's not something, like, it's common, and I'll just tag the people, who've been wanting to keep working on it, and we'll get it from there.
Lewis Lewis 00:47:30 Nothing.
Liudmila Molkova 00:47:36 Okay, then I am going to use a little bit of your time, if you don't mind, to… Chat about future, things I would like to bring to our document rendering.
I've… I think I showed it last time, but we had just a couple of people, so I wanted to share it with the bigger audience.
And.
So… As you probably know, or maybe not, we have a set of shared… well, we don't have a set of shared templates. We kind of do, but we don't use them yet.
So I'm proposing to move the shared set of templates For V2 into this common repo.
And we currently use them in GenAI, but we kind of need to generalize a little bit.
So that… They work for any federated repo.
And I have a demo here, of the things… I… Like, my first draft of how I want things to look, and it's different than what we do today.
So, first of all, we can… we don't render, All the things in the registry yet, and we don't have to, but, somebody could, and it's an easy way to just say, okay, render all the definitions we have.
And here is how it might look like.
So.
Just to compare… Maybe we'll open this one up.
And… So today, we have the docs. We have it's it's named however you want. It's just the the markdown files with snippets. Right? But we have registry. And then the registry, we have attributes. And if we had any entities, we would also have a folder for entities here.
And.
So let's take a look here first. What I'm proposing to change is a couple of things. You don't see attributes here.
Because they are hidden in there with me.
README is an index of all the things we have.
And maybe we should have a table of contents here, but it's all auto generated, right? So it's a list of spans and it's just the names, the types of the spans.
And then there are names of the metrics, and names of the events, and at the bottom, there is this blob with attributes.
So it's intentionally down below, so we don't, like, prioritize attributes, but we have still a good list of them for quick search.
I'm And then and the right individual spans and this is again a lot of generated and it's just based on the YAML definitions.
We can… In this proposal, we can switch off registries. We can switch off events, metrics, spans individually. We can even switch off a registry at all. So if somebody doesn't want to run their registry, they could, but it's their choice.
And then… For… This is the registry and then there is the free form markdown as we have today.
It doesn't change much.
It's.
Yeah, okay.
Nothing new here.
So, I don't want to, switch to this in the core semantic conventions until we finish migration to v2, because this brings a lot of changes to Markdown, but after we do, we can, switch there. We can try switching in GenAI semantic conventions. I can bring it on the GenAI call, but, like, it it's not worth it unless we want to use shared templates, for this.
And.
What do people think? What should they change?
Trask Stalnaker 00:52:15 So the main… difference was the attribute rendering like the the old registry, which is only attributes versus the Yeah, I mean, I really like the Span's… Metrics, events… layout.
Liudmila Molkova 00:52:37 Yeah, the other big part is that today the register, the top level is attributes.
and entities.
And then… Let's go to semantic connections.
Trask Stalnaker 00:52:56 I think that would be nice on the, doc site, also, because we've been… For a long time, we wanted to deprioritize the attributes.
Liudmila Molkova 00:53:07 Yes.
So, like, here, we have individual namespaces under the signal, or attributes.
And there, instead, we group by the… name space where we Here.
Trask Stalnaker 00:53:25 Oh, okay, I missed that.
Liudmila Molkova 00:53:32 So what we lose here is like this central file.
That lists all the namespaces, I'm not sure if it's particularly useful.
I like it more for the entities, we have the file that lists all the entities and all namespaces. We can render it, we can edit, it's not like the index for overall, it's not a big deal to render them for some of the signals.
Trask Stalnaker 00:54:09 I mean, in general, it aligns the… Like, grouping by domain aligns more with How we want people to think about things.
Again, like, not… it not being just a grab bag of attributes.
Liudmila Molkova 00:54:29 Yeah, when I'm saying that for entities and especially because there is like reasonable number of them, it might be interesting to see them all in one place.
and.
I I've not proposed. I'm not adding it right away. But if somebody feels strong that this place should, we should keep it.
I'm totally open to rendering them as a big list.
Yep.
Okay, done.
Any thoughts? I don't hear… Objections?
Are there any?
Ruediger Schulze (IBM) 00:55:13 Yeah, first of all, I think having a common… You know, use of templates, I think I'm in favor of this from a mainframe repository or semantic conventions perspective so that then, you know.
From a layout perspective, everything is actually the same.
I think I'm also in favor of calling out the metrics, traces, and logs or events separately.
I think the way… so when we look at how that comes out from mainframe, there are certain platform specifics, like processor type, something that, you know, is, I think, very specific to the platform.
But that demands that we describe for maybe more common metrics of how to use these attributes to, in the end, specify or qualify the particular metric. So I think with You know, having a more clear definition or section about metrics, and then being able to utter markdown language, which kind of, like.
it clarifies of how certain of these attributes have to be populated in context of the metrics that makes sense. So I think this proposed format actually will work better for that.
Liudmila Molkova 00:56:32 Yeah, you kind of have a choice. So that's what I'm showing today. It's fully auto-generated from YAML.
And we can go pretty far here. Like there could be some you can change on you.
Reference something you can change all these notes and all the briefs and examples. You just cannot change. I think this.
this… This, this, and this, you can change requirement level.
You don't control the text outside?
But you can choose, either you just render the registry and it's done, it's fully automated, or… Like today in Samconf.
Oh.
Here, all this text is handwritten.
And just the things, within this, snippet or… are… generated.
And it's probably either or.
This is just more involved, but you get more customization.
Christophe Kamphaus 00:57:42 Yeah, we have several domains where it's mostly written like that.
So I think, yeah, we have to choose either one or the other.
Liudmila Molkova 00:57:54 Yeah. And I I would like us to be at the point where everything substantial is part of YAML?
then, like, we can do the code gen, we can do validation and everything. It's just we're not there yet. We're getting there.
And maybe eventually Semconf.
Would switch to registry on the model.
With some minor… Parts where we do the markdown.
But… For now, it's just you, yeah, you pick one or another.
Well, you can pick both if you, if you like, but, but yeah.
Trask Stalnaker 00:58:41 It would be very nice to have that normalized.
Across everything.
Liudmila Molkova 00:58:51 Cool.
Then, I'll keep working in the background on it, maybe, I'll just.
propose the… okay, so, first, I'll need to put… I'll need to merge this pull request.
And, it seems we don't have any objections so far.
If you wanna take a look, it is… Somewhere, I'll paste the link to… I guess semantic conventions channel.
And ask for reviews?
And, if it's eventually merged, I'll probably propose to update semantic conventions genii as the first goal.
and eventually we'll get to the core semantic conventions. Once we switch to V 2 fully there.
Trask Stalnaker 00:59:42 Cool.
Liudmila Molkova 00:59:43 Yep.
That's all I had. Thank you.
Okay, since we have a few minutes, let's just spend a quick triage and see if we need to unblock anything.
Where is our board?
Here we are.
There are nothing is ready to be merged.
There are a few things that need more approval. The first one is policies.
And this is the switches, the semantic conventions, policies.
Ricoh policies, too.
V2?
to the shared set of policies we have in the same repo I showed you, I need another Approval on it.
Please?
Have.
Trask Stalnaker 01:00:43 What was the number?
Oh, I can find it. There's not that many.
Liudmila Molkova 01:00:54 Couple of these friends… Okay, so… There are some, there is some problem with.
Using Docker as the source of.
Versions.
And I don't completely understand which.
Oh, renovate dashboard.
This one.
But it's updated, we were… Good.
Trask Stalnaker 01:01:46 Or maybe it.
Maybe it updated, but didn't pin it?
Liudmila Molkova 01:01:53 Let's see here.
It would be in the versions.
Here?
No, it didn't.
Trask Stalnaker 01:02:09 Looks pinned there.
Liudmila Molkova 01:02:12 D one of B.
The same.
Okay, and… I don't know,
Trask Stalnaker 01:02:28 I can look at the logs. I've looked at those logs a lot for other repos.
It's…
Liudmila Molkova 01:02:38 Okay.
Trask Stalnaker 01:02:38 Not always obvious what's going on.
Liudmila Molkova 01:02:43 Yeah, I think that.
Trask Stalnaker 01:02:44 Obvious, what's going on?
Liudmila Molkova 01:02:49 Yeah, I think the concern here was that We actually pull the Docker from, sorry, we were from Docker.
And if for whatever broken reason the.
GitHub releases, and… Doctor Diverge.
We would have another issue.
But it's probably a minor concern.
Trask Stalnaker 01:03:12 Generally, Generally, I agree with… if we're pulling it from Docker, we should use Docker as the… the authoritative source, so I don't… really… I don't think we should do this unless there's something I'm not understanding still.
I'm.
Liudmila Molkova 01:03:30 Yeah. Okay, so then you'll take the.
Trask Stalnaker 01:03:32 I'll look at it, yeah.
Liudmila Molkova 01:03:34 Okay.
I… We wanted to use this belt. Okay, so I had a concern… Here. So we are switching one tool to another.
But we have a change here.
that looks odd, like, we are changing Kotlin to capital C, and the rest stays the same, and I don't get it, and… I don't understand, like, either we need to suppress the Kotlin, do we… why do we update?
Is there any benefit in updating this? So I kind of like context here. Maybe I'll leave a comment with all this.
And… I'll get it further.
Should we move this to maybe blocked, because we… we don't plan to work on this, Radiger?
Ruediger Schulze (IBM) 01:04:42 Yes, please go ahead. And we already have opened the issue to move this over to the federated one.
Liudmila Molkova 01:04:50 Yeah, or maybe we should close it?
Ruediger Schulze (IBM) 01:04:53 Or just close it and take the definitions from there, or I can close it.
Liudmila Molkova 01:04:58 Awesome, thank you.
Ahhh.
Okay, and then just a few.
Things that were blocked. I think this one is blocked.
Christoph, do you remember why there is no prototype?
Right.
And.
I don't think there is any update.
And it doesn't look like there is anything about the prototype.
Trask Stalnaker 01:06:27 Kristof dropped.
Liudmila Molkova 01:06:29 Oh.
And I don't remember where we landed, Tan.
This one, I think it's still… Blocked. We had a long spread conversation.
Okay, I think I promised to reply to this one, and we had a conversation on the call.
But I didn't post the discussion and the conclusion here.
For… for the context.
Oh, we don't have time for the context, but essentially we'd like to understand.
Still, why not span with extra attributes or an extra span?
I'll look to the reply here.
Trask Stalnaker 01:07:38 Yeah, and I might have replied on the Java PR itself.
It's where I get now.
Chuck King.
Maybe not.
Liudmila Molkova 01:08:05 It doesn't seem that there's anything recent.
Okay, we have to call it here.
I will.
remember to I'll reply.
Thanks, everyone. See you around.
Armin (Dynatrace) 01:08:28 Thank you.
Trask Stalnaker 01:08:29 Well…
