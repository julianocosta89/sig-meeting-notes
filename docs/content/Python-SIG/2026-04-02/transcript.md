SIG: Python SIG
Date: 2026-04-02
Duration: 1661 minutes
Zoom Recording URL: https://zoom.us/rec/share/XsmPtDrzOKJFNm6qtl_wBkdylOKNEG5J5syWw6Rl_uDT4qUme7FhfXOH6_KvBBxI.W6-_E2xfUmWixn2H
============================================================

## Zoom Recording Transcript

Riccardo Magliocchetti 00:00:37 Hello.
Tammy Baylis 00:00:43 Hi, Ricardo, hi everyone.
Paulo Vital 00:00:45 Hello.
Riccardo Magliocchetti 00:00:48 Right, Tammy.
Keith Decker 00:00:49 Hey, everyone.
Riccardo Magliocchetti 00:02:29 Welcome, everyone, to this week's PythonSeq call.
We are waiting a few more minutes for more people to join. In the meantime, please add yourself as an ane to the notes.
And also, if you want to discuss… if you have any topics you want to discuss, feel free to add it as well to the notes. And I'm sharing… They link to the notes in the chat.
Aaron Abbott 00:03:30 Hello?
Tammy Baylis 00:03:34 Erin.
Riccardo Magliocchetti 00:04:11 Okay, we're at 15, I think we can start.
So, why can we run, again?
To this week, a Python 6 core.
I think I'll start with urging a bit.
Tammy, do you want to… Gravo.
Tammy Baylis 00:04:31 Yeah, I'll do a quick narrative. Thanks for driving, Riccardo. In the no status column, we, we generally avoid the build depths, dependable PRs, but there's three… I think one… The MCP one needs a CLA sign. The other two are probably ready for review.
I wanted to use the 5 minutes today to talk about, the reviewed PRs that need fixes column.
If we go to the top of the queue, let's say… yeah, add warning for endpoint mismatch.
This one?
was closed a long time ago, but it's still in this column. And it wasn't closed because of our, stale bot, it was closed by the author.
So, It would be good… I'm not sure how it would happen. I think it'd be good to have, number one, a new workflow to find PRs that get closed like this, and on close, remove them from the ready-to-review column, or whatever.
And then we… the second part, we might need… either a cron job, like Super Mike's done before, or just someone to… Mike's here!
Yay!
Yeah, it'd be great if we could have workflows and a one-time job to… to fix those.
Mike Goldsmith 00:06:05 Yeah, sorry, just to add on this, yes, definitely, the board workflow supports things like this, of changing status, like, when a review has been made, it can move it to, like, a reviewed column. If it's close… if it's complete, merged, closed, whatever, it can move it to a done column. We can do automations like that, too.
Tammy Baylis 00:06:23 I don't want to volunteer you, so.
Mike Goldsmith 00:06:27 It's okay, I will take this on, because I like doing that stuff.
Tammy Baylis 00:06:30 Okay, if you like it, that's amazing, thank you.
Mike Goldsmith 00:06:34 Yeah.
Tammy Baylis 00:06:37 As for the rest of the board, yeah, I've just… I've just been trying to put things in columns, but yeah, anything else, Ricardo?
Riccardo Magliocchetti 00:06:51 Paying this, but… Yeah, like, I think I see that… A lot of us just, like, move the… new PRs when we gave them a first look, so I think it's working fine.
the process, so… yeah.
Niuanus… one's selfing.
have some issues there to discuss, some PRs there to discuss, so… We can go… Yazdankhah,
Mani 00:07:30 Yeah, sorry, it's the… approved PR that needs fixes.
new API to add or remove metric readers at runtime.
Yes, that one.
I had some contradictory feedback on this, so my original implementation was to log a warning and return normally, but Aaron asked me to make it an exception.
But Ricardo, you reviewed it and said you need to… or, like, we have a guarantee that we shouldn't raise exceptions at runtime?
So I'm not sure what the… Approach should be.
Aaron Abbott 00:08:12 Hey. Yazdankhah,
Mani 00:08:13 It's a bit further down. Yes.
Aaron Abbott 00:08:15 Hey, sorry, I, I don't think I saw your updates since… I'm a little fuzzy, I don't… I don't exactly remember. Yazdankhah,
Mani 00:08:23 So, when we add a… basically, when they try to add a metric reader that already exists, or they try to remove a metric reader that doesn't exist.
Originally, I had it as logging a warning and just returning.
But… I think you asked me to make it an exception because other parts are retouching the metric readers.
There was a precedence to raise an exception.
Aaron Abbott 00:08:50 I mean, I think… I think I would just defer to Ricardo here.
That's a good point. I don't remember exactly why I said that, but… I can… I think we could go with what Ricardo said. Let me dig through the. Yazdankhah,
Mani 00:09:04 Postgling recessions, yeah.
Aaron Abbott 00:09:06 Yeah, sorry about that. Yazdankhah,
Mani 00:09:08 No problem.
Yeah, that's it.
Riccardo Magliocchetti 00:09:18 Thanks.
Okay, we have one more minute for this strategy part.
Okay, and then we can go on.
We're on the next topic… Okay, I have a bunch of topics from me.
I started, most, more urgent ones. I'm… Seems like, for some reason, like, last week, after the last release was released, at the early… early of March?
We started to get some… Issues opened, but looked like, regression.
So, like… I started looking at them.
The first one was this one, which I think was not a regression, but it's like, Like, what… In 1.30, we changed the SDK to look at an attribute that has been added.
to the API of the same version, because the SDK has a dependency on the API of the same version.
So I think, this we were trying to re-implement, the auto-instrumentation.
And they were doing that wrongly, and so I just answered that.
Like, the proper way to handle that.
And closed the issue, and I haven't heard back, so I think it's fine.
The next one is more interesting.
And that is, like, one that I spent a bit… a bit of time on… Trying to understand, what was going on, because, like, we got 3 different issues reported in the same issues.
Where was the original one? That is, like, that we should mark more clearly the… changing behavior, because, like, when I matched the Tracy Configurator.
implementation, PR, I also, fixed an issue that was ported, during review of that PR.
What was that we were not doing the context propagation correctly, in case of the… The SDK was off.
And, yeah, I agree with the… the fact that I forgot to make it, like.
Very clear, but we fixed that as that.
as well.
But also, we got a bunch of more, issues. One with, the Lightstar web framework, I needed to add that… Limit on the… OpenTelemetry version, because, very tests were not running with 1.40.
And we get another issue, which was, like, some memory leaks are reported.
But, like… It was just an unint, and no proof of that.
And so, yeah, back to the Lightstar issue. Me and a friend took a look at that.
Like, first, I checked that… The code was working fine.
And then, it turns out that They show, is… well, this is not a PR for, for us, but the issues that… where we were calling the explicit bucket Instagram aggregation, on a counter.
And, Mrs. Bucket's, Instagram aggregation was assuming that the instrument at, An, underscore advisory, attribute.
And so it crashed.
But, like, the exception was, eaten by, I don't know… So, something else in the, in the pot.
And so this took a while to understand, and it was, like, quite an adventure.
And so… yeah.
So, like, the… My understanding of this, but… Despite the… They should report that 1.40 was not that bad.
Mike Goldsmith 00:14:12 So, based on the things you said there, so the… there was a change in behavior for the Tracer, which… I agree, could have probably been identified a little bit better in… in, breaking changes, nuts, or something like that, surfaced a little bit easier.
then the light star was an implementation issue because they were using a metric type with an incorrect inner value.
Is that right?
Riccardo Magliocchetti 00:14:41 Yeah, like, we… we got a PR for fixing, like, for entering the case in.
Mike Goldsmith 00:14:48 Yeah.
Riccardo Magliocchetti 00:14:49 On our side as well.
Mike Goldsmith 00:14:51 Okay.
Is that… is that to, like, surface? When there is a problem, it can tell you that you're using the wrong Meet the type, or something like that.
Riccardo Magliocchetti 00:15:03 Yeah, like, the PR we got just, make the… The degradation code, ignored the fact.
Mike Goldsmith 00:15:16 Okay.
Riccardo Magliocchetti 00:15:16 Try to… to do something to… And I guess this is… How it behaved before 1.40?
Mike Goldsmith 00:15:25 Okay, that makes sense.
Riccardo Magliocchetti 00:15:26 But, yeah, we can also, like, write a warning and just a donor at all.
Sure. I don't know.
Mike Goldsmith 00:15:32 Yeah. Yeah, it does not cause a crash or something, yeah, definitely. And then that last one was someone's observed higher memory consumption, but no evidence based on around that.
Riccardo Magliocchetti 00:15:44 Yep.
Mike Goldsmith 00:15:45 Okay.
Riccardo Magliocchetti 00:15:47 But speaking of memory consumption, we also got, More precise, issues reported, again, for 140.
And… again, this, was, like.
A strange behavior from the implementers, because they were calling, the Tracer provider getTracer API at every request they got.
And, at the time, we didn't cache the tracer.
And so, like, every time a new tracer got created, And in 1.40.
We started to, to implement the SDK metrics, and for doing that, when we get the tracer, we also, set up, some MyPers code. It is with stressor matrix class, but… web.
Maybe you can… I don't know if it's big enough. You can see here from the flame graph.
And so, but, like, later.
for an unrelated change, we started to have a cache, and so now, like, every time you call GetRacer, you got the same tracer, and so now… the new allocation, is done, so I think this, like, Fixed.
Mike Goldsmith 00:17:19 Okay.
Riccardo Magliocchetti 00:17:22 Yeah.
And I think, yeah, speaking of this, issue, we have this same behavior of Like, when, A user call, the… Getracer, GetMeter, and I think also GetLog, API… for the proxy in the nope, Tracer provider.
We have this, unbound, behavior where, like, We allocate stuff every time.
And so I was wondering if we should care about this case?
Or we should probably introduce a cache that, for the same instrumentation scope, you get the same tracer, logger, and meter.
And avoid, like, strange users of the API to… to… to get into membership issues. Like, I don't think visa allocate much.
But still, like… You know.
Mike Goldsmith 00:18:36 Yeah, we're doing constantly repetitive calls, so it will eventually add up.
Riccardo Magliocchetti 00:18:40 Yep.
Aaron Abbott 00:18:41 Yeah. Ricardo, are you saying that it… you don't want the garbage collector to churn by caching, or are you saying that there's a memory leak?
Riccardo Magliocchetti 00:18:58 I don't have a strong opinion, but, like.
Like, in this example… in this tracer case.
We got a memory leak reported, and I'm not sure it's a memory leak.
Because, like, we don't know if the garbage collector will… like, we'll, I'd eventually, like, cleaned it up.
The staff are located.
But… Yeah, like…
Mike Goldsmith 00:19:34 Yeah, I think that's something we can definitely check to see, that if you are doing repetitive calls to get Tracer, do the old Tracer instances do get garbage collected? That's an unfortunate thing that someone's doing that, but it's then not breaking, it's just unfortunate. If there is… if they're not getting garbage collected for some reason, like, something's holding onto a ref somewhere, then, yeah, that would be bad, because then that would be unbounded.
Aaron Abbott 00:20:02 Yeah, and I think… to be fair, I think the spec is, like, I think it says something like, implementers may… do this or that, it basically doesn't say that it's expected that you have to hold a reference to it and not call it repeatedly, if I remember.
Mike Goldsmith 00:20:17 I think you're right, and I think the, the get tracer spec also says it should return the same instance where possible, I don't think it's a must.
Aaron Abbott 00:20:28 Okay.
Riccardo Magliocchetti 00:20:29 Yeah, like, I also asked on… Delta specification channel.
And I got an answer from Jack Berg that says that the spec is, the SDK spec is, Ambiguous on purpose, so you can implement whatever you… You won't?
But, yeah, like, on the other side.
The problem with that is that we can have a discussion on solving, and that… and we cannot say.
The spec says that, so…
Mike Goldsmith 00:21:03 bet.
Riccardo Magliocchetti 00:21:04 Yeah.
this was it for me.
For the first topic?
And I have to say, like, I was a bit worried, because… like… Having, you know, getting the… Four issues at the same time.
And also, weeks later is kind of worrying, but yeah.
In the end, it was fine.
Okay, next topic, also for me, we had, like, som… We had, like, a VSPR fixing some typing issues in the HTTP exporter.
And… yeah, like, probably, like, we're… we are… Slowly, and doing a tech checking for all the core stuff.
But I think we forgot about the exporter.
And so, doing that for the OTLP HTTP1 was… quite… fast, and I opened a PR doing that.
fix, like, running a type check, over the OTTP common package.
It's a bit more complicated, because there are a lot more, warnings.
So… If anyone wants to get involved with that, you're welcome.
And also, I started to clean up the metric's internal, types.
like, when reviewing all the PRs, I've seen that we had a typo in the, like, the PR adding the… some rough checks, so roughlynt, Checks.
I noticed we… we got some… Typos in some, type names.
As I started fixing that, and also started… let me show… Splitting the… the… Exclusion in the… in the pipe project, so files, so at least we get… Like, a little part of the… of the internal metrics code, Checked, and again, if you have any… anytime to work on this stuff, you're welcome to help. Some of this, like, I think the, like, the point and, exemplar server model. I have just one warning.
And… so, yeah, some others, part, many more, but it should be, like, Doable to do that separately.
At your own pace.
So yeah. Yeah.
Mike Goldsmith 00:24:19 Brad, no problem.
Riccardo Magliocchetti 00:24:19 Please go ahead.
Mike Goldsmith 00:24:21 I was just typing it out, and I was gonna ask, do we have issues tracking those? Is we've got a, like, a track… so we know which things to do that we know we want to address before we can check it off? If not, we should… it'd be good to have.
Riccardo Magliocchetti 00:24:34 I don't remember if… let me check if we have an issue.
I think, like, we discussed that some times ago, but I don't remember if you… Looks like we don't have any tracking issues for it, or… Oh, maybe it's this one?
But, like, we don't have a checklist out there.
Yeah. All the stuff that we can… But yeah, maybe, like, I can update, yeah. The issue…
Mike Goldsmith 00:25:27 16 OH, okay.
Yeah, I'll, I'm happy to take that. I can… I'll update the issue and just say that… what we want to do with it, and reference that, what you've just pointed to.
Riccardo Magliocchetti 00:25:38 Okay.
We can do that. Thanks.
Aaron Abbott 00:25:48 So Ricardo, is this just, like, a call for contributions, mostly, or…
Riccardo Magliocchetti 00:25:56 Yeah… Yeah, what's the worst of that.
Aaron Abbott 00:25:59 Okay, okay, cool. Yeah, I mean, I think… If we can opt-in individual files, which we've kind of done in the past, That would be great, too.
instead of, like, waiting for everything, I don't know if we're already doing that.
Riccardo Magliocchetti 00:26:20 Yeah, like, the API opener was, like.
To make it explicit what, was missing, too.
Aaron Abbott 00:26:29 Okay.
Riccardo Magliocchetti 00:26:29 to fix. Stop.
Aaron Abbott 00:26:31 Cool. And then, I did look into, like, this, baseline file, which is in… the based Pyrite package is not part of Pyrite itself.
Unfortunately, but basically you can generate, yeah.
Yeah, baseline, maybe? If you search for baseline. It might have been in Contrib, too, because that one… Was, had more unchecked code.
Yeah.
Yeah, that one.
So I… I don't have, like, a super strong opinion on… like, I think Base Pyrite behaves a bit differently, so it's a little annoying if we just want this single feature, that we would have to switch… switch over to that one, but… Effectively, we could just turn on type checking everywhere, and in theory, it would only catch new errors.
And, like, the existing ones go in this baseline file, but the file is really large. I think it was, like, several megabytes.
For this repo, which is pretty annoying, too.
So I… I'm kind of… I'm kind of on the fence with this.
Yeah.
-Oh, might oom your browser, but… We'll see.
Yeah.
I think… I think I've also seen, like, some people try to hack this into normal pyrite by doing, like, a… they, like, generate a file, and then they just, like, use grep filters or something like that. It's a little hacky, but… Yeah, if we can fix the actual issues, then… That would be my preference, I suppose.
Just wanted to call that one out.
Riccardo Magliocchetti 00:29:01 Yeah. Next topic is… Are we fine on… trying to do this, all-screen, action, but is, like, to simplify our, required checks.
Configured for the repository.
I think I immediately also opened one for contribute. I've seen it on the… the first column on the board before.
Emídio 00:29:29 Yeah, Joe.
Riccardo Magliocchetti 00:29:30 Send it.
Emídio 00:29:30 be.
Riccardo Magliocchetti 00:29:33 Yorian, okay.
Emídio 00:29:35 Yep, so…
Riccardo Magliocchetti 00:29:35 Do you want to introduce the PR?
Emídio 00:29:39 Yeah, sure. I think we discussed it, there's offline, it was LAC.
Like previously, we discussed about the automation of Doing the checks, because it requires you to define which jobs you want to… to, require?
But by using reusable workflows, we are able to, like, just pass. We need, Lint, we need MISC, we need, test workflows to be run. If you open the files change, you can see.
Yeah.
If you scroll down a bit, this file… yeah.
So basically, we are running everything from a single ci.eml file now.
And here, we define which one we can.
We need to be succeeded, or failed.
Aaron Abbott 00:30:41 Oh yeah, interesting. Is there any, like, downside to this? It makes sense to me, though.
Emídio 00:30:46 Yeah, I put a note on the… on the comments of the PR, like, on the description of the PR.
The only downside I can see is the CI takes a bit more longer to restart, like, 5 to 10 seconds.
Because of the reusable workflow.
And, the check job only runs after everything is finished.
Aaron Abbott 00:31:15 Okay, I didn't get the second point. What was the… like, that's kind of expected, right? It would just…
Emídio 00:31:20 Yeah, yeah, yeah, just… just, pointing out, because if you, like, search during the… our jobs are running, you can't find the last check.
Aaron Abbott 00:31:32 Oh, okay, I see, I see.
Emídio 00:31:33 Nope.
And there is also not, On the naming of the jobs, if you want to skip.
The third point, like, you can just skip by the… by their name, like MISC, Olint, or Tess, instead of the absolute naming.
Aaron Abbott 00:31:58 Okay.
Emídio 00:31:59 Yeah. And also, I got rid of, the bunch of underscore 0123 test files.
Aaron Abbott 00:32:08 Yeah.
Emídio 00:32:08 No, it's just one, only one.
Aaron Abbott 00:32:13 Cool. I mean, I'm good with this, and I think if it's not working, we could always, you know, just revert this PR. I think we should give it a try, because… I haven't been able to use the auto-merge button. That's, like, the main thing, so…
Emídio 00:32:27 Yeah.
Aaron Abbott 00:32:28 If I forget to come back and click merge, I just have been avoiding it, because otherwise it's been submitting things before all the checks were finished.
Emídio 00:32:36 Nope.
So the idea is to first merge the one contrib.
And update the required checks on the enemy repo, and after that, update the PR on core.
And that's it.
It requires, like, a… quick sync.
Riccardo Magliocchetti 00:32:57 By the way, like, the… The idea is to just add, like, this one as a required check in admin, right?
Emídio 00:33:06 Yep.
Riccardo Magliocchetti 00:33:09 Yeah, but for doing that… So, like, so first we had to update admin, and then we can merge this one.
Correct, and then I can unblock everything, okay.
Emídio 00:33:20 Yeah, yeah, we need to touch that me first.
Aaron Abbott 00:33:23 Yep.
Riccardo Magliocchetti 00:33:23 Okay.
Aaron Abbott 00:33:24 Yeah, I can… Ricardo, we can work together on that. I can, you know, approve the admin PR, and we can get it in.
Riccardo Magliocchetti 00:33:31 Okay, yeah, like, maybe tomorrow, because if… For me, today is too late for doing that kind of work.
Aaron Abbott 00:33:38 Yeah, no problem.
Riccardo Magliocchetti 00:33:39 Yeah.
Emídio 00:33:43 Awesome, thank you.
Riccardo Magliocchetti 00:33:44 Okay, thank you, I meet you.
Aaron Abbott 00:33:46 Yeah, thank you for working on this, this is great.
Riccardo Magliocchetti 00:33:55 Okay, okay, last one for me, I swear.
And… yeah, we have VPR around.
That is… We're, like, to… this is, like, we got, like, an issues report, like, okay, this PR, with some very nice… numbers.
memory benchmark.
And the, the, the… the fact is that it looks like that our Python processes, I have a lot of memory, Allocated for using, by the context, because, when we export logs.
We have a reference in the log records to the context.
So… after a bit of iteration… And discussion?
We ended up with this solution to drop to, like, clear, the context, before, in the, I think this is, the spam processors, the log processors.
Before sending, the readable rug record to the exporters.
And so, since, yeah, like, this is a breaking change, I think if you have an export, But rely on that field.
I was wondering if maybe we can introduce an variable that, by default, keeps the current, behavior, but, like, if you want to drop the context, it's… you know, you just have to set the environment variable, and you're fine.
Because, again, like, The numbers are very interesting, talking about, like, 1 meg versus… More than 150 megs, so… Quite a bit.
Aaron Abbott 00:36:18 Yeah, assuming 50.
50K of baggage and 2,000 logs, yeah, makes sense.
So, if you go back to the code.
So, a question I had was, like, the… Context? Would we just want to deprecate it on the, I guess what I was expecting was for the readable log record, which is the thing that the exporters see, like, that would just no longer be able to see the context.
Riccardo Magliocchetti 00:36:54 Yeah, the problem is that, like, the… the field in the… In the log record, it's not optional.
Aaron Abbott 00:37:03 Yep.
Riccardo Magliocchetti 00:37:03 So, like, yeah, we are clearing and adding, like, an empty context.
Aaron Abbott 00:37:13 So the readable log record embeds the… Writable log record.
Riccardo Magliocchetti 00:37:21 Yes.
Aaron Abbott 00:37:23 Okay.
Yeah, that's unfortunate.
Okay, I could take a look, but I'm kind of inclined to say we should, like, you know, the logs SDK is still not stable. I feel like hopefully this is a pretty… Subtle change that wouldn't affect people, the… and we also talked about the context being available to, like, the processors, right?
Riccardo Magliocchetti 00:38:05 Yeah, like, this code is, before, I don't remember where it was placed, but now it's… it has been moved to… both to the simple Allure processor and to the… Batch, log record process.
And I think, like, this will be, like, the last, processor on your pipeline, so it should be fine.
Dylan Russell 00:38:44 Sorry about that. Didn't we just add the context?
To the log record, and like… Like, log a warning if… Context wasn't passed to log record or something like that?
Riccardo Magliocchetti 00:39:05 And I think that was…
Dylan Russell 00:39:07 Can you hear me?
Riccardo Magliocchetti 00:39:09 Yeah, I think there was, like, a yes in the API, because… we had, like, a version of the API that was taking the tracerD, the span ID, And something else, separately, and not, context.
Yeah, but, let me go to the…
lechen 00:39:34 This is different, because we're just removing it.
In the processors instead of the log record itself, right?
Dylan Russell 00:39:52 Okay. I didn't look at it super closely. Sorry.
Riccardo Magliocchetti 00:40:05 Well, maybe, like, we can discuss that, offline in the…
lechen 00:40:10 Yeah.
Riccardo Magliocchetti 00:40:11 the PR.
Okay.
Next topic is from Xuning.
Amending matrix PR.
Shuning Chen 00:40:24 Yeah, so based on the… a basic embedding span PR. After that converged, I added following metrics for embedding. So… Looking forward to, seeing more comments.
Riccardo Magliocchetti 00:40:52 Alright, thanks.
Shuning Chen 00:40:55 Thank you.
Riccardo Magliocchetti 00:40:58 Next one is from Ayrton.
Erdenesaikhan Tserendavga 00:41:03 Hi, Ricardo.
Yeah, this is an indication type UTSPR, based on the existing semantic conversions.
Please take a look.
And if needed, I can, make some changes related to the, tour open.
the amount of connection changes related to the splitting… splitting the, enrich agent P… enrolled agent type into the… Two different types, and also including the serial type from the Norwegian.
Right now, it's just on the… Existing type of the network agent.
Which can separate by a span kind.
Liudmila Molkova 00:41:48 Yeah, thanks, thanks for adding this, and yeah, I just left a couple of comments that you're probably ranking to those.
I… like, the PR follows current semantic conventions, it's just we are in the process of changing them.
And maybe we're… can expedite merging the open PRs so that we don't need to do some things. So, for example, we have this PR for enzymatic conventions to split and it, like, effectively remove some of the Attributes from the agent and vacation span that are never applicable.
So… Can I ask some Gen AI approvers, Like, Aaron, can you approve this pleat PR so we can just merge it and help, this one?
Aaron Abbott 00:42:46 Sure.
Liudmila Molkova 00:42:51 Awesome, and the other one is the two definitions.
Aaron Abbott 00:42:53 Meanwhile, could we… Is it linked in here already? I'm sorry.
Liudmila Molkova 00:43:00 It's linked.
Aaron Abbott 00:43:01 Coming from there.
Liudmila Molkova 00:43:02 comments, but yeah, let me, I'll give you a link.
Hmm.
Cold.
I've been going to the… I think this, this is trivial. I think there was some contentions contention point, but… Trask, reverted it, so I think this is very uncontroversial now. We can follow up on the contentions point separately. It just removes response ID and response model, and adds the agent version.
Aaron Abbott 00:43:44 Okay, yeah, yeah, I think that makes sense.
Liudmila Molkova 00:43:48 The other one is… tool definitions, and this PR uses two definitions, but uses them untyped.
Let me find the… tool definitions. It's currently blocked on Mingkoi not addressing some of the trivial parts.
So… Maybe… What I can do, I can just push the… push the… commit addressing the feedback to Ming, who is PR, and maybe… I can ask… Again, you, Aaron, to help merge it, because I think you have the context, and it should be easy to give it another review. Or maybe Dylan can take a look, because you also had a conversation there.
Aaron Abbott 00:44:40 Alright, that sounds good.
Liudmila Molkova 00:44:45 So let me do the update with the missing parts on the tool definition PR today, and I think it's pretty close, I think you are, but we can probably keep reviewing this change, and maybe we can unblock it as soon as possible in the next few days.
Aaron Abbott 00:45:04 Sounds good.
Erdenesaikhan Tserendavga 00:45:05 Thank you.
Riccardo Magliocchetti 00:45:15 Okay, next topic is from Yuriyud Mila.
Gen AI says right to repo, proposal, pros and cons.
Liudmila Molkova 00:45:24 Yeah, so we've had this discussion on the… during KubeCon and also in the GenAI call on Tuesday.
And so this is the proposal. I want to bring it up here, and we… I think we should talk through different options.
Because also Mike has some thoughts, and I would appreciate, if others share them. So, what happens today? Correct me if I'm wrong, I'm, like, I… it's, it's my impression.
that we have a lot of Gen AI PRs coming to the country repo, and we have a slightly separate group of people working on the Gen AI only, and working on everything.
We have some, like, new approvers, and people are looking into JAIPRs, at least they hope we do.
at least some reasonable job there. But, we are effectively taking resources away from Python Contrip, but also we are constrained on maintainers.
if we want to bring some new players, like, I don't know, I would hope some people from TraceLoop, or Rice, or OpenLite, or you name it, show up here, and tell, okay, we actually want to play in your Python country, rather than in our own repos.
I want to find a way for us to bring them in, but don't give them control over things that are not Gen AI.
Alright, so, like… And maybe in some… in some version of the future world, we can have a place where Arise and, Open Elementary and all those other people have approver powers.
Maybe even maintainer powers, but we have checks and balances, and this approver or maintainer power is used as a way for people to have control over what happens.
So this is, my incentive. Then, we would have different stability expectations, right? For the Gen AI, it's been part of the discussions that we want to move Sometimes faster, like, or, diff… we would have a different cadence of changes.
So, for example, in Java, they release their Java agent stable version, the distro, essentially, every couple years, the new major version. For the Gen AI, if the problem would apply to them, we would pick a different cadence of major version, maybe every 6 months.
What does it mean in practice? It's hard to say, because we have… I think we still should have one distro.
At least for semantic conventions, we would have a different… Cadence.
But… having a separate repo could solve some of these problems. It would not solve all of them, and it probably would introduce some new problems, like the fragmentation, or the, The question of the distro, like, how do we release, how do we, sync, keep things in sync, what to do with common dependencies, like instrumentation package.
So I think, Mike, you have some thoughts. Can you, can you elaborate on the cons? I think you, you have some cons.
Mike Goldsmith 00:48:39 Yeah, that's fine, thank you.
So yeah, my initial understanding was more around, I think, it would be fragmenting what we're wanting to do with Python. Like, we see Python as one of the core SDKs that's used a lot within GNI, and I think separating what the SDK is trying to do with the other contribrib modules from the semantic conventions and from those instrumentation libraries is only going to fragment, like, our understanding of how those things move, how they interact.
I would much rather see investment in trying to get us with more momentum within those two, like, those two groups. I definitely feel empathy for the people that are working on the Gen AI instrumentation PRs, that they do need help, that they do need more momentum, and that we want to go faster.
So yeah, I would… I'd rather see us try to add more capacity rather than move that capacity from somewhere else. But I… also, the… trying to bring… entice other people to come and contribute as well. I think that is a real consideration. We want more people to come and contribute, but maybe we don't want to give everybody everything, so I don't know how we would organise that.
Liudmila Molkova 00:49:54 And we could find means to organize this in a way like we do in semantic conventions. For example, we have an approver group and code owners, and then people would have the specific status for… for a specific component. This… this is technically possible. I'm also curious what our, like.
Other people think of… Father maintainers.
Riccardo Magliocchetti 00:50:27 I have mixed feelings.
like, I can understand the… I will say the frustration in not being able to move as fast as you want.
But… yeah, like, on the other hand, like, I see this as a failure for us as… Python… like, on the Python side.
Liudmila Molkova 00:50:57 Don't say this, no!
Riccardo Magliocchetti 00:50:59 Like, like losing an opportunity?
But, yeah, like… Yeah, like… as far as I can see, like, as a… Like, whatever works for you.
We, we, we, we can… work with that, like, as a pay-to-maintainer, like, I don't want to impose anything, like… like, if the GenAI SIG prefer to… Work outside.
by far, like…
Liudmila Molkova 00:51:40 It's not the preference to work aside, actually, don't treat it this way. I think it's just that the model we operate in OpenTelemetry and Gen AI World are… hard to combine. I don't… I'm not pushing for separation. I think this is a tool we can use.
Like, this tool can exist in different ways, if we can, like, find good ways to work together. We can have a report for conventions.
And all those checks and balances could be done there, and we can have code owners inside the Python.
it's… it's not… at least from my side, it's not like, okay, we cannot operate inside the Python country. It's more of how can we not… block each other, right? Because I feel like the energy that exists in GenAI is distracting some good efforts, like other folks, from some good efforts that happen in Contrape.
And I just want to talk it through and learn more about your… your thoughts and find a way that that would be great. Don't treat it as if, like, any, any, any, any… bad feedback to the Python.
Crew.
Riccardo Magliocchetti 00:52:58 Like, I don't know, like… like, from my experience, like, I… I feel that… We are missing, more people.
We've merge rights.
for… for the JNA APRs, because, like, sometimes I see that people, like, ask here for a view.
I see there are checks, but, like, I don't know, like, if… If this… like… Without looking at the code, if… We are still open discussion or stuff like that.
And so, like, for me, it's kinda… like, sometimes I merge stuff, because I see that I have, like, when I see green checks, I sometimes merge stuff, but… like, on the other hand, like, I'm not sure if I am doing some harm, because maybe, like, you prefer to merges other PRs, so, like, at the moment, I think the situation is a bit confusing.
as a final maintainer, but… Yeah.
Aaron Abbott 00:54:07 Yeah, I… I have the same feeling, like, I'm wondering if any other repos in OTEL, like… I know GitHub is particularly not well-suited to this kind of thing, but are there merge rights for… other groups besides, like, the strict maintainers and any other hotel repos? Is there some prior art here?
Liudmila Molkova 00:54:27 I can share how we try to do this in semantic conventions, and our PR load is smaller than yours.
But this is the flow that we have. Would you mind if I share my screen for a sec?
Okay, so, somehow I'm in the trust quipo. So we have this project board, similar to yours, and this is what we will look at during the call, and there is a column ready to be merged. Essentially, it means that there are enough approvals.
Well, ironically, this is not the PR that we are ready to merge. But… The normal flow looks like this.
When PR is created, it ends up in this untraged thing, then it's moved to awaiting code owner approval.
And this is where we are waiting for the green check from the SIG. So we would expect here that people from GenAI, like, 1, 2, and we decide, different companies, or… we decide what it means, for how… what is the criteria for PR to get the co-owner's approval.
So let's say I'm opening some PR. This, there are code owners. It's assigned, currently.
It requires approval from from, browser SIG.
if they approve, and I would see when they approve, because, they reviewed on behalf of, right? And the green checkmark will appear. And it relies on the maintainer knowing, okay, who are the… those people?
There is some tribal knowledge. But essentially, at some point, I can see, okay, it's approved.
And then, once it's approved, triage or anybody with right access can, move it to needs more approval.
This is where the… general… so we, like, our process is that we want the SIG, the sub-SIG, like, browser or GenAI to approve, then we want somebody from the general crew to approve.
And then one that gets to approvals, it moves here, and then any maintainer, should use their judgment, but, like, if there are no open discussions, and things go… look good, anyone can just go and merge it. So maybe I'll… I'll move it to block for now.
So it doesn't happen. But, essentially.
What we can do in Python is, or whatever the repo is, that we have the grace period where people are reviewing. We need to, let's say, hit approval from two different companies, if we are very cautious.
then, somebody should review just from the Python side.
And then, any maintainer.
seeing that things went through, should be able to merge it. If you feel, as a maintainer, it's controversial, you can give it a couple more days to accumulate feedback, but if it's not controversial, just… just let it be, let it go.
Not sure if it's helpful, if it answers any questions.
Riccardo Magliocchetti 00:57:54 Video, yeah.
Emídio 00:57:55 Yeah.
Riccardo Magliocchetti 00:57:56 phrase.
Emídio 00:57:57 I would say I really like the way Kubernetes managed that PRs.
Like, every… people can do things by just typing comments, like, slash, LGTM, and things like that, and they have a bot.
That can merge PRs.
Might… it might be a solution, like, for our case.
To people who have more powers.
And only a certain group of people can type comments, like people that belongs to OpenTelemetry, Contribution AI, Things like… things like that.
It would require, like, effort from our side to implement that, but… Yeah, it might, may work.
Liudmila Molkova 00:58:45 I wanna ask a controversial question. Like, why are we so hesitant to merge peers?
Emídio 00:58:52 Can you second?
Liudmila Molkova 00:58:54 why are we hesitant? Like, okay, there are, like, there are some rare peers that are difficult, and you can have, like.
I don't know, but if it's something that… Modify something to reveal.
Aaron Abbott 00:59:10 I think… I think for me, it's not necessarily if it's something trivial, it's very difficult to know if something follows the semantic conventions, and we, you know, like, we've talked about this a ton, like, having some kind of automation and conformance testing and stuff like that.
I think that's… that's probably my main one.
And if things are, like.
assuming we have all the automation set up, and it was dead simple, then I wouldn't really have any reservations if it was super clear.
Riccardo Magliocchetti 00:59:41 Like, for me, it's a bit different.
And it is that I don't know, like, what the GenA team is discussing. So, like, I don't know if they want this or that PR merge first.
And maybe, like, you had already a discussion that, okay, just merge this, and either a base on top, or stuff like that.
And they're not aware of that, so I'm a bit hesitant.
Matthew, like, usually, like, I think… Surya sometimes pinged me to review a merge, so… Like, when you ping me, usually I try to be active, but… I'm not saying I want to be pinged for every PR, so… About you.
Liudmila Molkova 01:00:28 Yeah.
Surya Teja 01:00:29 One thing what I want to chime in on this is, we can automate a lot of stuff.
So, Copilot and security bought from GitHub can be pretty much helpful, because this is an open source, and we should be mindful about security also.
I wanted to… I asked this in the SIG, and I was drafting a proposal that I can send to Trask to see if we can use Copilot reviews and security bot with Copilot.
to… Do an initial review, Before it goes to humans, so that it can, To reduce our cognitive load.
Liudmila Molkova 01:01:08 You can absolutely use it today. I'm not sure if you can do it automatically, but it's a good question to ask to Traz, but if you have access to Copilot, just ask her to review and know.
Surya Teja 01:01:17 Yeah.
Liudmila Molkova 01:01:17 Okay.
Surya Teja 01:01:18 I do not have access to it, but I left it inside the agenda to discuss, but I'll put my proposed… I put my thoughts over there, and I want to get some few comments from the maintainers also to see if it can help reduce the burden on their side.
So that, we can incorporate something to do this, semantic convention checks to, we could delegate the semantic conventions checks to the robot so that it can do an initial pass before humans can take a look at it.
Aaron Abbott 01:01:54 I think we're at time, but I don't know if we made a decision, Should we, like, take this on Slack? I think people are probably gonna have to drop.
Riccardo Magliocchetti 01:02:07 Or maybe…
Liudmila Molkova 01:02:07 Yeah, I think we should keep discussing it, maybe we should keep discussing it on the Gen AI. I think, Mike, you wanted to start joining the Tuesday call.
Mike Goldsmith 01:02:15 Well, yeah.
Liudmila Molkova 01:02:16 Yeah, but for the Python, I think whatever we identify should apply, too.
Either repo, or one day repo.
Aaron Abbott 01:02:29 Okay, yeah, and I think we need to discuss, like, the semantic conventions is separate from the instrumentation, and if that should live somewhere else, because I think… I think that's the way Weaver is supposed to work, if I understand right.
Liudmila Molkova 01:02:39 Yeah, yeah.
Cool. Appreciate it. Sorry for taking that much time, and there are some items we didn't get to.
Aaron Abbott 01:02:47 That's Okay, I'll see y'all next week.
Mike Goldsmith 01:02:51 Thank you, Emma.
Emídio 01:02:52 Decute.
Riccardo Magliocchetti 01:02:52 Thanks.
Erdenesaikhan Tserendavga 01:02:53 Thank you.
