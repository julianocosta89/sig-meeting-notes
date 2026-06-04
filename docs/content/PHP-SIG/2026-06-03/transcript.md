SIG: PHP SIG
Date: 2026-06-03
Duration: 16 minutes
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 00:36 And whoop.
Blue?
I'm not sure I can hear you, sorry.
I can't hear.
the…
**Bob Strecansky** 01:05 That's funny.
**Chris Lightfoot-Wild** 01:07 Okay, you know. Go ahead.
**Bob Strecansky** 01:09 Excellent.
**Chris Lightfoot-Wild** 01:12 Hey, Bill.
**Pawel Filipczak** 01:13 Hey, guys.
**Bob Strecansky** 01:15 Whoa.
How was your trip, Chris?
**Chris Lightfoot-Wild** 01:19 Yeah, it was, it was great. Yeah.
**Bob Strecansky** 01:23 Time to hear it.
**Chris Lightfoot-Wild** 01:28 Have you had a haircut book?
There's really like a cut.
**Bob Strecansky** 01:32 A couple weeks ago.
I think I just haven't, I took a shower last night, so this is a different thing… different way than you normally seem.
**Chris Lightfoot-Wild** 01:41 Maybe I was too bleary-eyed to notice last week.
**Bob Strecansky** 01:43 Yeah, maybe so.
**Chris Lightfoot-Wild** 01:44 with caffeine.
**Bob Strecansky** 01:45 Yeah, that's… That transition's always difficult, isn't it?
**Chris Lightfoot-Wild** 01:51 Yeah, back into the swing of things now, like…
**Bob Strecansky** 01:53 That's good.
Al, do you… do you have any, vacations this summer?
**Pawel Filipczak** 02:05 I didn't plan it yet.
Oh, I want to travel around my country, so…
**Bob Strecansky** 02:11 Yikes.
**Pawel Filipczak** 02:12 But, no, no plans yet.
**Bob Strecansky** 02:16 Do you get a decent amount of summer vacation time like a lot of Europeans do?
**Pawel Filipczak** 02:22 Yes, yes, I have 26-day sales.
I collected more, so I have around 40.
Nice.
Yeah.
**Bob Strecansky** 02:36 I feel very fortunate in that I work… like, I work for a ban… like, Intuit's technically, like, a bank in a lot of ways, so we get a lot of the banking holidays, which is really nice, but American paid time off is bad.
Some of my friends… some of my friends after the interview were, like, interviewing for new jobs, like, you get 10 days of paid vacation a year? Like, what is that?
Not enough.
**Pawel Filipczak** 03:02 jump.
I can't even imagine it's how to work the hole here without break.
**Bob Strecansky** 03:14 I… and they do… I don't know if y'all are familiar with that or not, if that's just an American thing, but… have you all heard of unlimited paid time off?
**Chris Lightfoot-Wild** 03:23 Yeah.
**Bob Strecansky** 03:25 That's a big crock.
**Chris Lightfoot-Wild** 03:27 Yeah, I've been in that trap previously, yeah.
**Bob Strecansky** 03:30 The first year I had that, I took 4 days of vacation. I very vividly remember that. I was very dumb.
**Chris Lightfoot-Wild** 03:36 Hmm.
**Bob Strecansky** 03:40 Wait, are we waiting on anybody else?
**Chris Lightfoot-Wild** 03:44 I don't love.
**Bob Strecansky** 03:46 Okay, so…
**Pawel Filipczak** 03:47 So…
**Bob Strecansky** 03:49 Alright, let's rip.
Okay, let's… y'all can see my screen okay?
Nope.
Got things out of here.
Let's go take a look. I don't… do y'all have any… like, let's start. Do y'all have anything that you want to discuss today?
**Chris Lightfoot-Wild** 04:08 Main… the main one I wanted to raise, I guess, sorry for not putting it on the agenda, was the Contra pipeline looks very broken.
**Bob Strecansky** 04:16 Okay.
**Chris Lightfoot-Wild** 04:19 I'm guessing at some point we just did, like, a renovate merge, and it's just fallen on its backside, but .
**Bob Strecansky** 04:27 I can take a… I'm happy to take a look at that.
**Chris Lightfoot-Wild** 04:31 Oh, cool, yeah. Equally, I was gonna say, I'll try and have a look at some point, if… if no one else can, but, yeah, I'll… Yeah, obviously, reviewing the other things where it's already read is really hard then, because people are like… Hey, what?
**Bob Strecansky** 04:46 Well, now… well, now that our main pipeline is green, you see greener pastures, right? Like, it's nice when it's not… Let's see… let's take a look, you said Contrib.
I'm gonna deviate from our path just slightly, because…
**Chris Lightfoot-Wild** 05:04 Oh, you've liked your option to me. Agents.
**Bob Strecansky** 05:07 Say it again?
**Chris Lightfoot-Wild** 05:09 You've got an Agents tab there.
**Bob Strecansky** 05:12 I do. What does that do?
**Chris Lightfoot-Wild** 05:13 I can't see that one, so I guess you've got something else?
Big proposed.
**Bob Strecansky** 05:18 I don't know what this is. I guess it's co-pilot stuff.
Anyway.
So you're saying this is broken?
**Chris Lightfoot-Wild** 05:28 Yeah, even if you just look him in, just… Yeah. Let's see a red.
**Bob Strecansky** 05:33 Okay, let's take a look.
**Chris Lightfoot-Wild** 05:38 So.
**Bob Strecansky** 05:43 Composer dependency, yeah.
**Chris Lightfoot-Wild** 05:45 I think it's the same… that same problem in all of the things, so… At least so we can… Same thing that crops up time and again, though, isn't it? The Vimeo Psalm…
**Bob Strecansky** 05:56 Oh, man. It's making me… it's making me think we gotta move towards MEGO more quickly.
I think Psalm… I think Psalm is not… like, I don't know how… I don't know how this is right now.
Is it still being maintained very well?
The last release was… Two months ago, which I guess isn't that terrible, but… Yeah, this is… this is just… this should be a simple dependency.
Swap around, but again, renovate just is causing a ruckus.
Let's see if this can do this.
Okay, let's leave that running while we go back to our agenda. Alright, let's take a look at OpenTelemetry PHP… Oh, I… speaking of, I moved some… an inactive member to Emeritus, Cedric, because he hadn't contributed in a couple months. If he comes back, we can always remove him from Emeritus, but they… They're getting to be a little bit more strict now about if you don't make contributions for a specific given length of time, then they just, move you to this status, I think it's to show active contributors versus just long-term contributors.
they did the same thing for me and Brett with DistroPal, just because we… obviously, we haven't contributed to the Distro, but, just thought y'all should know that that's, like, the process that happens. I think they're trying to… Encourage engagement.
Let's go take a look at these penguins.
Alright.
Sorry, Chris, I gotta get back to this one, too, the response body size. I know you made some comments on it, I just haven't had a chance to get back to it yet.
Pretty much.
**Chris Lightfoot-Wild** 07:53 I think Nibe was, left more than I did, perhaps, but…
**Bob Strecansky** 07:56 But yeah, both y'all did, but… He's not here, so I figured I'd mention.
**Chris Lightfoot-Wild** 08:01 Yeah, yeah, yeah.
**Bob Strecansky** 08:04 Great.
Coup on… Control… tension…
**Chris Lightfoot-Wild** 08:19 I thought, just looking at that list of PRs, I'd seen something that, There were supposed to be changes for Renovate to do weekly instead? Is that not the case.
**Bob Strecansky** 08:29 Yeah, that's true.
**Chris Lightfoot-Wild** 08:30 Have I imagined that.
**Bob Strecansky** 08:32 Yes.
This… no.
**Chris Lightfoot-Wild** 08:35 Only it looks like we're not getting that. Are they all coming… are they coming through weekly as separate ones?
**Bob Strecansky** 08:39 Yeah, they come…
**Chris Lightfoot-Wild** 08:40 They come…
**Bob Strecansky** 08:41 They come through on… they come through on Sunday now.
**Chris Lightfoot-Wild** 08:43 Right.
We're still getting a big wave of them, just more…
**Bob Strecansky** 08:49 This is… yeah, this is not what I was expecting. It says, please confirm you want Copilot to make this change in the OpenTelemetry PHP contributor repository on the default branch. You think that just lets it go straight through?
**Chris Lightfoot-Wild** 09:03 I would have thought it would be a PR, but that's not going to fix it anyway on there, if it's just.
**Bob Strecansky** 09:08 Let's see, let's see what…
**Chris Lightfoot-Wild** 09:09 The roof.
**Bob Strecansky** 09:09 Worst case.
**Chris Lightfoot-Wild** 09:10 root composer, right? It's not… it's not the root composer that's the problem, though, is it?
**Bob Strecansky** 09:13 Yeah, no, I think they was listing something else. Let's see what it says. I doubt it'll let you do this, but… If so, we can always revert if we have to. Okay.
Let me show some bubble… That's the same thing again, okay, I'm gonna have to look at that later. I don't think this is very good yet.
As we all know. Alright, let's take… let's go back to… Okay, not the main… oh, he looked at the main repo, it's a good contributor looking to see if there's any important pull requests that are not renovated.
Great.
Oh, I did see this, and this is something I did want to talk about in our meeting today. So this person, BuyerJC, made a very, very small change here, just allowing another version of this package.
And then… but then it was very unusual, because he said that he was… Or is this… this guy, or is it another one? There's somebody who made…
**Chris Lightfoot-Wild** 10:11 No, it's not… you're right, it's… it's the one that's closed there, if you look, it's JC by a… I think he said.
**Bob Strecansky** 10:16 Yeah.
**Chris Lightfoot-Wild** 10:16 But, presumably, it's, like, work account, you can't.
**Bob Strecansky** 10:19 Yeah.
**Chris Lightfoot-Wild** 10:20 So I knew the agreement.
**Bob Strecansky** 10:21 Yeah, that's… this is… yeah, this is what I was curious about. And so you've approved it, Chris.
But we can't… oh, he signed… I got it, he signed it with… it's my.
**Chris Lightfoot-Wild** 10:32 I think it's… I presume it's the same guy with, like, personal versus work account, but…
**Bob Strecansky** 10:36 I… I agree.
**Chris Lightfoot-Wild** 10:37 There's zero context, I guess. It could… obviously, it would be nice to get some, messaging on the actual PR.
**Bob Strecansky** 10:45 Yeah.
**Chris Lightfoot-Wild** 10:48 Because… where I'd noticed the pipeline had failed, it was like, I'm sure it's probably fine, but I actually don't know if Breath 3 will break the instrumentation, so, like, we need to fix the pipeline to see if this is…
**Bob Strecansky** 10:59 Yes, we do. Yes, we do.
Let's make that comment.
**Pawel Filipczak** 11:04 Yeah.
**Chris Lightfoot-Wild** 11:06 And obviously, with zero context on the PR, we're like, well, well… for all I know, I suppose that package has been compromised, version 3, and, you know…
**Bob Strecansky** 11:17 Right.
**Chris Lightfoot-Wild** 11:18 opens to supply chain attacks.
They're all the reds, aren't they?
**Bob Strecansky** 11:23 They are all the rage, so I'm sure that this, sells its best to me.
**Chris Lightfoot-Wild** 11:30 I even noticed, large, large companies have come to one in the Previous days, if you've seen that.
**Bob Strecansky** 11:40 Yep. Okay, anything else in here that's exciting?
Options, just get all the reappear ones.
Yo.
I had my PHPT tests.
**Chris Lightfoot-Wild** 12:00 Oh, sorry, yes, don't answer that. Yeah, sorry. That's good.
Can you stick that on those, sort of, actions, if you're not… you probably did last time, but, Which one?
Just that PRF, just click it on the… I can look at the docs, you know, the Google Doc.
**Bob Strecansky** 12:18 Oh, yeah, sure.
**Chris Lightfoot-Wild** 12:19 Stick it on the ass around.
Ugh.
**Bob Strecansky** 12:40 Right?
Let's scoot back here… Okay.
Alright… Cool. Okay, so we looked at all the repos, let's take a look at open issues and packages.
Is it?
**Chris Lightfoot-Wild** 12:58 Just… there was another, Emeritus PR somewhere there, wasn't there? Is it, should we be reaching out, do you think, to these people as well? Say, hey… or just, obviously, the passage of time, they've dropped off, like… Only the… I remember Cedric… Kind of us to… Join, and then…
**Bob Strecansky** 13:15 Yeah, and then sort of… the needs just sort of went… that's happened many times in this project. People will ask to join so that they can get… so that they can get the thing on their resume, and then they just stop doing… stop working on it.
Which, I don't know that that's what happened with Cedric, but I've seen that. I know there are other people that I know that have definitely done that.
**Chris Lightfoot-Wild** 13:35 Right.
**Bob Strecansky** 13:36 So… Anyway. Alright.
Melanie… issues… The stalls look like they're ballooning, which is nice.
Alright.
Anything else?
**Pawel Filipczak** 13:56 Maybe I'll give you some update on the distro.
**Bob Strecansky** 13:59 Yeah, let's hear it.
**Pawel Filipczak** 14:00 So, yeah, We are working on the PSR18, instrumentation, so we added that to the… to the… to the distro. PRR is… is ready.
I'm waiting for Sergey to take a look into that.
And, I also add that, support for the config file.
So it works well with the distro, and what next? We did a bit of refactoring, Mostly in the test environment for the end-to-end testing improvements.
And now I'm adding the support for the with spun attribute, because it was missing in the distro extension.
So, then it will be… We'll be one-to-one with the features of the classic extension, and of course, everything we add.
On the site, so yeah, that's what… what's… what's… what we are working on now, and I guess within two weeks, we'll make a release.
Because in the next week, we have a company meeting.
So, we'll be… we will not work, and we don't want to… to… to… to break anything, and… So, Andy.
**Bob Strecansky** 15:30 After that, we have… we have a hackathon this week, and I am very focused on that this week, so I know that feeling.
**Pawel Filipczak** 15:40 So that's all from us.
**Bob Strecansky** 15:42 Excellent.
Do you have anything else we want to talk about today?
Yeah, Chris will talk offline about cleaning up the… cleaning up Contrib, and we can give that a go together.
**Chris Lightfoot-Wild** 15:58 Cool, yeah, sounds good.
**Bob Strecansky** 16:00 We'll catch y'all internet.
**Pawel Filipczak** 16:02 Cheers, guys.
**Chris Lightfoot-Wild** 16:03 Good moment.
