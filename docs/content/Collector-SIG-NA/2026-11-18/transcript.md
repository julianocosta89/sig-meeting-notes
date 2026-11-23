SIG: Collector SIG (NA)
Date: 2026-11-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Ervin Wallin** 03:07 Hello?
**Paulo Janotti (Splunk Inc.)** 03:13 And,
**Antoine Toulme (Splunk Inc.)** 06:49 Hello?
**Andrzej Stencel (Elasticsearch B.V.)** 06:54 Hello.
**Evan Bradley** 06:55 Hello, hello.
**Antoine Toulme (Splunk Inc.)** 06:59 Ready to go?
**Evan Bradley** 07:02 Let's do it.
**Antoine Toulme (Splunk Inc.)** 07:05 Dude?
Alright, so we have to go through high priority issues for stability phase one. It's still on the board. Let's open that board. You want me to share my screen?
Okay.
I'll show my screen.
See if that still works.
Okay.
Alright, so, this is what we have right now, so there's a lot of stuff done.
Things are in progress right now.
So, Promise receiver into stables in progress, about 50%.
Semantic convention transitions… Protting file researches table… Is there any report here? Anything we should discuss?
**Pablo Baeyens (Datadog)** 08:05 I think maybe for the resource detection processor, there's quite a few PRs from Pablo and David, But I don't think they're listed here. But… Yeah, in general, if you're interested in the research detection processor, it would be… or to find low receiver, honestly, it would be good to have more code owners there.
**Antoine Toulme (Splunk Inc.)** 08:25 Yeah, I do see there's two issues that are marked in progress, but there's no assignee?
It's just, maybe just missing from the… Okay.
Alright, so who is… okay, so we need more code runners on file log to help.
There's Andrzej and Pablo.
Yes.
Braydon.
That's do it. Okay.
**Andrzej Stencel (Elasticsearch B.V.)** 08:55 That would be cool.
**Antoine Toulme (Splunk Inc.)** 08:58 But overall, like… Looking good, I do see… Some follow… okay, it's not the same thing. Alright.
Alright, is there anything in here we should discuss?
There's two of those.
Should we discuss those?
**Pablo Baeyens (Datadog)** 09:27 I think that's most… the Prometheus one is mostly on the… Prometheus interoperability to SIG, or the specification SIG?
**Antoine Toulme (Splunk Inc.)** 09:35 Okay.
So we have… we have 10 minutes, let's… let's take this one, right? Let's do it.
Transition to stable SIMConv.
These crystals here.
Maybe not.
Okay, so it may go straight to the end.
As of a year ago, we have a comment from Braydon.
Okay, something about feature gates… There's been some changes here.
Alright, is there a discussion still needed for this, or should we just start with, assigning it to someone?
So they start to work on that.
**Tyler Helmuth** 10:26 This is in progress. Christos is already working on this. You could assign him. Yes.
**Antoine Toulme (Splunk Inc.)** 10:32 Okay, that's what I wanted to know.
**Tyler Helmuth** 10:33 Yeah, we have… we're working through the gates. It's… this component is working its way to 1.0, and this is part of the work.
**Antoine Toulme (Splunk Inc.)** 10:43 Mmm… Okay, can I remove that, discussion you did flag, then?
Just wanna make sure we… I'm gonna say that's a yes.
**Tyler Helmuth** 11:04 I think the answer is yes. I'm, like, not.
**Pablo Baeyens (Datadog)** 11:06 Yeah, 100%.
**Tyler Helmuth** 11:06 Sure, we have it.
The feature flag policy in this repository.
that we have already documented in core with the RFC is the solution that this component is going to use.
**Antoine Toulme (Splunk Inc.)** 11:19 I'm also going to move it in progress for your recommendation, and then… We're good?
Okay?
Alright, let's go back. So, we have just this one discussion needed for Prometheus.
Number of stuff to pick up, if people feel like it, looks like.
And… Awesome.
Anything else we want to talk?
How about the towards V1.
**Tyler Helmuth** 11:49 Yeah, I need to… this week, I'm going to make the official, like, promote… 2 stability issue for the transform processor.
I have been just forgetting to do it, and I think that's part of the official process, so that'll be, created this week.
**Antoine Toulme (Splunk Inc.)** 12:09 Cool.
Who's possessive filter code owner? Do we know?
**Tyler Helmuth** 12:15 Me. We talked about that at KubeCon. The filter processor, we have a list of items that we need to work through that are already opened on the… stability tracking issue. As soon as I'm finished with Transform Processor, I'll start on Filter Processor. I expect that I'll… I think the Transform Processor could be marked stable in December.
Like, maybe even in the next release, honestly.
And then the filter processor, we've identified some work with the public config, and the public API that we want to clean up, and then it'll also be ready for tagging.
**Antoine Toulme (Splunk Inc.)** 12:54 Okay.
**Tyler Helmuth** 12:55 For our V1 effort for KubeCon EU, I think, in my mind, when I look at the component list, the one that is the most at risk is the file log receiver.
**Antoine Toulme (Splunk Inc.)** 13:06 That makes sense.
**Tyler Helmuth** 13:07 I don't know who… which maintainer or code owner is driving… will be driving the file log receiver to 1.0. I think that's, I think that's a risk for our efforts, and we need to find someone to pick up that work.
What, Braydon.
**Andrzej Stencel (Elasticsearch B.V.)** 13:23 Yeah.
**Braydon Kains (Google LLC)** 13:24 It'll be me and Andrze.
**Tyler Helmuth** 13:25 Okay. Yay, nevermind, not at risk anymore.
**Braydon Kains (Google LLC)** 13:28 Yeah, we've been working on it. We haven't, like, specifically said anything related to stability, but I've been working on some final things I want to fix before 1.0, and going through it, so we are working on it, we just haven't done anything, like, on… directly on these issues, so we can start to move some discussion there, probably.
**Antoine Toulme (Splunk Inc.)** 13:47 Cool.
Great, there's… I think, underlying the file receivers is also this little one, because… Scrum's gonna be all difficult.
Which way do we lean on this, me, other than that?
So, Stence is a donation, and then, it has a lot of API, so… Yeah, and Dave, what's your take?
**Andrzej Stencel (Elasticsearch B.V.)** 14:11 Well, it's being used with the file receiver a lot, so I think we should aim to… Stabilized as well.
**Antoine Toulme (Splunk Inc.)** 14:20 Okay. I'm… I'm… I agree with that.
we had a lengthy discussion, Andrzej, about, like, maybe how this could eventually become unified with OTTL, because… Stence operators should not be, like, their own thing.
But… Is that something we would do maybe later in 2.0?
**Andrzej Stencel (Elasticsearch B.V.)** 14:42 Yeah, for sure. My view of the stabilization is just to stabilize whatever we have now, right?
**Antoine Toulme (Splunk Inc.)** 14:48 Yeah, I agree with that. Cool, okay.
**Braydon Kains (Google LLC)** 14:50 there's a lot of usage already, and I… well, I think, theoretically, we can cover everything with OTTL, I'm not 100% sure. And so, like, unless I was 100% sure, I'd be more comfortable just stabilizing the oper… specifically the parser operators. Maybe not all.
**Tyler Helmuth** 15:07 Yeah, there's…
**Braydon Kains (Google LLC)** 15:07 foot operators, because.
**Tyler Helmuth** 15:08 Weird.
**Braydon Kains (Google LLC)** 15:09 There were lots of different stuff.
**Tyler Helmuth** 15:11 We should definitely not… O2TL is not a replacement for the file log.
Receiver. Prolog receiver. Use a stanza, that's okay.
we should just 1.0 stanza as part of this, because we're, right, we're, like, we're 1.0-ing, like, what we already have, right? To switch to… to OTTL and the file log receiver, like, that's not a 1.0 effort, that's a massive effort.
**Evan Bradley** 15:36 Just a side comment.
Tyler and I talked with Dan Jaglowski about this, like, a million years ago, and, Stanza has kind of its own pipeline implementation that might make it hard to put something like OatsTL in there.
I'll let somebody else do the thorough analysis on that, but that was kind of the conclu- er… that was the conclusion that we came to a couple years ago.
**Braydon Kains (Google LLC)** 15:58 Yeah, I don't think we can move, like… I don't think we can move OTTL into stanza, it'd be more like… the way I would see it is, like, can OTTL do all the same stuff and thus not need the Stanza operators? But putting… like, while logs are in the file log receiver.
they are in Stanza's internal format, and so OTTL, which is so tied to, like, PData context, like, it won't apply in any way, so yeah, there's… there's probably no way to do that easily.
**Andrzej Stencel (Elasticsearch B.V.)** 16:30 Yeah, my idealistic view on this would be for the V2, or whatever that would be, for Stanza to just operate on P data, but yeah.
**Braydon Kains (Google LLC)** 16:41 It would be…
**Andrzej Stencel (Elasticsearch B.V.)** 16:41 to be able to do one now.
**Braydon Kains (Google LLC)** 16:43 for performance, we would save a lot if we could get rid of stanza entry as a data structure, because if we just read directly into P data.
It would be more performant, but…
**Antoine Toulme (Splunk Inc.)** 16:54 Yeah, we have to look into that, I guess.
**Tyler Helmuth** 16:56 The biggest thing will be the fact that Stanza does all of the flattening automatically, which is, like, kind of a foot gun in OTTL, where you… where you don't get, like, your own little space to work in if you mess with resources or scope attributes and stuff.
But again, all of… all 1.0 stuff. I think for 1.0, there's no way to… there's no way to tag the… file log receiver 1.0 unless we tag Stanza 1.0. Just like we couldn't tag the transform processor 1.0 without tagging OTTL 1.0.
**Braydon Kains (Google LLC)** 17:28 Okay, makes sense.
**Antoine Toulme (Splunk Inc.)** 17:31 Cool, alright, let's go back.
I think we're at the 15 minutes mark.
Jade, would you like to take us to the RFC announcement?
**Jade Guiton** 17:40 Yeah.
So this is, relatively… Short announcement… For… Let me see… Yes.
So this is an RFC in the core Collector.
The basic… Goal of this is that… Once we have… saw the core and OTLP distros marked as stable.
We want to… Make it very clear to end users.
When they are opting into something unstable.
And so, to kind of, enforce this communication, we would make unstable components and unstable feature gates opt-in, so by default, they would be disabled.
This is an RFC which, proposes a technical and, you know, policy changes to do that.
The current version of the RFC proposes a concept of a release channel.
that the… the collector would start in, and that would determine Which components you can use, depending on their stability.
And whether or not, beta feature gates are enabled by default or not.
So, yeah, the link is in the… the, beating notes. So if you think you have an opinion about this, Please take a look.
And I will announce this in the Collector Dev Channel after the meeting as well.
Thank you.
The LFX person would…
**Antoine Toulme (Splunk Inc.)** 19:52 Yeah, go. Okay, next is Emilia.
Sorry.
**Emilia Ferreyra (New Relic, Inc.)** 19:57 Hi.
Hi y'all, I'm Amilia from New Relic.
A couple of Collector SIGs ago, I presented a proof of concept for a CLI that could dynamically validate a processor config by showing the diff of a payload passed through it.
All without having to run a collector, get network connection, or be confined to a browser. And from what I could gauge then, the reception was positive, and there was some discussion about how to integrate this idea into the Collector.
I did some feasibility checks for each of the unproposed options, but my favorite was to add a dynamic run validation subcommand next to the already existing dry run subcommand.
Validate.
If you want to know more about the alternatives I explored, I summarized them in their respective feasibility checks under the issue I created for my proof of concept.
I'll add that to the chat. But since the subcommand solution would need to be placed in core, I created a new, more specific issue over there. I'll also… Include that in the chat.
I've created a new proof of concept to demonstrate how the solution would look. Some main differences between my new and old POCs are that I switched the run subcommand from my old POC, also known as modelDuck, to diff, since run is an overloaded term, that could cause confusion, and diff more accurately describes what the dynamic run actually does.
Model duck's test subcommand, or essentially what was the run subcommand, but instead compares actual output to an expected output, instead of before and after, that was excluded from scope.
Model Duck manually registered and built each processor covered. My new POC, by virtue of it being within core, works with any processor the host Collector build includes, except for now, timer-based processors and processors that require extensions.
However, this means that it was not terribly more complicated to introduce the ability to change several processors for a given dynamic run, or rather, with the new POC, you can now see what multiple processors' configs run one after another does to a given payload.
And finally, I ported over my semantic diff package, and essentially… ported it over essentially untouched, but my new POC uses a Collector's real config provider to take in configs, and it uses the Collector's existing static validate functionality. Okay, I can show you guys, an example of how it works if I share my screen.
Let's see… Alright, You need to use the OCB to build a collector with a builder config that includes all the processors you want to test.
Then you can use the resulting distro to run the diff subcommand as follows. Just like before, You pass in a config to run.
A payload to run the config against, and a comma-separated list of processors you would like to run, but this time it's just, just one, the transform processor. The output is a semantic difference between the payload before and after running against the commit and config. Deleting or adding a bit of the telemetry doesn't cause changes all along the rest of the JSON.
Due to moving the following data up or down a few lines. Instead, all the changes are made in place. And as you can see here, I did the equivalent command in my old POC model doc, and it produces the exact same output.
Huh?
There you go. Anyway, I wanted to present this here to see if this iteration of my project integrates better into the OTEL Collector codebase than before, and if this is still a feature y'all are interested in. If that's the case, I would love to have some feedback here or in the discussion under my posted issue in core, please let me know. Any questions?
**Kells Kearney** 24:55 So, I… just to make sure I understand, I think this is a great addition for something like a CICD pipeline to kind of just validate that we're getting, like, the output from something. So, if I have, like, syslog data, for instance, I contain that from a file.
I push this through this transformation thing, and at the end of it, I would get at least that output from it.
How would I kind of get some sort of, like, gauge?
of, like, how successful that transformation was against that, because I… what I heard you say was that you… the… the actual, kind of, like, end up validated Component of, like, what you were expecting at the end of it is not a part of this?
**Emilia Ferreyra (New Relic, Inc.)** 25:39 Okay, so… I came onto this issue because, we have a static validation, or, like.
**Kells Kearney** 25:48 and dry.
**Emilia Ferreyra (New Relic, Inc.)** 25:48 run, which just checks, the config for, like, semantic correctness, but you don't exactly know what it actually does to actual data. Right.
I used, auto.run the auto playground a lot to… as a way to get around that, you can feed in a config, and you can feed in a payload, and then it'll show you what, the config did to the payload, what the differences were. And… This diff… Command will do pretty much that, but… in a CLI format, so you don't need to run a whole collector to do it, you don't need a browser, you don't need network connection. So the feedback loop is much quicker, it can be done in CI, like, workflows, but, well, this wouldn't, but I had a… in my old proof of concept, I had another one that would, instead of comparing the before and after, you would then compare the real output with the expected output. I definitely feel like that's a valuable thing so that we can better integrate into workflows, but… As of now, like, I just, like, cut it for scope, but I would love to add that later.
But now, it is essentially just, like, a CLI version of what Autel.run does, and potentially has a wider, use in most processors instead of just the auto-related processors.
All within the CLI format, yeah.
**Kells Kearney** 27:47 Okay, well, I do love what you've done here so far. And that next step that you're talking about, about producing it, I see… I very much see the value in that, so I'd love to see that next step, too.
**Emilia Ferreyra (New Relic, Inc.)** 28:03 Yeah, great, thank you.
**Kells Kearney** 28:04 Because the… the… one of the other issues that I have is kind of validation and verification of the traffic as it comes in.
So, I don't know how to do this, or how to kind of think about it, but I'm looking to kind of get some sort of, has the user actually switched, for instance, the firewall product from version X to X plus 1?
Which has changed the output of that, and then how much of a change has that… has that happened?
So, like, some sort of sampling technique with some sort of validation or, like, schema… like, JSON schema validation is one… is one thought that I had, at least to get, like, data types and things like this correct.
**Emilia Ferreyra (New Relic, Inc.)** 28:45 Yeah, that would be great, just to, like, whenever you know that there's, like, a small change that is going to happen, you can anticipate what it could potentially do with a sample payload.
**Kells Kearney** 28:55 Yeah, so I see a lot of value in basically just either kind of, like, a full-stop Boolean pass-fail, as well as, like, a more graduated, this is compliant because of X, Y's, and Z or something else like this. So I really, I really like what you've done so far.
**Emilia Ferreyra (New Relic, Inc.)** 29:13 Thank you so much.
**Andrzej Stencel (Elasticsearch B.V.)** 29:16 I have a question. Sorry, I haven't… this is the first time I'm hearing about this, and I'm sure I'm missing something, but I'm looking at this auto call run command. You're passing in a config.
You're passing, some payload.
OTLP payload, a processor, and you want to output it again into OTLP Make JSON.
Right? So, I guess you could do that… by just running OTL call with an OTLP JSON file receiver.
configured for a specific file, then a regular pipeline. There is OTP JSON file receiver, transform processor, or whatever other processor, and file exporter that would output the data into JSON again. And then you can compare the input with the output, like, outside of Collector with some… Well, anything, right? That's sad.
How's the difference, or…
**Emilia Ferreyra (New Relic, Inc.)** 30:15 Do that while… without having to actually run the collector?
**Andrzej Stencel (Elasticsearch B.V.)** 30:22 Well, yeah, you do have to run the collector, but you also…
**Emilia Ferreyra (New Relic, Inc.)** 30:25 Yum.
**Andrzej Stencel (Elasticsearch B.V.)** 30:26 How's the… Are we not running the Collector in this?
**Emilia Ferreyra (New Relic, Inc.)** 30:29 No, actually, it's a way to do that without actually, like, standing up the collector, having to run data through it, it's just, like, it, you just pass one payload through, and then it gives a before and after.
**Andrzej Stencel (Elasticsearch B.V.)** 30:50 Yeah, I'm not sure I see the difference. But yeah, the one problem with the Collector, like, with a regular pipeline, is that it will not stop after it consumes the pipeline. It would just keep running, you would need to know when to close it, but other than that.
I don't see the difference, but I'm sure I'm…
**Antoine Toulme (Splunk Inc.)** 31:07 I've done something like that. I had a STDN receiver, and the standard receiver would be able to kind of take data in, and then when you close Standard In, then it would shut down the collector.
Because you…
**Andrzej Stencel (Elasticsearch B.V.)** 31:19 That'll be good.
**Antoine Toulme (Splunk Inc.)** 31:20 So you could… you could pipe data in, and you could just, like, be like, okay, here's a bunch of data, I'm gonna push that in, and it's going to be ingested, and it's going to come out the other way, and… If you could… it's really difficult to commandeer the standard out.
But you could do that, I had a… my little program was meant for Bonsai's, and it's called Standard In Hotel. It's under my… Is it Hotel Warius? I forgot where I called this thing, hang on.
But it's got some logic in it about, like, how to deal with, Janodine and… Let me go.
Sweet.
Standing receiver.
And the receiver.go has… So what it would do is that it would use a component status thing to report status to say, hey, we need to stop.
And upon stopping the host of… tendon in was smart enough to say, if I get a stop, then that means I need to stop the whole collector.
So there's two components. The other one is… It's been a while.
It may not go, I think. Just, like… Mainline this whole thing without trying.
So, there's a host implementation right here.
So you can take a look at that, maybe this actually is, like… Exactly what you want.
But it's nicer in the sense you're not passing files around, like, I think, to Andrzej's point, it's like, the moment you pass files, then, like, light bulbs, right? Like, we're going to use a, you know, a TLP JSON file as a receiver in that case. That might be just as well.
Take a look at that, maybe? And, overall, like, I think there's interest for this, so… Yeah.
**Emilia Ferreyra (New Relic, Inc.)** 33:17 Yeah, for sure. And also, I would say that currently the solution, since it only ever needs the, the processor config, like, you can pass in, like.
An incomplete config, in the sense that there is not, like, your, your exporters, your, other types of components, you can just pass in, like, okay, I am trying to work out the kinks of what this transform processor actually does to data.
And so you wouldn't, if you were just in that, like, building and tinkering development stage, it is a little bit, difficult or tedious to, like, have a whole, like, otherwise no-op or basic… config that you would have to run a whole collector for to see what the output is. I think that the, STDN and, out does, like, make it a lot simpler, like, you don't have to also be, like, feeding live data through, but, But it's just, like, it is also much more accessible in the earlier phases of setting up your config, in the same way that, like, Auto Playground was, where if you had no idea what Auto was, or writing configs was, you… Can start there before you have to know how to set up a successful collector.
**Antoine Toulme (Splunk Inc.)** 34:49 Okay.
Take a look, take a look at this, it looks like there's some research, but hey, maybe, a point of detail is that currently you're thinking about adding this as a subcommand to the hotel call, thing. Personally, I'd rather it be a different binary altogether.
Where… well, any surface at this point is an attack surface, and I'm just worried that someone would just do something, like, they would find a way to… I'd like to keep our hotel call binary super tight. I might be in the minority here, right? People can say they don't like it, but… Having it a separate binary will also allow you to have a much faster or different release cycle.
I don't know.
It can still be inside of a contrib, right? It just needs… it might be nicer on the eyes and for you if you manage it as separate binary deliverable.
**Emilia Ferreyra (New Relic, Inc.)** 35:45 Yeah, I… that's a very valid thing. I think that the last time that I presented this here, somebody told me that kind of the opposite, where they were just, like, they don't want to manage a whole other binary. So I guess that's, like, open for discussion. I'm happy to do whatever y'all want to do.
**Antoine Toulme (Splunk Inc.)** 36:04 Okay.
**Braydon Kains (Google LLC)** 36:06 As maintainers, we've had discussions about security stuff that may be shifting Opinions quickly since we last spoke about it.
**Emilia Ferreyra (New Relic, Inc.)** 36:16 That might be…
**Braydon Kains (Google LLC)** 36:16 why you're getting totally opposite… opposite answers right now, but I do think as a separate binary, it would Probably be… easier… for everyone, Other than… the releases, people.
But otherwise, easier for everyone, because, like, you could just… I've also written something like this, I guess apparently everybody's written their own tool to basically do the same thing, but, like, that will pull in OTTL, like, the transfer processor, as a package.
To run unit tests around it, and you could do the same thing in a binary, and that would mean you're not… intrinsically tied to anything about building a collector, like OCB. Like, all of this could live in… the validator binaries config of just, like.
what processor are you running? Give it a Go module and a version.
And you'd… you would be able to, like, stay totally separate of any actual binary construction. That might be nice.
**Emilia Ferreyra (New Relic, Inc.)** 37:17 Okay, great.
**Antoine Toulme (Splunk Inc.)** 37:20 Maybe… myself, like… sorry, go ahead.
Sorry.
**Andrzej Stencel (Elasticsearch B.V.)** 37:24 Oh, sorry, go ahead.
**Antoine Toulme (Splunk Inc.)** 37:26 Just wondering, like, use cases, right? Are you trying to move that to maybe a REST service?
For validation? Are you trying to make it available for people so they can do this at home? What are we doing here? Is this just, like, going to be executed, like, a thousand times a second, or is it just going to be, like, something that people would do? I'm a little confused about that, but it might change a bit, like, the way we look at it.
**Emilia Ferreyra (New Relic, Inc.)** 37:51 Yeah, I… I wanted it to be both something that could be a way for… people to… like, it would be, like, an entry level or a first step when developing configs. I feel like it could be useful for that, but I also felt like with the second step that I was discussing with Kells, to have a, like, a test version, too, so that you can incorporate it into any workflows for… as a validation step, and that would happen as often as somebody would design their workflow to test it.
**Antoine Toulme (Splunk Inc.)** 38:30 Okay.
Yeah, okay.
Thanks.
**Andrzej Stencel (Elasticsearch B.V.)** 38:35 Yeah, so I agree, people have written these kinds of tools, and it's definitely valuable in this. Maybe part of my confusion is… you said, Emilia, that you don't want to actually run a collector, but the command is of the call run, and that's it.
**Emilia Ferreyra (New Relic, Inc.)** 38:50 Yeah, yeah, that's why I changed the name.
I changed it, I thought it was confusing, now it's diff, but, right, right, right. Yeah.
**Andrzej Stencel (Elasticsearch B.V.)** 39:00 Yeah, yeah, but still, yeah, it seems that it's a useful thing, you just need to…
**Emilia Ferreyra (New Relic, Inc.)** 39:05 You know, Coach.
**Andrzej Stencel (Elasticsearch B.V.)** 39:05 to packages. Thanks, thanks for doing this.
**Emilia Ferreyra (New Relic, Inc.)** 39:08 Yeah, thank you so much.
Any other questions, or we can pass off to the next person?
Alright, thank you for your time. I guess it's Antoine's turn.
**Antoine Toulme (Splunk Inc.)** 39:25 Thanks, Minia.
**Emilia Ferreyra (New Relic, Inc.)** 39:26 Thank you.
**Antoine Toulme (Splunk Inc.)** 39:28 Okay, folks, I've been on a weird quest to add some really weird stuff to the collector to allow people to change the way we formulate TCP connections, which is esoteric.
We have two things here. One is we have an open PR in Collector… I'll share my screen for a sake.
So, this has been debated, discussed quite a bit, so I just wanted to bring it up to your attention.
that this is an extension that we would allow to run on any config HTTP, any config gRPC-type server, that will allow you to override the way we would create the listening method. So then you would be able to change the way People would be, actually listening to connections, and, that might mean… For example, adding the ability to descend to a specific network.
Or to plug into a VPN, or what have you.
So this is passing, it's got some good reviews, some good approvals already. I think this requires a little bit more of a view from a maintainer. It's mirroring the dialer middleware PR that was merged in 165.
Any questions about this? And then I think I need to kind of make this more explicit.
Right, so… We return the net listeners, it's pretty much, like, it's very… the innards of your server has a different way of listening for TCP.
**Braydon Kains (Google LLC)** 40:59 This is strictly at a net listener level, Lori.
**Antoine Toulme (Splunk Inc.)** 41:02 Yes.
**Braydon Kains (Google LLC)** 41:03 Okay.
**Antoine Toulme (Splunk Inc.)** 41:05 So this is maybe weird, I'll explain that a bit more. So, for example, there's a Go library for WireGuard that allows you to create net listeners and dialers that would have the ability to plug straight into your VPN.
All that's software-based, there's no… no need to run anything on the host, but just to have that embedded into your collector.
So all of a sudden, you can start to have VPN-based networks that would be just collector-based.
Which is either awesome or terrifying, right? I don't know which one to pick, but you… you go.
Okay, and then, so the first part of this already landed, and we now have a way to do, custom dialing. So, just an explanation of what that means. So, here's an actual application of that through an extension that I built.
just as a way to prove what is possible with this, but also the interest for it, right? So, I've had a request from a user where they wanted to make it possible for them to actually pick exactly which network interface you're going to use when you make a HTTP call.
So there are multiple reasons why you might want to do that in some IT situations. Maybe, you know, you have multiple network routes out of your host, you're very opinionated, you've decided that you want to use a particular route because you want to test, like, maybe the latency or the timeouts on it.
How would you go about doing that? Well, in this particular case, we're going to use a network interface, and we have a way to set it up.
Note, we're going to do that in multiple components just to prove that it's possible more than anything else. There's no logic or rhyme or reason to it. We're going to export, and we're going to use this dialer middleware here, and we are going to also check for example.com, but also do it over this particular dialer middleware.
Just to show you that it's possible to use that in different ways. So there's two different use cases already. One is, I want to check this HTTP target is live, but I'm doing that over this particular network interface, and… or I would like to export data, but I want to do it over this passcode network interface. So… Let's say you were to use a OpenVPN, your TuneZero network interface is right here on your host, you want to use that for a variety of reasons, let's go ahead and do that.
Okay, there are multiple ways to do this, right? It's not like this is the grail of, like, going about it. The extension as much… All it's doing is that when you're about to return the dial function, it's going to go and pick up, based on your network interface you gave it, the network interface you want.
Based off that, it's going to look for your first APV4 interface. We're making some assumptions here, but that's fine, this is just for play. And once we get this, we're going to dial by using this particular local address as a way to dial out from here.
You can see how you could, like.
Continue to play with that, additional things, play with some of the additional aspects of it, based on what you want.
So, this is, very advanced. I don't expect people to play with it too much.
Any questions? Oh, Braydon?
**Braydon Kains (Google LLC)** 44:20 So, within the… dial context func, that means we could, like, do a gRPC client con in here, like a custom gRPC client within the dial context?
**Antoine Toulme (Splunk Inc.)** 44:32 Yeah, you can use that for gRPC2, it's lower level than gRPC, it's, like, really just returning the, net.com.
**Braydon Kains (Google LLC)** 44:40 Yeah, but if we can… if we can get the net.con out of the client con that we create in this, would that work?
**Antoine Toulme (Splunk Inc.)** 44:49 Yeah, you can, you can, so you would, the same way I did the OTRP HTTP exporter, you could also have the OTRP gRPC exporter that would behave the same way. You can set this on, on it, and then, it returns the same way, right? It's just, like, very uniform. Super low-level stuff, right?
Does that make sense?
**Braydon Kains (Google LLC)** 45:12 I think so. I've been looking into doing something similar, but, like, it would… I would need to do something at the entire gRPC ClientCon.
**Antoine Toulme (Splunk Inc.)** 45:22 Yeah, you can do that.
**Braydon Kains (Google LLC)** 45:23 context, so I think this would work for that, but I'm not 100%. I need to look into it again, but…
**Antoine Toulme (Splunk Inc.)** 45:29 Yeah, you can probably, like, play with this, like, fork it, play with it, and see where you go with.
**Braydon Kains (Google LLC)** 45:33 Yeah.
**Antoine Toulme (Splunk Inc.)** 45:33 The… So, I'm not sure what the future of the extension is. I'm happy to keep it here for a little while. I, as I mentioned, I'd love to get feedback and any issues, like, anything you'd like to see. If you think this belongs eventually to Contrib, feel free to let me know.
I'm not going to push that on Contra Bright… quite yet. I'm much rather interested in having the WireGuard extension, figured out.
So… Yeah.
Cool. Thanks. Yes, guys, I see somebody's in the chat.
Okay.
Alright, who's next?
I think there's someone else, if…
**Blake Rouse** 46:21 Oh yeah, that's me.
**Antoine Toulme (Splunk Inc.)** 46:23 take over.
**Blake Rouse** 46:23 Yeah, this one will just be quick, it's just a more informal, thing about the RFC for partial reload, this is the Phase 2.
PR for processors, and so this is ready for a look. I think Pablo's already looked at it a little bit and given feedback, and so I just wanted to bring awareness to it some more to get eyes on it to get it merged. I've already started working on the Phase 3 for exporters, which comes after processors, but… yep, that was it.
Thanks, Clay. Quick and easy.
**Antoine Toulme (Splunk Inc.)** 46:58 Yep.
I see.
Any questions for Blake?
Alright, anything else, folks?
Cool.
Okay, going once… Going twice.
Going 3 times.
Thanks, everybody, have a good day. I'm off.
**Braydon Kains (Google LLC)** 47:43 Thanks, everybody.
**Antoine Toulme (Splunk Inc.)** 47:45 Sweet.
**Jade Guiton** 47:45 Thank you.
