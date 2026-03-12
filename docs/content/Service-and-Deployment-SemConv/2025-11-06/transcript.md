SIG: Service and Deployment SemConv
Date: 2025-11-06
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/UJTwrmyvT42iTj_-AVsnbh7WrpZiOgGOxwE0P44pDyNIyMCSdy5bN3SUH0Lcddff.FU6IvvTLRois8t8Q
============================================================

## Zoom Recording Transcript

**Janhvi** 02:17 Hey, everyone.
**Bakhtiyar Garashov** 02:27 Hey, hello.
**Janhvi** 03:14 Feel free to add your points to the agenda for today. I've added a few things already, but if there's something you would like to add, please go ahead and add that to the doc.
Heydraska.
**Trask Stalnaker** 03:31 Books…
**Janhvi** 04:33 Let's give a minute more, and then we can get started. Josh won't be joining today. I think he's busy with a few other things.
Okay, let's get started. I'll go through the agenda for today.
The first thing I wanted to discuss more from the logistics side of things was, I saw on the Slack channel, so we have a bi-weekly meeting, right? The one that's… this is the one that happens, Thursday night for India time and morning for the US time zone, whereas the other one, which is the Asia-friendly time zone. I think, there's been asked to change that time.
This is the preferred option so far. I wanted to check with folks here if you guys… I know… I don't think anyone from this group joins the other call, but wanted to check if you guys have any preference, on this.
If not, Traskal probably need your help to reschedule the other invite. I would… I don't have the access to that one.
**Trask Stalnaker** 06:32 Sure, I just opened a community issue.
**Janhvi** 06:36 Is that the board or something else?
**Trask Stalnaker** 06:42 Oh, the community repo, I will give you the link.
Yeah, so you can just open an issue there.
The asking to change the… Tying.
**Janhvi** 07:01 Okay, if you could just add the link here, and offline I can, I can raise an issue for that.
**Trask Stalnaker** 07:07 Oh yeah, I put it in chat, but I will put it in the doc.
**Janhvi** 07:11 Perfect, thank you.
I'm taking my hair.
Next, I think this is something we discussed, last time as well, and I wanted to see how do we… how do we take this ahead. So, a quick TLDR for everyone. So we are trying to make a few changes to the service entity that we have.
And you guys can open… let me quickly open it up… This is a draft PR that Josh had shared earlier, and this is how the relationship now looks like. So we have a namespace, and under the namespace, you could have names, and finally, the instance.id. So as part of this PR, Josh is trying to change some of the comments, descriptions around this, that it's very clear on what the namespace what name is supposed to mean, and what Dean Stan's ID is supposed to mean.
I'll work with Josh, I think he doesn't have the bandwidth, so there's some comments he doesn't have the bandwidth to resolve them, so probably I'll work with him to… to get them resolved, but I wanted to check with the group to see if there are any high-level concerns or thoughts or questions on this PR, and how do we take it forward from there.
**Trask Stalnaker** 08:40 Sure, I was just waiting for the… I left comments and was just waiting for all the comments to be… Reviewed before doing the… and then I'll do another pass.
**Janhvi** 08:56 Got it. I think I'll talk to Josh, and maybe I can help him, get the comments resolved while he's out. And then I'll ping you, probably on the Slack group itself, I'll ping the PR again, and, you can take another look.
**Trask Stalnaker** 09:11 Sounds good.
**Janhvi** 09:12 So, to ask a quick question here, once we, let's say, submit this, we are right, the attributes are still not going to be stable, so what would it take to get them stable in Hotel?
**Trask Stalnaker** 09:25 first, it would be a PR to mark them as RC.
And… we need prototypes, minimum 3 prototypes, but I think for, you know, the service ones, There's probably… Well, service name, obviously… oh, service name is stable already. So, yeah…
**Janhvi** 09:56 This is not stable, right?
**Trask Stalnaker** 10:00 Which one?
**Janhvi** 10:01 Namespace?
**Trask Stalnaker** 10:03 Right, right. So, we would need, to cite The prototypes, like, what languages and or collector components implement it already?
And then we can… Raise a PR to mark it as RC…
**Janhvi** 10:27 Okay.
And where can I look at what all languages are supported today, and what all prototypes will be required for the namespace thing?
**Trask Stalnaker** 10:36 You'll have to dig through the repos to find that.
Usually, like, if you do a GitHub search at the org level, for, like, service.namespace, you know, that… that'll… get you to… various components. You can also, if you're having trouble finding, you could post in the Hotel Maintainer's Slack channel.
Asking for… help basically anybody who can point to prototypes in their languages, and or the collector is a whole different… a whole ex… Big area, which is also important.
So you may have better luck you know, looking at the repo directly, but then also if you need, you could ping on the collector Slack channel.
**Janhvi** 11:35 Got it, sounds good, because I think that would be the next, logical step for this. Once we have the draft, we are submitted, we should see how we can start working on the prototype and then get this stabilized.
**Trask Stalnaker** 11:51 Yep.
**Janhvi** 11:54 Okay, Moving on to the next one, so yeah, there is an issue raised, specifically for the criticality attribute, and this is one of the attributes that we have as part of the SIG as well.
At least in Google, we have a lot of use cases, and even on other cloud providers, we have a lot of use cases where we'd want to stabilize the, the criticality attribute. So maybe we could discuss about that, and see if… what the group feels about it.
I see Bhagtar on the call, do you… do you want to go ahead and talk about it?
**Bakhtiyar Garashov** 12:33 Yes, hey, hello. I'm glad to be here.
Maybe one sentence about me. I'm back there, I work as a DevOps engineer at Zendesk.
And over the last… maybe 2 years, I was mainly working with moving to open telemetry.
Regarding the semantic convention, we have a… A really, important use case for this.
We invested heavily into, tail-based sampling.
And, in order to apply different sampling rules, we come up with a custom span or trace attribute.
Which is critical, then?
And, then I… yeah, I was looking into option to, propose this as a… part of OpenTemmetry semantic formation project.
And, yeah. Basically, that's all.
**Janhvi** 13:36 Sounds good, thanks for the daily, Bhagtiar. I think even, the use case that we have in Google Cloud, so we recently had done, like, a survey where we went ahead and talked to all the end users and saw what all type of resource attributes that they commonly used, and criticality was amongst, like, the top 5.
That people use as attributes. Mostly in our use cases, they kind of add it for managing resources at scale. They add policies on top of it. Example, they, they tag their resources with difficult, different criticality level.
And then they can, can add policy values to say, hey, give me all the resources which, let's say, have a critical… a high criticality tag associated with it, and then they can have access restricted to that, or if they want to see billing for only their mission-critical services, they can do that via that attribute. So yeah, I think I agree that there is definitely use case for that, and we should see how we can stabilize that in the hotel space.
Trask, folks on the call, any comments, thoughts on this? Trask, I don't know if this has been earlier discussed.
In the hotel space or not, do you have context there?
**Trask Stalnaker** 14:55 Not that I recall, I think the same thing kind of goes for prototype, for introducing… even introducing it as an initial PR, it's helpful to have at least one prototype. We don't need the three that we need for stability, but just one to kind of show how it's used in instrumentation.
I think it's a little tricky in this case, so I don't know, Josh.
Probably would have more… thoughts on… What's appropriate from a prototyping perspective for it.
**Janhvi** 15:45 What do you exactly mean by that? That's tricky in this case. You think it's going to be difficult to show how, this would work end-to-end specifically for this attribute?
**Trask Stalnaker** 16:00 Only because it's… I think it's just user-driven. I don't know if there's, if there's a standard Kubernetes attribute that we can map, that we can show how it's mapped, that would be a good prototype, you know, how… Basically, some kind of standard instrumentation that we would build in The open telemetry for it, versus it being just a purely user-driven tag.
**Janhvi** 16:34 Got it. Bhagda, by any chance, would you know if there's, like, a corresponding Kubernetes attribute for this?
**Bakhtiyar Garashov** 16:42 I'm not aware of any, actually.
**Janhvi** 16:48 Got it. I think maybe if you could take that AI, even I can also look into it and see, if there are any other places where this is already being used, right, and what are the naming conventions there? We can kind of start from there.
And offline, I can talk to Josh, as well, and see what he thinks about it.
**Bakhtiyar Garashov** 17:09 Okay.
**Janhvi** 17:12 I'll probably take that as an AI.
So to ask a question for you, when we're trying to add new attributes, if it's, like, a specific user-defined attribute and we don't see a similar attribute in the open source world, let's say in Kubernetes, do we have precedence of such attributes in Notel?
Today?
**Trask Stalnaker** 17:43 Probably.
I'm not sure. I would… I mean, it's probably going to need to be… And, yeah, I don't know. Sorry.
**Janhvi** 17:54 Got it, got it.
Okay, and yeah, I think I'd request everyone to maybe take a look at this issue and leave comments on it and see if we think this is, like, the right fit for a hotel or not, and if you want to change the naming conventions, we can take it from there, and then we can look into prototyping.
Okay, I don't have anything else on the agenda for today.
Anyone else, anything you'd like to discuss?
I can quickly look at the board as well.
This is the one that Josh is already driving. Ability to specify the purpose, category, function, parts of a service.
Yeah, this is one of the attributes, I think, that Yoshi had recommended. There's no use case of it. I talked to Yochi last time, I think he's going to add a few use cases to this one and see if this is something that really makes sense.
This, I think we had discussed earlier.
Recording of deployment events.
The ability to recall.
Okay, I think deployment, we've not talked about it yet, so maybe next time we can talk about deployment.
Service.instance.id… Oh, I see, there's an issue for stabilizing the service.instance.id.
So I think trust the prototypes that we were talking about, I'll take a look from here, I think this would help. The SDKs are already mentioned there.
I think this should be a good starting point.
And I think this is the one that… We had just discussed.
So, Trask, for this one, should we, like, send this out to the wider community as well? Or, like, how do we go about it? I'll talk to Josh as well.
To see what he thinks about it. But, in general, for an attribute like this, what is the usual recommended process?
**Trask Stalnaker** 20:50 I mean, this group, this SIG, if we are taking it as part of this SIG's work.
Then we can, you know, propose it.
basically, as a PR… get SIG approvals on it, and then it will go to the general SEMCOM approvers.
**Janhvi** 21:10 Sure.
**Trask Stalnaker** 21:10 Review.
**Janhvi** 21:12 Yeah, so this is one of the, the three, milestones that we had committed as part of the SIG, right? The first one was, stabilizing attributes in service and deployment, and along with that, we wanted to add a few new attributes So criticality was one of that, one of those new attributes that we had committed for. So as part of this SIG meeting itself, I mean, not this meeting itself, but in general, as part of this group, we'll have to decide What we kind of think about it. We'll have to figure out an opinion, and then see how we want to take this forward.
**Trask Stalnaker** 21:53 Sounds good.
**Janhvi** 21:54 Oh.
Okay.
Cool, I don't think we have anything else. Anybody, anything else that you'd want to discuss?
**Kartik** 22:09 So, I just had a quick question on that board that we were looking at, right? Like, so what is the… how do issues… Get added to that board, Is it done by someone manually from some other SIG, or, like, is anyone kind of looking at… all the issues in OTEL, and then kind of reassigning them to the different boards, or… So I was just curious.
**Trask Stalnaker** 22:32 Yeah, generally the semantic convention maintainers try to triage things. There's a lot of issues, and so a lot of things don't necessarily get triaged properly. So if you see something that you'd like added to a board, just ping on the issue.
**Kartik** 22:52 Okay, okay.
So there's, like, a general entrage list somewhere else, and… It has to be manually moved from there to the various boards.
**Trask Stalnaker** 23:02 Yeah.
**Kartik** 23:02 Okay.
Okay, got it. So, Janvi, maybe occasionally we should probably also look at the… untrage list, and kind of see if any of them looked like something that belonged to the Charter of the Sick, and… Make sure we have the, you know, the latest set of issues that we're looking at. We can maybe work with Josh also on that.
**Janhvi** 23:22 Yeah, yeah, I think that's a good point. Up until now, we've just been looking at the issues that are already triaged, and I think you're triaging, like, for example, in this case, Daniel Liddert, he's part of the GC or the TC committee, I'm not very sure. But I think good idea. I'll work with Josh to see if where can I get that untraged list.
And we can start looking at it.
**Kartik** 23:45 Yeah, cool, thanks.
**Janhvi** 23:51 Okay, alright, if there's nothing, we can probably conclude the meeting.
Thanks, everyone.
**Trask Stalnaker** 24:00 Alright, thank you.
**Kartik** 24:02 Oh, thank you.
**Janhvi** 24:02 Like.
**Trask Stalnaker** 24:02 I…
