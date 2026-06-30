SIG: OpenTelemetry C/C++ SIG
Date: 2026-06-29
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Marc Alff [MySQL]** 01:07 Hey, hi, Doug.
**Doug Barker** 01:08 Hey, Mark.
**Marc Alff [MySQL]** 01:17 I don't know if you are following the weather in Europe, but last week was absolutely brutal in France, with a lot of heat.
**Doug Barker** 01:25 Oh, yeah. Yeah, I think I haven't been following that.
We're about to get hit for the 4th of July, at least here on the East Coast.
**Marc Alff [MySQL]** 01:32 I see, yep.
**Doug Barker** 01:36 Hey, Tom.
**Marc Alff [MySQL]** 01:38 Hi, Tom.
**Tom Tan** 01:39 Hi, Mark and the dog.
**Marc Alff [MySQL]** 02:00 I don't have a lot of things to discuss. I guess the big item will be to make a new release, because I said I would do one in June, and it's late June already.
And I think we should have one before the summer.
Which is typically quieter, typically.
**Tom Tan** 02:21 Okay, yeah, I think I just made a security fix in the contributor, and I hope that will also be included in the release this time.
**Marc Alff [MySQL]** 02:33 Okay.
In all the open PRs that we have, do you have any… specific things that need to be part of our ease?
**Tom Tan** 02:48 No, from my side, yeah, for OpenPR, which… Has to be included, no, no from my side.
**Marc Alff [MySQL]** 02:56 Okay.
Okay, DUGC2, which was added was, two things? Okay.
**Doug Barker** 03:42 Yep.
**Marc Alff [MySQL]** 03:43 Okay, who can take hook.
**Doug Barker** 03:46 So the first one's a question for you.
Because I think it involves, or will involve, the semantic conventions.
So what we are looking to do is to add, emitting an exception.
The exception is really just an event that has specific semantic convention-defined attributes in an.
**Marc Alff [MySQL]** 04:09 Okay.
**Doug Barker** 04:11 So, in order to emit it, some kind of… struct that we define, it really is tied to those semantic convention-defined attributes, so… the way that the API for the logger is constructed, implementing this in the SDK, would be… would mean that we add, you know, some concept of an exception, and be able to include the semantic conventions header in the SDK in order to add those attributes.
in order to include them from the logger side, it would mean including that header from the logger API, which what I've stated in the discussion is that feels backwards. Like, it feels like the logger API should never include semantic conventions. Is that understanding correct, Mark?
**Marc Alff [MySQL]** 04:59 Yes. So, I don't know if you noticed, but someone actually made a contribution recently on semantic convention itself.
Okay. Because, well… So the semantic conventions are all defined in YAML somewhere, in the semantic convention repo.
And there are many flavors of things. There are semantic conventions for spans, for tracing. There are also some metrics, and other things, and one of them is exceptions. So, we do have semantic ventures for exceptions, but these were never generated until recently.
So, someone made a PR to actually change the code generation, to actually generate all the constants for all the… all the exceptions that are defined in the semantic convention repo. So this is one thing. So at least now we have, We have a proper constant defined.
If someone wants to raise an exception, like Java exception this, or database exception that, they can.
The other thing, in my understanding, Semantic conventions, there are some semantic conventions which are defined by OpenTelemetry itself.
Just to have a common vocabulary for every instrumentation, basically.
But… Other third parties are also free to define their own.
Like, if you instrument your own application, you might have some semantic conventions which are for your field or business or whatever.
So, in any case, the instrumentation should be able to accept any attributes, just not only attributes which are listed in the same conv repo.
So… in that light, I guess it's up to the caller, like, when raising an event or raising a log.
to explicitly add, oh, I have an exception, I'm… Finding the exception with VAT semantic convention name and that attribute, and things like that.
The same way on a trace today, I think you can add some attributes, and you can even add links to other things.
**Doug Barker** 07:17 That makes sense. If you scroll down, so I put together, like, a little proposal what the call site might look like with some ideas.
Further down.
So I did… Yeah, so, like, this would be what it could look like if we included the semantic conventions in the logs API, which I think would be wrong.
But basically, that would follow the spec, which says you could pass an exception to a log record… emit log record optionally. I just… I just don't see how that could work, because then the logging API would have to depend on the Semantic conventions, header to actually set the attributes.
**Marc Alff [MySQL]** 07:54 Right?
**Doug Barker** 07:55 So… What seems to make sense is if we say that that's not allowed, we can't include semantic conventions header in the logs API headers, then what we could do is we could generate an emitException helper, similar to how we generate the, The metrics helpers for the various semantic convention-defined metrics.
That, if you scroll down, Little bit.
It might look something like this, where you pass in the logger.
And then you can, define your… Exception event as a struct.
But that would be defined also by the semantic conventions, like auto-generated.
But these objects.
the object for the exception event and the helper to admit it would be auto-generated and live in the semantic conventions header, is the idea. Like, one way that we could Support this part of the spec.
So that's… that's the idea. I think that the main question is, is, you know, do we want to try to support this? And if so… Would generating an exception event like emitter helper be the right approach, or should we consider something else?
**Marc Alff [MySQL]** 09:13 Not sure, because I have to… we'll have to dig into the details. One thing I… I don't know exactly how it works is, The logging API is making an extreme use of C++ templates, where all the attributes are stuffed together inside a huge template.
But, basically… Picks every attribute and populates them inside the log record itself.
it's… so, this is complicated code in the… which is in the… in the API surface, and I don't know how easy or how hard it is to… To add, something specifically for an exception there, for example.
If it needs to be a separate attribute with, its own values, or… I don't know what it would look like.
For, for a user to actually… Populate that exception part in the log record.
**Doug Barker** 10:18 Yeah, and what I was thinking here is, like, this helper would be auto-generated, but it would also be templated, so it would forward, you know, all of those different objects to the underlying emit log record call.
**Marc Alff [MySQL]** 10:30 Yeah.
**Doug Barker** 10:30 But it would take… Concrete, initial arguments for the logger of the event.
And so on.
But this is, you know, I think probably just the open question is, do we want to try to support this?
Omitting an exception.
Or leave it to users to define.
**Marc Alff [MySQL]** 10:52 Honestly, I don't know yet.
**Doug Barker** 10:54 Okay.
**Marc Alff [MySQL]** 10:56 If we… if we provide something which is more usable, why not? It's, The concern is… Do we… if by doing so, if we restrict the API too much, for example, that it can only work with semantic conventions generated from the same curve, but… but, It also has to work with semantic conventions used arbitrarily in an application.
So we cannot… We cannot always rely on generated code, for example.
**Doug Barker** 11:39 Yeah, I think… I think that makes sense. And one… one idea there is that we could auto-generate helpers to admit those standard exception events, too, because they have well-defined, The main thing that they differ is they have… each have a different event name that needs to be added.
**Marc Alff [MySQL]** 11:55 Yes.
But I think the only thing which is defined is the event name. Yeah. Attribute that goes with it, I don't… I don't remember if they are defined.
**Doug Barker** 12:05 They're just those standard ones, so it's the type, the message, and the stack trace.
**Marc Alff [MySQL]** 12:10 Let me try to find an example.
**Doug Barker** 12:31 the DB… Holy shit.
**Marc Alff [MySQL]** 12:39 I thought we had some exceptions somewhere.
**Doug Barker** 12:44 that DB events, that should be an exception.
**Marc Alff [MySQL]** 12:48 TB events, okay.
Yeah, so the only thing it defines is the name.
So it says… Here, this is typically, like, okay, a log event, some DB operation failed, whatever, and if you log an exception with it, it should be logged with that name.
Wow.
But it will not say, what is attached to it, if it is only one attribute, Many attributes, with an exception text and CRIT and whatnot, or things like that, so… But at least, yes, this, this PR is the PR that just added some, All the… all the exception to semantic conventions.
**Doug Barker** 13:54 Okay.
Yeah, that's helpful.
So I think in order to move forward with this one, we'll have to give some guidance to the contributor about should this… should we take, like, an auto-generated approach, where we generate a general emit exception event helper like this, with a corresponding struct?
Or do we, provide some… some other guidance? I think, like I said, the one that option would be to implement it in the SPK, but that would mean plumbing a lot of methods and APIs in order to determine if a log record is an exception or not. It doesn't feel like the right approach to me.
**Marc Alff [MySQL]** 14:45 Yeah, well, boo.
I guess it would be easier to see with an actual example, to see if we can Like, two styles of instrumentation.
What if we do it one way, what the user code would look like?
And what are the implications for the SDK, and the other way, same thing.
To see… To see what we can or cannot do, and to… In any case, once we decide on the final way to do it, it will need to be documented with an example so that people know what to do to instrument their code.
**Doug Barker** 15:25 Okay, sounds good. I can look at what it would look like with the, exception, being logged through the SDK, and put an example there of what would have to change.
**Marc Alff [MySQL]** 15:36 Okay.
Yeah, I'm sorry, I have not… dived so much into that cool area, so that's… that's about the help I can provide.
**Doug Barker** 15:49 Of course.
**Marc Alff [MySQL]** 15:52 I think you mentioned a different issue as well.
**Doug Barker** 15:59 Yeah, there was, an issue. As I was looking into the, the various packages for OpenTelemetry, I came across this, GenTube package management system, and there was a bug locked against the, I think it's a 1.25 release, so I just posted it here, but I think it opens up the… The question generally is, like, how do we… how do we communicate these… compiler definitions, which are generated by CMake and assumed to exist in the build, but for people who aren't using… who are building against a CMake-generated package, but they're using something else, like They're on make files, or… eyes.
How do we communicate what… Definitions need to be defined.
In order for the build to succeed. So this was a case where the OpenTelemetry Proto API definition was added, but it only works if you're using CMake and the user was not using CMake.
So it broke their bill.
**Marc Alff [MySQL]** 17:02 So… Yeah, so basically every time we have a flag, would you set by CMake, like.
or the ABI version number, or… the STL flavor used, and probably some things related to Epsilon and whatnot.
If I follow correctly, so it works if using CMake, because CMake will trans… will see the transitive dependencies and will see the definition of it somewhere.
But if you use a plain make file and just include data files from OpenTelemetry, you will never see that.
In that case, I think… Well… Yeah, it looks like we should, probably generate a config.ader file and install it.
That will contain all the… all the flags set, Which I decided at Brilliant, basically.
So… For example, if we decide to build OpenDemetery with ABI V1, the ABI version should be defined somewhere in that error file, and so when you install the libraries, you install the error files that goes with it and set those flags.
That could be a way.
But I'm guessing it's… Introducing some complexity to the install script and everything that goes with it.
**Doug Barker** 18:34 Yeah, we could generate it with, with CMake, and I think a user had logged an issue requesting this.
**Marc Alff [MySQL]** 18:40 Who knows?
**Doug Barker** 18:40 a year or two ago. I know there was some discussion about it.
Is that… is that something we should, Investigate, or what do you, what do you think?
**Marc Alff [MySQL]** 18:50 I think we can definitely investigate.
One thing I was hoping… well… To answer that question, I think the first question to answer is whether we should have all those flags exposed in the API or not.
Because it's the root of all evil here, so… If you have… if we have just a bunch of error files which are installed, and you compile against that and have something clean, that's enough.
Unfortunately, at least because of ABI version number, Just that alone.
Oh… if you compile against an application against OpenTelemetry, at some point, you need to say whether you are using ABIV1 or ABIV2.
Because that… But information is not part of… What is installed.
So… From that point, either we document that, hey, in your application, you need to set those flags yourself, which could be one way.
It works, but it assumes that those flags are in sync with whatever library was built.
Which is very risky.
Because if you… if we compiled… if you… we compile OpenTelemetry, some libraries with this and that feature enabled.
And this and that flag, and the application is compiling with something else, it's… Likely to cause a lot of chaos and clashes.
So it's… it may work, but it's… it's weak.
And the other solution is, well, instead of telling the user which flag to set, generate this config.header file, and ask the user to just include it.
Or even better, make sure that it is included in our editor files, so that when building, it will be seen, and it will be then built with the proper flags.
And if we do that, I think that should work.
Oh… as far as I know, we… I don't know how people are packaging OpenTeametry, or if they are even packaging it, because we have so many flavors and so many build flags, but it's something that has been there forever and has never been truly resolved, to say, okay.
Like, if I want to build OpenTelemetry and install it somewhere, well, there is just not one choice. There is, do you want gRPC, do you want OTLP, do you want Jipkin? And all those flavors, which are… At the end of the day, causing different builds to have different shapes, which is… Unfortunate.
**Tom Tan** 21:56 One more thing is, can we just see… either CMake or Bazel are required to, to, like, to… to reference our package on the Never Through… Include directly like that.
**Marc Alff [MySQL]** 22:14 Well, for Bazel, I think the way Bazel works, you see all the Bazel dependencies, so… you build the entire application at once, so you get the flags that were set by Bazel.
And on top of that, We don't have that many Bezel flags anyway, so… If you… if you build with Bazel and include Zipkin, you get Zipkin. If you include the OTLP HTTP exporter, you get it, and things like that.
so it's more of a CMake. At work, we are using CMake, but the… I think we set the… yeah, in one place, we set the flags that we need.
like, oh, take this exporter, not that one, a couple of things like that. And I think from memory that those are, kept transitively inside the build, so that we… We do a build of all the dependencies in the product, and have something consistent because of that.
But we don't use plain make files. Anyone using a plain make file in OCMake will fall into all those things, because they are likely to have some different, build flags.
Which I guess is the issue here.
**Tom Tan** 23:42 I mean, we just documented that that is unsupported scenario for us, like the current issue.
And maybe keep it open if some, like, the… generate a separate install config header, that's an option, but I'm not sure that can be done very soon. That is also a break and change, right?
**Marc Alff [MySQL]** 24:03 I… Don't think it will be a breaking change, Well, maybe people… yeah, so if we start to do that, people who set their own flags might have to… To remove it and rely on the flags which are installed.
So, yes, there could be some breaking change, at least in the makefiles, not in the code itself.
**Tom Tan** 24:27 Yeah.
**Marc Alff [MySQL]** 24:28 But it will fi- it will… it would fix, everyone using… the include of Edo files directly.
**Doug Barker** 24:44 We do provide the, package config files, too, which are generated with the CMake installation, so I don't know if people are using those. I don't think we're currently really testing them.
They are provided.
**Marc Alff [MySQL]** 24:59 Yo.
And this is something related as well. I mean, error files and build flags are one thing, but there is also all the naming of libraries and the transitive dependencies of libraries.
If you CMake… It will know which library to add to the application and link everything correctly, presumably.
But if you use a pen make file, every time we change a library name, or every time we say, this library depends also on that library, you have to adjust your final link statement to put everything together, otherwise parts will be missing.
I mean, for someone using a plain makefile, that is.
**Doug Barker** 25:59 Yeah, it seems like we've opened the door to using Plainmake files because we provide the package config files.
**Marc Alff [MySQL]** 26:05 Yes.
**Doug Barker** 26:06 So I don't know if we can… Say it's not supported.
**Marc Alff [MySQL]** 26:10 And to be honest, we cannot force people to never do that. Some people will use MakeFile no matter what, so…
**Doug Barker** 26:17 Right.
**Marc Alff [MySQL]** 26:20 But at least, yes, document… if you use a makefile, you need to be aware of this and that and that.
I don't even remember what this proto API is for… In OpenTelemetry.
**Doug Barker** 26:44 Something that was added, recently, I think, to support providing additional attributes on the DLLs for Windows.
**Marc Alff [MySQL]** 26:55 Oh, okay, so it's Windows-specific, yes.
**Doug Barker** 26:58 Yeah, but it's being applied unconditionally to all platforms, so, like, that could be one fix, is just to only apply it for Windows, but it would address the bug reports. I think they're probably using Linux, or a flavor of Linux.
I think it gets back to that.
larger question of what are these declarations should we actually expose publicly? I think a lot of them can be moved to private to the SDK.
And then, should we have a config header file that includes them by default, so it's easier for people building outside of CMake?
**Marc Alff [MySQL]** 27:34 Yes.
Yeah, well… Not knowing the exact solution yet, it's definitely something we need to look at anyway, because the… The way we install things, is… It's blurry at best, because we have so many compiled flavors, and… Different… well, yeah, different flavors that can be used.
**Doug Barker** 28:10 What do you think, Mark, of a follow-up issue? Because we already, I think, in several PRs recently, had called out the names of those preview… declarations, which don't.
**Marc Alff [MySQL]** 28:19 I don't have.
**Doug Barker** 28:20 the open telemetry prefix, so I could open up a separate issue where we look to move those.
**Marc Alff [MySQL]** 28:28 Oh, yes, this is definitely a no-brainer. We need to have things in the OpenTelemetry namespace. Okay. I've seen… actually, I've seen that internally as well, when consuming OpenTelemetry. In many cases, a symbol defined by OpenTelemetry would clash with something else defined in our own application.
Like, with Basil, for example, things like that.
I mean… Hmm… Open… if OpenTelemetry wants to use Bazel because of gRPC, that's one thing, but that should not imply that all our application is using Bazel all over the place, so it's… it's causing clashes in many areas.
And… So, yes, the proper thing is to just rename things so that If we say with, who, and without bar, that should limit the scope of that choice only to OpenTelemetry and not everywhere else, transitively.
So, yes, for renaming, we're definitely invest in.
Okay. And we can do it independently, because… It doesn't depend on, how… if we generate a header file with the settings or not, I mean, we have to rename anyway to avoid name collisions.
**Doug Barker** 29:51 Yeah, I think that makes sense. So that can be maybe two issues. So one, to do that, move the SDK preview flags off of the API and prefix them, and then… Another issue, maybe, to discuss or decide if we want to do a, config header file with the remaining API definitions.
**Marc Alff [MySQL]** 30:12 Yes.
**Doug Barker** 30:18 Sounds good.
**Marc Alff [MySQL]** 30:19 Okay, and I guess we want to do that before the next release, then?
Or do we wait, or do we always know and do that, In our own time.
**Doug Barker** 30:35 I propose that we address at least this bug somehow. I don't… what that could be like. Like I said, the easiest thing would be just don't define this on Linux, only define it on Windows, because that's where it's used.
It could also be addressed with the config header file if we decide that that's non-breaking, which I… we'd need to look at it to see if that's something we could release now.
**Marc Alff [MySQL]** 31:02 It was, like, things like the renaming that would be, easy.
Things like… so we can do it before we release.
things like generating a data file on the fly, and make sure that install works and the application is not broken. This is more risky.
So, I don't think it's realistic to do it just before releasing.
Because we might have, unforeseen things that we did not anticipate that we need to fix, and… Stuff like that.
**Doug Barker** 31:38 Yep, makes sense.
**Marc Alff [MySQL]** 31:40 Okay.
Oh, there's one thing I wanted to… to discuss quickly, which is… the PR, so I'm trying to merge as much as we can when things are… progressing. Some PRs, are basically stuck with some comments that are not addressed, so I don't know if, The offers are in vacation, or… Went to something else, or we'll come back to it, so it's, it's on hold.
One thing, though, is, everything related to… where is it?
Yeah, CTW.
We have 2 or 3 PRs, I guess, related to ETW.
Tom, do you want… do you know if it's realistic to review them before the next release, then?
Oh, we'.
**Tom Tan** 32:47 I think I reviewed it, I had and left a comment there, that was concerned, I'm, PR, so…
**Marc Alff [MySQL]** 32:54 Okay.
**Tom Tan** 32:55 Yeah.
So, yeah, we'll see whether the comment was, addressed, and, I think no hurry to… to merge them before the next release.
**Marc Alff [MySQL]** 33:17 Because this one, for example, is… Well, maybe it has comments from you and Lalit, I don't remember. Yes, I'm Lalit.
But that, yeah, that was a month ago, and I've not seen any activity since on this one, and the next.
Yeah, so it's, I guess it's unclear whether there is something… there is a command to fix in the code, and then the router should do something, or if it's waiting to be reviewed, I mean, it's.
**Tom Tan** 34:06 Okay, I think, I mean, the others, the other… fix on Tracer, ETW, maybe not this one, maybe, yeah.
**Marc Alff [MySQL]** 34:16 I think there's a third one somewhere.
Oh, yes, miss.
Yeah, so this one, you had some comments?
**Tom Tan** 34:58 Same, is that targeting the same way, I think.
**Marc Alff [MySQL]** 35:03 Sorry, say that again?
**Tom Tan** 35:04 I mean, the PRS are targeting the same issue, the lifetime Oh, True, sir.
**Marc Alff [MySQL]** 35:17 I'm sorry, I just missed that.
Which VR, this one, or the previous I looked at?
**Tom Tan** 35:24 This one, and the one from… on the linked, PR.
Yeah, and yeah, and not this, that's another one also, yeah, the span end. Okay. This one.
Yeah, but let me take a more look on all these ETW-related VRs.
**Marc Alff [MySQL]** 36:25 Okay, I guess what I'm trying to understand is… is something that needs to change with a PR, in which case we have a comment somewhere, or… Is it something that can be approved and merged? Because it's… I don't see sign everywhere.
**Tom Tan** 36:43 I think I looked, and maybe lost some context here, yeah.
**Marc Alff [MySQL]** 37:09 Okay, in any case, could you, or maybe Lalit, look at the status of those to… and indicate what should be done?
**Tom Tan** 37:18 Yes, yeah, we were thinking, look at, look at them.
**Marc Alff [MySQL]** 37:22 Okay, thanks.
**Tom Tan** 37:24 No problem.
**Marc Alff [MySQL]** 37:27 Nous veins… you know, those are free things on ETW, and It would be good if we… well, if we… if we can take it for a new release, then, That will be free out of the way I guess.
**Tom Tan** 37:46 Okay.
**Marc Alff [MySQL]** 38:14 I don't have anything else in particular. One thing… so… A long time ago, what was it? It was Include what you use was upgraded to a new version of C-Lang.
And that caused many, many issues to show up, which have been all fixed.
So, all the… include what you use, Bill, is back to zero issues.
In… in all the different, breed flavors, which is great.
The same thing also happened with Zengtidy.
But, I think we still have a lot of things to clean up for C9 Tidy, because we are still at, 300 and something, what was the, from being CIA.
Yeah, we used to have… quite a few things to… to address.
I have not looked at these, recently, But I will try to take a look again to see if we can somehow decrease that number.
Oh.
It's, at some point, we're at 600, so a lot of cleanup has been done, but it's slowed down… the cleanup has been slowing down recently, so I guess we need to take a look again.
And I would do it, or maybe also… code reviews. I mean, if we do fast code reviews, I've noticed that people will be more inclined to submit new cleanup and and have one more PR approved and merged and things like that, and when we slow down on code reviews, Indirectly, it also slows down the rate of contribution.
Which is understandable, because people are… maybe they lose interest, maybe they… they get sidetracked with something else.
**Doug Barker** 40:17 So one thing, I think that helped in the past was just logging specific issues for the groups of warnings, and maybe that helps us coordinate, too, if you and I are gonna take on a few. Should I, Break them out like that again?
**Marc Alff [MySQL]** 40:31 You mean by type of warning? Yes, So, it helps you in many ways. I think it helps, first of all, to… avoid collisions, so that we don't have many people doing the same thing. And also, it helps on reviews, because I guess it's much easier to fix the same type of issue, like maybe typecasting or whatever.
in different places of the code and get rid of it, and then go to the next issue, as opposed to COPR that fixes 10 warnings, but… One of them is a typecast, one of them is some overflow, one of them is some… Other things that… it's much more difficult to review that way, because we have to jump from left to right all the time.
So, yeah, it's, getting some hints that, we need to fix this area, then this area. I think that could help.
**Doug Barker** 41:29 Alright, I'll log a handful of issues with the groups of warnings.
**Marc Alff [MySQL]** 41:34 Okay, thanks.
just so you know, so I will start to work on the release. This is going to be the summer, so I guess everyone has vacation plans at some point.
I'm… I don't have firm dates myself, but I will be on vacation at some point, so expect some slower responses, and… when I know the dates, I will send them to you as well.
**Tom Tan** 42:10 Thank you.
**Doug Barker** 42:12 Sounds good.
**Marc Alff [MySQL]** 42:37 Anything else that I missed?
Oh, one thing. I tried again, so, so Duke, yes, you did an upgrade of gRPC and portable for CBank.
I tried to do the same upgrade for Bazel.
And I've been trying way too many times on that, for some reason.
Oh… CR in Bazel fails on Mac only.
with some arcane failure that I don't even understand. It's not even a failure in our code, it's a failure somewhere else.
And I'm just about to give up on this, and close that PR, and… hoping that by the time the next release of either gRPC or PoloBuff, shows up, maybe they will address that issue.
Because I don't think it's something in our control, somehow, somewhere.
The build is failing only on one platform, but it makes no sense why.
And…
**Doug Barker** 43:40 Yeah, I saw that too. I looked into it briefly. It looks like it might be a GRPC bug.
So… We might have to wait until the… an update.
**Marc Alff [MySQL]** 43:51 Yeah.
So yeah, I was hoping to get aligned between Bazel and CMake, but it looks like it's not going to happen.
**Doug Barker** 44:03 Yeah, and I was thinking of updating the docs on that, too, because I know there was an issue where somebody was asking, you know, why aren't these aligned? But I think… even if you look at curl, curl is a very old version on, Bazel.
Whereas, if we build with, you know, the latest version, they've fixed a lot of security vulnerabilities in the last two releases. So I think, like, we should always, at least my opinion, is we should always be trying to promote using the latest versions of these dependencies, and Basil may… may… may lag, just because I think even, like, Curl is on a… Maybe it's a year old or something, but it's a relatively old release.
**Marc Alff [MySQL]** 44:45 News.
Yeah, internally, we don't… well, we don't depend on Bazel, we use CMake.
And also, we don't depend on fetching content somewhere else. In fact, we upload the dependency first. We check that into our own repo.
They don't always build it from the colonial ripple.
And… In general, we are pretty aggressive of keeping dependencies up to date.
For things like current and current trends, so… Precisely for security.
**Doug Barker** 45:24 Yep.
That makes sense.
Okay.
I may, take a shot at updating the documentation, just saying that we'll, you know, the project will aim to use… promote the latest, and it doesn't guarantee that Bazel and CMake will be the same version.
True.
Yeah.
**Marc Alff [MySQL]** 45:42 Well, for CMake, we have some control, because we can pick. For Bazel, we depend on the Bazel Central repository.
Which is yet, I think that something goes.
By the way, I noticed also, thanks for that, that you did an upgrade on Rapid YAML.
**Doug Barker** 46:00 Yep.
**Marc Alff [MySQL]** 46:00 And I was surprised to see that, even then, so, yes, so Rapid YAML moved some things in a separate header file, it seems, which broke the build, so that now we have to have an if-def MLDefine.
to include this header, depending on what version, and things like that, and… I guess this is the kind of things that just happen all the time.
**Doug Barker** 46:27 Yeah, I think it's gonna be expected with that library while it stabilizes, but at least it's active. It's an active library.
**Marc Alff [MySQL]** 46:32 It is very active, yeah, it's nice.
Okay, so, yeah, I don't have anything else, so I will work on the next release.
Oh… If… so, as usual, if you see something that needs to be in the next release, just comment on the issue for that, so that I can keep an eye on it.
And wait for it to be merged.
**Doug Barker** 47:07 Sounds good.
I'll, There was a PR, I think, that we had talked about last meeting, but there hasn't been an update on it for the CMake change to, the configuration.
targets, so I'll comment to see if that contributor is still working on it, but I really want to get that in for the release, so if they're not working on it anymore, I might open up a PR to make that quick change.
**Marc Alff [MySQL]** 47:32 Okay, sounds good.
**Doug Barker** 47:40 Alright, that's it for me.
**Marc Alff [MySQL]** 47:42 Alright.
Too many last words?
**Tom Tan** 47:48 No, no, nothing from my side.
**Marc Alff [MySQL]** 47:51 Okay. By the way, I don't know if you noticed, but Owen also made an update, concerning his own situation, so… No.
I don't know the full details, but he disclosed that he's no longer working with Tencent anymore.
So, I'm hoping he can, well, first of all, find another job, and Also, that he will still have the time and interest to contribute to OpenTelemetry as well.
**Tom Tan** 48:21 Okay, I see.
**Marc Alff [MySQL]** 48:23 I… I know that, So, he has been very active, especially on the OTLP side with gRPC and things like that, and also from… so, Duke, from history, Owen has been using OpenTelemetry in production for a very long time, but also on very old, old systems.
To the point that, we were to keep NCI builds using some extremely ancient version of gRPC and Portoburf.
Which, at some point, even caused problems, because they were not supporting… they were barely supporting C++11, and not supporting C++14 at all, things like that.
So, I'm… I don't know the full extent of the story, but recently, it was not so much insistent on keeping old releases, so I guess Tencent has been doing some upgrade.
Yeah, it seems.
And in any case, if he's no longer at Tencent, I guess he's… he won't… He will no longer have access to the production systems he was maintaining, so… Oh… I'm guessing the, the need to support all releases will be less and less.
In that case.
We… we don't need… I haven't heard of anything specific to C++11.
And, oh, and even made the point that, which I think I saw a PR from him, to use Make Unique all over the place, Where, in the past, he would insist that we do not use Bank Unique, because he had some older C++ standards to support.
So, that's, we… that's probably, changing the… we don't have so much pressure in the past as to supporting some variable configuration. That's the bottom line.
**Tom Tan** 50:29 me, we can maybe start to remove some of the portfolio for C++11, because we even don't need that.
And do we clocked it.
14.
**Marc Alff [MySQL]** 50:43 Yeah, I think we require 14 anyway, But at some point, the question will also… we are in 26 today, so the question will still stand, okay, do we do something for 17, for 20, and so forth.
The other thing which is driving all that is the way all the Google code is maintained.
Especially with Absolute gRPC, portable, and friends.
They have a policy which is linked somewhere where they support the older compiler on the older platform, or something like this, and by the time the platform goes end of life.
then a lot of dependencies can be upgraded. And we had to follow with it anyway, because if we do a build and we don't have the latest library I mean, if we use a library which is no longer supporting C++14, for example, then we will have no choice but to upgrade to 17.
So, in general, we are following the flow of that.
**Doug Barker** 51:54 If you logged an issue a while back about C++17, it would be nice to, at some point, put that, Put that on a timeline.
**Marc Alff [MySQL]** 52:05 Nope.
**Tom Tan** 52:09 When was we upgraded to 14? Maybe last year, or…
**Marc Alff [MySQL]** 52:15 One… or maybe two years ago, I don't remember.
**Tom Tan** 52:17 Three years ago.
maybe… Three years after that, we can… we can… we could plan to upgrade to 17 as our minimum requirement.
**Marc Alff [MySQL]** 52:27 And surprisingly, I haven't heard of many issues or pushback on that, so the only person who was really concerned about the support for C++11 was Ovent.
**Tom Tan** 52:40 Okay.
**Marc Alff [MySQL]** 52:48 So anyway, let's hope that he will continue also to do some contribution. He has done some great, great works.
Especially for the… all the asynchronous code also, it's, went all over the place, so…
**Tom Tan** 53:03 Yes, sure.
**Doug Barker** 53:04 They're funny.
**Marc Alff [MySQL]** 53:11 Alright.
So… It's getting late, so I guess we are, it's time to, finish the call. Thanks, everyone, for attending, and for the discussion.
**Doug Barker** 53:27 Thanks, guys.
**Marc Alff [MySQL]** 53:28 Yep.
Bye now, thanks, thanks everyone.
**Tom Tan** 53:31 Talk to you later.
