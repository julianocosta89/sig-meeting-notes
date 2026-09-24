SIG: Semantic Convention Tooling
Date: 2026-09-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Arianna Vespri (OllyGarden) 00:01:36 Hello?
Jeremy Blythe 00:01:41 Hi.
Arianna Vespri (OllyGarden) 00:01:43 How are you all good?
Jeremy Blythe 00:01:46 Yeah. Yeah.
Those things. You're working on the… Spandex, right?
Arianna Vespri (OllyGarden) 00:01:53 Yes, now I have to resolve.
conflicts.
Again, also the… A cough code was, complained, yeah, because there is this… Carrier pattern that… Keeps on changing, so… Yeah.
And but it's okay, I mean, I'm working on resolving the conflicts now.
Jeremy Blythe 00:02:18 Okay.
I'm just seeing this… I think the Miller's on vacation.
Laurent's always busy doing other things these days.
So I'm just wondering if Josh is gonna show.
Arianna Vespri (OllyGarden) 00:02:33 Yeah.
Jeremy Blythe 00:02:34 Otherwise, this is not going to be our trigger meeting. Oh, hang on, here we go.
Arianna Vespri (OllyGarden) 00:02:40 Hello, Josh.
Josh Suereth (Google LLC) 00:02:42 Hey, sorry.
Some previous meeting ran over.
How we all doing?
Arianna Vespri (OllyGarden) 00:02:49 Oh, good. How about yourself?
Josh Suereth (Google LLC) 00:02:52 Not bad, not bad.
Somehow today, I managed to fill my calendar completely with meetings, till the end of the day. Pretty good, right?
Jeremy Blythe 00:03:04 It's not.
Arianna Vespri (OllyGarden) 00:03:04 I…
Jeremy Blythe 00:03:05 What is the win?
Josh Suereth (Google LLC) 00:03:09 Yeah. Alright. I haven't had a chance to look at the meeting notes, sorry.
Jeremy Blythe 00:03:14 around, honey. I'm just… Copy-pasting now.
Josh Suereth (Google LLC) 00:03:18 Gotcha. I gotcha here, I'll help.
Okay… Alright, and I'm behind on code reviews this week as well, so apologies.
Jeremy Blythe 00:03:46 That's what I was gonna… That was the only thing I was going to bring up is, I've got a couple of… At least two, I think.
Josh Suereth (Google LLC) 00:03:55 Yes.
Jeremy Blythe 00:03:56 I actually think… Pretty good.
Josh Suereth (Google LLC) 00:03:57 If you're okay, we should, we should, I'm being very tactical, but I was thinking we could go through issues and pull requests quick to make sure we're, like, paying attention to them. There's some good pull requests in the queue.
And I want to make sure that we're actually, like, getting reviews on them and things here. I'll… I'll share.
One thing Lyudmila mentioned last week.
was, we might want to do a stale review bot. So, waiting on reviewers and maintainers is, like, on us, right? So, findings on resource samples carry… resource attributes. This is one, you know, if you can look at this, Jeremy, that'd be ideal. It's about 36 days old now. It does have conflicts, so I don't know if we do anything with that, but it's got, It's got one approval, I think it's a good PR, generally, but…
Jeremy Blythe 00:04:50 Yeah, I think one's ready to go, actually. Apart from the complex, it was just ready, so we were… Maybe we were waiting… The conflicts to be resolved.
Josh Suereth (Google LLC) 00:05:00 Okay, we should probably ping and say, hey, as soon as conflicts are resolved, we can merge this.
I'm gonna go in reverse age order, because, well, I should say, this is one that I think we should just close. It's like, It's a little bit stale now, it's something I think needs a lot of discussion, and It's… it's over a year and change old, right?
Jeremy Blythe 00:05:22 Yep.
Josh Suereth (Google LLC) 00:05:23 Docker Build Cache, and CI, I remember looking at this one, it has conflicts, and I don't actually know… I don't know if we need to optimize our Docker build in CNCF, but we might need to eventually. It's… not super critical, but it just sort of got dropped, right? This is another one that I think, it's a proposal around V2 that… We basically are deferring almost all of these until we're done with, with V1, or sorry, until we get V2 kind of out the door, and then we can do… non-breaking extensions and changes, and that's what I think this is.
This was another one.
Regex captures filter to extract catcher groups.
I think this one had some conflicts. I don't remember reviewing this one, but I feel like I did. This is an addition to Forge.
Have you seen this one, Jeremy?
Jeremy Blythe 00:06:33 That's not one I've looked at.
Josh Suereth (Google LLC) 00:06:36 Let me, let me pull it up.
So yeah, I think it just adds this regex captures filter.
which returns a regex match and an additional capture group. So it's like a filter for, Jinja, to make Jinja templating easier.
But I didn't actually… I don't know. I was trying to figure out, when I first looked at this, whether or not this is something Jinja should be providing.
For us. But we do have regex Replace. So this is just kind of the same thing.
But it's, like, 30 days old, I think we should probably review it, merge it. It's like… it's a good little change. I think it's something we should review and approve, or not, you know what I mean?
Jeremy Blythe 00:07:21 Yeah.
Josh Suereth (Google LLC) 00:07:21 Okay.
And I think that's also one of those.
Jeremy Blythe 00:07:25 First issue.
Josh Suereth (Google LLC) 00:07:25 Thanks. What?
Jeremy Blythe 00:07:27 Whoa, 109, that's, that's old.
Josh Suereth (Google LLC) 00:07:31 Yeah.
Yeah, that was when we were first going. It now… I don't know why it conflicts, I guess we added another extension, but… Okay, let's go back to the pull request dashboard.
For things that we need to talk about. This one… this one is actually… These are… there's a bunch of these that I think we have to have a discussion about that are somewhat problematic.
So this is one where… Local pass get truncating with at, because we use at to be a,
Jeremy Blythe 00:08:07 It's for the ref spec, yeah.
Josh Suereth (Google LLC) 00:08:09 Yeah.
And so, this thing here is they're actually changing how we parse, where at is only treated as a ref spec if we're in a Git repo.
And I forget how they were using RevSpec.
Anyway, I… I think that there's a… there's a series of, like, VDERT sorry, virtual directory, like, bugs and issues here that people are submitting fixes for, that I don't know if we want to do a wholesale think about, The syntax for these, you know?
We've documented what we have, we have kind of naive parsing, we're gonna have to get more robust over time. I'm fine taking on changes like this, but when you look at what's going on here with RefSpec and how we're parsing things, I almost wonder if we should move to, like, a formal parser.
something like NOM, instead of just doing, like, you know, splits and regexes.
Jeremy Blythe 00:09:09 Oh, I see.
Josh Suereth (Google LLC) 00:09:10 Because this is basically saying, like, if it's a URL, right?
Jeremy Blythe 00:09:15 You know, I had a quick look at this one, last night, and I was like, we're, like.
Splitting things, and then we're reforming them again?
Josh Suereth (Google LLC) 00:09:24 Huh.
Jeremy Blythe 00:09:25 It looks like it's doing… it's like… Why is it taking it, tearing it apart, finding that it's… Got an at symbol in it.
And then it's reformat it again with the format command.
Josh Suereth (Google LLC) 00:09:38 Yep, this is just, like, the laziest way to do it that works, you know?
Jeremy Blythe 00:09:43 Yeah, I mean, it's generated, obviously. Everything is these days, so it's just like, ugh.
Josh Suereth (Google LLC) 00:09:51 So, that's where I feel like we should just define a formal parser, a formal spec of what we parse.
And… and if we need to have precedence rules and stuff, we can… we can control it more reasonably. But this is just one of that class of… of bug. So, I… I didn't like this implementation, but I didn't comment on it, because I didn't have a proposal to improve it, and then it just sat here.
I feel like we should do something about it. Okay.
Let's see… That was that one. Here's another one. Fail fast with actual error when local registry.
Dependency or policy path does not exist. This one was interesting. I forget what my comment was here. I did review this, and did they come back? Let's see.
Alright.
So this was, like, a month ago, they came back with that.
Alright, I might have to just re-review this.
Jeremy Blythe 00:11:02 This was one where I then brought up that we were getting these sort of lazy, very lazy, generated PRs.
Josh Suereth (Google LLC) 00:11:13 This is… yeah, because this also touches virtual directory, right? And it was slamming out errors, like, right in the virtual directory path.
Jeremy Blythe 00:11:22 Well, that… The test was never run, even by the… the agent never actually ran its own test, because it would… it would fail.
Josh Suereth (Google LLC) 00:11:32 It failed, yeah.
Jeremy Blythe 00:11:35 And so, I mean, what do you do?
Josh Suereth (Google LLC) 00:11:40 Right.
Jeremy Blythe 00:11:41 Then we had a conversation, like, 2 or 3 weeks back, where I'm like, Well… It didn't even test its own test.
Josh Suereth (Google LLC) 00:11:51 Oh, this is so bad, too, look at this crap.
like… This… this is where I… I'm not… I'm not comfortable even enabling this.
Why is it changing the permissions mode? Is that… oh, because they need to make it unreadable.
Yeah, okay.
Cool.
That's another one where I… I'll do another review pass, but I… I like the idea of what this is doing, I don't know if the value of the quality of the code is worth merging or not. I do want to encourage people to contribute, but that's… that's… there's a line, right?
The other ones I don't think are below the line, this one might be.
Okay. LiveTrek, Benchmark Rego Shared Context.
You reviewed this one, Jeremy.
Jeremy Blythe 00:12:54 Yeah.
Josh Suereth (Google LLC) 00:12:56 Any thoughts or updates on that one?
Jeremy Blythe 00:12:58 This one falls into a category I think we've spoken about a few times, of… Doing, like, a sweep through Weaver to… To, like, optimize the performance.
So there's a bunch of refactoring we could do to improve performance, and… Actually, this… this person did a different PR, which did get merged, but in the process of doing that, I pointed out, oh, there could be an opportunity to optimize here, because we're, like.
I can't remember what it is now, but we're serializing something every time to give to Rigo, when maybe you don't need to, or something or other.
Yeah. And of course.
what this person has is the agent just going, oh, there's a thing that I should do that came up in the other PR, so then it's, like, made a whole new PR with a benchmarking and everything.
You know, I don't have the heart to say… I didn't really need to do it. I just… it's just like a note.
So I basically… I put a note… I put a comment in this PR saying, hey, we're gonna look at doing, optimizing performance optimization soon, so this is gonna park this PR, I think I said words to that effect.
Josh Suereth (Google LLC) 00:14:16 We… we should, we should just close the PR, I guess, then.
If we're not gonna accept it, you know what I mean? Like, I'd rather give a clear signal of, hey, we're gonna do a bigger optimization if you're interested, here's where you contribute, you know?
Jeremy Blythe 00:14:30 Yeah, sure, we can do that.
Josh Suereth (Google LLC) 00:14:31 Yeah. Good.
Jeremy Blythe 00:14:34 we… maybe we need a plan of when we're going to do that. Like, we're going to do the V1 to V2… Split.
Josh Suereth (Google LLC) 00:14:46 Oh, you mean, like, publicly document a roadmap of, like, things we're doing? Yeah.
Jeremy Blythe 00:14:50 Oh, at least within the… at least within the… the team here, right? So that we…
Josh Suereth (Google LLC) 00:14:57 So we know when we can…
Jeremy Blythe 00:14:58 clear… Well, we want to do V1, V2, we need to clean that up.
Josh Suereth (Google LLC) 00:15:04 Yep.
Jeremy Blythe 00:15:04 I think we've had… we've got some, We've got some idea that we want to, like, release some of the crates on crates.io, we don't know where that comes in. Do we want to optimize before we do that? Like… I think we need a little bit of structure, maybe.
Josh Suereth (Google LLC) 00:15:19 Yeah, optimizing after is fine if we feel like the, the… API's not gonna break, but… If the API breaks, that's problematic.
Jeremy Blythe 00:15:31 Like, I think there's… We're doing a lot of cloning.
Where…
Josh Suereth (Google LLC) 00:15:37 We're doing a lot of cloning, yeah.
Jeremy Blythe 00:15:39 We're doing a lot of planning work, we actually went all the way back and made all of our structures use, like, arcs.
I don't.
Josh Suereth (Google LLC) 00:15:49 if.
Jeremy Blythe 00:15:49 Parks is the right thing.
Josh Suereth (Google LLC) 00:15:50 necessarily, Jeremy. Like, there's two things we should think about. One is, we might be able to actually keep the file resident memory, and reference the strings from it with, pointers.
If we're frickin' crazy. The other thing is, actually using a, object pool.
Memory pool.
Jeremy Blythe 00:16:13 Oh, like an arena.
Josh Suereth (Google LLC) 00:16:15 Yeah.
Oh yeah, arenas is the term for them now.
I just gave my age up, anyway.
Jeremy Blythe 00:16:22 I'm sure I'm older.
Josh Suereth (Google LLC) 00:16:25 I don't know. Who knows? Anyway, Yeah, arenas are the… the… yeah, like, we could… we could possibly, like, use an arena or stuff, but I agree with you, like, we're… we're… our memory usage was, and Laurent set this up, and I think it was the right way to start, was until you have a problem that you think memory is the problem, and you've diagnosed that as the problem, you know, like.
Jeremy Blythe 00:16:50 just…
Josh Suereth (Google LLC) 00:16:51 implement code simply, and I think that's fine, but we're at the point now where I think we are fighting a lot of cloning.
Jeremy Blythe 00:16:57 And… but we're also making use of those, You know, we've parsed it out into that… into our… core structure, the SEM core The model in memory.
And then we use… we want to make use of that across, like, lots of different async… lots of different threads for… Right, and so this… There's a bunch of async going on as well now.
And this has cropped up for me a few times in… In the… in Lifetrack, and in the… in the web server thing, with the API, and with, the MCP… So I think this is in consideration of how… Those structures can be used across… Cross-async, more smoothly.
Josh Suereth (Google LLC) 00:17:49 If we need to pass them between threads, yeah.
Basically, like, there's almost a make-everything-send compatible, you're saying?
Jeremy Blythe 00:17:59 Yes.
Josh Suereth (Google LLC) 00:18:01 Okay.
Jeremy Blythe 00:18:02 There are definitely places where we've cloned because we can't send.
Josh Suereth (Google LLC) 00:18:06 Yep.
I also, like, another thing for us to look at is, larger Noom variants. We have a whole crap ton of them.
Jeremy Blythe 00:18:18 Yep.
Josh Suereth (Google LLC) 00:18:19 So we might want to, think about that. And then if we just throw it at a box, that's not necessarily the best option. That's just the easiest one.
Okay, Let's continue a little bit. So you have the benchmark. We have V2 disallow entity refinement without identity. That is a simple, just, I need to review it and approve, and I've been out for basically a week of code review.
So, I'll get to that one. Live check refactoring by OTLP and admin API flow.
This one, is now conflicting. Was that from my merge, Jeremy?
Jeremy Blythe 00:18:58 I don't know, I can go and look at that one, but… Okay. This is… this is… Finally, fixing the problem with stop.
Josh Suereth (Google LLC) 00:19:07 Awesome.
Jeremy Blythe 00:19:08 And it actually came out quite neat, so I'd be interested to see what you think.
Josh Suereth (Google LLC) 00:19:13 Yeah, I'm looking forward to reviewing that one, so I'll try to get to that later today or tomorrow morning.
But I'll prioritize, basically, yours, Lyudmila's, and the one up here that we talked… this regex captures, I think we can get through if we just get the conflicts fixed.
Okay. Support user-provided JQ modules. This one is interesting. Did you… did you review this one?
Okay, so the TLDR is, in Weaver YAML, you can specify new JQ expressions, and they get pulled in along with your template.
So that when people are, when people are writing their… filters, you can use your JQ helper with it.
This reads like a whole bunch of vibe-coded stuff.
Jeremy Blythe 00:20:10 Yeah.
Josh Suereth (Google LLC) 00:20:11 But, whatever. They did tell us that they used AI assistants.
When I was reading the code, let me check and see… my comments should be in here, did they mark it fixed?
Looks like they marked it fixed.
Yeah.
they basically added JQ modules.
paths resolved in relative order and how to add JQ things. They have a test where they use JQ modules, but when I initially read this, the testing was really, really bad. Like, it just was non-existent, where you could actually read it like a human. It looks like now they have an example here, where they have, a model, they have a helper JQ expression, which is that.
And then they have a Weaver YAML that makes use of it, and they probably have a test somewhere I'll have to find that leverages it. But this is, This is basically the feature. I do like this feature.
I need to go re-review the code now that they fixed the test to be legit, but do you have any concerns with this if I were to approve this?
the V-tra.
Jeremy Blythe 00:21:19 I don't think so, but I haven't really looked at it. Maybe I… maybe I can look at that one as well.
Josh Suereth (Google LLC) 00:21:23 Yeah, take a look. The main decision here is that expanding the JQ modules that are loaded is a decision of Weaver.yaml.
not necessarily something you do elsewhere, and I think that's actually right.
And then this is local to the Weaver YAML.
So, I need to go verify that that's actually how they implemented it, but, overall, I think the feature is good.
Okay.
That one has been more recent, that was, like, in the past 3 days, so come on back.
What else do we have going on?
Jeremy Blythe 00:22:04 There were a couple of, yes, of the millers that I have.
Approved.
Josh Suereth (Google LLC) 00:22:14 I mean, yeah.
Jeremy Blythe 00:22:15 The car does good.
Josh Suereth (Google LLC) 00:22:16 That's waiting on authors.
Let's go back here. These are just the ones that are waiting on us to review that I'm going through. The ones that are waiting on the author, like, that's… that's fine, we can get through them later. I'm just trying to do, like, I want us to try to be more responsive, so we're just gonna go through the track all the way down.
Update Docker's renovate, global namespace Separator, I will review that from you.
Yeah, this was the JQ modules and filters, and then everything else is renovate. So then, I think that's it for… Waiting on reviews and maintainers.
I think we're good there.
Cool.
What else do we have going on?
That is just our dependency dashboard, right?
Okay.
If we want to look at open issues that are recent, I don't think there's anything that came in recently that's not from Ludmila.
And the work on the compliance test stuff.
So… Okay.
Jeremy Blythe 00:23:24 Yeah, what I mean…
Josh Suereth (Google LLC) 00:23:25 Good.
Jeremy Blythe 00:23:26 I, I'm just, Just… Working my way through the… Things that are labeled live check and book.
Nice. As a priority, first.
That's… that's where that namespace one came from.
Josh Suereth (Google LLC) 00:23:49 I think that makes a lot of sense to do. I was trying to get through all of the ones that, I guess I could go back to here, under issues.
Cause we actually did, and thank you for this as well, for anyone who helped, but we have really good labels now.
So if we look at, say, I was going through the model ones.
Right. Like, resolution engine and model were the two I was trying to make sure knocked out before we stabilized V2.
But if we look at all the model issues, we still have 129 open issues.
If we filter to the ones that are actually considered bugs… we have 3, and I think Lyudmila actually has PRs open for all of them.
This is one that, This is one we can fix now with the V1, V2 brake, so I was actually looking at going to try to tackle that next.
Disallow entity refinement without identity, and disallow requirement level field for… Yes.
Both of those we can do now.
If we look at features, we have a whole ton of features, I think.
Yeah, like, people just want tons and tons of things in the model that we'll have to address over time.
But that's not as important. Let's go back to bugs.
Then, were there any other labels you wanted us to take a look at?
for, like, a V2 stability, or a V1 thing. Let's just look at all the bugs.
We're down to 10 total that are open.
Live check, model, live check, live check, model, resolution engine, here we go.
Deprecation struct, deserialization, validity of properties depending on reason.
Okay, I'll take a look at that. I think we can do more work there now.
That is… yeah, that's some of the shenanigans we had when we added deprecation.
Just allow… that one's on that. Weaver cannot properly load… oh yeah, this is another interesting one that got blocked.
This is where we want it to load from a directory with a dot in it, right?
We, Should we close this?
Jeremy Blythe 00:26:15 This won't fix.
Josh Suereth (Google LLC) 00:26:16 What?
Jeremy Blythe 00:26:17 We sort of keep saying, no, we don't think it's a good idea.
Josh Suereth (Google LLC) 00:26:20 I know, every time. I haven't pulled the trigger and actually closed it. Should we close it?
And say it won't fix.
Jeremy Blythe 00:26:27 What was Lauren's last comment there, at the bottom?
Josh Suereth (Google LLC) 00:26:31 What else?
Jeremy Blythe 00:26:34 opt-in parameter.
Josh Suereth (Google LLC) 00:26:48 Yeah.
Arianna Vespri (OllyGarden) 00:26:51 Yeah, I know, I know who, I know the author.
Josh Suereth (Google LLC) 00:26:54 Yeah?
Arianna Vespri (OllyGarden) 00:26:56 Yeah, he's an ex-colleague of mine.
And I don't think… you know, I don't know if he actually contributes to open source anymore.
I'm not sure. So I don't know if he's always… if he's… I'm not in touch with him anymore either, but Yeah, I heard that maybe it's not super active anymore.
Josh Suereth (Google LLC) 00:27:20 Okay.
Arianna Vespri (OllyGarden) 00:27:20 So I don't know…
Josh Suereth (Google LLC) 00:27:25 Yeah, I mean, it's… the… Whether or not he's active, and whether or not this feature's a good feature, I think, are two different questions.
Arianna Vespri (OllyGarden) 00:27:33 Absolutely, yes.
Josh Suereth (Google LLC) 00:27:34 So…
Arianna Vespri (OllyGarden) 00:27:35 We're just, we're just, you know, in case, you know…
Josh Suereth (Google LLC) 00:27:38 Yeah, because if we're relying on him to make a fix, that… yeah, that's good to know. We'd have to fix this ourselves. This is more, because I think that he submitted two PRs, both of which I think we ended up not accepting, for various reasons, and I think they closed.
as stale. But the, the question is.
The can of worms this opens is really bad, but they wanted to have, like, a .sendcov directory.
for Semantic conventions. And I'm not sure why they want dot. And we keep talking about this, of, like, why… Why do we need it to be in a dot directory? And the cost of adding dots is dangerous, which is what Lauren's concerned about. If we read through your .git, we read through your .svn, we read through your .cache, we read through your dot… like, all those .files just have a huge ton of crap in them.
None of which are generally relevant for Semcov, and is, like, surprising if you troll through them.
You know?
Jeremy Blythe 00:28:40 Yep.
Josh Suereth (Google LLC) 00:28:41 So, I'm inclined for us to just actually say… We think this is a won't fix.
Jeremy Blythe 00:28:53 Yep.
I agree.
Josh Suereth (Google LLC) 00:29:01 Yeah, okay.
We discussed this in the… ZoomConk meeting.
So, there's a justification on why.
Using, non… dot.
File names is acceptable for semantic convention files.
ZAK the… and let's do not… Justified means the danger of reading.
Your house is rather high.
What's happening.
Look at this.
Thanks. But, more justification.
A recent center… oh.
Okay.
Cool.
What else did we have in terms of bugs?
Because I think that's a feature, not a bug, honestly.
Let's see… Template, set file name, integer is ignored when no output directory is provided.
I think this is sta- like, this might be a won't fix now. Like, this might still be a bug. Do you remember when we had to set filename in the template?
Have you done this at all? Either of you?
Do you remember when, like, when this was a thing, was in 2025?
when we first had Jinja and Weaver, before we updated the, the template syntax where you had file name and Weaver YAML, you… the only way to set the file name was in the Jinja template. We're calling template.setFilename. That was the first release of Weaver.
So, I think this bug is so stale that it's probably a won't fix. I will take a look at, I mean, should we validate it, or should we just mark it as stale won't fix? What do you think?
Jeremy Blythe 00:31:27 I don't really… I mean, it sounds like it's out of date, right?
Josh Suereth (Google LLC) 00:31:31 Yeah.
Jeremy Blythe 00:31:35 this.
Josh Suereth (Google LLC) 00:31:37 Thanks.
Arianna Vespri (OllyGarden) 00:31:37 This was opened by Lyudmila, right?
Josh Suereth (Google LLC) 00:31:40 Yeah.
Arianna Vespri (OllyGarden) 00:31:41 So, maybe she knows if it's stale or not?
like…
Josh Suereth (Google LLC) 00:31:49 Yeah, I'll run it by her later. I don't think… I don't think she cares about this anymore.
So I think it's… we're safe to do this.
There.
And the, template.setFile.
Hooks are still around, but not recommended.
Generally. Okay, I'll do that.
And then we have… Resolution engine, deprecation, that one, yeah. Disallow recording field, that one we will fix.
And then we have Weaver Code Generation Breaks HTML links. This is another rough one, if anyone has time to look at this. This is, Jeremy, you remember this when we were spending time on trying to make comments not suck?
This is where we're trying to take, string and markdown.
And then render it into a comment field.
in, like, HTML form for Java, right? Or HTML form for, what's it called? Doxygen is what C++ uses?
And we keep running into problems like this, where, the renderer… Is maybe splitting things?
Because the line is too long? Because we need a pretty print?
And… Then it dies here because of, it's insane.
HTML start tag prematurely ended, expected end name or attribute. So, what were we killing here? We were killing the LI, Oh, yeah. We decided… we decided… like, this is the frustrating part, right? So we have a hard word wrap limit, okay?
that Go is really particular about.
and we're word wrapping, so the A link comes down here.
And then, because the LI is here, and here on different lines.
Doxygen freaks out in C++ and can't handle it. But if you do it the other way, you break go.
And we, you know, we have one comment filter for all languages, and this is like a flexibility control hell. So, apparently the C++ folks found a way, a working… a workaround, where this no longer is blocking them.
But this gets into, how much work we want to spend on our comment filter. I almost wonder if we… should do some… Like, set up some test specification, where we would have, you know, a template where this works with the comment filter, with the setup, and then go ask an agent to fix it for us.
Jeremy Blythe 00:34:43 What's the… I guess I don't know much about the comment filter, but is this just a thing now that What if I am not using some special thing for comment? Can I… Can't I just write this with a template? And that's the kind of thing we'd have in Weaver packages.
This is, this is your…
Josh Suereth (Google LLC) 00:35:06 ability…
Jeremy Blythe 00:35:07 We've accrued to help.
Josh Suereth (Google LLC) 00:35:10 This is… this is… if you want to write generated code comments that look good or past style guides. Are comment filters the only way that you do that? So this is how you write a Weaver package.
And there's not a good way to solve this otherwise. Like, I can… We… you can look through some of the stuff Lumila did, some of the stuff I did, like, I do think that this should get solved by our comment filter.
It's just, I spent… About 3 weeks in our comment filter.
And I burned myself out on the comment filter.
I think we could probably spend more time now if we get a specification of what we want, but, like, this is a great example, right? Our comment filter, if you read the control for it.
that you have to do it this way for Java.
C++, you can do it this way, and pass style guides, and that's fine.
For Go, you can't do it either of these ways, you have to use just slash slash everywhere, right? So we have this crazy, if you haven't seen it.
Jeremy Blythe 00:36:14 Oh, I've seen it, yeah.
Josh Suereth (Google LLC) 00:36:15 You've seen the, like, like, the amount of controls we have for the comment filter? Yeah.
Jeremy Blythe 00:36:20 Yeah.
Josh Suereth (Google LLC) 00:36:22 But effectively, with C++, there was a particular thing that they were doing that theoretically should have worked, and we couldn't get them a, we couldn't get them a configure that worked. But yeah, all of this control, right?
There was… there's… there's… there's something missing here.
for what they need, and I'm not sure what it is, and we have to detangle it. That's what that one is.
I also think that's something that doesn't block 1.0. That's something we can fix later.
Because I think adding to this doesn't break things.
Jeremy Blythe 00:36:56 I guess my question is.
In the comment… in this comment filter, this is… this is written in a general purpose way.
It's not saying C++ this, Go this, Rust this.
Josh Suereth (Google LLC) 00:37:08 Exactly.
Jeremy Blythe 00:37:08 Written in a very… in a generic way.
Josh Suereth (Google LLC) 00:37:11 Yes.
Jeremy Blythe 00:37:12 Maybe.
We could just have… is this C++? Then you do this. Is it Go? You do this. Is it Java? You do this. Is it… like, we could just have it… instead of having all of the myriad of, like, generic.
Josh Suereth (Google LLC) 00:37:25 Yeah, I mean, that's…
Jeremy Blythe 00:37:27 Don't complain.
Josh Suereth (Google LLC) 00:37:27 end up doing in practice? I… Now that agents write the code, maybe that's a… Maybe that's fine. When we owned and wrote the code and had to maintain it all and read it, that was too painful.
Jeremy Blythe 00:37:39 Oh, totally, I understand that. I guess that's what I'm saying, you know, isn't this… can't you just solve the whole thing in Ginger with an agent now, anyway?
Josh Suereth (Google LLC) 00:37:48 Yeah.
what we want for that is we probably want a test suite, so… Yes. Alright, I… I don't think it's urgent for 1.0, But it's something we can think about adding later, because I don't… adding those doesn't break us.
Last thing I wanted to check, by the way, because I merged the next V1-V2 split, which was somewhat aggressive.
Not agents, I want actions.
Did… have you checked the nightly recently?
Downstream check.
We're passing! Look at that!
Jeremy Blythe 00:38:33 Yeah, I'm pretty sure I get emails if it fails.
Josh Suereth (Google LLC) 00:38:36 I probably get emails, and they probably go to some hole that I don't pay attention to.
But… Yeah, like, we're passing, so I think… The next thing to talk about would be… Release planning.
It's about that time of month again to try to cut another release, right?
Jeremy Blythe 00:39:01 Yep.
Josh Suereth (Google LLC) 00:39:07 Let's see… for Ginja 2.
I think… Here, we should just add those active PRs that we have, right?
This is the one that you have a PR for, right?
Jeremy Blythe 00:39:28 you know.
Josh Suereth (Google LLC) 00:39:29 Yeah, okay. I'm gonna move it into here.
Is this part of that PR, or is this separate?
Jeremy Blythe 00:39:39 No, that's different.
Josh Suereth (Google LLC) 00:39:40 That's different, okay.
Jeremy Blythe 00:39:42 That's, I think that's what Cidrew brought up.
Josh Suereth (Google LLC) 00:39:46 I'm gonna move this over, because I think I can cut that.
Do you think we can get our PRs in and try to get a release next week?
Jeremy Blythe 00:39:55 I think so. I think if the act… if the… if the active PRs we just went through, I think if they all go in.
They're the most… Especially the stock one.
And they were, like, the worst bugs.
Josh Suereth (Google LLC) 00:40:10 Yes.
Agreed. Okay.
Jeremy Blythe 00:40:14 than programming, yes.
I'd like to do a bit more.
I guess, real world.
With all… with the… because the next release brings in the live check, with the matches.
Which I know is merged and everything, and I've been doing it, but I… I'll… I'll take some… Time just to… I need… I'm going to convert a couple of things to V2, because I really want to do that. So, like, internally.
In the company. I'll take some of our company registries, and I'll convert them to V2, and then I'll play with… that I just want to have a little more confidence, because it's a big change.
Josh Suereth (Google LLC) 00:41:01 Yes.
Jeremy Blythe 00:41:01 There's tests and all of that, but you know what I mean?
Josh Suereth (Google LLC) 00:41:05 No, I gotcha, I gotcha. It's… until, like, we need to feel the cost of moving to V2.
Jeremy Blythe 00:41:13 Yep.
Josh Suereth (Google LLC) 00:41:13 Not, like, intuitively, not just meant, like, conceptually, yeah.
Cool.
I think we're in pretty good shape here. Is there any… is there anything we need to talk about that, isn't just general, you know.
Project Health following through things?
Jeremy Blythe 00:41:42 No, I don't think so.
I think it would just be nice to have that, sort of.
like, roadmap, almost. That sort of strategy of… I think you started doing one, like… the… the road to get to the stable in V1, or whatever you called it, I think.
Josh Suereth (Google LLC) 00:42:01 Oh, yeah, yeah, okay. Let me… where's our notes?
Okay.
Should make a road to stable slash V1.
So, generally, we have, basically, live check live check, V2, stabilization… We have, V2… Model cleanup… We have, cranes.io publishing.
To make stable.
B1.0 of Weaver.
Jeremy Blythe 00:42:53 We want to do, performance optimization.
Josh Suereth (Google LLC) 00:43:03 Yeah, we can throw these all as tasks.
In terms of the model, we're basically… we have the model cleanup, but I don't think we have anything to add to the model right now, that is needed for 1.0.
I think.
We'll go back through the bugs then, later, but I don't remember anything that was, like… there's, like, mostly removing stuff.
from V1 that we don't need anymore.
Do we think adding enough packages for out-of-the-box things as part of 1.0.
like, out-of-the-box code gen for particular languages. Should that be part of 1.0?
Arianna Vespri (OllyGarden) 00:44:02 I would say it depends on how much work there is, if it's, like, a blocker for the rest, you know, like, the order of magnitude, with respect to, you know, the ratio of, Time that you have to spend, and how, you know, how convenient that is that it… if it… if it delays the whole thing, basically.
So, pros and cons, basically.
Josh Suereth (Google LLC) 00:44:25 Well, I'm thinking about… we could… we could launch a 1.0 of Weaver and not announce it until CodeGen is ready, so we could have a blog post that uses it. But I, like, I'm thinking we want, Python Go… Rest… TypeScript… I'm trying to think of, like, what are the important languages to have CodeGen for these days?
In the ecosystem, right?
Jeremy Blythe 00:44:55 I think…
Josh Suereth (Google LLC) 00:44:57 I don't think it has to be everything.
I just think we need a few to show people what it looks like. Go ahead.
Jeremy Blythe 00:45:04 I think CodeGen's a funny one, because… what I found in the… in the company, In my company is that people want to generate code, but they want to generate code that is gonna fit with the libraries that they use. They've, like, we've got OpenTelemetry helper libraries, like, all over the place to, like, make life easier, and so… And a packaged, out-of-the-box codeGen is, like, We wouldn't use that.
So we just have a template that… you know, an agent has done the CodeGen that's going to fit the libraries that are in use in that project, and it's just there in the thing. So is… when we're talking about CodeGen, are we talking about CodeGen internally in OpenTelemetry projects.
Josh Suereth (Google LLC) 00:45:54 No, this is for people who use Weaver, for people who pick it up and use it.
This is the open… like, this is… so basically, I'll say this, open telemetry Weaver packages that we want, right? And so, in OpenTelemetry Weaver packages, I think out-of-the-box CodeGen and then Docs are the two that, we have… we already have… we have policies, so I think this is… Oh, sorry.
Mostly done, because we have all the SEMCOM stuff in there. Docs, I think, is mostly done, although we might want to do cleanup.
polish as we try it out, use it more.
the out-of-the-box codeGen is the thing in Weaver packages that I don't know how much we'd want before we'd say, hey, this is 1.0, try it out, that sort of thing, you know?
Jeremy Blythe 00:46:47 Yeah.
How… How deep does that… CodeGen, go right, so is it… If it's just sort of making constants from the registry.
Then, okay.
Josh Suereth (Google LLC) 00:47:02 No, I…
Jeremy Blythe 00:47:03 Like, oh, I want to actually define a whole… thing that… Makes functions for generating the span.
Or the metric, or the whatever.
Josh Suereth (Google LLC) 00:47:14 I…
Jeremy Blythe 00:47:14 Like, it gets really complicated really quickly.
Josh Suereth (Google LLC) 00:47:18 Yeah, I think we could… we could start late… I think maybe… we pick a language and do some code gen for it. If you… the talk that Lauren and I had showed, like, some Go prototypes that I think are something we could push for.
But yeah, I hear what you're saying. It gets complicated quickly, and it's a lot of decisions. That's why I'm… but I'm asking, like, if we were to… when we make this general purpose, we're going with kind of a bare-bones approach, which, you're right, like, a lot of people use Weaver today self-service, and they want that high-level customization.
that's cool. There's a group of people who just don't care. They want it to work, they want to get their API, they want to use it. You know, it's like the proto-GRPC style. I get, here's what my classes look like, and I just integrate, and I don't care what they are. You know, I just want this to work, I want it to be defined, that sort of thing.
That's where I think the… we have to cross the chasm from people who are really, really pedantic and want everything to be exactly the way they want, to people who just want observability, don't want to care, want the integration test and all that kind of stuff, but don't really want to go further.
We need to make… give them a happy landing path, you know?
Jeremy Blythe 00:48:32 Okay, so we're going to be very opinionated in the code… in the code gen.
Josh Suereth (Google LLC) 00:48:36 I think we can, but, you know, because we're so flexible, right?
We say, hey, here's out-of-the-box Go, super opinionated, does one thing, does one thing well.
You want to make your own code gen for Go? Go for it. We don't care. Same with the docs. We have a docs thing that people can use.
You don't have to use it, you can make your own.
But we're gonna give you one because it's so annoying to make your own, that if we don't give you one, you might not have docs, and it's more important you have docs that you will then maybe get annoyed enough you either contribute back to the project, or you build your own. We don't care.
Jeremy Blythe 00:49:10 I've already thrown away anything that we did by hand, and I just point at packages now. Like, I made that change.
Because it is just, like… That's fine.
But I think docs, you can kind of go, oh, that's fine, but then code, like, it's gotta… it's gotta work.
Josh Suereth (Google LLC) 00:49:27 Well, here's… here's the thing I… I think I'm… Are we designing for the world of yesterday or the world of tomorrow?
And by that I mean, like, I think there will be people who… We'll just generate code and leverage it, right?
Then there might be people who have an agent go write the template for them, and they just need good docs from us.
And then maybe it's not that high a friction, because the agent's gonna be the one writing the code and scripting it all, and you say, here's what I want my code to look like, go make this work. That's kind of how Ludmila's been doing Python.
with Weaver, where it's… and that's how I did V1 to V2 conversions, because agents are actually pretty darn good at reading… reading doc A, reading doc B, and doing a translation. They can do that pretty well, right?
So, I think there's a class of user that's gonna be that.
What I don't know is, I… I still feel like we should probably support both, where we have a package that has CodeGen.
That does it a particular way.
and… it's there as an example, so if you want to customize, you can say… tell the agent, hey, here's examples. You can read this to see how to do stuff, and it will go customize it to hell for you. Great.
You know what I mean?
Jeremy Blythe 00:50:45 Yeah, so I guess what we want… Maybe what we need is to actually document The… like, we want a spec for… the Kujin.
Josh Suereth (Google LLC) 00:50:58 Yeah, of, like, what would we provide? So this would be in OpenTelemetry Weaver packages, where we'd say… here is the, like, Go code we want to make, here is what the Rust code we make looks like, here's what the… and I think we should start with stable things, so I think, like, Rust… I don't remember if their metrics is stable yet, I think it might be, but maybe logs isn't, so, like… Go, I think their metrics and trace is stable. Logs, I think, is stable now, so we could do all three. You know, Python… I forget what in Python is unstable.
I think it's all stable at this point. But we would, like, use the stable pieces of the API, do CodeGen for that, and you don't have to use it, it's just there.
But it's… it's so that it comes batteries included if you want it. So when we go give conference talks, talk about Weaver, right? You can be like, oh yeah, hey, here's how you use Weaver, and here's the default CodeGen, you know? And it looks like a complete, holistic product.
It's the same reason why, like, Arianna contributing to Docs is super big, because now we have, hey, here's Docs, right? Like, we are a complete product. You can do everything.
Jeremy Blythe 00:52:03 Yep.
Josh Suereth (Google LLC) 00:52:07 So, that's why… but my opinion is 1.0, we'll have the 1.0 release of the engine, you know, of Live Check, the engine, all the, like, baseline components and foundation. But the 1.0 blog post would be when the Weaver package is the initial 1.0 of those. So that should be, like, a set of policies, some amount of code gen, and again, I don't… we could, like… Only target one language, pick whichever one's easiest for us to focus on, and just make sure there's enough of it there that people can infer the rest.
Because I… I also see this as a, what do you call it? The Thundering Herd? No, it's not the Thundering Herd.
If you build it, they will come. There you go.
Field of Dreams, right? So, we make the first one, and then other people are like, hey, why isn't my language supported? And we're like, feel free to write it, and then they send us possibly a vibe-coded thing, but, like, then all the languages show up, you know?
Jeremy Blythe 00:53:01 Yep.
Okay.
maybe do… I think I agree, do… do one language, but do it very completely.
Josh Suereth (Google LLC) 00:53:15 Yes.
Jeremy Blythe 00:53:19 And in doing so, there's a spec for, like, turn, you know.
what we've… Determined is the… is the right thing to provide.
for… A metric, or a log, or, like, one of the signals, each of the signals that I'm There's a sort of a spec that… maybe that spec can be… Hmm.
Used for the next language, but adjust… adjusted slightly.
Yeah. So, I mean, like… I don't know, in one language, It may be really… It may be really easy to have, like, you know, enumerations that you can have additional things in, right? Because in semantic conventions, all the enumerations are open.
But in Rust, that's kind of a hard thing to do. You've got to, like, you know, it's much more strict, and so, like, I can't even use an enumeration, like, because how can I have an… You can.
Josh Suereth (Google LLC) 00:54:27 If you can. There's a flag that you say to say it's an opening room.
Jeremy Blythe 00:54:30 Okay.
Josh Suereth (Google LLC) 00:54:31 And then…
Jeremy Blythe 00:54:31 You know what I mean?
Josh Suereth (Google LLC) 00:54:32 It makes it really confusing for downstream consumers. Have you seen the error messages, by the way, for open enums and REST?
Jeremy Blythe 00:54:39 No, I've not.
Josh Suereth (Google LLC) 00:54:41 Yeah, so you can… in Rust, you can tag in a Noom that says it's open, and then in all of your pattern matches, it says, hey, this Noom is open, and you're not catching for unknown cases. This will crash, go, like, and you're like, what? Like, the first time I saw it, I was really confused, because I'm like, no, I have all the… oh, right, it means there's cases… Okay.
But yeah, I got… I hear you, yeah. Like, in Java, with the Noomes, That would be bad.
to actually have a Noom's be a NUMS, so they might be strings.
Or we have to make our own Enum class, which is open.
That you use, you know what I mean? Yeah.
Jeremy Blythe 00:55:25 Yeah.
I guess we try. I guess we try it. And see…
Josh Suereth (Google LLC) 00:55:33 The…
Jeremy Blythe 00:55:34 Also, things were…
Josh Suereth (Google LLC) 00:55:36 Yeah, the thing there, Jeremy, we gotta look at refinements, too. Like, I think for some of the enums that are open, the refinement is not.
Jeremy Blythe 00:55:45 Right.
Josh Suereth (Google LLC) 00:55:46 And so, like, especially where you're using that as your filter for picking a span, the code gen for those can actually just be a hard-coded constant. Like, it's not even in a Noom at that point.
So, if you're, if you're talking about code genning, just the attributes for lookup and reference, that's one thing, but we're talking about, like, an API that says, hey, record this metric.
that has semantics to it, and I think… It is a ball of wax that we have to talk through, but I think it's a more constrained problem.
I hope.
Jeremy Blythe 00:56:25 So I've been doing some coaching just recently.
And I actually have spans defined for this thing.
Josh Suereth (Google LLC) 00:56:32 Yeah.
Jeremy Blythe 00:56:33 But I didn't co-gend the spans. I just co-gend the constants.
And then… In the code, I'm creating the spans using a combination of the ConfirmTree SDK and, like, our helper libraries and things that we've got.
But how I'm checking that… that code, that… that the whole thing, the whole loop is good as I'm using a life check.
Josh Suereth (Google LLC) 00:57:00 Yeah.
Jeremy Blythe 00:57:02 So… You can be… you can be reasonably thin with the code, Jen, because you want to sort of… it needs to fit nicely in the code.
You know, and I'm… I'm… sometimes if you, like, you build a whole function that's gonna create a span for you, that prevents you from doing things in the flow of your code, because I want to, like, I want to gradually add attributes in as I flow through this code. I want to go and do a thing, and then I want to add an attribute, and I want to go and do a thing. And so… It gets kind of, like… they sort of go, that's horrible now, I don't want that. I can't use that, because now it's preventing me from having a nice sort of flow through my code.
Maybe that's particularly a problem with spans, and it's less so with other things, but
Josh Suereth (Google LLC) 00:57:54 No, with spans, that's important, but again, that's where, when we were doing CodeGen for the SPAN API before, you know how there's the sampling relevant attribute?
Jeremy Blythe 00:58:04 Yeah, yeah.
Josh Suereth (Google LLC) 00:58:05 So basically, what it… what it would synthesize… in Rust, you can see this is basically, Maybe it would be a trade extension method, but it's a thing where… when you instantiate the span, right, you get back a type, which is the span that you're going to be adding attributes to. The only thing that's required in the constructor of it are the sampling-relevant things, so that they hit the sampler. Everything else would have, like, a set or add method to it, or you could add them as a bundle, possibly.
That was… that was, like, the API I defined, like, in Rust. In Go, it was, it's more extension-y. I forget how to describe what we did, but it's in, It's in Lawrence and I talk, how we did Go, where you could, like, add in attributes later.
Jeremy Blythe 00:58:51 Yep.
Josh Suereth (Google LLC) 00:58:52 So I think… like, again, it depends on the language, but I think there are ways that we can do what you're saying, and give you the access in a thick client. I still think, though, given this discussion.
And I listed that in the thing here. We should… we should think about a constants-only and a thick API for our… for CodeGen, and we should just recommend that all the time. So, you as a user, you want to do constants-only, you want to control your CodeGen, we'll give you a constants-only thing.
You want a, like, a more thicker client, a more, like, opinionated thing that takes away some of the pain, so maybe you don't need your hotel helpers, because this does it for you.
Jeremy Blythe 00:59:30 Yep.
Josh Suereth (Google LLC) 00:59:31 We can… we can make a client library that does that as well.
And Arianna, if you're looking for interesting ideas of things to toy around with, or proposals.
This would be a wonderful thing to pick a language and help us out with, of say, hey.
Arianna Vespri (OllyGarden) 00:59:44 Okay.
Josh Suereth (Google LLC) 00:59:44 No, I want to write instrumentation, yeah.
Arianna Vespri (OllyGarden) 00:59:48 Yeah, absolutely. Absolutely, I mean, why not? Let me, let me, let me think through that and see what, you know.
what I could be doing there. In the meantime, I'm still, you know, I'm still working on the span links thing. I'm, like, resolving conflicts for the… for the third time, but it's gonna be okay.
Josh Suereth (Google LLC) 01:00:08 Oh, sorry, yeah.
Arianna Vespri (OllyGarden) 01:00:09 No, no, no, it's okay.
Josh Suereth (Google LLC) 01:00:10 Okay.
Arianna Vespri (OllyGarden) 01:00:10 The only, the only thing is that, that, you know, it's like, it kind of seems to me that… you know, a kind of a pattern that Lumila had introduced in, like, in her PR, then got reverted from this latest PR that's got merged, like, about the carrier and everything. I mean, I'm gonna adapt, it's not a problem.
So, but now, apart from resolving the conflicts, I also have to… To increase the coverage of the test, so I've got some stuff to do there in any case. Once I'm done, I'm gonna ping you again, don't worry.
Josh Suereth (Google LLC) 01:00:47 Okay, awesome. Yeah, so I've, I've… Sorry that… I thought my first merge conflict would be the only one that hits you, but if more hit you, I apologize. That was not… No! I tried to get them all done early, I'm sorry, yeah.
Arianna Vespri (OllyGarden) 01:01:00 It's part of the game, it's okay. Don't worry. Just, just for you to know what I'm working on, and, yeah, and, yeah, but definitely, I mean, I will think about the… out-of-the-box codeGen and everything, absolutely.
Josh Suereth (Google LLC) 01:01:15 Yeah, I mean, at this point, basically, if there's a language that you feel like is your most comfortable one, that you would… just to find an.
Arianna Vespri (OllyGarden) 01:01:22 Go is definitely my language, what I'm most comfortable with.
Josh Suereth (Google LLC) 01:01:29 Yeah, so this would be just, like… like, you don't even have to write any Weaver code, just say, like, what should the instrumentation library be for a Weaver SemConf in Go? Write that down as a spec, and then, we can look at it and say, yeah, this looks good, this is what our thick client library should look like, and then we can go you know, make a package from that. That's… that's more what we're looking for. Like, I think Jeremy and I are really comfortable with Rust, we could do that.
I can beg and borrow time from TypeScript people, but I don't know if they have time, to help us do a TypeScript one. I'm trying to figure out, like, what's the right language to start with. I still feel like Go might be it for the OTEL ecosystem.
Arianna Vespri (OllyGarden) 01:02:06 And this should be, like, ready in order to, you know, for when we… we do a V1.0 stable.
Josh Suereth (Google LLC) 01:02:15 Yeah, this is… this… that's the idea. So, like, we would… like, you… all you have to do is write up, like, here's what the Go library should look like.
And then we make a Weaver package that would take the Weaver Semconv and write the library.
as a template. Like, we'd write the Weaver templates and Weaver packages to make that, and then that would be included as part of 1.0, of, like, hey, here's our, We, you know, Weaver 1.0 is out, you can use it, we have Live Check, we have all that stuff. Oh, and by the way, if you want CodeGen and you're using Go, here's a package that will actually generate your Go code, that you can use to, you know, accelerate your development in OTEL.
Alright, I gotta drop, because we're over. Great discussion.
Jeremy Blythe 01:03:02 Right.
Arianna Vespri (OllyGarden) 01:03:02 Fantastic, thank you.
Josh Suereth (Google LLC) 01:03:04 See ya.
Arianna Vespri (OllyGarden) 01:03:04 Bye-bye. Bye.
