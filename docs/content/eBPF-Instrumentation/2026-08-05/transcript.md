SIG: eBPF Instrumentation
Date: 2026-08-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 00:55 Anyway.
**Giuseppe Ognibene (Coralogix)** 01:07 How do we want…
**Tyler Yahn (Splunk)** 01:09 Hey.
**Roy Reshef (Kubex)** 01:09 Great.
Good morning.
Or, good evening.
Wherever you are.
**Giuseppe Ognibene (Coralogix)** 01:16 Believe it in, yeah.
**Tyler Yahn (Splunk)** 01:25 Whoa.
**Nimrod Avni** 01:26 Hello.
**Tyler Yahn (Splunk)** 01:27 Hey.
How's it going?
**Nimrod Avni** 01:30 I'm good, how are you guys?
**Tyler Yahn (Splunk)** 01:32 Good.
Good.
To start my day, and you all are ending your day.
**Nimrod Avni** 01:38 Yeah.
Need to finish working.
**Tyler Yahn (Splunk)** 01:47 Yeah, I was looking at… I'm guessing so, I know Mario's out, he had said last week he's out for 2 weeks. I think Nikola is still out, this week? I think he's back next week. Steven, do you know?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:58 Nikola's back, Mario's out for 3 weeks.
**Tyler Yahn (Splunk)** 02:01 Okay.
Nikola is back, okay. We could probably wait for him then.
Hang out here. If you have agenda items, though, you wanted to talk about, go ahead and add them there as well. If you haven't… Yet add your name to the attendees list, go ahead and do that as well, and then, yeah, we can… we can wait a little longer, and then probably just jump in here in a second.
Oh, yep, there's Nikola. Alright.
Yeah, I was just checking Slack.
Yeah, let me start sharing my screen, we can jump in here in just a second.
Awesome. Okay. Welcome, everyone.
Yeah, we can get started here. I wanted to start us off by just talking about the next milestone, the V, 11, V011. So, we had put it down to have this resolved in, the 18th, or have it out in the 18th. The goal being… having this out in the 18th kind of sets us up for getting the V1 done by KubeCon.
Pushing this is not, I think, a critical, in the sense that, like, it'll stop the V1, but it is, I think, gonna be critical in the sense that, like, it's gonna put the… put the release at risk, so, I wanted to try to… follow up now, we got about 2 weeks, 9 business days, and I wanted to try to see if we can go through some of this stuff.
There's still stuff I'm going through, but, like, we can just start off with what I have. I first off needed… to ask for some reviews on some of these PRs, These are blocking the V2, config.
path right now, so this one's been out for a little while… no.
This one's been out for a little while. It's… kind of large. This is the one that actually enables the V2 config runtime loading, so it turns it on in the CLI.
Meaning that, like, this is one of… this is definitely part of the gate features, like, this has to get in before the release, so this one definitely can't get bumped, given we've already merged other things to start the migration process.
So, yeah, I'm looking for, people I can assign to this to get reviews on it. I don't know if there's anybody on the call who's, an assignee, or I'm sorry, an approver or maintainer.
**Nikola Grcevski** 05:13 Yeah, sorry, I just got back from vacation yesterday. I know I commented on this, I'll catch up with these reviews today, hopefully.
**Tyler Yahn (Splunk)** 05:21 Oh, okay. Yeah. Yeah, that sounds good.
Yeah, perfect.
I will assign this to you then. So, yeah, and also, folks on the call that aren't approvers, one of the best ways to become an approver is to just do reviews, just a heads up, or people watching the call, so, yeah.
Right. Moving on. So then this one is also, kind of important. So one of the other long… or the other issues that we need to get resolved is documents. This, config v2 migration path, and I have a PR to do that, it's just that that PR kind of uncovered a bunch of, bunch of stuff to try to clean up, to try to, like, make things, I don't know, more digestible from an end user's perspective. This is one where it takes, it splits off the runnable configv2 example. Like, right now, it… puts it a little bit smaller. The original one was there just to show, like, the full breadth of everything that was possible. This is there to try to show, I think, a more targeted, example. So, yeah, also looking for reviews on this one. I don't know if there's anybody excited to take a look at this, that I could assign, or not.
**Nimrod Avni** 06:35 Yeah, I can take a look on this.
Awesome.
**Tyler Yahn (Splunk)** 06:39 That'd be sweet, really helpful.
Cool.
And then the last one is preserving the re… Again, this is coming from the docs, in doing this, I was realizing, there's, like, ordering and, you know, essentially rule semantics, that we want to preserve.
This is, again, just explicitly, preserving those and making sure that it's cleaned up.
This is, I think, again, just needs, needs more review before I can actually get this, this documented one.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:13 I can volunteer.
**Tyler Yahn (Splunk)** 07:15 Awesome. Yeah. Thanks, Steven.
There it is… Cool. Alright.
Thank you, So, yeah, I think with those last two, or the first two, after that, there is this, hardening document for the config v2 migration. That should be manageable. It should be really straightforward, actually, after that, because it's pretty much just documenting things. It's not cleaning things up as well.
So, yeah, I will pull that out of draft when they get those other two merged, or the other two You know, migrated to whatever review needs to be done.
Also in this next review is this Auto SDK Instrumentation, so we had talked about this before.
This is instrumenting the Auto SDK package, so it has full suite instrumentation for anything that's a manual span. This is activating that. This is, again, this is, I think.
if I remember correctly, it's the last thing that… actually, no, there's a documentation task, probably, as well for this, but Yeah, there… this is the last thing to actually, like, turn this on. We have the probes, there, we've got a bunch of cleanup around the spent, The… yeah, there's a bunch of, I think, more to do, around, like, sampling, but… I guess we didn't talk about that, well, or we talked about it while Nikola was gone, but, like.
Yeah, one of the things that this does is it just, like, assumes that the sampling is going to be true, and it doesn't really touch the sampling. There's an issue dedicated to head sampling, and now there's a proof of concept out.
That's… really large, that needs to get broken up. But anyways, the idea is that, like, if we're making the sampling decision when we're exporting currently, and if we don't, know what the sampling decision is while we're generating this span, then we can't communicate that back to the, Instrumentation library in any way, so… yeah, this doesn't address any of that, it just kind of assumes everything's going to be sampled, put everything to be sampled, and just keep going from there. And then follow-up, we can address any sort of sampling questions back to the SDK, communicate that back, so… But that is not, I think, really needed to get this out. We can get something, rather than nothing.
But yeah, looking for reviews on this. Any approvers or maintainers on the call, open to taking a look at this. I'm also open to try to break this up even further, if needed.
it's… it's large, definitely large, so I'm happy to… Take that response.
Okay well, if we don't have a review for this one, I guess we're… More of the question is, like, is the goal to not get this in this next milestone, then?
**Nimrod Avni** 10:15 I can try getting a review on this, But, yeah, I'm not sure if I, like, when I'll get enough time to do it, because it seems like a… kind of a bigger PR, but I'll try to get it in, and I don't… maybe, worst case, we don't get it in this release, but…
**Nikola Grcevski** 10:35 I'll try to get in as well, review today.
I mean, this code is familiar to me, so…
**Tyler Yahn (Splunk)** 10:42 Yeah.
should be. There's, like, Yeah, just try to do this kind of safely. I guess, like, the only complications coming in is, like, I was trying to, like, not… I'm trying to make these atomic, I guess, and I've got other code to make that atomic coming in, like, when the probe goes in, it doesn't try to… Anyways, it should be pretty straightforward, Nikola, from your perspective, what you're saying.
**Nikola Grcevski** 11:05 I'll review it, I'll review it.
**Tyler Yahn (Splunk)** 11:07 Cool. Nimrod, should I put you down here as well?
**Nimrod Avni** 11:15 Yeah, I'll try to get into it.
**Tyler Yahn (Splunk)** 11:17 Yeah, I'd appreciate it. That sounds good. And like you're saying, if we can't get through this, that's… I don't think it's… Mission critical to get it out in this, release, so, yeah, understood.
Okay, yeah, speaking of that, There was a ask from, Mario, I think, if I'm not mistaken.
to add integration testing, for end-to-end coverage of this ConfigV2 migration, I'm happy to take a stab at this. I do want to know, like, do people think this is kind of a required for the V1, or is this something that we can add after the fact?
**Nimrod Avni** 11:59 Do you mean, is it, like, replicating the same integration test we have today, just with the V2 config, or…
**Tyler Yahn (Splunk)** 12:07 Yeah.
**Nimrod Avni** 12:07 like, replace them. Because if we… because if we add them, I think they'll be just… a lot, a lot of, CI, you know.
A YAM will change. I don't know.
**Tyler Yahn (Splunk)** 12:18 Okay, yes, so I… you're saying what I'm thinking as well. It was asked to do a duplication, but I… I kind of agree that, like, I kind of like the whole migration, just do… a V2 instead of a V1, but that would also mean that we need to get the V2 out, and then start to centralize on the V2, I think is kind of the key.
But yeah, like, based on that feedback, I'm happy… If the rest of the group is in line with what you're thinking, Nimrod, is to postpone this from this, milestone, and then after we get the V2 out, go through a migration path, even maybe after the V1, go through and change our integration test to be the V2 config, not the V1.
**Nimrod Avni** 13:05 Yeah, I think that sounds, like, that makes more sense, like, we can… we still have, like, unit tests on the V1 to V2 conversion, but if anyone disagrees… Love to hear it.
**Tyler Yahn (Splunk)** 13:35 Yeah, okay, cool.
Awesome.
**Nikola Grcevski** 13:48 I'd say let's just migrate them all to the new config.
**Tyler Yahn (Splunk)** 13:53 Yeah, I mean, I'm…
**Nikola Grcevski** 13:54 Or, or just parts of them, right?
**Tyler Yahn (Splunk)** 13:56 I'm happy to go through it. Obviously, like, that's a lot of work, but…
**Nikola Grcevski** 13:59 That was just cute.
**Tyler Yahn (Splunk)** 14:01 I'm not… I'm not opposed to starting on that. And, like.
Yeah, maybe we could just start on it, it doesn't have to get, like, done by the time that the V1 is out, but… I… yeah, like… I'm happy to take on that task as well. Like, that definitely sounds like great, great feedback, so we can definitely start doing that. Yeah, I was just more like… Hesitant to just build… a duplicate thing. But anyways, enough said. We don't want to do that. Okay.
Similarly, filtering for traces, so this is another one.
So right now… If I'm not mistaken.
This is targeting… like, this filtering target is not, like, global enough, yes.
Yeah, the filtering semantics here… Are a little off in the sense that, like, yeah.
This will only generate a span, yeah, if the server part is 87, 87, yeah, this is the effect, the internal spans for DB triggered, yeah. So essentially, like, this won't actually do a full global filtering, it'll only do filtering for, you know, a particular, or it will do a global filtering, and it won't, like, be able to give you, like, fine-tune. The idea was, is, like, with these other, configuration, like, you probably could get something to go, but we don't currently have a solution here. And, like, my question is, is, like, do we want to actually… Address this now? Or is this something that, like, we want to just document as a… We're not gonna support this, I guess.
**Nimrod Avni** 15:41 I don't think it's needed, at least for the, 11 release.
If, like, no one has capacity to pick it up, we can… Hopefully, like, they'll get it in before V1.
**Tyler Yahn (Splunk)** 15:58 Yeah, alright.
So bump this, is what you're saying?
**Nikola Grcevski** 16:02 Yeah. The 12th, yeah.
**Tyler Yahn (Splunk)** 16:04 Yeah.
Okay.
Okay, cool.
Yeah, sorry, this list is not complete. I was, in the middle of doing this.
Then I had this drop, so I haven't gone completely through this whole thing.
Mostly through this hop setup. So this configV2 landing page, a lot of this we already touched on. I think the only blockers we've already addressed, we've got reviewers for those, so that's actually in a great state. Document the migration, yeah, it's part of it.
this… Yeah, define the V1 telemetry contracts, this is, again, like, one of the things I got sidetracked on, so I'm, like, trying to figure this one out. I'm not exactly sure where we want to go, with this one, so still just waiting through all the options here. I know, Nimrod, you've taken a look at this as well, but yeah, I… I don't know the answer here, still… Trying to figure this one out, working on it, but yeah.
**Nimrod Avni** 16:57 I'm not sure it's gonna be, like, a thing… maybe I still need to make sure I'm, like, the definition of done here, but the… I'm working now on, kind of, narrowing down… right now, like, our, telemetry schema, basically, we say, like, we inherit the, global semantic conventions, and we add a bunch of stuff, but we don't actually say what we… like, what we take from the Semantic Convention, so, like, people can interpret it as we take everything.
And also, we can't validate that, like, we cover the whole, like, in our integration tests and stuff, we cover the whole, semantic, like, our, like, what we declare is actually what we, we test and we make sure that we output. So I'm working on that now, I'm hoping I can get it done in a couple days. Basically saying, like, kind of refining our, our telemetry schema, and then doing, like, a coverage test, saying, like, we cover, like, 90-something percent, and kind of chipping down until we get to 100, and maybe after that, failing CI, if we, like, decide, like, if we see that we don't cover it fully.
So, yeah, it might take.
**Tyler Yahn (Splunk)** 18:09 Yeah, that's… that's exactly what I was thinking as well. I saw a pretty big list of things that, like, we probably want to include from the default, or the main semantic conventions, so I was, like, trying to wade through those and figure those out, but it sounds like you're… you're well on this path as well, so… Mind if I assign this to you, then? It sounds like you're actively working on this one, so yeah.
**Nimrod Avni** 18:30 Beautiful.
**Tyler Yahn (Splunk)** 18:31 Perfect.
Cool, yeah, this… I will stop paying attention to the… well, I will pay attention to whatever you do, but I will try to stop, developing a solution. Sounds like you've got… thought more about it than I have.
I wanted to check in, giuseppe, you were working on this one at the beginning of this milestone, is this still something we're planning on trying to get in?
**Giuseppe Ognibene (Coralogix)** 18:53 Yeah, I'm working on that. I had some other stuff to work on, but I plan to come back on that.
It's a big, big task.
**Tyler Yahn (Splunk)** 19:06 Yeah, it is, definitely. I think that's kind of, like, my question. Do you think this is still something you'll, like, get in in the next 2 weeks, or is this something probably after that?
**Giuseppe Ognibene (Coralogix)** 19:16 I can try. I… I can try you.
**Tyler Yahn (Splunk)** 19:20 Alright, cool. Then I will leave it in the milestone. Perfect.
**Nikola Grcevski** 19:23 Yeah, this is gonna be a little bit tricky. I think it's similar to the kind of issue that… mario hit with Dino.
There was a… There's also an issue that somebody opened just yesterday, or today, I don't know, I saw it this morning.
my time.
Somebody complaining that they… it doesn't work.
Node.js, but I'm not sure, but they mentioned Dino and Bun, where they stripped the symbols, yeah.
So, Node.js is always statically linked. It's not… they don't actually statically link it, they actually vendor SSL in the binary, so they have their own version.
Which works. I mean, we test with this version here, I believe. Everything works there. The issue is that if you use BUN or… Do you know any of these guys?
They're… they actually vendor it, and they strip it, so we can't see the symbols.
Yeah, I actually don't know how do we do this? I had, like, two thoughts. Both are… I mean, the first one is really wild, but… Disassembling would be expensive, but we could look for the binary patterns, maybe, in the files.
for what we recognize as the start of the TOS method being in line, and things like that. So, same for you, Giuseppe.
If you… if you're thinking of, Rust Tokyo, the problem with Rust is that it strips the binary, so there's no… it's gonna be really hard to tell where the method starts. Otherwise, it's easy. It's not that hard. There is even a talk that… Tyler linked a while back that somebody was… if you keep the symbols in, actually doing Tokyo is not that hard. But, and they figured out a way how to do it with U-probes. It's all in the talk, he's figured out exactly where to put the probe and where to read it from, but the problem is most Rust binaries are strict.
So for us, I don't have a solution other than trying to do binary matching of the pattern, and then saying, okay, that looks like a start of this function, which could be very fragile.
But I don't know how fragile it is. Maybe it's really standard. SSL is kind of easier to tell, because they use the standard crypto instructions that exist on both ARM and… x86, so you'll be able to recommend AES and whatever, so you can easily kind of scan for those and then try to Get closer, But for Dino and Bun, I was wondering, I don't know if you guys discussed it last week, but maybe we should start doing the same thing we do for Go, which is harvest the offsets from the actual binary, because they are actually compiled and distributed, and they have a strict version, so we could… like, Dino and Bun are… Fair game.
Even though they're stripped, as long as we can find the version, or maybe detect it somehow, which is probably going to be a string somewhere in there.
Then we could maybe tell… what's the offset of the SSL based on the actual version? Just like we do for goal offsets, we have Bon and Dino offsets. And for other well-known runtimes or other programs that we want to consider. But one kind of… issue that we currently have, which is I was experimenting this with this JN AI observability and whatnot, You can't, actually monitor Claude.
with Obi.
Because we… it's written in BUN.
Bond is written in ZIG.
there's not even a… like, it's… ZCC has a native Lib SSL, and they rewrote it in Rust, but I don't think that's made it to the… bun… Clawed version? At least, I don't think so.
It still looks like the ZIG version.
And… But codecs? It's completely strip. I don't even know what that is. Like, I run codecs, and there's no symbols in the binary whatsoever.
There's nothing.
So… yeah, but it's one of those, like, it looks like JavaScripting again, but… And we can't touch it. Like, there's nothing… we see nothing. We're completely blind.
**Tyler Yahn (Splunk)** 23:53 Yeah, I mean, I… that's, it's troubling, but it's also, like, I think you're… I think you're right. Like, I think your solution of, like, trying to get the offset seems reasonable. How to get the version? I'm sure it's somewhere in there, like you said, but…
**Nikola Grcevski** 24:08 It's probably on GitHub somewhere. They… The version? Yeah, I don't Oh, yeah, the version, yeah, the version string, who knows? But I'm guessing it's gonna be in one of the symbols, because you can do bun dash dash version, it will print it, so it must be, like, a… some static data symbol they have that we can extract and find it. That should be no problem.
San Bernardino.
**Tyler Yahn (Splunk)** 24:34 So for Rust, though, do you think that that's also a possibility?
**Nikola Grcevski** 24:38 bet.
I mean, Rust only keeps a handful of symbols in there. They don't… when they strip, they don't strip everything. For example, you can always find Rust panic. This is how we tell binaries Rust. Because… unless your Rust library will never panic, but those are rare binaries.
There's a handful of symbols. You can tell it's Rust, but it's… So then it would be… How do you find… the places where this Tokyo runtime is. And without symbols, the only thing you have And depending on the size of the binary, the disassembling is not actually… if you try to disassemble, like, a Rust binary, like, that's large, you're just gonna die disassembling it. So you must look at the binary patterns, just like we scan for the return addresses on… we have code for this, though. For the U probes in Go, we scan for the return addresses by decoding the… But we start at some point, and we started decoding.
So, you have to be clever.
But I… I don't know what the code generated for the Tokyo runtime looks like.
I thought SSL would be a little bit easier, but… Famous last words.
Yeah.
They would have to do, like, sort of, like, Matching of the binary and… I don't know, which is nasty and ugly, I don't know.
Because with Rust binaries, like, once you've statically built everything in.
it's kind of hard to tell where the offsets will be, right? I mean.
**Tyler Yahn (Splunk)** 26:17 Right.
**Nikola Grcevski** 26:17 Depends what the binary's like, so… it's not like a standard binary build like VUN or Deno, and you're like, okay, for this version of Deno, I know exactly where the offsets are.
Yes.
**Tyler Yahn (Splunk)** 26:36 Giuseppe, have you taken a look at this at all?
**Giuseppe Ognibene (Coralogix)** 26:39 So basically… from what I remember, because it's, like, 2 weeks that I don't touch that branch.
But I didn't even consider the strict binaries. I… I have a working solution for, Build the bug and build the release, but if there is no… I mean, if you.
**Nikola Grcevski** 27:01 Stupid.
**Giuseppe Ognibene (Coralogix)** 27:02 the.
**Nikola Grcevski** 27:03 Okay, because build release, for me, stripped the binaries, but maybe they've changed that, so maybe we're okay. Like, the last time I checked, when I did build debug, you… yeah, you have the symbols, but if you build release with Rust, by default, they just nuke them.
But maybe they keep some of it, because I know they keep some of it, otherwise we wouldn't be seeing rust panic in there.
So maybe there's Tokyo things somewhere that survived, so… maybe that's okay, maybe I'm thinking too much about it.
**Giuseppe Ognibene (Coralogix)** 27:30 And also, at least from… my, my tests, it's working with the, you know, work stealing.
Because, runtime is with this wonderful thing called Stealing.
And, but it's not working with, spawn blocking.
I tried, but I fed it.
**Nikola Grcevski** 27:54 Okay. Me and my mom.
**Giuseppe Ognibene (Coralogix)** 27:55 Claude, we tried many, many nights, but…
**Nikola Grcevski** 28:02 Well, we got one thing working here, that's okay here.
**Tyler Yahn (Splunk)** 28:05 Yeah, I think maybe that's just the way to do it, is, like, get something, and then we can maybe iterate on it?
**Nikola Grcevski** 28:09 Yeah.
**Tyler Yahn (Splunk)** 28:10 But yeah.
**Giuseppe Ognibene (Coralogix)** 28:13 again, again, I can work on that.
**Tyler Yahn (Splunk)** 28:17 Yeah, that sounds good. Alright, we'll keep an eye on it. If folks have more ideas on that one, collaboration's great. Please comment on that issue.
And then, yeah, we'll keep that… Keep that in scope.
Cool.
Alright, jumping into the rest of this, so, Publish or propagate the OBE telemetry schema. This is another one, Nimrod I was looking at, but I'm wondering… I definitely think you're… Looking more at this,
**Nimrod Avni** 28:51 Yeah, you can assign it to me, like, I don't know if we… if this is blogged by the previous one, or maybe we can just publish and iterate it, but I… anyway, I think we need some… something from the… GC or TC, or, like, some… like, if you want to publish it to OpenTelemetry.io.
Like, the, the, like the OTL semantic convention?
Then we probably need someone from there. I didn't see any other semantic, like, any other telemetry, schema published by anyone besides the official one, so it might be something new we're doing.
But I'll…
**Tyler Yahn (Splunk)** 29:28 I'm gonna open…
**Nimrod Avni** 29:30 Issue or slacks for them.
**Tyler Yahn (Splunk)** 29:33 We could definitely do something at, like, the top level. I think that'd probably be best.
But we could also just put it in our repo, and just link there. I mean, because a schema URL is just a schema URL, right? So,
**Nimrod Avni** 29:43 I mean, just linking it, like, to our repo.
**Tyler Yahn (Splunk)** 29:47 Yeah. I mean, obviously, like, we'd have to figure out, like, versioning things, because we probably don't want to link to, like, a branch or, like, main or something like that, but, like, I mean, even… It wouldn't look great, but you could do a permalink, right? And then… Although, I don't know how you do, like, a self-referential permalink.
**Nimrod Avni** 30:04 I don't know if we can do it, like, by release or something, I don't know.
**Tyler Yahn (Splunk)** 30:07 Yeah, yeah, actually, that's probably a good idea. We could do it by release, because those are predictable URLs, yeah. So we could put it somewhere there, if not, yeah.
**Nikola Grcevski** 30:15 Sorry, I gotta drop, I have another meeting. Apologies, sorry for interrupting this. Nimrod, I just wanted to say, like, for your question about deprecating the old tempo-style Grafana, I'm okay with that. Let's deprecate it for now.
I mean… let's not remove it, at least immediately. But I'm okay with uppercating it.
**Nimrod Avni** 30:36 Okay, so I'll ask the… the follow-up question is if we want to remove it at some point, but we can.
**Nikola Grcevski** 30:41 Yeah, we probably can remove it, I just need to figure out what breaks for us, and if it does break, then in the Baylor version, we'll just replicate that or something, or provide a way that you can rename the collection Keep it.
Because it's just the name of the series that's changing.
So, maybe we can…
**Nimrod Avni** 30:59 If it's only that, or the, some of the label…
**Nikola Grcevski** 31:02 No, the labels are all identical. Just the name, so we can make it configurable if we ever want to remove it, and then Bela can supply. If people use the old option, they can supply the… I need to go, unfortunately, but yeah, thanks, guys.
**Nimrod Avni** 31:20 Okay.
**Tyler Yahn (Splunk)** 31:24 But yeah, yeah, Nimrod… I mean, maybe it's just best if we, like, start publishing here if you don't get a response, but if… yeah, if there's already a planned thing to, like, support these at, like, the top level, I'd be down for that as well.
**Nimrod Avni** 31:36 Yeah, try to start with that, and maybe we can change the URL in the future.
**Tyler Yahn (Splunk)** 31:42 Yeah, I mean, that's actually why it's designed to do that, like, you can change it pretty much at any point, so, yeah.
Okay.
Complete OpenTelemetry, the OB Telemetry registry coverage, yeah, again, I think we talked about this, we don't need to… Weaver validation should cover the Cates test.
Yet, also something… I think this is pretty actively being worked on, right?
**Nimrod Avni** 32:06 Yeah, I think now… I had some issue with that, but I think now, the PR is reviewable again, so I'll… if anyone wants to have a look.
**Tyler Yahn (Splunk)** 32:15 What PR?
**Nimrod Avni** 32:18 It's, I think it's 25… I think it's linked there? No? Wait, what?
**Tyler Yahn (Splunk)** 32:24 Yahn.
**Nimrod Avni** 32:25 Yeah.
**Tyler Yahn (Splunk)** 32:26 Excuse me.
**Nimrod Avni** 32:29 I'm gonna link it. I'm gonna send it in the chat.
**Tyler Yahn (Splunk)** 32:33 Okay.
This one, right?
**Nimrod Avni** 32:40 Yeah, just neat.
I'll link it to that.
**Tyler Yahn (Splunk)** 32:45 To the issue?
**Nimrod Avni** 32:46 Yeah.
**Tyler Yahn (Splunk)** 32:47 Perfect, okay.
And, that 2785 is gonna actually, resolve this, right?
**Nimrod Avni** 33:00 2785…
**Tyler Yahn (Splunk)** 33:02 Yeah, looks like it's… okay.
**Nimrod Avni** 33:03 Yeah, that's the, that's the one.
**Tyler Yahn (Splunk)** 33:06 Awesome.
Okay, and then the rest we've already talked about. These are all PRs, related here. So yeah, this is… this is looking good. Anything else that's missing from the… the milestone?
**Giuseppe Ognibene (Coralogix)** 33:27 Obviously.
**Tyler Yahn (Splunk)** 33:28 There's a bunch of stuff we're gonna merge we can add, but, nothing blocking it, right? Sorry, Giuseppe, go ahead.
**Giuseppe Ognibene (Coralogix)** 33:34 Yeah, I did a PR about deprecating a flag application JVM, maybe if we can add it to this, release, it should be good.
Yep.
**Tyler Yahn (Splunk)** 33:51 Yeah.
**Giuseppe Ognibene (Coralogix)** 33:55 I saw that you commented yesterday, I… Check it today.
So if you have kind of a… check.
**Tyler Yahn (Splunk)** 34:06 Yeah, take another look, just looking for another round of reviews.
**Giuseppe Ognibene (Coralogix)** 34:09 Okay.
**Tyler Yahn (Splunk)** 34:09 Yeah, I can do that afterwards.
Awesome. Yeah, here.
Cool. Anything else? Other… other topics on that one?
If not, let's keep going. Nimrod, do you want to talk about this? I'm guessing this is what you and Nikola were just talking about, right?
**Nimrod Avni** 34:31 Yeah, so part of, like, all the validation weaver stuff.
I saw that we are declaring in our schema both of them, both, like, the old and new conventions, and I would say, like, if we're… because both of them export OTEL, and I think all the… I changed all the integration tests to only, use ApplicationSpanOTEL instead of application span.
So I said maybe we can start by, like, deprecating it, like, via the config, or, like, docs, I don't know. And maybe in the future, like, think of removing it.
It led me to a bigger point. I think that's probably a bigger change, and we might need to talk about it more, especially with Grafana people. If we still want to support both OTOL and Prometheus-style exports, because… the, like, with all the Weaver stuff, we can at least guarantee everything is, like, all the Weaver… like, all the hotel metrics are being tested, are being covered, and with Prometheus, it's a bit harder. And… like, it is like the, you know, it's very easy for, like, a collector to take hotel metrics and export them in Prometheus style, but I'm guessing a lot of already existing customers of Bela slash OB won't like that.
So I might… I can, like, open the issue, and maybe we can, like, think about it for the future.
I'm not sure if it's, like, blocking V1 or whatever, but in my head, at least, it makes sense that we have, like… I think it will also simplify the code, because we have, like, one pipeline for metrics, one pipeline for traces.
But, yeah, but I'm guessing people from Grafana might have, like, bigger, like, more, thoughts about this?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 36:19 So I think, like, mirroring what Nikola said on, the tempo-style metrics. Like, so we're actively using this in several places at the moment. It's not to say that we… We can't deprecate it and remove it, but… We would definitely… if it was to disappear today, we would definitely have to, you know, it would cause some work, and we would need to react.
So I think opening up an issue is the right thing, and we can, you know, prepare and document And, you know, come up with a plan for removing it away. I mean.
I can't see a strong argument right now, just off the top of my head, for keeping the Prometheus Explorer.
So, yeah, I'm kind of definitely open to the idea, it's just that, I hope it doesn't just disappear overnight, it's the only thing.
**Nimrod Avni** 37:11 Okay, makes sense, I'll open an issue on that.
**Tyler Yahn (Splunk)** 37:15 And this is, again, just for my understanding, like, if you wanted to keep the metrics, you could, in theory, send our telemetry through a collector, and then regenerate them there, right? Yeah.
**Nimrod Avni** 37:27 I'm hoping, like, the convention, like, the naming on everything will make sense, because, like, we hardcode have names for…
**Tyler Yahn (Splunk)** 37:36 Yeah, yeah.
**Nimrod Avni** 37:36 So, and, like, I think it's usually just replace dot with underscore or something, but… I'm not 100% sure it's the same, so we might need to do some validation on that before we remove it.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 37:50 Yeah, I think one thing storing in the backend is fine, it's no problem. It's gonna be whether or not a… like, what… which collector or agent is actually being used.
And whether it… whether it expects… the… and Nimrod, are you thinking, like, just removing Prometheus completely throughout, entirely?
Or are you thinking, like, just remove… the actual, you know, Prometheus.
client that is… And the registry, and then doing… Can you do an export some other way?
like, can you… are you saying, is there a way to directly translate BOTEL metrics into like a Prometheus remote route format, for example.
**Nimrod Avni** 38:30 Yeah, I think, like, the collector does it, right? Like, if you have, you have, OTEL, like, we export OTEL, you go to the collector, and then you have either… I think it supports both, like, a write, like, a push format, and I think even, like, it can expose the slash metrics to…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 38:50 Yeah.
**Nimrod Avni** 38:50 I'm not super sure on that, but so you can do the translation in the collector, and… that will make sense, I think, for us to not, like… if we don't have references to Prometheus in Obi, I think it'll make our lives easier, but I'm guessing for every existing customer that uses Prometheus, we need to make sure for some migration plan.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 39:16 Yeah, no, it'd be good to just start collecting some use cases there, and yeah, I'm open to an issue, and we can discuss it more there.
**Tyler Yahn (Splunk)** 39:26 Yeah, awesome. That sounds good.
Okay, looks like we are at the end of the written agenda. Any other topics folks had?
Any cool things they're working on?
All kinds of cool things. How about, talks accepted? Anybody?
Get some KubeCon talks accepted?
Yeah, I got two rejections. I got one, I think, that's in, like, purgatory? I don't know, but it's just sitting there pending.
I don't know what's going on.
**Nimrod Avni** 39:59 I think, like, from what I read, we had, like, 5, 6 OB talks. No one got… That's it.
**Tyler Yahn (Splunk)** 40:06 They're probably, like, rejecting.
**Nimrod Avni** 40:07 Like, Ruffle and, Matt? Oh, yeah.
**Tyler Yahn (Splunk)** 40:11 Yeah, I saw that, yeah. Which, that's exciting, talking about a deep dive, that should be really good. I am in charge of, the ContribFest, it's gonna happen this year, so… or I'm one of the people in charge of ContribFest, so that's another place that, like, we've definitely found a lot of really great, like, outreach and, like, just community involvement. Not necessarily, like.
Fielding new devs, but just, like, spreading word and stuff, so, We'll… we'll talk more as time comes, but having, like, quick issues around just, like.
literally, like, spelling fixes or things like that are great for first issues. We try to get people to work on their first issue in that process. So, yeah, hopefully OB can be involved, is my goal there, yeah.
Yeah. Any other?
Updates?
If not, yeah, we can end here. Steven, I see maybe you're unmuted.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 41:08 Oh, I was just gonna ask, there was a couple of GitHub advisories that I pushed through that got merged yesterday.
I just wondered if, if that was the right way to kind of deal with these things.
Author should be.
A more subtle process that should be used.
**Tyler Yahn (Splunk)** 41:26 Those were updates for the dependencies, so I think that was appropriate. Like, we do have, like, a security tab that should be tracking these. I do try to stay on top of it, but, I'll be honest, I haven't checked in a week or two, just been overloaded.
But yeah, thanks for catching those. I think that was appropriate, especially since you saw that they've, like, got dropped on the renovate. Obviously, like, for creating security advisories and other security issues with Obi, let's go through the different, like, channels than just a PR.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 41:56 Of course, yeah.
**Tyler Yahn (Splunk)** 41:57 Yeah, But yeah, no, I think that that was… that was… that was great. Yeah, thanks for the help on that.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 42:02 Yeah, no problem.
**Tyler Yahn (Splunk)** 42:07 Okay, cool, awesome. Well, I will, we can end the meeting here, and I'll see you all in a week's time, or, asynchronously. Till then.
But…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 42:17 Bye.
**Nimrod Avni** 42:18 Okay.
