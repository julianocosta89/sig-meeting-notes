SIG: Swift SIG
Date: 2026-07-16
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**nacho** 00:16 Bye.
**Bryce** 00:18 You're not sure.
**nacho** 00:19 Hey, Bryce, how are you?
**Bryce** 00:21 Doing good.
I'm finally, I'm finally feeling better after the plague I got from flying back from Spain.
**nacho** 00:31 Oh, really?
**Bryce** 00:32 Yeah, I was sick for, like, yeah, 3 weeks, basically.
**nacho** 00:37 Well, and, and, and what was it, I mean.
**Bryce** 00:39 I don't know.
**nacho** 00:40 Something personal, I don't.
**Bryce** 00:42 It must have been… it must have been some kind of COVID, because I've never… it'.
**nacho** 00:45 It was.
**Bryce** 00:46 Chest thing. Yeah, it was a chest thing. Nothing gross.
**nacho** 00:50 Yeah, I mean, you said that you were.
In that meeting, after we… we met, that you were in with a bad idea, and I respect you.
For so long, yeah.
**Bryce** 00:59 It was, the. The guy who was sitting next to me on the flight back to the US was, like, just coughing up a lung.
And it was so bad. At one point he was like eating a sandwich. I don't know if I told you this, but he was eating a sandwich and started coughing and like flung crumbs everywhere, like all over me. And I was like, it was so gross. Oh man, it was bad.
Yeah, I'm I thought it was something way worse, you know? So, I was really glad it was just… sandwich crumbs that I was pelted with.
**nacho** 01:34 Yeah, yeah.
**Bryce** 01:35 Yeah, I'm.
**nacho** 01:36 Yep.
I thought it had been something in Spain, and at least it was. I mean, I feel better not being something in Spain.
**Bryce** 01:43 Yeah, it wasn't. Yeah, it was, the guy. Yeah, it was whoever was sitting next to me. He was really sick. And. Yeah.
I'm just finally feeling cleared up.
Let me share my screen.
**nacho** 02:15 It was expecting Ari to come today.
And took a…
**Bryce** 02:18 Oh, yeah.
**nacho** 02:19 I mean, about soccer?
**Bryce** 02:21 Oh.
Was it Spain versus Argentina yesterday?
**nacho** 02:26 Okay.
**Bryce** 02:27 Did they… did Spain win?
**nacho** 02:29 The final is next Sunday, but it's Spain-Argentina, yes.
**Bryce** 02:34 Oh, that's the final next Sund.
**nacho** 02:35 Yeah, it was Argentina, England yesterday.
**Bryce** 02:38 Oh.
**nacho** 02:38 Argentina won, so it's playing with.
**Bryce** 02:40 Granted.
**nacho** 02:41 being the final.
Otherwise, they…
**Bryce** 02:50 I don't know if you can hear my children fighting in the background or not.
**Vinod Vydier** 02:55 Go Spain!
**Bryce** 02:58 I don't know, I gotta root for Argentina, because, you know, it's like South America, America, you know?
**Vinod Vydier** 03:05 No, no.
**Bryce** 03:07 Look at it.
**Vinod Vydier** 03:08 Yeah, no, I think the the main thing is Argentina got a lot of help, I feel.
From where?
Video assisted reference.
Didn't know that.
So I think that is, yeah, that's why I… I'm supporting Spain.
**nacho** 03:29 Okay, yeah.
**Bryce** 03:29 Very good. I respect that.
**Vinod Vydier** 03:34 Otherwise, I have no, I didn't bet any money on anyone, so…
**nacho** 03:41 Yeah, I don't bet any money.
In anything, right? I don't bet.
**Bryce** 03:46 I saw it. What was it like? There's like $1.5 billion bet on World Cup stuff now. Yeah. Crazy.
**Vinod Vydier** 03:56 Yeah, that is crazy, yeah.
**Bryce** 04:06 I was trying to find it, I thought that we had… Oh, here we are. Okay. Deprecation plan.
I wanted to bring this forward.
The PR is still… Oh, whoops I'm just struggling with this thing. I don't know why it's mad. I' So that's our blog post for the deprecation of cocopods.
**Vinod Vydier** 04:47 Nice.
**Bryce** 04:48 Still trying to get that… get that released, published.
Oh.
See.
I have not had a chance. My wife has been doing a lot of… work projects on her own today, so I've been watching kids the last couple weeks.
So I haven't had a chance to really work on anything.
**Vinod Vydier** 05:18 I'm in a similar situation. My Wife is out of town, so I'm a single dad for the last One more week.
**Bryce** 05:32 Yeah, so, Robert, Magnusson came last week, and it was just him and I, and Vinod… oh, Vinod was there too, but you didn't really… Didn't really say anything.
But… I guess I won't bring that forward, but just a little update. So he… Was looking for good first issues to do, and, I pointed him To a couple of things, I think what caught his eye the most was maybe reviewing spec. Like, we, like, one of the issues we've been having is, reviewing the traces spec.
And verifying whether or not our implementation still matches with.
What, what's in the spec?
So, I think that he might be working on that, but I don't know. So, but that's… That's kind of where it's at.
**nacho** 06:32 Yeah, I think, yeah, that's a good issue, especially if he wants to In the project, I'm, yeah, I'm doing things, And I'm using the library for his project, yeah, that…
**Bryce** 06:45 Oh, nice.
Okay, yeah, so we've finally got all of our CodeQL issues resolved.
Everything's building again.
I brought forward or I brought Ari's simulator resolver from the core into the main repo. So now that shouldn't be a problem ever again. Fingers crossed.
Any topics? Any other topics?
Anybody wants to discuss?
**nacho** 07:23 Yeah, we were, I couldn't come last week because I, yeah, I forgot. I was in a trip and I couldn't come back.
Yeah, we were talking two weeks ago about reworking the core.
And main library, I think.
Oh yeah.
**Bryce** 07:41 Great.
**nacho** 07:42 I don't know if you continued with that last week or not, no.
**Bryce** 07:46 No, yeah, like I said, it was just the… just Robert, was here last week, and so we mostly just discussed, Oh, yeah, maybe we can talk about this from last week as well. Yeah, we just talked about, kind of, what he can do to help.
**nacho** 08:04 Okay.
**Bryce** 08:04 But one thing that I did bring up was discussing this open telemetry or this the URL session instrumentation.
I don't know if you've been keeping up on… I guess there hasn't been any conversation here.
But I talked about it a little bit, in case anybody was watching the recording last week. But, so I reviewed this, and… what I… what I realized was, is, Simon is… what's happening is Simon is confused as to why, we aren't auto-instrumenting Delegates, just to automatically have everything instrumented.
And so that's why we were confused in this example.
So, the… what he was doing is, is he was checking to see if we actually can find any delegates that are implementing this method, and if not, we automatically Implement it.
And then call the allow. And that's why — I don't know why this is — he shouldn't be calling this since there's nothing to call, essentially. But he's basically just overriding this method automatically, whether or not it's implemented in the delegate.
And so, I raised the flag on that, saying, like.
You know, like, if this is implemented and, you know, customers are using the built-in callbacks on the, the task, methods, then those will stop working once the delegate implements this method. And so that's why we are not automatically implementing everything.
**nacho** 09:50 Yeah, the thing is that For some methods, if the system finds a delegate.
It's gonna call the delegate instead of the default method.
**Bryce** 10:00 Yep.
**nacho** 10:01 So yeah, we are changing behavior, and we can be…
**Bryce** 10:04 Yeah, and so.
**nacho** 10:05 Definitely changing, the… Seeing the behavior of the app, yeah.
**Bryce** 10:11 Yeah. Yeah. And so that's basically what I said here. And so I don't know — he hasn't responded back at all. But I think that we can leave it open for another week or two. And if there's no response, then we'll close it.
Okay.
**nacho** 10:26 Okay.
Yeah, I mean, this is a very, very, very fragile Thing, because Apple just doesn't… even doesn't follow its own… rules or documentation. So…
**Bryce** 10:41 You are…
**nacho** 10:42 We're playing with experience and with… Yeah, I… And I'm fixing bugs while they appear. That's the real truth.
**Bryce** 10:53 Thank you.
**nacho** 10:54 Yep.
Yeah, per… He… Yeah, I… Sometimes you have to put a delegate just because if not, things don't get called, but if you implement a delegate method.
By default, that also, as you said, sometimes just will… if the system finds a delegate, it will call just the delegate, and not the other methods.
**Bryce** 11:20 Yeah, yeah, yeah.
**nacho** 11:21 Yeah, that, that, that, that's dangerous.
**Bryce** 11:27 Yep.
All right. Well, there's that. So that resolves that open question that we were confused about. I just went through this morning and cleaned up all of the renovate tasks.
Okay, yeah.
Sure.
**nacho** 12:05 Yeah, that…
**Bryce** 12:06 I think this just needs a rebase.
Or maybe… Oh, that's why. It just needs, yeah.
I just.
Same amount.
So that should be merged after that is fixed.
Over in Swift Core.
It's a draft, hasn't been updated.
I think that these.
Might not want to merge this one if it's.
Having some problems.
Oh, interesting.
I wonder why that's… That's happening.
The… Simulator resolution script was supposed to solve this problem.
Why is that happening?
I'll take a closer look at that after this meeting.
No issues in core… oops.
And… I think that there aren't any new issues in, Oh, there is this one, which… Oh, but we've looked at this before.
That would be a neat thing for somebody to, like, a nice first issue kind of thing, I think.
Just to, like, test out… The new metric kit stuff, see if it still works.
**nacho** 14:40 Okay.
**Vinod Vydier** 14:52 Also, there's some new metric kit from Apple.
**Bryce** 14:58 Is that somebody from Apple?
**nacho** 15:00 I hope not, OG. I hope not.
No, it'.
**Bryce** 15:07 Chinese knockoff of Mac with a K.
Yeah, I don't think there's really.
**nacho** 15:19 Okay.
**Bryce** 15:22 Let's see. We got a couple let's yeah. Maybe we could review just what we have assigned. Have you had a chance to look at this, Vinod? You've you've been assigned to it.
TLP profiling.
**Vinod Vydier** 15:35 Oh, yeah, yeah, I think I I did respond on the.
**Bryce** 15:40 Huh? Oh, there's no EBM. Okay. Yeah.
**Vinod Vydier** 15:43 I see. Yep, yep.
Yeah, this this is so Microsoft is working on the Ebpf on their platform.
similar to what what's on Linux. But It's it's it's a very deep subject. It's not a.
**Bryce** 16:02 Yeah. I'm not very familiar with with, like, yeah, runtime profiling at all.
**Vinod Vydier** 16:08 Yeah, I'm very familiar with it on the… OpenTelemetry collector side.
**Bryce** 16:15 Oh, cool.
**Vinod Vydier** 16:17 And and that is actually elastic headed donation.
Grafana had a donation.
Splunk her donation. So like 3 donations to Oh, that sounds cool. Yeah, yeah. It's a.
But it's all, right now, Linux-based, right? It's not… If you're on other platforms, specifically Windows, right, because that's where all the server-side stuff is.
**Bryce** 16:45 Yeah, yeah.
**Vinod Vydier** 16:45 Yeah, it's all great. If you have containers running on.
which are all Linux. Yeah.
**Bryce** 16:54 That could be an interesting project to get that working for Swift on, you know, server Swift.
**Vinod Vydier** 17:02 Yeah, it'll definitely be… Great if you can inject something with the Ebpf.
**Bryce** 17:25 You got assigned to this one, not sure, a while ago. I don't remember what the…
**nacho** 17:31 Yeah, I think that… Yeah, I think that that Pr is.
**Bryce** 17:38 Is still open. This is the one that we're waiting to get merged. Yeah, okay.
Yep, yep, And then we have Ari, Ari, Ari Yeah, Swift packages.
**Vinod Vydier** 17:58 Are are you still recovering from?
Welcome to 3.
drinking parties.
**Bryce** 18:05 Yeah, I still haven't had a chance to look at that.
Yeah. Hopefully, like, in the next week or two, I'll have I'll be in a more set schedule and and actually spend more time just on OpenTelemetry so that I have something to do. Yeah. Yeah.
**nacho** 18:26 It's interesting for me, I was, you know, I'm starting my video next week.
So we'll have a table with help.
Didn't work. I'm… I hope to find some time to do something in the project. I was really thinking about the What we talked last.
Two weeks ago, about… Moving again the code from the core.
To the main repo.
if the… but I'm not sure… I'm not sure we got to a final decision about that.
About… Just keeping the copy when we release.
Into the… public, making core just a copy of the source code in in the non-core library.
I'm gonna use that.
**Bryce** 19:15 Yeah, I kind of, well, Yeah, that could be… Okay, either or, maybe, yeah,
**nacho** 19:23 The problem is really that we have… currently open PRs against that code, right? Yeah.
**Bryce** 19:31 No.
**nacho** 19:33 But yeah, moving again and, and just leaving the library, just copying the folders, the core and, and the, sorry, the API and SDK folders.
There, when we create that release.
I think it fixes so many things.
It simplifies our flow so much, like you said, with updating, you know, all these update libraries that we are duplicating every time.
And we have problems that we've had to release Encore, and we have to create that release so it can be taken with the other, and… it's slowing us a lot, and also everyone working on PRs.
**Bryce** 20:19 Yep. It's a huge pain in the butt for sure.
Yeah, I think… I think that… I mean, it was Ari's proposal, and I mean, I'm on board with doing it, for sure.
Yeah, I think…
**Vinod Vydier** 20:36 2 repos. I have not been able to keep up.
**Bryce** 20:40 No, I.
**Vinod Vydier** 20:41 Yeah, it's not a… Yeah, that's easier before.
**Bryce** 20:45 Either… yeah, I'm okay with either of them. The proposals being, what, copying the core into… Well, honestly, well…
**Vinod Vydier** 20:59 We talked about the submodule or something, right?
**Bryce** 21:02 Yeah, we'll… we'll just producing… producing artifacts of core that people can use, XC frameworks. I think that… Copying, like, copying it over is a little bit more complicated than just copying it over, because we'll also have to produce, like, a package Swift.
a Swift package file.
for it. I mean, and we could we could just generate it whenever part of the job or something as we as we copy it over, but it's just, like, a little little fiddly things like that that might make it a little bit more complicated.
**nacho** 21:37 Yeah, it… I thought that just for avoid breaking.
I… Breaking existing float, or people just… Using that, but yeah, the…
**Vinod Vydier** 21:50 So, so, what we're, proposing, or Ari was proposing, is create a Xc framework out of the Core, and then use it in the Swift.
**nacho** 22:01 Yep.
**Vinod Vydier** 22:02 Okay, so that way…
**Bryce** 22:04 Well, I think what he's proposing is that we, That we merge core back into the main repo.
And then for supporting vendors, either copying the SDK and API into its own repo whenever there's a release and locking that repo down so there's not PRs or anything to it.
or just generating XC frameworks that the vendors can use.
Rather than having…
**nacho** 22:39 Yep.
**Bryce** 22:39 A whole separate root poem, yeah.
Well, in…
**nacho** 22:45 For me.
**Bryce** 22:45 I guess those, those, those, those… Artifacts would be in their own repo, but… I guess they don't necessarily need it, but…
**nacho** 22:52 The thing is that if you create XC framework as artifact, you have to create lots of them.
I mean, you need one for each platform?
**Bryce** 23:01 Yum.
**nacho** 23:01 And one for each simulator, both.
I mean, we can avoid the Intel simulator one, but…
**Bryce** 23:10 Yeah, I.
**nacho** 23:11 Until recently, you needed both the simulator for Intel and for…
**Bryce** 23:16 Yeah, they're, they're.
**nacho** 23:18 Okay, yeah.
**Bryce** 23:18 to generate. Yeah, so maybe just copying into it.
**nacho** 23:24 And also.
**Bryce** 23:25 So.
**nacho** 23:25 Talking a bit about texting framework.
I think we had a library that I don't know if it's still like that, but I think Swift Concurrency, which was… being picked up by some project of us. Didn't allow the… Framework, the enable framework.
Something that you have to put for XC Frameworks, the… Okay.
There is a flag that you have to put, maybe that was only the… Concurrency context?
There is a library that we were leaking. Probably it has been updated. That did me.
Didn't work with the… You needed to build the library.
**Bryce** 24:17 It's only for.
**nacho** 24:18 Could be that one. It could be that. It could be Swift Atomics that didn't allow.
Building an XC framework, because it… Didn't work if you added the… I don't know what's the The… I mean, I don't remember what was exactly the… The flag you have to use.
**Bryce** 24:41 Mmhm.
**nacho** 24:42 for… for building an XE framework, because you have to… Yeah, you have to put builder libraries for distribution as a That's one of the… Skip install, and build libraries for distribution, you have to build with that.
And in XC framework, and I don't know if that is allowed in… I know it was… it wasn't in the past, but I don't know now.
**Bryce** 25:24 Yeah, I think… I think that, I think that just maintaining — it sounds to me like maintaining — just copying the code over to a read-only repo for Swift Core would probably be the least complicated solution.
generating the XC frameworks is a… is a pain in the butt.
For sure.
**Vinod Vydier** 25:55 Yep.
**Bryce** 25:57 But, yeah, maybe,
**nacho** 26:00 That killed my video, sorry.
**Bryce** 26:02 Oh, that's okay.
Yeah, I think that this is — I think this is the best solution. And if we want to pursue generating XC frameworks, I don't see any reason why — I feel like we're going to need to have the separate Swift package to make that work anyway.
**nacho** 26:25 Yep.
Yeah, also… If you generate Excel framework, you… you need also… To put the exact hash.
In the package, and you can only create that after you have the build theme.
**Bryce** 26:41 Yeah.
**nacho** 26:42 If you are deploying them, you have to… Yeah, that… yeah, but yeah, definitely that will be an option of having that in… just in code.
**Bryce** 26:52 Yeah, I'.
**Vinod Vydier** 26:53 Isn't the Apple's, recommendation to use SPM, or a switched package.
**Bryce** 26:58 Absolutely.
**Vinod Vydier** 26:59 Yeah, yeah, no Flexi Framework is,
**Bryce** 27:02 And…
**Vinod Vydier** 27:03 Artifacts from the old times, right?
**nacho** 27:05 Yeah.
Yeah, but if you link to a binary with SPM, you have to also add a… a hash of the contents of the of the size of the contents, or whatever. So it fixes that version to your Then they want your… for security reasons, basically.
**Bryce** 27:26 Yeah, I am at CRC.
**nacho** 27:29 Yeah, but that means also that you cannot… Publish in the same repo you have, because you cannot create the binary without having the exact number… Yeah, yeah. It's a bit tricky. I did that in the past, just moving the data, but that created conflicts with some.
**Bryce** 27:51 Okay.
**nacho** 27:51 Customers of a previous company of mine.
**Bryce** 27:57 Alright. Any other any other topics? I think that we should create an issue.
For this.
And maybe we can do some more discussion in there, figure out when we want to do the turnover, the changeover.
I can actually create the discussion topic.
Maybe I'll do it in… I'll do it in the domain repo.
because I'm going to spend some time, working on this stuff after this meeting as well, so… No.
Okie dokie. Any other topics.
**Vinod Vydier** 28:40 No.
Go speed.
**Bryce** 28:44 All right. Have a good rest of your week. I'll see you next week.
**Vinod Vydier** 28:48 All right, see ya.
**nacho** 28:50 Bye, cheers.
**Bryce** 28:54 Good luck on the game.
