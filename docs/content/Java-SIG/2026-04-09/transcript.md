SIG: Java SIG
Date: 2026-04-09
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**John Watson** 01:54 Howdy, everybody.
**Jack Berg** 01:56 Hello?
Trask is out today.
I'm getting ready to share my screen.
**Gregor Zeitlinger** 02:23 Nope.
**Jack Berg** 02:27 Please, if you have any topics, add them to the agenda.
All right, we're 3 minutes over. There's only one item on the agenda added by myself.
Which is about the tomorrow's 1.61.0 release. There's one PR that needs to get in for the release. There's several others that are already approved.
And… you know, I'll take another pass at those to see if any are, you know, ready to be merged and do so. But this PR is, This is a vulnerability that we need to… that we need to fix.
So… There's been some comments on it already, it's… It's frustratingly large, but unfortunately, that just seems like the reality of touching our senders, because there's so many different implementations So, yeah, you know, just a reminder, so this adds… limits to the size of an OTLP response that we will read into memory. It's currently unbounded, and so the vulnerability, which has been reported, and it's, like, it's, it's a vulnerability that applies to many languages in OpenTelemetry, but the vulnerability is basically, OTLP exporters will read an unbounded, response body, and, you know, there's a… there's a resource exhaustion, attack that, you know, SDKs are exposed to through that, if they're connected to a compromised collector. At least that's the claim. I don't know how often that'll happen, but, you know, we need to fix it nonetheless.
So, yeah, so this, you know, there's a… there's a corresponding proto-PR that I should pull up.
Which… Was merged just the other day, and it updates the Proto spec to talk about the specific limits and the specific behaviors that I've implemented in this PR, but, you know, the thing that matters for our purposes Is that, you know, the default limit for a response Body should be, 4 megabytes.
And so that's what's embodied here.
Yeah, so please take a look. You know, Gregory previously gave it a review. I had Copilot give it a review. I've, you know, been working on this for quite some time. So yeah, I'd like to get this approved and merged.
Happy to feel that.
**Gregor Zeitlinger** 06:37 I will take another look, just didn't see it yet.
**Jack Berg** 06:40 Okay.
Any other topics that people want to discuss?
**John Watson** 07:02 I just wanna… highlight that… I continue to not have a lot of time to spend on OpenTelemetry, so I'm doing what I… doing what I can here and there, but I'm… I really don't have time for doing any in-depth reviews, unfortunately, at this point.
**Jack Berg** 07:18 Understood.
One thing I was wondering, John, is if it would be good to have some automation to detect if a PR changes the public API surface area and label it accordingly.
Right? Because those are the more sensitive bits, not the only sensitive bits, but, like, you know, you know, even if you can't, you know, inspect all of the files, at least, you know, we talked about this a long time ago, is like, what… should there be additional approval requirements for things that touch our public API surface area, and, like, that might be a good way to you know, establish that, that, you know, we are touching the API surface area, and in those cases, we want to have approvals… two approvals, for example, or at least, like, have, you know, the maintainers all, give a thumbs up.
**John Watson** 08:11 Yeah, I mean, that's basically what I focus on now, aside from just Dependabot, or whatever the Dependabot replacement is called. That's mostly what I look at, so I do look at all the PRs, just, like, at least look at the descriptions and the titles.
And if there are changes to the public API, I try to look at those and give them a, you know, positive or negative. This one, I didn't really… I missed that there were changes in the public API here one, but these don't seem crazy, so… And this is also SDK API, which I… I'm slightly less concerned about than I am with the instrumentation side of things, like the actual API API.
Right. So… Because I feel like if, I mean, the number of consumers of the SDK API is way smaller than the number of consumers of the actual code that does instrumentation.
**Jack Berg** 09:05 That's correct. And there's actually, you know, now that you mention it, so we've… there's been these ongoing conversations in OpenTelemetry about, like, you know, the collector still hasn't reached 1.0. Like, why is that? And, you know, the… the sort of conversation that's happening is, like, because it's so hard to make changes. There's, like, a ton of scrutiny, maybe unnecessary scrutiny being applied to all of the APIs, all of the configs and everything, prior to declaring 1.0. And, you know, I think everybody has sort of adopted this, this idea that, like.
there's… there's no breaking changes allowed in OpenTelemetry. That's not right.
Like, there's parts of OpenTelemetry that would be very bad to have breaking changes in, to have a major version bump, and it's things like the instrumentation API.
Like, and there's other parts which, you know, while you don't want major version bumps all the time, they're way more tolerable, especially if there's a schedule, a cadence, communication around them. And it's like, you know, the Java agent has demonstrated this with a 2.0, and there's, like, a 3.0 coming.
And JavaScript, actually, has had a 2.0 of their SDK.
And it went really well. And they're gonna have a 3.0 of their SDK that's coming up.
Now… to me, having a 3.0 after you just had a 2.0 may indicate that, like, I don't know, maybe you should apply some more scrutiny to these APIs if you need to make breaking changes. You gotta catch all those things and bundle them together, but, you know, I guess the point is, is that the… like, I could envision a world where we have a 2.0 of our SDK API, I, you know, do not want to entertain a world where we have a 2.0 of our API, or OpenTelemetry API, for instrumentation, so…
**John Watson** 10:55 Yeah, but I mean, and also, I feel much better if we make a mistake in the SDK APIs, like, just deprecating it and saying, hey, don't use this, and here's the replacement, and it won't… like, as I said, the number of consumers of that is going to be way smaller than the number of consumers who… and the number of… and by consumers, I also mean things that depend on it, rather… not necessarily people, but, actual pieces of code that depend on that is going to be way smaller for the SDK than it is for… the actual API use for writing instrumentation.
**Jack Berg** 11:30 Totally.
That's right.
Yeah, okay, so maybe look out for that. I might tool around with some, you know, some.
**John Watson** 11:39 Yeah, and if there's a way to have it not only… if there's a way to have it not only… Label it, or tag it, but to automatically tag me?
Or tag maintainers, or something like that, that would also be, super helpful. Because that's, like, I still use the GitHub notification.
API, and I first look to see if I've been specifically tagged on anything.
**Jack Berg** 12:03 Yeah, I think I would have to tag you and me, the maintainers, individually, because like, my notifications, for example, are just an ungodly mess because, you know, for example, my review is requested on every instrumentation PO.
**John Watson** 12:20 Yeah, there's the… there's mentioned, I think, is the thing. I don't know whether that shows up if, like, maintainers… Mentioned is the thing that I look for.
**Jack Berg** 12:28 Mention is when you personally are called out as an individual, and so, yeah.
**John Watson** 12:33 Well, what about team… oh, team mentioned probably is two. Do we even have a team for the two of us?
**Jack Berg** 12:39 We have the maintainers, yeah. So yeah, there is a team.
the job I maintain.
**John Watson** 12:45 So, team mentioned, also, we're also in approvers, and we're in a bunch of other things, so it's probably too broad.
Yeah, okay. Anyway, having me tagged specifically in a con… even if it's just, like, adding a comment to the automation.
That would be… that would… that would help me be able to focus on the… the things that are more… most critical.
**Jack Berg** 13:06 Sure.
All right, and just a friendly reminder to everybody else on the call that PR reviews are useful and appreciated, you know, even if your approval doesn't have a green checkbox. So, you know, if you're aspiring to be an approver someday, the way you get that is you just… you start reviewing and approving.
And making, you know, thoughtful reviews along the way, so… Yeah, okay.
Sorry, John.
**John Watson** 13:45 No, I just said seconded. Agree, I'm agreeing. I wholeheartedly agree, yes.
**Jack Berg** 13:53 All right, well, there's nothing else on the agenda, so, you know, calling out for additional topics.
Before we end early.
Going once.
Going twice.
**John Watson** 14:08 There's nothing to talk about from instrumentation, not the fact that we have, like, 10,000 instrumentation PRs a day.
There's no one… no one worried about that? The fact that all the automation is generating so many… notifications is to make it almost… it's like… it's like, alert fatigue for GitHub PRs.
**Lauri** 14:30 Well, it actually is rate-limited. It doesn't… It, it's limited to something like 10 open PRs.
So… The fact that it is… Creating a lot of notifications means that those PRs are usually getting merged quickly.
**Jack Berg** 14:49 Yeah, the rate limiting was broken for a moment there, but I think it was fixed.
Looking slower.
**Lauri** 14:55 Yeah, it should be fixed.
I don't really get, like, What you're meaning, like, Every morning, I just, like, scroll through a bunch of mails, like, when Trask has been approving those.
**John Watson** 15:15 Yeah, I'm probably going to just remove myself from getting any notifications for the instrumentation repo, just because it's, I mean… There's no reason for me to be looking at them at this point.
**Jack Berg** 15:27 So, I don't think you can, short of removing yourself from approvers.
Like, so I've tried to do that already.
**John Watson** 15:35 Oh my god.
**Jack Berg** 15:35 limit my notifications from this repo to only things that I'm explicitly mentioned on, and it doesn't work.
**John Watson** 15:42 Interesting, okay. Well, anyway…
**Gregor Zeitlinger** 15:45 I tried it as well. I'm actually building a tool that is, like, a better inbox. It does more than that, but this is one of the things I got annoyed with.
**Jack Berg** 15:58 yeah, you know, GitHub notifications, GitHub inbox needs some… needs some work.
**John Watson** 16:04 I'm guessing that it is, like, that there's very few people who actually use it, and so that it never gets any love. That's my guess.
Because I'd like to be able to create filtered views in there. It would just be super handy.
**Jack Berg** 16:19 The closest thing I've seen to this, John, is there's this function called saved.
**John Watson** 16:23 Yeah, but you.
**Jack Berg** 16:24 I didn't.
**John Watson** 16:24 Manually save stuff, though, right?
**Jack Berg** 16:26 Exactly. So, like, the workflow, if you want to do this, is to go to your main, you know, fire hose of an inbox, explicitly save the items that are interesting to you, and then have this filtered view of only things that you've saved. It's, like, it's not a great solution, but it's slightly better.
**Gregor Zeitlinger** 16:43 The team member of, mine actually, uses it on a daily basis.
**John Watson** 16:49 I mean, I don't use the saved, but I use this as my only way to get notifications from GitHub.
**Gregor Zeitlinger** 16:57 So it's not that bad, actually, Ben.
**John Watson** 17:00 I mean, it's… it's not horrible, it's better than it spamming my email inbox.
But, but, I think it could use some love.
**Jack Berg** 17:14 It probably will get some…
**Lauri** 17:15 those automatic review PRs will… Will they lessen in the future?
But currently, it's doing its second pass. I don't know whether… It has any work for the third pass?
**John Watson** 17:30 Interesting.
**Jack Berg** 17:32 I mean, yeah, it's kind of exciting, the prospect of having these idioms, these code-style definitions, you know, and you know, after this work… this work is done and the dust has settled, you have confidence that, like.
200-plus instrumentation modules are, you know, fairly consistent. Like, that's, like, that's an amazing achievement, in terms of, you know, code sanity. I know none of these things are big on their own, but I think collectively they add up.
**Gregor Zeitlinger** 18:04 Definitely, it's, it's quite hard to get into the codebase if, It's basically… A chance of getting a good or a bad sample of something that you take as, The thing, to copy.
**Jack Berg** 18:22 Exactly, right? When all the examples that you could copy for the next instrumentation are consistent in terms of their style, then the, like, you know, you're carrying forward that good pattern.
**Gregor Zeitlinger** 18:41 Okay.
**Jack Berg** 18:43 I'm gonna call it, because, you know, we've done a couple of calls for more topics, and we've just been… Shooting the breeze.
Nice to see you all. See you on Slack and on GitHub. Take care.
**John Watson** 19:00 Thanks for running the meeting, Jack.
**Jack Berg** 19:02 Yeah, bye.
