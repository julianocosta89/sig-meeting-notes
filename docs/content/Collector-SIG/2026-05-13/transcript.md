SIG: Collector SIG
Date: 2026-05-13
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 01:07 Hello!
**Alex Boten** 01:10 Hello.
**Andrzej Stencel** 01:11 Aang.
**Evan Bradley** 01:11 Howdy.
**Alex Boten** 01:55 I can't believe that there is no other agenda items than… Then the stability pays one.
**Jade Guiton** 02:09 Great week, I guess.
**Pablo Baeyens** 02:12 Yeah, congrats on graduation, I guess is the other topic.
**Andrzej Stencel** 02:19 We're graduated, there's nothing else to do. Everything is now completed.
**Alex Boten** 02:24 It's done. We can now… we can now go on a… on a post-graduation trip around… The world or something.
**Fairly OddParents (ca-wat-brt3)** 02:33 And adopt an otter.
**Alex Boten** 02:35 That's right. That's right, we can adopt an order and debate what to name it.
I guess I will… I will say for the people that weren't in the spec call yesterday, one of the… one of the top items on the agenda for the stable by default OTEP that's being rewritten, was the stability of the collector, so… the Disability Phase 1 project is still very important.
**Pablo Baeyens** 03:22 We figured it out, what, like, 3 years before then?
But it was important.
I'm joking.
**Alex Boten** 03:31 No, that was… that was a previous… that was a previous version of… of the stability effort, Pablo.
**Pablo Baeyens** 03:39 Okay, then, like, 6 months.
**Alex Boten** 03:42 No, again, that was a different… that was a different stability project, Pablo.
**Pablo Baeyens** 03:50 Sometime prior to Tuesday.
**Fairly OddParents (ca-wat-brt3)** 03:56 The original version was called Collector 1.0.
I think that was a catchier name.
**Alex Boten** 04:04 It did have a nice ring to it.
I agree.
Alright, do you wanna… do you wanna kick us off with the high priority issues for 15 minutes, or do you want to talk about the 6 security, pull request, Pablo?
**Pablo Baeyens** 04:30 I mean, most of what I have to say there is just… If you have… input to give this review. We've been discussing this among maintainers, and with the technical committee, and governance committee, and… Well, the intention is for it to apply project-wide, but it is… specifically useful for the collector, I think.
So yeah, if you have input, if you have a security background, please.
Keep your comments, Sarah.
**Alex Boten** 05:02 And I guess… I guess to give a bit more context, the conversation that's being captured in that pull request is specifically around an influx of… CVs and security reports that have been opened against the collector and collector contribib.
And in a lot of cases, people open these CVs with the idea that, you know, hey, you can DDoS your collector if you're sending too much traffic, or if you're sending specific shapes of traffic.
And in a lot of cases, that is completely valid, but this is also covering cases where proper authentication or security practices aren't being followed.
when deploying the collector, so, like, I think what we're trying to capture here is the… Like, those issues can be opened as issues, and they don't necessarily have to be, like, security reports, because we specifically, document, don't put your collector in a, you know, an unauthenticated place to just receive traffic from anywhere, so… I think that captured the context.
**Pablo Baeyens** 06:14 Yep, thanks, expert summary.
**Alex Boten** 06:30 Alright, I guess if there's no… There are no questions. Evan, do you want to talk about config optional?
**Evan Bradley** 06:42 As soon as I can get my mic unmuted. Okay, so, yes, I just wanted to follow up on this. Jad, thank you again for your… really detailed reviews, I think we're in a pretty good place now. I just wanted to follow up and see if either anybody else wants to take a look at this, or if there's anything else, we want to see before we… Get this in.
Just trying to push it along.
**Pablo Baeyens** 07:12 I want to take another look at it. I… I'll do it before end of week. If I don't do it before the end of the week, I guess… Go ahead.
**Evan Bradley** 07:24 Okay, cool. I mean, it's no problem, I'm… I don't… I'm not, like, in a huge rush, I was just trying to keep it moving, since I'd like this to be, finally over with.
Cool. Thank you.
That's it. Next one is… someone else.
**Alex Boten** 07:49 Yeah, I just wanted to call out that, There's a PR open that's currently in the merge queue to add, Evan as A collector maintainer in the core repo, which is pretty exciting.
We haven't had a lot of these, so… Thanks. Thanks, Evan. For contributing and… Yeah, I guess welcome, welcome to the… Maintainer core team once this thing is merged.
**Evan Bradley** 08:20 Thank you.
**Alex Boten** 08:36 Alright, braden.
**Fairly OddParents (ca-wat-brt3)** 08:41 So, the… issue that I linked.
is… Initially, the plan was just trying to introduce a new feature into Exporter Helpler's Elks Air.
Exporter helpers, sending queue batch functionality.
But… It… Turns out that the simplicity of the current batching config is working against our ability to introduce this feature. So we're talking about making some kind of breaking change to the config to make it, in my opinion, less confusing anyway, as well as Introducing new functionality to it.
the SDK, Had an issue opened to change its config as well at the same time in the declarative config, adding batching to the declarative config schema.
So… I've lightly proposed that maybe the collector and the SDK people should just link up and… and decide on what that config should roughly look like, and even if we can't share the exact same, like, literal code mechanism for what the config should look like, we can at least have a very similar config surface, so people configuring batching for an SDK or for a collector.
would look… it would look relatively similar and have similar capabilities. The expectations would be the same, at least as the same as they can be across both. So, if that is of interest to you.
send me a message, because I'm planning to write that up as, like, an OpenTelemetry project proposal. So if you want to be part of that, let me know.
I think that's everything.
**Andrzej Stencel** 10:47 Any comments on Braden's point?
I just have this request to look at the ready-to-merge PRs in core, there are a couple of them, and either merge them or maybe remove and, Let us let the creators know what the next steps should be, right?
And then next is Ravi Shankar.
**Ravishankar Gnanaprakasam** 11:21 Sure.
**Pablo Baeyens** 11:21 one specifically, I'll take a look.
Andre, it was on my list, it's just… there's a lot of things on my list.
**Andrzej Stencel** 11:30 Thanks.
**Ravishankar Gnanaprakasam** 11:35 Yeah, I mean, like, I just opened the 2PRs for some open issues that was there, so… Anyone who has bandwidth can take a look, and… yeah.
**Fairly OddParents (ca-wat-brt3)** 11:58 Looks like both of those PRs are lacking descriptions. I might recommend adding that before someone takes a look.
**Ravishankar Gnanaprakasam** 12:06 Yeah, sure, we'll add that.
**Pablo Baeyens** 13:21 I guess that's everything, Daniel?
**Alex Boten** 13:23 I think so.
**Fairly OddParents (ca-wat-brt3)** 13:27 Agreed.
**Pablo Baeyens** 13:27 Alright, see you on the internet.
**Evan Bradley** 13:30 Thank you, everyone.
**Andrzej Stencel** 13:31 Thanks, everyone.
