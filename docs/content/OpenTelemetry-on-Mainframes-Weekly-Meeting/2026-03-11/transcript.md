SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-03-11
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Greg Shriver** 00:50 Hey, Richard, how you doing?
**Richard Nikula** 01:02 Good enough, once I found the mute button, there we go.
**Greg Shriver** 01:06 I burned as me all the time.
**Richard Nikula** 01:09 Such a popular meeting. I say everybody will show up here in a minute.
**Greg Shriver** 01:16 Yeah, I spoke with Rutica, and he's not gonna be able to make it today.
**Richard Nikula** 01:22 Seemed like he had the action items from the last one.
**Greg Shriver** 01:26 Well, he did update the… he did update the meeting minutes,
So, we'll get his second-hand updates, maybe not his first-hand updates. Well, certainly not his first-hand updates.
I think, rudiger put… issue that we talked about last week. You put the link…
And the meeting notes.
I'm just reading through it.
**Jim Porell** 02:11 I'm looking to see if he's online as well.
I know he's always driving his kids at this time, so…
**Greg Shriver** 02:20 Yeah, he told me that he wasn't gonna be able to make the meeting today.
**Jim Porell** 02:24 Oh, okay.
**Greg Shriver** 02:26 Sorry, should have said that.
**Jim Porell** 02:27 Oh, no worries.
I went and looked at the Slack channel first.
**Greg Shriver** 02:54 Well, we got about 3 minutes after, so…
Maybe today will be a short one. Let's see.
Let me go ahead and share my screen, just so we can…
Hopefully everybody can see my screen.
So, not, so I, I did speak with, with,
Rudigo, and he actually put these notes in here.
So he joined the semantic convention, SIG, on the 1898, PR.
And, they… there was some interesting feedback. I think.
The net-net was… they were really talking about the namespace.
you know, whether the namespace should be TPS,
and the other… the other… and if other vendors would support those transaction processing systems. And I think the… the comment was that… and maybe I'm misreading it, maybe…
maybe I'm misreading the comment a bit, but it sounded to me like the only ones that would be interested, or that would be… sort of fall into this category would be IBM and Oracle.
And Oracle is not necessarily active right now, so…
So they, they were wondering whether, instead of TPS, it might make sense to, to go to a, a different namespace, like IBM.CICS and IBM.ims.
So…
And then there's also, I guess, some blogging opportunities to try and, you know, get some more feedback on that.
And, so, I think we'll probably, there's a little bit,
There's, in the actual PR, in the 1898 PR,
I've got up here. Oh yeah, I do.
Okay, so… can you see my screen now?
Like, this… comment from…
**Jim Porell** 05:15 Nope.
**Greg Shriver** 05:16 Yeah. So… so that's, you know.
it might be, you know, if… it might be better to do the namespace that is specific to IBM.
And then, you know, if Oracle comes in again later, maybe they could do an Oracle namespace, and maybe Broadcom could do a Broadcom namespace in the, you know, if they end… if we would end up with something in the transaction processing system.
That fit within a transaction processing system, so…
That seemed to be, like, the general feedback. Maybe we'll get some more color when, when Rudiga is able to join. He said that he wasn't going to be able to make next week's meeting either.
So… so we'll see.
**Richard Nikula** 06:01 The only question, I guess, is if it's the IBM namespace.
Then it gets a little bit confusing when we start
sharing bits and pieces of it, right? So, technically, we could be publishing something that's
IBM Broadcom and CA… sorry, Broadcom and BMC namespaces gets a little bit weird, but…
**Greg Shriver** 06:27 You're right. I mean, it's… you're absolutely right when you have the namespace like that. I mean, it avoids collisions, but the downside to that is that we could
That, within the different namespaces, we could be, you know, essentially emitting the same data, right?
**Richard Nikula** 06:45 Well, or we… or we… right, but then I guess that's the question. If it's something that's in the IBM namespace mainframe, but we want to publish it.
if you publish the IBM version of it, we wouldn't want to publish our own private version of the same thing. I guess that's where it gets confusing about it.
**Greg Shriver** 07:02 No, I 100% agree with that. I mean, and that's gonna be…
I think almost on a case-by-case basis, this is going to be a discussion we have every single time, right?
**Jim Porell** 07:13 See, I think we're better off saying it's the ZOS namespace.
And then, we don't have the vendor conflicts.
Because, you know, because I even… even if it was an IBM main space.
Now, what happens when DB2LUW is different than DB2ZOS? We're gonna have conflicts there, so…
It's almost like you're creating mini standards bodies, and again, We're bringing this down.
We still want… Industry-wide support for this stuff for the mainframe, which is where we started with.
And now it's kind of like IBM's in its own space. You know, how does that change a lot of things?
I don't know.
**Richard Nikula** 08:01 I agree.
**Jim Porell** 08:03 I'd say ZOS namespace makes more sense than an IBM namespace.
**Richard Nikula** 08:13 Now, you could maybe blend the two somehow, right, and say it's an IBM ZOS namespace, or a…
**Jim Porell** 08:20 Yeah, it's an IBM mainframe, just like you'll.
**Richard Nikula** 08:23 Something like that, that doesn't… doesn't tie the… it's not the vendor's namespace, it's the…
**Jim Porell** 08:30 Correct.
**Richard Nikula** 08:30 It's the object that that particular vendor delivered, yeah.
**Morgan McLean** 08:34 That makes more sense to me as well.
**Jim Porell** 08:36 Yeah.
**Greg Shriver** 08:38 Good morning.
**Morgan McLean** 08:41 I snuck in without you noticing.
**Greg Shriver** 08:43 Yeah.
Yeah, I… that… I think I certainly… I agree that that probably warrants a bigger discussion.
You know, or at least more discussion, right?
You know, I can see the advantages either way. I mean.
**Jim Porell** 09:24 Yeah, unfortunately, I just see… More bureaucracy and delays.
I'm trying to go with an IBM one, and…
And what kind of sub-agreements are necessary between vendors?
To make it all come together.
**Greg Shriver** 09:41 Yeah, in the event… in the event that… that… that other vendors other than IBM want to publish something within the IBM namespace. Yeah, yeah, yeah, I can see that.
Because, I mean, we had… I had a similar discussion this, you know, this week with some folks within Broadcom.
And, you know, there's… there's… A desire to be able to emit some stuff that
You know, that might be,
That might almost be product-specific, right?
And then…
**Jim Porell** 10:14 Yeah.
**Greg Shriver** 10:15 You know, and… and… and where do you go with that? I mean, it's… it's… it…
it's compelling from the product standpoint, because for the back-end observability vendors, if they choose not to care about that product, that's fine, right? And not consume anything for that product, but it might be useful for
OpenTelemetry customers who want to do something with the data that's emitted from that product.
**Jim Porell** 10:40 Well, and I'll give you good examples, and I think that's probably where you're going with, you know, IDMS, database.
**Greg Shriver** 10:48 development.
**Jim Porell** 10:48 Not everything on the mainframe's generated by IBM, you know.
**Greg Shriver** 10:52 Well, no, that's true.
**Jim Porell** 10:53 Messaging, you know, that kind of stuff, so…
So it inherits a lot of the properties of the mainframe, but it probably warrants its own
Little subspace as well, or at least his own, you know, his own capabilities.
**Greg Shriver** 11:14 Right.
So, Morgan, you're… you're on a back-end observability vendor. What's your take on… on that, and the namespacing, and…
**Morgan McLean** 11:26 Generally, namespaces to me should be consistent with the way that OpenTelemetry does it. I think that saying… I… I'm not as in the weeds on this stuff as someone like Trask, but, like, I think that…
I have to go look it up, but, like, I'm pretty sure that namespacing by, like, OS name or something is much more consistent than by entire, like, a vendor-specific namespace.
Right, like, we don't have a namespace for Microsoft, we have namespaces for operating systems, and then subtypes of Windows and Linux and various others.
I would want us to be perfectly consistent with the rest of that, like.
Half the value of OTEL is that it has the code and artifacts that people need, the other half the value is the very stringent semantic conventions.
We've got to be aligned with those.
And I joined this conversation late, so I assume when we're talking about namespacing, we're talking about semantic conventions, correct?
We are. Great, yeah, so we should just be consistent. Having an IBM wide one would be strange in the same way as having a Microsoft or Red Hat-wide one would be strange.
**Greg Shriver** 12:30 Yeah, that's interesting, because that was the… I mean, maybe that was the feedback that came back from the Smithson Conventions Call on Monday.
So…
**Morgan McLean** 12:40 I mean, they're the owners of this stuff, right? So, like, those… those constraints that they're proposing aren't just suggestions.
**Greg Shriver** 12:50 Right, but I, you know, they're suggesting an IBM.CS namespace.
**Morgan McLean** 12:57 Sorry, I missed that part. Okay, so I came in late.
**Greg Shriver** 12:59 Yeah, so… They're the ones that…
**Morgan McLean** 13:01 Now I understand. Oh, that is peculiar, then.
**Greg Shriver** 13:05 Yeah, yeah. And maybe I'm misreading the feedback that Rudiga typed in here and in the meeting minutes. Maybe, maybe it might make sense to,
And I think Lewitt may.
**Morgan McLean** 13:18 Is Rudiger joining today, or no?
**Greg Shriver** 13:20 No, he can't join today, and he can't join next week, either.
**Morgan McLean** 13:24 Okay. But, but…
**Greg Shriver** 13:26 But I think we can, I mean…
It's good to hear everyone's feedback now, so that we can have, you know, maybe a,
You know, a further discussion on this, because this, to me, feels like it, you know, needs more discussion.
And maybe just to understand, or better understand, you know, what the actual feedback from the semantic inventions group on Monday was.
**Jim Porell** 13:55 Got it. It might also be that they don't understand…
The… the uniqueness of the mainframe in that regard.
**Greg Shriver** 14:04 That's possible.
**Jim Porell** 14:05 That we're not, you know.
Going back to Morgan's point, we're not trying to be heretics here, we're trying to fit in.
**Morgan McLean** 14:14 Yeah. Put it.
**Jim Porell** 14:15 It's a new type of object, and it definitely has different oper…
Different operating characteristics, and scale, and, and, and…
**Morgan McLean** 14:25 So maybe this is them just saying, like, I don't know how to deal with this, please just put it over here.
**Greg Shriver** 14:29 Yeah, right, right.
**Morgan McLean** 14:31 Yeah, which is probably not great. Alright.
**Greg Shriver** 14:37 Yeah, so I'm glad that, that all of you.
**Morgan McLean** 14:41 you know, have, you know, are articulating this feedback, and Morgan, I'm also happy that you're here to hear it.
Yeah, absolutely.
**Greg Shriver** 14:52 I was like, this isn't what…
**Morgan McLean** 14:53 Do we know who Rudiger talked to? I just… I can reach out to them and just get their direct feedback, because, like.
**Greg Shriver** 14:58 Yeah.
**Morgan McLean** 14:58 Is it enough from Semconv that…
I'm surprised that they suggested this, but they probably have their reasons, and I can find out what they are.
**Greg Shriver** 15:07 So…
So let me go back to… so this is, this is Rudeiga's… what I'm sharing on my screen right now is Rudiger's, 1898. This is the TPS doc… the TPS PR.
And, that's lunatic.
**Morgan McLean** 15:25 I work quite well. Yeah.
**Greg Shriver** 15:26 Okay. I don't know how to pronounce… okay. Ludmiller. So, and I think she… well, she's on the semantic conventions?
**Morgan McLean** 15:34 Yeah, and on the technical committee, yeah.
Knowledgeable about this stuff, yep.
**Greg Shriver** 15:41 Okay, so… and I guess her take is, if it's unlikely to get a second system to support.
**Morgan McLean** 15:47 I see, but this is specific… so when we talk about transaction processing systems, this is not the entirety of…
the IBM mainframe ecosystem, correct? This is a specific piece of it?
Now I understand. Okay, so her statement is specific to TPS, it's not specific to the other IBM mainframe stuff, and I joined late, I didn't quite understand the context there. And so, the statement she's making is…
It's likely that this is the only transaction processing system that will ever be submitted to OpenTelemetry.
**Greg Shriver** 16:18 Right, and at that point, she's like, why make… like, at that point, yeah, chuck it under an IBM namespace, because…
**Morgan McLean** 16:26 Oracle's not involved. I don't know if I… well, I mean, it's a sig discussion, so clearly other people talked about it.
That doesn't seem totally out of whack for me, if this is specific to the TPS parts.
**Greg Shriver** 16:41 Okay.
**Morgan McLean** 16:42 Yeah. Okay.
**Greg Shriver** 16:42 So, I guess, to everyone else on the call, I mean, do you see…
Do you see, you know, what other transaction processing systems could you see.
**Morgan McLean** 16:56 Because if you can bring another example to Lyudmila, she'll say, you know what, nope, make it standard, like… but she, like I, we're both ignorant of this part of the market. So are there other TPSs that we…
**Jim Porell** 17:09 Well, the problem is, Yeah, well, within the mainframe, there's multiple TPSs.
some of those TPSs like, for example, kicks.
It does run on AIX, on Linux, on other operating systems.
**Morgan McLean** 17:30 Yep.
**Jim Porell** 17:31 And so… there's some parallels there. There's…
**Morgan McLean** 17:35 All IBM…
**Jim Porell** 17:36 No, they're not all…
**Morgan McLean** 17:38 Oh, okay.
**Jim Porell** 17:39 No, they're… I shouldn't say that. Well, I think Broadcom, you could declare that you have a TPS,
You know, if you wanted to go there, so, I think…
**Morgan McLean** 17:56 In that case, then, Jim or Greg, if you can just reply back on this, pull request, just saying, like, hey, FYI, like, here are a few different examples of, like, hey, Lude Mill, here's a few other examples of TPSs, it probably…
makes sense to not just nest these under IBM, then, you know, again, like, she, like myself, is probably fairly ignorant of…
Of… of the availability of these, because none of us, neither of us have worked on mainframes much.
So if you can show her that data point, she'll probably say, like, yep, then this should be a standard.
**Greg Shriver** 18:30 So, for me, I know I'm one of the Broadcom representatives on the call. I would have to reach out for comment within Broadcom to…
Get a better understanding of whether there would be any appetite for doing that with some of the
things that could be classified as transaction processing systems within Broadcom.
**Morgan McLean** 18:53 I think it's less that we need them to go sort of adopt the standard or something, I mean, obviously that's desirable and you should do it, but I think it's also just showing Woodmilla the evidence of… because, like, I'm guessing her and the rest of the SIG in the discussion aren't aware that these other things even exist.
It's less than a statement of, like, we need these people to come help us, and it's more like.
I don't know, is this the only… is the only one in existence from IBM? Then sure, call it an IBM thing.
**Jim Porell** 19:19 No, because I just thought of another… it's another one. It was IBM originally, but Kix VSE is now owned by 21st Century.
So… Yeah.
That kind of fits in there, too, but…
**Morgan McLean** 19:32 I would just… one of you guys who know more than I do, because if there's a follow-up question, I won't be able to answer it. Just literally just reply on this PR and just say, like.
Hey, FYI, here's a bunch of these, and some of them are not all IBM.
**Jim Porell** 19:44 Alright.
**Morgan McLean** 19:46 Probably all they need.
**Greg Shriver** 19:48 Jim, can you take that and.
**Jim Porell** 19:50 Yeah.
**Morgan McLean** 19:50 And mention in that comment that we discussed it, like, the group of us discussed this.
**Jim Porell** 19:55 Yeah. Okay.
Alright, will do.
**Greg Shriver** 19:58 Cool.
Cool, thank you. And I can… I can, you know, get…
get some more feedback, from the Broadcom side as well.
**Jim Porell** 20:07 Yeah, because I understand you don't want to make a business commitment that an IDMS or something like that is going
support.
**Morgan McLean** 20:13 That's not what we'.
**Jim Porell** 20:13 We're going to future support,
open telemetry, but the fact that it exists and could, potentially, is good enough for the answer. And so, I can answer that.
Without making a business.
**Greg Shriver** 20:27 Yes, correct.
**Jim Porell** 20:27 commitment for Broadcom. Perfect. So, yeah.
**Greg Shriver** 20:30 Beautiful.
**Morgan McLean** 20:31 That's exactly all we need, right? Like, it's just another example of people like me in OTEL just not knowing a whole lot about mainframes.
**Greg Shriver** 20:38 Awesome.
Thank you. I'm so glad we had this discussion. Yeah, that's why I'm here.
**Jim Porell** 20:45 And I don't work… and now I don't work for IBM, so I'm kind of independent as well in that regard, so…
**Greg Shriver** 20:50 True, yeah.
**Jim Porell** 20:54 Okay.
**Greg Shriver** 20:57 So… so, okay.
Is that good, Jim?
Oh, it's true.
**Jim Porell** 21:21 Boom in, yeah, that's fine.
**Greg Shriver** 21:22 Oh, sorry, yeah, it's pretty slow.
**Jim Porell** 21:24 No, no, no, no worries. It's all good.
**Greg Shriver** 21:27 How's that?
**Jim Porell** 21:28 I mean, sticking my face 2 inches from my screen, but…
**Greg Shriver** 21:31 Yeah. Is that better?
**Jim Porell** 21:34 That's fine, yeah, it's all good.
**Greg Shriver** 21:36 Okay.
All right, okay, so we've talked about the 1898 PR, we've talked about, you know, at least secondhand Rudiger's, comments, and you can follow these links here if you want more.
The other open PR is this dock PR, and I still have the next action. Rudig and I are…
going to meet on this. He's gonna help me…
Deal with some of the,
some of the mechanics that I'm just not familiar with.
So, so I'm hoping to make some progress on that, before the next call.
And then, of course, there's this open issue
Which I just actually had a chance to read through, which is kind of interesting. It's… I think…
And, and I…
kind of look at a very high level, it sounds like there's high CPU usage when the OpenTelemetry collector with a given configuration at a given release is running on Linux 390.
But there's no comparison between that and running the same configuration, same release on an x86.
So I think it's… it seems to me like there's kind of more questions and root cause analysis going on than… than anything else, but anyway, that's… that's my read after
After looking at it for a grand total of, like, 20 minutes, so…
If anyone is interested, you might want to take a look at that and just kind of read through it.
**Jim Porell** 23:16 Well, that was my hypothesis from last week's meeting, is…
**Greg Shriver** 23:19 Yeah, yeah.
**Jim Porell** 23:20 you know…
we could just be killing them. I mean, the ZOS could be killing them with the volume of data that we ship out, and…
I'd like to know, you know.
Are we killing everybody equally, or is this unique to that particular instance of a collector?
**Greg Shriver** 23:42 I… I agree.
I agree. I… I think it… I agree that it's an open question. Is it… is it really…
Is it really something that the collector doesn't run well on that architecture, or is it just that we're…
We're… we're scaling it to… X.
I don't know.
**Jim Porell** 24:01 Yeah.
Yep.
**Greg Shriver** 24:07 So, I think from… at this point, it's probably one to follow.
I don't know that, that, yeah.
Other than that…
**Jim Porell** 24:19 Well, we really can't do anything about it anyways, I mean…
kind of an IBM issue. If it's their collector, that's the problem, so…
**Greg Shriver** 24:33 Oh, is that true? So that… so the collector itself is…
**Jim Porell** 24:38 Well, I know there's been discussions about making it open source or something, but…
**Greg Shriver** 24:42 Yeah…
**Jim Porell** 24:44 Kind of out of our… out of this community, you know.
**Greg Shriver** 24:48 Yeah.
**Jim Porell** 24:49 Control, for sure.
**Greg Shriver** 24:51 Yeah.
Yeah, agree.
Okay, well, other than that, I don't have any other items for the agenda, or any… any feedback on any of the items. Anybody else? Does anybody else have anything that they want to add to the agenda, or discuss?
**Morgan McLean** 25:17 Nothing for me?
**Jim Porell** 25:19 Me either.
It's fortuitous, because I don't… Conflicting meeting in 5 minutes, so this is perfect.
**Greg Shriver** 25:25 Perfect. Well, hey, as luck would have it.
**Jim Porell** 25:29 Nope.
**Greg Shriver** 25:30 All right, everybody, well, thank you. I think this was a short discussion, but I think it was really helpful to have, and I appreciate everyone's time.
And, so we'll talk again next week.
**Morgan McLean** 25:44 Alright, catch you later. See you soon.
**Greg Shriver** 25:47 Bye. Thanks, everybody.
