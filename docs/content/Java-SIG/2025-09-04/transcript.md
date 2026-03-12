SIG: Java SIG
Date: 2025-09-04
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao** 00:38 Hey, Trusk.
**Trask Stalnaker** 00:40 Hey, Steve!
How's it going?
**Steve Rao** 00:47 Yeah, I'm good.
Yeah, how about you?
**Trask Stalnaker** 00:53 Doing good myself. Hey, we're, like, almost matching.
**Steve Rao** 00:57 Yeah, yeah.
**Trask Stalnaker** 01:09 Hey, we just started the RPC Semantic Convention meetings today.
Do you…
**Steve Rao** 01:18 Today. Okay.
**Trask Stalnaker** 01:19 Yeah, yeah. An hour ago.
Do you know if albuminenge… I don't… No… from Dubbo… I don't remember which person…
**Steve Rao** 01:37 Yeah, I know him. I know him.
**Trask Stalnaker** 01:40 Okay.
**Steve Rao** 01:41 Yeah, maybe we don't realize the start time today, so maybe we can join last time, next time.
**Trask Stalnaker** 01:49 Yeah, that'd be awesome.
Yeah, we're just going through… it'll take us some time to go through the backlog of things and organize the board, and… Doing some basic things, so we're not really getting into any… thing to…
**Steve Rao** 02:05 Okay.
Yeah, is there any Google Doc to, track the, IPC… Stabilize.
**Trask Stalnaker** 02:16 Yeah. Yeah, I'll share… So, if you get the calen… the… so it's all in the calendar.
But it's also all in… This… Doc, I will dump into our chat here.
**Steve Rao** 02:40 Okay.
**Trask Stalnaker** 02:43 And so we've got a project board. This is the main thing that we're working on, probably for the first Few meetings.
We went through and… Moved some of them to to-dos…
**Steve Rao** 03:04 Okay.
**Trask Stalnaker** 03:04 Made some comments on some of them, added… Some to-dos that we know we need to do.
**Steve Rao** 03:13 Okay, makes sense.
Yeah, today I, had a question, yeah.
**Trask Stalnaker** 03:36 Yeah… Extension point to solve HTTP server span.
determine whether to sample it based on the… oh, yes, I think I saw… Did somebody open a spec issue, right?
**Steve Rao** 03:54 Yeah.
**Trask Stalnaker** 03:54 About this.
So… I mean, fundamentally, OpenTelemetry sampling is… the SDK does head-based sampling.
And so… samplers… Today, are designed around head-based sampling, meaning they sample at the start of a request.
And so, they don't have access… You know, to the final span name.
**Steve Rao** 04:43 Yeah.
**Trask Stalnaker** 04:45 I… Kind of recall this topic coming up before… Yeah… Let's see… Was it? And… Was this.
**Steve Rao** 05:21 Yeah.
Yeah, this is an issue, yeah, created by my colleague.
**Trask Stalnaker** 05:38 Oh, I see, so yeah, so if you did record only… on… non-sampled traces… Then… Well, why don't you… Why do you need on spam name updated in that case?
Can you… Check… I mean, the span processor on end…
**Steve Rao** 06:12 You would…
**Trask Stalnaker** 06:13 have… Oh, you can't read the… no, you can get this band name.
Is the problem of what to do with the children that were started in the meantime?
**Steve Rao** 06:27 Yeah, maybe, yeah, maybe, yeah, we should, code the onspendNameUpDATE in a span update method.
**Trask Stalnaker** 06:42 You know, I didn't follow you.
**Steve Rao** 06:45 Yeah, you can… you can jump to the, agenda. Yeah, I list the related class. Yeah, the first one is, HTV server root update.
Yeah, in this class, it will update the final class several times.
And, It will, record the, span update.
So then updateName, and maybe in that method, we… Kim.
**Trask Stalnaker** 07:32 In this method here.
**Steve Rao** 07:34 The, yeah, maybe it will, record on spam update.
method.
Yeah, on… Right, caught on the span.
**Trask Stalnaker** 07:49 on the SPAN processor.
**Steve Rao** 07:51 Yeah.
And, yeah, in the spam process, we can do something such as we can, decide to sample or not, based on the spam name.
**Trask Stalnaker** 08:05 Right.
**Steve Rao** 08:07 Yeah, maybe.
**Trask Stalnaker** 08:07 So you could…
**Steve Rao** 08:09 Yeah, I think maybe this is a common, requirement, for example, sometimes, for some users, they want to field some, spam.
According to the spend name.
Such as, they want to, set the, sampling rate to, something like, 10% for the whole application, and they just want to set, one, span.
one method.
one interface to, sampler 100%, maybe.
JC, it's a…
**Trask Stalnaker** 08:51 What about… I mean, so the point is, then, in span processor, in this function.
You would set some… thing on the span itself, so that children that are created After that point, the sampler could check that.
**Steve Rao** 09:11 Yeah.
**Trask Stalnaker** 09:13 Can you, in the… Sampler, can you get the… Could you get the span name?
of the parent.
And make your decision.
**Steve Rao** 09:32 Span's parent. Mmm… You mean, yeah, in its choking, thought as, yeah, if we sample it based on the local rule spend.
Or Roosevelt.
**Trask Stalnaker** 09:55 So, in the sampler… You could… so when you're starting one of the children, you could look at the parent span.
And check the name of that parent span.
**Steve Rao** 10:13 Hmm.
**Trask Stalnaker** 10:14 At that point…
**Steve Rao** 10:16 Okay, yeah, maybe I need to, check this point.
**Trask Stalnaker** 10:31 Yeah, because I'm thinking the reason when… I think that would be good to answer… Is because it feels to me like whatever you do in here, you've got to update the span somehow. You've got to update the span and then use that to… decide in the sampler, and so maybe you could bypass that and since the sampler is in the SDK, you should be able to get the span name, the parent span name.
**Steve Rao** 11:06 Okay, yeah, you mean, yeah, maybe we can try to update the, sample flag, in its, children's band.
**Trask Stalnaker** 11:20 Yeah, basically the sampler, because the sampler gets to decide the… Flags when that child is created.
So you could… check the parent. You only get to set the span… the flags, once when they're… when it's created.
I don't think you can update the flag after it's created.
**Steve Rao** 11:44 Hmm… Okay, yeah, maybe I can check this point, yeah, after meeting.
**Trask Stalnaker** 11:56 Yeah, and if you could, maybe if you could put together a… just kind of a sample code in Java.
**Steve Rao** 12:06 Hmm.
**Trask Stalnaker** 12:08 Then we could talk through that more, and… It… anything like this, I mean, adding something, you know, it would need to you'd need to put together kind of a, you know, a prototype in Java, and then, like, show it in the spec, and… So if you can do it.
Without adding something to the spec, that would be better.
**Steve Rao** 12:37 Okay.
Okay, yeah, maybe we think, yeah, maybe that it may not be a very common requirement, yeah, for users if they want to customize some complicated sampler.
**Trask Stalnaker** 12:52 So, I mean, most… Users who have that requirement are using the collector and doing tail sampling.
**Steve Rao** 13:01 Okay, yeah, maybe that is one scenario, one scenario.
**Trask Stalnaker** 13:06 Yeah, because, I mean, essentially, you're talking about doing tail sampling, or you're kind of talking about something in between head sampling and tail sampling. You want to be able to change your mind During… And I remember Josh McDonald talking about this once.
as a potential future thing for OpenTelemetry.
**Antoine Toulme** 13:31 Hmm. Actually, you can do it in a… So the telesampling processor, that is.
The head sampling processor, which is part of the collector.
Can, apply different levels of… and different scores to traces, based on a certain attribute and its presence on a span.
Which skin it needs?
So you could say, I want 100% of all the errors, I want 20% of debug logs, or debug spans.
And you can do that. So if you look at what is done there, maybe you could replicate that.
Here, right, in some sort of a conventional way.
But the other approach we could take is, I don't know yet what I'm going to sample, but I should probably have an attribute on my span that mentioned that that span is special.
Right? And I'd like to pay attention to it later, when I'm going to do my head sampling, or my tail-based sampling, maybe I'll look for that type of span, and do something with it.
**Steve Rao** 14:35 Okay.
**Antoine Toulme** 14:36 There's multiple ways to go about this.
**Steve Rao** 14:38 Yeah, yeah, maybe, Yeah, currently, yeah, in our distro, yeah, we achieve, it, in our, Java agent, yeah. For, for users, we don't provide, a component like, OTA Collector for them, so… So, so we, bring this, topic to, to the meeting.
**Trask Stalnaker** 15:07 Yeah, I… I think, there's… The… being able to update the spans… sampling flag?
During… while it's active.
**Steve Rao** 15:23 Hmm.
**Trask Stalnaker** 15:23 Would be very… would be an interesting topic.
**Steve Rao** 15:27 Okay.
**Trask Stalnaker** 15:28 Right? Because that's essentially what you want to do, right?
**Steve Rao** 15:32 Hmm.
**Trask Stalnaker** 15:34 You want to, if it looks like a name that you care about, say you had this.
**Steve Rao** 15:41 Yeah.
**Trask Stalnaker** 15:43 you would still want to ideally update that dynamic, that, flag. Otherwise, you have to build it into your, samplers.
Sampler logic.
**Steve Rao** 15:58 Sorry?
Sorry.
**Trask Stalnaker** 16:02 Oh, and I do feel like I recall that being discussed at one point, so that's a Potentially something that could ask about.
But it doesn't help you if you can't get, you know, this, or… Yeah.
Yeah, so try… try doing some prototyping and post a little bit more.
Code.
**Steve Rao** 16:33 Okay, yeah.
**Trask Stalnaker** 16:33 We can chat more.
Alright.
On to Antoine's topic.
**Antoine Toulme** 16:50 Hey.
Ask, we, initiated discussion on Slack, but I think it's worthwhile to just have it in person.
**Trask Stalnaker** 16:58 Sure.
**Antoine Toulme** 16:59 And we… we've… we've had a… I think a good discussion on GitHub as well.
Which I think is good, because it's…
**Trask Stalnaker** 17:06 standpoint.
I understand your point now.
I understand what you want.
I'm not sure I really want it in this repo.
**Antoine Toulme** 17:21 Yeah, and that's totally fine, but I need you to understand that there are some consequences to that, too, because I have to say.
This comes with some level of uncharted territory, some level of expectations, and maybe some… inconveniences down the road, if we have some level of Indirectness between the fact that you're no longer in charge of building the artifact.
So… First off, right, so to recapitulate the requirements, we want… To make it easy for people to consume what you produce.
you have it already, you've made it available, but I'm here with bad news. I'm like, people are more lazy than you think, they don't know how to download JARS. I've been in customer engagements where customers are telling me.
I get the jar, where do I put it on my box? I don't know. Is it under OPT, under var, under some level of, like, is it, you know, where do I put the config file? I need everything to be figured out for me. Also.
there's a SystemD thing going on, I don't know how to run a service file, I don't want to figure that out, and everything should… it better work the first time I install it, because I don't have more than 5 minutes to do this.
That's really bad news for a Jira developer, because a Jira developer does not want to understand how an RPM works, right? It's not fun, it's not particularly interesting, and it's far away in terms of specialization is actually very orthogonal from developing good Java, right? Might not be really related.
No.
**Trask Stalnaker** 18:51 Oh, I'm not… yeah. Yeah, yeah, I'm not…
**Antoine Toulme** 18:54 million.
**Trask Stalnaker** 18:54 Discounting the use case.
**Antoine Toulme** 18:57 Yeah, no, no, you're not.
**Trask Stalnaker** 18:59 So, I mean, the… For… Let's see, where was I going?
Yeah, I mean, so there's a few thoughts I have about this, about ways forward for this.
One is… I mean… the reason I… I… I liked the collector, like, we… What a lot of vendors do for this kind of thing, instead of having, like, all these piecemeal things that all have different installation life cycles and whatnot, is they have the one agent, right?
The one thing you install… Yeah, you have the one thing that you install.
You only, you know, and that's the thing that manages all of this. And… That's kind of what I liked about the collector.
receiver integration?
Was that… You know, people don't need to set up a standalone service. You know, there aren't… they… we basically… we get to piggyback on… okay, they already got to set up the collector as a service.
So we get to piggyback back on that.
**Antoine Toulme** 20:23 Yeah.
**Trask Stalnaker** 20:24 Maybe there's other of these, like.
one agent-y things that we should have in OpenTelemetry, that, you know, things that are important enough, like GMX Scraper.
Being bundled into there.
**Antoine Toulme** 20:43 Well… So… We can talk about some of that. So, the first thing is, the collector right now is available as a binary, you can download, install yourself.
Or it's available as a… Docker image, and I think we have a very basic RPMD package that we make available as part of the installable, path of the collector from OpenSemitin, right?
So there's a different story about, vendor-based installation paths and all that.
The collector contribut installation right now, so we have… We have our own qualms in the collector's realm where We actually don't know how to package a collector to make sense of it so that people can use it.
we… have… We have the collector core distribution, which is extremely opinionated about, let's absolutely not change anything, it's the classic thing, just the bare minimum, so that we could prove as a prototype that the collector was valid.
Oh, we have contrary, which is everything in the kitchen sink.
Including the Gen X receiver and others.
In between, we have people who've built the Kubernetes distribution of the collector, which has anything related to Kubernetes use case.
But actually might not be completely… Enough.
And so, because we don't know anymore, we just gave people a tool called the OCB, right, the Open Telemetry Collector Builder, that allows them to build their own collector out of sheer ignorance about how people use their stuff.
None of those distributions, when they are made right now available, have the jar as part of them, or the Java runtime.
Because distributing the Java runtime and the Docker image is a recipe for fun times, right? As you can imagine, like, it's, like, every two weeks you're patching for vulnerabilities at this point, because you just import the wall.
**Trask Stalnaker** 22:38 There's no reason we should do that, yeah.
**Antoine Toulme** 22:41 We could distribute…
**Trask Stalnaker** 22:42 the… the JMX receiver jar, if that… I mean, that is an option.
**Antoine Toulme** 22:49 And you're doing it now, right? It's available on Maven Central, anyone can download that jar and do stuff, right? And there's no limit.
**Trask Stalnaker** 22:55 Could be more tightly integrated into the collector contrib…
**Antoine Toulme** 23:00 Sure.
**Trask Stalnaker** 23:01 It could be…
**Antoine Toulme** 23:03 It could be somewhere on the path somewhere, but if it's in Docker, then you still need Java Runtime to be around.
If it's not Docker, then I'm not sure. Like, you could… this story is bigger than it looks, because we have the same problem of usability, not just with the GMX receiver, but let's even say, like, the Java augmentation image right now is managed by the operator, because they're the recipient of the use case.
But you could make the argument that the operator people would want to have a JMX receipt, like, a JMX scraper as the document image available to sidecar any pod on a Kubernetes environment.
Right.
You… this part says, I have GMX things that I'd love to export, come get them, and then you… you find out that you can just, you know, plop next to it another container that starts to get the information every 5 seconds, send it to some OTRP endpoint.
So… We have a…
**Trask Stalnaker** 24:04 Maybe a use case that I would be more inclined to support is the operate, you know, deploying it through the operator.
**Antoine Toulme** 24:13 It's kind of newt, right? I mean, this… this is cool, like, this is kind of novel, you get to do so much more.
The problem is, in… Do we want to have How do we… how do we, how do we weave that into the story of OpenTeometry? So far, all the vendors, what they've done is that they said, we'll build the LEGO bricks together, but when it comes to the integration, they want agent installed, these type of things, right? The thing you mentioned.
Okay, let's take back where we can be really good at it, and we want to do our own distribution, and we want to maintain and own this.
But what I'm hearing from our customers and our… everybody who's using OpenTeametry is, no, I do not want that. What I would like it is a no-vendor lock-in. You sold me no vendor lock-in. You said OpenTemmetry is an open source, community-based, best practice solution that people can use.
And you're shipping me some real stuff that I have no idea how it's built and built, and you just need, you know, trust me, bro, right? That this JMX receiver jar is the right one, and I'm gonna have to scan it myself, right? Because I don't know if your SHA-256 actually matches what is in the stream repository, or in Maven Central.
I'm on the course.
And can you come back? Thank you.
Can you come back later?
Thank you. So, sorry, 5-year-old. So… if… So, multiple options, right? One is, okay, Open Symmetry is a framework-driven open-source project. We build Legos, you're in charge of putting them together, right?
**Trask Stalnaker** 25:51 But no, I…
**Antoine Toulme** 25:52 the…
**Trask Stalnaker** 25:53 I… I support what Austin is saying, that, you know, I think that we need to mature OpenTelemetry beyond… just the LEGO bricks. We need to have more of a product focus.
**Antoine Toulme** 26:10 Okay.
**Trask Stalnaker** 26:11 I… I'm just not sure this is the… I'm just not sure this is the way.
Right? Like, this seems like… Not the best way to… This is still not what you… users want. They want The one aid… the one installer thing.
**Antoine Toulme** 26:31 So… The next step is… so there's… I was going to give you three options, and, you know, make your pick, right? First, we don't do anything, we keep it so it's framework-based and all that. And we make it like a Java Spring. If you look at Spring, right, the way you make it available to people is, like, putting yourself together.
Or pay a lot of money for a complete experience. It's totally fine, right? Why not?
That's one. Two, we make the Java Country people we… We give them intense training. They go through, like, a, you know, Apollo mission-type training, right?
**Trask Stalnaker** 27:04 The whole thing.
**Antoine Toulme** 27:05 And each and every one of them comes out of this, like, you know, buffed out, you know, can do, you know, all sorts of things, and they now know Kubernetes in and out, they know everything about managing the best Docker images, they know RPM dividend packages, they know how to do whatever, right? You can just throw them into any packaging situation, they can answer things by heart.
And they become experts into distributing those artifacts themselves, and then you have to replicate that on each of the SIGs, right? You go to Node.js, you do the same thing. You go to Python, you do the same thing.
**Trask Stalnaker** 27:37 Yep. Maybe that's fine, maybe that's great, right?
**Antoine Toulme** 27:42 Yeah?
**Trask Stalnaker** 27:43 That's gonna be painful. You're gonna get pushed back at every step of the way, and you're still gonna end up with, like, you know, all these just slightly better, bigger LEGO brick. Better LEGO bricks, but it's still LEGO bricks.
**Antoine Toulme** 27:58 Okay, and the last step, of course, and the one where you want to go, right? I mean, I think you indicated that very clearly to me, but I've been taking my time to get there, because I want to make sure you understand what you're getting yourself into.
is…
**Trask Stalnaker** 28:10 I don't. Yeah, go ahead.
**Antoine Toulme** 28:14 Yeah, I know you can be more nuanced than this, right? But I just want to make sure we walk this together, right? Because there are a lot of implications to this.
So you say, look, I'm a Java guy, we're doing Java. There's a Python guy over there, they're building Python packages. They have no JS, no.js packages, right? We put that out, and there's a separate team that's really, really good at building Debian packages. They do this… They have this to heart, they know how to build an install package. They actually don't just do that, they even manage a Debian repository for everything.
They even sign things for us. They do a lot of work downstream. They make it available, they build beautiful documentation. They take on all the work of being first line of support when something doesn't work, so they can route people to the right SIG.
let's say it's a Java problem, well, I… you know, maybe it's an installation issue, but oh, no, no, no, it's because you're using Java 11, and that version of Java 11 does not work with this. You need to go talk to the Java scene, right?
And so you build this layer of people who are going to be sitting in front of all the SIGs and building all the installers.
You already have it. The operator people have done that, right?
And when I talk to other people, they're very tired, let me tell you. They're really, really in a bad shape. They are bent backwards trying to make something work, and what they found out is that there's a recipient of all the acceptance testing that you do when you do this type of stuff, because they're the ones putting together the whole experience, right?
There is a breakage in the configuration string for this particular value. This cementing convention does not apply the same way. The collector changes, config.yaml does not accept telemetry settings the same way.
This is really, really difficult, and they have to navigate that. And they end up having quality issues which are much more dire, in a sense, because they are the… the last step in there. And sometimes, sometimes, they can actually push back and… or provide feedback back up the chain to the SIGs and tell them, hey, I think you broke something.
But that's tough. That's really tough.
So… the problem there is the indirectness and the start, like, the relationship is interesting. So for Collector, what we did is when we built the releases repository.
at first, it was just an outspurt of the collector itself. It was just the same population of people, but what I realized really quickly is that a guy who's working day in, day out in Go in the core is actually not qualified to talk to me about how we're going to do validation of some, you know, RPM install, or something like that.
And so we started to have to specialize. So we built recently, well, recently, a year ago.
Started to create a separate team of people who are going to be maintainers just for the releaser's repository.
And what that allowed us to do is to recruit people from… there's a guy from Dynatrace that we were able to make, a maintainer.
who has no idea about GoCode.
But it's really, really good about pushing bits together and making sure that things get signed, and that you get the Docker images in the right place. I mean, those go read these really well.
So, what we see is that, over time, you start to see a specialization of roles where you might have someone who's extremely obtuse and cannot talk to you about Java, but can tell you that your config file, in that sense, is not readable, or doesn't make me… sorry. I'm going at length, trying to explain to you that You might be… You might be chasing an evil where you don't have to think about packaging, but you're trading that for a bunch of people who are going to be downstream from you, yelling back at you every single step of the way, because things don't work the way they were thought, or, you know, things break.
Are you okay with that?
**Trask Stalnaker** 32:03 I am. I mean, you know, I don't want to minimize the amount of work and, You know, of getting such a group started and running, but I am… I'm 100% supportive of having that discussion.
In the community.
**Antoine Toulme** 32:30 Okay.
**Trask Stalnaker** 32:30 From what I've heard, Austin… I believe Austin is supportive of that.
**Antoine Toulme** 32:38 Okay.
Yeah, I see that too.
It's… it's interesting, because there might be a lot of refinement that we could do to distributions, because you could pair up multiple components together to build really interesting experiences for people.
Okay, so…
**Trask Stalnaker** 32:58 Yeah. Yeah, I mean, I think it's a very lot… like, and I think it… you could almost even pair it in… kind of tie it into the OpenTelemetry graduation.
That, as we look forward towards maturing the project, That this is, you know… an important…
**Antoine Toulme** 33:20 Yeah. Peace.
You know, what open temperature reminds me is, everybody, every one of those, early adopters curves or, projects, right, it could be Facebook or the internet or whatnot, is that when there is a critical mass of early adopters who feel good about where they are, and they like the project because it works for them.
And then we're going to make it easy, and then you're going to open the floodgates to everybody else who doesn't care.
Because the moment you make an exit installer of your stuff.
then you're opening the floodgates to millions and millions of people who are just like, oh, you know, I downloaded this on the site, and things don't work the right way. So I also want to make sure Is this where the project wants to go? Because it's kind of nifty to have vendors kind of handle the load of support and complaints that come with that.
the same.
**Trask Stalnaker** 34:13 All valid things to discuss, yes.
**Antoine Toulme** 34:17 Yeah, yeah.
Okay. It's a… I'm not… I'm not trying by any stretch to make you commit, or I'm not putting any weight behind your words as if you were a member of, like, making a decision, or a decision maker. I'm just trying to have a bit of a discussion with you, because I thought that this was actually an incredible opportunity also for Java Country and other projects, if they want to rein in how they want to run their stuff.
**Trask Stalnaker** 34:49 Yeah, I think from what you've seen from the, maintainers of this package, I mean, it's… Potentially, ultimately, up to the code owners here.
Sylvaine… Jason… But, yeah, I'm… it doesn't quite… Yeah, let's see if we can come up with something better.
Long term.
**Antoine Toulme** 35:18 I completely understand the reaction, by the way. I mean, this is… it must be absolutely overwhelming. It's, like, yet another thing to do, like, so that's way too much. But… So… How would I move forward? Should I open an issue in the community to discuss?
**Trask Stalnaker** 35:36 Yeah, I think so. Let me see, what do we have here?
**Antoine Toulme** 35:42 Did I put some actual numbers behind this, too? Because… so what I would love to be able to say with a straight face is that we would increase the adoption of OpenTeametry by a certain amount based on that.
Because otherwise, why do it, right?
**Trask Stalnaker** 36:01 Yeah, but, I don't know how you're gonna do that.
And I don't think it's necessary. I mean…
**Antoine Toulme** 36:09 I can use references?
**Trask Stalnaker** 36:14 Yeah, I mean, you can just give your opinion, you know, like, that it will… I wouldn't necessarily try to Pinpoint any numbers, just that… This would make it accessible to a lot of people who… Aren't already using it, and, you know, at the end of the day, you know, people need to will either Believe that, or they won't.
But I think we've got some pretty reasonable community. I think people will… understand, The value of that.
I think that the bigger, you know, trick, of course, is putting together a You know, getting together a group of people And… You know, who are committed to doing that.
And making that successful.
**Antoine Toulme** 37:07 That's the tough part.
**Trask Stalnaker** 37:09 Yeah, that… the staffing it is always the…
**Antoine Toulme** 37:12 the hardest part. Obviously, we would…
**Trask Stalnaker** 37:15 It would be ideal to… Learn from, you know, the, Kind of consolidate, you know, what can we consolidate from… the…
**Antoine Toulme** 37:27 dope.
**Trask Stalnaker** 37:28 Collector releases, the operator, the new auto instrumentation, Deployer, installer thing.
You know, how do we get all… how to… How does that all fit together?
**Antoine Toulme** 37:44 How do you make a download site?
Well, the point of this also that it needs to be end-user driven, so think of this as SourceForge.net, right? If you go to the download site of SourceForge and you're looking for, let's say, an OpenTemmetry tool there, you would probably be less than pleased, because if you've been to SourceForge, it looks like hell, right? So, if… What is the alternative might be a nice, centralized, one-page, here's everything you could download from us that would be useful to you right away.
**Trask Stalnaker** 38:14 Yeah, I mean, you could also discuss with Severin. I know Severin's, from a dock perspective, has been, wanting to rewrite all the installation Stuff.
And so, if he, you know, had, like.
An idea of, like, oh, like, here's a way to do it that could be simpler for users in the future.
**Antoine Toulme** 38:42 Nice, yeah, I will.
Okay.
Okay, I really don't want to… I really want to give it the time also to mature in, in this discussion. I wanted to make sure Do you understand what you're… again, sorry, I'm gonna go again about this, but I want to make sure that you understand that you're giving up a lot of A lot of the… the bandwidth and… People will not see the Java code. They will see, JMX scraper.
Do you understand?
**Trask Stalnaker** 39:14 That's amazing.
**Antoine Toulme** 39:16 Eve? Okay.
**Trask Stalnaker** 39:17 Okay. That's fine.
Yeah.
**Antoine Toulme** 39:20 That's fine.
**Trask Stalnaker** 39:20 I mean, there needs to be debug options, right, in the JMX scraper that then get exposed via the, you know, that users can set an environment variable somewhere, that they can get a log that we can use to tell what the problems are.
There's a lot of growth.
Certainly.
**Antoine Toulme** 39:44 Understood.
**Trask Stalnaker** 39:47 But, I mean, that goes, I think, the supportability aspect.
There's both pluses and minuses, right? The plus to supportability there is that there's less people asking, you know, how to write this Java code, because they're clicking the button.
**Antoine Toulme** 40:03 Nope.
Yeah. I'd like to see if it actually brings better discussions to your SIG.
That would be awesome.
I just don't know.
I'm afraid that… Yeah, anyway, I think… okay, I'll write up an RFC of some sort, open an issue, do something, work with you guys.
**Trask Stalnaker** 40:25 Yeah, I mean, essentially, I feel like it's a project proposal.
Yes. Like a SIG proposal, but you could… Start it as a sort of less formal Discussion, if you want to kind of gauge interest and get feedback.
**Antoine Toulme** 40:46 Yeah, I think if I propose it as a project, it's going to look presumptuous a little bit. I would like to also make sure that I create a number of consensus-based actions here, because it's… it cannot be me. It needs to be a member of Java, Python, Node.js, everybody needs to kind of be okay with this. It's gonna take some time to just find people Of course, you can present it as, look, this is time savings, you no longer need to think about some of the roadmap aspects of making your stuff available, we'll come and get it for you.
But I think it's, it's debatable. We need to make sure we're okay.
Alright.
**Trask Stalnaker** 41:26 Yep.
**Antoine Toulme** 41:29 Cool. Thank you.
**Trask Stalnaker** 41:31 Alright.
Well, see you, see you next week, hopefully, Steve, at the RPC.
**Steve Rao** 41:39 Yeah, yeah.
**Trask Stalnaker** 41:40 Awesome.
Alright.
Bye. Take care.
**Antoine Toulme** 41:43 Nope.
