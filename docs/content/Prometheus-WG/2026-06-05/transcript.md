SIG: Prometheus WG
Date: 2026-06-05
Duration: 42 minutes
============================================================

## Zoom Recording Transcript

**Arve Knudsen** 04:17 Hello, David.
**David Ashpole** 04:18 8.
**Arve Knudsen** 04:19 How are you doing?
**David Ashpole** 04:21 I'm doing well. And blessed.
**Andreas Gkizas** 04:23 Nope.
**Arve Knudsen** 04:24 Hello.
**Arthur Silva Sens** 05:36 Hello!
**David Ashpole** 05:39 Arthur?
**Arthur Silva Sens** 05:41 So many people today. It's nice.
We stopped?
**David Ashpole** 06:10 Yep.
Let's go for it. Let me share the… Okay, the meeting notes… Cool. Welcome, everyone.
Let's see what's on the agenda.
Looks like we've got one topic today.
This is from…
**Andreas Gkizas** 06:47 I, I, yeah.
Go ahead.
**Arthur Silva Sens** 06:56 Could you share a bit more context on what would you like to discuss?
**Andreas Gkizas** 07:02 Yeah, I'll try to be quick. That was the initial topic that actually brought me here to your team, and the correlated issue, it is the second one that I put in brackets, the 48767.
So, long story short, is that, in our project, we tried to use the Prometheus Remote Write Exporter, but we had a problem, because when we do batching, the metadata information that are being said from the upstream are being lost, so all the, badges that are being sent, finally, they don't include the initial headers of the initial request. So this, for us, it's a problem because it breaks the routing that we do based on the headers.
Based on this, thing, we tried, let's say, to replace the existing remote write, configuration, remote write queue, and, we changed it with the exporter helpers, functionality and the sending queue of the exporter helper.
We proved that it worked.
And, Then we found out about this issue, the 48767, where there was the same, let's say, initiative, the effort, to, More or less to enhance the existing functionality of the remote rider.
And there was a discussion on this thread, and I tried to add the exporter helper, and tried to, let's say, to add in the discussion why I… at least the Exporter helper seemed a good, approach to replace the existing Remote RideQ.
There was some discussion about the, the existing issues, in the remote right is, the, protection of the priority, and also the, the issue that when we use the wall and we have a restart, we cannot, let's say, persist the data inside after the restarts. So, the addition of the new remote helper, indeed, doesn't, solve the existing problems. It is gonna be a new, let's say, replacement of the remote, remote queue, but… All the initial analysis and all the existing problems that would exist in the remote ride queue should go and should be analyzed on the new exported Helper queue.
So, that… it's the context of what is happening right now, and I tried with an additional PR to add the functionality of the missing keys on the existing remote ride queue, and not on the new exporter helpers queue, in case it helped, the review and the analysis.
**Arthur Silva Sens** 10:11 Thank you.
One question, I'm not familiar with… 100% with the exporter helper.
And do you… do you know if they… So, this behavior of heaters If we replace our wall with, exporter helper, would we get this metadata keys?
by, like, for free, or do we also need to implement that in Exporter Helper?
**Andreas Gkizas** 10:46 So let's get the wall out of the discussion. So, if we just replace with the exporter helper, yes, the functionality is there.
And we are talking about only for the sending queue. So, we have a sending queue on the remote ride queue, and we have a sending queue on the exporter helper. So, if we compare the two sending queues, the functionality of the headers exists on the exporter helper. It doesn't exist… on the remote red queue. The second PR that I have in brackets adds this functionality.
the sending of the headers on the request. Okay, so this is the missing, let's say, functionality for us.
So, if we go to the hole right now.
Because we persist all this data inside the storage, also the headers are not being, saved or persisted, even with my fix. So the wall is out of discussion, even with or without the other.
It's not, let's say, test.
**Arthur Silva Sens** 11:49 Better.
Honestly, I like the idea of getting rid of our custom wall.
Like, this is code that we need to maintain, and if we just use the exporter helper, it would be less code.
but, yeah, I don't know how easy it is to just replace with the exporter helper.
I know that the order is a problem, like, Prometheus… The Prometheus Remote, like, I know there are several vendors who accept remote rights, but I think if we make the Prometheus the open source.
One, the… A bad… a bad, fit?
then that's really, really bad. I think the open source permissions is the most used one for permits remote, right?
As long as we get it working well with Prometheus.
I am all in to replace with Exporter Helper.
**David Ashpole** 12:51 An exporter helper guaranteed things are delivered in order today?
**Andreas Gkizas** 12:56 No.
**David Ashpole** 12:59 Can we make that improvement to Export or helper?
**Andreas Gkizas** 13:01 Yes, yes, this is something that, I think that Dave's comment is just to the heart of the problem. This is what actually raised on the initial issue, that either of the queues can gonna do that.
But, I agree that how to… how the transition should be done from one queue to another is, let's say, an additional discussion. But the problem, I think, should be… can be fixed in the in the… in both queues. I mean that the approach should be the same.
somehow to have an, an ID that, or the, let's say that we'll have the order, and when we have it, let's say, inside the batch, to reorder the batches. I think we can do it somehow.
Because we can have all the data inside the bots.
**Arthur Silva Sens** 13:58 Is there an issue on the collector repository, the core one, requesting this functionality from Exporter Helper?
Like, guaranteeing order.
**David Ashpole** 14:12 Not a recent one. There might be one from, like, 2022 or something.
**Arthur Silva Sens** 14:17 Oh.
**David Ashpole** 14:19 We've had this wall for a long time, you know.
**Arthur Silva Sens** 14:22 Yeah, yeah.
Okay, but yeah, so I… I think this is a good… direction, but this is gonna take a while, right? And, if I understand correctly, you need these heaters, sooner rather than later.
So if… if we accept this PR to support metadata keys… How would it work moving from this to the future where we have Exporter Helper?
**David Ashpole** 14:58 I mean, we have a whole bunch of config that's associated with the current like, wall.
Right, we're gonna have to… if we do a migration, there's gonna be a lot to migrate, and I guess this can be part of it.
**Arthur Silva Sens** 15:11 I see.
**David Ashpole** 15:13 Yeah, it's one more thing, but… I suspect this won't be, like.
the most commonly used feature? I suspect most people are just gonna be, you know, sending remote, right, as they do today.
**Arthur Silva Sens** 15:26 I… I… if I understand correctly, all… Andreas, you work for a vendor, right? So I guess all your customers would have to do this migration?
**Andreas Gkizas** 15:36 Yes, the good thing for us is that we hide the remote ride behind an endpoint, so we do the configuration, so… Let's say we don't care so much on the initial configuration from the users.
Of course, we care about the setting queue, because we need to have the optimal performance in order not to drop data and things like that.
Comparing the two configurations, the parameters of the existing queue and the exported helpers queue, I think that the most crucial that we are missing right now is the block, how is it called? Block on overflow.
Something like that. So the meaning is that, with exporter Herpel, when you have a full queue, you can block the acceptance of new data until the queue Has some space.
This is a crucial one in order not to have back pressure.
This feature is missing right now, totally from the existing, remote ride. All the other configurations, I think that they exist. The buttes, the size of the buds, the parallel things… David, correct me on this, I haven't tried the… the parallel, consumption from the remote, right? With many, consumers. I was reading something that you need to enable with a feature gate and have multiple consumers, but I need it right.
**David Ashpole** 17:02 I… did we not move that to beta yet? It may still be in alpha.
But… I, I thought we'd maybe move that to beta.
I don't remember the current state.
But that sounds correct, that there was that feature gained.
I don't know if it got flipped to true by default.
**Arthur Silva Sens** 17:29 Andres, I'm happy to help you land this PR.
**Andreas Gkizas** 17:35 Thank you, thank God.
**Arthur Silva Sens** 17:36 Yeah.
Could I… ask you to help us migrate to the exporter helper eventually? I… this is gonna take a while.
**Andreas Gkizas** 17:46 I would love to, I mean… Can we agree, let's say, to have a feature gate?
to enable exported Helper.
For start, so to have… to add, let's say, on the functionality of the exporter helper behind the feature gate, and start the tests over there.
How… or maybe behind the cuffing duration, I don't know. Can we have both?
The code, because it's a config one.
what they were…
**David Ashpole** 18:17 I mostly don't want to get into a state where we're half-migrated.
Like, if… if core… if the core repo… If we have a plan for addressing the in-order delivery in Core Exporter Helper.
And, like, we're confident that we can get there.
And then that would, like, open the door for us to replace our wall with… with Exporter Helper, right? So if, like, if there's a path there, and we're pretty sure we can go down it, then… I'm happy to start putting things behind feature gates.
**Andreas Gkizas** 18:54 Okay, so… shall we… besides the existing support of metadata keys?
the… for the exported here, but then… shall we start with this? Delivery… Priority on exported helper, regardless.
So, I will try to adjust the PR on the exporter helper. You don't need to… I will try to solve the problem. Even, I think that the problem should exist even with a normal, let's say, setting queue.
I will try to test even with normal data.
**David Ashpole** 19:31 Right, it just, I guess, depends on… most vendors… I guess don't, necessarily need in order delivery.
**Andreas Gkizas** 19:39 Yeah, for the OTLP, it's not a… it wasn't, it's a… a must.
**Arthur Silva Sens** 19:44 I think it's just Prometheus, the open source Prometheus that needs order.
**David Ashpole** 19:52 I think Google's probably also interested.
I can rope in maybe Braden and see if he'll… Help.
**Arthur Silva Sens** 20:03 Okay, so let me just write down the plan here, so we don't forget.
Oh… We are gonna… Open an issue for the core repository, requesting in order.
Support?
**Andreas Gkizas** 20:25 Yes.
**Arthur Silva Sens** 20:43 We are gonna try to land your PR, With the method that it keys in the existing an existing wall.
And once we have… buying… Latin.
Yeah, niche.
Does it… what I wrote down in the meeting notes, does that look correct to everybody?
**Andreas Gkizas** 21:55 Yep.
there's no comment about war, but I think it's a different beast, I mean… Aye.
**Arthur Silva Sens** 22:07 Yeah, that's correct. I'm just… I know that in Prometheus, every… everything remote ride-related is tied to the wall. I just assume every… everybody… everywhere it is, but it probably is not.
**Andreas Gkizas** 22:22 Yeah.
**David Ashpole** 22:23 Okay.
Yep, that works for me.
**Arthur Silva Sens** 22:33 Does, does that solve your concern, Sandra?
**Andreas Gkizas** 22:38 Really, thank you very much, guys.
**Arthur Silva Sens** 22:41 Cool.
We don't have any other topics.
So we could review… Project boards, unless somebody wants to talk about something.
**Andreas Gkizas** 22:59 Guys, I will block out.
But, real thank you for the prompt response and all the help. I will follow up on the issues, and I'll ping you both, okay?
I'll try also to follow up with the… the exporter help, okay?
**Arthur Silva Sens** 23:14 Yep.
If you… if you'll wanna join… Next time as well, these meetings are always open.
**Andreas Gkizas** 23:21 Of course, of course.
Thank you very much.
**Arthur Silva Sens** 23:25 Bye-bye.
**David Ashpole** 23:25 Yep.
**Andreas Gkizas** 23:26 By the way…
**David Ashpole** 23:38 Hey, there's nothing to do here yet.
Let's see… Nice.
Nice.
So there's two that can be picked up by people.
Content negotiation…
**Arthur Silva Sens** 24:10 That translation strategy, I think I was waiting on you reaching out to one of your colleagues. I don't know if that happened.
**David Ashpole** 24:23 One of my colleagues?
**Arthur Silva Sens** 24:24 Yeah, yeah, you're really good. You said you received… Right next to the guy.
**David Ashpole** 24:30 Oh, Quintin.
**Arthur Silva Sens** 24:31 Venting? Yeah.
**David Ashpole** 24:32 Did I not respond to that? I thought I pasted there.
**Arthur Silva Sens** 24:35 Maybe you did, I just missed.
**David Ashpole** 24:39 Where's the… Yeah, where's that?
Let's find that.
Should add it to our board.
I did. We just need to open the PR.
That closes it.
**Arthur Silva Sens** 25:13 Can you put that on the board? I can open the PR.
**David Ashpole** 25:17 Sure. Yep.
And the board.
**Arthur Silva Sens** 25:21 I added the… our team to the code owners, but it didn't work.
Because we don't have… right access, I… we don't get pinged anyway.
**David Ashpole** 25:36 That's unfortunate.
Yes. Okay, so it's on the board now.
**Arthur Silva Sens** 25:43 Right, I can take those.
**David Ashpole** 25:45 Interaction with translation strategy. Is this one… Okay, so we probably need more implementations here.
**Arthur Silva Sens** 26:06 I've been… I'm having a hard time with the SDK maintainers.
I… usually the PRs that I open don't get reviews.
**David Ashpole** 26:18 What languages?
**Arthur Silva Sens** 26:22 Yeah, like, I opened PRs for Rust SDK, Python, JavaScript SDKs, implementing some stuff.
And they just… Stay there.
**David Ashpole** 26:32 Rust, JavaScript, and Python?
**Arthur Silva Sens** 26:35 Yeah.
**David Ashpole** 26:36 For rust, You can rest.
**Arthur Silva Sens** 26:40 This is Siho.
**David Ashpole** 26:41 Yeah, Deidre's the only one I know who will review this stuff.
And… Python… You can… you can ping me on the Python ones.
I'll review it, and then I'll ask Aaron to approve.
He's one of the maintainers.
**Arthur Silva Sens** 27:04 The PR is already approved.
Oh, yeah? There are a few PRs that are approved, and they… nobody clicks the merge button.
**David Ashpole** 27:13 So you need two approvals?
**Arthur Silva Sens** 27:15 Oh, okay.
Yeah, I can, I can bring the links later.
**David Ashpole** 27:20 Yeah, it's kind of tricky, right? Because you need two approvals, but you, They also don't have that many active maintainers, so… wait, I have, like… I have, like, 12 PRs in OpenTelemetry Go that have one approval.
**Arthur Silva Sens** 27:32 and they'll…
**David Ashpole** 27:36 It's, like, all the optimization work.
**Arthur Silva Sens** 27:40 Does Brian help with… Code reviews, or he just joins the meetings?
**David Ashpole** 27:47 He helps every once in a while.
He's not, like…
**Arthur Silva Sens** 27:52 If… giving him some… some kind of… Official position would, incentivize them to do more.
**David Ashpole** 28:03 I don't know, he seems… I can't tell if he's, like, how interested he actually is in… Working on the project.
**Arthur Silva Sens** 28:10 Yeah, me neither, to be honest.
**David Ashpole** 28:11 So.
**Arthur Silva Sens** 28:12 Dave the mystery.
**David Ashpole** 28:13 him, you know? He seems…
**Arthur Silva Sens** 28:14 Okay, yeah.
**David Ashpole** 28:15 A person who works on what he wants to work on.
**Arthur Silva Sens** 28:17 Yeah.
**David Ashpole** 28:18 Yeah.
And I'm… I'm cool with him just… You know, being there to discuss things, if that's… what he wants to do, but… Alright, is there anything else that's workable here? Target info configuration. I think this is workable. This is… Oh, we need to update a bunch of names, don't we?
I'm gonna mark.
**Arthur Silva Sens** 28:44 What do you mean?
**David Ashpole** 28:46 I thought we changed… they used to be, like, without whatever.
**Arthur Silva Sens** 28:50 There were a lot of width, and we removed all the width.
Yeah. But, we vowed, I think we kept… we kept…
**David Ashpole** 29:00 Target.
Oh my goodness.
Okay, so we're not gonna do… target info config. I feel like that depends on target info being stabilized, right?
Feels weird to stabilize without target info. Target info's not stable.
Okay. Metric conversion…
**Arthur Silva Sens** 29:28 This is already marked as blocked.
**David Ashpole** 29:30 Okay, I see, I see.
Blocked, blocked.
Action with translation strategy.
This is one we should try and do.
I think it's workable.
Yeah, yeah, yeah.
Or maybe we should mark this one as blocked on… This…
**Arthur Silva Sens** 29:56 Yep.
**David Ashpole** 29:57 I forget how to do the blog.
**Arthur Silva Sens** 29:57 I can pick up all the translation strategies.
**David Ashpole** 30:01 Okay.
**Arthur Silva Sens** 30:01 I'm gonna assign myself.
**David Ashpole** 30:20 I don't actually see assignees on many of these.
Oh, that's right, because we can't assign cryo.
**Arthur Silva Sens** 30:25 Yeah.
**David Ashpole** 30:42 Okay… Content negotiation.
Do you want to put up… looks like this one is just, like, move it to stable.
Content negotiation, do you want to do that one as well?
**Arthur Silva Sens** 30:59 Yeah, sounds good.
**David Ashpole** 31:02 I honestly sometimes feel like it's easier to get things through if I'm one of the reviewers.
**Arthur Silva Sens** 31:08 Yeah, I believe so, yeah, that's why I'm… I want me to open the PR, because then my approval doesn't count.
**David Ashpole** 31:18 Okay, let me assign myself to this.
This is blocking the rest… this is blocking, like, basically the rest of these things, I think.
**Arthur Silva Sens** 31:27 Yep.
It would be awesome if we could call the specs stable by June, by end of June.
**David Ashpole** 31:38 Oof, yeah, that would be… That's a good goal.
Let me look at this.
Never.
This is the same thing.
Sign myself.
**Arthur Silva Sens** 32:01 Just, just a little quick, Kyle, the SIG instrumentation meeting should be happening very, very soon.
**David Ashpole** 32:09 you want to.
**Arthur Silva Sens** 32:09 I think… no, no, I can say Kyle will go there. But, like, I think this meeting here won't take the full hour, so I'll probably join later.
**David Ashpole** 32:18 I'm looking to see if there's anything else.
That's… that we can even discuss here.
I'll go ahead and assign myself to this one.
But I think otherwise, everything is pretty much a sign that we can work on.
And translation strategy and resource attributes are the two things left, so… Cool. I… why don't we all head over? I think that's, probably best.
**Arthur Silva Sens** 32:52 Can we… since him and Shu is here, and everybody else left…
**Himanshu Singh** 32:57 Yeah, we can…
**Arthur Silva Sens** 32:58 Talk about the Prometus Remote Write receiver.
Yeah, sure.
**David Ashpole** 33:03 Sorry, I didn't.
**Arthur Silva Sens** 33:03 Nice to drink.
Yeah, I… like, we are always happy to get more maintainers, but, like, It's, how do I say?
This receiver is just one small piece in a bigger puzzle.
Yeah. Have you… do you know what other kinds of work we are doing in the SIG? Like… the direction we want to take the remote rice receiver… I don't know, I just… Let's just talk later.
**Himanshu Singh** 33:38 Yeah, like, I'm not that much aware of that, just using the PRW receiver at our KS side.
So, I don't know much of the direction where this is going. This is my… this is my first SIG meeting.
**Arthur Silva Sens** 33:54 Cool.
**Himanshu Singh** 33:55 But…
**David Ashpole** 33:57 Yeah.
**Arthur Silva Sens** 33:57 the…
**David Ashpole** 33:59 Just for… What time zone are you in? I'm just curious, like, if this is a hard meeting for you to make.
**Himanshu Singh** 34:09 Like, I'm in Indian… India time zone, so it's… which is 5.30.
**David Ashpole** 34:17 That's not too bad.
**Himanshu Singh** 34:19 Yep. Yeah, it's, around 9.
PM in the evening.
**David Ashpole** 34:26 I thought you said 5.30. You said… so it's 9.30, okay.
**Arthur Silva Sens** 34:32 We don't…
**David Ashpole** 34:34 Yeah.
**Arthur Silva Sens** 34:35 We don't require… yeah, we don't have to join if it's inconvenient.
That's not a requirement to become a maintainer.
**Himanshu Singh** 34:43 No, no, it's not a problem.
**Arthur Silva Sens** 34:46 Hold on.
so the… the… the receiver… Like, the collector components, they… Yeah, implementations of, Office Pack.
spec is, document that we… We tell how to translate metrics from one format to another.
And this… our work is mostly on the spec, and the… And the components are just an implementation of that.
Oh.
when we try to make changes to the receiver.
Like, you did a bunch of fixes, like, you made it more performant, you made some bug fixes, this is very obvious work that needs to be done.
But there are sometimes work, like, hey, summaries needs to be translated in this way, or summaries need to be translated in this other way, and this is the kind of thing that we cannot just… like, whatever we decide, just do it, you know? It needs to go through the process of going through the spec.
**Himanshu Singh** 36:00 Yeah.
Okay.
Yeah, yeah, totally, I can, like, I, yeah, I'm, like, just started working with the, KTAS site, so got into the PRW. Yeah, I can discuss in my team, like, like, like, we are migrating in our KTS, from the two layer to one layer also, so there I can, like, see, like, on which direction we want to see the receiver.
So, I can discuss that.
**Arthur Silva Sens** 36:36 Cool.
**David Ashpole** 36:41 Cool.
**Arthur Silva Sens** 36:41 Yeah.
I don't know what else to say. Thanks for sharing, thanks for coming.
**David Ashpole** 36:50 there any… Is there any, like, big feature work left for the Prometheus RemoteWrite receiver?
**Arthur Silva Sens** 36:56 I… I think, right now, there's not, but, like, we wanted to do composite summaries in the permita side.
Once that's done… That's probably a big chunk of work.
**David Ashpole** 37:14 Okay.
Trying to think if there was anything else.
**Arthur Silva Sens** 37:19 Yeah, we will speak, with Jonathan as well. He could not join, and then we'll give you an answer. Is that… is that okay?
**Himanshu Singh** 37:29 Yes, sir.
**Arthur Silva Sens** 37:32 Bye.
**David Ashpole** 37:34 Thanks.
Thank you, Ms.
**Arthur Silva Sens** 37:37 Bye-bye.
