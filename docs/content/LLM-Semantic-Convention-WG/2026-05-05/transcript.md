SIG: LLM Semantic Convention WG
Date: 2026-05-05
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 03:55 Okay, I'm muted.
I was saying hello to GenAI people, and also some bots.
**Josh Bonczkowski** 04:13 Baloo.
**Wolfgang Therrien** 04:20 Good morning, or afternoon.
**Liudmila Molkova** 04:24 Yeah.
I forgot where you're based, Wolfgang?
**Wolfgang Therrien** 04:30 I am usually, on the East Coast, just north of Boston, but right now I am in Jackson, Mississippi, so I'm in Central Time.
**Liudmila Molkova** 04:38 Okay, so still, like, more deep. I am…
**Wolfgang Therrien** 04:41 Just barely, for another hour.
**Liudmila Molkova** 04:44 Yeah.
And Andre is anywhere in the world, I know.
**Endre Sara** 04:48 I'm in New York.
So it's just, just afternoon, by one minute.
**Liudmila Molkova** 04:53 Buck.
So, I am more in the rest of the world than in New York, at least I've never seen you in New York. I've always seen you in other places.
**Endre Sara** 05:03 Well, I live in New York, so this would be the… Normally.
But, we'll see each other in Minnesota?
Are you coming to Australia today?
**Liudmila Molkova** 05:24 Sorry? Can you hear me, Dan?
**Endre Sara** 05:26 Are you coming to Minneapolis?
**Liudmila Molkova** 05:28 No.
**Endre Sara** 05:29 Oh, alright, well, I'll miss you.
**Liudmila Molkova** 05:33 Thank you. I'll miss you too.
Okay, so our agenda is empty, but it will not be.
Let me… Talk to the bot.
For a sec… Okay, So, Trask, I'm going to do some triage. Would you mind adding topics on the, some conf split, and if you have a moment on Python repo to the agenda, thank you.
Cool. Let's start with the project board, and these are the… PRs that are open.
And… that are not in draft.
And we'll take a look at a few of them.
**Trask Stalnaker** 06:39 I don't think you're sharing yet.
**Liudmila Molkova** 06:41 Oh, sorry.
Thank you.
Okay, so this is the memory operations PR.
And there are some minor feedback. Does anybody know if Nakumar is interested in coming back to this work, or is he lost patience with us?
**Trask Stalnaker** 07:04 I'll check. I think he was out for a little bit, and then probably lost track.
But I may, I may help him to replatform it onto the new repo.
**Liudmila Molkova** 07:18 Right, yeah. So this would be the first candidate to actually… Hurry, hurry.
re… target.
So there is another PR for workflows. I think it needs the second approver.
Is Redeemer here?
Here, here. Thank you. I think you brought it up in the, in the Gen AI.
channel already.
**Ridhima Satam** 07:53 Yep.
**Liudmila Molkova** 07:56 Whoa.
Fantastic.
**Trask Stalnaker** 07:59 I think we will… we won't want to merge any more PRs to this repo, right?
**Ridhima Satam** 08:08 Yeah, I see your PR for the new report, right? So, do I have to open it against that when it's Ready? How are we going to go about this?
**Liudmila Molkova** 08:21 Yeah, that's a great question. It is ready.
Right?
**Trask Stalnaker** 08:27 Yeah, so, maybe you want to bring up the… the Next Steps link?
So basically the… the next step right now is to merge this PR into… the SimConv repo, which will remove all the GenAI from there. Basically, my take is that as soon as that is merged, then the new repo is live, and we… people can start sending PRs over there.
And once that's merged, then I will post to all the open PRs in the core repo, apologizing for the extra work, but asking people to, re-open their PRs in the new repo.
Which will require updating things to the Weaver V2, so it's not… trivial, but hopefully, hopefully AI can Migrate those without too much trouble.
**Liudmila Molkova** 09:44 And we have, oh, you didn't include the skills. I have the skill, we'll probably, We can leverage the skill, and I can help you migrate if you're stuck.
**Trask Stalnaker** 09:57 Sorry, I thought you had mentioned that you wanted to put that in Yeah. With the core repo.
**Liudmila Molkova** 10:03 Yeah, yeah.
Maybe River Packages report.
So then for this PR, we would… It probably doesn't make to get an approval right now.
the second one, but it can also, it's fine. Like, if somebody wants to take a look, I think substantially, it makes sense to review it anyway, that maybe you just need to re-approve later on in the new rebook.
And then… It doesn't make sense to merge it, though.
**Wolfgang Therrien** 10:47 Yeah, I don't think it makes sense to merge it into the old place. Mike, in the chat had an interesting comment, whether or not we should look at the existing open SEMCOM PRs and just post a comment there saying that, like, this new thing This new repo exists, and we have an expectation that they'll be reopened, or if we should handle them sort of, like, one-off.
Or if we just want to go through, like, the open PRs that are pointing in this area, and… Let folks know.
**Liudmila Molkova** 11:17 Yeah, I think this was the plan, right, Trask?
**Trask Stalnaker** 11:20 Yeah, that's, called out there on the then-posed to in-flight GenAI PRs.
But yeah, if somebody wants to go, go ahead, I think that… Yeah. Would be great.
**Wolfgang Therrien** 11:37 Okay, I'm happy to do some of that… that work today.
**Liudmila Molkova** 11:41 Oh, wow, thank you.
**Trask Stalnaker** 11:46 And Lyudmila, I don't know what you, Any thoughts on just pulling the trigger and merging the SEMConf PR?
Or should we let it sit there for a few hours?
**Liudmila Molkova** 12:02 What anybody in this group… Have one extra time to think about it.
Like, where do you actually go and… I have a thought of going and rejecting the PR for whatever reason. I would respect it, we will talk about it, it's not a problem, just curious if we need to give people more time.
**Aaron Abbott** 12:28 Wish pure?
**Liudmila Molkova** 12:30 the… I think the… this one, right?
**Trask Stalnaker** 12:34 Yeah This is, to me, the line in the sand.
As soon as we merge it, there's no going back.
**Liudmila Molkova** 12:49 Okay.
then I'll guess… well, there is going back, until we release stuff, and even after, but I think that I would rather merge it than list, like, we are doing this to move faster, right? Let's move faster.
**Wolfgang Therrien** 13:05 Let's move faster, let's do it.
**Liudmila Molkova** 13:10 Once I celebrated merging PR on a call, and I think it was Samayai, notaker at the time, told that I was sharing that I'm getting married or something.
Not that type of commitment.
**Trask Stalnaker** 13:26 And those AI note-taker bots, they've got to be so much better now, but oh man, when we were evaluating some, like.
9 months ago. It was, yeah, it was horrible.
**Liudmila Molkova** 13:38 Cool. So, we've merged that one.
Which means that we can go ahead and actually tell people to go to this new repo.
**Trask Stalnaker** 13:48 Yeah, Wolfgang, was that you that volunteered to do that?
**Wolfgang Therrien** 13:52 Yep, I… I'm happy to… to do it.
**Trask Stalnaker** 13:56 Fantastic.
**Wolfgang Therrien** 13:57 And happy to… Let's do that follow-up, yeah, it's exciting. Thanks. Let's do it.
**Liudmila Molkova** 14:04 Yeah, and… Then, do we have open Gen AI issues? I think we'll just move them. If we can't transfer them in bulk, that's awesome. I don't see a reason to not transfer something.
Like, we can always close it afterwards, instead of spending time on filtering it out right now.
**Trask Stalnaker** 14:25 Yep, I can do that while you're driving the meeting.
**Liudmila Molkova** 14:29 Oh, sweet, thank you.
Anything from the next steps we need to… more… talk about… Yeah, this one is a good one. We will need to figure out the release process for the… new repo and, work with Autel.io.
To publish it, but that's the problem for the first release. Yes or yeah?
**Surya Teja** 15:07 Yeah, for the issues, there were few that were raised in 2024 and, others. So, how do we, how should we target those issues? Should we only take the issues that were raised in 2026 and… transfer them to the new repo, or also take something that was raised in 2024 and put them in the new repo, because that would, again, create a backlog of stuff, and it would be confusing. So, any strategy over there for that one?
if we are, fine with taking everything, I'm fine with it too, but just asking because… This is the first thing that we're doing for the issues, right?
**Liudmila Molkova** 15:49 I'm thinking about backlog… yeah, go ahead.
**Trask Stalnaker** 15:51 Oh, no, please.
**Liudmila Molkova** 15:53 I'm thinking about backlog as uncommitted stuff, right? We… it doesn't signal anything that there is an issue, but if you're seeing that there are issues from 2024 that are irrelevant in 2026, leave a comment, and we'll just close them then. I'm pretty sure there are a lot of irrelevant issues.
**Surya Teja** 16:13 Yeah, sure. I can take a look at the issues and, bring up in the next SIG meeting to see what I feel are not needed, and we can take an action on closing them and transferring other issues that are relevant to us.
**Trask Stalnaker** 16:29 Yeah, what I think… what I think I'll do is just… Bulk transfer them all.
And then we can triage them in the new repo.
**Surya Teja** 16:38 Yeah.
Yeah, sure, short ask, whatever works for you.
**Alolita Sharma** 16:42 Yeah, I think that's the best thing to do, Rask. Agreed.
**Liudmila Molkova** 16:56 Awesome.
Cool. So, anything else on the new January book?
Shouldn't much… Move on to the next topic, which should probably be the Titan repo.
Sorry, you have your hand raised, do you still, linda, say something?
**Surya Teja** 17:37 Sorry, sorry, I… I'm extremely sorry.
**Liudmila Molkova** 17:41 Yeah, no, no worries, it happens to me all the time.
Okay, so I didn't prepare an item for this one, but… I've been playing around with Python repo and things, everybody who… helped me… Maybe… give me a sec, I'll steal, some text from… the Python SQL we had.
Sorry, I can't find it, it doesn't matter.
Anyway, so… the… I've been playing with the, new repo for Python.
We talked about it with amazing Python-Seek folks, and… We still have some, maybe, questions on how to version things, how to ship it all in one distro and whatnot, but essentially.
the… I don't believe there is any pushback. Maybe, Aaron, Mike, you'll keep me honest if I miss something important.
But… This is the scaffolding of the new repo.
important things. There are, OTLs here. This is the ported version of OpenTelemetry OTL GenAI from the current Python repo. It's tripped off any legacy, all the deprecated stuff.
is removed.
And there are instrumentations, it's empty here for now, but I have two PRs… Showing how it can be done.
So this is an example of porting something from height and contrib.
And this is essentially, AI-assisted, well, like, 80% AI-assisted work, using… the… the skill… I have somewhere… here.
Yes, yes, there is one skill for port from country, one skill from port from open entrance. I don't think we have a formal blessing from Arise to donate stuff, so this is for… Demo reasons here, but we can definitely move forward for the port from contrib.
So… The outcome of this reporting is this report, which compares well, the instrumentation and the report. It compares what we have in Autel Country, pin up and inference, and what we have as a result of the sport.
So there are some APIs that we don't instrument yet, and it looks bad, but… the open inference also does some generic stuff. We'll probably talk about it at some point.
But this is the stuff that's common everywhere, and we successfully ported it. It reports any gaps it found.
And… it's… the significant behavior changes. It's just for your information to… Help… You review the porting approach.
And it identifies any, problems with tests, and… Essentially, yeah, this is the reviewer helper.
I've got very successful with this part.
And also, this is the example of, like, I've tested this instrumentation, I've polished the skill, I have, like.
relatively high confidence that this is AI-assisted migration, that's the reasonable thing.
Same story with porting from Open Inference.
It also produces some reports with some notes, it's just the same migration report, but for the other story.
Then it was not as successful with porting, let's say, link chain. It still needs a lot of… tweaks specific to link chain, but still also something that's manageable within a few hours of burning tokens, and you trying things out, and writing some reasonable tests.
The cool part about this scaffolding, that it adds Weaver Life Check out of the box.
So there is this thing called conformance testing.
It… provides you all the helpers and, like, for Python perspective, the fixtures you need to work with Weaver.
And from each instrumentation, it demands, like, the porting skill demands that along with the instrumentation.
you bring this conformance test for every significant scenario. So, for example, there is one for inference, one for embeddings. For, like, blank chain, we'll probably have a few more variations, so it's interesting stuff.
and… This check is pretty… ex… Tensive.
So, let me find… So there are policies that run inside Weaver Life Check.
And, they… Have some means to understand which span, the… which convention the span should follow, and then it will like, for example, assert that the embeddings have all the corresponding attributes, or that inference has all the corresponding attributes. It also has means to test if attribute values, like input or output messages, follow the schema, and that they are You can also test that they're present when we enable the content. Yeah, Erin?
**Aaron Abbott** 24:29 Yeah, I was wondering, like, two things, like, how much of this do we get out of the box with the Weaver and the V2, YAML schema? And then the second thing was, I was wondering if this rego policy should live with the semantic conventions in the long term.
**Liudmila Molkova** 24:46 So we don't get span validation out of the box, unfortunately, because we need to actually change our TLP, or change general semantic conventions, too.
**Trask Stalnaker** 24:57 We don't have spam type.
**Aaron Abbott** 24:59 Yeah, yeah, yeah, yeah, yeah.
**Liudmila Molkova** 25:02 where should it leave? I think it should probably live in semantic conventions.
But, for the sake of moving fast.
I think it should leave whenever… wherever it's useful right now, and the moment we add it to the new language, we should probably move this to the… The fever… sorry.
Gen AI Symmetric Conventions repo.
**Aaron Abbott** 25:27 Okay.
Yeah, just trying to understand, like, from the move fast and iterate approach, like, how do we deal with the, you know, updating the rego. It'd be nice if it was along with the semantic dimension PRs, but yeah.
**Liudmila Molkova** 25:42 Yeah, I mean, we can, we can move it right away.
I think that nothing stops us right.
Well, my only worry is that I want to polish it a little bit with a few instrumentations.
So that we don't need to update to different repos.
But it can be done anyway.
Let me write the action item. Yeah, Leighton.
**lechen** 26:09 Did you mention that, we'll be getting rid of all of the legacy and deprecated functionality, especially in utils?
**Liudmila Molkova** 26:20 Yep.
**lechen** 26:21 Is there a reason why we're not supporting those anymore? We tried so hard to support them in the current repo.
**Liudmila Molkova** 26:30 Great question. So, I think we should, like, this brings us to the question what we should do with versioning.
the… And what we should do with existing instrumentations in Python Contrib.
Right, so I… my thinking was that we do this.
We release… Final version.
of sleep from pond trip.
And this affects lib.change package names.
Right? Like, I don't know if Vertex CEI needs to change package name, or Google Gen AI, this is for you guys to decide.
But if it's, let's say, OpenAI, it will change package name, and it's effectively a clean slate.
Let's say, up in the IV tube.
And as we are releasing it, we will update the PyPy docs, we will say that it's deprecated, go to this new package.
And then, people who install new library version, new library name.
are a de facto.
Subscribing themselves to a brand new instrumentation library.
And we don't need to… Keep the legacy for it.
But… If there is a strong case, let's bring it up, let's try to… Supported?
**Aaron Abbott** 28:32 Yeah, Leighton, I'm curious if you had… Like, a specific use case in mind.
I know… so, like, I can speak for Google, we have a bunch of stuff that uses the legacy format, and we're kind of slowly migrating over to supporting the new one.
I think most places do, but… it's okay, I think, when people upgrade.
They'll just take this breaking change.
**lechen** 28:58 Yeah, not a specific use case, it's just that, like, when I was… reviewing PRs the last week, it's like… There was excessive, kind of, Like, we tried really hard to make sure that we weren't making… breaking changes and stuff.
I'm totally fine with the… because this is being treated as a new package, but just wanted to ask, like.
What the plan was, so…
**Liudmila Molkova** 29:30 So… Yeah, go ahead, Shreya.
**Surya Teja** 29:37 So… we have a few couple of PR… I have a couple of PRs against responses and, messages API for… in Python country.
So, should I close those PRs, because, we are bringing in new instrumentations that are already covering those?
In the existing ones?
**Liudmila Molkova** 29:59 I think that we should review the PRs that are pretty close and merge them, and I will, sing the four quests, the ones in the contract.
I… I want to get back to the previous conversation of that compat from the new repo.
**Surya Teja** 30:20 Yeah. Also, we have a GenAI folder, Util folder, right?
which, we made a lot of changes. What should we be doing that with the new changes that are coming from the new packages? Like, should we align the… New ones to… mimic those functions, like telemetry handler and stuff that we wrote, in that util folder, or…
**Liudmila Molkova** 30:49 Yeah, it's here. Like, it's the same API, just the new flavor of it.
**Surya Teja** 30:54 Okay, okay. So, the skill is going to rewrite everything that is coming from Arise and others to mimic the Functions in this one, right?
**Liudmila Molkova** 31:02 Yeah, yeah, it will rewrite, if you're talking about open inference, it would rewrite open inference instrumentation to leverage GenAIO tools as you know them today, with just some maybe cuts for the legacy stuff.
**Surya Teja** 31:15 Okay, okay, cool. Thanks.
**Liudmila Molkova** 31:17 And for the Hotels Gen AI, I think we should keep versioning it accordingly, so it's just the same package, we don't need to rename it even.
**Surya Teja** 31:27 Yeah, and that's going to stay in country, right? Or…
**Liudmila Molkova** 31:30 No, I think we should move it to the new repo, because it's the foundation of everything that happens in the new repo, and any change, if we split it across repos, any change would be very, very painful.
**Surya Teja** 31:43 Yeah, yeah.
Shot, Cool. Thanks. I have a few other questions, but I'll take it offline and ping you on the chat, so, to see what I can do on this one.
But thanks a lot, Rutin.
**Liudmila Molkova** 31:55 Yeah, thank you.
Yeah, Layden, go ahead.
**lechen** 32:00 Yeah, so, I was thinking that maybe we should put, like, a, At least for other Python repo side, like, maybe, like, a hard stop on, like, new GenAI issues.
And then, already start kind of training people to, like, open stuff in… the fork.
That would be… that way, like, we can start the transition pre… easily. And for, at least for the open PRs, I've already marked a bunch of them, and then, like, some of them are already, like, ready pretty close. So I think we'll just have to take those case by case.
There's not really a systematic way to do it, but for the other ones, like, some people have kind of, like, left them.
And I'm sure we can just port them Or someone can open up a new PR, the new fork.
**Liudmila Molkova** 32:53 So, I'm thinking it all depends on us. This is currently, see, it's just my playground, right? It's not the real repo. We need to bootstrap this repo first.
And… Yup.
The way to, I think, to move forward would be to just transition the existing contrab instrumentations.
to the tripod, and once we have some formal agreement from Arise, we will pull the trigger, and we can bring the… Open interference instrumentations one by one.
**lechen** 33:29 Well, I'm just wondering, like, like, that's probably gonna happen quickly, but, we're still getting, like, new GenAI contributions every day.
In Python, like… How should the messaging be like while that process is happening?
**Liudmila Molkova** 33:47 I think until this repo is officially not a lurk, the messaging is keep working in GenIO tools.
Oh, sorry, keep working in Python contribute.
**lechen** 34:00 Okay.
Okay, yeah, that's fine.
**Alolita Sharma** 34:03 So I think, Lydmella, you should probably note that.
So that everybody knows about it, right, Cindy?
**Liudmila Molkova** 34:11 Yeah.
**Alolita Sharma** 34:11 Notes.
**lechen** 34:28 Yeah, we'll probably, like… there's not, like, that many, but we can handle issues in PRs, like, case by case. Some of them are, like, pretty quickly to push through, but I think we just want them to be in a state in which, like, people are okay with either porting them, or, like.
Not wanting to give up because, like, they know that like, if it's such a long PR, and it's caught in the middle of the transition, it's like, it's not gonna get included, you know?
**Liudmila Molkova** 34:57 So I'm thinking, if it's a new instrumentation, we probably should not take it. Probably should say to wait.
Alright.
**lechen** 35:08 Yeah, yeah.
**Liudmila Molkova** 35:11 Anybody has concerns with it.
**lechen** 35:20 I think some of the functionality is, like, large enough, like, for example, like, if you see, like, Nakamar released, like, released, like, 5, 6 PRs to upgrade line chain instrumentation.
And it's kind of like a… Like, there's… it's unlikely for us to get all of them in, or even one of them in, by the time maybe this is finished.
So things like that, that are, like, long-running and stuff. We don't have to have, like, a… overarching rules or anything, but I feel like it is definitely, like, case-by-case.
**Liudmila Molkova** 35:56 Yeah, and for its…
**lechen** 35:59 Oh, sorry, go ahead, yeah.
**Liudmila Molkova** 36:02 And since blank chain is probably a lot of work and far away, maybe if Nakumar can come and we can play together in the sandbox that I have, and… It will be… Another proving ground for… for… All the skills, and that we can move fast in this new world.
I think for some instrumentations, there is a remaining big question of I think this is link chain, maybe OpenAI agents. That approach the Open Inference uses for instrumentation is not something we really like, because it's the accumulating state.
And, like, some callbacks on non-start and end.
But I wanted to… Learn what people… think here, I would take the migration, And then we can… have some dedicated effort to switch to traditional monkey patching, if that's what we need, but I would rather Start with what industry already has, even though Callbacks, SA can never work.
properly.
**Trask Stalnaker** 37:14 just my two cents on the Python repo, I kind of hesitate to, stop existing work and existing repos until we're actually, you know, live.
Just because, you know, things can take longer than we want or expect them to.
So, I mean, I like, kind of, what I've heard makes sense to me as far as, you know, new instrumentations. Yeah, that makes sense to put a hold on, because… We're, potentially looking at bringing in, sort of batch other instrumentations, but for our existing work.
I would just continue it, because whenever we switch over, just the same as with the SEMCOM switch over. You know, we're all just gonna point our agents at the existing PR and the new repo, and tell it to port the PR to the new repo.
**Liudmila Molkova** 38:30 Awesome.
**Aaron Abbott** 38:31 We also have this doc that, you shared in the Python SIG with, like, some of the plans and open questions. Maybe we should, I don't know, are we still using that as kind of the design area for this?
**Liudmila Molkova** 38:44 I've tried to find it, do you have a link?
**Aaron Abbott** 38:47 Yeah, yeah, I do. Ready.
**Liudmila Molkova** 38:49 Thank you.
**Aaron Abbott** 38:51 Pretty busy with meeting notes, too.
**Liudmila Molkova** 38:53 Thank you.
Hi.
Any… I think we briefly… oh, right, yeah, so, I think the important part for the new repo… Who are the… Maintainers and approvers.
And, this is… I think Trask, you agreed to be our bed bootstrapping maintainer for the… because the… if you don't know, Trask does every GitHub admin working up in telemetry single-handedly, and he… he can be an enormously awesome resource to get to the best, like.
Practices in a tall world.
**Trask Stalnaker** 39:40 Yeah, yeah, I will… I'm happy to be a bootstrap maintainer, and… For a few months, and then… Tail off.
**Liudmila Molkova** 39:51 Yeah, I've, pulled some stats on who was active in, GenAI work in the last 6 months, and this was the list of people, the script gave me, if you're not in the FaceTime, I'm sorry, it has nothing to do with your, like, how fast you can become an approver, more like what, what the… involvement you've had so far in reviews. This is actually sorted by the review counts, And, I think since this is the… Our goal is to move fast.
I think we would want to adopt the practice trust you introduced for the Genie AI So I'm confident that we also have some scripts in OpenTelemetry to effectively, run, A script that checks who was active in the repo in terms of reviews and contributions and comments recently, and update the list accordingly.
So, I have an Excel table somewhere, I have a script somewhere, but I'm… it's just the stats.
So, and I didn't… I know, Keith, you… kindly accepted the role, appreciated. I didn't reach out to other people, so if you… Agree.
Tell me.
It's exciting.
**Keith Decker** 41:25 Happy to help.
**Liudmila Molkova** 41:27 Thank you.
Leighton, since you're here, I think you're… been active recently. Again, the, do you want to roll?
**lechen** 41:41 Sure.
Sounds fun.
**Liudmila Molkova** 41:43 Okay, and…
**Alolita Sharma** 41:45 You're giving work to Lytes already. Good work, good work.
**Liudmila Molkova** 41:53 So, since we're in the soccer spot already, Mike, would you be interested?
**Alolita Sharma** 41:58 A fine away.
**Liudmila Molkova** 42:04 Mike is keeping silent. Okay, I'll ping him later.
And I'll ping Dylan, I don't know, Aaron, do you know if he's interested still in Gen AI? Should I ping him there?
**Aaron Abbott** 42:15 Yeah, definitely, I think you should ping him. I can also reach out.
**Liudmila Molkova** 42:22 Yeah, it would be awesome if you were a child.
**Aaron Abbott** 42:25 Okay, will do.
**Liudmila Molkova** 42:28 Thank you.
I'm suggesting not to set up component ownership.
Because I don't think it's been helpful in the past.
And I think with Shaddal, Automated enough that we don't need component ownership, we should all be experts enough.
**Trask Stalnaker** 42:50 Yeah, especially with the… they're all so similar, or there's a lot of similarity across the GenAI instrumentations. It's not… I think it's less of a expertise issue that we have in some, like, collector-contrib.
**Liudmila Molkova** 43:10 Right.
And… I'm thinking what else is important to bring, you can… you're more than welcome to comment on the doc and, There are a lot of details. One important thing is what's in scope.
And it becomes interesting when we start talking about databases, and AI-focused databases.
So, if we look into, let's say.
Open inference, they don't have any, but if we ever come to start covering what open telemetry does, there are quite a few AI-specific databases there.
And if I go and look into the specific instrumented libraries, they… and the database behind it, like Quadrant, where… what is the other one? Chroma. It's just part of database description that they are for AI scenarios, and for those.
I… I think it would make sense.
Because it will be in the Gen AI.
Domain to have those instrumentations.
It's not an immediate problem for us, we're not going to bring anything right away.
I was just curious how people feel about having some of the AI.
Things related to databases in this repo.
**Alolita Sharma** 44:38 That makes sense, Danmila. I think, the more focus, you know, we have on different areas.
specific to Gen AI conventions, you know, the more easier it becomes to actually find All the conventions in one place.
**Liudmila Molkova** 45:00 Okay.
**Aaron Abbott** 45:01 It sounds good to me. Ludmil, I know that there was, like, at some point, this discussion about whether it should just be contributed to, like, db semantic conventions. I know in the spec call, we were just talking about federating other, like, subfields in SEMConv.
Do you feel like that's kind of orthogonal?
**Liudmila Molkova** 45:25 Yeah, I think that the… what we would expect from the DB instrumentations is that they just follow DB semantic conventions, plus they may have some additional Things specific to AI.
And the AI conventions… Could live in the… some Congenia repo. I don't think we should split database conventions from the core repo right away, like we discussed in the spec call, that there should be interest. Somebody should want it.
**Aaron Abbott** 46:03 Yeah, yeah.
I guess we should just be careful about, like, dependency cycles in the… between the repos, if we're, you know, generating some of the conventions into one repo or the other, and we talked about, obviously, the Uber package and stuff, so…
**Liudmila Molkova** 46:21 Yeah, and I think I have an example that may be helpful. So, we should never have something like this.
Because Postgres is a general-purpose database, it should live in the country bripple, the conventions, it should follow, it is in the… core DB conventions. But if it's the Chroma, or Quadrant, or whatever, AI database, or AI-driven search engine.
Then, we can decide on a case-by-case basis.
**Aaron Abbott** 46:51 Okay, yeah, sounds good.
**Liudmila Molkova** 46:53 Oh, another driving factor for me was, okay, open anometry.
has OpenTelemetry instrumentation chama. We cannot just use the same package name, this is package squatting problem again, we will need to come up with a new pattern, and since it's CI-specific, then… Okay, I think the rest of it is just mechanics.
And there is a package name pattern, and we need to preserve package names.
And, the other important thing, I think, here is that maybe we should have some gates on which instrumentations we can take in, and this should be based on the popularity of the library. Like, or if it's legacy, it turns out that some of the open inference instrumentations are for something deprecated.
Like, I think Google has some deprecated SDK, Microsoft had a couple, and we don't need to take these instrumentations in, probably, ever.
Whew.
So, take a look at the doc if you… if you're a Python… Expert, tool-link expert go for… this section… there is definitely a lot of gaps here. Yeah, Erin.
**Aaron Abbott** 48:28 Yeah, maybe one kind of final question here was regarding, like, the… I don't know if it's covered here, I don't think so, but the Utiligent AI. Do we… for people that are doing native instrumentation, so, like, for example, we have ADK doing it, do we want to provide, like, a stable instrumentation API for other people to consume?
From this repo, that they can, you know, depend on a major version.
So, for example, we keep talking about Google Gen AI, and I could go talk to that team and see if they're willing to do native instrumentation, but… Right now, that would stop them from using the… the… Genai utils, right?
Because they probably don't want to depend on this thing, so they would have, like, you know, a copy of constants, potentially they would have a bunch of stuff, so… I think that was part of the, like, roadmap, or the, you know, long-term plan was to have native instrumentation, so I was wondering if we want to have this API consumable in a stable way.
**Trask Stalnaker** 49:32 Just fro.
**Liudmila Molkova** 49:33 5 of us.
**Trask Stalnaker** 49:34 Just to give you some experience from the Java, instrumentation.
We have an instrumentation API.
And it did take us… A good while to stabilize it.
But even after… there hasn't been a lot of adoption of it, and I'm… almost… hesitant to push it. because the core API is… I don't know. It's one more moving piece that, it's hard to push on… The, native instrumentations to use it.
So, I could see Python getting there, especially given that it's a smaller, domain, the GenAI instrumenter, and… A lot of people are paying attention to this space.
But I… I… I would just be cautious to rush that aspect.
And if native instrumentations want a solution now, You know, it's fine to… Copy in some constants, and… Not get, you know, some of the sugar and… consistency that… I mean, you want the output consistency, but… Yeah, anyway, that's… Just our… been our experience.
**Liudmila Molkova** 51:18 if I'm still… was still wearing my Azure SDK had to, I would tell, hell no, we would never depend on it.
No, not because it's bad, but because it's an extra dependency that doesn't make sense.
**Trask Stalnaker** 51:32 And every extra dependency for a native instrumentation is a big deal.
**Aaron Abbott** 51:39 Okay. No, I mean, I agree to some degree, I think… It… it's a little at odds with… Like, maybe we should just update the plan with this, because we have, like, this hook mechanism that we're saying is really important for doing, like, you know, upload or evals or whatever, and it's going to be really difficult for any native instrumentations to be in that ecosystem if they don't take some kind of dependency.
**Liudmila Molkova** 52:02 Yeah, I wonder if we can solve this problem in some other way, like, through the, let's say, the declarative config where people register some component that Instrumentation is aware of, and the implementation is done.
spec… like, the duck typing, it looks the same for everybody, but even this will be hard to do. My company, Grafana Labs, has shipped the whole SDK to deal with this problem that the hook is… not, generic enough across different instrumentations. And let's say the identical AI cannot invoke it. But we need to find a solution for it, but maybe it's not… Through some thick dependency.
**Aaron Abbott** 52:47 Okay.
**Trask Stalnaker** 52:48 I was just remembering one of the… one of my hopes in the Java instrumentation space was that the Weaver code gen could be a path forward for us, I mean, part of, at least for the simple, like, shape of semantic conventions, providing, sort of, pieces there, because then it's a little bit… A, we could have more consistency across languages, and it's code-gen, and maybe easier to sell as, like, a really stable API, but that sounds like it probably doesn't address the… the upload kind of issues that… questions that you all are facing.
**Liudmila Molkova** 53:32 Yeah.
But yeah, you're right that with ViverCutGen, we can replace not everything, like, not the context management part, like, not the start-stop pattern, but the, low-level APIs of, like, how to, like, start Gen AI span.
or a start inference span, we can address, like, the big portion of it with code generation. Maybe even specific to… maybe even specific to GenAI, if we need to, and we can give the code generation scripts to native instrumentations, but Yahoo will still be the problem.
**Aaron Abbott** 54:12 You're talking about code gen for native instrumentations, though?
**Liudmila Molkova** 54:17 I mean, if we're giving them means to just generate it in their own package, and when they're in they can just run it themselves, not worry about syncing repos or, like, composing their own coding styles or everything, they just take the… Templates and comment line, they run it.
**Aaron Abbott** 54:38 Okay. Yeah, I think we can discuss, but I think it's pretty clear we should probably not push on native instrumentations right now.
It's fine.
**Liudmila Molkova** 54:52 I mean, we can find other means, but yeah, you're right, yeah.
Okay, we have 9 minutes left, I think we should talk about the next steps.
I'm… I think, Trusk, we probably should work together on bootstrapping this, but at first I want to get some review on the stuff from Python people, because the project structure, the… some… First impression from this repo.
Let's try to figure it… figure it out this week.
I'm pretty sure you would hate these two things being top-level, just my guess.
But anyway, so let's try to figure it out.
And, once we have confidence, maybe we can sync again at the Python SQ call, and if you folks are okay-ish with the structure, We'll work with Trust on getting this official hotel.
Huh?
**Aaron Abbott** 56:03 Sounds good.
**Liudmila Molkova** 56:05 Okay.
**lechen** 56:07 Nice having two SIGs to talk about this.
It's like a lot of face time, you know?
**Liudmila Molkova** 56:13 Yeah… I'm sorry for… for squatting the Python sig call, though.
**lechen** 56:20 It's okay, everyone loves Gen AI either, so it's fine.
**Liudmila Molkova** 56:24 laughs.
**lechen** 56:28 Yeah, maybe that's a stretch, but I don't know.
**Alolita Sharma** 56:32 There's more to Python than…
**lechen** 56:34 Right.
**Alolita Sharma** 56:35 Only Jenny I at this point.
**Trask Stalnaker** 56:42 Just back to… quickly to the native instrumentation topic, because I saw there's still some chat. The… I mean, the… I think we definitely, you know, we want… push on native instrumentation, but we've got all, I would say, not this month.
We have a lot on our plate this month.
**Aaron Abbott** 57:05 Yep.
Exactly.
**Liudmila Molkova** 57:11 Yeah, I think we have a tremendous amount of native instrumentations already.
And there…
**Trask Stalnaker** 57:17 There's not…
**Liudmila Molkova** 57:17 Despite it.
**Trask Stalnaker** 57:19 I'm excited, and the Gen AI space is the first place that we have seen like, a pickup of native instrumentation. We've… well, We've really struggled in the Java space to get native instrumentation.
And maybe we shot ourselves in the foot by having such a good Java agent, but… Yeah, in general, native instrumentation It's something we would lo- we'd love to see more of.
**Aaron Abbott** 57:50 Yeah, I think the CodeGen idea is pretty interesting, because, yeah, like, at least in… maybe in Node, it's not as important, where you can just install Whatever versions, like, of every transitive Like, dependency that needs a dependency can just copy it, so… In Python, it's just been a huge headache having, like, especially, like, diamond dependencies or any kind of weird conflicts that get created.
**Liudmila Molkova** 58:19 I can see Jamie's.
You're questioning whether it's okay in JavaScript, too.
Cool. So then, we have next steps. We know what to do with Python, we know what to do with semantic conventions. A lot of stuff is going on, people.
**Trask Stalnaker** 58:43 Hmm.
I'm exhausted.
Just hearing about it all.
**Liudmila Molkova** 58:51 Cool, Dan. Thank you all.
See you around!
**Aaron Abbott** 58:56 Right.
**lechen** 58:56 Thanks, everyone.
**Aaron Abbott** 58:57 Thank you.
**Alolita Sharma** 58:57 Thank you.
**Trask Stalnaker** 58:58 I…
**Alolita Sharma** 58:59 Bye, bye.
**Surya Teja** 59:02 Cheers.
