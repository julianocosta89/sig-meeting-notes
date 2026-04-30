SIG: Rust SIG
Date: 2026-04-29
Duration: 8 minutes
============================================================

## Zoom Recording Transcript

**Scott Gerring** 01:15 Hello.
**Björn Antonsson** 01:19 Hi there.
**Scott Gerring** 01:21 How's it going?
**Björn Antonsson** 01:25 Lots and lots happening, as usual. But anyway…
**Scott Gerring** 01:30 Anyway…
**Björn Antonsson** 01:31 Yeah, how are things on your end?
**Scott Gerring** 01:34 Good?
what's the word? Cognizant that the, these are automatically transcribed now, so I won't go into too much unnecessary detail, but no, it's been good. I was in Greece last week for a conference.
It was good fun. Off to London next week, talking to Java developers about Rust. This is something that I enjoy, it turns out.
**Björn Antonsson** 01:58 Do they enjoy it as well?
**Scott Gerring** 01:59 I think the ones that self-select to come to the talk about Rust for Java developers do.
But, probably the community at large is not such a fan of hearing all the rust hype sometimes, which I understand.
as an aside for this, the kind of, like, toy application I'm using for this talk… I built a imagery-serving thing, because this is something that I've done for a few previous jobs, like Google Maps backend style thing.
In both Java and Brass, and then I load-tested it very extensively, and Java does really, really well with the modern runtimes. Like, it's amazing how much performance this thing squeezes out of your machine.
**Björn Antonsson** 02:41 Yep.
**Scott Gerring** 02:43 I suppose you're unsurprised.
**Björn Antonsson** 02:48 If you don't do really… Bad things, I… I… I'm not surprised that it works well.
**Scott Gerring** 02:58 Yeah. I think once you start trying to squeeze it into small containers and constraining its RAM really aggressively, it gets much more.
**Björn Antonsson** 03:05 Oh, yeah.
**Scott Gerring** 03:05 It's rust, but .
**Björn Antonsson** 03:07 Java is sort of like… does not like you anymore.
**Scott Gerring** 03:12 Yeah.
This is a reasonable trade-off to make, generally, I think, for all of the convenience it gives you, and the ability to work at a very high level without thinking about… Kind of any of the underlying details of the machines you're on, really.
I think it might just be us. Should we, should we call it quits?
**Björn Antonsson** 03:39 Yeah, if it's only you and me, then… I don't know. So, what's their… I have not followed along when it comes to the discussion about… was the async runtime hiding thing?
**Scott Gerring** 03:55 So…
**Björn Antonsson** 03:56 Post.
I should review… take the time to review it.
**Scott Gerring** 04:01 Yeah, it's… I think the reason that it's sat around for a while is that… everyone realizes that it's important, because a bunch of stuff in the OTLP crate depends on it, and it's an unstable feature.
But everyone also realizes that it's super nuanced. Like, it's a pain to think about.
How we should stabilize it, and there are a couple of issues there, like how it can be generic across things that are no async and sync and rah-rah-rah.
Especially in the function signatures and, like, you know, single thread runtimes and whatnot, that are, like, actively a little bit broken at the moment. So I put up two… we've talked about this a little bit in the past, but I think at quite a high level. I put up two PRs that kind of, like.
One is a real soft touch, that's still enough to make it look stable, the other is a bit more ambitious, but I think there's a third option that I'm hoping to get some engagement thinking about.
Which is that, if you look at the processes at the moment.
there are both the ones that rest on top of the runtime abstraction and can work with async runtimes, essentially, and then there's the threaded ones. So, you know, you have a processor for logs, and you have a threaded processor for logs, but… the ones that are explicitly threaded are doing that within themselves. They're not… leveraging, kind of, like, an external mechanism to describe their threadedness, you know? It feels to me like you could just express everything against the runtime trait, and have a well-functional… no async or sync version of it, and save a bunch of code, but that is obviously a massive change, and I haven't thought about it very hard, but I'm hoping to provoke discussion, at least, or some thought around it, because there's just lots of duplication in the area at the moment, and maybe it's possible to do better.
But yeah, have a look, tell me what you think. It would be good to get the ball rolling. I think also, if I was, if I was CJO and the gang.
and I had a bit of a backlog, and I saw this one in front of me, I would know that it's gonna be a fair bit of effort to engage with.
**Björn Antonsson** 06:09 No.
**Scott Gerring** 06:10 In comparison to a bunch of the other stuff in the queue.
**Björn Antonsson** 06:16 Yeah.
I'll try to take a look. It's somewhat similar to the… things we're doing in Libdata Dark to break out.
Runtime traits, so we can… built for WASM and run things in… In Node, for example.
**Scott Gerring** 06:39 Oh, we wanna, we wanna target WASM now, for Lip Data Dog.
**Björn Antonsson** 06:43 For certain parts of it.
**Scott Gerring** 06:46 That'll be cool.
**Björn Antonsson** 06:48 Yep.
**Scott Gerring** 06:50 But not Diddy Trace RS, I think, because that rests on OpenTelemetry, and I don't think that in Noel Rust at the moment, we really play well with Wasm.
**Björn Antonsson** 06:58 I think there was some updates for something, some part of it, that can com… Biotism, I think? But, I mean, not the whole thing, and no.
So this is more for, like… Samplers and other things and encoders of the message format and things like that.
**Scott Gerring** 07:22 Things that are nicely stateless and don't need to impact the outside world.
**Björn Antonsson** 07:27 Yeah, but they have callbacks that use the node, it should be blank.
**Scott Gerring** 07:33 Oh, okay, yeah, that makes sense.
I'll just… I'll just simple functions that map from one, one, state to another.
**Björn Antonsson** 07:41 No.
But, yeah. No, I'll try to take a look.
**Scott Gerring** 07:47 Yeah, that'd be cool. I've spent a bunch of time recently burning through the issue backlog as well, and I've got a pretty good mental model of what's on the go as part of that, and I'm trying to get into the PRs a bit too now.
Just to really try and lower the burden on the project a bit and get things going.
**Björn Antonsson** 08:06 Yep.
**Scott Gerring** 08:09 But yeah, anyway, we've overloaded this meeting for, for data.
**Björn Antonsson** 08:13 Yeah, exactly. So…
**Scott Gerring** 08:18 Yeah, I'll talk to you soon.
**Björn Antonsson** 08:19 Yeah, see ya.
**Scott Gerring** 08:20 Have a nice evening. See you then.
**Björn Antonsson** 08:22 You too.
