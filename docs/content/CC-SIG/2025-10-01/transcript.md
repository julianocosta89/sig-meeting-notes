SIG: C/C++ SIG
Date: 2025-10-01
Duration: 49 minutes
Zoom Recording URL: https://zoom.us/rec/share/TXDcVjt9PgX6snoCH2mVZhXgr4GZXLDepuT7UmkbNkVHJ5rTJGXMby51Zm7Jta6P.xhQNRgXF09v_Mu1A
============================================================

## Zoom Recording Transcript

**Nikhil Bhatia** 00:44 Hi, Mark.
**malff** 00:47 Hi, Nikhil.
So, thanks for the PR on the battery exporter options, by the way.
**Nikhil Bhatia** 01:34 Thanks for the support, Mark.
**malff** 01:36 Yeah, and I don't know if you saw that on the main issue, but there is also the log exporter that has also a batch.
And the… it is also missing some system… some environment variable there.
If you want to take a look. It's exactly the same code.
**Nikhil Bhatia** 01:56 Yeah, I'll take it up. I just wanted to ask one thing that, it would come from the environment variables only, right?
**malff** 02:03 Yes.
**Nikhil Bhatia** 02:04 Yeah, I would like to take it up now.
**malff** 02:07 Okay.
**Nikhil Bhatia** 02:09 Yeah, thanks, Mark.
**malff** 02:24 Lalit said he has a conflict. Oh, there's do it.
Hi, Doug.
**Doug** 02:38 Hey, Mark.
**Nikhil Bhatia** 02:38 Hi, dog.
**Doug** 02:40 Hey, bro.
**malff** 02:56 Yes, so Lalit has a conflict. I don't know for Tom and his son if he can join or not.
We can wait a few moments.
I did put a few attempts on the agenda, do I see that you have some as well?
While we wait, anything in there you want to discuss right now?
**Doug** 03:43 I'm trying to find a, a room to go to, but if we could cover yours first, and then I could be, settled in about a few minutes.
**malff** 03:50 Okay.
You should see the link from the OpenTelemetry main page.
to the… To a meeting notes.
Let's see if I can paste that.
Hmm… So anyway, Doug, as you have seen, I'm playing with the installation test in CMake.
And I just bumped into the Windows DLL thing.
And in the meantime, a lot of… well, one guy also has filed three different issues, complaining about the single build… the single library for Windows.
Which is missing a lot of symbols and is not linking for his application.
And… the way to build that is a bit awkward, to say the least, so I was wondering what we should do about it, and if there is a better way.
And… As usual, I don't have Windows at home, so it's harder for me to actually do a boot and debug there.
**Doug** 05:24 Yeah, I, I posted my recommendation in your draft PR, because I ran into the same challenges. Like you said, it only… the DLL only supports the V1 ABI, and then it also has… has limitations, like, it doesn't support a lot of the examples or the OTLP exporters at the moment, so… I posted a link to the script the PowerShell script that actually runs that test, and I think.
**malff** 05:53 Yeah, I saw that.
**Doug** 05:54 Yeah, I think we can just disable configuration for that particular test for now, and then…
**malff** 06:00 Yes.
**Doug** 06:00 probably… probably talk with Tom and others about, you know, the plan for the DLL support, because it's… it's gonna take, it's not just the configuration, it's a lot of those other components that we'll need to add support for.
**malff** 06:13 Yeah, I think we need to discuss that with Tom, because he would know about this part, but I think the main question for me is, how come we have… With special definition file, as opposed to just export… rely on exports.
Because for some reason, it seems that just doing an export alone is not sufficient, which is a bit surprising.
**Doug** 06:35 Right, yeah, I kinda… I ran into the same thing. I ran out of time trying to investigate it, so I just turned them off for now.
**malff** 06:43 Yeah, okay.
So, well, I forgot, but thanks a lot also for your reviews, especially on the… Is she making stuffing.
I will try to wrap up this so that we can… we can merge it.
**Doug** 07:03 Sounds good.
**malff** 07:17 Don't know if you… If you see the agenda right now, but one thing you added also was to cleanup CI.
Especially to have a matrix so that we do build in a more sane way, I would say.
Because right now, we have a lot of CIs with a lot of flags all over the place, which are all defined.
On a case-by-case basis.
And so, yes, definitely, if we… if we can clean that up, it will be much, much better for everyone.
**Doug** 07:52 Okay, yeah, I think… So I put, like, an initial proposal for, like, what a matrix might look like, but I think, you know, in thinking about it a little bit more, what I need to do is document, like, what we have, like, what we're testing now, and then we can probably look at That, and then the desired state, you know, certainly we want to test against all the C++ versions, and all the features on and off, and so on.
But I need to try to understand, like, what we're fully covering now, and make sure that we don't create any gaps, and then I'm sure that there's gaps that we have now that we want to cover, and then do that within the… the GitHub matrix strategy so it's easy.
**malff** 08:36 Yes, yes.
**Doug** 08:37 pain.
**malff** 08:38 Yeah.
And with all the different preview flags that we have, some of them are quite old.
A while ago, I created issues to actually get rid of them.
So, basically… When we have a preview flag which is off by default, The first step is to… To put it, enabled by default.
And basically wait to see if anyone screams, and if they scream, they can just turn it off again.
And once this is stable and nobody complains about issues we may not have seen, then we just remove the flag entirely, and the codebase which was in preview is now part of the main codebase without any flags.
So, it will take some time, because it takes several, several months to just, for people to… get an increase, upgrade to a new telemetry release, and see if we have, adjustments to make and things like that, but ultimately, I think we should get rid of all those flags, because some of them are quite old, and… Just to simplify things.
Yeah, yeah, I think that makes sense.
Okay.
a big part of the discussion for today was also to see… so, I don't know if you're aware of PH, Elastic is making a donation for PHP, and part of that donation is actually written in C++.
And so, there are some discussions about, first of all, what to do with his contribution.
And, once we take it, what to do with the code, keep it as is, or replace it, some parts we've opened, geometry, CPP, and whatnot.
Soup.
I don't know all the details yet, but At some point, I think the plan is to, instead of having, a small SDK and a small exporter that happened to speak OTLP written in C++ inside the PHP contribution.
I think they want to take a dependency on OpenTelemetry CPP itself instead.
So it will be less code, but just a dependency on us.
And… The goal of that discussion is to identify if things need to be changed for us, or if we need to support them somehow, and things like that.
So, I don't have all the details yet, just… it's just a heads up that, hmm.
Maybe we will be asked to do a code review, or to… Provide some feedback on some parts there at some point.
**Doug** 11:21 Sounds good, and that's basically just a review of how they're integrating OpenTelemetry CPT into this separate repository.
**malff** 11:29 Yes, when the time comes, because it's not yet.
**Doug** 11:33 Okay.
**malff** 11:43 Do you… so, Nikhil and Duke, do you see… do you see my screen?
**Nikhil Bhatia** 11:49 YAML.
**Doug** 11:51 Yep.
**malff** 11:52 Okay, so… One thing I wanted to show you On this scale.
configuration thing.
So, there is a long list of, PRs that went to a main branch already.
Including, recently, both the Bazel and CMake build. I'm just finalizing the CMake install, but after that.
I think the future would be, If not totally complete, very close to it. The parts which are missing are just polishing some parts.
One is, for example, when we raise an exception to have a proper location in the YAML file, things like that, so we have code for that, which is prototyped.
And the other main thing is OpenTelemetry Specific, configuration itself.
For a long time, they've been, on, RC1, and now there are plans to actually do an RC2 with some small bug fix.
So the repo is moving closer and closer to NRC for a 1.0 release.
And when that happened.
Yeah, so they just released our C2. So, when that happens, OpenTelement 3 C++ will be already in, We'll be hopefully compliant with, the… official GA schema in, configuration.
So we are not too far behind.
**Doug** 13:42 Awesome.
Yeah, I'm excited to start to play around with this in my own project.
**malff** 13:47 Yeah.
It was definitely interesting to implement.
Yeah.
It would be interesting to use as well.
So, yeah, that was just a side note.
We are missing Lalit and Tom, so I don't think there is a need to go through all the new issues that we have.
Oh.
Most of them, we know them anyway. One thing which I mentioned earlier is, yes, some complaints about the Windows DLL thing.
So this is about Windows DLL, this is about Windows DLL, and there was a third issue from the same reporter, Yeah, that there as well, on the same topic.
So, definitely some area we need to look at.
And that's, yeah, that is, again, the Windows DLL thing.
So this is pretty much it for recent changes.
One thing I would like to suggest, but we have time to discuss that, it's not for today.
Currently, when we send, open, OTLP HTTP data to an endpoint. There is… pretty much no authentication at all. The only thing we can pass is basically a token.
Inside various GDP headers.
Oh… And… different, I think different endpoints, so they will accept that, but a different endpoint may also as well.
Enforces stronger authentication.
So the question is how to rule.
how to fix hotel CPP so that the application can also contribute its own, authentication method to sign a request when it goes.
to your endpoint.
This is something that, over our repos have implemented.
The collector also supports some custom authentication plugin, I think.
But we don't have anything for C++.
So, I think at some point we need to look at that.
**Doug** 16:08 Yeah, I think that makes sense.
Would, do you think Owent would have some ideas on it? I think Owen might have worked a lot on the OTLP HDP.
**malff** 16:21 Excellent.
Well, basically, the way it works, we prepare an HTTP request with headers and a buddy.
And send that to curl.
And from what I've seen, what needs to be done is just to put some code in the middle of that.
to… Get a chance to look at readers, sign them, add a new reader with a signature, for example, things like that.
Before sending the, sending the message.
Okay. So it's really an interface that can be added in the flow to give a chance to third-party code to Process headers and the body the way we like.
For example, you may want to sign radars, you may want to… sign everything, including the body. You may want to encrypt the body if you are… if you need to do that, things like that.
Depending on the… on the proper… authentication protocol.
**Doug** 17:28 Excellent.
**malff** 17:29 Nope.
One thing I noticed today, this is for… for CPP, but it's also for CPP contribute. Somehow, some PRs are not progressing in CI. I think something is stuck somewhere.
So, I will take a look and… Probably, restart some bridge if we need to, but, So, yeah, basically, this pair from yours is approved. I'm just waiting for CI to finish to merge it.
This one needs to be merged as well, and Why is it… yes, you also, Nicholas, also… Once CI completes, I will merge it as well.
**Nikhil Bhatia** 18:11 Oh, yep.
**Doug** 18:20 Sounds good. Hey, Mark, since we're, all three are on the, on the call, Nikkel, I think you, created an issue. Remember, you were working on the resource detector for the process, and we, Didn't quite know how to proceed at the time on redacting some of the process commands.
I gave a thumbs up to your issue. I think we can probably proceed, but I'm curious what… Mark, if you know any more on the spec. You know, I couldn't really find anything on how to redact sensitive secrets from these, resource detector, attributes.
So I think… My interpretation is that we're probably free to implement it how we like, but maybe we can bring up that issue and look at it, since Nicole's on the call.
**malff** 19:04 Yeah, I'm not aware of a specific Specific details on the spec to say, oh, you need to do this way or that way.
I would assume that we need some sort of filter to say, hey, if there's an option that says password.
Maybe strip the content of it, things like that, so that people will define… would define all the list of options by name that we don't want to see appearing in OpenTelemetry.
But beside that, the only… The only thing that the spike requires is to provide a way to scribe the data, so that we don't leak sensitive data.
As to how to do it, It's not specified clearly, and it most likely is language-dependent anyway, because C++ would do it differently as Java and Go and whatnot.
So, as long as we do it, much will be okay.
**Nikhil Bhatia** 20:02 Mark, I was, regarding this.
I was thinking that we could pass a set of filtered attributes which we want to scrub, and then we could scrub those, whatever are present in that set filter.
Does that sound good?
**malff** 20:27 Yeah, I will have to look at the details in… because it's… I have not… Been in… in that codebase recently, but yes, it sounds… it sounds good.
**Nikhil Bhatia** 20:36 Okay.
**Doug** 20:39 Awesome.
The, the other issue, and I don't want… I don't think we need to decide it now, but I put in a proposal, that I wanted to get some eyes on for, like, upgrading the third-party dependencies.
And, I put that link in the document here for today's meeting, Mark.
But there's a… there's a comment at the end of that issue, and what I'm proposing, since we talked about just bumping the Bazel build to just pull the latest, dependent… versions of the dependencies, I was proposing that we just do the same with CMake to keep things simple.
And then… what that would be… what I think that would be, because I struggle to just upgrade one dependency at a time, like Google Test and Benchmark, because they… they then depend on C++17, and…
**malff** 21:27 They are coupled, definitely, so…
**Doug** 21:30 Yeah, so what I was gonna propose is I just do one big PR to upgrade all the dependencies for Bazel and CMake.
And then we… we merged that in at once, and I think…
**malff** 21:43 Okay.
**Doug** 21:43 That… that would have to be coupled with… a change to the CI, so that we're testing those only against C++17 and up, so… Yes. I'll have to figure out what the right timing is, but I think one big PR to upgrade all the dependencies, and then probably a separate PR beforehand to update CI, or possibly after.
It's gonna be at least two.
**malff** 22:04 Yeah. So we… Probably don't want to do that and change CI with matrix exactly at the same time. It should be more one before the other. Otherwise, it would be just merge conflicts and… Things to… To sort out after that. But, yes, we should do that.
Speaking of CMIC, Recently, there was a build break, on open tracing, because it used a really ancient version of CMake, so I saw that you did a PR to basically, downgrade CMake, and accept… to have a version that accepts CMake.
Older than 3.5 or something.
So, which is great. One thing I would like to understand is, so far we have been pushing that issue away and away, Just trying to avoid, the blue break as long as possible. But at some point, I should expect that We will need to make change to the open tracing codebase itself.
For example, one change would be just simply to actually change the CMake minimum requirement in the CMEC file.
But another, another thing would be, that CMake file also… Somehow, the Bazel build, is invoking CMake internally, because some files are generated using CMake during the Bazel build, and it's creating a lot of chaos.
So, it's very trivial to actually fix that, but to fix that, we need to apply a patch to the open tracing codebase itself.
So I'm wondering when we do fetch content or things like that, or when we pull from GitHub.
Is there a way to pull and apply a patch at the same time, so that… We could, we could build a cleaner version of the code instead of… Of degrading the tooling all the time to use a very old version.
**Doug** 24:01 Yeah, and in the CMake, authors, they came up with this approach where we're supposed to be able to set an environment variable, and it should work. I just couldn't figure out how to get that to properly get set in the Conan build for that macOS build that was failing.
I think it's probably possible to figure that out, and then that would allow us, you know, to kind of force, open tracing to be built into the new CMake.
But the alternative, like you said, is we apply a patch as part of our build to open tracing.
I think the question, too, is, like, are we planning to deprecate, or is OpenTelemetry deprecating support for open tracing?
Yeah, well, that's good.
**malff** 24:43 I'm not sure. The problem is that open tracing itself is deprecated, and we only keep it for that bridge.
So, my fear is that one day or another, if we have a bug in that codebase, we can no longer consider it read-only, so we will need to apply a patch to it to fix, even if it's one line of code.
So if we have the tooling in place that we know how to do that, it will save us a lot of time for later, I guess.
**Doug** 25:11 Okay. Yeah, it's probably worth, worth, a ticket, in that case. You know, I think the rest of our codebase is just fine, like, the macOS brew, package, job is… is building with the most modern CMake and new dependencies, and it's… it's working fine. So, I think our… really, our only issue here is the open tracing.
**malff** 25:34 Okay.
I'm not sure if I will say your name right, but, hi, Powell.
**Pawel Filipczak** 25:42 Hey, hey.
That's… And I'm Lucan. Hi, guys.
**Doug** 25:48 Hello.
**Pawel Filipczak** 25:49 I'm Pavel Filipchak, I'm an employee of Elastic, and I'm co-author of the eDot, so I opened a last UVC portion of OpenTrometry for the PHP.
Yeah, I'm here to discuss The next steps, or answer your questions.
Yep.
**malff** 26:10 So, the… So, I looked briefly at the code, and Lalit also is another maintainer of OpenTelemetry C++, looked at it.
My understanding, so I don't know exactly what processes looks like… the process looks like to process the donation itself.
We just looked at things from a technical point of view so far. My understanding is that, so this is doing some automated instrumentation in PHP.
And the way it is done is to actually invoke some modules in PHP which are written in C++, if I understand correctly.
And as part of that codebase, So, first of all, there is an OPAMP implementation, which is some small tooling.
I think for that codebase, it will be beneficial to put it in its own repository at some point, so that we can use it not only in PHP, but in new places.
**Pawel Filipczak** 27:17 over places.
**malff** 27:18 So to see… we need to see if it's feasible, if it's desirable, but it looks like it is.
And the other thing that was discussed in general is, instead of having, a C++ implementation, which is, doing some, some parts of SDK, and I think you have an OTLP exporter, if I… to send to an OTLP endpoint. Another solution is to, instead of keeping that code, to just have a dependency on OpenTelemetry C++ itself, which has the same features.
**Pawel Filipczak** 27:55 Hmm. Oh.
**malff** 27:57 So, how to do it, when to do it, In which Ripple to do it, it's all open questions right now.
But just from a technical point of view, this seems to be something which is both feasible and, I think, desirable.
**Pawel Filipczak** 28:15 So, yeah, I read the document, and also read the comments to each, so… I can agree at some ideas, so, of course, I would love to implement the op pump and put it into the C++ OpenTelemetry C++ repository.
And… but maybe from the… from the end, from one of the last questions. First, I… we would like to… to merge it to OpenTelemetry PHP ecosystem, and try to move the parts of the code into the… into the OpenTelemetry CPP.
So, what the PHP extension, the C++… C++ part is doing, so, it's basically… PHP has a possibility to extend its functionality with the extensions. Extensions are native.
And, our extension is… first providing that possibility to instrument functions in the… on the PHP side.
So, this is exactly the same what is doing, the current existing OpenTelemetry extension.
And in addition, it's also adding some new features, like the oil… like the… Infrared span, so it's… Probably creating additional threat, which is probing and dumping the stack trace of the PHP executor.
**malff** 29:49 Okay.
**Pawel Filipczak** 29:49 creating an artificial response for that, so that's one of the features which requires the native part. The second one is background sending, so we are creating the thread responsible for the sending the data.
the OTLP exporter is It's not really an exporter, it's just… just the… replacement of the PHP class, which is doing the serialization.
Because the serialization… the pure PHP prototype of serialization is very… slow, so we decide to do it in the C++, so it's a fin wrapper. Of course, we can try to adapt and use the OpenTelemetry C++ component.
But I'm not… I wasn't studying it deep enough to… to see how much effort it would require, because at some point, we need to wrap the class and expand… expose it to the PHP ecosystem.
And, And maybe it will be easier, maybe not. I'm not… I'm not sure if it's worth investment, but maybe yes.
And… And there is, of course, open question about… about the SDK itself, which… because we are… We… the PHP OpenTelemetry agent has SDK implemented in pure PHP, Maybe we can make use of the C++ implementation. We are also considering the Rust.
implementation, so… but that's for the… for the future. It's… we cannot answer that now.
And all of those replacements is because of the performance. So the performance is crucial here, and PHP is not really a good Language to do some serialization, managing a lot of, you know, small data buffers, and so on.
So it's good for the text and string modifications, but not for binary data.
Yeah, but about the donations? So, as I said, we have a few brokers, which should be solved. So, we are using the CMake, and Conan.
We have our own conan repository, and we have our… we have deployed the packages, which are copied from the original conan. Of course, the original ones can be Can be used, but they are prepute.
So it… they are… they are deployed faster.
There is an issue with the Conan. The issue is with the GLIPC version, so the Conan itself, it doesn't provide any protection against ABI incompatibilities. So, if someone is building for different GLPC, and the package, current package contains, for example, the binaries, or the static libraries, then it becomes incompatible with the build. So that's the reason why we… get the packages copied into our Conan repository, and we have our own in Elastic.
And the second reason is that we have the package with the pre-built PHP headers.
And the next thing is that we are using… we are building in the Docker container, so we have the… GCC, the Docker container with the probability GCC.
The bill itself is well organized, so it's, it's… starting from… the starting point is the CMake, then it's, building up that environment for the colon, so it's automatically set up, it's just set up the Python virtual environment in the background, so it can… so it can be just run with one comment, so it doesn't require any… and effort.
But it requires the access to the conal registry from Elastic, which is public.
But, only for… for reading.
So far, so… I have a question. Do we have, in OpenTerremetry the common repository we can deploy packages, or should we use some public ones?
**malff** 34:28 I'm not too familiar with Conan. One thing… so, I know that some repositories do their own packages, like the collector, things like that.
So they build it, and build them, and ship them.
For Ubunt Elementary C++, we are not even there yet. We will provide the source code, but we don't provide binaries to any platform or anyone.
**Pawel Filipczak** 34:49 So, people typically, breed from source again when they consume OpenTelemetry C++.
**malff** 34:55 Other repos might have some packaging already done, I'm not… not aware of which one does VAT and which one does not yet.
**Pawel Filipczak** 35:04 Okay.
And…
**malff** 35:08 Yeah, when we need some change also to some building tools, we have a case for Bazel, for example. For Bazel, when a new release of OpenTelemetry is published.
the Bazel Central repository needs to be updated to little bit version.
So… Someone, We have people who… knows OpenTelemetry and can provide a PR there to upgrade and do a new build for I mean, A new Bazel, script for that, of a new OpenTelemetry release.
So, we have that for Bazel. We have Tom, who is doing the same thing for VC Package, as well, when a new version of OpenTelemetry is, is shipped.
And The thing with the C++ world in general is that there is no… There's no unique tooling and packaging, like, the way everyone can The way in other languages, other people, everyone uses the same thing, so it's a… There are a lot of different things, left and right. But in general, after some time, people will just obit the different places where there is a package.
2.2 recent version of OpenTelemetry.
And if we need one, we can also submit a PR to that report to upgrade.
**Pawel Filipczak** 36:36 Okay, okay, I understand.
bow, and… about the donation process, so I'm not sure how it looks like, because it's my first donation.
**malff** 36:54 Honestly, I don't know either, because I'm not familiar with it.
just on top of… so, this is my own impression. It may not even be the reality, but in my impression.
There most likely will be things to be done before the donation, like a lot of things like legal or copyright assignment, things like that.
Most likely, I think we will need to set up a GitHub repository somewhere to actually receive the code.
And then there would be things after the donation, like, okay, if we want to refactor this, or if… We want to put that code into that repository, then it's just a matter of regular development with different needs from different, Different repositories, to move code around, so that could be to integrate code with the current PHP codebase, it could be moving the OPMP implementation to a separate triple.
Things like that. But, but… I'm assuming that most of the… of the technical work will happen after the donation anyway. As for the donation itself, and the… the process to get it, I have no idea.
**Pawel Filipczak** 38:11 Come on.
Okay, okay, so… yep, that's… I agree, so… I think that we get some feedback after comments, and then we can move forward. But about our involvement into the OpenTelemetry C++, of course.
We would like to contribute, so… Sure.
Of course, we have the op pump, which is implementation, which is using the HTTP protocol, but I have also the outpamp, which is using the… Hmm… WebSockets.
But it's not committed yet, so of course we can… we can contribute it to the OpenTelemetry C++ as a first step, and I think it would be worth to implement that as a library, and then.
**malff** 39:06 use some of your needs as a C++ client.
**Pawel Filipczak** 39:10 And, yep. So, we're open to, for, for, for cooperation.
**malff** 39:16 Sure, and thanks. So, we can, we can definitely do that.
So, in a lot of cases, when someone is, say, contributing a PR to an existing repo, it's just a matter of filing a PR, and it gets reviewed and accepted. In this case, it's more complex, because it's more… it's a higher level, so… What we may need to do is, oh, file a ticket, say, in community, to ask to create a repo, and then, ask to have this and that person added as maintainers of that repo, so that once the repo is created and those are maintainers, then we can, in turn.
Import code, and accept it, and review it, and things like that.
So, for all the… I would say for all the administrative parts like this, the… so we can… we can cooperate and take care of that. I'm assuming that the, So there is a technical committee, there is a GC, I don't remember what it stands for, but there are people overseeing all the different repos in general. They would know how to create a repo, where to do it, how to assign people to it, so that we can have a basic working environment.
**Pawel Filipczak** 40:35 Yep, I'm aware of that process.
**malff** 40:39 Okay.
**Pawel Filipczak** 40:41 Booth.
**malff** 40:50 just so you know, also, CPP is not only OpenTelemetry CPP, we have the CPP control repo.
Which… contains a collection of things, some of them quite dying, so it's… it's to see on a case-by-case basis. Some countries are maintained current and up-to-date, like Virginia Exporter, things like that. Other countries are falling behind, but it's… This is just a single… it's just one repository, it's a collection of independent parts.
So, the… I've seen also for OPAMP… OPAMP, I think the Go implementation has one, and it's in OPMP-Go, and there's an OPMP-specs, I think?
So, if we decide to… to take the OPMP code somewhere. One possibility is the CPP contrib, but it can also be… a different possibility is to create a OPMP CPP repository, for example, to have that alone.
So, fell.
There are… we basically have the flexibility to decide how to organize things, it's not an issue.
And on top of that, something to know also.
In OpenTelemetry in general, There is a lot of tooling also in CI integrated to do some security scan of the code, things like that, to do some reporting with known vulnerabilities, things like that, so this is… there is a common framework which is maintained at the GC level to scan all the different reports that we have with some tooling.
And on top of that, we have some tooling specific to C++, that we maintain, which is basically in CPP build tools. It's not much, but it's just help of things like, oh, format the code with filling format, or things like that, so that… We have a unified code, which is easier to work with, because it Once the code is formatted, you have less merge collision or things like that.
**Pawel Filipczak** 42:59 Yep, yep. I'm using it too, so…
**malff** 43:02 Okay.
**Pawel Filipczak** 43:06 Nope.
Okay.
So, in case of any questions, and if you have something on your mind, and you would like to ask anything, you can reach out to me on Slack, or…
**malff** 43:18 Okay.
**Pawel Filipczak** 43:18 I'm just, you know, emailing me, whatever.
**malff** 43:23 So…
**Pawel Filipczak** 43:23 comparison. Yep, and I…
**malff** 43:25 Right. Slack is good then.
**Pawel Filipczak** 43:28 Yeah, I will try to attend this meeting every time, but it collides with my private appointments, so I… I will be a bit later.
**malff** 43:40 Oh my goodness.
**Pawel Filipczak** 43:40 We'll join after 20, maybe 30 minutes, so, yeah.
**malff** 43:44 Okay, that's fine. And just so you know, we have some weird schedules, because this meeting is sometime on Monday, sometime on Wednesday.
So it's, I'm assuming you have seen that in the OpenTeametry page that describes the… The meeting calendar.
So, basically, every… Every other week, it's either Monday or Wednesday.
So yeah, feel free to stop by if you… If you have questions, then, also to get a feel for… on how… how we work, and to see how Pandem actually CPP is organized.
**Pawel Filipczak** 44:27 Thank you.
Okay, weird.
**malff** 44:35 So, as for the next step for the contribution, I think the… So there are other people in OpenTeametry which are following this more closely. We have just been asked to look at the… Advocode to… advocate to give some, technical feedback, but I think they will, they will define exactly what needs to be done and what, What steps to follow for the process to get that done?
**Pawel Filipczak** 45:04 Okay.
So… If you could maybe add some comment at the contribution issue, then we'll get some, you know, green light, or, you know, there's some, you know.
short summary of your thoughts about how we should proceed, and I'll be grateful.
**malff** 45:26 Okay, yeah, I will… I will have some comments there.
**Pawel Filipczak** 45:28 Thank you very much.
Okay, so that's all from me. I will take a deep look into the OpenTelemetry CPP. I was looking into the codebase a few months ago.
And I need to update, so… I will… I will take a look and maybe find some parts which are… which are, you know, easy to… to replace with, and to remove from our Elastic codebase.
And then use the CPP parts.
Interesting.
**malff** 46:05 Okay.
**Pawel Filipczak** 46:09 Nice.
Okay, thank you very much.
**malff** 46:12 Okay, so, yeah, I will comment, and well, I'm sure we will have more discussions on this to see how to proceed, so…
**Pawel Filipczak** 46:20 And thank you for your comments and the code review.
**malff** 46:24 Yep, thanks.
**Pawel Filipczak** 46:25 Peter quite a lot of, a lot of reverse, yeah.
Thank you.
**malff** 46:34 So… for other topics, I think, before Paul joined, we also discussed other things already for pentametry itself.
So I don't have anything specific.
Duke or Nikhil, do you have any… anything you want to discuss before we close the call?
**Nikhil Bhatia** 46:55 I would like…
**Doug** 46:57 So.
**Nikhil Bhatia** 46:58 Okay, sorry. Doug, you can go ahead.
**Doug** 47:02 No, I don't have anything else. Thanks, Mark.
**Nikhil Bhatia** 47:05 Oh.
So I wanted to ask one thing, that, batch span processor would also implement export timeout, right?
**malff** 47:16 Sorry I missed that, can you repeat that?
**Nikhil Bhatia** 47:19 The bad span processor, does not have export timeout, Oh, yes.
**malff** 47:26 So, for some reason, this is something which is mentioned in the spec, but not used in the implementation.
So, this is why I made a comment that we can have this, This setting, just with a comment saying it is not used yet.
And, I think the spec is a bit unclear on what it does. Reason being, you can have either a batch exporter or a simple exporter, and the simple exporter has zero configuration.
And then… Sorry, a batch processor and a single processor.
I think it's called Simple Processor as well.
And then those things delegate to an exporter, and the exporter may have a timeout defined. So, in case you have a batch processor and an exporter, there are two places with a timeout, and I'm not sure which one we use.
well, obviously we use the one from the exporter, because we don't use the one from the batch processor, but I don't know which one we should use, so it's something we need to investigate and clarify with a spec. Maybe… it could be that OpenTeametry CPP is not implementing what was meant.
And that we need to change something, to investigate.
But yes, I know that this part of the configuration is just not used anywhere.
**Nikhil Bhatia** 48:52 Okay.
**malff** 48:55 And for log records, there is most likely the same thing.
The batch log record processors most likely will have a timeout, but we don't It's not there in the code, and we don't use it.
**Nikhil Bhatia** 49:09 Okay.
Yeah, I think it's, that's it from my segment. Thanks, Mark.
**malff** 49:23 Okay.
Well, in that case, thanks everyone for joining, and hope to see around, one guitar goal.
Or later in, other meetings.
So, thanks everyone.
Goodbye.
**Pawel Filipczak** 49:42 Goodbye, thank you.
**Nikhil Bhatia** 49:44 Thanks, everyone. Bye-bye.
