SIG: eBPF Instrumentation
Date: 2026-09-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 00:57 Hey.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:01 Right.
**Tyler Yahn (Splunk)** 01:03 How's it going?
**Mattia Meleleo** 01:05 Hello, hello.
**Tyler Yahn (Splunk)** 01:07 Hey.
**Roy Reshef (Kubex)** 01:24 Hey, good morning, afternoon, whatever it is. Evening.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:33 Just a reminder that the entire of Grafana is all off-site, except me.
So… Mario and Nicola are out, as is Mark.
**Tyler Yahn (Splunk)** 01:45 That's right, that's right.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:47 I had to stay behind because a couple of my kids are starting school for the first time this week.
**Tyler Yahn (Splunk)** 01:53 That time of year, huh?
Yeah.
Well, cool. Then, I guess, actually, we could probably get started. Yeah, I don't think… There's much more else in the quorum. So, yeah, if you haven't yet, go ahead, please add your name to the attendees list.
If you have agenda items you wanted to talk about, please also go ahead and add them there as well.
I can start sharing my screen, we can jump in here.
Alright, cool. Okay, Mattia, you wanted to start us off by asking about, V0… 123 release?
**Mattia Meleleo** 02:40 Yeah, so basically on, I think it was Monday, we merged the PR that, that is currently causing, HTMLS, segments or data payloads to be, injected with, transparent, so I think it's, It's somewhat urgent to put this release out.
And there is also one other issue, which is the memory leak that I think Nikola fixed.
So yeah, these two issues, I think, they should be out as soon as possible.
There was, an issue opened, like, some, half an hour ago, or something like that.
It's also asked for, for a new release.
Let me try and find it.
**Nimrod Avni** 03:35 I think, I think Mattia Spr is, Which one is, like, 3192 or something?
**Mattia Meleleo** 03:44 One moment… 3, 2, 5, 7… This one.
**Nimrod Avni** 04:04 No.
**Tyler Yahn (Splunk)** 04:08 This… sorry, when did this get merged?
**Mattia Meleleo** 04:14 2 days ago, or yesterday? I don't remember.
I also noticed that, this, this, function is, also called, like, two other times.
So, I had in mind… well, it was in my plans to check it today.
But I will do after… I will do it after the meeting and eventually fix the error to… codes.
And, yeah, I think… And it's, it's good for a release.
**Tyler Yahn (Splunk)** 04:56 Okay.
Yeah, I mean, sounds good.
The only hesitation I have is, like, what else is in the pipeline that we've already committed to?
So I guess I'm wondering, like.
Are there other features as well that would be included here that mean it needs to be a… A V013?
**Mattia Meleleo** 05:22 Oh, I didn't check, to be honest.
I don't know what merged since it's 0-12.
So, we did the release, like, 10 days ago, or something like that?
**Tyler Yahn (Splunk)** 05:35 Yeah, that sounds right, yeah.
**Mattia Meleleo** 05:37 Yeah, we need to check. I don't… I don't remember what emerged in the meanwhile.
**Tyler Yahn (Splunk)** 05:43 Yeah, I mean, I'm seeing things like the GO127, Target Instrumentation, like, that's a pretty big… fix as well. I don't know if you call that a bug or if it's a feature. The Deno extract service metadata for Deno apps, like, that was a pretty important one.
Yeah, runtime metrics for Python.
Fixes for .NET, yeah, I mean, like, I think we could probably say it maybe needed to be a minor release.
Yeah, more bug fixes…
**Nimrod Avni** 06:17 I think maybe it's, even in a, yeah, in a minor release.
**Tyler Yahn (Splunk)** 06:22 Yeah, ad service, yeah.
Okay.
Yeah, I agree.
Okay.
So, yeah, I mean, if that's the case, then I think that I'd probably say we probably want to go… Yeah.
What else is in the pipeline, though, I guess?
Guess what's already been reviewed?
No, that's no hat.
Yeah, I don't care about renovate.
So, this looks close. Is this worth getting in?
**Nimrod Avni** 07:41 Yeah, I think I approved it.
**Tyler Yahn (Splunk)** 07:45 Approved, yeah.
**Nimrod Avni** 07:46 I think Pino already… I think you can… you can, merge it. Probably Pino, unless you have any.
My pleasure.
**Giuseppe Ognibene (Coralogix)** 07:53 Goodbye.
**Nimrod Avni** 07:54 What's that?
**Tyler Yahn (Splunk)** 07:56 Yeah.
This is… I don't know, actually… This has been reviewed. Oh, Steven reviewed it, yeah, this isn't really… needed for a release. This is helpful for the next phase. One of the things that we aren't supporting right now is that, like.
If someone does have a new version of Go.
with different, like, offsets for the ABI, like, we don't actually support it unless we have those offsets offsets, so I wanted to, like… dynamically generate those, so this is kind of a step in that direction, but we're not there yet.
Declare OB's full telemetry schema. How's this looking?
**Nimrod Avni** 08:45 No reviews yet. Okay, I think you reviewed.
**Tyler Yahn (Splunk)** 08:49 review.
**Nimrod Avni** 08:50 Yeah, it's a big one, you can have a look.
**Tyler Yahn (Splunk)** 08:54 Yeah.
**Nimrod Avni** 08:54 But,
**Tyler Yahn (Splunk)** 08:56 Okay.
**Nimrod Avni** 08:57 I think I need to rebate… No, I need to rebate something else.
Something will do that as well.
**Tyler Yahn (Splunk)** 09:03 Yeah, okay, yeah, this probably still needs more reviews, but that's… yeah.
This looks… Also close, if not ready.
**Nimrod Avni** 09:14 Yeah, that's the one I just need to… Yeah.
**Tyler Yahn (Splunk)** 09:16 Okay.
**Nimrod Avni** 09:17 Fixed conflicts, do it now.
**Tyler Yahn (Splunk)** 09:24 I just saw feedback from Mattia on this one. I need to go back on this one. This one… Doesn't look like it's… Mattia also just got me some feedback.
Er… nope.
**Mattia Meleleo** 09:40 I think it was the other one.
This one is, I don't know if the Go changes were added lately.
But, yeah, I need some more time to review it. It looks very… Complicated.
**Tyler Yahn (Splunk)** 09:58 Okay, let me add you here as well, then.
Yep. So I don't forget.
**Mattia Meleleo** 10:10 Is the one, is the one not… there are two?
From you?
**Tyler Yahn (Splunk)** 10:14 No, sorry, this one? Yeah, yeah, yeah, no, I saw… I'm sorry, I skipped over it. I saw you already reviewed this one as well. I just haven't got back to it. I was just looking over what's ready for merge.
**Mattia Meleleo** 10:26 Oh, good, okay.
**Tyler Yahn (Splunk)** 10:27 Yeah, sorry, I just saw this shit right before the meeting, so, sorry.
Skipping in my head, yeah.
This one… Actually, I don't know where we're at on this one.
Did we just get a push on this, Nimrod?
**Nimrod Avni** 10:57 Which one is it? I don't think it… yeah, I think I… just a few… A few minutes ago.
Okay.
**Tyler Yahn (Splunk)** 11:07 It's a braking change, maybe we need more winter view on this.
**Nimrod Avni** 11:09 Yeah, I think it's, like, breaking in the… only the internal metrics, but maybe if we, like, maybe we should get more reviews on that, and maybe some more of the… Grafana folk.
**Tyler Yahn (Splunk)** 11:21 Okay.
Yeah, sounds good.
Trying to record those, or… Yeah, this is a long-standing bug. I think I might be on the hook for reviewing this again.
Yeah, actually, I think I just need to take a look at this. I think I… No, I guess I didn't approve it.
Okay, yeah, that's not ready for review, or not ready for merge. Okay.
But yeah, so I think with that said, then, Mattia, you're gonna take a look and double-check on the version?
Or Visa 13, right? Or… I guess… I guess we can kind of just agree that that's V013, right? Not… Patch, given what we saw.
Cool. Okay, if that's the case, then yeah, then I think that let's… let's go ahead and move that forward. We still have… the other milestone, but we can talk a little bit about that in just a second. But, Yeah, I think that that sounds good.
Mattia, are you gonna be able to take that action item to do the release?
**Mattia Meleleo** 12:44 Yeah, sure, I can do that.
**Tyler Yahn (Splunk)** 12:46 Okay.
**Mattia Meleleo** 12:46 And we'll restart, tomorrow.
**Tyler Yahn (Splunk)** 12:50 Sounds good. Yeah, yeah. Yeah, let me know. Otherwise, I probably have time tomorrow or the next day, so, yeah.
Okay, cool. Next up, Mattia, you want to talk about stale PR handling, enforce maximum number of review round trips in our author response deadline?
**Mattia Meleleo** 13:07 Yeah, this started, so I was, writing that, that other, thing about AI policy.
And then I thought about one PR that we have, which is somewhat stale.
And I was wondering if it makes sense to enforce stuff like maximum round trips for our reviewers, or maximum days of, Non-response from, from an author.
And stuff like that.
**Tyler Yahn (Splunk)** 13:38 Nice.
**Mattia Meleleo** 13:38 Yeah, it's that one. Because it's, it's open since May, and we are… we did, like, 4 or 5, Back and forth on this one.
And then pests are failing, and the author doesn't answer, and…
**Tyler Yahn (Splunk)** 13:59 Yeah, I mean, I'm, yeah.
We can put this explicitly in policy, like, if we want. I… I think there's just kind of an implicit policy.
that I've… I mean, I guess I've… I'm maintaining Go, like, the Go repos as well, like, I normally put something like this, and then I see, not last week, we just closed it, so, like.
We could just do that. Like, there's nothing really stopping that.
Because you can always reopen the pull request, like, there's not really anything stopping us there.
Obviously, we can put more comments, you know, instead of disclosing, saying, like, you know, we haven't seen a response, we consider this stale, like, yeah, we're gonna close, like, if there's… I normally do that, actually, like, if, you know.
I think the author is… has a chance to come back and saying that, like, you know, don't get discouraged, like, come back and, like, you know, update your PR, we'll reopen it. That makes sense. I think that's totally fine. But, like… I mean, I don't know, this one's pretty obvious that I don't think they're coming back.
So, yeah, I mean, I think that, like.
Yeah, that's fine. Like, as a maintainer, I think you should feel qualified to be able to do that kind of thing, and close these sort of things. Like, there's always, like I said, like, it's not final, it's a state change.
And that state change is reversible. So yeah, that sounds good. If you want to put that in a policy, though, like, I'm happy to do that. Another thing that we have in, like, the Go one is, like, a response needed, and so that makes it, like, explicitly clear. Like, not only in, like, the labeling to find from other people, but, like.
For the user, like, literally, like, we are waiting on you to get things done, Yeah, so we can do that. Okay.
**Mattia Meleleo** 15:39 I will, answer this PR then.
**Tyler Yahn (Splunk)** 15:41 Okay, yeah, that sounds good.
The… the other thing that… I did see… Man, I'm trying to think of where… It might be in the specification.
It's like, Trask wrote, like, this dashboard?
Thing?
maybe… Sorry, I'm…
**Nimrod Avni** 16:06 I think I saw it in the profiler as well.
**Mattia Meleleo** 16:08 Yep.
**Tyler Yahn (Splunk)** 16:08 Yeah, there it is. Okay, cool.
Yeah, so, like, this is another one that's, like, yeah, like, exactly, like, the profiler, where it, like… It helps reviewers, because it's literally, like, giving you a dashboard of things that, like.
You know, as a reviewer, maybe you should prioritize waiting on this, because it's… Waiting for you, But it also, if I'm not mistaken, like, communicates to the authors, like, hey, by the way, like, this is waiting on you after a certain amount of time, so it can automate that process.
So I think… is this… this seems, like, in line with what you were thinking, right? Mattia?
Yeah, does something like this, you know, just a friendly reminder, this pull request waiting on you, yeah.
So yeah, maybe we could try setting… looking to setting this up as well?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:03 Is this the one that needs, like an OpenAPI key, or something.
**Tyler Yahn (Splunk)** 17:10 That's a good question. I think it does. I think you're right, yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:13 Because I… because I asked… Who, who's it? Is that one of…
**Tyler Yahn (Splunk)** 17:20 Trask, you mean?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:21 No.
somebody else had set one up, the PR dashboard, and I asked them how they set it up, and they said it… they said they set it up with a personal open API key, and the only reason they had a personal API key Available was because, they were, like, a hotel maintainer or whatever, and they had an open source key, and they… they didn't mind just coding it into the repo secret.
And so I don't know what we'd do with… Because obviously we have so many vendors involved, and I don't… from what I understood, there isn't, like, an OpenTelemetry, you know, OpenAI API key that we can use.
So, unless somebody is willing to volunteer.
A personal open source key or something.
That was… when I looked at this last time, I kind of got blocked on there.
On that, because on the Grafana side, we only have access to those secrets when it's in the Grafana org.
But obviously this is the OpenTelemetry org, so,
**Mattia Meleleo** 18:26 I don't know where we are.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:28 keys.
**Mattia Meleleo** 18:28 For the profiler, there is this PR here. I don't know if that's enough, or it requires something additional.
**Tyler Yahn (Splunk)** 18:38 Do you want to share your screen? Oh, you're… sorry, see it in the chat.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:45 Oh, they put it as a shared workflow? As long as it doesn't need any secrets from the repo.
Should be good.
Or we could… we could just try it and see if it fails. That's the other thing.
**Tyler Yahn (Splunk)** 19:01 Yeah, right?
Yeah, I mean That sounds cool.
Required approvals? Cool, you can do a bunch of things.
In this… This is the only PR that was required to get that working, Mattia?
**Mattia Meleleo** 19:20 I'm not sure, I just, just had a look at.
**Tyler Yahn (Splunk)** 19:22 Cool.
**Mattia Meleleo** 19:22 his luck, and I saw this one, but maybe we should ask Florina that. I saw he did that for the profiler.
**Tyler Yahn (Splunk)** 19:30 Yeah, yeah, okay, okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 19:32 Yeah, the shared workflows repo is very new. I think they're trying to move more and more workflows into there, so the ZSMOL one came through.
Yeah. The other week, so this looks like they moved the… PR dashboard into the shared workflows repo, too.
**Tyler Yahn (Splunk)** 19:49 Well, cool.
Yeah, Mattia, did you want to try to also set this up? Do a PR there?
**Mattia Meleleo** 19:58 Yeah, sure, in the tomorrow as well.
**Tyler Yahn (Splunk)** 20:01 Yeah, okay, cool.
That, yeah, that'd be great, Grab that.
Okay, alright, and then next, Mattia, you wanted to talk about AI policy tightening. Reviewers, maintainers should be able to read PR descriptions with eyes instead of AI tooling, how to ban wallet text. Ideally, issues also, should also be easily readable, explicitly ask for a reproducer… a reproducer?
**Mattia Meleleo** 20:42 Yes. I don't know how you do the… you usually do reviews, guys, but at least, for example, the PR description, it would be nice to just be able to read it instead of feed it to Claude.
At least that's… that's what I, usually did in the past, that's what I feel it's, it's better doing. So, I wonder if it makes sense to, to put this in policy, like, to have something, readable by humans, not, not just AI tooling.
like, two pages, PR descriptions are… are okay if you feed them to Claude, but it's very… time-consuming for a maintainer that needs to review, like, 10 PRs.
**Nimrod Avni** 21:33 Hello.
No, you see.
**Mattia Meleleo** 21:35 that.
**Nimrod Avni** 21:36 I saw some other, peoples have, like, the… down, like, in the checkboxes, you have something like, I, a human, wrote this, description, or something like that.
I mean, that doesn't enforce anything, but maybe… We can… like, and we know everything is, like, assisted by Clutter AI and stuff, but if we can… I don't know.
I don't know if it should be, like, hand, curated more than, like… kind of, like, short and concise, and give, like, examples of how we expect a PR description to be in, In, like, not a wall-of-text thing, but more of, like, a… like, I noticed, like, every… every time I got AI to write some description, it does, like, a lot, okay. What's changed? And it lists all, like, the files, and what's changed, and I think maybe we should aim for, like… What's, like, you know, general, like, what's… like, in general, what's the purpose, and then, like, some sections of… reviewer guidance of, like, you know, I had a couple PR where it's, like, you have, like, a lot of files that are kind of repeating, so you don't need to pay much attention to it, but here is, like, the main thing you should pay attention.
And I don't know, maybe we should think of… not mainly the template, but more like a… Like, guidelines.
**Mattia Meleleo** 23:07 Guidelines, yeah.
**Roy Reshef (Kubex)** 23:10 You can also… that's something that we did internally.
for both a PR, for staging a PR, and for reviewing a PR using AI, you limit them by… I mean… One thing these tools do, they… they… You know, like… walls of text, or everything, even PR comments, which are… so negligible that you don't want to read 2,000 words or 2,000 characters for it. So, we just limited them.
And… and tell them, okay, figure out the 5 most important things in this PR, and limit yourself to 1,000 characters, or 2,000, or whatever you want.
Yeah.
Yes, it's not gonna be maybe 100%, but at least it, eliminates the walls of text.
It's a problem, I mean, everywhere.
**Nimrod Avni** 24:08 Yeah, right. I'm still thinking, like… Because some, like, PRs that are… like, touch many places, and many files might need, like, longer descriptions, but you still need to…
**Roy Reshef (Kubex)** 24:22 You can have classifications, you can have, depending on the amount of, files touched, or lines of code changes, you allow a bit more, or things like this. I mean, you can make it a bit more flexible.
**Tyler Yahn (Splunk)** 24:37 Yeah, I mean, I'm… I'm like… I don't think there's actually a rule that you can apply that catches all of them. Like, just from.
**Roy Reshef (Kubex)** 24:45 Not harm.
**Tyler Yahn (Splunk)** 24:46 I've written… I've written, you know.
10 lines of code, and I've… I've personally written well over 100 lines of description, because, you know, it's an API change, and I'm explaining all of these things, and I'm including benchmarks, I'm including all these other things, like… It's… Yeah, like, I mean, I'm also, like, trying to understand, because, like, I don't really mind seeing a lot of information. I really, yeah, I mean, I get that, like.
seeing stupid information that's, like, redundant, like, files change, like, I can go look at a file list somewhere else. Like, that's not helpful, right? But, like… You got 15 different things that are being included in this PR. I do like to see that. Actually, I prefer that because then it's easier to say, like, hey, maybe this PR is doing too much, right? Like, maybe we need to break this apart. I do like seeing, like, what verifications you've actually run, and, like, what sort of testing has been done.
But yeah, now…
**Mattia Meleleo** 25:48 The wording is very difficult, though, to read, like, very convoluted words and…
**Tyler Yahn (Splunk)** 25:54 Yeah, yeah, yeah. Like, like, yeah, like, AI slop wording. Like, it's… it's… has meaning, but there's also a bunch of, like, filler words and all this other crap, right? Like, yeah, like, I'm… yeah, like, that's not helpful. I… I agree.
**Nimrod Avni** 26:06 redundant, like, even the verification stuff, like, saying, you know, you ran unit tests, it's like, okay, but CI does it as well, like, I don't mind, you ran unit tests, like, I need to see… I want to see, like, the, like, stuff that won't be caught automatically, I guess, right?
**Tyler Yahn (Splunk)** 26:26 That's true, but also, like, if you tell me that you ran unit tests, yeah, that doesn't mean anything to me. But if a brand new user ran unit tests, like, that means that they've actually, like, tried something. I guess is kind of where I'm saying, like, it is helpful to see, like, they did put some thought into, like.
you know, testing. It wasn't just, like, an afterthought. But yeah, I hear you. Like, you know, maybe verification's not as important, unless it's something outside of what CI is gonna run.
That's fair. I could see that.
But I also think that, like, all of this stuff can be encoded in our AI policy, right? Is that where this is going, Mattia?
**Mattia Meleleo** 27:05 Yeah, yeah.
**Tyler Yahn (Splunk)** 27:06 Okay.
Yeah, I mean, like, I, I would love it if we could focus on that AI policy to provide better descriptions, if folks are going to be using AI to write these, like… in ways that are helpful to you, like saying things that, like, you know, don't put verifications that are just gonna be run by CI, don't put filler words, like, try to speak like a human, try to, like… be concise, try to, like, you know, optimize this for a maintainer to, you know, actually read this, not just a, like, information dump. All of these things aren't great.
I definitely don't want to go in the direction of, like.
requiring a human to write the description.
**Mattia Meleleo** 27:50 No, I agree. I think AI written is fine, as long as it's understandable and not super sloppy.
**Tyler Yahn (Splunk)** 27:57 Yeah, I agree, yeah. The more… the more it can provide, like, value to the maintainers, that sounds good.
Yeah, I… yeah, okay, cool. I mean, anything you want to do there, I mean, I think if there's, like, more… than even just the PR descriptions that we could start looking into for these policies. But yeah, we can at least start here, right?
**Mattia Meleleo** 28:21 I think we can just put some guidelines in the AI policy, and we can see where we go from there.
**Tyler Yahn (Splunk)** 28:28 Yeah, I mean, I definitely think you could put in hard restrictions, like, don't list the files changed.
But yeah, like, I agree, let's go there, yeah.
Roy, do you have any, like… Copies of… AI policy stuff that you could share in this situation?
**Roy Reshef (Kubex)** 28:53 I… I have to check, because I did not set them up, There was someone else in my team, and we have both, you know, cloud source repos, like, on our Bitbucket org, and… and open source repos on GitHub.
I can check out if I can share anything like this.
Yeah. And if I can, I will, yeah.
**Tyler Yahn (Splunk)** 29:19 And maybe even if just, like, you could take a look at our policy, take a look at your policy, and see, like, hey, like, here's this class of things that we found to be useful, and just making something there, yeah.
**Roy Reshef (Kubex)** 29:29 Yeah, I can… I can try to do that, yeah, sure, Tyler, no problem.
**Tyler Yahn (Splunk)** 29:32 Cool. Yeah, that'd be helpful. Thanks.
And then, Mattia, you're gonna take a look at this as well. It looks like you got another action item.
**Mattia Meleleo** 29:39 Yeah, sure.
**Tyler Yahn (Splunk)** 29:40 Okay, cool.
Oh, man, I just… Sorry, I saw a block of code that has AI used both as artificial intelligence and action item, now I'm, like… Having a brain fart. Yeah, Okay.
Cool.
So, next up, I wanted to just go over, the V0113 milestone. Specifically, I kind of wanted to, I wanted to pare this down. It's kind of funny that we're gonna, like, I think bypass this release, and then I'm trying to pare it down as well, but, like, Maybe it's just funny to me. I think there's some things in here that, like… so this is supposed to be the, essentially, the milestone that we have before we go, like, 1.0. So essentially, this is, like, the catch-all, these are the last things that we're trying to actually get done.
We have a goal to get this done by November, but that means that, like, we need a release candidate out in… sometime in October.
It's already September. I'd love to get the release candidate out, tomorrow, but… That's probably not gonna happen. So, so I did wanna, though, like, see if we could try to accelerate this a little bit. One of the things that, like, did stand out to me after working on this for a little bit is, the… this migration, of end-to-end coverages. I've, like, gone over it, like… I think there's gonna be a considerable amount of work. I don't think it's, like, on… like, tenable, but, like, I'm also asking the question of, like.
do we need this, for a V1? Like, this is a testing strategy. Like, obviously, like, I… like, we have some tests for the config… V2 already in place, but, like, the config migration so that we're only using the config v2, like, I don't think it's, like, a strict blocker for the, you know, 1.0 release.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 31:53 That sounds reasonable.
**Tyler Yahn (Splunk)** 31:54 Okay.
I'm gonna pull this out of this milestone, then.
Okay.
So, okay, and then on that line, I kind of just wanted to ask, like.
Is there anything else in here that kind of… doesn't make the cut, like… Some of this, like, some of the complicated cleanup and hardening stuff, I think it's nice, but I'm not actually 100% sure we need it for the VE1 as well. So I was thinking maybe moving these two out, but I also have PRs for them, so I'm like.
You know, probably worth just leaving them as is, but maybe deprioritizing the reviews of these if we have other things.
I did want to call out, though, that, like, the telemetry, like, contract stuff and, like.
what we're actually doing with this registry does seem like a V1 blocker. Nimrod, is that something in line with what you're thinking as well?
**Nimrod Avni** 32:57 Yeah, I think… I think it makes sense to get a full at least the contract out, like, maybe the coverage tests and all those stuff can be, like, more of a improvement to the CI, but I think the contract of what we omit, what we should omit.
is… is, like, a blocker. I think once, like, I have the PR open, like, once that is merged, that's basically the full contract.
And beyond that, like, we can do… like, improving it and testing it to make sure that we cover everything, and we might… like, I think I exposed most of the stuff that we kinda, thought we emit but don't, and other… and vice versa.
But maybe we'll, like, find more with, like… I did… I ran, like, those coverage tests locally, and I found a couple stuff, but maybe as we go running it in CI, we find more stuff.
But yeah, I think that's the main, like, this PR is, like, the main thing that's blocking, so maybe the defining the V1 telemetry contract can be a blocker, but… Doing, like, the full registry coverage can be, like, you know, like, less of a blocker.
**Tyler Yahn (Splunk)** 34:17 Right, okay.
Yeah, that's kind of what I was thinking as well, so that seems in line.
With what I would say.
Okay, cool, then let's definitely leave that in. I think also this, line OB network attributes with OpenTelemetry semantic conventions. Oh, that's the network attributes specifically, I guess.
Yeah, I did want to ask about this, because I don't think this is… gonna get done. Just based on, like, how fast we've been seeing this move. This has spawned off an entire networking SIG.
So, I'm wondering, like, thoughts on moving this out of the V1 as well?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 35:01 Yeah.
I think that makes sense, right? Because… The, we don't know how long this is gonna take.
**Tyler Yahn (Splunk)** 35:09 Right.
Okay.
I will… I'm gonna take that as an action, because I also see it's in this parent issue, so I need to update that. But, Yeah, sorry, was somebody else gonna say something? I don't know if I heard.
**Giuseppe Ognibene (Coralogix)** 35:21 Yeah, no, I was saying the same thing of Steven. We… I mean, we are working on that, but… I don't know.
It's been a long, long journey.
**Tyler Yahn (Splunk)** 35:33 Yeah, it is. It's… it's a… Massive project. So, okay.
I think… I think, well, I think I'm just gonna pull that out of here so I don't forget that it's not gonna be in this, milestone.
And then… yeah, we'll… I'll update the original issue as well.
Giuseppe, what about the Rust Tokyo context propagation stuff? Do you think this should be… Still something we can get done? Something that is gonna make the cut?
**Giuseppe Ognibene (Coralogix)** 36:04 Yeah, I mean, I had to work on Node.js random matrix, but… I will talk with, internally and see… If we need to prioritize it, or remove it. I will let you know.
I'm not sure.
**Tyler Yahn (Splunk)** 36:24 Yeah, yeah, yeah, no, that sounds good. I mean, yeah, we don't have to know in the meeting.
This should be out, but anyways, choice print header is duplicated. Yeah, so then we start to get into, like, things like this, where it's, like, there's just bugs. I think I've got, like, a track on this, But, like… I'm also wondering, like, I don't know if these need to be, like, hard blockers, given they've been in for a while. I do think it'd be nice if we could resolve them before we get a 1.0, but I'm also, like, not 100% sure that, like, it needs to be… needs to be resolved. It's not gonna be, like… looking at this as far as I have, like, and other issues, but, like, I feel like there's, a very low chance there's gonna be API breaking changes, that are going to be needed to fix this, I guess is kind of where I'm coming from. And so, like, if this is a bug, like, I think that we can… Debug this after the 1.0, is also my thought.
That being said, like, 1.0 is a signal, you know, saying that, like, it is production ready, so… known bugs going into it are, obviously, we're gonna have bugs going into it, I think it's just more about, like, triaged bugs that we know that we can fix in that timeline, I guess is kind of the question.
But… Yeah, is there anyone with a strong opinion either way on that?
**Giuseppe Ognibene (Coralogix)** 37:54 I…
**Nimrod Avni** 37:55 Sorry, Peter.
**Giuseppe Ognibene (Coralogix)** 37:57 Not just one thing, I'm not sure, but, sometimes when… I mean, I just want to not work on something that I'm working on, I just, search for to-do in the repo. There are some to-do that are features, or, like, I don't know.
left there, but I think that maybe some of them is, it can be a bug, or, like, the… the owner of the code thought that maybe it can be a bug, so maybe we can, Check.
**Tyler Yahn (Splunk)** 38:33 So your suggestion is to, like, do an audit for to-dos before the 1.0?
**Giuseppe Ognibene (Coralogix)** 38:40 Maybe. Not sure if it's a good thing to do.
But the…
**Tyler Yahn (Splunk)** 38:45 Yeah.
**Giuseppe Ognibene (Coralogix)** 38:46 enough to…
**Tyler Yahn (Splunk)** 38:47 I think that's… that's helpful, The way I've classified it, though, is that, like, if it hasn't risen to an issue yet, then I don't think it's, like… I go by the motto, like, I can't care more than you, and so, like, if somebody thinks it's a good to-do, like, I agree, like, put it in code, like, that sounds good, but, like, if they don't think it has risen to the level of an issue, like, I… I can't.
But… If you would like to, though, like, if you want to go through and find all the to-dos and see if there are things in there that need to be issues that we track, and then we can add them here as blockers, like, I'm not saying don't do that, but, like, yeah.
**Giuseppe Ognibene (Coralogix)** 39:25 Yeah, yeah, I can do that. Actually, I'm doing it in my free time, but I can start to degrade issues if I'm thinking it's a… It's good. Okay.
**Tyler Yahn (Splunk)** 39:37 Let's also keep in mind, though, that, like, scope-wise, like.
the 1.0, like, RC needs to go out in, like, a month. Like, we have, like, 4 weeks left, so… If you're finding you know.
issues that are gonna take years to do, like, we're probably not gonna accept them into the scope. So, yeah, just a heads up on that one.
**Giuseppe Ognibene (Coralogix)** 39:58 If there is a to-do that will take years to do, I don't think it's a to-do. I mean, it's…
**Nimrod Avni** 40:05 Yeah, you'd be surprised.
**Giuseppe Ognibene (Coralogix)** 40:06 more.
**Tyler Yahn (Splunk)** 40:08 Yeah, I've written some bad reviews before, so, yeah.
Don't look at my old code. Cool, alright.
**Nimrod Avni** 40:17 I wanted to say, sorry, I wanted to say that I think, bugs… like, I think also, kind of right to what Steven wrote, like, that we need to differentiate, like… I think the worst type of, like, the main zone we want to kind of hack out before is anything that can impact the runtime, like, that goes outside of the OB scope, anything that can affect… you know, user, application, runtime, whatever, and we should try to eliminate as many of those as we can before V1. And then after that, it's probably, like, correctness guarantees of, like, you know, like, we expect this metric to, whatever, this thing to emit, and it doesn't. So, like.
like, not… not gathering data correctly, or, like, something that even affects only Obi itself is probably better than anything that affects anything outside of OB.
**Tyler Yahn (Splunk)** 41:16 Okay, I agree. That's definitely where I'm leaning to at this point. Like, I definitely thought it would be nice to clean things up, but I also, like.
I think what you're saying, and this is just double-checked, so things like… This Obi, the fan-out stuff, like, yeah, so the fan-out asynchronous, like, obviously is a bug, because you can have blocking behavior, right? But it's also not one where, like, if we go 1.0, we can't fix it afterwards, because literally all we have to do is change internal code. And so what you're saying is, like, this should probably get bumped, is what I was thinking as well, right?
**Nimrod Avni** 41:50 Yeah, and then I… I don't know if, like, the thing with, like, trace parent header, being duplicated, I don't know if it might… it probably can affect anything that, like, consumes… I don't know, it might consume, the setter duplicate and might cause other issues, so that can be bumped up, I don't know, like…
**Tyler Yahn (Splunk)** 42:11 I agree. I think, I think that transparent header.
Sorry, when you say bumped up, you mean, like, bumped out of the V1, right?
**Nimrod Avni** 42:21 I'm saying maybe… I don't know if that… if this can affect any, cut, you know, user applications, this might be, like, more important and needs to be prioritized for the V1. Hmm, okay. But if it doesn't, like, if just, you know, if it's just some, correctness issue.
Then, you know, because we know, like, for example, that bug with, like, the… in TLS stuff, I don't know, when you… when we kind of inject data where people don't expect it, some… Customer applications can handle it incorrectly, and refuse connections, and reject requests, and… All that type of stuff. I don't know exactly the full scope of this.
**Tyler Yahn (Splunk)** 43:01 Oh, okay, I think I see what you're saying now, sorry, I wasn't catching it. So what you're saying is that, like, the application that we're instrumenting, if it's affected, we should definitely include that in the B1, and then if it's telemetry going downstream to, like, some sort of, like, observability system, that may not… that shouldn't make the cut, is what you're saying.
**Nimrod Avni** 43:16 Yeah, I think at least, like, prioritization-wise, like, we need to first, like, the most important thing is, like, to not, you know, not be disruptive of, like, anything that runs besides Obi as much as possible, like, besides the, you know.
**Tyler Yahn (Splunk)** 43:31 I see.
**Nimrod Avni** 43:32 the documentation of what we do, and and after that, we should probably fix, like, logical bugs, and, like, the telemetry that we should have made, and even… and then after, like, that, like, internal stuff, like you're saying, with, the Q Metadata fanout that can cause, enrichment lag.
**Tyler Yahn (Splunk)** 43:51 Yeah, okay.
So yes, there's things… so I think this… Yeah, I think this is… this is the one… I thought these were linked, but, this is the one I was actually looking at. So this is, like… another one where, like, it's injecting, like, the trace parent header twice, right? Based on, like, if there was a pre-existing HTTP2 connection and whether it had, like, that header or not. And so what you're saying is, like, if this is overwriting something that an application's already sending, like, that's actually a bug we should fix for the V1, right?
**Nimrod Avni** 44:18 I think so, yeah, and let's, like, let's see what you think, if it makes sense.
**Tyler Yahn (Splunk)** 44:22 No, I agree, I think that's a great, metric, or, demarcation. So yeah, I think that that's great. Let's do that.
I also think that's great, because I think this, this, and this are all related, so, and I'm pretty sure I already have a PR for it, So, yeah, let's keep going in that direction. And I think those are, like, the last big bugs outside of this cube fan out, but I think that might be something we can fix after the fact.
Okay, actually, yeah, let's… I'm gonna move this out as well, and then… unless there's an objection… It's moving this out.
Again, we can always move back in.
Okay, cool. That looks good. I think that's pared down a little bit. I think… Are we at 12 issues to go?
Okay.
That looks reasonable.
Yeah, this is also something… okay.
Cool. Alright, then I think, like, with that said, like, the top priority PRs that need review, I think, are Nimrods, right? With, the schema and the registry. So let's… let's… I'll try to get those out as well.
And then, working on this, this transparent stuff.
Yeah, actually, I think we have a track… you know, for 4 weeks from now, I think we should be making an RC, so that does sound good. Okay.
Maybe sooner, that'd be great. I'm always super worried, Because you always get an RCO, then… People come out of the woodwork asking for you to get things done, and included in the actual 1.0, so… Okay, sorry, jumping back into the agenda really quick, nothing else is written there. Any other topics folks have, or things they wanted to talk about?
**Mike Dame (Odigos)** 46:22 I just wanted to bring up, quickly shout out the, thing that I mentioned in Slack about I'm gonna be… talking to this college course for the school that I went to. It's a computer science class. They do a semester-long, contribute to an open-source project. A lot of the ones that they usually find are kind of smaller games and simple apps and stuff, and so I met and I was talking to them and said, hey, this is a real thing. Would you guys be interested in me, promoting it there? So, I'm gonna be talking to them about that. We'll see if we get any takers. The students get to decide which projects they work on, obviously, and I'll let them know that this is a little bit, higher level than I think most of the projects that come along there, but, definitely some very real-world stuff, which, you know, I think… I honestly think that this project, taking it in this class would be… Like, equivalent to an internship in terms of experience that you get.
So… any of those big to-dos that we were talking about, or issues or things that you come across, feel free to open up issues, and yeah, we'll see if we end up with any students this year, or if not, I might end up just, like, doing a workshop with them during the semester, and kind of showing off Obi and trying to get some people interested. But, you know, looking to pull in some more contributors. It'd be great to kind of spread the good word a bit.
But… Anyone that wants to join in with that, feel free to let me know, but it all comes down to… Does anyone pick our projects want to take on the challenge for their semester? It's definitely, I don't think, going to be an easy A, but they… they do take it pretty seriously in this class, and the professor also talking to him, he really, like, encourages, you know, good… good contributions, and we'll see. I'll keep everyone updated.
**Tyler Yahn (Splunk)** 48:13 Cool. Yeah, that's… that's great.
One other thing, I think, on that line is that, like, the KubeCon in North America's coming up, and we're doing ContribFest, this year as well, which is awesome. This is another one where, kind of similar to what Mike was talking about, we're looking for, like, people that want to make their first contribution to OpenTelemetry.
In the past, I've definitely… I've run it once, and, like, we… and I've been to a few of them, but, like, they… they look for… Before the actual event, good issues, for… for new people to be working on.
So, I expect… like, before that, you know, in, like, the Go one, just for reference last time, I found, like, issues that are gonna take, like, you know.
fix the spelling here, or, like, do this really quick. Like, something that is gonna take, like, five lines of code to actually resolve the issue. So, like, those kinds of things, like, if we have a lot of those, that'd be good.
I think for Mike's stuff as well, having smaller issues is helpful, just to get your, like, feet wet. So, yeah, I think, like, just a heads up, like, there'll probably be some ask for that in the future, or me just creating a bunch of issues. But yeah, it'd be cool just to think about it in that way, yeah.
What's the timeline, Mike, for when they choose their project?
**Mike Dame (Odigos)** 49:31 The semester's starting now, the project pitches are happening, like, this week and next week, and then I think they kinda gotta pick pretty quick, so we should know in the next couple of weeks, but… Yeah, small issues would be great, even if there's anything that you think could take a little bit longer, too. Any extra library support, stuff that they can kind of measure throughout the semester, but besides that, I think, you know, it's all about the attending the SIG meetings if they can, and, you know, contributing to issues and stuff like that, so it's an all-around.
class. It's not just measuring commits, and so, yeah, we should know soon, but we'll see. If I was in school, I don't think that I would pick Obi as my project when I'm… I've got a lot of stuff going on, but I'll try to make a really good case for them, because I think that the experience that you can get out of it is… Very valuable.
**Tyler Yahn (Splunk)** 50:24 Yeah, I think so. That'd be cool.
Okay, any other topics, things people are working on?
How many people are gonna make it to KubeCon North America?
Yeah, 1. A 2.
Yeah, Mike, you've got to talk to her phone already.
**Endre Sara** 50:47 I should have said this, but You might have known this, there is Cocoon Shanghai next week.
**Tyler Yahn (Splunk)** 50:59 I didn't, but… no, okay, yeah.
**Endre Sara** 51:02 And Haibin, who is, contributing to especially the AI stuff, asked me to present with him.
**Tyler Yahn (Splunk)** 51:10 Nice.
**Endre Sara** 51:11 I'll be in Shanghai.
Anybody's coming to Shanghai next week?
Not next.
**Tyler Yahn (Splunk)** 51:18 That'd be awesome.
**Mike Dame (Odigos)** 51:18 Yeah, that's cool.
**Endre Sara** 51:21 So, yeah, there is… before COBICO North America, there is a OB presentation about Gen AI Instrumentation in Shanghai next week, on Wednesday.
**Tyler Yahn (Splunk)** 51:34 Obviously, like, the talks recordings take a little while, but can you please make sure you post the recording when it does come out? Yeah. Yeah, that's awesome.
Yeah, that's…
**Mike Dame (Odigos)** 51:44 with, I'll be with Rafael. We have… a, observability Day, and then a KubeCon main pack one, too. So, it's kind of…
**Tyler Yahn (Splunk)** 51:54 Oh, nice.
**Mike Dame (Odigos)** 51:55 Twins.
**Tyler Yahn (Splunk)** 51:56 Are they the same talk, or are they different talks?
**Mike Dame (Odigos)** 51:59 No, no, the observability Day is kind of on the, like, vending stuff that I've been really working on, and the dynamic API, and I really want to show how OBI can be vendored and built on top of. And then the main track one was really Raphael's idea to do, like, a deep dive into the…
**Tyler Yahn (Splunk)** 52:15 Yeah.
**Mike Dame (Odigos)** 52:15 code, so even though he's not still contributing with us, he's, still gonna be, you know, speaking for us in spirit, and I think that he, he's a good person to have on stage there, so… We've got some good ripples.
**Tyler Yahn (Splunk)** 52:27 I saw a contribution.
**Mike Dame (Odigos)** 52:28 across the world.
**Tyler Yahn (Splunk)** 52:29 Yeah. He's still around once in a while, yeah.
**Mike Dame (Odigos)** 52:32 Cool, cool.
**Tyler Yahn (Splunk)** 52:35 Well, cool. Yeah, that's awesome. That's actually really exciting.
Two talks, that's… Man.
I'm jealous.
Yeah, I know people that, like, submitted, like, 5 different talks and, like, got 0 accepted, so it's definitely rough sometimes, yeah.
**Mike Dame (Odigos)** 52:50 I mean, Reshao must know how… he said he's never been to a KubeCon before, and he's never submitted a talk before, and he must know something about it, something about having him on a… on a submission, because I always submit talks, I never get stuff accepted, but we went and we did these two, thinking, you know, play the, you know, submit as many as you can, and then… Get the first one, and then get the second one, and you're like, oh…
**Tyler Yahn (Splunk)** 53:14 I know, that's always the thing.
I thought…
**Mike Dame (Odigos)** 53:18 There's people that are interested in.
**Tyler Yahn (Splunk)** 53:19 5. I was like, you're gonna get all five accepted, but yeah. Yeah.
**Mike Dame (Odigos)** 53:24 Good problems to have, right?
**Tyler Yahn (Splunk)** 53:25 Yeah.
**Mike Dame (Odigos)** 53:26 Excellent.
**Tyler Yahn (Splunk)** 53:28 Okay, well, cool. Alright, we can probably end the meeting here, then. Thanks, everyone, for coming. we'll see you all in a week's time, and, we're executing. Until then.
