SIG: eBPF instrumentation
Date: 2026-03-04
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/9uqeNLTkvdz2G4VC556PJrfHDSWo0S87UtWl-vQYJrW7oEY7QSk4zrxIs_uJojJT.moLbnTOZCBBSvS3c
============================================================

## Zoom Recording Transcript

Tyler 00:00:44 Hey, Raphael.
Rafael Roquetto 00:00:46 Hey, Tyler, how's it going?
Tyler 00:00:48 Doing well. How are you? Are you at a airport, or where…
Rafael Roquetto 00:00:52 No, I'm a university, so… I just had to take my wife to something around, and it just came here.
Tyler 00:01:01 Oh, cool. Yeah, I gotcha. Is this… did you go there, for your undergrad?
Rafael Roquetto 00:01:06 No, no, no, no. It just happened to be on the way, and .
Tyler 00:01:10 Yeah, yeah, cool.
Rafael Roquetto 00:01:11 Indigo.
Tyler 00:01:11 Yeah.
Rafael Roquetto 00:01:12 I was actually looking for coffee, and I ended up.
Tyler 00:01:14 Yeah, That's the reason I do most of the things in life.
Nice, yeah.
Hey, Giuseppe.
Giuseppe Ognibene | Coralogix 00:01:26 Hi, guys, how are you?
Tyler 00:01:29 Doing well.
Rafael Roquetto 00:01:31 How is the connection, by the way? Is it alright?
Yeah. Okay.
Tyler 00:01:35 There's, like, a little chop, but it's not, like, yeah, it's… Not even… barely noticeable.
Rafael Roquetto 00:01:40 That's it.
Tyler 00:02:00 Well, I had,
asked Nicola to run this last week, because I thought I was going to be out, but it turns out I'm not out. Oh, there's Nicola, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:02:10 That's work for me. Excellent. Thanks for being here, Tyler.
Tyler 00:02:14 Yeah, thanks. Yeah, I, it ended up… thing got canceled, and so I ended up being able to make it. So, yeah, if you were really… had your heart set on leading and sharing.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:02:24 No, no, no, I love how you guys… how you do this thing, so, yeah.
Tyler 00:02:28 Okay, cool, cool. Yeah, I'm happy to… happy to jump back in then.
But yeah, I mean, on that note, I see we got a pretty good agenda going so far, but if you haven't yet, please go ahead and add your name to the attendees list, and then, if you have agenda items you wanted to talk about, go ahead and add them there as well.
And, let's see what time we're at. We can get started here in just a little bit, yeah.
Cool, yep.
Okay…
Well, welcome everybody. Yeah, let's, let's jump in here, then. So, if you haven't yet… yeah, I think, I think everyone's still on, but just in case you, wanted to go ahead and add your, add your stuff here. Nimrod, do you want to start us off with talking about, Go interpretation for general TCP interpretation?
Nimrod Avni 00:03:33 Yeah,
Yes, I just saw, Nicola's PR, and I remember I saw it open, but I just encountered…
That we have kind of a different path of, like, where…
normal HTTP, like, we go through some different… one pipeline, and for, like, GoHTP, we go through a different pipeline, and for sure, I know it happens in other protocols, because for…
Go, we have, like, different events coming from kernel space, and for TCP, we do, like, the TCP, and then classifying user space.
And then there's, like, a different pipeline there, so…
Yeah, I'm just wondering, one, how do we make sure that,
it's, like, the same. For example, in GoHTTP, we don't get anything of, like, the large buffers and, like, post-classification of, like, AWS, GraphQL, all the stuff we added recently.
And in general, like, regarding… because I saw we do, kind of.
for some stuff, like, that I added, I didn't add an equivalent implementation in Go.
and I don't know if I… if I need to, or do I, like, what's the… in general, like, what's the… the advantage of having, like, for example,
Implementation in… of, like,
you know, I guess for stuff like gRPC, that we know we have limitations, that we have, like, when we instrument the library, it's probably, like, better, because we have some information that we might not have on the network level. But in general, is there, like, a guideline on how we, want to move forward with, like.
Doing always both instrumentations when we add new stuff.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:05:23 Yeah, it's a really good question, and same thing that's been bugging me for a long time, because every instrumentation we add, we now have to add it to go, specifically.
And… And especially now that… I mean, when you do the instrumentations for,
for the standard libraries in Go, that sort of makes sense.
But recently, it's been, especially for some things like MongoDB, or,
I don't know, Kafka, and people use various libraries, and then it's sort of proliferating in what instrumentations we need to add. So, that's been one thing, and obviously, it's pretty annoying, so you add MongoDB support, now you gotta add it in Go, and then you have to imagine what libraries people use.
So I went on the path.
To… to do this, but having said that, traditionally, it's been easier to instrument things in… go.
comparable to instrumentation with the K-probes, and what I mean by that Originally, when we started this.
You just have to add a U-probe, extract strings from the Go objects.
Usually it was easier, and you didn't have to worry about, instrument HTTP, is it SSL or not?
Or is the gRPC using SSO or not? You kind of tap a little bit.
up the stack, so you kind of get the objects before it hits the wire. It was easier to do context propagation.
Right? Because… this thing…
You kind of handle the go routines, and you're able to pull stuff off the go routines.
And so on.
So, I think there's a good reason to keep a lot of the stuff that we existingly have, but…
It also means something like, so I was… there was an open issue about
go fiber, and that's one of the servers we don't support.
But it's HTTP. At the end of the day, there's nothing special to it about it.
So… I think we can do two things.
and… You know, we can… we can discuss which one's better.
So I added on this path, I made a POC, and it actually did work.
I was able to send whatever was not handled
At least that first step. So, let's say you're… you're using a strange Kafka library, and the majority of the stuff is something called GoNet. That's where the meat of the thing is, gonet.c.
So, essentially here, I split off some parts of the generic tracer, and I tapped into two things, which is NetFD read.
an ad write, which is an equivalent to our TCP send-receive that we get on the Cape Revs. So, technically, if you wrote a Go instrumentation, and you just tapped into two things, and I just called down into our existing stuff, everything will just work.
And then, for SSL, we need to tap into the GoSSL library, which is equivalent to what we do for LibSSL. So that's not here, I didn't do that part, but…
I know how to do it. It's not a big deal.
And so that leaves us with a question, then, we can easily get everything we want.
Essentially.
And get large buffers and all this stuff.
By just pushing down to the existing code we have, and nothing will break.
The… the one thing that I know is that these not FDRead and FDWrite are called a lot.
So they'll be called for every package in and out.
And what blocked me, and what's told me from continuing here, is I wrote the POC, but I was like, hmm…
how do I ensure I don't get duplicate telemetry? Because now I need to know that this particular packet, or whatever it is, was handled by
the existing Go instrumentation, or is it something we haven't handled yet?
And… This proved a bit challenging.
The reason why I'm saying that is because, let's say we take something like…
Some of these libraries, they do not actually use the same goal routine
to handle a request and serialize on the wire. They may do this async, so they'll kind of launch a Go routine to send the data over. So the Go routine won't match, so I was like, oh yeah, the connection info will match. So the connection info was used.
Then,
But we need to have 100% correct connection info, which in Go is done, but there could be bugs. So, that's one of the last things I kind of needed to work in my head of how do I detect that this is already being handled, so I don't do it twice.
And after we do that, I think…
We should be able to just call into the… Existing stuff we have, and…
Protocol detectors will work, and they will make it to the other side as a regular event, and so on.
That thing…
Nimrod Avni 00:10:43 Also, maybe adding the…
at least for HTTP, I don't know if it's the same for other protocols, like, having…
instead of having, like… because we already detect, like, HTTP based on TCP in a different path than we do, like, all the default TCP, making sure that the GoHTP also goes through that pipeline.
Yeah. And, like, have the same, like, enrichments, and I tried it because I worked on…
I'm trying to do a POC with, like, header extraction, with HTTP, and then I was like, why is it not working? And then I saw the.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:19 Oh, yeah.
Nimrod Avni 00:11:20 Yeah, and I did the skip, go.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:23 Yeah, and.
Nimrod Avni 00:11:24 matters, whatever, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:11:25 Anywhere, yeah, yeah, I know.
Which is kind of sad. And I needed to, so this needs to happen from, I think, from Grafana's side, we want to instrument… this is why I started working on this OpenAI thing. We want to instrument our Gen AI stuff, and they're all written in Go, by the way, so we don't use any Python, so all our Gen AI stuff internally is Go.
So this needs to work.
Nimrod Avni 00:11:50 No.
Mattia Meleleo 00:11:51 One thing to say, if we just want to support HTTP for this case.
I think we can just create an HTTP event from Go, because right now we have two kinds of HTTP events.
And if we create the same, that will get classified as, like, a normal HTTP, and we'll get enriched or processed as a different kind of,
Span in… in user space.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:22 Yeah, so the thing is, I think somebody attempted this a while back, and the key is the body, right? And right now, the Go instrumentations don't read the body, they just read
It's unlike the regular instrumentations, we have the buffer, right? And then we parse out what was the method, what was the URL. What we do right now for Go, we pull those things out of the request. It's already parsed for us.
So the actual meat of what we need for HTTP classification, or payload extraction, is in the body. So what we need to do is actually
Read the body and ship it to you using the existing large buffers.
I think we could do that. If we just want to do it for HTTP and not in a generic way, then maybe that's a first step that we could do.
the response and the request are already present as objects in the Go user space objects.
And I believe…
the JSON RPC support that was added, that's currently disabled in our test because it's a little bit flaky or something, the JSON RPC work looks at the body, because I think the developer that added it, they went and scanned that body for the RPC method in the JSON body.
So the code is already there, we just need to use the large buffer send and shoot them over.
On the rain buffer.
And I think that might be a quickest way. If you want to just handle HTTP Numrad, and not worry about my long-stall PR and dealing with this, I think that's probably looking at that.
serializing the body. We need to do the response as well.
Same way.
Nimrod Avni 00:14:03 I can… I can start… I think maybe, yeah, I'll try to do it as a…
at least for now, maybe, like, in a different PR, and then.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:12 Yeah. Make sure that the same, like, the HTTP flows through the same, kind of.
Nimrod Avni 00:14:16 path.
Yeah, I just wanted to know what's, like.
What's your thought? Is it more like…
if you… if in the future we want to mostly rely on TCP, unless, for example, gRPC, I know, like, in Go, you don't need… you don't have all the issues with, like, you go in the middle of a request and with HVAC and stuff, so some stuff might be good to do UProbes, and some stuff…
Might be not.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:43 Yeah, exactly, and I certainly don't want to add every Kafka and MongoDB library in the world, or a Redis library, to support in Go. So, I would… I want them to ship over to the TCP and use our protocol parsers to do this work, rather than having to write
And I was hoping that if we do that, then we can maybe just even remove some, because there's more U-pros, and if this works well, like, why bother?
So… I mean, it's important to do it in Go.
I mean, the U probes, when we need the context propagation.
But for stuff, we don't need context abbreviation, we just need to extract the protocol, and that's a Redis database, and we're just extracting that.
Nimrod Avni 00:15:32 Okay.
Sounds good.
I think I… I think I have a better…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:15:36 chance at this now with what Mattia added with… with the cast wall. So then, I think, with what you just added.
I think I'll be able to just immediately tell, is this thread in one of these guys that is handled?
I was hoping that I can reuse your stuff, because the map is already there, and then it is helpers, I can probably just say, was this ever seen by any of the existing probes? And if it has, then…
Leave it alone.
And then I can just say.
For the rest, just shoot it over to the common code and have it parsed.
Maybe, alright.
Or the connection info.
Hopefully that's enough.
Nimrod Avni 00:16:19 Thanks.
Tyler 00:16:21 Rafael, did you want to mention this as well?
Rafael Roquetto 00:16:23 Yeah, so, it's a little bit tangent, since we're talking about the,
different ways of doing things. So, a part of the, .NET, work.
the, like, as you guys know, the idea was to inject headers on ingress.
And unfortunately, that will not work. So there is this branch where I expanded TP injector.
To… to be able to do that, so TP… in this branch here, still work in progress. Basically, TP injector, you see… you can see we have ingress and egress there, and it's dealing with HTTP, only, so, no gRPC for now. So…
with .NET. Turns out the manipulating packet on ingress
it… you know, long story short, the kernel doesn't like it, so that will not work. So for .NET, I talked to Nikola, and we're gonna try a different approach with U-Probes and see if that works, but that's a different…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:17:26 That's not what I wanted to tell you, so just a quick update.
Rafael Roquetto 00:17:29 But the work is there. I still want to pursue it without injecting the,
the packets, but the idea is to still leverage socket programs, like SOCMessage and SOCOps.
For, yeah, for, like, protocol detection as well, and parsing.
No encrypted, stuff.
The reason for that is performance.
Right now, we have some issue with performance, like we talked about in the past as well, with K probes and U probes firing.
These programs, they're much leaner, because there's no copy involved. You always, no matter what part of the pipeline, you're always dealing with direct packet access and packet data.
So… I just wanted to make you guys, like, aware of this. I don't know if this is gonna take off or anything, because it becomes an… the downside of this is that it becomes another thing to maintain that's doing the same thing, so…
If it's useful, great. You know, if it, you know, the idea is to… once… if this lands, this would be, like, like, the first
first,
first-class citizen try to process things, and then it falls back to the K probes if there is, like, a protocol that's not implemented, or things like that. That's the idea.
And that does, like, makes it much easier for, like, header parsing, like, so…
HTTP headers, for instance. It's easier like that. So I just wanted to mention it. I'm trying to bring this to the finish line, it's gonna take a while.
Cause… they're being busy with other things, but
Just in case, you know, it's relevant. I thought I would mention it, and the code is there, if you're curious.
Tyler 00:19:25 Gotcha. Yeah, okay, cool. Yeah, thanks for bringing that up. I think that's worth maybe also keeping in mind, yeah.
Okay, next up, Nikola, you wanted to discuss if there's anything outstanding on this? I don't,
I think there is…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:42 I don't think Sponge's on the call, I actually looked to see if he showed up, but…
Tyler 00:19:48 Mmm…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:49 Yeah.
Tyler 00:19:49 Yeah, I don't see him.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:50 There's, yeah.
Tyler 00:19:51 Yeah.
Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:55 Go ahead, yeah.
Yeah, I just wanted to know if people thought this was a good idea to do. I think the current state is okay. There's some issues with the unit tests that need to be fixed.
But I'm not opposed to doing this.
If we read the spec carefully, then seems like we should do this.
Tyler 00:20:19 Yeah, I think this is right. I don't, think this is right, but I think that that was a mistake in the description after reading through the PR. But yeah, I think that this is… this made sense to me.
Yeah, I think, like, this, I think, is a part of the specification. You're supposed to say this…
I think maybe technically this isn't correct, because we're actually running our own, but that's a whole other, topic. But yeah, I think this is really helpful, to, like.
filter out, as well, like, where a source of information comes from, and having something like this as an attribute would be really helpful to understand, like, this being the source. So, yeah, this made a lot of sense to me. I was really excited for it. I was…
Twice now, halfway through this, trying to review it,
just to make sure that this all made sense. This, I think, was the thing that stuck out to me as to, like.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:09 Yeah, we should… I don't know.
Tyler 00:21:11 hate all this. Yeah. But…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:13 We need them if Bela wants to still override, but I don't even know for how long or… much longer Baylor will be a separate build, but that's another.
Tyler 00:21:22 Oh, I see. I see, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:24 Or anybody else that uses OB, maybe… I know Mike is working on something.
Tyler 00:21:29 So then they would need to override.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:32 as well.
the… the SDK.
Tyler 00:21:36 Okay.
that actually helps under me understand where this needs to be. So, yeah, I think we'll… we just…
Are these… used those the problem?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:46 They're used for Bela. Bela just changes them.
Tyler 00:21:49 Well, yeah, yeah, but like…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:51 public.
Tyler 00:21:53 But, like, oh, okay, here it is.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:56 Yeah, the vendor is used there for SDK version, but now it should say OpenTelemetry, and then Bela, when vendors OB internally, set those to Bela.
Okay.
But… I don't know, we haven't discussed it internally, but I'm not… Here we go.
Tyler 00:22:12 No, that's right, I didn't… I didn't know these were used, I think they were used in the latter half, not the top half, and so…
Yeah, no, that makes sense. I think this looked great. I like the idea of adding this sort of telemetry on top, so… I'm in favor of this. Cool. I just haven't put my stamp on it yet.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:28 Yeah, I was mostly worried about the proposal to change the… the… everything to say the telemetry…
SDK language. That one, should stay the instrumented, but I think he mentioned that
He changed the spec.
Tyler 00:22:45 Because there's… because right now, the telemetry SDK language…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:50 Key is the language of the application itself.
I think. Without that, we don't know what the underlying language was.
And I think that's losing information.
Tyler 00:23:02 Yeah, I agree, I think that that's important to keep as well.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:06 And then… but I think Sven said… I forget whether… I think he mentioned on the Slack channel that he… his PR to, to update the spec got accepted.
I don't know if…
where, but I think he… he clarified the language was accepted, it should be the language of…
I don't know, he mentioned that I'll find the link.
Pellared 00:23:30 One who emits telemetry.
Tyler 00:23:34 Sorry, what?
Pellared 00:23:35 I think the language is right now that these are, like, the languages, etc, that emits the telemetry, not the thing that it is…
It is instrumenting.
but kind of, you know, the language which of the SDK, or automatic instrumentation, or stuff like that.
If I remember DPR correctly.
Tyler 00:23:54 Oh, it's the language of the telemetry SDK, is what this says?
Yeah. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:59 pasted in the notes the pull request he made for the spec.
Pellared 00:24:06 Yeah, I think the…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:24:06 the.
Pellared 00:24:07 Yes, I think that it clarifies a lot.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:24:12 Yeah, because he clarified that… I think… oh yeah, I see. You, you approved it.
Yeah, the observe entity, yeah.
Pellared 00:24:22 I'll start, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:24:23 Yes.
Florian Lehner 00:24:25 And, to keep the language of the process that is observed.
There is, auto semantic convention with process runtime now that can be used.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:24:35 Hmm…
Florian Lehner 00:24:39 So this would be done on a,
process level, I would try to say, just not on everything.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:24:49 And the process level, not the service level, yeah.
Tyler 00:24:52 Yeah, that makes sense.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:24:54 I think the intent was, like, we're maybe the first SDK that instruments different languages with the same tooling, right?
Usually, so I'm one-to-one mapping.
Tyler 00:25:04 Right.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:25:04 to language, right? And Obi's the first one that perhaps does this.
Florian Lehner 00:25:09 Yeah, we have similar issues, in particular, if a program is using the
foreign language interfaces, and they call from Go into C and from C into Python.
You have multiple languages, and yeah, we face the same, so what do you cite as the main language?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:25:31 Yeah.
Yeah.
Tyler 00:25:34 I feel like that one's even harder.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:25:36 Yeah.
Florian Lehner 00:25:37 Yeah, we attach the information on the frame level, so you can differentiate.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:25:41 Okay.
Tyler 00:25:42 Oh, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:25:42 That's pretty sweet.
Tyler 00:25:44 Huh. Yeah.
Cool. Alright, well, yeah, so we need reviews, reviews on this at the specification level, and reviews on this, here at our, our level. So, yeah, please, please take a look. Yeah, I'm excited to get these in.
This sounds good. In fact, I think I'd like… I don't see any opposition to this. I'm planning on approving this afterwards. I'm just gonna add this to the milestone for this release, I don't see why we couldn't get this in, unless there's…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:12 I agree.
Tyler 00:26:13 Yeah, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:14 I agree. So, let's good. I think it's just a unit test. I think integration tests passed, I think it's just unit tests are failing on some tests checked.
Tyler 00:26:23 Probably a manual string somewhere that needs to get updated, I'm guessing.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:28 Yeah, it's… the test is checking for the specific field, and now it's different, and it says there should be eBPF instrumentation, but it's just open telemetry, or something like that. I looked at it.
Tyler 00:26:40 Yep. Yeah, there we go. Okay.
So, actually, this is pretty easy to track down, so that's actually not that bad.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:46 Yeah, shouldn't be that. Okay. Yeah.
Tyler 00:26:50 Cool, Nicola, I think you also had the next thing. Oh yeah, service instance ID, and moving to UAID?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:26:55 Yeah, there's a big discussion on that issue there. Apparently, I was tagged in another thread by David Ashbel. Yeah, sorry, that's not working. They're moving to… sorry. And then I started looking into this, and…
And… and trying to find what happened, but this apparently got merged.
And… After… a while. So, if you look at the files changed, what the spec used to say
Was that you should use something Like, for example, my pod…
deployment for the service instance ID, but now it's a UUID5.
Tyler 00:27:38 Right, yep.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:27:39 So… Now, this… I mean, when we do this, it will be a break and change,
I think it's not a hard requirement, my understanding is that it's recommended, it's not actually enforced.
But there's moving parts here. I believe that the OpenTelemetry operators also use the exact same algorithm as OB. OB, we use the exact theirs to set the service instance ID.
And the operator still uses…
you know, pod name, namespace kind of thing. There is a… there's a rule.
So they haven't moved.
But I just wanted to bring it up that this is coming,
Yeah, and I don't know, man, we should probably, plan for updating. I don't know.
I know that some SDKs have updated. I believe Node.js and Java are already putting new UIDs.
But the operator overrides them.
With, resource attributes.
And I think maybe even the collector, CERN version, I'm not sure about the collector.
Yeah, I don't know what our stance should be on this. To me, the UOD is not useful, and that was my main complaint.
Because, when a user sees this in, let's say, a dashboard.
something like metric, it doesn't mean anything. It doesn't tell them
maybe in Kubernetes, you have a lot more of these attributes that maybe also be attached to the metric, but for something like a host, where it's a VM and you have
Just some UID, you have no idea which host this is, so… .
Tyler 00:29:39 Is there a service instance name field, though?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:45 I actually don't know. I don't think so.
Maybe?
Tyler 00:29:49 Hmm… Yeah, I also did notice this is experimental, so… well…
It was, at least. This is 2023, I think. I saw the merge date, so this might be…
Long past, but…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:04 Yeah.
Tyler 00:30:05 This is, oh, no, okay, it's resource, okay.
Stephen Lang 00:30:10 Well, there's… I mean, this host… dot name.
Tyler 00:30:13 Yeah, the service name…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:16 Yeah, so host.name, but host.name is not…
So what we do right now in OBI is a combination for various things, so open ports, host name, PID IDs.
To uniquely identify it, And hostname is not sufficient, because you may have multiple services on the same host.
Stephen Lang 00:30:36 I'm not saying it's unique.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:38 -
Stephen Lang 00:30:39 I'm just saying for, like, a human-readable identifier of a host or a node.
I think hosted name's common amongst… inside and outside of.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:50 Yeah. At least to identify.
Stephen Lang 00:30:54 a machine, but yeah, I mean, there's… I know, is it AKS, Azure, they keep…
The host name is not unique between clusters, so you could have two completely different clusters with the same host name.
So, yeah, it's not unique enough on its own.
Tyler 00:31:11 And I think that was the problem with the service instance ID being the container name, was that it wasn't unique enough, and you needed this, like.
Triplicate to be actually unique was the idea.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:23 Yeah.
Tyler 00:31:25 I mean, there is…
Yeah, it's not… service name isn't really the thing we're looking for, though, right? Because that's, like, it may be the container name, but it may also not be the container name.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:36 So… so…
I think it works if you understand that from an end-user perspective, they need to do an extra hop to find out what this
service is. So, we can use this unique identifier. There is issues with unique identifier and
multi-process services, like a Python, like, you imagine a green unicorn, and it starts 10 workers. Each one of them is a PID on its own, and each one will load the SDK, so each one will create its own UID.
I don't think that's a good idea, it just blows up cardinality.
So I don't know how that works. I think there's some language here where you should do in that case.
But I think they haven't decided on that.
Then… but assuming that you can do UID, uniquely identify the process, and
So, then what you do is you, in your metrics, you have this UUID, a Service Assistance ID, and then to find the actual meaningful name, you have to go and look at target info, and then…
see if that was a Kubernetes cluster, then you have the pod information.
If that was, like, a host, maybe you'll get the host name and server port, or PID, maybe, in there.
or if it was, like, a cloud vendor, maybe you'll find the cloud metadata in there. You need an extra hop, so it's not immediately usable as it was before.
in… And user dashboards.
Tyler 00:33:12 So, I think… I think, oh, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:18 Yeah, you see it, say, for applications running behind application server unicorn, we do not recommend using one identifier for all processes.
We've tried this before, and it…
I have customers screaming at us, because we didn't do the service business ID, but we added the PID of the underlying stuff, and people are like, why is my cardinality all of a sudden, like, tenfold everywhere?
Tyler 00:33:46 I think that this is also applicable here, where it says that the collector shouldn't be setting the service instance ID, because…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:51 of reasons, but I think it, like…
Tyler 00:33:54 The same reason we prob- yeah.
I, I think…
I think two things. One is, I think you've raised some pretty good points. This is development, also, it's not stable, so having those points documented in an issue would be really beneficial, I think, if they don't already exist in an issue. So I would say recommend, like, opening an issue to try to just document these, because…
If it's going to go stable, it needs to have
there's somebody saying that, like, I, you know, here's the workaround, or here's the, you know, at least it being documented, that this is not adequate for what you're trying to do.
And the other thing is, it may be a moot point, When entities come in?
Yes.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:34:39 Yeah. So…
Tyler 00:34:40 I… I think that I… I would… I'd put that there, and I imagine you might get a response from Josh Shorth saying, like.
yeah, this isn't great, but this also is just gonna go away, which may be a solution, right? Like, it may just be, like, this won't be a thing going forward, and we're actually gonna drop this, so… But yeah, I think opening an issue is definitely… I think you have valid concerns, and I think it's worth, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:02 Do you mean an opening issue with Obi, or opening an issue here?
Tyler 00:35:05 Oh, in,
I guess the Nancy Conventions, yeah, it would be… I would… that or this… yeah, because it's not in this specification anymore. I would say here, in the Nancy Conventions.
And yeah, I mean, you can definitely just say you're coming from Obi, here's Obi's… very OB-centric, like, issue is totally valid, to say, like, yeah.
You're useful.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:27 Yeah, because, I mean, the operator updated, I think collector, that's… we all use the same algorithm. I know that Mario did all the work to make sure they're identical, because you think about the collector is exporting
maybe logs, but OB wasn't exporting logs, and then if you wanted to jump from trace to a log, or from metric, they needed to match, so…
Tyler 00:35:49 Right.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:35:49 Defined for an existing service to get the logs.
the service instance ID must match, so…
I don't even know how that… how we do that. So, I mean, I guess Obi can generate it from now, and the collector and the operator can't touch it, because if we generate a UID and they override it, then it's… it's like… yeah.
Tyler 00:36:16 No, I think that's a really important concern. It's also, like.
we have no motivation to support this until that is the case. And even then, it's still not really valid from a user's perspective, right? So, like…
Is this a really good idea? I guess it's the.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:32 Yeah, yeah. But I already have customers complaining about this, for the… for the SDKs, because all of a sudden they lost the ability to debug which instance it is.
Because…
Tyler 00:36:45 Interesting.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:46 Service Assistant ID became unusable, so they upgraded a Java agent or something, and…
They're like, well, what just happened? Now, none of my dashboards, I can't tell which host it is.
Tyler 00:36:56 Yeah, be sure to include that user feedback in the issue. I mean, the whole… all of it, but, like, it's important that I think… you know, a lot of the time, OTL gets developed, and we think that we have users' expectations, but real users' feedback is actually.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:37:13 Way more valuable than our… what we think it'll be, yeah.
Yeah, so in our workaround, they actually made a workaround, so they actually override it with resource attributes. That was the fix. They just went, okay, well, you guys did this, we're gonna override it, so…
Tyler 00:37:30 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:37:31 Thanks, buddy. Okay.
Just wanted to bring it up, because I've been in discussions and looking at different threads, and yeah.
Tyler 00:37:41 Yeah, I think it's a valid issue. Steven, do you have something to say?
Stephen Lang 00:37:44 Yeah, I just wanted to ask a question, because I don't fully understand entities. I thought they were just, like, a group of attributes, almost like a symlink, to say, you know, it follows this entity, which includes this set of attributes.
Tyler 00:37:59 So I don't understand how…
Stephen Lang 00:38:01 using an entity, you know, would make this problem go away, because I thought it was just effectively pointing to the same underlying attributes, but are you saying that it's…
It's something else.
Tyler 00:38:12 No, I'm not. No, I think you have the right idea, but I think that this was added…
this specific, instance ID was added so that you could have these unique identifiers for the service, meaning the service name, service, all this stuff, right? But the uniqueness may not become as important if you are then grouping this in the resource with
An entity ID? The entity ID may be then…
Stephen Lang 00:38:37 The entity itself would have an ID.
Tyler 00:38:39 Yeah, and yeah, so that ref may be the thing that, like, can supersede this, and then we don't need to have this specific, like, uniqueness requirement at that point.
But…
I don't know if that's actually going to be the case. So, yeah. You may be 100% right, and people are not thinking about it that way, and it's just going to be another bag of attributes that are going to be included, and then, yeah, this is still very much an issue there, yeah.
But, yeah.
Stephen Lang 00:39:08 Thanks.
Tyler 00:39:09 Entities. Correct.
Have been the… the golden panacea that…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:39:13 We've been chasing for, like, 2 years now, so…
Tyler 00:39:16 We'll see.
Okay.
Moving on, Nikola, also talking about sharing service metadata through the protocols, mostly only Kubernetes?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:39:26 Yeah, so I have this outstanding issue, we talked about it in the planning. We'd like to make OB more useful for non-Kubernetes use cases, and…
Here, I obviously see a number of things that we kind of benefit today from in the Kubernetes world, but primarily, it's…
easy to find, the peer service names and things like that. So when we produce traces, or we produce, just metrics, just saying what connects to what, like the service graph metrics.
It's…
it's kind of cool, because we… we can consult the Kubernetes metadata and say, oh, what was this IP? And this IP tells us, oh, that's this pod, or this service.
It's kind of very useful, right?
So, even without traces, you have full service graph, and it's meaningful.
However, that goes away if you're on a host. Let's say you have two separate machines, let's imagine two VMs in the cloud, and you have put OB on each, and you want to collect the same information, produce… If this was, like, say you had
traces, then they'll get correlated, so even if the information is not correct, with the trace context propagation, you'll show them connected, so… so be it, but you know exactly what happened.
So, to support
Non-trace mode, like service graph metrics or span metrics, to be service graph metrics, and primarily to be accurate with the names of the other service.
I thought of this idea, and I've created the prototype, I just wanted to bring it up here. So, piggybacking on our trace header injection, I wanna…
provide from one service to another, metadata to say, hey, I'm calling you, but this is my name, actually, and this would be the hotel, service name and namespace encoded, so that… it's like baggage, but a little bit more compact, so that I can actually pass you
A little bit of context about myself.
And then on the receiving side, using the large buffers and the parsing of the headers, I can extract that information and populate the peer.
And same thing on a client requests, they're receiving data back, they want to know that.
the server name, so they can produce who they called. On the response, I'm injecting the same metadata information back.
So that, even without tracing, you get, like, full
Correlation between these two things.
So this obviously does not require any…
external services to collect this. That's one of the, things that the old eBTF networking project had, which is they would push the metadata up to some service that would be collecting all this information, and they could resolve the names between the network devices.
or the network, services, but we don't have that, so I… just for the purpose of application observability, I'm thinking of
Or APM in general, to produce
To kind of pass this context back and forth.
On the request.
I've looked into it, I spoke to Rafael about this, to also use maybe the TCP options.
that seems a bit more challenging, it's more restricted in byte sizes, how much I can push through.
So, I haven't implemented that, but…
I want to kind of gauge the opinion about this, and…
Also, another question I have is, like, what header name do I use? I just made up one, OB namespace or something, to pass through.
I looked at hotel baggage, but then…
the W3C baggage, but then I don't like the way it's encoded, because it specifies… it's too much strings, I guess. It's… it's the end of it, because it says service.name equals, and then comma, service.namespace equals, and…
I mean, sounds a bit… Much.
But maybe I can use baggage, and then come up with something, like, a special key…
Tyler 00:43:41 Yeah, I think you'd have to… I mean, I think baggage is probably…
the place I'd start, just because, like, people are gonna be more familiar with it, and, like, already have parsing functionality there.
But this is something that, like, other downstream hotel services, they're also gonna need to understand, right?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:01 on…
I mean, yes and no. I mean, this would only be if you have Obi on the other side to extract this information.
So…
Tyler 00:44:10 Well, if it's just Obi, then I don't…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:12 Yeah.
Tyler 00:44:13 I don't think it really matters.
I know.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:15 I agree.
Tyler 00:44:16 It's kind of up to us, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:17 Yeah, I just wanted something compacted, small, so that…
Tyler 00:44:23 Yeah, I see Florin has his hand raised.
Florian Lehner 00:44:25 Isn't this approach limited to unencrypted traffic?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:30 Yeah. So, encrypted traffic I would use, have used TCP options.
But TCP officers will… which we already do for encrypted traffic, But… Those are also…
victims of proxies, because packets get replayed. So you'll get to the proxy, or some sort of gateway, and the gateway will replay the request downstream, and then you're… you're done.
There's no perfect solution there.
The other solution would be to export this data to a, like, a central service, but even that is questionable, right? If I'm going through a proxy or a gateway, I don't know the downstream IP. So, what I advertise as my IP address, it's not going to pass through.
So yeah, right now it's limited to unencrypted traffic.
Florian Lehner 00:45:22 I think in the terms of hotel ecosystem, Hmm.
Resource attributes should be more… leverage to… for this purpose, because, yes, Auto will not be able to
To have the full picture with every request and provide information.
But then in the backend, where all the resource attributes merge together, you should…
be able to get this picture, regardless if traffic is encrypted, they are using QUIC, which you cannot handle, or stuff like this, and…
I think that's also the, the approach that,
the people from Datadoc are approaching with the SDKs, where they're asking the SDK, hey, if you're an SDK, publish your, publish your, resource attributes so they can be attached to, information, like, from OB profiles and stuff like this.
Except for this… for this case where you don't have Kubernetes or stuff like this.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:46:23 Yeah, so the resource attributes, we already handled that in a way, because OB works at a low, like, I mean, low level, essentially, so…
We know there is actually resilientation because we parsed it from the environment variables. So it's passed through OTEL. I mean, maybe the clarity config breaks that, and it will, right, if a service is configured through the clarity config, we won't be able to read them anymore.
But if it's passed to environment variables, we read that.
So, but the service itself, we kind of know for that service what the resource attributes were, and what's the service name and namespace.
And it would be nice if, you know, they get advertised through this data or proposal. But the problem is, we send…
A request to another service.
And then…
So what OB does right now, it can produce service graph metrics, which a lot of people like.
To create the graphs and everything without sending traces.
Traces are expensive, you have to sample 100% of the time, and to produce accurate this. So, OB produces the service graph metrics straight up.
And…
to have the correct name on the other side, you need to say something. So you have a client, you have a server, so what's the server? Well, I don't know, because, I mean, or which namespace it is, so we just…
We have an IP address, we talk to the remote guy, but they may have encoded something in the host.
But it may not be what the service name is configured on the target, so then you end up with, sort of, disconnect that you're talking to.
service A, but internally, somebody configured it through namespace and name to be something else.
So I'm looking for a way to communicate this information between… on the protocols so that they can actually correlate themselves correctly.
So,
So it's orthogonal to that, I guess. If the resource attributes and what data is proposing will be great, so we can read them.
And they advertise to eBPF.
Especially with declarative config.
True.
Tyler 00:48:45 Yeah, I mean…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:48:45 I'll just make up… is it okay if I make up a header or something?
Tyler 00:48:50 Yeah, and I think this is a great idea for a prototype.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:48:53 Yeah.
Tyler 00:48:55 But yeah, I think that sounds great. I think you should definitely do that. And then…
Yeah, let's iterate. Let's see if…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:49:01 consider it, yeah.
Tyler 00:49:02 It's a horrible idea, we can always pull it out, like, it's not the end.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:49:04 Yeah. Right? Yeah. Yeah. Yeah.
Tyler 00:49:08 But yeah, I would do that. I think that that sounds like a great way to start. And then you can demo it, start showing the proof of concept as well, and I… I don't see why it's gonna be a problem. I think it actually will work fine, so I would just go that way. But yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:49:21 Yeah, I may go for the first one PR for the HTTP options, and then see if I want to proceed with the TCP options. I'm living with the number of bytes, and that's what irks me the most, and we already need something for the trace parent, so…
Yeah. How many packets will the services exchange? I may kind of push multiple parts of this, you know, if they're sending more packets, then I can just…
Keeping on pushing parts of it, and eventually all of it makes it on the other side.
But I can rely on luck.
Tcp options are 40 bytes total.
And… I mean, maybe the TCP packet already has some, so then it's less than 40, and then…
Yeah, it becomes…
Tyler 00:50:04 40 bytes for a full service definition is pretty impressive.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:06 Yes.
Tyler 00:50:07 So, alright.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:08 Yeah.
Well, you think it might be enough? I don't know, maybe.
Tyler 00:50:14 I… I think in…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:15 They call their service Obi, yeah.
Yeah, but if they call it product.
Yeah. Product catalog or something, right? Product catalog in the.
Tyler 00:50:25 By loquacious service, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:27 I mean, thinking OpenTelemetry Demo, right? So the name is, like, OpenTelemetry Demo on the namespace, and then you have product catalog service, and then all of a sudden…
Tyler 00:50:39 Morty bytes are easy to… Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:42 To re… to use up.
Tyler 00:50:44 Man, okay. Yeah, that's a tough one. I think… I think starting the way you're talking about is a great idea, so let's do there. And then it also shows, like, if it is really valuable for, like, the HTTP, we can… we can tackle the other stuff next, so, yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:57 Yeah.
Tyler 00:50:59 Sounds good.
Stephen Lang 00:51:00 Nick Lowe.
Tyler 00:51:01 Book.
Stephen Lang 00:51:01 Maybe you need a lossless compression algorithm.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:05 Yeah, I was talking about that, do you have a proposal? Do you have a suggestion of, like, a failure and our bouncing ideas? And everything we looked at, too, like, any of the standard ones have this preamble, whatever, I need somebody.
Stephen Lang 00:51:19 Anyway.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:20 And then we're thinking maybe we can… I mean, service names, they use a subset, so if we assume lowercase, and then we assume that there will be no special characters, or maybe just dash and dot, then we can kind of pack it.
Right? You can sort of do, like, a cheaper encoding.
Stephen Lang 00:51:38 There must be one. It's worth researching.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:40 And I think we only need 5 bits or something to represent all characters possible that people typically use, and then…
Yeah, I think so. I think it's doable.
Yeah, you save some bits, I think, if you do, like, a more tighter packing. I think it's possible.
So maybe we extend that to, to more…
I'll see. Yeah, I think I like the TCP idea. I know… I'm not sure how much in practice… it will work in some cases, but as soon as people do things like
Gateways, or anything like that, where they…
So, typical in various organizations. From a service, you don't call directly something else, you call through a gateway that resolves into which one you should call downstream, and
people put, like… and Kubernetes is all handled by the Kubernetes environment, which is kind of nice, but outside of Kubernetes, you have to do everything, like…
I don't know.
Use those proxies, gateways to… to make sure you have,
ability to update the backend service through another version, and just rewrite of routes in Nginx or another one. So it's very typical that the TCP packet doesn't actually make it all the way to the other side.
So… I didn't think it was gonna be very practically useful. Kind of cool packet on project, but maybe…
Very usable in practice.
Tyler 00:53:12 Yeah, I think… I think starting with the HTTP approach sounds…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:16 Print the header.
Tyler 00:53:18 Okay.
Cool, next up, I wanted to ask about, the next release.
We've got a lot of, great stuff.
I think it's only been, like, 2 weeks, but I think that there's a lot of really good stuff.
To release here, one of them is the embedding of the Java agent I'm pretty excited about. That'll clean up a lot of the install for standalone binaries.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:43 Which, yeah, I think is great. We also.
Tyler 00:53:48 Oh, yeah, we're, the distribution of the source. Sorry, I'm blanking right now. The source code's gonna be really helpful, and then unblocking the work on getting us included in the, collector distribution. So…
Yeah, I think there's a lot of really good things I'd love to…
get released out here. I don't know if there are…
Specifically, anything, like, we just added, this PR to fix the telemetry. Anything else that people are really wanting to get into this next release that we want to hold up on?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:22 I think it was good for my side.
Tyler 00:54:24 Okay.
I do think that, all of these, except for this, we could move to the next, milestone.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:54:32 Yeah. Just cause they've…
Tyler 00:54:34 continually been moving along. I was looking at trying to get a few of these done, but I'd rather, I think, just work on them after the next release, so…
Yeah, I'm gonna bump these to the next milestone.
And, if folks are thinking about a particular thing, go ahead and add it here. Otherwise, I'm gonna try to get a release PR out tomorrow, I'm guessing? Maybe later on today, depending on how fast this gets merged. But yeah, I think it, keeping the cadence going and then moving forward would be great, so…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:07 Awesome.
Tyler 00:55:09 Okay, Rafael, got 6 minutes, you wanna take us home with talking about large buffers?
Rafael Roquetto 00:55:15 Yeah, yeah. So, it would be less than that. This week is, Hackathon week at Grafana. So, you guys saw I've been raising some PRs, with large buffers,
The idea is just to optimize them a little bit. Hopefully… I mean, this is already possible, but we can do… we can do… use them even more for doing more, like, user space processing, because it's much easier to
parse headers, all the kind of stuff that, you know, Mattia and Erod… And Giuseppe have been doing.
So… yeah, I just want to say I've been working on that this week, just for the… for the Grafana Hackathon, and one thing, like, we discussed on the channel, like, on the Leeds channel, and… but just to remember.
what I would like to do is to change the buffer size settings to be, instead of being per buffer.
So every time you see in a buffer, it's at most that size, it's gonna be…
per request. So, you get a request, and you have, let's say, buffer size of 100, it means that for that request, I'm gonna send at most 100 bytes of large buffers in. And I would like to see, do you guys agree with that? Does that, make sense?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:31 Yep.
Mattia Meleleo 00:56:32 Yeah, yeah, I think it makes sense. Like, like I wrote in the channel, I think it should only be consistent with the other buffers. Like, if we do this for HTTP, it should be the same for
Or any other protocol?
Rafael Roquetto 00:56:46 Yeah, yeah, yeah, I'll do that. I'll do that. So, this is just to avoid having holes in the… when you're sending things to user space, and then also limiting, like, someone has a really large request, you don't want to send 10GB to user space, so you… it's, like, cut off. So, that's what I want to do by the end of the week. Fingers crossed I'll make it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:57:07 Cool.
Yeah, I also, like, want to turn them on by default. So, we had an idea here, and I'm… Patia, I especially want your opinion on if this is going to work.
But…
I don't know if I mentioned it earlier. I've talked about this before to run people, I forget. So, the idea is that we detect
just like the SDK instrumentation, that there is an interesting
Like, process that's doing this, and then we enable them for the test that bid.
Let's kind of another map.
So, let's say it makes it to user space without the large buffers, we see that it's, like, S3 in one of the headers, with whatever little bytes we have, and then we're like, oh, okay, this bid should do large buffers. And then…
we… we add an extra check, a large buffer, so instead of being a constant, we actually consult the map, say, should I be tracking?
This bid with large buffers, and then turn it on.
Mattia Meleleo 00:58:08 Wouldn't the user still have the power to say, I want large buffers here, or… I don't know.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:58:16 Yeah.
Yeah, but we can have an auto mode, where, kind of, like, see an interesting…
Mattia Meleleo 00:58:21 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:58:22 we see an interesting payload, and we're like, oh, okay, this process is talking to OpenAI. Okay, so let's enable large buffers for this guy.
So it could be low overhead for everything else, you have some large… some really high-volume service, you don't want to send everything, or somebody's sending, like, gigabytes of data, whatever. We don't want to capture that, but then…
We'd see something interesting based on the small buffers, and then we're like, okay, now it's… now it's a good opportunity to…
Make it get more.
Mattia Meleleo 00:58:53 Yeah, I think it's interesting, follow-up question. Should this auto mode be configurable? For example, what if a user wants, auto mode for AI-related stuff, but not,
I don't know if any… yeah, like, an interesting protocol, like Mongo, for example.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:15 Yeah, that's a good question. Yeah, I don't know the answer, but I'm looking at how to
Like, make it on by default without the impact.
to the end user, for performance. And I think it's doable. I think we'll come up with some good heuristics, too.
to kind of say, it will work out of the box, you don't have to touch it. I like that thing about Obi, that you have very little to configure. It just works out of the box, and I think we can continue with that.
Mattia Meleleo 00:59:42 Yeah, that would be very nice for, like, just install and see good stuff without a lot of overhead.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:48 Yeah, without configuring or worrying the customer of touching stuff, so… I think it's doable. There's some heuristics we can do, like, known…
Like, if you're talking to AWS, we probably have your DNS, we know it's AWS, and so then turn on large buffers, you're talking to OpenAI, turn them on, and…
And then…
Mattia Meleleo 01:00:11 I think that 90% of use cases, you can just do that with headers.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:17 Yeah, I think so too, yeah. And I think… I think it was doable, because I think in the first 256 bytes, there will be enough of the headers that we can probably see.
Tyler 01:00:29 Yeah, I think this is cool. Okay, we are at time. I want to be respectful of everyone's time, so yeah, good talk, everyone. There's obviously a lot more to do, so, yeah, good talking with you. I'll see y'all in a week's time.
Rafael Roquetto 01:00:41 Correct, bye.
