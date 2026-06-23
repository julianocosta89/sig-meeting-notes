SIG: Entities SIG
Date: 2026-06-22
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Matthieu Noirbusson 00:03:52 Hi, everyone.
Arve Knudsen 00:03:56 Hello.
Michele Mancioppi 00:07:56 Folks, we are… 6… 5 people, 6 people in here. Everybody's silent.
Braydon Kains (Google) 00:08:05 I don't know who usually runs this meeting.
Arve Knudsen 00:08:09 Don't surreff, isn't it?
So I guess we're all waiting on Josh.
krajo Krajcsovits 00:08:35 I'll just fill in the particulars.
While we met.
Wow, actually, a lot of… Long, complicated names, including mine, so… I'll just put in a number of empty slots, and you can…
Braydon Kains (Google) 00:09:37 Oh, sorry, I had started the meeting section, I just forgot to change the day.
I'll just move my stuff.
krajo Krajcsovits 00:09:54 Oh yeah, that was today. Okay.
Braydon Kains (Google) 00:09:56 I just… I just forgot to change the day on the little selector thingy.
krajo Krajcsovits 00:10:03 No, that's fine.
Braydon Kains (Google) 00:11:29 Looks like there were some messages today in the hotel entities channel, saying Josh would be 30 minutes late, Ted won't be here, Dimitri won't be here.
krajo Krajcsovits 00:11:50 Since we seem to be waiting for… Josh, do you want to reconvene?
20 minutes?
Michele Mancioppi 00:11:59 It seems it's another skip week.
Josh is technically on vacation, apparently.
Arve Knudsen 00:12:09 Isn't he saying he's just… 30 minutes late today?
Braydon Kains (Google) 00:12:15 Yeah, he said it'd be 30 minutes, but then, Ted and Dimitri are both skipping, and…
Arve Knudsen 00:12:20 Daniel.
Braydon Kains (Google) 00:12:21 suggested a skill.
Arve Knudsen 00:12:22 Okay.
I see.
Braydon Kains (Google) 00:12:38 Could also try and reconvene in 20 minutes if… We have to discuss. My topic can wait a week if we want.
krajo Krajcsovits 00:12:47 Yeah, I think ours… ours too, because it's going to be a long… -Oh.
Discussion about that proposal?
Alright, any objection to just… Reconvene in 20?
Let's see if Josh turns.
Braydon Kains (Google) 00:13:42 Wow.
krajo Krajcsovits 00:13:43 Alright.
See you then.
Josh Suereth 00:33:50 Hey!
Am I too late?
Arve Knudsen 00:33:54 Hello, Josh. We're all waiting on you.
Josh Suereth 00:33:59 Sorry. I love that.
Alright.
This is 622, okay.
Matthieu Noirbusson 00:34:09 Hello, Josh.
Josh Suereth 00:34:12 Sorry I am late, man. It's been… it's been crazy the past two weeks because of holidays that my calendar went insane.
We have a new June holiday in the US, and I'm still not used to the fact that we have off in June.
Alright, let's get started, because I'm slow and late.
I think the most important thing to discuss here, delay 30 minutes. Braden, you want to talk about host entity?
Braydon Kains (Google) 00:34:44 Sure. So, I'm here on behalf of the System Semcov Group. We're pretty close to finishing Marking all our process metrics as release candidate, and we want to work on our system ones next, but the hard part with marking system metrics stable is that we need to stabilize the host entity that we're working with, and… It's… Kind of… kind of messy, and it's going to rely on some stuff in entities that isn't really, like, landed yet, or fully decided how it's working.
And so I wanted to just come and quickly state the way I think we want it to work, and then see if that's, like, in line with what Entities is doing at all, or, like, if I'm totally off-base.
Okay. The way we're thinking about it is… To identify a host, there's this field, the host.id, we cannot think… Of a consistent way to… Always uniquely identify a machine under any context.
like, we thought about using, like, Etsy machine ID, but that, like, only really works for Linux and for, like, some distros and stuff.
there isn't really any other way we can think of to say, in any context, this is what a host ID could be. So we're pretty much saying, like.
host.id is just, like, in whatever context your host is in.
whatever makes the most sense. And so if you're an EC2 machine, then host ID being an EC2, or what's ARN? Is that the AWS, identifier.
or if you're in a different context, like a VMware, like, whatever VMware's identifier for that machine is, essentially saying that the host entity is identified by whatever identifies it in the monitoring context.
The other thing we were thinking of doing… Related to that was… there's this kind of idea of, like, entity relationships and, like, an ISA relationship.
I thought it would make sense if… We have the host entity.
that could be, like, an ISA AWS EC2 instance, then the EC2 instance entity could have… whatever deeper information about it as an EC2 instance, and it would be joined on host ID and EC2's, like, cloud instance ID, and there would just be basically a list of, like, whoever cares about monitoring hosts and being able to identify hosts. It could be, like, the different cloud providers, it could be, like, a Proxmox thing, it could be… VMware, whatever, they would come up with their own entities that could join on host ID so that you can get more information about the host, but also still get the base host entity.
Does this all still work? Like, is this kind of still the way we're thinking of modeling this sort of thing?
Josh Suereth 00:37:43 Yes, except, so this, this for sure was our, our original plan. What's interesting is, is, you can't get away to uniquely… identify. Does that mean that you… if we needed to have a local identity, we'd have one, but we wouldn't have a unique identity?
That's the… that's the thing we're exploring right now, like, Dimitri's been looking into this, of… In situations where you can't make a universally unique identity, you can use a local identity that at least is unique within some context, and someone else provides that context.
Braydon Kains (Google) 00:38:19 Right.
Josh Suereth 00:38:19 So, like, process is that example. Process is not unique, but a container or a host could provide context to make it more unique, right? Yeah. Is host also one of these things?
Braydon Kains (Google) 00:38:32 So it… that kind of… that kind of does line up. The only part that doesn't line up is that not only can we not uniquely identify it, we actually don't know what to say to put in that attribute at all.
Josh Suereth 00:38:48 Like… Yeah.
Braydon Kains (Google) 00:38:49 There's no generic thing that we can say, this is what you could put in host.id.
Dmitrii Anoshin 00:38:54 But, but currently, we add, sound like, as you mentioned, whether it's a machine ID from the host, or if it's cloud ID, we take that data from the cloud.
Why that doesn't work?
Braydon Kains (Google) 00:39:10 Well, that's kind of what I'm saying. Basically, like.
for host.id, it has to be… like… there's, like, 5 different things it could be, and it depends on what context you're in. We basically… there's just no one… one-size-fits-all host.id value that we can give.
Dmitrii Anoshin 00:39:28 Yes.
Braydon Kains (Google) 00:39:29 It depends on what you're… where you are.
Dmitrii Anoshin 00:39:30 That's how it works right now, and we discussed that in the… initial… when we started, like, entities in general, we… I think we decided to keep it this way.
And say that… host.id, a value.
Can, like, has several sources, essentially, and whichever it's currently running in, It'll get that… based on the priority list, right? The cloud would be the highest priority. If it's not part of the cloud, we would, use, machine… Machine 80 instead.
It's currently actually defined in the specification.
Braydon Kains (Google) 00:40:17 Yeah, that part, that part we're keeping the same way it is. It's mostly about, like.
how do we… how do we model it for, like… like, imagine a backend is… is dealing with, like, multi-cloud, and that host.id could be lots of… very different formats.
Dmitrii Anoshin 00:40:34 Yes, and in that case, we… it has to go with cloud… cloud… other cloud, cloud entities.
Josh Suereth 00:40:41 Right, but, so, the concern, though.
like, think about this from the instrumentation standpoint. One of our goals with entities was to have resource detectors be somewhat independent of each other. If I write a host detector that detects hosts resources. Does it have that hard code? Like, does it have to have code that understands every possible cloud in that resource detector? Like, how do I attach host environment variables without understanding every single possible cloud that could exist in the world. You know, like, do I want to bundle in VMware code, and AWS code, and Microsoft code, and Alibaba code into that host detector?
Dmitrii Anoshin 00:41:24 That's what we have… we resolved that problem in Collector by having detectors per, like, cloud, for example, and they all can write host entity.
Josh Suereth 00:41:40 Right, but then what you did in the collector is not part of our data model generally, which is you write that stub entity, right, that's all descriptive attributes. So, like, you have… you have a host detection, which it looks up host name, host IP, all that kind of junk, right? And it writes an entity that doesn't have an identity to it.
That's just the description. And then you merge it with the identity that came from the cloud-specific ID detector.
Right. That, like, that model, our data model doesn't support that today.
Right? Our merge algorithm.
Generically in entities. And so, we also haven't written it down that that is… How we think entities should work.
Let me rephrase this for you, Braden, so you can follow along with, like, what this looks like. So effectively, what we would… what we're saying is, you would have a generic resource detection block of code that would Find all of the descriptive attributes of a host.
and provide them in a, like, degenerate entity. It's like a bundle of stuff that says, I'm an entity that's a host, I don't know who I am, I have no identity, but I know that this describes me, and I'm, like, the local thing, if you will, okay?
Then you would have individual detection code for every possible cloud that users can configure what they want to use, that basically would say, hey, here is the host that you're on.
I have your identity. I can figure it out. And only I can, because of how crazy it is. So you could have a generic one for Linux that does Etsy Machine ID, you can have one for AWS, etc.
You put these two together in, like, a resource detection pipeline, if you will, that… where the thing that detects the descriptive attributes would join with the identity from the other thing and create you a host entity.
So that's… that's how we're doing hosts.
in the collector today, right, Dimitri?
Dmitrii Anoshin 00:43:38 Yep.
Josh Suereth 00:43:38 Okay, the weird thing here is that's not how we're doing process to host, in terms of global identity, unique identity.
And is that a thing that we want to make Like, is that a thing we want to make part of the data model of entities, or somehow, like, lift up as a first-class thing to solve this kind of a problem?
Dmitrii Anoshin 00:44:00 And how you would do that on the data model?
Josh Suereth 00:44:06 how would I do it in the data model? We would… we'd update our merge algorithm to allow you to register these, like, you know, basically, I'd call it, like, a local entity descriptor or something, where I can… Put that bundle of descript… like, what you're doing to the collector would be part of the data model and part of the merge algorithm.
Dmitrii Anoshin 00:44:34 Yeah.
Probably.
I can also talk about my experiments with bringing Local identity versus global identity.
in the collector resource detection, probably it's also related and something we need to discuss. Maybe your idea about Solving that on the data model.
Site would help with that as well.
Josh Suereth 00:45:00 Yeah.
So, for context, I think, like, the question behind what you're asking is, can you stabilize host.id?
and the entity for host, if we have no idea how we're gonna generically create host.id in general.
Braydon Kains (Google) 00:45:21 I think that's… that's… Kind of it. Yeah, it's also that, we want… An answer for… people want to suggest things that are going to go on the host entity that don't make sense on the host entity. In my eyes, they make more sense on specific entities for different virtualization providers.
And we want to be able to say why we're not Like, introducing a bunch of attributes into the root host entity.
And we, like, we would say, because of the way we intend to join relationships with other entities that are going to provide more information. I mean, this also kind of lines up with… current, stuff going on in process. It's a little bit simple, because it's just between process and, like, it's executable, so, like, only one thing we're worried about joining on. In this case.
We were thinking… could probably join on any number of different types of things, like maybe it would be generic cloud instance, or maybe it would be specific for each provider, or maybe it would be specific to some specific virtualization technology, or… We just want to be able to… We don't think we can stabilize before we have that answer, basically.
Josh Suereth 00:46:34 Yeah, so, I mean, the plan from the beginning for entities was that you can have ISA, so that you can have, like, I… there's an entity which is an AW EC2 instance, right? And you can say that this host is this EC2 instance. And one of the big differences, you know, there is, if I want to aggregate across all my hosts, I don't care if it's EC2.
And so instead of having, like, some sort of, like, type extension policy, we decided to go with a flat hierarchy with is or relationships. So basically, instead of, like, a, you know, what you would call an inheritance OO style, we have a more flattened style.
Where that's possible. So if I needed to group everything by EC2 instance, I can, and I get only the hosts that are EC2 instance. If I want to group by all hosts, I can in the data model.
Because host and EC2 are ISA, Yeah. So I would have both of them available in resource if I need to do so, and the entity relationship, you know, I can discover things appropriately there. So I could have something that asks AWS what machines exist, and gives me a list of all the ARNs, and I can ingest that independently of anything else, and I can use that signal to tell me about, like, you know.
where things live inside of regions and all that kind of crap, you know? That's… that's the idea behind having them decoupled with Iza.
So I think that's in line.
I'm still nervous about this ID thing, generally, because it's like a giant wart on the entity data model, which… Makes us question whether we have the right model.
Dmitrii Anoshin 00:48:11 I'm thinking… I'm thinking if we… if we, keep, like, this flat data model as a… as a default, let's say, like, host, and having separately EC2 instance, and, like, the GKE instance, for example, GDCP, but we have some kind of Like, layer on top of that.
Kind of capability that would… Converge identifying attributes of the flat entities.
And you would say which particular Host… which particular entity needs to be… Replaced on… And in that case, it'll be host.
Saying, hey, host would inherit Identifying attributes of associated, like, cloud instances, for example, something like that.
This kind of… kind of orthogonal capability that can be applied for those specific use cases. Particularly, it'll be useful for host ID when we need to provide some kind of backward compatibility.
with the old way of detecting hosts. Does that make sense?
Josh Suereth 00:49:26 Yeah, it still doesn't give us an set of identifying attributes for hosts, though.
Like, I think… I think what I'm hearing is there's not really… An identity for hosts that we're happy with.
Dmitrii Anoshin 00:49:38 At least not a…
Braydon Kains (Google) 00:49:39 Not a generic one. Like, you can identify a host within a context if EC2 is your context, or if one Proxmox setup is your context. You can uniquely identify hosts in that, but like…
Dmitrii Anoshin 00:49:50 Yeah, but that… we are solving that issue with the local global identity when we specify Right. Context, context type, right?
Josh Suereth 00:50:02 Even in that case, Dimitri, I don't think we have a local identity for hosts. Like, what's the local identity that we'd use?
like, let's say… let's say we try to identify a host locally. What would the… where… so… so there's a Proxmox detector, or an EC2 detector, or a VMware detector that detects the VMware ID, the Amazon ARN, that sort of thing, and would say, hey, this thing is an Amazon, you know, VM, and there is a relationship with hosts, okay? Cool.
And, like, I'm the context for that thing. What is the idea of the host, then? Of the host entity?
Like, it…
Braydon Kains (Google) 00:50:40 I thought it would just be the same as whatever the identifier would be, and like, if it's an EC2 instance, then host ID would contain an ARN.
Dmitrii Anoshin 00:50:48 Yes.
Braydon Kains (Google) 00:50:48 That's how I thought it was going to work.
Dmitrii Anoshin 00:50:50 And that's gonna be optional, but by default, we can just use a machine ID from the host, right?
Josh Suereth 00:50:57 Machine ID doesn't work in Windows.
Braydon Kains (Google) 00:51:00 It also doesn't work on all Linux machines.
Josh Suereth 00:51:02 Yeah.
That's upset.
Braydon Kains (Google) 00:51:04 That's why… that's why we were talking about this in System last week.
Dmitrii Anoshin 00:51:09 I see.
Josh Suereth 00:51:09 It might not work in Mac either, right?
Dmitrii Anoshin 00:51:13 And, like, I guess default fallback would be UUID in that case, because we need to provide something.
Braydon Kains (Google) 00:51:20 just, like, come up with our own UUID.
Josh Suereth 00:51:22 Yeah, basically make the UID that's stable for the lifespan of the host.
Dmitrii Anoshin 00:51:26 maybe we can have some kind of association with the host, making it deterministic. I, I, I… I really… I don't think it's a technical problem, we can have a… For each of the possible environments, we should be able to find some, like.
some way to deterministically generate your idea, right?
There should be a way.
Braydon Kains (Google) 00:51:55 Yeah, I think…
Dmitrii Anoshin 00:51:56 my bike.
Braydon Kains (Google) 00:51:57 Feel it.
we'd have to deal with, like, UUID clashes if we're in charge of generating it. Like, one thing about using, like, an instance ID from AWS is that it's, like, AWS's job to make sure it's unique.
If we're generating the UUID, then it's our job to make it globally unique.
Josh Suereth 00:52:18 So, what we're trying to do is, if you don't have a universally unique identifier, you provide a globally unique identifier where global is global within some scope.
And an entity's data model allows you to have other resource detection that happens, which adds the scope to your identity. So, for example, process… the process entity doesn't have to put all kinds of crazy shenanigans around it. You literally just need PID, maybe Creation ID, right? And then we will, We will ensure via resource detection that, like, a host is added, or a container is added, or something is added, to make that.
Braydon Kains (Google) 00:53:02 Josh crashed.
Josh Suereth 00:53:06 So… You're unique within a context thing is that somebody else has tagged you remote to you, and you have to understand who that remote thing is, and it could be one of any N things, you know? But even if we think about, like, let's say old-school hardcore on-prem use case, someone… Someone is running a cluster somewhere. I have a machine under my desk.
What's my host ID when I use OpenTelemetry with it?
Braydon Kains (Google) 00:53:43 That one, I don't even know how to come up with an answer, because I don't even know what I would say. What's the unique identification of the host? Unique identification of the host is just, like, on… like, on my local network, what's my host name? Is it the same, right?
Dmitrii Anoshin 00:54:01 Can we use MAC address, just as a…
Braydon Kains (Google) 00:54:04 Yeah, yeah, probably. MAC address.
Josh Suereth 00:54:08 I think my internet is hurting here. Did I…
Braydon Kains (Google) 00:54:11 Yes, it is, unfortunately.
Josh Suereth 00:54:13 Yeah, sorry.
they're ripping apart the road, and they keep puncture… puncturing internet randomly, so that might have just happened. Any… Can you hear me now?
Braydon Kains (Google) 00:54:28 Yes.
Josh Suereth 00:54:29 Yeah, so… so I think that's… that's kind of what I'm getting at, is like, even then, you know, I might have two NICs, and so I might be connected to two different networks, so which… which one is my host ID? Yeah. Right? It's a hard problem, so I think… I think what… We only have about 7 minutes left, so… and we don't have good advice for you here. I think what we can agree to is, I think you don't have a… ID that is unique.
I don't think you have an ID that's even global. Like, like, how… that question to the machine at my desk, right? If I were to tell you, in your detector.
How would you… create an ID for that machine at my desk that I literally am using OpenTelemetry to observe, but I'm not posting host ID, because I don't need to.
I run Prometheus locally on it. I send the data right to it to look at things. The only thing I'm remote observing is my aquarium controller, which actually has an IP address that I'm using for its ID. I'm not using host, right?
What would you do there, right? What are we gonna do for a cluster? That might be a way to answer that generic host ID thing.
So, maybe we spend some time thinking about that, but I do feel like there's not a good answer, and so I feel like this is where we probably need to find a way to make what Dimitri's doing in The Collector, and this notion that you can have someone else give you an ID, Somehow first class in the entity data model.
Does that… resonate with other people, like, in terms of, like, is it worth exploring the first problem?
Or should we just… Find a way to take what we all do, and make it first class in this data model.
Dmitrii Anoshin 00:56:20 That sounds reasonable to me, as far as I can understand.
Where are you?
Michele Mancioppi 00:56:26 I am not particularly bothered by not having a generic, general way to calculate host ID.
Because in reality, I mean.
Agents are going to need different ways in different environments. That's… that's a fact of life.
Josh Suereth 00:56:42 Yeah.
Right, so that's… that's kind of the way I'm leaning to. Alright, so, Braden, what we're going to propose then, to answer your questions is, we'll… we need to find a way for the host ID to be contributed by something else.
in this data model, right? Because we don't have a thing to secure. We should probably write this down.
somewhere. I don't know where you have this written down, but Already?
Braydon Kains (Google) 00:57:13 Yeah, currently it's just in semconf, like, in the attributes description.
Josh Suereth 00:57:19 Okay.
Braydon Kains (Google) 00:57:19 It's kind of loose. Like, we… this… I believe even these attributes were, like, written and documented before entities were really taking much shape. Like, it's been a long time. The AWS Resource Detector has been setting host ideas in ARN since as long as I can remember.
Josh Suereth 00:57:37 Yeah.
Braydon Kains (Google) 00:57:46 So, I don't… I wanna at least… let the other… so I didn't mean to take the whole meeting with this, I didn't… so we can move on from it now.
Josh Suereth 00:57:55 I cut the meeting in half, so that's my bad.
I'm just writing down the consensus. So what I'm writing is we need to find a way for things to contribute for other detectors… instrumentation.
We're a generic host resource attribute.
Exactly.
Not to skip it.
its own ID.
Yeah, so that's basically… what we're saying.
Good work, Andy.
Would be sent to take existing… collector, prototype, or… behavior.
and formalize it.
Alright, I think I do want to formalize the collector behavior, because I don't know if host is going to be the only thing that runs into this problem.
But let's… does that sound reasonable, Dimitri?
Dmitrii Anoshin 00:58:53 Yes, it does.
The thing is, I remember a collector can even, it depends on the order of the detectors, actually. So if you said system detector, after that, it'll be overwritten by the system. So I think maybe we need to… Either fix that or formalize as well.
Josh Suereth 00:59:14 That's… that's actually why I want to formal… I don't want people to be surprised by this. Like, if I were to have…
Dmitrii Anoshin 00:59:18 Yeah.
Josh Suereth 00:59:19 system detector and an AWS detector, and I do it wrong, and I get the wrong ID, that's hugely problematic for everybody. So we need to make sure this is, like, easy to understand and easy to get right.
Dmitrii Anoshin 00:59:30 Right.
Josh Suereth 00:59:31 Okay.
Cool.
I'm not presenting anymore, but, Crejo, do you want to talk about, informational native metadata proposal?
I can try it again. I think my internet's back.
krajo Krajcsovits 00:59:47 Yeah, I just wanted to share it as an information that, So information is the category of this agenda item, basically. That's not part of the title. So anyway, so Arva and myself have been Arwell, for longer than me joining, have been working on.
Trying to come up with a proposal for Promatus, for handling, better supporting OpenTelemetry UX, and also agentic workflows.
And in that, we are proposing some… something called native metadata.
That would make, certain kinds of metadata, like, first-class citizen. And it… I'm mentioning it here in this group because we talked about you know, handling resource attributes and hotel entities in Promatus, and this is, this has use cases related to that, and we incorporated, I think, your major requirements, which is that There should be some way to easily use these, resource attributes and entities.
And also the left-hand navigation. Most of it, this is, like, future stuff, and just reflected in use cases, but… and I think it's going to generate a lot of discussion in Prometheus.
Because, you know, we have time series labels.
And now we would have something new, which is a huge step, so I think it's going to generate a lot of Discussion, and possibly controversy.
Josh Suereth 01:01:26 One thing we love in OpenTelemetry is discussion and controversy.
Let us know how we can help, and yeah, I… honestly, the metadata join thing looks awesome.
Looking forward to trying that out.
krajo Krajcsovits 01:01:44 Thank you. We'll keep you updated as we… Goal?
Josh Suereth 01:01:49 Cool. So we're out of time. I just want to call out, there's a few SDK, PRs. For those of you who aren't on the CNCF Slack channel, the Java prototype, I got it updated. I met with the JavaSig last week. I'm not going to be able to meet with him this week, because I'm on vacation.
But, we're making progress on getting the Java SDK kind of, updated, so there'll be a flag or something that you can use to opt into entities, and then we can actually send data from Java to the collector with entities. So, Dimitri, you'll be able to get data with entities.
has been a while, so that's, that's, that's in progress. Planning to use that prototype for these, these SDK PRs, but please, if you haven't reviewed the SDK PRs, I think, I don't remember if Daniel made his updates yet, he's not here, but the second update is, The second PR is the one that I am really kind of focusing on for the Java thing, which is updating resource detectors to silently add in entity support, without breaking users. So, the thing to review there is A, does it seem reasonable from a technological perspective? And B, are we actually going to break users if we do this? Our goal is not to. So, if you can, you know, code review it with both of those things in mind.
Cool.
Yeah, and I think Jack already did a first review of this, so… awesome.
Thank you, everybody. Apologies for being late, and I look forward to seeing y'all next week.
Arve Knudsen 01:03:27 Oh, yeah.
