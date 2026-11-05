SIG: OpenTelemetry on Mainframes Weekly Sync
Date: 2026-11-04
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Rüdiger Schulze (International Business Machines Corporation)** 01:56 Hey, Santiago.
**Santiago Ortega** 02:07 Hey, how are you?
**Rüdiger Schulze (International Business Machines Corporation)** 02:09 Good.
I was hoping… I'm sitting in a car… I was hoping the light would switch on, but it doesn't.
That's a funny moment.
Should be seeing more.
**Santiago Ortega** 02:23 Yeah, it was, I was on with Matt Lars, Matt Hogstrom.
Last week, but nobody showed up, so…
**Rüdiger Schulze (International Business Machines Corporation)** 02:31 Yeah, there were… we were on a conference last week, and… But this was probably difficult.
Trying to find my car keys, here they are.
Let's put a little bit of light on.
I mean, this is better. It's not much better, but it's a bit better.
**Santiago Ortega** 03:01 Why are you in your car?
**Rüdiger Schulze (International Business Machines Corporation)** 03:03 My… my daughter, she… she has a sports club, or, yeah, she plays hockey.
And, I have to pick her up afterwards, and… you know, I'm in Europe, and the time is… There's no better way to do this, and we have been moving around this meeting already a few times.
Just tried… decided to handle it this way.
**Santiago Ortega** 03:26 I see.
**Rüdiger Schulze (International Business Machines Corporation)** 03:28 So, when you work with Matt, are you maybe working with VMware, or are you maybe from the VMware organization, or are you from the Mainframe organization?
**Santiago Ortega** 03:38 Main… Mainframe organization, yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 03:40 Okay, okay, good.
Anyway, there might be not too much for today, but maybe, as you have been on last week with Matt, we have this… this gigantic, this huge PR for virtualization and mainframe.
And we will split this up, I will do this by the end of the week.
But I was wondering if, As from your organization, from your company perspective, there is also virtualization VMware, you know, within the house, if there were any feedback or any comments, either from the virtualization perspective or from the mainframe perspective.
**Santiago Ortega** 04:18 So I'm sort of new to the group.
I, I quickly brief, skim over the PR. What caught my attention was the fact that there were two naming spaces, one for COS and one for Mainframes, and I didn't quite get why was one Favor versus the other.
And I think I did a Google search, and I found that one is referring more to the software side.
Versus the other one being more towards the hardware side.
And I think… I think for your PR, you chose Mainframe, is that correct?
**Rüdiger Schulze (International Business Machines Corporation)** 05:00 That's correct. And the reason for this is, so, the idea is to build this up from the, kind of like, the bottom layer, which would be the infrastructure side.
So, and we started with a mainframe namespace in very early days.
And, that would be… let's say for any telemetry coming from the… available from the HMC API perspective.
And, then, from a COS point of view, for the other namespace, that would be then being really specific to… I was a… COS operating system characteristics.
Or… potentially also subsystems. I think this is something that we still need to go through.
We started at some point also to use TPS, a transaction processing system, for… you know, KICS and IMS, but I suppose we want to revisit this. The idea at that time was to generalize and bring this into the base semantic conventions.
But, for various reasons, this was a… long process, and in the end, the Federated semantic conventions came up as a… As a way of actually handling these type of conventions within… in a… in a domain, in a separate… repo, so… We can revisit this decision, obviously, to, go with TPS.
Or go just as… Let's say…
**Santiago Ortega** 06:59 Yeah, I agree.
**Rüdiger Schulze (International Business Machines Corporation)** 09:22 Apologies, Santiago. I lost my network connectivity for a second.
Yeah, continuing what I was about to say, I like the TPS.
Because we could actually combine the concepts of CICS and IMS under one naming convention and wouldn't have to To define this.
You know, For each of the products.
The idea is always to kind of, like, go with a minimal model, if you can. And if you don't need to… introduce or multiply concepts, then that would be preferred. So that's the idea why we started to talk about TPS.
**Santiago Ortega** 10:06 But… but when… if you select TPS, you still need some sort of a qualifier.
Because KICS can run on the distributed side as well, right?
Should…
**Rüdiger Schulze (International Business Machines Corporation)** 10:19 And that's… that's an interesting consideration. You were right about that, right? Yeah.
But, that actually might be handled with, was rather describing the resource, so… I mean, any telemetry would be associated with a resource?
So, the resource could actually… The information could be inherited from the resource.
We could also have attributes that qualify that on TPS itself, but you are right, it's a good consideration.
**Santiago Ortega** 10:57 That's what I was thinking, is… I think I saw somewhere the concept of TPS, and I was thinking it is… There's a constraint, or there's a… there's a challenge in defining where does it run.
And… And I don't know if, if from the point of view of, of software is important to understand if it's a S390X, Versus, An Intel-based, architecture.
**Rüdiger Schulze (International Business Machines Corporation)** 11:37 Yeah, so… yeah, so usually the… the… The information would be carried with the resource, what kind of hosting architecture that would be.
So, I think we would be able to see this via the… for instance, the span, or eventually also some of the metric definitions could live under TPS, and then you could have this association was… The… the owning, entity, eventually. I'm just updating next to, There are meeting notes, I'm updating the meeting notes while we speak, that we are discussing some of these questions around,
**Santiago Ortega** 12:24 I was showing how this son.
**Rüdiger Schulze (International Business Machines Corporation)** 12:25 Yeah.
**Santiago Ortega** 12:26 Excellent.
**Rüdiger Schulze (International Business Machines Corporation)** 12:27 the, modeling…
**Santiago Ortega** 12:30 We went in to address it.
**Rüdiger Schulze (International Business Machines Corporation)** 12:33 Discuster…
**Santiago Ortega** 12:34 It's API mountain, so I don't think…
**Rüdiger Schulze (International Business Machines Corporation)** 12:37 Mainframe.
COS namespace…
**Santiago Ortega** 12:55 Bye.
**Rüdiger Schulze (International Business Machines Corporation)** 12:58 Yeah, so, moving forward, just to ask this, moving forward, would you, as these more detailed PRs come available.
Would you… would I view them, you know, from the perspective of your company?
And your product portfolio, so that, you know, this… Becomes, in the end, from a… from an ecosystem perspective, a complete definition. I think that's what we essentially want, that we get to a common definition.
**Santiago Ortega** 13:32 Yeah, I probably won't be the only one, but that might… that might help, yes.
**Rüdiger Schulze (International Business Machines Corporation)** 13:37 Okay.
**Santiago Ortega** 13:37 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 13:38 That sounds good.
Good, just to update you on a couple of points that I just wanted to… Call-out, which we discussed also on the… Meeting, before last week.
The, There was, obviously, in the base semantic conventions, some definitions around mainframe and CS, and I think this is what you have been seeing and also referring to.
They will be deprecated from the base definition as the… community is moving to version 2 of the semantic conventions, and we will reintroduce them in our repo. This will be a separate PR.
Plan to open this until Friday.
And, then, this, however, needs to also go in alignment with the other definitions that we want to do. And from… today's perspective, my point of view would be we have mainframe, like we just described it, so infrastructure level, CUS, anything that lives on the operating system.
specific subsystems, I think we need to talk of how generalized we can do that, or… how Windows specifics we want to expect to do that.
that's kind of like this differentiation, what we just discussed. Is this TPS, or would we go for a case of CICS for IBM.CICS as, for instance, a… Qualification.
And, then… Also, let me see what else I wanted to point out. I don't know if Matt spoke with you, there's a project being established by the Open Mainframe project, which is called Opleano.
which will bring, OpenTelemetry Conform APIs to… to the operating system, to COS.
And that's a technical… an initial technical committee kickoff on the 16th of… November, and… the idea here is to… for languages like COBOL, Assembler, and so on.
to provide a way to ingest OpenTelemetry conform.
telemetry to the… To any of the observability backends, obviously, from any of those Addictive.
**Santiago Ortega** 16:20 generate, right? To generate…
**Rüdiger Schulze (International Business Machines Corporation)** 16:22 Alright, right.
**Santiago Ortega** 16:23 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 16:24 Yeah, right.
**Santiago Ortega** 16:26 I see.
**Rüdiger Schulze (International Business Machines Corporation)** 16:27 Yeah, so this is… yeah, go ahead.
**Santiago Ortega** 16:29 So this would be more like what Java can do, and Node.js can do, to instrument the runtime so that it would automatically generate some of these metrics without having to purposely force the application to a meeting? Is that… is that the idea?
**Rüdiger Schulze (International Business Machines Corporation)** 16:51 So, that's the challenge, right? I mean, in products like… or programs like… like Assembler and Kobo, it's very hard to do auto-instrumentation.
So… I think the first approach is to… Half is done through… manual instrumentation, essentially providing some sort of API that you can ingest the data.
If there are other ways, this is probably something to discuss at some point. Are there more automated or no-code ways for those type of languages where… Maybe if there are certain frameworks that, you know, maybe these frameworks could bring these injection points.
And be more… In a more transparent.
Perspective of, you know, the code that somebody would be writing.
But yeah, that's left for future discussion, I think.
**Santiago Ortega** 17:52 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 17:56 Okay, and that would be all for today. This is always a very small SIC, so it's essentially the four main vendors.
I spoke last week to Jim and also to Richard from Rocket and BMC.
I expect them as well to… To join on one of the next meetings again.
**Santiago Ortega** 18:18 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 18:19 What I will do is I will open these PMRs, and then… or… not PMRs, PRs, obviously. And, then I think there will be something next week that can be reviewed, and that is smaller in size, so that we can make progress here.
**Santiago Ortega** 18:35 Sounds good.
**Rüdiger Schulze (International Business Machines Corporation)** 18:36 Okay, Santiago, thanks a lot.
**Santiago Ortega** 18:39 Thank you. Take care.
**Rüdiger Schulze (International Business Machines Corporation)** 18:41 But…
