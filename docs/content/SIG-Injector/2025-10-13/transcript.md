SIG: SIG Injector
Date: 2025-10-13
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Bastian Krol** 01:53 Hey there.
**Antoine Toulme** 01:59 Hey, bestie, how are you?
**Bastian Krol** 02:02 I'm fine, how are you?
**Antoine Toulme** 02:04 Looks like I'm missing a major holiday.
**Bastian Krol** 02:07 Yeah, I was about to ask, you, you have a public holiday today that you didn't notice, or what's the story?
**Antoine Toulme** 02:15 Holidays in the US is a complex story. The holiday in person is Columbus Day, which is celebrated by most of the East Coast. Really, the West Coast does not like the idea that Columbus was the… the main action?
And in general, we have rebranded it to Engineers Celebration Day.
**Bastian Krol** 02:36 Engineer Celebration Day!
**Antoine Toulme** 02:37 Indigenous, like.
**Bastian Krol** 02:39 Indigenous, okay, yeah, sorry. Yeah, that makes much more sense.
**Antoine Toulme** 02:43 Yeah.
And I am pretty certain that we stopped celebrating it as a result, because, frankly, It's just… I mean, during… Let me check, though. I don't know if you have Veterans Day, it's coming up in November, but that would be neat. I'll be thinking.
Sometimes kids…
**Bastian Krol** 03:02 Okay.
**Antoine Toulme** 03:03 But anywho, I'm here. That's the important part.
Oh, yeah, I get… I get his DF!
I can't wait to have Tuesday in a month off.
That'd be nice.
Okay.
So, just…
**Bastian Krol** 03:21 So let me get that straight. Once you rebranded it from Columbus.
day, and no longer celebrated that genocide to Indigenous Day, it stopped being a public holiday, so you don't…
**Antoine Toulme** 03:33 Thank you, yeah, you got it.
**Bastian Krol** 03:35 That's wild. Kind of.
**Antoine Toulme** 03:39 It's more like, so the corporation has to choose up to a number of holidays that they want to celebrate.
**Bastian Krol** 03:46 Wow.
**Antoine Toulme** 03:46 speak from that. It happens that most US corporations are going to be choosy about where they want people to have respite.
**Bastian Krol** 03:55 Good.
**Antoine Toulme** 03:56 You know, we're…
**Bastian Krol** 03:57 Do they have to pick a minimum number out of a catalogue of public holidays, or can they just say, you get none of these days off, or…
**Antoine Toulme** 04:05 And it could be none.
**Bastian Krol** 04:07 And you, you guys get so, so few vacation anyway, compared to Europe, like, it's…
**Antoine Toulme** 04:15 Yeah, we're on the grind the whole time.
**Bastian Krol** 04:18 Yeah.
**Antoine Toulme** 04:23 Look at us. Where's the best?
**Michele Mancioppi** 04:25 Speaking of grind, we just launched in the Death Zero operator, the support for .NET.
**Bastian Krol** 04:33 Right.
**Michele Mancioppi** 04:36 Yeah, we, we shipped the, very improved operator injector version.
And I will start, hearing from people if it explodes or not.
**Bastian Krol** 04:48 So that one has been out for, like, half a week, maybe, or so, and so far nothing exploded, so I'm… somewhat?
**Michele Mancioppi** 04:58 Most people do not update the operator very often.
**Bastian Krol** 05:00 Yeah, yeah, that's right. I mean, some have already rolled it out in production, I know that, but, sure, that… Wow. I mean, that was what I wrote about in Slack last week, that relatively lengthy post.
About that update.
**Antoine Toulme** 05:18 Yeah, I appreciate that. Thank you for being… for sharing all those good news. This is good to see in terms of maturation.
**Bastian Krol** 05:25 Yep.
**Antoine Toulme** 05:26 Yeah, I don't have anything to report on our side. We… We're starting to shore up a bit more, but the injector is not on the critical list of things that we need to deliver soonish. I do have it on my to-do list that we need to make that release, because it's ridiculous why.
**Michele Mancioppi** 05:42 Oh, let me, I'm hacking away at the packages in my spare time.
**Antoine Toulme** 05:46 Okay, thank you. I appreciate that.
I think it's great to have some strongly.
held opinions for first release, because… what does it matter?
So, you know, I trust you folks to do the right thing. If you have a specific choice you need to make, let me know, but if it's… If it… let me… hey, let me be super clear, if in case that wasn't clear before, if this release doesn't work, that's fine, because we're not trying to do a good job, we're trying to make a release, and we're an open source project, so we need help.
**Bastian Krol** 06:19 Why not both? No, but you made that point before, I know.
**Michele Mancioppi** 06:24 Yep.
We also know, Antoine, that you say that, and I'm here… Sure.
**Antoine Toulme** 06:31 Yes, European. I understand that. Let me, let me, make it clear.
First release, bad, good.
**Michele Mancioppi** 06:40 No, first release, good, good. First release, bad.
**Antoine Toulme** 06:44 good. Oh, come on.
**Michele Mancioppi** 06:46 First release, very bad, tragedy. First release, bad… meh.
**Antoine Toulme** 06:51 You know, it's… what flag are you gonna push on this thing? And so you're gonna say, yes, depend on this with your life. No. You're gonna say, this has been tested on my laptop for a duration of 45 minutes in between two meetings. It will work the first time.
If you do exactly what I said, and you had the right lip-sy, or whatever the completion protocol in the right place.
Anything else that is not my machine, nothing is guaranteed, even my…
**Michele Mancioppi** 07:18 I want to reharge that discussion, because we agreed to disagree last time.
**Bastian Krol** 07:22 Yeah, and.
**Antoine Toulme** 07:23 Okay, fine. I'm just trying to give… get you half the hook, man.
**Michele Mancioppi** 07:27 No, it's, that's the wrong hook.
**Antoine Toulme** 07:31 To get Delta.
**Bastian Krol** 07:32 But we don't need to… we don't need to agree on that point.
**Antoine Toulme** 07:37 Don't…
**Michele Mancioppi** 07:38 Wow, for example, if you wanted to make the first release now, I would not block you.
**Antoine Toulme** 07:42 No, no, yeah, I mean, I need to do it.
It'll be what is…
**Michele Mancioppi** 07:45 So, if you give me a couple of weeks, I'll probably have better packages.
**Antoine Toulme** 07:50 Yeah, but everything gets better all the time, right?
**Michele Mancioppi** 07:53 There is the thing about splitting it into the meta packages that I mean, putting.
**Antoine Toulme** 07:59 top area, huh.
**Michele Mancioppi** 08:00 Not a drama, but if we want to change the structure.
**Antoine Toulme** 08:04 That's fancy. I think that's fancy. I think that's great, if we do that.
And I love…
**Michele Mancioppi** 08:08 And that is what we're committed to do for KubeCon.
**Antoine Toulme** 08:11 Yes, yes, yes, we do need to get off our asses. I need to get on and do this.
So…
**Michele Mancioppi** 08:18 Anyway, hang on.
**Bastian Krol** 08:19 One, one… Go ahead, Michaelam.
**Michele Mancioppi** 08:22 Our friends of Elastic.
Hard?
I am not seeing progress on this thing.
**Bastian Krol** 08:31 Is that the Tyson?
**Antoine Toulme** 08:33 Are we back on Python?
**Michele Mancioppi** 08:35 Huh?
**Antoine Toulme** 08:36 This is a Python sig. Like, let's be real, right? This has turned into a Python sig.
**Michele Mancioppi** 08:39 But, I mean, the last guy said, oh, I brought in the maintainer.
**Antoine Toulme** 08:44 Oh, yeah.
**Bastian Krol** 08:44 What has Elastic to do is eject from Elastic?
**Michele Mancioppi** 08:48 Yeah.
**Bastian Krol** 08:48 Oh, okay, I didn't know.
**Antoine Toulme** 08:49 pessimistic, yeah.
Well, I think he talked to us one too many times, and now he's told that, you know, I gotta go work elsewhere, right?
**Bastian Krol** 08:57 Probably.
**Antoine Toulme** 08:58 I mean, this is love, it's fun.
**Bastian Krol** 08:59 We scared him away.
**Michele Mancioppi** 09:01 Antoine, you have… Disposable manpower.
**Antoine Toulme** 09:07 Me?
**Michele Mancioppi** 09:08 Can we maybe make this thing finally happen in the year of the Lord 2025?
**Antoine Toulme** 09:13 I mean, you got, like, what, 3 months left?
Realistically, for.
**Michele Mancioppi** 09:17 In the future, you have the Lord 2026.
Because.
**Antoine Toulme** 09:22 previous fiscal year.
**Michele Mancioppi** 09:24 We should not… we should not automatically inject Python until there is an exporter without dependencies.
We just shouldn't.
**Antoine Toulme** 09:34 Alright, let me… let me bring it up to the attention of… My very select number of Pythonistas, but… I… I find this interesting.
I'm not responsible for Python too much.
In my job, but I'm starting to be.
So maybe I'll bring it up.
Let's see what we can do.
Who is the person who started on this? March?
**Michele Mancioppi** 09:59 Like, it does, like, there were 3, 4 attempts over the years.
They just wash out maintainers being entirely unresponsive.
**Antoine Toulme** 10:08 Oh, is it because it's Jason?
So, OTRP protobuf works over OHCP.
**Michele Mancioppi** 10:13 No, yes, but the point is, you cannot have protobuf as a dependency.
**Antoine Toulme** 10:18 Okay, we're back on that. Okay, alright, so… You…
**Michele Mancioppi** 10:23 In a language that actually figured out that maybe not all the packages should live should see each other all the time, then you can use Protobuf, sure. Not in Python.
**Antoine Toulme** 10:37 Ooze.
HTTP, JSON over HTTP… 4… Python SDK.
Exports, exporter, and… It's not landed quite a bit.
Here is the PR.
Would you know… Anything about this?
The… Would like to avoid… the port above dependencies.
**Bastian Krol** 11:11 That brings… now that you mention that, I mean, we talked about that a bunch, but I only now realize that that brings up an interesting point. So, I think the SDKs are slowly moving towards using HTTP proto, I think, as a default, but of course, they can have other defaults that's still allowed, and of course, there's also OTLP exporter protocol or something to… what… should the injector have any business of selecting the protocol? I mean, if you say Python should always go without a prototy dependency, that would also mean by extension that the injector should maybe override the Prod… the protocol, and, Or should that happen on a higher level? Because just from the perspective of how we use it in the dash zero operator right now, we set the exporter endpoint and the matching protocol already in the Kubernetes level, and not… and the recovery does not have any business determining that.
**Michele Mancioppi** 12:23 Exactly. That is actually one of the things that Eric brought in us, giving up the get time override.
Because the catam override was the most, the most sure way of figuring out which runtime it was.
And then that would happen before the SDK was loaded.
Which means before, the SDK would look up the environment variables for the… the encoding, and that we don't have anymore. Because, for example, Java is perfectly happy having gRPC as the default.
Node is perfectly happy with HCP Proto.
Python, God forbid we do something out of the box that is not HTTP JSON, or PHP, same story, right?
**Bastian Krol** 13:05 Yeah, so that's another complication that we somehow need to solve, I guess. I mean, that's kind of… orthogonal to the Python dependency stuff, that needs to be solved anyway, but then we still have to figure that one out, I guess.
**Michele Mancioppi** 13:23 But I have a solution for that, for Python.
**Bastian Krol** 13:27 I think we need a solution for, globally, or runtimes, right?
**Michele Mancioppi** 13:34 No, in reality, no. It's, this particular one… is, mostly about languages that have a package model with a faculty leader, the social boundaries of an earth.
That's Python, yeah, let's be particular, it's Python.
For Python, what you would do for injection is to add, append to the Python path.
**Bastian Krol** 14:00 Yes.
**Michele Mancioppi** 14:01 If we append to the Python path, it means that, so we would append another… another location. We actually would prepend so that it goes first, but…
**Bastian Krol** 14:10 the Python Autel SDK, we would depend there, I guess.
**Michele Mancioppi** 14:14 No, we would… so first, the same way that in, I mean, we don't use it, but you could have used Notepath to say where to look for packages, yeah?
Python path has the same.
With Python, you can put, at one specific location, a specific file of the directory in the Python path, a user site script.
**Bastian Krol** 14:37 Yeah, you mentioned that before.
**Michele Mancioppi** 14:38 The user-side script allows you to do a lot of things. If you actually make it in the subset of Python that is both 2X and 3, you actually can do things like checking the Python version, and then… inject if the version doesn't match. You can look up Through codes that I know where to find.
Locations, like, which dependencies are in other places.
And, you would also be able to create a marker for the injector to say, hey, override this one as well, please.
So we could make it so… That the injector, when it has a way.
to check whether Python loaded it or not.
**Bastian Krol** 15:25 So that's… that's basically the injector being able to figure out, okay, this is Python, and I need to do something differently with the protocol and the endpoint. Okay, got it. Okay, yeah, that… that could, good.
solves it. I still am a bit skeptical that, I mean, wouldn't the injector code run completely, even before this user-side script? Because it's before the Python runtime actually starts?
**Michele Mancioppi** 15:54 But paste. Who says?
**Bastian Krol** 15:56 Mikido.
**Michele Mancioppi** 15:57 That, that is, that is the injector to do all the work.
Because technically, So we don't even need the injector to know it. The, the user site script can modify the process.
the Python environment.
**Bastian Krol** 16:12 Yeah, yeah, okay, that makes more sense.
**Michele Mancioppi** 16:15 It is a bit a convoluted way, but that's Python for you.
**Bastian Krol** 16:19 Fine with that, okay. Yeah, right. I will forget that again, and you will have to explain that again to me in…
**Michele Mancioppi** 16:27 For me to explain, so… I might.
**Antoine Toulme** 16:32 Oh, I mean, Bestie's point is more like, can we have good defaults so we have less surprises?
**Michele Mancioppi** 16:38 The answer is no.
**Antoine Toulme** 16:40 Oh, come on, man!
But I think, I think, I think we… the default should probably be HTTP Proto…
**Bastian Krol** 16:48 And then we need…
**Antoine Toulme** 16:50 But he was phenomenal.
**Bastian Krol** 16:50 There's a fallout for the cases where that doesn't work, but… Maybe we try to stay out of the exporter endpoint and protocol business, except for Python.
**Antoine Toulme** 17:02 He'll…
**Michele Mancioppi** 17:03 Yes. Yeah, that'd be the healthier way to do it.
Although, although, although, although… Within the… In containers, fine. You expect to have something put from the outside.
on a VM, very doable APT minus i open telemetry.
No, you don't.
So there, we need to find a way for people to set which endpoint they want.
**Bastian Krol** 17:31 Yep.
**Michele Mancioppi** 17:32 And we had the discussion a few… couple of months ago.
Considering shipping, the configuration file format.
That is something that could be vended.
In different languages.
Although, I'm not entirely sure how we would achieve it yet.
**Bastian Krol** 17:54 Although, for, I mean, for… if you would do some… install something with… apt or… or whatever package manager, couldn't we just then… I mean… First, we could also say, let the user just… set the endpoint and the protocol as environment variable. Very simply, we still stay out of that business, and that is a responsibility of the one installing the package, or the package could set stuff up.
**Michele Mancioppi** 18:23 I find that that completely defeats the experience of APT manufacturer. Yeah, to some degree.
**Bastian Krol** 18:28 But we don't install the collector, right? So…
**Michele Mancioppi** 18:32 No, we don't.
**Bastian Krol** 18:33 Yeah, so…
**Michele Mancioppi** 18:35 But, for example, for a user.
The way to set the process environment for an application, they start with sys init, is remarkably different.
than what they do with SystemD.
In ways that, good luck explaining Jo Rando, just wanted APT minus iOpenTelemetry, what the hell to do with it?
**Bastian Krol** 19:00 Yeah.
Okay, we will cross that bridge when we get there, I guess.
**Michele Mancioppi** 19:06 This is something where I was thinking that the configuration files are a good idea, because it allows… .
**Bastian Krol** 19:16 Which…
**Michele Mancioppi** 19:16 People would expect them.
**Bastian Krol** 19:18 Which configuration files are we… are you talking about?
**Michele Mancioppi** 19:22 This is the OpenTelementary configuration file.
**Antoine Toulme** 19:24 Let me show you something. There is a blog post in the making around those configuration files from Grafana.
Which, a member of our team was posting.
It's called a declarative config, so it's a very slanted approach, All right, we're not trying to solve everything. Put it in the chat here.
So it's gonna come up later this week, apparently.
**Michele Mancioppi** 19:53 Yeah.
**Antoine Toulme** 19:54 your configuration in Java, how you do it, what it looks like.
The format of the file, even the versioning is done.
And you can see the availability, there's a paragraph around availability. Java? JavaScript?
PHP.
and go.
**Bastian Krol** 20:11 E-H-E.
**Michele Mancioppi** 20:13 Oh, there's actually a very nice maintainer in the PHP SDK.
I think something, something Matt Bride. I, he looks like a good one. And now he was talking recently in The Rust.
In Rust, SIG, about, rebasing the PHP SDK on Rust.
**Antoine Toulme** 20:33 Oh, okay, well, my apologies.
**Michele Mancioppi** 20:36 Because there are massive performance issues, as far as I understand.
**Antoine Toulme** 20:40 In PHP? No. It's not possible.
Okay, so, anyway, Python is not in that list, which is interesting.
But that would be…
**Michele Mancioppi** 20:50 Do you know who could actually parse that file?
**Bastian Krol** 20:55 Director?
**Michele Mancioppi** 20:57 No.
Our code in the u- in the, in the, user, directory.
So, if the PHPSDK does not yet have the parser.
**Bastian Krol** 21:09 You mean the Python SDK?
You said PHP SDK.
**Michele Mancioppi** 21:14 SDK doesn't go to the configuration format.
**Bastian Krol** 21:17 the configuration form goes to the Python SDK.
**Michele Mancioppi** 21:21 We could technically support that as well in the injector with some dirty, dirty, dirty things.
**Antoine Toulme** 21:31 Sure.
**Michele Mancioppi** 21:33 It's going to be dirty.
**Antoine Toulme** 21:36 I find that it would be great if Python kind of owned its own journey on that one, because they would be giving them a bit more… Respite, but it's true that why would they do this work if we can help them?
Anyway, they're not in that list, which is interesting, right, on its own. And Java is always first, which is… The Java guys are more mature…
**Michele Mancioppi** 21:58 Jack Burke was pushing the declarative configuration language. Of course Java works.
**Antoine Toulme** 22:03 I would say, I mean, I have a lot of respect for Jack. I also think that, Trask, Jason, they're all really good at what they do.
They also are trying to be very grounded in the truth, and there's a lot of insanity.
Around some of the requirements for live reload, for example, of the SDKs.
That is just not lending very well.
It's tough, man.
**Michele Mancioppi** 22:32 It's tough.
Effectively, so did, in terms of the user experience.
Technically, DPM packages… I don't know about RPM, but I combat.
In interactive mode, They can ask you things.
When you do, APT minus psi default minus JDK.
in Ubuntu.
It asks you things like, which time zone are you?
Which other stuff are you doing?
Which is, I think, implemented as a pre-install script.
**Antoine Toulme** 23:10 Oh, you want the.
**Michele Mancioppi** 23:11 Sometime sooner.
But that is, if you install it in not minus i, minus Y, so…
**Antoine Toulme** 23:18 Yeah, yeah, yeah.
**Michele Mancioppi** 23:19 Interactive mode.
**Antoine Toulme** 23:20 Well, anyway.
**Michele Mancioppi** 23:22 Which… That could be a first way to go. In interactive mode, then we print out, hey, go and modify the configurations here.
And then it's going to work whether it is SystemD or… or something else, because the injector is going to read it and say, this is what I set as OTLP endpoint.
**Antoine Toulme** 23:50 Okay.
**Michele Mancioppi** 23:51 And it's actually compatible with, the configuration file, because the, if I recall correctly, the spec says that the configuration file trumps all environment variables.
So, if the SDK is using the configuration file.
Because the user set it somewhere.
Our modifications don't matter, and that's… Let's go to Twitter.
**Antoine Toulme** 24:23 So… I think we have lofty dreams. Let's get that resolved by KubeCon. Have a good discussion. At KubeCon, I want to make sure we get to talk with SDK people.
It's not so innocent that I involved a Java maintainer into my talk. I'm gonna make him demo stuff, but also, I'm going to invite him to the next couple meetings and see if he can help me Kind of level up on the injectors, you approach, meet your.
**Michele Mancioppi** 24:59 Let's see, he, by the way, he also invited me for the talk.
When do you prefer different?
**Antoine Toulme** 25:06 Well, I have not done anything, so I need to get on that.
What I want you to do is to be there for, frankly, it's going to be a pretty dry talk. Here's what we're doing, here's why it exists, here's a problem space, right? That's 10 minutes.
Then we're going to say, here is the demo, so we'll show you it's not just for show, there's actually some work, and then I'd love to have time for questions. This is where you show up.
Does that make sense?
**Michele Mancioppi** 25:35 Yes.
But it doesn't have to be dry.
**Antoine Toulme** 25:39 It is what?
**Michele Mancioppi** 25:39 demo, given the DBM packages.
The demo would be a VM that comes up, and has everything instrumented out of the box.
**Antoine Toulme** 25:48 Yeah.
It's gonna be a one-liner demo, it's like, apti get… Debian package.
Tomcat.
And… there it is, showing up in your collector.
**Michele Mancioppi** 26:02 Yeah. Well, that's pretty cool.
**Antoine Toulme** 26:04 I think that's good enough for everybody in the room to go, yeah, I need to do this next time I'm having to do this thing. Like, why did I install things by hand? That's prehistorical.
Right?
**Michele Mancioppi** 26:15 Yep.
**Antoine Toulme** 26:17 I'm not sure how much I'm gonna be able to nail, but we need to get on that.
Too many things going on, Anyway, I'll… I'll make sure to involve Jason more into our next two sessions, because the other thing we need to start to have is all those discussions we're having in the Injector SDK. We should have them with every SDK maintainers. So, I'm trying to find budget to go to Belgium at the DevOx.
Because I like the idea of showing up there, and maybe having a part of the OTL Unplugged discussion to be about that.
**Michele Mancioppi** 26:53 I intend to be there as well.
**Antoine Toulme** 26:55 I will… I will try. It might not be me, but, worst case, we have a early, a PM out of Poland who can be there.
**Michele Mancioppi** 27:05 Oh, I know him.
**Antoine Toulme** 27:07 Yeah, we have a… we have a team in Krakow.
**Michele Mancioppi** 27:10 I know, I know him personally. What's, what's his name?
**Antoine Toulme** 27:12 NJ Cubic.
**Michele Mancioppi** 27:14 Yes, yes.
**Antoine Toulme** 27:15 He'll be at CubeCon NA as well.
So, there's plenty of good discussions we can have together. It's, it's gonna be very, rich. Also, NJ is responsible for instrumentation, so he's responsible for everything related to Java SDK, he's got some Pythonistas under him, this type of stuff, right? So, he's my… Pier slash bus, given the structure we're in. So, he's, he's working.
**Michele Mancioppi** 27:40 Can you spell me, please, the name in the chat?
**Antoine Toulme** 27:42 Because I don't remember how to spell it.
There you go.
So, we'll see if we can participate in some session. We have… Some other people can help out, but he is kind of the main person for now, until he… He's gonna, at some point, he's gonna, like, you know, put the car on automatic, and then give the wheel to the next person.
Maybe me.
Or maybe someone else.
So, yeah, he's a good guy to work with. Let's see if we can do this. I think having a conference-driven schedule is better than nothing, so… Let's use that as a motivator.
**Michele Mancioppi** 28:37 Yeah, because otherwise, we would have set deadlines after KubeCon, and then there's Christmas, and nothing happens. I mean, it'd be like… Back in February, oh my god, KubeCon is happening again.
**Antoine Toulme** 28:47 Yeah.
But I'm on a treadmill, because I have KubeCon twice, then I have, Cisco Live, and I have Planck.com. So, I have a… I have a conference every 3 months right now, like… Mute.
Hey, let's, I think I need to get back to work. Thank you so much.
**Michele Mancioppi** 29:16 Get somebody to fix the bloody HTTP Python exporter, please.
**Antoine Toulme** 29:21 The message is out to the people who might know, and I just don't understand, because we have a lot of pythonistas on the team who are working on AI.
But they're not working on financial, like, type of features like this that would actually help them. I'm actually not happy not to see the configuration file in their work.
Because if there's one place where that would help, it's Python.
**Michele Mancioppi** 29:48 Yep.
**Bastian Krol** 29:49 Before we close the meeting, can I quickly bring up a nitty-gritty detail? I… Talks about the, GitHub Actions, the Renovate, actions, like, two weeks ago or so in Slack, and we said, yeah, let's discuss it in the meeting. We didn't last time.
I'm not… I don't exactly remember how the discussion… when… I think you said something there, it's not… not so straightforward, we can… we can do it… yeah, the, the, SHA versus version thing, you said that's…
**Antoine Toulme** 30:33 I know nothing.
**Bastian Krol** 30:34 some… What?
**Antoine Toulme** 30:37 I know nothing, I'm just… you know, I know how code looks like, but I'm mostly just… I know there's a way for you to group updates together, which is your ask, right? I want… I wanted this to be a bit better.
So, the only thing I have for you is what I can pick up and paste from some other repository, because I haven't been given time to do any of that, but if you look at Contrib, they've done this type of work, where they have a… Set of things that, like, ignore some path, pin together some changes, make it only happen on one day.
**Bastian Krol** 31:13 Yeah, no, that's fine. I was more interested in, like, it sounded like you have some more context on why we specifically need to use a.
**Antoine Toulme** 31:22 Precious.
**Bastian Krol** 31:23 the hashes, instead of the versions that might be a little bit less PRs, but implicit updates under the hood. So, Do you… do you have opinions on that? Okay.
**Antoine Toulme** 31:37 It's you.
It's a stupid opinion. It's… I got screwed a couple times by… random automatic checks that will be telling you that if you use V5, for example, you may get hacked, and that has happened, actually, because that's a great factor of social attacks.
**Bastian Krol** 31:53 Yeah, that's totally okay.
**Antoine Toulme** 31:55 And so someone's going to try to inject a bad… I mean, let's be clear, right? This is not a foolproof thing at all. What's gonna happen is, if they say you just put V5, whatever minor release underneath will be picked up by the next one, and then you.
**Bastian Krol** 32:08 No, I know that Attack Vecor, I'm familiar with that, That's… that's okay, then I'll just group them.
**Antoine Toulme** 32:19 To be clear, right? Just because you get… doesn't actually mean that you're safe, because it's going to update you to a new hash, and you'll be like, okay.
What do I do with that, right?
**Bastian Krol** 32:28 I mean, you could always go to all the commits and check if it's from the right contributor, but who does that?
**Michele Mancioppi** 32:34 Good, everybody.
**Bastian Krol** 32:35 Buzz?
**Michele Mancioppi** 32:36 It's the favorite sport of everybody.
**Antoine Toulme** 32:39 That's what we're gonna do, yeah. We're gonna do that religiously, like, if anyone's listening on this recording, we will be checking every single comment on every update, on every dependency we have. Yes, yes, yes.
**Michele Mancioppi** 32:50 And then we'll go check it for other things as well, because we like it so much.
**Antoine Toulme** 32:54 Oh, we do that all the time, yeah.
**Bastian Krol** 32:56 Yeah, okay, gotcha. I'll figure something out, and because right now I'm getting an email every day about some random GitHubection getting updated, and I'm tired of that, that's what's fine.
**Antoine Toulme** 33:09 So, but…
**Bastian Krol** 33:10 Yeah.
**Antoine Toulme** 33:10 Yeah, so I would say, like, the minimum is just to put the scheduling option that they had in the country, because I think they had similar issue where it was just very noisy, so you can just, on a weekly basis, on a Tuesday or something.
**Bastian Krol** 33:22 Wow.
**Antoine Toulme** 33:22 That would be just, fixing the immediate issue you're having about the noise.
**Bastian Krol** 33:28 Yeah.
**Antoine Toulme** 33:28 The rest of it.
**Bastian Krol** 33:29 Sounds good.
**Antoine Toulme** 33:30 Loosely held opinions based on being, you know, slapped on the head a couple times by some stupid thing. It's like, you can't just put V5 in here. I'm like, oh, fine.
**Bastian Krol** 33:39 Yeah, yeah, no, no, we had the… we had the same thing before, yeah, yeah. True, okay.
**Michele Mancioppi** 33:44 Antoine, are you married to the deal of using this weird Python FPM package to create a deb and RPM?
**Antoine Toulme** 33:52 No, I'm not married to any of that. But do you have a better solution?
**Michele Mancioppi** 33:58 Yeah, I mean, there's tons of tools in the Debian ecosystem to do good dev packages.
**Antoine Toulme** 34:02 Is there a better solution? Is there something that's more native, that works better? I mean, I…
**Michele Mancioppi** 34:07 It will never… you will not find something that does both a good job and RPM and dev.
They're just too… Separate package ecosystems.
**Antoine Toulme** 34:16 I did not, I did not come up with FPM at the time. FPM was the tool of choice 5 years ago when this type of packaging started with us.
Is there some better tools.
**Michele Mancioppi** 34:27 I'm not entirely sure I've managed to do metapackages that don't suck with us.
**Antoine Toulme** 34:32 I understand. I've done Dominion packages by hand before, so…
**Michele Mancioppi** 34:37 I'm not doing that by hand.
I know what it takes to do packages, I'm not doing that by hand.
**Antoine Toulme** 34:43 Chris, what's important to me is not so much how we do it, it's that the test pass, and that the test cover the functionality, right? And so, I'm more married to the test than I'm married to the implementation.
**Michele Mancioppi** 34:53 Very good.
**Antoine Toulme** 34:55 I have to be practical. And frankly, yeah, there's no way 5 years go on with the same tool being the choice of the community. There's always new innovation.
**Michele Mancioppi** 35:04 I do not believe FPM was ever the choice of the divin community.
**Antoine Toulme** 35:08 Oh.
Okay.
I have no idea.
**Michele Mancioppi** 35:13 To be perfectly clear on the matter. I don't think anybody looked at that front even says, this, this is the best tool to package.
**Antoine Toulme** 35:21 I… The problem is, I think the conjunction of finding something that works for both RPM and Debian, there must be a very small intersection of those tools, right? And that's probably what happened.
**Michele Mancioppi** 35:31 It is… no, I mean, if you do run-of-the-mill packages, the intersection is not that small.
If you go into meta territory, I think that meta packages and RPM work Quite differently, but… I never built them, so I don't know.
**Antoine Toulme** 35:48 I'm also not gonna build them, because I'm going to stick to Debian.
**Michele Mancioppi** 35:51 This time around.
**Antoine Toulme** 35:52 Let's just do that, yep.
Yeah, let's… let's go for that. I think our friends at Red Hat will get some really healthy for me.
**Michele Mancioppi** 36:00 Yeah, I expect Pavel to join this, Highly honored SIG very soon, and then fix it.
**Antoine Toulme** 36:07 So, a thought for that is that Red Hat is very much on the hunt to… for relevance, and they really want to have as much help as possible to bring up their empire around Ansible.
So, an approach that we could take is that we make an Ansible playbook, or collection, sorry, out of this, that would please, maybe install the RPM or something.
Why are you having a bad time with this, huh?
**Michele Mancioppi** 36:35 sensible.
Are you using the A word with me?
**Antoine Toulme** 36:39 And… and then they…
**Michele Mancioppi** 36:41 You don't even give me warming, you just drop it like this, like a savage.
**Antoine Toulme** 36:45 I could say chef or puppet instead, if you want, you know?
**Michele Mancioppi** 36:50 We need HR and local telemetry so that I can get them to talk to you.
**Antoine Toulme** 36:57 but the truth is.
**Michele Mancioppi** 37:00 every single time you drop the A word, Red Hat shows up in your recordings, and they start to watch it, and then, they show up… Ansible! It's great.
**Antoine Toulme** 37:11 They will then tell you that they'd love to host it on their official certified platform for which they actually offer QA and testing, and agree.
**Michele Mancioppi** 37:19 In reality, what I would like them to do is Ansible, I… The amount of facts given is negative.
where I would like these packages to land is there, What is the name? The UBI?
Try the QBIs? Universal Bayesian?
**Antoine Toulme** 37:36 Okay, oh man.
**Michele Mancioppi** 37:37 Oh, that, that is… that would be a… that would be good stuff. I mean, I want this to be upstreamed in Ubuntu.
**Antoine Toulme** 37:44 Okay, yeah, yeah, yeah, sweet. Okay, okay.
**Michele Mancioppi** 37:46 I want this to be upstreamed in, in, right at UBIs.
So… I mean, Ansible, I don't care. But system packages? Oh, yeah.
**Antoine Toulme** 37:56 It's just that if you mention Inceivable a couple times, people start to appear in your chat. If you mention… Right.
Or if you mention, like, RPMs or something like that, I'd be like, great, good job, people, don't care.
Because they must… they seem to have better stats on Ansible, and a lot more attention being paid to that.
**Michele Mancioppi** 38:16 Yeah, I'm perfectly fine to let the canonical people upstream this in-universe, and then they have one up on Red Hat, and in my experience, there is no easier way to get Red Hat to do something.
**Antoine Toulme** 38:27 Okay, alright, let's play that game. I think we also need to be real about our capacities. We cannot support everything.
**Michele Mancioppi** 38:34 And we need to go with some…
**Antoine Toulme** 38:37 I'm… I'm fine with this approach.
okay.
**Michele Mancioppi** 38:44 And also, at some point, we can talk to Chain Cars for Alpine.
An APK.
**Antoine Toulme** 38:51 Is that even around still? I don't.
**Michele Mancioppi** 38:54 Given the fact that we had to go through a federally.
**Antoine Toulme** 38:57 childbearing pains to get the injector out, to make it independent from LIPC.
**Michele Mancioppi** 39:01 Yeah, they very much are, yeah.
**Antoine Toulme** 39:05 No, it's just, between, what's the thing? Bitnami just went, completely AWOL.
**Michele Mancioppi** 39:11 Bin Nami said, hey, we would like you to pay us.
So they, they retired, they moved all the… they broke the helm ecosystem.
**Antoine Toulme** 39:21 Yeah, the broker, but it's… It's like, there's this concentration and kind of, People will say incidentification is not that. It's more like they're turning from the R&D, VC-funded approach to, let's make some money.
next 6 months.
**Michele Mancioppi** 39:39 Yeah, that's the monetization lever.
**Antoine Toulme** 39:40 monetization.
So, I don't know if… who else is playing that, but I'm worried.
**Michele Mancioppi** 39:48 No, I'm positive that if you do a good job of this, I can get the Ubuntu people to eventually put it in one of the universes.
And, then that means, effectively.
40% of the people out there can just APT minus IO print it out.
**Antoine Toulme** 40:05 This would be a huge achievement.
**Michele Mancioppi** 40:08 Yep. And then the rest of the RPM ecosystem will follow suit?
**Antoine Toulme** 40:14 Alright, let's talk some more. You should have more options.
And more stuff to talk about soon.
Thank you so much. I'm gonna go.
**Michele Mancioppi** 40:24 Bye.
**Antoine Toulme** 40:24 One.
**Bastian Krol** 40:25 Bye! See you.
