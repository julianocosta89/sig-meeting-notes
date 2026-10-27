SIG: Networking SIG
Date: 2026-10-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Sven Cowart (ElastiFlow Inc)** 00:32 Oh, good morning.
**Serena Kei (Raintank, Inc. – Grafana Labs)** 00:38 Good morning.
**Sven Cowart (ElastiFlow Inc)** 00:44 What were you climbing in your picture?
**Serena Kei (Raintank, Inc. – Grafana Labs)** 00:47 Oh, this was, I think it was… Ugh.
I forgot the name of it, it's called Rock something.
Rock on, and squad.
**Sven Cowart (ElastiFlow Inc)** 00:58 Oh, sweet.
**Serena Kei (Raintank, Inc. – Grafana Labs)** 00:59 Yeah.
It was, I think 2 years ago, I went with my husband.
**Sven Cowart (ElastiFlow Inc)** 01:06 Oh, great.
**Serena Kei (Raintank, Inc. – Grafana Labs)** 01:08 Hello.
**Sven Cowart (ElastiFlow Inc)** 01:09 Where's Rock on?
**Serena Kei (Raintank, Inc. – Grafana Labs)** 01:10 It's, like, do you mean the city, or…
**Sven Cowart (ElastiFlow Inc)** 01:15 No, no, the location. I mean, that looked like outdoor climbing, right?
**Serena Kei (Raintank, Inc. – Grafana Labs)** 01:19 Yeah, yeah, it was outdoors.
It's like… It's in Squamish, like, Vancouver, BC area.
**Sven Cowart (ElastiFlow Inc)** 01:27 Awesome.
**Serena Kei (Raintank, Inc. – Grafana Labs)** 01:28 Yeah, where are you based out of?
**Sven Cowart (ElastiFlow Inc)** 01:30 Dana Point, California.
**Serena Kei (Raintank, Inc. – Grafana Labs)** 01:33 Okay.
**Sven Cowart (ElastiFlow Inc)** 01:33 We'll go from there.
**Serena Kei (Raintank, Inc. – Grafana Labs)** 01:35 Yeah, you probably have a lot of climbing there, too.
**Sven Cowart (ElastiFlow Inc)** 01:38 Yeah.
Hey, Steven. Hey, Giuseppe.
**Stephen Amstutz** 01:46 I'll…
**Giuseppe Ognibene (Coralogix)** 01:47 Are you…
**Sven Cowart (ElastiFlow Inc)** 01:48 Some new faces, I'd love to see it.
**Serena Kei (Raintank, Inc. – Grafana Labs)** 01:54 I'm pretty new to, open telemetry, so I'm mostly listening for now.
**Sven Cowart (ElastiFlow Inc)** 01:59 Okay.
**Serena Kei (Raintank, Inc. – Grafana Labs)** 02:01 But yeah, let me know if there's something I could help with.
**Stephen Amstutz** 02:05 Yeah, same here, pretty much. I did a lot of work last year, specifically around networking,
**Sven Cowart (ElastiFlow Inc)** 02:11 Well, awesome.
**Stephen Amstutz** 02:12 And then I left… I didn't leave, I finished what I was doing, and I haven't really touched it for 12 months, and I had a look during the week, and saw that this group had formed, doing a lot of what I was trying to do a year ago.
Awesome. So, same thing, if I can… contribute, I will. Otherwise, yeah, just wanted to listen alone.
**Sven Cowart (ElastiFlow Inc)** 02:29 Okay.
What were you trying to, get done?
**Stephen Amstutz** 02:33 So we have an observability system, and it was pretty proprietary around using APIs to various vendors, and I was trying to standardize as much as possible, so I was doing a lot of work with the semantic conventions.
I was also building a, discovery element, using CDP and LLDP to kind of, map a network.
So I had to create some custom extensions to do that, and they're not too different from, what this group is doing.
So I thought it was reasonably relevant, and, might be worth joining.
**Sven Cowart (ElastiFlow Inc)** 03:12 Yeah, yeah, I just… we're trying to head that way right now. So what we're trying to do is write what's there, and set a good foundation for more network telemetry. Hey, Antonio.
**Antonio Martinez (Cisco Systems, Inc.)** 03:28 Alright, well.
**Sven Cowart (ElastiFlow Inc)** 03:29 Was that you jotting down a bunch of notes in the doc?
Antonio?
**Antonio Martinez (Cisco Systems, Inc.)** 03:37 Could you repeat the question? Sure.
**Sven Cowart (ElastiFlow Inc)** 03:39 Is that you putting down a bunch of notes in the doc?
**Antonio Martinez (Cisco Systems, Inc.)** 03:42 Yeah, it might be me.
**Sven Cowart (ElastiFlow Inc)** 03:43 Okay.
**Antonio Martinez (Cisco Systems, Inc.)** 03:44 And we're setting it.
**Sven Cowart (ElastiFlow Inc)** 03:44 obvious, I don't know why, but, I didn't get it.
**Antonio Martinez (Cisco Systems, Inc.)** 03:50 Against the ice cream.
**Sven Cowart (ElastiFlow Inc)** 03:53 But yeah, I think we're gonna head that direction, with, discovery and those things. I think it's a little bit… It feels like it's a little bit stuck, that part, because, I think there's good reasons to focus on the entities that would be produced out of a discovery process, and right now, no one's putting the appropriate focus on entities, because I think we're, like I said, trying to just set down the right foundation that… for, A lot of the things that exist.
**Stephen Amstutz** 04:31 I think when I was working with it, entities weren't really a thing, or they were about to become a thing. So as far as, how to refer to interfaces versus devices, I did a lot of, kind of, preliminary work around that.
And again, I was kind of checking the status of entities to see if it had come along at all, since I'd done the work I'd done.
**Sven Cowart (ElastiFlow Inc)** 04:55 Yeah.
Are you on Slack? On the CNCF Slack?
**Stephen Amstutz** 05:00 Not yet. I'm, because I'm using my corporate email, I need to get that approved. We're not a company internally, but, I'm… I've started the process off of that today, so, hopefully I'll be on soonish.
**Sven Cowart (ElastiFlow Inc)** 05:13 Okay.
I'll drop, you should have access to this doc, I'll…
**Stephen Amstutz** 05:18 I have seen this from last week, so yes, I did see that.
**Sven Cowart (ElastiFlow Inc)** 05:22 I'll drop some links that are relevant that have been discussed in the past around… that aren't yet either GitHub issues, but should be, around network interfaces and, the BGP.
Entities that… were drafted up by someone else in the part of the SIG, Rob, but he's been down in the weeds with a bunch of other things, because he's not… he doesn't have full-time capacity to help contribute here, so it's kind of stalled out there. But I know there's, there's another… someone else, I believe his name is Mark, if I remember right, who's also trying to tackle this same problem, specifically around discovery, and entities that would be produced out of discovery processes, And I know we are heading there very, very, very soon, so it's going to… we're gonna have full-time capacity to work on it, because it is a thing that we actually need to do, so…
**Antonio Martinez (Cisco Systems, Inc.)** 06:17 Correct.
That's really cool.
Okay. Thanks meeting you also, Stefan. From my side, as you said, I have a few notes. Those notes are coming from the last one, but you were not there. I think they are important. So those three pull requests are ready for being merged, so I'm asking the maintainers to take a look, so they will be merged soon, hopefully.
For the SNMP, as I guess all of you already know.
**Sven Cowart (ElastiFlow Inc)** 06:45 Antonio, on… on map, did we land on… Dot Mac, dot… yeah, okay.
**Antonio Martinez (Cisco Systems, Inc.)** 06:52 address. Yeah, we had approval from… not approval, Lyudmila put a comment saying that that's the way how we should proceed, so yeah, that was…
**Sven Cowart (ElastiFlow Inc)** 07:02 Okay, awesome.
**Antonio Martinez (Cisco Systems, Inc.)** 07:04 There was… there was a lot of back and forth with that user, but yeah.
There is no need.
Okay, moving on.
Braydon's here. For the SNMP receiver, Sven and I, we became code owners, and we need to start investigating what are the current status of that project, and we want to plan a roadmap.
For the moment, there are some existing issues, like the most interesting one is supporting the traps logs, like the notification.
I put together a couple of pull requests for, for supporting that, so whenever you have time, like Mark, the guy that you were mentioning, that one, he already provides feedback to one of them, so Rice provides feedback whenever you have time. Yeah, happy to apply.
Out of those ones, there was, a couple of GitHub that were… sorry, GitHub issues that were created. One is, enrich the MIPS file, pull up tickets, so today we are always putting the old ID, but we need to have, like, if we have those files, we can do the mapping properly. That will be, like, a follow-up ticket.
And then the next one is… I was proposing, like, now that we have… I don't know how familiar are you with the… with that SNMP, collector… sorry.
But today, the… I don't think there's another one.
**Sven Cowart (ElastiFlow Inc)** 08:45 On the, On the MIP files, what's the thinking there?
**Antonio Martinez (Cisco Systems, Inc.)** 08:57 Current, the idea, like, without jumping to the next one, the idea here is, like, we can use something similar as, Prometheus SNMP Exporter is doing today, optional PIPS name for enrichment, and that… there will be the mapping, honestly.
But yeah, the idea is, like, we will do some exploration before jumping into a solution, I guess. That's why I created also that issue, so if any of you guys have a proposal, it would be more than… Then work on here. But if not, let's follow up with something similar as Prometheus is doing today, I guess.
**Sven Cowart (ElastiFlow Inc)** 09:36 Okay, is this just asking that we put the MIB Name into the export?
**Antonio Martinez (Cisco Systems, Inc.)** 09:44 Yeah, yeah, that's the main thing.
**Sven Cowart (ElastiFlow Inc)** 09:46 I see.
And that's then to help the… someone who receives the trap to understand symbolic conventions and those things.
**Antonio Martinez (Cisco Systems, Inc.)** 09:58 Correct, because only having the, those IDs are quite confusing, unless you are an expert at those, I guess.
**Sven Cowart (ElastiFlow Inc)** 10:05 Yeah, yeah, this is the challenging part of SNMP.
The most challenging part.
**Antonio Martinez (Cisco Systems, Inc.)** 10:11 Right, right.
**Sven Cowart (ElastiFlow Inc)** 10:13 We've spent a lot of time on that internally in our SNP collector.
And… this is the large standardization effort, or I don't know if you remember Rob bringing up that he's been trying to normalize SNMP into his common semantic conventions, that's what he would do. So, I mean, I think the long… that's decent enough for now, but the long-term solve would really be standardization.
into… common and generic semantic conventions based on a large collection. Oh, shit. Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 10:46 Absolutely, that would be, like, the long term, because right now, I don't know how familiar are you guys, but right now, we give the capability to each user to create their own attribute our own ad magic names, which, it's fine, we… I think we always need to provide that.
But we also need to support, like, as you just said, we have a standardization. Addresses are always going to be network.peer or log marked.address, and that's with something that is auto-generated, based on the old IDs, I guess.
Yeah. So yeah, that's something that we need to work. I totally think that's the main complexity of the SNMP receiver today. Like, people have to build those… their own data, or any other receiver today, they… That is really solved.
So yeah, we will need to, I guess, still support that flexibility, but we will need to put the… the one that appears in the semantic convention will need to be false, I guess.
**Sven Cowart (ElastiFlow Inc)** 11:44 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 11:46 Okay, the other ticket that I put, that I created was, refactoring the pool configuration. So, when I started supporting the… traps in the logs, what they did was, actually, I split it in two, so that was existing configuration, and then I put another one, which is called traps. And then what they did is, like, all of that, I put it inside a new parent call.
pool.
And then Mark, which I really like his proposal, is like, before we just move all of those into the new Hey, and they're a new parent, what about if we refactor those configurations? And then he suggested that we use a similar approach, also, as they are using on the Prometheus Exporter today, something on those lines, like Endpoint for sure and collection interval, and then SNMP exporter, where you're gonna have, like, a configuration file that is gonna be the same file that you're gonna be using in other collectors, and then you're gonna specify your authentication and your model there.
That is a proposal, as I said. Here, we are looking also for an alternative on how we can do that, but we should start thinking about also how we can improve the configuration, because from The problem that he explains, like, every time that he goes to a different platform, he has to build that config file again, and that's quite a pain.
So if we can reuse it somehow, that would help.
**Sven Cowart (ElastiFlow Inc)** 13:17 re… reuse what? What do you mean, though? Like, support… Specific platform configuration files.
Or come up, only refactor once, and support.
The structure that we want to support moving forward.
**Antonio Martinez (Cisco Systems, Inc.)** 13:34 I would say the structure that we support moving forward, that would be the.
**Sven Cowart (ElastiFlow Inc)** 13:37 Okay.
**Antonio Martinez (Cisco Systems, Inc.)** 13:38 solution.
**Sven Cowart (ElastiFlow Inc)** 13:38 Yeah.
Here, because if we have…
**Antonio Martinez (Cisco Systems, Inc.)** 13:42 Because I don't think there is, like, a standardization for that today.
**Sven Cowart (ElastiFlow Inc)** 13:45 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 13:46 I doubt.
**Sven Cowart (ElastiFlow Inc)** 13:48 Yeah. I think it's… before we commit to anything here, I think, you and I need to just sit down and really bang out.
I need to, one, get caught up on how this SNMP receiver actually works, and then bang out what the actual architecture needs to be for it, based on some of the things that… the one that we have internally, because… I do strongly believe it's one of the better ones that exists, because of the way that our discovery process and pruning process avoids work. Because a lot of, I don't know if you know this, but a lot of, like, S&P receivers are pretty… naive and dumb. Like, if an OID is configured to respond, but then the device… that specific device doesn't have the OID, it'll just respond with Like, not available, or I forget the exact… response message that gets, and then they'll just keep polling for it. But that kind of thing needs to be pruned out, automatically.
And, and then the way that you can apply different deployed discovery and… Schedules based on groups and… subgroups of items. I think we did really well in our configuration.
So I think we just need to, like, I need to take the time.
to sit down, figure out what the S&P thing is, and then together figure out, like, what is… The architecture that we want here, and then from that, we need to create a configuration structure that makes sense to support that.
**Antonio Martinez (Cisco Systems, Inc.)** 15:13 That could be the idea, yeah, that would be awesome.
So here we have a couple of examples. The Prometheus exporter, most likely your, from your company, the CNMP receiver. So yeah, we can get the best from both worlds, I guess.
Hopefully.
So that's the current status today. Feel free, guys, to create new tickets, to create new pull requests, and we will try to be on top of that. Also, for… awareness. Splunk is donating the GeoName receiver. I don't know how familiar are you with the… with that new technology. It's like a gRPC for network telemetry data.
network management interfaces, so it's, like, the next phase, if I understand correctly, of SNMP, like, where data is pushed whenever there is, like, a change, or it's, like, more like an open telemetry and not saying it's, like, push approach rather than a pull.
And… and Splunk is donating to OpenTelemity, so we can also keep an eye there and improve it, or… I mean, try to follow a similar approach also that we're gonna do as an MP, most likely, but yeah.
For you to know.
And then for KubeCon, it's great that Braydon is here. Do we have any available slot, or do we need to request it somehow?
**Braydon Kains (Google LLC)** 16:36 So I haven't seen… Any, like… booking of, like, SIG calendar, like, would usually be there. I'm… I'm pretty sure, based on what I've heard, that there is no, like, observatory this year, so it's probably gonna be another, like.
at the project booths. I'll message Reese directly, she usually books that, so I'll message her today and see if that's… if… if that's happening.
If… if it's not happening, then we can kind of just… like, make a decision ourselves, hey, go at this… at this date, this time, we're all gonna go meet at the picnic tables, or something.
**Antonio Martinez (Cisco Systems, Inc.)** 17:17 Yeah, it will be kind of the same, yeah, if we put it there, or we set that ourselves, but yeah, it would be great if we have something more formal.
**Braydon Kains (Google LLC)** 17:24 If the official calendar is, in fact, happening, then I'll make sure we get a slot.
**Antonio Martinez (Cisco Systems, Inc.)** 17:30 That could be awesome.
Now that we are talking about KifCong, any… Any topic that you want to bring about that one, guys? Any topic here?
**Braydon Kains (Google LLC)** 17:42 Only to mention that I will… I will be there, and I won't have booth duty, because Google doesn't want me to do booth duty, so I'll just… I'll just be walking around.
**Sven Cowart (ElastiFlow Inc)** 17:54 I'll be there as well. I don't know if I have booth duty or not yet. I probably will.
**Antonio Martinez (Cisco Systems, Inc.)** 17:59 Makes sense.
**Braydon Kains (Google LLC)** 18:01 Both of my talks are on the Tuesday, so, Before and after, I'll just be hanging out.
**Antonio Martinez (Cisco Systems, Inc.)** 18:12 Yeah, looking forward to seeing you there.
And then Stefan is not here, but he also added that topic, how they are solving it into… Prometheus.
**Serena Kei (Raintank, Inc. – Grafana Labs)** 18:24 He's awesome.
**Braydon Kains (Google LLC)** 18:24 We… Sorry. Sorry, go ahead.
**Serena Kei (Raintank, Inc. – Grafana Labs)** 18:26 Off this week as well, but he mentioned he just wants to put it in there as awareness, so nothing other than raising awareness on it.
**Sven Cowart (ElastiFlow Inc)** 18:35 I…
**Braydon Kains (Google LLC)** 18:35 We have a thread in the Hotel Network Slack channel where we talked about this a bit, too.
**Antonio Martinez (Cisco Systems, Inc.)** 18:42 Oh, nice. Maybe it's that one, okay.
Okay, and we jump.
**Braydon Kains (Google LLC)** 18:45 Oh yeah, that's what he liked. Okay, makes sense.
I… TLDR is basically, like, I think it's kind of… Up to us to tell instrumentation to do that.
Since there isn't… like, as far as I can tell, any, guidance within… I mean, one of the… one of the guidance within, the OTEL protocol is that if you expect to overflow 64-bit signed integer, you should use a float instead.
But this… this idea of, like, float saturation isn't written anywhere, and… Most of the specs say, to… just default to whatever, like, the language runtime will do to handle overflow, which… I see why they said that, but it doesn't hand… it doesn't necessarily… Work super well for, like, how are backends supposed to interpret resets coming from generic metrics?
But I think for us, in our instrumentation, to say.
Float saturation should be with this… 2 to the 53.
Number… like, we can just… we can probably just say that in any counter that we expect to be big, and If we have that happening a lot, Then we can… Try and bring it up as a more general semantic conventions thing. Like, the… the… using 2 to the 53 for saturation is not a special networking thing, it's just, like, it's, like, based on the actual math of IEEE floats.
**Sven Cowart (ElastiFlow Inc)** 20:25 So…
**Braydon Kains (Google LLC)** 20:26 For us to potentially propose something to semantic convention rules in general to say, for floats.
For any float instrumentation, ever do this.
Probably isn't that far-fetched.
But, I don't know if we need to, like.
Push on it hard right now, necessarily.
**Sven Cowart (ElastiFlow Inc)** 20:49 That makes total sense to me.
As we get into that SMMP work, I think that's when this will become… more relevant. I was doing some math around this the other day for unrelated reasons, and I was having a hard time coming up with concrete examples of when we would need U64.
On counters, but I need to… So, I… I've… Based on my past conversations with Rob, it always seemed incredibly important.
So, I might be missing something really obvious, or we've made a bigger deal of something that it needs to be, and that for the scenarios where this Is relevant, we can just use this type of solve.
So, is… Well, when I read… I forget where I read this the first time Steam brought this up, but this is not yet implemented. Or is it?
**Braydon Kains (Google LLC)** 21:42 In the Prometheus Exporter, the SNMP Prometheus Exporter, I think it's implemented, or maybe the P… at least the PR is up. I don't remember if it got merged.
**Sven Cowart (ElastiFlow Inc)** 21:50 I see.
**Braydon Kains (Google LLC)** 21:50 but…
**Sven Cowart (ElastiFlow Inc)** 21:52 Oh, I think… that's right. This is… he was saying that Prometheus can ex… Receive that value.
**Braydon Kains (Google LLC)** 22:03 it's… yeah, so, like, the… the Prometheus Exporter, when… if, like, an app… the exporter itself has the Prometheus, like, API instrument, and I think it… what it does, and maybe we can check the PR to be sure, but, like, when that instrument goes over the It… It will, like, wrap the value to avoid… well, that's basically what the… The PR says.
**Sven Cowart (ElastiFlow Inc)** 22:31 I see.
**Braydon Kains (Google LLC)** 22:32 It'll wrap the value to avoid precision loss.
And I don't know if Prometheus has this same… Like, guide… specific guidance as the… OTEL protocol, but the hotel protocol says to use a float.
If you… if you think you're gonna… Like, overflow sign 64 in a common scenario.
And now I don't remember where that was, so I can try and find that.
I don't think Prometheus has… Prometheus is generally much more loosey-goosey with that sort of thing, so I wouldn't be surprised if there's nothing mentioned in, like, the open metrics protocol or anything.
**Sven Cowart (ElastiFlow Inc)** 23:18 Okay.
**Braydon Kains (Google LLC)** 23:21 I think on our side, we'll just, like.
Say, in instrumentation guidance to do this, like… In the note for every metric where we want this to happen, we say that, and then if it becomes so prevalent that we're saying it all over the place, that's the point where we probably bring up some sort of root SEMCOM rule about float instruments, like, how they're… how they should handle.
**Sven Cowart (ElastiFlow Inc)** 23:45 Right.
**Braydon Kains (Google LLC)** 23:45 float saturation.
**Sven Cowart (ElastiFlow Inc)** 23:51 Okay.
**Antonio Martinez (Cisco Systems, Inc.)** 24:00 Is it?
I have another comment. Do you remember that Robert Kitty that you were mentioning before, the interface?
attribute and interface metrics was here. The idea was that he was gonna create, like, a GitHub issue, proposing the different, fields, and then we can have a deeper discussion at that time.
was… Do you know if he's gonna do that, or are we… do we want to do that ourself, and then have his feelings?
**Sven Cowart (ElastiFlow Inc)** 24:31 I asked the same question last week of him, and…
**Antonio Martinez (Cisco Systems, Inc.)** 24:35 Nuts.
**Sven Cowart (ElastiFlow Inc)** 24:36 Said he'd do it, it's still not done. He got surprised with, having to move, because his landlord sold the property.
So, that he was living at.
So I know that's been consuming his last week.
**Antonio Martinez (Cisco Systems, Inc.)** 25:00 Bird?
Any other topic, guys?
**Sven Cowart (ElastiFlow Inc)** 25:03 Call up from me. I don't have anything to show for it yet, except for all the existing artifacts that I've created around this. But I will… the thing that's kind of top priority for me, besides this SMP work now, is the flow-based semantic conventions.
Like I said, I'd like to start moving on that, so that… I can help make those contributions in OBI.
**Antonio Martinez (Cisco Systems, Inc.)** 25:33 But are those flow semantic commands already… Created, or are they gonna be new?
**Sven Cowart (ElastiFlow Inc)** 25:39 No, they're new.
So it's… you know how, like, in, my… if you look at… I created a project called Mermin, just for background. It was EBPF instrumentation, of… Creating flow records out of any Kubernetes, or actually, any network traffic, but specifically more focused around Kubernetes CNIs, because I was tired of the fact that only, Why am I? I'm brain farting on the one.
Psyllium, then what's the second most popular?
**Antonio Martinez (Cisco Systems, Inc.)** 26:21 OBI, SIG.
**Giuseppe Ognibene (Coralogix)** 26:24 polyco funnel.
**Sven Cowart (ElastiFlow Inc)** 26:35 If I remember, oh, Calico.
They do some flow exporting, but it's not very great.
And I have all this documented in the Mermin docs, I can share it out. But more or less, what I want to happen, see happen, is that, you can install an eBPF agent, it generates flow records, and the question even for us, has been, what's the best way to represent flow records inside of OpenTelemetry? And not flow metrics. I know that's what OBI has today, is flow metrics.
And the… answer I landed on was, This should be a trace. And so what you have, then, is you have a… A network trace.
Which is a flow trace, and… application traces.
And the application traces are consumer, producer, client, server, and then you have flow-based one as well. And, And the reason it should be is because flow records have start and end times, so it naturally more fits into that, and then allows for easier, Correlation to… application traces.
So I've spent a lot of time working on that, and the convention for it already. It needs to now be refreshed because of some of the changes that we've worked on in here, and the things that have changed over the last 6 months, so… But that… that is my goal, is to take the work I did with Merman. Unfortunately, it was written in Rust, and so now I have to port it to Go to bring it into OBI, which is not a big deal, but… And at the time, when I was working on it, OBI had not been donated, it was still Bela, wasn't donated yet to OpenTelemetry, which is why I created our own, instead of trying to contribute it to Belux, I didn't really know what that process would look like, not being part of Grafana. And maybe that was short-sighted, I don't know, but I needed to… get this thing out. So I did, and And now I'm just gonna try to work on bringing all that functionality into OBI.
So that's kind of the… For me, the… Highest priority item.
Besides supporting all the other things that are already going on here.
**Antonio Martinez (Cisco Systems, Inc.)** 28:52 That's liquid.
And I mean, it's… You know.
**Sven Cowart (ElastiFlow Inc)** 28:56 No, go for it. I think you were gonna go to the same place I was about to go.
**Antonio Martinez (Cisco Systems, Inc.)** 29:00 Yes, so I imagine that was the reason why you asked me about my talk about how to convert and trace route into… Yeah, you were asking me about that the other day. I didn't have the slide, like, that subtle yet, but I think I have something for today, so… just for context, everyone here, I will be doing a talk about how to compare a trace route into an open telemet trace. That's something that we are doing in Cisco 1000ized, and our customer is using it already, but it was something, like, kind of new, and that's why I think it makes sense in Givecom.
So I'm not gonna go through the presentation, of course, but just to give you a little bit of light on that, the trace route is something like that, as you are familiar, so we have, like, an agent or a user or a computer doing a request to a target, and then we have, like, the delays, which helps with traversing, so on and so forth.
So what we are doing is we are normalizing those hubs, and we are adding extra enrichment, like the reverse DNS, yes, a name, prefix, and many more, and we are converting as a lead student tracing, where we are going to have, like, an internal tags with the start time and end time. And now for each link, let's call it, like, each link of those, we're gonna have, like, an client span and a server span. And then, by having that client and server is how we are gonna build that connection. The connection that I'm talking about is like, that one. So, like, in that case, it's a thousand SIG, but that could be, like, a computer or whatever. It's connecting to that IP, let's go to that IP, and so on and so forth, until it reaches Fisco.com in our example.
And then the information that for sure we have, which is the round-trip latency, it's gonna be converted. For the moment, I just put it as a… as an attribute, which is Network Path Hub RTT, that one will… will evolve. It's a temporary, proposal, but for sure, once we have more standardization over that, that will change. But the idea is, like, we cannot put the… we don't know when request start, and when the request finished for each TTL, remember here we have, like, a TTL, like, that one go to that one, that one go to that one, source go to the TTL3 to that one. So, as we don't know, those are start time and time.
we cannot put the start of each trace, sorry, of each span, so what we are doing there is, like, we are adding, at the end of the day, we are adding that attribute that I have it here, which is the… the network path RTT.
**Sven Cowart (ElastiFlow Inc)** 31:32 Hmm.
**Antonio Martinez (Cisco Systems, Inc.)** 31:33 This is kind of the proposal, I don't know if that's kind of aligned with your flow, the student tracing, where you are… I guess you're having flows between different devices or services?
**Sven Cowart (ElastiFlow Inc)** 31:44 Interfaces, yeah, network interfaces.
**Antonio Martinez (Cisco Systems, Inc.)** 31:46 Tracy, okay.
**Sven Cowart (ElastiFlow Inc)** 31:47 So, it works exactly like the flow producers inside of network devices work, where it's just producing flows out of the… about interfaces on the device, and they're, you know, they're like the typical 60-second export window that exists on most devices, and And… but it's doing it on interfaces. Those could be virtual interfaces, anything that you want to instrument, and it's doing it through eBPF. So, like, traditionally, in a Kubernetes environment, you would never get flow records about pod-to-pod communication. Well, you can get that now, with what I've.
**Antonio Martinez (Cisco Systems, Inc.)** 32:21 Darn.
**Sven Cowart (ElastiFlow Inc)** 32:22 And it actually… this is so closely aligned to the things I'm working on, there's definitely going to be overlap, because part of what we do, like, the attributes I put on there as well, under those records, is RTT, and other things.
This is just a different… a slightly different angle, right? It's using the trace routes as a way to produce those.
**Antonio Martinez (Cisco Systems, Inc.)** 32:45 Perth, because here, from our perspective, it's totally… synthetic test, so we are not inside of those devices, or inside of those routers, so we cannot generate the instrumentation of the data. What we have here is just the trace route, and we are converting onto OpenTelemity trace.
the typical view from Thorson Ice, I don't know if you have seen in the past, but it's something around those lines, that you have, like, one agent going to a destination. So that view, we can convert into a distribution tree, and then we can send into to Dynatrace, to Grafana, to 1000… sorry, to Splunk. That's kind of the goal, using a standard, which is up until Indy. So my idea here would be, like.
presenting GiveCon, see if people have feedback or like it, improve it, and then once we have something, like, kind of using my customer and kind of working, creating a couple of GitHub issues to propose those metrics, sorry, those attribute names that I was talking about. There are not that many, actually, there are those two because those, the host name also, there's already that IHAB issue, and then proposing, like, today we're always talking about metrics, is proposing the student tracing, and then I guess we can do it at the same time that we do your blog proposal, so both are going to the same direction.
If they merge.
Yeah. That was kind of my idea here.
Honestly.
**Sven Cowart (ElastiFlow Inc)** 34:07 I think that… I think this is great, and I love it. The… I think maybe the one thing that'll be the hardest is for the specs to… Except a new… trace type value, because right now, it's just… What, it's 5, unknown, client, server, consumer, producer?
**Antonio Martinez (Cisco Systems, Inc.)** 34:30 Yep, and really…
**Sven Cowart (ElastiFlow Inc)** 34:31 What we want is a new one, which is initiator and responder, or something like that, that lines up with.
**Antonio Martinez (Cisco Systems, Inc.)** 34:36 Networking.
**Sven Cowart (ElastiFlow Inc)** 34:37 inventions.
**Antonio Martinez (Cisco Systems, Inc.)** 34:39 I had many conversations with the Splunk OpenTelemity teams about that, because we are sending that to them, and they don't have an easy way to differentiate, okay, this is application trace, and Networking phase, let's call it, right now. But then, if you read the server, sorry, the client and server of the kind of an SPAN, they don't say they have to be an application, they just say that it is a request and response.
So, we… from our perspective, we can evaluate that in a different context, but from our perspective, we are fine keeping those, but the only important thing for us is, like, we are going to have a… in the scope, I don't know how… if you guys, recall that, let me see if I have it around here… Here, in the… I don't see… I don't know what it is now, but there is, like, a scope in a… in a span that is, like, the resource attitude, and the scope, and then the scope, we will… yeah, here it is. OTL scope name. It will be something like Network Path Model.
And then by having that scope is where you know that those client and server are network communication. That's kind of the proposal without not breaking, without making a huge change, or adding a new, because.
**Sven Cowart (ElastiFlow Inc)** 35:58 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 35:59 As you said, we have consumer and receiver, or message queue, and we have client and server, usually for application talking to application, or service talking to services. But at the end of the day, this is… those two IPs are connected, and by… as they are connected, we can also use the server and client. That's at least the way how I see it.
**Sven Cowart (ElastiFlow Inc)** 36:19 Yeah, I think just calling it… it's the same problem that… why we wrote the network guidance document, right? It's that client-server actually means… client-server, not just they're connected, and one… we don't know which side is the client and which is the server, which is the same problem you have here. I think it's the right long-term solve. I also, for the work I did with Mermin, just did client-server, because I… I needed to do something, and I agree with you, actually, in the definitions for that. It's not very… It's pretty open-ended, so it could… it works, and gets the job done for now.
It just feels hacky at the moment.
Yeah, I think we should… we should definitely propose it, and I think if we give two examples here of this is how we take advantage of that trace kind and using trace routes, and this is for, flow records, and we can use the same one, then I think it makes a lot of sense. And I don't think it's too hard, because it just… like, what we care about is who's the initiator and who's the responder.
Right? Like, we base it on INA, BuyFlow's convention on that specific problem that every network telemetry thing has, and… and then hopefully doesn't get too much pushback, because we're not trying to invent something new here. It's pretty standard.
**Antonio Martinez (Cisco Systems, Inc.)** 37:40 Nope.
**Sven Cowart (ElastiFlow Inc)** 37:41 Things that exist.
**Antonio Martinez (Cisco Systems, Inc.)** 37:43 Yeah, we can start that conversation. Once those things are more used out there, we can start convincing them, but I think for the meantime, scope might also solve our problem, I guess.
**Sven Cowart (ElastiFlow Inc)** 37:55 Yeah, that's exactly how we're doing it too, by the way. Like, we identify the different app versus client, network traces based on the scope and the resource.
**Antonio Martinez (Cisco Systems, Inc.)** 38:07 Nice.
**Sven Cowart (ElastiFlow Inc)** 38:08 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 38:09 So yeah, I will put the link here about that, and I think I have to upload, I guess, everyone that is a speaker in QFCON, we have to upload the… the slides, once I have those slides, public, I will share with you guys, so you can also see there.
And… Jace wrote…
**Braydon Kains (Google LLC)** 38:30 Your slides are way further ahead than mine.
**Antonio Martinez (Cisco Systems, Inc.)** 38:33 I have tomorrow to do a rehearsal with my team that way. This weekend was fun.
But yeah, I love, I love it that they are kind of aligned.
I would say.
**Sven Cowart (ElastiFlow Inc)** 38:45 Yeah.
**Braydon Kains (Google LLC)** 38:47 I think your talk ends when mine starts, so I would… I might be able to, like, be there for the first few minutes or something, or probably miss it, so… good luck.
**Antonio Martinez (Cisco Systems, Inc.)** 38:56 from anyone.
**Braydon Kains (Google LLC)** 38:57 If I don't… if I'm not there.
**Antonio Martinez (Cisco Systems, Inc.)** 38:59 Appreciate it.
Yep.
Okay, so yeah, we will, I guess, talk more about that once those things are more standard, or I mean, more subtle.
If you have any docs also about your distribution for flows, feel free to post it somewhere so we can read about it.
**Sven Cowart (ElastiFlow Inc)** 39:32 I do. I'll just link to it here.
I… I try not to share them, because it's not an official hotel project, and I feel bad, and I've been… was pretty spammy in the beginning about getting people to look at this, but I don't think it got enough attention. But there… I just added them there.
**Antonio Martinez (Cisco Systems, Inc.)** 39:59 I mean, if the goal is to move it to OBI, it's perfectly fine.
**Sven Cowart (ElastiFlow Inc)** 40:08 This is actually what got the whole thing started for me, for wanting to start the Networking SIG and Lyudmila… giving me her blessing around, oh yeah, this is valuable.
And you can just see that there's a whole lot here.
**Antonio Martinez (Cisco Systems, Inc.)** 40:25 I think that will be quite useful.
Anything else, guys?
**Sven Cowart (ElastiFlow Inc)** 40:38 So, I sent it in Slack, but just for… There's also that, which is, the docs.
Oh, let me… that was the wrong one.
They're both there. Nice.
Anyways, you can get a sense for… the configuration structures in our SMP coal docs, and kind of what we do.
And we have two. We have the S&P one and the S&P TRAP ones.
Very closely related, but different. Slightly different.
**Antonio Martinez (Cisco Systems, Inc.)** 41:27 So that's the… that's your product, right? For me to understand? Yeah.
Yeah. Okay.
**Sven Cowart (ElastiFlow Inc)** 41:32 So this is a slow one.
**Antonio Martinez (Cisco Systems, Inc.)** 41:34 Is it… is it using OpenTelemetry today?
**Sven Cowart (ElastiFlow Inc)** 41:37 No, no, no. We started, like, 6 years ago, so… we're trying to… Move everything to OpenTelemetry.
It's not really possible.
At this time, but that's why we're here, so…
**Antonio Martinez (Cisco Systems, Inc.)** 41:53 I saw that there was from… He translate, yeah, I think it's that one. I think Kentik, which is another network company out there, they build that heat translate product, and they support OpenTelemetry.
exporter, but I didn't have neither the chance to look into. They also support, like, SNMP receiver and exporting using, but… I mean, looking at the start, they don't have that many, so I didn't… too much attention, but yeah, there was a customer from Cisco that they were using that.
Shit.
**Stephen Amstutz** 42:25 I've done quite a lot of work with Cantip in the past.
**Antonio Martinez (Cisco Systems, Inc.)** 42:29 Okay. Do you know if people are using that keytranslate nowadays, or are you aware of?
**Stephen Amstutz** 42:35 I am aware of it, yeah. They added, they added SNMP about… 2 years ago, 18 months, 2 years ago, something like that. They were predominantly just, handling flows prior to that.
But yeah, they added, quite a lot of stuff in the SNMP space.
**Sven Cowart (ElastiFlow Inc)** 42:56 They were just acquired by Infoblox.
**Stephen Amstutz** 42:58 Yes. Number one.
**Sven Cowart (ElastiFlow Inc)** 42:59 competitor, I'm very familiar with everything they do.
**Antonio Martinez (Cisco Systems, Inc.)** 43:10 Okay. Yeah, I discovered that, honestly, because the maintainer of that was also talking on the OpenTelemetry receiver, one of the GitHub issues.
I see. He was mentioning, like, oh, you guys, you don't have to build that, we already have it in Kei Translate. That was so fun. That was so fun, as it's… but yeah, you know.
We need to read a little bit what they are doing here.
Okay.
**Sven Cowart (ElastiFlow Inc)** 43:49 Curious… I will look into that. I am curious what that actually means, because… Kintec is… Largely proprietary.
Business, where it just sends to their backend.
And…
**Antonio Martinez (Cisco Systems, Inc.)** 44:04 accept, right?
**Sven Cowart (ElastiFlow Inc)** 44:06 Sorry?
**Antonio Martinez (Cisco Systems, Inc.)** 44:07 Makes sense. Like, why are they using OpenTelemet if they don't support OpenTelemetry neither on their… On the product, yeah.
**Sven Cowart (ElastiFlow Inc)** 44:15 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 44:30 And then… I don't think there are new tickets or anything new here, I… I saw that ticket.
I saw that ticket, but… That is… that you make a comment, or you created this thing. I don't know if we should… Do something here, or…
**Sven Cowart (ElastiFlow Inc)** 44:51 Oh yeah, this was a follow- not yet. I'm not ready to go there yet.
It's fine how it is right now, and when we get there, we'll address it. But it was, Leftover from how… the… the… how… the… the guidance on picking the appropriate network addresses. I think it was Mark actually who brought this up, that… What happens when you have multiplexing situations, and… to source and destination, and all these things. And I think there's actually some easy resolutions, but… I think we need to get a little bit deeper into the, The… the network peers conversation to really address that.
**Antonio Martinez (Cisco Systems, Inc.)** 45:40 Oh, sorry, Copeland?
Good evening, so see you next Monday, everything's alright.
**Sven Cowart (ElastiFlow Inc)** 45:48 Awesome. Thank you. Take care, everyone.
**Antonio Martinez (Cisco Systems, Inc.)** 45:50 Go for the one, but…
