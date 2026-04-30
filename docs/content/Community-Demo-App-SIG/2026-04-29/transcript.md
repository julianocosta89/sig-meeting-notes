SIG: Community Demo App SIG
Date: 2026-04-29
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/h28_spCyknbfIUuIyU4mAMZSijLSfOEUakRfdAdEyLQ8_DHgW475QYFXhAlNX4OM.oGjegcRFwqOvPY1t
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 00:08 Hello, hello!
**Pierre Tessier** 00:24 Alright, are you there?
**Juliano Costa | Datadog** 00:26 I am here.
How are you doing?
**Pierre Tessier** 00:31 I'm getting busy.
I like it.
**Juliano Costa | Datadog** 00:38 Okay?
**Pierre Tessier** 00:40 It's good. It's good. Yeah. I have a lot of, activity. This is…
**Juliano Costa | Datadog** 00:46 Yeah, this is good.
**Pierre Tessier** 00:47 So…
**Juliano Costa | Datadog** 00:53 I…
**Pierre Tessier** 00:55 Go ahead.
**Juliano Costa | Datadog** 00:56 Yes. No, no, go ahead.
**Pierre Tessier** 00:58 This is, you know, my comment there, now I'm more dependent upon PRs.
we really need a good testing harness out there for this, and I really need to write this initial draft, PR, or something.
So we can, Yeah. I've got an agent, local agent that I use to test them all, that actually runs the demo for every single one of them, runs through the actions, like, it just takes… time. You know, I kick it off, and I say, go run this for all the Dependabot PRs. And, like, 4 hours later, they'll come back, and they'll give me a summary of every single thing that I did.
Why I passed and failed each one of them.
And, and if I have questions, I can move on from there, so…
**Juliano Costa | Datadog** 01:47 Does it also… I don't know.
Does it provide, like, feedback? Like, hey, this one failed because of this, here's a fix. Okay.
**Pierre Tessier** 01:57 Yes. So, right now, the, there is, depending on PR, I think it's 18, 3218 or 33.18, or something like that. I didn't merge yesterday, because it fails. It actually breaks, the OpenAI span generation. There's been a change in the… upstream libraries.
function signature, right, called RAP2, and it says, hey, maybe you should let the maintainers of this know, like, like, you want me to write the PR for the upstream repo and everything? I'm like, slow down. Yes, I need to investigate some more, but fantastic. Thank you for finding that. So that was yesterday.
**Juliano Costa | Datadog** 02:34 Is that… is that in Java? I saw that in Python.
**Pierre Tessier** 02:41 I think it's a Python one, yes.
**Juliano Costa | Datadog** 02:42 Okay, okay.
**Pierre Tessier** 02:42 Python one.
**Juliano Costa | Datadog** 02:43 Yeah, yeah, I found that exact same issue on a project that I have, and it was yesterday, I think, where… So, what I did was actually pinning the wrapped to, to avoid,
**Pierre Tessier** 03:02 Yeah, right.
**Juliano Costa | Datadog** 03:03 Major, major.
**Pierre Tessier** 03:04 That was one of its options. It gave me a bunch of options. I try to look at what's the proper long-term option, because that's where I want to go. And what I may do is, depending on what it is, I may say, let's do this or the other. For example, I haven't tested, the, the Android stuff, but same thing for the Android stuff. It said, hey, this is the deal, and I'm like, okay, this is way bigger than I want to entertain ourselves. Yes, we could pin it.
But… What's the long-term fix?
So, and That is something that we also need to test. I need to get the Android toolkit reinstalled on this laptop.
**Juliano Costa | Datadog** 03:43 Yeah, maybe a follow-up on that. Maybe we can have your key as a secret, and then we just call your agent.
**Pierre Tessier** 03:54 Oh, my.
**Juliano Costa | Datadog** 03:55 Problems?
**Pierre Tessier** 03:55 Look, I work for an AI company that… is happy to hand Anthropic a lot of money every month.
Yes. I'm just gonna stop there, okay?
**Juliano Costa | Datadog** 04:13 Cool. Okay, so let's get, into business.
As we are, we have a couple of folks here. I want to ask something to Pierre, and I think Chanel can also give his opinion.
But I think Donau is involved in the project for some time now, and it looks like you do have the time to help us out.
I… I would like to invite you to become an approver.
because we have, like, Mikko and Cedric that are not too… too much active. Maybe we can move them to… to Emeritus, and… Yeah, but… the invite is there. I didn't sync with anyone on this call before, so I would like to… I don't know if Pierre wants to block.
Okay, cool. Chanoy, any… any… okay, good. I'll go over it.
**Shenoy Pratik Gurudatt** 05:18 Let's get them onboarded.
**Juliano Costa | Datadog** 05:21 Cool.
Thanks, guys.
**Donal O'Sullivan** 05:24 I appreciate that.
**Juliano Costa | Datadog** 05:26 I'll do the… I'll do the work, and I'll let Cedric know that we are moving him to… to Meritos, because, yeah, I don't think he approved anything for… for some time.
And, Miko, I know that he's in another, a different project now, and, he doesn't have, too much time to invest on the demo.
when I moved him from maintainer to approver, he already said, hey, yeah, you can move me to Emeritus, and I said, no, yeah, let's keep you as approver for now, but yeah, No, maybe, maybe it's time.
Cool. Okay. So, with that, we can… move on to the pending things. So, Pierre, I did have, I did invest some time on reviewing your PR.
The problem now is that, we have a couple of new stuff on the… on the…
**Pierre Tessier** 06:28 Yeah, yeah, I realized that, like, we need to add services, because we added Weaver, is what it was.
**Juliano Costa | Datadog** 06:34 Yep. Right?
**Pierre Tessier** 06:35 Yep.
And that somebody also, for what it's worth, the changes we had to make to remove the log references.
for Podman. There's several things that need to get kind of… brought in, if that makes sense. Yup.
Should've… I will do that now. Were you able to take a look beyond that, or does it just completely fail?
**Juliano Costa | Datadog** 07:01 I didn't run, because I, well, I saw Donal comments, on there, on… regarding the weaver.
Yeah. But then, after that, I think I merged one or two other PRs that touched the Compose.
So then I said, well, those two will also affect PR's PR, so… The thing is that it doesn't complain about merge conflicts, because we are renaming from.
**Pierre Tessier** 07:32 I know, I know, that's where it gets hard.
**Juliano Costa | Datadog** 07:35 But I need…
**Pierre Tessier** 07:35 I need to look at all the changes that have been done to Docker Compose.
and migrate those up to the appropriate Compose files, is what I need to do.
Okay.
**Donal O'Sullivan** 07:50 I did actually pull the code locally and ran it, and the only feedback I had was just the comments, apart from that. It looked good to me.
So, I don't know, is that worth anything, but…
**Pierre Tessier** 08:03 Can you push your changes up to my branch?
**Donal O'Sullivan** 08:08 I… yeah, if you… yeah, I can if you want, it's…
**Pierre Tessier** 08:11 Yeah, yeah, it's all open. I don't do any weird stuff on that, so go ahead and push them to my branch. Okay.
And I will also do another one more manual review to make sure any changes to Docker Compose over the past… since I've opened this up.
are… Part of this, too.
**Donal O'Sullivan** 08:32 Now, Pierre, it was… it was literally only that those telemetry environment variables, I think. It was just those two things.
**Pierre Tessier** 08:40 Yeah, but I think we have to add this service to start up.
**Donal O'Sullivan** 08:44 Okay.
Yeah, I'll… I can… I can double-check what I… what I did, because I… yeah, I pulled the branch, and I ran it locally, and it looked good, I just had to make a tiny change. But yeah, if I have any changes, I can push them to your.
**Pierre Tessier** 08:55 Yeah, we did make another change to, We had to make another change for Podman, because Podman doesn't support…
**Donal O'Sullivan** 09:04 I forgot what it was,
**Pierre Tessier** 09:06 eggs, or something like that, part of the log file, so… so I… I just… it's… I'll do a manual review as well. But if you can make it work, that'd be fantastic.
**Donal O'Sullivan** 09:15 Okay.
I'll, I'll take that as an action.
**Juliano Costa | Datadog** 09:22 And, just so we are, we have that registered, I reached out to, Kusho, which is the user KernelJack, the one that, raised the minimum Docker, profiles.
full and minimal Docker profiles, and I had a sync with him and said, hey, yeah, we may… we may need to go with a PRS approach because… Because of the way that we have the demo, and the way that we have, the… the observability stack being added. At the moment, your PR is not as complex, but once we add a new profile for the For the observability stack, it will start to get S… complicated as the approach that PR is, suggesting. And, yeah, I don't think it's, like, And then, like, I think the extras is a good approach that we do not have with the profiles.
and also the collector configurations that we need to change, like, there is no way we can do that with profiles, so… in the end, I told him, hey, yeah, sorry, so he was fine with it, and yeah, What else we… we have here pending?
Pierre, you… you said that you ran the Reactive Native, PR, And it failed. Is that the one that… Jonathan raised now?
**Pierre Tessier** 11:11 No, it was the…
**Juliano Costa | Datadog** 11:12 Okay, the other one.
**Pierre Tessier** 11:14 It was the… the dependent bot ones, like.
**Juliano Costa | Datadog** 11:17 Okay, okay.
**Pierre Tessier** 11:18 And that's, that's why I said, hey, Jonathan, help?
Because this is beyond what I can do. Well, it's not beyond what I can do, it's just… it looked… and, you know, for what it's worth, Jonathan wrote a really big red diff, and I don't mind those at all.
Those are my favorite diffs.
**Jonathan Munz** 11:40 Yeah, depending on the PO, I… if you could point me to the Dependabot one, some of that might not be relevant once.
**Pierre Tessier** 11:47 No, no, it was… we needed to… We just need to review your PR and approve it. I think we're ready, right? Okay. And once we do that, and then Dependabot will run its next iteration.
And it'll stop trying to upgrade Gradle, because you would have took care of that.
**Jonathan Munz** 12:05 Okay, if it's… yeah, yeah, if it's greater, then.
**Pierre Tessier** 12:07 That's… that's what I'm trying to… do, so, Instead of trying to pin Dependapod to exclude certain folders.
Right. Right.
Because I think we have to pin it for all of Gradle, not just Gradle in this folder. It's a little bit more tricky like that, so we'll just let DependBot keep on not able to get its thing done.
Okay.
Yeah.
**Jonathan Munz** 12:30 Yeah, just enough… so yeah, that one's ready to look at. I had done some additional verification, and everything looked good.
On my end, so, so yeah, I think that one's, ready to be reviewed whenever.
**Juliano Costa | Datadog** 12:43 Awesome.
Cool.
the… We have now from Dono, the department PR, I think we are… there… you have… you are… Jesus, where's the English? You are having some discussion with, Roger, right?
**Donal O'Sullivan** 13:05 Yeah, so… I think… so Roger's happy with it at this stage, so I got some good feedback there, and Pierre, you gave some good feedback, too.
So it… the way it was working was the makefile would… would check if you had Podman or Docker installed, and it would… if you had Podman, it would default to using that one. I think, Pierre, your feedback was just default to Docker, and if they want to use Podman.
you know, they can set… we can set an environment variable, so I went back to that approach, and I just updated, like, the documentation just to show how you can, like, set up Podman. So it won't default to Podman, you'll just have to, like, set an environment variable.
for it to work, but it works on my machine, and I have an approval from Roger, so… Works on my machine, it's the famous language.
**Juliano Costa | Datadog** 13:56 I understand that.
**Pierre Tessier** 13:57 Works for me. Best comment ever.
**Donal O'Sullivan** 14:02 But yeah.
**Pierre Tessier** 14:04 Yeah, I just, I just don't want to break somebody's existing setup in case they did have Podman installed as well. That was really the, you know, like, all of a sudden somebody's like, what's different? Why, huh?
**Donal O'Sullivan** 14:15 Yep.
**Pierre Tessier** 14:17 Yeah, awesome.
Cool.
**Donal O'Sullivan** 14:22 So, yeah, so I think it's good for a re-review, so the only update I've done to, like, the makefile is… I've added, like, another environment variable for Docker commands, which is set in the makefile to Docker, but you have the choice then, you know, it's in the documentation, you can just set that to Podman, and I think it just allows you to, like, run there's, like, a clean images command, make target, and there's a… one for Build React Native Android as well. It's just… just to allow you to use either, but apart from that, it's… it just… it should just work as is.
**Pierre Tessier** 14:54 I imagine setting locally as well, docker command equals podman inside of your .env.override file would take care of it for you.
**Donal O'Sullivan** 15:04 Yeah, I think so, yeah.
**Pierre Tessier** 15:05 That is actually the intent of that file. It's yours, that's your… do whatever you want with it.
**Donal O'Sullivan** 15:13 Yep.
**Pierre Tessier** 15:13 And, it should be ignored, if I'm not mistaken.
**Donal O'Sullivan** 15:18 I think you're right.
**Pierre Tessier** 15:19 Okay, it should be, it should be git ignored.
**Juliano Costa | Datadog** 15:23 I know a bunch of folks that use PartMan, and they just map, the common partman to Docker, and then whenever the user calls, like, Docker, whatever, it… In the background, it actually calls Putnam.
**Donal O'Sullivan** 15:38 Yep. Yeah.
For sure, yeah, I… yeah, I think Roger might actually do that, but I'm not sure, is that… is the buildX command supported by that? I'm… I'm… I would happily do it, but I'm hesitant at the same time.
**Pierre Tessier** 15:55 Yeah, we need to build the X only for multi-platform.
So, if BuildX is not supported by Podman.
Could we just say it's always Docker in that case?
**Donal O'Sullivan** 16:12 That's the way I've left it.
**Pierre Tessier** 16:14 Because it's, it's… yeah, okay.
Yeah, it's only used in the multi-platform builds.
Okay.
So, a little bit more of a… unique use case, but if you want to, from your local machine, build ARM and, 86 images.
On… and publish them to, like, a Docker hub, or whatever reason, and it's not part of a CI, that's what those exist for.
**Donal O'Sullivan** 16:39 Yeah, cool, yeah. I left them as is, so it should still be just the, like, it's just using Docker.
Yeah, I think they should be good for re-review.
**Pierre Tessier** 16:52 Cool.
**Juliano Costa | Datadog** 16:55 So, let me just, tag everything here, like, good, to reveal, and then I just add everything under that.
Because… Wait, the PR from… from the Docker Compose, this one is not good, right? Yet. We need to fix the… We need… we need to fix the… okay.
**Pierre Tessier** 17:21 We need to bring it up to… Up too recent, because of, File changes.
**Juliano Costa | Datadog** 17:34 Okay? And now, one cool thing that I want to… To… to discuss the profiling.
This one is exciting.
**Pierre Tessier** 17:47 It is…
**Juliano Costa | Datadog** 17:47 It is, it is tricky, but yeah, let's, let's talk.
**Pierre Tessier** 17:55 I need a CNCF project.
For an open source profiling backend to exist.
I'm gonna… it's… and it's unfortunate one does not right now.
Pyroscope is popular, but man, does that really show… A preference if you include it.
**Donal O'Sullivan** 18:20 Yeah, yeah, I agree.
**Juliano Costa | Datadog** 18:27 There are two things, actually, that bothers me a bit about it, is that we had Periscope, but we are actually not… seen this stuff on Pyroscope, we are actually seeing in Rafana. I mean, we can also see in Pyroscope, but, like, then we are… I don't want to become the hotel demographer, no?
**Pierre Tessier** 18:50 Exactly, that's what I'm trying to avoid as well.
**Juliano Costa | Datadog** 18:53 Yep.
**Pierre Tessier** 18:53 I'm really trying to avoid that… that view. The busy Adam one, or is it somebody who wrote an open source thing?
It was pretty small and nimble. I left a comment about it in the issue, I think.
**Donal O'Sullivan** 19:03 Oh, yeah, Florian, he's a, he's a colleague of mine. Firefox.
**Pierre Tessier** 19:08 Fire pit. That looked, interesting.
Lightweight, but my fear is that… you know… I'm thinking of the XKCD comic.
Where, you know, you know, there's this little component at the bottom written by one person in North Dakota that nobody respects. I don't want that to be us with fire pit.
**Donal O'Sullivan** 19:29 Yeah, yeah.
**Juliano Costa | Datadog** 19:31 But what… what if… what if we… Like, the problem of profiling at the moment is that it's not stable, so it is… I mean, it is stable, but it is changing.
So, for instance, the PR from, from Donal with Pyroscope, I think you are using 147, right?
**Donal O'Sullivan** 19:58 Yeah, yeah, I just raised the PR just as, like, a… I probably should have tagged it as a POC or something, just to show how it can be done, but yeah, like, I would agree with you guys, like, it is kind of annoying having to use Pyroscope for it. But, yeah, you're right, I think it's using… it's, like, profiling is very much an alpha, and you have to use a different collector as well.
Because it needs that… I think you'll probably always have to do that, but profiling needs, like.
elevator privileges just to run, because it's, you know, running… it's using eBPF in your kernel, so…
**Juliano Costa | Datadog** 20:28 how… how that will affect, Kubernetes runs.
Do you know?
**Donal O'Sullivan** 20:34 So I ran it locally in kind. You're talking just about, like, memory, is it? And, like, etc, is it, or…
**Juliano Costa | Datadog** 20:41 No, the privileges.
Because, like, if I run the demo on EKS, how…
**Donal O'Sullivan** 20:48 Hmm.
**Juliano Costa | Datadog** 20:50 I never ran an eBPF on EPS, so I don't know.
**Pierre Tessier** 20:54 And I'll even raise my hand and say, how does username spaces rolling out now?
And a new version of Kubernetes affect us as well.
That's kind of what allows you to run elevated stuff on a host.
**Donal O'Sullivan** 21:09 Yeah, no, yeah, these are good questions. No, I… I ran it in kind, fine. I didn't check it in, like, in a managed cluster, a managed cloud way. It's… they're good points, though.
Something, something to check out, I think.
**Pierre Tessier** 21:26 Okay, now I thought the signal was no longer alpha in the collector.
Is it still Alpha in the Collector?
**Donal O'Sullivan** 21:36 So… Profiling as a signal… I mean, let me… is this… hang on.
**Pierre Tessier** 21:53 Actually, I'm gonna ping somebody else I know who would know the answer specifically.
**Juliano Costa | Datadog** 21:57 I… I really like FirePit.
**Donal O'Sullivan** 22:07 Yeah, so in…
**Pierre Tessier** 22:09 It's interesting, isn't it, Giuliano? And it's small, lightweight, doesn't look complicated.
and provides the value that we're looking to provide, which is, here's your profile. That's it, right? We don't need to showcase back in I almost wish, like.
We can do the same for all the other signals as well, because I feel observability is a really heavy lift.
on the stack.
**Juliano Costa | Datadog** 22:38 Yeah, we discussed that during the Delta Unplugged.
But go ahead, you were finishing up something.
**Pierre Tessier** 22:47 Yeah, I just… no, that's exactly it, just… how do we reduce the demo's footprint? And Pyroscope is not small.
It's very feature-rich, it's great, fantastic, Fire pit is tiny. It's got a small footprint, small resource consumption.
And, I just… I'm fearful of what maintainership of it looks like. You know, we'll turn it to, like, the next trace test, for example.
**Donal O'Sullivan** 23:20 Yeah.
**Juliano Costa | Datadog** 23:21 But, we can always drop it. Like, if it… if we need a collector just for profiles, and we have FirePit just to receive those profiles, if FirePit or, the collector, or whatever, profiles on, on hotel changes something and starts… Breaking, we just drop those two components, and we are good to continue our lives.
Like, it's… it won't impact as much as the trace test actually impacts us.
Trace tests, we feel the pain of dropping trace tests till now.
**Donal O'Sullivan** 24:02 There is another approach, I know, so the… so Florian, he's… he's a colleague of mine, he's the… crate or a fire pit, but… Crystal's also replied, so there is a, There is a profiling metrics connector in the, that they're… that they're working on now, I think it's in… I'm not sure, is it in full, hotel yet, but, you can turn your profiling data into metrics, and then just kind of graph them. That's another way to do it.
So then you're just, like, not… you could just use whatever graphing tool you want, you know?
I don't know a huge amounts about it.
**Juliano Costa | Datadog** 24:45 Yeah, any… any tool could.
**Donal O'Sullivan** 24:48 Yeah, receive it.
**Juliano Costa | Datadog** 24:49 Yeah, basically, yeah.
**Donal O'Sullivan** 24:50 Exactly, yeah. Yeah, no, it wouldn't be as good, you wouldn't get the flame graphs or anything, which is kind of nice, but…
**Pierre Tessier** 24:58 So the signal is still alpha in the collector, so it would require us to not have a standard collector.
**Donal O'Sullivan** 25:08 Yeah.
**Juliano Costa | Datadog** 25:11 I think we still need the ABPF, collector to generate the… to collect the profiles.
But then it would point to another collector, this other collector would do the profile to metrics, and then export.
**Donal O'Sullivan** 25:26 Yeah, exactly.
**Pierre Tessier** 25:26 But you'd have to custom build a collector, because it's an alpha signal, it's not included in the contract.
**Donal O'Sullivan** 25:31 No, so there's… there's a collector available, so you can… I think I have it in.
**Pierre Tessier** 25:35 Up here.
**Donal O'Sullivan** 25:36 So there's one kind of built for profiling that you can just use. I think there's… I think it's in Docker Hub and everything.
**Juliano Costa | Datadog** 25:43 It has a distro already.
**Donal O'Sullivan** 25:46 Yeah, that's it, exactly, yeah, yeah.
**Juliano Costa | Datadog** 25:50 I'd like to propose a, a vote.
a poll.
what are the options we have here?
add to my.
**Shenoy Pratik Gurudatt** 26:03 Before we go into the voting, I think we discussed about Inspector Gadget a bit.
Long ago, I think a year back, right now.
There's a CNCF Black project, which had the hotel export for its profiles to metrics and logs.
Doesn't do.
**Juliano Costa | Datadog** 26:25 What's the name of it?
**Shenoy Pratik Gurudatt** 26:26 luckily.
Inspector gadget? I added it in the chat.
**Juliano Costa | Datadog** 26:32 Spectre Gadget. Yeah, I think you, you brought that up.
**Shenoy Pratik Gurudatt** 26:37 Nope.
It doesn't do, like, a profiling flame graph capture.
It will convert the… eBPF capture data into hotel logs and metrics.
It's the same sidecar thing that you run.
**Juliano Costa | Datadog** 27:04 Sweet.
I… I like better if… I like better if we could use profile, in the flame graph approach, like, as profiles are meant to be, Like, at least as profiles are usually viewed by.
**Pierre Tessier** 27:24 Intended to be consumed.
**Juliano Costa | Datadog** 27:25 Yeah, exactly. Thank you. Yeah.
**Pierre Tessier** 27:29 Yeah, I agree as well. I'm not too interested in creating things that convert profiles to other formats?
I'm more interested in… Getting the profile signal end-to-end.
Received and exported out.
all through OTLP, and then have something else that can… Render those profiles.
As a backhand.
whether that's Pyroscope, or…
**Shenoy Pratik Gurudatt** 28:01 Yeah, this is more like a receiver, and it's a complementary tool, it's not a backend.
**Pierre Tessier** 28:07 No, no, and I want to try to stay on the OpenTeleTree chain as well. If this means we have to have a, you know, another distribution of the OpenTel collector, I think that's fine.
But I'd rather just stay to the profile signal.
Amand.
**Juliano Costa | Datadog** 28:27 Can you just toggle?
**Shenoy Pratik Gurudatt** 28:29 It was last year when they didn't have the profile. I see exporting to profile also added in.
**Juliano Costa | Datadog** 28:34 Cool.
**Shenoy Pratik Gurudatt** 28:35 But it's just a receiver thing. It's not a backend to store anything there.
**Pierre Tessier** 28:43 Okay, so what are our options here, Juliana? We, could… .
**Juliano Costa | Datadog** 28:53 So, we have, Periscope, that Adono suggested.
We have fire repeat.
And, we also have Parka, but I don't know how far they are with, hotel support. And it's also a vendor.
It's like… I think.
I don't know if ARCA has, yeah, an open source approach or whatever, like, distribution or whatever.
But what I want to say here is that I feel that Firepeat is, I know, a side project, but… like, lightweight and agnostic, even though it was created by a Elastic guy, but, like, yeah, I don't mind. It doesn't have anything from Elastic there, so… part of the demo, as a maintainer, I think it would be, like, nice to have, and he's open to donate and, like, accept more contributors, so we can even help improving the tool. It's not like TraceTest that had some parts that were closed source that we do not have access anymore, and, yeah.
**Pierre Tessier** 30:11 He is also a CNCF, he's already signed his, He's part of the hotel community, so, he has contributed. You know what'd be great? I agree, I would love to move this to using fire pit instead of… Pyroscope.
And, for that reason as well.
We should probably make up… I know others are plus-oneing it there, also. I, I, I, can we just get him to, Florian, to, like, bless this?
Yay.
**Donal O'Sullivan** 30:42 Yeah, I…
**Pierre Tessier** 30:43 You know?
**Donal O'Sullivan** 30:45 Just an FYI, Florian is a maintainer of the hotel profiling as well, so he's… he's, he's big in the profiling world, so he's, This is his bread and butter.
**Pierre Tessier** 30:59 So he's well-vested in this, and perhaps when he moves on, he will start up a brand new company based on Fire Pit, and, started as a CNCF contribution.
And we will be okay moving forward, and we'll have support. So that's… let's go. I'm sorry, but I've seen a lot of people do that now in the open telemetry community. Jurassi being another one, right? And it's great, this is fantastic, because… Yeah, they create companies that have solutions leveraging OTEL.
**Juliano Costa | Datadog** 31:31 Guys, I gotta go, but, I'll publish on… I'll post on the… on the issue, like, hey, let's go with FirePit. I don't know if, Florian, or… don't know if he will change your PR to use Firepeat. Yep.
or if Florian would raise up here. Anyways, I think we all agree to hear.
Jonathan, Jonathan, you didn't say anything, but yeah.
**Jonathan Munz** 32:02 Sorry, I was, focused on something else for the last bit.
**Juliano Costa | Datadog** 32:05 Okay, then you're good.
**Pierre Tessier** 32:08 I do have to run.
**Juliano Costa | Datadog** 32:10 See you all. Cheers.
**Donal O'Sullivan** 32:12 See you guys. Bye-bye.
