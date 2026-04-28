SIG: Kotlin SIG
Date: 2026-04-27
Duration: 48 minutes
Zoom Recording URL: https://zoom.us/rec/share/9r8whr5iimuESfAHBJgdj8sLl46suIuEcH3CybgMgzUxRTKdZF0UxFpREqxAXkgu.VvH_90l0Xafa12Cu
============================================================

## Zoom Recording Transcript

**Hanson** 00:24 Hate?
I didn't plug myself in.
**Jason Plumb** 00:34 Oi!
**Hanson** 00:35 Eric?
Is next Monday a bank holiday, Jamie?
**Jamie Lynch** 01:00 Yeah, so I'm gonna be out, so… either you or Jason are able to run it, that'd be appreciated.
Sure.
**Jason Plumb** 01:09 Let's see if you want to, Hansen.
**Hanson** 01:11 Are you out too?
**Jason Plumb** 01:12 No, I'm in.
**Hanson** 01:14 Yeah, I can do that, if there's stuff to talk about.
**Jason Plumb** 01:18 Cool.
Do we have a new person that joined?
**Viorel Alexandrescu** 01:24 Yep, hello.
**Jason Plumb** 01:25 Hey.
**Hanson** 01:26 Hey!
**Jamie Lynch** 01:27 Hey, bro.
**Jason Plumb** 01:27 Thanks for joining!
**Viorel Alexandrescu** 01:29 Hey, nice to meet you guys.
**Jason Plumb** 01:30 Yeah, same.
**Jamie Lynch** 01:35 Cool. So, basically, there's a shared Google Doc where you can add agenda items if you're interested in, like, talking about specific topics. I'll just give it a couple of minutes, and then we can basically Run through whatever's on my agenda.
**Jason Plumb** 01:54 And also, the agenda's pretty light. Yeah, the agenda's pretty light, so if you have something ad hoc you also want to bring up, we can just do that too.
**Viorel Alexandrescu** 02:01 As a matter of fact, I've been, conversing with Jamie on Slack, and… His, his pitch was for me to join in and talk with you guys about, splitting The environment variable configuration.
and to multiple tasks, so I guess you can adjust that there. I don't have anything else on my mind.
**Jason Plumb** 02:27 Was that in the Kotlin channel?
Was it somewhere else?
**Jamie Lynch** 02:34 We've just been talking via DM, I think, and a little bit on GitHub issues.
**Jason Plumb** 02:39 Okay.
Can you give us the, the summary of what that discussion was?
**Viorel Alexandrescu** 02:47 Oh, yeah, so…
**Jason Plumb** 02:49 There's an issue about environment variables that's, I think, is out there. Is it related to that issue?
**Jamie Lynch** 02:57 It is, so maybe we can go through that for context.
Yeah, so basically, the OpenSilometry specification allows setting a bunch of Configuration via environment variables.
So this is kind of defining, like, all the types, and then… there's various… Various properties, but you can set, like, all the V's, basically.
We created an issue on the repo to track that. And then… farewell. Dope.
How do I pronounce your name? Sorry, is it V-O-L, or…
**Viorel Alexandrescu** 03:42 You can stress the R a little bit, but…
**Jamie Lynch** 03:45 Yeah, bro.
**Viorel Alexandrescu** 03:46 You're on point.
**Jamie Lynch** 03:49 So yeah, I offered to… help, and then I think it was basically a question of Like, how do we… break… up all of those different properties in the spec, so… Yeah, we started with log limits, I think, is that correct?
**Viorel Alexandrescu** 04:11 Yep, that's what… that was your proposal.
**Jamie Lynch** 04:15 So, I guess the thing to… Kind of discussed today is whether there's… A logical way for splitting up all these, Kind of like… potential configurations.
**Jason Plumb** 04:35 like, into smaller chunks of work that could be, like, PRs, like.
**Jamie Lynch** 04:38 Yeah.
**Viorel Alexandrescu** 04:39 Yeah, yeah, exactly. The whole point was to join in, and if you guys have the time, maybe do some grooming over it and see…
**Jason Plumb** 04:46 Awesome.
**Viorel Alexandrescu** 04:46 How we would split all of this.
**Hanson** 04:48 That's perfect.
I mean, ideally, there would be logical chunks, you know, things related to the same component, the same related to the same spec, and kind of go that way. At this point, it's a bit of… as long as the order seems reasonable, that things are building on top of each other, that would work. I don't necessarily think these ones are more important than the others, unless folks are clamoring to use specific ones. So I'm… as long as they're separated into, like, digestible, reviewable chunks, I'm okay however you want to do it, to be honest, so…
**Carlos Alberto Cortez** 05:27 By the way, something I would like to ask is that in Java, I think this is something that exists as a layer on top of the SDK.
I wonder if such approach would work for us, and whether, if that were to be the case.
It could be a good idea to try to port that to Kotlin, or not, you know.
**Jason Plumb** 05:50 I'm not following Carlos, what are you saying?
**Carlos Alberto Cortez** 05:53 Like, let me try to look for that, because, OpenTelematy Java, I think they exposed this functionality as a separate artifact.
**Jason Plumb** 06:02 Yeah, it's auto-configure.
**Carlos Alberto Cortez** 06:04 Right.
**Jason Plumb** 06:05 Is that what you're talking about?
**Carlos Alberto Cortez** 06:07 Correct, yeah And I don't know if it makes sense at all to consider porting that to Kotlin.
**Hanson** 06:18 Is it considered a separate, API spec?
**Jason Plumb** 06:22 It kind of is, yeah. It's like a way to get the SDK initialized through environment variables and system properties.
And, and a bunch of, like, auto service. Like, Google auto service stuff.
So you can also have programmatic configuration.
There's, like, extension points for configuration.
**Hanson** 06:48 feels reasonable to be a separate module. If you want to include it, then you take the module. Kotlin, it's pretty lightweight to create a new module to handle that, so I don't mind. We probably don't have as much, like, auto-configuration as Jallo. Well, we may, especially the backend use cases, so yeah.
Sounds, sounds good.
**Jason Plumb** 07:09 Yo, there's…
**Carlos Alberto Cortez** 07:10 It's up to you, but I think it would be nice to consider at least the possibility, you know?
**Hanson** 07:16 I think in general, I like more modules than… than fewer, especially if… if there is a way… there are easy ways for us to, like, define, you know, dependencies. So, yeah, I'm… I'm generally M4, unless we're talking about, let's add 100 modules for pedantic reasons. I think something separate as… as a configuration API, I… Certainly. One at least, if not more, so…
**Jason Plumb** 07:46 Yeah, the chunks that we kind of were looking at in that SDK environment variables section Those seem… that seems like a reasonable breakdown, because none of those are huge, you know? So if we wanted to just kind of do, like, yeah, spam… spam limits is one, log limits is one, and then, Ignore declarative configuration for now. I've been… I had a… I've had a thing on my backlog forever to at least open the issue to support declarative config, but I think we need to kick that can down the road a little bit.
But we're gonna want it, people are gonna want it.
**Carlos Alberto Cortez** 08:18 Yeah, but not now. I think it's a good choice to not go for that.
**Jason Plumb** 08:22 Thank you.
Yeah.
**Hanson** 08:29 It's very attractive, though, to be able to have a YAML file to…
**Jason Plumb** 08:33 Oh, yeah. Stupid.
**Hanson** 08:34 But yes, yes, definitely.
Let's go with the one first that you don't need a separate, you know, thing for.
**Jamie Lynch** 08:43 Cool. I'll do that.
I was just gonna say, but how does that sound? Like, do those points feel reasonable? Is there anything else we need to discuss there?
**Viorel Alexandrescu** 08:56 Well, I'm not sure if it's worth mentioning, but I'll throw it out anyway. At this moment, the only target I've actually made an implementation for is the JVM. I mean, there is a… I mean, a multi-platform declaration for getting environment variable values.
But the only one which actually does something is the JVM. The others just do not just return null at that point, because from what I can tell, that's the only target which would actually work, unless we're actually… we actually want something to happen For the native targets.
**Hanson** 09:40 I… don't… think… like, even if you build on Android, which we're using the JVM target to pull environment variables, it's not the actual Android device that's… So, will that Android target… if Android target can work in the build, then that's fine. But I don't know how… that quite works as part of the build process for Android. If it's, you know, But…
**Jamie Lynch** 10:10 Yeah, I think from my perspective, that's absolutely fine. Like, the way we've written it as well, Yeah, it was just an expect actual declaration, so if folks did have an interest in implementing this on other platforms, That would be possible to do this at a later point.
**Hanson** 10:33 Like, I'm trying to think if, like, we… if Gradle… if somebody had a Gradle plugin that was using this, then that would be building with the JVM, target, right? And not the Android target.
And if somebody was running this on an Android device, they would not be picking up environment variables on an Android device.
So, in the Android ecosystem, you know, the build is actually JVM, and that would work if we want to do, you know, telemetry as part of the Gradle plugin. So… So for the Android use case, which, you know, top of mind for me, this is fine. So, yeah.
**Jason Plumb** 11:18 What about on native? Like, I know native… are we targeting… we're targeting native eventually, right?
**Viorel Alexandrescu** 11:24 Yeah, I mean, at this point, I've created… I mean, there are no op implementations for all the targets we're supposed to, support.
But on the native side, I'm not really sure how well does that play out, because… okay, Linux is one example, but the Darwin Target on Apple… I don't know… I mean, I think it's a different story there.
It's, it's worth…
**Jason Plumb** 11:52 Maybe.
**Viorel Alexandrescu** 11:53 Making a dedicated issue for this thing, specifically with the native target, and maybe picking up on it later.
**Jason Plumb** 12:01 I agree.
**Viorel Alexandrescu** 12:02 have something going.
**Jason Plumb** 12:04 Yeah, I think that's an awesome way forward.
**Viorel Alexandrescu** 12:07 Yep.
**Hanson** 12:08 Frankly, if someone were to use this on native, there's gonna be a lot of other bits in the SDK that probably needs, you know, testing and implementation before we even get to configuring or configuration, so…
**Jason Plumb** 12:20 Yeah.
**Hanson** 12:23 Plaza builds.
**Jason Plumb** 12:25 But some of that testing requires configuration, kind of up front.
And I'm assuming that most of those platforms, I'm hand-waving around Windows, maybe, but, like.
POSIX getEN should be mostly everywhere, right?
With little asterisk caveats, probably.
Cool, yeah, I think it's a good approach to create an issue for these specific targets as they arise.
**Viorel Alexandrescu** 12:49 Okay.
And somehow circling back to what, what I had in mind about this grooming session, so to speak, is there any guideline as to how these issues should be written?
Or everything… I mean, do you guys expect some form of… I don't know, wording, or… As long as the message… Is understood, it's fine.
**Hanson** 13:20 I think we talked about this really early on, and we said, until there's a need to have, some sort of format, we're not gonna have a format.
So, unless, you know, 10 people come up with dramatically different, you know, formats, I think we're okay for now. How do you guys feel about it?
**Viorel Alexandrescu** 13:41 I, huh.
**Jason Plumb** 13:41 We're not very… not dogmatic about it at all. It just needs to be just… just enough description, typically erring on the side of shorter rather than longer.
**Viorel Alexandrescu** 13:51 Okay. Okay.
**Jamie Lynch** 13:54 Yeah, I think as long as folks know what the issue is about, I don't… I don't mind how it's written.
Yeah, I would say I can… perhaps create a milestone, Given the number of tickets, but it might be helpful to have something to group them against.
**Viorel Alexandrescu** 14:16 But yeah, that's fine. Yeah, that sounds great.
**Hanson** 14:19 Yeah, I think more important, rather than, like, the format of the description, the issue is… is that there is… is, like, something that… if it… it's gonna be, like, 10 PRs, there should be 10 different… issues, or, you know, some way of mapping instead of, like, implicitly saying, hey, support, you know, configuration via environment variables, and then implicitly, there's, like, 10 different things you have to do. Having those 10 different things written out, either as, you know, as part of the description, or as separate, kind of, you know, issues.
That's the important part, I think, for tracking.
**Viorel Alexandrescu** 14:56 Okay, okay, yeah, I get it.
Thanks.
**Jamie Lynch** 15:03 Cool. And, I'll just say that it's really awesome to have people contributing like this. So, yeah, thanks for, Thanks for doing this.
**Viorel Alexandrescu** 15:13 Yeah, it's my pleasure. To be fair, it's actually a first time I haven't really had the chance to contribute on… on open source projects until now, and I saw your message on the Kotlin workspace, and just thought, hey, why not? I mean, I try to squeeze in as much free time as I can into this.
But, you know, I guess it's the whole point of contributing to open source, you do it whenever you can, as long as you like doing it.
**Jason Plumb** 15:43 Yeah, that's awesome. Yeah, more of this. I love it.
**Hanson** 15:47 I appreciate talking, you know, about this as well, instead of just, you know, here's 2,000 lines of code, without description.
**Jason Plumb** 15:58 Yeah, those do happen these days, more and more.
**Jamie Lynch** 16:04 Cool. If we don't have anything else to discuss on that, then I think the next item on the agenda was the Attributes API, so that's just kind of carrying on our discussion from last week. If folks do have other things they want to discuss, feel free to add them to the agenda.
Let me find… P… Shoot.
**Viorel Alexandrescu** 16:36 I saw in some previous documents that you keep track of what issues people picked up.
**Jason Plumb** 16:48 Not really.
**Jamie Lynch** 16:48 Yeah, we'll kind of do that on an ad hoc basis to some extent, for individual GitHub issues, by just assigning folks to them.
And then we'll use these meeting notes just as Typically, what would happen is I'd go through it the next day, and… Like, create GitHub issues or action items from them.
**Jason Plumb** 17:17 Jamie, can you humor me and click on the list of pull requests in the project? It's not working for me. Like, I feel like GitHub might be having… Challenges again here. Yeah, what the…
**Hanson** 17:28 That is categorically false, so.
**Jason Plumb** 17:35 Yeah, okay.
**Jamie Lynch** 17:36 89s of uptime.
**Jason Plumb** 17:39 Yeah, GitHub, struggling.
**Hanson** 17:41 I haven't had a GitHub outage in a couple weeks, it sounds about time, you know?
**Jamie Lynch** 17:45 Hmm.
**Viorel Alexandrescu** 17:48 Has it really been happening so often?
**Jason Plumb** 17:50 It seems like it. I saw it.
**Jamie Lynch** 17:52 Happy.
**Jason Plumb** 17:53 I saw a graph that someone put together that was, like, basically trying to blame Microsoft for all this. It was, like, number of issues per week since Microsoft bought GitHub, and it was, like, there was, like, none.
bike, biking.
**Hanson** 18:07 Usage, also complexity. I don't blame myself.
**Jason Plumb** 18:10 I mean, yeah, they should have feature set on there as well.
**Hanson** 18:12 Good.
**Jason Plumb** 18:13 I mean, the number of features has also done that, so…
**Hanson** 18:16 They released Stacks recently to Alpha or something like that. I tried to apply for it, haven't been accepted yet, but…
**Jason Plumb** 18:22 What even is that?
**Hanson** 18:24 Oh, it's, it's, it's my whole deal with, with, with, stacked diffs, so I use Graphite for that, and GitHub supports it natively now, it's a feature, and you have to.
**Jason Plumb** 18:37 Oh, interesting.
**Hanson** 18:38 apply to. It looks like exactly what I want, but GitHub, so hey.
**Jason Plumb** 18:45 Okay, Attributes API, sorry.
**Jamie Lynch** 18:47 Sure.
**Jason Plumb** 18:48 Here we go.
**Jamie Lynch** 18:48 So, yeah, just some context. I think this is one of the parts of the API we wanted to stabilize as a prerequisite before doing the logging and tracing API.
I figured this is probably one of the easier ones to discuss, so… Yeah, we could just take a bit of time to go through it.
So, currently, if you want to write attributes to your face with an interface like this, So, the type is basically encoded in which function you call.
We also offer… Kind of, like, synctatic trigger, where you can pass in an arbitrary map, and that will Basically, Corvus under the hood.
If you want to read the attributes, you basically get Passed back a map, kind of like that.
Ben… resource… Well, looks like these interfaces here.
So… I will… Put this in the doc so that everyone can… Read it.
So I just highlighted a few differences.
With the spec.
So, I think bytes array values… aren't supported.
Whereas I think they've been recently added to the spec.
But yeah, I was curious to get people's… well, rather than me kind of, like, list off everything here, I was curious to get people's thoughts on what this API looks like right now, and… How we should change it, and… If we need to change it, basically.
**Jason Plumb** 20:42 So, there's redundant… just… yeah, just to bring up the first thing that occurred to me, and I don't know why I didn't think about this earlier.
There is redundancy between the typing, the type information in the name of the method, and also the arguments. So I'm assuming, just practically, it would be unreasonable to have a bunch of overloads all called setAtribute with different parameter types.
**Jamie Lynch** 21:08 You look different.
**Jason Plumb** 21:09 Or… go ahead.
**Jamie Lynch** 21:10 I think, but I'm not 100% sure that that would be a compilation failure in Kotlin.
**Viorel Alexandrescu** 21:20 No, that should… I mean, that should work, because you would change the type of the parameters, and it should be fine.
**Hanson** 21:27 But it wouldn't really be an overload, it would be a generic type, like the method itself would have a type, and the implementation would be mapping to it, right?
**Jason Plumb** 21:35 I mean, I think the problems come in with the type erasure for the list types, probably.
**Jamie Lynch** 21:43 Hmm.
**Jason Plumb** 21:45 So those… how do those look in Java? It's been a minute.
**Hanson** 21:51 You mean, like, List string and list bool looks same after type erasure.
**Jamie Lynch** 21:59 I think in Java, from what I remember.
Like, you can set an attribute, and then the type is encoded in the key, so you've got.
**Jason Plumb** 22:08 It is, right.
**Jamie Lynch** 22:09 With, like, a string as a generic type.
**Jason Plumb** 22:14 Which has its own set of challenges around it, and is kind of clunky to deal with, honestly.
Like, and there's a lot of these key instances that fly around.
Yeah.
**Hanson** 22:31 What… what do other Kotlin APIs do for things that are similar to… to this?
Where we have to have some type of information, in… like this.
Because… Just feels very clunky to have.
You know, and different methods.
When we have already some type of information there.
**Viorel Alexandrescu** 22:59 You mean, the… using the reified, keyword?
**Hanson** 23:05 Something like that.
But I don't know if there are downsides to inline reify everything, yeah, I mean…
**Jason Plumb** 23:18 Can you… can you find another example anywhere in Kotlin APIs that does this kind of type stuff?
**Hanson** 23:27 Yeah, that's what I'm.
**Jamie Lynch** 23:27 Thank you.
That's… That's a good, a good call.
**Jason Plumb** 23:33 I just… I don't… I can't think of one off the top of my head.
**Hanson** 23:38 like, other serialization libraries?
**Jason Plumb** 23:41 Just, I was just typing serialized, that's so funny.
**Hanson** 23:44 What does Kotlin serialization do?
But it's everything generated, so it doesn't really matter.
So, my, I think, high-level opinion is that we should be idiomatic to Kotlin, and not idiomatic, or not, like, follow, whatever hotel Java does, because I think this is much more a language-specific thing than anything.
I would be okay with whatever status quo is, to be honest. I'm, again, not a language expert, especially, so… My opinion is more of a taste kind of thing.
**Jason Plumb** 24:25 And then we don't have value accounted for in here yet, either, do we?
**Jamie Lynch** 24:30 No, we don't. So…
**Jason Plumb** 24:33 Is that captured in the issue?
**Jamie Lynch** 24:35 I think… You're talking about any value.
**Jason Plumb** 24:38 Yeah, yeah.
**Jamie Lynch** 24:40 So yeah, just for context, so everyone's on the same page, basically any value is an object that can represent, like, primitives like boolean and string.
Or, by the way, various other bits and pieces.
So… I think that's something we need to add support for.
**Jason Plumb** 25:05 Yeah, I mean, that's the worst one, right? Because that's what allows for the complex attributes, like nested object structure.
attributes.
**Hanson** 25:13 So for, like… serializers, they have, you know, I'm just looking at, the concierization JSON, there's… JSON primitives, JSON array, and JSON object.
So I do split these into, you know.
broad categories. If it's something that's just a primitive, then yeah, theoretically, the type of information given should be sufficient. But if we're talking.
**Jason Plumb** 25:41 Yeah, in that case, also, the arrays, I'm assuming, are considered always to be heterogeneous, and not… Homogenous.
**Hanson** 25:51 Json represents JSON's a list of elements, so theoretically, it…
**Jason Plumb** 25:56 There's, like, anything. Yeah, it's a genius, yeah. Yeah.
I mean, it's not… we don't want that, but… No. That's one… because the lists are… the lists and the maps are where it gets tough.
And… Yeah.
**Hanson** 26:15 like, I… I would even be okay with, if we can cut down, like, the… the kind of the more primitives and have that Taken out, and then if we need to have, more type information when we're talking about collections, put that there.
**Jason Plumb** 26:34 Can I clarify what you mean by that? Do you mean to collapse the naming of the primitive ones?
**Hanson** 26:39 Yeah, so, like, yeah, set…
**Jason Plumb** 26:41 So have overloads for all those.
**Hanson** 26:44 It'll be, like, set primitive attribute, and then, you know, the type information will be, it'll be a, it'll be a typed, you know, method. So, you know, if you pass, if the type is along, or whatever supported ones that we have, it'll, it'll, you know, set it down to that.
But that won't work for a list. If you pass in a list there, it'll throw an exception, or, you know, whatever.
**Jason Plumb** 27:08 Got it.
**Hanson** 27:09 Or, type check, actually.
**Jason Plumb** 27:15 So we would get rid… we would get rid of… the set Boolean… we would collapsed the set Boolean long double… And string?
**Hanson** 27:28 Yeah, isn't there a third one? For a fourth one? But yes, basically.
And then… Like, could… is it possible to do, like, a set array attribute, or set list attribute, and then have… have homogeneous lists like that.
**Jason Plumb** 27:50 I don't know how to enforce it, is the… is the thing.
Maybe somebody has a clever trick up their sleeve, but I don't.
**Hanson** 27:59 I wish I were better at the language than I actually am, so… Or, if we can't, like, if we want to defer this, basically have what we have right now as V1.
and then move forward.
I'm okay with that, too. Cause I don't… I don't want to… I don't want to, like… hang up on this. I… collapsing a verbose API into a more streamlined API in a future version, I think would be okay, because these could just be backwards supported, because they deterministically map to a functionality, so I think backwards compatibility support would be easier. So, if… I would be okay to be just like, hey, this… this probably could be improved, but, at this point, we want to sign stuff off, so I'm okay with this being one of…
**Jamie Lynch** 29:03 I think I'd be okay with that in principle. There's a couple of… differences that I would like to address before doing that, though.
like… Yeah, jumping out here, bully number, yeah, 4 and 5, like, is not really possible to clear a value right now.
Well.
**Jason Plumb** 29:23 Yeah, what… does the spec have an opinion about number 4?
Like, setting the entire set, is that a thing that's in the spec?
**Jamie Lynch** 29:32 Yeah, so… Yeah, spam… well, it's specific to spans here, but it has the ability to set the attributes object Yeah, so that's another… area where we differ a little bit from the spec, in that you… Can't create a top-level object and then pass it in to a spam or a log, do you… Basically, call, like, setString attribute on the spam or the log.
**Jason Plumb** 30:05 But in that list, like, number 4, just to be clear, was about setting the entire collection, like, about setting the entire contents of the attributes associated with whatever the data type is, and then… Java does it one way, and we currently do it a different way.
Is that what was in there?
**Jamie Lynch** 30:30 Yeah, basically. So, Java and a spec basically set everything all in one go, and gets rid of any previous attributes, whereas our current implementation You can mutate the existing values in the attributes collection.
**Jason Plumb** 30:51 So if there was, like, some other random attribute set in there, and you call set attributes, that random attribute will still be in there afterward. Yes. So, do we… maybe, Carlos, do you know what other languages do in this case? Because the spec is, I think, ambiguous about this.
**Carlos Alberto Cortez** 31:06 Yeah, I think there's some activity and purpose on this one, basically, they… So, long story short, if I remember correctly, is that you are just sending an instruction to set or override an attribute, and in the backend and the SDK, they can do whatever they want.
They should be overriding that value, but it's up to them, you know?
**Jason Plumb** 31:33 Okay, so we have a choice here, it sounds like, and we can choose which way to do it.
pros of doing it the way Java does it is consistency, and maybe keeping up with the expectation that some users will have, that it changes everything. And then the other flip… the flip side of that is that, It's a little… yeah, it, it's a little more sensical to… just set the ones that you're given, and not touch the ones that you weren't given, right? So there's… I think there's pros and cons.
To both approaches.
**Hanson** 32:09 like, the behavior that Java offers, do we have a way of clearing and then setting?
So that… it would basically be a two-stepper.
**Jamie Lynch** 32:21 I mean, you can overwrite existing attributes, but there's not a way to completely clear an attribute.
**Hanson** 32:31 Got it. So basically, Java has this concept of, like, the attributes sit as a separate object, and you can blow away the entire thing. Yeah. Versus us, it's inherently part of the thing that has attributes. So there is no way of saying, blow away the entire thing, because there's no entire thing.
**Jason Plumb** 32:54 So maybe this is something that can be addressed with naming. If we had two different methods, and allowed both of them.
So one is replace all attributes, could be one method name, that's pretty clear. And then the other one is, like.
Update attributes, and then what you pass in is the attributes collection.
**Jamie Lynch** 33:14 I don't know.
**Jason Plumb** 33:17 Because then it'.
**Carlos Alberto Cortez** 33:17 Anyway, I'm coming, I'm thinking, and I don't think I… I think all things do what Java does.
I would have to confirm that, but I think that…
**Jason Plumb** 33:26 They replace it.
**Carlos Alberto Cortez** 33:28 Yes.
Remember the Python, the old one, the JavaScript one, they do what Java does.
**Jason Plumb** 33:37 Okay.
**Hanson** 33:39 it, it seems… pretty powerful to basically be like, I don't care what anybody else said on there, I'm gonna… I'm gonna just blow it up, like, as a default behavior.
Like, if you have two, processors.
**Jason Plumb** 33:56 Yeah, two-span processors, the later one wins, yeah.
**Hanson** 34:00 Like, as a default approach, it seems too powerful.
To me.
**Jason Plumb** 34:06 But I think by… I think that ex… I think the expectation is that span processors usually only set a few things, they don't want to pass the entire representation of all attributes, but I agree with you in that it is a little heavy hand, it's kind of powerful.
But it makes me wonder why other… why all of the implementations did it that way, then.
**Hanson** 34:29 It could be a backwards compatibility thing, like, you know, whatever OpenCensus or Open Tracing did, it did it. Like, could just be that.
Like, I know what the intention is, but then we're still giving somebody without a safety… a gun without a safety, you know?
And at this point, unless some… if we have a way of replicating the old behavior, so if we don't have a way of clearing all attributes, maybe that's something we want to add. And then, you know, through proper naming, we could effectively achieve both.
One having a more, kind of, like, merge, you know, attributes in.
Update whatever's in the thing that's passed in.
And then that's a default behavior, and then if you want the old Java behavior, then you call this clear all, or whatever, and that will handle… that will, you know, get you what you did… you had before.
**Jason Plumb** 35:29 Yeah, I don't think clear is part of the spec, though.
**Carlos Alberto Cortez** 35:33 Yeah, tear it's not, for sure, yeah.
**Viorel Alexandrescu** 35:36 Is the attributes, let's say, data structure immutable? I mean, once it's set, is it considered immutable?
**Jason Plumb** 35:44 No.
The attributes themselves are not.
**Hanson** 35:51 Well, the spec doesn't have clear because, you can pass an empty map in there, and that's effectively clear, right? So…
**Jason Plumb** 35:59 Depending on the implementation, right? Depending on whether or not it replaces or mutates. Fair.
**Hanson** 36:07 It, it… I wonder if this was just something everybody's implemented, it's always unstated.
And I don't know if it's a good thing to have that, especially in an environment where the instrumentation, or the app and the instrumentation could be a lot more disconnected.
**Jason Plumb** 36:29 Github!
It won't let me search issues now, either. Damn it.
**Hanson** 36:34 It's probably down, yeah.
**Jason Plumb** 36:37 Well, I was looking to see if maybe Java had an old issue about clearing attributes, because I imagine somebody asked for that at some point.
**Hanson** 36:45 Well, I mean, I thought… Temporary.
**Carlos Alberto Cortez** 36:48 Because I'm moving to rates.
**Hanson** 36:51 No, go ahead.
**Carlos Alberto Cortez** 36:53 I was saying that maybe in the specification, there was an issue.
**Jason Plumb** 36:58 Heck yeah, maybe.
**Carlos Alberto Cortez** 36:59 Yeah.
**Hanson** 37:06 I'm trying to think, if you're a back-end… I'm trying to think whether in the, in the, kind of, client apps and mobile perspective, this would be a bigger problem or a smaller problem.
like… My gut?
Which, you know, for what it's worth, it is what it is.
My gut says, by default, killing everything when you call set attributes is too, too, too powerful.
There's a lot… it's very easy to make a mistake like that.
It's like, hey, I have a bunch of attributes, so I'm just gonna call setAttributes instead of, like… And then, what happened to the attributes, you know, I had before? Sorry, you didn't meet the definition, or the spec.
Or the implementation, specifically.
So, I'd rather err on the side of merging, rather than blowing up, and then having that explicitly stated.
Like, unless the spec… like, if the spec explicitly says it has to do that, then, you know, hey.
Throw my hands up, but if the spec is ambiguous, we should lean into the ambiguity and say, yeah, this is the behavior.
It's my opinion.
**Carlos Alberto Cortez** 38:33 Yeah, I have to leave in one minute, because I have other calls, but, I will work on this issue, I would like to go and check what other cities are doing, re-read this part of the spec, and probably can provide some feedback before the group makes a decision.
And hopefully we'll have more, Context on that, and then we can, once more information from what other cities are doing, can help us decide.
So, yeah, we'll need a couple of days to, before we forget.
**Jamie Lynch** 39:02 Cool. That'd be helpful, yeah.
**Jason Plumb** 39:05 Yep.
**Carlos Alberto Cortez** 39:06 Perfectly good, so yeah, I'll send this issue to me, probably, just to make clear that, you know, I'm… the person in charge, before… at least in charge of providing the context, you know? Yeah. Okay, I hope to all…
**Hanson** 39:19 It's for those.
**Jason Plumb** 39:20 Yeah, thanks, Carlos.
**Hanson** 39:23 If we default to that destructive behavior, I want the spec to clarify that that is what we're expected to do. And then I think we can do it, and then offer, like, an extension function that says merge attributes or something like that, that… Did what it did before.
**Jason Plumb** 39:38 Oh, I encourage you to open that spec issue. Oh my gosh, you are in for a, I had a lovely time with that, I think.
**Hanson** 39:46 I know, I know.
I want to open a spec issue about, like, maybe the span having no end time being a possibility, which theoretically should be easy, and you just have to ignore it if the collector gets one, but… Yeah.
**Jason Plumb** 40:02 Huh.
Well, so, as far as consensus goes, I like the current set of methods. I think… I don't… I'm not hung up on those at all. I think it's a good start. I also agree with what I think… I think Hanson said this earlier, that, like, extending with convenience or, like, less… less burdened type stuff, if we can layer that on top later, that works lovely.
and… we still need to address some of those differences, but I think we're… I think it's a good… I think we're on track.
I don't see anything yet that's deal-break-y. I want to see, and I think we need to see an implementation that does any value.
**Jamie Lynch** 40:46 Cool.
Yeah, I guess for next week, Ben, I can try and go implement any value.
And we should hear more from Carlos about what the other zigs are doing, which should… Help make us… help give us a decision.
**Jason Plumb** 41:08 Cool. That sounds reasonable.
**Hanson** 41:10 So of the differences that, that, that, you listed in the, in the, was that a PR, or the issue, Jamie, are there ones that you want to specifically dig into?
Because I think…
**Jamie Lynch** 41:25 So, number one, by the way values. I think I've got a PR up for this.
If it hasn't already gone in. 2… I think that'll be implemented… As part of supporting any values.
Number 3… I assume that's fairly non-contentious, and can just have a PR open for it.
4 and 5, we just kind of discussed.
Yeah, then I guess 6 and 7 are to do with whether we want to… have a reference to an attributes object and pass that in, or whether we want to keep the API we've got right now.
**Jason Plumb** 42:15 Yeah, so attributes is a class or interface?
Is that… is that true?
**Jamie Lynch** 42:22 So yeah, as an interface right now, like, Whoa.
It's got an attributes mutator and an attribute container, so this is basically right, and this is reading it.
In the spec, it's just a… attributes.
**Jason Plumb** 42:43 Type.
**Jamie Lynch** 42:44 type, I think.
**Jason Plumb** 42:45 And we don't have one of those that's exposed?
Oh, it's just kind of… oh, it's very…
**Jamie Lynch** 42:52 We attribute as the… There's not even an interface, it's a key-value pair.
**Jason Plumb** 42:58 Yeah.
**Jamie Lynch** 42:59 It's got to be one of the types defined in any value, but not necessarily is any value.
**Jason Plumb** 43:05 Right.
**Jamie Lynch** 43:06 And you can have a collection of attributes.
**Jason Plumb** 43:12 Yeah, very non-prescriptive here.
Like, Java doesn't have an attribute class either.
It's only the plural.
And operations that do stuff, like, if you want to iterate over… the attributes, you can do that, either by converting it to the entire thing to a map first, or using a closure. Like, you can do both those approaches, but… they're always paired, right? So there never has to be an actual attribute type, because both ways of accessing them are through the pair.
**Jamie Lynch** 43:46 Yup.
**Hanson** 43:48 And I remember the, the, the Java implementation, the attributes does some shenanigans with like, serialization with, with, like… Arrays under the hood, rather than… like a map, which you would… you would think name-value pairs, you know, convert into. I remember reading issues that there's a… there's a bunch of performance-related reasons, for it.
that's, I think, all well and good, but that doesn't… still doesn't seem like it necessarily needs to happen.
having the higher-level attributes object, as part of the interface, I still don't see… why we need to have that, and what it serves, as long as the functionality, if we could… if we could do the optimization when we serialized and stuff, then I think it's okay.
**Jason Plumb** 44:41 Yeah, I think I do too, and I'm not trying to suggest that we need that type. I was just thinking through whether or not we need that type.
**Hanson** 44:47 Right.
**Jason Plumb** 44:48 It sounds like we don't.
**Hanson** 44:51 Yeah. Especially if the spec isn't prescriptive, but you have to have that.
**Jason Plumb** 44:56 Right, so that was number 7 on the list, right? Is, like, whether or not we need to be able to create one of those, and it sounds like not really.
The set attribute that, like, the number 5, where it, like, replaces everything, or doesn't replace everything.
What method is that?
It's just all of the individual ones. We don't have one that takes a.
**Jamie Lynch** 45:18 So… I think… there might have been a link to it.
**Jason Plumb** 45:22 Okay.
**Jamie Lynch** 45:26 Yeah, so Spa must have the ability to set attributes with it. I think this is just copying what OpenTelemetry Java does, to be honest, so it kind of comes back to Carlos going and getting feedback from the other things.
**Jason Plumb** 45:40 I guess what I'm getting at is, do we have a way to set… a collection of attributes at once. And it sounds like we don't.
**Hanson** 45:52 I think we have an extension function, to do that.
**Jamie Lynch** 45:54 Yeah, so there's an extension function where you can basically set attributes from an arbitrary map.
And I think when you're creating a span, there's also a lambda based on this, so you can basically call these functions.
**Hanson** 46:09 That's where the issue we had before was, where folks are passing in an int, and I think we're setting it as an int, and I think Jamie corrected that by mapping ints to longs, so that, you know, it's not just gonna be like, hey, whatever this is, I'm gonna try to set it.
**Jason Plumb** 46:27 What is the name, or where does that extension live? Do we know?
**Jamie Lynch** 46:32 There's one on the tracer interface.
**Jason Plumb** 46:38 Does it have extension in the name?
**Jamie Lynch** 46:42 So there's a spam creation… Action.
So, basically, you could supply a lambda to that. Did you want to see the actual implementation of this?
**Jason Plumb** 46:55 Yeah, or where that lives, I'm curious.
**Hanson** 46:58 in API EXT.
Another module.
**Jason Plumb** 47:04 Yeah, which is great, but where?
Attributes, mutator extension. Okay.
**Jamie Lynch** 47:13 That's basically just… Calling bees under bed.
I also think we're at time, so if any folks do need.
**Jason Plumb** 47:22 Yeah, I completely lost track, sorry. Yeah, we are over time. We should… we should be good about ending on time.
Cool. Cool.
Thanks for talking that through.
**Jamie Lynch** 47:36 issues from all this. Thanks everyone for coming along.
**Hanson** 47:39 To answer your question, it takes… we usually do, until 9.45, or 45 minutes.
**Viorel Alexandrescu** 47:45 Okay.
**Hanson** 47:46 It takes till whenever we say, hey, I think we're over time, so, usually.
**Jason Plumb** 47:50 profit.
We should be good about ending on time. Okay, thanks everyone.
**Hanson** 47:55 Cheers, thanks.
**Jamie Lynch** 47:56 Thanks, buddy.
**Hanson** 47:56 Right.
**Viorel Alexandrescu** 47:57 Have a good one.
