SIG: Agent Management WG
Date: 2025-07-23
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 01:44 Hi Andy.
**Andy Keller** 01:50 Hey, Tigrin! How are you?
**Tigran Najaryan** 01:53 Good! How are you?
**Andy Keller** 01:54 Good. You have a good break.
**Tigran Najaryan** 01:56 Yes, nice vacation family vacation went to Europe.
**Andy Keller** 02:01 Oh, wonderful!
**Tigran Najaryan** 02:02 Netherlands, Belgium, to a few different cities, so was was good.
**Andy Keller** 02:07 Awesome sounds, great.
**Tigran Najaryan** 02:09 Yep.
**Andy Keller** 02:11 While you're gone, I realized I'm not a a maintainer of the spec. I I knew I knew this, I guess, but I just didn't really think about it. So I couldn't merge and release the changes that we're.
**Tigran Najaryan** 02:25 Do you? Do you want to be.
**Andy Keller** 02:28 I think it'd be probably good to have somebody else, so that you aren't the only person. But and I'm I'm happy to do it certainly familiar with it.
**Tigran Najaryan** 02:36 Yeah, sure. Let's do it.
**Andy Keller** 02:38 Okay.
**Tigran Najaryan** 02:39 Hi Evan!
**Evan Bradley** 02:42 Hello!
See you again.
**Tigran Najaryan** 02:46 To see you.
Hi, Michael!
**Michel Laterman** 03:04 Oh!
**Tigran Najaryan** 03:16 So I'm just back from the vacation. I did a round of reviews and mergers and and stuff like that, so I think I merged a few and close the few Prs there.
Michael, I think I did also review yours, the one about the connection setting status.
I left a couple comments there for you questions. I think it's pretty close now. So once we resolve those we we should be able to manage.
The one that is wasn't quite clear to me is the based on what do you decide that the the status needs to be updated or no. So maybe you can take a look and and help help me understand that that part. The rest seems fine to me. It looks good.
**Michel Laterman** 04:03 Yep.
**Tigran Najaryan** 04:04 And I think you also have another one that is in a draft.
**Michel Laterman** 04:08 Yeah, it's it's pretty rough right now, because gorilla web sockets isn't merging anything.
**Tigran Najaryan** 04:18 Yeah, they're not, really I I actually checked just today to see if they replied. And they didn't right then. Nothing.
**Michel Laterman** 04:24 Yeah.
So right now, I pushed to commit earlier this morning, just trying to see if I could switch the Client Websocket Library to Gws it provides like a really nice Api for the programmer to use.
But I'm having a bug right now with the test, where things aren't closing in the right order.
but I don't know if I'll even need to switch the client library because their approach is custom dialers, and I haven't checked if I can just pass a custom dialer into gorilla.
**Tigran Najaryan** 05:06 Okay?
So I'm gonna ask, yeah.
**Michel Laterman** 05:09 Yeah, I'll publish my own custom Dialer with only using standard go. I'll see if I can just use gorilla with a custom dialer and go from there, basically.
**Tigran Najaryan** 05:22 Okay, yeah, that's that would be preferable. Switching the library to something else would be a bigger lift.
**Michel Laterman** 05:29 Yeah.
**Tigran Najaryan** 05:30 And we would want to to do a whole lot more extensive testing if we do that particularly performance testing which I did back then when I was starting.
yeah, I the bunch of tasks.
**Michel Laterman** 05:43 Yeah, I'm wondering.
**Tigran Najaryan** 05:44 Okay.
**Michel Laterman** 05:44 If you, if you have any anything set up for scale tests. So.
**Tigran Najaryan** 05:50 Unfortunately, it has been a while ago, and I.
**Michel Laterman** 05:54 Yup!
**Tigran Najaryan** 05:54 Don't think I kept all those experiments. I did a bunch manually.
Yeah, because.
**Michel Laterman** 06:01 What I would love to do is just set up a docker container that has one gig of memory for a server, and just see? How many connect? How many?
Yeah, yeah, for Htt.
**Tigran Najaryan** 06:13 I I can take a look, but I did test with like a a few 100,000 connections.
**Michel Laterman** 06:20 Okay.
**Tigran Najaryan** 06:20 Back then with with with actual Ec, 2 instances running on aws with the load balancer, or like a production like environment to see where we're hitting the limits. And I stopped somewhere around, maybe half a million or something like that, connections which seemed.
**Michel Laterman** 06:39 On!
**Tigran Najaryan** 06:39 Good enough to me.
Own a couple, I think. 2.
Okay behind the load balancer. I can try to dig up the settings I had, but I unfortunately, I didn't automate. It was fairly manual process. But just as a caution, if we were to switch, we would have to reproduce this, to to be.
**Michel Laterman** 06:59 Yeah, yeah.
**Tigran Najaryan** 07:00 Confident that we're not.
We're not regressing performance. Wise.
**Michel Laterman** 07:04 Yup!
**Tigran Najaryan** 07:04 So we we could avoid that. I think that would be preferable.
**Michel Laterman** 07:08 No, yeah, I agree.
**Tigran Najaryan** 07:11 No.
**Michel Laterman** 07:14 So I think I'm the only one with something on the agenda right now, and it's you know Eric has something to follow up on I just noticed that our the go mode in OP go.
It's still on 1.2 2 and.
**Tigran Najaryan** 07:30 Yes.
**Michel Laterman** 07:31 Standard go.
Life support is currently some previous manner.
So I just wanted to know, is there a reason? Or is this just.
**Tigran Najaryan** 07:40 We're just logging, we should. You're you're absolutely right.
**Michel Laterman** 07:42 Good.
**Tigran Najaryan** 07:43 We should go to 1, 23, essentially use the same version as the collector uses. I think that should be our strategy. We're on 1 22. Right now we should bump to the next version. I just tried to do it actually, before I saw your message, and something is not building there. If you, if you get a chance, if you're willing to take a look at it, that would be great, because I'm not sure I'm understanding why, exactly, is it not building? Because it's building on my machine. No problem. Something is failing in github actions, and I'm not sure I understand what's going on there.
But yes, the answer is, yes, we should.
Okay.
Oh, Eric, welcome. I'm not sure if we met in this call. So you have something on the agenda.
**Eric Chlebek (Sumo Logic)** 08:41 Hi Tigrin. Yeah, we haven't met on this call. This is the 1st time I've joined. But you may remember me. I've contributed to OP.
**Tigran Najaryan** 08:48 Yes.
**Eric Chlebek (Sumo Logic)** 08:48 Or.
**Tigran Najaryan** 08:49 Yes, I do.
**Eric Chlebek (Sumo Logic)** 08:50 Yeah, So I was just wanted. I wanted to call in and ask about the OP Amp Supervisor and remote upgrades, because, My employer is very interested in remote upgrade capability, and I was wondering if the project we're still pursuing that, because I did see that there was a Pr. Opened but did not get merged.
and I think it's actually been closed to stale at the moment.
**Tigran Najaryan** 09:18 I think it's for you, Evan. Do you guys want to comment on that.
**dpaasman** 09:25 Stop.
I think that's still something we want to pursue. The Pr has been open for quite a while.
it includes a lot of substantial changes to the way the supervisor works. And there's a lot of consideration needed, especially from a security perspective when we're downloading binaries.
And I'm sure they're executing them.
So I think because of that, it's just gone through a very long review process. And so yeah, I I think that's still something that.
No, I know. We certainly wanted that buying plan.
and I think that's the end goal of the supervisor as well as having that functionality added.
Just kind of a long road to get there.
**Eric Chlebek (Sumo Logic)** 10:15 Yeah, yeah, it's very understandable.
**Andy Keller** 10:17 Sorry I was just gonna add that it's yeah. It's been reviewed several times. Gone through several rounds of feedback but never quite got over the finish line. And then, you know, during that process, as those things get reviewed and people kind of move on to other things and then come back to it, and it just it just has kind of taken a long time.
So if it's something you're interested in.
I think that's the starting point is, is trying to get that over the finish line. And so.
you know, testing with that branch.
looking at that pr, and I think it's really close.
But I also myself haven't looked at it in a little bit. Dakota has been the one primarily working on it, but also not primarily working on it for the last few weeks. So.
**dpaasman** 11:03 Yeah, yeah, that yeah. And that's on me for allowing the Pr to go stale.
I haven't looked at in a long time. I didn't realize they had gone. Still.
**Tigran Najaryan** 11:14 I think it's it's closed already. Right? It's not open anymore. I I.
**dpaasman** 11:18 So.
**Tigran Najaryan** 11:19 In the open list.
Yeah.
**Eric Chlebek (Sumo Logic)** 11:21 Yeah. The stale bot closed it. I think.
**dpaasman** 11:23 Okay.
**Tigran Najaryan** 11:25 I, personally would like it to be completed.
I think we want that capability. The reason I was not rushing it personally was exactly that right that we wanted to be confident we're not bringing some something that that is a nightmare from security perspective. Right?
If we can get additional eyes on the Pr.
Somebody, especially from somebody who has the experience with this sort of things, and we can get additional confirmation that if this looks good.
then I think we should it. I agree with Andy. It's pretty close to.
I mean, I, personally don't see what is wrong with that right. Let's let me say it this way.
So if we could get more.
more, more especially experts in the security area to confirm that they also are happy with it, I think we can go ahead, and I don't know if there's final cleanup needed to that and and merge it.
**Eric Chlebek (Sumo Logic)** 12:31 Yeah, for for what it's worth. Our security team did look at the at the at the draft specification for that. And they thought it was more or less sound.
It's not clear to me how this kind of strategy would be accepted by something like Fips or Fedramp. Maybe that's a conversation for another time, but definitely agree with being cautious about the security aspects here.
**Tigran Najaryan** 13:02 Yeah, if you, if you can bring people yourself or others from from Sumo logic to to take a look, review, comment.
approve even right to have more, I guess. Independent confirmation that this looks good, regardless of whether you have official approval. Rights on the collector or no. I don't think that matters then we would probably all feel more comfortable with going ahead and and merging it.
**Eric Chlebek (Sumo Logic)** 13:34 Okay, yeah, we're happy to pitch in.
we. We obviously weren't involved in the initial stages of the development. So our confidence it may not be that high either, but definitely, very willing to help out. And we'll take a look at the Pr. For sure.
Thanks.
**Tigran Najaryan** 13:57 Evan, do you think you could reopen the Pr. So that we can take another look.
**dpaasman** 14:03 Yeah, I think.
Thank you.
**Evan Bradley** 14:06 Yes.
**dpaasman** 14:06 Brandon's, Pr.
Oh, yeah, sorry.
**Evan Bradley** 14:10 No, I can. I can go reopen it as long as it hasn't been pushed to We might want to reorganize the commits or squash something at some point. But I do think that the comments on the Pr are going to be valuable at a minimum.
Yeah, everybody anybody wants to do that.
That was just something I was noticing as time was going on, since obviously this point, it's changed hands once. Anyway, I'll go through and open that and we can go from there.
**dpaasman** 14:47 Cool.
Are you a part of the Cncf slack at all?
Yeah, I'm on there. You can find me feel free to reach out.
Yeah, yeah, I'll send you a message when that Pr is, you know, rebased and in a good state to be reviewed again.
**Eric Chlebek (Sumo Logic)** 15:04 Sounds, good thanks.
**Tigran Najaryan** 15:13 Okay, okay, anything else. Anyone. Other topics.
Okay. Thank you. All.
Bye.
**Eric Chlebek (Sumo Logic)** 15:30 Thank you.
