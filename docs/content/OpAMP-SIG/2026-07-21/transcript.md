SIG: OpAMP SIG
Date: 2026-07-21
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Evan Bradley** 01:32 Andy.
**Andy Keller** 01:46 Hey, how's it going?
**Evan Bradley** 01:48 Gonna write.
**Andy Keller** 01:51 get used to my, Zoom.
Keystrokes.
**Evan Bradley** 01:56 Oh, yeah.
I'm usually on Linux, and then when I go onto my laptop, which is a Mac, it always trips me up, because they're different.
**Andy Keller** 02:04 Hmm.
sees a Linux desktop.
**Evan Bradley** 02:10 Yep.
It's a product of a bygone era.
**Andy Keller** 02:20 Is that managed by Dynatrace?
**Evan Bradley** 02:22 Yeah, technically, yeah.
**Andy Keller** 02:28 It's been a fun, Migration period, but…
**Evan Bradley** 02:32 Oh, I'm sure, yeah.
Probably from a relatively simple setup to, you know, just corporate tentacles all throughout the system.
**Andy Keller** 02:40 More or less.
Hey, Tigran.
**Tigran Najaryan** 02:43 Hey, guys.
Have you guys been, acquired?
**Andy Keller** 03:02 Yes.
In April.
**Tigran Najaryan** 03:05 Oh, okay, I guess I missed that. Sorry.
**Andy Keller** 03:11 Yeah, we have…
**Tigran Najaryan** 03:12 I guess.
**Andy Keller** 03:12 Yeah, thanks.
We're still not sure half the time how to refer to ourselves.
Binplane will remain an independent product, but will also feature some site integration with San Andreas, so… FindPlane's still a thing. The website still exists.
**Tigran Najaryan** 03:34 Okay, cool.
**Andy Keller** 03:38 But we are part of Dentatrace.
**Tigran Najaryan** 03:49 Okay, let's start, Dakota, you have a few… items there.
**Dakota Paasman** 03:56 Yeah, let me go ahead… Share my screen.
Oh, cool. So the first one I'm going to talk about… So… This came out of review of one of the initial upgrade PRs. Basically, the… OpAMP, you have… Remote config, and you have package upgrades. For each of those capabilities, there's a… an accepts version of it, which means you accept a remote config, or you accept packages, and then there's a reports version of it, which is you report your remote config, or you report what package you're running.
And the PR review left was we should combine these two capabilities when configuring the supervisor, because you can right now, configure them independently.
And just from a user experience perspective, We want to just have one single capability option in the supervisor.
So, combining these to standardize on the accepts version of the config option, so if you set accepts remote config to true, then it also will set the report's remote config capability.
And the same for the packages option.
For the… for unifying the packages capabilities, that's pretty straightforward, just because the capability is not fully implemented yet, and the supervisor fails on startup with an error if you set either of those. So, removing the reports Capability is not… a problem. We can just do that. There's no working configs with that today.
However, for the remote config options, for those, we need to go through a deprecation process.
Just because… There are working configs out there with remote… with reports remote config, which is going to be the capability that we remove.
So I just wanted to describe a deprecation process that we could follow for Removing this config option, and get some… Group consensus on this before moving on with it.
So in this issue here, I've kind of laid out, like, a three-phase approach for this. The first one would be logging an error message whenever reports remote config is set, explaining that it's been deprecated, and changing accepts remote config to enable it.
If the reports option is not there.
assuming that gets, merged in by the next OTEL release, which… I think this is out of… Date now.
Or is it… was it 157 that was just released today?
I think it was. So 157 was just released today, so if this gets merged in before version 158, Then this would last for two releases until version 160, at which point we start returning an error message whenever the report's remote config option is enabled.
And then that would last for two releases until finally, in 162, we just remove that capability from the config.
That's kind of the proposed process I have here.
Yeah, Andy, you have a question?
**Andy Keller** 07:39 Yeah, I guess, It makes sense to me that if you accept Remote Config, that you would imply that you report it, because I don't think Functionally, things… Would work very well, accepting and not reporting.
I think that there's probably a use case Just like the way the OpAMP extension works, where you… are effectively read-only. You only report. You don't accept.
Certainly for packages, maybe config is less likely, because you're probably using the supervisor so that you can accept configuration.
But maybe you just want to report the package that you're using so that you can… Display that somewhere, but you don't want to allow remote upgrades?
**Tigran Najaryan** 08:33 For packages, by the way, by the way, it's a good point, Andy, for packages, it's not… bar… it's not called report.
remote packages. It's called report packages.
And I think the spec says there's a possibility to have packages installed locally.
Not as a result of accepting packages from the server, but somebody can go and manually install packages, and those will be reported.
To the server, even though the agent doesn't accept packages.
So I think for this one.
We do have use cases where accept and report Do not necessarily… Are not necessarily enabled at the same time.
For config, though, I think it does make sense to me, because I can't think of a scenario where Because it's… it clearly says report.
Remote config, right?
And if you're not accepting a remote config, what is it that you're reporting?
I… I think it doesn't make sense, then, for the config, then.
if we set aside the packages, I think you were… you wanted to do the config first, right?
I think what you're suggesting does make sense to me for the extension in particular. I'm just trying to think of… does it… Does it also make sense to… remove that concept from the spec altogether? Like, is there a scenario where… you would somehow accept a remote config, but is unable to report configs for whatever reason. I'm not sure if there is any… anything like that possible.
So you're… the first one you're doing is the config, right? So let's maybe focus on.
**Dakota Paasman** 10:31 So… Sure, yeah, so, and so this is the supervisor specifically, not necessarily the the OpAMPO library, that I'm leaving untouched.
That's me.
**Andy Keller** 10:44 get that.
**Dakota Paasman** 10:46 But… So yeah, we can talk about the remote config one first, Yeah, if we're still in agreement that we want to unify these on one, then… I guess, is this…
**Tigran Najaryan** 10:59 I think, yes. I think, in my opinion, yes, simplifying the configuration options makes sense for the… for the supervisor.
I really can't see why you would want to have Except enabled, but not reports enabled.
Like, what's the… why would we want to do that? Or the opposite.
Where accept is disabled somehow, and you report, you report what, if you don't accept.
the config from a remote source. So for these two, I think I agree with you.
Keep just one. Okay. Remove the other.
But, and this point that he was making, I think it applies to packages, in my opinion. For packages, I think it's different.
**Dakota Paasman** 11:47 Okay, so we should not do this for packages, then.
**Tigran Najaryan** 11:50 I think for packages, so… We should probably double-check, but I think the spec says… Maybe give me one second.
Somewhere… That's a command, you just need to open it.
The specs… Of course, packages.
What's that?
**Andy Keller** 12:22 And while you're looking, I think… I was sort of forgetting that we have a reports effective config, which would be the read-only case.
Yes.
**Tigran Najaryan** 12:38 Don't have those.
**Andy Keller** 12:38 Maybe there's not a case of the report's remote config.
If you don't accept it.
Because then it's not really remote, to your point.
**Tigran Najaryan** 12:48 I think so, yes, that's what I'm saying.
**Andy Keller** 12:51 Yeah.
**Tigran Najaryan** 12:53 So, if you look at the package statuses, it says… The package status message describes the status of all packages that the agent has or was offered.
And, let me see if there's a more specific warning about local packages or something like that.
It's been a while.
Let me take a look maybe offline at that piece, so we don't have to… Don't have to waste time now, but… I think for packages, there may be an actual use case where you would want one enabled and not the other.
**Evan Bradley** 13:37 So… On that point, if you don't accept packages, would it be… would it… I mean, assuming that the spec doesn't already say something about this, would it make more sense just to report those as components, if they're just locally installed packages that you're not expecting to get from the OpAMP server?
Because we've expanded the available components message to be a lot more generic now.
**Tigran Najaryan** 14:03 Hmm, maybe, I guess you could.
So you're saying eliminate that use case, the concept of locally installed packages.
being reported. Here's… here's the warning, I found it. If you go to the packages section.
There is… there is this… this piece.
**Evan Bradley** 14:46 It sounds like we should keep that then. I'm just thinking from a use case perspective, why you'd want to report I mean, the intention is that you're… that the server can offer packages, and that the agent can download them, but if these are modules that are just installed locally and aren't meant to be managed by the server, why you'd want to report them using the same mechanism that you would use for this.
**Tigran Najaryan** 15:10 It… it could be that… There is a possibility For the server to offer these packages for remote?
Downloading by the agent, but if the agent already has them, because it was… Prepackaged somehow?
Then the server would want to know and avoid offering those as a remotely downloadable package, essentially.
So, it allows having, essentially, two mechanisms for package distribution. One is… Prepackaged with the agent.
And the agent tells the server, I have them already, I don't need them anymore, or… The remote downloading is used.
And it's the same set of packages, so they are no different. If we make it reported through components, we're introducing some sort of inconsistency now, right? We're saying.
Oh, no, these are really… we're reporting them as components, but they are the same thing as the packages.
So, the server needs to be aware that oh, this is… that component is actually a package that I could offer, but I'm not going to offer, because that's the same thing.
This makes it clearer that it's actually the same thing.
**Evan Bradley** 16:26 So, I think the… maybe the thing I'm not so sure about for that use case is if… You don't have the accepts packages status enabled, why would the server need to care about whether to offer packages or not?
**Tigran Najaryan** 16:44 I mean, for the same reason, we are sending the component status information, right? That's information that probably is important.
To know about the agent, what the agent has, and packages is our… Important part of that, that, that knowledge.
**Evan Bradley** 17:02 So, okay, I think I see… yeah, it would…
**Tigran Najaryan** 17:04 We're reporting information about components.
**Evan Bradley** 17:07 Right, right.
**Tigran Najaryan** 17:07 Nothing that the server does specifically about that, it's just knowledge.
**Andy Keller** 17:11 Yeah.
**Tigran Najaryan** 17:12 Server.
**Andy Keller** 17:12 It's.
**Tigran Najaryan** 17:12 May or may not use it.
**Evan Bradley** 17:13 Sure.
**Tigran Najaryan** 17:14 Okay.
**Andy Keller** 17:15 It is needed for, like, a read-only use case.
There isn't a… there isn't a distinction, sort of, with remote packages versus effective packages, if you will, like there is with config.
There's just packages.
And so I think… That falls in the case of needing to be able to support reporting, or read-only use case, where you're just kind of Maybe you're deploying using other tooling, and you just want to monitor the status of the.
**Tigran Najaryan** 17:47 Exactly, yes.
This isn't hypothetical, we actually had a use case like that at Splunk.
Where people… there wasn't, like, we had our own remote management protocol, and there was a way that you could push packages to our agents, like our proprietary agents. But it was also possible, and it was a supported way for people to go and install those packages manually.
At the agent, at the specific location, and so… We did want to know that actually that happened, so that we… we… the server didn't offer the same package to the same agent again, right?
So it was an actual scenario that was happening with our internal agent, with our proprietary agent.
**Kelsey Ma** 18:33 So, quick question on the read-only package. Would the suggestion then be to not use the package state provider in the start settings? Because I do remember, if you want to use a package state provider, it actually requires both to be enabled, even if you just want to use it to report package status.
**Tigran Najaryan** 18:54 It's a good question, so that's… that's maybe a limitation of the Go implementation that… that shouldn't be there.
**Andy Keller** 19:02 Yeah, I would agree, I would agree.
Yeah.
**Tigran Najaryan** 19:05 Yeah.
Yeah, we should… we should decouple the… the reporting from the accepting.
more… more carefully in the Go implementation. But in the spec, at least, it clearly says you can have local packages.
So, I mean, we can decide if we want to keep that, but… I did see that in the wild, right? That there was a use case like that.
I would maybe suggest that we keep that.
for… particularly for the hotel collector implementation, we can still decide that we don't… we don't want two separate options. That's okay, right?
We can eliminate one of the options, and… Except, and it implies reports as well, but… in the spec by… in the spec, I would… I would suggest that we keep that, because we… we had an actual use case for that.
**Dakota Paasman** 20:04 Okay.
So, just to be clear, then…
**Tigran Najaryan** 20:08 For the way of how you want to handle this, in what versions, you… with the very first change, you suggest that we log an error message here, and error message means that it won't stop anymore, right?
Should it be a warning instead, so that it does start when, in the first phase of it?
**Dakota Paasman** 20:31 Is it…
**Tigran Najaryan** 20:32 intentional, you want it… you want it to be, kind of, fail at the startup when the config plug is used?
**Dakota Paasman** 20:39 For… so for the… Yeah, so for the remote config capability, Right now, yeah, it's just a soft failure. It just logs an error message, it doesn't stop the supervisor from starting. And then in the second phase, so after…
**Tigran Najaryan** 20:55 Oh, the error doesn't stop the… it doesn't… it doesn't fail the startup?
**Dakota Paasman** 20:59 Yes.
Second phase.
**Tigran Najaryan** 21:01 Okay, I see, okay.
**Dakota Paasman** 21:02 And the second.
**Tigran Najaryan** 21:03 So it's gonna…
**Dakota Paasman** 21:03 It'll fail startup.
**Tigran Najaryan** 21:05 Then, then, yeah, that's fine.
**Dakota Paasman** 21:08 Okay, cool. And then, yeah, just to be clear, the packages front, we're okay not having an opinionated approach, And the supervisor. That was one of the… Comments you left.
Originally, for why we should unify them was the supervisor should be opinionated about it, but… We're okay with it.
For packages, at least. Not.
**Tigran Najaryan** 21:34 And again, for the… specifically for hotel supervisor, I think it's okay if we want If we decide that we want just a single flag.
I'm fine with that, I don't mind that.
I'm just saying let's… let's not also unify the… the spec.
For the config, though, I would like us to consider actually eliminating the flag from the stack altogether as well.
Because I can't think of a situation where You really want to have one enabled and not the other.
They are very clearly tied together, just about the remote config. That's the naming of the capability.
**Dakota Paasman** 22:16 Sure.
Okay, then, for the supervisor, I will just… I will, I'll close the issue for the upgrades.
Unifying upgrades, and if that comes up again in the future, we can revisit it.
But it sounds like we don't want that for the upgrades flag.
**Evan Bradley** 22:39 One question about that. For… should we just autom… should we have reports package status default to on?
If you turn on Accepts Packages.
**Dakota Paasman** 22:51 If you don't specify. Yeah.
**Evan Bradley** 22:54 Or is that too complicated?
**Dakota Paasman** 22:57 I think that makes sense. It feels like that's kind of a given if you're accepting packages, that you'd also be reporting them. I mean, that is… what Kelsey brought up, where, you know, you can't use a package sinker unless they're both enabled, Which is required if you're accepting.
**Tigran Najaryan** 23:15 I probably wasn't clear, just to say one more time.
I think it's okay for us to be More strongly opinionated in the supervisor and say that… it doesn't make sense for us to have accepts packages enabled, but not report packages enabled, or vice versa, and say that there's only one configuration setting. If you enable that.
with both accept packages and also report statuses of packages. I think that's… that's totally fine for… The reason being we want it to be simpler to do the configuration.
Because we can't.
**Dakota Paasman** 23:52 Okay.
**Tigran Najaryan** 23:52 A good use case where you want to have that finer Finner granularity of settings.
I'm okay if we want to do that for the supervisor. I was just saying, let's also… let's not do the same thing in the spec, the entire spec, eliminate it as a concept from the spec. Let's keep it, because I can see other agents needing that.
**Dakota Paasman** 24:15 Yeah. Okay, yeah, that makes sense.
**Tigran Najaryan** 24:17 Our agent, for the supervisor, for Autel supervisor, I think that's okay, to just say we support just one flag. You set that one flag in the config, that results in setting both flags on the wire.
As defined by the specification.
**Dakota Paasman** 24:33 Okay, then, yeah, these issues are… Strictly about the supervisor, so then I'll.
**Tigran Najaryan** 24:40 Yeah. Keep this.
**Dakota Paasman** 24:41 Open then for the supervisor, and unify in the supervisor, not bespec.
Yeah. Okay.
**Tigran Najaryan** 24:47 And my suggestion was that for the config in particular, we can go a step farther and then say that we would like to also Remove one of the flags from the spec as well.
**Dakota Paasman** 25:00 Okay.
Sure.
**Tigran Najaryan** 25:01 We can have that discussion separately, we can open a separate issue to talk about the spec portion of it.
**Dakota Paasman** 25:07 Yeah.
Okay.
Cool. Yeah, so that is those two issues. The next issue… So… This is… This issue right now is specifically on OpAMPO, if this is… If this is something that we decide to do, changes are also needed in the supervisor and the OpAMP extension. However.
for… initially, I'm just focusing on OpAMPO to discuss this.
So, we have a use case where, Let me back up. So the OpAMP server and the OpAMP client, they both connect to each other over TCP, However, we have a use case where TCP is not, it's not allowed in this environment.
And so, alternatively to using TCP transport, we need to use Unix domain sockets as the transport layer.
So this issue is about adding support for, configuring the server and the client to connect over a Unix domain socket instead of using a port.
And this issue here is just kind of outlining.
You know, why potential changes, I'm looking to see, you know, what do we think about this, the changes are… Relatively minor.
I've got a working, setup of this with changes across OpAMPO and the supervisor and the extension. It's really just a configuration. From the user's perspective, it's a configuration change, you know, instead of configuring a server URL, you're configuring a file path for the supervisor and the collector to talk over.
You know, for the supervisor and the collector.
that deployment paradigm. It's, you know, two processes running on the same machine.
At least in Linux.
UDS is the… the preferred approach for inter-process communication.
I think it makes sense for it to be like this, or to at least have this option.
Does anyone have any initial thoughts or questions about it?
**Evan Bradley** 27:52 I have to drop, but we support, communicating over domain sockets in the collector, so I don't see any reason why we couldn't do the same thing here.
Ideally, really, we support most of the connection set… well, I guess the client's a little different, but yeah, I think this would make sense.
**Tigran Najaryan** 28:14 And there is a… there's… there won't be any concept of URL anymore, right? Or the URL is going to be ignored, I'm guessing.
When you're using it. Yeah.
**Dakota Paasman** 28:24 And this… Yeah.
**Tigran Najaryan** 28:25 Will this also work with a plain HTTP transport?
With its requesters.
It should, I'm guessing, right?
**Dakota Paasman** 28:37 I think so. I'd need to look into that part of it a bit more.
**Tigran Najaryan** 28:41 Yeah.
**Dakota Paasman** 28:43 But, yeah.
**Tigran Najaryan** 28:47 Okay.
I think I… yeah, I don't mind it. I think I would want this to be described in the spec as well.
Maybe not immediately, after the implementation is there.
After it's clear how it works, I would like to make maybe a small section in the spec as well, explaining how you could use a different transport, different, like.
underlying transport instead of TCP.
I… I don't know why not, but like… like Evan said, we do this for the collector already.
And it makes sense if you're running things locally.
No particular objections from my side, other than… We should have the prototype to demonstrate how it works, and… And also maybe make a small change in the spec to describe it.
**Dakota Paasman** 29:44 Cool.
**Tigran Najaryan** 29:45 Provided that it's actually a small change in the implementation, it's not a major thing to maintain.
I think it should be fine.
**Dakota Paasman** 29:52 Yeah.
Yeah.
**Tigran Najaryan** 29:54 And I would also like to make this, like.
For both WebSocket and plain HTTP, so that… walks across.
**Dakota Paasman** 30:04 Okay.
**Tigran Najaryan** 30:05 If possible, if it does work, yeah.
**Dakota Paasman** 30:08 Yeah, yeah, I'll double-check the HTTP side, make sure.
No, I'll post a follow-up if needed.
**Andy Keller** 30:16 Nakota and I have already talked about this in general, so I'll just… say that I support it, because I'm fully aware of it, but…
**Tigran Najaryan** 30:26 Yeah, I'm fine.
I don't see… I don't see why we wouldn't do this.
**Dakota Paasman** 30:34 Cool.
**Andy Keller** 30:34 Thanks, thanks, Dakota.
**Dakota Paasman** 30:37 Yeah, thank you guys. Yeah, that's all I had on the agenda for today.
**Tigran Najaryan** 30:46 Okay, thank you.
That's all in the agenda. Anyone has anything else?
Okay, thank you all.
**Andy Keller** 31:06 Bye.
**Tigran Najaryan** 31:07 Bye.
