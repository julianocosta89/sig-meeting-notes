SIG: Semantic Conventions SIG
Date: 2026-08-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 02:46 Hey, folks.
We'll give another minute here.
I see at least… Oh, let's see, I can do better than that. Let's see… what do we… No, I guess.
There we go. Go ahead and fill in your name, and anything… go ahead and add to the agenda.
So, I'm guessing that, Ludmila added this, unless it was you, Jay.
So, we'll… I can talk a little bit about that.
So, if you haven't seen, We have a new repo, Semantic Conventions Conformance.
And, I'm trying to… oh, yes.
Oh, is this the first Semantic Convention meeting on the new LFX?
Platform.
I saw that.
Joao was trying to join.
So… this is the issue, if you want some… oops, what did I click on?
I'll add to the meeting notes… Okay, hormones… So what this is, is, it was kind of a prototype, done some prototype work, in terms of… let's see if we can see… Sort of, initially, it came up around generative AI, of trying to… there's so many different instrumentations, Gen AI instrumentations, emitting so many different telemetry shapes and conforming somewhat, or not at all, to Semantic Conventions.
That we wanted to be able to… Sort of start, Cataloging that and trying to, push people to conform by saying, hey, here's this dashboard, you're not following this, and give that to… users as a place they can use to decide which instrumentations they want. Hopefully, they want things that conform to the semantic conventions.
But then, we had the idea that, hey, this is actually… could be useful for other things as well, like HTTP, to see, you know, what different HTTP libraries We instrument and… How much they conform to semantic conventions as well, which attributes they emit.
And… so… Which is a question also that has come up in the past… We find… Let's see, some other issue… HTTP… Yeah.
Like this. So this had been a request from, some folks to be able to understand the, how much of our… our HTTP Semantic Conventions has been updated to the stable HTTP Semantic Conventions.
So, this would give us kind of a way to do that and run tests continually against those and produce, reports.
Not sure at this point where those reports will live and in what form.
Jay, there's definitely some, Opportunity for… I want Explorer.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 08:55 Yeah, Explorer.
Yeah.
**Trask Stalnaker (Microsoft Corporation)** 08:58 Okay.
There's some cool stuff over here, which… there's definitely, some interesting overlap opportunities as far as, This is sort of… A potential replacement for, or much more detailed information than the current, registry.
And so, similar to… similar idea, this is the Semantic Convention, conformance.
Has more detailed information about individual instrumentations that people could consume.
So, we've got a new repo, There's another goal from this, which is to be able to share these conformance tests to let repos run them, so the Python GenAI repo is the first, kind of, consumer of this tooling, that they can run the conformance tests in CI, and actually, like, fail CI if it's not conforming. So, we're kind of hope… hoping to get sort of the best of both worlds, where we enforce this upstream in the instrumentation CI themselves, as well as we have this sort of Global report across all the instrumentations that will just bump, you know, version by version.
So if you're interested in this stuff, come and watch, There's a couple of… yeah, we're just kind of… just barely seeding some of this stuff, and the goal will be to start seeding, sort of, things… one by one, especially for, like, the HTTP, Or at least language by language, so that we can, you know, I'll CC the maintainers, those language maintainers, instrumentation maintainers.
So that they can also review these and kind of see what's happening.
Any questions about that? Yeah, Riccardo.
**Riccardo** 11:14 Hey, first of all, thanks a lot for this. I was working on something similar.
For running it in the open… on the Python country CI.
So it would just, like… Accepting a test.
But this, like, this is way better, so, like, thank you.
I'll… Follow this work, and hopefully being able to also… help, with the Python.
instrumentations. Like, I've seen that on your repo, you already have, like, a ton of instrumentation covered already?
And so, yeah, maybe I can help importing some of that to… With new repo?
So…
**Trask Stalnaker (Microsoft Corporation)** 11:57 Yeah, awesome.
Yeah, and definitely check out, the work that Liudmila's doing in the Python GenAI repo.
as far as… Reusing the conf… these, the tooling here.
**Riccardo** 12:21 Yeah, we'll do, thanks.
**Trask Stalnaker (Microsoft Corporation)** 12:27 Alright, let's, move to our… Next and last topic.
Kathie… Hey!
**Kathie Huang** 12:39 Hi, I just wanted to raise this PR again, since it's been about a month since I first put it up. Oh, did you just…
**Trask Stalnaker (Microsoft Corporation)** 12:49 No, these are pending that I have. Oh, gotcha. This is probably some… AI… probably… yeah, anyway. Okay. Yeah, I haven't posted that.
**Kathie Huang** 13:02 Gotcha. Sounds good. Yeah, I was, like, happy to split up this PR into two, because initially it was just the replica name, but after some review, I added the revision name, but that's, like, the part that has been having more discussion.
So happy to split that up if that makes the review for each one separately quicker, or happy to ping anyone else you think may be helpful to… to ask for a review from. But, yeah, just wanted to raise this again.
**Trask Stalnaker (Microsoft Corporation)** 13:37 Yeah, yeah, apologies, I definitely want to spend some time on this. I need to, re-familiarize myself with the Azure Container Apps.
The… and I haven't had the time, The… let's see, as far as splitting it… Yeah, so this is adding… just adding these two attributes.
**Kathie Huang** 14:10 Yes, just adding those two attributes, and then creating two entities to, like, identify them.
**Trask Stalnaker (Microsoft Corporation)** 14:19 Two… two entities, or one entity? Two entities.
**Kathie Huang** 14:23 the, yeah, the Azure Container App instance is its own entity, and then the Azure Container App is a separate entity, following, like, what the service… Semantic convention, kind of set as a precedent.
like, service.name, I think, is the identifying attribute of a service, but then, like, service instance ID is the identifying attribute of a service instance.
**Trask Stalnaker (Microsoft Corporation)** 15:06 Okay so if it was split, it would be two PRs, one that adds… This plus the entity… the instance entity, and one that adds this, and adds the… Entity.
**Kathie Huang** 15:27 Yeah, correct.
**Trask Stalnaker (Microsoft Corporation)** 15:30 Yeah, do you feel like they're independent?
**Kathie Huang** 15:37 Not super, since it's talking about the same workload, but I was just wondering if, like, that would help, like, make review easier, potentially? Or maybe it's better to actually just review it together.
**Trask Stalnaker (Microsoft Corporation)** 15:53 I haven't… yeah, I, I… it's not a particularly big PR, and there's just these two, so unless we find some issues with one… Or the other.
It's probably okay.
**Kathie Huang** 16:10 Okay, sounds good.
**Trask Stalnaker (Microsoft Corporation)** 16:12 VR.
**Kathie Huang** 16:12 But, yeah, sounds good.
**Trask Stalnaker (Microsoft Corporation)** 16:15 Yeah.
**Kathie Huang** 16:17 Sweet, yeah, let me know if there's anything else I can do to push this along, but… Just… This is one to raise it.
**Trask Stalnaker (Microsoft Corporation)** 16:25 Okay.
**Kathie Huang** 16:26 Yeah, thank you.
**Trask Stalnaker (Microsoft Corporation)** 16:32 Sven.
**Sven Cowart (ElastiFlow Inc)** 16:34 Hey, Thrask. I just… I didn't know if I was ready yet to talk about this quite yet, but I'm gonna bring it up anyways, just to see if there's any context that you would have… This… Conversations around local and peer versus source and destination.
Keep coming up.
And it seems like, based on GitHub history, they've come up in the past before, and confusion about when to use which one.
I'm trying to make sense of it myself, and it's not very clear, which is concerning.
So… I don't know if you have any history or context around that. I do know local piers stable, so changing them would be tough.
I think where a lot of this is coming from is… folks want to show a directionality, and the things that they're applying these attributes to, and local peer makes that difficult, versus source and destination makes that much more clear.
But I think the… And my understanding of the situation right now is… I'm thinking about it more broadly.
is… Based on the implementation.
Someone could opt for either, which makes it hard for the observability backends to make a decision around what should we standardize on? And maybe it's… Yeah, I think… I think that's the statement. I'm not quite sure. I'm still trying to work through this in my head right now, because it just came up this morning.
**Trask Stalnaker (Microsoft Corporation)** 18:23 Yeah, so, would definitely… like the… I remember when we kind of went through… we used to have, sort of, local peer in more places.
And we went with, like, client server, to… because we wanted that, For the same reasons you wanted, you want, so I'm trying to Remember why we didn't… Do that for network… Local and network peer.
**Sven Cowart (ElastiFlow Inc)** 19:03 I'm wondering if… If the best thing is to move to source or destination is the advice in most cases.
and deprecate local peer, but I… I need to first… the reason I was hesitant is because I don't know the usage of local peer across the ecosystem, and I need to make sure I understand that before that's the, official advice that I would give, but, that's kind of where I'm at with it right now. I… I'm being very open-ended and ambiguous, but… Not very hopeful.
**Michele Mancioppi (Dash0 Inc.)** 19:41 Does that bring up that also the, Pr dot is also challenged as a semantic convention in terms of services.
So it's, at no level of these proposals, there is, unfortunately, consistency and agreement across the various Semantic Conventions.
We have now merged a, For example, we have service.peer and service.namespace in the Semantic Conventions. That was supposed to be the successor of peer.service.
It was, like, insta-deprecated the moment we bursted.
Trask is laughing, still crying about it. And I don't know where we're going to land.
**Trask Stalnaker (Microsoft Corporation)** 20:32 I think we have… I think there's agreement on that, that we just haven't implemented it, so… Pierre… yes.
I think… There was… I think there was agreement on this proposal.
We just never implemented it.
**Michele Mancioppi (Dash0 Inc.)** 21:03 Sven, to my understanding, the answer to Sven's question is… Replace service with network, and off you go.
**Trask Stalnaker (Microsoft Corporation)** 21:15 Yeah, let's look at… because we do have source and destination.
Right.
Elsewhere… Source destination…
**Michele Mancioppi (Dash0 Inc.)** 21:31 Wait, I actually remember a discussion a few, like, a couple of months ago from somebody else from the network SIG that came in, and if I recall correctly, they said the source and destination means something completely different in the domain.
And that would be confusing for practitioners.
**Sven Cowart (ElastiFlow Inc)** 21:55 That's weird, because… I wouldn't agree with that. If you look at flow data as a thing to describe it that uses source and destination, like the IENA IP fix standard.
**Michele Mancioppi (Dash0 Inc.)** 22:09 It's a… it's a hazy recollection on my side. I hope I'm wrong.
**Sven Cowart (ElastiFlow Inc)** 22:13 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 22:17 Sven I wonder if maybe part of the thinking is that when you, for example, what… Whether you know whether you're a source or a destination.
**Sven Cowart (ElastiFlow Inc)** 22:33 That's… that's… that's kind of where I arrived right before I joined the call. I was like, is that it? Is that when the scenario becomes applicable?
**Trask Stalnaker (Microsoft Corporation)** 22:42 Because, like, if you… We do have… I mean, the idea was that, so we've got client server… So logical… For… When you know, like, a TCP… style… And we've got source, destination… logical layer… Kind of universal… say, like, UDP or anything else that, broadcast So, I mean, I'm curious if you can, like, for modeling, network layer.
I was kind of assuming you would use source destination, the top-level source destination.
So, see if that… Works, if you even need the network?
Curious if you even need network… local and network peer?
**Sven Cowart (ElastiFlow Inc)** 24:05 Yeah.
Right now, I'm not convinced that we do.
But one of the things that gives me pause is that it's stable.
And… the attributes considered stable, and I don't… maybe it's my uncertainty around what it would look like to To deprecate something that has been deemstable.
**Trask Stalnaker (Microsoft Corporation)** 24:32 Well, I mean, would you, like… can you… do you need that, I guess, is the question for the network, like, if source and destination… if the existing source and destination attributes work for you.
Then that sort of sidesteps the question, and maybe we just need Better guidance around when… to use these…
**Sven Cowart (ElastiFlow Inc)** 25:02 Yeah, I think that.
**Trask Stalnaker (Microsoft Corporation)** 25:03 Versus…
**Sven Cowart (ElastiFlow Inc)** 25:04 one.
is better guidance, and then we can go… because I can see the situation where If you have something that's being instrumented about Well, no, because if it's a server, then you'd use server, right? And you wouldn't… She's used server.address instead of even network local. Like, I'm trying to come up with reasons why I would need this, where I wouldn't know either the direction or the server.
Or, sorry, if it's… where I wouldn't know if it's a client or a server, or where I wouldn't know the direction.
**Trask Stalnaker (Microsoft Corporation)** 25:40 Yeah, so, for example, with, like, network, local, That's, like, say you're at a server, an HTTP server, that's gonna be, like, whatever you bind to locally.
Do you want that to be… the destination… Like, it's not… it's not gonna match up to the destination that the client sees.
**Sven Cowart (ElastiFlow Inc)** 26:11 Yeah.
What I'm thinking about there, though, is if you're a server and you're an HTTP server, I would use server.address.
**Trask Stalnaker (Microsoft Corporation)** 26:20 Right, right.
I'm thinking, it might help to look… check the Java instrumentations.
**Sven Cowart (ElastiFlow Inc)** 26:26 Okay.
**Trask Stalnaker (Microsoft Corporation)** 26:27 for where we use these. Yep. Because we do use… we use client-server, and those are the default ones that we capture.
But in some cases, we also… capture, like, for HTTP clients.
I think in some cases, we capture the actual, like.
network address that it connects to, versus the logical, say, DNS name.
**Sven Cowart (ElastiFlow Inc)** 26:55 Inc.
**Trask Stalnaker (Microsoft Corporation)** 26:55 Which would be in server address.
**Sven Cowart (ElastiFlow Inc)** 26:58 Got it.
Okay, yeah, I'll do some more digging, and then I'll come.
**Trask Stalnaker (Microsoft Corporation)** 27:04 Yeah, and it's still not clear to me that It's needed versus source… network source, network destination, but yeah, if you can do some research for us.
**Sven Cowart (ElastiFlow Inc)** 27:17 Okay.
**Joao G. (Dynatrace)** 27:17 Yeah, Trust, wasn't that also what we discussed, I think, when the elastic donation stuff came in?
There was this discussion about, also, like.
when a specific case here in the issue, when there's this ambiguity, then the… particularly the source and destination thing is better aligned. I'm pretty sure there was… there was an issue of PR or something about this. I tried to find while you guys were talking, but I couldn't find anything.
**Trask Stalnaker (Microsoft Corporation)** 27:48 Yeah.
**Joao G. (Dynatrace)** 27:50 I'm pretty sure I remember that it was this exactly case, like, that there's this issue when Looking in this side that you don't know which… Which one it belongs to, and then when you map that to server… to source and destination, then it's pretty easy.
Because in the, in the example here, right, it says, like, for that flow.
Packet… packet capture and similar telemetry observer may not… may be neither.
But in this case, the observer, then, is the source, probably.
**Trask Stalnaker (Microsoft Corporation)** 28:19 Yeah, so… Joao G. (Dynatrace) 28:20 Probably.
**Trask Stalnaker (Microsoft Corporation)** 28:20 I mean, I would argue that in this case, probably… Joao G. (Dynatrace) 28:25 That's…
**Trask Stalnaker (Microsoft Corporation)** 28:25 use the existing… we do have existing top-level source and destination namespaces.
The question that I don't really know is, like, at the net, like.
That's supposed to be a logical layer, which can also be physical layer if you don't have the logical layer.
If there's no difference.
What I don't remember is why we kept network local and network peer, I mean, as opposed to, say, network source and network destination.
**Joao G. (Dynatrace)** 29:01 Yeah, that's something I couldn't find as well, yeah.
**Trask Stalnaker (Microsoft Corporation)** 29:04 Yeah, it's probably worth doing some archaeology, because it was, as y'all mentioned, it was around when we brought in the elastic comment schema.
**Sven Cowart (ElastiFlow Inc)** 29:16 Okay.
**Trask Stalnaker (Microsoft Corporation)** 29:17 And kind of normalized, took some sort of best practices from that. That's when we introduced that client-server namespace and the source and destination namespace.
**Joao G. (Dynatrace)** 29:30 I was able to find this, but I didn't… I didn't have time to read, but I just found it now.
This, this one here.
It's about, like, moving stuff around, but then… That was a… comment and say, network DeLocal address of this now. So maybe that is a point where we can start digging.
I thought, that seems related.
**Sven Cowart (ElastiFlow Inc)** 30:00 I have that open, thank you. I'll do some archaeology.
**Joao G. (Dynatrace)** 30:03 I don't remember.
**Trask Stalnaker (Microsoft Corporation)** 30:04 Yeah.
**Sven Cowart (ElastiFlow Inc)** 30:05 I think it's important that I… that's, Ross, where you ended up within your suggestion, is where I was… Going to go after this was to actually look at the implementations across the ecosystem, see how it's used, and then just understand, is it actually necessary still? And I hope that would uncover why it's still necessary or not necessary.
**Trask Stalnaker (Microsoft Corporation)** 30:26 Yeah, Chuck… I mean, I… the… I mean, I checked the… definitely check the Java one, because, at least I can vouch that it's… whatever we did there was fairly intentional, and, at least in my brain.
**Sven Cowart (ElastiFlow Inc)** 30:42 Sounds good, thank you.
**Trask Stalnaker (Microsoft Corporation)** 30:44 At that time.
Cool, anybody have anything else they want to chat about today?
Can't tear you.
**Liudmila Molkova** 31:07 Can you hear me now?
Yep.
Yeah, sorry, I just joined. I've seen you discuss Conformance Repo. That's awesome. I wanted to chat what… about the scenarios we'll keep there, and, like, how we distribute scenarios.
Across different places.
And I was thinking… Maybe this, that… Like, let's pick GenAI.
We have Python repo, and it runs… conformance as a part of HCI. It's a strict checks, they don't need to report to the central repo.
We have… Reference scenarios in GenAI Semantic Conventions.
Again, they don't need to be anywhere in the… Conformance repo.
So it sounds like what we will have in Conformance is a unique set of scenarios that… Individual repos can copy, paste, and modify, probably tighten up or customize in some way.
And we will have them for open telemetry instrumentations.
And if somebody… and native ones, maybe. And if somebody wants to contribute theirs, like Open Inference, or, I don't know, somebody who has an instrumentation.
wants to contribute. We will happily take it, but we're not sure if we want to put them there ourselves, because it's a little bit aggressive, saying, okay, we're going to measure your conformance, and maybe we can make it part of the, process of getting into Auto Registry.
But I'm, I'm interested what you folks think about, this.
**Trask Stalnaker (Microsoft Corporation)** 33:14 So, the, I'm not sure if you were asking this question about which, I would want the same scenarios sort of applied across, like, right now, the scenarios in the prototype were very limited, like, just, like, super happy path, Whatever, and I could see that list of scenarios growing in the conformance repo.
But as it grows, I would want them applied evenly across all the instrumentations.
In that conformance repo?
But let's take that separate from the… third-party instrumentation.
question.
**Liudmila Molkova** 34:01 Okay.
So… Let's take Java.
We would… have conformance tests against Java HTTP instrumentations.
There.
Would you also… Run conformance suit against PRs in Java.
**Trask Stalnaker (Microsoft Corporation)** 34:31 Probably not for… not anytime soon.
Because we have a way, way, way more comprehensive Testing… over there.
I guess it's not tied to Weaver, which is the only… Sort of, but we would probably see… If there's errors in the conformance repo.
With our conformance, and take those back, and add them to our… integration tests…
**Liudmila Molkova** 35:04 Makes sense.
And then it will be against the released versions of… Java urgent.
Or instrumentation libraries, whatever.
**Trask Stalnaker (Microsoft Corporation)** 35:14 In the near term.
**Liudmila Molkova** 35:16 Okay.
And…
**Trask Stalnaker (Microsoft Corporation)** 35:19 Where I was getting at is, like.
as I could see, you know, taking some of the scenarios that we run in Java and saying, oh, these are, like, say, HTTP cap… header capture using the config… the standard configuration mechanism. Like, that would be a great test to add to conformance.
And apply across all the instrumentation so that users can see, oh, these ones do support the standard configuration.
Mechanism, and do capture those.
**Liudmila Molkova** 35:57 I see. So then for each domain, we kinda wanna have a set of golden scenarios that every library should implement.
**Trask Stalnaker (Microsoft Corporation)** 36:05 Yeah.
**Liudmila Molkova** 36:08 Cool.
I'm thinking what would be the next…
**Trask Stalnaker (Microsoft Corporation)** 36:14 If they don't… if they don't, that's okay, too. It just… it just flags that in the report as not implemented.
**Liudmila Molkova** 36:24 Okay.
So, then, I'll make a stab on… GenAI, Cape HTTP… Out for now.
**Trask Stalnaker (Microsoft Corporation)** 36:38 Yeah, I'm gonna start layering… sending… layering HTTP stuff in.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 36:46 I don't know if this… it makes… if it… if we need to worry about this, yet. But one of the things in the Java project where I've been doing the similar things is one thing that I came across is, like, The difference is based on configurations or runtimes, And things like that, like, do we need to… Are we just thinking, like, our conformance will be, like, the default behavior of these instrumentations, or do we want to take into consideration, like, if you're using this, but you configured it this way, you know, now… now the conformance changes, or… or do we just want to stick to to just the defaults. And then the other thought layering on top of that is, like, as projects are, going to adopt this, like, in Java.
we have, like, the HTTP stuff, but for database and messaging now, it's kind of in flux. So, do we… do we just have a mechanism for us to continue using it, while we work towards conformance, even if it's under, like, a gate or a flag or something like that? Just some thoughts as we start to think about how the mechanics of the scenarios work.
**Trask Stalnaker (Microsoft Corporation)** 37:57 Yeah, so the first, part was about, config flags, and, I would like to test config flags, but only the spec ones. So not the, you know, 500 different config flags that we have in Java, but just the ones that are, like… so the HTTP header one is a good example. There's a standard declarative config setting for capturing those.
I would like to have a scenario there that uses that and validates that.
For… Database… so, for things in flux, you… I think you can see already, but I think it's okay for… in the way that, so Liudmila has designed where you can, in the conformance test, you can give it environment variables specific to that conformance test.
So, for Semantic Convention opt-in stuff.
I think it's totally valid to put that flag into the conformance YAML.
And have it run under that flag, and spit out the result. And in the report, we would just show that, you know, it wasn't a default setting, you did need to apply this environment variable, or something like that.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 39:39 Yeah, so basically, like, the when condition.
**Trask Stalnaker (Microsoft Corporation)** 39:43 Right.
**Liudmila Molkova** 39:46 We'll probably add declarative config support.
To the runner.
**Trask Stalnaker (Microsoft Corporation)** 39:51 Yeah, yeah.
That would be awesome.
Yeah, let me look through the config. I just re-subscribed to the configuration repo notifications.
I had unsubscribed a while ago, because I was just overwhelmed, but yeah, I want to start paying attention to the configuration again, because it's such a critical part of The story, the whole story.
**Liudmila Molkova** 40:35 Yeah, at some point, we will probably… have… List some of the configurations mentioned in YAML.
And then we would also have access to it, and then we would… automate it even more, but nothing should stop us from doing this already. Like… The testing, not the automation.
That we have a…
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 41:03 I was just gonna say, one other thought I had, too, is not related to what we just said, but in terms of the, like, the report and the display of this, I think, like, the Explorer will work really well in the sense of… Like, right now, we have a model of basically scraping the information from OpenTelemetry sources, so even if we have some of these tests run in the primary repo, but we also run them alongside like, the Java instrumentation repo or whatever, like, that should integrate, still very smoothly with the Explorer. And as soon as we start to have you know, something that we want to display, like Trask already had, like, a pretty good prototype, like, we could even just start with what he had there. We could get that wired up pretty quickly.
Onto the Explorer, too, so… I'll be… I'll keep an eye on that so we can get that pipeline going once we're ready.
**Trask Stalnaker (Microsoft Corporation)** 41:55 Cool, I, yeah, I'm gonna, In the background, start, having, pushing some HTTP, stuff to the conformance repo for different, instrumentations and different languages, so that would be a great.
It would be really cool to have the Explorer show more than just Java and the collector.
**Jay DeLuca (Raintank, Inc. – Grafana Labs)** 42:20 Yeah, definitely. Cool.
**Liudmila Molkova** 42:27 Well, the moment I ran it against one of the HTTP instrumentations, it showed something.
**Trask Stalnaker (Microsoft Corporation)** 42:36 Alright.
Cool! Anything anyone else wanted to raise today?
**Liudmila Molkova** 42:52 Sorry, I'm not going to let you go easily. Can you please open the V2 migration issue? It's 38… 08.
I'm going to be… So, there are a bunch of…
**Trask Stalnaker (Microsoft Corporation)** 43:11 issue.
**Liudmila Molkova** 43:13 Ish.
**Trask Stalnaker (Microsoft Corporation)** 43:13 issue.
**Liudmila Molkova** 43:20 Yep, this one.
So, we have a bunch of attribute groups that appear in the public docs in the… that we render as a group, and I'm suggesting to… to drop a bunch of them.
I want to check what people think.
So, we have this… It's in the attributes general. We have the network core, network connection and carrier.
Oh, sorry, I didn't prepare links.
**Michele Mancioppi (Dash0 Inc.)** 43:53 Ideally, then, before V2 drops, we need to fix the service.peer.
Again?
**Liudmila Molkova** 44:02 Oh, we won't drop this one. I, I think this one is important.
There are just a few that I want to drop.
**Michele Mancioppi (Dash0 Inc.)** 44:11 But we have, I understand there is consensus.
That it is not the right namespace, and should be instead something like client.service.something.
We spoke about it earlier in this call.
**Liudmila Molkova** 44:25 Oh, okay, yeah, sorry.
**Trask Stalnaker (Microsoft Corporation)** 44:28 But I think that's independent, like, you're… you're not… This is… has nothing to do… this is just rearranging things.
Is my understanding, Liudmila, versus actually dropping… Any Semantic Conventions?
**Liudmila Molkova** 44:44 Yeah, not dropping semantic conventions, but dropping, the rendering of some of them in this file. So, like, if you search for network connection… And carrier attributes. This friend.
We have attribute registry now, I don't think anybody uses it as a group.
And I'd rather just drop it, and it will still appear in the registry.
This one, no suggestions, we'll keep it.
Yeah.
Oh, but there are nice pictures here. We'll need to find a better place, better home for them. Unless… Oh, they are in the section I don't want to drop, I think.
**Trask Stalnaker (Microsoft Corporation)** 45:46 Yeah, it would be nice to, even if we just drop some of the things that aren't needed here as kind of a… A little unwieldy.
mix of… it's also a kind of unwieldy mix of, These and the footnotes, like, it's kind of hard to… Underst… to read, like, okay, what is this… heading now, I've kind of gotten lost in what section I'm in.
**Liudmila Molkova** 46:14 Yeah, maybe we should have a page about network.
As a separate thing, how to approach it.
**Trask Stalnaker (Microsoft Corporation)** 46:21 Yeah, or just removing, like, the group, like you said, the groups, like, if we could just take these tables and all their footnotes out of this page, and then link over to it if we want.
**Liudmila Molkova** 46:36 right.
**Trask Stalnaker (Microsoft Corporation)** 46:46 Yeah. Yeah, that would be nice to not have… these app… I mean, it doesn't really seem to be… Helping to have these attribute tables in here so much.
**Liudmila Molkova** 46:59 Yeah, I'm not… like, my immediate goal is to transition to V2, and the blocker is that we have them as groups. I don't want them to be public.
Meaning they cannot be rendered.
And it's a good exercise to see what is actually a reusable group versus a bag of attributes that we only created because we didn't have attribute registry.
So… I like the idea of refactoring this dog, though. I'll probably make a stab, and I'll try to be mindful of the useful information we have there. Maybe some of them will end up in a separate Page. Can you return to initiate for a sec?
Yeah, this front.
So this is related to the network. If you scroll down, there are a bunch of other things. I didn't see… I didn't look into the logs. We'll probably figure out what to do as logs, don't have an, don't have a proposal yet.
I kind of want to deprecate open tracing group and stop rendering it altogether, because it's deprecated and it's… Still in the attributes registry, if anybody needs it.
**Trask Stalnaker (Microsoft Corporation)** 48:21 Makes sense.
**Liudmila Molkova** 48:23 Yeah, and Joao has left, so I think I will talk about cloud events sometime, some other time.
Yeah.
Okay, Dan, I'll prepare something for the network, and we'll… we'll talk.
More specifically about it.
**Trask Stalnaker (Microsoft Corporation)** 48:52 Sounds good.
**Liudmila Molkova** 48:57 Awesome, thank you.
**Trask Stalnaker (Microsoft Corporation)** 48:58 Last chance.
Alright, let's get 10… 11 minutes back.
Have a good one.
**Liudmila Molkova** 49:09 You do.
**Armin Ruech (Dynatrace LLC)** 49:10 Bye-bye.
