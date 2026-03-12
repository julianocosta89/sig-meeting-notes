SIG: JavaScript SIG
Date: 2025-12-17
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:00:19 I don't…
Jamie Danielson 00:00:23 Hello.
Andrei Borza (Sentry) 00:00:28 Hello?
Jamie Danielson 00:00:30 Hello.
I was gonna give it.
One more minute, especially, cause… We don't have any topics, right now, and so in case someone joins in… How's a topic?
Not sure.
I feel like I usually go till… 3 or 4 after, but I'm realizing time of year, it's possible not many people We'll be joining.
Marc Pichler (Dynatrace) 00:02:42 Or possibly people are wrapping up the things already, and… PC with other stuff.
Jamie Danielson 00:02:56 Yeah, so either way, I guess I put a note in here. This is the last SIG meeting, of 2025. I think all of OTEL is holding off meetings for the last two weeks of December.
So… Yeah.
So I'm just gonna put a note.
Thank you to everyone, for your involvement and contributions.
appreciate.
Everyone who's… shown up, or… not shown up, but is involved either way, so… thank you.
I guess one thing I'll note, just for, like.
Status update sort of a thing, Trent and I talked this morning, with Mark, but our hope is to get the, HTTP and database Some comms, migration updates done.
This week, hopefully. So that… You know, in roughly 6 months' time, We can look at dropping the old… Code.
and just move forward.
Marc Pichler (Dynatrace) 00:04:32 New Year's resolutions.
Jamie Danielson 00:04:35 2026 is gonna be great.
Trent Mick 00:04:39 It was gonna be out of June, so that by Christmas we could drop it.
Jamie Danielson 00:04:44 Yeah.
Trent Mick 00:04:45 6 months.
Jamie Danielson 00:04:46 Yeah. You know what? It's better, better late than never.
That's what happens when we manage to push again and say, okay, let's focus on the thing. So, that's good.
I guess we can jump into bugs. Again, if at any point someone joins in and wants to add a topic.
Feel free to do so.
Marc Pichler (Dynatrace) 00:05:16 Oops, I had looked into that one. It was, I think, just a… Loader.
Jamie Danielson 00:05:25 Excuse me.
It seems to do the trick. It'd be nice to have this information on the public. Did I not add this in the public docs? I meant to.
At least…
Marc Pichler (Dynatrace) 00:05:35 note.
I think there's a note there, but I guess people just glance over it.
Jamie Danielson 00:05:47 If there's a note, it's not easy to find. I think… Cause we have a… Yeah. So no, there's definitely an issue we had somewhere.
for, like, ESM… documentation.
I can't remember, it might just be in, not contrib.
Trent Mick 00:06:17 Not the one that you closed, because you added ESM docs.
Jamie Danielson 00:06:20 Yeah, but there's more to it. So Mark had made this really comprehensive issue, saying, like, how we would consider it done.
And then I put in a checklist, I think.
And just looked at this, actually, the other day. I think it's one of my many open tabs.
So, like… I don't think the public docs is there. Like, we have the note… in the READMEs.
But so, this is, like, the main thing, so I'll come back to… Doing this, even if it's just, again, the idea being, like, it might just be a link to the repo, to that one doc in the repo, but just making it more obvious, because… It's not here, but you can see, like, We have this… Just this line should be in there.
Marc Pichler (Dynatrace) 00:07:22 I will, put a comment on the, bug issue here that we have, An issue already that tracks this.
Jamie Danielson 00:07:32 Yeah, I guess I can do it, because I have it open, right?
Marc Pichler (Dynatrace) 00:07:36 Oh, I'm, typing already.
Jamie Danielson 00:07:37 You're already typing it? Okay.
Marc Pichler (Dynatrace) 00:07:40 You don't need to do it live, huh?
Jamie Danielson 00:07:45 Just put that issue in chat, in case it's… Easier to find.
Okay… So… and then close that issue?
Marc Pichler (Dynatrace) 00:08:00 Yes, I will close it as, duplicate, I think.
Jamie Danielson 00:08:04 Cool.
Thank you.
Marc Pichler (Dynatrace) 00:08:09 Thank you.
Jamie Danielson 00:08:16 Oh, DynamoDB traces after instrumented for Lambda Node.js application by self-building a layer.
We have enabled debug logs. I can see there's DynamoDB-related logs.
But from DataKit, we did not get any incoming DynamoDB traces data.
If this shows up in… Debug logs.
That means it's being… generated.
And… exported.
Alright, so if anything, there's potentially an issue… On this data kit.
Or, what is DataKit, actually? We sent the OpenTelemetry traces to DataKit, so I guess that's, like, a backend.
Marc Pichler (Dynatrace) 00:09:34 Data kit is…
Trent Mick 00:09:41 It's the collector for this vendor.
Jamie Danielson 00:10:13 like… my thought… I guess maybe I can double-check and ask on here, but… If this is showing up.
Whoa.
Trent Mick 00:10:33 Yeah, I agree, that's the diadette debug saying this is dated to be sent, so either…
Jamie Danielson 00:10:38 There's something wrong with the.
Trent Mick 00:10:39 Something just after that, it borked on export?
Or… It just dropped it.
Jamie Danielson 00:10:47 The debug logs is a simple processor, right? So, it's going to send them out immediately.
Isn't that usually a thing with Lambda? Like… It shuts down before things can export.
Although it has the other one.
Trent Mick 00:11:05 Description, they're getting other data, so…
Jamie Danielson 00:11:08 One sec.
Trent Mick 00:11:08 Yeah, I don't think it's about buffering.
Marc Pichler (Dynatrace) 00:11:13 I'm not sure if… I think it might not be completely clear where they are not seeing the… things. I'm not sure if they have some sort of, debug exporter in this data kit thing.
Or if it's just not showing up in whatever UI they are using to, look at the data.
So… if… they can… Tell us exactly where it gets dropped, or do some investigation into where it gets dropped, and see if it actually Get sent to that endpoint, then… We might be able to help them in figuring out where stuff gets lost.
Jamie Danielson 00:12:39 Like, I wonder if they could even… it might be too heavy-handed. I was gonna say, like, set up a collector, and see if it shows up in a collector.
And if so, then the issue's not on… The OpenTelemetry side, it's on… the data kit side.
We have, like… Yes, should I… We'll just leave this here…
Marc Pichler (Dynatrace) 00:14:29 Yeah, I guess we don't have enough, info here.
So… I guess leaving it for now is probably okay. Then we'll get back to it once there's an answer.
Jamie Danielson 00:14:42 Yeah.
Trent Mick 00:14:42 I also had a comment that they could try setting hotel traces exporter.
To include consoles, so they could see in there.
Output.
That would confirm that.
the… exporter…
Jamie Danielson 00:14:57 K-sided.
Trent Mick 00:14:57 Successfully exporting stuff.
And then you know that it's on the reception site?
Jamie Danielson 00:15:03 Good point.
Trent Mick 00:15:04 There's another thing I noticed here, too, in that the screenshot includes old DBenConf and DynamoDB was not on our list of… Database some comp work to do, so we gotta add that one, too.
Jamie Danielson 00:15:16 Bullshit.
Trent Mick 00:15:17 It's something I got missed, on the list.
I can… oh, I can go add another one. You're driving.
Jamie Danielson 00:15:30 This is the… Okay, so, actually, let me double check if we got… Any other topics? Nope. Okay.
Trent, this one was yours, the unit test job failing. I think it was a cache.
Trent Mick 00:15:56 Yeah, that's fine. David and I discussed. We could talk about… increasing there.
Dash size… I don't know. David, what do you think, a week, or is that… Is that problematic? The retention of one day means that you need to be right on top of it if you want to rerun
David Luna Bistuer 00:16:13 Yeah. Failing steps.
Jamie Danielson 00:16:15 Oh…
David Luna Bistuer 00:16:15 Yeah, usually it works fine, because you push again, and you commit, and then you run again everything. And that, feeds up, again, the cache again, but… Okay, maybe a wicked.
We need to… we need to think… I need to check what… what are the limits of, For caching.
If.
Trent Mick 00:16:37 Yeah, it's just whether we hit some quota or something like that, yeah. This is super low priority, so… it's an edge case.
That I think is probably… I'm not even sure if it… does it require… maintainer. I'm not sure what, group levels are allowed to even go rerun in the CI.
Marc Pichler (Dynatrace) 00:16:56 Approvals… everybody with right access should be able to…
Trent Mick 00:17:01 To go do that. Okay, yeah. So, this can only possibly hit those people, so… This is…
Jamie Danielson 00:17:08 And, I guess.
Trent Mick 00:17:09 It's not impacting users or anything, so…
Jamie Danielson 00:17:11 and what David just mentioned is, like.
You could also just push a new commit to it, and that would work, because it's gonna clear the cache.
Trent Mick 00:17:20 Or choose the option to run… rerun all jobs instead of just the failing ones.
Jamie Danielson 00:17:25 Awesome.
Trent Mick 00:17:25 And that'll run the first compile step that regenerates the caches.
Jamie Danielson 00:17:29 It's fine.
It does seem like it would be nice to, yeah, increase that.
The days, even?
Right? If we can.
Because then you think that something is failing, and it's not really, potentially.
Marc Pichler (Dynatrace) 00:17:45 One thing that I have noticed before is, if there's a lot of traffic on the repo, and we are running a lot of, stuff.
The cache will get… so old cache entries will get dropped before the one-day time.
So I'm not sure if… Increasing it would… Be helpful in that case, because…
Trent Mick 00:18:14 We might already be in here.
Marc Pichler (Dynatrace) 00:18:15 Anyway, yeah.
Jamie Danielson 00:18:20 So just never rerun from failed. Just always rerun all, or…
Trent Mick 00:18:25 Or you get lucky sometimes, but yeah.
Jamie Danielson 00:18:27 Yeah.
Marc Pichler (Dynatrace) 00:18:28 Yeah, I guess, One thing that we could think of is also keep it in mind that we need to That this is something that could happen.
And then just… Yeah. Whenever it could happen, we just think about it in the back of our minds, or we have some sort of a logging step that tells us, hey, you might need to rerun the whole thing again, so that we don't run into, That stuff, where it looks weird, and we don't know what to do.
David Luna Bistuer 00:19:09 So it says, the max is 3 months, it's now 90 days, but, it's also bound to the, artificial policies, which are now, formed.
That depends, I think, on… Which plan do we have in the GitHub?
Marc Pichler (Dynatrace) 00:19:27 I seem to remember that there was some way to see, like, all the cache.
Where the cached stuff.
Or is it just an, admin?
Trent Mick 00:19:46 Oh, I do remember seeing that.
Marc Pichler (Dynatrace) 00:19:47 have to.
Trent Mick 00:19:48 No, no one knows.
Marc Pichler (Dynatrace) 00:20:09 Alright, that's just for the, OSF… OSSF scorecard. I think it was, it's bound to the role that the user has on the contract repo.
nowadays, we are maintainer role, not admin role, so I guess we can't see that anymore.
Or maybe… I was just… It's on caches. This is the link, one second.
Just put it in chat.
Yeah, so that's the… Like, the 10 gigabytes are…
Jamie Danielson 00:20:57 We're approaching the.
Marc Pichler (Dynatrace) 00:20:58 I'm in.
Though all of these seem… Barely old.
There's some that are 2 weeks old.
Jamie Danielson 00:21:31 Yeah.
Okay, I guess…
Trent Mick 00:22:01 I think we can move on. Eventually, we'll probably just close.
Jamie Danielson 00:22:03 I know, I'm, like, nerds.
Trent Mick 00:22:04 Don't intend to fix.
Jamie Danielson 00:22:09 Okay.
That's okay.
Okay.
So it's those… I guess just a note on, like, an update on this one. I assume nothing new since this morning, yeah.
So, this was a PR that went to add in newer messaging at conventions, which aren't stable yet. So, Mark has a PR, I believe, in SEMConv, to add in messaging latest experimental, so that we can start implementing that. And in the meantime, I created a separate PR to be able to move forward with the finishing the HTTP SEMCOM migration to separate the two things so that that can get done, sooner, and the messaging thing can get sorted out.
Otherwise, I don't think there's anything else.
In there.
Remember… Looking at… this. This one's still waiting on spec and consistency, isn't it?
Of something new?
Trent Mick 00:23:29 Oof.
Jamie Danielson 00:23:31 Before I can.
Trent Mick 00:23:31 Continue work.
Jamie Danielson 00:23:32 this PR, I opened an issue to formalize the conversation and see what will be the right way forward. Okay.
So… Do we have, like, a… Waiting on spec or something.
Or on hold, needs spec.
Seems good.
Cannot be implemented without some changes or clarifications in the spec or semconf.
Trent Mick 00:24:05 Okay.
Jamie Danielson 00:24:12 Redis Cluster, I think this might just still need reviews.
Marc Pichler (Dynatrace) 00:24:24 Yes, I think that one's waiting for reviews.
Trent Mick 00:24:35 Anyone heard from Amir recently?
Jamie Danielson 00:24:40 No.
Oh, so this guy.
Fixed.
So this might be close, then. Like, last time when we looked at it, there was just actual errors.
With a dependency tree, but… Everything looks to be passing now.
So… Maybe another… Quick look, but then this might be… Okay to go.
Sector here now.
Marc Pichler (Dynatrace) 00:25:58 Well, it's weird, jackson's… check mark is not green.
That might be something… maybe I messed up the latest… Codelness change.
Jamie Danielson 00:26:28 Because if he's… Contrib… triager.
Marc Pichler (Dynatrace) 00:26:34 I think I added him to… Approvus a while ago.
Jamie Danielson 00:26:40 Oh, yeah.
Marc Pichler (Dynatrace) 00:26:55 I'll look into that.
This is weird.
Jamie Danielson 00:27:02 Yeah, he's not listed in… cure.
Marc Pichler (Dynatrace) 00:27:08 He's listed in the README, I'll just, send an invite again.
Or, maybe. Or, maybe.
Jamie Danielson 00:27:15 He needs to accept.
Marc Pichler (Dynatrace) 00:27:16 Because I forgot to… Send it the first time around.
Jamie Danielson 00:27:22 Gotcha.
Marc Pichler (Dynatrace) 00:27:23 I follow up on that.
Jamie Danielson 00:27:25 Okay. Cause then, at that point, this one might be good to go.
As long as… These are pretty basic.
Marc Pichler (Dynatrace) 00:27:36 Usually with these, it's good to have one last look to just double-check that all the dependencies are up to date.
I have ran into issues before where… Saw the approvers, then merged it, and then realized that, the older dependencies were out of date, but this seems to have… Happened in the last two weeks, so it should be… Almost good to go.
Jamie Danielson 00:28:04 Famous last words.
Marc Pichler (Dynatrace) 00:28:06 Yes.
Jamie Danielson 00:28:06 I have a question. Didn't we used to have… The update branch thing on this screen?
Like, did we change something?
Like, for the lazy, I just want to merge branch main in without having to do it.
Locally.
Marc Pichler (Dynatrace) 00:28:23 It should be there. I'm pretty sure I used it in the past two or so days.
Trent Mick 00:28:29 Is it just not showing because it's up to date?
Jamie Danielson 00:28:33 Maybe.
Because I remember… no, because I remember one of mine, I had to do it locally and push it.
I don't remember which one.
Marc Pichler (Dynatrace) 00:28:47 It might be that… Maintainer edits are off.
I don't know, maintain the salon and that…
Jamie Danielson 00:28:56 I think it's for mine, too, though.
Because I had something that was failing.
And I knew that there was a fix on main.
And I had to do it locally.
I don't know. I can look at it later, I just didn't know if anyone else noticed that, or if I was losing my mind, which I could be, and it could be unrelated.
Don't snail.
I have too many things open now.
Yeah, maintainers are allowed to edit this pull request.
I don't know.
The MCP SDK… Looks like this.
Has some… things.
The author should come back for… Yeah, and I think the draft we can skip over for now is my strong ones instead.
Marc Pichler (Dynatrace) 00:30:27 a follow-up.
Jamie Danielson 00:30:29 Yeah. Right now, this one's… Has some feedback, so just need them to… Come back to it.
This one…
Marc Pichler (Dynatrace) 00:30:48 Yeah, I did review this one, or not… I didn't look into it in detail, but the test data that's being added here is fairly large, so… I was hoping that there would be some way to reduce that amount of test data, because that makes the pulley request, A few thousand lines, which… It's a bit difficult to reveal.
Trent Mick 00:31:20 So those are… generated… Files, so… Yes.
And the way it's architected, there's… The way it's currently set up is you can't reuse any of them, so some of them may just be a copy of another one if it's the equivalent call to the open… AI API.
I don't know.
We could just test less.
Jamie Danielson 00:31:47 Wow.
Trent Mick 00:31:48 Where we could tweak. I mean, but they're all pretty similar, right? They're basically just NOx encoding of a request and response.
Jamie Danielson 00:31:58 Yeah.
Yeah, that's, like, most of it.
Trent Mick 00:32:05 The fact that the test file is… 7,000 alliances.
A bit unwilling.
point.
Jamie Danielson 00:32:13 Oh, wow.
Trent Mick 00:32:13 Those things could be split up. They… also the… The assertions used on the… Responses is getting… a bit big, but that's not really the fault of the way the test was written, it's just that OpenAI… or sorry, AI… Gen AI semantic conventions, like.
There's a lot of freakin' data that's… Virgin AI stuff, so… asserting… All of that is… Wordy.
Also, this is, yeah, updating to the latest NCON, because it's also changing fast, so another one should be… a pain to change in the instrumentation, but then updating 7,000 lines of tests for changes in structure, the return stuff is just nightmarish, so… I don't know. It's like… I can be a bit of a cowboy sometimes, so suggestions to, like, let's just test less probably doesn't always come well received, and I can understand why, but… I'm listed as one of the maintainers on this. I'm certainly not going to have the energy to update to the latest SEMCOMF. That's not related to this PR, but… Yeah, I don't know.
Jamie Danielson 00:33:30 It is a lot. I mean, I guess some things, like, I think the HTTP instrumentation, we might have multiple test files there.
Trent Mick 00:33:40 Oh, it certainly could be broken into separate test files, that would be… reasonable. There's some boilerplate that would have to get copied over, but that's fine.
Jamie Danielson 00:33:48 Yeah, like… Like, this is what we have for HTTP. Now, HTTP is a big instrumentation, it's, you know, certainly a very critical path used all over the place, but… That would be one of the things, but that is… yeah.
Marc Pichler (Dynatrace) 00:34:20 Yeah, this, I think I've just generated by the script.
Hmm.
Jamie Danielson 00:34:26 Wow.
Yeah, there's a lot in there, okay.
So, I guess… What is the… current thought on this right now, is it just… Looking for… time, and…
Trent Mick 00:34:58 Hector was reviewing it, so… had he given it a checkmark?
Jamie Danielson 00:35:02 So… Hector did not give it a checkmark.
Mention some people…
Marc Pichler (Dynatrace) 00:35:11 There's also one comment still pending, from his reviews.
And I think the person at some point mentioned that they… Wood.
continue work on this PR right now, and then split it up into smaller ones.
says, at some point, thanks for reviewing, I can try to split changes into separate commits, but I wait to finish refactoring.
So I guess we're just waiting for the person to… Address the comments there, and then… The way forward would be to split it up into smaller chunks and get these reviewed separately.
Jamie Danielson 00:36:09 Okay, maybe I'll just put a note on there, like…
Trent Mick 00:36:13 What's the separate chunks?
Jamie Danielson 00:36:16 There's a way to split this PR into… separate PRs.
Trent Mick 00:36:23 I mean, if it's just covering one segment of the OpenAI API, then… Breaking that down doesn't feel… necessarily… I don't know, I haven't looked at it. I'm one of the maintainers, or the code owners, so I guess I should take a look.
I haven't yet.
Jamie Danielson 00:36:40 Oh yeah, I guess this is what Hector had said, too. I'm not sure if it will be easier splitting it in different PRs.
Trent Mick 00:36:44 Oh, breaking source instrumentation. Yeah, I mean, that's possible too. Is that file huge?
Jamie Danielson 00:37:02 It does add a thousand lines to that file.
Trent Mick 00:37:05 Which is… a lot.
One thing I worry, too, about, I guess, this instrumentation is… importing a lot of the types from OpenAI. I mean, if they start breaking those, then it gets really hard.
But then also having your own shadow types for… Types was a huge pain in the ass, too, so… I don't know.
Jamie Danielson 00:37:29 Yeah, especially if it gets out of date.
Trent Mick 00:37:37 An OpenAI package, at least.
I haven't been following it for a number of months, but it does move pretty quickly.
Yeah, there are some bits of source instrumentation, TS that could move out to utility.
Files, or separate files.
They're sad.
Jamie Danielson 00:38:24 Okay, I can move on.
Trent Mick 00:38:26 I don't know.
Actually, they definitely should have moved it.
So that's huge.
Marc Pichler (Dynatrace) 00:38:50 I wonder if that might be… If there might be some feedback that, may be valuable to… the Gen AI SimCon folks that… it's kind of difficult to work with. I'm not sure, I've never used the telemetry generated by that, and I don't know how many, how many Sikhs have implemented that yet.
But it definitely seems to be a bit unwieldy.
Trent Mick 00:39:29 So I think there are 3… in Gen AI, 80% of the attention is to Python, so… mostly you'll look at what Python's doing. For the OpenAI, their, library, their instrumentations for Java and JavaScript as well. And then, there are… third-party instrumentations for a bunch of these things, so I think, like, the Langchain world has Some instrumentations for this as well, or is it not like… I don't know, there are a bunch of them.
It's a busy space, or at least it was when I was attending the GenAI SEM Comp.
Yeah, I don't know.
I can take a look at this in the new year, but it won't be this week.
Jamie Danielson 00:40:19 Yeah, that's fine.
Alright, that's probably enough on that one.
There is… Topic, if we want to hop back to that for a sec.
From Trent?
Trent Mick 00:40:37 Oh, if we were gonna do a contribib release, because there was the P1 fix in OpenAI instrumentation.
Surprise, surprise.
Did we have a new package? I can't remember, because if we do that, then that requires you, Mark, so we definitely would have to do this today or tomorrow or something.
Marc Pichler (Dynatrace) 00:40:57 I also don't really recall if we had a new package…
Jamie Danielson 00:41:02 The last.
Marc Pichler (Dynatrace) 00:41:02 the packaging.
Jamie Danielson 00:41:03 I remember was when Marillia added the config, but that's already published, right?
Marylia Gutierrez 00:41:08 I don't think it is, because the… at least the issue mark is… it still marked as open, and as a release blocker, but that is on the core report.
Jamie Danielson 00:41:17 Oh, that's on core, not control.
Marylia Gutierrez 00:41:19 Yeah.
Jamie Danielson 00:41:19 Sorry, okay.
Marc Pichler (Dynatrace) 00:41:20 So, I think we won't do a core release, this year still, Because many people will be out, and probably best to keep… What we have now.
But for a con trip, I think we should… we should do one. If… There is a new package, and we don't… included in… I think I know which one is new. There's probably… one of the browser instrumentations that will be new. So, I can publish one of these.
I guess we should just sync… when releasing, it will stop on the publish step anyway, and that will give me time to, publish these packages manually, and then I will approve the publish step, and we should be good.
Jamie Danielson 00:42:25 Okay, that is this one, this is the new one.
Trent Mick 00:42:28 The browser navigated.
Marc Pichler (Dynatrace) 00:42:28 So, yeah.
Trent Mick 00:42:30 Yep. Okay.
Alright, so, okay, maybe later today I'll get that started, and then… You can finish it up tomorrow if it's stuck on you.
Marc Pichler (Dynatrace) 00:42:41 That sounds good.
Jamie Danielson 00:42:49 Okay.
Okay.
Dependencies… It's context propagation via session action.
Okay, just waiting for a review from code owners right now.
Oh, this is the Oracle DB, yeah.
If I remember, yeah, we were suggesting not making… some cheese.
Marc Pichler (Dynatrace) 00:43:31 I want to follow up on that one. I did not do it yet. It's still the same state as, last time we looked into this one.
I… Try to get back to this as soon as possible.
It's relatively low on the priority list, because it's just changing the way we manage dependencies.
Jamie Danielson 00:43:57 Yeah, that's fine.
And this is another… Similar thing of… Getting CI environment updates quicker.
And removing the need for them to be approved, to be created.
Marc Pichler (Dynatrace) 00:44:17 Yeah, this is mostly GitHub Actions, I think.
Because right now, you need to approve GitHub Actions updates in the, dependency dashboard, and with that removed it, with this new Match Managers rule, it would.
Jamie Danielson 00:44:37 Oh…
Marc Pichler (Dynatrace) 00:44:37 Allow those through.
Which… Yeah.
Also, has a bit of a, There's a caveat with that, which is, if you… have your GitHub Actions updated quickly, then that also means that if somebody messes with tags on, like, third-party, actions, you will get this update immediately, and… RenovateBot's action, or RenovateBot's workflow runs are triggered automatically, so it might… run a malicious action in a repo context.
immediately when the… when the update is published and RenovateBot first runs, so we would probably want to have, few days of delay with updating GitHub Actions.
Jamie Danielson 00:45:37 Especially with some of the issues I feel like we had this fall. Like, not we specifically, not OTEL, but just JavaScript in general.
Marc Pichler (Dynatrace) 00:45:44 Yes.
Jamie Danielson 00:45:45 a few.
Malicious attacks that have been pretty widespread.
Marc Pichler (Dynatrace) 00:45:49 Yeah, it might be worth doing that for, NPM packages as well.
To just wait for a bit until we actually pull these into, dependency update PRs.
We do have tester versions, of course, which will… Take the latest ones anyway, but at least this way we could reduce the surface a little bit.
Trent Mick 00:46:17 Do you know what the renovate setting for that one is? I think it's called Cool Down in Dependabots Config.
Marc Pichler (Dynatrace) 00:46:22 some… something like that. I think it's, You can set the age of some of the packages, somehow.
Jamie Danielson 00:46:40 Minimum release age.
Marc Pichler (Dynatrace) 00:46:43 Yeah, exactly that one. So I guess we would want to have that, at least for the actions, I'm not sure how many third-party actions we use, but… For the ones that we do use.
Might be.
worth just, delaying that a little bit.
Anyway, I will summarize my thoughts and, put a comment there.
Jamie Danielson 00:47:22 Dependencies, lock file maintenance… Release main… dependencies… Multi-pipeline…
Marc Pichler (Dynatrace) 00:47:39 Oh, I thought I had to… I did look at this one for instrumentation radis, but not I.O. Redis yet.
I will assign myself to this one.
swear…
Jamie Danielson 00:47:51 Okay.
Marc Pichler (Dynatrace) 00:47:52 Since I have the context… From the other PR.
It's essentially just a, requirement by the SEMConf.
That… Spans should be named accordingly, when they run in this multi-pipeline thing.
Trent Mick 00:48:26 Is that adding batch to the name or something like that?
Or I guess it could be multi.
I think the language in the spec was batch or something appropriate to this specific database.
Marc Pichler (Dynatrace) 00:48:37 Yeah, I think it's, with your exec, and I think it's, specified for that, for, for Redis.
Trent Mick 00:48:46 Okay.
Marc Pichler (Dynatrace) 00:48:48 I think it even says, like, at a pipeline, or…
Jamie Danielson 00:48:54 Yeah, down here.
Marc Pichler (Dynatrace) 00:48:55 Yep.
Jamie Danielson 00:48:57 Somewhere.
Marc Pichler (Dynatrace) 00:48:59 So that's the, link to SamConf.
Trent Mick 00:49:03 Yeah, it does say their DB operation name should be multi or pipeline for those cases.
Marc Pichler (Dynatrace) 00:49:09 And DB operation name, influences the span name as well.
Trent Mick 00:49:16 If I recall correctly.
Yep.
Jamie Danielson 00:49:30 Okay, so Mark, you said you were gonna take a look at this one, but…
Marc Pichler (Dynatrace) 00:49:34 Yes.
Jamie Danielson 00:49:34 Should be pretty straightforward.
Marc Pichler (Dynatrace) 00:49:36 Yeah, especially since I've seen the other one already, it's, basically the same thing again.
Jamie Danielson 00:49:45 This one I know we talked about last time, and the main thing was… Using ignore instead of skip.
And we're just waiting to hear back from the author still.
Okay.
There's a draft… patches. This one, we do want to… Review.
There has been some recent updates…
Trent Mick 00:50:31 I'll probably take a look at this later today, too.
Jamie Danielson 00:50:33 Okay.
Trent Mick 00:50:34 Because it's in the way to some kind of stuff.
Jamie Danielson 00:50:36 Yeah.
Okay.
And they're pretty active, I think this is the author, right? Yeah.
Trent Mick 00:50:43 Yeah. Looks like. So, cool.
Jamie Danielson 00:50:47 Parent name and attributes of resolver span. GraphQL.
Try and drive performance metrics from GraphQL traces.
I've added graphql.parent.name to the attribute names enum.
So the thing that's funny about GraphQL, I think, is that I don't think our attributes currently match SEMCOM.
But SimConv also isn't.
Stabilize.
If you can hold on.
Trent Mick 00:51:47 Yeah, correct or not.
Jamie Danielson 00:51:55 Is that a thing at all? No.
It's like… So… If you will. Operation.name, yeah.
Identified by the combination of its parent type name and field name.
So… It's hard because already we have all the attributes that don't really match anything, but I'm inclined to say that if we're gonna add anything new, it should probably be defined in semantic conventions, and so maybe this should be opened as an issue in semconf to add this.
thing, I don't know if they would add it, though.
I don't know graphics well enough.
Marc Pichler (Dynatrace) 00:53:30 I think if it's not in semantic conventions, then we should reject the change.
Unless, that's part of some sort of, prototyping or something like that.
I guess this is also one of those things where, like, a latest experimental thing would help.
Maybe?
Tool.
Jamie Danielson 00:54:17 We need latest experimental for all of them, but it's not even… this is not even an experimental yet, though, right? So that would be the first step, is…
Marc Pichler (Dynatrace) 00:54:25 Oh, there are no… there's no GraphQL…
Jamie Danielson 00:54:28 Well, there is, but not this. Not what this person is asking for.
Marc Pichler (Dynatrace) 00:54:32 Yeah, sure.
But, what I was… what I was trying to… get it, boss, if… changes to SIMConfarm made, we… Probably wouldn't be able to move very far with it anyway, so having the experimental the latest experimental stuff would allow us to give them what they want, if it also gets merged to SAMCOM.
Because right now, they might go to SEMConf and get the change in, but we can't do anything.
Jamie Danielson 00:55:12 Yeah. Well, yeah, I guess it would be… One step at a time.
I guess there are a few.
Trent Mick 00:55:21 Can we.
Jamie Danielson 00:55:21 Can we not?
Trent Mick 00:55:23 I guess I'm not… I don't grok with the… line is there. So, like, staying… if we're not talking HTTP, and we're not talking database, where there's some… work that's been done to stabilize some of the CENCOM. So, we're in GraphQL, and say CENCOM adds a new a new span attribute to its definition. Could we not add it to our…
Marc Pichler (Dynatrace) 00:55:54 Yeah, stir…
Trent Mick 00:55:55 incremental… Instrumentician.
Jamie Danielson 00:55:58 We.
Marc Pichler (Dynatrace) 00:55:59 I think we can do it, yeah.
Jamie Danielson 00:56:02 we don't really have guidance on it, so I had opened this PR last year, asking, like, what should we do? Like, if it's a library-specific attribute, does it have to be in SEMCOM, right? That's basically what you're asking, is like… if this is, like, a thing that makes sense… seems to make sense with GraphQL, or you can't get every single… Library, like, if there's… like, in the case I put in here, I think it was, like, Express. Like, we're not gonna have Express-specific… semantic conventions.
But… is there a scenario where people find it useful to have certain attributes Generated by the library that someone can opt into.
And that's kind of like… The idea here, just experimental opt-in YOLO.
Whatever the telemetry authors decide to put in.
I want it.
Otherwise, it could be…
Trent Mick 00:56:59 I wonder if another kind of less morally outrageous out would be to provide a… a hook.
Jamie Danielson 00:57:06 Yeah, I was just gonna say that.
Yeah.
Trent Mick 00:57:08 And it's like… You know, go crazy, add your own, but they're not… Where SimConf.
Jamie Danielson 00:57:14 Yeah, add custom attributes.
Trent Mick 00:57:17 Right, but whatever name we ended up tending to use in other states.
Marc Pichler (Dynatrace) 00:57:20 Speaking of that, do we… do we actually have… I… I think we have such a hook in the GraphQL instrumentation already, right?
Maybe I'm just…
Jamie Danielson 00:57:32 I've seen it in a couple of the.
Trent Mick 00:57:34 A response?
Jamie Danielson 00:57:35 Fuck.
Trent Mick 00:57:35 book that allows adding custom attributes based on data returned from execute GraphQL action.
Marc Pichler (Dynatrace) 00:57:42 That'd probably…
Trent Mick 00:57:43 Code here.
Marc Pichler (Dynatrace) 00:57:45 They probably wouldn't have access to the data that they need to derive that information here.
Trent Mick 00:57:51 I'm not sure, they just need that GraphQL info.
Marc Pichler (Dynatrace) 00:57:56 Hmm.
Trent Mick 00:58:04 Okay, it's given the span and the result, so no, it doesn't have the information that needs. We're assessing for the thing.
Where's this simple thing?
Jamie Danielson 00:58:48 Add parent name and attributes of resolver.
Trent Mick 00:58:55 So, I'm showing my GraphQL ignorance here. This is on a resolver span.
Or on the code path for creating resolved responses, as opposed to this response hook, I think it's for… The existing option is for execute.
Operations? That's what I saw. That's why I was just trying to reread this, because it says it executes the same account name resolver.
Jamie Danielson 00:59:20 This is also the same for me, though.
Ignorance and GraphQL.
Lingo.
Trent Mick 00:59:25 Okay, so I don't know if it's… yeah, I don't think it's covered… possible to do with the current response hook.
I don't know.
Jamie Danielson 00:59:37 Throughout time, I want to look at this a little bit.
more, because I'm also curious if it's just something that exists.
Like, that can be added downstream, like in a collector or something, if there's a way of… Seeing what's there, but… I don't wanna hold people up for that.
Thanks everyone for… Coming?
Hope everyone has a good winter break.
And see you online in… in the new year.
Marylia Gutierrez 01:00:06 Yeah, I created… I created an entry for both days, and put, like, no meeting. Because I know that people sometimes copy the calendar, and they would not notice that we deleted all the meetings from the official one, so just in case someone shows up, I put in the message there.
Jamie Danielson 01:00:22 Oh, smart. Thank you so much.
Marc Pichler (Dynatrace) 01:00:24 Thank you.
Jamie Danielson 01:00:25 Here, just to…
Marylia Gutierrez 01:00:27 Yeah, I put it.
Jamie Danielson 01:00:29 Lovely. Thank you. Good idea.
Alright.
Happy New Year.
David Luna Bistuer 01:00:38 You too.
Trent Mick 01:00:39 Yup.
Happy.
Marc Pichler (Dynatrace) 01:00:40 Bye.
