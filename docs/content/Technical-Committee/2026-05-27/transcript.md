SIG: Technical Committee
Date: 2026-05-27
Duration: 22 minutes
Zoom Recording URL: https://zoom.us/rec/share/O_H_vJrhPDJUornn3M9IYnLNx9ikRnYFM9Sbfwg9ULL_GMEpLg2aJYFPf7C5Gnw.Kfwls5S0lVh95ogn
============================================================

## Zoom Recording Transcript

**Reiley** 01:17 Hey, Tiger.
**Tigran Najaryan** 01:24 Anyway, just trying to edit the document. For some reason, I still don't have edit permissions.
**Reiley** 02:07 But I use your spunk email, or another email?
**Tigran Najaryan** 02:13 Sorry, say that again?
**Reiley** 02:14 Should I use your Splunk.com email, or another email?
**Tigran Najaryan** 02:19 No, I think it should be my personal email, and let me, let me try it again.
I'm gonna ask for a minute.
I don't know who is the owner, but… Let me request from my personal email. We no longer have Google accounts here at Splunk.
they eliminated them completely, so I can only use my personal account.
**Reiley** 02:41 I see.
Or you can put your email on the TC Slack channel, I'll add you now. I also noticed we still have Yuri there as the owner.
Yeah, not me.
**Tigran Najaryan** 03:09 do that. Thank you.
Okay, so this is emptying… Community Team inbox.
So this one, ted and I both, we replied to it, and I don't know if there's anything else that we're supposed to do here as a TC.
**Armin (Dynatrace)** 03:54 It looks like the governance committee is also looking into it from Ted's response, right? I think he's writing on behalf of the GC there, if I'm not mistaken.
**Tigran Najaryan** 04:06 Sorry, say that again?
**Armin (Dynatrace)** 04:08 I think that Ted is writing on behalf of the GC there, right?
**Tigran Najaryan** 04:13 I think so, yes. Anyway, both he and I, we replied to it. I think now… I can sync with Ted. It seems like we should just maybe say we're rejecting this, or they have to rework this substantially, if we want to accept it. I'll sync with him. I don't think there's anything else that we need to do here as a TC.
Don't know if we need to relabel it in some specific way.
Maybe let's keep it as it is, I'll sit… I'll talk to Ted, and we'll decide how we want to go ahead with that.
**Armin (Dynatrace)** 04:48 Yeah, sounds good. Thank you.
**Tigran Najaryan** 04:49 The other one is his proposal. This is Ted's proposal, right?
What do you mean?
Anything that we should discuss for this one?
We had it… We had it in the spec call yesterday and the week before, I think.
And it's labeled as a PC inbox.
Do we want to make any calls on this one?
I think we're good with the idea of having it.
what may still need to be discussed is the… the precise scope of the project, I think, may need to be defined, but that's okay.
we, I think when it lends into the TC inbox.
maybe the call that we need to make is whether we're fine with having the project or no, and in my opinion, I'm personally fine. So maybe that's what we decide here. If we as a TC are okay with it, we just mark it as is.
Does that work?
What are the labels that we have here normally?
OTC reviewed… What else?
That's the only two things, inbox and reviewed. Okay.
So, I guess as the next step, we could keep this open until we actually do that review.
And then we'll mark it as reviewed, and we can go ahead with it, unless we think we shouldn't be accepting it. If anybody thinks so, maybe we can talk about it now.
**Reiley** 06:42 I reviewed, and I have some outstanding concerns. I… like, I look at Kubernetes. Kubernetes, like, if you search, when did Kubernetes announce GA? The answer is never. Like, they don't even have a Kubernetes GA concept if… If I'm not totally wrong. And when you look at Kubernetes GA announcement, they made probably, like, 2030 announcement, and each one is about an important feature, like some, like, dynamic resource upgrade or something. So.
I… I feel like open telemetry as a product, or umbrella, general availability is very confusing.
And I out of the water against that.
So my position is OpenTelemetry as a product should never announce GA.
individual feature announced GA, and individual feature, there could be a spec level. We can see the spec level has a stable version, and we shouldn't collect general availability, because nobody can just use a spec and be done, right? So, general availability must happen for a feature, and must happen for a set of components.
It cannot.
**Tigran Najaryan** 07:49 And that's what Kubernetes does as well, right? I think if you go to Kubernetes documentation, that's exactly what you see. There's a feature described…
**Reiley** 07:56 Exactly.
**Tigran Najaryan** 07:56 It's labeled as whether it's stable or better, or whatever it is.
**Reiley** 07:59 Yeah, yeah, so I think the intention here is good, but, like, whenever her general availability for open telemetry, that's already super confusing, and… And I want us to avoid that, like, just stop doing that. So, the stability can happen on the spec or a component, but the general availability should only happen on a component, like a software artifact that we ship.
And feature. And then, I think we have a mixture, so we might have a component, that version is 0.2, and if you look at OpenTelemetry Lost and OpenTelemetry Collector, I think both of them have the same situation. Their version is 0-point something, but they tell the user, hey, we have at least, like, 3 features that are already stable, and you should use that in production. Which is… confusing. I think that that's where some users got frustrated, so my suggestion would be If you have a component that's zero point something, you should never tell anyone to use that in production.
Like, you should always move it to 1.0, 2.0, like, 2.3, something like that. The major version needs to be a non-zero thing. And then, in that non-zero, like, version, like, major version.
you might have many different features. There will be features that are already stable, and you implement that, and you guarantee the backward compatibility, you think that's production ready, then that feature like, people should rely on it by default, because you declare 1.0 or 2.0. And if you have an experimental feature that's still, like, evolving, either the spec is not ready.
Or, even the spec is ready, you're still polishing that, then you should explicitly set those as experimental things. So, you need… you need to ask for explicit opting.
**Tigran Najaryan** 09:48 Okay. I think I agree with you, what you're saying about the GA labeling of the entire project. One thing that we'll still want to address is that when we graduated CNCF, Made some explicit requests.
that we need to address one way or another, right? So, I think what we probably need to do is figure out what exactly is that the CNCF was looking for.
and address specifically that, at least that… I think that needs to happen either way, even if we decide that we don't necessarily want to have OpenTelemetry GA as a whole. They are looking for stability of certain elements of it, like the collector and things like that, which to me also doesn't make sense. If we're called a graduated project.
then the fundamental, important elements of it do need to be. They need to meet the certain stability bar.
So, maybe that's what we need to focus on, and there's no need maybe to call the entire project GA, but rather say this is what we're doing to address the concerns that the CNCF had.
For the graduation process.
And it's… I don't think it's going to be fundamentally very different than what Ted is already aiming for. It may be… maybe the scope will be slightly different. I would prefer, and I said that yesterday in the spec call, that we try to reduce the scope as opposed to bring more I don't remember what was the thing that he wanted to add. So, can we focus maybe on that? So, the CNCF asks for this, and we're doing that to address those asks for graduation purposes.
Does that make sense?
**Reiley** 11:40 Yes to me.
**Tigran Najaryan** 11:43 Okay.
I think we can chat with Fed. He should be on board with that as well. I think that the reason he's doing this is also because of what CNCF wanted to do for graduation, so the goals are going to be no different. It's about the details of the scope, essentially.
And the labeling, I agree with you, it's going to be confusing to call the entire thing GA when it has multiple diverse components of different maturity level, and we'll always have those.
Okay, cool. Maybe let's have that chat in the TCGC channel.
And we'll decide what we want to do about it, and maybe comment on the PR as well.
**Reiley** 12:29 Yep.
**Tigran Najaryan** 12:31 So, I'm gonna keep it at that same state. I don't think we need to do anything about it. Let's do the unassigned PRs.
This is a draft.
The swampy.
**jmacdonald** 12:55 all the Prometheus ones are pretty straightforward. I… I would go… Click those as for my… for us.
**Tigran Najaryan** 13:03 Do you… do you want to take those?
**jmacdonald** 13:05 I will, I will take those, yes.
**Tigran Najaryan** 13:08 Okay.
Why is it so slow?
**jmacdonald** 13:23 Could have to do with growth at GitHub.
**Tigran Najaryan** 13:26 Yeah.
Jason, and I can take this.
This one is also Prometheus.
You wanna take that, too?
**jmacdonald** 13:39 Yes, yep, I'd be glad to.
**Tigran Najaryan** 13:51 Okay… Don't lose it.
What's remaining?
Maintenance, that's fine… the old tip.
Okay.
Who wants to pick this?
This is, I think, a continuation, we discussed it yesterday in the spec call, a continuation of the process context, the recently added proto.
**Reiley** 14:20 Yeah, assigned to me.
**jmacdonald** 14:23 I've been reading the PR, I just am not finished yet.
**Carlos Alberto Cortez** 14:27 Also, I think that the, the… the group, the related group, because, correct me if I'm wrong, but this… it comes to, eBPF, they should review this.
And come to an agreement before we can, like, ask everybody just to review this one.
**Tigran Najaryan** 14:44 Okay, sounds good. I think we're done with our maintenance issues, we don't need assignees for those.
Okay.
We're good. This is… Dom, dung, and done.
Okay, sounds like we have the private topic. Anything non-private to discuss here?
**Reiley** 15:06 Oh, I have a quick question related to the security version bumps, like, a lot of, like, GitHub actions, those things. I think in Microsoft, like, we have some… some product that try to enable automatic PR approval. So this is, like… I know in OpenTelemetry, you have the last, like, defense line that, like, we always require some human approval. I wonder if you see a similar trend, and what do you think?
Like, do you think at some moment, maybe we'll just say, hey, let's just enable this auto-merge for this type of PR, like GitHub action?
I mean, if there's a URL check or something, I don't want to review that PR, because what I'm doing is I'll just look at, oh, this is just, like, bump… bumping the action for a URL check or, like, lint or something, and I don't even click the link to see the history and what's the actual change. I just trust It's not a big deal, but when it comes to it, update this underlying HTTP library or something, I'll spend more energy on it, so…
**Tigran Najaryan** 16:10 That's interesting, by the way, for repos which do not contain code, like specification repo, it's even less… like, there's no risk, like, you're not releasing any code from that, right? So it's, like, the tools that are checking links and stuff like that.
The risk is very, very low that something can go wrong there, right?
**Reiley** 16:32 Yeah.
**Tigran Najaryan** 16:33 So, I think I'm fine with having auto-merge enabled for those types of repositories for updating dependencies. Is there a way to do that? Like, you can configure somehow, renovate both? Yeah.
**Reiley** 16:45 I know how to do it in Microsoft, but I don't know how to do it in CNCF, so I'll check, but I probably will start as the Sikh security part, because in Sikh security, my goal is we only keep the guidance doc and those things. I don't release any artifact from it, so it's like…
**Tigran Najaryan** 17:02 Yeah, yeah, and yeah, that's…
**Reiley** 17:04 Also, I'.
**Tigran Najaryan** 17:05 Yeah. Yeah.
**Reiley** 17:05 Also, I'm… I'm the only, like, the… the project maintainer for now. I, like, Jeremy's, is, stepping back, so… I feel…
**Tigran Najaryan** 17:17 I'm fine with that, with what you're suggesting, especially for the repositories, which are basically just documents. The worst that probably can go wrong there is that the bot is, I guess, compromised, and it corrupts the docs, and we'll just notice it, we'll see it, right? It's not… it's hard to go unnoticed. We'll fix it if something like that happens. With code, it's a bit, I guess, easier if… there is actually a compromise port, and it changes the code, and you don't see it. It's possible, I would be more cautious there.
**Reiley** 17:52 Yeah, we should be more careful there. Okay, so… so I'll try to make myself a little bit lazier, and then I'll report back and see if we can do the same for the SPAC, and maybe even the Proto repo.
Okay, thank you.
Let's switch to a private column.
**Tigran Najaryan** 18:09 Okay, let's go there.
