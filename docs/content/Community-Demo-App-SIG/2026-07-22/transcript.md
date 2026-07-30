SIG: Community Demo App SIG
Date: 2026-07-22
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 01:10 Hey, everybody.
**Felix Felix (IBM India Pvt Ltd)** 01:15 Hi, everybody.
**Juliano Costa | Datadog** 01:18 Hello, beautiful people!
**Donal O'Sullivan** 01:21 Hello.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 01:22 Thanks again.
**Juliano Costa | Datadog** 01:23 This… this laugh was like, who is beautiful?
How is everybody?
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 01:34 Good.
How are you?
**Juliano Costa | Datadog** 01:37 Man, this 3.0, release is, like, Killing me.
Life.
Literally.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 01:48 So what is, what's pending, I guess?
**Juliano Costa | Datadog** 01:52 So I was working today on the… on the health chart, and then I start playing, I was checking the environment variables for the services.
after, of course, Claude created the whole thing to me, so I was manually reviewing and going through. And then I found some stuff on the… on the Agentic services, that was mapping environment variables in a way that we do not do for the other services, so I started playing around and testing it, and then I raised that to Felix, that whenever I enabled the MCP, the chatbot crashes, so I'm not sure if it's, just happened to me, or,
**Felix Felix (IBM India Pvt Ltd)** 02:42 No, no, I was able to recreate it. So it was because, since, MCP… so there was a bump-up in the MCP version recently.
that format with MCP since the response has changed a little bit. So, whatever there is in our cache is slightly different.
So, I can fix it with… by updating the cache, but I don't think that's the correct approach, so I thought I would write a fussy matcher to match a request with an existing request in the cache. If they're very similar. We can keep the threshold very high, like, similar… something similar to 85, Out of 100, if the policy manager identifies a very similar request, we can send the response back of that existing cache. So, it… the MCP, while sending the tool response, it adds some prefixes, which is causing the issue. But right now, the VCR checking for an exact match of request and sending the response, cache response.
But we can make a fussy matching.
there.
Oh, so I, I, I… started with a rudimentary version, and it's working for the MCP?
So, yeah, so I was able to identify the issue, and we can mitigate it with a fussy matcher, rather than updating the cache.
**Donal O'Sullivan** 04:01 So what exactly happened? Did our version get bumped, and the response from a HP… from some… Requests over the net has changed.
Pizza?
**Felix Felix (IBM India Pvt Ltd)** 04:10 because of the MTP version change, the initial cache that I have added, right.
**Donal O'Sullivan** 04:15 Yeah, yeah, yeah, no, I understand. So, yeah, my concern would be… this… so it's brittle, right? So… so changing the version… so doing a version bump has broken something, and it… it's brittle, essentially, the API response has changed, has broken something.
So maybe we just need to be a bit careful how… how the implementation is done, can it be done in a way that's not brittle? Like, fuzzy… fuzzy finding can be… is fine, maybe, but again, it's a bit… like, it's… adding a kind of a layer of brittleness to it, maybe. I don't know, is there a… Is there a… is there a better way to do this, maybe?
**Felix Felix (IBM India Pvt Ltd)** 04:57 So, I think the ideal approach will be to understand the semantics… semantic of the question, and respond if anything semantically matches exists.
But, to check this, semantic similarity, we will need some embedding model as well, right?
I'm not sure how good the existing, similar, you know, open source similarity measures, like, you know.
Sequence to vector, or those kind of things work.
To capture the similarity, you know, contextual similarity, we're not sure.
That will need some experimentation.
But I… No, I…
**Juliano Costa | Datadog** 05:40 Go ahead, go ahead, sorry.
**Felix Felix (IBM India Pvt Ltd)** 05:41 No, so I was… I was… a little while ago, I was playing with this fussy matcher, and if we adjust the threshold a little bit, I think… not sure, I was just playing with it, so… So, yeah.
very primitive version of Aussie Manager. I was able to, you know.
Fix this issue without any change to the existing cache.
I can create an issue and send, you know.
create a PR, you guys can comment on that, that's better.
**Donal O'Sullivan** 06:11 Yeah, okay.
**Juliano Costa | Datadog** 06:12 One thing that… I'm a little bit afraid is that we have Dependabot, taking care of dependencies all the time.
So, if there are… significant changes between versions, then this is a service that will be Breaking more and more.
I don't know what we could do, but yeah.
But let's see, let's see your, proposal, Felix. I… -Oh.
I don't want to rush you, but do you have any, estimated on when you will… Work on that?
**Felix Felix (IBM India Pvt Ltd)** 06:58 I'll try to create it within this week.
Or in two days, I mean…
**Juliano Costa | Datadog** 07:04 Okay, cool, cool.
Yeah, I think I tagged everyone on the… OpenTelemetry.io blog post, everyone that is here, at least.
if you could take a look over there as well. And I also replied on… on your PR Felix on the… On the services.
Yeah, on the… on the hotel.io, on the service documentation. I saw that you are… kind of replicating what we have on the README with, details.
I think on the OpenTelemetry.io, we could keep it simple, saying, like, chatbot is a chat interface to talk with the agent, and here is how we do the instrumentation. For traces, we use a trace loop. Here we start, here we end, whatever. If there are metrics, you say, if not, keep it empty, and logs the same. If you take a look at the other services, that's what we do.
We do not talk about how the service works and all the other things, we just talk about the instrumentation part of it on the Hotel de Rio.
**Felix Felix (IBM India Pvt Ltd)** 08:18 Okay, I don't accept it.
**Juliano Costa | Datadog** 08:20 Cool.
Does anyone have any other topics? I have one thing that I want to discuss, but Okay, I was also playing around with, so, the, the health chart.
And, Currently, on the Helm chart that we have on the demo, we use a bunch of sub-charts. So we have, a couple of them, and one of them is the collector. So to deploy the The Demo Helm chart, we use the collector Helm chart.
Which is… great.
But we do not have, EVPF profiling HumpChart. So then, for this one, we need to deploy, through, Deploy the collector and configure everything.
as it is a BPF, and it requires a couple of extra permissions, Do you guys have any opinions on… Should we deploy as default or not?
I was thinking about making the default disabled.
So then, just if someone wants to deploy and see the eBPF provider, they would need to enable and add all the, permissions that eBPF requires, but I want to hear the group opinion.
**Shenoy Pratik** 09:54 We're blue.
default disabled, because it's easy to deploy, the people who are using LMCharts as is today can still continue to use it. If they start using something with privileged access, it might surely have a cutoff point, and, like, this is not coming up right now.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 10:13 Yeah, I mean… I've always recommended using eBPF where hotel instrumentation is not present, which isn't the case, right? This app is specifically meant to instrument hotel, so… I think we'd probably get a lot of duplicate traces and information with eBPF on, I think… no?
**Donal O'Sullivan** 10:32 No, this…
**Juliano Costa | Datadog** 10:32 Because the…
**Donal O'Sullivan** 10:34 Yeah, go ahead, go ahead, Juliano, go ahead.
**Juliano Costa | Datadog** 10:37 No, no, no, good. You are the PR alter.
**Donal O'Sullivan** 10:40 So I guess what you're talking about, Juliano, is probably adding profiling, is it, for Kubernetes?
**Juliano Costa | Datadog** 10:47 Yeah, yeah, yeah, the APPL profile. Oh, apologies.
**Donal O'Sullivan** 10:49 Yeah. Got it.
Yeah, so it's a separate collector that runs with higher privileges, because it hooks into the eBPF in the kernel, and it needs re-permissions to access probes, so every time you do, like, system calls, it's just gonna log that, and Yeah.
I would agree with Shenoy here. It probably needs to be maybe something you enable, if… would be my opinion as well.
just keep it separate, you know? I think, like, the permissions are fine, they're just read permissions. I don't think they can't do anything malicious, really, but when people hear about, like, higher privileges and eBPF, I think he probably got a bit kind of freaked out.
**Juliano Costa | Datadog** 11:37 I have never deployed a BPF on a cloud provider, so does anyone have an experience there with AKS or AKS, whatever?
If… If it is, like, a problem?
**Donal O'Sullivan** 11:53 I haven't done it either, so…
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 11:56 I've run, like, Bela for eBPF for Traces and EKS.
**Juliano Costa | Datadog** 12:02 And it works fine.
Bye.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 12:05 Yeah, I mean, it's… I always think of it like kind of a best guess, right? So, like, it's not as good as implementing traces in OpenTelemetry directly in an application, because it's.
**Juliano Costa | Datadog** 12:14 food.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 12:14 internal.
But it worked, yeah, it got… it got traces. Whether, like, how…
**Juliano Costa | Datadog** 12:20 Yeah.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 12:21 Yeah, but it's more of a binary here, right? Whether or not it works at all, yeah.
**Juliano Costa | Datadog** 12:26 Yeah, yeah. My main concern is not about the data that we are collecting. My main concern is people not being able to deploy the demo, because it requires some… like, I know that there are some restrictions, for instance, on OpenShift, and we have a couple of issues open, because some services require, read access, or whatever, like.
there are some issues that I just breed and never… Reply, sorry, whoever is listening to this and on the recording.
But… Yeah, there are some security things that are in place for some Kubernetes distributions that may crash the demo, and I.
**Donal O'Sullivan** 13:14 Yeah, yeah.
**Juliano Costa | Datadog** 13:15 Yeah, I would like to avoid that.
**Donal O'Sullivan** 13:17 Yeah.
**Shenoy Pratik** 13:19 I bet.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 13:19 Test an EKS, if that's helpful.
**Shenoy Pratik** 13:25 Yeah, that would be great, yeah. I tried EKS, like, a long time right for EBBF, and also with other things like Inspector Gadget, I don't know, like, 2 years ago. Things worked. It's not that it doesn't work. There are some nits here and there on how to set it up as sidecar, or… Gateway, but it does work.
So, that's the question, but I don't know, like, we need to check our HIM charts and see what's the configuration that we are putting it in.
**Juliano Costa | Datadog** 13:50 Okay, yeah, I'll… I'll continue playing around. I… I stopped in the middle of the thing because I found the issue with the Agentic flow.
But, florian… from Elastic shared with me that there is already a preset on the… on the… old tower operator, so maybe I can copy over some stuff from there. Because currently, we do not use the operator on the demo, we use, just the Helm charts, so… Dove.
the preset wouldn't work for us, but, I mean, the preset exists, so I can copy the code over, so, you know.
**Shenoy Pratik** 14:38 Yep.
**Juliano Costa | Datadog** 14:43 Cool.
Hey, Charles, welcome.
**Charles** 14:51 Hello.
**Juliano Costa | Datadog** 14:52 Hello.
Just, out of curiosity, are you joining just to hear us talking, or do you have any… anything in mind?
**Charles** 15:04 Nothing in mind, I'm a totally newbie. I just want to see where the strategy or directions were going with the demo apps.
**Juliano Costa | Datadog** 15:16 Cool.
Whoa.
So, yeah, we are in the middle of a release cycle. We were discussing a couple of pending things, but we're gonna release the 3.0 soon, which will be a major release, and… Breaking a bunch of stuff.
Okay. But I… I think everyone that is already using Maine is already, complaining to, like, about the demo, because, yeah, the docs are not aligned to whatever we have on main.
So,
**Charles** 15:52 The, timeline estimates, when it's expected?
**Juliano Costa | Datadog** 15:56 Yeah, 2 weeks ago.
Okay.
**Charles** 15:59 Okay, imminent, imminent, I guess.
Cool, cool.
**Juliano Costa | Datadog** 16:04 Yeah, two weeks in the past. Yeah, I… I… I really want to get that done by the end of this week. I have, we have already a blog post, scheduled, or… I don't… I didn't hear back from the, from the OpenTelements.io teams… yet.
But, we have a blog post ready to go, and, I'm working… I'm currently working on the Helm chart PR that will bump everything.
Once I have the Helm chart PR, then I'll just click on the release 3.0. But I want the Helm chart to be ready, at least in a draft mode, ready to go, so then whoever sees the 3.0 release can already deploy using Helm.
**Charles** 16:56 Perfect. Look forward to it!
**Juliano Costa | Datadog** 16:59 Me too. I think I'll take a week off of PTO, just to rest.
**Charles** 17:07 I can imagine.
**Juliano Costa | Datadog** 17:10 -Oh.
Do we have any… anything else pending?
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 17:22 That's what I was gonna ask, like, is there anything any of us can do to help with the release, aside from the Agentic stuff that, I believe Felix is working on.
**Juliano Costa | Datadog** 17:40 I think what we can maybe do is, start documentation.
So, everything that we have on the docs are deprecated now.
So, we need the new make comments added.
we need to document the new… well, the new services are ongoing. Felix has this, and you also have a PR for the CC exchange.
We need to update the architecture, diagram, To reflect the changes.
What else?
So, I would say mainly docs.
There were a couple of dashboards added to the demo that we do not mention on the docs as well. So, there are a couple of doc pages that we can remove, replace, improve.
So, yeah.
I would say that any help on there would be appreciated, because whenever 3.0 land, people will want to use, and they will take a look at the docs, and the docs won't say what How to actually deploy, so…
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 18:59 So the open… you're talking about the OpenTelemetry.io docs, but also.
**Juliano Costa | Datadog** 19:03 Yeah, yeah.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 19:03 Me in the repo itself, right?
**Juliano Costa | Datadog** 19:06 The, the… we do not have instructions on the README.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 19:11 Oh, yeah.
**Juliano Costa | Datadog** 19:13 We do have… we do have instructions for development on the… on the README for the services. I think those are fine.
It's, just the OpenTelemp.io docs.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 19:29 Here, I could have a look at that.
**Juliano Costa | Datadog** 19:33 Cool.
Cool, cool.
And I'll try to, I'll try to raise the help chart PRF, so then we can, we can get, everyone… everyone's eyes on it.
Because it's… It's huge.
**Shenoy Pratik** 19:52 It's basically rewriting most of it.
It's not the guy.
**Juliano Costa | Datadog** 19:55 What?
**Shenoy Pratik** 19:56 changes. It will be like rewriting the HilmThreads again, altogether.
New environment variables, new services coming in.
**Juliano Costa | Datadog** 20:05 Kind of. I mean, the services are… the way that Tyler and Pierre developed at the… initially, it's pretty configurable, so I'm just adding some cool things there, like, just a couple of minor stuff.
But, like, I think… We have an example on bring your own, bring your own backend, something like that, where we explain how to… replace the collector and send… or expand the collector to send data somewhere where we all are interested on that, right? And, that changed, because the collector changed, the components got renamed, so yeah, that's gonna be fun.
And… Then we have the whole profiling case that I have no experience with, so yay, that's gonna be exciting.
**Shenoy Pratik** 21:11 If you have a PR, I can probably test out things early next week, like Monday or something.
**Juliano Costa | Datadog** 21:18 Cool.
**Shenoy Pratik** 21:18 for profile, and also deploy it probably on ETS, just to do a quick sanity check, everything works into it.
I was also looking at docs and seeing, do we want to mention about the new… composable Docker Compose here, because we currently have just minimal and the full demo in the Docker deployment.
We need to see how to update it in the docs as well. Matt, if you're looking into it, probably, we'll need your help here.
As well.
Apart from the architecture changes.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 21:55 Yeah.
I'll look through all the docs and see where we can… What changes do you have to make, including that?
I mean, I'll try to go down the list, I guess there are a lot here.
**Shenoy Pratik** 22:07 Probably just start with an issue, put, like, pull in everything that we think needs to be changed, and then start creating PR so that we don't miss anything or do an overlap of things.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 22:18 Okay.
**Juliano Costa | Datadog** 22:18 That would also be a super help, like, creating issues.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 22:23 Oh, yeah.
**Juliano Costa | Datadog** 22:23 extract this stuff, because, yeah, I'm horrible on that.
I'm not a… I'm not a PO.
Spencer will take care of them.
That's what POs do, right? Create tickets.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 22:43 What's that?
**Juliano Costa | Datadog** 22:46 what POs tend to… Oh.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 22:48 Product, product owner.
**Shenoy Pratik** 22:48 Product owner, product manager.
**Juliano Costa | Datadog** 22:50 Donner, yeah, yeah.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 22:51 Yeah.
**Shenoy Pratik** 22:51 Running the show, giving things to SDs, SDNs.
**Juliano Costa | Datadog** 23:02 Cool, cool. Okay.
Anything else?
Nope.
Perfect.
Then, let's… That's rough, but… Now, so we have 7 minutes more. Well, near a hour left.
**Shenoy Pratik** 23:32 Can I add one point? This one point.
**Juliano Costa | Datadog** 23:34 Sorry.
Yeah. Okay.
**Shenoy Pratik** 23:37 the one from SIGO about the self-telemetry collector thing, I think we discussed at the last meeting. I mentioned that it's fine to probably have the supervisor manage the current total collector itself, you don't need the second one.
Only thing is, it shouldn't be, causing outage if op-amp server is down.
Collectors should just still come up.
I don't know how.
**Juliano Costa | Datadog** 24:01 But it's…
**Shenoy Pratik** 24:01 to win.
**Juliano Costa | Datadog** 24:02 It's a demo, right?
**Shenoy Pratik** 24:03 Yes.
**Juliano Costa | Datadog** 24:05 Like, we try to show things that it's possible, but, yeah,
**Shenoy Pratik** 24:11 We have a lot of things in Alpha.
The collector comment Like, 50% alpha, even today, so… Should we still find IFA?
**Juliano Costa | Datadog** 24:20 And we do some stuff that are not, like, recommended for production use. For instance, auto-instrumentation and manual instrumenting everything, like… Yeah, we have… I think on, quote, the services, like, one… one file, and it has auto-instrumentation and manual instrumentation on it, with traces, metrics and logs. That's the most over-instrumenting case that I have. So, like.
Oh, we did not… show how to run hotel in production. We show what hotel can give people, so, yeah. If the collector needs to restart and drop telemetry for a minute. I'm fine with it.
Maybe we just give a call-out on that and say, hey, yeah, this will cause that, but yeah.
But it… For me, it's way better than… Way better than having an extra collector deployed.
**Shenoy Pratik** 25:30 Yeah, yeah, yeah.
**Juliano Costa | Datadog** 25:35 Cool.
Awesome. Okay.
Then, see everyone next week, hopefully with a 3.0 release out.
Fingers crossed.
**Shenoy Pratik** 25:52 West Coast, yeah.
**Donal O'Sullivan** 25:54 What
**Juliano Costa | Datadog** 25:56 Cheers.
**Matthew Wimpelberg (Raintank, Inc. – Grafana Labs)** 25:57 Thanks.
**Donal O'Sullivan** 25:58 See you later.
**Shenoy Pratik** 25:59 Thanks, Evan.
