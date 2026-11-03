SIG: Semantic Conventions SIG
Date: 2026-11-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker (Microsoft Corporation) 00:02:26 Hey folks, we'll get started in another minute or so.
All right, looks like we've got a reasonably full agenda, so I will try to keep this, time box… tier.
Jeff, welcome!
Hey!
You wanna…
Jeff Leva 00:04:34 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:04:34 Take it away.
Jeff Leva 00:04:35 Oh, yeah, thanks, Yeah, sorry. I didn't mean to take over your agenda, but I think I put it right at the top, so apologize if I…
Trask Stalnaker (Microsoft Corporation) 00:04:46 No, no.
Jeff Leva 00:04:47 over.
Trask Stalnaker (Microsoft Corporation) 00:04:48 How it works.
Jeff Leva 00:04:49 Okay, alright. Well, you know…
Trask Stalnaker (Microsoft Corporation) 00:04:51 And we have a bunch… we've got a bunch of meaty-ish topics here.
Jeff Leva 00:04:55 Yeah, well, I won't take much time, and I do have to drop at the half hour, so I appreciate you letting me get started. But, so we talked last week, kind of about what COSI was trying to do with getting some of these Agentic, mapping done.
And I think you'd kind of stated that we wanted more presence for that, and then reviews were kind of maybe an issue. But, that being said, I did open one little PR here, the 650, to kind of, get to… these, attributes, just starting with 2. And so this is the type of thing that we're… we're trying to get done, is… is have these attributes, filled out, and kind of help support the COSI, telemetry.
Needs.
So… Anyway, I just wanted to start with this basic one.
And, see how you guys wanted to work this. You mentioned maybe a separate group, or… So anyway, just trying to get your… your thoughts on the best way to go, Trask.
Trask Stalnaker (Microsoft Corporation) 00:06:09 Sure, so I think, we're probably confused a little bit about where to go for what pieces. I think we had, kind of directed you to this group as sort of for foundational security stuff that's, broader than AI.
But for something like this.
kind of proposal that is, you know, directly in the GenAI Semantic Conventions, that would go to the GenAI SIG.
Jeff Leva 00:06:50 Okay.
So, when is… what… where's that group,
Trask Stalnaker (Microsoft Corporation) 00:06:54 It's the Tuesday group that you joined last week, when… and that's what I mean. I'm afraid we've confused you about where to go for which pieces, because I think I had suggested coming here, because at that point, it felt like, broadly, a lot of the things that you… the group was doing Or maybe more… we're broader than GenAI, we're secure… like, we lack the security foundation.
In Semantic Conventions, and that.
Jeff Leva 00:07:24 What kind of…
Trask Stalnaker (Microsoft Corporation) 00:07:24 where OCSF, could potentially fill in, help And, you know, we're open to discussion of where that should live, whether that should be in Semantic Conventions, or, you know, if that's something that OCSF could own. There's kind of a lot of… Discussions potentially to be had around that area.
But if you are looking for, sort of, very specific Gen AI attributes.
And things that aren't… Like, this is not looking to me like a… security… specific… Proposal.
Jeff Leva 00:08:16 Well, yeah, I mean, Arthur, do you want to help me out on this? I'm not sure if I'm explaining it well, but yeah, I mean, COSI is all security, So, I… you know, wherever you think we… fit, but I think this is just really the tip of the iceberg. This is just getting us started. So, there could be definitely more.
Flavor, but that's what we do in COSI as security, so these are… You know… Primitatives that we'll need to work through.
Arthur Saputkin (CosAI) 00:08:48 A, I'll add up to that, and everybody, multiple.
I'm also part of the Coastline Trask, I met you in the past in the telemetro meeting. Yeah, like, it is, like, we obviously focus on GenAI, but I assume there's, like.
Like, it's how to distinguish what is Gen AI and what is, like, security for GenAI, right?
Like, the fields that Jeff is trying to add.
might be GenAI related, but we… Think they are important for security use cases.
Right, so, like, using those to identify attacks that are happening, or have happened in the past.
So I'm curious, like, where should we, like, how do you see that Trask? Like, if security-related, like, are these, like, fields that are, like, very much security-related, but… because usually in security, we use the regular fields.
To, you know, identify security issues.
Trask Stalnaker (Microsoft Corporation) 00:09:56 So, there's polo… I mean, there's certainly some things that are… Useful as general observability.
And those things… You know, and I'm not sure if that's… these fall there.
But I don't think we're… Yeah, I think we… it's a tricky area we need to discuss. Yeah, Josh, please.
Josh Suereth (Google LLC) 00:10:27 Yeah, I was just gonna add, like, the… the simple model we have now is, like, namespaces have ownerships in SemCom groups.
And so, this is the general group where, like, everybody who owns a namespace should be here to talk about general issues. And so, when you want to work across all the teams, this is the right place. And I think that raising awareness of security, and by the way, kudos for working on Agent Security, I think this is the most important work we are doing right now in the world.
So, thank you. But anyway… the, the simple… the simple nature is, like, if it says GenAI, the GenAI SIG is the one who makes the ultimate decision, right? And so I think we can, in this SIG, have, like, a requirement around, like, if there's security requirements we want to enforce across all the SIGs.
the Gen AI SIGs and say, hey, there's a baseline set of security things you need to respond to and have, great. Like, that is… that's something we can do, but the way we do that is usually policies and enforcement of policies and that kind of crap.
Versus, like, here you're like, okay, we need these 3 pieces of information for a security use case. That would be reach out to the SIG, because they own that.
But in terms of going forward, if you're saying, hey, I need security, and I need, like, stuff from the browser, and I'm using that client domain, or the browser domain, there's a SIG that owns that, and you'll have to talk to them, because they own the namespace, right? And so, we kind of, like, practically Namespace equates ownership.
Jeff Leva 00:11:56 Gotcha.
That's a small…
Trask Stalnaker (Microsoft Corporation) 00:11:58 Moving target.
Jeff Leva 00:11:59 Okay.
Trask Stalnaker (Microsoft Corporation) 00:12:00 if you need kind of general things, right, like, I mean, this is kind of where I was… Partly guessing you were going with security as potentially things that are, like, user, or… do we have role?
We have a few overlapping barely overlapping Concepts in the general Semantic Conventions that But some of… some security domain stuff is outside of Gen AI, right? Like, identity, that sort of thing, and that's where the GenAI SIG isn't the right place. That's where this SIG, I think, is the right place to have those discussions and figure out the coordination between us and you all and OCSF.
Jeff Leva 00:12:53 Okay, so it sounds like we need to be a little more surgical on where we… depending on what we're doing at the time.
kind of dictates where we go. Is that what I'm basically hearing?
Instead of just throwing a big plunk on the wall, it's not that simple, so we just need to dial it in to specifics.
Liudmila Molkova 00:13:12 Maybe we can start with, like, an overall story? Like, if you can show the… the design overall better present than write it down. It's hard to read things these days.
And we can… kind of discuss where… what areas things belong to, because what I was going to say, similar to Trask, that sometimes if you send things to Gen AI-specific.
we would, from GenAI's side, ask you to, use a general concept, just because it's not specific to Gen AI.
And then… and this would be this meeting. But if we talk through the design first, then we can kind of see where these things are that are Gen AI-specific or not, or maybe we'll ask way more questions.
Jeff Leva 00:14:08 So for this, we need to… like… go for tomorrow's meeting. The… Correct, just move this to that agenda.
Gen AI.
Trask Stalnaker (Microsoft Corporation) 00:14:20 For this one specifically, yes, but I think… you know, the GenAI group is also gonna kind of, you know, look for use cases and understanding how that applies and how it fits, you know, our current Observability focus, and so… to support why the Gen AI SIG would need that, you know, you may need A broader security story.
Jeff Leva 00:14:49 Okay.
Trask Stalnaker (Microsoft Corporation) 00:14:49 one thing to consider would be, at least as you're the federated Semantic Conventions, which allow you to build semantic conventions outside in your own repo on top of GenAI and the core semantic conventions.
You could use, like, cosi.genai.trigger.type, cosi.user.stuff.
And even if, like, even if that's not the ultimate goal, having to go through that modeling, process with our tooling and our policies, the Weaver tooling and the Weaver… the policies there.
Will help you, as well as then it will help us… it would help us to see it in that format.
To see, you know, the whole… the whole thing kind of together of where you're trying to go.
Even if it's not a final, even if it's just kind of a draft.
Proof of concept kind of thing.
Trying to figure out how we can understand the bigger picture here.
Jeff Leva 00:15:59 So maybe an issue with… More scope to it would help, As well, so I can open an issue, as opposed to this PR.
Art Indition with this, and give that.
Trask Stalnaker (Microsoft Corporation) 00:16:12 Yeah, but definitely check out the federated Semantic Conventions just, from, you know, as a way to… maybe build out You all can build out what you want, and then we can kind of see that bigger picture, and how, you know, that could help us to piece together I think the OCSF folks have… At least been discussing something similar.
And again, then we can see what the overlap between all three is, and… Figure out how to go forwards.
Cause it's… it's a big… it's a big… ball of wax there.
like, it's… Gonna take some work to figure out a good Path forward for all of us.
Jeff Leva 00:17:04 Okay, yeah, I work with the… OCSF team, too, so… I'm probably the only one that's… working in OCSF and COSI, mostly, so… But I'll talk to them again, too, because, yeah, I mean, that's how it all started, was, you know, trying to get some… I mean, it's easier for me right now, I can work with OCSF, come up with telemetry… you know… stuff, and… and… work it into COSI. This was the missing piece, is to get it into OTEL. So, yeah, that's what we're trying to do, is have symmetry between the three, at best possible. Okay, so, yeah, well… I'll take that away and try to improve on that.
Trask Stalnaker (Microsoft Corporation) 00:17:54 Yeah, and maybe an Uber… an Uber overarching issue would be a good idea, just in the… and I would… It could be in Gen AI, or it could be in the Semantic Convention, depending on which kind of focus you want to take.
Yeah, and then you could point to, you know, places that we could go and kind of understand Other pieces better, and proposals and discussions.
Jeff Leva 00:18:24 Okay. Gotcha. Alright.
Well, that's what we needed to know, so I appreciate your time.
And feedback, so thank you.
Trask Stalnaker (Microsoft Corporation) 00:18:33 Cool. Yeah, thanks for coming. Yeah, it's a, I mean, it would be an amazing thing to… accomplish.
Jeff Leva 00:18:40 Alright, it would, yes.
Trask Stalnaker (Microsoft Corporation) 00:18:42 We're on… we're on board with, like, we're motivated to… for something to come together there. It's just… it's… Gonna be… work.
Jeff Leva 00:18:54 Gotcha, okay. Yeah, I'll get back with the OCSF team, I'll talk to Arthur and our COSI group, and we'll open an issue and kind of get started, so… Alright, thanks again for your time, appreciate it.
Trask Stalnaker (Microsoft Corporation) 00:19:09 Alright, Ludmila.
Liudmila Molkova 00:19:12 Yeah, I wanted to try to push through the remaining, entity changes that are holding, V2 stuff, the lost ones.
So for these two friends, I hope that maybe Martin or somebody from the client seek would be here, but I'll ping them.
I want to check with others, how do we feel about… okay, I can just merge these two. What they do, they replace the entity with public group.
But… and I have the approvals.
But we also know that these two friends will be owned by client in the client federated Conventions.
So, even the public group does not have to exist.
And I'd rather not introduce the contract, like, public group as a contract.
Then… Like, if we do it now, we will need to remove it later.
If I just drop it now, it's just a matter of timing when they pop up, and how they pop up in the client repo.
If people here don't have objections from removing them completely, I'll just check with the client group and see what the plans are.
And if they are okay with it, we'll just go ahead with… Full removal.
Trask Stalnaker (Microsoft Corporation) 00:20:38 Sounds good.
Liudmila Molkova 00:20:39 Okay.
So this one and these friends, were grouped by the ownership. There was, all of them were owned by the Core SIG, and some of stuff got extracted into individual PRs, but what's left in this one is… Narrowing down cloud, to cloud resource.
Then Fast to Fast Instance, and Heroku to Heroku app.
The first one and the last one, they don't have any contention around them.
The fast is tricky.
So the first instance today is fast name, first version, first instance, and guess what? Fast max memory.
We… I… this is not my goal, yeah, this is not my goal, immediate goal, to fix this.
And obviously, this design is problematic in many ways. So what I'm trying to achieve here is just the… that the FAS instance, is a new entity, which has still all of this, but it has identifying attributes.
Probably fast name, fast version, and especially fast memory should go away.
Maybe there is a need for a separate FAS entity?
Than, I don't want to solve this… yet.
I think James is very eager to solve it, and he has 2 or 3 PRs around this.
We could not reach agreement on, let's just do the fast instance for now, and evolve it from there.
Michele Mancioppi (Dash0 Inc.) 00:22:30 But… fence instance ID.
Liudmila Molkova 00:22:34 Yes, it should be.
Michele Mancioppi (Dash0 Inc.) 00:22:36 Then, shouldn't we wait to define the entity until it is fast instance ready?
Trask Stalnaker (Microsoft Corporation) 00:22:44 There's already an entity.
Liudmila Molkova 00:22:47 Yeah.
Michele Mancioppi (Dash0 Inc.) 00:22:48 Okay.
Liudmila Molkova 00:22:48 So that's the problem. There is an entity, and it's not modeled right.
Because it was more…
Trask Stalnaker (Microsoft Corporation) 00:22:54 I agree.
Liudmila Molkova 00:22:55 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:22:56 So the schema V2.
Is the… kind of the forcing function here.
Liudmila Molkova 00:23:08 Yeah, so what I'm.
Trask Stalnaker (Microsoft Corporation) 00:23:09 Would you mind pulling this out into a separate PR?
Liudmila Molkova 00:23:13 Okay.
Here.
Trask Stalnaker (Microsoft Corporation) 00:23:17 Just so we can get the non-contentious parts in, and…
Michele Mancioppi (Dash0 Inc.) 00:23:25 And for the record, we'll probably need a second entity, or at least we could use a second entity for the version.
Especially when you start talking about aliases on AWS.
Liudmila Molkova 00:23:38 The version is yet another thing. I wanted to get Josh and other entity SIG people opinion. Turns out we… It feels very natural to mark version as identifying.
But it sounds like it's absolutely wrong from an entity design perspective.
Michele Mancioppi (Dash0 Inc.) 00:23:57 Yeah, the, an instance will, will have… So, it changes between, between, serverless things. In Lambda, are not all… Not all instances have a version.
So there is an implied version playtest.
Which is seldom reported in those cases.
So it should not be identified. But the version itself is a valid entity.
And then it gets nastier when you talk about aliases.
Another bucket of nonsense.
Josh Suereth (Google LLC) 00:24:39 Yeah, I can only speak to, like, Knative and, Cloud Run, but the… I do think we probably need to sit with the FAST folks and talk about entity modeling, I think is the TLDR of what I'm reading here. I would be a fan of us turning this into an attribute group for now, and then remodeling as an entity later. I think that is a lot less content… well, it's probably contentious, because probably someone wants to model as an entity immediately, but, it might be safer, but yeah, the… to… to what Michele is saying, it's… it's, here's the version… if it has to be identifying, there's, like, places where, say, in Cloud Run, it's actually called revision, the name of a job and the revision make a unique ID together, and you could model it as that. But that's, like, Cloud Run specific.
if we go to Fast, and we're trying to look across AWS, Knative, Cloud Run, you know, all the different people who have FAST things, I really don't think versions should be… Identifying, particularly of, like, the… component, the unit. The other thing is, you know, we have service name here. Like.
Is the service and the fast name the same thing? I think they are.
So, I think there's just a lot of… what?
Michele Mancioppi (Dash0 Inc.) 00:25:58 Nope. No, they're not. No, no, you're not supposed to imply that.
Josh Suereth (Google LLC) 00:26:03 Okay.
Michele Mancioppi (Dash0 Inc.) 00:26:04 You can, you could have multiple versions, multiple deployments of the same Lambda in different regions. They would have a different name and provide the same service name.
They must not.
Trask Stalnaker (Microsoft Corporation) 00:26:16 I'm gonna try to keep us on, time.
So, does that sound agreeable to everyone, to convert this to attribute group?
Liudmila Molkova 00:26:28 Separate para attribute… public attribute group.
Trask Stalnaker (Microsoft Corporation) 00:26:30 I… same PR, if that's not contribution… not controversial, then… Yeah.
Liudmila Molkova 00:26:37 Okay, let's try the same PR.
Josh Suereth (Google LLC) 00:26:40 I would approve the changes you made now, too. Like, I… I can do that.
Trask Stalnaker (Microsoft Corporation) 00:26:44 I already approved it.
Josh Suereth (Google LLC) 00:26:46 Yeah, like… Did… so the concern now is just, like, the FAST group wants to redo their, entities. Those aren't… they're not… Released, right?
Liudmila Molkova 00:27:01 They are released, it's just the…
Josh Suereth (Google LLC) 00:27:04 Sorry, are they.
Liudmila Molkova 00:27:04 Whatever… They are not stable, no.
Josh Suereth (Google LLC) 00:27:07 Right, so we can still make changes to them, I guess is my point.
Liudmila Molkova 00:27:10 Yeah.
Josh Suereth (Google LLC) 00:27:12 Do we have concerns approving this and moving forward with this if, like, two of the maintainers approve it?
And then we can let the FAST group come back with proposals and fix their design from there. Or is that… or would we rather try to push for attribute group?
Liudmila Molkova 00:27:30 I think the FAS instance entity makes sense regardless. It should lose probably all the other attributes it has.
Similarly to Service Instance ID.
So, I don't see how this change would… Not be better than the existing state.
And public attribute group would need to disappear, probably.
Josh Suereth (Google LLC) 00:27:55 Yeah.
That's kind of my thinking. Anyway, I'm gonna approve this, because I did take a look at it, and I forgot to mark it as… You made some changes and merged it, and I think it's good to approve now.
For the other things I was looking at, but yeah, this, it… why don't we… why don't we take it offline and work with FAS, and if we get enough approvals to merge this, I know that there's some contention, but we know that we have to rework the system, it's not breaking, we're not making any changes here that will That are unreversible, right? Like, none of this is irreversible, it just fixes V2, so… If no one has complaints, why don't we move forward?
Liudmila Molkova 00:28:39 Yeah, if you approve, I'll merge. I can take the blame with Fast SIG.
Josh Suereth (Google LLC) 00:28:44 Okay.
Liudmila Molkova 00:28:45 But it does not prevent any of their plants from materializing.
Josh Suereth (Google LLC) 00:28:51 Yeah, it's approved now.
Trask Stalnaker (Microsoft Corporation) 00:28:52 And I have requested in the FAS Slack for them to open a community, like, a project proposal for stabilizing these things, because it seems like there's… Interest and want to make sure there's enough Diversity of opinion there to push that forward.
Alright,
Liudmila Molkova 00:29:19 And,
Trask Stalnaker (Microsoft Corporation) 00:29:20 This one…
Liudmila Molkova 00:29:21 Yeah, and the final one.
Okay, so I extracted it from, this PR. So we've done some stuff for AWS ECS.
And, but we also have an entity for AWS EQS.
And all it has is the cluster ARM?
Which… According to my research, nothing in… up in telemetry or in public, populates, so this is this de facto unused attribute.
Michele Mancioppi (Dash0 Inc.) 00:29:55 back… Technically, Splunk populates it.
And, Lumi got it.
And indeed.
Liudmila Molkova 00:30:04 What was the last one? Who got it?
Michele Mancioppi (Dash0 Inc.) 00:30:06 Lumigo.
acquired by Dash Zero. It requires something insane, like matching a node ID with an auto-scaling group, and through that.
getting the cluster around, like, the EKS, the RN is not known inside an EKS cluster, as far as I can tell. Last time I checked, 6 months ago.
So, technically, some people use it.
Liudmila Molkova 00:30:32 Okay, good point, the AWS CloudWatch.
populated in the cloud resource ID, which kind of makes sense.
There is an interesting question, what happens with other properties, because in theory, the node could also be a separate resource, because it could be a virtual machine, and you can build one cloud resource for multiple cloud resources.
there are a lot of questions on what should be the cloud resource ID for something complex like that.
Michele Mancioppi (Dash0 Inc.) 00:31:15 Yeah.
the cloud resource for the node should be the ARN of the node, which is the… either the EC2, I think it's called Machine ID, or the, on FireGate, you have a federated task identifier behind the scenes.
Liudmila Molkova 00:31:33 Yeah, but, like, if you have, cloud resource ID set to node, but it's… the node is the part of the cluster, and the cluster is also a resource, then what is the cloud resource ID? Because you have to…
Michele Mancioppi (Dash0 Inc.) 00:31:49 Yeah. The, in my head, it makes a difference whether you are the node and you are a cloud resource in your own right.
But, for example, I would expect the AWS EQS cluster ARN to be set as the resource ID on, for example, a deployment, collecting via the CADS object receiver.
if… Amazon saw fit of actually exposing the Iran inside the cluster, that is however they've used it.
And, when you look at the management UI of EKS, If I recall correctly, the workloads have their own errands.
So, one could say that in that case would be… would be something different, but nobody says.
That inside the same cluster, you have only one resource ID. That's my point.
Liudmila Molkova 00:32:49 Which brings us to the point that How to… we need, more, better conventions for the cloud.
for this one, I'd rather deprecate this attribute, because it is not populated by OpenTelemetry.
Anybody who populates it can keep doing so, it's deprecated, it's not removed.
I'd remove the entity, and we would get back to Designing it properly once we get to the cloud conventions.
Michele Mancioppi (Dash0 Inc.) 00:33:31 That would work.
Liudmila Molkova 00:33:33 the slightly controversial piece, then, is that I'm updating the cloud resource ID attribute, saying that it should be the AKS cluster, Yes, this friend.
And from what you're saying, Michele, it could be problematic, because it's… first, it's hard to get. Second, it creates a contention around the instances.
So maybe I'll…
Michele Mancioppi (Dash0 Inc.) 00:33:58 Yeah, just a bit of an auto.
On this bit, I have another.
Liudmila Molkova 00:34:12 Okay, I'll think a bit more about what to do about it, but it sounds like… about this, this line. The rest seems not that controversial.
Michele Mancioppi (Dash0 Inc.) 00:34:25 I mean, Antoine will have probably words with you at KubeCon, but for the rest, yeah, sure.
Liudmila Molkova 00:34:31 I'll talk to Anton then.
Trask Stalnaker (Microsoft Corporation) 00:34:37 Alright, let us move on.
Shawn?
Shawn Alpay 00:34:45 Yes, hello, can I take the screen?
Trask Stalnaker (Microsoft Corporation) 00:34:48 Absolutely.
Shawn Alpay 00:34:49 Right. So, I'll try to move quickly here, but I kind of want to give you kind of an overview of what we're doing in focus, and really in the Tokenomics Foundation, under the Linux Foundation, and how that leads to this, and then get to some of my questions about how we're gonna, move forward with a federated focus, schema. But let me, let me share my screen here.
So, just… oop, not this one.
Let's go to the top. Just super quick, I just want to give you an idea of where we're going with this, so… to ideally bring… we're building out a set of data structures around value attribution. So how do you go from cost and usage through telemetry to tasks and outcome and then assign value to it. Obviously, assigning value to AI spend is, like, a huge question in this space right now. So, the idea here is to be leveraging OTEL as kind of this, like, Rosetta Stone to get you upstream to cost and usage and downstream to your tasks.
So you've got your metered bill of cost and usage, which is cost metered at a high level. You've, of course, you have your runtime activity in telemetry, then you've got your deliverable, like, your tasks, like, what were you doing? And then the proof of the business state change, like, what was the business outcome?
that you want to record, and then what was the value you assigned to that outcome? So, it's these five pillars that you need in order to do this work.
And so, no one data source tells a story. I won't belabor this, because I built this for our governing board last week, but the point here is that you need all five of these to do value attribution.
Cost and usage, well defined by focus, and of course, there's proprietary billing solutions like the AWS CUR. Telemetry, very well defined by OpenTelemetry, so my pitch back to our governing board, which I don't need to make here, is let's leverage OTEL for this, let's not build this ourselves. But it's an island from cost, so how do you get from cost through activity to value? And then, of course, tasks are fragmented across orchestrators and tools, etc.
Outcomes are siloed in business systems, value is like spreadsheets, mental models, vibes, like, how do we help mature this whole space by having a place to land all five of these data sets?
So, I'm gonna… I'm gonna skip through this, because I don't think you all need to under… to understand all the deliverables that I'm proposing back downstream from OTEL, but, one thing here is… is… that I want to talk you through is… First, the publication of this thing, like, we're gonna build out this focused telemetry schema, and per your recommendation, we're gonna do this in a federated way.
We'd be adding focus attributes, like resource ID, service provider name, etc, there. But we'd also be adding these task ID, outcome ID, workload ID, to be able to allow people to either, at runtime or post hoc.
enrich those traces with these IDs to tie back… tie downstream to your tasks, your outcome, and then your value.
So, then that gets published, and then, of course, we'll have to launch into the enablement part, which I don't know to what extent you all give guidance to folks doing this, but… what I foresee is that we're gonna… the focus… the working group is gonna have to go through this whole exercise of issuing pull requests to all of these open solutions, like agent harnesses and AI routers and partnership with the closed source solutions to, like, leverage this telemetry schema.
to present data to both generate and ingest and present data in a native way. So, I know this is an eye chart, but, like, there's a lot of work downstream once I… once we get the schema in place and it's available for people to use.
And then the last thing I want to show you here is just kind of, like, what I see us needing to do, and listening to the conversation earlier in this meeting, I fear I may have over-engineered this, but I'll look forward to you all telling me, whether that's true.
Which is that we would have, we have our focus working group, we would be authoring our spec, and then, of course, we would be generating the concepts that would lead to attributes that we put in our focus OTEL schema. We'd be standing up a new working group and a repo to steward the working group.
And this… the… the repo would be called focus-otel-semcon.
It'd be running under the JDF, the Joint Development Foundation's called, quote-unquote, community specification.
Where we have a single maintainer that's defined that determines consensus and stewards the spec, and then we have one editor that issues to main. So, we have submitters that can create PRs, and then we have one maintainer and one editor. That's the process by which our program manager Adopted the community specification to run that.
we would… and this is kind of maybe the open question here, is how… how to interact with this body? Like, how much… how much oversight is too much or too little oversight? Like, to have two or more reviewers from this body.
that we could leverage in an advisory capacity to optionally or be required to be reviewing PRs within some timeframe.
And to give us feedback on whether this, this looks good, this meets specifications, or if you want to just say, just, if it goes through the linter and Weaver, that's fine, we don't need to look at that very closely. And then it gets into the registry.
The workflow would be that anyone can propose an issue in our repo, but then only the working group authors can be authoring against our staging branch. We would then approve it, and then there'd be this, PR issue to go to Maine, we would then bring it to this body for feedback, and then, you know, pending consensus, then we'd merge it into Maine.
And then main means registered. Like, that would be the thing that gets into, downstream artifacts.
So, the last thing here would be some… just some open questions, or some asks would be, like, we would want a couple of advisory reviewers for those PRs.
I'd want to know whether a 7-day review window works, or if that's just way, like, not what you were imagining for federated semantic conventions. Confirm that this is the right approach.
One open question is, like, how does… how will this get into your list of federated registries, and who approves those listings? And then… The second question would be, I saw this OTEP PR4906 around its federated Semantic Conventions. I know it's still open, I know that it's not been merged yet. I don't… I don't know how, like, close to done that one is, but some of this is built on the back of that… of that PR, so… A couple working assumptions here is that, for focus, we'd be defining billing scope keys, and of course, each entry would note its nearest hotel attribute. It'd be attributes only, we're not proposing measurements at this point.
And then, just to name the term attribute means something different in focus. It means this, like, body of normative requirements that can straddle entities. Obviously, the way you're using the word attribute means, like, a column and a table, or, like, a field and a dataset.
And so we're… I'm just gonna have to make sure that we delineate between those two, the overlap of those semantics there, so… Now I'll pause for questions and thoughts. Go ahead.
Liudmila Molkova 00:42:20 Couple of thoughts. So, it seems like… In this group, we don't define just attributes.
We define the signals.
Shawn Alpay 00:42:30 Yeah.
Liudmila Molkova 00:42:30 And, the second we would kinda… Don't want to define the same concept multiple times. Like you mentioned, let's say workload ID, or the resource ID. We kind of already have those things.
And if… Let's say cloud provider needs to set both, one for, cost-related data, one for general observability, it would be duplication.
Yeah. So it might be interesting to entertain the idea of reusing some of the stuff that Odell has, and maybe, helping us shape it better, but, it's, of course, more… more work together, which is awesome and difficult at the same time.
Shawn Alpay 00:43:18 I'm very keen on that, but let's just take, like, Cloud Resource ID as an example, like… What if you're not a cloud provider?
why would you use the cloud namespace? Like, that's kind of my point. Like, there's one thing to reuse these namespaces, it's another to reuse a namespace that's not applicable to a given provider. So, has that come up? Like, and if so, what's been your guidance in those situations?
Michele Mancioppi (Dash0 Inc.) 00:43:45 I can tell you that, for example, people are pretty nonplussed in using the cloud namespace for their private data centers, and nobody pats an eyelid on the matter.
Liudmila Molkova 00:44:03 Yeah, I can speak a little bit about this. I think Josh also has some thoughts.
Shawn Alpay 00:44:08 Sure, go ahead.
Josh Suereth (Google LLC) 00:44:10 Sure. As the author of the PR that you're mentioning for the OTEP, It's funny, because we implemented the PR before the PR got approved. So we're actually, like, halfway down the PR and making it, and, like, it's almost… a formalization at this point for us to get it merged, but we should get it merged, because I think there's some important things in there to… So, in terms of you, like, thinking about, Federated SemConv.
Totally fine, but, like, now to some of Ludmila's concerns. It is… it is actually about, the attributes and things that you're adding. Are you adding new signals, or are you adding new, like, layers of attributes that have to be applied across all signals? And the way you phrased it earlier with the work that you're doing.
it might be the latter, is what it feels like from what I look at. But again, I don't know the details specifically, but when you say, like, cost attributes.
Cost is funny, right? Because the way we measure cost is always vicariously. We don't literally write a dollar spend as a signal. What we do is we write some metric, and that metric is your proxy to cost.
And you use the metric instead. So, what metrics are you going after? Are those metrics going to be things that actually duplicate metrics Gen AI is producing, or metrics like the hosts.
Semantic Conventions are producing. If so, like, what we'd ask is, we want to have a set of host instrumentation where when you sit down on a host, it goes into the Linux kernel and grabs all the bits of detail that it needs, and creates a set of metrics. And to the extent those metrics are used to evaluate cost, great.
We don't want to have, like, a cost-specific instrumentation, and a observability-specific instrumentation, and a security-specific instrumentation over time.
This is, again, like, we talked North Star OpenTelemetry, we want to be able to say, okay, here's the set of data that we get out of hosts, and here's the instrumentation you can turn on and off things, and if your cost happens to be very, very, very attuned to CPU usage, great. This gives you a CPU usage metric.
That you can use for cost, or power consumption, or whatever. For AI, it's what, token… tokens is the way everyone's charging right now, so that's your cost. Maybe that changes in the future, who knows? But, like, whatever metric you're using for cost, right, you would… you would make sure that that is instrumented in the right places. So, in OTEL, what that means is… these different SIGs and these different things are targeted at the instrumentation, the actual code that you write. So if you would go back in your diagram, where you're like, oh, we have to reach out to this team, and this team, and this team, and this team, and this team, to get our instrumentation in place.
what we've tried to do in SemConv is align our groups around the people who own those systems, or I should say, people who own instrumenting those systems. So the Gen AI team right now, the GenAI SemConv, is focused around, like, you know, agent SDKs, and agent harnesses, and agent, you know, that side of the world, whereas there's a group that is doing networking right now that's focused on, okay, how do I get data out of networking systems. There's a host SemCom group that is, like, how do I get data out of Windows and Linux, right? So, I think you're… you're… First, again, super excited to see all this, and super excited to see the thought that you've put into all of this as well. But I think you're going to be more aggressively engaging with our ecosystem, is what I'm saying. Particularly when you look at… you already have an aggressive plan for all the teams you have to reach out to, but I would say, The best way to reach out to us would not necessarily be to have this focus thing on the side.
but to actually look at what signals you need to produce, and actually put them into, a particular SIG.
7-day review window for an active SIG is reasonable. For an inactive SIG, we're really bad, just frankly. If it's something that doesn't get a lot of attention, you're talking, like, 30 days, in reality.
Am I happy about that number?
No. I think that needs to get fixed. But, like.
for the work you're doing here, we're talking specifically about Gen AI, cost of AI, That group is really fast. Now, the way we work is not a 7-day review window of 7 days and you're in.
It is, you know, 7 days, but we hold things as long as they're still active, contentious.
behavior. So it's not… I used to say OTEL has a veto culture, I still think that's partly true, but if somebody has a concern on a PR that we're not comfortable moving forward without addressing, we do hold PRs.
So, I don't know what you're expecting there, yeah.
Shawn Alpay 00:48:55 No, no, I just… I'm happy to… to align with the culture, I'm just trying to get a sense of what… how the federated model works. Like, to what extent has… has what you just said got… been applied to federated, registries?
Liudmila Molkova 00:49:10 Oh, I think there are two ways. There is federated Conventions that are in open telemetry governance.
But, for the focus, it sounds like you are the owners. So, we… even though we would love to work together, there is no requirement on you to follow any of our processes, or get us veto or approve your changes. So if it's a separate repo owned by your organization, go ahead with it. You don't have to interact with us, but we'd love to work together.
Josh Suereth (Google LLC) 00:49:44 Yeah, and to echo on that, that means that you're also writing that instrumentation yourself.
You're not necessarily interacting… like, you can do whatever the hell you want if you're on the side.
And if you want to know how Federated SemComf has worked for, like, getting PRs through an activity, you know, Trask and Ludmila have been driving Gen AI. I don't know if you want to speak to the volume that you've had, the, like, speed at which that So, you know, is there anything you want to talk to from experience there?
Liudmila Molkova 00:50:16 We are overwhelmed. We get a lot of different, asks for all areas of Gen AI, authentication, identity, security, and everything, GenAI, and some things we have no idea about, obviously written by OpenClaw.
Shawn Alpay 00:50:33 Yeah.
No, I can only imagine that you're overwhelmed. So, it sounds like a 7-day window is too short. It needs to be either 15 or 30, maybe 30 days, is that what I'm hearing?
Trask Stalnaker (Microsoft Corporation) 00:50:47 Or you don't need a window, like, you don't need our approval.
We do have in the general Semantic Conventions… I mean, part of the Weaver tooling is to force you to conform with a lot of basic stuff, and then we also have a lot of documentation in the Semantic Convention repo about how to write conventions and our conventions for writing conventions.
Shawn Alpay 00:51:09 Okay.
Trask Stalnaker (Microsoft Corporation) 00:51:10 So definitely, you know, check those out.
Shawn Alpay 00:51:13 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:51:14 I think the piece that I would kind of be interested in understanding more, or discussing more, but I do want to kind of cut us off, because we have a couple other topics.
Is the instrumentation story I'm kind of curious where that would land, and maybe we could have a follow-up discussion,
Shawn Alpay 00:51:37 Sure, happy to talk about them more. I presume that summer, all of you are going to be in Salt Lake next week, and I'll be there too, so we can talk more then.
Liudmila Molkova 00:51:45 Nice.
Trask Stalnaker (Microsoft Corporation) 00:51:46 Fantastic.
Come find us in the, hotel area.
Shawn Alpay 00:51:50 Yeah, I'll be coming on Monday, so I'll be part of the observability Day stuff, so… I'll see you there. We'll talk about that.
Trask Stalnaker (Microsoft Corporation) 00:51:58 Alright.
Awesome.
Shawn Alpay 00:51:59 Thank you.
Trask Stalnaker (Microsoft Corporation) 00:52:01 Ludmila, you have span type… oh yeah, let me reshare. Span type cleanup.
Liudmila Molkova 00:52:09 Yeah, this is just the, Pink, and call for reviews, or… So, I'd like to make progress on the spend type and the spec, and eventually it will get to Semantic Conventions. We talked about it last time, that the spend type, that is.
Just a random semi-validated thing today would become something we… would publicly put on the OTLP and guarantee… provide stability guarantees and everything.
So, our spend types are not awesome, and the idea is that we would keep them consistent with metric names.
In most cases, it means… in cases, it means renaming span types. In a few cases, it might mean renaming metrics.
But here is a giant PR that only changes the, spend types and their markers in Markdown.
Aligning them around the, let's say, area, kind, and then the… the specific operation name, like HTTP client request.
So this is what… how we've been calling our metrics. The interesting part is what do we do with, let's say, gRPC-specific metrics, or whatever, database-specific metrics, and then we would use the system constant.
let's say MongoDB, client operation duration.
Trask brought up a good concern, that we still have a mixture of V1 and V2 spans, and some of them are prefixed with span. And I think we even require it for the group ID.
So I'll follow up, I'll create an issue. We need to do the big cleanup of our docs for V1, V2 stuff.
I'll create an issue so we don't forget, but it doesn't seem like any of you think it's blocking for now. There is nothing I can do about it anyway.
Trask Stalnaker (Microsoft Corporation) 00:54:25 Merge it.
Liudmila Molkova 00:54:27 Cool.
And there is a follow-up for the docs. I think there are some good comments there from Christoph. He couldn't make it. We had some active discussion. I'll… I think he pinged me on Slack, we'll talk about it.
I'll see if there's any contention there. I'll hold it until Christoph's concerns are addressed. I forgot what they were.
Trask Stalnaker (Microsoft Corporation) 00:54:54 Sounds good.
Liudmila Molkova 00:54:58 Awesome, that's it.
Trask Stalnaker (Microsoft Corporation) 00:54:59 Looked good to me.
Let's see… I had, okay… We have this text, and I wanted to… Instrumentation should require explicit configuration of which headers to be captured.
Does this… I was interpreting this to mean that instrumentation should not allow a wildcard, should not support a wildcard, but I'm not I wanted to understand if that… how it was… How other people read it.
Or if it just means that… We should advise users about the warrant… about… we could support wildcard, but advise users about the problem of… using it.
Josh Suereth (Google LLC) 00:55:55 Yeah, I think this is just about secure by default. So, if a user wants to wildcard grab everything.
okay, but we should tell them it's not a great idea, and I think wildcard matching isn't the worst, especially if you do, like, prefixes and stuff like that, so I wouldn't use this to stop wildcarding. It's also not a must, it's only a should.
But I think this is more about security by default. We shouldn't just grab credentials out of headers and throw them into observability by default. You should… if you want that, cool. I don't know why you would do it, but maybe someone does.
Trask Stalnaker (Microsoft Corporation) 00:56:32 So the reason I was asking was, I was… I like the… Declarative configuration included excluded selectors.
And so I like the idea of having a kind of consistent mechanism everywhere for, selecting what, you know, headers you want, what, for Java, what metrics you want, what… MDC values you want, etc.
And so, I was… Considering… proposing this for… because right now, declarative configuration, I think, conforms to that other understanding of, like, only explicit named headers.
Cool, I think that's enough feedback. I may bring this up in the spec meeting tomorrow, just to get broader feedback on from people.
Liudmila Molkova 00:57:35 I love the configuration, all but non-problematic, like, you know, all but authorization.
Trask Stalnaker (Microsoft Corporation) 00:57:45 Yeah, yeah.
Bucket Boundary Evolution. I had a question, if you haven't seen, I have a PR… Documenting a proposal for, kind of bucket boundary, advice, conventions for us, specifically for durations.
I was thinking about this in the Gen AI world, and, I like this, series. It's approximately… it's like a decimal-friendly approximation of an exponential.
progression.
And it also, for these values, it's essentially the same as our HTTP, except that it doesn't include the .75, values that we have in the HTTP.
And then for larger values, it snaps to minutes, for the remaining progression.
Database today… as, just 1 and 5, and so, if we do adopt this, I was just curious if we could add… if adding new boundaries… is… backwards compatible.
So, certainly adding new… yeah, go for it, Josh. I know you. You don't need any further explanation.
Josh Suereth (Google LLC) 00:59:28 This is, according… okay.
Is it backwards compatible by the OpenTelemetry definition of our data model? Yes.
The way we define histograms.
And the way that we encourage their usage in Prometheus, for example, it should be compatible because you should be interacting with them with the histogram, methods, not with the specific, like, less-than value.
where a bucket change would break things, right? So bucket changes should only change The accuracy of the histogram.
In practice, and, like, your calculation of things, by our data model.
However, users might complain who use Prometheus and rely on, like, the less-than buckets, but basically, that is something we accepted, as that is an allowed breakage from OpenTelemetry.
Of a way of using Prometheus that we don't think is actually good for the health of the ecosystem. The histogram buckets have to be able to change.
to make things more accurate, or to adjust to where your actual distribution is, for a variety of reasons. Users actually need the ability to change these over time. Like, modifying histogram buckets is a thing that we know we have to do all the time.
To optimize. So, I… anyway, is it allowed by our data model what we defined? 100%, yes. Is what you're proposing, I think, a good fix? 100%, yes. Totally should do it. The only database I know that would break is a particular query style in Prometheus of I want to look at values at an exact bucket by label.
And I actually think that that use case is… I mean, you know what I think of the use case, because I already said so, but in our compatibility docs, we don't allow that use case, so you're fine.
Trask Stalnaker (Microsoft Corporation) 01:01:19 Alright, sorry we've gone over time. Lewis, I got stuck, I did look at this, I got stuck on the whole, is it an app service or an app service plan instance?
It was very…
Lewis Lewis 01:01:34 I think I linked the issue, and I should have linked the PR, I'm sorry.
Trask Stalnaker (Microsoft Corporation) 01:01:37 Oh, oh, it's.
Lewis Lewis 01:01:37 Different ones.
Trask Stalnaker (Microsoft Corporation) 01:01:38 Oh, this is a different one than that. Okay.
Lewis Lewis 01:01:41 So, this is a specific question. I've been getting review for this PR from James Thompson, who is insisting… who would like me to add, I should say, an instance ID Which is to say an app service.instance.id, which is a thing that previously was discussed, and we said specifically that we weren't gonna do it.
In relation to one of Kathy's Container Apps PRs, it would be exactly duplicative of the way we're currently doing service in society.
Oh.
I'll do it.
Trask Stalnaker (Microsoft Corporation) 01:02:15 Stay with this. This matches the GCP, right?
Lewis Lewis 01:02:19 Yeah.
Trask Stalnaker (Microsoft Corporation) 01:02:20 came from… before.
Yeah, I'll try to, I can't promise, it might be after KubeCon, but I did… I got confused by the… this is the one, the app service plan instance versus app service instance.
Lewis Lewis 01:02:39 I don't have a strong opinion on this.
Trask Stalnaker (Microsoft Corporation) 01:02:42 Yeah.
Lewis Lewis 01:02:43 Plan is more accurate, but it's also more wordy, and if you… Okay, he's right that you should know that it's on an app service, so… That one doesn't matter.
Adding another attribute matters.
Trask Stalnaker (Microsoft Corporation) 01:03:00 Yeah, leave it.
We'll, we'll, we'll get to it.
Lewis Lewis 01:03:04 Okay, thank you.
Liudmila Molkova 01:03:05 Yeah, and prefer scoped PRs that get out of the scope you have the use case for.
Trask Stalnaker (Microsoft Corporation) 01:03:13 Great. Alright, thanks all. Sorry for going over today.
Liudmila Molkova 01:03:17 Thank you.
Trask Stalnaker (Microsoft Corporation) 01:03:17 R.
