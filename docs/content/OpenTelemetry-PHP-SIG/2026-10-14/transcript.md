SIG: OpenTelemetry PHP SIG
Date: 2026-10-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Pawel Filipczak (Elasticsearch B.V.)** 01:40 Hey, Grace.
**Chris Lightfoot-Wild** 01:42 Hey, Bill, how you doing?
**Pawel Filipczak (Elasticsearch B.V.)** 01:45 I'm okay, thank you, how are you?
**Chris Lightfoot-Wild** 01:47 Yeah, okay, thank you.
the Did you see Bob… sorry, not Bob, Brett had, put a message in, like, early hours this morning, just asking if we had any thoughts on the.
Different time.
**Pawel Filipczak (Elasticsearch B.V.)** 02:04 No, I missed that. Let me take a…
**Chris Lightfoot-Wild** 02:06 I missed it. I was in bed when he, both when he sent the message, and then when the time would have been, so… But.
**Pawel Filipczak (Elasticsearch B.V.)** 02:18 Here it is. Summary.
**Chris Lightfoot-Wild** 02:30 So there might not be a time that we can… as Europeans, realistically, try and get to, but…
**Pawel Filipczak (Elasticsearch B.V.)** 02:35 UTC7, UTC7… So… It works for me.
**Chris Lightfoot-Wild** 02:48 It does.
**Pawel Filipczak (Elasticsearch B.V.)** 02:50 Yeah.
**Chris Lightfoot-Wild** 02:51 What local time is up for you, then?
**Pawel Filipczak (Elasticsearch B.V.)** 02:53 So, it's 9.
**Chris Lightfoot-Wild** 02:56 What.
**Pawel Filipczak (Elasticsearch B.V.)** 02:56 and Yeah, in the winter it will be It will be right.
In the wintertime.
Yeah.
**Chris Lightfoot-Wild** 03:04 I mean, I don't mind trying it. Were we tied to Wednesday, though? Is that the best day for you?
**Pawel Filipczak (Elasticsearch B.V.)** 03:11 It doesn't… it doesn't matter for me. If it's in the morning, then it doesn't matter, so I… I have… Everything except… let me check… except Mondays.
Okay. But, yeah.
And the other day, same.
I'm free at the morning.
**Chris Lightfoot-Wild** 03:31 interesting if could do next Tuesday, because you can't do Monday, maybe next Tuesday, because I'm… going to work, at the office next Wednesday, Thursday, and then coming back on the Friday, so… Which… we only go, like, twice a year, so I don't… I can't not… not go.
Yeah. Anyway…
**Pawel Filipczak (Elasticsearch B.V.)** 03:52 Oh!
Let… so you, you let him know.
or.
**Chris Lightfoot-Wild** 03:57 Yeah.
I'll reply in that thread, and then see if you're happy with that, and Brett's able to make it, then we can… We could even just try one and see how it goes.
Obviously, if Bob's… if that was Bob's last meeting last week, then… and that he was the only American presence, then… Maybe we don't need to worry about it so much?
**Pawel Filipczak (Elasticsearch B.V.)** 04:16 Yeah.
**Chris Lightfoot-Wild** 04:20 Cool. Did you have anything you wanted to put on the agenda? I've got… I've added one thing, and then we can obviously go through…
**Pawel Filipczak (Elasticsearch B.V.)** 04:24 No, I didn't add anything, because I just finished, I hope I finished, I'm fixing the… issues from Copilot, so I've… I hope I finished the, probability sampling.
So I created pull request, so I guess it's the latest pull request in the repository.
**Chris Lightfoot-Wild** 04:50 Nice.
**Pawel Filipczak (Elasticsearch B.V.)** 04:50 So please take a look. So it's a bit of code.
Don't be hard.
**Chris Lightfoot-Wild** 04:58 No, sorry, yeah, 5, 6, 5, 6, yeah, I'll, I'll try and get my way through that.
**Pawel Filipczak (Elasticsearch B.V.)** 05:04 Awesome.
**Chris Lightfoot-Wild** 05:07 Cool. Should I share my screen and I can do the meeting notes, etc?
**Pawel Filipczak (Elasticsearch B.V.)** 05:12 If you want, if you can, please.
And.
So I also reviewed the pics in the instrumentation repository made by Brett.
So… so it was hard to get what… What is it about how the fix is working? But yeah, finally, I… I got to the point, and I approve that.
**Chris Lightfoot-Wild** 05:42 I'm glad you did, because I'd seen it and I thought, oh, this is way beyond me.
**Pawel Filipczak (Elasticsearch B.V.)** 05:46 It looks crazy, yeah. So it's just… It's solved, but we are leaking some memory at some corner cases, but, you know, it works.
**Chris Lightfoot-Wild** 05:57 Do you think… is there a way to further test it and refine that, or is that going to be a separate PR?
**Pawel Filipczak (Elasticsearch B.V.)** 06:03 I think we cannot accept that at some corner of the case it's It's leaking, so it's hard to, you know, fix that, so… You know.
**Chris Lightfoot-Wild** 06:16 I'm just trying to share my screen a second, sorry, I'm just… it seems to have changed… I don't know if I've had an update or something, but… the way it's presenting the thing is different. I'm just trying to figure it out, sorry.
**Pawel Filipczak (Elasticsearch B.V.)** 06:32 Yeah, maybe we should prepare some Bored.
And… or something to just click and go through.
**Chris Lightfoot-Wild** 06:44 I guess if we've got enough test cases, then… We're okay, but just… if it's leaking memory, does that mean long-running processes are gonna succumb to just… Exhaustion. I'm just gonna…
**Pawel Filipczak (Elasticsearch B.V.)** 06:56 Mmm…
**Chris Lightfoot-Wild** 06:57 at some point.
**Pawel Filipczak (Elasticsearch B.V.)** 06:59 I think we cannot do anything with that, so… You know.
**Chris Lightfoot-Wild** 07:05 But it's not… the changes that have been introduced haven't… Cars like that, have they?
Is it…
**Pawel Filipczak (Elasticsearch B.V.)** 07:11 Yeah, but otherwise it will just, you know, break the application, so there is no good solution for that.
**Chris Lightfoot-Wild** 07:16 Okay.
**Pawel Filipczak (Elasticsearch B.V.)** 07:17 Yeah.
**Chris Lightfoot-Wild** 07:20 Well, you've approved it already anyway, haven't you? So, all those other ones.
**Pawel Filipczak (Elasticsearch B.V.)** 07:24 Yes.
**Chris Lightfoot-Wild** 07:24 That won't be… Oh, the one thing I'd put on then, on the agenda, if you're talking about that first, is a change I've done in the… well, I've got a PR for it in, the Laravel package.
And that was something that I think it'd be maybe touched on very briefly in the past, I don't actually remember.
I think I recall Cedric.
Probably a couple years ago now, mentioning it as well.
But, like, composition and functionality rather than… so at the moment, obviously, Laravel.
Is using the framework events to sort of capture log messages, etc.
But under the hood, it's just calling, like, PSR3 loggers.
So that would be… You know, it's possible there to actually… compose the… those packages in to Laravel instrumentation, so rather than having to repeat the functionality everywhere.
I guess Laravel could basically string together PDO, PSR18, PSR3, And I wondered what, like, I guess your thoughts were, perhaps.
I'm doing that.
The example here, I'm using the… HTTP, package that's been written by Neva.
Sorry, can you hear me okay? It seems to be freezing a little bit.
**Pawel Filipczak (Elasticsearch B.V.)** 08:47 Yeah, my… my internet is laggy too, so…
**Chris Lightfoot-Wild** 08:51 Oh.
Maybe it was Zoom that just went a little… So this was spun because someone had replied an issue.
saying that the default capture of the traces in Laravel Leaks sensitive data.
Good.
Can you hear me okay? This is… feels really laggy.
**Pawel Filipczak (Elasticsearch B.V.)** 09:18 Yeah.
Yes, so… Yes, yes, please go on. So, I just enabled captions, so if it… I hope it will capture the text and recognize on your side.
**Chris Lightfoot-Wild** 09:30 I'll try turning my video off and see if that helps a little bit.
One second.
Seems to be going a bit.
**Pawel Filipczak (Elasticsearch B.V.)** 09:41 Okay, okay, so it works, let's… if it will just, you know, freeze, then I will let you know.
**Chris Lightfoot-Wild** 09:48 Thank you.
So… Apologies, it seems to be on a very… Very slow stint.
So.
Just trying to get to that composer file.
It's a little bit like pulling teeth.
**Pawel Filipczak (Elasticsearch B.V.)** 10:24 Still waiting.
**Chris Lightfoot-Wild** 10:27 Sorry.
**Pawel Filipczak (Elasticsearch B.V.)** 10:28 You clicked Composer?
**Chris Lightfoot-Wild** 10:31 I have done, yeah. It's just taken forever.
**Pawel Filipczak (Elasticsearch B.V.)** 10:33 Okay, okay, okay, here it is.
**Chris Lightfoot-Wild** 10:36 There we go. Finally. So This, this config package here… That does bring with it a bump to 8.2.
I don't know if there's, like, an explicit reason for that or not, but… I decided to just go with it, because 8.1's, like, out of support anyway, and I thought…
**Pawel Filipczak (Elasticsearch B.V.)** 10:56 Wow. So, I think… I think we should fix that in the HTTPConf thing, because I think it doesn't… it should not require 8.2. It should be, you know.
It should support 8.1, at least. The other… Country packages are supporting that.
But… Okay.
**Chris Lightfoot-Wild** 11:16 I'll be happy.
Tell them.
**Pawel Filipczak (Elasticsearch B.V.)** 11:18 You know.
You can take a look. If it will pass, you know, the CI, then… And then we can just, you know, change it to 8 at 1, but… I guess we'll drop support somewhere in… early December for the PHP 8.1, so maybe we can just accept that. Yeah.
**Chris Lightfoot-Wild** 11:39 If that's the case, then maybe… I'm not in any particular rush to get this out, but it was, That was one of the main reasons, and I thought I'd just… try and prune a few of the older versions that even Laravel's not supporting anymore.
So probably potentially drop 10 and 11 as well.
I just wanted to highlight it, because I guess I don't know if this causes a problem for the distro.
Maybe it won't.
**Pawel Filipczak (Elasticsearch B.V.)** 12:07 It will cause a problem, yeah.
It will cause the problem, so… yeah.
**Chris Lightfoot-Wild** 12:11 Would you rather me not do that, then?
**Pawel Filipczak (Elasticsearch B.V.)** 12:13 Yeah, it will be better to use 8.1, but… As I said, if… we can just, you know, change it to 8.2 later. But if you can, please take a look if it's not a big deal to change it to 8.1.
Then… Then, yeah, why not?
**Chris Lightfoot-Wild** 12:32 I guess plan to drop.
in the distro 8.1 all at the same time, for all the packages. We'd bump them all to 8.2, and then… Yeah, exactly. Okay.
Cool. Yeah, I can do that. I'll have a look.
Then.
But, yeah, so it composes the same.
And then, where it's using that, then, is… Within the instrumentation here.
I wasn't sure… I wasn't entirely sure what the API is supposed to be on this, because you get this configuration, this config properties object back.
And it's basically an eraser, you just get something out of there.
So I said, oh, I'd like to get the HTTP config.
And that obviously brings the sanitizers and things. So the way I then use it in the kernel here is.
What's down here?
So I also I pulled in the factory, PSR17 factory, so it can discover.
It's already composed into the user land application.
And then from that, I can get a URI and pass it into the sanitizer that the HTTP config package provides.
And then, obviously, the values that come back then have been sanitized through this process, so… Oh, it was quite useful to achieve the same thing without having to reinvent the wheel, because it already exists in the other package.
But… To my knowledge, this is, like, the first time that we'll be doing that.
**Pawel Filipczak (Elasticsearch B.V.)** 14:07 Oh, sorry.
For me, it looks very good, so it's okay.
**Chris Lightfoot-Wild** 14:13 That's okay, no concerns.
**Pawel Filipczak (Elasticsearch B.V.)** 14:16 Yeah, I'm wondering about the headers. Can we also… if I'm thinking about implementing the header capturing, and I did it for the HTTP frameworks, but didn't do that for the Laravel.
And I'm wondering…
**Chris Lightfoot-Wild** 14:35 you.
**Pawel Filipczak (Elasticsearch B.V.)** 14:36 We can also sanitize the headers here.
**Chris Lightfoot-Wild** 14:39 Yeah, well, I actually started playing around with PSR18 instrumentation as well. I just noticed as well, so we've got another attendee joining us. Hi there, Gilberto.
**Pawel Filipczak (Elasticsearch B.V.)** 14:50 Hey.
**Chris Lightfoot-Wild** 14:51 Unmute. But welcome.
Yeah, I was playing with the PSR18 instrumentation, because I thought it was… Basically the same thing. The Laravel, instrumentation currently is looking at the Client Watcher.
And that's built on top of Guzzle, basically, and obviously Guzzle then implements PSR18.
So it's either just… guzzle, or I thought I'd go to the sort of lowest possible point with the instrumentation.
So, I don't know what your thoughts potentially would be around that, but it was to try and get SPI into PSR18.
And then have it… Because I realized this was something that yourself and Sergey had added.
With the helicopter.
**Pawel Filipczak (Elasticsearch B.V.)** 15:37 Yeah.
**Chris Lightfoot-Wild** 15:39 But… There's functionality for this already in… oh, there's partially some functionality for this.
In the API?
Oh, sorry, in the SDK configuration.
Which is here.
**Pawel Filipczak (Elasticsearch B.V.)** 15:56 So.
**Chris Lightfoot-Wild** 15:57 I thought there was some overlap, and I didn't know if, like.
If we're heading down that route, if you don't object to the SPA and then composition of these packages.
Yeah.
But if you've got no immediate concerns, Then maybe that's positive.
**Pawel Filipczak (Elasticsearch B.V.)** 16:15 I think, I think it's, it's okay.
**Chris Lightfoot-Wild** 16:20 I'd like to basically stream… I'll strip back some of the functionality that Laravel's had to use itself.
And just delegate that to the appropriate package instead.
Because it's fixed. If someone reports a problem with login, we can fix it in one place.
And then it benefits everywhere else.
**Pawel Filipczak (Elasticsearch B.V.)** 16:40 Yeah.
Makes sense.
**Chris Lightfoot-Wild** 16:43 Yeah. So I was I was trying to sort of, wrangle PSR 18 instrumentation.
I realized that some of the the way it's set up might.
There's some crossover with… the way they stubbed out the Laravel tests as well, and if there's a comment.
But maybe we just need to put them in, like, the utility, testing.
package, which I think we've got… Here, but isn't used very often.
And then we can… Centralize that, rather than just copying Copying the code around.
**Pawel Filipczak (Elasticsearch B.V.)** 17:16 Exactly, exactly. Good point.
**Chris Lightfoot-Wild** 17:19 So I've got a bit of cleanup to try and do. But yeah, ultimately I was looking at PSR 18 for.
The client watcher, because that is obviously making outbound requests rather than sort of the server spans, the client ones.
And that… The sanitization can happen there.
Umm.
By this picture.
you know So if that makes… yeah, cool.
So, so great.
**Pawel Filipczak (Elasticsearch B.V.)** 17:46 Salzburgers.
**Chris Lightfoot-Wild** 17:50 Yeah, yeah, thank you. Sorry for.
Being so laggy as well, though.
**Pawel Filipczak (Elasticsearch B.V.)** 17:56 Yeah, sometimes I have to wait a bit for the refresh of the screen, so…
**Chris Lightfoot-Wild** 18:03 Yeah, sorry about that.
**Pawel Filipczak (Elasticsearch B.V.)** 18:05 Oh, no worries, it's not your fault.
**Chris Lightfoot-Wild** 18:07 I'll maybe raise that with Brett as well, just to see if he's got any concerns, put it in the chat, but…
**Pawel Filipczak (Elasticsearch B.V.)** 18:13 Yeah.
**Chris Lightfoot-Wild** 18:14 Yeah.
**Pawel Filipczak (Elasticsearch B.V.)** 18:15 I will also take a look into this draft PR you created, so I will, yeah.
I will analyze.
But… Thank you.
**Chris Lightfoot-Wild** 18:26 So… I'll put, realize I didn't fill out the attendee list. Sorry about that.
Yeah, hi there, Gilberto. I don't know if you had anything you wanted to add to our agenda before we, walk the board?
If you do, feel free to pop it down.
Oh, I realize I should say actions.
Sorry, the text formatting's gone garbage.
This is my spelling.
So… The parachute board.
you know… You don't have anything in… I might as well open it, but in distro, I suppose, that you needed looking at.
**Pawel Filipczak (Elasticsearch B.V.)** 19:59 Oh.
I was focusing on this probability something this week, so… I guess, how are you?
When I… when we will merge it, then I will try to include it into the distro, and as well, and update the packages, so… Yeah, maybe next week.
**Chris Lightfoot-Wild** 20:20 Sounds good.
Right.
Country PRs.
There's a Larva one there, so I'll take a look at that.
The Zismore findings one, I think Trask opened that a little while ago, and… Just come back to us on that, because there was… Something blocking it.
There's nothing…
**Pawel Filipczak (Elasticsearch B.V.)** 20:52 Thank you so far. Yeah.
**Chris Lightfoot-Wild** 20:57 So I'm going lucky again, huh?
Turn my video off and see if it helps.
Second time.
**Pawel Filipczak (Elasticsearch B.V.)** 21:10 So it's still the same issue, right? With this dot and dollar sign in the paths.
**Chris Lightfoot-Wild** 21:16 Yeah, it looked… it looked to be.
I mean, could just merge it in, and then if it fails, back it out again, I suppose, but then that's a bit… Like, I suspect it's gonna be broken, so maybe just ask the question, and… See what we can do about it.
And then some dependency ones that… Not had a look through yet, but can try and get through.
Was there anything to hear you if I say this, the monologue one.
**Pawel Filipczak (Elasticsearch B.V.)** 21:48 I think there's no update.
**Chris Lightfoot-Wild** 21:51 Cool. That was the one with… it's waiting on more SPI-based stuff, isn't it? So, maybe we can pick that up as part of that soon.
Figure that out.
This wasn't enough.
Instrumentation, 11 PRs, but I'm guessing most of that is noise, is it?
Renovate.
**Pawel Filipczak (Elasticsearch B.V.)** 22:14 Yes.
Those are my thoughts.
**Chris Lightfoot-Wild** 22:18 All the pipelines are green.
I can't actually imagine this repo either. I'm guessing you're probably the same.
**Pawel Filipczak (Elasticsearch B.V.)** 22:25 Yes, I can't do… I can't… can't merge.
**Chris Lightfoot-Wild** 22:29 ask.
**Pawel Filipczak (Elasticsearch B.V.)** 22:30 Maybe something changed, so let me, let me check. One second, one second.
**Chris Lightfoot-Wild** 22:43 That could be.
**Pawel Filipczak (Elasticsearch B.V.)** 22:46 No, I can't.
**Chris Lightfoot-Wild** 22:49 Maybe that should be an action for, Discuss maintenance, at the next… the next meeting. Obviously, with Brett just being our, sort of, down to our Single call one.
**Pawel Filipczak (Elasticsearch B.V.)** 23:05 It'd be good to know that, because now we are totally blocked.
**Chris Lightfoot-Wild** 23:09 Yeah.
Yeah, hopefully, we'll we'll be open to that.
Cool, so thanks for reviewing that one of Brett's earlier.
**Pawel Filipczak (Elasticsearch B.V.)** 23:21 Yeah.
**Chris Lightfoot-Wild** 23:22 Are you the same boat there? Obviously, you can take care of these ones, but a lot of renovate noise.
**Pawel Filipczak (Elasticsearch B.V.)** 23:26 Yes, I have to invest some time and… And review them. Mostly they are because we have a bit fixed building procedure, so we are using log files, and it's trying to bump the packages constantly, and it's… Yeah, it can be just bumped.
**Chris Lightfoot-Wild** 23:45 Is it beneficial to… Have that remain kind of being renovated or can we disable it for certain?
**Pawel Filipczak (Elasticsearch B.V.)** 23:54 I think it's, it's, it's, you know, for the, for the, Native packages, it can be named, but for the PHP, it should be disabled, so maybe I will try to figure out, maybe I can apply some rule or exclude some paths.
Or files from investigation. That's a good point. Yeah, I wasn't… I never thought about that.
I can solve that too, to prevent this, you know… Must.
**Chris Lightfoot-Wild** 24:23 messing around.
Sorry, is it these ones that it's, it's missing?
**Pawel Filipczak (Elasticsearch B.V.)** 24:30 Yes, exactly, exactly.
**Chris Lightfoot-Wild** 24:32 Hopefully there's a way of just excluding that directory in them.
Causing less noise on the channel.
**Pawel Filipczak (Elasticsearch B.V.)** 24:38 Exactly.
**Chris Lightfoot-Wild** 24:41 Issues… oh, sorry, I missed that one.
Pull request on this one.
Oh, Brett's already opened. Oh, that's that's good.
It's still in draft, but he said there was going to be some changes to the… Declarative config stuff in that, and… I tagged a version of the Laravel instrumentation of the day as 1.10, which used the previous, so I hope… I guess I need to be on this and check what the changes entail.
I kind of jumped the gun a bit slightly, I think, because I'd semi-forgotten that we'd had that conversation, and I thought… Because I've got this other PR built on top of it, I just want to get that one done and out of the way, and it's been a few weeks of… Sitting in draft.
Yeah, I'll take a look at that.
**Pawel Filipczak (Elasticsearch B.V.)** 25:30 Yeah, me too.
**Chris Lightfoot-Wild** 25:35 I think it'd be quite, it seems quite powerful, the SPI stuff, once you start sort of tinkering around with it and understand.
The extra benefits it brings along with it.
Yeah, I'm still trying to learn how it's structured and pulls together, but… Yeah.
Interesting stuff.
We have. Did I miss any other boats?
**Pawel Filipczak (Elasticsearch B.V.)** 26:04 No.
**Chris Lightfoot-Wild** 26:08 Wouldn't mind adding for, I guess, for the next agenda as well, to put it as, Boom.
I've seen, it's kind of a bit all over the place, isn't it? The API and SDK haven't been tagged for a while. I don't know if there's a… Brett's gonna just do that at some point or not, but…
**Pawel Filipczak (Elasticsearch B.V.)** 26:30 Yes, that's a good point, that we should discuss that, because now I think we are not… we should definitely release more frequently than every half year, or… Yeah, then…
**Chris Lightfoot-Wild** 26:41 I agree, yeah. Even patch releases, I think, were beneficial, because it's hard… When you just, sort of, wait for so long that there ends up being a bunch of stuff, and it's like, well, one of the things could have broken it.
So yeah, improving that cadence would be useful.
I've got one more final thing as well, which… The packages on packagist.
The majority of them, are owned by either Bob or Brett.
But the Ometry Bot user that we've got, kind of, access to.
Has created a few new ones, because it does that in the pipeline.
But it doesn't automatically get… The other missing ones. So, There's a… one in here was an example of that, some Falcon.
That was one that the workflow had created, but this user can't access the other one, so if I go… Looking at,
**Pawel Filipczak (Elasticsearch B.V.)** 27:44 So the Zoom panel hidden the name. So it was the bot user, right? This previous one you showed me for the file.
**Chris Lightfoot-Wild** 27:53 Yes.
Yeah, this is the name of the bot account.
That is… A maintainer on these four, so it's been added to that manually.
But these three, it got done via the pipeline.
But obviously.
if Bob's going, sort of, emeritus, we're down to just Brett, and if there's any other changes required, and Brett's lost his access, then we're stuck out.
**Pawel Filipczak (Elasticsearch B.V.)** 28:21 So, in that case… Brad should add this bot to the maintainers.
Yes.
**Chris Lightfoot-Wild** 28:30 Yeah, there's about 60 or 70 of them to do.
**Pawel Filipczak (Elasticsearch B.V.)** 28:34 I guess.
**Chris Lightfoot-Wild** 28:35 Well, I guess…
**Pawel Filipczak (Elasticsearch B.V.)** 28:36 He can use the script to do that.
**Chris Lightfoot-Wild** 28:39 Yeah, well, there's not actually an API to do it, so you could either look into it, or just… you know, painfully go through and just add it in. So, we could ask, it's an ask on Brett either way, so, put it on for next time.
That we can visit with him.
But I don't personally care for having, like, any… one… well, I guess it's my opinion, but would… as long as the bot owner, the bot user is… And then all these then handle stuff as much as we can via the pipelines.
And.
And it's not tied to any one individual.
**Pawel Filipczak (Elasticsearch B.V.)** 29:18 Yes, it's better to keep it as a bot, because otherwise it will be always a problem that someone leaves the community and we have a, you know, package without maintainer, so… It's even hard to change anything in the package settings.
So, yeah, bot is better choice. At least we can… We can fix something with the CI, with the scripting, or whatever.
Or however, different, you know, tool, create some tools.
I had some issues with the packages from our company, and it was difficult to, you know, to change something in the settings, because the old maintainer left.
**Chris Lightfoot-Wild** 30:03 Yeah. Just in the same position, yeah.
**Pawel Filipczak (Elasticsearch B.V.)** 30:06 Yeah.
**Chris Lightfoot-Wild** 30:06 Yeah, there is, if you need access as well, Severin can add you to the OpenTelemetry 1Password.
Should you need to log that bot account, but… I think for the most part, we all needed to… to do that, to set up the package in the first place. The rest of it is automated, so… Should all be good.
You just… obviously, we've installed the webhook once within the OpenTelemetry PHP organization on GitHub, and then… All the new packages use that, so it's… So trivial at this point.
Cool, I'll put that on for the next time, then.
Mmm.
Maybe for Brett.
Mmm.
Was there anything else you wanted to… Discuss there, or is it just a… I appreciate I've kind of loaded up the next, meeting where hopefully Brett's about.
**Pawel Filipczak (Elasticsearch B.V.)** 31:22 So, no, no, nothing.
I have to, you know, focus a bit on distro this week, so yeah, maybe I will… I'm considering implementing the body capturing in the request. So yeah, I have to figure out if there is a SEMCONF for that. I guess there is already for the body.
But I'll take a look.
**Chris Lightfoot-Wild** 31:52 I guess that would be just an opt-in, certainly opt-in by default thing.
**Pawel Filipczak (Elasticsearch B.V.)** 31:57 Yeah. It's easy, it can, you know… create a huge overhead on the memory and you know and processing time so.
**Chris Lightfoot-Wild** 32:07 Give me the bullet.
Okay.
Yeah. Is that like a user request then? Is that.
**Pawel Filipczak (Elasticsearch B.V.)** 32:12 Yes, yes, yes.
**Chris Lightfoot-Wild** 32:15 Interesting.
As well, going back to the… We'll talk about that in the HTTP config.
I thought there was a potential option for that there.
Capture requests.
**Pawel Filipczak (Elasticsearch B.V.)** 32:30 Got it. Yes.
**Chris Lightfoot-Wild** 32:32 The actual, not the actual body.
**Pawel Filipczak (Elasticsearch B.V.)** 32:34 Yes, you can you can limit the body size.
**Chris Lightfoot-Wild** 32:38 But… Okay, so… Maybe that implies that it's not… It's not been discounted. It could be an option to add to this.
But this… this thing… With the capture headers, I realized it seemed to be nested under a PHP, rather than, like, the generic level at the top.
And.
So the PSR18 header capture stuff.
My wife.
part of this as well, I suppose, but I don't know… I don't know why that split exists. I don't know if this is because it's under development still.
I have a good for my.
into the SDK config package or not.
And.
Maybe that's one to try and check out, because… I'm not fully sure why the SDK configuration lives separately to the SDK.
Because if you're going to be configuring it most of the time.
you kind of need that package. I don't know if that's going to be… Like, first party at some point.
**Pawel Filipczak (Elasticsearch B.V.)** 33:42 Yeah.
**Chris Lightfoot-Wild** 33:43 I've not got a strong opinion on it, it just seems like… everywhere you're going to use SDK, you want the SDK config package as well alongside it, you might as well combine the two, but… We can, we can ask that next time.
**Pawel Filipczak (Elasticsearch B.V.)** 33:56 Yeah.
I will take a look. I will take a look. I guess it's already in Java, but yeah.
I'm wondering how they how they solve that.
**Chris Lightfoot-Wild** 34:09 Well, it's split in Java, the SDK configuration, is it?
**Pawel Filipczak (Elasticsearch B.V.)** 34:13 Yes, I think it is.
**Chris Lightfoot-Wild** 34:16 I had seen something in the Java API where it's configuring itself.
I think I mentioned this previously, but obviously Java's got a load of functionality, so it does.
reach out into the class loader to ask for an SDK configured component.
Whereas in my head, I had it that The API should be totally disconnected from the SDK. It should never.
But then, I think, if they're setting a precedent for doing that.
I remember Brett had a V2 branch of the API, and it had… added SPI into it, because then essentially we could do the same with SPI, couldn't we? We just declare an interface that we want to get the central config from.
And then separate packages can implement that, and we can effectively load in.
Hmm.
Yeah, I guess if you're…
**Pawel Filipczak (Elasticsearch B.V.)** 35:09 yeah.
**Chris Lightfoot-Wild** 35:10 Let us know how it goes.
**Pawel Filipczak (Elasticsearch B.V.)** 35:11 I think it's possible with SPI, yes.
**Chris Lightfoot-Wild** 35:16 Yeah, maybe we need to… again, so another one for the… for the list for next time, I'll put it on.
For Brett, question, are we… And… Well, I guess it's more likely to be SDK V2, isn't it?
But the API also need the SPI in it, so you can… Optionally compose in, so.
And with… Kind of butchered that sentence, but I'll explain it over there.
Cool, well, that's everything from me, if you've got nothing else. Gilberto Berlito, by any chance, did you want anything to add or ask, or are you just here to… See how it goes.
I'm just here as an observer.
**Pawel Filipczak (Elasticsearch B.V.)** 36:14 Okay, so…
**Chris Lightfoot-Wild** 36:17 Okay.
Oh, no.
So I've just seen that, English isn't very good yet. Work with IRL, I'd like to start contributing a bit more to the country. I also plan to follow the meetings more closely, so I can contribute in the area, even getting a deeper understanding of the project.
Thank you, Gilberto. Nice to have you. Hopefully, we'll see you again.
Feel free to say hi in the… in the Slack channel as well, if you're not already.
In the hotel PHP channel.
I can slack. I'll put that in here as well.
Thank you very much. See you next time. Cheers, Bob.
**Pawel Filipczak (Elasticsearch B.V.)** 36:59 Thank you, guys. See you.
