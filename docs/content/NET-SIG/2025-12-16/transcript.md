SIG: .NET SIG
Date: 2025-12-16
Duration: 40 minutes
Zoom Recording URL: https://zoom.us/rec/share/KCExcArXYIBKZ1M7w4zr49v_w3u2Z3oY727EPn4Tc772fq8B9ucHX3QxyCo7bGDc._ocXlHhyxS4_27JT
============================================================

## Zoom Recording Transcript

**Alan West** 02:37 Hey, Martin.
**Martin Costello** 02:39 Hey, how's it going?
**Alan West** 02:41 Not too bad. How are you?
**Martin Costello** 02:44 Not bad. The last week of the year.
But for work, at least.
**Alan West** 02:50 Yeah, you taking the rest of the year off after… after this?
**Martin Costello** 02:53 Yeah, from Friday, got, a bunch of holiday to use up that I can't carry over, so…
**Alan West** 03:01 Nice.
How does vacation work there at Girvana? Is it,
Do you just get, like, an allotted…
Number of weeks or something, or…
**Martin Costello** 03:14 Yeah, we get, 30 days a year, but I only joined in May, so mine's prorated, but
you could… you can carry 5 days over to the next calendar year, but otherwise you have to use it, and I've got more than 5, so…
**Alan West** 03:30 Cool.
30 days? That's… That's pretty… That's more than… I've heard before.
**Martin Costello** 03:39 Yeah, it's more than I had at my old job.
**Alan West** 03:42 Yeah.
Technically, New Relic is… Unlimited?
**Martin Costello** 03:50 With the gay quotes.
**Alan West** 03:52 Yeah, in air quotes, exactly.
And I… I don't think I've used 30 days.
I don't even know. Maybe I, maybe I'm close. I mean, I took a lot of November off, so that would have been, like…
You know?
Maybe 15 days or something like that.
**Martin Costello** 04:11 Oh, there's quite a lot in one go.
**Alan West** 04:15 Yeah, yeah.
Cool.
Hey, Matthew.
I guess we can… Start talking about stuff.
Hmm… I think there was actually a few things to talk about.
Let me kinda… Collect… some things… yeah, I can share my screen.
And kind of collect a few things to discuss, and then maybe we can just kind of go one by one.
There's this bug, I've been seeing some chatter this morning on…
This, so we should probably talk about… What we're gonna do… Here…
And… Also… I just wanted to chat briefly. Sounds like Steve is gonna do some work on…
Some stuff here, but I just wanted to chat briefly about the database stuff.
And then… Peter, pinged us about this, to chat about this again.
And I haven't really given it any thought, but maybe we can… Come to that.
Are there anything on either of your guys' thoughts or minds?
**Martin Costello** 06:09 Nothing for me.
**Alan West** 06:11 Okay.
**Matthew Hensley** 06:14 Nope, I'm all good.
**Alan West** 06:18 Hmm… So yeah, that's… What was this? Oh, yeah, yeah, okay. So, we got a null reference exception.
Sounds like you fixed it, I haven't really reviewed the PR, but… Her yet, but…
Seems like it's got approvals. I think the conversation, from what I can gather, is… Should we…
Should we do a release?
And… what should it be versioned?
**Martin Costello** 06:48 I think.
like, I… for me, it makes sense, if it's a bug fix, it's a patch, but then Peter's pointing out
the build pipelining changes and some other stuff. But also, you could argue that it's been out for a month, and I think Raj only found the bug because he was doing the other PR he just opened.
**Alan West** 07:11 So, no user has noticed the problem.
**Martin Costello** 07:16 So it doesn't necessarily need to be rushed out as a patch.
**Alan West** 07:25 And so the point you're making is that since it doesn't need to be rushed out necessarily, maybe it's worth…
Taking a little bit more time and reconsidering
Our build, pipeline to see if we want to change.
Anything.
**Martin Costello** 07:38 Possibly. I think also I kind of see where Pieta's coming from, which is there's some other changes in the pipeline that are minor, so you could just do 115 and release everything that's currently in the pipeline.
But then that probably gets you into a conversation, which is like, Raj has just opened a PR to add something, then he'd probably be like, well, I want that to be in 115 too, and then the conversation goes background in a loop.
**Alan West** 08:08 Yeah, totally.
yeah, we've had a lot of conversations about our versioning over the years, and
you know, on the one hand, like, I kind of lean towards, what you just said, right? There's a bug, so…
by semantic versioning, then you would just release a patch. So 114.1 would be…
The correct thing to do if… if we were…
Following semantic, aversioning to the T.
But then… but then, you know, it… it… things kind of… even if we agreed to that, things kind of get funky, because…
When we want to do, like, an actual feature release, right? Like, if there was only features added to the OTLP exporter.
Would we… would we want to just, like, change our stance to be absolutely true to semantic versioning, and…
And if…
only a feature was added to the exporter, then just bump that to 1.15 and leave everything else at 1.14, and then everything would eventually just kind of, like, diverge from a minor AND patch.
**Martin Costello** 09:28 Yeah, I… yeah, I think… I think it would be too complicated to treat every individual package as its own Senva island.
But I think just with respect to this specific bug.
In an ideal world, I'd just take that one change and go, there's 14.1.
**Alan West** 09:46 Yeah.
Yeah, so it's kind of like a… it's kind of like a…
A middle ground between staying true to semantic versioning and, basically just treating bugs as…
An acceptable place where we diverge, between packages.
**Martin Costello** 10:05 I think the other complicating factor is, as Peter says, there's already non-patch changes in main.
So, if you did want to do a bug fix, you've already got to do patching and manual stuff.
**Alan West** 10:21 It's just for the… just for the hotel exporter.
**Martin Costello** 10:24 Yeah, so then that's why I was sort of leaning to, well, if we've only found this because Raj happened to notice it, rather than a user found it and reported it, then that doesn't necessarily mean that suddenly brings a release timeline up.
Because, the fix that broke this…
That was sat in main for, like, a month or two before users actually got it, because it got tied to the .NET 10 support release.
**Alan West** 10:55 Oh, the bug was introduced at that point?
**Martin Costello** 10:58 Yeah, because, Ra… in the issue, Raj tracked it back to… it was a regression for when I fixed that issue that was causing the collector incompatibility.
**Alan West** 11:09 Okay.
**Martin Costello** 11:09 But once that went in, it was then in Maine for, like, a month before we actually shipped the fix.
And that one had actually had users reporting the problem.
**Alan West** 11:20 But we didn't release it immediately, we just rolled it into whatever the next scheduled release was.
**Martin Costello** 11:26 So you could kind of argue, if it's just Raj finding it, then it's not a user issue, so then if you equated the original bug versus this bug caused by that bug, this one's less important.
**Alan West** 11:41 Did you see what I mean? Yep, nope, I agree. I agree with what you're saying. Yeah, I don't… I…
I agree. I don't think that there's a reason to rush this, fix out, and…
You know, honestly, I haven't been paying super close attention to see, like, what else we haven't released. I mean, obviously, there's, like, for hotel exporter stuff, there's, like, the…
There's the, MTLS… Settings, which would be cool to release soon.
**Martin Costello** 12:17 There's also some stuff Pyotr did for the schema URLs.
But I don't know.
**Alan West** 12:22 Wales, though.
**Martin Costello** 12:23 is in there.
**Alan West** 12:24 Cool, yeah, then there's… that probably spans some other packages as well, no?
**Martin Costello** 12:33 Yes, I think, yeah, I think it's at least the console and the OTLP exporter.
And then… and then I think there's also an internal change in one of the other packages. It's, like, not user-facing, but it's to do with the schema URLs.
**Alan West** 12:48 Yeah.
Yeah, and for that reason, I think,
Yeah, I'd agree with, Peter's, Conclusion here that at 1.15,
is probably the next step. I mean, it makes the most sense.
I'll thumbs up at 2.
So yeah, I'll write out some notes in the, in the, in the meeting notes.
Oh, and I guess, comment on the issue as well.
Just that that's how we feel.
Generally speaking, you know, this PR aside, I… I personally would like to… leave.
the door open for doing something like this in the future, you know, whatever that would require, build pipeline-wise, you know, or change to our policy, or whatever. I think that that's a sensible thing to…
consider as a tool in our tool belt for, you know, when we need to maybe do something more quickly.
**Martin Costello** 14:01 Yeah, that makes sense, like, you know, because there was, like, there was that DDoS issue back in March.
That needed to be reverted, so yeah, someone reports a security issue in 10 minutes.
and suddenly it needs patching before Christmas, then we'd have exactly the same question, and we wouldn't know what the answer was either.
**Alan West** 14:23 Yeah, so I think it makes sense to, you know, expand the conversation and maybe change our policy.
Beyond just this PR. So I'll write up some notes about that, too. It sounds like you and I are kind of, like, on the same page.
And it also kind of sounds like that's what,
Miraj is beginning to advocate for as well.
One just kind of, like, even a more radical thought,
You know, it's funny, there's… there's just, honestly, there's not a lot of packages.
And sometimes I get this thought that, like, why don't we just have one?
I mean, none of these, none of these, none of these code bases are all that…
Significantly… it's not very large.
And if they were just all rolled into, like, one SDK package… I mean, I guess we'd have an API package, that would be separate.
But then all the, like, SDK components, which would be pretty much…
All of these, some of which, you know, are basically
deprecated, or getting rid of. And so it gets you… the list gets even smaller.
I guess we'd probably keep these separate, because they're kind of experimental things, or not stable, I guess.
But, like, anything that's stable, I have thought, like.
any of these exporters, all these exporters are stable, it just… it just almost makes sense to me to just have one SDK package. And then that actually brings us, you know, it gets to the point where we can actually be true to semantic versioning, right?
**Martin Costello** 16:10 Hmm.
**Alan West** 16:11 And not have, like, you know, this, like, dance around, like,
Well, we want to lock… we want these packages to be in lockstep, or whatever.
Anyways, I was thinking about sharing that thought as well. I don't… I'm not strongly attached to it, but just looking at the… looking at the number of packages here, I just feel like…
It might be a nice simplification to our lives.
**Martin Costello** 16:41 I could, I could see the user.
besides breaking changes, I could see the user pushback maybe being a bit, like, it's not pay-per-play.
And you just had to take all of it, and it might make it a bit,
more difficult to, like, ensure things like native AoT and things like that.
Because we… unless you were very strict with, like, how you…
made sure it was all annotated for bits that weren't, because I don't know which of these packages, if any, aren't AOT compatible, but some of them will be, for sure. So then if you had one, the whole package would have to be.
**Alan West** 17:22 Yeah, interesting. Yeah, I don't… I… we did a bunch of AOT work
A while back, and,
I wasn't super involved in it, but I was under the impression that we were…
And a pretty good footing on that.
**Martin Costello** 17:38 Oh, I guess what I mean is more like, if there's, like, a package that's there now that doesn't need native AoT, you can just say it doesn't work with native AoT and not touch the code.
Whereas if you crammed it all into one.
and some of it needs to be native AoT compatible, then the assembly needs to be, and then suddenly everything in it that isn't, now you have to explicitly go through it all and go, but not this bit, and not this bit, and not that bit. And then… and then sort of…
The net… the net effect to the user is the same, but then there's a big chunk of engineering effort to go through all the code and say what is and isn't shh.
native AMD compatible, whereas with them in separate packages, you can kind of just sort of, like, dodge some of them under the carpet and go, but yeah, but not…
**Alan West** 18:28 Hmm.
Yeah, so there may be AOT concerns,
You also mentioned breaking change. I think…
I think you can forward types to, like, a new package without… Yeah, forward type's one of those things that…
**Martin Costello** 18:44 I've never myself used.
So I'm vaguely aware of it, but I've never actually had to use it, so whether
Whether it would be done properly, or spot any problems with it, would be a whole different thing.
**Alan West** 18:56 Yeah, sure, and to be fair, I have not done it myself either, but…
Yeah, that was basically in the back of my mind, like, you know, to avoid a breaking change.
Anyways, again, not attached to that idea, but just maybe another option to…
You know, consider as we.
As we talk about this more generally.
Okay, well, I'll comment on that issue, and it seems… it seems like pushing out 115 is,
Is the most sensible thing, and we can do that.
**Martin Costello** 19:35 I guess that'll… actually, no, because it's Contrib, not this repo. I was gonna say that would probably tie in with, in the new year, doing the database stability as well.
**Alan West** 19:47 Sure, I mean, we could probably… yeah, they're separate, but we could probably wait until the new year.
To do… all of it, anyways.
So, we're pretty good there.
I haven't looked at any of these other PRs, but they look, small. Some of them are in draft. I think we're…
Oh, oh, this is the other one that I want to talk about, actually,
There's been some conversation about this, max retry.
I don't know if you've spent much time on this one, but this is definitely something that we,
Back in the day, when retry…
I actually did the original retry implementation, or at least I, like.
sketched it out, I wrote code, sketched it out, and then…
someone on Raj's team, ultimately picked up the work.
But it was… This… this whole thing about the…
I haven't read this most recent comment, but…
I… when I… when I originally sketched it out, I…
Had it on my mind that, like, a max retry attempt would probably be a good idea.
So in a lot of ways, I agree, with… with these… and I'm actually the one that put the to-do in the code, unfortunately. I try to refrain from to-dos now.
But…
Because the specification doesn't,
have something like this, and it seems like languages have begun to basically diverge in their interpretations of the spec, and…
add different things, like, you know, Java has a… basically has this, max retry attempts.
Sounds like Go does something different, I've not really looked at Go to really understand exactly what…
They mean by time-based here, but…
I think… what I'm gonna suggest here…
Actually, it doesn't… do you know offhand? Is our retry still, under a feature flag?
**Martin Costello** 22:22 I don't, I don't actually know, I haven't dug into it.
**Alan West** 22:26 Think it is…
**Martin Costello** 22:31 I think, from what I remember of last time I looked at the issue, because it seems at the moment it's sort of going around in circles near the end, but, it makes sense to me that
we should ignore any other SDK and just do what the spec says we should do.
**Alan West** 22:50 Yeah, and that was my… that was my original premise with… with basically sketching out this work. That's why I didn't land a max retry limit, because…
I, I wanted, I wanted the spec to…
either become clear on it or, or not. And… Cheers.
**Martin Costello** 23:13 Because I think, functionally, like, as long as there's a cut-off point of some description, I think that's fine. Yeah, we wouldn't want… I don't think we'd want it going forever.
But if there's a time-based deadline on it, then… That's good enough.
**Alan West** 23:30 Oh, you're speaking to the timeout.
**Martin Costello** 23:32 Yeah, yeah, I think as long as the code isn't looping forever.
In… for a lack of this setting.
Then… then it's… it's fine.
as it is, it's not a bug, as I think it was… you said.
**Alan West** 23:49 Yeah, it's… it was by design, essentially.
But the one question, because I've not thought about this for so long.
The one question I had, is…
What happens if you set the timeout to…
like a negative number, or zero, or something. Is there a way to set the exporter, basically, to have an infinite timeout?
And if so, you know, is that, like, a foot gun that is… You know, maybe.
**Martin Costello** 24:21 It's technically not a bug, but it kind of almost kind of feels like a bug.
I have conflicting opinions on that, because…
Polly lets you do that. I don't think it's a good idea, but it is a feature Poly has had forever, and I think it's just…
Lazy people's way of just keep trying until it works.
I don't… I don't want to say… tell you to do it 20 times, and then it would have succeeded on the 21st, but because I didn't say 21, it failed.
But yeah, I think it… I would think of it more of, like, will we let you shoot yourself in the foot if you really want to?
**Alan West** 25:04 Yeah, totally. And if it… if…
If that's true, if we… I wasn't… I looked at the code briefly, but I wasn't able to answer the question very quickly, so… but if it's true that we allow, basically, some infinite timeout…
It's probably at least worthy of putting in, like, The documentation, you know?
**Martin Costello** 25:30 Oh yeah, that, yeah. You can do this, we don't recommend it, but it is possible.
**Alan West** 25:35 Right, right, right.
I think that would be a reasonable, middle ground,
Anyways, I will respond to this guy again, but it…
You're… it sounds like you two are generally of the opinion that if…
This really needs to be driven through the spec if it's gonna be a thing.
**Martin Costello** 26:02 Yeah.
**Alan West** 26:03 Yeah.
**Martin Costello** 26:04 Yeah, because otherwise, we're just… Making the divergence worse.
**Alan West** 26:13 Right.
It's funny, I talked about this, about OTLP retry, a lot with Jack, who is, you know, your new co-worker. Oh, okay. Because he and I basically both implemented retry at the same time, him and Java, and me and Donnet.
And so we talked about it a lot back in the day, and he…
he introduced this, it wasn't a total, like, thing that he just invented. The funny thing is, is that,
GRPC has its… Own specification. I don't know if I'm gonna be able to find it,
Very easily, but there's,
I don't know if this is it, but there's, there's actually, like, a specification dock somewhere.
For any GRPC client.
And… It's… it's supposed to follow.
In any case, I'm not gonna try to find it right now, but…
It essentially… it essentially describes just… just this. It's… it's got, like, a…
Did your PC clients have, like, some sort of a retry policy?
And so Jack was very much inspired by that, and just basically, like, implemented that, of course, for the gRPC exporter, but then took all of those concepts and just, like, made it also work for the HTTP exporter with all the same…
kind of options. And of course, the gRPC exporter was really, like, easy to implement because the…
it basically just leveraged the underlying gRPC client's retry policy.
And he basically just kind of, like, you know, surfaced that up to the,
as a first-class thing in the OTLP.
Exporters configuration.
And in that way, you know, like, I actually think… I think what he did was a relatively reasonable thing. It's just unfortunate that it didn't, become, like, the thing that was codified in the specification.
Because the, because the hotel specification
I've not looked at this for a while either, but it is… It is very anemic.
Where would that be? It's probably in the exporter spec.
Yeah, I think, I think I even, like, changed some of the wording here way back when.
Just to clarify some things, but…
You know, basically, it's just like, there must be a retry strategy.
And then, oddly, you know, it goes into a little bit of implementation, like wording here.
In that it must have an exponential backoff with jitter, But besides that, it's like…
go with God. Go figure it out. There are… there are… so it does go a little bit more. There are status codes that the protocol spec declares as retryable or not, but, like, that's basically where it… it ends.
There's no… there's no…
There's no specification around, like, how to configure this thing, if it is… if it even is configurable.
**Martin Costello** 29:44 how you would do the jitter, etc. It's just sort of like, here's a concept, off you go.
**Alan West** 29:51 Yeah, exactly, exactly. And so the jitter that… I actually,
when I implemented the exponential backoff with Jitter, I…
ripped off the code from .NET's gRPC client. So it has the exact same algorithm.
as… as the… as the gRPC.net.
Client for this, so… But…
that was, you know, the .NET client? I don't know, like, you know, other language SDKs might, you know, try to make up their own thing here, because, again, not specified, so go with God.
Anyways… I'll probably comment again on this issue, but that,
I would love to see the specification get a little bit more opinionated on this. It's probably going to be really hard now, though, because languages have basically just done their own things, and…
It would be breaking… breaking for them to change.
In any case.
So… yeah, I think everybody's approved this. I agree with Peter, I think that,
I think we should hold on doing the release candidate.
on… on Steve's work. I don't know if he's…
**Martin Costello** 31:31 I haven't seen anything on it yet, but yeah, he's said he's gonna work on it soon.
**Alan West** 31:36 Yeah.
Yeah, I'll probably just, like, hang tight on… and see what he comes up with there.
If he gets something… done, or PR Open, soonish, I would consider…
doing the release candidate, you know, in the coming week or two, just to get… just to get the release candidate kind of, like, out there and sitting so that people can begin to, you know, pick it up in January and…
And so on. But, anyways…
So I'll hold on to release Canada, at least for now. I… I agree with them.
I agree with, Peter.
Any additional thoughts on there, on that?
**Martin Costello** 32:28 Not from me, no.
**Alan West** 32:31 Okay.
Cool.
And then what was this one? Oh, yeah, yeah, yeah.
He pinged us about this on Slack.
We talked about this.
A little while back.
I don't know if there's…
Doesn't look like there's any new conversation, it just looks like it's just been in limbo, basically.
**Martin Costello** 33:05 Yeah, I don't recall we really talked about it after the last discussion.
about it.
Which I've forgotten most of.
**Alan West** 33:16 Yeah, yeah, it's… it's just kind of a wonky thing. Like, we introduced this thing a long time ago in the SDK,
It's… it's a super useful
feature, but it's… it's not part of the specification.
So, you know, whatever, our bad there for releasing a stable in the SDK, but… That happened years ago.
But the funky thing is, is that instrumentation isn't supposed to take a dependency on the SDK. It should only need to take a dependency on the API, so…
You know, it's always been this weird thing, it's like, our API is technically Diagnostic source, so, like, really, it would be…
probably the coolest if, the .NET team actually Implemented this somehow, but…
They're not gonna do that unless there's a specification or there's a, like, a strong need, so…
That's why we've not really pushed,
On that idea, to propose something to… to .NET itself.
Anyways, I'll respond to Peter. I don't have any, like, new thoughts on this necessarily offhand, so…
We don't need to…
Circle on it right now.
Anyways, that's what I had today.
Anything else from either of you?
**Martin Costello** 34:57 The only thing I'll mention, it's in draft at the moment, mainly because it doesn't build until the other bug fix is merged, but, I'd had a thought recently,
there was an issue that I opened, and then I closed it, because I looked into it, and I think there was something in the .NET 10 release notes about how the JIT was getting better
Doing bounds checks, so you didn't need to have unsafe code.
necessarily, and there's a bit of the… some… there's a bit in the OTLP exporter that does, like.
there's a comment somewhere, and it says, let's avoid boundaries checks here and do unsafe to make it faster. And I equipped to see if I could make it faster, and whatever they've done in .NET didn't make a difference to the code when I did some benchmarks, I put it back.
But then I thought it might be a good idea to… Add some fuzz tests.
For that stuff.
So…
**Alan West** 35:55 What's this one?
**Martin Costello** 35:55 By a coincidence, I started this yesterday, just before Raj opened
The issue saying there was a bug.
in the, the metric serializer. That was my fault.
So…
I tidied up the PR and opened that this morning, and then I tweaked it so it finds that bug.
So, this PR's broken because of the plug, and then once the other PR's merged, I'll rebase this, and then…
In the short term, I think this is just a good… Like, a bit of breadth.
Over the serializer stuff.
But then we could potentially use it
to extend it to other things that it might be useful for over time. But, the bit I wasn't sure on is, like, are they just more tests, so they go in the test project, or is it its own type of thing? So, for now, I've put it in its own project that's just for fuzzing.
And, this will also make scorecard happy… OSS… OSSF Schoolcard happy at a point in the future, because it doesn't currently understand FSCheck.
as a .NET fuzzer, but I added support for that last week, but they haven't released the change yet.
**Alan West** 37:10 Oh, cool.
Yeah, I've never used FSCheck.
**Martin Costello** 37:18 I've only used it a little bit. It's similar to a similar JavaScript library that I've used before, and it's a lot more user-friendly than something like AFL fuzz or LibFuzz.
Because it fits into your test framework, and you just write some tests, and the smarts, is it going off and generating ridiculous values for you automatically, and doing the randomization? Whereas libfuzz is, like, you have to run it on Linux, and it does loads of crazy stuff with Bang, and…
stuff, and it's just very slow, and maybe a bit OTT, if you're not actually doing native code.
So this is sort of a… I think this is a bit of a nice middle ground that makes things like, do you do fuzz testing happy?
while still feeding, like.NET.
**Alan West** 38:14 Cool.
Yeah, I like it. Yeah, it does kind of feel like a, like a separate…
Kind of testing, so… Separate package.
**Martin Costello** 38:25 Plus, I was lazy, and I got Copilot to write most…
Well, at least the first pass. I said, Copilot, write me some fuzz tests, and then I went through it and made it slightly more sane.
**Alan West** 38:37 That's really cool, you know, yeah, I've not… I just started playing around a little bit, not with Copilot, but I was…
New Relic has basically adopted Clawed.
**Martin Costello** 38:48 Right.
**Alan West** 38:48 And so I've been… I used Cloud a little bit to… New Relic's primarily a Java shop.
And, you know, I mean, I can read Java, and I can kind of write it, but I'm not really a Java guy.
So I needed to prototype something for a team, and I had Claude basically do most of the scaffolding work for me, and get, you know, get all the bits in place. I was pretty impressed.
**Martin Costello** 39:15 Yeah, it did a pretty good job, especially as well, because fuzz testing is just more, does it not explode?
**Alan West** 39:23 Right. So you don't have… you don't… it doesn't need to be as good at…
**Martin Costello** 39:28 getting all the nuance of what the assertions on how it should behave should be. It's just, if I give it garbage, does it beha… does it either not fail, or does it fail in a controlled way? And if it doesn't, then the test fails.
**Alan West** 39:46 Yeah, cool, cool.
Alright, yeah, I'll take a… take a look over this.
Seems pretty neat.
Other than that… I guess have a good holiday.
**Martin Costello** 40:03 Yep, you too, Alan.
I saw the ban… I saw the banner in New York.
Oh, it's on your screen as well, yeah, they put their.
**Alan West** 40:09 Oh, yeah, yeah, yeah.
**Martin Costello** 40:10 At the meeting moratorium.
**Alan West** 40:13 Yeah, and I think it's already been removed from the calendar.
Yeah, cool. Well then, yeah. I'll see y'all next year, I guess.
**Martin Costello** 40:22 Yep. Happy New Year, see you in 2036.
**Alan West** 40:25 You too. Talk to you soon.
**Matthew Hensley** 40:27 Phew.
