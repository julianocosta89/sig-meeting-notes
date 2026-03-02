SIG: Collector SIG
Date: 2025-09-16
Duration: 48 minutes
============================================================

## Zoom Recording Transcript

**Andrew Wilkins @ Elastic Observability** 01:07 Ray, how you going?
**Raj Nishtala** 01:09 Hello?
**Antoine Toulme** 01:10 I'm Irish.
Oh, shit.
Look…
Hey, Paolo, you wanna go first?
**Paulo Janotti** 01:49 Yes, I just wanted a core maintainer. I have a PR that seems to be,
They're waiting.
**Antoine Toulme** 02:01 I just…
**Paulo Janotti** 02:02 wanted some core maintainer to take a look at Merge. I already had reviews and comments, so…
**Antoine Toulme** 02:10 Gotcha.
**Paulo Janotti** 02:15 And, after that, I… I keep… I'm not planning to do, kind of, very fast one behind the other, but I'm gonna keep pushing to have the Windows arm ready, and even, on the releaser, because, you know, the…
Eventually, it's coming for us, so we're gonna keep pushing. Yeah.
**Antoine Toulme** 02:42 I don't think we have a core maintainer on this call.
**Paulo Janotti** 02:46 Yeah.
I, I, in that case, then I'll… I think after the meeting, I'll push through, it's like, I'll push through dev, or talk about the dev.
I'll… I'll ping you there to see if we get traction.
**Antoine Toulme** 03:01 Yeah, I'll, I'll, I'll also push it on the…
on the, the core leads, channel.
Alright.
Let's go to… Well, you good, you're done?
Anything else? Okay.
Okay, Raj.
So…
**Raj Nishtala** 03:28 Yeah, hey guys.
the… the… I was looking for a sponsor for a new, component in, Contrib.
Yeah, I think Andrew and Antoine, both of you are kind of familiar with that component, yeah.
Yeah.
So essentially, yeah, we, you know, we wanna…
unroll the slice, right? And aggregated,
record… a log record containing a slice into multiple… unroll it into multiple log records, right? So, I looked at the OTTL function aspect of it, and it looks like there were some complexities for interleaving that with other functions in the transform processor, like.
You use it with another function, and then…
Yeah, but the function in the pipeline next, it still thinks that it has to work on 3 records instead of 6, potentially, right? Because it generates new telemetry, so…
So, so because of that, we, you know, came to the conclusion in that thread that maybe a new processor is better than,
And I believe that's what…
I think Dan was also referring to earlier in a different issue, yeah.
**Antoine Toulme** 04:48 Yeah, that makes sense.
**Raj Nishtala** 04:49 Yep.
**Antoine Toulme** 04:51 So, yeah, I mean, the only thing I had to say for you is, I wish OTL supported this, or somehow, I think this has been kind of the guidance.
Forever is that you're supposed to do everything with a TTL these days?
But it's not… I don't know.
This… Kind of the stupid guidance that we have, yep.
**Raj Nishtala** 05:17 Yeah, I got the sense last time that there was some,
I think some folks were open to it as well, like, because potentially to…
extended to other signals as well, right? Metrics, for example.
something like this, have something like this supported for. So, having a new processor would mean you start… one could start with logs, and then…
Potentially extend the solution to other signals, like, maybe metrics.
Alright, so…
**Antoine Toulme** 05:48 fixes.
**Raj Nishtala** 05:48 That was another, Case for it, I guess, yeah.
**Andrew Wilkins @ Elastic Observability** 05:54 I think there probably are use cases where you would want to add
Metrics or logs to a batch.
Yeah, like… like you're saying, I think there are other use cases, so I kind of… kind of agree that OTTL might be the way to do this.
It's just a bit awkward at the moment because things get reprocessed, potentially, by the transform processor.
**Raj Nishtala** 06:18 Right. If you're not careful, I mean.
Right. So, we… we look at the number of… we… We essentially,
Look at the number of, it's a fixed number of…
records, right? That… that the state… up front, that the transform processor receives, and then it executes each statement on those fixed num… on each record, right?
**Antoine Toulme** 06:41 Yeah.
**Raj Nishtala** 06:42 So that's the… that's the bit. So it executes all the statements on each of the records.
And somewhere along that line in the processing, it has more records, and it doesn't know, right? It can't go back and…
Right, so
So instead of… yeah, so that was the… I don't know if there's any other function that does this currently. I don't… it doesn't seem like it.
**Antoine Toulme** 07:04 Boom.
**Raj Nishtala** 07:05 Yeah.
**Antoine Toulme** 07:05 There isn't.
**Raj Nishtala** 07:07 Right.
**Paulo Janotti** 07:12 I'm looking from outside, it's just perhaps a question for you to, strengthen your case,
it sounds useful to me. The question that crosses my mind is, like.
why not have that in a fork of your distribution that you build from OCB?
Do you think it's, useful to the point that a lot of people will use it
On the contrib, on top of contrib.
**Raj Nishtala** 07:49 So… so we could…
we could build something very similar to what's in the bind plane distribution, I guess.
it's… but that's the… I see, like, a common use case there, which is why I'm trying to get this into Contrib.
But yeah, I mean, absolutely, we can definitely have a custom processor in our distribution. That's the…
If we were to decide that this component is not going to be in contrib, then that's probably my next…
That would probably be something that I would propose to my team, I guess.
**Paulo Janotti** 08:32 Yeah, I… this is what I'm gonna say is actually a detour from yours, so feel free to stop me and get back to the top, but…
Because I see this requiring, challenge to get sponsors, right, for components.
**Raj Nishtala** 08:50 Yeah. And…
**Paulo Janotti** 08:53 what I… I've been thinking is that perhaps you… we went on some path
Through them to eventually become to contribute, but that we can keep, kind of, making the process easy, and at the same time,
observable to the contribib in a way that,
Kind of, okay, we would like to contribute this component.
Right now, it's part of this distribution, or you can have this OCB to build and use it.
And at the same time, keep the contrib, the contributors,
Involve it, the approvers, maintainers, are aware, at least, and involved to some level.
Through… when we get to that point, we say, hey.
I… we really think, and then people already have some knowledge, already… perhaps some of them already tried or incorporating their own distributions, you know?
**Raj Nishtala** 09:57 Yeah, I think we are at that point already, right, with bind plane.
the bind plane distribution, having that component, and then at least… I know at least two other… I think, Elastic… Andrew, I think you were interested in that, and… and I think our… our…
we are also interested in that. So, I mean, there's at least 3 distributions, potentially, that,
Are already interested in that component.
So… so I think… So, yeah.
**Antoine Toulme** 10:25 You're… you're not an approver, right? Is… Shmiky an approver?
**Raj Nishtala** 10:32 I… no, I'm not an approver, yeah, not yet. And then, yeah, I don't think he is either, yeah, yeah.
**Antoine Toulme** 10:37 Andrew is not poor.
**Andrew Wilkins @ Elastic Observability** 10:38 I am, but actually, so I don't think we have a use case for it in the Elastic Distro, but I'm not 100% sure, so I was actually going to ask if you could remind me, please, what are the use cases you have in mind for this.
**Raj Nishtala** 10:54 Yeah, so… So, oh, yeah, so, so, the use case was…
So, one was the CloudTrail aspect of it, right? The CloudTrail… you have… there's a specific processor for CloudTrail… there's an CloudTrail extension which does something similar, which… which essentially splits
The,
Which essentially splits the, the record into, into one log record into multiple log records, right?
So that's, there's a CloudTrail extension that does very… something similar today. But this… this,
this aggregated log… one aggregated log record can come from any source, right? It can come from CloudTrail, it can come from a Kafka, it can come from a Kafka, you know, receiver, getting… receiving such events.
Right? And then you have, instead of having, like, specific component extensions, which do… which recognize each
log record format, potentially, right? You have something generic which,
Which says, hey, this field is a slice, right? A slice of str…
this attribute is a slice log body, typically. It's a slice. I wanna,
you know, split that or unroll that into multiple records, essentially. So, something generic.
the CloudTrail extension does something… it looks specifically at the CloudTrail format, where it, you know, it expects the log to be in a certain format, right? Certain fields in there, and then it does something very similar to what this processor would do. But yeah, so I guess the motive of this processor is to have
irrespective of where it's coming from and what the format of the log record is, you can… you can… you can potentially do something like this, right? So, that's… that's my…
I guess, that's the… that's the… a genetic use case, irrespective of the source, yeah.
**Andrew Wilkins @ Elastic Observability** 13:02 Yep, thanks, thanks for reminder. Yeah, as you said, we have support for CloudTrail in the AWS Logs Encoding extension already, and I think for well-defined log formats like that, that's the way to go, that's my opinion, but for generic use cases, I suppose it could be useful.
Yeah, I think about it, maybe I'll sponsor… I need to think about that a bit more.
Sorry, Antoine, I cut you off before I was… kept, kept going.
**Antoine Toulme** 13:36 You're good. Just wanted to ask you, like, you seem to be interested, so… I think Raj indicated that you would be interested, you're an approver now.
you could… you could sponsor. Now, the thing about that particular component is that, for once, the sponsor is not gonna have to do a whole lot of heavy lifting and building community and…
being the person who has to be in charge of this code afterwards, because I would hope that between Raj and the BindPlane folks, there's going to be enough that there's going to be people managing this component moving forward, right? So, it's actually…
for once. Like, the only thing that we could say about this is that maybe there should be a way to do it in Transform Processor, and transform processor should be the Swiss knife for every possible change in a payload, and blah blah blah, but the reality also is that we need to ship code so that people are happy, and then we have use cases that we need to be able to perform.
I'd much rather have something that is maybe replaced in a year or two than nothing for two years, until we have a perfect solution that just falls in place. Because I've never seen that happen.
So, that's…
It all comes down to… don't think it's going to be a huge expenditure of time. It all comes down to whether this is something that, yeah, is adding value to
You know, if…
I would say it's been opened for just 2 weeks. I mean, just take heart, look at the list of all the issues with sponsor-needed label. We currently have…
38 open?
there's so much demand for people to bring stuff into Contrib,
I could make the case that this is…
It's not bad at… bad at all.
So maybe I would give it, Raj, I would give it just two more weeks for people to kind of have time to waffle through, understand a bit better, and what to review, and then in two weeks, let's maybe come back to seeing meetings, just push a bit more.
Does that work?
**Raj Nishtala** 15:40 Okay. Yeah, that's, that's fine, I'm, I'm, yeah, that's fine, I, we can, I can come back.
come back to it after two weeks. I think, Keith, the person who raised that issue is, yeah, he's following up on that in the ticket, but… and I think he also has a PR open, just for reference. He linked it to that issue. So, yeah, that's fine, we can come back to it, that's fine, yeah.
**Antoine Toulme** 16:06 Yeah, I think you should mention in the issue that you have a discussion about it at this SIG meeting, that you can, you know, if people want to, they can come and listen to the recording, and
The thing that's missing the most in this discussion so far has been any of the corners of OTTL, and I'm thinking about Tyler and Evan.
Who may… maybe they have, like, something up their sleeve, and they're like, oh, actually, we meant… we have a whole roadmap on this, and we know what to do.
But I haven't heard anything. It's just been 2 weeks.
I don't know.
**Raj Nishtala** 16:40 Yeah,
The only… the only thing I got from, so far is there's a similar function in metrics called CopyTo.
which appends, which appends metrics, though it doesn't unroll it. It appends metric records. It's similar, in the sense that it generates new telemetry, right?
Yeah, but that's, that's, that's, the only,
That's the only discussion we've had on, related to OTTL so far on this, yeah.
Yeah. But that's the closest to… closest to what… to what hap… what, to… to this use case in metrics, yeah.
**Antoine Toulme** 17:25 So, the other thing that I gleaned from discussions with different people on a project is that
The TTL itself has been growing organically, as you can see, right? There's just people adding functions. If you look at the backlog of PRs we have, there's a lot of, one of… I'd love to add one more function to a TTL-type discussion.
And unfortunately, there isn't a…
I mean, the folks who worked on this, they were just trying to build an expression language to get something done. They had a very specific set of use cases when they started out, and then they just padded on more use cases because it's a versatile type DSL.
there are people around OpenTeometry, and I'm thinking specifically about Josh Sharef.
who think that there should actually be a lot more thought about the semantics of OTTL in the sense of a model. That there is no foundation for some of the changes, or there are some inconsistency in the inputs, outputs, and the transformations and whatnot of the language, which actually contribute to some level of complexity and maybe
down the road, might bring this to a terminal complexity where you can't evolve it anymore, create all sorts of weird cargo code-type programming, or issues with this type of language.
So, a guy like Josh Sheriff, looking at your proposal.
Might actually have a very different uptake on this, which is, actually, we should
we should use this as a foundation to one of the requirements of what we want to build as a DSL moving forward.
But,
There's only one person in the whole project who is able to actually talk about this type of things.
And it's just good context, but…
it takes a whole bunch of people to think about this in a holistic way. We don't have those people.
So, justify, right? This might be…
You might, you know, in a sense, having just a digital processor that just does one thing really well and gets out of the way.
Maybe not the worst thing.
But…
**Raj Nishtala** 19:29 Right.
**Andrew Wilkins @ Elastic Observability** 19:31 I'll also raise this with my team. We have some folks on the team who work on Logstash, and they're interested in contributing more functionality that's traditionally been in Logstash to OTL Collector, so they might have some use cases in mind for this.
So I'll have a chat with them and then see if we might want to sponsor it.
**Antoine Toulme** 19:53 It…
**Raj Nishtala** 19:56 Yeah, I think Logstash does have a custom processor that does something like this, if I…
If I remember the documentation correctly, right?
**Andrew Wilkins @ Elastic Observability** 20:05 Yeah, I think there is. I don't remember what it's called, but yeah, I'm pretty sure there would be something like this.
**Raj Nishtala** 20:09 Oh, sorry, I think I lost you there for a bit. Can you…
**Andrew Wilkins @ Elastic Observability** 20:13 Yeah, sorry, my network's playing up. Yes, I think there is, but I don't know what it's called.
**Antoine Toulme** 20:19 Okay.
All right, Raj, we're good? Can we move to the next one?
**Raj Nishtala** 20:29 I think we're pretty good. Yeah, thank you, thanks.
**Antoine Toulme** 20:32 All right, Andrew, you have the floor.
**Andrew Wilkins @ Elastic Observability** 20:34 Okay, this is just sort of an FYI, more than anything, this issue 13778 on core was opened a couple of weeks ago relating to telemetry and authentication support. The proposal was to bridge
So, when we talk about telemetry here, we're talking about the internal telemetry of the collector, so sending logs, metrics, traces of the collector, and then enabling the collector to authenticate itself to external
backends, so the backends for the telemetry. We can already do that for the collector pipeline itself, but we can't do that for the telemetry, apart from simple headers for the OTLP output.
The proposal was to bridge the internal telemetry providers to the collector, authentication extensions.
I pushed back on this because I think it needs to be in the SDK itself.
And then…
My proposal is that we should actually consider removing authentication extensions from the collector, and then sharing them between the SDK and the collector. So actually going the other way around.
But that might be contentious. So anyway, I wanted to bring this to everyone's attention and see if anyone has thoughts, and maybe could also provide their opinion on the issue.
Any immediate thoughts?
**Antoine Toulme** 22:04 Immediate thought is that we should…
Sorry, I'm talking without looking, someone's got far too. I thought that maybe the Go SDK should have complete control over the YAML that goes under the telemetry tree when it comes to that.
That's what I have.
So, yeah.
**Andrew Wilkins @ Elastic Observability** 22:25 Yeah, so, like, in the hotel conf…
package, the OpenTelemmetry configuration YAML, is that what you're thinking? That would also grow support for OAuth? I think that's already on the plan… on the cards as well.
So I think that makes sense.
**Antoine Toulme** 22:38 Yeah, I wonder if you could do this today, at least you could put headers, right, under this OTRP key.
So, it's not super cool, but you could have, like, the token Or some sort.
**Andrew Wilkins @ Elastic Observability** 22:51 Yes, yes, but if you wanted to do something like MTLS with reloading of certificates and that sort of thing, then it's… then you're on your own.
**Antoine Toulme** 23:00 you better go talk to the Go SDK for them to expose some config that we can expose into that branch of the telemetry tree, so that.
**Andrew Wilkins @ Elastic Observability** 23:08 Yep.
**Antoine Toulme** 23:08 They can do it, but… We need to stop trying to do everything ourselves.
**Andrew Wilkins @ Elastic Observability** 23:13 Yeah, that's my opinion as well. Okay, thanks.
So, if I understand… Yeah, anyway… Oh, sorry, go, go ahead, Brush.
**Raj Nishtala** 23:21 So instead of having the authentication be done by an extension, we're going to do this in that specific component itself?
**Antoine Toulme** 23:29 components. So, it's,
In the sense, right, the collector is a Go app. It's an application that's running with the Go SDK for OpenTelemetry. The Go SDK for OpenTelemetry takes configuration, and once you bridge the fact that you're now talking about a Go application with a Go SDK that has configuration, then let's follow that logic to the end, meaning that
you're now configuring a Go SDK. A Go SDK can take a number of configuration variables, maybe as environment variables, or maybe as a programmatic configuration that you can inject into the Go SDK. In our case.
we have exporters that we can configure under metrics, traces, and logs that will actually configure how the Go SDK exporters are done, and that should take configuration of a standardized and
completely part of the Go SDK by default.
**Raj Nishtala** 24:20 Right, okay, so that's… so you would specify that in the exporter itself, then?
**Antoine Toulme** 24:25 by the exporter of the Go SDK. So if you look at the detail of that YAML, it's kind of weird, because it says service telemetry, and then it says metrics, traces, logs, and under those, there's the readers, and periodic exporter, and all that. This, the moment you pass metrics.
or traces, or logs, now you're in the Go SDK function. Like, you're talking about a Go program.
Yes.
Yeah.
**Raj Nishtala** 24:50 Yeah, makes sense. Okay.
**Paulo Janotti** 24:52 Well, so this is basically, let's say…
Instrumenting the collector as a goal.
application.
**Antoine Toulme** 25:01 Yes.
**Paulo Janotti** 25:02 And the configuration, also coming from the SDK, in this case. But the configuration is, what's the stability of YAML configuration, on the SDK, on the Google SDK?
**Antoine Toulme** 25:17 It's… I don't know, actually.
**Andrew Wilkins @ Elastic Observability** 25:20 Well, the version is 0.3, so I don't think it's stable. I don't know what the…
Stability level is there.
**Antoine Toulme** 25:26 I know there was a point of contention with some of the members of the OpenTeometry Core team, of Collector Core, as of February of,
as of February, when we met in London at the… we had a maintenance summit, Dan Jaglowski was making the point that some of this was too tight and could not allow us to do additional telemetry attributes or things like that. There was just not…
The Go SDK is very declarative, right?
So you can't… you can't change the telemetry of your… of your component easily after the fact, and so you had to kind of do backflips to make it happen.
Which, actually, is something I'd love to talk about with all of you, but… So, anyway,
Andrew, did we… did you get everything you wanted? Anybody else? Like, go ahead?
**Andrew Wilkins @ Elastic Observability** 26:13 Yep, just wanted to raise awareness of the issue and see if anyone.
**Paulo Janotti** 26:17 Yeah, I can voice my agreement with both of you that from the high level, it's what makes sense. The collector has the history of not having that, because the collector came before the Go instrumentation. So, yeah, makes a lot of sense.
**Antoine Toulme** 26:38 Okay.
**Andrew Wilkins @ Elastic Observability** 26:41 Thanks.
**Antoine Toulme** 26:44 Okay, so, I do have one item that I'll drop into here. I didn't know if it… don't know if it's very useful or anything. I just, also…
consideration, discussion, awareness, whatever you want. I'm having a bit of a pickle, and…
It's turning into a bit of a weird discussion about the fact that, pretty much, the issues seem to be really hard to read.
Let me show you instead the factory option PR. I'll put that in the doc as well.
So, in a nutshell, the issue I'm having is that currently, when you look at the collector core codebase, it has a number of intertwined dependencies, because there is a pretty dirty dependency tree where all the components end up depending on the Go SDK. Exactly the discussion we just had.
And, I don't like that. The reason I don't like that is I just got a fuss alert, because my component has nothing to do with any of the stuff that's in the core. It's now having to inject into its indirect dependency, transitive dependencies path, all of that.
all of the Go SDK, and of course, we have a high CVD somewhere in the background version or something, and now I have to fight for that and tell it that's not such a big deal. That is not going to fly.
So, what I want to do instead is to start to, find a way to separate the code that is defining which telemetry attributes you're going to set on a component.
And the implementation of how you actually implement the meta provider, the trace provider, and the log provider.
Right now, everything is under internal telemetry in one big package that is handling both.
So, I tried to do that in two steps. The first step I did is, 1387,
which, is an imperfect draft PR right now, which allows you to break the current module in two by creating a separate module called Internal Telemetry Import.
And, move all the stuff that actually is doing the injection of the meter log trace providers into a separate module.
If you look at the diff, it's, pretty cool, for at least one reason, is that all of a sudden, you drop a bunch of translucid dependencies from all the packages.
And, well, that motivates me.
I can… I can maybe share my screen so it's a bit more poignant.
No.
That's not it.
Oh, well, I'll just shut my desktop.
Okay, so…
This is the first approach. You take the code, and you split the module in two, and you create a new module.
So, lots of file changes, a negative diff.
lots of weird changes, such as, you know, adding a new telemetry import module, and then you can start to see how even mdataGen had, like, this type of injection of dependency, which is kind of gross in the first place, right?
And same goes for, so, you know, component status, for example, drops a whole bunch of stuff, because all of a sudden it doesn't have this weird dependency track.
And so on and so forth, right? So we see that. The difference is that we're creating a new telemetry import package, and what are we keeping around? We're keeping around
this type of stuff, right? So we're moving Logos app, for example, from component attribute to telemetry import, and this moves around.
Right? Same goes for a meter provider.
Which is just moving, and then the tracer provider.
So, this is moving to internal telemetry impulse because, for better or worse, those custom providers.
Are used in tests by OTLP receiver and the memory limiter processor.
If I can show you…
So that was pretty jarring as an experience, as you can imagine.
Let's see if I have receiver… okay, processor… so the memory limiter processor in its factory test…
Like, it's just a slight refractory. We're not changing anything.
So what that means is that the leaf of the dependency tree still has those dependencies on those… on those additional things, but it's only because they're using that in test explicitly. The factory.go.
still has it, because they have this weird thing. So, what… what they did, what they were doing,
in internal… Do you run this…
to change your telemetry settings. So, let me open that so you can see.
What's the whole point of this?
Right? Why are we doing this?
Is that… We don't like the default telemetry settings signals that we get.
So we decide instead that we're going to remove some of them, and so we'd say 10mmetry without attributes, we take the existing settings, and we pass those three keys, and we say we're going to remove those three keys from the…
blogger, from the metrics, and all that. So that means that we're going to have maybe a less causality coming from that particular internal telemetry for that component.
So that's a really interesting, but weirdly niche case, I guess. And anyway, after that, you have to call this function explicitly to do that.
So I still like… don't like this. I find this to be not so cool.
But at least, now we get our dependencies nice and tight, so if, let's say, you were to build a special Git repository with just one component in it, then you're not depending on this bunch of weird dependencies.
Right?
Yay? Maybe? I don't know.
Okay, not good enough, because still pretty dirty, so I did one more thing. On top of this, I added
a factory option. So before, as you could see, you would just, in the middle of your processor code, when you initialize it, you change the telemetry settings, and you say, without attributes, and it just works. That's disgusting. I don't like that. Oh my god, we're being weird about this, right? So what I want to do is do it once, I want to do it at institutions.
Because every time you call that method, it also resets some fields on your telemetry settings, and I got spooked, thinking maybe this could actually leak something, which is me being dramatic.
So, don't… don't take me for… don't take my word for it.
So, I then print a factory option, so this is the exact same code as before. Let me see here, let's go to the processor…
We're in that memory limit processor, so factory.go now looks like this.
We no longer manipulate these telemetry settings anymore, we don't do that, right? What we would say is that when we are going to initialize with the factory, we're going to get a chance to manipulate the set that is being passed in, and then we will be able to filter
All those things out of the set of attributes that we will allow for the telemetry of that component, and then return the attributes.
So…
It's so nifty, because I think it's more discoverable by people. Like, you look for factory options more than you look for weird functions that are doing weird stuff.
And you don't really still need to know anything about the SDK all that much. The only thing you will get from the SDK is this very small package module that is just describing some conv attributes, so mostly it should be okay.
And, the same goes for the OTLP receiver. The LTLP receiver is kind of the same approach.
Receiver. Let's up your receiver.
factory.go…
So, we're importing this attributes module, and then we're passing that in, and we no longer need to do weird stuff like OTRP.go had, where you would be doing this in the middle of the creation of the receiver.
Note, okay, there's some nitty-gritty. So, for example, factory test used to depend directly on that code, and I'm like, this is disgusting, I don't… I don't understand why we're calling the implementation of the log provider here.
So instead, I'm just going to test what it was supposed to be testing, which was you're going to make a core with a field, and you're going to make sure that it's coming through, and…
It somewhat works.
So very complicated for no reason. I wish I could decompose this change more. The feedback I'm getting is that instead of the factory option, we could use a spatial host interface that will allow us to perform this type of changes programmatically.
Where did I move all this code? Instead of having a telemetry import module, this particular PR actually makes everything move under service.
Because I think that's where it belongs.
Oh, boop, oh, where is it?
Okay.
And if you look at service, thegraph.go now has a factory attributes, little annotation, interface here, which is…
weirdly, like, you know, just implemented by all the different X-Factory type patterns, and for each of those.
If you're able to start, you know, cast it as such, then you'll be filtering the attributes you would get by default here. You pass them in for the telemetry settings, and then after you're done, you initialize with that.
And we just do that for receivers, for processors, all that, once…
That's build time, instead of having resets on those fields whenever we feel like it.
And that's… That's where I am.
Does it make any sense?
**Andrew Wilkins @ Elastic Observability** 36:46 I think this makes a lot of sense. Only question is…
a certain, I guess, comment. I've been trying to remove dependencies on the SDK as well, and…
**Antoine Toulme** 36:58 Yes.
**Andrew Wilkins @ Elastic Observability** 36:58 isolate them to the OTel… the new OTELConf telemetry package.
I'm wondering if we… would we still need a dependency on the SDK?
If we moved it under service telemetry.
I'd need to refresh my memory on this component attribute thing, but is there a hard dependency on the SDK there? Or is it…
**Antoine Toulme** 37:22 Right now, there is, because it's mixing both.
If you were to look, this is the change of that. So, the telemetry, internal telemetry, telemetry.go, currently, is making… so when you say with attribute set, you see here how it's…
Resetting your logger, provider, meter provider.
Right here, right? If you go to attribute.go, then there's some stuff that is clearly, like, in the implementation-type territory.
Right.
And so, the only thing that's left in component attribute after my change is those keys.
And that's it. So… You could… you could go with that and be okay.
What else is known? Totems?
So, moving on the service, everything that you don't want to expose feels like the right crawl, but the…
So the use case that I'm… so I'm talking with Jad, right? She's looking into this with me, and the reason I reached out to her is because she's the author of a line of comments in internal… actually, it goes there. It says, eventually we want to make this public, with that attribute and with attribute set.
But I don't think this should be this.
should really not be something that you do right here and then. I think you should do it much later in the process, when you're about to create the component. But she's invoking that there might be some additional use cases around setting those components and maybe changing the attributes,
Multiple times, or in some situations. And so she started to detail some of those use cases in the issue that they asked me to create for this.
So, going back… Here, you can see that I'm already having a lengthy discussion with both Pablo and Jad.
And… I opened an issue…
And then this is the discussions, the page-long discussions we're having about this, which is… Not cool.
If there's a smaller delta we could go with that would work for me, this is all coming from the fact that I started to build applications that do not actually have a dependency on service module.
And all of a sudden, I don't need half of the stuff that is coming from this, and it's giving me a whole, like, a hard time for no reason. So I posted two different applications that I built. Let me show you…
One is called Standard Eon Hotel. It's a very simple application that is just going to be able to take a file, for example, and cat it into it, and send it to some OTLP endpoint. You just pass some unwant variable, and that's your configuration.
And then the other one is just open source, which is a technical add-on that lives on Splunk, that allows you to do all sorts of things, and has its own main.go, and does not need to have a discussion about, like, the lifecycle of a collector or anything like that, because you're doing your own thing.
You're just pretty much meshing together two components that work, and that's your application.
So, I don't think a collector should always be running as a service module. I don't need the whole enchilada of all the telemetry that is offered by all those things, and I'd like it if we kept it as small as an API surface as possible.
If we go right now to…
So let's go to OpenTeometry, collector, and let's take a look.
This might be something, a deeper conversation, which is, you go to component, you go to go.m.
Can we either riddle down the list of all the things in here?
Or, be mindful about not adding more stuff moving forward.
For example, None of this should be here.
Right?
I mean, Component.go makes just nothing. Like, there's barely anything going on. I can pick another one, right? So we can go to receiver, for example, and receiver.gov
Go.mod is… Depending on logar? Standard R?
there's a dependency on protobuf, can we discuss that for a second? Like, what is going on? Like, do we…
Maybe that's PData that's seeping in, what about, for sure.
Right, so there might be some discussion that we're not currently having about DepGuard or this type of stuff, so we can start to have a smaller API surface.
Does that make sense?
Well, mate.
**Raj Nishtala** 42:00 Yeah, I think so.
So, another thing that we've, another thing that I've noticed is, you know, we regularly have to bump up these dependencies because there's a… for CVE as well, right? So, reducing the number of those indirect dependencies will definitely go a long way.
In… in… in releasing… we've had to release patch… make patch releases with bumping some of these dependencies just because of that reported CVE. So yeah, I think the…
I'm for reducing the number of indirect dependencies by…
Restructuring the core.
For sure.
Yep.
**Antoine Toulme** 42:38 Okay.
Thank you.
Okay.
My rent is over.
**Andrew Wilkins @ Elastic Observability** 42:46 Yeah, since I've been in this code recently, I'll have a look at the issues and see if I've got anything to contribute to the discussion.
But I agree that we should…
Cut down the dependencies as well.
**Antoine Toulme** 42:58 Yeah, but I feel like I'm taking, the China and the bullshit,
No, the bull and china shop approach to this, which is not good. I think I'm roughing feathers, I'm not… I'm also trying to get somewhere with this, which is not a good idea, maybe I should, you know, maybe just be a bit more intentional about what we're trying to achieve here. I don't want to make a mess of things, so…
Yeah, keep me honest.
But I figured you might have some… some opinions.
**Raj Nishtala** 43:32 Would we have a number of API breaking changes with this?
I think…
**Antoine Toulme** 43:37 the intent.
So, I mean, so, you know, we're talking good game about how the fact that we're doing stable, and we've got this collector thing, and it's making a lot of sense, and we're good to go, and all that. My personal feeling of this is that while we have an internal folder in Hotel Collector Core, we risk that we may have,
Unintended indirect dependencies like that, they'll continue to seep in.
And we have too much stuff under internal. So, for example, it's something I shared about two weeks ago. I asked, could we please not have internal shared component? Internal shared component is used by the OTLP receiver.
And…
I've been trying to do something with this for a good part of, like, 18 months. I look at it sometimes, I stare at it for an hour, and I don't know what to do with this code. It's showing that we're failing at being good about how
Yeah, and this is another violent thing construct, it's not even compatible, right? It's not even the same code anymore. And, it shows that, in a sense, like, the graph approach that we've taken and all that does not work. It's… it's not a good… it's a… it's a… it's a leaking,
It's a leaking concept.
Right. We did not think, when we built all the collector stuff and all the components, we're like, okay, we're gonna have one component that's gonna do this and all that. And then all of a sudden, oh, the same component is used in three different places, do we create three of them, or just one that's using… used three times? And how do we manage the state of that? How do we manage the state of that pipeline?
Can we stop the metric pipeline, but keep the trace pipeline up? Okay, but which one do we shut down first? How did that work? All those type of weird questions were not answered. That's just one particular problem. The telemetry issue
If you look at who touched his last time, it was Dan Jaglowski, and as I mentioned, he started the year in February in London by saying, hey, I'm not able to move forward with the telemetry challenges.
And the reality of it has been that this is the last big block for us to get to 1.0GA, whatever you want.
And we…
I don't think we have… we don't have it. What that also means is that only core components have access to anything that's in internal.
None of the contrib components use any of that logic. So all this, while it's a beautiful idea to have an API that allows us to do stuff right now in internal telemetry to filter attributes and whatnot.
We're not actually testing that at large with a large population of components. We're not learning from that.
And, having it used in OTLP receiver and memory limiter processor are two very small edge cases. Like, they already are very weird components in the first place, because it got too… too much attention.
I'd be more interested to hear about, like, what telemetry you'd like to see for a relatively benign, like, SQL Server receiver, right? Like, what is it that's missing? Why is it that someone would be hung up about, like, how we use this stuff, right?
So, we're…
And since then left, I don't think we've been able to move forward on the internal telemetry work as much, and know that we have people looking at it from different… like, there's a lot of perspectives on it, right? And if you look in this call, we talked about it several times, like, what should the configuration for the telemetry look like? How do we manage it long-term?
So, I just want to point that out, is that… We may actually use…
We could… you could use this interdependencies angle as a…
As a blunt, like, instrument to kind of slow down exactly what it is we want to keep inside internal.
Right.
**Andrew Wilkins @ Elastic Observability** 47:46 I don't have anything else to add on that at the moment. I'll… as I said, I'll have a look on the issue, and…
Chime in, see if I've got…
as you said, to keep you honest, I'll see if I've got any other, suggestions for things we could do. But I haven't been looking at it holistically, to be fair.
**Antoine Toulme** 48:06 Yeah.
**Andrew Wilkins @ Elastic Observability** 48:06 But anyway, I'll think about it and go back to you.
**Antoine Toulme** 48:10 No problem.
Is it influence?
Okay, raj, I'll put you down to the list of attendees.
**Raj Nishtala** 48:27 Oh yeah, sorry, I forgot, yeah.
**Antoine Toulme** 48:29 No, no reset up. Cool. Have a good one.
**Raj Nishtala** 48:35 Thank you, thanks.
