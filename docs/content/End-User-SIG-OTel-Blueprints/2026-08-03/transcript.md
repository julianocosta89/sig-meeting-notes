SIG: End-User SIG: OTel Blueprints
Date: 2026-08-03
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Lukasz Ciukaj (Splunk Inc.)** 00:51 Hello!
**Siva Guruvareddiar** 00:55 Hello, Lukasz.
**Lukasz Ciukaj (Splunk Inc.)** 00:56 Nice, Siva. Do I pronounce your name correctly? Is that Siva, or Siva?
**Siva Guruvareddiar** 01:00 Yeah, it's Siva.
**Lukasz Ciukaj (Splunk Inc.)** 01:02 Siva. Hey, how are you?
**Siva Guruvareddiar** 01:03 I'm good, are you?
**Lukasz Ciukaj (Splunk Inc.)** 01:05 I'm doing good, thanks for asking. Where are you based in?
**Siva Guruvareddiar** 01:08 I'm from Austin, Texas, from US.
And how about you?
**Lukasz Ciukaj (Splunk Inc.)** 01:13 I'm originally from Poland, but now in North Carolina suburbs of Rani.
**Siva Guruvareddiar** 01:19 Nice.
**Lukasz Ciukaj (Splunk Inc.)** 01:21 What's the weather in Austin today?
**Siva Guruvareddiar** 01:24 Yeah, it's been crazy. Today it is… now it is 88.
**Lukasz Ciukaj (Splunk Inc.)** 01:30 -Oh.
**Siva Guruvareddiar** 01:31 Yeah, so last week it was pretty bad.
It was around 100, too.
last week.
I think this week is… should be okay.
And, but, by the way, how is the weather in NC?
**Lukasz Ciukaj (Splunk Inc.)** 01:46 It's… it's not that bad, I would say. We had some heat wave in July, but now the weather is pretty, like, moderate, so it's… I mean, modest. It's okay, like, I'm not complaining.
**Siva Guruvareddiar** 02:01 Nice.
**Lukasz Ciukaj (Splunk Inc.)** 02:01 Yeah, so… Dan pinged me that he will be late a few minutes to this call. I'm not sure if anyone else gonna join us.
And I believe you'd like to review or discuss the blueprint that you are working on, correct?
**Siva Guruvareddiar** 02:18 Yeah, correct. So, if possible, if time permits, like, you know, I would like to discuss about the Blueprint and, the next steps.
**Lukasz Ciukaj (Splunk Inc.)** 02:26 Yeah, so yeah, let's maybe wait for Dan to join, so we can all together review it. Not sure, let me check if we have any… Notes for today, or anything in the agenda?
I see we have Joe as well. Hi, Joe.
**Joe Josue** 02:45 Everyone.
**Siva Guruvareddiar** 02:47 Hey, Joe.
**Lukasz Ciukaj (Splunk Inc.)** 02:48 Yeah, I don't see anything on the agenda. Let me check the last meeting… Blueprints, and… Okay, the labels, so that is something that I… I was working recently on… Give me a sec… Close a few things here… Maybe I will show you what I was working on.
To give everyone the update.
Trying to reorganize the stuff.
Yeah, so… Open helmetry… So, can you see my screen? You should be able to see.
**Siva Guruvareddiar** 03:45 Yeah, we can see your screen.
**Lukasz Ciukaj (Splunk Inc.)** 03:47 Yeah, so something that we are working on recently, because the Blueprint initiative is still pretty new in the OpenTelemetry.
So, something that we wanted to improve is the documentation for Blueprint and reference implementations, so we got some feedback from some people that it's a bit confusing to find out where to get started, because if we go to Opentelemetry.io, and go to the documentation part.
And then we go to the concepts, I believe. No, it's not concepts, it's,
**Siva Guruvareddiar** 04:28 Maybe the Blueprints?
**Lukasz Ciukaj (Splunk Inc.)** 04:30 Yeah, there is a Blueprint, yes, we have now a dedicated section. So we go to Blueprints, there is the section, how to contribute.
And, but this is, for those… I mean, oh, Siva, perhaps you… you know how it works. Like, Opentelemetry.io is the GitHub repo for the documentation, website, and all of that, right? So… so that's the one piece, but… The Blueprint Initiative is part of End-User Seek, right? So we have two different GitHub repos, so that's the reason we wanted to improve the documentation And I'm working on that actively, so we have a nice progress of this at the moment. So what I did, I opened 1PR under the End-User Sik, which is now merged. So if we go now to the… And user seek, open telemetry… And go to the… architecture… And then we have, updated the Blueprints and reference implementation process, with all of the steps that are required, with details, where to open PR, where to open an issue, and also the label reference, so now everything is clear. We believe that now it would be a bit easier for new contributors to follow that, and also for us, for Blueprint team, it would be easier to navigate through it by assigning labels and providing the feedback updates, so… so we believe that that's a good progress, and that can help us really to… especially for new contributors to… get started. What is missing is updating this, the documentation page to put a reference to End-User Sikh to this new contribution process, so once this is done, this issue will be closed. So we believe that after this, it will be a little bit easier for everyone to navigate through it, so… so that's the only feedback I had, and update that I wanted to share with the team, and I see that Dan joined in the meantime. Hi, Jack.
**Dan Gomez Blanco** 06:34 Yeah, there is another thing that I added to the SIG End-User repo, and thanks so much, Lukasz for doing this, in the top of the fold of a repo, as in, like, at the root of a repo.
**Lukasz Ciukaj (Splunk Inc.)** 06:45 There is no.
**Dan Gomez Blanco** 06:46 Now, a mention of that, basically, and… no, and the… the root of,
**Lukasz Ciukaj (Splunk Inc.)** 06:52 Indeed.
**Dan Gomez Blanco** 06:53 I spell.
**Lukasz Ciukaj (Splunk Inc.)** 06:54 Just in case.
**Dan Gomez Blanco** 06:54 It's like people land here, and they go to… they scroll down. I did add here, basically, that if you scroll to the top of this…
**Lukasz Ciukaj (Splunk Inc.)** 07:01 Nope, okay.
**Dan Gomez Blanco** 07:02 is, like, you know, I added some more stuff to the charter, right? So there's, like… Yeah, so this… The primary goals, and then there is a… ways to get involved.
Which is, if you scroll down, yeah, so, like, the… there would be… Something there to open a Blueprints proposal, yeah.
But then there is a triage aspect, yeah, issue triage, which basically points you to that, right? Blueprints or reference implementation issues, they fill a specific… expansion process.
**Lukasz Ciukaj (Splunk Inc.)** 07:38 Thanks, and that's, yeah, that's definitely needed. Some people are starting from this landing page, right, from the root, so it's good that you updated this as well. Was it part of any issue, or you just updated it…
**Dan Gomez Blanco** 07:49 It was part of a general issue that we had in the… that I brought up with the rest of the End-User SIG, including, if you go… if you scroll up, there is a file that says Charter, like SIG End-User Charter Charter.
**Lukasz Ciukaj (Splunk Inc.)** 08:02 Yep, this one.
**Dan Gomez Blanco** 08:03 So we updated that. I mean, it's not like… things that are in scope, things that are not in scope, it's not… massive, but yeah, so I think I added.
Blueprints and reference implementations here, which is…
**Lukasz Ciukaj (Splunk Inc.)** 08:17 Cool.
**Dan Gomez Blanco** 08:17 That shouldn't be,
**Lukasz Ciukaj (Splunk Inc.)** 08:20 Yeah, but then, so for this issue that I opened and that I'm working on, so the other PR that we have on OpenTelemetry.io.
**Dan Gomez Blanco** 08:29 Yep.
**Lukasz Ciukaj (Splunk Inc.)** 08:29 See, this one is still not merged, and there was a comment from you… And, like, nobody is, like… I tagged the dogs, maintainers…
**Dan Gomez Blanco** 08:40 Yeah, maybe, can you, share that in the OTelcoms Slack channel? Maybe. I don't know, if you haven't.
**Lukasz Ciukaj (Splunk Inc.)** 08:47 I don't have access to it. I tried, but I think this is only for maintainers. OTel comms? OTel comms, you mean, right?
**Dan Gomez Blanco** 08:54 Yeah.
Is there enough?
**Lukasz Ciukaj (Splunk Inc.)** 08:56 Oh yeah, OTel comes, I do have an access, okay, so I will post it there.
**Dan Gomez Blanco** 09:01 Okay.
**Lukasz Ciukaj (Splunk Inc.)** 09:02 Sounds good.
**Siva Guruvareddiar** 09:03 I think this… this is a great initiative, Dan and Lukas, thanks for sharing. So, maybe, like, you know, yeah, maybe I can work with you guys if you think any help is required, like, you know, I'm more than happy to do it, because even I… I saw this firsthand, like, you know, when I was proposing it, I had to go through a lot of bunch of places to figure out how to do that, yeah.
**Dan Gomez Blanco** 09:23 Yeah, so I think, you know, we're trying to make it easy. There's another… there's also another issue that I think I said I would work on, I've not really had the bandwidth for, which is related to improving our… guidance, basically, on what a good blueprint, It's, like, that communicate Blueprint and reference implementations… guidelines, yeah, so I think this is more like… We currently have some of it I was like… Markdown comments. But what we said was, like, it would be good to create another document.
You know.
To… this is why, you know, we're sort of, like, not really pushing forward with more Blueprints, to review more Blueprints at the moment.
is that… it's good to have, like, the framework in place, right? So I think, the… the main goals of the initial project, that is, in OpenTelemetry, as an OpenTelemetry initiative.
Was to do 3 Blueprints, which was the 3 that we agreed on, do 5 reference implementations.
And I think we've got 3. Now, the reason why we've got 3 is because the DevX, the Developer Experience End-User Group, sorry, the Developer Experience… SIG.
Mmm… created those, and now we're porting them to… instead of being blog posts, being reference implementations, but, you know, they are in progress, to publish another… another two.
So then we'll have 5. 5 revs implementations, 3 Blueprints, and a framework to continue to evolve. After that's done, we can close the… I think we can… there was a blog post proposal there. I think, you know, we're… if we're almost there, I think we should probably focus on finishing these initial things.
Close the project, or we can call it complete, and then have a blog post where we announce that, hey, you know.
We've got 3 Blueprints, we've got 5 reference implementations, we've got a framework, now we can call for more.
contributions and more actions, right? Call to action. So I think this is where we are at the moment, and that's how I see the project evolving. Then the more people that will have to go and, you know, help us review stuff and… And… and all that is… yeah, it's gonna be super welcome, so… thanks for… thanks for joining. And… both Siva and Joe.
**Siva Guruvareddiar** 11:55 Yeah, Dan, like, you know, if time permits, like, you know, I would like to discuss about, the one that we are discussing, the Blueprint.
**Dan Gomez Blanco** 12:03 Yeah, of course, yeah, but before we move into that, I think, Alex… Had, mention that… a comment there, I'm not sure if you want to see anything about the… Except it might be an easier… thing to talk about first. So anything about the, the Kubernetes Blueprint, Alex?
**Alexandre Ferreira** 12:23 Yeah, hey folks, my camera's off because I'm, I'm cooking, some food here, but, so then, I just saw your, your comments, I'll… I'll work on them. I guess the… The only thing that… not that we have to agree upon, but perhaps other people need to take a look into it, is using the operator and the collector Helm charts independently, versus using the CubeStack.
collector, and… I… like you mentioned, I think the… The CubeStack doesn't use the Coblet stats receiver just yet.
I don't have a preference to either option, but I want to make sure that we are suggesting something coherent.
to where Kubernetes development is going, right?
**Dan Gomez Blanco** 13:25 Yeah.
I think that's important, is that we, whatever we… you know, we propose, I guess, that is the… right now, that is the… the advice that we have from the community, right? And I think if, I don't know enough about the… Cube Prometheus stack, right? Sorry, the OpenTelemetry cube stack.
Yeah, so I don't know… I don't know if the idea of… because all these are handled by the same group of maintainers, and the helm.
Helm approvers and helm maintainers, so, Yeah, I don't know what the… what the advice is. I think I have tagged them into that PR, but I will…
**Alexandre Ferreira** 14:10 Yeah.
Yeah, you have, you have. So, perhaps, like.
The feeling that I have is that some of this is still, like, being developed and discussed.
to the point where, like, if you were to deploy something today, you would probably use Nature Collector separate?
I mean, each chart separately?
**Dan Gomez Blanco** 14:33 It's child.
**Alexandre Ferreira** 14:34 Yeah, so, what are our thoughts on deploying it as sys, and then perhaps… Having the… the chart… maintainers… Possibly looking into and improving whenever the… the overall chart, the cube chart gets to a point where we can… confidently suggest this through every single Kubernetes installation.
**Dan Gomez Blanco** 15:06 Yeah, that's… That's a good idea.
I think we can… we can… I mean, we can… I mean, they're… they're going to have to… look into this as well, right? Because they're part of… Yeah.
We want to have their opinion anyway, but yeah, so that… that makes… that makes sense.
**Alexandre Ferreira** 15:24 Alright, I think this is… this is me for today, so I just saw the comments, I'm going to work on it and ping you whenever I do. And, from the looks of it, we are almost there, like, one or two reviews away.
**Dan Gomez Blanco** 15:39 C-coo-coop. I see that, I may need to re- remove that.
You have signed the CLA now, right? So, I think… That wasn't…
**Alexandre Ferreira** 15:47 enabled us.
**Dan Gomez Blanco** 15:48 like, missing CLA, and I don't think it is, yeah.
Yeah, cool.
I will… ping… I will just… I'll ping the helm approvers, If you want to do it yourself, as well, on Slack, or if there is an OpenTelemetry help?
OTel… It is an OTel helm, I think it might be worth… Asking about, you know, what's the current status of,
**Alexandre Ferreira** 16:20 Only time.
**Dan Gomez Blanco** 16:20 Prometheus, OpenTelemetry, KubeStack.
and see if they… If it can have a…
**Alexandre Ferreira** 16:27 collar.
Yeah, I'll send a message there.
**Dan Gomez Blanco** 16:31 Awesome.
Okay.
So, we normally go in, like, I was gonna mention that we normally go and mention the topics here in this… in the… in the notes, in the meeting notes that I share in the chat.
But, yeah, okay, I see that someone's been taking notes. Nice.
Okay, so, Oh, it's a general cancel. Yeah, so OTel Blueprints. Siva, do you want to… Take us through, I guess, your topic, which is related to the… your proposal?
**Siva Guruvareddiar** 17:25 Yeah, sure, yeah, let me quickly, so can I talk about it, or do you want me to share anything for the group, or how do you want to take it?
**Dan Gomez Blanco** 17:36 But if you… if you want to, yeah, maybe, like, share your screen or introduce the topic, that would… that would help, yeah.
**Siva Guruvareddiar** 17:42 Cool, let me share my screen.
Yeah, thanks, Dan. Yeah, so my proposal is, like, you know, I wanted to have a proposal for AI inference platform observability on Kubernetes.
So, today morning, like, you know, I was working on Dan's comments. Like, you know, my initial proposal was to come up with 3 different challenges. Challenge number one is GPU opacity.
Where we wanted to identify what are the GPU hardware utilization at the pod level, namespace level, at team level. So that is challenge number one.
And challenge number two is, related to that, we wanted to have a per-tenant GPU cost attribution, so that's challenge number two. And challenge number three is, like, you know, when we are doing multi-agent, how do we do with tracing, with open trace context propagation, how can we do that?
But based on Dan's comments, like, you know, I think it is still on very early stages. I would say, like, you know, that particular application-level challenges, we can scope it out.
So, at this point in time, as part of my proposal, I am doing, like, you know, two different challenges I wanted to address. The first one is the GPU utilization opacity.
So my idea is, like, you know, we can see, like, if GPUs are emitting signals, for example, DCGM. So DCGM, I'm just using that as an example, like, you know, I'm not enforcing that as any OTel limit standards. So the source signal it is emitting, so anytime, like, you know, more than 300 plus metrics, it is coming out.
So then, along with that, like, you know, using Kubernetes Attribute Processor.
take all the pod-level, team-level, labor information, and enrich it, and then send it to the telemetry backend. Like, in this case, again, it could be, like, you know, Prometheus or whatever, right? So, with that one, like, you know, with recording rules and all those, with Prometheus standards.
or it could be, like, an equivalent of other things in other tourings. We should be able to identify, like, you know, what should be the utilization opacity, right? So that's my challenge number one, and my challenge number two is, like, you know, the cost attribution.
So in this case, like, you know, there are no chargebacks. So basically, the FinOps team is not able to produce, like, you know, okay, hey, this is what, like, you know, I allocated to you, and then how much you are using it, what is the waste stage, and all those things. So that is something, like, you know, with this… particular strategy of taking the GPU metrics along with the Kuberdotes attribute processor, and then combining that with the, maybe how much, for example, like, you know, in AWS, if I'm using, like, you know, A100 instances, so I can run a sidecar which goes and talks to AWS, gets a pricing API, so that I can give real-time information on how much that particular team is using, instead of estimating and all those. So that's on a high level, like, you know, my proposal is.
Let me take a pause here for any questions.
**Dan Gomez Blanco** 20:48 So the, I guess the, the… the core is really… the core of the issue, basically, is related to… yeah, to… to GPU… Observability, right?
**Siva Guruvareddiar** 21:03 So it's basically on the inferencing part, like, you know, we are not necessarily focusing on training part, like, it's end of the day, like, you know, many customers are using inference workloads, and then they don't know, because many teams are using it, they don't have any clue, like, you know, how much they have been allocated, how much they have been using it, how much they have been wasting it, and all those things. So this particular proposal is able to solve that particular problem.
**Dan Gomez Blanco** 21:27 And, and I think one of the things that, I guess, in the past.
this probably relates to that other PR that was raised, is that we need to be very careful with, you know.
with… I guess with OTel Blueprints, we need to be careful that we don't touch the backend perspective, right? The observability back-end, because that's not something we're… Either the observability backend, or, like… an SRE agent, whatever, like, you know, data… like, the analysis of data. I guess that's… that's the perspective where, like, we should focus on the… on the instrumentation side, which is where OpenTelemetry's scope is, right?
Which I think this aligns with that, and then how that instrumentation can then lead to better analysis, rather than focusing on the, you know, on the analysis itself. So that makes… that makes sense.
**Siva Guruvareddiar** 22:22 Yeah, totally, 100%, like, you know, that's why I said, yeah, we are just taking, like, you know, maybe Prometheus could be a backend, maybe in the reference implementation, we can say, like, hey, in this example, we have been using Prometheus, maybe if you want to use something else, like, maybe Victoria matrix or something, yeah, it's up to them, yeah.
**Dan Gomez Blanco** 22:38 Cool. And then the other aspect is, I guess, things that are not, You know, we're having this discussion about the… the Kubernetes Blueprint, right?
As things that are not… stable, let's say. Things that are not, like… either not stable, or that they're not, you know… if they're in OpenTelemetry, if they're within OpenTelemetry, that's different, right? Because, like, we know that certain things may not be completely stable, but, like, they are… being used in the community, right? Even the collector, if you take it, the collector itself is not completely stable, right? So, I guess… this is what I don't… I don't know enough about, like, GPU monitoring, or, you know, what stuff can be done with OTel tooling, what stuff Can be done with other standards that we are… that we are, proposing here, and how we make sure that we're not You know, proposing something that is either not a cloud-native standard.
or that's not integrated with cloud-native tooling, I think this is, like, where we need to be, as well, a bit careful, right?
**Siva Guruvareddiar** 23:47 Exactly. Yeah, so I totally agree, Dan, like, you know, in this case, I just wanted to… because earlier I was using, like, you know, a lot of other things, like, you know, including the semantic conversions that we are still worked up on, but now I'm kind of, like, you know, working on standardizing all those things, whatever it is approved, and then it is used, within our vicinity, like, you know, that's what I'm using.
But yeah, that's what, like, you know, please, take a review, and then let me know if anything needs to be changing, but I think at this point in time, we are good. We are just making sure whatever in the open delay scope, that's what we have been using.
**Dan Gomez Blanco** 24:23 Cool, awesome.
Sounds good. As I said, you know, like, I'll… happy to… to… for others to start having a look at this. I probably will try to focus the effort on the… on the Kubernetes one, on the review of that, but if I… So yeah, what I'm saying with this is, like, I can't promise to have bandwidth to review this at the moment, but thanks for… thanks for sharing. If anybody else has bandwidth to… to start reviewing this ahead of time, then, yeah.
**Siva Guruvareddiar** 24:54 And one question, Dan, like, you know, currently I see this as being assigned to Alolita for review as an assignee. Is that something she will be doing, or any other next steps?
**Dan Gomez Blanco** 25:07 Yeah, I think she's self-assigned. So she's… she couldn't make it today, but but I think she, She said that she would be looking at this as well, so, yeah.
**Siva Guruvareddiar** 25:16 Cool, cool.
**Dan Gomez Blanco** 25:18 And then I think Olita might have more experience with GPU workloads, so, yeah, she's probably… I mean, I… personally don't have much experience with GPU, workloads, so yeah.
**Siva Guruvareddiar** 25:33 I see it, I sent.
**Alexandre Ferreira** 25:36 So, hey, Siva, Alex, nice to meet you.
Similarly to that, I don't have much experience with GPU monitoring, however.
I have a customer that's trying to do class attribution, on GPU.
and from the looks of it, the OpenTelemetry community doesn't have a… alternative to the… to the GC… the GCM exporter from NVIDIA.
So, like, together metrics around that, there's no… there's not a OpenTelemetry native way of doing it, but that being said.
First, this, this proposal could… Inform the user, like, what… components they should be… be observing. But on the cost attribution perspective, specifically, there's a challenge to… to generate GPU costs whenever they're not being run on a cloud provider.
If it's interesting to you, check this message Hosanna in the channel. It's from the OpenCost channel.
Where, I was asking about GPU observability costs, and… Take a look into it, see if it relates to your idea.
And then, the open cost tool specifically doesn't have much documentation on how to generate custom pricing on CSV.
Or… reviews and every other component, really.
So, I would suggest seeing if this… this helps out.
Stop.
**Siva Guruvareddiar** 27:31 Yeah, cool, thanks for sharing, Alex. Yeah, let me take a look into it, and then I will see, like, you know, if I can interpret that one as well. Yeah, as you know, like, you know, this space is rapidly evolving, yeah. So, yeah, maybe, like, you know, I will take a look into it, like, you know, what that particular open cost is trying to do, and then I will try to Maybe incorporate as part of the proposal.
Thanks for joining.
**Dan Gomez Blanco** 28:01 Cool.
Yeah, thanks for sharing. I think, as I said, I will see if, if we can have, More reviews, I'm… I think I'll… Yeah, I'll personally say that, maybe after the… I'll prioritize it myself after the, the Cates one, and other work that is happening in… To close this project, to close the initiative?
The initial, set of deliverables.
But yeah, I think that sounds like a… like a good one. There is also, I should say, probably, that there is also a… I'm also part of, of a working group within the Green Salt Work Foundation, which is interesting, that just makes me think about cost attribution, and I think one of the elements that they're trying to… they will be trying to standardize is on… Some of the measurements for carbon emissions, right?
With OTel semantic conventions, so they'll be spinning up their own… their own federated registry for Sencomp.
And it'd just make me think if, if that is an element of, you know, Alex just mentioned cost, and I was thinking… if there is an element of power output as well in this, right? Which… in this Blueprint. Which is something that… Yeah, I guess.
another type of measurement that people would be interested on. I'm not sure if this is possible with the current tooling, but yeah.
**Siva Guruvareddiar** 29:37 Yeah, yeah, yeah, maybe, yeah, thanks for sharing that one, Dan. Like, you know, maybe as a next step from my side, like, you know, I will go ahead and then improve on the dog, maybe removing the challenge number two that we discussed today, and then I will also follow up with Alolita if she has some cycles to review it, and then I will… I will go ahead and do that. Yeah, thanks.
**Dan Gomez Blanco** 29:57 I think one of the things, yeah, I think ultimately, if you want… I mean, a good blueprint is one that basically is able to list I mean, we will apply… it's almost like, you know.
you… the advice that we give, or the guidelines, may be almost like the same, right? But if you're able to expand the places where this can be applicable to, which could be cost management, it could be, you know, you're trying to solve issues with… In terms of GPU observability in areas of, Yeah, like, energy, consumption, or… Yeah, I don't… I think water will be a bit more difficult, Alex.
But, but yeah, so then that's, that's another, that's another element.
**Siva Guruvareddiar** 30:42 Yep.
**Dan Gomez Blanco** 30:44 The more that we can make it applicable to more people, the more that… in a specific context, the more useful it will be.
**Siva Guruvareddiar** 30:52 Cool, thanks.
**Dan Gomez Blanco** 30:57 Alright.
Any other topics?
Just trying to think. There's one thing, I will raise an issue for this.
But going back to the… Well, if someone wants to raise an issue for this, go ahead, and we're not going to be able to do it today. But there's an issue that we should probably raise in the second-user repo, is to discuss how we… How we get better at, assigning.
Reviews and stuff.
So at the moment, if someone raises a PR and, OpenTelemetry I.O. repo.
we are not marked as code owners, as in we have a GitHub team, but we're not being marked as code owners of, of the repo. Same with, like, co-owners of the… Of the Blueprints and reference implementations.
Which… Yeah.
Would need some collaboration with the… with the website maintainers.
Yeah, so that's an aspect that… We should probably start to work on.
Send me the end-user repo. I think now that we have better labeling, we could probably, at least for the… for the… for this group.
We could have a… I forgot the name of a… It's probably not an action.
a GitHub action.
For… if you have a specific label, or if you apply a label.
on a… on a PR… on a PR, or… or an issue.
For example, Blueprints.
That it automatically adds the team as… Assigning, or assign… assignee to that?
As in the Blueprints approvers?
I think that would help things. So we don't miss things, right? So if someone raises a PR in… Somewhere, that we don't miss it.
**Alexandre Ferreira** 33:00 So, Ben, quick question on that. So… this is my first contribution to the community. Whenever the PR merges, like, Do you think… The person that first… that initially created the Blueprint would be assigned as a code owner, plus… the relevant group.
Or that, or that context? Or, like, is the ownership… donated to that group, say, like, the CAIC Shark Team.
For the Kubernetes Blueprint.
**Dan Gomez Blanco** 33:37 No, yeah, so the agreement that we've got, in a way… well, I'm written agreement until we put this in the co-owners.
Actually.
I did realize that.
There's not a co-owner's file.
But I think there are things being applied, I think they do it in a different way, in the OpenTelemetry I.O.
What I would like us to… let me just share my screen.
I would like us to be code owners, too. And when I say us, I mean the… the, everyone's welcome to… Contribute, of course, but there is a… OpenTelemetry… Blueprints approvers, right?
Ideally, what is it? It should be part of… Yeah, so anything… anything under here.
Should be… the co-owners should be the approvers, the hotel.
I'm not saying code on… there's no code on us here, but if someone raises a PR against this.
We should be asked for, or, like, requested for our review, right?
And then we get… yeah.
And then as we get more approvers, then that will… That'll make it easier.
But yeah.
**Alexandre Ferreira** 34:58 following, right?
**Dan Gomez Blanco** 35:00 Good stuff.
**Alexandre Ferreira** 35:02 Nice.
**Dan Gomez Blanco** 35:04 But yeah, I don't… I don't think it would be, the… it's our responsibility, in a way, as approvers, to ensure that we… that we link the right people, right? So that's part of the… I guess part of the role is that.
**Alexandre Ferreira** 35:18 Oh, it's… I see what you mean.
**Dan Gomez Blanco** 35:21 So, you know, if you raise a new blueprint, or there's a new blueprint for… I don't know, Kubernetes observability. Okay, well, then we'll engage the… the people in the helm, the Helm approvers, right? If someone raises up PR on the… on GPU, for example, as Siva was saying.
I don't think we have a specific group, but the closest one may be the GenAI. I don't know, just people to… to… to give, you know, that may know more about that there.
So, yeah, so I think… We'll just have… Have that position in the community to, like, go and reach out to specific people that we know, or teams.
**Alexandre Ferreira** 36:01 Yeah, I see what you mean.
**Dan Gomez Blanco** 36:03 as well as.
**Alexandre Ferreira** 36:03 It's like, they're not Dorn's, like.
We will not gatekeep the review itself, but as… Like, contributors, we should point them out to the, like, mention the correct groups, right?
**Dan Gomez Blanco** 36:17 Ultimately, the final review should be ours, like, the approvers, but… we won't give it until there is, like, until everyone's happy, right? I guess, yeah.
**Alexandre Ferreira** 36:26 Yes.
**Dan Gomez Blanco** 36:27 Yes.
**Alexandre Ferreira** 36:28 All right, agree.
**Dan Gomez Blanco** 36:29 Sounds good.
Any other topics?
**Lukasz Ciukaj (Splunk Inc.)** 36:40 I've got one, done, so… Correct me if I'm wrong, so we are still waiting for these two additional reference implementations, and let's say, one or two more Blueprints to close the project.
**Dan Gomez Blanco** 36:54 one.
**Lukasz Ciukaj (Splunk Inc.)** 36:55 Just one, okay. So the one that Siva is working, or the one that Alexandre is working, right?
**Dan Gomez Blanco** 37:01 Yeah, so that's the CA sorts of ability, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 37:04 Okay, and that we are pretty close to be finalized, and for the reference implementation, you said that DevOx team is working on two more?
Is it tracked by issues, or where it is?
**Dan Gomez Blanco** 37:20 That's a good… that's a good question.
**Lukasz Ciukaj (Splunk Inc.)** 37:22 It's not practical issues.
**Dan Gomez Blanco** 37:24 It's not… it's not really tracked by issues that I can… that I could find anywhere, but it's… they're… they're posting some updates on the DevX SIG, and I… and every time that the meeting happens, I've got a clash with it, so I've not been able to join, but I've asked them about it, and In there. And so let me go back to here, where we have OTel Blueprints as a project.
Deliverables.
reference architectures… Blueprints.
Mmm… Did we give it exact numbers? I can't remember.
Yeah, we did.
So… Work objectives will be to find a standard repeatable process for caption and publishing End-user reference architectures.
We do have that, and that is what we… well, I told them that, well, instead of us going to end users and, like, you know, we're not really spending any cycles and actually asking end users to do it.
But as they publish in these new blog posts, what I did ask them to do is to, To go through the template, the reference implementation template.
And then get feedback on that, because they may not have used it for the blog post that they published.
But they'll probably have some good feedback on… on it, right? So after that, I think we can call it done.
The same for… for Blueprints, we do have it, that… template.
and process.
5 Revis architectures, 3… So 3 Blueprints, yeah.
And then I discovered a location. So I think we are almost there, but yeah.
**Alexandre Ferreira** 39:15 So, question on the reference executive for the Kubernetes one, Where is the reference architecture going to come from? Do we have any customers, or any, like… component.
That would carry this reference technology?
**Dan Gomez Blanco** 39:34 Good question.
**Alexandre Ferreira** 39:35 I have… I have seen pitfallners, but they… really is, like, none of the box.
Types of deployment, so… I wouldn't want to add them as a first reference, because…
**Dan Gomez Blanco** 39:48 Yeah, you don't need to… I mean, you don't need to add them if you don't… I mean, this one, for example, just gonna start with… this one doesn't include anything related to Kubernetes monitoring. Mastodon doesn't include anything… Bo.
I mean, it runs on Kubernetes, but, like… It doesn't talk about Kubernetes-specific, right?
To use the operation.
**Alexandre Ferreira** 40:10 choose one.
**Dan Gomez Blanco** 40:11 They do metadata enrichment, but I guess… Yeah, doesn't cover that, and I don't think the Adobe one covers that either.
Again, they use the operator for auto-instrumentation, but that's where it's mentioned.
So, I don't know if the other two that are coming are using more of the OpenTelemetry, tooling for Kubernetes, but if you don't have any, it's not… We will be able to, like… change them in the future. However, like… If you, if you want to convince any of your… Of your, of your customers, or I can do that with mine as well.
Whoever is in this call that works with end users, or is an end user.
and we want to share one, that would be great as well. I mean, I think reference implementations are… I'm a bit less… concern about the bandwidth, because, like, ultimately, they're just completely self-contained, right? When we think about Blueprints, they're all gonna be connected in some way, and we need to think a little bit.
Carefully about how we want to structure them.
But reference implementations, I think, is just more like… Yeah.
As long as someone can come and write it, then… That would be great.
**Alexandre Ferreira** 41:30 Yeah.
I just have one customer using OpenTelemetry, the other one's just, our oil.
But… I'll shoot them a message and see if they would be interested.
**Dan Gomez Blanco** 41:43 I'll do the same. Yeah, I've got a few that are using… Yeah, no.
**Alexandre Ferreira** 41:47 Okay.
**Dan Gomez Blanco** 41:48 I mean… That's a… that's actually an interesting… an interesting one. You mentioned alloy.
I guess, you know, it would be the same for… like… I guess customers using NRDOT, right, which is a new distribution for OTel, which does Kubernetes monitoring.
**Alexandre Ferreira** 42:06 Yeah.
**Dan Gomez Blanco** 42:07 I guess I had it more specifically targeted for it.
I guess that's okay, if there are, like, reference limitations that they're like… You know.
**Alexandre Ferreira** 42:17 No.
**Dan Gomez Blanco** 42:18 As long as… as long as it relates to OTel, right? If we don't focus on the other stuff, that… alloy does, or that inner dot does. Yeah.
**Alexandre Ferreira** 42:31 There are, like, rappers around OTel, so, like, most of it should be translatable to OTel, but, like.
**Dan Gomez Blanco** 42:39 Yeah.
**Alexandre Ferreira** 42:40 I personally haven't it?
**Dan Gomez Blanco** 42:41 I'm personally okay. If there are distributions, if they qualify as distributions, then even better, right?
**Alexandre Ferreira** 42:47 Oh, I see, yeah, good point.
**Siva Guruvareddiar** 42:50 And Dan, like, you know, if the thing about ADOT we are talking about is that more on the lines of the customer using ADOT, and then we can consider that as a reference implementation? Is that the right understanding?
**Dan Gomez Blanco** 43:04 Yeah, I mean, that's fine. I think, what we… if someone… I think if someone is using a distro, it's the most normal thing for customers, right? So… Yeah, I don't see that as a problem for… for reference implementations. I think… I think we would be closing our… We'll be closing our… gates to a lot of customers that are using distributions, and in a way, that is… almost, like, encouraged by OpenTelemetry, right?
**Siva Guruvareddiar** 43:29 You know…
**Dan Gomez Blanco** 43:30 with that.
**Siva Guruvareddiar** 43:31 Yep.
**Alexandre Ferreira** 43:32 God.
**Siva Guruvareddiar** 43:32 I have some customers, like, maybe I'll kind of come back on that. And then, just one last question, Dan. The three proposals you mentioned, like, you know, I think the ones that Alex and myself, we are working, that counts as two, and then we still have one more Proposal waiting? Is that right?
**Dan Gomez Blanco** 43:49 For Blueprints, or for reference implementation?
**Siva Guruvareddiar** 43:52 Blue, blue, Blueprint.
**Dan Gomez Blanco** 43:54 For Blueprints, we have a few, actually. We have one for host monitoring.
And that was the original one. I think we're going a bit more in detail, I'm assuming, and getting into the injector stuff, I think that was… things that they packaging SAG could probably… I think probably could take in a bit… Level down from, from… the blueprint that Lukasz wrote.
Right. Which is more, like, about, like, high-level, non-Kubernetes environments to… host monitoring.
There is a… there was another one for… what was there, like… Actually, we should probably create a project for this. As in, like, a board, a GitHub board for this.
Is he… Let me share my screen.
My brains.
Actually, yeah, at some point, this is, like, because, Lukasz has been working on the labeling, It's, Yeah, it's actually a lot easier to see this. We could put it in a… in a board and then see which ones are in progress or in review.
So yeah, so we've got Kubernetes, we've got host infrastructure monitoring, I was unsure about this one.
And how that… Mmm…
**Lukasz Ciukaj (Splunk Inc.)** 45:33 Yeah, I believe I commented on that, but there was no response from the… You did.
**Dan Gomez Blanco** 45:39 June the 4th. Right, I think, you know…
**Lukasz Ciukaj (Splunk Inc.)** 45:41 outdoor, so I can follow up on this if that is still something that… The author wants to continue working on.
**Dan Gomez Blanco** 45:49 I don't think we need… I don't think we need the… so maybe, yeah, maybe it would be a good idea to… to reach out. One of the things that we do in the… in the spec repo is that we add a label at some point when, like, you know, now it's in review, fine, but, like, we change that… Has been reviewed, in a way.
And, we changed that now to… well, we changed that to, like, needs author.
feedback, or something like that, right? Maybe that's another… Almost like to say, if it has stayed in… because then what you can do is, like.
You can have a… stale type of deal, right? Would you say, like, if it has been and needs author feedback for a month, and they've not responded, then we'll close it. Or mark it as stale, basically, and then close it later.
But yeah, for… I don't think we need that, because we don't have that many, but if we… if we get to the point where we have a lot of issues, then we may consider doing that.
**Lukasz Ciukaj (Splunk Inc.)** 46:46 Yep.
**Dan Gomez Blanco** 46:47 These are all those that I created that I don't have the bandwidth to follow up on… to do now, but, like, if someone wants to pick them up, it'd be more than… Which are related to… these were, like, in the first Blueprint that I wrote, I called out certain things where I think it would just need another blueprint for that. First one being, like, semconf governance, and validation, and telemetry contracts, and things where, like, you would put Weaver, and schemas, and… And how to basically, this would be a really good one, I think, if anyone wants to work on this.
**Alexandre Ferreira** 47:21 I would… Can you, can you get me the, the, the link of the… the one? Coincidentally, I'm working on something versus… oh, it's the 332, okay, I'll pull this up here.
Nice, thank you.
**Dan Gomez Blanco** 47:38 Oh, 332, yeah.
Compliance and audit data, I think this is another one related to, yeah, I guess, organizations that are subject to, like, SOCs, PCI, DSS, Audit Login, HIPAA, and whatnot.
Which will have their own… requirements. What I wanted to get into here is more of a… I wanted to get into a bit more of, I guess, relying… reliable data, reliable pipelines, which is not in the original managed telemetry one.
basically saying, hey, you might drop some daytime, but that's okay. Well, it's not okay here, perhaps.
And there's one a bit more about privacy, so… I think it would be good as well for… how to… Work on redacting… Encryption, reduction.
blah blah blah.
Meet these two, maybe? I don't know. I think they… I'm not convinced that they're not… That they couldn't be done in the same. I just think that one single one may be to… Too white.
And I think they're two different things.
**Alexandre Ferreira** 48:49 Yeah, so, I think 334 and 333 should… could be the same one, but then, the SIMCOM governance could be a separate one. Yeah. Because, those two on data governance relates to, like, PCI, box and all that, and the CENCOM governance could be applied to company-specific governance, like, hey, you should have this customer ID label, and every telemetry should have it, so,
**Dan Gomez Blanco** 49:21 have a look at them, see, you know, because I think the challenges are not exactly the same, right? If we think about this as, like, this one is, like, no delivery, no delivery… Guarantees and mixed reliability requirements.
For shared pipelines, no durable buffering, all those things. And this one is more about… PII.
Unity… Authentication and encryption between pipeline layers.
Tenant isolation, like, This is slightly different, but yeah.
I… I don't know.
**Alexandre Ferreira** 49:58 I'll take a look.
**Dan Gomez Blanco** 49:59 Yeah, take a look. And this one is not… and this one is someone that, This is coming from an intern, I think.
that Tiffany was working with.
For one of her internships.
from the Renoch Foundation.
I don't know what the state is of this, but I think this would be quite… Good, as well.
I've started to put together some notes here, which I've not been able to… go through.
I see that Tiffany.
has already.
The idea of this one is related to, having a good story about Prometheus… ingesting Prometheus metrics, basically.
From the SDK layer, to the collector, to exporting, which is… I guess, in a way, related to… this is why I didn't really want you to get into too much detail on the Prometheus stuff, in your… Blueprint as well, Alex?
**Alexandre Ferreira** 51:03 Yikes.
**Dan Gomez Blanco** 51:04 And the core components that are… that you need to… because ultimately, that is like, okay, you know.
for CoreDNX, or for CEDA, you're gonna need Prometheus metrics, but… this Blueprint does not cover that for that… you know, you can… if you want to call it out there, as in, like, in your blueprint as well, and say, hey, I don't… this is… I'm not gonna cover here how to properly do Prometheus, Like, monitoring, there's other things that you may want to… Although…
**Alexandre Ferreira** 51:35 Who knows?
**Dan Gomez Blanco** 51:35 strains, and… And that would be a separate Blueprint, right? That might be it.
**Alexandre Ferreira** 51:39 But, that's specifically for non-Kubernetes environments, right?
**Dan Gomez Blanco** 51:44 Well, it's not specific to non-Kubernetes environments, I think. Oh, yeah, no, it is, actually. You're right. Okay.
Well, then… Yeah, fine.
But there will be some things that are related, right, I think.
**Alexandre Ferreira** 51:56 Yeah, alright, I can take a look into this as well, because in Kubernetes, you will have the target allocator to distribute scrapes, but then in non-Kubernetes, you would have to use, like, a premature cluster or something.
**Dan Gomez Blanco** 52:09 Bimp, bimp.
Yep.
**Alexandre Ferreira** 52:13 Alright.
**Dan Gomez Blanco** 52:15 Very good. Okay, any other topics?
**Lukasz Ciukaj (Splunk Inc.)** 52:21 Nothing from my side.
**Dan Gomez Blanco** 52:23 Yep.
**Alexandre Ferreira** 52:23 H.
**Siva Guruvareddiar** 52:25 You know, Tim.
**Dan Gomez Blanco** 52:26 Well, thank you all. Oh, one last thing. I did. I did have one last thing.
If we have 5 minutes, because, like, why not?
I was… I mean, I don't know if anybody else has been struggling or had that problem with seeing… mermaid diagrams on the OTel website.
I guess not. So if you open any of the Blueprints, M… You… do you have… did anyone have any?
Any issues?
**Lukasz Ciukaj (Splunk Inc.)** 53:06 Again, what was the cushion done?
**Dan Gomez Blanco** 53:09 So, Amy's fitness, and I'll explain this… So, if I open… Alright, so if I open any of the Blueprints, for example.
This one has a bunch of diagrams, right? That now render well, like mermaid diagrams.
If you go into here… Like, do the diagrams render for you, basically? That's what I'm asking.
**Lukasz Ciukaj (Splunk Inc.)** 53:42 We didn't see any issues with that, to be honest.
**Dan Gomez Blanco** 53:45 Right.
**Siva Guruvareddiar** 53:46 I also don't see any issues.
**Dan Gomez Blanco** 53:49 Right? Because for days, it wasn't rendering for me, and I think I entered a weird condition with this, and this is why I think it's a fun thing to discuss, because I think that it's, like, it's been fixed now, but yeah. So, if you see here, I was looking at, every time that I loaded a Blueprint, and this happened for at least a couple of weeks.
I would get the initial request to Mermaid going to, like, MermaMate at latest, as in, like, basically not pinning the version.
So, that, basically, would… so this request here.
We'll download the initial JavaScript module, and then that imports different submodules, which then get all the different chunks.
of, of data, right?
So, all those, I was getting 404 for all those. And actually, doing a query, I would see that I was getting this fail to fetch version info for NPM. This is from… JSDeliver.net, which has a CDN that is used M.
Now, I was thinking, what is that used? And basically, with a bit of, of course, a bit of clod, as well, helping here. But, It turns out that is the… the docs… Doxy is the… I guess is how the website is built, with HugoDocs. It uses HugoDocs, and… And that under… the underlying framework is DOXI.
And, it actually… M… Has, by default.
It uses the latest version of… mermaid.
So I think something must have happened here.
Which is that, I don't know, somehow, I was getting the version… That, and that works, but all the imports we get in 404s.
So I just opened a… draft PR here, too.
To basically pen the version of Mermaid.
So we're not… I guess it's a good practice in general, not to have things on latest, and have a pinned version.
Of libraries, so, yeah.
I was having that weird issue on this, and it's… and one thing that I found out.
is that this website, which is used by Hugo Dogs to get mermaid from.
I'm not a… I'm not a front-end developer, so I don't know if this is, like, useful, like, normal or not.
But I have worked with CDNs in the past, and I don't think this is too normal, that anyone can actually purge a particular URL.
And then, yeah, I just purchased the cash, and it started working.
There you go. For all those URLs.
So, it's fixed.
**Siva Guruvareddiar** 56:35 It's interesting. I never see that. Thanks for sharing.
**Dan Gomez Blanco** 56:38 I just… I just thought it was, like, a weird thing. We're like.
**Siva Guruvareddiar** 56:40 Yeah.
**Dan Gomez Blanco** 56:42 It must have been, like, a race condition on a particular… and I was telling all the people, like, can you go and check if this works for you? And it was working, but I was changing laptops, I was on the VPN, outside the VPN, and it doesn't really… you know, it didn't really affect the… the thing that I was seeing, so I must have been, like.
put into a particular CDN, like, point of presence, or something like that, where that was happening there, but it wasn't happening for others, so… Weird. But it's fixed now.
So yeah, there you go.
Cool. Alright, we'll have mermaid diagrams now.
But yeah, I think we've got a few actions to follow up on, and thanks, Eva, for sharing that.
Appreciate that.
And thanks all.
**Siva Guruvareddiar** 57:29 Cool, thanks, Dan. I will work on the next steps. Thank you.
**Lukasz Ciukaj (Splunk Inc.)** 57:32 Anything. Have a good one, thank you.
**Siva Guruvareddiar** 57:34 Thank you, everybody. Bye.
**Joe Josue** 57:36 Thanks, Roy.
