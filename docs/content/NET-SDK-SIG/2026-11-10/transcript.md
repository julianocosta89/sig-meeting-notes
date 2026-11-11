SIG: .NET SDK SIG
Date: 2026-11-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:50 Hey, Aaron.
**Alan** 01:51 Hey, Martin.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:53 How's Mexico?
**Alan** 01:54 Oh, Mexico is great.
Nearly 3 weeks.
It's a good break.
Yeah, it's quite…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:02 a long, long holiday. It's like, usually I… if my longest holiday would only be 2 weeks.
**Alan** 02:08 Yeah.
Yeah, this was… I think 2 weeks is normally what I take too, but yeah, just extended this one a bit.
I feel like if I had had it to do again, I probably would have taken the same amount of time off, but maybe… Left more on the tail end to just kind of chill out at home.
You know.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:30 Right, right, yeah.
**Alan** 02:32 But, yeah, it was a… it was a great time. Much warmer weather.
than what I came back to, so…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:41 Oh, yeah, I can imagine.
**Alan** 02:44 Kind of miss at that, the sunshine and all that.
but yeah, how things been going?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:56 Not bad. Busy last week with all the anthropic scan findings, but otherwise, kids.
**Alan** 03:06 Yes, I saw your note about that for adding to an email list.
I don't know, I may as well… May as well just hop on that bandwagon, and let me respond to your message right now with my email.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:20 Yeah, it's not urgent. It's, it was more important maybe 2 weeks ago than it is now, because since I set the group up.
they, in a Anthropic launched the feature to have it directly report to the GitHub advisories.
**Alan** 03:38 Oh, I see.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:39 So, so less should come through to the email now, but we've got the alias set up now anyway, if we need it for anything.
**Alan** 03:46 Gotcha, okay. Well, I just… I just sent you my email address anyways.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:50 Cool, I'll set that up tomorrow.
**Alan** 03:52 Alright.
But it was… it was productive, like, it actually found some stuff. It looked like… He said something about Geneva and one collector, but it sounded like Raj was like, yeah, these aren't really problems.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:11 Hey, Raj. Yeah.
**Rajkumar Rangaraj** 04:12 Hey, mate.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:13 Basically, apart from one issue, all of them, really, they were just bugs.
But because they got found by the security scanner.
Anthropic just send them all through the same funnel.
**Alan** 04:26 Oh, interesting, I see.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:28 But, there was one that we turned into an advisory, whereas if… if you happen to have your app set up in a certain way, and you didn't have… you had less than about 400MB of memory on it, so say, maybe, say, like, a Lambda function, or a small container, it was possible that you could, like, spam it with non-existent pages, and fill up a cache and oom it.
So, that one's been published as an advisory, but… with the current GitHub backlog, it might take 50 days to get a CVE assigned.
**Alan** 05:06 Gotcha.
Huh, cool.
**Rajkumar Rangaraj** 05:10 Just a question, Martin. Like, do you know how those Anthropic folks got engaged? I know they added, they gave permission, I've been monitoring that, but do you know how their engagement started here, to bring the scripts to the repo?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:27 So, it started by me reading the blog post that said they were launching this new service.
And then…
**Rajkumar Rangaraj** 05:35 Okay, we went to them.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:37 Sort of. There's a GitHub repository if you submit a pull request.
you can… ask to be added, and then they do an assessment of how popular and distributed your project is. Okay. Whatever the criteria is, we met the bar, and Piotto was, also thought it would be good to add ourselves to it, because he's been doing scans with codecs internally.
**Rajkumar Rangaraj** 06:07 Yep.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:08 So we onboarded onto the scanner, and then it took about a week or so before they started sending us findings.
**Alan** 06:18 Have there been other hotel repositories that have hopped on this?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:22 So, let me, let me check, there was definitely some interest.
Sorry, Raj, what was that?
**Rajkumar Rangaraj** 06:32 Do you know, like, what's the repo, their repo name?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:36 I'll just share my screen.
So it's the, OSS scanner repo.
**Rajkumar Rangaraj** 06:52 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:54 And then it's just… everyone does a pull request if they want to be included.
Alright, so Collector, oh, is onboarded as well.
But we're the only SDK.
But to onboard, it's a YAML file with a few lines in it.
the real config for it is in our repo in this folder, so that we can update the Dockerfile that's needed to build it without having to do a pull request to them.
**Rajkumar Rangaraj** 07:34 Nice, good initiative from our side.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:39 Yeah, so out of two scans so far, we've got one… what will be a CVE out of it, but It's still been there for, like, a couple of months.
Also, welcome, Peter.
Tell me if I pronounced your name wrong.
Welcome to the SIG call.
**Petar Jerinic** 08:08 Thank you. It's better, but if it's too hard for part for your tongue, you can also say, Peter, I don't mind.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:18 Petar.
**Petar Jerinic** 08:19 Yeah, that's right.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:20 I'll try and remember that.
**Petar Jerinic** 08:23 Appreciate it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:26 Cool. So, I've just put… I've got 3 things on the agenda today. Two are from… Holdover from… Classic.
Oh, maybe we were in different calls, Raj.
**Rajkumar Rangaraj** 08:41 Yeah, that's why I joined from the Google Calendar, today I joined from the one… the link over here.
So, like, we need to figure out if there's a difference between those two.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:53 I usually follow the one in my Google Calendar.
But yes, that would explain why there was… we both seemingly… there was no one there.
Yep, so… First item is… Excluding the fact that I'm just waiting for the Docker images to be published, to update the PRs, the .NET 11 stuff should be ready. I don't think there's any new PRs… but urgent, that need to be merged, or ideally there's two AWS ones waiting on Norm to review.
So, unless there's any reason not to, should we be able to do the 1-2-1 release tomorrow?
**Rajkumar Rangaraj** 09:51 Yeah, I think we always do that. Once the .NET stable version is available, next moment we do the release.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:59 Okay, thank you.
**Rajkumar Rangaraj** 10:00 We're on track there.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:01 Yeah, I've, Piazza… Replied to your review on his… braking change for the baggage stuff, so pump that into 122.
**Rajkumar Rangaraj** 10:15 Yeah, that's better, actually. That issue has been for a longer time. We can just hold on to that and then do the release.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:23 Yep.
Sure.
So yeah, so unless anything comes up to not do the release, I'll do that tomorrow morning, and then… Your daughter would then be able to update the ZRA code.
To consume it as well.
And then we've got two other items.
Type in the template.
This is just more, visibility, rather than anything we necessarily need to chat about now. First one is this OTEP that I saw last week that's been opened in the spec repo.
The TLDR is… the proposal is adding new API to… Allow you to… say whether or not you want non-stable instrumentation to be emitted by your SDK.
So, if that were to be implemented, it would mean we could make all of the instrumentation libraries that are otherwise not stable only because of spec reasons.
to be stable.
So we could make them more binary stable.
And then users would opt in to non-stable instrumentation.
**Rajkumar Rangaraj** 11:49 I would strongly support this, because As this feature is not available here, we are handling this in the… within the export.
So, if it's a part of the instrumentation itself, it makes the life super easy. Exporter can be very thin, just doing the exporting capability only.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:08 Yeah, and also, like, one of the top questions we seem to get in issues is, when's this going stable?
Yeah. And then I have a canned reply that, we're waiting on the spec.
**Alan** 12:25 I guess… Yeah, I think we… I think the communities needed something, to this effect for a long time.
But one of the things that makes it a little bit odd is, like.
There are still some bodies of conventions that are just… none of it is stable. So, like, some of the messaging frameworks, just for example.
So, what would that instrumentation do? Would it just be, like, you'd enable it, but nothing would come out of it unless you… explicitly say, like, yeah, baby, I'm good with… I'm good with this.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:00 I guess that… I guess that's a good point for stuff where everything's unstable.
**Rajkumar Rangaraj** 13:06 Yeah, probably in those guys, we can say that we are marking their development as a default in that, and call it out in the release notes, or somewhere for that specific component.
That it's going to change, or the… something like that, but… What's your thought there?
**Alan** 13:27 Oh, I don't necessarily have ideas or thoughts, just kind of… Still some awkward, just thoughts about some awkward corners, that exist.
One of the… one of the things that we did, with the AWS instrumentation that I kind of liked.
is we… I mean, it was somebody from AWS that pushed for the stabilization of that instrumentation, and the… Solution that we landed on was essentially an enumeration that Allows a user to configure which version of the semantic conventions they want.
I… I thought that that was a relatively elegant way to handle this explicit, kind of, like, I am… I am adopting this version of the conventions, and I'm going in, eyes wide open, that there are elements to this version that may not be Declared stable yet.
Anyways, just to point out that we've… we've done something along this… this line that was not necessarily, like, spec sanctioned or ran through an OTEP or whatnot, but might be a useful data point.
for this effort.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:57 Yeah, I think this one's more at the signal level.
And possibly, like, the meter level.
So it would be more granular than the AWS… instrumentation approach.
But yeah, there's definitely… Stuff in there we could… I don't… I… From having to code against it to put new ones in.
It's a bit cumbersome, and this… we've had a few bugs sometimes.
Where, like, I've forgotten to override a property.
To change your name, or something like that.
**Alan** 15:34 Huh.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:35 So, I think if we did something like that, again, in a more wide-ranging basis.
There's probably a few rakes that have been stepped on. We'd need to try and design out of it.
**Alan** 15:49 Yeah, yeah, yeah.
That makes sense.
So this would… this idea, though, as you said, at a more granular level, this would… Require… Diagnostic source changes. Is that right?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:08 Am I thinking about that?
**Alan** 16:09 Right?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:13 I… I… maybe?
**Alan** 16:16 Oh, no, this is at the provider level.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:19 Right, okay.
Yeah, because I was thinking it was, like, in the inter… when I read it last week, it's like, it's in the… sort of baked into the internals.
To make… do you see which ones it should and shouldn't be doing?
But, But yeah, I forgot most of what I read the paper. But, you know, it's like, for example, there's a bit of declarative config here.
And, they're being opted into… There we go, that's the one.
Oops.
So, it's saying for HTTP server active requests, it's opting into it because it's unstable.
**Alan** 17:07 Yeah, gotcha, okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:08 But yeah, I think it'd be good, just to sort of, like, socialize that this exists, and for people to take a look at it when they've got some time.
Because if this gets… Approved in the spec, it might give us a way to, get rid of some annoyances we have from the unstable stuff.
**Alan** 17:30 For sure.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 17:34 And then the other one I've added is… Exceptions… On spans, it's been deprecated, and there's a new thing in the spec.
For doing exceptions through logs?
I had… called Codes.
Give me, like, a skeleton of what we'd need to do to adopt this?
So… I think there's too much to talk about now, but yeah, if people could have a look at this.
When they've got some time over the next week or so, because it'd be good to start… Working out how we actually implement this, so we can move over to it.
**Alan** 18:20 Cool. Yeah, I've known that this was coming for a while, do you… Except I haven't really been… paying attention to the conversations for a while. So, do you know offhand whether this is being considered, essentially, like, a breaking change, like, is the idea that it's implemented in such a way where, like, the data used to show up on span events, and then with the next version, like, upgrade, whatever, like, it's not going to show up on span events anymore, it's going to show up.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 18:52 So… there's, there's an MVAR.
**Alan** 18:59 Okay, it's odd.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:00 you opt into it. So, essentially, we'd be doing both, and the user would pick Which one they wanted to use, excuse me, which one they wanted to use for them.
**Alan** 19:10 Okay, so standard pattern that, the community's been using for, like, new semantic invention stability efforts?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:18 Yeah, I think so.
**Alan** 19:20 But then, eventually, if it is like the other efforts, eventually this environment variable will get dropped, right?
**Rajkumar Rangaraj** 19:34 Maybe in the version 2, right? But not in… Version… this version at all, because it's going to be a big… Breaking change.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 19:44 Yeah, just in case you misread it, Alan, it's exception, not experimental.
**Alan** 19:50 No, no, no, I read it right. No, no, no, yeah, yeah, yeah. So, like, this same environment variable has, you know, we've… we've had other flavors of it for, like, when the HTTP conventions were being stabilized, and when the database conventions were being stabilized.
there was one of these OTEL SEMCOM, like, I don't know, don't remember the names, but, like, database signal opt-in, or something like that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 20:12 Hmm.
**Alan** 20:12 And… the… So yes, I recognize that this is a big breaking change. If it follows the pattern that we've done for, like, the HTTP and database stuff.
The dance that we have done, at least within the .NET community to date, is that You know, we've always had pre-release versions of our instrumentation, and then… when we release the version that drops the NVAR, We just simply publish, you know, like a… a one dot.
Whatever.
In this case, like, we already have, say, HTTP, Instrumentation that does emit… Exceptions on span events.
So… Would we publish a 2-dot or something like that?
When that day came.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 21:21 One thing I've been thinking from reading this is that, potentially, it's something we could change internally.
Like, it would go through the span event.
infrastructure, if they were using that API, But then at the exporter level, you could potentially change it to the other signal.
But that's just me spitballing from a thought, rather than something I've actually tried. It would just be, how would you identify the logger to send it through?
**Rajkumar Rangaraj** 21:54 Another thought also is, like, all this time we have changed within the signal, right? There are people who could be using the… only the tracing, but not logs at all. So I've seen many cases where customers use 1VD.
Log signal, but not the other two.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:11 Hmm.
**Rajkumar Rangaraj** 22:12 This is slightly going to be a challenge in those cases if we follow the similar strategy what we have followed slightly earlier, because that was within the signals boundary. Here, we are switching the signal boundary itself.
So…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 22:29 the impression I got from reading it was that Users would opt in.
And then both exist, but one is deprecated and one is preferred.
So if you were using all signals, you'd be encouraged to do the new way of doing it.
**Alan** 22:49 So your impression is that Unlike the, other… environment variables of this nature. This one… is… Going to be longer-lived.
Kind of always be an opt-in?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:08 Maybe not always, but… Not as… not a… not a short-term thing.
But yeah, excuse me.
If, people, like, take a look at the specs.
In their own time, and then…
**Alan** 23:31 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 23:32 scheme read this potential plan of what we would need to do.
then I could maybe start working on it, trying to… at least trying to prototype, for non-merge what it would involve.
But, as it's a bit more involved than, you know, just add a thing.
Yeah, I figured there was no point starting on it until there was some agreement.
**Alan** 24:01 Yeah, sounds good. Yeah, I'll try to spend some time on this. Yeah, Raj brings up a good point, which is that this is… this is definitely bigger than some of the other things that we've encountered before, given that it's kind of cross-beling and whatnot.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:20 Cool, those were the three items that I had. Is there anything else anyone else wanted to chat about before we just skim through the PR dashboard?
**Alan** 24:36 Nope.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 24:44 Somewhere about here? That's where you can go to look at… this one, I think this PR of Steve's, you had some feedback on this one, Raj?
**Rajkumar Rangaraj** 25:01 I think I did not hear back after that, I believe.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 25:05 Let me just hook.
**Rajkumar Rangaraj** 25:18 It looks like it's done. It's a minus. I'll take a look at it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 25:22 Okay, where else can we go?
That one's waiting on CJO. Last I heard from CJO, since he moved to Apple, he's waiting for legal to let him sign CLAs and stuff.
So, he's sort of in Hotel No Man's Land at the moment.
But, we're waiting on him to look at that one. He has promised to look at it, and he can.
There's a docs PR to do with async exceptions, which is… To resolve an issue that is… 5 years old.
So, if someone who was around then… would like to take a look at it. It might get done a bit quicker than if I try and… Fully understand it, and take all the context.
Oh, yeah, and also, I guess this one's mainly for you, Raj. One of the anthropic findings was to do… was the PI you approved yesterday to do with the file permissions?
For the persistent storage stuff.
**Rajkumar Rangaraj** 26:35 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 26:35 Because that was in the main repo.
the persistent storage libraries got out of sync, so I've opened two PRs today to get them back in sync with each other. So there's the one in… the main repo. Apart from one change to fix a co-pilot finding, it's mostly all tests. And then there's another one in Contrip, which is pulling the fix you approved yesterday into Contrip.
**Rajkumar Rangaraj** 27:03 Yeah, I saw that the persistent storage was not in sync, but I did not want to block this PR for that. We are solving the security concerns here.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 27:13 Yeah, yeah, the part of the reason it got out of sync is not just the anthropic finding, but also when I tried to keep them in sync by, like, opening a PR in one and opening a PR in the other, waiting on the other one.
Copilot would find different… review findings on both PRs, and then I would get confused keeping them up to date with each other.
But, once these two are in, they should be back in sync again now.
So yeah, it'd be good if you could take a look at the contribun today, so that.
**Rajkumar Rangaraj** 27:47 Definitely.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 27:48 Get back in with the 121 release tomorrow.
**Rajkumar Rangaraj** 27:52 Sure, I'll see if I… right after the SIG, I'll spend some time on that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 27:59 Cool. Thanks.
Then… what else we got?
Conflicts, conflicts… conflicts… That's the one we talked about just now, that's for the next minor release.
But with the baggage fix… Bunch of drafts… And then over and contribute… There's… There's a Kafka one, Waiting on the… Code owner for that library to take a look at.
does a PR… I've approved it, but it hasn't been merged. That's the follow-up.
brought the comment you had on the baggage PR yesterday, Raj?
Matt is working on that one with this person.
Matt's not here today because he's at KubeCon.
There's two… There's two anthropic findings for the AWS instrumentation that I'm just waiting on feedback from Norm from.
there's a PR… to extend the EF core instrumentation to support, Late… the later ability to, like, sanitize… NoSQL queries, but I've been ignoring it until this release gets out and the security fixes are done.
But it adds a lot of public API, so… in two minds about that one. I think we talked about it a few months ago.
Being able to change the query sanitizer.
This is… there's a small PR on Geneva, Raj,
**Rajkumar Rangaraj** 29:51 Yep.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 29:51 I was playing with Copilot agents to have it do performance investigations, like, in the background in the cloud, and it came up with a small one to do with number formatting, so I figured it was small enough To submit.
**Rajkumar Rangaraj** 30:04 I think that… I think that's straightforward. I think both myself and Sean are in here, so we will take care of this one today as well.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 30:13 Okay, cool, thanks. Yeah, I, I figured for the… at least doubling… The per operation throughput, it was… it was worth it for how little the code needed to change.
And there's… A bug fix for an old issue.
To do with container identification.
Piotr had a comment on the original issue, which basically was, copy what Java does. So that's what that PR does.
And… That's… it. I think everything else is a draft.
Are there any anyone wanting me to drill into specifically?
**Rajkumar Rangaraj** 31:08 No, I don't think we should get into that detail, sadly.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 31:12 Okay.
Well, that's everything on the agenda, then.
**Rajkumar Rangaraj** 31:18 Just want to ask one question here, Martin or Alan. Like, any of you know what… how many people are shown interest, towards having a metric producer?
Is there an ask, or anything from your org level, where people wanted a metric producer?
**Alan** 31:40 That's the API, what, for, like, basically bridging in… metrics from a different system into OpenTelemetry, is that right?
**Rajkumar Rangaraj** 31:51 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 31:52 Oh, I… yeah, for a minute I didn't know what you were talking about. I know… I remember now. There's an issue somewhere in the main repo about it.
**Rajkumar Rangaraj** 32:00 Yeah, but no airport and everything, probably not most people come here. I think it's metric, yes, it's not there, I believe, yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 32:12 Yeah, because…
**Rajkumar Rangaraj** 32:12 So many people taking a stab at it, and they did not move forward at all. That's why I was wondering, like, if there's enough interest in the community to… because it's Java, it's done as a first-class edition, and people rely upon that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 32:29 So I think the last we got to this is, yeah, people kept looking into it, so then I had a quick local spike of playing around to, like, what we need to do to create it.
And the sticking point was, you need to produce a batch of metric points.
But the metric point struct, the cons… it's… it's… It's been designed to be viewed, not to be made.
And there's some complexity on how would we do that without breaking the API to let people create metric points?
Because it's sort of… it's a bit like if you gave someone an abstraction to create some object, but you never gave them a public constructor to make the objects.
So, the design of Metric Point at the moment, sort of.
Makes it currently impossible for anyone outside the codebase to actually create them.
**Rajkumar Rangaraj** 33:30 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 33:32 So I think, to answer your initial question, we do occasionally get trickles of people asking about it.
But I think… only one person on this thread was actually interested in using it. I think all the other.
**Rajkumar Rangaraj** 33:46 No, he shouldn'.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 33:47 It was doing the work.
**Rajkumar Rangaraj** 33:48 Yeah, Matthew is from my team, so he tried taking a step, so whoever is after that… he tried and take a stab, and then he also left. SIGO also tried. Earlier, Blanche tried, I tried, so none of us took it forward to completion.
**Alan** 34:06 We talked about… I remember, Martin, I don't know that you were on the call, Raj, but we… we did talk about this issue some number of SIG calls, probably months ago.
And I vaguely remember that there… may have been an actual, like, use case. That's the thing that's always been on my mind. It's like, I don't… I'm not aware of any, Strong use cases?
for it, to date, at least within the .NET ecosystem.
So that's kind of been the thing that I've been most curious about.
But on that call, I vaguely thought maybe we had identified one. Maybe it was Kafka, or maybe it was…
**Rajkumar Rangaraj** 34:48 Yeah, something like messaging and… not many small projects in the… within the Microsoft uses that.
So, they… from the old system metric, they cannot adapt the open telemetry immediately, so this can act as a bridge layer, and they can easily migrate on later and all that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 35:07 It might help with this… this one.
**Rajkumar Rangaraj** 35:10 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 35:14 But yeah, what I've… what I remember now when we talked about it is, like, the only construct… other than the default constructor.
For the struct, the only construct is this internal one.
Yeah. And it accepts lots of, sort of, like, internally things, so… And because all the properties are, like… and methods are, like, gets.
There's no way for anyone outside of the SDK to create a valid metric point.
So I think, if I remember correctly, we discussed, like, maybe we could come up with, like, an intermediate API That is public, that uses the internals to create metric points.
that then a meter provider could use to do its own thing, but I don't think we got any further than that.
In terms of what we would need to do.
**Rajkumar Rangaraj** 36:13 Yeah, I think there are two major things that we… major feature I would call to complete in the .NET SDK is the one is this metric producer, and another one is the logs bridge completion. These two have been pending on this for a very, very long time.
Probably, if we have a bandwidth Next, switching our focus to getting this done would cover all the gaps that we have.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 36:42 Really, I think, I think we need to design Yeah. Some… something it… because we got in the… in the issue, Like, I did a skeleton of what we would need to implement to do the meter producer spec.
Yeah. It's just we're missing the bit that would actually let you implement this outside the library, because creating the metric points.
**Rajkumar Rangaraj** 37:10 I remember looking at Go implementation, it's well done in that the entire metric implementation is .NET is completely different from what Go or Java does. That makes the scenario pretty much complex over here.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 37:34 Are you… are you… are you getting lots of internal asks for this then, Raj?
**Rajkumar Rangaraj** 37:39 The… what is that?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 37:41 But you're getting lots of internal people.
I'm asking for this.
**Rajkumar Rangaraj** 37:45 We, here and there, we get a lot of asks. Mostly, we ask them to go and contribute here, because my team has a limited bandwidth at this point in time.
when the team comes, we route them to OpenTelemetry, but we have never seen them coming over here. That's when I'm, like, we tried taking a stab at it, that's when Matthew finally came here. He was new to Open Telemetry, so he tried taking a look at it, and That's when he had those conversations with you, the last one.
Matthew Saintsburg.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 38:23 Right, okay. Yeah, I was trying to find the comment. Right.
**Rajkumar Rangaraj** 38:32 Let's see if we can discuss in the further after this, the release of the next .NET one, the .NET, the major one that we planned for this week.
And then we can bring it up in the next week to see how we can address this one.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 38:47 Yep, sure. Yeah, I'd completely forgotten about this issue.
Because, yeah, I, yeah, I put a comment on it that it needed more thought before we could get,
**Rajkumar Rangaraj** 38:59 Yeah, this needs someone… Yeah, this needs someone with good knowledge of this SDK. Either of the approvers or the maintainers here would be the good fit, especially for this issue. I call it out. It requires the in-depth knowledge of that.
the mythic… How the metric system works.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 39:30 Maybe a Q1 thing.
**Rajkumar Rangaraj** 39:32 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 39:36 Cool, anything else anyone wants to chime in?
**Alan** 39:43 Nope.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 39:47 Cool.
Right, in that case, I'll see you next time.
Thank you, Kelly.
**Alan** 39:52 Bye.
Bye.
**Petar Jerinic** 39:53 Thank you, bye.
