SIG: Prometheus WG
Date: 2026-04-24
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Arthur Silva Sens 00:00:44 Hello.
krajo Krajcsovits 00:00:49 Hey, hey! Sorry, I'm just trying to answer a… Hostings question to… for Yuri, Anton?
I'm probably not the right person to answer, but… I'm trying to get him to write into Prometheus Dev first.
Oh, is this recorded? Then, yeah, then I said nothing.
Arthur Silva Sens 00:01:14 That's right. I'm still writing down the topics.
I'm a little bit late.
Oh, hello I… I've been… stuck in meetings since I started my day. I had, in my mind, like, 4 topics for today, but right now, I cannot remember any.
David Ashpole 00:02:49 Well, you weren't one of them down, so…
Arthur Silva Sens 00:02:51 Yeah, I had more.
I… David, could you, like, I think you are… up-to-date with the design doc from Braden. Can you explain while I hunt other topics?
David Ashpole 00:03:16 I can explain a little bit, yeah. So, let me… Let me share my screen.
do this.
Owen Williams (he/she) 00:03:43 You make the window a little narrower.
If possible.
David Ashpole 00:03:50 Yes?
Owen Williams (he/she) 00:03:51 Thank you.
David Ashpole 00:03:53 I zoomed in.
Owen Williams (he/she) 00:03:54 Yeah.
David Ashpole 00:03:55 So this is Braden's dock.
So it seems… so my take on this is… Basically…
Owen Williams (he/she) 00:04:16 Sorry.
Sorry to interrupt, I don't have access to this.
David Ashpole 00:04:20 I think he… There's, like, a Slack thread where he asks people for people's emails, because he doesn't want to send it out publicly yet.
Owen Williams (he/she) 00:04:29 Okay.
David Ashpole 00:04:32 I think it's in… Let's see… collector… Is it in Collector Dev?
No, might be in… Collect… it's in collector leads?
Arthur Silva Sens 00:04:49 I think it's Collector Def.
David Ashpole 00:04:51 Collector debt, okay.
There it is, yeah. I was looking for something by Braden, but you started the thread right there.
Arthur Silva Sens 00:05:08 Yes.
Oh, some extra context on this one, It is required that we… a component that is declared stable has a way to observe its own thing, like, what the component does, it needs to be observable.
And this includes if we drop data, because of whatever reason.
Users of this component is… are able to tell how much data is being dropped.
And the reason.
And the Prometheus receiver… does drop data.
Which I can't recall why.
I think there are some…
David Ashpole 00:06:06 You can fail to translate stuff. If you, like, somehow have a metric that has… a, a type that doesn't exist in Prometheus?
Then, like, you can get… It's theoretically possible, I don't know if… or if you have, Like, histograms that are… No.
Arthur Silva Sens 00:06:26 Instagram, for example.
David Ashpole 00:06:28 Right, so, yeah, we do drop, just, like, straight-up drop gauge histograms, you're right.
Arthur Silva Sens 00:06:34 Yeah, so we need a way… To have a metric for this.
And, it seems like it's more complicated than we initially thought, and we… Like, we're block on RFC, and this is the RFC.
David Ashpole 00:06:50 what's interesting is this seems extremely non-controversial to me, because if I look at… I'm consumer… Is there… I think it was, like, a partial… Here?
Is it an ex-consumer error?
Profiles… Thought there was something.
Interesting. So today, I think you just make one of these, like, new… new metrics errors.
And you can just pass the data that… You weren't able to send.
And it'll just log it, or it'll just handle it properly.
But it… it isn't handled in… It's handled for exporters, but not for receivers, for some reason.
So I'm not entirely sure why we need this, necessarily, but I'm okay with it.
Arthur Silva Sens 00:08:11 If I remember correctly, the part that Braden is struggling is something related to gRPC codes?
Where partial success is declared, okay.
and the success in gRPC.
David Ashpole 00:08:30 Yeah, I mean… I… I think that that's silly.
But… This feels a little bit overthought to me. I think we just need… A thing that says that something was dropped.
My ask was actually that… We align on using error.type.
In these metrics, so that… Instead of having to… like, partial success is very much a An error that is defined by… like, OTLP, there's, like, an actual partial success message.
So, I think it would be nice if there was a way for us within the Prometheus receiver to define a… translation error, right? That… includes a… Number of points that we failed.
And so that then, when… when it shows up in self-observability metrics, it'll be differentiated from other errors, or it'll have, like, an error.type that's associated with whatever errors that we came up with. We could have multiple errors if we felt like that was useful.
Like, we could have unsupported errors where we could have, like, invalid argument type errors, like… That, to me, would be more useful than just… We could have partial success.
But, I… I think as long as we get… as long as we get our self-observability metric with the count of points that were not sent, I think that's… it meets our needs.
Arthur Silva Sens 00:10:32 But, like, to do what you just described, Do we still need this?
If we can just implement our own metric.
David Ashpole 00:10:44 Well, my hope was that we would define an error that implements an interface And the interface would be defined in consumer error. So the interface would be, like.
Failed items, or something, that would return an integer.
And then the self-observability framework.
Would look at the errors that we pass back to it, to see if they implement the interface.
And if so, it would add error.type.
And the count returned from the error, so that we could define our own errors, we could define the error types, and we could tell them how much How many things were dropped?
Arthur Silva Sens 00:11:24 Okay.
And how confident are you that you can convince Braden to… simplify.
David Ashpole 00:11:30 Alright.
I don't think… I just shared my opinion, I… I think we need this to move forward. It's blocking our stuff. I assume it's blocking other receivers as well, because I don't… I can't imagine a receiver stabilizing without Being able to somehow report the number I've dropped.
Like, honestly, if it comes down to it.
then… Like, we can just define a new metric, and that's not the end of the world.
It's… it's just not the best user experience, honestly.
Arthur Silva Sens 00:12:16 Hey, are you okay with us… Creating our own metric for now, and then once this gets moving, we replace our existing metric with this one.
David Ashpole 00:12:29 I mean, either way, it's gonna block us stabilizing, right?
Arthur Silva Sens 00:12:33 No, if we declare… but if we declare our own magic… Yeah, we can… we can very quickly do this.
Like, less than a day, I have a PR open.
David Ashpole 00:12:50 I guess it's funny to me that implementing an experimental feature to satisfy a graduation requirement.
Arthur Silva Sens 00:12:58 Yeah. To get this.
David Ashpole 00:12:59 stable.
Look at, look, our stable stuff is behind the feature gate.
Arthur Silva Sens 00:13:04 So you can still…
David Ashpole 00:13:08 I'm not against it, if you want to do that.
I know… I know it's hard… to be patient when it's the only thing left. I don't think it's actually the only thing. I was trying to find our project board.
Is that linked from here, maybe?
Yes.
So we have your instrumentation scope, PR, And we still have to discuss… Whether we want to stabilize resource attributes or not.
Arthur Silva Sens 00:13:52 Hey, the instrumentation scope, I think the PR has, like, 4 approvals already. I'm just waiting for people to merge them.
David Ashpole 00:14:00 Prep.
Arthur Silva Sens 00:14:00 But the resource one, yeah, we can discuss that.
3 approvals.
David Ashpole 00:14:09 It would be helpful if someone else from this group approved as well, I think. Does anyone want to let me resolve this?
Oh.
It's this one, right?
Arthur Silva Sens 00:14:22 Yes.
David Ashpole 00:14:25 5004.
I'll make sure I grab the right thing.
Arthur Silva Sens 00:14:43 It's not in the place you put It's in compatibility, not on metrics.
No, no, there is a heater below called compatibility.
Yep, yep. This one goes to Companion.
David Ashpole 00:15:04 Good.
Arthur Silva Sens 00:15:05 Okay.
Arve Knudsen 00:15:17 So one other of us should, review this PR.
David Ashpole 00:15:22 Yes, did we ever… Let's see…
Arve Knudsen 00:15:25 I'm looking at the PR now for the first time.
I don't know if, Yeah, it wouldn'.
Arthur Silva Sens 00:15:36 We should, like, poke the TC again to update the Prometheus team.
David Ashpole 00:15:44 Yes. It might be, like, just a community issue or something we have to open.
Arthur Silva Sens 00:15:50 We should include people here, over there.
David Ashpole 00:15:54 maker.
Arve Knudsen 00:15:56 all the PR does is promote, It promotes to stable.
Arthur Silva Sens 00:16:03 Yeah.
Arve Knudsen 00:16:04 Okay, I'm not very familiar with the process.
Arthur Silva Sens 00:16:07 So the, so… For reviewers, look at the wording below.
And if anything needs to change, then you can say it so.
Arve Knudsen 00:16:20 Okay, I see. Okay, I'll try tributes.
Arthur Silva Sens 00:16:23 Thank you.
David Ashpole 00:16:40 Is this where people get added?
Arthur Silva Sens 00:17:14 What are you trying to do?
David Ashpole 00:17:17 Oh, I was trying to figure out where we define the group.
Sorry, I'll make a note, and I can do that later.
Awesome. Let's look at this.
Arthur Silva Sens 00:17:44 Yeah, to you… But one of my teammates… Review the whole documentation and compare it to the requirements?
To be… very transparent. She is, like, beginner with Prometheus.
So, she relies on AI a lot.
David Ashpole 00:18:09 That's totally fine.
Arthur Silva Sens 00:18:11 Yeah, yeah.
David Ashpole 00:18:13 I've gotten more used to AI output.
Awesome. So we have a few small things.
Arthur Silva Sens 00:18:26 Yeah, I've… I think… I think I remember some things that… We might need to double check.
For example, getting started. The collector… has a dollar or double dollars KP node for embedded Prometheus YAML. I have no idea what that is.
David Ashpole 00:18:46 Yeah, oh, well, so, often in… when you run the Prometheus server, you want to use regexes, right?
And dollar sign is an important regex key, but if you put a dollar sign in your Prometheus config.
the OpenTelemetry collector is like, huh, you want to look for the, like, environment variable 1, right? So it does environment variable substitution on your dollar signs.
So you need to escape it by putting two dollar signs in.
Arthur Silva Sens 00:19:15 Oh… Oh, wow. Because this is because the hotel collector supports environment variables, and Prometus doesn't?
David Ashpole 00:19:24 Yes.
So… You cannot copy-paste.
configs from Prometheus into OTEL.
And this is Creason. Yep.
There was a… there was a different issue about trying to, like, define sections of config that disallow environment variable substitution.
Bogdan had suggested that at one point.
But I don't know if it went anywhere.
Arthur Silva Sens 00:19:53 Cool.
Alright, so about this assessment, do we want to, like, create individual issues, or…
David Ashpole 00:20:02 I would like…
Arthur Silva Sens 00:20:02 I'm not willing to do this.
David Ashpole 00:20:04 I would like to go through and review it myself first, just to make sure before we make issues.
Unless you'd rather make the issues and then have people close them if they're not actually accurate.
Arthur Silva Sens 00:20:15 I think if we open issues, some LFX candidate will just start spamming GR. Yep.
David Ashpole 00:20:27 Yeah, I agree. So I'd… I'd rather, we read through this and try and confirm.
Arthur Silva Sens 00:20:36 Cool. I did a small… a small, like, a quick pass. I think most of it is correct.
But yeah, let's double check.
David Ashpole 00:20:54 Hmm.
And board review. So we've… we've already gone into… The main one… right, so there's still this stabilizing resource attribute. Why don't we leave this topic to the end?
And we'll go through and see if there's anything else we can… get through. So we have instrumentation scope, people are gonna review that.
That's it.
Those are the 3 items for the Prometheus receiver.
Which is awesome.
We have this…
Arthur Silva Sens 00:21:32 We should also write a blog post.
David Ashpole 00:21:35 Once it's stable? Yeah, for sure.
Arthur Silva Sens 00:21:37 Yeah, what's this table here?
Why the left?
David Ashpole 00:21:45 Me?
Arthur Silva Sens 00:21:46 Yeah.
David Ashpole 00:21:47 Oh, just the thought of writing a blog post about things that aren't stable yet. Something about… Everybody's been asking me to do blog posts on various things I've worked on. I'm like.
Arthur Silva Sens 00:21:59 Oh, okay, I see.
Yeah, yeah, but I… once it's stable, of course.
David Ashpole 00:22:05 So we have a lot left to do.
Understandably, in the exporter spec.
What about this one?
What is this?
Arthur Silva Sens 00:22:26 I think this is the…
David Ashpole 00:22:30 Okay, so Cryo's gonna work on… Native histogram, custom buckets.
Arthur Silva Sens 00:22:36 I mean, is this true… still true, Cryo? Do they have time for this?
krajo Krajcsovits 00:22:41 I haven't had time recently.
I'm trying to get out of a bunch of projects, I don't know when I will get to that.
To this.
Alright. But…
David Ashpole 00:22:57 Didn't we already do this one direction?
Arthur Silva Sens 00:23:02 Yeah, it's just the other way around.
David Ashpole 00:23:04 So it's just the reverse.
So we already… we already have a spec for going… because that was part of the Prometheus 2… OTLP spec.
Arthur Silva Sens 00:23:16 Jonathan, do you want to take this one? You've been doing a lot of native Instagram stuff as well.
Jonathan Santos 00:23:24 Can you tag me on the issue?
David Ashpole 00:23:29 Do you want me to change the assignee yet, or just tag you?
Jonathan Santos 00:23:33 Just tag me, yeah?
Arthur Silva Sens 00:23:37 That's.
Jonathan Santos 00:23:38 P. A…
Arthur Silva Sens 00:23:43 A PE.
Jonathan Santos 00:23:43 E.
B, E, B?
Arthur Silva Sens 00:23:50 You don't even know your handle, like, it's P…
Jonathan Santos 00:23:53 No, no, no, it's R… yeah.
David Ashpole 00:23:58 E-E-R.
Arthur Silva Sens 00:23:59 E.
B-A-J.
David Ashpole 00:24:05 curveball.
Doc?
Jonathan Santos 00:24:08 Yeah.
David Ashpole 00:24:10 Okay, you've been tagged.
Arthur Silva Sens 00:24:14 This is, this work is a little bit different from what you're doing, Jonathan. You've been mostly doing Go code that translates, native scripts. This is plain text.
You explain plain text, how this is translated.
Is that okay?
Jonathan Santos 00:24:36 What do you mean… what do you mean with plain text?
It's… it's just documentation?
Arthur Silva Sens 00:24:43 Yeah, it's a piece of documentation that explains how the translation happens.
So, SDK maintainers can implement what you write?
Jonathan Santos 00:24:55 Okay.
David Ashpole 00:25:00 So the remaining part is OTLP to Prometheus.
Which is funky, because… I guess this is going to be relevant when we talk about the Prometheus Remote Write V2 Exporter, because it has the choice of separate series, or CB&H, right?
Like, it could send a histogram as… Separate.
Individual series, or it could send…
krajo Krajcsovits 00:25:35 In promote, currently it's solved by having a config option.
So that you can choose. By default, it's classic histograms.
Arthur Silva Sens 00:25:47 So I've… do we need a configuration option for SDKs as well?
David Ashpole 00:25:56 Mmm.
krajo Krajcsovits 00:25:56 I would… Probably not. You want to do NHCB and then convert on the other end?
David Ashpole 00:26:05 Because NHCB is only really relevant for the for Prometheus Remote, right?
Okay, we don't have any scrape formats, or no, if you scrape the protobuf format, can you get an NHCB?
krajo Krajcsovits 00:26:24 Well, you can configure parameters to scrape classic histograms as an HCB.
But that's… that's not relevant, because we turned them into OTLP.
Stuff.
David Ashpole 00:27:09 And we do want it to default to… separate series.
krajo Krajcsovits 00:27:14 Yep.
That's the least surprising to people.
David Ashpole 00:27:20 Yeah.
Arthur Silva Sens 00:27:23 Okay, but… but then… what are we doing with this issue? Like, because…
David Ashpole 00:27:30 It needs to define how an OTLP histogram His mouth.
Arthur Silva Sens 00:27:36 The data model, right? Not the configuration.
David Ashpole 00:27:39 Yes. Well, it should say… So… Let me just, like, write some of this out. So, an OTLP histogram, Must.
krajo Krajcsovits 00:28:11 And I assume the first part is already covered, like, that's…
David Ashpole 00:28:14 Yes.
krajo Krajcsovits 00:28:15 That's already documented, right? Yeah, sure.
Also know that this is remote ride, too, only.
Like, you can only send… yeah, okay.
David Ashpole 00:28:43 And something like…
Arthur Silva Sens 00:28:51 The explanation histogram is a separate thing.
krajo Krajcsovits 00:28:56 Do what answer?
Arthur Silva Sens 00:28:58 the OTLP exponential histogram.
Is that a separate DC?
David Ashpole 00:29:03 Financial history, yes. Well, we already did… I don't think we stabilized it, but it exists. Like, the spec exists.
Arthur Silva Sens 00:29:10 Got it.
krajo Krajcsovits 00:29:13 I'm just trying to look it up right now.
Let's see… No, this is not it.
Where's it?
compatwerte.
Tos…
David Ashpole 00:29:35 Okay.
Hopefully that's a helpful starting point for whoever works on it.
krajo Krajcsovits 00:29:46 Yeah, looking at the current spec, it already talks about, obviously, the classical Rams, Hand those exponential histograms.
Status development.
Both of them are development status, so you can update within HCVM.
David Ashpole 00:30:05 Sounds good.
You're good.
krajo Krajcsovits 00:30:07 And Jonathan, you did some… code related to NHCP, right? I remember correctly, you are reviewing your code.
Jonathan Santos 00:30:15 Yeah, it was on the Prometheus remote right.
David Ashpole 00:30:23 Good luck.
krajo Krajcsovits 00:30:26 Yeah, that's a good foundation.
Arthur Silva Sens 00:30:35 I don't know how much of this still is a problem, because… this issue that you are looking now on, David, because, Java… has OpenMetrix 2 almost implemented already.
Yep. And they can switch to… To no translation mode, since… OpenMetrics 2 allows that.
David Ashpole 00:30:59 Right, it's, like, kind of… It's kind of funky, because obviously someone can still request Open Metrics 1, they can say, I would like no translation mode, and then they can send a query in that… asks for Open Metrics 1.
But…
Arthur Silva Sens 00:31:15 Yeah.
David Ashpole 00:31:16 Maybe at least the no translation mode makes sense now.
Arthur Silva Sens 00:31:20 But our spec says, The interaction between translation strategy and content negotiation? Is that content negotiation always.
David Ashpole 00:31:29 Yes.
Arthur Silva Sens 00:31:31 has higher priority.
David Ashpole 00:31:36 Yep.
Arthur Silva Sens 00:31:49 Yeah, so I don't know what to do with this one. Should we just close it, or… ask Gregor to give more… or updates.
Owen Williams (he/she) 00:32:01 so, he was sort of waiting for Open Metrics 2, And kind of didn't want to think about… Hotel.
So, we were… I was starting with, like, hey, here's Open Metrics 2, let's start with that.
And then… And then we can sort of revisit… translation modes.
But, like, we've done this in a number of other places, where it's like, if there's a backwards compatible thing that doesn't match the new standard, then you have flags, and you can have your… You can do whatever you want, you can have your default be, You know, the old thing, and then you have a flag to do-do thing, or the other way around, you know.
It's sort of… Up to them.
Yeah, I think the key comment is users usually want to control translation on the ingestion side rather than scrape time.
So, in other words.
he would like more content negotiation to determine how these things get set, and I've always resisted that, because I feel like that's encoding… open telemetry logic into Prometheus, you know, into the Prometheus, like, scrape protocol.
Which I feel like is out of scope. And… and a bad precedent, because then everybody If there were other… protocols, then they're all starting to embed their own business logic into the Prometheus Scrape protocol.
David Ashpole 00:33:34 I don't… I don't necessarily agree with that, just because, like, the feature is UTF-8 support.
And… even if OpenTelemetry didn't exist, we could think about the UTF-8 feature, and… If someone gives you a bunch of emojis, You have to.
Owen Williams (he/she) 00:33:51 Exactly.
David Ashpole 00:33:51 What to do with it, and, like, that can be completely, like, scoped to… Prometheus, and have nothing to do with OpenTelemetry, if we want to think about it that way.
Owen Williams (he/she) 00:34:03 Yep.
David Ashpole 00:34:04 Okay.
Owen Williams (he/she) 00:34:04 It's true. I guess, yeah, I guess if it's a generic… this is how you treat multiple… like, do you… do you collapse underscores or not? That could be considered a generic enough option.
David Ashpole 00:34:24 Let's discussed August 2025.
Owen Williams (he/she) 00:34:34 Now the problem converted.
So, now the problem converter in Java SDK doesn't change ampersand and Ampersand to a single underscore anymore.
Because the underscore escaping has done it.
Scrape time.
David Ashpole 00:35:02 Oh, because UTF-8… UTF-8 is negotiated, right?
Owen Williams (he/she) 00:35:08 Yes.
do you allow UTF-8 or no? And so…
David Ashpole 00:35:16 Why is this a breaking change in clients?
Arthur Silva Sens 00:35:21 Like, before double percent signs became one underscore, but they are now becoming two underscores.
David Ashpole 00:35:32 Oh, is this because the… Is this because the spec… That we have here.
And…
Owen Williams (he/she) 00:35:40 See you here.
David Ashpole 00:35:41 escaping that you defined, Owen has different behavior?
Owen Williams (he/she) 00:35:46 Could… That could be. I mean, to me, this is a conflict between, are you exposing UTF-8 and then relying… and then… Relying, and then during content negotiation… basically, it's, yeah, it's… it's the difference between pre-escaping and automatic escaping. So the idea is… I think the least desirable scenario is the one he's describing, where I'm exposing UTF-8 by default, and then content negotiation says, I don't want you at UTF-8, and then you just get a default translation of that.
And really, what you should do is if… if your scraper doesn't support UTF-8, you do your translation ahead of time and give it exactly what you want to give it, whether that's multiple underscores or single underscore. Does that make sense?
David Ashpole 00:36:42 Just… weird.
Owen Williams (he/she) 00:36:53 To put it another way, there's so many different ways to do translation.
And right now, the content negotiation is just, I accept UTF-8 or not. And it doesn't… there's no… there's no way to… yeah, you'd have to have all these new headers, which I don't… I don't particularly want to do, because there's another solution, which is you define how you want to do the escaping.
On the other end.
David Ashpole 00:37:25 I'm so bad at reading Java code.
Owen Williams (he/she) 00:37:31 I, I think, I think maybe we sort of say, hey.
Open Metrics 2 is out, does this change anything? Or maybe ask… does he… does he even propose, like.
What he really wants.
Like, he just says users usually want this, and it's… I think we can make a little, like, what are you actually asking? Like, what do you… you're just… it feels like he's just stating, here's a problem.
And I want a more concrete thing to talk about, which is like, okay, how are you proposing we solve that problem? Are you talking about new headers? Are you talking about new flags? And that maybe will make this discussion, because I think right now we're just trying to guess, like.
What do you… what do you actually want?
So it's like, okay, sure, there's this problem here.
but we're not seeing this elsewhere because we've added these flags and done it in this way. Are you saying that you want control over the translation process?
at… negotiation time? Like, what do you… what do you want?
That's… that's how I'm reading it.
David Ashpole 00:39:09 Okay.
Otherwise, I think we're done on this board.
Let's see, we have 20 minutes left.
Hmm.
Lumber.
Target.
Remember, there being this many sections.
Arthur Silva Sens 00:39:46 There's a… a configuration in the SDK that does not include Scope attributes to the labels.
David Ashpole 00:39:58 You know, I just… It's more like I looked at this doc.
And then looked at the list of open issues and was like.
This is… this is… no, this is actually the whole… This is actually for the whole, compatibility spec, right?
This is not just for the export page. Okay.
Arthur Silva Sens 00:40:29 So it is both OTLP to Prometheus, and also the configuration options for the SDKs.
David Ashpole 00:40:36 Okay.
Let's see if we can move some more stuff to workable from discussion needed. I think that would be a useful use of our time.
Arthur Silva Sens 00:40:44 Yep.
David Ashpole 00:40:45 Okay.
Arthur Silva Sens 00:40:47 Oh, hello, Braden.
Braydon Kains (Google) 00:40:50 Hi, I just wanted to see if there was a… if there was a minute here, because I saw all the share requests on my document and figured that it was probably being discussed in a meeting.
David Ashpole 00:40:59 Sniffed us out.
Braydon Kains (Google) 00:41:00 I'm wondering if there was anything… any questions you had for me on it, or… Any discussion that would be relevant for me to know?
David Ashpole 00:41:11 I think we did go over it.
Most of our discussion was about How soon we think it's going to land, because this is one of the last remaining items to mark.
ourselves stable. So we were trying to decide between waiting for this to land, and alternatively adding a different self-observability metric to capture The partially… failed, points that we weren't able to translate. So, that was what most of our discussion revolved around. I think we're just very supportive of the feature, obviously, but I don't… I'll let others speak, but I don't think there were any strong opinions about any of the design decisions that you're trying to evaluate.
Arthur Silva Sens 00:41:59 Oh, since most of the people here didn't have access, we didn't go through very deeply.
Braydon Kains (Google) 00:42:05 Yeah, sorry, I got… I got home only, like, like, 10 minutes after this meeting apparently started, so I… I didn't share it with everyone right away, but… The hard part about me pushing this forward is mostly just that it's Deeply intertwined with just general… Confusion around the exact words to use, or, like, the exact error scenarios we're trying to be able to track.
And I think… People were… concerned that I was, like, trying to… Measure something that is hard to measure, and that they've been trying to measure for a long time that is challenging, mainly that, like, figuring out exactly how much data is dropping where throughout the pipeline.
And I have been trying to say largely that, like.
I understand that that's confusing, but I mostly just want to introduce this API because it's necessary. But I'm still… I'm trying to settle it from… from both angles.
Arthur Silva Sens 00:43:04 Hi, one question. I saw that there was discussions between using the word, refused versus rejected.
Braydon Kains (Google) 00:43:13 Yeah.
Arthur Silva Sens 00:43:14 Is this… really a concern? Like, choosing different words has different behaviors, or is this somebody nitpicking?
Braydon Kains (Google) 00:43:24 It's… It's that… So, maybe I'm nitpicking a little bit, but there's… the… the… two different, disparate parties chose different words for the same things, and now they're colliding, is essentially what's happening. But the receiver new metrics chose the word refused.
And… the partial success in the OTLP protocol chose rejected.
And so now, it's like, how do we… Make clear within… Someone just holistically looking at the collector self-metrics, why one word is used somewhere and one word is used somewhere else.
Arthur Silva Sens 00:44:01 Like, every metric has a description, and the description is a longer task that explains what this metric is about.
I would expect people to read the metric description if they want to understand.
Braydon Kains (Google) 00:44:14 Yeah, probably.
Arthur Silva Sens 00:44:16 I would… I don't think people will care if it's called refused or rejected.
Braydon Kains (Google) 00:44:21 I think the other thing is that… I, I think, I think the other, the other thing is that, people… Want a distinction want to keep the word refused and rejected separate because they want a distinction between a point, or an item was sent.
And rejected by the backend, versus it failed at the exporter level because something was wrong with the format.
David Ashpole 00:44:49 But which would meet which?
Braydon Kains (Google) 00:44:51 That is… that's the problem.
David Ashpole 00:44:54 Like, they both sound like the backend said no.
Braydon Kains (Google) 00:44:57 They, they do both sound like the same thing.
David Ashpole 00:45:00 In the past, we've used, like, Dropped or something.
When it's… I think processes… A lot of the…
Braydon Kains (Google) 00:45:12 They're using failed a lot in the self-metrics, like, failed items.
David Ashpole 00:45:18 Even in the process.
Braydon Kains (Google) 00:45:19 Science Twitter.
I don't remember offhand.
David Ashpole 00:45:26 That's okay, that's okay.
Braydon Kains (Google) 00:45:27 Yeah.
Arthur Silva Sens 00:45:27 the metric… won't the metric have, an attribute, or a label, whatever you want to call it? Like, error type, or reason for refused, or reason for rejection?
Wouldn't that be enough?
I mean, enough to differentiate the two cases you said.
Braydon Kains (Google) 00:45:56 Yeah.
Possibly.
Arthur Silva Sens 00:46:05 Yeah, I mean, I… if this, like, choosing the right word is very important to you, like, I, of course, want to give you the time, but… But I feel like we can solve this in different ways, and I don't know. Feels a little bit awkward to wait.
So long, just because we can't decide on the name of the metric.
Braydon Kains (Google) 00:46:31 Well, I… I have… felt that as well, because the number one thing I want is just to be able to introduce this as a capability in consumer errors, like, be able to report account.
like, the reason that hasn't been pushed through is because of the concerns around the names of the metrics that are actually going to be used. So that's why now I'm… I'm forcing myself to care, so that we… I can, like.
Push it.
Arthur Silva Sens 00:46:55 Yep.
David Ashpole 00:46:56 are they actually not orthogonal? Like, can you not just introduce a new error type and consumer error?
I tried…
Braydon Kains (Google) 00:47:03 to… I tried to…
David Ashpole 00:47:04 Tried to do that.
Braydon Kains (Google) 00:47:05 Okay.
David Ashpole 00:47:12 Interesting. Okay.
who… who are the… who are the decision makers here? Like, who's… who… not… I'm not asking you to call people out, but more like… If, if we want to help.
What discussions should we be a part of?
Who are the people who are, like.
Gatekeeping, or just making decisions on the self-observability metric.
James.
Braydon Kains (Google) 00:47:35 We have been talking about it mostly at the collector stability meetings, which is… Okay, one on Mondays. Yeah, a Monday meeting that's only for collector leads.
we probably could talk about it at a general collector SIG, but… I cannot usually attend that time slot, so I don't go to those.
Arthur Silva Sens 00:47:55 I can't either.
I can make it on Monday.
David Ashpole 00:47:59 Yep, I'll be there on Monday, so maybe…
Braydon Kains (Google) 00:48:01 Maybe.
David Ashpole 00:48:01 I can help.
Arthur Silva Sens 00:48:04 Yeah, sounds good.
Braydon Kains (Google) 00:48:05 Sure. We can talk about it Monday, then.
I did… I did try and straighten… some of this stuff out, because I think… I think a lot of, like.
the way I pitched this originally was that I wanted to be able to count partial success. Like, this all started because like… in the Google Cloud Exporter specifically, we have a specific spot where we count.
partially failed ones, and we wanted the OTLP exporter to be able to do it, too. And that's all… that's where this all started, but then… it cascaded into a whole, like, exactly what the design of these self… I think maybe things are just being… conflated with, like, my… what I feel is a relatively simple need.
So… It would probably help if you guys were there to help straighten out exactly what the… because I think there was also confusion about why, why Prometheus receiver cared about this, and I tried to clear that up, to my understanding, but…
David Ashpole 00:49:03 Yeah, I mean, for us, Right, we can talk about it on Monday, it sounds like.
Arthur Silva Sens 00:49:11 But, to summarize, when we scrape a page.
There are a few metrics that cannot be translated to OTLP.
And some can.
So, we translate what we can, and we draw what we cannot.
Braydon Kains (Google) 00:49:25 Right.
That makes sense.
Okay, well, I will, I'll add it to the agenda of that meeting now, so that we ensure that there's… that it's being discussed, and if you guys can make it and help out, that would be good. I did also, separate from that RFC draft, I did make A gist, just sort of explaining my understanding of how the… Collector maintainers are trying to… like, what exact error scenarios they're trying to track, and why this is, like, why it's confusing right now.
So that… I linked that in the RFC as well, so if people want to look at that, that might help inform the discussion a little bit.
Arthur Silva Sens 00:50:13 Sounds good.
David Ashpole 00:50:15 Good.
Braydon Kains (Google) 00:50:15 Alright, I'll drop now, but, thank you for taking a look.
David Ashpole 00:50:19 Yeah, thanks, Braden.
Arthur Silva Sens 00:50:21 Bye, mate.
Oops, alright.
Where were we?
David Ashpole 00:50:33 I'm… Sorry, I've been moving on along during that discussion. Everyone can still see my screen, right?
Arthur Silva Sens 00:50:40 Yes.
David Ashpole 00:50:44 So I've been going through the… Is this the right one? Yes. I've been just going through these issues here and trying to mark them as, workable.
So this… this is the resource one. I do think for… this is for SDK exporters. I think this is going to be blocked on entities stabilizing. I don't think we'll be able to block… to have target info metrics enabled by default.
Arthur Silva Sens 00:51:15 I… Maybe we can, but I, I, like, this needs to be discussed.
David Ashpole 00:51:22 Okay.
Arthur Silva Sens 00:51:28 So the… Isn't this related to the other PR you're doing, David, for the…
David Ashpole 00:51:36 Soda.
Arthur Silva Sens 00:51:36 Prometheus.job.
David Ashpole 00:51:39 the, sub… I think it's… I'll repeat what I said, I think, last meeting, but I think it's going to be easier for us to stabilize the resource handling logic in the Prometheus receiver, because it's easy for us to introduce something new and continue to support the old one.
I think it's harder for us to stabilize target info in the Prometheus SDK exporters, because once we… Have a particular behavior, we won't be able to change it easily.
Arthur Silva Sens 00:52:08 Yeah, yep.
David Ashpole 00:52:11 This is the… OTLP to Prometheus part of it.
And I feel like we at least need to ask the entities group to stabilize parts of the data model.
And then we need to decide how we're going to interact with entities.
At least But that it impacts target info.
Arthur Silva Sens 00:52:33 My worry here is that, the collector group says that they cannot release Collector V1 until we stabilize the primitives Exporter spec.
And then if we depend on entities, now collectors also depend on entities.
David Ashpole 00:52:52 Let me… Is this even… Examples… does this even define…
krajo Krajcsovits 00:54:06 Are you looking for how it's going to look in the OTRP, or what are you looking for?
David Ashpole 00:54:09 No, no, no, I just… I just want something that we can build on, that we… will be stable. Like, otherwise… The exercise is useful to figure out how we're gonna make it work, but…
krajo Krajcsovits 00:54:25 make what work. I mean, in my head, entities… At this stage, just say that Here are your identifying attributes, here are your descriptive attributes, but doesn't actually say, like, how are you going to use them.
So it's… kind of hard to build anything on it. I mean, it certainly would help us No.
Identifying from descriptive, but beyond that, it's just… It's not very helpful.
David Ashpole 00:54:58 Well… So there's a related problem.
Where… having… I… actually, maybe Arv can tell me if this is fixed, but my understanding is that if you have A label on your target infometric.
That is descriptive, and changes frequently.
That that wreaks havoc on all of your queries today.
Because you get new target info series relatively frequently.
I thought we even had some, like, logic to extend target info out.
Maybe.
You can respond.
Arve Knudsen 00:55:43 Yep.
krajo Krajcsovits 00:55:43 Sorry.
Arve Knudsen 00:55:44 I don't think that in general would wreak havoc on your queries. I think… Because usually, you just join with the job and instance labels, on-target info.
So, and they… they will be… they should be stable.
David Ashpole 00:56:05 Okay.
Arve Knudsen 00:56:05 Do you have… do you have, like, a specific example in… in mind?
David Ashpole 00:56:10 No, no, sorry, I'm… Trying to page back in some of the stuff that we had talked about with respect to, I feel like it's in one of Bjorn's documents somewhere, but I thought that it was a problem that target info contained.
Arve Knudsen 00:56:27 Maybe…
David Ashpole 00:56:28 Obtained labels that could change.
In some cases, but I don't remember.
Arve Knudsen 00:56:32 Maybe, maybe you're… Thinking of the fact that, joined queries can fail as a result of this, because you have You temporarily have, overlapping target info series?
Is that sort of, like, the corner case you have in mind, David?
David Ashpole 00:56:55 Sounds like a dog.
Arthur Silva Sens 00:56:55 Yeah, I think… I think that's the problem, yeah.
Arve Knudsen 00:56:58 But, if that's the exact corner case you have in mind, it's actually fixed by the… using the… the info from QL function.
David Ashpole 00:57:07 Okay.
Arve Knudsen 00:57:08 Because it doesn't… it doesn't stop, it doesn't suffer from this, this, failure, how do I say?
It doesn't failure to this one… sorry, it doesn't suffer from this, One too many, join… join problem.
David Ashpole 00:57:26 Interesting.
Arve Knudsen 00:57:26 It will, it, it, it actually intelligently fixes… sorry.
It, it intelligently picks the… the newest target info series with those, identifying labels.
David Ashpole 00:57:44 I'll let Cryo talk, because he's had to stand up.
krajo Krajcsovits 00:57:47 Yeah, I'm… I'm a little bit confused, like, how is the entity SIG, or… the OTA spec is going to solve issues in Prometus. That's kind of a weird… Maybe I'm misunderstanding it, but… yeah?
Arthur Silva Sens 00:58:03 I can clarify, like, one example is, I think ARV has been battling with, databases, receivers in the collector, or one Postgres receiver, for example, that monitors Two different, databases.
It is expected… there's some problems there where it is expected a unique service instant ID.
But the database… the maintainers don't consider a Postgres database a service, so they do not include service insert AD.
And but they could include, for example, Postgres database ID, something, I don't know, something that identifies uniquely a database.
And then this will use the… the attributes from the database entity, not the service entity.
And target info depends on the service attributes, not on Postgres, whatever attributes.
Arve Knudsen 00:59:11 I wonder if the… let me see… I think, actually, the PostgreSQL receiver, it does send service instance ID, it's just that it's not identifying.
Arthur Silva Sens 00:59:28 Got it.
Arve Knudsen 00:59:29 It's like, I'm looking at the PR now, I think, I think with that particular receiver, the problem is that They've, I think they've modelled it so that… The modeling is, is difficult there.
what were they doing again? I think… I think they have… Several different, resources with the same identifier.
But I'm not sure… I'm not sure how it's sort of, like.
How it ident… how it exemplifies the problem you were talking about, originally.
Arthur Silva Sens 01:00:13 So, you think… Yeah, I don't recall… 100%, but I… this problem that I said, that some place, some… some stuff.
Are not considered a service, and those labels aren't… those attributes aren't present.
I thought I… I saw some comments like this.
Arve Knudsen 01:00:33 I think the host metrics receiver is an example.
Arthur Silva Sens 01:00:40 they do not add service instance ID.
Arve Knudsen 01:00:43 I think so. I think there I have… I'm in a discussion with Braden and others.
About, the fact that service.instanceID is used by Prometheus.
So, even… I think they're sort of coming around to the fact that this resource attributes is necessary for compatibility with the Prometheus OTLP endpoint.
So the… the problem… yeah, so the problem with host metrics is that, when Prometheus receives those metrics, it cannot generate, target… the target info metric, because it… It doesn't have any of the identifying research attributes.
But then, with the Postgres, Postgres receiver, it's sort of even worse, because Because it does receive service.instances.id, but it's not unique.
David Ashpole 01:01:46 We are at time.
Arthur Silva Sens 01:01:48 Yeah.
David Ashpole 01:01:49 Cryo, do you want to say one more thing before we drop?
krajo Krajcsovits 01:01:51 No, we can talk in two weeks' time.
That's fine.
David Ashpole 01:01:58 I will…
Arthur Silva Sens 01:02:02 But I think the discussion was worthy.
And we realized this is really, really hard.
David Ashpole 01:02:15 Alright, well… Till next time, then. Thanks, everyone, for joining.
Bye-bye.
krajo Krajcsovits 01:02:21 Right.
