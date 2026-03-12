SIG: Java SIG
Date: 2025-11-06
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

GZ Gregor Zeitlinger 00:00:37 Test… Can you hear me?
John Watson 00:00:49 Yes, can hear you, Gregor.
GZ Gregor Zeitlinger 00:00:52 Thanks!
Trask Stalnaker 00:01:20 Surrounded by Jays.
Another J.
JP Jason Plumb 00:01:28 The best letter.
John Watson 00:01:32 We have to turn Gregor's name into Gregor.
I guess if it's German, it would be Jureger. Jureger.
GZ Gregor Zeitlinger 00:01:41 That's right.
John Watson 00:01:48 I could just go with Johan, he'll fit in just fine.
GZ Gregor Zeitlinger 00:01:51 Yep.
Trask Stalnaker 00:01:52 You look like a Johan.
GZ Gregor Zeitlinger 00:01:56 Yes, that's a compliment!
JP Jason Plumb 00:02:10 It's a packed agenda.
Trask Stalnaker 00:02:21 Alright, let's get rolling, then.
Car repo release is tomorrow, right?
Jack Berg 00:02:31 Yep, and I guess… I can take that responsibility back over.
Unless anybody really wants to keep doing it.
Trask Stalnaker 00:02:43 All yours.
JP Jason Plumb 00:02:44 Yeah.
John Watson 00:02:45 Much appreciated, Jack.
Trask Stalnaker 00:02:48 Can I milestone this one?
Jack Berg 00:02:51 It look… like I said, it looks good to me. I know some other folks had some comments on it, Does anybody feel strongly enough about this to block its merging?
what would be the reason why this would matter to block? It's, you know, it's still experimental, so it's not part of the public API, so breaking changes are allowed, but it's still, it's used in a lot of places, and so churn is impactful, even though it's allowed.
Trask Stalnaker 00:03:26 Yeah, I thought this was interesting, like, your, SPIs, because part of… I was guessing one of the reasons why auto service fails so badly with Generic types is that SPIs, I mean, essentially aren't type-safe.
Anyways…
Jack Berg 00:03:49 Right.
Trask Stalnaker 00:03:53 Which was part of my… I didn't feel too bad about removing the type safety, since it was kind of fake anyways.
But this is… yeah, I am curious.
Do people use our DAOs, like… loaded via SPI?
Jack Berg 00:04:17 I think in some cases, yes. I'm most familiar with using Spring's dependency injection mechanism, and that's not SPI-based.
But I was seeing examples on the internet where, you know, they were loaded via SPI in, like, you know, worms and things like that.
And, yeah, I guess I was just surprised by it. I think there's a lesson in here for us, which is like, hey, don't add generic types to any of our SPI interfaces. And I guess we haven't come across it before, because nobody tried to write a SPI for us that was generic yet, but Yeah, I guess we shouldn't do that going forward.
Trask Stalnaker 00:05:06 Cool. Not urgent, but I know Lori and I would both appreciate it. We both have gotten bit by that a few times.
Jack Berg 00:05:17 So if there's no dissenting comments, I'll go ahead and merge that.
Trask Stalnaker 00:05:27 Looking forward to next, we… release… oh, I think I saw Lori… oh, yes, okay.
So… I am looking at… I kind of want to try, as this… part of this effort of Broader effort in OpenTelemetry around stabilizing things.
We're trying to push these… forward… I think this one is pretty, it was actually pretty much… Ready, except for… One thing that Lori has raised… Which… I did a little research on… So the idea here is that in some cases.
Well, actually, in most cases, our attributes extractor, our instrumenter, generic parameters are… use the underlying framework classes directly, like, this is the, response.
But, in some cases, we wrap it.
Because we need to pass some extra information along.
And… So, we wouldn't… once we're stabilized, we wouldn't be able to… Add, this is more limiting, or this is limiting.
Us, versus with wrappers, we can always add more Stuff more things in there without breaking… Most of these were… let's see… wrapper… I'd say most of them… we were only using wrappers in, it looks like, about 5 places? 4 places?
So, I think my… I was thinking… And we haven't needed it, so I was thinking it might be okay just to go with the… Not wrapping… And then we would have to do, you know, major version bump if we ever needed that.
But I'm not opposed to wrapping everything Out of abundance, out of… caution, also.
There's a very small amount of overhead to wrapping, I don't know if that… really, probably, doesn't… matter that much, given it's fairly coarse-grained, it's a full HTTP request.
Cycle that we're adding You know.
A sing… a rapper.
JP Jason Plumb 00:08:51 It seems like a good idea to wrap those.
Trask Stalnaker 00:09:02 Cool. Bruno?
As a downstream consumer, And someone who cares about Us not breaking things.
Do you… would you prefer that we wrap them So that there would not… Be, like, for consistency, and that we wouldn't be changing that.
Later…
Bruno 00:09:31 Hello?
Trask Stalnaker 00:09:32 Hey.
Bruno 00:09:35 I don't think it will be a problem for me.
Trask Stalnaker 00:09:42 Either way.
Bruno 00:09:47 Hmm…
Trask Stalnaker 00:09:48 Do you expose attributes extractors? Like, can Quarkus users customize… Add their own…
Bruno 00:09:58 No, we don't.
If they want to add customizations, they need to call the low-level API.
I get the span and set the attributes as they… as they wish.
Trask Stalnaker 00:10:16 Cool. Well, why don't I, Give that a shot, wrapping, and see what that looks like.
Lori… I… are you… do… Prefer the wrapping.
Lauri 00:10:38 Well, I don't feel that strongly about it, I think. But, if we don't wrap.
I guess it could limit our future possibilities.
Maybe we are overthinking this stability thing.
That's, it's definitely… It feels scary that you take on a responsibility not to change some pieces of code, and when you need to change them, then you're kind of screwed.
Trask Stalnaker 00:11:12 One thought I had was, I mean, if we were going to wrap everything… What was the point of the extractor… Right? Like, isn't the point of the extractor architecture design to be able to extract from Framework classes directly.
Because if we were gonna wrap, we could… Have just implemented all those getters… In the wrapper interface?
I wish we had Anurag here.
Lauri 00:11:59 In ConoRock's original design didn't include the getters, those were added by Matthias later on.
JP Jason Plumb 00:12:05 Yeah, Mateuszh did all that instrumentation API stuff.
Lauri 00:12:11 Well, of course, I could be misremembering.
Trask Stalnaker 00:12:29 Alright, well, we got a lot on the agenda, let's move on… Oh yeah, thanks for… on the database, semantic conventions, thanks, I saw there were some reviews, on those, I'm hoping to kind of move that forward in this release.
Gregor.
GZ Gregor Zeitlinger 00:13:00 I know it says Global Hotel, but I don't want this to take the entire time of the meeting.
So, I was not able to answer the question in this poll request about, whether a global hotel is, active.
And, this is disregarding whether it's a good use case of Global OTEL. Because it's in spring, I'm not totally convinced, but, Still wanted to give it a good answer, but I couldn't.
So there is a code snippet where they try to find out if the global hotel is set by comparing it to no op, and that doesn't work because it's obfuscated.
Jack Berg 00:13:54 Yeah, I've been catching up on this. This… this PR went sort of dead when I went on on parental leave, but I still think it's… it's a valid request, and that we should have a solution here.
And so there's, there's two things that this conversation is about. It's one is, hey, I want to be able to check if global open telemetry was set without causing side effects.
And a separate case is, like, I want to determine if a OpenTelemetry instance is a no-op instance. Those are kind of, like, the two kind of ideas that are popping up in this conversation.
So, just to simplify this conversation, I was just reflecting more, and I was like, hey, why would you actually ever want to know that an OpenTelemetry instance is a no-op?
And the reason is, is because you're trying to write instrumentation, and you're trying to short-circuit things, and prevent doing work when it's unnecessary, because it's not going to get recorded anyways. But we already have a mechanism for that. Tracers, meters.
GZ Gregor Zeitlinger 00:14:51 What are you intuitive.
Jack Berg 00:14:52 There's another reason, too.
GZ Gregor Zeitlinger 00:14:54 If you are running an application and you want to see if the Java agent has, been set up.
And if so, then you don't set up your own, At least this is what I thought.
As a use case.
Jack Berg 00:15:12 Isn't that the same, though, as the other thing I was talking about, which is being able to check if global open telemetry was set without a side effect?
GZ Gregor Zeitlinger 00:15:20 Right, but the reason why you're asking the question is, in one case, what you said is you don't want to do extra work, and the other one is if the Java agent is not running, then you set up your OTEL instance according to some other configuration parameters.
Jack Berg 00:15:39 Right, and I… and that… that case where you're setting up an OpenTelemetry instance according to some other parameters, I think is something valid that we do need to accommodate. And the, the other case, though, I just want to, like, quickly dispel that. Like, hey, do I need to be able to determine if an OpenTelemetry instance is a no-op?
to prevent doing unnecessary work and instrumentation? And I think the answer is no, because Tracer, logger, and meter already have this isEnabled method that allow you to check that. So, like, rather than providing a no-op, like, isNoP function on an OpenTelemetry instance, just You know, ask for a tracer, meter, or logger, and ask if they're enabled, and that will allow you to do whatever short-circuiting you need to do.
JP Jason Plumb 00:16:21 I don't see that on meter, Jack. Sorry, Bruno.
Jack Berg 00:16:25 It should be there. Oh, it's down on instruments, it's down at the instrument level.
JP Jason Plumb 00:16:29 Yeah, okay.
Jack Berg 00:16:33 And so, I'm… I would like to focus on that… that more… that other case, which is like, hey, we need a way to check if global open telemetry was set without causing side effects.
And that basically allows you to check if the agent was used, or if somebody else was, you know, setting it up.
Bruno 00:16:54 So, sorry, will this answer a problem that I have, which is, okay, I want to customize my OpenTelemetry instance.
But for some reason, Somebody else started up, earlier, and, set it up, the default.
And… So, sooner or later, I will find who's responsible for that and fix it, but it would be really handy to understand exactly who it was.
Jack Berg 00:17:26 That… That should be discoverable today, because, you know, if you are intending to be the one that sets up Global OpenTelemetry, then you should call Global OpenTelemetry set.
And if you call Global OpenTelemetry Set, and somebody else has already configured it, then we print out a stack trace that includes the location of the original caller, the first caller.
Bruno 00:17:49 Yeah.
So, I don't think these will affect any of that.
Jack Berg 00:17:59 I don't think so.
Bruno 00:18:02 Yeah, I'm good, thanks.
Jack Shirazi 00:18:06 Just on the… on the enablement… Haven't we changed that so it's mutable? Which means that is enabled could be false and then true later.
Trask Stalnaker 00:18:19 Do you, you would check it each time that you… Want to do something.
Jack Berg 00:18:25 I think that's a general problem, though, Jack. Like, so, there's also… like, imagine you're an instrumentation that's trying to determine whether it should, you know, do anything at all, whether it should install itself. Like.
you know, at initialization time, you want to be able to do something like, hey, check if the tracer is enabled, and if it's not, like, avoid that logic for all operations that come after that. And dynamically enabling and disabling tracers just throws a wrench in all of that that needs to be thought about.
I don't have a good answer to that right now.
JP Jason Plumb 00:19:04 Jack, I still can't find what you're talking about for metrics.
Jack Berg 00:19:08 Let me pull it up.
JP Jason Plumb 00:19:10 Thanks.
Trask Stalnaker 00:19:12 I think it's still incubating, so you guys.
JP Jason Plumb 00:19:15 Oh, that might be why I can't find it.
Jack Berg 00:19:27 Yeah, here we go. I'll show you an example.
JP Jason Plumb 00:19:29 Yeah, no, it is incubating, that's what it was.
Thank you.
Cool.
Trask Stalnaker 00:19:39 Alright, is there anything… else that we want to discuss here, or it just needs more… Baking.
Jack Berg 00:19:52 I want to open a PR that just adds a method, is set, to global open telemetry.
And it just returns a Boolean.
I proposed that in this, like, this PR over here. You know, there's other alternatives, but I think that's, like, simple, and it gets to the point. Like, somebody wants to determine if global open telemetry was set without causing side effects.
GZ Gregor Zeitlinger 00:20:19 I think that's a good idea. Do you want to do it incubating or straight away?
Jack Berg 00:20:27 Probably straight away.
GZ Gregor Zeitlinger 00:20:30 I think that's a good idea.
John Watson 00:20:33 I approve.
Trask Stalnaker 00:20:36 All right.
Moving on, then.
Jack Berg 00:20:39 The fastest consensus we've ever had about one of the time.
John Watson 00:20:42 Why we haven't done that before is just that there hasn't been enough Glamour.
Trask Stalnaker 00:20:52 We kept thinking we would have a better… I don't know…
John Watson 00:20:56 There's the…
Trask Stalnaker 00:20:56 Or we didn't need global, or something.
Something, something.
John Watson 00:21:04 It seems very reasonable to me.
This is something that should be in the spec, by the way?
I mean…
Trask Stalnaker 00:21:11 Is global really in the spec?
Jack Berg 00:21:14 Serious?
John Watson 00:21:15 Global Health.
Trask Stalnaker 00:21:15 sort of.
John Watson 00:21:16 Yeah.
I mean, I don't want to fight the spec war, but I'm just wondering if this is something that we should… It should be there or not.
Not saying it should block our doing it, whether it's something… if it's something that we should… I think that should be available in other languages.
Jack Berg 00:21:35 I don't even think… well, the problem is that, like, the spec doesn't even mandate something like our OpenTelemetry instance, something that, you know, aggregates all the providers for the different signals. And so, like, even if it existed in the spec level.
it would exist in, like, 4 different places. Like, logger provider, meter provider, tracer provider, and profile provider, when that eventually exists.
John Watson 00:21:58 Are there languages that don't have this concept? I know Go does.
I don't know if Python does.
Jack Berg 00:22:07 I… I assume so, based on… Anecdotes.
Trask Stalnaker 00:22:17 Alright.
I'll… we'll leave that to Jack if he wants to look at any spec.
Jack Berg 00:22:24 No.
No, I did not volunteer for that.
Trask Stalnaker 00:22:30 Cool, alright. Moving on. We have a reordering here. Tyler, you're up next.
Tyler Benson 00:22:38 Sorry for preempting, I've got another meeting in 10 minutes, so… I do have just a quick question I wanted to ask.
So I'm working on the servlet filter instrumentation, to, be able to, instrument servlets without the Java agent, using a library. And there… is a lot of… a lot more complexity there than, what I remember from before. But one thing I'm running into is that in the Java agent instrumentation, there's some interactions where it's expecting a… it's using a class that's expected to be on the bootloader class path. Specifically, it's the, for example, the servlet async context.
So, I'm trying to figure out, how to structure this gradle-wise, and I'm not quite sure.
Do we have any, guidance on how to, do, like.
a library instrumentation that's also using classes that are, expected by the Java agent to be on the Bootstrap class path.
Trask Stalnaker 00:24:03 So it sounds like you're struggling because you're trying to share Stuff between the library and I mean, honestly, like, I… I thought Lori, Lori's comment early on in, when you opened the PR, that.
Tyler Benson 00:24:21 But it may just be easier to…
Trask Stalnaker 00:24:24 Have separate, not tried to do the sharing.
Tyler Benson 00:24:29 Okay.
Trask Stalnaker 00:24:32 I don't know, sometimes it's hard.
I don't know if Lori has any… More specific thoughts.
Lauri 00:24:44 I think in JDBC instrumentation, we have some… something that, takes a class from library instrumentation and somehow squeezes it into a bootstrap class path by shading it, or something like that.
But, if you really don't need to do it, then it's best not to do it, I think.
Tyler Benson 00:25:05 Okay.
Lauri 00:25:07 the, like… I assume that the sort of library instrumentation is already going to be quite complicated.
maybe… Maybe it would be possible to… To leave some parts out, somehow.
Tyler Benson 00:25:25 Yeah, so for example, the, I couldn't find a way to get the, the snippet injection working.
So I've… I'm kind of just skipping over the snippet injection, but if we're okay at, you know, just duplicating stuff, maybe that's the best approach, and I'll just, be adding a whole lot more classes than, trying to share them.
Lauri 00:25:51 One strategy you could try is, It's inside the library instrumentation, you could, like, Let the agent install some sort of helper class, so that, When running with the agent, it would call the classes on the boot class path, and when not running with the agent, then, well, maybe it doesn't do anything.
Tyler Benson 00:26:15 Okay.
Cool.
Trask Stalnaker 00:26:19 And you keep… I mean, the library instrumentation, I would expect to be a lot simpler, because, I mean, we don't need to… we could limit that to only supporting, like.
a recent version of Servlet API. We don't need to go… like, the Java agent has all those different modules to support back to, like, Servlet 2.2.
Tyler Benson 00:26:43 I was just going for the Servlet 3, just to start, because that seems to be a decent baseline. I wasn't trying to do the older 2.2 or whatever.
Lauri 00:26:54 The thing is that, like, the classes on boot class path and, and a lot of other complexity, I think, arises because, The server instrumentation interacts with app server instrumentations.
Tyler Benson 00:27:07 Yo.
Lauri 00:27:07 And if you're doing the library instrumentation, then you don't have that kind of issue.
Tyler Benson 00:27:13 Okay.
I'll keep working on it. Anyway, thanks for letting me preempt, sorry about that.
Keep, keep on fighting the good fight.
Trask Stalnaker 00:27:26 Alright, Gregor, back to you.
GZ Gregor Zeitlinger 00:27:32 Thanks. Yeah, this is actually a question about declarative configuration, but it also is about stabilization more in general, so I thought it would be good to bring it up here.
So, there are a couple of questions in this PR, but I particularly want to focus on the question, what happens if we stabilize a component? Here in declarative configuration… configuration, it will get a separate name, because, right now it's called inferred span slash development, and later on it would be just inferred spans without a suffix. And Jack Shirazi.
Was, asking, if, this could be a non-breaking change, and that the slash development could be kept. I don't know if he's actually on the call, no, does… Yeah, he is.
Quint.
Jack Shirazi 00:28:32 Yeah, so the, I mean, the implementation is there, is that, specific class, right?
Have I ever lost my audio?
Trask Stalnaker 00:28:43 Oh, no, we hear you.
Jack Shirazi 00:28:45 Okay, yeah, yeah, so, I mean, there's a specific class which gives that name, and it looks like we could just implement another class with that name, which is an ugly an ugly way to do it, but it's better than nothing.
And I was… that was, all I was asking Greg… you, Gregor, is, if we can just do another class with the other name, and, will that work, so we can support both names?
And generically, yeah, we, I don't see any reason… and we've done that with metrics, right? When we've taken the stable names, we've kept the old names as well, so you can use… both, or one or the other. I don't see any reason why this wouldn't be the same.
Jack Berg 00:29:27 That was my vision on how this would work.
Sorry, go ahead, Gregor.
GZ Gregor Zeitlinger 00:29:35 No, no, I just wanted to say it's possible, but if it's… If we should do it, I would defer to you.
Jack Berg 00:29:43 Oh, to me, so that's my vision of how this would work. you know, even for properties that don't represent the names of, like, component providers, SDK extension plugins.
we're going to have this, this issue. And so, what I was imagining is some sort of process whereby we strip off the development prefix and continue… but continue to recognize that old property name for some period of time.
3 months, 6 months, or something like that. And ideally, we could have, you know, code in there that recognizes the old name and logs a little warning, a deprecation warning, an end-of-life warning if it's seen.
Right? So, like, we would have a path to eventually removing support for the slash development, property name.
Jack Shirazi 00:30:38 Is that going to be part of the declarative config infrastructure, or is it something that the… Target class, like, the framework… the, sorry, the, like, inferred spans needs to do it separately.
Jack Berg 00:30:50 I think it's something that, at least right now, that the inferred spans, every single one of these component provider implementations needs to do separately. Maybe there's some, like, you know, tooling we can introduce to, to ease this process, so it doesn't have to be repeated so many times.
But nothing like that exists today. No tooling like that exists today.
Trask Stalnaker 00:31:14 I almost wonder if, like, the infra… When you ask it for a component with slash development, it first tries that name, and then it… if it doesn't find it, it… Strips off the slash development and sees if there's a stable version.
Available for it.
Jack Berg 00:31:39 That's a good idea.
And, you know, that way we could standardize the… well, I guess…
Trask Stalnaker 00:31:46 Because I like the standardization of the slash development.
Jack Berg 00:31:52 I just… the one thing that we wouldn't be able to do by that is, like, okay, so let's say we see the use of the slash development.
Even though there's a stable version of it.
It's… we want to print a warning message and say, like, hey, use this stable version instead.
Do we eventually want to remove support for the slash development, or is it okay to keep that around indefinitely?
maybe it's okay to just keep it indefinitely if there's, like, you know, common tooling like you're talking about for it. It's like, you know, because the inferred spans and all these implementations don't have to do anything extra to strip off that suffix.
Trask Stalnaker 00:32:33 the only…
GZ Gregor Zeitlinger 00:32:34 But then…
Trask Stalnaker 00:32:35 Go ahead.
GZ Gregor Zeitlinger 00:32:36 But then they would not be able to signal that they are actually stable.
Or how would you determine that?
I'd like to infer.
Jack Berg 00:32:48 Read the notes.
Trask Stalnaker 00:32:50 Well, we would… I mean, the documentation would change to not use the slash development, and people should… Remove the slash development, it would just be, like, a fallback.
Jack Berg 00:33:02 And we could warn if we see the slash development, and, like, have a log statement that says, like, hey, this component has stabilized, and… but we wouldn't be able to say, like, hey, this component has stabilized, and the slash development will be removed. The support for it will be removed on this state, because we wouldn't have that information available.
Right. And I'm saying, like, maybe that doesn't matter, because we can just keep it around indefinitely.
Trask Stalnaker 00:33:30 The one thing we lose is kind of the schema change, like, if there's a schema change from development, but I guess when you're using slash development, you don't really know if your schema's gonna change out from under you anyways.
Jack Berg 00:33:45 Any version change is risky for you when it's in development.
Trask Stalnaker 00:33:55 Alright, some good food for thought, but I think the, as Jack said, the, the current solution.
Would be copy-paste.
GZ Gregor Zeitlinger 00:34:11 Got it, thanks.
Trask Stalnaker 00:34:16 Alright, we got a big topic here. Let's dive in.
Invoke Dynamic…
Jack Shirazi 00:34:23 Yeah, so, we… we think that we've… we've finally, migrated all of the instrumentation over, so it is capable of running, Invoke Dynamic.
And this, comment from Sylvain here is a proposal for the next steps. Essentially, it's a two-step thing. One is to turn it on so that, it uses InvokeDynamic using the rewrite mechanism that I think you wrote, Laurie, which just, changes the instrumentation dynamically to, say, inline equals false.
And leave that on now, because it's… we don't think it's a braking change. But then, when we go for 3.0, essentially make that a braking change so that, we convert it into A fully invoked dynamic, Agent.
And, in the agenda… so, so please do read… through Sylvan's… comment there. In the agenda, I'm just reminding us why we're doing this in the first place, which is that first line, just there's a bunch of benefits.
That we have now done, we think, we've done all the instrumentations, we moved them over, so they can be changed, and if we change this, hotel, javaagentexperimental.indy.
Flag over to true by default.
Then, what happens is that, each instrumentation just gets converted to inline equals False, so they can't be inlined, and they're used as invoke dynamic.
And for those who haven't heard of this before, When you have an advice.
the code that you're… for your instrumentation, the curr… a lot of the instrumentations use inlining, which is that the code goes directly into the method, but InvokeDynamic just adds… instead, it adds a bytecode, which calls out to the advice method instead of inlining the code.
And that… that gives those benefits that you can see in that first slide.
Okay, so that's, that's it, that's the proposal.
Just to flip that flag to, to make it, So that we will actually run the instrumentation as… Dynamically invoked, rather than inlined.
But it's easy to flip it back.
Trask Stalnaker 00:37:07 So, initially, I was thinking we would… Flip that in 3.0 as sort of, like, hey, we're a little worried there might be some regressions there.
But… I don't mind relying on our test suite, basically saying, hey, if the tests pass.
There's no regression here.
We can do it in a minor version bump.
Jack Shirazi 00:37:38 I think we're already running that, test. I think we run it in both modes.
Trask Stalnaker 00:37:45 Yeah, yeah, yeah, I mean, we're basically saying, hey, our tests prove out that this is… A non-breaking change.
Jack Shirazi 00:37:56 So, if we just pop back to the agenda, there are… it is potentially breaking for… distributions that have… so if you go down to, I think it's the last of those three bullet points, distributions have custom instrumentations, which… are one of those edge cases that don't map over automatically, they… they would fail. So that's the only case, but you… you should… you'd see that fairly quickly, and it's only really distributions that would have that situation.
Lauri 00:38:30 What about people who have written their own instrumentation extensions?
Jack Shirazi 00:38:36 I… I don't think it affects them.
Lauri 00:38:40 How come?
Jack Shirazi 00:38:43 I think that's a different path, maybe I'm wrong, but I thought that that was a, a different… That… Because we're not changing the IsIndy, That wouldn't change the is Indie. That would only affect the instrumentations that ha- are… is indie ready.
And they won't have that.
So, they won't get rewritten by this.
We're… so we're not… we're not disabling, we're not saying if you're running inline, it'll fail. It's only saying that, those that it is… it is indeed ready will be in… will no longer be inlined.
And… so, actually, I'm not even sure that it would… It would break any downstream.
It probably wouldn't even break downstream, distributions.
Trask Stalnaker 00:39:58 Yeah, instrumentation… module… Oh, right, it's in the, experimental.
So, maybe that is, would be just the… Follow-up, would be to… confirmed that… It's ND… Ready is false.
So it wouldn't change… .
Jack Shirazi 00:40:48 Change that.
Trask Stalnaker 00:40:50 wouldn't change this.
It would only affect the instrumentations that we bundle in our… in the… our Java agent.
Jack Shirazi 00:40:59 Yeah.
So it's only when we get to the proposal for 3.0 that that would actually Cause, braking changes, and… That's for… please review and comment, but that's… that's not the immediate change that we're proposing. We're just saying.
Let's flip it so that we're actually running, Invoke Dynamic.
In case there is something subtle that we didn't notice.
Trask Stalnaker 00:41:38 I mean, that… that reasoning, though, to me, is a reason to do it in 3.0, in a major version boom. Like, if we, something subtle that we didn't notice, I'd rather do… Users know when they're taking a major… there's more of an expectation that, oh, this is kind of some new… unbaked stuff.
Jack Shirazi 00:42:03 I mean, the technology itself is really old and stable, and… It's used in quite a lot of agents, so… It's not… it's not something, like, that's experimental, it's just… We… I was just…
Trask Stalnaker 00:42:18 Same the way that.
Jack Shirazi 00:42:18 Understood.
Trask Stalnaker 00:42:19 Yeah, I'm just saying, the… not to… I wouldn't phrase it, if I were you, I wouldn't phrase it in terms of you want to get it into, the next, you know, a minor version bump in order to See if there's any edge cases that we didn't catch.
Does that make sense?
Jack Shirazi 00:42:39 Yep.
Lauri 00:42:44 think, one, one major thing that we have to solve.
Is that we have to figure out what to do with the existing extensions.
When we are going to do this conversion.
Like, are we going to support existing extensions?
Are we requiring people to rewrite them?
Jack Shirazi 00:43:08 So there is a proposal in that comment, sylvan… Says that, we could actually… we'd be supporting them, but we… we'd, Put out a warning that it's a good idea for them to migrate.
Lauri 00:43:27 Well, if you want to support them.
Then the question is, how are we going to distinguish, Extensions that have already been converted from those that haven't been.
Jack Shirazi 00:43:41 Does it matter?
Lauri 00:43:45 I think so, like.
Jack Shirazi 00:43:47 If you're getting auto-converted, then there's no need for them to change anything, it all works.
Lauri 00:43:52 I don't think we want to do the auto-conversion.
Trask Stalnaker 00:43:57 It'd be nice to remove the auto-conversion.
Lauri 00:44:02 The auto-conversion was more like a proof of concept that this thing can work.
To just give us time converting it manually, like…
Jack Shirazi 00:44:11 Yeah, the order conversion wouldn't apply to any instrumentation within the agent. That would only be extensions, and it would only be to let them remain compatible.
Trask Stalnaker 00:44:25 But we don't know if they're compatible with the… With the auto-migration.
Lauri 00:44:35 Yeah, if we want to run them, we just could keep them as, like, the inline device.
Jack Shirazi 00:44:49 I think there's nothing that stops us doing that. The benefits that the agent gets, we get all those benefits anyway. As long as we've converted all the agent instrumentations, it doesn't matter what the extensions are running.
Because they're… they're a separate… Separate… they're quite isolated.
At least as I understand it.
Trask Stalnaker 00:45:17 I think that… I mean, that's a nice story, and allows us to… Move forward with the… our instrumentation without… Any breaking changes?
Before… at least before 3-0.
Jack Shirazi 00:45:47 So, yeah, I mean… the immediate proposal, I think it's fairly safe, because it's not changing the instrumentations anyway, it's just stopping them from being inlined into being… Invoked dynamically.
Which is essentially… Where the code is run.
But… Every change always has a risk, so… Yeah.
Trask Stalnaker 00:46:14 Of course, yeah.
I'm generally okay with, like, hey, if our tests We've got… that's why we have so many dang tests.
If the tests pass, that's our bar, generally.
Lauri 00:46:31 There are use cases where they could break, like, If there is an extension that, That depends on one of the built-in instrumentations.
like, we have instrumentations that somehow, like, rely on NETI instrumentation, for example. If somebody has managed to craft similar instrumentation, then that would break if we turn on the indie… So, if you want to, like, turn it on before and experiment with it, then… I don't know, like… Maybe we would need to check somehow whether there are, like, Any other extensions, or, like, any user-specified extensions?
And if there are, then maybe back off and use teamline advice, or… I don't know.
Trask Stalnaker 00:47:22 Not a bad idea.
To basically switch this, because, I mean, that would get, sort of.
what your goal is, Jack, of getting it out there.
To the majority of people, who aren't using… any extensions?
Lauri 00:47:48 Anyway, like, in the long run, I think, It would be more important to solve, like, How to run, like, the converted extensions and not converted extensions.
Oof.
Trask Stalnaker 00:48:07 Well, we want to.
Lauri 00:48:09 Yeah, to ensure that when users have their existing extensions, that they won't break immediately.
Jack Shirazi 00:48:17 Yeah, I will take that away, and we'll actually do some tests, we'll do some extensions.
And see what happens.
You're right, that's an obvious test for us to do.
Trask Stalnaker 00:48:31 Cool, and there's, You could probably enhance the, we do have an example… we do have some tests for extensions over here.
Distros, I honestly, I think it's okay to break distros, because distros have to rebuild. There's not… they have to recompile, rebuild with each version anyways.
So I would focus on the extensions.
And, yeah, if there's maybe some… Additional testing over here that… Could prove that out.
Jack Shirazi 00:49:12 Okay, so let me go away and do some extension work, testing, and then I'll come back.
Thanks. Alright.
Lauri 00:49:21 And, yeah, congrats, Stope, for getting, getting…
Trask Stalnaker 00:49:25 Almost over the… the line there.
Lauri 00:49:29 Just one more thing, like, If you really need to distinguish between the instrumentations, like, that, want to use inline advice, and the new ones that don't want to use inline advice, like, one of the options would be to have some sort of method in the instrumentation module like, currently we have this easy ready, obviously, like, We could use something like that, but we wouldn't have to come up with, like, a reasonable name for it.
Another option that we could consider, for example, would be to add something into the manifest of the extension jar file.
Like, extension version or something like that.
But if you're setting extension version to 2, then you're saying that this extension is doing now the non-inline device.
Jack Shirazi 00:50:21 Yeah, I thought we had… I thought that's what is, his indie module was, but, I'll need to check back on that. It's been a while since I looked at that.
Trask Stalnaker 00:50:39 All right, let us move on. Complex attributes.
So… I did some more thinking on this, and this is… This is kind of… this is more or less the pro… my current proposal.
Which is a very trimmed-back, proposal of, let's just… Support value? Like, add a… Value attribute type, which is a… the any value, generic, any value.
Before, I was trying to do some special stuff for, like, maps.
Say, because we could do it maybe more ergonomic and user and performant.
But what came out in the spec was that we should… we need to support any value Anyways… And so this… We could always… Add… make some map stuff more performant, more ergonomic.
But… this gets us at least… and we're also… I mean, we're not… We don't think that these complex attributes are going to be common.
Right, like, this is… There's not gonna be a lot of them, so… That reduces the importance, I think, of, at least initially, the ergonomics and, performance.
And…
Jack Berg 00:52:32 Just to echo that, or, you know, add to what you're saying, so… The idea is… for… We want to support any value attributes because there's cases we've found where we're trying to record data which, at its source, is complex, and we don't want to artificially flatten it or.
Trask Stalnaker 00:52:54 JSONify.
Jack Berg 00:52:55 JSONify it, when we could retain its original structure.
And, like, in all those cases, like, it's something you… to translate the data you're capturing to a value, you want to do something like what Jackson does, where you provide, like, an arbitrary object to Jackson, and then say, like, hey, give me, like, spit this out as whatever type. Transform this, or translate this to whatever type I want.
And this… I have a PR that proposes this, like a convert method, right, that converts any arbitrary object to, a value using Jackson. And… that's… or maybe it does… I don't use Jackson. Maybe I found out a way to use… to not use Jackson in there. But that's, like… that's just kind of, like, echoing what you're saying, right? So, like.
if… if… like, we're steering users to use primitives and arrays of primitives, because that's what we want them to use, but if the data you're recording at the source is complex, then you're going to want to do something like record it as a value and not modify it, and use something like this convert method that I proposed to do so, which are going to restore your good ergonomics anyways.
Trask Stalnaker 00:54:08 Oh, true. Yeah, yeah.
Jack Berg 00:54:12 So you don't have to write that big, complicated convert method, every time.
So I like this proposal. I agree that it's not the most performant, but, like, maybe that's a positive?
JP Jason Plumb 00:54:26 The convert method is only for value, though, right? It's not for the primitives and arrays? Like, it's kind of only for the value special case.
What I… what I… what I'm slightly concerned about Is that someone that's, trying to come up with a one-size-fits-all solution for handling attributes is going to code everything to value?
Right? Like, even strings are values, even ints are values, like, everything's a value, and then they kind of do it one consistent way.
Which kind of violates or breaks our current expectations.
Jack Berg 00:54:59 Well, this kind of goes to my recommendation on this. I made a comment in this PR to this. Trask was like.
okay, do we allow people to represent primitives and arrays of primitives as value? And my guidance was like, no, I don't think we should do that. And we can have default implementations of the method to record a value type that, like, check if it's a primitive or array of primitive, and if so.
you know, record it using the standard attribute API.
JP Jason Plumb 00:55:26 So, like, kind of forcing it to be complex if you use value.
Jack Berg 00:55:30 Yeah, and so if you choose to treat everything as if.
Trask Stalnaker 00:55:32 No, Jason, more, forcing, if you use value, it… on a primitive, it would force it into the primitive case.
JP Jason Plumb 00:55:44 Okay, and you think there's a natural path to do that? Do you think that… Okay.
Jack Berg 00:55:49 Yeah.
JP Jason Plumb 00:55:50 Alright, I trust you.
Jack Berg 00:55:51 And so, yeah, and so basically, if you treat everything…
Trask Stalnaker 00:55:54 Javadoc for it, Jason.
Jack Berg 00:55:58 If you treat everything like a value, Jason, like you're talking about, if you try to, like, short-circuit this, you're only… you're going to be paying a pen… a performance penalty that you don't need to pay.
JP Jason Plumb 00:56:09 Yeah.
Jack Berg 00:56:10 And so that's on you.
John Watson 00:56:12 Well, I was gonna.
JP Jason Plumb 00:56:12 Right.
John Watson 00:56:13 Did we put that in the Java doc, also?
JP Jason Plumb 00:56:15 Yeah.
John Watson 00:56:16 What's.
JP Jason Plumb 00:56:17 Was that Java doc there yesterday, Trask?
Trask Stalnaker 00:56:19 Later on, after Jack… yeah, after your comment.
JP Jason Plumb 00:56:24 Okay, okay, I'm like, I don't remember seeing that.
Trask Stalnaker 00:56:28 The… so, the thing that… the only thing that I don't love about, Jack, is that we're saying that value key, put value key ABC value… of XYZ, and for other people, just to kind of catch us… catch you up on what we're talking about.
So, this… At the proto layer, it's going to be the exact same as this.
Jack Berg 00:57:05 Yep.
Trask Stalnaker 00:57:07 And…
JP Jason Plumb 00:57:10 In memory, they're different things.
Trask Stalnaker 00:57:12 In memory, they're different things.
Well, that's the question, is should they be different in memory or not?
John Watson 00:57:19 Does it happen at court time, or does it happen at recording time?
Trask Stalnaker 00:57:24 Yeah, and where that affects you is if you call… if you have attributes get, and you call… You know, value key… Get me this attribute back.
Right, like, this makes sense.
For this, but this is no longer a value, like, if we auto-convert it to this, Now, it's not…
Jack Berg 00:57:52 But we can… we can adjust the implementation to make that work trask, where you, when you're getting an attribute out, you can either ask for a value key or a, like a primitive key.
John Watson 00:58:05 Yeah, but the types are going to be weird on the return values.
JP Jason Plumb 00:58:07 Yeah, and also, like, if you put the same key twice, it's supposed to overwrite, right? So does the second put overwrite? And if you reverse the order, does it still overwrite?
Jack Berg 00:58:16 I'm saying on the… on Jason's point, on, like, when you call the first line there, put value key ABC, I'm saying internally, we'll catch that case and instead call the second item, put string key. And so, like.
they're indistinguishable. Like, if you're… it's… one is just the same as the other.
JP Jason Plumb 00:58:38 Yeah.
Trask Stalnaker 00:58:40 What happens, then, here?
Right, you do attributes get value key, and you get back… so we would… Then, on getting, we would… Convert it back from a string key to a…
John Watson 00:58:57 They may have it as this value on the left-hand side in their code, though, right?
Jack Berg 00:59:01 And what we can have as a value. So what we have to check. So we have to say, okay, you're asking for a value key, ABC. Is our value that's stored already a value? If so, just return it as is. If it's not a value, then turn it into a value.
John Watson 00:59:17 Yeah, but I don't know that we can… we'll have a way to know whether their left-hand side was declared.
Jack Berg 00:59:24 Value Key tells us that.
Trask Stalnaker 00:59:27 has a GET type on it that we can…
Jack Berg 00:59:29 Oh, this value key does.
Trask Stalnaker 00:59:30 Yeah, it's not a pure generic, yeah.
John Watson 00:59:33 Fair, fair enough.
Jack Berg 00:59:38 So, what you're… like, if we have to take something that's represented in memory as a primitive, but the user wants it as a value.
Trask Stalnaker 00:59:45 I see.
Jack Berg 00:59:46 We're paying a performance penalty for that, because we're gonna wrap your primitive in a value in order to return it to you. But, like.
I don't know, that's, that's not perfect. Yeah, yeah.
Trask Stalnaker 00:59:57 Okay.
All right, we are hitting our time box, but that was, mostly wanted to just get people thinking more about this. I will… I kind of started working on an implementation.
JP Jason Plumb 01:00:14 for this.
Trask Stalnaker 01:00:16 version, incubating implementation, so I'll keep hacking on that, and… Again, folks.
JP Jason Plumb 01:00:24 No meeting next week?
Trask Stalnaker 01:00:26 I won't be here… oh, actually, I will be, because I'm back on Wednesday night.
JP Jason Plumb 01:00:32 Okay.
John Watson 01:00:34 What's going on next week?
Trask Stalnaker 01:00:35 KubeCon… So I think you're the only one who will miss, Jason.
JP Jason Plumb 01:00:42 Okay.
Trask Stalnaker 01:00:45 We'll record it for you.
JP Jason Plumb 01:00:47 Awesome. I can't wait to watch the recording.
John Watson 01:00:50 Quickly, quickly, Baskar's question, does a spec…
Trask Stalnaker 01:00:52 Yes.
John Watson 01:00:53 Not something… not something for us to decide here.
Right.
Trask Stalnaker 01:01:00 Sorry, I didn't catch up on it.
Jack Berg 01:01:02 I tried to respond in chat, and I just responded again with the last little thing. So, I think the code that we have for our standard out exporter is solid, and we just haven't promoted it to the stable portion of our API, because the spec is unstable, and therefore, our configuration API for this component is still subject to change.
But, like, you know, the code itself, the serialization logic in it is used in, you know, our production OTLP exporters.
It's the same serialization logic, so I think that part is solid.
Trask Stalnaker 01:01:33 Send up PR to market stable in the spec.
There's gonna be… People are… there's motivation right now to mark things as stable, so ride the wave.
Jack Berg 01:01:44 Get it while you can.
Trask Stalnaker 01:01:46 Alright, thanks all.
Jack Berg 01:01:47 Yeah.
JP Jason Plumb 01:01:48 Bye.
