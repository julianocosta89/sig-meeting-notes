SIG: PHP SIG
Date: 2026-03-04
Duration: 15 minutes
Zoom Recording URL: https://zoom.us/rec/share/zOIk6RyIqSR5842HT8dN9LUfFXXq7iwoTP1pal6Uz9t_xmMEIwouCfz8knmYD7Bk.4uUaUft3n_zCImj_
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 00:13 Hey, Bob.
**Bob Strecansky** 00:14 Chris, how are you?
**Chris Lightfoot-Wild** 00:16 Oh, thanks, sir. How are you?
**Bob Strecansky** 00:18 I, you know.
Another day, another dollar.
**Chris Lightfoot-Wild** 00:25 Awesome.
**Bob Strecansky** 00:30 Are you a big tea drinker?
**Chris Lightfoot-Wild** 00:34 Just got black coffee here.
**Bob Strecansky** 00:37 Nice.
**Chris Lightfoot-Wild** 00:39 Yeah. And, well, our tea is a bit different from yours.
Hmm.
You have sweet tea, usually, don't I?
**Bob Strecansky** 00:47 Well, I love, like.
your kind of tea, but sweet tea is very… a very popular… I think sweet tea is disgusting, but a lot of my peers love it.
**Chris Lightfoot-Wild** 00:58 Yeah, we've tried it when we were over there, it's, like, different.
**Bob Strecansky** 01:02 Yeah, it's too… like, I always get unsweet tea when I go places, because sweet tea is just like… it's like a so… it's, like, worse than a soda to me.
**Chris Lightfoot-Wild** 01:14 Yeah, I don't offer… I don't usually offer tea myself, but if I meant my wife a drink.
and I've had enough coffee in the day, I'll just, like… this is gonna sound cheap, but… because I don't like strong tea, so I'll just use the tea bag myself.
**Bob Strecansky** 01:25 No.
**Chris Lightfoot-Wild** 01:26 Week of tea.
**Bob Strecansky** 01:28 Yeah, that's… the whole, like, tea with milk and sugar thing is also very unusual to me, but… part of your ethos, I feel like.
**Chris Lightfoot-Wild** 01:38 We do it without the sugar bit.
**Bob Strecansky** 01:42 Hmm.
**Chris Lightfoot-Wild** 01:42 And then I did used to have, like, coffee with milk in it as well, but… Cut back on that once, and then once you try it again with milk, it feels really weird.
**Bob Strecansky** 01:53 read.
Very… I very much agree. I… I went… I did, like, the whole cold turkey, no… nothing in my coffee except for black for a while, and then you can't… it's… I'll still drink… I'll drink a latte occasionally, but, like, I'd much rather have it black, especially if it's just beans and water.
**Chris Lightfoot-Wild** 02:16 It feels like we've got a similar taste on our, beverages, though.
**Bob Strecansky** 02:21 Yeah, that's true.
Seems like it.
**Chris Lightfoot-Wild** 02:25 I don't know if you're quite… you seem like quite a Europeanized kind of, palette there, with that kind of thing.
**Bob Strecansky** 02:32 I think… the right way for me to describe it is I have a, I have, like, a very, opinionated palate, but I will eat anything.
If that makes any sense. Like, I know what I like, and I'm very opinionated on what I eat and drink, but I'm also happy to just do whatever.
We may be the only ones here today, Chris, that'd be nice.
**Chris Lightfoot-Wild** 02:59 I was just… yeah, I was wondering if… So yeah, probably fun.
**Bob Strecansky** 03:06 Maybe they're busy finishing the distro.
**Chris Lightfoot-Wild** 03:11 Are you anonymous elephant?
**Bob Strecansky** 03:14 I assume so, I should be… I have it open with my profile in it.
Maybe you're anonymous… anonymous… anonymous gopher?
**Chris Lightfoot-Wild** 03:26 Oh, my… am I showing up as anonymous?
You're showing up as an anonymous gopher, yeah. Or you were.
**Bob Strecansky** 03:31 That disappeared.
**Chris Lightfoot-Wild** 03:32 Let me sign in, I'll just…
**Bob Strecansky** 03:34 Okay, this is meant to be anonymous. Have you read anything about the, the whole Linux with age… with, age ID verification thing yet?
**Chris Lightfoot-Wild** 03:46 No, it's our joke.
**Bob Strecansky** 03:47 No, it's real.
They're like… so, California is… like, try… attempting to mandate operating systems have some sort of age ID verification, and… and ubuntu said that they will probably comply with it, which has been, like, a big thing.
**Chris Lightfoot-Wild** 04:08 No.
**Bob Strecansky** 04:09 I still have to switch distros at some point. I know, right? That's… it's… that seems… rash, but I… that was my first thought, too.
Good hell.
**Pawel Filipczak** 04:20 Hi, guys.
**Bob Strecansky** 04:21 How are ya?
**Pawel Filipczak** 04:24 Oh, I'm okay, sorry for being late. How are you guys?
**Bob Strecansky** 04:28 Pretty good.
**Pawel Filipczak** 04:30 Good to hear that.
**Bob Strecansky** 04:31 We were just talking about, have you heard the, the whole… age ID verification thing with Linux yet?
**Pawel Filipczak** 04:40 No.
**Bob Strecansky** 04:42 California's, like, trying to pass laws where operating systems are required to have age identification.
And that, like.
both Microsoft and Mac were like, yep, yep, yep, yep, yep, and Google, and then Linux has obviously been very much against that, but Ubuntu talked about complying, so it's just been a very interesting saga to watch.
Alright, let's… Let's get rocking, because I have… I have to leave at half past the hour, so we want to make sure that we leave enough time for everybody today.
Make sure my Safari window… One second… Gotta hide all the mission-critical things?
Y'all can see my Safari window.
**Chris Lightfoot-Wild** 05:30 Yep.
**Bob Strecansky** 05:31 Chris, you wanna talk about suppressing instrumentation?
**Chris Lightfoot-Wild** 05:35 Yeah, I'll probably follow up with a, like, a Slack thread, maybe, in the hotel, PHP, or instrumentation, maybe with… to get the best eyes on it, or, thoughts.
Or a GitHub issue, whichever.
So on the… for the Laravel instrumentation.
I'd like to be able to… At certain points, turn off all… instrumentation and turn it back on again. So, like, I've got to capture a unit of work.
At the moment, there's some, like, old, Issues that people have raised, where you get very long-running traces.
So, like, if you're doing, like, job processing, the sort of distant parent kind of exists from outside of the unit of work, where the queue worker ends up checking a cache, and that starts a trace.
And then, like, you start then the job processing, and it inherits that trace from… kind of outside the scope that I want.
So, I don't know if I'm misunderstanding how this should tie together, but I know there's something called a configurator.
And I've seen some examples of… I've done tests.
But it looks like, the instrumentation gets a context with, like, a late binding Series of providers that… I couldn't get to disable. I want to be able to just turn it on and off and say, right, I want to start capturing data again.
And then get rid of all the sort of cruft that happens outside of that context.
**Bob Strecansky** 07:12 I don't.
**Chris Lightfoot-Wild** 07:13 I'm making any sense, or I'm misunderstanding it, or it sounds… Vaguely.
Familiar to some other scenario with a cattle before.
Hub.
**Bob Strecansky** 07:27 Yeah, I'm trying…
**Chris Lightfoot-Wild** 07:28 guidance on this. Very vague point.
**Bob Strecansky** 07:30 Yeah, I'm trying to think if I… Seen anybody ask about explicitly turning it off and then turning it back on again.
I don't think I can think of that off the… but I know that… I know that this is a problem with long-running jobs. I've talked about this in the maintainers meeting more than once, too, so, I do think it's… I do think it's not just a U problem, and I do think the instrumentation channel is probably the best place to ask about it. I think that there will be a lot of… a lot of the spec maintainers that will have good insight there, because there may be… I'm… If I'm… Don't quote me on this, I feel like there was an OTEP around this.
**Chris Lightfoot-Wild** 08:08 Okay.
**Bob Strecansky** 08:09 Oh, I might search for that.
**Chris Lightfoot-Wild** 08:11 Yeah, just, there was a PR in Contra at the moment for some Laravel functionality that… I was trying to avoid getting merged in, because I want my SBI stuff to go in, and, It introduced, like, a bunch of variables to basically short-circuit Hooking the methods in the first place?
**Bob Strecansky** 08:30 Mmm, okay.
**Chris Lightfoot-Wild** 08:31 Like, a per request.
Model, that means, yeah, that code just won't run, so therefore isn't a problem.
But it seemed like kind of the wrong way to do it. But that could just be my misunderstanding.
But yeah, obviously, the declarative config, and if we turn it off, do it via that instead.
But then disable or enable As and when we need to.
M.
**Bob Strecansky** 08:58 Yeah, it's all… it's like… I understand your plight, though, because it's like, you're essentially… you want manual instrumentation in certain spots and auto-instrumentation in other spots, almost.
**Pawel Filipczak** 09:11 Maybe some kind of filtering, you know, implement some filters, and let's say, skip implementation on some particular routes in the On the paths, or in the larva?
But, how to instrument others, right? So, some exclude list.
**Chris Lightfoot-Wild** 09:31 Yeah, and there is some functionality in the base SDK, I think, isn't there already, for that?
But when you're then doing, like, any job with a CLI, it becomes more problematic. I think that's what people have… Other people have stumbled into as well.
I don't think it's an issue on… yeah.
But it does… it does make sense to include that functionality as well, to strip out certain routes, I'd like to account for that in the request processing as well.
Sorry, I appreciate that. It was a very vague, throw it out in the air and see if anything lands kind of thing, and I'll maybe stick it in the channel or GitHub issue.
And see if, you know, someone else can chime in.
**Bob Strecansky** 10:22 Yeah, I'm sure you'll get… I'm sure you'll get tons of feedback on that one. That seems like a very practical use case that a lot of people might be interested in.
**Chris Lightfoot-Wild** 10:32 Thank you.
**Pawel Filipczak** 10:35 small update from me. So, last week, I was working on some small bug fixes, and I… Wrote a documentation.
So, there is a README, and there is a docs folder with the documentation. I also reviewed the development guide.
So, now I'm working on the release workflow, and… and that's it. So, yeah, hopefully soon we'll… We'll make a release, and… And, yep, if you would like to test it, then… Then… you can fetch the artifacts, I mean, the Debian, RPM, or APK package from one of the GitHub actions.
and built, but in… if you would like, and you have some troubles, then let me know, and I will help you.
**Bob Strecansky** 11:29 Do you have a link? Do you have a link for that, Paula? I want to make sure that I include that here.
**Pawel Filipczak** 11:32 I'm not sure, I will… I will send it to you on the chat, but… or I will paste it into the docs, but I'm not sure if it will work from… to the others. I… I'm not sure how the… how the… those links are working for… not maintainers, I'm not sure if you are added to the repository as a maintainer or not, so yeah.
**Bob Strecansky** 12:00 Okay.
**Pawel Filipczak** 12:01 Please just try it, and if not… if it's not working, then please let me know, okay?
**Bob Strecansky** 12:07 Sure, yeah.
**Pawel Filipczak** 12:13 Over 18 sections.
Sack… I'm putting click to the build on the… on the chart.
**Bob Strecansky** 12:40 Oop.
**Pawel Filipczak** 12:41 On the bottom, there is a… Just above the summary, there is an artifact tab.
Yeah.
Please try to download the artifacts from the build, maybe… We'll… we'll then see if it… if it's available for you or not, so… The… the name of the package is… maybe I will just put a link to the… to the artifact. This is the… for the x86.
**Bob Strecansky** 13:12 Yes.
Let's see it here.
**Chris Lightfoot-Wild** 13:16 I just managed to download one.
**Pawel Filipczak** 13:18 Yes, it's packages, it's for, Linux.
**Bob Strecansky** 13:22 booths.
**Pawel Filipczak** 13:23 the file is called Packages minus Linux, or Linux Mosul, so it depends on the architecture, so…
**Bob Strecansky** 13:32 Love it.
**Pawel Filipczak** 13:33 Yep, yep, yep.
Okay, so it looks like it works for you. Great.
**Bob Strecansky** 13:45 I am able to bitch it.
**Pawel Filipczak** 13:52 Cool.
**Bob Strecansky** 13:54 Excellent.
One second, my headphones are dying, I gotta switch.
**Pawel Filipczak** 14:14 So, okay, so that's all for me.
I hope next week, I will… Share more details.
And I guess if you will find some time, please let me know how it works for you.
**Bob Strecansky** 14:27 Y'all can hear me now?
**Chris Lightfoot-Wild** 14:29 You're good.
**Bob Strecansky** 14:30 Nice.
**Chris Lightfoot-Wild** 14:32 You know, travel for that.
**Bob Strecansky** 14:34 Yeah, thank you, pal. Appreciate your work… your hard work on that.
**Pawel Filipczak** 14:38 Thank you.
Okay, that's… that's our proof.
**Bob Strecansky** 14:44 Alright, let's go over the… Sleep those real quick, and then we'll call it a day.
Couple Renovate PRs that I gotta merge.
Probably a couple more APRs that I gotta merge.
Yep.
I'll do that today.
And then… same in here… wonderful. Alright, I will take care of that this week, and we can move forward. I opened a thread talking about, auto-merging those renovate PRs, and I got a whole lot of nothing burgers, so maybe I'll have to follow back up with that again, too.
Alright, thanks, y'all, we'll see y'all next week.
**Chris Lightfoot-Wild** 15:30 We don't see that?
