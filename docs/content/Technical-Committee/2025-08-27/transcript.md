SIG: Technical Committee
Date: 2025-08-27
Duration: 69 minutes
============================================================

## Zoom Recording Transcript

Reiley 00:02:06 Hello, Club.
Bob Strecansky 00:02:08 Hey, Riley, how are you?
Reiley 00:02:12 Doing well, thank you. How are you?
Bob Strecansky 00:02:15 Living the dream.
Reiley 00:03:15 Hey, Sarah, Tiger.
Tigran Najaryan 00:03:17 Hey, everyone.
Morning.
Severin Neumann 00:03:21 Hey, good morning, good evening, good afternoon.
Hey, Bob.
Bob Strecansky 00:03:27 Gentlemen, how we doing today?
Severin Neumann 00:03:31 Good?
My day is almost over.
Bob Strecansky 00:03:35 I'm jealous.
It's almost launch time here.
Severin Neumann 00:03:45 Yeah. That's also good, right?
I have to wait much longer for my next lunch, so… That's fair.
Bob Strecansky 00:03:55 There, indeed.
Reiley 00:04:04 Hey, Bright.
Severin Neumann 00:04:10 Hey.
Tigran Najaryan 00:04:12 Whoa.
Josh Suereth 00:04:28 Hey folks, I'm late.
Tigran Najaryan 00:04:31 Hi, Josh.
Reiley 00:04:32 Thanks, Josh.
Josh Suereth 00:04:34 So, Tigran, I think you saw the chat. We have guests today, so welcome.
Reiley 00:04:39 Yep.
Josh Suereth 00:04:39 Cool. I don't know if we want to wait another, like, 2 minutes for… If we have quorum or not, but yeah. Just for folks' reference, we usually start about 5 minutes late, I should have mentioned that.
Does anyone else Google's docs, like, freaking out on the… Notes, or is it just me?
Armin (Dynatrace) 00:05:47 No, or Sumi?
That's you. Like our bullet points.
Josh Suereth 00:05:51 Alright, I'm gonna re-reload it.
Armin (Dynatrace) 00:05:55 I thought you were saying you were going to reboot it.
Tigran Najaryan 00:05:59 Can you reboot Google?
Armin (Dynatrace) 00:06:02 Just about the dock service, that's enough.
Josh Suereth 00:06:05 Do you want to… going down? I could.
Bob Strecansky 00:06:08 They tried a couple… they tried a couple weeks ago, right?
Josh Suereth 00:06:11 Yeah, that, fun story. That's… if you wondered why I disappeared from OpenTelemetry slightly, or have less free time, it's because of that. That's one of my teams, or near one of my teams.
Bob Strecansky 00:06:22 Oh, man.
Josh Suereth 00:06:23 Yeah.
Bob Strecansky 00:06:25 Sorry to hear that.
Josh Suereth 00:06:27 Yeah.
Anyway, you can be assured that we won't knowingly let it happen again.
Alright.
Tigran Najaryan 00:06:38 I think we can start, Josh.
Josh Suereth 00:06:40 Yep.
Do you want me to start presenting, then? Because we can just jump into.
Tigran Najaryan 00:06:45 Yeah, yeah, let's do it.
Josh Suereth 00:06:48 Alright, cool.
So thank you to, Brett, Bob, and Severin for coming in to kind of talk through the due diligence. I want to first just check to see if anybody feels we need to go private because they have things that they think are sensitive to discuss here, if we're okay doing this in the recorded meeting.
Tigran Najaryan 00:07:09 I don't know what's in due diligence, you tell me.
I don't know anything sensitive.
Josh Suereth 00:07:14 I will say, I am comfortable not having… having this be private, like, like, talking about this publicly. I don't think there's anything sensitive here. I don't think we have, … anything that we found that we need to kind of talk through in that way. But if, like, just to call out, if somebody wants to talk about something sensitive that they don't want recorded, we can move to a private meeting. So I'll just call that out first.
Okay.
Cool.
So, yeah, this is… this is a due diligence for OpenTelemetry PHP. A reminder of what this is, this is a zero-code instrumentation option.
for PHP.
What the code actually is, it's a combination of native code written in C++ and, PHP libraries and modules. It makes use of OpenTelemetry itself, and this is kind of the marketing advertisement for it. Actually, let me go to… is this readable?
Tigran Najaryan 00:08:11 Yep.
Josh Suereth 00:08:14 … Cool. So, the distribution's provided in a couple different packages. Notably, OpenTelemetry PHP actually already provides zero-code instrumentation of some form. Opentelemetry PH code, OpenTelemetry PHP is, is distributed… distributed as an APK, a Debian file, or an RPM file.
… So, it kinda, it kinda lines up a bit.
… The code consists mostly of PHP code, 50%. There's an extension in C++, it builds both for ARM and XA664, it builds both with, mucil, libc, and glibc, so you get the container-friendly libc, if you're familiar with that hell. And it's Apache 2 licensed.
The other thing is, it maintains a list of supported PHP versions.
But the, current version that's, distributed kind of locks you to an OpenTelemetry PHP distribution.
This was actually called out by, I think, Datadog has an alternative, where they made a comment about how, this locks to a PHP version, and there's a way you can do this where the user can actually have a dependency on OpenTelementary PHP, and the zero-config instrumentation can leverage that instead of coming hard-coded.
A few other important, notable things to call out, it actually supports a portion of OpAmp, so if you're familiar, Tigrin, with OpAmp, these are the, capabilities that it provides.
In terms of accepts remote config and reports remote config, I didn't actually dive into the details of what remote config support means here, because if you read their docs, they generally recommend doing everything with environment variables.
One thing I also want to call out is because of the op-amp support, you have resource detection that is used in OpAmp that actually grabs this set of resources, and as far as I could tell, I couldn't see how this integrates with resource detection in the PHP code from the PHP SDK.
So one of the… one of the requirements that we have listed later is just to make sure that if you're doing resource detection in both native and PHP, to make sure they line up.
… Okay.
Come on, computer. Alright, other notable features, and thank you for adding to this, Bob and Brett, automatic route span creation, so basically this will automatically make route spans.
PSP engine events fire earlier and more reliably, so this is actually more reliable than, going after the engine instead of doing it in the SDK, is that correct?
Sorry, Bob and Brett, you guys can jump in and talk anytime.
Brett McBride 00:11:10 Yes, that's correct.
Josh Suereth 00:11:12 Great.
Async exporting, so the, C++ implementation.
actually does asynchronous export instead of blocking in process. That's kind of a huge win.
If I understand correctly from our discussions.
Great. And then, ….
Tigran Najaryan 00:11:30 Have to be in a native code?
Or… There's no threads in PHP, not even the modern PHP? There's no way to do that?
Brett McBride 00:11:40 … Yeah, that's pretty… there's… yes, there's a thread-like implementation.
Which is fairly new, but, … Okay. We don't think….
Josh Suereth 00:11:54 the key here is, does PHP have background threads that run when the actual evaluation of PHP isn't running? I think… That's the main problem, right?
Bob Strecansky 00:12:04 Yeah, mostly.
Tigran Najaryan 00:12:05 Okay. Yeah.
Bob Strecansky 00:12:06 There is active work on some of those things in PHP, but they definitely are in their kindergarten phase. They are not… they, are not documented well, and they're… it doesn't feel like they're ready for prime time. Maybe they are, but that's just my perspective.
Josh Suereth 00:12:21 I feel like you should define our, sophistication levels for our software of kindergarten, prime time.
Like, what's in the middle? I like it. Anyway.
Tigran Najaryan 00:12:31 Sorry. Can you guys talk a bit about the mechanics of the zero-code instrumentation? What exactly does that mean? Is it that it… Is it… is there any overlap with the… with the thing that Antoine recently contributed, started working on?
Like, the one that injects the environment variables into the process at the startup time.
Is there anything similar happening here, or is this just pure, like, PHP-based solution?
Josh Suereth 00:13:01 I call this out, and I don't… you know, Brent and Bob jump in, but basically, from what I was reading, there's environment-based variables that will enable this, and you have to install this thing in the VM or container that you're running PHP.
And it will hook into the PHP engine, as a… as a kind of shared… shared library, you know, hook into PHP.
And so the environment variable is how you configure it. So there is overlap with Injector SIG, where when this is in use, we would want the injector group to know how to make sure this is in play, and how to send environment variables to it.
Tigran Najaryan 00:13:41 So this is zero code in the sense that you don't write any PHP code.
But this is not… essentially zero-touch instrumentation. You have to do something manually.
for the instrumentation to be injected into the PHP process, is that correct? Unlike what Antoine is doing, which was, essentially, you do nothing in With your particular process, it just injects into every process, an OpenCluency instrumentation.
Is that… Correct?
Josh Suereth 00:14:15 Almost all the zero-code instrumentation, you have to do something to the process to get it to go in. Antoine's hook is to do that thing on your behalf.
Tigran Najaryan 00:14:25 Yes.
Josh Suereth 00:14:25 Right.
Tigran Najaryan 00:14:26 This is… this is different from that.
Josh Suereth 00:14:28 So yeah, this is the core capability, this is like the Java agent, right? You have to do something to the workload to get, like, the Java agent on, or to get the .NET diagnostic thing hooked up, right?
Tigran Najaryan 00:14:38 Okay. Can you clarify what exactly is that thing that you're doing to enable the zero-code instrumentation?
Josh Suereth 00:14:46 Yeah, yeah. Go ahead, Bob or Brett, if you know, otherwise I can jump in.
Brett McBride 00:14:53 So, so the thing that you're doing here, is… Is installing an extension into the.
Reiley 00:15:00 to the PHP runtime.
Brett McBride 00:15:02 Okay. And that gives hooks into the, you know, the life cycle of a request.
Okay.
Tigran Najaryan 00:15:08 Got it. That's the C extension that essentially does that job.
Brett McBride 00:15:12 Yes.
Josh Suereth 00:15:13 Okay, makes sense.
And in practice, that's a Debian, RPM or Alpine Linux package app, that you would.
Tigran Najaryan 00:15:22 Okay, understood, yeah. You essentially modify the PHP engine, modify it in a supported way, through an expansion.
Witches.
Typically what people do with PHP when you have to do something in the native code.
Bob Strecansky 00:15:36 Right, and our current auto instrumentation does kind of the same thing, but it runs in C, and is even more obese than this result, and it can be, like… we don't really have that many maintainers for it, and it can be a little obtuse for those who are, unaware of it.
Tigran Najaryan 00:15:55 And is it… is the… do you… these days, do you modify the php.ini file to do that, or there's a different way to do that?
Brett McBride 00:16:06 You do also need to modify php.ini. That's how you enable a, an extension or a module, and… And, theoretically, you can also configure them through PHP.
Tigran Najaryan 00:16:23 Just trying to understand, my PhD knowledge is about maybe 15 years outdated, so trying to understand what's new there.
Josh Suereth 00:16:31 Yeah.
So, I think you're asking lots of good questions. I want to get to kind of the hard, hard things and why we have these here. So, acceptance requirements. Basically, work with PHP maintainers to figure out what zero-code instrumentation looks like.
We need a plan for the existing zero-code instrumentation with this donation.
And kind of how to move forward. So I assume there'll be some sort of a phase where we try to phase out the existing zero-code instrumentation in favor of the new one, but that's something we're going to ask them to work with you, Bob, you, and Brett, on how that looks, what that… You know, what kind of, … Supportability timeline you want on that?
Bob Strecansky 00:17:08 Yeah, so I think that it is important to accentuate that our current existing implementation has very few maintainers or a few people that understand it. The Elastic people have been very willing and able to help us with a bunch of instrumentation things, and I think they developed this I mean, they developed the solution as part of something… as part of a product offering. I don't think… it's definitely a little self-serving, but I think it's pretty generic, and I think that they are willing and able to help us continue to work on this, which is a big plus for us when we have very few contributors.
Josh Suereth 00:17:44 Cool.
The other thing I already mentioned was basically the native… native and SDK resource configuration. We want to make sure that somehow we have a way to share those, or keep them consistent.
As needed, so we're calling that out as something we'd like to see. This is… this is in line with the… the value we have for zero code, where if you… if you use the PHP, you know, libraries, the API, and you use Zero Code in… installation.
Things should be the same as if you just use the PHP libraries by the same, it should just be easier.
Right? That's kind of, like, the goal here. So, that's why we have this as a requirement.
The other one is ensure the codebase could be contributed to by other PHP-supporting APM vendors. We already had, Datadog make some comments with things they would like to see in the codebase, in the, donation proposal. You can read those if you're curious.
But yeah, that's another thing we want to make sure, is that this has a robust set of maintainers. I will ask the hard question, which I already know I hissed both of you before, Brett and Bob.
you know, how comfortable are you with this native code coming in and the maintainer approvers within the PHP ecosystem to, like, continue to provide this?
You know, is this gonna be, like, the Elastic Show, or is this something that you feel is gonna be a healthy kind of ecosystem benefit for everyone?
Bob Strecansky 00:19:18 I was trying to play rock, paper, scissors with Brett. I'm not a C++ expert, and I don't pretend to be one on the internet. I'm pretty sure Brett's in the same boat. I think that we don't… like, the Elastic people are most of our C++ knowledge at this point, but that's a… I think that that shouldn't preclude us from letting Taking this, this, … donation, because I think that that's probably what would have happened either way. I would encourage other APM vendors to take a look at this. Sometimes it's difficult to engage with them, because they have other competing priorities, but… Of course, we would love to see other APM vendors contributing to this repo, and I think that would probably be good for not only the health of the repository, but also the subject matter expertise across our seg.
Josh Suereth 00:20:09 Did you want to add a report?
Tigran Najaryan 00:20:11 Yeah, sorry.
Brett McBride 00:20:15 Yeah, yeah, I agree with, what Bob said there. You know, I've actually… I've been going over the code.
In the last few days. I'm certainly not enough of a C++ programmer myself to… … you know, to maintain it, at least at this point, but, but I don't see that as a blocker. It's… Yum.
it's still, you know, it's very good code. I just, … I'm not… I don't feel that I'm qualified to… to understand it at the moment.
Tigran Najaryan 00:20:55 So, regarding that C++ portion, there is an implementation of an OTLP exporter, right, if I understand correctly there, in C++.
I think that's… that's what you said, Josh, earlier.
Josh Suereth 00:21:06 Yep.
Tigran Najaryan 00:21:07 So, and does that use our OpenTelemetry C++ SDK's OTLP exporter implementation?
Josh Suereth 00:21:16 I… I don't believe it does.
Brett McBride 00:21:18 It does not.
Tigran Najaryan 00:21:19 Okay, so why not? That would be my question, why not? And can we make that happen, so that there is… only one C++ OTLP exporter implementation to maintain in the project.
And we actually have C++ maintainers, right? So that there is.
Josh Suereth 00:21:36 Right.
Tigran Najaryan 00:21:37 A lot less for the PHP SICK to maintain in that case.
Josh Suereth 00:21:40 Yeah, this is where I am going to be very careful what I say that's publicly recorded. I think… I think their implementation's pretty good, and they are allowed more dependencies than we allow our C++ implementation.
So our C++ implementation is… tries to be as zero dependency as possible, and has, like, a flexible, bring-your-own kind of HTTP endpoint to it.
Whereas they can depend directly on gRPC, they can depend directly on Boost, and they end up with kind of a bit of a cleaner implementation, because there's less, like, abstraction layers.
So I actually think that what they have is low cost and easier to maintain for the PHP folks, if they're looking for that. I actually think it might be rather expensive.
for us to force the no-standard OpenTelemetry SDK exporter into this mix. We can look into that and kind of talk about that, but I think that that would be quite some time.
Tigran Najaryan 00:22:37 I think we should look into that, Josh. My opinion is we should look into that.
whatever deviation there is from the decisions that were made by our C++ SDK maintainers.
I think we need to look into that. What you described there, that they are using different dependencies, they're… essentially, you're saying it's… batteries included, right? It includes the HTTP client. You need to have one if you have an OTLP exporter. But the thing is that it… what sort of dependencies does that include? Does it… does it use… is it dynamically linked? Does it include curl there?
in the distribution, unlike our OpenClonetry SDK, which doesn't. You said Boost?
Is it statically linked? Like, it's… there's a bunch of questions that I'm not sure… I'm seeing immediate answers that I think the questions probably need some answers there.
If the decisions made here are different from our C++ maintainers made.
Why is it? Is it just because we control the distribution in this case, and have no problem including the HTTP implementation, as opposed to the SDK, which is a library where we don't control that? Is that the reason?
Josh Suereth 00:24:02 The main rationale behind this is this is a application, not a library. And so, taking a dependency of something the application can totally do and be fine, because it's building… like, you're building a RPM where you can control your set of dependencies, right?
Tigran Najaryan 00:24:18 Okay, I understand that.
Josh Suereth 00:24:20 is important to this. So we could have it use C++ and go through that layer of dependencies, that's fine too, but honestly, the thing that it's doing, it's also… it's not using an API. So if it goes after the C++ SDK, it would be using a lower layer.
Reiley 00:24:36 than what.
Josh Suereth 00:24:37 we provide in our API and SDK, because it's basically funneling OTLP out of PHP and then getting it that way, and it's using the API provided by PHP, right? So, what we're… what… if you wanted to look at a different mechanism where the C++ API is basically fronted by a PHP.
Reiley 00:24:55 Source?
Josh Suereth 00:24:57 Cool. That's something we can investigate. That is not what this is. This is basically take the PHP API, funnel it almost as is into C++, and then fire that out C++.
Tigran Najaryan 00:25:07 Yeah, yeah. Okay, my concern still holds that this is essentially duplicate functionality and implementation of OTLP Exporter in C++ done in a different way, that still has to be maintained.
and maintained by now PHP maintainers, who don't necessarily feel that they are.
Reiley 00:25:28 The right people to maintain that code, right?
Tigran Najaryan 00:25:32 I think I would ask this hard question. Is it possible to rip out the exporter implementation, and replace it by the one that we have in our own C++ SDK.
add on top of that the actual HTTP implementation, which is what you need to do, because this is an application, right? You make your choices, you bring the HTTP client from Boost or whatever library it is, I'm totally fine with that, but don't fully reimplement OTLP, right? Because it's, … I don't know why would you do that.
So, that's… that's my comment there.
Josh Suereth 00:26:11 I hear what you're saying, but again, like, the… we're talking about… we have a data model from the PHP API and protocol, right? And we're just taking that data model, turning it into proto-events, and firing it out, like a gRPC implementation.
It's not actually… like, if you look at the amount of code in there, there's about twice the amount of code for supporting op-amp than there is for supporting the OTLP export async stuff, when I was looking through it.
So it's not a significant amount of code, and that is considered an internal implementation detail in the C++ SDK.
That's my point. It's not a public API.
Right? So, it, like, if we want to say this should use the C++ APIs and SDKs.
and use the C++ exporter. That, I think, is what we'd be asking in practice here.
Let's make a note.
Tigran Najaryan 00:27:06 A lot of that we can discuss later. I think Riley had his hand up for a while now. Go ahead, Riley.
Reiley 00:27:13 So, first, I apologize. I believe Zoom is telling me I'm muted. I have to unmute and unmute myself again. So, my question is about security. I look at the repo from Elastic, and I check the changelog. It seems it has been there for 6 months, and I haven't seen… … like, a lot of examples how people patch the CBEs.
So my question is, what's the… current security debt on the existing OpenTelemetry PHP products, and with this adoption, do we think it's going to Like, how to make the security aspect better, or… we think it's going to add an additional burden. Like, if we already have a lot of security vulnerabilities that we… we cannot easily fixed. By adopting this, we're adding more debt than I… I would have some concerns.
I'm… I'm specifically worried about the… the supply chain, like, because now we're not talking about PHP only, we have C++, and a lot of libraries, so… The supply chain might be big, and… I don't know, even it might bring additional license issue, because latency, the source code being being donated is… is all following the compatible, like, Apache 2 license model, but what about the underlying dependency? Do we take the source code in some form and compile that?
Josh Suereth 00:28:50 I did a brief look through all the dependencies, I can add that to the due diligence, but they… they are all… from what I can… from what I saw, it's… it's Apache or things we already depend on, right? So, like, it depends on the PHP libraries. Boost is Apache, effectively. Boost is allowed by CNCF, I should say.
So I think from that standpoint, we're right. If you're worried about supply chain of C++ libraries, like, we should just follow the conventions that are done for OpenTelemetry C++, whatever we decide to do there. I don't think this expands any risk footprint higher than we already have the capability of addressing.
So, like, everything's built in a container. That container can go through a security audit, and we can use that, our existing container security audit mechanism to make sure that those containers are up-to-date and vulnerability patched for, build, like, supply chain security.
Reiley 00:29:46 Okay, thank you.
Josh Suereth 00:29:50 Good, Carlos.
Carlos Alberto Cortez 00:29:51 Yeah, so basically, mine is about the feature requirement point, which seemed a little bit, important to call out. If you could scroll down.
A little bit, please. Yeah, the… Papa, which one was that? Provide a bring-your-own SDK version capability. I was looking into that, and a lot of people were saying that they would like to have a slightly different approach. Like, the same, because they have the same, I think, or something similar.
But what Elastic has is that they bring their own instrumentation and SDK and everything. And what Datadoc wants is that you allow the user to bring their SDK, and you only install the instrumentation, you know?
And, … That… I don't know how abstraction would be required to actually achieve this.
But it sounds like a lot of work to me, you know?
And that… I'm just… I would like just people to know that probably this would require Datadoc people to work on that, and … Yeah, I think this is a big thing, you know, just to keep an eye on, because this could prevent Datadog, in theory, you know, from providing, like, some maintainers or help, you know, here.
Josh Suereth 00:31:07 Yeah, I agree with your concern, Carlos. I guess my question to you, I listed this as a future thing, where we could accept the proposal, pull it in, and then add this in the future as part of the acceptance. So, like, we get Elastic to agree they will move this direction.
and work with Datadog to make sure it fulfills that. That's my thinking. We could make it be an acceptance criteria where that has to happen first.
which one would you prefer here? Because I agree we need to make sure they're on board with that, yeah.
Carlos Alberto Cortez 00:31:35 I think that what you are doing is enough, as long as it's super clear that this is a requirement, like, it's not, like, good to have, it's, like, a requirement, you know? And if it's not a requirement, discuss why, but yeah. Yeah, I don't think it has to be done before. But yeah, as I said before, let's just make sure that Elastic folks are super sure that this This is something you could be happy with, like, way down the road, you know?
Bob Strecansky 00:31:59 I want to echo a lot of the sentiments and sort of underscore a couple of these important points, like, this is… this, like, this elastic distribution that they're planning on donating, has been only worked on by Elasticsearch people, and has only been within the Elasticsearch organization for, like, a pretty decent amount of time. Them exposing it to the public.
is definitely a thing, right? Like, we need to make sure that all the security vulnerabilities are patched up, we need to make sure that it's vendor agnostic so other APMs can contribute to and use it if need be.
the… I don't want to say issue. The opportunity we have there is we need to get other people that are more well-versed in C++ than our current list of maintainers to vet this and make sure that things are hunky-dory before we accept it, probably. I think that's the too-long-didn't read from my perspective.
Josh Suereth 00:32:51 Yeah. Should we… should we bring in the C++? So if we look at… hold on.
Where is this? If we look at stakeholders, should I bring in the C++ folks as a stakeholder here?
Bob Strecansky 00:33:07 I'm curious whether the C++… I think that might be one of the… again, not… I'm not gonna use the word… that might be one of the opportunities. The C++, like, might not care about this at all, right? Like, this is not their focus, this is not what they're interested in, this is not what they are using their open source time to do. I think we might have, like, a… misaligned. There… it's possi… Riley, you're really loud. ….
Reiley 00:33:30 That we might have a misalignment.
Bob Strecansky 00:33:32 there, and that could be… that could be troublesome if we need… if we decide that we need to go down that route. That is a concern that I've had, too.
Reiley 00:33:44 I feel it makes sense to at least notify the C++ maintainers, and they can choose whether they want to be here or not.
And I also think there's a tricky situation, because we're seeing many folks moving from C++ to Rust, so the reality is, for many projects today.
it's a hybrid situation. You might have, like, 80% of the code in C++, but you use some ROS libraries. And… and we've been having this thinking about, hey.
we don't want people to use both C++ and Rust SDK in the same application, because in this way, context propagation, like.
propagating the spend ID trace ID is a nightmare, and doing the metrics aggregation, do you want two separate SDKs to have separate exporters configured? So, one possible outcome is maybe we'll just, like, make more investment in OpenTelemetry Rust.
and have the foreign function interface, so people use C++, or even, like, C, they can do the I-55 into Rust.
And I feel those things might also… affect how people think about the C++ code here. Maybe at some point, we want to move to Rust. So, I at least share this information with both C++ and Rust maintainers.
Let them decide if they want to join or not.
Josh Suereth 00:35:08 Yep, so….
Brett McBride 00:35:09 It's… Sorry, I was gonna say, that's a really good point, Riley, and we've actually, already prototyped, using OpenTelemetry Rust.
… I've been working on that a lot, actually, the last 6 months, but… we just don't have… anybody except myself, who understands PHP and writing PHP extensions, and knows anything about Rust. There are just so few contributors, and we basically abandoned… abandoned the idea for that reason, not because it doesn't work, it does, We just… we just don't have the people.
Reiley 00:35:49 Yeah, I understand. It's hard to find someone who's good at C++, Rust, and PHP.
So, like, recall that.
Bob Strecansky 00:35:58 And is interested in observability, and is interested in working for free.
Reiley 00:36:02 Exactly.
But at least we should do the reach out, and we can share with the community this is what we're looking for. So, I know recently there conversation between the Rust maintainers and to developers in a startup company, and they actually seemed, like, super interested, and said they would join our SIG meeting and see if they can contribute. So the problem is.
I think the first thing is we should let people know that we have this problem, and we're very interested in solving the problem. We don't have the people with the right skill set, but if someone would want to contribute, we would love that. Currently, I feel that information is not… widely communicated.
Josh Suereth 00:36:54 Yeah, okay. So, … We'll take an AI to bring them into that discussion and continue that for further due diligence. That… that sounds absolutely reasonable. Now, I will say that, Brett was very, very, very gracious with us, and adapted to our time zone.
I don't know, is it, like, 3 AM for you or something? It's like a horrible time, so thank you, Brett. I think we're gonna have to have discussions at different time zones, going forward for this.
So, I think this, like, I don't want to ask Brett to continue to do that. So the next one, let's meet with the C++ developers, and let's find a friendly time, for, like.
for Brett, Bob, and the C++, maintainers to discuss. So that's an AI going forward. Real quick, let's go through future acceptance, and then make sure we've covered all the concerns to continue.
Because there's two new to flesh out more things. So, the provide your own SDK version, since Carlos called it out, and this was also my thinking, I'm gonna put that at the very top.
The other thing we want to call out is support for file-based configuration as defined by the configuration SIG.
There seems to be some file-based support in the op-amp, native code. I'm not exactly certain what it… does, because, you have to follow the code traces to see what it is, and the docs seem to recommend using environment-based configuration only. So, that's something I want to follow up with them and just make sure they're committed to having to support the, what the configuration SIG is providing.
I want, the other future requirement was to work with the injector SIG on capabilities, so the injector SIG is trying to make zero-code instrumentation even easier to use, and so we want to make sure this is on the radar of, hey, PHP zero-code instrumentation is changing. Let's make sure that the capabilities you're building as part of injecting you know, zero-code instrumentation, let's work with them to see what they need to make sure this is aligned, and make sure that going forward, Injector supports this capability.
….
Tigran Najaryan 00:38:56 And Injector does not support PHP today, right? They only support, I think, Java, Node.js, and another language, but not PHP, I think.
Josh Suereth 00:39:07 Yep.
Bob Strecansky 00:39:08 This is my first awareness of the injector SIG, so I'm pretty sure it's not collaborative.
Josh Suereth 00:39:14 Yeah, it's new, so if this is your first awareness of it, don't worry, it was the previous, like, donation proposal.
… Cool. This one, I think, Brett or Bob, did you add this one? Do you want to talk about this one?
Brett McBride 00:39:30 I did, yeah, yeah. So we do… asynchronous exporting, as, as we mentioned earlier.
But the… the batch span processor is still using the one from the PHP SDK, so it's not fully asynchronous, non-blocking. You know, it relies on… … it doesn't… it doesn't fire on a timer every, you know, BSP schedule delay, it just fires the next thing that happens after that time has passed. So, … Yeah, so I think the Elastic guys have just, ….
Josh Suereth 00:40:14 We've done the least amount of work possible.
Brett McBride 00:40:16 You know, to, you know, replace one component of… of the, … a delivery PHP SDK, to make… … the actual export process, asynchronous, but I think we can go back a step and You know, do more of the hot path.
Josh Suereth 00:40:37 Yeah, yeah, yeah, this, this is, good, good call-out. I actually didn't notice that they hadn't overrided that. Yeah, so this, this gives us the kind of runtime capabilities we want in tracing SDKs for what Batch is meant to do in PHP, yeah. Cool.
Alright. So then, the other thing was basically looking at installation methods, and looking at current, current packages that we propose. This is in line, Riley, with what you're saying around security around build attestations and understanding our packaging capabilities. I think we just want to look at their packaging capabilities, our packaging capabilities, make sure that when we pull this in, we pick a set of packages that we can stand behind, that we have secure builds for, that, you know, match our distribution mechanisms that we want over on OTEL.
This is just making sure what they do, what PHP's doing today, is in line.
So, yeah.
I actually… interesting. When I was doing the due diligence, I learned about Peckle, because it's been a while since I did PHP as well. I didn't learn about Pi, I don't know how I missed that one. So, let's take a look.
Anyway, cool.
… Any other concerns here? Otherwise, I think, thank you, everyone, for the extra time.
We'll follow up more offline. But last, last minute, any concerns we need to add here?
Reiley 00:42:10 No, it looks great.
Josh Suereth 00:42:12 Okay.
Cool.
Thank you, everybody. Thank you, Bob and Brett, and … we'll see you online on Slack and continue the discussion there. And feel free to update the document with things you discover or want to add based on the discussion.
Bob Strecansky 00:42:26 Thanks, everyone.
Reiley 00:42:27 Thank you, guys. Alright.
Brett McBride 00:42:29 Yeah, Paul.
Liudmila Molkova 00:42:30 Thank you.
Brett McBride 00:42:30 Nice to meet you.
Josh Suereth 00:42:32 Yeah.
Tigran Najaryan 00:42:38 Josh, I think you have the second item as well.
Josh Suereth 00:42:41 I do. Is there… are there any other items that might be more urgent?
Like, do we want to handle Riley's item quick? Because the other one I have is quite large, or somewhat large.
Riley.
Reiley 00:42:57 I can quickly go through it, won't take more than 3 minutes, I think. So the measurement processor PR, I think the original author feel tired about all the All the blockers, and… And seems like he's no longer actively working on it. So given the fact that PR already had multiple TC approvals, I feel there's support from the TC. We believe that's the right feature we want to have.
But… do we want, like, do we think someone would be willing to spend the energy there? I feel like if there's only one TC member trying to push, we won't get some success, but if we can have, like, at least two TC members who actually try to drive it. Like, either we can say, let's step back a bit, try to scope it down, so we can remove the… the blocking comments from Ted and Tyler. That's one approach. So we'll say, like, we're not trying to achieve everything.
originally we wanted, but we tried to step back. The other thing is we still believe that we want the ability to modify the measurement And we'll go through that, and maybe at some time, we'll escalate to a TC voting or whatever. So, my question is, there's 3 options in front of us. One is we just don't care. We let it die.
But given all the approvals from the TC and all the comments we made there, I don't feel that's the right approach. So I would be leaning forward to have at least two TC members working on, like.
making progress there. We want to get something done there. And then those two TC members can decide whether they want to go, Like, with the original proposal, or they want to step back to have a balance, just to unblock things?
What do you think?
Tigran Najaryan 00:44:53 Do we have those TC members who want to do that?
I guess that's… that's where he… Where it plants, right?
Reiley 00:45:00 Because it's my choice, I have the history, and by default, I know the history of measurement process, and I know people need that. We've seen the request many times, so I'm willing to help. My problem is, if I'm the only one who's actively helping.
I won't be able to merge anything. I can either send a PR with no approval, or I can approve something.
Nice.
So, so….
Josh Suereth 00:45:24 I think, I think, let's look at who the 5 approvals were, right? Riley, it was you, it was me, it was Josh McDonald, it was David Ashbold, and it was Jack.
Reiley 00:45:33 Sure, right.
Josh Suereth 00:45:34 Which, depending on how the vote and the GC discussion goes, anyway, we, … that's 3… 3 of the TC members, and that's one who is an ex-TC member who also led metrics, and another person who's a metrics approver. So we have 5 metrics approvers to move this forward.
I think you have support here, we just need to finish the discussions with maintainers. Like, I do think we have to address Go's concern.
And I… whether we take a step back or not, I actually… one of the discussions I want to have when I did the proto, issue triage, because I just noticed we had a bunch of issues that are unlabeled, I think it might be worth making a Phase 2 metrics.
project.
of, let's go through… we've pushed a lot of things out of scope in metrics when we pushed the initial API SDK.
I think it might be worth putting together a principled approach to, like, let's figure out the use cases and metrics that are struggling right now, let's get a full, dedicated project to just nail them and get them done. I think there's enough for us to look at.
to do that, in my opinion. So, and this is one of those things that is just languishing, because we don't have… like, it's not a dedicated, focused effort right now, right? And so.
I think, let's use the project process, let's put together a list of all the things that are missing in metrics that we want to add as the next wave, and let's make a metrics phase two.
That's… that would be….
Reiley 00:47:08 Enough bandwidth or funding.
Like, I have a lot of doubts there. I mean, I have the passion and energy, but I feel we're already drowning. Like, for example, the security one, how do we fix CVEs? I've been pushing for that, and I kind of don't see enough help from… from many folks in the community. So, my worry is, if I start another effort, I might be… wasting more time, instead of actually seeing the progress in the open telemetry community. Like, like, originally, I agreed to help on the metrics because I see a lot of people willing to help. I got support from you, from GMACD, from Bogdan.
This is why we're able to, like, I'm willing to spend a lot of SPAC, I'm willing to drive things, but now I feel, even if I'm trying to dump the energy there, I don't get a lot of support from people, because we're spreading things. We have too many things we're interested in, so… so do you think it's reasonable for me to spend time on it?
Josh Suereth 00:48:08 So I'll say the second thing, which is, I think if you were to make that proposal, I would say not now. Which is, like, we have too many active projects, and so if you were to try to put that proposal together, we'd instantly see, we don't have enough sponsorship for that proposal to be executed on. So let's finish some stuff, and then let's do that. That's my opinion, right? Like, if configuration finishes, Jack might free up a little bit. If we get entities finished, I will free up a bit, right?
Reiley 00:48:36 Yep.
Josh Suereth 00:48:36 Sorry, Entities Phase 1, because we're cutting entities in two.
And my thinking is, it might be important to actually finish Metrics Phase 2 before Entities Phase 2. Like, we can do those kind of games now, if we start having well-defined scopes, and we start using the project mechanism. So yeah, like, I fully think we should work on this. I fully think we should use the project mechanism, and I fully think if we do so, we'll be able to slot it in when you can get attention.
But that's probably not right now.
Reiley 00:49:06 I see, yeah. So my gut feeling is, if we couldn't even prioritize some of the critical security vulnerabilities.
then I won't have bandwidth for anything else.
Josh Suereth 00:49:20 That's fair, that's fair. That's… yeah.
I hear your concern, and I think that's overall just a problem we're all struggling with, right? Even some of the projects that are active, I still feel we're spread pretty thin with our current active projects.
Reiley 00:49:40 Yeah, I understand. Thank you.
Okay, I'm done here.
Josh Suereth 00:49:45 Okay.
Related, in terms of getting stuff done and cleaning stuff up, I guess I'll present again.
I wanted to talk a little bit about the proto-repo. So, we… the… the, … Profiling folks have been doing a lot of work in the Proto Repo. I was trying to look at it and look at triaging. Today, for context, I don't think… the, … I don't think that the GC triage includes the protorebone, or at least it didn't go and do old issues.
So what I tried to do was triage… there's only 36 of them, but I tried to go through and triage issues to try to give a better signal to the community of what we're going to do with the Proto Repo, and kind of close things. So things that we know we're not going to do, or things that we already did, but forgot that there was an issue about them, we should just close.
There's a few contextual things here around the protorepo that, I'm gonna call out.
Specifically, one, consuming protos is confusing.
The way that people consume the proto repo, we probably need to do a better job of documenting or explicitly saying, you know, go to a language SIG and ask them for a proto thing, if that's what we want.
we might need to actually fix up how we bundle the proto-repo. Right now, it's a tar of the entire repository. That confuses people. And the other thing I found is people are trying to use our build tools … thing that we do to validate protos before we make releases and PRs, they're trying to use that actively in their, their builds. And I think that's problematic, because I don't think BuildTools has the best, the best maintenance.
Tigran Najaryan 00:51:29 Josh, you mean for generating the language bindings for that purpose? And for all of the languages, we essentially have the generated bindings in the SDKs, right?
Josh Suereth 00:51:43 Not necessarily. No, it's not… No, not necessarily. Like, some of them don't.
Tigran Najaryan 00:51:46 are the ones where the… there is an implementation of OTLP exporter, I mean? No.
Josh Suereth 00:51:51 No, Java does not provide one.
Java hard-coded their own language binding.
Tigran Najaryan 00:51:57 Oh, there's a hand coding.
Okay, but we… what I was… what I was suggesting is that we can link to the implementations in the languages, regardless whether it's generated or hand-coded.
At least it would be a starting point for them.
Especially if those are, implemented with, with as few dependencies as possible. Like, for example, in Go, I think there's an OpenTelemetry OTLP Go or something, like, it's a completely separate repository, not even in the SDK, right? With that, you can actually consume it, right?
Josh Suereth 00:52:31 Except that is for expert only. If you wanted to provide ingestion, like you wanted to make a.
Tigran Najaryan 00:52:36 No, that's a good point. Yes, that's a good point.
Josh Suereth 00:52:39 So, so, anyway, you can look at the issues, they're all listed here.
I'll make this a little bit bigger. You can look at them if you're curious. I think that there's just a dedicated effort we could do around cleaning up packaging. I think we do a little bit of documentation about what we actually do, and that will clean up and let us, you know, fix a bunch of these.
Tigran Najaryan 00:52:58 What do you want that we do? Like, do you want us to generate canonical bindings, or is it just that we provide instructions on how to do that? What's the… what do you expect here?
Josh Suereth 00:53:11 I think we should document… like, the things we all say in meetings, we should just put in the README, so that someone coming in externally sees it. That's all I want right now. Let's document the state of the world.
Going forward, what I….
Tigran Najaryan 00:53:25 Sorry, I'm not sure I understand. Regarding what? There's a set of protocol files Protobs have the tooling to generate the bindings from those protobu.
Reiley 00:53:35 Product.
Tigran Najaryan 00:53:36 What exactly should we document there?
Josh Suereth 00:53:39 We should document the expectation that you should go to the language SIG to find out the best way to consume these protos for your language, and that we provide a zip package within RAW that you can use as a versioned zip, right?
There's a few things around that package I think we can clean up. One of these pull requests is about dumping a version file in the zip that we generate of what the current version is, so that when you extract a zip, you know the version, like, it's part of the distribution.
that's, like, a simple thing we can do, but, like, consider that zip file of all the .proto files a distribution, a package. So I think we want to move that direction. I'm not suggesting we do that initially, but we can at least just document for people, hey, don't rely on our build tools.
Docker container. Like, don't use it. It's for us, it's not for you.
And talk to language SIGs for how to consume, or consume the zip directly and generate that one. Some of these are, like.
There are ways for you to zip up proto-files and send them in a language-specific manner, where you actually don't distribute the generated code, you distribute the proto-files in a zip file.
Java actually allows this, and Maven somehow, and you can do that in, I can't remember if it was Ruby or some other… language that I'm not as comfortable with also had that capability. Oh, Node, it was Node. You can package them in NPM and fire them as a node module, and then you can actually generate definitions from that node module.
So, I don't know if we want to support that kind of distribution.
at a minimum, I say we just clean up our zip to have less junk in it, and to be, to maybe have a version file, right?
Tigran Najaryan 00:55:20 We don't have a build process there, essentially, just packages, whatever there is, right?
Josh Suereth 00:55:25 Yep.
Yep, and so we document what we have today, we take all of these.
issues, and basically make a meta-issue that says, clean up the packaging of Protos.
and we put them all as, like, dependencies underneath. That's what I'm proposing for that.
… Okay, the other theme was actually around metrics-related things that we left for later.
If you look, I have metric-related cleanups and things. This is actually, something we tell people all the time, but looking through the issues, we might not tell them in the right places. But whether or not an int… time series can become a double, and whether you should depend on that. Histograms handling negative measurements, that's something we deferred. Better metric descriptions, this is just a cleanup. More confusion around int and double, and then, some multivariate metric kind of questions, right? How do we… how do we send metrics in aggregate? So this is where I think bundling all these together into a project proposal where we can decide when to execute on the project, but give a clear signal that we are not doing this work anytime soon until that project is greenlit.
That's all I'm asking for here. I'm not saying we do it now, I'm saying we bundle it.
Put it in a bucket and say, we'll do it later, right?
And here's… here's the project to propose and get behind if you want to do it.
… there's a… there's some documentation… documentation clarity things that I think are cleanups. If anyone has time, I think these are somewhat easier to fix.
things we could do in Protos. There's, so these are things I think we can actively do as, like, little one-offs. They don't take a lot of time. I put them in a bundle. And then there's a little bit of best practice. This is about how to consume Proto. This one, I wasn't sure if I should put in the packaging or not.
….
Reiley 00:57:17 Yeah, so….
Josh Suereth 00:57:20 That's the key.
three things there that I kind of want to discuss. I think this proto-packaging thing is something we should actively do a little bit of work in documenting.
what we believe, what we think, how people should consume it, because there's some confusion in there with how people engage, and I think that's still a problem.
… The last bit is just minor features.
… having a sample flag on span, I think we can actually just close that, because we have all the flags on span now. This is before trace flags existed.
I may have already closed that one, by the way, I don't remember. Partial retry capabilities, should the protocol allow partial retries? So, since it allows partial success, should we also allow you to partially retry, a batch of things with all the items that failed instead of the entire batch?
That's a thing that people ask for. That's actually a pretty big feature that we could either What I'm asking for now is we say either we will absolutely not do it, or this needs a sponsored project behind it.
Tigran Najaryan 00:58:26 With a bunch of these issues, there was an initial discussion, and then it kind of… Went quiet, right?
Josh Suereth 00:58:34 It is a gift.
Tigran Najaryan 00:58:35 It feels like… like, there is no clear… Puff forward, or there's no… No person who moved… moved it forward.
I think, in some cases, we need to make some hard decisions here and just close the issue, right? We don't know how to solve it, there's no one who can solve it, we close it.
Josh Suereth 00:58:54 Yeah, half of the… if we want to say to these features, we're going to close until there's a sponsor willing to drive it, I'm totally fine with that. What I want to do is kind of be clear to them, and since we don't have a formal triage process in Proto, I just wanted to kind of… it was only 36, I had some time, I was tired of doing some of the.
Tigran Najaryan 00:59:13 No, no.
Josh Suereth 00:59:13 Oh, yes.
Tigran Najaryan 00:59:14 There's not a ton of open things, yeah, I agree, yeah.
Josh Suereth 00:59:17 Yeah. Okay, go ahead, Riley.
Reiley 00:59:19 Yeah, I really appreciate your effort, Josh. My question is, if you look at the activities in the past 12 months.
I think, for example, if you look at, like, what Riley is doing on the protocol repo, I was just helping people to approve and merge something. I'm not actively contributing. I probably haven't sent a lot of PRs to update the protocol, and if you look at the history, Tigran is the most active one.
And Josh, sometimes you help, so I feel like Carlos probably is in the same spot as me, and you can… you can see, like, many other team members are the same, so I… I, I feel… like, either we can say we expect all the TC members to be very actively maintaining the protocol repo, then, of course, like, I have to do extra thing, which I'm… I'm fine doing.
But if we can say, like, right, you should spend more folks helping on the security side, maybe spend your time, like, redirecting metrics phase two, and we'll have the problem maintainers. Like, recently, I updated the… the… the groups in GitHub, and I screwed up, so I… now that's fixed. But now we have the formal, maintainers for Prodho and approvers for Prodho.
I want to understand, like, what folks think here. Do we want to, for example, remove Riley from the pro-home antennares, and… and add someone who's not a TC member to the pro-home antenna?
so we can… we can have the product, like, in good hands, or we want to ask, like, riders to spend more time on Prohore. So, what do we think here?
Tigran Najaryan 01:00:47 So, when you remove profiling.
from the, I guess, one consideration, because profiling is actively being worked on by the profiling maintainers.
there's almost nothing there that happens on the protorepository. The only, maybe, significant change that has been happening recently is the change in the attribute values that Robert was driving, primarily.
I can't remember anything else, to be honest, right? Outside of profiling and that.
So I don't know if there is a need for… Significant continuous maintenance for… on this repository.
So, your question of, do we need, like, more maintainers, more dedicated maintainers, I think the answer is no. What Josh is bringing up here, these are, like, years-old issues that we just… either close or do something about it. It's not like we're accumulating this at the rate of 10 per day. These are maybe 10 per year, right?
Josh Suereth 01:01:51 Yep.
Tigran Najaryan 01:01:52 not very difficult to deal with. We just… we just decided that we're not closing the issues because we don't have a solution. I think we just need to make the opposite decision. If the issue is open for many months, and nothing is happening there, and nobody is driving it, there's no clear solution, we just close it.
For that, I don't feel like we need….
Reiley 01:02:11 expert maintainers on this repository.
Josh Suereth 01:02:14 So….
Reiley 01:02:15 I hear you. So, I have a really quick question. So, Tigran, I remember you mentioned that you want to give some proposal about a more efficient protocol.
And I also know the Hotel Arrow Project, which I'm sponsoring.
They have a… a different protocol that's more focusing on the columnar encoding. So, do you think these are, like, separate projects and should have different people there, or at some point you want to combine this? This is just the general protocol, it's not just the Google protocol buff definition for the existing OTLP.
Tigran Najaryan 01:02:49 So, for that, I'm working on that myself, personally. I have been in discussions with, with Hotel Aero folks with that.
What I have is, I don't think, is ready to be pushed as any sort of replacement or second version of protocol.
to OpenTelemetry. The staff thing, right? I'm working on that. It's sort of… I consider it an experimental project.
Reiley 01:03:16 Okay.
Tigran Najaryan 01:03:16 There is an experimental implementation in the collector. That is work in progress at some point. The answer to your question is maybe I can make that proposal. I don't feel like I'm there yet.
But I… I think we'll continue working with, with both, Josh McD and with Laurent on this thing, and maybe at some point it will become a thing.
Josh Suereth 01:03:39 Okay. We're out of time, yeah. I just wanna, to Tigrin's point, like, if you look here, we only have 10 open. One is from 2021, and I feel like we should just close it. So maybe what… the AI we can do… I'll work with Tigrin on the minor cleanups here.
these things, and just… he and I, I'll sync with you, Tigrin, I'll send you some PRs, you and I can knock these out real quickly.
The feature ones, I'll put into the TC chat with a proposal of, like, hey, I think we should just reject this because no one's pushing it. I think this one we should put needs sponsor, because we actually probably still want to do it, but we would need someone to sponsor it, and that's our current technique.
Or we just close all of them, I'm fine, but I'll put those in TC Chat. So, the minor cleanups that I can look at, we'll look at the packaging thing together, too, and the rest of this, anything vague, we'll put on TC Chat. Does that sound good?
Tigran Najaryan 01:04:29 Yeah, yeah, especially the feature requests, the old ones that don't have much support, like, they are not highly upvoted, we should just close them. Nobody needs that.
It's a 3-year-old feature request.
Literally no upflows. Who cares, right? I'm gonna close it.
Josh Suereth 01:04:46 507… 507's interesting. I don't think it's as needed as it used to be. It's basically, we don't really support Zipkin or Apache Skywalking features. They're things that they can't do through our protocol.
But it's been 5 years, and it hasn't been escalated.
Tigran Najaryan 01:05:00 Who cares at this point, yeah.
Josh Suereth 01:05:02 Exactly.
Reiley 01:05:04 Cool.
Josh Suereth 01:05:05 Alright.
Okay, thank you, guys.
Tigran Najaryan 01:05:08 Bye.
Reiley 01:05:10 Good, bye.
