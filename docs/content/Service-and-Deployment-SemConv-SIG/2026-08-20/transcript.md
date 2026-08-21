SIG: Service and Deployment SemConv SIG
Date: 2026-08-20
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Ayushi Asthana** 02:07 Hello?
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 02:09 Hi, Ayush.
**Ayushi Asthana** 02:12 Hey, hi, Ayushi.
It's been away.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 02:16 It's been a while.
So I need to take a look at, look at your… The… your proposal.
The ninja.
**Ayushi Asthana** 02:28 The data…
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 02:29 Yeah, new changes.
**Ayushi Asthana** 02:33 Yeah, the data classification thing, right?
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 02:36 Yeah, yeah, yeah.
**Ayushi Asthana** 02:38 Yeah. Yeah, I went through your comments, and I think the nomenclature thing has been called out in the working group meeting also. So, I was already talking to the folks over here.
at Google, the DataPlex team and such, what they thought about the nomenclature. So, that conversation is underway, but our PMs had advised us to go with data classification, so that's what we… I might, like, redo the proposal.
Have data, classifications, you know, just data.
So that part, I understood.
But the rest of the things, I might have to, like, redo parts of it, as suggested by your comments, but… So over there, I think I would have to get back to you, either on the doc or in the next call.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 03:30 Yeah, I really appreciate it. Yeah, well, so I commented from my employee's point of view, like, and it's really conservative… my comments were really conservative comments, so, Yeah, so that… that was only…
**Ayushi Asthana** 03:47 So, the…
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 03:48 The reason why I left those comments is… I just wanted to add the different perspective.
on the, on the dock. So… I don't think you… no, we can… we can… Change the older thing to meet my questions.
But at least I appreciate if you… You are able to, like, consider the… those kind of point of view in a… in a spec.
So, that's the thing I just wanted to call out.
**Ayushi Asthana** 04:23 Yeah, I think, I think you were not in that meeting, but I met with the semantics working group also, some time back, and I think being conservative might be… Because, we don't want to make it overly broad. That was the general consensus.
We don't want it to be too broad, or too ambitious, and we become The gatekeepers for something that we don't really understand or can't control, right?
So I think I sort of resonate with that sentiment, at least. That it's good to be conservative, we can always, like, you know, broaden the scope, but it's harder to restrict it, especially in open source. That's why I get that part.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 05:15 Yeah, so thank you for the considerations, and then as for all the, like, communication with the other relevant teams.
I will go through the new updates on the GitHub request, and then we'll give you… Some comments, if, if they're… if there are… So, yeah, so that's the thing I just… I have right now.
**Ayushi Asthana** 05:43 I think there was one, other thing that I might, like, go ahead and propose today.
would be, I think we spoke about it briefly, about stabilizing the criticality attribute.
And then sylvis… So, service.criticalities right now in development? No, it's an alpha stage right now.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 06:08 Huh? Right.
**Ayushi Asthana** 06:09 would like to see it stayed. Yeah, so I think I was not able to get a very good sense of what the process looks like for stabilization, really.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 06:20 I see.
**Ayushi Asthana** 06:21 Because there is no, like, there's no opinions against it, but also, like, there is no other… there is, like, just no noise around it, so I…
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 06:33 So, do you want me to put some up on a PR, or… So do you want to have an explicit, explicit agreement from others on the PR?
**Ayushi Asthana** 06:45 Yeah, I think that that would be helpful. There's already a proposal out for stabilizing, and it has some plus ones also, I think.
But, yeah, the only concerns were, why are we doing this? So I can raise a PR, and let's go with raising a PR first, and then see if anybody disagrees. Yeah, that's the approach that Josh suggested, just regularly.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 07:14 I searched it on GitHub right now, and I couldn't find it, so I just realized that the PR is not yet, so I looked.
**Ayushi Asthana** 07:24 Gotcha.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 07:24 I look forward to it.
**Ayushi Asthana** 07:28 Yeah, okay. So that was the main concern. We have a proposal out, and, but we don't have a PR yet, so let's… I'll do that. I'll raise the PR, and then we'll see if, like, there is, like, any, explicit disagreements.
If not, then you can go ahead with stabilizing it.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 07:49 Yeah, I do.
**Ayushi Asthana** 07:50 We have… I think, the dem… More and everything already in place for this attribute.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 07:59 So good, yeah.
**Ayushi Asthana** 08:00 These are the two things. I've shared a PR on the thread for cost center, also. Maybe take a look at that.
separate, like, offline.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 08:09 Yeah, I'm looking at.
**Ayushi Asthana** 08:10 I think there has been some discussion about it before.
Okay, okay, yeah, that's good.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 08:15 Yeah.
**Ayushi Asthana** 08:16 So, yeah, I think that… Those are the only things that are open right now, from my side at least.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 08:25 I see.
**Ayushi Asthana** 08:26 Good.
Okay, cool. So, I will share the PR for criticality with you, by…
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 08:38 Yeah, let me know, please let me know.
**Ayushi Asthana** 08:41 Yeah, sure, sure. Thank you.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 08:43 Alright.
Have a good day.
**Ayushi Asthana** 08:46 Yeah, you too. Have a good day. Bye.
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 08:48 Have I…
