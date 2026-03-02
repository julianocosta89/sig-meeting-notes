SIG: eBPF instrumentation
Date: 2025-09-17
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:30 Invitated.
**Mattia Meleleo** 00:30 Father.
**Tyler Yahn** 00:32 How's it going? How's it going?
It's good.
That's good.
How's the day, progressing over there? Are you almost done?
**Mattia Meleleo** 00:41 Yeah, I'll say 1 hour in the half, and then done.
**Tyler Yahn** 00:46 Hello, Raphil.
**Rafael Roquetto** 00:48 Hi, do you want to switch? I'm just starting my day, so…
**Mattia Meleleo** 00:51 Yeah, let's switch. I'm, I will, stop now, and, no, I'm joking.
**Tyler Yahn** 01:10 Mitzi, is it getting to be fall in your area, or does that not really happen too much there?
**Mattia Meleleo** 01:16 Yeah, but not right now. Usually, it starts around November.
**Tyler Yahn** 01:22 Oh, wow, okay.
**Mattia Meleleo** 01:23 Until… yeah, the October will be very warm. At least in the past year, few years, it's been like that.
**Rafael Roquetto** 01:32 Is it humid or dry?
**Mattia Meleleo** 01:35 No, it's very humid here.
Is that a good thing? It's 27 right now, 27 degrees.
**Tyler Yahn** 01:46 Yeah, you got the AC on, I'm guessing, right?
**Mattia Meleleo** 01:49 No, I'm very… It must get, like, extreme for me to turn the AC on.
**Tyler Yahn** 01:58 I feel like it's gotta get to be, like, it would be, like, 25 Celsius, and I'd be like, oh, this is way too much, this is too hot, I gotta go down.
**Mattia Meleleo** 02:07 Hello, everyone.
**Tyler Yahn** 02:13 Yeah, so we could probably… let's see, we're almost 3 minutes in. If you haven't yet, go ahead and add your name to the attendees list. If you have agenda items you want to talk about, please go ahead and add them there as well. I'll start sharing my screen in just a second, we can get started.
Nika, do you know if, or, Rafael, do you know if Mario's able to join?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:35 I think so, I don't know. Okay.
**Tyler Yahn** 02:38 We can wait.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:39 I will ping him.
Steven can't, he's got a conflict with, Granite.
**Tyler Yahn** 02:46 Because Mario.
Oh, okay.
Hey.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:55 So, sound level is… Always faint when Zoom, I don't know what it is, but…
Zoom auto-adjusts my sound level every time.
**Tyler Yahn** 03:05 Oh, like, you can't hear us?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:07 Oh, I can't… I bet you you can't hear me when I talk sometimes.
**Tyler Yahn** 03:11 Yeah, you're a little louder right now, but… I don't know. No, you're okay. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:18 Yeah, I have to manually adjust it every time.
Google Meet seems fine, but every time I enable Zoom.
**Tyler Yahn** 03:28 That's kinda weird.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:28 Maybe it's a setting somewhere.
**Tyler Yahn** 03:36 Okay.
Well, we can jump in here. Welcome, everyone. Good to see you all. So, first up on the agenda, Nicola, you wanted to talk about, the 0.1 release, it looks like.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:50 Yeah.
Yeah, why don't you just bring it up, see if we have a plan. Do we make a 01 release?
There seems to be the Helm chart is blocked on that, and also that's blocking the…
A blog post announcing the project and all.
We got pinged by Severin about this.
So…
**Tyler Yahn** 04:14 Might be a good thing to do a one-release.
Yeah, that sounds fair. There were still two remaining tasks here.
One was adding the project licensing to distributions, which I'll be fair, I forgot until this morning when I was looking at it, so I can… I can work on this later on today. The other one is evaluating what we want to move internal before the release. This is one of those things where we have a bunch of Go packages that aren't,
Needed to be exported, that are exported right now. And so when we make this release, we're gonna have
to… it'll clutter the API and the docs.
And so the idea is…
Maybe we can just go through this really quick,
I definitely think the test directory is one of the things that we could put into some sort of internal package. We have an internal tools right now, which I think…
We were trying to change, but
I don't… so, this is also kind of a question for the folks at Bela that are using,
yeah. The… Yeah, the external API right now, like, what is actually.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:20 Yeah.
**Tyler Yahn** 05:21 here.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:22 I think we need to do that on our side. Okay, I forgot about this, too. This is a task.
Some of our Baylor maintainers to…
start serving this and bring back… we initially opened everything up so we can slowly migrate all the code and delete everything from Vela, but now that's done, we should go back and revert that stuff to go back to internal
Moby, initially, because it was, initially, it was the easiest to do, it's just everything, put everything in package components.
Needs to go back internal.
**MM Mario Macias** 05:51 Yeah, yeah.
**Tyler Yahn** 05:55 But yeah, I think… I think that's kind of it. There's nothing else remaining. I can work on the licensing thing after… after this later on today, but yeah, the…
I think other than that, I don't see anything blocking.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:11 Yeah, okay. Alright, alright, so we'll take that. Hopefully, we have a conclusion on that until next week.
**Tyler Yahn** 06:21 Can I assign this to you?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:22 Yes, sure, yeah. Okay.
**Tyler Yahn** 06:25 Yeah, I mean, obviously, you can find somebody else to do it, but just wanted to…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:28 Yeah, yeah, yeah.
**Tyler Yahn** 06:32 Cool. Yeah, but I mean, other than that, like, I don't… I think that we should be pretty straightforward on getting something out. There's… I mean, obviously a lot of stuff is happening, so it's a good idea to just take us… take a moment and…
and actually pin it to some version as features are coming out, and so we can keep track of that. But yeah, I think that's it, yeah.
Okay, cool. Alright, so we'll plan on hopefully soon, looking for the release, so pay attention. It should be, should be coming out.
Next up, I've got just our standard review of open issues, or I'm sorry, open pull requests.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:10 Excuse me. One more issue.
**Tyler Yahn** 07:13 One more issue?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:14 Yeah, about the GK autopilot?
**Tyler Yahn** 07:18 Oh, sorry, I thought that that was included. Okay, yeah, sorry, go ahead, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:21 Yeah, right, so Nimrod wanted to know last week, how did that happen? Well, we didn't know either, so I chased within Grafana and couldn't find any answer, nobody did it from our side. Then I reached out to David Ashbel, and he told me that apparently a large Google customer requested that both Bayline Alloy, get added.
so, we were not in the loop.
My guess is that once we actually make a release, we can probably make the same case for OB, but I think we need to stabilize or something, get to a point where we have something that we can publish.
And then we try to… Talk through the partnership program.
And get Google to add it, I mean, make the request.
**Nimrod Avni** 08:09 Makes sense. I don't know when we plan to do that, because, like.
some of our customers also, like, want both Obi, and maybe we can even,
cooperate with the continuous profiling, like the eBPF profiler, because I think that's also a project where they need elevated permissions and all that stuff, and maybe we can, like, unify those requests.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:33 Maybe through a CNCF, we can reach out to Google and see if they're willing?
**Nimrod Avni** 08:37 Yeah, I'm guessing I'm gonna go through OpenTelemetry, CNCM.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:42 Yeah, and make that request.
If you have a customer that needs this immediately, I would say maybe for now, get them to use Baylor. Baylor accepts all OB environment variables, so you can configure it. It's… we do have a build, that's, I mean.
Bayload 5… 2.5 and 2.6 are purely OB-based. There's…
It's just that we cut our release branch and we work on making it stable.
It's not far off from where Maine is, but it's a little bit off.
And I think we're gonna cut another one soon, 2.7.
You can configure it pretty much, they should be interchangeable.
And… You know.
**Nimrod Avni** 09:33 Oops, sounds good. Allah, we'll have a look.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:35 For now, until, I would say, this… we've found a way through CNCF to publish these images.
**Nimrod Avni** 09:44 Nope.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:45 Yeah, I don't see why… why Hotel Collector wouldn't be there, or…
**Nimrod Avni** 09:50 I guess Auto Collector doesn't need… I don't think it needs, like, many elements.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:55 No, premiers, yeah, okay, gotcha.
**Nimrod Avni** 09:57 Yes, just, like, all the EPF stuff. But thanks for, checking on it, and .
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:03 Yeah.
**Nimrod Avni** 10:04 That's good. Thanks.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:06 Yeah, I was surprised that this happened, and none of us from our team got even, like, pinged about this somehow, and…
By letting you away.
**Nimrod Avni** 10:16 You received the present number on the GCA.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:19 Yeah, yeah, I went through a… I… and nobody knew, and then I went through the partnership folks, and…
Okay, alright.
Nope.
So…
**Nimrod Avni** 10:30 Okay, next.
Good to know.
**Tyler Yahn** 10:36 Okay. Alright, yes, we'll… we'll have to follow back on that one.
Moving on to the open pull requests,
So, looking through, there's still a draft PR from Steven. This is something that we skipped over last time as well, so I think we'll still wait for this to switch out of a draft.
Update all the patch versions, this is still something to look into for the Prometheus upgrade, still haven't figured this one out, spent a few more minutes on it, but I haven't actually discovered it yet.
This we talked about as well last week, Mario. I… I think that.
**MM Mario Macias** 11:09 Haven't had time. Yeah, it was… there was still some pending issues with the… with some of the old testing environments.
that doesn't seem to like this new form, but I didn't have time to look at it and fix it.
**Tyler Yahn** 11:27 Okay.
Alright, so, still just a work in progress, then.
Next up, fail, fall back to bounded loop if BPF loop is not available.
**Mattia Meleleo** 11:38 Yeah, this morning I removed some code that didn't run some subtests in the 5.15 kernel, so this code is now testable.
And I noticed that I just checked the logs, and the verifier is failing because there are too many instructions. So for some reason, the kernel 5.15 creates more…
instructions than the 5.10 on which it is.
So, I think I will try to…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:09 Yeah, I read.
**Mattia Meleleo** 12:09 to reduce it a little bit, if it, just doesn't want to go, I will, tail call and call it a day, I think.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:20 I seem to remember there was a…
Anna Norfolk, you may know this. I… there, we…
don't seem to compile at 02 or something for those?
Isn't there something with our compiler that it's… we hit another thing that was weird with C, and then with O2, it would get stripped, but without O2, it was…
Maybe it's a compiler switch thing?
**Rafael Roquetto** 12:49 There we go.
**Mattia Meleleo** 12:50 Fritos.
**Rafael Roquetto** 12:53 I'm not sure, the only thing that… no, I'm not sure. The only thing that comes to mind is that we cannot strip the symbols because of BTF, but I think that's now related to this.
Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:05 Okay, yeah, some of these kernels are temperamental, and I think 515 is chosen for a reason.
**Mattia Meleleo** 13:13 Alright, I will proceed then. As I said, I will try to reduce a little bit the number of loops, and if it doesn't work, I will just tail call.
**Rafael Roquetto** 13:23 don't quote me on this, because I don't quite remember, but I think the 515 kernel has a different threshold for number of instructions that was relaxed in later kernels. That's why you might be seeing that, but I…
I guess.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:39 Yeah, I didn't.
**Mattia Meleleo** 13:40 Double check. It's still 1 million.
I think that one was locked in 5.4, or something like that.
**Rafael Roquetto** 13:48 Because the binary… the binary… the binary is the same, right? That we're trying to load, so it's… it wouldn't be…
The compiler, or the number of instructions.
Are you sure?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:00 Are you sure? Don't we build for each one?
**Rafael Roquetto** 14:04 Nope, It's the same binary. It's the same binary. Same compiler, same binary.
It's just the loader that's different. Why it's hitting that million instruction of 515 and other kernels.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:17 The verifier is different, too. So the verifier, it may do different kind of counting.
Yeah. What it considers an instruction, and I think there was some sort of regression in 515 that we kept on hitting.
Which is why we chose this specific
Kernel as something we test with.
**Mattia Meleleo** 14:38 There also might be some difference in the just-in-time config.
conflict, so maybe, yeah, I have to compare those two.
But yeah, the solution is, is always that one.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:59 Yeah. Yeah, split it with a tail call in half, or something like that, I would say. I don't know what else to say. Or reduce the number of instructions.
Yeah.
**Tyler Yahn** 15:10 Okay.
Well, we'll keep an eye on this, sounds like Mattia's still working on it. Thanks for the feedback, everybody. Yeah, we'll check back in.
Next up, these are… Upgrades,
We'll skip those. Still working on those, actually. The next is a draft from Mattia as well. I'm guessing this is something we can probably skip over, right?
Still being worked on.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:36 I reviewed this, Matthew.
**Mattia Meleleo** 15:38 This is mostly for… for context, in the, in the benchmark issue, in the HTTP header and body extraction issue.
I put some benchmarks over there, which are based on this, on this code.
So if anyone wants to see the benchmarks, then there is the code on which They are created.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:07 Yeah, cool.
I was actually, yeah, I looked at this, this is pretty cool, so yeah, we'd like to reproduce this, kind of take a look, and if you want us to start reviewing the code while it's in draft state, just let us know.
**Mattia Meleleo** 16:22 Well, the code is ready, so it can be reviewed if…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:25 Okay, good. Alright, cool.
I also had a question I wanted to ask, like, you guys, like, before I went on vacation, I guess this was a month ago or something, you guys mentioned that you had a customer issue with heavy… some BPF helper was too slow or something, was causing a network disruption when you deployed OB?
**Nimrod Avni** 16:45 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:46 Get to the bottom of it.
**Nimrod Avni** 16:47 Yeah, it was a very, very weird issue. It was,
after discovering some stuff, it was specifically in the… we discovered it, like, specifically for Node.js, and we discovered it's the Node.js, like, injector program that calls… like, it does, like, a specific syscall, like SIGUser1.
And apparently, they had that for, like, opening the debug port, but apparently they had… that, there was an option of doing a heap snapshot every time you did… you called.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:20 I'll singular.
**Nimrod Avni** 17:21 So it does… it did, like, heap snapshots every time, that the…
So, like, as a quick solution, we just added, like, an option to disable it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:31 And that…
**Nimrod Avni** 17:32 Okay. Like, we try to think if we can, like, detect it somehow, I don't know if that's, like, probably, like, we can solve a bit with Profile. I don't think it was… it's possible, but that was a very… we discovered it, kind of, by luck. It was interesting.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:47 So the customer has some settings set up that every time you select C user1, it would do a heap dump on their Node.js application.
**Nimrod Avni** 17:53 Yeah. Like, the default value for that is, like, there's a, like, a flag option in Node, and the default, default, like, signal is sig user 2.
And I don't know why they changed it to one which, like, collides with the bug port thing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:13 Okay, okay. All right, interesting. All right, so I think maybe we can detect that on the command line or something in the future, and…
ensure that… yeah, because we have the access to the full command line and environment variables, so if anybody's doing this, we should probably warn, say, we're not enabling this agent. Because if you disable it, no distributed traces, right? Node.js heavily relies on that now.
**Nimrod Avni** 18:40 Oh, that's good, we can, like, look at arguments and environment variables and… To see…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:46 Yeah.
**Nimrod Avni** 18:47 I'm just, like, thinking if it's something that… I don't know, if it's, like, the script that wraps the node execution… You'll still see it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:56 I still see it. Bosses, yeah.
**Rafael Roquetto** 18:58 Oh, that can be good. Nimrod, do you remember, if… how he's selling that case? Because I have a vague memory of that, but I think when I was researching, like.
In certain cases.
the user could override a signal for these, pragmatically in the code, and then I don't know how we would detect that. I mean, doesn't mean that… doesn't mean that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:23 Yeah.
**Rafael Roquetto** 19:24 said we shouldn't do, we should do that, I'm just bringing out the other, very other corner case, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:29 Yeah.
**Nimrod Avni** 19:30 Yeah, you're right.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:31 Yeah, in that case, we use the disable.
**Nimrod Avni** 19:34 I think that's how we discovered it, is that we had some Node.js application that had, like, basically handles, like, signals manually.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:43 And on the V1, it exited.
**Nimrod Avni** 19:46 So, we discovered it like that.
I mean… I mean, for their, like, situation, that will probably solve it, and, like, looking at the command line, but…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:55 Yeah.
**Nimrod Avni** 19:56 Still having the option to disable it as a backflip.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:59 Yeah, it's good.
**Rafael Roquetto** 20:00 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:00 We implemented that, right?
**Nimrod Avni** 20:03 Yeah.
**Rafael Roquetto** 20:03 Yes.
**Nimrod Avni** 20:04 Both of them options.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:06 Thanks.
All right, yeah, so we'll look at that benchmark data. I think we'll try to reproduce on our side. Like I mentioned in that comment.
like, when I tried this in the past, sending large buffers, it was very heavy. However, that was before we did all the work to optimize the reading of the data from the ring buffer. So now that… that used to do a lot of copies and all sorts of things, so…
maybe it's not an issue anymore, and we can just… Have a better default.
**Mattia Meleleo** 20:37 It was heavy from the CPU perspective, or…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:41 CPU side, on the user space, all in a go is this massive overhead. Not on the kernel. Kernel, I never saw anything,
that I was, like, massively increasing this, but on the user space size, it was just… Yeah.
**Mattia Meleleo** 20:56 Okay.
**Rafael Roquetto** 20:57 Did you see… did you see anything like that? I haven't looked at the, benchmark yet. Mattia, did you see if there's anything affecting the CPU?
Because in my street…
**Mattia Meleleo** 21:07 fuel…
**Rafael Roquetto** 21:07 It's fine.
**Mattia Meleleo** 21:09 Yeah, yeah, the CPU looked fine, like, in line with the lower buffers.
The only thing that changed was the allocations, and the heap, but that's expected.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:21 Yeah.
**Rafael Roquetto** 21:22 Because I think you might be right, Nikola, because from the top of my mind.
the CPU usage came from the parsing, the read, and whatever, so it might… this might have been not an issue anymore.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:36 Yeah, the ring buffer, like, I certainly remember that it was just massive overhead on the ring buffer reading, so since you fixed that.
With the direct cast and whatnot.
I think that problem might be solved, so… Cool.
All right, we'll review that, Pierre. Thanks.
**Tyler Yahn** 22:00 Awesome. Okay.
We can move on then, I'll…
start sharing my screen again. I think there's only one, remaining issue, or pull request. This is remove, references to the collector's batch process. I saw this open, recently.
Looks like, Nicola, you've already taken a look at this.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:21 Yeah, I think we need… may need to help this person. I think this was the issue that was opened from the community, right? That they wanted us to stop using the batch processor in the configs. But it's obviously broken tests, and I don't know what,
what that did, but I mean, the configs are removed, now the tests are failing, so…
I think we need to take a look at…
Why? And I think, symptomatically, the old tests are failing, and a lot of those configs were touched, so…
Those tend to be more stable, so we need to see… Alright.
**Tyler Yahn** 23:03 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:04 Right. Why? Yeah.
Maybe data's not making it, or something.
**Tyler Yahn** 23:09 Yeah… Was there, like, a cutoff where the collector…
supported this different config, and maybe we're not using the right version. I feel like we just upgraded to the latest version of the collector, though, so…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:23 That's true, I think so, but the old stuff may not have been updated, are they? I think they used some different config that's managed.
Okay. I… by these folks at Grafana, their work on Java Hotel.
I think there's discussion they're trying to upstream votes.
But we… we are… they may have actually upgraded. We're pinned on some version, and we're keeping it, stable. We should probably upgrade to the latest zones.
**Tyler Yahn** 23:59 Okay, so that might be what's holding us back.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:01 Yeah, maybe, because… yeah.
**Tyler Yahn** 24:05 Okay, well, we'll have to take a look at that then.
But, yeah.
I think, yeah, just we'll have to make some more reference. Obviously, we need to get these passed, so…
Yeah, like you're saying, like, these…
don't… these aren't flaky as much as the other tests, so…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:18 Yeah.
**Tyler Yahn** 24:20 Okay.
Well, yeah, well, hopefully the user can look into this a little bit more, and if not, we can probably take a little bit more of an active role, but otherwise, yeah, this stuff.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:30 Do you want to ask them to.
**Tyler Yahn** 24:33 upgrade to the oats, upgrade the OATS testing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:35 No, just to kind of look at the failures, see if they're… but I don't know if they have any… they have the skill to…
decipher what's happening there.
If not, it won't help.
**Tyler Yahn** 24:53 Yeah, yeah, we can… we can definitely help if not, so… Okay, cool.
Alright, that's the end of the open PRs.
Going back, nothing else on the agenda.
So I can stop sharing here. I did see,
David joined as well. I don't know if you wanted to add some color to Nicola's, comment about the GKE Autopilot stuff, but it sounds like it was automatically added, and we were talking about that earlier, for Bela.
**David Ashpole** 25:25 Oh yeah, some customer asked for it, and there's just an allow list somewhere in…
Google's pile of code, and someone just added it and then published it. If, yeah, if there's any questions about it, or if we want this project to be allow-listed as well, I can definitely
Figure out who to get in touch with.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:46 Yeah, that'd be awesome. That's what we're talking about, yeah, sorry.
**Tyler Yahn** 25:51 We def- we definitely want this project, it's just, timing, I think, I think is the only thing we came up with. Yeah.
**David Ashpole** 25:55 Yeah, I think it seems like it's based on, container image?
So I think once we have, like, some release artifacts, like, I…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:05 Hmm.
**David Ashpole** 26:06 Then we can make that happen.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:08 Cool.
**Tyler Yahn** 26:09 Yeah, that's…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:10 That's another one, Kevin. Sorry.
**Tyler Yahn** 26:12 No, I was just agreeing, I was saying that's what Nicola was saying as well, he already relayed that, so our goal is to try to get some… some tagged release artifact out. Does it have to be a 1.0, or is it, like, an early beta? Okay.
**David Ashpole** 26:23 as long as it's…
Yeah, I think as long as it's, like, community endorsed or whatever, like, a legitimate thing, then they'll…
You know, they'll… they'll…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:37 Right.
Okay.
Yeah, we were discussing that as possibly, the OTEL profiler as well.
along, like, I think they also have a build together with the collector.
collector contribution with the LTL profiler, so it might be multiple CNC projects that… We can kind of…
**David Ashpole** 26:59 Yeah, we've been living all together.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:01 Yeah.
**David Ashpole** 27:03 Yeah, that'd be great.
Cool, I didn't know there was that much interest in GK Autopilot, but…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:08 Oh yeah, customers are, like, hounding us, like, I have an issue open, and a bunch of people have contributed fast this.
**Tyler Yahn** 27:19 Well, awesome. Yeah, thanks for the insight, David.
At the end of the agenda, any other items people want to talk about? Or…
New things or new projects they're working on?
**Endre Sara** 27:38 I'm trying to figure out how to share some piece of Golang code for the thing that I proposed about DNS thingy, and I need to clean up my code, because it's actually inside our codebase, but I will at least
put some sample code into the issue. I want to do more, but I'm just trying to be cautious, because I'm a bit overwhelmed, but it would be really cool to get the NS3 thing out of OBI. So.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:07 Yeah.
Yeah, yeah, yeah. Yeah, we'll do. I think it's been asked before. I think somebody else actually brought it up. And you have a really valid point there. It's one of the things that this project kind of
good at it, is finding this low-level stuff, right? I'm not sure you'd be able to easily get a DNS information from an SDK instrumentation. Yeah.
**Endre Sara** 28:28 Usually, when your DNS lookup fails, you don't actually create a trace in the first place, so this is actually a pretty good use case, I think.
**Nimrod Avni** 28:39 I also looked at that, I saw, there is some, like, very minimal hotel conventions for DNS queries. There's, like, one metric, but, like, you suggested a lot more, and we don't… but we can definitely, like, do something like that, maybe we can propagate to some specification, that can be cool.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:58 can propose in your spec if we have something that here we agree that's good, and we want to be… yeah. I was trying to be religious, but there is no religion yet, so we can create one.
**Nimrod Avni** 29:14 That sounds really good.
**Tyler Yahn** 29:16 Well, cool.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:17 Yeah.
**Tyler Yahn** 29:17 Awesome, yeah, thanks for that.
Okay, well, if nothing else, we could probably end the meeting early here.
Thanks, everyone, for joining, good seeing you all. I will see you all in a week's time, or asynchronously.
Bye, everyone.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:31 Cool. Bye.
