SIG: Zig SIG
Date: 2026-06-10
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Giovanni Panice** 00:31 Hello!
**Francesco Gualazzi** 00:33 Hi, Joe, having a good day.
You doing okay?
**Giovanni Panice** 00:38 Yeah, and you?
**Francesco Gualazzi** 00:40 Not too bad.
Stopped training just minutes ago.
So, yeah.
**Giovanni Panice** 00:53 Let's wait for the others.
Hey, Lam.
Painting.
**Francesco Gualazzi** 01:25 Hi, fun.
How you doing?
**Antoine Gagniere** 01:28 Great than you?
**Francesco Gualazzi** 01:29 Yeah, pretty good, yes, thank you. I mean, I was saying to Johnny that, We had very heavy rain yesterday night, and just a few minutes ago, it stopped, so the sun is… Finally getting out, and we are… And actually, I'm back from a holiday in Dimuliasu, which is south, not south, but… southern Premier, where it's much less rainy. Always not used to that. Anyways… It's very well needed a vacation after months.
Oh, no less, and now, you know.
just grinding till August, and then another couple of weeks. I don't know you, but… We really… with the baby, we really need some, some… Getting away and changing habits, otherwise she gets bored very easily.
Oh, okay.
Alright.
Yeah, I guess we can start. So, the attendees, I filled them in, and if you open the document, there are a couple of updates. One, Alulita created the project board, and I'd like us to fill in, maybe I will do that.
With the items that are still open in the old repo.
And, yeah, just, just, Fill it in with everything that we… we have open on the other side.
even before merging the PR.
Because at least we have a clear, clear… view of… The difficulties and the pain points.
And, you know, we know that the biggest problem is JRPC, but at least we make it evident on the board.
So yeah, I… I will port over the existing issues from Zigg Observability repo, and put everything in the backlog. Let me see… Yeah, backlog ready, in progress, in review done. Okay, the board is, is done this way, sort of a Kanban style, no?
And, yeah.
And then, I guess, a part of the meeting, if not maybe the first, like, 10 minutes of the meeting, or 15 or 30 minutes, can be actually going through the open issues and see if we can, if we can dispatch them, or… Take care of them during the meeting here, no?
Other than that, yeah. This is moving slowly, but moving, somewhere.
And then… Yeah, any comments on this?
Nice.
Okay, then… Next item… It's something that we briefly chatted, Joanne and I chatted about on the previous meeting.
And, the building strategy. So, assuming… we have the PR merged, and the repo is moved. By the way, I asked in Slack about the content of the repo, and Josh said… He's not available until next week, so… we can do two things. Either… We wait for you to advise on the best strategy to bring in the content in the repo.
Or we just go ahead and just merge the PR once we absorbed the CLA.
And we move it from there. But… The biggest pain point that we have right now is… that… The repo is meant to be… is meant to contain multiple modules. The SDK, the proto definitions with the ZIG-generated code, the SAMCOM library, and all of these three need to be independently consumable by by zinc projects. So… there is no really, a way. I investigated that, and there's no really, technically feasible way right now, with 016 at least.
To… have… multiple build.zig files in the same repo, and only have zig fetch.
Take one of them. Just take one of them.
Because it works on the whole repo.
So, what we would have to do, I guess, is solution 2.
Unless you know that… that it's… this… that we can actually… maybe you know something that I don't know, but… Yeah, that's… that's what we… That's what we're aiming for.
Which means another big PR.
Well, not a big, but… decently big PR to… To restructure the reports we need.
**Antoine Gagniere** 06:58 Okay, yeah.
Yeah, a workaround I can think of it would be to For each release, to create individual archives, but there would be more work, so I don't… I don't think it's a good workaround, but… Yeah, else… I mean, I'm guessing you can split the build.z, but import all of them in the root build.z?
But it doesn't…
**Francesco Gualazzi** 07:29 I don't think that's possible, because when you do zig fetch.
And you try to compile a dependency, even if you're importing it lazily, it expects to find… build a zig at the root.
of the repo.
**Antoine Gagniere** 07:47 Yes.
Yeah, yeah, I mean, I mean, yes, you can… like, just instead of a… I mean, yeah, like, it will be fetched… all the repo will be fetched anyway, unless we split… With the work around the mission?
But you… if you just want to split into multiple files, you can, right?
Like, if you want to put the logic of the cement decavation in a subfolder…
**Francesco Gualazzi** 08:23 Yeah?
**Antoine Gagniere** 08:23 You can do it and import it from the root build.zee, but it does not really solve the problem.
I agree, but it at least splits… the logic.
**Francesco Gualazzi** 08:37 Yeah, yeah, yeah, yeah, the…
**Antoine Gagniere** 08:39 I see.
**Francesco Gualazzi** 08:39 Yes, the thing is that we will have to, for example, let me make an example. Open Telemetry Proto as a test-build step, because it has its own build.zig file. And then, OpenTeameter SDK also has a test step.
**Antoine Gagniere** 09:01 Yes.
**Francesco Gualazzi** 09:02 These two steps, if we have a single build of Z, They… they cannot coexist.
**Antoine Gagniere** 09:10 Yes, it would need a different name, right?
**Francesco Gualazzi** 09:12 either a different name, or we go… which I… which seems the best, option with the build options.
like…
**Antoine Gagniere** 09:23 Yes.
**Francesco Gualazzi** 09:23 We say there is a build option that is called package or module.
And we switch on the enum.
That the option is made of.
And we apply, you know, logic that is currently all encoded in the build.zig, So the test step… for example, is when you pass "-d package SDK, or OpenTyman SDK, it indirects to the test step of.
**Antoine Gagniere** 09:57 Right, yeah.
**Francesco Gualazzi** 09:57 Okay, yeah.
**Antoine Gagniere** 09:58 I see, I see.
**Francesco Gualazzi** 09:59 it's, yeah, something… I mean, I guess it's something interesting to discuss, also with, some ZIG, team members, maybe core team members, because it's definitely something… the concept of a workspace, and if you want to do a monorepo with Zeek, currently you don't have much choices.
So, maybe it's something to… Johnny said, maybe we can ask… last time Johnny said, maybe we can ask the core team if they are planning to do that, but I'm… I know for sure that the dependency management is not, In the list of the parade objectives right now, 4 countries.
**Antoine Gagniere** 10:41 But… Yeah, yeah, like, it sounds like something that go… Like, it sounds like a go habit of…
**Francesco Gualazzi** 10:51 But also, as Cargo Workspaces does the same thing, but… we don't have to do a comparison across the other languages. Let's just say that for the way we want to structure the repo, which is how other repos are structured right now.
There is no native way of doing that with multiple BitOSIG files, unfortunately.
Yes. So yeah, let's, let's just, you know, let's just, one step at a time, come up with, with ideas, and, And see, if we can keep one built.zig file per directory and then selectively import them… I didn't find a way so far, but… Maybe there is a way that I… that I haven't found, so… Let's just say, first we put the code in, and then we reason about it. We can… because we have, decent testing.
We can, we can, you know, work locally, work with the CI, see what happens if we, you know… I tell it over and over, on, on… On the Bilt of Siege than that, I think, that is over, right?
So let's just say this. I haven't… I haven't heard back from Simone. What I would like to know is… wait a second, I have a phone call that I need to take, couple minutes.
Okay, so okay. I'm back.
Yeah. I don't remember what I was saying. Apologies.
Oh yeah, the CLA. I need… I need to understand… What do we have to do?
with the… with the commits that don't have a signed CLA. Of course I can remove the co-author and buy, but that feels… Unpleasant.
What do you think?
**Giovanni Panice** 13:44 Yes, for sure he's unpleasant. Let's wait another bit.
And, I don't know, so… In any case, if we want to proceed working on things, okay, we can create a branch upon your, Your, your pull request, okay?
So, if we won't keep working on… So, because it will be the next, main, okay?
So, in the meantime, we are, waiting for, Simone, where we can, proceed, okay?
So, then we will, you know, enqueue, pull requests that are based on that code, okay?
So… Actually, if we want to keep development, we can, you know.
OpenPR based on that, and and then, it's in review, so… To feel, less pain.
**Antoine Gagniere** 15:05 Okay, so I can start moving my PRs.
**Francesco Gualazzi** 15:09 No.
Because, I mean, if you stack them on the draft PR.
**Giovanni Panice** 15:16 Exactly. Yeah, we… I was saying that, yeah, I was saying to… yes, to stack new… do you hear me? So… no, no, I was saying to stack new PR in order to, I mean, to unblock the development, based on your PR, your draft PR, okay? Because I think that, for sure.
we don't… we want to… don't change anything. If we have to change the history, in any case, we can, cherry-pick, our changes.
And align it. So, I think that this is the kind of approach that we can, fake.
Okay. Do you agree?
Francesco.
**Francesco Gualazzi** 16:00 Yeah, yeah, sounds good.
**Giovanni Panice** 16:02 Okay.
**Francesco Gualazzi** 16:03 Okay.
**Giovanni Panice** 16:06 Okay. Okay, cool.
I don't know, so, only to recap a bit, Francesco, so, on your side, you will, also try to port, issue.
OpenAD issue into the project, okay? Okay, so, Ping us when you have finished it, okay?
So, okay. So, and, well, I think that, the next time that we will see us.
I don't know, Antoine, the next meeting, you are not available, right? Because you have an overlap. Okay, so we… okay, so if we want to do a bit of grooming and so on, we will wait the two weeks, okay? When Antoine is, available.
So, in this case, we can discuss a bit the new, the features that we want to, you know, to prioritize, okay? And, I mean, in the next one, maybe we can talk about minor stuff, okay? If, in this case, in order to have also Antoine on board, okay?
If you agree with, with me. So, I hope that for that time, so the next two meetings, new, next two weeks, you have reported the issue, okay? If you, if you need any help, don't worry, I can, we can speak, I don't know, the…
**Francesco Gualazzi** 17:40 There's just probably 7 or 8 of them. Okay. Five, I think, are very relevant.
**Giovanni Panice** 17:47 You know, but don't underestimate, because you have to create labels, things like that, I think. So… so with some… some…
**Francesco Gualazzi** 17:57 Good point on the labels, I'm not.
the permissions to do that, but I will double-check that.
**Giovanni Panice** 18:02 Yeah, I think, yeah, for this reason, don't underestimate these things, because they are really tricky, okay? I are tedious and tricky, so… Okay. From my side, it's all, I think, that, I don't know for Antoine, so…
**Antoine Gagniere** 18:23 Y-yeah, like… So you want to discuss, for example, the gRPC next time?
**Francesco Gualazzi** 18:34 We could… we could start even today, if you want to open the PR, start it on top of the draft, and and then we… and then we discuss over the PR, The comments, if you would like.
**Antoine Gagniere** 18:49 Right? Yeah.
**Francesco Gualazzi** 18:51 feminist, no?
**Antoine Gagniere** 18:54 Yeah, I can move the existing PR to the new repo and stack it on your PR, yes.
**Francesco Gualazzi** 19:00 Okay.
**Antoine Gagniere** 19:02 so, because, yeah, I don't know what your… what your thoughts were on the… the… this comp… build option to choose the gRPC implementation, to have the choice between multiple gRPC implementations, and not Pull in the dependencies when we don't need them, yeah.
**Francesco Gualazzi** 19:27 I think it's fine.
I think you nailed it, honestly. There is no other way, right now.
Unless we create a proper gRPC implementation, for, for Z, because there is none.
So, reusing the C library and giving the build options is exactly what we need, because.
**Giovanni Panice** 19:51 Yeah, I agree.
**Francesco Gualazzi** 19:51 That is not… that is not willing to… to do this type of, compilation, you know, bringing in the C library, they will just not put the option. And they will… they will have to know that they will have to use HTTP, so that the gRPC is not supported in that case, so OTLP is only HTTP and Proto.
So I think, you know, that we are the repo, and it's very sensible to just port it over and… And discuss the PR briefly.
**Antoine Gagniere** 20:25 Okay, great.
**Francesco Gualazzi** 20:28 And again, thanks a lot for the huge work you did there, it's, it's very, very appreciated.
**Antoine Gagniere** 20:34 Yep, thanks.
Because I did not spend that much time looking at the C… implementation of gRPC, then?
was clicked, like, the… that exists. I know you spend a bit more time than me.
**Francesco Gualazzi** 20:55 You mean the iguana one, the Solana guy?
**Antoine Gagniere** 20:59 Y-yes.
**Francesco Gualazzi** 21:01 Yeah, the thing is not working. I… I tested… I cross-tested it, and it's just not working. So I tried, in a branch, to run it with a proper, with an actual OpenTelemetry collector, container, and running the ingestion, and the protocol is not working, so it fails, it fails in multiple places. It doesn't even authenticate properly with TLS, so I guess it's just broken.
From the inside, so…
**Antoine Gagniere** 21:34 I do.
**Francesco Gualazzi** 21:35 I don't even know why the repo is in that state, honestly.
I had a… so, to do my test, I had it upgraded to 0.15.2.
But the code has a basic reimplementation of HTTP2 data frames.
And, yeah, it just… just doesn't work, so…
**Antoine Gagniere** 21:56 Okay.
**Francesco Gualazzi** 21:57 There is another option that, I'm afraid Hendrik is not here, but Hendrik did a HDB2 library.
I don't know if I shared before, I think I did, but yeah.
this HTTP2 library that is very early stage, and it is experimental, but apparently is more complete than the minimal thing that is inside the Zigwana gRPC.
So… Yeah, the real problem is that we don't have… we don't have the… the protocol that gRPC defines available to us in ZIG, other than importing the C bindings, which is… Totally fine for the stage we're in, I guess, so… beginning.
Open the PR, please, and we start with that.
And then we see what to do next. Maybe we got some time to create a repo.
in open telemetry, I don't know. In Zig observability, maybe, I have no idea. But we might have… Energy and time to create the proper.
**Giovanni Panice** 23:10 Yeah.
**Francesco Gualazzi** 23:11 Okay, NBC.
**Giovanni Panice** 23:12 Exactly.
What… I mean, I have a question, okay? Echo what a big question in the critical time. Sorry. Sorry. Puck. Sorry, sorry, sorry.
I really hate Alexa went and do these kind of things, so… Anyway, so I was… so, yes, I had a question. So, what if, for example… okay, so we don't have cycles to work on, gRPC, native ZIG library, okay? But what if we create, Zig API?
on top… of the C… Library.
I'm seeing this.
**Francesco Gualazzi** 24:07 That's what Antoine already did, huh.
**Giovanni Panice** 24:09 Okay, but you are, you have it in another, like, in another, repo, so… or you think about to take it, in another, okay, so, it's in your, okay, you're right, okay.
So, it can… so I don't… maybe, I mean, you have already addressed it, but the idea is, I mean, to… this is a starting point, no? Because from that API, we can iterate, okay, and, you know, defining, you know.
a native ZIG gRPC, so, I think that, I mean, maybe, if we, I mean, remove, you know, the serialization, we do the serialization, then we remove, step by step, I don't know, if it was already your idea, Antoine.
to proceed in this way, or, I don't know.
**Antoine Gagniere** 24:59 Like, yes, like, if one day we want to tackle to implement… it would… like, to be able to test the behavior difference, it's easier if we already can call the real implementation from ZIG, right, to make tests, behavioral tests, right?
So, yeah. But I'm not sure about, unrolling the layers, because it's really a mess, the… the C library is actually not… it's in C++, but they have a C API on top, it's a complete mess, so it's hard to unroll… to just… or pick a layer, but not the other layer, because it's in C++, so we cannot do that.
**Giovanni Panice** 25:46 We cannot do that. Okay.
**Antoine Gagniere** 25:49 Yeah, it sounds hard, because… because it's C++ inside, yeah.
**Giovanni Panice** 25:53 Okay.
**Francesco Gualazzi** 25:55 So, it's forces, dynamic printing, that's… for me, that's the biggest problem.
**Giovanni Panice** 26:02 Well, you know… I mean, I was, I mean, investigating other alternatives, so… I mean, because in some… In the future, in any case, we will remove it, no? So… and we will have it native, no?
okay, okay, fine. So, yeah.
**Antoine Gagniere** 26:20 not forced to be dynamic, I'm not sure what the…
**Giovanni Panice** 26:26 Francisco, or…
**Antoine Gagniere** 26:30 What did you mean?
**Francesco Gualazzi** 26:31 Dynamic linking.
**Antoine Gagniere** 26:34 you're not obliged… well, the… like, you can link it statically, the one I… my package, but it just… it's so big.
It's like… It takes super long, like, the linking phase… Because it's… it's, like, statically linking, like, 1GB library.
It wants to optimize link time optimization or whatever, so it takes super long.
So, by itself.
**Francesco Gualazzi** 26:59 to do that, because even… even with the… even with the time at my disposal, I was not able to achieve a fully statically linked.
**Antoine Gagniere** 27:13 Yeah, I can… my package can do that.
But it's optional, it's not by default, like, you have to… Add the option to…
**Francesco Gualazzi** 27:25 That's cute.
**Antoine Gagniere** 27:26 Thank you.
**Francesco Gualazzi** 27:27 Sorry I missed this detail, I thought, because, because C++… was, using, system libraries, like, I don't know, Netlink, Studio, or whatever.
**Giovanni Panice** 27:42 Andrea.
**Francesco Gualazzi** 27:42 it, it had to use, GLPC…
**Antoine Gagniere** 27:47 Yeah, human…
**Francesco Gualazzi** 27:49 human.
**Antoine Gagniere** 27:49 I had, like, I had to rebuild all the dependencies.
It's not, yeah, upsell and… like, the DNS library, or whatever, yeah. It rebuilds everything, so, yeah. You can build it statically, it's just that… It takes more time, it takes more space, it's… not a pleasant experience, but you can…
**Francesco Gualazzi** 28:14 I have to say, I have to tell you that there's been… it is work, that is currently in Zig Master Branch. Matlag worked on improving the link… And it's speed in the x86 backend, so… Right now it's much faster. So, when the next release comes, 017, it might have… For all platforms, the new linker that is based on the incremental compilation backend.
And that is improving dramatically, the linking time, so it goes, like, from… Maybe… what used to have… what used to be 30 seconds of linking, it goes, like, to 30 milliseconds. It's… it's, like, 100 times faster, so that's gonna land in the next release, but it's not so easy, because, yeah, you can imagine. So, it's a complete rewrite of a linker, so it's not… it's not immediate.
**Antoine Gagniere** 29:20 Yeah, this is. Also, maybe… like, because I had to make two packages, like, the… build… build of the LibJRPC, and then the wrapper. It's two different packages, and it's true that I did not add The linking choice… to the Raptor package, only to the… So maybe that's why you missed it, because I… yeah. So I should.
**Francesco Gualazzi** 29:47 Now it makes sense, because I remember I was looking… And what we import in your PR.
**Antoine Gagniere** 29:53 Yes, he's a rapper. He's a rapper. So, maybe, yeah, I should definitely add the option.
**Francesco Gualazzi** 29:58 If you can do that already in the PR, that would be awesome, because if you… like, modify your router with the ability to linking statically, and then we give the option to the user, that's gonna be amazing. Even if it's, you know, 1GB library.
**Antoine Gagniere** 30:18 Yeah.
Sure, yeah, okay, we'll do that, yeah.
**Francesco Gualazzi** 30:24 Sorry, we need to work now, one sec.
**Giovanni Panice** 30:29 Yeah, anyway, it's really, I think, challenging to create entirely a gRPC library.
**Antoine Gagniere** 30:39 Yeah. Yeah.
Well, like, yeah, just… I mean, I don't know all the details, but the little part I touch is so complicated, like, so much bloat, yeah, it's… A bit crazy.
**Giovanni Panice** 30:56 Yeah, I can imagine swimming.
Yeah.
**Antoine Gagniere** 31:15 But yeah, like, currently, it means we are forced to use the C allocator fan.
Yeah, like, the gRPC uses CR locators and C… Threads, like, yeah, it spawns threads in itself, on its own.
So it bypassed a lot of zinc logic, so it's not ideal.
**Giovanni Panice** 31:42 -
**Francesco Gualazzi** 32:24 Okay, I'm back. Apologies again.
**Giovanni Panice** 32:27 Don't worry.
**Francesco Gualazzi** 32:28 Not an easy day.
**Giovanni Panice** 32:30 No water.
I think that we are all set. I think that we are all set.
**Francesco Gualazzi** 32:35 Yeah, I will just add one more item, so gRPC API… It's going to be opened via cluan.
Stacked on top of… Sdk.
**Giovanni Panice** 32:53 Yes.
**Francesco Gualazzi** 32:54 Alright.
Okay.
All good.
**Giovanni Panice** 32:59 Okay 15.
Yeah.
I have to leave.
**Francesco Gualazzi** 33:07 Thank you, everybody. Bye.
**Giovanni Panice** 33:09 Bye.
**Antoine Gagniere** 33:09 Right?
To you?
