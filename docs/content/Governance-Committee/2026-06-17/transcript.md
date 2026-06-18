SIG: Governance Committee
Date: 2026-06-17
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Austin Parker** 00:06 Oh, okay.
**Ted Young** 01:19 Austin, did you move back to Kentucky? Because it looks like.
**Austin Parker** 01:22 No.
No, just outsides.
I'm just enjoying, a lovely New York… Early summer day.
Are you referring to the cutoffs?
**Ted Young** 01:40 The cutoff's the hat, the… it's like, it looks hot.
**Austin Parker** 01:44 I always wear the hat.
**Ted Young** 01:45 Southern.
**Austin Parker** 01:47 Can you take the… Take the boy out of the south, can't take the south out of the boy.
No, but I figure I have all this, like, nice outdoor space, I should enjoy it, even if it just… Even if the only thing that I get to enjoy is sitting out here while being on a computer.
**Ted Young** 02:13 Yes.
**Austin Parker** 02:14 at least I have, like, this nice green trees and… sunlight, and… Bugs.
Maybe not the bugs.
**Pablo Baeyens** 03:55 I think your topic set is the same as mine, about…
**Ted Young** 03:59 Okay, great.
And we will…
**Pablo Baeyens** 04:02 What are we applying?
**Ted Young** 04:04 Yeah, we'll move it.
Yay.
Looks like Quorum?
**Austin Parker** 04:45 Yeah.
We wanna get… we have two separate private issues? Do we wanna…
**Ted Young** 04:51 Maybe get really helps first.
**Austin Parker** 04:54 Yeah.
I guess, start with Dark Flutter?
**Ted Young** 05:01 Yeah.
**Pablo Baeyens** 05:02 Yo.
phones.
**Austin Parker** 05:08 Oh, there's severing.
**Severin** 05:11 I'm not sure if you can hear me, like, my audio is really horrible.
**Ted Young** 05:16 We're gonna use…
**Austin Parker** 05:16 We can hear you.
**Severin** 05:18 Yeah, so I followed up with them, like, as we discussed, I think, two weeks ago, so they have now put out a proper proposal.
I'm also waiting for someone from Google to come back on commenting on it, right? They wanted to take a look into it. And they also put out a blog post proposal, so it's making some good progress, but… Yeah, there's some simple questions, and I think Michael submitted it, and I'm not sure if he has fixed the CLA issues, but yeah.
**Austin Parker** 05:50 It's not…
**Severin** 05:53 He's not? Okay, I will… I will chase him on that.
**Austin Parker** 05:57 Yeah.
**Severin** 05:57 So I don't know if there's anything specific to talk about this today, but, like, it's making progress. I think that's… that's the good news.
**Ted Young** 06:06 So, yeah, I mean, there's definitely, like, legs under this thing, which is great. Like, a lot… I feel like this has come a long way. There's contributors now from different organizations, and a lot of Flutter out there.
So that's awesome. As usual, I think the challenge and bottleneck is, like, what kind of attention do we need from the TC for this project?
Right? Does there need to be, like, a donation review of some kind?
And a TC sponsor.
And… What should we do on that front?
**Pablo Baeyens** 06:51 Sorry.
**Austin Parker** 06:52 Oh.
It looks like, according to this, the design was reviewed by Android, someone from Android Sig.
Already, so… I… I think it prob- this is probably just escalating?
from TC? Like, I don't think it needs… super strong guidance, but I do think we will need a… Tc review of the… donation.
**Pablo Baeyens** 07:28 Right, and my question was going to be if we know of somebody on the TC that is interested on this. I don't think we do it right.
**Trask Stalnaker** 07:39 To me, a… less… The most important thing to me, at least, is the… is trying to get a… I don't know if they have any… the maintainer list, if it includes anybody who is… Already engaged, actively engaged in the community.
**Ted Young** 08:04 Yeah.
**Severin** 08:05 chip in that, I think.
They have listed some staffing already.
There's someone from Embrace, but I'm not sure if they're… as a client.
**Austin Parker** 08:19 SIG pre… Guy… It's a Robert Magnuson, who's at Grafana?
**Ted Young** 08:30 Yeah, he's new to OpenTelemetry, but has been maintaining Grafana's version of the Flutter stuff for some time.
**Austin Parker** 08:38 Okay, and there's, Ben Bennett from Embrace.
Yeah.
**Trask Stalnaker** 08:46 I'm not recognizing…
**Austin Parker** 08:49 Yeah, there's…
**Trask Stalnaker** 08:50 containers.
**Austin Parker** 08:50 Pizza, huh?
I only… Maint RIC is Cesar, or Cesar?
But he's not on the project, he's just the designer view.
**Trask Stalnaker** 09:01 Yeah, so maybe if we could get, Caesar to, join, and it's, his liter… his, hub alias is like the salad.
**Severin** 09:15 Excuse.
**Trask Stalnaker** 09:16 Yeah. Yep.
**Austin Parker** 09:18 Okay.
**Trask Stalnaker** 09:18 That is clever.
**Severin** 09:19 Now I get it. Now I get it.
**Austin Parker** 09:21 Thank you for bringing it up, because… yeah, no.
**Severin** 09:26 No, I… Okay, okay. Yeah.
**Trask Stalnaker** 09:29 But yeah, if we could get him as a, to commit as a boot… just… even just as a bootstrap maintainer for, like, the first 3 months.
That would make me feel a lot better from a… just from an infra perspective of… there's generally a lot of questions that new SIGs have that, it helps to have somebody who can field those.
**Severin** 09:51 There's… Is Cedia only from Android that… or should we just ask anybody at Android, or ask them if they would be happy to help them get started? So, I mean, there's a lot of… kind of overlaps.
**Morgan McLean** 10:05 I can ask,
**Trask Stalnaker** 10:06 Yeah, anybody.
**Severin** 10:07 I'm like, it's.
**Morgan McLean** 10:07 Obviously, I can ask Jason Plum if you want.
**Austin Parker** 10:09 I was gonna say, you know, from Android or even I.O, like, Dart and Flutter will run.
**Morgan McLean** 10:14 The whole point of it is you can use it on iOS.
**Austin Parker** 10:16 Yeah, so I would say, like, maybe also put it out to the iOS guys.
**Severin** 10:21 At least half.
**Morgan McLean** 10:21 Awesome.
**Severin** 10:22 them, like, also review it, and then, like, yeah, pay attention to it. I think it's a… it's a good point.
And again, like, I think they put it in the proposal as well, like, there's a few folks from Google that should also maybe tag on the issue and say, like, hey, can you… can you comment on that? So, there's something on industry outreach where they said, like, there's Let me see… Abdullah Shabban and Kevin Moore.
They tagged them in their industry outreach, so maybe we should also make sure that they're aware of that. I think we talked about this last time, that we want them also to know about that.
**Ted Young** 11:05 Great.
**Severin** 11:07 Yeah.
**Ted Young** 11:08 And just as, like, a meta note on this, you know, like, we want to evolve our project management process in general.
And this is, like, a good example of this, right? Like, normally we'd be, like, the TC would need to be super involved in something like this, but the reality is, like, there isn't really much expertise in this domain on the TC anyways, right? Yeah. We do have these other people in our community, like Jason.
you know, and Cesar and stuff, who have expertise in this domain, and expertise in open telemetry. So I think this is, like, another case study of lake.
Trying to find a way to… to… I don't know what.
**Severin** 11:45 delegate, yeah.
**Ted Young** 11:47 formalize this as, like, a change, but, like, it's a good example of a place where, you know, this would work better by just being able to Find the right people and say, you're… you're… You get the hat, you're in charge of this.
**Trask Stalnaker** 12:01 Most of the language SIGs don't really have TC sponsorship at this point, anyways.
**Austin Parker** 12:08 Yeah.
**Trask Stalnaker** 12:09 So it's more important… the TC sponsorship, I think, is more important for these cross-cutting things.
**Ted Young** 12:15 Yeah.
**Austin Parker** 12:16 Yeah, I feel like that's why I said, I think just, like, some ones that they can escalate stuff to, if there's…
**Trask Stalnaker** 12:22 spec questions.
**Austin Parker** 12:23 I mean, the thing is, there's already something, it already works, there's already people using it, like, it doesn't feel like there's going to be a lot here, so I think just someone to kind of, like, hey, I'll check in on you every few weeks.
**Ted Young** 12:36 Okay.
**Severin** 12:37 And I think it's also good to know if a language can implement the SPAC without having a spec expert, like, attending every meeting, and, like, I think maybe it's… maybe it's also proving out if the SPAC is, like.
easy to follow, so to speak. So, yeah, having someone to escalate to is maybe the right… the right choice. But I will check with the TC who is willing to do that. And they would have the Android maintainers, right? Side by side, and maybe Swift.
**Ted Young** 13:06 Usually what we… Sorry, go ahead, go ahead.
I was gonna say, usually what we do is, have, the language SIGs when they want to stabilize, like, there's some point where they get a review of each signal from the TC, just to make sure they actually did implement the spec correctly.
But this SIG is starting with a donation, right? Like, it's a little bit farther along.
Then other efforts, which are starting from scratch.
But anyways, I think it's fine. We can get it sorted. I don't feel… I guess what I'm saying is, like.
if we've got people like Jason involved, like, I don't really feel like the TC needs to pay a lot of special attention to the SIG. I feel like… like, those reviews, anything weird about it would get raised properly by having those people take a look at it.
**Morgan McLean** 14:04 I agree, Ted.
**Ted Young** 14:05 Yeah.
Okay.
But I will poke in the GCTC channel to figure out who's gonna be the escalating sponsor.
Alright, next up, Severin Maintainer Track.
**Severin** 14:22 Yeah, I just wanted to clarify where we are standing with that, like… And I said, you know, on behalf of maintainer, something to the maintainer track, not the summit, the track.
Or did we sort something out there? I wasn't able to follow that conversation with the community managers, so I was, like, just wondering, do we have any news on that, or…
**Austin Parker** 14:44 The impression I got from the… or where it was the last time is that it's… The same as last time, so we would… if we submit The project updates, and that takes the slot.
So…
**Pablo Baeyens** 15:01 Last time, we did have more than one maintainer truck.
**Austin Parker** 15:04 I think last time… alright, so when I say last time, I mean the normal way.
Last time was the exception, apparently.
**Pablo Baeyens** 15:15 Okay… As a graduator?
**Morgan McLean** 15:19 Project, do we get more of these, or no?
**Austin Parker** 15:22 Apparently not.
**Pablo Baeyens** 15:23 No.
**Severin** 15:24 So, we only get one now, like, it's confusing, I think.
**Austin Parker** 15:29 I think it's… yeah, I… I think we're just gonna have, like, I think we just need to submit the maintainer, we need to do the normal thing, someone needs to take… Point on submitting the project update, and… We will just have to yell at people.
**Morgan McLean** 15:44 When's it due?
**Pablo Baeyens** 15:47 Is it worth… submitting something? I know some people on the collector's seat would be interested in submitting something to maintain a track, maybe in collaboration with people from CENTCOM.
I can tell them, no, don't do that, or I can tell them, like, Let's try.
Good morning.
**Austin Parker** 16:09 The… the answer… My interpretation is we only get one thing.
**Pablo Baeyens** 16:17 Okay.
**Austin Parker** 16:22 Like, then we can…
**Pablo Baeyens** 16:23 Iris.
**Austin Parker** 16:26 I can double.
**Severin** 16:26 So we tell maintainers, like, yeah, no, not gonna happen, so sorry for, like.
Making you excited about that it's not happening.
Okay.
**Pablo Baeyens** 16:40 Okay.
Nope.
Okay, then I think it's my topic.
So… On the 2025 GC elections, there was some… discussion…
**Morgan McLean** 17:03 I don't know if we're finished with that topic. Who's doing the submission for the maintainer track? We should put an owner on it.
I'm happy to do it.
**Severin** 17:11 The one thing I think, Didn't Alolita say something on the channel?
**Austin Parker** 17:16 Alita said she.
**Severin** 17:17 It's like.
**Austin Parker** 17:18 too. Great story.
**Morgan McLean** 17:19 Perfect.
**Austin Parker** 17:20 Someone should follow up and Slack with her on that.
**Morgan McLean** 17:22 poker right now. Yeah. Alright, go ahead, Pablo.
**Pablo Baeyens** 17:26 Sure. So… yeah, we talk on the 2025 election cycle about introducing some rules about campaigning, because there were a few related questions on trust violin issue.
And I put a suggestion there on the issue of what to add to the governance charter.
So, yeah, I'll follow up ER next week, unless somebody complains. So please complain if you don't like it.
**Austin Parker** 17:56 Oh, it looks like Alolita already said she's working on the abstract to be submitted for Cuban project update, which she'll share that later today.
Yeah, oh, I looked at the thing you posted, Pablo, it looks good to me, so…
**Pablo Baeyens** 18:14 Cool.
Yeah, so expect a PR at some point.
Should we… Move to the private session, then?
**Austin Parker** 18:30 Yeah, hold on, I got this… Assign into Slack.
Cloud-native.
My… cap… bit my… Laptop.
And so my laptop screen broke, and so I'm on a different laptop, and…
**Trask Stalnaker** 18:52 That is a… strong cat!
**Ted Young** 18:54 Fuck.
**Trask Stalnaker** 18:54 kind of cat you got?
**Morgan McLean** 18:56 My cat does the same. She gets jealous of a laptop on someone's lap, because then she can't go in your lap.
So she bites the screen.
Yeah, she, like, just…
**Austin Parker** 19:09 like, tiny…
**Severin** 19:10 I'm not sure if this is… I'm not sure about it anymore, like… I have a feeling it's smart.
**Austin Parker** 19:21 Like, it was a tiny, tiny, fight, too.
Like, she just, like, got the corner, top corner, and somehow it, like, fried… like, I don't know if the digitized… I don't know what exact part got… got, but, like, the screen… Okay, I'm signed in. The screen, like, stopped working entirely. I'll post a picture later. I'm gonna start a meeting and put it in the GC chat.
**Ted Young** 19:47 So, one, the, One quick thing, we'll talk about it on Slack, but I just wanted to flag before we go.
Because I just saw it in the Japan channel, we're getting more and more questions around, like, terms like hotel native and stuff like that. Like, I know that we want to, like, maybe with a collector have, like, an official certification program and yada yada yada.
But just as, like, a thing to put in everyone's head, I think we should not wait for some big fancy certification thing to maybe go through… and add in the community repo or the spec or somewhere, maybe just start working on some of these terms and how they apply to different domains. Because we're just starting to get, like, questions around this stuff, and we should start… Coming up with some guidance before people start inventing their own meaning for these terms.
**Severin** 20:42 I think we had an issue in that on Docs, like, a year or two ago, so maybe we can revise that. I will double-check on that.
Yeah. Good call out.
**Ted Young** 20:50 No need to, like, have a big discussion right here, right now, we can move on, but I just wanted to like that.
**Austin Parker** 20:55 Cool. Alright, I'm gonna go start the domain.
