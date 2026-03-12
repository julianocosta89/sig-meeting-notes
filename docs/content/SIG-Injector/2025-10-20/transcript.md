SIG: SIG Injector
Date: 2025-10-20
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Antoine Toulme** 01:15 Noted.
**Ted Young** 01:22 How's it going?
**Antoine Toulme** 01:24 It's going, just… Don't know if I have much…
**Ted Young** 01:31 Yeah, seems like… seems like no one… no one today.
**Antoine Toulme** 01:35 No… I don't have anything either. I… I started to just do a bit more of a job of cleaning things up, but… Yeah, it's… it's gonna be a long road.
**Ted Young** 01:47 Yeah, I just had a question about, you know, the current… current state of the repo. I'd like to… to throw some more people on it, if possible.
I'm waiting for Jack Berg to get back.
From parental leave, when he comes back in, like, a week or two, he'll be on my team.
Nice. And I'm also asking him to see if he's interested in being the TC sponsor for this, and get that job covered as well.
But…
**Antoine Toulme** 02:20 That'd be neat.
**Ted Young** 02:22 you know, we have other people, we're interested in helping get this thing over the finish line as quickly as possible, but I was curious what… you know, if I look at the repo today, it's like, oh yeah, works in these three languages, but, like, to what… degree… Are you… are you trying to flex that right now?
**Antoine Toulme** 02:44 Not really much, we just need to make a release out. That's the point of the discussion for the last two weeks, is just we've been toying… toying with the idea of making a release, and there's just two camps. There's… my camp is, we need to release imperfect software to get it tested and get some feedback from the community. Yeah. And Michele is saying.
I don't really care for that. I have my own way of consuming this software. I don't think a release can make a whole bunch of difference. I think if we make a release, then we enable more people to participate and help.
**Ted Young** 03:17 Yeah, yeah, I mean, if the argument is, like, Dash Zero's got away productizing it, you know, and so they feel fine, like, that's nice.
**Antoine Toulme** 03:26 Good for them, yeah, yeah, they're starter.
**Ted Young** 03:28 But…
**Antoine Toulme** 03:29 They have none of those things in place, they don't care, right? It's just…
**Ted Young** 03:32 But it's like, yeah, I wanna… I don't wanna start replicating that. I don't want the Grafana Labs approach to be like, well, it's not released yet, so we just… we just smushed this thing into alloy because we could shove it there instead of…
**Antoine Toulme** 03:49 Yeah, that would backfire for everybody.
The other discussion we're having is the RPM Debian packaging seems to be a topic of… it's not contentious, at least, like, it needs improvement. We… we have the scripts that I contributed early on using something called FPM.
I mean, Michael did give me some feedback last week, like, I don't think FPM is actually a great solution for… doing stuff, like, it's… I'm not sure why you handed… ended up with that, like, I don't know, I just picked up whatever had been there for years. If you don't think FPM is a good technology, let's hear you out, man. I really don't have a big opinion.
So he was going to work on that a little bit. I would say adding additional things like Ruby.
So it depends a little bit on what the speciality of people are. What I would say is that I try to lend Ruby, for example.
and it didn't work, and I realized that I needed to be very good with the Ruby SDK and understand what the Ruby SDK can do before I can make claims about… like, in a sense, you get the subset of what you can do in the first place, right? So you have to do… you have to be pretty cozy with the Ruby SDK maintainers, and get some feedback from them in a timely manner. It was like… because I'm like, okay, I think it works, and then you try it out, and like, I don't know how to write a Ruby app that actually would show those primitives.
Does that make sense?
**Ted Young** 05:13 Yeah, totally, totally.
**Antoine Toulme** 05:14 So, the guy was like, oh, just use Rails. I'm like, oh, oh my god, you want me to do a Rails app?
I don't know how to do that, like, is it rails new? Is there, like, what… and then, you know, he sends me, like, a sample that he's using himself. I'm like, I can squint at this, how do I justify… how do I know if it's working properly? Like, if… unfortunately, at some point, we need some people with, like, some deep knowledge of the SDKs to kind of show up and help run the last mile, especially for testing.
So that blocked me on Ruby. For Python, there is a cracker full of issues.
Because the… apparently there's, like, a lot of opinions about what should be said in the NVAR. You don't want to just replace NVAR, you want to just concatenate stuff on top of them. If you look what they're doing with the operator, it's kind of, Mash of things, where they take an existing environment variable, and they're like, oh, we need to make sure you can have the SDK auto-instrument the code, so we're going to prepend the environment variable with this additional path from some Python library, and then we're going to append to the end of that string with some additional things, like, this is like magic to me, right?
So… we're running into this type of, issues with some specific languages, and overall, what would be kind of neat is to also start, like, making this available, so I think people need to kind of… I need to walk in the shoes of this, make a demo.
And come back and say, I did not like steps 3 to 10, right? I think Jack Berg would also be a great guy to go and with the…
**Ted Young** 06:52 Yeah.
**Antoine Toulme** 06:53 a TC mindset was like, if I was to take this repository without knowing anything about OpenTemmetry, what are my first 5 minutes like?
And if you can answer that, that's already great feedback.
**Ted Young** 07:03 Yeah.
**Antoine Toulme** 07:04 So when you say you want it to work with the… you said with the hotel demo repo?
**Ted Young** 07:08 Like…
**Antoine Toulme** 07:09 I think that's a lofty goal, I was just like, can I do a… Can I… can I try it out? I haven't tried out BSIG yet, so I need to try it out and make sure it works the right way, and then I would want it to… we have an integration test that shows it works, right? I'm not just… we're not just bluffing the whole way, but… I'd like to see if, we can… do a bit of more of a demo, and especially with CapeCon around on the corner, I need to make my slides this week. So I need to kind of work on that anyway.
So…
**Ted Young** 07:41 Java? I mean, Java's the simplest one. I mean, it's, like, the most complicated way to set an environment variable ever invented, is my opinion of, like, the Java approach, right? But nevertheless, that's all it has to do, basically, right?
**Antoine Toulme** 07:56 No, Java's very mature compared to other is the case. It's not going to give us any trouble. Once you have it set up, we will just fly. And this is what you see in the integration test, like, we just installed Tomcat in this, and you… Tomcat starts to report in. I think that's a beautiful testament of how great, like, these ecosystem's coming together, and it tells a really nice story, so I don't want to go into murky waters and… Because, for example, even Node.js, you have NPM in the middle, people start to have opinions, why do you have this done this way? How do you install that?
We're… yeah. Right. So…
**Ted Young** 08:30 I wrote down in the notes that I feel like I see there's, like, 3 fronts here, right? There's… there's productizing the injector, which is, like, this is a mechanism, but we need to have a clear story about what's… what in OTEL is going to be driving this mechanism, right? Like… You know, you mentioned, like.
like, package managers, like RPM, but there's also, like, does the collector have this thing built in with the scanner, and it's using op-amp to, like, scan the system and then decide what it's gonna target? You know, that's more the approach we would take, probably, at Grafana.
The operator, is this thing gonna have it and drag it? What's its big Santa's bag of goodies that it's gonna bring with it? You know, like, how big is the…
**Antoine Toulme** 09:22 Yeah, actually, that might be a… There may be a low-hanging fruit is… So we've had a discussion about that. When we started, I thought we would just replicate what the operator does, which is that there's one image per SDK, And the feedback I'm getting from Best is, like, can we just make one image for everything?
And this way, you just inject one image.
you copy the right things on startup for the operator.
And then you're done. So we could simplify the lifecycle of the operator, we could make life much better for the operator moving forward, because it wouldn't have as many…
**Ted Young** 09:55 If you're doing gigabytes, if you do that.
**Antoine Toulme** 09:58 Maybe…
**Ted Young** 10:00 When you're late.
**Antoine Toulme** 10:01 Whoa!
**Ted Young** 10:01 Every kitchen sink we have in OpenTelemetry, all bundled up into one image.
**Antoine Toulme** 10:06 But it's… so it's appalling… it's appealing to them for a reason that's kind of weird, is that they would like it so that you could find So you would need to customize the behavior less and less of the time, because…
**Ted Young** 10:19 Yes. Yeah, caching, right? If this thing was just cached everywhere, it's nice. Yeah. And also, if you don't have it all in one spot, the next thing is like, oh, well, it scans what is available, and then it downloads things.
**Antoine Toulme** 10:32 Yeah.
**Ted Young** 10:33 Right, and now it's downloading and injecting and executing code, and that's not fun. You're gonna have people who don't want to do that. So I definitely agree that the, like, kitchen sink image is a thing people will want.
But you can also see people being, like.
That's… that's just way too big.
It's slowing down my deployments because I have to download.
**Antoine Toulme** 10:59 That's true, that's possible. I hope that there's enough caching in a way that it doesn't matter. It looks like the guys from Dash Zero are saying that it's not.
This is the way they want to go about their own.
Approach to implementation at this time.
I… I can… I can see that, because… who knows what's really running on your Docker image anyway? Why are you having… so, right now, as the operator, it's an opt-in mechanism.
For each pod, you're starting to tell us what exactly you want us to inject into.
Right? And as you were starting to take this indiscriminate approach, you're like, I don't really care, I'm just gonna mount everything and, overall, like, overload everything that you're doing with my little utility, so that if, and when the time comes, there's always a way for me to kind of, get that going.
I don't know if we're talking gigabytes, I hope not, but I'm… I think given the current, like, we have 3 languages, fairly small.
it could be okay. So… I'm intrigued.
**Ted Young** 12:00 There's also not just Gigabyte, there's also Providence is gonna show up here, you know.
Right, like, even within the contribib rep repos, we've got, like, lots of stuff, but you could ask, what's the providence behind all of this stuff? And there's a subset of it where we're like.
**Antoine Toulme** 12:16 That's true.
**Ted Young** 12:16 partner is the only people with keys to this code. And other stuff is, a random community member left this couch.
corner.
**Antoine Toulme** 12:26 And now it's here.
Yeah.
**Ted Young** 12:29 So…
**Antoine Toulme** 12:30 that you could have vinyl MPT scanning go crazy on this, yeah.
**Ted Young** 12:34 Right. But I don't wanna… I don't wanna get into that stuff with, like, the first version of productizing it, but… but it would be helpful to be like.
Okay, so this thing works fine for Java right now. So, saying, like, we could use just Java as, like, for the team or the people who want to focus on, like.
trying to get the… the collector, or the injector, or RPM, or the various things that are gonna, like, stand this up, and, like, what is this experience gonna be for hotel people could probably… start hacking away at that, and just say, like, just… just focus on Java for now, because…
**Antoine Toulme** 13:11 could do… if I was to look at a path to some value, just to intrigue the community, make it easy for them to adopt.
**Ted Young** 13:18 Yeah.
**Antoine Toulme** 13:19 let's say, let's start with the Docker… the Docker story, because the Docker story has some premise, like, it's… it's on premises. What we could do is, We create a Docker image, and it's shitty, right? It barely works. It gets you where it needs to be. Then you start to play with it in OpenTermity Demo, and you make a… case of it to make a blog post, like, hey, here is, OpenTermity Demo plus this thing in, look, it starts to report in, right? Didn't have to do as much work as before. And then, you could productize just that slice by making a helm chart for it.
And then the whole time, you're just trying to get more people involved by saying, hey, we're expanding a little bit, so see how you could just help with a demo, you could just help with the chart, you could just help with this.
is… rather than trying to get the base layer really nice, showing the whole thing, and showing all the gaps in the middle, you get 10 people to be helped instead of 3 who are really good at Zig, because no one cares about Zig, right?
So, I think that's a way to kind of engage, because I'm just worried that we need more people to play with this, and it's super complex and technical. I was just trying to make slides about, like, even how the process is being started in Linux, to showcase how preload.so is so much safe.
It's not that easy, actually, right?
**Ted Young** 14:35 Yeah.
**Antoine Toulme** 14:36 Just, like…
**Ted Young** 14:36 Java's ironically the worst thing to start with, because one of the weird things I encounter here is, like, it's not hard to install the Java agent, right?
You know, and so, people sometimes don't understand the value of this thing.
**Antoine Toulme** 14:51 Right, right.
**Ted Young** 14:51 I've encountered this this past week, talking to people about it, so in that respect, something like Ruby or Node.js or, you know, whatever would be, like.
**Antoine Toulme** 15:01 Okay.
**Ted Young** 15:01 I do think there's an exception to that, though, Ted, and that's people that are running, like, WebSphere, and you have to dig through and find out, like, how the environment's actually configured, because.
**Jason Plumb** 15:11 The scripts that launch some of these servlet containers are so complicated.
**Ted Young** 15:15 Absolutely, like, there's also, like, what… the… what is the right version of what to get in there is also… Yeah, totally.
like, OTEL doesn't have quite enough backstory for there to be, like, a lot of options there, but still, you know, like, there's some complexity there about, like, which one of these things do we install based on what kind of Java is running.
**Jason Plumb** 15:39 like, I think Tomcat has, like, 3 different scripts, and then in some cases, you're supposed to, like, bring your own and name it something special, and we'll source it if it's there, and…
**Ted Young** 15:49 Yeah.
**Jason Plumb** 15:49 Yeah, so having, like, one standardized way of doing it for some… for some people is helpful.
**Ted Young** 15:54 Yeah.
A complete believer. I guess what I'm saying is, like, I think the sooner we have, like, a working demo in hand.
the sooner we can get other people in OpenTelemetry involved. And I really think we're not just talking about… making something on the side. I'm… the whole GC is looking at this, like, we want to do a big push into productizing open telemetry, and… And kind of… saying the future is the instrumentation needs to go upstream into native instrumentation, but that's a multi-year effort, and… but at the same time, operators need to install all of this stuff, and we don't actually have an answer for that. We can make the docs as good as possible, and it still won't Won't work for a whole bunch of people in our community.
**Antoine Toulme** 16:43 Yeah.
**Ted Young** 16:43 An approach to installing this stuff.
**Antoine Toulme** 16:46 You know, it's also, you don't have a canonical, like, you don't have a, a place where all those things are being installed that is kind of standard, like, you still need people to kind of go out of their way, and one of the topics of discussion in Injector last week was Michele was saying, I can make it so that Ubuntu would make this an official package in a repository.
That's a game changer, right? Because you don't need to add, like, some random PPA thing to add this, because that scares people off.
Yes. Easy, right? It just takes me.
**Jason Plumb** 17:18 Maintainers, I mean, that's true of any, like, Debian-based thing, it just requires maintainers.
**Antoine Toulme** 17:23 Yep.
Yeah, but… so we're talking about having… hey, that's… that's a discussion that's kind of up for grabs. We're like, okay, so we want to have an RPM for injector, right? Or Debiant. And so we're gonna have the zip code for this preload.so hook gonna be in some package, and will be distributed through that mechanism. Now, do we make the Java SDK part of that Demon package?
I don't think so.
Right.
Cause… Who are we to?
**Ted Young** 17:54 I mean, so what.
**Antoine Toulme** 17:55 Boo that.
**Ted Young** 17:55 What is it? Right, so you have, like, a bootstrapping thing where you RPM install, and then that thing goes, like, cool, for my next trick, let me download Gigabytes.
**Jason Plumb** 18:05 agent.
**Antoine Toulme** 18:07 I mean, but that's not gonna work, right? So instead, what you would do is you would do, like, the right way, which is you have Debian packages for each of the things you want to install, and there are dependencies between them.
So when you pull on the injector, it says, oh, you must mean that you want to install Java 2 and Node.js, and Python, and whatnot, right? And you go, mmm… Yeah, maybe it's optional. Maybe it's required.
**Ted Young** 18:31 But there's also, like, the collector is part of this, too, because I get that… that at Dash Zero, they might have the approach of, like, we just want this thing to automatically, aggressively attach to everything it finds, but I think you're gonna find plenty of people who want… Managing this stuff through the op-amp and the control plane to work.
Away from a world where we're telling people they have to run, like, 5 agents to run OpenTelemetry.
**Antoine Toulme** 18:59 true, but for… for… so the collector, you know, PAMP, and all that stuff, it can be a… almost like a… for example, you could make it so that the config file that is related to the Java SDK can be managed through AppEMP.
Right. So, whenever you reload, or you stop, you start your job, process, poof, it, you know, pulls up the new version. In a sense, this is, you make it orthogonal, like, there's… there's a… a separate install, you say, I want to manage this with the… you would even hear… my move would be to say, first you install OPAMP on all your machines, because then you get full control of everything, and then you tell OpAMP, hey, now install… install the injector on all my machines, because then we get full malware-type insertion of every program.
Right? And the injector is going to say, okay, but, you know, we can… Michael was talking about that, it's like, if you remember the gold days of… the golden days of Debian packages, you have an actual dialog that says, what would you like to install today, right? And you go, Java, Node.js.
Right? And installs those three additional packages for you as part of that. And then you have the great installation story where everything gets installed, managed through that. There's a non-interactive mode where you don't have the Java stuff installed by default, you have to, like, spell it out, right? And then it just starts to work.
**Ted Young** 20:20 I'm totally with you on the idea, also, of, like, For environments where it's available.
having package management be the way things are installed, not… you know, there is some of this, like, the collector, you can get a new image of the collector through op-amp, and it'll boot itself up, and there's some bootstrapping there.
But I would love it for, like, where package management is available, if it's, like, if this thing's gonna be installing these things for you, right? Like, first the collector, like you're saying, you have some scanner, and it installs the injector, and then it sees it needs Java and Python, so it installs those things.
But it's just driving the package management to do that. To me, sounds like a totally reasonable experience for situations where that's available, right? Where it's like, let's not reinvent package management in Providence and, like, all of this other.
**Antoine Toulme** 21:10 Well, you cannot. You'll never win that one.
**Ted Young** 21:14 But what about environments that… where Debian is not there? Is that… is… are there Linux environments we need to support in production for, like.
customers, where we can't use…
**Antoine Toulme** 21:27 The other half is RPM, right? So the other half is RPM, Usually, there's some level of support for DBN and RPMs in most Linux distributions.
**Ted Young** 21:37 Right.
**Antoine Toulme** 21:38 But I would keep it… I would say I don't really have a solution for 100% support of everything, and I have to live with that uncertainty. I would love for people to come back to me and say, my Arch Linux Gen 2 version of Slackware that I compiled myself lovingly does not work the right way when I, you know, set those JC tags when blah blah blah, I'm like, great, you know, did you want to help with this?
**Jason Plumb** 22:01 Or, you realize that this package thing has been a problem for so long that people invented snaps and app images, right? Like, then you just go the completely other approach. You're like, well…
**Antoine Toulme** 22:12 Oh, yeah, I mean, Snap is just fine by me, I have no qualms with APT or Snap to stop him, I just want to not invent our own thing.
**Jason Plumb** 22:20 No, we can't.
**Antoine Toulme** 22:21 The only thing, like, if we start to hear about, we're gonna install these things via OpEmp, I start to shrivel inside, because I'm like, my God, just recreating a whole bunch of hosts of problems, where there's gonna be a problem, you know, environments which are, I guess.
**Ted Young** 22:37 Not seeing that's a problem, certainly not today.
**Antoine Toulme** 22:40 Yeah, today's just a good program to mention that. It's a good day to mention the DNS, but Yeah, I mean, just, I think we should make it simple for people, because if… Normal developers these days, when they want to install Tomcat, it just simply gets installed Tomcat. Why is it that OpenTemmetry, you have to go out of your way and go like, I'm gonna go to a website on GitHub and download something? Why?
**Ted Young** 23:04 My curiosity is more, do we still, no matter how much we try to lean on package management, do we, Emma, end up with also, like, something that's more like an image-based… approach.
**Antoine Toulme** 23:16 Bush.
**Ted Young** 23:17 Or do we have to be like, we don't have to support that at all?
**Antoine Toulme** 23:21 No, I think you need a… you mean a Docker image?
**Ted Young** 23:24 Just any… yeah, a Docker image or any kind of approach where there's a blob that this thing…
**Antoine Toulme** 23:31 I think it makes total sense to have a Docker image for this, because look at your stupid Docker Compose use case, or ECS, or… and then you can expand to Kubernetes. This Docker image packaging is easy as hell to just get on top of it. The operator does something that's… kind of silly, where they use a document as an init container, and they copy the contents of that container over to the main container before it starts, so that by the time the container starts, it's already been poisoned with your injection code, so that the SDK gets picked up.
That's how they do it, right? We don't have to be that blunt moving forward, but it's just a limitation of what communities allows us to do. In the case of a Docker Compose, you could mount it as an additional container, and then it runs on its own, and you could just share volumes or whatever. I don't know. I…
**Ted Young** 24:25 Another dumb fucking question here is, like, you know what the most common demo environment is for OpenTelemetry?
**Antoine Toulme** 24:34 eager, and… Some graphing in the back.
And…
**Ted Young** 24:37 The spectacular.
**Antoine Toulme** 24:38 Bobos. Oh, my goodness.
**Ted Young** 24:40 Right?
**Antoine Toulme** 24:40 Oh, and so you're worried that it might not work on Mac the right way, because, well, there's no pre.so in Mac anyway, right? So, you're kind of.
**Ted Young** 24:47 Right. Right, there's literally no way to…
**Antoine Toulme** 24:51 So it's…
**Ted Young** 24:52 There's really no way to demo this.
Never. Never. When we're doing it on a Mac, right? Even…
**Antoine Toulme** 24:59 Duh.
**Ted Young** 24:59 rides, and… All of that.
**Antoine Toulme** 25:02 You should be able to merge it on a…
**Ted Young** 25:08 I believe there's a virtual machine layer happening in Docker on Mac, right? So that you can run all of your Linux…
**Antoine Toulme** 25:15 Oh, yeah.
**Ted Young** 25:16 I'd be insane.
**Antoine Toulme** 25:18 Yeah, you're right. That's gonna be a big, dumper on everything we try to do.
**Ted Young** 25:24 Because, I mean, and it sounds dumb, right? Because it's like, well, this is for Linux, but it's like, if you can't… if we're gonna be like, this is the default way to do it with OTEL, and we can't demo it on people's laptops, that's actually, like… that, from a product perspective, that's problematic.
**Antoine Toulme** 25:41 That's true.
I don't have an insert.
I don't know that preload.so works on that one, yeah, preload.
**Jason Plumb** 25:54 Look at this.
**Ted Young** 25:55 Interesting.
**Jason Plumb** 26:01 Awesome.
Just thinking of, like, macOS, I'm like, what OpenTelemetry packages are available for Homebrew? Apparently, the CPP library.
Sorry, sorry.
**Antoine Toulme** 26:18 I don't know, I don't know how that happened, but…
**Jason Plumb** 26:20 That's new to me.
**Antoine Toulme** 26:21 It's new to me, too. Huh.
**Jason Plumb** 26:25 Oh, how the…
**Antoine Toulme** 26:26 Love.
**Jason Plumb** 26:26 in there.
**Antoine Toulme** 26:27 Yeah, of all of them, like, the collector makes more sense to me.
**Jason Plumb** 26:32 Yeah.
**Antoine Toulme** 26:35 We still don't have a good story about, I mean, in general, like, the problem of the injector is that it's not the prime of the injector, the problem of injector is the packaging and installation of hotel, so that it's standard installed on your freaking box by the time you get in, and… We're having dumb issues, so… But right now, like… It's kind of where the crossroads on the RPM Deviant packaging is.
we would need to have a RPM or DBIN package for every one of the SDKs so they're easy to install.
We don't have one, so… I was, trying to make sure I show up at your Unplugged Day in Belgium in February to discuss that.
**Ted Young** 27:18 Hopefully we can get something before Feb.
You know?
**Antoine Toulme** 27:22 Yeah… I mean, I'm starting to get Jason in those discussions also, because I think from… he's got a very different perspective, he's got so much more richness from the Java SDK and the challenges they have to maintain that stuff.
I've already mentioned to the Java maintainers that I want us to have a better packaging story around not just the Java SDK, but even, like, JMX Scraper and things like that, and the feedback was very honest. It was like, hey, Antoine, this is just too much.
you're killing us here. Like, this is… we're already pretty stretched thin with what we have, and it's a different specialty. We know how to build a Java file, we know how to make it so it's downloadable from some central repository, but… I don't think you can expect us to make an RPM for this. That's crazy. That's not gonna work out.
**Ted Young** 28:11 I don't have a solution for this.
**Jason Plumb** 28:15 And really, I mean, the packaging is kind of its own project, I think is the way that a lot of us look at it. It's like, the source is out there, and we publish and build artifacts, and you have all of that available to you to package up in any way that you want to, but the packaging itself is kind of a different project.
**Ted Young** 28:31 Yeah.
**Jason Plumb** 28:33 Even if that's still part of OpenTelemetry, it's still a separate project from… developing. Just like the instrumentation agent is a separate project from the core SDK. Like, those are… those are related, but they're different projects, and they do different things.
**Ted Young** 28:50 why I'm sort of wondering if there's, like, a step zero, which is to figure out what would get packaged up into the RPM, right? And, like… You know, if you were gonna say.
Step one is, you know, you're using package management to get this blob of stuff, but if we even just went to step zero and say, this blob of stuff appeared magically, somehow, by some package management system, would we put it? What's in there?
**Antoine Toulme** 29:21 Yeah.
**Ted Young** 29:22 Obviously, it's like, bro, we do not have the cycles.
or the know-how to give you what you want there, right? Like, that's a great thing to identify early on, because that's going to be the same in every other SIG.
**Antoine Toulme** 29:35 Yeah.
In that case, we can ask for forgiveness, because we might make calls for you, but like, okay, Jason, we're gonna stick this Java under OPT, OpenTelemetry, Java-sdk, blah, and you're gonna be like, dude, how do you version this?
I don't know.
Yeah. Go with it.
**Ted Young** 29:53 Yeah, I would love us to start doing that. And that also sounds like the kind of thing that, okay, maybe the Java maintainers don't have the expertise, but at least you don't have to be a fucking ZIG expert.
to figure out…
**Antoine Toulme** 30:07 Yeah, there's a middle ground here, right?
**Ted Young** 30:09 So we… there are other people we can tap, potentially, to… to… to have a look at that part of the problem.
**Antoine Toulme** 30:16 So going back to proving the point, and getting the value, and getting more people involved and interested, I still think that Docker image gets you, to the demo that you need to be able to pull together.
It's, it's, yeah, maybe we get there, and we're able to do something meaningful here. And I'm in love with the idea of a home chart, not because, Because I pulled that stunt before, and it worked. And it's been amazing for me, because the charts are really good at doing one thing well, and get less maintenance burden than most things, which has been a bit weird. Good example is the target allocator was part of the operator.
and you only go get it through the operator, which was a pretty heavyweight install, and I moved, like, just that section of the code and made it installable, like, here, just install this, and you get that in your community's vanilla environment without having so… so much OpenShift overhead.
And all it's doing is that it's deploying a Docker image as a pod in your environment, doing the right thing. So we could do the exact same thing here.
I just don't know.
How smart we have to be about this, but it would… it would be meaningful.
**Ted Young** 31:29 Yeah.
**Jason Plumb** 31:32 I have to dip for another meeting.
**Antoine Toulme** 31:34 Yeah, I think we should… We should close this up.
**Ted Young** 31:38 Yeah, that's a fine update. You know, for my end, it just means, yeah, step zero for packaging is just figure out the folder structure for this thing. What would we shove into this folder, and what would that look like, right? And then we can start… like you're saying, we can put that in a Docker image, we can put that in RPM, we can put that in various places.
But just… just getting… and I… I, in general, agree with you, Anthony. I think we're… it's better to ask forgiveness and to ship… half-working stuff, like, it's better to have, like, step zero be, like, wrong, and just throw it in front of people, right? Because we'll get faster feedback from them, being like, this is wrong, than asking them to just…
**Antoine Toulme** 32:25 Hello.
But for what it's worth, that's not the opinion shared by Michael. He doesn't like it when we… I'm a specialist of faceplants. That's what I do all day long, because there's nothing that works better on the internet that's showing something wrong.
You get 10 people to show up and tell you that they know better, and frankly, I have to abide by that rule, and that they know better, for sure.
It's not something that, azure is more like… being aloof about this, I'm like, you know, I don't want to really play this game.
And I get it.
But, yeah. Wow.
**Ted Young** 33:00 Well, but again, it's a community effort, it's not just them.
**Antoine Toulme** 33:04 Nope, it's not. Have a good one.
**Ted Young** 33:05 So, we can care more about it than they do, and that's okay.
**Antoine Toulme** 33:10 Yes, proof.
**Ted Young** 33:11 If they're like, we don't care so much about this part because we're just going to… Have our own… Non-Hotel injection mechanism for it, sure.
**Antoine Toulme** 33:22 Yeah, they're way ahead of us. They've done more in this payment than we have, and this is great because it validates the approach, but we just need to kind of keep together and kind of move forward.
**Ted Young** 33:32 I would say I'm with Michelle when it comes to, like, this… if we were still doing this in C, you know, I feel like Zig is supposed to give us some protection from shipping something dangerous, and I would say the dangerous parts are the parts we don't want to ship.
Alpha-level stuff, and be like… hopefully doesn't eat your fucking computer, right? Like, that's the part where I'm like, yeah, if we want to be cautious there, that's okay. But with the packaging and everything else, we should just… throw out there and be like, what? Is this what you want? Is this what you seek?
**Antoine Toulme** 34:08 Perfectly. Yeah, yeah.
**Ted Young** 34:10 Yeah.
**Antoine Toulme** 34:11 Cool, man. Alright, gonna run. Take care. Bye.
