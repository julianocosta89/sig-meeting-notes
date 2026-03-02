SIG: Kubernetes Operator SIG
Date: 2025-11-06
Duration: 35 minutes
Zoom Recording URL: https://zoom.us/rec/share/jdUL6ptD8cXY7W0LcYUNXxG-D4B5_L3KjBvOYxbDmsNNTB9icLuxZabdJPyyLRse.Uqghp6_7rtxU5Rec
============================================================

## Zoom Recording Transcript

**Benedikt Bongartz** 03:40 Hello?
**Mikołaj Świątek** 03:44 Oh, what's up?
Things is going okay.
Are you… are you, like… are you sleeping… I'm not gonna ask, well, are you sleeping… Alright…
**Benedikt Bongartz** 04:02 It depends. There are days where I do, and there are days where it could be better.
**Mikołaj Świątek** 04:13 Well, you don't look too bad. You don't look like you're gonna fall over.
**Benedikt Bongartz** 04:19 Yeah.
**Mikołaj Świątek** 04:20 in my mouth.
**Benedikt Bongartz** 04:21 Eye rings, I think they are noticeable, depending on the light.
**Mikołaj Świątek** 04:28 Pavel, Pavel was… Pavel didn't like the discussion and left immediately.
**Benedikt Bongartz** 04:34 That's, yeah, we spoke about child processes.
**PL Pavol Loffay** 04:41 Grace.
**Mikołaj Świątek** 04:42 Yeah, it's up.
**Benedikt Bongartz** 04:49 I hope in a few minutes we can merge stuff again.
**Mikołaj Świątek** 04:55 You wanna know a funny… you wanna know… wanna know a funny story?
So…
So, like, Claude, the AI company, sent me an email saying, hey, we did this Claude on web, where you can just go in here on the site and link it to your GitHub repo, and then it will do, you know, agentic coding and so on.
So I was like, and we're giving you however many hundred dollars of credit to try this out. I'm like, okay, oh yeah, I'm gonna link it to my personal auto operator repository, and then I pointed it to our end-to-end test directory and said.
Try to find ways to simplify and modularize this.
And it's been a day.
Still mulling over it.
**Benedikt Bongartz** 05:47 I mean.
**Mikołaj Świątek** 05:47 No, that's kind of what the problem is, right? It's not that many, it's not that many lines, I don't think. Maybe, maybe it's, like, it doesn't like our bash script. Maybe that's the problem here.
**PL Pavol Loffay** 05:58 I, I…
**Benedikt Bongartz** 05:59 You observe it.
**PL Pavol Loffay** 06:01 We have some CDEs, or some recommendations for… to improve the end-to-end tests, and I…
Gave it the inputs that we got from the security scanner, and it completely broke everything.
It didn't work at all.
**Benedikt Bongartz** 06:20 I think.
**Mikołaj Świątek** 06:20 I also…
**Benedikt Bongartz** 06:21 Hello, autonomous stuff. I played with SVE Agent to autonomously resolve some low-effort issues.
And I guess this video summarizes basically how this went.
**Mikołaj Świątek** 06:40 I was hoping, I was hoping it would get some stuff. At the very least, I have hope that it can do, like, some refactoring on its own, if you already have tests, because it can run the tests, so maybe, maybe it can figure it out. I had hope, but… And to be fair, to be fair, I have a PR app, which is, like, switching the ENV test to V1 Beta 1. That is, like, about half written by an AI.
Roughly.
But only half, and that PR is mostly just text replays, honestly, and so it's a little bit concerning that it couldn't figure it out on its own.
**Benedikt Bongartz** 07:18 I think where it's awesome is sometimes this… when you have to rename just a bunch of stuff, so this was with the.
environment verb is when I graduated
go memory stuff to Better.
**Mikołaj Świątek** 07:32 Hmm?
**Benedikt Bongartz** 07:33 you just… I just made it for one test, and then I figured out, oh, there are more unit tests which break, so I went to Cloud Code and said.
Go ahead.
**Mikołaj Świątek** 07:42 I, I agree, I agree. That is very good. Like, I also had a PR earlier, which was, like.
Moving cluster role creation to a step template in the end-to-end test.
And that was… that I also told Claude to do, and it eventually did it. It took way longer than I would have expected to do that, but it did work, so okay. So this is, like, a nice boost.
**Benedikt Bongartz** 08:10 two pieces I needed to revert.
For some reason, it did always touch other environment variables in other tests, and it also added the test for this specific environment variable to tests which are meant to test something else.
**Mikołaj Świątek** 08:24 Like…
**Benedikt Bongartz** 08:25 tests and variable… ABC?
And then underneath it said test n variable XYZ, and it was, don't do it in ABC, because this is specifically for some specific environment variable.
Okay, I will do this, and it did it again.
**Mikołaj Świątek** 08:48 Alright, it doesn't look like we're gonna have anyone else, which is strange, because I expected the…
I expected us to discuss the cluster observability.
CR.
**Benedikt Bongartz** 09:00 testing.
**Mikołaj Świątek** 09:01 Today.
Maybe next time.
Do you have opinions about this? I wrote some comments on it.
my major… I would say my… part of the comments were like, you know, please don't… please, you know, make it not appear in our default bundle for now, and so on.
**Benedikt Bongartz** 09:24 Yeah, I think that's implementation stuff, right? So,
how it's merged and implemented and whatever. Similar, like, I had also one comment, which was regarding
You could potentially have a race condition, because the instrumentation CR is always named the same.
But I was more curious about the configuration, because we propose this sickness, Like, metrics, logs, and traces.
But there is no actually meaning behind it, so do I get system metrics? Will I get Kubernetes metrics? Will I get…
Metrics ingested from a user.
And there is no, actually, way to…
Block one or the other, or whatever.
**Mikołaj Świątek** 10:11 I think that's intentional. From what Antoine has said many, like, multiple times in these meetings, it's intentional, they don't want it configurable to start with, if, like… and they plan to say something like.
If you want this to be configurable, go install AutoCubeStack and do whatever you want. We are, like, not gonna expose every possible knob. I am actually also against exposing most of the OTLP exporter knobs.
In there, too. For, like, reasons which are roughly…
Do we want to add every single option that OTLP Exporter adds in here? Do we want to be subject to breaking changes in the OTLP Exporter?
Today, my…
**PL Pavol Loffay** 10:58 Well, TLP exporter is one of the stable components, so I would say…
That could be one of the… Good candidates to actually… declare in the CR.
But I as well… I think as well we should… Not expose anything starting?
But then, as we collect feedback, we should have a design that will allow us to…
To make the change, if we have to do it.
**Mikołaj Świątek** 11:28 I am… I am in favor of maybe exposing some values in that.
But, like, I am… I would be fine with doing something similar to what's in the instrumentation CRD, which is, like, you have endpoint and, like, maybe, like, one other value or two, something like that.
I don't want to reproduce… if we want to reproduce the whole configuration structure of a TLP exporter, I think we should just import it, and… and do… and that's it.
**Benedikt Bongartz** 11:58 then endpoint and TLS, and maybe some of… Settings.
**Mikołaj Świątek** 12:07 And, and then, and then, like, embed a, you know, just a map.
From string to whatever in there, and…
**PL Pavol Loffay** 12:16 Yeah, I bet.
**Mikołaj Świątek** 12:16 People can put in whatever they want to.
**PL Pavol Loffay** 12:19 Like, I think the question is, like, what is the use case for this OTLP exporter? Is it to export data in cluster to another collector, or is it to export to vendor, right, to backend? And then…
**Mikołaj Świątek** 12:33 Probably vendor?
**PL Pavol Loffay** 12:34 Yeah, I think so, as well. And then we should kind of understand, like, what are…
the usual configuration, like, what is needed? It's probably a header, right? Like, some token, usually it's not a TLS certificate, it might be.
But I think we can then… we can then reason about, like, what should be there from the get-go.
**Mikołaj Świątek** 12:58 Like, the thing is also…
**Benedikt Bongartz** 12:59 But for multi-cluster setups… So when I have my spoke cluster, so…
Two clusters, let's say my observability cluster and a few others.
I think that's a really nice thing, to just send it out, configure it to send the data back home to my observability cluster.
And don't really care much.
So that's why I went with the TLS things. You would like to maybe send it to something insecure inside of your cluster, you would like to enable… yeah.
**Mikołaj Świątek** 13:30 I think this… the whole idea of the CID is that it's supposed to be, like, maximally turnkey.
Like, it's supposed to be maximally, I don't care, I, you know, I have no opinions, I don't know what I should be collecting from Kubernetes, because I am not an expert in Kubernetes observability, and so on, so just give me something that will fetch me, like, a reasonable set.
of data, and it will, like, light up. Whatever vendor, whatever vendor I'm using, it will light up their dashboards that they have prepared for me, and we're good. Like, the use case where it's like, oh, we exposed this to the, like, internal private network, so other clusters can send… if you want to do stuff like that, you can figure it out on your own, in my opinion.
**Benedikt Bongartz** 14:14 No, it was more like, if I have, let's say, two, three clusters, and I have one observability cluster, I can just, instead of pointing it to a vendor, I can point it to a private cluster.
**Mikołaj Świątek** 14:25 Yeah, I know. I just think, like, this is definitely supposed to be to a vendor. The things that I'm worried about here, mostly, are things like…
What should the queue settings be like?
Right? Right?
**Benedikt Bongartz** 14:46 Technically, if this is just a starting point, I would argue that if… You deploy this?
And… then you…
notice something doesn't work, because my queue runs out of size or whatever, you just recreate the custom resource, the open times you collect a resource and get more into it.
So if the defaults don't work.
It's the same thing here, if I don't want to expose specific, let's say, my logs or whatever.
Yeah, then I need to… or do some other filtering, then I need to do this on my own.
Or send it… Yeah, no. I think probably you just do it on your own.
**Mikołaj Świątek** 15:31 Yeah, that's kind of my feeling. I definitely don't want to have every single configuration option that OTL peak partner has, like…
in the CRD.
That's just, like, asking for trouble. That's just asking for issues about, like, us not having, like, some option that OTXporter added and the user really needs, right?
I've been…
**Benedikt Bongartz** 15:55 For me, it's more the other end. It's like the, The signal part, where I'm…
I'm sure if this is…
a good idea. So, I would then either go and just enable it by default.
And just remove the signal part at all.
Completely, because… Having there just traces or metrics, from my perspective, is somehow a bit… wake…
So you need to go to documentation and understand what it actually does.
**Mikołaj Świątek** 16:36 I mean, kind of, yeah.
**Benedikt Bongartz** 16:39 then I would say, if this thing is there to accept metrics, and get host metrics, and do everything in one.
run, then I would just… remove it from the CRN. If someone says he would like to
Yeah, let's say stop… Accepting logs that a user can report, or from auto-instrumentation, disable this one.
We can add something to disable pieces, and…
**Mikołaj Świątek** 17:12 I am fine with it as it is right now. My expectation is that it's gonna evolve once any, like, real user gets their hands on it and actually tries it. And that's kind of the explicit goal here, even though, like.
It's not V1, it's not alpha in the same sense that, like, target allocator CRD is alpha. It should probably be beta at this point, because, like, people is just…
**Benedikt Bongartz** 17:33 I didn't get…
**Mikołaj Świątek** 17:34 and whatever, yeah?
**Benedikt Bongartz** 17:35 look into this. Does it deploy the target allocator, too, to script metrics, or…
**Mikołaj Świątek** 17:42 Pretty sure, pretty sure it does, like, a single…
It's like a… it's like a very alternative approach.
Basically, all the… all the data is auto-native. You don't do, like, you don't use, I'm pretty sure you don't use QubeState metrics, instead you use, like, the receiver that does the keep-state metrics.
**Benedikt Bongartz** 18:02 Yeah.
**Mikołaj Świątek** 18:02 Staff, and then so on.
And the cluster stats, and so on.
So you're not actually hitting all the Prometheus endpoints inside the cluster to do that.
Your fix to the end-to-end test still fails.
**Benedikt Bongartz** 18:25 Yeah, I've seen it. It finished, and I… Don't know why.
**Mikołaj Świątek** 18:32 Where does that test even come from? Like, why is it here?
I didn't notice when we added that.
**Benedikt Bongartz** 18:38 I added this today.
**Mikołaj Świątek** 18:42 Okay.
**Benedikt Bongartz** 18:43 Worked on my machine. No, sweet.
I was also surprised when it just started fading on Kubernetes 1.25.
And then I wrote this issue, and then I was thinking, I was.
it's a sidecar, so I expect… the only difference between 125 and 133 is actually that we use native sidecar on 133.
So, the collector is up and running, And it seems…
It's an issue if it's not.
Up and running.
And the process starts before, because… but, yeah.
Technically, it shouldn't matter, from my understanding.
But yeah, I will… Debug this locally after this call, I guess.
**Mikołaj Świątek** 19:39 Alright. Do we have… do we have anything else to discuss?
**PL Pavol Loffay** 19:49 Not really. I started working on MCP, on the hotel MCP.
I'd be curious to get your feedback, Nikolai, what do you think?
Or if you heard anything about…
Or if you have any opinions about LTL and CDs?
**Mikołaj Świątek** 20:06 Hmm…
I am only vaguely aware that this is something that exists. As in, auto MCP for… what's the scope when you say auto MCP?
**PL Pavol Loffay** 20:20 That's a great question.
At the moment, it's about the collector configurations.
But its next step would be to…
Connect it to the collector and understand the data that is going through.
So that a user can ask questions about
What the collector is processing, receiving, you know, what are the attributes.
What are the values of attributes, if there are hardcadinary attributes?
I think this can be very helpful to…
write custom filtering, PII filtering rules, for instance.
Or identify instrumentation issues.
Maybe as well do, like, data volume attribution.
So that you can kind of understand which workload is. Maybe, as well, miss,
instrumented, and it's emitting, like, too many locks and stuff like that. Or just for understanding, you know, where…
-Oh.
For which workload you are paying most for observability.
But going back to the collector configuration, what I did is…
I use the collector builder to get all the components.
And then… Extract the factory, so next… and get… from the factory, get the config.
and then compile JSON schema.
For each collector component config.
So the JSON schema has the… the field name.
description, like, a comment from the Go source codes and the type.
And this is exposed through MCP, so you can, like, ask, like, give me the schema for, like, file log receiver, and it will give you the…
the JSON schema.
And then there is another MCP tool that allows you to validate the config against a schema.
So you are sure that the…
the config is valid, that the airline creates.
That's one part, and second part is, this is all versioned with Collector.
So you can ask a question like.
compare 149 with 140, and show me all the added components, and what config options changed across components.
Or you can ask, like, what are the deprecated fields, and it will give you, like.
Tills per component, which are… which were deprecated in the version.
Or you can ask in a cluster, like.
am I running any deprecated features from OpenTronometry Collector? And based on that, it will, like, parse your config and ask the deprecated fields and compare.
**Mikołaj Świątek** 23:40 Okay.
**PL Pavol Loffay** 23:42 Share your link.
There's a blog post, and I would like to start a working group.
Because there's, like, multiple of these servers, they…
often offer similar functionality, mostly around collector configuration, but then as well about the data profiling and understanding, you know, what data is going through collector. And I think if you want to properly
support this in OpenTelemetry, we need to have, like, a collector component that, you know, caches data and offers some API to
To query it. That will be one part, and second part will be actually an MCP that is embedded in the collector as well.
Because then, I think that's kind of the…
The best way to actually implement the…
the API for, like, looking at the collector data to directly have the MCP on the collector.
But yeah, I think there is a lot of things we can do.
**Mikołaj Świątek** 25:05 Like, the… have a look at the data kind of functionality is very useful even without the MCP, it's just that it's difficult to actually properly define what that's supposed to do, unfortunately.
In my opinion, anyway, it's.
**PL Pavol Loffay** 25:24 Like, what would be the query language, and what functionality?
**Mikołaj Świątek** 25:27 No, no, I mean, like, what do you actually keep, is the question.
**PL Pavol Loffay** 25:32 Yeah, well, it kind of relays to the API, right?
**Mikołaj Świątek** 25:38 I don't… I actually don't know. Like, it would be very useful to, like, know roughly what kind of attributes you have in your data, but you can have a lot of data passing for a collector of all sorts of, like, different, you know, shapes, and, which ones do you keep?
how do you tell whether, if you see a record, how do you… do you have to do some kind of sampling? If you see a record, how do you know that this record is, like, similar to some other record versus not, and whether you should consider it, like… like, you have to do some kind of categorization internally, right?
you have to be able to know, like, for example, these are… these are system metrics, so I need to… so I only need to keep one of these to show, right? But when you're ingesting logs, you can be ingesting logs from, like, many different sources, and you potentially need
one of each, to have this kind of view. And how do you tell which one is which? Maybe you just go by, like…
Maybe you just go by instrumentation scope, or something?
Maybe that's, like, sufficient for 90% of use cases?
**PL Pavol Loffay** 26:55 Yeah, my… I would start with, like, native implementation. I wanted to just cache the attributes and values, and maybe count the occurrence.
And if we… if I could do, like, regex search on it, that'd be as well super helpful.
But… That would not solve the use case of
Of, like, understanding which attributes come in the same record.
Right? Because, like, sometimes there is… you need… You need this information.
Yeah, I would look at this from, like, use case perspective, like, we have these use cases, and then let's try to…
keep… The minimal amount of data to satisfy this.
there is one MCP, someone wrote, they spin up, like.
Open search, and ingest all the data there.
And then you can, like… use.
like, query open search to figure out what is there, but…
**Mikołaj Świątek** 28:16 That's true.
**PL Pavol Loffay** 28:17 I'd like to do.
**Mikołaj Świątek** 28:17 Spin up… if you spin up a day… a full analytics database, then of course you can… you can query…
You can do anything. At that point, you don't even need to connect to the collector, right? You can… I go to… at Elastic, I keep going to these all kinds, and they keep saying how great it is when you connect an AI to Elasticsearch, and how much, you know, how well it allows it to answer questions, and so on.
So… so I'm not surprised you can do that.
But, you know, that's… that's a pretty heavy thing to add, just to be able to ask… ask about your collector's date.
Alright, I, I, I, I, I'm, I'm not, I'm not sure, like, this is, I, I think this is a pretty difficult…
problem. Like, the question of what information to surface and how is difficult. Like, it's not the LLM part that's difficult, right?
It's, it's the…
API and data stream, and how you're gonna… and how you're gonna implement it, because if you wanna implement it, you basically…
You're basically forced to add a processor to each pipeline, but if you add a processor to each pipeline, you want the user to do it, and they might not, and so on, right?
Because the collector is really just an, like, an encyclic graph.
And, like, having some central place where you're collecting metadata is…
Problematic, in and out of itself, right?
**PL Pavol Loffay** 30:03 Yeah, I think it makes kind of sense to spin up, like, additional collector with MCP that will cache the data.
Have it, like, off the hook path.
**Mikołaj Świątek** 30:12 Something like that might be… like, that's not gonna be… that's not gonna be light still, but it's gonna be lighter than, like, you know…
open search, click house, you know, put up a database specifically so you can do it. Like, a collector is much lighter than a full database.
So, that sounds more reasonable to me, at least.
**Benedikt Bongartz** 30:40 I think it highly depends on what you would want to know.
So if you would like to have analytics over your data, you need access to your data entirely, so which means…
It needs to be stored somewhere.
**PL Pavol Loffay** 31:06 Hey folks, I will drop if there's nothing to…
**Mikołaj Świątek** 31:10 Okay.
Have a… have a nice, have a nice evening.
Both of you.
See you.
**PL Pavol Loffay** 31:17 Goodbye.
