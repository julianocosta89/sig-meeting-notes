SIG: RPC Sem Conv Stability SIG
Date: 2026-07-09
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao** 01:54 Hello? Sasko?
**Trask** 02:03 Hey, Steve. Hey, Matt.
**Matthew Hensley / Grafana Labs** 02:07 Hello.
**Madhav** 02:15 Hey, Trask.
**Trask** 02:17 Hey, Meta.
I am just making coffee, haven't quite made it to my desk yet, but on my phone here.
**Liudmila Molkova** 02:42 Hello, hi.
**Madhav** 02:42 But it's.
**Trask** 02:45 Good morning, Lyudmila.
**Liudmila Molkova** 02:49 Good morning.
**Trask** 02:55 I haven't quite made it to my desk, if you can… if you're able to… Drive.
**Liudmila Molkova** 03:04 Yeah, I didn't wake up, but I made it to my desk.
**Madhav** 03:08 But…
**Liudmila Molkova** 03:11 Okay.
see.
Okay, today.
It is.
Remember we talked about, all the different, parts of the feedback, Madhav. I I don't I didn't see an issue.
Yeah.
**Madhav** 03:37 I have started logging the issues, so I have… what I've done is for each, Each of the problems have logged a separate issue.
So that, you know, those do not… like, one issue doesn't… block the others, like, if we can proceed with one, we have alignment, we can close that, and, you know, I've just segregated all of them. I'm yet to log two more issues. Do you want me to ping the list of issues in the Slack channel?
**Liudmila Molkova** 04:06 We'll find them, sorry, I don't know how I missed them.
**Madhav** 04:11 No, no, I just filed it, like, 10.
**Liudmila Molkova** 04:13 Oh, I see, okay.
**Madhav** 04:14 These are the ones, yeah, from 68 to 73.
**Liudmila Molkova** 04:19 Yes.
Do you want to talk about them, or do you have any specific things?
**Madhav** 04:24 I think we had already spoken about all of them, the only one that we don't have an alignment on is the RPC method original.
So… The… leads in gRPC want to actually understand why can't we have separate values for RPC method in, In metric versus in spans.
**Liudmila Molkova** 04:51 So for unknown methods, that we don't recognize, we would require the method on spans.
And made it, and a capped version of it.
on metrics.
**Madhav** 05:08 Yes, so if we already have RPC method.
label, we can just populate other for unknown methods in case of metrics. And in case of span, we can populate the actual value, right?
**Liudmila Molkova** 05:22 Yeah, so for… That's the one of the principles we have that we want attributes to be the same.
Right? So if you query expanded metrics, you would query them.
In the same way and expect the same things.
But more probably more importantly, if you want a practical reason. So RPC method is part of, span name.
And span name has low cardinality.
And we're… actually want Span method.
Sorry, span name to… part of the span name to match the attribute so you can query it properly.
If you only care about the the cap one.
**Madhav** 06:14 RPC method is part of the span name, but currently, span names are already populated with the actual method name. We are not keeping it capped.
**Liudmila Molkova** 06:25 Well, you, you aren't, but, but we, we would recommend you too, because, people.
**Madhav** 06:30 It's not recommended in this as well, like, I was going through this, I did not.
**Liudmila Molkova** 06:35 So it is RPC method and RPC method is capital.
**Madhav** 06:42 Okay, understood.
Yeah, maybe you can just respond on the ticket with the details, so it'll be easy for me to… Take it to the leads, and then… having…
**Liudmila Molkova** 06:56 Okay.
**Madhav** 06:56 Have a discussion if… if they… Align.
If they're okay to have RPC method original.
**Liudmila Molkova** 07:03 Sure.
**Madhav** 07:05 Yep.
And that was… I think I filed almost all of them. The other one was just about the error type.
Oh.
Which I think would be, again, misalignment. So, error types, I understand that Based on how HTTP is working, there are some things which are error for servers.
Which are not errors for server, which are okay behavior. But, that's not how gRPC is designed. There is no way for us to know.
If a certain error code is appropriately assigned to.
the RPC. So, we treat everything which is non-OK as error.
I have not yet filed an issue for that. I was busy.
**Liudmila Molkova** 07:59 Oh, okay.
**Madhav** 08:00 Yeah, exactly. Yeah.
If you want… I'll just quickly…
**Liudmila Molkova** 08:06 Help me understand, so… Yeah, it's… The concern is that you.
Don't.
Like, the way our type is designed, you'd rather not populate it, or…
**Madhav** 08:22 Yeah, the error type, there are certain error codes that you have mentioned, which mean That on server side, they will not be considered as errors. They will only be considered errors on client side.
**Liudmila Molkova** 08:36 Okay, like not found.
**Madhav** 08:40 Like, not found, yes.
**Liudmila Molkova** 08:42 And This is a problem… why?
**Madhav** 08:47 Not found? So, in general, gRPC doesn't really know not found is generated.
Because of a client's mistake, or is it because of… A bug on the server? We don't really know. It's not… Traditionally, you wouldn't map it to a 5xx error in HTTP, which is where this is coming from, and I understand that. But in gRPC, the premise is not at all that. The premise is… Either the RPC is okay.
or there is an issue with the RPC and we are not able to return.
A success status, and we are returning the closest, error, whatever would… I mean, sometimes the server might be responsible for not found as well, right?
**Liudmila Molkova** 09:37 Yeah, and it's it's not designed to be like 100%.
Bulletproof because.
404 is one of those things that you never know.
If it.
**Madhav** 09:50 Yeah, 404, so in HTTP case, at least 404 is quite, Well understood and determined that it's a 404, which means… it's a… it maps to not found, and it's a client error in most cases, but for us, it's not even 404. A not found is just a not found that someone has said to be not found.
It… server, or client, or whatever.
So, that's why… It will create confusion, because currently, all the existing users that are using gRPC metrics would I already assume that everything that is not okay is an error. And then, once we start segregating this based on HTTP or some other RBC system, it will… it basically will not apply to GRPC.
**Liudmila Molkova** 10:50 Okay, so I think we can take… Different paths here, and we can keep discussing it.
So I'm trying to find… do we have GRPC status codes somewhere?
**Trask** 11:08 That one you said you hadn't opened an issue for yet, Madaf?
**Madhav** 11:12 I am just doing it, give me, like, 10 seconds.
Yep.
I have just done it, it is 3874. You should have it on your board.
**Liudmila Molkova** 11:33 The caller is definitely cancelled by the caller.
And.
**Madhav** 11:41 Okay.
Not definitely. Typically is okay, not definitely.
**Liudmila Molkova** 11:49 Yes, and this is the criteria, right? Typically, typically, it's not an error.
Sometimes it is, but…
**Madhav** 11:59 No, no, no, typically… no, no, what I mean to say is, typically, it would be canceled by the error, by the caller, but… The… in all scenarios, it's an error for the RPC, right? The RPC failed halfway, or got canceled halfway, like… I understand what you're saying, and I do understand your perspective, it's just that these are very… specific nuances, then we'll have to start listing it down specifically for gRPC, that This is what we are trying to mean.
And this is what we are not trying to mean.
The existing gRPC documentation just says everything that is not okay is error.
And now then, we'll start deviating from that.
**Liudmila Molkova** 12:44 Okay, so there is this. Okay.
**Madhav** 12:47 Yep.
**Liudmila Molkova** 12:48 At.
The one thing I feel.
Strong about this that.
The error type should be there.
Otherwise, on spans and metrics.
**Madhav** 13:02 No, error type should be there, we are not deb.
**Liudmila Molkova** 13:04 Okay.
**Madhav** 13:05 Yeah, I am okay with error type being there, but what I want to say is everything that is not okay will be an error for GRTC.
**Liudmila Molkova** 13:13 Okay.
**Madhav** 13:13 I don't want to have categories of error codes, which would mean something else in… some scenarios and something else in some scenarios. We categorically state that everything that is not okay is an error.
**Liudmila Molkova** 13:26 Okay.
No.
I might have.
**Trask** 13:32 Yes.
I… So you haven't gotten… I know on the HTTP side, and I agree that there's differences between HTTP and RPC, or gRPC.
In this area. But I know like in ACVP, we have gotten a lot of feedback from users over time that these 404s and client errors shouldn't show up.
on server… As server… server errors.
So my question is, have you gotten… it's good feedback to know whether you've gotten any Complaints from users about these… Client side errors…
**Madhav** 14:31 No, no.
**Trask** 14:32 Sure.
**Madhav** 14:32 In the one… in the one year that I have been on the GRPC team, I have never seen an issue that says that, but I have just been one year in the team. I can go back and ask for people who are Elder in the team.
**Trask** 14:50 Cool. And then, how long has that behavior been in gRPC?
Is that, ever, okay.
**Madhav** 14:58 Ever since the…
**Trask** 15:00 Open census, even.
**Madhav** 15:02 Yeah, that's Probably, but I don't want to… quote you… quote me… I don't want you to quote me on that, I'll just go back and check the specifics, but…
**Trask** 15:13 Yeah.
**Madhav** 15:13 That's.
**Trask** 15:14 Okay.
**Madhav** 15:14 This.
**Trask** 15:16 Yeah, I think…
**Madhav** 15:16 Do that for a long time.
**Trask** 15:18 Yeah, that would be useful feedback for us.
kind of prior prior art.
**Madhav** 15:26 Right. I'll find out the details on how long this has been like this, and if we have had any feedback in any of the other GRPC implementations. So, I specifically look at Go, but I'll speak to other folks who look at Java, C++, web, everything, and then try to see if there are any such specific feedbacks about error codes.
**Trask** 15:50 Great, because I feel like this one is the most… the stickiest of the issues that you've raised so far.
**Madhav** 16:01 Yeah. So, I want to explain it to you this way, Trask. In today's world, let's say there is a 404 because the URL is incorrect.
You would get a 404, or you would get something like… you'll map it to… You are thinking that we'll map it to not found. We are not actually going to map it to not found. An HTTP error is translated very differently in… gRPC. Like, in different cases, things will map differently in gRPC. We first take priority of the gRPC status code, and if it is not there.
Then, based on a lot of conditions, we'll map some error codes to some specific gRPC status codes, and there is a bit of logic behind that. I can go back, dig it up, and send it to you, so that you are able to look at it and make sense of what I'm trying to say, but I'll also get more context of the questions that you're asking.
**Trask** 16:57 Cool, thanks. Yeah, I mean, I… that will help. I do more or less understand where you're coming from on that. It's just that we're it would help us if we're going. It will be painful for us to not have the same rule applied to both RPC and HTTP.
So we need some pretty, kind of, strong, Reasoning, if we're going to make that deviation.
**Madhav** 17:37 Understood. Yeah, I will find more, supportive documentation and get back to you.
**Trask** 17:43 Great, thanks.
**Liudmila Molkova** 17:45 Thank you.
**Madhav** 17:48 And I think there is one last issue that I still have to file. You remember about RPC request metadata and RPC response metadata?
I discussed with the leads what would be an appropriate name, and they have told me it should be RPC Request Header.
RPC response header, and RPC response trailers.
**Liudmila Molkova** 18:16 Yes, for GRPC.
Yes. No, for in general, right?
Because…
**Madhav** 18:24 Oh, yeah.
**Liudmila Molkova** 18:28 Yeah.
**Trask** 18:29 Do we have meta — is metadata under RPC today?
**Liudmila Molkova** 18:35 Yes, it's shared across everything.
And I think… maybe, Steve, do you remember by heart how metadata, if it's applicable to Dabo, and what is the, like, natural name for it?
the protocol.
**Steve Rao** 18:58 Cool.
**Liudmila Molkova** 18:59 Level.
**Steve Rao** 19:01 Yeah, in double. Let me find the documentation. Sorry.
I forget the specific name in double. Yeah, it's mapped to the metadata.
Okay.
**Liudmila Molkova** 19:23 Or maybe we have it documented.
RPC.
Oh, it.
**Trask** 19:30 But no luck.
**Liudmila Molkova** 19:31 Challenge it. Mhmm.
**Trask** 19:32 For HTTP, We could potentially have trailers, we just don't.
Right.
**Liudmila Molkova** 19:41 Right.
**Trask** 19:44 I mean, I'm not opposed to the term headers.
**Liudmila Molkova** 19:56 I'm not the post either, so your point is that metadata is ambiguous, because it's both.
Right.
**Madhav** 20:03 Yes.
**Liudmila Molkova** 20:04 Okay.
Okay, I see.
**Madhav** 20:07 Okay.
So, I will file… Yeah, I'll file an issue. That's the last one that I need to file. Everything else I've already filed.
And,
**Trask** 20:34 I was checking, Lyudmila, we don't have it on… it is in the RPC namespace.
But it is, like, It's not on the base span.
Base RPC span.
meaning to sort of opt in for Rpc. Frameworks that even have the concept.
**Liudmila Molkova** 20:58 Right. So, like, what you're saying is that imagine we put something new here. I don't know. JSON RPC grows, metadata.
Then, we would… If it's not comfortable with germs, headers, and trailers, it could potentially create something custom that would work for For it.
But.
It.
Well, it's… I'm fine with headers and trailers if it's the common terminology, but given that Connect RPC and Dabo are compatible with gRPC, The headers and trailers are effectively common terminology, I think.
**Trask** 21:49 Right, right.
**Liudmila Molkova** 21:54 Okay.
Yeah, so… I am okay with this.
**Madhav** 22:06 Okay, so other than the error type, the remaining two issues we discussed, we are okay. If you can go back to the dashboard and just glance through the other issues that I have filed, I think, in principle, we had already aligned on them, but I just want to confirm So that there are no surprises, given that we'll meet only after 2 weeks.
**Liudmila Molkova** 22:27 Cool. So let me actually open the map and make sure we And label, and add them to their PC, or they already are in their PC. Awesome.
**Madhav** 22:39 Yeah, yeah, I do.
**Liudmila Molkova** 22:41 Doesn't have enough details. Cool. Yes, absolutely.
I am going to… Market doesn't accept it.
to do.
**Steve Rao** 23:00 Hello, Damila. I sent a documentation in chat.
Yeah, this is, Description of metadata in double.
**Liudmila Molkova** 23:12 Mmhm.
**Steve Rao** 23:14 Yeah, I guess, okay.
Yeah, there you go.
**Liudmila Molkova** 23:21 Oh, they…
**Steve Rao** 23:22 tab called Attachment.
Attachment for user to send some metadata in double.
**Liudmila Molkova** 23:34 Do you have a distinction between, like, headers and trailers?
**Steve Rao** 23:47 No.
**Madhav** 23:50 Doesn't look like it.
**Liudmila Molkova** 24:39 Is it the Java concept?
You.
Okay, we we can investigate it further.
**Madhav** 25:35 Okay.
Emily.
Okay.
Can I move to the next issues? This will probably need a deep dive.
**Liudmila Molkova** 25:49 Yeah, okay.
**Steve Rao** 25:50 Yeah, I can do some investigation later.
**Liudmila Molkova** 25:54 Awesome. Thank you. Appreciate it.
Okay, the histogram buckets.
**Madhav** 26:20 Yes.
**Liudmila Molkova** 26:23 Okay, and you're saying… Oh.
So the current metrics have certain buckets.
And it would probably be absolutely uncontroversial for GRPC to document this as the Old.
There are a lot of them now.
I think it's twice as much as we have a much bigger resolution.
**Madhav** 26:50 Yes, because we work on much smaller margins than regular RPC, otherwise we would be, like, bucketing up most of the RPCs into one bucket, and it wouldn't make any sense to our users or that.
People don't listen.
**Liudmila Molkova** 27:05 Wait, this is for… The units are used.
So it's both for the call, and at…
**Madhav** 27:17 Yes.
**Liudmila Molkova** 27:19 Okay.
Do you use the same for streaming calls?
**Madhav** 27:28 Yes.
**Liudmila Molkova** 27:30 Okay.
So they are very focused on very fast, probably ordinary stuff.
**Madhav** 27:37 You know.
**Liudmila Molkova** 27:47 Yeah, I mean, this is something that's definitely.
it's even… I feel like even instrumentations should have a choice on what the… on.
default buckets are.
But assuming we have the same instrumentation, I have to ask, what do you think? Would you be comfortable having this as a default in Java gRPC instrumentation or in the shared one?
**Trask** 28:15 I would probably, first counterpropose, I support going, Lower, you know, creating these lower bu… creating lower buckets?
But we do have, sort of, general rule of… rules of thumb for histogram buckets.
and… So my counterproposal would be not quite as many buckets, but covering that same lower range. Basically, I think our kind of standard is we've documented as like the More or less having… Yet.
I'm.
But but we'll I'll definitely comment on the issue, and we can have that discussion. But totally At least, at minimum, very supportive of the… having the smaller the smaller buckets.
**Madhav** 29:25 So, I'm trying to understand, you're saying that about the instrumentations, or are you saying that gRPC should emit metrics in… The changed… Bucket boundaries.
**Trask** 29:45 I that's a good question. I mean, so that'll we would. I think my 1st proposal would be I mean, I'll figure out what it is, but it would be slightly different than this, but it would still cover those small values.
**Madhav** 30:04 But if we are going to, like, I want to understand this, if we are going to have a separate, list of bucket boundaries for gRPC, anyhow.
then… why not go with what gRPC already has?
**Trask** 30:18 I would propose it for RPC in general.
**Madhav** 30:23 Okay.
**Trask** 30:24 Because it's a RPC… Problem. I mean, But if then, you know, if you all come back and say, you know that that is a breaking change, or you know, let let's get to that point.
I I definitely understand your initial concern of it. The bucket sizes being not having not having smaller buckets.
**Madhav** 30:56 Okay, fair enough. I'll wait for your comment.
**Trask** 30:58 I mean, if there's more other details you can provide on the issue, then, you know, we can.
That, that would help.
**Madhav** 31:06 No, that's about it. I think we had, like, a healthy discussion before arriving to this bucket size, so that's why it's there, and it's documented. It's documented as one of the… proposals in gRPC long back when metrics were started.
Like, when metric emission was started, so all the metrics… for… Which are not just duration metrics, like, other metrics also which are not just call duration.
Follow the same bucket.
And now, if we'll change it, for us, it will apply to everything else as well.
So that it has a bigger connotation for us to not… it's not going to be changed just for one.
**Trask** 31:48 Sure. Yeah. And to Lyudmila's point, like the bucket boundaries are not a super important… part of semantic conventions, meaning like.
If… Jer, like, we could… I think we'll let's start by proposing smaller buckets across Rpc. But then we could still override the Grpc bucket boundaries.
Yeah, that makes sense.
**Madhav** 32:22 That makes sense. Okay, cool. Sounds good.
Yeah, because consumers…
**Trask** 32:27 Consumers aren't, you know, it shouldn't have a big effect on consumers like cross.
**Madhav** 32:36 Okay.
Understood.
**Trask** 32:38 Think, I don't know, Lyudmila, what like, can we… like, if we have… if somebody's reporting both GRPC… oh, sorry, we're over time.
Better.
**Madhav** 32:51 We just discussed this one, because this might be, like, I mean, I know we agreed, but let's… If it is okay for people for 5 minutes.
**Liudmila Molkova** 33:03 I personally, I would rather think about it and come back to it later. I don't have a strong opinion, but I would like to read an issue and think.
**Trask** 33:13 Yeah, sounds good.
**Liudmila Molkova** 33:15 Yeah, and it's also bike shedding.
Okay.
**Madhav** 33:22 Okay, yeah.
**Trask** 33:22 Thanks for opening all those issues though.
**Madhav** 33:25 Yeah, I'll open the last one for the header and trailer, but I've already informed you about it, and I think we are okay for most of it, just the error one is the one that we'll have discussion on the ticket itself.
**Trask** 33:37 Okay.
**Madhav** 33:38 Okay.
**Trask** 33:38 Josh, are we sharing a Zoom room?
**Liudmila Molkova** 33:44 Oops. Oh, I thought Josh is interested.
**Trask** 33:48 Or… or we're just blocking the account.
**jmacdonald** 33:56 Can you hear me?
**Trask** 33:57 Yeah.
**jmacdonald** 33:58 Sorry, yeah, this is the second time. We think this is the same room as the Arrow SIG wants to start right now, and I.
**Liudmila Molkova** 34:03 Oh.
**jmacdonald** 34:04 trying to figure out if that's the case. I don't know what to do about this, Trask.
**Trask** 34:09 Posted. I posted on the on your community issue when you opened it.
**jmacdonald** 34:14 Yeah.
**Trask** 34:15 Yeah, I posted with the problem.
**jmacdonald** 34:19 I understood the problem. I don't know what to do about it.
**Trask** 34:21 Didn't I assign it to the person who needs to fix it?
**jmacdonald** 34:25 I think you did. Okay, so we need to bug Ted.
**Trask** 34:28 Yes, you need to bug your GC liaison, yes.
**jmacdonald** 34:30 Okay.
The GZ liaison for this SIG, okay.
**Trask** 34:35 No, no, GC liaison for your SIG. You're my GC.
**jmacdonald** 34:38 liaison task.
**Trask** 34:41 Oh, for… oh, no, no, sorry, for the SIG that… Scheduled it wrong.
**jmacdonald** 34:47 Okay, for this sake.
**Trask** 34:48 It was not this. Which sig was it? I forget.
**jmacdonald** 34:53 I'm confused, Trask. The arrow signates on this room right now.
**Trask** 34:58 I know. I thought I commented on your issue with the exact problem and who needed to fix what. OK.
Let me…
**jmacdonald** 35:11 In the moment, I don't quite know what to I think…
**Trask** 35:17 Get it fixed before two weeks passes. Did I not? Yes, yes, I did.
**jmacdonald** 35:25 So I think.
**Trask** 35:25 It's the packaging. It's the packaging thing that messed up.
**jmacdonald** 35:29 Yeah, that's what… I don't understand. See, I don't understand. But… Because this says it's room 2.
Gee, this is… this is the Zoom room number.
**Trask** 35:38 Yeah, we can have two meetings concurrently in each Zoom account.
**jmacdonald** 35:45 Okay.
I'm confused, but… Nevertheless… Do you think we can start our, arrow meeting right now?
**Trask** 35:53 Oh, yeah, yeah, yeah. I think everybody dropped except us, so… Oh, and a meeting assistant, so…
**jmacdonald** 36:00 That's the problem.
**Trask** 36:00 And yeah, you can try.
**jmacdonald** 36:04 Are you the host?
**Trask** 36:05 I am not.
**jmacdonald** 36:07 Okay.
I wanted to try and kick out the note-taker.
**Trask** 36:11 You can… You should have access to the…
**jmacdonald** 36:18 I'm not logged in. This is okay. This is the problem is that I wake up in the morning and I have to do things with my brain.
I have to log in, which I should have been logged in.
**Trask** 36:33 No, it's, there's a document… Here, let me — I'm just going to —.
**jmacdonald** 36:42 Found that document.
**Trask** 36:43 You found it?
**jmacdonald** 36:44 Well, I had it earlier a second ago.
**Trask** 36:50 Which room are we in?
I can punch it in.
**jmacdonald** 36:53 Room. Room number 2.
**Trask** 36:56 Okay, hang on. I'm on my phone, so this is why it's a little more challenging.
How do I… take… Here, let me just, Teams you the host key.
I can't find where to plug it in.
**jmacdonald** 37:18 Yeah, this is… Zoom… I can't understand Zoom, basically.
Okay, that's the key.
**Trask** 37:28 Yeah, so if you you want to do something like take.
ownership, or…
**jmacdonald** 37:48 Okay, well, Trask, you're on a phone. You can… you can… you've given me everything. I don't know what to do, but I'll.
**Trask** 37:54 I'll rejoin… I can rejoin on my computer now. I was just on my phone earlier because I was making coffee and it was too early in the morning.
Okay, just a sec. I'll be right back.
