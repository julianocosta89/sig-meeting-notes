SIG: JavaScript SIG
Date: 2026-10-07
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:08 Hello.
**Trent Mick** 00:10 Hey, just you and me, let's fork this thing.
Called Closed Telemetry JS.
**Marc Pichler (Dynatrace)** 00:17 will.
**Trent Mick** 00:17 Anyway…
**Marc Pichler (Dynatrace)** 00:18 Yeah, close telemetry.
Fun.
We can we can change the name of the NPM org maybe too.
**Trent Mick** 00:32 Right. Yeah.
Gotta think of something there.
Here, Jennifer.
**Marc Pichler (Dynatrace)** 00:38 you.
**Trent Mick** 00:40 Were you away for a while.
**Jared Freeze (Palo Alto Networks)** 00:41 yeah.
**Trent Mick** 00:42 Vacation or something?
**Jared Freeze (Palo Alto Networks)** 00:44 Wedding, and then doctor.
Okay.
You're a little out of it.
Not my little, yeah, high school friend.
**Trent Mick** 00:54 Yeah, okay, cool.
**Jared Freeze (Palo Alto Networks)** 00:55 So…
**Trent Mick** 00:56 That's more fun. Well, okay, I shouldn't say it that way, but it's fun.
Can be.
**Jared Freeze (Palo Alto Networks)** 01:01 Less work, for sure.
**Trent Mick** 01:04 account.
**Marc Pichler (Dynatrace)** 01:25 Let's wait a few more… Seconds, and see if anybody else tries to see… David is also here.
Hello!
Alright, I guess we can get started. First topic of the day… Just an announcement… Probably everybody is aware already, We did release a new SDK version, that's mostly to make the, migration possible for SDK Trace web users to the new SDK Trace package.
Thank you, Trent, for backporting the changes and making that happen.
And other than that, we also have a new pre-release, for API, SDK and experimental packages.
with the development one suffix, thanks to Trent and Hector for, getting the API changes in.
the any value change and the logs API change.
So that's now in there.
All right, that's it for that announcement.
Moving on to the next topic, Trent. I have one on here.
Looking for browser reviewer.
**Trent Mick** 03:07 I looked at that, looks the same to me, but oh boy, do I have… What's it called?
5, When you don't think you belong.
**Jamie Danielson** 03:16 Imposter syndrome.
**Trent Mick** 03:17 Yes, on the browser, anything browser spec, but it looks the same to me, I'd like a browser personal one.
Looks like the event is being put on.
Oh no, wait a second, this is a different pier. Oh no, no, this is it.
Yeah.
That thing ran with a page hide listener on document, which doesn't exist, it's actually on Windows, so it's probably doing nothing.
**Jared Freeze (Palo Alto Networks)** 03:39 Yeah, this shouldn't even be there.
We… it's not… it's not part of our, baseline support. It should be only visibility.
There's a lot of reasons why this tends to get ripped out, so… We will do that.
**Trent Mick** 03:53 I'm glad I asked him.
Yeah, from the description, this was added as a fallback for Safari, because Safari is not doing the visibility changes I read, or something like that.
**Jared Freeze (Palo Alto Networks)** 04:03 Yeah, it's from 8 years ago, so we're not gonna do it.
**Trent Mick** 04:12 Imposter syndrome was accurate.
**Marc Pichler (Dynatrace)** 04:20 Alright, I guess that's it for that topic. Then let's move on to the next one.
No.
**Jared Freeze (Palo Alto Networks)** 04:28 Yeah, so this is, what we had talked about previously.
I asked for a review. I think it might be more of a collaboration at this point, because… I did a lot of testing. I think… I figured out most of what we need here, Based on, like, the NPM docs and what they recommend, for kind of the new way to do things.
But, yeah, if anybody has any very specific You know, experience here, it'd be nice.
it's the same change over and over. Like, it looks super long, but basically you just only need to check one package JSON. So if anyone wants to chat about it, Slack is probably the best place to do that. You can also comment here.
So… I don't know, I don't think there's another way to preview, outside of… merging and cutting to development. So I'm going to end to unpack it and use it at my day job.
and figure out if it works. Hopefully it does, and then I can get back to everybody. I can do that today, because I know we're kind of on the time crunch here, but Yeah, just looking for feedback.
**Marc Pichler (Dynatrace)** 05:46 Thanks for working on that. I didn't have a look yet, but I will make sure to prioritize this.
In the next few days.
Okay.
**Jared Freeze (Palo Alto Networks)** 05:57 Yeah, there's a few… I will say, there's, like, 3 or 4 other PRs that are in draft, you'll see under related. What it actually does just to give a little background, this is all here, but I'll just say it real quick so it's in your head, is that the surface for browser and the surface for Node are not the same.
And we were relying on types to direct people to like what was available and what's not available. The truth is that never actually happened because most people rely on code editors.
And the code editor was never aware of the browser types, because it only ever looks in the source folder. It actually doesn't even look at the ESM types, it always looks at a common. So, there is another.
portion of code that actually makes the services the same. What it means is that Node takes on batch… or.
options, like Document Hide, which is truly only web, but if you want to do this, you have to align them.
Or we need to do something else, like have another subpath export. The way that this is refactored, I got rid of all the slash platforms and all the slash platform slash node and platform slash browser to do this, to have a shared surface. So… Just approving this and merging it, this is really for discussion, just so everyone knows. And then that test right there, there's a bunch of these platform surface tests, it does exactly that. It runs through the type and makes sure that the type for browser that's published And the type for node that's published have the same public surface.
Because of this swap at compile time.
But this also makes all the editors happy, and it actually aligns all the types properly. Well, I say properly, but it's, like, in the way that all the tools are written.
So.
There's a lot there.
**Marc Pichler (Dynatrace)** 07:55 Yeah, we had a lot of these, and I think we've since gotten rid of a bunch of them, but there were a few ones that stuck around, and those are the ones that you've been working through. So we're kind of… or I I at least was somewhat aware of the issue. Thanks for tracking all of these down and aligning them. I think that's the way to go, anyway. They I don't know exactly how it ended up in that state, but, like, we just had to carry it forward, for most of the browser… or, like, most of the… OTRP exporters. I think they are the worst offenders, in there.
**Jared Freeze (Palo Alto Networks)** 08:40 Yeah, those were the ones that needed the most work. I will say, I think that we got lucky by coincidence, because when you're building browser instrumentation, nobody happened to override, like, in it an instrumentation base, even though that's available in Node, but not browser. So technically, it was always using Node.
It… it… actually, no one was able to use browser, it's unreachable, but… no one overwrote it, so nobody noticed either. So, like, technically, there's an in it sitting in every browser instrumentation. It's just unused. So, like, all that stuff got aligned, so it changes things quite a bit.
Anyways, you'll see.
**Marc Pichler (Dynatrace)** 09:21 Yeah, thanks for working on that.
I'll have a look at your PRs, and let's see… We can get them merged quickly, and then we can also look into publishing a pre-release.
**Trent Mick** 09:38 Oh, Jared, if you get a chance today, I made a merge conflict by moving SDK logs from experimental, like, a half an hour ago, so both of those PRs will need a brief update.
**Marc Pichler (Dynatrace)** 09:57 All right, any more questions about this change?
Moments.
Excellent.
1, 2… Next one. Trent.
**Trent Mick** 10:16 Okay, so that's an intentionally… Well, again, words are failing me. I need Jamie to give me all my diction here, but anyway, this… I am not proposing changing anything right now, but this is just socializing the idea of us eventually Pardon my French shit canning.
Gaxios and GCP metadata usage for our GCP resource detector. It pulls in, like, 7 gazillion lines of design just so we can make a single HTTP request to get some data.
And it is not… as far as I can tell, it's not really being maintained right now. So there are kind of vulnerability things that probably don't affect us, but if you're OCD and want to clean up all of the vulnerability warnings on the repo, you run into… A problem with these ones.
Also, the Gaxios usage, I think, is one of the complications that we had of… loading stuff before instrumentations can instrument the thing, so it causes some issues for us there. So it's complexity that, frankly, I don't think we need.
Eventually.
as I said, I'm socializing the idea. Eventually, I'll probably come around to proposing.
simplifying the GCP detector to not use any of this stuff, even though it's the Google, kind of.
Here's the way you do it, so… see if that's… Anyway, that's the idea.
If that makes sense.
**Marc Pichler (Dynatrace)** 11:43 for removing it, because I had the same experience that you now described with, trying to get rid of the vulnerability, alerts in the security tab, and… Not being able to, because it wasn't being updated and stuff.
So, I think we also had some.
Some issues being opened where people asked for, that To be updated, and… I'm not sure if these… I think we were able to address these, because there was actually a way to update them, but, yeah.
I'm for removing it, so…
**Trent Mick** 12:26 Okay, cool.
**Marc Pichler (Dynatrace)** 12:27 Looking forward to it.
**Trent Mick** 12:31 I kind of get the impression that looking at what Gaxios does is, like.
Reading the full… wow, what happened to your screen? Reading the full.
Google SRE book on how to design client libraries and stuff like that, which is a little bit more than we need to make a local HTTP call for the GCP metadata. Anyway.
**Marc Pichler (Dynatrace)** 12:50 Yeah, agreed.
Alright.
Moving on to the next one.
**Trent Mick** 13:06 So, the last… I added an issue to the logs… Ga milestone. Since we were starting this long process of stabilizing it, there was a change in the spec.
for the… this part of the spec is still in development on logs, so technically this could happen after we GA it, because we could break this part of it, but we should… we should do this update. I opened an issue for it, and someone opened a PR, so… Just FYI to people, if someone wants to review that, go ahead, otherwise I'll probably get to it soon.
**Marc Pichler (Dynatrace)** 13:38 It's for, looking into that again and opening the issue. I just had this I just checked out this PR before the meeting and hoping to review it soon.
So, okay.
**Trent Mick** 13:54 Cool.
**Marc Pichler (Dynatrace)** 13:56 I guess we can see if we can merge that in and include it in the next pre-release as well. So that everything's sorted out there.
Come.
I think it would be good to have that in before actually releasing 3 to do so.
So we can also add it to the… Logs, Api milestone or logs. Sdk milestone.
**Trent Mick** 14:26 Yep, the issue for it is already, but yeah.
**Marc Pichler (Dynatrace)** 14:28 Oh, okay.
All right.
**Trent Mick** 14:35 And then, not an agenda item, maybe we could look at the remaining 3.0.
definition.
**Marc Pichler (Dynatrace)** 14:43 Let's do that.
**Trent Mick** 14:49 Okay, so… Four of them that are about SDK Trace Star, and the last one.
Are all just remaining dock issues.
Since we just got the latest 2.x release, all of those can be removed in the 2.x series, so I… I have, like, waiting draft PRs for most of these things that couldn't fully do the job because we hadn't had that 2.x release, so this week I'll have PRs to update all those things, so we'll be able to close all those.
Soon.
And then… At least, mostly just Jared's. Sorry, go ahead.
**Marc Pichler (Dynatrace)** 15:27 Yeah. One, update on that, I today took some time to look into the demo app thing, and… have a PR for one of these services already. I will look into the React Native one.
Later, because I have… It needs a lot of tooling, and… I have it installed, but it's outdated, so I just need to update stuff and get it running again.
But, yeah, I would take that over if that's okay with you.
**Trent Mick** 16:04 Yeah, that's totally cool. I think I had one to… A different part of… oh, that's the demo.
Can't remember if I had something started there.
Sorry.
Not, maybe, okay.
I'd had a local start at it, but I'll take a look at your thing.
**Marc Pichler (Dynatrace)** 16:33 Thank you.
**Trent Mick** 16:34 Cool.
**Marc Pichler (Dynatrace)** 16:36 I think I also approved your PR on… OpenTelemetry IO for this.
It's changed here.
**Trent Mick** 16:50 Yeah, I looked in a few days to show and get back. I'm not even sure how to test it.
**Marc Pichler (Dynatrace)** 16:55 Oh, looks like.
**Trent Mick** 16:56 can.
**Marc Pichler (Dynatrace)** 16:57 One of the… Docs maintainers already approved it, so…
**Trent Mick** 17:02 Okay, I'll call it that parking code.
**Marc Pichler (Dynatrace)** 17:04 I had a look at that and tried it out, and it seems to work fine. This is also very similar to the front-end changes in The demo app, so…
**Trent Mick** 17:14 Yep.
**Marc Pichler (Dynatrace)** 17:15 Works okay.
**Trent Mick** 17:16 Okay, so my understanding from looking at this is that OpenTelemetry IO docs themselves are instrumented with OTEL JS, and they're sending to some backend.
Has anyone looked at that back end? I vaguely remember.
Some discussion of it somewhere, but I don't remember. Okay, I think you need to request access to get… I'm not even sure where they're dumping it.
Okay.
**Marc Pichler (Dynatrace)** 17:40 I think it goes to Honeycomb, if I recall correctly, I saw.
**Jamie Danielson** 17:44 Was it? We used to do a thing for Ruby, but… How do we get access to that? You think anyone knows anyone at Honeycomb?
**Trent Mick** 17:53 I'm not totally assigning this to someone yet.
**Marc Pichler (Dynatrace)** 17:55 business.
**Jamie Danielson** 17:56 Okay, good follow up.
**Trent Mick** 18:14 Okay, so then the last real one remaining is Jared's, which we've already discussed, I think, so we're probably doing pretty well on 3.0.
And then working through those deprecated calls.
**Marc Pichler (Dynatrace)** 18:25 This, I think we can also do after publishing.
deprecating.
**Trent Mick** 18:32 Yes.
**Marc Pichler (Dynatrace)** 18:33 packages, so…
**Trent Mick** 18:34 Agreed.
**Marc Pichler (Dynatrace)** 18:35 That can be a follow-up then.
I think… A few things that we still need to look into is, starting a PR for Contrib.
with the experimental, packages, so that we have the PR ready to be merged once… Once we get to releasing, so that hopefully we can get the contract release out on the same day.
And also, I think we might need to look into doing the same in the browser repo.
Just to make sure that there's no friction there for updating.
With the new, API package, if… It's registered somewhere else now. The logs, will stop coming in from… previous registration. So if there's different uses of the different API packages.
There's some incompatibility there, and getting everybody migrated quickly or solve that issue.
Because we have API logs, and now we have API. These are different bloopers, so…
**Trent Mick** 20:09 They use the same global.
Symbol, didn't they?
**Marc Pichler (Dynatrace)** 20:14 I think it's a different one.
Or…
**Trent Mick** 20:19 Okay. I don't know it at all. I was making an assumption.
**Marc Pichler (Dynatrace)** 20:22 I haven't checked. Okay, so… I think there's a check in there that just sees whether, like, which version it was registered with.
And if it's a different major version, which is the case with.
API logs and API, then it won't give you the global, that was being registered, so…
**Trent Mick** 20:52 Okay.
that API thing should be the only thing the browser's impacted by, I'm guessing. That and this, like, updating STK logs.
After finish removing SDK trace web usage, which we can do before, but yeah, okay, cool.
**Marc Pichler (Dynatrace)** 21:07 Yep.
**Trent Mick** 21:10 While Carlos is here, I think we're probably at a point where we could get.
If we need to have any more TC review of… Yeah. Logs.
**Carlos Alberto Cortez (Dash0)** 21:20 Actually, that's what I wanted to ask. Yeah, like, if you want to request one now is the time.
**Trent Mick** 21:28 Okay.
Yeah, I do. I'm not sure how to do it.
**Jamie Danielson** 21:32 I formally request.
**Carlos Alberto Cortez (Dash0)** 21:35 Yeah, you have to fill an issue. I can show you, like, one that… but it's basically filling an issue in the community repo, and I will let people at the TC know that one is coming.
**Trent Mick** 21:47 Okay, great, thank you.
Is there a template for this, or…
**Carlos Alberto Cortez (Dash0)** 21:53 I will look for that during this call, so I will send you a link.
**Trent Mick** 21:59 TC review request. There is a template.
**Carlos Alberto Cortez (Dash0)** 22:01 Although.
**Trent Mick** 22:02 I'll look at filling that out, yeah. Okay.
**Carlos Alberto Cortez (Dash0)** 22:04 Perfect.
**Trent Mick** 22:06 Excellent.
**Marc Pichler (Dynatrace)** 22:13 I think that's all for visual.
Maybe one more topic to discuss.
It looks like we're gonna be ready for the, new release date that we set, which is October 15th. Do we want to release as latest straight away, or do we, want to put, next, tag on there?
For some period of time.
And it's…
**Trent Mick** 22:56 Go latest right away, in my opinion.
**Marc Pichler (Dynatrace)** 22:59 Right.
**Trent Mick** 22:59 I think it's a major version bump, so people should already have reasonable guards there, I think. I'm not totally opposed to… Sitting on next for a while, but I'm inclined to just go for it.
**Marc Pichler (Dynatrace)** 23:12 Sounds good.
I just wanted to bring it up because of, the way that the… the release workflow is set up right now, there's no way to put next on there. But if you're going to go latest anyway, then that's fine.
So, yeah.
And moving on to the next one.
One question from Jamie.
**Jamie Danielson** 23:52 Oh yeah, I haven't been around as much lately, so you might have already chatted about this, but I was just curious if anyone is going to be going to, KubeCon in Salt Lake City.
next month.
Just me.
**Trent Mick** 24:05 Let me.
**Jamie Danielson** 24:05 Okay. Just you. One thing I'll note is that they are doing a ContribFest again, so if anyone has ideas on things that we want to… Mark is good for that. I usually have really, you know, optimistic ideas on things we're gonna mark for those, and then we get to the day, and there's maybe, like, a couple, but… Figured I'd just mention it that some people may be looking at that repo.
If we… if we come across anything. I don't know if we have anything top of mind right now.
I feel like it's gonna get harder and harder with people using AI for everything now. Like, most easy things get scooped up pretty quickly.
**Trent Mick** 24:47 Indeed.
**Marc Pichler (Dynatrace)** 24:52 Looks like all.
**Trent Mick** 24:53 I feel like I've been…
**Marc Pichler (Dynatrace)** 24:54 Once a call.
I…
**Trent Mick** 24:56 I've been pushing off some things that aren't for the 3.0 for so long that there's this big pile of PRs to get back to.
**Marc Pichler (Dynatrace)** 25:09 I.
**Jamie Danielson** 25:10 Last time we had a bunch of those, the easy ones of like, where we swapped out functions. That was kind of nice.
**Marc Pichler (Dynatrace)** 25:19 I think some people got bored of them quite quickly.
So…
**Jamie Danielson** 25:28 Dooley, Yeah, it was like, if it wasn't able to be resolved during ContribFest, that's usually a thing, too. If it's not small enough to get done during that time period, a lot of folks aren't coming back to the PRs either, yeah.
Okay.
**Marc Pichler (Dynatrace)** 25:54 Right.
Then… I guess we can move on to Park Triage. I don't think… Or at least I don't have… I haven't seen any… Recent ones pop up, so that's good.
I would say let's skip the old PR triage.
in current contrib and give everybody half an hour back unless there's Some more topics to discuss.
If not, then happy PR reviewing. Have a nice Week, and see you next week.
**Jamie Danielson** 26:43 Thanks, Mark.
**Trent Mick** 26:43 Thanks.
**Jamie Danielson** 26:44 ma'am.
**Jackson Weber** 26:44 everyone.
**Marc Pichler (Dynatrace)** 26:45 Thank you. All right, bye.
