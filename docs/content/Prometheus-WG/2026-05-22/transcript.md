SIG: Prometheus WG
Date: 2026-05-22
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Arve Knudsen** 04:24 Hello, Creo. How are you doing?
**krajo Krajcsovits** 04:28 I'm good, thank you.
How are you?
**Arve Knudsen** 04:39 I'm good. We're actually having a very beautiful day here today.
It's like, so, Marie's, arriving.
**krajo Krajcsovits** 04:50 Yeah, I wish I wasn't on call from Saturday.
**Arve Knudsen** 04:54 Oh, okay.
**krajo Krajcsovits** 04:55 I really wanted to go hiking, but…
**Arve Knudsen** 04:59 Is it, is it warm in Budapest?
**krajo Krajcsovits** 05:03 Yeah, it's, like, 20-something, I think? 26.
It's going to be even, warmer over the weekend.
**Arve Knudsen** 05:12 Looks like we are… looks like it's 27 degrees here right now.
**krajo Krajcsovits** 05:17 Oh, that's cool.
**Arve Knudsen** 05:18 And it's gonna be… If it's correct, we're gonna reach 30 degrees on Tuesday.
**krajo Krajcsovits** 05:26 Oh, wow, okay, that's… maybe that's a little bit too much.
**Arve Knudsen** 05:35 I quite like 30 degrees, I mean, I guess I'm not sure if I'm used… not sure if I'm quite used to it yet, like, maybe I need a bit of, adaptation.
But when I'm… when I'm used to it, so that's kind of my, you know, my… comfort temperature.
**krajo Krajcsovits** 05:53 Right.
Yeah, we are on top floor in a… Flat-roofed, building, so… 30 degrees gets really hot inside very soon, so we need to use the AC.
**Arve Knudsen** 06:07 Yeah, same here. Do you know our maximum temperature in the sec- on our second floor?
the maximum we recorded.
**krajo Krajcsovits** 06:15 What was it?
**Arve Knudsen** 06:16 36.
**krajo Krajcsovits** 06:17 Ouch.
**Arve Knudsen** 06:19 I'm laughing, but it was not fun.
We were forced to buy an AC.
**krajo Krajcsovits** 06:27 One time today, he wrote down, he went to the cinemas to watch a movie just to get the air conditioning.
**Arve Knudsen** 06:32 Yeah, that's kind of classical, isn't it?
Hello, David.
**David Ashpole** 06:47 Let's see, are there topics for today?
I always open the old dock.
First… Mmm… I don't see any.
See, advisor.
I'm happy to talk about Arthur's topic, but if he's not here… You might just want to hold it and wait.
I assume he might still join, so maybe we can just wait and see. Otherwise, if there's other stuff you guys want to talk about, You can talk Or we can… yep.
**krajo Krajcsovits** 07:30 Oh, there it is.
**Arthur Silva Sens** 07:36 Hello.
**David Ashpole** 07:38 Arthur.
**Arthur Silva Sens** 07:40 Sorry, I'm a bit late.
**David Ashpole** 07:53 Okay, I put everyone's names down. We have one topic, and that's yours, Arthur.
**Arthur Silva Sens** 07:59 yeah, I've been sharing… with a few people that I'm refactoring a lot of Prometus exporters to make them embeddable into collectors.
So right now, it's mostly me, Ben, Kochi, Nicholas Takashi, and Kyle doing this work.
**David Ashpole** 08:22 Hmm.
**Arthur Silva Sens** 08:23 And we came up with a list of exporters that we want to refactor.
Like, most of them we can act on our own, but two… like, Coop State Metrics and CAdvisor are not owned by Prometus.
Yeah, so I was… I wanted to ask mostly you, David. Like, you've worked on both before. It's like, is it easy to… to convince them that this is good? Like, what is your thoughts?
**David Ashpole** 08:52 Are you using the, you're using the bridge, though, right?
**Arthur Silva Sens** 08:57 Yes.
**David Ashpole** 08:59 So… I think C-Advisor… C-Advisor might be open to it. The issue right now is that C-Advisor kind of doesn't have owners. I'm not sure if you guys remember that conversation about, like.
So, C-Advised Google was like, we want to donate this to… they're just trying to find someone to donate it to, like, does OpenTelemetry want to own it?
And OpenTelemetry kind of was like, mmm… they tried to give it to Kubernetes SIG Instrumentation, and we were like, No, thank you.
And so now they're planning to just, like, retire it?
And remove it from the kubelet.
So… I don't know if they're actually gonna go ahead with that, or if… They were just trying to get someone to own it. But…
**Arthur Silva Sens** 09:55 Yeah, I do remember that.
**David Ashpole** 09:57 I don't… I don't think they're… I don't think they would be against this kind of thing, it's just… I don't… I suspect that none of the people working on it want to do, like, reviews and… Take on projects and stuff.
Like, they just want it to go away, not to… I mean, you could… you could, bill it at least as… offering collector compatibility, which I think would be helpful.
it may be a step towards making it easier for this to exist in Contrib, or something like that, so maybe… Maybe, maybe, maybe that would be… A feasible thing to do.
But… I don't think that one is simple. I think for CubeState metrics, the biggest issue is just that KubeState doesn't use the Prometheus client.
**Arthur Silva Sens** 10:46 Yeah, yeah, yeah, I know, I…
**David Ashpole** 10:48 Okay, right? So, like, You're welcome to come to seek transportation on Fridays? No.
Thursdays.
When is it? No. It's actually during this meeting.
**Arthur Silva Sens** 11:03 Oh, really?
**David Ashpole** 11:03 So it's in the second half of this meeting, so we could have this talk and then hop over and ask them themselves, if you want. But.
**Arthur Silva Sens** 11:12 I would need links, I don't know how to join, but yeah, happy to do so.
**David Ashpole** 11:17 Yep.
Yeah, I can… Is the agenda… And here's the Zoom link.
But yeah, so that one will start at 11.30 in, like, 20 minutes.
so we could join there and talk about that. My suspicion is that they would be supportive, But… the…
**Arthur Silva Sens** 11:47 It's gonna be hard.
**David Ashpole** 11:47 hard lift, right? It's not as much about, like, whether they would do it or not, it's that, like.
someone's signing up for a lot of work, and like, I don't know if it actually… Like, is the performance gonna be good enough where it'll make sense for people to run it this way?
**Arthur Silva Sens** 12:06 But, like, it is… they don't use the client going exactly for performance reasons.
And I… I… yeah, like, I don't… Like, the way we are implementing is that the… collector… the bridge implementation doesn't live inside the exporter code. We just want to refactor so we can use the exporter code outside of it.
**David Ashpole** 12:37 But it would… would it have to implement the, collector interface?
**Arthur Silva Sens** 12:41 No. Okay. No, they do not. We just want to make sure that exporter code is reusable as a library.
And then we implement this outside.
**David Ashpole** 12:51 Yeah, yeah. What… but what's the library interface? Is it the Prometheus Describe and Collect?
Gatherer interface, or is it…
**Arthur Silva Sens** 13:00 We need a package that provides the user-facing configuration, and a package that we can extract a registry out of it.
**David Ashpole** 13:12 Okay, so it does… it would need to support the Prometheus client library, essentially, right? Because the registry is, like.
the Prometheus client thing.
**Arthur Silva Sens** 13:20 It's something that, if we can't transform what they have into a registry, That's good enough for.
**David Ashpole** 13:28 That could also… yeah, that could also work. Totally, you're right.
Okay, so… Should we, like… I'm supportive.
I don't… so just… I'm not, like, one of the… I'm one of the TLs for the SIG. I mostly own the tracing stuff and, the metric stuff in core Kubernetes. There's, like, almost… I would say, like, two-thirds of the SIG today is actually just CubeState metrics folks, and they kind of operate pretty independently, so…
**Arthur Silva Sens** 14:02 Okay, I… I did a noise.
**David Ashpole** 14:04 Supportive.
**Arthur Silva Sens** 14:05 I thought you left the Sikh long ago. So you're still joining?
**David Ashpole** 14:10 kubernetes SIG Instrumentation? Yeah, I'm still one of the tech leads.
**Arthur Silva Sens** 14:15 Oh, well, I didn't know that. Cool.
**David Ashpole** 14:20 I don't… maybe I should have left.
one of those maintainers that doesn't… actually, I… the SIG is not active in general, so the bar for being active, for me, I feel like, is not that high. But I, you know, I put up a PR every few months, like… Making me one of the most active people in the SIG, so…
**Arthur Silva Sens** 14:42 Okay, yeah, I'm down to go there in 20 minutes.
Do you want to discuss something else, meanwhile?
**David Ashpole** 14:49 Any other exporters on the list that are worth discussing?
Windows Exporter.
**Arthur Silva Sens** 14:59 I just… I just found some exporters that are very widely used, but… I don't have any data, it's just… my own… fonts.
**David Ashpole** 15:14 Cool.
I like this, especially if there are any exporters that aren't, like.
what would you say? Supported by… If there aren't any exporters.
if they're exporters for things that don't exist in the collector, I feel like that would be very… very valuable, right? Because then, it's like, if we could… if we could roll back the clock and have done this from the beginning.
Yeah. You know? Then… Like, there would be fewer headaches, so getting ahead of the ones that don't exist yet can make it easier to say, oh, like…
**Arthur Silva Sens** 15:50 Like, right now, it seems so obvious. Like, this is such an easy… kind of work.
But yeah, took us a while to realize that.
**David Ashpole** 16:01 Yep.
Cool.
Are there any… let's see… Are there any PRs open that we have that need discussion?
Oh, it.
**Arthur Silva Sens** 16:12 Cryo has a…
**krajo Krajcsovits** 16:15 Yeah, I just… I was wondering if you had time, David, to look at the… the spec BR that I have open.
**David Ashpole** 16:22 The histogram on, right?
**krajo Krajcsovits** 16:24 Instagram, yep.
**David Ashpole** 16:25 I did look at it.
I thought there was…
**krajo Krajcsovits** 16:30 Any general feedback, I reorganized it.
**David Ashpole** 16:34 Yeah, I was… I was pretty happy… did I approve it yet?
Jack approved it.
**Arthur Silva Sens** 16:43 I think we added a comment about delta conversion.
Have you seen that, Cryo?
**krajo Krajcsovits** 16:51 No, not yet.
I've been busy with other things. I just wanted to make sure that I got something to work on next week, although next week's going to be tricky a little bit.
I… Monday is a national holiday here, but I'm on course, so I might as well work on that PR. Also, I want to open another one in parallel to have We're at least one more.
for the specs, so that I have more going on at the same time, because I have this weird, you know, cycle of… mainly working on this on Mondays, and then getting back to the next Monday, so it makes sense to have more open.
So, we move forward more quickly.
**David Ashpole** 17:31 Let's talk about… I think there's one open thread we have, About whether to refer to the histogram's count, or to refer to the histograms… Underscore count metric.
Yep. And… Yeah, we… when we originally wrote the spec, we wrote it with Like, only the text format in mind, so we had a lot of the, like, everything underscore count.
**krajo Krajcsovits** 17:57 Oh, yeah.
**David Ashpole** 17:59 And now we have, like.
**krajo Krajcsovits** 18:02 Put the buff.
**David Ashpole** 18:04 Well, we've got Protobuff.
Which is complex, and then we also have open metrics.
To… which has the, like, the count field in it, and so…
**krajo Krajcsovits** 18:15 Okay, now I understand what you meant, yeah.
**David Ashpole** 18:17 Yeah, yeah. When we did the summary one, we went and changed all that to, instead of saying underscore quantile, to just say the quantile.
**krajo Krajcsovits** 18:25 Okay, now I understand what the problem is, I can follow up on that, yeah, okay.
**David Ashpole** 18:29 Cool. Hopefully it's just a simple thing.
**krajo Krajcsovits** 18:34 I mean, it's going to be simple from my point of view, but, like.
I don't know how simple it will be from… The point of view of people that want to implant it.
Do… would you still say something like.
If you have to do classic histograms, then these names should be used. Like, try to help a little bit with the… With that…
**David Ashpole** 18:58 Yeah.
**krajo Krajcsovits** 19:01 I don't know.
**David Ashpole** 19:02 My… like, part… part of why I… I've… I was, like, interested in pushing on the, like, Prometheus should have ownership of the… How does this get written into a text format, or into any of the, you know, 6 text format we support, is because I was kind of hoping that, like.
If we just said, like, yeah, make this the count of the histogram, then… There's some set of libraries that Know how to take that and turn it into… Like, text exposition responses, and do all the negotiation.
For content type and stuff, right? Like, kind of separating those two out, where we map the data models in this document, and then Prometheus can continue introducing new formats as they… as, you know, we want. Okay. So that… that's, like, the direction I want to go, but we're not… Yeah, I agree, like, for someone doing it in Rust, they're gonna have to basically look at this.
And then, maybe there's, like… Prometheus… You know, text exposition format.
docs that they'll have to go read to discover how A maps to the actual text representation for the classic, you know, text format.
**krajo Krajcsovits** 20:22 I mean, to be fair, we have those descriptions, you have the Prometus format described in the Prometus I.O, open metrics already also there, a lot of buff is well-defined, so… It should work out, I understand what you're trying to do. Okay, I'll… I will not do it then. Also, I think it's… Most of this is already implanted, especially for graphics programs, so it's not like…
**David Ashpole** 20:43 Yes, yes, yes.
**krajo Krajcsovits** 20:44 A ton of new people will touch it.
**David Ashpole** 20:46 And then, there's one outstanding question from Jack, just, like, can we confirm that this is the current behavior of the Prometheus Remote Exporter?
I think we've all been through it a few times, but it would be good Just as part of this process for one of us to sign up.
even if it's just pointing Clawed at, the remote write exporter.
Spending 15 minutes to make sure.
**krajo Krajcsovits** 21:15 Well, it certainly… the last time I looked at it, it didn't do the NHCB thing as an optional.
**David Ashpole** 21:23 This, this is for the part that we're marking stable, is what…
**krajo Krajcsovits** 21:27 Right, right.
**David Ashpole** 21:27 That's the…
**krajo Krajcsovits** 21:28 Yeah, I think it does that, but I can take another look as well.
And, yeah, ask code, yeah.
**David Ashpole** 21:35 Okay.
**krajo Krajcsovits** 21:36 Cool. Alright.
**David Ashpole** 21:50 Actually, did I do this? Nice.
**Arthur Silva Sens** 21:52 And regarding, like, if you want to take, another issue?
I feel like Jonathan has not worked on the exponential histogram.
**krajo Krajcsovits** 22:04 Oh yeah, definitely.
**Arthur Silva Sens** 22:04 It's not doing… contains.
**krajo Krajcsovits** 22:07 I'll do that.
**David Ashpole** 22:11 I didn't even know at GitHub, or GitHub supported at me.
No.
In my searches. I like it.
**Arthur Silva Sens** 22:43 David, do you have permissions on the SIG instrumentation meeting notes to add a topic there?
**David Ashpole** 22:51 Yes, kept.
100%.
**Arthur Silva Sens** 22:55 Thank you.
**David Ashpole** 22:58 I would hope so.
We have a lot of topics.
Very big book.
on the agenda.
**Arthur Silva Sens** 24:21 Thank you.
**David Ashpole** 24:23 Yeah, awesome.
For some reason.
I thought I had opened some issues for the… remote Exporter.
**Arthur Silva Sens** 25:00 We don't have any open PRs, besides the flaky tests.
**David Ashpole** 25:06 Yeah.
I'm just responding to Jack.
Okay.
I think we're good to go.
on the histogram PR. I'll probably approve that. I'll take one last look.
Once… actually, right. You're gonna change some of the language there, but hopefully it should be simple changes.
Do we have anything else to discuss?
Should we open up the.
**Arthur Silva Sens** 26:49 don't fit.
**David Ashpole** 26:49 project board? Is that useful?
**Arthur Silva Sens** 26:54 Do you want to share your screen?
**David Ashpole** 26:55 Sure.
Too many tabs right now.
a receiver, No updates.
And then… can everybody see? Let me make this bigger.
Come on.
You have workable ones.
**krajo Krajcsovits** 27:38 Yeah, I think I'm still… Yeah, I… Still not in the whatever group.
**David Ashpole** 27:44 Yeah, that's Totally fine. I'm working on it.
**krajo Krajcsovits** 27:49 Hopefully this will… this work will give me the cache to actually get into the group.
**David Ashpole** 27:55 Translation strategy.
**Arthur Silva Sens** 28:00 as a translation strategy, I was planning on opening a PR, but then we received an issue from some guy complaining that it was not clear.
Do you remember?
**David Ashpole** 28:14 That was Quentin. Yeah, Quentin, just… Don't, don't worry about Clint.
**Arthur Silva Sens** 28:21 I, I don't, I don't know him, but…
**David Ashpole** 28:23 He sits next to me at work.
He's a Googler.
**Arthur Silva Sens** 28:30 Okay, so, but what do we do? We just ignore the issue and move on?
**David Ashpole** 28:35 I… Let me find the issue. No, no, no, we shouldn't… shouldn't just do that.
How are you?
I think there was a small change he asked for, so… in MIT.
Let's see, where's the key part?
I think there's, like, a precedence.
**Arthur Silva Sens** 29:40 I think, like, he's not asking to change.
Anything, just to… Like, just to clarify the text somewhere.
He says it's confusing or ambiguous.
**David Ashpole** 29:55 Yep.
Ben, I cannot find anything in here.
I think it was this section that he had an issue with.
I'm gonna make it readable.
I think his… let's see, his issue was… this makes it sound like… This makes it sound like content negotiation saying.
UTF-8 means that I should get my dots.
Right.
**Arthur Silva Sens** 32:53 Okay.
**David Ashpole** 32:55 That was his, like, fundamental thing. So, I think the question is, how do we make this Like, must, you know, must comply with the accept header.
We're saying this… the accept header just says what the server can accept.
And he said it makes it sound like if I say.
content equals UTF-8, I should get my dots.
**Arthur Silva Sens** 33:19 I think, I think there's a section that says, named the… Content negotiation and translation strategy that is very focused on this.
**David Ashpole** 33:30 Yeah, yes.
**Arthur Silva Sens** 33:31 Interaction with translation strategy, yeah.
**David Ashpole** 33:34 So that's the section.
**Arthur Silva Sens** 33:37 But… isn't that clear?
**David Ashpole** 33:41 Well, the examples don't actually cover that case, so… If configured with underscore escaping with suffixes, but the client requests UTF-8, there's no need to revert.
What has been translated since the exporter will continue to be compliant.
**Arthur Silva Sens** 33:58 Okay.
**David Ashpole** 34:00 Let me find the discussion. So originally it was about, like.
So this was, for example, one of the… ones that we disagreed on, Quentin and I, in terms of what the example should look like. If no translation.
And no accept header.
then I should get foo.bar.
but… So that didn't seem correct.
**Arthur Silva Sens** 34:34 Yeah, like, a Prometheus that doesn't send except heater means it's before 3.0. 3.0 does not accept dots by default.
**David Ashpole** 34:51 Let me see what…
**Arthur Silva Sens** 36:59 I think I need to go into the… Kubernetes link.
Yeah.
I'll be going there.
**David Ashpole** 37:15 Okay, I'll see ya, I'll finish the smell training.
**Arthur Silva Sens** 37:18 Alright, this isn't…
**David Ashpole** 37:18 Alright, bye everyone.
