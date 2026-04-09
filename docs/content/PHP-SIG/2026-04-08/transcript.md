SIG: PHP SIG
Date: 2026-04-08
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 00:20 Yeah, bro.
**Bob Strecansky** 00:21 Ray, how are you?
**Chris Lightfoot-Wild** 00:24 Alright, thank you, how are you?
**Bob Strecansky** 00:26 Doing alright.
**Chris Lightfoot-Wild** 00:30 Started watching, is it called For All Mankind?
**Bob Strecansky** 00:35 No, no.
**Chris Lightfoot-Wild** 00:35 week. Have you seen it?
**Bob Strecansky** 00:37 -
**Chris Lightfoot-Wild** 00:38 I'm surprised no one's mentioned it to you. There's a section where they all start saying hi, Bob, to each other.
**Bob Strecansky** 00:45 Oh, that's true.
**Chris Lightfoot-Wild** 00:47 Reminded me of that.
**Bob Strecansky** 00:48 TV series.
**Chris Lightfoot-Wild** 00:50 Yeah, that's it.
**Bob Strecansky** 00:51 I see.
**Chris Lightfoot-Wild** 00:53 Like, stir-crazy, and they've only got, like, one or two episodes beamed up to them of a certain chat show.
They say hi, Bob. So then they start doing that to each other, and…
**Bob Strecansky** 01:04 That's funny. I just finished reading, not too long ago, Project Hail Mary.
**Chris Lightfoot-Wild** 01:10 Oh, nice.
**Bob Strecansky** 01:11 Yeah, it's not same. It feels like it's not the same.
**Chris Lightfoot-Wild** 01:13 Is that in prep to watch the film, or have you seen it?
**Bob Strecansky** 01:16 So, I hadn't… I'd…
**Chris Lightfoot-Wild** 01:19 I'm moving.
**Bob Strecansky** 01:20 Let me… let me… let me, start over. So my boss told me to read the book, and I had no idea that the movie was coming out, which is good. She's like, I think there's a movie, but if there is, don't watch the trailer.
And so, I read the book, and it was great, but… I am very… Chris, I am very excited about a new piece of technology that I got this week. This is very rare that I get to share stuff like this. So I got a, a portable… e-ink creator like a Kindle.
That goes on the back, clips on the back of your phone with a MagSafe connector.
**Chris Lightfoot-Wild** 01:54 Oh, wow.
**Bob Strecansky** 01:55 Isn't that cool?
**Chris Lightfoot-Wild** 01:57 That's awesome.
**Bob Strecansky** 01:58 Yeah. So, like, it keeps you from doomscrolling, you just, like, anytime you have a micro… a couple micro-minutes, you just read instead of…
**Chris Lightfoot-Wild** 02:05 You just flip the phone around, and then you can… needless.
**Bob Strecansky** 02:08 Yeah, it's kind of fun.
**Chris Lightfoot-Wild** 02:13 Might have to look into one of those.
**Bob Strecansky** 02:15 They have all sorts of, like, cool custom hackable firmware, too, so there's, like, all sorts of fun things you can do.
**Chris Lightfoot-Wild** 02:24 Nice.
**Bob Strecansky** 02:25 Is it just gonna be you and me today? This is a rare one.
**Chris Lightfoot-Wild** 02:28 Yeah, I'm not sure. I guess we need… there's a… just about the templates, there's just one thing I wanted to add on to the… the agenda.
**Bob Strecansky** 02:35 I'm doing it, I'm doing it right now.
I wonder if, Sergey and, Pal have something elastic-related.
I have a couple things on the agenda, too, but… They're not… none of them are super important.
Alright, you should have the agenda items now.
**Chris Lightfoot-Wild** 02:57 Sweet and switch.
**Bob Strecansky** 02:59 release… Oots, and then…
**Chris Lightfoot-Wild** 03:09 So I didn't…
**Bob Strecansky** 03:13 test coverage… Alright.
Oh, I can share my screen, I guess.
Does my ultra-wide bug you?
**Chris Lightfoot-Wild** 03:54 No, that's fine.
**Bob Strecansky** 03:58 I changed… teams and companies at work, so I'm in a new space.
**Chris Lightfoot-Wild** 04:05 Oh, okay. Are you still within the same umbrella, into it.
**Bob Strecansky** 04:10 Kind of.
I'm working… I'm actually working on QuickBooks right now.
And… Yeah, so it's… that's a big shift for me.
That just, like, happened abruptly on Wednesday. My boss was like, you have 4 hours to decide if you want to stay on our team that's halving, or go work on this new project. I was like, okay, I think I can read the writing on that wall.
**Chris Lightfoot-Wild** 04:35 Yeah.
I hope it's the only one.
**Bob Strecansky** 04:40 Yeah, it's, it's… I have worked in the infrastructure space for, like, pretty much my whole career, and this is the first time I'm working on a product team, and that's very, very different, but… also working in Kotlin, which I've never worked in before, so… We're getting there.
Nice. Alright, let's do it. Let's do your topic first.
**Chris Lightfoot-Wild** 05:03 Oh, cool. It was only, I reviewed something for the Laravel 13 thing that someone's contributed. Okay. And then I was just getting, like, kind of pinged on it, but I said I can't merge it, so I was wondering if you could have a look.
It's very minor.
**Bob Strecansky** 05:17 Oh, excuse me, this one's real tough.
I will approve and merge.
**Chris Lightfoot-Wild** 05:23 But it's probably taxed onto the end of your release plans anyway, so…
**Bob Strecansky** 05:27 Yeah, so, yeah, that's in… that's on my agenda, so we can talk about that in a second.
**Chris Lightfoot-Wild** 05:32 Nice.
**Bob Strecansky** 05:33 Oh… squash and urge… Alright, it's in.
**Chris Lightfoot-Wild** 05:40 Thank you.
**Bob Strecansky** 05:41 You're welcome. Alright, so… now… so, we've talked about your topic, now we can talk about my topics.
So, I am almost done with my previous release. I have a couple more, like, small ends to tidy up, which I'm planning on doing sometime this week, and then I'll probably do another new release next week. I want to give, like, a tiny bit of time in between the two of them, just to, like.
triage or troubleshoot if needed, or whatever, so… I guess I should write this in here.
**Chris Lightfoot-Wild** 06:21 When you say release, which bits are you releasing? Is there a more specific?
**Bob Strecansky** 06:25 Yeah, so…
**Chris Lightfoot-Wild** 06:26 I don't think so.
**Bob Strecansky** 06:28 Tele entry.
HP DevTools. So if you… this… I'm following this development tools, release plan. So I don't know if you've seen this before, read through it or not. This is how we release all the, like, get split things in PHP land.
So, that's… I'm creating new releases on each of the repositories, and then doing the release to Peckle, and all of those things.
**Chris Lightfoot-Wild** 06:56 Cool. Sorry, because I see you've done a release for the instrumentation, package, aren't you? Yeah.
**Bob Strecansky** 07:03 That's part of the release plan, so that's… yes, that's part of, doing that, so… I hadn't done that before, Brett had always done it, but he is… with babies, so… I was… I was handling it.
Alright, I also had a couple pull requests open that need a look. I added ClaudeMD… here, I can just pull them all up really quick.
Mmm, let's do it this way… My pull requests… So I added a couple bot MDs.
And I added a, unit test coverage improvement. So these… these Cloud MDs, I updated this one. I think you approved it, and then I had to pull in a branch from you, so if you could just give me a rubber stamp on that, that would be great.
**Chris Lightfoot-Wild** 07:51 Yep. Hey, Paul.
**Bob Strecansky** 07:53 Hey, Paul, I might need the same thing here.
And then, last but not least, I was able to use Quad to help us improve our, you know, test coverage for Contrib and some of the other packages, so I think that those will be… I think that's one place where this… where AI can be very, helpful for us. I've read these, and they seem like relatively sane changes, so… I want to get to a point where we're passing CI checks and have the code test coverage that we expect and stuff, so… I'm going to try and nudge that along.
So, up.
So those, those are the things that are open for me.
Yeah. Release, spot MD, Tesco coverage.
**Chris Lightfoot-Wild** 08:38 So all those Claudy-esque PRs are ready for review now, are they?
**Bob Strecansky** 08:42 They should be, yeah.
They're… I mean, they're all just… I went into each of the repositories, ran the slash init, and committed it. It's just the right… that's how you initialize a repository to be used with Cloud effectively, so… If you see something glaring in there, you can feel free to comment on it, but it's mostly just, like, an automated thing.
**Chris Lightfoot-Wild** 09:03 Cool.
Claude won't be offended.
**Bob Strecansky** 09:06 I don't think so, nor will I.
I'm very… I'm very unoffendable.
I live in America, there's offensive things every day, everywhere.
So, yeah, those were… those were the open things that I… I mean, that's a lot of open things, but those were the open things I had.
**Chris Lightfoot-Wild** 09:28 Awesome.
**Bob Strecansky** 09:28 Paul, did you have anything you wanted to discuss today, or you just came to hang out?
**Pawel Filipczak** 09:35 Not much, so we finished the shadowing of the dependencies, so I tested it with some bigger apps.
And it works, so… Today, maybe tomorrow, we will make a next treatise with the 020.
Version, and that's it, so… I'll be glad to get some feedback from you, if you have some time, but please wait for the release first.
Yeah, so that's all from us.
**Bob Strecansky** 10:09 That's, I mean, again, small update, big impact. That's cool, thanks for sharing.
That's about it for me. Y'all have anything else you want to discuss?
**Chris Lightfoot-Wild** 10:30 Do you have a preference of some of the PRs that I might have, like, approved, but still needs you to, like, locate to merge? Do you want me to… Request review from the approvers group, or just, like…
**Bob Strecansky** 10:44 We're…
**Chris Lightfoot-Wild** 10:44 or something, no.
**Bob Strecansky** 10:46 I think, unfortunately, right now, the reviewers group is me, because Brett…
**Chris Lightfoot-Wild** 10:49 Yes, but…
**Bob Strecansky** 10:50 away from the keyboard, so… You can either DM me if that's easier for you, or you can… you can ask an OTELPHP ad… maybe just ask an OTELPHP admins, just in case Brett just, like, happens to see them. And that's probably… like, DMing is almost never the answer, as we all know.
**Chris Lightfoot-Wild** 11:07 Cool. Yeah, I just didn't know if we should have, like, a label or something, or I don't know if that would necessarily even help, but, like… The tags…
**Bob Strecansky** 11:16 It tags all of the, reviewers automatically.
when you open a pull request, but to be blunt, like, often a lot of those just, like, fall out of the top of my inbox, because I have so many of them. So, if there's one that you're, like, itching to get through, just…
**Chris Lightfoot-Wild** 11:33 It wasn't particularly me, it's obviously more like, if I've approved it and someone's gone, oh, this Chris Gale, is now the blocker, and I'm like.
you know, how can I unblock other people a bit more?
**Bob Strecansky** 11:44 I mean, alternatively, Chris, you have definitely proven yourself worthy enough of being at least somebody that can merge NPRs to this repository. We can also go that route, too.
**Chris Lightfoot-Wild** 11:56 I guess maybe there's some potential in the future for at least the Laravel subtree part of it. I don't know if that's…
**Bob Strecansky** 12:01 I think you've… I mean, you've… you've proven yourself over and over again that you're responsible enough to be a part of this repository, so, if you… if you want to, like, request that… that level of access in the admin… in the, community repo, I'll absolutely vouch for you.
**Chris Lightfoot-Wild** 12:20 Okay, I could, I could look into that. Yeah, thank you.
**Bob Strecansky** 12:23 Yeah.
**Chris Lightfoot-Wild** 12:23 Did we… I know in the past, we had, Not just agenda topics, but we're still going to go through the… our project board that he started in the past.
**Bob Strecansky** 12:34 I haven't been maintaining the project board. We probably could or should, I just haven't had the cycles to do that.
**Chris Lightfoot-Wild** 12:41 I feel very similar, to be honest.
**Bob Strecansky** 12:45 It's like, I have a very limited amount of time to, to reserve to this project, even less so now, but I'm on a different team, so I'm, like, trying to weigh, like, keeping momentum and keeping organized, so perhaps we need to have… maybe… Not today, because I don't have the mental energy to do it today, but maybe next week, we could, like.
Walk through the project board and move some of the things around, and potentially, like, get to a better state where we all know where we're at.
**Chris Lightfoot-Wild** 13:17 Yeah, that sounds good.
**Bob Strecansky** 13:20 But we can go through… we can, We can walk the repos real quick, too, that's a good idea.
33 million installed. This… this number used to make me feel good, and now I see, like, the open cloth stuff that has, like, 33,000, or, like, you know.
33,000 GitHub stars in a month, and I'm like, oh, okay.
That's a upper community, too.
Alright, let's look at the open pull request.
This would be… Pin dependencies, meaning… oh.
Looks like this one needs a review.
**Chris Lightfoot-Wild** 14:00 Are you preferring the… the renovate stuff now to…
**Bob Strecansky** 14:04 Dependable. Yeah, it's definitely a lot less intrusive.
Which is good.
**Chris Lightfoot-Wild** 14:26 Oh, well, that was the one… I've already looked at that, I didn't think that was, Maybe you can clarify, you might have a better understanding. I… I don't think we should change it.
**Bob Strecansky** 14:41 Okay, that's fine.
**Chris Lightfoot-Wild** 14:43 Well, my understanding might have been incorrect with that. Do you have much experience with the hotel collector? Like, because I didn't know at this point, like.
Should someone from a hotel collector be… weighing in.
Because I think the functionality, though, is… hotel collector specific, but I'm not entirely… you know, I'm not 100% on that.
**Bob Strecansky** 15:01 So, containers with spam attributes on PHP container, all spam information. OpenSearch Database, I got an exception. Wrong attribute names are hard-coded.
So I have to do them with constants… Do I get the issue? Like, code function is wrong, code function is… Yeah, you're, I mean, you're right here, this should be the same, like… They may… they might have changed the semantic convention from 125 to 130.
**Chris Lightfoot-Wild** 15:39 But the way I understand it is that we're omitting it correctly for the time.
**Bob Strecansky** 15:44 Yep.
**Chris Lightfoot-Wild** 15:44 Down to the collector to handle a migration to the newer way.
**Bob Strecansky** 15:48 Yeah. I also think we should probably ask him what version of the collector he's running, too, right? Like, that would help us to troubleshoot, maybe?
**Chris Lightfoot-Wild** 15:56 I think it was 145, it says it somewhere in that.
**Bob Strecansky** 15:59 Does it?
**Chris Lightfoot-Wild** 15:59 message, yeah, excuse me, but, yeah, at the time, I couldn't… the… I can't, tag the, sort of, hotel collectors group or anything, so I'd have to… Maybe… link this in the Hotel Collector channel.
**Bob Strecansky** 16:12 They have, yeah, they have a… what is it, collector?
OTO Collector Dev would be the right place.
**Chris Lightfoot-Wild** 16:19 Yeah, I just did, obviously, like, like a work account, typically you could just tag another team or something, but it seems that in the PHP team here, I can't tag… Overall Collector team.
**Bob Strecansky** 16:33 Is there enough…
**Chris Lightfoot-Wild** 16:34 I don't… unless there isn't a team member for it, but…
**Bob Strecansky** 16:37 Oh, it's, Hotel Collector…
**Chris Lightfoot-Wild** 16:42 Yeah, I don't think I get the same list as you.
**Bob Strecansky** 16:44 Oh, okay.
**Chris Lightfoot-Wild** 16:46 Part of your book.
Anyway, it was… yeah, it was more… this was another one, sorry, I didn't… I feel like I've kind of blocked something here, because I've answered to it, and then it's, like, you know, dried up, because… You know, this person's not gone and followed up with Colette's team, and neither have I, so…
**Bob Strecansky** 17:09 Alright.
This span suppression… this, span suppression one, looks like you approved this… we're ready to merge this.
Whoa.
I guess I can… I guess I should review this before I merge it. I'll do that later.
Contrib just has a bunch of renovated garbage.
We were talking about this one.
Look, this is another one, it looks like you approved this, and we're probably ready to merge this, yeah?
**Chris Lightfoot-Wild** 17:56 Yeah, probably a failure on my part for, obtaining you again, sorry, but I forgot.
**Bob Strecansky** 18:01 No, it'.
**Chris Lightfoot-Wild** 18:01 That's…
**Bob Strecansky** 18:02 That's on me, I need to be more diligent here.
**Chris Lightfoot-Wild** 18:06 I think that's the thing with, like, the renovate stuff, isn't it? That, like, it's, like, noisier, pins itself.
**Bob Strecansky** 18:10 Yeah.
**Chris Lightfoot-Wild** 18:11 And then you just, like, get lost in it.
**Bob Strecansky** 18:13 It really does.
So… Alright, and then instrumentation… I've… I really wish that they would just auto-merge those, but… Yeah, so these are the… these are two other ones.
That.
**Chris Lightfoot-Wild** 18:30 I mean, there's been a lot of supply chain attacks, though, recently, hasn't there? So, maybe it's safer not having auto-merge, but…
**Bob Strecansky** 18:37 Yeah, y'all, there have been a lot of supply chain attacks, and Yeah, it's been… been kind of a mess, huh?
**Chris Lightfoot-Wild** 18:48 Thankfully, I don't have to touch any node, so…
**Bob Strecansky** 18:51 Right.
**Chris Lightfoot-Wild** 18:52 I was, I was…
**Bob Strecansky** 18:53 I was reading an article the other day. All of the, like, different node package managers have utilities to not pull in stuff unless it's, like, a week older or whatever. Like, you can explicitly set.
And they all have different units and names, like, for the same thing.
**Chris Lightfoot-Wild** 19:11 Hmm.
I'm not aware that Composer has something similar, so it feels like it's only a matter of time before.
you know, it just turns on to Composer, so maybe we do have to remain vigilant, I suppose.
**Bob Strecansky** 19:24 Yeah, probably. Well, I mean, the problem is, you can only remain so vigilant, right? Like, when those renovate PRs come in, am I going to, like, read through them and test the code every time? No. Nobody's gonna do that.
So, it's just, like, a best faith thing, which is never fun, but… The alternative is letting the old stuff slide, and definitely having some sort of vulnerability, so… She said.
You just have to, I guess you just sort of have to take it as it comes.
**Chris Lightfoot-Wild** 19:55 So…
**Bob Strecansky** 19:58 Sweet.
Alright, well, We'll wrap up, and next… I'll plan next week on spending some time to clean up the project board, and maybe that will help us to keep momentum.
**Chris Lightfoot-Wild** 20:11 Awesome, thanks very much.
**Bob Strecansky** 20:13 Alright, we'll see y'all next week.
**Chris Lightfoot-Wild** 20:14 Cheers, hello.
**Pawel Filipczak** 20:16 You know what I am.
