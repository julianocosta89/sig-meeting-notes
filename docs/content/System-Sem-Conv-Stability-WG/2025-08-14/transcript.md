SIG: System Sem Conv Stability WG
Date: 2025-08-14
Duration: 25 minutes
Zoom Recording URL: https://zoom.us/rec/share/kd6ILth0Tp6Ivd0bSbpnR4ZX_MjKtZsq4YuYEEtMUrkzPLaWDFjBs_GJ7FocWiQ.1DmGLcvdpie3oRrb
============================================================

## Zoom Recording Transcript

**Braydon Kains** 00:40 Hello.
Hello.
**Pablo Baeyens** 00:54 Hey.
**Braydon Kains** 01:51 Am I remember correctly that Christos is on leave at the moment?
**Roger Coll** 01:58 Ricks.
**Braydon Kains** 02:08 I'm just waiting on Dimitri, then. We'll give him another minute.
Alright, I guess we can get started.
**Roger Coll** 03:46 Yeah.
I'll say that.
I think I just added one topic. It will be very quick, but I… Start working on some of the… issues, or PRs blocking the GA, and just created a PR for, … for this issue, that it was to rename the system network drop to SystemNetwork.packet.dropped, and I think that… A few months ago, we agreed on… Not having it, in the system. namespace, sorry.
But, as I was mentioning in this commit, I think that, … okay, I see that Pablo meant it out, but, that we reverted that decision of having, let's say, non-white area metrics, for example, we did that for the CPU, that we reverted the….
**Braydon Kains** 04:46 Oh, yeah.
**Roger Coll** 04:47 Moving from CPU to system, so… Yeah, in the PR that I just made, I kept the system namespace.
So, if you agree, please… Take a look… And another comment that I wanted to do… Is that also you?
We're, let's say, suggesting Moving the metric system.network.packets to, packets.received.
And it looks like it has an attribute, this metric, that is the network I.O. direction.
That actually defines if it's either, let's say, received or transmit.
**Braydon Kains** 05:34 Right. So….
**Roger Coll** 05:35 I don't know if this affects anymore, you remember the context of that, or….
**Braydon Kains** 05:42 It's coming back to me now, and I think… … I think you're right that the… Packets.received.
is probably not the right choice because of that. The main thing I was trying to… Figure out is this whole, like, clash of… of, … metric namespaces to metric names, where, like, if we have… if we have packets.dro… or, sorry, we… you don't pluralize namespaces, so if it was packet.dropped.
And then you also had system.network.packet. I guess you'd need it to be count, or something.
This is .network.packet.count.
**Roger Coll** 06:22 I see. Yeah.
I see. Let me check the metrics, because maybe we'll have something similar already.
Yeah, so we have system.network packets that it's, as you mentioned, a counter, it's not count, but I think this is still valid, right, with the… Definition having the plural for counters.
Yeah.
**Braydon Kains** 06:49 Wait.
**Roger Coll** 06:49 Yep.
**Braydon Kains** 06:50 I think they… I think we've, like, changed the guidance recently to be more specific, like, just don't pluralize metric names in general, so maybe we need to… Re-evaluate some of these.
**Roger Coll** 07:03 Yes, I think I read it a few hours ago, and my understanding was that, seeing it… It's visible, it's visible, this thing, but I… Can take a look.
We can take a look at the guides. Yeah, this one.
**Braydon Kains** 07:24 Yep.
**Roger Coll** 07:26 You know, guidance… So yeah, here it basically says system network packets should be parallelized, even if there's just a single data point is recorded.
So it looks like this one is….
**Braydon Kains** 07:42 Oh, okay, yeah, in this case, yeah, yeah.
**Roger Coll** 07:45 Or at least we are recommending it here.
**Braydon Kains** 07:47 So, I think the only way to… to name it around this guidance would be system.network.dropped underscore packets, maybe? But that feels bad, too.
Oh, good.
**Roger Coll** 08:02 I see, yeah.
That's right.
**Pablo Baeyens** 08:06 get why we cannot do system.netport.drop.packets? Like, what's the… the rule we are not following there?
**Braydon Kains** 08:14 O.Dropped.packets.
**Roger Coll** 08:16 Yeah, it's packets that dropped.
**Pablo Baeyens** 08:20 Oh, sorry, yeah, I… Got it wrong, Ben.
Oh, yeah.
**Roger Coll** 08:29 Hmm.
But maybe, … We have an issue here, because, … We have systemnetwork.packets.
But at the same time, we have system, network, I.O.
which… I don't know what's the difference at the moment, because.
**Braydon Kains** 08:49 I think the difference is that it's measured in bytes versus packets.
**Roger Coll** 08:55 I see. Okay, yeah, right, yeah.
Yeah, yeah, yeah.
**Braydon Kains** 09:01 wisdom.network.io.
**Roger Coll** 09:04 Yeah.
**Braydon Kains** 09:04 I think both of these… accounts come from the ProcNet whatever the file entry for the device in ProcFS, if I remember correctly.
**Roger Coll** 09:14 Okay.
Okay.
**Braydon Kains** 09:16 I might not be remembering correctly, I haven't looked at this in a while.
But….
**Roger Coll** 09:21 Yeah, yeah, yeah, you're right.
No, maybe… Could be another… Attribute, like the state or something like that, that dropped.
Or accepted, or something like that, right?
And be part of system.network of packets.
**Braydon Kains** 09:49 Yeah, that… that would allow us to… to follow the naming rules. It feels like a… somewhat… Awkward… usage.
Maybe.
**Roger Coll** 09:59 Yeah.
**Braydon Kains** 10:00 It's like, we would have to make the metric harder to use just to follow the naming rule.
**Roger Coll** 10:13 Yeah, the good thing is that with the… if it's an attribute, then we could make… Make it opt-in, the attribute, and by default, just provide the… Aggregated of dropped plus accepted, that it would be the current System.network.packets, and then you could… just opt in to enable the, I don't know, system.network.
**Braydon Kains** 10:39 Hmm.
**Roger Coll** 10:40 Packet state, or… Something like that.
**Braydon Kains** 10:44 I… I don't remember if… this value from… from Proc DevNet is including the dropped packets or not.
I need to look at the main page again.
**Pablo Baeyens** 11:03 Wait, not proc pin.
**Braydon Kains** 11:15 Network to… So… I… aw, man, I can't… this doesn't say… packet, what the packets column means in the man page.
**Pablo Baeyens** 11:28 And you click on the… there was a link, next to the… prop.net, or maybe there.
**Braydon Kains** 11:35 Oh, yeah, actually there was in the drop column in Proc DevNet.
Of course, sir.
web archive.
What is this?
Looking at….
**Roger Coll** 11:52 Hong Lam.
Boom.
**Braydon Kains** 11:57 Huh.
It's… some, like, blog post.
**Roger Coll** 12:02 Yeah, it looks like.
**Braydon Kains** 12:04 Also, I think that there may be a typo in that description, too, on an unrelated note, because I'm pretty sure it's ProcNetDev, not Proc DevNet.
**Roger Coll** 12:15 product net that, ….
**Braydon Kains** 12:19 I think that's probably just been sitting in that description for ages.
**Roger Coll** 12:32 Cool.
**Braydon Kains** 12:49 Cuz….
**Roger Coll** 12:50 Parker.
**Braydon Kains** 12:50 The number of received and sent packets.
**Roger Coll** 12:53 Yeah, so you have multiple… Multiple states, you have errors dropped.
**Braydon Kains** 13:04 Yeah, and it's… it's not quite….
**Roger Coll** 13:07 comparisons.
**Braydon Kains** 13:08 Not quite clear to me, … whether packets is… because for one thing, packets is also… … Sent and received?
Or, no, okay, sorry, there's two sections. There's a receive and.
**Roger Coll** 13:23 Yeah, exactly.
**Braydon Kains** 13:24 Okay, I, okay, okay.
**Roger Coll** 13:26 That's the….
**Braydon Kains** 13:27 Same number.
**Roger Coll** 13:27 I.O.
**Braydon Kains** 13:29 Oh, that's just….
**Roger Coll** 13:30 Yeah, but this is the loopback interface.
**Braydon Kains** 13:34 Yeah, okay, that's why I was… I was confused.
Okay. That one, well. Yeah, the WLAN0 is the one we're thinking about.
**Roger Coll** 13:42 But also….
**Braydon Kains** 13:45 This one says that there were 26 drop packets, transmit.
**Roger Coll** 13:50 But what's not clear to me is if the 26 is included in the packets or not.
That's a good question.
**Braydon Kains** 13:58 I wonder if I'm gonna need to browse the ProcFS code again to figure this one out, because the man page wasn't telling me.
Oh, well.
….
**Pablo Baeyens** 14:11 One page is not helpful at all, yeah.
**Braydon Kains** 14:14 No, really, it's really not giving me what I need.
**Roger Coll** 14:18 Probably this can be… hold on, this is bytes, this is packing?
Hmm.
**Braydon Kains** 14:29 There is something to be said for us just, like, matching exactly what this file gives, it's just… we need to make sure we do it in a way where, like, if someone's trying to instrument the network device metrics on Windows or something, they can still get the same….
**Roger Coll** 14:43 Yeah, exactly.
**Braydon Kains** 14:43 information.
**Roger Coll** 14:45 Huh.
But what I think is that we also have a metric for network errors, so probably it should be… look really similar to the dropped one.
**Braydon Kains** 14:56 Yeah. Yeah, I think I… it seems like it's mostly because, like, these are just, like, mapping directly to what's in this file.
Error… errors, and dropped, and… … It doesn't look like we take frame, compressed, and multicast, but the other ones are, like… I see.
**Roger Coll** 15:23 Hmm.
**Braydon Kains** 15:27 Mmm, I might… we might need to think about this one a bit.
**Roger Coll** 15:30 Yeah.
**Braydon Kains** 15:30 a bit deeper.
Yeah. At the moment, I'm not… I'm not sure.
**Roger Coll** 15:37 Yeah, me neither.
Probably I will put a few….
**Pablo Baeyens** 15:41 Good name.
**Roger Coll** 15:42 Yep.
**Pablo Baeyens** 15:43 I was sure when I reviewed the PR, but yeah, not now.
**Roger Coll** 15:46 Yeah, same for you.
**Braydon Kains** 15:48 If you talk about anything long enough, we can become unsure about it.
**Roger Coll** 15:55 Yeah, I think I will move that period to draft and give it a shot, probably.
**Braydon Kains** 16:00 Sure.
**Roger Coll** 16:01 common portal.
**Braydon Kains** 16:03 I'll leave a… leave a comment, … Right after the meeting.
**Roger Coll** 16:09 what we discussed.
Sounds good.
Yeah, well….
**Braydon Kains** 16:15 Excuse me.
**Roger Coll** 16:18 Nope.
**Braydon Kains** 16:21 My topic is about the… the PRs that James Thompson posted in our… in our channel, the OS property one.
… At the moment, I'm kinda skeptical.
One of the main changes… That he's proposing, is that… the OS type is… like… essentially merged into just, like, being, like, Windows Unix.
Or whatever the last one is, and then, like, that means… like, Linux and macOS and BSD and all these ones are now just, like, the Unix OS type.
**Roger Coll** 17:08 Hmm. ….
**Braydon Kains** 17:10 I don't agree with that, because it doesn't feel… it feels way too restrictive. Like, even if… it's one of those things where, like, yes, it's technically correct that Linux and BSD and whatever, they're all Unixes.
But if I'm talking about, like, is this attribute useful?
Not… not really. Not if all of my… all of these would be the same OS type of Unix. Like, if you have to look at the family to get any useful information, then why does this attribute exist? That's… Like, just to differentiate Unix from Windows, I guess.
**Roger Coll** 17:48 I agree, I think, on this.
statement about… Whoop.
actual value groups. Yeah, Unix for macOS and all the other stuff.
**Braydon Kains** 17:59 Yeah. I think, like, part of what the PR does is, like, get rid of all the different BSD variants and just… We could… but I think, like, and just call them all BSD, I think that's fine. And then the os.family would be where you'd get, like, is it FreeBSD, or Dragonfly, or whatever the fuck?
**Roger Coll** 18:18 Okay… And then what do you have for OS type is just Unix… and Windows, or….
**Braydon Kains** 18:28 Like, the way I think it should be is, like, the OS type should be, like, Windows, Darwin, Linux, BSD, And, like, mainframe, or whatever, ZOS, whatever it's called.
And then… the OS family would have, like… is it… if it's… you see the OS type of Linux, and then you see it's, like, Ubuntu and the OS. family.
**Roger Coll** 18:51 I see.
**Braydon Kains** 18:52 Or fedora, or rail, or….
**Roger Coll** 18:56 Yeah.
Okay.
**Braydon Kains** 18:59 I think that's more useful, like… I, I also am not sure I… understand… like, I guess for OS type.
like, logically, if you… you would aggregate OS type if, like, you had a bunch of VMs and you wanted to get all of your Linux VMs.
Or all of your Windows VMs, and so you'd use OS type to figure that out. But in that case, like, I think… The logical way most users would think about it is that like, Linux is distinct from BST, and thus the os.type becomes less useful because of how many things are squashed into Unix.
**Pablo Baeyens** 19:48 Yeah, I also feel like we should be conservative with the values that we add, like… I don't see the point of using… of adding Wasam if there's… I'm even skeptical that it wasn't concept internal as an operating system, but, like, I wouldn't add it if there's no concrete use case of, like, we're going to use it for this.
**Braydon Kains** 20:08 Yeah, like, that one, I could… I could maybe… I see WASM as, like, a runtime, like, if a WASM process was running on a VM, you wouldn't… Or, like, think of, like, a Java process. You'd call it a Java process running on a Windows machine, not a Java process running on the JVM.
That's kind of the relationship I see.
I guess there's these, like, WASM platforms, like this Hyperlite one that he linked.
In that case.
**Pablo Baeyens** 20:37 But is that a… I'm… Establishing op thing for us to… commit to supporting this forever? I don't know.
**Braydon Kains** 20:45 That's a… that's, like, a good point. I would, like, I would wager probably not.
**Pablo Baeyens** 20:52 I also… I don't know what… industrial training.
**Braydon Kains** 20:55 I've never heard of it in my life. But it also looks like, … And maybe this is… maybe this is telling in some way, but, like, it looks like, … they matched the values to basically exactly what comes out of this Rust standard library thing.
Which I don't think is a definitive enough reason for us to… to choose it. Like… like, he also wants to change Windows NT… Windows to Windows NT.
But… why? Like, Windows… Gives you the same information.
**Pablo Baeyens** 21:33 Yeah.
**Roger Coll** 21:36 What is Windows NP?
**Braydon Kains** 21:40 basically, like, he's… he's suggesting changing the os.type of Windows to Windows NT, one word, for any Windows operating system based on the NT kernel, but, like.
**Roger Coll** 21:51 Mmm.
**Braydon Kains** 21:52 I think that's… all of them? Like, the OpenTelemetry… there's not gonna be OpenTelemetry instrumentation for Windows 98 anytime.
**Roger Coll** 21:59 Yeah, yeah.
**Braydon Kains** 21:59 To my… to my knowledge.
**Pablo Baeyens** 22:04 I mean, maybe in the future, but, like, maybe in that case we would say, like, Windows 9X and Windows?
Yeah, maybe.
Yeah, the default, so… and what people identify as Windows, so….
**Braydon Kains** 22:19 Yeah.
And… but even in that case, like, I think Windows would be the type, and then the family would be Win… Win9X or something, right?
Even under, like, under this new model.
Right, yep. Yeah.
So yeah, I think I'm gonna… I'm gonna put my foot down about the Windows and Unix things, at least.
**Pablo Baeyens** 22:44 Sounds good.
**Braydon Kains** 22:49 I think… and then the other one was adding more OS attributes based on the OS release file.
Which… I agree with in principle, but the thing I'm worried about is that, like.
some of these things, like, if you're on Linux, these things are very obviously pulled from very specific things in OS release, but then getting the same information on a non-Linux platform is kind of unclear. Like, what should OS.ID actually be on Windows?
or ID, like, ID-like, like, these things don't have, like, exact equivalents in other platforms, and… the instructions only… in the PR only say how to get it on Linux.
so I'd be a bit confused if I, like, if I was a resource detection implementer trying to… do OS resource detection and using these conventions, I would be very confused on what to say if I was in another platform.
So that was… that was mostly what my review said, and… … I would recommend looking at the PR as well, since… it's… it's a pretty major shake-up. I think the OS attributes actually does need it, so we can work with what… what's there, but I think we should.
Refine it a fair bit more.
**Pablo Baeyens** 24:15 I'll… Leave something in support of what you're saying.
**Braydon Kains** 24:20 Sounds good.
that was the only topic I had. Since I've been… I've been out for a while, I haven't… Had much progress on other system stuff.
**Roger Coll** 24:40 Okay, thank you.
**Braydon Kains** 24:43 Maybe worth noting as well that I just entered a double on-call shift, so I'm also, like… reduced… reduced capacity, like, I'll basically only be taking, like, reviews, like.
collector reviews and SEMCOMF reviews for the next, probably, couple weeks.
**Pablo Baeyens** 25:02 Good luck with that.
**Roger Coll** 25:03 Yeah, thank you.
**Braydon Kains** 25:09 Alright, I'll talk to you guys later.
**Pablo Baeyens** 25:11 Sounds good. Yep. Thank you. Bye-bye.
