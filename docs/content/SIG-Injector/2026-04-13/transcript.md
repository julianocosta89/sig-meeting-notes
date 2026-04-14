SIG: SIG Injector
Date: 2026-04-13
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/nv4ux0oxUFZgIxB6S8fX0mei1A5KT-R-egV6S085cJkeo8jozK8kZFsZ52i8hrw.I6VR4h62yiTslOjI
============================================================

## Zoom Recording Transcript

Jack Berg 00:01:54 Morning, Ted.
You're muted.
Ted Young 00:02:04 I was just saying, fancy seeing you here.
Jack Berg 00:02:07 Yeah.
Ted Young 00:02:09 Thank you so much for… for jumping on those… those rail issues, by the way.
Jack Berg 00:02:15 Yeah.
Yeah, I didn't realize this, I thought I would have to have a VM to test out stuff on RHEL, and then I was… I guess I just… it never occurred to me to search for, like, an image for it.
But I found an image, and so I can emulate Raul on my machine, and… run into all the same issues, so I should have done that months ago.
Ted Young 00:02:38 Here we are.
Bastian Krol 00:02:54 Hello, folks.
Ted Young 00:02:57 Hello, hello!
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:59 Okay.
Ted Young 00:03:10 I added a big blob about system packaging that we can discuss at the end, but put actual injector issues above that thing, please.
Michele Mancioppi 00:03:20 I mean, we have one that is related, so we need to decide whether we go with the conf.D approach.
in the debt or not, and I recall the last time we spoke about it.
We did not really get to… Decision, right?
Antoine was pushing that.
Bastian Krol 00:03:46 We write anything down the last time we discussed it.
Oh, was the last meeting March 30? There are no notes for that, or the one before.
Michele Mancioppi 00:03:58 They are not consistently excellent in the in-nots.
Bastian Krol 00:04:01 Yeah, looks like it.
So I don't… Remember the details super well, but… Summary, we didn't reach a final conclusion, could be correct.
Ted Young 00:04:15 So this is just basically the comp file, where should it go?
Michele Mancioppi 00:04:20 Yeah, totally what you need is a… Right now, when… a language SDK registers itself to the injector. They write a… they're supposed to write a line in a file, and that file is shared across the various language SDKs, and that does not play well with system packaging at all.
Because having multiple packages, owning or contributing to the same file, is guaranteed pain.
So, one of the things that I had done in the POC for the packaging was actually to split that file in a sort of conf.t approach, where each SDK was supposed to write a different file under the same directory, and that way would the injector discover the, the fact that, for example, on this machine, it can install Java.
And I remember that the discussion was like, do we break backwards compatibility, yes or no?
With, me expressing pain on the matter, and Antoine saying, it's early enough, we can break it.
And I don't remember if we actually decided what to do about it.
Bastian Krol 00:05:50 We might be rehashing the discussion from last time, but since we all don't really remember, so I think we don't break… Anything for users of the system packages, because if we publish a new system package, which this new stuff, it will accommodate for that. We only break… Maybe direct usage of the injector?
breaking changes, and I think that is acceptable.
A, because it's early days, and B, these are relatively… easy things to fix. I think one is the… that the default is empty now, or… Something like that, or changing the default directory, or stuff like that, and that's really easy to fix in the config file.
So I would share Antoine's viewpoint that it's not really a big deal to do that.
That makes the packaging easier.
Jack Berg 00:06:59 I'm just gonna say something obvious that I think everybody on this call knows, but, so, one, I agree that we're allowed to make these changes, we're not 1.0 yet.
The config API and the directory structure are a key part of the contract of this, and so it would constitute a breaking change once we reach 1.0. We should describe what kind of guarantees we make once we reach 1.0. We haven't done any of that yet, so we have freedom to do those.
The way we mitigate, you know, the risk and the pain for users pre-1.0 is we, We do things like we bundle breaking changes together, if possible. We provide a migration period, so we could have a 0.6 release, where we introduce the new directory structure, but still allowed the old directory structure to be used with a warning message.
And then, you know, have a scheduled removal of the old directory structure in some release in the future that we announce in our release notes. So, those are kind of the things that we can do to mitigate this if we are worried about the user impact.
Michele Mancioppi 00:08:22 Does any… does anything speak against So, What you say, Jack, makes tons of sense.
So if there is the old, the old format, use the old format, otherwise we use the new one.
If there's no format, we put a, we output something, although… Technically.
Logging in the injector is something we should do very, very sparingly.
Because… the people are not they use in general, I'm not going to care that the package is a bit while blue.
I don't know. Maybe we go with a clean break, and then we don't need to log anymore.
Jack Berg 00:09:06 Exactly, so over in OpenTelemetry Java, you know, we sometimes will make breaking changes. We only make breaking changes where we're allowed to, but, you know, depending on judgment, subjective judgment. We either make the breaking change just, like, all at one time and rip the band-aid off, so to speak, or provide some sort of migration path where, you know, we provide the new solution, backwards compatibility for the old solution for some period of time, and then kill the old solution. So, you know, You know, we have to decide on a case-by-case basis which approach we want to take.
I don't personally know of a large number or any significant usage of this directly on Linux right now, and so, like, that's the user base that we're trying to protect or shield from this type of change, so I think in this case, unless unless somebody speaks up and has, like, a user base, a customer that they want to shield, that they know is working off of Linux with this, then I say rip the band-aid off and do it without a migration period.
Michele Mancioppi 00:10:14 My, queasiness on the matter is because… We have Ray Charles' level of visibility about who's using the interactor at this time.
Like, we know nothing. Where do you chants know of analytics?
Jack Berg 00:10:28 Yeah, and that's always going to be the case with libraries, and… I don't know, we just have to sort of count on the communication channels that we do have, Slack.
GitHub, and then the maintainers, and the idea that we have the finger on the pulse of our user bases that, try to extract signal where none exists, or where little exists.
Ted Young 00:10:53 Breaking everything would be a great way to get them to find us.
Bastian Krol 00:10:58 Excellent.
Michele Mancioppi 00:10:58 Yeah, it's not the best impression that we would engender, but… so, I understand the consensus is effectively we're the band-aid.
0.6.0 goes with the confi, end of story.
And I'll put.
Bastian Krol 00:11:11 Yeah, I think, I think that's good, and to be honest, I think you worry too much, because I think the user base… It's really small, if there is even one.
Michele Mancioppi 00:11:21 I have never been accused to be careless or not worry.
Bastian Krol 00:11:25 No, no, that's fine.
Michele Mancioppi 00:11:26 Okay.
Jack Berg 00:11:28 I… so, the only thing… so, the 0.6, like, I'm in favor of ripping the band-aid off.
my topic is about this issue that I ran into, trying to run this on RHEL, and it is sort of, like, time-sensitive to fix, at least maybe not all of it, but portions of it. And so, like, I don't know what the schedule is for this sort of adjustment of the, the config system, but, you know.
how immediate is that? Like, I would like to, you know, propose that some of these PRs and thoughts that I have open, maybe we can cut a release quickly after, you know, we agree on those.
Michele Mancioppi 00:12:14 I mean, I can imagine that I could get the PR for the coffee.
To work later tonight.
So, we could be able to merge to release in a couple of days.
Bastian Krol 00:12:27 Jack, I didn't really understand what your point fully, I think. Do you want your changes to go in before that braking changes, or quickly after, or.
Jack Berg 00:12:38 I just don't want to block a release on maybe, like, a more complicated config re-architecture.
if… if it is, in fact, complicated, and if it would take, like, several weeks. But if it's, like, if it's quick to do, and, you know, we can get a release out this week, then, you know, I'm just in favor of doing everything at once.
Bastian Krol 00:13:01 Yeah. Yeah, so, Antoine already extracted these confD changes from Michaela's very much larger PR, and I think they are basically ready to merge, right, Michaela? Just… we just… I just brought up, this is a breaking change, and that's where we stopped on that.
Michele Mancioppi 00:13:17 Yeah, so it's, this is about the factory back porting, one of the changes I did in the, in DPR.
239, so the packaging, prototyping what used to be the OTEP, that then became the project.
Antoine was going through the process of effectively taking out smaller parts of that PR and, kind of putting it in main to reduce the delta.
Bastian Krol 00:13:45 And that is 291 that we are displayed.
Michele Mancioppi 00:13:47 239.
Bastian Krol 00:13:49 239 is your original PR, and 291 is the one with just the conf DJ chain, it's from Act 1, if I'm not mistaken.
Michele Mancioppi 00:13:58 I didn't know… Good. Then I can, instead of making it from scratch, I can fix this PR.
Alright, good. Let's work.
Bastian Krol 00:14:12 Yeah, I think VB probably could… give that one another round of quick reviews, and just… just merge it, I think.
Michele Mancioppi 00:14:21 There are other build issues on that.
But.
Bastian Krol 00:14:24 build issues on that. Oh, yeah.
Right, that's probably in the… In the, yeah, that's in the packaging integration? No, it's… it's in the injector integration.
Michele Mancioppi 00:14:35 I'll figure it out, and then…
Bastian Krol 00:14:37 Yeah, yeah, yeah.
Okay.
Could.
Michele Mancioppi 00:14:45 Jack, do you want to remind us what is the time-sensitive issue with RAM?
Jack Berg 00:14:50 Just that we have some users that are trying to incorporate the injector and start picking it up, and Trying to turn that around fast for that purpose.
Bastian Krol 00:15:04 Do you know what's the context of that usage? Just because we just had that discussion, who is using the injector, and how? I'm super curious, what's… what's…
Jack Berg 00:15:17 Yeah, it's a user that, I think fits squarely in this category that we've been discussing the injector for, you know, outside of Kubernetes. So, they run their environments to a large degree directly on Linux, without any sort of, you know, Kubernetes or containerization intermediary. And, you know, they're very interested in the injector as a sort of force multiplier.
to get OpenTelemetry deployed to their environment quickly. And yeah, they run on… they run on RHEL. And, I think, I shared some of the details in that issue, but when you try to run even, like, simple Java applications, and presumably other applications on RHEL.
And I haven't completely pinned down why, but basically, the libc detection, runs on every binary, every process that starts, and many of the binaries, and again, I haven't exactly figured out why, produce libc detection errors, or maybe not many, but some do, and maybe, maybe important common ones do.
need to track that down. And so, like, I talked about the four different ways I'm thinking about, like, addressing this. So, like, you run the… you install the injector on a Linux box, and you run some sort of simple command, like grep.
and you see, like, an error in grep that's, like, from the injector. It's not an error, it's a warning, but you don't know the difference, because you don't know, like, the source code. And so it becomes, like… it's, like, a really scary thing really quickly, and And so, I want to be able to avoid that, or at least provide mitigation if it does happen. And so, you know, the first PR that was merged was to fix this bug, this minor bug that I found in include-exclude evaluation, that's fixed, that's merged, but then, the next step is like, hey, if you do encounter this, like, we're always gonna have this long tail of, of processes for binaries where libc detection fails. For some reasons, it's like unknown unknowns. You know, maybe, maybe we do a really good job, but there's just, like, some situation where We don't fully understand, because we haven't encountered it in the wild.
you should be able to configure the injector to skip those cases when you encounter them, to minimally put your, like, system operators' minds at ease. And the way that you do this is you bump up the include-exclude evaluation ahead of libc detection.
And that's what the next PR that I have open is, so that, like, you know, you have this very early evaluation of which processes are… the injector applies to, and so, you know, if you encounter a libc detection error, you can just update your configuration, and that warning goes away from your logs.
So you never see it again.
Bastian Krol 00:18:17 Yup.
Jack Berg 00:18:17 So, those… that's like low-hanging fruit, right? And then, you know, after that, it's like, well, what about… what about fixing the libc detection? Like, I want to do that. I want to investigate further what the actual problem was and fix that on RHEL. And then, finally, well, could we ship the default config with some reasonable out-of-the-box include and exclude? And there's some problems with that, so I'll table that conversation.
For now. And, you know, the first two.
PRs that I opened, I think, are pretty straightforward.
Michele Mancioppi 00:18:50 To be fair, I think that the default, include and exclude It's more a matter of packaging than it is the injector itself.
Jack Berg 00:19:01 Right, like, you know, ideally we would, we would delegate the responsibility of specifying what is included or excluded to the language experts, and maybe that's what you're pointing out.
Michele Mancioppi 00:19:14 Not even… Not as…
Bastian Krol 00:19:15 to the distros, it's probably distro-specific, it's, like, different directories on Red Hat than it is on, I don't know.
Michele Mancioppi 00:19:24 I'll give you a few examples. It's… there is a whole bunch of Python doing background stuff in Ubuntu.
It almost never makes sense to inject it.
Yep. Those rules are going to be very different in Ubuntu and Debian derivatives than it is going to be in RHEL.
Jack Berg 00:19:42 Got it.
Bastian Krol 00:19:44 But to… on the points you raised, I think that is a fully, fully correct analysis there, so, Currently, I think it mainly, mostly works as design, so all these processes that, have emitted warnings probably just don't bind to libc, like grab or other shell stuff. That's… that's fine, and right now, the default behavior is to… to… emit one warning lock line for that, and that, of course, if you install it directly on the Linux box, will create a lot of these warnings, and we should get rid of those. I think, one of… I think your third point was fixed lip-C detection. There might not be anything broken with it, it'd just be… maybe it's only processes without LIBC bindings, and if we can exclude them by default, by just excluding anything from the… I don't know, system executables, or anything like that, that would probably Be good enough.
But you're right, the first step needs to be to move that before the libc detection, which we already did receive.
Escape Hedge by… for manually disabling the injector, and that… that is just the same.
thing here, I wonder if they should…
Jack Berg 00:21:05 the disabling of the injector if we move include, exclude up.
Right? Because the include-exclude is, like, this big sort of switch, it's like a binary switch that enables it or disables it wholesale, and that's equivalent to just an exclude star.
And so, you know, I guess they're sort of different.
Bastian Krol 00:21:27 So the environment variable to disable everything, or to disable the injector completely, is just something that you can… Directly put on a process.
and not have it in the configuration file that is system-wide, so that's where I would see the difference.
Jack Berg 00:21:48 Well, I think you could… I think there's an environment variable for setting the exclude paths as well, and so you could have a process-specific environment variable that, you know, disabled it just within the context of a single process, if you set, like.
Bastian Krol 00:22:04 Okay.
Jack Berg 00:22:04 Exclude environment variable to star.
Bastian Krol 00:22:08 Okay, okay, yeah, then this is maybe a little bit redundant in… indeed, we might need to… Consolidated at some point.
Jack Berg 00:22:19 I think it made sense, because, like, the include-exclude was at this later evaluation cycle, so you wanted this, this switch to you know, before you did libc detection, which could potentially break. But, like, if you can bring the evaluation criteria really early up into the injector's lifecycle, and also have a lot of confidence that it's reliable, and it won't break your processes, then, you know, you can adjust your thinking, and maybe that… that… disabled environment variable that was previously needed no longer is, but, you know, I don't know, it's not really that important right now.
Bastian Krol 00:22:55 You know.
Jack Berg 00:22:56 A minor observation.
Bastian Krol 00:22:58 Yeah, yeah, good point. I think there was one detailed discussion on your PR, whether we call, or we loop through the environment every time, or if we read it all into memory once, and then go from there. Do we maybe… Is that something that we want to continue on the DPR discussion, or maybe we can clarify it here?
Nikola Grcevski @ Grafana / OpenTelemetry 00:23:20 Yeah, I don't know, yeah, we should discuss that. I, I ran… I pulled this branch, and I added a little print on how many times it's called, and I think it's 10 times now that the reading the environment variables is called.
But it's really quick, I mean, so in the grand scheme of things of how long it takes for the injector to do other things, this is sort of minor, so I put the timings in there.
what I thought. But as I was doing that, I found something interesting. So, I was trying to turn on the log level, and in main, the log level would not be read correctly, before Jack changes.
I put the details and opened an issue regarding that as well. So every time, like, I read a very simple command. I said, like, injector log level debug, and then something else, and all of a sudden, it would say, some random garbage text is not equal to debugging forewarn… whatever.
But with JAX changes, that goes away, so I think it's some sort of memory corruption problem.
Did we deallocate something when we added the… both of them.
Michele Mancioppi 00:24:32 to be arrested.
Nikola Grcevski @ Grafana / OpenTelemetry 00:24:33 red… I don't know.
Michele Mancioppi 00:24:34 Yeah, my guess is that… So the, we can read the environment only after we've done the lip-sy detection, because the… Why not?
Bastian Krol 00:24:44 No, no, this, this, this pre-libsy detection environment where we are in works by reading ProxL engine.
Nikola Grcevski @ Grafana / OpenTelemetry 00:24:52 Yeah, so it's not actually.
Michele Mancioppi 00:24:54 Yeah, interesting.
Nikola Grcevski @ Grafana / OpenTelemetry 00:24:54 But it's not only that, it's like, in this case, the application was Java, so I was… I had the label simple command when I ran this on top of Java, for which we should be able to find libc, and no problem.
I don't know, like, I had never seen it before.
But… yeah, I can consistently reproduce it.
Bastian Krol 00:25:14 That's… that's super interesting, because I'm quite sure that this worked at some point, and that change is also not so… and don't we even have tests for the injector lock lab? I… I don't know, but yeah, that's… that's… I didn't look into that yet.
Nikola Grcevski @ Grafana / OpenTelemetry 00:25:31 Yeah, but with Jax, what he did was he actually separated as, like, getAMP one thing, and you're looking for one specific thing, the problem went away, so I was like.
Bastian Krol 00:25:39 Oh, that's, that's, that's good.
Nikola Grcevski @ Grafana / OpenTelemetry 00:25:41 Because I couldn't even actually log things. So I had to initially, like, print with the log, and to determine the timing of how long the whole previous function took.
Where we kind of read and process the environment variables, and I wasn't… it wouldn't print. So, Yeah.
Jack Berg 00:26:04 Yeah, so that's cool. And we could probably track down where the bug specifically is with the existing pattern and fix that.
it's good that it's fixed in this, but, like, putting that bug aside, which is interesting, like, about the performance, so, you know, we're slowing down the injector now, And, you know, the question is, when is it too slow? Like, at least that's the question in my head. And so, I think it would be useful for us to have a budget.
Like, to be… document somewhere in the project how long we think is acceptable for the injector to run the various parts of its life cycle. There's, like, two key things. There's, like.
The evaluation phase of whether the injector is actually going to be enabled or disabled.
And that needs to run really fast, because that's gonna run prior to everything else. And then, you know, and it's gonna run on every process start. So, even ones that, you know, the injector is not going to ultimately do anything to. So that needs to have one budget, I think, and then there's, like, another budget for everything else. And, like, the… you know, maybe… I was just looking this up on the internet. I was, like, asking the question, like, what is an acceptable amount of time for, like, an LD preload-style program to execute in before you start to notice?
And the, the internet, and it's like, you know, the Borg mind of AI is reporting something like tens of milliseconds, like, before it starts to impact, you know, system performance. And we're still on microsecond scale for the injectors, so we have, like, a lot of headroom. But, you know, I also don't accept that tens of milliseconds would be acceptable, so, like.
You know, in my head, it's like, come up with an acceptable amount, document it, and then once we start exceeding that amount, then we can have, like, conversations about trade-offs. Like, you know, trading off memory for time.
Bastian Krol 00:28:06 But then you would also specify, probably, a memory budget over a budget, because it's a trade-off, ultimately, always, memory versus speed, and then we need to look at, also, budgets for both, probably.
Jack Berg 00:28:20 Totally.
Yeah, so, like, I think we should go with something like that, like, accept that this amount of time is still probably well within any budget that we could come up with, and also document a budget for time and memory. So, you know.
As time goes on, and we're tempted to add more things, we can, you know, point to this previous decision we made about, like, you know, not exceeding a certain amount of time, or whatever.
Michele Mancioppi 00:28:49 Yeah, it's going good.
Bastian Krol 00:28:50 Let's…
Michele Mancioppi 00:28:52 This is…
Bastian Krol 00:28:53 Time awards, not also depending on the length of the environment?
Nikola Grcevski @ Grafana / OpenTelemetry 00:28:59 Yeah, it wouldn'.
Jack Berg 00:29:00 Right.
Bastian Krol 00:29:02 Okay.
Jack Berg 00:29:03 Definitely.
Michele Mancioppi 00:29:04 That is all iterating in memory. I really don't think that is the issue. Now, what we're going to see is that the more we upfront I.O. operations, like, go and read the configuration files for include and exclude, then that is where the time is going to be used, mostly.
Because all the lookup, it's… There is no allocation, just goes and throws the memory until it finds what it's looking for.
Bastian Krol 00:29:30 And you said, you said reading from ProxChef NRE1 is a virtual file, that's not… that's not actually a file operation. No, no.
Michele Mancioppi 00:29:38 No big deal, but reading the configuration files from included.
Bastian Krol 00:29:40 No, that's from this, that is the order of magnitude slower, sure, that's… but I was thinking about procrevAnion also just as a file, but that is naive, obviously, apparently.
Michele Mancioppi 00:29:58 So how do we get to these numbers?
Jack Berg 00:30:01 We just throw out a number.
Like, we're not, like, let's not pretend that we can be more scientific, more, specific than we'll be able to, you know?
Come up with a number, and then accept that the number is, like, you know, imperfect and subject to change over time, as, you know, the arguments change, but…
Michele Mancioppi 00:30:24 With our current numbers.
Jack Berg 00:30:27 Like, you know, this is the problem with numbers, too, is they're hardware-specific, they're environment-specific, so the number of environment variables, for instance, will dictate it.
Michele Mancioppi 00:30:42 And this is why, you know, people are getting to the final say, It's gonna be difficult.
Jack Berg 00:30:47 I know, and that's why we don't put too much credence on this, like, you just… Well, you don't… you don't put too much credence on it yet, like… over time, as usage increases, there will be more parties interested in… in performance, and that become performance sensitive. But for now, like, because there's not a lot of people using this, like, we just have to… sort of acknowledge that this is a performance-sensitive application, and we need to be reasonable. And, you know, we start to develop the rails, the tools.
To reliably measure this over time, but we don't have to do it all at once.
Bastian Krol 00:31:26 That's good.
Jack Berg 00:31:29 At least that's how I would do it.
Not make it a bigger problem than it needs to be for now, but, you know, also sort of putting our finger in the wind, anticipating a future where it is something that we have to pay attention to.
Michele Mancioppi 00:31:43 So, for example, I could tell you that if I had to have these discussions at canonical, double digits, milliseconds.
Would cause a riot.
So it'll be somewhere between 5 and 9.
With a lot of chagrin.
Jack Berg 00:31:58 And what, what did, what did your timing, Nicola, say with the change? How many microseconds was it?
Nikola Grcevski @ Grafana / OpenTelemetry 00:32:05 Yeah, each reader of the addend was around 4 microseconds, just the wall clock time, I just put a… Time before and after.
So, hey, I mean, timestamp is 40 microseconds.
Jack Berg 00:32:20 40 microseconds for the entire… Evaluation of this.
Nikola Grcevski @ Grafana / OpenTelemetry 00:32:23 Yeah, but that… that actually includes a program where we wanted to actually, instrument. So, for anything that is sort of like this Graph LS and whatever people are running, for that, it will be only 2… around 8 microseconds?
Because you're just gonna get called twice. One for the log level, one's to kind of… Figure out if you shouldn't do this, right?
Jack Berg 00:32:53 Yeah, so, like.
We're at… we're at 40 microseconds right now, even with this performance regression, and you know, I get that tens of milliseconds would be a deal breaker, but even if we said that 1 millisecond was our budget, we would still have the budget to go 25 times slower than this before.
Michele Mancioppi 00:33:12 Let's make it strong and say, half a millisecond.
Jack Berg 00:33:15 Half a million.
Nikola Grcevski @ Grafana / OpenTelemetry 00:33:16 No, no, no, I mean, just to be clear, your change introduced 40 microseconds extra, or something, because previously we would just read this… Once, like, the environment variables.
So, I mean, but that whole function that… I forget the name of the function that does the reading environment variables and does all the processing and everything else, that one itself was 40 microseconds, so… Your change was… I mean… I don't think a big deal. That's based on my measurements, so…
Michele Mancioppi 00:33:49 So, if you say 40 microseconds is only a function, the entire injection process How much is it?
Nikola Grcevski @ Grafana / OpenTelemetry 00:33:56 I don't know, I haven't actually checked, but I would say half a millisecond or so.
Based on what I've seen.
Odd.
I haven't measured yet, and it's kind of, like, depends on a lot of factors. But… For this case, it was around 500 microseconds, so, like, half a millisecond.
Michele Mancioppi 00:34:18 I mean, my guess is that the, the moment the way to do injections, since we go and check.
But the files you want to inject exist?
And that some runtimes have more files to check.
than others, that is going to be a significant variability. Todd Knight, you need to look up, I think, like, 3 DLLs.
Something.
Nikola Grcevski @ Grafana / OpenTelemetry 00:34:39 Yeah, so I tested Java, so that might be not representative.
Jack Berg 00:34:45 But again.
There's, like, two numbers we care about. Like, the cost to be able to evaluate whether you should inject or not, that time, and then the time to actually, you know, do the injection. And, I think we have a much bigger budget to… in terms of the time to actually do the injection.
Because it's running on a subset of the processes at that point, and these subsets, like, you know, it's a really high-value outcome at that point. You've narrowed it down to your potential candidate set, and you really want these things to be instrumented, so you're willing to pay a few extra microseconds.
Bastian Krol 00:35:21 And a lot of these are dynamic runtimes that themselves take a while to start up, so we might not be very noticeable in Adobe M or in a CRR.
Michele Mancioppi 00:35:34 No, you can bet that we will be playing for every slowdown ever perceived by mankind, so…
Bastian Krol 00:35:39 Yeah, okay.
Jack Berg 00:35:40 So, just to kind of, like, move us forward, why don't we say this? So, I'm adding roughly 40 microseconds for this. That seems like a small amount of time. We have some ongoing work to do to come up with, like, budgets, and also to, like.
develop some intuition about what the current time is for end-to-end injection. So why don't I open an issue to do that?
Just to, like, come up with that, and then we can sort of, you know, work on that in parallel or separately. And I have some experience from OpenTelemetry Java, of using OpenTelemetry's dedicated hardware to do, more deterministic performance testing. We have dedicated hardware from somebody that donated it.
So, like, I know how to use those rails and to be able to run performance tests on an ongoing basis.
Bastian Krol 00:36:33 That sounds very good.
Jack Berg 00:36:41 So, can we… We roughly… how do folks feel about trying to target a release, then, for the end of this week?
And we try to… we try to make a concerted effort to get, Mikel, your changes in related to the directory reorganization, and this… you know, 313PR of mine, and like anything else that comes, great, but those are the two priorities.
Bastian Krol 00:37:11 Yep, let's do that.
Jack Berg 00:37:14 Sounds great. Thank you. I'll cede the floor.
Bastian Krol 00:37:22 Ted, do you wanna come in with your larger issue?
Ted Young 00:37:27 Yeah, let me just, Doop dodoop… Let's share so we can all be looking at the same thing. So, this is just an update about the packaging SIG that I know you all care about, trying to get that work out of here.
You know, first of all, apologies, I feel like, you know, that GC and TC have been slow, to respond to this, and we need to do better on that front, and be more public when we are discussing these things.
But, we have been trying to, to sort out… How to rearrange the work that's in flight to make room for this, because we do know that it's important.
So, based on that plan of work, I just went ahead and updated your PR, Michelle, to add this to the deliverables section.
The main concern was really that when it comes to dealing with config.
Er, sorry, not config, but contrib in all the different languages, which is what we're… the bulk of what we're packaging up.
That looks like work, for the TC, but also, like, work for maintainers. So, part of the goal was, how do we divide this work up so that, the packaging SIG can just get moving, and actually build something useful that people can get into their hands and have feedback. Because we believe if we've got that, then people would give us feedback, they'd be a lot more interested in it, and we're not waiting on trying to do some kind of bigger organizing.
So, my proposal for that is to break it up into two phases.
Phase 1, I think, probably with the work you've already been doing, will go very quickly. But basically, build out the OpenTelemetry package, the subpackages, but keep everything, for now behind an unstable flag. And…
Michele Mancioppi 00:39:42 That's the part where, I had concerns. It was not the… it was not, the right, the discussion that you see. This was too technical.
There is no such thing in packages, to have kind of an unstable flag.
I mean, the package is there or is not.
Which is where, then, the question becomes.
If we want, to, treat Preferentially different languages that are more stable.
then, maybe we should not, in Phase 1, build the OpenTelementary meta package.
Ted Young 00:40:20 Well, one thing I've wondered is it just two different distros that we're giving people, right? Like, we want to have a stable by default distro that gets you just the stable stuff, right? But you do have people who would want to be able to… to use the unstable or experimental stuff, and… deploy it this way, and I don't know if that's just, like, it's just a different package, OTEL Unstable, or… Something experimental or something?
Michele Mancioppi 00:40:48 I think there are different APT commands.
Ted Young 00:40:51 Right, right, like, it's a totally different… package, essentially, that you'd be installing.
Michele Mancioppi 00:40:56 like, what we would say, then, is, hey, the OpenTelemetry meta package is experimental. The reason I don't stand the way I know, of flagging something like this. So, it's not like… if you don't want to install all these languages, go and install the injector, OBI, and whatever else you want.
Ted Young 00:41:15 No, but I mean even for these sub-packages, right? Like, there's always gonna be a situation in any language, like Python, what have you, where we're gonna have, like, some packages that are stable, and then additional packages, you know, that are not yet stable, they're still experimental.
So, one approach is we're saying, like, we're not going to install anything that's marked as experimental.
Ever with this tool, but the other is, like, you know, there needs to be some mechanism for saying, no, give me… give me all this stuff, not just the stable stuff. I could be misinterpreting What users want on that front.
Michele Mancioppi 00:41:58 No, I mean, I sympathize with me. I'm trying to understand how to make that work.
Because the delivery mechanisms of packages Work philosophically different from feature flags.
Ted Young 00:42:12 Great.
Bastian Krol 00:42:14 How about… we… what if the package just packages all the stuff, but the more experimental stuff is off by default in the configuration files, and then… I mean, configuration files can be overwritten by users for system packages? That is a well-known concept, right? And they can enable experimental stuff they want.
Michele Mancioppi 00:42:40 It's going to be a… it's a… it could be possible. Let's say you could say, look.
installment telemetry, and it has… packages have, among each other hard-coded dependencies.
Yeah. If OpenTentry will pull in the injector, Python, Java, whatever.
And then, we say the open directory package or the configurations by default are off.
So if you install Python, then you need to go and turn it on, because it's not great yet.
Bastian Krol 00:43:11 Right.
Michele Mancioppi 00:43:12 It's all the great UX.
That is what I'm trying to say.
Bastian Krol 00:43:16 Yeah, well, but so is every other opt-in mechanism.
If you want to make it opt-in, there is… there needs to be some user interaction.
Michele Mancioppi 00:43:25 That depends, because, for example, the opt-in nature of packages is if you want it to install it, if you don't want it, you don't install it. That's why I'm saying maybe then we either mark experimental the meta package, or skip it in the first phase.
Because then, do you want Python? It's experimental? Yeah, you need to go and do APT install open directory dash python, otherwise it doesn't get pulled.
Bastian Krol 00:43:51 No, that's all good.
Ted Young 00:43:53 We could… maybe it is just the answer to keep it simple is, like, you know, we're just gonna install stable things if you're using package management. Like, if you want the experimental stuff, don't… this is not the way to get it.
Michele Mancioppi 00:44:05 No, I think the solution is very simple. We do not do the Open Tendantry meta package at first.
But if we say it's a remarket, it's experimental. If you go and say, like, stable instructions, go to install the injector, Java, and Node.js, you want to live dangerously, install the MCTA package, it pulls everything, including stuff that is less than great.
Ted Young 00:44:26 So, a problem that we have is, well, I don't know, Jack, in Java, in Java instrumentation, do you have a bunch of packages marked as stable at this point? Because I believe we don't, right? Like, that's been the thing. We've held off on marking things as stable, at least in a lot of languages.
Jack Berg 00:44:44 So, I don't know what you really mean by that, because… so, the package that OpenTelemetry Java would publish would be one that bundles up the Java agent.
And the Java agent has a macro version, like this, the version that, you know, covers tons and tons of, you know, instrumentations that, that it it includes. And, so some of those instrumentations are unstable, some of them are stable, and the Java agent overall is stable.
Right. And so what we mean by that is that, like, we are going to… the Java agent will take care of, like, the housekeeping business to make sure that… that… output telemetry that you are going to experience as a user of it will not break outside of major versions. So, it essentially means that the versions of the individual instrumentation libraries They don't matter. Their stability contract doesn't matter, because the Java agent is, like, underwriting the stability of itself and all of its instrumentation holistically.
Ted Young 00:46:01 Hmm. Okay.
Michele Mancioppi 00:46:02 Yeah, we're talking… we're talking about packages at multiple levels here.
Jack Berg 00:46:06 Yeah.
Michele Mancioppi 00:46:07 And that is confusing the discussion significantly.
Ted Young 00:46:09 Well, the issue is just that in most languages, the thing we have is we have unstable semantic conventions, or we have semantic conventions that have become stable, but people have not gone back through and updated all of those contrib packages to be marked as to the new stable version.
And we have users who are like, you know, we're… we have… we're contractually obligated to not install software that's still marked as beta or unstable. So, to get around that, one thing we want to do is decouple the idea of stability of instrumentation packages from the data.
in a bunch of languages like Python, we have a bunch of packages, instrumentation packages, that are essentially de facto stable. And we want to take all the de facto stable stuff and just mark it all.
Michele Mancioppi 00:46:59 1.0.
Ted Young 00:47:00 And then when stuff comes back in, we want to do it as 2.0 when we update the, this… update it to the latest version of semantic conventions. The reason we're thinking about all of this, just to be clear, is because we're trying to unblock the.
Michele Mancioppi 00:47:16 Shipping.
Ted Young 00:47:17 This stuff, right?
Michele Mancioppi 00:47:18 Yeah, it's, this is gonna be… this is going to look, then, very similar.
to, what happens when you have, for example, an Ubuntu main, Node.js libraries. Then each instrumentation package is a separate system package Grouped in different meta packages.
they're gonna have Python, all that install Python, there's stable, and Python, there's YOLO, and then YOLO has inside a whole bunch of different packages.
Ted Young 00:47:50 Exactly.
Michele Mancioppi 00:47:51 Boy. Okay.
Jack Berg 00:47:52 Wait, wait, wait, wait, wait. I don't actually think that needs to be the case. I think other languages should follow the lead of what OpenTelemetry Java has done. So, like, let's say you have 100 instrumentation libraries, and they all have their own independent versioning schemes, and these instrumentation libraries, some are stable, some are experimental, some are making, breaking changes all the time.
you need… something that… Curates all those together, and has its own versioning scheme.
and is making curation decisions about which of these instrumentation libraries to include and when to upgrade them, so that you have an overall, like, Java agent version.
Python Auto Instrumentation version.NET agent version, Node.js auto instrumentation version, and that versioning scheme of that, let's say the Java agent's on 2.22 right now.
Like, users can be confident that there won't be breaking changes on any of the instrumentation that that includes until it goes to 3.x.
And Python needs to do the same thing. Python needs to have, and it does, I think, have, like, an overall version for its auto-instrumentation product. And it just needs to do the housekeeping work to make sure that there are no major… there are no breaking changes outside of major version bumps.
Ted Young 00:49:17 Crazy.
Exactly. There's work in each language to figure this out. There's work in each language to then just do the task of going back through all the things that are de facto stable and just marking them as actually stable, like bumping them up to 1.0. If we feel like… there's gonna be a fair gap between when we could get to them and actually, you know, update them to the latest semantic convention. So, like, that's, like, a bunch of work, and the concern is that maintainers are busy in different SIGs, right? They're all working on whatever it is they think is the current highest priority, and so if we want to do this work, we have to do it with maintainers.
Doing all of that work first is gonna delay us from starting the system packaging SIG and shipping something that people can play with.
So the idea we want to propose is, if there is a way to have a… a more, you know, unstable version, if we can figure out the… the way of, like, just going into each sig and saying, we're not gonna try to go through and make sweeping changes to everything and try to touch every package and update them, but can we just solve the… how do we ship the unstable stuff that you already have?
then we'd be able to bundle that into a system packager, and actually write that thing, and hand that to the community to get feedback. Because the concern is, right now, outside of Java, what do we have that we could actually package up?
So it's just this kind of, like, how do we unblock this situation, right, so that we could… because part of my feeling is, the sooner we can actually make the system packaging be real and get it into people's hands to try it, the more, Interest there's gonna be in feedback, and it'll also potentially help drive interest in… in getting things stable.
The other approach is we just do this, and it only includes, you know, Obi the Collector in Java, from the get-go. And we say, we're just not gonna touch these other languages until You know, they… they figure this stuff out.
But one way or the other, we want to have a way of kicking this off that isn't presuming… We're gonna get involved with y'all.
Michele Mancioppi 00:51:45 I'll get that information.
Ted Young 00:51:45 try to sort them out. Does that make sense?
Michele Mancioppi 00:51:48 Purely technical. I mean, Java is a special case where the artifact is a monolith.
But all the other languages.
Bastian Krol 00:51:57 Node.js also has… Node.js has a similar auto-instrumentation package that bundles instrumentations, and that could make that curation work. I'm not sure if they do, though.
Michele Mancioppi 00:52:09 But that is…
Bastian Krol 00:52:10 Python, I don't think we really have said. There are auto-instrumentation product is this pre-process executable that is a bit weird for the injector, and probably also for packaging, so I'm not sure how that fits into the packaging story. We might not want to use.
Michele Mancioppi 00:52:31 So, from the point of view of… let's take Node.js. Node.js has the auto-instrumentations package, and that… let's assume That it doesn't have enough curation.
About what is included, what is not.
That package is not required.
We can work around it.
Bastian Krol 00:52:53 But then we need to do all the curation, and we don't want to do that long-term, or even mid-term.
Michele Mancioppi 00:52:59 Oh, no.
Bastian Krol 00:52:59 And all of them.
Michele Mancioppi 00:53:01 Not long-term, but it would be a way to get off the ground.
Ted Young 00:53:06 Great.
Bastian Krol 00:53:07 I don't buy that, to be honest. I mean, it's not only for… let's take the concrete example of Node.js auto-transformation. It's not only the curation or selection of packages, it also does the heavy lifting of doing… The actual require in the middle and all that stuff, and that's what we want to use From the injector, and we don't want to rebuild that, or fork that, and if the packaging stuff includes the injector, and it uses that as a vehicle to instrument Node.js, and we need the auto-instrumentation Node.js package. We don't want to replicate all of that. It's not just a… List of packages.
Jack Berg 00:53:55 Yeah, those maintainers over in JavaScript have to do that curation, and they need to… they need to view that curation of making sure there are no breaking changes outside of major versions of the Node.js auto-instrumentation module. They need to… Feel that that's important, make sure that it's happening, and and I guess, like, like, it's our job, or maybe some combination of our and their jobs, to, like, sort of put a carrot in front of them, and be like, this is why you ought to do this. Like, you should view this as table stakes for publishing such an auto instrumentation module, is doing this curation activity.
Bastian Krol 00:54:38 Yeah, so the current version that we include, and that is the latest, is 0.72 something, so it's also probably not stable, so if we tell the Node.js folks that, they will probably say, yeah, we don't have a Stable version of that package yet, so that… basically gets around in circles a little bit, I guess, and they probably won't feel like Our story is… is a push to go stable, like, in… in a few weeks.
Realistically, yeah.
Jack Berg 00:55:10 So maybe we should gate it on, you know, only packaging things up that are stable right now, and actively open these conversations with these respective SIGs.
Like, encouraging them to own it, trying to articulate the importance of doing it, and, like, coming up with a timeline.
For… for when it can get done.
Ted Young 00:55:31 Right.
So, that stuff is what we were trying to put… firmly into Phase 2, mainly because we're just concerned that there's this logjam right now, where we're saying, hey, we want to start this system packaging SIG up that's going to require a lot of attention from all the maintainers to, like, grow together, and then we're getting just huge pushback from everybody, being like.
the… you know, that all these SIGs are at different places in their own timelines, the TC is at max capacity, So that sounds like… like, basically the thing that's been kind of blocking this from getting started. So, the… trying to thread the needle is sort of like… it feels to me like if we had something that worked, and had some way of including something, maybe it's just… Java and some things that already have met, you know, the requirements that we want. They already are packaging things up the way we want.
Or we have a way of, like, bundling together all the unstable stuff. But let's just focus on the first one.
We… getting something out there and saying, this is how it works.
It works with some things, and as part of our stability initiative, stable by default, so that we can graduate, we need to get every language added to it. It feels like if we build the infrastructure, if we build the trellis that everyone can hang their thing on.
that… unblocks us from being able to do the rest of the work. You know, put this up on the website as, like, a goal for each language, and start to motivate everyone to do it. Because if we do it the other way, it just feels like… It's just, like.
we're eternally blocked. So that… that's really, like, the goal of trying to separate this out. How can we get, like, something out there today, quickly, that… that… People can play with and understand what we're trying to do.
Because that's the other thing we see, right? As long as this is just, like, theoretical in words.
people are kind of grabbing at it in different ways, and will probably get a lot more interest from people if they can actually play with it. But it does sound like unstable versus stable is not the way to do it. Maybe it's just… we just start with Java, and maybe .NET is also in a similar place.
Ruby might also, weirdly be in a similar place, because I know they have a, you know, OpenTelemetry All package that they kind of use.
What?
What do you… you're making a face, Jack. What do you think about all that?
Jack Berg 00:58:23 Bye.
I think it's like a chicken and the egg problem, and you know… You know, you're talking about starting somewhere so that people get motivated to do this, but, like, if we have, packages for just, like, two things, and… because those are the only things that meet this criteria, then, like, it's not really something that you can get your hands on, because it's just a toy. Like, it's not… It's not complete until you get a critical mass of languages that have met this criteria that have these packages.
And so, like, somehow, someway, we have to motivate these language things to take this thing seriously, to take seriously the versioning and the curation of their auto instrumentation packages.
Ted Young 00:59:13 Right. But the thing is that most SIGs, like, Java's in a unique position, which is you have a SIG devoted to managing this, and the problem with other languages is we have SDK maintainers who have enough bandwidth to manage the SDKs.
But they don't feel like they have the bandwidth to manage all of Contrib, and they've said that repeatedly.
We could grow that, right? But there needs to be some kind of motivator for growing it.
But I do think if we've got, like, a couple languages, like, like Java and .NET, Obi, and the Collector.
as things you can install. Like, that to me feels like it's past… past being a toy at that point, right? Like, that at least matches what you can… What you can install in the operator today, for example.
Jack Berg 01:00:05 And the collector's not even 1.0.
Ted Young 01:00:07 Well… We need to get that thing to 1.0 as well. But this also gets into, like, me wondering, is there a way to make the packaging work You know, what if people do want to install the unstable stuff?
Jack Berg 01:00:26 Yeah, they, they, they have to… They have to… Yeah, and I don't know how to reconcile that with what Mikael said, and we're out of time, so maybe I should just hold my thoughts.
Ted Young 01:00:40 Okay. So it sounds like… it sounds like we still have this… this chicken-egg thing, but I really feel like if we can get something out there to people, and, like, something bootstrapped, it will help… pull the other SIGs in and get more end user involved, so…
Jack Berg 01:00:56 Yeah, and I'm not gonna… I'm not gonna block the packaging stage, because I think the… the sort of productive consensus thing that was coming out of last week's GCTC meeting, where Mikel attended, was like, something to the effect of, like, hey, if we reduce scope or work on a certain, like, subset of the original vision now, then we can make some progress and, like, also line up the prerequisites to do the follow-up steps, and I'm completely on board with that. So, I don't want to split hairs about how that, you know, takes place, but there's… there are lingering issues, and I think that's what we're swirling around here.
Ted Young 01:01:34 Yeah, well, it sounds like my unstable approach is a non-starter, so we gotta back up and go forwards again with maybe what you're proposing. It's like, we're just gonna start with a limited number of languages.
And use that as the structure to then help motivate the rest of the languages to… To… to get on board.
But part of it really is just a resourcing issue in those languages. It's, like, the SDK maintainers, I think, in Python is, like, a great example of a language where they're just like, we don't have the resources to build a whole bunch of stuff that we don't already have, at least not on a quick timeframe.
But we could use this as a motivator to maybe get companies to start contributing more resources, if it's, like, a clear goal they're trying to hit.
Jack Berg 01:02:21 I gate it. Like, if you want your AI shit taken care of, first solve, like, the, the, you know, the packaging issues.
Ted Young 01:02:27 I was trying to use the unstable flag as the gate, but it sounds like we need a different gate. Okay, we're out of time, but…
Jack Berg 01:02:35 Yep.
Ted Young 01:02:36 we'll keep this… I want to keep this pushed through, quickly, so I'll be poking you.
Michele Mancioppi 01:02:41 Well, that we sync again at some point this week, or what?
Ted Young 01:02:47 I'm going to… yeah, let's… we'll certainly be bringing this up in the GC meeting, and yeah, I will hit you up on Slack.
But I think it's, like, we need to come up, Michele, you and I just come up with what we want to propose to people as the next step. Asking people to propose to us, we gotta propose to them, I think, at this point.
Michele Mancioppi 01:03:12 You know, the, PSA, will not be available next week. I'll be at Google Next, and flying to and from.
So…
Ted Young 01:03:23 Yeah, GrafanaCon for a bunch of us on our side, so next week might be a wash, but… If we at least have a plan together this week for… for how to move forward, I think that would be good.
Michele Mancioppi 01:03:36 That's it.
Alright, final one point.
Bastian Krol 01:03:38 Cool, bud.
