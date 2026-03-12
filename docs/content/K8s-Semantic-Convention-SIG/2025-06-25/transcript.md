SIG: K8s Semantic Convention SIG
Date: 2025-06-25
Duration: 12 minutes
Zoom Recording URL: https://zoom.us/rec/share/8AQbVWkeyUMJQkmkKxjdFtasFJON3OsuGJ6hLHm0A9iHJgvQMBGIdpJD1ByW1T8m.sijGJeml3kZRsk1D
============================================================

## Zoom Recording Transcript

**Christos Markou** 02:16 Hey, folks? If you have any topics for today, please add them to the agenda. Let's wait a bit. See if others join. Otherwise we can start.
**Stephen Lang** 02:30 Thanks. Crystals.
Yeah, this is Pete and I 1st time joining. We were invited by Gregel.
So we both work on the calix team at Grafana. So.
**Christos Markou** 02:40 Alright, cool.
**Stephen Lang** 02:43 Yeah, this is our 1st meeting. So bye.
**Christos Markou** 02:46 Welcome.
I guess most use folks.
should be on the open availability summit or something.
So yeah, but I don't know who's joining, so let's give it some more time.
Let's see.
Okay, let's start. And if anybody joins yeah, I don't know if anybody if anyone else will join. But we can start. So yeah, it seems we have no topics for today. And do some very quick triage on the board. Since you're joining, I don't know. If you would be interesting into like helping more with this working group. But we have these board over here that would track the work.
so, for example, here we have, some prs that are already approved by the Sig. I think the Maintainers earlier today to give some the the general maintainers of smart conventions to take a look. Yeah, it seems that an another one was merged. So have co- conflicts here.
but in general we're tracking the work here. I think the main effort right now is this Meta issue which tries to transfer everything that the collector uses today.
In regard with kubernetes, metrics and container metrics. So it's essentially the qubit stats receiver. The cage cluster receiver. Essentially, these 2 components that emit metrics. Those metrics were only defined on the collector itself. We're not part of semantic conventions. But now, with this effort, we're trying to define them within the semantic conventions. Those might.
Yeah, we could have breaking changes between what the collector defines today compared to what we end up like defining eventually in the cement conventions. But that's okay. The first, st we consider this as a 1st step for stability. So 1st we will transfer. We're trying to transfer everything, for from collector to cement conventions.
And then we once we once we conclude this we will give some more time to revisit some topics and target for stability. The first, st let's say, goal is to conclude this work. The 1st transfer, let's say until, by the by, the by, this November to combine this with Kubecon, which is early November, I think, and then we will see. Probably we will give some more time, like 6 months, or something like this to target stability, if possible.
So that's more or less the idea of this working group right now. I don't know if you have any any any topic or any questions or any topics that you would like to to highlight you can bring them here this meeting. So we also have a slack channel.
**Stephen Lang** 07:38 So can I just clarify what you meant by all of that that's captured on this Meta issue.
When you're saying you're transferring everything over from the collector to the semantic conventions. Does that mean that you're creating like draft conventions just based on the metrics and attributes that are in the collector right now and then. We're gonna look to, you know, revise those.
**Christos Markou** 08:02 Yeah.
**Stephen Lang** 08:03 Tricks and attributes to make them more consistent with each other, or whatever, before defining them as as stable. So you kind of import them all wholesale as they are right now, and market as draft.
Is that right?
**Christos Markou** 08:15 We take those as inspiration, let's say, but at the same time, while introducing them, we also try to apply some unconventions guidelines. So it's not that we take. Take them like blindly, just transferring them. We try to May to to introduce them in a in a way that we feel comfortable with so it's not. It's not. It could not be considered like stable. But we put thought on this once. We have transferred everything, and we have the big picture. Let's say we will need to revisit them for sure. Or probably by then we will have, like other issues raised. Or during this work, we have issues that we want to tackle during stability. But we don't just transfer them. We also put thought on those, and we try to introduce them in a way that probably would be would remain like this. Hopefully, or at least for most of them.
**Stephen Lang** 09:14 Okay? So at that point, say that you do. You completed the transfer. There would be some kind of discrepancy between the semantic conventions and the actual collector is that right?
**Christos Markou** 09:24 Exactly. Yeah. Yeah. But the plan is to wait for a stable cement conventions release until we go back and change the collector. So we will move them forward. We will try to stabilize those, and then we will change the collector altogether, probably with feature gates or with specific migration plan.
**Stephen Lang** 09:48 Great. Okay, that makes sense. Thank you.
**Christos Markou** 09:51 Yeah, I I don't know, Dimitri, if you want to. If I forget anything.
**Dmitrii Anoshin** 09:55 Yeah, that's that's correct. Thank you for summarizing it. It's pretty much the same approach we are taking for other stabilization work like for host metrics receiver. We're doing the same.
**Christos Markou** 10:25 cool, then. So yeah, I think there are couple of Prs for review. If you have time you can have a look later. Otherwise. I think we don't have anything else, for for today sounds good.
**Pete Wall** 10:45 Sure. Thank you, Christopus. Okay.
So for the one that you said that that are, you know, the the to do ones, the ones that haven't been started. Do you have? I mean, just for the sake of you know, like Steven and myself, who are kind of new coming into this project. Do you have one like a Pr that you have gone through a review? Just so we can look to see like what are the things that you're looking for? What's the things that are important? So that when we if we pick up one of these Prs, then we can, you know, applicably put in good comments. Things like that.
Anything with the green check mark. Is that what we're looking at.
**Christos Markou** 11:17 Those are merged already. So those those are completed. Let's say, there is one about this one is probably merged, I think a few moments ago. There is this one which is open right now. If you want to pick it up, then we have some CPU met CPU memory metrics related ones. But we're quite close. I I would say, so yeah, if you want to help here. Yeah, you're more than welcome and you can get an idea from other Prs that are linked here.
**Pete Wall** 11:55 Perfect. Okay, yeah, that helps. Thank you.
**Christos Markou** 11:58 Cool.
Okay, then see you in 2 weeks again.
Alright, bye-bye.
**Pete Wall** 12:04 Take care! Goodbye.
