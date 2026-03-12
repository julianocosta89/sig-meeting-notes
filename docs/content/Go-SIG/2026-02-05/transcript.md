SIG: Go SIG
Date: 2026-02-05
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/4PnNapaSe3eM6zUqC6Bb8B5zWXj4p8DD_TpP6s33D2HGsEJdiJNQCttIoj_moUZZ.gTa4hmk2AhSvAHdL
============================================================

## Zoom Recording Transcript

**Tyler** 02:14 Hey, Damien.
**Damien Mathieu** 02:19 Hey!
**Tyler** 02:20 How's it going?
**Damien Mathieu** 02:22 Good, how are you?
**Tyler** 02:23 Good.
How was, Fostim and, the hotel day?
**Damien Mathieu** 02:28 Good, busy, I guess. Lots of things. Not so much, like, Go SDK, more corrector.
And stability and stuff.
**Tyler** 02:42 Oh, okay, I gotcha.
So, like, yeah, I think I saw some, like, photos of, like, there was, like, a main stage or something like that, where people were…
**Damien Mathieu** 02:49 Yes, there was a main stage, but we did not use it that much.
**Tyler** 02:53 Oh, okay.
**Damien Mathieu** 02:54 It… based on the format of Inconference, basically we… Went. We spend the day in small rooms.
Like, chatting about the subjects that were produced.
**Tyler** 03:06 Oh, cool, okay, yeah, I gotcha.
Yeah, I was talking with the OV guys yesterday, and, like, they had a lot of really great conversation there for that.
**Damien Mathieu** 03:16 your mouth?
**Tyler** 03:17 Sorry, what?
**Damien Mathieu** 03:19 Kemara?
**Tyler** 03:21 Is that the name of a person?
**Damien Mathieu** 03:22 No, sorry, there's someone named… no, it's not OBI, it's from, Go Instrumentation.
**Tyler** 03:30 from the Go Auto Interpretation project.
**Damien Mathieu** 03:33 Yes.
**Tyler** 03:34 That would have been… oh, Eden or, Ron?
**Damien Mathieu** 03:37 No, no.
**Tyler** 03:37 Or…
**Damien Mathieu** 03:38 Kmart or Camel.
**Tyler** 03:40 Oh, Kamal? Oh, okay, yeah, yeah, yeah, Kamal. Yeah, he, Is that Datadog, right?
**Damien Mathieu** 03:47 Yes.
**Tyler** 03:47 And… yeah, I don't… I think he's definitely… I've seen him in meetings, for Obi as well, yeah. Sorry, yeah, it's coming together, I'm understanding what you're saying now.
**Damien Mathieu** 03:57 My brain was there, too.
**Tyler** 03:59 Oh, nice, yeah.
Yeah, that's cool.
**Damien Mathieu** 04:04 Yeah, I… I also was at Kamal's meeting, like, talk on Sunday?
And… yeah, I found it surprising. He was, like… it was, like, about auto-instrumentation in Go, But he was, like, very quickly saying that the Go SDK is very verbose and not a good thing to use, which I found a bit hypocritical.
**Tyler** 04:34 Well, I wouldn't use the Go SDK in the first place, but… I guess that maybe is just a slight at, yeah, anyways.
But yeah, I… I… I would use the API, is what I'm saying, but yeah, I…
**Damien Mathieu** 04:50 Yeah, no, what I meant is compared to eBPF.
**Tyler** 04:54 I… I gotcha. I'm… I'm just joking, because… Usually, a lot of the time, that evaluation is done without a complete understanding, I think, of the use space, but… Yeah, I mean, I don't know, like, it's one of those things where, like.
Yeah, some… some people take a, like, a stance on that, like, there's a… there's, like, a zero-sum game, but I, like… Don't think that's a valid argument.
Like, I… I see a world where, like, they both exist. In fact, like, in the Obi project, we specifically are trying to, like… we already… we already support that, right? Where, like, you can start using the API to supplement OB, we were trying to actually have it so that Obi can help provide additional spans that say, like, the API or the SDK aren't including, and it can detect that, like, there's a lot of really, like, metadata information, if we could pass that along, like… I think there's a lot of really great interaction that you can have between, the OpenTelemetry, like, APIs and SDKs and, like, automatic interpretation, and we're definitely exploring that, so… I don't know, like, I get, like, if you're gonna go, like, tell customers, and you're trying to sell a product, and you're trying to say, like, your product that is based on EVPF is superior to them writing their own thing, like.
Yeah, okay, I see why they would make that argument.
**Damien Mathieu** 06:12 Yes, but I find that, like, the context was not them going to customers, it was them going to the Golang dev room in FostDam.
**Tyler** 06:26 I think maybe you should remind them sometimes, but I… I don't know, like, I… I can't fault somebody, like, I get it, like, you just get into that mode of, like, that's the way you see the world. I… I just… I don't know, I'm not as pessimistic about the whole thing. I think that there's, like, room for both. In fact, I think there's, like, a need for both.
**Damien Mathieu** 06:43 I agree, there's a room and a need for both, definitely.
**Tyler** 06:46 Yeah, yeah. So…
**Damien Mathieu** 06:49 I wouldn't use it, at least, unless it's, like, I wouldn't use eBPF, unless it's a, like, like, long-running project that has been around for a long time, and where having manual observability is very tricky, and maybe we don't use context as it's supposed to be used, but in any new project, I would rather prefer manual instrumentation over eBPF.
**Tyler** 07:14 Yeah, I think it's also one of those ones where, like, like, my time's really valuable, so, like, I'm really excited to just go, like.
turn on Obi and be like, hey, does this solve my problem? And then, when it doesn't, it takes, you know, 10 minutes, and I go, like.
nope, like, let's go add some spans, like, let's go do this other thing, like, let's go, you know, or maybe I'm like, yeah, this is great, and then I just move on, you know? Like, sometimes I think that, like, it gets lost in the weeds of, like.
Having the perfect solution, and so, But yeah, I mean, I think that that's, like, I think great… feedback, yeah, I think Kamal was also… had a lot of really great EVPF, like, suggestions as well for, like, what could be done there, integration.
We've also talked, like, in the past about, like, integrating the, the injector, right? Because, like, that's also a really cool piece of… code that helps with auto-instrumentation and, like, setting things up, and, like, if you could couple that with Obi in some, like, discovery pipeline, in some, like, packaged, like, distribution, like.
I think there's a lot of really cool value that we could do there, and so, like, that's another thing that's being explored now. I think it sounds like there's some sort of, like, packaging SIG that's gonna get started up, So, yeah, that sounded really cool.
But, yeah, there's all kinds of EBPF stuff.
That I've heard. It wasn't there, but yeah.
Brian, you were there. Any other cool takeaways?
**Bryan Boreham** 08:41 From the thing on Monday?
**Tyler** 08:44 Yeah, or… and anything, possum as well, yeah.
**Bryan Boreham** 08:48 Well, yeah, there was no, in, monitoring dev room at Fosden, for… For a change.
So that… that was kind of weird. I mean, people… People did things like showed up at the databases track. Say, I have a database that stores logs and metrics.
But yeah, I… I… I don't… yeah, Fosden was Fosden. I mean, it's… it is… it's a… it's a thing to behold.
So the thing on Monday was much, much smaller, like.
I think we had 100… 120 people, something like that.
No.
**Damien Mathieu** 09:31 I would say under 100.
**Bryan Boreham** 09:34 Really? Okay.
**Damien Mathieu** 09:34 My guess was, like, just under 100.
**Tyler** 09:37 I've heard from organizers it was 100, but yeah, like, so I think you guys are in the ballpark, yeah.
**Bryan Boreham** 09:44 So it was really nice to get, you know, relatively small gathering, and see a bunch of people, see some of them in the face, in the flesh, for the first time. I'm not really answering your question, am I?
I guess I sat in on some discussions that because I kind of deliberately went to things that were kind of new to me.
**Damien Mathieu** 10:11 Like, the concrete discussion, where you left because you… Where can they flust, I guess?
**Bryan Boreham** 10:20 The, let me try and remember that. The contrib trip discussion…
**Damien Mathieu** 10:27 Yes, we had, that session on country, where it was mostly collector.
**Bryan Boreham** 10:34 Yeah, I… I left when it was nearly finished. I wasn't, it wasn't like a… value judgment.
the, yeah, well, I guess that one was kind of frustrating, because… It was… it was like an hour long, people bringing up bits of other discussions that they were in, and I wasn't…
**Damien Mathieu** 11:01 It was supposed to be Contrib as a whole, and there were a lot of collector-Contrib folks, and like, Contrib in SDKs have very, very different needs and problems than Contrib in Collector.
And so, yeah, the discussions and asks were very different between JS and Connector.
**Bryan Boreham** 11:26 Yeah… I honestly, I'm struggling to remember, exactly what happened, but I do remember it positively, just kind of getting the people together and, we did… we had, I think two sessions about… Prometheus Metrics SDK versus OTEL Metrics SDK.
I don't… I shouldn't have used the word verses.
You know what I mean? Friends forever.
Which… I wasn't in the first one, but I think it was kind of… high level, and then I was in the second one, and we… We tried to kind of thrash out I think, yeah, we're sort of starting up a working group there, I think, to…
**Damien Mathieu** 12:32 Do you mean the one with Richie?
**Bryan Boreham** 12:34 Yeah.
**Damien Mathieu** 12:35 Yeah.
The ID, it's Collector again, but the ID is… Prometheus has a lot of receivers for data, and, right now, Collector Contributes doing lots of re-implementations of everything that Prometheus is already doing.
And so the question was, would it be alright if those were just, like, the Prometheus receivers having the proper interfaces to be collector components.
So in the idea, there's no problem to that. There is a bigger problem with, like, collector distributions.
If, we start having lots of receivers that are coming from different repositories, But it's something that's resolvable.
there was a need for more discussions, and we left basically saying that we should meet during QCon.
**Bryan Boreham** 13:33 Yeah, anyway, I think it's always positive to get people together, and it was… I think it was a pretty… Pleasant.
Environment and meeting, and so on.
**Tyler** 13:46 Well, cool. Yeah, sounds great. Yeah, I'm excited to… Keep going with the KubeCon coming up as well.
**Damien Mathieu** 13:53 Would you be actually…
**Tyler** 13:54 jump in here.
**Damien Mathieu** 13:55 Would it be a cucumber end?
**Bryan Boreham** 13:58 Yes, I will be at KubeCon and at the Maineer Summit.
**Damien Mathieu** 14:02 Taito 2.
**Tyler** 14:04 Yeah, I don't know about the Maintainer Summit yet, but, I'm planning on being at KubeCon. I think I'm getting approval just today-ish, maybe?
**Damien Mathieu** 14:13 So… And Sam, Sam, you won't be.
**Sam Xie** 14:18 I will try, I don't know.
**Damien Mathieu** 14:26 I'm not asking still now, but, maybe you would be, I don't know.
**Sonal Gaud** 14:32 nose.
**Tyler** 14:35 So, Nali, you're based in India?
**Sonal Gaud** 14:38 Yeah, I'm from Mumbai.
A bomb day lately.
**Tyler** 14:43 There's the KubeCon India one coming up too, right? Yes, it's… yeah, it's going to be in Mumbai only.
That's right, yeah, yeah. Are you gonna be at that one?
**Sonal Gaud** 14:52 Yeah, of course, it's going to be in June, so yeah, if you guys are coming, then it's do this.
**Tyler** 14:57 I think there's a chance that, there's a chance I might be, it's slim right now, but then Robert, I think there's a chance he's gonna actually be, so… Yeah, there's definitely some GO folks that are gonna be there, so yeah, worth, worth, worth… oh, well, that's also tentative, I think, so I don't know if I want to speak too much, but…
**Sonal Gaud** 15:14 That's great, would love to meet you on… meet you guys.
Yeah, yeah, that'd be cool.
**Tyler** 15:20 I did want to jump in here.
**Sonal Gaud** 15:23 based on…
**Tyler** 15:24 Sanal being in India, I'm sure it's 10PM. So if you haven't yet, go ahead and add your name to the attendees list. And if you have agenda items you want to talk about, we can go ahead and jump in here. Sanal, you did have the first one. This is, I think, is also something Damien's brought up. Go ahead, I'll let you jump in.
**Sonal Gaud** 15:42 So basically, in the open ECTP civilizations, you know, we were auditing. So there was one thing that came out that we will be deprecating the laborer In the favor of the width matrix attribute Fn, but Robot pointed out that it is not very reliable, because the function is, like, very… you know, not a fully replacement to what the Liberal does. So, I think the question came out, like, we have to think more about the API, so I wanted to ask the ideas and feedback, so what I should be, you know, doing, like, if you could put down how we should be, like, rethink the API.
Because that is, like, a core API design, so I would love to know your guys' feedback, you know, before working on it, so…
**Tyler** 16:29 Yeah, I mean, I think Robert's point is well made, that it is correct that, like, the labeler has more access, so I think that that's intentionally a good thing.
I mean, I don't know, I think that, like.
obviously, like, it depends on, I think, Sunal, like, what your comfort level here is, but, like, if you wanted to go through and, you know.
come up with some sort of brainstorming ideas of what you think should be done here. I mean, I definitely think that one of the options here is to leave it as it is. I think that's fair. I think another option is to switch, like is presented here. I think another option is renaming, things. That may be helpful. Another option may be, investigating if there's, like, something that's specific for the labeler that could also be applied across other signals, like, if it's specifically a labeler access thing with, The handler scope, like, maybe that's relevant for tracing and for, for, met… or logs as well.
So, I think I would probably suggest looking at all of these, because, like, you know, if it's the latter, and it's relevant to all of them.
Maybe the widthmetrics attribute function could be updated for all of these signals, to support the access that's here. If it's something specific to metrics.
I'm sorry, I don't know the exact context, if that's the case, I can't answer that off question, hand, maybe Damian can. But, like, then I would… I would say that maybe metrics needs to be a different thing at that point, and so…
**Damien Mathieu** 17:58 Evaluating those other proposals would be helpful. We never introduced with span attributes functions, because you can add, span attributes in any middleware, and so the recommended behavior has always been to just add a middleware that retrieves the current span, and then add attributes to it.
Whereas you cannot do that with matrix, hence the existence of that function.
So, it doesn't make sense to add that function to every signal. It's really matrix.
**Tyler** 18:33 Okay, yeah, alright.
And then, so then, Damien, what is your recommendation here?
**Damien Mathieu** 18:39 I… I'm not sure what we're losing by removing Labrador.
I need to dig into that.
**Tyler** 18:49 Yeah, I mean, I… the… the… I'm kind of remembering what happened, and based on what Robert's saying here, like, I'm guessing what he's saying is that, like, if you wanted trace context in your attributes that you're providing here, you wouldn't have that if, if you didn't have this labeler.
**Damien Mathieu** 19:05 And so, okay, so you would need a context. What if we added a context with metric attributes different?
**Tyler** 19:11 Yeah, I mean, I think that that's… that seems reasonable to me.
**Damien Mathieu** 19:14 That's a breaking change, so we should do that, sparingly, but yeah.
**Tyler** 19:20 Yeah, yeah, it is.
**Damien Mathieu** 19:22 If we do that, I think we should… what I mean is, we should add the context to withMatrix attributes function, and then, in a later release duplicate labeler.
**Tyler** 19:35 I think that seems reasonable to me, yeah.
**Damien Mathieu** 19:40 Does that make sense as a, next step, Sunil?
**Sonal Gaud** 19:47 Yeah, I'm talking about this morning.
**Tyler** 19:49 Can you comment the plan in the… the… Is there an issue for this?
Yeah, okay. So maybe comment what the decision is here, maybe, like, the discussion as well around, like, the idea around where… why we don't want to do certain things, why we want to do other things, so that it can be full context, and then just point Robert to it. He's out this week, but he will be back next week, so I, like, I think… getting his buy-in on this one would be helpful, as he's had some thought on it. So yeah, I think that'd be… that'd be great. I don't know timeline-wise, if you're trying to get this done this week, but if you can wait till next week, that'd be great.
Okay.
Well, cool. Alright, yeah, that sounds good to me.
Let's go in that direction.
Cool, alright, that's the end of the agenda, I can… Stop sharing here.
And we can… oh, look.
keep talking, any other topics of discussion, or things people wanted to talk about here? Oh, Brian, I did see your PR around the string, method being added to the, the value and… key value? I can't remember.
It looks good, I'm super excited about that. One thing that I did notice is, You were pointing out a lot of, like, weirdness with what's being emitted from the string function.
I would suggest, like.
fixing it to be whatever you think is appropriate. Like, this is actually, I think, why we didn't have a string function before, is because of the format of the string itself. The emit function is, like.
Rough. I'm not exact… like, the attributes package is… To be fair, a collection of things that have accumulated at the very earliest start of the project with anticipation of what things could have happened, and it's built long before its actual use, so… if you see things that don't make sense, it's probably because they don't make sense. Like, it's not because it's intentional sometimes, most of the time. So, if you see things, like, that are being weirdly… like, if you're trying to shoehorn the emit function to get the values to work, I would say maybe just look at… writing its own, like, string formatter in the string function. Like, that seems completely fair to me.
you've already made it clear in that PR, that that format is not stable, so if we needed to change things, we could, but I think that, like, doing something as idiomatic as you can make it, I think, is ideal.
I would prefer that. I would definitely prefer that than trying to conform to some, like, arbitrary, like, I don't know, marshalling thing that's going on there. So yeah, I would say move in that direction is the only thing I was looking at earlier. I was gonna say that I just got pulled off to another PR. I don't know if that helps.
**Bryan Boreham** 22:46 Yeah, I mean, it's… Right now, it's… I think, consistent with what was put in the log, value…
**Tyler** 23:00 Okay. Yeah, that's probably a good idea, like…
**Bryan Boreham** 23:03 And log key value…
**Tyler** 23:06 Note that the log attribute stuff is gonna go away.
So what you're doing will become, like, the standard, so if you wanted to copy what's doing in the logs, that's fine too, but, Yeah, I… Just a heads up on that one.
**Bryan Boreham** 23:23 Okay, well, I… And… and there was a suggestion to Mark emit as deprecated, and I… I guess I took that to mean in the go sense, i.e, that you'll start getting a warning.
**Tyler** 23:44 Yeah, I took the same sense as well. I don't know if I would go that far as well. I think I saw your comment saying that, like, maybe that's a separate PR, or maybe that's, like, not something we want to do, and I kind of agree with you. I think that we can update the documentation on Amit and saying that, like.
You probably want to use string instead, but I don't know if going as far as to saying that, like, deprecating it is really worth doing.
**Bryan Boreham** 24:09 Okay.
**Tyler** 24:09 I don't know why it exists, but I also don't know why we would tell people to not use it. Is kind of my stance on that.
**Bryan Boreham** 24:16 Yeah, and yeah, I mean, it's just something I sort of blundered into while trying to do something else, so I…
**Tyler** 24:24 You're not alone. Like, every time that we look at tests, and, like, they're super opaque, and you're trying to go through key values, and you're like, I don't even… I can't even figure out what this thing is right now, it's… Yeah, it's just something we've put up with for years, so, yeah.
Okay. So yeah, that's… I'm definitely excited about what you're doing. I think it will help with the clarity that we're seeing in telemetry when it's ported to the console, let alone other places, yeah.
**Bryan Boreham** 24:48 Okay, well, I might take another pass, So… I think there's… there's two big inconsistencies, or… one is… is that Booleans… bull slices don't have commas between them. I think that's a relatively easy sell. Like, everything that's a slice should be comma separated. And then the other one is, should strings be quoted?
And… I…
**Tyler** 25:17 I prefer it that way.
**Bryan Boreham** 25:19 I, I, I think it's…
**Tyler** 25:21 Yeah.
**Bryan Boreham** 25:21 It's kind of… it's an easy sell if… the string has spaces in it, or something like that. Kind of seems natural to quote it. If it doesn't have any spaces in it, it doesn't need quotes, but… Yeah, so that, And then sometimes these whole things get put in places where the whole string is quoted, and you end up with lots of backslash quotes. That would maybe be an argument not to do that, but I certainly could… Just quart strings, and .
**Tyler** 25:58 Yeah, another thing is… there was recently a PR on, like, how we want to, I think there was a PR at the specification level on how we want to, like, represent, attributes in, in, like.
complex attributes in things that are not, like, supporting complex attributes, so this is, like, maps and other… other types. We don't have these yet. But the answer was that we wanted JSON-fi, like, these things, and… and so, like, I think what you're describing is doing the JSON-fying anyways right now, so if that was the case, like, when we go to trying to… Yeah, pseudo, right? Like, but, like… Yeah, I mean, I guess definitely pseudo, we don't…
**Bryan Boreham** 26:38 I'll eventually.
**Tyler** 26:38 Keep in mind, we are going to have, like, a null type, right? Because an empty type is gonna get introduced, and, like, a map is going to get introduced, and so, it's worth thinking about, maybe.
If we wanted to… write something consistent. Like, obviously, like you said, it's not stable, it can change. But if we wanted to try to, like.
anticipate we're gonna be doing something like that? Maybe, you know, thinking about it now.
**Bryan Boreham** 27:03 Sure. I mean, if, if… If Jason is… really gonna be what people want, then we could just do that.
I mean, there are kind of problems the other way with Jason, like, Very large floats are not representable in…
**Tyler** 27:26 Yeah, and that was… that was recognized as well. And, like, the loss of precision, or the loss of type as well, is… it's… it's a lossy encoding, right? Like, there's definitely a.
**Bryan Boreham** 27:35 Yeah, so this is supposed to be for debugging, it's not supposed to be for… encode, decode.
Sorry, Core… That's exactly what I thought.
Making it noticeably not Jason.
we… we… yeah. I think if…
**Tyler** 27:52 Sounds good to me, too.
**Bryan Boreham** 27:54 Sorry?
**Tyler** 27:55 That sounds good to me, too.
**Bryan Boreham** 27:56 Yeah, if you want Jason, it's not that hard to get Jason Today.
**Tyler** 28:00 Yeah.
**Bryan Boreham** 28:00 So I, I, I think I would probably… yeah, not make the string method produce JSON. But, you know, it's not something I feel hugely strongly about.
**Tyler** 28:14 This is what we did also for the standard exporter, right? Like, we, like, explicitly didn't make it JSON by default, because we don't want people to rely on it as, like, a communication protocol, and it needs to be something that, like, we're not… we don't want you to assume that this is, like, serializable in any way. And so, like, yeah, that, I think, is fair enough as well for these attribute strings, like… you know, if we're telling people, don't count on this to be some sort of encodable or decodable format, like, don't make it one, right? Yeah.
That seems reasonable, okay.
**Bryan Boreham** 28:46 Thanks, Philip.
**Tyler** 28:48 Yeah.
Well, cool, any other topics people want to talk about? Otherwise, we can probably end the meeting early here.
**Sonal Gaud** 29:00 Well, I have ordered, so I'll be speaking with Rafna and friends.
Tomorrow, and it is going to be open telemetry, how open instruments, can go. So, anyone who has… like, it's going to be my first class, so anyone who I've spoken before has to give me any suggestions, or I would love to…
**Tyler** 29:24 Sorry, I was having trouble understanding you. Sounds like you're giving a talk tomorrow?
**Sonal Gaud** 29:29 Yeah, I'm giving a talk in GraphNs, and it is going to be about open telemetry, how it instruments, the data and go. So, any suggestions, like… Because it's gonna be my first talk, so yeah, Fight knows.
**Tyler** 29:44 Yeah, I mean… I think that's great. Definitely, I would suggest sharing your talk on the Goach Hotel Goach Slack channel afterwards. I think we'd all appreciate seeing something like that and sharing in the community. That's great. I'm excited to hear that you're giving a talk.
Yeah, I mean, yeah, there's a lot of really… great things to talk about there, so I… if you're looking for content stuff, like, I'm sure we could… we could discuss that as well in the Slack channel, but I'm guessing you've probably given the talk tomorrow or you have content nailed down.
But yeah, I mean, I… I think… Feel free to, I think, speak as a contributor to the project, so yeah, I think that's what I would say, yeah.
**Sonal Gaud** 30:28 No one would like to add anything?
I mean, it's like our first time talk, like, you guys have given the talk, so, you know, you feel into your nose, so anything like that.
**Bryan Boreham** 30:38 My… so, sorry, it is quite difficult to hear you, but I think you're saying… you're asking us if we have tips for you giving a talk, and it's your first time giving a talk?
Did I hear that? Okay. So, yes, I think, Learn your first line, and your last line.
That's my… that's my number one tip. So if you… if you know, because it's very… Scary, sometimes you stand up there as a bunch of people, so if you… if you know your first line, like, absolutely cold.
it's much easier to kind of keep going, right? First line came out, okay, now second line, third line, fourth line.
And… and the thing about knowing the last line, it's just… it's just nice to have a good ending, you know, you sort of… you end your talk, and everyone claps, and, so you kind of know where you're going. And… yeah, I, slow down.
There's a very great tendency to talk really, really quickly, and… and, You tend… just everyone tends to, in a public speaking situation, talk much faster than they need to.
And much faster than people can hear them.
So, so consciously slow down, have some water with you. There's a stress response in the body that your mouth can go very, very dry.
And that also gives you a moment to pause.
You know, pausing is good, slow down, pausing is good.
That's about it, really. I mean, you know, you're… you're only there as the expert, right? You're being invited to give a talk, so don't worry about what you know or don't know, or who these people are, or anything else. You're the person, you're up front.
Give the talk, enjoy yourself.
**Damien Mathieu** 32:36 I would add, be yourself. It can be tempting to try to, like, imitate folks that you have seen doing talks, and be funny on it, on stage, and be, like, very, like.
Yeah, outside… showing on ScanCase, and just, like, don't try to imitate them. Just be yourself, and give the content you want to give in the way you want to give it.
**Sonal Gaud** 33:03 Thank you so much, everyone. I really appreciate it.
**Tyler** 33:09 Yeah, absolutely. Good luck, and like I said, let us know how it goes.
**Sonal Gaud** 33:13 So, thank you.
**Tyler** 33:15 Yep.
Okay, everyone, weekend meeting here. Thanks for joining. We'll see you all next week, or maybe the week after. Yeah. Bye, everyone.
**Sonal Gaud** 33:25 Never mistake.
