SIG: PHP SIG
Date: 2026-03-25
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Pawel Filipczak** 04:38 Hey, Chris.
**Chris Lightfoot-Wild** 04:41 Hey, how you doing?
**Pawel Filipczak** 04:43 I'm okay.
How are you?
**Chris Lightfoot-Wild** 04:45 I'm alright, thanks, yeah.
Wasn't sure if I've messed up the timing again because of the daylight savings.
**Pawel Filipczak** 04:52 Yeah.
**Chris Lightfoot-Wild** 04:53 You're the only one here, I was just waiting around.
Glad someone else's here.
**Pawel Filipczak** 04:57 I miss… I missed meeting two weeks ago, so…
**Chris Lightfoot-Wild** 05:00 That was the same, yeah. I think next week, for… well, for us, the clocks change on Saturday.
**Pawel Filipczak** 05:06 Yeah, same, same here.
**Chris Lightfoot-Wild** 05:07 Oh, nice. Yeah, so next week, back to normal program.
**Pawel Filipczak** 05:11 Yeah, I'm gonna be… a longer day, I mean, brighter during the evening, so yeah, I'm waiting for that.
**Chris Lightfoot-Wild** 05:20 Yeah, it's getting… it's quite bright in the mornings as well, which is nice.
**Pawel Filipczak** 05:24 Yeah.
**Chris Lightfoot-Wild** 05:27 Still cold, though.
**Pawel Filipczak** 05:29 Yes, is… is it called?
**Chris Lightfoot-Wild** 05:31 Yeah, we had a, well, it's only a few degrees, it's in the single digits, but we, we had a bit of snow that didn't stick.
**Pawel Filipczak** 05:38 Wow, wow.
Here is, here is the… it is single.
This is… but it was… 15, up to 15, a few days ago, so… but only for a few days, maybe 2 or 3 days, so…
**Chris Lightfoot-Wild** 05:54 Last… last week, we did have that, I think on Wednesday and Thursday, we had some, like, abnormally warmer days. Dropped down again, so…
**Pawel Filipczak** 06:03 Whoa, whoa.
I'm waiting for the summer.
**Chris Lightfoot-Wild** 06:07 No, me too, yeah.
**Pawel Filipczak** 06:10 Winter was quite difficult here this year, so maybe… Maybe summer will be… will make summer, you know, different for us, and it will be nice for… We'll see.
**Chris Lightfoot-Wild** 06:25 Being supposed to. Yeah, we're a lot milder, yeah, so we don't really get any extremes, but… Yeah.
Hey, Bob.
**Bob Strecansky** 06:34 Morning, y'all. How are you?
**Pawel Filipczak** 06:37 Good.
**Bob Strecansky** 06:39 Not bad.
I'll pull up our… What are missing.
Talk through it.
**Chris Lightfoot-Wild** 06:50 We're in some different surroundings.
**Bob Strecansky** 06:52 Yeah, I, I had tennis practice this morning, you can see I'm still in my tennis clothes, and I just, like, walked into my office and took the first available space because I was running a little bit late, because Atlanta traffic is… Very, very bad.
Yeah, I'll get to see me in my natural element, I guess.
**Chris Lightfoot-Wild** 07:16 I'll turn this attire.
**Bob Strecansky** 07:18 Yeah, I have my tennis kit on now.
6am is an early practice, but it's, it's always fun.
Let's get rolling here… yesterday… Agenda… Alright, I have a good agenda to talk about. I'm planning on doing a release today.
We haven't done one in a while. I hadn't… I had not ever done one with the get split piece, so I spent some time talking with Brett, who is not very responsive on paternity leave, and they should not be, so it took a little while to get some insight for him.
Finally got some, so I should be able to do that release today. That's my plan anyway. I'll let… I'll post to the channel if there's anything that, That comes up, but I think it should be alright.
**Chris Lightfoot-Wild** 08:13 What, what are you… what were you planning to release? Which, what… SDK, everything, what's the…
**Bob Strecansky** 08:19 Yeah, new, yeah, new minor versions, or none of the 2.0 stuff, but just all of the, like, a new major version, because… or a new… I'm sorry, a new modern version, because… Andre asked for it for his work, and it made me realize, like, yeah, we haven't done a release in quite a little bit, so we probably need to.
**Chris Lightfoot-Wild** 08:38 Nice. So you're doing, both repos, then? Like, contrive as well?
**Bob Strecansky** 08:42 Yeah, there's, let's see if I can sh… if I can share it with y'all, I think I can.
Bear… I'm shooting, let's see.
Where are you? Not this one.
**Chris Lightfoot-Wild** 08:58 There's, like, a release tools repo, and it opens on the.
**Bob Strecansky** 09:01 Yeah, I'm looking forward. It's, you know, it's OpenTelemetry, HP.
What is it? Open T, L-E-M-E-T-R-Y-P-H-P… Or is it… is OTL CHP?
**Chris Lightfoot-Wild** 09:16 No, you had it, you were just missing an E.
**Bob Strecansky** 09:18 Oh.
Bentel line, lip tree, HQ.
Yeah, and there's, there is a… I don't know if I'm… Like that.
This'll be easier.
**Chris Lightfoot-Wild** 09:36 Oop.
**Bob Strecansky** 09:37 We have tools.
**Chris Lightfoot-Wild** 09:39 I've just got, like, a weird… Oh, there it is.
**Bob Strecansky** 09:43 I need to bookmark that, but… So there is a release tool in here, and I'll be following this today, just to check it out, but I think we should be… It seems like it's pretty well documented, but… If I get stuck, I will abort.
**Chris Lightfoot-Wild** 09:59 Good luck.
**Bob Strecansky** 10:01 Thanks.
Paul, you got, first OpenTelemetry PHP distro release.
**Pawel Filipczak** 10:08 Yeah, two days ago, I, I made that. So, yeah. The first stock, first series, and… Let's say it's… it's not marker like a stable, it's… Some kind of technical preview, so it's easier to… To fetch the artifacts and just install and test, so if you have some time, please do that, and share the feedback.
**Bob Strecansky** 10:33 Got it.
**Pawel Filipczak** 10:34 Did you try.
**Bob Strecansky** 10:35 Did you try this… did you try this with the demo? Yep. That might be a good place for you to try it out.
**Pawel Filipczak** 10:41 Demo, I mean, you mean demo applications? OpenTrabatic demos? No, I never tried it. I have to… I have to test it, yeah.
**Bob Strecansky** 10:50 It's… I think it's relatively straightforward.
**Pawel Filipczak** 10:57 Oh, you know, my first attempt was a few years ago. It wasn't easy back then, but maybe something changed, yeah.
**Bob Strecansky** 11:04 Yeah, so there is a demo here, and I know that there's, Why can't I never remember the…
**Pawel Filipczak** 11:11 I would dry it. I would try it, yeah, yeah, okay.
**Bob Strecansky** 11:15 Yeah, the quote… the quote service is probably our best… that's probably our best, like, publicly exposed thing that has, That would give you a good place to give it a rip. So I'll put that in the, document here.
**Pawel Filipczak** 11:41 Yep, yep.
So, so far, I tested it manually with my scripts and with WordPress.
And we fly this aim was a lot of random applications, I mean, this web… webshop.
So, it's working. It's not, not, not, not clashing, and… yeah.
Now we are working on the shadowing, so… It will be in the second release, I guess, so…
**Bob Strecansky** 12:09 What are you… what are you working on? I didn't catch that.
**Pawel Filipczak** 12:11 shadowing, I mean, dependency, the shadowing. So, we will use the PHP scoper tool during the build, and it will put everything into the additional scope, so it will… it will… it will not, collide with any dependencies bring by third-party or open telemetry components, so… it should be transparent to the application. So even if you have something loaded, I mean, the SDK API, whatever, manual instrumentation in your application, then it should work.
together. Now, if there is some version mismatch.
Let's say it may lead to an undefined behavior, because the distro classes will be loaded first.
So, we have the POC, it's working.
I mean, this shadowing, or scoping?
Whatever you can call that, and… I hope soon it will be ready.
For testing, so, yeah.
And I think that the code service, it's a good application to test it with.
**Bob Strecansky** 13:24 Cool.
**Pawel Filipczak** 13:25 Yep.
So, that's all from our site.
**Bob Strecansky** 13:30 I just have another one. Chris, thank you for your help with fixing that, like, doing that revert, that song and, fan error was annoying. It interrupted people, and thanks for the help. I think that… that will probably make me fast-forward the Mega work a little bit, because I think the faster we can pull out these older things.
The faster, the better off we're gonna be. I'm gonna leave it as it is for now, and then when, Renovate runs next time, we'll probably see if there's a dependency, and we'll have to watch that, but that's okay.
**Chris Lightfoot-Wild** 14:09 Cool, I've seen you've got another PR as well for removing fan.
**Bob Strecansky** 14:15 Yeah, I created that just so, like… see what kind of… what level of effort it would take. I don't know that I'm… how do I say that the right? I don't know that I'm ready to do that yet, but I think that.
**Chris Lightfoot-Wild** 14:29 Well, as I've maybe threatened last week, I'll try and do it in the live one first, if you want me to, like… No.
**Bob Strecansky** 14:35 Yeah, that…
**Chris Lightfoot-Wild** 14:35 Example instrumentation that does it, and see how it goes.
**Bob Strecansky** 14:39 Yep.
Clw… We'll try… Big fan… And, Sarabelle is to see what happens.
Okay.
I'm thinking, do we have any? I don't think I have anything else.
On the agenda right now.
So, we can walk the board real quick and then adjourn.
Owls.
Wait, oops, there I go.
Oh, yeah.
**Chris Lightfoot-Wild** 15:23 I wasn't here from Nevo, wasn't there, as well?
**Bob Strecansky** 15:25 Yeah, there was.
And Jerry was talking with Nive about this, span suppression strategy. Did you see… are you watching that thread?
**Chris Lightfoot-Wild** 15:35 Yeah, well, you mean just in GitHub? Because I've seen it there, I don't know if it's somewhere else.
**Bob Strecansky** 15:39 Oh, no, there's a Slack thread that, I'll… hold on, let me post, let me, copy and paste it.
**Chris Lightfoot-Wild** 15:45 Oh, on our hotel PHP channel.
**Bob Strecansky** 15:48 Yeah.
There's one… there's one where Gary Lang is talking about recursion instrumentation.
I'll post it, wow.
**Chris Lightfoot-Wild** 15:57 Well, this one, from Friday the 20th.
**Bob Strecansky** 16:00 So I'm just gonna post them in here so that we have them.
Then there's this one for, tracing asynchronous jobs. That one I think you're involved in, right?
**Chris Lightfoot-Wild** 16:29 Yes, yeah.
**Bob Strecansky** 16:30 Mute.
**Chris Lightfoot-Wild** 16:36 Which was awesome as well, because that's something at work where I realized, perhaps, we need to split some of the longer-running things, and then someone's done it, which is awesome.
**Bob Strecansky** 16:46 Hell yeah, nothing better when somebody does the work for you.
Cool. Alright, well then let's go back and look.
Yes.
**Chris Lightfoot-Wild** 16:56 Also, I think that span suppression thing is… is that a way to prevent all spans being created, so it's, like, no op, and you can turn it off and on again?
**Bob Strecansky** 17:05 Yeah, I think…
**Chris Lightfoot-Wild** 17:06 what I was asking about the other week, the larva.
**Bob Strecansky** 17:09 You were.
**Chris Lightfoot-Wild** 17:10 Whoa.
**Bob Strecansky** 17:10 You were asking about that, that's true, maybe… Maybe you and this person need to, like, be buddy-buddy now.
**Chris Lightfoot-Wild** 17:17 Yeah, absolutely.
**Bob Strecansky** 17:20 Anywho, alright, we will, I'm probably gonna clean this up at some point this week, the Mago PR, because I don't want this to report failure, because that's confusing. But besides that, I think it'll be ready to go. I'll tag you when that's ready, Chris.
**Chris Lightfoot-Wild** 17:37 Cool. Well, I'd seen you actually had one, the post you did last week for Margot said one sort of interaction so far, isn't it? I don't know if it's… We'll see you.
A little bit longer, too.
**Bob Strecansky** 17:50 Yeah, this is it. You're talking about… this.
**Chris Lightfoot-Wild** 17:55 So you posted on Slack last week, and some… someone's responded to it?
**Bob Strecansky** 18:00 Oh, yeah, yeah, somebody said that they're using it. One person is probably not enough, but I still want to run this in parallel.
**Chris Lightfoot-Wild** 18:06 I thought, given that I was in the meeting, I didn't want to just jump on it and be like… just see who else would… No piloting on it.
**Bob Strecansky** 18:16 I don't think many people are watching that channel, so there's probably not a lot of signal. I wonder where the right place to ask that would be, maybe the PHP Discord?
Not sure.
Alright, let's see, so, put back on… And then… trip out… Couple little things… Yeah, I can fix those later.
Transientation, probably just has some renovate PRs, yep.
Alright, well, we'll review those later this week.
Y'all have anything else on the… on the docket?
**Chris Lightfoot-Wild** 19:03 That's written.
**Bob Strecansky** 19:05 Sounds good. Alright, we'll catch y'all on the internet.
**Chris Lightfoot-Wild** 19:08 Cheers.
