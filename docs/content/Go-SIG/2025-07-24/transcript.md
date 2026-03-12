SIG: Go SIG
Date: 2025-07-24
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/qCyIYGuFukh3IVoWxA20UMVtGzipBv181V7Xjz59_AiWz0OH-8K1Ry-QAbOSHlZT.JfXIIg9aBld_Nwbj
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 02:39 Hey, everyone.
**Damien Mathieu** 02:45 Hey!
**Tyler Yahn** 02:47 How's it going.
**Damien Mathieu** 02:48 Good! How are you?
**Tyler Yahn** 02:50 Doing? Well, yeah.
**Bryan Boreham** 02:55 Hello!
My first.st
**Tyler Yahn** 02:59 Hi! Brian!
Hey, Sam!
**Sam** 03:08 Hey, Taylor.
**Tyler Yahn** 03:11 How you doing.
**Damien Mathieu** 03:12 Hey!
**Sam** 03:13 Good hey? Damian!
**Tyler Yahn** 03:32 Well, cool, all right. I'm looking at the agenda. It looks like Sam. You had something in the next week that I put in the agenda for this week or the next meeting, and so I moved that down. I didn't move Roberts down because it looks stale, and he's not going to be here for today's meeting. So I'm just gonna leave that one off.
But if anybody else has something they want to talk about or additional things they want to talk about. Why don't you go ahead and add them there, and I'll start sharing my screen here in just a little bit, and we can jump in.
Awesome. Okay.
all right. So Sam, 1st up, you wanted to talk about host, text, attribute propagator and contrib for support.
SQL, commenter.
**Sam** 04:35 Yeah, so this is kind of the support from the single commenter, because, the where should I start oh, so this sequel commenter adds, propagation ability to kind of correlate the single client between the database. But it has some issue like, because database doesn't support natively tracing. So what we usually do is we will run the receiver in the collector that will periodically run the query against the database and put the query that is currently running, which basically means it's it's doing another sampling. So even we push the trace information to the database versus commenter the chance to correlate these 2 is not very high.
So I, trying to bring this text, attributes propagator to support the single commenter, which means, at this we can have a stable correlation on their service level because a user can always push the service name of of of the sequel client. So when the receiver called the database. We we always know what what is the client name of that. But that that's just the context here. My, my question is.
do you think, host propagator, like text attributes in the contribute? Would that be acceptable.
**Tyler Yahn** 06:39 yeah, I'm still not quite getting. What? What is this going to be used for? Like? Is it just going to be used in hotel sequel, or where? Where is this used?
**Sam** 06:50 It.
Yeah, in in go probably is gonna only use for hotel, but other. But we also have other library, probably.
I know some library like also doing the SQL. Instrumentation. They could probably also use that.
**Tyler Yahn** 07:17 I mean.
yeah, I I think we need to have some use cases in in like the go space. I think before we wanna try to host this like, is the collector trying to use this.
**Sam** 07:32 No collector is just kind of like the second step to fetch this information from the database. But in order to have such information in the database. We need to per push it to the database first, st and this propagator used for sequel client can make that information pushed to the database.
So I have a demo, and that that there is a Pr. Or do not merge, and if you, if you check that.
Yeah, this is what probably it looks like. And if you going back to description of this Pr.
there is a usage yeah, there is a link, says this is the example of usage.
**Tyler Yahn** 08:35 One time. Okay.
Okay.
**Sam** 08:47 Yeah, so basically just composed.
And a propagator with trace contacts.
And this text attributes propagator can take attributes as parameter. And so it could propagate a service name of the client to the database.
**Tyler Yahn** 09:14 Yeah. So I can you walk me through like what's going on here? I'm pretty ignorant of what's actually happening. So like, what what are you trying to accomplish? I guess. So like right now, you have communication that goes from a service to a database. And and you're trying to propagate context along that communication, protocol.
**Sam** 09:31 So so after we put this.
the the sequel commenter will inject comments to every SQL. Query when it when there is a code to the database. Right? So with this propagator, it also push the service name as one of the comments to the database. So when collector side, when when collector fetch this Query samples from the database, it also has this service name, so it knows that which client I mean it. It knows the client name.
**Tyler Yahn** 10:18 Yeah, okay, I think I see what you're saying. And so essentially, anything in the in the the database you can annotate with like.
I guess this is. Is it tracing information? Sorry are you intending to put like a trace Id in here, or are you trending just to have like service? Name.
**Sam** 10:35 Yeah, I I think that trace Id is also is another thing. But what I'm trying to say is, even, we have trace Id, because the way, how we collect the query sample from the collect side, it's actually doing another sampling, because what collector can do is it can only fetch to currently that is, run the the query that is currently running.
But you know we cannot just run the the the fetch query against the database. Every 1 ms right? So it's very likely that the query that you fetched that is currently running is is not all of the query run in the past. So this behavior is actually doing another query, sampling so and or trace sampling. So I mean, even we push the trace information from the client to the database when we actually fetch it from the database.
The trees we got might not sample in the client side.
So I mean.
that makes the correlation between the client to the server. Not very stable without, even with the we don't even guarantee that the the trace we have can.
What can correlate.
That's why I'm trying to push more attribute like the service name. At this we can. With that we can guarantee that. Oh, we know it's the client.
It's the client name.
**Tyler Yahn** 12:21 Hmm, okay, I see.
Yeah, okay, that makes sense is the I mean, I think this this propagator looks like it should live. Next to this thing that's called this SQL. Commenter, though right? Or is there like a more general SQL. Commenter? This is using.
**Sam** 12:45 So this is only example. So ideally, I think it should be put into the language control.
So like. So all the database documentation could just reuse this propagator instead of implement their own.
**Tyler Yahn** 13:04 Hmm!
How would you do that, though given, this is an option to this package.
**Sam** 13:13 Like like, what? What do you mean?
**Tyler Yahn** 13:18 Well, I mean. So what I'm saying is that, like this text, attribute propagator is tied to this implementation because we want to have it associated with this SQL. Commenter. But the SQL. Commenter looks like it's specific to this package.
**Sam** 13:32 Yeah.
Yeah. Seal commentary should tie to the instrumentation. That's that's for sure.
By, well, I I mean this attribute of this with single commenter, you only accept propagator. Right? So the implementation of the propagator can live. Other place and user could just use it.
**Tyler Yahn** 14:03 Yeah, I think I think that makes sense. Yeah, I'm just going back to your original question of like, should this live in the contrib.
But I don't think there's like it. Seems like this is, this is very much tied to this implementation here.
And I think it should live here, at least until there's there's multiple use cases right like this is the use case that it exists in. And like, this is the only place that it's it's used right.
**Sam** 14:27 Yeah.
**Tyler Yahn** 14:27 I think I think if you so I guess maybe what I'm saying is like, I don't see like the the scope outside of this this package like you're you were saying that there are other database packages that may want to use this and and so like, if if we can show that that's the case, and that it would benefit from having a centralized like definition of this type, this this propagator.
I think that would motivate moving it to contribute. But I think we need to see that first.st
**Sam** 14:57 Yeah, yeah, that that makes sense. So next step is what we probably gonna to push this propagator to the spec to, you know, maybe centralize. But before that, I think it's it's it's better to ask sick people. So I mean linguistic people. So I know, like what it can actually do when they implement it.
**Tyler Yahn** 15:24 Yeah. Do you know other database authors or database instrumentation authors that are are planning to use.
**Sam** 15:30 In go? Probably not because go already. Have a centralized Seco sequel interface right?
But in other big database like I know done that they have specific SQL. Client. Just work for SQL. Server.
I mean, that's 1 of the instrumentation, right? They they must have something else. So for that has they? They will need a centralized place to put this propagated.
**Tyler Yahn** 16:02 Oh, okay, I see what you're saying. Yeah.
Hmm, how does this propagator get used? If it's just like used alongside like Http. Instrumentation?
Does it encode these things in a header.
**Sam** 16:22 And I think he only called the courier, so he doesn't care. Actually.
**Tyler Yahn** 16:31 It doesn't care.
**Sam** 16:32 I I mean, the the implementation of this propagator doesn't, doesn't care what the underlying carrier is.
Because you just take the text map carrier and just set, and it's done so it can also be used for headers. If user want to put something like, you know their custom header.
**Tyler Yahn** 17:00 So isn't this like so how does this work with the like baggage, though? Like, I guess it's kind of the question then, because isn't baggage supposed to be that thing that encodes this like attribute, like custom, specific attributes in in a W. 3 C. Form.
**Sam** 17:18 Yeah, that that's a good question. But baggage is kind of like, once you set it, it will be everywhere, right. And I I don't think user will like there some attribute that's specifically tied to the database they propagate everywhere.
So that that's my, especially when we're talking about like, we want to propagate a service name right? If we put the service, name the propagator, I mean the baggage. Then this attribute will be everywhere, even in other service.
So so that's my concern.
**Tyler Yahn** 18:03 Well, but isn't that the case here, though like, isn't, isn't this going to be everywhere like, yeah, this setup here.
**Sam** 18:12 Every time.
The the user may may need to inject other service thing like for this application they use seco, hotel seco dash example right, but for other service they might need they. They're gonna need the other name.
But if they just set the baggage ahead of this, then this baggage. Will we propagate to other service, like everywhere? Right? If a call B and a set that this package, then B will also get this, the baggage with the same value.
**Tyler Yahn** 18:51 Yeah, I'm just. I'm wondering why we couldn't use a baggage propagator here, something that propagates baggage.
**Sam** 18:55 Oh! Directly!
**Tyler Yahn** 18:58 Yeah, like, why in this, why does it take this format, instead of reusing something like that.
**Sam** 19:06 Oh, that's a good question.
**Tyler Yahn** 19:18 I don't know the answer. It was genuinely, yeah, I don't know.
**Sam** 19:26 Yeah, I I don't know. I've already forgotten implementation of package. So.
**Tyler Yahn** 19:33 Well, you're not alone. Okay, maybe we we can look into that. But all right. Yeah, I think that. That's I. Yeah. I'd be interested in looking into that, because, like that also might be very helpful in in formatting, because then you could use the W. 3 C. Standard for these comments, and then you don't have to redefine like a new specification for specifically this.
But it may also not be applicable. I haven't thought it through all either. So like I'm just kind of more coming up with questions.
But yeah, I mean, I think to your point, like of asking about contributing here. I think we can do that if we need some sort of motivation outside of this, this specific instrumentation. So like, if there are multiple instrumentation libraries which I mean, I don't think that that's impossible to find that are going to want to support this.
Then then that might be a good motivator. But I think we need an n plus one sort of thing or sorry a 2, and is one in that situation. Yeah, so because otherwise, like, it makes a lot of sense to just leave it here right? Because this is the only place that it's actually used. But if this is going to exist in other SQL. Libraries, I think that that's a great, great idea.
But yeah, I would also want to know, yeah, exactly. Yeah. Okay, cool.
yeah. I I am interested. I'd have to look more into this. I haven't looked at this like at all until we just started talking. So I would like to know more about the format. That'd be kind of interesting.
Okay, I can. I can keep taking a look at this as well. Maybe we could talk as well next week when I have a little bit more understanding.
But yeah, sure, yeah.
Okay, all right with that. Then next up on the agenda, Damien, you wanted to just say, you're gonna be off most.
**Damien Mathieu** 21:37 Yeah, it's it's just informative.
**Tyler Yahn** 21:40 Yeah, okay, that sounds good. Hopefully, you're off having fun.
Yeah, I think that's that's a requirement. If you're in Europe, you're supposed to take at least a month off. So I think you're you're doing a good job there.
Okay, nothing else on the written agenda.
I'm going to stop sharing my screen here.
Any other topics people wanted to talk about. I didn't have anything else set up, and we just went through our goals last week, so I didn't add them to the list, either here. But maybe in a week or 2 we can talk about actually Damien, are you going to be gone next week. Does that.
**Damien Mathieu** 22:20 Next week is when it's too late for me, like it's the 7 pm. One. So I will not be attending next week. Yeah.
**Tyler Yahn** 22:29 Let's maybe just check in on the goals while while you're here.
**Damien Mathieu** 22:34 Yes.
**Tyler Yahn** 22:36 Yeah. Cause yeah, timing wise that that would make sense.
**Damien Mathieu** 22:41 I don't.
**Tyler Yahn** 22:41 Think.
I don't think there's anything burning, but I just want to make sure we don't forget something here.
Okay.
So I also know that David is. If he's not on leave right now, it's very soon coming up as well for fraternity leave. So we talked about these last time. SDK, self observability signals. This is something Robert's also picking up and working on, and he's parsing out. So this is something that we have. I think, some good good work going on here. The runtime metric stabilization there is still work in progress on this one. I think it's actually done. We're just looking at like removing the old version. So like, if I remember correctly.
yeah, we rolled it out. We're going to wait 2, 3 months for your feedback. Yeah. So once it becomes the default which is in the next release. So yeah, looking good on this, too. The logs api stability. Obviously this is more blocked on the specification, a lot of great movement going forwards. We're looking to stabilize the the complex value specifically around the any value to get like a prototype. We talked about this last meeting as well. It's in the meeting notes the Http stabilization. Yeah, this is probably a good one. So this one.
**Damien Mathieu** 23:58 So we removed.
Sorry we remove support for the old 70 conventions. So it's going to ship with the next release, and there is some cleanup to do, because, like the removal was just like removing the old one. But we still have weird stuff in the same package.
so I intend to change that, to make it nicer. In September.
There should be. No, no rush. It's going like it's an internal package, and it there's not going to be any visible changes. It's just like cleanup on our end.
**Tyler Yahn** 24:36 Yeah, yeah, I, right, exactly. Yeah, that sounds good. So I'm going to say, once we get this release out, we'll we'll be done with this and then any other follow-up tasks. I don't know if you want to create issues in this upcoming week or so, and you can. Just I mean also, that's another thing is like, if you really want to do them, maybe just hide them. But otherwise, if you want somebody else to do them. You might just want to also create some tasks. For while.
yeah, I'll create an issue just in case someone wants to tackle them.
**Damien Mathieu** 25:05 Yeah, yeah, I fear, like, it's not a good 1st getting started issue, either, I think. But someone like.
**Tyler Yahn** 25:13 What?
That's a good point, because we're looking for really in that cleanup redesigning a lot of that. And how we interact. Okay? So.
**Damien Mathieu** 25:19 Yes, sir.
**Tyler Yahn** 25:20 I feel like.
**Damien Mathieu** 25:21 We've we've relied a lot on new contributors for setting up the internal package originally, and I find it's it has ended up being a bit of a mess.
which is which is not due to anyone's fault. It's more that because many people have been looking at it without any coordination. It's it's hard to make things make sense.
**Tyler Yahn** 25:47 Yeah, that way.
Hmm.
I did just notice that this is also called the stabilization of Hotel Http. And this is for a project for migration.
**Damien Mathieu** 26:01 Yeah, because we said that we couldn't do. We couldn't even think of stabilization before that was that happened.
I.
**Tyler Yahn** 26:10 Yeah.
**Damien Mathieu** 26:11 Yeah. The question is, do we feel happy with figuring out Api for Http or not?
I think there is work we could be doing on Hotel Http.
especially like the things we mentioned at the beginning of the year. We've kind of repetitions between packages and making things nicer that way, but I'm not sure that would be any breaking changes, so I'm not sure that's a blocker for stabilization.
**Tyler Yahn** 26:41 I, yeah.
I definitely don't think we're ready to stabilize it. I definitely think there needs to be some review of the package.
**Damien Mathieu** 26:49 Yeah, yeah.
**Tyler Yahn** 26:50 Yeah, yeah.
**Damien Mathieu** 26:51 But yes, I I agree. I'm just saying I'm not sure we have any blocker changes before we start seeing. Let's start reviewing.
**Tyler Yahn** 27:00 Yeah, right? Okay, I think we're on the same page. Then.
okay, so let's let's plan on really tackling that. I think in the last quarter of the year when when you're back.
Okay.
file based configuration. We talked about this. This is something Robert's also looking into and just verifying the stabilization at the spec level.
This is done so cool. All right. Yeah, I think that's it for the goals here. Any other things people want to talk about on this one. I think we're actually looking good.
The logs Api stability is the only one. I think there's some.
There's some questions there, but otherwise yeah.
cool, I think, other than that, Damien. Anything else come to mind that. Maybe we want to touch base before we send you off.
**Damien Mathieu** 27:56 I don't think so.
**Tyler Yahn** 27:59 Yeah, I don't think so, either. Okay.
okay, well, cool. I think it's probably good to end it here. Then, if that's the case. Thanks everyone for joining. Appreciate the time and effort. I will see you all in a week's time, or asynchronously, bye.
**Damien Mathieu** 28:15 Bye.
