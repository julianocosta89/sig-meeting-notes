SIG: Python SIG
Date: 2026-06-25
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Riccardo Magliocchetti 00:02:55 Hello.
Marcelo Trylesinski 00:02:59 Hello.
Riccardo Magliocchetti 00:04:18 Welcome to this week's Pythonship Call. We are waiting a few more minutes for more people to join.
In the meantime, please add yourself as an attendee.
to the sign notes… And also, she wants to discuss any topic.
If, if you're free to add them as well.
Will… Will people think we can start?
Welcome again.
Tammy, do we want to do the triage? Do you want to share?
Tammy Baylis 00:05:59 Hello, yes please.
Dope, work, digest, cool.
Okay, let's timebox this until, 9, 10 Pacific?
Go status. We ignore the chore and build bot bump PRs.
Instead, we want to look at, contributor-generated PRs, so… Last month, Clear Open Census Execution context.
Did we talk about this, right?
Okay, so last week, I think Carlos attended the call and mentioned that Open Census is being deprecated.
So I'm gonna close this one.
And that's done, cool.
Riccardo Magliocchetti 00:07:27 Yeah, Tammy, while at it, we should probably also close the issue.
Tammy Baylis 00:07:31 Oh.
Riccardo Magliocchetti 00:07:32 We can avoid other people opening the very same PR.
Yeah.
Tammy Baylis 00:07:36 Thank you.
Thanks, Ricardo.
Update OTELIO Cookbook with common view scenarios.
But why is it here? Hmm…
Aaron Abbott 00:08:10 you know, I think this issue predates the, openTelemetry.io docsplit thing.
And… this looks like… Some kind of, you know, agent contribution, so…
Tammy Baylis 00:08:26 And it's stale already.
Aaron Abbott 00:08:28 Yeah, did the, PR go to, like.
Did it add new docs? What… I'm kind of curious what it did.
Tammy Baylis 00:08:40 What? Oh.
Disabled?
Aaron Abbott 00:08:50 Yeah, I think we could just ask them to create it against the OpenTelemetry I.O, and I can… I can drop a link, G63. I can… Reply on this one with a link to the… Actual cookbook, if they want to add it there.
Tammy Baylis 00:09:06 Okay, yeah, if you could do that to the PR, that'd be great. I'll comment on the issue here.
Aaron Abbott 00:09:16 Yeah, actually, if you can paste it here… That's the… Actual thing they should probably update if they feel like doing this.
Tammy Baylis 00:09:25 Sorry, can't find the chat. There we go.
Thank you.
Show me to update this instead.
I'll close this.
Alright, as well, just do that here.
Okay.
And that is done now. Thanks, Erin. Two more minutes.
Confluent Kafka, get outer delegation to proxy Producer, and… Hmm… Fixes this issue… Earlier this year… Segfault, oh dear.
Okay, so we've had some eyes on this already… Oh, an earlier attempt.
Say this is ready… Review, and… Code should be okay, I'll just approve work closing that.
Should, I think, unstale this.
Update branch.
Riccardo Magliocchetti 00:11:08 I think, I've opened a related, issue. Sometimes I go when looking at, confident CAF instrumentation.
what I was suggesting, too, instead of creating this proxy object.
Try to use, RAPT instead.
Tammy Baylis 00:11:28 Okay.
Riccardo Magliocchetti 00:11:29 Yeah, yeah, like, it's for teacher certificates.
Yeah.
But yeah, like, I can take a look.
Tammy Baylis 00:11:38 Thank you.
Okay, one more minute, oh, another closed one, I think because I suspect someone deleted their fork.
Yeah… Removed from board… I thought removed from board.
Oops.
Okay.
We will call that… Time for today.
Back to you. Thanks, Tammy. Thank you.
Riccardo Magliocchetti 00:12:35 Next time, ma'am.
So… Okay.
Thanks to the people, right?
Listed what they were working on this week.
I've declared the config for Mike, JSON and Jaron Exporter work, and process context for Lucas.
And Greg, the HTTPX instrument, or added to the HTTPX instrumentation.
So, to the topics. Marcelo, you're first.
Marcelo Trylesinski 00:13:08 Yes.
So, can we… like, I find it very hard to read the code source. Can we change the… I've opened this issue, I think, a year or two years ago, maybe 3 years ago? A year ago. Oh, good. So, can… like, if… nowadays it's very easy for, Well, rebase… pull requests, so it doesn't bother anyone. At the time, I think there was a… the bad side of doing this was because it would annoy everybody.
But nowadays, it is still annoying, but you can just point cloud to fix it.
Aaron was on board. Aaron, say something positive, please.
Aaron Abbott 00:13:51 Yeah, I think there's this git revs file that we can use. I… I don't have, like, a super strong opinion here, I think… Like, yeah, it's definitely easier to rebase the… 82 open pull requests if we need to, but… Yeah, I don't know, I think it's kind of like an opinion-based thing, I'm curious what other people think.
Riccardo Magliocchetti 00:14:22 I prefer 120, to be honest.
Diego, you have your hand raised.
Diego Hurtado Pimentel 00:14:27 I do have a strong opinion here.
I want it to be 80, I don't know if… It is like that, It's just because I have a really small laptop, 14 inches, and I like to split it in half, but, Years ago, I would have fought for this with A lot more energy now that… there is AI, right? And we don't read code that much. I'm fine with… Any length, I guess.
Marcelo Trylesinski 00:15:05 Amazing! So, 4 positives.
Aaron Abbott 00:15:12 Yeah, I mean, I'm not doing much, 80… 80 column… editing in VIM these days either, so, I think I'm generally in favor.
yeah.
Marcelo Trylesinski 00:15:31 So, can I open up a request and then… Ping people?
Aaron Abbott 00:15:36 Yeah, I mean, maybe… Would it be okay to, like… I don't know, I'm not hearing any dissent. There's the issue, but there's not really a lot of comments, I think, just me and you, Marcelo.
Marcelo Trylesinski 00:15:52 But yeah, I…
Aaron Abbott 00:15:56 I don't know, Ricardo, what do you think? Are you okay to just go ahead with it?
Riccardo Magliocchetti 00:16:00 Yeah, like, usually I use 120 on my code, so… But, like, like, up to now, like, I haven't felt any issues.
Working with, open telemetry limits.
So, like… I don't have a strong opinion, but… On the 120 is fine for me.
Mike Goldsmith 00:16:30 I'm good with 122, I think it's… It makes it easier for most people who actually care about it, if you're not using an agent, so go for it.
Aaron Abbott 00:16:39 Bill.
Marcelo Trylesinski 00:16:41 Amazing. Thank you.
Riccardo Magliocchetti 00:16:42 Yeah, like, maybe you can give it a try, open a PR, and so we can see… How much code will change?
Marcelo Trylesinski 00:16:52 I mean, I can already tell you it's gonna be a lot. Is that a negative side? Like, I mean, it's gonna change the limits, so it's gonna change most of the code stores.
If that's… if that's… if that's gonna prove anything negative, then… You know?
Liudmila Molkova 00:17:12 Let's just merge it right away, so that this pull request wouldn't need to be rebased all the time.
Aaron Abbott 00:17:23 Cool, sounds good, and yeah, sorry… sorry, everybody, in advance for having to rebake here.
But I guess, yeah, sounds good. Thanks, Marcella.
Marcelo Trylesinski 00:17:36 Alright, thank you.
Riccardo Magliocchetti 00:17:41 Next, next topic is from Diego.
Diego Hurtado Pimentel 00:17:47 Right, so… oh, oh, that one's… I was thinking about either.
Yeah, so, I think last week I… I… I mentioned that we could start discussing using AI to help us with the review process, and I think we agreed on me opening an issue so that we can kind of brainstorm other ideas. So I… Opening it, I added a few… ideas I have myself. Please take a look. If you also have ideas, some folks have already added their own ideas, please add them there. I am very interested in reading what you all think. I think this can be a great opportunity to make, To make this, project move forward a little bit faster. So yeah, please take a look, at what you think, and I'll be reading everything you write. Thank you.
Riccardo Magliocchetti 00:18:59 Thank you. Any comments?
Marcelo Trylesinski 00:19:04 Is it, is it helpful… sorry.
Riccardo Magliocchetti 00:19:06 No, please go ahead.
Marcelo Trylesinski 00:19:08 Is it helpful to share the experience with code reviewers?
Diego Hurtado Pimentel 00:19:11 It is, helpful, yes, but I also would encourage you to write it down there in the issue, so that it gets all in the same place.
Marcelo Trylesinski 00:19:25 Okay.
Riccardo Magliocchetti 00:19:35 Okay.
So, yeah, like, maybe we can work on this fly?
Thank you, Diego, again, for finding this.
Next one is from Mike.
Mike Goldsmith 00:19:52 Yeah, hello everyone.
So we've been doing a lot of work on declarative config, and we, in the last release, we made it so that the… Autel file path environment variable can be read, and then activate the SDK configuration based on that environment being set. As part of the declarative config spec, we should also offer a programmatic option to do that. It is available, but it's currently in a private module, so it's underscore configuration. I opened this PR to make it a public.
component, a public module.
with to basically talk about whether we want to do that now, or do we want to move it into a different module, like a different, yeah, a different package, so it can be imported separately. I'm… I feel as though that we should probably make it as part of the core SDK, just because if you don't include it, and then the path to use the config is then broken, even for environment variable options. So, right now, it's always available, so the environment variable Will just work, where moving it into a separate package would require them to know that they need that, and then have a fallback for when it's not.
if we feel as though that we don't want to make this public yet, we could probably just leave it as a private package, a private module. But yeah, it just feels as though, like, open the conversation is like, do we want to leave it where it is? Do we want to make it public? Do we want to move it somewhere else? Because I think this is one of the last… bigger things that we need to solve before we can say that we've got a good… we've got, like, a baseline, implementation of the declarative config.
Yeah, go ahead, Lucas.
Lukas 00:21:38 Yeah, I'm not, like… I think I originally suggested maybe moving it into a different package, and I don't think it's, like, too much to ask to install it, because, like, chances are you're probably gonna also need to install, like, some of the additional packages that you'll need, right, for, like, any of the exporters that you use. But yeah, I'm, like, curious what other people think there.
Michele Mancioppi 00:22:00 I can tell you from the point of view of the injector and the system packages sig.
It's a slam dunk for us to include it in, in the list of packages that we would inject, right away in SDKs and applications.
Mike Goldsmith 00:22:14 Okay.
Michele Mancioppi 00:22:15 It's a slam dunk. We're also the OpenTelem operator.
Jacob Aronov is working on, Making the next version of automatic injection based on the open territory injector, and this is part of the vision.
Okay. I have a, I have a ques… I have a couple of, pleas.
for you folks. One is, there is an… a set of, configurations in the… The quality configuration schema, which are currently experimental, that allow language overrides.
That would really, really, really help us in the system packages to avoid having to create one configuration file per language.
At the moment, those options are experimental, because not enough SDKs implemented.
I, if we could actually have more implementations of that to make it something stable, and then we can assume that the SDKs will implement it, that would be a great improvement.
And, the second thing, we have in the system packages SIG, a, first version of, APT and DBM packages that, that install, at the moment is java.net.
And, Node.js, Python is going to be the next. If somebody from the, the SIG would like to, collaborate.
And, because there are a few product decisions to be had there, for example, which instrumentation is out of the box, the declarative configuration.
That would be great.
Mike Goldsmith 00:24:00 Yeah, I think that's fair, I think… the… the goal of getting the config to what I would call as, like, a usable state doesn't include everything in the spec, because the spec is quite a lot of things in there, and as you said, there's a lot of experimental things still in there. I would like to see if you feel as though that the… the language overrides is a particular thing that we do want to include, then, we should definitely track that as, like, the community interest in supporting that feature.
And for the, the… or adding the Python to… was it the… the injector? The new version of the injector?
Michele Mancioppi 00:24:36 So the injector already has support for Python, but the injector doesn't have, like, the operator and image. In the system packages, we are building Debian and RPM packages for… it's the equivalent of the images that the collector has.
And, Python is up next.
Mike Goldsmith 00:24:54 Okay, yeah, I'd be happy to help work on that as well. I've driven a lot of this declarative config stuff, so I'm happy to help with that too. Go ahead, Ricardo.
Michele Mancioppi 00:25:03 Python support by end of the week, and then ping you.
Mike Goldsmith 00:25:06 Great, thank you.
Riccardo Magliocchetti 00:25:08 Yeah, I was going to add the Michaelb.
Please open an issue, maybe, and link it from the tracking issue.
we are, we are using for tracking the deciding config work Mike is doing.
And… yeah.
Aaron Abbott 00:25:28 Yeah, I don't know if I actually caught the answer, but, like, is the environment variable not sufficient for the injector? Like, you need to use the actual API?
Michele Mancioppi 00:25:39 The, the injector is fine. The injector uses the site customized trick and Python path.
The problem is, in, system packages.
So, when you, when you deploy applications directly on a Linux host, people do not configure the environment.
They are, at least it's very cumbersome. It's very difficult to find people that write really complex system D units, for example.
In that case, the declarative configuration is fantastic, because you just… you just put the file in HTC OpenTelemetry slash Python, and then all the applications that, all the Python applications that you want instrumented, they will automatically configure that way in a consistent fashion.
Aaron Abbott 00:26:28 Okay, and then, so do you, I guess, do you use the site customize file to point it automatically at Etsy? Okay, I see.
Michele Mancioppi 00:26:38 No, the customizer is there to avoid, for example, injecting Python 2.7, and currently, to prevent injecting into applications that are running gRPC. Diego did the next bit, it's Diego explaining you what you want to do about it.
The, the injector today does not set the environmental for the decarity configuration, but that would come within the system packages.
the configuration to add it. The injector can add environment variables.
To the, to the, processes it injects. It's something that you obtain via a configuration file.
Aaron Abbott 00:27:22 Okay.
Mike, did you… did you get all that? Like, do you feel like,
Mike Goldsmith 00:27:28 I won't say that I understand all of it, but I think I know enough to, to engage, and we can have the conversation, but figure it all out.
Yeah, I think that's fine. So, jumping back to the original topic of where we think it is, if we feel as though that it's fine to put it into a new module.
Is that where we landed with that?
Riccardo Magliocchetti 00:27:53 I'm not sure, but, like, for me, like, before making things public, I would really like to give it a try.
Like, now we have a release.
Like, does the thing from a user point of view more easily?
So yeah, I would really like to give it a try before… They're selling on the antennas.
Mike Goldsmith 00:28:16 Okay.
Aaron Abbott 00:28:20 Well, I mean, I think one of the questions was if it should live in this SDK package, or if it should be in its own package, and if it's separate, then it's, You know, versioned independently also, and we don't have to deal with the… I don't know, I guess we could have a public API and then mark it unstable versus the assumption in the SDK is, if it's there, it's just gonna be, People are gonna see it as stable, right?
Mike Goldsmith 00:28:45 Right.
Yeah. Yeah, I think moving it to a separate package and then just expecting people to have to install it alongside the SDK is probably a normal pattern we expect people to do for all of the extra things. I think if you just installed the SDK, you probably wouldn't have a good experience with Python anyway.
Aaron Abbott 00:29:04 Yeah, no, I mean, I think… I'm actually curious what other languages do, like, if they have separate packages, or if they're just included in the SDK. I feel like it is kind of nice that if you just used it, you could set the environment variable, and you run your Python code, or your, you know, Kubernetes manifest, or whatever, and it just works, but… like, I remember there were downsides for… for example, like, lambda startup times, because there's a bunch of generated code. I don't know if it would be in the hot path, we can obviously do some lazy imports and stuff like that to mitigate it, but… Yeah, I guess the main concerns are, like, stability, and then just the size of the… loading the size of the SDK package.
Mike Goldsmith 00:29:44 Yeah.
carlosalberto 00:29:44 By the way, the Java one has it as a separate package, for example.
Mike Goldsmith 00:29:51 Yeah, JS has got it as a configuration package, too, so you do have to install it separately.
Lukas 00:30:08 Yeah, I would be in favor of moving it to a separate package, just, like, working with… I mean… the Lambda use case is, like, 1. Like, even with the lazy imports, it's still gonna add to the… your overall artifact size, so… And it seems like… Yeah, Java, it seems like if the other languages are doing it that way, we should probably do it that way? I don't know. And yeah, again, like.
I don't know if we have, like… We could maybe create, like, a package that just has everything, like.
kitchen sink, everything. I know we have, like, the contrib one that does all the instrumentation packages, but maybe we could have different, Maybe it could be just, like, we could add, optional extras on the SDK or something?
Mike Goldsmith 00:30:52 That would just…
Lukas 00:30:53 automatically install, like, configuration, but again, you'll still need your exporters, so you'll need to set that up and everything, so, yeah, I don't think… I don't… I can't see too many downsides of separating it out.
And that there is definitely some upside, so…
Michele Mancioppi 00:31:10 Bob?
Mike Goldsmith 00:31:11 Yeah.
Michele Mancioppi 00:31:12 If I may interject, the, Effectively curating a distro with instrumentations that are table stakes for Python and resource detectors.
That helps a lot in system packages, and the Open Talent Reparator as well.
Because right now, the kind of… the amount of packages that are being installed, it's effectively a… separate curated list by the OpenTrange operator that I understand does not get so much input from this SIG.
And ideally, we should agree on what kind of things get automatically injected.
Mike Goldsmith 00:31:51 Oh, so, like, default extras that we think that you should install alongside the SDK, and we can have a curated list of that.
Michele Mancioppi 00:31:58 Absolutely. And because automatic injection without automatic instrumentation is pointless, and automatic instrumentation without excellent resource detection is very sad.
Mike Goldsmith 00:32:11 No.
Okay, yeah, I think I'm happy with that decision, then we'll move it into a separate package, and then, we should definitely open an issue to see if we get, like, a default Recommended install that includes the configuration plus exporters and things like that.
Aaron Abbott 00:32:30 Mike, there's one more question in chat I was just gonna call out. I don't know if you saw it, but Ludmil asked, is the API part of the configuration, still part of the API package?
Mike Goldsmith 00:32:42 I think because the… it's all currently in the SDK, we probably should separate it, so the API still lives in the SDK, and then all of the extra stuff goes into a new module.
Liudmila Molkova 00:32:54 No, I mean, there is the instrumentation API. Like, when you… there is a part of configuration that's API only.
This thing should leave an API, I think, because… It's just crazy to have multiple API packages.
Mike Goldsmith 00:33:11 Right.
Yeah, yeah, I think the, yeah, I, yeah, I agree.
Riccardo Magliocchetti 00:33:31 Okay, any other comment?
And let's move to the next topic. Diego, save or a cell from Portabuff.
Diego Hurtado Pimentel 00:33:44 Yes, so… Well, we all know that Python has this problem that, If we have a dependency in OpenTelemetry.
That can come… that will come in direct conflict with, any dependency that the application has, right? So, we always have this… problem, and we… We're having the same problem with the injector, so after considering several solutions.
We decided to try and implement protocol for ourselves.
Which is, pretty crazy, but, it works, so… I guess it's not that bad then. We made an implementation, a pure Python implementation of Protobf.
that is, produces the same results, byte by… byte, and, then we replicated the… maybe I can share my screen.
Here will hear the… I just had a terrible experience sharing screens. Try again.
The… One, three… Here.
So… So I have this branch in my fork.
And, What we're doing here is that we had a continuummitted portal, right? The portal of dependencies right here. So, we replicated this, package.
And… inside… There is, Code that replicates everything that, Opportunity Product does, And we also have… this… by portable.
Package here that does everything that Protog those, convenient.
When it comes to bytes, right? So… For example, we have, conclude here.
So, There's something in the way, and I cannot click the file that I want to show you, but it doesn't matter.
For example, for scholars, the… You sign into her, signing tours, everything.
It's, implemented here, and we have test cases that, com… that use the, The actual protocol of implementation?
We took a look at here… You can see that, Yeah, Protob is a dependency… is a test dependency of this package, because we use Protob.
to, compare the results that this implementation does, and same thing. So, it is, we're doing this Not only to create a item paragraph package, but to also replicate the… Hearing exporter… this, PyProto Common package.
And also, to implement this PyProtoHTTP exporter, which is the same thing as the proto-HTTP exporter, but using this PIP protocol of implementation. We also tested it out, produced the same telemetry.
traces, logs, and metrics. So, I think having this in this repo could be useful for, pretty much any situation where we have Trouble, because, we have this dependency that many other projects use.
So, I wanted to present this to you.
And, wanted to know, what do you think?
I'll step short of my end.
Aaron Abbott 00:38:14 Yeah, I just wanted to call out, so, we've been working on… over the last couple months, we've been working on a pure Python ProtoJSON.
Exporter?
And I'm wondering, like, I think that could probably solve most of the use cases we have here. Is there a reason to use Purdabuff over JSON?
when they're both available, if you're just trying to solve the issue of dependency conflicts, or… I think there's also ABI issues as well, right?
Diego Hurtado Pimentel 00:38:42 Yeah, we want to, yes, we're aware that we're trying to use JSON first, and actually we did, thanks to Lucas' efforts.
This, adding this is not in conflict with, having JSON, and, this could be, in theory, These screens here, we have a better performance.
Not, because, of course, we're producing less bytes.
The Python implementation is something that we are… we just tried first, like, implementing this in Python, but, another possibility will be to, implement this, in C or in Rust, to make it even more performant, right? So, performance will be the answer to your question, Aaron.
Michele Mancioppi 00:39:36 The, AutoP JSON exporter is a great idea.
It's also not… the default, encoding of other SDKs.
So, for users, the possibility of having both, that can be automatically injected, this would be, That'll be good.
Aaron Abbott 00:39:59 Could you say more? Is it… is it because, like, you're saying, like, a collector might not… pre-set up to accept JSON, or…
Michele Mancioppi 00:40:06 Not really, but for example, when you think about, one declarative configuration for multiple languages in the system packages.
the, been able to use either.
across all the various SDKs.
That would remove so much confusion from the users.
They would just set HTTP protobuf or HTTP JSON, they're done.
Aaron Abbott 00:40:35 I think… I remember there was, like, some discussion in the spec seg where… I think they said SIGs may choose their own default, or something like that.
Michele Mancioppi 00:40:44 Yes.
Aaron Abbott 00:40:45 In the declarative config, are you able to just say, like, OTLP, give me whatever, doesn't matter?
Michele Mancioppi 00:40:53 No, because in many implementations, the way that you specify the endpoint for protobar for gRPC is syntactically different than the one for HTTP JSON.
for example, in, I think, actually, Python's one of them.
If you're, in, gRPC, set HTTP as a protocol, then it explodes.
So, having one endpoint configured in one way.
will not work reliably if different SDKs are trying to use different encodings for developing.
Aaron Abbott 00:41:31 Okay, yeah. I think, just for, like, context of my… view of this, it would be nice to avoid the complexity of, like, another implementation, especially one that implements, like, the, you know, vertical encoding from scratch.
I… I kind of wonder if we could fix this in the declarative config, because… you know, like, fixing it in Python is one thing, but there's also, you know, JS and other places where.
Michele Mancioppi 00:41:56 Jazz and the other languages do not have an issue with using the default OTLP exporter, because other runtimes have class loading or the closures in Node.js. It's in Python that injecting gRPC and protobuf in a different version that your app expats leads to breakage.
Aaron Abbott 00:42:18 Okay.
Liudmila Molkova 00:42:20 the HTTP version of TLP Exporter is the default, but it changed at some point.
And languages that had gRPC by default just kept it.
But some languages switch to HTTP by default. And since declarative config is a greenfield, it might be a good idea then when greenfield… oh, sorry, when Code Declarative config is used, the default as HTTP.
Michele Mancioppi 00:42:55 HTTP protocol for HTTP JSON?
Liudmila Molkova 00:42:59 Oh, HTTP parad above, sorry. And you want HTTP… it doesn't help there, right? Sorry.
Michele Mancioppi 00:43:03 Because Protobuff is the shit.
Liudmila Molkova 00:43:06 Right, yeah.
Aaron Abbott 00:43:07 Is it the issue, though? Because… because can't you send… protobuf or JSON, and the only difference is the headers you send, like, the way you specify the protocol is exactly the same, no?
Michele Mancioppi 00:43:17 The headers are different, the endpoint in the collector is the same on over HTTP.
I'm not sure about whether the way that you specified URL is the same, to be honest, across the languages.
Aaron Abbott 00:43:36 I… I want to say it is, but I… we can definitely double-check.
Michele Mancioppi 00:43:43 I mean, all in all, I can tell you that the current OTLP exporter for gRPC or HTTP protobuf It's not injectable safely. It breaks applications.
Aaron Abbott 00:43:59 Lucas, do you wanna say something?
Lukas 00:44:02 Oh yeah, I just wanted to bring up… I think we discussed this. We just, we, we definitely discussed this before.
Yeah, the one concern, I think, with the pure Python implementation is the… the performance, so… that's where, yeah, so… I think I shared a POC a little while ago, like, just using, like, a Mature in Rust, but… implementation, but yeah, I guess that's kind of the same thing here, but… I think… So, the way that we generate the… the protobuf… the proto-library, it should be compatible with a very wide range of protobuf versions, at least currently.
So, I guess… maybe I'm not quite understanding exactly what wreckage.
Michele Mancioppi 00:44:59 The issue is the following.
The, the, what we inject through the injector must be self-contained.
Because we have no idea what the application looks like when we start injecting it.
So, we need to ship… gRPC and protobuf as dependencies of the gRPC exporter.
or the protobile for the HTTP exporter.
And if the application that is running in the container, on the Linux host, wherever, already has a different version.
of gRPC and protobuf.
technical.
Lukas 00:45:40 Right, I guess I'm just saying, like, our protot range is, like.
You can use anything from, like, 4.0 to 8, or 7.0.
So I guess, I mean, I guess there's still technically… some great.
Michele Mancioppi 00:45:55 to explain more in detail, maybe at another time, why that doesn't work, not reliably, because ultimately what you do in a sidecaster, in the site, you are going to have one version of JPCN protobuf coming alongside the injector and the Python SDK.
And then that will conflict with whatever else is there. The Python path is pre-painted, because we need to go first.
And then, when the application tries to load the gRPCM protobuff, the application will not have… will not have the compatibility.
the Python SDK has.
Lukas 00:46:29 Okay, yeah, maybe we… yeah, we can discuss it later, but, Yeah, I would, the… I guess my other point is, like, I'd be probably, kind of against, like, if we were to Do something like this, probably against, like, hand-rolling our own thing.
So… I know there are some existing, like, pure… I think there's, like, pure protobuf I looked at, which is, like, an existing Pure Python implementation.
And or… and then the other option, again, would be just using, something like Prost with Rust.
which… which I looked at, I guess the only downside being there is that then we have to build wheels for every architecture and OS.
But then you'd have… you'd have the native performance there.
So, yeah, and I think, yeah, I guess the only remaining question is, like.
it'll be… I guess it's being very confusing for users, having multiple different implementations to choose from, so… I guess that's why, like.
that's the only reason to go against it, so I mean, maybe this could be something that could live in Contrib, or maybe this is, like, an injector-specific thing, like a package that the injector could use itself that just self-contains everything.
Yeah, I guess that, yeah, that's all I have to say here.
Aaron Abbott 00:47:54 Yeah, thank you, thank you, Luis. I think maybe we should call time, but, it sounds like there's, like, a need here. Could… is there already an issue for this, or can we, you know, take the discussion to an issue?
Diego Hurtado Pimentel 00:48:05 I haven't yet opened an issue, yeah.
I can… I can do that, and we can move the discussion there if we are out of time now.
Aaron Abbott 00:48:20 Yeah, I think there's, like, maybe 3 or 4 more, topics, so…
Riccardo Magliocchetti 00:48:28 Yeah, like, I think we… I don't know if you have an issue just for that, but I remember we had some discussion with Lucas I did, is a Rust prototype as well.
So maybe we already have something with them.
Correct.
Anyway… Next topic, also from Lucas.
about adding Rust dependencies, I guess?
Lukas 00:49:01 Yeah, just for some context, and Aaron, I know you know the context here, so… there's an OTEP that recently got approved for process context sharing with, like, the, eBPF profiler?
And it seems like the only way to actually… I mean… you could maybe get this done with a pure Python package, but it would be, very nasty, and, certain, And certain down-the-line features, like thread context, will absolutely require native code.
So, the… so, I think the most straightforward way to approach this is to probably just write a native, package. So… I've gone with Rust just because it seems like the integration with Python and using Maturin is pretty nice. Yeah, I just wanted, like, some maintainer feedback on, like, are we okay with… adding Rust, just for… just for, at least… just for this functionality. This is Linux only, also, I guess I should just mention, so, we just need to build wheels for the… for different, CPU architectures on… Linux, specifically.
Riccardo Magliocchetti 00:50:18 There you go, you have your underrace.
Diego Hurtado Pimentel 00:50:21 Yeah, right, so… I review your PR. I, thank you for putting that, by the way, I am totally okay with having parts of our components written in Rust, or actually in any other language.
as long as there is a good reason to do that. The only thing I asked, and I think you did already, was just to add comments to the codes where it's, like, very heavily commented, so that people who are not familiar with those languages can… Yeah, I understand the code. Actually, using Rust is something that I have in mind, precisely for these, problem of reimplementation, because, of course, it will be even more performant to use lower-level language, so I'm totally okay with MRS. Having to make more wheels, I mean, that's, Yeah, it is… it is a little bit more work, but it's, the… Totally worth it, you know?
So yeah, I'm okay with that.
Aaron Abbott 00:51:39 Yeah, I think… I think I agree with you, Lucas, we need some kind of lower-level language to implement the specs, since it requires, you know, poking around in thread local storage, and I think also the handle for this in Python It's not available in, is not available in a Python API. It's like, I forget exactly what it was, Pyth, like, get a set wall.
Lukas 00:52:02 This actually just does… this doesn't have that yet. This is just… But there's, I mean, you're… you have to, you know, create an MFD file descriptor and do all this other stuff, so it's.
Aaron Abbott 00:52:15 Oh, yeah.
Lukas 00:52:16 I mean, you could maybe do it in Python, but it just… but then once we do the thread context stuff, like, we're gonna end up having to use… for sure, use native code, so…
Aaron Abbott 00:52:25 Yep, I was… I was just gonna say, like, I personally don't have a lot of experience with Rust beyond mostly just, like, rooting it, so… I think Leighton has been kind of involved in the rest of SIG, so it should be fine. Like, we'll have a maintainer who, knows… Rust, which is good, I think the other thing I was gonna say was I also prefer Rust because, if I understand right, like, Maturin makes it really easy to build multi-platform wheels.
And it's pretty well integrated with, like.
existing Python tooling, whereas it could be kind of painful with C++ to get toolchains and stuff like that.
Yeah, it seems… seems good to me.
I guess, Ricardo, go ahead, yeah.
Riccardo Magliocchetti 00:53:12 Just a quick question for Lucas.
This… Otep is for, like, sharing the context to be accessible from the BPF code, right?
Or something else, okay.
Lukas 00:53:29 Or, I mean, it's supposed to be more general, like, any external reader can then just look in the process memory maps and literally grab, like, resources and stuff.
Riccardo Magliocchetti 00:53:40 Like, I remember, like, Trying to solve the same problems a couple years ago.
For the very same reason, I guess. And they tried to read the Python context from eBPF instead.
like, trying to parse the structure that Python uses for the… our own context series, but it was a mess. Anyway, okay.
Lukas 00:54:10 I would recommend, yeah, if you haven't read the OTEP, I would read the OTEP. It's, I think it's a pretty good approach.
Riccardo Magliocchetti 00:54:17 Thanks.
Aaron Abbott 00:54:18 Yeah, I was gonna say, Ricardo, I remember that, and this is more like the process exposes it in a certain format, And you have to install something in the process somehow, which does the exposition. So, I think it should be a little easier. I think the issue is, like, the dictionaries in Python were really difficult to read from Rust, so… Yeah, it sounds good, Lucas. I think one other comment I had was, I wonder if there's, like, a Rust library for this in… just as part of, like, OTEL, since people might have to do… go down to native code for other languages, too, that we could maybe reuse for, like, the… the protobuf part and the thread local storage part, the MMAP part, And then we would just have, like, a Python… wrapper, which uses that as a library, but I don't think it's blocking, we can always revisit that.
Lukas 00:55:06 Got it, yeah.
Riccardo Magliocchetti 00:55:17 Great, thanks.
Next up in VIN, Greg?
Gregory Loshkajian 00:55:22 Yep.
At risk of being a little annoying, but really trying not to be as… like, this is my first contribution, so I just wanted to check if there was anything else I should be doing for this beyond just addressing anything Marcelo has in mind as he looks at it.
That… that's… that's really all I wanted to check in on, because I know Lucas has looked at it a little bit, and… I totally get, like, asynchronous feedback. Just… Want to be sure there's nothing else immediately that I should be doing.
Riccardo Magliocchetti 00:56:01 I don't think so. Like, usually, like, with just a view.
And discuss comments, and when you're fine, we approve a match, so… if, like, if we want something for you, we'll be explicit… explicit about that. Don't worry, like…
Gregory Loshkajian 00:56:19 Yeah, no, I'm not asking… I'm not asking for you to prioritize me or anything.
just… I'm newer to the process, so I'm just trying to understand if… like, what the signal is that, like, I really need to be doing more, because I see, like, it's a lot of, like, comments, so it's… so, like, it's not immediate to me, like, what's blocking.
Marcelo Trylesinski 00:56:42 I think… didn't I add one last comment?
Gregory Loshkajian 00:56:44 You, you, you did, you did, and I'm… and I'm looking into that.
Marcelo Trylesinski 00:56:48 Okay, thanks. Yeah, but because I think on the type checker, that doesn't work.
Gregory Loshkajian 00:56:53 Yeah, I mean, I also noticed that on the type checker, HTTPX isn't even on the type checker?
Marcelo Trylesinski 00:56:59 Wow, that's why! Yeah. So… Okay, that makes sense.
Gregory Loshkajian 00:57:04 There's a lot of things that aren't on the type checker by default, actually. I didn't really know what to do with that, and I don't… know if it should be in my scope to fix that, but, like, I'll take whatever feedback makes sense.
Aaron Abbott 00:57:22 Are you talking about the talks… the talks environment, Gregory, for this one?
Gregory Loshkajian 00:57:27 What?
Marcelo Trylesinski 00:57:28 I'm typing it, yeah.
Okay. I think he's just saying that, some packages are excluded from the type checker.
Gregory Loshkajian 00:57:36 for talks, I think. Like, there's… there's, like, a list of… packages that are specifically invoked for the type checker, and I don't think HTTPX is in it.
Lukas 00:57:47 Yeah, we've been moving, like, originally, I guess, I don't know the full context, but, like, not all of them, yeah, you're right, not all of them have type checking. We've been trying to gradually… so, I mean, if you want, you can try adding it, but I would maybe leave that to another PR to add the type checking.
Gregory Loshkajian 00:58:03 Yeah, that's…
Lukas 00:58:04 The proper type checking.
So… Yeah, yeah, just to comment on the PR, yeah, I think it's, I think it's, like, a good… good approach. It's a little bit messy, but, I think this is preferable to just duplicating the entire package, because there is… it would be, like, well over a thousand lines duplicated, which is a pain to maintain. And yeah, the other thing is, like, we just have a lot of PRs, so…
Gregory Loshkajian 00:58:31 No, no, no, no worries.
Lukas 00:58:32 I would expect, like.
A few weeks, but yeah, as long as you have all the comments resolved, it should be good.
Gregory Loshkajian 00:58:40 Okay. Yeah, no, that's… that's totally fine.
Yeah, if at any point you see any mess that feels, like, non… That feels, like, not… that feels reducible, instead of, like, not like a result of, like, trying to squash everything into… into the single repo, like, I'm happy to take those comments. I'll work on things as I see it.
Marcelo Trylesinski 00:59:12 Wouldn't it?
Riccardo Magliocchetti 00:59:13 Working on that, yeah.
Marcel, we have 3 minutes, and we have another topic, but…
Marcelo Trylesinski 00:59:20 When is the last… when is the next release?
Riccardo Magliocchetti 00:59:24 Next month.
Marcelo Trylesinski 00:59:26 Okay, well, then we have time.
Riccardo Magliocchetti 00:59:32 Okay, thank you.
Gregory Loshkajian 00:59:34 gap.
Totally fine. Thank you so much.
Riccardo Magliocchetti 00:59:38 Thank you.
Toria, for you.
on this, Sam.
Surya Teja 00:59:44 Me.
Riccardo Magliocchetti 00:59:45 Yeah.
Surya Teja 00:59:46 Yeah, hi. I have been looking into CPP OTL core repository and saw that they have two issues for implementing these two samplers. I could not dig into the Python codebase, so I just thought.
If we need to add these two samplers into our Python, Codebase, since it is still development, I'm not sure.
what… Or which path SIG is leaning towards.
Riccardo Magliocchetti 01:00:18 We already have the composite one.
It's inside the experimental samplers.
I think. Oh. Inside the SDK somewhere.
I don't think we had a probability.
Surya Teja 01:00:34 Okay… Cool. So, if, we can add this, can I go ahead and, open a show and adding it?
Riccardo Magliocchetti 01:00:46 Yes.
Surya Teja 01:00:46 off.
Riccardo Magliocchetti 01:00:47 First, please open an issue first, thanks.
Surya Teja 01:00:49 Yeah, cool.
Sure.
Thank you.
Riccardo Magliocchetti 01:01:00 Yeah.
Take a look at this directory.
Surya Teja 01:01:11 Cool, thanks, Segaro. I'll open up a beer.
And of tissue soil.
Riccardo Magliocchetti 01:01:18 Thanks.
Surya Teja 01:01:20 Thank you.
Aaron Abbott 01:01:23 Alright.
You did it. Hit through.
Riccardo Magliocchetti 01:01:27 Bye.
Aaron Abbott 01:01:29 Alright, thanks, everyone.
Riccardo Magliocchetti 01:01:30 Catch you next week. Thanks a lot.
Surya Teja 01:01:32 Nice.
Mike Goldsmith 01:01:32 Bye.
Riccardo Magliocchetti 01:01:33 Modern.
Diego Hurtado Pimentel 01:01:34 Bye.
Liudmila Molkova 01:01:34 Thank you.
