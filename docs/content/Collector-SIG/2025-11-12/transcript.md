SIG: Collector SIG
Date: 2025-11-12
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 02:53 Hey.
I think we can get started.
**Pankaj Kumar** 04:49 Yes.
Hi everyone, this is Pangas from Sumo Logic.
So, I have quite the issue regarding Addition of a feature in, one of the receivers called Windows Event Log Receive, right?
So the problem we are trying to solve is, basically, we want to collect the Windows security events.
For a particular domain, for all domain controllers that are present in that domain, right?
And the solution that we have devised for that is that one solution that we can install the collector on each domain controller machine, locally, and collect the security event from there. But we also want to give customer the support for remote collection, right? So, what we are proposing is basically Based on our flag that user controls, we auto-discover all the domain controller in a particular domain.
Which is, like, quite feasible using LDAP query or the Windows Event API that Windows provides.
And then dynamically create the underlying connection input object for each domain controller.
And, thing I'm looking here is for the input and the feedback.
Like, what are the blockers, and what we can do next?
**Pablo Baeyens** 06:20 Okay, thank you. So I don't think we have… Either of the code owners here?
I think it would be good if you can… Talk to them.
Since the issue was created yesterday, maybe they haven't had time to look into it, but if not, you can… reach out on the CMCF slot.
My first thought, and I'm not a I don't have a lot of knowledge about Windows, is we have a… component called a receiver creator.
Let me share the link on the Zoom chat.
There you go. And so the receiver creator uses observers.
Which… the link is here. I can put all of this in a comment.
To discover things, like, hosts, or, kubernetes boards, stuff like that.
And it will create receivers based on those. So I wonder if it's better to… Try to implement this on the receiver creator instead of implementing it on the… this specific component, on the Windows Event Clock component. I… but as I said, I don't have, enough context on this to answer. I don't know if anybody else on the call has, but if not, you can reach out on the CNCF Slack.
To the code owners after you've waited, like, you know, give them a couple of days, and then you can reach out to… For example, to Paolo, to… Okay.
**Pankaj Kumar** 08:15 I will look into the component that you have provided, if we can use it, and if we can, how we can use it. Just one more thing on which Slack channel of CNCF I should post this, if I want.
**Pablo Baeyens** 08:27 So you can reach out via DM, or if you want to make the conversation more public, you can reach out on AutoCollectorDemp, which is for development of new collector features.
**Pankaj Kumar** 08:37 Okay, got it. And this is the right meeting, right? If code owners want to have a meeting, this is the right forum, right?
**Pablo Baeyens** 08:44 Right, yeah, that would be the right place to discuss it, yep.
**Pankaj Kumar** 08:48 Okay, thank you.
**Jagan** 08:54 Hello everyone, maybe I can go next.
So, I'm Jagann from SumoLogic.
So, we are looking for a feature, basically, to enrich logs with the DNS data.
like, some, basically, some IP address or some domain would be present in logs. We would like to, basically, interested in a feature, to reverse DNS lookup, or a forward DNS lookup.
on this data from these logs. Looked at the similar issues reported with the DNS lookup processor, specifically. That is an accepted component. When I… I was planning to implement that.
in the skeleton which is raised for the DNS lookup processor, I saw there is another processor which is being proposed, enrichment processor, which handles the… which basically provides this functionality in an abstract way.
with, basically DNS lookup as a separate extension, and, there will be a lookup processor, which uses this extension to do a different type of lookups, like memcached, like, the component may be vary, but, how it will be implemented in its… in the extension.
Yeah, but this component, I think it is not accepted yet.
So, I think Zhao is also here. We are looking for sponsors for this component, or how to proceed with this. We are happy to help with the implementation, but we just need the framework or, base framework to start working on.
**João Duarte** 10:29 Yeah, hi. Yeah, I'm the creator of that proposal. Just a question, is the… there is, like, a DNS lookup processor in Contrib right now?
Is that useful at all?
**Jagan** 10:41 No. I think in the proposal of DNS Looker processor itself, I asked whether we can start contributing it, it's just a skeleton, but the person who has been proposed that processor mentioned that, she's kept it on hold, because there is a new processor which handles it In an abstract way, supporting multiple types of… types of lookups.
So she… so that is whole, that is on hold.
No one is working on it.
**João Duarte** 11:10 Yeah, for the Richmond processor, I mean, we brought it a few times already to the SIG meetings, typically in the US one.
I was attending this one, I was not planning to, again, nag people about it, but it is a very voted issue. We're still looking for sponsor, sponsorship, and there's there's a couple of people from Elastic also in the KubeCon US, seeing if there's anyone interested there that could sponsor. We could sponsor it internally at Elastic, but… I mentioned this in the issue, I think this is a critical component, or a component that is big enough that we would like to have other people and other vendors also part of this initiative, and not just be only Elastic.
So yeah, still trying to get… folks interested in it, so happy to have discussions about it, get feedback. We got pretty much three pieces of feedback so far. One of them was to use extensions as a way to augment the set of possible sources for enrichment.
The other one was to use the functional interfaces, a proposal from Josh from Microsoft, I believe, and the third piece of… Feedback was to use, see if we could use the entity model as a basis for The enrichment that we do.
And that's the thing that I'm doing right now, is adapting the scalp and PR to at least see how much we can use of NDT model. I'm learning about it myself.
As I go. So yeah, that's the only thing that I can… present so far. So yeah, if anyone is interested in it, or knows someone that maybe Happy to talk on Slack or anywhere else.
**Pablo Baeyens** 12:57 Wait.
**Jagan** 12:59 Let me speak.
**Pablo Baeyens** 13:00 Yeah, thank you, I think I already mentioned that. I don't feel like I have the bandwidth to sponsor it myself, but yeah, like, it seems like a good… Component, and, well… As I mentioned.
I think last week, we may be looking into changing the rules for accepting new components and making it a bit more… Restrictive, just because, well, we want to to focus on stability right now. But, yeah, if you find a sponsor, like, that's… you know.
**João Duarte** 13:35 Yeah, I think this is… Sorry, go ahead.
**Pablo Baeyens** 13:39 No, I was just gonna say, like, if you find a sponsor, this clearly covers our use case that the community wants, and, like, it seems… it makes sense to me, too.
**João Duarte** 13:47 Okay.
**Pablo Baeyens** 13:48 Go ahead.
**João Duarte** 13:48 Yeah, what I was gonna say is that I think that the new rules would probably help here, because we could have the two sponsors, and we could have one sponsor internally from Elastic that does a lot of the heavy lifting of the reviews, but still have someone that can counsel and can be, like, an adversarial, you know, a good way.
To the proposal and to the PR, so it kind of offloads a lot of the responsibility of this single, Sponsor. So if anyone is interested, they will not be the only ones who could actually have this thing shared, this effort shared.
Maybe that helps someone take photos.
**Pablo Baeyens** 14:30 Yep. I… I'm not sure when I will continue working on the change in sponsorship rules, but if you're interested in, like, rewriting those.
Happy to get any help.
**João Duarte** 14:48 Oh, okay, good, got it. I'll review, for sure.
**Bejal Lewis** 15:01 I have the next subject, so I can go next if there's… if there's nothing else.
**Jagan** 15:08 Yeah, yeah, you can go next.
**Bejal Lewis** 15:09 Okay.
Okay. I wanted to… well, first of all, I'm Bijal, working at Grafana Labs. This is my first time in this collector sig, by the way, so it's nice to meet everyone.
And I wanted to follow up on… On a feature request, this is from maybe a month ago.
I think it's kind of interesting to discuss, and I was hoping to get maybe a bit more of a temperature check on it.
But it's regarding end-to-end acceptance testing, kind of like a black box style approach, where we could… Perhaps have some kind of framework that is testing data being emitted, or telemetry emitted from applications to a collector, and then to the back end.
Making sure that the flow works as a whole, and the data gets to the backend, as you would expect.
There's one issue linked there, which I think is quite interesting.
Where, at Grafana, we actually had an incident because of, a bump inversion in the collector.
Which… Was essentially making sure it was only accepting valid data.
And there was an existing out-of-spec bug in the .NET SDK that was sending invalid data.
And so this bump in the collector actually broke that integration. So the .NET SDK was sending data, and the collector was rejecting it after that bump.
And it wasn't super intuitive why it was breaking until looking into it after.
And some of the comments are saying that we could improve testing on the .NET SDK level, and I don't disagree.
But I'm wondering if there's also a need to have a higher level testing framework, because if we're doing specific tests on the SDK level.
Or on the collector level, you're sort of testing for what you already know.
But when you take one step back, and you do a full end-to-end test, you start to catch things that maybe you weren't aware of.
And I'm wondering if perhaps other people have experienced similar issues, or if they feel that A framework like this would be beneficial.
Or if it's not something that the hotel community is currently interested in. So, I'm not sure if this is the right forum to ask this. I could also post in Slack.
But I'm open to discussing that, or getting any other opinions on it.
**Pablo Baeyens** 18:06 From my side, I think the comment from Tom Young is interesting, This one, on whether it should be… on the SDK level, or on the collector level, by… Don't have a strong opinion there. I think it's, like, it's good to have these tests, and we should have them somewhere. I don't have a strong opinion on where, but, like, that's maybe the thing that we should clarify before moving forward.
**Bejal Lewis** 18:42 Yeah. I think, in my opinion, it's sort of… it's almost like a different… a different question, because… when you test something on the SDK level.
You sort of know what you're testing against, and you have an expected output.
But an end-to-end test would be sort of, like.
Testing the relationship between two separate components that are being iterated on separately.
Which, it's, like, another issue, and I guess I wonder, like, even if we… if we do decide to first go ahead with… with improving testing on the SDK level.
If there is gonna be some edge cases that we still can't catch.
Or perhaps if that's something to… to address later, after we improve testing on the SDK level.
**Jade Guiton** 19:33 I think the question wasn't about, whether to do unit testing on the SDK level. It's more, if we're going to do end-to-end testing or integration testing, where should that live? And where…
**Bejal Lewis** 19:43 Who should have?
**Jade Guiton** 19:44 I have the responsibility for it.
And… Obviously, there's gonna be some shared responsibility between the collector and the SDK, But I do agree with Damien that I think it makes more sense to put these tests in the SDK repos, because we can't possibly list all of the SDKs, and it's not even really clear which ones we need to support, like, which ones are official enough, I guess, to be supported. So I think it would make sense if… and maybe we could provide some help with doing that, to… to have, integration tests in the SDK repos.
Maybe we could provide a tool to help doing that?
I don't know.
I guess.
**Bejal Lewis** 20:32 Yeah.
**Jade Guiton** 20:33 The problem with end-to-end testing, like, going all the way to the back end, is that there's many different backends, and they don't work the same way, and they don't all support all of the features of OpenTelemetry, so… The backend would probably end up being, like, the debug exporter.
But we could try to provide some help on how to set up This kind of end-to-end testing.
**Bejal Lewis** 20:57 Yeah.
I think, sorry, Pablo, I misunderstood what you said, but I think that makes sense, when it comes to where to put the tests. I also agree on the back-end point as well, because we have a framework like that at Grafana, but it's pretty specific to our stack.
I think one of the points of the proposal as well is could we adapt what we currently have to be a bit more hotel-native, and maybe reduce the scope a little bit more, so… We have an integration test on the SDK level, perhaps between the SDK and collector.
But not, like, a specified backend, if that's what you mean.
**Douglas Camata** 21:44 But you… but you might need a backend anyway to be sure that things are working right.
But, I agree with Jade and with Damon as well, that In the end, the SDKs… whether we want it or not, what happens is a given SDK is… only supports certain versions of the collector, right? Because sometimes there are changes in Protos, which seems to be what happened.
So, in the end, it, like, an SDK will have to say.
oh, this release X that we have works with collector up to release Y.
And, then collector Y plus 1 had the breaking change, and we released X plus 1.
And it works with that collector version.
**Jade Guiton** 22:42 For the record, I don't think the issue that motivated this was about breaking changes to the protos. Those are… those are happening for profiles, but I think for the rest of the traces, it's mostly stable. I think the issue was just that the parser we started using And the collector became more strict, about what it accepts.
But technically, the proto itself didn't change, it's just a different way of putting it on the wire, I guess.
**Douglas Camata** 23:10 Gotcha.
**Bejal Lewis** 23:14 Yeah.
**Jade Guiton** 23:17 Yeah, I think regarding… Regarding, yeah, the backend, it's… Definitely. I think… I think a complete end-to-end test would be complicated, because there's a lot of different variables. There's the SDK, and then there's the backend you're using, but something that stops at the collector and just… outputs with the debug exporter or something like that. I think that might be enough to ensure that the… SDK is compatible with what the collector accepts.
**Bejal Lewis** 23:53 I agree. That sounds good.
Perhaps, like, as a next step, I could do a little bit of brainstorming on what that could look like, and tack that on to the proposal as it is. And either we can discuss there, or I could bring it back to the next SIG to continue, whichever makes the most sense.
**Jade Guiton** 24:18 I think there could be some value in bringing this to, one of the North America meetings.
Especially if we want to know, like… I'm only aware of this one incident of incompatibility between the SDK and the collector, It's possible that there were others that people are aware of.
Which could, motivate further the proposal.
**Bejal Lewis** 24:42 Yeah.
**Pablo Baeyens** 24:42 I'm personally not aware of any others, that are not related to product changes themselves. There's been, like.
You know, profile breakage, but that was, like, intent data unexpected.
But, yeah, like, maybe somebody else knows about something else.
**Bejal Lewis** 25:02 Cool. Yeah, that sounds good. The feedback is really useful. Thank you.
**Pablo Baeyens** 25:22 Okay, I think it's… my turn, so… This is both to announce that issue, and also to, like, discuss changes on… this meetings organization. So, as you can see on the issue, which I'll post on on the Zoom chat, We, as in the collector approvers and maintainers, have been, working on a roadmap for, marking The components that we think are most important, stable.
So we've used the data from the collector surveys and anecdotal data, Basically, a big spreadsheet to decide on a number of… Key components that we think, are among the most used by, users for across any use case that they have for… for OpenTelemetry.
So you can see the list there, that includes, few receivers, like the Prometheus receiver, or the host metric receiver, and some processors, transform processor and filter processor, which is OTTL, and a couple other processors that enrich the data in some way, the Kubernetes attributes one and the research detection one.
So… We want to focus the community on working on, making sure that these abide by the guidelines that we have for components ability, and prioritize them to be marked stable.
And so, well, I want to take the time first to, like, announce this. I already posted this on Slack, but just so that everybody is aware.
And, secondly, in order to make sure that we focus on this, I would like to… change a bit the way these meetings work so that we have some time at the beginning of each meeting to discuss any PRs and any issues related to Pursuing this goal, like, stabilizing these components.
There is a project board that you can see at the top of the issue. Here's a link. We are still working on it, so… We don't have, we're gonna do it today, but the idea would be to look into say, PRs or issues that are under discussion, at the beginning of each meeting. Yeah, I don't know, like, I'm… interested if… If you have any… Suggestions on how to organize this, how to make sure that we… we focused on this, but still allow, well, the early discussions that we had today, for example, to happen.
I'd be… I'd be happy to hear your feedback, and if you… don't have anything, well, I'll… I'll try and come up with something for next week, probably, so that we… We try it out.
And see how it works.
**João Duarte** 28:39 Why do you see this being… Reviewed across team meetings, across time zones.
Just to try to… trying to avoid, like, duplicated work and stuff like that.
**Pablo Baeyens** 28:52 I mean, so, like, ideally we would work async on GitHub, but, yeah, like, if there are… synchronous discussions that need to happen. This would be brought up to, yeah, any meeting, from any time soon.
**João Duarte** 29:12 I'm always… Plus one on trying a process, and if it doesn't work well, we can adjust.
I think it makes sense to start the meeting, look at this, see if there's anything to discuss. Otherwise, just skip it.
**Pablo Baeyens** 29:29 Okay.
**Douglas Camata** 29:38 Yeah, plus one as well for this. I think it will be great, especially having a board where Maybe.
that we can look at all of the issues that we think are required for the stabilization of the components. We could even Label the ones where… We think, you know, could be some easy first contributions for… for new people, and Kinda say, hey, if you're looking to do your first contribution, we have a few Easy and very useful ones here that you could start with.
I don't know if there will be any, you know, maybe things are complicated, because maybe stabilization work is not that simple, but… we could… Help ourselves and help others.
Start contributing as well.
**Pablo Baeyens** 30:31 Yeah, so, there's a label, Component Stability Phase 1, and yeah, we would… be able to add good first issue to an E.
That makes sense. That's… That's a good idea, yep. I think this is an opportunity for people to… to get more involved if they want to.
Alright, any other comments on this topic, or any other last-minute topic?
Okay.
We can call it an agent. See you on the internet.
**Bejal Lewis** 31:19 Yeah.
