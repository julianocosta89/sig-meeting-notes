SIG: Java SIG
Date: 2025-07-17
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/o_GFof6yMDz8hIrMP4S9vB2svYW7IPFPxDNJdSfqDNVXm_exHzW6VwApqUDmCjs.FWTZ18NbW08xztiM
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:59 Hey folks.
**Robert Niedziela** 01:04 Hello!
**GZ Gregor Zeitlinger** 01:12 Hello!
**Trask Stalnaker** 02:02 Alright. Let's kick off with the releases.
Do this one. Is this one still not passing? Okay.
I will look at that. If it's easy and push. Otherwise wait for the author.
The other one that I did look like worth chatting about
was, I think, Robert, you had
Some questions about?
Yeah.
**Robert Niedziela** 02:55 Yeah, there was some to me. It was a kind of inconsistency.
**Trask Stalnaker** 03:05 There's been discussions in Simcom specifically around this question.
whose count, let's see, clarify count guidance for up-down counters.
Yeah, it was just.
**Robert Niedziela** 03:40 There's a suggestion in some conf to use dot count suffix instead of pluralization, for up down counters, right? And here we have some metrics that
are singular without dot. Count suffix, and one of them have dot count suffix.
That just was a kind of inconsistency for me.
**Trask Stalnaker** 04:06 Hmm, yeah, it's a good question. Let's look at the so.
**Robert Niedziela** 04:18 So if you take a look at my comment, it's it's all mentioned there, I guess.
So.
Scroll down.
**Trask Stalnaker** 04:31 Okay. So at least this doesn't 2 go against this
guidance. And actually, so we did. There was a lot of there was confusion in some com around. Count like, should you add dot count to everything.
and so this was removed very recently.
In favor of just don't pluralize, but not specifically recommending dot count.
So like run dot active is fine.
**Robert Niedziela** 05:12 Okay.
**Trask Stalnaker** 05:16 So let's see. Wild side transaction committed.
I see. Let's see which ones have that account in here.
**Robert Niedziela** 05:34 Yeah, so there is this wild fly session, active count, and then, there are white session rejected without count right session created without count right that that was to me some
somehow inconsistent. But it's fine. So if others are are okay. As I said, I'm not going to
block this Pr.
**Trask Stalnaker** 06:05 So one possible reason, so that count here like we can't remove dot count here, cause there's
well, this is another discussion going on whether we need this rule in some not, but whether a namespace
can also be a metric name.
Okay.
Why not? Given the kind of lock
of clarity here on, let's see. Wait
transaction, count.
**Robert Niedziela** 06:56 And in tomcat, for example, Yaml, maybe it's overused. But in tomcat yaml actually, all metrics have
almost all metrics have dot count suffix, which are counters, not not goges, of course, but the counters have dot count suffix.
**Trask Stalnaker** 07:16 Okay, yeah, like this one.
I think probably we would be dot active.
Something like that for number of in flight is typically what we would do.
Let's see.
Okay, yeah, let's I'll I'll take a look. Thanks for explaining and try to make some
recommendation here.
Is there?
Do you know if it's there's any reason to hold not to?
is it okay to hold off on this for the release.
**Robert Niedziela** 08:11 Hold of you mean
**Trask Stalnaker** 08:13 Remove it from the I think I had removed, added it to the probably the milestone.
But yeah, I'll I'll just remove it from the milestone, and we can finish up that discussion.
**Robert Niedziela** 08:26 Yeah, okay, I think there's no rush here.
**Trask Stalnaker** 08:29 Yeah, cool.
That weren't clear.
Anything else.
Did anybody add anything here? Since we've been discussing anything anybody wants added, here, gonna kick it off today.
**GZ Gregor Zeitlinger** 08:50 We could discuss what Jack Shirazi was talking about. Jack, do you want to discuss that OP. Amp thing?
**Trask Stalnaker** 09:02 On the contrib side.
**GZ Gregor Zeitlinger** 09:05 I don't know where, but we discussed it in slack.
**Jack Shirazi** 09:11 Milestone.
I don't think there's I mean the the only thing that there is one thing in the contract which is
not Mp. It's actually this, the the consistent sampler.
**GZ Gregor Zeitlinger** 09:26 No, I mean the
the discussion you started around adding dynamic capabilities to the SDK, or am I mixing up something.
**Jack Shirazi** 09:37 Yeah, but that's not for this milestone, is it?
**GZ Gregor Zeitlinger** 09:40 No, it's not for this milestone. Sorry. I thought the question was in general sorry.
**Trask Stalnaker** 09:44 Oh, sorry.
No, no, no. Still, on this 1st topic here for the release. Yeah. Milestones.
Okay. This was, why did I add this? Oh, yes, cause it was approved.
Yeah, I will merge this for the release.
Alright,
Let's see, we.
**Jason Plumb** 10:14 Trask remind me, the order of releasing does contrib come 1st before the instrumentation or the other way around.
Okay.
**Trask Stalnaker** 10:21 Yeah, and it's very confusing either way we do it. There's it's not a.
**Jason Plumb** 10:28 That's why I'm asking, yeah.
**Trask Stalnaker** 10:30 Yeah.
**Jason Plumb** 10:31 Thanks.
**Trask Stalnaker** 10:39 Let's see. So we lost Jack to.
**GZ Gregor Zeitlinger** 10:44 Paternal leave so.
**Trask Stalnaker** 10:49 I don't.
No, let's let's move this at least to the end.
Jason.
**Jason Plumb** 11:00 Oh, yeah. So I tried. I tried this thing, and it works like kind of like.
and for some use cases it injects whatever little snippet you want into this HD. Into the head of the HTML. I didn't know this existed. There's like very little visibility on this, but you had mentioned. Some Alibaba folks were also interested in this.
**Trask Stalnaker** 11:22 Yeah, yeah, they were literally just asking about it last week.
**Jason Plumb** 11:27 Okay, this has been in here for a long time, though I think, too, right.
**Trask Stalnaker** 11:34 Yeah.
**Jason Plumb** 11:36 Is anyone on this call using this in production?
No, I know that other vendors have ROM solutions out there.
Okay.
**Trask Stalnaker** 11:59 I mean, we have it in our distro. We do have a flag, an experiment unstable
flag to enable it for our, and it will inject our rum rummy
**Jason Plumb** 12:17 Right. But it's not a different implementation. It's using the same implementation.
**Trask Stalnaker** 12:21 Yes, it's easy.
**Jason Plumb** 12:23 Sure it was, yeah. Okay, well, someone, yeah. Someone offered to
Did they delete their comment.
**Trask Stalnaker** 12:35 I. It also looks like they closed their Pr. I thought there was weird.
We are.
**Jason Plumb** 12:40 Yeah, yeah.
**Trask Stalnaker** 12:43 How did it go.
**Jason Plumb** 12:45 Huh?
I didn't hallucinate that like that really happened.
**Trask Stalnaker** 12:50 Yeah, there must have done a
Maybe a information act.
From Github.
**Jason Plumb** 13:00 Oh, their their account is no longer active on Github.
Okay, that would. Yeah.
I think that would explain it right like, maybe there's something.
**Trask Stalnaker** 13:15 Not really like there should be a record of it unless.
**Jason Plumb** 13:20 Hmm.
**Trask Stalnaker** 13:21 Github.
People expunged data, I figured.
but I could be wrong anyway.
**Jason Plumb** 13:31 Or maybe or maybe it was a bot like.
yeah, okay, well, help still wanted. I will.
We'll edit my comment here to update that there was someone who offered.
and their comment was actually helpful because they had kind of done the pre work on describing what how that feature works.
So it's unfortunate that it's just gone. But
you know it. I think it's it's probably one to 2 h of work for somebody.
**Trask Stalnaker** 14:04 I bet Copilot could spit out.
**Jason Plumb** 14:07 No.
**Trask Stalnaker** 14:07 That out.
Sorry. I've been using copilot to do a lot of stuff lately, and once you figure out what it's good at and what it's bad at.
It's surprisingly good at certain things.
Oh, yeah, I'll I'll show off what it
the release notes. These are the
best release notes that we've had.
That I've ever written.
Because I told normally I'm normally. I go through
each one, and I have to remember what it was because we don't write great title, pr titles.
**Jason Plumb** 14:53 Yeah, yeah.
**Trask Stalnaker** 14:54 So I have to open a bunch and be like, okay, this is what it is, and write something. I just told Copilot to open. Go and get, you know. Look at all the Prs and write, you know one line
description.
and then, you know, I mean I I scanned through. I mean, I read through them to validate, but
did a very nice job.
Oh, I also asked it to categorize them into enhancements and bugs.
because normally, the script just spits it all out into one and
it did a good job. It actually didn't.
No, I mean, yeah, of categorizing, anyway.
**Jason Plumb** 15:42 Well, it sounds like no one else knows anything about this this thing, but I did try, and it seems to work, and we can probably move on from that topic. If anybody wants to try this out and document it. That would be helpful. Otherwise maybe I'll find time to do that sometime
cool.
Well, now, now, everyone on this call has heard that that exists so.
**Trask Stalnaker** 16:05 Yes.
**Jason Plumb** 16:06 There's at least that cause it's buried like I didn't. I didn't know it existed, anyway, moving on.
**Trask Stalnaker** 16:15 Jason, I I will ask Copilot to do the oh, actually here!
What can we don't have so like in my for what I'm gonna do is let's see.
go to my fork.
We haven't enabled this in open telemetry yet. But okay.
I like to try to give it as little prompting as possible and see what it does.
So I assign it to copilot and
Now y'all can check in a
for this one, I'm gonna guess, like 10 min that's gonna take.
**Jason Plumb** 17:07 Yeah, that's not something any Triager can do. It's something you can do.
**Trask Stalnaker** 17:12 Is anybody that has a co-pilot license.
**Jason Plumb** 17:15 Okay? Okay, yeah, it's gonna run under your account because you did the assigning.
**Trask Stalnaker** 17:21 I also did it on my fork.
**Jason Plumb** 17:24 Oh, I see. I missed that. Yeah. Sorry. Okay.
**Trask Stalnaker** 17:26 Yeah, we have a community issue open, and we've enabled it. On a couple of repos.
So if you're interested,
there was a small Kerfuffle in how it was rolled out.
**GZ Gregor Zeitlinger** 17:50 So we.
**Trask Stalnaker** 17:51 But the
Once we enable it on one, we can enable it repo by repo
and then any. But then anybody who has right permission to the repo. So approvers and maintainers
cause. Only approvers and maintainers can assign issues to anyone.
Then, if you have that, and if you have a co-pilot license, then you can do it.
We are working with the Cncf. And Github to try to get all of the maintainers co-pilot licenses.
so that anybody could do that.
We also.
**John Watson** 18:36 I think they have.
**Trask Stalnaker** 18:37 Relay.
**John Watson** 18:38 I thought Github is all already, basically gave co-pilot licenses to all hotel Maintainers. They gave me one
they like reached out and said, Hey, do you want a co-pilot license?
**Trask Stalnaker** 18:52 Hmm! Can you? If you go to.
**John Watson** 18:58 I also have a co-pilot license through Cloudera. So
it's not not a good, not a good test of anything at the moment.
**Trask Stalnaker** 19:08 Yeah.
that's a good question. I don't know. Yeah, what if there's different variants of co-pilot licenses, or if it's just any
license, you should be able to do it.
**John Watson** 19:21 Yeah, I don't know.
**Trask Stalnaker** 19:23 We do have an easy Cla problem right now, which is probably the main reason I haven't added it to
Our hotel Repo
is that the co-pilot bot the easy Cla team is working on a fix to to make that work.
But so for now I just do it in my fork, and then I steal the code and
send it as my own pr
jay.
**Jay DeLuca** 20:01 You want to share?
Yeah. So you know, for the past 5 or so months I've been talking a lot about Yaml in these meetings, and
I decided it would be good to kind of experiment with showing, you know, just some proof of concept of some of the things that we could eventually do with some of this data. And we've gotten pretty far in terms of having a lot of data
in the file. So yeah, this isn't like deployed anywhere I don't have
it all hashed out. It's a little buggy, but I wanted to show you know, at some point, you know, we can have this this information generated into readmes, and maybe in the open telemetry documentation site.
But what I wanted to highlight is, you know, I think when we
do our update to 3 0, there's gonna be a lot of changes in terms of the emitted telemetry and so I started thinking about how we could maybe get ahead of some of the the user pain that might be associated with some of that and so one of the things that I was thinking was, I basically hooked this, the the Yaml file up to the semantic conventions and for people who
aren't familiar. The one second.
**Trask Stalnaker** 21:26 What did you just do there at something.
**Jay DeLuca** 21:31 Oh, yeah, I have. I have some shortcuts set up so I can get to like my fork. They're they're just in like your chrome settings, and then you go to search engine, and you can add.
like little shortcuts to bring it to different links.
Thank you for sharing that set that up. Yeah, no problem.
yeah. So so within this output, what we've been doing is labeling the telemetry based on certain
properties, so we could say, like what? What metrics are omitted by default versus with certain flags.
And so what I did was, I have this set up where you can see like, okay, if you're using this particular client. You could see what metrics are, or spans are emitted by default. You could see which ones are emitted. With this particular property, and then we can cross reference them to you know what semantic conventions they actually adhere to and my thought with this was, you know
we could use it, for you know, a semantic convention scorecard, or, you know, identifying what instrumentations adhere or don't but, more importantly, I think I went through, and I created like a test yaml file for 3 0, where potentially we remove this flag and have these attributes
by default, and then kind of put together. This little you know version diff to say, like, Okay, if you're going from 2 17 to the New 3 0, where semantic conventions are, we could see, like, okay, by default, you're gonna get these new metrics. We could see that these old attributes go away. These new attributes are added, and then we have, you know, full semantic convention compliance.
And then another thought with this is I think Gregor had had debited a while ago. But like there's this
command line tool that the Grafana team did in a hackathon around.
If you give it your jar file, it will look at your dependencies and identify all the different libraries within your class path. And then the idea is, we could hook that up to something like this to say, Okay, if my application
has all these libraries within it. You know, this is the resulting telemetry. That, you'll get and you can identify like which instrumentation it came from. And the idea here is,
you know, if someone has their just standard jar file, they can a identify which libraries it's using. Then they could cross reference that with all of our instrumentation and see what telemetry is emitted. And then, as we go from different versions to versions or change functionality, you know, it can output even maybe dashboard or alert syntax and changes. So.
so, yeah, all this is just like very experimental. But I just wanted to kind of put some like concrete examples of some of the tooling and capabilities that we'll get. Once we
have all this, this data hashed out.
I mean, obviously the the 1st step is going to be. I think the the focus will be generating readmes and the the documentation site. And this is just this is just kind of a, you know, an additional thing. But yeah, just wanted to put a little bit of a make it a little less abstract than just talking about a yaml file every week. So.
and you know we could. We could look to see like which one.
**Trask Stalnaker** 25:03 Oh!
**Jay DeLuca** 25:04 Implement.
So this one.
**Jason Plumb** 25:05 It is all.
**Jay DeLuca** 25:06 Awesome.
**Jason Plumb** 25:07 I just have to get out. I have to say that like this, this is really really awesome, like our. I would love to have this at our disposal. Yeah, this would be super duper, helpful.
**Trask Stalnaker** 25:17 Cool.
**Jay DeLuca** 25:18 Yeah, so.
**Trask Stalnaker** 25:19 There of a default and some comp opt in of really slick.
**Jason Plumb** 25:25 Yeah, thanks for showing that like, this is great.
**Jay DeLuca** 25:29 Yeah. So as yeah, as you as you see on my prs, that's that's what I'm working towards is the ability to do this kind of stuff, and and have nightly diffs and and all that kind of stuff. So I'm I'm excited about it, but I think it's hard for people to to understand what I'm going for with, with just sharing a file every week. So.
**Jason Plumb** 25:45 No totally like these kinds of tools are, are exactly what the metadata is supposed to facilitate. Do you think that there's an opportunity for the schema for the instrumentation list schema to be applied to other languages.
**Jay DeLuca** 26:00 So, okay, that's that's the
I need to get more involved with the Weaver group. I think because I think there's a lot of discussions about this happening elsewhere. So so, yeah, well, while I've been doing it, very, Java focused one of my next steps also is to
branch out and understand what other languages other tooling teams are doing and and kind of converge. So so yeah, I'm I'm very interested in getting involved in that kind of wider effort. Now that you know, I've kind of got a proof of concept going so.
**Jason Plumb** 26:32 Cool. Yeah.
**Trask Stalnaker** 26:33 I would.
**Jason Plumb** 26:34 Also sorry. I was also hacking on something, but using weaver to facilitate metrics searching by name and other stuff, but like, because people will come in the metric. And they're like, where does this come from? Or like? What does this? What does this mean? And they don't know how to navigate the semantic conventions repository. Because, frankly, it's it's complicated. And if you're not working in that world, it can be hard to find stuff
so like having some sort of metric surge on the doc site would be like, I think, really helpful for some for some users, but so it was like a similar thing. But yes, yeah. Appreciate what you did. Sorry, Trask.
**Trask Stalnaker** 27:09 Yeah, I I was totally thinking, Weaver, while you were showing that I would.
it would be great. If you want to join the Weaver meeting next week. And
just Demo, you know that same demo, and basically, you know, cause they are doing there is a good amount of overlap with some of the stuff that they're thinking about.
And basically just ask, you know, hey, how do we?
How do we converge to what you're working on.
**Jack Shirazi** 27:46 Cool.
**Jay DeLuca** 27:46 Yeah. And I know that they have. They have, like the concept of the live checker, which I think has some similarities. But I think one difference here is that, I think, requires you to actually generate telemetry data, and which would require you to kind of exercise all the different libraries, where I think this approach at least gives you like the possibilities based on, like your code, base of your your application, might not necessarily generate all of these, but like it could.
But yeah, so yeah, I could certainly come to that that meeting and and talk about it more.
**Trask Stalnaker** 28:17 Yeah. The part that I'm interested in there with the convergence potentially is around.
The schema definition.
So they're working on a telemetry schema. 2 point. Oh.
if you've seen our telemetry schema one, it's the basically it's that schema file that only has the things that were added or removed in the next version. It's not like a schema. Which is what you're doing is like a schema of all this stuff.
And so that's the piece in particular. That would be interesting if
I don't know how far along they are with that project and what we can
collaborate on from that perspective.
**Jay DeLuca** 29:10 Cool.
**Jack Shirazi** 29:11 Okay? Are there.
**Jay DeLuca** 29:12 All I got. Thanks.
**Jack Shirazi** 29:13 Are there in other instructions to try it out anywhere, or is it still too raw.
**Jay DeLuca** 29:19 It's still too early. I'm gonna polish it up and get just this, you know, like I said, this isn't production code. I use like Gemini, and came up with this in a few days, and I've just been using it to experiment. But yeah, I'll put it up somewhere so people can
play with it, and and all that. I'll I'll post in the Channel or
report back once it's somewhere someone can play with it.
**Trask Stalnaker** 29:47 Oh,
Alright we're still gonna bump my topic down.
**Jason Plumb** 29:56 You're not sharing Trask.
**Trask Stalnaker** 29:58 Oh, thank you.
What to do about.
**John Watson** 30:08 Yeah. So we got a a Pr from renovate here to update our Kotlin plugin, and it is
causing the Api diffs to fail with the very cryptic Kotlin.
**Jason Plumb** 30:22 Ow.
**John Watson** 30:23 Binary
failure diff, and I have. I do not know what we like, what we are, what we should do about this I don't understand.
**GZ Gregor Zeitlinger** 30:34 I think, already taken at it today.
So it is about a Kotlin metadata he had yeah generated, and
I was trying to exclude that it hasn't worked, but I think it's the correct way to exclude that, because it looks generated.
**John Watson** 30:56 Cool if you can figure out, figure that out. That would be awesome. Because I I took a brief, a quick look at it, but I don't have time to dig in. So if you have time to dig in and can figure out how to exclude that metadata that would be fantastic because we've run into this before, and I just didn't remember how we had dealt with it before.
**GZ Gregor Zeitlinger** 31:15 Well, I've seen that there is a script part that is doing, some tweaking, not for this, but for others. So.
**John Watson** 31:22 Yeah, because.
**GZ Gregor Zeitlinger** 31:23 There must be some setting that I have not found out so far.
**John Watson** 31:29 Cool. Yeah, if you can. If you can figure that out. That would be fantastic. Ping, me, or yeah, ping me, or tag me on a Pr.
If you figure it out.
**GZ Gregor Zeitlinger** 31:38 Okay.
**John Watson** 31:40 Fantastic. Thank you.
**Jay DeLuca** 31:47 If we could go back to I I just I forgot that I had that question around so I was thinking that I would
kind of target getting something, you know, up and running before we do the 3 0, but I realize I don't really have an idea of if we have any idea of when that's coming. So just wanted to ask that.
**Trask Stalnaker** 32:09 So we've got a few things float, few ideas floating.
**Jack Shirazi** 32:21 There. There's a page with 3 0 milestones somewhere.
**John Watson** 32:27 We lost the Trask.
**Jack Shirazi** 32:29 Yeah.
if anyone remembers where that page is, you can go ahead and show it.
**GZ Gregor Zeitlinger** 32:39 Isn't it a milestone.
**Jack Shirazi** 32:42 Yeah, that's right. There's a 3 0, milestone. And it's got a bunch of issues against it.
**Trask Stalnaker** 32:51 No idea what happened there.
I was here, and then one second, and then I wasn't.
**Jack Shirazi** 32:59 Yeah, I was just saying that there's a 3 0 milestone and there's a bunch of issues open against that. So.
**Trask Stalnaker** 33:07 Good point
I don't have. Why isn't the database one in there?
This one should be in there?
Yeah.
Do we have the in the
I mean. I know it's not a required for trio, but a nice to have.
**Jack Shirazi** 34:07 Yeah, we're we're we're putting as much as we can into that. So I think, says I was also gonna wind onto that one as well.
**Trask Stalnaker** 34:15 Awesome.
**Jack Shirazi** 34:16 It's just chugging through all of the
the automated ones to make them manual.
**Trask Stalnaker** 34:26 Cool, and that one was I just didn't search for the right thing. Invoke. Dynamic is in there.
And then we'll see. I don't think, Gregor, that the declarative config needs to
be tied to that, since it's a brand new thing, and so there's nothing that we would be breaking.
I think the invoke dynamic. We want to get in so that we can deprecate the old way.
**GZ Gregor Zeitlinger** 35:07 The only thing related to declarative configuration I can think of is having the spring assist changed with the new format.
but this is only for autocompletion and documentation.
**Trask Stalnaker** 35:26 Spring assist.
**GZ Gregor Zeitlinger** 35:29 So that in your editor you
get the suggestions for the declarative configuration-based properties which will be embedded into the main spring file.
**Trask Stalnaker** 35:41 Oh, okay, okay. But will that be? A breaking like, will we still support the old format? Or or would we snap at some point basically to the new format for spring
properties.
**GZ Gregor Zeitlinger** 36:00 To be discussed. So my current plan is just the documentation. But we could also, completely remove the old one if if we want to.
**Trask Stalnaker** 36:12 Can we support them side by side for a while.
**GZ Gregor Zeitlinger** 36:15 Yeah, yeah, this is the current. Pr, so it's based on whether you have this opt-in flag or not.
**Trask Stalnaker** 36:22 Okay, yeah. Yeah. So if that is, if we are stable
by 3 0 for declarative config, then we could.
I like the idea with kind of these big breaking changes of
deprecating the old in 3 0 and running side by side in the 3 0 major version, and then 4. 0, we could drop
the old.
**GZ Gregor Zeitlinger** 36:52 I like that.
**Trask Stalnaker** 36:52 Version.
Oh, let's go see what
copilot did.
Okay, a bunch of nonsense. Okay. I don't understand why, like I need to fix the prompt to be like don't make unnecessary changes like, why.
why did you commit the build? Scan?
Okay, Javascript. Snippet injection.
Inject for some server applications.
Head tag.
Save monitoring. Oh, look at that! Not bad.
It followed our format here.
Snippet to inject which one read, okay, okay.
Example. Nice nice notes. Let's see.
**Jack Shirazi** 38:21 Pretty good.
**Peter Findeisen** 38:23 Yeah, it is.
**Trask Stalnaker** 38:29 It's a it's a brave new world.
I will send this Jason.
**John Watson** 38:40 Yeah, I've also found that Copow is fantastic at generating documentation, especially if there's already examples in the repo of what it should look like.
**Jason Plumb** 38:49 Cool.
**Trask Stalnaker** 38:50 If you're
a fun failure copilot failure. I asked it to fix the Java Doc. Build errors yesterday, and it fixed it by just removing the flag.
**John Watson** 39:03 Yes, the classic way to to get rid of your errors just.
**Trask Stalnaker** 39:07 Yeah.
**John Watson** 39:08 Ignore them.
**Trask Stalnaker** 39:08 To allow Jama Doc to succeed Goodwith. Lordy's.
**GZ Gregor Zeitlinger** 39:14 I've seen engineers come up with solutions like that.
**Trask Stalnaker** 39:19 It's true. It it is a way.
Oh.
alright! I don't think I quite have the
energy to drive this right now, unless other people want to
alright anything anybody else wants to chat about today.
**John Watson** 39:51 I'm gonna be out next week, so we will be completely maintainer free in the core repo for at least a week.
**Trask Stalnaker** 40:00 All right.
**GZ Gregor Zeitlinger** 40:01 Like, I, said, John. If you would raise me a level I would be happy about that.
I'm Triager now.
**John Watson** 40:10 Yeah, that's not the same as maintainer, though maintainers are the ones with the merger, merge mergeability.
And yeah, so.
**Trask Stalnaker** 40:21 Keep contributing Gregor.
**John Watson** 40:23 Yes, keep contributing, and all as always, code reviews are the most valuable thing that you anyone can possibly contribute.
They're they are the thing. That is the what main, at least in this project. And I think it's probably true. Across almost all open source project is is thoughtful. Deep code reviews are the most valuable thing that can be contributed.
**Jack Shirazi** 40:50 So so since we've got a bit of time, just a quick question, maybe, in the contrary brief, I've got a Pr that's
sitting there.
And Peter's
approved it, but he hasn't got so that he's a code. He's the code owner, but he hasn't got the ability to actually approve it
as in approve like, you know, he's got the tick there, but it's not a green tick. It's just a tick, and I'm wondering
how I mean is, is there anything that we should be changing for a country Repo to
allow code owners to be able to ticket? But I mean, that's going to be really complicated if we do.
**Trask Stalnaker** 41:33 Yeah, it just relies on
one of the maintainers paying better attention.
Generally, if it is approved and feel free to ping me, because generally, when it is approved by one of the component owners.
I will just merge it.
**Jack Shirazi** 41:55 Okay, so that's that's the
the bar. We say, just one component owner to approve it, and maybe another approver and another
review or something I don't know.
I don't know what you're.
**Trask Stalnaker** 42:07 Not even that. No, I I'm looking for one component owner to approve it.
And.
**John Watson** 42:14 In trip. I think it's the component owners job. That's that's their job. And if somebody approves it.
it goes.
**Trask Stalnaker** 42:22 Yeah, I mean, I'll I'll I'll take a quick scroll just to make sure there's nothing like
crazy but
**John Watson** 42:32 Yeah. Also, just, I think, feel free to if there are
things like this that just need an app need a maintainer to to merge
in, contrib. Feel free to tag like I definitely look 1st at the things where I'm tagged in Github like, if you just put me on the mention me in it.
I'm happy to. That is one thing I do have time to do is to click the merge button.
**Jack Shirazi** 42:59 Yeah, I mean, I wasn't in a hurry for it. It's a it, didn't. It? Wasn't. I didn't need to ping anyone else. Just curious about what we're looking for. That's it. Thank you.
**Trask Stalnaker** 43:10 This one I was trying to. I was trying to follow this one, Jason.
I didn't quite get through it, but.
**Peter Findeisen** 43:21 Yeah, where's that?
**Jason Plumb** 43:22 Yeah.
**Peter Findeisen** 43:23 This is a bit tricky. Yes, sorry.
Well, so there was some confusion originally, whether, if we I'm not sure if you guys are really familiar with this concept of consistent probability sampling. But So
instead of relying on the sampled flag we want, we see the threshold value and code it in the trace state and in normal situation. This gives us enough information to proceed. I'm talking here about parent
based sampler, which takes the state of sampling from the parent, and wants to do the same thing for the child.
Now, just in, just to
make life easier for those who are mixed have mixed environments, and definitely, there will be such environments. We want to support also the legacy sampling for the parent which does not provide the threshold, but provides the sampled flag.
In this case we do not know what was the probability of sampling for the parent.
Therefore we don't know the sampling probability for the child. We just copy the sampled flag.
But in certain situations, when we
wants to limit the rate of sampled spans at the child level.
this causes some issues because we we do not sample with
same probability as the parent which is unknown. But you still can can be the same.
We want to sample with a specific probability that requires comparing the threshold with randomness value that randomness. However.
if in this scenario we don't know anything about it, because it could be abused a at the parent level.
That's in very brief description of the situation. It it is a corner case, maybe, but we need to fix it.
So the solution is to use a new randomness value in such situations, which we know that has the proper distribution.
**Jack Shirazi** 45:54 Well, while while we're here.
it's the the the version that you've got the like, the 56 version that's now stable.
whereas the old version that's actually in the core repo is experimental for trace id ratio.
I'm just wondering whether we're just gonna leave it as is because I'm.
**Peter Findeisen** 46:19 The old one.
**Jack Shirazi** 46:20 Yeah, because it yeah, but in not in the contribut repo, but in the core repo, the the trace id ratio that was experimental, and they've now gone stable on the the sampling, the sample
but the the so the core repo doesn't use the stable version. It uses the experimental version, and I'm just wondering whether there's any plans to do anything.
**Trask Stalnaker** 46:46 Jack. Do you mean that they change the hashing algorithm.
**Jack Shirazi** 46:53 Yeah, for the sample.
**Peter Findeisen** 46:58 Well, but the
trace id ratio sampler I consider as a legacy sampler, whether it's a new version or not, because it's not
recording the probability.
**Jack Shirazi** 47:13 Yeah. But what I'm saying is that the the version that you've got in the contrib repo? That's that's correct. That's the stable version
that's now in the spec.
**Peter Findeisen** 47:23 But.
**Jack Shirazi** 47:24 And the version that's in the in the core repo is not, is not the stable version, I think?
Yeah. So.
**Trask Stalnaker** 47:33 So this got changed. So the actual this got changed.
**Jack Shirazi** 47:38 Yeah, this is this, I think you're looking at the stable one, and
the the sampler that's in the core repo is the is using the experimental one, unless that's been changed.
**Jason Plumb** 47:56 We should fix that.
**Trask Stalnaker** 47:59 I mean, that's isn't gonna break people.
**Jack Shirazi** 48:03 Exactly. Yeah.
Distributed traces could use a different name. I mean, it can be a different name sampler. So that
with that, so then it would be non-breaking
or we could just leave it in contrib, because it's all there and working, or Peter's implementation is all there working.
I more of interest from from me rather than any requirement. We're just gonna use the contribut.
**Trask Stalnaker** 48:38 Yeah, I mean, I'm really looking forward to the consistent sampler stuff and propagating and trace state. Because then you don't have this problem of having different hashing algorithms on different rolling out things.
did we discuss? Wow, yeah, I wasn't following this.
Yeah, I don't know what we should do.
He just didn't.
**John Watson** 49:09 This is a breaking. This is a breaking change in the spec.
**Trask Stalnaker** 49:15 There's a weird thing where they didn't really define it in this.
**Peter Findeisen** 49:22 Right. The thinking was that the original specification for trace id ratio based sampler was not really prescribing any concrete algorithms.
So there was a number of notes related to this one of the
recommendations was to use on use it only for root nodes root. Sam root spans so that would never cause any any issues. If if it's used for non root spans, there could be some issues.
The algorithm was not the same for depending on the platform. For example, different languages had different algorithms.
**Trask Stalnaker** 50:14 So, John, this is what it said 4 months ago.
**Jason Plumb** 50:22 Hmm.
**Trask Stalnaker** 50:23 that's what the spec said.
And so everybody just went and implemented this in some way.
And now the spec has a prescribed algorithm for.
**Peter Findeisen** 50:42 Yes.
**Trask Stalnaker** 50:43 This.
But yes, I feel like it is a breaking chain like, while it might not be a breaking change in the spec. It would feels like it would be a breaking change in the SDK.
**Jack Shirazi** 50:57 It would, if you use the existing sampler rather than bring in a new named Sampler, which.
**John Watson** 51:04 The new naming thing makes me think. And then maybe, Trask, if you could take this to the
maybe this is a Tc issue.
Like, if we, if we were, just change the implementation here and it is going to break people.
then. That's a problem.
We need some. We need some recommendations, I think, about how should deal with the the fact that the
although this, the api specification, is nothing has changed.
The implementation will be breaking. People.
**Peter Findeisen** 51:45 Well, yes, but only if they did not follow the recommendation right? So.
**Trask Stalnaker** 51:52 Of only.
**Peter Findeisen** 51:53 Of only using it for root spans.
**Trask Stalnaker** 51:56 I see right, parent always doing parent based and and propagating that.
**Peter Findeisen** 52:02 Yes.
**Trask Stalnaker** 52:02 Across. Yeah.
yeah, I'll I'll add that John to the spec meeting.
**John Watson** 52:17 Yeah, just having some having, especially without with basically no maintainers at the moment having some advice from the
Tc. Would be helpful. I think.
**Trask Stalnaker** 52:34 When did that change? Okay,
okay.
Back to this, Peter.
This example. Here?
So are you, does. Are you saying here that this is what happens today or.
**Peter Findeisen** 53:32 This is what happened. Yeah, this is what happened.
**Trask Stalnaker** 53:34 And.
**Peter Findeisen** 53:36 This is what happens today with consistent probability samples prototype, which is which is in the country prepository
and.
**Trask Stalnaker** 53:48 Can you ex, walk through, explain.
**Peter Findeisen** 53:52 Okay? Okay? Sure. So
well, the 1st step using legacy always on sampler for the parent span. We all know that it will set the sampled flag for all parents spans, and it will be propagated
along to for the children's.
Now
for the child span. If we use a consistent rate limiting sampler and using the parent sampler as a delegate just for those who are not familiar with this. So this works like it's first, st ask the delegate for suggestion about what threshold to use.
and then it will trim this threshold accordingly, to arrive at the at the prescribed rate of spans. So the consistent, pattern-based sampler with that when it doesn't see any
threshold, but sees the sampled flag, it has no choice but to select the threshold as 0, which means sample, all
which is consistent with intentions of the user. Apparently.
The then, if we want to trim it by 50%, the consistent rate limiting sampler, we will
provide threshold, which is
2 to to the power of 55, which is half in the right, in the middle of the
interval for for the distribution, for the randomness, right? So
it will cut off 50% of
of spans and pass at the other one.
**Trask Stalnaker** 55:40 This at this point.
**Peter Findeisen** 55:42 Yes, at this point. Now.
**Trask Stalnaker** 55:44 Okay.
**Peter Findeisen** 55:45 For the grandchild spans, which look again at
**Trask Stalnaker** 55:52 Sorry I didn't quite hear them. It's a rate limited sampling
at 50 spans. Oh, I understand what you're saying. It based on the it's seen we're getting a hundred spans per second, and we want to down sample to 50 spans per second.
Yes, at that instant it's a 50% sampling decision.
**Peter Findeisen** 56:17 Yes.
**Trask Stalnaker** 56:17 Hello!
**Peter Findeisen** 56:18 So the the last 3rd step, using again the same setup.
It will. It will see 50% of incoming spans as sampled, and
it will want to the consistent rate limit exemplar. It's step 3 will want to raise the threshold
again to the value that would
provide 25 spends per second. However, it will not work if we use the randomness value
which is embedded in the trace, and that's because the population of
spans that we see as sampled does not have.
the randomness uniformly distributed across the interval from 0 to to the power of 56. Instead, it will have
this randomness value, only populating half of that interval the upper portion.
because in this second second step.
**Trask Stalnaker** 57:33 Threw them away.
**Peter Findeisen** 57:34 Already throw. We have thrown away
the lower part of the span randomness.
That's why, when we have to deal with legacy samplers, we have to create our randomness value each time
from scratch. And that's that's the change that that it's suggested here.
So it it is a little bit tricky to explain. If you guys want to have a deeper understanding, please ping me directly.
**Trask Stalnaker** 58:12 Oh, I we could have a whole
meeting about that topic if people are interesting, listed
I I've been following enough that I think I get it. But it's taken a lot of time for me to follow it. That much.
**Jason Plumb** 58:31 That's exactly what my comment is getting at. It's like I had to read it like 3 times at least.
to figure out.
**Trask Stalnaker** 58:37 So I mean.
**Jason Plumb** 58:37 Why this did that?
**Trask Stalnaker** 58:38 You're
you also have to have been following the spec and the trace state propagation and the randomness difference between the randomness value and the threshold that are being propagated in trace state. There's a lot for us to
that as we roll this new sampling out to everybody that will be good to understand.
**Peter Findeisen** 58:59 Yeah, the whole thing went unnoticed because we decided almost in the last moment.
Then we want to have some user friendly
interface or interfacing with the legacy samplers pre. Our original thought was to drop any any
spans if they want to use parent-based sample parent based sampler, and the parent does not provide the threshold, then we are
dropping the span that would work. But it wouldn't be user friendly.
So that.
And unfortunately, this introduced this complication here.
**Trask Stalnaker** 59:49 Cool. Thank you.
All right. We hit our time window. Thanks, everyone.
See ya.
**Peter Findeisen** 59:58 Right.
**Jason Plumb** 59:58 Bye.
**Robert Niedziela** 59:59 Bye.
