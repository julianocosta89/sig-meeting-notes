SIG: Configuration WG
Date: 2025-07-21
Duration: 11 minutes
Zoom Recording URL: https://zoom.us/rec/share/THNsMjdn8aZ1nizc3kWgSy-uiOf71HLswG0yklesQlCozA_pC3orbS7_sKE2n35L.5hPlBdBCN0ZExoyy
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:59 Hey, Daniel.
**Dan Gomez Blanco** 01:02 Hello!
**Tyler Yahn** 01:03 How's it going.
**Dan Gomez Blanco** 01:04 It gets.
I wasn't sure if Jack or
Alex will be joining, just checking there.
**Tyler Yahn** 01:16 Yeah, I don't think they will. I I know Jack is out on paternity leave, and then I haven't seen Alex in a few weeks. I think he's also on some sort of leave.
But I don't know the specifics.
**Dan Gomez Blanco** 01:34 Summer holidays, I guess, as well.
**Tyler Yahn** 01:36 Yeah, that. That's a good guess. Actually, yeah.
Did you have a question for him?
**Dan Gomez Blanco** 01:45 No, no, I just join as a
just in case, you know, like as Gc. Liaison, just in case there's something to to
to escalate, or, you know, see how things are going in general.
**Tyler Yahn** 01:59 Yeah, I mean, obviously, like, the stabilization process is kind of top of mind. For I think this group it's going pretty slow. I think that there's a lot of
maybe not a lot. There's, I think the Gosig has asked to just maybe pause while we evaluate it.
And so that kind of put a lot of pressure on us to get it done, and it's going slow. I think people are kind of, you know, waiting through it again and making sure things are correct. But yeah, I think it's just a matter of, you know.
lack of activity for the summer. And then it's just yeah, trying to trying to get that done.
**Dan Gomez Blanco** 02:37 Cool.
Yeah, I saw the issue from Jack as well.
To track like implementation across languages.
**Tyler Yahn** 02:47 Right.
**Dan Gomez Blanco** 02:49 So. I guess. Would that would that be? Maybe that was. My only question is like, is that the best place to that issue that is on the board to go and track
**Tyler Yahn** 03:01 Beautiful Limitations.
**Dan Gomez Blanco** 03:02 Limitations. Yeah.
**Tyler Yahn** 03:03 Yeah, I think so. I think that's actually probably the most accurate. As far as I know.
you know, anybody who has tried to implement it has come here. So I'm pretty sure they're all tracked in that issue. So yeah, I'd say, that was, that's accurate.
Yeah.
**Dan Gomez Blanco** 03:19 Good stuff.
**Tyler Yahn** 03:22 Yeah, I was kind of expecting nobody to be here to be honest. But yeah, I'm glad to see you here. Yeah.
**Dan Gomez Blanco** 03:31 Just 1. 0, I know that we're here. I mean, I've got maybe another another tangential, maybe like a slightly related question. There's 1.
One thing that I've been trying to find time to do is like I've been trying to find time to write an Otep on controlling context propagation that's over the back of a
of a spec issue. That yeah, there was some sort of like agreement like.
and I say, controlling is like, you know you, you might have a subsystem, and then, or a service, basically, would you say I did this particular
origin onto this particular you know, server dot address. I don't want to propagate baggage. I think that the question came from baggage mostly that could contain, you know.
random, like potentially personal or like sensitive information in baggage. Right?
So you want to control when you propagate things or not. And I think the idea here was like someone was proposing changes to the propagators. Api.
And then we in that issue, we sort of like agreed that
that was not the right place to do it.
and then that it would be something more on the configuration of this is why I'm asking this on the configuration of
of
clients, for example, to propagate context or not. So when you've got a client that's instrumental with hotel, then
you should be able to control that.
And you know I'm now that made me think
I believe there was some config that was common, like a block that was common for other things, right, for example, and I think there's like
controlling. If you store like headers for
and in common. Http requests right? Which again, you know, can contain sensitive data. So by default, that is
not recorded, and that would be, I guess.
is that something that's already being used by any instrumentation libraries that you're aware of.
That type of.
Let me see if I can find it, because I think I remember seeing that in the config repo.
**Tyler Yahn** 05:44 Yeah, I know you're talking about. That's yeah. I mean. So I think I think it is. I think the Java team actually has been doing a lot more work on this. They would know more, for, like the interpretation side, this is also the side that isn't necessarily done.
But yeah, I I guess that's a good question, because it sounds like what you're describing, though, is something that's more aligned with, like the SDK, or, yeah, I guess the SDK,
which would would be more of a it wouldn't be in the instrumentation configuration at that point, because, like that'd be like a general configuration for instrumentation is what you're talking about. But the context propagation stuff like that, I think, is, I think, more core to the project right.
**Dan Gomez Blanco** 06:26 Yeah. But I guess what we talked about in in the issue, and I can probably I can try to find it.
was the fact that you know the propagators like the fact that, you know, propagators shouldn't be concerned about
all the other properties of the, so that might be in the context of like, we're trying to propagate context, too. So like, basically
the the being like them.
the responsibility of propagators. Just to be like, you know. Here's a carrier. Here's the content that you.
**Tyler Yahn** 07:00 Yeah, right? Right?
So what you're saying is is that like it should be in the instrumentation configuration, because it's only instrumentation that should be concerned about sending it.
**Dan Gomez Blanco** 07:09 Exactly. Yeah, I think. Well, I would appreciate any feedback on this as well. I think there was a comment. There.
I just put the link here in the in the chat.
But yeah, so that there were a couple of like.
So yeah, so there were a couple of comments that related to like
the way that people are already doing it, which is with some type of like
property that you put in context. And then you have a custom propagator, maybe, that you know that can read that from the context and then inject it or not.
But then, in a general way
the agreement there. I think I only got a like from Yuri as in like Tc.
I don't think that's a Tca approval, they say, but but yeah, I think it would be quite
a, I guess.
quite a big change for propagators to have, like some type of like standard way of defining
where you propagate to or not, but like
I think, instrumentations would be more. It's very, I guess, almost like tight
to the actual thing that you're propagating right.
**Tyler Yahn** 08:35 That makes sense. Yeah.
**Dan Gomez Blanco** 08:37 So it was like.
because you could take, for example, W. 3 C. Let's just think about like baggage like W. 3 C. Baggage.
and then, if you're if you're propagating over, I don't know. Like the messaging like Sqs propagator, right?
I you will define your
where you want to propagate or not in a different way. Then you would define it for
W. 3 C. Baggage to
an Http. On an Http. Client. Right? It would be the way that you, the way that you define the allowed
destination, or they allow us.
Yeah, let's say boundaries would be different. For for the same propagator, depending on the
instrumentation that is propagating it.
**Tyler Yahn** 09:29 Yeah, I mean, I think that makes sense. Yeah.
**Dan Gomez Blanco** 09:32 So, anyway. So I think the the reason I was asking here was that you know, if we if
someone is already using that type of I guess global config.
And when I say global, I mean, like Http config.
for example, right? That is like
as we've got now, Http instrumentations that say, well, you store the you capture the the headers or not.
and I wonder if and I haven't really put any thought into this. Apart from like, you know, basically thinking about that in that issue.
if it would make sense to have some type of like common
config for Http clients for this sort of thing.
**Tyler Yahn** 10:18 Yeah, I mean, we already have kind of this thing in a lot of languages where it's like, you don't accept like public
context, essentially like you drop public context and you start your own span right? And I think that that's configuration for a lot of well, I guess it's a higher level. But like.
yeah, I mean, I think this seems fair like it seems like it's it's something that would be related to this Http configuration in the instrumentation configuration. I know again, like the the Java folks have been messing around with this a lot. Bragger was asking about Http like method, adding that here last time. And so I definitely think it's not out of the question. It seems like it's a reasonable place for it to go.
**Dan Gomez Blanco** 11:01 Cool.
**Tyler Yahn** 11:03 Yeah.
**Dan Gomez Blanco** 11:04 I mean, I'm just always trying to find some time to work on these things, but
struggling. But we'll get there. No, that was that was useful.
**Tyler Yahn** 11:12 Thanks. Yeah. And like, I said, I think if you have a proof of concept asking Gregor, or if you're able to do it in the Java language. That's probably your best bet to get some feedback on this, because that is the group that's actively on developing this section of the config.
**Dan Gomez Blanco** 11:28 Cool. Yeah, I mean, that's that's the one that I'm
most familiar with in terms of SDK, as well.
**Tyler Yahn** 11:36 Well, perfect. That works out, yeah.
**Dan Gomez Blanco** 11:40 Good stuff, all right. I don't want to take more of your time. Then. Thanks for joining.
**Tyler Yahn** 11:44 Yeah, alright. I'll talk to you later. Bye.
**Dan Gomez Blanco** 11:46 See you bye.
