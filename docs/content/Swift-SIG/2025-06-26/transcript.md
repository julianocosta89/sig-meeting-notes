SIG: Swift SIG
Date: 2025-06-26
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 02:11 Hello! Hello!
**Ariel Demarco** 02:16 Hello!
**Martin Holman** 02:23 Hello!
**Bryce Buchanan** 03:29 We'll give it a couple more minutes for people to filter in.
Alright. Let's get started.
So topics from last week, data, compression problems is anybody. Was anybody here last week that that's familiar with what this is.
**Ariel Demarco** 05:52 Yeah, I was, I was here.
So basically, there's there's a a user saying that there's another library called Data compression, and that makes complete conflicts in the Spm
whenever they are downloading that thing with spm and the open telemetry. SDK,
because we have a data compression target. What product.
If I remember correctly, the library, or the same as SDK, using a data compression dependency is launched directly.
so that generates a a problem that couldn't be resolved.
I think NATO is going to address that
if he didn't address it already, it's an issue on submitted
basically, we will create a branch
with the change, with with that change for for this user to use. But UN until 2 point O, this is difficult difficult to to actually fix, because we have to change the name of the data compression to be auto data, compression, or something like that.
**Bryce Buchanan** 07:02 Okay, fair enough makes sense.
so the cocoa pods are also still failing.
**Ariel Demarco** 07:17 Yeah, there's a there's another issue, though. I created an issue to actually
document what's happening, and also some easy way to
not wait until next release to actually fix those issues. So
I I submitted that issue. I I'm probably going to address that one.
**Bryce Buchanan** 07:41 Okay.
we can. We can do a release specifically to fix the issue as well. Don't you know, if you want to do that if that's necessary.
**Ariel Demarco** 07:50 Yeah, I don't think it's necessary. But basically, I would treat the Ci job so you can rerun it because there's a problem with synchronization
of the different bots.
Some pots depend on each other on others, but if, for example, the 3, rd the 3rd part sales, but nobody depends on that one.
the other should be pushed. Better that one, all of one pod just failed, instead of like all of them.
**Bryce Buchanan** 08:18 Right, right, right, right.
**Ariel Demarco** 08:20 But at the same time it will be good if we can rerun the push to bots whenever there's a release already done.
No.
**Bryce Buchanan** 08:28 Yeah, we could just break out that job or something.
**Ariel Demarco** 08:31 Yeah, yeah, yeah, exactly.
Probably do something like that.
**Bryce Buchanan** 08:39 Okay.
alright. So I guess let's go on to new topics.
Does anybody else have any topics? They want to add.
Alright, cool cause. I think we might. It seems like people are a little apprehensive to to review
the metrics. Pr, so I thought we could maybe go over it briefly here, just to give people some some, you know orientation to it. So last week I added a Pr to extend the span data to allow it to be
constructed publicly. But there's a little pushback on that. So I decided to go another route. However, I'm still running into issues where our span
our span implementation is a little bit lacking such as like the attributes are not accessible.
after a span starts. So if you have like, let's say filters or something in a span processor, you can't actually look at what this, what attributes the span has to make decisions about filtering
and there would. It would also be nice to be able to set attributes as well rather than having to do it one by one.
**Ariel Demarco** 10:17 But that means that the end wouldn't make
this. This is at the processor level, isn't it?
**Bryce Buchanan** 10:27 What's that?
**Ariel Demarco** 10:28 This is at the processor level you're talking, or at the.
**Bryce Buchanan** 10:31 So.
**Ariel Demarco** 10:31 Hello!
**Bryce Buchanan** 10:32 This would be at the processor level, so this could be during the this could be during the while on span start
while the span active. So my original implementation was just doing all this doing like filtering on and updating like attributes on span end, which isn't necessary. But when on the processor level, when on span ends gets called, the span is locked. So you're not allowed to update it anymore, even in the processor, which
it almost seems like it shouldn't be locked until after on span ends gets called. But you know, that's like a nitpick kind of thing I can work around that
But these missing attributes I was looking at other projects, and it like there is a way to get the attributes from a span in in most of them.
or at least in the android one and the and or Android and Java one, and that seems.
**Ariel Demarco** 11:38 That.
**Bryce Buchanan** 11:39 But it's okay to.
**Ariel Demarco** 11:40 If if we can, why, why wouldn't we be able to get them? Whenever the span ended? Because it's not public.
**Bryce Buchanan** 11:48 Yeah, it's it's not a public attribute or the it's not a public public member. So it's the you can. You can set attributes, but you're not allowed to look at what attributes have already been set.
**Ariel Demarco** 12:01 Oh!
**Bryce Buchanan** 12:01 Think you might be.
**Ariel Demarco** 12:02 I was exposed, it.
**Bryce Buchanan** 12:04 Yeah, yeah.
it. I think the the hitch is, is it just needs to be like a copied artifact
due to the due due to the all the
locks around updating the art or the attribute.
But that's an implementation detail.
but anyway, I'm gonna probably make a Pr to add that here in a minute, but it doesn't sound like there's any pushback against that.
Alright.
**Ariel Demarco** 12:43 Only thing to take into consideration is that.
considering now, attributes are going to be immutable.
and you will want to read of them. You'll have to take care about using it.
setting and accessing it in a safe manner. Threat, safe manner.
**Bryce Buchanan** 13:00 Yeah. Well, and and that's why I was saying it probably needs to be like a copied a copied dictionary, you know, that gets returned, rather than like a reference to the to the actual attributes. Because then you're kind of like taking it out of the the managed space with the locks and stuff, and then giving it in an unmanaged way. So.
**Ariel Demarco** 13:21 Yeah.
**Bryce Buchanan** 13:22 Yeah, it'll need to be avoided that will need to be avoided.
man, this this renovate thing is a little pushy.
Here we are
alright. So I don't know if anybody's actually looked at this metrics. Pr, yet. But basically the what it's doing in this one is
deleting all of the old metrics stuff. And I guess that's that's really it.
is that the right one? Still? Okay. There were a couple of
places where the old metrics were being referenced, such as, like all of these examples. So I've updated them to use the new metric, the stable metric
implementation. So after this one's merged, I'm gonna do another pass and remove all the references to stable, so it'll just be like Hotel Http metric exporter. It won't have stable on there anymore.
But that that that'll be in a in a subsequent Pr, yeah. So like Prometheus samples, this has all been updated to use the new stable stuff. There were a couple of other.
Yeah, most of it's just removal.
There was one other
kind of larger change. What is this? That's the Prometheus exporter, swift metrics. So these are kind of places to take a little bit more care. They all seem to be working fine in the tests. So
well, I also I also moved the stable metrics
into just the the metric or way one is
yeah into the into the root metrics folder. So I deleted the old metrics, moved the stable metrics into the root metrics folder, so that that created a little bit of noise, too. Maybe I should have not done that.
But the other.
**Ariel Demarco** 15:36 Well.
**Bryce Buchanan** 15:37 Yep.
**Ariel Demarco** 15:38 One question. Do you remember that there was an issue submitted around metrics
not being threat safe because of the in outs parameter.
On initializing the
I know. If it was the shared context, or something like that, we still have this in in this Pr.
**Bryce Buchanan** 15:57 Yeah, I haven't made any changes in that regard. I'm not. I'm not sure which one you're referring to. Maybe that was was that for the old metric.
**Ariel Demarco** 16:07 No. So there's a part that both the old and the new one has a uses the same. The same classes. I think that is the share context, metrics or context, or something like that? I I don't fully remember I was doing a fix for that. But maybe I will use your branch as a base instead of main.
Okay?
**Bryce Buchanan** 16:34 Oh, here, okay, I think it's up here. Actually, this is.
oh, that's kind of annoying.
I'm looking for the the persistent metrics processor. Okay, here it is. So this is, this is one of the
I guess it's not really a larger change. But this just actually adds, this is like a feature addition where it actually adds the persistent metric exporter for the stable metrics, which is something that we didn't have before.
So it required a bit of finagling in the stable metrics to add codable to a lot of
a lot of things.
So that that's kind of another
bit of noise in here if I can find yeah, like, exemplar data. Oh, that's interesting. Oh, that's
I guess there's just a lot of this sort of stuff like the the codable additions like in it, decode encode.
Oh, that's interesting.
No calls to throw functions occur within. Try.
Weird.
I guess this. That's not that needs to get fixed. That's not a trying doesn't need a try.
**Ariel Demarco** 18:12 Yeah, you'll need to try.
**Bryce Buchanan** 18:14 It just got on a try. A try roll
so that that's another place to take. A little bit of care is, but I've added tests for these encoders.
So yeah. And I had to add these like
these, yeah, just a lot of
a lot of encoding decoding stuff.
for special cases just due to
The like. All of these, all these data points were a little finicky because, they're referenced as like just a point data in in a lot of places like in in arrays and whatnot. So there, there's some
checks to get the right encoder running for those.
We're not exactly sure where those are at, though probably in the
probably in the persistent metric exporter.
I guess maybe not persistent exporter export.
Where is that referenced?
Well, I'm not sure where where that is. I feel like
there's more to it than than just that that should be showing up some somewhere else. But
but if that, I guess if that persistent stuff is a little bit too too hard to look at, with all these moving moving files
I can, I can put that out into a different, a different Pr, oh, here it is.
Oh, but this isn't a test.
Yeah, so here, this kind of this exercises, this should exercise. Oh, maybe not.
there were tested. Here we are.
The point data tests. Yeah. So here's where I test all the encoders and decoders for each of the different point. Datas. So. That should be pretty easy to review, despite the kind of large number of those changes.
But yeah, most of these, most of these, like diffs here, are are
kind of like. These are files that haven't been touched in a while. So there are some formatting fixes to them, using like the swift formatter which
didn't get didn't get hit when we added that.
Oh, so I'll take that.
Yeah, hopefully, hopefully, we can get that get that merged. So.
**Ariel Demarco** 22:08 Yeah, yeah, can you? Can you check one of the A metrics builder? Ck, like, I don't know double Gotcha.
**Bryce Buchanan** 22:17 What's nasty.
**Ariel Demarco** 22:18 Okay, or the double Godch builder, SDK, or
long gosh builder, SDK, one of those.
**Bryce Buchanan** 22:26 Well, what about it? Can I? What.
**Ariel Demarco** 22:28 Can you? Can you check? Can you check one? Some one of them in the VR.
**Bryce Buchanan** 22:34 What do you mean? Check one of them.
**Ariel Demarco** 22:38 They are under metrics. Table on on the old version, so probably
should be part of phase one.
**Bryce Buchanan** 22:51 Do you mean these ones here.
**Ariel Demarco** 22:55 The the ones inside SDK.
**Bryce Buchanan** 22:58 Oh, inside the sc.
**Ariel Demarco** 22:59 Double. Yeah.
Any appeals?
Oh, they got moved.
Yeah, probably 2.
**Bryce Buchanan** 23:09 Renamed, without changes.
**Ariel Demarco** 23:11 Okay.
yeah, because they are. They're no longer stable. It's like the only one. Okay, so I'll I'll probably use this as space here then.
Well, for I'll try to approve yours first, st or comment yours first, st and then do the fixes there.
**Bryce Buchanan** 23:30 Okay, yeah, they they're just they basically just moved up a
look up a up a
yeah, that that was like, one of the problems is
not all of the all the metric items had stable in the name of them. Just due to the fact that they didn't exist in the original
implementation.
So yeah, like, this one got got moved just up into this folder. The metrics folder where it used to be under stable. But now it's
Am I still in the Pr.
I still am in the Pr, yeah.
Yeah. So it just yeah, move. Well, it doesn't even can't even see it. All.
Yeah, moved from metrics, slash stable into just metrics.
Yeah.
Yeah. So most of most of these ones like are all just files getting moved.
and then the rest, save like.
Oh, yeah, like, here's a
just some like minor formatting stuff.
and then like redundant internal, that sort of thing. So there, there's not too much
to review in terms of like
actual changes other than those those things that I touched on.
Yeah, these are all just deletes, deletes, deletes, deletes.
Oh, it's this is why, get out of here, there we go.
Yeah. So there's just a lot of
a lot of stuff that is just removed.
That's interesting.
Curious.
I'll look at why, what is?
It's like the. It's just an empty file with that in it. That's interesting.
I'm not sure why that happened. But there, yeah, I can. I can double check some of these things.
Alright. But yeah, please take a look.
**Ariel Demarco** 26:18 I'll do.
**Bryce Buchanan** 26:21 Are there any other topics for today.
**Ariel Demarco** 26:31 That's fine. That's from my side.
**Bryce Buchanan** 26:33 Cool, alright. Thanks for joining everybody.
Have a good rest of your day.
