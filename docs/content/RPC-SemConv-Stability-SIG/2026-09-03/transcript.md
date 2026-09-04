SIG: RPC SemConv Stability SIG
Date: 2026-09-03
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Matt Hensley** 01:04 Hello.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 01:05 Hello.
**Liudmila Molkova** 01:15 Hi, sorry, I missed you for joining.
How are you?
**Matt Hensley** 01:27 Oh, I'm doing well. Currently in Vienna.
**Liudmila Molkova** 01:33 Oh, you're in Indiana? You're not that, like, in Vienna? Why?
**Matt Hensley** 01:37 I am in Vienna, I'm in Austria.
**Liudmila Molkova** 01:39 Oh!
And you're joining from Vienna. Oh my gosh.
**Matt Hensley** 01:44 Yay.
Grabbing her.
It's been a minute since we've had one of these, so I thought I'd come join.
**Liudmila Molkova** 01:51 Appreciate it, thank you.
How's Grafunding Fest going?
**Matt Hensley** 02:06 It's going good. Having… All hands. Off-site.
**Liudmila Molkova** 02:19 Yeah, I think Madhav is not joining today, because he is at a conference.
And he has a talk, so he's getting ready for it.
I think Trask will join at some point.
Maybe we can check what's going on here, what do we have in progress?
Oops, sorry.
So, Matt, I've seen you send the PR to use refinements.
Pretty awesome. I left some… comments.
to drop some… redundant stuff, I think most of it is coming from the Parent note.
**Matt Hensley** 03:13 Yeah, yeah, I, I'll… As soon as I get home, I'll… Get those results, thanks for… Taking a look.
like the V2 schema stuff, it's… It's a lot.
So, definite improvement.
**Liudmila Molkova** 03:30 Awesome.
Any, rough fetch cases you hit, any problems?
**Matt Hensley** 03:39 Nope.
not doing this, I mean, there's a lot of redundancy in the IDs and such, but it's kind of necessary.
**Liudmila Molkova** 03:49 You mean in… in the notes, or…
**Matt Hensley** 03:54 just play on, I'd have to… Actually… It's not in this one, but… I don't think.
Just in general, defining some things that's, It feels like you repeat yourself, even though you don't.
They just, you know, themselves end up looking very similar, even though they're different.
Almost the same content, but different purposes, so it's a little awkward, but it's definitely functional, and it makes sense once you… start using it. It just doesn't read super intuitively at first, but, you know, that's not a big deal.
**Liudmila Molkova** 04:31 Okay.
Cool, thanks. Then, this would add metrics for gRPC.
after you're done with this, I might convert the rest to V2 and add refinements, for other… for… Or maybe, Steve, would you be interested in documenting double metrics in a similar way?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 04:58 Okay, yeah.
Okay, yeah, I can, do something about it.
**Liudmila Molkova** 05:08 Yeah, and if you want to take a look at the PR and give it a review, it would also be great. So what it allows us to do is, like, this metric, we can document in YAML the flavor of it for gRPC for double, and whatnot.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 05:27 Okay.
**Liudmila Molkova** 05:28 And, like, we can customize the… Add the attributes, or customize the notes and everything.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 05:36 Okay, I will take a look later.
**Liudmila Molkova** 05:40 Yeah, thank you.
Grey.
Shiftan, I have a PR for the metadata, and I would love to… Now, what do you think?
So… We had this problem that the metadata Only describes one, thing on the request and response, and turns out that the requests Indeed have only the headers, but responses have headers and trailers.
And it… it is gRPC thing, but through gRPC, everybody else has it, so ConnectRPC has headers and trailers, and Triple has… others and trailers on the response.
From my research, the DAB2 doesn't have headers.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 06:47 Yeah.
That, doesn't have… Yeah, maybe I left a comment in the issue.
Yeah.
**Liudmila Molkova** 07:00 Oh, right.
Yeah, you'll have to comment in the doc, and yeah, we copied it here.
Oh, right, yeah.
And it seems… There is also… There are also technically requests.
for a double.
But because of the compat- oh, sorry, for triple, because of the compatibility with… gRPC, but they are not, like, exposed on the API surface, if I recall correctly, and then essentially they don't make sense.
But yeah, I've added the… Replaced the existing attributes, Wes… The Renew Friends, the request header.
It's pretty much the same, nothing interesting here.
Oh, there is an interesting part for all of them.
So, gRPC, and through gRPC, others support binary data.
And the proposal I have is to keep type a string.
I have strings, but binary… oh, sorry, base64 encode, binary data.
And in… GRPC is back.
they actually… have a convention that the things that are binary end with "-bin", and the API sometimes takes care of the type.
Where essentially, if we… if somebody… asks to record binary header, we would record it as Base64.
And by this convention, the… Consumer can… In most cases, see that if it ends with a dash been, then it's binary. So we don't even need to, like, record the fact that it was binary initially.
Okay, so then we get response header and response trailer.
And they are all up.
Then they require special configuration.
This is all the same.
And I think the only interesting place happens in the customizations.
Aww.
For example… Yeah, so I'm trying to… to the point of repetition, Matt, there's a lot of repetition between this node and the parent node, but I… Couldn't really find a good way… well, I found some way, but yeah, we'll see.
So, we… say how to record… when to record what for a Connect RPC?
So, it's kind of an interesting beast, because connector PC uses different protocols underneath, and what I'm saying here is to… the underlying protocol doesn't matter, what matters is the Connect RPC API, and they do have some guidance and different API for headers and trailers, so they kind of normalize different protocols.
And you can… Set them independently.
And… you… oh, the binary headers.
By the way, the VIN.
And they have an API for trailers that's separate.
And the tricky that the duplication avoidance part here is part of YAML syntax, so this is actually… it becomes a YAML variable that is used later on.
Literally, so… Whenever we need to reference it in the same file, we can reference it by reference.
Yeah.
And maybe… For gRPC, it's kind of easy. There are… there are APIs, and there is just one protocol.
I would need your help, Steve, to review the double.
If I missed anything.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 12:06 Okay.
Okay, I will take a look.
**Liudmila Molkova** 12:09 Yeah, thanks. So I've tried to divide it like this, and essentially for W2, I'm saying everywhere that it's not applicable.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 12:17 Okay, thank you.
**Liudmila Molkova** 12:20 Oops.
Oh, this is the… the tricky part.
Maybe… okay, maybe I messed it up.
So, this… the double also references the RPC response header.
Not just the trailer, but header.
because, technically, you can send them.
And… Wait.
Oh, I think this is my… sorry for my AI slob, this is total bullshit. So, it tells that you should not record response headers.
Should report them as trailers, I'll just drop it.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 13:21 Okay.
**Liudmila Molkova** 13:37 Okay, and then the rest is pretty trivial, nothing super… Special, but if you see any… Concerns, or anything you want to document more, let me know.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 13:51 Okay, thank you. Happy to.
**Liudmila Molkova** 13:58 Yeah, and I'm thinking about what to… do next, after I done… I'm done with it.
I'll probably start thinking about… this friend.
So… The… in streaming case, we can create a very long span.
And… I was thinking that maybe we don't need to, or, well, maybe we can do it by default, and probably should, but maybe we should allow… To disable it, and maybe we should define start and stop events instead.
And maybe we should report start event.
All the time, because by the time span ends.
It can take hours, and at least you can get the information that it started.
And maybe the severity is debug or something low enough.
So I'll probably propose, the configuration option to turn spans off.
And I would introduce a couple of events, and then the event would be, like, you either turn span on, or end event on? Not both.
**Matt Hensley** 15:30 Yeah, I think that makes sense.
**Liudmila Molkova** 15:39 Okay that…
**Matt Hensley** 15:42 I can already… I suspect someone's gonna immediately ask to be able to enable both.
**Liudmila Molkova** 15:51 Yeah, yeah, maybe, maybe they should have.
Maybe we don't even bother about the mutual, exclusion or… Like, if we just… Document the event.
And give them, whatever, info severity for streaming.
then… People can turn them off by just the login pipeline one.
**Matt Hensley** 16:31 Yeah, something like that maybe makes sense.
For some of these, there's… Some unexpected use cases when I start reading.
And it's… I haven't operated some of, like, a, you know, a really long one here, like, where it has a giant never-ending span.
But there's probably some operational issues that… But it makes sense where they actually do want both for some reason.
Nice.
Trying to understand a little bit more about streaming, but…
**Liudmila Molkova** 17:04 Yeah… Aaron, I wish we had some general rules for the… spans, right? You could probably make the same argument for any span, that you want a start event, but you want to know that the spend has started.
Period, because it can go long, your application may die midway.
And it's useful in general. And then we probably want a convention around how to record them in general way.
I'm a bit worried about… and then the end becomes the same problem, so you just say, okay, the end can be reported as this event, and then the SDK does the work, not the instrumentation.
I'm just thinking… How can we separate the… this stability of RPC from stability of such a thing.
In general.
Yeah, but I'll probably come up with some proposal, and I'll, yeah, I'll try not to have any relationship between spans and blogs, they can be… whatever.
**Matt Hensley** 18:26 Okay, yeah, do we… is there any cases today where, depending on what attributes you're using, it affects ability? Because we already have plenty of… I know we've done that just, like.
Attribute by attribute, you know, there's some that are not… stable, but I was just trying to think, like, basically, like, if you, you know.
Are using streaming, which would… be marked? Does that end up causing some of the other ones to, Like, would that be allowed? Makes sense.
While we figure out some of these issues around streaming, to go ahead and have… It's like, hey, if you're not streaming.
We're very sure about how to represent all of this.
**Liudmila Molkova** 19:14 Oh, I see. Yeah, and I think we wanted to do this, that, and we are doing this, that… Anything streaming is essentially a possibility.
I think we need to figure it out to the extent that Okay, we wouldn't block, The… we wouldn't need to do breaking changes after.
And introducing events, but unstable.
would validate this idea, right? So we would run it by then and other people who reported it.
We would get their… Arguments or feedback on… This approach, if they're happy with it, the events can become stable after, but the approach will stay. So, by default, we do create a span.
We have no way to tell how long the streaming will be, but you can turn it off if you don't like it, and even if you… Don't turn it off.
Well, there is little harm in endless span, as long as you know that it's happening.
It's just… I don't even know is the problem.
Okay, I'll put my thoughts on this one. I'll probably assign myself… And… Add it to to-do for now, maybe we'll move it to streaming.
And… I think what we'll have left is mostly around… Status cards… So we put the convention for canceled spends to post stability, and there is this friend.
Which is… Consolation?
Okay, so Dan is suggesting that we have a heuristic?
And the heuristic for… Whether it's its failure or not is that… It's streaming in BD streaming.
Oh, both.
**Matt Hensley** 22:17 Oh, AIC. This is no different than, like, H2P SSE stuff.
Where, just because it disconnects, like, it intentionally disconnects regularly.
As part of his polling.
Slash streaming cycle.
Smoke.
**Liudmila Molkova** 22:37 Yeah, for HTTP, though, we would end… before.
But the… We wouldn't wait until the stream ends.
For JPC, we would.
We are also having the same problem in, Gen AI in life, with The Voice, where you can talk to… A model, and it just understands your speech.
There, it's usually… you have a long-lived connection, and within this long-lived connection, you have a BD stream, and then you… the model sends you events, And there we decided… Yeah, very clean.
Oh, sorry, there we are not going, not going.
I'm going to kind of spend… used yet.
Dara, we kinda know it's going to be very long.
Oh, wait, this is not about spans, this is about the cancellations.
**Matt Hensley** 24:42 Yeah, this is, cancellations that aren't errors.
**Liudmila Molkova** 25:22 I think we can do two things. The first one is, semantic conventions can give the… Can hint instrumentations more, that if they have some means to know.
That's not a problem.
than… They don't have to record this failure, it's already the case, it's just maybe we need to emphasize it more.
So this person mentions that they can… Dig more into what her… what her real failure is.
Okay.
So, let's see… What?
People reply, if they reply anything.
But let's put it going to… To-do for now.
And maybe we'll… Decide to thump something.
Maybe we'll drop it.
Anyway, we are almost out of time.
Anything urgent they can help with?
Okay, then thank you for coming, and enjoy GrafanaCon.
Go find it fast, sorry!
**Matt Hensley** 28:29 Oh, no problem. It's… we just got dinner left, and then… I'm on a plane in, like, 12 hours, so…
**Liudmila Molkova** 28:38 Oh, okay.
If you see someone, someone I know, say hi to them.
**Matt Hensley** 28:44 Well, indeed, I just… left him to come join us. One quick thing, Obviously, we have still plenty of things going on here.
With gRPC and such.
How far out do we think we… Far from wanting to actually start.
Prototyping.
**Liudmila Molkova** 29:10 I mean, we can prototype. I have a prototype running prototype for Python. If you have some capacity to prototype this, go for it. I think we do. We did. For Java, we do have prototypes.
**Matt Hensley** 29:26 Okay, cool. I had started to, but then when it looked like we needed to make a lot of changes, I called off, so… Clear.
If it's not incredibly premature, I'm gonna go ahead and pick one of the .NET ones and… Clean up what's there already.
Get ready for metrics.
**Liudmila Molkova** 29:46 Yeah, thanks. I think it's, like… The only breaking change is the metadata that I see here, and maybe just minor tweaks to other stuff.
**Matt Hensley** 30:00 Okay, cool.
I just… I'd stop just in case we ended up… With some of the feedback we were getting, having to make major changes.
But it looks like, yeah, it's… Just some tweaks is not any… Thinking crazy luckily it turned out.
Lots of details to sort out, but… Nothing that… Yeah.
Alright, well, just catch y'all in, like, 2 weeks.
**Liudmila Molkova** 30:32 Yeah, see you in two weeks. Thank you for coming.
**Matt Hensley** 30:35 Yeah, no problems.
**Liudmila Molkova** 30:36 Yeah.
