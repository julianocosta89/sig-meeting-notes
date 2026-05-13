SIG: .NET SIG
Date: 2026-05-12
Duration: 48 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello** 04:56 Hey.
**Matthew Hensley / Grafana Labs** 05:01 Hello.
**Martin Costello** 05:54 I know Raj isn't coming today, but I don't know about Alan.
**Matthew Hensley / Grafana Labs** 06:09 There's been a decent selection of other folks showing up last few weeks, but… Doesn't seem to be the case today, potentially.
**Martin Costello** 06:18 Even the AI note-taker left.
**Matthew Hensley / Grafana Labs** 06:21 I told her to leave.
I was deeming it… Trying to figure out what commands this one responds to.
**Martin Costello** 06:33 Oh, I didn't know you could do that.
**Matthew Hensley / Grafana Labs** 06:35 Yeah, this one supports leave.
So it's slash FFLEAVE.
But a number of them, if you just start spamming, stop and leave, they will drop out. Now…
**Martin Costello** 06:50 I'll remember that next time.
Is there anything you wanted to discuss today?
**Matthew Hensley / Grafana Labs** 07:20 Oh, let's see… I did have… One thought, You all are… been hacking on the Prometheus exporter, trying to get it into shape.
actually compliant.
Might be worthwhile looking at some updated benchmarks.
the Prometheus.net client has some.
Built in for their meter to Prometheus bridge stuff.
And, yeah, they're… they're years old now, so some updated… Comparisons might be useful.
**Martin Costello** 08:00 Okay, I've, I've put a Prometheus end-to-end one in my… Other repo benchmarks.
But it didn't work because of a bug, which… is the fix for it. It got merged about 5 minutes ago.
So I might be able to get those working again.
Later tomorrow.
There's a ton of microbenchmarks, but I haven't looked at… see what there might be in the… in the Prometheus client we might want to borrow.
**Matthew Hensley / Grafana Labs** 08:35 Yeah, they're pretty straightforward, but… Considering the performance discrepancy that was… Recorded a few years ago.
Probably worth… trying to include them. It didn't look great at the time, A while back, I did… Hack them enough to run again.
And the, the gap had closed, and actually, in some cases, the hotel exporter was faster now.
**Martin Costello** 09:06 Do you happen to ha- know or remember What the difference was, and what sort of… roughly what the numbers were, because I have done some changes.
for performance improvements.
As part of the work, but they're… Stuck behind a bunch of other improvements that haven't been merged yet.
**Matthew Hensley / Grafana Labs** 09:30 I'll try to dig up… That stuff, I'm sure it's just lurking on a branch somewhere.
**Martin Costello** 09:41 I didn't even miss the… Matthew Hensley / Grafana Labs 09:46 So definitely not necessary to stabilize the Prometheus export or anything, just… some, Just some maintenance stuff that might be worth considering.
**Martin Costello** 09:58 Yeah, I've sent you a link to where I've got up to so far.
Which has got the absolute numbers in it.
Obviously, if they have not… the other ones haven't been run for years, then… It's not… it's not apples for apples.
But, you know, if we were talking, like, milliseconds versus microseconds, then… Probably a bit more competitive now.
**Matthew Hensley / Grafana Labs** 10:24 It was, mostly, if I recall, to do with… memory usage?
Unless… Anything with CPU time?
**Martin Costello** 10:42 Yeah, because, in the… the PR I've got pending is… there's quite a lot of allocation improvements, especially on .NET.
rather .NET framework.
But most of it's just from piggybacking… piggybacking new APIs, like the UTF-8.
Stuff for formatting, rather than doing anything radical.
And there's… and there's also… there's also… because I basically just threw Copilot at it to find… Interesting things to do, and, like, one of them was… Don't turn the strings of the meter names into bytes every time you serialize it, just cache it.
And stuff like that.
**Matthew Hensley / Grafana Labs** 11:32 Oh, yeah. Yeah, that's nothing too… Crazy.
I'm looking for these old… Benchmarks might have to go… digging, but I'm… very surprised if I would have deleted them.
These are some, Nice numbers, though, at least as far as an improvement over the baseline there. Even for .NET Framework.
**Martin Costello** 12:17 Yeah, I was surprised when the numbers came out that it had got noticeably better for .NET Framework as well.
**Matthew Hensley / Grafana Labs** 12:34 Yeah, I'm… I'll try to find these later.
Sleutin' through… My files, and… all my work trees for the SDK and contrib are… Following the results.
**Martin Costello** 12:57 Yeah, there's no… there's no rush on getting the numbers, but it'd be… it'd be, like, if it turned out that the old numbers Are nearerish, the new numbers.
Then they'll sort of deprioritize it.
**Matthew Hensley / Grafana Labs** 13:14 The, now, I remember in most cases, the gap had closed, if not… Then, it was Prometheus, the Prometheus.net client that was slower.
Surprisingly.
**Martin Costello** 13:28 Alright.
Thanks, I had a look at it the other day, and it's still, you know, 3 years with no anything.
Hang on.
**Alan West** 13:41 Hey, how's it going, y'all? Sorry I'm late. I had a contractor show up at my house.
Yeah, how's that Prometheus stuff going?
**Martin Costello** 13:57 It seems to be going in a positive direction.
**Alan West** 14:02 Cool.
**Martin Costello** 14:02 Mostly stopped on it at the moment, because I'm… you know, trying to change the same line of code in 5 different ways at the moment, so that the PR stacking is sort of… restricting them.
how far I can cope with it.
**Alan West** 14:19 Gotcha.
**Martin Costello** 14:24 But yeah, me and Matt were just discussing, performance… the performance of it.
Compared to the… the abandoned Prometheus client.
**Alan West** 14:37 Yeah, you know, again, I was never really involved with the Prometheus exporter all that much, but I know that, team at Microsoft spent quite a bit of time Trying to make sure that it was pretty performant. Is that… What you're seeing.
**Martin Costello** 14:58 So, with the latest… Copilot Advised improvements.
It's a lot faster again now.
**Alan West** 15:08 Cool.
**Martin Costello** 15:10 But, yeah, I am waiting for… I've got about 5 PRs, which are, like, fixing spec non-compliance stuff to go in, and then once that's done, I've got a PR that builds on top of all of those.
That, does stuff like use the new UTF-8 formatting overloads on .NET, and… caches some stuff that you don't need to do repeatedly and stuff like that, so… the numbers I just shared a link to with, Matt, it's, like, it's about… 5 times faster in some cases.
**Alan West** 15:52 That sounds good.
What's the… Prometheus supports OTLP now, so what's… What do you see as the use case for people using the Prometheus Exporter? I've always just been curious.
**Martin Costello** 16:11 From my own experience at my old job, I think it was mainly that there was existing infrastructure in place.
So, you just sort of tell your existing Prometheus scrapers To call your hotel services, and then you've got, like, continuity of approach if you want to move?
So you can sort of do both at the same time.
**Alan West** 16:34 I see, I see, yeah, so, like, kind of, like.
If you already have existing Prometheus infrastructure in place.
Then it just makes it easy.
**Martin Costello** 16:45 There might… there might be other use cases I'm not aware of, but… Me picking all this up is mainly driven by, them trying to stabilize things.
**Alan West** 16:57 Yeah, makes sense, makes sense.
Cool.
I don't know. Did y'all have anything else you wanted to discuss?
**Martin Costello** 17:10 I put a couple of things on the agenda.
The first one was last week, or was it the week before? Raj mentioned something about, like, labelling.
To try and, like.
provide an easy way to see what things should be looked at sooner rather than later, in terms of PRs.
**Alan West** 17:32 Oh, yeah, yeah, yeah.
**Martin Costello** 17:33 But we don't… we haven't agreed on what we should actually do for that. So, it was like, does anyone have any opinions on how we should do that? And then I can start actually applying that.
**Alan West** 17:47 Right, yeah, probably would be worth getting Raja's.
Thoughts on her, since… I guess he suggested it.
Why not?
**Martin Costello** 17:56 That's cool. Because, yeah, I put these items on the agenda, like, you know, like, 7 hours ago. Yeah. At lunchtime, my time, so I didn't know Raj weren't coming at that point.
**Alan West** 18:05 Got it, got it.
**Martin Costello** 18:11 So, the third one is… I've been… I was chatting with Jay, who's in my team, who's one of, you know, works on the hotel Java stuff, and also the Ecosystem Explorer, which currently only documents the Java instrumentation, so it would be good to get .NET in there.
an external contributor.
is done some work that I did a review on at PR in the Ecosystem Explorer earlier today to, like, sort of scrape NuGet for packages and work out what there is that way. But in Java, the way the have it is… there's effectively, like, metadata files in the repo that declare what instrumentation there is, what version of the semantic conventions it implements, what attributes it emits, etc, etc.
is that a direction we'd want to go down as well? Because… I don't think we really have a structured way of working out what's actually implemented at the moment, other than reading the code, or reading the README files.
**Alan West** 19:22 Yeah, right.
I mean, unless AI was able to sort it out for us. I think that, I think that's… I would assume that that's probably what the Java… folks did, right? They probably just got really structured in their way of documenting what they produce, so we… Probably want to do something this similar.
**Martin Costello** 19:47 Any, any, like, firm opinions on, like, how that should be? So, one big file, a file per library, YAML, JSON…
**Alan West** 20:00 I suppose it could be cool to have it as part of… like, I'm imagining per… Per instrumentation library.
Where maybe there's some auto-generated, like, human-readable documentation?
But also, you know, in a format that… could be consumed by the… by the ecosystem Explorer, I guess?
**Martin Costello** 20:32 Yeah, because I, I, I think… Once we've got a vague idea of What we would want in the repository.
then we can, like, set an AI in it to do an initial pass.
**Alan West** 20:44 Huh.
**Martin Costello** 20:45 But I figured there was no point in doing that yet, with at least getting a vague agreement. You know, because if we run this on Contrip, and suddenly, you know, a PR appears with 50 files of YAML, and everyone's like, what the hell is this?
**Alan West** 20:59 Yeah, yeah, yeah. You're right, right, right.
**Matthew Hensley / Grafana Labs** 21:02 So, if we, stick to Weaver's newly stabilized V2 schema. It has all kinds of fun tooling, like a templating engine to generate docs.
So… Most of… you get a lot of it kind of for free, if you stick with their stuff, and it can be consumed by Weaver, of course, if you… Use that schema, so if we wanted to… Like, with the live check stuff, you were… Looking at Martin.
He kind of off-heed itself.
Yeah, no.
**Alan West** 21:39 affected Weaver all that much, so, I mean, it seems like the community's Trying to standardize on a way of representing these things.
Is that right? Is that essentially what the Weaver project is mostly about?
**Matthew Hensley / Grafana Labs** 21:53 Weaver's a… CLI that does lots of things, but it's just tooling to deal with the schema format. So, like, validation of the schema, you can point OTLP exporter, some different things at it, and it'll tell you what's coming across, and does that fit the schema? Like.
you know, using a deprecated field or something. It also generates documentation, And a whole host of… Other fun things.
**Alan West** 22:29 Well, that'd be cool. I mean, it's… I mean, I suppose it always would always be great to leverage what the community's building, and that way we can… Maybe continue to improve it, and… If it needs to.
**Martin Costello** 22:41 Yeah, because I was… chatting to Matt earlier on Slack, like.
this afternoon, just for a couple of hours, I did some hacking around with Weaver to try and do some, like, spec compliance tests.
The contrib I think I've got enough.
for me to, like, park and come back to in, like, a week or something and do some more. But the idea was just sort of go, here's some instrumentation, implement this version, does it look right?
And, like, it's fleshed out, like, one or two things that I need to look at. Like, the tests fail at the moment, but… If we could put them into the existing tests in some way, it might sort of help with iterating on, like, keeping semantic conventions up to date, and that we don't break things, and things like that.
**Alan West** 23:34 Huh.
**Martin Costello** 23:36 But yeah, it's the same as, like, if we… Do something that… Weaver's happy with, and we did it, like, per project.
Then, that'll be the right direction to try and move in.
to light up ecosystem Explorer.
long term.
**Alan West** 23:59 Yeah, it sounds it, and it sounds like that would be a pretty convincing direction to… I think for anybody that might, chime in.
**Martin Costello** 24:09 what I might do tomorrow is… Do a quick bit of research on, like, what the file format might be.
for Weaver, and then pop up, like, a Help Wanted issue.
and then cross-reference it into the Ecosystem Explorer, because Jay's been getting a lot of people helping contribute over there, including the PR I looked at today to, like, try and do an initial hydration of the .NET support.
as, like, a phase one without actually putting anything in the .NET repos. So maybe we could get, some of those people to, like, help Add those files once we know roughly what we want them to be in terms of format.
**Alan West** 24:55 Nice. Yeah. Okay.
**Matthew Hensley / Grafana Labs** 24:58 I have… quite a bit locally. I can make a branch against, like, the Redis instrumentation, just as an example of Kind of what Weaver can do.
Super basic one.
**Martin Costello** 25:15 Yeah, that'd be cool, because then if we've got, like, sort of, like, the golden template example.
Then we can just point people at it and go.
Do this, but for all the other ones.
**Alan West** 25:34 Cool. Yeah, I'll have to take a look at the Ecosystem Explorer. I've heard about it, but I've not actually… Played around with it much, so… Well, that sounds great, though.
**Martin Costello** 25:48 And then the final thing I wanted to discuss is… If you cast your mind back to last year, and we did, like, harmonized all the versions?
**Alan West** 25:59 Yeah.
**Martin Costello** 26:00 Now, there's a bunch of Microsoft people complaining.
Because now we've shipped a bunch of CVEs that affect every version.
Turns out they're using really old versions of one collector.
and other libraries, and they don't have the fixes, and they're running .NET Framework services, and the fact that we picked target latest for .NET Framework is causing them a bunch of grief.
I'm trying to push back on us doing a new version that rolls those backwards, because we'll only roll them forwards again later, when they go out of support anyway.
But it's raised questions about, oh, should we do back ports? But I don't know what our official Sort of support policy is on how far back, in terms of versions, we'd consider backporting anything for.
**Alan West** 26:58 Hmm…
**Martin Costello** 27:01 Because it's… reading through the comments, it seems like what happened was… People were using the latest.
And then… version 1.10 moved… took everything up to 9, so a bunch of users just stayed on… 1.9, because that was .NET 8.
**Alan West** 27:23 Sorry, 1.9 of the hotel S.
**Martin Costello** 27:24 Oh, sorry, yeah, they were using 1.9 of the OTel SDK because it depended on .NET 8 dependencies.
Okay. Then 1.10 took the dependency on .NET 9 and moved everything up to 9, so those users stayed on 1.9, and then 11 and 12 and 13 did the same thing with .NET 9, and then 14 Was the one that went up to 10 for 10, But 9 for 9, 8 for A… but for Donnit Standard and DONIT Framework, it went to 10.2.
Then we had 15, which was the same.
And then we had all the CVEs, so then we patched 115.
So now all the users who are still using 1.9, Because they want .NET 8, Don't have patches.
**Alan West** 28:17 Yeah, got it.
**Martin Costello** 28:19 I'm pushing… Back on doing back ports.
Unless the… unless it's very… Constrained in exactly which ones.
And or there's, like, a support policy that says no.
We don't care about that anymore.
Because I couldn't easily find something if we do have something that says how far back we'll go.
**Alan West** 28:45 Mmm, yeah, I mean, no, we've never really made any, policies about that. So their .NET framework… And… Technically.NET Framework should be able to use the latest SDK, right? 1.15, whatever.
**Martin Costello** 29:09 Yeah, it's just… it depends… Depending on what you're using, it would depend on, like, 10.
**Alan West** 29:17 Right, so it creates that… it reintroduces that friction that they were trying to avoid with having to upgrade all of their Microsoft extension dependencies.
**Martin Costello** 29:28 The .NET Framework, it doesn't reintroduce it, it never went away.
It's… it's just… it was 8 in 1.9, then in 1.10 it moved to 9, and then in 1.14 it moved to 10.
So.NET Framework has just continued to move forward, so the changes I made last year were more fixes… were… fix things more for 8, 9, and 10.
And I think… Like, I actually… I went back and looked at the issue, and in the… you know, the justification of why I thought we should do what we did in there. I think I've written something like, for .NET Framework, it's not tied to the 8, 9, 10 release cycle, so might as well just use the latest.
**Alan West** 30:16 Yeah, okay, yeah, that's all, that's all jogging my memory, so… And .NET, I guess the extensions packages all are… they're support… lifecycle is all tied to the major version of .NET, right? So, like, 8 is… Data's out of support now, right?
**Martin Costello** 30:38 8… 8 and 9 go out of support in November.
**Alan West** 30:41 In November, okay. I see.
So then I guess the question is… okay, I think I'm catching up now. So the question is… Because technically, 8 and 9 are… NET 8 and 9 are still in support by Microsoft.
Should we… Support… any security fixes… CVs… for older versions of the SDK that depended on Older versions of the extensions packages that are still under support.
**Martin Costello** 31:19 Yeah, because, like, the different outcomes for the issue I've linked to, I can think of, are do nothing.
release a 1.16 for .NET, standard and .NET framework.
Moves the dependency back to 8.
But then we'd move it forward again in November, which is why I'm hesitant to do that.
Or we could pick an old version and go… We will backport to this very specific old version.
These specific targeted fixes and nothing else.
And it's still on you to, like, you need to work your way forward.
**Alan West** 32:05 Yeah.
**Martin Costello** 32:10 And also, we could potentially revisit the thing that we did last year with the view to 11, and for 11, not move .NET Framework and .NET Standard to 11 in November, and keep them at 10.
So then it would sort of naturally kind of do what they wanted from 10 onwards, going forwards.
But wouldn't help them now.
**Alan West** 32:38 Well, then I think the reason why you made the decision that you did was because then the question is, like, when do we upgrade the .NET framework targets?
**Martin Costello** 32:47 Hmm. Because I think eventually we'll get to a point where the SDK will shout at us and say that it's not supported anymore.
**Alan West** 32:58 Oh, right, so sure. So, like, 10… we'd upgrade… we'd upgrade the .NET framework targets only once Whatever version they're pinned to.
Goes out of support.
**Martin Costello** 33:09 Yeah, so, like, potentially, when 11 comes, we leave .NET Framework at 10.
And then, next year.
for 12, we still leave them at 10, if I've got the years right. And then the year after that, when 13 comes along and 10 drops out of support, then we'd move to 12 or 11.
**Alan West** 33:33 Yeah, okay.
**Martin Costello** 33:33 They'd move… they would move forward at the pace of the oldest supported version.
And the others would stay in the lockstep, so 12 gets 12, 13 gets 13, 10 gets 10, 11 gets 11, etc.
**Alan West** 33:46 Do you have a sense from the discussion that whether they'd… That would appease them.
That idea, it sounds like it wouldn't help them in the immediate term, but…
**Martin Costello** 33:58 It wouldn't help them immediately, And it would… Give you longer to upgrade.
**Alan West** 34:06 Right.
**Martin Costello** 34:07 But you would still eventually have to upgrade your stuff.
**Alan West** 34:11 Right, right, right, right.
**Martin Costello** 34:12 Because I don't think we can just pin the .NET Framework ones at 8 forever, because then it just becomes a nightmare for us to support it.
**Alan West** 34:27 Yeah, I don't know. These things are always… this has always been a sticky thing for us.
**Martin Costello** 34:35 Because… because part of the reason I've not just, oh, I'll do a back port, is one.
Has CI changed in a way that means it's difficult or not possible to build from those old tags anymore?
And also, has the code changed so much that you effectively have to write the patches again from scratch?
On the old versions, because the code has changed so much.
**Alan West** 35:02 Right, yeah, yeah, totally.
And that may very well be the case for some of the things. I mean, I don't know, some of the code that was probably patched hasn't actually changed in a few years, but yeah, no, I mean… You never know until you get into it.
**Martin Costello** 35:17 Hmm.
**Alan West** 35:18 Hmm.
**Martin Costello** 35:19 Because there's only two specific patches that have been asked for, but I don't think they've properly answered all my questions yet, which is, like, which exact version is it you're running?
I think one of them hasn't, it's like 1.9, but I think the other one they haven't.
**Alan West** 35:44 Yeah, I guess I'd be leaning towards the do-nothing approach, at least until we, you know, learn more and… I wonder if, since these are Microsoft teams, whether Raj could, you know, influence this at all.
**Martin Costello** 36:05 Yeah, I did… I did tag, Raj onto the sheet, but he hasn't chimed in yet.
**Alan West** 36:11 God.
It's difficult. He might be able to gauge, like, you know, the amount of impact this is actually having across… across teams.
**Martin Costello** 36:22 Because I think… Sorry, come on.
**Alan West** 36:24 I was just gonna say, if it's just, like, one team just kind of struggling with this, and they just opened up an issue, but, you know, that's… It's not a huge problem, then, you know, maybe… maybe that team just needs to figure it out for themselves, right? But if Rod finds out that this is, like, a more systemic problem that's, you know… causing a lot of grief across a lot of teams, then, you know, maybe he could… maybe Raj could bring more of a case to… What we should do.
**Martin Costello** 36:54 Except, I think the other thing that's confusing things as well… is, one of the CVs is in one collector, and that's that component that only Microsoft uses.
So then it's like, if you're on a really old version of one collector, why are we bothering building new ones?
**Alan West** 37:14 Yeah.
One collector is, yeah, I don't know. I don't even know why that's in the Contrib repository, honestly.
There was a point in time where there were some other vendors, exporters.
In the contrib repository, like, I'm talking, like, 5, 6 years ago.
And… We removed them, because they were, like, vendor stuff, and we just decided, like, they should be… vendors should… control.
Their destiny there, but then… The one collector and that other exporter, the Geneva one, Somehow, just kinda… slipped in there, and they got, like, the OpenTelemetry.prefix in their NuGet package, and… I always felt like that was kind of… kind of an odd decision from Microsoft people, who had originally advocated for Vendored things not having the open telemetry.
Prefix in their… in their packages.
Huh.
**Martin Costello** 38:17 Because it feels like they're coming to us complaining about a thing that's effectively theirs.
**Alan West** 38:24 Yeah. Yeah, I don't… Yeah, I, I, I… I'm inclined to withhold sympathy Based off of the current fact pattern.
I think, I think if we learn more, if Raj can dig into the details and we learn… we learn some more, facts of the situation and how this might… you know, be problematic for OpenTelemetry users more broadly.
then… then I'd… That would be more convincing to me.
**Martin Costello** 39:02 Yeah, because I… as well, I don't think they've been properly following the issue, because they were like, oh, why don't you just use VA? It's got all the APIs you need, and it's like, well, no, it doesn't, and it says that in the issue I linked you to.
**Alan West** 39:16 Yeah.
**Martin Costello** 39:18 Because we, depend on new metrics APIs that were added in the V9 of diagnostic source.
And then someone… I just noticed someone left a comment this afternoon that they're using 113.
So… It's like, if we did backport, we'd have to backport to two different versions?
as well.
So, it's… it's, like… And there's part of me as well that just doesn't want to just continue the flip-flopping from one position to the other that's happened over the last few years.
**Alan West** 39:57 Yep, yep.
**Martin Costello** 39:58 Latest, oldest, latest, oldest.
Because no one's ever happy.
**Alan West** 40:04 Exactly, yeah. No, I think we should… we should stick, we should stand our ground.
Again, until we hear more broadly that there's a more substantial problem here than Than maybe we're… we're seeing.
**Martin Costello** 40:21 And also, potentially, like, if it was that important to the… I think it's the team's team, which is always a confusing thing to say. But, I'd have a bit more sympathy if they'd maybe, like, gone, oh yeah, we went away and looked at how much work it would be to do a back port, and here's a PR.
**Alan West** 40:42 Yeah, right.
**Martin Costello** 40:42 But they're just, they're just basically just going, make me a fix, please.
**Alan West** 40:46 hmm.
Yeah.
**Martin Costello** 40:55 And, you know, it could be the case.
this is just me making a stability. It could be that it's just their builds are failing because of the warning, but they don't actually use the vulnerable code, so they could just suppress the warnings.
**Alan West** 41:11 Totally, yeah.
Yeah, do they actually have a compatibility problem with the later versions or not?
Who knows?
Well, cool, yeah, I guess… I guess, what do you think? We just… let's wait for… let's wait for Raj's input, and…
**Martin Costello** 41:33 Yeah, that's what I'm inclined to do, is I think… if there was, like, one specific version and one specific CVE, And they were maybe a bit more inclined to, like, help investigate how much work it would be to backport it.
Then they may be considered, but they're just going, oh, there's issues.
We want fixes. Oh, by the way, we're not using the current version.
**Alan West** 41:59 Yeah.
But…
**Martin Costello** 42:02 The thing I'll keep… consider maybe for the .NET 11 branch.
is maybe for net standard and net framework, we pin those to 10, or leave them on 10.
in November, rather than moving them to 11, except for Diagnostic source.
**Alan West** 42:19 Yeah, that's a worthwhile point to circle back to, maybe when the larger group is here.
We can… we can discuss that.
In more depth again. And I think the other thing, maybe, to… to discuss… In another meeting is… Just slipped from my mind.
Well, I guess they're just our policy. I mean, I guess, you know, these particular people's issues aside, when Microsoft Extensions is still under support, should we change our policy?
You know? Just generally speaking, or not.
I don't know, sounds like a lot of… Lot of toil.
**Martin Costello** 43:14 Yeah. Still working.
**Alan West** 43:15 Still worth talking about, I think.
**Martin Costello** 43:18 Hmm, because I think… Hence, last year, we've had, like, 3, 4 minor races?
13, 14, 15, I think. So, like, fit… so, was it the other week when we were doing all the CVEs, or was that… 10 different issues, spent about 2 weeks on it, and that was just… for Maine.
**Alan West** 43:46 Yeah, right.
**Martin Costello** 43:47 Like, we would have spent a month doing just fixes for all of the ink supports in quotes.
versions to be able to do that, and we just don't have the time.
**Alan West** 44:01 Right.
No, I agree. And I think… I think it's still worth having the conversation about the policy, though, because, like, to your point of, like, what if they had come and said, here's a PR against this one version?
Then it kind of sets… even that would kind of set a precedent for, like, well, why are you backported it to that version, but why not this version? So then… what would our policy say? Like, if you do the work… Then… Then we'll accept it, or… I kind of feel like we should be maybe a little bit more black or white, you know, in this kind of a… In this kind of situation. Yeah.
**Martin Costello** 44:41 Because the thing that… Concern isn't the right word. I'm not concerned, concerned.
But, like, if we did just create a new branch based off 1.9, and do all the… and do whatever the patch is, it's like, is the GitHub action… all the GitHub Actions workflows using versions that actually work on the runners that are available today?
**Alan West** 45:04 Huh.
**Martin Costello** 45:05 like, what if they're using Node 18, which doesn't work anymore? So then you've got to update all the actions, and then does the… do the workflows for doing, like, the package publishing Have they… do they work with things built against older versions, where files they might expect aren't there anymore?
Or aren't there yet. And then suddenly it's just this explosion of… Trying to maintain, like, 4 different versions of a release pipeline.
porting every change we made to the release process across X number of branches.
Because, yeah, I think you're right, it's like, unless we… we need a policy.
And then when we have a policy, we can work out what the consequences of it are.
Because… because otherwise, you could argue, if we backport for one of these.
and it's a vulnerability that's been there since version 1, then people could justifiably pop up and go, oh, I can have a 1.1, I can have a 1.2.
Yeah. And then we've got to backport it 15 times.
**Alan West** 46:16 Yep.
Yeah, it… I don't know. It also just bugs me. I mean, this is… This is… kind of beside the point, but it's just always bugged me that we have all these dependencies on all these Microsoft extensions libraries.
Should never have happened.
Shit should never have happened.
I wish we could go back in time.
a lot of this pain… I don't know if all the pain would have gone away, but I think a significant amount of it would have.
Anyways… Yeah, let's pick it up. Let's pick up the conversation again when… when Raj is here, and maybe, I don't know if you've talked with Peter about any of this, but .
**Martin Costello** 47:06 No. I think this got opened right at the end of… Oh, no, this is true. When did the last… right, so the thing that brought it back, since otherwise it hadn't been touched since March, which was basically me going, oh, we'll probably do nothing.
There's… the Microsoft people chimed in last week, so I think Piotr was about to go on vacation.
**Alan West** 47:32 Gotcha.
**Martin Costello** 47:33 I haven't spoken to him about it.
**Alan West** 47:35 Right.
Alright.
**Martin Costello** 47:40 Tomorrow, I'll create an issue as a placeholder, just to track that we should discuss what the support policy should be.
**Alan West** 47:52 Sounds good.
Cool.
Thanks, man.
**Martin Costello** 47:59 That was all I had to… Discuss?
**Alan West** 48:05 Alright.
Anything else?
Nothing from my end. What about you, Matt?
**Matthew Hensley / Grafana Labs** 48:12 Nope, I'm good.
**Alan West** 48:14 Right on.
Cool. Alright, y'all, well, good catching up.
**Martin Costello** 48:19 Did you say?
**Alan West** 48:20 Talk to you soon.
Bye-bye.
