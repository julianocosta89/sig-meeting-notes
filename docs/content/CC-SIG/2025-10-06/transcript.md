SIG: OpenTelemetry C/C++ SIG
Date: 2025-10-06
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/82dUNWwem5qPV5wfuxbVKJ-TwsSwS7UnBz92lLvHkmqtdgx66X5vHaIaojUeazc.BXZGYpoKtyIGG76R
============================================================

## Zoom Recording Transcript

**malff** 00:58 Hi, everyone.
**Pranav Sharma** 01:00 Hey, Mark.
**Nikhil Bhatia** 01:01 Hi, Mark.
**malff** 02:12 I don't know if, Lalita and Tom Indulget are joining today, so… We can wait a bit.
In the meantime, anything special you want to discuss?
**Nikhil Bhatia** 02:23 Yeah, Mark, actually, I have raised that PR for batch log, record processor options, so…
Yep.
**malff** 02:31 Yeah.
Yes, I saw it, I took a quick look, it looks okay to me, so we'll probably approve it after that.
It's all thanks, yes.
**Nikhil Bhatia** 02:44 Thanks, man.
**Pranav Sharma** 02:51 Yeah, nothing from my side. Been, I was on a vacation, and then there was too much work stuff, so couldn't really work on it.
Sorry.
**malff** 03:33 had a few topics to discuss, but one of them is really for Tom, because he knows this area, this is related to the Windows export, when we have a single DLL.
So I guess we can wait next time for that.
and add other things also in CPP Build Tools to review, but We, we need,
More people for… to join, then.
**Pranav Sharma** 04:03 Hi, Dug.
**malff** 04:39 Hi Duke, can you hear us?
**Pranav Sharma** 04:53 Hmm.
**malff** 04:55 Looks like no, but…
**Pranav Sharma** 04:57 Huh.
**malff** 05:10 Okay, so yeah, we're seeing the…
that we need to wait for Tom. He's the most familiar with that area.
although, Doug, if you can hear me, I'm looking at…
Improving the CI coverage for the Windows DLL, because it's,
we need to make sure it works. There are a lot of,
Issues reported about that right now.
Hi, son.
**Ehsan** 05:45 Hi, Mike. Hi, everyone.
**Pranav Sharma** 05:48 Hey.
**Doug Barker** 05:56 Hey, everyone. Sorry, I got my audio figured out.
**malff** 06:00 Haha, great.
Hi, Luke.
Yeah, I was saying, I don't have a lot of topics, the…
Two items I have is for the Windows DLL build, I think it needs a lot of cleanup, we need to take a look at that.
And the other topic is some small PR that I just did on CPP Build Tools, which is the place where we maintain the… all the formatting scripts that we use.
Now that we have shell tests, test cases in the repo.
We also need to make sure that we don't format the shell test file, because it's causing chaos.
So I did a small PR for that, if you have a chance to take a look.
And when… when this is done…
I would probably make a new release for CPP realtors.
Oh, dear.
So, this is the PI itself.
Only.
Only one… well, two lines, actually, just two… Ignore those things.
And I would make her… make her a visa afterwards.
Dugo, Aesan, anything you want to discuss in particular?
**Ehsan** 07:30 No, nothing from me.
**Doug Barker** 07:34 We'll probably go over, but just my, PR to, update the third-party defenses.
**malff** 07:40 Okay.
Yeah, I saw the PR, I didn't have time to look at all the details yet.
Do you want to… Cover the snow, or…
If I can find it…
**Doug Barker** 08:12 Yeah, so basically, this one just takes the strategy that I proposed in that ticket, which is to update all of the third-party dependencies in the third-party release file.
And then update those corresponding submodules.
One issue that I ran into.
And, I probably won't add to this ticket, was the Basel build, and trying to update its dependencies, so…
I was running into a lot of, build errors with that. I don't know if it's just, like, not getting the right combination of gRPC and protobuf.
Any other dependencies that they have.
But what I'd like to do is just merge this in as the upgrade for all the dependencies that CMake uses, and then we figure out Bazel in a separate PR.
**malff** 09:01 Okay.
Yes.
So all the CMA code is,
all located inside the CPP repository, so we don't depend on anyone else.
whoever forbids them.
when… Let's see…
In Bazel, when we have a dependency like that, like curl or gRPCN or whatever.
Those things actually point to the Bezos Central Repository, which has some make… well
makefile-ish for Bazel. Well, it's not a makefile, but it's a Bazel equivalent to actually build,
Jobby Seeker and whatnot.
So, it could be that,
those things, do pick C++14 instead of C++17, for example.
So that when you… When you change VAT and, in Bazel, if you change
one part in the CPP repo, and another part which is not changed in the Bazel Central repository, it could be that we end up with mixing things.
But that could be causing some chaos, so…
**Doug Barker** 10:22 Yeah, there was some of that. There was also, like, upgrading curl to… I think the latest one they have is 8.11. It's not compatible with the version of Basel that we're installing, so then you have to upgrade Bazzle for that.
And then there's also upcoming limitation with, the latest protobuf. So in Protobuff 34, so in 2026, they're gonna drop support.
for building with, Windows and Bazel entirely, with ProtoBuff, so…
**malff** 10:50 I see.
**Doug Barker** 10:51 And they have a build warning now that causes an error, so we have to set some special flag to get around that. So I think it's just, like, a whole other effort to upgrade the dependencies with Bazel.
**malff** 11:04 Okay. Yeah, those are… those are…
Bazel and CMake are very different build systems, and they're just parallel builds, so…
Probably better to only touch one at a time.
du basin.
**Doug Barker** 11:19 Agreed, yep.
**malff** 11:33 Yeah, so, thanks for PR. I will take a look later, but, looks good to me. I saw that, yeah, you reverted some basel things, and everything
Passes now, so… It should be okay tomorrow.
So, yeah, so, oh, one thing, I think I mentioned that briefly last time.
Github is…
Upgrading the macOS images and removing this one, which is old.
So… probably have to upgrade CI for macOS as well to keep up to date.
So, this is something coming soon.
They say they will retire that in December, but in the meantime, there are… Pre… dates where the…
the GitHub workers will be unavailable just to…
Intentionally causeable failure to so-called raise awareness so that people know that it's coming.
So if you see something weird, like,
something that works one day, and the next day, CI is failing, especially on… specifically on macOS. It mostly… most likely will be related to that, and not to the… not related to the PR itself.
Something to be aware of, and that we need to fix.
And, yeah, as I was mentioning earlier, that we have a lot of…
A lot of complaints on,
the way we export things on Windows when we make a single library.
So, one thing is, it's not working for both ABI V1 and V2, so we need to fix that.
But even then, there are a lot of things that we… Which are missing.
And… I don't know, Isan, maybe you know the history of that?
There is one part I don't quite understand, is that, on one end, we have OpenTelemetry export that we put in the code.
So, I was thinking that that would be sufficient to just export a symbol, but also, on the other hand, we explicitly export some symbols that way, in a special file, which is this thing.
And…
It's… it's a bit surprising to see we have both, so I don't understand quite why we need both, and…
If we should put… should put…
The exporting the code and a symbol in that file, or if…
Only one is sufficient, or what's the… what's the stories?
So… If you know…
**Ehsan** 14:38 Yeah, tentacle.
**Tom Tan** 14:44 And, which one of the means should be sufficient to handmark?
**malff** 14:51 Well, I'm just surprised we have both, so…
**Tom Tan** 14:54 I would like to understand why, like…
Yeah, I just missed maybe the first part. Which, which part of both do you mean we need for this SRC file?
**malff** 15:07 Well, when we… when we export something.
**Tom Tan** 15:14 Okay, you mean the… the… le…
the Clarice spec, and also the SRC.
**malff** 15:21 When we export something, we put that in the code itself.
Marker Class has exported.
**Tom Tan** 15:28 Okay.
**malff** 15:29 and… Typically, that should be enough, because that declares the symbol exported.
normally.
And somehow, we do that, And we… we also have this magic,
input file, which is processed as a definition file later, and given to the linker to do some post-processing of some sort.
**Tom Tan** 15:52 Yeah, I think just the declaration is not enough, because
I vaguely remember, because if the…
If… because we are building library, and if the class function is not used anywhere, it can be removed, so we have to put that into the…
SRC file for… and pass that to the linker, then the linker will… Cape it and export it.
Maybe one reason, but I… yeah, I think there is reason to have both of them.
I can dig more into it, I think I… maybe I added this, I added it as RC file.
Yeah, because most of the declaration is built into library, right? And when you link that to the DLL, that's a final executable, it doesn't export everything marked as export here in the library, because that could be too much to…
And especially the library function is not directly, like, used in the DL, because, you know, DL is just an empty wrapper, right, in our DL. It doesn't do anything.
It has… yeah, it even… it links to the library, but it doesn't call the library function. It just needs to expose the library functions.
**malff** 17:16 Okay.
**Tom Tan** 17:17 Yeah, so we need a mechanism to… Explicitly mark them as Alive and explore to them.
I think this is… the… Top reason for this, maybe some, some other…
**malff** 17:34 So, yeah, so something about… Symbols that just disappear.
Another thing… So this is the magic file.
**Tom Tan** 17:48 Yeah.
So in the main file, you don't do anything, so…
**malff** 17:51 Yes.
**Tom Tan** 17:52 Yeah.
**malff** 17:53 So another thing… a lot of things are missing from this list.
Okay.
**Tom Tan** 18:00 So, with some extra, yeah, V2, I'm assuming.
**malff** 18:03 So, yeah, we need to…
to have some more code, then, to make sure that this can be either for V1 or for V2.
**Tom Tan** 18:12 Yeah. But on top of that, the main thing is the makefile itself.
**malff** 18:20 Where's that?
Do you remember where the make file is to… to… Builder installed tests for that?
**Doug Barker** 18:36 Open the install test, it's gonna be an install… See mate.
Sorry, insult to see me.
**malff** 18:49 Sometimes it's generic.
**Doug Barker** 18:51 Yeah, components.
Well, there's a DLO.
Under the components test.
**malff** 18:56 Component tests… Okay, oh, yeah, and there should be DRL somewhere.
**Doug Barker** 19:01 Okay, this one. Yeah.
**malff** 19:06 So…
**Tom Tan** 19:11 So, anything's missing here in the…
**Doug Barker** 19:15 You're talking about the examples test, where we…
**malff** 19:17 Yes, examples test.
**Doug Barker** 19:20 It's actually, done in the, CI.ps1 script.
**malff** 19:25 Oh, that's right.
Exactly.
**Doug Barker** 19:35 And then if you search for the DLL, it's just… Summit.
It sold me all the classroom.
Something similar.
**malff** 20:03 An enclosure, yes, so this one.
So… This is the test where we compile all the installation tests with the DLL. However.
A lot of things are just disabled.
So, we only check that the symbols from the SDK itself are exported.
**Tom Tan** 20:24 But we don't check that GRBC symbols are exported.
**malff** 20:28 HTTP, are exported, and so on and so on.
So, everything which happens in those libraries, or in that codebase, It's most likely broken.
And he's missing some exports.
**Tom Tan** 20:42 Yeah, unless I think the macro is, like, checked in the SRC file, if it is not there, it is currently not supported.
Like, the… I think with OTLP, HTTP is supported, right?
just check the SRC file, there's quite a few.
**malff** 21:00 There is, but it's not covered in CI.
**Tom Tan** 21:02 Yeah, okay. Okay.
**Doug Barker** 21:05 I think it's broken, so I think something's missing on the OTLP side, that's why I had to turn it off, and I think…
**malff** 21:11 Time zone.
**Doug Barker** 21:12 You had a, a CRM trying to turn that test back on, and it's… Yeah, I have one.
**Tom Tan** 21:24 Okay.
**malff** 21:24 So, we… most likely, we have a lot of cleanup to do for that.
to expand the CI, to expand to ABI V2, and to make sure that, Every symbol is there.
**Tom Tan** 21:37 Yeah.
**malff** 21:37 missing.
**Tom Tan** 21:38 We need to do some more work on that.
**malff** 21:40 Yeah.
And… world.
I'm lost.
Yeah, and this should take care of issues like that. I mean, there are several issues from the same reporter complaining about this,
With single DRL, in fact.
**Tom Tan** 22:10 Okay.
**malff** 22:18 Yes, as I was saying earlier, I made some recent change to build tools. There is a new PR there.
Which is… Oh, it's approved. Okay, thanks. I don't know who did that, but… Thanks, Hassan.
I was about to ask for reviews, so thank you.
So that is… that is done.
Yeah, so apart from those two things, I don't have anything special to discuss. Do you have any topics?
**Tom Tan** 23:00 No problem, I said.
**malff** 23:06 Okay.
Do, just so you know… Nope.
For the YAML file, YAML configuration, I have one… one last PR which is coming. It's… it's very small.
But it's, well, the code is an integration PR, but I would make a clean PR out of that.
This is the last change that I have.
Which is cured.
And apart… when this is merged.
Basically, all the main… the code in the main repo will be up-to-date with what I have, so…
Which would be… so then we can just remove the integration PR and avoid having to
Keep code on the side and merge it once in a while, because it's, it's taking some time as well.
getting extremely close, only one PR away.
**Doug Barker** 24:06 Awesome. Wonderful shower.
**malff** 24:24 I haven't seen anything… well, apart from the… what we just discussed, I mean, for older PRs, I have not seen anything changing recently.
Do you have any PR you want to discuss in particular?
I don't feel like going in the old list again.
Don't you know what's the…
what's the outcome with copy-dot, experiments, whether we…
whether using Cubanote is actually, working.
**Tom Tan** 25:05 Anand, what's her ask?
**malff** 25:08 So, I think, or maybe it was Lalit. Lalit tried to use Copilot to do some, either some reviews or to generate, PRs. Do you know how it is working, and what's the status of that?
**Tom Tan** 25:24 I think from… based on my discussion, it's like, I think it worked fine, like, for… for small features, or… and many cleanups, and maybe not for… for some big feature work, so…
Yeah, I think that our feedback is very positive on using Copilot in.
In that repo.
**malff** 25:42 Okay.
**Tom Tan** 25:47 I think there's one weird thing about Copilot, is that I think we found is, and for code reviewer, like, I think just last week, I'm not sure it is still, up true, for the reviewer, if, like, you read the comment.
and ask Copilot to make some change, and then Copilot followed your suggestion and proposed the change, and then… then the reviewer is not… is not considered as a, like, valid reviewer, because not considered that the code is contributed by the reviewer, so…
The approval will not be counted.
Not sure if this is an issue or will be fixed, but that's the current status.
**malff** 26:33 I see, okay.
**Tom Tan** 26:34 Yeah.
So if you… you just approve, yeah, that works, but if you provide a comment, and the copilot follows it and makes
Current, like, update, then your approvals will not be considered, because that means you approve your own code, like that.
**malff** 26:51 I see.
**Tom Tan** 26:53 Yeah.
**malff** 26:57 Yeah, so just something to be aware of.
**Tom Tan** 27:03 Yeah, that means, like, if we… all… all of our approver and maintainer, like, comments on our PR, and Copilot follows it, then no one can approve the PR.
**malff** 27:17 So at the end, we just have to take the pattern…
**Tom Tan** 27:20 B.
**malff** 27:20 And he threw another pill.
**Tom Tan** 27:22 That's true.
**malff** 27:30 Okay. I forgot to mention, we have, So, the…
this contributor, he contributed a fix a while ago on some waste condition happening in the SDK somewhere.
I don't remember the details, but it was…
a valid risk condition, and that guy obviously knows how to debug the OpenTelemetry CPP code and to investigate things.
And now he's contributing, improvement for multiple instruments.
I'm not sure who, who is doing a review on that. I see that Owen, provided some comments.
And Alitz, do you want to…
Should other people take a look at that as well, or do you think it's,
That it is sufficient for the… for the metric code.
**Tom Tan** 28:28 Yeah, I'll take a look and also sync with Ladita on this one.
**malff** 28:32 Okay.
Because it's, it's a very nice, improvement, and something which has been missing for a while.
**Tom Tan** 28:40 Yeah, that's true.
**malff** 28:48 Okay.
Okay, I don't… It's getting late here because of a time difference. I don't have anything else to discuss.
Anyone, do you have any… anything… any last thing that you want to…
discuss other in general, or issues, or PRs, or anything, really.
Otherwise, we can just close the call then.
**Ehsan** 29:33 Thanks, Mark. Thanks, everyone.
**malff** 29:35 Yeah. Okay.
And, yeah, thank, thank you everyone for joining.
And, see you soon, Ven.
**Pranav Sharma** 29:44 Thank you.
Yep, yay.
**Nikhil Bhatia** 29:45 Hi, everyone.
**malff** 29:47 Yep, thanks everyone. Bye.
**Tom Tan** 29:49 Bye.
