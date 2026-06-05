SIG: Python SIG
Date: 2026-06-04
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

Mike Goldsmith 00:02:15 Hi, everyone.
Lukas 00:02:21 Hello?
Tammy Baylis 00:02:21 I'm… I'm Mike. Hi, everyone.
Dylan Russell 00:02:25 Blue.
Aaron Abbott 00:03:00 Alright, hello everyone, sorry I'm late.
Mike Goldsmith 00:03:02 Hey, good morning.
Tammy Baylis 00:03:04 Aaron.
Aaron Abbott 00:03:06 Hello?
I think… I'm driving today, so let me… Share.
Oh, wow. Oh, no, we just didn't update the date.
Yeah, folks, please add your names to the attendees, and any topics you have, please?
Looks pretty light today.
Okay.
Let's get started, I guess, on the triage.
Tammy, do you want to drive? Do you want to share your screen or anything, or…
Tammy Baylis 00:04:02 I'll… I'll just strive for today, so I'll, Sorry, my throat has something going on, but I can share screen and just… do the… triage… Share the board.
Light mode. A, okay, we'll just take 5, maybe 10 minutes, and see what's going on.
Yeah, I guess I could go left to right. I will skip the chore, build, bought PRs.
And just look at what might be new in no status.
Copy change log updates… Oh, also… Also, from a bot.
Hmm…
Aaron Abbott 00:04:54 Change log…
Tammy Baylis 00:04:58 I don't know that's… that's probably accurate.
Aaron Abbott 00:05:05 Maybe we just missed this one from the last release, or maybe it was blocked. I think Ricardo did the patch release last week, and .
Tammy Baylis 00:05:14 Got it.
Aaron Abbott 00:05:15 I will take a look at these, yeah. I don't… I don't remember seeing any messages in the From him, but…
Tammy Baylis 00:05:22 Yeah, I'll just do a CC.
of you. Thank you.
Okay, next one… Where did it go?
GRPC, add support for metrics.
There is a linked issue.
I'm 2025, so… Not too long ago…
Aaron Abbott 00:05:58 Yeah, I think… I think Leighton asked me to review this, But I haven't had a chance to do it.
Tammy Baylis 00:06:09 Yeah, no worries.
Aaron Abbott 00:06:12 Wayne, are you around? I see you left a comment there.
I don't think he's here.
Yep. Yeah, this one needs reviews, I guess.
Tammy Baylis 00:06:26 Okay.
Ready for review?
I'll leave that for now.
DBAPI, suppress async cursor spans… No linked issue, but we have a description.
Hmm… Seems to be tested in stock.
Yeah.
Aaron Abbott 00:07:04 It makes sense to me.
Tammy Baylis 00:07:06 Yeah.
Got tests, too. Okay, I'd say that's ready for review.
Next, build add lib instrumentation for all Django middleware spans.
Two weeks ago… Fixes… Another 2025 issue, probably still relevant, about… Yeah, middleware spans not being captured.
Okay… I'd say that's ready for review.
Aaron Abbott 00:07:46 Tammy, would you mind just dropping a comment to fill out the PR template on this one?
Tammy Baylis 00:07:54 Oh, yeah, that's not great, so I'll do that.
Way… template.
Just wondering why… Why reviewers aren't being picked up here.
Aaron Abbott 00:08:34 Yeah, that's weird.
Mike Goldsmith 00:08:37 It was originally a draft that got converted to a…
Tammy Baylis 00:08:46 Yeah, kudo.
Mike Goldsmith 00:08:47 Yes, it got… yeah, 2 hours ago, got Mark Paul ready for it. That should add… The approvals list, I'll… I can check to see why that hasn't happened.
Tammy Baylis 00:08:55 Oh, thank you, Mike.
So we've been doing this 4 minutes, we can go one more minute.
Fix Kafka. Avoid recording incorrect partition when using random partitioner.
No linked issue, but pretty good description.
Although the checklist is gone.
Mike Goldsmith 00:09:31 But it does have the fixes at the bottom of the description to issue two.
Tammy Baylis 00:09:35 Oh, thank you. It's at the bottom!
I do kind of miss having that, the tick boxes with the unit test done, change lock done, but… I'll just… Say it's ready and comment accordingly.
Mike Goldsmith 00:09:58 This is also one that got approvers listed as, sorry, assigned reviewers.
Tammy Baylis 00:10:06 Yeah. Hmm.
Aaron Abbott 00:10:08 Maybe it's just.
Mike Goldsmith 00:10:09 There's something going on with one of our workflows.
Aaron Abbott 00:10:13 That one… that one usually is the code owner's file, right? I don't…
Mike Goldsmith 00:10:18 Yes.
Tammy Baylis 00:10:22 Jesus.
I guess there's no owner for the Kafka instrumenter, maybe?
Mike Goldsmith 00:10:29 It should do, so if it can't find a directory, it should then keep walking up the tree until it finds the route, and I'm pretty sure approvers will be like, the Python approvers group should be set as the root, so it should walk up until it reaches that.
Tammy Baylis 00:10:45 Yeah, that makes sense.
Leighton Chen 00:10:48 I believe it gets populated by component owners as well.
Mike Goldsmith 00:10:54 Okay.
Tammy Baylis 00:11:07 Okay.
Thank you, there's always more to look at. I'll cap it off for today, and we'll… Let someone do the topics!
Aaron Abbott 00:11:24 Yep, I can share again.
Thank you so much, Tammy.
Mike Goldsmith 00:11:29 Thank you, Tammy.
Leighton Chen 00:11:30 Thanks, Tammy.
Aaron Abbott 00:11:32 Alright.
Who's kicking it off late?
You wanna talk about…
Leighton Chen 00:11:42 Yeah, A LinkedIn issue there, and this was the… it was like a two years ago issue, but this was the last kind of tracking issue related to… migration plan for semantic conventions, Originally, it was only targeting HTTP, but I think we extended it to database as well.
So all of the… I believe all of the migrations actually have been finished.
At least the ones listed there.
But we've never… I think the conversation kind of died down a little in regards to actually, Whether or not we want to deprecate old attributes, and, like, the timeline for moving on past to have the new semantic conventions, at least the stable ones, be default.
The last I recall that we discussed about this was give… giving them, like, a… incubating time, which was, like, 6 months to a year, I believe. I don't remember, too clearly. But we never really executed on that plan.
The reason I'm bringing this up.
now is because I think a majority of the instrumentations have implemented, double pumping of the Semantic conventions with the flag.
So the natural next step would be to, like, decide how long we want to keep this.
Aaron Abbott 00:13:22 Right.
So, I mean, keep me honest here, but we're way past the required amount by the spec already, right?
Leighton Chen 00:13:31 Yeah. Yeah.
Aaron Abbott 00:13:35 Yeah, so I, I guess…
Leighton Chen 00:13:37 I guess.
Aaron Abbott 00:13:38 would the first step be to, like, change the default, and then remove the support for the environment variable altogether? I'm a little bit fuzzy, but… I feel like it's time, and Yeah, we should do it, it's just a matter of communication, right?
Leighton Chen 00:13:55 Right, right. And I guess the… the execution of it, can be discussed. I think just the bigger… Maybe more pressing matter is, like, whether or not I mean, we probably should, but, like, alongside, changing the default behaviors, like barge instrumentation is stable.
Might be a good chance to do that, especially because, you know, this would be breaking for sure, so…
Aaron Abbott 00:14:28 Yeah, yeah, I like that, Lynn.
Lucas, you wanna go ahead?
Lukas 00:14:33 Oh, I was just gonna mention, I thought we brought up… I don't know if we ever ended up implementing it, but changing the default for the Semcov opt-in to be HTTP.
Did we ever do that? Or…
Leighton Chen 00:14:49 I believe it's still default, how was the…
Lukas 00:14:53 So…
Leighton Chen 00:14:55 Yeah, I believe it's still defaults. I can double check, sorry.
Tammy Baylis 00:14:59 Yeah, I'm pretty sure the default is… is none for both HTTP and DB right now.
Lukas 00:15:07 Got it. Yeah, I would think that we should start by setting the default to HTTP.
And then, we can… I would want to, like, remove the… code that handles the HTTP migration?
And then we can bump the version for, like, those specific instrumentation libraries.
to, like, one dot… Whatever.
Leighton Chen 00:15:37 Lucas, question. Are you implying that you want the ability to still revert back to old semantic conventions and provide users with the option to do that in the interim?
of the HTTP.
Lukas 00:15:55 Yeah, I think that was the discussion, was that we could set, by default, the opt-in to be HTTP, so people could potentially switch back to the old that they wanted.
And we would not do a hard version bump, maybe?
Yeah, I don't know what other people think, but…
Aaron Abbott 00:16:15 Has everybody seen this part of the spec here?
I think it gives… pretty direct guidance for this. It says, I guess since we never had a major version, we're just treating the existing Experimental version as, like, de facto stable so far.
you know, it says, should maintain existing major version, which is what we have right now for at least 6 months. I think we've already done that after it starts submitting both sets. Should drop environment variable in the next major version.
And I think… yeah.
Mike Goldsmith 00:16:51 Right, so the sixth one starts once you've got the option of having the environment variable to do both.
Leighton Chen 00:16:59 Yeah, and I think we're compliant with that already. I think the point that, like, Lucas's suggestion, or not maybe his specific suggestion, but maybe what we decided, the first point here says that We probably need to change the default And market stable, and kind of, like, the same time.
I'm actually leaning towards that, actually. Especially because it's been so long, and I think we should just, especially because it's, like, bumping a stable version, we should just, like, rip off the band-aid, in my opinion.
Ludmilla, yeah, sorry, hand up.
Liudmila Molkova 00:17:44 Yeah, there's… like, there is a theoretical part there, the practical part is that the time, was given for backends to start supporting new semantic conventions.
There are a lot of language ecosystems that switched the default or dropped the old conventions completely, and at this point, all backends should be ready for… to receive new conventions.
And if they aren't, like, Python is just one of their problems, will be one of their problems. So I, I think from practical perspective.
I think it's fine to drop old stuff at this time.
Or at least switch the default.
Aaron Abbott 00:18:36 Yeah.
And what do you think about Leighton's suggestion of doing it in the same… doing the major version bump, and then doing that at the same time, so that the breaking change is pretty clear?
Liudmila Molkova 00:18:48 doing, yeah, like, signaling that HTTP instrumentations are at V1 is an awesome thing. I'm curious what it means for the whole distro, though.
Leighton Chen 00:19:05 Boom.
Liudmila Molkova 00:19:05 But here.
Like, major version bump, drop legacy. Yay, let's go.
And stabilize up in telemetry instrumentation, because it's a dependency, right?
Leighton Chen 00:19:19 Yeah, Yeah, a little bit, I was, gonna say, and Lucas kind of commented on this too, He's asking, do we want to try to do this for all packages in a single release, so we don't have a mix of all the new packages?
I think practically.
Like, it's really good to not have a mix of all the new packages, but practically, like, Stamping, stability.
possibly could not… it might not… the scope of it might not only just be semantic conventions. I think there are discrepancies between instrumentations that, for example, like, certain configuration parameters or, like, environment variables that might exist, That… are not necessarily maybe spec-compliant, or not, like, well-defined.
at least when I was going through the HTV instrumentations, There were some… a few discrepancies, and… I think marking a package stable would… probably need more scrutiny, than just, like, hey, like, I got rid of the old semantic adventure symbols, and I'm removing the stability opt-in.
That's just my opinion, though. I'm open to other suggestions.
Aaron Abbott 00:20:43 Maybe as, like, a… You can all tell me that this is a bad proposal, but what if we did… the V1.
And we made this change to change the default, and then just… looking at the pace that we've currently had, we work on, you know, removing some of these old options and whatnot, and by the time that that's done, we would do a V2 release.
Leighton Chen 00:21:14 So, so V1 would be, changing the defaults without marking it stable?
Aaron Abbott 00:21:20 No, I mean, it would be stable, but we would… you know.
Not have to deal with all the other stuff that you mentioned, like parts that we're not compliant with, parts that… I've, you know… like, API inside of the code, stuff like that.
Leighton Chen 00:21:36 I got it. So, so we'll release a 1.0 of all instrumentation packages, And just change the default and remove the opt-in. And then we'll have a… For specific packages that perhaps introduce some configuration settings that we weren't sure yet, we will scrutinize those and then Are you proposing to release a 2.0 for those packages, or…
Aaron Abbott 00:22:03 Well, yeah, I guess what I'm… what I'm proposing is, like.
I forget, I forget what the proposal's called now. Not stable by default, but not general availability, not stable by default, whatever we landed on, like… Just… You know, do the normal thing that software does, where we… Make breaking changes in a major version bump so that people can Figure out what's changed, and, like, if we're planning to just leave stuff around.
de facto stable, like, people are gonna use it that way, we might as well treat it like that.
Liudmila Molkova 00:22:36 And I think this is the path Java follows. They planned for the major version bump, and I think they've… they are… the agent is at version 3 now.
And they bundle breaking changes together. So, like, for the configuration options where public APIs, it would look like we deprecate… well, it's tricky in Python. We mark this as deprecated, what we don't like, right? We introduced the common thing, it's not breaking, but at some point in the next 12, 24, whatever months, once we're ready, we're saying, okay, we are removing all the deprecated stuff, we are marking everything else as the primary way to interact with it, and here is the next major version.
Leighton Chen 00:23:25 Yeah, I like that. I feel like we should take a… learning from Java and be a bit more brave with the major version bumps, and maybe…
Aaron Abbott 00:23:38 Yeah.
Liudmila Molkova 00:23:38 and stability.
Mike Goldsmith 00:23:40 Yeah.
Right now.
Yeah, just don't… don't do what God does where they don't upgrade anything past 1.
Aaron Abbott 00:23:53 Yeah.
That's where we are right now, so… Yeah.
Does anybody, like, disagree?
I'm sure a lot of you are OpenTelemetry users as well outside, like.
I personally think this is a better experience for users, because the semantic versioning is capturing, like, the semantics, right?
any dissenting opinions?
Mike Goldsmith 00:24:21 No, I think somatic convention changes at a major bump is expected, like, you expect those things to change, because even if the instrumentation doesn't change, how it describes what it's doing should change at that point as well.
Aaron Abbott 00:24:35 Okay, cool. And then I guess, so the thing we didn't really decide is, do we want to just do it all at once, just to kind of… I think that would make sense based on what we said, like, It's already de facto stable, we can… remove this option, and then do our V1 release of at least HTTP conventions. I think DB are also kind of in scope from this, issue that you shared, right, Leighton?
Leighton Chen 00:24:59 Yeah.
Yeah. I'll do an audit of, like, whether or not it was complete, because I didn't take… pay as much attention to DB, but I believe there was a lot of efforts behind DB already, so I'll take a look.
Aaron Abbott 00:25:16 Bovee?
That's awesome. I… if somebody… I don't know if anybody's taking notes in the doc. I tried to write down some of what we're doing here in the… They have issue.
Leighton Chen 00:25:33 Oh, thanks for that, Aaron. I was just gonna comment on the issue.
That's good.
Aaron Abbott 00:25:36 Oh yeah, if you have something better, then please.
Leighton Chen 00:25:40 Yeah, I'll take a look after it, thanks.
Aaron Abbott 00:25:42 Okay, this is a bit incomplete, but I'll just finish writing it.
Jeez.
Lukas 00:25:48 One last thing to just comment on. So it's… it sounds like we're gonna do the… try to do the V1 bump for this, all the HTTP packages in a single release.
So, I'm imagining we're just gonna basically… update the code to always set the HTTP SEMCOV mode to HTTP stable.
We'll probably want to have some follow-up work, though, to, like, remove all of the… SHIM code that existed before to support both But that can be done after the V1 release.
Does that sound… is that what we're planning on doing?
Leighton Chen 00:26:35 Yeah, I like, I like that idea.
I think the removal of the shim code, it will take… A lot longer.
And it's probably a bit more complicated to do it in one go.
and when I say complicated, it means more, I guess, more error-prone.
So changing the default HTTP is pretty simple. So that we could confidently, kind of, like, release a stable and, Be sure that the only change that was involved was the default behavior change, so…
Aaron Abbott 00:27:16 Cool.
Maybe… we should probably move on to some other topics we've got, some other stuff in the agenda. I guess… one, I think there's some dependencies, I don't know if they're called out in the issue, Leighton, but, like.
I think we need to mark the main semantic convention package stable. We need to mark, probably, the instrumentation package. We need to at least do something to avoid creating dependency conflicts for people.
If they're, like, mixed between stable and unstable, This is probably stuff we need to do anyway, but, Yeah, do you know if it's captured in here?
Leighton Chen 00:27:52 No, it's not. I'll, I'll investigate and, add some more detail.
Aaron Abbott 00:27:58 Man.
Cool.
Tammy Baylis 00:28:01 Yeah, thank you, Leighton, for, doing the audit of everything. I appreciate it.
Leighton Chen 00:28:09 Yeah, no problem.
Aaron Abbott 00:28:13 Great.
Lucas.
Lukas 00:28:23 Hi, yeah, this is just a small issue, Someone brought up an issue in, I think, the Python Slack.
About… You know, dealing with, UV corn, like, process forking.
And we don't currently include service instance ID resource attribute by default. I did notice, like, Mike, that we added this in the declarative config by default.
So, I guess I'm just wondering.
I have a PR open, which adds a resource detector just for the service instance ID, and made it opt-in.
The spec's a little bit unclear, but it seems to imply that it should be populated by default, so… I guess I just wanted to see, like, what our thoughts are here, like… Basically, this is just recommended to be populated as, like, a UUID.
I guess the only concern with having it be on by default is that it can, like, introduce metric cardinality issues for people.
Potentially. So… Yeah, Aaron?
Aaron Abbott 00:29:35 Yeah, I think… I think, like, this is… I think this is really good, there was… so I guess, first of all, for cardinality, I don't think it would change the cardinality, right? Like, the… We're just adding a new label, but it's still… Not gonna change for the life of a single process, right?
Lukas 00:29:55 Right, yeah, I guess it would just… if you had some weird setup where you're, like, continuously creating new processes and, like, sending them to a collector, it could somehow, like, impact cardinality.
Aaron Abbott 00:30:06 Yeah. I guess the problem is if people are doing that today, and it causes all kinds of problems because it's semantically wrong, right? Like.
Lukas 00:30:14 Yeah.
Aaron Abbott 00:30:14 There's the single writer thing and all that.
So, yeah, I mean, I think at some point this wasn't in the spec, so maybe we were not sure on adding it.
Do you know if this is… this is stable in the semantic conventions?
Lukas 00:30:32 I believe it is, let me just.
Mike Goldsmith 00:30:35 Yeah, I think it is, that's why it was part of the declarative config requirements.
Aaron Abbott 00:30:40 Okay.
Lukas 00:30:40 Yeah, it's stable. I mean, this… I can drop a link in Zoom, but yeah, it is stable.
Aaron Abbott 00:30:48 Awesome.
I mean, I think this is great. Thank you for doing this.
my… I'll leave a comment on the PR, but my one concern was in implementation.
I think… if people… if people do this, right, and they make sure that they set up, for example, Unicorn correctly so that it, doesn't run this code until the worker starts. I think there's… an option in Unicorn, but it's… it can be kind of hard to set up in certain cases.
then it works fine, but for cases where people use, like, for example, subprocess in Python, with the fork.
worker mode, which I don't think it's the default anymore in newer versions of Python. Like, this will just inherit the service instance.id from the.
Lukas 00:31:32 Right.
Aaron Abbott 00:31:33 process anyway. So, I guess, I don't know if we want to… I think to fix that, we would have to update resource.
to do this, like, embed it directly in resource so that it either reads the current PID when people, Like, I don't know, does this cover that? Any thoughts?
Lukas 00:31:52 Well, we would have to have a way to, like, actually modify a resource if we wanted to support, like, a post-fork.
Type of a deal, right?
Aaron Abbott 00:32:03 Yeah, exactly.
Lukas 00:32:05 Yeah, I don't know what the best way to solve that is, I guess, like, the biggest question is… The other question I wanted to ask was, like, should this be its own resource detector, or should it be folded into the old cell resource detector?
Just adding the service.
Or, like, I guess what you're saying, Aaron, maybe this… Should be not even necessarily a resource detector, like, it could be kind of natively supported in the resource class to handle these edge cases.
Aaron Abbott 00:32:37 Yeah, that's… this might need, like, a special case, just because Python and forking is weird.
Mike Goldsmith 00:32:44 Yeah.
Aaron Abbott 00:32:45 But, I mean… If we want to go with a separate design.
I don't have, like, a super strong opinion, I don't know. Anybody else?
Mike Goldsmith 00:32:55 I'd be interested to see how this compares to what, we did in .clarityconfig, because this… that value does get… that attribute does get set, but it feels like a long time ago that I remember how it actually works.
Lukas 00:33:08 When I looked at it, it seems like we're just, manually passing it into the resource object within the Clip2Clar diff config, so we'd want to update that, probably, to just use this resource detector.
Mike Goldsmith 00:33:20 Okay.
Lukas 00:33:21 Yeah. So, yeah.
Mike Goldsmith 00:33:24 Maybe because this wasn't there, because I think the declarative config tried to use existing resource detectors.
So maybe because this one wasn't there, we did it slightly differently. Yeah.
Lukas 00:33:35 Yeah.
Mike Goldsmith 00:33:36 To consolidate onto one implementation.
Lukas 00:33:40 Yep.
Aaron Abbott 00:33:46 Cool. Lucas, do you think you can look into the… the forking requirements for Python on this, like, I can leave a comment, but…
Lukas 00:33:53 Yeah, yeah, yeah, go ahead and leave a comment. I'll, try to… see if I can come… to, like, a… a good solution, I guess. But are we… so, I guess… Yeah, the main question I just had, though, is do we want to have this be a separate resource detector?
Or should it be in… the hotel resource sector, it doesn't really matter, Assuming it stays as a resource detector, would we want it to be separate or not?
Mike Goldsmith 00:34:29 Yeah, I think there was something in the config spec.
that described where this should happen, what resource, etc. is about, I can't remember. I'll see if I can find the link for you, and then we can see how it describes it there.
Lukas 00:34:43 Okay.
Yeah, I'll just keep it as is for now, unless there's other concerns, and then I will look into the forking… behavior.
Mike Goldsmith 00:34:54 Okay.
Aaron Abbott 00:34:57 Oops.
Lukas 00:34:59 Yeah, I think that's… that's all for this, then. Thanks for the… the comments and feedback, everyone.
Mike Goldsmith 00:35:05 Yeah, thanks, Lucas.
Aaron Abbott 00:35:14 Yep.
I'm just writing a little bit in the issue.
Do you mind also linking, like, the Uvicorn? I think you mentioned there was, like, a Uvicorn discussion this came from, which makes sense, but just kind of doing the cross-linking, Lucas?
Lukas 00:35:29 It's in… there's link the Slack link? It's… it's in Slack.
Aaron Abbott 00:35:34 Oh, okay, okay.
Alright.
Cool. Alright, next one is also Lucas.
Lukas 00:36:04 Yeah, I just wanted to know, so… yeah, unfortunately, with the selected… seems like we never can get away with this.
There's just a minor bug.
Where this… It logs a warning, when we… called, when we use the behavior on, like, the selectable groups object with Python 3.10 and 3.11. So, the fix is pretty straightforward. I was just wondering… there seems to be a lot of noise around this, I don't know if we wanted to create a patch release for this, or…
Aaron Abbott 00:36:42 Do you have… do you have any idea how… I see this issue, but, like, not a lot of thumbs up or anything. Was there a lot of people asking out Slack?
Lukas 00:36:49 No, I'm just seeing, like, a lot of PR links. It looks like we broke a lot of, test suites for other… like, if you scroll on this issue… I see. You'll see, like, a lot of, repos.
That are impacted, so, yeah, I don't know.
Aaron Abbott 00:37:10 I see.
That's annoying.
Well, I mean, one thing is we're already, like, two weeks into the cycle, you know, people have already been dealing with this change, they've probably already baked it and all that, so maybe we should just put in the next minor version release, or… You know, we could do a minor version release maybe next week and do… not wait a full month.
like.
Lukas 00:37:40 Yeah.
That works.
Just wanted to make sure this is, Yeah, on people's radar. Yeah, the fix was just to, like, call the dict, method directly.
Aaron Abbott 00:37:55 That's… Annoying. Okay.
Man, this is so annoying. Everybody's like, why can't you just remove this thing? And it's like… it just will never behave the same across Python versions. It's kind of frustrating, but… Okay, thank you so much, Lucas. I'll, I'll probably just approve this one, and I think… Yeah, hopefully we can just do a… Put it in the next minor version, unless anybody thinks it's more urgent.
Alright, thank you all. Love the thumbs up.
Next one, we've got Mike.
Mike Goldsmith 00:38:37 Yeah, it was just something that I noticed. I know that we've recently, enabled merge queues, so I just wanted to check what the expectation was, because this has got 3… approvals, but from what I can see, it's 3 approvals from 3 approver-level roles. There's no maintainer interaction here, and I just wanted to check, is that still an expectation, or is it… The approvers can now effectively get something into the merge queue.
Aaron Abbott 00:39:05 That's a good question.
I wonder if anybody knows what happens across OTEL. I'm guessing it's always expected that a maintainer has to press the button, but…
Mike Goldsmith 00:39:16 That's my experience of it on, I think, most of the repos that I've seen. I've not seen it have approvers be able to actually get something merged.
Aaron Abbott 00:39:27 Yeah.
I think… this kind of is, like, the… this one's merged already now, obviously, but the ready for merge option here, I think we also kind of talked about it last week. It's like, if it has a bunch of maintainer approvals, how do maintainers or triagers know if it can be moved to… ready to merge, or if it needs… we have, I think, waiting for maintainer, right?
Mike Goldsmith 00:39:50 I think the ready-to-merge is the internal level one of, like, someone needs to click the button.
Aaron Abbott 00:39:55 Yeah, yeah, yeah, yeah.
I mean… I think, in most cases, if it has, like.
especially multiple approvals from approvers, I would like to be able to just click the button and not think too hard about it, so we could just.
Mike Goldsmith 00:40:09 stick it right.
Aaron Abbott 00:40:10 Right? Ready for merge. I think, and we talked about this last week, the only kind of counterexample is we don't use, like, an accepted tag or, like, ready for contribution tag on the issues in the first place, so… I think maybe there's some… Cases where it would be good to have, like, Obvious feedback from maintainers that Like, it's not blocked on them, however we choose to do that.
Mike Goldsmith 00:40:34 Yeah.
Aaron Abbott 00:40:35 Yeah.
Mike Goldsmith 00:40:36 Yeah, I think the reason that I brought it up with the SIG is just that I don't know what the expectation is around, like, when, like, is 2 approvals and it wouldn't have done it. I was like, 3 is the gate, I'm not sure, but just, it was different to what I expected to happen, and then seeing it happen. So I don't actually have a problem with this PR directly, because obviously I approved it, and I think it's a good change, but it was just the mechanism of how it got merged.
Yeah.
Aaron Abbott 00:40:59 Hopefully.
I don't know, Leighton, do you have any thoughts?
I think we talked about this one. I don't know if you were here for this one, Mike, it might have been when you were out, but, like, SEMCOM has this very, very clear process, which is probably way overkill for us, but it's… there's, like, a label that the SIG or the code owners or whatever are ready for the contribution.
That, hey, if the issue's approved, and the… like, issue has… sorry, the PR has the requisite number of approvals, and it's probably ready for merge.
Yeah.
Mike Goldsmith 00:41:35 Yeah, I know that Sencomp have got a two-approver minimum for it to go to be considered for merging, So, yeah, I'm… yeah, I don't know what the right answer is here, I just thought it'd be worth discussing.
That feels like… that feels like a very complicated process for what we want.
Aaron Abbott 00:41:54 Yeah, I agree, yeah.
Anybody have thoughts?
No. Okay, I have… I have my thought. I think Leighton probably had to drop. He mentioned he would leave halfway through.
like, maybe to make this more clear, Mike, just in the short term, would it make sense to add a new, Just having my sharing, sorry.
This one.
Would it make sense to add… Either, like, a label or a new category in the… in the board.
that, PRs would go to if they're waiting for an approver… sorry, waiting for a maintainer, but they're approved?
Mike Goldsmith 00:42:35 I think that the Ready for Merge column is that, so I don't think there's any automation that will put something in there. I think automation would move it to the approved PRs column.
So I… I think maybe renaming ready for merge to Waiting Maintainer might be a little bit more clear, but I…
Aaron Abbott 00:42:54 Okay.
Mike Goldsmith 00:42:54 Maybe.
Aaron Abbott 00:42:56 That sounds good to me, Nolan.
Liudmila Molkova 00:42:59 Yeah, we… for some comfort, don't really follow this, this complicated process. Well, if the processes are some, it's… a bit too complicated. I think this is the maintainer discretion. If you see the PR, that doesn't seem controversial, that you don't believe other maintainers would have an issue with, there are approvals has been out for a bit.
there is, in some confidence back, there is no controversy in just merging things if you have high trust and approvers doing a good job reviewing it.
Mike Goldsmith 00:43:36 I actually think that that's an interesting… point is that I think the roles that we've got in OpenTelemetry, I think sometimes they're implemented or actioned differently across different SIGs and different groups. So, like, the approvers are therefore looking at changes, PRs, or whatever it is, and approving them, and then maintainers are… It seemed to be the quality gate of getting something merged in some places, but in other places, it's the approvers do that work, and then the maintainers are responsible for doing project direction, and making sure the project's healthy, and making sure maintainers are doing the right things.
it's… I guess that that's just a difference that I've noticed between different groups.
Aaron Abbott 00:44:21 Yeah.
Oh, go ahead, Lumil, sorry.
Liudmila Molkova 00:44:24 No, go ahead.
Aaron Abbott 00:44:26 Yeah, I was gonna say, like.
speaking for myself, and I can chat with, like, Ricardo and Leighton offline or whatever, but the only time that I wouldn't merge something that has multiple approvers from, you know, from our approvers pool is if I… like you said, it's like project alignment, like, maybe, maybe I've seen something in the spec that That, like, you know, precludes this, or whatever, or, like… you know, like, mechanical stuff, like, oh, it's an API breaking change, maybe people didn't think about it. So, like, that's… that's pretty much the only thing I'm looking at when it has two approvals already. So we could… we could make that more clear for, like, you know, what's it called? Copilot instructions, stuff like that.
But I'm… I'm usually not looking at, like, the… quality, so… All that's to say, I'm fine with the thing that we discussed and Tammy said in Slack, or in the chat here, like, we could just move it to that column, and then I'll take, like, maintainers could take a quick look, and the expectation will be super clear.
Mike Goldsmith 00:45:28 Yeah, that sounds good. Thank you.
Aaron Abbott 00:45:33 Alright.
Awesome. Anyone… Any thoughts on that? He's like, no.
Oops, sorry, I gotta scroll up.
Okay, Lucas again.
Lukas 00:45:50 Yeah, sorry, last… last thing for me, just…
Aaron Abbott 00:45:53 Yeah, just a chuckle.
Lukas 00:45:54 a quick reminder on this, yeah, it's just, I think that Prometheus SIG just wanted to… get some of this out. It's pretty straightforward change, but yeah, I think this PR is just, the most important one, since I did end up doing some… refactoring of the Prometheus exporter a bit, so…
Aaron Abbott 00:46:19 Yeah.
Lukas 00:46:20 Yeah, no rush, just… just wanted to… Make sure there's eyes on this, but…
Aaron Abbott 00:46:27 No, no, thank you for raising it. This one's good.
I think… I don't know if I've seen all the other changes you've done, but, like, Could you describe me a little bit? Are we still using the Prometheus, client to generate the text format, for example?
Lukas 00:46:45 Yeah, yeah, we're still using Prometheus Client for everything.
Aaron Abbott 00:46:49 Okay.
Is that working okay? Any issues?
Lukas 00:46:53 Yeah, I was actually gonna try setting up our Docker tests to, like, properly test this.
Like, with a… a real… Like, the full integration?
Aaron Abbott 00:47:08 Right.
Lukas 00:47:09 We can… I can do that, like, if we're concerned about merging this, but it should just, Yeah, it's just really just rearranging code. I haven't really changed behavior that much, or really just asked… there's just some additional added behavior here.
Aaron Abbott 00:47:26 Okay.
Cool.
We do have some tests here, like this one. I don't know if it's feasible to do this, and that would be a little easier than the whole Docker thing, where you can just assert on the text format.
What do you think?
Lukas 00:47:39 Yeah, yeah, I can, I can, add some more tests, but I don't think… Like, the existing tests should cover… Everything pretty well.
But… Yeah, I can, I'll go through it again, make sure that there's… Proper test coverage.
Aaron Abbott 00:48:06 Okay, no, I'm sure it's fine. I just… I've worked on this before, so I was kind of curious, that's all.
Lukas 00:48:12 Yeah, sure.
Yeah, and there's, like, there's actually, 3 more PRs related to this, but, yeah, just… just wanted to… This one should be done first, since it has the refactor.
Aaron Abbott 00:48:26 Okay, awesome. I will probably take a look at this one. Thank you so much.
Alright. Oh, Gregory.
Gregory Loshkajian 00:48:35 Oh, no control.
Aaron Abbott 00:48:37 Iowa.
Gregory Loshkajian 00:48:38 Hi, it's very nice to meet you. I… So, I have this, request in about HTTPX2, Because it seems like, in the past, Few months or so.
The HTTPX has slowed down maintenance. It's been about a year or so since any real release has been done on that library, and the contributors are starting to lock up things like discussions and issues, which has led Pydantic to make a API-equivalent fork.
called HTTPX2.
So, I'm hoping that that's something we can maybe account for in some way. I would… I would be really open to contributing to this one, because it's something that, like.
I kind of need, but given that it is, like, a feature request, I wanted to come and introduce myself and ask, is that the sort of thing that's, like, reasonable scope for a new contributor? Like… I want to do this as, like, nice and polite as I can.
So…
Aaron Abbott 00:49:41 Well, yeah, awesome. Welcome, first of all. Thank you for joining, I think that's really appreciated. It makes it easier to make a decision here. Lucas, you wanna go ahead?
Lukas 00:49:51 I was just gonna chime in here. So, I… I recently added support for AI or BotoCore.
to our Bodecore library.
without actually creating a new instrumentation package. So, I don't know if you were, I don't know if you've outlined an approach yet, but…
Gregory Loshkajian 00:50:07 No, I appreciate you.
Lukas 00:50:07 Probably…
Gregory Loshkajian 00:50:08 And that's actually part of… I haven't, and that's part of the reason why I wanted to come here first, because I had an inkling that you guys might say something like that. So…
Lukas 00:50:17 Yeah.
Gregory Loshkajian 00:50:18 Before… before I even did anything, I wanted to, like.
So, yeah, this is very much a, like.
Can I work on this? Did you guys have any thoughts about, like, appropriate way of going about it? Because I was also thinking it might make sense to just Have the current one.
know about both, so… Like, that would be…
Lukas 00:50:36 be… yeah, I might be jumping the gun a bit, but yeah, that would be probably my preferred approach, is, like, we could update the HTTP library to be able to instrument both HTTPX and HTTPX2.
So, yeah, I see Aaron. Aaron has some more thoughts.
Aaron Abbott 00:50:56 Yes, I was gonna say, well, I don't think we have, like, Sam or, Marcel or anybody from Pydantic on the call today, but they do…
Gregory Loshkajian 00:51:05 my other questions.
Aaron Abbott 00:51:06 Yeah, they do pretty regularly contribute, and… they're also, you know, like, a kind of an observability vendor now, so… Yeah. What are the chances that they would, You know, accept the… Instrumentation either in that repo or directly in the code as, like, a native instrumentation.
Gregory Loshkajian 00:51:27 Yeah, that was gonna be my next question, like, is this something that we would appreciate checking in with their side before trying to figure out anything here?
Aaron Abbott 00:51:38 Yeah, I would say so. I don't know, you could either file an issue in that repo directly, or, Yeah, I'd probably start with that, just because, like, they're all, you know, pretty well connected with the hotel community, so I think they would consider it and have really good feedback on whether or not that's a good approach or not. Also, I know that they like Rust.
So I'm wondering how long we stayed as Python, so…
Gregory Loshkajian 00:52:06 Fair enough.
then I'll put in a task then, and let them know about this.
And… get… and get their thoughts on it. That seems completely reasonable, but… like… Yeah, thank you very much, and… crap. Yeah.
Aaron Abbott 00:52:26 Yeah. Thank you, Gregory, and thank you for not just sending, you know, like a… five-coded thing without coming and chatting first, I think this is… Always a good way.
Mike Goldsmith 00:52:37 Yeah, you don't want your introduction to be a $3,000.
Gregory Loshkajian 00:52:39 Yeah.
Mike Goldsmith 00:52:39 the new instrument.
Gregory Loshkajian 00:52:40 Yeah, exactly. My team's really invested in OTEL. We want to, like… we want to make a good impression, so… Okay. Cool. Then, I'll file that into HTTPX2 then, and we'll see where it goes from there.
Aaron Abbott 00:52:57 Yeah, that sounds great. Do you mind just jotting something in the meeting notes as well, under this topic, just to… just for bookkeeping?
Gregory Loshkajian 00:53:05 Sure.
Aaron Abbott 00:53:06 Cool.
All right, last topic then, unless anybody else had something on that one. Surya, your own?
Surya Teja 00:53:17 Yeah, hey, Aaron, I was just trying to close the loop on the Gen AI migration. So, as a part of the issue that Mike has put together, we just need to create a new release in PyPy for all the packages that are inside the Python country, and then put a note over there to come to this new repo. If that is done, I can work on the last step, which is removing these, packages from the country prepper.
Liudmila Molkova 00:53:55 I'm thinking we can remove the things that were not released ever.
just…
Surya Teja 00:54:00 Right.
Liudmila Molkova 00:54:01 away.
Surya Teja 00:54:02 Yeah.
I… oh, sorry, go ahead, let me lie.
Liudmila Molkova 00:54:06 Okay, go ahead.
Surya Teja 00:54:08 I played doing that, and Actually… I'm forgetting the name of the person.
Ricardo asked me to do it en masse instead of doing one by one. I tried doing it with Anthropic and Cloud Agents SDK.
Liudmila Molkova 00:54:29 Okay, Ricardo wants to do it all at once.
Surya Teja 00:54:32 Ugh.
Liudmila Molkova 00:54:33 We're… if we want… oh, so I think there are two… 3, 2 packages that… We… we… Well… that we have released and we need to deprecate. I think it's OpenAI and something else.
I like that.
Aaron Abbott 00:54:53 Me too.
Probably the vertex, the Vertex one.
Liudmila Molkova 00:55:00 We don't move… we didn't move the vertex, right? Because it's complicated.
Aaron Abbott 00:55:04 Yeah, sorry, we did release that one, though.
Liudmila Molkova 00:55:08 And we probably should not remove it in case we need to patch it, or do we also remove it?
Aaron Abbott 00:55:15 I mean, we have it in the old branches, so it's probably fine.
Liudmila Molkova 00:55:19 Okay. There is, like, two packages that have been moved to the new repo, and that will need some deprecation. It's OpenAI and something else, I'm blanking.
And for them, I think we first need to release the… The new version, well, ideally.
And then we can deprecate this.
Mike Goldsmith 00:55:44 Sorry.
Liudmila Molkova 00:55:45 Go ahead.
Mike Goldsmith 00:55:46 I was gonna agree, I think the… we should probably want… we would probably want to release the new packages so the, the deprecation notice points to the new package on PyPi, not just to the new repo, because I think that… I think it'd be better to link directly to the new package rather than a repo that may… that may not have released something yet.
Liudmila Molkova 00:56:08 Yeah, and then the next question, I think, Mike, you had a PR, and that we didn't merge yet.
To, that does the release magic, right?
Mike Goldsmith 00:56:19 Yes.
Liudmila Molkova 00:56:21 And I've made a change to rename all the packages and set the version to V1 for all of them.
Do we need to coordinate on your, PR… To account for this.
Mike Goldsmith 00:56:37 Maybe, I'm not sure. I will check what… Is yours the V1, is that being merged?
Liudmila Molkova 00:56:46 Yes.
Mike Goldsmith 00:56:48 Okay, I'll… I've not looked at that PR for a little while, I'll merge main into it and see what… what impact it has.
Liudmila Molkova 00:56:55 It has a tremendous impact. The first impact is that the package name have changed.
Mike Goldsmith 00:57:02 Okay.
Liudmila Molkova 00:57:03 Second is that, we don't really need per-package release, I think, to start with.
When we… like, the… probably the most important thing is to release it all.
Mike Goldsmith 00:57:16 Okay.
Okay, I will… I will, I'll take a look to see what, we want with that PR and see how it could be changed.
Liudmila Molkova 00:57:27 Awesome. And we can still do the… well, I don't want per-release to merge per release, and… sorry, merge… Sorry, release per package, and start releasing individual packages, because then we will have the version mismatch.
That's not needed, probably, in the long term.
So, I think the best course would be to just, yeah, figure out how to release it all together. Release it, and, Then, drop the things from the contribib.
Mike Goldsmith 00:58:02 I thought that we talked about wanting per package, because it doesn't always feel good that if, like, one package has not had any updates, and then it's gonna get, like, an empty Version?
Liudmila Molkova 00:58:16 there are pros and cons to both, right? So, if we do, per… we've done, we tried per package, and what happened is that we didn't release things for a long time.
And we actually have never… Released.
We have never had the need to release something very fast.
So far.
Mike Goldsmith 00:58:45 Okay.
Yeah, we can go back and have that conversation, and see what impact that releasing has there. Yeah, that's great, I can look at that.
Aaron Abbott 00:58:56 Thank you. We're just about out of time. I want to make sure, does this have everything that Surya, like, Surya, you clear how you can help? Like, Do we know what to do?
Surya Teja 00:59:06 Yes, so once, you guys have an idea of how to release, when it is released, I can go ahead and, open a PR for removing all the instrumentation from Contra.
Mike Goldsmith 00:59:21 Yep.
Aaron Abbott 00:59:22 Okay.
Liudmila Molkova 00:59:23 Oh, wait, wait, so before removing, we will need to… Release… The last version of this old libraries was updates to the… Docks, right, to point to the new place.
Surya Teja 00:59:40 Yeah, no.
Mike Goldsmith 00:59:40 Go on.
Surya Teja 00:59:42 That is done, Lytmila. I updated the docs with the READMEs of the packages with where they can find the new packages.
Liudmila Molkova 00:59:52 The repo.
Aaron Abbott 00:59:53 We'll put it on the pie, though.
Surya Teja 00:59:54 Yay.
Aaron Abbott 00:59:55 Yeah.
Liudmila Molkova 00:59:55 Yeah.
And we will need to release them.
I think we can…
Aaron Abbott 01:00:11 That's it.
Liudmila Molkova 01:00:13 Sorry.
And I think it makes it impossible to do it all at once.
Because we would remove things that were not released.
And we will need to update 2 packages.
And then release them, and then… It's at least… Three PRs.
Surya Teja 01:00:46 Okay, so if I understand this correctly, first.
remove Anthropic, Cloud Agent, SDK, and others that do not have a release.
And, then, release OpenAI V2 and the other one, which has an entry in PyPy. After the PyPy node is published, delete them. So, are these correct tasks?
Per your, thoughts, good enough.
Liudmila Molkova 01:01:15 So yeah, remove what we didn't release, and wait for the new stuff to be released on the PyPi.
Then come back to the, remaining packages in Contrape.
Update the docs to point to new PyPy packages, release them for the last time, and then remove them.
Surya Teja 01:01:36 Oh, okay.
Yeah, yeah, got it. Makes sense.
Liudmila Molkova 01:01:41 If you, like, want, me to help talk to Ricardo, happy to do so.
Surya Teja 01:01:47 Yeah, sure, I can take this on-site.
Liudmila Molkova 01:01:50 Yeah, thank you.
Aaron Abbott 01:01:51 Alright, yeah, let's take it to slide, maybe.
Thank y'all.
Liudmila Molkova 01:01:54 Yeah, thank you.
Surya Teja 01:01:54 Congrats.
Mike Goldsmith 01:01:55 Aye.
Aaron Abbott 01:01:56 next week.
