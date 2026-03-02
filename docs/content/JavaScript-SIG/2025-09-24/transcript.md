SIG: JavaScript SIG
Date: 2025-09-24
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/8ygFncpbTcZXBwJ7IF4-Rl8sPJ67Hkzf24tRt9adX9jzCQ_2mC7Hn9T7IotnRwQ2.O3u4o7I-CfJljqPO
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:01:47 Hello?
H.
It looks like, we can get started.
The first thing on the agenda is me saying thank you to everybody who has been reviewing pull requests over the past few weeks. We have gotten
from time to time, even below one page of PRs on both repos, which is, I don't think something that I've seen
Since I joined the project, so,
Yeah, thanks everybody for reviewing PRs and merging them in.
Yeah, just huge, huge thanks to everybody, and…
That is it for the first… -Oh.
green here.
Yeah. The next one is,
Andre, any plans to graduate the experimental packages to a Proper major version.
Yes, do you want to…
Andrei Borza (Sentry) 00:03:39 Yes.
as I said, it's quite hard for library maintainers, instrumentation maintainers, to rely on these.
For example, Prisma is still on 203, so… yeah, you end up with diverging, packages, and…
It can lead to problems.
Would be easier if we had proper 1.0 major versioning.
Yes.
Any plans, any recommendations?
Marc Pichler (Dynatrace) 00:04:10 So, there are plans, actually, it's just that, like, actually stabilizing the instrumentation package is blocked on other work.
So we cannot mark the instrumentation package as stable as long as we have, experimental dependencies there. So, we have to kind of wrap up the problem from, like, the…
Dependencies first, and then, we can actually…
actually graduated to a proper major version, as you said. So, one of the main things that is actually missing right now
East, Let me check real quick…
One thing that's for sure a problem is the API logs package, which the instrumentation package depends on.
So that is something that we have to, deal with first, and once that is done, we can actually think of,
Oh.
we can actually think of, also stabilizing this package. So… to get.
Andrei Borza (Sentry) 00:05:26 Installment here.
Marc Pichler (Dynatrace) 00:05:27 Cool.
Andrei Borza (Sentry) 00:05:28 Sorry. Yeah, go ahead.
Do you know off the top of your head what's missing there in API log?
Marc Pichler (Dynatrace) 00:05:33 Yes, so we have this milestone.
Where is it?
Logged API SDK GA.
these are the things that, still need to be done. It's not a lot, mostly, just auditing stuff.
And, like, once all of that is done, we will request a review from the GC, not the GC, the TC, tool for them to have a look if everything we did is SPAC compliant and,
Or sort it out.
And once that is done, we would actually…
then retire the API logs package, and move everything to the proper API package.
In that case, then, we would be able to get rid of the dependency in the instrumentation package. And since we don't depend on the Shima package anymore, since a few versions back.
There's not a lot that would then prevent us from, stabilizing the instrumentation package there.
Andrei Borza (Sentry) 00:06:43 Does that mean API is gonna get a new major as well?
Marc Pichler (Dynatrace) 00:06:47 API is not gonna get a new major, because integrating the logs part is basically just a new feature.
Andrei Borza (Sentry) 00:06:53 Okay.
Marc Pichler (Dynatrace) 00:06:53 So, yeah, it's…
There's… there's nobody to be broken, because there was nothing to implement yet, so adding it there, should be… should be fine.
Yeah, but that's basically the gist of it. It's just…
Andrei Borza (Sentry) 00:07:11 Okay, cool.
Marc Pichler (Dynatrace) 00:07:12 We need to do dependencies first, and then we can,
Actually graduated the instrumentation package there as well.
Andrei Borza (Sentry) 00:07:22 There… sorry to go on with this, is there anything we can help with here?
world.
Marc Pichler (Dynatrace) 00:07:31 I think, this PR here has started.
Mostly because…
the… oh, this is not the PR yet. There's… there it is. This PR, for example, has started and needs somebody to take it over. It's just a way to figure out how to handle circular references and stuff like that in the attributes type.
Then there's also… so, so the problem here is only that,
it's in the wrong package, so the actual validation is done in the API, which doesn't contain any,
any,
or doesn't contain a lot of business logic, usually we push that down to the SDK. And that's something that needs to be done, and then…
we have a review of the API logs to remove any unnecessary exports. This is also something that can be done,
just need somebody to go over stuff and see if there's things that are just there for testing, and figure out clever ways to work around that so that we don't have, like, a large public API that's really just there for internal testing.
And,
This one, we still need to contact the browser folks about, but I guess overall, there's not gonna be much that we will change here.
Yeah.
I guess the first two are ones that need help right now.
The rest is mostly audit and stuff like that, so we're just…
Need to take our time, as maintainers to go over these, once the other two things are done, and, make sure everything's sorted out there.
And then… yeah.
This should be good to go.
Andrei Borza (Sentry) 00:09:38 Okay, thank you.
Marc Pichler (Dynatrace) 00:09:40 So, timeframe-wise, after these two things are done, I reckon…
Two to three months, usually, getting the…
getting the TC to review it. I'm not sure exactly what sort of timeframe we were looking at there, but
Yeah.
That's it.
Andrei Borza (Sentry) 00:10:07 Cool, thank you.
Marc Pichler (Dynatrace) 00:10:09 Okay.
Yeah, having… having it stable is… is something that,
will be really good. It's been experimental for way too long, and
Wrapping these things up will help us as well in the country repo quite a bit to better deal with things going forward.
Right.
Any questions?
Comment, concerns?
Notice… If not, then I guess we can move on.
To the next thing, there's just some ongoing publishing issue, in Contrib. I created a new
published workflow and had a typo, and what that did was it created all these great new releases without packages on NPM, so I'm trying to figure out,
how to sort that out without it looking sketchy. So if you run into that somewhere, that's on me, and I'm looking into what to do, to reserve this. My current idea is that I will
Create a new patch.
release… And… Yep.
just states that the previous release was a bad one, and…
publish the packages to this new patch release, so there wouldn't be any instrumentation document load B0.51.0 on NPM, but there would be one with
051.1.
And then I would go and update these releases to state that this package won't be on NPM, package version won't be an NPM to…
Let everybody know that that's what's happening.
Does anybody have any… Concerns.
about this approach.
Or maybe alternative approaches that you can think of right now.
Trent Mick 00:12:31 Probably not, still trying to catch up, but yeah, no, whatever you decide is great.
Marc Pichler (Dynatrace) 00:12:37 Yeah, it's kind of an unfortunate situation. I don't wanna,
go in and, like, I can re-tag them to…
Can move the tags around and have it published from the latest commit there, but changing the tags on a already live
or live on GitHub release, probably looks sketchy as well.
Trent Mick 00:13:06 Yeah, I wouldn't do that. Yeah.
Marc Pichler (Dynatrace) 00:13:09 Kind of… Not too,
keen on actually doing that, so…
The patch release would be the one thing to do.
Pink.
Trent Mick 00:13:23 I think it's release.
Marc Pichler (Dynatrace) 00:13:27 Alright, and that's what I'm going to go with after this meeting right now.
Alright.
It's… hop onto, park triage. If you have any topics that you would like to discuss.
please feel free to just put it on the agenda while I'm talking, and then interrupt me, and then we can go back to talking about your topics here.
Looks like SDK shutdown does not flush logs.
I'm asking for, more minimal reproducer.
I guess it should be fairly simple to actually try this out.
Trent Mick 00:14:44 I'm not sure we have. They're doing it on… on process.onexit, the link that they have there, the… the second link.
It's in that same file, but yeah.
Process. On exit is… You can run something synchronous.
But then the process is gonna end, is my understanding of the node.
exit event.
And so that doesn't allow flushing to happen, because flushing's… I think async, right?
It has to be.
Marc Pichler (Dynatrace) 00:15:16 Yeah.
Trent Mick 00:15:17 Where's their shutdown telemetry? So…
Yeah, await SDK.shutdown. So, if you want to do something like this, you can use before exit, which…
Works, but you gotta be aware that it's async, so during the…
Turns of the event loop between before exit and exit.
There might be another log event that gets thing, and you're always… you're never going to be able to fully flush unless,
I think. So that depends on whether things are sequenced really well. But,
A potential answer to them would be to try before exit, and that would handle…
Allow, I think the before exit handler can be…
an asynchronous function, and I'm not sure if NodeCore will actually wait for it.
Marc Pichler (Dynatrace) 00:16:12 Wonder what we do in,
What is the auto-instrumentations node?
Trent Mick 00:16:23 Yeah, we used before exit there.
Marc Pichler (Dynatrace) 00:16:26 I'm registered.
Trent Mick 00:16:27 in sourceregister.ts.
Marc Pichler (Dynatrace) 00:16:30 Yeah, these two.
I think I'll just, put a comment here saying…
This is what we do.
There's a different…
keyboard in the room that I'm in right now, and I'm just looking for the proper keys here.
Oh, dear.
We're looking at this.
Oh my god.
I wonder if there are, like, some…
It seems like they are, actually working on this.
And then we can see if… Take it.
pick tool, to us here. I think there's also some recommendation of what to do.
here.
But… it's missing the before exit, so maybe I should try to add this.
Trent Mick 00:19:01 Yeah, that's older, the before exit was added.
Later.
In…
that PR, which adds a little bit of color, but, I can follow up with another comment there if you want.
And I think Aaron… Aaron asked for a better repo? Was that him?
I think Aaron was the one to add that code to…
Yeah, Aaron was also the one that did that PR link that I gave that added before exit, so…
You know, sir, as well. Okay.
Marc Pichler (Dynatrace) 00:19:48 I went to the wrong one, we're not finished here yet.
Yeah, this is still, pending some discussion of, which…
Which bundlers we want to support, and in which versions.
Yeah, this needs some more discussion as well.
Finally.
And this one here is,
Where we are blocked on JavaScript language features.
Hmm.
Okay.
Alright, that's the core repo.
We can move on to contribute. I had, commented on this one before. It was a bit, was opened in the corridor and didn't really have a lot of information on it.
it… still doesn't have a lot of, information on it, I'm not exactly sure what…
They expect to happen.
I guess what we need to do here is we just need to go in and ask a few more questions.
I did look at their output before, and…
I'm not sure if they're just not getting anything from IO Redis here, or… Something else…
It seems that none of the, the instrumentation scope actually reads the IO readis, or has the IO readis, thing on here.
So… I guess that's what's happening for them.
Oh, dear.
difficult tool.
There you have just the information.
That's on here.
What's it?
Yeah, and I guess we need to also dig a bit deeper into what's going on here.
But… That needs…
Some more info, for sure.
Then this one is… Soka.io and this.js.
Platform socket I.O. integration doesn't work.
And it seems… To me, like it is… P2.
Since they expect to see something, but they don't. But it doesn't seem that,
It doesn't seem like there's actually… Anything breaking on their end?
We're not etching these two functions here.
Which is very likely, because I don't recall a lot of PRs landing in the socket I.O, thing.
Over the past… Yeah, so at least, I think. So…
It's very likely that an initial version of the instrumentation didn't, didn't instrument that.
I'll put a socketail labor on here, and,
Yeah, if anybody has time to look into this one, that would be very much appreciated.
Let's just check who actually is the component owner for that.
And let's just ping them real quick on here.
Trent Mick 00:28:05 So this wouldn't be a bug, it'd be a feature request, basically, right?
Arguably, if I don't know.
Marc Pichler (Dynatrace) 00:28:11 Yeah, it's… it's always difficult to say with these, like, telemetry is missing, and we added a feature to,
Telemetry is missing.
for,
A library that we already instrument for features that might or might not have been there in the version that,
was out when we instrumented the package. I'm always having a bit of a difficult time classifying these.
I guess we can go either way, either it's a feature request or a bug.
I think in the past I have handled them as bugs every car.
working on something in the gRPC instrumentation a while ago, where,
like, some library was using it in a different way, and we hadn't instrumented that, and I seem to recall that this was…
Or I should label it as a packet then.
Alright, that's this one here, and then there's another one.
Which is labored as… needs of the response.
I'm not sure why I put needs author response on there that actually needs response from… Component owner.
Yeah, that's still… Oh, nothing… here yet.
Alright, guess that concludes bug triage, and now we can move on to, old PR triage.
Looks like there was no movement here. The next one is… HView Instrumentation.
Well, I'll be net, actually.
fix the conflicts, but there's so much churn in the package lock, Jason that conflicts reappeared probably immediately again.
That still needs some…
Look, it seems…
I guess we'll leave that, be for a bit longer, and then circle back to it.
At some point… This year also didn't seem to have any cha- have had any changes.
David reviewed this… Recently… To just get it updated to the latest,
Way that our, workflows work.
There's also nothing to do yet for this one.
I guess there's also a question of do we…
I'll actually ping the person that opened up PR and see if they…
I've had some time to look into the, comments.
Trent Mick 00:32:57 If we think it's mostly just meta stuff, like, we've changed.
Basic structure.
that's not specific to the SQLICE thing, then… Is that your understanding?
what it is.
Marc Pichler (Dynatrace) 00:33:09 I think it's mostly that, but also, I don't wanna add an instrumentation where
The component owner that's being added is unresponsive.
So…
Trent Mick 00:33:26 I think we have… yeah, I don't know.
I don't know what their names seem. He's…
He's sometimes responsive, and he's, like…
Marc Pichler (Dynatrace) 00:33:34 Yeah.
Trent Mick 00:33:34 he's doing other PRs and related stuff, so I think he's around.
Marc Pichler (Dynatrace) 00:33:40 Yeah.
Trent Mick 00:33:41 Why don't you… give me a to-do on this one, I'll take a look at some point and see if it's just…
unrelated meta stuff, then I can update the PR.
So he doesn't have to learn all these other… Changes that we've done.
Marc Pichler (Dynatrace) 00:33:56 I will… do you mind if I just assign you to the PR?
Trent Mick 00:33:59 Yep, yep, that's cool.
Marc Pichler (Dynatrace) 00:34:03 Alright, thank you for… Picking just one.
aren't… And I guess we can move on to the next one, which is web exception instrumentation.
If I recall correctly, this one was waiting for component owners to be added onto the PR.
But this still looks like no component owners for this one.
-Oh.
I'll just assume… One of the new browser maintainers.
Doesn't seem like there was any movement here, but let's keep this one open for now.
I don't know.
This one, I haven't had the time to actually look into, because I was working on other workflow changes,
But… I think this should be…
Okay, now I had to review it.
Hector Hernandez 00:35:30 Yeah, this one is complicated, because I cannot validate. I'm just making I'm hoping it works.
Marc Pichler (Dynatrace) 00:35:37 Yes, so… Yeah, I, I feel your pain.
With these sort of things, it's always kind of a bit difficult.
Hector Hernandez 00:35:56 Yeah, he addresses the comments. I think we just need to kick it off to see how it goes.
Marc Pichler (Dynatrace) 00:36:01 Yeah, I had reviewed this,
before already, so I'm just gonna have a quick look here.
Looks good.
I kind of need to approve to… Get the thing to run.
Gotta check the action run here.
of repo up here has not been set, and it looks like…
there's… Still something wrong here.
Hector Hernandez 00:37:08 Yeah, we'll take a look. Looks like it didn't run.
Marc Pichler (Dynatrace) 00:37:11 Okay.
Yeah, thank you, for… for working on this. I put,
I dismissed my review and put the changes requested.
Sounds good.
I forgot now what it… what it was. This looks like. There's… Something…
Alright. This,
with me approving and disapproving starts looking quite silly, over time, but, guess that's the only way that we can try it out.
Alright,
And the next one is approved, but has a failing build.
See what…
Trent Mick 00:38:35 Oh, that boat. Oh, that's just CodeCov, who cares?
Sorry to be flippant. I think it looks good, I had a knit on…
Julia to maybe, tweak one error handling thing, so… I was gonna give her more time. I'll poke her at some point.
Marc Pichler (Dynatrace) 00:38:54 Alright, thank you. Yeah, I wouldn't want to merge it in right now anyway, because there's the stuff going on with.
Trent Mick 00:39:02 the releases.
Marc Pichler (Dynatrace) 00:39:03 is kind of pending right now, so I don't think I will merge anything in on the card today, but…
Trent Mick 00:39:10 Sounds good.
Marc Pichler (Dynatrace) 00:39:10 Okay.
Alright.
And we can move on to the next one.
This one I've, I think said that I was going to have a look at…
Some time ago, but still didn't get around to it.
Bailing on some lint step right now, which probably just, due to the changes here, should be fairly easy to fix.
Trent Mick 00:39:49 It's just prettier stuff, yeah. Most of them.
Marc Pichler (Dynatrace) 00:39:52 Yeah.
Yes, this is probably nothing that we can review right here. I know I've said that quite a few times already, but
Stuff keeps popping up that,
Needs to be addressed right away, so…
Yeah, hoping to get to this one soon.
Trent Mick 00:40:17 Same.
And I agree, we can't… Fully discuss it now.
Marc Pichler (Dynatrace) 00:40:26 Right, this is… Also, some larger changes, or, like, larger changes to the ESM.
Built, did we…
I think we agreed to discuss at some point when David's around, so we'll skip these as well.
Let's renovate PR, draft PR… There's one PR about… adding Staber Semconf to the…
instrumentation AMQP, but we had, looked into this at some point, and…
The messaging semantic conventions weren't actually stable yet, so…
We're kind of in a weird state right now.
I guess the question is, do we leave this PR open?
Or…
Trent Mick 00:41:41 Are we… so…
not necessarily related to this one, but are we necessarily blocked on waiting until messaging is stable before moving it? Like, we have…
this thing was last seriously worked, I'm guessing, here a little bit. Last seriously worked on a long time ago, and since then, there's kind of a significant change in messaging, semantic conventions, and yes, it hasn't been stabilized yet, because…
They haven't gotten there over the course of time. I don't know.
But it could be that there's messaging stuff is still…
will have some upheaval and stuff, but I'm guessing it's mostly just because they did HTTP, and then databases, and then…
Over the course of time, I'll get there, but, like, Technically, we could just…
Get closer to the current state of messaging and wouldn't have to be blocked on it, right?
Marc Pichler (Dynatrace) 00:42:33 Yeah, I think technically we can. We could always update it without the environment variable. There's nothing that really blocks us from it.
Trent Mick 00:42:47 Oh, yeah, this one is talking about using the… the…
the opt-in thing. I agree we wouldn't use the opt-in thing yet. We'd just, like, switch it and say, sorry, dudes, breaking change.
Marc Pichler (Dynatrace) 00:42:58 Yeah, so that would definitely be possible. One thing that…
this would also do is, should the messaging spec, get stabled at some point, in the future, we are way closer to
The actual thing that we want to have, so we might not even need the opt-in thing.
Because we're so close already that,
Trent Mick 00:43:25 And it already maps, yeah.
Marc Pichler (Dynatrace) 00:43:28 So…
Yeah, I'm not… not opposed at all to, actually bumping the same conversion, I just think that we…
Would need to not do it via the, stupidity opting them far.
Alright, should I put a comment here? Let them know.
Trent Mick 00:43:55 Alright, Ken, if you want to move on, I'll add a comment.
Marc Pichler (Dynatrace) 00:43:58 Okay, thank you.
I guess we'll just move on to the next one.
This is, adding SQS context propagation.
There's some back and forth with the component owner.
It seems like there's a lot of context on here that we…
I would still need to read through.
It looks like there's some, disagreement on, all spend links…
could be used.
This was a decision that was made a long time ago, I think, for this,
messaging semantic conventions, I seem to remember…
That happening back more than a year ago already.
So it's kind of set in stone.
And, go.
Also, doing anything else with messaging is kind of… Difficult, to accomplish.
So, it makes sense to have the spendings there, as the mode of…
Creating telemetry for these things.
Looks like there's actually some inconsistency with,
what the Lambda spec is saying, and what the, what the actual…
Messaging spec is saying…
I'm not sure if there's anything that,
I would be able to read out right now from… the discussion here.
And give a thoughtful enough answer to reserve the situation.
Anybody have any immediate thoughts on this one?
If not, then I guess we'll move on for now, and we will circle back to that one at a later date.
Once we've actually read up on all the context that's there.
Right.
There's Renovate PR, then there's… Pr for the test store versions.
Things, seems like this still has failing tests, and they…
Probably didn't have time to get back to this yet, but, has had activity recently, so I guess we can still leave that open for now.
I think I did, yeah, this… Yeah, I actually… Started reviewing.
some point… Boom.
I'm gonna post my… Review yet.
There's quite a few different things that are happening in that, PR.
That's, yeah, makes it a bit difficult to…
Approve the, just the, the,
PR that adds the instrumentation skeleton, so just the package itself, because it's pulling in a bunch of dependencies that we aren't usually using in this repo.
So one of those… one of those is, chest.
And a few other, things that are a bit odd.
So… yeah, just… Need to figure out that first before we… Actually add this component.
Trent Mick 00:50:06 Had you… sorry, I didn't… I didn't follow that discussion at all. Had you asked them if they're willing to change to use smoking?
Marc Pichler (Dynatrace) 00:50:12 I… I think the review that I posted now has, some questions about, why using Jest.
Trent Mick 00:50:22 Yeah, if… yeah. I mean, if they're importing from somewhere else that was using Jest, I can understand that they started that, but…
Marc Pichler (Dynatrace) 00:50:28 Hmm.
Trent Mick 00:50:29 If it's…
Marc Pichler (Dynatrace) 00:50:30 Yeah, I guess…
Trent Mick 00:50:30 If they wanna, then yeah.
Marc Pichler (Dynatrace) 00:50:33 Yeah, I think they had, this instrumentation posted somewhere, and they are trying to basically move it here, so…
They probably had an environment somewhere where they could, just take on dependencies that they are used to, and then,
Upstreaming it into the repo is a bit more difficult, because there's just so much stuff happening, that it's…
difficult to align if it was first created outside, outside the contract repo.
And there's… A bunch of…
better decisions that one can make when starting off with a completely, clean slate. So I… I do understand the,
approach here, sometimes. Yeah.
Trent Mick 00:51:28 Okay.
Marc Pichler (Dynatrace) 00:51:33 Alright,
Then there's a draft PR with upgrading to ESLint 9.
Trent Mick 00:51:47 I'm curious if he's had some movement on that.
Last week.
Marc Pichler (Dynatrace) 00:51:54 Dainer.
Trent Mick 00:51:55 That's Jared. Jared's not on the call. Nice.
Marc Pichler (Dynatrace) 00:52:00 And I think the, tests aren't running because, there's conflicts.
So, I'm not exactly sure what the status is on this one.
Trent Mick 00:52:18 I can't push to that one. I'd been helping him on some things, including writing a new ESLint.
plugin to use for the license header check, but, it's a corporate branch, so I can't push to it to help.
Marc Pichler (Dynatrace) 00:52:32 Yeah, there is a workaround to allow that, and I think I let him know what the.
Trent Mick 00:52:38 there is.
Marc Pichler (Dynatrace) 00:52:39 on this.
Yeah, there's,
Let's see if the search is good enough.
Laura.
Like, if you do this, if you use this alias and then run it from…
your repo, root, then…
Trent Mick 00:53:12 So…
Marc Pichler (Dynatrace) 00:53:14 It does some tricky,
some tricks on the GitHub API to actually set that flag to true that's not exposed via the UI.
Trent Mick 00:53:27 Jesus. Okay.
Marc Pichler (Dynatrace) 00:53:28 It is a hack, but I was annoyed by my own situation, which is basically the same, that I also have to use an organization fork, and everybody wasn't able to update my branches, so…
when someone complains to me, then I have usually forgotten to run this, and… Yeah.
Trent Mick 00:53:54 Okay, good to know.
Marc Pichler (Dynatrace) 00:53:57 So, yeah, if you ever run into anybody, and you would like them to turn on maintainer edits, and they're okay with, actually letting you edit, then you can…
Refer them to this, sketchy-looking script that I wrote.
Alright, where did we stop now?
It's the ESLint, there's a lot of IO readies, going on, it seems like.
It already is cluster Instrumentation support.
Things like there's a bunch of…
Trent Mick 00:55:12 I wonder if he'd want
I wonder if there'd be a way to turn… anyway, this probably sounds like a good thing to review and get in. I wonder if it'd be…
A way to do this without…
There being a configuration option for it?
But… but I haven't looked up here.
Marc Pichler (Dynatrace) 00:55:32 So… You mean without, having to explicitly turn it on, just have it on by default.
Trent Mick 00:55:43 Yeah, I would think so, if it's a reasonable thing to do.
Why have… Because another config option is just another… Lurking corner for bugs.
Marc Pichler (Dynatrace) 00:55:54 Yeah, I agree that, probably having it on by default might be good.
on…
PR itself actually looks fairly…
Trent Mick 00:56:16 I was proposing new attributes, what does SEMCOMP say about that?
Are you allowed to just… Add whatever.
Marc Pichler (Dynatrace) 00:56:32 Yeah, I'm not sure if these actually exist, I guess.
It might, but… Yeah, this, needs some deeper looking into as well.
It is 3 weeks… oh, I opened 3 weeks ago already, so… It is fairly old.
I just want these… This one, we just had a look at, second to go…
I have another draft PR.
And there's one PR for instrumentation GraphQL.
Boom.
This actually just looks like, not a problem.
It's just some confusing output from…
Golfed.
It's passing… oh…
80%, which… Yeah, target agent.
Or target.
of 80%.
Oh, it looks like they pinged David on it, because, likely…
He talked to David for the previous PR.
These are resource spans under the same parent.
Instead of a nested tree structure. I guess this is a very similar, Very similar…
thing to what we discussed about in the, express instrumentation, where there was also,
They used to be, like, what is being proposed here.
Like, looked like this, but, actually a lot of people were… asking for…
this here, so I guess that's why there's an option to put all of them under there.
I'm not sure,
that's the route that we wanna go. It can be difficult to look at, I agree with, with the person, though, looking at,
A span that has so many nested spans that you cannot find what you're looking for is also kind of difficult.
I'm not sure if anybody has served, like, showing these, in a digestible manner.
But it looks like we're out of time today, anyway.
Thank you, everybody, for joining.
See you next week. And, yeah, if you have some time, please…
Continue reviewing PRs, that's always helpful, and, move stuff forward.
Quite quickly, as we've seen.
Thank you.
Trent Mick 01:00:34 drones.
Marc Pichler (Dynatrace) 01:00:35 House Month.
Trent Mick 01:00:36 Thanks.
Marc Pichler (Dynatrace) 01:00:36 Alright. Thank you, Aaron. Bye.
Andrei Borza (Sentry) 01:00:38 Thank you, bye.
