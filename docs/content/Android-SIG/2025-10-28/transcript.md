SIG: Android SIG
Date: 2025-10-28
Duration: 35 minutes
Zoom Recording URL: https://zoom.us/rec/share/yJ2t-I-bbprSN0ufJ3Fu6SlBA9MYnp57m_7nrabQPiG3FdXY-N69lCWvn8isKGv0.MfLDuZkKEipfRR-S
============================================================

## Zoom Recording Transcript

**JP Jason Plumb** 01:33 Good morning.
Still getting set up here. Give it another minute.
There is currently no agenda.
Oh, did I get disconnected?
Wherever we go. Okay.
That was real weird.
**Cesar Munoz** 02:19 Halo.
Good morning.
**JP Jason Plumb** 02:22 Good morning.
I think that's who's here.
Yeah, the good news is we got a release out. Maybe the less good news is that we didn't do the RC1 as expected.
Let me see if I can find that issue real quick.
this thing.
Which has not been merged yet, but there's still some back and forth, and this was resolved, but it looks like, I think… Let's see… So, for those… I'm assuming everyone has contacts, but basically, Austin is getting this Blog post in place, which is attempting to… Solidify some of the terminology and define a path for stability.
And there was a section in here… Which might not show up if it's resolved.
But it's gonna impact a few instrumentations.
The idea being that if you have a stable component, it should not include unstable components, or… Alpha components.
**Cesar Munoz** 04:10 Yeah, I remember reading something about that.
**JP Jason Plumb** 04:13 Yeah.
**Cesar Munoz** 04:16 And I also saw your comment that it's… strange, given that that's something that's happening in Java.
Hotel Java at the moment.
**JP Jason Plumb** 04:27 It's true. So it's gonna be… we'll have to figure out how they're gonna handle it. It looks like… so, if you install a stable distribution of the Java agent, the default receivers… Which isn't really a thing. Maybe I should comment on that. Like, there aren't really receivers in the agent, but processors, samplers, exporters, and libraries, which is kind of vague.
should not include alpha or experimental instrumentations, right? So it's like, the agent, if it's stable, should not have experimental instrumentations.
Which is totally what we were planning on doing. It's currently what the Java agent does, so that, you know, this is why it was delayed.
**Cesar Munoz** 05:08 Yeah.
**JP Jason Plumb** 05:09 Yeah.
So, I just want to be transparent about that. I don't… I have no idea what the outcome of that is going to be. I mean… if that lands, and that is the new kind of direction for OpenTelemetry, is to, like, if you say something stable, it needs to be stable all the way down.
Then, we've got some harder decisions to make, probably, and…
**Cesar Munoz** 05:37 The thing is that I don't think that's… I don't think that's gonna work, for example, for… for… for Java.
You know?
**JP Jason Plumb** 05:44 Yeah, I mean.
**Cesar Munoz** 05:44 It's not out of space.
**JP Jason Plumb** 05:45 200-plus instrumentations? Are we gonna call them all stable, and…
**Cesar Munoz** 05:51 Yeah.
**JP Jason Plumb** 05:51 Yeah.
**Cesar Munoz** 05:52 Are they all turned on by default?
**JP Jason Plumb** 05:55 No, but most of them are.
There's a few that aren't, but I'd say the vast majority, or 90% of them are on by default.
**Mustafa Haddara** 06:05 Hmm.
**Cesar Munoz** 06:08 I guess what I'm trying to say is that… Like, in practice.
I don't see how this could be implemented as It's… as described for Autel Java, So, either… This should change, or it would essentially become a sort of recommendation, more than More than a, you know, a mandatory… mandatory thing, so…
**JP Jason Plumb** 06:37 Yeah.
It's true.
**Cesar Munoz** 06:49 But I don't know if this has… this has been discussed in the JavaSig.
**JP Jason Plumb** 06:54 I think…
**Mustafa Haddara** 06:55 I think this goes back to, like, when we were first talking about putting out a 1.0… I think we came on the idea of, like, interface stability versus… Function stability, or, like, functionality stability, right?
of, like, oh, this instrumentation isn't buggy, we know it works, but we want to reserve the right to change the interfaces or APIs or whatever into it.
**JP Jason Plumb** 07:24 That's right. I suspect their blog post…
**Mustafa Haddara** 07:27 Is talking more about Functionality stability?
**JP Jason Plumb** 07:33 Yeah.
**Mustafa Haddara** 07:38 Because, like, the idea is, if the thing is 1.0, you shouldn't enable buggy instrumentations by default, right? Which, fair.
**JP Jason Plumb** 07:46 No, in concept, I think I understand that. I think it's, I think it's definitely well-intentioned. We're trying to… You know, the project is trying to graduate, which means that it's gonna expand its user base. We don't want it to be a collection of… alpha components forever, like, I understand that, and… There's a lot of benefit in calling stuff stable and letting stuff, like, not change for a while.
But I think what that'll do to us, in Android, is it's gonna require us to… At some point, just say.
Well, we either don't include these by default, these being a bunch of instrumentations, because we know they're going to change because there isn't a semantic convention yet.
Or we say… you know, YOLO, we're calling all these stable, and if we break them, then we… Then we break them, and maybe we have to do a major revision, and that sounds like a lot of work.
So… Yeah, I don't know what the outcome of this will be. I mean, I think this… hmm… is the spec… Meeting at the same time as this meeting?
I feel like it is.
Yeah, the communication SIG is meeting… at 9… do we have clients today? We do, okay, so… the communication SIG or the spec SIG, I would expect to sort of be talking about this topic, but… We'll see what comes out of that, we'll see what we talk about on Thursday with JavaSig around this topic, and… We'll go from there, I guess.
**Cesar Munoz** 09:35 Yeah, sounds good.
**JP Jason Plumb** 09:37 I'm curious about people's comments, or thoughts, rather, on this, this thing… So… there's a little bit of back and forth with Colt and Idle.
And Jamie's been involved in that, which I appreciate.
But, there was some question about R8 stuff.
Oh no, okay, so… Cool, I asked them to move it to another issue, it sounds like there's nothing new on that. Okay.
What was the other issue I was thinking of? There's another one, I'm not awake yet.
This thing, maybe.
No. Is there an issue that matches this?
this thing, yeah, sorry, I'm definitely not awake yet. Someone was, asking, are we going to do a major version bump for this? Which I thought is interesting, because we haven't even released a major version yet, so why would we bump… I don't know what they were getting at, but this is around having GZIP be enabled, right? So this is an issue that we filed, you know, last week.
And I said, I wouldn't expect this to be a major version bump, because our API doesn't change for this, right? The DSL, even if it adds new parameters, can support this, and it's not breaking, it's backwards compatible.
The behavior, though.
could be… you could make an ar- I think there's an argument to be made that the… the behavior is breaking if you have existing backends that do not handle GZIP, which I'd be surprised, but… If there are currently backends that don't handle GZIP, and we default to it, then that is a breaking change for some folks. Curious what people think about that.
**Cesar Munoz** 11:32 I think you're right on the DSL not breaking.
By adding this.
Yeah, I guess that my question boils down to.
Should we set it as the default?
Which I don't think… Should be the case, given that My understanding is that the backend has to support it.
I don't know how to… I don't know how does it work, or at least how does the upstream implementation works. I don't know if it checks for… for some headers, see if I can… You know, accepts that kind of format before sending it.
I'm not sure, but if it's, if it's fixed, you know, being that when it's enabled, it's always going to be compressed.
Then we should probably… not set it… Like that, as just the default, and keep it as uncompressed.
Yeah.
**JP Jason Plumb** 12:39 Yeah, I think we should change this issue. I wish Hanson was here, but I want to change this issue to say, like, allow… enabling GZIP compression, and maybe not by default, right? This is, like, of the default exporters, which are OTLP HTTP.
**Cesar Munoz** 13:01 I think he mentions there that initially it could be disabled.
**JP Jason Plumb** 13:09 Okay.
Yeah, okay.
Okay, that's fair.
**Mustafa Haddara** 13:13 I think GSIP compression is really important, though.
like… Cutting down on the…
**JP Jason Plumb** 13:20 Sure.
**Mustafa Haddara** 13:20 Yeah, exactly. For Android specifically, it's really useful to cut down the payload sizes a lot, and… we haven't… actually shipped a 1.0 yet.
So… This is one of the, like, we're in alpha, let's… let's make changes, because we can.
**Cesar Munoz** 13:41 No, even in RC, we can make breaking changes, as far as I'm aware.
It's just that… So do you… so you think it should be the default? Is that what you're saying?
**Mustafa Haddara** 13:53 Yeah. As long as we're landing it with an option to turn it off.
This is, like, the least painful kind of breaking change, which is… You change one option in one spot, and it's very well defined, and you get exactly the old behavior back.
**JP Jason Plumb** 14:11 Well, the spec is pretty clear about this, I just… I haven't… this is not fresh in my brain, so I had to look for it, but it looks like all server components… presumably that's receiving OTLP, has to support both.
**Cesar Munoz** 14:25 Okay. Okay, so then he's safe.
Yeah.
**JP Jason Plumb** 14:29 Yeah, it seems reasonable to me to turn it on by default.
Pretty standard.
**Cesar Munoz** 14:38 Yeah, sounds good.
**JP Jason Plumb** 14:44 Cool.
So I think… I think we have a strong case to make here. If anybody feels really strongly about not enabling it by default, let's talk about that, but… And since we're in here and talking about this and the agenda's pretty light, I think… I think I'll just put a link to the spec there, too.
Is anyone, planning on working on this?
Okay.
**Cesar Munoz** 15:54 I can have a look.
**JP Jason Plumb** 15:56 Yet, do you want me to sign it to you?
**Cesar Munoz** 15:58 Yeah, please.
**JP Jason Plumb** 16:00 Sick. Thank you.
Okay.
We have 100 open issues!
This is new.
I get twitchy when I see GPT in somebody's name, but it's actually their name. I mean, it's a shortening of their name.
Okay, so we have Semconv for Telemetry SDK version.
Should we replace RUM SDK version with telemetry SDK version?
That's a good question. Probably.
What's our value for RUM SDK version?
**Cesar Munoz** 16:59 ROM SDK version, I'm guessing, is there because of… historical reasons.
**JP Jason Plumb** 17:05 Yeah, I think so.
**Cesar Munoz** 17:07 Yeah.
I'm not sure what was the…
**JP Jason Plumb** 17:13 Oh, it's from the buildings.
Interesting.
**Cesar Munoz** 17:19 Drew was the initial, Idea behind it, but if it's the same as the, telemetry one, then probably yes.
Should replace it.
**JP Jason Plumb** 17:32 Yeah, I wonder what we're specifying now. There, I think… With this silly metrics… PR, I think we can… I think I have an example of what the resource currently, or, you know, a month ago contained.
Let's see… this one.
So, this was the resource, just by default, so Telemetry SDK, version, that's coming from Upstream, I believe.
ROM SDK version looks like our version.
So, 1.51.0, that's the Java SDK.
So…
**Cesar Munoz** 18:25 So, maybe… so you're saying that Otelandra might… might be… because I guess it could be seen as… an SDK.
Kind of, depending on… How you look at it?
**JP Jason Plumb** 18:39 Let's look at what the convention says.
**Cesar Munoz** 18:43 Because I also know that there's a distribution.
namespace.
**JP Jason Plumb** 18:49 There is.
There's telemetry distro version.
Telemetry distro name.
Yeah, so these are two different things, right? Telemetry Distro, telemetry SDK.
Is there any description of the difference between an SDK and an instrumentation? I know it's a little bit pedantic, but maybe it's important.
Well… I think the answer is probably yes, though, because this RUM SDK version is not spec'd anywhere, I don't think.
**Cesar Munoz** 19:30 I haven't seen it.
So far.
**JP Jason Plumb** 19:38 Yeah, I think we should.
**Cesar Munoz** 19:42 But it's… But it's a good question. Should it be telemetry CK or telemetry distro? At least for the case of all telemers, because… Kind of feels like it's neither.
In the case of Hotel Android.
**JP Jason Plumb** 19:58 It does feel more like… like distro.
But distro… the intention of distro is for people to add their customizations, like the elastic… Android distro would use this string, and it would be your version. So if we put it in upstream Android, then you would have to either append it or… Find some other place to put it.
So, I don't think that our native OpenTelemetry Android agent is really a distro. I think distro is intended to be vendor distro.
Right?
I think that's the intent.
**Cesar Munoz** 20:35 It sounds… Reasonable, yeah.
**JP Jason Plumb** 20:38 But it's confusing, because it's like, it's the name of the ag… it's the name of the agent, or distribution.
So there's… there's some room to, I think, improve these a little bit, at least… The descriptions of them, and the distinction between the two.
I don't… so given… given this, I don't know that we want… I mean… We do indicate what version of the upstream SDK we use. We don't give any version about what version of the instrumentation we use.
But all of that should be discernible from the build artifacts. Like, if we know that we're using… if we know that someone's using 0.13.0, we can trace back what instrumentation and SDK that was built with.
Right, that's built.
**Cesar Munoz** 21:28 true.
**JP Jason Plumb** 21:28 Into the build process.
So, that should be fine.
I suspect we should get rid of this, but then we need this version number somewhere.
and telemetry SDK… I think we should have Android for these.
That's my instinct.
**Mustafa Haddara** 21:52 Yeah, plus one.
**JP Jason Plumb** 21:54 Okay.
Do I have a plus 2?
I haven't convinced anyone else yet.
**Cesar Munoz** 22:01 I know, I just really don't have a reason why not to go with either.
You know? Yeah. So… yeah, that's fine.
was trantically.
find out if there was an issue, but I don't see any issue with either.
I know that for distro, I think for the, back in… Java Elastic Distro.
I think that's over… over… overwritten Because the Java agent, I think, provides a distro.
value.
But, so, I mean, you know, vendors can still override stuff, I think, but, But I'm really not.
Yeah, it's weird. It's, as you said, it's like, kind of feels like it's more of an SDK, even though it relies on the Java SDK, still feels like It's not exactly a distro, so… Yeah, let's go with SDK.
**JP Jason Plumb** 23:05 Okay.
Alright, well, I can, you know, I'm just basically, like, doing, issue comment work as a group here, because we have a light agenda. If anybody has any other topics they want to talk about, or issues or PRs to look at, please, now's a good time.
And why is this so… why is this so jacked? So…
**Cesar Munoz** 23:42 I have a question regarding… What's the.
**JP Jason Plumb** 23:49 I think if you don'.
**Cesar Munoz** 23:49 I know there were some discussions going on about what to do with metrics for clients.
And…
**JP Jason Plumb** 24:00 metric?
**Cesar Munoz** 24:01 Yeah.
I know that the idea initially was not to use metrics.
And to be honest, I don't… I don't hate that idea. I really don't have, right now, a use case.
for metrics.
But it's… it… My understanding is that I'm not sure if we actually have Made a consensus on what to do with mentors and clients.
Because… And the reason why I bring this up is because I think today, in Slack, Somebody… brought that up, you know, Jose Andre.
And… you know, whatever decision we make, I think it would be nice to… Have some sort of docs page explaining if we decide to go with metrics or not.
And why? Because, you know, it seems like people oftentimes brought it up… bring it up, and so… Yeah.
What to answer?
**JP Jason Plumb** 25:10 I thought when we talked about this recently, the idea was to have something in here which described it, but I'm not sure where that… Was it a metrics issue? Yeah, we've definitely discussed this, and I don't know that we have written down what our decision was.
So I agree with you, there's work to be done on that.
**Cesar Munoz** 25:33 I think there was an issue created by… I don't know if it was Santosh.
From the client's sake.
**JP Jason Plumb** 25:40 In the spec, Or SIMCOM?
**Cesar Munoz** 25:44 Probably.
Yeah, I'm not sure where.
**JP Jason Plumb** 25:47 Probably spec, right?
Oh, shit.
Boom.
Like that, maybe?
I forget who.
**Cesar Munoz** 26:03 thing with an S.
**JP Jason Plumb** 26:05 That?
**Cesar Munoz** 26:07 Oh, yeah.
There is.
**JP Jason Plumb** 26:12 Yeah.
Still open.
And he doesn't look like this, by the way, that's not… that's not, like, a picture of his face, that's just a generated avatar.
What's the last comment on this? Okay, so back in August… Yeah, so top-level page somewhere on the website, which I think… I think is why this placeholder was created.
Yeah, I think… I think that's what Hansen did.
There's a thumbs down from that person.
Yeah, so our API…
**Cesar Munoz** 26:59 Nope.
**JP Jason Plumb** 27:00 we can… Cesare, I think you were an advocate way back when I was like, we should not even allow metrics to be exported, and you were like, you know, we should be consistent with the signals, and so the compromise currently is that we do support… we allow the creation of metrics.
**Cesar Munoz** 27:18 Is that we don't create those ourselves.
**JP Jason Plumb** 27:21 Right, nothing to do.
**Cesar Munoz** 27:22 don't prevent them, users, from doing so. Correct.
**JP Jason Plumb** 27:27 But if someone does, they're probably gonna be surprised when they get this from a million handsets, right?
Which was the whole, kind of.
**Cesar Munoz** 27:36 Yeah, fair enough.
**JP Jason Plumb** 27:37 This was the idea behind this experiment, and that's really what this was, was just like a… Experiment to see, like, if we strip this down, what's the minimum set of shit that we think we need for a metric to be meaningful?
But, you know, you lose… like, I don't know, like, this important stuff is lost? Like… you know, I think if you're looking at a given metric, you really do probably want to know what models You're looking at…
**Cesar Munoz** 28:08 Yeah.
**JP Jason Plumb** 28:09 at least a model identifier, and probably Android version.
But, whatever, I mean, so, yeah, we still don't have… We still don't have that guidance here.
So I think I will just link to these.
And just make some comments here.
**Cesar Munoz** 28:31 Yeah, I was thinking maybe we can just share that link.
**JP Jason Plumb** 28:34 Yeah.
**Cesar Munoz** 28:34 in Slack with this, person.
**JP Jason Plumb** 28:37 Yeah, okay. I haven't seen it yet.
**Cesar Munoz** 28:42 The cardinality issue, it's… I don't know if we've discussed this, but is it something that might also affect logs?
You know, log events.
You send the same log event from… 1,000 devices.
**JP Jason Plumb** 29:06 Well, I think the… I think the use case of a log or an event is somewhat different, unless your backend is metricizing from logs, which some do, right? You might be looking at events and… Creating histograms or, you know, plotting, like, counts of a certain log, or a certain event over time.
And then if you start doing aggregations with metricized log data, then I think you do run into the same problem.
But, because it's entirely back-end, the back-end can then choose… the thing doing the metricization, which I don't even know if that's a term that we use in OTEL, but certainly a term we use here.
The components that are doing that metricization get to decide What resource attributes and what dimensions to put on their data.
**Cesar Munoz** 29:56 Got it.
I was just curious.
But really don't have much to say on that.
**JP Jason Plumb** 30:05 That's cool.
Yeah, I hadn't seen this message yet from the Slack person.
**Cesar Munoz** 30:15 That's fine, if you like, you can… Have a look later.
**JP Jason Plumb** 30:18 But people… I mean, this… it's interesting, because this does keep coming up, and it's… I'm assuming it's… It's mostly… Naive users that are coming from having instrumented other applications, like microservices, and they're used to seeing metrics, and… Like, it makes sense to me that users naively want metrics for their mobile apps, and… like, whatever the experience that, like, Google App Store data gives you, do they… they probably chart metrics, too, right?
**Cesar Munoz** 30:53 I think so.
**JP Jason Plumb** 30:54 Yeah, what would I look forward to see what they provide?
**Cesar Munoz** 31:01 Barely Play Store…
**JP Jason Plumb** 31:04 vitals?
It's gonna be, like, downloads and install base kind of stuff, yeah. Oh, perceived crash rates… So there's this thing, though, there's the Vitals dashboard.
Do they give a screenshot? They don't. I just want a screenshot.
They are not gonna give a screenshot.
I haven't used… This stuff in a long time.
So I don't… it's not fresh in my brain what that looks like for… for real apps and a real app store.
**Cesar Munoz** 31:49 Me, yeah, it's the same for me. And they also quite change it quite often, so…
**JP Jason Plumb** 31:56 But I suspect that that's where people are coming from. It's like being used to seeing some dashboards.
With, you know, charts and lines, and it makes perfect sense that they would want to ask for that.
We lost Jamie.
**Cesar Munoz** 32:11 Also, if the, like, if that's the case.
I think I found that screenshot. If that's the case, then… It would also be kind of difficult to, you know, To… to… to have an argument against metrics, because then I guess people can… can just go and say, well, but the Google Play Store does… does it, so…
**JP Jason Plumb** 32:38 Yeah, totally.
But maybe in our description or our explanation, we could say that what's emitted from the phones is probably still not metrics. It's, like, created into a metric. It's metricized by the Google.
**Cesar Munoz** 32:53 Yeah, probably. I found that good.
**JP Jason Plumb** 32:55 and the Google Vitals.
Yeah, let's see.
**Cesar Munoz** 33:01 I don't know how dead it is.
**JP Jason Plumb** 33:04 We don't have instrumentation for stuck partial weight locks yet.
I was excited to see that somebody submitted, orientation instrumentation. Did you review that yet?
**Cesar Munoz** 33:20 Well, I haven't. I saw that they query… But I haven't. I actually have a question, because I took a first glance at it.
**JP Jason Plumb** 33:29 Yeah.
**Cesar Munoz** 33:30 And they seem to have added it Right away, as one of the default instrumentations for the…
**JP Jason Plumb** 33:37 We did, yeah. Yeah.
**Cesar Munoz** 33:40 I just want to confirm if that's what we want, because I really don't have… I like it, because I think it's pretty low…
**JP Jason Plumb** 33:50 frequency signal.
Like, unless somebody's really turning their app all the time, I think it's, you know, it doesn't happen that often.
So, I like it as a default.
And people can turn it off if they don't find it helpful.
If you're looking at it with a RUM lens, I think… it's very helpful to know when a user turned their phone, like, as part of their journey. Like, they rotated their phone, you're questioning why, or what does your UX do to encourage or discourage that, like…
**Cesar Munoz** 34:22 Okay.
**JP Jason Plumb** 34:23 Seems helpful… to me.
**Cesar Munoz** 34:26 Sounds good.
Yeah, let's go with that.
**JP Jason Plumb** 34:30 I did… I did put a block on it, though, because they have some… they have some work to do on it, and hopefully they'll get back to it.
**Cesar Munoz** 34:37 I'll have a look, too.
**JP Jason Plumb** 34:39 Cool.
Well, I don't have anything else. Somehow we've managed to get 35 minutes, but, we can… we can sort of break if that's… if that's a good time.
**Cesar Munoz** 34:52 Yeah, I also don't have anything else for now.
**JP Jason Plumb** 34:56 Okay, cool.
Cleverchuck, you good?
**cleverchuk** 35:01 Yep.
**JP Jason Plumb** 35:03 Okay.
Well, thanks for coming out, appreciate the help, everyone.
**Mustafa Haddara** 35:08 Cool.
**cleverchuk** 35:08 Cheers.
**Mustafa Haddara** 35:08 I've.
**Cesar Munoz** 35:09 Thank you.
**JP Jason Plumb** 35:10 Right.
