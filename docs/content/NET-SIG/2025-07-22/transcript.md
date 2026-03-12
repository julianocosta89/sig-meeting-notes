SIG: .NET SIG
Date: 2025-07-22
Duration: 13 minutes
Zoom Recording URL: https://zoom.us/rec/share/YTg-BRn4eYZR0tK7RLn8P7qQC21vBGT8vXn61u_8GnPG1sYdYmoKcNGN76Zu8dwq.LOq1XcEP_WtTJEhW
============================================================

## Zoom Recording Transcript

**Alan West** 01:56 There you go!
**Martin Costello** 02:01 Hey! Alan!
**Alan West** 02:40 Go ahead and put your name on the agenda.
Welcome, Martin, joining us as an improver.
Thanks for accepting the offer.
**Martin Costello** 02:54 Thank you for asking.
**Alan West** 03:07 I don't have much on the way of agenda today.
Of course, if any of you do feel free to plop it on cool. Otherwise let's I guess. Take a quick peek at at things, I think.
mirage popped on and helped move a couple things forward in the last day or 2, which is nice.
Don't think that there's too much in the way.
Martin, as usual. I think you're I saw that you're going back and forth with this guy.
So thanks for that.
I just saw this one this morning.
Looks like a pretty small one. This was a follow on, I think, from one of the previous Prs right.
**Martin Costello** 04:15 Yeah, I did. I did a Pr, and then I think Paolo saw it, and then went down a bit of a rabbit hole of more things that could be improved. And I forget who the other reviewer was but me. I think it was Peter being someone else who were like, yeah, let's just stop this one here and merge it. Do you wanna do more changes on top of it. And then he's open this Pr, and he's opened an issue with the proposal for some larger changes.
**Alan West** 04:46 Oh, okay.
Haven't actually looked at the issues I see. Looks like like this top one.
Okay, yeah, there's a lot here.
Any any initial feelings on what he's proposing here.
**Martin Costello** 05:15 I I think, at a high level it makes sense, but I don't know enough about how often the code runs.
etc, to know whether it's worth the effort.
**Alan West** 05:32 Gotcha.
Which part of the Otlp exporter is it.
**Martin Costello** 05:41 I believe this is to do with the Grpc.
X. 40 bits.
**Alan West** 05:47 Okay, so specifically, Grpc and the serialization.
**Martin Costello** 05:54 Yeah, there, there's a bit of the code where there's a like a byte array buffer.
and it doubles it as it needs more space. I think the code, as is at the moment, it just sort of assumes it will always succeed to write into the buffer, and if it goes out of bounds. Then it goes. Oh, it must not be big enough, and then it makes it bigger. I think he's proposing it like properly indexes and checks the bounds and things, and then expands when it computes. It needs space rather than it tried to write, and it went out of bounds. So that must mean that it's got run out of space.
**Mike "Blanch" Blanchard** 06:34 Hello!
I think the idea with the current design is like the Otlp exporter.
you know, using its thread model. It's only gonna ever be exporting one thing.
So the idea is, it starts with some memory. It exports. If it needs more memory, it grows until it's happy.
and then it just holds onto that memory forever.
So you're gonna have some ratcheting, you know, on a cold start, if you're sending big payloads.
But the idea is, you know, once you reach steady state stable state that all just goes away.
So this design seems more like you're gonna keep paying those costs every time you export.
You're gonna keep handing things back to the garbage collector or the pool.
I don't know. It seems kind of unnecessary.
**Alan West** 07:45 I see.
**Mike "Blanch" Blanchard** 07:48 The only benefit here would be like.
you know, you're up and running, and you get some giant abnormal export request, and you take a bunch of memory, and then you never see that again. So now your process is holding on to some giant buffer.
But I don't know if that's like the core use case.
**Alan West** 08:16 Right. It seems like pretty pretty unlikely possible, I suppose, but pretty unlikely.
**Mike "Blanch" Blanchard** 08:22 We kind of do the same thing all over the place, like I think Prometheus works the same way. It's just it's just greedy, takes as much memory as it needed needs, and then it stops.
**Alan West** 08:37 Oh, you mean our our Prometheus exporter, though the one that had manual serialization in it as well.
**Mike "Blanch" Blanchard** 08:43 Yeah, pretty much anywhere. We're writing to a byte array. I think we have the same design where we just keep a single byte array, we expand it as needed, and then reuse it forever.
**Alan West** 08:58 Got it.
Okay? Yeah, I think we can.
I think we can at least comment on this issue.
**Mike "Blanch" Blanchard** 09:04 This. This design here is very similar to like what aspnet core does.
But it's it's different, right? You have many threads, all processing requests that are gonna be generally very different in size, so that pipeline is written very strategically, so that it.
you know, it's reading off a stream of bytes a pipeline, and it's taking chunks.
and then it's passing them as sequences. So you don't need to like. Put them in a single buffer. You get many, many small buffers, and then you just read them out, you know, as you take Json or whatever. But that's a different, you know. That's really more for highly concurrent things, which isn't really what our otop exporter is doing.
**Alan West** 09:57 Yeah, that's to your point that we basically have one thing that we're holding on to at any one moment that we're exporting one batch.
**Mike "Blanch" Blanchard** 10:10 This could actually increase the pressure on the application. If it's constantly taking buffers, just some things to consider.
**Alan West** 10:34 Good points. Good points. Okay.
With that in mind.
This pr, that he's already opened up, which is my understanding, is not an implementation of that full proposal.
having not looked at this pr, is there anything here that intersects with any of those concerns.
**Martin Costello** 11:01 I don't think so. I think I think this is probably something he found, while looking into the like, the original catalyst for him, looking into anything. And this, this is basically it's refactoring the code to do a while loop instead of recursively calling itself.
It's it still terminates in the same condition, but I think it's it looks a bit. It looks a bit neater and easy to reason with than it calling itself trying to get a bigger, a bigger buffer.
**Alan West** 11:39 Okay?
Yeah, that's helpful.
In that case I'll probably be able to give a quick review to that one and just get him heard.
**Martin Costello** 11:50 Yeah, with with that one to review it. I I it was easiest to just open the files individually and look at them, because the diff is a nightmare.
**Alan West** 11:59 Yeah. Yeah.
Okay, I think that's not a whole lot of other activity here.
Is there anything else folks would like to chat through while we're all together.
Oh, I guess there's the contribut, though I've glanced over this list.
but most of the stuff seems to kind of be probably in the hands of whoever the code owners are of these of these various things.
but of course feel free chime in. If there's anything here that you'd like to like to dig into while we're together.
Okay?
Well, should we give everybody's time back?
Sounds good, thanks. Y'all talk to you soon.
**Zach Montoya** 13:24 Thanks.
**Alan West** 13:25 If.
