SIG: eBPF instrumentation
Date: 2025-11-19
Duration: 35 minutes
Zoom Recording URL: https://zoom.us/rec/share/f3MIPiAwQrH-iaavsm_bEsz0CZNg5Tag3UNBpUz77LtwGYK2A737EHOol0feaKFh.UXwjl6oe19FUubJx
============================================================

## Zoom Recording Transcript

**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:49 Is he gone?
**Giuseppe Ognibene | Coralogix** 00:51 I…
**Florian Lehner** 00:51 Hello.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:57 Let's see how they're doing, Tyler, our usual MC, is not here.
run this thing.
Let's just wait for, few more people to join up.
Maybe I can move these to next week's meeting. They're not urgent.
Tyler's thought on that as well, because he's been involved in the hotel demo.
So, I'm just gonna, for now… Move them up… I know Steven has… oh, you're here, okay.
Yeah, I was assured.
You have a conflicting meeting.
**Stephen Lang** 02:26 The other one's recorded, so I'll stay here.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:28 Nice.
Let me just ping Mario, because he's got an issue… Let's see… Enjoying… He's having issues. Okay, well, we can get started. I just saw a message from… Right, so I'll do it, and I'll try to.
Okay, do you guys see the meeting notes?
**Stephen Lang** 03:37 Yeah.
**Mario Macias** 03:38 Hello!
**Stephen Lang** 03:41 Hey, Mario.
**Giuseppe Ognibene | Coralogix** 03:43 P.
**Mario Macias** 03:43 Fucks.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:46 We're good. I think we have full house here.
If you haven't added your name to the list of attendees, please do so.
I'm gonna run the meeting, because Tyler left a message that she's not able to attend.
I guess he's away this week, so, thanks all for joining, with, we have a couple of issues, things on the agenda, and finally, I'm just gonna go and… the open PR reviews.
Just to see if anything else needs to happen at the end.
So let's kick the ball rolling. I guess, Steven, you have the first issue on the agenda?
**Stephen Lang** 04:35 Sure, yeah. So, it was mentioned previously about potentially adding artifacts to our release process.
Because I think at the moment, we just do a git tag.
And, there's no artifacts that are produced.
So I spoke to the Open Software Security Foundation at KubeConk.
About this, and apparently there's some things that we can… we can use as a… as an open source project we can… we can use for free.
So… SIGSTOR is the initiative behind, COSign.
Cosign is a binary that you can use in GitHub Actions to sign both container images But also artifacts in general.
So, you can sign, binaries.
But you can also sign, interestingly, eBPF programs and store them in an OCI registry.
I'm not saying… not saying that we do that, because that's a… it's different to what we do now, it's just good to know that that is a capability, and that's the link there, the work… working with other artifacts. But the first one, which is, sort of signing… signing the binaries.
The good thing about using cosign is that we can do this within a workflow, and we don't need to store keys on developing machines.
So it's not like GPG, where we all have to, you know, add on our public keys to a certain you know, registry or whatever. This can all be handled online.
And so the… the SIG store actually provide, like, a signing… Authority, or store.
And there's even, like, a public ledger.
Where people can kind of confirm that these, These keys, you know, the certificate keys.
if they're actually part of that organization, and are recognized for this, this binary.
And you can do the whole, you know, checksum.
Verification process as well.
So it looks like we might be able to tie this into our existing Release process, we just have to do a build, and then add a step.
And I added a link here for the cosign installer GitHub action, which they provide.
so, yeah, I just wanted to bring this up, because this looks like, a really easy way, and also a recommended way of doing signing. And so I kind of see Cosign is almost like, the Let's Encrypt.
For signing artifacts.
So, yeah, just wanted to bring that up.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:17 Very cool. Very cool. Alright, I mean, I guess we, you know, tried to get a… And try, like, a PR or some kind? Maybe, like, an experiment with this, see if it works.
This will be cool.
Well… Good, good find.
**Florian Lehner** 07:36 Maybe a question around this, also related to the question that Naev from Datadoc asked in the, Slack channel.
Should be there… what is the… what is the idea of integration with AutoCollector? Because… does OTCollector something similar, and is this work something temporary, or will this be duplicated work, or… How does this fit into the bigger picture here?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:05 Yeah, I mean, our long-standing goal is to add Obi into the collector. I think Just like the profiler, there is a… there is a build with it, and… I guess… If we need to sign there, we can have to figure something out there, but maybe at that point… When it gets merged into the collector, that's a separate sort of work item there.
I don't know if the collector's… distributions are signed at the moment, in any way, or…
**Florian Lehner** 08:39 I don't know, that's why I'm asking if there is something… That maybe duplicated work, or later done.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:46 I haven't heard of anything, I know that we… we were… you know, discussing this in other SIGs as well. I haven't heard of any official way, so… I guess we're gonna trial it. We're definitely going to add, OB into the collector, and… Especially, I'm interested there, because if it's the same process, then we can easily share with the profiler the data. For example, provide a trace ID in a map or something for a given thread, then maybe the profiler can pick it up and add it to the profiling.
**Florian Lehner** 09:19 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:19 on extra metadata.
**Florian Lehner** 09:21 I'm not sure if this was shared with DISC, sorry for the off-topic, but Datadoc came up with an approach to share, some kind of information that can be correlated across, different observability solutions. So, that an SDK, for example, opens an MMAP. Let me quickly… find.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:47 Yeah, I saw that.
**Florian Lehner** 09:47 Don't temp.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:49 Yeah, yeah, I think I saw that, that's pretty cool. They want to be able, from the SDKs, to write into the storage of the thread that the, the Ultra profile, I can pick it up, right?
**Florian Lehner** 10:01 Yes, yes, I think it would… Benefit with just profiling, but also, This project.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:10 Yeah.
That… that's gonna be pretty cool. If the SDK started doing that, then we can pick up the information from Moby as well. And that solves a lot of… issues, whereas in respect to finding the right trace ID, Do you know if that's moving forward, if anybody's gonna implement that?
**Florian Lehner** 10:32 There's a high chance that we will do it, on the profiling side.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:37 Okay. How it will be adopted by the SDKs, I cannot tell.
**Florian Lehner** 10:43 The challenging part is, I would say the… Duh… Anonymous… anonymous mapping approach.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:54 that not every SDK can use.
**Florian Lehner** 10:58 But maybe this protocol can be used, so there's a, protobuf.
Declaration on how the status will be shared.
one way is to share it in an anonymous mapping, in a process, but also could be a socket or whatever. It's just a way of communication. Yeah, but yeah, super exciting to… I think correlation is… Super critical to get to get these signals together, On their own they are good, but together they are better.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:33 Yeah.
I agree.
I mean, if the profiling adopts it, we will too.
I'm just gonna say, yeah, if that lands and SDK started doing it, I… I don't see a reason why I wouldn't want to use the same thing.
Right now, we parse the… this… this thread information from incoming headers, and as you can imagine, with things like gRPC or other technologies that are not as straightforward as an HTTP is difficult. So, if this information is provided somehow by the SDK, then… so much better.
**Florian Lehner** 12:10 Yep.
Sorry for off-topping.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:14 No, that's good, that's good.
Okay.
We, the next thing is just an FYI, I don't know if people saw this, but, we're gonna start… we started working on the adding Java support for TLS into the product, so there's gonna be a small Java agent that needs to be injected, because otherwise there's… We looked at other approaches here, and none of them are good.
Because technically, in order to capture TLS, we would have to set, probes into the JIT-generated code.
Which is only doable if we get remapped to Java code cache to, file, memory map file, so that we can, have a inode number so that uProbe can attach.
Which, yeah.
requires P-trace, stopping the program, running syscalls to remap and all, and it may not succeed. So, we decided to take that easier way out and inject a small, tiny Java agent, which… So far, it works with even Dynamic Attach.
This agent isn't doing much, but, just providing the information, to the… to the EBPF sides through, invoking a C library call, which then is intercepted.
The agent code is now in the codebase, and there is a design doc in there in the README explaining how this works.
If anybody wants to take a look. It's not actually working yet, because we… the inject part is not done.
Right now, it's just only experimenting with an external tool. But we do have support for injecting, And talking to a JVM, only hotspot for now.
And so, should be able to… tie this together. So, a couple things need to be resolved, like the whole packaging situation, and Making sure the jar is in there, and so on.
But provided that all works, I think we should be able to… Support TOS for Java.
Sue.
Yeah, so Mario, I think that's the next… any… if you have any questions on this topic, Mario?
You have the next item on the agenda?
**Rafael Roquetto** 14:59 You're muted.
**Mario Macias** 15:00 Let me see… let me see if I can share my screen, because I had issues with Zoom. I couldn't connect.
Let me try to connect again from my… I'm connecting as a guest.
Let me see if I can connect again… Okay.
And share my… no… for some reason, I'm… Okay, for some reason, I… I cannot. Okay, I've been digging into this, error,
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:33 Sorry, if you have a link or something that you want to send to me, I can share it for you, if you like?
**Mario Macias** 15:40 Of the… it's, it's a, it's a, it's a unit test, a branch with unit tests, but, Sure. Let me see if I can, it's a bit weird… One moment, let me try again. Okay.
it say I'm not anymore in the Zoom application from… From Grafana. I don't know… I don't know the reason, but okay, let me see if I can connect this from the browser.
is not… If not, I will just mention…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:20 That's okay.
**Mario Macias** 16:21 Okay, I've been… Whoa.
Okay, I cannot.
I've been doing some tests, and the behavior is very weird. there is an… if you… you might have noticed, there is an error, login, OBI is logging, sending message, sending queue is full during traces.
I've been verifying that the… the metrics and the traces are resubmit.
resubmit after they fail. But, it seems that under certain conditions, the traces might, be lost.
Because if… if… it's what I think is happening. If… if something… if a submission fails.
Then it keeps retrying the resubmission, but if another submission fails again from other batch of metrics, then it seems that the previous resubmission is… the previous retry is discarded, and then it tries again with the latest batch.
I noticed that because I've been doing some… some unit tests, you mean… it's not realistic in the sense that there is no network latency and so on, but for… I've observed some counterintuitive behaviors. For example, if the… if I reduce the back-off time of the retry to the very minimum.
The number of lost traces is much lower.
Also, it's counterintuitive that if I increase the max queue, the max size of the queue.
We also lose more… more traces than if I keep a small… a small size for the Max-Q.
Yeah, I don't know if it is because then the… I don't know, the Q… Takes more to be filled.
And then the retry is longer, I don't know, I don't know, but there is… there are some counterintuitive. So, my main… I was suggesting last week to just moving this error message to the back.
But I'm not sure if we should move it, to the back, because under certain conditions, we are losing traces. I'm not sure if that's the case of… of real users. I was talking last… last week with Andre.
who noticed that, and they said that they weren't losing traces. So I guess that in a more normal pace, and not a… not a unit test.
Okay, the number of traces lost could be very small. Yeah, Raphael?
**Rafael Roquetto** 19:31 where… do you know where the traces get lost? Like, because they make it to the queue, but then they never appear on the other side? Did they get the queued, or they don't even make it to the queue? Do you know?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:45 I've looked at this as well, but the thing is, like, they work… the collector SDK sends a batch, and the batch fails.
So, but at the same time, it's filling up a new batch. So there's a new batch going on, being populated, and new sets of traces. But you have the existing one where they're trying to send, and you presumably can't send it for some reason. There's a network disruption, or whatever it is.
It retries a couple of times, And then… Eventually, the new batch that has been filled up Gets ready to be sent to.
So then, the new batch simply overrides the previous batch as the current one that it's sending. So it has this sort of, like.
split, that I have the current sending badge, and I have the one that I'm filling up with new traces.
**Rafael Roquetto** 20:33 And you're saying that if you increase the… so increasing the queue means increasing the batch size, is that correct?
**Mario Macias** 20:40 Yes, for, for some reason, it makes, lower… I mean, it, it makes losing more traces.
**Rafael Roquetto** 20:51 I mean, that makes sense, because if you're pushing a huge batch, maybe on the other end, it's not able to… Catch up with this huge batch, like it's a big burst.
And then it drops it. Whereas if you're pushing just, like, one by one, or two by two, like, small batches, it's…
**Mario Macias** 21:08 No,
**Rafael Roquetto** 21:09 It can process it quick and turn around, it's quick enough.
**Mario Macias** 21:11 Yeah, yeah.
**Rafael Roquetto** 21:13 probably… I mean, I'm just guessing here. It's not necessarily, We're generating these batches, and then you can increase the queue as much as you want, but it's like the consumer on the other end is not able to keep up, if that makes sense.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:31 Yeah, and I think, Mario, maybe in your experiment, if I get it right, reducing the back-off time, maybe…
**Mario Macias** 21:38 Yes, reducing… reducing the back of time allowed to lose very few metrics, so the number of lost metrics was much smaller.
**Rafael Roquetto** 21:53 So this is the collector ingesting, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:56 Yeah, or something, but… but I think it makes sense, Mario, like, if… if I'm… But it means that you're filling up the next batch.
maybe very quickly, but if your back-off time is smaller, then you retry the send faster, so you have more chance of completing that current batch that is about to go out.
**Mario Macias** 22:17 Yes. Before the new one comes in and overrides it, so… Maybe we can…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:23 lower the setting.
**Mario Macias** 22:24 Yeah, I agree. We should… we should at least document. I mean, because we were recommending users to increase those values, but maybe we should recommend make them smaller.
**Rafael Roquetto** 22:39 Yeah. But do we know why, on the consumer side, it fails to process it?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:47 There's gonna be a number of reasons for that profile.
**Mario Macias** 22:49 Yeah,
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:50 Could be, like, collector's too busy, could be that there's a network disruption, some temporary issue, like… This is normal, like… Yeah. Well, I see.
**Mario Macias** 22:58 In the unit tests I'm doing, I'm using a fake HTTP collector that runs locally. It should process very quick, the things. But yeah, anyway, we are losing. So, yeah, I guess that the… any remote collector that is actually doing things with the ingested metrics should Should be low, slower, I'm… And get… and struggle more often. But even in local tests, fails.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:29 Yeah, it would… it would happen, but it's… it's just… the beast we're dealing with, right? So… Okay.
**Rafael Roquetto** 23:40 Yeah, I was just wondering if there was anything we could do on the collector side, even though it's kind of outside of our scope.
You would… I mean, I don't know anything about the collector, but I would have hoped that if you… send a… a huge batch, like, you're in queue, and you push it, that's the whole point. You… you would be able to process it, and, like, in background or something, like, have a better throughput, but… yeah.
**Mario Macias** 24:08 I… I wonder if we can have… A number of parallel, trace exporters.
And… And we… So instead of having one single queue, processing all the batches serially, having some of them at the same time, so they can retry before getting a new batch. I don't know if this is feasible.
That will involve, instead of one connection per client, having multiple connections, probably.
But I don't know, I don't know.
Okay, we should investigate a bit more and provide… A solution, because it's actually very annoying, this continuous log message.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:58 Yeah, it would be nice to know when, When the packet is dropped, but… Perhaps not when it's retrying.
Yeah.
**Mario Macias** 25:07 Yeah, exactly, exactly.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:10 I think we can control the collector logger. There's waste, so I think perhaps it's not too bad. I think.
**Mario Macias** 25:19 That is awesome.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:20 We can investigate that to control to see which messages we see and which ones we don't.
**Mario Macias** 25:25 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:31 Okay, okay, next to the agenda is the open PRs.
I think we're looking good. There's only one that… Maybe outstanding. Mario, this is yours.
**Mario Macias** 25:46 Which one?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:49 Do you see my screen?
**Mario Macias** 25:51 Yeah, yeah, update and fix auto collector in tempo, and… Yeah, these… this… this is, this old… yeah, this old testing update is, is a bit… requires very big changes. I tried if… if I could…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:10 Hmm.
**Mario Macias** 26:11 If we could just update some dependencies, but there are many breaking changes.
Okay. Yeah, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:18 Okay, we can reattempt that, if you'd like. Maybe update OATs as well. I know there's a new version, so maybe this is a bigger work item.
Something… To be added as an issue, rather than… I don't know if you want to continue on this PR, or close it.
**Stephen Lang** 26:40 the Alpine one I want to talk about.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:44 Which one is… this one?
**Stephen Lang** 26:47 Yeah, this probably picked up on the fact that I moved Alpine to an older version. So, do you remember the CV that came out with the Insecure, Run C, Rocket Fest?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:00 Yep.
**Stephen Lang** 27:00 So the workaround was to pin Alpine at 3.20, Because that used an older version of RunC prior to the CVE patch.
So the reason, probably, that this fails is because, and imagine 3.22 got a new version of, run C, and so we… we hit this CVE problem, which is… How the host Proctor Fest is now no longer accessible with, nested virtualization, which we use in our, QE new VM workflows to test.
For example, kernel 5.15.
6.10, so our older kernel.
workflows rely on this nested virtualization, because the GitHub runners are on, you know, 6.14, there's no other way to run an older kernel. So, this is another thing that I discussed last week. I spoke to a few vendors about what we might be able to do here, but actually.
I think we might be able to do this with, self-hosted GitHub runners.
So the idea would be is if we had a self-hosted GitHub running, where the machine itself was running an older kernel.
then we wouldn't need to use nested virtualization. We'd be able to natively run it on, you know, 5.15.
But it means having a machine that is running 5.15.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:18 So, Tyler mentioned that.
**Stephen Lang** 28:21 We might have some OpenTelemetry self-hosted runners.
Okay. And the other option that I came up with is maybe we could use the free tier on, you know, various hosts.
just to build, like, a simple… say, for example, an EC2 node, and put a 5.15 image on there, and use that as a self-hosted runner.
So that's probably why this particular build is failing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:44 Okay, well, I can close it with a comment saying that.
**Stephen Lang** 28:50 There is an open ticket, I don't know if you want to reference that. There's another issue, which is to investigate, This whole thing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:58 That's a good idea.
**Stephen Lang** 29:03 If you look at author SKL, you should be able to find it.
That's the one.
Florian, you have your hand raised.
**Florian Lehner** 29:19 Yes.
I don't know if the internals of, internal test VM at the moment.
But on the profiling side, we are also doing, per-kernel version tests, from starting 5.4 to… I think the latest one is…
**Stephen Lang** 29:39 616, 618, 617 something. Okay.
**Florian Lehner** 29:43 And we also use just regular GitHub action.
And we don't… this issue.
But we also don't use.
**Stephen Lang** 29:57 Not Alpine, right? So I think this might be Alpine-specific.
**Florian Lehner** 30:03 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:04 Can we switch away from Alpine and use another…
**Stephen Lang** 30:08 So, Raphael might know about this.
**Rafael Roquetto** 30:10 Yeah.
Yeah, we can, we can, like, pine was picked just because it's compact, but if it's giving us headache, we can… We can get a…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:21 Yeah.
**Rafael Roquetto** 30:22 We can get a different… get a different, root file system.
**Florian Lehner** 30:34 Maybe to expand on this, on the profiling side.
we are using, BlueBox, which just generates, generic integer MFS.
One time, and then we use this generic intendrome FS multiple times on various kernels, so we can say we have always the same INITROMFS.
And testing it, against, various cars, so… yeah, maybe that's… that's the reason. And in this interim FS, we don't have, We don't use, Alpine or something like this, so… very basic.
Cool.
**Stephen Lang** 31:11 to that workflow?
**Florian Lehner** 31:13 Sorry?
**Stephen Lang** 31:14 Do you have a link to that workflow?
**Florian Lehner** 31:15 Yeah, sure, let me quickly check.
**Stephen Lang** 31:18 Thanks.
**Rafael Roquetto** 31:20 Do you have… do you have a, like, a root file system on top of, like, you… you… or you just use the Unit RAM FS for your tests?
**Florian Lehner** 31:29 We abuse Go, so we build everything in our Go executable, pack it into the inner MFS, and execute the inner MFS, or the inner MFS would trigger the Go executable Then everything will just happen.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:43 Nice. I see. Okay.
**Rafael Roquetto** 31:44 I don't think that will work for us. I don't think that will work for us, because we need a full Docker, like, environment running for the integration tests.
For, you know, to launch, Kubernetes and Docker Compose, so that in that case, only having you need to run FS, One code. We need a full-fledged, like, VM system.
**Florian Lehner** 32:10 Okay, yeah, maybe then this is not an option for you.
**Rafael Roquetto** 32:12 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 32:15 Yeah, just as a comment, but we can put a… probably pick a different distro than Alpine, if Alpine.
**Rafael Roquetto** 32:22 Yeah, can get Ubuntu, for instance, back.
Trimmed-down version, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 32:28 Yeah, yeah, like a minimal distro, or some… something else, like, maybe there's even a smaller distro based on… I don't know.
**Stephen Lang** 32:36 Debine?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 32:38 Yeah, Debian, or Redhead, or something, I don't know. Like, we're… I'm sure we'll find some alternative.
Go ahead.
Yeah, these are probably just, hitting random issues, yeah.
we would, like, us, I guess, maintainers have to go and nurse these to completion.
Where they've hit a problem that might be just, one of these random ones.
But nothing else, it seems. We did have a problem recently with one of their multi-node, local node tests or something. We're constantly running out of space in the… And, runners.
It was a kernel upgrade, and that pushed, I guess, the size a little bit, and fewer tests were failing, but that's resolved now.
In the pull request, so… should be okay.
I'll see if some of these can be pushed to completion.
Yeah, I think this one's probably the most important one that we need to get through.
I don't know why it's failing, so I'll check on this.
**Mario Macías Lloret** 33:57 Regarding this, I'm manually updating the versions. There are some breaking changes.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:05 Okay. Yeah.
**Mario Macías Lloret** 34:06 Yes, I know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:06 I remember, I remember we had to upgrade some way we set up the exporter, right? Yeah.
**Mario Macías Lloret** 34:13 Yeah, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:14 There's one function, yeah.
**Mario Macías Lloret** 34:15 Absolutely.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:16 VR.
**Mario Macías Lloret** 34:16 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:17 I have a PR, I have a PR for that in our release, so I'll push it. I'll push it.
**Mario Macías Lloret** 34:22 Okay, okay, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:23 I may close this and update it manually.
**Mario Macías Lloret** 34:26 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:29 Okay, we're done with the agenda. Any other… things you'd like to share? Anything cool you heard at KubeCon, for those that made it, unlike me.
**Mario Macías Lloret** 34:43 The coolest stuff was from OBI, so you are… you are up to date.
Just, just joking.
**Stephen Lang** 34:54 From Mario's talk, specifically.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:58 Yeah, Mario got it.
Maria presented all the talks, yeah.
Okay, well, if there's anything else, we can, continue async, and thanks all for coming this time, and I hope we see you next week.
**Mario Macías Lloret** 35:21 Thank you, Nicola.
**Giuseppe Ognibene | Coralogix** 35:22 You guys, bye-bye.
**Rafael Roquetto** 35:23 Thank you, bye.
**Cheithanya PR** 35:26 Hi, everyone.
I guess.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 35:31 Bye.
