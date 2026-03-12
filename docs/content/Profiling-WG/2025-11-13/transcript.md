SIG: Profiling WG
Date: 2025-11-13
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Ivo Anjo 00:04:30 Hello.
Felix Geisendörfer 00:04:32 Hey.
Florian Lehner 00:04:33 Bonjour.
albancrequy 00:04:42 Hello?
Felix Geisendörfer 00:07:21 So we're 3 minutes in, so you can get started. If somebody else churns a little bit later, that's fine too.
So, hello and welcome, everybody. As usual, we'll start by reviewing our previous action items, and then we have some more agenda items for today. So, let me share my screen.
Here we go.
And I see we have a bunch of… items on Alexi, who, when I just checked, was not here yet, so maybe I'll just move that.
To the bottom, and see if he joins in the meantime.
And… Move this one up here, or I guess this was part of… performance.
Sure, we'll get to it. Okay, So, let's start with number one, Florian OTLP P-Prof converter. Any updates?
Florian Lehner 00:08:27 Yes, this is just, helper PR to get in more… Semantic convention attributes.
Around, keep frames, strong frames, comment, and, dog rule.
So, yeah, we need them to… for the… for the conversion.
Yeah.
So, I think I linked also in the… In the code where these will be used, because at the moment, we are using hard-coded elements.
Yeah, this translator packet, package translator PTROF, that's the place where they will be used. At the moment. There is a hard-coded value, which would conflict with, semantic conventions.
Felix Geisendörfer 00:09:18 Okay, for this group, does this need more referrals right now, or what…
Florian Lehner 00:09:22 Yeah, I just opened it today, so there would… I need to refuse on it.
Felix Geisendörfer 00:09:28 Okay.
And yeah, so basically these are people of specific fields, that need to be represented in OTLP, because we dropped them from OTLP, basically, and then dropped them from PROP.
Okay, Alright, then anybody who has time, please take a look and leave a review.
Then… Or is there any questions, comments here?
Okay, then… next three few context propagation documents. I already saw Evo unmute, so… go ahead.
Ivo Anjo 00:10:36 Yes, hello. So, a couple of smaller plates, one is that, I have basically rewritten, like, taken the document we already had, and we wrote it in the OTEP format, and opened the PR in the OpenTelemetry specification repo, as I said last time, so… I think the, if any… if you already gave feedback and, like, on the previous document, or read through the previous document, this one is kind of just… it's rewritten in the OTEP format, so expect no surprises, but please give it a quick look, and I think… I'm hoping to… I was actually hoping to present this in this week's OTEL specification SIG meeting, but that got… moved because of the Kubicon, so I'll try on the next one, but yeah, I am hoping to keep pushing this and, and hoping that the specification folks can kind of agree, and we can… like, get to a first version of this specification that we can then start implementing.
And the other note I had is that, the PR I had, let me open it… Oops.
Let me… I'll just do this. Let me open here a new item, and this… this PR that I had for the protobuf format, I think I've addressed the feedback, so I don't know, like, what's, if we can merge it, or if there's other things we want to do before we can merge it.
And… and I was, yeah, I'll stop here.
to let people reply to actually what I'm saying.
Felix Geisendörfer 00:12:52 Okay, looks good. Yeah, so I think, they asked for anybody who hasn't taken a look, take a look at this, and for this one, do you think we should already review and comment, or should we wait for the, for your meeting with the stick? Like, does this need more feedback from this group? Because I think a bunch of people already Looked at your previous stock.
Ivo Anjo 00:13:10 Yeah, I think, I think we don't… I think, we don't need extra feedback, because, like, most people already gave feedback on the previous doc, and this is basically that.
So, the only question I had was.
the… I've been keeping a repository on my personal GitHub account that has some of the reference implementation we did in C, and the experiment in Java.
If it would make sense to also move that to the SEC profiling repo, or if I just keep it in my repo until we find a better home for that.
And the repo I'm talking about is this one.
Felix Geisendörfer 00:13:53 I think the SIG profiling repo is good for, like, these kind of prototypes and other things.
Ivo Anjo 00:13:58 Yeah.
Felix Geisendörfer 00:13:59 Just make sure, like, to get yourself a top-level directory.
Ivo Anjo 00:14:04 Okay. And then, in that case, I'll make… I'll be out for a few days, but after I come back, I'll open a PR to kind of add these things there, which is, I think, a better place to put them in.
Christos Kalkanis 00:14:19 Yeah, I think we should have everything in the same place. That's also one reason why I quickly approved your other PR, Evo. So I thought that we would do all the commenting either on the Google Doc, but unfortunately, like, your pull request has turned out, like, it received a lot of comments, and yeah, it hasn't been merged yet. But anyway, but yeah, let's try to… To get all the tooling in the same place.
Ivo Anjo 00:14:41 Don't look.
Felix Geisendörfer 00:14:48 Okay, cool. Any other thoughts on this?
Once? Going twice? No? Then, Next item is an order wanted. We basically need to document that values and timestamps, the shape of that in the samples message should always be the same within the same profile. So if you do decide to use timestamps, you should do it consistently in a profile and not switch between samples that have timestamps and that those that don't.
But this is kind of non-urgent, it's not blocking us right now, so we'll get to it, but I think everybody has a lot of stuff going on right now, so I think we can leave it at as owner wanted, unless somebody got inspired by what I just said and wants to own it.
Christos Kalkanis 00:15:35 Hey, I think… I think we have a pull request open, unless I'm mistaken. Jonathan has a pull request open for this, that also clarifies, And that was blocked on a comment by Josh.
Let me find it. It should be in the agenda, but… This dress is also here.
Jonathan Halliday (IBM) 00:15:55 Yeah, that's… the next one, 724, but I don't think it explicitly covers the… all samples should have the same shape thing.
I can imagine it does, but I'm gonna derail it again.
Felix Geisendörfer 00:16:08 No, no, no, let's keep it scope limited.
Christos Kalkanis 00:16:11 So, if we scroll… if you scroll down here, let's… let's try to find…
Felix Geisendörfer 00:16:16 This one?
Christos Kalkanis 00:16:17 Yeah, there's a comment there by Josh, and then I have a follow-up, and then Alexei also has commented there. Yeah, so, essentially… Sorry, go ahead, Jonathan.
Jonathan Halliday (IBM) 00:16:26 I just need to ping Josh. I think he's got the wrong end of the stick on that, basically.
I don't eventually want to change it.
Christos Kalkanis 00:16:34 Okay, cool.
Yeah, so let's match this first, and then, yeah, I can open a follow-up to do that, or Jonathan, if you prefer, because you started the work, you know, whatever you would like is good, like.
Jonathan Halliday (IBM) 00:16:47 I'll take a look at it once we've got some T4 in.
Felix Geisendörfer 00:17:12 Okay, I think I… oh, wait, I put this in the wrong place. Where did my owner want it?
Single.
Are we merging this together?
Jonathan Halliday (IBM) 00:17:23 I'm just trying to…
Felix Geisendörfer 00:17:25 Oh, you're… okay, okay.
Jonathan Halliday (IBM) 00:17:27 Bye now!
Felix Geisendörfer 00:17:29 You… it's yours, wait. No, ownership is up here. No, it's not here.
Cool. Thank you so much. That's great.
Yes, 724, I guess, was the next agenda item anyway. Do we have more?
Okay, okay.
Jonathan Halliday (IBM) 00:17:50 Do you need?
Felix Geisendörfer 00:17:51 You just need to talk to Josh. Okay, awesome. Great, thanks.
Then this is also 724, I guess, sorry, okay. Then Alban, I think, is the next one, and I think we also had an agenda item down here for the security advisors, I guess is basically the same Alban, right?
albancrequy 00:18:11 Oh, yes, that's the SIM.
Yeah, email the security at kernel.org mailing list, and, have received feedback on They told me what happened on the issue.
I think, I'm not sure if there was a conclusion from the discussion on the GitHub issue, that if we want to use PockFS, or if we want to not do that.
I mean, if you want to have an option, or if you don't want to have this option.
Christos Kalkanis 00:18:44 So I think the Elastic folks, this is basically me, Florian, Timo as well, like, yeah, we don't like the proc effects, we would like to steer away from that. Now, that said.
you know, if Felix, Datadog, or the other people would have strong opinions on Crockpit men being used, then, yeah, we could make it a fallback, as long as it's not a default.
But, like, on that front, if we absolutely need a fallback.
I'm more inclined to… like I wrote in the… I left a comment in your… on the issue, Alban. Yeah, I'm more inclined to look deeper into the other proposal that you have, which is essentially an artificial timeout using a signal.
Right, for the system call, right? I mean, my only reservation there is that it kind of relies on how the Go runtime uses CGRG internally.
so if they change that, you know, maybe we ran into problems.
But, I like that better than using Profit Man, for example.
But yeah, I mean, thoughts, like, we wish Elastics shouldn't be the only ones commenting here, right?
Felix Geisendörfer 00:19:57 Yeah, my… or Avan, do you want to go? I saw you on mute. We can go first if you want.
albancrequy 00:20:03 Sorry, I had a problem with the button. Yeah, from my side, I don't really like so much the timeout solution, because I think it's… Difficult to get right, especially because for a lot of interpreters, we need to read the memory several times, it's not just one read, so the cumulated effect could be, If each trade takes some time before the timeout, we should not accumulate the timeout.
it that way, so I think that's more difficult to get rid of.
Felix Geisendörfer 00:20:40 Yeah, that makes sense to me.
I personally don't have strong feelings against ProcFS, but what I would still try to understand, and I don't know if there has been a follow-up comment yet, is what are the concerns around ProcFS?
Christos Kalkanis 00:20:57 So, if we open the issue, Timo made a pretty big comment, but he goes into detail about all the issues that we ran, because we did used to have, Eric Memory from Prague, Vietnam.
Initially.
So that should kind of lay…
Felix Geisendörfer 00:21:18 I'm sharing for a second to open it, because we're trying not to fully disclose all the details yet. So let me just see real quick.
Christos Kalkanis 00:21:33 But it's also, like… aside from the issues that Timo has listed there, my other concern, like, has to do with emerging complexity. Like, every… you know, like, proc… using probe to do… to fetch data is never free, right? There are multiple problems. For example, there are blocks in the kernel. Like, if you do it concurrently, you can run into contention.
We have a system called here that's designed for exactly what we want to do, right? Which is read the other process memory. Now, and using ProfitMem for this reason feels like a colossal hack, to me. So, that's the main reason I don't want it to be the default.
if everyone else, so, personally, I don't even care about the fallback. I think… This… it is a security issue, but it's very limited in its implications.
It's a denial of service attack against the profiler and nothing else. There's no privilege escalation, there's no data exfiltration.
So essentially, the attacker You know, it's pretty far-fetched to… the scenario that someone would have to craft to actually exploit this, and for what purpose?
That said, yeah, you know, it's… it is a security issue, so we should document it.
And we should transition to the… Updated system call, once that becomes available.
Felix Geisendörfer 00:22:59 Yeah, when I talked to Alban, one, So the viewpoint that came up where potentially the security issue could matter is, there are a few companies in the world that do run untrusted customer workloads, specifically the hyperscalers do that quite successfully and profitably. And so, if they ever want to adopt something like an eBPF profiler behind the scenes on some of their VMs.
Then they might be worried about this. Now, is that our… target audience for what we're doing for now, that's something we can debate, but I think that's sort of the line of thinking where this could be seen as a legitimate issue that we do need to come up with a solution for. Curious what you think, Christos.
Christos Kalkanis 00:23:50 So, what I propose in the comment and issue is that… let's see how the proc bid mem implementation looks like, right? Like, if there's no significant implementation complexity, and it becomes a configurable fallback, I have no problems with it.
That said, you know.
I don't think anyone at Elastic is going to volunteer to do that work. We have a lot of higher priority issues we're all working with.
So, you know, whoever is interested in this, feel free to open a pull request, and then… yeah, if it seems reasonable, then, yeah, I'm fine with accepting it.
albancrequy 00:24:32 Could this PR be done in public, or do you want to do it in private?
I guess it can be public, because it's just, another implementation of the package?
Christos Kalkanis 00:24:45 Right, yeah, and it's, I mean, it's something we used to have in the beginning. Just go through it a bit.
But maybe…
albancrequy 00:24:51 Yep.
Christos Kalkanis 00:24:51 Like, the way it works now, though.
So one complication is that we have a scenario where the main thread in the process can exit, but the process stays running, right? In that case, proc bid mem becomes unavailable, so you have to use proc bid, task, teed mem instead.
So you're switching to that.
And the same thing is true for the map files.
So that's one corner case, like, we have to take into account now, right? We didn't, like, that wasn't, taken into account when we first, Use profit, ma'am.
Maybe there are other common cases, because we've changed a lot of things about how the process manager, works.
Florian Lehner 00:25:35 Maybe a little heads up.
One reason why we switched to proc, VM Breed is that, we did run into, various numbers of race conditions, like what happens if there are process exits or the thread exits, and, If the fallback will be implemented, there needs to be a way to avoid these race conditions.
And reliable manner, I would say, and that's… that's the bigger challenge.
So, the syscall is really just reliable to, to getting us information that we want, and, doing the reading on ProcPit, or a proc FS is really… Really is, really, really, racy.
Felix Geisendörfer 00:26:24 That's what I wanted to say.
Florian Lehner 00:26:27 So there will be a significant overhead in complexity.
Felix Geisendörfer 00:26:31 Thanks.
reading between the lines here, what about this as a reasonable step forward? I think, Arban, as far as this group is concerned, this is probably, at the end of the day, more a kernel issue than a profiler issue, because it's, like, something that impacts every user of that system call, and so I think… our willingness to just, like, make all the information public is probably less important than the kernels for this, so I would say if the kernel people are okay with this going public, we would be as well. Anybody disagree with that?
I guess not. So, Yeah, basically, I think we're… we're not… feeling strongly about blocking this. We're open to, like, a fixed landing from anybody who wants to make a fix, even so it might be difficult to make a correct fix for the reasons pointed out by Florian and by Christos. But, yeah, I think at this point, Yeah, if you want to see what the kernel… like, basically, where are you with the kernel people, and have they had any opinions on this staying private versus public?
albancrequy 00:27:48 I think the conclusion from the kernel people is, like, it's not a bug, because it's a… there is a… from that point of view, there is a solution with ProcFS or with Pinterest.
So… If you don't want to block, you shouldn't just not use, process VM redefi. That's our opinion.
So, so I don't think there is a problem from that perspective to, To… to talk publicly about it.
Felix Geisendörfer 00:28:25 Yeah, I guess if that's their standpoint, then I guess it's… good to get this information out to the community of practitioners ASAP, because this is impacting a lot of agents that are out there that are doing various sort of observability things, and if the kernel people are unwilling to fix it.
And we are not treating this as, like, a high priority, except for this one potential user group that we don't actually have right now on the Profiler, really. I think we can go public, we're not going to hurt any existing users of the profiler, and future users are welcome to contribute.
changes that will make the profiler hardened against this backdoor of attack, would be my conclusion.
What do you think, Alban? Is that reasonable from your point of view, or…
albancrequy 00:29:17 I'm not entirely sure.
thinking.
I guess from the kernel thing, I would like to… Well, I have a dispatched to, use the flag on the process VM with resources we want for the project.
We can make that, and then, When it's available, we can make use of it in OpenTelemetry.
I'm not completely sure about making the detail of the issue public.
Yeah, I don't know exactly how to… Hypothees.
Felix Geisendörfer 00:30:06 I mean, I'm assuming that even if you make a patch, it's only… would that get backported to lots of older kernels?
albancrequy 00:30:14 That will probably not be parted, because it's, it's kind of a new feature, like, I mean, maybe some distribution will backport it, but not necessarily.
Felix Geisendörfer 00:30:26 In that case, I don't think there's a plausible scenario where people can protect themselves against this, unless we go to literally every user of the system call, tell them about this issue, get them to upgrade their thing in secrecy, and then we release information.
Otherwise, we're just playing favorites to the eBPF profile out here by saying, like, oh, this project gets a chance to… Fix the issue before, and then we go public.
Yeah, seems… I mean, it's your call, ultimately, since you're the reporter, but… I don't see a Bible pastor actually disclose this in a way that everybody gets a chance to fix their stuff.
albancrequy 00:31:07 Yes. But since, from the point of view of our pontametry, it's not a big issue, like, it seems civil case, okay, it's a denial of service, but it's not a huge issue.
There is not urgency to fix it, so we could as well, wait.
Until there is this new feature in the canal, and… At some point.
Felix Geisendörfer 00:31:29 Yeah, yeah, I don't think we want to rush the information out there, it's just if you feel some advantages to making it public at some point, then we don't want to be in the way.
albancrequy 00:31:40 Okay, yeah, I think for now, no urgency.
I would like to have a fix, but it's not… It's not urgent.
Felix Geisendörfer 00:31:48 Okay. I think the only thing that's a little annoying for us as, like, a group is it's been difficult to get more people added to the security advisors than getting visibility to everybody who might be in a position to make changes, but that's something we can sort out on our end, to just ask for more people to be added if there's volunteers to work on this.
Okay, then… let me try to summarize… oh, Chris, let's go ahead.
Christos Kalkanis 00:32:15 Yeah, just to clarify, we'll keep the issue, like, we'll make no public announcements regarding the issue itself, but any follow-up work for, for example, ProfitMEM can happen in public, right? We don't have to… To hide that, because we're providing an alternative way just to read memory from the process.
And assuming it will make no reference to the.
Felix Geisendörfer 00:32:35 Yeah, I think that's fine.
From my point of view.
albancrequy 00:32:41 Yeah, that's good for me as well. So then I can use rapid telemetry as a library with this alternative option for remote memory, and… And then it's fine.
Felix Geisendörfer 00:32:58 Okay, great.
Let me just try to… capture the conclusion. Conclusion is we'll… Keeps, Ebpf Security Advisor… Pretty private.
For now, until… Well, until when, like, until your kernel patch lands, or… I mean, it's up to you, really, until Alban decides.
Besides to publish it.
Okay, this would be my summary. If anybody thinks I missed something important, feel free to edit the doc, or… Speak up.
Any, any more thoughts on this? Or should we move on?
albancrequy 00:34:16 For me, that's good. That's one of the two security issues. On the other one.
there is a pull request that has been reviewed, and I'm not sure what is the next step.
For the… Second security advisable.
Christos Kalkanis 00:34:31 when I last looked at it, so there were some comments there by Tim and Florian. If you addressed everything, Alban, yeah, feel free to ping people again to take another look.
And then when we… yeah.
Do another, another class.
albancrequy 00:34:47 Okay, thank you.
And, you know, there is… There is actually two, pull requests. One is the main thing, and the other is for the, APM interpreter, and this one has not been reviewed.
Okay, so I can ping on the issue as well.
Felix Geisendörfer 00:35:10 Yeah, on the APM interpreter, that work maybe gets superseded by what we were talking about earlier. I don't know what Elastic feels about the APM issue. It's probably you're the only users of it, I think, right now.
Christos Kalkanis 00:35:22 Yeah, if we have a better… like, we're also looking at it as a transitory mechanism. If a better mechanism manifests, we'll switch to it.
albancrequy 00:35:35 Sorry, I'm not sure I understood, but do you mean you have a different protocol to communicate, or…
Christos Kalkanis 00:35:44 Datadog, there are proposals that we're now discussing, so we could be moving to them. The current APM interpreter was, essentially a protocol that we designed in-house at Elastic in very little time, mostly, like, a proof of concept.
So, it's… I don't think it's specified in OTIL in any way, but… We are currently discussing alternative proposals, and it looks like those will be the way forward.
Felix Geisendörfer 00:36:18 So I guess in other ways, words like this is probably not going to be a priority for anybody to work on, and it's probably going to sit around until we have some new proposal, aligned on, and we… I guess, Evo, for you, the ask is to make sure that whatever we're designing is not vulnerable to that, attack, and I guess, if you haven't already been added to those advisories, we can add you to make sure this knowledge is in your head.
Ivo Anjo 00:36:46 Yeah, I think the fallback would work for that one, but yeah, I can give another… I saw the very, very early discussion on the advisories, but I didn't see the updates, so if you can add me, I can give another pass and make sure that it still makes sense.
Felix Geisendörfer 00:37:10 Okay, Abund?
That makes… that works, or what do you think?
albancrequy 00:37:15 Yes, that's good.
Felix Geisendörfer 00:37:16 Oh, wait, with maybe… I think when we discussed in person, you mentioned that you were interested in maybe an option to disable the APM thing that's in the profiler right now. Is that needed?
albancrequy 00:37:32 I'm not sure, but I think there is already an option to disable specific.
Felix Geisendörfer 00:37:35 Oh, okay.
albancrequy 00:37:35 Yes.
Felix Geisendörfer 00:37:36 Okay.
Okay, so if that option exists, then I think we're good.
Okay, do we have Alexi here now?
No? Does anybody have contacts on his stuff? He said he was gonna join a little later. Maybe we'll just, Give a hat to… the other main agenda item we have, and see if Alexei shows up later. Or maybe, what's this reference resources thing? Let me just…
Florian Lehner 00:38:10 reference resources, I did not put my name on it, but… I'm involved in it.
The idea is that we get dictionary-based references, like we do for other attributes. The discussion is currently if it's fine to just add a reference to any value.
And, like Tigran said here in the second comment.
or if we have a dedicated, any reference value, like in this PR.
Yeah, as far as I can tell, TC is not… does not have a unique opinion, and depending on who you ask, it's a different answer.
So the discussion continues at that very moment.
There was also the… discussion to require us to introduce capabilities first into OTEL.
Meaning that every hotel signal will send a capability request to the collector. Collector answers with, hey, I'm supporting this capability, for example, dictionaries, yes or no, and then the signal has to adopt accordingly, so, for example, providing any ref with a dictionary order, or with our dictionary support.
Would add a ton of complexity, not only on us, but also on the other signals, like logs, metrics, and traces.
And, my current understanding is that this capability request is not enforced on us might change the opinion. I think there are people in KubeCon at the moment discussing this, but, yeah, I don't know what corn status is, so… Yeah, I'm asking to get a… unified TC feedback on how we can get references on the… on the resources.
Yeah, that's… that's the part at the moment.
Felix Geisendörfer 00:40:22 Okay, thanks for the update. I think, Naev and I have a little bit of updates on this as well, unless anybody wants to follow up on what Florian just said or asked questions.
If not, then, yeah, basically, Nef and I have been working on benchmarking for this.
And we made some progress, and it has been setting up a workload on Kubernetes that's producing, sample data that we can use, and I've been working on a tool to ingest that data, and then, imported using the new protobuf definitions that, basically from your pull request for AM, and then, basically… mutate the profiling data in the new formats that we want it to be in, so we can see the before and after impacts on size. We did make some good progress today, but also ran into some issues along the way, so we're not quite ready yet to share results today, but we feel pretty confident that we'll have some next time around.
Yeah, Naev, do you want to add anything to that, or is that… Sufficient.
Nayef Ghattas 00:41:33 No, I think that's sufficient.
Felix Geisendörfer 00:41:36 Okay.
I'll just take note.
Nayef Ghattas 00:41:53 Maybe I can add a bit more context on the benchmarking setup that we have. So, essentially, it's an EC2 instance with a Minikube, configuration, and it's running all the OpenTelemetry demo environment, which has, like, many languages and databases and processes that are doing very different things, as well as a Python process that forks a lot.
So that when we start splitting by process ID, we get also… we can see also if we have this impact on the payload size.
Felix Geisendörfer 00:42:36 Okay, that's cool. Is there any load on this, hotel demo, if you hooked up load chain?
Nayef Ghattas 00:42:42 Yeah, there's a load gen included in it, automatically.
Felix Geisendörfer 00:42:45 Okay, sweet.
Yeah, any questions on this, or concerns with this benchmarking approach?
But yeah, the idea is to basically reproduce data once, and then we'll have a tool to encode the data into the different proposals that we have, and we might even be able to, like, add some flags to tweak data distributions, where we're like, oh, what if there was a lot more processes by just duplicating some of the data that we have in the original payloads?
So we can extrapolate a little bit. Yeah, sorry it's not ready yet, but we've been working on it, and should have it ready next time. Then, is Alexi here now?
Alexey A 00:43:35 Yes, I joined the story.
Felix Geisendörfer 00:43:37 Okay, cool. Just in time. We are now on your agenda items. The first one would be write the consistency check tool, initial PR send, number 12, What's the latest on this?
Alexey A 00:43:52 I… there's not a lot of updates. It's been a very busy time at work, but I saw people have comments, and I basically need to react to those, and Yeah, I think… I think one… one thing that I still… I need to add, like, code-wise, like, one of the… more major thing, I guess, is, this optional checks for… we added documentation in the format that we like… Dictionaries should not have duplicate values or orphan values.
And I plan to add it as optional, but the… It's not, like, super tricky, but, like, this requires comparing values deeply and recursively.
And given how versatile What they'll attribute is… is, like, I… I've been procrastinating a bit because I don't know, like, exactly what's the best way to… to write this, because… Conceptually hotel attribute… is basically can represent JSON. It's like, it's a recursive tree-like data type.
And I think we currently allow it, and I don't think… maybe someone can help me, like, are there common primitives somewhere in, maybe, hotel repos for maybe serializing hotel attribute value to a string, and then I could use that to… to compare, because, like, I need to recursively compare identity, and it's not like… It's not, like, super tricky code to write, it's just… going to be a fair bit of code, I guess.
But maybe, maybe initially I will add something that supports just primitive attributes, such as, like, primitive types, such as, like, either the value of a primitive type.
Such as, like, integer or string, or arrays of primitive types, and then we can expand it as we go forward, if it turns out that this is not sufficient.
Felix Geisendörfer 00:46:11 Would the GoPackage CMP comp do the trick for this? Because it can recursively compare data structures and give you a nice diff?
Alexey A 00:46:22 That's a good point, I'll take a look.
Felix Geisendörfer 00:46:32 Thank you.
Alexey A 00:46:33 Yeah, maybe. I don't remember how well it deals with Protobuffs.
Felix Geisendörfer 00:46:38 I think it's fine, I think it just looks at the public struct fields, which… It's not going to see the private ones. I don't know if it complains about not being able to see the private ones, but yeah, give that a shot. I think that would be my first instinct. If not, I suspect there's probably some code somewhere in the collector that can print out attributes. I think, Neyev, didn't we just look at something like that?
Maybe you can drop the link to that code as well.
Alexey A 00:47:06 Collector would be PData, probably.
Felix Geisendörfer 00:47:09 Yeah, but PData is just, like, another struct grabbing the protobuf struct, right?
Alexey A 00:47:15 Okay, so I can create AP data from…
Felix Geisendörfer 00:47:19 Yeah, you can unmodule into P data, I think, pretty straightforwardly.
Alexey A 00:47:23 Okay.
Felix Geisendörfer 00:47:25 Yeah, Nirv, can you drop those, links that we had?
Nayef Ghattas 00:47:29 Yep.
Felix Geisendörfer 00:47:41 Okay, I'll let you update the document. Cool, okay, then thanks for the update on that. Should we move on to the next one?
Alexey A 00:47:48 Next one is done. I think it's merged.
Felix Geisendörfer 00:47:52 I like the sound of that. Verify dictionary guidelines. Awesome.
Did we already remove it? No, I guess we should remove it from the action list up here.
Unless this one right?
Nice.
Then… Verify start timestamp duration conventions.
Alexey A 00:48:36 Not done, but… No, not done. We'll, we'll, we'll do…
Felix Geisendörfer 00:48:43 Okay.
Alexey A 00:48:44 It's, This one and the next one, also.
Felix Geisendörfer 00:48:59 Okay, docurlprop attribute.
Alexey A 00:49:05 No, same, not done yet.
Florian Lehner 00:49:08 I think I've covered this with my PR.
Alexey A 00:49:12 Oh, yeah, I see you sent a pull request, okay.
Thank you, Lauren.
Florian Lehner 00:49:17 It was just done today, so, yep.
Felix Geisendörfer 00:49:23 Then should we remove this as a duplicate?
Florian Lehner 00:49:28 Because I think it's…
Felix Geisendörfer 00:49:30 it's pretty likely that your PR's gonna land, and it has more things, so I think… Then let's close this one.
Alexey A 00:49:43 Oh, you're also adding, drop frames, keep frames, okay.
Florian Lehner 00:49:49 Yeah, I need them for the conversion back and forward, because for PProf, it's important to have them, and I want to have.
Alexey A 00:49:57 Yeah, that… Yeah, that's a good point, we forgot about those, but yeah, we need them as well.
Felix Geisendörfer 00:50:04 Okay, awesome.
Then, yeah, any, any more thoughts on this? If not, we can move, finally, to the first non-review action item, agenda item, and only agenda item for today, so we have 15 minutes for it.
Okay, let's do that. So, we have this big pull request here, to improve the stack traces for Ruby, and Dale said he might be able to join, I don't know if Dale's here.
dalehamel 00:50:39 Hey, I'm here.
Felix Geisendörfer 00:50:41 Awesome! Yeah, first of all, thank you so much for all the work on that, and I guess, probably for this group, the main ask is to review this, but maybe you want to talk a little bit more about it before we discuss who can help.
dalehamel 00:50:54 Yeah, so actually, right after I, filed this, I noticed, as I was reviewing it myself, that the line numbers, for the leaf frames are, in some cases, incorrect. So I actually have a fix for that.
But after a bit of back and forth, it looks like Timo has a PR943 that's a draft right now.
to basically make the frame struct, variable length. And that's required because I need to push an additional value from BPF to be able to get those line numbers, correct.
So the, the… the fix is essentially to just pushes additional value and then use it within the interpreter. So the majority of the PR remains the same. It can definitely be reviewed, but I don't think it'll be able to be actually landed until 943.
Is landed, so that we can incorporate that fix and make sure that all the line numbers are correct, because we won't want to regress that on main.
But yeah, as for the PR itself, it just… it extends the… the behavior of the existing Unwinder and existing interpreter.
The biggest difference is that there's this concept of a callable method entry in Ruby, and it adds support for that. So there was previously, everything was treated as, like, a bare instruction sequence. This does the same sort of lookup that the Ruby Ruby… Sorry, this is a bit of an overloaded term. RubyVM, I was gonna say Ruby Interpreter, does when it, when it's collecting a profile.
So on the collection side, we build the buffer the same way that Ruby's own RBProfile frames function does, and then there's an analogous call, where you go and symbolize that.
And that's what we're doing in Go, so basically just trying to copy exactly what the Ruby, VM is doing. I think someone has their hand up. Is it Alexi?
Alexey A 00:53:02 Yeah, just as a quick note, when you said the wrong line numbers, this probably doesn't apply here, because Ruby is an interpreter, and I assume that, like, stack unwinding is also using the interpreter stack, but when reviewing stack unwinding for a profiler here internally at Google, one thing I saw, like.
Return addresses on the stack will point to the next instruction after the call instruction, and one thing we do in almost all our profilers is subtract one, because you want… you want the address to be within the call instruction. Otherwise, especially for C++ programs, the next instruction will be like, something after the call, and with inline debug information, especially, it can, like, it produces very odd stacks. I almost, like, I already, like, know how they look, at least for our C++ code, when someone forgot to subtract one from the return.
dalehamel 00:53:52 Yes.
Alexey A 00:53:53 But I think it doesn't apply here, probably.
dalehamel 00:53:55 Yeah, no, in this case, basically, There's two instruction sequences. There's one that's accessible directly from the Rubio's concept of control frames, and that's the one you actually need to use in order to get the correct line numbers. And then if there's a callable method entry, that has an indirection to a different instruction sequence, which is the one you want to use to get the the symbolic, like, stringified label. But then, for the leaf frame, it seems like you need to actually have this original Actually, I shouldn't just say for the lead frame, it looks like it did change for some other ones as well. But all this to say, you need the control frame instruction sequence in order to get the correct line number, deterministically.
So basically, we need to be able to push an extra value.
aside from that, the logic is unchanged. It uses the existing GET line number helper within the Go code.
Felix Geisendörfer 00:54:58 Got it. Cool. I guess that the main question still is, so, do we already have somebody who has such, like, future capacity to refuse this, or is that still what we need here?
Christos Kalkanis 00:55:14 Yeah, so both me and Florian will review this. Timo has… so this is the second, kind of, big pull request. Also, major refactoring, in a way, that Timo is doing. Like, the first one is also in a review, and he also changes frame representation and parts of the process manager.
So I've been reviewing that for the last week. I found a regression there.
So, the problem with Process Manager, because I referred to it before when talking about the average and complexity of propit mem, is that it's so easy to introduce race conditions there, and it's, like, we haven't done a good job of creating an isolated subsystem that can be tested in isolation very well, so testing is always a problem.
And it takes some time.
So I would say that I will wrap up the review of Timos' first PR tomorrow, and then I will spend part of next week the reviewing these, but it's still in draft, so I will, like, I'll ask Timo if he's finished with it. So once he's finished, then, yeah, both me and Florian will look at it.
dalehamel 00:56:20 And then, one other thing I just wanted to add is I actually have additional work based on top of this that I've cut out, It's already a big PR, I didn't want to submit it all In one go. But assuming, 907 lands, I plan to follow up with two additional pull requests. One is to add, garbage collection frames, and I filed an issue on the hotel repo to kind of describe the motivation for this.
And then the other one is to add support for, Ruby, JIT, Currently, if you have, YJIT or the more experimental ZJIT enabled, it just completely breaks all Ruby profiling. And so I have a fairly kind of quick and dirty workaround, for that.
So yeah, if this lands, then those can subsequently land, and if all of that lands, then we'll actually be pretty close to being on Main, which would be awesome.
Felix Geisendörfer 00:57:19 Really cool. Thank you so much for these contributions.
dalehamel 00:57:23 Yes, it's.
Felix Geisendörfer 00:57:23 Awesome to, to, to review.
dalehamel 00:57:27 It's been an awesome project to work with, kudos to everyone. The existing Ruby interpreter was already in decent shape, it just needed a little bit of reworking.
Christos Kalkanis 00:57:37 I have a question for you, Dale. We had an internal chat yesterday at Elastic about introducing code owners for interpreters, because now we're starting to get the full requests like yours, and you're an expert on the code that you wrote, and I'm assuming also part of the Ruby virtual machine.
So how would you feel about that?
dalehamel 00:57:59 Yeah, that makes total sense.
Yeah, like, it's not really tractable for the project maintainers to have the… the… expertise of every VM and language, right? So, absolutely, Yeah. Makes sense. And then at Shopify, I'm not part of this team, but we actually do have a team that's a bunch of, like, Ruby slash Ruby contributors that their entire job is to just hack on Ruby, so I have access to the experts if I need to talk to them.
Christos Kalkanis 00:58:31 Okay, great. Yeah, so the idea is that whenever, you know, changes take place in those subsystems, you get automatically notified Yes, but what we also want to have, however, is that we're not blocked, because, you know, we may designate a person to be a code owner, but we don't want to, let's say, because someone doesn't reply, right?
For a week or two. We want to, as maintainers, we wanna be able to have the option to move ahead if there is, you know, silence, basically. So, and I think…
dalehamel 00:58:58 Yeah, of course.
Christos Kalkanis 00:58:59 This is an open question, like, if it's possible on the auto end, it's probably some bit of configuration that needs to happen.
But we'll figure it out.
dalehamel 00:59:08 Yeah, like, we have our own needs to continue to maintain this, and if someone, you know, the goal for upstreaming is so other people can take advantage of it, and if someone finds a bug or a limitation, it's probably something that we would benefit from, and we can definitely justify.
Felix Geisendörfer 00:59:23 you know.
dalehamel 00:59:25 Being… being able to continue to own the code.
We're continuing to use it, of course, so…
Felix Geisendörfer 00:59:41 Awesome, thank you so much. All right.
dalehamel 00:59:45 Cool, so I'll keep an eye out on 943 there, and in the meantime, like I said, if someone wants to take a look at 907, it shouldn't have significant changes, and the changes to fix the line number are already detailed in a comment, so…
Felix Geisendörfer 01:00:05 Great.
Awesome. Any more thoughts on this? If not, we have, about 4 minutes left for last-minute topics anybody wants to bring up, or… Four minutes to get back to our schedule.
Lexi is taking this end up.
fruit?
Alexey A 01:00:27 Just a quick note, felix, I don't think CMP works, because I think CMP compares values pairwise, and I need some kind of, like, a lookup table.
Otherwise, like, trying to compare… Things, lookup-wise, would not be efficient.
like, pairwise.
Felix Geisendörfer 01:00:49 Okay.
Alexey A 01:00:50 But I'll take a look. Maybe CMP has a way to serialize values to a string?
Or something like that.
Felix Geisendörfer 01:00:59 I mean, just, like, a really stupid idea. Couldn't you just chase and stringify the whole struct and just compare that?
Yes.
Alexey A 01:01:07 Chase mushrooms Okay.
Like, I was also using, using… simply using Go.
Felix Geisendörfer 01:01:17 Fifth?
Alexey A 01:01:20 Okay.
Felix Geisendörfer 01:01:27 Okay.
Any…
Jonathan Halliday (IBM) 01:01:30 Other topics, questions?
Thanksgiving, I think. Do we want to go ahead with it anyway?
Felix Geisendörfer 01:01:40 I think that there are a bunch of Europeans here who do not… celebrate. I would certainly be willing to join and show the benchmark results. I don't know if anybody feels strongly about canceling. We would be, of course, understanding that some People who do, honor that holiday would not show up.
I guess…
Jonathan Halliday (IBM) 01:02:07 Yep, let's keep it.
Felix Geisendörfer 01:02:09 Yeah, because I, I mean, I know it's a big one in the US, but, like, there's a lot of holidays that also, like, in Europe that fall on our meeting days, and I think we would have too many cancellations if we did that.
Jonathan Halliday (IBM) 01:02:25 Another quick one, do you know if Marcus is running?
OpenJDK Virtual Serviceability Meetup this year.
Felix Geisendörfer 01:02:33 I do not know, but I will ask him, and I think he'll be happy to hear that question, and I would expect him to host it again, but I'll confirm with him.
Jonathan Halliday (IBM) 01:02:42 Alright, thanks, Felix.
Ivo Anjo 01:02:44 I know the answer to that. He's actually running a survey on, like, the best dates, so he does want to, run it. I will, Let me get the link, just one second… Mmm…
Jonathan Halliday (IBM) 01:03:05 there still exists, I think, A slack for it.
I haven't seen anything on there, so it might be a good place to post that.
Ivo Anjo 01:03:12 Oh, you just posted that yesterday on the JDK… I think I saw it on the JDK Mission Control, maybe not on the other one.
But yeah, I'll drop a note to Marcus.
And the link is here.
Felix Geisendörfer 01:03:31 For those of you who might not be familiar with this, this is a meeting organized by my manager, Marcus, who is getting together people who work on Java observability or serviceability, whatever you want to call it. So, a bunch of runtime experts for the JVM usually attend and share ideas on improving the visibility into Java, so if that is interested… interesting to anybody, feel free to ping Ivo or myself to get more information.
As well.
Jonathan Halliday (IBM) 01:04:00 Yeah, it would be good for one or other of us to… offer a session on this, I think.
get, get some more Java eyes on it. I know.
Some of the async profiler people, Already keeping an eye on it, but, We don't have a lot of overlap with the people who do JVM stuff.
Felix Geisendörfer 01:04:21 Yeah, do you think we should talk about the eBPF profile, or about the OpenTelemetry signal, or both?
Jonathan Halliday (IBM) 01:04:28 I think certainly about the signal.
Because I think we, in the same way that we want to be able to convert PROF, we want to probably be able to convert at least a subset of JFR.
I don't know if… Java people seem to live in a little bit of a bubble where JFR is all they care about, so giving them some exposure to ePPF might actually be good, in terms of bursting that bubble, but I don't know.
How, welcome that will be.
Felix Geisendörfer 01:04:57 Yep.
If you want to put something together, feel free. If not, I could also volunteer. If not, we probably… maybe Ivo, I think we have a bunch of people who'd be willing to speak at that summit to talk about that.
Jonathan Halliday (IBM) 01:05:11 Great, we're over time, I've got to jump to the Java call, which is up next.
Felix Geisendörfer 01:05:15 Yep.
Jonathan Halliday (IBM) 01:05:16 See you next time.
Felix Geisendörfer 01:05:17 Thank you, everybody, for attending and all the great work.
See you?
Ivo Anjo 01:05:21 Everyone.
dalehamel 01:05:22 Thanks, everyone.
