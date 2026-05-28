SIG: eBPF instrumentation
Date: 2026-05-27
Duration: 47 minutes
Zoom Recording URL: https://zoom.us/rec/share/u4qYW0cjmjH2hJTZzo3926TvURUCp4wQ__EzLsaUQKTCkqICtKupPT21_12_Up-9.8pccK349lHdsTv-M
============================================================

## Zoom Recording Transcript

**Rafael Roquetto** 01:22 Hey, guys.
**Antonio Jimenez** 01:25 Hey, honey.
**Rafael Roquetto** 01:26 Yes!
Hi, Andre.
Are you in… are you in a conference?
**Endre Sara** 01:33 No, it's just a coffee place, so I'm going to an eating, I guess.
**Rafael Roquetto** 01:37 Oh, at least you got coffee. That's what matters.
**Endre Sara** 01:41 It's really fancy.
To show you guys the stuff.
**Rafael Roquetto** 01:47 Whoa.
Whoa.
**Stephen Lang** 01:52 Was that perfect?
**Mario Macias** 01:52 What about the…
**Stephen Lang** 01:56 Hello?
**Endre Sara** 01:58 That's good.
**Stephen Lang** 02:04 Andre, were those puddings to your left.
**Endre Sara** 02:06 Well, you would probably call them puddings, but it's a, best cheesecake with piramisu, and sesame mulch with it, and blueberry, really thick, so I guess you could say pudding, but that would be August, I guess.
**Mario Macias** 02:24 One thing, guys, I think, I think you are adding your names and the… and the points to talk today to the May 20, meeting in the… in the document.
Okay, I… now I see that you are correcting it.
Okay.
Let me start sharing my screen.
Okay, it's 5 minutes past the time, so I guess we are everybody, so welcome to this week.
submitting. Tyler and Nicola, can't do it, so I will… I will just coordinate today the meeting.
I see we have some people we, we, knew, Andre, we, we know Andre.
An, Vivek.
Okay, so it's, it's glad to see new, new names and… and new faces.
**vivekbharathakupatni** 04:59 Hi, everyone.
**Mario Macias** 05:01 Hello… Yeah, so, please put your… your items in the agenda in case you want to… to discuss… something… In the meanwhile, I see, Rafael added, Added an entry pointing to… linking to a… to an issue.
What do you want to talk about it, Rafael?
**Rafael Roquetto** 05:33 Yeah, so, Giuseppe had some comments, if you scroll down.
**Mario Macias** 05:39 Yeah, so…
**Rafael Roquetto** 05:40 Basically, let me explain… let me explain to everyone what this is about. So… We're grow… with all these new open, like, OpenAI, all these new protocol supports, we're getting more and more maps for all these customers.
TCP, maps. So… and this… I think this starts to add up in terms of memory consumption, because all of these eBPF maps, they are pre-allocated, unless you… you set a flag, which has its own trade-offs.
So, I was wondering if we should selectively load those, and this is, like, a genuine Question. Not a rhetorical one, in the sense that, We already look… only load tracers.
When… when they are required per configuration.
So, I wonder if we can be more granular. Now, what Giuseppe was saying, and you're here, Giuseppe, so you can add to it if you want, is… he was asking if… what I meant was, during runtime.
we kind of detect a protocol, and then we load something, or not load something? No. That's not what I was thinking, just because this seems… it's too complicated, I guess. Wouldn't be my first… my first approach. But more like, I don't know if we have configurations, for instance, for, let's say, Kafka, like, or MySQL. I don't remember from the top of my mind. If we only detect MySQL when we have large buffers enabled or not, I think we always work with MySQL, regardless of large buffers, right?
**Endre Sara** 07:28 That's right, you don't need… I don't… I think… I think I'm… I'm using Lightbox only for GenAI payload parsing. I think that we… Freeport was without it.
**Rafael Roquetto** 07:38 Okay, so, I mean, then it makes sense to load everything that we're using up front based on configuration.
So, I guess… if this starts to add up, maybe what we could consider is have more, like, protocol selection on the configuration only. So, you can disable, let's say your cluster doesn't have Kafka for whatever reason, so you can maybe disable it, and it will not load, all the Kafka machinery and skip all the checks and all the maps.
I don't know if this is a good idea, I'm just putting it out there, because this kind of goes on the opposite direction of what we were discussing, a few weeks ago. With our configurations already, it's so complicated, and it adds to the config complications, so I guess… Thinking out loud what I should, or anyone else wants to be involved, should probably do is to… Just… kind of… Maybe measure, the usage of everything when we have all the knobs turned on.
and see if it's worth it or not, like, disabling parts of the daily maps. So it was more like a general concern.
Low priority.
**Endre Sara** 08:54 I don't know if this is related, and I don't want to distract, maybe, as well, but… but one of the things that I was discussing with Nicola is sometimes, the loaded DPF modules can take up a significant amount of the CPU, and I was thinking about a way to reduce that load, which I think we're talking about gaps, and I don't know if that may or may not be related to the CPU, but specifically about the gRPC parsing that environment took up, like, 90% of the CPU, and the improvement still keeping So I was thinking about, being able to disable things, but maybe more dynamically, and I'm… maybe that's over-publicating, like, shifting the conversation, but, I… I can measure this with the laptop and stuff, and, It makes an impact on the mode and other applications, which is the problem.
**Rafael Roquetto** 09:53 Yeah, I think this is actually a very good point, that you're bringing.
And, again, this is… this… this is adding up. We had a… someone reported in a particular scenario that, that Obi was adding a non-negligible overhead to a Redis process. And, this is… there was no single, culprit, like, in the code. It was just the sum of all, all the little, you know, like a credit card at the end of the month, I guess. So… Yes, I think maybe then the takeaway from this is that we should probably go back and start measuring this and see what can be done. Yes, there's a bit tension to what I was saying, but I think… but I think it's related. So, there are two aspects. You're talking about CPU, this was more, like, memory-related, but they go hand in hand.
So, maybe what we really need is just, like, to take some time to… to see… Where the problem lies, and then, then we can implement Try to implement a few things, like, you know, selectively disabling things. Not sure if at runtime would be possible, because it gets complicated, wouldn't be my first My first option, but it's definitely on the table, you know, if push comes to shove.
And optimizing things in, in general, I think there's a lot of things to… That we can do is still there. So, yes, I will take note of that, and maybe we can talk about it. If you, Andre, have any, like, I mean, he… any already, like, real-world example that you can share? I don't know if you shared that with Nicola already, but, let me know, because I'm interested on that, so I can… I can profile that.
**Endre Sara** 11:52 Absolutely, I will. Is it okay if I just comment on the issues?
**Rafael Roquetto** 11:56 Yeah.
**Endre Sara** 11:57 I'm gonna stay okay.
**Rafael Roquetto** 11:58 Please. Yes. Thanks.
**Mario Macias** 12:01 Great.
Thank you.
**Mike Dame** 12:03 chime in, too, that this is, you know, something that we were kind of interested to for our use cases, where, you know, just modularizing the different instrumentations apart. I think I've mentioned it to maybe Niccolo before and some people about yeah, everything gets… gets loaded in, and there would be times even tying into some of the dynamic stuff that I'm working on, too, if, some sort of exposure to that, that might even be able to be, like, an API that's used internally in OB, too, to, you know, kind of piggyback off of. But, yeah, same idea, we… we can… detect if, you know, an app is using Kafka or something, in our own Process detection. And, if we could, you know, turn it off.
Even, you know, per app, that's kind of my problem to solve, but just kind of throwing in a plus one for something like this, some sort of, like, refactoring and breaking these apart would be useful.
**Rafael Roquetto** 12:56 Yeah, okay, maybe if you can leave a comment there on the issue with that, just so we don't lose context, and then I can go back, sometime soon and kind of… Reorganize it in some sort of planner, what we can do.
**Mario Macias** 13:14 Right.
**Rafael Roquetto** 13:17 Yeah, that's all.
**Mario Macias** 13:20 Okay.
So we have… Another item in the agenda from Andre.
**Endre Sara** 13:30 So, I opened this yesterday, so I don't expect anybody to read this, but I can reproduce this other sample application, and in hindsight, this is not surprising, specifically related to, much proper capture.
We are basically silently failing when the request is too large, and then we just bail out from the code, not parsing anything. So, what I think we could do in user space is just to do a more permissive parsing, and it's not zero parsing, but I'm not sure if that's right.
I have a test branch where I'm testing this, and functionally, it's good.
**Mario Macias** 14:07 Huh.
**Endre Sara** 14:07 I… my question was on Slack, if this should be done something at eBPF, or just the user space.
I… I am testing with OpenAI, but it's actually a problem with every, Gen AI parser. Strangely, this was already implemented for Gwen by Hybrid. So I'm just trying to think of, like, to be generalizing Gwen, parsing to all OpenAI parsing.
So that we don't fail and degenerate the place where we can install the model on site.
**Mario Macias** 14:44 Okay, I'm… I'm pretty sure, famous last words, it's… it's a… it must be some… some check that this shouldn't be where.
Where it is. Yeah, Mattia?
**Mattia Meleleo** 14:58 Yeah, I tried to look… to have a look at this issue, and I think this is how it's supposed to work. So if the setting for large buffers isn't big enough.
the trace won't be created because we don't have the full buffer. So, this is done because, some, some protocols, it… I don't think it… maybe it's the case for the Gen AI stuff as well.
It's JSON, so if we don't… if we are not, if we don't have the full buffer, we are not able to, un-martial that.
**Endre Sara** 15:34 Yeah. Okay, so, so… It's interesting, on the response buffer, before even if it's 100 and not complete, but on the request, you are failing, and I'm actually failing my request because my request starts.
Larger than my background, so, I think it's generated for trace because things can be plugged.
Even if we… it surely the best Jinson doesn't talk normal supermembers, but, Can I maybe just show you my branch, and then, it's completely… But it can be made to work without, you know, breaking something I'd like to try.
**Mattia Meleleo** 16:21 Yeah, I see your point, because right now we… we always fail if some of this response or request buffer is, isn't big enough.
Maybe we can improve something there, maybe we can, we can find some, some middle ground where, if just the response fails, fails, we, we create the trace with what we have.
But that depends on the specific, Protocol.
**Endre Sara** 16:50 Exactly.
So, I think that… I don't actually want to touch EVPF, but if the user is parsing, I could do something, then… that's what I'm trying to do. So, let me show you what I'm working on offline, maybe things you will say.
**Mario Macias** 17:06 Okay.
Yeah, I think this show… depending on the protocol. Even if the buffer is small, if you have enough information to… to… to get what you want from the trace, maybe it's not needed to… to just discard with end of 5.
I see many, many hands… raised. Sorry, because I don't know how to raise the hand in Zoom, but please, I think Rafael raised it first, and then Nick wrote.
Limbra?
**Rafael Roquetto** 17:38 Yeah, yeah, I just wanted to just throw some… something in there. I think we can do incremental JSON parsing, and… and I wonder if that will… Yeah, I was gonna say… you were gonna say the same thing?
Okay, yeah.
Yeah, I don't know.
I've never done it with JSON, I've only done it with XML, but maybe we could do something like this, I don't know, Nebrad, if you have… Any experience with that, or…
**nimrodavni** 18:06 No, I don't have any, like, experience or implementation. Like, I know, for example, the Kafka parcel.
walks with, like, a potion match, like, I think, basically.
I don't know, like, we want to extract, like, specific types, I don't know, like, the topic name or whatever, but we don't need to read the full message because we don't care about it, but as soon as we found it, even if the payload's too big.
then, like, our parser works fine. So I think we can do it, especially with all the recent stuff we added with, like, HTTP large buffers and, like, a ton of protocol parsers over it.
**Mario Macias** 18:44 yet.
**nimrodavni** 18:44 sort of… I guess we need to check, like, the efficiency of it, but, like, having an incremental parser with, like, I don't know, like, if we detect the names of the fields we need, then it's fine, and if there are some optional ones, we just, like.
Don't put them if they're not there, I don't know.
**Endre Sara** 19:06 That seems like people.
**Mario Macias** 19:07 I eat.
**Endre Sara** 19:08 is doing, so… I'm clear at the PR, and, and everybody, comment on my PR.
**Rafael Roquetto** 19:18 Honestly, this, again, we gotta measure… before anything, because maybe what I'm saying is not true, but I… I have the impression that if we can do more of this JSON, like, streaming or incremental parsing.
we might benefit from it, because we do, like, especially in this, AI Code that we have now.
there's a lot of, a lot of, a lot of JSON serializing, deserializing, and… You know, I can only imagine what's going on under the hood, so maybe something… I mean, again, tangent to what you guys are saying, you're discussing functionality.
But, maybe a little bit of connection between them, and… Something to… to look into.
Replacing everything?
**Mario Macias** 20:03 be embarrassed.
**Rafael Roquetto** 20:04 in person.
**Mario Macias** 20:05 I remember from the good old XML times, you could… you had the two modes for parsing, copying everything into a stroke memory, or do this streamed So, I think that maybe it's even more efficient, since we don't have to load the whole XM… the whole contents in memory. We just get the stream, stream parsing, get the data, and discard it. Even for the other use cases, it can be… more efficient. We could experiment.
**Rafael Roquetto** 20:35 Or we switched everything to XML.
**Endre Sara** 20:37 Well, yeah, I think in payload, you don't have a choice to parse whatever you get, but I think that most of what I'm discussing is user space, because the kernel has to do the same thing, even if the user space parser throws away data, so sadly, this does not make the EBPF performance versus water. We're really talking about user base, parsing. I don't think it's too expensive, and I think it could be done safely, and to the extent that I… what I was trying to do is create just one little function that does this, and then apply it across those four or five different Gen AI, without parsing, so that you only have to do this once and not per each pass. Anyway, so… Okay, to be honest.
**Mario Macias** 21:26 Cool.
Good.
So any other topic you want to talk before we can have a quick view to the open PRs?
So, I will suggest we always start, reviewing the open PRs from the bottom, but we end up discussing or putting more focus on the all… on the same PR. So, I… I will suggest start by the… by the opposite… in the opposite direction, from newer to… to older.
So the… okay, the late… the last PR, or the newest PR, is… is from me. It's basically, in the VM tests, we are… it's a security informant. For the VM tests, instead of, instead of, pulling the VM images, we download by tag name. You know, tags are over-readable. For security enforcement, we can pull them by the digest.
So, what… what I added, in addition to… to the modification of the scripts and the YAML definition of all the machines, is also in Renovate. I discovered that in Renovate, you can provide your own renewable renewal policy, so basically it's… I added also to renovate the… a way to renovate the… the images in the… in the… in the VM tests. So, yeah, feel free to have a look.
And provide your feedback, if you like it.
Next PR is from Rafael of Data LALVM22. I see a… there was a comment from… from Mattia, saying that even if we update it to be in 22, Elang is 21. Okay.
There are some mineral… things to be.
**Rafael Roquetto** 23:47 Sorry, I hadn't seen that yet. I just got started. So, what was it, Matthia?
**Mattia Meleleo** 23:55 I think it has to do with the generator image that you use in CI.
So, the CI that is running in this branch is using that image, which is not using the CLANG version that we specify here.
**Mario Macias** 24:10 I think? Hmm.
**Mattia Meleleo** 24:11 And that one in the image is also not using the LLVM20, but is using a 21, which is why I think we should pin the CLANG binary.
Because other than Ceylang, there is also Ceylang 21, Ceylang 22.
**Rafael Roquetto** 24:29 Right. I'm not sure. I mean, I agree we should pin the binary, but I thought that's what I was doing when I installed, or maybe I'm misunderstanding what you're saying.
**Mattia Meleleo** 24:39 No, no, that, that export BPFC lung, that should be, I think, export BPFC.
**Rafael Roquetto** 24:46 Cilante equals cilante.
**Mattia Meleleo** 24:48 2022.
**Rafael Roquetto** 24:50 I see, I see, I see, I see, okay, alright. Now, that makes sense. I was in doubt about it, I was checking this when I was checking this yesterday, playing with the Alpine image.
It's kind of confusing, because if you install playing 22, it sometimes installs only Clang or not, but yeah, I see your point now. I'll see if I can do this and just ping everything to use the… basically, what you're saying is use the 22 suffix when we call the binaries, right?
**Mattia Meleleo** 25:20 Yep.
**Rafael Roquetto** 25:20 Yeah, okay.
**Mattia Meleleo** 25:21 Also, I'm not sure if the generator image is generated, on a request in the CI, or is, pre-generated, and we just pull the image. In that case, we should.
**Stephen Lang** 25:34 We should remind you?
**Mattia Meleleo** 25:35 First update to the image, and then.
**Stephen Lang** 25:37 This manual I created, there's a separate action for it. If you… if you go to the actions, there's, publish generator image.
And you can… you can publish a new generator image either off of main or a source branch.
**Rafael Roquetto** 25:52 Okay, so would you say, does it need to be merged before you're published, or should we publish it and then merge?
Chicken, egg.
**Mattia Meleleo** 26:00 I've so…
**Stephen Lang** 26:00 Oh, excellent.
**Mattia Meleleo** 26:01 I believe we should first publish the new image, and then run the CI on that after we updated the tag.
**Stephen Lang** 26:09 So if you're going to publish, you can't do it from a fork branch, you have to do it as a source branch. That's the only difference.
Because the action won't run from your fork repo. So, you can do it before merge, but it has to be a source branch.
**Rafael Roquetto** 26:24 Okay.
Alright, so you guys reckon I'll run first. I'll publish first.
And then we merge it, if it… And then if it goes wrong, then we…
**Mattia Meleleo** 26:38 If it goes wrong, we revert, no problem.
**Rafael Roquetto** 26:41 Okay, okay, cool, alright.
Thanks.
**Mario Macias** 26:45 Nice.
Well, next PR… from Mattia…
**Mattia Meleleo** 26:57 Yeah, this one, enables a couple of, commented-out tests that, that were not running earlier, from, red, red-out kernels.
And, it fixes some bugs that were preventing the probe to run on these kernels.
There are some refactors in there, because these kernels are more problematic to work with in the sense that they… I think the verifier is older on there, and the number of instructions, it's the limit.
**Mario Macias** 27:36 Okay.
Okay.
Okay, I see Rafael already commented.
okay.
Okay.
Thanks.
Okay, I'll update Docker from Renovate, as always failing.
well, many, many stuff updated, so yeah, it's normal that it's broken. We'll… we'll… we'll have a look.
Later offline, and see what's failing, and many things, and how to fix it.
Okay… This is also created from Mattia. This is already approved.
It's a docu… I understand it's a document.
It's a document update.
**Mattia Meleleo** 28:38 It's not only documentation, I… there is, I think, a discussion.
**Mario Macias** 28:42 Huh.
**Mattia Meleleo** 28:42 with Rafael, so… Yeah, I think it needs another, another pass.
**Mario Macias** 28:49 Okay, okay, it's fine.
**Rafael Roquetto** 28:52 Do you… do you want me to do another pass, or you mean you're doing another pass before I…
**Mattia Meleleo** 28:58 No, no, it's… I think I, changed it, today, or years, yesterday. Okay, okay.
**Rafael Roquetto** 29:05 Alright, yeah, sorry.
**Mattia Meleleo** 29:06 Do I have the comments here?
Yeah, this one. Oh, yeah, I answered there today, so…
**Rafael Roquetto** 29:13 Okay.
**Mario Macias** 29:15 Okay.
Cool?
**Rafael Roquetto** 29:18 Alright.
**Mario Macias** 29:21 Okay, another… thing broken by Renovate. We'll… we'll… it's… we'll have a look later. FTCPIO metric.
**Giuseppe Ognibene | Coralogix** 29:34 Mine?
**Mario Macias** 29:37 Okay, you said that.
Okay, this is a new metric, right?
**Giuseppe Ognibene | Coralogix** 29:43 Yeah.
It's a new metric, and I also needed to change the probe names. I just saw Adobe starts before any probe name.
**Mario Macias** 29:54 That's cool.
Okay.
Okay.
**Giuseppe Ognibene | Coralogix** 30:01 Oh, I also actually incremented the stats event ring buffer. I saw Rafael comment.
Rafael, I did some tests. I know that you said maybe I can do it in another PR, but I ran it, and… Technically, the… The threshold, it should be okay.
Because we have the flash available bytes from user space, which is 3 seconds.
But I guess, that we should… I mean, at least I should run some tests in a node, with higher true boot. In that case, we should see if it's correct or not.
**Rafael Roquetto** 30:45 Okay, I mean, as… it was just, like, more like a thought, so… You know, whatever, whatever you… you think is the best, way forward.
It's good.
**Mario Macias** 31:01 Correct me if I'm wrong, even if you said max entries to 1 million doesn't mean that the space is reserved, or is static, right? It's… it can grow or decrease depending on the… On the frequency you write and you read.
**Rafael Roquetto** 31:21 No, the ring buffer is pre-allocated, so…
**Mario Macias** 31:25 Reallocate it and fix, okay.
**Rafael Roquetto** 31:27 Yes, so that's the size of the ring buffer, in bytes, basically, so that's… 1 megabyte?
**Mario Macias** 31:35 or in entries. Sorry, the name of the property is.
**Rafael Roquetto** 31:41 Yeah. Yeah, it says H, but it's bytes, so it's gonna be.
**Mario Macias** 31:44 Okay, okay.
Okay. Yeah, actually, we don't say the type of the entry, yeah, so it should be byte. Okay, that's fine.
**Rafael Roquetto** 31:57 So it's, it's 1MB, it's not too bad.
**Mario Macias** 32:02 Okay.
Yeah.
Okay, this is, Apply unresolved host rename. This is… this is from Hyven.
Yeah, I actually added, I don't know who added this Donut Merge, I don't know if it was me. I… I added this… this comment. Let me put some… put some… some background here. We have the client and the server host names that, are usually a hostname, and if we don't… if we cannot resolve the host name from the IP address.
It resolves to an unresolved stream.
In address, what we have in client address and server address is we try to resolve the host name, but if it doesn't resolve, we send… we set the address. This is true that this is high cardinality.
But, It's… it's actual… it's actually the ultra-semantic convention for that, so that's why there is the client host name… the client name and server name, and the client address and server address. What this PR does is makes equivalent the… the behavior in client and client address and server and server address.
I don't see it as a super big issue, because at the end, it's true that most people won't use those… those attributes.
But they could use it for traces, for example.
Because even if they are, high cardinality, I think that doing these Fakes.
To prevent high cardinality, what we are doing is not fulfilling the… the… the semantic conventions. So that's why I left the comment here. Also, I left it in the… in the parent… I added the, the, my, my opinion in the, in the parent issue.
So, I think it's… it's worth discussing whether we should… Accept this, this change.
Or… Or not, or yeah, okay, I see… I see the… sorry, I missed the explanation from… from Haibin, so yeah, probably we can… I can read it, and we can continue the discussion offline.
Eurofine?
**Rafael Roquetto** 34:49 Yeah, I didn't know about that, so when I approved it, you know, after hearing your explanation, I feel like we should always stick to the semantic conventions, unless there is a very good reason that everyone agrees. Otherwise, it's not a convention anymore, and then if we keep, for… there's gonna be so many of those, that if we're gonna keep deviating for whatever reason, then we're no longer adhering to the convention. So I think it's simpler.
**Mario Macias** 35:15 Yeah.
**Rafael Roquetto** 35:16 And more correct if you just stick with the convention. I haven't seen what he wrote.
But, I think there's a… I mean… I'm not very experienced in this front, but I feel like if the convention is there, we should.
**Mario Macias** 35:29 Interesting.
**Rafael Roquetto** 35:30 to it. It's not our fault if it's like that.
**Mario Macias** 35:33 Yeah, yeah.
We have this attribute disabled by default.
**Rafael Roquetto** 35:39 Yes.
**Mario Macias** 35:39 It's not a big danger unless someone explicitly adds it, but you see this anti-convention domain name, if available.
Otherwise, IP address or Unix domains of the name.
**Rafael Roquetto** 35:53 Yeah.
Yeah, so maybe, what is it saying there? Like, the explanation?
**Mario Macias** 36:00 So… Let's go back.
Ace… I lost the… Okay.
Or we rewrite client server to the unconfigure placeholder.
To the other address-shaped counterparts.
Yeah, idle end to work option when unresolved is enabled, and the value will be a raw IP. Simply omit.
Yeah, it means… omit… client address. I'm not sure, I… is… is not a… well, we can discuss later. It is not a.
**Rafael Roquetto** 37:00 Yes.
**Mario Macias** 37:01 Just not adding a client address, and if you want If you want… either the host or the IP just using the client or server name attributes?
**Rafael Roquetto** 37:17 Yeah, I feel… I feel like… I feel like, and again, correct me if I'm wrong.
I feel like this is not an issue, after your explanation. If these… these attributes can be, like.
Already be disabled, like, you said it, they're not enabled by default.
So, if you enable them, you're expecting high cardinality, so be it. I don't think there should be any other flags that just… change their behavior or omit them, you know, because they will… if you have this attribute enabled, and then you have a, like, the proposed allow… allow foot guns or disable, that kind of overrides a previous, like, flag, it's just confusing. I don't… Yeah.
on it, is that I would probably, and,
**Mario Macias** 38:04 Yeah.
**Rafael Roquetto** 38:04 So, like, don't go ahead with this, and it's not an issue.
**Mario Macias** 38:08 Yeah, I'm afraid this issue might be abraised by an automatic… AI that maybe lacks this context.
Yeah.
So, would you agree on… just, Rejecting this as not an issue, and close it.
**Rafael Roquetto** 38:32 Yes, I don't know about the others, but for me, that's… that's the way to go here.
**Mario Macias** 38:38 Okay, okay. We'll… we'll anyway, we'll anyway, before closing it, we'll leave… drop a message in the, in the VPF signal?
A Slack channel, just to confirm, and then we can… Okay, let me take a note.
Okay.
Thank you.
I have more… more stuff broken by Docker. We'll have to have a look. I buy Renovate, sorry.
we have… another… change from hybin I can go OpenA to completion on Upro.
We have some comments from Nikola.
And some changes requested from you, Rafael.
they… since they are… they have been addressed.
Cool is if you can have a look, Rafael, or any other… anybody else of us have a second look.
That will… that will refine.
I'm… I got lost.
Okay, this is… this is… We are now entering PRs that we have already discussed in the previous weeks. This is an ongoing task of integrating the V2 format of the config This is a long-term task.
From Florian, event-based Docker container info caching… Okay, there are still some changes… Tyler… I don't know if there is more recent activity, Seems nonetheless, since… last week.
At Telescope uPro, this is a draft.
This is a draft, also.
Some of them are… some of them, if I remember well, are from people that are… We… they got some changes requested, and I don't know if they… If they updated… Okay, there is some… some discussion going on.
No news from… from the last weeks.
**Rafael Roquetto** 41:45 Yeah, I think we can ignore all of those for now.
**Mario Macias** 41:48 Oh, God.
**Rafael Roquetto** 41:49 From this author.
Like, this…
**Mario Macias** 41:51 Okay.
**Rafael Roquetto** 41:52 Yeah.
**Mario Macias** 41:53 Yeah. This, also, this first-time contributor, that looked… that was… too big, it was asked to do some modifications. I don't see… okay, yeah, There are some… some new… there are some… some new changes recently. Failing red tests should be fixed now. I see some integration tests failing.
But maybe they are not…
**Rafael Roquetto** 42:28 I know he's here, right?
**vivekbharathakupatni** 42:29 I'm here, yeah.
I don't know why they are failing, like, this is, like, this is maybe because this is my first time, so I have always had a problem trying to run.
**Mario Macias** 42:39 Yeah.
**vivekbharathakupatni** 42:39 locally, so it's, like, the flaky test, like, for example, the.
**Mario Macias** 42:43 Yeah.
**vivekbharathakupatni** 42:44 failed right now. It runs locally on my machine.
When I try to run it, let's say, even though it takes more time, it's not a big.
**Mario Macias** 42:52 Yeah.
**vivekbharathakupatni** 42:52 right now, is that, let's say, it runs a bunch of 40 or 50 tests. So, if you run all of them at once, they fail, but if I were to run them individually, let's say, like, you know, pick the failing test that runs, and it works. So that's what I've seen locally. So, I don't know whether it's just me.
Or, like, does everybody experience the same problem?
**Mario Macias** 43:17 Some test of time phase. I… I'm rerunning them and see what's… what's… what happens. I wanted to rerun all of them, but only rerun one. Okay, we can… we can… We can execute again when this other finish completes. We can execute the other failing tests.
**Rafael Roquetto** 43:36 So, is it… is it, passing for you? Vivek, right? Is that how I pronounce your name?
**vivekbharathakupatni** 43:40 Yes, correct.
**Rafael Roquetto** 43:42 Yeah, is it passive for you locally?
**vivekbharathakupatni** 43:44 If it's passing for me, yeah, I just ran it right now, like, when it failed, I think, and it runs successfully, yeah?
**Rafael Roquetto** 43:52 Alright, I will… I will… I'm not sure if I will have the time today, but certainly this week, I'll try to… to run it locally, and I'll try to help you, getting this right, and we'll be in touch over the PR.
**vivekbharathakupatni** 44:06 Thank you so much.
**Rafael Roquetto** 44:08 Yeah, thank you for, you know, for contributing.
**Mario Macias** 44:11 Yeah, thank you, thank you a lot.
**vivekbharathakupatni** 44:13 Thank you for all the help.
**Mario Macias** 44:15 Okay, and I think the rest of PRs are just a work in progress, and drafts, and so on, so I don't think it's worth… commenting on… on them. They are, some of them, even a bit old.
So, I think that's all. Any… any other topic you would like to discuss before we close the meeting?
Nope.
So, thank you, everybody, for joining, for your contributions.
And see you next week.
**Rafael Roquetto** 44:55 See you guys!
Right?
**Mattia Meleleo** 44:57 See you, bro.
**Mario Macias** 44:57 I…
