SIG: JavaScript SIG
Date: 2025-06-18
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:01:21 Hello.
alright!
Let's get started.
The 1st topic here is David asking for review on
the docker. Compose and test services scripts.
David Luna Bistuer 00:01:55 Yeah. As a Pr mentions, this is kind of a follow up for the previous work that trend has started. I think that there were a couple of Prs that tried to do that
so long story short, it's something that I need for my Pps. Pr. On the on on improving the the workflow.
Basically long story short, this adds a docker, compose file with the Mvars as well with another environment file. So you can test all instrumentations locally.
So just by running a command to start the services
Mysql or other databases and and services that are needed for testing and then run. Npm test at the root level.
Okay,
exactly. So you're gonna start the services. You're gonna stop them. And then you can run with the config so usually, all these limitations rely on a configuration environment bar to actually run the tests. So when these bar is set, they assume that the services is available and they use it.
So that's what the skip is doing. So it's loading the environment file and then run trying to run ambient test on all the yeah, it's the same that we have in the workflows.
There is also a change that I did in the workflows, because
there was a specific step just to set up my SQL.
To set up the log table.
which can be done, and move that to to
set up script in the in the may as well test itself.
So yeah, here, it's just you check the mask. My SQL.
Instrumentation. This one.
Yeah, what we are doing is in the before we are actually enabling this just for my SQL,
so we don't have to do it in the workflow.
They look
Marc Pichler (Dynatrace) 00:03:59 Looks really good already.
David Luna Bistuer 00:04:01 Yeah.
Marc Pichler (Dynatrace) 00:04:02 Thanks for
that. I know it's a common pain as well for people that are developing to run the tests and then
think everything's fine, and then license. Ci, and it doesn't work.
David Luna Bistuer 00:04:15 In my case it's a means to an end. So I'm happy to take the, you know, to take the pain. It's not finished. So what I have here is just, you know, the devil. Trans. Pr, I think it's better because it has also added scripts. And there was a discussion about that, but I don't want to get into that discussion yet. So my plan is to have then a follow up Pr, adding the the you know, adding the necessary scripts to just, you know, clone the repo, check out it.
CD into a an instrumentation, compile it, and just test it with the service, just only with the service that that it needs.
But that's in a different discussion. It's something different. And and I need that feature that I need it for the for the workflow especially because I need
to create the 1st report for each flag that I'm I'm I'm willing to upload to Codegov.
So yeah.
I will explain this also in the in that, in the workflow, pr, and and the issue as well.
So we've been on.
That's it.
Marc Pichler (Dynatrace) 00:05:24 Yeah, thank you for working on this. I will. Give this a look on Monday, most likely.
but yeah, it looks looks really good already, and it's definitely an improvement over what we had before. So thanks for working on this.
and as always, if anybody else has some some time in the meantime. Please feel free to head over to the Pr and give it a review.
Yeah.
Does anybody have any comments that they would like to add right away.
If not, then we can move on to Hector, looking for reviews on yeah, reduction.
Hector Hernandez 00:06:20 Yeah, to bring this up in. Today's sick meeting. I can see. Mark your review. Thank you. Yeah, she's just looking for more reviews here, and I saw your comment. And now I have a question you're asking for to add this experimental config. Is there a way to say I want to use experimental everywhere in the open telemetry. Is that something that you guys consider before.
Marc Pichler (Dynatrace) 00:06:45 We didn't. It is
so basically at the moment all the instrumentations are kind of in
weird state. Since, like we use the old Sam. Conf there's a bunch of old being emitted, and then, like most of them, are experimental already, but we try to get them as close as possible to a state where you know only stable stuff is being done, and you opt into whatever is experimental. And then
that's that's fine, and if you
need to turn it on, you would need to set a flag. I think what you're asking for is some sort of environment variable, right? So that.
Hector Hernandez 00:07:30 Yeah, something like that. The thing here is that we have been using experimental stuff for so long. Yeah, it's just normal for us. Right? So.
Marc Pichler (Dynatrace) 00:07:38 And he.
Hector Hernandez 00:07:39 Maybe just some way to turn it on.
Marc Pichler (Dynatrace) 00:07:42 Everywhere.
Hector Hernandez 00:07:42 And don't. Don't worry about the specific configuration and stuff like that.
It's just it's it's just some comment. I I was thinking when I saw your your feedback, but.
Marc Pichler (Dynatrace) 00:07:53 Yeah, I think. The way Java does it. There's like one option that you can set for like not all of them. But you can turn them on individually. I'm not sure if there's a way to to
turn everything on at once.
Yeah.
Hector Hernandez 00:08:15 That's fine!
Marc Pichler (Dynatrace) 00:08:16 That's fine!
Hector Hernandez 00:08:16 Maybe that's something we can discuss.
Marc Pichler (Dynatrace) 00:08:19 There there, if if needed. I I was just curious about it.
Yeah.
Doesn't. Oh, sorry. Go ahead, Trent.
Trent Mick 00:08:26 I, I was gonna say, like this is vaporware. But the path that I would see towards something like that is, if we implement file based config.
And for having that, we talked briefly about having some canned configs with
that call them profiles, or whatever. And maybe one of those could be. This is the one that sets all the
experimental thing. So it's a thing you'd have to maintain going forward. But it
that's a potential path for doing that. So it would still be individual configs for each of the things. But you would have this canned config thing that included all the turning on all the experimental things
that has a possibility of getting out of date, obviously because you'd have to keep up with
the latest canned file config. But anyway, that's potential.
Marc Pichler (Dynatrace) 00:09:19 And then, yeah, I I think for for this specific pr,
I'm not sure if we want to introduce that right now the easiest way to get this Pr in
at the moment would be to just
at the flag, and then we can figure out the details around like how we would turn, turn it on everywhere,
and go from there.
Or it could be also like splitting this Pr up into just the reduction for the
for the auth things, and getting that one merged and then
getting the experimental stuff in later. But as as long as the flag is there? I don't see any blockers for this.
so we could. We could move ahead
bit more quickly on on this, to at least get the thing in with the flag, and then figure out
what we do.
I guess one thing that we could do is have like an alternate
experimental something flag that one could turn on.
and that would turn on all the experimental things.
And then, later on, if if there's additional oh.
additional things added to the same conf that we don't want to enable for everybody yet that would also enable those.
But I guess it warrants more discussion before we do such a thing, because if we introduce it and it's being used everywhere, it will likely stick around for a very long time.
So I want to make sure that we get it right? Ish in the beginning.
Yes.
Does anybody have any comments about this?
Any concerns?
Or does anybody disagree with
the fact that we should, we should put it behind a flag. I wasn't sure myself, to begin with when I suggested it. So I'm open to other suggestions. If if you have any.
Daniel Dyla (Dynatrace) 00:11:57 Sorry I received a phone call at the start of this. So I'm coming in a little bit late. The the specification here is experimental.
Marc Pichler (Dynatrace) 00:12:05 Yes. So the specification for redacting these query string parameters by default is in development at the moment.
Daniel Dyla (Dynatrace) 00:12:14 Can we look at the word of the specification, real, quick.
Marc Pichler (Dynatrace) 00:12:19 Yes,
Daniel Dyla (Dynatrace) 00:12:28 Okay should be redacted by default.
Marc Pichler (Dynatrace) 00:12:38 That's a good choice of view.
Daniel Dyla (Dynatrace) 00:12:39 A case made for.
Marc Pichler (Dynatrace) 00:12:42 But you likely don't want these at all, anyway.
So they should be redacted.
Yeah, this this yourself.
Hector Hernandez 00:12:52 This came in our side. Some azure SDK customers were leaking as some tokens in there. So that's why we we.
Daniel Dyla (Dynatrace) 00:13:01 Yeah, I think so that there's a couple of ways that we could do it. We could have
a default list of redacted keys that then customers could override or sorry users could override.
We could have and opt in like a list of
a configuration that's like these keys will be not redacted, regardless of, you know, like the opposite.
add keys to a list in order to have them not redacted.
Or we could just have a flag that's like enable experiment or disable experimental
redaction. I think what I would do is have a
for now, since this is in development.
yeah, I mean, I don't know. I don't think any of these are, gonna be. I don't think people will complain if
we start redacting these by default.
And we don't have any instrumentations that are one dot. O, personally, I would just add the feature I wouldn't worry about.
Hi, yeah, I I don't think that this
specification is likely to go away. The exact keys might change, but I don't think any of these keys are likely to go away. I think it would only be a list that gets added to
so I would probably have a configuration for redacted headers.
and then have the default value for that configuration be the list of these 4 keys.
I guess what I'm advocating for is not a particularly careful implementation of this.
I think it provides a lot of value, and I think it's unlikely to be removed or reduced in any meaningful way. Here.
Marc Pichler (Dynatrace) 00:15:18 Alright, yeah, that I think also makes sense.
Then do you want to add a comment to the Pr, then I can.
Yeah, I'm
I I don't have like a strong opinion either way. And I think your argument makes sense. So once you put the comment, I would just
dismiss my earlier review with the
changes requested, and then we can go from there.
Daniel Dyla (Dynatrace) 00:15:48 Yep.
Marc Pichler (Dynatrace) 00:15:53 Blind.
So yeah, if anybody else has any
any comments, please head on over to the Pr. Give it a review and we can
move on with getting dismerged.
MG Marylia Gutierrez 00:16:19 I see that my questions being answered. Now, yeah, it's just because I got the I got a question someone was asking me like, Oh, is Hgp like fully supported now, like on the SDK. But I know that, like the migrations happening, some implementation still happening. So I'm assuming that we can say that is like fully supported after this. But I just wanted just to confirm that if this is doing for like traces and metrics.
Trent Mick 00:16:46 So yeah, that was me adding this link. So
Jamie had been kind of creating the Meta issues. And I've been doing some of the implementation. So I think the core repo instrumentations are all done and ready and released, and they support that the opt in thing. So we're currently in the default behavior is the old semantic conventions. And you can use the opt in environment variable to get either dual or the new stuff.
And then the link to the contribute issue. There points to the remaining
instrumentations that are doing. Htp related
using Htp. Related semantic conventions that had not yet been
updated to support the opt in environment. Variable. Yeah, I was kind of on doing that. And I'd set a
half joking deadline of
HP. Semantic conventions by Christmas, which means I have until June 25th to get Prs merged and released for these things. But I'm now thinking that's probably not gonna happen. So
certainly having other people follow the example of the instrumentation. Happy
Pr there and doing it for the other ones would be welcome. If other people want to pick it up.
MG Marylia Gutierrez 00:18:00 And but I think for the review on the database one. Now, I can just update the
the test as well. Yeah.
Trent Mick 00:18:10 Oh, right, definitely poke me. If you need another review on that, I'll probably.
MG Marylia Gutierrez 00:18:14 Yeah. Now, now that I know that I I was doing the right path, I'm just adding basically tests to see if the behavior works depending on the flag that you have, but then it would be done for.
Trent Mick 00:18:26 Nice. Okay. Cool.
MG Marylia Gutierrez 00:18:29 Okay.
next up is also mine. So yeah, just in case people miss this. And then I saw the can you share here? But I know that some containers know, but not everybody knows, that
Cncf slacks going away very soon.
The gist is, if you have something to save, say by this Friday, and very likely we would move to discord.
But yeah.
Marc Pichler (Dynatrace) 00:18:59 Yeah, thank you for the update. I had already seen this
this year, and the the post in the maintenance channel. I think it was yeah.
I guess. The card to action here is, if anybody has anything in slack that, they wanna save go ahead and do it now, otherwise it will be gone.
For now, I guess. Slack, we're still stick around. It's just a 90 day
time out of the messages that we have now where they age out and go away. But yeah, I guess it. We have to also be a bit more diligent to move as many discussions to Github as possible to make sure we have a paper trail for things.
Daniel Dyla (Dynatrace) 00:19:55 It also, disables any workflows or anything like that. So if you have any web hooks set up they will
go away.
I think we've been pretty good about not using the slack channel for development decisions.
Partially because the slack channel has turned out just not to be very good for that. But
I I think we're not as affected by this as we could have been. So yeah.
Marc Pichler (Dynatrace) 00:20:36 Alright thank you, Amelia, for bringing this up. I also put slack dump suggestion here.
which that's the the thing that people can use to
but dump all their dms and private channel info to
somewhere. I haven't tried it out yet, but yeah, messages might be going away soon, so probably best to do it sooner rather than later.
Alright, any additional questions or comments about this topic.
If not. Then we can move on to Andre's question here about Api. V. 2. Timeline.
Andrei Borza (Sentry) 00:21:34 Yeah. Hi, I just noticed this in the last week's meeting notes. I I'm sorry I didn't watch the recording yet. But did you discuss a rough timeline of this.
Daniel Dyla (Dynatrace) 00:21:44 There is, there is no timeline, there's no.
Andrei Borza (Sentry) 00:21:46 Yeah, I figured.
Daniel Dyla (Dynatrace) 00:21:47 There's no promise that anything will actually happen at all.
Okay, it's
that it. It is my personal prototype of what an Api v. 2 could be. There's no
there is. Yeah, there's nothing official about it. There's no timeline. There's no promise that it will happen, or that if it does happen, it will take this form.
It's just my brain dump of
a potential possibility that solves a lot of problems that we have.
Andrei Borza (Sentry) 00:22:22 Got it. Thank you.
Daniel Dyla (Dynatrace) 00:22:23 Yeah. Sorry for such a a hard cut. No on that. But I just I want to be very clear. I don't. I don't want people to. It was part of the reason that I it was private for a really long time.
because I didn't want anybody to.
You know.
I I was trying to avoid people posting on Twitter like our Maintainer of Hotel Js, says, V. 2, coming.
No, I'm sorry I'm not trying to pick on you. I'm just.
Andrei Borza (Sentry) 00:22:55 No, no, it's fine. We're, I think we're happy with it, not coming out too soon.
Daniel Dyla (Dynatrace) 00:23:01 That, said, there is a I'll put this in a doc. Actually, we should be talking about it anyway.
MG Marylia Gutierrez 00:23:10 I was. Gonna say, if anyone wants, we can always tag Daniel every single time someone mentioned Api just tag Daniel, that.
Marc Pichler (Dynatrace) 00:23:17 How it works.
MG Marylia Gutierrez 00:23:20 I hope.
Daniel Dyla (Dynatrace) 00:23:20 This browser phase, one project just merged it. This is what was the client instrumentation, Sig.
One of the things that they have in their list of items to talk about is any Api changes. They actually have a potential
browser Api in as like something to consider.
I am hoping to dissuade them of that
again. That's my personal opinion. That's not
But Api changes will be coming.
Whether it comes in the form of an Api. V. 2. With breaking changes, or an Api like non breaking changes to the existing Api, or whatever I think the only thing that everybody agrees on is that the existing Api
has severe limitations and problems.
That make it unsuitable for browser, at least and potentially
even unsuitable. For yeah, I, unsuitable, is too strong of a word, but for it's difficult to extend, I
in a backwards, compatible way
difficult to run multiple versions at the same time. Lots of version compatibility questions between multiple Apis in a process. And what SDK version am I using? And all kinds of stuff like that
that we want to address.
Will it take the form of my V 2 prototype? Most likely not. Just because.
you know, it would be somewhat surprising if they just took the the
the brain dump from one person had
and said, like, this is the new Api.
I think that would be just as much of a mistake as doing nothing. So
yeah, I made that public partially because of this browser project.
as a food for thought more than it is an actual plan.
Andrei Borza (Sentry) 00:25:50 Got it. Thank you so much.
Daniel Dyla (Dynatrace) 00:25:53 The browser phase one merged. We know we talked about this in the past. But the meetings are gonna be Thursdays at 8 30 Pacific, which is
2 30 Central European, and a different time. If you're in a different place
this Thursday, likely not. The 1st meeting, even though it was supposed to be, because it's a holiday in the Us. It's Juneteenth
next Thursday is Hotel Community Day, which interferes with
several of the important contributors. So possibly the 1st meeting will be like July 6, th
3, rd which is the day before 4th of July.
July 10, th would be the one after that. Yeah, who knows?
Not a very good time to start a new project. But these meetings will be starting. That's the time, Slot. I just don't know the day yet. I encourage everybody here to at least read the proposal like the the project proposal, and know what's going on, since this directly affects us.
And get involved, if possible, because.
it would be a shame if the 2 groups
continue to work as separately as we have been in the past. I think
it's it's already unfortunate how long we've done that. And I I think it's something that we can fix.
Marc Pichler (Dynatrace) 00:27:32 Yes, I do agree.
Thank you, Dan, for bringing that up. Yeah.
As Dan said, I encourage everybody to read the proposal, and if possible, and it works for you also trying the meeting to see what it's all about.
Does anybody have any questions or comments about this.
then select no?
Then, yeah.
Guess we can move on to bug triage if you have any
comments that you would like to add, or any other agenda topics. Please feel free to just put them in the document and let me know, and then we can go back to discussing your topics
in between pack triage, so feel free to just interrupt me while I'm going through the things here.
Alright. Looks like no new box filed in Port Repo.
and let's have a look at a trip repo.
There's 1 new one about Rpc. Metadata route
being overwritten by Middle West after request. Handle
that looks like p. 2, and that's for instrumentation express.
I know there were recently some changes around this, but I'm not sure if
that has released already is this hasn't released yet, but I think that
a completely different thing. So it shouldn't affect or fix this, I think.
Yes, so priority assigned anybody has time to work on this.
please feel free to head on over, assign yourself if you have permissions or otherwise reach out to somebody in the country Triages
group, and they can assign you
and then moving on to the pino instrumentation, not working. I was looking at this earlier.
2 weeks ago I posted this reproducer where I couldn't reproduce it and the person hasn't gotten
back to this issue yet. So I were meet them again.
and if they don't come back until next week, I will just close this as cannot reproduce.
and then we can move on to old country Pr triage.
Let's see, is, we had talked about E. 4.
I'm not sure is Jamie on the call today.
Doesn't look like it right.
Daniel Dyla (Dynatrace) 00:31:33 Don't see her.
Marc Pichler (Dynatrace) 00:31:35 Okay, then, I'll reach out to Jamie about this Pr separately, I think.
We have now added similar to be included, as like
directly into open telemetry instrumentation. So we can make changes to it.
Which would address some of the problems that
cause this pr to store. I would think, Jamie, if she had time to look into
the thing that was blocking this here
This pr here awesome
at that. I will wait for this to land first.st It did.
and I will ping them.
Looks like this person here would be interested in.
MG Marylia Gutierrez 00:33:22 I think I need to take a look at this, too, because I just see that it's talking about like connection string. I'm assuming this is kind of like database related, but we remove connection, string.
Marc Pichler (Dynatrace) 00:33:36 Okay. This connection attribute? Oh, yeah. Connection string. You're right.
Yes, if it gets removed then. I'm not sure about what is
making its place, or is it just removed without replacement? Do you know.
MG Marylia Gutierrez 00:33:59 Remove. So the connection string got removed. And the yeah, I can see here like database user was removed.
And then the just the database name, and host got removed and replaced with namespace.
Marc Pichler (Dynatrace) 00:34:16 Okay.
MG Marylia Gutierrez 00:34:17 So, okay, so like is not really valid. I can take a look again. Just yeah.
Marc Pichler (Dynatrace) 00:34:24 Yeah, if you
if you could have a look since you're very very much up to speed on the on the database Sam calls I would appreciate it.
Thank you.
MG Marylia Gutierrez 00:34:38 1932, yeah.
Marc Pichler (Dynatrace) 00:34:42 All right. Okay.
yeah. I guess. If you have a a look at this, and you figure out that it's or working on stuff that's going away, anyway. Then we can just put a comment here and we can close this pr
MG Marylia Gutierrez 00:35:00 Okay, I can do that.
Marc Pichler (Dynatrace) 00:35:01 Yeah.
you can either do it yourself. Or if you don't want to look like the bad guy that's closing the pr, so you can also ping me. I'm.
MG Marylia Gutierrez 00:35:12 Yeah, yeah, I can do. And I probably because I will eventually. If this is like the database related, I would eventually get to this package at some point, because this is what I'm doing now, just updating for all of them. So.
Marc Pichler (Dynatrace) 00:35:24 Awesome.
MG Marylia Gutierrez 00:35:24 Probably be the one removing this, anyway. So yeah.
Marc Pichler (Dynatrace) 00:35:28 Alright, thank you.
Okay, so this one, we talked about one, we also talked about, m moving on to
this pr, here.
this is for the cool instrumentation. And it's being kept alive.
Okay?
Continuous repacing.
probably just put the comment here
to let them know that
the rebasing is causing the the auto close not to go through. But the intention would still be to close this Pr. If
nobody wants to sponsor it or become an owner for the core instrumentation.
So, yeah.
Daniel Dyla (Dynatrace) 00:36:54 What was the last actual interaction with this Pr.
Trent Mick 00:36:58 Is me in November, reviewing it, making a suggestion.
Daniel Dyla (Dynatrace) 00:37:06 Cause. I mean, I think this person has obviously pushed quite a few times
over quite a few, you know, even very recently.
Yeah. So you review this period. What? What is that? Oh, it's from Mark. Yeah. So I think we should give them some.
I some path forward like if they want to sponsor the
component or something along those lines. Yeah. Oh, I see.
Yeah, okay, I guess. Never mind.
Marc Pichler (Dynatrace) 00:37:52 Right.
Trent Mick 00:37:54 That's so.
Still.
Daniel Dyla (Dynatrace) 00:37:56 So diligent about the about keeping this up to date. I almost wonder if it's like an automation.
Marc Pichler (Dynatrace) 00:38:03 I think we talked about this last time as well. That. It looks very, very much like clockwork.
Daniel Dyla (Dynatrace) 00:38:16 Okay, I think you can. You can let them know that
there's no sponsor, and and the Pr. Will be closed if there isn't 1
I think that's good enough.
Marc Pichler (Dynatrace) 00:38:29 I will put this in my notes, and I will write down a comment later on so that I don't have to do it on on the call right now, where you would just be looking at me struggling with the English language. So yeah.
then, these 3 here are in draft, so we can skip those.
Oh, here
there is this Pr for aws SDK, where
the owner has left a review and seems to have been addressed.
I'll just ping them again.
Not sure if there's I think there's multiple people
in all of the Aws SDK package.
So the ones that I remember.
Alright! Let's see if they can
have a look at this one so.
and moving on to the next one. This is the attribute serialization stuff.
Which we had talked about before, I think, and we have come to the conclusion that most of this should be handled in the SDK. And I also opened
this issue right here, which was kind of an offshoot of
above about circular references being might. That might be a problem during lock record serialization. So
we can address this in the SDK if needed.
I'm not sure how to move on with this, I guess. We were just close this Pr
in favor of addressing most of it in
into core repo.
Now, I should put this in my
list of Prs to close later.
and and this one was around for a long time.
Okay, react native instrumentation.
Which has a lot of thumbs up and
is a very much requested feature. It's just that react native.
The runtime that it's using is doing some odd things which makes it very hard to support
And this is the issue in the core repo.
I think we also at some point, added Florence here and
and to the contract triages thing as if this was already an approved instrumentation.
I gave a quick overview review here, but
was open for a very long time already, until I got to actually have a look at this one.
yeah, I'm not entirely sure what we
what we can do to make this move along here.
I think there's also the fact that this is using
using tracing to generate telemetry, which is kind of a concept that got him folks have
departed from. If I understand correctly.
Daniel Dyla (Dynatrace) 00:43:35 Well, yeah, I think that that's the plan. But it's hard to say like.
that's all very much in progress right now. This looks like a lot of work to just say like, No, thank you.
I would point her to the browser. Phase one project, folks
and let's see if we can get them to review these types of things. If the whole point of that project is that we don't have the
we don't have all the context here right now.
Marc Pichler (Dynatrace) 00:44:13 Okay, yeah. But then, again, this is a react native. So I'm not sure if.
Daniel Dyla (Dynatrace) 00:44:19 Oh, is it? Yeah, react. Native react has sorry.
Marc Pichler (Dynatrace) 00:44:24 Pretty quickly.
It is somewhat related, though. Because the like, whatever decision will be made, what's what's going to be used in the browser for
generating telemetry. If it's just a logs, SDK, or if it's traces, or
whatever else will also factor into.
Daniel Dyla (Dynatrace) 00:44:46 Yeah.
Marc Pichler (Dynatrace) 00:44:47 Hold this!
Daniel Dyla (Dynatrace) 00:44:47 I think.
Marc Pichler (Dynatrace) 00:44:48 Going to look like.
Daniel Dyla (Dynatrace) 00:44:48 Very similar to the browser react.
Marc Pichler (Dynatrace) 00:44:51 Good.
So okay, I guess sending them to
the Browser project and putting a comment
putting a comment on that. It's kind of in flux. What?
Oh, finer suggestions are going to look like to to generate telemetry on a on a client
Daniel Dyla (Dynatrace) 00:45:27 Yeah, I'll I'll add a comment. Here.
Marc Pichler (Dynatrace) 00:45:30 What did?
Daniel Dyla (Dynatrace) 00:45:31 Yeah, I'll I'll add a comment. I'll point them to the browser, Sig, and just let them know that this is in
influx. And yeah, hopefully, we can get it resolved.
Marc Pichler (Dynatrace) 00:45:47 All right. Thank you.
Daniel Dyla (Dynatrace) 00:45:49 Yeah.
Marc Pichler (Dynatrace) 00:45:51 Thank you for looking into this one.
Daniel Dyla (Dynatrace) 00:45:55 No problem.
Marc Pichler (Dynatrace) 00:46:00 Right.
and this is an approved Pr. To add the page, view, instrumentation. Plugin. I had looked at this one earlier to remove some of the labors where there was a mishap with the rebase.
Looks like the tests are failing right now.
So
and we're just ping them here.
David Luna Bistuer 00:46:35 Sorry, Mark. Maybe this one could wait In
yesterday we had the client's invitation taken.
We revived a couple of piastros for semantic conventions.
and specifically the page view semantic. So there are no semantic messages yet
for this, and they are using, and.
you know, run the names for for that. So there is a proposal on a Pr. And now we are planning to review that
probably we're going to discuss tomorrow on the 1st processing.
So I think this one could could can be on a standby, for now.
Marc Pichler (Dynatrace) 00:47:17 Okay, do you want to? Put a comment on this Pr to let everybody know what the current status is.
David Luna Bistuer 00:47:25 Yeah. All good.
Marc Pichler (Dynatrace) 00:47:26 Okay, thank you. Thank you for looking into this one.
Yeah.
Then we can move on to the next one, I guess, which is the sqlize instrumentation.
This was originally created by spector, and all the instrumentations in the
aspect to org are now
archived and read only so it looks like this is just adding this instrumentation here as well.
Yeah. So this one would need illness tool
for us to merge it first.st
Oh, let's see, there is the contributing guidelines.
Second, link in here
component of where did it go?
Daniel Dyla (Dynatrace) 00:49:21 Are you looking for?
Component owner? Oh, new interpretation.
Marc Pichler (Dynatrace) 00:49:24 More instrumentation is what I'm looking for. Yeah.
I think the person also opened
cr a while ago that we then subsequently merged. I think it was title or M.
So let's see
this. Pr.
No, I didn't put this link.
and let's see, hold it, move that.
and then the next Pr is adding an exception, hook to instrumentation. Aws, SDK
component owners.
I seem to remember that there was somebody asking for this in
slack, and saying that if they get a review they would replace it and
continue working on it. Maybe they just haven't seen the activity on
on this pr, so what I will do after this is, I will
see if I can find it on slack, and where we still have it. Let them know
that this Pr. Has been up has been reviewed.
Let's see if they come back to here.
This one we discussed a while ago that
it's not in the state to be merged, yet.
Trent Mick 00:52:17 Sorry that's still on me to follow up.
Marc Pichler (Dynatrace) 00:52:21 Okay, no worries I will. I guess we just move
move on from this Pr, for now and then. Yeah, we're just
talk again about it next week and see where it went.
And the next one is draft. Pr, so
I guess that's also something that
will depend on whatever the browser
project comes up with. If that will go ahead, or if that will stay in draft.
then the next next one is for instrumentation data loader.
there's some comments here.
Only I actually saw.
And the component owner for data loader did the review on this feature Pr here that just merged earlier
time.
The name was so yeah.
so I'll just be them in here.
I'm actually not sure. Are they a member of the org yet.
No, it doesn't seem like it.
And then and next one is awesome draft.
MG Marylia Gutierrez 00:54:39 Not related to any of those Prs. But just a question that I got. Now do we have a frequency of releases.
Marc Pichler (Dynatrace) 00:54:48 In core or in contrib, in.
MG Marylia Gutierrez 00:54:51 So I have here saying that inquiries every 4 to 6 week, and in contributes monthly.
Is that is that correct?
Marc Pichler (Dynatrace) 00:55:02 So in core. I tried to release every 2 weeks. Actually, it
has not seen a lot of releases after we released 2 and in contrip it's kind of an on demand thing.
if there's an approval on the release. Pr, I will usually go ahead and merge it if I see it.
But yeah, I guess if anybody is
interested in bringing a more regular release schedule to the whole thing.
MG Marylia Gutierrez 00:55:45 The concept this Pr that I just share here. So they're putting up
central release file for all 6.
And there is this one for the Javascript, with those dates.
I think they are just asking for reviews.
Marc Pichler (Dynatrace) 00:56:01 Okay, yeah, I were, let's have a look at this one.
Frequency.
Yeah, it is always at least aligned with. When we do a core release. Because if there's any breaking changes, we need to get the releases out as soon as possible.
Yeah.
Daniel Dyla (Dynatrace) 00:56:28 Oh, sorry I was distracted. So we yeah, we talked about this in the spec meeting. No, none of this is like.
I mean once it's documented, it's there, but none of it is is like a guarantee or anything like that. It's just a requirement from the Cncf. There. They want
the idea is that users can have some idea of how often something should be released and who to talk to about a release problem or something along those lines.
This is not the component owners. This is like
people responsible for the release itself, like who at the end of the day said, yes, this is good, and shipped it.
Marc Pichler (Dynatrace) 00:57:14 Right?
So yes.
Is there also somewhere? Mention of these thinks
like, who is responsible for it?
MG Marylia Gutierrez 00:57:32 If you look at the seem to, it, has, it shows like
Js maintainers. If you look like release Maintainers of the table is a group that's mentioned.
Daniel Dyla (Dynatrace) 00:57:44 Yeah, if you change the view of this file to be like the rendered view, like the preview or whatever you'll see. It's just like a table of.
Marc Pichler (Dynatrace) 00:57:54 Eyes.
Daniel Dyla (Dynatrace) 00:57:55 Yeah. So it shows contribute Js maintainers and contrib maintainers, which is.
Marc Pichler (Dynatrace) 00:58:01 It's not something that exists, not something. Yeah, it's just jazz containers.
Daniel Dyla (Dynatrace) 00:58:08 And then you have to be like an org member to see that link, too. There's there's other problems with it. But.
Yeah, we talk also.
Marc Pichler (Dynatrace) 00:58:20 I will also put this on the list as
I'm very frequently doing the releases.
I can probably give some input and update this with the the actual scheduler.
Daniel Dyla (Dynatrace) 00:58:40 Okay.
Marc Pichler (Dynatrace) 00:58:44 Now, if there's any appetite for
being part of the release process, or something like that and anybody wants to go through the process themselves, and this approval already feel free to reach out to me as well. And
I can
show you how it's done. And yeah, we can alternate to doing releases as well. So it would be good to like, share the responsibility as well every once in a while to get the releases out. And then maybe we can also go go to a more
but more consistent time between releases which can be can be good to. Yeah.
Have, like some set dates where we say we will release for sure. And
then we can follow through with it, because at the moment it's
for me. Sometimes I delay a release. Because I'm like out the next day, or something like that, and I won't be able to follow up for with it.
And yeah, if there's someone else who
might not be out at the same time that I'm also out of office, then we can get to a more regular release cadence there.
So just fyi, if you're interested reach out on
slack, or whatever we move to in the future.
Daniel Dyla (Dynatrace) 01:00:23 I think it might be discord. I heard some some rumors about discord.
MG Marylia Gutierrez 01:00:31 Yeah. The only comment that I put on this
Pr was like, please change to alphabetical order, because it's dot net. Go, Python Javascript. No, don't do this.
Marc Pichler (Dynatrace) 01:00:44 Yeah.
Alright. Yeah, thank you for bringing this up. This was I'm sure it would have showed up somewhere in my notifications list, but I'm
kind of drowning in.
Daniel Dyla (Dynatrace) 01:00:59 Somewhere in my notes.
Marc Pichler (Dynatrace) 01:01:00 Vacations. Yeah.
MG Marylia Gutierrez 01:01:02 Yeah, I got this one because of another report that I Maintainer. And I was like, well, since I'm here, let me also check for the Javascript. And then I noticed the the time that I was like that. The right thing. Yeah.
Daniel Dyla (Dynatrace) 01:01:14 Yeah, I probably should have brought this up. I already knew about it, and just dropped from my brain.
Alright, I think that's time.
Marc Pichler (Dynatrace) 01:01:27 Yes, we're out of time. Time flies. It seems like
when you're when you're having fun reviewing. Or Prc,
Jackson Weber 01:01:36 Doing? What? Prc, yeah, yeah.
Daniel Dyla (Dynatrace) 01:01:42 I think.
Marc Pichler (Dynatrace) 01:01:42 Oh, sorry I didn't.
Daniel Dyla (Dynatrace) 01:01:43 You're not muted.
Jackson Weber 01:01:44 I think you're not muted.
Daniel Dyla (Dynatrace) 01:01:49 Alright! That's the end of the meeting, anyway.
Marc Pichler (Dynatrace) 01:01:53 Right then. Thank you, everybody, and see you next week.
David Luna Bistuer 01:01:59 Yeah.
Trent Mick 01:02:00 So.
Marc Pichler (Dynatrace) 01:02:01 Thanks, but.
Jackson Weber 01:02:02 That's a good one, guys. Thanks.
