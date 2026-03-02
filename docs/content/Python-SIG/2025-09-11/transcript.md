SIG: Python SIG
Date: 2025-09-11
Duration: 51 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 04:28 Hello, everyone.
So welcome, everyone, to this week's Python Weekly Sq call. In the meantime, we'll wait a few more minutes for more people to join. Please add yourself to the meeting notes, and I'll share the link.
In the chat, if you don't write.
So…
And… of course, if you have any topic you want to discuss, please add it to the topics too.
Okay, I think we can start.
Okay, first topic will be really quick. I've released… utterly's,
This morning, in my time zone.
Yeah, it is out, at some troubles.
Doing an eddies, as always.
Everything, like, was… Like, not really outdoors all, but anyway…
Some fun things, like, we had some failures, because the configuration for the, discussion was different between country and car.
And for some reason, contribute announcement category was, like, locked for maintainers.
And so, the…
the token we're using in CI, was not, did not have maintenance right, of course.
Then another one was that the newly added OpenTeametry UT region AI package was not listed in the one to exclude when doing the
The release, because it should be, like, released, independently of the… The various, other packages.
And also, it is, the… the,
restaurant… how it's called, RST…
text in README was not, correct, and so it did fail at uploading at PyPI upload time.
And we already had an issue, I've assigned it myself, because this is, like, the second time I have this issue doing release, so I want it to have it fixed.
But other than that, everything's fine, yeah.
**Aaron Abbott** 09:55 Yeah, I think that one, too, we should probably just add, like, a CI check.
**Riccardo Magliocchetti** 10:00 Yep.
**Aaron Abbott** 10:03 So, so I didn't, I didn't quite follow. Is the OpenTelemetry Utiligen AI, not an independent release?
Like the other genetic packages.
**Riccardo Magliocchetti** 10:15 It is, but it was missing, an exclusion rule inside the… what's it called? ScriptsBuild.sh.
**Aaron Abbott** 10:26 Okay.
Cool. Well, thank you for dealing with that, I know.
**Riccardo Magliocchetti** 10:31 Yeah, true.
Okay, I'm gonna think we can go… well, a new release is out, please test it out, and let us know if there are any issues.
Okay, next topic is also for me, from me.
And… yeah. This morning, again, I refreshed a bit my PR event tree before adding an OPMP client. OPMP is a protocol
specified inside OpenTelemetry for doing remote configuration and… Stuff around it.
So… yeah, if you have time, please take a look, especially if you are interested in remote configuration.
And… just, like… This is just, like, adding a patch… a packaging country, because,
it should be used by distros at the moment, because, like, OPMP is not… specified, like, the…
the things we can configure in SDKs and stuff like that is not specified, and so, like, there is no risk if you don't use it.
But, again, if you… like, if you've had time, please take a look.
And… yeah, this one. Also for me, next topic.
And… yeah, like, I think we should really start to merge the… the various PR we have ongoing.
But they're introducing, like, breakages, or… like… Moving us forward in…
Making the logs implementation compatible and supported.
Yeah, Arrow?
**Aaron Abbott** 12:28 Yeah, I was gonna say, thanks… thank you for raising this,
I would also really like to make some progress on this, but…
I feel like we've had a couple discussions on specifically, like, breaking changes.
And that's kind of led us to indecision. So, I was wondering.
First of all, I think we still are planning some breaking changes, is that right?
**Riccardo Magliocchetti** 12:55 Yeah.
**Aaron Abbott** 12:58 Click.
**Riccardo Magliocchetti** 12:59 We are for sure some PRs, but rename, class's name, and…
change the shape of things, so… yeah. Yep.
**Aaron Abbott** 13:10 Okay, so with that in mind, I was wondering if people here could, you know, share your opinions, especially as, like, a user.
I think I'm a little bit torn on how to do this, so there's this sort of…
Put everything into one breaking change, try to minimize the number of disruptions, versus
Do, like, you know, deprecated release.
Remove something later on and have, like, a trickle of these changes.
Which, you know, while making the small individual changes for users are smaller, it kind of creates distrust that
We're gonna keep breaking things, so… Yeah, Marcella, please.
**Marcelo Trylesinski** 13:53 Yeah, I mean
I guess I raised this some months ago, about not having a way to deprecate the version of packages that we support.
But on this specific topic, if there is no policy around it, I think it's better to… first, you add a deprecation warning, where on the… on the warning, you actually tell when…
it's gonna be removed. It makes… the less confusion.
**Aaron Abbott** 14:24 Yeah, and just to be clear, do you mean, like, a date or a expected release number?
**Marcelo Trylesinski** 14:30 I left it open on purpose, but since the releases are usually not
Well, they don't bump much stuff, you know, like, it's always… it's always, what, minor? What?
I would put a date or something.
**Aaron Abbott** 14:46 Yeah.
**Dylan Russell** 14:49 At least for some of the changes, we're not, like.
deprecating things? We're, like, breaking things.
Like, we're changing the names of things.
So, do we still want, like, a deprecation warning, be like, heads up, we're gonna, like, change the name of this thing?
Like…
**Aaron Abbott** 15:08 So, I mean, for renames, it's pretty straightforward. We could do, like.
You know, slap a deprecated on it, and then…
keep that as a reference to the old thing. It's mostly,
You know, like, a backward-compatible change, and then people will see the deprecated thing and move it.
I think there were… by… to your point, I do think there were some, so we had, like.
We were considering really changing the data model for the logs export.
And then even we were talking about having logger.mit accept, like, keyword arguments instead of
like a data class or a struct with the stuff in it. So, those kinds of things are a lot more…
Disruptive, but we could, you know, we could definitely consider, like.
If it's worth putting the effort into…
deprecate it smoothly. We could… we could do it, it's just gonna take some effort.
**Dylan Russell** 15:59 Yeah, it's a lot more work.
**Aaron Abbott** 16:02 Yep.
Oh yeah, John.
**Marcelo Trylesinski** 16:08 I don't think… sorry, I don't think that's how the ecosystem does, in general, if… You care about users.
**Dylan Russell** 16:18 But it's, it's… it is, it is… we underscored everything, right?
It's an alpha.
We put under.
Hmm.
**Marcelo Trylesinski** 16:27 We were talking about private APIs?
**Dylan Russell** 16:30 Like, the law…
**Aaron Abbott** 16:31 the logs.
**Dylan Russell** 16:32 Yeah.
**Aaron Abbott** 16:33 Go ahead, sorry, Dylan.
**Dylan Russell** 16:34 Yeah, the logs, we put an underscore in the logs package path.
**Marcelo Trylesinski** 16:39 Then it's fine.
Well, hold on, it's fine… no, it's not fine for us. It's not fine for us. We do use it, yeah.
**John Scancella** 16:53 Sorry, I was just gonna say, you know, like.
for me, as just a casual user, right? Like, I, in the past, have had really good luck using something like Open Rewrite to do, like, hey, major
version changes, where, like, that automatically says, oh, this thing got renamed to this other thing, or whatever, and, like, it just goes, updates my code, and then, like, I can see…
you know, hey, git diff, like, what change? And, like, see if there's any, like, glaring, obvious things. Like, that, to me, is much more palpable
for, like, big disruptive changes, if, like, there is some sort of, like, hey, we know there's these big disruptive changes, you have to make these sort of things, here's an automated way to do that.
So, I guess that was just my comment. Like, if there's an automated way that you can say to people, hey, yeah, like, there's gonna be breaking changes, but just, like, run this, and it should
do most of the work for you. I think that…
That really helps, you know, by, like, goodwill.
**Aaron Abbott** 18:00 Yeah, that's really interesting. John, is this what you were talking about? Open rewrite, you said?
**John Scancella** 18:05 Yeah, open rewrite. I've used it, so, like, for instance, like, when I moved from, like, Java 17 to Java 21, and it just, like, it even did niceties, like, oh, you're using this old syntax style, like, hey, like, go ahead and, like, we'll just change that for you, you know, and get… let you see, here's what the new syntax should be.
**Aaron Abbott** 18:25 I see.
**John Scancella** 18:26 So, really nice things like that.
**Aaron Abbott** 18:29 Okay, so this is something that… it's basically like a script… it provides, like, a way for users to transform their code pretty easily.
**John Scancella** 18:35 Yeah, from what I understand, behind the scenes, it builds an abstract syntax tree, and then, using different rules that you define, it translates it to a new abstract syntax tree, and then rewrites out the code.
**Aaron Abbott** 18:50 Okay.
Yeah, it seems… it seems like this one in particular is Java-specific, but I definitely… I like this approach. I'm a little unsure if something like this exists in Python, just because…
It's a much harder…
**John Scancella** 19:05 In general, open rewrite is language agnostic. Like, I know they have ones for, like, JavaScript. It's… the Open Rewrite is, like, the free open source part of Moderna's, like, paid offerings for doing a whole bunch of migrations. So it's not just Java, I do know that, but.
**Marcelo Trylesinski** 19:25 Like, I don't know what the process is for writing your own, I just know that it's possible.
**Aaron Abbott** 19:31 Gotcha.
**Marcelo Trylesinski** 19:32 Yeah, but I think what is annoying is, like, for example, we have a package that is on top of OpenTelemetry, and then I have my user that, is spinning.
the package, but then… Not pinning the underlying package, like OpenTelemetry. And then…
what's gonna happen is that you're gonna break the user experience, because actually there is expectation that OpenTelemetry packages will not break any code, I guess.
Great.
**Aaron Abbott** 20:13 Ricardo, you wanna… go ahead.
**Riccardo Magliocchetti** 20:15 Yeah, but… like, I don't think that…
For the casual user, it will cause… like, the renaming of this stuff will cause much… Issues?
like, I'm worried about, like.
Libraries on top of frameworks on top of a telemetry breakage, or distro code, because, like.
I'm pretty sure that the Azure distribution has a, like, does not have,
affixed dependencies on the OpenTremity version, and so we already caused them regressions.
And… yeah.
Yep.
**Aaron Abbott** 21:01 I mean, Marcel, maybe you could speak a little bit to the usage, like, of the logs API and SDK that you guys have, because, like, to Ricardo's point, it's mostly… like, mostly people are using different loggers in their actual code. It's probably only instrumentations using the logs API directly.
**Marcelo Trylesinski** 21:21 Yeah, I think… well, I'm not exactly sure how we use it.
But I know we have logic where there's,
Well, I know we are using it, the internal API anyway. Like, the private.
So…
**Aaron Abbott** 21:37 Okay.
Do you, by any chance… Sorry, go ahead.
**Marcelo Trylesinski** 21:41 Yeah, it broke before, I remember, on one of the releases, so… You can ask something.
**Aaron Abbott** 21:49 Yeah, I was gonna say, do you all…
In the SDK version, in your… in your dependencies.
**Marcelo Trylesinski** 21:56 No, we do not, do not pin.
**Aaron Abbott** 21:58 I mean, just the minimum.
Yeah. So, I think what I'm really hearing here is that the underscore thing is not…
Not sufficient for what we were intending it for, like…
just because it's in the same tree as the rest of the OpenTelemetry SDK, it's…
And it exists, people start to take it as de facto.
Stable thing, and we need to be careful here.
**Marcelo Trylesinski** 22:25 Yes.
But,
I mean, I would say that this is not the same as the other Python packages, because given the nature of
being an observability package, then you actually expect this to not break other stuff.
So… I think it's useful to have a bigger discussion on how to deprecate and remove stuff, and
Like, in general.
**Aaron Abbott** 22:54 Yeah, and just to be clear, like, I… if we're deprecating something that's stable, like, say… say, for example, in the…
in the OTEL API, we have some… something in metrics that we want to deprecate, like, absolutely, we're gonna…
we're gonna do deprecation warnings, say, we'll remove it at this point, and all that stuff. This is just…
I think we're purely talking about the logs, which has been kind of in the development stage, but it's been, like, 3 years, so people will start to rely on it as a stable thing.
**Marcelo Trylesinski** 23:21 Right. I mean, I also understand that there is this conceptual thing that everybody… well, at least on the numbers, you believe that it's experimental, but everybody uses it.
Even if it's… Yeah, absolutely. Like…
Doesn't matter, people are gonna get frustrated.
**Aaron Abbott** 23:36 Yep.
Okay, so maybe, in the interest of time, like, does anybody else want to share their opinions on this? I think…
Dan, like, our GC rep, was really helpful in kind of raising this and all that, so if other people, especially, like, from a user perspective, anybody here wants to share, please do.
**Riccardo Magliocchetti** 24:05 Yep.
**Dylan Russell** 24:07 What about, like, because eventually you want to remove the underscore from the… the folder.
That's just gonna break everyone, right?
No.
**Marcelo Trylesinski** 24:20 Not necessarily. I mean, you can just edit the packet, like, the module without, and then you import everything on it.
**Dylan Russell** 24:26 Yep,
**Hector Hernandez** 24:29 Yeah, but the moment you make these logs API stable, you can just break as much as you need. You can do all this cleanup and everything, right?
I think the problem…
I think we want to push for this to happen soon, right? So, the… I think the strategy of having multiple break-inch changes at the same time, but letting customers know, okay, this is the actual thing that we changed, so they can easily remediate or use these kind of tools that people were talking about,
will be helpful, but we need to make these changes, right? To move… to move this forward.
**Aaron Abbott** 25:14 Yeah.
I mean.
I don't know if we need to make breaking changes, like, I think…
There's a couple things that don't follow the spec, but if you squint hard enough, most of them do follow the spec.
like, I would love to clean it up, like, I would like to, you know, remove all the stuff that doesn't make sense, historical stuff from 3 years, but…
It's just, like, a cost-benefit thing, I guess. I mean, Hector, what did you have in mind? Was there anything… because you have that PR out, I think you have good perspective here.
**Hector Hernandez** 25:49 Yeah, sorry, can you repeat the question?
**Aaron Abbott** 25:52 Yeah, I was wondering, like, in particular, which… which breaking changes…
Are… like, from a cost-benefit perspective, you think they're worth…
Making the breaking changes before the release.
**Hector Hernandez** 26:04 Well, most of the changes I'm making are because… to align to the spec, right? We have this review.
That Loadmilla helped us create a bunch of issues, basically, to go through the… our implementation for locks.
And this… my understanding is that we need to just make these changes in our APIs and SDKs to be able to mark this as stable. So it's just following the process. It's not that I need these changes, right? I just… for us in Azure side, what we really care is to have this stable, because customers…
don't want to be using these alpha versions in their code, even if… there's no way around it right now, right? But, this is a concern for us. Breaking changes, that's something that we're… we're prepared for them, because we know we're introducing the breaking changes, so we understand
And we basically patch our code immediately after release.
But some other people that are not aware that these breaking changes are happening definitely are going to… to have some issues, right?
**Aaron Abbott** 27:13 Yep.
Okay, so I don't… I don't know if we… if we're much closer to answering the original question, but, Ricardo, do you wanna… this was your thing, and I think we've taken a lot of time, so if you wanna…
**Riccardo Magliocchetti** 27:34 Yeah, I think probably we should… Like,
Maybe, or do a specific call about this. Or, yeah, at least, like, try to be, like, next time I'll try to…
you know, list all the PRs making changes, so we can evaluate Maureen. But we can do this offline, like…
So Bobby can share, like, all the…
the up-to-date PRs we have regarding logs, and we can evaluate,
Water break, water depicator, and then we can probably have them,
A more, you know, informed opinion about this.
Okay, so I'll try to wrap our stuff in and share in the Autel Python channel before next week.
That sounds good. Okay.
Then we can move to the next topic.
From Keef?
**Keith Decker** 28:42 Hey guys, so, This is our first…
PR around inference for the GenAI utils. It covers starting and stopping LLMs and emitting, span.
attributes around… Those, we…
from last week, we pulled out metrics and logs in order to get this PR down in size to get much more eyes on it, so just looking for more feedback around it, and…
What's on.
**Dylan Russell** 29:24 I'll definitely take another look at this.
Yeah, thanks for making changes.
**Aaron Abbott** 29:36 Cool. Yeah, thank you, Keith. Yeah, let's just keep the line, since I think…
This is a hot topic. There's, like, a lot of concurrent work.
So, thank you for raising it.
**Riccardo Magliocchetti** 29:53 Okay, so thank you, anyone?
And… okay, next topic is from, Ridima.
LLM stuff again.
**Ridhima Satam** 30:07 Yes, yeah. Thanks, Ricardo and Aaron, like, you have given a good amount of time to review this PR. I think there is this last comment pending from Aaron.
If you can just scroll down in the end…
Oh, I think it's just down below, if you just expand that load more thing.
Ew.
So, here we are adding the telemetry. I hope I understand, like, you are asking about when we are adding the telemetry, and we spoke about this briefly last time.
About adding that flag in the context API.
Is that what you're asking here? And if that thing we spoke about, that we can add it in the Gen AI utils when we are actually generating the telemetry there.
**Aaron Abbott** 31:04 Yep, yeah, that's right. I was mostly just asking if we're planning to do it before or after,
I think my preference would be before releasing this package, for sure.
So if you can, like, if you want to do it after, let's, you know, just make a follow-up issue or something like that, and add a to-do in the code.
Just for tracking.
**Ridhima Satam** 31:28 Oh, okay.
**Aaron Abbott** 31:30 Yep.
**Ridhima Satam** 31:31 Yeah, okay then.
I'll just add the issue then, if that's okay with you.
**Aaron Abbott** 31:39 Okay. Was there anything else on this PR,
Like, I think I could take another… another pass, but it was…
I think the scope is… is clear and good to know.
**Ridhima Satam** 31:52 Yeah.
Yeah, that's all from my side.
**Riccardo Magliocchetti** 31:59 Okay, thank you.
Next toppings from Pawan.
Sorry.
**Pavan** 32:10 Oh.
Yep. Hi everyone, so…
I won't take much time. I mainly, you know, have been attending a lot of the semantic convention SIG meetings. This is the first time in Python. And, you know, as a part of Cisco, I think we are generally trying to
improve how developers, you know, instrument their, like, GenAI applications using the OpenTelemetry Python SDK. And, given the fact that, you know, there are, like, lots of different frameworks, lots of different providers, and it's sort of hard to have
like, sophisticated, you know, instrumentation for each one of them. We wanted to also have an alternative way for, like, developers to
let's say, import decorators annotate their code, and also ensure that the, you know, semantic, convention-compliant
telemetry, is emitted, to their respective hotel backends. And even though we have a PR out, but essentially, we just wanted to sort of harmonize
and, you know, like, generalize the concept and see if, you know, if you had any comments, thoughts before we brought up the POC. And, you know, after that, maybe we can open a PR, but this was generally aimed to see if
if this approach… I don't know where it'll go, maybe it could go in…
GenAI utils, you know, or it could be, you know, in a different place, not sure, but hopefully this could be sort of a framework or provider-agnostic way of not just emitting LLM-based, you know, spans, but also agents, because agents, as you probably know.
are, you know, rising in popularity. Many are sort of, you know, trying to.
developer agent, you know, in Python, and OTEL stands as a best solution to sort of observe and emit the traces, or rather, you know, have observability for their application. So, you know, agents, specifically, they aren't tied to any single framework, and from experience, I think
Agents could be developed as a method, it could be, you know, sort of developed as a class in Python, for example, so doing an auto-instrumentation of agent, for example, or tools, for that matter, is sort of generally hard because, there are, like, sort of no, easy way to sort of either do, monkey patching or, like.
sort of having callback handlers, you know, for those, because it's not, like, easy… it's not similar to NLMs, for example. So, having this alternative approach where decorators could be, you know, imported and added to their code, where it'll do its best job to probably
figure out, you know, what fields it could extract from the input-output, and then, you know, try to ensure semantic convention-compliant telemetry is emitted. I think
could be, an interesting way. So just wanted to get this thought out there and…
See if there were any initial comments.
Yeah, so good.
**Aaron Abbott** 35:54 No worries, yeah. This is great. Thank you for sending the doc, because I think it's… it makes it pretty clear, and I'll, I'll try to take a review, and maybe leave some comments, but yeah, like, I think this is great. It seems pretty similar to what Keith and Dylan are working on for the LLM invocation capturing, right? Like,
Have some kind of helpers or general thing to make the instrumentation easier, because it's actually pretty error-prone.
So I guess,
this seems more like a… less like something that the monkey patching instrumentations would use, or maybe in addition to that, it's something that, like, people would embed in their code and use as an instrumentation API, is that right?
**Pavan** 36:35 Yeah, correct. Generally, it wouldn't necessarily replace, you know, like, the existing auto-instrumentation approach, but rather, we could see both of these are sort of complementary to one another, where, you know, it would sort of
You know, come in when auto-instrumentation doesn't necessarily capture a lot of the details.
**Aaron Abbott** 36:59 Yep.
Okay, so my… I just, like, I want to let Marcela go, but my two kind of high-level things would be, first, it's kind of hard to do decorators with… because you have, like, these four variants that we see, so you see, like, streaming, non-streaming, async streaming.
async non-streaming.
So with the decorator, you kind of have to handle all those cases, which can be… Kind of tricky.
And then the second thing was, a big part of the agent conventions is, like, the conversation ID.
Which is… not static. So, like, you have name, description, the kind of static stuff on the decorator parameters.
Do you have… like, does this design cover, for example, if the conversation ID is passed
as a parameter of the function, or something like that. You can annotate it, or put it in a context key, or something like that.
**Pavan** 37:50 Yeah, no, that's a great point. I think we were starting to look at the conversation ID next, but we do have some thoughts on that, but definitely, along the process, we can actually figure out, you know, if it needs to be passed in statically as a parameter, or it could be inferred somehow.
I'll sort of kept, you know, keep it for the entirety of that, conversation.
But, yeah.
**Aaron Abbott** 38:19 Okay, yeah, I'll… limits.
**Pavan** 38:22 Sure, sure, yeah, that'd be great, thanks.
**Marcelo Trylesinski** 38:28 But who'll be the user of this?
Because if… if I have instrumentation, or, like, automatic, like, the normal instrumentation for a specific package, then…
Why would a user would use this?
**Pavan** 38:48 Even, you know, having auto-instrumentation, for example, let's say OpenAI package or, like, Langchain package, it does cover the, LLM
you know, callback handlers well, meaning you are able to sort of figure out when the LLM operation starts and when it ends, but when you go into the other GenAI types, like agents and tools, that's where it sort of becomes hard, unless, of course, the library that you're auto-instrumenting, like, for example, LandChain.
Covers that signif… like, you know, on their part.
We, as the instrumentation libraries, won't be able to, like, capture, you know, what was some of the fields that we wanted to do.
as a part of the agent invocation, because in semantic convention, there is, like, agent name, agent description, agent ID, and other things that we want to capture, but there's actually no way for us to actually do that reliably without explicitly the user passing that information for, to us. And I can see that, you know.
the agentic semantic convention is just growing day by day, so we need to, like, sort of find a way to reliably gather that information. And as a part of building agents in our, you know, day-to-day job, we find that, you know, it could be a method, it could be a class, so there are, like, various ways to instantiate an agent, for example, so…
We feel that, you know, a developer could simply annotate it, and we'll do the best effort of capturing all those information reliably. You know, the decorator, at least, will do that. I don't know if I…
Answer that question correctly.
**Marcelo Trylesinski** 40:39 No, but then the point you said is just this will be useful for packages that do not have more instrumentation
Alrighty.
So it will be useful for packages that are not that used.
**Pavan** 40:55 it'll probably be used for almost, like, all. For example, land chain as well. I don't know if it gives us the ability to attach callback handlers to, like, agent start and agent end methods, tool start, tool end, and things like that. So, if we are to capture those information.
I wonder if, you know, like, the decorators are, at least the best solution to do that, because some of them needs to be explicitly provided by the developers themselves, because auto-instrumentation can't reliably capture all of that, because it lacks the inner, like, knowledge of, like.
How the inner working is, you know, of that particular you know, method, or…
Class, for example.
**Marcelo Trylesinski** 41:47 I mean, again, like, this is just a span with some information that you're adding on top of it.
But then…
it seems you are missing a lot of information from inside, right? On this decorator, for example, the one I'm seeing, agent, name, description, you could just have
Creating a spam out of this.
**Pavan** 42:07 I… My point is… yeah.
Right.
**Marcelo Trylesinski** 42:12 My point is still… I'm not sure if it was answered by what you said, but…
If the package that you're using
is popular enough, which I think OpenTelemetry covers the most popular.
Agentic packages, then you'd already have this kind of…
Instrumentation underneath. You don't need to go and add those. That's my point.
**Pavan** 42:41 I don't think OpenTelemetry at least covers any agentic,
frameworks. Like, you know, if you take out Langchain, which Langchain is like a general purpose, you know, library that does all, everything under the hood, and we do support Vertex AI, we support OpenAI, but they are mainly for LLM invocations, but, some of the other Gen AI tools are sort of
at least in my view, I didn't find, like, you know, the sufficient instrumentations for that in the SDK. So, like, the thinking from
us, was that we could probably, do this, you know, or rather provide this as a way to, you know, capture those info,
Yeah.
**Marcelo Trylesinski** 43:32 But I think… I think it's a matter… but then you said, the writing. I think it's a matter of the… if the package is popular, then… it's a matter of package. It doesn't matter if it's a genetic package or not. Like, if you have a package that's popular, then you contribute to instrument, package name into…
in the instrumentator, package in OpenTelemetry, isn't it like that?
I mean, go ahead.
**Pavan** 43:57 It could… yeah.
**Aaron Abbott** 44:01 Up.
So, I think… It sounds like the… we need some more scoping on this.
Like, which… who's the target for this?
**Pavan** 44:13 Yeah, okay, okay.
Let me do that.
**Aaron Abbott** 44:19 Yeah. Yeah, one other thing I was gonna say, I think there is, like, this content capturing, there's, like, environment variables for that.
there's a couple things that are tricky that we could add in. I think for agents, the conventions are pretty new. For LLM calls, there's, like, a lot more to it, so I think having, you know, having something that's typed, that people implement, and they know if the type's passed, if they have the correct instrumentation, I see value in that over just using, like.
the start span, or start his current span decorator here.
There's also, like, metrics and stuff like that, too, so… If we capture Agent Invacation,
metrics here, too, it would be helpful, but… I'm not saying to expand the scope, I think just saying what's in scope would be helpful.
**Pavan** 45:06 Okay, okay, certainly.
I'll, I'll add that info, to this doc.
**Riccardo Magliocchetti** 45:22 Okay, thank you.
Any other comment?
Okay… let me move to the last topic for today, from Tammy.
Or that's be honest.
**tammy.baylis** 45:41 Yeah, thank you. Not Gen AI-related. I have more docs, updates, PRs out. Please have a look. I think it's…
increasingly important that we document what the instrumenters that support SQL Commenter are doing, because it's now part of the SEMConv. One is just to update the read the docs for
the DB API kind of shared util. Thanks, Eric.
And, the other is to add a new, core repo docs example,
SQL Committer's not implemented by the core SDK, but I think it's a fair place to put this, because there is a Django example in the core repo as well, so… yeah, let me know, and if these look okay, there's others that I'd like to submit later.
**Riccardo Magliocchetti** 46:38 Okay, thank you.
Any last new topic or comment?
Okay.
And then Thanks, everyone.
And see you next week.
Thank you.
**Aaron Abbott** 47:10 Yep.
Thank you, everyone. Later.
**tammy.baylis** 47:12 Thanks, bye! Thank you.
