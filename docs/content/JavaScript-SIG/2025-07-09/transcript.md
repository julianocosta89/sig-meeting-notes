SIG: JavaScript SIG
Date: 2025-07-09
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:00:55 Blue.
MG Marylia Gutierrez 00:00:57 No worries.
Daniel Dyla (Dynatrace) 00:02:05 Hello!
Raphaël Thériault 00:02:09 Hello!
Daniel Dyla (Dynatrace) 00:02:19 Very big agenda today.
I refuse to save my recovery. Codes, Trent.
Alright, I guess. Let's get started. We don't have a lot of
we don't have a lot of
topics today. The 1st thing I wanted to call out was that the browser phase, one project?
Had its 1st meeting last week
meeting recordings are public. If you're interested.
we didn't cover a lot. We just went over what the current state of that project is, but I think that project will have a lot of overlap with us so probably best if we
stay as up to date on them as is reasonable.
I did show them the
Api 2 dot o poc thing that I made, or the backwards compatible. Api poc
they asked, that I put together a presentation around that. So I should be showing that off tomorrow.
yeah, Project, thank you. To whoever is adding stuff!
Mark experimental! 2 0, 3. Live now.
Marc Pichler (Dynatrace) 00:04:47 Yeah, just an announcement
cut the release earlier today. And the contract release is running right now. So packages will be available
probably in a few minutes. That's it.
Daniel Dyla (Dynatrace) 00:05:01 Excellent dan needs to save his recovery. Codes. Yes.
they should give you a notification or a banner, or something
alright in debug triage. Everybody's favorite part. Oh, yeah, no results.
Perfect software
contribute bugs. No results here, too. Oh, man, when was the last time? We had no bugs on both
old Prs replace Karma with wpt runner.
March 8.th What's the last on here?
Marc Pichler (Dynatrace) 00:05:47 I'll sign Jamie. On June 5.th
It's mostly a question about the Pr. That Jamie was about to open there. I think this Pr here can be closed now.
There hasn't been any activity.
Daniel Dyla (Dynatrace) 00:06:11 Okay.
Marc Pichler (Dynatrace) 00:06:17 Housing it, and then if there's appetite to do this which I think I still think we should do this at some point and
we'll probably need to go through everything again and try new
David Luna Bistuer 00:06:35 Bluetooth, is that the strategy for
but for web instrumentations? So we'll move away from kernel.
Marc Pichler (Dynatrace) 00:06:45 I think so. Yeah, comma is deprecated, as far as I know, or like, completely unmaintained already. And they point towards web test runner, which, is
like kind of the next thing that everybody should use. So we'll have to migrate at some point.
not accepting new features, origin generate fixes so.
David Luna Bistuer 00:07:10 Okay.
Marc Pichler (Dynatrace) 00:07:10 We should migrate away from it at some point. It's just that most of the web instrumentations are kind of unmaintained. I think so it's kind of difficult to
figure out what's wrong with the tests as well, because there's nobody around anymore who actually wrote them in the past.
David Luna Bistuer 00:07:30 Hopefully, that's going to change.
Marc Pichler (Dynatrace) 00:07:33 Hmm.
Daniel Dyla (Dynatrace) 00:07:33 Yeah. Fortunately, there's a group of people who are interested in
all of that right now, so they should take them over, replace them whatever.
Marc Pichler (Dynatrace) 00:07:46 Okay.
Daniel Dyla (Dynatrace) 00:07:47 What's your comment?
Alright, Trent, this is a draft test services, should we? We've been skipping this skip it again.
Trent Mick 00:07:59 Yep.
David Luna Bistuer 00:08:01 Else. Actually, I have a
I work on this into steps. I made the 1st VR that was adding, and the the root folder was adding these test services.
Now there is a Pr. That they open just an hour ago or so.
That adds the second part, which is the thing. So I sorry, Trend I not sending your work, but just, you know, reusing that and and splitting, you know a couple of of Ps.
So.
Trent Mick 00:08:31 Sounds good.
David Luna Bistuer 00:08:32 This pr, if
If finally, if it gets merged.
will supersede the the trends one, so we can close trends as well.
Daniel Dyla (Dynatrace) 00:08:45 Cool Sqs. For C.
These spam links, instead of processing spans.
Are we at here, tag the owner a couple of times same, tagged him again.
Is Jonathan. Are you on the call here?
Marc Pichler (Dynatrace) 00:09:09 I don't think you're trying to find this on the car. Yeah, has been.
I think the owners of the instrumentation have been kind of quiet for
the past few weeks or so.
Daniel Dyla (Dynatrace) 00:09:26 Yeah, I mean, this is like what the specification
tells you to do now. So I do think we should accept it.
yeah. Still a lot of conflicts.
Marc Pichler (Dynatrace) 00:09:44 Yeah, that's called.
Daniel Dyla (Dynatrace) 00:09:45 Oh, that's because.
Marc Pichler (Dynatrace) 00:09:46 Move!
Daniel Dyla (Dynatrace) 00:09:47 Yeah, that's Trump's fault.
Marc Pichler (Dynatrace) 00:09:50 So.
Trent Mick 00:09:50 Full.
Marc Pichler (Dynatrace) 00:09:51 Thank you, Trent, for doing that, though.
This call is my fault. Every conflict.
Daniel Dyla (Dynatrace) 00:09:57 All the cost.
Trent Mick 00:09:57 Alex.
Marc Pichler (Dynatrace) 00:10:00 I. I was actually looking for a package today and was able to find it way quicker. So thank you for
making making everything neat and tidy. There.
Trent Mick 00:10:14 You can name me in that comment, too. I'm happy to help people, too.
Daniel Dyla (Dynatrace) 00:10:17 5.
Trent Mick 00:10:18 Conflict. I don't know. Sometimes that's a pain in the ass package lock, especially
just doing the naive thing really was doing this on her Pg. Instrumentation. Pg, thing, the naive thing results in like a 30,000 line. Diff and package lock. So.
MG Marylia Gutierrez 00:10:34 Yeah, I try, like 3 different ways, and all of them just created every time like 30,000 new lines, like, what is happening. So, yeah.
Daniel Dyla (Dynatrace) 00:10:45 The only switch way.
Trent Mick 00:10:46 How to do it is okay.
MG Marylia Gutierrez 00:10:48 I, I blow it away and regenerate it
did that, and then he keep creating different things.
Trent Mick 00:10:54 Actually so blow away and regenerate also has problems because Npm sucks the package lock file has
a number of fields in there that don't need to be there, and with different state on your system in your cache, or something like that, it'll add or not. Add the license field and a couple of other fields, and so you still get a multi 1,000 line diff the best way I found to do it. I think well, best ways from a couple of tries yesterday was
remove package, lock, copy, package lock from Main.
and then rerun Npm. Install in the directories in which you've made package. Dot Json changes.
and hopefully, that results in the minimal change to package, lock.
MG Marylia Gutierrez 00:11:36 So, yeah, I think I tried. That version also created a bunch of things. So my final solution was, I just copied the raw file like, I went on. Github copied the file on mine and just manually change the package log because it was just one version that I changed something. So I did only that, and then it worked.
And then this morning Mark updated the version, and I'm like, Damn it, conflict again. But that was an easy one to fix.
It's a never ending.
Marc Pichler (Dynatrace) 00:12:10 Sorry about that.
MG Marylia Gutierrez 00:12:12 Lord.
Marc Pichler (Dynatrace) 00:12:15 Something related to
like Npm creating large diffs in the package log. Jason, I think I figured out the
reason why it adds the license fields and stuff.
and it seems to be fixed with npm, n, dot 8
So every time there's a version that's kind of
low, tender date. It will like
not be consistent behavior. I added the constraint to the renovate Jason in the core repo, and it hasn't happened since. I think that it that it adds that so that's something that we may want to look into in the contribut repo as well.
And then I've also seen that one can run Npm. Dedupe as a post processing step for renovate Jason, which might help keep the file a bit smaller.
Trent Mick 00:13:19 So I'm wondering if we wanna do that as well.
MG Marylia Gutierrez 00:13:25 And also, if you have any ideas of like people that are contributing that they could do on their side, we also have like that file that is like contributing. Why you should do things like that. Maybe that is one of the troubleshootings.
Oh.
Marc Pichler (Dynatrace) 00:13:41 And you mean for the package lock.
Yeah.
Oh, yeah, it might be.
Trent Mick 00:13:50 Far I've been.
Yeah, I'm not sure how we would write that thing. So far, I've been updating package like the same way a program, Perl, which is to just keep throwing random stuff at it until it seems to work.
which isn't good advice.
MG Marylia Gutierrez 00:14:04 Yeah, just put it on the fire. Try something if work ends, if not.
Trent Mick 00:14:10 Yeah, well, it's it's educated around in this. But yeah.
Daniel Dyla (Dynatrace) 00:14:19 Alright.
This is the sequelized instrumentation mark. It looks like you reviewed it recently.
It looks like it's been reviewed by a couple of people. Recently one of the component owner candidates, I
responded. The other still has not. That's Martin Hennock.
t2t2 00:14:42 Joins us.
Daniel Dyla (Dynatrace) 00:14:43 This, call.
t2t2 00:14:43 He's on vacation until end of week. So.
Daniel Dyla (Dynatrace) 00:14:47 Vacation. Okay?
Yeah. So this one actually seems to be on decent track. Now.
Marc Pichler (Dynatrace) 00:14:55 Yeah, I will be out of office or the next weekend the week after that. So if anybody in the meantime, can have a look at that. I would appreciate it
otherwise it might be sitting there for a while again.
Daniel Dyla (Dynatrace) 00:15:22 Okay?
And then
that was sequelize exception. Hook, this is another. Aws. SDK one.
It looks like Jonathan did review this.
Marc Pichler (Dynatrace) 00:15:45 Yeah, I think that's the cr that was brought up in the auto chass channel on slack a while ago. But the person hasn't come back to
actually keep working on it.
Daniel Dyla (Dynatrace) 00:16:10 All right.
Open AI instrumentation for chat creation.
Trent Mick 00:16:23 I skipped this one. I asked him when, little while ago, to see if he wants to keep following up. If not, we'll probably close this. And then I was talking
with Mila. She was gonna hook me up with some people, Microsoft, that are also interested in doing an open AI instrumentation and signing up as
code owners of it. So there may be another passer.
Daniel Dyla (Dynatrace) 00:16:49 Old draft 2 weeks ago.
This is the masking. Again.
Think this one's been relatively healthy.
MG Marylia Gutierrez 00:17:35 Yeah. So this one I guess I gave like 2 weeks should be enough for the person to reply. They didn't, so I guess I can
continue then that is the one that I just wanted to give them a chance.
Yeah. By the way, do we have? Cause? I I don't think we have a
specific like or environment variable for cases like this.
Should I just create one? Do we have any
any others as example like this?
Daniel Dyla (Dynatrace) 00:18:07 I don't know. I don't know where the environment variables are necessarily specified. I think they might be in
semantic. And yeah, I don't know. I don't know if they're specified anywhere, actually, which is because.
MG Marylia Gutierrez 00:18:25 Because the idea, when we were doing even like the database semantics we were discussing having something for this like this case. Specifically, we were like, Oh, we don't want to create this now, because probably when config file comes, this is gonna change so we didn't create it on purpose. But now we do have this case like this. So maybe I should just create one environment variable perspective for this case. And whenever we do the config file, then we can replace it.
Daniel Dyla (Dynatrace) 00:18:55 Yeah, I could go either way. I don't
love the idea of just creating more environment variables, because
when we do the config file, I think every single one we add is adding to the burden of the
of changing over but at the same time I don't know when that will be so.
I don't want to block valid use cases. I mean.
it's not in. I assume it's not in semantic conventions. The environment variable.
MG Marylia Gutierrez 00:19:24 No. Yeah.
Daniel Dyla (Dynatrace) 00:19:27 Yeah, I mean, I I don't necessarily want to create like
one that then might be different than one a different language created like if there's 1 that all the other languages are already using, then maybe we use that
MG Marylia Gutierrez 00:19:41 Yeah, because, as far as I know, the others, we, for example, I think we saw, like the Java one was already. I could see the like. The query without having to like mask, for example. So it was not a concern on performance. So we just like or send. If it is it? It is or doesn't send. But this case we are adding in the extra performance. I don't think we have any others.
SDK, that is doing what we are doing. So I don't think we have created an environment variable for any other sdks.
Daniel Dyla (Dynatrace) 00:20:14 Yeah. So I've if there isn't an environment variable for other sdks, I don't know.
Like we don't have environment variables for all of our configs. What makes this one different.
MG Marylia Gutierrez 00:20:31 yeah, because otherwise, I don't know how we would let the user decide when to turn on the masking.
Daniel Dyla (Dynatrace) 00:20:39 Will they set the config?
I guess I don't understand.
MG Marylia Gutierrez 00:20:48 So that is my question. What would be this config where they do like turn on?
Or they enable this? What would? How would be like? What is their action?
Trent Mick 00:20:58 It would be in Bootstrap code. That's specifically creating the Mysql 2 instrumentation.
Yeah. Object. So not.
Well, no. The auto instrumentation node also has a way to pass in config to those.
MG Marylia Gutierrez 00:21:11 Okay.
Daniel Dyla (Dynatrace) 00:21:11 It does. Yeah.
Trent Mick 00:21:13 So I mean it rules out configuring that for, like the hotel operator
situation, and I guess for Landa as well, if that's relevant.
MG Marylia Gutierrez 00:21:29 I guess you can. I can look if you anyone have any example that can just share that would be great. But yeah, I can look into this one, then
this, this way of doing, not use environment, variables.
Daniel Dyla (Dynatrace) 00:21:43 I think the zoom stuff is always, in a way.
should be probably an example in every readme.
Yeah, there's no configuration. But when you do this.
you can pass an object here with the configurations.
Any of these options are valid.
MG Marylia Gutierrez 00:22:01 I see what you mean. Got it?
Okay? Yeah. I can gonna start working on this. Probably tomorrow. Friday.
Daniel Dyla (Dynatrace) 00:22:14 Okay.
instrumentation for web exceptions.
This was March of this year.
Looks like 2 people have requested changes.
Component owners, Martin volunteered.
Doesn't look like
anything's really changed since last week.
I'm gonna go.
I'm just gonna add all of these examples into here. So they see what we're talking about.
Where was I.
This one ci github action for owner. Approval label
looks like this was reviewed in May.
Looks like this just needs reviews.
Marc Pichler (Dynatrace) 00:23:36 Yeah, I need to review this. Still.
I think we should probably be fine merging this. Actually,
Daniel Dyla (Dynatrace) 00:23:46 I haven't had enough time to look into it.
Marc Pichler (Dynatrace) 00:23:49 It's also all these workflow changes are
always a bit tricky to figure out all the security implications and whatnot.
Daniel Dyla (Dynatrace) 00:24:02 Yeah, I think, for the most part like this pull request like review
as long as it's not like running external code or whatever.
I think they're usually pretty safe
if this is just adding labels. But
yeah, just needs to be reviewed
instrumentation data loader.
Marc Pichler (Dynatrace) 00:24:42 I think the last state here was that it was missing tests.
David Luna Bistuer 00:24:46 Yeah. And it's still there, that way.
Daniel Dyla (Dynatrace) 00:24:50 Yep, as of yesterday. I think this is
Gcp detector. Oh, this was the Gcp external.
Yeah, this was kind of the conversation that we had last week.
Let's see.
expanded.
Feel like my keys aren't working.
And then.
Staff, I think that's good enough for now
extending testy pills.
Marc Pichler (Dynatrace) 00:28:56 This is just extending the test helper.
Yeah, that's also related to this resource detected Pr.
Daniel Dyla (Dynatrace) 00:29:12 Clarify the duplicate logging, workaround.
Trent Mick 00:29:21 That's on me. I took it last week. I haven't done it yet.
Daniel Dyla (Dynatrace) 00:29:25 Okay.
Ws, more aws stuff.
This is one of those things we're having aws. Host. These things would be helpful, I think, for both of us.
This looks like it's been reviewed in the last week.
So I'm not particularly worried about it.
Extract the full container. Id.
Where are we at here.
Okay, so last week took it out of draft.
Yeah.
So this just needs reviews. I guess.
Stink
as we get to the bottom of this list. A lot of them are going to be in the same boat.
Renovate lock file maintenance. Is this mergeable?
Nope? Oh, I just need to review refresh locks.
Okay.
Add new pr workflow. David Luna, this is a draft.
David Luna Bistuer 00:31:33 Yeah, and so wrapped until my my other Pr is merged. When
the Pr with the test services is merge and you want to work on this one and
and set it for review.
Daniel Dyla (Dynatrace) 00:31:46 Awesome. Okay?
Another renovate dependency. Since I just merged one. I'm sure this one is not going to be
Marc Pichler (Dynatrace) 00:31:53 This one can be closed, we will not support, fastify before. So yeah.
it's actually coming up to
be removed soon. I think the end of the
period that we would keep it around was soon 30, th
and I still have to go through the process of deprecating everything and removing the instrumentation and stuff.
Daniel Dyla (Dynatrace) 00:32:24 Okay.
Instrumentation. Oh, we're into peers from last month. Look at that.
Trent Mick 00:32:33 Yeah, Marilla and I are working on that one.
That's 1 i just need to review.
Daniel Dyla (Dynatrace) 00:32:42 And
or I'm just gonna skip the renovate ones. For now, Trent, linting examples.
Trent Mick 00:32:52 Yeah. Sorry check again. And merchant.
Daniel Dyla (Dynatrace) 00:32:59 Okay.
Trent Mick 00:33:02 Looks like it's close, though.
Daniel Dyla (Dynatrace) 00:33:04 Add minimum token permission for all github workflow files, open telemetry, bots.
Marc Pichler (Dynatrace) 00:33:12 I think trust has been working on this one. I merged the one in core recently.
Still have to look into that one. There was one thing that caused trouble in core, which was the Graphql analysis, or what am I talking about? Coq, analysis thing.
workout? Ql needs security, events, right permissions, and that one was missing. So
I think that's the only thing that we need to have a look at here as well. And once that's changed we can merge this one.
Daniel Dyla (Dynatrace) 00:33:57 Union type support and Graphql opened last week.
Looks like
Opecne is the component owner for this one. He hasn't been around for a long time, I think we should probably
sign new owners for those packages.
Marc Pichler (Dynatrace) 00:34:17 I did reach out to him I don't know a few months ago. And he said he still wants to keep owning these packages, so
I have kept him on the list. There.
Daniel Dyla (Dynatrace) 00:34:30 Okay.
Marc Pichler (Dynatrace) 00:34:33 Yeah. So maybe we can ping him.
Daniel Dyla (Dynatrace) 00:34:43 If he wants to be an owner, he can keep getting emails about comments.
Alright. That was graphql rate limiter and sampling targets.
This is Jonathan himself. Look at that.
Marc Pichler (Dynatrace) 00:35:02 Yes.
Daniel Dyla (Dynatrace) 00:35:03 Component owner here and there is also another component owner. I think I'll let them
work this out amongst themselves.
Marc Pichler (Dynatrace) 00:35:12 Yeah, they are,
basically taking a lot of the code that they had hosted in the aws repo themselves. And they're moving it to here.
so.
Daniel Dyla (Dynatrace) 00:35:26 Okay.
Marc Pichler (Dynatrace) 00:35:27 It.
Yeah, you should
just wait for them to apply the has all the approved label, and then merge it in.
Daniel Dyla (Dynatrace) 00:35:41 David, an hour ago.
David Luna Bistuer 00:35:43 No, this is the one you already mentioned.
Daniel Dyla (Dynatrace) 00:35:46 We already talked about this one today. Perfect.
I think that's it. We got through the whole list 27 open Prs.
Marc Pichler (Dynatrace) 00:35:56 We can start.
Trent Mick 00:35:56 Now, sometime the core repo, yeah, exactly.
Daniel Dyla (Dynatrace) 00:35:59 Yeah, I was just gonna
is that really the oldest one that's not so bad?
2023.
Trent Mick 00:36:16 It's here!
Marc Pichler (Dynatrace) 00:36:17 I've been closing out few of them. This one I've kept around because there's a lot of people that want this
It's fairly out of date right now.
After the changes I made to the
to the exporter. It's a bit easier to get this working now.
The thing is that I would like to have a new exporter interface to
make this a bit easier to work with.
So right now, if we add this fetch sender thing.
There's a lot of kind of moving parts
on one end. We would have the
browser code that's using the xml. Http. Request and send beacon right now
and then. There's the Nodejs stuff that's using the Nodejs Http module and we can just
switch everything over to fetch which would be my preferred solution, because,
the no Js version that we support. I think you can turn off patch with feature flag or something. So if we add that, then, like everybody who's using that feature flag might not be able to export anymore. It's kind of unfortunate
but it would simplify a lot of the things for us if we were able to use.
Fetch just everywhere.
Daniel Dyla (Dynatrace) 00:38:09 So really, no fetch
that's annoying.
Usually, most functionality shows up there.
Okay?
Well, I think that's okay, for now then, I guess.
Marc Pichler (Dynatrace) 00:38:34 Yeah, I.
What what I really need to do is I need to come up with a prototype for new interface and play around with it a little bit.
and after we've done that we should have an path forward that we can communicate here. Just takes a lot of effort to
make make it in a state that is kind of
something that we can extend later.
Daniel Dyla (Dynatrace) 00:39:16 It looks like there was discussion going on here, and then kind of all dropped at the same time.
Marc Pichler (Dynatrace) 00:39:22 Yeah, but we weren't really sure if that was the
correct approach. But it seems like it is the correct approach. So dot easy.
Daniel Dyla (Dynatrace) 00:39:37 Seems pretty straightforward to me.
Okay, I will keep this one open and take a look at it. After.
Trent Mick 00:39:58 Yeah, we can probably close it.
Daniel Dyla (Dynatrace) 00:40:04 Can probably close it or close it.
Trent Mick 00:40:06 Yeah, let's close it.
I'm not gonna get back to this.
Daniel Dyla (Dynatrace) 00:40:17 To create Api logs.
This is probably something that needs to be redone.
Since we now have like a separate, there's a logs and events merged back into logs.
I think this is oh.
Marc Pichler (Dynatrace) 00:40:42 Yeah, it still has a lot of conflicts.
but seems to be just a package log. Json. Now.
That's that was probably the release that I cut previously.
though I'm not sure if we wanna do that immediately, or if we wanna
make all the changes that we need to make to the blocks. Api, before actually integrating it into the Api package.
Daniel Dyla (Dynatrace) 00:41:13 I don't know how many changes really need to be made. I know that. Svetlana was looking into the
logs. Api. It looks like she's not on the call today.
Marc Pichler (Dynatrace) 00:41:25 Yeah, I've I've been following that a little bit. There's at least one more breaking change that needs to go in.
Daniel Dyla (Dynatrace) 00:41:34 Okay.
Marc Pichler (Dynatrace) 00:41:35 It's fairly minor breaking change. It's not something that I would assume any
person would actually use, but it's still a breaking change, and it's probably better to get these crossed off the list where, while we still have a 0 dot something version rather than
an experimental entry point in a staple package, so always gets a bit
more difficult to justify breaking changes there.
So this is something that I would want to do all the way at the end, when
we're kind of sure that we wanna go ahead with releasing it, or like a release candidate.
Trent Mick 00:42:35 Oops!
Daniel Dyla (Dynatrace) 00:42:38 I don't really have a label for that.
Martin said. This is on hold, I assume that's not any different, for now.
Marc Pichler (Dynatrace) 00:42:51 Maybe that's also a thing for the list in.
Daniel Dyla (Dynatrace) 00:42:55 Can't.
Marc Pichler (Dynatrace) 00:42:55 The processing.
Daniel Dyla (Dynatrace) 00:43:00 Content length missing.
I think this is not necessarily browser, seg, because these are just Http
instrumentations. I mean they they do run in the browser, but
I don't think we have to wait on decisions from them. Necessarily.
Marc Pichler (Dynatrace) 00:43:18 Yeah, I I meant the previous one, actually,
Daniel Dyla (Dynatrace) 00:43:21 Yeah, okay, I gotcha.
Trent closed this. Jamie reopened it.
Trent Mick 00:43:31 Yeah, we are discussing, maybe wait until Jamie's back next week or the week after.
Daniel Dyla (Dynatrace) 00:43:36 Maintainers are fighting
all right.
Which one was that that was this one Otlp serializers.
Marc Pichler (Dynatrace) 00:43:50 Oh, yeah, that's mine.
Daniel Dyla (Dynatrace) 00:43:50 Mark open this. 2 people reviewed it.
Marc Pichler (Dynatrace) 00:43:55 Work, but good. I will replace
this. I'm not sure if we still want to do that, though.
so basically, the reasoning why I opened this is, there's 2 issues open right now, which are
the 1st one. And
I think they they both ask about the same thing is, basically, if you bundle these up then you will get a warning about
something that I don't remember anymore. But it's not really something that actually happens. So if you split that up into different entry points, then the exporter that's Jason will only import Jason and not product the Proto path library which causes this error.
So it basically gets rid of a bunch of concerning locks for people.
that's 1 thing. And the other thing is that it also introduces like an experimental entry point for logs serializes
and that would enable us to basically mark this as stable at some point
without the logs. SDK, having to be stable
that was part of the
of the milestone for otop exporter stabilization, because that's 1 of the dependent packages that we need to get
stable before we can get the exporter stable, or at the same point, at least, we need to get it stable.
Daniel Dyla (Dynatrace) 00:45:37 Okay, we had. Yes, Link warnings. It's like I commented on. This one
looks like the comment that I made is out outdated.
and nothing has happened since here. It's just change log. This is only yes, Lynn. So I'm actually gonna there's no change log required for yes, and stuff.
skip, change log. Get that fixed?
The lint signed out, I wonder?
Verify text map, propagator, Api requirements.
Man, I wish we had this guy back. He did a lot of work really quick.
Where are we at here? Closed stable, closed record views reopening.
That was Hector in May.
Clarify api requirements.
Oh, he's just changing Doc template stuff.
Alright, I'll leave this one open because I think I do want that one to survive.
These are gonna be the same fixes lint warnings. Fix eslint warnings.
this is a draft, Trent add testing with Node 23 looks like it's failing. And it's still a draft.
What's the type stripping situation right now?
Trent Mick 00:48:24 That's what I was gonna ask. I can't. There's been some movement on those issues in the various
tool repos, but I don't know what the current state was.
I can't even remember what this one was.
My draft. Pr, here, I think, was a
seat that we manage 57.
Daniel Dyla (Dynatrace) 00:48:45 Files changed more than I expected.
Trent Mick 00:48:47 Yeah, yeah, we don't want to do this one if we don't have to.
Daniel Dyla (Dynatrace) 00:48:55 Okay.
Trent Mick 00:48:57 This was one of the options.
Daniel Dyla (Dynatrace) 00:48:59 Close it? Or are we leaving it open?
Trent Mick 00:49:02 Awesome
if we go link the the relevant discussion is the linked issue.
And what
what's gonna happen there? So someone needs to go follow up, and
with, I think, the Tsx path was that what we were hoping.
Marc Pichler (Dynatrace) 00:49:23 Yeah, I was, I was meaning to work on that. Actually,
Daniel Dyla (Dynatrace) 00:49:28 Yeah, I used Tsx for something recently. And I was. It was like.
I ran into a minor problem
using Ts node Googled it. And one person was like, just switch to Tsx. And all I did was switch the binary, and everything started working in a different project so
hopefully that shouldn't be too difficult.
I actually tried, and it was unfortunately not the case.
Gorgeous.
Marc Pichler (Dynatrace) 00:49:53 There's a lot of.
Trent Mick 00:49:55 We're using it indirectly with Mocha, and it gets.
Marc Pichler (Dynatrace) 00:49:57 Yeah.
Trent Mick 00:49:57 More. Involved. Yeah.
Daniel Dyla (Dynatrace) 00:49:59 Got it. Okay.
Marc Pichler (Dynatrace) 00:50:00 Yeah, I've I've started updating a lot of the packages that we have that we use for testing which might also cause some trouble
some points.
But it's a lot of work. Unfortunately.
Daniel Dyla (Dynatrace) 00:50:19 Yeah, I think actually, it might have been this one.
Yeah.
Well, in any case.
Yes. Next export condition is more specific than module.
Yes, next is next for conditions. Module conditions always use package chase.
So this just changes the order.
Marc Pichler (Dynatrace) 00:51:01 Yeah, I think, too, they're using something that basically takes module before is next and
by switching it it will select ears next, if they have something there selected.
Daniel Dyla (Dynatrace) 00:51:22 Yeah, it's like picks. The 1st one that matches.
It's probably okay. I wish there was some better way to test this
example. Here, Trent, did you ever have time to look at their example?
Trent Mick 00:51:59 Sorry. I'm catching up and.
Daniel Dyla (Dynatrace) 00:52:09 Like when they use roll up.
It's matching on module
when they want next.
Trent Mick 00:52:22 Yeah, I understand.
Daniel Dyla (Dynatrace) 00:52:26 And.
Trent Mick 00:52:27 Yeah.
Daniel Dyla (Dynatrace) 00:52:27 Kind of the embedded.
Trent Mick 00:52:32 Lists of keys in the exports that
will be used depends on the bundler like to each other, unless
looks like we could make the switch and then add it. I'm like I'm creating
fake bug things. But then there's another bundler that uses things in a different order. So there's no kind of total order that makes everyone happy. Like. I'm not super comfortable in this area, but
I can.
Daniel Dyla (Dynatrace) 00:53:07 Yeah.
Field significant during condition matching earlier entries of higher priority.
General rules. Condition should be for most specific to least specific in object order.
So he's making the argument that next is more specific than module, which I think is correct.
Actually.
Trent Mick 00:53:33 Yeah, so it's probably.
Daniel Dyla (Dynatrace) 00:53:36 He did. Yeah. He created the repro, the the reproduction repo. That shows that.
I'm not exactly sure
how exactly it's supposed to show it. My guess is the output here. Yeah, when building.
So there's a bunch of warnings.
I think it's probably okay.
I'm similar to you, though I don't like. I don't feel comfortable in this area. I wish
we had somebody that was more of a
a web bundler expert. Maybe we can ask. You know what.
That's what I will do.
I closed their meeting notes.
Browser, Google, Doc.
Trent Mick 00:54:58 So we should presumably do the same. Then, in semantic conventions.
Daniel Dyla (Dynatrace) 00:55:06 Probably all of the browser packages. Right?
And no, I'm the only this is the only ones that use exports, which is the semantic conventions Api.
Trent Mick 00:55:16 Otlp export, but exporter, base and shim open census, but but no one uses that.
Daniel Dyla (Dynatrace) 00:55:25 Okay.
Trent Mick 00:55:28 Never mind a bike.
Daniel Dyla (Dynatrace) 00:55:31 Should be applied probably everywhere.
Is this only done in Api, then I assume, yeah, instrumentation. Http, context, hook.
Marc Pichler (Dynatrace) 00:55:52 This can be closed. It's out of scope for the project.
if that's the correct one. Wait, let me double check first.st I think you commented on this one right or on the issue itself.
Daniel Dyla (Dynatrace) 00:56:06 Yeah, you didn't comment on the Pr, but wait, are there 2 Prs fixes?
Yeah, okay.
Marc Pichler (Dynatrace) 00:56:22 Yeah, so what they were trying to.
Daniel Dyla (Dynatrace) 00:56:25 The scope of the project.
Marc Pichler (Dynatrace) 00:56:26 Yeah, what they were trying to do is basically use this context thing for some caching library.
And the thing that we have built just fit there
what they were trying to do. But it's just not the way that it's supposed to be used, and I don't think we should add features to
make things like that possible.
That's helpful.
This this use case is one that's fairly often requested to not propagate
So the stuff to 3rd parties.
Daniel Dyla (Dynatrace) 00:57:43 Yeah, I think this needs to be addressed at spec level.
But so
that was in May.
Marc Pichler (Dynatrace) 00:58:57 Yeah, I didn't follow up on actually closing it. So that's why this one still open. Usually I mark these as triage rejected and then close them.
Daniel Dyla (Dynatrace) 00:59:50 Yeah, out of time.
I think we got through quite a bit, though.
Marc Pichler (Dynatrace) 00:59:55 Aboo!
Daniel Dyla (Dynatrace) 00:59:56 Alright, I guess that's it for today. Oh, there's a bunch of chat messages.
Sorry, everybody, very.
It's all good.
Just don't notice these when I'm sharing my screen.
Looks like they're all from an hour ago, anyway. Alright!
Thanks for everybody for your time. I'll see you all next week, I guess, Mark, you're gone for the next 2 meetings.
Marc Pichler (Dynatrace) 01:00:22 Yes. Oh, I didn't realize I didn't realize I wasn't going to be around for the meetings. I should have looked into somebody to run it. I would do that. Next to this.
Daniel Dyla (Dynatrace) 01:00:33 That's fine. I can probably do it. If you can't find someone.
Marc Pichler (Dynatrace) 01:00:38 Thanks.
Daniel Dyla (Dynatrace) 01:00:38 Alright!
Thanks everyone for your time.
Trent Mick 01:00:41 Yeah, okay.
Daniel Dyla (Dynatrace) 01:00:41 Next week.
Marc Pichler (Dynatrace) 01:00:42 Thank you. Bye.
