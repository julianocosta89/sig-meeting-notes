SIG: Zig SIG
Date: 2026-10-07
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Francesco Gualazzi (OpenTelemetry)** 02:08 Pan Tun.
**Antoine Gagniere** 02:09 Hey.
Yes.
**Francesco Gualazzi (OpenTelemetry)** 02:11 Good afternoon.
**Antoine Gagniere** 02:13 Good afternoon.
How are you doing?
**Francesco Gualazzi (OpenTelemetry)** 02:16 Yeah, not too bad. It's raining, but I'm okay. And you?
**Antoine Gagniere** 02:22 Same, same.
Kidneys… the… He's not sleeping well, so… not sleeping well.
**Francesco Gualazzi (OpenTelemetry)** 02:31 Mmm.
**Antoine Gagniere** 02:33 That's how it goes, I guess.
**Francesco Gualazzi (OpenTelemetry)** 02:35 How old is your baby?
**Antoine Gagniere** 02:36 Almost 2.
**Francesco Gualazzi (OpenTelemetry)** 02:40 Okay.
Yeah, it's, It's definitely a period where they can have some sleep disorder and also cause sleep disorders to the parents.
**Antoine Gagniere** 02:54 Okay.
**Francesco Gualazzi (OpenTelemetry)** 02:54 Yeah, there you go.
**Antoine Gagniere** 02:56 I think it's… Cool.
Like, nose… nose prevents him from breathing correctly, that kind of stuff.
**Francesco Gualazzi (OpenTelemetry)** 03:07 What did you say, Sabi?
**Antoine Gagniere** 03:08 The the you know, when you catch the cold, you you have the runny nose.
**Francesco Gualazzi (OpenTelemetry)** 03:15 Okay?
**Antoine Gagniere** 03:16 Yeah, so this kind of is issue.
**Francesco Gualazzi (OpenTelemetry)** 03:19 I get it, okay, I see.
Okay, so… yeah, welcome. I'm not sure we will be… Joined by other folks, unfortunately.
**Antoine Gagniere** 03:38 the.
**Francesco Gualazzi (OpenTelemetry)** 03:39 Giovanni is very busy also. He's become father recently.
**Antoine Gagniere** 03:45 Oh, yeah.
**Francesco Gualazzi (OpenTelemetry)** 03:46 ago. So he's, he's super sleep deprived.
**Antoine Gagniere** 03:51 Okay.
Finn Lake, yeah, I can guess.
Okay, okay.
**Francesco Gualazzi (OpenTelemetry)** 03:58 So yeah, basically the biggest topic right now is, upgrades to 0.17.
Because there has been a release of Zig 017.0.
Last week.
And, and because we made the decision of keeping multiple modules inside the same repo, so SamComp, SDK.
And, Paroto so far, we have now 2 problems, one Is that when we upgrade, The language… All the projects needs to be, all the modules needs to be upgraded.
At the same time.
Two, that the dependencies that we have In either of the module.
Need to also compile with CR17.
So if I look at our build Zigzon right now.
We have 3 dependencies, Zbench, which is made by Hendrik.
For the benchmarks?
Protobaf, which is from Lorraine.
And that's it, because the other one is the lazy dependency from the proto repo in OpenTelemetry, which is good that we only have a very limited number of dependencies, but still we have to wait for a release that supports 0.17, or we could use master.
Let me check. I'm checking Zig Protobuf, which I believe… has… A017, not yet.
**Antoine Gagniere** 05:40 Yeah, that was Zig master branch.
**Francesco Gualazzi (OpenTelemetry)** 05:43 Yeah, that would be Master, okay.
**Antoine Gagniere** 05:45 But, I mean, master, but they did not update.
super recently, right?
**Francesco Gualazzi (OpenTelemetry)** 05:51 So because we have Zig master.
**Antoine Gagniere** 05:54 Yeah, Ziggurustown.
**Francesco Gualazzi (OpenTelemetry)** 05:55 That was updated 2 weeks ago.
Z… the master branch, I think, is still on 016. Let me check.
**Antoine Gagniere** 06:07 Yeah, yeah, so I was thinking about the Zigmaster branch.
**Francesco Gualazzi (OpenTelemetry)** 06:10 Yeah, Zig Master is still… I think part of master branch is still on 16. So really we cannot do much until we have an upgrade of at least Protobuf.
So… That basically solves it.
**Antoine Gagniere** 06:30 Okay.
Oh, and I had, A point to bring, it was about, so… Currently, the SDK does not depend on the SEMCONF.
module.
**Francesco Gualazzi (OpenTelemetry)** 06:46 Okay.
**Antoine Gagniere** 06:47 And I was thinking about making it depend on Semconf, so that we can use the Semconf strings inside the SDK.
Is there a… Is it okay?
**Francesco Gualazzi (OpenTelemetry)** 07:02 How would you do that?
**Antoine Gagniere** 07:08 Okay.
**Francesco Gualazzi (OpenTelemetry)** 07:09 Dependency in the sense of meal dependency or dependency.
**Antoine Gagniere** 07:11 Right, right.
**Francesco Gualazzi (OpenTelemetry)** 07:13 sense.
**Antoine Gagniere** 07:14 You, like, just add the… import in the… module.
Right, so… So they would be linked in the graph, like in the dependency graph built by the build.zig.
**Francesco Gualazzi (OpenTelemetry)** 07:29 Okay.
**Antoine Gagniere** 07:30 Yeah, we could… add an import.
So the SDK can import some code, and then can use,
**Francesco Gualazzi (OpenTelemetry)** 07:39 You mean, ok, ok, ok, I wait, so.
SAMCONV BUILD, SDK BUILD… okay, let's check that one. The modules that are passed into SDK BUILD are build mods.
Which are built just for Protobuf and Benchmark, ok, so you're suggesting instead.
to also fetch from SDK build.
the module for SDK, and inject it into the SDK build.
**Antoine Gagniere** 08:13 The… yeah, take the same call module, and then use it as an import in the SDK.
**Francesco Gualazzi (OpenTelemetry)** 08:20 Let me share my screen real quick, so maybe we understand if I got the same, idea.
So you're saying… When we have this Sam convilled setup.
**Antoine Gagniere** 08:35 Right.
**Francesco Gualazzi (OpenTelemetry)** 08:35 Scorpion.
**Antoine Gagniere** 08:36 These are the three setups are independent.
**Francesco Gualazzi (OpenTelemetry)** 08:39 Exactly.
**Antoine Gagniere** 08:40 Built in parallel, right?
**Francesco Gualazzi (OpenTelemetry)** 08:43 Yes, I mean, they are built in parallel.
**Antoine Gagniere** 08:45 Right.
I would suggest to make the SDK depend on SELCOM, so it would no longer be… Power a little bit would be dependency, right?
**Francesco Gualazzi (OpenTelemetry)** 08:57 So, wait, but… so that means that this setup… Needs to somehow return.
The Semconf module, right?
Yes.
**Antoine Gagniere** 09:11 6.
**Francesco Gualazzi (OpenTelemetry)** 09:12 Post this one.
**Antoine Gagniere** 09:15 Okay.
I'm guessing this one, yeah…
**Francesco Gualazzi (OpenTelemetry)** 09:20 And then this module goes.
as part of the build modules here. Right?
In the same…
**Antoine Gagniere** 09:31 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 09:32 field.
**Antoine Gagniere** 09:36 Oh yeah, you could add it to the… okay, to… Like, it's like a dictionary of… Modules… okay, yeah, yeah, we could add it to the dictionary.
Yep.
**Francesco Gualazzi (OpenTelemetry)** 09:56 Okay.
But what advantage do we get? Is that we can then, inside the SDK, consume The module in our own, in our own code.
**Antoine Gagniere** 10:10 Yeah, yeah, to be able to consume, and so… let me get my notes. So, first of all is… When I add the attributes, you know, the resource attributes, I can use the same call.
**Francesco Gualazzi (OpenTelemetry)** 10:24 streams.
**Antoine Gagniere** 10:25 And what did they… Right.
2, Good.
Okay, now I do that. Notes… Oh, so they had no but anyway, yes, so so Yeah, the first use case. So, you know, yeah, I have this pull request about adding resource attributes.
**Francesco Gualazzi (OpenTelemetry)** 10:57 Yeah.
**Antoine Gagniere** 10:59 And yeah, so you would be the first user of simple strings, right?
**Francesco Gualazzi (OpenTelemetry)** 11:04 But look, we already do that. We have these dependency modules.
That is, added the SEMCONF module, so…
**Antoine Gagniere** 11:15 Oh, you you already.
**Francesco Gualazzi (OpenTelemetry)** 11:17 Yeah.
So this…
**Antoine Gagniere** 11:19 Oh.
**Francesco Gualazzi (OpenTelemetry)** 11:20 This is executed before.
**Antoine Gagniere** 11:23 Oh, so the order. So, okay, the order is actually very important.
**Francesco Gualazzi (OpenTelemetry)** 11:28 Look, it's in the comment ProtoMSM.com expose modules the SDK can import so they need to be built first.
**Antoine Gagniere** 11:35 Oh, yeah, yeah. I'm sorry, yeah.
**Francesco Gualazzi (OpenTelemetry)** 11:36 Now I remember!
**Antoine Gagniere** 11:39 I completely missed.
**Francesco Gualazzi (OpenTelemetry)** 11:40 Oh, it's okay! I mean, I didn't even remember as well, so it's fine.
**Antoine Gagniere** 11:44 Okay, yeah, yeah, it was…
**Francesco Gualazzi (OpenTelemetry)** 11:47 Yeah, that's why we, that's why we pass this pointer because then we allow and in fact, even though we have this.
And as you can see, we, initially we only put the protobuf.
And the benchmark, but then Proto adds this, Protobuf mode here. Then we have OpenTelemetry Proto that we can import as a named module. And in fact, we do that in the SDK.
I think in Otlp. So where is that? Here.
**Antoine Gagniere** 12:22 Hmm.
**Francesco Gualazzi (OpenTelemetry)** 12:22 At the very top… Yeah, there you go.
So yeah, you can do something like const temp semconven import open telemetry semconven, it will just work.
**Antoine Gagniere** 12:33 Okay, so no problem, so…
**Francesco Gualazzi (OpenTelemetry)** 12:36 So, done. It's already done.
**Antoine Gagniere** 12:39 Nice, nice, nice.
**Francesco Gualazzi (OpenTelemetry)** 12:41 Don't you love it?
**Antoine Gagniere** 12:42 Yeah, yeah, that's great, okay.
**Francesco Gualazzi (OpenTelemetry)** 12:44 I don't know what's happening, I cannot stop my screen share.
I think, Zoom is… Completely broken.
Do you? What?
What's happening?
Do you… do you see my screen still?
**Antoine Gagniere** 13:01 Yes, to see your screen,
**Francesco Gualazzi (OpenTelemetry)** 13:03 I cannot,
**Antoine Gagniere** 13:06 moving anymore, so…
**Francesco Gualazzi (OpenTelemetry)** 13:08 Okay. Let me just quickly kill, Kill this, and I will be back in a second.
**Francesco Gualazzi (OpenTelemetry)** 13:49 Hey, I'm back.
Now there is two of me. I think the other one is just a zombie process. Maybe I can remove it.
Let me check if I can remove my older self.
Someone joining?
Hell.
Never mind. Yeah, okay.
My previous me left the code. Okay, so you can just do that. In fact, I should do that, because it's a lovely idea.
And, yeah, looking forward to… to… to that. On the open PRs, I… Oh, I have two… that… Need an approval from someone.
And, yeah, I just want to… to understand if there was no… capacity on your end to review, or, you know, is there a… do I need to try to involve someone else? Because again, Giovanni is very busy, Kemal.
I don't see him joining the work anytime soon. Jacob is also… Not hopping on this repo very often, unfortunately. Whereas we have Henrik, apparently completely disappeared, I don't know what happened to him. And so these are the only maintainers that we have. We could try to find someone else, let's say.
Apparently it's, it's mostly you and me driving this project right now. Oy Giovanni.
The moment I was saying you, you are so busy not to join us, you appear like a demon.
**Giovani** 15:35 Sorry, sorry, sorry, Francesco. The problem was, like, that I was using the… the old link for the Zoom. So I think that there are, like, two times that I join, and then don't see anyone in the call, and I say, okay, they have already completed it, so… But this time, I said no, because I saw that you were writing on the agenda, so I said, okay, it's something…
**Francesco Gualazzi (OpenTelemetry)** 16:01 Last week, or two weeks, no, last week, we didn't do it because.
**Giovani** 16:07 Okay.
**Francesco Gualazzi (OpenTelemetry)** 16:07 I think we skipped. But the previous week, I was in the call until 5:20, 5:25, and I see nobody joined, and then I talk.
It's okay.
**Giovani** 16:17 Okay, and…
**Francesco Gualazzi (OpenTelemetry)** 16:18 Now that you're here, I want to know, are you sleep deprived?
**Giovani** 16:23 Sorry, are you sleep?
**Francesco Gualazzi (OpenTelemetry)** 16:25 Deprived because of the baby.
**Giovani** 16:27 Well, honestly, I have to say that it's like, I don't know, a wave, you know, some days we sleep, some other days we don't sleep, totally don't sleep, so.
**Francesco Gualazzi (OpenTelemetry)** 16:43 Antoine and I were just, you know.
remembering, but also Antoine is experiencing something similar with.
**Giovani** 16:51 Yes, we have some children.
**Antoine Gagniere** 16:54 Yeah, the worst is over for me, so I'm okay, but… Maybe, round two, I need to prepare for round two.
**Francesco Gualazzi (OpenTelemetry)** 17:04 Yes.
**Giovani** 17:07 will.
**Francesco Gualazzi (OpenTelemetry)** 17:08 Alright. So, yeah, I was just, saying, well, Antoine asked me a question about the… the import in the build, and we sorted it out. I was just asking if my two PRs can be merged, or if someone has had the time to review them.
I found very helpful the Copilot review. In fact, I am thinking about running it like Every time, at least the light one on all PRs, because it's gotten very smart. So it's able to find interesting things. And yeah, so I fixed in both PRs those.
So that would be 105 and 100. With regards to 88. So the W3C trace headers I messaged back.
In the… Slack channel, and he will resume that PR very soon. The stream of work there is that once we have the trace context propagation properly done, with all the WTC baggage and etc, then we can add the… A Zig service in the Open Telemetry demo.
Which is the de facto standard for the, for the displaying the capabilities of OpenTelemetry and back was the propose, the original proposer of this work, so I'm happy to have him, completed, both in the SDK side, where he created a couple of PRs already merged, and this one is the third one, and then in the hotel demo, where he opened the issue, and, and we started, Understanding what's needed to make it happen, so Other than that, my hunch is always with gRPC, and I know that there are these… there is this PR in draft that I… should look at, but Antoine, can you help me understand why it's still in draft and not ready for review? Is there anything that needs to be addressed, aside from the…
**Antoine Gagniere** 19:17 Yeah, I've saw the Copilot reviewer found a few… Thanks. Okay.
And they are relevant, so I want to fix them before… Putting it in Not Drop.
**Francesco Gualazzi (OpenTelemetry)** 19:32 But… and does this review came before or after your commits from two weeks ago?
**Antoine Gagniere** 19:43 Let me reopen the…
**Francesco Gualazzi (OpenTelemetry)** 19:44 You fixed a bunch of them.
**Antoine Gagniere** 19:45 requests That's.
**Francesco Gualazzi (OpenTelemetry)** 19:48 It's, number 83.
**Antoine Gagniere** 19:51 Yeah, but I don't think I have fixed everything. Oh.
Okay… I think.
Yeah, I did fix a bunch of the rooms in there, right? I'm not sleeping enough to remember what I did.
**Francesco Gualazzi (OpenTelemetry)** 20:05 It's okay. You see, you also are deeply proud.
It's okay.
**Antoine Gagniere** 20:17 Yeah, yeah, yeah.
And… Yeah, it's pretty easy.
issue about the… dot SO… path being relative like you know when you when a binary is Dynamically linking a .so.
How do you find the data? So… if… Like, either you have to modify the LD library path.
Like, the search parts of the… or contains the path of the .so, and is it relative, or… Absolutely, it depends, and so, yeah, I think… It's an issue about making it, but I think it's solved now.
**Francesco Gualazzi (OpenTelemetry)** 21:05 Okay.
**Antoine Gagniere** 21:06 But.
Yeah.
**Francesco Gualazzi (OpenTelemetry)** 21:09 You don't have to do it now, but if you find some time and you can mark it ready for review.
**Antoine Gagniere** 21:16 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 21:16 And we can land this one, that's a big milestone, so…
**Antoine Gagniere** 21:20 Right, right, right.
**Francesco Gualazzi (OpenTelemetry)** 21:21 I'm super, super ready for, for reviewing, as soon as you mark it, ready for review.
Yep.
And yet, and yes, I haven't still looked into what to do with the So the OTLP trace, included as X, there is a PR from Jacob in Zig Protobuff, but, So far, nothing, no news from Laurent, which is the maintainer of Zig Protobafon, letting me be also a maintainer of that project in order to speed up the reviews and the release.
It's unfortunate that probably he's focused on something else and the other maintainer is also busy with something else, so Apparently Zig Portobuff is a bit, It's a bit unmaintained at the moment and it's unfortunate because it's, again, it's the core dependency that we have to use.
For gRPC, but for protobuf, sorry, but yeah, let's try to.
To go ahead with that at least. So as I mentioned, I want to resume that PR fix was broken inside of that.
And just, when we have a proper fix in the protocol, in the wire protocol, then we remove our own code and we use the encoding from there. In the meantime, we just fix the bug which we have, that is, that the hex encoding is not applied right now in the JSON format That we use for exporting OTLP.
payloads.
So, yeah.
Not much let's say not much action in the couple of weeks before today, but I hope we gain well, there's been a couple of contributions from Daisuke on the metrics.
Which is good and, I want to get the gRPC out the door, fix the JSON encoding.
And then I think after that it's, it's, everything is easier because we can start planning a An alpha release adding the.
The language SDK in the official documentation and step by step.
improve the utilization. I don't know if you knew, but we have, we have, We are starting to getting some there is interest in using the SDK in already viable projects such as FX from Vercel, which is a coding agent.
And, someone from, someone from Tiger Beetle apparently also is interested in onboarding, Optionally, the tracing, so… Just, just know that this will be eventually.
Possible, but we have to, we have to do some, some.
Some increments, yeah?
Sorry, I have to sneeze.
**Giovani** 24:37 I don't know this library from Vercel, Effect.
**Francesco Gualazzi (OpenTelemetry)** 24:44 FX.
**Giovani** 24:45 affects.
**Francesco Gualazzi (OpenTelemetry)** 24:46 FX, Yeah.
Let me, there we go, this one, it's a coding agent entirely written in Zig.
And we've had a mention in their, in one of those… in one of their PRs.
There's a mention to our repo saying, add tracing, open telemetry tracing.
Okay. And… Yeah, number 856.
What is that? Here.
So in this PR, this guy, or this, this, this.
Hold.
Arnav 12114.
**Giovani** 25:35 Okay, no worries.
**Francesco Gualazzi (OpenTelemetry)** 25:36 is consuming our repo.
in build.zig and Onboarding traces, so using the trace provider and all of that.
In the… in the… in the FX, cool.
**Giovani** 25:53 The pinna, the comet.
**Francesco Gualazzi (OpenTelemetry)** 25:57 Yeah, yeah, because we don't have, in this new repo from OpenTelemetry, we don't have any releases.
And the reason why we haven't done is simply because, again, we don't have gRPC support, which is the default. And we also have some bugs, such as the one about hex encoding. So I want to get those out of the door and then we start making 0.1.
And that should give us some more traction, you know, because we do a big announcement and then we put it on the OpenTelemetry page. It's an officially supported language, blah, blah, blah.
Okay. So… yeah.
And yes, guys, I want to thank you for the help in achieving everything so far and what we are going to achieve in the future because without you, this would not have been possible, so I'm very happy that we did this together.
Thanks.
**Giovani** 26:58 I have to say that Antoine gave a super boost, I have to say, because in the last period I was really, really busy. So thanks to Antoine, honestly, we can say it.
**Francesco Gualazzi (OpenTelemetry)** 27:09 Thank you, Antoine. I was mentioning also, I was mentioning also that Hendrik apparently disappeared completely, I don't know what happened.
**Giovani** 27:15 Yeah, you know, it's life in the open source space. If they, I mean, if, for example, IBM can… Pay me the cycle for the OpenTelemetry SDK.
For Zig, it would be, I mean, super awesome. I asked because, I mean, there is an OpenTelemetry team in my company.
And they contribute to the Go, because they do observability for mainframe. There is an initiative in IBM, but for Zig, there is no support for Zeta OS. Yes.
**Francesco Gualazzi (OpenTelemetry)** 27:55 Yes.
**Giovani** 27:56 Yes, the mainframe, because I mean, it will be much better with Zig. I started a discussion with the, yes, I started a discussion with the OpenTelemetry team in IBM, as I said, because they… Use the Go. The Go… I think, I guess, they use the Go SDK, the Go instrument, but I asked for the… For Zigua.
Because there is some interest, really, I'm not joking, so.
**Antoine Gagniere** 28:30 Interesting. Yeah, I have a team next to me that also are working on those.
mainframes, so AIX, ZOS, and…
**Giovani** 28:39 Yeah.
**Antoine Gagniere** 28:40 Another one.
And they have problems with Google.
But Zig dropped support from AX, right? Yeah.
**Giovani** 28:54 Because, I mean… It's reasonable, because, I mean, IBM should provide the machine, so, to test the toolchain and so on, so… yeah, yeah.
**Antoine Gagniere** 29:04 Yeah, it's a big problem. And it's because, like, the system headers, like, Zig is cross-compile, and so it needs system headers, so, yeah.
**Giovani** 29:14 Exactly. So some developers from IBM are interested, okay, to compile for Zeta iOS. But I mean, you know, IBM is so big, it's really difficult to do anything.
**Antoine Gagniere** 29:29 So.
**Giovani** 29:30 you. So, so.
**Antoine Gagniere** 29:32 Using the movie's estimators.
**Francesco Gualazzi (OpenTelemetry)** 29:34 There is an enterprise SDK developed by IBM for Go.
**Antoine Gagniere** 29:39 Yes.
**Francesco Gualazzi (OpenTelemetry)** 29:40 There's a Go version developed by IBM to target the ZOS.
**Giovani** 29:45 So I mean let let me explain. So I was in an I was in a meeting related to open source and so on and I said okay no yes I contribute to the Bidium obviously the Bidium is I mean I'm paid for the Bidium and I said I'm also contributor for the open SDK for Zig and someone from oh yeah we do open open observability for mainframe so we should the beta Why? Why is so cool?
**Francesco Gualazzi (OpenTelemetry)** 30:15 Yes.
Go ahead.
**Giovani** 30:16 Guys, one step at a time.
**Francesco Gualazzi (OpenTelemetry)** 30:19 Yeah.
**Giovani** 30:20 One step at a time, so…
**Francesco Gualazzi (OpenTelemetry)** 30:21 In fact, you know, I was missing you in this meeting, Giovanni. I didn't want to write to you because I didn't.
**Giovani** 30:30 You know, Francesco, I mean, I have my, I mean, as I said, IBM don't want to, for now, pay me cycles for the Zig development. And I mean, you know, I have a baby now, so it's a bit difficult for me to, you know, to have this kind of side project.
But don't worry, behind the scenes, I'm always working on,
**Francesco Gualazzi (OpenTelemetry)** 30:53 Then you can spare some time to review one of the two PRs.
**Giovani** 30:57 Yeah, or I can spend some token from IBM to do the review from the agent.
**Francesco Gualazzi (OpenTelemetry)** 31:05 The.
The code there is, his, Is manual, is handcrafted, there is no AI.
**Giovani** 31:16 Really?
**Francesco Gualazzi (OpenTelemetry)** 31:17 Yeah, yeah, Zig is the only one where I'm not using, anymore, any, any coding.
**Giovani** 31:22 I like it, I like it, I like it.
**Francesco Gualazzi (OpenTelemetry)** 31:24 Yeah, because at least in my spare time, you know.
At least when I want to do real programming and, and develop my craft, I, I don't, I shut it down, shut it off, yeah.
Anyways, yeah, I think I don't want to hold you for longer unless you have more topics to throw at me or questions or anything else.
**Antoine Gagniere** 31:50 So I hadn't read your PRs, actually. I just don't remember why I did not press approve, but
**Francesco Gualazzi (OpenTelemetry)** 31:57 Okay. Which one did you review?
**Antoine Gagniere** 31:59 the two of them, so I…
**Francesco Gualazzi (OpenTelemetry)** 32:01 Both!
**Antoine Gagniere** 32:02 I mean, I remember reading the code, but I don't remember why I did not push approve, so I will…
**Francesco Gualazzi (OpenTelemetry)** 32:08 I mean, if you… if you happen to push now any of… either of one, either of the two, then Giovanni can do the other, or, you know, do both. Those are two pretty serious bugs that, that we had to… that we had to fix, and.
I think, I mean, thanks to the, to the, the man reporting them in Jay, in Jay Takura, Jay Taka, wait, wait, wait.
J, so this.
**Antoine Gagniere** 32:38 do.
**Francesco Gualazzi (OpenTelemetry)** 32:38 A couple of folks from Japan.
Junji, Takakura, and Daisuke, they seem to be consuming the project a lot, and they gave us interesting feedback with interesting fixes that we applied, so yeah.
**Giovani** 32:55 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 32:58 Actually, you know what? Let me ping him. Dre Daka.
If one of five… I'm pinging in… That's the issue.
Thanks. I'm pinging Junji.
In the, in the issue that he opened, so maybe he can also review and give us more feedback.
Also, you know, the Rails API is now much better, much more ergonomic. I really like it, that we don't have to, you know, go and pass the tracer in the span end. Now we just call span end, and we pass either null or another A parent span, or child span, and it's just very cool.
**Antoine Gagniere** 33:49 Yeah, I think that something that he said last time was that it was possible to end the trace Server before the trace, and so then you… if you end the trace, it points to a non-ex… but is that actually a real…
**Francesco Gualazzi (OpenTelemetry)** 34:06 No, but I fixed that. It was right, and I fixed it, yes.
**Antoine Gagniere** 34:09 It was real.
**Francesco Gualazzi (OpenTelemetry)** 34:10 Yeah, the only problem is that you have to call shutdown and the init in the same order, so it's a bit tricky, because if you use the defer, you have to do… The fair, the fair, you need the fair shadow. But I fixed most of it. Let's say it's better than before. Before it was crap and now it's, let's say, half crap.
**Antoine Gagniere** 34:36 Okay.
**Francesco Gualazzi (OpenTelemetry)** 34:36 It's not optimal yet, but it's much better. Me as reading through the examples, I saw that it's much simpler to use now.
Even if I were able to use the one, the version before, because I wrote it, now it's much better.
**Antoine Gagniere** 34:57 Cool.
**Francesco Gualazzi (OpenTelemetry)** 34:58 Okay, so… you're going to use the SEMCONV module in the, attributes, put in, review the gRPC one, I will review it immediately, I will work on the X encoding, mostly, and, yeah, we touch base, next week, or in two weeks, and, I hope you can get some sleep by then, you both.
you yeah.
Awesome!
**Giovani** 35:31 Thank you, thank you guys, thank you Francesco for leading the initiative, thank you Antoine.
Bye.
**Antoine Gagniere** 35:38 Thank you.
Enjoy!
**Francesco Gualazzi (OpenTelemetry)** 35:40 Hi.
