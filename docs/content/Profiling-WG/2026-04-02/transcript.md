SIG: Profiling WG
Date: 2026-04-02
Duration: 66 minutes
Zoom Recording URL: https://zoom.us/rec/share/YfDSvI63mvS9EwRFS6YrZ1kEwI2-tOm81fKV7SWVidgFmTyd42cor2AHgGh5aw.evzQ2dTVJfsSKuCe
============================================================

## Zoom Recording Transcript

Tigran Najaryan 00:01:02 Hello, everyone.
Florian Lehner 00:01:05 Blue.
Nayef Ghattas 00:01:06 Hello.
Frederic Branczyk 00:01:13 Hello, hello?
Felix Geisendörfer 00:03:41 We're 3 minutes in, so may as well get started.
First of all, thanks everybody for all the awesome work leading up to KubeCon and the Profiling Alpha Lounge. It's really awesome to see that come together.
And yeah, for those of you who weren't there, the talk went well, the feedback went well. Also, online, I saw lots of good feedback on the launch, so… Hopefully, we will soon make a lot of people very happy and help them solve their computer problems with OpenTelemetry profiling.
And, I guess, yeah, today we're gonna go back to our regular rhythm of reviewing action items and starting the course, so we can hopefully soon be headed towards a better level, and also start to work on simple occasion, and figuring out how to get that piece in place as well.
Yeah, if you haven't already, and you want to add something to today's agenda, please put it in the doc. If not, I'm going to start us going over the action items. I'll share my screen.
Okay, can you all see the Google Doc?
Okay, so I think Alexi's not here, so I'm gonna put Cease as not here.
Maybe he'll come back later.
I have not made progress on the… discussion… I had some discussions at KubeCon with Damien and Florian and a few others about this, but I haven't opened an issue yet, and on, probably Tigran or somebody who's… since he's here, whose mind I want to pick on this as well, like, basically figuring out how to do either protocol negotiation or at least protocol advertisement to give maybe a chance to people who want to run the profiling alpha and not get broken all the time. But yeah, I'm going to open an issue there, but I haven't had a chance yet.
Tigran Najaryan 00:05:53 Pardon me there on that issue, let's have a discussion. This has came up a few times in the past.
And we typically said no, because we didn't want people to have version-specific code written.
And instead wanted people to look at the specific capabilities based on the presence of the fields.
I understand that with Alpha, where you may make breaking changes, it's not maybe necessarily the best way to do it.
So… I guess let's have that discussion. When you open it, include your reasoning and what you want to do about it, and we can look into that.
Felix Geisendörfer 00:06:34 Will do, and thanks, that's a good piece of context.
Christos Kalkanis 00:06:37 Can I add something here? Because we had, I think, one or two discussions in the SICK about this before, maybe Tigran wasn't present. I think, yeah, you weren't present, Tigran.
I think the reasoning behind this is not that we would like implementers to support multiple versions. Obviously, for an alpha, like, within Elastic, we're not going to do that. What we want is to support only one version of the protocol, typically the latest.
But have a way to give people a fast way to reject incoming payloads, because then they can just look at the version and say, okay, I clearly don't support this, so I will reject you at this point. And then, if that check passes.
there are going to be checks on the actual payload, right, to determine capabilities, and those checks need to be there regardless. Like, we won't use the versioning scheme to abort those checks. For example, yeah, if the version is okay.
Those checks will still take place.
But if the version is clearly incompatible, there's no reason to pay the cost of actually going deeper into the payload and examining if, you know, that compatibility is there.
Tigran Najaryan 00:07:40 Welcome.
the logic you're describing applies only to unstable protocols. As soon as it is stable, you don't want that situation, ever, right? So, because any evolution of the protocol, once it is stable, is supposed to be backward compatible.
So, essentially, you're looking for a mechanism that is for the unstable situation. But you carry over that.
once you become stable, so if it is the version number.
That version number keeps changing when you are stable, and people may accidentally begin depending on it, which can cause unintended consequences of people rejecting something that they are not supposed to reject.
So that is the reasoning why we didn't want the version number to be available at all, for people to make that mistake of reading it and making decisions based on that when they shouldn't be making a decision. But for Unstable, we haven't, I guess, had the option of doing something about it, so… perhaps… I guess we can make it a possibility, but once you go stable, we remove that, right? So it's only for profiles, and only while it is unstable, something like that maybe is possible. So let's… let's have the issue, let's have the discussion with others as well, and we'll see what is possible there.
Felix Geisendörfer 00:08:58 Yeah, and I want to add two things. A, what Krista said would be the lowest common denominator of what I think everybody in the SIC would like. Like, if something is clearly incompatible, there should be an error message rather than, like, weird failure and, like, maybe corrupted data showing up.
I think some of us, myself included here, would be interested also in backends being able to support older versions by just, like, knowing what it is, because then it's just a backend complexity thing, like, a backend doesn't have to do that, but they could do it during alpha.
And last but not least, I want to comment on sequencing, saying, like, once you're stable, you're never going to change.
the main feedback that people had on, actually, the Profoning Alpha launch on Hacker News and on X and a few places where I posted was concerns around, performance overhead with OpenTelemetry and protocol overhead. So at some point, OpenTelemetry will definitely want to do, like, a V2 where the existing signals.
Tigran Najaryan 00:09:53 Yes.
Totally. I didn't say you never change. I said the stable protocol doesn't change in a way that breaks it.
Now, you may end up having a completely new version 2, which is incompatible, but that's a deliberate step.
Before you go there, there is often… evolution happens within that stable version 1, you add fields in a way that we have the definition, what is allowed, what is not allowed there, and that is backwards compatible. So, yes, it is also a possibility to have a version 2 at some point in the future, and that can be reflected in the payload somehow, to be detectable.
Typically, like, if it's the… The HTTP version, it's in the URL already. You have V1 in the URL right now, so you'll have V2 in that case. But we haven't done that yet with any of the signals, and I guess it's a possibility sometime in the future.
But before you get there, there is also a minor revolution happening, which is backward compatible.
Felix Geisendörfer 00:10:59 Yeah, that makes complete sense. I'm just thinking that once you decide to make that leap towards a V2, it's going to become very compelling to have clients that can speak V2, but also still B1, so it makes the deployment story easier, and then the client needs to figure out, like, hey, try sending B2. If I get an error, maybe I fall back to B1, but there needs to be some mechanism to facilitate that.
Tigran Najaryan 00:11:18 Yeah, yeah. We will have to solve that for all of the signals, not just.
Felix Geisendörfer 00:11:21 Yeah, profile.
Tigran Najaryan 00:11:22 So we'll have to find a consistent mechanism to do that. For profiling, we can have… we can have a specific mechanism because it's the only unstable signal at the moment, so we can have something that just use… is just used by profiling for now.
Felix Geisendörfer 00:11:39 That's actually good to hear, because that makes it much more palatable for me to open an issue and try to reach consensus that the whole thing with all signals would be much harder.
Yeah, and just FYI, what we're thinking there is potentially something like, gRPC metadata or HTP headers that indicate which alpha version exactly, like OTLP version we're sending.
Tigran Najaryan 00:11:59 Yeah, and we can have that, and we can have a note that once we go stable, we remove that header, let's say, for example.
Felix Geisendörfer 00:12:06 Yeah, that's all.
Tigran Najaryan 00:12:07 Of course not, yeah.
Felix Geisendörfer 00:12:10 Yeah, I'm gonna try to capture your other things.
Nayef Ghattas 00:12:21 We could even call it out in the header key, like, profiling unstable version, or something like that.
Tigran Najaryan 00:12:28 Exactly, you could just include the word unstable, literally, in the value of the field.
Felix Geisendörfer 00:12:47 Okay, I didn't capture all the color here. If somebody wants to edit and add more color, please do, but, I guess the meeting's also recorded.
Okay, thanks, Tigran, that's gonna be… that's really good context for, like.
giving me idea of how I should scope the thing I'm gonna propose. That's great, thank you.
Christos has specification PR, please review, has this since landed?
Christos Kalkanis 00:13:15 He has some approvals already, I think Tigran approved both of them. There are currently two open pull requests in specification related to profiles, yes, so Tigran approved both of them. I think we need one more approval from that group of maintainers, spec. I think Tigran asked Josh to take a look.
This is, yeah, mostly as… I actually added an additional point later, because I forgot about the action items, so we can skip it later. But essentially, a reminder to people to take a look. I addressed, I think, all feedback that currently exists, but yeah, if you haven't reviewed those and would be interested in looking at them, just please go ahead.
Tigran Najaryan 00:13:51 I just… everybody, all spec approvers, to take a look, so hopefully we'll get one more soon.
Felix Geisendörfer 00:14:03 Yeah, I might take another look. It seems like maybe a bunch of changes happened since I added my review.
Cool. Any, any other comments on this?
Going once, going twice… And number 3 takes us to Data Model PR.
Also still awaiting review, so I have not refused this one yet.
Christos Kalkanis 00:14:32 Yeah, so I renamed it. Tigran made a comment here, that the data model is not really an accurate term to use. What we have now, it's essentially the protobath specification, so I renamed it to Data Format.
Hopefully, hopefully that's better. And then, you know, everything we just discussed applies to this one, so it has some approvals already. Felix, yeah, if you haven't taken a look, maybe you'd like to take a look.
Felix Geisendörfer 00:15:08 Okay, anybody have, thoughts on… on this one?
Do we… maybe I have one quick one. I assume that this contains, yeah, a lot of duplication with what we have in the protobuf, which implies anytime we change the protobuf, we need to remember updating this. Do we have, like, a good list of, like, hey, any protobuf change, we need to go do these things?
Christos Kalkanis 00:15:32 And we don't… I don't know, should we… write it down somewhere. Like, I have an open pull request in the repo as well, to make backwards changes to the protobath, because I changed some things in the data format, description. Also, you know, Alexi left some good comments, so I took his step back into account, Tigran made some comments, and those are not yet reflected in the actual proto.
Bye.
So, changes can happen in both directions, right? So, we change the proto, we need to change the data format document. If we change the data format document in a way that affects the proto, we have to go back and change the proto.
Or maybe we remove most of the comments from the proto and have them in the data format. Takman, I don't know how you would feel about that.
It feels a bit, redundant.
To actually have those extensive descriptions in both places.
Tigran Najaryan 00:16:25 It is redundant. What… what is the purpose of having this document? I assume it contains… Some descriptions that are not present in the product file.
Christos Kalkanis 00:16:37 Yeah, it's…
Tigran Najaryan 00:16:37 case.
Christos Kalkanis 00:16:38 It's… I actually elaborate a bit more, I give examples. I… it's easier to hyperlink, right? You can add links, you can add diagrams if you want, like, proper diagrams, not ASCII diagrams.
It just reads as a technical document, right? Like, the protofile is a protobuf specification, it's not meant to be read as a technical document.
Tigran Najaryan 00:17:02 How do you feel about including things that you wanted to be extra, like the diagrams and all that stuff, but avoiding including things that are easily readable in the proto and just linking to the appropriate lines then? Like, the fields themselves, the list of the fields?
That is the most redundant part, and I don't think it necessarily adds a lot of value to this document.
The diagrams are, the other descriptions are, and then for the specific field, the meaning of the particular field, you can go and just read the product, and you can link to the specific line in the proto, so it's not difficult to follow that.
Christos Kalkanis 00:17:41 Yeah, you can do that.
Tigran Najaryan 00:17:44 So that you don't necessarily have to have a detailed description of each message with all of the fields.
Christos Kalkanis 00:17:51 like, for me, so if we do that, then it's… I guess it's a question of, like, what would you prefer to read when you try to understand the proto? Just an ASCII file, which is the proto, right? Where it's, like, it's not very easy to read, right? You can't have proper tables in there.
instead of this, and this is extensively hyperlinked. It's actually a document that you can… it helps you, right, understand the protocol in a better way, because you can cross-reference things very easily, the tables are visual instead of implied, you can have diagrams and so on.
But… and then… So I can throw out all the tables, for example, because the meat of the product is in those tables, in the technical data form and document. And then I can add links to the proto.
Yeah, I'm not sure, I don't know. I actually… and I think there's precedence for this, actually. I didn't just invent it myself, right? The concept of taking bits from the protocol and putting them in a technical specification document like this. I think the other protocols or signals are doing something similar, some of them.
Tigran Najaryan 00:19:00 Yes, but I don't think they go into the full details of what is contained in the product, as far as I remember.
And they are the, like I said, the data model document, so the distinction is important. They try to explain the logical nature of the concepts, rather than going into the specifics of the protograph format.
Whereas in this case, you… you are tightly coupled to the description of the… what the protobufs are, and that results in… More of that feeling of being… redundant there. We have another precedent here in Autel with the OPUMP protocol, where we have a specification and a protobuf, and specification has that redundancy in a very similar way, where it explains the fields.
The difference there, though, is it's in the same repository, and it's easier to, when you make changes, make them at the same time.
in both.
Christos Kalkanis 00:20:01 media.
Tigran Najaryan 00:20:01 And keep them in sync, whereas these are two different repositories, so it's going to be a bit more challenging and possibly easier to forget, so I'm… I'm a bit on the fence on this one. I'm not sure what's the.
Christos Kalkanis 00:20:15 Yes, sir, what… Why don't we… then I think that one option is to remove most of the text from the proto file, right, and leave the proto be the protobab specification, and then link from the proto to this technical document here, where we have more freedom, essentially, to present information in a better way, because we can do it visually.
We can do it with hyperlinks, and so on.
Tigran Najaryan 00:20:39 I don't like that, because the texts in Proto, once you generate the bindings, they become comments.
Typically, in whatever language you generate, and they are very useful when you work with the messages and fields, so I would prefer to have them.
So, when you say that you don't… you want to have these mermaid diagrams and all that stuff.
I guess you could have the ASCII versions of those as well, and you do have for many of those already, right?
Christos Kalkanis 00:21:15 Yeah, the mermaid… the mermaid icon is a direct… it's essentially this, right? Yeah, it's…
Felix Geisendörfer 00:21:19 Yeah.
My personal preference, just looking at it, it would be the mermaid diagram is kind of awkward in ASCII. I think there's not much loss to remove it from the proto file. I would move that over. I do like having, actually, the, like, comments on the fields here, because as we design this, this is the thing that we work on, and that we have to reason about.
Tigran Najaryan 00:21:38 Yeah.
Felix Geisendörfer 00:21:39 And so I would probably just, like, remove these tables, and, like, basically, if there's nothing to say about a message.
then just… yeah, I don't think we need each message described, it's more like concepts that need to be described, how messages interact with each other. So, I like the high-level diagram, I like this text, I like the examples, down here, this is great, but, like, the repeating all the fields and comments that can get out of sync really easily, I would remove. And I would keep them actually also in the Proto as my preference.
Tigran Najaryan 00:22:11 Yeah, essentially have this as a sort of an overview, which then, if you need more details, you go and read the product file, essentially.
Christos Kalkanis 00:22:23 Okay, makes sense. So I have an open public host already in the, Proto repository, so I guess I can… amended, so I can move some more information from this document that wasn't sourced from the proto, put it there, and then I can Chains, remove all the tables, essentially.
Felix Geisendörfer 00:22:47 Yep.
Tigran Najaryan 00:22:49 Yeah, I think so.
Christos Kalkanis 00:22:51 Okay, sounds good.
Felix Geisendörfer 00:23:02 But I get what you were trying to do, Chris, is, like, having… it's kind of nice for, like, somebody who, like, implemented to have, like, a single document that they need to read without cross-references, but I think in this case, we need to strike a balance between, like, complexity for maintainers to keep stuff in sync, and.
Christos Kalkanis 00:23:16 No, that's fine. Yeah, it doesn't make sense to have all this information in two places. It's essentially embedded.
on a loss.
Felix Geisendörfer 00:23:23 If we could automate it, but then you're gonna, like, maintain some automation script and, like, Python.
Christos Kalkanis 00:23:28 Yeah, he's.
Felix Geisendörfer 00:23:28 And, you know…
Christos Kalkanis 00:23:30 No, it's not worth doing for now. Essentially, we don't have a lot more to say.
Like, if I… if I expanded on its field with, let's say, half a paragraph additional information, maybe it would make sense, and that was something we didn't want to have in the product, but currently, as things stand, that's not the case.
Felix Geisendörfer 00:23:47 Okay, cool, awesome.
That's good. Alexi's probably still not here…
Tigran Najaryan 00:24:02 For the question he's asking about OTEPs, we don't remove OTEPs, but they can become outdated.
In this case, it's, I guess, very significantly outdated. We can add a notice at the top of the OCAP to make sure that people Understand that it is no longer relevant.
And that should probably do it. Should be enough, I think.
Felix Geisendörfer 00:24:32 Okay.
Sounds good.
Tigran Najaryan 00:24:39 Make a… add a link to whatever is the latest version, and then say this is obsolete.
Just, like, typically, what the RFCs do, right?
Felix Geisendörfer 00:24:50 Sounds good, cool, thank you.
Then I think we are ready to jump into the, action items, sorry, into the, normal agenda. And I would guess Ivo is gonna start first with body size limitations and profiles. Take it away.
Ivo Anjo 00:25:12 Yes, so, this was something that came up in the hotel specification SIG, that they're planning on maybe documenting some recommended limits for file sizes, especially the second PR is on the collector side, and they're thinking of maybe recommending up to 4MB in gRPC, and up to 20 in HTTP, and even during that meeting, someone kind of raised, oh, but is that okay with profiling? So, yeah, this is me kind of… I think, passing on the message of, like, maybe we should comment here that maybe that's not great for profiling?
And what we want to suggest instead, something like that?
Tigran Najaryan 00:25:57 By the way, as far as I know, the limits are already there in the collector.
They are not… this is… they discovered that the limits are missing… In the SDK implementations.
But the collector already has those limits. And as far as I know, 4MB is the default for gRPC, and that default is what is present today in the collector.
So, yes, I think it is a concern for profiling, especially the 4MB limit for the gRPC version.
For the request size. The first one they opened was for the responses, in particular, for the SDKs, that was important. Responses, I guess you don't care, it's fine, but the request size, which is the second PR, is going to be important for you, and maybe you need to look for higher defaults for profiling in particular.
Christos Kalkanis 00:26:48 Thing is, it's uncompressed payload, right? Not compressed.
Tigran Najaryan 00:26:51 Both. The way that it is phrased, it says both the compressed and uncompressed sizes are limited to same value.
to… it's configurable, but the defaults need to be sensible, right? So, something that makes most of the cases work properly, and I'm guessing 4MB is not going to be enough for profiles, for the request size, uncompressed request size.
Felix Geisendörfer 00:27:17 But, wait, can I… That makes… doesn't make sense, to have two limits, when one limit is always going to be the one that you hit. Like, you're always going to hit the uncompressed limit. Why have a limit on the compressed?
Tigran Najaryan 00:27:29 Sure, I guess you could have separate limits. The idea here is that, yes, you… I guess when you receive a compressed request, it's easy to verify whether the compressed size already is over the limit, and stop even… don't even try to decompress.
But you still want to have the limits on the compressed size as well, anyway, right? So, you do need to check twice.
The question is then, do you check against the same limit, or no? It's simpler to just say that, okay, just check against the same limit and be done with it, so that you don't have to then kind of try to guess what the ratio of the default values is going to be.
For the compressed and uncompressed size. It, essentially, it's a try to protect the recipient. That's the idea.
Felix Geisendörfer 00:28:18 Yeah, I just don't think it's very efficient protection, because if you assume, like, a compression ratio of 2 or 3x, and you have payloads from 1 to 4 megabytes, 0 to 4 in a normal distribution, then, like, 75% of them are going to look fine uncompressed, but then… compressed, but then are going to go over your limit when you uncompress, so…
Tigran Najaryan 00:28:37 Yeah, it can be even worse than that, right? You can have GZ bombs or anything like that, where it uncompresses to a much higher ratio.
So, the… I guess the idea here is you will be cautious, and you will be… when you're decompressing, you won't try to decompress fully, then check for the limits. You're probably using some sort of streaming decompression, and once you hit the limit, you stop that.
You have to do something like that anyway. Otherwise, with the idea of… having a very high multiplicative ratio when you're decompressing is scary anyway. You have to be careful there.
So, anyway, what you're saying, that maybe you would prefer to have two different values for the limits, for compressed and uncompressed?
I think it's open for discussion, we can look into that, but what is probably more important for you is to decide whether that 4MB is enough for profiling. It seems to be it's not, so… then in that case, what is a good default for profiling? You'll need to come up with some number and make that as a suggestion. Probably… So, and we have two options there, then. Do we want to make that higher number the same value for all of the signals, or profiling needs a different number than the others?
Felix Geisendörfer 00:29:55 Yeah, I see NAF had his hand raised for a while, so he should go first.
Nayef Ghattas 00:30:00 Oh, yeah, so I had checked… we have the profiler running for a couple thousand hosts, and I checked… we used the HTTP internally, HTTP and not gRPC to send the data, and… P99 is around 4MB, P99.99 is 5, and maximum is around… 15 megabytes uncompressed.
Christos Kalkanis 00:30:27 Now you have to scroll through.
Felix Geisendörfer 00:30:28 uncompress.
Christos Kalkanis 00:30:29 That's from agents running on host, right?
Nayef Ghattas 00:30:32 Yeah, that's from agents on Amazon.
Christos Kalkanis 00:30:34 We can also have… we can also have the case where a collector acts as a sink, so that it collects profiles.
Nayef Ghattas 00:30:40 Yeah, stuff like that.
Christos Kalkanis 00:30:41 And 20, 50 machines, and then sends them to another collector.
In that case.
Yeah, I mean, we have to be reasonable. Like, we would like to support both cases, I imagine.
Report profiles coming from single host, and aggregated profiles coming from multiple hosts with multiple processing points, middleware, multiple collectors, for example.
But it's the second case that would need higher limits.
Tigran Najaryan 00:31:06 Yeah.
Christos Kalkanis 00:31:07 So…
Tigran Najaryan 00:31:07 And I would set the lim… set the limit.
higher than a reasonable number that you saw in production, right? So, if… if 15 megabytes is an actual number you saw in production, then that has to be supported.
I guess that's what I would aim for.
higher intent, obviously.
Felix Geisendörfer 00:31:29 So you would optimize for max rather than P99.9 or something?
Tigran Najaryan 00:31:33 I think so, yes, because then, if you optimize for P99, then 1% of your requests are failing. That's not great.
Felix Geisendörfer 00:31:40 Oh, I was saying P99.9, like, 0.1.
Tigran Najaryan 00:31:43 Even better, do you want 0.1% of your profiling data to be lost by default in normal operations?
You wouldn't have priced.
Felix Geisendörfer 00:31:51 I, I definitely do.
Tigran Najaryan 00:31:52 By design, right?
Felix Geisendörfer 00:31:54 Because these are actually biased towards potentially the most interesting profiles you want to get, because that's when stuff hits the fan.
Tigran Najaryan 00:32:01 Yeah.
Felix Geisendörfer 00:32:01 CPU samples, but, okay.
Tigran Najaryan 00:32:04 If you choose a limit like that, you are essentially saying, by design, 0.1% of my profiles is going to be lost. Not great.
Felix Geisendörfer 00:32:13 Yeah, but we're optimizing for two things here. We're trying to protect the collector from, like, destroying itself, and we're trying to get the data we want, and there's tension here, right?
Tigran Najaryan 00:32:22 I hear you. 15 megabytes, I guess.
today doesn't feel like it's a… it's a huge number, so I… I would feel comfortable with having a number, maybe a bit higher than that, even. And we already have 20 megabytes for HTTP limit today.
Christos Kalkanis 00:32:43 I think the proposal in the pull… sorry to cut in, I think the pro… maybe… because we haven't opened the pulley request, the person who created the pull request makes a suggestion to bump up the GRPC limit to 20 megabytes to make it the same as HTTP.
Tigran Najaryan 00:33:00 And that seems reasonable to me. I don't see why gRPC would have a lower limit than HTTP. It's essentially conceptually the same thing. It's for protection reasons.
Christos Kalkanis 00:33:12 Yes, sir.
Tigran Najaryan 00:33:13 Anyway, the interesting bit there also is, I think, on the client side, you may have limitations in gRPC defaults, if you try to send bigger messages.
I don't know what exactly happens.
So you may… the sender may need to… to also do something to reconfigure gRPC defaults.
I'm not entirely certain. If you try to send bigger message, what happens?
Felix Geisendörfer 00:33:37 Do we do that on our end, Nev? Because…
Nayef Ghattas 00:33:42 Oh, I might have missed the question.
Felix Geisendörfer 00:33:44 Do we reconfigure TRPC clients to allow bigger outgoing messages?
In our…
Nayef Ghattas 00:33:50 Right now, we're not using gRPC, only using HTTP.
Felix Geisendörfer 00:33:54 Okay.
And, yeah, sorry, and another stupid question, but I initially, when I saw the difference between GRPC and HTP, I thought the assumption was HTP would be using JSON, but we're talking protobuf payloads in both cases, right?
Tigran Najaryan 00:34:10 Yes, it's probatives, both cases, yes.
Felix Geisendörfer 00:34:13 Okay, but OTLP can generally also be transported as JSON, is that correct?
Tigran Najaryan 00:34:19 That is correct. I don't think anybody does that in production, but it is a possibility. The collector supports that.
Which is, I guess that's a good question. Do we want to have the same limits there? I would imagine? Yes, because I don't… It's primarily for, I guess, for… Maybe for debugging, for looking at it, seeing what it looks like. It's a good question. Maybe, yeah, I would add that as a comment on that issue to see whether we want to have different limits for… Or different encodings.
Felix Geisendörfer 00:34:59 Okay.
But I think the most important thing is, like, the… a reasonable default here, and 20MB might just do the trick for the data, at least that we're seeing on our end. One thing worth pointing out is probably obvious to a lot of people here, but, the amount of data produced from the profiler scales directly with the number of CPUs utilized on the host, so a bigger machine, bigger data. So even 20 megabytes is going to be fine for maybe, I don't know how big the machines we have now. I think we saw, like, 40-plus cores on average.
When we checked, but, if somebody is running 128 cores machines exclusively, they're still not going to be happy with the 20 mech limit.
So that's… I don't know if we can make everybody happy if we go for the absolute max of maxes here.
Christos Kalkanis 00:35:53 And there's also original payload, still to think about, right? Because if the message contains an original payload, that's going to bump up the size as well, and… Essentially, you're sending the same data encoded to different ways.
Tigran Najaryan 00:36:09 So, I guess… Based on what you're saying, the collector May need to be able to have… Smaller limits on the… on its receiving end when it comes from somewhere else.
But… the… the payloads coming out of the collector may end up being larger, because it observes a large number of processes, so the… backends, then, that are receiving data from the collector may need to have… may need to be able to receive these larger payloads. Is that what I'm hearing there? So that we may need to have different recommendations, essentially, for different participants here.
Christos Kalkanis 00:36:53 Right.
Or you could have multiple layers of collectors, right? You could do, processing, different kinds of processing, like a first-stage collector that accepts raw files from any hosts, a second-level collector that acts as… has a processing pipeline that looks at profiles, merges and rejects them.
And so on.
To me, 20 megabytes seems like a good starting point. Like, if I had to guess, without any data to back this up, I would say it's probably not sufficient for… to cover most cases.
like, if we think about the original payload as well, okay, I mean, you could say, how often is that going to be used?
I don't know.
We don't use it right now.
Felix Geisendörfer 00:37:41 Yeah.
Tigran Najaryan 00:37:41 It's also possible to split the payload.
ignoring the original payload for a moment, on the sender's side, technically, right? You could… knowing that the recipient has A particular size limit, you could try to split your payload into multiple requests.
Christos Kalkanis 00:38:00 Right, that would work. And even, like, if the sender had a way to determine that his request was rejected? Because, okay, maybe the sender knows upfront what the limit is, and then… he can… the sender can take it into account before he creates the request. So he can craft multiple requests so that none of those requests are rejected because they go over the limit.
But in some cases, that's not going to be possible for the sender to know ahead of time what limit a particular collector has. Like, in those cases, it would be nice if the error that the sender got reflected the fact that the request was rejected because it went above a limit, and the limit is part of the error.
In some way, and then the… The sender.
Could send the same request if it, you know, chunked it, essentially, so the data is not lost.
assuming it passes with one request, right? And it keeps it in memory until the response comes back.
That would be another win.
Tigran Najaryan 00:38:57 Yes, so there's two possibilities there. One is you know what the default is, because it's defined in the stake, you aim for that default, and you split if it's larger than that. And the other is we could look into adding the response content is too large.
in the OTLP spec, we don't have it today, as far as I remember.
But we could do that. Maybe.
Felix Geisendörfer 00:39:26 I think as long as, the default is pretty high, so that a lot of people are not going to run into issues, and it is user-configurable still, right? Like, I think this was pointed out earlier here. I don't think we need to over-engineer it.
I am partially thinking so that 20 megabytes is not a crate limit, should be 32. Like, if it's not a power of 2, how will you be taken serious by people? But, that's just me. I don't know if I can make a real argument out of this.
Tigran Najaryan 00:39:56 And it's a nice double of what the maximum you saw, I guess, is.
Felix Geisendörfer 00:40:00 Yes.
Tigran Najaryan 00:40:02 Possibly.
Double and add a bit more.
I think it's reasonable, 32MB.
Seems fine to me, if you… if you have a collector that has to deal with large profiles, then that's what it is, right? You give it a bit more memory so that it can receive the payloads.
It's best that you guys then, I guess.
Maybe post a summary of these concerns on the… on those, proto PRs.
And we can have the discussion there, continued.
Felix Geisendörfer 00:41:01 Yes. Any… anybody feel particularly interested in doing it? If not, I could also do it.
Going once, going twice… Aye.
Guess it's me. I'll give myself an action item up here.
Okay, any more thoughts on this one? If not, we have a few more things to get through today. I'm doing once, doing twice… Then Christos has another one. Oh, did we cover those?
Christos Kalkanis 00:42:09 Yeah, we can, we can skip this.
Felix Geisendörfer 00:42:12 Then Igbo again.
Ivo Anjo 00:42:14 Yes, so just a quick update on the context sharing stuff. So, the, it looks like the OTAP might be merged soon, So that's… that's… That's cool, and I've also done a PR to, move the proto to the right repo, so that, because right now we kind of had the proto just being copy-pasted around while we were testing stuff.
And, yes, we have that PR to add support on the eBPF profiler, and I think the missing part So once this lands, we can kind of land the PR on the EPF profiler, and the missing part is that I believe right now, in that PR, we're reading the data, but we're not yet propagating it to the profiles, so I think that's the missing bit.
Yep.
So… I guess progress is being made.
Felix Geisendörfer 00:43:15 Any calls to action for the group here?
Ivo Anjo 00:43:18 I think not at the moment, just pray and, like, light some candles.
Felix Geisendörfer 00:43:23 Okay, well, the light see all requests getting more scandals.
Christos Kalkanis 00:43:28 Yeah, once we get the auto merge, then we can proceed with merging the profiler. It will still need some work, because there is another pulley request that, I think, I'm guessing, is going to be merged first, that makes some structural changes to parts of the process handling in the profiler, and then Nikola's PR, it depends on those.
But it's…
Ivo Anjo 00:43:47 Nicolas said he was going to revise, 2 years old, he's aware.
Christos Kalkanis 00:43:51 But it's not going to be anything expensive.
Ivo Anjo 00:43:54 Thank you.
Oh, and yes, like, I had a note there that I forgot to say, which is, the… we have the ThreadContext OTEP, which is kind of the next step, in draft, and, like, once this lands, I'll undraft that one, and we can kind of start asking for feedback and, kind of iterating on that one as well.
Felix Geisendörfer 00:44:18 Cool.
All right, any… any more thoughts? Going once… twice.
Marie Thompson, is Jonathan here today? I can only see a few.
Jonathan Halliday (IBM) 00:44:31 I'm here today.
Felix Geisendörfer 00:44:32 Awesome. Take it away.
Jonathan Halliday (IBM) 00:44:35 well, pretty much just, what it says on the tin. I've noticed in experimenting with encoding JFR files to our format that If you're running JFR in a mode where it's doing more than one thing, It's basically creating multiple samples.
Sorry, multiple profiles.
And, there's no easy way to efficiently incurred that at the moment, because… The original payload is.
Part of the profile.
So if you have two profiles in your… JFR file, you have to send the JFR file twice, which is a little bit silly.
So, I think we, we could do with fixing that one.
That kind of relates to the message size discussion as well, in that there is also no easy way to Split the JFR file.
So if you have a large JFR file, that gives you the… the floor, the minimum size of the RTLP message.
Which is, a little bit inconvenient as well, and I don't think there's anything we can do about that one, really, other than Encouraging people to use, smaller JFR files.
Felix Geisendörfer 00:45:52 Oh, interesting. I misunderstood you originally, like, So the problem is not that JFR is producing multiple files, it's that we split a JFR file into multiple profile messages, and there's original payload is on the profile.
Jonathan Halliday (IBM) 00:46:05 Yeah, conceptually, a JFL file can contain multiple profiles.
Because you can configure JFR to do, you know, memory sampling and CPU sampling at the same time.
And that's… that's two different profiles as far as our encoding is concerned.
Felix Geisendörfer 00:46:21 Yes, that makes complete sense. I think this, like, original payload was added when we still supported multiple sample types on one profile.
Jonathan Halliday (IBM) 00:46:28 Yes, that's right, we just… we didn't, follow through and realize that the consequences of changing that were… Gonna reflect the original payload field?
Felix Geisendörfer 00:46:38 Yeah, yeah, we do need to change that.
question is, like, yeah, you suggested this could be a dictionary reference, that's one way to fix it.
Jonathan Halliday (IBM) 00:46:46 Yeah, well, yeah, ish. At first glance, it fixes the problem, but you have the additional issue of, if you've got a file in the dictionary.
You can use an index to tell you which of the dictionary entries it is.
So you could, for example, have two JFR files in the dictionary, and you'd know which one to look at, but you wouldn't know within that file Which sequence of events had formed that particular profile.
So if your JFR file has, you know, memory samples and CPU samples.
The encoder knows what it did to read those events and turn them into two profiles.
There's no way to pass that metadata along in such a way that… The transformation can be recreated at the other end.
Felix Geisendörfer 00:47:39 Yeah, I'm not hugely concerned with that, but it is… it's a valid problem. I think the bigger problem is, like, just duplicating the single that.
Jonathan Halliday (IBM) 00:47:47 Yes, yeah, absolutely. The message size problem is more significant, yeah.
Felix Geisendörfer 00:47:52 Yeah, and on the other one, that's a question, like, you could kind of do it with, I mean, we could specify some, I guess, attributes and semantic conventions that tell you, like, hey, this attribute tells you, like, the the name of the events in JFR, how they map to the, openTelemetry, sample types, something?
Jonathan Halliday (IBM) 00:48:11 Yes. Yeah.
Felix Geisendörfer 00:48:13 So I think we could standardize that out of bound, out of band,
Jonathan Halliday (IBM) 00:48:20 Yes, I think it's less likely to… They're breaking change to the message format than moving to a dictionary is.
Felix Geisendörfer 00:48:30 Yeah, but then, okay, still the question is, how do we want to solve the file problem, like, having the data twice? Like, dictionary is one. Would it be simpler or better to just move to skill profiles, like, as one higher level?
But I guess that wouldn't also be the right level, right? Or would it be?
That's what I'm trying to wrap my head around right now. One resource is basically, like, one, like, container or process or something producing data, or one host, and then scope profiles would be, like, a library, like the Java agent or something producing stuff. So I guess for that case, it would make sense to have it here, but… I guess dictionaries are a nice way out where we don't need to figure out the actual, Semantics of how these things might produce profiles, right?
Like, at which level they're produced. Are they produced on the resource level, like, from the original thing, or on the scope level?
I guess it has to be the scope, huh?
No, it could be the… I guess it could be any level, so I think… I guess I'm coming around to dictionaries as I'm… Thinking about this.
Jonathan Halliday (IBM) 00:49:39 I think it's just leaner, because we're doing everything else that way.
point of view of… reducing the number of abstractions people have to learn about the number of patterns, it makes sense to just reuse the existing pattern.
Felix Geisendörfer 00:49:54 Yeah.
Yeah, and creating hierarchies is really hard, I mean… God knows we struggled with getting the resources aligned with OpenTelemetry and figuring that out, so… I would go with dictionaries as well, so… Anybody else feels against dictionaries here?
Jonathan Halliday (IBM) 00:50:14 So, in terms of breaking changes, I don't really want to merge this one right away. We've only just released. I don't want us to be breaking it in the first week.
So I think I'll open a PR but market draft, or do not merge for now.
I guess we wait a while for user feedback, and then we do a bunch of breaking changes all at once.
Some… some months down the line.
Does that sound like a reasonable plan?
Felix Geisendörfer 00:50:41 To me, it does, yeah, I think we want to batch up anything that's not time-critical on the proto-change side to give people a little stability.
So I'm plus one on that.
Christos Kalkanis 00:50:52 Yes, same here. I think we made an agreement to do that anyway.
Maybe even wait until the better.
Jonathan Halliday (IBM) 00:51:04 Cool, okay, that's it for me then, thanks.
Felix Geisendörfer 00:51:07 Awesome, I'll give you an action item if you're willing to do that.
Jonathan Halliday (IBM) 00:51:11 Sure, yeah, yeah. I'm off until Tuesday, but… Yeah, it'll get done next week.
Felix Geisendörfer 00:51:17 That's fine. Same… same for the… some of the Europeans here.
Oh, and I should add a note on using semantic conventions, Okay, anybody else has more thoughts on this?
Going once, going twice, three times… Thank you for bringing this up, this is a very good catch.
Definitely need to change that. And Florian has a proposal for… Key value, and key value and unit. Take it away.
Florian Lehner 00:52:26 Yes, coming from one breaking change to the next one. This was already discussed before, promoting the alpha, signal to alpha.
topic.
The big… Critic was that we use a custom key value and unit attribute in the profile signal, and we are asked to switch to key value.
At the moment, key value does not have a concept or understanding of, units, but, the… we as a profiling group have the need to, Indicate unit speed, for example, bytes, megabytes, or something else.
Yeah, the idea going forward would be to… at… Unit.
String index to key value, like we have now.
Key, string index in key value.
and market, the same way as, Alpha, and just for profiling, so… This would allow us to work on, or to make use of this.
a new field in key value.
But exclude other signals, like locks, metrics, and traces.
Because, string index is only capable… can only work with, the profiles dictionary.
Yeah, and I wanted… To get some feedback if this is something we want to go, or, we should avoid.
Tigran Najaryan 00:54:10 I think it's… Worth opening the discussion on this?
I'm not entirely sure, Where it will take us.
with, with the… with the key, key indices and value indices there, values, string indexes there. We had the… we had the string values there already, right? So the ability to do the dictionary encoding was… simply an alternate.
you could use. Now, with this, if you just add the units index to key value, it means that profiles can use units for key value.
While other signals can't.
So, there's a functional difference there. It's not just a difference in how you can encode the data more efficiently, it's that Profiles now have access to an interesting capability that other signals don't.
Florian Lehner 00:55:16 Yeah, and we str…
Tigran Najaryan 00:55:17 may then, I guess, as a consequence of that, would be then, I guess, a reasonable question to ask, why don't we then have a way to record the unit directly without Using dictionaries, because these other signals simply don't have the dictionaries.
So, it seems logical, then you would have to add the pair of those, the unit and the unit string index.
Now, I don't really know if we want to do that for all the key values, because they are probably… I guess they are the most numerous things you have at the proto-level for all of the signals, so that can add At least in memory, it cannot, even if you don't use the values on the wire.
In memory, it adds some overhead, certain overhead, and that's… that's in the… in the… in the message that is… you have the largest number of those in memory.
Is it worth the overhead if no one is going to use it?
Or is there an actual appetite for using it by other signals? I don't have the answer to those. I think it's worth opening an issue and having that discussion.
And maybe the outcome will be that No, let's keep it as is. It's possible, right?
But I think we should have that discussion to make a conclusion on the open issue there.
Florian Lehner 00:56:40 Thanks. What I'm thinking about is that maybe we can be the guinea pig as profiles for the other signals.
use some kind of Unit 3 index at first, and if there is enough feedback, we can still add unit string just for other signals.
Similar, we have… for the similar… we use the similar mechanism that we have for key and keystring index at the moment.
So, if the… if… So that profiling can continue, it can switch to the… new key value and use a unit string index.
And if the request is still there from other signals, like log medics and traces, that they want to have the same capability, then we can still add the additional field.
Tigran Najaryan 00:57:29 Yeah, I guess that maybe the interesting bit there is I see that keystring index is an… is a 32-bit integer.
Which, on a 64-bit platform means that, because the other values are 64-bit aligned, you can add for free, essentially, another 30-bit integer there, and it wouldn't change your memory sizes at all.
So… Maybe if we use that argumentation, essentially.
nothing changes. If you don't have a unit, you can have that value there, and it doesn't occupy any extra memory.
Florian Lehner 00:58:07 Nope.
Tigran Najaryan 00:58:07 Or, I guess… for… for… for languages where it's applicable, not pass them or anything for languages like that.
Felix Geisendörfer 00:58:16 Yeah, one thing that I think we should spell out is, like, the backstory for why we have units is PPROF, right? Because PProf had units on the labels, and… we have mostly dealt with PPROP-specific stuff that we didn't want to track into OpenTelemetry by pushing it to semantic conventions. I don't think we fully explored what it would look like to… to do units as, with some level of attributes. Like, you could basically have attributes on the… on the resource level that tell you that, hey, this attribute in the rest of the message maps to this unit, for example, right? Like, this attribute string, or something like this. So it's… it's not… beautiful, but, like, it would get us the PPROF round-trip semantics that we need, and wouldn't… would also give us the ability to use units on other things, but wouldn't require us to make a fundamental OTLP change. I'm not proposing we should do that, but I think we need to at least Sketch that out a little bit and argue why that's not sufficient for solving the problem, compared to, like, adding… getting, like, unit to the… to the key value message.
Certainly, if we do find that the hacky way would work, it might actually save us a lot of trouble and would allow us to make Move faster and not make another braking change, etc, right?
Florian Lehner 00:59:33 Yeah, I'm switching to key value, from key value, and unit will be a breaking change from profiles.
Felix Geisendörfer 00:59:39 Oh, okay, sorry, it didn't sync.
All the way through, only some of the way.
Florian Lehner 00:59:44 Yeah, I think there are some attributes in resource attributes that have a unit attached in semconf.
But… Covering all cases that are possible to have a unit is… does not scale well, I think.
I'd be happy to…
Felix Geisendörfer 01:00:07 to sit down, like, async, or, like, on a Zoom call, like, in the coming week or two, to sketch it out and try it out, if somebody wants, like, Frey, and if you want to sit down together or something.
Florian Lehner 01:00:18 Sounds good.
Felix Geisendörfer 01:00:21 So we take that as an action item, we play around with this, and then, based on that, we either make a proposal towards the… 32 bits are free, let's get them, or the other way of going with systematic things, and then see where that takes us.
Florian Lehner 01:00:36 Yeah, let's take it as a… homework.
Felix Geisendörfer 01:00:41 Awesome. We'll… will assign us…
Tigran Najaryan 01:00:45 I think we missed an opportunity here to make key value and unit.
compatible with key value. We could have used the… The field numbers that were matching there, we didn't, so it will be a breaking change.
It's too late now.
Had we used the same numbers, then it wouldn't be breaking change.
You could just… because replacing the name of the message doesn't change the wire format.
But yeah, I think it is what it is, that's fine.
Okay. Where time I have to drop.
Felix Geisendörfer 01:01:30 Okay.
Tigran Najaryan 01:01:30 Thank you, guys.
Felix Geisendörfer 01:01:31 See you, thanks for joining, Tigran. If people want to stay a minute longer, I think we can maybe quickly get to Fredericks, or does everybody want to drop?
Frederic Branczyk 01:01:40 I've got the minute, but…
Felix Geisendörfer 01:01:43 I'll stay as well, because I…
Christos Kalkanis 01:01:45 Yeah, I think that was sick.
Felix Geisendörfer 01:01:47 Yeah, alright.
Frederic Branczyk 01:01:47 I guess both are wondering, and, you know, now that we're at this stage, should we be encouraging SDKs to implement and experiment with this? Should we be tracking this?
Do people know of some SDKs already working on this? I mean, obviously, Jonathan is working on Java-related stuff, but are there others?
Like…
Florian Lehner 01:02:11 I had a quick, conversation with Tyler and Damien that, were more… are part of the GoSig, Hotel Gozig, and they are interested.
And they are also highly interested in the process context.
So, these are the two things they want to tackle, but no timeline attached.
Felix Geisendörfer 01:02:36 I think we should definitely encourage, we should definitely track, maybe the best way to do that is to have a meta issue on the ProfilingSync repo, where we list all the SDKs, and we list, sort of, the status, like, hey, they know about that being a thing, like, somebody talked to that SIC, or they're working on it, or so on, like, and then people can link other issues to that, like, as SDKs commit to actually doing stuff, we can link their issues, and then kind of use that as, like, a… a way to keep track of it. I think we should do it, and I don't know if you have any bandwidth of maybe creating this initial issue, I don't think that's a big lift, but it's gonna.
Frederic Branczyk 01:03:11 Yeah, I can take care of that, and then, I happen to know some of the folks who maintain the, Python and Node, SDKs as well, so, I can… I think I could get them… I know they are aware of this, I don't know whether they've plans to do anything about it at the moment.
Felix Geisendörfer 01:03:35 Yeah, I mean, we don't need to get everybody to get moving at the same time, but once a few of them start moving, and we can show them, they can write blog posts, and the outdoor sticks might get interesting as well.
Christos Kalkanis 01:03:51 It's also critical to get feedback, right? Because if we don't get the SDKs involved at this point, and then we progress further, we have a beta, and we need the feedback from the SDKs to revise the protocol if such revisions need to be made, and now is the best time for that to happen.
Felix Geisendörfer 01:04:05 It's a very good point, because we thought a lot about the eBPF profiler as we were designing the protocol.
Christos Kalkanis 01:04:11 Absolutely.
Felix Geisendörfer 01:04:12 me and a few others here from Datadoc, we have an interest in runtime profilers and have expertise, but we mostly also thought about, like, what the eBPF profiler needs. So, yeah, it's going to be great.
Christos Kalkanis 01:04:23 Yeah. So maybe…
Frederic Branczyk 01:04:24 I know that the Google folks also want to get rid of, Node.js PProf. I know that Datadoc also wraps this, this, this, you know, library, so, like, I think they could be interested in… getting that out of their… out of their, org, basically, and get the, Node SDK to be kind of the canonical source.
Sorry, Chris, as you were saying, Colin.
Christos Kalkanis 01:04:58 No, I was gonna say, maybe we should be a little bit more aggressive, actually, so instead of assuming that, you know, all the SDKs have heard about us, or we're in their periphery, maybe we should just write a message to all of them, explicitly mentioning that we're now in alpha, we encourage people to look at the protocol, try to implement it. This is the best time for them to provide suggestions to us.
We're at the point where we're most flexible now.
for that.
Felix Geisendörfer 01:05:25 Yeah, at the very least, we can open an issue in everybody else's repo, and then cross-link that to our meta issue, and so this is how we can initially inform them, and we can put up more, like, advertisements in the form of joining their signal and other things.
Sorry, if we'll get back to my hands.
Frederic Branczyk 01:05:43 That sounds good.
Felix Geisendörfer 01:05:49 Okay, I have to play with my daughter now, but it was really fun specifying stuff with you all again, and I guess we're already over time, so thank you, everybody, for all the work, and have a nice local time. See you next time.
Frederic Branczyk 01:06:02 Thanks, everyone.
Christos Kalkanis 01:06:04 Bye.
Florian Lehner 01:06:04 Sure.
