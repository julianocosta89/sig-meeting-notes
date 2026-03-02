SIG: eBPF instrumentation
Date: 2025-06-18
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Mattia Meleleo** 00:50 And our phone.
**Rafael Roquetto** 00:52 Hey, Mattia, how's it going.
**Mattia Meleleo** 00:54 Good good!
I'm almost done with. The my SQL. Changes.
**Rafael Roquetto** 01:00 Cool, cool.
Yeah.
Are you based in Italy?
**Mattia Meleleo** 01:06 Yeah, I'm in South Italy. I'm in Puglia.
**Rafael Roquetto** 01:10 Cool, cool. I have a
one of my masters in programming like his. His father is from Puglia. Yeah.
**Mattia Meleleo** 01:18 Oh, nice!
**Rafael Roquetto** 01:19 That's it.
**Mattia Meleleo** 01:21 Hello! Everyone.
**Tyler Yahn** 01:26 Hey!
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:31 Welcome back! Tyler!
**Tyler Yahn** 01:32 Hey? Yeah. Thanks.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:35 This is a trick.
**Tyler Yahn** 01:36 Oh, it's great. Yeah. Good. Take time away.
Get you energized to come back. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:42 Amazing.
**Tyler Yahn** 01:46 Okay, you have any plans for the summer, Nicola.
Vacation.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:52 Yeah, I'm good.
Yeah. I'm gonna go end of August Conference in Halifax, Nova Scotia.
So I'm gonna take a trip around the East Coast, Canada.
**Tyler Yahn** 02:04 Yeah, nice.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:06 The Atlantic, Canada ban.
**Tyler Yahn** 02:08 Yeah.
Gonna do some cod fishing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:11 Yeah, maybe you know, whale watching?
Yeah, exactly. Yeah. Yeah.
**Tyler Yahn** 02:22 Well, cool. Yeah. So I see some people trickling in. I also see we don't have an agenda currently. So if you have topics you wanted to talk about. Please go ahead and add them there. If you haven't yet. Also add your name to the attendees list.
and we can get started here in just a little bit
cool. All right. So we could jump in here. Welcome, everyone.
I've
good to see you all. It's been a little bit Nicola, you wanted to start us off by talking about the status update.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:46 And migrating.
Yeah, yeah, I just wanted to bring it up unless Mario wants to talk. He's been doing a lot of the work. But yeah, I can give an update, too.
I guess. Starting from 2 weeks ago.
we went like full on, so that you may have seen some Prs go in related to
making certain things public where they're internal and whatever that's just to help us with a transition.
But I think we've taken out probably 2 thirds of the Bela Code base. And now it's just vendor in Obi. I think by the end of the week we're hoping that it will just be some random stuff that we have to deprecate and
just kind of retire in the next major release. But the Beta Code base is now
fully vendoring everything Ebpf related, at least
and we're slowly working out on the
yeah, the rest of the exporters, metrics, whatever else we have. There's some stuff that we need still need because of the process metrics. I don't know if we're gonna retire. Those that were taken out from ob.
but majority of that is going away.
Yeah. So hopefully, after we do that, and everything's like taken out
that we can go and review and start to move a bunch of stuff back to internal
**Tyler Yahn** 05:10 Awesome. That's great news. That's really exciting news. Actually, yeah, thanks for every Mario and everyone. Thanks for working on that. That's definitely really exciting.
Cool.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:24 Became unsustainable. Like we realized, like, we were just yeah working on bail and then porting changes our stream. It's just too much pain. And we were missing changes. We made mistakes. And we're like, okay, well.
enough of this.
Yeah.
**Tyler Yahn** 05:41 Awesome. Well, I mean, yeah, I'm all about it. I love seeing projects like this. Just get fully open source. And and working in this community would be great. So you know, moving that forward, that sounds great.
So on that note, maybe we could jump through the open pull requests and see if we can help this along, or unblock it in any way, or find out any sort of details about what's left.
I don't know if we wanted to go through a lot of the open ones, but I don't see some people on the call, but I guess that's fine. So
I guess we can start here. So the port of 1813 add Service name template. This is from Mark. I don't know if Mark's I didn't see Mark on the call.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:24 I think he's here. But essentially, yeah, we need to see if that's still required. I think somebody like.
**Tyler Yahn** 06:30 Yes.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:31 A community member out of this
service name template. We need to see if
some changes might be ported, because we're now we're going package by package
between Bela and Ob. We're looking at anything that's different. And then still moving stuff upstream where it was that a lot of that happened last week.
so we need to see what is remaining here. That needs to be done. But I think it's.
**Marc** 06:57 Yeah, thanks. For.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:58 You're very quiet, Mark. I don't know. Like maybe check your mic.
**Marc** 07:07 What about now?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:08 Oh, that's good!
**Marc** 07:10 Yeah, no, that I. Yeah. Thanks for the reminder just
how to merge it. And that's it, I think should be yeah, straightforward.
**Tyler Yahn** 07:22 Sorry. Say that one more time, mark you, you wanted to.
**Marc** 07:25 No, just like I opened this port request
2 weeks ago, and I completely forgot I was on vacation. And now still catching up. So yeah.
**Tyler Yahn** 07:35 Yeah, okay, alright. So you're just gonna take another look at this and then clean it up. Or, okay, all right, cool. Yeah, yeah. No worries. Oh, yeah, that sounds great, perfect.
Okay, cool. Next up is Parse, Mysql data in the kernel space. Let's see, I don't know if the author's on.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:53 Yeah, it's me. It's me. Yeah, I've almost finished. I applied all the changes that we discussed offline with Nigra.
**Mattia Meleleo** 08:03 There is only one thing left to handle, which is the multi pocket request and response. So I need to add the support for pending to the to this buffers.
and then it should be ready to go. I I also need to add some some tests. I I think I added the
like an integration test in the old Pr in the in the Grafana repo.
I probably need to to just copy paste. It.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:36 That should be great.
**Tyler Yahn** 08:38 Yeah, yeah, that'd be great. Is there a reason? Is this failing? Have you taken a look at.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:44 Yeah, it probably misses all the changes that's in some early thing. Yeah. Okay.
**Tyler Yahn** 08:53 Well, cool, all right. We'll we'll look for updates on this one. Then.
Thanks, Mattia.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:57 Yeah, they they like, I really like what they they brought up in the meeting. You were not here. But
for the, there's quite a bit of a performance benefit. Right? Now, what we do in ob is we detect. There's an unknown Tcp traffic, and then we send it to user space, where it kind of is determined what the protocol is, and then we generate traces or metrics.
But they brought a really good point. Mattia and Nimrod last time, saying that I mean some of this detection could be done in Ebps space, and
hmm we would not be sending stuff that we don't know of in user space.
So that we're we're looking at sort of like a mixed design that when this proposal is and what we have to actually
get the benefit out. I think it's gonna be great. I'm really excited about the final state of that.
**Tyler Yahn** 09:52 Yeah, I am, too. That sounds very great.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:56 Yeah, so yeah, some protocols are, gonna be difficult. We we discussed. But something like this sequel is is pretty sweet.
and and they also have a really good point about right now, Baila, for performance reasons, or ob including do you use a really small buffers for the Tcp traffic. It's only 2 56 Byte.
which isn't enough for some more advanced sort of like, if a user wants to see the full query, or you want to do more analysis on that data?
I know people have asked in the past to expose all headers in Http. And stuff. So Matte is also working on
enabling this additional buffers to be shipped so that can be analyzed if enabled.
So that we can kind of work with protocols that have more like
more of the payload is important to end users.
**Tyler Yahn** 10:52 Hmm.
**Mattia Meleleo** 10:53 Yeah, right now they are dynamic, like,
the buffer is is big like 200 Byte. It will be there will be sent 200 Byte
but the user can specify a maximum amount of data like 8 8 k maximum.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:11 Okay. Yeah.
**Tyler Yahn** 11:13 I see.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:14 If they want to pay the price, you know, there's some there's gonna be downside to that like. Obviously, it's gonna be slower. It's gonna take more overhead. But it's user chooses versus, you know.
**Tyler Yahn** 11:25 Yeah, I think.
**Mattia Meleleo** 11:26 Yeah, this will also come sorry. This will also come handy when when doing stuff with with other databases, other protocols, and also for Http full payload.
**Tyler Yahn** 11:40 Yeah. Oh, a hundred percent. Yeah, definitely can see that. Yeah.
Yeah. I imagine just having the configurability is gonna be really helpful for troubleshooting as well as I guess, for just user specific desire, right? Like, that's gonna be really key. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:55 Yeah, yeah.
A lot of people have like asked us on the old Baylor repo where they're like, Oh, can I see all headers? Can you guys put them in the traces, you know.
I mean, and it may be a bad idea if there's authorization headers, you don't don't want to do that. But
but they want to say, I want to pick and choose between. I wanna see content type.
**Tyler Yahn** 12:19 This is something that was brought up. I mean, it's in the semantic conventions, actually like, there's a semantic convention.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:23 For the.
**Tyler Yahn** 12:24 Letters, and they
what you just described is exactly the the sentiment it's like they're not recommended, but they are recommended to be configurably enabled
for that exact reason, because, like one, it's a security issue. If you're not careful. And then 2, it's like it's it could be a lot and overwhelmed a lot of things. So yeah, I think what you described is also the solution. Everyone else came up with.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:47 So, yeah, this will give us that
ability. Because right now with the small buffers, yeah, the performance. But at the same time you can't implement.
**Tyler Yahn** 12:57 Yeah, no. Okay, cool.
All right. Awesome. All right. So it looks like this is just going to take a few more iterations. So sounds good.
We can move on. Next one is just a dependency update which just needs to get looked at. There's this
Jason, Rpc. Or, sorry, did somebody want to talk about the dependency update.
**MM Mario Macias** 13:18 Oh, yeah, some of them. We got many of them every day. I merge as most of I can. Some of them fail. Then I say, I will check later. I think maybe some of them are even updated, because especially doger images are
many. Docker images are daily refreshed. I don't know if if we can configure this bot to to work or to send. For example, one daily, we pull request with all the changes, instead of many individual pull requests. I don't know if that's possible.
**Tyler Yahn** 13:57 I definitely think it's configurable I don't know about. I've never found one where it says like
So so 1st off, I don't think you want to do them all in the same pull. Request that that's probably a bad idea, just because if you have, you know, 5 different things in the same pull request. And one of them actually is failing because it's a conflicting dependency, then that means that, like the other 4, are dragged down with it. But that
that that's kind of beside the point, because, like what you're, I think maybe also describing is like, if you could just get those 5 pull requests opened on Friday, right, or or Monday, or something like that, instead of all week, is is going to be better.
if I'm understanding you correctly, Mario.
**MM Mario Macias** 14:40 Oh, yeah, maybe. Yeah. What I I mean.
yeah, what I ha happens sometimes is that I I get every day like before, every every morning when I wake up. So maybe this is restricted to one day. Maybe it's better, but I mean for me, it will be even useful, more useful to have one packed into everything packed into one so revise because at the end they are must mostly.
changing the digest. Numbers of of docker images.
**Tyler Yahn** 15:20 I think so. I think you can group things like that so like if you want, if we wanted to. Group, like all the the docker digest numbers. I'm pretty sure we can group all those into a single pull request that that I think is possible.
yeah, I mean, we. I definitely like, you can look around at a lot of other repositories because they have different configs for renovate bot. And they will.
I mean, there's definitely like.
yeah, there's the default is not great, because there's a lot of spew, especially when, like certain modules are Updated in sync.
You know, a good example, is just like the hotel module for open telemetry like that. We release that. And there's like 5 different modules, or probably 20 different modules actually, that get released at the same time. And if you didn't group them into the same Pr, it's just it's kind of worthless, because, like, they're meant to be updated in sync, anyways. So yeah, we we can definitely take a look at that. I know that.
like the a good place to look is probably
the collector. This is really good for go components. Let's see.
it's somewhere here. I always forget where it is. Maybe it's here.
I also think that it's like a different I always forget.
Oh, yeah, there it is. It's not a hidden file.
So yeah, like this sort of thing.
Man, there's a lot.
Yeah. So I think, here you go. This. This might actually be what we're looking for. So docker file, you can group all the docker file dependencies together.
**MM Mario Macias** 16:57 I think.
**Tyler Yahn** 16:58 They do?
**MM Mario Macias** 16:58 Exact same thing. Yeah, yeah.
Similar with in the okay.
Okay. Yep, okay, I will. I will have a look. Yeah.
**Tyler Yahn** 17:10 Yeah. And in the past, like we've, I think in other repos, we've just copied this. There's a lot of copying that goes around open solitry on this one. Because, like, yeah, like, here's a great example, like the build tools like, you can group all the go MoD, build tools together, right like, cause. That's just there's really no reason they wouldn't get updated together. Yeah. So I think we could do a lot of copying of a lot of this.
**MM Mario Macias** 17:32 Okay.
**Tyler Yahn** 17:32 So yeah, take a look. Here.
**MM Mario Macias** 17:34 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:36 Maybe.
**Rafael Roquetto** 17:36 Another thing that we could do parallel to this. I don't know if it makes sense, or is it terrible? But now we push a docker image every time there's a new push to many. So even if the docker file hasn't changed, for instance, so another thing you could do is not do that, and instead only push the docker image. When there is an actual change to the docker file that originates the image, then we would end up with less
hash is being pushed. I don't know if that that works. Just an idea.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:07 You mean the generator image, or the.
**Rafael Roquetto** 18:12 Both both both
I mean, of course, if main code, probably the I guess there's only a passage generator image, you're right.
Yeah, you wouldn't apply to the main one is, yeah, correct. Yeah, you're right.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:28 Maybe we.
We can also do auto merge auto merge is another option. So we don't have to go manually. Click the button.
Yes, with the Pr.
**Tyler Yahn** 18:38 Yeah, do that. No, but there! So there's
there's a whole thing around. Why, you can't do that. But.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:47 Kind of.
**Tyler Yahn** 18:47 There is a thing that I have seen in the specification where you can do this like group, I think.
trying to find where this would be like, there's there's like some sort of like workflow, I think. Maybe
sorry.
Oh, here you go, I mean, I think this is also what we were looking for for patch releases and grouping on the schedule.
That might be helpful. So it would help, yeah. So this is another. Yeah. Again, they get like, just
just searching around in a bunch of other repositories usually is the answer,
so yeah, I, they do these things here where like they can. I'm trying to think of like the exact term that they use. But like they.
yeah, I think this might be one.
There's a way to group them essentially. And it, it puts it into some sort of state where it will just try to merge it.
if if it's if it's ready to merge. So I think that it's a like it gets. I think it gets around the merge queue so where you can't click it. But it does like allow like more restrictions. I can look into that as well. Nicola. The merge queue thing is a problem, because, like it gives permissions to people to put it into the queue that shouldn't have merge rights and so that was like.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:09 Okay.
Yeah.
Okay, fair.
That's okay.
Man.
**Tyler Yahn** 20:13 I wish we could do that. We've we've done it in the past, and it was great. But yeah, so I if we can. I can look a little further into this thing that they do in the specification to try to get around it.
it's like it groups, I think. And so it's like, if it's in a group, then it will try to merge the whole group, you know, one after the other. But yeah.
I agree. I think it would help a lot.
But yeah, okay, so there's a few different things. Obviously, there's 2 different renovate configs that would be really helpful there. So yeah, I think that's that's good.
Sorry, Raphael, was that. Did that answer your question?
**Rafael Roquetto** 20:48 Yep.
**Tyler Yahn** 20:51 Cool. All right. So
outside of these dependency Prs, then we also have this Json, Rpc, 2.0 support.
I don't know. I don't guessing the author is not on.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:07 Yeah, I think, times, time, zone issue. Yeah.
**Tyler Yahn** 21:11 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:12 But we we sort of asked them to move. This Pr. Was going on for a while in the Baylor repo, so we've asked them to move over here.
and so yeah, they're working towards implementing
Json, rpc, so right now, I guess
it's a regular Http request, which they're not happy about because everything looks like a single request.
So they want to extract the context from the Http body to what.
**Tyler Yahn** 21:42 Maybe.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:42 Function is and generate Rpc. Spec. Rather than Http. Spec.
**Tyler Yahn** 21:50 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:50 My understanding is that it's like you call Jason. Rpc. Is like you call a standard endpoint. But then you say inside what you want to call essentially in the body.
so every request looks like and execute, and it's not useful.
**Tyler Yahn** 22:11 That makes sense. Yeah, no, that sounds like a great feature to add to that. Yeah, definitely.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:17 Yeah. So looking through reviews, yeah. Or if I.
**Tyler Yahn** 22:21 They're pretty active.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:21 Yeah, yeah, they're very active. That's great, great developers. So they.
I think there was somebody else that started doing the exact same thing. But for Nongo
**Tyler Yahn** 22:33 And then.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:34 Different approach, and they've sort of gone quiet. We have to see what's happening there. But maybe once this goes in, once we have the spec we can pick up and use the same
stuff. Or, yeah.
**Tyler Yahn** 22:50 Yeah, I agree.
Okay.
well, cool. It looks like there's some more iteration needed from the author here. Raphael still up to date on the review. So yeah, nothing needed, I think, from this. But yeah, this is great to know. Thanks for the update.
Okay, these next are dependencies as well. I think we can skip those.
Stop, go. Http. Context propagation on invalid headers is something from you, Nicola. Anything.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:21 Yeah.
**Tyler Yahn** 23:21 Like we've got 2 reviews here.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:24 Yeah. So I, I, we encountered this issue user reported it as, and it's sort of weird. We didn't expect this would happen.
So this is trying to trigger our outgoing context propagation support and go on a response from a server
or so it's like, How is this even possible. You know, because there's a lot of checks in the code. That kind of detect. Is this a client request? Is this header being used for a client call so checks all these maps, and then only if it validates it says, Yeah, sure, I'll do it.
So this apparently crashed the the Dex server, which is some sort of like an open id thing people use.
I I 1st time I learned about yesterday, but it's a popular project, and apparently you enable ob on this and crashes the server. I couldn't reproduce it for me. It worked but then I was digging through the call yesterday, waiter, file, and we sort of found out that
in a response this header right subset, which we tap into.
could be called on a null header, so the header could be nil.
and it sort of works because it never touches the the actual header object internally.
It's just so they call it, on 0 header.
And so we weren't checking to see the header is 0. And so what would end up happening is, it seems like a response, and a
where the client and the server call can just key off the same thing
which is not supposed to happen like header, should be unique.
As a pointer, which we use as a key. But then, if it's 0, we just collide essentially
so technically, there could be 2 go routines, both using 0. They could do all sorts of bad things.
And so the fix is just to add the check.
If the header is no, don't, don't attempt to do this.
**Tyler Yahn** 25:25 Right pretty straightforward,
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:30 And I added some extra checks to see if we fail to like. This is sort of dangerous, because Bpf probe right user again.
**Tyler Yahn** 25:37 Yeah, maybe.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:39 I mean, I wish you could remove this code, but we can't because of Tls right now. This is the only way to do it.
We have the addition, the other support now, that would do it for even for go
using the injection of the header at at the socket time.
But if it's Tls, we're unable to, because the other socket
time is encrypted. So we still kept this support.
and the thing is, I added some extra checks to see if we couldn't find the offsets. For some reason
I just bail right now
previously, would attempt to do something, and while you may read garbage, and you report wrong events, so less of a problem if you crash the application so.
**Tyler Yahn** 26:24 Yeah, but it's still not great. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:25 It's not great. So, but I think people will tell us, okay, yeah, you're producing garbage data. But you know, fix this right? But it's crashing my app. It's a little bit more serious.
So if the offices are not
somehow resolved and we couldn't get, I just added, sort of like a paranoid check.
For the office. It's not being resolved.
and I either the check for the header not be nil, in which case, if it's nil. Then
don't do it. We can't.
**Tyler Yahn** 27:00 That makes sense.
Well, cool. Okay. Yeah. This looks ready to merge. Is there anything blocking that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:08 No, I couldn't reproduce this. I couldn't make a test. I mean, out of the code I ran all this deck server, rang Argo, CD. They had Argo, CD. Connected to Dex. I ran both. I can't see it.
but then in the logs we do, we do see Header 0 being being used, so.
**Tyler Yahn** 27:28 Even so, you see, the header being used, even though it's not crashing it. That's interesting.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:33 Yeah, because I think it needs to be. I think it must be some sort of special circumstance where the client was using 0 header
which I couldn't reproduce. If I could reproduce, I could write a test, but I.
**Tyler Yahn** 27:47 Yeah, I couldn't. Yeah. Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:51 No.
I only saw the responses doing 0, and in all cases it did what it's supposed to do. It couldn't find any client information, but I think it's like,
if the client call happens at the same time, it's probably some sort of like a concurrency thing.
**Tyler Yahn** 28:08 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:09 If there's a client call with 0 at the same time as this is happening, then we might read that information and try to both write at the same time, and then mess up. But
it it may actually not feel the problem. I don't know. Like we'll see, I mean we'll we'll fix it that this is a safe check to add, and
and if he still crashes, then we're back to the drawing board
But if you look at this image. I know it's a little bit blurry, because I can only take a screenshot
if you look at that.
I don't know if I paste it here. The address is completely bogus that we're trying to.
It looks like overwritten memory that we were trying to write on top. I guess it's not based in here, but
with the address he complains about the goal, Runtime. It's like
it's bad memory, so it must be right where we shouldn't have written something.
Oh, yeah, so dangerous. Vpf, pro, right user, right?
**Tyler Yahn** 29:15 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:16 If you get it wrong, you get it wrong. Yeah.
**Tyler Yahn** 29:22 Yeah, that's definitely okay.
Well, that sounds good. Yeah. Like you said it would be great to have tests. But I think that, like in this circumstance, like just doing defensive coding right here is probably good enough. And then hopefully, we can get a report back from the people who can reproduce it. So yeah, I think plan is merge. And then if you can get the reporter to retry.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:41 That's right.
**Tyler Yahn** 29:41 Like, yeah, that'd be great.
Awesome. Okay, I will let you determine when you want to merge that. I think it's ready. So I'll yeah.
Next up, Mario, you want to. You have this Pr for generating traces. Allow overriding resource attributes.
**MM Mario Macias** 30:00 Yeah, this is, for we are, since we are working in vendoring everything, or allow vendoring it in, in or in in the collector. There are some scenarios in which the the resource attributes provided by Ob
will defer with what the the container code requires in in this, in this, for example, this is reporting as library open telemetry, Apf. Instrument, and in Bela, for example, to avoid breaking changes, we would like to keep reporting Bela. So I I added some options to allow overriding from outside some
some attributes. If if you're gonna specify anything, it will stay with the default attributes.
**Tyler Yahn** 30:59 Yeah, that makes sense.
Yeah, okay, cool. It looks like there's 1 review just needs maybe more reviews. Or yeah, I mean.
**MM Mario Macias** 31:06 Oh, yeah, if anybody, if anybody wants to do another review, it's more than welcome.
But I it was just waiting for integration test to pass when we submitted it. Yeah.
**Tyler Yahn** 31:20 Okay, well, cool. Yeah. I I see, those are kind of the blockers. Right?
Yeah.
Okay. Well, cool. That sounds great. It looks like we've gone through all of the open issues, or I'm sorry all the open pull requests, thanks to everybody for joining on that. I think we're halfway through actually, maybe double check.
Yeah. Okay, no other agenda items, anything that came in that people want to talk about an issue. Wise, maybe something that you've opened, or something that you want to bring up.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:55 No, there, there's some cool, good, interesting issues here.
it's been open a while, I guess.
the docs are important part. I think maybe I don't know. We don't have a plan for that, but we need to figure that out sooner than later.
**MM Mario Macias** 32:11 Hmm.
**Tyler Yahn** 32:14 Yep.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 32:16 Sorry. Yeah.
**Tyler Yahn** 32:18 No, it's good just good to document. Yeah, go ahead. What we're gonna bring.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 32:20 I was gonna bring up one more item that we've sort of started discussing internally as a need that customers have expressed which doesn't exist at at the moment, and I just wanted to see what people think about it. So right now, the way that you, in ob enable traces or just metrics is by specifying the exporter.
So you say, do you want to use the hotel export which then exports both traces and metrics? Or you do want to just do the metrics endpoint, then it just metrics, or vice versa, with traces.
but it might be beneficial. Some users want to pick and choose
for which services that they've listed in, what they want to instrument to see what they want to export this elementary. So give you an example. Maybe I'm running some sort of like, let's say, pick this Argo CD. That I worked on, and I have just one metrics for Argo, CD. But I want to have full distributed traces for my actual services. I don't want to pay for traces for Argo. CD,
because I I can't like that. Application is not something, I own, but I would like to have metrics. So I can build, maybe like alerts on.
you know, something.
So
we're discussing. If we should try to extend our when we list the discovery rules to say, instrument this instrument, that instrument, this instrument that that you can actually additionally supply flags that you want to limit the instrumentation to the various telemetry types
and say, I don't want metrics. I don't want traces, or I only one subset of something.
I think that sounds like.
**Tyler Yahn** 34:04 Great idea.
Yeah, I I'm I'm all about that. I don't know why we wouldn't want to do that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:12 Yeah, it sort of makes sense right when you think about in hindsight. But
we don't have that capability right now. And the other question is, how deep do you want to go?
do you wanna start limiting them further? I only want hotel metrics. I don't want span metrics. I want this and that. Do we go further than that? Because all these are global switches right now. But I could see the benefit that you can pick and choose
to. As you define your categories, what you want to instrument, then say what you want to get as telemetry.
**Tyler Yahn** 34:46 Yeah, I mean, I definitely can see it getting much more detailed here. Because, like, I think the answer is, I would start with just an on off switch for like traces and metrics and that kind of thing. But.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:57 Thanks.
**Tyler Yahn** 34:58 You can definitely see the case where somebody would say like, Hey, I actually want a different sampling rate for this. This portion of the code. Or I want a different view in in this metrics. So like, it'll actually like, combine these things like.
I can definitely see, like way, more customization that people would want to provide to like tune down the telemetry that they're receiving. But I I think starting with just an on off switch is a great place, because, like when it would get the plumbing in in place, for like actually like connecting
some of the some of the other things might be a little harder cause. Like, yeah, like, like, like sampling rate.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 35:36 Super valid point. Sampling rate per definition is also important. Maybe you want certain a spaces. Really?
Yeah. But the.
**Tyler Yahn** 35:46 And that is probably
the problem there is like, well, one we like. We'd have to have our custom sampler then to to do that because, like we do.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 35:53 Yeah, we already do. So I think I think it should be should be doable.
**Tyler Yahn** 35:58 Yeah. So then, if that's the case like that, that would work metric wise, there may be like
different different rates that you may want to do collection on it, but that might be harder.
but it's not the end of the world. But yeah, I think just like an on off switch, because then you could also see like, how much it's used.
In some way.
And like, if if no one's actually using the on off switch or no one's complaining about it.
Then, you know, there's no use in building things people aren't going to use, I guess. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:28 Yeah,
there was somebody that actually opened an issue. I'm not sure how values. We've only seen the use case once.
their use case was like related to metrics. They were asking us like.
well, for this application. I only want the client metrics. I really don't care about the server metrics. They're really, I guess, concerned about the costs. And then, like, How far do you go? And then say, do you list the specific metrics we export. And you say, I only want these, and then the rest of the series are not actually generated.
Yeah.
**Tyler Yahn** 37:05 Yeah, so that I don't. I don't know what the metric processing pipeline looks like here, but like, that's what views are for originally right?
So like, I don't know if they can provide like. I guess this is in configuration. That's where views become a lot harder, because, like you need static language to talk about them, whereas, like views are really functional language, right? Like they're saying, like.
you know, on some sort of input give me some sort of like, you know, description of what I what I should do with this metric.
But I mean we could. We could try to.
We could try to shoehorn something like that in, you know, like, we definitely allow that in like the SDK where you can say, like, Yeah, here's this view, and these, you know, metrics change them to a No. OP. Essentially, you know, no aggregation so like that's possible. Whether we want to plumb that into some sort of like static configuration. That's kind of up to us on that one. Yeah.
like, it's harder cause, like.
like, we could also take a look at what Java does like Java auto instrumentation, because they, I think, have this sort of control as well. So it might be worth trying to synchronize on that one. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:07 Can investigate that. Okay, so Java.
okay, yeah, we can follow. I figured, yeah, okay.
**Tyler Yahn** 38:16 Because I know they also have, like an on off switch for this sort of thing, and I think they are specific on, you know different portions of the code, and that kind of thing. I don't think like it also is not a multi process instrumentation. But I may be wrong on that. I mean, I think it's just one Jvm.
That they're instruments.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:33 What tab.
**Tyler Yahn** 38:34 Time. So yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:35 But maybe we can put it under the discovery section. So when they go specify, I want this services, whatever you can define rules for that. And if you want a specific application in there, well added specifically as another rule, and then describe what you want for that one.
Yeah, I think that's that's a great idea.
This will help alleviate a lot of the the feature requests we've had in the past. I want to do this, but I don't want to do that. So
sort of in hindsight. We should have always done this, but then.
**Tyler Yahn** 39:11 This is.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:12 Development, yeah, exactly.
**Tyler Yahn** 39:14 Yeah, I don't.
Don't. Don't build something till somebody asks for it. Right? Like, exactly. I think you're
start to see it. Yeah. So yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:21 Okay, I'll open an issue to track that work, maybe as a sort of an epic and kind of write down some of these ideas. I really like. The the I think the next ask is, gonna be the tracing sampling.
I'm glad you brought that up. Because, yeah, yeah.
**Tyler Yahn** 39:38 That's you. That's usually where it goes. It goes on off. And then it goes. Wait, I just want like 10% here instead of 100.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:43 Yeah.
**Tyler Yahn** 39:43 Yeah. So yeah, yeah, well, cool. Yeah, that's a great great feature. I really like it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:50 Okay.
**Tyler Yahn** 39:52 Any other topics. People wanted to bring up cool ideas they've been playing around with.
Well, if not, no worries. There's a lot of stuff to do definitely getting back from vacation points. That out there's just endless amount of notifications. Yeah, so okay, we can end it here. Everybody can go back to chugging away at the code. Appreciate everyone for joining good, seeing you all again.
Yeah, and thanks for thanks for all the hard work. I'll see you all in a week's time, or Asic.
**MM Mario Macias** 40:27 Hey? Thank you. Tyler.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 40:29 Bye.
**MM Mario Macias** 40:30 Bye-bye.
