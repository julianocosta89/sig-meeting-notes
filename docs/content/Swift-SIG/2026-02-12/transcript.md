SIG: Swift SIG
Date: 2026-02-12
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Vinod Vydier** 00:58 Good morning, Audi.
**Ariel Demarco** 01:01 Hey Vidalvis, how are you?
**Vinod Vydier** 01:03 I'm good. I guess, multitasking Like, crazy these days.
**Ariel Demarco** 01:11 Yeah?
**Vinod Vydier** 01:11 Yeah?
**Ariel Demarco** 01:13 Hmm.
**Vinod Vydier** 01:14 Beautiful.
**Ariel Demarco** 01:17 Yeah.
**Vinod Vydier** 01:17 Thomas, how are you doing?
**Ariel Demarco** 01:20 Yeah, also crazy days. We had a bunch of, things related to…
Planning, the new quarter, and all that stuff, so…
**Vinod Vydier** 01:30 You know, it's all good, good meetings, then.
**Ariel Demarco** 01:34 Yeah.
**Vinod Vydier** 01:35 Yeah, not furiously working on things, okay.
**Ariel Demarco** 01:41 I don't even know.
Good. Not that bad.
**Vinod Vydier** 01:45 Yeah, yeah.
**Ariel Demarco** 01:49 Wow.
**Vinod Vydier** 01:58 Oh, it's just the two of us, okay.
**Ariel Demarco** 02:01 What's reading?
**Vinod Vydier** 02:02 It's just the two of us yet, right?
**Ariel Demarco** 02:05 Seems to…
**Vinod Vydier** 02:05 This is, you know.
**Ariel Demarco** 02:08 Maybe, Nacho, it's scammy, he sometimes…
**Vinod Vydier** 02:11 It's mostly.
**Ariel Demarco** 02:12 Probably.
Other meetings, some of that stuff.
I was just finishing eating, so I just turned on Zoom and started, so…
I have one of my fingers really, really Bothering me.
**Vinod Vydier** 02:42 Oh, really?
**Ariel Demarco** 02:43 I think I…
**Vinod Vydier** 02:44 Keyboard? Keyboard injury, or…
**Ariel Demarco** 02:47 I think I… might have injured… on Monday, playing basketball.
**Vinod Vydier** 02:54 Oh, okay.
**Ariel Demarco** 02:57 So… probably it's that.
**Vinod Vydier** 03:00 How tall are you?
**Ariel Demarco** 03:04 No, not really at all. I'm 100… 1 meter, 78… 70 meters.
**Vinod Vydier** 03:09 Oh, okay, okay, okay.
**Ariel Demarco** 03:11 Not really at all.
**Vinod Vydier** 03:13 Okay, and I was thinking, maybe you're, basketball player from Young, and…
**Ariel Demarco** 03:20 No, no, I'm, I'm bad. We play with friends just to do some sports and all that stuff.
**Vinod Vydier** 03:25 My relationships.
**Ariel Demarco** 03:27 That's… that's basically it.
**Vinod Vydier** 03:29 Yeah.
**Ariel Demarco** 03:31 Playing for fun, not proficient.
To be professional, to be honest, but, you know?
**Vinod Vydier** 03:38 Yeah.
**Ariel Demarco** 03:39 Not that great.
**Vinod Vydier** 03:43 Well, actually, when I was, in, Buenos Aires, I think I saw some from my, apartment, my,
Airbnb.
I was in a nice area of the Palmero… no, what is it? Palmerto? No.
But learn more.
**Ariel Demarco** 04:03 Palermo, yeah.
**Vinod Vydier** 04:04 Yeah, gotcha, gotcha.
**Ariel Demarco** 04:07 Yes, it's starting to get… get traction here.
when I was little, nobody really played, there were no pitches at all. Now, I think more people are starting to…
like it, I don't know, father, parents are…
Training their sons in… in… or children in… in Basket, Originally, like, the only…
Things that were played were hockey, volleyball.
Football.
And, ripe.
those are the four things that, when I was little, it was common for people to play and do.
**Vinod Vydier** 04:50 Yeah.
No, I went to the football stadium, the one in…
The big, near, in, in downtown.
I'm just, forgetting all the names now.
**Ariel Demarco** 05:05 Priva?
**Vinod Vydier** 05:07 Yes, yes, yes, the one near that, art center, right? Yeah. La Boca.
**Ariel Demarco** 05:14 It's because you have in Palermo, you have close… close by, you have Nunez, where it's… the River Club.
**Vinod Vydier** 05:23 Did you go.
**Ariel Demarco** 05:23 to Caminito.
**Vinod Vydier** 05:24 isn't.
**Ariel Demarco** 05:25 the… In Boca, you also have the Boca Stadium.
**Vinod Vydier** 05:29 Yeah, the Booker Stadium is the… is the historic…
**Ariel Demarco** 05:33 Yeah.
**Vinod Vydier** 05:33 Cheers.
**Ariel Demarco** 05:34 Yeah, and it's really particular, because most beaches are, like, a circle or a noble. This is weird, because it's kind of a semicircle, and then you have a big, big wall like this.
That it's also full with people, so it's… it's… it's really amazing as a… That's a field, but…
**Vinod Vydier** 05:54 Yo.
**Ariel Demarco** 05:55 You know?
**Vinod Vydier** 05:56 One side is like, you know, it's like a flat… it's flat, right? It's like a straight air.
**Ariel Demarco** 06:02 Yeah, like a street wall.
that.
Hey, Billy.
**Billy Zhou** 06:08 Hey, guys.
**Ariel Demarco** 06:11 Okay, I think it's… All of us only today.
So I'll share my screen then.
Which ones?
Yes, this one.
okay.
So… Topics from last week.
I think the one, it was the release of Core 2.42.4.0.
I think Bryce did it, but we had an issue.
So we created this new topic as a retrospective.
of this. I don't know if, Billy, you have any new topics to discuss, or something from the…
Last week.
You wanna mention?
**Billy Zhou** 07:05 Yeah, I,
So, yeah, last week we, deployed the Core 2.4, and, unfortunately it was backwards incompatible because the, monotonic clock fix PR, like…
Modified the, global extensions we had to time interval, which…
Actually, like, I think my repo also depends on those, so,
Yeah, we just converted those to, from, like, N64 to Uint, I think. Anyways, I, I had a discussion with, like, a customer who, like, cut up… or not a customer, a user, this isn't, commercial, but,
Anyways, yeah, I proposed, like, a system improvement to, just run the, you know, integration tests against, main. This workflow includes that, and then,
If you can see… scroll down to… yeah, right here, you can see it catches it,
before I revert the change that, broke 2.4.
**Ariel Demarco** 08:12 Oh, this is the thing that broke CodeQL.
**Billy Zhou** 08:17 Well, not CodeQL, but yeah, the integration test, yeah.
**Ariel Demarco** 08:21 Okay.
Oh, because I was looking today, some time ago, like, if, I don't know, looking at this, got QL.
**Billy Zhou** 08:30 Oh, maybe CoQ will call it as well? Okay.
**Ariel Demarco** 08:33 For some reason.
I had many… it had many of these ones. I don't know if CodeCL fails because of warnings or not, that was something I was…
I wanted to ask you guys, do you know it, because it's weird. I don't see any, like, error at all, but…
**Billy Zhou** 08:50 Maybe at the top, maybe some… sometimes the error's at the top with the warnings.
**Ariel Demarco** 08:56 Let me… let me see this around. I mean, thermal, like this.
**Billy Zhou** 09:00 Play this?
**Ariel Demarco** 09:02 Oh, yeah.
Exactly, this was the cause, the one that was causing. Okay, great.
**Billy Zhou** 09:10 Do we already have, backwards compatibility in the CodeQL? Because usually, like, CodeQL is, like, a…
Different thing.
So I already have this.
**Ariel Demarco** 09:23 Okay, so this is kind of important to… to do it.
What's the primary compatibility zone? The change from INT to UI income with retain monadony fixed with the result?
Okay.
So, this is the pending thing to do to revert this.
**Billy Zhou** 09:43 Yeah, Bryce here is suggesting to roll forward with a small fix instead of rolling back the bad commit.
**Ariel Demarco** 09:51 We can do, because it's.
**Billy Zhou** 09:53 It's not a… Tabith, yeah.
**Ariel Demarco** 09:57 Okay.
Okay, cool. I agree with that. I think that…
Seems, seem, seems, seem, seems okay.
**Billy Zhou** 10:06 Okay.
Wait, so, with the CodeQL workflow, do we need the backwards compatibility tests?
is, yeah, I didn't actually… usually, CodeQL just does, like.
**Ariel Demarco** 10:21 But I think it…
**Billy Zhou** 10:22 Yeah. Broke, because…
**Ariel Demarco** 10:24 we already merged the PR…
with the new version of 2.0, I think.
2.4, so whenever it updates the package Swift and runs all the tests, it fails.
Because if… while I was looking, it was, like, all the other ones, Didn't really… Worked.
I haven't digged too much details into why it was breaking, to be honest.
But… I don't know what he's checking out.
It shouldn't have… Broken, but, you know.
Yeah.
**Billy Zhou** 11:12 God.
**Ariel Demarco** 11:13 here.
The one that computed was Blue Core.
So…
**Billy Zhou** 11:19 Okay.
**Ariel Demarco** 11:22 Same thing because of that.
But…
**Billy Zhou** 11:24 Okay, yeah.
**Ariel Demarco** 11:25 Okay, I think it'll depend on this, on this revert.
And I also, I think that a 2.4.1 would be worth considering.
we weren't able to release CocoBots because of the problem.
Where this…
Dagon Robins, this one.
This one.
They failed on pushing to CocoBots.
Badly.
So… I think Bryce already did a fix for that, and he already merged it.
Still.
Whenever you have this one.
We've gotten… merge it, and… Release 2.4, 2.1.
**Billy Zhou** 12:12 Okay, do you want to… I also added the, backwards compatibility, tests per platform, do you wanna keep those as well, or…
**Ariel Demarco** 12:22 Backward compatibility to platforms… you mean the… the job?
This one?
**Billy Zhou** 12:29 Yeah, yeah.
Oops.
**Ariel Demarco** 12:33 If it works fine, yes, for sure, why not?
**Billy Zhou** 12:36 Both.
**Ariel Demarco** 12:39 Let me write this down.
New topics?
2.41… He bends… Release.
It depends.
**Billy Zhou** 12:57 Yes, and yeah, sorry, go ahead.
**Vinod Vydier** 13:03 I think if you revert the backward compatibility, it does run boil, correct?
**Billy Zhou** 13:12 What's that we know?
**Vinod Vydier** 13:13 So, when you, when you, reverted it…
Or when you… the last one seems to have… run successfully.
**Billy Zhou** 13:23 Yeah, that's correct.
Yeah, and it'll also work against, like, mainline as well when you merge in.
Yeah.
**Ariel Demarco** 13:37 Whoa.
That's… that's okay.
So this is on Jubilee.
Are you able to do the release, or do you want me to do the 2.4.1?
**Billy Zhou** 13:49 Yeah.
I can do it… today's not a good time for me, because I've, like.
**Ariel Demarco** 13:56 No, no, no worries.
**Billy Zhou** 13:57 Tomorrow, I can… I'm… Totally free.
**Ariel Demarco** 14:01 Yeah, no, no rush. Whenever you…
you have this up to date, just ping us. If you want, you can ping in the…
the open telemetry, Swift, Slack.
And say, hey guys, review this so I can do the release, and that's it.
**Billy Zhou** 14:16 Okay, cool. So we're just doing core release tomorrow?
**Ariel Demarco** 14:20 Whenever, whenever you're available.
**Billy Zhou** 14:23 Okay.
**Ariel Demarco** 14:24 Obviously, I don't wanna, like, rush you, like… You have your own say-so.
Feel free to do whenever you're… you're able to.
Oh, yeah.
Mostly to prevent, breaking other pipelines and all that stuff, like, having this badge will…
Will be good for that.
**Billy Zhou** 14:45 And then, do we have, like, a quick runbook on the… on deployment?
Very, I guess we kind of discussed everything already.
**Ariel Demarco** 14:55 Yeah, yeah, you go to… the actions?
you… Run… Here, framework release.
You run this workflow manually, Ew.
Right here, the… the new SDK, this will raise a new PR.
We'll review it, and whenever that gets merged, it will run this.
These other jobs?
That basically runs the release.
**Billy Zhou** 15:26 Okay. Yeah, I don't think I have permission to do a workflow dispatch.
**Ariel Demarco** 15:31 Oh, really?
**Billy Zhou** 15:32 Yeah.
**Ariel Demarco** 15:33 Oh, okay.
In that case, I can run it myself, no problem.
Whenever you, you merge that.
**Billy Zhou** 15:40 Okay.
**Ariel Demarco** 15:40 the other one.
No worries.
Okay, I'll write this down.
When we merged.
There.
Mentioned. Yeah.
Got it.
Thanks. Bye.
Runs through this.
Performance sucked.
My English is not really working right today.
Okay, great.
This topic is related to nightly bills, or… or something to catch this kind of release.
I didn't know…
Maybe it will be good if we can discuss this whenever we have either Nacho and Bryce.
So, we have a proper process in place, so I'll move this… to discuss… with the whole… We're gone.
maintainers.
I think we've undelightly, to be honest.
But I don't know which would be the best
repository to have this, either on…
OpenTelemetry Core, or the normal OpenTelemetry Swift. Maybe both of them?
So we can have the same issues scattered.
I think daily bills would be a really good idea for this, and also for the cocoa pots issue that we had.
Prior to releasing. Like, whenever we merge stuff and that stuff is not compatible, I think that's…
Also a good idea.
**Billy Zhou** 17:26 It doesn't, the, background scalability tests already catch this, and this is just a different frequency.
Like…
**Ariel Demarco** 17:38 the background compatibility. When does the background compatibility test run?
**Billy Zhou** 17:43 on PR and Merge Domain.
**Ariel Demarco** 17:47 Let me go… go aside.
Okay. Opened and synchronized. Okay.
**Billy Zhou** 17:54 Yeah, we can produce it, but, for now, I just figured maximum coverage.
**Ariel Demarco** 18:02 Okay, I think that… Let me see what I actually do this.
Get release… Check out… Core… Oh, it's a code score, and Swift.
Yeah, I think they should be able to catch this.
Easily.
What is this?
Okay.
I think this… Should cover this.
I know if we can do something to block the release from happening, if this doesn't work.
Or maybe run it on the reduce process. How much… how much time it took? Let me see.
4 minutes.
Probably… maybe it's something we can run as a…
Parallel as a job on the… While running the framework release.
**Billy Zhou** 19:06 Yeah, I can, I can run the, I can improve the caching, I don't know why, but, like, it wasn't, there was all these, like, invalid cache hits that were messing up the workflow. I can try to fix that, and then it'll go down.
**Ariel Demarco** 19:22 In the one that succeeded, or in the one that fails?
**Billy Zhou** 19:27 In between, after I, okay, that is good.
commit, there was all these, like, false, gotcha.
**Ariel Demarco** 19:38 gosh, it's…
**Billy Zhou** 19:38 Let's see.
**Ariel Demarco** 19:40 Let me see one that took long.
Much worse.
Okay, oh.
**Billy Zhou** 19:45 Got it.
Can you look at the commit history as well.
**Ariel Demarco** 19:50 Run action, check out, check out… Here, run action cache.
Okay.
Yeah, the only, the only thing that…
It shouldn't bother, because whenever you…
build, it will try to fetch packages, but they are not cached. Okay.
Yeah, feel free to look at that, but remember that also the cache has a…
a short limit, so I don't think it will be able to cache everything on actions. I don't know if there's a way to increase that. I think that paying more, but I don't know
how much cache, capabilities does it have actions in the OpenTele material?
So, maybe that's the why it's not hitting the cache, because all that thing is not really stored.
**Billy Zhou** 20:53 Yeah, okay, understood.
**Ariel Demarco** 20:56 Let me joke.
Okay.
**Vinod Vydier** 21:03 Yeah, we used to have, problems with our test… tests before.
Some of it.
**Ariel Demarco** 21:09 Would be Lantez.
**Vinod Vydier** 21:10 Yo.
**Ariel Demarco** 21:12 Yeah. Yeah, I remember.
**Vinod Vydier** 21:14 Nope.
**Ariel Demarco** 21:15 It was super slow at some point.
I think it… really improved.
**Vinod Vydier** 21:23 Ew.
**Ariel Demarco** 21:25 Okay, I think we… we can keep talking about this next week.
Let's see… Weird.
Any new topics? If not, we can just go and see if there are new VRs or issues.
Okay.
Let's go back to this.
So… BRs?
So, it's pretty swift.
Or… pull requests… So I think it's only yours.
This one… There were some changes requested by Nacho.
Okay, so I think that…
Imagine if she's up to go and check it out.
Just write it down.
Great.
This is from… Bye-bye.
And this one is your… Oh, yeah, this one is the… the old one, okay.
Let me see if there's any issue… This one…
This one is the one I added for the bot spec.
So it doesn't break.
A, the sync away the APIs for exporters.
Yeah, so nothing really new on OpenSense Telemetry Suite Core.
Let's go to… Open time at your shift.
So we have a bunch of these ones, I think that prior to…
even Bulism, we should go and…
I'll release a new version and see if everything works fine.
We have the Crash Exporter.
**Billy Zhou** 23:54 No, no, I've been in this one.
**Ariel Demarco** 23:57 Okay, no update on these ones.
The same on the other ones, okay. Let's see if there's… there are any new issues?
Okay, this one is the… The one related to the release?
Okay.
Wow.
Did we add an issue on core about this? No.
**Billy Zhou** 24:32 Yeah, but, Bryce took down the 2.4 release, and it failed to publish to Cocoa Pots, so,
There shouldn't be any other impact.
**Ariel Demarco** 24:45 Oh, you removed it?
**Billy Zhou** 24:46 Yeah, so do we want to go to 4.1 again, or.
**Ariel Demarco** 24:53 Yeah, yeah, yeah, for the sake of caches and stuff like that, if somebody in Xcode, for example, already have downloaded the 2.4, like these people, unless they go and manually clean all the sweet package cache, not the one that you have in Xcode, like, manually go and delete everything.
They will still download the previous one.
**Billy Zhou** 25:14 Okay, good point. Yeah, let's just tell them we dug it down then.
**Ariel Demarco** 26:40 Don't remember the words, my name? My words.
Okay, so this is… I'll assign this to myself.
So I remember this?
And this one, it's… Already.
One that we were discussing.
So, nothing else.
The repositories to review.
Okay.
I think that's… that's all. Anything else, guys?
**Vinod Vydier** 27:26 We're good.
**Ariel Demarco** 27:27 Okay, so I'll be waiting for news from you, Billy. Let me know whenever you do the changes that Bryce mentioned, and let's merge the PR and do the release.
**Billy Zhou** 27:38 Okay, yeah, I'll do that right now.
**Ariel Demarco** 27:41 Okay, guys. Thank you so much. See you next week, then.
**Vinod Vydier** 27:45 See ya, bye.
