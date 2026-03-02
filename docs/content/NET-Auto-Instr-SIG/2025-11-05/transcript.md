SIG: .NET Auto-Instr SIG
Date: 2025-11-05
Duration: 39 minutes
Zoom Recording URL: https://zoom.us/rec/share/mBpUFiD314KiF-BYcpNoVimHC6K-ZUJjt2AhEzrZdB-3O5LX719pQ_K_DjIwwO15.MbtksxYl5MQNIKql
============================================================

## Zoom Recording Transcript

**Zach Montoya** 03:13 There you go, I'm unmuted now.
**Yevhenii Solomchenko** 03:15 Bye, guys.
**Zach Montoya** 03:17 Let me start sharing, and we can get started.
Let's see, let's do this… Oops.
Okay…
So, let's see, does anyone have any specific topics they wanted to…
Discuss outside of our normal agenda?
**Yevhenii Solomchenko** 04:11 About a pair, file-based concept for… Internal logging.
**Zach Montoya** 04:24 Is there… do you have a PR on this, or…
**Yevhenii Solomchenko** 04:27 Yeah, I have a PR and a comment in the PR.
**Zach Montoya** 04:31 Is that…
This one, okay.
Alright, so… This one?
**Yevhenii Solomchenko** 04:44 Yeah, general issues about, do I need to compile… the… package of YAML.NET into… Startup Hook and loader.
And.
**Zach Montoya** 04:58 Oh, interesting.
**Yevhenii Solomchenko** 05:00 Yeah, because that's, compile that, Bogger into that package… packages.
**Zach Montoya** 05:07 I see, so we're already compiling that as part of OpenSeometry auto-inputation, correct?
**Igor Kiselev** 05:13 I'm… very worried about that, because I need to check what dependencies have yaml.net, because for loader.
**Yevhenii Solomchenko** 05:21 No, no, no, no, no, no, it's vendor at vendor at yaml.net.
It's not a dependency.
**Igor Kiselev** 05:27 No dependers, okay, in that case.
**Yevhenii Solomchenko** 05:29 Yes.
**Zach Montoya** 05:34 And are we already vendoring YAML.NET in the main OpenSeometry out interpretation?
**Yevhenii Solomchenko** 05:39 Yes, yes.
**Zach Montoya** 05:41 Okay.
I'm so used to compile.
Sorry, we're, how exactly are we using it in the… Loader?
I'm sorry to puck.
So, the idea here is… Okay, loader… That's something to… Vendor those… And then… Oh, I see.
So, hotel logging is… Sorry, how is this being used in the loader?
**Yevhenii Solomchenko** 06:30 It's already compiled when I start to…
Use it. I think it's, log some loader configurations, debug, some debug, logs.
For the checker, I think you should open the project.
**Zach Montoya** 06:49 Sorry, open… what should I open?
**Yevhenii Solomchenko** 06:52 Full project of optometry instrumentation.
**Zach Montoya** 07:14 Sorry, I'm a little lost.
So, so this PR is computer internal logging, Using YAML.
So basically, you're also trying to say, instead of just the OpenTeometry.net.
or the auto-instrumentation project referenced in the YAML, that also within our,
Our loader would also reference that file.
**Yevhenii Solomchenko** 07:41 Yes.
modern startup book.
Also, it will compile that, full YAML vendorat code.
**Zach Montoya** 07:51 Oh, I see, because it's trying to read it there.
What if we… what if we don't do that? What if we only do it in our auto instrumentation projects?
**Yevhenii Solomchenko** 08:03 We don't do logs from a loader, if you don't use that.
If you don't compile.
Maybe you have another way to… instead of compiling… Lawler.
**Chris Ventura** 08:18 I guess another way to ask the question is, what settings does the loader need to
access, which drives the need for, including the YAML.NET.
And full configuration.
**Yevhenii Solomchenko** 08:40 Give me a second.
**Chris Ventura** 08:50 One of the ones that comes to my mind would be the fail fast check.
**Yevhenii Solomchenko** 09:14 Actually, we need logar in, loader… Package for logging.
Some information from the… Water.
So, for that, we compile… Logger into the loader.
**Zach Montoya** 09:41 So this isn't… Trying to use…
File-based configuration for other things is just so we can get, logger settings?
**Yevhenii Solomchenko** 09:51 Yes.
**Zach Montoya** 09:54 Okay.
**Yevhenii Solomchenko** 09:54 But the logo.
**Zach Montoya** 09:57 Okay.
**Igor Kiselev** 09:58 I have a question. What we do with a logger for a profiler in that case? Are we doing it in a profiler 2 and parse from profiler or not? Because
it's… that loader logger sounds for me as a very special logger, same level as a profiler. If we handle it some way in a profiler.
Probably for a loader only. Think we could, add some native API to our profiler, so that a loader log would also go through a profiler to not
Included in one additional place.
they would…
So, I don't have a very good idea about, what can be done in, hook… in our startup hook, because a startup hook can function without a profiler at all.
**Zach Montoya** 10:55 Yeah, I do know if there… if we do anything special with the…
profiler? I suspect that we are just reading environment variables, and then we write to, like, the default path of, like, program data logs, and then maybe we read a log level?
I don't think… I don't think our profiler is reading.
I don't think we're trying to read the, file-based configuration for that.
**Chris Ventura** 11:22 Yeah, cause it's… You should…
**Yevhenii Solomchenko** 11:24 Yeah, but the issue is created for using Filebase also for native code.
**Zach Montoya** 11:29 Oh, okay, so that's something that you're proposing we do, okay.
**Yevhenii Solomchenko** 11:33 And so, we'll be implementing in future, I think.
Rosa.
**Zach Montoya** 11:38 Okay.
**Igor Kiselev** 11:47 Yes.
**Zach Montoya** 11:48 So, if the entry point… the entry point would go startup hook slash… Profiler…
And then that would launch… Do we always launch the loader?
Assembly?
Does it go startup… like, I know startup hook eventually loads the rest of the instrumentation, but does it go startup hook loader instrumentation?
Or is it straight just startup hook, auto instrumentation?
**Chris Ventura** 12:20 I remember them sharing code. I… don't…
I don't think one calls the other.
**Zach Montoya** 12:29 Because native goes through the loader to get to instrumentation.
But then starting here, I don't remember…
**Chris Ventura** 12:37 Yeah, the… So, native calls the loader for… NET Framework.
And I think we rely on the startup hook instead.
for .NET…
**Igor Kiselev** 12:54 But for sure, we have some branches in, loader that serve for .NET also. So, up to some…
**Chris Ventura** 13:06 Yeah, what I don't remember is if we actually…
Are just reusing some of that code?
Or if we're reusing the whole assembly, because I thought the loader assembly was this special case where it was an embedded assembly, or…
**Zach Montoya** 13:25 Yeah.
**Chris Ventura** 13:25 Something like that.
**Zach Montoya** 13:27 Yeah, early on, and I think it might still be the case, this is sort of the bridge, so we embed this inside the native…
DLL.
And then we, like, assembly load this, and then this gets started with… Naturally…
Oh, there's the Resolve event. That's not the one.
The sell does some of the resolver stuff.
I forgot where we absolutely load the instrumentation.
**Chris Ventura** 13:59 But yeah, with that being said, I don't think we ship a separate… Loader assembly.
And instead rely on just sharing some of the code between the startup hook and the assembly loader.
**Zach Montoya** 14:20 Yeah, that sounds about right. Let's see… We include instrumentation… Okay, this is all just… instrumentation code.
Anyways, yeah, the point I was… I was… I was trying to get closer to is… where do those paths converge? So, like, if we're trying to do…
if we're trying to eventually read the file-based configuration to doing that in the central place, I'm not sure if they start sharing the code path when they just already launch auto transportation, or if there's in the loader code, if that's where they converge, and that's where we'd want to…
Try to read that. Yeah.
So right now, as it stands, for this one, you're saying that if we… Palace as is…
This would increase the loader size by, like, 300 kilobytes.
**Chris Ventura** 15:51 Which, file do we write the loader logs into?
Because we have a native log file.
**Zach Montoya** 15:58 Yeah, I think we have a separate loader log file.
If I'm not mistaken, so… Loader log, loader logger, suffix, loader…
Hotel logging…
And this takes a suffix, right?
Yeah, so get our add suffix.
But yeah, I think we just, drop it in the same folder, but we have a different suffix in this case, so it's called loader.
So… The system just writes to a loader file, and then the rest of the instrumentation would write to…
Just, like, a general managed kind of file, and then our profiler…
Just writes to an entirely…
Different file, I don't think they communicate at all.
**Chris Ventura** 17:11 Right, and so I'm wondering, in order to…
Keep the implementation simpler for now, keep the, assembly smaller, especially that loader assembly.
If it makes sense to treat it as a separate thing.
And… it doesn't support full… YAML configuration.
Like, can we do something smaller?
Because just… how many settings do we actually need to control the… the inner logger?
**Yevhenii Solomchenko** 17:45 4, I think.
**Chris Ventura** 17:47 like, is there a lighter weight way for us to support those four settings? Or do we need the full…
Yeah, multi-pendency.
**Yevhenii Solomchenko** 18:01 We don't need a full butter. Anyway, we need about a half, maybe.
dependency…
**Igor Kiselev** 18:14 it is the question, could we implement some lightweight YAML parser that would be able to parse only that for settings? I'm a little bit afraid that,
It would be…
It would work in many cases, but it would not work in some cases. I don't know specifically about YAML, but there is some rules about how it can be escaped. In some cases, how it could be quoted in one cases, how it may not be quoted in other cases. I don't know if they have some entering and other things, and yes, it would probably work in easy cases, but there would be always some edge cases where
So, trivial parser would fail to parse it.
Maybe it's okay.
I not say that it's… Not good, but…
**Chris Ventura** 19:02 Yeah, and so that's a good call-out, especially if somebody decides to do some sort of includes, like.
build a YAML file using includes and things like that.
maybe… so another idea is, if we only support environment variable configuration, for… The loaders and startup hooks.
Just to give more time to figure out how we want to handle things in the long term.
Because I feel…
**Yevhenii Solomchenko** 19:44 That's correct.
**Chris Ventura** 19:45 I feel like if we increase the size of that loader, Significantly.
Like this does. And we're embedding that in the native… assembly… I…
I'm not sure what type of side effects we're gonna get with that.
Across all of the different systems.
**Igor Kiselev** 20:14 I would still suggest also try an approach with sending logs to a profiler.
If we have a profiler. So, in case of loader and it would solve both loader sync and startup hooks when we have a profiler. The only case which would not be solved is a startup hooks without
profiler.
So it can be probably done much easier.
They have very, very limited amount of locks from that… both of that assemblies.
Wonderful.
just several lines of logs, anti-YAML parser feels a little bit overkill.
**Zach Montoya** 21:00 I could also see us doing this as a conditional compilation, where we can iterate on this, but not compile it by default, and then that would give us the ability to try and
I don't know when… If we're planning to do benchmarkings of this.
But that could be an option if we wanted to have it not compile
This dependency by default, and then just have that flag so we can later start to do experiments on it.
**Igor Kiselev** 21:35 Benchmarking, it's already… we have all data about that it would increase assembly size by 300 kilobytes, and it would
increase, potentially, for a customer, that use a law that
use, YAML log, it would increase by 1 or 2 megabytes, runtime usage, because it would installize types.
One more time… And they still load bigger assembly, so it's not a huge effect.
But…
And for Loader, I'm very much more about what we actually use inside YAML parser, because loader may work at a… right now, a loader, for example, after my fix, works at up the main construction time.
So early stage of, NET installation that many class.
used at that time may affect, break an application. After it, it would be… it would require a lot of tests.
before we could say that, yes, it's okay or not, or just make sure that we never use logs
in case of, when we use a loader in that early stage, but in that case, I would still have a question, okay, now we need to have two log systems, one that is used if we are in early stage, one in later stage.
tricky, it now sounds, for me.
**Zach Montoya** 23:16 Yeah, that makes sense.
So in this case right now, the potential options we said were… To one, investigates…
Doing this within, like, the native profiler, having that… being able to… Read the ammo? Is that…
Is that accurate, that that was one of the solutions, or one of the… approaches.
**Chris Ventura** 23:50 That's one of the approaches.
I do think, for the immediate need.
If the existing solution just respects the environment variable configuration, that…
That might be good enough in the… Imme… for the immediate needs.
But that's mostly just to buy us time to explore a few options, and so… Option 1.
If the profiler's available, if there's a way to send the information to the profiler,
Option 2, perhaps, is configuring a… Separate, bootstrap logging.
where, it only applies to, to the… the startup.
Logging before the rest of the system is able to be initialized.
and treat that as a separate concept. Yes, it diverges the logging that we have.
But if the configuration is distinct, maybe that never supports.
YAML configuration.
And it only ever supports environment variable configuration.
**Igor Kiselev** 25:21 worst case, we could build, as we said, that if we're talking all the… so if we talk about, the only configuration that a profiler is not available is a startup oops without a profiler.
Theoretically, we can compile two different versions of startup hooks.
And, suggest, customers that require… that needs to use a YAML configuration in that specific way.
So, without a profiler, to just use different startup hooks, they allow?
I don't like it, but just… as an idea.
**Zach Montoya** 26:14 Sorry, I was trying to jot down some of the stuff so I didn't really…
Receive all you just said, Igor.
So I want to make sure we kind of document what we were talking about.
Okay, so yeah, so for right now, we can still just use environment variables,
But yeah, I think it would be good to… to document, or to understand which…
Environment variables we would actually… or, yeah, which configurations we would use, and then we can see if that's something that we should do.
I think right now.
**Chris Ventura** 26:54 Yeah, and maybe we wouldn't need a separate, startup hook build.
Maybe there's, some sort of middle ground there, where…
If certain environment variables are present.
Then… it wouldn't… push the logs through to the profiler, and would instead
Do something more like what we have today.
So, I do think there are options.
**Zach Montoya** 27:47 Does that give you some sense of…
Next steps, you have any, or, what's your takeaway?
**Yevhenii Solomchenko** 27:55 I'm thinking about another approaches. I'm thinking about one approach that, like, maybe also needed for some .NET and profiler configurations. It's, we need to read YAML and set current NVARs.
Somehow.
Understand about… that approach.
**Igor Kiselev** 28:22 Of course, but…
**Yevhenii Solomchenko** 28:25 or SparkQ, Need all the environment variables, so…
It will be hard to set profiler…
Which is not in the OpenTeometry, and even not the… I don't
Another level in the… in those.
configuration, I think.
profiler environment variables.
**Chris Ventura** 28:53 You talking about the… the environment variables to enable the profiler?
**Yevhenii Solomchenko** 28:58 Yes, yes. Of course, LR, profiler.
**Chris Ventura** 29:02 I don't.
**Zach Montoya** 29:02 Oh, really.
**Chris Ventura** 29:03 ever be part of the YAML.
**Zach Montoya** 29:04 No, that has to be environment.
Unless you wanted to talk about, like, customizing the continuous profiler, like, you know, interval, like, how often to take samples or stuff like that, but the core profile enabling…
**Yevhenii Solomchenko** 29:21 Yeah, for that solution, I mean, we can read the YAML and set that environment variables from the YAML.
**Igor Kiselev** 29:30 You mean in setup, initial script?
**Yevhenii Solomchenko** 29:34 Yes, some success. Yes, yes.
**Igor Kiselev** 29:36 So before, before you start an application, yeah.
**Zach Montoya** 29:39 Okay, yeah.
**Yevhenii Solomchenko** 29:40 That's lovely.
**Igor Kiselev** 29:41 Potential option, yeah.
**Yevhenii Solomchenko** 29:44 And keep current that solution for logs, also.
For logging.
**Zach Montoya** 29:51 Yeah, that could work if you had some… some agent or some…
Something that was guiding the deployment of starting processes.
Cool, shall I move on to the rest of the agenda?
Let's see, I know there was a… a lot of the, file-based stuff that was merged, so… really cool to see that. In progress, we still have this N-Log one, which I actually have not looked at recently, but…
It's kind of been stuck there.
a little bit.
Okay, yeah, it's just stale. They haven't gotten a chance to revisit. Okay, there's a couple of draft PRs, we just discussed the internal log and Jet Startup Assembly. Okay, configured. And then we have generates net effects, transient dependencies, any high-level…
**Igor Kiselev** 30:55 Oh, yes.
So there are two changes that, so, initially, we have a bug report that, yesterday, that, generate NetFix dependencies, do not remove unused, transitive dependencies. On one side, it have never done it before.
So it was not something that had broken, but at the same time, I looked on trade, and the problem was,
So, it's… yes, it's some inconvenience that we have some garbage in our version file, and without any easy way to identify which of the lines we don't need at all.
Because they generate it, and we do not ask all the time, okay, give me the list of all transitive dependencies that I actually have.
So, main idea, I added a way for generate transitive dependencies, to remove, package version reference, from auto-generated section.
It's not always good, because sometimes, you would like to… when we generate the dependency, we always use the oldest possible version, so we do not out-update it, but we just say what, that if we,
we just found it, which dependency.net used by default.
So, in some cases, you may add a dependence, get a new transitive dependency, then you would update a version of that transitive dependency, and then, for example, you remove
Initial dependence, so downgraded the version, upgraded the version, and now the lines that you already modified would disappear from a file.
If you've already committed that file, probably not bad, you would even notice, it would simplify, notice it. On other side, if it's in a work time, it may be not always good, but at the same time, we do it only for package versions that are in a section auto-generated.
So the clear is that everything here auto-generated. If you need it all the time, just move it from auto-generated section somewhere else. Second thing that in that pair that I have done, so, previously we have only one auto-generated section, but
After my change, we have a
separate auto-generated section for .NET 462, 4.7, 471, 472, but it is not very convenient to manage, because in most cases, it would be the same line. So I added a grouping, so if we have the same dependency, the same version for all frameworks, in that case, I move it to a separate section that
use only common dependencies. So, most likely update, it should not affect anything for production, because even if we have a garbage in the directory packages props file, it would not be applied, because we just
So that if that transitive dependency is used, please use that version.
But if we do not use the transitive dependency, that version would be just ignored. So, nothing changes except of quality of life for developers, so not…
required. Quick few… quick merge or something like that.
**Zach Montoya** 34:31 Okay?
Yeah, okay, yeah, I'll take a look.
I think, I think I need to refresh myself on this.
On this, transdependency.
Generation.
**Igor Kiselev** 34:50 there was a… there is a reference to a bucket, so it's pretty easy to understand what happens. So, I'll…
one of OTEL, OPAM dependency, Alpha 1 that used, added, system, collection immutable, dependency, and Alpha 2 removed that system collection immutable dependency. So that's why a developer wants added system,
immutable that OPAMP alpha-1 version, dependency generated for him,
It is at least a reference to system… not reference, but package version for system collection immutable.
Once he updated to the next version, system collection immutable was still in a file, because it's generated, but does not clean up.
**Zach Montoya** 35:46 Got it. Okay.
**Igor Kiselev** 35:50 Or both of my in sync.
Once again, it was not very critical, because the generic version would not be used, as there is no dependency, and we would still not put… we would not put system collection immutable to our output folder, but…
Have some garbage in.
Accelerated section.
Okay. At the same time, there was a suggestion to, can we just clean up entire package, package version section and regenerate it? It's not possible, because with central package management, we must have a package version statement for each
used,
for each used, top-level dependency, so if there would be only transitive dependency, probably. If not, but still, we would need to remember what was before, right? Because, because we may… we may not use the oldest one, and in most cases, we would have an updated version.
Ugh.
Okay.
**Zach Montoya** 36:58 Got it.
Okay.
Cool, yeah, we'll revisit this, PR in, give it a review.
And then we have one last dependent one.
So, should be simple enough.
Rest container.
Alright, so… Going through the rest of our agenda…
So, let's see, issues, okay, yes. This was tracking the new work.
Additional file-based configurations…
So yeah, I don't think there's anything too new here, just more file-based configuration work.
And this one we just talked about's… No discussions…
Nothing to check on this milestone in particular.
And then, just a general project board.
Don't believe we have really any updates here.
I guess a question for you, if any,
how many… are we planning… is the idea to implement all these, before, like, we do the next release? Are we still tracking all these, or are some of these, like, out of scope?
**Yevhenii Solomchenko** 38:24 I think in that release, we definitely need integration tests and documentation examples, as remains only.
I'm not sure about, native code, and
I'm not sure about, optimized parsing resources, because it can be a build line.
Okay.
**Zach Montoya** 38:45 Okay, yeah, definitely agree on these two.
Okay, so we can, once we kinda get those…
Get those moving and get those merged, then we can revisit, how much more we need to include.
Alright.
I don't think there's anything else…
Any other topics you guys wanted to discuss while we're all here?
Going once… right?
Cool. Well, thanks for the discussion. Yeah, I'll see you guys next time. Thanks, everyone.
