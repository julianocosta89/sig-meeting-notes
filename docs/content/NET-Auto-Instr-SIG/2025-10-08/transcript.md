SIG: .NET Auto-Instr SIG
Date: 2025-10-08
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 00:34 Hello?
**Mateusz Łach** 02:18 Hello?
**Chris Ventura** 02:38 I'm just getting my machine set up so I can drive the meeting.
Okay, I'll go ahead and get us started.
So let's see, open pull requests…
Okay, so we've got, multiple PRs related to file-based configuration.
Let's see… For configuration-based instrumentation, looks like we got a fix for our test. We've got some…
**Piotr Kiełkowicz** 04:09 The boring one, but if you can approve, it should be auto-merge.
**Chris Ventura** 04:16 Okay, I'll just do it right now.
Okay.
Okay, so Dependabot updates,
Are there any file-based configuration PRs that we want to dive into or talk about in particular?
**Piotr Kiełkowicz** 05:00 I think plugins configuration is kind of our internal stuff, other… looks like.
More or less following the other approach, so… Maybe this one.
**Chris Ventura** 05:13 Okay So let's see…
Do we want to talk about anything in particular in this PR? So, like, the description here…
**Piotr Kiełkowicz** 05:36 Okay.
**Yevhenii Solomchenko** 05:36 What's… Hmm.
**Piotr Kiełkowicz** 05:40 YAM structure in general.
**Chris Ventura** 05:42 Yes. Yes. Okay.
So, we've got the plugins, plugin list.
Plugins Development…
Let's see, do we have an example?
Okay.
So, under Plugins Development… Plugins, and you can give it a list of plugins.
Do we support more than one plugin at a time?
**Yevhenii Solomchenko** 06:29 Yes.
**Piotr Kiełkowicz** 06:32 I doubt that anybody is using more than one plugin.
**Chris Ventura** 06:39 That's what I was wondering.
Because I could see it being difficult to coordinate between them if you're using multiple.
**Piotr Kiełkowicz** 06:56 And the plugin list is just for the backward compatibility, if anybody is using more than one plugin, just to populate it from the environmental variable.
**Chris Ventura** 07:10 Okay.
**Piotr Kiełkowicz** 07:14 And I think it is following the… resources configuration from… configuration spec.
**Yevhenii Solomchenko** 07:25 Yes.
**Chris Ventura** 07:32 Yeah, I think it's… it's fine.
Follows a pattern that… Exist for resources.
**Yevhenii Solomchenko** 07:45 I'm not sure about that, plugins development and the plugins naming.
Plugins inside plugins.
Maybe there's something… In that way.
In the future, when we… We're not development date, we're just plugins inside plugins.
**Chris Ventura** 08:17 I don't know if extensions would make it any clearer.
But it's…
Another word that could be used to… to allow us to have that structure so that you can have both the…
Plugins and plugins list nested under something.
**Piotr Kiełkowicz** 08:41 Where… I have a more general question.
I do not think about this during the no-code implementation.
But is there any recommendation to make our… any…
language-specific, or distribution-specific configurations, like prefixing it by .NET Auto Instrumentation, or something like this.
**Yevhenii Solomchenko** 09:10 I think only in the instrumentations.
for instrumentations, use the .NET.
You can open the instrumentation.IPR and, see how it looks.
Not for… specific our instrumentation and stuff, I think, spark doesn't say anything.
**Piotr Kiełkowicz** 09:40 So, I think what… what we could do, Evgeny, is to check with Tyler.
He's pretty active on the configuration.
SIG, and also working for us for Splunk, so…
It should be the shortest way to double-check the recommendations.
**Yevhenii Solomchenko** 10:02 Okay.
**Chris Ventura** 10:03 Yeah, cause I can see a case where somebody has their own distribution.
But wanting to bolt on some sort of custom configuration.
Perhaps it's related to a plugin.
That's… Being developed.
Something along those lines.
And so, if a plugin needs its own configuration, I don't…
I'm not sure if it makes sense to nest it.
Within this plugin's… YAML structure.
Or just have it be its own standalone thing in the YAML structure.
**Yevhenii Solomchenko** 11:02 I created, plugins development for
For merging that plugins and plugins list.
Back in one structure.
**Chris Ventura** 11:21 Okay… And so… Looks like we got a work in progress.
on, shoring up some of the dependencies for .NET Framework.
**Igor Kiselev** 11:43 Yeah.
Yeah, there are some… I created a draft pull request, it's… I'm still looking into a few issues that have been revealed by Unitest. I still need to add more unit tests, but the idea is already visible here, what it would be at the end, so…
And I described the wrestling.
Yeah, so basically, instead of one folder NetFix, with all files, collected for Net462, we use, only files that, for all
for all runtimes in that folder, and inside we create a special additional folder for Net462, Net47, 471, 472, and up.
And would load or registering GAC, only files, related to… current… Framework, the all… the additional
problem. I don't think it would be very critical for customers, but, if customer updates version of .NET,
from older to Inuva, he needs… and he registers everything in GUC. He really needs to uninstall and install assemblies in GUC, so that everything will work correctly for him.
**Chris Ventura** 13:11 Yeah, so this is the implementation, based on the discussion we had.
**Igor Kiselev** 13:15 Yeah.
**Chris Ventura** 13:16 In the separate ticket.
**Igor Kiselev** 13:17 Yes, yep.
**Chris Ventura** 13:19 Okay.
And we've talked about many of these other things…
Anything that we want to talk about for the OpApp client draft?
**Piotr Kiełkowicz** 13:41 I think we are looking for better…
for newer release from OpenClient, because it's… we already removed one dependency. There is the second one, protobuf.
And we do not want to break it here, so…
Grasmus will be working on the possibility to drop it as in OpenTelemetry OTLP exporter.
**Chris Ventura** 14:15 just want to remind everyone about this.
I think it's… Getting close… But, take a look at this.
And N-Log, I think it's still on hold, the developer's busy at the moment.
**Piotr Kiełkowicz** 14:51 I've spent some time to… Trying to fixing it, but…
**Chris Ventura** 14:59 Okay.
**Piotr Kiełkowicz** 15:00 It is the bytecode instrument that Mentos is wrongly choiced, in my opinion.
It is not covered.
all… Cases.
**Chris Ventura** 15:13 Okay.
New issues… This is probably one worth talking about.
So, Mateus, you notice that on… some Windows systems.
The, frequent sampling, is getting delayed.
**Mateusz Łach** 15:48 Yeah.
**Chris Ventura** 15:49 quirks of Windows.
**Mateusz Łach** 15:52 Yes, exactly, exactly. So, it seems like there is, like,
There is a known solution to that problem, which, like, has some drawbacks. I think the drawbacks might be, like, acceptable for this project. So basically, the…
The solution is to… to force the more accurate timer, but this…
Yeah, this has some side effects. So basically, while it's…
for the case of auto-instrumentation, I mean, the main drawback would be that this affects other processes that uses… that use the same API, so…
They might be, like, being waken up more frequently, so this might cause more, common context switches, so this might, like.
decrease, performance, but… yeah, so I think there are two options, either reduce the API,
the time beginning period API, or, or a document as a… As a known limitation.
On our side.
So… Yeah, I'm not sure if there are any, like, recommendations at this time.
Related to… This, because this was not a prob- this was not, like,
Not visible for the continuous profiling.
For which the frequency was lower, but if we…
For the more frequent sampling of threads, for some selected spans, if we want to use a more…
Smaller, basically smaller interval, this, starts to be, like, visible.
Or, more… Moreover problems, yeah.
**Chris Ventura** 17:51 I mean, the simplest thing for us to do right now is simply saying, on Windows, don't set frequent sampling to something less than 16 milliseconds.
**Mateusz Łach** 18:02 Yeah.
**Chris Ventura** 18:04 And then there's no side effects.
It would be interesting to find out if there are cases where somebody wants sampling more frequent than that.
I don't know if you've seen cases in the wild where you want more frequent sampling?
**Mateusz Łach** 18:28 Yeah, so, so, we were looking at something like…
50 or 20 milliseconds in our plugin, but this is, like, first beta that we…
Deployed. So, yeah, this… we can adjust also to…
To basically take into account this limitation, so…
**Chris Ventura** 18:57 Yeah, I guess where I'm leaning in, I can…
I think it's worthwhile for us to share our opinions on this, issue.
But… I just prefer to keep things simple until we have a need.
And then, if we… Have a need, then we can pursue doing something more.
**Mateusz Łach** 19:20 Sure Yeah, that makes sense as well.
**Chris Ventura** 19:25 But yeah, everyone, feel free, share opinions on this.
And then this way, we'll have it in writing.
Okay…
So this is a follow-up, for value task support…
I'm kind of leaning towards us waiting until we have a need.
So perhaps putting this in VNEXT?
I don't know if anybody wants it sooner than that.
**Zach Montoya** 20:10 I think that's… yeah, I think that's fine.
I'm trying to think if… I don't even think our data… the Datadog one has…
this support, anyways, and I haven't seen issues…
**Chris Ventura** 20:22 Okay. Come on.
I know that there's a handful of libraries that use ValueTask a lot.
I wanna say it's one of the two Redis libraries.
**Zach Montoya** 20:34 Yeah, I mean, if we're talking about performance, it's probably Stack Exchange.
**Chris Ventura** 20:43 So… oh, where is it?
Milestone.
So I'm just gonna park it there.
Just so that, we can reference it.
So, we talked about this… Last week… And,
I don't know that… if there's any updates… On, The experiment here.
**Igor Kiselev** 21:23 No, we haven't yet come to… Ariel.
Old what it should be.
**Chris Ventura** 21:30 Okay.
And then, yeah, file-based configuration…
Let's see, file base, yep.
Okay, yeah, and then this is… Looks like a stale issue.
And so, yeah, it's been a month, we've marked it as still, I'm gonna just close this for now.
Okay…
So, discussions… No discussions…
Guys, that looks fine.
And I don't think there's any updates to the project board.
Does anybody have any topics they want to bring up?
Huh.
That note, we can all get some time back.
Thank you all.
**Zach Montoya** 23:17 Thank you.
**Igor Kiselev** 23:17 Good question, actually, about, just closed, 4239. Have anyone tried, at least, follow the steps that, original rapport said? Because he attached
to sample application.
And I haven't seen any text that anybody confirms that they tried it.
About a stale issue that we closed the sale.
**Zach Montoya** 23:47 Sarah, which issue is this one?
**Igor Kiselev** 23:48 4239.
**Zach Montoya** 23:52 Okay.
**Igor Kiselev** 23:53 4239, because honestly, when I read a text, looks like in the first, report, the customer provided, binaries, on which he produced the issue.
Then nobody mentioned anything that, we tested it, we just, pointed him to some other issues that maybe it looks the same.
And after it, customer confirmed that he can reproduce it in his environment, and asked if we was able to reproduce it in our environments, and we just closed on it.
Cool.
I'm not sure that it's… a proper way.
Wrecked.
**Zach Montoya** 24:39 For this one, I'm… if you think it's worth a second look, I can, I can try to run the steps that were, submitted, see if that yields anything that we can look at.
**Igor Kiselev** 24:52 Because… because if… if we, if we tried it and it would not work, we… we should close, otherwise we could probably review it, and it may be up to some level correlated with what I'm doing with, .NET Framework,
proper loading in different subdomains, so it's something that I could look… not right now, I would be busy with penalizing what I am doing, but maybe in some weeks.
**Zach Montoya** 25:22 Yeah, I can certainly, try to pull that down and see if that…
like, if I can reproduce the issue, and then I think that would be a good signal, like, to see if that would go along with your work.
**Igor Kiselev** 25:37 You too.
**Chris Ventura** 25:41 Yeah, cause that one's… Because it's all the same apple, it's the same process, And so it only gets…
**Igor Kiselev** 25:54 the info from whatever's loaded first. It would be different, domains in the same prototy, because he created different applications on iOS. So, I would say that it's…
It… it have high chances that something would go wrong, and it's at the same time probably not the way what's tested all the time, because we usually test one application. So, it may be pretty real, just based on the description.
**Chris Ventura** 26:25 Yeah.
**Igor Kiselev** 26:25 Maybe still an A user mistake, so… A's could be.
**Chris Ventura** 26:30 Yeah, as long as they're not relying on environment variables for the… Application name… Or the service name.
Because even with a separate app to name, it would… be a…
It would be the same environment variables.
**Igor Kiselev** 26:53 But…
still… it would be pretty easy to understand if both applications are instrumented or not, because it depends on if transaction only from one. If spans only from one application register on a coordinator, it means that second application is not working properly.
Oof.
I… I could look into it also later, but…
I'm afraid that if we would just close it, everybody would forget about it.
**Chris Ventura** 27:26 Zach, do you have time to…
**Zach Montoya** 27:29 Yeah, I think I'll have… yeah, I think I'll time this week.
Before Nets meeting, yeah.
**Chris Ventura** 27:35 I'll just… Add your name to it.
**Zach Montoya** 27:41 Okay.
**Chris Ventura** 27:51 And do you want me to reopen it for now, Zach?
**Zach Montoya** 27:54 Yeah, that sounds good.
**Chris Ventura** 28:02 Okay.
Thanks for bringing that up, Igor.
**Igor Kiselev** 28:07 Oh, welcome.
**Chris Ventura** 28:12 Okay, anything else?
See y'all later.
**Zach Montoya** 28:18 Alright, see ya.
**Mateusz Łach** 28:21 Thank you. Bye.
