SIG: .NET SIG
Date: 2025-07-08
Duration: 14 minutes
Zoom Recording URL: https://zoom.us/rec/share/TreiQTxug7UwxveMhks21GBpKwqAehmAh8vJRs_w1lCwbJr4Eb57AQHb2HURmBYK.VkIMSzKF6Ztl6JNz
============================================================

## Zoom Recording Transcript

**Mike "Blanch" Blanchard** 01:39 Hey, everyone.
Alan can't join today.
So I told them I'd host for him.
I don't have any agenda, so if anybody has anything, please add it to the notes.
**Zach Montoya** 02:11 Hello! I I don't actually don't have any topics myself, but I'm on the hotel like.net auto interpretation. Sig. And I thought I would check out what the SDK. Was doing, so I figured I would join.
**Mike "Blanch" Blanchard** 02:28 Hey, Zack?
It's probably gonna be pretty quiet because Raj, he's on vacation to the end of the month.
How's it going on auto instrumentation?
**Zach Montoya** 02:49 Things are. Things are going. The velocity has has dipped a little bit. Things are pretty in a pretty good spot right now. We're just doing a couple of different pocs and extending into some. There's like a configuration Poc, the the file based configuration thing.
There's also some stuff in the profiler. Trying to improve some of those signals. But yeah, right now it's pretty stable, just branching out a little bit more into some other signals.
**Mike "Blanch" Blanchard** 03:22 Did that file based configuration, go stable.
**Zach Montoya** 03:27 I thought it did. Last I checked. There was. They were tracking a one dot o release, but I haven't followed up on that.
**Mike "Blanch" Blanchard** 03:36 Cool.
Alright, Martin, you got the only thing on the agenda.
**Martin Costello** 03:50 This. This shouldn't take long. But so I did the action item from last week. That was us to do. I put a link to that in the agenda. So I collated sort of a few themes of different types of comments that be made about the use of the 9 packages.
And then I summarized, what we thought maybe would be a forward after that. And then a few hours ago, I updated the Pr the only real change. It was basically refactoring. But I've changed the Pr that's linked as the proposed resolution to this to like treat system diagnostic sources like special and be allowed to not PIN to whatever the runtime version for the Tfm. Is, but otherwise it's the same. Pr.
But I think unless there's anything else more you need from me, Bunch, I think that's and that should be enough of a summary for you to chat to whoever it was. You were going to chat to.
**Mike "Blanch" Blanchard** 05:02 Hang on. Second, I was just clearing my desktop here, so I can share this at the right screen. Let's see.
Okay. So we asked for a consolidation of what, like feedback and.
**Martin Costello** 05:30 Yeah. So there's a, there's a few issues where the same question is being asked. So I put 3 examples of that. Then there's 2 examples of issues on auto instrumentation that are related to the higher version.
Then I've put some links to issues that are in the same ballpark or caused by this up in Downstream project. And then I've just put a note of the customer issue I mentioned last week.
**Mike "Blanch" Blanchard** 06:04 This is really good. I'm just thinking I'd like to wait for Raj to come back.
**Martin Costello** 06:12 Oh, no, no, that's fine I used. This is more I was updating, and the fact that I've done the thing.
So unless there's anything else you need from me all the information you should need to talk to him about this and anyone else on the.net team should be all here.
**Mike "Blanch" Blanchard** 06:31 Cool. This is great.
Yeah, I could just I mean, we could just tag like Noah and tarek on here. But without Raj we can't really make a decision, so I think it would be better if we just wait for him to get back. I can bring him up to speed, and then he can lead those conversations. We can go from there.
**Martin Costello** 06:56 Okay. Cool.
**Mike "Blanch" Blanchard** 06:59 Cause, he really needs to form an opinion and then drive it towards whatever his conclusion is.
I think Alan and I are both supportive of adjusting the course.
But we need Raj to also be on board.
So it kind of stinks. We gotta wait a few weeks, but there should be plenty of time to get something in for release.
**Martin Costello** 07:37 Depending, depending on which tact we go with. We might have something earlier than November.
but then we know what we need to do for November.
**Mike "Blanch" Blanchard** 07:47 I haven't looked at your Pr. But it it may be we just move forward with it.
**Martin Costello** 07:53 Yeah.
**Mike "Blanch" Blanchard** 07:55 I'm just.
I'm no longer a Maintainer, and I'm not really involved in the direction of the SDK team, so I just don't. I don't want to make any promises, and I don't want to speak for Raj.
I'm happy to take it to.net, but then they'll probably have the same response like we need to wait for Raj, so we might as well just wait for him.
**Martin Costello** 08:20 Sure, no problem.
**Mike "Blanch" Blanchard** 08:23 Thank you, though, Martin, this is great.
**Martin Costello** 08:25 No problem.
**Mike "Blanch" Blanchard** 08:31 See, I don't think anything else has popped up here.
Alright. Anybody have anything else.
**Zach Montoya** 08:51 Nope, nothing on my end.
**Mike "Blanch" Blanchard** 08:56 The interesting Zack to get the auto instrumentation perspective on this whole thing probably haven't had time to review it. But what the SDK does is, it's it's very opinionated about the levels of its dependencies. So like, take.
I don't know Microsoft. Dot extensions dot login the last release or 2. We've just always bumped to the latest version.
And that causes issues.
And I know auto instrumentation has a lot of issues with like patching dependencies and conflicts. So I don't know if it would help it or make it worse if we change that strategy.
**Zach Montoya** 09:44 Yeah, I I'm not sure. So it yeah. Dependencies are a struggle, especially with the way that as I'm sure you all are familiar with that. The runtime has these like trusted platform assemblies, and then the different bindings operate differently.
yeah, in an ideal world we would just have like a runtime dependency, and we wouldn't have to declare anything. We could just use what was in the Runtime. But I guess, in order to support other users that are on something older. Then, you know, bringing in the new get packages, helps them, but then gives difficulty for us.
Yeah, I haven't support this particular issue too much. I've kind of haven't been too involved in some of our dependency loading issues as of late. But yeah, if if you want some other, some feedback, I can. I can take a look. But yeah, this is a area that we've faced issues with in the audio interpretation time and time again, with just pulling in, either, like if users provide their own SDK, and then we had to work with that, or if they're just on an older platform. And then we had to figure out how to support that without them changing code. It's it's rather tricky.
**Mike "Blanch" Blanchard** 11:04 Yeah, I know it's been. It's come up in the past a lot.
If you, if you have time, take a look at it, maybe bring it to the auto instrumentation, Sig, and just get some more opinions.
I think what we're considering doing is basically for everything other than diagnostic source, like sticking on whatever version the users Runtime is. So if you're on 8, you would get the 8 versions. If you're on 9, you would get the 9. If you're on the 10, you would get the 10.
**Zach Montoya** 11:45 Okay, yeah. I mean, that's that sounds like a good strategy. Just top of my head. But yeah, okay.
**Mike "Blanch" Blanchard** 11:55 It seems to be, if I remember correctly, aspire had the same kind of setup that the Hotel SDK does currently.
And there was a lot of pushback from the community. So they switched aspire, switched its strategy to what I just described.
So to me, that's like the clearest direction that, like we should do what this buyer is doing, and not take an aggressive stance and bump users to packages.
**Zach Montoya** 12:28 Yeah, that makes sense to me.
**Mike "Blanch" Blanchard** 12:30 But that's what we want to discuss with Raj and then take to, you know, our contacts on the.net team which are really Noah and Tarek.
We do get a lot of the aspire team in and out of that sync less so now. But like when they were building that aspire dashboard, and they were doing a ton of open telemetry. We we worked closely with them so I could try to pull in the current, aspire people to get their perspective on it, too, which will be helpful.
**Zach Montoya** 13:03 Who are the latest people that have been working on aspire.
**Mike "Blanch" Blanchard** 13:06 I don't know. Originally it was like David Fowler and James Newton King.
I don't know if they've moved on to other things, but like I can just ping them and say, like, Hey, who? Who should we pull in for this discussion?
**Martin Costello** 13:20 I think they're both still working on it, although I don't know whether they'd be the people that come came to the meet any meeting, but that they still seem to be doing stuff.
**Mike "Blanch" Blanchard** 13:29 They're still pretty active there and then we can probably just look at like who did this work as well.
Eric and Eric's pretty involved, too.
**Martin Costello** 13:42 Yeah, I think I think Eric has looked at the at my Pr, because when I moved one of the dependencies backwards, it broke the aot test, and then he left a comment on. He went, oh, yeah, we fixed the bug in a O. 2, but.
**Mike "Blanch" Blanchard** 13:55 This one.
**Zach Montoya** 13:57 Hmm.
**Mike "Blanch" Blanchard** 13:58 Yeah, Eric has helped us a lot on the aot stuff.
Alright, great Zack! If you have anything, you can just comment on this.
**Zach Montoya** 14:15 Yeah, sounds good.
**Mike "Blanch" Blanchard** 14:22 Alright! Let's give everybody back the time I will. I'll fill in, Alan, on what we talked about, or and he could just go watch the recording, but should be pretty simple.
**Zach Montoya** 14:40 Good.
Thank you.
**Mike "Blanch" Blanchard** 14:41 Thanks, everybody.
**Martin Costello** 14:43 Bye.
