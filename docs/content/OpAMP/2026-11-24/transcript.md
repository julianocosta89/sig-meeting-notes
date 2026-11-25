SIG: OpAMP
Date: 2026-11-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Evan Bradley** 01:50 Hi, everyone.
**Kelsey Ma** 01:54 Hey, folks.
**Tyler Helmuth** 01:59 Hello.
**Evan Bradley** 03:16 I think we can get started. Kelsey, you wanna start us off?
**Kelsey Ma** 03:20 Yeah, I just, wanted to talk about the comments on the add-on proposal.
So, I think, yeah, that is a good point regarding, you know, like, when does it just become an agent?
of its own, especially for, like, executables. I think a lot of that, I was considering, like, oh, do we build in stuff for, like, health, etc, all those things, but I didn't really consider, like, custom messages, etc, and at that point, it does… start really expanding out, so I… I think what you were saying, Evan, makes a lot of sense if we want to make a, like, a delineation between executables being agents and Add-on packages just being anything non-executable, then it's a little more… it's a little easier to kind of make that split, since, like, any other way we try to split out certain executables as agents, I feel… I mean, as add-ons, I do feel like… a lot of times, if you try to delineate, like, with the JMX scraper versus just, like, the Java agent, things like that, like, both of them operate in vaguely similar ways, you know, telemetry sent to the collector, etc. So it does get fuzzy of trying to split those up.
So, if… if that makes sense, I think I was replying to you guys on the proposal as well, like, we could just… go… go with that way forward regarding the proposal. Keep the add-on packages as non-executables, which also, I think, keeps it simple regarding the spec, things like that. Like, we… We probably don't need to introduce more spec, For add-ons, because if they're non-executable, then… They're not really gonna expand across too many more maps, just, and then… Yeah, I think that was kind of the…
**Andy Keller** 05:26 So are you saying that they wouldn't really exist, then, in remote?
Config.
**Kelsey Ma** 05:32 Yeah, pretty much remote config, and then, the normal package stuff, and then, maybe we add a little bit still into the available components, but that's not really something that… that… that's just, like, a reporting backup sort of thing. So really, the only impact one would be, like, remote config.
**Andy Keller** 05:50 I think the thing that's awkward about available components is And honestly, this is a little bit awkward about the supervisor in general right now, is that we're trying to communicate state about the supervisor.
And right now, the supervisor is just a mechanism to transmit state about the collector.
We've kind of run into this a couple times. I know there was a proposal to add a header identifying the supervisor.
In the agent description, I think.
It's, it's, like, the available components, I guess I'm just trying to figure out how that would work. So the agent would report the collector, I guess. I'm so bad at using the terms correctly, especially when the… the entire specs as agent. So let's just say agent for now. The agent, reports its available components, but I think what you're suggesting is that the supervisor itself has its own available components based on the add-ons that are available, or… Or no.
**Kelsey Ma** 06:51 Yeah, like, if it could just inject, like, an add-ons, Map into the… whatever the collector is sending up, and then that gets, all of that gets sent up to the server.
**Andy Keller** 07:05 And how's that different than… Like, why… I guess, why do we need that separate from packages?
the package status.
We don't have enough.
**Kelsey Ma** 07:18 Oh, this would just be… this would just be more, like, information-wise, because I… oh, sorry, going back to the package proposal, I think, I think it's still helpful to have the factory setup that… that Dimitri was introducing in his prototype. You know, I… especially because Even with files, I do think there is a variety of behavior that people might want, like maybe, certain, bundles, like, file bundles don't need a collector restart necessarily, things like that, and they want to avoid, that sort of, stuff happening. So, so the file type that we define, built in in the supervisor could be, like, really minimal standard, and then The factory still allows distros to kind of, like, add in their own custom behavior if needed, which then, it is helpful maybe to have the available components to be sent up so that the supervisor can kind of report what types of add-ons it can support.
**Andy Keller** 08:22 Right.
Yeah,
**Kelsey Ma** 08:28 Since with the add-ons being kind of, coded into the supervisor, it does get tricky if they're… you know, like, the server doesn't necessarily know, like, if it could send an add-on down, and if the supervisor actually supports it without trying to do it, and then maybe it, like, errors out. So then this way is, like, an easier way to kind of report up an inventory of what it can do.
**Andy Keller** 08:54 Yeah, I think the intent is certainly right. I'm just… I guess I'm just… it does… like I said, it kind of confuses things, because we're… we're mixing the state of the supervisor and the agent, and I guess we're considering them all as, like, a collective.
deployment,
**Kelsey Ma** 09:12 I see. I thought available components was… a little more flexible in the spec definition, or were we trying to keep it, like, collector only?
**Andy Keller** 09:21 Well, I think right now it's collector only. I mean, it… I, I don't, I don't know if… It's a good question. I don't remember what the spec says specifically about available components.
and whether they're just meant to represent the available components of the agent. I mean, I feel like they're… they're on the agent-to-server message.
The agent has an ID, the agent has a description, it's really, like.
Agent has status, it's all agent stuff.
and so… I'm just… you know, and I'm not… don't make this out… don't take this the wrong way that I'm, like, against this or anything, I'm just trying to think out loud about, like.
this… what… what state do we currently… represent of the supervisor.
you know, should we add more? Should we… should it be more clear?
**Kelsey Ma** 10:22 Yeah, I guess the available components, it just sort of says, each agent may be composed of multiple subcomponents, so I guess if we did want to keep it focused on the agent with that definition… some sort of… would it be, like, some sort of, maybe, packet, add-on specific?
Thing we could send up,
**Andy Keller** 10:48 Yeah, I mean, it's probably… Possibly. I guess just to kind of take it… you know, but back up, maybe a higher level. Excuse me, my… my feeling on this in general is I'd rather, like.
Really get this right in the spec.
And, you know, I'm happy to… we're not 1.0 yet, I'm happy to iterate a bit on Especially the add-ons, which aren't really used yet. If we feel like they're missing things.
Like a list of add-ons that the agent supports, for example.
I'd rather, like, get that right in the spec. I'm concerned about this, like, convention Of prefixing fields in maps, and, like, blurring that across.
Multiple maps, and then, and also this… I'm kind of torn on this issue of… The agent versus the supervisor identity, and whether the supervisor should have some identity and should be represented in some way, or… or if it should just be merged in and treated as… The agent really consists of… supervisor plus agent, and that's, like, All considered the agent, so… I don't know whose hand's up first, so… one of you.
**Evan Bradley** 12:13 Mikola.
**Mikołaj Świątek** 12:15 If you're already unmuted, it says, you might as well have said…
**Evan Bradley** 12:19 Well, you're unmuted as you're speaking, but… Okay, alright, no, I'll take it, I'll take it. No, I just… I needed a quick reminder on, you said that the factories, you think would still be good, but if we consider add-ons to be non-executable, couldn't we just consider them all files?
Like, plain file, write to disk, and then… You have the agent do something with that?
**Kelsey Ma** 12:44 Yeah, I think, it's useful if you want to configure behavior regarding, like, oh, maybe you don't need the agent slash the collector to, like, always reload, or things like that. The factory, I think, is more scoped down to specifically how the supervisor implements it, so that wouldn't be at least, like.
defining anything required in the spec. It's more just allowing some flexibility in the supervisor of how you handle the files, Especially if you want to… yeah, I think the main one would be maybe you don't need the collector reload, and then maybe you want to allow for some minimal, like, remote config.
without needing to send down a new package. So in the base, like, built-in file one we add, we could just, like, keep it really… straightforward, like, no remote config and… and always reload collector, like, but then if users want… if, like, you have different behavior that you want, maybe you can, use the factory to kind of add that.
**Evan Bradley** 13:45 And then, one more question, on that, So, the… for determining which packages the supervisor supports, couldn't we… if they are non-executable, couldn't we go off of the available components that's sent by, in this case, the collector? So, I think the example that was given on the issue was the GOIP database.
So we could look… the server could look for that in the collector and knows that it makes sense to send that file versus not send that file based on… on the agent's, requirement. I mean, I see the issue with the factory, but I'm just wondering if we can… Simplify it from the supervisor end, if we could.
Kind of remove the need for, needing to understand, like, what the supervisor supports, per se.
**Kelsey Ma** 14:33 Yeah, that's a good point. I'm trying to think. I guess, would the server need to know, then, each individual package, like, what component it would need to map to in that case?
**Evan Bradley** 14:46 Right. Well, I mean, that's the idea, right? You're sending an add-on file for some other… So, I think the idea for add-ons, at least in the spec, is that it's a… an add-on is like a sub-package for, like, a main package. So, an add-on in this case would be a subpackage for the collector, and then you would just know which sub-packages, or how to map, What the main package, the collector, supports to the subpackages.
**Kelsey Ma** 15:15 Yeah, yeah.
I think, I guess, like, if you had the supervisor, like, the general, like, file type, etc, like, you don't need to know exactly which component at the… from the server, at least. I think as long as… You're sending down something that matches the supervisor types, but if we are okay with, like, the server needing to know which, like, exact component, then… I think using the existing available components, that could still work then.
**Evan Bradley** 15:55 Okay, Mikolai, you have your hand up.
**Mikołaj Świątek** 15:59 Now, on a completely different note about how… whether to… what to report about the supervisor.
I think the prior art, or all the prior art that I'm aware of, basically reports it as its own entity.
Maybe that's… But all of those supervisors that I'm aware of generally do more than the current… OpAMP supervisor?
That we have, and I… I think… I think reporting it as its own entity is just basically being truthful about the reality of the situation.
I'm not sure what the exact right format for the description is necessarily there, but it definitely makes sense for a backend to know some things about the supervisor as an entity that is, like, separate from the collector running. They have, like, very different purposes.
Right.
And problems with, like, the problems with the supervisor have very different remediation paths than, like, problems with the collector as well, I think, a lot of the time.
**Andy Keller** 17:15 Yeah, makes sense.
Are you… do you want to handle executable add-ons eventually, anyway?
because I understand, like, simplifying the requirements initially, but what I don't want to do is simplify the requirements and then, you know, come back, like, a couple months later and try to figure out how we, like, shoehorn JMX into this.
So, I'd like to just have, like, a… a really clean spec, both… both at the supervisor level, like… like, there are two specs, right? There's the supervisor spec, and there's the, OpAMP spec, and I just like both of them to be… Super clear about, how this works, and also… Accommodate… future expansion.
And I'm just worried that if we… If we do something… Partial right now, and then… try to expand on it later, it might not fit well in what we're trying to… Hmm.
Support right now, and… and then… We have this issue of, okay, do we just add this other mechanism for this other executable thing, or should we have just have… Salt this all along, and… So, I guess that's my concern. So, what are your thoughts?
**Kelsey Ma** 18:44 Yeah, yeah, I think, I agree with what everyone was suggesting, maybe we scope add-ons to only non-executables, and then executables will need to join the whole discussion. I think that that's starting to begin regarding, like, different agents, supervisors supporting different agents, because, like.
It is… like, the more I think about it, the harder it is to kind of scope what kind of executable would be an add-on and not an agent. Like, it gets really hard to, I think, split that up and then They could, you know… use, like, all the other things that you're pointing out, like, in the message, so I do think maybe, like, if we want to just lump, like, anything executable that basically needs to be its own agent, and then that's something that we can discuss on, you know, how do we think supervisor might support multiple agents.
**Andy Keller** 19:44 Yeah.
I know that's… I mentioned this in Salt Lake City, but it's definitely a need of ours right now to, like, solve this for multiple sub-agents.
And I think there's two paths we could go down.
for that. One is… Just sort of a forwarding, like, proxy method, like, basically let the supervisor proxy OpAMP messages to… other listeners. So, you know, we already have an OpAMP server in the supervisor, we just allow other agents to connect, and if they're not, like, the primary agent, we… Just forward messages back and forth.
The other model is that… the… it's more of a package, right? It's like you… You send one remote config down, and it represents the remote config of All of the agents that you, that you have operating, you know, it's like one state, it's one entity that you're… managing, One set of packages, one set of… You know, everything, available components, but prefixed and structured in some way that supports nested… you know, agents below the primary agent.
So, I think there's some advantages of having this. Like, this is one kind of compound agent.
it makes it a little bit easier, I think, on the server side, because… you're just like, I don't care if this is made up of 1 agent or seven agents, like, this is the config I want to give it, and, like, let them disperse.
Where if… if they… if you're just proxying, then you have these 7 agents that are all, like.
Part of this one… Entity, but our reporting just is completely separate.
Like, they're just not associated, unless we introduce some mechanism for association, like, the supervisor always adds Itself to the description or something, but, But otherwise, you end up with you know, generally, I think on the server side, you want to coordinate configuration amongst these things.
And… you know, in the case of JMX, you want to configure JMX at the same time you want to configure the rest of your receivers and the rest of your pipeline.
And if they're separate things, then you're… you kind of have to coordinate that yourself with a server. Say, like, okay, like, I gave it the new JMX thing, now I need to give… my pipeline, like, the new thing that's gonna use it, or whatever. I don't know exactly how you're planning to use the JMX thing, but that's just… Just a hypothetical, right? So… So, I mean, I'm interested in solving the larger problem, because, you know, we need to, we have a use case for it.
But I also don't want to, like, hold up If the file thing is just something we need right now.
we could solve that, but I also don't want to solve it in a way that… Precludes us from solving the larger problem.
**Kelsey Ma** 23:02 Yeah, that makes sense.
I think… if we have, the non-executables as add-ons, that should hopefully, like, not block anything executable side where we're trying to solve it as, like, an agent.
I think, because most likely it would… it would probably be, like, a totally different path, and maybe even, you know, spec additions that we might have to do for that, especially if… We… Wants some sort of… better grouping… Of those, but also to have their own identity.
Or, like, a description, I think you were mentioning, which probably is helpful for if you're having a bunch of, side, things also running. It's… Yeah, so I feel like it makes sense if we lump those all together, and then maybe see if we want to do some sort of, like, spec change regarding that to better accommodate, Yeah, and then… and then, meanwhile, like, we just scope add-ons down to, like, they're just… they're just non-executable files.
**Andy Keller** 24:17 Yeah.
And I'm just looking at what it's… what the spec says about add-ons.
It's really not a lot.
It's just as part of, like, a package stripe includes add-on, as opposed to top level.
**Kelsey Ma** 24:40 Yeah, so we could also… I don't know if we need to add this, maybe this more in the supervisor spec, where we just say, like, for the supervisor, an add-on for the collector means just, like, a non-executable file, if we wanted to verify it there, yeah.
**Andy Keller** 24:58 Yeah.
Okay.
Well, any other thoughts on this kind of issue in general?
If not, I would say that maybe we move forward with the proposed supervisor spec change.
To actually document, like, what messages What appear in which cases, and what behavior the supervisor Should have, upon seeing those messages.
if we need any available components injection, what that looks like, and why. It sounds like we probably don't with files, but maybe… maybe you're thinking we do?
**Kelsey Ma** 25:36 I guess it depends. I think what Evan said makes sense, like, if… If it just uses the existing available components that the collector's recording, because technically the files will always map to one of those.
Yeah, so maybe we just clarify, like, how… how that's…
**Andy Keller** 25:54 It was the super hot.
**Kelsey Ma** 25:55 to use it, yeah.
**Andy Keller** 25:56 Unless the supervisor is executing on the file in some way.
which we're deciding it… it won't, then… then it, then the only thing that could execute on that file, it would be… The… the collector itself.
But I think we also need some spec about, you know, where these files live.
Where they're written… where the supervisor writes them.
How they're accessible to… The collector…
**Kelsey Ma** 26:26 Yep, that makes sense.
**Andy Keller** 26:27 Like, what that… what that should all look like.
I think I understand it high level, but we just need to get it really tied in the spec, and then we can implement it.
**Kelsey Ma** 26:42 Sounds good.
Yeah, I think,
**Andy Keller** 26:54 Start…
**Kelsey Ma** 26:56 Oh, no, I was just gonna say, I think the agents thing is definitely needed. There's a few different use cases, I think, out there of wanting to run other stuff, but yeah, I think that'll be probably a much larger discussion that might take some more time to really worry about the spec needs on that.
**Andy Keller** 27:16 Yeah.
Okay.
Alright, so something further on that, Jessica?
**Jessica Yang** 27:27 Yeah, won't take up too much of everyone's time, but, yeah, like, I know, Andy, you kind of did a call-out for maybe the need for more, like, approvers, reviewers, maintainers for the SIG, and… I think we're pretty interested in maybe stepping up and doing more of that, just because, like, yeah, we're also hoping to kind of support a variety of use cases with OpAMP, and I think, like, in the upcoming, at least, like, quarter slash, like, year or so, we'll kind of see more development there. So I won't speak for Stanley, but, I believe he's, like, a pretty good candidate kind of, like, step up a little bit into more of, like, an approver-reviewer role. Obviously, we'll kind of… wait for him to get back from PTO and, like, see his interest, but, yeah, like, that's kind of what I just wanted to bring up. Definitely a lot of interest from us to get more, more involved.
**Andy Keller** 28:31 I'm just gonna make it… put it in the notes, Jessica volunteered at Stanley.
**Jessica Yang** 28:34 Yeah.
**Andy Keller** 28:36 Cool.
**Jessica Yang** 28:37 But yeah.
**Andy Keller** 28:39 Okay, that sounds great.
All right, and let me follow the attempt link, but…
**Mikołaj Świątek** 28:52 Is it… did I mess up the link?
**Andy Keller** 28:54 No, it's good, I'm just following it.
**Mikołaj Świątek** 28:55 Oh, that's this one, right, right. So I don't think I really need any… or maybe, maybe I do. Maybe I would like to ask the opinion of this, like, you know, expert gathering of experts on this. It touches… it's not exactly about remote management, but it's about status propagation.
And essentially, like, the question is, if we're doing a partial reload.
We need to get rid of the state machine for a different component. Right now, we don't, so it leaks.
And the question is, when can we actually get rid of it?
And this question maybe has, like, an obvious answer now, and this pull request kind of had the obvious implementation for it, but that obvious answer might not be so obvious in the near future.
In the sense that if we start doing things that some of us here would like to do, like the reload interface for components, and even more slightly dynamic things, then the answer to the question of, like, can we get rid of this state machine becomes Not that straightforward, or at least you can't really easily tell just by looking at component status, because it might be possible for a component to, like, go from running to stopped, and then from stopped to running.
In the future.
So, just saying, after we get stopped, or permanent error, or what have you, we get rid of it, is not that easy. Is that… I mean, there's certain problems with doing that? So, I asked… I'm not sure if the contributor there knows, I actually don't have any power in this repository, but… But I did… I did… I did give my opinion that this should probably… and every, like, again, all the prior art that I've seen essentially does this.
that… The only way you can, like.
Definitely tell whether something's running or not.
is to just go to whatever component is supervising it, and check with it. So in this case, we only drop the state machine after… in the graph, after the graph is done shutting down components.
And also, the problem, partially, is that, and this doesn't happen right now, but, like, as ideally, the, you know, the bright future where components are going to be more decentralized and other things are going to be encounter, and there's going to be, like, more of a normal ecosystem for all this stuff, the component can emit whatever it wants.
In terms of status. There's no… There's no guarantees. It can… it's stopped in the middle by itself. Nothing really prevents it from doing that, right?
So… so we need something that is, like, more authoritative.
BlackLogic. And I'm just bringing it here because I think some people here might be interested in it. And also, and also Evan is on the reviewer list.
If anyone has opinions about this right now, I don't know.
We can talk a little bit.
**Andy Keller** 31:56 Yeah, I mean, I'm definitely interested in, more dynamic.
Partial reload of configs, and the impact that that has on… I guess what I, like… so what's not clear to me is this… Do you see this as a spec concern, a library concern, or just a collector implementation concern?
**Mikołaj Świątek** 32:22 This is just a bug in the collector. It's just that…
**Andy Keller** 32:26 Yes.
**Mikołaj Świątek** 32:27 This is, this is literally just bug. It doesn't have anything directly to do with remote management, but it has, it has, you know.
it is in spirit, in the… a little bit in the remote management, let's call it. And I also don't want to, you know, take up anyone's time with this here.
**Andy Keller** 32:47 No, it's definitely interesting. Thanks for… thanks for bringing it to my attention.
**Mikołaj Świątek** 32:53 There's also, on that note, I can also, I can give a smaller part on what is going. There's also a pull request in the collector to do dynamic reload on processors right now.
So, that's one thing. The… if you're interested specifically in the reload… In the reload interface, which is a different concern, the partial reload work is basically the idea. We still demolish any components that we… where the configuration changes, it's just the attempt is to demolish only the parts that we actually need.
Whereas with the real interface, the idea is that we keep the component around and just call a special, special method on it to have a new config instead of a thing. And that is a little bit more contentious, I think. I talked to Demetr about this at KoopCon. Well, I harassed him about this, and… There's, like, a concern where if you implement… if you do this naively, you're putting a lot of implementation pressure on a component to do it.
Whereas, it's possible that if the… If the collector itself did more work, you could make this much simpler for components to implement, potentially?
So… so there's… some ambiguity.
In.
**Andy Keller** 34:18 Yeah.
Well, it's good to know that this is coming, and, you know, in terms of impact here, it's going to change the way this… We're gonna want to extend the supervisor To be able to… Trigger this behavior, as opposed to always shutting down the supervisor, writing config, and restarting.
Hmm.
**Mikołaj Świątek** 34:41 I mean, it's… you don't have to do anything specifically in terms of triggering, you just have to have, like, a config provider that can implement.
whatever the interface is called, that's… at Elastic, we have it.
It works.
We have an incredibly stupid config provider… well, incredibly stupid. We have an incredibly simple config provider where you literally just write to… over a pipe to the collector's standard input.
**Andy Keller** 35:10 Oh my goodness.
**Mikołaj Świątek** 35:11 And you can wire this up, and it works. It's… the reload works fine. But you could easily write, like, write a new provider that Just watch as a file.
and reads from the file, or something changes. We don't do this for, like, security reasons, because, you know, people who are security conscious hate having stuff in files on disk when they don't have to have it in files on disk.
But yeah, and otherwise, otherwise the behavior itself is mostly transparent. There's some problems with it still. It leaks from telemetry resources, or unfortunate Go SDK reasons.
Hmm.
But other than that, there isn't really, like, a conceptual problem with any of it, I would say.
**Andy Keller** 36:03 Cool.
That's… Thanks.
**Mikołaj Świątek** 36:07 That's what I had.
**Andy Keller** 36:10 Appreciate it. Anything else?
Something else on the agenda.
Okay.
**Tyler Helmuth** 36:21 I've got one, I've got one, just an anonymous.
**Andy Keller** 36:24 Keller, great!
**Tyler Helmuth** 36:24 hadn't seen. We just published a CVE for the OpAMP supervisor. It's, a pretty high one. The issue is fixed in version… 0.165.0 of the collector. You can go read about the details of the advisory if you want, but the issue was our implementation of the remote the remote configuration… remote… connection settings, remote connection settings, was done incorrectly, and we essentially were dropping TL… any setup TLS, if you got that message. So it was pretty bad. So, just FYI, if you're running OpAMP Supervisor anywhere, you probably want to upgrade.
**Andy Keller** 37:06 Yeah.
Would you mind adding that to the notes?
**Tyler Helmuth** 37:12 Yep.
**Andy Keller** 37:13 If you don't have them handy, I can give you a link.
**Evan Bradley** 37:16 I do want to say that…
**Tyler Helmuth** 37:17 I think the… Yeah, I got him.
**Evan Bradley** 37:18 CVSS score of critical is a little bit alarmist, but, yeah, I definitely would recommend upgrading.
**Tyler Helmuth** 37:25 Every single time I score something with CVSS version 4, it just, like, jumps 3 numbers, 3 ticks from the version 3, and I… Yeah.
**Evan Bradley** 37:37 No, it's not… it's not your fault, I just saw that, and I was kind of like, okay, I get it, but…
**Tyler Helmuth** 37:41 Pretty crazy. It's our first critical, and it's really annoying.
And the criticality of it doesn't take into effect any nuances, like if your OpAMP server or your supervisor never accepts remote connection settings, right?
So, but whatever.
**Evan Bradley** 37:58 Not to mention the fact that you need an established connection to a trusted OpAMP server to start with. This isn't, like, critical, I would think, like, somebody is remotely going to tap into your supervisor and do something, but… no, this is… this is essentially, like, you have a misconfigured server.
But still, definitely important.
**Mikołaj Świątek** 38:19 There's definitely an inflation of severity scores going on.
**Tyler Helmuth** 38:29 It's annoying.
**Andy Keller** 38:29 Right.
Well, thanks, Tyler!
Anything else?
Alright.
Great. We'll celebrate in two weeks.
**Evan Bradley** 38:44 Everyone.
**Andy Keller** 38:45 Kelsey, if you, If you have a spec that you want reviewed, and I don't notice it, I would just add it to the… put it in the Slack as soon as it's ready.
Just make sure, like.
**Kelsey Ma** 38:56 wouldn't…
**Andy Keller** 38:57 I know you want to make progress on this, so…
**Kelsey Ma** 39:00 Yeah, thanks.
**Andy Keller** 39:02 And also, I'm, I'm going to get back to the message Anastasia stuff next week.
So, I'm sorry that I was, like, totally sick last week, I was completely… useless, It was not good.
I forgot how much, you know, when you're sick, your brain doesn't work as well. I always just think of, like, physically ill, but… I wasn't… I was not… you did not want me approving any PRs last week, so… Right.
**Jessica Yang** 39:34 the better.
**Andy Keller** 39:35 Thank you.
Me too. Alright, see you, everybody.
**Kelsey Ma** 39:40 See ya.
