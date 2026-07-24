SIG: Profiling WG
Date: 2026-07-23
Duration: 72 minutes
============================================================

## Zoom Recording Transcript

Scott Gerring 00:02:28 Hello?
Florian Lehner 00:02:31 Hello, hello.
Scott Gerring 00:02:34 Are you enjoying not catching on fire as soon as you go outside at the moment, Florian?
Florian Lehner 00:02:40 Yeah.
Yeah, yeah.
A lot of change.
Scott Gerring 00:02:49 Some rain would be nice.
Nayef Ghattas 00:03:01 Hello?
Florian Lehner 00:03:03 Bonjour.
I will put, agenda in the document in the… Zoom chat, so everyone can, list them as attendees.
Otherwise, I suggest to wait 2 more minutes, then we have 5 after the clock, and then we can start.
If no one speaks up, I will try to do a moderation.
I think that's not a usual problem, no one speaks up.
Ivo Anjo 00:04:48 Hello.
Florian Lehner 00:04:50 Nope.
Okay, then I will try to share my screen.
And you should be able to see my screen now.
Yeah, plusie.
Ivo Anjo 00:05:40 We have your desktop, so I think, but it looks fine.
Florian Lehner 00:05:45 Oh, yeah, Zoom doing Zoom things.
No, it should be a full desktop.
Ivo Anjo 00:05:55 Yep.
Florian Lehner 00:06:05 Okay, then I will try to start.
As usual, let's start with the review of the action items. I did see we have already some action items resolved, comparing to the last meeting, so I removed them from the active action items. I don't… see Alexey in the call. Alexey, if you're here, please pick up.
Otherwise, I did not see any… Work on the offense check for the conformance checker on the… On the, profCheck and SICK Prof.
But, same… Here, in the last two weeks, I did not manage to write the second or the other duplicate checkers.
And, I still have one duplicate checker open PR… Open PR for duplicate checks of mappings.
So if you have time, give a review. I think the last, comment was from Alexey, but if Alexey is not here, I think it does make sense.
Alexey A 00:07:19 I'll actually skip. Sorry.
Florian Lehner 00:07:20 Okay.
Perfect, sorry, sorry. Maybe, do you have an update on the conformance checker for the offense checks?
Alexey A 00:07:31 No, sorry.
Okay, but I think you implemented this. I think we can just, I think this… I think you submitted the PR.
Florian Lehner 00:07:44 The last time I remember was that we split up work. You did one part, and I did another part, but I would need to go back exactly what we agreed on, but I just remembered that I need to do the duplicate checks for the conformance checker.
Alexey A 00:08:01 Yeah, but I think you also… you actually sent a pull request for the orphan check as well. I, I reviewed it last week.
Florian Lehner 00:08:09 Okay, cool. Okay, then, okay, then I will double-check before I, remove it from the actual items list, but then this seems to be resolved. Cool, yeah, thank you. Yeah, but the other part, I did not have time to implement it.
If there are no comments on the ProfCheck tool.
I suggest to go on.
with, probably Nayef and, the document about, OTLP version in payloads. Do you want to talk about it now, or,
Nayef Ghattas 00:08:48 I did add an item next in the agenda, so I think we can talk about it at the end of the meeting.
Florian Lehner 00:08:54 Okay, then, then I will go on.
Next item also, Alexey, the… dependent PR4965 is merged, so I think this can be now implemented.
Alexey A 00:09:11 Okay, I'll… I'll take a look.
Florian Lehner 00:09:16 Okay, cool.
Denton going on, Shivan Shu, if I pronounce the name correctly. I don't see… Any attendance in the… List.
Can someone say something about this PR that is related to this topic, other than, hey, I have looked at this PR?
Namespace, okay, we already closed it, Okay. Yeah, I know that we have an open PR, probably a follow-up directly.
Yeah, here.
That is related to this?
Yeah, thanks, Roger, for the initial comment.
But I think if the original auto is not here, and cannot… say something I would… I, suggest to go on.
Roger Coll 00:10:28 Yeah, I would wait for his reply on the beer. I will…
Florian Lehner 00:10:32 Yep.
Christian Simon 00:10:33 I think if I understand the problem correctly, it is about when… A nested namespace has other child namespaces, and that is quite common with Kind. You might run, I guess, 3 Kubernetes nodes in Kind, and currently, I guess we have matched the inode of the PRD namespace, but obviously the child ones wouldn't match.
And therefore, I guess it wouldn't, I don't know, maybe work as people would expect if you run that as a daemon set in such clusters.
Frederic Branczyk 00:11:05 And then this kind of thing goes beyond profiling, right? Like, I think people are, like, people ultimately want a true PID, right? But, like, the point is, there are multiple that are true, potentially, right? And I think… I think the… that… yeah, I don't know, the data model is just not quite right, or we need to allow multiple PIDs or something. I don't know, but, like, I think this is… I guess what I'm trying to say, mainly, is this is more… more than just about profiling, really.
And I wonder how other signals think about this.
Florian Lehner 00:11:43 I think we are unique in the sense that we have a daemonset view, which most of the other hotel components don't have.
Frederic Branczyk 00:11:53 about, like, Baylor or something?
Florian Lehner 00:11:56 That's a question OBI needs to answer, I don't know these details.
To be honest, to… I don't know these details exactly to give a… Proper answer on this.
Frederic Branczyk 00:12:15 I guess there's even, more generic thing, right? Like, where multiple values are true for one entity, or whatever, or one data point, I guess, right?
like, PID happens to be one that, you know, comes… came up here, but, like, you could think of potentially other… other cases where this might be true as well, where multiple values are correct.
Alexey A 00:12:49 file, but… Can be also different, for example.
Between namespaces.
Frederic Branczyk 00:12:56 Sorry, I didn't catch that one.
Alexey A 00:12:58 File… file paths, yeah.
Frederic Branczyk 00:13:00 Exactly.
Alexey A 00:13:01 The file can be mounted In… at one path, at the root names… at the system namespace, and… And… At a different path in the container namespace, or not mapped at all.
Christian Simon 00:13:18 I guess it is true that the user space of the eBPF profiler runs in one PID namespace, and I guess that would be the maybe true one, but I don't know.
If that should be.
Frederic Branczyk 00:13:33 That would mean that, you know, PID1 within the container is always false, which I think there's plenty of systems that don't necessarily make that assumption. And you can't find out your true host PID from within the container, which is kind of the whole point, right?
So, yeah, I don't know. I'm not saying that I have any of the answers, but I'm saying I think this is, like, not just a profiling problem, and not just a PID problem.
Christian Simon 00:14:01 No, I agree.
Florian Lehner 00:14:03 Yeah, I think, Roger left a good comment on the PR.
I think it was on the name… Pit Translation PR.
That we could use a BPF helper and figure out, hey, is this the root C group?
Where we are in… if I remember correctly.
Roger Coll 00:14:27 Yeah, that is for the C group, but then on another PR that I'm trying to… basically remove the host PID and use the mount… use a mounted profile system.
There, I… I suggested using a VPF function to get, let's say.
the host PID, and use that to get all the offsets, etc, etc.
But probably in the PR that we are mentioning, the issue is that, In kind, there's no concept of host PID, let's say.
You can run a pod with host PID, but you cannot run a… kind cluster as a host PID, because the cluster has its own namespace.
And… For me, it doesn't make sense, actually, running as host PIV in kind.
Because it… it's not a feature that it has itself.
That's what I'm trying to suggest in the… in the PR.
Florian Lehner 00:15:33 Yeah, sounds reasonable. I think we… there will be a lot more technical discussions in the PR, the follow-up PR.
I think I will just link it here.
So, if… Everyone that is interested with the follow-up discussions can chime in.
Okay, any other comments on this topic?
Otherwise, moving on to the next one… I'm happy to see the memory profiling proposal from Scott and Nayef.
I just had a quick look, so I cannot speak for it.
But I think it's best, if one of you probably… Talks about us, give us… an intro…
Scott Gerring 00:16:48 Sure. So, it's a reasonably long proposal, I apologize, I guess that the meme is that I didn't have time to write a shorter letter, but the mechanism is basically that we want to hook something in user space, so that we can have a sampled point to let us grab allocations, not every allocation, but, you know, a geometric distribution around some size. The other allocators that do this sort of thing, like TC Malloc and JEMALIC, use half a meg, so we've kind of started there.
The proposal itself is focused on the USDT interface back into the profiler, and it doesn't really overly specify how the sample points get there. I've linked what we've been doing in Libdatadog that has some ideas about that.
there's different stuff to play there, play with there, but I think… From the profiler perspective, it should really be, like, this is our contract, there's kind of, like, this muddy, hard part over here to end up with the sample points, and maybe in the long run, we even end up with them upstream in some of the more interesting allocators, like JEMALIC and TC Mallik, where they already have sampling infrastructure in that fashion.
And then there's pulling that through into profiles, out onto, onto the wire.
There's a sample PR in there as well that I've staged against the Datadog fork, just because it's easier for us to dog food internally, but I can rebase it pretty quickly. I would really like to be able to stack it on top of your custom probes work, Florian, but I think you're about to head out for a bit of a break, so it's probably better that we spike that one Till your back so it doesn't haunt you in your absence.
Florian Lehner 00:18:23 Trying to land it.
Scott Gerring 00:18:26 I chucked all comments on it just now, with the memory profiling hat on.
Florian Lehner 00:18:30 Some of the bids.
Scott Gerring 00:18:31 Where there's, like, maybe a bit of a mismatch.
Florian Lehner 00:18:34 They kind of be.
Scott Gerring 00:18:35 Interesting ones are that You would need… For a memory profiler probe 2 attachment points, you want the.
Florian Lehner 00:18:42 Oh my gosh.
Scott Gerring 00:18:43 side and the free side. And on the free side, you also don't want to unwind, I think, because it.
Florian Lehner 00:18:49 I'll tell you.
Scott Gerring 00:18:49 pretty much, really. But I don't think these are big deals, like, it's just, it's some detail. And hopefully it's another useful… Example of the abstraction that you can use to shape the abstraction, potentially.
Florian Lehner 00:19:00 Yeah, I think I answered already on the PR, and the API already covers such a case as for the off-CPU profiling, where we have one probe that triggers… is triggered on the scheduler event, and then writes something into a map, keeps the information in the map, and at some other point, a second probe is triggered that is, fetching the information from the map, and then do stack unwinding or not, depending on the… on the decision. So, we can already do this.
Scott Gerring 00:19:32 Great, I'll check it out. And obviously, I've been messing around at the edges of this repository a bit with Ivo, so I've got a bit of familiarity here, but really, all feedback is very much appreciated on that doc, and also when we've got a bit further along on the code as well. That would be really great. So if you folks have time and you're into allocation profiling.
Have a look.
Frederic Branczyk 00:19:53 One… so I took a quick pass over it, and maybe… maybe I missed this, but, like, one major topic that I don't think I saw, in it so far, is basically what does the… what is the thing that actually tracks the live allocations, basically, right? Like, basically, there are, like, basically two paths that one could go with this, and I think this needs to live in the allocator, but curious if you've thought about this more.
Scott Gerring 00:20:27 So the way we've done it on the USDT interface is that you basically just return the address in both cases, so you have a sampled allocation, you pick it up again on the free side.
The way that we are doing it in the user space code is one of two variants. In the ARM64 variant, we use pointer tagging, which is… seems like kind of happy magic that is going to be pretty effective if we don't discover that other people twiddle all of those high bits for other purposes.
we'll see. I think this is kind of like, let's see how it shakes out, because it's nice, right? Like, you have no cost, you have the pointer in front of you, you don't have to look aside somewhere.
For x8664, we're doing something that is moderately gnarly, where… we basically bump the size of the allocation when we're going to sample it, and we make sure that it's not aligned to a page boundary. And on the free side, we say, if this pointer isn't page-aligned, we can read before it, it might be a sampled allocation, and we look for the magic thing. And then there's some funny stuff that we do Where you have to meet a certain alignment, which makes it gnarly.
But so far, so good with the dog fooding. I'm kind of wondering with the proposal.
if we want to talk about this stuff or not, I think it makes things a bit more complicated if we just kind of focus on the USDT interface back and say, we leave this up as an exercise for the reader.
It obscures…
Frederic Branczyk 00:21:53 I think it's pretty important because it is an explicit interplay with the allocator or not, right? So I think, it's… I think it's worth… worth sketching out, and I think the… in my mind, the most unknown one in all of this is TCMAL… Sorry, Mimaloc.
And I want to say we've looked into meme analog before, and we're thinking about a similar approach to what you just described, with the resizing of the allocation, and I want to say we found some reason why this wasn't a good idea.
Did you… did… were your experience, were your experiments with me malloc, or…
Scott Gerring 00:22:38 I've been using GLIBC Malloc, TC Malloc, and JEMalik, but that's a good hint. As a kind of an aside there, one of the other folks in the profiling team here has opened a PR against Mimalek to add sampling hooks into it in the same fashion as TC Malik and JEMalik do, which would be super nifty. Yeah. To my light, kind of.
a high-level mental model, it would be optimal if the ones that already have a sampling path just whack the USDTs in it, because they all sample in the same fashion, it's always geometric with some mean, and that way you benefit from the bookkeeping they're already doing to track the matched freeze, so that the cost is amortized a bit more effectively, but… Yeah, just this slide.
Frederic Branczyk 00:23:16 I'm curious whether the Memalloc folks are gonna be happy with this, because they put so much work into that, the, like, average path uses a single instruction, right? So, like… I'm not sure how happy they'll be.
Scott Gerring 00:23:34 I'll find the PR and I'll ping it into the notes later on so we can all subscribe and see what shakes out. But yeah, it's a good hint that we should also check what happens with the bumping in that case.
Frederic Branczyk 00:23:42 I specifically mention it because, like, in the Rust ecosystem, Memalloc is very popular for performance reasons, and it's the one that we haven't been able to, you know.
really figure out for our customers. And we've basically forced customers onto other allocators if they wanted HEAP or allocation Profiling, and… You can get both.
Scott Gerring 00:24:07 Maybe we can also go the other way, and we all just force customers onto our other allocators, but no, I'll have a look at it and see what we can do.
Frederic Branczyk 00:24:14 We've successfully moved a lot of customers to JEMalloc for this very reason.
Scott Gerring 00:24:20 Yeah, we have quite a lot of JMLIC usage internally here, which also makes the surface area for us for dogfruiting a bit more straightforward, but yeah, that's not so helpful for the open source part of things.
Frederic Branczyk 00:24:32 But this is very cool. I'm excited, I'm excited to, be making some progress on this, and I think with the project as a whole, moving towards this, I think we'll have some… Wait behind us to make allocators be interested in this.
Beyond a single company's interest.
Scott Gerring 00:24:51 Yeah, I think that would be really cool, if we can get momentum and use it to impact upstream, so it becomes a zero instrumentation kind of story.
Frederic Branczyk 00:24:58 Yeah, would be awesome. Thank you for this work.
Scott Gerring 00:25:00 Yeah, thanks for the interest.
Florian Lehner 00:25:02 Yeah, I fully agree on that, and, I think with if we land it with custom probes, we can have multiple allocators, maybe specialized for Jmalog, ME malog, so we don't need to find a perfect solution that fits all, but we can have specialized ones, that are dedicated to the allocators, so I'm happy to, really happy to see this, and… Getting formal routes.
Scott Gerring 00:25:31 But yes, tear the document to shreds, please. You all have time.
Nayefuto.
Florian Lehner 00:25:46 Other comments on this topic?
Otherwise, I suggest to move on and hand over to Ivo.
Ivo Anjo 00:26:00 Yes, hello. Since it's been a while since I've talked about some of the context sharing work, and we had a nice milestone that the OTEP was merged for the Dread context.
So, I kind of wanted to, like, drop a bit of an update, basically what it says there. So, now we have both apps merged for the process context and the thread context. We have PRs to implement this in the BPF Profiler. Thanks, everyone, that already gave feedback.
I'd say, like, the… one of the big next things that we're working on is getting the custom labels that, we… We're adapting from polar signals to make it work for Rotel. There's, like, a bunch of work to make it pretty on the library side, and adopt a lot of the conventions from the specs, and then we need to work at the reviving the eBPF Profiler part and getting it upstream.
There… we have PRs, one of them is from Scott here, and the other one is from another colleague at Datadog to, like, start adding this to the Autel Rust SDK.
Actually, someone else opened the PR for Open Telemetry Python, and I have not had the chance to review it, but I want to.
So I think, like, we're slowly getting some traction in the SDKs, and… and yeah, like, overall, we've been, working with this end-to-end data dock, so I think it's, we've… it seems… it seems to be working fine, so I think now is the… like, get it in the multiple hotel projects, and yeah, I think I'm… We're making progress.
Frederic Branczyk 00:27:41 Do we know where we are, with Java? I assume Java's gonna be an important one for everyone in this room.
Ivo Anjo 00:27:50 Yes, that's a good question. I do not know. So, specifically, I had built, a prototype implementation for the process context, so we could kind of revive that and get that upstream, but I think what everyone wants is the thread context, so I think that's the big one that nobody has picked up yet.
Jonathan Halliday (IBM) 00:28:13 So I've been looking at this a little bit. There's an open… Topic on the, discussion forum for the Java SDK people.
About how they would feel about accepting the… Process-level stuff upstream. They're not.
objecting to it, but equally, the line seems to be there's a very, very small number of people learning a recent enough Java to take advantage of it, because the only way it's going to work is with Panama. They don't want to ship a native Binary to do it.
So the… the system calls involved will be Panama, calls.
Yeah, I don't know how much adoption it's gonna get, but I'm happy to work on this, and they don't seem to object to reviewing it and accepting it upstream, so that's the process bit.
The thread bit, I've been talking to some of the OpenJDK engineers.
mostly it's straightforward. The tricky bit is Loom, because virtual threads obviously are invisible to the the external world.
Currently, the way that's done is JVMTI callbacks.
Which is horrifically expensive.
So there's a couple of alternatives, we've been kicking around. One is to use the agent to rewrite virtualfed.java.
to insert.
J&I calls into Mountain Unmount.
And… that's nice in that you only pay the overhead if the thing's active, if the agent's there and chooses to rewrite it. That's because you want it, so there's zero cost if you haven't installed the agent, so that's nice and not terribly invasive. And we can do that without, cooperation from the upstream, from OpenJDK, it's kind of a bolt-on, so it would be possible to put that into the Java SDK agent code, which is already rewriting various things to instrument them.
The other way we've been exploring is… Potentially to take advantage of, interspecial, for the… the Java people who know what that is, it's down in the C++ bit of the JVM, and it's basically, assembly stuff that gets called to do black magic when, virtual threads are… Context changes occur, so when a virtual thread mounts to the carrier and unmounts.
So Andrew Haley, who's one of the OpenJDK committers who worked on Loom, has been… hacking together an assembly-level thing, he, he got interested in it and was like, how efficient can I make this?
So he's been, playing with that, and he has sent me a PR that I haven't had time to look at yet, because I only got it last night.
Evaluating that is another alternative, and if that works.
And if the OpenJDK people, We'll take it, then that's by far the most efficient route to getting this in.
Because then, you know, there's a handful of assembly instructions that will deal with the TLS switch.
So yeah, I'm… I'm kind of… low-key on this. I'm aware of the options, and I'm working towards implementing some of them.
Florian Lehner 00:31:52 Cool, yeah. Amazing.
Thanks for the great work and having the overview on this part, Jonathan.
That Java and Oracle world is really huge.
Jonathan Halliday (IBM) 00:32:04 Yeah, so I want to get some benchmarking done of the alternatives, and then I'll write up a kind of summary document, a proposal, and circulate it between us and the Java people, and potentially the Oracle people.
Florian Lehner 00:32:18 Cool, thank you.
Yeah, my hope is that, with the official release of the OTE Proto, that includes now the oil process context, that, adoption will be easier for more people.
So happy to see this now going… faster and more easy. And thanks, Ivo for all the months of work getting… trying to get this done and merged. Was a long… was a long run.
Anything else?
under… on this topic, Otherwise, I'm suggesting or handing over to Nayef, and auto-contribution and security implementations.
Nayef Ghattas 00:33:15 I started talking, but I was muted.
So, there's an issue that, has been opened, and the Open Telemetry Collector releases a repository to add the eBPF Profiler to Contrib.
And this, this is making me slightly uneasy in terms of, in terms of security, and I was sort of… my goal is sort of to solicit feedback from everyone here.
See what all the others think on this before, discussing this further with, other folks on the… on the collective sig.
So, I actually wrote a very quick, doc on this. Maybe I could… I'll quickly share my screen, or you could share it as well.
Oh, I'll let you share it, it's okay. So it's a very rough, draft, but essentially, right now, the eBPF Profiler runs as privileged on Kubernetes workloads when it's deployed, with the Open Telemetry Helm chart or the Open Telemetry operator.
And this means, from a security perspective, that it bypasses all container isolation, and there's no access control mechanism that applies to it. It can do whatever it can.
On the other hand, the contribution mission statement is to have all the components from the collector, repository, and contrib. So, this includes open source and vendor, supported components.
And the recommendation is to never run this distribution in production, because the security best practices is to limit the amount of components available in the collector before deploying it. In practice, however, users rarely ever want to rebuild their collector, so they either end up using Vendor distribution, or contribib, for practicality.
So this puts us in a place where users will, by default, be able to, and will likely do run a single collector process that runs both the eBPF profiler alongside other components, including network-facing receivers, extensions, and any other constrip component. And any RC and any one of them could inherit, like, the permissions of the profiler and lead to host-level components.
So, we looked at what we could do to restrict the profile of privileges in an easy way by default.
So we already have a PR upstream, that we're iterating on.
to remove privileged and replace it with another limited set of capabilities using Linux capabilities. So the minimum set we found is host PID or a host-level proc mount, like Rogers PR is doing, and all the capabilities that I listed in that doc, so BPF, Performance, etc.
The issue there is that all those are required, and the profiler doesn't run without them, and it's not easy to remove one of them without affecting the features that the profiler provides. But at the same time, just host PID or the host-level proc mount and sysp trace grants full read and write access to the entire host file system.
via the proc PID root file system SIM link, as well as read and write access to all processors' memory, which is essentially equivalent to doing whatever you want to do on the host. So we could do things to further lock things down, like we could have, by default, seccomps restrict the system calls. It doesn't really change the file system access, but if someone wants to abuse a system call that is not supported, they won't be able to do it.
We could use SELinux or AppArmog, which can restrict access to read-only and to specific pathways. The problem is that the OS has not agreed on a single one of these two, so Ubuntu uses… our mobile uses SELinux, so it depends on the underlying OS, and it's difficult to do something that by default applies to everyone.
And it's possible also, and Florian brought that up, to use landlock, which is a feature of the kernel starting 5… starting from 5.13, which can restrict access to read-only on a file system. It can also restrict network access and to specific pathways.
But any of those methods of doing things will be very hard to apply without potentially breaking other functionality that other components in the collector do, especially when these other components run in exactly the same process and the same container than the Profiler. So, the recommendation we're trying to put forward is that the default deployment path of the profiler should be in a dedicated distribution, so that it runs in a dedicated container.
We're going to continue removing privilege because it's defense in depth. Like, even if without it we are basically a route, it's still better not to run with privilege, and we're going to continue exploring any other ways to… to reduce the… the surface area, but that would only be possible if we do the assumption that it's only the profiler who is running in that process, and not virtually any possible config component.
So yeah, looking for, general thoughts on this.
Florian Lehner 00:38:57 Yeah, I'm thinking, for putting this together. I also contributed a bit to the discussion we see on the right side, on the GitHub issue. I share the same, concerns, that, Profiling needs to run with the special privileges, but granting these privileges to every hotel component, opens, security.
Opens the discussion for, opens the concerns for security issues, and, this should be handled.
Property, but, I also see that, the lockdown elements you listed here is really on a process level, so you cannot specify, hey, this dependency, using landlock, but the rest of the, the process are fine to do whatever they want.
Yeah, so, yeah, I fully agree with the recommendation to have a dedicated distribution for maybe not profiling specific, but more like, everything that needs privileges, so, maybe we need to, or can come up with something, also with OBI. I think they are running into the same issues. They also need, Perform, BPF, Suslock.
I'm not sure about P-Trace, but they use also Sys Resource and Duck Research.
So, yeah, then they need also the privileges.
Christos Kalkanis 00:40:34 So, and Nayef have a question regarding the country distribution, and sorry, maybe it's been answered before, but I'm kind of late in this, going over the discussion, the issue that you have open in the screen. So, like, if we go back to the beginning, what are we trying to get out of having eBay Profiler in the content distribution? I'm guessing a lot of it has to do with getting more users to use it, and, you know, ease of use. We're making it available in a distribution. They don't have to think about, you know, how do I use this thing? They can just go use the confidence distribution, that packages a lot of, you know, related functionality altogether, so it's just a very convenient, very easy way for them to get exposed.
Okay.
So now, the security concern, to me, it seems that it's orthogonal to that. Like, why would the contrary, distribution, or us for putting it there, be responsible for ensuring that the way that distribution is used, you know, why would we have to solve the security problems that arise out of how this thing is deployed? Because that's normally on the people that deploy the distribution, right? Like, different environments have different security policies, and so on.
So… Why can't we just add the profiler to the country distribution, and then, extend if there is a security warning there, or… Like, anything related to how… the recommendations on deploying this, and the security implications, and so on. If it's not, we can add it.
But… You know what? Yeah.
Nayef Ghattas 00:42:12 Go ahead.
Christos Kalkanis 00:42:13 So I'm wondering what problem are we really trying to solve here, essentially?
Nayef Ghattas 00:42:16 Yeah, I guess there's already a security warning to never run contrib in production, and nobody is doing this. So, if we add another security warning, I think that users are just not going to read it and just do the most practical thing they can do.
And what I'm trying to avoid is just bad press for the entire Open Telemetry community and how we do things, because if we are allowing users to do by default something that is not secure, and just putting something in the documentation to say users should not do it, I think users would do it and will not necessarily understand the risk that they're partaking when they're going to install the profiler.
Christos Kalkanis 00:42:58 Okay.
Yeah, that makes sense. But it's a trade-off, right? So it's, again, convenience versus security. Who wins? Well, we know who wins in practice. It's always convenience, right?
Nayef Ghattas 00:43:07 I mean, we can also make it convenient to deploy the profiler without having it running in content, because we already have it in the Helm chart, it's a preset, so it's only a single flag.
Indeed, you have to deploy another daemon set, but I mean, in terms of convenience, it's not the end of the world. Like, we have already shared this with a lot of users, and so far, we have never gotten any feedback or pushback from the fact that it's, running in a dedicated daemon set. And all users have been like, this is super easy to install, I just turned the preset, and then it's deployed everywhere. Very cool.
Florian Lehner 00:43:47 To add on this, I think we also need to keep in mind that there is already an auto collector distribution for eBPF Profiler. So, it's… moving, or that idea from Antoine, as I understand it, is not… to replace our Auto Collector EV path profile distribution that is isolated, and doesn't share this concern, but have it also in Auto Collector Contrib, and if you look into Auto CollectorContrip, and in… I think it's Manifest, then, We see that this opens up the… The possibilities of issues everywhere.
Christos Kalkanis 00:44:29 Florian, can you… can you… I'm not… I think it's you who's sharing the screen, I don't… if not, then…
Florian Lehner 00:44:34 Yep, whomever.
Christos Kalkanis 00:44:34 Can you click on the fixes? So, Antoine left a link, fixes 1562? There, because that's… I think it's his reasoning for why he wants it in ComTrip, so let's figure it out.
Like, I think he has… yeah.
Okay, so yes, so… more adoption.
checking how well it works in different operating systems, and then help vendors, try it out, adopt it, and so on. Okay.
Nayef Ghattas 00:45:04 Yeah, to be honest, I'm not sure it really drives more adoption if the way to do it via dedicated distribution is already super easy, and I'm also not sure it helps vendors, because, case in point, we are a vendor, we have adopted it, and it works great.
And we can also do the checks for the OS in other ways, but yeah.
Christos Kalkanis 00:45:26 Okay.
Yeah, I mean, I guess… we need to get Anjoan involved, because he's the one who created this issue. Just talk to him, figure out, you know, maybe there's more here that's not directly captured in what he put down in this, issue.
But, I mean, fundamentally, nayef, if we… Yeah, I think I fall more on the side of… if Open Telemetry has clear guidelines regarding the security implications of running contrive in production, and that users can read and understand, then At some point, the responsibility has to be on the user, right? Like, it cannot be on Open Telemetry. If Open Telemetry is clear about, do not run this in production, or if you do run this in production, here are all the security implications and so on.
Like, I think whenever… You try to restrict what the user can do.
Yeah, you're basically worse off in many ways than if you just lay out all the implications and let the user make a decision.
But… Yeah, I'm not the one making any decisions here.
But I would also… I would also agree with… I'd be fine with what you mentioned, by the way, so I'm just… Yeah.
Nayef Ghattas 00:46:48 I think I agree with that statement. My concern there is that the guidelines that Open Telemetry had were written when there was no privileged component like the EDPF profiler that is running.
If we… if we bring this up to the collector's sake, with the security concerns, and then the technical committee of OTEL says.
This is fine.
And we want to allow this by default, well, I mean, we have to do this, but I think it's still worth just putting the trade-off for everyone's eyes and talking about it, just to make sure that this is the trade-off we want to take.
Christos Kalkanis 00:47:30 No, absolutely. I think also because it… maybe it's not… it's probably not clear to, I guess, most people that end up using the profiler through Auto. Like, they probably don't understand that the security implications are transitive, and whatever privileges the profiler server needs are essentially exposing the entire process.
So, we absolutely need to make that crystal clear.
Okay, so I guess, what's the next step here? Do we reach out one-to-one, or… Ideally, he would join the next SIG meeting, and we can talk about it.
Nayef Ghattas 00:48:09 So, I think if everyone agrees, I can spend a bit more time just, working on the document, doing a couple small edits, and then we can probably race this to the Collecto SIG meeting, and find a SIG meeting while Antoine can join, so that we can discuss this with the other Collecto folks, as well as Antoine, and see what is the global opinion there.
Florian Lehner 00:48:30 Yeah, sounds good.
Muted.
And if there are no… Further comments on this topic? I think we have 12 minutes left for the last topic, also Nayef.
Nayef Ghattas 00:49:29 I'm going to be talking a lot.
Florian Lehner 00:49:32 Do you want to share your screen? And I'm stopping sharing.
Nayef Ghattas 00:49:35 Okay, yeah, let me show my screen.
There we go, I can maybe zoom in a bit.
Does that… does that work for everyone?
Okay, so… Understood.
This is about, the versioning for OTLP profiles.
So, so far, we said that OTLP profiles are going to continue using V1 development, even though we ship incompatible changes, especially. So, now that we've done alpha, we said that we're going to pause all incompatible changes and maybe ship them together before better, but there also might be other incompatible changes on the code above while we switch from beta to stable. So what this proposal is doing is proposing a temporary request metadata key, which is OTLP Profiles development version, so that the servers can reject the unsupported format before decoding.
And so, the proposal, essentially, is to also say that if that metadata is not available, we suppose that it's the current alpha format that is there right now, and this should apply as a header to OTLP HTTP and metadata in OTLP gRPC. And the idea is to retire this when profiles move to V1, because all V1 signals are, like, do not contain breaking changes and changes.
Should be, should stay compatible.
So, yeah, essentially, the motivation is, is what I just said, And then, the constraints, sort of, what we're trying to deal with is letting the OTLP server, so it's either the collector itself or a backend, identify the version before decoding a request, and make the unsupported version a clear error on the backend side that it returns to the client, and the client should not retry In that case, and have… have it work with both OTLP HTTP and OTLP GRPC.
So this is not introducing a global version for, all the stable signals.
Another known goal is to require version discovery or a negotiation protocol, because this could be very complicated to implement, or require collectors or backend to support previous development versions or convert between versions, so a collector or a backend should be free to support only a single development version.
So yeah, as I said, this is the metadata key, and the suggested value is maturity-revision, so that we're able to have multiple revisions in the same maturity, if ever we are to push multiple breaking changes in beta.
But we could also have also maturity as well. I have very strong opinions on this. And the idea to move forward with a format like this instead of the Open Telemetry Proto version is because the Open Telemetry Proto version is sort of hard to parse, because it's the same veg, so it requires a bit more logic to parse.
And also, multiple open Telemetry proto, like VE1.11 and 1.12 and 1.13, might be completely compatible in terms of what the profiling signal is doing, so we don't necessarily need to break compatibility if the server is emitting 1.11, but the backend supports 1.12, if they're completely compatible on the wire.
So it's essentially another way of indicating when we break backward compatibility.
So… On the client behavior, if the client is serializing alpha 1, it can emit the metadata, or it can send the alpha 1 value, which is the current protocol that we have. Any later format must send exactly one value, and if a server rejects the version, the client must treat the request as permanently failed.
And then on the server side, if the metadata is absent, we treat it as alpha 1. We suppose that exactly one supported value is present, otherwise anything unsupported, malformed, or with a repeated value would lead to the payload being completely rejected.
And in terms of compatibility, so we need the servos to implement the version check and accept missing data or explicit alpha 1. Then updated clients may send alpha 1, and when we do the beta, then the servos can add support for Beta 1 and start filtering on it, and later compatible beta changes, must increment the version to Beta 2, Beta 3, etc. The server can choose to support multiple versions if needed, but in the Open Telemetry Collector itself, I think the recommendation is going to be to always, support a single version. But that leaves the option to backends to implement whatever they think is preferred.
So, a couple alternatives. Adding this in the payload, this doesn't work, because we need to be able to get the version before passing the payload. A global OTLP version, this was already suggested in the hotel ecosystem in 2022, I think, and rejected.
version service pathways and HTTP pathas is, like, switching between V1 development, V1 alpha, V1 Beta, which we rejected because of the work required to update all the code.
In the different SDKs and the collector, as opposed to just, like, one single, version level, version, string.
And anything that involves negotiation, or conversion, or multi-version, mandatory multiversion support, is too complicated to be implemented. So yeah, that's essentially it, and I'm happy to have any feedback.
Christos Kalkanis 00:55:39 Yeah, looks good to me. We actually had something like this internally at Elastic, way before we did the Open Telemetry submission.
So, we've seen this stimulant scheme working.
That's just one comment for the must language, so we write that, clients must implement this, right?
Yes. But if they don't, we don't really… the server can't really tell, right? So…
Nayef Ghattas 00:56:06 If they don't… the server will suppose it's alpha 1, and the copy.
Christos Kalkanis 00:56:09 Oh, yeah.
Nayef Ghattas 00:56:10 Who doesn't support Alpha 1, yeah.
Christos Kalkanis 00:56:12 Yes.
Florian Lehner 00:56:22 I'm just thinking out loud, most of the Profiles OTLP stuff will… Be used via the… custom gRPC implementation from the… Collector PData implementation.
I think Bogdan wrote this.
So this probably needs a change in the OTEC Collect… tour… If I'm not mistaken,
Nayef Ghattas 00:57:00 Yeah, so I think we need to have at least a change in the hotel collector right now to… to accept Alpha 1 or empty header, and when we ship Beta 1, we need to update it to only accept Beta 1, at the same time that we update the… protocol version, for Open Telemetry Quarter, ideally.
Florian Lehner 00:57:28 Yeah, makes sense. I think then it needs some kind of synchronization with the collector people.
Nayef Ghattas 00:57:35 Yep.
Yeah, I agree. I think, since… since it's something that impacts, Potentially, the collector, the… Profiler and all the SDKs, because they can build and emit profiles and backends. It feels like this needs to be an OTEP, although… If we make it an OTAP, it might take time to merge and get shipped. So… what I wanted to do next, if, like, if there's a rough agreement in the Profiling CAIC that a mechanism like this makes sense, is to take it to the specifications CAIC during Tuesday meetings, and see what their opinion on this, how we should move forward with this.
Hmm… And then see what next steps are.
Christos Kalkanis 00:58:28 Yeah, I think we should avoid an OTEP if we can. Like, there's no clear reason why this would be an OTEP, it's just a small change, and, like, most of it is profiling-specific, so it doesn't really touch anything outside of Open Telemetry. The only non-profiling-specific thing is the change to the collector to propagate the metadata.
Nayef Ghattas 00:58:47 And they changed the SDKs, for the profile emitters, so that they set the metadata.
Christos Kalkanis 00:58:53 Okay, yeah.
Nayef Ghattas 00:58:55 this is the… this is just the part, since it requires a change on the collector and SDK, this is why I wonder if they're going to say that, but I will try to push for no OTEP if we can.
Florian Lehner 00:59:12 I'm not sure how many SDK implementations are there for profiles, maybe Yeah, probably Charma.
Nayef Ghattas 00:59:23 net, I think, has an alpha one.
Florian Lehner 00:59:27 Okay, I'm not aware of the .NET, yeah, but I just know a… on the Auto Collector side, the go part.
And the Java part, these are the two major things I have in mind for this that are impacted by this.
Nayef Ghattas 00:59:43 Yep.
Florian Lehner 00:59:52 Yeah, otherwise, I think I'm also aligned, and I agree with, with the proposed, Way of going forward.
Adding this as a metadata information.
presenting it.
Thanks for taking it on.
Nayef Ghattas 01:00:14 Yeah, and feel free to add any other comments, you think, if you… if you think of anything.
Florian Lehner 01:00:27 Any other comments on this?
Otherwise, it looks like perfect timing. We have 30 seconds left.
Unattended.
Okay, then, thanks everyone, and see you in two weeks.
Christos Kalkanis 01:00:47 Thanks. Thanks.
Right.
Florian Lehner 01:00:49 Bio.
