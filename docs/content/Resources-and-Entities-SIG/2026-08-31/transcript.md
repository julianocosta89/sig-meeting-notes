SIG: Resources and Entities SIG
Date: 2026-08-31
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth (Google LLC)** 00:35 Hey.
**Neil Fajardo** 00:41 Blue.
**Josh Suereth (Google LLC)** 00:44 How we all doing?
**Dmitrii Anoshin (Splunk Inc.)** 00:47 Hello… I'm trying to get back to OpenTelemetry.
**Josh Suereth (Google LLC)** 00:52 It looks like you're going on an adventure right now.
Are you actively searching?
**Dmitrii Anoshin (Splunk Inc.)** 00:59 I mean, I have some stuff to do, that's what, yeah.
**Josh Suereth (Google LLC)** 01:05 Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 01:05 Which takes my time.
**Josh Suereth (Google LLC)** 01:08 Oh, no, I… my joke was that you were searching for OpenTelemetry in your office.
**Dmitrii Anoshin (Splunk Inc.)** 01:14 Yeah.
**Josh Suereth (Google LLC)** 01:15 Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 01:16 There's nothing.
**Josh Suereth (Google LLC)** 01:20 Ugh, awesome.
Yeah, my cat really wants attention right now, so she's literally on top of me. Cool.
Since we have everybody, the agenda item… I had basically two agenda items, which was, one, was figuring out, I think… Dan, I approved your PR.
on the spec?
**Daniel Dyla (Dynatrace LLC)** 01:45 Yeah, like, maybe 2 weeks ago.
**Josh Suereth (Google LLC)** 01:48 Yeah, so I wanted to figure out, like, I want to get our spec things closed, And then, Figure out what we're doing next.
**Daniel Dyla (Dynatrace LLC)** 01:57 Yeah, I think it's fine to merge. Honestly, I was just waiting, like, I… I try not to merge my own PRs, so I was waiting for somebody to merge it.
**Josh Suereth (Google LLC)** 02:05 Same, and that's… Yeah.
**Daniel Dyla (Dynatrace LLC)** 02:09 I think it might be out of date now.
**Josh Suereth (Google LLC)** 02:12 Yeah, I'm looking for it now. Would it… would… let's see… It sees SDK startup specification, and then I have the resource detection one as well. So let's just go through both and see if we can merge them.
And then we can, step into other things, specification PRs.
**Daniel Dyla (Dynatrace LLC)** 02:29 Mine has open conversations, cannot be merged with open conversations.
**Josh Suereth (Google LLC)** 02:34 Yes, so we need to resolve any open conversation.
So we can just go through those now. We'll do yours first.
Share this tab… We have Carlos on it. I think Jack had questions, let's see what those are.
**Daniel Dyla (Dynatrace LLC)** 02:57 I think Jack's biggest question was about the should for synchronous detection.
Wondering why it's a should, not a must.
**Josh Suereth (Google LLC)** 03:13 Right. This is how the pros of Canadian's bitstone development is denoted elsewhere. Oh, okay. It's also just minor things that we should be able to apply, right?
**Daniel Dyla (Dynatrace LLC)** 03:21 Yeah, there's a few minor things, I will just apply them. There's a couple, there's, like, some spacing changes and stuff, too.
**Josh Suereth (Google LLC)** 03:29 Should I mention that it's accommodating JavaScript and talk about the use case? Like, I can answer this one if you want, because I think it's… hardly it's the GCP ones that matter, right?
**Daniel Dyla (Dynatrace LLC)** 03:39 Well, I… I think it depends what direction he's asking. So, if he's asking why it's a should and not a must.
**Josh Suereth (Google LLC)** 03:47 Yeah.
**Daniel Dyla (Dynatrace LLC)** 03:51 Yeah, yeah, okay.
**Josh Suereth (Google LLC)** 03:56 Alright, here's what I'm gonna say. JavaScript, Alright, to be… films.
This means… Infoam.
Unlimited data servers… Or, testing.
Review.
It's the week.
HTTP git.
to be async in JS.
I think it should have said the one.
stability here.
Okay.
How's that sound?
**Daniel Dyla (Dynatrace LLC)** 04:55 Seems fine to me.
**Josh Suereth (Google LLC)** 04:56 Okay.
Alright, then we have this. This space question, how these attributes change over the lifetime of the entity.
May change a… right.
**Daniel Dyla (Dynatrace LLC)** 05:08 Yeah, so we say they may change over the lifetime of the entity. We never specify any mechanism for that, we never say when it will happen. I think we've been discussing in this group You know, with the assumption that descriptive attributes will change over time, but we have not discussed specific mechanisms for it.
**Josh Suereth (Google LLC)** 05:32 Yeah, and we haven't… We have implementations of it that we weren't… yeah.
**Daniel Dyla (Dynatrace LLC)** 05:39 Yeah, I would say that, for the purposes of this PR, Changing non-identifying attributes over the lifetime of the entity is left for future work.
We… I mean, we may decide that we don't want them to change, but it's harder to go the other direction.
**Josh Suereth (Google LLC)** 06:03 Yeah, I'd say we leave it out for now, because I think for our… For the initial… set of things I'd like to do, which is getting SDKs producing entities.
So that the collector can interact with them.
I… I don't think we need this yet.
And you're right, I think it's easier to add this than to remove it.
Is that what you're suggesting?
**Daniel Dyla (Dynatrace LLC)** 06:26 No, I was gonna say it's easier… it's easier to say now that they might change over the lifetime of a process, or at least maybe we… we… say that identifying attributes may not change over the lifetime of a process. Like, that's the only thing we actually care about, and we could leave descriptive attributes sort of undefined from this regard, maybe?
**Josh Suereth (Google LLC)** 06:53 Yeah… This gets into, like… specification versus future-proofing implementations. Because, like, Jack's point is this is in the SDK.
Right? And we know that we might do this in the collector.
But, what mechanism allows them to change over time?
That is not gonna… that's not specified yet, but we want to make sure the implementations assume it will happen, and don't… Program it out, right?
**Daniel Dyla (Dynatrace LLC)** 07:24 Yeah, basically. We want to make sure that when we introduce it in the future, or if we introduce it in the future, it won't be a breaking change.
**Josh Suereth (Google LLC)** 07:34 Let's see, documenting that it would change.
Now, so that… They might be considered.
Breaking… SIGs on the table.
First.
Entities… that, it should not assume. Mutable.
scripting.
Tributes.
Okay.
Was that fair?
**Daniel Dyla (Dynatrace LLC)** 08:15 Yeah.
**Josh Suereth (Google LLC)** 08:20 Okay.
Then, We need to standardize for care… oh, right. Anytime we say resource provider.
It's, Java has a thing called a resource provider. Do you remember this from, like, 2 years ago, where we did all the discussions about resource provider?
**Daniel Dyla (Dynatrace LLC)** 08:36 And the naming, yeah, because Java already has something with that name.
**Josh Suereth (Google LLC)** 08:41 Yeah.
**Daniel Dyla (Dynatrace LLC)** 08:44 I… I don't know how…
**Josh Suereth (Google LLC)** 08:46 to, from.
**Daniel Dyla (Dynatrace LLC)** 08:47 From, like, a general perspective, I don't know how you go about defending against the idea that a language implements something that's not in the spec.
And, like, now that name is squatted, I… It's kind of a bummer, to be honest.
**Josh Suereth (Google LLC)** 09:08 Well, I think what his… his question now is about, like, do we need the name if we're a resource detector? I… I read through this, and I actually think this section deserves to exist, but I don't know how to respond to this specifically.
Like, the other thing is, the way you're using Resource Provider, let me, let's look at the diff version.
So we can see it in context.
If I do the rendered stuff, does his comment show up?
**Daniel Dyla (Dynatrace LLC)** 09:32 No.
**Josh Suereth (Google LLC)** 09:33 No, that… That's a miss.
Yeah, if I remember what you had in this section, right, it's a component responsible for running all configured resource documents corrected resource. Java actually has this. I think it has two of them, even.
**Daniel Dyla (Dynatrace LLC)** 09:52 Yeah, well, I mean… Every SDK that has resource detectors has something that runs them all.
It's just… What is that thing called?
**Josh Suereth (Google LLC)** 10:04 Yeah.
This is… this is legit, because that's actually what's blocking my PR, is whether or not we have a mechanism to import entities. Like, so this is like a… We say when entity support is enabled, but nowhere in the spec do we call out how to do that.
**Daniel Dyla (Dynatrace LLC)** 10:22 Yeah, well, so… We talk for development.
**Josh Suereth (Google LLC)** 10:25 Sorry, go ahead.
**Daniel Dyla (Dynatrace LLC)** 10:27 A couple of weeks ago in the spec meeting, there was some discussion about, like, whether entities should be enabled by default or not, and, like, the breakingness of adding entities. And because it is additional fields in the protocol, I think it would be safe to just… Remove that line when Entity Support is enabled, and just say, it is enabled.
**Josh Suereth (Google LLC)** 10:52 Yeah, and then just state it must occur first, followed by resource attribute merging.
**Daniel Dyla (Dynatrace LLC)** 10:56 Yeah, exactly, just remove the conditional, and entities… there is no enabled, disabled.
**Josh Suereth (Google LLC)** 11:08 Based on other specification discussions… the other social media in… And the other PR… the other PR… discussions. Okay.
Cool That sounds reasonable for that one. This one here, though, around resource provider.
Section above, detecting reads a lot like this content. So, where's the detecting… That's Entities.
Oh, you know what it is?
Dan, I think it's this, it's stuff you didn't change.
This pre-exists your spec.
**Daniel Dyla (Dynatrace LLC)** 12:00 Yeah.
**Josh Suereth (Google LLC)** 12:03 And so, I think what he's saying is this basically should replace this, in some fashion, or we need to figure out how those two interact. I think that's actually a fair ask. Yeah, go ahead, what?
**Daniel Dyla (Dynatrace LLC)** 12:16 Yeah, or just merge them together. I guess…
**Josh Suereth (Google LLC)** 12:18 Yeah.
**Daniel Dyla (Dynatrace LLC)** 12:18 Yeah, okay.
**Josh Suereth (Google LLC)** 12:20 But this… this helps answer one of the big problems on my PR, which was, like, the interaction between schema URL and merchant Entities first, and all that kind of stuff, so I really do want to make sure yours goes in first, upon rereading both.
Okay. You're okay figuring out… I'll make a… I'll respond to Jack's comment here from the SIG.
Wait, how do I get back to just his comments? SourceDiff? Okay.
Because the other ones, I think, are somewhat minor… rates.
discuss this in Entities SIG… We'll merge these two sections together.
Amazing.
Holy cow.
resource provider… It's responsibility to use. Weird, less ambiguous.
specifications… Alright, so we had already discussed about that previously, I think.
The notion that, like, having a thing called a resource provider that has its responsibilities to make a resource Is better than the current spec, where it's like, hey, someone has to do this, but it doesn't actually declare anything that's responsible for it, it's just the SDK does it. But the SDK is split into three components, so we're actually saying, hey, there's a thing called this, it does.
So, I want to make sure that that doesn't get lost in your… in this thread.
Okay.
**Daniel Dyla (Dynatrace LLC)** 13:53 Right.
**Josh Suereth (Google LLC)** 13:55 Cool.
Sorry, go ahead.
**Daniel Dyla (Dynatrace LLC)** 13:59 No, I was just confirming.
**Josh Suereth (Google LLC)** 14:02 And then Creo had one here. From Tensor's point of view, when I see descriptive attribute be created changed from empty, should it set it retroactively in the database, or is it ever only valid from the point when it's set? Not sure we could solve it retroactively, to be fair.
I can respond to this. This is a, kind of state thing.
Okay.
scripted.
It's similar to how you would, some of the You state metrics?
Like, pod state.
Green, when… Spooked it.
It should be… may be useful.
Conservability signal.
Treat it as a time series.
Jose… Tell me what's latest.
Oh, this… Great.
My shot.
Oh, this type series.
Okay.
That's just an answer from the data model. I don't know if you guys want to nitpick what I'm saying here before I just write it.
But that's being written from me, not from the SIG.
Does that make sense, what I wrote, though?
**Daniel Dyla (Dynatrace LLC)** 15:37 It makes sense.
I'm not… Yeah, I think it does.
**Josh Suereth (Google LLC)** 15:47 Yeah.
Oh, I'll just follow, yeah.
Recommendation for Prometheus… Remember when you saw the descriptive attribute first?
Treat it on your seriousness. Okay.
Cool.
I think that's all the main questions. This just seems like a… I don't… I don't know what this actually is. Is he just adding this extra space?
**Daniel Dyla (Dynatrace LLC)** 16:18 There's no, blank line before the heading.
**Josh Suereth (Google LLC)** 16:21 Okay, okay.
Yeah, and here, I think that would make sense, yeah. Cool!
Okay, let's look at the other PR.
If that's okay. Unless there's any other concerns with that one.
Because I think with those changes, I'd be willing to mark those things resolved and merge it.
On my PR, We had 20 comments, but I forget how many are opened.
Danny, you haven't approved.
**Daniel Dyla (Dynatrace LLC)** 16:46 Oh, I haven't… I haven't approved it yet. I thought I had.
**Josh Suereth (Google LLC)** 16:50 Well, I think the reason why is I still have the entities enabled here.
And what I'd like to do is when yours is merged, I was gonna merge against yours and remove it at that point.
And then send it out for review.
**Daniel Dyla (Dynatrace LLC)** 17:06 Got it, okay.
**Josh Suereth (Google LLC)** 17:07 Because I want us to agree on that decision, but basically, we're not going to have an experiment-enabled thing, and I need to go update all this to remove that. I can start updating now, but I want to merge against your PR, so I'm, like, a follow-on, right?
Yep. That way, I can get rid of some of my language to reference yours. I think the other thing, Dmitrii, you had something about… We need to reconcile OTIL resource attributes and OTIL entities before adding the detector.
what… I forget how… I think with Daniel's change.
this will be resolved, but I need to go check.
Because I think what's… the way this is phrased, and then with your change around that resource provider, I think it'll be very clear when things happen.
But we should… we should check. The… the thing about the env… resource detector, though, is I don't know if it's going to be default on, from what Jack was saying with config.
Like, you have to opt in to have config for that to be used.
**Dmitrii Anoshin (Splunk Inc.)** 18:18 But hotel resource attributes are on by default, right?
**Josh Suereth (Google LLC)** 18:24 Otol Resource Attributes is on by default, yeah.
**Dmitrii Anoshin (Splunk Inc.)** 18:28 So, there's kind of… Any consistency here in that case.
**Josh Suereth (Google LLC)** 18:33 Yeah, well, that's one thing I need to resolve. I actually thought that we had a default config for the SDK, but it turns out we don't.
**Dmitrii Anoshin (Splunk Inc.)** 18:41 Okay.
**Josh Suereth (Google LLC)** 18:42 So, I think I… yeah, need to do a little bit more investigation on that one.
Yeah.
This one… some kind of possibly annotations. This is, This is an active discussion, actually. I'm gonna mark this as resolved.
We're actually discussing that with Config and Weaver Semcov. So this is really the only open question, Dmitri, and then… Dan had some comments on, right here.
that I will… I'll remove the experimental enablement.
Okay.
Cool. So I'll do some follow-up. Dan, if you update your PR, I'll update mine, and we should be able to get them both merged. One thing I will note, which I think is ironic, this one has enough approvals to merge, but not from this SIG.
**Daniel Dyla (Dynatrace LLC)** 19:33 Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 19:34 Sorry, I can follow up as soon as… Beautiful.
**Josh Suereth (Google LLC)** 19:37 No, no, no, it's fine. It's not… it's not a cost, it's like, you… everyone else agreed to it, but we didn't agree to it. And then, I think on Dan's, we agreed to it, but no one else did.
So, another side note, I was talking to, I think David Ashpel.
And I'm planning to spend more time in the spec meeting on entity-related things. Possibly, if we end up with, like, a lot of canceled meetings and canceled agendas, I think right now we're basically blocked on spec work.
and getting things to the spec. So I want to spend a lot more time there on our issues, like getting things through.
And then Dmitrii, I know all the collector stuff that you've been working on has been on hold for work-related things, so I think we're gonna… I'd like to get to a point where we have, entities usable for everyone in some modest fashion.
And then to kind of pick up that work when you have time, or some of the rest of us can maybe stand up and help you out with some of that work. Because I think the relationship modeling work you were doing is critical.
To start, as soon as we get the SDK stuff out.
**Dmitrii Anoshin (Splunk Inc.)** 20:46 Sounds good. Yeah, I'll… I'll… yeah, I'll… Give some updates by the next SQL.
**Josh Suereth (Google LLC)** 20:52 Okay.
Cool. What I'm afraid of is we might be at one of those points where we exhausted our budget on this project, if you will, and so people are kind of burned out, and so for the relationship modeling, I actually want to kick off a new project.
around it. Like, basically shut down this SIG and kick off a new project around entity relationship modeling, and call that Phase 2.
**Daniel Dyla (Dynatrace LLC)** 21:16 What's the advantage of that?
**Josh Suereth (Google LLC)** 21:19 Basically renew the hype cycle, get people excited, get people to join, that sort of thing. Like, it's, yeah.
But it's, it's, it's a, a, marketing technique to try to renew… Yeah.
**Daniel Dyla (Dynatrace LLC)** 21:35 I guess if we end up with the same people, we're not any worse off.
**Josh Suereth (Google LLC)** 21:39 Yeah.
But it also could be that, like, if you don't have time from work, you know, we can't get there, so… Alright.
Cool. But that would be, I'm gonna call that… Let me put the other note here, so that would be Phase 1, Phase 2 plans. We always plan on Phase 1 being, SDK collector work, and Phase 2 being relationships, right? So that's why I do think that we could call Phase 1 done, and basically say, okay, here's our plan for Phase 2, and all the thing… all the work we know we need to do.
**Daniel Dyla (Dynatrace LLC)** 22:14 That makes sense.
**Josh Suereth (Google LLC)** 22:17 Cool, I might have to drop at 1.
I, I, there's a meeting that I'm optional for.
That I'm trying to get out of, but I haven't confirmed whether or not I can skip. So, with that, let's go to Rob's question quick.
**RC Rob Cowart** 22:34 There we go.
Y'all actually mentioned something that I did Oh, I gotta wait for you to stop sharing.
Oh, probably.
**Josh Suereth (Google LLC)** 22:48 I can stop sharing, yeah. Sorry.
How do I get out of this? Did it stop?
**RC Rob Cowart** 22:55 Pawar now, yeah, we're good.
Yeah, there we go, that works.
So… Again, just for those that didn't know from previous calls or don't recall, we… a new network SIG was kicked up a number of weeks back, and we've been starting to, Create some of our initial… semantic conventions and things, so we're very much in a work-in-progress stage, and the idea is to first Create some core entities?
And then after which, we'll start to flush those out more with metrics and other things as well. We're still getting our final place for our stuff to land, so at the moment, we have a few things on a public repo that's… We just shared under our, Elastiflow's GitHub org, but we'll move this stuff over as soon as a few more, housekeeping items are taken care of so we can start getting PRs and stuff, posted. I did want to mention one thing, though. The comment was made about, Descriptive things being immutable.
We kind of were depending on that, actually, quite frankly, as it goes. So, like, for example, network interfaces. Generally, I think the network interface name is the thing that is, probably the immutable item, which is why it has a role as being the identity.
However, there are things like a description or an alias. You know, an alias might have something like.
this is the ISP link to Verizon, or something like that, right? And it very well could change, you know? Someone, they might change the naming convention, they might change it to be, this is the link to site XYZ, you know, and so… As it goes right now, we have been assuming that descriptive things are immutable, so if there was a desire for that to change, then it'd be great to know now, and where we would then put this.
**Josh Suereth (Google LLC)** 25:05 So, yeah, we always expect a description to be mutable.
the discussion was around inside the SDK.
So OpenTeleTree SDKs are designed around an immutable resource, and some of them might actually really struggle to make it be mutable. Whereas if you're doing, like, brand new instrumentation for networking that doesn't go through an SDK, you're fine.
**RC Rob Cowart** 25:29 Got it, perfect. Okay, that's good to know, thanks. So what we wanted to talk about, and this would… this particular one was a good example of this, is we were trying to think of… you know, What's gonna be the general direction of naming conventions for where we're going?
And while everything we're doing is under network, we got… we took this example, BGP Peer, and it's relevant for a particular reason, that there are already some existing attributes under, like, network.local.address, network.peer.address, some things like… so the question is, like, what what kind of naming convention makes the most sense? We don't want to step on… Anything that is already existing unnecessarily, but at the same time.
we want a consistent naming convention or way to think about it, you know? So, what we were discussing today, and by the way, it just got suggested, we should ask the Entity SIG what they… what they think, because one of the ways we were thinking of is, okay, everything's under network, and maybe the next thing should be The, like, the entity type, and then things come after that as kind of a clear delineation.
And what I've done here on this page is I've kind of made examples of… of four different ways to do it.
One which is… and actually, two are very similar. The only difference is, are we dotting between BGP and peer, or is… because the entity is a BGP peer, is… should it just be one thing?
And I should note on this, by the way, one of the questions we had on a previous call was.
do we perhaps even suggest we should throw away those original network local address network, or deprecate them, you know? So we went through this particular set of entities to see, like, can we actually keep those? It turns out we probably can, actually, which is good, but the, But then again, when we get into naming, for example, one conversation was.
is this BGP pier, or is it pure BGP underneath the existing pier that's already there, for example? And that's probably the main thing I would be… I would be curious about, if there's any input on… should the entity name, or the entity type, be at all part of the attribute names? Is that the way it's envisioned? Or are the names completely irrelevant to that? And, And there's some other way that would need to be in this record when it gets put on the wire that you know this particular network peer address happens to be talking about network peer address for a BGP peer, because it knows that from attribute or entity type somewhere in the payload, right?
**Josh Suereth (Google LLC)** 28:34 Yeah, so, you're walking into two things, so I'll talk about principles, and then, we can talk, like, there's a few things we've debated back and forth around the actual protocol, but we'll get there, because it's not an easy answer. The first easy answer is generally, right now, at least for all identifying attributes.
we have not found a need to deviate from this pattern, where the entity has a name, and that name becomes a namespace for all the identified attributes. In fact, for a lot of our entities, it's also the namespace for the descriptive attributes, or for a lot of them, right? So if your name is network.local, right, Then network.local.whatever would be your identified attribute for that thing.
But again, it depends on… we haven't… I think you've done the most aggressive modeling so far with entities.
Why not barely…
**RC Rob Cowart** 29:27 So that's not a good thing, I think.
**Josh Suereth (Google LLC)** 29:29 Well, no, by aggressive, I mean the domain you're modeling. Networking is a very topological, heavy, intrinsically complicated domain.
Kubernetes is, by design, not. Right? And the VM, you know, modeling that we've done is light, and the service modeling, by design, is a lexical mapping, where we have namespace, name, and then instance, right? For services.
But that's… you can consider that, like, a deployed application, or a deployed service on, like, Cloud Run, or in Kubernetes, or on VMs. Like, that's… that's the modeling we've done so far. So this is probably the most robust modeling, which I think means you're gonna give us a lot of good… We're gonna have a lot of good discussions here about relationships and entities and really push on the model.
What you're getting at next is one of the limitations we have with how we're embedded in OTLP, to not break things. Only one entity can own an attribute at a time.
in OTLP, Four metrics, logs, and traces that are reported.
That doesn't mean that you can't have… the model you have, it just means that you'll actually be engaging with the entity signal Dmitri's been working on, which is saying, here's the topology of the network, and pushing that out as a thing. But for any individual, like, metric, it would be reported against an entity, and you would not have The same attributes show up in multiple locations in the, like, entity identity of the metric.
Does that make sense?
**RC Rob Cowart** 31:05 Yes,
**Josh Suereth (Google LLC)** 31:08 Okay.
**RC Rob Cowart** 31:10 Okay, so what you said starting out, that the… it would start out with the entity name, so in this case, a… I would argue a network BGP peer is the entity.
So… so it would be correct. This naming would be then more correct than attempting to… Down here, for example, reuse the existing network, local network peer stuff.
**Josh Suereth (Google LLC)** 31:44 Yes… I think. But I, I'd like… That's where the devil gets in the details. Dmitrii and Dan, I don't… do you guys have any… thoughts from our other discussions on this? I don't want to be the only one suggesting things.
**Dmitrii Anoshin (Splunk Inc.)** 32:00 Unless, network local, isn't a separate entity. I think that makes sense. But… I'm in… If you can… if you can… actually, no. If you can think that network local is some part of an entity, in that case, it makes sense to put a different… it makes sense to put the peer as a separate entity. But if network local is some kind of a namespace.
that potentially is applicable to other entities under it, and for the BGP peer.
In that case, maybe we can reuse that. I mean, if… If there is no… if there is no conflict between different entities in that case. Does that make sense?
**RC Rob Cowart** 32:50 be more like… The last one, which is… it's actually a mix of these two.
**Dmitrii Anoshin (Splunk Inc.)** 32:58 winning…
**RC Rob Cowart** 32:59 Good thing.
stable.
network peer, address, port, and the local equivalent. We use what's already there, because they fit that thing. But for all the other things, all the other attributes of this BGP peer, they all start network BGP peer.
**Dmitrii Anoshin (Splunk Inc.)** 33:22 I see, so we have, we are building against existing conventions, essentially, and in those conventions, we already have network peer and network local. Okay.
**RC Rob Cowart** 33:33 That's the challenge, is there's a handful of things that already exist that people have already used, and we want to try to avoid stepping on them You know, or creating confusion, or unnecessarily duplication of stuff if you don't have to. It does create, within this set of, you know, attributes for this entity, it does create some inconsistencies in the naming.
But it does work, you know?
**Dmitrii Anoshin (Splunk Inc.)** 34:03 Yeah.
**RC Rob Cowart** 34:03 Oh.
**Dmitrii Anoshin (Splunk Inc.)** 34:04 I think in that case, we should, like, figure out what would be the entities for the existing ones, maybe even before, but at least, at least at the same time when we introduce new ones, because if we introduce new entities and do not consider existing attributes and how they map to other entities, but in that case, we can potentially run into the problems. Does that make sense?
**Josh Suereth (Google LLC)** 34:29 I think, Rob, yeah, Rob, correct me if I'm wrong, all the things you're reusing are already only descriptive attributes of other entities, is that right?
**RC Rob Cowart** 34:41 I'm going to say that I believe so, although, like, this one here is this peer relationship.
the… the address of the peer is the identifying thing. So if we reuse that field, even if for everyone else it's a descriptive, it would definitely be an identity for this peer.
Okay, so I'm not for this entity.
Right.
**Dmitrii Anoshin (Splunk Inc.)** 35:05 In that case, we would need to think about network peer entity, if we can somehow Like, flesh it out.
**Josh Suereth (Google LLC)** 35:13 But… but a network peer… okay, so… Again, going back to the point I was trying to make… yeah, go ahead.
**RC Rob Cowart** 35:20 The… the current network local and network peer, the best way to describe them are… they are the endpoints of some type of network connection, network relationship.
So, like, this thing talks to this thing, or this thing has a connection to this thing. So… so they're… they themselves… I guess if you were to say what they are as an entity, I'd probably call them a network socket.
Is the entity?
or a service access point, that might be the other way to refer to it. Some organizations might, but at its core, it's a network socket, you know, IP port number, protocol.
**Dmitrii Anoshin (Splunk Inc.)** 36:03 But we also have, this kind of, different, like, generalization of the entities. We can say database as an entity, which is another entity, let's say MySQL database. So in those… in that case, those are two different entities. I'm thinking if we can apply something similar here, so we'll have network peer as a, like, call it abstract entity, and at some point, it can be referenced to something more specific.
**RC Rob Cowart** 36:32 And this is where we get into relationships, because it's really going to be… we have two network sockets.
a… network local and a network peer. They have a connected-to relationship with each other, which happens to be… and this is where we get to… what's that type of connection? Well, in this case, it's a BGP peering session.
Right.
In another case, it might be… it's carrying web traffic, or it's doing what… but, like, in this… this has a particular meaning in this case, right?
Okay.
**Josh Suereth (Google LLC)** 37:12 Yeah, the… So, so the, A few things that I've been thinking about with this. So, one is, when we have, like, net… peer.
in OTEL Now, it usually shows up not on the resource as an entity, it usually shows up actually in, like, the metric, or the span that's being recorded.
So, we don't have this yet today, but it's something we've discussed, which is, like, the notion that you can have an entity on a signal.
So you could have an entity that talks about, like, you know, this network socket talking to that network socket. You'd have a metric that describes network socket A to network socket B, how much traffic is flowing through it.
That would be, like, your latency metric, your count, request count, whatever, you know. Bytes in, out, that sort of thing.
Network peer, from what I remember, I don't think shows up as an entity per se, but as, it might be an entity in the model, but in reality, the way we use it is as a metric attribute.
So there's… there's a bit here where, like, the flattening of attributes and crap that we have is at a resource level, not at a scope level, and these relationships are important. Some of them, I think, are things you discover from watching data, right? So, like, if I have a metric that says.
point A is talking to point B, I can use that to extract a relationship.
And then there's the entity relationships that we're talking about, where you kind of know ahead of time, like, I'm configured to do X. So, in Kubernetes, I have a set of relationships that are configured, where there's, like, an independent view.
I don't necessarily want to blend those two problems together in the same solution, so… The model should be able to account for both.
But the way that the data's reported might actually be different.
That's just one point I want to make as we all think through this. So, like, Dmitri, the thing that you have around reporting entity signals out of the collector.
Does it make sense for us to have this notion of, like, inferred relationships, where if I see port A talking to port B, I'd report a relationship across the entities?
Or do I just report the metric that has implicitly that A and B are talking, you know, and the entities show up on In there.
I know I'm not taking this towards your modeling, necessarily, but this is kind of, to me, really critical when we think about entities and when we think about signals, is… I'm reporting signals about a thing.
I'm reporting signals about two things communicating, right?
**Dmitrii Anoshin (Splunk Inc.)** 40:03 Yeah.
That was a… we discussed that some time ago, and I think what we were… the direction we were thinking is that, actually, what you mentioned, when we reference entity from the signal itself, from the metric, from the data point. And in that case, the metric itself can reference two different entities, like, let's say, source and destination.
But in that case, well, what's in the resource? And in the resource, it's potentially something… Like… on top, like, overarching, I don't know, network, some kind of… I don't know, what can be… Between two things.
Connection, or something.
**Josh Suereth (Google LLC)** 40:51 Yeah, a network connection, or, We can also have something where you report the data as if it came from source.
And in the metric is the destination entity that you're talking to.
**Dmitrii Anoshin (Splunk Inc.)** 41:06 Maybe, yeah. But this kind of involves some sort of, Lex… Contacts that we need to… provide, saying that source is always the most, like, the owner of that metric, which sometimes might not be the case, might confuse people, I guess.
**Josh Suereth (Google LLC)** 41:29 I do think resources are the owner. Go ahead, Rob, sorry.
**RC Rob Cowart** 41:32 I do think there is a difference, though, between, like… network traffic connections that can be very ephemeral, and something like… like this, like a BGP peer peering, you know, two BGP routers talking to each other that gets configured once and changed in 5 or 10 years, right? You know? So, And in that case, that peer relationship, to me, is a… is a unique thing in and of itself in that context. In other contexts, I can definitely see your point.
You know, like, a given system application talking to one of 20 things You know, randomly when it communicates, but it's not long-lived conversations, you know.
**Josh Suereth (Google LLC)** 42:22 Yeah.
So, yeah, I guess my overall point, though, was there's a few… you're hitting on a few unresolved discussions and entities. One is, the need to share some of these attributes, or have, like, the same entity with a different role.
in… in the thing that you report, right? So this notion that I have a source and a target as a role, so if I have two PGPs, or, sorry, why did I say PGP? BGPs.
As peers of each other.
and I want to report something about the two of them together. How do you do that? Like, you can model them as entities, great. Like, we know how to model them, but we want to make sure that the relationship's in the part and hotel. So, like, one of your questions around, can you share attributes? Today, the answer is on a per-signal basis.
You cannot share it, like, you cannot share an attribute for the source or for the actual signal itself.
So you have to caveat one of them with, like, this is the destination… you know, scope of those sets of attributes, or this is the source scope of those sets of attributes. And you see that in Semcov, with, like, I think we actually literally have source and destination, and we have, client and server, right?
So that, that's kind of showed up in SEMCOMF, but we haven't… I, like, I think we need a better model around this, especially as you dive into networking, where we're gonna have to address all of it real hard, real fast.
go ahead.
**RC Rob Cowart** 43:53 I, I think, I think then… what I probably would like to do, and you just tell me if this is a good way forward, because I don't want to, you know… I sometimes think the best way is to have enough examples, you know, so that can be talked through, is… I think I… what I… what I feel like I want to do is… For now, do this combined method here, where new attributes will have, like, be named under whatever this entity is.
If something exists already, we will… we will use it. If later it's decided, that's not the best way to… we shouldn't reuse it that way, although I will say in this particular case, I think we are going to go back and define, like, a network socket or something like that as an entity, and then… Create a relationship there, but, But nonetheless, I think that's the path then, it sounds like, to go down. Get some more of these done. I'll probably then try to make a diagram of how we feel they are related.
And then we can maybe go from, But there's somewhere at times where GitHub stinks, and it's tough to make diagrams that can be more interactive, but everyone on OTEL needs a Miro subscription. That works pretty good.
Or Google needs to come up with a good, good thing to add to the Google apps, the diagram stuff. Anyway,
**Josh Suereth (Google LLC)** 45:25 Are you saying Google Drawing is not good? Because I think a lot of people would agree with you.
**RC Rob Cowart** 45:31 But anyway, we will, we'll, we'll come up with something to better, kind of graphically, because I think this is also, like, reading these tables gets to be a challenge, and something graphically to go through it for a future call. Okay, that helps to move forward, at least, I think.
**Josh Suereth (Google LLC)** 45:47 I think that would be ideal for us, because the other thing I want to have happen out of this discussion is we start pushing on the model and finding flaws in it fast, and we start pushing on the relationship design, because we still have a lot of flexibility with that.
**RC Rob Cowart** 46:01 Okay.
**Josh Suereth (Google LLC)** 46:02 Yeah, so that'd be ideal. I think, again, you're pushing on… we made a bunch of decisions early to move forward.
where there was a lot of debate about them. And, this is where the rubber meets the road on, like.
Actually making the design work and real.
**RC Rob Cowart** 46:18 Okay, this was helpful, so I think, I think that'll help me to move forward, and just understanding, as we said on the call today, it's like, okay, we don't have to decide this right now, final, this is just a draft anyway to pro… to then get conversation going, so… Yep.
**Josh Suereth (Google LLC)** 46:36 The other thing I'd recommend, if you're on GitHub.
And you have a visual representation of something.
I have had success asking AI agents to take my drawing and turn it into mermaid diagrams.
**RC Rob Cowart** 46:49 Oh yeah, that's better.
**Josh Suereth (Google LLC)** 46:50 Because I hate making them myself, but…
**RC Rob Cowart** 46:52 Yeah, yeah.
Yeah, that's good.
**Josh Suereth (Google LLC)** 46:54 Okay.
Alright.
**RC Rob Cowart** 46:56 Cool. Thanks, gentlemen.
**Josh Suereth (Google LLC)** 46:58 Thanks, and see y'all.
**Dmitrii Anoshin (Splunk Inc.)** 46:59 Oops. Right.
