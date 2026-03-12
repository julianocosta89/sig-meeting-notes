SIG: JavaScript SIG
Date: 2025-10-29
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/XN1TU1pxgbWujRRVyLJNdCRnGir-SIXt6sunYMiO_nVuPM1MLEpF1fqiqFrVSnPE.DQyKl_9mlH5ykJls
============================================================

## Zoom Recording Transcript

**Trent Mick** 00:37 I know.
**MG Marylia Gutierrez** 00:39 Oh.
**David Luna Bistuer** 00:42 Boom.
**Trent Mick** 01:53 I was still gonna wait about a minute.
Started.
Please let me know if sizes are okay.
**Jamie Danielson** 02:58 Looks good.
**Trent Mick** 02:59 Okay.
Alright, I drew the short straw, so welcome to the slightly more Canadian version. It's a SIG.
Right, get started, and as ever, feel free to add agenda. I'm the only one with stuff. Raphael, welcome to Approvers.
And there's the PR. I think that was in the last week.
I don't know.
**Raphaël Thériault** 03:28 Things. Yeah.
**Trent Mick** 03:30 Good to have more people.
Yeah, next one. Jared had in this… Here, I've been working on hoisting all of our dev depths up to the top-level package.json.
Which I've been helping with a bit. I don't know if… I don't think Jarrett's on the call, is he?
No.
Jared is overbalanced.
And… If anyone had a chance to look? Sorry, let me try to find the… Here's one of the failing runs.
And… You look at the workflow file, the way that this is structured now.
is… David, maybe you know this better? I can't remember if you're the last one working on this. So we have a… a couple… a few separate jobs. So we do compile, step.
that does NTMCI with ignore scripts.
And then… Does some compilation, and then… stores those as a build artifact, the idea being that we only need to do most of that compile step once instead of doing it for the full matrix. So then, for the full matrix.
Each of the next… Steps for the matrix for unit tests, and then a slightly lesser number of versions that we do to test all versions tests.
We do the… Check out, set up node… MPMCI, this time without ignore scripts, because we need to run the scripts for a few of the dev dependencies, like ESBuild and… better SQLite 3 and SQLite 3 for some of the tests to work.
Then we download the NX cache, which is meant to help with the… Compile, CI affected.
And then we run tests, and similar for test all versions, except it's a different set of test runs. But, if you look for all of these guys.
This is the install step, so that's, let me go back to… the workflow file. So this is not in the compile job, but we're now in the unit test job. So for each of these versions, we're doing… NPMCI, which should be just straightforward.
Fine, but for every one of these guys, we get… Okay, so for this one, some of the warnings that we expect to see, unfortunately for now at least, is a bunch of the EBAT engines.
And not really any more details on whether it completes Satisfaction or not, or how far it got?
Similar for this one.
I'm clicking through because it changes.
then this one doesn't even get as far. All the rest of the ones don't get any MPMCI output, so, like, what the hell is going on? I can't forget that, I want to…
**Jamie Danielson** 06:33 They all just keep going indefinitely? Like, that one's, like, started 36 minutes ago.
Does it ever fail, or just…
**Trent Mick** 06:41 I think some of the earlier ones failed with a network thing or something, but there's not a timeout. We've never set a… Time out on any of these jobs or things, but… I just got distracted by the chat. Is there a party reaction on your screen?
**Jamie Danielson** 07:02 Sorry. There was for, like, up until I started talking again, it just stayed in the top corner of my video, and it was…
**Trent Mick** 07:08 Oh, and it's gone. Okay.
**Jamie Danielson** 07:10 Okay. Carry on.
**Trent Mick** 07:11 debugger.
Anyway, so, yeah, I don't want to suck too much time on this one, but, I had posted some… ideas here, unlike… something weird going on, but really I'm grasping at straws there. So that's… that's on that issue, discussion in there.
**Jamie Danielson** 07:30 I wonder if, like, you tried… Pushing, like, your own branch, does it have the same problem?
**Trent Mick** 07:38 So, I had tried to do… my own PR based on this one.
Jared likes to force push, so that's making it hard for me and my usual workflow that I'm used to, so… I was having a little bit of trouble, but I got in there, and… I think… I hit this thingy mesh shoe.
So this one… no, this one got, okay, econ reset, and then that canceled all the other ones, and I think I've tried again, but… This one didn't even run, so what's going on there?
I don't know, I can't remember, so I have to get back and try again.
Let me check my notes again.
Yeah, and I think this is only happening in CFCI, if I remember this, two weeks ago, before I was off for part of last week.
I could not reproduce it locally. So, anyway, I think maybe I need to… keep on this one and try again in my own branch, but I… I think it's just… it's failing in CI, and not in whatever. I don't know if… Does NPMGS consider it a BOS attack? Because we have, like.
12 different things that are trying to do NPMCI right at the same time, or is it something that's weird because of the annex cache thing that is… But then the annex cache should only be for compile step, and not for MPMCI, so I can't see anything that's relevant there.
Anyway, so, something to play with.
That one's holding up that PR.
If someone is inclined to play with that, I would certainly be welcome.
Otherwise… Yeah, some normal maintenance going, then a whole bunch of work has been going on by Merilia and Jamie on configuration stuff, so that's kind of cool. I still have not… Had a chance to get over the hump on that one, so sorry, I'm no help yet.
**MG Marylia Gutierrez** 09:51 No worries. And yeah, and thanks, Jamie, for taking up a few of the issues there.
**Trent Mick** 09:58 Oh, I guess maybe I'll bring up another one. Hold on, give me a second.
Oh, I can't even find my notes on that one. Oh yeah, it was the, So this one is still going. I think I said it was going to be all over this a couple of weeks ago, but then I totally dropped the ball and haven't followed up on that one. So, Jamie, you got that one in.
So there's still this.
**Jamie Danielson** 10:35 Exactly one.
**Trent Mick** 10:37 I'm done to finish the… finish those ones off, yeah. Yeah. And then David waltzed it, and he's like, yeah, I'll just pick one off the top, I'll do MQP, which is the worst one. It is just… You kind of walk into questions like.
I'm not sure what we should be doing. Messaging is a big question mark right now on how to handle various things.
**Jamie Danielson** 10:55 There was another weird one, too, because I was originally going to pick up a different one, not Memcache, I don't remember which one it was, but it was… also just very different in… in several ways, and I was like, Why don't I, why don't I go to one of these other ones instead?
**Trent Mick** 11:10 Yeah, it's not all mechanical. It's…
**Jamie Danielson** 11:12 You have to.
**Trent Mick** 11:13 about some of these ones, so yeah, unfortunately, still take a while. I still do intend to get through all these, so we can just tick it off.
Same.
I had said by Christmas, which is the 6-month thing, but I think, actually, realistically, in reading.
what they want you to do in the SEMCOM guidance was to have it be a major version before you drop support for the old ones. So, really, I think the expectation is next June, when we'll do a V3, and we'll drop Node 18, Node 20 support, is be when we basically drop those opt-in and just have the newer ones, is my expectation.
**Jamie Danielson** 11:44 We just have to get them all done by Christmas to be able to do that.
**Trent Mick** 11:49 Well, no, we don't. The 6-month window thing is about…
**Jamie Danielson** 11:53 6-month or major.
**Trent Mick** 11:57 Is that what it says? I don't think it did.
**Jamie Danielson** 11:58 Generally, that's, like, the general guidance, is actually 6 months, ideally.
**Trent Mick** 12:05 But… There's no 6 in here.
I'll wait a second.
Yeah, so this… This guidance does not talk about sex.
**Jamie Danielson** 12:17 Oh, S-I-X.
**Trent Mick** 12:19 Oh, there we go, yeah, okay, okay.
**Jamie Danielson** 12:24 We should put a…
**Trent Mick** 12:24 To maintain their existing major version for at least 6 months.
But that's, like, if we do JS SDK3.x, we still support 2.x for a while, so if there's, like, the support for us is meaningfully gonna be… Yes, there's a skew It's about the only thing, yeah, yeah, support over there, close. Okay.
**Jamie Danielson** 12:45 Either way, I mean, like, once… once it's done, we can move on with our lives eventually. Right now, we're gonna stay in limbo for a while, but easier said than done.
**Trent Mick** 12:56 Yep.
**Jamie Danielson** 12:57 Literally.
**Trent Mick** 12:59 Alright, if anyone has anything else they want to bring up.
**MG Marylia Gutierrez** 13:02 I'm gonna say, just for the… this is just for the HTTP, there's also, like, the database.
Once.
**Trent Mick** 13:08 Yes, so… Sorry, I'd been pulling from another…
**Jamie Danielson** 13:15 Yeah, there's, like, 2 pages.
**Trent Mick** 13:18 So there's this one.
**MG Marylia Gutierrez** 13:19 as well.
**Trent Mick** 13:22 So there's this guy as well.
Yeah, I guess I could put…
**Jamie Danielson** 13:27 Oh yeah, that's the one where I was gonna grab from the bottom of that list.
And then laughed and said, no, never mind, and picked a different one… for now.
And yeah, because we were doing the… database instrumentations that still don't have the net attributes updated, doing them in the same PR where possible.
**MG Marylia Gutierrez** 13:54 Yeah.
**Trent Mick** 13:58 Right, so that means a set of those ones in database are going to be handled by… that bigger for people. So this one that's going through and doing .NET… oh, yeah, had we done…
**Jamie Danielson** 14:10 Both? Did this one do both?
**MG Marylia Gutierrez** 14:12 Yeah, even says, like, the title, yeah.
**Trent Mick** 14:15 Yeah, and database, yeah, good.
So, yeah.
So there are about a dozen PRs to get through there.
Okay.
So… And triage bugs.
New one, feel free to jump in if you haven't answered for any of these.
**Jamie Danielson** 14:50 So it's multiple layers, if it's Azure and Next.
**Trent Mick** 15:04 I mean, I don't know what that's doing.
**Jamie Danielson** 15:07 I wonder if this ends up being a question for… like, the Azure package more than… this.
Because…
**Trent Mick** 15:20 What's that going to do?
Oof.
So where are their packages?
Jay.
**Jamie Danielson** 15:46 There's a few.
**Trent Mick** 15:48 Yeah, no kidding. Oh my god. Okay.
Where are weeping in?
Monitor OpenTelemetry.
It's its own SDK, I bet, that's setting up So, okay.
Depending what… are they using the Next.js setup thing?
**Jamie Danielson** 16:25 Yeah.
**Trent Mick** 16:28 It's not the next hotel thing, though, because next… or Vercel has their own hotel thing, which is an SDK setup as well, so… Okay.
Someone would need to take a look.
to maybe try to reproduce or June. I don't think it's… Fun for anyone to watch me try.
**Jamie Danielson** 17:02 Let me click.
**Trent Mick** 17:03 I didn't understand.
**Jamie Danielson** 17:07 No, I wonder… Okay, I guess they gave, like, a… small Reaper, but ideally…
**Trent Mick** 17:23 page components.
This is Next.js instrumentation, isn't it?
**Jamie Danielson** 17:37 I'm feeling like it is, like, part of me is wondering, like.
If they could also open an issue in… The Azure repo?
Because it's, like… there's some kind of issue with something maybe happening twice that's not specific to OpenTelemetry, it's specific to the SDK that's in use.
Right.
Yep. And they might still come back and say, here's a thing that we need to fix, or whatever else, but they're gonna also find it a lot faster, I would think.
**Trent Mick** 18:11 Would you be willing to… I can ask. Got a comment on that one?
Stop me.
Thank you. Go to the next one.
Bunker doesn't accept that, it doesn't actually apply a schema, I thought.
I have a guess.
Do we… to know if… we'd had a separate PR for supporting That any attributes types, instead of being restricted to…
**Jamie Danielson** 19:12 Is that the new… isn't that a new thing that was just getting…
**Trent Mick** 19:18 That Mason could help.
**Jamie Danielson** 19:20 Oh, allow any values right above where your mouse is.
But…
**Trent Mick** 19:29 Yeah, I think that's gonna be… that's my strong guess, is that this is the limit, because… An array of objects? Is that not one that we're allowed to… yeah, because right now we only… well… Okay, so if I go to… Gonna ask me for a sec.
Any value? I thought… so I was looking at the types that we have right now.
Cyber back. Okay, long record.
The log record SDK emit function takes a log record, and the attributes are log attributes.
Which are any value maps, so I thought we'd gotten there, but I'm not sure what this PR then is.
Okay.
I'll take a note to look at this afterwards, but my guess is… space… Just taking a note for myself to look at this one later.
So I'll try to follow up on that one.
Unless anyone else wants to take that and jump in. Should I be changing the labels on these, that we've triaged them now?
**MG Marylia Gutierrez** 22:35 Yeah, I usually remove the triage, and… Can add one of the pieces?
**Trent Mick** 22:40 bubbly.
It's probably not a… I guess it counts as a bug? I don't know, anyway.
**Jamie Danielson** 22:45 Removing triage, right? If we put a priority. If we don't set a priority yet, then keep the triage on there.
I guess this would be… P2?
If it's a.
**David Luna Bistuer** 22:59 I agree.
**Jamie Danielson** 23:00 consistency.
**Trent Mick** 23:01 Teaching?
**David Luna Bistuer** 23:02 Yeah.
**Trent Mick** 23:06 Alright, and then… back to this other one, I don't know if you'd had a chance to…
**Jamie Danielson** 23:10 Yeah, put a comment on there, that's an EP3, actually.
Think.
So P3 or P4? P4, maybe? It's like… The telemetry is off, that's not an actual problem with the…
**Trent Mick** 23:30 Well, this is not this one, Class 1 through being complete or incorrect.
**Jamie Danielson** 23:34 So maybe that.
**Trent Mick** 23:37 Still, we have no idea if it's a bug on us, but .
**Jamie Danielson** 23:40 Yeah.
**Trent Mick** 23:40 Fair enough, too.
**Jamie Danielson** 23:42 It's fair enough to put it here.
**Trent Mick** 23:44 Worry is that once the triage goes away, then… Might not get looked at very closely, but…
**Jamie Danielson** 23:50 Gone forever.
**Trent Mick** 23:54 Okay.
Thank you.
Next.
Really?
**MG Marylia Gutierrez** 24:07 Yay!
**Jamie Danielson** 24:09 It was here. Yay.
**Trent Mick** 24:16 Okay, we don't have to look at these ones, it's, I wasn't here last week.
Right.
So, we'll see who wins these guys. I think we're almost down to one page, right? 26? 30, if we get those to 25 and under, then… It's a single picture. Okay.
So, we're doing the core repo this time.
She's on the call.
Hector today.
Suspect a lot of these are gonna be no update.
Okay, so Mark still has… Outstanding.
Comments on this?
**Jamie Danielson** 25:11 Yes, I supp.
**Trent Mick** 25:12 Gotta wait.
This one… So it's from way back, though.
Okay.
Anything happened recently?
**Jamie Danielson** 25:41 Oof.
**Trent Mick** 25:50 Okay. So, I mean, yeah, that was my understanding, too. It's mostly to work through the things on the milestone here, and then it'll be pretty straightforward to integrate those.
Once we have those.
**Jamie Danielson** 26:04 And I assume a lot of people have seen the recent.
**Trent Mick** 26:08 discussion blog post to start a discussion. It's very meta in the OpenTelemetry I.O.
repo about… Changing some things about, like, how… The project talks about stability for components.
**Jamie Danielson** 26:25 Oh, yes. I own an issue, actually, we talked about it a little bit last week, Marillia had brought it up.
**Trent Mick** 26:32 Okay, that is probably easier to find here.
**Jamie Danielson** 26:36 Yeah, the hotel graduation stuff there.
**MG Marylia Gutierrez** 26:40 Yeah, there's… yeah, this one is just pointing to nothing, but yeah, the recommendations for a towel, and we… I brought it up, kind of like, what were the discussions there?
**Jamie Danielson** 26:51 Yeah.
**Trent Mick** 26:51 So, yeah, and as Mark said on the side, that might give us a kick in the pants to start stabilizing some of these things.
**Jamie Danielson** 26:57 Yeah, so I was gonna create a meta-issue that I forgot about that I will try to do promptly after this meeting right now, that helps us track some of the stuff that we want to get done with it. Because the collector folks have an issue right now that's sort of similar, so I figure I'd just kind of use that as inspiration for the stuff that we want to do.
**Trent Mick** 27:16 Okay, cool.
I'd had a comment. One of the examples they used on that blog post was about the… the auto-instrumentations node thing.
Which I… I comped on that one, it felt a little bit weird, because that thing's not stable itself, so… I don't know, anyway.
There's still some questions about that whole thing, like… then no one can use anything from MotelJS, because there's not a… complete stable chunk of anything. I'm curious what the other languages… what state they're at there. I know Java's obviously past that mark, but… Yeah.
Okay.
Moving on.
**MG Marylia Gutierrez** 28:03 Yeah, just to give you, like, a context on the Java one, there was discussion that some of the things that they have, there are no specs for it, so they were like, we can mark it stable because there's nothing we can actually have to follow, so all of their agent stuff is, like, as soon as we decide it's stable, it's stable, so that works a little different for them.
**Trent Mick** 28:24 Okay.
Meaning that they're gonna, like, not… well, there was part of that spec discussion I was talking about the intent is not to yank away stuff, but is that mainly what they're referring to, or is it just…
**MG Marylia Gutierrez** 28:35 Yeah, so they… they're thinking, like, separating, saying, like, there should be a status for the implementation, and one for the spec. So, like, we can say, okay, this amount of convention, or whatever, now it's stable. And for the instrumentation, you can say, like.
is stable, but not following necessarily the stable convention. Because people think that stable, if it is not a stable, just means that it's not ready to be used, or it's just, like, full of bugs.
So the kind of idea is to say, like, no, no, it is stable in a sense of it's working, but it's not yet following, like, the convention, so it might change, like, names and stuff like that, so this is the type of breaks that you can expect. So that is kind of, like, idea, just to let people understand that they can use Thanks.
**Trent Mick** 29:26 Okay.
Oh, is this one just waiting for Mark to come back and merge?
**David Luna Bistuer** 29:35 You can, yeah, or you can hit the button.
**Trent Mick** 29:38 Well, I'm not gonna do it. Mark's not around this week. I'll let him handle all the… I'm certainly not gonna do it. If you're comfortable, you can go do it, David, but… I don't even know what this one is for.
**David Luna Bistuer** 29:50 I'll drop him a message in Slack, so when he comes back, he can click the button.
I'm sure he'll see it when he's back. Okay.
**Jamie Danielson** 29:58 I think it's mostly just from, like, not knowing anything about the PR, so… You know it, it's probably fine.
**Trent Mick** 30:08 Okay, this draft, and I assume there hasn't been any movement there.
Renovate… Skip those. Okay, and we were discussing this one just recently.
This one is… yeah, blocked. Waiting on… Some review for a while, so that one's maybe stuck a little bit.
Okay.
I think probably definitely open for someone if they want to jump on and help that one.
Okay, so that one still needs work.
I think it's the only thing we're gonna do here.
I have never looked at this one.
Yes.
Adding protector to everything. What does that do?
Someone with stronger TypeScript opinions is welcome to weigh in on that one.
**David Luna Bistuer** 32:02 You should.
**Trent Mick** 32:03 way.
**David Luna Bistuer** 32:04 My opinion is that it's just for type correctness.
So, the output the… After compilation, that code, it's going to look the same.
But… for, for user… for dev experience, maybe it's better to have this, so…
**Trent Mick** 32:24 Okay.
**David Luna Bistuer** 32:25 I'll have a look, you can assign it to me.
**Trent Mick** 32:28 I'll let you sign it, too. Well, okay, sure.
Thanks. Good luck.
I would have to go to TypeScript and learn what the actual implications of override is, something you remember.
Thanks.
Num… I know what that's about.
Sorry, hold on a second, we are doing this in reverse order, right? Yeah, we are.
**Jamie Danielson** 33:03 Right, it's, like, oldest to newest.
**Trent Mick** 33:06 Yeah, surprisingly recent.
we don't really have a whole lot of really old PRs, which is kind of nice.
Okay, interesting.
Someone would have to take the time to get in there.
Yeah, the complexity is something we want to do, or if there are alternatives.
Num.
**Jamie Danielson** 34:20 Yeah, because it is a feature, and… has gone stale. Have they commented on it since… Opening.
No, they haven't, but, I mean…
**Trent Mick** 34:32 No one's done anything on it, so…
**Jamie Danielson** 34:34 No, it was just a curiosity thing.
**Trent Mick** 34:37 So far.
I mean… performance is not something I think we've done a whole lot of.
Wow.
work on.
Like, when I… or, I don't know, at least I haven't… seen in the project since I've been around. I don't know.
**Jamie Danielson** 35:01 I think that's one of the.
**Trent Mick** 35:02 I've had internal work issues where, like.
We have a customer that's using in high load, and they observe performing it, but I hadn't seen any performance work there bubble up.
**Jamie Danielson** 35:11 Not a ton, but I think it's one of the things that's noted in the graduation stuff of potentially adding some kind of benchmarking, not necessarily with a specific goal of improving performance necessarily, but more of having it documented, or tested, or benchmarked in some way, so…
**Trent Mick** 35:30 Sure.
**Jamie Danielson** 35:31 This could end up being part of that, depending on… How it works.
**Trent Mick** 35:50 Sorry, I said oof, because I don't know anything about B3.
I think it's for my.
**Jamie Danielson** 35:54 Less about B3 and more about, casing, for B3. I feel like… Was it just, like, lowercase?
**Trent Mick** 36:07 Things.
**Jamie Danielson** 36:11 Or am I a liar? I might be a liar.
Like, I remember…
**Trent Mick** 36:23 Like, it would be unrelated.
**Jamie Danielson** 36:26 Yeah.
Say that again? Sorry.
**Trent Mick** 36:29 It's just changing request or response fields, like, not something that I've expected from the title, but…
**Jamie Danielson** 36:55 this is, like, ringing a bell in my head. Like, I remember something related to… maybe… Java… looking at Java and how they did this. Maybe it was, like, does anyone remember it was, like, Kafka and something else interop?
Oh, okay.
**MG Marylia Gutierrez** 37:20 Yeah, I'm still… I'm still confused by the… the same comment that Trent did, like, why the change from request to response has to do with… Yeah, the specific.
**Jamie Danielson** 37:28 the specific chain. That's why I was like, here's what I think this is for, and then I saw the code, and I'm like, this doesn't…
**MG Marylia Gutierrez** 37:32 Nope. That's what I thought, actually.
**Trent Mick** 37:37 I mean, that could be an accident that was just pulling in some unintended commit better than… Probably not, though, it is about B3 once, so… Like, it could be the tests are just totally wrong.
Okay.
Looks like Mark… Commented, and he responded.
**Jamie Danielson** 38:02 Oh yeah, and Swift and Java, yeah.
I'm curious about that.
PR there that's closed that's mentioned in Swift.
Like, what ended up happening there?
**Trent Mick** 38:20 So, then as well. No, that's…
**Jamie Danielson** 38:22 No.
Oh, it just got moved. Did it get…
**Trent Mick** 38:40 Where in Swift were.
Oh.
**Jamie Danielson** 38:57 I don't understand.
**Trent Mick** 39:03 Or did not.
Okay… So it just withered?
**Jamie Danielson** 39:17 Kind of seems that way.
If we go back to the PR… Is it linked higher up in the comments there, or in the history?
It just disappeared.
**Trent Mick** 39:51 Guess maybe that just didn't happen.
Jerry, why are there no… Final changes don't appear.
**Jamie Danielson** 40:10 Maybe they got rid of it before closing it?
**Trent Mick** 40:14 Or it was two files that have since just… yeah, okay, I don't know.
**Jamie Danielson** 40:18 Weird.
**Trent Mick** 40:18 Okay.
Mmm… I'm moving out for now.
Okay, looks like David and… Mark of both.
I'm done this…
**Jamie Danielson** 40:57 So right now, do we have a label for, like, Waiting on author.
something? Maybe that'll help us give us, like, at a glance, we can see…
**Trent Mick** 41:06 Needs author response?
**MG Marylia Gutierrez** 41:07 as well.
**Trent Mick** 41:10 Do we want to keep adding that when we're going back and forth? I don't know.
Sure.
**Jamie Danielson** 41:13 No, but this is more of, like, it looks like it hasn't been updated in, like, a month, and so, like, at a glance, we'll be able to see, like, why did this get left off? Oh, we're waiting on the author.
No, no, no.
**Trent Mick** 41:46 Is this the one that I commented on?
Okay, so this was a… for other people, this was a… Proposed performance improvement to the implementation of this.
With a benchmark script added.
Which is nice.
But when I ran it, it was not performance improvement on my machine, at least.
Why is the same timer slower?
And then… A little bit faster… Brahim… And then David ran, too.
And the news's a fair bit faster for you, right?
**David Luna Bistuer** 42:48 Yep.
**Trent Mick** 42:50 What's going on in my machine?
I'm never…
**Jamie Danielson** 42:53 Did you say what…
**David Luna Bistuer** 42:55 You don't have an apple chip.
**Trent Mick** 42:59 I do, I do.
**Jamie Danielson** 43:00 It is, I saw arm…
**Trent Mick** 43:03 And it's an ARM machine.
You saw Ram somewhere, or was that…
**Jamie Danielson** 43:07 And you're…
**Trent Mick** 43:08 Oh, there we go.
Okay, so I will…
**Jamie Danielson** 43:19 Someone else maybe run it.
**Trent Mick** 43:21 I'll go look at that one again.
Bam.
Let's go… Can I expense a new laptop so I can try it?
I have to get some work.
Yes. Yes.
**MG Marylia Gutierrez** 43:36 Yeah, I used to give this excuse when I were working, like, prior job. They're like, oh, you have to test in several regions, like, oh, but I can only test if I go to these regions in person. That is the only way that it would work.
**Jamie Danielson** 43:51 Only possible way.
**Trent Mick** 43:52 Only. Well, that's the only way, yeah.
It has to be my laptop in and.
**MG Marylia Gutierrez** 43:57 Yes.
**Trent Mick** 44:01 Okay.
I'm lost, where were we? Here we go.
Okay… before I get too deep, I don't expect to make any… work on exporters without Mark around, but maybe Mark doesn't want to be the exporter guy.
Oops, sorry.
Is this… Actually, David, I can't remember if we discussed this one. There was one that was talking about wanting to have a function for changing the headers.
For, like, expiring tokens or something, but that was a different one, right?
**David Luna Bistuer** 45:10 Yeah, if I recall properly, it's.
**Trent Mick** 45:18 Alright, well, I'm gonna homer back into the bushes on this one.
Sorry.
This one's in draft.
Again, exporter… I asked Mark asked.
Damn.
Right, looks like there's something to add here.
Okay.
Cool.
Sorry, everyone, for my slow reading.
Mmm.
**Jamie Danielson** 47:02 Doing a great job.
**Trent Mick** 47:04 I don't know if Jackson is on the call. Jackson had asked for a review of this last week.
Martin, I noticed you're on the call. If you want to scream at me something about tedious PRs, then you can go ahead at some point. I know it's coming. I don't know if we'll get there in time, though.
**Marten Hennoch** 47:22 Hmm.
No, I have no voice, I can scream.
**Trent Mick** 47:29 Do you want to skip ahead to that one? Given that… I don't know if you specifically got on the call for that one.
Is that one right near the top?
Oh, it's in the other repo.
**Jamie Danielson** 47:39 contribute.
**Marten Hennoch** 47:40 Yeah, it's constant. They fixed it today.
**Trent Mick** 47:43 I will jump across there.
Though it's… the answer's probably gonna be I should look at it offline, but.
**Marten Hennoch** 47:51 Probably, huh?
**Trent Mick** 48:00 Yes, I read for you, looked at it.
**Marten Hennoch** 48:02 There's an issue was about, scheduling here.
So the… Apparently, you can only have… One request at a time, and if you try to execute them both, it will throw.
**Trent Mick** 48:16 So my worry is that we're returning… aren't we patching a function that's synchronous, but asynchronously doing something in there, so that the user And have control of being able to only have one in flight at a time.
At that point.
I might be wrong, I have to go looking at.
**Marten Hennoch** 48:38 Yeah, I don't think that's the case.
Because everything… they… they use callbacks for everything.
And one of their methods returned nothing, so…
**Trent Mick** 48:50 Yeah, right, they are all void.
Okay, anyway, it's on my list to go take a look at this one.
**Marten Hennoch** 48:56 So it's kind of weird, but I don't see another way to do it.
**Trent Mick** 49:00 Yeah, I'm not sure that I did either. So, okay. I had just been looking at code, I hadn't actually been trying it against a real database, so I'll play with that a little bit and see if I can… prove that I can break it, if not.
**Marten Hennoch** 49:11 And enjoy your Microsoft Discord.
**Trent Mick** 49:16 Yeah.
Okay.
Thanks, anyway, back to our regularly scheduled program.
Before we… Okay, Jackson had asked for a review on this one. I don't know if Mark had… Okay.
That was 3 weeks ago… This might… I might defer and let… Mark, get back to looking at this one.
But I'll take a note. I'm gonna take a look at this one, too.
Corporation.
Scope info option. I don't know anything about that.
Olan's trying to get a review from someone on this one.
This is a Prometheus option.
Is it this…
**Jamie Danielson** 50:58 without scope info thing as a Prometheus thing?
curious, like, where… I guess they had mentioned something about… it being in Go. I was trying to find the…
**Trent Mick** 51:14 If you're trying to click and follow along, that's this, by the way.
**Jamie Danielson** 51:29 So, yeah, I guess Go has… Without scope info… Removed.
**Trent Mick** 51:41 Is that this one that he's talking about?
**Jamie Danielson** 51:48 There's the… links that I'm looking for.
**Trent Mick** 52:08 Yeah, there's a lot of back reading.
On this one, I think.
I'm not super adept at Prometheus, so…
**Jamie Danielson** 52:38 Yeah, it definitely needs, like, some… like you said, some reading and all that for that. I wonder if we could…
**Trent Mick** 53:05 Is he talking about spec?
**Jamie Danielson** 53:07 Yeah, it says, from the spec.
But some links or whatever might be useful.
Since we're… Less familiar.
**Trent Mick** 53:46 Okay.
Not gonna finish, but okay.
**Jamie Danielson** 53:59 And maybe just one more.
**Trent Mick** 54:50 I don't know if he did create an issue.
That was 2 days ago, so…
**Jamie Danielson** 54:58 I feel like they probably would have linked it.
**Trent Mick** 55:05 Let's a look, see if we… No.
Yeah, I don't see that he's added one yet, but this was just 2 days ago, so I'll just let this game sit here for now.
Expecting an issue, okay?
Or her, we could close it. Other people's opinions are welcome.
Got some draft… Well, this is not something I've proposed adding before, so I'm not so sure about us adding more environment variables.
**Jamie Danielson** 56:43 No, I mean, I feel like… Well, we've talked about adding environment variables. More recently, it has been, like, let's see what we add with the declarative config work, which I think they mentioned there in additional context also.
Marilla, what do you think?
**MG Marylia Gutierrez** 57:00 Yeah, I was actually… I was just trying to read if… if this… it was, like, a new environment variable, or no, it's something that already exists. I think it already exists.
The new one.
Is anyone…
**Trent Mick** 57:16 Richard?
**MG Marylia Gutierrez** 57:18 No, but I'm saying, like, did they created this just for JavaScript, or this exists in other SDKs?
Because if did it exist in others, then we can add. If it is something created just for us, then no.
**Jamie Danielson** 57:35 Yeah.
**Trent Mick** 57:49 That is… Oops.
**Jamie Danielson** 57:53 All that show… oh…
**Trent Mick** 57:55 So it's just this one, and… Oh, well, okay.
Yeah, so no, it's just that one machine.
**MG Marylia Gutierrez** 58:09 Yeah, so if it is just…
**Trent Mick** 58:11 search.
**MG Marylia Gutierrez** 58:12 Yeah, if it is just for us, then no, because we are not adding anything… anything new.
**Jamie Danielson** 58:17 Yeah.
**Trent Mick** 58:22 I lost the tab.
Goodbye.
And that was this issue.
Early, would you be willing to…
**MG Marylia Gutierrez** 58:35 Yeah, I can reply.
**Trent Mick** 58:36 Yeah, that one, or do you want to? Okay, thanks.
What's that one?
**MG Marylia Gutierrez** 58:40 Great.
**Trent Mick** 58:41 launch.
Okay, and one minute left, I think I'm gonna call it.
**Jamie Danielson** 58:48 That's fair.
**Trent Mick** 58:50 Anyone has anything else they want to bring up? If not… Thank you.
See y'all next week.
**MG Marylia Gutierrez** 58:57 And we'll see y'all next week, yeah. Okay. I won't join next week, but yeah.
**Trent Mick** 59:03 Okay, we'll see you later.
**Jamie Danielson** 59:04 Alright, we'll see you online.
**MG Marylia Gutierrez** 59:06 Yes, yes.
**Trent Mick** 59:06 Bye. Thank you.
**Jamie Danielson** 59:07 Okay.
