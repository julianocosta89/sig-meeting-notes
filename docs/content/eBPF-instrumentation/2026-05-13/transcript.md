SIG: eBPF instrumentation
Date: 2026-05-13
Duration: 93 minutes
Zoom Recording URL: https://zoom.us/rec/share/1C-r90-V2LJsGYXDNwPecRKgYspXxwCkP2RoW4P4aaxSa4FB7FmMdkOosGrnAHnV.3impmtJLOeGMhU2O
============================================================

## Zoom Recording Transcript

Mattia Meleleo 00:00:22 Hello, Mike.
Tyler 00:00:51 Hey, how y'all doing?
Rafael Roquetto 00:00:55 Good, how are you? How are you guys doing?
Oh, sorry, Mike.
Tyler 00:01:10 What's up?
Rafael Roquetto 00:01:11 No, no, race condition with Mike, putting the names on.
Tyler 00:01:15 Oh, oh, I guess.
Awesome. Looks like people are filtering in. If you haven't yet, please go ahead and add your name to the attendees list, and if you have agenda items you want to talk about, go ahead and add them there as well, and then… Yeah, we can jump in here in just a second, get started.
Awesome. Okay. Welcome, everyone.
Okay, so to start us off, I just wanted to call out, just a point of order, I am going to be out, the next two weeks. Is there someone on the call who's able to lead these meetings in the next two weeks?
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:45 I don't mind doing it.
But if somebody else wants to, yep.
They can share the responsibility.
Tyler 00:02:53 Awesome.
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:54 Going somewhere fun.
Tyler 00:02:56 Yeah, I'm headed off to Colorado for a little bit, so… Oh, nice. Different time zone. I think I'm in Raphael's, time side at that point, so, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:03:04 Right.
Tyler 00:03:05 Yeah.
So, yeah, should be fun. I'm not, like, completely gone, but I'm gonna be extremely slow to any sort of responses and don't expect a lot of reviews kind of thing, but, Yeah, should have a phone, I guess, is what I'm saying.
Rafael Roquetto 00:03:20 This is the most fun time zone. Welcome.
Tyler 00:03:26 Yeah, I used to live in it, I'm all about it, so yeah.
Okay, cool.
Awesome, so moving on then, Nicola, you want to talk about supporting log enrichment for non-JSON logs?
Nikola Grcevski @ Grafana / OpenTelemetry 00:03:39 Yeah, I just wanted to bring it up here. That's a pretty cool feature, but, Especially, like, I was looking at, say, for… Some of these kind of more legacy applications, where they Right, they want to have the long enrichment, but they're just sprint to stand it out.
you have to consider something like a Java application that's not using Log4J, which is what we would be targeting, like, something that's, I don't know, doing system out print line.
likely will not be in JSON.
So, I just wanted to bring it up and see what… I know there are some discussions around this, in the Slack channels, but async, but I just wanted to bring it up and see what people thought. Is there, like, a realm of possibility where we can actually make this happen?
nimrodavni 00:04:33 I think, why we decided to start… at least start with Jason is because Like, appending it to any unstructured output can… like, you can add it to stuff that are not even logs.
printed out to FTD out? Like, I don't know. Example, like, you have, like, I don't know, some applications that print out some stuff at the start, or… I don't know.
Nikola Grcevski @ Grafana / OpenTelemetry 00:04:55 Hmm.
nimrodavni 00:04:55 maybe stuff that are not logs, or even if they are logs, but you just, I don't know, they have different formats of, like, how do you add attributes, and you have, like… Do you add it with equal? What's the separator? What's the whatever? And… like we said, okay, we don't want to get into it for now, but if we… so I… I thought maybe… trying to get some structured text stuff, like text formats, at least that's a couple of families. If you want, like, completely, like, everything that prints to STDL, just append the trace ID at the end.
without any format, that can be possible, but it might break, like, parser after it, and, like, if you have You probably want them to somehow parse it.
That's, like, what we… at least what we thought, I think.
Oh, and so… Nikola Grcevski @ Grafana / OpenTelemetry 00:05:47 Yeah, no.
Mattia Meleleo 00:05:47 To add to that, there is, there are multi-line logs, exceptions, panics, stuff like that.
Which I'm not sure how we should handle.
Rafael Roquetto 00:06:00 Maybe some… some… something… I mean, I don't know, multi… so multi-line lots… You mean, like, literally a lot of new line characters in, In the sense that… All these lines, they kind of refer to the same context, but it…
Mattia Meleleo 00:06:17 Yeah, I remember there are some Java apps, that instead of putting a log line, a single line, they put, like, a blob big like this, with a lot of logs in there.
Rafael Roquetto 00:06:31 I mean… Maybe I'm simplifying this, and you guys have thought about this way more than I have, I'm just thinking out loud.
maybe we can start small, in the sense that we can, for now, not, not think of the semantics per se, just think for known JSON logs.
for each line, so not for each log, contextual log line, but just for every line. CS slash N, we can start by appending, like, TracyDspend ID, like, in brackets or something. We make this optional, so disabled by default, so people can enable this, and then maybe… maybe after… we're gonna have to trade this, and this is what you guys are talking about, I guess?
we can kind of try to add, like, rules with RAGX. I'm thinking something out loud where you can say, like, match rule, and then where you insert after the match rule, but this is the more complicated, work, so I don't even know if that's really feasible, but… maybe… maybe starting with, like, just one, one form, one, like, trace ID, span ID per line, and we can then later do another, like, iterate this, start with the, like, fixed Within brackets, prepaid with, I don't know, OB span ID, OB trace ID, leave it disabled, then next situation becomes, okay, can we let the user format that, and then can we let the user filter lines, so just, they can filter lines, like.
iterate this to the point where it gets really cool, but maybe we can do, like, baby steps, and if we never get to the cool part.
We still have, like, opt-in functionality where, you know, maybe some people might find it useful, and for those who need something extra, we can tell them, look, we don't support that because of A, B, and C, or maybe we can look into it again, or… I don't know. Maybe we'll have nothing to lose by doing it like that. Just a thought.
Mattia Meleleo 00:08:24 Yeah, definitely, that's a way to start.
Nikola Grcevski @ Grafana / OpenTelemetry 00:08:27 Yeah, I was thinking about this, like, because I agree with, you know, you just have an application start, and it just writes all sorts of junk, right? But that will not have a trace ID, right? That will be, like.
startup. It's not related to any HTTP transaction or anything like that. So, then we won't print it. But anything else… We can just prepend it.
I'm front with square brackets, so it's just put trace ID, span ID, or whatever.
If we have it. And I think it will go a long way, because it's really… I'm thinking here is, like, if an application is already doing JSON, they probably may have actually put in some trace ID. Like, they've… it's probably a modern… application. I honestly looked at the, the OTEL demo, and there's, like, tons of them that we could not handle. They could just do… Random, simple, plain text logs.
And… Yeah, so, like, and I get your point about the exception. I don't know what to do there, because do we put it at every new line?
It will look ugly.
But…
Rafael Roquetto 00:09:41 Well, if you're preparing it with, like, you're seeing with the square brackets, it just looks like… I mean, nothing looks pretty.
But it's gonna be like what we have in Dmask or TracePipe, where we have this column that's always the same, and the log is to the right, so maybe it's not that bad. And maybe we only pretend it to standard output, so I don't know where the… which I guess is already the case.
I don't know where these, Yes, exactly, my tea.
Nikola Grcevski @ Grafana / OpenTelemetry 00:10:10 Something like that.
Rafael Roquetto 00:10:13 And then I don't know where, like, stacks end up, if they go to a standard error instead, but it doesn't… maybe it doesn't matter. And, like, because it's up to you.
Maybe it's, like, 80% good enough for people and for the rest.
I don't know.
Nikola Grcevski @ Grafana / OpenTelemetry 00:10:26 Yeah, I mean, I would have taken it. I have a random exception in Java I would have taken if I knew what trace ID that was from, so… So I can track the transaction.
Rafael Roquetto 00:10:36 Prepending makes it easy for your… for any other, like, someone post-processing the log to kind of strip it, because it's always the same width, or, like, fixed length. We can just, like, filter that out, and you end up with the original log again, unlike in the end, which is going to be variable length, so… maybe, maybe we could do something.
Nikola Grcevski @ Grafana / OpenTelemetry 00:10:54 Yeah, I actually like that idea. If it's… if it's a, like, a prefix, I mean, that is of standard size, then you can easily strip it with log rooms. And make it optional, obviously.
Tyler 00:11:07 Yes, I think about a few things there.
I would start with how you're gonna use it, I think, more than, I think, how we're gonna accomplish it.
Because, like, if you're gonna use it just by reading it.
That'd be one thing, but I don't think that that's actually the case, right? Like, I'm sure you're gonna, like, try to get this into your… some sort of, like, tooling in, like, your backend.
Yeah. Do some sort of, like, actual linking, and so… Yeah, that, I think, is… I think that use case needs to be, like, understood, because if this needs to be, like, in a specific format, I think prepending makes a lot of sense, like you guys are talking about.
But if, like, the backend's also expecting a timestamp, in its parsing.
Nikola Grcevski @ Grafana / OpenTelemetry 00:11:50 Patrick or something.
Tyler 00:11:50 Something like that?
to be the… to be the first thing that it sees, like, that makes it harder. If you're not appending… if you're not prepending the trace ID to every line, that also has inconsistent parsing at that point. You'd have to essentially start prepending, like, stubs or something like that to make it consistent.
or not, like, it really depends on, like, your background parsing. I think the other option of, like, having users provide regexes and stuff is, like, really helpful, but, like, there's a point where you just start to become, like, a log processing tool instead of, like… you know, Obi at that point, right? And so… Yeah, I think this is all great, I think this is a great brainstorm, but, like, I'd really want to understand, like, the use case first, and understand, like, you know, if we do send this to I don't know, open source tools, or to… vendors, like, how does this show up? How are they gonna be able to process this?
And so, like, if they can process it in one form.
but not another, we should try to target that one form. If they cannot process, like, a particular form, like.
Or it's gonna cause, like, log ingestion to fail? Like, that's definitely something we should consider as well.
nimrodavni 00:13:11 I think we can, like Matthia recently did, because, currently we had an issue.
where we… like, how the login work is basically you replace everything with null s, and you just append the TracePen ID, because you need to overwrite the buffer. And in that case, like, at least in CoreLogix, maybe other platforms as well, it was appearing as… like, you could actually see the, like, the null bytes in the log, and we did… we basically added an example, I think it was approved, Mattia, right? Like, of, like, the.
Mattia Meleleo 00:13:43 I think it's still in a PR state, yeah, I…
nimrodavni 00:13:49 It's like a collector config to basically, like, we change the… like, to separate it into different logs, and just drop the null … only the null logs, and then you have, like, a clean type of log.
Mattia Meleleo 00:14:03 That's only an issue in the case of a pipe, because the automatically deletes the notes, but the pipe sees everything.
Because you put the number of bytes that should go in there.
nimrodavni 00:14:16 Oh.
Mattia Meleleo 00:14:17 But the log shippers, if you put a simple rule, like remove new lines, and you put a new line before putting the real data, then it's easier to… fulfillment.
Tyler 00:14:31 The log shipper, you mean, like, collector here?
Mattia Meleleo 00:14:35 Collector, yes.
Tyler 00:14:36 Yeah, okay.
nimrodavni 00:14:36 You know what I'm…
Mattia Meleleo 00:14:37 collector…
nimrodavni 00:14:37 Excellent.
Mattia Meleleo 00:14:38 Dior.
nimrodavni 00:14:39 Yeah, for at least, like, the collector, maybe other stuff we can… add some sort of rule that kind of extracts this, like, start prefix into, like, actual attributes. If you go through Otel Collector, or let's say we have one for a couple of log… there's, like, infinite, probably, log shippers, but… I don't know if we have, like, the… a couple of examples, maybe we can say, okay, you can enable this feature, and if you want to parse it into, like, a stateful… not stateful, like, a very structured thing, you can take this and put it as a rule.
Tyler 00:15:15 Yeah, I think… I think that's kind of, like, that'd be great. I think maybe getting that answer, especially for the collector, right? Because I think, like, once you get into the collector and you parse it into a stable state, you can… do other translations and send it to other places. So I think if we can target that, and target to some degree… natively, it'd be great if you just, like, the collector just worked. If you have to configure the collector additionally to parse these sort of things, that's… not as ideal, but it's something that we could do. But I think this is probably the way to look at trying to resolve this.
Rafael Roquetto 00:15:46 And, aside of that, more, like, into the implementation side, I agree with that, like, we gotta check, but if we decide to go ahead, I was just thinking in the meantime.
what we could do to make this really flexible, excuse me, is… I mean, a mix of, it's using regular expressions, to match. If you want to match, okay, there are two aspects of it. Where you want to put these, This prefix, like, we could start with, like.
with the prefix, as, Mattia typed on the chat. But, if you think of your, your, Unix command line, you know, and your prompt where you can, everyone just tunes it, and you have, like, placeholders, we can just have, like, a placeholder for span ID, Tracy, same thing like the Unix command line, so it lets you render or customize this the way you want, and seems it's very straightforward to implement. And then as a second interaction, I mean, you could just do literally… regular expression on the line. I mean, probably won't scale, I'm not sure it's expensive, so it's, just an idea, not sure if it will scale in real life, where we can literally search and, like, mesh and replace, you can capture things, and it lets you rewrite the logline, and then you can insert the span ID or the trace ID wherever you want.
on the, on the template, just like, you know, the S command on VIM, or something like that, you know, like, it would just be, like, a regex. Might be expensive, though, for if you're running this for every logline, so…
Mattia Meleleo 00:17:15 Yeah, basically…
Rafael Roquetto 00:17:16 Do you have it?
Mattia Meleleo 00:17:17 Basically, specifying the format, but .
Rafael Roquetto 00:17:19 Yeah.
Mattia Meleleo 00:17:20 What's… I mean, I think… I think it would not be that expensive, but the issue is that you would need to specify the format for every app in your cluster, and I think most people don't… don't want to do that, or… We're too lazy.
Nikola Grcevski @ Grafana / OpenTelemetry 00:17:35 Yeah.
Mattia Meleleo 00:17:35 To the LVR.
nimrodavni 00:17:37 If we have, like, Like, going back to the start, if we have, like, a set of formats that we choose that are, like, kind of standard, we can do some auto-detection per service of, like, this is the format that we see, and by that, select how we inject it. If it's a JSON, it's a common log format, it's a whatever.
Stephen Lang 00:17:59 The trouble is that when you have exceptions and multi-line stack traces and things like that, they break the format, so it's not necessarily one format for a service.
nimrodavni 00:18:09 So I guess maybe if we have, like, stack traces and stuff like that, they might not even be considered logs, and we can say, like, that's just something we don't know.
Tyler 00:18:22 Yeah, but, I mean, that was, like, Nicola's point you wanted to trace for that one, right? Like… Nikola Grcevski @ Grafana / OpenTelemetry 00:18:27 Yeah, so how about… I mean, I understand that this will break other, like, tools that implement, like, processors and whatever, which maybe is, like, we choose the default format as we're gonna print this.
If we decide to do it, and then people can change the default format?
To whatever they match. And it maybe could be done per service, As a… in the selectors?
So, you can say, I'm using this kind of tool, and I know this particular… not putting the square brackets.
work for me. So just adding a simple prefix, trace ID equals, so trace ID colon, I can just choose that.
And then, if the default that we introduced breaks you, you can modify it, and it's flexible.
And you may not want the span ID, you don't put that, so the default format will be square brackets, trace ID equals percent.
T… I don't know.
span ID equals %s, and then close square bracket, but you can just modify it.
Rafael Roquetto 00:19:32 So it's all about providing mechanism, but with defaults, Aurora, right? So people can pick some templates or whatever, auto-detect, I don't know, but the implementation itself is… under the hood, it's flexible, you know, if you want to extend it, do something custom later.
Nikola Grcevski @ Grafana / OpenTelemetry 00:19:50 So that, if you have a vendor, and this is what breaks you, then… or we can choose one that doesn't break vendors, I think. I just want the trace ID in the logs in one way or another, if it… so that people can search for it.
Because especially, like… and I know that we had a discussion around this working with regular SDKs. It's one of the features that's most common people Wow.
I mean, we could kind of close the gap for legacy applications, even that are SDK instrumented, where the stress log correlation does not exist. Well, we can just finish the work, at least put the trace ID, not the span ID, but at least put the trace ID, even for SDK-instrumented applications.
Tyler 00:20:37 Yeah, I mean, I think this sounds like a good thing to progress on. I'd be very… I just want to say, I'd be very hesitant to try to support regular expenses here.
Given, like, my history using, like, FluentBit and other, like, logs.
Nikola Grcevski @ Grafana / OpenTelemetry 00:20:50 Shit.
Tyler 00:20:51 In the past, like… like, I've definitely seen them remove that support because it is so expensive, especially when you get users writing you know, poor regexes, like, it just becomes untenable, and all of a sudden, like, throughput drops, but I think for what we've talked about, we have a lot of good ground to start on, so maybe we can just start there, and then… like, the graph I was saying, iterate on this one?
Yeah.
Okay.
Cool, I think I'm gonna move this on, given we are 20 minutes. Good discussion. Thanks everyone for joining. Nicole, I'm guessing the action item on that one is open an issue on this one, to track the… Nikola Grcevski @ Grafana / OpenTelemetry 00:21:34 Yep.
Tyler 00:21:34 Conversation, and yeah.
Perfect.
Okay, Nimrod, next you wanted to talk about a, work towards, the OB receiver.
nimrodavni 00:21:49 Yeah, so I've opened an issue, in the collector releases of basically specifying, maybe… trying to get, like, after we talked at the last thing, about getting an OB collector distribution, or even… I've said there's, like, two solutions, either, only an OB one, or, like, a eBPF one that contains OB and the profiler, and maybe other components in the future.
And, Florian, we talked about it, and one of the things he commented is that we currently don't fully support, building a distribution… a distribution only with OCB, there needs to be some… Premature steps of, like, downloading the source, and doing the replace, and the manifest, and… I'm just wondering if it's something that we have any plan to, like, work towards only having to work with OCB, if it needs to be changed on our end or OCB, or are we saying, that's fine, that's how we, like, that's how OB will be, packaged into a distribution for now, and we can continue on with this without, like, fully resolving this. And I think Florine is here too, so if you also want to talk about it… I'd like to hear you.
Florian Lehner 00:23:10 Yeah, cool. Yeah, as I said, I like the idea, but I see the challenges around, building, especially OBI, as the artifacts for eBPF are not part of the, the code, and so they need to be fetched in some way beforehand. From my experience, OCB, so the, hotel collector builder is the… Default standard tool for building collectors.
And, I can just say, at least from our side in Elastic, we use OCP quite heavily, or we are heavily invested in the sense, if someone wants to have some custom changes in the OTL connector, we just provide a manifest with a new processor, a new exporter, whatever, and they just, we just run OCB, and that's why I think for most of the people, having some pre-major steps to get OCP working with OBI will be a challenge.
To get a first experience with, OBI, with the auto collector release is a good point. I think that that's… will attract awareness and maybe also motivate people to work on OCP to Get something in, maybe, to fetch these steps.
Yeah, but I see it as a technical challenge at the moment that, To be… to… for a more bright… bright use.
Tyler 00:24:47 Yeah, I mean, I think that's fair.
We already have, like, the prototype to actually bundle this into the existing collector, right? It has, like, these additional scripts and steps to get this actually working.
I don't… I don't know if we're gonna solve that.
right now, so I would probably say more, like.
If we are going to do this, it's going to be in the collective releases.
repo, and, like, maybe track that work alongside the existing issue for the, you know, tracking the… binary objects in our Git code somewhere. We have an issue for that, but yeah, I don't think that this is gonna get I'd rather it not stall us on getting something Then it just, like… Becoming a blocker, because they don't think it's going to get unblocked.
If I'm being honest. And so, I think that, like.
Yeah, trying to do something that's already been done in, like, that prototype I have there, where you're just running scripts to download the source, or if you wanted, like, a point to regenerate the source, I think is probably a good thing to get started. For other users with OCB, like.
Yeah, I mean, I think at the, like, we could make it easier, but, I think… I think that's the edge case, rather than using, like, the main distros, but I may be wrong, I don't know.
And I do think that, like, if you are running the edge case, and you are building your own distro, like, of a collector, like.
expecting you to jump through some of these hoops doesn't seem too unreasonable. I would assume, like, if you're giving this to somebody who's a layperson who doesn't know anything about coding, that that'd be, like, pretty unacceptable, but I think that this is, I think it's a little bit more of an advanced topic, but that's just… yeah, I don't know. I still think it is all, like, an edge case, though.
Nikola Grcevski @ Grafana / OpenTelemetry 00:26:44 And I just wanted to say, like, maybe it's time to reconsider, bundling the BPF artifacts into releases.
Tyler 00:26:55 We do, though, on the releases.
Nikola Grcevski @ Grafana / OpenTelemetry 00:26:58 On releases, do we do?
It wouldn't…
Tyler 00:27:01 We distribute, a binary.
Nikola Grcevski @ Grafana / OpenTelemetry 00:27:04 No, the EVPF artifacts. The AVPF.
Yeah, so, so…
Tyler 00:27:08 We have the source code that includes all the EUPF artifacts is the tarball.
Nikola Grcevski @ Grafana / OpenTelemetry 00:27:14 Oh, okay.
Tyler 00:27:14 That you can download.
Nikola Grcevski @ Grafana / OpenTelemetry 00:27:15 Oh, but… oh, the source code, but not… okay.
Tyler 00:27:19 Yeah, so if you wanted to, like, Use the Go tooling, No, I mean, I don't think you can use that right now.
There is a way you can use, like.
GoTooling to use tarballs, like, but you have to run your own proxy server, but, like, I wonder if there's a way you could, like, tell it to just be, like.
GitHub releases as a proxy server? I don't know.
But no, like, it… yeah, you can't use the Go tooling, but you download the source. Like, you can take a look at the POC that is in the releases. That's all it does, is just, like, it fetches it, vendors it locally, and then it doesn't do any building, which is great, because then you don't have to, like.
Have all these, like, tooling.
But yeah, that's also, again, like, just for releases.
nimrodavni 00:28:09 Okay. Santos, I think if… Okay, for now it's not a blocker, I'll try to continue pushing that, with… I wrote in the collector, collector dev channel, let's see if someone can respond there.
Hopefully you can push this.
Tyler 00:28:28 Florian, what is your take on the bundling with the profiler?
Florian Lehner 00:28:34 Super fine, so I'm using or pushing quite heavily within Elastic to get this done.
bundling OBI with profiling, because, with the recent changes that OBI does, and profiling does, with the sharing of the span trace IDs, you have so many easy wins, that's just incredible.
Just filter profiles for spam trace ID, and you know the hot paths, and can just… Go through it, and… reduce and improve them, that's super helpful. SREs just… crying for fun, that's really awesome to see. But yeah, the, having a reproducible and reliable OTEC collector built with OBI is the challenge at the moment, so I know how I can do it locally, but doing this on a scale is a different topic, and for scaling, we use OCB.
But I know also there's a lot of change happening at the moment with OCB, so, let's see how this goes. But yeah, I agree that for starting with the OT Collector release is a good point.
It's more managed, people can try it and, can forward the data to whatever collector proxy they want for later purposes, so that's… that's good.
Tyler 00:29:57 So, would you be in favor of, in Nimrod's proposal, the, the EBPF bundled one, instead of just an OB by itself one?
Florian Lehner 00:30:06 I don't have a strong preference on this. I know there is currently the eBPF profiler.
Right. Collector release?
But no strong preference on this.
Yeah, faster bundling would, did become easier as we dropped, support, or the requirement for SEGO.
So it's just, like, use your regular Go tooling, that's just working fine now.
And that's… that's why, for us, the steps were a little bit easier now.
Nikola Grcevski @ Grafana / OpenTelemetry 00:30:41 That's a major stroke.
So this got merged into the profiler?
Florian Lehner 00:30:46 No, not, not recently, Do you ask about Siegel or the OBI maps?
Nikola Grcevski @ Grafana / OpenTelemetry 00:30:54 Oh, the OB map, reading the OB map.
Florian Lehner 00:30:57 The OBMAP was merged, Already, 2 months ago, 2-3 months ago?
nimrodavni 00:31:03 That thing's been…
Florian Lehner 00:31:03 fine, though.
nimrodavni 00:31:04 We tested…
Mattia Meleleo 00:31:05 Dean could… I think the version is 0152.0 onwards, or something like that.
Nikola Grcevski @ Grafana / OpenTelemetry 00:31:12 Okay.
Mattia Meleleo 00:31:12 Because I tried with the… with a slightly older one, and it was not working. Because there is a config… of the process CTX, or something like that?
Nikola Grcevski @ Grafana / OpenTelemetry 00:31:23 Okay.
Mattia Meleleo 00:31:23 Which, which needed to be done, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:31:26 Nice. Alright, that's amazing. I didn't know about this. This should have been… yeah, you should have mentioned this. This is great news.
Tyler 00:31:33 It's like a blog post where… Nikola Grcevski @ Grafana / OpenTelemetry 00:31:35 Yes.
Tyler 00:31:35 Great, yeah.
Yep.
Yeah, I mean, in that case, I think there's a strong motivation to have these in the EDPF collector, I guess, because there's… they're already working together. So, yeah, that's great.
Florian Lehner 00:31:50 Cool, thanks.
nimrodavni 00:31:52 Thank you.
Tyler 00:31:54 Okay, cool. Alright, so, just to… Heads up, I am working on a… sorry, trying to share my screen here.
So the Configv2, I merged it, this week.
Thank you all for the reviews on that, like, it's a pretty big one, It also is still a work in progress, I guess, I was realizing, because it is just a new schema that's being added, so, The idea is to keep iterating on it, but also to looking to, you know, start using it, is kind of the idea.
I have a PR here to integrate this. This is, literally updating our binary to accept the new format, and also updating the collector receiver to do… All the isolation that we wanted to have, with the new config.
That being said.
it's, probably way too big just to submit it as is, so I'm trying to get CI to work right now, which is, always fun, but Yeah, it's partly my fault, so that's the hard part to tangle out. It's when it's just CI, or when it's just your fault, that's a lot easier, but, But yeah, so I'm looking to split this up into, parsable, PRs. I was looking at… there's actually, like, a lot of really good ways to split this up, so I don't anticipate it getting submitted as is, but before, this is just kind of like a North Star. I wanted to mention this, just to kind of heads up, that I am looking at this. Obviously, I'm going away at you for two weeks, so I'll try to submit these things and keep active on it, during those two weeks, but… I can't promise a lot of, turnaround time on this, but yeah, just a heads up, it is… it is still something on the radar, still working in progress.
nimrodavni 00:33:36 Is this, like, the full… like, in the config v2, you had, like, a bunch of, splitting of, I don't know, like, splitting of instrumentations per, matching, and all that, that's, like, all of this is in this PR?
Because it looks way too short for, like, what we do is, like, a bunch of features that we still don't have.
Tyler 00:33:58 No, yeah, this is just parsing, and that kind of thing.
nimrodavni 00:34:02 Awesome.
Tyler 00:34:02 Yeah, that's still a work in progress. But yeah, no, this is just, like, the ingest side of things. So yeah, this is… Yeah, there's still… there's still a lot of work to do there. But, like, what this does do is it adds a new, config package itself, yes, sometimes it doesn't load. Yeah, down here, and so this is something where this becomes… usable, and so, like, this is how, essentially, we're going to parse it, and then from here, plumbing this back into the existing codebase is kind of the path.
But yeah, like I said, still a work in progress on that part. This is more just, like.
Getting a line of sight on how to do that, though, I guess is where this is going, yeah.
nimrodavni 00:34:47 Oops.
Tyler 00:34:48 Yeah.
I actually don't know if it's gonna be too hard to do that, it's just essentially, like… Yeah, I actually don't know if it's gonna be too much harder, but I'll just leave it at that. So, yeah.
One step at a time. Okay, cool.
Next up, Mike, you wanted to announce the Go Auto Sunset SIG call?
Mike Dame 00:35:10 Yeah, I don't know if anyone can hear me, I was having some mic problems.
Tyler 00:35:15 Yep.
Mike Dame 00:35:15 Okay, cool. So yeah, we set up a call to talk about the archival sunset of Go Auto. It's, it's on the hotel calendar. Thanks for setting that up, Tyler.
really tried to get a time that works for everyone, but we've got people, like, literally all over the world, so, fortunately for me, I'm right in the middle, on the East Coast, but it's gonna be 11 a.m. Eastern Time, hopefully it's not too late for our, across the pond folks, or the, West Coast people, too. Yeah, just kind of go over what… you know, what we want to try to do to kind of gracefully sunset that and, point people towards OB where they can, and, yeah, hopefully not leave too many things, hanging on Guano, so… Yeah, got a couple weeks, bring some ideas, anyone that's interested, please feel free to join, and appreciate the, the input from everyone.
Tyler 00:36:14 Awesome. Yeah, I will see you there.
Okay, next up, I did want to mention Release V09 went out. Thanks again to everyone, on this one. A lot of great things went out here.
I think the GenAI stuff is really, like, interesting me, but there's still a bunch of other features, protocols, stuff. I don't know what I'm telling you all. Y'all wrote it.
But, one of the things I did want to mention, just kind of a heads up, is, like, I don't know if it was me or if it was GitHub, but in the process of releasing this, I double-released it.
I released this one first, and for some reason, when I hit, like, publish, the tag that was associated with it just, like, disappeared, so it made its own tag, called, like, Untagged or something like that. Like, I don't really know what happened here, but, Turns out, Go doesn't care about this. Technically, you could pull in this version. It's not really, like, yeah, I don't know. This doesn't comply with any of our versioning, so it's not really, like, a usable tag.
But the V09 tag still is out, that was always out. The release is here, just kind of a heads up that there's a duplicate there in case you ever are questioning that.
Mike Dame 00:37:23 It seems like it could have been part of GitHub's new, 09's uptime policy.
Tyler 00:37:30 It does have a 0 and a 9, right? Yeah.
Mike Dame 00:37:33 Yeah, there you go. That's more 9s than GitHub has now.
Tyler 00:37:37 I thought they had 1.9, they were at, like, 89%, right? So there's texture…
Mike Dame 00:37:41 Oh, that does count, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:37:45 Should we just delete that untagged?
Tyler 00:37:47 So, I don't think you can. We have immutable tags, immutable releases.
Nikola Grcevski @ Grafana / OpenTelemetry 00:37:56 Okay, that's fine.
Tyler 00:37:58 that's a good question. I don't know if we can release, or.
Nikola Grcevski @ Grafana / OpenTelemetry 00:38:02 I see the trash… trash icon next to… That, so I don't know if you can just… If you click on that. Not the tag, but on the previous, on the release.
Tyler 00:38:12 Oh, on the release? Oh, yeah, good call. Yeah.
Yeah, so the tag may have to state, I see what you're saying.
Nikola Grcevski @ Grafana / OpenTelemetry 00:38:21 Yeah.
You'd have to kill the real, you know…
Tyler 00:38:25 Definitely.
Nikola Grcevski @ Grafana / OpenTelemetry 00:38:25 the releases, the main one. Yeah, that link, and then…
Tyler 00:38:31 Yeah, that'd be great if we could just do that.
Nikola Grcevski @ Grafana / OpenTelemetry 00:38:33 Yeah, just throw it off, please.
Tyler 00:38:36 Yeah.
Yeah. Yeah. Okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:38:39 And it's like, garbage tag, that's okay.
Tyler 00:38:42 Right, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:38:45 Nice. Alright.
Tyler 00:38:47 Cool, that cleans things up. Thanks, that's a good… that's a good cleanup.
Again, I don't know if, like, my update somehow, like, kicked off that thing where the tag disappeared, or it was just… GitHub's been having a lot of problems, as Mike was pointing out, so… Yes.
Mike Dame 00:39:02 an incident right now on GitHub.
I just looked.
Tyler 00:39:07 Yeah, I mean… Any time of day, I'm pretty sure you could say that at this point, but yeah.
Okay.
Cool, alright, next up, Antonio, you wanted to talk about Observability Summit, and asking other folks if they're gonna be there.
Antonio Jimenez 00:39:23 Right, that's mainly that. If you're gonna be there, let me know, it would be great to catch up in Persian, to meet in person. It's gonna be next week.
Stephen Lang 00:39:32 Yeah, I'll be there. Nicola was going to be there originally, but he can no longer make it, so I'm stepping in.
Tony.
So I'll be talking about the Java OB agent, next Friday.
I'll see you then.
Antonio Jimenez 00:39:44 That's cool.
Stephen Lang 00:39:47 Anyone else going?
Tyler 00:39:49 I'm not. Where's it at this year?
Sit.
Nikola Grcevski @ Grafana / OpenTelemetry 00:39:53 Minneapolis.
Antonio Jimenez 00:39:53 Anybody here.
Tyler 00:39:54 Minneapolis? Yeah, that's right, yeah.
No, I wasn't able to make that one.
Florian, do you know anybody from, like, the Profiler team or anything like that?
Florian Lehner 00:40:05 And no, we will not be present.
Tyler 00:40:08 No, okay.
Nope, I think it's just you guys. You guys gotta hang out and talk over.
Antonio Jimenez 00:40:15 That's do it.
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:17 I almost made it, but my daughter's graduating, so I have to pay for her graduation, I can't…
Tyler 00:40:25 You can't zoom into that.
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:26 No.
Tyler 00:40:29 What about life events, right? Yeah. No, that's a good idea.
Okay, cool, and then the last one on the agenda right now is, Mattia, you.
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:41 Oh, you miss me. I wanted to talk about KubeCon. I mean, there's lots of good work here.
Oh, sorry, yeah.
Tyler 00:40:48 Yep.
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:49 Yeah, I thought he was talking about KubeCon. Sorry, Antonio. I saw, like… I know that's virtually… proposals that went out to KubeCon, Japan didn't get accepted. Maybe recycling some of those in a new submission.
But also, we have really good stuff, There was something that also came under the maintainers channel.
that maybe even Maintainer Summit. I think things will be interesting, Nimrod, your stuff with Weaver.
If we kind of mix up the companies here for proposals, usually has higher chance of acceptance, if it's not a single vendor. So, partnering amongst ourselves, to kind of talk about OB and all the cool stuff we're doing. So, just wanted to bring it up there.
Think of ideas, and maybe we can… for async on… figuring out who submits what, and I'm happy to help with every submission, even if I don't go. And if somebody goes, I don't care, as long as Obi gets talked about.
Tyler 00:41:55 Yeah, absolutely. I just want to echo that. That's a really good point. I am a part of, like, a bunch of different SIGs. This is, like, one of the few SIGs where I think I've got more talks than I have, like, time to give in the SIG. Like, there's just a lot of really, really good, ideas and topics and things that you can play with.
So, like, this is definitely one where I think, like, if you are, like, considering going, like.
come up with a talk idea, or maybe even, like, ping other people with ideas if you want, like, we can talk in, like, Slack or something like that, because I think there's a lot of really good ideas.
any of the work that you've been doing here, I think, is really good, and it shows and it highlights how, like, this is a very new way to look at instrumentation, so, yeah, worth… worth going.
And worth presenting on a talk.
There's… there's KubeCon, there's Observability Day, and then, as Nicholas said, also Maintainer.
Nikola Grcevski @ Grafana / OpenTelemetry 00:42:46 Summit.
Tyler 00:42:47 summit.
You don't get a KubeCon ticket if you get a talk accepted to the Maintainer Summit, just a heads up on that one.
Nikola Grcevski @ Grafana / OpenTelemetry 00:42:54 Hmm.
Tyler 00:42:55 if your company's gonna pay for it, I think that it's worth… you should try to go to the Maintainer Summit, even though it is, like, on a Sunday, normal time. But yeah, it's also really great.
Yeah, I mean, I think… there's a lot of really good talks there. I like, like you said, like, the Weaver stuff would be great. It shows a lot of cross-functional, usage, but yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:43:17 Yeah.
Tyler 00:43:19 Yeah, there's a lot of really good stuff.
Stephen Lang 00:43:21 I wondered about submitting around all the CI madness.
Tyler 00:43:25 Yeah, like, I think, honestly, that'd be a really good maintainer talk, or even an Observability summit talk. I think that there's a lot that you can help other projects learn from. One of my favorite maintainer talks last year was, It was… they were just, like.
talking about, like, their whole release process, they were just like, yeah, this is what we do, these are all the other things, these are the hard parts that we've had, and, like, Some of them were very applicable, some of them were just, like, hierarchical structuring, how you, like, handle teams, how you handle, like, roles in the project, like… this project actually has, like, an on-call engineer, this is an envoy, and, like, and it's, like, that's nuts to me, but, like, it works really well for them, like, they, they, yeah, and so I was like, oh, wow, that's cool. So, just talking about our problems here, and, like, how we're, like, trying to wrangle it, and, like, the scope, you know, I think it'd be great for a CI talk, yeah.
Mike Dame 00:44:18 Is there… do we know when the Maintainer Summit is this year? I don't see it on the schedule. I remember before it was, like, on Saturday that made it tough.
Nikola Grcevski @ Grafana / OpenTelemetry 00:44:27 Yeah, it's usually sunny.
Tyler 00:44:28 A.
Mike Dame 00:44:29 Yeah. Okay.
Yeah, that Saturday one was… was weird.
I was thinking of doing… trying to do maybe something for Observability Day about the dynamic stuff, if I can get a little bit more dynamic stuff added. I think I mentioned this to Nicola, Maybe something about… doing, like, how we do stuff with that, building extra controllers on top of Obi.
Maybe interesting.
Nikola Grcevski @ Grafana / OpenTelemetry 00:44:53 Got it.
Mike Dame 00:44:54 More than just one.
One function.
Tyler 00:44:59 Well, but I think that, like, holistically, the actual problem itself is important, right? Because, like, it's one thing to just… you know, have a program running, it's another thing to, like… and it's not just Obi, right? Like, just the idea of dynamic config across, like, Java as well, like, it's a big one on dynamic config.
And that's been years in the making, so, like, it's a hard problem to solve, because you're really trying to intersperse, like, state, right? And so, yeah, it's definitely a good one, I think, a good talk, so, yeah.
Mike Dame 00:45:28 Yeah.
Tyler 00:45:32 But yeah, Cool, like Nicholas said, yeah, like, happy to help as well, so yeah, let's get some talks. The more Obi talks, the better the project's gonna be, so… Nikola Grcevski @ Grafana / OpenTelemetry 00:45:43 Yeah, 100%.
Tyler 00:45:46 Okay.
Now, we can talk about Batia's PR.
Mattia Meleleo 00:45:56 Yeah, as far as I understood, last week, from the last, SIG meeting.
This one was waiting for V090 to get released.
I think, it's ready to go now.
Everyone agrees.
Rafael Roquetto 00:46:17 Who's that? Ilios guy?
Tyler 00:46:22 Guy's a jerk.
Okay, cool, yeah, I mean, I think we've got… two approvals, I can get rid of this as well up here.
But, yeah, let's… let's… any objections to merging this?
Nikola Grcevski @ Grafana / OpenTelemetry 00:46:37 No, I'm actually keen on merging it, because I want to… we want to test it at scale as well, and a bunch of us have… work they want to do in the same area, and we're all kind of waiting for this to get merged, so… Awesome, yeah.
Mattia Meleleo 00:46:57 I was blocking the whole pipeline.
Nikola Grcevski @ Grafana / OpenTelemetry 00:47:01 Oh, that's… that's… that's okay, you know.
Rafael Roquetto 00:47:05 You were blocking, but you were doing all the work, we're just here waiting, so… Nikola Grcevski @ Grafana / OpenTelemetry 00:47:09 Yeah.
Rafael Roquetto 00:47:10 incompletely.
Mattia Meleleo 00:47:14 Please let me know if there is any sign of a flaky test or whatever.
Let me know, personally.
Nikola Grcevski @ Grafana / OpenTelemetry 00:47:23 Yeah, we want to run it internally as well, to see if we can break any apps by injecting headers in random places and stuff like that, which we definitely did with the HTTP until we got it right, so… That's, yeah. I don't expect anything, I'm just saying, yeah, I think it's just gonna work.
I'm being optimistic, but, just in case. We're just gonna run it through.
Mattia Meleleo 00:47:46 We already tested some previous versions, and nothing broke.
That's good. But I can't… I can't say for your… Nikola Grcevski @ Grafana / OpenTelemetry 00:47:53 before you…
Mattia Meleleo 00:47:54 your cluster.
Nikola Grcevski @ Grafana / OpenTelemetry 00:47:55 Yeah, yeah, exactly. Yeah, gRPC is finicky, so… Yes, yeah.
Tyler 00:48:07 Awesome.
Well, yeah, now it's merged, what the… what the… triaging begin, right? Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:48:15 Exactly.
Tyler 00:48:16 Awesome. Okay, cool, that looks like the end of the written agenda.
Pause here. Any other topics people wanted to discuss?
Cool things, cool projects.
nimrodavni 00:48:28 Regarding the stuff you talked about, Weaver, I just wanted to say that if anybody wants to… take a look at the PR… I saw, I think, only… I think Mario and Mattia viewed it. The PR itself is really big, but it's, like, you have, like, two to three just repeating changes.
And I want to get your, like, feedback. Like, the only thing I'm concerned about is CI time.
after… I did some, like, routes of optimization, and, like, it dropped down to about, let's say, 2 to 3… like, I think, like, 20 to 40 minutes of total CI time, or about… Let's say 5… the 3 to 5 minutes per shard?
The only thing I thought about, like, how to really optimize it more is… instead of each test doing Weaver evaluation, you basically just write down all the telemetry to some file, and then, like, after all the tests run, you just get a Weaver and, like, it validates everything, but we just need to make sure that we correlate it to the original test that it came from, so it'd be hard to, like, easier to debug.
I can try to do tests on it and see if it, like.
This is better, like, and by how much?
But, like, anyway, if you guys wanna have a look, or, like, at least a general, like, guidelines of what was done.
Nikola Grcevski @ Grafana / OpenTelemetry 00:49:53 How much did he add to the CO time? Do you have a rough idea, or…
nimrodavni 00:49:56 Yeah, so, like, the CPU time is about, like, let's say 20 to 40 minutes, but the… the longest shard is about 7 minutes, so that's, like, the… like, let's say from, a shard that took, like, 25, it's, like, about 30… it was, like… Yeah, from, like, 20 to 26.
At least that's in some runs, but I can run it again and make sure.
Which might, like, be… I don't know if we move it to the end, if it will be… it'll probably be less CPU time, like, less machine time, but it might be more like, wall clock time, because we need to wait for everything to end, and then only after that. Or maybe I can do it… maybe I can do it once per shard or something? Like, at the end of each shard?
Nikola Grcevski @ Grafana / OpenTelemetry 00:50:50 Hmm.
nimrodavni 00:50:52 I don't know, I need to… I need to test it. That might be a better idea. I'll try a couple of stuff as well.
Yeah, that's it.
Nikola Grcevski @ Grafana / OpenTelemetry 00:51:04 That's pretty good.
Tyler 00:51:05 Steven, have you had a chance to take a look at this?
Stephen Lang 00:51:09 I will take a look at it.
Tyler 00:51:15 Yeah, I think that'd be great. I still… I've taken a look, cursory glances at it, but I haven't completely jumped through the whole thing yet.
But yeah, I'll try to take a look as well.
nimrodavni 00:51:28 Thanks.
Tyler 00:51:33 Awesome! Well, cool. If there's nothing else to talk about, we can end the meeting here? Yeah, coming up on the end anyway, so yeah, makes sense. Good to see you all. I will see you all in, 3 weeks' time, but, I'm sure there's just gonna be tons of stuff to come and see the awesomeness when I come back, yeah, so I'm pretty excited.
Nikola Grcevski @ Grafana / OpenTelemetry 00:51:49 Matt?
Rafael Roquetto 00:51:50 Yeah, enjoy the time zone, till this one.
Tyler 00:51:52 Yeah. Alright, guys.
Rafael Roquetto 00:51:57 Dear?
Mattia Meleleo 00:51:57 Bye-bye.
Mario Macias 00:51:58 I…
Antonio Jimenez 00:51:59 Curious.
Jose Torres, Simon.
Correcto, entonces, la hora que queriamos aqui a la de Plaza Barcelona, y tiene route una… Mmm… como… 202 herramiento, y ro tambien… God, yeah.
Correcto, por eso deta preontando, mi preonta la sigiente. como un funciona esto.
variantanes.
un poquillo idea.
Y por la estan plaza Barcelona, asi que cuando que sias, por misi Antonio. Antonio, por vamos a circado ally, lo vamos en aquilamente. Y demos porque el obra bastante sentencia cambia bano y cocino.
Pero. Besto de tu granquilamente.
Perfecto. Vale. Y nuevo pou… Mamo al piso.
Perfecto. Alma.
Yeah, paramo.
Period.
hermano pasi y medioc.
Alright, I normally have a corner at Java.
lobby.
dio alche… ahi.
Yeah, but they were to have the helmet.
amente, y yo de… Y entonces, una vazca clara modulo para al ficios y madimo. Ego perfect.
Yeah, I think I've been going on.
llevado a yo muesto.
Es se nino de Julio como ello.
habitacion donde yo trabajaria. Es aca cabamo larga.
Es ha itacion tiene una puerta hacia la terrazza.
a dime.
Esa han amimo, esa puerta, que yo quiero ponar… No puede tenas persona, porque si de una puerta, Gabria hacia fuera, imaginade como si fue la puerta de nuestra.
escano siempre.
initialmente como una puerta porque son mas… ahilante, pero creo que tiene sentido pone una ventana, corredera es alament iguar que donde vamo dormi. El mimos tambano incluso, porque tenga yo se un que creo que la que tienen donde vamo dormi.
No, salia la terraza es tiem, eso 104 que yo quiero esta sento, salia a la terraza.
una puerta en mailante, pero no una puedas por es persona, ya mas pequena, una puerta correredera, como la cavo pane esasamente, la mitacion dondeor mismo, en poquito mas grande.
creo que la mas entido tienen seria escho.
opinion, porque el taba asi, que compre siempre lo malante, lo mas reciente, lo mascaro, lo mas mejor.
el med dijo, que lo que caramos que la dan no ball.
Creso decimo de este.
Sounds good.
de la cos.
I'm off on the board, huh?
mas como para… a cada bien?
Yes, ba?
Batrahalai.
Open. Yeah, hello dir, yellow dira.
Gracia. To geto.
Hello?
Can I?
Hola, bueno tarde? En llama. Hola, mi de llamo dece obedible hemos copia. Estamos a un pequenos conelectoral que el minuto camb me cortita.
