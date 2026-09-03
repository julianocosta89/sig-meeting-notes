SIG: OpenTelemetry PHP SIG
Date: 2026-09-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pawel Filipczak** 00:26 Hey, Chris.
How am I?
**Chris Lightfoot-Wild** 00:29 Hey, bro.
I'm okay, how are you?
**Pawel Filipczak** 00:32 I'm okay.
**Chris Lightfoot-Wild** 00:37 Busy week.
**Pawel Filipczak** 00:39 Yeah, I mean… Oh, yeah, staring to the dock, cool.
No.
So, do we have anything?
In the agenda for today.
**Chris Lightfoot-Wild** 00:54 Bob said he was gonna write something, I thought.
Which was about the, release schedule for the… Packages.
**Bob Strecansky** 01:05 Hello, gentlemen.
**Chris Lightfoot-Wild** 01:06 Speak of the devil?
There we go.
**Pawel Filipczak** 01:08 If any of you have access or possibility to edit the invitation, because there is no link to the To the agenda document.
In the Zoom meeting description, so previously it was available.
But now it is not, so…
**Chris Lightfoot-Wild** 01:28 I have access… do you both?
**Bob Strecansky** 01:33 I don't. We'll have to raise the community issue for that, probably.
**Chris Lightfoot-Wild** 01:40 I can link the… I've got it… Bookmarks, if you want.
Have you already got it, or… Yeah, I'll put it in the chat anyway.
**Pawel Filipczak** 01:51 Meetings… Okay…
**Bob Strecansky** 02:02 Sorry, just give me a… I'm just getting everything sorted, I'll be right there.
**Chris Lightfoot-Wild** 02:15 I, I'll copy last week's agenda over, and we can, to play with it.
**Bob Strecansky** 03:25 Good morning, boys, how we doing?
**Chris Lightfoot-Wild** 03:29 Beautiful things, are you?
**Bob Strecansky** 03:31 Other than the dream.
**Chris Lightfoot-Wild** 03:33 How's your, recovery going?
**Bob Strecansky** 03:37 From my… from the bachelor party? It's pretty good.
**Chris Lightfoot-Wild** 03:41 No, well, last week you were, like, on the sofa with your legs.
**Bob Strecansky** 03:44 Oh, yeah.
Forgot about that, that was, my knee's feeling a lot better, thanks for asking.
Maybe it was time with my boys. That's, That was good recovery, mentally, I guess, I'm not certain.
Bob.
Alright.
Yes, that is… First agenda topic… I guess we can get… we can get rolling. I don't expect anybody else.
**Chris Lightfoot-Wild** 04:13 I was gonna say, is Brett joining us today, then? I've seen there was an activity, but…
**Bob Strecansky** 04:17 He said he… I can't remember if that was a DM or in one of the cha- he said that he is sharing… putting his… putting Ruby to bed responsibilities is, like, it's always gonna be 50-50 whether I can make it or not.
**Chris Lightfoot-Wild** 04:31 Oh, that's…
**Bob Strecansky** 04:32 I understand. Young children are a lot of work.
Alright, so talking about packages, or package releases cadence, Yeah, so that person asked about the package release cadence.
And I think the thing, right, is we don't really have one now, right? We just sort of YOLO do it when we feel like it.
And maybe it's worth discussing what y'all think are a reasonable release cadences. Is it monthly? Is it on demand? Is it… because, like, I feel like there's a bunch of different scenarios we could have. Like, if we find a P0 security vulnerability, you gotta do the release very quickly.
Otherwise, like, when do we feel like we must release versus when do we feel like we should release?
**Chris Lightfoot-Wild** 05:25 I mean… other repos I've seen tend to… if they're using, like, Semva, they can have some automation around it and simplify the whole thing, right? They just…
**Bob Strecansky** 05:36 Yeah, I… I mean, I think… continuous release.
is fine, too. Like, that is always an option as well, if we want to do that. Just takes a little bit more effort. And do I think that's effort that's worth doing? Maybe. The only reason that I would be hesitant to do Continuous release is we often will, We'll often find something that broke Or packages, or, you know, whatever, especially since our CI isn't perfectly green right now.
Like, if it was green all the time, then I would be very happy to do it.
To do a continuous release thing, but it isn't right now, so, maybe that's the order of operations that we should take, is, like, get CI to green, then we could continuous.
**Pawel Filipczak** 06:28 But otherwise, if you have the… if we have the CI red, then we'll never make any release, right? Because we cannot be sure, so… Yeah.
**Bob Strecansky** 06:37 I agree with you, pal. Like, right now, like, if we continuously release, or we… cadence released now, in our current state, it would we sort of have the same thing. I don't know why that makes a big difference for me. I guess it doesn't, really. I don't know, do y'all have strong opinions here?
**Pawel Filipczak** 06:58 So, if… I think that if you… release every change, so we can continuously make any release, then we'll get the feedback sooner. So that's… that's okay for me. So even if we'll break something, then at least we can… Fix it quickly.
But if we will just, you know, keep the things… Or keep the bugs which are not visible to anyone.
Then they can last in somewhere and can be forgotten.
So, at least we'll get the fast feedback. And of course, we should put the grain CI as our priority right now.
**Bob Strecansky** 07:41 Yeah, I agree.
**Pawel Filipczak** 07:42 Yeah, I think the split, at least in the country repository, the split started by Reese's… Something which can help us a lot.
**Bob Strecansky** 07:52 Yes, I agree with that, too.
Good work, Chris.
**Chris Lightfoot-Wild** 07:58 I'll try and do a few more of those, sorry, I've just been…
**Bob Strecansky** 08:02 Yeah, that's what…
**Chris Lightfoot-Wild** 08:03 He'll be taking me away and hoardy all the time, it's terrible.
**Bob Strecansky** 08:06 Aww, what a shame.
**Chris Lightfoot-Wild** 08:09 Well, steak is too buttery.
**Bob Strecansky** 08:12 - We call them… we'd say caviar problems are still problems.
Okay, so that's cool.
So, I guess, like, that… This is what we need to focus on more than anything. Bold, italics, underline.
Because right now, it's green in main, but it's not green in Contrib. Is it green in instrumentation?
**Pawel Filipczak** 08:42 I don't remember.
**Bob Strecansky** 08:44 I don't… I realistically don't remember either.
Oh, before I forget, pal, have you spoken with Sergey yet?
**Pawel Filipczak** 08:58 Mmm, that's, you know, fewer cents.
**Bob Strecansky** 09:01 Yeah, he DM'd me, too.
I won't… I won't expect him anymore, but he may show up.
**Pawel Filipczak** 09:08 Hmm.
**Bob Strecansky** 09:11 Alright, yeah, this one's… this is green now, so it's just contribib that we have to get to green.
That's not that hard, right?
Namous last words.
Okay. Let's see, let's see… What, does anybody else have agenda topics before we walk to boards?
**Chris Lightfoot-Wild** 09:46 Olean, talking about that contrary split, the workflow… so Renovate keeps trying to bump… the tagged version of, like, I guess, essentially main.
So every time you merge to main, it would obviously then come back later and go, hey, there's a new commit on main now. Which is great.
I don't know if… Either we tag a release of contrib, like, with the workflows as we're happy with them, or… Move that shared workflow somewhere else, so it doesn't constantly change.
again, I think I might have raised this previously, but I've just seen a few more renovate PRs doing the same thing.
**Bob Strecansky** 10:25 Do you think that… is that a renovate setting that we could change?
**Chris Lightfoot-Wild** 10:29 I guess potentially, yeah, to just disable it for these specific files, because, like, we want it to be the latest one, don't we, Maine? Because… Right.
So maybe that would work.
**Bob Strecansky** 10:40 Okay. We can give that a… we can give that a go, I guess.
**Chris Lightfoot-Wild** 10:45 Yeah.
Maybe that's one that, Claude or whatever can answer for us quite quickly.
**Bob Strecansky** 10:51 Yeah, I'm certain… I'm certain that, Claude.
Oh, my Claude.
Cool.
Alright, let's go check out our open stuff.
Let's see… Nice.
Renovate, renovate, OpenTelemetry bot, renovate. Sam… oh yeah, this… this person has been… Sam Alsa has been putting in a lot of stuff around system clock and timings.
Should just merge some of these renovated bad boys, too. I'll take that as an action for this week.
Same here, lots of renovate, let's renovate Jerry, yeah, Jerry's still working on that, trying to get that repo set up.
So… We appreciate, you…
**Chris Lightfoot-Wild** 12:10 It's gonna be in contrib for the time being, and I was okay with it. Brett had a sort of an issue.
Oh, well, minor concern that… I'll see if Brett comes back to that, but if, Maybe that's something we can ship soon.
**Bob Strecansky** 12:26 Okay.
Cool.
And instrumentation.
**Chris Lightfoot-Wild** 12:33 I mean, he's done very well, Jerry, hasn't he? To persist, or… This is a…
**Bob Strecansky** 12:38 I feel so bad for him, this is, like, his first thing with OpenTelemetry PHP, and he's just been like.
Pushing the Atlas stone up the hill for forever.
**Pawel Filipczak** 12:48 By the way… Going back to country, is it… can we merge the trace, attributes, migration?
**Bob Strecansky** 12:56 Who's attributing?
**Pawel Filipczak** 12:57 Yes, it's…
**Bob Strecansky** 12:58 this far.
**Pawel Filipczak** 12:59 First or fifth one here.
**Bob Strecansky** 13:01 This one. Oh, yours.
**Pawel Filipczak** 13:03 Yeah, yeah.
**Bob Strecansky** 13:04 It's been approved. So, yes, I can merge it. And you know what? I will merge it.
**Pawel Filipczak** 13:10 Great, thank you.
**Bob Strecansky** 13:11 Hey, you're welcome.
**Pawel Filipczak** 13:12 So I can move on.
**Bob Strecansky** 13:14 Well, this is… Alright…
**Pawel Filipczak** 13:18 Right.
**Bob Strecansky** 13:20 And… Yeah, nothing else crazy here, nothing else crazy in instrumentation… Nothing else. Anything exciting in the industrial land, Pawel?
**Pawel Filipczak** 13:31 Nothing, nothing, nothing. I merged one of the… Of the… of the issue today, but so, yeah, it's up to them.
**Bob Strecansky** 13:43 Cool beans.
Alright.
Let's check our stats.
Oh, we're so close to 50 million!
We'll get there. It looks like this is… it looks like we're taking off a little bit here, gentlemen, that's good news. I like this… I like this steeper curve here.
That means one major company started installing on all their hosts.
Cool.
Anything else that y'all want to discuss before we adjourn?
**Pawel Filipczak** 14:21 No, I will focus on making CI green, at least in country, so…
**Bob Strecansky** 14:26 Cool. Yeah, we can all focus on that as we have time and effort to do so.
**Pawel Filipczak** 14:31 No.
**Bob Strecansky** 14:32 Alright, we'll see you all.
**Pawel Filipczak** 14:33 something I will let you know on the Slack.
**Bob Strecansky** 14:36 Sounds good, yeah, I'm happy to review.
Alright, we'll see you all on the internet.
**Pawel Filipczak** 14:41 Cheers.
**Chris Lightfoot-Wild** 14:42 Bullet.
