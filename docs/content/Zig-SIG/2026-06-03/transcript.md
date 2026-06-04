SIG: Zig SIG
Date: 2026-06-03
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**Francesco Gualazzi** 00:07 Bye, too, sure.
**Giovanni Panice** 01:44 Hello.
**Francesco Gualazzi** 01:47 Hi, Germany, good day.
**Giovanni Panice** 01:49 Ayy.
I don't know if we want to keep talking in English, because this meeting.
**Francesco Gualazzi** 01:57 Yes, it's so cold, yes.
**Giovanni Panice** 01:59 Okay.
Okay, so… let's wait, to…
**Francesco Gualazzi** 02:04 A couple of minutes, yes.
**Giovanni Panice** 02:05 Yes, exactly.
**Francesco Gualazzi** 02:06 Let's see if someone has joined.
**Giovanni Panice** 02:08 Okay. Cool.
**Francesco Gualazzi** 02:13 Again, there's no item in the agenda, so I guess it just, So, you know, one thing that I would like to discuss, and I hope, Kemal or maybe Josh is joining, is, if we need some sign-off before merging the PR.
Assumed we fixed the CLA stuff.
I'm not sure we can automatically merge the content of that PR without, like, asking anything to anyone, but let's see if, if… maybe we pinged Josh in the channel, because he was… Going to support us in this regard.
**Giovanni Panice** 02:55 Yeah.
Yeah, yeah.
**Francesco Gualazzi** 03:09 By the way, are you able to add the new entry to the… to the document? Because I am from the phone, and…
**Giovanni Panice** 03:16 Yes, sure.
**Francesco Gualazzi** 03:17 That's pretty good. Thanks. Thank you.
**Giovanni Panice** 03:26 Okay… so… Let me share the screen… Okay.
Tough.
Today is, okay.
**Francesco Gualazzi** 04:05 June 3rd.
**Giovanni Panice** 04:06 Yeah.
So, we have… Okay… Why we put next meeting? Not better to, put meeting.
**Francesco Gualazzi** 04:18 Whatever, yes.
**Giovanni Panice** 04:20 Well, okay, no, I… I mean, it's only, maybe, it's only for me, the problem.
Okay, so… Oh, shit.
**Francesco Gualazzi** 04:33 So one item that I would add in the agenda is, once CLA is, Done, or fixed, or… Completed.
**Giovanni Panice** 04:46 is, once, all…
**Francesco Gualazzi** 04:48 It's completed in the…
**Giovanni Panice** 04:50 All the contributors have assigned the CLA.
**Francesco Gualazzi** 04:53 Exactly. Do… do we need sign-off from some more senior members, or are we completely autonomous in merging the code? We need to clarify this, and I will do… I will ping Josh while I not only inside.
**Giovanni Panice** 05:07 I think, I think that we only need to say, do we need additional, additional, activities before merging?
**Francesco Gualazzi** 05:16 Clear and specify sign-off, because sign-off is literally approving… someone that approves our action to merge the code into the repo.
What I don't know, because I'm not so familiar with the governments, is, if we need, If we are completely autonomous in managing the code, or do we need some guide rails? Because, again.
the repository parting order was mentioned in the proposal for bootstrapping the SIG.
But there's no clear understanding on my side, and maybe, you know, someone that is more experienced on the governance can tell, if we are completely autonomous in managing the code as SIG and SIG members, or we need some sort of sign-off From, from the organization.
**Giovanni Panice** 06:08 Okay, so once all the contributors have signed the CLA, do we need the sign-off from the, governance?
Or…
**Francesco Gualazzi** 06:15 The Mississippi from the TC sponsors and GC liaison, which are Joshua McDonald and Alulita.
**Giovanni Panice** 06:26 Okay.
**Francesco Gualazzi** 06:27 I will ping them directly in the Slack channel, so this action is on me, and I'm happy to do it, but, again, merely because I don't know, I don't have the experience.
**Giovanni Panice** 06:39 Okay, but maybe, maybe you can also write a comment, so, and you can ping them in the document, okay, about that. So, in a synchronous, or maybe.
**Francesco Gualazzi** 06:50 Which document?
**Giovanni Panice** 06:51 This one, this one, so a NASC meeting note, so you can, you know, select and, you know, tag, someone of them and say, about this point, we… maybe, I don't know.
**Francesco Gualazzi** 07:04 Let's do this! No, no, yeah, let's do this, and I mean, more notifications don't hurt, so let's do this.
I will ping them in Slack as well, and then we… and then we write everything down.
**Giovanni Panice** 07:16 Okay.
Okay, cool.
So let me… I don't know why.
Okay, so… Okay… Chairman?
Anything else? I don't know.
**Francesco Gualazzi** 07:58 No, because, again, before we can bring in other, say, packages, such as Proto.
and, SAMCOM, so… Basically, the goal is to have a structure in the OpenTelemetry Zeek repo that is very similar to the OpenTelemetry raster repo.
And not because the two technologies are inherently similar, but because.
**Giovanni Panice** 08:25 the way… Oh, yeah, the…
**Francesco Gualazzi** 08:27 the code structure is equal. And I already checked with the Zeek community. It is not currently possible with the Zeek build system to have to have a ZIG build that works in the way Zig workspaces or cargo workspaces work, so there is no notion of that.
in Zig yet, so we have to decide which approach we want to use. Maybe let's add also this to the, to the agenda for the next meeting, because I'm assuming before the next meeting, we will have sorted out the CLA.
and receive the sign-off. So for the next meeting, what I would do is discuss, so the entry that I would add is discuss building strategies for packages, because we have the SDK, proto, and semantic conventions, and.
**Giovanni Panice** 09:31 Hmm.
**Francesco Gualazzi** 09:31 All three of them and others, we can either build everything together.
Or, have dedicated, dedicated, looking at the paths in the repo, but unfortunately, the technical difficulty for the… each path gets its own Zeek build, is that there is no such concept of fetching a sub-part of a repo inside ZigBuild, so… Yeah, we need to overcome this difficulty. We have to… we have to come up with a workaround, and the workaround would be that we have to create a single build… build.zig file in the repo that contains each of the module's build processes, and then Selectively, you can build one or the other, or build all of them, but definitely when you import… when you import a dependency, you want to only import maybe one package, such as the SDK, or maybe two, SDK and same, and then most of… more often, you don't want to import the proto, so we have to come up with a strategy to allow ZIG users to consume the packages they want.
**Giovanni Panice** 10:55 Do you want to add also the solution and pros and cons?
**Francesco Gualazzi** 11:01 Wow.
**Giovanni Panice** 11:01 Entry, or we can discuss in the next meeting, so…
**Francesco Gualazzi** 11:05 Let's draft them, yes, let's draft the proposal.
**Giovanni Panice** 11:08 Okay, okay, let me… okay, okay, so solution one.
**Francesco Gualazzi** 11:12 Solution one is, one build.zig per folder, so per, per package.
Again, this might not be possible, but we have to test it. From my understanding, it is not, but we can test. So this is going to be every package, so OpenTelemeter SDK, OpenTelemetry Pro, Open Telemet SAMConf.
gets their own build.zig, and then somehow, zig.zig fetch, so the ZIG package manager, should be able to read.
Apologies.
**Giovanni Panice** 11:49 All directory. So the process is that, we have a much more granular availability of, packages.
**Francesco Gualazzi** 11:59 Bing ding?
**Giovanni Panice** 12:00 Yes. Do you think?
**Francesco Gualazzi** 12:01 And, and, and, and back.
**Giovanni Panice** 12:02 I didn't even.
**Francesco Gualazzi** 12:03 And they can also be released differently, because…
**Giovanni Panice** 12:05 Okay.
**Francesco Gualazzi** 12:06 Again, the version is… Per package, so per folder.
**Giovanni Panice** 12:11 Morgan… okay, so Morgan already, for, available… packages, and, deliverable.
Okay, cons, it's difficult, it's complicated, because you have to check,
**Francesco Gualazzi** 12:35 It might also not be possible with Zeek Fetch, so…
**Giovanni Panice** 12:38 my…
**Francesco Gualazzi** 12:38 But also doing that, we cannot do that.
**Giovanni Panice** 12:41 Consibbon?
to do that. Okay, cool. Solution 2?
**Francesco Gualazzi** 12:48 So what you do is, single bill does zero, file for the whole written.
**Giovanni Panice** 12:55 But for the wall… Rapo.
**Francesco Gualazzi** 13:00 With, with modules.
That corresponds to the… to the… to the project being… to the dependency being, needed.
**Giovanni Panice** 13:18 What do you mean, that corresponds to the project dependency…
**Francesco Gualazzi** 13:23 So, if we have a repo with OpenTelemetry SDK, OpenTelemetry Gencom, and OpenTelemetry, whatever.
That single folder of code is the dependency that someone wants to bring in its own project, right?
Okay. So, if there is an outer build.zig that contains… that builds every folder in that… in that repo.
**Giovanni Panice** 13:49 -
**Francesco Gualazzi** 13:50 that same build.zig must be able to specify individual modules. So a module in Zig is, like, literally a folder that contains code, and that can be imported in other projects via ZigFash and the build system.
Because Zeek Fetch works at the repo level right now, doesn't work on parts. What splits the parts is, modules, and… and yeah, so we have to come up with an idea on how to… also even build and release differently, if possible. I don't… I don't know how, but we have to come up with something in that regard.
**Giovanni Panice** 14:31 So, in this case, it'd be possible, I think, in this case, because normalized…
**Francesco Gualazzi** 14:37 So any…
**Giovanni Panice** 14:37 normal ZIG way to distribute the packages, so it's feasible.
It's feasible, okay? And cons, we have, one big, baggage.
Yeah.
**Francesco Gualazzi** 14:58 ZigBuild basically build everything, unless you use build options or build steps to selectively build specific models.
I mean, we can work it out.
some ways. Or, we can even contribute to the ZIG build system to allow fetching only parts of a repo. Because again, the ZIG fetch protocol is mainly based on Git over HTTPS. That's what most of… most people use, if not everyone uses, so…
**Giovanni Panice** 15:37 Is there a… did you check if there is some issue related to this.
**Francesco Gualazzi** 15:43 Oh, no.
**Giovanni Panice** 15:44 So, like, something, something, you know… Oof.
something, interesting as a feature. So, maybe I… maybe I can check, now. Do you know that the issue tracker is on CodeBerg, or…
**Francesco Gualazzi** 16:00 It is, yeah, yeah, yeah, it's no more on GitHub.
**Giovanni Panice** 16:03 Okay.
Okay, let me check a bit, like, one minute, as we are in you.
Okay, so G, the build system is in the D grab, or is in some.
**Francesco Gualazzi** 16:17 Yeah, yeah, yeah, you go to court.org slash Zieglang slash Zieg.
**Giovanni Panice** 16:22 Okay, so let's see if I'm lucky. So, issue, check, I searched for all the… the issue related to Zig Fetch, okay?
**Francesco Gualazzi** 16:34 Yep, yeah, yeah.
**Giovanni Panice** 16:35 Let's see.
Okay. Support frame file in ZigFetch. ZigFet doesn't replace fetch file for word. Does not replace missing figure, fetcho, and zigFetch memory festival.
Well, there are a lot of pages of each show.
**Francesco Gualazzi** 17:11 I don't think there is one in that regard.
**Giovanni Panice** 17:13 So, franchise search also for directory.
**Francesco Gualazzi** 17:18 Director or part, usually they use sub-path, yeah.
**Giovanni Panice** 17:22 Maybe part, yes?
**Francesco Gualazzi** 17:35 The gist of it is that since Git supports checking out ads only.
I think there might be a way to contribute the ZIG binary to fetch only specific paths.
It might be a very long shot, because again.
It would be only in the next step, minor release.
And we… we might… we need this before the next release. So, we have to discuss, and so we need to create.
**Giovanni Panice** 18:10 In any case, I think that maybe the right way is to ask directly to Ular is… I did.
**Francesco Gualazzi** 18:17 I need to… Yeah, I already did, and the outcome is that currently paths are not supported. That's why I'm raising the point to what we should do.
**Giovanni Panice** 18:27 Okay, but there is already an issue.
you know, that there is an issue is something discussed. I don't know if they have some… I mean, I don't know the governance for the… about new features and so on, so if they only have to write an issue, or they have a governance in which they, for example, propose something, like, you know, key IP, like Kafka, so… and design document about the feature, I don't know, so… So, I mean, this is, I mean, maybe what I would like to ask to Oris. So, if we know that there is already… to don't noise on the issue tracker without writing down.
**Francesco Gualazzi** 19:07 No, but I think creating the issue is not a problem. It will not cause any harm. The point is that there's gonna be very little interest in that, because it's gonna be very low priority.
**Giovanni Panice** 19:23 No, but,
**Francesco Gualazzi** 19:25 Not on the plate.
**Giovanni Panice** 19:25 No, no, but for… this is for sure, okay? No, what I want… I'm saying that to have the right approach to, to discuss with the ZIG, community. So, but at the end, probably we'll… we will, to this kind of feature, so… at the end. So, you know, so if they, so, start a discussion with them, design the feature, and then 100%, if they want to have the this feature in the ZIG we have to implement. So there is no… no other way, so…
**Francesco Gualazzi** 20:01 Okay.
**Giovanni Panice** 20:01 But there is a lot of space before, you know, put it inside, a project. So, for this reason I'm asking, so, because we have to understand what is the right approach to, discuss with them, so… and, and see if it's… something, that they want, in their, codebase. Then I'm pretty sure that, they prefer, contribution.
**Francesco Gualazzi** 20:33 I don't know. Let's, let's keep it up. For me, it's even… fine if we have one big B.zig, one gigantic B.zig.
It's…
**Giovanni Panice** 20:46 Yeah.
**Francesco Gualazzi** 20:47 A little bit less maintainable, but, and… but equally functionally… functionally equally, let's say.
**Giovanni Panice** 20:54 Yeah, so, sure, because, I mean, I don't think it's a super big data base, actually, so… but it's something that, I mean, can be, interesting in the future, so… For other projects, mostly.
not super big.
**Francesco Gualazzi** 21:08 That is all I had. I don't know if you have any entries to add, Joanne.
**Giovanni Panice** 21:11 No. Actually, no.
**Francesco Gualazzi** 21:18 No one else is joining, because Antoine has a clash today.
**Giovanni Panice** 21:22 Yeah.
**Francesco Gualazzi** 21:23 Kemal is also away, probably, and Jacob did, said he didn't… Okay, I couldn't.
**Giovanni Panice** 21:29 So, I think that we can close here, so… Thank you, Francisco. Bye.
**Francesco Gualazzi** 21:34 Thanks, John, enjoy your day. Cheers.
**Giovanni Panice** 21:36 Bye, bye-bye. See you.
