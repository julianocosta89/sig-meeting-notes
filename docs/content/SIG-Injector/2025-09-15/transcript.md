SIG: SIG Injector
Date: 2025-09-15
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/0CSRmKXovxHFWaXuy6fooRcRK8QQUGUIkJWb_oI9aDbw013z4kxJDrfyMSjAAX97.70iZaatgiG7vamh8
============================================================

## Zoom Recording Transcript

Antoine Toulme 00:03:24 Hey, everybody.
Bastian Krol 00:03:28 Hello, everybody!
Michele Mancioppi 00:03:34 Hello!
Antoine Toulme 00:03:37 Hey Jack, nice to meet you.
Okay, do we have an agenda?
Bastian Krol 00:03:46 An agenda? I don't think you have an agenda.
We don't have it? Okay, hang on, let me find this.
Michele Mancioppi 00:03:52 I think Jack has raised some very interesting points.
on the channel, And I think I would like to understand exactly the scope.
Because I think… the, so my best guess…
is that, Jack is talking about when we use the system packages instead of using… instead of the injector alongside the operator.
Right?
Jack Shirazi 00:04:21 Talking about… If the operator's not there at all, we're talking about just using the injector for a system.
Michele Mancioppi 00:04:30 Because this is also, like, one of the things that is front and center, for example, in my ambassion is the injector alongside the operator, so as a better way of adding
Things to container images without
Having to modify subcontainer images so that they flip out.
And, the point you bring up is
Perfectly correct in terms of the system package, what do we do if we have different agents?
Jack Shirazi 00:05:02 Yeah, I mean, the operator… for me, the operator works fine. I like the additions that we can get with the injector, but it's not…
it's not something that I would prioritize,
For my effort, anyway. But the injector as a… as part… as a…
as a replacement for, you know, the Dynatrace one agent, that's sort of equivalent.
Michele Mancioppi 00:05:29 You're running on a host.
Jack Shirazi 00:05:31 Yeah.
Antoine Toulme 00:05:32 Exactly.
Michele Mancioppi 00:05:34 That makes a world of difference.
Jack Shirazi 00:05:36 Yeah, so that's… that's, that's a really attractive option, and for that, it needs the additional flexibility of,
a few other things that I've… so I open the issues as I said I would.
So we can, we can do the discussions and the issues.
Michele Mancioppi 00:05:55 Let me understand, which languages do you use?
Tell your applications which languages do they use?
Jack Shirazi 00:06:03 So, I'm with Elastic, and our customers use every language.
So… there's no limitation. The injector, obviously, only handles 3 languages at the moment, but, yeah.
Bastian Krol 00:06:19 I mean, the vision there is also to support
All the languages in air quotes.
Michele Mancioppi 00:06:27 In the languages that…
have a runtime which can be injected, which is every SDK, every runtime that has an open SDK, with the exception of, at the moment, C++, Rust, and Go.
Bastian Krol 00:06:41 That was what the air quotes were for, yes.
All within Reese, yeah.
Antoine Toulme 00:06:47 Yeah, we might want to shore up a bit more Python, and then Ruby is next.
But we need this to be a big tent where people from those instrumentation SDKs come and help us do, because it can't just be us.
Michele Mancioppi 00:07:00 Speaking of which, Ted, as in, have you met Tad Young?
Has barged in last week, and he wants to set up a, kind of, summit alongside…
Let me figure out it.
conference in Belgium next year in February, and the conference being, Otter and Plague alongside Fosden.
Antoine Toulme 00:07:28 Is it the books?
No.
Michele Mancioppi 00:07:31 No, he wants to make it, together with Fosden Fringe.
Antoine Toulme 00:07:39 Oh.
Michele Mancioppi 00:07:39 February the 2.
Antoine Toulme 00:07:43 Well, that's in your backyard, right?
Michele Mancioppi 00:07:45 I'm sorry?
Antoine Toulme 00:07:46 That's in your backyard, right?
Michele Mancioppi 00:07:48 Yeah, I plan to attend.
I mean, it's one of the points that we come and say, hey, look, we have a super fantastic new toy, but unless some distros
Clean up the rack and ensure that
It's possible to inject without breaking, and I am mostly looking at Python.
Then, it's gonna be very, very difficult for us.
Antoine Toulme 00:08:14 Yo, what is Ted? Ted wants us to be in that conference to discuss that type of stuff?
Is it more?
Michele Mancioppi 00:08:21 He was pitching it to me as a way to bring together the community and start with the next leg of the OpenTelemetry journey, where instead of making it technically feasible.
Becomes more like a product.
Jack Shirazi 00:08:36 And I just asked, what's the issue with Python?
Michele Mancioppi 00:08:39 Many. So, first of all, python carries, dependencies to.
Jack Shirazi 00:08:47 Okay, wait, so before you itemize it, is it listed somewhere online? Have we got an issue open for that?
Antoine Toulme 00:08:55 No.
Michele Mancioppi 00:08:55 video writing, I'm not sure.
Jack Shirazi 00:08:56 Okay, so if we can do that, because my colleague is one of the Python maintainers, so I can…
If… I mean, we're interested in the injector, so I'm…
Antoine Toulme 00:09:07 That'd be great.
Jack Shirazi 00:09:08 Try and get them to prioritize stuff.
Antoine Toulme 00:09:11 Okay, so, I mean, just for comparative evidence, right, what we have in the operator today is that we're trying to do in the operator what we do in this injector, but we do it in a communications environment, as you mentioned in your comment.
And in a sense, it's easier there because you have maybe a bit more control over the host, since it's a container and you're spinning it out.
And so, most of the time, when you set environment variables for those containers so that you can inject the SDK into the runtime, for Java and Node.js, it's fairly straightforward, because you have a way to do this with a precompile type step, specifically in Java, right? You set the Java agent, and it does a bunch of things. For Node.js, same way. For Python…
Michele Mancioppi 00:09:53 Although, to be fair, Node.js got harder because of ECMAScript, no, the CommonJS and DSM.
Antoine Toulme 00:10:02 Yeah, yeah, so there's maybe some flavors where we need to be mindful.
Python requires you to manipulate a thing called PythonPath. PythonPath is an environment variable that is used to determine the order in which you are going to import Python dependencies. Now, I'm talking
Here, I'm talking just straight up from what I've seen in the code, I'm not very much a Pythonista. And what we found out is that PythonPath is actually used heavily in some of the existing containers, specifically when you're running with Django.
Or other type of dependencies. And now, instead of having to replace or set this environment variable, you're gonna have to dance around with it, where you might prefix it and suffix it with additional.
Michele Mancioppi 00:10:42 You actually need to prefix it. Specifically prefix it.
Antoine Toulme 00:10:46 Night, okay.
Michele Mancioppi 00:10:47 You want to go first.
Antoine Toulme 00:10:48 Otherwise, you cannot check for the conflict independences.
But there's also a thing that you have to load up the pre-compile step as part of the loadup of the package, or something like that. Like, there was… just… it felt…
a lot less put together compared to what you can get from the other languages, and we could see, like, if you go to the OpenTeameter operator, open the issues, look at the number of Python issues, right? People are…
yelling or screaming or having issues with a variety of problems there. The other thing is, what the injector is actually solving for this, is the Alpine versus x86 type, or sorry, libc, alternatives are a lot more poignant in Python compared to other languages.
Java doesn't care.
Not just I don't think cares that much about that, because there's no need…
Michele Mancioppi 00:11:36 at all.
Bastian Krol 00:11:37 netcastle.
Michele Mancioppi 00:11:38 Mentos.
Antoine Toulme 00:11:40 But you go to…
Michele Mancioppi 00:11:40 Even there.NET is fine, because it's just a smaller runtime thing, but Python breaks like a brick, if you interject that one.
Antoine Toulme 00:11:48 Right, and then there's also things we don't know. So, add to the uncertainty of just having enough of a test framework for every single possible flavor and version of this.
We don't know.
So, yeah, Python's big beast.
It would be Phil…
Michele Mancioppi 00:12:05 Long story short, we're not succeeding without the SDKs accepting test suits that ensure that injection works.
Antoine Toulme 00:12:14 That's right.
Michele Mancioppi 00:12:16 And there are some SDKs that may need to change some of the things they do, like Python having unspeakable dependencies to protobuf, which… it has broken every single gRPC application I've ever touched.
In Python.
Antoine Toulme 00:12:35 Yeah, flavors and libraries such as JARPC.
I'm just taking notes in a notes doc, if you're interested.
So, Jack, does that help you?
Jack Shirazi 00:12:51 Yes and no. I mean, what I'd need to do is go to,
go to my colleague and say, look, these are the problems we're having, and I need, actually, a…
Antoine Toulme 00:13:06 He can do that. I think he'll be…
Jack Shirazi 00:13:08 That's an issue, so that he can, he can, he can work off that.
And…
Antoine Toulme 00:13:13 Sure.
Jack Shirazi 00:13:13 And I'll need, I'll need to take that to my manager, who's also his manager, and say, can we prioritize these, and…
And prioritize, and he'll come back and prioritize accordingly.
Antoine Toulme 00:13:27 You're thinking small, Jack, just bring your manager to this meeting, I will talk to him.
Okay, Jack, so I think that's one way. The other way is just, we need to just have a set of tests that cover every possible thing under the Earth, and we need to have those tests fail.
Otherwise, we don't know if they pass. And however our best intent is, I think we just need to be extremely dumb about this whole thing, where we have a matrix of, here are all the possible use cases.
here is, per language, how far we are in the certification matrix of making sure that this works in that situation, right? So…
Java on ARM with a, Alpine-based container running this way. Works okay?
Jack Shirazi 00:14:11 I can… I can tell you, because I actually implemented the tests for Elastic for the operator integration, Mmm.
we did, I think, 5 languages, and the 2 architectures.
end-to-end on traces and metrics, not logics. It's a pain, and you're not going to get all of that. You'll get the basics. You'll get the… it'll fail if…
if something doesn't work at a very basic level, but you won't get all the bells and whistles. It's… there's too much to do, too many tests to run.
Antoine Toulme 00:14:50 Okay. We gotta start somewhere, though.
So, if you want to contribute that to us, I think the injector project is the place to do all sorts of system testing like that, where we… we test and to end those things so that we know it works.
We cannot ship it, because we don't know if it works, so we cannot make any promises.
Jack Shirazi 00:15:10 Yeah, I will… I'll add that to the list of things that I need to… Push upstream.
Antoine Toulme 00:15:20 Right? The whole reason we're doing this is that we don't think it's a good use of our engineering time inside our own companies to have to maintain all those compatibility metrics. We want this to be a mutual shared resource, so we have a better leverage over the existing projects, we can move faster.
And we can also have some sort of a maturation coming around the cycle. We've had a great effort to build a specification for OpenTeometry that's supposed to help us understand how all those SDKs are supposed to work the same way and together.
We just forgot to actually have tests with that. So now we need to do those tests.
Jack Shirazi 00:16:00 I… I… I agree.
I just… it's not gonna happen anytime quickly.
But it will happen.
Antoine Toulme 00:16:09 No pressure.
Jack Shirazi 00:16:12 I feel no pressure anyways. I'm juggling… just like all of you, I'm juggling lots of things, so…
Antoine Toulme 00:16:20 Yep.
You bet. No, we do have a number of tests that we have already in a repository which test very basic things, like you mentioned, just making sure… this is something that…
Bestie had to deal with, like, we brought this over from our own initial contribution, and then Besti made it better, and I think we'll make it even better, where we have, like, a bit more of a, teeth into it to make sure we are able to test this type of conformance.
there are a number of things that we should do down the road, right? They're supposed to bring with Weaver an ability to test that the right telemetry is being emitted based on the Weaver models that are coming from those SDK signals.
So, I'd love to make them work for that, and actually interpret those things, so we can actually check that the semantics make sense, not just that we're getting signal.
But one thing at a time.
Michele Mancioppi 00:17:08 Yeah, it's pretty interesting. For example, both at Instana and,
For some things that are zero, we actually…
have end-to-end tests. I mean, instrumentations are all good and fun, and sure, you can really test them and mock some stuff.
Antoine Toulme 00:17:23 But you still need to check that the aperture behaves the way it does, so…
Michele Mancioppi 00:17:28 At Lumigo, I was creating a bunch of those, because we did a similar injector.
Antoine Toulme 00:17:34 Yep.
Michele Mancioppi 00:17:35 And that was the only way to make sure that anything worked at the end, and…
Bastian Krol 00:17:39 I think what we need…
what we need here is first low-level tests just for the injector. We kind of have those already, and then I think there's… we need tests per packaging mechanism, so there are some basic tests already for the dev and the RPM packages, only for
Java, though, but it's a start, and then we already talked about that, that we also want to distribute the injector as a standalone container image with all the SDKs on board, and then we would need tests for that distribution mechanism, which we already have in the
the zero operator repository, and we could upstream those over, or we could look at what
Jack has, and compare what's…
best and most maintainable. But that's, like, nothing that happens tomorrow at 12pm, but…
more like a midterm thing, I guess?
Michele Mancioppi 00:18:42 To Canonical, we actually layered
The testing of system packages.
Where, one thing were the tests of the application, because there are patches and stuff.
Then there were… usually, you needed to test in some way, the, pre-installation and the installation scripts.
And this is very applicable to us, because effectively what we'll need to do is to go and modify
from memory, HTC slash LD slash…
Bastian Krol 00:19:11 I'll need something preload.
Michele Mancioppi 00:19:13 Yep.
Antoine Toulme 00:19:17 Yeah.
Michele Mancioppi 00:19:17 That, that needs.
Testing.
Bastian Krol 00:19:20 Yeah, absolutely. Those do not exist, so right now the packaging tests only do, like, they start a Tomcat and then see that there is some tracing going on, and installation and uninstallation is not
So, I mean, installation is tested implicitly, uninstallation not at all. But that's a good point.
Michele Mancioppi 00:19:42 I would even argue that until the SDKs kind of chip in, and they want to take the compatibility with the Injector as a first-class citizen.
In their own tests, to merge stuff.
We could stop if we are detecting that There's an SDK now.
Instead of testing the full end-to-end application.
That would be the.
Bastian Krol 00:20:07 Yeah, what do you mean with there is an SDK now that it exists on disk, that it was installed by the…
Michele Mancioppi 00:20:13 That, that something is printed about it.
Antoine Toulme 00:20:16 Yeah.
Michele Mancioppi 00:20:16 He has a wake-along.
Bastian Krol 00:20:17 Mostly what happens right now, I think.
Michele Mancioppi 00:20:22 And my proposal is, so, one thing is, eventually, ideally, we would have end-to-end tests.
Bastian Krol 00:20:27 Hmm.
Michele Mancioppi 00:20:28 Do I feel that the SDK is…
Should contribute those, because they… some of them have
kind of test applications, making sure the injector works in those setups. It's something that…
they need to have before they merge patches of operating chapter.
Antoine Toulme 00:20:46 That's all valid to me.
Jack Shirazi 00:20:49 Guys, look at it.
The issue is that, so most of the SDKs, the tests they have, even the integration tests, are only using a mock collector, and what we really need here is the full end-to-end. That means that the SDK talking to a collector, talking to an end system, which you can then extract from the end system.
And see that you've got the traces, the metrics, the logs appropriately for the injector that you've used, or the operator that you've used.
Michele Mancioppi 00:21:18 Eventually, maybe. Eventually, maybe. But from our perspective, the moment we activate the SDK correctly.
That's as far as the injector goes.
So, the first… the first thing that we could do is to get to that point, to start to make sure that after injected, the SDK does the right thing. That requires the SDK coverage.
Bastian Krol 00:21:43 I mean, good end-to-end tests from injector over SDK to even some backend collecting, all that stuff is good and nice to have, but it's really a question where that scope falls into, and…
These are the most time-intensive and most fragile test setups, because you have so many moving components, and yeah, that would be quite a burden, and I don't see this… that this needs to fall onto the
This working group right now.
Michele Mancioppi 00:22:14 But also, think about it. The moment that like, let's say Python.
Finds a new and exciting way of breaking things.
We have a test in our… in our… in the injector project. Cool, we cannot ship the injector. The Python SDK continues in their untamed creativity forevermore, so that doesn't really help anybody.
The only thing that we would stop is…
a new version of the injector image with the SDK that breaks stuff, and…
But the injector itself, I mean… You cannot fix Python.
Antoine Toulme 00:22:48 food.
The injector shouldn't care about the semantics of what Python is expressing. It could be as simple as Python installs a different metric name for a particular use case.
And you wouldn't know any better, right? But I think this is where I would say that we should stop our responsibility and involve Weaver.
and just use the Weaver model validation. They have a live check, so going to the point that you mentioned about having a backend that can receive all that telemetry signal to check against it, Weaver has a way to receive gRPC data, right, for 317, and then actually express based off that whether this is validation with the schema that they have.
Bastian Krol 00:23:27 Excuse me, enlighten me, what is, what is Vivo in this context?
Antoine Toulme 00:23:31 is a creation of the semantic convention SIG that is a tool that is used to manipulate semantic conventions and schemas and specifications built by OpenTeometry.
By using multiple documents, you can express a rich model of metrics, logs, spans.
all the attributes behind that, and you can use that to generate code, but you can also use that to read existing schemas and perform validation. So you can run Weaver with a flag that says, run this as a life check, and it will, you know, it will actually accept data over that port and make some, like, give you a result.
And I'd much rather we use that and not try to invent our own way, rather than what there is. There is another
tool that exists today that I've used expensively, for own validation, called Golden. Golden is part of the collector contribute repository.
Bastian Krol 00:24:24 Yeah, no question.
Antoine Toulme 00:24:25 to make assertions against data received, but it's much more limited, because it's just going to take one big payload, and it's going to check against a YAML file that is loading at startup time.
Which is great for some use cases, but not all, and I think in that case, we should also just make sure we don't even try to step into that realm. We would just make it available to people and say, here, everything we're building.
Great.
Go test it.
and make it the problem of everybody to kind of reach at the summit of that, right? There's a whole bunch of… pretty much, you bring back all the people who were at the beginning and say, we've gone through all the validation, and now we can tell you this dumb cat does not work the way you think it does, or something like that.
Michele Mancioppi 00:25:07 Also, to be fair, if for some whatever reason, and it has happened historically several times.
an SDK decides that an instrumentation
Needs to change in the shape of the data ships.
Then the instrumentation needs to change in the shape of the data it ships.
Antoine Toulme 00:25:23 Yep. It's not, like, something that should break the injector.
I wish we weren't doing that here that much. The tests we had for Injector at first were very simple, like, to the point.
The first thing they would do is that they would just print out the environment variables that are available to the program, and we would just check that the environment variables printed actually match what we want them to show based on what the injector should be doing.
And that's what we did with my old preload.so stuff, right? So I think we should also stick to that, that's a good…
You know, did it work type tests?
Yup.
Yeah, it's what it is. Wookie,
What else? You guys had a good point just a bit ago.
Oh, I wanted to mention something. I'm in discussions with some of the Java country people, and I'm making them feel really bad.
So, Javacontrib is one of those repositories where things kind of are in there. Maturity levels are…
I don't know, all over the place. They have a set of
tools that could be used on their own by customers. One of them is a JMX scraper. What it does is that it runs an independent Java program, connects to your GMX port, gets metrics, uses some level of configuration and, you know, default metrics for those, and then exposes them over to a gRPC endpoint at some point, right?
The problem is those Java folks, what they've done is they've made those Java files available as Java files on Maven Central. And the instructions are literally just go figure it out, right? Go get that Java file and run it.
The response I'm getting from customers is, I don't know how to run a jar file in 2025. Where's my Debian package? Where's my RPM package? Where is my Docker container? Where's my thing? I don't want to do anything. I don't want to think. What did you do to me?
Michele Mancioppi 00:27:14 Properly legitimate for end users, by the way.
Antoine Toulme 00:27:17 You have the same users as me?
Michele Mancioppi 00:27:19 No, I just know how people work.
Antoine Toulme 00:27:22 Oh, yeah. That…
And, of course, they're doing that on Friday at 4.55 before they get out, because, you know, boss asks for this on Monday, now they just need to finish that before they go.
Nothing wrong with any of this, but I think this also shows that the fact that those projects are not getting that much contributions is telling, that people are not finding them, they're not able to use them, they're not able to leverage them.
The injector project, in a sense, is also in the same vein, trying to make more people use the SDKs. So, this is all an adoption effort.
So I pointed out that to all the Java contributors, who very quickly started to tell me, no, I don't want to be the person who's going to do the RPM, the distribution of that.
Yeah, and
I… I think there's going to be a… we're going to have a healthy discussion about having a package in Sieq for OpenTeometry.
Jack Shirazi 00:28:17 I mean, the thing about that particular one, the JMX scraper, is that,
It's really packaged with the collector.
And so…
Antoine Toulme 00:28:26 It's not…
Jack Shirazi 00:28:27 If we don't package it with the OpenTelemetry collector, the vendors package it with their collectors.
Antoine Toulme 00:28:32 That's right. So, now you have vendor lock-in, which sucks. I mean, that's not what I want, right?
So, here, here's the exact problem I had, is that the Java constraint people came back and said, no, it's actually shaped with a collector. And I showed them the Dockerfile for the distribution of the collector, and said, where do you see a Java runtime in there?
We don't… we certainly do not ship a Java runtime in our Docker image. Thank you very much. We're not… we're not going to patch it every other week. What is going on with this?
And we don't ship the Java with our collector control repository at any point. Not in the RPM, not in the binary, nowhere is it available. You have to install it separately on your own, or you'll go and get…
the Splunk version of that, which has every bells and whistles, including those things, and then you'll suffer through having to deal with the vendor support.
So, I think we need to make it much better as a whole, and as an ecosystem, otherwise we're not gonna get traction and adoption, and things will just die on the vine, and it's not what I want.
And I'm saying this because I have a… I have a horse in that race, right? The JMX scraper is just one of those things. The other one is the IBM MQ, which we just added. So we're gonna have to have a discussion about how we… we have a multiplication of this type of packaging. We need to have a discussion about how we make packaging work.
Michele Mancioppi 00:29:52 It'll be fun if you… if you have to go have dependencies.
Antoine Toulme 00:29:57 On, a system package.
Michele Mancioppi 00:29:59 Like, on Ubuntu? I mean, RPM, a little less, but Ubuntu, or…
I have more than a passing knowledge.
Of how quickly they update JVMs in main.
Yep.
Antoine Toulme 00:30:13 That's a real poem.
But it's not our problem here, right? I'm not trying to make you work on this. All I want to say is that if there's a packaging SIG next to us, in terms of injector and all that, that makes the story of the injector look interesting, because it's building its RPM and Debbie and whatnot.
But then packaging seems to have the exact same mission, where they need to also do debint RPMs of every single thing out there.
You could do the composition aspect of, like, Debian, where they like to cube all the dependencies down to the minimum amount of files, where you could have an RPM for just Java agents, right? That just installs it in the right place on your host, and then the injector could depend on that instead of having to package its own.
Michele Mancioppi 00:30:54 Which is actually the way that we would probably do it with dependent packages.
And, you would actually… what you would do is either install a meta package, like OpenTelemTrial.
that has dependencies to the SDK… to the SDKs and other instrumentations, and they each depend on the injector, and then APT and DNF and all the friends resolve it just once.
That would be the way we would do it, right?
Antoine Toulme 00:31:20 I mean, I love this idea because that allows them to do an RPM update without having to involve us.
I mean, this is the way. So, if this is the way, that also changes a little bit the charter of ours. In a sense, we have a dependency of having a packaging SIG that makes all the agents available as RPM in Debian packages and whatnot, so that we don't have to do it ourselves.
Michele Mancioppi 00:31:42 But before we can… we can… before the packaging SIG can succeed in doing that.
we need to agree on what is the interface between the injectors and the SDKs. Because right now, we said.
the correct way is to append minus Java agent to Java tool options, or the correct way is to pretend… to prepend Python, env, path, whatever it is.
Thing.
And if the SDK says, actually, we are changing stuff in a way that breaks it, then it breaks.
Antoine Toulme 00:32:13 They might need to document some stuff, is that what you're saying?
Michele Mancioppi 00:32:17 I think that the point is that the reason to have the summit in February, Richard Duggan said, here's the case, engage, and we figure out what is the…
holy blessed way of activating the SDK, so the injector implements just that.
And you make sure, their SDK, that when somebody does those steps, it works. Because also, when you go out there and look at the ways that people are telling each other how to automatically check processes with OpenTelemetry.
I mean, Java, pretty much, we all agree, as well as Java agent, the little details about resource detectors and other stuff changes wildly. Python, and I don't want to pick always on Python, but I would pick always on Python. Severing does the totally fine thing. We go there and say, no, the correct way is the Python path.
I have seen others that notified me further, so there…
There's creativity involved, and creativity in this kind of thing is really bad.
Antoine Toulme 00:33:13 Yes.
Agreed.
Alright, no problem. Jacob, what? You got your hands up.
Jacob Aronoff 00:33:20 Yeah, I was just trying to understand the actual architecture of this JMX stuff. The documentation is honestly pretty confusing.
That's… that's…
Antoine Toulme 00:33:29 That's a very point. If you want to have an issue on that, give them a hard time, that'd be great.
Jacob Aronoff 00:33:34 I just want to see, like, an architecture diagram of how this is supposed to work. Like, is the idea that you run…
The collector as a…
sidecar, and that is… like, you're running it same host, and then it, like, launches a JRE process to hook into the JMX scraper? Is that the idea?
Antoine Toulme 00:33:53 That's the old idea. The old idea is actually something that we inherited from a SignalFX contribution, because that's how everything started. And signal effects had a thing where the going.
Jacob Aronoff 00:34:05 The goal length process is going to run Java for you.
Antoine Toulme 00:34:09 Which I find a bit toxic in the first place, but…
Jacob Aronoff 00:34:12 No, I remember this, actually, because, we… one of my former companies, like.
5, 6 years ago at this point, we were SignalFX customers, and I remember looking at this and being very confused by why this was working the way that it was.
Antoine Toulme 00:34:27 The point of that was that, and I think Sigma fixed at least at one point, is that they didn't want to confuse people by having to tell them how to run Java, so they said, we'll do it for you, don't need to think about it, right? And then they did the same thing with CollectD, so they actually ran CollectD as a subprocess of the collector back then.
So that it would be possible for you to do additional things using, additional Collect D native functionalities.
In the case of the GMX stuff, there is no way for you to do anything in Go. There is no JMX implementation in Go. You cannot do MBINs in Go. That's just never been supported.
So you have to go and run this in Java no matter what.
Michele Mancioppi 00:35:05 Let me, since we're talking about this, it just came to me.
If you go and install a different JVM,
On a host, for example, on… Hubuntu on LTS.
People will come at you with pitchforks.
Antoine Toulme 00:35:21 Yeah, that sounds bad, right?
Michele Mancioppi 00:35:22 It's terrible, because the actual value of going on LTS on Ubuntu is that they will patch the packages in main for you.
there's the classy misunderstanding, also universe. No, no, no, that was never…
Never a problem with that. The JVM is in Maine.
Yeah? There is one reason to install the system GVM, like GVM from main, and that's because there is the promise that it will be patched. If you go and ship another one, hello!
Antoine Toulme 00:35:47 No, you're in trouble now.
You're actually opening up a can of worms, because then your security team is onto you.
And for good reasons, I mean, seriously.
Michele Mancioppi 00:35:57 Excellent.
I mean, you pay a whole bunch of money to mark Sutherworth.
At least make him work for it, right?
Antoine Toulme 00:36:03 Hi.
Michele Mancioppi 00:36:05 Mark, if you're listening to this.
Antoine Toulme 00:36:08 It's probably listening to this. So…
Yeah, so, you know, the idea for me was that this receiver, GMX receiver, is a shim right now, in the collector, and it's calling Java on your behalf.
And then, all those Java tooling that they have to collect the ambience, they can behave in two ways. One is they can send all the data very standard out, and then the Go process, which acts as a parent process, then reads all that data back, rehydrates it into P data, sends it down the queue into… to be consumed.
It's actually very expensive, if you think about it. Another approach is that a GMX receiver can also run with a OTRP endpoint, and then it sends data to whatever remote endpoint you want.
Which I find a much more, attainable approach. Can run on, operator, can run on Sidecar, can run on many, many different settings, and does not require as much babysitting as if it's being suppressed of the collector.
Michele Mancioppi 00:37:05 Anyway.
Antoine Toulme 00:37:05 levels.
Michele Mancioppi 00:37:07 The reason, in the year of the Lord 2025,
to have a GMS, GMX scraper is because people object to the Java agent in the midst of a process, or what's the deal?
Antoine Toulme 00:37:19 Oh, you'd be surprised. Their GMX is a massive, massive, technology expenditure. People love using this.
Michele Mancioppi 00:37:25 No, I mean, I know, but what's the reason why not to do… not to get the MBN exporter and do it inside the process? That's my question.
Bastian Krol 00:37:34 Can I quickly interrupt? I'm a little bit confused. What is the relevance of the details of the JMX scraper in the context of the injector, and why are we talking about it?
Michele Mancioppi 00:37:47 Fine points about packaging and what's going on.
Antoine Toulme 00:37:49 You…
Bastian Krol 00:37:50 Okay.
Antoine Toulme 00:37:50 It's brain to get…
Bastian Krol 00:37:51 We are on a… quite on a tangent here.
Antoine Toulme 00:37:54 Absolutely, yes. But the reason this is happening, Bessie, is because your PM right now, he's trying to get the download from another PM who has customers in the space, so he's trying to understand the priority of JMX support based on customer usage.
It's nothing to do with stage, it's about business.
Bastian Krol 00:38:11 Yep.
Jacob Aronoff 00:38:12 Excellent.
Bastian Krol 00:38:13 Okay.
Jacob Aronoff 00:38:14 Peace.
Bastian Krol 00:38:15 Could.
Antoine Toulme 00:38:16 But, yeah, sure, bring us back.
Bastian Krol 00:38:19 Yeah.
Antoine Toulme 00:38:20 Need to…
Bastian Krol 00:38:20 I mean, we discussed a couple of high-level conceptual points about the injector, and where it should go, and what the vision is.
I think there were also some, some nitty-gritty detail stuff. I'm not sure if we need to discuss it in the meeting, but, so I created a couple of issues that came out of the importing the zig injector,
Not sure if you folks had a chance to look at those. Is there anything where you have questions of why we need that, or what's up with that?
I cannot solve.
Or would it make sense to go through the current open issues?
Yeah, okay, let me, let me, let me share my screen then.
Boop, boop.
Okay, so I see, Jack, you have already…
opened a couple of things that you probably talked about on Slack as well, right? That's probably…
Jack Shirazi 00:39:40 Yeah. Related to that? I'm assuming that we'll discuss those in the issues rather than here.
Bastian Krol 00:39:45 Yeah, that's, that's, that's, that's, fine, yeah, it's, it's all well described, excellent.
Yeah, I saw, I saw that as well, that that currently fails for every PR, I think, when you don't want to add something for the changelog, so that is something that we should, I guess, fix rather…
soon, just to get CI, in good shape again.
I saw that Antoine talked about that, and said that other repositories have a mechanism for… for that, that we are missing,
Great to have.
Some more context on that, how we get that going.
What else, what else, what else? Yeah, that's…
a little bit, issue that Antoine is gone right now, because that's also something that I wanted…
him to ask about, because we have files for all those releases, and there's a render wait config in there, but I don't know, it doesn't work, apparently, so I wanted to ask.
Antoine, what's up with that?
Michele Mancioppi 00:41:13 Well, one is away. 72 updates to the latest SIG version. Yeah, yeah.
My take on that is, unless we have an excellent reason, nope.
Bastian Krol 00:41:26 Okay, not right now, or not at all?
What, what's, what's your…
Michele Mancioppi 00:41:33 what, every kind of minor version of SIP?
Has some risks, yeah.
And, what I'm thinking is that the current functional scope of the injector.
Antoine Toulme 00:41:45 Is, perfectly fine.
Michele Mancioppi 00:41:48 And if we…
What is going to happen in Zigind in the next few weeks and months is going to be
significantly works to I.O, to have, continuation-style things, and
I mean, that's gonna be great for the language, but I would rather not
follow the three backs and forths until it lands. So, I would stick with the current version.
Until there is a 1.0.
Or we have some bug that really.
Bastian Krol 00:42:20 Okay.
Michele Mancioppi 00:42:21 Makes us, because right now, we are… otherwise, we would end up investing non-trivial effort.
Just because it is… moderately updated language? I don't see it.
Bastian Krol 00:42:36 No, that's fine. I mean, if 1.0 is somewhere on the horizon, that makes sense.
Michele Mancioppi 00:42:42 Well, there is really no timeline for that, as far as I can tell.
The people are claiming, to the best of my knowledge, that
The IO rework may be one of the last big things.
But I also heard that that claim has been done before, so…
Bastian Krol 00:43:00 Yeah, I mean, but with somewhat young languages, that's always a.
Michele Mancioppi 00:43:04 That's a bit unpredictable.
Bastian Krol 00:43:05 I mean, the only reason for me creating that is you don't want to fall behind, like.
forever, like, at some point, we need to, you cannot live with, like, 5-year outdated sick version, but for now, we… there's no.
Michele Mancioppi 00:43:25 I would revisit this in the next calendar year.
Bastian Krol 00:43:29 Yep.
Let me phrase it like that, actually.
Antoine Toulme 00:43:38 Sorry, Basty, I'm back, I heard you ask for my input on something, so…
Bastian Krol 00:43:42 Yeah, exactly. Just, just a minor detail,
So, we have these files that say which, oil transplantation agent we actually want to include.
And… there's the renovates.
in there, but apparently Renovate doesn't open PR, because there are newer releases available already for all of them, and something is not working there.
Antoine Toulme 00:44:15 Yeah, no surprise.
Okay.
Bastian Krol 00:44:19 Pardon?
Antoine Toulme 00:44:20 That probably messed that up, don't worry.
Bastian Krol 00:44:22 Oh, okay, okay, good. Maybe, maybe one thing that you want to look into. Yeah, no worries.
Okay, cool. What else?
Michele Mancioppi 00:44:35 There is one topic that I don't think we ever discussed, and it's something that came to me while I was reading the messages from Jack.
Antoine Toulme 00:44:42 dope.
Michele Mancioppi 00:44:43 What do I want to do about the configuration?
file format.
He stopped.
I first received them for the injector.
Antoine Toulme 00:44:54 You mean the active configuration of the SDKs through the injector?
Michele Mancioppi 00:44:57 So for example, one of the, one of the issues that… Jack has brought up.
Like, the configurations, like, what we pass as environment variables?
Actually, it would be better solved.
By having a way of mapping processes, probably by runtime.
Antoine Toulme 00:45:22 Two configuration files.
Bastian Krol 00:45:26 Huh, that's interesting, because I think we…
Previously, before I came in, we had configuration files per runtime, just with a mapping of environment variable key to value.
I removed that.
Michele Mancioppi 00:45:44 I do not mean things that you would, like, source with Bash. I mean the official configuration file format of OpenTelemetry.
Bastian Krol 00:45:53 What? So right now, you can only configure where the instrumentation stuff for something is, but you're talking… This is nothing that I'm talking about. It's absolutely nothing else. Okay. Antoine, I mean, you look like the person that has actually.
Antoine Toulme 00:46:08 Yes.
Michele Mancioppi 00:46:09 APRs from Jack Berg on tap, so can you please share the screen on that?
Antoine Toulme 00:46:13 Oh, Jack Burke. You mean…
Michele Mancioppi 00:46:17 The configuration platform.
Antoine Toulme 00:46:18 You mean the config sig?
Michele Mancioppi 00:46:20 Yeah.
Antoine Toulme 00:46:21 Oh, yeah, I mean, there's a whole config sig, right, that's supposed to come up with some…
SIG, configuration.
Jack Shirazi 00:46:30 I think I did, and there are implementations in some SDKs, including… A declarative config? You're talking about the declarative config, are you?
Antoine Toulme 00:46:37 You're talking about the fact that they want to have some sort of a declarative config file, indeed, that is supposed to come up and become the standard for how we configure an SDK in any situation?
Michele Mancioppi 00:46:47 Yeah.
Antoine Toulme 00:46:48 For example.
Michele Mancioppi 00:46:49 for one of the easiest ways that I could imagine B, is that…
we would ship in the injector, or maybe in the packages with the SDKs inside, on which the injector will depend, or vice versa, there are trade-offs.
You would be able to specify a default configuration file that should be consistent across SDKs, but…
Until when it happens.
Then have, look for Java, use this. For Python, use that.
Beautiful.
Bastian Krol 00:47:25 this, what, can you, can you give an example of a.
Michele Mancioppi 00:47:27 concrete setting.
Bastian Krol 00:47:28 That you want to change depending on the runtime?
Michele Mancioppi 00:47:30 The location of the endpoint.
Today.
Bastian Krol 00:47:33 Why would your Java processes want to… specifically the Java processes want to export somewhere else compared to the Node processes?
Michele Mancioppi 00:47:43 Because…
Bastian Krol 00:47:43 I mean, that can…
Michele Mancioppi 00:47:44 interesting things on hosts. It's rather common that, for example, system monitoring will go in one direction, so think about the monitoring of DMessage, SystemD, some system processes, and application data will go somewhere else.
Bastian Krol 00:48:02 Yeah, but that does not necessarily depend on the runtime, right? That's what… that's my point. It could be… depend on any number of…
Things that you want.
Configure, or have your configuration, or your endpoint.
Michele Mancioppi 00:48:15 Yeah, but in my experience, like, on most, there are, like, on most hosts.
you're going to have, like, the Java applications, or applications go somewhere.
the monitoring for Python demons and something below… sometimes are closer to what happens with the operating system going one place. Sometimes the Python is the app, but it's very seldom that you have system applications written in Java.
Yep.
Bastian Krol 00:48:41 Yeah, but I mean, Python could be both, right?
For, just for example.
Michele Mancioppi 00:48:47 Unfortunate.
It's always popular. It's always Let's agree on that, it's always Python, the problem.
Bastian Krol 00:48:53 Yeah. Yeah, I'm…
Antoine Toulme 00:48:57 I mean, so this is supposed to be the panacea of the future, right? Like, flying cars and all that, it's these configuration files can solve every problem you can think of.
It's a.
Bastian Krol 00:49:06 She couldn't.
Antoine Toulme 00:49:06 It's a great declar.
Bastian Krol 00:49:07 Then you want to have an implementation of that format in Zick.
Michele Mancioppi 00:49:13 No, no, that would be levels of insanity that not even I would attend.
No, it's like, assuming that we are shipping those configuration files in the operator, in the injector package.
And these files are activated in the SDK by exporting what specific environment variable?
Bastian Krol 00:49:34 Okay, gotcha.
Michele Mancioppi 00:49:36 Now you see what I mean.
Antoine Toulme 00:49:38 I think the environment… so, I think the SDKs take an environment variable says, go read that file.
Michele Mancioppi 00:49:44 Yeah, exactly.
Bastian Krol 00:49:46 Yeah, yeah, no, that…
Michele Mancioppi 00:49:47 The debtor could say, hey, you're Java, we know because we just asked for Java tool options. Go ahead and have that configuration file, please, and thank you. Which, by the way, means that this is part of the contract with SDKs, because if they look up the configuration file.
Antoine Toulme 00:50:00 Before the runtime gets to…
Michele Mancioppi 00:50:05 Look up the stuff that we inject, which should never be the case, but you know it's gonna happen.
Then we have a problem.
Bastian Krol 00:50:13 Yeah, no, but I mean, for the language that we have right now, they all look up their specific
agent variables directly from the runtime implementation before the Autel SDK encompasses, so that Enough. Works out.
Michele Mancioppi 00:50:27 It shouldn't ever be the case, but I am known to say that.
Bastian Krol 00:50:31 Yeah.
Sure.
Jacob Aronoff 00:50:32 So, to confirm… I want to confirm my understanding of what you're saying. You're saying that the injector
We're going to, like, sort of ship it with various configur… language-specific
configuration files, and then once we determine the language, then we just say, I mean, it'll be a copy operation, right? We copy the right file for Java into the right location where Java wants it, and we say, here's your file, go use it.
Michele Mancioppi 00:50:57 I would even say that since the operator actually can check the existence of files, as a user, I would like to say, hey, for all Java things, send it there.
Jacob Aronoff 00:51:07 Yeah. Or maybe the job applications with this environment where I will send it somewhere else. Sure.
Michele Mancioppi 00:51:12 And effectively, just…
through the environment variable, point to the correct file, and that is the way to do enablement, disablement, where to send particular things in different places, without having to implement
A quadrillion environment variables, and then the user will be able to use the same configurations that they add to… as a config map into a volume in a pod on the host, and it just works.
Jack Shirazi 00:51:37 So the,
Bastian Krol 00:51:38 The downside of that being that support for this configuration format in the SDKs right now is probably very spotty.
Michele Mancioppi 00:51:47 Absolutely.
Bastian Krol 00:51:48 So it's also more like a…
Michele Mancioppi 00:51:50 Eventually, that is supposed to be the one true holy way to configure, so we might as well.
He's a scribe.
Antoine Toulme 00:51:59 It's a great way to make it their problem. I love it. I mean…
We may… we could split hairs and say, like, you know, if it looks like a Tomcat thing, then use that file. If it looks like a JBoss application server, maybe use that other file.
Because you could do additional things in those files. But we could also make it their problem. So when they ship their RPM or their Debian package for the Java agent, those files should be in there.
Because it should be good defaults.
Michele Mancioppi 00:52:23 Exactly.
Antoine Toulme 00:52:25 Yeah.
And that means that in terms of how many environment variables we have to manage…
Michele Mancioppi 00:52:30 They will never be self-contained.
You are never shipping a Debian package
That will contain the endpoint and authentication token through the particular location.
Antoine Toulme 00:52:41 You're right.
Michele Mancioppi 00:52:42 user. That part, that's why these YAML files, to the best of my knowledge, they're supposed to be composable. So you layer them.
One after the other.
Antoine Toulme 00:52:51 If they're not composable.
Michele Mancioppi 00:52:52 and say, look, my authentication token and endpoint is here, and they just customize Yodel exporter, and the rest is fine.
Antoine Toulme 00:52:59 They're not desperate.
Jack Shirazi 00:53:00 They're not composable.
Antoine Toulme 00:53:03 they should be.
Michele Mancioppi 00:53:04 They should be. I remember that.
Jack Shirazi 00:53:05 What they do is they support the ability for you to inject via environment.
To substitute things.
And not the existing environment variables, it's sort of defined by the declarative concrete.
Michele Mancioppi 00:53:19 Possibility went down the drain?
Antoine Toulme 00:53:22 Yeah. Yeah.
Michele Mancioppi 00:53:23 Huh.
Antoine Toulme 00:53:24 Well, we can apply pressure to make it better if we are in a position to push them into having some level of certification or better approach to management of configuration in the first place.
But it's great if you have this lever to make sure that we don't end up being the people who have to manage the nitty-gritty of every environment variable tag and flag and whatnot for each SDK.
that's better for us down the road. So, let's use that, and also, it's less… we should really just make sure that whatever work can be done by another team, it's done by another team, right?
The scope of this… think about it, that's…
Michele Mancioppi 00:53:59 to the best of my, like, the way that I imagine it, there are exactly two sets of environment variables
the injector.
gives a hack about. One is, which runtime are you, and hello, that is the SDK, and the second one is auto-resource attributes.
Antoine Toulme 00:54:17 Yep, agree with that one.
Michele Mancioppi 00:54:19 Why auto resource attributes?
Because SDKs and users alike have a Profoundly terrible track record.
inserting resource attributes and resource detectors, to the extent that for a while in Java, you had to use one of the jar files that that one loves so much, and somehow plug it in to get GCP resource detection, and it never managed. Never managed.
So, if that is something that there is some extension to the injector, that actually does
most of the resource detection, and sets everything up, and then exposes it as other resource attributes, that's actually leveling up the entire ecosystem in one go.
Because I do not see users with the current idea that proprietary or kind of cloud-specific resource detectors are not part of the auto-instrumentation of SDKs.
I don't see the mechanics in place for people to actually go and fix their stuff.
Yeah, I don't see it, I'm sorry.
Antoine Toulme 00:55:23 the… Resource detection processor in the collector makes backflips to make things happen.
Michele Mancioppi 00:55:28 It does a lot of interesting things.
Antoine Toulme 00:55:31 As a communities attributes processor, this also has to be first in your pipeline, because it's going to use the IP of the incoming request.
to find out which container you're coming from, then it doesn't do a good job, because it cannot go down to the IP of the container itself, it has to go to the pod, which is not… it's lossy. You may have a complex deployment with a pod with 5 different things, and then you don't know which one is what.
Michele Mancioppi 00:55:53 But assuming… if your argument is, hey, people can put a collector with the resource detection.
Antoine Toulme 00:55:59 So, that means that you must have the collateral sidecar, because nothing…
Michele Mancioppi 00:56:03 In the architecture of the injector.
Including the discussion we had with configuration files, implies that there is a collector on the same host.
Antoine Toulme 00:56:12 Yeah, that's true. We did not say that. I don't think we can make that statement with a straight face anyway.
Michele Mancioppi 00:56:17 I actually would be completely against. We should not require a collector as a sidecar.
Antoine Toulme 00:56:23 Yeah, I agree, we need to make that clear in that case, because, yeah, we have not talked about this, but I would see, for example, the injector being deployed in very private machines, or machines that do not support
Go versions from the last two years, and you actually would want that to still work. So, you're on a mainframe, you're in your IBM data center, you have some really old crafts that is running on there, and you still want to have the injector work, but the collector is too modern to run on the same OS. Then you need to do something.
Michele Mancioppi 00:56:53 By the way, Jack has a colleague called Francisco Baccetti, who apparently, for fun, is making a Zeek SDK for Auto.
Antoine Toulme 00:57:04 Nice, we need that.
Michele Mancioppi 00:57:06 Let me check if the name that I remember is correct, maybe I misattributed it, but…
I'm sure there is an Italian based in Milan.
That, actually, he's doing something like that.
Antoine Toulme 00:57:18 That's… that's fun. That's a great niche. I don't think we had Zeek discussions before.
Michele Mancioppi 00:57:26 Hi, yes. Okay.
Antoine Toulme 00:57:35 Do they want to bring.
Michele Mancioppi 00:57:36 Just Google Garazzi, sorry.
Antoine Toulme 00:57:39 Are they interested to bring it to a hotel? We could discuss that, maybe, as a… it's more like a GC discussion.
Michele Mancioppi 00:57:44 Because, think about it, if there was… as Ziggas decay.
With resource detectors we can just install.
Antoine Toulme 00:57:56 That is… that is a very smart thing to say. Thank you, that didn't… didn't occur to me. Very, very nice idea.
Why not? Free?
Michele Mancioppi 00:58:03 Why not?
Antoine Toulme 00:58:06 Okay.
I'll put the name on the… Put this on a discussion.
Jacob Aronoff 00:58:17 I like the idea of that.
There was also this idea that was proposed by Josh…
like, JMACD a while ago, where… Rather than doing,
what was it? It was, like, he wanted to run a Rust sidecar to every process, and then you, instead of outputting OTLP
over, like, like, actually sending OTLP, you just dump it to a data file with, like, Parkit.
And then you have Rust that's just constantly reading and then sending it over Arrow instead, and I can imagine him wanting to do something similar with Zig, or, like, same sort of concept, where you have
an injector, which installs the… instantiates the SDKs, and then it's also the thing that is the persistent sender from reading the file.
It's interesting. It's an interesting idea.
Wow.
Antoine Toulme 00:59:12 I know a guy working on JavaSeek wants to do a memory-mapped file instead.
Jacob Aronoff 00:59:17 Yeah, MMAP. Nothing ever went wrong with MMAP, right?
Antoine Toulme 00:59:22 could go wrong.
Jacob Aronoff 00:59:23 Yeah.
Antoine Toulme 00:59:25 But yeah, I mean, the rest approach, yeah, I know it's, hot right now. I don't know.
Jacob Aronoff 00:59:30 Yeah, I mean, they're… the Rust project is… they have plenty of other challenges before they get to that one, so…
Antoine Toulme 00:59:35 That's true, there's lots of work.
Jacob Aronoff 00:59:38 Yup.
Michele Mancioppi 00:59:38 There is some very interesting work also in Lambda with Rust, where they created a kind of mini-collector in the Lambda layer in Rust, which goes way faster.
Jacob Aronoff 00:59:47 Where's that? Is that… is that in our pro… is that in, like, OTEL project, or is that an AWS?
Michele Mancioppi 00:59:51 Yeah, I think I've seen both from Datadog, and that's how I understand some of their proprietary layers work.
And, then, I have, a developer in their studio that is in love with the thing, and he keeps linking it to me, give me a second.
Jacob Aronoff 01:00:06 Yeah, I'd love to see that.
Antoine Toulme 01:00:16 Okay.
This has been an interesting meeting.
Maybe a bit, tangential at times, but thank you for bearing with us.
Jacob Aronoff 01:00:28 Streamfold, Rotel… Oh, yeah, these are the Rotel people, that's right. They've been, they confused a lot of the Rust group, because they were like.
Someone came, and they were asking about a rust collector, and they were like, we're the rust collector, and they say, no, I saw this other rust collector, and then it was these guys. I don't know where they're at in their, in their, project, though.
Michele Mancioppi 01:00:57 Some good things to say about the input on start times of outer work.
Jacob Aronoff 01:01:02 Yeah.
Antoine Toulme 01:01:03 Well, the Digitug one is actually a lot…
Jacob Aronoff 01:01:06 Slower than I thought.
In their benchmarks, it's like… Twice the normal OTEL lambda.
Michele Mancioppi 01:01:15 What do you mean by auto-normal… normal loo to lambda?
Jacob Aronoff 01:01:19 load the, like… here, I'll put the screenshot in the… The chat here.
Antoine Toulme 01:01:23 Which I didn't have a deal.
Jacob Aronoff 01:01:24 Oh, I can't send screenshots. If you go to the… if you go to the projects, the Cold Star comparison.
Michele Mancioppi 01:01:30 Yes.
Jacob Aronoff 01:01:31 The blue line being the, like, Hotel Lambda.
Collector?
Datadogs is twice as slow.
Michele Mancioppi 01:01:41 That is not what I hear from actual customers.
Jacob Aronoff 01:01:44 Really? I guess their benchmarks are wrong.
Michele Mancioppi 01:01:47 Yeah, I don't know if I trust this particular benchmark, especially with Datadog. Also, it depends.
layers, they work differently if you're on containers, if you're on things, so that's…
Jacob Aronoff 01:02:00 Yeah, their Fargate setup is also, like, a factor in that, right?
Michele Mancioppi 01:02:05 There's all types of interesting things on my AWS serverless. Don't get me started.
Antoine Toulme 01:02:12 I'm not quite sure about any of those axes as well, or whatever.
Jacob Aronoff 01:02:16 It is kind of a weird graph. I mean, the x-axis is memory usage.
Antoine Toulme 01:02:24 Yeah, whatever.
What is this?
Michele Mancioppi 01:02:27 No, sorry, it's not memory usage, it's memory allocated to.
Jacob Aronoff 01:02:30 How is memory allocated?
Michele Mancioppi 01:02:31 Because that actually, implies how many virtual CPUs you're going to get.
Antoine Toulme 01:02:36 Jay…
Jacob Aronoff 01:02:37 You don't get to choose your CPU count for lemons?
Michele Mancioppi 01:02:42 So…
Bastian Krol 01:02:43 It's coupled together.
Michele Mancioppi 01:02:45 One of the tragedies of the commons in Lambda is that people think.
Jacob Aronoff 01:02:49 that will make their Node.js faster by giving it more memory, because more vCPUs, and Node.js is like, Hans single tried it, hello! This is… this is making me happier that I've done…
Michele Mancioppi 01:03:01 WSPN.
Jacob Aronoff 01:03:02 No landing.
Michele Mancioppi 01:03:02 swimming in cash better than not managed gateway, just because people don't understand that, because it does nothing.
Antoine Toulme 01:03:10 I assume that the Futurist Cluster workers anyway, not this, so…
Jacob Aronoff 01:03:14 Yeah, I would agree with that.
Antoine Toulme 01:03:17 Hey, so,
We can pick this up another time, but this has been a good conversation. We have time. I probably need to run. Feel free to keep talking. I'll see you around.
Jacob Aronoff 01:03:26 No, I gotta go too.
Bastian Krol 01:03:28 Bye, folks.
Jacob Aronoff 01:03:29 Thanks, everyone.
Antoine Toulme 01:03:30 Take care.
Jacob Aronoff 01:03:31 pleasure.
