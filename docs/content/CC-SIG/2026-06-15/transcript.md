SIG: OpenTelemetry C/C++ SIG
Date: 2026-06-15
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**malff** 00:59 Hi, Doug!
**Doug Barker** 01:02 Hey, Mark.
**malff** 01:05 So… Let me see if I'm… Better waste time at sharing my screen.
**Doug Barker** 01:22 Yep, I can see your screen and your mouse.
**malff** 01:25 Okay, and it's moving.
So, how have you been?
**Doug Barker** 01:34 Oh, not too bad.
About yourself.
**malff** 01:47 Tom mentioned last time that Ladit was in a different time zone, compared to the usual, so I don't know if it's still the case or not.
So, I don't know if he'll be, joining or not, we'll see.
**Doug Barker** 02:01 Okay.
**malff** 02:10 Oh.
As usual, I… put together a few notes. I don't know if you have Anything you want to discuss in particular?
**Doug Barker** 02:21 Maybe just, sync on the… YAML CMake PR, and then the one that I just, posted as draft with a, severity, so this is something we discussed in the last meeting, but we can, talk about it.
**malff** 02:36 Sure, we can do that.
I'm assuming it's this one?
**Doug Barker** 02:51 Yeah.
**malff** 02:52 Yes, okay.
**Doug Barker** 02:56 So I made some comments on this one. I think my only thought was… that there's another approach that I hadn't brought up that we could take, which is to just put the programmatic header files.
into the normal SDK target, and don't make it a CMake component, and then that way we would just leave the existing component and configuration CMake target to just bring in the YAML file, that would Do the least change for users.
That's one option that we hadn't discussed, but could consider here as well.
**malff** 03:31 Could be, although… So, all the configuration part, especially for the programmatic interface, it is mostly Ado files, but not only, I think, because we have, at the minimum, the SDK builder, things like that.
And… given that it's, It's still an optional component, so I think it makes sense to have a different library compared to the SDK.
For people who want, really, a very minimal binary, where they just… Create an exporter directly, and don't even use this.
**Doug Barker** 04:10 Okay.
**malff** 04:11 I'm thinking, like, recently we had a PR for an embedded system where, No.
So, the request was to use something different than curl, but I'm assuming that for an embedded system, you only want to strip down the amount of code to the bare minimum.
So that would be a way to, do it.
**Doug Barker** 04:37 That makes sense.
In that… in that case, like, one thing we could… we could consider to have the least amount of change since the configuration component, CMake component in target has been out there for a while, is to add a new CMake target for the programmatic SDK header and CPP.
providers.
And then just have the CMake component only bring in the the YAML dependency.
**malff** 05:04 Yeah, so basically, don't rename to YAML, but instead, rename the… the common part to something like Core, or something like that.
**Doug Barker** 05:12 Right, yeah, configuration core, maybe that's a good one.
**malff** 05:16 Yes.
**Doug Barker** 05:18 We kind of have a… Where CMake components bring in dependencies, and that's why they exist.
Because we can always, you know, build the SDK component with different targets that we can optionally link to.
It doesn't need to be, like, a whole CMake component, which is what this PR does, and what I had originally proposed, but I think Probably the simpler path.
With least amount of change on users may make sense.
**malff** 05:44 So that will work, In the very long term, I don't know if YAML will be the only way that exists.
It's very likely, but… conceivably, someone can decide to do the exact same thing in XML if they want to.
Or something else.
Right. So, if we go… if we ever go that route, it's likely that we will have like, a library named YAML, a library named DXML, a library named something else for all the different flavors of… configuration, but… Not, not going up and shopping anytime soon, anyway.
So…
**Doug Barker** 06:28 Okay. Well, in that case, maybe what we could do… Is have this new compo- core component, we call it a configuration core, that way it's a new target.
And then we can… we can make an alias.
configuration to configuration YAML, and then maybe deprecated over some period of time?
**malff** 06:48 True.
**Doug Barker** 06:51 And then that way…
**malff** 06:52 Yeah, yeah. I'm not saying it's likely to happen, but just trying to think out loud.
**Doug Barker** 06:57 Yeah.
**malff** 06:58 If we… if we ever need to support multiple, file system… file storage, basically, or not? Or only, you know?
Like, Yeah, people can have, maybe a JSON instead, of a YAML file, things like that.
**Doug Barker** 07:15 Yep.
Okay.
I may edit my comments here then. So I think what I propose is that we keep a CMake component for… to bring in the YAML dependency.
and then add a new CMake target for the core programmatic, configuration, components.
And then we can' then we can do an alias target for configuration to configuration YAML, and then… Maybe that, reduces the amount of change on users.
**malff** 07:54 Nice.
Or just keep configuration as is, for the demo part. And the day we have JSON or XML, then it will be configuration JSON and configuration XML.
renaming… It would be nice to have a symmetric naming, but It doesn't have to be that way.
**Doug Barker** 08:16 Okay.
Okay, yeah.
**malff** 08:20 I don't… I don't know… so this is recent, so I don't know how many people are actually using it.
It looks like some people do, so we have to say exactly… no matter what we do, we have to say exactly what would be the impact for the makefile, so that people are not surprised.
And I don't know if you noticed, but, In the community repo, there is a discussion about, a donation for Python, which is using the C++ SDK underneath it, especially for the YAML configuration.
So I know at least that it is used in this context.
**Doug Barker** 09:00 Yep, I saw that, too. That's kind of what I did, because I'm using the programmatic… or want to use the programmatic interface, and then I saw the Python… Library was also using it.
**malff** 09:12 Okay.
**Doug Barker** 09:13 So…
**malff** 09:17 Okay, so yeah, so if we… instead of configuration and configuration YAML that we have today, if we have… Something else, like configuration core and configuration, then that would… That would not imply any change to user make files?
So that actually resolves the comment that I had.
who are the… A note to the changelog, because that will not even be necessary then.
**Doug Barker** 09:47 Yeah, I think that's a better approach.
**malff** 09:50 Okay.
And so, otherwise, I think this, from what I've seen of at PR, it looks okay to me, so I was planning to merge it soon.
**Doug Barker** 10:04 Okay, I'll, after the call, I'll reply and, update my, my comments and, give them an update based on what we discussed.
**malff** 10:14 Okay.
**Doug Barker** 10:15 Correct. Yep.
**malff** 10:19 And also, I saw that you had a different, I think it was an issue… vous sampling?
**Doug Barker** 10:30 Yeah, I didn't get my comments in before that one merged, but I think we should rename.
composable trace ID ratio-based sampler, because that's not one that's defined in the spec to,
**malff** 10:41 Yes.
**Doug Barker** 10:42 to one that aligns with the specs. I think they're technically different things, like the trace ID ratio would be deprecated, but should still exist for a period of time, I think.
2027, or whatever they say.
**malff** 10:53 Yes.
Yeah, I have to read respect exactly again on this area, because I know that it's, Well, at least my memory is a bit blurry, and I don't fully grasp why they had a name change for that.
So maybe if there is a technical reason being, About that, but, yes, it's… at least if a spec named something We should use some consistent naming, so it's easier to map this back and forth.
Otherwise, it adds confusion.
So, yeah, that will be a major… minor change anyway, so easy to do.
**Doug Barker** 11:30 Cheer.
**malff** 11:35 Vo… I forgot his name, but the person who actually contributed that PR with all the cons… composable samplers.
So, the PR is only implementing the samplers themselves, with unit tests and everything.
But it's not integrated yet with the rest of the code, and I think he wanted to follow up and do the next part, which is… Now that we have the samplers.
hook them up in the YAML SDK Builder.
To actually, create… when the sampler is configured, to actually create the samplers and use them at runtime.
So, we'll see how it goes, and maybe we'll have also some input on the naming, and… More things, obviously.
**Doug Barker** 12:28 Perfect.
**malff** 12:42 Trying to find my notes.
One thing I noticed, so… Strangely, OpenTeametry C++ is popular those days.
So, the first thing is we have plenty of PRs.
Which… Well, it's a good issue to have, I would say.
But then we need to, To keep up with the pace and do the reviews that… People don't forget about it and do something else instead.
That's who, yeah, so a lot of reviews, and on top of that.
I don't… so I don't know why. Maybe it's the end of the year, so students in CS have more time and do some personal projects or whatnot, I don't know.
But I just noticed that we have a lot of contribution, Especially on things which are listed in the contribution welcome part, this… In this list. So this is the list of, good projects to start with, and, add a few… Let's hold on forever. I had a few in this area on the YAML configuration part, which have been, So, for which we had contribution, which have been reviewed, merged, and so on, so I think I will try to add more entries there, because there seems to be some competition where everyone wants to play with this thing.
And because of that, we just had, two or three kids, at least two.
Where we had multiple contributions for the very exact same issue.
**Doug Barker** 14:33 Yeah, I think the most re… well, there was two. There's one that you had marked duplicate, and then this recent one, which was a little… little concerning with the, was it the spam, or the log record limits?
**malff** 14:45 Yeah, we don't work out fingers.
So, to address that, I plan to add more entries, so at least we don't have a bottleneck with everyone eating the same one.
And, just so you know.
also to try to mitigate that, I added some notes there, which is basically saying, hey.
If you want to work on something, make sure nobody else is already looking at this first.
**Doug Barker** 15:15 That makes sense. Should we add something? Because I think this also came up with the… like, the YAML configuration, and maybe there's another one where I logged a ticket with the intent to discuss it, and then come up with a plan… an agreed-upon plan before we implement, but, as soon as the issues get posted, people will pick them up right away. Do we need to give any more guidance on, like, which issues? Certainly the ones that say, help one had good first issues.
But then some of them are being picked up where there's… there's, like, a dis… even still a discuss, label on them.
**malff** 15:48 Yeah.
Not… not truly the… I mean, it's good to see people contributing and finding stuff they like.
So I don't want to put more bears there.
But then it's up to us to… Well, provide a… provide choice, so that not everyone, Use the same one, and also… Oh… Maybe there's an issue of scoping, like, whether… I've not decided whether it's better to have one big issue with a lot of things that, spans a lot of code and then can take some time to review, or if it's better to… Size that into smaller chunks that can be done one at a time.
**Doug Barker** 16:43 I'd probably… as a reviewer, I would prefer to have small, you know, smaller PRs. I think we've attended… several of these recent ones have been almost 2,000 lines changes.
**malff** 16:54 Yes.
**Doug Barker** 16:55 So… you know, that feels… it feels like it's getting up there a little bit high. I think it's, sometimes the AI tools do help a little bit, but it's still quite a bit to keep track of.
**malff** 17:11 Well, sometimes these PRs are very repetitive, so the number of lines is not a concern, and sometimes the code is very difficult to get into.
Like, all the gRPC changes and whatnot for… There's something in HTTP, gRPC, and HTTP…
**Doug Barker** 17:28 Yeah.
**malff** 17:29 well, OTLP, HTTP, and OTLP gRPC, sorry. And yeah, the code is harder to get into there, and if there are thousands of lines, yes, it takes some time.
The thing with trying to get some smaller issues is that, Then we have to detail, okay, do this part, and do this part, and do that part, and it takes even more time to… To identify the smaller parts and to put whatever work, so…
**Doug Barker** 18:02 That's correct.
**malff** 18:08 Yeah, but anyway, so I don't know… I don't know why, but I'm surprised that a lot of… we have a lot of resolution, and I think, in my understanding, those come from… CS students, looking at that, so it's, It's good news in any case.
**Doug Barker** 18:38 Hey, Tom?
**malff** 18:41 Hi, Tom.
**Tom Tan** 18:43 Hey, Mark and the dog.
**malff** 18:52 So, we are just discussing, contributions, But, We just saw a lot of them recently.
And also, in some cases, multiple contributions on the same issue, causing some collisions.
So, you know… Trying to find a way to avoid that.
**Tom Tan** 19:17 I see, that makes sense, and what's the conclusion on that?
**malff** 19:24 Sorry, say that again?
**Tom Tan** 19:25 I mean, the conclusion, like, to avoid multiple contributions on the same issue.
**malff** 19:30 So… one… so, one thing I did is just to… to make people aware that, they should look if there's an existing issue… existing PR solving the same issue first. But I think the main important point is, in the list of issues that we have, we should, Possibly have more of them, so that we don't… we don't have a bottleneck with everyone picking the same one.
If there is more choice, then… let's say there are 10 interesting issues to work on, well, people can see that, yeah, the first one is taken, maybe I'll take the fifth one.
**Tom Tan** 20:11 Okay.
I see, so the other issue is just some, like, bigger issue which could cover multiple sub-issues, and people maybe… Try to work on the big issue at the same time, and then may… Fix the same… same part.
From multiple PR, right?
**malff** 20:31 Yeah, true.
could do Sizing in smaller issues, means to start to do the design, in fact, and define every one of them.
Chongtun.
I think that may work better for very, Juno contributors who don't know the codebase?
But from what I've seen, some people… actually, someone started to do only… warning fixes in the codebase, and did quite a few of them.
just to be familiar with the process, familiar with the review of PRs, and so on, and after that, started to do, actually, some… Decent-sized peels with.
**Tom Tan** 21:17 Hmm, move on.
**malff** 21:18 big area, so… That works too, though.
It's… not knowing who will contribute to a PR, it's hard to say, oh, this one is easy, this one is hard, and this one is no, this one is big.
**Tom Tan** 21:32 Yeah.
like, could we, like, ask the contributor, like, for the decent-sized PRs?
Always prefer open the issue on that, and when open the issue, we ask the… The contributor to check whether this is… it is duplicate or an existing issue or not.
Maybe it could help reduce, yeah. Already?
**malff** 21:55 This is what part of it. This is what I described here.
**Tom Tan** 21:58 I see.
I see. But how do we… we need to make changes to, like, to our issue template or the public doc, right? Or just put it here, sir?
**malff** 22:13 It's… in general, it's not people filing a new issue, it's people finding an existing issue which is marked as, airport wanted, and start to implement a PR on that.
**Tom Tan** 22:26 Okay.
I see.
True.
**malff** 22:32 Yeah.
Yeah, we'll see how it goes, but it's, at least… It's a good problem to have, to have too many contributions, as opposed to not enough.
**Tom Tan** 22:48 And we have… for each issue, we have a… we usually set issue only, right? Once people… declared interest, instead of just submit PR on that directly.
**malff** 23:02 Yeah, I'm… quite frankly, I'm a bit reluctant to do that, because so many times I've seen someone saying, oh, I want to work on that, and this is the last time we ever heard… hear of that person.
**Tom Tan** 23:13 Okay, that's true, yeah.
**malff** 23:16 And so, if we do that, like, okay, someone says, I want to work on this, so we say, okay, you get, you get it, and then nothing happens for two weeks, and then we say, well, the issue is open again, someone else says, I want to work on that as well, wait for two weeks, so it's…
**Tom Tan** 23:33 Yeah.
**malff** 23:34 And I think…
**Tom Tan** 23:35 Yeah, go ahead.
**malff** 23:37 Yeah, I think if we… if we go that way, it will be delayed forever.
**Tom Tan** 23:42 Yeah.
Even for this, I think we… maybe we can make it automated. If one issue is assigned to someone.
Like, without update for 2 weeks, we get it on our side and make it open.
Like that, or maybe steel.
We still, yeah, not… not will not help, like, attract the… More people to contribute.
**malff** 24:11 Yes.
**Tom Tan** 24:12 Okay.
**malff** 24:17 Do you know if Lalit is joining today?
**Tom Tan** 24:20 I think he will not. I think he's still in a different time zone, maybe for the whole month, yeah.
**malff** 24:28 Okay, yeah.
Okay, I had a few points I wanted to discuss, but do you have any… I forgot to ask you, do you have anything else you want to discuss as well?
**Tom Tan** 24:55 Or, okay, new release in the list. Do we have new… initial to track the new release?
I think we planned to do it this month, right?
**malff** 25:05 Yes, I have not created one, I will do that after the meeting.
**Tom Tan** 25:10 Okay.
That would be great. Thanks.
**malff** 25:13 Who knows?
So yeah, so the… the collisions on issues, we just discussed that. Yes, I would, create an issue for the next release.
And another thing also to be aware of, one is in the specs, open tracing is now deprecated in the specs.
So, we are not affected yet, because what this says is that The spec for open tracing is deprecated, and it will be removed, like, in a year.
from the spec repo itself, but even then… different SDK can still implement open tracing, and the timeline for deprecating open tracing in the different SDK will be more than that. We don't know yet, it's not defined.
Oh, but vu.
The first step is to… deprecate the spec first, and then after that, it will be deprecated into different SDKs, so we have plenty of time.
Okay. Just something to be aware of.
And another thing that changed, so Cement Convention did a new release, I just adjusted to that, and I don't remember if it was you or Lalit who did the review.
Maybe, like, so it's, it's merged, already.
Although there is one thing which is changing there.
Some semantic conventions… well, to… So, until now, we have only one repo for semantic conventions that contain everything.
And now, some semantic conventions for GenAI are, Moving to a different repo, which means there will be, two repos to look at now instead of just one, so we probably need to do some changes in the tooling.
And I also… Voose to repo, I don't know the details yet, but there are, I would expect, they will not release at the same time.
So, we have to see… And when to adjust for each, each new… I don't really triple.
So, some tooling change, otherwise I don't expect a lot of impact for us.
**Tom Tan** 27:49 Okay.
The toning change will not be a braking change, right?
**malff** 28:03 No, it's, well, basically, the… We need to invoke, some script to… Generate from one repo to generate a bunch of files, and then we'll have to make a second invocation to the script to just point to the second repo and generate again.
For the overset of 70 conventions.
**Tom Tan** 28:26 So, can we just use one script, like, to configure to run?
Against 2… semantic convention repose, or…
**malff** 28:36 Yeah, yeah, we can. Let me… I don't have to remember what this thing is.
We have a scripts or bridge scripts somewhere.
Yes.
So, this thing… This thing is generating from one repo.
So we'll have to just, add two lines to it to, to invoke generation from the second genera repository as well.
So… Very minor change.
**Tom Tan** 29:51 Okay.
**malff** 29:58 And this is, yeah, this is the code generation script which is used for semantic conventions.
What it does is, yeah, peak… Speaks for tuning… Picks for semantic conventions, so we would have another source for that.
To use in the circumscript invocation.
So… some minor adjustment. We just have to keep track of it, just to not be surprised.
**Tom Tan** 30:41 Do I have any issue to track this?
**malff** 30:44 Not yet, but I can create one.
**Tom Tan** 30:47 Thanks.
**malff** 30:48 Yeah, in fact, I'm waiting first for the new release of Senkong the… Gen AI, semantic conventions.
Because there is a report, but there is no first release yet.
**Tom Tan** 31:01 I see.
**malff** 31:07 On… on PRs, do you have any… Do you have any news on everything related to ETW?
And did you have a time to take a look at that?
**Tom Tan** 31:21 Yeah, let me take a look at it today. I put it on my… In my list, and yeah.
**malff** 31:27 Okay.
**Tom Tan** 31:28 Where we're playing Sunday?
**malff** 31:30 Okay, thanks. Because I don't know that code too well, and I know that you depend on it for Geneva, I think?
**Tom Tan** 31:37 Yeah, yeah, yeah, that's our ample money exporter.
**malff** 31:41 Yeah, so it's probably better if you take a look.
**Tom Tan** 31:43 Yeah.
Yeah, thanks for the reminder.
**malff** 31:46 Yep, thanks.
So… Well, everything else is same as usual, I would say, so I don't have any other topic in general to discuss.
One thing, I don't know if you noticed a lot, but I'm also getting more involved in the, YAML configuration repo itself.
So we're just beginning to maintain over there.
**Tom Tan** 32:29 Nice, congratulations, Mark. Yeah.
**malff** 32:32 Yep, thanks.
**Tom Tan** 32:42 Yeah, so I remember you did a lot of such changes in our report, huh? How… how is the current status of that? Just curious.
**malff** 32:50 It's, it's almost done, actually. Let me show you… So… There is a file in the configuration report that tracks all the different types.
Defined in the YAML format.
And for the C++ language, it says whether this thing is supported or not, so… You can see all the types which are supported. We have some types which are missing some, so far.
But very few.
And this is basically the list of things which are missing. And actually, this list is out of date, because… Recent PR… so, I need to update that, that status, but… Recently, the code for resource detection was added, so we have only a very few classes which are missing, so… It's, as far as YAML parsing is concerned, it's near completion.
No, the next step is… when something is passed in YAML, understanding the syntax is one thing, the next step is to actually invoke the SDK for it, and sometimes we, We don't have, all the code there.
So, there are things in the SDK that we need to support to back that up.
But the YAML file itself is almost complete.
**Tom Tan** 34:26 So you mean all the configuration could be parsed, or maybe not be honored by the SDK for now?
**malff** 34:32 Yes.
**Tom Tan** 34:34 I see.
Maybe that's a phase two of this YAML configuration adoption.
**malff** 34:41 Yeah, and of course, this is a never-ending story, because in the meantime, there are also some PRs in the config repo to add some nodes, add some features, all the time.
So… By the time we implement something which is missing, there's something else that showed up.
But it's, it's getting close.
**Tom Tan** 35:07 I see.
So currently, I mean, all… almost all the YAML config can be… can be configured, right, by the user, but they are not… most of them, I think, assume, will not be, like, make any change to the SDK behavior. Like, in this way.
Do you have any prompt or message for the user to see? Yeah.
the actual… config is not enforced, like that, or the user may be, if not, maybe confused, you know, with all the config.
read about the SDK fine, but behavior is not… Changed.
**malff** 35:48 Well, the… So, all the, all the config comes from a YAML file, which is, which is passed. There are some… Right, let's see… I'm trying to remember where it is. It's a JSON5 somewhere.
In the configuration repo, there are some generated documentation that shows what is done in each language.
And some… some documentation on, this thing, like, what's supposed to do, so… This doc is automatically generated from what is reported for each language.
And so this is for C++, so… This is the format we support, this is all the… all the nodes that… with the status, and what is inside, and things like that, so…
**Tom Tan** 36:52 I see.
also mean for supported, which means the SDK behavior has been updated right based on the config.
**malff** 37:06 Well, the SDK builder, as you're saying, it's just that the config does not come from… code which is written in the main application, explicitly, it comes from the YAML file which is parsed, which is doing… what the user would do by writing code, which is to say, hey, build an exporter, build a processor, attach that processor to the exporter, use that parameter, and blah blah blah.
**Tom Tan** 37:33 Okay.
**malff** 37:46 So yeah, it's, it's getting close.
See, for example, this is an example of something which is missing.
Unfortunately, this one is implemented, I just need to update the status.
Oh, nice.
In general, it's converging.
**Doug Barker** 38:04 I think maybe what Tom's saying, like, span limits? I know, because I logged… I looked into that one. That's an example where it's being parsed, but it's not… there's no plumbing to.
**malff** 38:14 Yeah, so it's…
**Doug Barker** 38:15 integration, and…
**malff** 38:17 Yes, good.
**Doug Barker** 38:17 Okay.
**malff** 38:18 Yeah, so it's the typical case. It is being passed, and there is no plumbing in the SDK, so it is ignored.
And there should be a warning for that somewhere in the code, so that if you try it, at least you will get a warning that we are enduring limits.
Yeah. And the next step is actually to implement limits in the SDK, which is what the different PRs are doing right now.
And then… Once the limits are supported in the SDK, hook that up into the SDK Builder.
And when that is done, there is a lot of PR to do in the configuration report to say, hey, this thing is supported now. So as we have, The coverage documented.
**Tom Tan** 39:18 Yeah, I think it would agree to follow this process will be more clear to the user.
**malff** 39:29 And I forgot the link, but the nice thing also about it, if you think about it, is that, This is a YAML schema. Well, this is a YAML file, so it has a schema, and if it has a schema, you can have an IDE that helps you to actually populate… write the file.
With the proper tags, the proper attributes name, the proper values, as opposed to write the syntax yourself.
**Tom Tan** 39:55 Is this gamma file, like, or how… How can the user config the schema file?
Manual configure, or is there some way to auto-detect it?
**malff** 40:13 Sorry, I missed that auto-detect which part?
**Tom Tan** 40:17 to auto-detect that schema file, like, the user is authoring a YAML config.
The user has to config the schema file manually to get all the… For the, like, features, or… Auto… Completion like that.
**malff** 40:36 Well, the… so the YAML file is, when you write a YAML file, you just put it somewhere in the file system. It could be in a different location, and there is one environment variable that tells you where to look at it.
Souvre… the YAML configuration will look at that only environment variable.
To find the schema file, and then, from that, read it.
Pass the content, and do the configuration according to the YAML file.
**Tom Tan** 41:12 Okay, I see.
We probably wish we… Make this as a submodule in our repo, so users don't need to clone it separately to get the schema.
For… for creating… the YAML config.
**malff** 41:44 We don't… well, the, We don't have a dependency on the config repo, so we don't, So, there is a schema file in the YAML repo, but we don't use a compiler to generate code for it. The code was written manually.
**Tom Tan** 42:03 Okay.
I mean, not the parsing code, I mean, just for… for authoring the YAML file, right? I think that you mentioned it will be helpful to have this schema file.
**malff** 42:18 Yeah, but the… well, the schema file itself is registered in this place.
So, if you… If you have some tool, you can, you can say in your IDE, okay, use that schema file, and…
**Tom Tan** 42:33 Okay.
**malff** 42:36 to generate some content.
**Tom Tan** 42:37 Or we should… we could register this schema as environment variable for our repo, like… Like, there's setting for various code, if, like, that we can… Set it there, so if we… the user open our… repo as a project, it will get… the user will get this by default.
Just for convenience, sir.
Yeah, like, I just mean the user may not be aware that the schema file is, like, defined here, so use it, so we maybe make it easier.
Or, by default, make it configured for the user.
to, like, to create a YAML file in our repo.
**malff** 43:22 Yes. Okay, so… basically, this is a… I think what you are describing is adoption, to let… make people aware that they can use YAML, and they have a way to do that, and…
**Tom Tan** 43:36 Yeah.
**malff** 43:37 to tell them, okay, use this file, use Putin in that place, use this, this code.
I think this is pretty much covered by the YAML example that we have in our repo.
We have a domain that, does all that, basically.
Okay. Which can be… which can be used as a… as an example when you write your own application.
**Tom Tan** 43:59 I see, yeah, I will take a look at the… our example.
**malff** 44:04 Yep.
It's, PB… Examples… Yeah, so this is the code in main.
So… you basically say, okay, I want to have this.
Maybe I want the trace exporter, but I don't want the OTIP exporter, whatnot, to say what components you have.
And then, you parse a file, and you get a result, and you create an SDK for it.
Oh, that's it.
And so this is the entire, It's… it's a bit involved, because there are all the… all the different choices, what you… you can decide if you want on or to HTTP, gRPC, and everything.
But basically… You see it's line 150.
line. So, in 100 lines, you have everything always set up for person who you're on file.
And if you copy and paste that into your application, it should work just as is.
**Tom Tan** 45:46 It was slow.
So the Yami config is… just for SDK, not for any exporter. It also applies to exporter.
**malff** 45:57 So, the YAML config will say, use this exporter, use, whether you set up a tracer provider, a matrix provider, a lot provider, and whatnot, it also covers, Propagation, limits, even though we don't support them at runtime yet.
And there are also other things, fraudworth.
It also covers logging, I think, internal logging with the log level.
resources. We just had recent work with resource detectors, so same story as limits.
the YAML parser can parse all the YAML for resource detectors and understand that. The next part we need is to actually implement resource detectors in the SDK and use them.
I think we have a process resource detector so far, but we might be missing others.
**Tom Tan** 47:04 Okay.
**malff** 47:09 And yeah, this is the… the main code, you… You pass a file, you get, a representation of SDK.
So anyway, that was a sidetrack, but bur amazing parties.
all the contribution we have so far, I mean, not all of them, but a lot of them are related to the YAML parsing area.
Oh… It seems to be a… A part which is, interesting to people to contribute.
Maybe more than fixing bugs in some deeper, doll carriers, or other things.
**Tom Tan** 48:04 So, this means, does this mean that the YAML config can… could work across language, right? Like, for different languages, the same… YAML configure can become…
**malff** 48:17 Yes, this is the whole point. The same config file should work with different SDKs in different languages.
**Tom Tan** 48:24 I see, huh.
**malff** 48:25 This is why there is a schema which normalizes the name of nodes, attributes, your meaning of them, everything.
**Tom Tan** 48:37 Okay, got it.
**malff** 48:43 Which, by the way, reminds me that Lalit needs to do this thing in Rust.
**Tom Tan** 48:48 Here, I haven't heard about any.
Progress on this in Rust.
**malff** 48:53 Yeah, I know, because this thing is done in Java, in JavaScript, in Python, Maybe overs, I don't remember.
But not every SDK is, is supporting YAML config yet.
**Tom Tan** 49:10 Okay, yeah, I think that's… that will be something for Nalid to explore.
**malff** 49:15 Yes, I know.
Okay, I don't have anything else special to discuss, I think… let me check my notes.
If we can find them… Oh yes, one thing with dependencies, I don't know why.
We have quite a few… Renovate PRs.
Which are stuck, like, for protobuf, gRPC, and AppSel, I think.
Murcisi and Absalom?
So… this thing is, you know, it's… this thing is automatically generated by Dependaput to obligate dependencies.
And it's failing in CI, even though I don't know quite why exactly.
Sorry.
So this one passed, but others like, Upsell and gRPC are failing, so… I don't know… If a failure is due to our code, or if we need to adjust something, so we need to investigate.
Oh.
maybe we should upgrade, like, gRPC, Porto, and AppSear all together at the same time, which is possible, because there are some interdependencies there.
But the… The bottom line is, we should try to To stay up to date with dependencies, otherwise we have the risk of footing behind.
And not get bug fixes or security fixes from all those third-party things.
So… I'll try to investigate what's going on there, and… back to my comment, the… some dependencies are moving fast, the rapid YAML code itself, the parser for Rapid YAML, I just recently made a few releases with bug fixes, so we recently upgraded, and we need to upgrade again, because it moved again.
**Doug Barker** 51:42 So this only… the Dependabot only works for… Bazel, should we look at integrating Renovate and using that? Because I think that one we can actually customize some parsers, so potentially to get it to upgrade the dependencies from our release, third-party release, this text file.
**malff** 52:02 Well, I guess… when… so, yes, Renovate… Dependable works with, with Bazel files, so whenever… dependable detect that an upgrade… something can be upgraded. I think at the same time, we can adjust the… the third-party files for CMake at the same time.
What's missing so much is the notification that something is changing. The grid itself is a few lines in a few files to adjust.
So I don't know if it's… if… if it's… if it can be, and if it can… Can you, automated in such a way that it will always work, or if it needs manual adjustment once in a while, not… I've not been, working in this area too much.
**Doug Barker** 52:54 Yeah, that's a good question. I saw some other projects you didn't renovate. I looked into it briefly, because I'm manually updating a third-party file every release, but maybe that's a reasonable thing to keep doing.
But if it could be automated, that would be better.
**malff** 53:11 Yeah, if we can, sure, why not?
**Doug Barker** 53:16 One thing about the gRPC I notice is that, they do tend to lag behind the protobuf and probably the AppSil versions. So, like, 1.8.0 doesn't… pull in the latest protobuf, so that might be what's happening here, because I think Dependabot is just grabbing the latest from all the different dependencies, but they don't correspond to, like, what was actually released with gRPC.
**malff** 53:40 Yeah, it could be.
And also, DependAbout sometimes is confused by… well… it's… it's suggesting some upgrade, with things named RC1, RC2… And so forth.
So… Probably you just want to wait for the official release, not, intermediate things.
But in that case, we just ignore it.
So, yeah, just to say that I will try to keep an eye on that, too, so that, Our dependencies don't fall behind too much.
And another reason for that is that internally, we are also upgrading Polobf Two more recent versions, and It's… it's always… because of so many dependencies from so many places, it's, We have our own code that depends on protoperf, and then we have a telemetry code that depends on protoperf, but of course a different version.
So, trying to upgrade all that to something recent is also, More painful if some parts of the code is already behind.
So it's a good incentive to keep it up to date as well.
Okay, I think that's it for me, I don't have any… any other things.
Tom and Doug, you have any…
**Tom Tan** 55:33 Wow, that topic's so much sad.
**Doug Barker** 55:34 Yep, nothing for me.
**malff** 55:37 Okay.
So I think we can… we can close the call, because, It's getting late here, as you can see in my… on my screen in my clock, so…
**Doug Barker** 55:47 Very…
**malff** 55:49 Okay, so thanks for joining, and thanks for the discussion.
**Doug Barker** 55:54 Thanks for that.
**malff** 55:55 Good night, everyone. Well, a good day, Mark. Good day, everyone.
**Tom Tan** 55:59 Have a good night.
**malff** 56:00 Yeah, bye.
**Tom Tan** 56:03 Bye. Bye, Tucker.
