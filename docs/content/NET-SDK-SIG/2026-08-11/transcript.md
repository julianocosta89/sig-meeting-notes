SIG: .NET SDK SIG
Date: 2026-08-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:28 Hey, Rajk.
**Rajkumar Rangaraj** 02:38 Hello, Martin.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:39 Rash.
I saw you in the meeting, but you weren't on the call, so I wondered if you'd maybe joined the old one by accident.
**Rajkumar Rangaraj** 02:48 Oh, okay.
Let me share my desktop, I haven't presented for a long time. Let me take…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:06 Sure. I was doing it last week, and I had a bit of trouble because my laptop overheated.
**Rajkumar Rangaraj** 03:10 Yeah, yeah, he just read that in the chat. Okay, yeah.
Hope you're able to see the browser window.
Which I haven't opened.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:30 Yes.
**Rajkumar Rangaraj** 03:32 Okay, let me switch to… I think we… only two, should we give it one or two minutes? Or it's already 7 for…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:39 I'm happy to carry on if you want to.
**Rajkumar Rangaraj** 03:42 Yeah, maybe we will wait for one more minute and see if people are ready to join. If not, we could start the discussion.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:49 Okay, sure.
Did you enjoy your vacation?
**Rajkumar Rangaraj** 03:57 Oh, definitely, yeah. I was with my family, like, I did not… even last year, I took some vacation, but I was working when I was in India. So this time, I was completely out of my system and everything for a month, so it's a good recovery time.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:12 Nice.
**Rajkumar Rangaraj** 04:17 I have an issue with the mouse. I could not see the cursor. Okay, let me use the touch.
burden, yeah.
I think we will start our discussion, Martin. I don't think, anyways, this meeting is getting recorded.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:45 Sure.
So yeah, this one was just, we don't necessarily have to discuss it all now, but while I was adding the Blazor interim tests.
discovered that because Blazor apps don't run the hosted services.
the, like, the bootstrapping of the SDK doesn't run, so you have to, like, manually force it to start up.
So this issue's just recording that fact, and… wondering if we should do anything about it to make it easier to use, so that it just works in a Blazor scenario.
**Rajkumar Rangaraj** 05:26 Like, correct me, on this one. We added a, support for the Blazor recently with the… Even a .NET team has done the contribution. After that, only this is getting supported, is that right?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:44 Yeah, so, I forget who it was, but someone did a pull request to fix the way the threading worked in the.
**Rajkumar Rangaraj** 05:51 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:51 since.
**Rajkumar Rangaraj** 05:52 I think it was good.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:53 directly under Blazor, and Blazor does work in the end-to-end tests now, but compared to running, say, an ASPNET Core app, you have to do… if you want to use the hosting extensions.
it doesn't work by… as quite as simply, and you have to know to sort of poke the SDK to start it up.
whereas infusing it in an ASPNET Core app.
It will automatically happen because of the hosted startup.
Support.
**Rajkumar Rangaraj** 06:25 Probably, I think we should have some solution. If that's a bug, make it simplified for customers instead of they doing this, or everyone writing something like this.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:36 Yeah, exactly, exactly. It's like, if we pull the logic out of the hosted service to have the hosted service just call a method.
And then, if we can't come up with a magic way to have it just work, then we add an API that's… and then update the instructions that just say, if you're using Blazor, call this one line.
**Rajkumar Rangaraj** 06:56 Yeah, I think we should get that done, instead of… this is a… I would not call it as a bug, but I would say it's a feature where we can… we are getting it added here.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:09 Yeah, it's a bit of a sharp edge, but because it needs some sort of public API adding to make it work, unless anyone has any ideas on an alternate magic way to have it just work, then I figured it was best to discuss first before I go… I went off and tried to do something.
**Rajkumar Rangaraj** 07:29 I think it's… this is a reasonable addition. We are… Blazor, anyways, it's supporter, so we can treat it as a first class and provide that support. That's what I believe.
Here.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:41 Okay.
**Rajkumar Rangaraj** 07:41 One only thing is that, if you can find a different name, utilize that.
I'm too much used to this name when it comes to the application inside. It has this… So, just try and see. Utilize a different public AP if possible.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:58 I'll… I'll consult a thesaurus and see if I can come up with something, but if we… if I can't think.
**Rajkumar Rangaraj** 08:04 I'm biting.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:04 Two ways in.
**Rajkumar Rangaraj** 08:05 babe, yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:06 We could always bike shed it in a PR.
**Rajkumar Rangaraj** 08:08 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:09 Okay, cool. At some point in the next week or so, I'll at least put up a draft.
Of this skeleton.
And then we can discuss it separately.
**Rajkumar Rangaraj** 08:20 Sure.
Yeah. Is it fine if I assign it to you, or… because…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:25 Oh, I just did it myself, so yeah, that's fine.
**Rajkumar Rangaraj** 08:28 Yeah, good. Thank you, then.
Let's move on to the, yeah, the PR dashboard for the… I know there are a lot of things to take a look at it, So, I'm seeing a lot of work from you, Martin, like, yeah, how do you want to prioritize? Because we already… I'm finding whichever is simple and easy, I'm just reviewing and moving on.
But, I'm not seeing that label, it's very important or something.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:01 Oh, yes. So, I've been avoiding adding it.
by default, unless something genuinely is important. Okay, good. And then, if something that is… not very important, but it's slightly important, starts to age out, then I'd add it on. So, for example, the one that I think… would be good to get reviewed soon. I'll put a label on it anyway. It's the… there's one about fixing a bug for the Prometheus exporter.
**Rajkumar Rangaraj** 09:32 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:34 All the other… pretty much all the other ones that are open at the moment is… because, Claude recently launched the newer models.
I did some scans of the repo, looking for, like, relatively low effort, high-impact performance improvements.
And that's where all these are coming from, and they're just sort of… they're small-ish, but some of them aren't… they're, like, maybe a couple of hundred lines, the biggest one, but they're not… they're nice to have, just because they're performance improvements. There's nothing, like… You know, if this makes it 15 times faster, or anything like that, they're all micro-optimizations, you know, would add up as a body of PRs, rather than individual ones.
**Rajkumar Rangaraj** 10:21 Sure. I'll go ahead and sometime around the end of this weekend, the week, I should have some bandwidth. I'll try to go and cover most of the… apart from the API, OTLP and Expo, the Prometheus, anything is there, I'll try and finish it off.
maybe these things I'll park, because this I have to just read the spec and all that. So, I'll just keep it… oh, this is also… propagated portfolio, so I can take a look at this as well.
Only this one had to park it for some more time, If a review is important, mandatory needed from me. And I know I need to prioritize this as well, I believe. This is… you… it has your approval, I think.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:06 I made a few more comments on it, since Julius updated it overnight.
But, but yeah, I think even if he, like, does everything I've left feedback on, and I would re-approve it, because you've had a lot of questions about this one, I sort of deferred to you to do, like, the final approval on that one.
**Rajkumar Rangaraj** 11:28 Okay.
I'll put on the next one, the config, it has the Alan's approval,
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:35 Oh, yeah, so Alan had one comment, and I asked… I asked him to just check that he was happy with what Steve had done to address that, but otherwise, that… that one's ready to merge, in my opinion.
**Rajkumar Rangaraj** 11:49 Sure, I'll also take a glance through this one as well. But don't, you don't need to wait on me. If it is ready for merge, go ahead and merge it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:59 Yeah, it's just because that one's declarative config, and it's, like, a relatively big feature. I figured it was best to have at least two people happy with that one.
**Rajkumar Rangaraj** 12:08 Yeah. Anyways, I think this is guarded, I believe, if I understand correctly, so I don't have a very big concern. It's getting…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:14 Yeah, we, I've also had some feedback on it, and it's under its own, MinVer tag at the moment.
**Rajkumar Rangaraj** 12:22 Yep.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:23 And Steve isn't planning on wanting a version in NuGet.
Anytime very soon, so having that merged won't mess up releases of the other packages.
**Rajkumar Rangaraj** 12:36 Yeah, that's what I found, like, I skimmed through that earlier, so I don't have a very big challenge, that getting in.
So… but I will do another glance to see if I'm finding anything in that. Just use some agents to review and give me some hint over there, if anything is there.
I think apart from that, I think we are good, I believe.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:02 Yeah, I've also… they're under draft at the moment. I'm also trying to fix… there's some flakiness in the CI at the moment.
**Rajkumar Rangaraj** 13:09 Yep.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:09 it's a bit, trial and error, because I'll open a PR, It'll, like, pass 10 times.
And then it will get merged, and then it'll fail.
So there's a couple of things I'm trying to fix up there, but I'll move them out of draft once. I've got it to pass more times than 10 in a row.
**Rajkumar Rangaraj** 13:30 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:30 But it might not be a guaranteed fix.
**Rajkumar Rangaraj** 13:34 Sure, I think this is a good strategy, to have it in draft, and then… there is no… at least it's… I need to appreciate you are… you are taking a stab at it and trying to, see… improve that one, so it's a…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:48 Yeah, it's just sort of like that… the minor annoyance of having to rerun jobs.
Yeah. Because I think we've got to the point now where the SDK and the test base is so big.
But we're sort of, like, starting to fight probability.
Yep.
**Rajkumar Rangaraj** 14:05 Let me move on to the contrary, words, I think.
I think this should be ready for March. It has a,
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:17 So.
**Rajkumar Rangaraj** 14:17 Thanks. Hi.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:18 That one… Alan… Alan had a small bit of feedback on it that I've replied to.
**Rajkumar Rangaraj** 14:23 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:23 And then, I think Piotta had Codex look at it, so I've done some more changes to that PR, so I've left that for a re-review.
**Rajkumar Rangaraj** 14:34 Okay. I want to speak a little bit on these components, with you. The one collector and the Geniva.
the reason Geneva change that got incorporated, caused a massive sales across Microsoft with different teams.
So, the idea is, this has happened with the last few releases, so, what we plan to do is, like, we just don't want to… because as more teams are complaining, we don't want to add any new features to it, or any change to It for the next 3 months, based on our retro.
So, we want to pass any changes to it, apart from the normal package upgrade and the open telemetry updates. So, we may need to just put a pass on this one. We may not be able to take… this one at this point. Or if there is something in Geneva, we have to pass that as well.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:36 Yeah, that, that one came up through, the co… Co… Yeah. Scan.
**Rajkumar Rangaraj** 15:44 Yeah, I asked one…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:46 I can… A bug. It came across as a bug, not a feature.
**Rajkumar Rangaraj** 15:50 Yeah, I understand that, because I asked you that question and you answered that also, so I went back. So, this… all of these things does not directly send the data to the ingestion endpoint. Rather, they have their own specific agent sitting there and all that.
So, whenever we do something like this, it needs to be evaluated against that and all.
And there is a very few subject matter experts, on these areas. So, we need to take and get it to them and do the end-to-end evaluation and all that. So we are just formalizing a process on that. So until that, based on whatever has happened and the retro happened within here, It's a temporary measure to pass and keep it for a few minutes.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:37 Okay, that's fine. But yeah, I just, I just, I was… yeah, because I didn't see that you replied or reacted to my reply, so yeah, it was just, as far as I know, it's a bug, it's not a feature, because, yeah, because outside Microsoft, we don't really have any visibility on what you do with Geneva or Collection Collector, so, like, I wouldn't be trying.
**Rajkumar Rangaraj** 16:59 I hate that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:00 new features.
**Rajkumar Rangaraj** 17:01 Yeah, we… I really don't understand why these both components aren't made open source, so… but, yeah, but it's already there, but, Yeah, apart from that, I think… I… normally, I don't get into the Elasticsearch, unless if it is some… it's just updating a semantic convention, I think I can take a look at this and unblock.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:35 And then the third one, I've just been… as, Reznas and Steve are doing most of the work on the OPAMP stuff, I've just been waiting for Steve to approve that one, and then I'll give it a skin read and merge it, if he's happy with it.
**Rajkumar Rangaraj** 17:52 Yes, that should be good to go then.
I think the… this one is something I wanted to take a look at it. I am much more interested, and I was spending a lot of time earlier on this one.
So, even if it gets… this is getting in the contrib repo, so I don't have any problem getting it merged, but I'll be spending some time, even if it merges also, I'll take a look at it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:20 That's cool, that's cool. With that one, the more the merrier, as far as I'm concerned.
**Rajkumar Rangaraj** 18:25 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:26 Because, yeah, Piotta had, Codex look at it and left a bunch of feedback that I, addressed yesterday.
So that's also why I've not merged that one, even though Alan's approved it.
Okay.
**Rajkumar Rangaraj** 18:40 I know.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:41 If it does… if it's, like, there for, like, another week with no feedback, I might merge it anyway.
**Rajkumar Rangaraj** 18:46 Sure. The thing is that it's a good addition, I think, and we can iteratively work on it. I don't think we need to just keep there and, yeah. I'm just gonna skim through it, because I spent a lot of time to add this.
And it's good to see that future coming here, and I hope that if it works well, we should move this to the main repo.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:10 Yeah, the plan was… when enough time, however long that is, elapses once it's got a first release, and it seems to be working, then we'll work out extracting it from there and putting it into the core SDK.
**Rajkumar Rangaraj** 19:24 Yep.
I think the other one is over.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:29 Actually, an interesting one to possibly discuss is the one about the HTTP reduction.
So I left a comment on that by the person who opened that today. It's adding an experimental NVARD to, like, say which parameters to redact and the others don't. However, it raises a good point that Because the… for .NET 9 and later, the telemetry's built into the runtime.
We can't fully deliver this feature.
without .NET also implementing it, unless we… like, reintroduce Us and the runtime will do stuff?
**Rajkumar Rangaraj** 20:12 Yep.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:13 And then, I've linked near the bottom to, some pull requests and issues in the .NET repos. And yeah, I think at this stage in the release cycle.
**Rajkumar Rangaraj** 20:24 I.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:25 12.
**Rajkumar Rangaraj** 20:26 Yeah, I think this should work in the reverse order. If such feature is needed, it need to happen in the .NET, and then we should be considering that. Adding anything here is going to cause a customer's confusion. Hey, it works in one of the framework and not in the other.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:40 Yep.
**Rajkumar Rangaraj** 20:40 So, yeah, we need to let the author know about that, yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:46 Yeah, something that might be interesting to discuss with the .NET folks at some point is.
**Rajkumar Rangaraj** 20:52 Yep.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:53 from… doing some stuff on ASP.NET Core this year. I've noticed a theme that comes up in the issue sometimes is a bit chicken and egg. It'll be .NET doesn't want to implement a semantic conventions feature, because OTEL doesn't.
But then OTEL doesn't implement it because we think it should be built to .NET.
So it ends up that no one.
**Rajkumar Rangaraj** 21:16 That is amazing.
I think if there is an issue right up, I can reach out in the ASP.NET Core repo. I can reach out to the ASP.NET Core PM and speak to him about that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:31 Yeah, I don't think it's any one specific feature, it's just, like, a theme that I've spotted in a couple of issues that are like, oh, it's not in the SDK, so there's no rush to do it in the runtime unless people want it, but then it's like…
**Rajkumar Rangaraj** 21:43 And, G.
Yeah, if you see those challenges, please bring it up. I can, being in, sitting here in Microsoft, some connection to the ASPNet Core and the .NET team, like, I can just have a discussion with them to see how we can avoid those kind of like, a confusion. We should have a very, very good clarity. When we worked with .NET team, we, or when they came to the OpenTelemetry, we had an agreement, they will be very supportive and all. So, this is going against that.
It's going to create a failure in both the places. Instead of APIs being in the .NET layer and as .NET is not listening to it, we might go and do something, within the OpenTelemetry API layer itself, which is not the right thing to do. We need to, aligned to the agreement which we had, and if needed with them, we need to bring them to the SIG for a discussion here, as the .NET is slightly different than any other SIGS.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:45 Yeah, because I think it's, like, a couple of… a couple of the issues as well. It's the sticking point is getting… an agreement on an API shape, rather than the effort, because I think a lot of the things that are currently open that we would like in .NET, like, me, you, Piotto could happily do a PR to actually implement the feature, so they… obviously, there's the ongoing support burden once it's in.
But, a lot of these things are just stuck waiting on someone to say what the API shape should be.
And they just get stuck in the backlogs.
**Rajkumar Rangaraj** 23:18 I think if you can get the list of that. Earlier, we used to maintain a list. I've been slightly inactive for the past few months here, that's why I could be missing those stuff. So if you could help me get those things, we can start a discussion and see if we can Chain things around for us.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:40 Yeah, I'll have a dig around and see if I can find the other ones, but I've linked to the two… query stream redaction ones, you know, comment on this issue.
up here.
**Rajkumar Rangaraj** 24:00 Cool. Are there any other topics for discussion, apart from…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:06 I don't think so.
I can't think of anything right now.
**Rajkumar Rangaraj** 24:13 Cool, let's go back to the participants. Anyone has anything? Any other things for discussion? If not, we could add it.
Cool, then.
Thanks, everyone. See you next week. Bye.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:27 Bye.
