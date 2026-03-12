SIG: PHP SIG
Date: 2026-01-14
Duration: 16 minutes
============================================================

## Zoom Recording Transcript

**Bob Strecansky** 01:30 gross.
**Chris Lightfoot-Wild** 01:34 Hey, Will, you alright?
**Bob Strecansky** 01:37 Doing alright, how about you?
**Chris Lightfoot-Wild** 01:39 Yeah, I'm okay, thank you, yeah.
Sat warming myself under a little blanket, like an old man. Freezing it.
**Bob Strecansky** 01:48 Oh, is it? It's… it's been cold here, and it's gonna get very cold this weekend.
**Chris Lightfoot-Wild** 01:53 Well, I think cold there is probably usually colder than here, isn't it? We had a bit of snow the other day, but it's melted now, but…
**Bob Strecansky** 02:01 Ugh.
**Chris Lightfoot-Wild** 02:01 No, we don't get snow.
Oh, okay.
**Bob Strecansky** 02:05 I bet.
**Chris Lightfoot-Wild** 02:06 Hey, Bo.
**Bob Strecansky** 02:10 Yeah, no snow for us.
**Pawel Filipczak** 02:12 It happens a lot.
I have a lot of stuff.
**Bob Strecansky** 02:16 Do you?
**Pawel Filipczak** 02:17 Yeah.
It's a…
**Chris Lightfoot-Wild** 02:18 There's a lot of snow.
**Pawel Filipczak** 02:20 Yeah, half matter, about half matter of snow.
**Bob Strecansky** 02:24 That's neater.
**Pawel Filipczak** 02:25 Today, today, you know, actually today, it's… it's crazy. The weather is changing, so it's going… the temperature is going up, so it's about minus 2.
And… and on the upper levels, it's… it's hotter, and there is… it's raining today, so it's rain, and every… and it… when it hits the ground, it starts to… to be frozen, so everything is covered with the ice.
Everything, you know, trees, cars, roads, everything is covered with ice, so it's… It's hard to walk outside.
**Chris Lightfoot-Wild** 03:04 Sounds fun.
**Pawel Filipczak** 03:07 Yeah.
I was driving today, and it was, you know, very fun, too.
I was waiting a bit to get rid of that ice from my car.
**Bob Strecansky** 03:24 Let's see… yeah, I'm going… I'm going to a friend's bachelor party this weekend, and the low is 13 degrees, so that's like… It's 13 Celsius, I'm trying to think. I don't do well with the negative numbers.
**Chris Lightfoot-Wild** 03:40 The 13 Fahrenheit?
Yeah. Well, because 30… 34 is zero, isn't it?
**Bob Strecansky** 03:46 Yeah, it'd be minus 10.
on Monday for us.
**Pawel Filipczak** 03:50 Hmm.
**Bob Strecansky** 03:51 Too cold. Don't like it.
**Chris Lightfoot-Wild** 03:54 We're cooler than we are.
**Bob Strecansky** 03:56 Way colder than the air.
Alright, well, let's get rockin'. I don't have a ton to talk about today, let's see… There's the three of us going.
Today's the 14th.
Can you all stream my screen, okay?
**Chris Lightfoot-Wild** 04:22 Yep.
**Bob Strecansky** 04:25 Alright, and this is Chrisley for a while, let me copy your name.
Agenda… I'm keeping my same agenda topic, because I have not had a chance to turn off Dependabot. I think that I have to go and open a ticket with somebody, because we don't have access to that anymore.
So I got back on.
Kyle, how are things going with the distribution?
**Pawel Filipczak** 05:02 So… Maybe, maybe, like, I'll share the window, let me…
**Bob Strecansky** 05:05 Oh, sure. For one second, I can show you, so… live demos.
**Pawel Filipczak** 05:12 Yeah.
It's always step-by-style.
Walk towards my window.
**Chris Lightfoot-Wild** 05:23 I guess that's why.
**Pawel Filipczak** 05:26 Okay, I'll change the size. Can you see it?
**Bob Strecansky** 05:29 Yes, we can.
**Pawel Filipczak** 05:32 Oh, now it's bigger for you, right?
**Bob Strecansky** 05:35 It looks good, yeah.
**Pawel Filipczak** 05:36 Yeah, you're so… Actually, the… This is the… I'm… now I'm working on, removing dependencies for the elastic… Elastic, Docker… Images, which we are using to build the native parts.
So, I'm preparing the build, and… which will push the… the built images to the Docker Hub in the OpenTelemetry namespace.
So, it's taking a bit of time to build, but it will only trigger if someone will change the images, the Docker files.
And, I have some issues with bidding on ARM. I successfully enabled the ARM runner, so we have available arm runners, but they are based on the Oracle system, and it's a bit out of date, and I have some issues with with running CMake on… on… inside the docker, on the master, so I have to figure out what's going on. Most probably, I will set up today the VM on ARM.
So we have some… some resources in our company, so we can do that, then I will… I will investigate it faster.
But anyway, going back to top, to the OpenTelemetry distro, so… everything is almost done. So, I pushed the native part, I pushed the PHP part, responsible for the instrumentation.
and it builds, it produces the packages, but it does… I didn't do any release, because we have to… contribute the tests?
Which are testing the installation and how the agent behaves with the… in the real-world applications, or let's say it's a bit of real-world app tests.
So we want to contribute that.
Let's say that it's almost end-to-end test.
And, and that's it, so… It's very close to… to finish.
And I would like to make a first release end of February.
Maybe beginning of the March, who knows?
It depends, because next week I'm on vacation, so it slows down at work a bit, and the Christmas time, it slows down me a bit.
And, yeah, maybe I can show you some of the… some successful builds from the past. So, yep, here.
We have a successful build, so it passes. We are testing with the PHPT tests.
So we are testing two extensions. One is the agent extension, the second one is the Artificial extension, which is testing the layer which is responsible for the communication with the PHP engine.
And, yep, we are also running the OpenTelemetry tests from the country repository.
So, if we are including some contract package into the distro, then we are running executing tests.
From the… from the conflict?
together with the agent installed, so not… it's not running in the PHP unit with the… with the classic extension, but it's running with the full instrumentation based on the… on… on… on this distro, so automatic instrumentation.
The tests are not passing, because they are flaky, and they are not passing… not all of the tests are passing on the… in the contributor, so we have to clean it up.
And, give me one second, I have the results in the summary, but… I'm not… I don't know why I can't scroll it down.
Oh, here I can.
So, this is the test summary for, for the PHP 8.1, because the destroyer supports the PHPA.1 too.
For all of the supported versions, we have the results, so they are a bit different between the versions, but yeah.
Not, not all of the tests are passing, and, and, We have to figure out why, but… I tested it manually, and there, mostly because of the flakiness of the test, and some… let's say, minor issues in the test, but not in the instrumentation itself.
So, yeah, those tests are not breaking the build, they are just for… Checking the regression, and so on.
So, that's it from me, and of course, you can download the packages from the build.
So it's still not released, but if someone wants to test it, then the packages are here in the… for the x86 and for the ARM architecture.
And also for the, Alpine Linux, they are available here in the, in the second repository, Arctic. So… This is how it… How it looks.
Today.
**Chris Lightfoot-Wild** 11:09 Awesome.
**Bob Strecansky** 11:09 Excellent, excellent progress.
**Pawel Filipczak** 11:12 Yeah.
**Bob Strecansky** 11:12 Thank you for all your hard work. I know that must have not been easy.
**Pawel Filipczak** 11:16 Huh.
You know, almost 95% was easy, but… Those 5% hours blocking you for hours.
**Bob Strecansky** 11:27 Yes, and…
**Pawel Filipczak** 11:28 4 hours, you know, trying to figure out some small issue, it was so basic mistake, and it happens.
**Bob Strecansky** 11:37 It's sort of like moving… it's sort of like moving, too. The last 5% always takes just as long as the first 95%.
**Pawel Filipczak** 11:43 Yeah.
**Bob Strecansky** 11:45 Cool.
Alright, Chris, did you have anything you wanted to bring up, or we can walk through the repos real quick?
**Chris Lightfoot-Wild** 11:53 No, I didn't reach out to Sergey. We mentioned last week we were gonna maybe have a catch-up. I don't know if he's, around this week, Paul, if you know, but I might reach out to him and…
**Pawel Filipczak** 12:05 No, no, he's… he's off from the beginning of the week, so I… I don't have any, you know, news from him.
**Chris Lightfoot-Wild** 12:13 He's off this week, okay.
**Pawel Filipczak** 12:14 Yeah, yep, yep.
**Chris Lightfoot-Wild** 12:16 Cool.
**Bob Strecansky** 12:16 Well, you didn't tell us. What are you doing with your vacation? Anything exciting?
**Pawel Filipczak** 12:20 So, I'm going to Italy tomorrow, for a few days.
**Chris Lightfoot-Wild** 12:24 Yeah, yeah. There'll be no snow there, I'm sure.
**Pawel Filipczak** 12:27 Oh, did I… Who knows, but now.
**Chris Lightfoot-Wild** 12:31 Boomer.
**Pawel Filipczak** 12:31 Around 15 degrees Celsius, so it's quite okay. It's a bit rainy, but yeah.
**Bob Strecansky** 12:39 I think they'll still have pizza and espresso, regardless of rain or snow.
**Pawel Filipczak** 12:43 Yeah, I've enjoyed the Italian food and, you know… So…
**Bob Strecansky** 12:50 I thought…
**Pawel Filipczak** 12:51 It won't be rainy, so… but anyway, even if it will be then, it's easier to, you know, visit some of these fancy places, because during the winter, it's not so heavy crowded.
**Bob Strecansky** 13:05 Yeah, that's true. The place where I'm going this weekend… I always love telling non-Americans this one, because they just, like, always laugh at it. Nashville is very famous for something called chicken and waffles. Have you all… are you familiar with this?
So that we'll take… So chicken and waffles, pal, is a dish that you can get. It's mostly a Southeastern cuisine, and it's, like, a waffle with a piece of fried chicken on top of it, and then syrup on top of that.
It's, like, one of the most… it's like one of the most American things I could possibly think of. It's real good. It tastes so good. You wouldn't expect it to taste good, but…
**Pawel Filipczak** 13:45 So, yeah, next time, in, in States, I will order it.
And try.
**Bob Strecansky** 13:50 Yeah, you need to… you definitely need to, it's very good. Alright, so let's see if there's anything exciting in our pull request. I need to review this Symphony support. I'm gonna put that in my queue.
And this one got approved, but it has a red X, so we'll see what's going on here.
Unrelated thing.
**Chris Lightfoot-Wild** 14:11 I've got another one as well that is a similar boat, where Brett's maybe reviewed, but I'm not sure if he's been around much recently, and if it's worth, like, trying to ping him. I don't want to interrupt.
**Bob Strecansky** 14:21 Yeah, do you have a specific thing that you're looking at, Chris? I'm always happy to help.
**Chris Lightfoot-Wild** 14:25 That one that's right at the bottom, disable SDK.
**Bob Strecansky** 14:29 Disable SDK.
**Chris Lightfoot-Wild** 14:32 But the…
**Bob Strecansky** 14:33 That one.
**Chris Lightfoot-Wild** 14:34 That's it.
I reviewed it, and then I made some changes after holiday, but there was a bit of a lag as I was away.
**Bob Strecansky** 14:41 Understood.
**Chris Lightfoot-Wild** 14:42 So…
**Bob Strecansky** 14:43 Good.
**Chris Lightfoot-Wild** 14:43 Just wondered if I don't mind pinging Brett, but I don't want to equally…
**Bob Strecansky** 14:47 Yeah, I think you can… I think you can message him if you want to, because he doesn't have to respond.
**Chris Lightfoot-Wild** 14:52 Yeah, absolutely.
**Bob Strecansky** 14:54 So, yeah, I wouldn't hesitate to message him if he responds, that's great. If not, I'm happy to help push it along.
**Chris Lightfoot-Wild** 15:02 I'll ping him on Slack or something, and then, you know, in a week or so, if not heard anything back, maybe we could… you could look at it for me.
**Bob Strecansky** 15:10 Sure, no problem, happy to do it.
**Chris Lightfoot-Wild** 15:12 Thank you.
**Bob Strecansky** 15:12 And these… and these mostly look like… Same thing… rings.
Instrumentation just has a lot of the same thing. Cool. Alright, I will… I'm excited to get, I'm excited to get that dependent bot thing out. I'm gonna try to get that done today, because I really have just been procrastinating opening this ticket, because I don't want to, but I will.
**Chris Lightfoot-Wild** 15:39 Did we look at new issues, then? Sorry, was there any… has anyone raised an issue on that?
**Bob Strecansky** 15:44 You know, my man puck.
**Chris Lightfoot-Wild** 15:46 You might have to… I didn't see, sorry, I wasn't…
**Bob Strecansky** 15:49 I don't… I think… I think I just skipped it.
Let's see… Zend interim heap corrupted with using span hook.
**Chris Lightfoot-Wild** 16:00 Oh, I think I'd actually seen this one and, like, buried my head, because I'm not sure anything about… this.
**Bob Strecansky** 16:09 Looks like Brett responded.
Okay, so a little latency.
Alright.
Good enough.
Okay, well, That's all for today. We'll see you all on the internet. Paul, we'll see you in two weeks, I guess. Enjoy your vacation. Have an espresso for me.
**Chris Lightfoot-Wild** 16:36 Did you have a great time.
**Pawel Filipczak** 16:37 Thank you, guys, and see you. Bye-bye.
**Chris Lightfoot-Wild** 16:40 Feel that over.
