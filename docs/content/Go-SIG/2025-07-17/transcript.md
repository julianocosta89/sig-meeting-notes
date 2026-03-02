SIG: Go SIG
Date: 2025-07-17
Duration: 58 minutes
Zoom Recording URL: https://zoom.us/rec/share/kqQDIGlBMHdGoF3yM4JMzboCmfdSMKRIWL22X4xfi2mAAeeNZf8Sz8iwumBz4-po.2ZbuZIzP0P4V1IkH
============================================================

## Zoom Recording Transcript

**Robert Pająk** 00:10 Hello!
Hello!
**Tyler Yahn** 00:15 How are y'all doing.
**Robert Pająk** 00:16 Fine.
I guess I suspect it will be a stank meeting.
**Tyler Yahn** 00:24 I? Yeah, I was thinking the same thing.
**Robert Pająk** 00:31 Yes.
**Tyler Yahn** 00:45 Yeah, we could probably just jump in. Given
David Salmon, I guess likely, Damien, he didn't explicitly say it. But yeah.
**Robert Pająk** 00:53 Yes.
**Tyler Yahn** 00:54 Aren't going to make it so. Robert, you want to talk about this self observability span metrics. I see this Pr just got opened up.
**Robert Pająk** 01:01 Yes, we can make it quick. I finish it basically today.
So I try to do it by asking for as much issues as possible, because I created the sub issues for all the self observability
and the best like.
I would like this Pr to be, you know, the one that we would like others to follow. If they will be contribute, they will be wanting, contributing some from one perspective along to be good. But also I do not want to make stuff over complicated at the same time.
So I the only thing which is like not clear, like I wanted to propose a different way of
documenting the experimental features. Because I'm not sure if it's this.
Yeah, this is the discussion. I think so. If you go to this hyperlink from the last comment.
So this is an example from the metrics, experimental features. So basically this has this, you know. This is from the readme Markdown. Then below, you have the documentation from the from the Go dog, basically.
And
yeah, and for instance, if you have the features here, you cannot you, it's kind of in the variables, right? So if you go to the variables.
it's not here is in the variables. So basically you cannot have a hyperlink for this feature, because it's a variable, basically.
So I was thinking about simply because this kind of the one benefit of this of this package is that it adds this, at least I see, I say, from my perspective, one benefit is it? You know it decomposes this experimental as a separate documentation. So there's a clear distinction for the end users. What is experimental? What is not?
And I think the other is this variable, so that probably later you can easy find out this. This feature flags right
or.
**Tyler Yahn** 03:12 Yeah.
**Robert Pająk** 03:13 Or or that that is my guess. That was the intention, because in this.
**Tyler Yahn** 03:18 What? What link are you talking about? What hyperlink are you talking about?
**Robert Pająk** 03:22 I'm I mean that, for instance, you cannot create a hyperlink for the cardinality limit here.
So if someone would like, you know if you go up to the top right now to the pure description. Here I make a screenshot of the dog of the go, Doc, that I am proposing here. So basically, I'm creating basically a header for each feature. I'm not creating any variables. The X package is basically just about documentation.
**Tyler Yahn** 03:54 Yeah, I saw that I was a little confused. Why, we're doing that. It seems like.
**Robert Pająk** 03:58 That I thought, that is basically less. You know, it's basically easier to consume from the users that there is not so much information. It's more concise.
and I thought it would be also maybe seem
that it it will be simpler for yeah.
**Tyler Yahn** 04:15 The problem is is that this is bleeding in like.
**Robert Pająk** 04:18 Yes.
**Tyler Yahn** 04:18 This point you're you're including experimental, like functionality inside a stable package which obviously is not exported, but like the whole point of like packaging is to partition across, like.
you know, define functionality within, like some sort of scope, and I think that this belongs in that scope of experimental.
**Robert Pająk** 04:35 Yes.
So that's what I told that this X makes it very easy that you have the slack, and you can easily find it out and which codes to remove later. So yeah.
because I'm not sure if it's easy to to totally re, you know, move all this code to the X package because of circular potential secular.
**Tyler Yahn** 04:56 This is this is the only code that needs to move there essentially.
**Robert Pająk** 04:59 Okay.
**Tyler Yahn** 05:00 Like this just needs to be like, Hey, X. Is this enabled, like we've done for all the other ones? And this would just do the lookup right like.
**Robert Pająk** 05:08 Yes.
**Tyler Yahn** 05:08 Returns, it returns. This, this, this value essentially just gets, returns, whatever that function is right.
**Robert Pająk** 05:13 Yeah, yeah, that's the correct.
**Tyler Yahn** 05:14 So I mean like, and that that would encapsulate the entirety of of the
experimental portion of this, and then this this setup process, you know, when this becomes stable.
let's just say there's an environment variable probably won't be. But whatever like, say, there's some configuration mechanism, that configuration mechanism, just replace. Yeah, it just replaces that that function that gets returned from the X package right?
**Robert Pająk** 05:37 Okay? So I have another question. So I can create this feature flag. And the other question is, the.
are we okay? Because this is one thing, this field and the second one. I also try to move all the documentation
to the basically, you know. Go, Doc format. So if you will be moving this kind of description
to to the main package. Then it will be just easier. Because right now in the yeah, it's just in the go, Doc. So just having documentation like that. So still, I was just thinking right that right now, as a sec, as a second step to refactor, just to have these fields. But keep the documentation, the stability, compatibility. Docs here, instead of Markdown.
**Tyler Yahn** 06:23 Oh,
That's a tricky question.
The problem is that this is not as a rich of a language as Markdown, right? This is definitely a subset of Markdown.
So.
yeah, like, I mean, like, even like this, like this is super critical on, like the formatting here. Whereas like, if you put a space in between here and here. It's gonna get.
**Robert Pająk** 06:48 Yeah.
**Tyler Yahn** 06:49 Messed up here, but it would not get messed up in Markdown right? So like
I mean, I don't. If you have a threat.
**Robert Pająk** 06:59 If you have preference just to keep it marked down. I'm fine. I just want to have you know. You know there are bad pros and cons. If you prefer to be consistent and use reading Md. As everywhere else, we can just do do it. If you think that.
**Tyler Yahn** 07:16 Is, is that what we're doing in the other X package.
**Robert Pająk** 07:18 Yes.
**Tyler Yahn** 07:18 Read me. Yeah, I think there's probably a reason for that. I mean, I think
one of the things one of the things kind of.
**Robert Pająk** 07:27 You were. I remembered, one of the reasons were that you could inline this kind of
kind of code blocks inside lines, and not only as separate code blocks, which was very nice for describing the environment developers. So for instance, here in line 21,
I could make this yeah opting set and variable. So instead of you know, writing like that, I could make a code block auto go accessibly equals true, which.
**Tyler Yahn** 07:55 Yeah.
**Robert Pająk** 07:56 Which is more readable.
**Tyler Yahn** 07:59 I think I think that would be preferable. I know that this is also another thing is like sections like you can only have like 1 1 level of headers, right like there's there's no like 2 2 version. Essentially so.
But like what you've described, obviously like fits within this format. So like, I'm not opposed to going in this direction. But I do think that, like it leads to limitations that may cause us problems in the long term.
**Robert Pająk** 08:23 Okay.
So I will change it today
and do it in the same way as others.
Yeah, it's okay, at least not controversial. We can always change it later. If there is any problem.
**Tyler Yahn** 08:36 Yeah, I mean again, like, it's not super critical. Given, it's experimental packaging and like documentation. But like, I think that we'll be in a position to.
I mean, so I mean, I get it like, it's also kind of annoying.
Because you have to like
push this down. But yeah, I mean, like
a lot of this stuff becomes
way richer in what we're able to actually include here. I guess.
**Robert Pająk** 08:58 Yes.
**Tyler Yahn** 08:59 Yeah, I mean, like this, right? Like, none of this stuff is actually possible in Godocs, right? Like having subsections. So like, I think it. We couldn't do this there, we'd have to
very much change how this is structured.
**Robert Pająk** 09:12 Okay.
**Tyler Yahn** 09:14 But yeah, I mean, I think that makes sense enabled instrument.
**Robert Pająk** 09:21 We don't need it for.
**Tyler Yahn** 09:23 I don't know what this is. But anyways,
yeah, cardinality was the thing that I was thinking about. But okay, yeah, I mean. So like, yeah, you see how this is just like this is like, literally that simple like, that's all we need. Right? Like.
**Robert Pająk** 09:35 Yep.
**Tyler Yahn** 09:35 Yeah.
Okay, any other topics on this one.
**Robert Pająk** 09:42 Nope.
**Tyler Yahn** 09:43 Okay.
okay, cool. Alright. So I'll look for an update. And then you're looking for reviews on that. After that, right?
**Robert Pająk** 09:53 Yes.
**Tyler Yahn** 09:55 All right. Next up, you want to talk about the logs, to reuse the attribute key value and remove the log. Specific attributes.
**Robert Pająk** 10:03 Yeah, I it's just more like a heads up and just asking for opinions. If everyone is okay and all board of it.
I propose to add it, not to the nearest release, because I think, if we would like to have, like the nearest lease, probably, you know, with the next new semantic conventions. Some of the stuff pretty early, and this will require more work, you know. Update all the bridges, etc. So I think we need probably 1st create a release and then work on it also. I will be leaving on vacations, and I do not want to have this work, just, you know kind of
than just, you know, dropped in the middle.
**Tyler Yahn** 10:47 Yeah,
that's a tough one.
I don't know.
So I so here's here's the thing is the only reservation that I have is that we're seeing a large uptick in current use of the logs. Api, right? Like it's not 0, which is great. This is great. That's a good problem to have right?
And so if we switch over to the attribute key value.
unless we update this to support all of these other values, we're going to then immediately limit what we can do in the logs. Api.
So I, you know. Then we have to go update all of our bridges because all of our like. Our bridges do support these conversions to these complex types right like.
And if I'm not mistaken, like, there are switch statements that are expecting.
**Robert Pająk** 11:44 Yes, sir.
**Tyler Yahn** 11:44 Values. So it's like we're obviously gonna have to update it to switch to the new package. But in that process we're probably just gonna have to comment out a bunch of like formatting things.
**Robert Pająk** 11:52 Is the other way. So you have a switch over the you know type.
because we are bridging to the Api.
So that's what.
**Tyler Yahn** 12:00 Saying, yeah.
**Robert Pająk** 12:00 Set.
I think we're single
a map. Yeah. Instead of creating map, we'll just create a Json string. That's what I proposed here before.
And I think it's also what the auto proposes for other signals.
**Tyler Yahn** 12:12 Yeah, yeah, it does.
**Robert Pająk** 12:15 So for the bytes, probably for bytes. We'll also do probably not. Probably some base 64,
and or something like that, I I guess.
instead of Jason, I don't know what.
**Tyler Yahn** 12:27 Reasonable.
**Robert Pająk** 12:28 Base will do anyway.
But I read us. I have no bloody idea.
**Tyler Yahn** 12:36 Yeah, how do we? How are we going to handle empty values?
**Robert Pająk** 12:43 I thought that basically have no idea idea right now.
**Tyler Yahn** 12:50 No, I mean. So that's.
**Robert Pająk** 12:50 Or not.
**Tyler Yahn** 12:51 It's a valid value. It's a valid value for any, though right.
**Robert Pająk** 12:55 Yes.
**Tyler Yahn** 12:55 Can be empty.
I guess. I mean, I don't know. I guess you can kind of just say like, this is the same. You can just put attribute value here and have an empty attribute value.
I think you're right. I think it is.
There's many other parts, I think, of the sdks that won't like this
like I think our exporters may choke on this, but.
**Robert Pająk** 13:17 I will need to double check.
**Tyler Yahn** 13:19 Yeah.
**Robert Pająk** 13:20 Yeah, depending what will happen on the usages. I will probably keep it as invalid, but may maybe just
empty string.
**Tyler Yahn** 13:31 -
**Robert Pająk** 13:31 It's a snow.
but I will say I would say it's an edge case, but we will need to figure it out. But I don't think it's, you know, Super.
**Tyler Yahn** 13:42 That one's that one's actually, I think, pretty important.
because that one, I think, is kind of the key thing. For, like the body stuff like you're going to see a lot of that in the body where you have empty like null values, right? And you definitely want to be able to distinguish between like an empty string and a null value. So we need some sort of way to communicate that.
But I don't.
I feel like I don't know.
I feel like having. I think you. I think you can do this with the attributes package.
because we I mean, we have an empty type. I think there, right. We don't.
**Robert Pająk** 14:13 Have all invalid.
**Tyler Yahn** 14:15 Sure. Yeah. Invalid. Yeah, I guess
But invalid only means empty. Right? Like, I don't think there's a difference between the 2.
**Robert Pająk** 14:24 Right, but at the same time in a long time.
yeah, in the long term it will be safer to have it. Yeah.
**Tyler Yahn** 14:30 Yeah, yeah, I agree. Like, I think we should definitely have something. Not this.
**Robert Pająk** 14:34 But one. I was making the prototype, and I was proposing invalid. I think I have checked all the code paths. Maybe if I even check the the code. And maybe if there's any problem with invalid, probably find it there in this draft. Pr, because I think I was checking all the occurrences of invalid.
**Tyler Yahn** 14:55 Well, so
So there's there's usage of invalid. But then there's implicit dropping of invalid as well.
**Robert Pająk** 15:03 Yes.
**Tyler Yahn** 15:04 The problem. So that, I think, is the thing that you need to be a little bit more careful on, because it may not show up in like a search, or something like that.
**Robert Pająk** 15:12 Or default? Yeah.
**Tyler Yahn** 15:13 Oh, that's not what I want. Why am I in the logs?
Yeah. Yeah. Right? Default.
yeah.
**Robert Pająk** 15:31 And there's a default invalid. It's a string.
**Tyler Yahn** 15:35 Yeah. But then this becomes a problem, right? Because this doesn't necessarily mean invalid. At that point.
Huh!
**Robert Pająk** 15:48 That's why I was thinking of an empty string, because probably the closest thing.
**Tyler Yahn** 15:53 Well, I wonder if it's an empty string, or if it's an empty slice we want to do.
**Robert Pająk** 15:59 Okay.
**Tyler Yahn** 16:00 Right cause. An empty slice and go. Parlance is is
null or nil right? So maybe that
makes a little bit more sense.
**Robert Pająk** 16:13 The question how it work on the Protobuf side.
**Tyler Yahn** 16:17 Well, yeah, I mean, yeah.
**Robert Pająk** 16:19 What's this?
**Tyler Yahn** 16:20 If you.
**Robert Pająk** 16:20 I'm more concerned about the you know what will be exported because.
**Tyler Yahn** 16:24 Well, this is my problem. Yeah, I'm with you. But like right now, this isn't gonna like, if we put if we put an empty string. It won't be right, because it won't be in any value of the correct type. If we put in invalid, it won't be right, because it'll also again be an invalid or a string value. So that won't be right, like we need some way to like get this into like a different thing.
**Robert Pająk** 16:44 Yes, we could, but in the same time we could change it in the. We could change it right
in theory, but it can break, change. It can break other users.
**Tyler Yahn** 16:55 Yeah, exactly. Yeah, yeah. I mean, this is, this is kind of what I'm coming back to is like
as we go through and try to make this work for the logs package like, how much of a disruption is this going to be for the logs? Api users as well as other users, right? Because, like.
**Robert Pająk** 17:11 For sure before, for sure. Make a prototype of changing everything, you know. It won't. Yeah.
**Tyler Yahn** 17:18 Yeah, because I think this is going to be. The key is like, how does that eventually get
encoded in Otlp plus other exporters? Right? Like what? Yeah? And this is, I think,
I mean, another option is to just work on a branch
is kind of the other thing.
but that's a pretty large maintenance burden.
**Robert Pająk** 17:47 I know.
**Tyler Yahn** 17:47 Like that.
Yeah.
So I don't. I don't know. I don't know when we want to move forward with that, but I think we wanna be careful about about thinking through it.
Yes,
**Robert Pająk** 18:02 I'll make a comment that we need to be careful, especially about empty value.
**Tyler Yahn** 18:07 Yeah, yeah, yeah, I think the encoding
complex values is like a string seems reasonable for because, like that would work with the translation.
**Robert Pająk** 18:20 Yes.
**Tyler Yahn** 18:23 I do wonder what did that Otep say about like the empty, because it definitely talked about encoding as a string.
**Robert Pająk** 18:29 I think it says that empty also needs to be added just to the you know, attributes.
**Tyler Yahn** 18:35 Yeah, okay.
**Robert Pająk** 18:37 Bytes. Yeah, the problem is that it won't get stable.
**Tyler Yahn** 18:44 Yeah, well, yeah, yeah.
**Robert Pająk** 18:47 You could make to the end the very, you know.
**Tyler Yahn** 18:51 Yeah,
**Robert Pająk** 19:00 Can search for bytes.
**Tyler Yahn** 19:03 Bytes.
**Robert Pająk** 19:04 Yeah, I think it will be in the same place when bytes are yeah, sure.
empty maps arrays, combination data arrays.
**Tyler Yahn** 19:15 Yeah. But I mean, this is just the definition. But the thing is like,
**Robert Pająk** 19:24 There's no if there's no description how the empty.
**Tyler Yahn** 19:28 Yes, yeah, exactly. And.
**Robert Pająk** 19:30 Encoded.
**Tyler Yahn** 19:32 Yeah, and
hmm.
Well, I mean, it does. Say, I mean, maybe you could encode the empty value as like Jason encoded string of null . Right?
Yeah. And it would be null if it's Json encoded, though. Right?
I think, okay, yeah, that's your key.
Yeah, yeah.
Should not be allowed in an arrays.
**Robert Pająk** 20:18 Yes, it will be encoded to know, if I remember correctly, nearly.
**Tyler Yahn** 20:26 Yeah, but yeah.
**Robert Pająk** 20:28 It will be. No, no string, that's it.
**Tyler Yahn** 20:32 Well, okay. But how do you? Okay, how do you do that?
How do you tell me?
I have this empty array? And I want this eventually, like in the bridge, I'm going to send you something from Slog, and it's going to be an empty array. And then all the way down through the end of the pipeline. I want something to eventually turn into Json with a null .
**Robert Pająk** 20:52 I mean, if you have a Neil in S log, you'll just emit it as an yeah, you will. Just emitted as a node of stripe of of string type.
**Tyler Yahn** 21:02 Okay, I'm saying like, Okay, now go to the next step.
How does that go through the Api?
Do you have an attribute that is.
**Robert Pająk** 21:10 It doesn't.
Yeah, this is just a string, just a string. Yeah.
**Tyler Yahn** 21:15 Well, no, it's not a string. It's it's an empty value, right?
**Robert Pająk** 21:18 I know.
**Tyler Yahn** 21:18 I'm saying like no. So there's no way to like encode that information right now with the attributes.
**Robert Pająk** 21:24 Yes.
**Tyler Yahn** 21:26 So I I don't like we need some sort of solution there, if you want to like, provide that, I guess.
And the problem is, is that like what you just mentioned is like any solution that I think we come up with is we're gonna have some sort of like special identifier.
**Robert Pająk** 21:39 Yeah, you're right, because.
**Tyler Yahn** 21:41 Yeah. And then, if that special identifier gets released
any anything that's not using this this new thing in the exports are going to be problematic.
Yeah, right? Because they
could just give you the special identifier. And like, it would just it would do something unexpected on their part. Yeah.
**Robert Pająk** 21:56 Yeah. And you're right that the body is the most problematic thing, because it's the default value.
**Tyler Yahn** 22:03 Right? Yeah, exactly.
**Robert Pająk** 22:04 Is the default, so the default value will be invalid. Right.
**Tyler Yahn** 22:08 Yeah, yeah.
So I I don't know. I don't know if we can make this change prior to updating the attributes. Package is the problem, which means we could do that, but it would probably need to be done in a in a branch.
**Robert Pająk** 22:30 Do you think, would we still consider making the invalid S in, alias for empty?
Or you think it's not acceptable.
**Tyler Yahn** 22:42 I mean, I do. I think that's I think that's fair. But we run into that same problem.
So it's still the same problem here.
**Robert Pająk** 22:49 Trying to adapt. Yeah. But yeah, you're right.
**Tyler Yahn** 22:53 Yeah, see this? Yeah, like, this is like, no matter what we do to use this special key to identify it. Like
it's not, it's going to change the behavior of the the stable. Api right now for tracing and metrics, which is like intended eventually, but not like right now. It's not stable in the specification. So like
this, I think this actually, the invalid will probably never change in the long term. So if even if we changed it in the short term. That would be. That would be not a good idea.
**Robert Pająk** 23:22 So probably the thing which we need to push 1st it to try to 1st add empty to the specification, to the standard attributes.
**Tyler Yahn** 23:32 Yeah, that's right.
**Robert Pająk** 23:33 To make it stable as soon as possible.
and try to explain why we are blocked by this.
**Tyler Yahn** 23:42 I.
Yeah, I think I think the sooner we can get complex
into the Api that are like all of them, it'd be ideal. But even just.
**Robert Pająk** 23:50 But empty is the most, the blocking one for us.
**Tyler Yahn** 23:54 Yeah, I.
**Robert Pająk** 23:55 This is the default value.
**Tyler Yahn** 23:57 Yeah.
**Robert Pająk** 24:02 Thank you.
**Tyler Yahn** 24:03 I don't know if I'd say Thank you. But anyways.
**Robert Pająk** 24:06 No, no, thanks, really this were great constructive comments.
**Tyler Yahn** 24:11 Okay.
Okay. If, Jenny, you wanted to talk about the cardinality limit next.
**Yevhenii Solomchenko** 24:18 Yeah, I think about the default default value.
It's a 0. I said to 0, because the benchmarks it's gonna have a bit.
**Tyler Yahn** 24:37 You said so. There's no cardinality. Limit by default is what you're saying in.
**Yevhenii Solomchenko** 24:41 Yeah, yeah.
**Robert Pająk** 24:42 In the spr.
**Tyler Yahn** 24:43 Yeah.
yeah, I think if that was what the consensus of all, the feedback was right. Oh, yeah, 0 means not set right.
**Robert Pająk** 24:54 Yes.
**Yevhenii Solomchenko** 24:55 Yes.
**Tyler Yahn** 25:02 Yeah, this looks great. Yeah, are we just waiting on more reviews?
**Robert Pająk** 25:10 I think if Jenny wants to double check, if it's fine.
I think we have free free approvals already, or 4.
**Tyler Yahn** 25:19 Let's double check.
**Robert Pająk** 25:23 Do we.
**Tyler Yahn** 25:24 2. 0, wait! Where's mine? I thought I'd approve this.
**Robert Pająk** 25:28 I have to reach. I have to ask you again because the default has changed. I want to be sure that
sure save it.
**Tyler Yahn** 25:36 Yeah, I'm not.
Yeah. I was fine in 2,000. But
this is even even less impactful. Let me see, I mean, it's just the default. This
there's no limit applied, and so is the plan. Is the plan to always have this be the case.
**Robert Pająk** 25:57 That's my question.
Since you created a that is a comment. How how they made it
impact less, I think, for rust. And I just created an issue of of out of it. I do not understand it. I have not looked into details. I just, you know, created an issue. If someone has time to look at it.
Any thoughts on on your side, Tyler.
**Tyler Yahn** 26:27 I don't like. I'm worried that
so so the specification, it's a recommendation that the default be 2,000 right.
**Robert Pająk** 26:36 Yes.
**Yevhenii Solomchenko** 26:37 Yeah.
**Tyler Yahn** 26:38 Yeah.
I don't. I mean, I don't know. Like if it's if it's a breaking change, then it's a breaking change that came from the specification, like, I think that to be compliant, we want to eventually have a default of 2,000. Right?
I I don't know. I.
**Robert Pająk** 26:59 1st answered more about the performance overhead than having default as 2,000.
Because it's kind of a match case, I would say, to hit the cardinality limit.
**Tyler Yahn** 27:14 Yeah, this is also another question as to like where the cardinality limit gets applied. Did we ever get a resolution on that like? Is it applied in
the measurement, or is it applied in the export, or in the batching.
**Robert Pająk** 27:28 Wasn't, wasn't. You? Haven't create what haven't you created, Pr which resulted, or Seejo?
I think there's.
**Tyler Yahn** 27:37 I mean, there's definitely an issue I had created for this in the spec, but I don't know if it got resolved.
**Robert Pająk** 27:42 I'm not sure if CEO has not addressed it.
Probably you can create your dishes created by you, by by yourself.
**Tyler Yahn** 27:50 Oh, yeah.
**Robert Pająk** 27:57 Cardinality.
**Tyler Yahn** 28:08 this is this.
**Robert Pająk** 28:12 This is the one.
**Tyler Yahn** 28:13 Yeah.
yeah, yeah, okay.
**Robert Pająk** 28:27 Okay.
**Tyler Yahn** 28:28 So I don't. Yeah.
**Robert Pająk** 28:38 I think someone just ignored your ask that
because I think you ask that this should be resolved before stabilizing, and I think someone ignored you.
**Tyler Yahn** 28:50 Yeah, I think you're right.
I don't think I know you're right.
okay, where? Where are we applying this? Now? Where's the cardinality limit in in our.
**Robert Pająk** 29:08 Looks like on the measurement, because
it affects, affects the measurement performance.
Yeah.
**Tyler Yahn** 29:18 Well, okay. So then maybe that's
I don't know. Maybe we just fix it here like I don't.
I mean, I I think I don't know, like I think you want to weigh. I don't know. It's such a mess.
So there's definitely like a cardinality limit that you don't want to send to the back end, because it's going to go into a database right? Like that is important, because it's like you can overload a database, and it may be the case that, like every collection just like this is where your problems coming from is like
every collection is going to have. I mean.
this is dumb. So if every collection has different attribute sets, then, like, you're eventually going to like hit a cardinality limit that like will. Only, you know.
especially, I guess if you're cumulative, I think this is where it matters right. So eventually, like, you're going to just be recycling the same thing. But that doesn't really affect the
the collection limit right? Because, like, maybe maybe you can, you can handle a thousand within that collection timeline. So it's not a big deal. So you want to be applying the cardinality limit on collection, not on measurement.
There may be the other side where it's just like there's so much coming through that you're going to overload the go like memory here, where it's like it's so fast that it is overloading. And so
I don't know, like I think I think we could. I don't know. I feel like we should just we should add something here to address it on ourselves like.
put the put the cardinality limit at the end and then put the collection limit as well as another option
right like, have another thing here that's called collection limit that says, like.
you know, we only allow this number of unique events to come through within a collection cycle. This is by default off.
and when it's not on like you may overload the memory, and when it is on, then you may incur performance
degradation, because we have to do that comparison. Every measurement cycle.
But it puts the choice in the user's hands instead of
like right here. Like, if right right now, we're applying cardinality from the start
at this point. So like the user can turn it on or off.
But the problem is is they're they're not given the choice between
managing the collect like the measurement process, or or the or the cardinality that's sent. They're only given one dial to to handle both.
I yeah, I don't know, like, okay, I mean, like, it's pretty obvious the the
spec isn't gonna address this. So I let's just do it ourselves, like, I don't know, like
I think I think. What I would say is, I'd remove this line and.
**Robert Pająk** 32:26 Not say about the default.
**Tyler Yahn** 32:28 Yeah.
**Robert Pająk** 32:28 Just so. Let's have it specified.
**Tyler Yahn** 32:30 Yeah, I see.
So
**Robert Pająk** 32:33 Changes later, when we figure it out.
**Tyler Yahn** 32:35 Yeah, yeah, and I think maybe we can also then create an issue to track this?
Yeah, because I think I think there's a problem here that
I'd rather like we have a cardinality limit be able to like be by default. But I also don't.
**Robert Pająk** 32:56 I just have a question. Tyler.
**Tyler Yahn** 32:58 Yeah.
**Robert Pająk** 32:58 Is it? Will it be a blocker for the release to have.
**Tyler Yahn** 33:03 The card, not the default.
**Robert Pająk** 33:04 Yes, or you just want to say that the default
is unknown, or it may change, maybe sift.
I think the the documentation should say, what is the behavior, even if it's something which is subject to change.
because people will have issues and they will not be. You know, they will need to look into the code. Basically.
that's my concern.
**Tyler Yahn** 33:36 So the problem is, they'll only need to look into the code. If we set a default of a 2,000.
**Robert Pająk** 33:41 Yes.
**Tyler Yahn** 33:43 The thing is, is that like, if.
**Robert Pająk** 33:45 If it's unlimited, we do, we do not need. Yes, I agree.
**Tyler Yahn** 33:52 And so I think that's why, if you, if you leave it at unlimited and then just don't put it here.
I mean, I don't know. Maybe there just needs to be more consensus like, is there like? Was there opposition? I thought that I saw that, like David, was more on board with doing it in like a stage rollout.
saying that it's going to be changed in the next release, maybe, or something like that. But like I don't
I think it was.
**Robert Pająk** 34:19 I think it was they they mean proposal. But I I was saying that. How will they know that it affects them?
**Tyler Yahn** 34:28 The cardinality limit. You mean.
**Robert Pająk** 34:29 Yes.
like we'll do. Would we ask him to check it, you know. Set it to 2,000, just to check in future if it affects them.
**Tyler Yahn** 34:40 Yeah, I mean, I guess they could do that. But I just I don't know. I'm also just sitting here going like I don't. If you have a cardinality limit of of over 2,000, like.
**Robert Pająk** 34:49 Yes.
**Tyler Yahn** 34:51 It's Gonna blow Prometheus up. So there's no way they're using Prometheus. So it's got to be some other like vendors back end
I don't know like there's also a way to show that the cardinality limits hit, because when it's hit like when you start to use that overflow attribute right? So like.
**Robert Pająk** 35:09 You're right.
**Tyler Yahn** 35:11 It's like it's not like. It's a silently dropped problem.
**Robert Pająk** 35:14 Yes.
**Tyler Yahn** 35:18 I don't know. I just come back to this idea that like it's an edge case, right like there's definitely an error scenario here where you have unbounded cardinality. And what we're doing is we're changing the behavior of how we're handling this error scenario. And if that's the case, like, are we changing it in a way that's helpful to users, or hurt or harmful like.
It's going to be harmful to users that want unbounded cardinality, and that are just like paying through the through the nose on like their back end storage costs. And it's going to be helpful to users that don't realize they're doing this, and don't want to be paying through the nose, and that are having, you know, some sort of issue like I also could see, like, you know. Let's say there's, you know, 2 releases after this, and we have a cardinality limit of 2,000 as the default set and somebody comes along and like the upgrade instrumentation that starts
spewing cardinality right like this is going to save them.
I think if it's still set to 0 like it's it's going to give them the tools to fix it, but it won't be like a fix right off the bat.
**Robert Pająk** 36:16 Yes, I have a proposal.
because I think that in order to have a follow up of this work, I think it's better to merge it as it is.
and just create an issue.
**Tyler Yahn** 36:28 Yeah, I think.
**Robert Pająk** 36:29 The default. If we want to change the description, etc, would you be able, Taylor, to create an issue just to track it about what we want to do with the default. If we plan to change it or not document it so we can change it later and stuff like that.
**Tyler Yahn** 36:45 Yeah, that sounds fine. Let's let's do that. I mean, I don't mean I definitely don't think this should get blocked anymore on this because there's a lot of other work that can get done that does not require like this default stuff.
**Robert Pająk** 36:55 Yes.
**Tyler Yahn** 36:56 Who else are we waiting on, David?
Everything looks resolved.
**Robert Pająk** 37:02 Yes, it's resolved it was the same. I think it was the same concern, mostly.
**Tyler Yahn** 37:08 Yeah. Did David approve this, though?
No.
Is he on?
**Robert Pająk** 37:15 He's responsive on slack. I was talking to him.
**Tyler Yahn** 37:19 He's not gone.
**Robert Pająk** 37:21 No, he's not gone.
**Tyler Yahn** 37:23 All right. Maybe we'll wait just a
**Robert Pająk** 37:26 Can you check his comments?
I think he had 2.
Yeah, he had just nervous about Cardinal team by default, and he had just.
It was just one.
**Tyler Yahn** 37:44 Oh, it's the unexported thing! I I don't think we should do that. I think that's a step. But
yeah.
**Robert Pająk** 37:57 This was a.
**Tyler Yahn** 37:58 Like the thing is, is like also like our version and compatibility. Guidelines explicitly are not defined around behavior.
**Robert Pająk** 38:04 Yep.
**Tyler Yahn** 38:05 They are defined around like the compiled Api, like.
I don't know. This is, this is a behavior that comes down from the specification like if you wanted to argue, this is a breaking change that should have been argued at the specification level.
**Robert Pająk** 38:18 Like this is also not, you know.
positive use case. May. You know, it's not a you know, normal user scenario. This is a different behavior for error. Error, you know error, error.
**Tyler Yahn** 38:33 Error. Scenario. Yeah.
**Robert Pająk** 38:34 Yeah, in our scenario. That was yeah scenario. That was the word I was looking for
in a separate issue.
If any. Do you have any other questions regarding the next issues.
**Tyler Yahn** 39:09 Sorry I didn't hear you. If any.
**Yevhenii Solomchenko** 39:11 No, no, I it's like, it's okay.
**Robert Pająk** 39:15 Okay.
**Tyler Yahn** 39:16 So it'd be, apply the cardinality limits to the aggregation. So essentially just do the implementation with the idea.
Yeah, I mean, that seems pretty straightforward. Have you looked at this already, or do you want me to assign this to you?
**Yevhenii Solomchenko** 39:31 Yeah. You can assign.
**Tyler Yahn** 39:33 Okay, help me with your username.
Why.
**Yevhenii Solomchenko** 39:36 Igreg somchanka.
**Tyler Yahn** 39:39 Oh, sorry!
Oh, man, I am messing this up here. Let me just do this perfect.
**Robert Pająk** 39:49 I'm not sure if you can assign. I think.
**Tyler Yahn** 39:51 Inside, the company.
**Robert Pająk** 39:52 And because he's not in our repository as an approver or.
**Tyler Yahn** 39:57 No, it's not. You're a member of open telemetry. That's the problem.
**Robert Pająk** 40:00 I thought.
**Tyler Yahn** 40:00 Thank you.
**Robert Pająk** 40:01 Remember. But what? Yeah.
**Yevhenii Solomchenko** 40:05 I remember.
**Tyler Yahn** 40:06 Then you should be assignable. That's weird.
That's changed.
Okay, that's not great.
**Robert Pająk** 40:16 I saw it everywhere on Github.
**Tyler Yahn** 40:19 Really, why did they do that? I don't like? What's the point of being a member now like I don't
alright. So.
**Robert Pająk** 40:27 It was.
**Tyler Yahn** 40:28 I guess you'll have to comment on this, and then we can assign it to you. That's yes. Ridiculous is the right word. Okay? Cool.
Okay, follow up task for me.
Okay, Robert.
you want to look at the triage project. Do you want me to leave this? Or do you want to share your screen.
**Robert Pająk** 40:59 I would love you to.
**Tyler Yahn** 41:03 Just.
**Yevhenii Solomchenko** 41:03 You can assign me.
**Tyler Yahn** 41:05 Okay.
there you go. That's weird.
I don't know why they did that. Okay,
**Robert Pająk** 41:20 The bottom.
**Tyler Yahn** 41:21 Triage. Yeah, are these the oldest or newest? Oh, yeah, definitely, newest is on here. All right.
It's aws lambda detector incorrect fast. Max. Memory value
**Robert Pająk** 41:35 Probably low.
**Tyler Yahn** 41:41 Yeah, I think that seems 10 h ago. Okay, yeah, I think that can be a low as well.
Cool improve Eks detector. That does not sound like a bug.
Yeah, this is, I don't.
There's also a bug in that.
I think this is trying to do too much. This is trying to describe a different
requirement or configuration, but it's also describing a bug.
**Robert Pająk** 42:33 Yes, still, I think the owner, the owner of a case detector, should, you know, propose something right.
**Tyler Yahn** 42:47 Sure. Yeah, I mean, I am. Yeah, they definitely should. But
**Robert Pająk** 42:56 Unless there is a.
**Tyler Yahn** 43:19 Okay, well, I.
**Robert Pająk** 43:21 It's too complex.
I will change it from to enhancement, for sure.
**Tyler Yahn** 43:26 Yeah, I, I'm gonna just yeah. That doesn't like, if there's a
problem with the other one, then I think that that can be clarified in its own issue right now. It's asking for way too much here.
Okay.
Detector
aws. Ecs tests are failing locally.
**Robert Pająk** 43:56 This is created by me. It annoys me very much.
maybe just assign it to me.
**Tyler Yahn** 44:01 What
**Robert Pająk** 44:02 It's always. It's always that. This test is always failing on my machine. I was not checking why, but always 100%.
**Tyler Yahn** 44:13 Really? Huh?
**Robert Pająk** 44:14 Yes.
**Tyler Yahn** 44:15 That is bizarre. Okay, I don't.
**Robert Pająk** 44:18 Maybe it's something on my machine.
**Tyler Yahn** 44:22 Yeah, it doesn't work for me, so I don't, or I'm sorry it works for me. So I
I'd want to know, like, why is this failing? Yeah, that's really weird.
**Robert Pająk** 44:36 So the contribut detectors are working for you. The it's working for you. Fine. When have you?
Have you recently run all the tests in go country or not really.
**Tyler Yahn** 44:46 I mean, I could just run this really quick for you.
**Robert Pająk** 44:49 Okay.
**Tyler Yahn** 44:56 It's in. Where is this? Aws? Ecs test?
Yep, going just fine.
yeah, I yeah, I don't have any.
**Robert Pająk** 45:18 Assign so assign to me.
**Tyler Yahn** 45:21 I don't. That's crazy. I don't know why. Yeah, all right, I'll assign to you, I mean, don't think you have to like I'd be interested like I doubt it's just on your machine. There's probably, you know. The thing that I'm thinking is, there may be some sort of like.
**Robert Pająk** 45:32 I can reproduce it.
**Tyler Yahn** 45:34 That's a big part. I can't reproduce it. Yeah.
let me get you some info.
I don't know where I'm obviously
alright. Yeah, I don't know if that helps, but
give you something. Okay, yeah, I got low priority here as well. But yeah, I mean, that's that's frustrating. We don't want that. So yeah.
Did I assign that to you?
**Robert Pająk** 46:35 Yes.
**Tyler Yahn** 46:36 Oh, okay, hotel. Http does not work with Prometheus 3.0. Well, yeah, I don't doubt that.
I mean, this looks like it's got a response I don't like.
If you want to use the new thing we provide a pathway like this. Seems like it's done right.
**Robert Pająk** 47:15 Kind of, but I also saw some discussions in
I think also some discussions in the auto primitives that they want to do, some refine it to make it less impactful. But I do not remember. I was just.
**Tyler Yahn** 47:29 Well that that, I think, is up to them.
**Robert Pająk** 47:32 Yes, but we can.
**Tyler Yahn** 47:33 Control.
**Robert Pająk** 47:34 Instead of doing some global like, it is currently they wanted to set them. Had some, you know, response negotiation and stuff like like content negotiation and stuff like that instead. So it's more, you know.
not global, but more dynamic.
But yeah, it's more on them.
It's more problem with Prometheus, not auto. Http, right?
**Tyler Yahn** 47:58 Yeah, I mean, no, it's definitely an Ios. HP is the exporter. And I think Damien points out that we have a validation schema that should support this in a backrest, compatible way. It's just you need to set it. And so.
**Robert Pająk** 48:10 I was not planned so that
it won't go to the milestone.
**Tyler Yahn** 48:20 Okay.
hotel grp, or superfluous right header call still happens.
**Robert Pająk** 48:31 Is it?
There would be awesome.
**Tyler Yahn** 48:34 Hotel mucks.
We still support Mux.
**Robert Pająk** 48:42 I think we do. Let me check, go, contrive.
**Tyler Yahn** 48:48 I think that might have been one of the ones that left and came back.
Yes, yes, we do. Yep.
Okay.
8 cats is the owner. Okay?
Well, I'm gonna put low priority on this for triage.
Okay, withspan option is not considered when using hotel Grpc stats, handler
yikes.
**Robert Pająk** 49:32 Almost like you might be outside.
**Tyler Yahn** 49:36 Yeah, I mean, I oops, that seems like a problem.
**Robert Pająk** 49:42 Yep.
**Tyler Yahn** 49:45 Yeah. Who's the owner of Delta? Grpc.
**Robert Pająk** 49:49 David, I think, and Damien.
That's that would be my best.
**Tyler Yahn** 49:54 And.
**Robert Pająk** 49:56 David.
**Tyler Yahn** 49:58 Oh, it's just David!
**Robert Pająk** 50:00 Yep.
**Tyler Yahn** 50:09 Okay, hotel. Comp. Cannot use IP address for Grpc endpoint without preventing. Yeah? Well.
**Robert Pająk** 50:16 Low. It's assigned already.
**Tyler Yahn** 50:19 Okay? All right. Yeah, it's a.
This is a tough one.
Hopefully, we do a better job on our hotel Comp than we did on our exporter configuration. But anyways.
this is coming from the spec as well. So I'm interested to see how this goes.
Yeah, exactly. This is yeah. Okay.
**Robert Pająk** 50:38 Pack the Grpc config endpoints, etcetera. This. Yeah. I always so confused about the schemes, how it works, for what language?
Well.
**Tyler Yahn** 50:48 And configuration, because, remember, if you put it in here as a
argument, it'll parse it based on your security. But I think if you put it in as a one of the environment variables. It won't so and it will just fail, because it will have a yeah, it's
it's it depends on how you're configuring it. Anyways. Yeah, it's not great
error, stack and exception type, not being properly set for hotel. Grpc.
clear, concise description of the book.
Yeah. Yeah.
**Robert Pająk** 51:23 There's right.
Tab, bash, hold down.
No.
okay, no, I think I understand. I think someone is complaining that probably they were using other languages, and they thought they will have something interesting. This tax raise.
or things like that.
**Tyler Yahn** 52:22 Not kidding.
**Robert Pająk** 52:28 Probably there was a panic, and there's what. And you know, when you're getting a panic.
then you're kind of you know you. When I think we probably, for 1st of all, there's no repro steps.
but I assume it was a panic recovery when someone put this with stack trace configuration on SDK provider, which basically
doesn't tell a lot.
I, yeah, you can. You can see.
**Tyler Yahn** 53:03 I mean I don't know. It tells you where.
**Robert Pająk** 53:04 And the.
**Tyler Yahn** 53:05 And.
**Robert Pająk** 53:05 So PEI see and finish sector. Yeah.
Span finish.
If.
oh, yeah.
**Tyler Yahn** 53:52 Within triaging.
Okay, alright.
Prometheus Exporter, incorrectly adding units to metric name. And I just saw this one.
Let's got this. Yeah, I was like, well.
yeah, opened yesterday. Looks like it's being addressed. Yeah, it's already got somebody looking at it.
I mean, I.
**Robert Pająk** 54:23 Yeah, it was about the translations.
**Tyler Yahn** 54:26 Yeah, I mean, I.
**Robert Pająk** 54:27 We can put it as low.
**Tyler Yahn** 54:29 Okay.
I don't know. It sounds like David's working on it. So maybe just put this also in the next milestone.
**Robert Pająk** 54:38 For tracking. Yeah, it makes sense.
**Tyler Yahn** 54:41 Okay? And we can just take it out as well. So okay.
**Robert Pająk** 54:43 Maybe the last one, because we are.
**Tyler Yahn** 54:46 Coming up on time. Yeah. Mutex contention at metric sums, high mutex contention matrix sums.
Yeah.
I don't think you're going to be able to get away with this just because this is the nature of how this is going to work.
but I think it for triaging purposes. We could probably put low. Given, it is not a correctness issue. So yeah.
let's let's do that.
**Robert Pająk** 55:19 Should it be, should be changed from a bug.
**Tyler Yahn** 55:23 Yeah, I think it's questionable. It's a back or is an enhancement.
I don't. That's actually a good. That's a good point.
see if I can open that again.
**Robert Pająk** 55:33 It's not incorrect behavior, right?
**Tyler Yahn** 55:36 No? Correct. Yeah.
Yeah. Good point. Yeah. Maybe it's not enough.
The bugs.
Okay.
**Robert Pająk** 55:49 Maybe let's put it at label to the metrics and SDK.
**Tyler Yahn** 55:55 Yep.
**Robert Pająk** 55:56 And I think that's it for today.
**Tyler Yahn** 55:59 Sounds good.
Anything else on the agenda. Nope, all right.
Stop sharing my screen any other topics you all want to talk about.
Of
one thing I did find out yesterday. For people on the call as well as the ones reading the Transcript later is that there is the Maintainer Summit is still accepting Cfps till I think Sunday. I think it's the 20.th So yeah, if you have, like. Maintainer related talks.
we could do that. I was also looking like there is a way that you can do like a project meeting thing. I was. I submitted one for the Ebpf instrumentation.
I didn't know if we want to submit one here, because there's I don't know how much of us are going to actually be there, so I think if there is a desire, I don't know. What do you think like?
You know how much, how many people are going to be at the Maintainer Summit from the Go Sig.
**Robert Pająk** 57:00 Like for us, too. I think the chances are pretty low for me. The only chance is, I guess, if I get my other talk approved.
Unless I have one. I have one idea for the Maintainer Summit a proposal, so maybe if it catches I'll be there.
**Tyler Yahn** 57:18 Yeah, the problem. I mean, I don't know what the policy is. I think you get a ticket to the Maintainer Summit.
I don't know if you get a ticket to Kubecon if you get that accepted. But I still think you should do that.
But yeah, I mean.
**Robert Pająk** 57:34 I get it.
but I think that I could have a chance to get a ticket from from Spark. That's a good point.
**Tyler Yahn** 57:47 So yeah, if if you want, I'd I'd say, submit something to the Maintainer Summit as well. If you have something obviously like, I think that one's a little bit easier to get into as well. It's like more ditch for people on this call.
**Robert Pająk** 57:58 Yeah.
**Tyler Yahn** 57:59 So yeah, but yeah, cool. Let's let's keep an eye on that.
All right, I think with that, then we can end it here. Thanks everyone for joining. I'll see you all in a week's time. Bye.
**Yevhenii Solomchenko** 58:12 Bye.
