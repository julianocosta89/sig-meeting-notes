SIG: JavaScript SIG
Date: 2025-11-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:52 Hello?
**Andrei Borza (Sentry)** 01:02 Glue.
**Marylia Gutierrez** 01:04 Hello.
**Marc Pichler (Dynatrace)** 01:05 Hello?
Great.
Hello, everyone.
Looks like not too many topics here on the agenda today. I will… Get started with… My topic here, but if you have any, please feel free to just put them on the agenda here.
So the first one, that… I was… Wanting to talk about is that last week we discussed about this, proposal to it.
A way to instrument, tracing channels, and the person that was on the call here was so nice as to, create this really simple example, which is based on the authorized role, application that you're familiar with from OpenTelemetry I.O, and it basically instruments this, dice road library with tracing channels, so it's, Really simpler setup that, we can… look into and play around with. So, yeah, if anybody has… Time, and would like to look into it, please do.
It would be great to have more people involved in the discussion. I haven't had a lot of time to look into it myself yet, but I'm looking forward to it. So, yeah, if anybody has time, please have a look.
That's all.
Any questions?
About this… If not… Then, we can… move on to Marilla's topic, which is…
**Marylia Gutierrez** 03:39 Yeah, just an FYI.
Yeah, the… we did this last year, we're gonna do it again, so the last two weeks of December, all the sick calls are pretty much canceled, so people can have some time off.
**Marc Pichler (Dynatrace)** 03:55 Awesome.
That sounds good, because I also won't be here during that time. Yeah, exactly.
Alright.
Then, I see some typing here.
I should have given more time to add, topics to the agenda in the beginning, didn't it?
Yeah, Rafael put something here about input in the middle to the dough.
**Raphaël Thériault** 04:45 Yeah, so my understanding of 2.0 is that it's not a breaking change, but they marked it as a breaking change.
As, like, what they say is an abundance of caution.
And given it shouldn't break anything we're doing with it, I'm wondering if we want to start, like, changing the bound in the instrumentation package.
to… what I just listed, so that slowly, over time, we actually have all the dependents, that, like, start upgrading their instrumentation package, being able to use those 2.0 version.
**Marc Pichler (Dynatrace)** 05:21 So, if I recall correctly, we already bumped the version there.
**Raphaël Thériault** 05:30 Boop.
**Marc Pichler (Dynatrace)** 05:32 Let me check real quick here, it's in packages, Instrumentation…
**Raphaël Thériault** 05:46 Oh yeah, there it is. Huh, missed that.
**Marc Pichler (Dynatrace)** 05:48 So… We went directly to… Toodle, pumping everybody.
I seem to remember that, somebody has mentioned that there's some trouble when you have two different versions of input in the middle.
**Trent Mick** 06:10 That was me. If we're… I don't know if it kills us yet, but if we were… If, when we do change to the, Mechanism of not having used the dash dash experimental loader, but using module.register.
inside code.
There's… There's the… hold on… Is there an issue?
There's… Okay, okay, sorry.
I wasn't prepared.
Ch-ch-ch- Why cannot?
**Jamie Danielson** 07:02 What are you looking for? Is it the issue for module.register?
**Trent Mick** 07:08 Yeah, maybe that… well, I can't… do you have that issue, Andy?
**Jamie Danielson** 07:11 It's… yeah, last week, I had linked it.
Here, I just threw it in chat.
**Trent Mick** 07:23 Okay, I can't remember if I showed the usage stuff in there, if we scroll down… Okay, so that, the top code block?
telemetry.mjs there. So there's that other… that create ad hook message channel?
and the other… functions coming out of import in the middle. So it is maintaining some state Inside that instance of import in the middle.
for, determining which modules to hook. So, one of the things that this adds is instead of import in the middle, earlier versions, or at least… I'm not sure where this switch happened, but it would try to, hook everything, right? Then there are some ESM modules where that was problematic, so one of the improvements there was that you can Actually, maybe I'm mixing up two things. Anyway, Kate.
Let me simplify here and not get too far in the details. Import in the middle, an instance of it will maintain some state in its… Module object, for which modules to instrument.
In certain uses of Import in the Middle, if you have two installations of import in the Middle active.
one by one instrumentation, another one by other instrumentations, then the state in one of them won't get noticed by the other one, and so the instrumentation stuff won't work properly.
So that's something… something to think about at one point. I don't think it's something that's necessarily hurting us right now.
**Raphaël Thériault** 08:55 But yeah, I was… then I was… I'd wonder if we want to maybe relax that bound so that… like, if someone is using both an old instrumentation package, that's depending on… An instrumentation that depends on importing a middle one.
And one that depends on, like, one that supports 1 and 2, that it actually resolves to the same version.
All the way until they eventually upgrade and everything's on 2.
**Trent Mick** 09:24 Yep.
This… I mean, this is something I meant to dig into a long time ago, but kind of, I stalled on it.
But yeah, so, like, the fix could… be in… Import in the middle, or the fix could be in the hotel instrumentation side to make sure that it has a singleton of Which… import in the middle installation it uses for doing various instrumentation things, but that might be… the hotel side fix might be a long time coming, because I think it requires some structural changes to how The instrumentation package works.
So, yeah.
Anyway, so yeah, Mark, you brought up, I don't know that this is a… Oh, I guess you're bringing it up because we might have more cases of that if we have…
**Marc Pichler (Dynatrace)** 10:08 Yes, for sure.
**Trent Mick** 10:09 2 and Version 1.
**Marc Pichler (Dynatrace)** 10:09 That was what I was thinking when I saw, The suggestion to relax it to this here.
I'm not sure, Rafael, have you seen any, Issues with that already?
**Raphaël Thériault** 10:26 Not yet, but I'm kind of scared of upgrading right now.
**Marc Pichler (Dynatrace)** 10:33 Alright.
**Raphaël Thériault** 10:33 Yeah, I'll actually test it out and see how it goes, and if it's actually causing issue, I'll do a little write-up and see what we can do about that.
**Marc Pichler (Dynatrace)** 10:41 Yeah, I'd be totally open to just, also relax it to… what you proposed here. I'm not sure if we use any… I think we use any… We do use features that are introduced in later feature versions, so we wouldn't be able to do exactly one, we would be able to do one.
I think it should be possible to do that, if we figure out that it causes trouble somewhere.
should be possible to make that change, I think.
Alright, any… Additional questions?
Or comments? Or anything that you're concerned about.
But… Input in the middle update.
If not, then, we can move on to Jackson's topic. This is the… Logger Configurator. Sorry for not getting to this this week.
**Trent Mick** 12:04 Or to stop you for a second, Dre had a comment.
**Marc Pichler (Dynatrace)** 12:07 Cool.
**Trent Mick** 12:08 Related to the middle thing?
Just in the comments.
**Marc Pichler (Dynatrace)** 12:14 Just pumped input in the middle to 2, not a big deal. Yeah.
**Raphaël Thériault** 12:22 I think it's mostly, like, if, say, someone is using the Fastify instrumentation, or the, I don't know, Prisma instrumentation, that's gonna depend on an old version, and, like.
bring in its own EATM one. Even if you depend on two, like, it's gonna be in the dependencies.
**Trent Mick** 12:41 The one's gonna use one, and that… I'm guessing that's because of that internal state.
Sing.
Maybe relaxing would be a good idea.
**Marc Pichler (Dynatrace)** 12:56 Hmm.
Yeah, I'm… I'm wondering how we're gonna test it… Properly…
**Trent Mick** 13:09 Yeah.
**Marc Pichler (Dynatrace)** 13:13 that's gonna be a bit more difficult, but I guess let's… cross the line when we get to the PR.
We don't have… test our version stuff in the core repo, which…
**Trent Mick** 13:28 But this isn't exactly that, it's about two versions installed at the same time, so…
**Marc Pichler (Dynatrace)** 13:36 Tricky.
**Trent Mick** 13:42 Yeah, Andre, though they indirectly use it by the instrumentation package, I think.
Or at least I'm guessing.
Can't remember the festifying.
**Marc Pichler (Dynatrace)** 13:53 Yeah, Fastify is, plugin, I think. They… Have a completely separate thing going.
Prisma I haven't looked into in a while. I can't recall anymore how that works.
**Raphaël Thériault** 14:09 I mean, I was just drawing examples off the top of my head, where it's mostly just instrumentation depends on old version of the package, which depends on ITM not too, which brings it into the dependencies.
**Marc Pichler (Dynatrace)** 14:32 Yeah, I guess if we relax the versioning, I'm not sure if there's any way that we can… Because I'm also thinking of troubleshooting such a thing, then.
And you don't know which version of input in the middle is actually being reserved.
Because you might have the latest instrumentations installed, but there's no guarantee that input in the middle is actually at the latest version, and then you run into… Fun times, troubleshooting issues.
**Trent Mick** 15:19 Yeah, I mean, it may be just having an issue to… Where we can… At least start documenting what the issue and exploring it is, so we can… Point… people have something to point at, at least for starters.
Whether or not we have a test for it, or then eventually a fix for it, so you can work with Multiple versions installed.
Or, if you're doing support on things like this, and things are getting weird, ask for npmls-a.
**Marc Pichler (Dynatrace)** 15:50 Boom.
**Trent Mick** 15:51 To get a full listing, and if there are multiple I, imported the metal installations, then beware.
**Marc Pichler (Dynatrace)** 16:04 Yes, so I guess let's continue with creating an issue for now, and then… We can also look into relaxing the… constraints there.
**Trent Mick** 16:19 Raphael, do you want to open that, or would you prefer?
**Raphaël Thériault** 16:21 Yeah, I'll open it.
**Trent Mick** 16:23 Thank you.
**Marc Pichler (Dynatrace)** 16:24 Thanks.
Right.
then I guess, now let's move on to the… logger configurator thing. I was about to say sorry for not getting back to this, didn't have a lot of time to dedicate to Alter since last week's SIG meeting.
This is now back to the original, way that it was before. This is implementing the spec, exactly as it's written. So, yeah, I will have a look at this.
**Jackson Weber** 17:06 Thanks.
**Marc Pichler (Dynatrace)** 17:08 Is there anything else you want to discuss, Jackson?
**Jackson Weber** 17:12 No, just, just wanted to, bring this one to the forefront, given the change back to the original, spec-based approach. But yeah, I really appreciate the reviews and any folks giving it a look.
**Marc Pichler (Dynatrace)** 17:26 Yeah, thanks for working on this.
Or try to get to this, as soon as possible.
Will assign myself, too, so… Alright.
Does anybody have any questions, about the logger configurator?
If not, then… I guess we can move on to bug triage.
The first one here is… should have actually gone into the security tab, but it was opened as an issue, and it's actually not something that… affects us.
in any of our, released, artifacts. So, JS Yammer has this, vulnerability, but we only use it in dev dependencies, and we never use any Yammer, or… we never parse any Yammer that is untrusted, so we're not affected by this.
It's really just an annoyance when you npm install that you will see, not zero vulnerabilities, but… more now, depending on how many copies are installed of that, I guess.
I've been working on getting these, dropped.
But there's still one, put in through Lerna, the current version, so I guess we have to wait until they, actually release.
Another patch version there.
An unassigned bug here.
Because… it's not really a bug, it's just… Yeah.
regular situation, I guess.
So, yeah, I'll continue with that and have a… eye on… new releases of Rana to make sure that… We get back to zero, on the vulnerability side there.
Alright.
Meriform metrics export.
If value type is not specified.
Custom metric producer… Metric descriptor type was not correctly applied.
And there's two singular data points.
Hmm.
I will look into this one. I'm not entirely sure that this one is… Buck… Because if I recall correctly, the value type here is not… Optional anyway, we're required to be there.
But I will have another look. This metric producer is essentially the concept from the spec, where you can, Create metrics that are… Out of… they aren't created by the SDK directly, but you have a way to, create metrics in a way that the API doesn't allow you to, so… Have some insights into the internals of… What we use… here.
So I think I'm the right person to look into that.
This here, I still forgot to… ping the person that I was trying to ping, I will actually close this as not planned, because… This seems to be related to the endpoint that the metrics are being sent to, and not, Not on our package.
And this one I assigned to myself, because I probably still wanted to check What exactly it's… doing here, so DFTC.
instrumentation, gRPC, and they have this Firestore instrumentation, and… that one takes the span from gRPC and then attaches something at the end, if I understand that correctly. Like, after the span has already ended, and that emits, Warning lock.
And… doesn't export the Aventador.
just put an update here. If this is an actual bug in our code, then it would be P2.
And I'll put a comment here saying… Oh, there's a different keyboard here, aren't I?
Can't seem to find the ad. One second.
There we go.
And this looks… Like… It's a touching D… Right, so the request here was that, we should consider whether the span and timing should be configurable for streaming our PCs.
I did check the… semantic conventions, but… Wasn't able to find anything about, span timings for, gRPC or RPCs in general.
So… Actually, what I would do is I would… Put a note here to reach out to somebody in… The SIMCONF… Group… And ask for guidance there.
Krusty should have a bit more insight into… What's going on?
And how things should actually look like.
If at all possible, I would like to prefer not to, add another option to just… be able to set, how long an RPC span is, and then, having to deal with that forever, I would like to have some… Consistent way of doing it, so that we don't have to, Change settings based on which other instrumentation is being used.
I'll take some time after this to write up a… Somewhat coherent message there.
It's a bit too… Complex of an issue to, discuss… And type up right here. So the next one is, we're actually… in country PR triage, so I guess let's do that. The React Native stuff, there hasn't been… Any movement, I guess.
Yeah, the comments that I put here are still… Valid… Then we have the page view instrumentation.
Looks like there's also… in place.
of the page view instrumentation, so I guess we can close this one here.
Closing this PR as it seems, back… Hmm… Story… Pricement for this… Pure.
then… Let's continue on to… This one, this is the programmatic config.
Stuff… Amarillo, you were looking into that one as well, right?
**Marylia Gutierrez** 30:01 Yeah, so that was the question, because I saw that they were doing the opposite here, so they were giving priority to the environment variable, so…
**Marc Pichler (Dynatrace)** 30:11 Yes, thank you for… Reviewing that one, I think that's the right way to do it, here.
we had discussed this, I think, in the past, also in the SEC meeting, would be… Ideally, we would have everything aligned. There's a few edge cases where we don't do exactly what we say, but overall, I think that's the way that we do it, and introducing different ways in different environment errors.
Makes it more frustrating than… Yeah, it just ends up being frustrating for everybody, probably.
**Marylia Gutierrez** 30:56 Actually, in this case, just to confirm, because… okay, so today is, like, programmatic, then environment variables. Now, I'm changing, I guess, the environment variables to be basically the configuration package, so that… Means the priority would be programmatic, config file, or environment variable.
Yeah, I think we…
**Marc Pichler (Dynatrace)** 31:18 Config file is active, environment variable is completely inactive, right?
**Marylia Gutierrez** 31:22 Yeah, yeah, but I'm saying, like, the programmatic also takes precedent compared to the config file, right?
**Marc Pichler (Dynatrace)** 31:30 Yes… I think so. The… I guess it's one of these it-depends sort of things, because the way I understand it, we want to use the configuration to then generate, like, SDK components, right? And set them up.
So… If somebody modifies that configuration model and just… like, feeds that into the, thing, the component that creates it from the configuration model, is it then programmatic config, or is it… file config, and also, will we expose all the ways to modify an SDK?
or change settings on the SDK with this new interface that will take the configuration model .
**Trent Mick** 32:35 I think you just defined an additional category.
Cause I, like, I think… I think the case that Marilla was talking about is using the existing constructor options to the Node SDK class.
as programmatic config. There's this other level that's not exposed anywhere as a thing, is using the configuration package to generate a configuration model, then doing whatever manual tweaks on that, and then trying to pass that to some function to create the SDK components. There's no… there's no code path that allows that right now.
But I suppose that's a future possible thing. I don't know if that's…
**Marc Pichler (Dynatrace)** 33:17 Anyway.
I'm… I haven't looked into exactly how it's gonna be used, so I'm…
**Trent Mick** 33:22 Yep, yeah, yeah, sure.
**Marc Pichler (Dynatrace)** 33:24 Hmm.
So… Yeah, it's a good question. The easiest… is… to not have it be override over via programmatic configurator.
But that would mean that, when using Node SDK, we would have to have a separate interface to trigger, like, setup of an… of an SDK from a file without Allowing the programmatic configurator.
Which is… I'm not sure if that's the route that we're gonna go with.
What we want to go with.
**Marylia Gutierrez** 34:06 Yeah, well, so I can't give, like, a concrete example. So, I have one PR up that is in draft right now that is for the logger provider. So, for example, for that one.
What it does, it calls a different package that I'm not touching yet.
So.
**Trent Mick** 34:25 Jimmy's good.
**Jamie Danielson** 34:26 screenshot.
**Marc Pichler (Dynatrace)** 34:27 Awesome, thanks.
Just wanted to have something up here to look at.
**Marylia Gutierrez** 34:34 So, basically, if you go, like, yeah, files changes, go to the SDK file.
Let's see if you keep scrolling down, down… a little more here. So, yeah, the line, like.
that you are actually… have the plus on it. So, if you can see, I am doing, like, a new batch log record processor. So, on this one, this is actually this batch log record log record processor is, is coming from a different package that I'm not touching yet. What that one is doing is checking your config.
Which is basically something that you can, like, put when you create the new, and if it doesn't have, it's looking at the environment variable.
So… I have, like, two ways of changing this. One is eventually gonna change that function to say, okay, check the config, and if it doesn't have, then… I mean, like, the programmatic config, and I… and then I replace the part that is going to the environment variable to my new package, and that one is file, and then environment variable, like, priority-wise.
So that is something that I will work towards when I get to that package. What I did want on this one right now is because I want to give priority to the file, I am passing the file here, my config here, as the programmatic config.
So this line here, if you see the max queue size, max priority, I'm getting… from my config.
**Marc Pichler (Dynatrace)** 36:19 And that one is given the priority file and that environment variable.
**Marylia Gutierrez** 36:24 So that is an example of… But if someone creates like, a new batch log record, like, they create, not from this SDK, the priority would be whatever they are passing as the config, and then the… the other ones.
**Trent Mick** 36:43 So, sir, let me restate, so if I call… in my bootstrap or hotel setup code, I call node SDK, and I pass in… as one of the constructor options, log record processors. And I set the environment variable for declarative File-based config.
And my config file has a log record processor section.
**Marylia Gutierrez** 37:09 Who wins?
**Trent Mick** 37:12 which log record processors do I get? The one that was passed in as a constructor option to Node SDK, or the one in the config file?
**Marylia Gutierrez** 37:21 So that is the thing, like, I haven't seen anywhere on this code looking at the… because, like, when it was calling.
here, like, the create the logger, it was not passing the config at all.
So I don't know if that was not working correctly. Like, right now, how it is, is gonna look at the… Basically.
**Trent Mick** 37:42 Well, so, I mean, so… so right now, without any of the… your work to… declarative config stuff. The constructor option will win over… Using environment variables.
**Marylia Gutierrez** 37:55 Yes.
**Trent Mick** 37:58 Even, like, I'm not even entirely… I'm not 100% confident on that, I have to go look. And then, like, I don't know, I guess we just want to decide what the answer should be. So the question I'm asking is, now that we have declared, or… Once we have declarative config support.
Is there anything in the spec that says who should win in that case?
**Marylia Gutierrez** 38:20 No, so I was even discussing this with them today, and they were like, yeah, we don't have this priority, and they're not sure if they're gonna set up this, priority, so it's kind of like… up to implementation, because… because I was telling exactly, because I think in Java, it works differently. Not related to… it's just, like, priority-wise, programmatic versus environments. I think it's the opposite in Java, so they were, like, concerned that if they now impose this, it's gonna, like.
break for a lot of the SDKs, so it might be… like, we recommend, but it's not a requirement, the order.
**Jamie Danielson** 39:01 Yeah, like, I was trying to read… because, yeah, like, in general, it's not fully specified, environment variable versus programmatic, aside from with the config file that… if the config file environment variable is set, we ignore all other environment variables, unless they're specified within the config file. This one comment that I found from Jack when they were trying to figure out how to merge different properties and everything was in response to a question about .NET, where they said something about, you know, it's common for .NET to want to have additional programmatic ways of configuring things, in which case it sounds like The config file happens first.
and then looks to see if there's anything additive from additional programmatic configuration, but it doesn't really seem like it's something that's been fleshed out, so it might even be worth bringing up, like, I think Monday is the next file configuration working group meeting, so it might be worth bringing up there.
of, like, what happens if someone passes it in a constructor and also has the config file? Because that's generally the question, right, is that's the… least… Fleshed-out or written-down thing that we can find, is if both are there.
**Trent Mick** 40:14 Okay.
**Marylia Gutierrez** 40:15 Yeah. I can bring it up.
**Jamie Danielson** 40:16 I plan to be there, yeah.
**Marylia Gutierrez** 40:17 Yeah, because I was talking with Jack today about this, and we're gonna talk about it on Monday with the rest of the group, so…
**Jamie Danielson** 40:26 Cool.
**Trent Mick** 40:26 Okay, so yeah, I don't know if we would eventually get to a place where you would have an additional, like, override True or false option in… the Node SDK constructor saying, like.
If you're using declarative config, we're basically gonna ignore most of the options here.
Unless you say this override thing to say, yeah, I actually do want to use a declarative config, but have my constructor options win.
If and when there's.
**Jamie Danielson** 40:54 Did that ever happen? I mean, I guess anything's possible, right? It seems like… a rare case, unless people aren't really talking, I suppose. Like, if one person is implementing the code side and someone else is doing the… Config file environment variable side.
**Trent Mick** 41:10 We're at work, and people are slinging around multi-hundred-line YAML files. I'm like, do you even look at those things? Most people don't. It's just to put that in there, and then, oh, but I want to make a change. I, like, the only thing I really care about for my case is the log record processor, so I'm going to specify those ones in code, and I've been using the same YAML config file for… all my other projects, I start with that and want to do it. And so, yeah, I don't know if you want to have… A thing where we warn about it, saying, like, there's a conflict here, and we picked a winner.
**Jamie Danielson** 41:39 Also, looking at the merging involved, so, like, right now, right, the config file, what you see is what you get, you have to put the actual thing in there. So, like, I want a tracer provider, I want a meter provider, I… don't put in anything related to logs there, but I do add the logs programmatically in my constructor.
do I still get all of those things? Like, do they then all merge together in my final configuration?
**Trent Mick** 42:02 I think those ones don't conflict, right? Because the meter process is independent of the logger provider, yeah, but if you have…
**Jamie Danielson** 42:10 But then there's the question of when do you ignore what's passed into the constructor, like, only if it matches what's already in your config file?
**t2t2** 42:21 I bought someone using config file have access to constructor anyway? Because, shouldn't you be… component providers, be creating those objects?
**Marc Pichler (Dynatrace)** 42:33 Yeah, that's also my understanding of the thing. This is why I was suggesting that There might be an interface where you can't pass any overrides in.
Adore.
That's separate from the Node SDK one.
**Jamie Danielson** 42:50 So, like, Node SDK with config being separate from Node SDK, essentially. Yeah, so you would have, like, a… I don't know.
**Marc Pichler (Dynatrace)** 42:57 setup telemetry function that… You know, gets the config.
does the thing, sets everything up as Node SDK does today, but you can't override.
things here.
With your programmatic config, and if that's something that's needed later anyway, we could just… edit. We could just say… I don't know, there's the log record… additional log record processes.
thing.
If that's not possible to do with the, I forgot what they're called, this provider thingies.
**t2t2** 43:37 Yeah, about the providers.
**Marc Pichler (Dynatrace)** 43:39 Yeah, if that's not possible with that, somehow, then we can add that additional interface.
**Marylia Gutierrez** 43:49 Yeah, I can't…
**t2t2** 43:50 page one.
**Marylia Gutierrez** 43:52 I was gonna say, like, I can… cause right now, I haven't… encountered this use case yet, so all the things that I'm doing are very, like, straightforward, how to initialize the SDK, so I guess when, like, when the time comes that, okay, I got to this point that those decisions need to be made, that is when I can also bring up here on the SIG, and we can have a decision before I make anything.
But yeah, so far, the things that I'm doing is a very, like.
pretty much, like, replacing everything that was, like, environment variable to be the new config package, so… so far, I haven't changed the priority of, like, anything. It's just, like, a replacement.
**Marc Pichler (Dynatrace)** 44:31 Yeah, it still does the same thing, but, or still intended to do the same thing, and then, Yeah, be kind of invisible in the background.
But it's still used, yeah.
**Trent Mick** 44:45 So, I'll give you my most likely use case, which is, ironically, I think, one of the drivers for the declarative config stuff was on sampler configuration.
And that… my understanding is they're still discussing, and it doesn't look like it's probably close to resolution, is how to… declaratively configure the rule-based composable samplers. Which… Maybe in… well, in the limit always involves some code, like… Because the rule-based thing is, like, execute this predicate to decide which sampler, composable sampler you're going to use after that, and that's… that's like code, unless you define some canned things, like the… the classic example is, how do I ignore health check endpoints on my thing, right? Sample those out.
I have a service that has ALS Check Endpoint that gets called all the time. I don't want any sample… trace samples from those ones. Well, how do you… know what's a health check. You could define can… like, you could have the SDK that define scanned static things for saying, well.
the user configures… a pattern for what the route is going to be, kind of doing things, but in general, you kind of want some code there. So I can see me wanting to use declarative config, but… I want to define my samplary code, because it's going to be complex enough, because I want to do fancy things there.
So, I don't know, yeah.
**Marc Pichler (Dynatrace)** 46:12 But isn't that what, like, a component provider plugin… Things?
**Trent Mick** 46:17 Oh, God.
**Marc Pichler (Dynatrace)** 46:19 It would play.
**Marylia Gutierrez** 46:20 We're not ready for this.
**Trent Mick** 46:23 The component providers… okay, so here's my read. This is an opinion, but my read is that declarative config a… an initial run at declarative config is, we have a YAML file with a schema, we parse the YAML file with the schema, and we can generate the SDK components. And the… the only, like, names of… like, process, or spam processors or something are, like, batch and simple, because we only have the built-in, well-known names for a few types of all these other things.
The component provider stuff felt like it was added with the understanding that you have an extension system, like they do in the Hotel Java, where you start to get all generic for these things, and so you can have… Extensions that are loaded that can define names for… Different, like, something other than a simple or a batch.
span processor, for example. Like a pastel?
**Jamie Danielson** 47:24 processor.
**Trent Mick** 47:25 Right. Or custom versions of other components with names.
for them, and so you can refer to those in the YAML file. So, Yeah, at least my understanding is that our first run at config stuff was not going to do any component provider thing and not have that whole structure there. So, I worry about relying on that, at least for our… For our take on it.
**Marc Pichler (Dynatrace)** 47:48 Hmm.
So… One thing that I was thinking of was… do we need to build the fully-fledged thing immediately, or is it fine to have, like, a, I don't know, set up OpenTelemetry function that does what the config model can do today?
And then build on top of that later on, be it with these component providers, or via some new way to provide additional code-based SDK extension components.
**Trent Mick** 48:28 Yeah, I think we can do. So… Yeah, you're proposing having, something other than… Create Node SDK, or…
**Marc Pichler (Dynatrace)** 48:36 Yeah. Yeah.
**Trent Mick** 48:37 Now it's… now it's new, Node SEK, because we export the class, but if we were to do it again, we'd export a function instead of the class.
**Marc Pichler (Dynatrace)** 48:43 Yeah.
**Trent Mick** 48:44 But we'd have to create Node SDK 2.
We'd come up with a better name that has something called declarative config in there, which has.
**Jamie Danielson** 48:50 3000.
**Trent Mick** 48:51 A much.
We're not Python, man, you can't use… Ignore me, ignore me.
**Marc Pichler (Dynatrace)** 48:58 And also, what I'm kind of after is… the interface for Node SDK is a bit awkward right now, right? You have the start thing, and then you have… Different ways to provide, like, a… You can put an exporter in there, and it will automatically get wrapped by a…
**Jamie Danielson** 49:18 Bent.
**Marc Pichler (Dynatrace)** 49:18 And you don't have that for all of them, and there's a few weird things here and there.
would be… Structured way better than they are right now.
And the config… the declarative config gives us, It gives us a… Justification to say, let's… Start from scratch.
And build it.
**Jamie Danielson** 49:50 Properly this time. Better.
**Marc Pichler (Dynatrace)** 49:52 And then…
**Trent Mick** 49:54 Second system syndrome. But anyway, I agree, I agree with what you're saying, I'm just… yeah. Yeah.
**Marc Pichler (Dynatrace)** 50:00 The Node SDK is essentially, I think it's grown from a point where Somebody just wanted something to… Set everything up easily.
And then we tacked on stuff.
Without thinking too much. And then we let it sit for a while, and then it became de facto stable, even though it's 0. something, because everybody's using it.
**Jamie Danielson** 50:27 It's nice and easy to use compared.
**Marc Pichler (Dynatrace)** 50:29 Yeah.
**Jamie Danielson** 50:29 Setting everything up manually.
**Marc Pichler (Dynatrace)** 50:31 Yeah, exactly. And… Changing that is really difficult, but… If we start again, we would do things differently with the things that we have learned.
So… I guess that's what I'm proposing there.
**Trent Mick** 50:50 Would you still do this in the SDK node package? You'd just create, basically, a parallel path for creating Node SDK.
In there.
**Marc Pichler (Dynatrace)** 50:58 independent of the current… I think that's how I would start with, and I wouldn't mention it at all, that it exists in the beginning. I would just.
**Trent Mick** 51:08 Yep.
**Marc Pichler (Dynatrace)** 51:09 You know, Roll it out slowly to people, and then at some point, when we actually say we're gonna build the fully-fledged thing with, like, you can override stuff.
with programmatic config, then we deprecate Node SDK.
And we point people towards the new one and say, hey, this is the new, better way of doing things.
**Trent Mick** 51:36 Same package, or are you talking about two different packages?
**Marc Pichler (Dynatrace)** 51:39 Maybe. Or we can also do it.
**Trent Mick** 51:41 Oh, Node SDK, the class, not SDK.
**Marc Pichler (Dynatrace)** 51:43 Yeah, I noticed it.
**Trent Mick** 51:44 You mentioned when you said deprecating, yeah.
Okay, so here's SDK node, it's unstable, but here's a super unstable part of the unstable.
**Jamie Danielson** 51:52 Here's an experimental part of the experiment.
**Trent Mick** 51:54 I mean, we could…
**Marc Pichler (Dynatrace)** 51:55 We do an entry point.
**Trent Mick** 51:57 I don't know if we want an incubator or experimental entry point in there, or if that's just kind of silly waste of time.
**Jamie Danielson** 52:04 That's true.
It's funny, we did write that note, too, of considering the approach of a new, like, node SDK from config.
Than we had, initially.
shot it down, but I do also like the idea of it being… it's almost like its own feature flag in that way, right? Like, right now, we're being extra careful in implementing it into the current Node SDK class path, because… what if we break something? What if we have some unexpected behavior? Whereas if we have a totally different entry point, then… were a lot.
**Trent Mick** 52:33 And so, like, there was that change in behavior that we saw, right? So maybe it would actually make the task a lot easier.
**Jamie Danielson** 52:40 You can just compare the two.
**Trent Mick** 52:41 Don't… you don't have to worry about… Breaking the current, if you're not touching the current.
**Jamie Danielson** 52:47 I kinda like that.
**Trent Mick** 52:49 Really, what do you think? Would that bees here?
**Jamie Danielson** 52:54 You asking Marilla, he said?
**Trent Mick** 52:56 I did ask, yeah, really, if you thought that would be easier, doing that, or maybe you kinda… Ragequitarily.
**Marylia Gutierrez** 53:03 No, I didn't get, like, right now, I'm mostly, like, focusing, like.
don't break current behavior, and just replacing environment variable to the thing that gives priority to, like, file or environment. So that was kind of, like, my thought process, and I'm going, like.
taking things as they come. So, for example, like, hey, the logist provider were, like, a very straightforward one, because they're already being created. Now I have to think about the case. Somebody adds this from another way. So I'm just, like, going case by case, and also thinking about it, because we were also discussing that the end goal is to actually have the operator to be able to just send the file and use all the instrumentation, so I need to also make sure that works with that case, so that is kind of, like, what I've been thinking of.
**Marc Pichler (Dynatrace)** 53:53 Yep.
**Trent Mick** 53:53 Okay.
**Marc Pichler (Dynatrace)** 53:55 Sorry, go ahead.
**Trent Mick** 53:56 No, you go ahead.
**Marc Pichler (Dynatrace)** 53:58 So, when… If we do it that way, that there's, like, a separate path, we could also integrate that into auto-instrumentations node, because if I understand correctly, that's what the operator also uses. Yeah, yep.
So, if the environment variable for declarative config is set, for example, we just use the new path.
of setting things up. That is our own little opt-in thing for the new… Path?
Dear?
And then… I think the time until… We can get it to the operator, it's just the same if we build the new one versus… If we build it into the Node SDK part, because we have that… New environment variable that we can just use as a feature flag for that.
And also… for… auto-instrumentations node for this register script. There's no way to do, To do programmatic config anyway. So that's the perfect place for it to… Be used, in… The packages that we publish.
Boom.
Yeah, that's just some thoughts on this, aye.
Don't have a strong preference towards… Doing that, or doing the other thing, it just seems to be the simpler… path to me.
having touched the Node SDK things, before, and broken stuff.
I know it can be a bit, It can be a bit stressful, too, then…
**Marylia Gutierrez** 55:55 And I feel like I would need to look a little more on how everything works to have an opinion on that one, of, like, creating a new one.
Just because… I don't know, I feel like there is the downside of, like, confusing users. Like, we have two ways now of doing… what is the difference? How do I care? So I… I need to look a little more to see if it is, like.
If the confusion, initial confusion, is worth it in the long term.
**Marc Pichler (Dynatrace)** 56:28 Yeah, that makes sense.
**Trent Mick** 56:29 Okay.
**Marc Pichler (Dynatrace)** 56:36 I'm on board, either way. We go. It's, Yeah, just wanted to bring it up.
I guess.
**Trent Mick** 56:43 I like the idea of trying a separate path, but… I'll give it time, let's see. To pile on, if you guys are gonna be talking with… in the config sig. I'm curious what the state or eventual expected state will be for configuring instrumentations.
We're configuring the set of instrumentations to use. I'm not sure what… it's… Oh my god.
My phone started giving… Ed, do you… do you guys… Jamie and Millie, or whoever, have an understanding of what the current State of the world is for declarative configs selecting which instrumentations to enable.
**Jamie Danielson** 57:26 I think there's… like, the ultimate goal is to have, like, almost like a set of… default recommended instrumentations that are just available, like, for example, HTTP, gRPC instrumentation for every language should be easily enabled, with the config file. I think, ultimately, the goal is to be able to have a lot of those, like, anything that's defined in semantic conventions, so, like, you might have, like, MySQL database-specific things, then maybe that should ultimately be available.
Just getting to the block.
**Trent Mick** 57:58 thing on stability as well. Okay, maybe I.
**Jamie Danielson** 58:01 I don't want to confuse.
**Trent Mick** 58:01 They asked you too much, yeah, out of time, anyway.
**Marylia Gutierrez** 58:04 Yeah, there is the part of, like, also specific for, like, languages. So, right now, for example, the JavaScript is empty, because we didn't provide any, like, feedback of things that we need. But if there's also, like, there is pretty much, like, development, the flag or something, so we can just, like.
add things that make sense, if you want to, like, use that to register stuff, if it is something that is very specific for just JavaScript, because I don't know how it works with the others, but that is also something, too.
**Trent Mick** 58:34 Yeah, at least looking at the Java examples there, that area felt more like, at least the way they were using it for now, was about configuring Instrumentations, and not about… choosing which ones to enable or do whatever, but I think they're kind of relying probably on the Java agent has a well-known set of ones that are enabled by default, and then they have other options for enabling or disabling additional ones, which I guess we kind of do, too, through the hotel node enabled disabled Instrumentations and VARs, so…
**Marylia Gutierrez** 59:03 I guess… or it could be, like, if you have any config for it, that means you should enable… I don't know.
**Trent Mick** 59:10 Oof, nope, scary.
Yeah, anyway, it gets mixed up there. Yeah.
**Marc Pichler (Dynatrace)** 59:19 Right.
I guess we're out of time for today. Hope it was okay, too.
reused the contract triage for a little bit of configuration discussion, I enjoyed it.
So.
**Marylia Gutierrez** 59:36 We all enjoy it. There are, like, a couple of PRs open.
**Jamie Danielson** 59:39 Look!
**Marc Pichler (Dynatrace)** 59:42 Alright.
**Trent Mick** 59:44 Nice.
**Marc Pichler (Dynatrace)** 59:46 Thank you, everybody. Go review the config PRs. I will also try.
And, I will see you next week.
**Marylia Gutierrez** 59:54 Thank you.
**David Luna Bistuer** 59:56 That's all.
**Marc Pichler (Dynatrace)** 59:56 Yeah, bye.
