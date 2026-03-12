SIG: eBPF instrumentation
Date: 2025-09-10
Duration: 95 minutes
Zoom Recording URL: https://zoom.us/rec/share/JSocsQYtSmq0ownnvOvNCyzIyaM6e7_MxJT5D7HP4HkIKJPc4GrwypLgrFv9ULLA.ZvleHfV_GZ20lcmH
============================================================

## Zoom Recording Transcript

**Rafael Roquetto** 00:49 Hey, Tyler.
**Tyler Yahn** 00:50 Hey, Raphael, how's it going?
**Rafael Roquetto** 00:52 Good, how are you?
**Tyler Yahn** 00:54 Doing well, yeah.
How's the, how's the weather there?
**Rafael Roquetto** 01:01 It's great, actually. Blue skies, 20 degrees Celsius, so yeah, no complaints, how about there?
**Tyler Yahn** 01:09 Yeah, it's a little bit overcast, but I… it's cool, so I'm also… I can't complain. I like it, yeah.
**Rafael Roquetto** 01:18 You're… you're in Seattle, right? Or…
**Tyler Yahn** 01:19 Portland, Oregon. Portland.
**Rafael Roquetto** 01:21 Bargain, okay.
**Tyler Yahn** 01:23 Yeah.
**Rafael Roquetto** 01:23 Hi, Mattia.
That's, is it similar to Seattle? Like, in terms of…
**Tyler Yahn** 01:28 Yeah.
**Rafael Roquetto** 01:29 Water?
**Tyler Yahn** 01:30 Yeah, it's, Seattle, I think it's a little bit more rain, but it's pretty similar.
the time shifts a little bit more, so it's actually pretty closer to… like, Seattle, I think, is closer to, like, you for, like, how much the, sunset and sunrise shift.
We're pretty… I think we're, like, 20 minutes difference or something like that. It's not, like, in the depths of winter, in the peak of summer, but… Yeah, it's, like, noticeable when you go down to, like, California, and it's, like, the sun's setting at, like, 7pm still, and you're just like, how… like, this sounds great, like…
**Rafael Roquetto** 02:00 What are you still doing there? Go south.
Yeah, that's a whole thing, yeah. Yeah, I know.
**Tyler Yahn** 02:09 Yeah.
Hey, everyone.
Boom.
Hey.
I was looking at the, agenda, it looks like, Nimrod had a few things he wanted to… talk about, so maybe we can wait a little bit and, and see if he joins, otherwise we can jump into maybe just doing some review.
But yeah, if you have other agenda items you wanted to talk about, please go ahead and add them, and then… If you haven't yet, go ahead and also add your, Your name, which I probably need to do.
Yeah, we can get started here in just a second. Oh, yep, there's them, Rob.
**Mattia Meleleo** 03:03 I think the microphone is not working, Nimert, I'm not sure.
**Tyler Yahn** 03:08 I can hear you now. It's a little…
**Mattia Meleleo** 03:10 Yeah, now it works, yeah.
**Nimrod Avni** 03:12 Maybe I'll talk quietly.
Can you hear me fine now?
**Tyler Yahn** 03:18 Yep.
**Nimrod Avni** 03:20 Cool.
**Tyler Yahn** 03:26 Cool. Alright. So, yeah, welcome everyone. We can jump in here in just a second. Thanks for joining.
Nima, you wanted to talk us, or start us off by talking about GKE Autopilot support?
**Nimrod Avni** 03:39 Yeah, it's actually something I discussed with, Mario Bid, and… mainly redirected to the Grafana guys, maybe, but maybe someone else knows. Basically, GKE Autopilot is, like, the way of running, kind of like serverless Kubernetes, whatever, and we had someone, who wanted, to, like, wanted if they can install Obi, and it's… it also talked about the profiling, like, the EVPF profiling.
On, on GKE Autopilot, and for that, like, from what I read, you need to have, like, it's… they don't allow, like, program, like, containers to run with, like.
elevated permissions, usually. Like, you know, stuff like a host PID, a host network, and elevated, like, privilege, all that stuff.
Besides a few, like, couple, like, autopilot partners?
And, the autopilot partners, we have, like, kind of two categories. You have, like, the actual, like, companies, the stuff like, I think, also, like, Splunk, Datadog, whatever, whatever.
And you also have open source workloads, and in there I saw both Bela and, there's another Grafana product, I forgot the name.
**MM Mario Macias** 04:59 annoyed.
**Nimrod Avni** 05:00 Aloy, yeah.
And I think it has to do… I think there's some, like.
I don't know, I don't say, like, legal process, but again, I think there's some, like, procedure on how to register to Google with that, and just because we have a lot of people from Grafana here, I wanted to know like, first, if anyone knows how, like, you got Bela and Alloy there, and if you want to do the same thing for, like, OpenTelemetry agents, mainly the ones that need elevated permissions, which are Obi and, like, the profiler, maybe we can, like.
Worked together on that.
So… I don't… yeah, I think I talked with Mario a bit, he said maybe… I don't know if you had a chance to, like, dig around in Grafana, maybe someone else knows.
**MM Mario Macias** 05:51 Yeah, I didn't phone… we didn't… we didn't talk so much time to talk about it internally, so it's nice that you bring it up.
To be honest, I don't know if Nicola or Raphael have more insights. I just found somewhere notified, hey, you are on autopilot, but as far as I know, no one of these teams started… of the Vela team started this process.
even it's not really still complete in… in terms of Grafana, I think. I think Vela doesn't yet work. So, to be honest, I'm… I don't have an idea who and how, started this… Process.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:35 I will chase this down. Yeah, I will chase this down. First of all, I have to say, like, I didn't know Bela was added, so… which is a big problem.
Yeah.
**Nimrod Avni** 06:44 All the people in Bela, and no one knew that it's on… it's, like.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:48 No, we actually have an outstanding issue opened by somebody saying, from the community, you guys are a partner of Google, it will be dead simple for you to publish this.
Now, somehow this happened. I'm not even sure which version of Bela is there. Can you just have any version? So, I have to dig this in, but I know where to start within Grafana to ask this question, and then wherever it leads us.
If we get there, I think maybe those two manage to get in, because Grafana is a partner?
So… but we can, same way, publish an Obi image.
**Nimrod Avni** 07:27 Yeah, I'm guessing, I think, from what I, like, I kind of read a bit, they have some sort of, like, first of all, you, like, need to publish it to the, like, their, like, the Google, like, repo of images, and I think they do, like, kind of whitelist based on the prefix.
Of the image, so I think every, like, every Bela image, theoretically, should be there.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:49 You'll be there? Okay.
**Nimrod Avni** 07:51 Maybe I misread.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:54 Okay, I have to dig…
**Nimrod Avni** 07:56 what we need from, like, the, like, if we go, like, we'll say, like, hey, we're from OpenTelemetry, can we, like, be approved, I don't know what processes, so that's…
**MM Mario Macias** 08:07 Some… some… some silly, some silly question.
does this autopilot stuff needs to be initiated by Grafana? Because, as far as I know, there was a Google team using Bela.
Is it possible that they added it, or no, it's…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:28 I mean, why alloy, then? I mean, I know David Ashbold.
**MM Mario Macias** 08:31 Yeah, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:32 Playing with Bayless since day one, but, I mean, I don't know who added Alloy.
**MM Mario Macias** 08:37 Correct.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:38 So, there must have been some internal communication between Grafana and Google on this. We were just not made aware.
Yeah, or maybe Google did it, so I… maybe it was good to sync with David, see if he knows anything more about this.
**MM Mario Macias** 08:57 Hmm.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:59 Yeah, I was surprised now that you pointed here that we are listed there. I mean… Because we have an open issue, somebody in community asking us when Uganda's gonna do this.
It's been open for at least 8 months, I think, and recently there was somebody else coming back, I really need this, can you guys… Push this forward.
And we just told them, like, sorry, like, focus is elsewhere, but we'll get to it.
So.
**Nimrod Avni** 09:25 And I was coming from your direction.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:27 Yeah, it happened somehow without… any of our team members being involved, so I'll chase this down. If it happened from Grafana's side, I know where to start, like I said, so I'll go from there.
**Nimrod Avni** 09:39 Thanks.
Cool.
**Tyler Yahn** 09:42 Okay, well, yeah, alright, we'll follow up on that one.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:46 We'll need release 0.1 at least, though, with Obi, right, so we'll need.
**Nimrod Avni** 09:51 Yeah, I guess it's…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:53 Official.
**Nimrod Avni** 09:54 version.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:54 Yeah, yeah, yeah, yeah. Okay, so we need an OB release, but if we manage to pull this off with Bela, I think we should be.
**Nimrod Avni** 10:03 Yeah, I can… Todd, you want me to continue?
**Tyler Yahn** 10:06 Yeah, go ahead, yep.
**Nimrod Avni** 10:07 Yeah, so that's a… we have, like, an unrelated topic, another issue we encountered. Wanted to hear your thoughts. Maybe you encountered it, and maybe we have ideas to… what we can do with it. Basically, we have the option to exclude the already intrepid services with OTEL, which I think right now basically looks at both, like, HTTP and gRPC exports, both for traces and metrics, like, detects, like, if this route, like, looks familiar, and, like, if we so, then we disable instrumentation. In HTTP, it works fine. gRPC, I think, is… the most common one, most, like, most services use gRPC, and the normal issue is that because we track gRPC only when the connection is started, then this thing only works when you, like, restart the application pod.
And then, like, it stopped tracking it.
Okay. So that's what we… like, so I try to think if we can do it… if there's any way we can do it not based on natural, I don't know, like.
I had thoughts of, like, I don't know, trying to find… open telemetry, like, symbols in binaries, but that doesn't… that doesn't necessarily mean it's instrumented. Or, I don't know, just… just some thoughts.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:30 Okay, yeah, I think I know what you mean.
Yes, because we… If the communication started before we saw the first establishment, and they never reestablished the connection, which is long-lived, we will miss it.
Yeah, we… we may add… have to add, like, an additional secondary heuristic for detecting this.
Here's a thought, I'm not sure if it's gonna work or not.
One is to kind of try to detect the ports. If this is gRPC traffic going to 4318, or 4018, or whatever… 17, sorry. 17 is gRPC. We can kind of suspect that this might be actually a gRPC call, to OTEL, and then… I'm hoping that through these requests and responses, there might be a header That we currently don't look for.
That will give us indication that this communication is actually So, when we get the GRPC…
**Nimrod Avni** 12:36 We can't read… we still can't read headers, though, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:40 We can. So, if you want, I can share a screen, what I mean by this, but…
**Nimrod Avni** 12:45 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:47 Kyle, you okay with that?
**Tyler Yahn** 12:48 Yeah, yeah, yeah, yeah, sorry. When you said the text ports, I also had the thought of, like.
**Nimrod Avni** 12:53 If we see this poured, we can… like, I guess we can access the… I know we can try to parse the payload as, like, the protobuf, and see, like, if we manage, then this is probably the gRPC export one? I don't know, also probably a stupid thought.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:10 Yeah, so where is this now? Okay, should be in components.
Adpf.
common.
HTTP gRPC Transform, so here, I think.
So, in here…
**Nimrod Avni** 13:36 Oh, we have the headers, but not the values, you mean?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:38 So, this is the stuff we look for.
**Nimrod Avni** 13:41 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:42 So we currently, look for known frame keys, and we try to find a specific one, and then we get the values for when we read these frames for a gRPC request. So, we… this is maybe, like, a way we actually detect that it's a gRPC connection after the fact, because initially, to us.
if it wasn't detected as a gRPC connection to begin with, we may just think it's a TCP traffic. But this code here, parsing, detects that, oh, it was not… we didn't see the initial communication.
But… we see, that there's gRPC frames here, so we're gonna make this a gRPC, connection from now on, and then we start reporting it correctly. So… I'm… we need to inspect what other, things happen here, so what do we get here for HF key? There might be a specific thing in the request or the response that's not actually, encoded as one of the standard paths that is specific to the collector.
And then we can kind of use two-way approach, like, we have… The port, plus… Plugs the thing on top.
**Nimrod Avni** 15:03 Yeah, I can look at that, that sounds like… I mean, maybe if the collector, like, or the exporter sends with, like, a specific header.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:14 Yeah, we should look to see if there's any specific header that would give us an indication that this is an OTLP export. There might be. We may get lucky, otherwise we just go with maybe an optional flag, maybe turned on by default to say, detect based on the port, and… Now, considering people can turn it off if it gets them in trouble. But I'm hoping that we'll find something there that's… So, all you need to do is really, as you're running these workloads, just print what you get for HF key, and see if… If there's anything there, that… This header field will contain the value as well, so you can print them, see what's in there.
**Nimrod Avni** 16:00 The… the value… The value is, like, It's only because we… when we, have it at the start, like, when we detect a connection at the start, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:12 It will be later as well, like, if these are standard headers, they're known. So, so gRPC has these two tables. One is a static table, where they contain the list of all fields that the gRPC protocol knows of. And, for example, content type is specific field.
And then they have a dynamic table for additional headers that you as an application may use, but they're not known to us, to the protocol. And then protocol will encode that
**Nimrod Avni** 16:43 nerds.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:43 add those additional in the dynamic table. I'm hoping that some of these standard headers will contain information.
that is enough for us to detect that it's a collector.
**Nimrod Avni** 16:56 I can try, but I also like the, like, worst case, maybe…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:01 report.
**Nimrod Avni** 17:02 If, yeah, if, like, it's a gRPC with port 1417, and you can turn it off.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:07 Yeah.
**Nimrod Avni** 17:08 That sounds, like, more, like, probably green.
**MM Mario Macias** 17:11 Yeah.
And there's…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:14 Things like this gRPC message, gRPC status, there's all sorts of things that we can look at. So there's two of them, just make sure. This is the decoder returns, so this is the response, and there is a decoder for their request. So we could see if any of them contain interesting headers.
**MM Mario Macias** 17:31 What about this assumption? We look… when we instrument a process, we look for some auto standard environment variables.
To read the configuration of… of that, of, of that, process.
What if we just look for the hotel exporter OTLP endpoint?
if someone sets this… this NVAR to a… to a valid endpoint, we might assume they are exporting hotel data, otherwise nobody will set it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:06 Yeah, that's another good indication. The exporter has been set. To the end, we're doing gRPC traffic on the same port.
I think that's a pretty good assumption that they're actually exporting it.
We see the traffic, they've configured it.
**Nimrod Avni** 18:22 But, like, it needs to come with… we see traffic on the same… we can, like, parse the URL, get the port, and see if we… I know, because we have, like, some instances, like, services in CoreLogic, I think, like, automatically.
Every service has that environment variable, like, inserted.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:41 Yeah. Even if it doesn't, like, report anything.
**Nimrod Avni** 18:44 Exactly, yeah. I guess…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:46 Exactly.
**Nimrod Avni** 18:46 in the car.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:47 But you see the traffic, as we do right now, we don't recognize it as an OTLP export, but then we see that it's on the same port as the environment variable that we know of.
And then we say, oh, okay, so this is a better indication than just the port.
**Nimrod Avni** 19:05 I think that… yeah, I think that's a…
**Tyler Yahn** 19:08 good, like, yeah, I think that's a good approach. We still have to verify that it's gRPC, though.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:14 Yeah. So that could also be an issue. Yeah, so we know how to do that.
**Nimrod Avni** 19:18 And, yeah, and like, from the… if we have the environment variable, take the.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:22 and the port, and the port matches, I think it makes sense. One thing that will trip us over is that if you're doing local host export.
Because those may be defaults. Like, I think a lot of the SDKs will default to localhost 4317.
**Nimrod Avni** 19:40 If you don't specify it.
So…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:46 But…
**Nimrod Avni** 19:46 In that case, do you, like, there won't be, like, an actual network request, you mean? Or is it, like…
**Tyler Yahn** 19:52 Maybe not in retirement.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:53 It's just… but there won't be an environment variable, yeah.
**Nimrod Avni** 19:56 Yeah, I think, yeah, we can probably assume… yeah, I guess if we don't see it, we assume it's the default port?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:03 Yeah.
Where you can see.
**Nimrod Avni** 20:04 There's, like, probably tons of standards of, like, I think there's also, like, a environment variable that states the protocol, and, like, if it… if that's it. I think we can, like, follow the…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:15 Yeah, yeah. Yeah, I think we can get really clever there. I think, in a sense that if it's a local host with 4317, then you may assume, and you didn't specify it, then you still, okay, that's fine, because it's localhost. But if it's anything else, then you must see the environment variable as injected to the application. What may trip us over additional is people hard-coding this, I don't know if anybody would, but… I mean, nothing stops people from writing code that actually has a hard-coded value in there, or they're pulling it out from some other config that's actually not environment variable.
**Tyler Yahn** 20:52 I mean, that is true, like, so you can definitely set it as a hard-coded, but you can also set it for the O2, or the OpenTelemetry, like, configuration.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:58 How to continue.
**Tyler Yahn** 20:59 duration file.
Pretty sad.
**MM Mario Macias** 21:01 If, if I…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:02 Java can be injected as options to the agent. Like, you can specify the agent, then you can do colon, and you can say, oh, TLP exporter, and give it a URL.
So…
**MM Mario Macias** 21:14 if I recall correctly, at least for the Go Hotel library, even if you set it programmatically, it internally set the environment variables.
**Tyler Yahn** 21:29 No, it doesn't do that.
**MM Mario Macias** 21:30 No? It doesn't do that? Okay. Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:35 Yeah, Java will, I think, add it to the system options, but those don't necessarily mean they're environment variables, they're internal to Java. So the environment variables get turned into the system properties, but not the other way around.
**MM Mario Macias** 21:50 Oh, God.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:52 So, I mean, having the environment variable would be a better indication, but…
**Nimrod Avni** 21:57 I think we can maybe, I don't know, You can, like have it… how, like, how many… it can be, like, a config of, like, how much assumptions can we make? Like, I don't know if it's… If it's 4317 and we don't see anything, then we can assume that it's probably that, but you could have set it internally to do, like, port 9000, and we wouldn't know, but I think you can, like… If you maybe, like, we can save to the customers if he can control it, or he can turn off automatically all the exclude, stuff.
**Tyler Yahn** 22:34 like, why don't… why don't we just add an option for that port? So, like, you can just say, like, exclude the OpenTelemetry instrumentation, and, like, we can try all this default stuff, and then if it doesn't work, we can have another option that says, like, what port are you listening on, or what port are you sending to, right? Like, if you wanted to do something…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:47 your OTLP port, so we can know to exclude it.
**Nimrod Avni** 22:52 Yeah, and, like, we can default it to the default geography.
**Tyler Yahn** 22:55 Yeah, exactly.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:57 Yeah.
**Nimrod Avni** 22:57 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:58 That's perfect, yeah, that's a good suggestion.
**Nimrod Avni** 23:00 No, so I think… yeah, so we just, like… So, wait, so we don't need to do all the environment variable reading? We just give… I mean, we could do it, like, additionally, but as a first step, just, like, specify your port to ignore.
**Tyler Yahn** 23:17 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:18 Yeah.
**Nimrod Avni** 23:19 I think that's also a very quick… change we can do, so I'll, yeah, true.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:25 Cool.
**Nimrod Avni** 23:26 Nice, thanks for the, suggestions.
**Tyler Yahn** 23:31 Cool. Alright, yeah, well, thanks for the suggestion from everyone, that was great.
And the quick online debugging.
Okay, the only thing left on the agenda is to go through open PRs, and just make sure we're making some progress here.
So, stepping back, the first one up is the trace export internal metrics, with BPF internal metrics. Nimran, this is also from you.
**Nimrod Avni** 23:55 Yeah, I, I… I mainly just… I re-rebased it, I think today, and just, like, all the test passes, so… I had an issue last week where it didn't, now it passes. I didn't change anything. I think I… I changed something, I changed some, like, config test.
But I think it's just ready for re-review.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:17 Okay, yeah, it's just looking… yeah.
**Tyler Yahn** 24:19 Go ahead.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:20 Okay, yeah, I just wanted to confirm, so there's no spans being generated for… In… as trace paths anymore? Or is that still a problem?
**Nimrod Avni** 24:30 No, that wasn't, never a pro-.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:33 Oh, okay.
**Nimrod Avni** 24:33 The only change I made with, traces is instrumenting the trace, like, the normal, like, the application trace exporting. I just added some internal metric to, like, how many spans did we export, and how many… it's not, like, exports OB spans.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 24:51 No, but what I mean is that, I don't know, maybe last time it was, like, lost in communication or something. We… So, when you enable internal metrics, initially, when we did this, and maybe it was done differently, I can dig up the code.
When it would… you enable the internal metrics for the exporter.
Not only that it collects some metrics, it also generates a trace span every time it exports.
So it generates a trace band to Jaeger, for example, with Obi as an application.
And it just pollutes your, your database with all these spans, they're… I mean, to any customer, not very useful. And I… there may be, like, an option that we had done to enable this. I will confer.
I will confirm your PR, I'll take a look.
**Nimrod Avni** 25:51 I can also, like, I didn't change… I only changed, like, the internal metrics part of it, no, like, internal traces.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:00 But I think we need to…
**Nimrod Avni** 26:00 Add more internal metrics instead of.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:03 Oh, okay. But I… okay.
But I thought you enable the… Okay, just make sure that whatever you're doing in Jaeger, you don't see, or whatever trace database you're using, you don't get, like, spans from OBI that are just exported this, exported that, and so on.
**Nimrod Avni** 26:20 That's all.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:21 Because, that's what happened to us. I think Mark did the work, that's why he commented on this.
Initially to enable this internal metrics, if the internal metrics are enabled. That's a similar change, if I… if I'm not mistaken, where you enable the… if you're enabling internal metrics, then you tell the exporter to enable its internal metrics, but unfortunately it makes those spans, and maybe it was us using some option to enable that.
But… For our customers, it was very confusing. They're like, what's this thing?
Why do I need to pay for this, and whatever.
You know, people get… I mean, internal metrics is one thing, but… Why not?
**Nimrod Avni** 27:04 Damn.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 27:04 There's junk traces, yeah.
**Nimrod Avni** 27:07 Totally. So I'll, make sure, again, I'll check that.
And, yeah.
**Tyler Yahn** 27:13 Okay, awesome.
Alright, so moving on. The next step is fixed Prometheus metric export is missing the SDK version in Target Info.
Let's see… I think, yeah, this is something we talked about. Mario has been working with the author on this one.
**MM Mario Macias** 27:30 Yeah, no, no response.
**Tyler Yahn** 27:33 Yeah, okay.
**Rafael Roquetto** 27:33 I will ping… I will ping him. I'm… I'm in touch with him, on… on Slack, so I'll see. He's also part of the C++ sync?
So he shows up there a lot, so I'll ask him if he's still gonna do something about that, or not.
**Tyler Yahn** 27:49 Yeah, okay. Alright, thanks, Raphael.
**Rafael Roquetto** 27:51 No.
**Tyler Yahn** 27:54 Okay, next up, refactor the NetOle Tracer Part 1.
I feel like I just saw this, how's this 2 weeks old?
**Rafael Roquetto** 28:02 Yeah.
**Tyler Yahn** 28:04 Cool. Alright, Rafael, wanna talk about this one?
**Rafael Roquetto** 28:07 Yeah, I promoted it last night to, Yeah, no draft, so this is… this is something that I had been working in the past, like, month.
And then, there was a different… I don't know if you remember, there was a different PR work in progress. I mean, it looked the same, but it was a different PR that was, like, a more aggressive refactoring. I closed that one, and it just, got the lessons learned from that one into… into this. So this, basically, what it does is we… the Network Observability Tracer, The, current implementation… It gathers statistics in a map, and then it drains this map… From kernel space into user space.
By iterating this map. And this… this was showing up a lot in the profiles, like, and… and I thought, okay, how can I… optimize that. So, long story short, I got rid of that map.
And instead, we just pushed the flows into the ring buffer. This was the original implementation. The problem with the pushing things to the ring buffer is that it was generating a lot of context switch between kernel and user space.
Because, okay, we… I mean, you have thousands of… those events coming into your space. So, what this refactor does in a nutshell, part of it, or the most part of it, is… First, it tries to… it holds onto the… to this data into the kernel space, so VPF still has the same map that was being drained from your space there. But… Once it detects that the flow is over, or a certain time has elapsed.
Which was the equivalent of the… this map draining was being drained after, I don't know, every 10 seconds or something like that, or every 30 seconds of… you know, certain period. Then it pushes those events, those flows into the ring buffer, but it doesn't wake up the ring buffer, necessarily. So, the way it works is… It queues things on the ring buffer, and it flushes the ring buffer only after a certain time has been elapsed, or if the ring buffer is reaching its capacity, usage capacity. Then everything gets flushed at once.
to use space, and gets processed, like, batch processed to user space. So, that kind of did without all of these Yeah, bottleneck. The other thing that that it does.
We have two tracers.
For network observability. The original one that was using TC, And then we have another one using, the SOC filter, and the code was very similar between one and the other, so in the process of doing this, I kind of merged the code, because it is, like, 99% the same, so… That was the other thing.
And then there's some… there was some race conditions going on, I fixed that as well.
This is a… an interesting… Interesting challenge, because with the SOC filter EVPF programs, you cannot use locks. Like, spin locks don't… are not allowed, so it had to be, like, lock-free atomic operations. Hopefully, I got that right.
And yeah, and then, another thing that we did is we have an option to skip certain protocols, like.
maybe don't care about ICMP or BGP?
And this was being done in user space, so the event got delivered to user space, and then we checked the protocol, and maybe we dropped it in the pipeline.
That was very easy to do in BPF instead, so I pushed it to eBPF space. So when we see the packet, and we check the protocol, if it's not allowed, we don't even push it to user space to begin with. So this is… pretty much what this does. The other PR, the work in progress PR that I closed, was, did fare more in terms of, optimization and refactoring.
for instance, it used… instead of using subcomputer programs, it used secret programs, which was easier to manage, but I hit a wall with that, which we need to… we need to… we care about flows going from virtual network interfaces to virtual network interfaces, and because the SQL programs run at a socket level, we didn't have that kind of visibility, so I had to do without that.
And it refactors other parts of the pipeline, which I haven't done here. So, the network accessibility pipeline, there are several nodes, you know, you get the event, and then it gets enriched by Kubernetes metadata and other other parts of the events, and I… collapse that into a single node to avoid allocations and copies, but that's, like, also radical, so I thought I would leave this without for this PR. Most of the optimization gains are… by getting rid of the map iteration, so I did that. The couple of questions I wanted to ask about these overall, when we… when we enrich the event with Kubernetes metadata, the… or the attributes, they are in the map.
So, every time… We got a new flow, it goes through the Kubernetes enricher, and… Yeah, we… we keep adding to this… this attributes map with the new, whatever, Kubernetes container, namespace, all these Kubernetes attributes. And there is a… I… it's not a lot, but it shows up in the profiler, this map assign, map hash, you know, because it's happening For a lot of flows per second.
So what I did on the other PR is I got rid of that map, and instead, I changed the data structure to have actual fields. So there is a field, like, string Kubernetes, spot name, string Kubernetes, whatever, which we lose a bit of flexibility.
But for 90% of the things we're enriching, it ends up in the right slot, so there's no… like, once we allocate the object up front, there's no further, like, map allocation or anything like that, so that… that showed a bit of performance improvement, and I still kept them at 4 attributes that don't fall.
into these categories, like these common ones, maybe we'll have something else. But they are minor. So, the downside of that is that you end up with a bigger data structure and explicit code to, you know, fill in those member variables, if you will, on that structure. Is this something that we'd be interested on doing in a subsequent PR, or… Or is it, like, not worth it?
Any thoughts?
If that makes sense.
**MM Mario Macias** 35:39 Yep.
**Rafael Roquetto** 35:43 Okay. We can see it maybe in more detail with some…
**MM Mario Macias** 35:47 cold, or… Yeah.
Okay, okay.
**Rafael Roquetto** 35:51 Okay.
**MM Mario Macias** 35:51 Yeah, just as you said, I don't see anything against.
**Rafael Roquetto** 35:57 Okay, yes, I'm not strongly opinionated with that either. I just thought I would mention, because that was the another point of optimization that I saw. It's very low priority, so eventually I might raise a PR with that.
Yeah, the last thing that I have, the failing tests, maybe… I don't know if Mario or anyone else could help me. Not the integration test, not that one that's, flaky, but the Kubernetes one.
It's… I was trying to debug it, I don't know if… Yet, if it's related or not.
If you could scroll down a bit and find the error.
So yeah, it's failing, where is it? This transformer's cache, matrix Decoration AA, wait for components, so something… This is not coming up. Do you guys have any idea what could be going on here? I will look… I'm looking into it, but maybe it's obvious to someone?
You're mute, you're muted, Mario.
**Tyler Yahn** 37:03 What?
**Rafael Roquetto** 37:04 You're muted.
**MM Mario Macias** 37:05 I'm thinking, like, it's.
**Tyler Yahn** 37:06 720 seconds right there, right? I'm guessing you're probably hitting a timeout, is what I'm guessing.
**MM Mario Macias** 37:12 Yeah, that… that usually happens when, for example, OB, crashes… or stops working suddenly, then the unit just keep waiting for… for the… for the data. You can see if it has crashed. If you click in the summary, you can download the logs of the execution, and then you can see there if Inovi…
**Rafael Roquetto** 37:44 Okay.
**MM Mario Macias** 37:44 see below KA test logs. Otherwise, just execute it locally and see if… At a transpoint and see if… do some manual tests.
**Rafael Roquetto** 37:56 Okay, okay, cool. I'll get to this.
Thanks, yeah, that will be all for this, Pierre.
**MM Mario Macias** 38:03 We… we can anyway, next… next day, join and together, I mean, sit together and… and try to guess what's happening.
**Rafael Roquetto** 38:14 Okay.
Sounds good. Thanks.
**Tyler Yahn** 38:18 Awesome. Thanks, Rafael, for this. It's a lot of work. So yeah, definitely, excited to see this go through, so I appreciate it.
Okay, next up, there's a draft PR.
I don't know if I see Steven on here… author's not here, so let's probably skip over that.
update all patch versions, maybe we can talk about this one for a second. So, I took a look at this, Mario's taking a look at this, still taking a look at this. It looks like… so, the Prometheus, upgrade itself is causing some problems.
Which, just to be clear, like, we're not unique there. It's causing problems for a lot of, repositories right now.
One of the things that they did change is that the… the parsing is all, different now is to support name parsing for OTEL standards, so if you have things that are in an OTEL format, like, you can parse them correctly and handle it. So to do that, they added configuration options, so that means that, like, I've already updated some changes where I found it that will change.
the tests are still failing on this. They're not, transient, it looks like. I've tried to look into it a little bit, but it's still… I'm not exactly sure where the rest of the failures are coming from, so still looking into this.
Yeah, as Mario's pointing out, like, something broke here, so we still need to investigate a little further. Obviously, I fixed some things, there's still more things to fix here, though, so, yeah.
Mario, have you had a chance to take more of a look at this, or is this still just something on the backlog for you?
**MM Mario Macias** 39:51 It's still in the backlog. I was yesterday looking for it, but since we have other…
**Tyler Yahn** 39:57 Yeah, okay.
**MM Mario Macias** 39:58 other… other stuff in the backlog, I… I still haven't.
Yeah, I'm.
**Tyler Yahn** 40:02 Doing the same. I spent a few minutes here and there, and haven't found anything immediate, obvious. So, okay, we'll keep… keep working on this one, then.
Okay, next up, the foreach input pattern wrapping, open to discussion, something from Mario.
**MM Mario Macias** 40:18 Yeah, basically, in each node in our pipeline, Reproduces this pattern.
So I just suggested, putting this pattern into a… into a function, so… because sometimes we forget… a part of this has some verbosity in some simple notes, sometimes we forget.
Checking for the context, or checking for the input channel being closed.
And some… then… so then it causes that some nodes, when you try to stop OBI, some nodes keep still looking for that, and it… it delays sometimes, many seconds, the destruction of… of… of the process.
So, yeah, basically, if you like this… This… replacing that code on top by this for each input below, we can… we can discuss it, we can merge it. In this pull request, I create this… this function, and I… I replace… I… I use it in multiple parts of the code, just to see how it… or look.
So, yeah, just feel free to comment, or to shield that and say, no, it's… it's… It's not nice, as you… It's just a request for improvement, but…
**Tyler Yahn** 41:50 So how do you handle the… Like, yeah, so this is one of the things that I'd be interested in, because, like, right here, it actually returns from the function.
**MM Mario Macias** 42:00 Yeah, these… yes, basically this for each input is the last function in the… in the… is the last… is the last function of the… in the last function invocation, so when for each input exits, it… It… the instrument that they will loop, will exit anyway.
**Tyler Yahn** 42:22 Yeah, but how do you return from this function signaling that forEach should return?
**MM Mario Macias** 42:27 of a… No, yes, this is because in… in this pattern, we don't… we don't exit for this, or… or we don't… we don't invoke, or we don't have any mechanism to… to get out of… of here. This return, you can see, for example, in the process events, this is inside the for each input, which is… this is the common pattern. Usually, we only get out of this function when the input channel is closed.
or when the context is done. And this is handled inside the foreach input. So in that function we pass, we only put the process and forward mechanism. If we had to implement something that is outside of this pattern, we should… we… we cannot use the 4H input, we… we should stay with the normal And…
**Tyler Yahn** 43:23 That's… so that's… that's not what this is doing here, though.
**MM Mario Macias** 43:26 Yes, for each input, it's doing this inside, so we don't.
**Tyler Yahn** 43:31 So, like, what was happening before was it was iterating over this, and then when it accepted an event from this process event channel, and the OK was not there, meaning that it was closed.
**MM Mario Macias** 43:42 Yes.
**Tyler Yahn** 43:42 This outer loop actually returned.
**MM Mario Macias** 43:46 Yes, and this is handled correctly inside the… inside for each input. So, basically, for each input, what does is, it does this for, select, those initial lines you see from… From here, okay, you can see, it follows this same pattern.
**Tyler Yahn** 44:04 Oh, okay, I see, sorry. So, the return, you're still doing this, okay. Yes. I missed that for.
**MM Mario Macias** 44:09 I hadn't.
**Tyler Yahn** 44:10 Description, okay.
**MM Mario Macias** 44:10 Yes, it just invokes the action.
**Tyler Yahn** 44:13 Yeah, okay, I gotcha. I'm sorry, I missed that. The description didn't have this, but this makes more sense now that I see the actual code.
Okay, yeah, cool. This looks good.
So yeah, you're just looking for more reviews on this?
**MM Mario Macias** 44:29 Yes, I'm… I've replaced it in some parts of the… of the earth.
Of the cold base, just to see how it will look.
**Tyler Yahn** 44:40 I think this is a great… yeah, I think this is great. Oh, no, it was here in the original as well, sorry, I'm… I'm… Going crazy.
Yeah, okay, then let's just get some reviews on this, yeah. I think this is a great optimi- er, cleanup of the code, so I appreciate it, yeah.
**MM Mario Macias** 44:56 Cute.
**Tyler Yahn** 44:58 Any other comments on this one?
Okay, this is a dependency update, so let's skip that. Next up, Mario, you also want to talk about internal tools go mod, 124 Go Directive…
**MM Mario Macias** 45:13 Yeah, it's not yet working. I need to fix the old test. Basically, currently, we have followed some approaches to get the tooling, to download the tooling.
Currently, we are setting them into a… Go… you see these internal tools, and we… we don't load it from there. But now… the… since Go 124, you can just set or specify your tooling inside the Go mode for… using the tool directive, and then you can use it just, invoking… you can invoke it via Go tool.
And Go will… Go will… will download and compile and run it for you. You see this?
**Tyler Yahn** 46:04 Really? Oh, this is cool.
**MM Mario Macias** 46:06 Yeah.
**Tyler Yahn** 46:06 Yeah.
**MM Mario Macias** 46:07 So now… now instead of downloading locally BPF2Go and invoking it, you're just specifying it there, you… you run go to BPF2Go, and it will run it.
And this… this is aware, or this is repository aware, so if you run it in another repository, or outside your repository, it won't work, or it will get another version.
**Tyler Yahn** 46:30 Right, it'll do whatever's there, I see. Yeah, so it's local only, yeah.
**MM Mario Macias** 46:35 Yeah.
**Tyler Yahn** 46:35 Yeah, this is awesome. So how does this… so then in the Docker images? Oh, yeah, okay, so you don't even need any of the extra context Yeah, okay.
**MM Mario Macias** 46:44 Yeah, yeah, I need still to do some fixes, especially in the… in this old testing that is using another approach, so I will need to do some extra changes. It was just a proof of concept. I don't think it's something urgent, we need to vet, because what we have works, and it's not super complex, but… Since there is a standard tooling for that, yeah, maybe it's good having.
**Tyler Yahn** 47:10 Yeah, I… I'm, like, super excited about this. This is gonna clean up a lot of repositories, so yeah, I… It's not urgent, but boy, I want this, so, yeah.
Awesome, okay, yeah, cool, I'm excited about this one.
I will keep an eye on that. Next up, Mara, you also have fixed tests and meta-inter in, for non-Linux?
**MM Mario Macias** 47:32 Yes, this is because this… recently, this JVM tool was introduced as a dependency, and it's a Linux-only dependency that is invoked from some… from some code that is visible by non-Linux codes, so the linting and testing fails. It's just those few… it just moves the invocation to this to another Linux and not Linux.
**Tyler Yahn** 48:03 And at least you can keep with…
**MM Mario Macias** 48:06 Unit tests and local linter.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 48:10 Yeah, this is again my fault.
Yeah.
**MM Mario Macias** 48:15 It's unavoidable, as long as people only has Linux, it's unavoidable, so no problem. It's quick to fix.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 48:24 I don't know if you guys saw this PR, but we're trying to make the roots, extract them from executables and… Parts, so, So we'll have actually correct routes rather than the star thing we do with the heuristic.
This should help with folks that are actually generating, maybe, traces with SDK, but they're using Vela for metrics.
And then, then, if you link the trace, it will actually… by the route, it will work. So, say you find a metric, this route was bad, then you can hit your trace database, and you can find what slow requests were happening there. And you can do it with tracing with the Java SDK. So it's sort of the same thing we do, kind of, like, detect that the application is sending traces itself, so we don't send traces.
But you send metrics with, Obi, then you, you will… The roots should match, so…
**Nimrod Avni** 49:20 That's cool, like, I didn't… I saw the… It's like an in… I don't know what's the JVM package, I think… I think it's some Grafana internal thing. It just, like, parses the, like, JVM symbols, or something like that?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 49:35 Yeah, we can… we can actually… there's no reason that's separate. If you guys want to bring that in, we can bring it in. We just had a separate project for that, but… I'm totally fine with moving that into OB, we don't use it for anything else.
**Nimrod Avni** 49:48 I just was, just for curiosity of how it does it, because I wanted to.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 49:53 Yeah, so it's actually… there's a C tool, and it's called JAttach, which is implemented in C. We just ported that to Go, right? We didn't invent this, but when you run a JVM, it opens up a Unix socket in a specific location that you can talk to.
And it has its own internal protocol and whatever, but… and the JVM has a Java program for talking to that, so it's an open protocol, you sort of know what the protocol is. They have JCMD.
And so this is a translation of that tool in Go, so we can easily use it in OB. And… Essentially, what he does is, like… ask the JVM, tell me all the symbols that you have, and then we look through the symbols and find the ones that look like paths, and then we process them and add them to the To the roots generation, so that… we have… Correct routes, rather than… Something that looks like a word, and we think it's a word, and it's part of the path, and we make it hard cardinality, this will avoid that problem.
So we're thinking of doing the same thing for Go, so since we already parsed the ELF binary, we can actually go in and look at the binary, find whatever path people declared.
maybe that'll work. I don't know. I haven't tried it, but… I mean, we parse the ELF, we just don't look for those things. We look for the methods, the functions, and offsets and things, so… I think… We'll find them as strings, and all we really need to do is now add them to our first service.
Alright, so I'll follow up with a PR today that you can… in your discovery section, as you kind of list, I want to instrument this, I want instrument that, you can also specify custom routes for that to be detected, so you don't have to have a global one, but you can have… you can say, I actually don't want any… any here… to be, like, outgoing, I won't starve for that, because it's high cardinality, maybe I'm hitting some crazy endpoint, and things like that, so you have a lot more control.
And after that, we can now actually add automatically what we discovered in Go, which you can later override.
If you have your own… those take precedence, but, yeah, so… It should be cool, I'm quite excited about this, because there's been one sticking point, people, like, well, if I use the SDK, I get this, it looks much better.
And you guys are putting these stars everywhere, I want to see what the actual thing was, and… ID, user ID, those kind of things, you know? It looks better.
We can extract them.
Now, I think for any executable that we parse, we should be able to find them, provided people with the strip symbols.
If this trip, administrative.
**Tyler Yahn** 52:45 Yeah, okay, that sounds good. I think that's interesting to look at. Thanks for working on that, and Sharon, Nicola, that's definitely cool.
I think that's the end of our open PRs. There is one more, from Raphael, but it's in a draft state, so I think we can, skip over that one.
**MM Mario Macias** 53:04 Hmm.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 53:05 selecting an agenda item there.
**Tyler Yahn** 53:07 I saw, you have added another agenda item, which is great. So, yeah, Nikola, you wanted to ask about this, PR?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 53:15 Yeah, I don't understand it, so maybe… I guess this was initially for… added to the auto collector?
Somehow, Matt made it here?
We… this is… I don't understand it, that's why I kind of brought it, if anybody had more information here.
**MM Mario Macias** 53:36 That looks to me as someone that got the wrong repository, maybe.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 53:42 That's what I think.
I mean, there's a… example there, but I think the example might be just our internal example or something?
Like, we have examples maybe we collect, or… Maybe it's just about to stop using those things?
Maybe they're just telling us, don't use the.
**MM Mario Macias** 54:05 Does anyone, examples?
Yeah, that must be in the… from the tests, maybe.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 54:11 Yeah.
**MM Mario Macias** 54:12 Yeah, okay, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 54:14 So, I mean, I guess it's fine, like, maybe we can… Take out this. Okay.
Processor's batch.
Okay, that explains.
**Tyler Yahn** 54:23 Oh, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 54:24 confused, it's not an OB change, it's actually they want us to remove it from the test changes.
**MM Mario Macias** 54:29 Oh, God.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 54:30 Oh… Yeah.
**Tyler Yahn** 54:42 Yeah, okay, that sounds good. So the idea is we'll just go through and try to do updates on this.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 54:48 The collectors… Configurations that we use to remove the batch processor.
Is it being removed?
From the collector, I guess.
**Tyler Yahn** 54:58 Yeah, I guess that's the kind of the question.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 55:01 Fair.
**Tyler Yahn** 55:02 Well, I don't think the processor's being removed, it's just more the configurations. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 55:07 Or maybe we had, like, empty bad roasters, yeah.
Okay.
**Tyler Yahn** 55:35 Okay.
Yeah, alright.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 55:39 Cool.
**Tyler Yahn** 55:40 Awesome. Alright, so that looks like the India agenda.
I can stop sharing screen. Again, if any… did anybody else have anything else they want to talk about? Another issue?
their PR… Cool. Any cool projects you guys have been working on? We have a few minutes to share.
Obi, yeah, there you go.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 56:10 Mattia and I were talking this morning, trying to figure out if we can actually support cgroupv1, with our context propagation. So, trying to find the right spot to add the socket into the map to be tracked, sort of… Yeah, absolutely.
**Mattia Meleleo** 56:26 doing the experiments over that, I found a couple… I found one kernel bug, I think.
And the one library bug. For the library bug, we discussed with… we talked a little bit with the Celium VPF maintainers.
For the kernel bug, I'll leave it there, I mean, it's too much for me.
But yeah, we discussed with Nicola where, where might be the, the, the best point to… To add this, value to the map.
I'm doing some experiments right now in the ingress path, right after the last ARC flag is received.
So the fir- the first, established, socket established point we can, we can find to see if we can, Managed to, to start instrumenting… not instrumenting, to start enriching after the first request.
But yeah, I'll also do some more research if we can, somehow track these sockets, right from the first request. Because the issue is that with the SOCOps program.
We can track the socket event, changed, like, to established, as soon as it's made, so… and the program gets attached to the socket path.
at that time, so it gets executed as soon as possible, but with TCs, it's much harder, and the socket needs to be in the established state. That's the hardest part.
Yeah, we are still experimenting.
We're crossing fingers, and… Hope this works.
**Tyler Yahn** 58:21 Awesome.
Yeah, well, keep us posted, let us know.
Okay, at that, I think we're almost at time, so we could probably end the meeting here. Thanks, everyone, for joining, appreciate seeing you all, and I'll see y'all in a week's time, or asynchronously.
Till then. Bye.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 58:36 Cool. Bye.
**Nimrod Avni** 58:37 Meh.
