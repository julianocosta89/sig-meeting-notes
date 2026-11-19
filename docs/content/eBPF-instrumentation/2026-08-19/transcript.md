SIG: eBPF Instrumentation
Date: 2026-08-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Mike Dame (Odigos) 00:00:43 Hey, guys.
Tyler Yahn (Splunk) 00:00:45 Hey.
How y'all doing?
Mike Dame (Odigos) 00:00:48 Good.
Endre Sara 00:00:49 Great.
Tyler Yahn (Splunk) 00:00:54 Hey, Steven.
Endre Sara 00:00:56 Parents do you?
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:00:58 Hey. Hey, Andre.
Endre Sara 00:01:00 Huh?
best people.
It's an amazing guy.
Tyler Yahn (Splunk) 00:01:11 Endre, where are you out of? That looks like a very pleasant weather you're having over there.
Endre Sara 00:01:16 Me? Yeah, I'm actually at my mother-in-law's house in Hungary.
And then, next week, I'll get my sisters in Germany.
Wow.
Tyler Yahn (Splunk) 00:01:26 Whoa.
Endre Sara 00:01:27 And sadly, I won't make it to… England, but that would be even cooler, hopefully.
Tyler Yahn (Splunk) 00:01:37 Yeah, Hungary sounds pretty good. Yeah.
Cool.
Well, I'm seeing people filter in… I think Mattia, I just saw him.
Yep, there's Mattia. I think we might actually have Quorum. So, yeah, I guess… Folks, if you wanted to make sure that you add your name to the attendees list.
And, any agenda items you wanted to talk about, go ahead and there as well, and I'll start sharing my screen, and we can get started here in just a second.
Awesome. Okay, welcome. First up on the agenda… Giuseppe, you wanted to talk about this, PR? I'm guessing this is the semantic country.
Giuseppe Ognibene (Coralogix) 00:02:58 Yeah, actually, there was the issue, but then I had some days.
And I did the PR, and it was approved, so I think we… we can skip it.
How about,
Tyler Yahn (Splunk) 00:03:12 Yeah.
Yeah, that seems reasonable.
Alright, cool. Is there anything blocking merging this from anybody?
Giuseppe Ognibene (Coralogix) 00:03:23 No, no, no, I added the issue just because I want to talk with all of you, but then, I mean, it was easier than I thought. I didn't want to remove the item from the agenda.
Tyler Yahn (Splunk) 00:03:36 Yeah, oh, okay, gotcha. But this should close, oh, no, it does. Okay, yeah.
Cool.
Alright, well… Yeah, let's merge it.
Nikola Grcevski 00:03:49 Anyways…
Tyler Yahn (Splunk) 00:03:51 Okay, cool. Alright, well, up next, Mitya, you wanted to ask about a patch release.
Matt 00:04:00 Yes. I know it's past, just one day from, from the B11 release, but I think we should, Release the patch, because we… we fixed the… some, some bugs. There is, there is a serious one.
Which could, crush, nodes.
Yeah, so… If everyone agrees, I think we should release a touch.
Nimrod Avni 00:04:24 Did we merge, like, I know there was… There was one with the, 6.13 kernels, and there was the other, like, mitigation to the, Phenode thing that, like, if we detect that we, like, if we detect that we can't override it, we just turn off… Context propagation, where both of.
Matt 00:04:48 Yeah, yeah, previously, previously we were just logging, that we weren't able to fix it, but now we just disable context propagation in order to not break other apps.
And that one has been merged, and Nikola has the, like,
Nikola Grcevski 00:05:05 Yeah, that one.
Matt 00:05:05 An hour ago? The other bug?
Yeah. One fix.
Nikola Grcevski 00:05:08 the FION read made it, right? Made it into 11, I think.
Or no.
Matt 00:05:15 Yes, but we did do another change on that.
Nikola Grcevski 00:05:18 Okay.
Matt 00:05:19 So… So, previously, we were just logging, that we weren't able to…
Nikola Grcevski 00:05:24 Yeah, yeah, yeah.
Matt 00:05:25 I had a fix-up, but now we are just disabling context propagation.
Nikola Grcevski 00:05:30 Yeah, I think we should release 11, update. To be honest, especially the kernel bug. I mean, I reproduced it yesterday. You need an underpowered machine, but… with the workloads we run, I think, I'm actually tracking one current issue. I don't know if it's because of the inode sharing numbers, but we noticed since May 30th.
Manage Grafana randomly dies.
In our… clusters?
And it could be because of this kernel bug.
Yeah, I thought it was maybe because of the change we made to, INO number… That stuff, there was a change around that time.
But now I'm more suspicious of this, because… when it crashes, there's nothing you can do, you have to evacuate the node and everything. So, it sounds like we just bombed the whole thing.
Yeah, it's not like a pod restarts.
So… I think it's, serious, yeah.
Tyler Yahn (Splunk) 00:06:45 So, my question is, though, how do you want to release it? Because I think there's… Enough to say that, like, this release… If it went out, would not be a patch release?
We have Node.js manual spend captures, we've got.
Filter support now, or not global filter support, like… So, there's definitely more than just a bug fix that would go out.
If we released from Maine, There is an option where we could try to branch from the, B011… Commit, and then just back-propagate these fixes, but, I mean, we can do that. It doesn't seem like… it seems like there's other fixes that are included here, though, that would be useful in going out, you know, sanitizing UTF-8.
A bunch of other things, yeah. Disabled CPU on failed fixed attachment. So, like… what's the version number, I guess, is the question.
Nikola Grcevski 00:07:48 There we go with 12, and then what we have in 12, we just go with 13.
Tyler Yahn (Splunk) 00:07:53 I mean… I think that might just be what we have to do, right? Like,
Nikola Grcevski 00:07:59 Sure.
Tyler Yahn (Splunk) 00:08:01 Yeah.
Nimrod Avni 00:08:03 Yeah, I think it's… should be fine.
Nikola Grcevski 00:08:09 I think it's important to get a release out there with, Matthias fixed it the most, I mean, with, With a workaround for the kernel bug, because that affects… Machine's under heavy load.
Okay.
Tyler Yahn (Splunk) 00:08:27 Yeah, I mean, that's good. This next topic is gonna be a little bit, harder to talk about, but, we'll… we'll get through it. Yeah, so that sounds good.
I can take the action item, unless somebody else is looking to do this release.
Nikola Grcevski 00:08:47 Sounds good, man. Okay.
Tyler Yahn (Splunk) 00:09:00 Okay.
This, kind of is a moot point, not looking for reviews if we're gonna do another release right away, but, I… I don't actually know how I'm gonna update this PR, for the V… 0, 1, 2, release. I guess… I'll, like, have to halfway do it.
With, like, a… V11 and a V12, so…
Nikola Grcevski 00:09:27 Or did we do two of them, or…
Tyler Yahn (Splunk) 00:09:30 No, I…
Nikola Grcevski 00:09:31 No.
Tyler Yahn (Splunk) 00:09:32 Well, I mean, we could, but then…
Nikola Grcevski 00:09:34 Too much work.
Tyler Yahn (Splunk) 00:09:35 what happens when V12 gets merged before V11? You know…
Nikola Grcevski 00:09:40 Yeah.
Tyler Yahn (Splunk) 00:09:40 Yeah, the… Yeah, I think we probably just… like, we're also asking, like, I'm asking you all to review this, it's a pretty big PR, it's like a thousand lines, and it's mostly just because it's, this config v2 stuff, which is, like, a recreation of our dev docs, so if you've read our dev docs on this, like, it actually isn't too bad, it's just rephrased, but… Yeah, it's more about just, like… Yeah, the, like, the index stuff, where we'd probably want to say, like, okay, instead of announcing the V11, we would just announce the V12.
Yeah.
It's gonna be, I think, a little bit of a mixture. Okay, I… that seems good.
Nikola Grcevski 00:10:22 Yeah, I'll review it today.
Tyler Yahn (Splunk) 00:10:24 Okay, let me… let me get the review out, and then, and then I'll… I'm gonna convert this to a draft while I… do the next release, and then I'll ask you to review it. How's that sound, Nikola?
Or, I mean, I guess you could review what we have, but it's gonna change the yeses thing.
Cool. Alright, that sounds good.
Let's… let's go with that.
Hmm… Okay, cool.
Alright, last up on the agenda, I just wanted to go over open PRs, we haven't done this in a while, but I wanted to pause here in case there's other things people had topics on. I'm guessing we'll probably touch base.
Going over the PRs.
But yeah, just pause here for a second.
Cool. Alright, well then let's… let's jump in. So, wow, two pages.
Add trace pipe only BPF debug mode.
This has been open for quite a long time.
Nikola Grcevski 00:11:46 I think Mattia's reviewed it.
I think Rafael asked for some changes, so maybe we need another approver.
Matt 00:11:53 Yeah, I did, like, 4 or 5 passes here, but every time there was something that needed to be fixed.
And now the tests are all failing, I guess some, some verifier error.
Nikola Grcevski 00:12:08 Yeah.
Tyler Yahn (Splunk) 00:12:23 Yeah, okay. So, but otherwise, it's just looking for another review. We can probably, There is a way to… I thought I could ignore, Raphael's… Change request, I don't know why that's not showing up right now. Okay, but it's just looking for another review once, I think.
Nikola Grcevski 00:12:42 You can, you can hit it as, you can hit it, like, the refresh button at the top, yeah.
Tyler Yahn (Splunk) 00:12:48 Yeah, this… it doesn't actually clear his review, though.
Nikola Grcevski 00:12:51 Yeah.
Tyler Yahn (Splunk) 00:12:52 It just asks for another review.
Nikola Grcevski 00:12:55 Okay.
Tyler Yahn (Splunk) 00:12:57 I don't know, it's… yeah, we'll figure it out.
Nikola Grcevski 00:12:59 We know what, you know, we know what we need to do, yeah.
Tyler Yahn (Splunk) 00:13:02 Okay.
Cool. Rfc… Mattia, I'm guessing we don't need to talk about this…
Matt 00:13:10 Yeah, I didn't have the time to revisit the API and split it.
Tyler Yahn (Splunk) 00:13:16 Okay.
Matt 00:13:17 Boom.
Tyler Yahn (Splunk) 00:13:19 Cool. Alright, well then let's all… we'll wait on that one.
This is still a draft, I don't think we need a… Oh, okay, it wasn't a draft. Oh, okay, I was like, why did I review this already? Yes, now I remember this one.
Nikola Grcevski 00:13:35 Yeah, it's turned into a draft, right? Because we were like, let's figure out what we need to do.
Tyler Yahn (Splunk) 00:13:40 Yeah.
Nikola Grcevski 00:13:40 Something…
Tyler Yahn (Splunk) 00:13:43 I think this might deserve to be closed. I don't know if we're gonna move forward with this. You can always reopen it, but… Okay. Yeah, I think, I think we probably want to keep the status of this, being honest, seeing that, like, we're not planning to accept this, but,
Nikola Grcevski 00:14:01 Well, let's close it then.
Tyler Yahn (Splunk) 00:14:03 Yeah, I'd probably want to put a comment, If you want to close it, Nikola, and maybe just add a comment on there, I don't want to think of one while I'm drafting this, but yeah.
Nikola Grcevski 00:14:12 The main issue is that we're coming up with, our own metrics for this, right? And not trying to get the.
Tyler Yahn (Splunk) 00:14:17 Yeah.
Nikola Grcevski 00:14:19 Correct.
Tyler Yahn (Splunk) 00:14:20 That was… that was my take, as well as, yeah, there's, I think, some… some other stuff, but yeah.
Nikola Grcevski 00:14:25 Okay.
Tyler Yahn (Splunk) 00:14:27 Yeah, I mean, I said… I guess I did say convert it to a draft as well, but…
Nikola Grcevski 00:14:35 Okay, well, I'm gonna let it simmer for one more week and see if there's any movement or something.
Author, and then decide to close it.
Tyler Yahn (Splunk) 00:14:43 Yeah, okay.
Nikola Grcevski 00:14:44 That sounds good.
Tyler Yahn (Splunk) 00:14:45 I don't see much engagement on this issue either, so…
Nikola Grcevski 00:14:47 No, no, it's been… it's been quiet since.
But it's August, people are on vacation, I don't know.
Tyler Yahn (Splunk) 00:14:53 Yeah, good point. Yeah, good point.
Okay.
I think I saw Marc on the call. This is upgraded to the V10 of, OATS.
Guessing this is still a work in progress.
Marc Tudurí 00:15:07 No, it's just that it doesn't work, we have to update the Go version.
So, maybe we can just close the PR for now.
Okay. Gonna reopen later.
Tyler Yahn (Splunk) 00:15:18 ZRA doesn't support, 125, is what this is?
Marc Tudurí 00:15:22 Yeah, exactly. It's a 126.
Tyler Yahn (Splunk) 00:15:26 Okay.
Interesting, okay.
Okay, add support for generic Python async server.
Listen to their…
Marc Tudurí 00:15:40 Yeah, I just, have to… address your feedback, and I'm gonna push.
Your last comment.
Okay, yeah, cool.
Tyler Yahn (Splunk) 00:15:50 Yeah, I, I definitely think that, like, some of these other feedback, like, we can definitely iterate on, but this one was standing out to me that we need that extra address, but it sounds like you're on it, so, okay.
Marc Tudurí 00:16:01 Cool.
Tyler Yahn (Splunk) 00:16:06 Awesome. Alright, do you know Instrumentable type?
This is Mario, who's out still.
Nikola Grcevski 00:16:11 Mario's away for the whole month, yeah, so…
Tyler Yahn (Splunk) 00:16:14 Yeah, yeah, okay.
I think there's… Yeah, it's actually, I think, just a little bit… it's actually not too bad, it needs to get rebased, but yeah.
Nikola Grcevski 00:16:24 And it's interesting, because in the new PR that Mark's working on for the Python runtime metrics, he actually added offsets scattering for Python, so I think we can just offsets scatter for Dino as well, and…
Tyler Yahn (Splunk) 00:16:36 Yeah.
Nikola Grcevski 00:16:36 And actually, it's not… It's possible to instrument it, and…
Tyler Yahn (Splunk) 00:16:41 I think you're right, which would be pretty cool.
Nikola Grcevski 00:16:44 Yeah, I… I think we should apply more of those. When it's a well-known runtime that has releases and whatever, the code that Marc has, I think, could just easily be repurposed, too.
Grab certain Deno versions we support, get their offsets, and then we'll be able to instrument.
TLS and everything else.
Tyler Yahn (Splunk) 00:17:05 Yeah, I agree. Definitely agree.
Well, cool, yeah, I think we'll wait for Mario to come back to kind of iterate on that, but I think that the path that Mark is kind of setting is a good roadmap for it as well.
Okay, yeah, don't need to talk about this one either. Mike, dynamic climate, client, sorry.
Marc Tudurí 00:17:31 God.
Mike Dame (Odigos) 00:17:32 Yeah, hey, sorry.
I clicked off of your screen now, Sharon. Yeah, so this was something that I was working on. I'm trying to do more dynamic client stuff with, like, trying to add network and stats metrics to our VM support, so we can do OB through there. And I found that the… the metrics pipelines, anyone can correct me if I'm wrong on this, are, like, really based around that CAITS attributes, collection. So I was just trying to find a way to do this, and, like, I tested it myself as just a… The main setup that we have is, you know, if someone even is running just a bare process on the host, we really want to be able to Click.
Like, network metrics just for that process.
Nikola Grcevski 00:18:23 So I made this P.
Mike Dame (Odigos) 00:18:25 No, it's not possible. Like, my follow-up with this, I think I put in a comment, would be, you know, trying to get attribute names on those metrics, too. But then, like, like, Tyler pointed out in here.
I'm just kind of curious in feedback of if there's any way to make this possible. I think it would be a good overall, like, it wouldn't just apply to, I think, the dynamic, so I think this would be for the whole… anywhere that OB runs on VMs, too, so it kind of helps the VM support. But yeah, any ideas that we have? I didn't see your comment, your reply yet here, so I haven't read this yet, so I'll go through that, but… I don't know what people think about that, or what kind of options we have for that.
Nikola Grcevski 00:19:11 I think it's possible, it's just, you know…
Tyler Yahn (Splunk) 00:19:15 Yeah, I agree, like, I think it's possible, and I think it's actually… it'd be great, because like you're saying.
Nikola Grcevski 00:19:19 Yeah.
Tyler Yahn (Splunk) 00:19:20 It's nice to not… to support all the places that this runs.
I just think that, like… you're gonna have to start associating, each one of those sockets or connections with the selected IP, or the…
Nikola Grcevski 00:19:32 alert.
Tyler Yahn (Splunk) 00:19:32 PID, right? And so, it's… it's gonna be… it's gonna take a little bit of work, I think is gonna be the harder part, yeah.
Mike Dame (Odigos) 00:19:40 Yeah, I mean, if it's not something that we're, like, totally against, then I'm happy to kind of, you know, try to bite it off and see what people think. Like you're saying, it does sound like a lot of work, but… That's kind of what I was… looking for, at least as a general, you know, go for it. But, yeah, I'll… I'll tip at this and see, you know, I'll go through what you're saying here. It might be… A lot, but… Again, any ideas that people have is… I'm open to it.
Nikola Grcevski 00:20:11 So there… there is an idea that, in my work with, so the way we do things right now is the… the SOC message program that we currently use for context propagation.
has PID access. At that time, we know what the process ID is that's trying to make that network request, and it hasn't yet Created the packet in terms of… It's… IP and whatever.
So, level 1, level 2, level 3, none of those, are actually created, but you do have the connection pair.
So you know incoming, outgoing port, incoming-outgoing address.
So it's possible at that time to say, this is a tracked connection, because that matches a PID we're tracking, so stored in a map.
And when the network, which we currently do either with a socket filter or a TC, depending on what the mode is, or what we could do.
then you query this map, and you say, is this one of these track connections? And if it is, then you emit the network event. Otherwise, you just block it. So, you could potentially add a little an extra mat there. To track this.
Mike Dame (Odigos) 00:21:31 Okay, so, I mean, that doesn't sound horrible,
Nikola Grcevski 00:21:35 No.
Mike Dame (Odigos) 00:21:36 be able to… work my way through that, so yeah, I'll look at that, and
Nikola Grcevski 00:21:41 Yeah, this goes even… Yeah, exactly. The only… so, maybe you'll need to go back in history of how we did this. So there's a slight little wrinkle there, so we… when I first initially wrote the code.
I used, I used to pull out a destination IP and address and port and everything from from that socket message program, but then the map that we currently use, I think.
file switched it to use the key, which is a lot more efficient. So it creates this, you know, the BPS socket key, whatever, and that is used for the key operation now, rather than the tuple. It's more memory efficient, and it seems to work.
I think if you're able to get a key, and… at the lower level, I think… then you're good. Then you can just query that. And if you're not, then we're gonna have to Pull back the old code that extracted all this information, store it in a separate map, and pull it from there, but…
Mike Dame (Odigos) 00:22:45 You don't want to make things less efficient, but if it could be, like, a separate map that is only queried in this kind of scenario, like, there could be a trade-off that, hey, there's a bit of an efficiency hit on VMs, but VMs are also, I think you're… Gonna be using less processes, like, you're tracking less.
Nikola Grcevski 00:23:02 there.
Mike Dame (Odigos) 00:23:02 Gen… in general, than a whole case cluster, so… Alright, cool. Yeah, I, like I said.
Nikola Grcevski 00:23:08 I think that would work. I think we can use it for stats. I think, initially, Pino wanted to, I think, add that as well. He was asking me, like, can we do it per process? How do I filter these? And we said, no, a network just gets everything. But I think, I think we can pull this off.
Mike Dame (Odigos) 00:23:26 Cool.
Yeah, so I'll… I'll look into that then. It'd be… be great for us on, you know, we have some VM users that want to get, like, the network metrics. It'd be cool to show that. And then, like, the… kind of corollary to that is things like service.name, I saw, are just under the CAITS attributes, list, so trying to pull those out, too, so that we can actually see what, you know, if you do have two processes that you're tracking, you want to see that break down, so… but I think we can kind of cross that once I at least solve the, the initial Sounds like this will be some eBPF changes, but… Not too bad.
Nikola Grcevski 00:24:08 Yeah, I think she'll be fine.
Yeah.
Mike Dame (Odigos) 00:24:11 Awesome. Yeah, well, I'll try to, work on that then.
Tyler Yahn (Splunk) 00:24:17 Perfect.
Cool.
Alright, so moving on, sure, log queue, processing, combined log…
Nikola Grcevski 00:24:28 Yeah… I… I think we should close those.
There's two PRs here.
So… Yeah, it's not for the same author, I don't think it's…
Tyler Yahn (Splunk) 00:24:42 No.
Matt 00:24:43 No, it's not this…
Nikola Grcevski 00:24:43 No, this is… no, this one, the previous one.
So, essentially, I had this long-standing issue that I wanted to attempt to replace the current breakdown we do processing and in queue.
that actually lets Obi show to the end user how much of the time was actually spent in the transaction, and it's one of the advantages of eBPF. We get the actual full time for the transaction rather than just the transaction time, right? So we know how long the process is just kind of waiting to be served. So I thought it would… but it's noisy now in the spans, we see those everywhere, right? And then… So I thought span events could be, but then span events might be going away, or being deprecated. So this user added this in logs, but I think it's pointless, to be honest, like… If you add them in logs, you don't have to have the log exporter, and then for somebody looking to see this information.
I would have to go check the logs, too. It's not user-friendly anymore.
And it's like, you have this in traces, but then to find out how much of the time was actually spent waiting.
You have to go and check in the logs.
Tyler Yahn (Splunk) 00:25:59 Yeah, I mean, in theory, like.
they're supposed to be linked in some backends, is, like, events, first fans, like, they're supposed to become, but, like, that's completely back-end, so, I mean, I'm… I'm… I'm with you, like, I think closing this seems reasonable.
Nikola Grcevski 00:26:14 Maybe… I don't know, maybe we should… Use another alternative or something to kind of… Record the timing weighted in the trace as an attribute instead of You know, maybe we come up with our own attribute and say, spent in waiting, so you can kind of get that information.
Tyler Yahn (Splunk) 00:26:37 Yeah, I know, this is, like, the whole argument of why people were like, don't get rid of spin events.
Nikola Grcevski 00:26:41 Spread events, yeah.
Tyler Yahn (Splunk) 00:26:42 Yeah, they're like, this is just what it's gonna be, it's just gonna be a bunch of attributes.
Like, I… yeah.
I don't know, I might just say, like, use… Are SPAN events deprecated? Did they actually.
Nikola Grcevski 00:26:56 They are, but I… when I talked to David Ashpel, he said, yeah, it's gonna be a while before they're fully removed, so… go for it.
That was his answer, so…
Tyler Yahn (Splunk) 00:27:05 I think that's probably the way I would say it as well, is probably just go for it, like… You know, have a few years of it working.
Nikola Grcevski 00:27:13 Yeah.
Tyler Yahn (Splunk) 00:27:13 seeing if there's actual value here, and then, like… Yeah.
If… if it turns out that, like, these actually aren't that helpful, then, like, whatever, just remove this from.
Nikola Grcevski 00:27:21 Yeah, we can remove them.
Tyler Yahn (Splunk) 00:27:23 And then if they are, and then we'll actually have a better plan once the deprecation happens as to what to move to.
Nikola Grcevski 00:27:28 I agree.
Tyler Yahn (Splunk) 00:27:29 Yeah.
Nikola Grcevski 00:27:30 So let's just close the PR and the corresponding and generic logs pipeline, saying, please use span events.
Instead, even though they're deprecated.
And then we can close the other PR, because we have no other log exporter at the moment, other than these. These will be the only things we'll be pushing out.
Tyler Yahn (Splunk) 00:27:50 Yeah.
Marc Tudurí 00:27:51 We don't… we don't want to support logs at all, at some point.
Nikola Grcevski 00:27:57 Oh, it's a good question.
We talked about it, right, when we… Mattia and, you know.
Brought up the log correlation, and… No, I could, but…
Tyler Yahn (Splunk) 00:28:13 I mean, I think… Well, like, what are we gonna ship?
Like, what logs do we plan to ship?
Nikola Grcevski 00:28:22 Yeah, exactly, like, there would be… Taking stuff from Standard Out, completely clobbering it.
I'm letting it go and stand it out, then they're shipping it ourselves,
Tyler Yahn (Splunk) 00:28:35 Hmm.
Nikola Grcevski 00:28:36 Yeah, I don't…
Tyler Yahn (Splunk) 00:28:38 Yeah, I… I don't know, like, I was… Yeah.
I'm hesitant about that one.
Nikola Grcevski 00:28:46 Yeah, it's not the right time, anyways, yeah.
Tyler Yahn (Splunk) 00:28:49 Yeah. We essentially start becoming, like, a Fluent bit equivalent.
Nikola Grcevski 00:28:53 Yeah, yeah, yeah.
Tyler Yahn (Splunk) 00:28:55 like… Yeah.
Like, I'm not saying, like, we shouldn't, but I think we should motivate it, like… Yeah, like, I… I don't know.
Because, yeah, if you're just gonna act as, like, a pipeline for logs.
I don't… yeah, you're competing in a space that I don't know if we're gonna win. But then, I don't know… like, the value add there. But, like, if we can do something more, like, a lot of the trace annotations, the trace ID and the spanity stuff that we do, like, that's phenomenal value. If we can do more of that, or, like, if we can generate logs that are relevant, like, I think that that becomes a good motivator to me.
Marc Tudurí 00:29:35 Yeah, yeah. Because my motivation was that, Like, I had a prototype to generate, exceptions from… Yeah. Like, SDKs now, like, generate automatic, exception… or error… errors, and… And they're in a span event, but now it's deprecated, and they have to use… This log record.
So, if you want to have this capability, In Obi, we should do… So, we should, comply with the spec and use the logs, so I don't know if… Yeah, how we couldn't achieve it.
Tyler Yahn (Splunk) 00:30:21 Do you know of other SIGs that have examples of using logs for span events?
Marc Tudurí 00:30:26 No, I didn't, no one had started already.
They just deprecated, and all the SDKs are still using span events, and… And eventually, they…
Nimrod Avni 00:30:38 some of the, like, exception events on traces in some of the SDKs became logs, if I remember correctly.
With all the, the, like, exception dot tags.
Tyler Yahn (Splunk) 00:30:53 But, do you know what languages those were?
Nimrod Avni 00:30:55 I think JavaScript, I remember? I don't know which one. Probably other… Like, I know that, a lot of people, like, wanted this kind of exception support in Obi, and, like, we don't… we can't really get it because we're not instrumenting code.
Maybe somehow in the fu- I don't know, maybe if we… do the same with, like, the Go and the Node.js that we connect to SDKs, maybe we can, like.
pipe them through a… I don't know exactly how to do it, but that might be a situation where we want logs.
Not super sure.
Tyler Yahn (Splunk) 00:31:34 Yeah, I mean, I think that that seems reasonable.
Nimrod Avni 00:31:37 We… but this PR, we can, like, close it for now and say, like, if it ever arises in the future.
Nikola Grcevski 00:31:44 Yeah.
Nimrod Avni 00:31:44 that we need a log pipeline. Like, whenever we will need it, we will probably need some adjustment, rebases, whatever.
Yeah. Can we conclude.
Marc Tudurí 00:31:55 Okay.
We can also do that.
Yeah.
Meh.
Tyler Yahn (Splunk) 00:32:02 Okay.
Okay, moving on then.
So, Nikola, are you also saying this one?
Nikola Grcevski 00:32:15 No, no, that one, in the previous PR, there's a mention of another PR. That's the one also we need to close.
No.
Tyler Yahn (Splunk) 00:32:25 Oh.
Nikola Grcevski 00:32:26 That's the original issue I opened.
If you go scroll down, you're gonna see a mention of another… yeah. no, that, no, still… Oh, that's still there.
Tyler Yahn (Splunk) 00:32:36 Yeah, sorry.
Nikola Grcevski 00:32:38 If you go with more and more and more… There you go, yeah. That one needs to be closed, because it just has a generic log exporter pipeline without any user at the moment.
Tyler Yahn (Splunk) 00:33:39 Okay.
Marc Tudurí 00:33:42 Cool.
Tyler Yahn (Splunk) 00:33:43 Alright, then moving on to this PR… Restore… contacts have SQL scopes. Oh, yes, okay.
Matt 00:33:51 Yeah, this one, maybe I can add a comment. So, I started working on a generic solution a couple of times.
But the user found, another hedge case which, I haven't addressed yet.
But I have a draft in our, internal fork.
So this one only addresses the SQL part, but this bug is, it's shared with all protocols.
Tyler Yahn (Splunk) 00:34:23 Yeah, yeah, I gotcha, okay.
So, Mattia, what do you… think is the right move on this? Do we want to keep pursuing this, or are you… do you think there's a more broad fix that we want to try to address?
Matt 00:34:37 I mean, I think I left a comment somewhere… oh, yeah, here… So, yeah, if this PR addresses this edge case that the user found.
Then maybe we should proceed with this one. Else, I think, the generic solution, which handles also these HKs would be better.
Tyler Yahn (Splunk) 00:35:02 Yeah, I kind of agree.
Nikola Grcevski 00:35:06 I think I also left a comment there, I think he was restoring the wrong context, but maybe I'm wrong.
I don't think I got an answer to that. Maybe he replied, I haven't checked.
It's right below.
I think there's Maybe.
Tyler Yahn (Splunk) 00:35:23 Mmm…
Nikola Grcevski 00:35:24 Maybe he had dressed in.
Yeah, because it's restoring… the invocation context. But the invocation context is the SQL context.
I don't know.
Matt 00:35:49 What's the Obi-CTX Restore doing?
you found words.
Nikola Grcevski 00:35:56 Yeah, I think it restores the context.
of… in the context map, that we correlate what is the current thread ID, and so on, with… With whatever you have in the trace parent, so… So if you expand this function, you'll see this GoSQL, if you expand the Go code more, yeah.
Mostly is up, if you go the up… Expand the… Higher VIN.
So, in vocation here.
is the ongoing SQL query, and we're about to finish it, so I think he wants to restore The previous context.
Because the current… ongoing location context is the sequel.
Yup. So… What's your term?
Matt 00:36:55 Can you go one moment in, obctx.h, the second file?
Yes, it's the wrong context.
I was thinking maybe he's looking in all the maps in here, and restoring the right one, but it's not the case.
Nikola Grcevski 00:37:14 Literally.
Tyler Yahn (Splunk) 00:37:15 Copying it back in. Okay.
Nikola Grcevski 00:37:17 Yeah, he's copying it back in, so which means the sequel is finished, but then we still remember the sequel as the valid context.
Yeah, I think, I think this needs your PR, Matt.
Mattia, I think it's, yeah.
Matt 00:37:38 Okay, then, maybe we can, close this, I can, I can leave a message and, I can pick this up.
Tyler Yahn (Splunk) 00:37:45 Yeah.
That sounds good.
I'm gonna sign it to you, just so we don't lose it, and then, yeah, if you could just do that, and then we can…
Marc Tudurí 00:37:52 Keep me.
Tyler Yahn (Splunk) 00:37:53 Maybe they just track an issue, or something like that, yeah.
Okay, cool.
Move head sampling to eBPF. This is a cool PR, we don't need to look at it. I'm probably gonna park this until after a V1.
Because it's huge. But it's just a proof of concept that got it working.
It's probably gonna have massive, conflicts.
Marc Tudurí 00:38:19 No need time.
Tyler Yahn (Splunk) 00:38:21 We'll talk about it. Next up, first DNX, or fixed DNX capture, so pure endpoints get named correctly.
Nikola Grcevski 00:38:28 Yeah, this is the one that you and I have been looking at. Yep.
I think he… He just, responded.
Tyler Yahn (Splunk) 00:38:37 Yeah. Yeah.
Nikola Grcevski 00:38:42 Yeah, he claims he's fixed, all issues, so maybe you'd want to take a look at your comments.
I did try to kick off the verifier test, but I don't think it ran.
Oh.
It looked at it. Okay.
So I guess… I guess it… yeah, I need to check that, okay. Because it wasn't happening for a while, but I think it just needed, Yeah, we probably need to help restart those timed-out tests, but, but it's… It's looking like it's passing, so… unless the verifier died.
Yeah, seems like…
Tyler Yahn (Splunk) 00:39:22 And CI has been… Rough this week.
Nikola Grcevski 00:39:26 Oh, and GitHub.
Tyler Yahn (Splunk) 00:39:27 Yeah, that's what I meant, yeah.
Good God.
Nikola Grcevski 00:39:31 Probably co-pilot coding instead of…
Tyler Yahn (Splunk) 00:39:35 Yeah.
Okay. Yeah, I needed to take another look at this one. Yeah.
Nikola Grcevski 00:39:41 I'll check that link now to see what might happen. Is the verifier passing?
Right. Because he added some X-ray structures there, and I think, yeah.
Tyler Yahn (Splunk) 00:39:55 Yep, yep, okay.
Nikola Grcevski 00:39:57 We'll see. Still gone. Still gone.
Tyler Yahn (Splunk) 00:40:00 Yep.
Okay, enable eBPF PID filter…
Nikola Grcevski 00:40:06 Oh, yeah, this… this one, yeah. I completely… I always forget about that. It's just not possible to run multiple at parallel, man, that's just… I don't know if you fixed it, but it's good you caught that. I was like, yeah, it looks good, and then I'm like…
Tyler Yahn (Splunk) 00:40:21 Yeah… He says he did, okay.
Nikola Grcevski 00:40:24 Okay, so he added some sort of, like, a channel, I guess, to which we kind of queued these on and pulled them up.
I think it's valuable what he… he does, it's like, and essentially, he wants… He wants to unblock.
The Instrumentation pipeline And not wait for the Java to… to be attached.
Which is kind of cool, because… All you really lose is context propagation.
capability, or TLS, but you still get everything else going, and then eventually…
Tyler Yahn (Splunk) 00:41:02 Yeah, right.
Nikola Grcevski 00:41:02 Eventually, then we can even increase the timeout period for waiting for the JVM.
Realistically, because it's async, so eventually it adds the agent, and… all good data starts flowing, but for any Java process that's not doing TLS, we're sort of waiting in 10 seconds in the pipeline for It's not a bad idea.
Tyler Yahn (Splunk) 00:41:25 No, I definitely agree. Like, I… if he can get this… again, I haven't looked at what he's done, but yeah, Yeah, I'm excited about that as well.
Nikola Grcevski 00:41:34 Clear.
Tyler Yahn (Splunk) 00:41:36 Okay, needs more… more eyes on that.
Add generic OTLP logs… oh, I think we…
Nikola Grcevski 00:41:44 Yeah, let's closed that one.
Tyler Yahn (Splunk) 00:41:45 Tp injector… Perfection.
Nikola Grcevski 00:41:49 Oh, that's a no-go, we can close it. I don't actually, I've asked this user here for, Okay, so long story short, a user's saying that, the, the backup plan we added, Mattia added, for, fixing the bug in the kernel for FION read.
Does not work poorly for them.
And there's a mention of an ePaul Something, but… Further down, there's even a mention of a kernel patch, or is that in the issue he opened?
I've asked for a reproduction case. He claims that this fixed it.
But… I mean, adding a… so, the thing that I've discovered is that Adding a fake ingress, or a dummy ingress path of verdict.
does resolve the original FION read. However.
this breaks when you do this, and I'm not sure how this API is even… Possibly a valid API in the eBPF?
Maybe we're doing something wrong, but I don't think so. I'd spend a lot of time spent a whole day looking at this, and essentially any socket that does splice the Linux kernel called splice when they're sort of trying to stream one socket to another completely breaks with this verdict. As soon as you attach the verdict, those sockets don't work.
And one common one that does that is Docker Proxy, or any proxy. I think Istio proxy, same thing.
Any… anyone does splice, the verdict just breaks that application.
It could be just a dummy verdict. As soon as you start tracking the socket, it fails.
So… It just doesn't respond. There's no, like, the… they have no idea that traffic is coming through.
Yeah, I… I couldn't tell. I did kernel traces, I did S-trace, and it just sits there, stuck.
So then I was like, does anybody use this verdict? And I can't find evidence that anybody in the world uses this, program type.
And it's so strange, because there's, SKB Stream Parser, which is also attaches to the ingress. There is an SKB StreamVerdict, which is supposed to be only for TCP calls. And then there's SKB Verdict, which is what this PR uses, that they all seem to be documented, and there's… examples how to do this, but none of them work, actually. I actually tried also the stream verdict, same problem. As soon as you attach it to Docker proxy sockets, it… Docker Proxy never… you just get a timeout curling into Docker Proxy.
no OB. I can just write a simple reproduction case.
run a Docker proxy, attach a Werdic program to this socket, It just doesn't respond anymore.
actually completely breaks my Linux… network, as well. Like, a lot of things break. As soon as you attach it, they start adding sockets randomly to the verdict. Bunch of stuff on my… Kernel stops working.
So we can't actually accept this, we must close it, but… There's comments in the issue.
that he opened related… I think he opened a bail issue.
This is the sibling.
I've actually looked at… I think this is AI-generated, because I looked at the comments he made with the commit hash or whatever, that has nothing to do with ePaul.
The stuff he's mentioning here… I don't think it has anything to do with ePol. I looked at those kernel patches, supposedly the ones that broke this.
I can't make sense out of this, to be honest.
Matt 00:45:53 I was curious to… to see a reproducer from the original poster, because, if that… if that's, if that breaks EPOL as well, all, like, Node.js should stop working, all the… everything that is not, basically, Java or NGINX or .NET.
But I don't think it's the case, because it's months that it's broken like this, and no one has complained about… that case.
Nikola Grcevski 00:46:23 So there's two people that actually claimed that this failed to them. If you see this niche and share chat.
Which is, I don't know, but there's somebody else which, even with bad words, this, this one.
Distributed tracing has gone for a toss.
I mean, my understanding is in British English, that's pretty bad, so I don't know.
I didn't know what gone for a toss means, but I think it's a swearing of some kind.
Steven, if he's on the call, he can actually… Shed lights into.
The specific use of it, but
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:47:01 I'm far too polite to do that, Nikola.
Nikola Grcevski 00:47:13 So, I don't actually… I don't know…
Tyler Yahn (Splunk) 00:47:15 So, like, you know, just keep in mind, though, that, like, these could be the same person, just a heads up.
Nikola Grcevski 00:47:20 It could be.
Tyler Yahn (Splunk) 00:47:23 Yeah,
Nikola Grcevski 00:47:25 it could be the same people, or… I mean, originally it was reported as it's, it's slower.
I don't know if just… This changes timing somehow for them, and things go awry… the… the only thing that I'm thinking of is… potentially, the workload under test is Node 16. That's quite an old node version, and the reason why, maybe we can't reproduce it, because I tried hard. I got a node service, I had a broken kernel, I disabled… own read. I actually know it works fine.
NGINX fails, but Node just never had an issue, and Matias patch does not affect what Node does at all.
I'm wondering, though, that maybe it's the Node 16 API, so… I'm gonna try that today, see if I can actually get an old node version, And… see what they do. Maybe that's broken for real.
Tyler Yahn (Splunk) 00:48:37 Going back to the issue, though, can I assign this to you, and then have you close it, and then explain, like, the next steps that you're gonna take?
Nikola Grcevski 00:48:45 Yeah, yeah, I think I'm just gonna close as that this is not workable, we're still working for.
Tyler Yahn (Splunk) 00:48:50 Absolutely.
Nikola Grcevski 00:48:51 We'll keep the issue open, but the PR needs to be closed, yeah.
Tyler Yahn (Splunk) 00:48:55 Yeah, okay.
Yeah, let's… let's do that. That sounds… that sounds like.
Nikola Grcevski 00:48:58 And he confirmed, actually. He confirmed later, if you want to look at the comments, he said, yeah, I think you're right.
I tried with… with this patch on some NGINX, and it broke out of stuff.
Yeah.
set small Node.js payload.
I don't know.
Tyler Yahn (Splunk) 00:49:19 Yeah, reproduction would be really helpful still.
Nikola Grcevski 00:49:21 Yeah, that's what I asked for, yeah.
Tyler Yahn (Splunk) 00:49:24 Yeah.
Okay.
Alright, let's, let's move forward on that one.
Thanks, Nikola, for taking a look at that.
Next up, deprecate the application spans. This is, Nimrod, if I'm not mistaken.
Yep.
I'm guessing this is waiting on a review from me. I haven't taken.
Nimrod Avni 00:49:47 Yeah, I think I just resolved, yeah, the few minor comments, or resolve,
Tyler Yahn (Splunk) 00:49:52 Okay.
Nimrod Avni 00:49:53 For the more…
Tyler Yahn (Splunk) 00:49:54 Yeah, yeah, I just haven't… yep. Okay.
I can take another look at this.
Make integration tests fail fast, yeah.
I'm pretty… pretty tempted to just close this.
Like… It… I don't know why this has been so problematic.
But it's been open for, like, a week or two, and I have not had CIA succeed at all, so… I… maybe I'm, like, just not that smart, but, like, if this isn't working in the PR, like, I'm not super motivated to get this merged, I, I don't know… Steven had a great suggestion, because, like, I think this… I came to the same conclusion right about the same time, is, like, don't… end all the things early, just end the, you know, the particular runs that are gonna fail early, which I'm doing now, but I'm still, like… I mean, I just kicked these off this morning, and they failed again. Like, I don't know what is going on.
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:50:53 I think the problem is because there's so many different flaky tests.
Every time you run this thing, there's one, like, different failure.
And it's kind of hard to get everything to pass, like, the entire… all the checks to pass, unless you have… like… Multiple layers of retries.
So what we have in Maine with… You know, the retries.
On the individual tests themselves, and then the retries on… Like, individual shards.
It's, I mean, it's not great, because, obviously, the test suites.
flaky enough that if you do turn any of the layers of retries off, that you just can't get the PR to go green.
That's, that's not great.
Nikola Grcevski 00:51:40 It seems like we need to work on it more.
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:51:42 Yeah.
Nikola Grcevski 00:51:43 Again.
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:51:43 So, the… There should be a report with the flaky tests.
But I haven't looked at it in a long time.
Tyler Yahn (Splunk) 00:51:51 Yeah.
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:51:53 I should make some time to… to go through that.
Or, you know.
Nikola Grcevski 00:51:56 I don't close it just yet.
Amy.
Tyler Yahn (Splunk) 00:51:59 I mean, we could always open it up again.
Nikola Grcevski 00:52:01 Okay. It's not.
Tyler Yahn (Splunk) 00:52:01 Yeah, like, yeah.
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:52:04 Anyone else is welcome to look at the Fleggi test report as well, then.
Nikola Grcevski 00:52:08 Here.
Stephen Lang (Raintank, Inc. – Grafana Labs) 00:52:09 See how it's doing.
Tyler Yahn (Splunk) 00:52:14 Yeah, I mean, we can always reopen this. It's also hard to recreate, it's, like, 14 lines. So, like.
Yeah, I think… I think you're right. I think that's exactly… I think I'm cutting off retries that were… Masking some things, which is great, because then it's passing, but… Okay, let's just… just… Kill it, move on. Okay.
Next up, fail schema generation on duplicate config types. Yeah, I think this might also need another review from me, if I'm not mistaken.
Yes.
Okay.
Also on my list… Other… it also needs another review on that one as well, if folks haven't taken a look.
Add OB's emitted telemetry schema…
Nimrod Avni 00:53:02 Yeah, that's waiting on me, I… I think I… after your review, I realized it's a kind of a wider change, because we need to define… I did it, I think, not only for metrics, but I need to define all the resources that OB emits, all the, like, spans and span attributes, I want to define them… Like, it's kind of load-bearing, because we need to define them explicitly, because we want to, like… we don't want to import the entire SimCov, but just what we use.
But there's also some bugs in… I don't know if it's Weaver, or in general, like, telemetry schemas, that you don't have a lot of ability to kind of refine Like, take an attribute or metric and kind of refine it and remove, for example, some enums or change them, so you kind of need to redefine everything.
So I have something, like, I haven't had too much time to work on it, but I have something, so I'll try to get it in soon.
Tyler Yahn (Splunk) 00:54:08 Okay.
Alright, yeah, I will keep an eye open then. Thanks for the work on this, though, yeah.
White duplicate… this is still a work in progress. It's a bug fix for the next milestone.
Correlate, AOTLS connection. I think this is actually ready…
Nikola Grcevski 00:54:32 I think Martia made a point.
Matt 00:54:34 Nikola left a comment recently, yeah.
Nikola Grcevski 00:54:40 Yeah, let's see what, the author says about that.
Tyler Yahn (Splunk) 00:54:48 Yeah, that makes sense, yeah.
Yeah, that's definitely… Kosh is here. Okay, yeah, waiting for…
Nikola Grcevski 00:54:57 Everybody can extend it beyond the 6x11.
Tyler Yahn (Splunk) 00:55:01 Yeah.
A test would be great there, too, but yeah.
Nikola Grcevski 00:55:05 Yeah.
Tyler Yahn (Splunk) 00:55:05 Yeah.
Why did I scroll? Add support for Python runtime metrics, I think this is just in… it needs more iteration cycles between you and, Nikola and, Marc, right?
Marc Tudurí 00:55:21 Yeah. Yeah.
So, I was actually… Nikola suggested to… Another approach.
And I think that, probe that you mentioned, Nikola, is only when you do manual garbage collection.
So, but there… I think there might… must be a way to… Yeah, to attach a probe to even a slim… Tucker, you mentioned…
Nikola Grcevski 00:55:49 Okay.
Marc Tudurí 00:55:50 So, I'm testing now, and… Hopefully it works, because it's gonna remove all the… this crappy… Read their code that is in user space, yeah.
Nikola Grcevski 00:56:01 Yeah, maybe if we can prove that the reader coding user space is not ever going to read something bad, So, I guess I should… maybe we should explain for everybody. The issue is… The issue is that… so what Marc did is that implemented a different way that we read runtime metrics for the first time. So he finds the memory location of of where that is in Python memory of the process, and it scrapes from Ovi the user space. So it's not involving eBPF in any way.
The challenge that I thought about that approach is that So it's… We're reading at the same time as Python runtime itself is writing, and there's no lock here.
So what they write and what we read could be… inconsistent, right? So, any counter that wraps around and goes forwards, we could read part of the old value and the new value.
And we also read one value, then another, then another. I mean, we could sleep in between and read some part of the old, some part of the new. So there's a way to tell that we've made a bad read.
It's okay, and reattempted, and… So on.
that would be okay, but I'm not sure that's possible. So it'll be nice to be able to do the same thing with it for JVM, so… that PR in the JVM pushed all the offsets to the… to the eBPF side, and on a specific point, when we know the JVM has done garbage collection or something, then we know we can pause it there and read the values, because… the process is actually waiting for us to… to read, and the U-probes…
Marc Tudurí 00:57:46 Okay.
Nikola Grcevski 00:57:48 Right, so it sort of fake, creates a sort of implicit synchronization, because the garbage selection is done, and it's about to terminate, or whatever, and then we capture the values.
There's nobody else that will write those.
biometrics.
But if it's not possible, then… you know, I didn't read the Python GC code, I just looked at a couple of GC symbols, there were a few, and that one looked reasonable to me, but if you think that's… There's a few other ones, I can paste them in the slide here.
Marc Tudurí 00:58:22 GC, Donna?
GC underscore Don. That's… that's the one that is… removed in… Any places, but…
Nikola Grcevski 00:58:32 I don't see it in my Python.
As a symbol, so it must be, inlined everywhere.
But there's also, like, gc visit objects, or something like that, that maybe… that one is more reliable.
I mean, I just checked what symbols existed in my Python that I have on my machine.
And… Hi GC Collect, I think maybe you're right, maybe that is, like, only manually triggered, but… Yeah.
Marc Tudurí 00:59:09 But I think with the offsets, maybe we could do that.
Because I think, you can… Get the address of the runtime.
If you have the offsets.
Nikola Grcevski 00:59:26 Yeah, yeah.
You just need a place to stop in the Python runtime, which is a legit place where something… driven by GC activity, and… At the end of the day, yeah,
Tyler Yahn (Splunk) 00:59:42 Okay.
Marc Tudurí 00:59:43 We are right.
Tyler Yahn (Splunk) 00:59:44 up in the last minute. Steven's already dropping. So, yeah, okay, that's… we'll keep iterating on that one. Definitely more…
Marc Tudurí 00:59:51 of you.
Tyler Yahn (Splunk) 00:59:51 So thanks, thanks, YouTube, for working on that one.
Any other last points, people need to make? We've got 20 seconds.
Awesome. Well, if not, then it was good seeing you. I will see you all in a week's time, or asynchronously. Till then.
Nikola Grcevski 01:00:08 Bye.
Marc Tudurí 01:00:09 Bye.
