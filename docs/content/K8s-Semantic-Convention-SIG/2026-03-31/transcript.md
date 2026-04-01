SIG: K8s Semantic Convention SIG
Date: 2026-03-31
Duration: 23 minutes
Zoom Recording URL: https://zoom.us/rec/share/ALZ--r1k-aVO01GKLJu4bYTCAnB9jKLnSDQpaceM_YTPi3SS2CaFgu8AGGA7Pr84.JuRSjFH7Clru5nW6
============================================================

## Zoom Recording Transcript

**João Marques Correia** 08:10 Hey, hey Gina, I know pieces won't be attending.
Dave had mentioned he wasn't able to join, so I'm…
**Jina** 08:20 Oh.
**João Marques Correia** 08:21 Yes, there might not be a meeting today.
**Jina** 08:24 Oh, did they post in the Slack channel?
**João Marques Correia** 08:29 Yeah, I know Christos is out, he's on vacation,
**Jina** 08:35 Dimitri is out until, it's either Dimitri or Kristas who drive these meetings, usually.
Okay, I guess… I'm not sure. Since the two of us are here, I guess, do you have, any agenda items specifically?
**João Marques Correia** 08:54 Not from my side, I'm mostly trying to help with the stabilization of Kubernetes metrics. I had a few PRs up, but I think David… already reviewed them. I'm waiting for Christus to be back, before continuing on that side, so… I'm not really stuck, basically just kind of waiting for reviews, but it's because, Christos is out. Not sure if there is anything on your side, or there's something I can…
**Jina** 09:19 Yeah, I just… I have a PR open, which I would like to… Get in, I guess.
**João Marques Correia** 09:29 Okay.
**Jina** 09:30 Yeah, it's a similar situation on my side. I'll just… I guess I'll just add it to the agenda, so that if somebody takes a look at this, they can, remember to look at the PR.
Yeah, but that's about it. Oh, is your PR the one with, With the, the new resizing metrics, like, how do we get the… different, You know, value accumulate might actually set versus what's actually desired.
**João Marques Correia** 09:58 Yes.
**Jina** 09:59 Okay.
**João Marques Correia** 10:00 Yeah, that's the one. It's the… yeah, basically, I had started that for pods, but it seems it's also needed for containers. So, yeah.
just working on that side to try to help stabilize the metrics, but I think we need to first finalize a few things in the semantic conventions, and that is one of them, yeah.
**Jina** 10:19 Okay, alright, yeah, sounds good. I, I did have, like.
a doo-do to take a look at that PR.
Because I'm a little worried, if that's a trick.
All our existing metrics and, you know, what the plan is going to be for users to move.
But yeah, thank you for opening that.
**João Marques Correia** 10:41 Yeah, and should also have any feedback, I totally appreciate it, but I think David went through it. I'm waiting for Chris's, but in the meantime, again, if you have any comments.
it can always help, and if you put any link, I guess, to PR, I can also try to take a look. I'm still getting started, like, I'm just trying to… still getting kind of onboarded and all, but I… Oh, David was able to join, I think.
**Jina** 11:05 No problem. I just added the link for the one for the PR, which I'm trying to get reviews for.
**João Marques Correia** 11:20 Yeah, dude.
**David Ashpole** 11:24 See if this is what I've looked at.
**Jina** 11:27 Hey, David.
**David Ashpole** 11:29 Oh yeah, yeah, I can take a look at this.
**Jina** 11:31 Yeah, the one I have, I think, like… you and Christos took a look at it, the May 3 already approved it. The issue was because I was confused if I want to if I should send a metric which defines the relationship between the persistent volume and the persistent volume claim. For now, I've kind of just, like, removed trying to define that relationship, because, like, I just… I want to see if, like, entities model will support it.
By default somehow. So I'm going to wait a little to, you know, for entities to get there.
For now, I just kept, like, the basic metrics, which I was trying to get from those, storage stuff.
**David Ashpole** 12:22 Well, are there any open discussion points, or just… This still needs… Just needs review, okay.
I will take a look.
**Jina** 12:39 Thank you.
**David Ashpole** 12:58 Alright, is there anything else?
People wanted to discuss here?
**João Marques Correia** 13:02 Don't think so. I think I already reviewed my PR. I think for now, I'm just waiting, basically, for Chris's to be back.
But yeah, I will just be continuing, I think, mostly working on stabilizing the Kubernetes metrics, but yeah, just waiting for Chris's as well to… I'd like to give his feedback.
**Jina** 13:18 I had one question, another PR, which is… About the system containers?
It is .node.systemcontainers, And, like, it looks good. My only real concern there was, The name, like, the identifying attribute for a system container is the name of the container, which is not unique, it's just, like.
Kubelet, or… Something, just a word.
And I wanted to see if we should… we have in the metrics itself, in the semantic convention, you can do entity associations, multiple entity associations.
And I feel like we are not doing that correctly, because, like, we put in caters.pod, but sometimes it is caters.pod and caters.namespace, or something.
So, for this one, right, the entity association is just kdas.node.
system containers, which kind of does… which, by just semantic conventions, you know, how it's defined, it doesn't give you a unique metric.
So I wanted… should stop.
**David Ashpole** 14:27 How entity associations work, are they… is it, like, all the things you need to point at to be identifying?
**Jina** 14:32 I… that's how I… that's how I'm… yeah, I understand it. Okay.
So I wanted to see if we should start adding those correctly, in our, you know, when we are defining now new metrics.
at least for this case, it feels like you cannot just have the, you know, system container name as the attribute. You would have to add the node UID to actually get meaningful MDSs.
**David Ashpole** 15:00 Yeah, yeah.
50.
Copy.
**Jina** 15:17 Yeah, I'll just tag the group where I posted the question, because, like, I don't think it got resolved, even though it was marked resolved.
**David Ashpole** 15:25 I was.
**Jina** 15:27 Yeah.
So if… if anybody has, like, I guess if anybody in the group has, like, any opinions on If this makes sense to start doing now.
Now that Dimitri has, like, a… PR.
for, adding entity support in the KDAS cluster, so you were to, you know.
**David Ashpole** 15:49 Yeah, I was…
**Jina** 16:00 So I tagged the group there, and also linked to the comment where I'm But I would like some feedback.
**David Ashpole** 16:11 Yep.
Okay.
Sounds good. I can take a look.
**Jina** 16:45 I think that's it from my end at least, if either of you have anything on the agenda.
**David Ashpole** 16:53 Nothing for me. I remember we talked at KubeCon last November about a top-level controller.
Is that still something that's on your mind? I had some people ask for it internally.
**Jina** 17:05 Oh, A top-level controller, as in, like, for just a way to define a random custom Resources, how do you send those names?
**David Ashpole** 17:14 Like, a single attribute that has, like, whatever the… Deployment slash stateful set slash…
**Jina** 17:24 Oh, Kate has got something…
**David Ashpole** 17:26 Workload or something, or…
**Jina** 17:28 Yeah, yeah.
it's not defined in the semantic convention, but, I know either through the KRS objects receiver or somewhere, we already send this, the KRS object. Oh, yeah. Yeah.
The issue with that was only that while, you know, you can send this if there is an actual controller which is taking care of a workload, but you can't use this sort of naming for random custom resource objects by themselves.
**David Ashpole** 17:58 So…
**Jina** 17:59 Are there… is this, like, controller only, which, you know, can meaningfully track… be considered a workload, like, manager, versus is it a custom resource, just a random custom resource name, object name, or something?
So, yeah. But either ways, I think, like, we have, we have some usage already of caters.workload, and then we also have some usage of caters.object.
So I think, like, we just have to, like, go look through the existing ones and put it in the semantic convention.
So we don't create too many… I guess he wins.
**David Ashpole** 18:40 Yeah, that would be very good to do. I didn't realize we were already using it.
**Jina** 18:44 Yeah, yeah, the… yeah.
Yeah, and we have some stuff for caterers, even… Which is not really in semantic convention, which might be useful here.
**David Ashpole** 18:57 I see, but the events receiver is not one of the ones that's marked for, like, the first round of collector stability, right?
**Jina** 19:03 Yeah, neither is the opposite, but I think we only, we're only looking at the… Is that in the kibleit status receiver, right?
**David Ashpole** 19:13 Yeah.
Alright, I think we should call it.
Thanks for joining.
I'll see you guys, in 2 weeks.
**Jina** 19:25 Yeah. Thank you.
**João Marques Correia** 19:27 Jim?
