SIG: SIG Injector
Date: 2026-07-09
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Bastian Krol** 01:23 Hey, hey.
**Nikola Grcevski @ Grafana / OpenTelemetry** 02:34 Hey, rested.
**Bastian Krol** 02:38 Hello.
So I'm not sure. Hi, Diego.
**Diego** 02:59 A…
**Bastian Krol** 03:01 A.
So I'm not sure if anyone else will join today, I think… Nikhil is out on a conference, Antoine said he's double booked, so… Let's see if anyone else joins.
And whether we have any topics to discuss.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:26 Check the agenda. There's nothing on it.
**Bastian Krol** 03:29 Yeah, nothing on the agenda, that's not… Nikola Grcevski @ Grafana / OpenTelemetry 03:33 We can just talk about the.
the football.
quarterfinals. I'm just joking.
**Bastian Krol** 03:42 This is not my favorite topic.
Diego, are you a football person.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:48 No, no.
**Diego** 03:50 Fortunately not.
**Bastian Krol** 03:52 Absolutely not.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:53 I'll just…
**Bastian Krol** 03:54 I didn't even follow the… Nikola Grcevski @ Grafana / OpenTelemetry 03:57 Oh.
**Diego** 03:59 Well… To be honest, This, workup… was organized by Mexico, Canada, and United States. Both of them got automatic spots.
Because… They are the hosts, right?
And Costa Rica is in the same federation as the three of them.
Oh. Which means Costa Rica didn't have its three toughest competitors in the qualifying process, and it still didn't manage to qualify.
So it was, kicked out of the tournament by… Teams that have absolutely no… tradition in place.
**Bastian Krol** 04:50 Okay.
Looks like you're frozen now.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:55 Ross, Diego.
**Diego** 04:56 Like Panama and IT. So think about Costa Rica.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:02 Yes.
Right, right.
Yeah, we're, we're here, but we, you're frozen for us.
**Diego** 05:13 Okay, what was the last thing you heard?
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:15 I heard something about Haiti and somebody else making it.
**Diego** 05:20 Yeah, what I'm trying to say is that Costa Rica never had it so easy and it still failed to qualify.
Okay.
**Bastian Krol** 05:29 Well, Germany is also already out, and I think that's not a… Nikola Grcevski @ Grafana / OpenTelemetry 05:33 Yeah, of course.
**Bastian Krol** 05:34 Than expected, but that's fine with me.
Okay, yeah, so, besides that… Is there anything injector related that we should have a talk about?
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:59 No, I haven't actually tried the new release, I will Try to see if I can… Update our image to use the new release, so… It's on my to do.
Okay.
**Bastian Krol** 06:10 And… Nikola Grcevski @ Grafana / OpenTelemetry 06:10 Yeah, to pick up those bug fixes, and I mean, the hotel environment renaming doesn't concern me, but…
**Bastian Krol** 06:18 Right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:19 That's what I… yeah.
**Bastian Krol** 06:22 Yeah, I already integrated the latest release, not in our released operator version, but at least in the main branch, and it… Passed all the tests, so I think it's good. But there was also… kind of… minor. I think there was one thing for that net included with double instrumentation, so… Right.
I, I have.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:47 I had one sort of like kind of thought that popped into my head, but I don't actually know if it's an issue or not. I thought maybe I could just bring it up.
So, with people moving to this declarative config.
us setting resource attributes through the environment variables on the process.
Do you know which one takes precedence? Is it the declarative config or the stuff that we pass?
That's good.
**Bastian Krol** 07:19 question.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:20 Because if they if it's if it's a declarative config, then it's fine, because then that's the source of truth. That's what the customer intended.
But But… If it's what we pass in, we may override it.
And as… and then the… and then we detect the application is instrumented. But the environment variable is already set.
**Bastian Krol** 07:48 It could even be that it's merged from both sources, like, I know the Go SDK, I think, merges from environment.
**Nikola Grcevski @ Grafana / OpenTelemetry** 07:55 Therapist, okay.
**Bastian Krol** 07:56 other detectors, so that could also… Okay.
**be, so that is probably… it might even also be different per runtime and per SDK, that would… Nikola Grcevski @ Grafana / OpenTelemetry** 08:07 Yep.
**Bastian Krol** 08:08 Surprised me a lot.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:13 Jack is a king of that. I'll ask him. He's away this week on vacation, but…
**Bastian Krol** 08:17 Yeah, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:19 Maybe I'll ping Jack when he's back home Bugging on.
Okay, sure.
**Bastian Krol** 08:23 Yeah, I would expect over time we would need to build more dedicated support for declarative config also in the injector probably.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:34 Yeah, somehow, yeah.
**Bastian Krol** 08:36 Yep.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:40 Yeah.
**Bastian Krol** 08:41 I don't know exactly how that's… Would look like… Specifically… Because, I mean, we… I think, so… Nikhila talked quite a bit about declarative config within the context of packaging, and that also packages the injector then.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:58 Mmh.
**Bastian Krol** 08:59 With this, I think, I'm setting auto config, but I'm not sure exactly how it all plays together.
The end.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:08 Right.
I think we're ways… Away from that, but… once the SDKs start using it, or people start adopting it, will… will become a topic, I think.
**Bastian Krol** 09:22 Yep.
I saw this morning that Antoine is working on creating binaries for two additional architectures, CPU architectures. I think it's 396, 398.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:39 390? IBM? Really?
**Bastian Krol** 09:41 Yeah, yeah, yeah, exactly that one.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:43 Yeah.
**Bastian Krol** 09:44 But it's currently a draft.
PR, yes.
Yeah, and PPC, PPC 64, Little Indian.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:56 I see the nice.
**Bastian Krol** 09:58 Yeah, no, it… We might need… to use cross-compilation, I guess, for that, if we don't… because I think we use dedicated CPU architecture runners for the two architectures that we support right now, and that's probably not sustainable. If we want more CPU architectures, having a dedicated runner for each of them might not be an option, I don't know. So we might need to look into cross-compilation there, but I think.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:31 Yeah. Okay.
**Bastian Krol** 10:32 They did, so that should… potentially work.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:38 I mean, PPC will be fine, because I think QEMU supports it, but I… Unless things have changed, I mean, I haven't been… paying attention to the mainframe space, but I know in the past IBM actively went after each person trying to replicate an emulator for 390.
**Bastian Krol** 10:57 Because, Nikola Grcevski @ Grafana / OpenTelemetry 10:58 They, I mean… I I remember I worked at Ibm so full disclosure. I.
**Bastian Krol** 11:03 I would.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:04 I've been at Ivm for 13 years in the compiler department, and.
**Bastian Krol** 11:08 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:08 At some point there was a company that was.
founded by Intel.
that.
built a 390 emulator that ran better than the 390 hardware on x86. So I think IBM just bought the company.
**Bastian Krol** 11:29 Okay, okay, interesting.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:31 It was quite an interesting technology they built, because it had… Okay.
a trace compiler that was optimizing under the covers. It would take the mainframe instructions and convert them to machine code. It was quite neat.
**Bastian Krol** 11:47 Good stuff.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:48 Yeah, very cool. But I don't think that's available. I think if you pay them enough money, you'll get it as a development environment. So you can kind of.
Run locally.
before the point on mainframe. But.
**Bastian Krol** 12:01 Yeah, probably not available as a GitHub action right now.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:05 Doubt it unless things have changed. Maybe Ibm is gonna step. We have to. I don't know what the world looks like now in that space.
**Bastian Krol** 12:12 Yeah, you need that. Yeah, I would, I would.
**if we can avoid Kimu, that would be better, because it's hella slow on GitHub Actions, but, I mean, also, we only run builds every… every once in a while, so… even if we need to use Kimu, that's… that's also fine, I guess. But we will see how… I guess Antoine will work on it a bit more, and then we will… Nikola Grcevski @ Grafana / OpenTelemetry** 12:35 Yeah, maybe on certain PRs, maybe we can create a workflow that you can just tag the PR, run all… jobs and then.
**Bastian Krol** 12:44 No.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:45 You can request it.
**Bastian Krol** 12:49 Right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:49 on demand, or something like that to run. We do that in Ebpf, because for us, Kimu is It's quite essential because we need to try different kernels.
**Bastian Krol** 13:00 Yep.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:01 And so… but we don't run all kernels for all PRs. If it's changing some user space code, just the default, and then… but if it's changing BPF code, then we run… on bulk kernels.
**Bastian Krol** 13:15 I mean, I wouldn't expect… really any differences whatsoever with respect to CPU architectures. I don't think we ever had a bug that was only specific to one CPU architecture injector. So, I mean, why would it?
It's the compiler works and then the injector code works irrespective on all architectures.
Okay.
Cool, okay.
There's nothing else… I guess we can… Call it a day for today.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:49 Sounds good.
**Bastian Krol** 13:51 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:54 All right.
**Bastian Krol** 13:55 then… Nikola Grcevski @ Grafana / OpenTelemetry 13:56 See y'.
**Bastian Krol** 13:57 So.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:57 Next time. Bye.
