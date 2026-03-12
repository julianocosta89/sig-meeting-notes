SIG: Java SIG
Date: 2025-08-21
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/QBeG2ZKa-kdjO1vXF47AdhKcApuTPyvMXEekcZso7lrUd9BiuyJ-2PNrnMospkBt.GMORr1IiytsOUMwd
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:02:21 Good morning!
Steve Rao 00:02:36 Hey, Chaska.
Trask Stalnaker 00:02:39 Hey, Steve. Hey, Jared.
Good morning.
Steve Rao 00:02:43 Okay, yeah, non-tano, C.
Trask Stalnaker 00:02:45 Yeah!
Steve Rao 00:02:49 Yeah, some of, folks, they are on the road to the company. They will join us, a couple meetings later, maybe.
Trask Stalnaker 00:02:59 Okay.
Steve Rao 00:03:00 Okay. Yeah, maybe we can, start, firstly, and I have a question I want to discuss with you today.
Trask Stalnaker 00:03:10 Sure.
So true.
Steve Rao 00:03:16 Yeah, here.
Trask Stalnaker 00:03:19 Alright.
Customizable parent class loader… For the agent class loader.
Crash Log Collection.
Steve Rao 00:03:36 Yeah.
Trask Stalnaker 00:03:39 on error… … Okay… Create a crash that needs to be executed, … Yeah, this is, … I've never used this, so just trying to… So, on error… Do you specify it?
here? Is this supposed to be, like, "-XX on error… something?
Steve Rao 00:04:14 This is a class, across, data, collector, yeah, we developer in our disk tool. And, Yeah, maybe I can explain more about the on-error parameter of GVM.
Yeah.
Trask Stalnaker 00:04:33 So how do you run… how would you run it with the Java agent? So, like, if I'm running Java… dash our agent….
Steve Rao 00:04:47 … Yeah, yeah, maybe we can add this parameter on the command.
You can add on, … on, on the, parameter, behind, Java agent.
between the Java agent and a user's application.
Trask Stalnaker 00:05:13 Oh, okay, so current… let's see if you show this… oh, sorry, there's more stuff, yeah.
… Desired constructor signature, okay, yes, you want to pass in a parent class loader, yep, understand.
… When Jesus… Java process crashes, executes, the XX on error… script.
Okay, the piece I'm missing that I'm not following yet is how do you specify the crash data collector class. Have you….
Steve Rao 00:06:01 That's….
Trask Stalnaker 00:06:01 Five.
Steve Rao 00:06:03 Yeah, yeah, I can explain, more… More about these.
… … Yeah, in fact, this, parameter, we add, add it to the, Yeah, you, yeah, let me show an example.
Trask Stalnaker 00:06:27 Yeah, you wanna share?
Steve Rao 00:06:30 ….
Trask Stalnaker 00:06:36 Let's say hi to Antoine. Hi, Antoine.
Steve Rao 00:06:40 Okay, maybe I can show it on, Google Doc. Maybe I can, yeah, give the example to on Google Doc.
Trask Stalnaker 00:06:49 Oh, sure.
Steve Rao 00:06:51 ….
Trask Stalnaker 00:07:02 Wise… Okay, and then you give it the… File….
Steve Rao 00:07:11 Yeah.
Can you see the example? Yeah, maybe we… I just need to add the parameter to… user's, application, and the script, we can, contain the, script I show on the issue.
something like a Java Gong, license key.
equal, blah, blah, blah, and, and I can also, tell the script, the location of, Christ's Lock, something like, like.
Trask Stalnaker 00:07:50 Sorry, just give me one second… … So, crash… oh, you give it a… a script, a shell script.
To run?
Steve Rao 00:08:05 And,
Trask Stalnaker 00:08:07 And the contents of the shell script is this. I understand, thank you.
Steve Rao 00:08:13 Yeah.
Trask Stalnaker 00:08:14 Okay, interesting.
Okay.
Steve Rao 00:08:19 Got it. One error is a hook provided by GVM, and when a vacation occurs, a photo error, something like a crash, and it will execute the hook. And in this way, we can collect the crash log directly.
Trask Stalnaker 00:08:39 Right.
Now… okay, that… I got that part. Now, can you… what… how does that connect to the parent loader?
Steve Rao 00:08:53 ….
Trask Stalnaker 00:08:53 Because this seems like it's just executing an external process.
Steve Rao 00:08:57 I achieved this, … I get the agent class loader in a cross-data collector. This is a Java class.
In its main, method, maybe we can get the agent class loader.
And, use the constructor of Agent Class Loader to create an object.
When it's, executed.
Trask Stalnaker 00:09:27 So, when this happens on error.
Is this just any… it happens on any… … Is that a fatal error, like JVM dump, or is that any error, like, anything that… throws, like, java.ling.error.
Steve Rao 00:09:51 Something like, … something like photo arrows.
In QA. What error?
Trask Stalnaker 00:10:00 Fatal error. Okay, so when it's actually Generating a crash dump.
Steve Rao 00:10:06 So is the process dead at that point?
You mean, when it, created, message of, of federal… Fetter Arrow.
Trask Stalnaker 00:10:24 Yeah, when this, when this crash dump class.
Steve Rao 00:10:29 Shell script runs.
Trask Stalnaker 00:10:32 has the original JVM terminated, or do you still have access to it somehow? Or are you still inside of that?
Steve Rao 00:10:44 ….
Trask Stalnaker 00:10:44 JVM?
Steve Rao 00:10:47 Yeah, in fact, we achieved, the script in our distro, and when the application starts, and we will write… Grip on users' environment.
And, when, when, when the, error happened, and, the GM, well, executed the, script, crash script.
And, in that time, we will, We are, give, tell the application, which file we need to, generate the crash log.
Something like, … yeah, something like, show on the issue. We, set a, parameter.
arms, … Paul.
Trask Stalnaker 00:11:44 So, in Crash Collection Service, the agent class loader needs to look at classes that are not… in the INST directory, but are there one other… modules… … Okay, why, maybe… I mean, it might help if you could throw together, like, a small proof of concept.
bet.
You know, what does this crash data collector look like?
Hawaii, you know, how does it call? Why do we need… the parent class loader, because I'm still not quite….
Steve Rao 00:12:31 ….
Trask Stalnaker 00:12:32 Making that loop.
Steve Rao 00:12:33 Yeah, yeah, yeah, yeah, maybe you can, yeah, you can, find the, use case of agent class loader, on value Java Agent. I can tell, how we use it in, across the data collector.
Antoine Toulme 00:12:56 So you're trying to collect the crash at the time of crash, but the Java process is not dead?
And there's.
Steve Rao 00:13:03 comment.
Antoine Toulme 00:13:03 weekend.
when, on case of out-of-memory error, you can actually execute a script, and we're trying to execute a script as part of that to collect data and send it to some backend. Is that right?
Steve Rao 00:13:14 Yeah.
Antoine Toulme 00:13:16 But by that time, you've left the comfort of your JVM, and you're back into user land with not that much to go on.
And none of the utilities that you had before.
So it's, like, kinda hard, actually. … And you're trying to do what's….
Trask Stalnaker 00:13:31 Antoine, it sounds like there is something… connection to the current Java process, because the… they want to make a change into the Java agent.
It's solid.
Steve Rao 00:13:44 ….
Trask Stalnaker 00:13:45 to support this?
Antoine Toulme 00:13:47 Whoa, okay, that's awesome.
Steve Rao 00:13:50 Yeah, in fact, we just want to, yeah, add the, collection logic to Java Agent, and we don't want to, write a script, independently to collect the crash log.
And, when the, crash happened.
And, we don't can use the, application, processor to do these things. We need to execute the script, and this is another, Java processor. So we cannot, use the… Hmm… class loader mechanism.
in this SaaS.
So, we, we, we can… load, its parent's, class,
Antoine Toulme 00:14:39 Yeah, so you're….
Steve Rao 00:14:40 uncover.
Antoine Toulme 00:14:41 Yeah, type thing, or…?
Are you doing a nice GI-type class loading, or is it something custom to you?
Steve Rao 00:14:54 Yeah, no.
Antoine Toulme 00:14:57 So, you're familiar with OSGI, right? Or is that…?
Are you using this type of, overloading class loader, or…?
Are you doing something else?
There's no way, at least in Java between class others when it comes to memory use, like, you're out of memory, you're out of memory. So, we can try.
… Stuff. … may I ask, maybe, why you're doing this? Maybe we can come at this from the point of view of the requirement?
Before we go into solutioning?
Steve Rao 00:15:30 Sorry.
Antoine Toulme 00:15:35 Did you… am I coming out clear, or…?
Can you hear me okay?
Steve Rao 00:15:46 Yeah.
Trask Stalnaker 00:15:46 I hear you. Okay.
Antoine Toulme 00:15:49 Alright, I'm on my earphones, so… So, dumb question. Why are you trying to do this?
Steve Rao 00:15:56 Yeah, because, we found some users, they were, Yeah, when their application will occur to crash, and they, they don't know how to solve this question, and, really, CrashLog can, help us to analyze the reason why the application crashed.
So we, we, collect this information. It's, important, especially in, Kubernetes environment, when it occurred crash, and the, instance will, restart again, and, we, if we… Don't, collect the crash log, independent, directly, the, the, the, the information will disappear.
Antoine Toulme 00:16:48 Hmm.
… Yeah, because you can't be sent by your TLP, because The log exporter for itself is gonna be dead anyway, right?
Are you… are you currently logging via OTLP, or are you logging and getting the logs another way?
….
Steve Rao 00:17:08 Yeah, in fact, we found if we don't use this way, we can't use something like Java Agent to collect the log, because once a crash occurred, the Java agent will start to walk.
Antoine Toulme 00:17:27 Yes, yes, okay, that's what I'm saying. Okay, agreed. Completely serious. … I mean, it could be interesting to get profiling information that… even leading to the crash.
So that you can get an idea of… unique?
Steve Rao 00:17:46 You mean to use something like profiling to, diagnose the crash?
Antoine Toulme 00:17:53 Yeah.
That's one way.
Another way is, so on the crash, right, you can get multiple things.
You can ask for a heap dump to be written to file.
You could ask for substack to be returned to parallel to the CDL.
… What do you think is going to be useful in that information that's going to help you diagnose the crash?
Or do you….
Steve Rao 00:18:20 Yeah, in fact, yeah, what we found so, many crash problems, yeah, is because, when some user use, some profiling tool, like, a sync profiler, in some early version, it will cause, course crash.
Yeah, this is the first reasons.
While we solve any crisis, scenarios. And, yeah, we also try to use other tools like profiling, but it can, solve these questions. We found that the crash log is, yeah, it's very important and useful.
Information have asked to diagnose these questions.
Antoine Toulme 00:19:05 So, in my… in my view of the world, when it comes to Kubernetes, the way my team has addressed this issue is that we don't trust OTLP exporters from SDKs to collect the logs. We go to the Kubernetes logs, and then we get the logs from there. These are, a couple ways to do that. One is AWS CloudWatch.
You can send it out there. You can trade them from there.
The other approach is to have a demand set with access to the host to mount the volume where the logs are.
With a init container that changes the permissions on those logs.
And then you scrape those logs using a file log receiver with the container parser information.
Those things, give you more information.
Because they don't rely on the side of the program, and if the program crashes, as long as it's actually, you know, recurring this information out, then you can actually get that information.
Another approach you could take, which is a little bit of a janky approach, is, You could have… A job application runs.
… You could make it run inside of Bash Wrapper.
The Bashraptor could be catching the application if it dies, and on its way out.
you could write to the TLP exporter.
the information that it's catching from, from Java.
It's a pretty disgusting, too, but that would work.
Trask Stalnaker 00:20:29 So, Antoine, just a little bit of background here, Steve, Zimi, and Huxing are from Alibaba.
And they have their own distro of the Java agent that their customers use.
So this is… they're… they're not, like, trying to, you know, bespoke make a solution. They're trying… trying to bake something into the distro that all their customers, all the Alibaba customers use.
Antoine Toulme 00:21:00 Well, so, to ask a question to you here is… would be.
In the case of a crash, meaning that somehow there's an irreparable harm being made to the JVM, if memory is breached.
It no longer can run.
How do you want the exporter to behave, such that it can actually get all the… The latest tidbits of information all the way to the end before it exits, right?
So….
Trask Stalnaker 00:21:24 So, that's not what they're, … so, when… what they're saying is, when the JVM crashes.
It will spin up another… process that… and that other process can then… send the, crash… the JVM crash dump, it'll… they'll have access to the JVM crash dump, and they can then send it somewhere.
Antoine Toulme 00:21:52 Nice.
If you do it this way, I have a script that's called, Standard In Hotel.
Which is, as dumb as it looks, takes a few environment variables. One of them is a CLP endpoint.
And, you can… you can fetch in data.
And he will send it to a GLD.
Is that what you want?
That could be a fix.
But you're still winning the best group.
Trask Stalnaker 00:22:21 I mean, it sounds like they have this all working. They're just… the only point in contention here is they want to upstream something, into… the upstream OpenTelemetry Java agent, and so I'm trying to understand why, why the parent class loader is relevant to this So now this….
Steve Rao 00:22:48 ….
Trask Stalnaker 00:22:48 discussion.
Steve Rao 00:22:50 Okay, yeah, maybe I can, explain more about this. Yeah, because, we, collection, tooling class, they are, they are in, in the directory, they are loaded by agent class loader.
Something like….
Trask Stalnaker 00:23:14 That's because here… because you're passing your… when you're running your crash data collector, your class path is the Java agent itself.
Steve Rao 00:23:25 Yeah.
Trask Stalnaker 00:23:26 We… Why?
Steve Rao 00:23:29 Hmm.
Trask Stalnaker 00:23:29 That's the part that I don't underst… if you do this.
Isn't it just gonna load the crash data collector in the standard system class loader?
Yeah. Why is the agent class loader?
Steve Rao 00:23:45 This is the class that we, put it in the directory. They are loaded by Bootstrap Class Loader.
Trask Stalnaker 00:23:52 And, … System class loader.
Steve Rao 00:23:56 Yeah, in this class, they will use some class, from agent class loader.
in Java Agent.
Trask Stalnaker 00:24:05 Oh, you want to… from here, you're trying to… start… you're trying this… separate process, you want to restart up the agent class loader so that you can access things that are in there?
Steve Rao 00:24:20 Yeah, yeah. Yeah, as we know….
Trask Stalnaker 00:24:23 Is there a lot? Oh.
Steve Rao 00:24:25 as we know, yeah, we usually, use some extension to, collect the data to the backend, something like a trace, exporter, or log, exporter, or something like that. We also achieve, exporter, Yeah, expose, crash log to our backend. They are loaded by, Agent Class Loader. So, in class data collector, it will use some class from agent class loader, so we want to, use agent class loader to load related class and, invoke related class to achieve this goal.
Trask Stalnaker 00:25:08 I see, because you're also using those same… that same, whatever, communication mechanism to your backend.
In your extension.
So why… why can't you just copy those classes that you need? So, copy all the classes that are needed by this?
into….
Steve Rao 00:25:29 Ew.
What's job, assistant class loader, you mean?
Trask Stalnaker 00:25:35 Yeah.
Steve Rao 00:25:37 Yeah, we've… we found that maybe….
Trask Stalnaker 00:25:41 That would pollute the… I guess that would pollute it for the Java agent also.
Yeah, that's not good. Okay, I understand now. I understand now the connection.
Steve Rao 00:25:53 ….
Trask Stalnaker 00:25:55 I think it's fine, so you want to use… basically, you want to use the agent class loader.
in order to be able to reuse the INST The inst classes, class data stuff.
… Yeah, I mean, I don't… I… yes, … I… makes sense to me. It's a very simple, small change, right?
Steve Rao 00:26:24 Yeah.
Trask Stalnaker 00:26:24 having that. Okay.
Yeah.
Steve Rao 00:26:28 Send up, send a PR.
Trask Stalnaker 00:26:30 Yeah, yeah, send a PR, now that I… yeah, that helped. I'm glad we had this discussion here, though, because I was not going to… figure that out on the, on the PR. Thank you.
Steve Rao 00:26:43 Okay, Augie, thank you.
Trask Stalnaker 00:26:52 Zooming… filter out some high-frequency but unimportant Redis fans. Oh!
Which ones are these? Oops, why am I logged into the wrong account?
Ping and hello.
Ziming Liu 00:27:18 Hey, Jask.
Don't have enough sleep. Hey!
Trask Stalnaker 00:27:21 Yeah, good to see you.
… Have you tried with… … sampling….
Ziming Liu 00:27:34 … … actually, I have tried, but … I think the ping and hollow span is, … Some, somehow useless for the youth, because These spans, may not be meaningful. Usually, it is a single span, and without the… It's parent, or some other information. It's just a ping, or just a hello.
Trask Stalnaker 00:28:10 Oh, do they typically not occur within… they occur in, like, a background, like a thread pool?
I mean, like, a connection pooling… Brad.
Ziming Liu 00:28:23 Yeah….
Trask Stalnaker 00:28:28 Do they typically have a parent span?
Ziming Liu 00:28:31 No, they typically don't have a parent span, they're just a… it's just a single, single span.
And… yeah.
I think it is, a con job, something like a con job.
Trask Stalnaker 00:28:48 that Redis is just, like, testing that the connection is alive.
Ziming Liu 00:28:52 Yes, yes, yes. And, actually, it occurs frequently and generates, so many spans, even more than the spend, like, get all set in the radius, … Sometimes makes use, confusing.
Trask Stalnaker 00:29:18 Do we… when… do we have any of these in our tests, or… do they show up in our tests?
Ziming Liu 00:29:28 … The test, I think the test in OpenTelemetry, Java Instrumentation, Try to verify, if the hello or the all spam occurs.
Trask Stalnaker 00:29:52 Let's see, like, … So, do you know which particular driver, Redisin, Jettis, or Lettuce?
Let me… Sure. Let me….
Ziming Liu 00:30:05 Take a look.
Trask Stalnaker 00:30:10 Oh, look at this! Ha! In our tests, we disable connection ping.
Ziming Liu 00:30:16 Yeah, yes, yes.
Trask Stalnaker 00:30:17 That's why they don't show up in our tests. Okay.
Okay.
What are the… so, I understand the… that's where the ping ones come from.
Do you know where the hello ones come from?
Ziming Liu 00:30:39 I… Me… Have to take a look.
Trask Stalnaker 00:31:02 So that was… I found that in reticent.
Looking to see if there's something similar in lettuce.
And we've also got, of course, Jettis.
Because I… the reason why I'm asking is, … We can definitely consider disabling these by default.
But I think it would help… if we could… if we had them in our TA, if we could see in our tests where… They're coming from… Yes, I….
Ziming Liu 00:32:25 I don't find the end test to verify the hello command, actually.
Maybe you could try to add a test?
Trask Stalnaker 00:32:36 That shows the hello and ping.
Ziming Liu 00:32:40 Yes, maybe it is related to the version of the Redis… Redis client. Yes.
Trask Stalnaker 00:32:48 Yeah.
Yeah, why don't you start there, if you can add a test showing the… showing their capture… And that'll help us to make a decision if we can… Or should.
… The other thing, We might want to… Go to, … If we're going to not capture it by default, especially… we should probably… Ask in semantic conventions.
… The other option is we could have a setting in the Java agent to disable them.
But we would still want to have a test for that anyway, so I think the test is a good place to start.
Ziming Liu 00:33:51 Yes, I think, have, settings is a better solution. Something like the, the UIL exclusion in the HTTP server instrumentation, something like that. We can… We can….
Trask Stalnaker 00:34:08 Exclusion in HTTP?
Ziming Liu 00:34:13 URL, exclusion, I think.
Trask Stalnaker 00:34:17 Oh.
Ziming Liu 00:34:18 Our agent today is a UI exclusion.
Something like that.
Trask Stalnaker 00:34:22 I don't think we have that. People want that, but we've told them instead to use the rule-based sampler.
Ziming Liu 00:34:30 Oh, yeah.
Rule-based sampler.
Trask Stalnaker 00:34:35 So you're probably thinking, … Top… most popular issue, this is how I always find it, sort by most thumbs ups, and it's closed now.
But exclude URLs from tracing.
So what we eventually resolved it with was, the rule-based… We have an extension in contribib now.
Samplers… And it supports declarative config now, which is cool, so you can add Like, rules now to the samplers to drop certain patterns.
Ziming Liu 00:35:28 Okay.
I see, I see.
Trask Stalnaker 00:35:32 Which is the other option… At a distro level that you could maybe do today.
Which is to add that … Filter these out via a sampler.
Ziming Liu 00:35:48 Okay. So, in conclusion, there are two ways to solve the problem. First is to, two… Disable the pin and hello by default, and change the same conventions.
The second is to add… provide the customer settings in the Java agent to let the users filter them, and add the related test.
Trask Stalnaker 00:36:15 Is that correct? Yeah. Yeah, and I would say 3 would be… I mean, you said you tried the sampler.
… They can't believe… You tried to sample it out?
Ziming Liu 00:36:29 Yeah, sample it out… it is. Yes, I can try to sample it out as well. This is the third solution.
Trask Stalnaker 00:36:42 And while we're going through all possible solutions, the fourth solution would be to filter it out in your exporter.
Like, have a delegating exporter.
Ziming Liu 00:36:53 Yes.
Trask Stalnaker 00:36:54 Right, right.
… But if they are annoying and useless, then, you know, the easier we make it for other people also is good.
Ziming Liu 00:37:05 Okay.
I prefer to do it in the Java agent, because, to start a lot of them, it, has, has some overhead to, to, to use this program, so just, … Right.
filter in the Java agent is better, I think.
Trask Stalnaker 00:37:29 Yeah, the sampler would… would stop it from getting created in the first place.
Ziming Liu 00:37:35 Yeah.
Trask Stalnaker 00:37:37 … But yeah, sounds good.
Ziming Liu 00:37:43 Yes, and … Steve is working on the proxy agent, so we may need some extensions for the, for the, in the Java agent, and, who I have, … I have, … I need to customize the… trace provider deeply, and actually, I… I need to customize the, spam builder, spam builder, and actually.
And currently.
the agent provides the install OpenTelemetry SDK method, and, which uses, auto-config… configured OpenTelemetry SDK Builder. But the auto-configure OpenTelemetry SDK Builder can only customize the Sampler, spam processor, and clock, and etc.
And, what I need to do is to… customize the, the whole trace provider, and to let it, generate, the span, rather than SDK spend, we may generate some spend that, only used in our commercial versions, so we need to customize the spam builder of the trace provider, and currently we're.
Trask Stalnaker 00:39:22 Oh, you mean so that it affects, also, if your customers are using the API directly?
Ziming Liu 00:39:34 … Yes, yes, yes, actually. If they use the API, they will use the trace provider that the Java agent provided.
Trask Stalnaker 00:39:49 Okay, so it's not for… because generally for the internal stuff, you are the… … Pieces that are part of your distro.
Are the new customizations, like the instrument or builder customizations, enough?
Ziming Liu 00:40:09 ….
Trask Stalnaker 00:40:10 Or you also need more… You need… do you need this also for distro-specific… for distro instrumentations?
Ziming Liu 00:40:20 I think this show… I think the upstream may also need the extensions to let the users customize their trace provider more deeply.
Because we can only add the spam processor and set the ID generator currently. We can do… do some other operations.
or customization to the Chase provider, or meter providers.
Trask Stalnaker 00:41:02 Yeah… So it sounds like… so… There's no hook here for Tracer provider… odd… Tracer Provider Customizer… Is this a final class?
Let's see… Yes, it is, DRAT. Because it allows you to customize… … the builder… But that just means adding in more… calling it. If it was not final, you could subclass it, and then you could have the builder, you could override the build method.
Ziming Liu 00:42:08 you know, I think, we need something like the… global open telemetry SDK DOS set trace provider, something like that.
Trask Stalnaker 00:42:26 Yeah, I just… I think it has to… I'm trying to think… the… We use the auto-configure for setting everything up.
And so, like, that's why I'm coming over to this auto-configure and feeling like maybe it needs to be… a… Tracy.
Ziming Liu 00:42:50 Custom.
Trask Stalnaker 00:42:53 optimizer… Yeah, so this… it says you can customize the tracer provider, but really you're just customizing the builder.
What's the specific use case,
Ziming Liu 00:43:11 Maybe we… I'm just asking and.
Trask Stalnaker 00:43:14 In case we can get more creative and find a different way to address the… use case besides… Tracer provider.
Ziming Liu 00:43:25 Yes, because we… hmm… We have done some, overhead optimization for the span, because, actually, the agent uses the SDK span.
in the, default trace provider. And the SDK span, when the SDK span, invoked the set attributes, set attributes method, we found that the overhead is, is high, and so we just, override the SDK span, we… we… we write, something like, Alibaba SDK Span, and, overwrite the set attributes method to, let the overhead, to, to, to, to, to minimize the overhead. So, we need the tracer to… generate… Alibaba SDK span, rather than the default SDK span, when the tracer invoked the start span, method.
So, we need to customize the entire trace provider.
Trask Stalnaker 00:44:47 And, is it… is that optimization not able to be upstreamed?
Ziming Liu 00:44:56 I think it is, hard to upstream, because We have our own, metrics… Same… semantic convention.
It is not the same as the upstream open telemetry, same con.
So, … So, it is hard to be upstream.
I think so.
Trask Stalnaker 00:45:26 How… what does the metric semantic conventions have to do with the attribute optimization? Are you flattening out attributes, like, instead of storing them in a map?
Ziming Liu 00:45:38 Storing them in a struct? Yes, yes. I have done the flattening… I have flattened out these attributes, and it contains… it only contains, the fixed attributes for… only for Alibaba use.
Trask Stalnaker 00:45:59 I see.
So, Antoine, you still there?
Antoine Toulme 00:46:08 I am.
Trask Stalnaker 00:46:10 This is an interesting from the, Weaver, so what they're doing is they're… optimizing the SDK, they've kind of have their own… some of their own SDK stuff, components, to… in order to flatten out Like, the bag of attributes is not very performant, versus, like, if you know what attributes you're gonna store for, like, an HTTP span, you can just create a struct for that.
And I recall that, Laurent… one of his… long-term motivations for Weaver was to be able to generate That kind of thing, that… those kinds of… performant SDK, span, attribute, structs.
Antoine Toulme 00:47:12 Okay.
I don't know what they are.
On that at all.
Trask Stalnaker 00:47:20 I think it's like a… late, like, it's an eventual, so… Later.
thing, but… I'm trying to think.
I'll….
Antoine Toulme 00:47:34 You can do it, you can do it today, because you can generate there's a semantic convention for what goes into an HTTP request attribute, right?
Trask Stalnaker 00:47:43 Yeah… But how would we hook it into the existing, like, existing SDKs would need… there'd need to be new hooks in the SDKs for that to be aware of?
Antoine Toulme 00:47:56 I mean… I mean, the thing is, you could generate the structure for that in some sense, right? Such as that Create a builder for it or something, and then the structure itself is either an internal….
Ziming Liu 00:48:10 And you create those convenience builders that are just there for that.
Antoine Toulme 00:48:14 And then you create a reader for those builders, like, you know.
You can, you can, you know, … what's do that?
You can interstate the data to see which popular version of the Baggage you're going to have, and the attributes, and the bids that you can cast, that you can… Getting, you know, parse the… The bag using the pre-made pass. So it's mostly going through utilities, you're going to be dancing around the problem.
Trask Stalnaker 00:48:47 Yeah, but there needs to be a, API, like, so you have your tracer, and you, you know, start, span… For a span builder, you need to somehow tell it… Which trucked… To use to store the attributes. What's your optimized struct?
Antoine Toulme 00:49:11 Well, it could be… it could be a start HTTP request term.
You know, with name, and then after this one, two, and three, as determined by Weaver.
Good luck with you.
Trask Stalnaker 00:49:24 Yeah, so that would be, like, the outer layer would be, like, a start HS piece, and… … But It would still… ideally, it would still reuse the… Like, tracers and stuff, like, unless… it rebuilds the whole SDK, and then… so the tracer… when you're… I guess when you have your span builder, I thought there would be….
Antoine Toulme 00:49:55 Get some synthetic sugar on top of it Yeah.
Trask Stalnaker 00:50:00 I… definitely, the… but the syntactic sugar is the easy… easy part, like… the….
Antoine Toulme 00:50:07 Oh.
Trask Stalnaker 00:50:08 The part that I don't… Easier. Mara and do we… Get that, inject that.
struct into the SDK, because the syntactic sugar, then, what does it call? It calls span builder… And it says, use this attribute struct.
maybe….
Antoine Toulme 00:50:36 Sure.
Trask Stalnaker 00:50:37 HTTP span….
Antoine Toulme 00:50:39 We have a library somewhere to generate Java code from well-known attribute sets of Java, of the semantic conventions.
Right?
Trask Stalnaker 00:50:47 Yeah.
Antoine Toulme 00:50:49 And then you have just a little bit of generated code that lives on top of your existing layer of API that calls out to those well-known attributes.
trucks?
And that creates the easy part, like you said, the synthetic sugar.
And so, pretty much, when you start the span, you have the ability to pass a concrete structure with everything there is to know about this.
It can hardly, given that the Java SDK has its propensity of moving builders all over the place, so… You could make a builder API for that?
Right?
Start efficiency request down.
We use a builder… of attributes, but instead of attributes oft, it's going to be HTTP request attributes, and it's opinionated about what attributes it means.
Very good.
Is there a problem with that approach? I mean, I'm just making that up as a little bit.
Trask Stalnaker 00:51:43 Yeah, I think it's good, … zooming your… You all, though, you still want A way for your particular optimization, you want just one struct… One attributes class… And you still need a way to kind of set it as the default.
1… Oh, Is that Tracer… I guess it could be on… Tracer… Provider… That's… let's say extension.
Because, well, it will take some time to get this into the, spec, but if you could… Set attribute struct.
On that, and then that could propagate down I'm just… I'm trying to kind of frame… the reason I'm bringing this Weaver conversation into this is trying to see how we could… Do this in a way that will… Help these other goals, also?
And be kind of a long-term strategy instead of just a one-off fix for you. Sure.
Antoine Toulme 00:53:21 Trust your story about this summer?
Trask Stalnaker 00:53:26 Is there what?
Antoine Toulme 00:53:27 Is there a story about everything we just talked about? Like, is there… Is Laurent from… On the Weaver side, working on that?
Trask Stalnaker 00:53:36 No, I don't think actively. It has something he has… Talked about before.
I will have to… I'd have to look and see, or just ask him and see if it's in any of the Weaver roadmap.
stuff. Actually, they have a pretty decent roadmap, we can… Just go look. Roadmap… Oh, I thought they had a roadmap. Roadmap.
Roadmap. Oh, yes.
Github project.
Right.
… Optimized SDK? … No.
Probably something I will just have to, … King… Laura, about… … But… We could… so you need a tracer provider in the… So there's this… If in the builder.
Oh, let's go to the public. This is the… Is this, … Let's go to the Auto Configuration Customizer.
Antoine Toulme 00:55:12 I mean, now you make me think I should go and build this.
Trask Stalnaker 00:55:16 That would be awesome.
Antoine Toulme 00:55:18 In fact, that's not very difficult, is it? Because you already have some declining schemas in there.
Trask Stalnaker 00:55:23 What's that?
Antoine Toulme 00:55:24 So you… You already have the semantic prevention schema, you could include it into a WIVA resource.
Put some ginger sauce together.
generate some data code that is just semantic convention version 127 of whatever.
Here is the attributes for initiative request.
And then we can argue about the format of the API, but the hard part is what exactly? Just finding the Jinja found and the… the right implication of technology so that we can generate the Java.
Trask Stalnaker 00:55:54 Oh yeah, this is… this is all along… I mean, this was… I don't….
Ziming Liu 00:55:59 This is….
Antoine Toulme 00:56:01 New groups.
Trask Stalnaker 00:56:01 strategy.
Antoine Toulme 00:56:03 It was, something I can do tonight, if you're interested.
No, that… I'm just trying to understand, are you trying to… Overpoint is a strategic approach that is shared by the jealousy.
Or are we trying to just be able to test out this capability so we can check?
whether it's taking the bill or not, because I think Weaver needs a lot of you to actually Sustaining tools in the sport.
It's too vague of a tool. You can do anything.
Trask Stalnaker 00:56:30 We can do not.
Antoine Toulme 00:56:31 Yeah, right.
So… I was wondering what's your ultimate aim here? Are you trying to prove the technology, or are you trying to prove the approach, or…?
… I don't know, I'm over here.
Trask Stalnaker 00:56:45 I'm trying to, address Alibaba's need… ….
Antoine Toulme 00:56:52 Oh my goodness.
Trask Stalnaker 00:56:53 To… they have kind of a specific optimization they want, and so trying to think what's the most open telemetry potentially… OpenTelemetry Blessed Path for that.
We would have to definitely make it all experimental stuff.
To start with, because you, you know the spec cycle.
But at least if we could come up with something that felt good, the… then I could….
Antoine Toulme 00:57:35 That would certainly put into a lot of perspective what's in the stake, because it actually would become very salient as a….
Trask Stalnaker 00:57:46 … So the auto-configuration… Customizer… Okay, so you have… SDK Tracer Provider Builder.
Do we have an extension for this? I forget.
We may not, and it's probably final.
Maybe we need… I wonder if this whole auto… Yeah, I'm not sure… I guess, and we're running out of time, but zooming… what I would… look at is… look at options. Maybe you could come up with some options for how that could work in the auto-configuration customizer… Fdk Builder… to… what kind of API would we need to add here?
And… there's… I would… look at two different options. One is… like, exactly what you're asking for here, which is, you know, how can I swap in my own tracer provider and basically rebuild the whole chain?
Ziming Liu 00:59:14 Yeah.
Trask Stalnaker 00:59:15 But I would also look at… What would it look like to… Provide this kind of attribute struct.
class?
as a… first class.
idea?
Because that's definitely, like, we could benefit from that in the Java agent. Like, our HTTP instrumentation.
would benefit right away from being able to have, like, HTTP struct Behind that, for those attributes.
Ziming Liu 00:59:55 Yeah, I got it.
So, you mean, later we can customize the data structure for the attributes in the auto-configured OpenTeametry SDK Builder?
So… so we can customize the… so we can, use that extension to do something like threatened attributes or something else.
Trask Stalnaker 01:00:31 Yeah, I think, you know, we would… need, like, a span builder, like, for the Java agent, for the upstream, we would want On each span builder, to be able to have a different attribute struct.
… But for you, you would kind of… you kind of want to set, like, a global default attribute struct on the tracer provider.
Ziming Liu 01:01:03 Yeah… Yes.
Trask Stalnaker 01:01:07 And I know that's all very, very vague and hand-wavy.
… So… We can definitely chat some more, if you want to ping me on, Slack, if you've got some thoughts, and we can… I can also, … ask in… let me add this to tomorrow's agenda, for the US folks, and I can… See if there's any thoughts, opinions… Yeah, that's actually a good, … Maybe somebody will have some thoughts. Unfortunately, Jack is out on, paternity leave for a while longer, so it's hard to make too many decisions, design decisions in the, core SDK repo.
Steve Rao 01:02:33 Okay.
Ziming Liu 01:02:35 I think we can, trace the issue on the GitHub, trace the extension issue.
Trask Stalnaker 01:02:46 Sounds good. Oh, last thing to share real quick, I'll share with you in our… Distro… And last PR to get merged… was thanks to Steve, thanks to your, Instrumenter Builder Customization.
I added that in our distro, and got rid of… we've forever had this, copy of the instrumenter Builder that we, have one line of… have to add one line of code to.
Okay. And now, don't need that anymore.
Cure.
Alright, bye y'all.
Huxing Zhang 01:03:36 Line.
Ziming Liu 01:03:38 Bye.
