SIG: Profiling WG
Date: 2026-06-25
Duration: 43 minutes
============================================================

## Zoom Recording Transcript

**Nayef Ghattas** 02:10 Hello.
**Scott Gerring** 02:17 Hello?
Glorian, I heard there's no power in Zurich, or there was a big power outage or something.
**Florian Lehner** 02:35 Really?
Amazing.
**Scott Gerring** 02:37 It was in 20 minutes.
**Florian Lehner** 02:39 Okay, I'm following 20 minutes, but so the fan is running all day, so… Yeah, I'm happy I'm not affected.
Yeah, funnel of living in Switzerland, there is no AC, you just have fans, we just have fans.
**Scott Gerring** 03:01 Yeah, there's a big debate going on at the moment about whether or not maybe you shouldn't have to go to the commander to get a permission to install air conditioners if it's going to be 36 degrees every day for a month, but… Things move slowly.
**Florian Lehner** 03:19 Yeah, sometimes…
**Nayef Ghattas** 03:20 Sorry, sorry, go ahead.
**Florian Lehner** 03:21 Please go on.
**Nayef Ghattas** 03:23 No, I was going to ask you, you're going to have 36 degrees for a month?
**Scott Gerring** 03:27 I think I'm exaggerating a bit, but I think it's been over 2 weeks now,
**Florian Lehner** 03:32 Yeah… Yeah, I think the problem is also that, during night, it's no longer cooling down.
**Nayef Ghattas** 03:38 Yeah.
**Florian Lehner** 03:39 That's very 6 degree, on a peak, or even 40 is fine if it can cool down during night, but… The cooling down during night is missing, I think.
**Scott Gerring** 03:50 And it's so much… it's really humid here as well. Like, at home, it's hot, but it's dry, and it makes such a difference when it's humid at the same time.
**Florian Lehner** 04:00 Yeah.
**Christos Kalkanis** 04:41 Okay, folks.
Scott, are you based in Europe? I see the farm running.
**Scott Gerring** 04:47 Very perceptive.
**Christos Kalkanis** 04:49 Yeah.
**Scott Gerring** 04:50 I'm also in Switzerland.
**Christos Kalkanis** 04:53 My girlfriend is in the Netherlands, and they're having, like, 35 degrees Celsius. It's insane, you know how…
**Scott Gerring** 04:59 Yeah, the continent isn't built for this sort of hate.
I need two fans, at least.
**Nayef Ghattas** 05:08 It's actually 42 today in Paris.
**Christos Kalkanis** 05:12 Wow.
**Scott Gerring** 05:16 You can swim in the… you can swim in the river now, though, can't you?
**Nayef Ghattas** 05:21 Oh yeah, yeah, in theory.
**Scott Gerring** 05:23 In theory.
I think Felix is probably not coming, right?
Who runs the meeting when Felix isn't around?
**Christos Kalkanis** 07:01 I think we take turns, We've all tried it. I tried it once, twice, I think, Anybody wants to volunteer, it's not easy.
going after… Felix is really good at it.
**Scott Gerring** 07:17 I've not come enough to run the meeting yet.
**Christos Kalkanis** 07:24 I'm just going through the agenda, because I missed last, the last, SIG, I was in Spain.
And I was out last week with a horrible flu, so I'm not quite catching up to do here.
**Florian Lehner** 07:41 Yeah, I can… I can volunteer if everyone is happy with this.
Then I would just start. We're already 7 minutes in.
For the first topic, that is also assigned to Felix and myself, this will be just, I would say, information for the SIC. We are good to go with the key value and unit, attribute in the protocol. There will be no changes to key value, applied to all, to all protocols, NOCs, metrics, and traces.
This was, the decision from the… from the maintainer's SIG meeting. So, we did get a green light, so this is now off of our, chest, basically, or we don't have to work any longer on this, and we got… just got green light, and that's why the issue on the Proto, that was opened by, That was opened by… I'm repeated now.
**Christos Kalkanis** 08:44 I've gone, I think.
Bogdan? Yeah.
**Florian Lehner** 08:47 Yeah, that's why the issue, that was opened by Bogdan, is now closed. Yeah, after the meeting, I will close, move this as to done.
If there are no comments left on this, I will continue.
So far.
**Christos Kalkanis** 09:04 This means that the other… the design document that Felix and you worked on is what we're going with, right?
**Florian Lehner** 09:11 Yeah, Yes and no. We keep key value and unit, and how we, use key value and unit is on our side. So, unit is not specified at all, so it can be arbitrary and just be something like, is used in the… PTROF by Google, but there's nothing we need to follow immediately.
The documents Felix and I wrote are really like a replacement for key, value, and unit. It would allow to adapt, the existing structures, but this is no longer needed.
Hope this helps.
**Christos Kalkanis** 09:56 Okay.
**Florian Lehner** 09:58 Next on the agenda is Alexei. Alexei, do you want to give an update?
**Alexey A** 10:06 One second…
**Florian Lehner** 10:09 The duplicate, and then orphans check on the conformance checker.
I did some…
**Alexey A** 10:16 I haven't worked on this, I saw that you are slowly churning on this, so I was… I don't know, like, maybe, like, should we pre-assign it to you, or… At least for… at least for the… at least for the duplicates check, We can… we can leave Orphan check for me.
**Florian Lehner** 10:40 Yeah, we can split it, it's fine.
**Alexey A** 10:43 Okay, yeah, sounds good.
And, I also com- I left some comments on your, on the… On the duplicates.
PR for mapping. I think that.
**Florian Lehner** 11:01 There was a bit of… Yeah.
**Alexey A** 11:02 those.
**Florian Lehner** 11:02 I saw some sort of notification, but we had some interesting days, these days at Elastic, so didn't come to these notifications yet.
**Alexey A** 11:10 Sorry. Okay.
**Florian Lehner** 11:13 Then, moving on, next step was, clarify profile period type and period semantics, there was a discussion, and we have.
**Alexey A** 11:25 Yeah, I think there was a discussion, and I think Felix wanted to kind of, like, read this a bit more and think.
Because I have that PR, but I think it's… there's a bigger discussion about the shape of, like, how to connect the… The, this, basically, period type and the shape of samples.
**Florian Lehner** 11:47 Yep.
**Alexey A** 11:48 We had this discussion, last… Last week.
**Florian Lehner** 11:55 I don't know.
**Alexey A** 11:55 No, maybe I will… I will maybe write a short doc, just to kind of, like, summarize the… where we are and the options, because I think maybe it makes sense to make this a bit more structured.
**Florian Lehner** 12:10 I just see that we, that the PR already has 3, free approvals, and we could merge it.
But, and I don't see any… And that you just questioned here,
**Alexey A** 12:30 Yeah, let me see, like, what… is there anything…
**Christos Kalkanis** 12:34 I have… I opened… I have a small comment there. Alexi, maybe you can take a look. It's mostly about standardizing the names.
**Alexey A** 12:43 Yeah, I actually addressed that one, I think.
Or I didn't respond, or… Yeah, because I thought… I thought I made the change.
**Florian Lehner** 13:05 so I don't see any, any… open task for Felix on this… Otherwise, I would just recommend that we… ask for merging this PR if, if the latest changes are, applied. Does that sound good?
**Alexey A** 13:29 I'll take a look at, I thought I addressed, I thought I'd just comment about the underscores, but… For some reason, I… I'll… I'll… let me take another look offline. I, I want to.
**Florian Lehner** 13:56 Yeah, Mexico.
**Alexey A** 13:57 I want to address that comment, and I also want to make sure, like, that nothing in the text I added contradicts the discussion. Like, if this is an improvement anyway, we should just merge it.
But if there's… if there's anything that is kind of contradicts the discussion we had, then… Either we should not merge it, or I should make it smaller. Yeah, I'll take another look.
**Florian Lehner** 14:20 Okay, cool. Then we keep it above that?
And moving on, naive, open GitHub issue on including OTLP version and payloads.
**Nayef Ghattas** 14:31 Yeah, I took that info from Felix this week.
So… I think the current status is that there was a sort of rough… we opened an issue on the SIG profiling repo a couple months ago. There was soft consensus from everyone that, we should probably include the version as HTTP header or gRPC metadata, for emerging signals like profiling, so that we can more easily make the switch.
Between alpha and beta, especially that we know.
**Florian Lehner** 15:10 Perfectly.
**Nayef Ghattas** 15:10 Going to have breaking changes and beta.
So this would allow the collector, for example, to drop alpha profiles, if it only supports better, or it could also allow vendors to, to support parsing multiple versions if needed. I think we got feedback from Tigran on this to say that we wouldn't want to add this for all signals, but only for images.
**Florian Lehner** 15:35 jump on.
**Nayef Ghattas** 15:36 So if there's still, consensus on this, in the profiling SIG, I think the next step would be to open an issue in… Probably OpenTelemetry Proto and bring it up to the maintainers in the specification SIG.
To see what's the… Thinking on this, but yeah.
So that's what I was, planning to do next.
**Christos Kalkanis** 16:03 Sorry, naive, so Tigrant proposed that we do this for all emerging signals, but just starting with profiling isn't, good enough. Why can't we just start with profiling? Like, I'm trying to…
**Nayef Ghattas** 16:14 Sorry, I mean, he said that he doesn't want to do this for stable signals.
**Christos Kalkanis** 16:18 Okay.
**Nayef Ghattas** 16:19 Like, to say… In general, when a signal is emerging, let's do this.
**Christos Kalkanis** 16:26 Okay. Just trying to reduce the scope, because… maybe we don't have to propose something that's applicable to any other signal than profiling for now, right? Maybe we can start with something that's just for us.
**Nayef Ghattas** 16:38 Yeah.
**Christos Kalkanis** 16:38 I think we'll have an easier way of getting it through, maybe it's gonna happen faster.
**Nayef Ghattas** 16:43 I think his feedback was that he didn't want to make a special case for profiling.
But I can… I can bring that up again in the specifications segment meeting.
**Christos Kalkanis** 16:55 Okay.
**Florian Lehner** 17:02 Okay, if there are no further… comments on this topic, I would move on.
Christos, the next one's up to you.
**Christos Kalkanis** 17:16 Yeah, so this still needs one approval from NTC members, Yeah, I don't know, I think people are either too busy, Because I keep asking.
So either Josh needs to take a look and approve it, or someone else on DC.
And Tigraner is asking me also need to fix some merge conflicts, so I'll do that today, and, keep pushing.
**Florian Lehner** 17:40 Yeah, I think we might need to bring this to the specification sake.
Otherwise it will not trap their…
**Christos Kalkanis** 17:48 Yeah, I mean, I mentioned this to all of them, I joined your Slack channel, right, so… if that's the next step, then I can also join, the meeting.
**Nayef Ghattas** 18:03 It's sort of tangential, but related. I thought that Josh was going to propose that we have, like, sort of a permanent TC member that joins all the profiling SIG meetings, and that would help with those sort of things. I don't know exactly where that…
**Florian Lehner** 18:21 Yes, yes, Tigran is the appointed person for us, yeah, but, with… holidays at the moment, I'm not sure if Tigran is at the moment around, so I might not be able to join every time.
But yeah, it is not charged for us to contact person as TC is Tiger.
**Christos Kalkanis** 18:46 Okay, so let me, like, I'll resolve the merge conflicts today, so then this is measurable as is, and then I'll reach out to Tigran, and then the entire ITC as well.
hopefully we have this deadline at the next week, because it's been a long time.
And that's also the last one, right? All the other ones are the MERS.
**Florian Lehner** 19:14 Okay, moving on.
I think there is no progress, Alexei, with the older hotel profiles.
Or Profiles or tab.
As it's still blocked by the… by the PR we just discussed, am I right?
**Alexey A** 19:35 I think… So… yes.
**Florian Lehner** 19:40 Okay, so there is no progress, and if there is no comment, I would continue to move on.
Evo and Scott, update on the Fred Contact Stone tab.
**Scott Gerring** 19:50 Yeah, it's looking pretty good. We have 3 of the, I gather, 4 serious approvals that we need. We've added a bunch of extra detail to clarify some stuff that was kind of implicit, I think, in the minds of everyone that we've been talking about this with.
is now in the spec, so about why we're doing the custom attributes, and what we expect to go in there, and no, it's not the entire context of the span, that sort of stuff.
It looks like we're probably chasing a review from Josh, and then hopefully that's that. But if anybody else feels like going through and, picking out anything else that's popped up that seems wrong, more than welcome.
I'll be excited to merge this. Loading that PR is like a load test for my browser.
**Florian Lehner** 20:34 Yeah, and it's not the number of line, change lines.
Okay, cool. Thanks for the great work. This is essential for moving on, I think, especially when we want to correlate profiles with other information like traces.
**Scott Gerring** 20:54 It would be really cool when it works.
**Florian Lehner** 20:55 Yeah.
Okay, then this brings us already to the end of the review action items.
And we are on the first agenda item. Yeah, I wanted to ask, so, wanted to ask if we want to have something merged in Proto.
Before I ask for a release of Proto. The release of Proto is also what I will then include.
the process context. So, the process context, currently lives in Auto Profiles, and this would allow us to move it out of eBPF Profiler and have it in the respective Go part, and also released as part of the rest of the profile files. So, this is not there yet.
And… Looking at our open PRs… We have the profiles at Better Documentation.
I'm not sure if you want to move already on and… Continue with this… PR… I think it will be a breaking change, if I remember correctly.
Yes, it will be a braking change. No, it will not, reserved.
**Jonathan Halliday (IBM)** 22:33 I regarded it as breaking, I'm not 100% sure it is.
I don't feel like people are asking for that right now.
we're gonna have to break things at some point, but I'm inclined to do it at the point where we change To be to release.
So, I'm… I'm not in a hurry to merge that one.
**Florian Lehner** 22:56 Okay, then let's keep as is.
**Jonathan Halliday (IBM)** 23:00 I think, thus far, all the changes are documentation-related, aren't they? So, this… this release, if it goes out, will not actually change the… productive structures at all.
It'll just add, not the new one.
**Florian Lehner** 23:22 Yeah, I think this is… Yeah, we have to change this now.
Okay, then, as it's just documentation, I think we can just merge it. I will merge it after the Cold?
Transported on my list.
Okay, then, yeah, you're right, Alex.
Just merge it, and especially as it's just a documentation, it should be a low-risk change.
Okay, then I will ask for a release, to get… us forward. I think this would also, simplify the work on the threat context, from… for Ivu and Scott.
And also, from… around, indication if something is instrumented by Nimrod from CoreLogix, there's also, a PR that, touches process context, so I think this could help, bringing these two, Two approaches, forward.
Okay.
Dan, next up is awesome. Sorry?
**Alexey A** 24:53 Is there a standard cadence for Hotel Proto, or it's pretty much usually by request?
**Florian Lehner** 24:59 by request.
**Alexey A** 25:01 Okay.
**Florian Lehner** 25:01 Yeah, there's no cadence.
That's why I wanted to open issue and ask for, for a release.
as there was some change in the responsibility for the protocol, this is now a little bit different, I would say. It's not longer, no longer just TC that is doing this. I think in the past, we asked, Tigran or just to cut a release.
And, this is no longer the case, I think.
Nope.
We will figure out, I would say.
If there are no more comments on this, I would continue.
Okay, I'm speaking a lot today, prof check on the signals. yeah, as Alexei mentioned, already, I started… To work on some improvements.
And if people are fine with the checks, I'm happy to merge them.
Yeah, the first one is to make sure that the shape of the values and timestamps is consistent throughout all samples.
There was a gap.
It should be closed.
One thing… maybe if this is fine as a follow-up, Alexei, ignore some… so changing… it would be a breaking change to rename check, check Sample timestamp shape to ignore sample timestamp check.
But it should be fine as a follow-up if this works for you.
**Alexey A** 26:49 Yes. Do you know where… do you know if it's, referenced by anyone, anywhere? I agree it's a breaking change, I'm just curious, like, how many clients will it break, if we know?
**Florian Lehner** 27:00 I know at least eBPF Profiler, I think we have it in a test, then… AutoContripProf.
But I'm the code owner there, so… It's fine.
And other than this, I don't… any public references on this… on this yet.
**Alexey A** 27:26 Yeah, I think it should be… it should have been inverted, like, maybe… Maybe when we did it in the first place, maybe, like, it seemed nice that the names would be consistent, but… I think in reality, it's better when the default behavior makes sense, and… and the… and the shape of samples is actually, like, it's… it's… it's mandated, it's not optional. It's the duplicates checks and, like, and orphans references checks that are… we say, like, it should. It's more, like, optional, so… so, yeah, I think it should be on by default.
**Florian Lehner** 28:02 Yeah, makes sense to me, make perfect sense to me.
And if there are no comments on this PR, I just open for the view the other one.
So this is quite new. So, at reference check, this didn't exist before that.
So it adds a new option, check reference, check.
and removes the to-do. I decided to go with a dedicated function and not have it in the existing functions, because I didn't want to keep track, of the… if something is referenced or not.
in conformance Checker, so the only option I did see was extending the conformance Checker struct.
But I didn't want to add in these things, that's why I went with a dedicated function, even if this means we are going twice through the protocol. So that's… That's the overhead.
**Alexey A** 29:05 Yeah, I think it… I think it makes… I think it makes sense. Otherwise, otherwise it will end up, like, very scattered, and it's, it's… yeah, I think I agree that it's easier to… even if it's a bit of, like, duplication and extra loops, at least it's easier to inspect that we are handling everything.
**Florian Lehner** 29:24 Yeah, this and, as conformance checker is not running on every production… on production rules, I'd assume, I think it's fine if… If we go the second time over the protocol for these checks.
Yeah, but, if you have, if you have time, feedback is welcomed.
If you didn't find any time yet.
Okay, and this brings us, I would say, to the last topic for today. Scott, we are starting to look at heat profiling.
**Scott Gerring** 30:06 Yeah.
**Florian Lehner** 30:06 or something.
**Scott Gerring** 30:08 Yeah, so we've got a bit of time to spend on this at Datadog at the moment. The idea is pretty much what's discussed on the issue on the repository, that we emit a USDT in applications.
For allocations and free behind a sampling path, so that you don't hook every single allocation.
I think… A good idea would be to kind of prove it out a bit on our side, and then raise a design proposal against the repository so everyone can weigh in.
I'm interested in whether or not that sounds sensible to you all. And Florian, I also know that you've done a bit of work on a branch looking at extending the profiler for different event sources that seems like it should probably be a big… a good thing to maybe build on top of.
Or at the very least, discuss with you.
**Florian Lehner** 30:54 Yeah, as you're discussing about, you discussed it somewhere in an issue, do you have a link to the issue?
**Scott Gerring** 31:02 Not off the top of my head, but I can find it quite quickly. There's an issue if you chuck in USTT or heap profile or memory profiling, but I can also do that.
**Florian Lehner** 31:12 I don't find anything about USD on eBPF profile.
**Scott Gerring** 31:17 Bear with me.
I'm struggling to find the, It's late in the day for me to be using Google.
**Florian Lehner** 31:36 We need more assistance to keep these issues up for us.
**Alexey A** 31:42 This is… this is for what language? You're profiling?
**Scott Gerring** 31:47 We would hope to be able to do it for any language that can emit USDTs, so, sample points in the code, but we're trying to dog food it internally.
for native code, and for native code behind Python applications, because those are both cases where we have poor visibility into heap usage.
**Christos Kalkanis** 32:07 So, Scott, does this mean… because UFDs have to be predefined, right? So this means that the developer has to explicitly insert the hook points, create the points that you will attach.
**Scott Gerring** 32:18 So there's two ways we're thinking of doing it. The first will be like that, that the developer inserts them, or rather the developer uses some library that makes it easy to insert them.
The other way is that we do some runtime trickery. I don't think that, profile aside.
should care about this too much, I guess, but, like, we have, the Datadog DDProf, the native profiler, it does got table rewriting when it is injected into a process to hook dynamically linked allocators, so it can intercept them without you doing it beforehand, as long as you don't statically link things.
So we want to support that as well, because it makes it work and usable in, kind of, like, dynamic runtime contexts like Python, but it's a bit more… Complicated than when people just add the sampling bar themselves.
**Christos Kalkanis** 33:05 Yeah, so for the second is what we prototyped years ago inside Elastic, and one issue we ran into there is that you really need a way to sample allocations and not just trigger a contact switch on every call, depending on the granularity of the course that you're booking. Like, for example, with the JVM, You could go hook at low granularity, like individual allocations, right, which is going to give you a tremendous amount of context switches, or you can find a function call that basically sets up in your slab or an arena at the JVM, if I believe, if I remember correctly, had one of those, and those are triggered less frequently, right? So then you can hook that, but still.
you do need a way to, yeah, ideally sample that call, right? So maybe you actually do trigger the contact switch, where you go into the kernel and grab The stack trace, run once every 100.
calls, or 110 calls, or whatever. And the way we… We're trying to do it back then, was via a trampoline.
which, again, was hockey, you know, like, coming from the security space, I'm sure, you know, it's essentially… what, you know, malware does a lot of the time. So, a lot of error alerts flying.
**Scott Gerring** 34:21 Yeah.
It seems like there's a common pattern in some of the allocators, like JEMALIC and TCMalloc, where you draw from a Poisson distribution over bytes allocated with some average sample size, like every 512 bytes seems to be a classic one.
You sample, basically, or if you have really big allocations, you omit multiple samples.
And then the way we've got it for our DDProf thing is basically doing that with the trampoline that you do around the GOT table.
Manipulation, which, as you say, is a bit terrifying, but… Yeah, in the simpler case where a user actively opts into it, or even more optimally, uses an allocator that has an observability hook, like JEMALIC, where you can just plug in and say, when this fires, then… emit a sample, it's… it's pretty robust, I think. And then there'll be a bunch of discussion about we're looking at native languages primarily, but as you say for Java, like, maybe there's just a better place to hook it as the profiler that gives you the visibility you need without having to go and manipulate the runtime or the user's application.
But if you… is this something that you folks wrote up, or published, or have any public code from? Because I'd love to have a bit of a look.
**Christos Kalkanis** 35:33 We have an internal prototype, I don't think we've ever published it. Maybe we could.
**Alexey A** 35:40 No.
**Scott Gerring** 35:40 In terms of working with a project, does it sound sensible to kind of, like, pocket out on our side and then raise a PR with a design proposal?
**Christos Kalkanis** 35:50 Yeah, it sounds good to me. I mean, at least the first part seems to be well-scoped, and it doesn't, rely on anything that is hacky, right? Because it's, like, if you're using a library that inserts those points for you, or you as a developer decide where you would take the hits, then that's perfectly fine.
**Scott Gerring** 36:09 Yeah, cool. And Florian, is it okay if I hassle you a bit in the channel about your PR as I pick over it to see what we might be able to use there?
**Florian Lehner** 36:18 You mean the custom probes PR?
**Scott Gerring** 36:20 Yep.
**Florian Lehner** 36:22 Yes, I would not recommend, building on the RFC. The RFC is just like how this can work, I… I'm volunteering, so I have, I split down the RFC into intermediate steps.
At the moment, I'm blocked by the reporter API, so, if we bring these custom, custom probes, like heap profiling, then we need some kind of not hard-coding everything. At the moment, I'm… I'm blocked with this PR, so 1461.
Once this is done, remove of hard-coded origin IDs should be straightforward, I don't expect too much on this.
This will be maybe a little bit of a discussion, but should be also possible, and the last one are just an… making… moving existing code from Package Tracer to the custom props.
So this should not be a big, topic for discussion, but yeah, at the moment, I'm… I'm kind of continue because of this.
Yeah.
**Scott Gerring** 37:30 Okay. I think there's probably going to be, realistically, a bit of a lead time until we get to the point with the heat profiling. We want to do it really seriously, and maybe we can combine forces a bit here.
**Florian Lehner** 37:40 Yeah, makes total sense, makes total sense. So, I think, in one of the last, PR, not in the last PRs, in one of the last SIG meetings, GPU profiling was also, discussed.
And I know that CoreLogix did some experiments with it and want to bring it in.
Polarsignals mentioned something, that they have something, and they probably want to bring it in.
So, yeah, at the moment, I would say… Yeah, let's enable custom probes first.
Because it allows us to… We work on these kinds of things, but… This is the tricky part, I would say.
Alexa?
**Alexey A** 38:27 I added a link that Google's TC Malloc allocator has an implementation of HIP Profiler, but I guess this is less interesting to you because it's, like.
just yet another sampling implementation, which is… there is, like, a number of, and you're building something more generic, so anyway, I just wanted to kind of… maybe in the proposal that you prepare, maybe it's worth at least mentioning how, kind of, like, hotel heap profiling ecosystem will interoperate with existing profiling samplers, like, for example, Go also has a heap profiler, and I… so I assume, like, for Go, we wouldn't… we wouldn't need to have a solution, and we would just plug in what's already there. Just, I think, like, it's… it's an interesting topic.
**Scott Gerring** 39:17 Yeah, it's super interesting. It's also interesting because I think both the TC Malloc and JEMALIC sampling infrastructure in them takes a very similar view on how you sample across the distribution, which is helpful, because You can also provide, optimally, something that plugs into their existing extensibility mechanism.
Rather than having to wrap the allocator again, which is cool, because they already have these structures off to the side they need to write to, to read to, to sample, so you don't add costs there. So I think, optimally, the way we would do it from, like, an application perspective would be kind of like this generic fallback where You have an allocator and you wrap it without any insight into the allocator, like black box style.
But if you find JE Malik, or TC Mallik, or another one that has an existing mechanism, you use that instead to avoid the cost.
Yeah. It's such a rabbit hole, it's great.
**Alexey A** 40:08 Yes, and I think, like, the sampling approaches, I think, at least, like, like, ATARS I saw, they seem to kind of, like, agree that, like, Poisson sampling in the number of bytes is what… I think both GMLIC and TCMalloc do.
**Scott Gerring** 40:23 Yeah, and then maybe you just need to also, in the face of different samplers, making different decisions about… I mean, you always return the probability of the sample, so it's fine even if they make different decisions there, actually.
But yeah.
**Alexey A** 40:36 But…
**Scott Gerring** 40:36 We'll try and do a bit of… a bit of work in the open here, and do some design proposals once it's got a bit more concrete, so we can all tear it to shreds and see what makes sense.
**Alexey A** 40:45 Yeah, but there are interesting new answers. I remember if… I don't remember if it was Heap sampler, or was it some other sampler we had, but… couple times we had this, bug, I think we even documented somewhere in, like, guidelines or, like, tips for building a profiler, that you need to be careful about how you sample the very first event, because I think, like, in a couple of profilers, it was… the sampler was set up in a way that, like, the first occurrence always is always sampled, and instead you need to, kind of, like, you need to set your sampler early enough, so… because otherwise you might… inflate, like, a static, like, the very first allocation that happens in the program, which can be deterministic in some cases, and then suddenly, like, it looks like it's significant, but But it's not, like, more significant than other things.
**Scott Gerring** 41:39 Yeah, anything with statistics always requires more thought, for me at least. I think it should, initially. Sorry, Naya, if you had your hand raised.
**Nayef Ghattas** 41:50 Yeah, sorry, I think I lowered it because you said what I was going to say.
I was maybe going to just add a small thing, that since we're focusing first on native languages, I think that can still help fork some of the blind spots for, for Go, for example, because when you use CGO, for libraries like ZSTD or Kafka, you end up introducing a blind spot in terms of memory profiling.
So having native… having tracking for what's happening on the native side would still help.
**Florian Lehner** 42:26 Yeah, sounds great. Thanks for the great work. I'm just looking forward to To see the design and what you're doing.
**Scott Gerring** 42:34 I'm excited.
**Florian Lehner** 42:42 Are there further comments? Otherwise… There's no topic left.
But this is also fine, I think everyone is fighting the heat, otherwise, and we can just… everyone craps up.
Cold water and gets hydrated.
**Scott Gerring** 43:07 I'm gonna go shower off in the garden with a hose.
**Florian Lehner** 43:12 Word is sweet.
**Scott Gerring** 43:17 See you all next time.
**Nayef Ghattas** 43:19 Thanks a lot.
**Christos Kalkanis** 43:21 Alright, take care.
**Florian Lehner** 43:22 Thank you.
