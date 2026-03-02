SIG: Java SIG
Date: 2025-11-13
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/ZYN_tTmVoW7cIJA8-fmkORAOmEePAIsYUFZ04b0nludCisM4c2ffOCx7mjnhb504.46phYo7EZyWPWg_m
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:01:11 Hey, folks!
John Watson 00:01:14 underneath.
GZ Gregor Zeitlinger 00:02:27 Hello!
Trask Stalnaker 00:02:30 Hey, hey!
Alright, let's… Kick.
Get off. We've got instrumentation and contribib releases due, this week. Might, might slip until, Monday.
Tuesday next week. I know we were hoping to get Potentially a declarative config, PR in…
Anything else that… People would like in the release.
And Tyler, you had requested the servlet.
GZ Gregor Zeitlinger 00:03:45 I'll add it to the milestone.
I think it's already… Well reviewed.
Trask Stalnaker 00:03:57 the… Servlet… filter.
GZ Gregor Zeitlinger 00:04:00 Yep. Right.
Trask Stalnaker 00:04:08 Cool.
GZ Gregor Zeitlinger 00:04:13 So we have, 6, PRs there right now.
Trask Stalnaker 00:04:19 Alright.
So…
Not a promise that they will make it into the release, but at least it is what we will… we will.
GZ Gregor Zeitlinger 00:04:31 Always aspirational, right?
Trask Stalnaker 00:04:33 Yes, yes.
Lauri 00:04:34 Why did you add the servlet filter there?
Trask Stalnaker 00:04:38 Cause, it was requested.
to be added.
Lauri 00:04:43 Who's the brave soul who's going to review it and rework it?
Trask Stalnaker 00:05:00 Yeah, so… shall we just kick it out now?
Tyler Benson 00:05:06 I'm happy to kind of give a quick summary of that later in the meeting. I put it on the meeting notes if we want to talk about it.
Lauri 00:05:15 I'd say it's, like, hmm… It's nowhere near ready, like,
It contains way too much copy-pasted code.
Tyler Benson 00:05:26 Okay? That was your suggestion in the last meeting, so… That's what I did. I… Apologize if I misunderstood.
Lauri 00:05:36 Like, it's a 5,000 line pull request. I think it… you also copy-pasted the test stuff like that.
That is a lot of lines of code. It requires some reworking.
Trask Stalnaker 00:05:52 Alright, well, so I did, you might have missed, Lori, I did clarify with the, the milestone that it is aspirational only, no guarantees whatsoever.
Let's look, though, at… If there are other things in the milestone…
Okay, the other ones are all approved.
So… Oh, except for… SQL commenter… Okay. I…
suspect that the, the release will probably… Lori, I'll probably make the release on Monday or Tuesday.
So we've got a day or two.
GZ Gregor Zeitlinger 00:06:53 Yeah, the, spring starter's also a big one. Jay has approved it, but Laurie has not yet.
Trask Stalnaker 00:07:05 We'll… we will see what we have ready on Monday, Tuesday, when I make the release.
Jack Shirazi.
Jack Shirazi 00:07:19 Yeah, this is a quick one. I was hoping for a non-elastic co-owner, so if anyone's interested, just ping me and I'll add you. Otherwise, next week I'll add an elastic co-owner.
Trask Stalnaker 00:07:39 Your op-amp grand, let's finish.
controllable… So how much is this, do you think this is gonna be a contribib… module…
Can we implement it in Contrib? Like, if it is, sort of, updating…
Jack Shirazi 00:08:05 The intention here is to implement an extension which does everything, and has an example which you can just configure into any Java agent, and even configure for your own backend if you support OpAMP at your backend. And you have your own protocol.
Yeah, the whole thing.
And I don't actually expect it to be a very… Complex.
contribute.
Mostly, it's fairly straightforward.
Trask Stalnaker 00:08:40 Cool. We had some interesting discussions at KubeCon about, remote configuration and op-amp. I put it on the agenda, we can chat, later.
But yeah, it'll, I think getting even anything working and prototyped and implementations will help move that discussion along at the, spec.
level.
John Watson.
John Watson 00:09:12 Yeah, so I just wanted to bring this up for discussion, and that is we have a growing Java 8 problem, and at least… I mean, the core repo, for sure, I assume it also probably propagates into the instrumentation repo in contribib.
The latest two things are, we basically don't have a image from GitHub that supports
testing, like, running Java 8 on Mac OS anymore.
So we're gonna have to disable that testing, or just… or figure out some other more complicated way, our own custom image or something to do that with.
I put in a PR to just drop testing on Java 8 on Mac, because I… I suspect nobody is running Java 8 on Mac in production anywhere. So I think it's probably safe, and we still have Linux testing and Windows testing for it.
Trask Stalnaker 00:10:05 Yeah, I don't think we even test in the instrumentation repo on macOS.
Lauri 00:10:11 John, why do you need to drop, testing Chao 8 on Mac.
John Watson 00:10:17 Because there's no image anymore to support it.
There's no image that runs any… there's no image anymore that will actually let us run them.
From GitHub.
Lauri 00:10:26 Maybe you just need to use a different flavor of the JVM. I believe Amazon Correcto is the one that supports Jow 8 on Mac.
John Watson 00:10:38 It's possible. If someone wanted to give that a try, I'd be happy to review it.
But I also think it's low value.
So… I don't know how important that is.
But basically, macOS 13 is no longer… is basically…
is essentially dead on GitHub, so we can't use that anymore, so we'd have to deploy onto something… we'd have to run on 15 as the minimum.
But I… but then we have a bigger issue, which I… I don't know if Jack, is on the call, but, Snake YAML, we're having to limit upgrades on Snake YAML. We already have limits on Makito and the Fuzz Library.
that cut off at Java 8, require Java 11 as a minimum, and I just wanted to bring it up for discussion about what the future of Java 8 and OpenTelemetry Core is going to be.
Because this is only going to get worse. It's only gonna grow. There's only gonna be more and more libraries that say, no, we're not going to support Java 8 anymore.
Trask Stalnaker 00:11:50 The testing libraries don't bother me as much.
But… Yeah, Snake YAML, any… any dependencies that we pull in at runtime, that's…
gonna suck, especially, Snake YAML, anything that's notoriously, doing, I think they've fixed some of their binding stuff, so they're not quite as CVE-heavy anymore, but… Yeah, but there… it definitely has a history of CVEs, though. Yeah.
Lauri 00:12:23 I think, currently it affects only this, sneaky YAML engine.
That's, actually, it's the safe version.
the snake YAML that has, like, all the CVEs hasn't been updated yet.
Trask Stalnaker 00:12:40 Oh, to Java 11.
Lauri 00:12:42 Yeah.
I don't even know, like, which one we are using. I think we are mostly using the engine.
John Watson 00:12:48 Yeah, we're… the engine is the one that… with the upgrade.
requires Java… Java 11.
Jack Shirazi 00:12:55 we had experience with our agent of a lot of false positives. We're still supporting Java 7 on our agent, not the distribution, but our old agent.
We had a lot of… all of the security issues are fixed, but you still get a lot of false positives, because we're on a version, you know, like with whatever, it's always a version that is included as the latest CV1.
What we had to do to make customers happy, even though there were false positives, was actually create a
second distribution, so we… we actually create a distribution which is Java 7, and a separate one which is Java 8-specific, and I think that we'd have to go with a Java 11-specific one if we started getting more false positives.
John Watson 00:13:51 I also wonder whether there's just a… whether it would be feasible
To… and this might be a… this might be a legitimate reason to go to version 2.
feasible to just say, like, we're going to… we're going to drop support for Java 8 in the core repo.
And bump the mage version and say, if you need job 8, you're going to be on the older version, and the older version of the agent that's… that's on the older version of…
the core repo I just wanted to bring it up for discussion.
Trask Stalnaker 00:14:29 For Snake YAML Engine.
John Watson 00:14:33 And we could also just say declarative config requires a minimum of Java 11.
Trask Stalnaker 00:14:40 Yeah, but what, could we support both? Like, can we support…
Potentially via reflection. I don't know what… how breaking Snake YAML…
engine was between the two versions, API-wise.
But users of Java 8 could bring the older Snake YAML engine
for example, the Java agent, we would like to be able to still use declarative config on Java 8.
John Watson 00:15:17 Yeah, I don't know… I don't even know if there are any breaking changes, I don't… I just… I know that the… the, Renovate PR
Broke.
Because it requires job 8 for… or requires Java 11 in the new version. So, I haven't done any further investigation. I just wanted to kind of just note that over the past couple months, we've started getting a bunch of these things cropping up.
Trask Stalnaker 00:15:44 The SDK doesn't have very many runtime dependencies.
Which is a good thing.
John Watson 00:15:51 That is true.
Trask Stalnaker 00:15:54 Do you know what else besides Snake YAML?
John Watson 00:15:59 I think everything else we vendor in.
Like, thinking about the queue, whatever that queue implementation was.
And St. Camel is not… I would not even say it's really… it's not… It's just declarative config.
So it's not the… not any of the other rest of the… not anything else in the… in the core repo, just declarative config requires it.
Trask Stalnaker 00:16:30 Yeah, but that's gonna be an important…
The dependency going for in the future.
GZ Gregor Zeitlinger 00:16:43 Vueconfig is also using it, just looking at the repository.
Trask Stalnaker 00:16:50 What config?
GZ Gregor Zeitlinger 00:16:52 View Config.
Trask Stalnaker 00:16:56 I don't know what that is.
John Watson 00:16:57 View… well, view config is part of… the oz.
Trask Stalnaker 00:17:00 View, metrics, views, got it.
John Watson 00:17:01 But that's still part of declarative config, though, right?
GZ Gregor Zeitlinger 00:17:06 I… it might be. I don't see it right now.
Trask Stalnaker 00:17:10 It was… it kind of had its own file-based thing, but yeah, we're… should be…
In declarative config now.
GZ Gregor Zeitlinger 00:17:23 You can use declarative config for it right now, but you can still… Use it standalone, I think.
John Watson 00:17:36 That's not a stable… that must not be a stable module, though, right?
GZ Gregor Zeitlinger 00:17:41 That's correct.
John Watson 00:17:42 Yeah, so we could drop… we could drop it. We could drop that support and just use the same people use declarative config.
Anyway, I don't know if there's any decision to be made, I just kind of wanted to bring it up, because it's definitely a growing…
A growing problem. Java 8 is getting more and more problematic.
Trask Stalnaker 00:18:04 Any thoughts from…
vendors on… I haven't looked at the numbers in a long time, but my gut feeling has been that the Java agent is
It's gonna be really hard to drop Java 8 support in the Java agent.
Peter Findeisen 00:18:26 Well, so…
According to our very limited statistics, approximately between 40% and 60% of our customers are still on Java 8.
Now.
not… all customers are the same, right? So I believe that those customers who use… still use Java 8 are relatively reluctant to switch to newer technology, like OpenTelemetry. So the statistics is a little bit skewed, because
When thinking about those customers who want to embrace open telemetry, the numbers could be quite different.
Trask Stalnaker 00:19:25 Yeah, I can… I might be able to get this number… for our… customer base.
on our OpenTelemetry distro.
Lauri 00:19:42 What was the… Projected end of life for child 8.
2030.
Was anybody doing support post that?
John Watson 00:19:55 I mean, I'm willing to bet Oracle will let you pay them forever.
Trask Stalnaker 00:20:04 Currently.
Lauri 00:20:06 I didn't actually even mean Oracle, like, I thought that maybe, like, the…
to adopt OpenJDK, or, like, how long are they going to support it?
John Watson 00:20:18 I thought that was… I thought that was already done, yeah. I think Oracle is, as far as I know, the only vendor that supports.
Lauri 00:20:23 No, no, no.
Jonathan Halliday (IBM) 00:20:24 No, but…
Lauri 00:20:25 also has ridiculous deadlines for that.
Trask Stalnaker 00:20:35 Yeah… There's just too many.
Customers.
On Java 8.
For people not to, supported.
Yeah, I think this would be an interesting, we could look at this, definitely.
If we can, you know, if the D… if we can test, basically, against both the new version of Snake YAML and the old version of Snake YAML,
Would be one path forward.
Major version bump for the SDK.
to… to limit to Java 11.
It's an option.
We would… but it would… make the Java agent… More difficult.
Because we would… Need to… Backport things, or support two paths, or…
GZ Gregor Zeitlinger 00:21:53 Also possible that, we, engaged in the Snake Gamble project.
To help support the older version.
And backport fixes.
I think the… The effort would be worth it for our customers.
John Watson 00:22:24 Well, or would it be better for us to just… write a minimal YAML parser.
GZ Gregor Zeitlinger 00:22:32 Yeah, if that is easier, then yes, yeah, right.
John Watson 00:22:38 Like, we know we don't need to support everything that YAML might support, we need to support what declarative config?
requires.
GZ Gregor Zeitlinger 00:22:47 I have not looked into Snake YAML, if it supports anchors and stuff like that, which we don't need.
Jack Shirazi 00:22:54 Just to be aware, for the backport fixes, that's the route the log for J went.
which is where you get all the false positives from, because you've got an older version that you can use that has no CVEs, but because it's an older version.
every scanner says, no, that's not good enough, and that's where you get the… that's why we've had to create a second distribution, because even though there's no CV… there's no security holes in the version we're on.
the Java 7 version, they all insist on
having the latest version, which is only Java 8 compatible, so… yeah.
Trask Stalnaker 00:23:42 Is there any other YAML parsers?
Can you use Jackson?
John Watson 00:23:49 Yeah, I was wondering about Jackson as well.
Lauri 00:23:52 I believe Jackson depends on Sneak YAML.
John Watson 00:23:55 Yeah, I think that… I think that's the case. First, the animal support.
Lauri 00:23:58 And they might even be depending on the non-engine version that has all the CVEs.
Jack Shirazi 00:24:07 Just get Copilot to write one.
John Watson 00:24:16 I mean, the basic YAML is not that complicated a format, so…
Well, it wouldn't be too terrible.
Trask Stalnaker 00:24:26 Yeah, we don't need it to be performant, it's just for reading config.
I don't know.
Okay.
So, yes, so we have a snake YAML problem. We will have to… Explore options there.
Yeah, I think these ones aren't…
Very serious problems, but this one is…
So, I think this one will have to… Figure out a path forward.
John Watson 00:24:59 Well, right now, we are… I mean…
If we want to test on Java 8, which we do.
Which means we can't upgrade JUnit.
Trask Stalnaker 00:25:10 Yeah, to me, that's okay.
I guess… I don't mind so much getting stuck on an old JUnit version.
It only… it limits our features, but it does… it's…
Not too bad from a security perspective.
I mean, certainly there's supply chain security to worry about, so it… I don't want to write that off completely.
But it's the CVEs that customers get that are super-duper annoying.
John Watson 00:25:47 there will be a point at which finding new contributors will be difficult if we're stuck on Java 8 as well.
Trask Stalnaker 00:26:03 I have a few… yeah, welcome to infrastructure land.
John Watson 00:26:08 Oh, no, I'm aware, I'm aware.
Trask Stalnaker 00:26:14 Alright, let's… Move on and chat about remote configuration.
So… There… is a spec PR…
Is it a PR? I thought it was a PR. Oh, I think it got… Stale-botted.
About OpAmp, and so this generated a lot of discussion.
Around op-amp, and how we can do remote configuration, and the… proposal that Josh Sareth
has, made is, having…
Instead of trying to… so there's kind of a different… there's the whole config, right? And we were kind of trying to figure out, how do we send the whole config over…
op-amp, the whole declarative config, or diffs of the declarative config, or… How do we…
Standardize these messages that go over declarative config.
For example, we want a rule-based sampler, like the Jaeger remote sampler. We have a rule-based sampler, we have a declarative config.
Syntax for configuring it.
What does that look like?
how do we message that? How do we send that over OpAMP? And only that, because we don't want to send
the entire… We're probably not going to support hot reloading of the entire config.
Like, there's…
all these pipeline, you know, setup things, exporters, that we probably don't want to hot reload, but definitely, like, processors.
Views, instrumentation enabled, disabled.
Probably we could go to Jack Shirazi's list of things that they want. It's probably…
Actually, let's do that.
You had a good list. Oh, there it was.
Log levels… Disabling instrumentations, disabling, yeah, traces, metrics, logs…
This is a good one where it's like, here's an instrumentation, here's sort of, like, a declarative config snippet for this… this.
And… We're not going to probably be able to…
Write that generically out to a config file, and…
Let's see, where am I going? So, Josh is proposing calling these things policies.
That… We… that are those configurations of those components.
And so, as opposed to configuration, which is the whole everything, but each component can have policies that can be applied to it.
And so we would define…
the op-amp messages in terms of policies that get sent down, so I want to apply this
Policy for the, instrumentation enablement.
And…
Right now, OpAmp is just… it's just totally generic. You just get to send messages back and forth, essentially. There's no… there's zero structure.
And… this… PR was proposing adding structure into the proto itself.
But got a lot of pushback from the op-amp folks, so this was actually defining specific proto-messages.
And I don't think that's…
going to happen, at least in the near term. I think what… So what we should do is, yeah, focus on what do these…
messages look like? What is… I think we can, in the op-amp, messages, there's, like, a…
Name or something that then we can have a structure defined.
So that's kind of what I'm looking forward to seeing, Jack, when you're… as you're building this out, is what those individual messages look like.
And, yeah, I'm just… I'm just using a simple JSON key-value protocol.
Jack Shirazi 00:31:37 So it's, the body is just… is keys, which say which of these things you want to change, and the value is what… what do you want to change it to? Or, yeah, what do you want to change it to, and that's it.
Because if you're going for a really generic solution, we'll never get there, which is why this is a very specific and very targeted solution.
for… The set of things that our customers insist must be dynamic.
Trask Stalnaker 00:32:08 And are you passing those in the config map, or in as custom messages?
Jack Shirazi 00:32:15 That is the body. The body is a JSON structure, and the key…
is… there is, you know, it supports an empty key, but we're using the elastic key, and that's one of… just the string elastic, and that's one of the things that will be configurable, because that… that means that you can specify a namespace for…
The body messages.
But, no, not the config map, it's the body.
Trask Stalnaker 00:32:46 You're using custom messages, the thing called custom message?
Jack Shirazi 00:32:50 Essentially, yeah. I mean, it's a body, it's the body of the message, so…
I'm not sure if that's called custom, can't remember.
Trask Stalnaker 00:32:58 And…
Really?
So… There's this thing, which is Custom Message.
You've got capability, type of the message, and then the data. This is the body.
But there's also this… config map thing.
Jack Shirazi 00:33:44 Yeah, we're not using the config map, no.
Trask Stalnaker 00:33:46 Okay, you're using custom message?
Jack Shirazi 00:33:48 Yeah.
Trask Stalnaker 00:33:50 Perfect.
Okay, cool. Yeah, yeah, I…
I don't know if I can volunteer to be a code owner, but I will definitely review those
PRs from the op-amp message perspective.
Because I want to see how we can help drive, sort of…
The… this story forward at the specification level.
Oh, yes, and so… so Josh's thought, if we called these things.
like, so remember I was mentioning then in the issue, like, how do we leverage declarative config
To get these mutable configs, or listen for updates.
Josh's thought…
was if we did have a… if we did call these things policies that were coming down over OpAMP,
And if we had something called a policy provider, that then instrumentations could ask for that.
And… or they could register for callbacks when one of those policies was updated.
So it's definitely… the policy would just be, you know, that.
struct.
The… the data.
Jack Shirazi 00:35:36 Yeah, I mean, that would all work, but
the question is, where does the diff happen? Because that's… that's the intensive bit.
Trying to… trying to diff… arbitrary things, where if it's…
That's… where I focused, it's very, very simple, because they're very specific things, so you can… I mean, it's a key value, so it's very easy to see what the diff is. But if you have a general YAML thing, and you want to do a diff, and you say, okay, which instrumentations have changed, and pull back on just those ones, it's a lot more complex.
Trask Stalnaker 00:36:09 Yeah, so the thing that I like about this is that it gets away from my original thought of, like, declarative config and diffing and all of that.
And it just says that a policy is one of those tiny little messages. Your message is a key-value pair.
But it might be… You know, a slightly more complex config for a rule-based sampler.
That is, here's my new config I want to apply to the rule-based sampler.
But it wouldn't be the whole declarative config thing, it would just be this one narrow policy, and each message would just contain that, and would overwrite that component's…
The component would apply that policy.
Jack Shirazi 00:36:58 Yeah, I looked at that for the methods instrumentation, and it was doable. I mean, there's a different reason why it won't work, but that part of it is pretty doable.
And just saying, okay, this is the new config for the methods instrumentation, and here's the old one, here's the new one. You can actually parse them both, since it's already got the parser in there in the instrumentation, and then do a comparison after the parsing. So that… that… that bit works fine.
GZ Gregor Zeitlinger 00:37:29 Or you could, basically say that the policy provider is saying that this part of the YAML tree is dynamic.
Because in the methods instrumentation, you also have a YAML node, and all that part below is dynamic.
Not sure if that's better, but just thinking about it.
Trask Stalnaker 00:37:54 So, yeah, so I think what Josh is proposing there is that the, the policy would, be…
Like, the structure would be the same there, but it wouldn't be trying to…
Like, the declarative config would probably match
But it's… it's just… it's kind of its own concept there that represents the policy of the component that then
Yeah, just trying to get away from the declarative config, which has so much things, and worrying about diffing, and just focusing on these narrow… defining these narrow policies.
I don't… I'm not sure it's gonna make sense until we… Try it out.
Jack Shirazi 00:38:47 I mean, Gregor's suggestion's quite a good one of just…
Defining some aspect, some part that, like, the… near the leaf can be mutable, and you have to explicitly state that, and then the config provider has to support that.
And that…
That kind of… that means that it would have to provide an API to change those values and only those values.
And that… that kind of works nicely.
Or a lot better than… a lot better than a generic op… generic solution.
GZ Gregor Zeitlinger 00:39:21 I'm thinking about it from the way that the SDK is working. In the SDK, you basically
take a node of YAML, and you give it to a thing, I think it's called Factory.
And if it's dynamic, then you would have, like, a dynamic factory that would not only have a create, but also an update method.
Trask Stalnaker 00:39:48 And so, would instrumentations Would we have, would instrumentationists be able to register, like, callback?
Listeners…
Jack Shirazi 00:39:59 Yeah, that's straightforward to do.
GZ Gregor Zeitlinger 00:40:04 Yeah, I think the answer is yes.
Trask Stalnaker 00:40:08 Or… updates to… Ayyyy… specific,
I like it. Is this something that, Jack, you had looked some at the existing
How… whether this was implementable,
Experimentally, at this point, without having to change things.
Jack Shirazi 00:40:50 Yeah, so technically, I can create a mutable config provider and…
have that loaded, but the problem is that the… all of the instrumentation is asking whether it's a declarative or a non-declarative config, and if it's declarative, it assumes it's… the full declarative config is available at initialization.
And you don't have that available for a random config provider that you've implemented, so it doesn't work.
To just provide a config provider that's mutable, you'd have to have
the declarative config 2 for that.
So it doesn't work as a…
Just to implement that and pass it in and say, okay, this node is available.
Because it's inspecting all the other nodes, and anything… every instrumentation that we've… we've…
made declarative config capable, the first thing it does is checks whether it's declarative config or not, because if it isn't, it goes back to the old one.
So if you… if you… and the… and that method is saying, if I've got a config provider, then I'm using declarative config. So if I provide a config provider, everything says, okay, I'm using declarative config, let's… let's use that.
But I don't have declarative config available to my provider, so it doesn't work.
GZ Gregor Zeitlinger 00:42:14 Right, I think, if you're only trying to implement it in the agent repository, then it's going to be hard. And Jack Burke's plan was to add it, to add
OpEng support and the SDK repository, and I think that's when you will be able to fix those problems.
Jack Shirazi 00:42:36 Yeah, this… I mean… It was… this was generic. This is… this is a generic problem because…
The way we're defining whether something is…
Where the declarative config is available is if there is a config provider.
Which means that you can't provide… you can't create your own config provider which doesn't have the full declarative config.
specified.
Trask Stalnaker 00:43:05 So, Gregor and I were just discussing… Oh, go ahead.
GZ Gregor Zeitlinger 00:43:10 You can, actually. The Java agent is also swapping out the config provider for something else, or the config properties, one or the other, but you are able to
To provide your own thing.
Jack Shirazi 00:43:25 Yeah, technically, that's not a problem. Technically, I can stick in my own config provider, stick it on the class path, and it picks it up, but then every instrumentation is expecting declarative config to be available for it.
GZ Gregor Zeitlinger 00:43:39 Oh, okay, got it.
Jack Shirazi 00:43:40 Yeah, get it? Yeah, okay, so it's the config that's the… that's the problem, not the config provider.
GZ Gregor Zeitlinger 00:43:46 Hmm.
Trask Stalnaker 00:43:49 Gregor and I were just discussing, previously the, potentially
Taking the system properties and, for people who aren't using declarative config, and creating a fake declarative config for them.
So that there's… there is always a declarative config?
And we can… we could then… Update instrumentations to… Only read from declarative config?
I don't know if that helps this situation or not.
Jack Shirazi 00:44:23 I mean, that would work, but I don't think you're gonna do that. I don't think it's doable.
GZ Gregor Zeitlinger 00:44:30 You mean because it's too much code to change?
Jack Shirazi 00:44:33 Not just that, but that means you have to know every single instrumentation's, dependence, every config that every instrumentation requires.
Robert Niedziela 00:44:45 We actually have… sorry.
Jack Shirazi 00:44:47 Go on.
Robert Niedziela 00:44:48 Yeah, actually, we have the implementation in reverse order. I mean, we have fake declarative config based on environment variables built on top of the declarative config, right? So…
Now we are going to implement it yet in the reverse direction, then?
So it, it may be…
GZ Gregor Zeitlinger 00:45:10 That's… that's basically the idea, yeah.
So, as a first step, it was easier to, build the bridge in a way so that instrumentations are… don't have to be changed.
to unlock declarative configuration, and now what Trask is suggesting is that now that we have a little bit more time, we can actually update our… all of our implement… instrumentations.
In a pretty automated way, basically saying, whenever you have a dot, create a new method called getStructured, and…
Using Copilot, you can probably do this in a quite automated way.
And once you have done that, then it looks as though all users would use declarative configuration.
Even though you are providing them a bridge that translates the system properties into this virtual declarative configuration.
So that users don't have to upgrade yet.
Jack Shirazi 00:46:15 You do it, I'll use it.
Trask Stalnaker 00:46:20 Give us some time.
GZ Gregor Zeitlinger 00:46:21 That's actually true.
Trask Stalnaker 00:46:22 We're chatting about this the hour before this, and we're…
Know that it's, something to hit our heads against, but… would be better.
GZ Gregor Zeitlinger 00:46:32 I'm actually looking forward to get my head smashed next week for that, so we can collaborate.
Trask Stalnaker 00:46:41 Love it.
Robert Niedziela 00:46:45 One more question, but the clarity config, do you plan to leave the clarity config bridge in place? I mean, the bridge we have now, will it remain, or you are going to clean it up?
GZ Gregor Zeitlinger 00:46:58 It would eventually get removed, deprecated first, and then removed later, but this is,
Several months, from now.
Robert Niedziela 00:47:07 Okay. I'm asking because some, custom, codes
already may use it. Actually, I'm using… The, the.
Trask Stalnaker 00:47:17 I suspect that we… we may not be able to remove it until 3-0.
because we… there's some upgrade… we can't break 2X people who are using
Who have extensions, who rely on… I don't know. There's some hard problems still to figure out.
Robert Niedziela 00:47:39 Okay.
Trask Stalnaker 00:47:47 Yeah, so, Jack, if you don't, yeah, definitely… oops, not that one, but for your,
Yeah, if nobody volunteers, yeah, just get, Elastic, somebody else from Elastic, so that at least we have somebody to review, but I will review from the,
from the op-amp messaging perspective.
I wanted to bring this up, just… I know we continue to get New instrumentations contributed.
to the, Java agent.
And…
It's fine, but it's also, like, if we, you know, as… it would be also okay if we wanted to set some more limits, some limits on that,
I don't know what, basically deferring to Laurie and Jay here, who do most of… those,
Hard reviews today.
Already.
Jay DeLuca 00:49:16 Do we want to… Limit to instrumentations that
implement semantic conventions. Like, there's been discussions about the stability
stuff, but I don't know if that's one particular vector to…
incorporate. I know we have a lot that we…
we'll just put behind an experimental flag, but I do wonder how many people are actually using
A lot of those, as opposed to just, like, one company kind of contributing it and then using it.
Trask Stalnaker 00:49:54 Yeah, I mean, so we can really…
Define whatever we want, whatever we think is manageable.
There's a Y… we are the, a lot of the language repos are more…
Strict, and basically…
Tell people to go and implement, the instrumentation, contribute the instrumentation to the library itself, for example, or…
Even host it themselves.
We…
could push… we have pushed some things to the Contrib repo, but even the contrib repo, I mean, we can sort of…
We have the option to define the scope that we want.
It's a never-ending tale, right? Like, it's not scalable forever.
So, just wanted to… I don't…
I wanted to get, sort of, feedback from how… People feel about…
The amount of work that goes into, Bringing in those new instrumentations.
Jack Shirazi 00:51:13 Is the reason here workload?
Trask Stalnaker 00:51:18 Yeah.
Jack Shirazi 00:51:20 So is there any reason why you can't just tell a contributor, this will take a long time to get reviewed because of the current workload?
And put it in a backlog.
GZ Gregor Zeitlinger 00:51:32 But it's not just getting it reviewed, it's sitting there, then it has to be maintained.
Trask Stalnaker 00:51:41 Well, the workload, like, there is an amount of workload that requires, like, as, OpenTelemetry as a whole is trying to focus more on stability of the current things that we have.
Same with SEMCOM, you know, we're having some difficult decision… discussions in semantic conventions about
How can we draw the boundary around a smaller set there and federate more semantic conventions?
It doesn't mean that these things can't live somewhere, but they don't have to live in open telemetry.
And from a workload perspective, I mean, there's just always constant maintenance of what we have today.
That I… I don't think we can just necessarily say, oh, we'll get to it eventually.
But again, I haven't been… I haven't been doing… it really has been Lori and Jay who have been doing most of those
Most of that.
work.
Today, so I'm kinda… Opening the floor for them.
Lauri 00:53:00 I think most of the instrumentations are actually quite small.
And it isn't too bad.
There have been some that are, like, pretty crazy, like, there was this Komunda…
Which was some sort of business process management, I guess?
Which felt a bit too much for us to maintain.
But with the smaller ones, like guides.
It's hard to draw the line, like…
We could say that, like, we don't care about frameworks that are used only in China, but
I'm pretty sure that some of, some people would be unhappy about that kind of… Decision.
Trask Stalnaker 00:53:48 Well, we need to give people, and this is where I can help if we want to pursue this, is…
Sort of…
the messaging, and where can people be successful outside of having to land it in OpenTelemetry? How can we get it discoverable via the registry? How can we get it, how can…
People build extensions that are easily brought in, or native instrumentation.
Like, Jack has been thinking more about, you know, how people can write.
native instrumentation that interops well with the Java agent.
Things like… Dot.
Jay DeLuca 00:54:43 One other thought is around just really old stuff, like the Java 8.
conversation that we had, like, maybe it would make sense for us to start being a little bit more strict about things that are gonna require
compatibility there.
Or, like, real… instrumenting really old versions of Things in general.
But…
Trask Stalnaker 00:55:06 Or, yeah, that's a good thought for new… Instrumentations that people are contributing?
We could definitely, like, if it simplifies the instrumentation, to focus it on newer versions.
Then, that's a good option.
I think our existing instrumentations, We'll… It's…
Gonna be hard for us to drop support for old versions of things.
Cool. Well, just think on it, if you have…
I just wanted to offer my support there for, if there's anything we can…
If you have… preferences.
Jay DeLuca 00:56:06 Yeah, just one last thought, it's, is I, I am working on more extension documentation. I'm still working through some of the feedback that I got from Lori, but hopefully.
That can help with when we turn people
A way to give them better resources of how they can
package their extensions, and I hadn't considered the…
extensions as part of the registry, and I can certainly think more on that and how we can incorporate that into, like, the Explorer project.
So that if people are writing these extensions externally, they have a place where they can make them more discoverable, maybe, in some way.
Trask Stalnaker 00:56:44 Yeah, I think for the, I mean, the long-term health of the whole OpenTelemetry community,
We'll have to, you know, kind of figure out how to distribute more stuff, let people be successful outside of the OpenTelemetry GitHub org.
I think Weaver is gonna…
help with that. One of the topics with SEMCOM is
I'm gonna… is… we want to kick out… we want to basically draw… try to draw a very narrow box around what we manage in semantic conventions, like HTTP, SEMCOM, database SEMCOM, RPC SEMCOM, things like that.
But, even something like JVM semantic conventions.
I'm gonna look at how, if we can kick that out of semantic convention repo and bring it over into the Java repo, and do, you know, we can still have Weaver and still do,
When we generate our semantic convention constants, we can…
Point to multiple destinations, multiple semantic conventions, registries, so, yeah, things like that.
Cool, Taylor, sorry, we don't have… Too much time, but, what are your thoughts here?
Tyler Benson 00:58:25 Yeah, so, thanks for those that have, taken a look at this, already. I know that Lori's expressed some concerns about the size, and I wanted to just get some feedback on, way… is there any way that I can improve this? What needs to be done here?
I need to update the description, obviously, but anyway.
Yeah, so there's a lot of stuff that's copied over. I did, mostly out of…
trying to be sensitive about long-term maintenance, to keep it as similar as possible to the, the Java agent instrumentation.
And so that's why there's so much copy, copied classes.
Trask Stalnaker 00:59:24 So the tests, I mean, definitely, see if the tests are needed for… to be copied,
Because we have a lot of, like, right, we already share tests often between library and Java agent instrumentation.
And that has a lot of value, to make sure that we're writing the same tests against both.
And we're… Yes.
We often have options of, like, what feature capabilities something has, and so the test can have conditionals based on those options.
Tyler Benson 01:00:03 Sure. Yeah, I, I did,
try… I mean, I didn't try and, like, depend on the other, classes, or other packages, test package. I copied them over, but if, it would help, I can try and reduce some of that by, through dependency. The main issue there is I still had to, modify the base class in order to, inject the servlet filter.
Lauri 01:00:33 Have you looked at how we… It's, we have a common testing module.
And, we have some sort of abstract method that library tests can implement that sets up the filter, or whatever.
Trask Stalnaker 01:00:49 Have you looked at how other common tests work across both Java Agent and Library?
Because that's a pretty common, right? All of those have to deal with that, where the Java agent is automatic, and library instrumentation requires a little setup snippet.
Tyler Benson 01:01:08 Sure, okay, I can take a look at that.
Is the concern more on the test copying, or all of the other classes?
Lauri 01:01:19 So there's, there's a…
Trask Stalnaker 01:01:21 Yeah, let's start. Yeah.
The test one is the most obvious one.
Tyler Benson 01:01:27 There's a package of all of the, copied classes. All of these are copied over as well.
Trask Stalnaker 01:01:35 Yeah, it's… it's so much code, though, right? Like, let's take… let's take it slow.
Tyler Benson 01:01:40 I'm not arguing with that.
Trask Stalnaker 01:01:42 of time.
Start… start with the tests.
Work on that.
Oh, no, we ran out of time. Sorry, folks.
See you next time.
Tyler Benson 01:01:59 Good one.
Trask Stalnaker 01:02:00 I…
GZ Gregor Zeitlinger 01:02:01 See you!
Robert Niedziela 01:02:02 Pay.
