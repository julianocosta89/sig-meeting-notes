SIG: GenAI SIG (APAC)
Date: 2026-10-13
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Nir Rozenbaum (NVIDIA)** 09:31 Hello, everyone.
**Omer Aplatony** 09:33 Sorry.
**Trask Stalnaker (Microsoft Corporation)** 09:35 Hey.
**Omer Aplatony** 09:36 Hello?
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 09:37 Hello?
**Trask Stalnaker (Microsoft Corporation)** 09:37 com.
We'll give them another minute or so.
And then we'll get started.
**Omer Aplatony** 09:51 Yeah, I mean, Steve Rao (Alibaba Cloud (Singapore) Private LTD) 11:11 Hello?
And Fox.
**Trask Stalnaker (Microsoft Corporation)** 11:14 Hey, Sue.
Let's see, looks like… okay, so this is in the agenda… This… Let's… Move down… And… All right, welcome, Got some new folks here.
Hey!
**Omer Aplatony** 11:48 Hi, hello.
**Trask Stalnaker (Microsoft Corporation)** 11:51 and a topic. Yeah, why don't you kick us off?
**Omer Aplatony** 11:56 Yeah, thank you. So, nice to meet you all. My name is Omer, and I work for NVIDIA, and I'm also Secret Scaling Tech Lead for Kubernetes.
With me is Neil. Neil, would you like to introduce yourself for Santa Soto?
**Nir Rozenbaum (NVIDIA)** 12:12 Yeah, sure. So, I also work for NVIDIA. I am a maintainer of another project in Kubernetes, Gateway API Inference Extension, which handles inference, basically, and also a SIG leader and maintainer in LLMD.
We started to see… Some things around, Model serving metrics and signals.
And we wanted to propose, we proposed a project, a new sub-project.
to Kubernetes, so… Omer, do you want to.
**Omer Aplatony** 12:50 Maybe if you can… yeah, it's final.
**Nir Rozenbaum (NVIDIA)** 12:53 Yeah, if you'd like to.
**Omer Aplatony** 12:54 So.
**Trask Stalnaker (Microsoft Corporation)** 12:55 that's…
**Omer Aplatony** 12:55 Yeah, yeah, yeah, I can, maybe I can share the doc, just a sec.
Maybe it's fine if you… you can… yeah, Trask, you can do it yourself if you can want to share your screen. Sure. And there is a link in the README file, yeah.
**Nir Rozenbaum (NVIDIA)** 13:11 Yeah, exactly.
**Omer Aplatony** 13:17 Yes, exactly this. Yeah, yeah.
So, in general, we discovered that there are a lot of Different solutions to how… Different projects in the ecosystem are doing.
LLM7.
One of the things they're doing differently is how the different inference engines are advertising different metrics with different semantics.
for their use cases. So if you can scroll down a bit.
there is an example of how different LLM serving, such as VLLM, TensorRT, SGLang, and such.
really advertises different… different metrics.
And the metrics means differently per inference engine. For example, you can see that SG Lang.
advertises token usage, and VLM is a KV cash usage purse.
And TensorRT is something different.
So, this means there is a tight coupling between the inference engine and between the semantics of the metrics that this inference engine is published.
So… We want to create… we also… we already created it. A project that Its purpose is to overcome this obstacle.
By having a sidecar next to the old inference engine, and make One language that you can You know, scale and do whatever you want.
Based on a unanimous metrics that this site here will.
So… So we already know that OpenTelemetry is some… Convention for those metrics.
And we want to present here the… this is this part of the solution, but this is the part that is… with OpenTelemetry specifically.
So we wanted to present this topic for you folks to, first of all, review.
Second of all, we would like to have you on board for this.
So if you have any questions… Feel free.
**Nir Rozenbaum (NVIDIA)** 15:28 Maybe, maybe I'll just add two more sentences, so… We are aware of the standardization effort that you are already doing, the examples like GenAI.server.request, and these things.
But having said that, there are, Important signals, let's say those ones that drive the routing decisions, the auto-scaling decisions, these things are not standardized yet.
We have seen multiple issues around it, issues that have been created within OpenTelemetry GenAI SIG, LLMD, Kubernetes, like, all around this space.
And the idea with this new sub-project is that basically, no matter which Kubernetes integration comes and want to integrate with a model server, whether it's a router, observability, autoscaling, whatever it is.
They can work with that.
Contract with that standard.
And they shouldn't care.
which of the model server is underneath. Like, they shouldn't care whether it's VLLM, SGLang, or any other thing, and not only from this table, so we surveyed these three model servers, but you can think also about new… new ones, like.
Token speed, I think that's the name of something new that is, like, trying to do same as VLM and others. So, as long as they publish metrics that are aligned.
with the standard.
Any Kubernetes integration should work out of the box. And the intention?
is to eventually push this standard to the engines. So they will eventually adopt As soon as they see value, so they see that all the Kubernetes integrations, that they work with those metrics.
we are expecting them to pick this up, and we are definitely going to use our contacts within all these three. We have contacts with maintainers in all of those three engines, and we're going to use their help to push this standard. So this is just To summarize.
We want to collaborate together.
And make sure that.
We end up with a single standard that is used.
Both in OpenTelemetry GenAI effort, and also in that new, project.
**Trask Stalnaker (Microsoft Corporation)** 18:04 Cool, yeah, thank you. That answered, one of my questions about, like, yeah, pushing, like, the ultimate goal would be, is generally to push those things upstream, but it makes a lot of sense to have that intermediate step.
Because I… Takes time, and like you said, you have to show value through usage first.
I'm… Cool, is there sort of a… maybe a summary, The metric… Okay, the… this… these are the metrics at this point.
**Nir Rozenbaum (NVIDIA)** 18:50 Yeah, this is just a minimal set of examples. I think I've already seen the queued and running proposed in some threads. I think this is, like.
And a simple example that is kind of straightforward, because all of those engines, they are already exposing the metrics with these semantics. When we talk about KV cache utilization, the main challenge here is that different engines, they have different semantics, and this is the table that we've seen in the upper table, but this is just a minimal The minimal set that we expect that Should be, you know, extended as we move forward, but… It is something to start with.
**Trask Stalnaker (Microsoft Corporation)** 19:36 Cool, yeah, no, it just helps me to kind of wrap my… around. Yeah, so, The majority of the… Semantic Convention GenAI effort, as you've seen, has been around the, kind of, client, semantics.
But definitely there has been interest in server, semantic conventions, and… I think we have… We may have a couple, or at least it's certainly… kind of starting, some of those discussions. This is maybe… I don't think we have anything around models, but basically the way the SIG works is, that if… if we have people who are interested in those topics, if we have a group of people who are interested in those topics, that we can extend in that direction.
Right, we just need, sort of, enough, I.
Domain experts, which you'll… Bring… we need, implementations, prototypes, that sort of thing, like you said, showing value.
And, you know, people who can review these and give feedback on them.
It feels… so there's sort of a… in general, broad open telemetry semantic conventions, there's a couple of approaches, there's… the… you can define semantic conventions outside of our repo, using federated semantic conventions, which is, fairly new, but, is a really, how we're kind of trying to not be the bottleneck of the world.
on… But, that said, these, I mean, GenAI server stuff.
probably would fit into the GenAI Semantic Convention repo.
At least long term.
So, I don't know, I… I… be in favor of, you know, seeing those… bringing those proposals into the repo. Would love to hear Liudmila's thoughts.
**Liudmila Molkova** 22:02 Yeah, I… I have mixed feelings about having them in the repo, mostly because what you mentioned, Trask, it would be a bottleneck.
But there is a lot of interest. I think we have some Alibaba folks on the call. I posted some issues in the chat that were created by them.
There is a… I don't know if you're aware, maybe you talked to the people, there is an effort from LLMD.
Or something very similar.
And I think… I would love to have a discussion between people who are interested in this specific topic on, can it exist outside of OpenTelemetry semantic conventions?
Or… Like, for whatever reasons, it's… we cannot agree, and then it kind of have to land somewhere, but we need a place where all the people who are interested can collaborate and.
Define things together.
Yeah.
**Nir Rozenbaum (NVIDIA)** 23:03 So.
I have one comment about the… so first, we are well familiar with LLMD people. I've also been working with, Wenjia Liu, one of the authors of the LLMD doc. So… Basically, so just to give you, like, a TLDR.
On the differences.
So basically, LLMD is a router, and it… this is, like, one consumer of the metrics, right? So, if you want… so, what LLMD does today, they are allowing to work with different model servers. I think they have… they have 5 options, and then they have this in-memory translation table. So if it is VLLM, then they translate let's say, the running request to some, internal, representation. And if it is SGLang, they… they… translate the other, the SGLang metric to that struct. They have internal in-memory struct. And what we propose is different in a sense that the contract is within the model server pod boundary. So the pod exposes the contract, and then no matter which Kubernetes integration want to work with that contract.
They all work with the same… so we move it from the consumer to the producer. The pod who produces the metric produces the contract.
So if we want today, let's say LLMD, they have the LLMD router, and they have LLMD autoscaler.
if they want to implement it with GenAI metrics, they need to have the translation table in two places, right? Both in the router and in the autoscaler.
It cannot work otherwise.
If we move the translation to the metrics producer, then everything works out of the box. So, I'm not saying That we cannot collaborate, of course we can.
I'm saying there is, some sense of a difference here, and the new sub-project that we started within Kubernetes, the goal is to move the metrics towards the producer.
And not the consumer.
**Liudmila Molkova** 25:24 I understand. Trask, can you open the doc? I paste paste it in the chat. It's the last one.
If you scroll down the metrics they are trying to define, they are slightly different than the ones I saw in your proposal, but they are very similar.
In nature.
And they're about the same things. So, it… they can… they… It.
It probably doesn't matter where they are produced, like, to me, from my ignorant perspective, sorry. But since you folks work on the definitions, they look pretty much the same.
I think the collaboration needs to happen.
**Nir Rozenbaum (NVIDIA)** 26:10 Yeah, yeah, so you're… if I get it to you right, you're basically saying we need to converge on name plus semantics.
And then you don't care if it's consumer or producer.
**Liudmila Molkova** 26:26 Oh, sorry, I don't care from me today, because from the high-level perspective I'm trying to look, it seems you're solving very similar problems, and you would have same naming patterns, maybe the.
And I'm producing would be different. Or maybe the the proper ways to have metrics in both layers, I don't know yet.
But.
It seems it's there is a reason to work closely together.
**Trask Stalnaker (Microsoft Corporation)** 26:56 Yeah. To your…
**Nir Rozenbaum (NVIDIA)** 26:58 we.
**Trask Stalnaker (Microsoft Corporation)** 26:58 Quick to your what you're saying here. Yeah, from semantic conventions, we don't really care if it's producer or, you know, if it's a translation layer, it's just.
**Nir Rozenbaum (NVIDIA)** 27:09 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 27:10 I mean, yeah.
**Nir Rozenbaum (NVIDIA)** 27:11 Understood.
So, in your view, what do you see as the next step, like, or the next set of steps?
**Liudmila Molkova** 27:28 I would like to.
See where Alibaba folks stand, and… I can ping.
I work with Yang Gao, the… I think one of the authors of this document. I can ping him and point him to your document, but maybe we can… Kind of find the place and time.
Here, but what time to meet, and… You folks talk through and decide where you want it to be, and… Entertain the option of having it in somewhere where you work together on this?
That's not semantic conventions, and I am open to semantic conventions as well. It's just… it will be harder.
**Trask Stalnaker (Microsoft Corporation)** 28:23 I'm, just to expand a little bit on working on it outside of semantic conventions.
So with the federated semantic conventions, and the Weaver tooling that we use, it allows you to, define semantic conventions, like, kind of an extension.
That still leverages all the core semantic conventions from GenAI or from the core semantic conventions.
And that allows you to kind of basically get a lot of the tooling and, policies in place.
And if you worked on that, say, outside of semantic conventions, and then, you know, once kind of proving that out, and to Ludmila's point, the advantage of doing that is you would be able to iterate faster, right? You're not blocked on us merging PRs, which is where we tend to become a bottleneck sometimes. And, once you, you know, I think that this… Well, it could potentially, if it's scoped well, it could live permanently as a federated semantic dimension.
But it's also something that, we can always decide, you know, once something is established and proven out.
By, you know, that we could… look at bringing it kind of wholesale into the Semantic Convention GenAI repo.
Huxing, yeah.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 30:02 Yeah.
Hello, my name is Huxing, I'm from Alibaba Cloud. Actually, I've noticed that you have created that working group in the SIG, the new project, so I noticed that, so I reached out to one of my colleagues and to send this message and showing that we can discuss this in this server side in inference metrics semantic convention here actually i we are very interested in contribute to that actually we propose a existing issue in the repo maybe several months ago and actually we are pushing forward internally in Alibaba Cloud. We provide multiple support for different inference engines, like VLM, SGLAN, and RTPLM, which is another open source by Alibaba Cloud. So, actually, we are very, curious and encouraged to make that standard happen because that makes a burden to us and we want to standardize it and we want to connect them in a very universe universal way, so actually, we are very interested in making that happen. So, actually, I very agree with.
Trask and we can develop a new repo or maybe outside the repo first and we can iterate fast and then we make some progress and maybe make it more like stable, we can then like, contribute and merge to the GenAI repo this is a more easy way for us to contribute. I think this is a good approach for us, so we… from our side, we are very, very interested to see that happen, so we… Actually, we want to… actually, we also talk about, to maintainers from VOM and SGLANs, we have some contributions to this project, but we see that these projects, they may something there's difference between these two project maintainers, then I think we should make it happen and talk to these maintainers of that project to like to, adopt this standard, because, more… with more companies, get involved, I think it's more easier for us to convince them to embrace this standard. So, maybe one company, they may not be believing in us, but if Well, a lot of companies coming, and then I think this… It's more possible to become a standard. Okay.
**ziming liu** 32:54 Yeah, and I think, the… Inference server community is very happy to see that we contribute those, tracing or metrics to their community, because I'm contributing to SPLAN.
for some time and the maintainer of SGLine It's very happy to see that we just contribute our matrix and tracing instrumentation to the community.
Yeah.
**Omer Aplatony** 33:36 So, do we have… do… Yeah, sorry. Do we have a place that… I mean, a repo beside the LMD… doc, you just sent… where we can maybe discuss and have, like, you know, metrics that we already defined, and metrics that we are in progress to defining, and metrics that we said we are not going to define. Maybe something that we can track.
About those different semantics that we can… utilizers?
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 34:11 Yeah, I think there's a proposal that Zimin has proposed, and defines the difference for each project, and we'll try to, like, to have a… More common way to express that semantics.
I think Ludmila has sent a PR in the comments. We can check it later, maybe.
**Nir Rozenbaum (NVIDIA)** 34:40 Yeah, I think, like… Overall, if we can get, like, let's say… a broad agreement that collaborating in… within Kubernetes.
Is the best home, because eventually.
every component… ILLMD, like, it is a router. Like, autoscaler cannot take a dependency on a router, right?
And the same thing for observability, or for autoscaler, so a router will not take a dependency on autoscaler. So, if we are thinking about a neutral home that can hold this, limited Thing, limited contract.
Then.
I believe no one in the ecosystem has an issue with taking a dependency on a Kubernetes repo, right? Same as… LLMD, they take a dependency on LWS, on a disaggregated set from Kubernetes, from different, multiple different repos from Kubernetes. They do not have an issue with this, because they are Kubernetes-native distributed inference.
So, in that sense, I think It should be more of the same, and if we can get that GenAI part around inference.
done in that repo, and we are more than happy to collaborate with anyone in the ecosystem, whether it's LLMD folks or Alibaba.
We actually, we would like to welcome more and more contributors and partners to make this a really, like, vendor-neutral and really collaborative effort.
**Trask Stalnaker (Microsoft Corporation)** 36:22 And I think that's a really… key piece of success of the federated semantic conventions, when living… when it lives outside of OpenTelemetry, like, the key is finding a vendor-neutral home for that.
And that's why, but you all have that already, so you're kind of set up perfectly there. And then also you can have very.
Consolidated discussions on this topic.
Versus in this SIG, right, like, we've got a lot of topics, most of the people here are gonna be talking about client-side stuff, so, like, I do think that would allow you all to move faster.
At least, you know, again, for the… for proving all of this out, and then someday, you know, we can talk about whether it makes sense to bring it into the core GenAI repo.
Chris Hagelin, And we can definitely, and you should definitely advertise that. Feel free to advertise that in our issues.
On any issues that are related to, you know, point people over to your repo.
**Nir Rozenbaum (NVIDIA)** 37:40 Yeah, perfect. Sounds good.
**Liudmila Molkova** 37:45 Do you folks have any meetings?
We're… Any place people can join and talk?
**Nir Rozenbaum (NVIDIA)** 37:52 So, this is actually a really new repo, like, we've created it, I think, a few days ago.
We're going to create, of course, a community call, whether it's going to be weekly or bi-weekly, I don't know, depends on how many issues and… and, pull requests and things, you know, depends on the volume.
But yeah, definitely, we're going to define it sometime soon, and publish it, whether it's in our… we have a Slack channel within Kubernetes Workspace, we can publish it in your Slack channel as well. And, yeah, yeah, of course we'll do this.
**Trask Stalnaker (Microsoft Corporation)** 38:30 Yeah, please do feel free to always to use our Slack channel to advertise anything that you want about your SIG or about the work you're doing.
**Nir Rozenbaum (NVIDIA)** 38:39 Yeah, sounds good.
**Omer Aplatony** 38:41 I'm good.
**Trask Stalnaker (Microsoft Corporation)** 38:46 Cool, we are at time.
Apologies for not getting to any other issues, but this was a big, important one. Glad we had time to talk through it all, and glad we got to meet you all.
**Omer Aplatony** 39:02 Thank you. Thank you very much.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 39:04 Thank you.
**Liudmila Molkova** 39:05 Thank you.
**Omer Aplatony** 39:06 Bye-bye.
