SIG: SIG Injector
Date: 2025-11-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

atoulme 00:02:22 Hey, Jeff!
Jack Berg 00:02:25 Hey!
How you doing?
atoulme 00:02:28 I'm okay.
I'm, what, brings you to this humble sign meeting?
Jack Berg 00:02:37 I am ostensibly the TC sponsor, so, I'm… I figured I'd start paying attention, and .
atoulme 00:02:46 Okay, okay.
Jack Berg 00:02:47 And also, and also Grafana is interested in this project, so, you know, I need to get caught up to speed and figure out what the state of things are, and if, you know, if and where there's any places I can help.
atoulme 00:03:02 Okay, so… I can tell you a bit where we are. I think we're due for a new release, that's gonna be the gist of it.
Jack Berg 00:03:09 But you said you cut a release? Sorry, I didn't catch that.
atoulme 00:03:16 We need to get a new release, we are due for that. We did not.
get me… Alright, yes, the docs… Might want to get to the meeting notes, and I'll share them with you.
Jack Berg 00:03:29 I'll get the meeting notes, you know, started, I guess, with a little template.
atoulme 00:03:37 Yeah, there's a… I'm about to declare bankruptcy in Canada.
Sorry.
Okay, pump it.
Thank you.
Okay, so, So we did a… last week, there was a bit of discussion about how things went at JupCon. I think it went over pretty well.
I think there was actually a Graphene employee who came and joined us, Raphael.
We discussed that we need to have a crisp story between Bobby, Bela, whatever, and what the injector does, so that we can, avoid confusing people, because it's, it's pretty easy for people to kind of start, like, what, what is all those options I have to deal with, right?
So Obi makes a ton of sense. It's a useful technology. How it plays with an injector is more like a mechanism thing, right? So, how do you stop one versus the other?
The interesting tidbit from Raphael is that, oh, if we find out that you're already instrumented with, Hotel SDK, then we don't try to do anything without it, because there's no point.
Right?
So… That was great to hear, because that means that we could play a little bit of a lazy approach, where we start with injector trying to inject whatever he can, and then Audi comes in and gets the rest, like, the 99% of the CPU processes that you might not have a SDK for, right? Think curl, for example, right?
Which is super neat. We really just need to leverage that as much as we can.
So the story becomes the overarching installation and product story around OpenTeometry. It's like, how would you install OpenTeometry on a host that would do all the Java SDK, all the Python SDK, all the Node.js SDK, and then also get everything else that you're not thinking of using Bobby?
Right.
Jack Berg 00:05:41 Maybe you all reached this conclusion already, but, like, should Obi be just another thing that the injector installs?
atoulme 00:05:50 The problem is the lifecycle is a little different, so you can install Obi, and you can catch on to in-flight processes, you can do a lot of things.
So… but I think the installation story needs to be simple for people so they can match onto it.
If that makes any sense, so… The way we're thinking about the injector right now is that it's going to be a series of Just for host… the host story, right? So you should be good about that. We are going to have divine and RPM packages that are going to make it easy for people to install the injector on a host in a nice way.
We are having discussions with Mikarena Dazzio, who's another maintainer.
to have a series of Debian RPM packages that would, instead of having an injector being this weird contraption, it should have dependencies on a RPM package for the Java SDK, an RPM package for the Python SDK, an RPM package for the Node.js SDK, for example.
Okay.
Jack Berg 00:06:45 So, like, a composition thing, where there's, like, one overarching OpenTelemetry RPM package, and then there's, you know, that has dependencies on smaller pieces, so you can kind of… Okay.
atoulme 00:06:56 That's right, so I think we're missing a top level, which would be the OpenTemmetry package, which would be installing the injector and Obi.
Jack Berg 00:07:05 Okay, so then, okay, so then the top level… okay, so there's a low level… Injector type of package, which all of the language-specific packages would have a dependency on, because they're all leveraging the injector to install the relevant auto-instrumentation tools.
atoulme 00:07:24 Now, in reverse. So, the injector needs the Java agent to be there, right? Otherwise, it can't do anything. So, the injector depends on the Java agent.
So, if you think about it in different layers, it's like, I just want the Java agent, just install this RPM. I just want the injector, install the RPM for injector, it will install the Java agent for you as a dependency of itself.
Oh, I don't care about anything, they just want to have all the data I could want and wish for. Install the OpenTMC RPM. It will install the injector, which will depend on Java, which will install the Java agent.
And it will also install ABI, which will then bring whatever dependency it has.
Let me…
Jack Berg 00:08:03 OpenTelemetry package is overarching. It depends,
atoulme 00:08:09 Yeah.
Jack Berg 00:08:10 and…
atoulme 00:08:10 Yo… We don't see that thing.
Jack Berg 00:08:14 So it depends on things like the collector, did you say, package, an OBI package?
And that.
atoulme 00:08:23 an SDK.
Jack Berg 00:08:23 pay packages?
atoulme 00:08:25 Yeah, I could do that.
Let me see, I seem like my internet is not gonna work, so that means I do a terrible type of PowerPoint.
The way I see it… Which should not be a… it's not a final, it's not a final thing. Let me see… draw… I want some shapes, can I get some shapes?
Jack Berg 00:08:50 Are you trying to share right now? If you are, I can't see your screen.
atoulme 00:08:53 Not yet, I'm trying to find out how to add shaking PowerPoint, which is worth more.
This is so much worse. Okay, No, I'm sorry, the job is making us move from, from Google to, to PowerPoint in 360, so I end up doing web stuff.
So, if I want to be… Okay, so I got a horse… oh my god.
Oh, no, this is not gonna work. So I've got… no.
Jack Berg 00:09:29 Are you allowed to use draw… are you allowed to use… oh, whatever, just… just do this. This is fine.
atoulme 00:09:34 I'm also in a cabin somewhere, so I don't have great internet. Sorry. So, I'm gonna go and install the hotel package, right? So, hotel… And that hotel package is going to depend on injector.
Injector…
Jack Berg 00:09:58 Yep.
You don't have to write it all out.
atoulme 00:10:00 And then it's going to depend on Bobby, next to it.
Because I'm hoping that Obi will have a RPM or the intake gauge at some point, right? That's the idea.
And so, those two are installed by this.
And then this guy depends on the, SDK.
Right, so each SDK is gonna have its own package eventually. That's the hope. We want them to have Even if we do it for them, we would like each SDK to be installable on its own.
So, depending on your level of expertise, let's say you know exactly what you're doing. I just want a Java SDK. Just install this top thing, the leaf here.
Oh, I don't care about how SDKs are installed, I just want the injector, install the injector, we'll install the SDKs for you.
I don't know what I want. I want all OpenTemmetry. I want the experience, right? Okay, install the OpenTemmetry package, and we install the whole kitchen sink. Everything they can think of, they could install, right? And that goes on your host. So, for example, the collector, you're right, could be another package.
It is available as a package right now, so you could do this, right?
So you could do collector… Oh my god.
Depends on…
Jack Berg 00:11:12 So one issue with this is, like.
Can you install the SDK packages ad hoc?
atoulme 00:11:20 being present.
Jack Berg 00:11:20 presumably be able to. And what do those do without the injector present?
atoulme 00:11:24 If you're intent on it, we can give you the environment variable that you can use to do the injection yourself.
I've done it, I was just doing this over the weekend. I had the need to do, injection for Tomcat, so I set the environment variable Java tool options.
And I set it to load up the Java SDK, so, self indices.
Okay. Sensible.
Jack Berg 00:11:51 I got you now. So then, those, those SDK packages, when you install them, they are just going to download the auto-instrumentation package for that, like, relative language to some well-known directory, essentially.
atoulme 00:12:06 That's right. You just use one on your feet.
Jack Berg 00:12:09 you're on your own for installing that auto-instrumentation package in your language of choice, right, using environment variables, or however else you want to do it.
atoulme 00:12:19 Yeah, you could just do NDM install at this point, right? And you can just do a MVN Maven unload, or whatever you want.
So options abound when it comes to this. I was just going to show you… just an example that I was working on this weekend for some come with different engagements. I have a Docker Compose here.
I have the Splunk Hotel agent Java Jar, right? This is just the branded Splunk Hotel version of the OpenTeometry, Java agent.
I'm gonna mount this under bar, Spunk Hotel Gel Agent on some Tomcat image that's, like, super standard.
Okay?
Now, what do I do? When I want to run, When I want to run this, I just put the Java tool options right here.
Jack Berg 00:13:05 Yep.
atoulme 00:13:06 And then I can put some OTL endpoint, and we're good.
So, if you're on your box, and you know what you're doing, you could just get by with just a JavaTP, you don't need the injector.
Because you know better than anybody else, like, you have a really good handle over things, right?
But the population we're addressing with this are people who don't want to think. Well, like, I'm sorry, I don't care. I have thousands and thousands of machines. I am, like, in… you know, I have 15,000… this is… this is real life, right? I have 15,000 Linux boxes that are in the wild that are unable… I can't even switch into them, I can just do, like, some remote install or some package, and we're just going to run this, right?
Jack Berg 00:13:48 Yeah.
atoulme 00:13:48 I think we need to target these injectors, like the 2 minutes… I have no time to test open telemetry today. It's 4PM on a Friday, I want to get home. How do I test this so my boss can get off my bag?
That's.
Jack Berg 00:14:03 Yeah, no, I got that. So the… the value of the individual language packages, then, is to sort of… provide standardization about the download process, then, for… let's just take the Java agent, for example. So, you know, you can already do what you just shown by, like, you know, curling it, right? Curling the particular version of the Java agent, and then setting up your Java tool options the same way. And so, like, you know, that's a little bit bespoke, because, you know, everybody's going to have to add that download instruction to their Docker file, or, you know, whatever their base images are.
atoulme 00:14:41 Wow.
Jack Berg 00:14:42 And so, you know, it's, I guess, a little bit easier to do a, like, you know, an apt-get update, apt-get install OpenTelemetry Java agent, or OpenTelemetry Java, something like that.
atoulme 00:14:54 Huh?
And the security can be happier with you, if you do it this way, right?
Jack Berg 00:15:00 I'm installing some tools on my Linux machine now. I'm, like, I just did, like, a fresh install, and, like, you know, I have to do things like install the GitHub CLI.
And one of the things I came across with that is, like, you have to, like, you have to configure your machine to trust its, it's, what do you… it's keys? It's signing keys, right? And to, you know, and to register this… the, the, the package… what do you call it? I'm not… I'm not as familiar with, Linux…
atoulme 00:15:36 And that.
Jack Berg 00:15:37 repository.
atoulme 00:15:38 that you need to add to your sources.list, yes, correct. And then you need to add it to your keyring so that the pop key will be, allocated, like, you'll be able to trust the explicit key, yes. Yeah. Right, okay.
Jack Berg 00:15:49 You gotta update your keyring, gotta add it, like, you know, your own custom repository location, right? So, we would probably have to have those same things for open telemetry, right? We'd have to have our own repository where we're publishing this to, and, you know, steps to trust our keys.
atoulme 00:16:07 This is a really difficult type of… it's not difficult. It's just painful, How much do you know about that? If you want to talk about that, that's a fun topic.
So, I guess…
Jack Berg 00:16:19 I don't… we don't need to go into the weeds of that, but, like, I'm just… I'm just thinking out loud about the trade-offs between having every… having the canonical instructions be to curl the Java agent from, like, a well-known, like, URL versus a package manager solution where you have to configure your system to trust the right keys, point to the right repository, etc. Like, you know, if you have too many steps to use our package manager solution.
And you kind of reduce the benefit of it.
atoulme 00:16:48 That's true.
Yeah, eventually, so, it depends a little bit on the maturation we're looking for. So, to answer you, right now, you would need to do that. We don't have a repository for RPM deleted packages, and it's not offered by GitHub either, because it's actually pretty difficult to manage those type of repositories.
They need to build indexes, they're front-facing the internet, they get a bunch of, like, dumb traffic. You have to pay for, Artifactory, or you can do some things with it free, which require you to do some level of upkeep. It's not free.
So, for a little while, I think we could get by with either, manual ZBN install, so KRL for ZBN, and then the dev file, and you install it using, ZPKG-I, which gets you pretty much the same conclusion as where you would read with KRL.
the, Eventually, the idea, discussing this with the injector SIG, was that we would want this to become part of the default Ubuntu repositories. So we would actually make this part of the default distribution.
That's a really big endeavor, not because of the technicality of it, but just going through the hoops of getting it adopted as a… either Debian or a Ubuntu package.
Jack Berg 00:18:01 Yeah, like, just the other day when I was installing a fresh Ubuntu on my server, I was prompted for what, what packages I want to install by default, and you know, you have things like OpenSSH Server, but then also Prometheus was on there.
And, like, you know, that, like, you know, Prometheus made it into the default list, and there's only, like, 15 or so in the default list that you can choose from. So, you know, it'd be amazing if OpenTelemetry was in that list.
atoulme 00:18:26 And I think this is what people want, right? This is what our user community would want to be able to see, like, I need this to be loaded on any Ubiquito box that I install by default.
Jack Berg 00:18:35 And that's a novel goal. I think we need to take steps toward that. Right, right.
atoulme 00:18:40 we don't have to be there tomorrow. We also need to be able to signal to people where we want to be on that. There's, there's more than just Ubuntu. The other one is, of course, Red Hat. So for Red Hat, we also can work closely with that community to certify your packages, make them part of the defaults that people we use. So we're doing that, frankly, from a vendor perspective. We're in those discussions to make them certified, but eventually, it makes sense for us to also start to just make that a default for the open source as well.
We just need it to be kind of mature across the space. So the vendor stuff is kind of easy, because we're like, oh, we have dedicated support team, we can take care of this, right? When it comes to support with open source, we need to also be good about, like, setting some boundaries and understanding better how we're going to work on that. So I think every… every of those items take a lot of time.
I think having maybe an APT repository in some intermediate step, that might be great to learn more about what type of patterns we see, who's using what, to install everything all the time, what type of versions are you using with.
as they're trying things that we should not be, doing, like, maybe some telemetry there could be useful for that type of use cases.
But that's down the road. Really, also, like, so we've had… I've had discussions with Trasp and others, where I've put them to Sam's like, you, Java maintainers.
Yeah, you were not around for that discussion, because, you know, you were away for the one. And I think it was good for me to concentrate on it, because, frankly, I think the ejector's not to that level of capacity yet, but when I wanted to have a discussion with other SDK, and Java is, in my opinion, the most mature, just because I know them.
I said, what's your future of your packaging? Like, as a Java guy, I know. A Java file? You're done, right? A Java file pushed to Maven Central? Wow, this is as good as it gets. This is gold standard. No need… why are you talking to me about RPM? Like, you're pissing me up for it. Like, go away, right? I don't want to talk to you.
But that's not how people consume the stuff, right? So… We need to…
Jack Berg 00:20:44 Now, some people consume the stuff, not all people.
atoulme 00:20:47 all people.
The Java people will do that. The Java people are like, oh, where's your Maven sample artifact? They know to go through MVN repository, they know… they know how to go for group IDs, and all that.
Jack Berg 00:20:59 The sysadmin will. The sysadmin will.
atoulme 00:21:01 This is… this is just a… yeah, this is… we bought some off-the-shelf Oracle software in Java.
We don't know how things work inside. We just want this to be so that it continues.
So for those people, I do believe that having an RPM obsibian would make sense. But the discussion with trust I was very careful not to… I was looking for commitment, or understanding the interest from the JSIG.
Would you be interested in maintaining a daily and marketing package yourself, right?
And the answer was clearly no. That's not what we do. This is not what we're good at. We don't want this to be a duty that we have to be on top of the existing duties of the Sea.
And it might make sense to offer a packaging SIG. A packaging SIG which would then be responsible for all this minutiae about dependencies between packages.
of the release train that is starting to be talked about by often in some cases. How do we… how do we orchestrate a mindful release where we know that all those packages are compatible with each other and work together well?
That's right.
Jack Berg 00:22:01 Yeah. So…
atoulme 00:22:02 I… I think I didn't want to… push too much, but it might make sense to start into that, and, start into that into the new year, or maybe before, to push that message. It's like, you're going to have a much better time as opportunity moving forward, because we're thinking about your use case as a user who wants to install and update before they see everything that we ship.
Because, you know, curling a Java jar, easy enough, but updating a Java jar 3 months in, 6 months in, 2 years in, that's a different discussion. That's what people think about now, right?
Jack Berg 00:22:35 Yeah, yeah, and, you know, there's a couple of other related things. I was thinking the same thing, so that's one of the benefits of the RPM package is, you know, there's a well-known update path, right? You, APT, upgrade open telemetry Java.
And… But we gotta figure out what the story is like that, like, okay, so it's not necessarily the right thing to do when, if you call upgrade to erase the old version of the Java agent on your file system and have the new one. You want to… you want to be able to maintain both artifacts, for example, and maybe have some, selection criteria in terms of, you know, whether you select, you know, version 1 or version 1… or version 2.
So that's one thing, and then you want, sort of, like, the other benefit is, like, when you have RPM packages, you sort of drive standardization around configuration for these things. Like, you could have a, you know, depending on the language ecosystem, you could have, like, a standard A declarative config file that's shipped with the package, or a standard, like, file that exported environment variables that, like, get you reasonable defaults for that, For that language ecosystem. And, you know, maybe they're heavily commented, so you can, like, you know, uncomment things to change the behavior, or, you know, just, like, you know, like.
update to suit, and then… and then, you know, do something to reload. So… but you know that all of your configuration is going to be in this… this well-known location, so that if you do update your, your Java tool options, you know where to look for these things. It's always going to be in the same place.
atoulme 00:24:12 Yeah, exactly so. Wow.
I think… and we're going to find those things once we're in that… pretty much we enable this, and then 10 questions will come up, right? It's like, oh, but how can I get an example of that? Or is there a way for me to get even more, like, the configuration, the palliative config right now is kind of toothless, because it's not shipped.
The moment you start to ship it by default into every install.
You're having a very different conversation with people.
Jack Berg 00:24:40 It's shipped for Java.
atoulme 00:24:43 But do you keep it on people's box, because as we said, right now, the workflow for someone is to just curl a Java.
Jack Berg 00:24:50 Yeah, so what you would have to do is you'd have to… you know, curl for the jar file, the agent jar file, and then you'd have to set a particular environment variable to point to a file. And, you know, we have these template files, which are good starting points, and you'd have to know to look for one of those, to curl for that as well, and put that in a location, and set an environment variable to look for that. So, to your point, there's a lot of hoops you have to jump through, and you know.
If… the more sort of opinionated we get about how all this process works, the less hoops there are to jump through for users, and the smoother it gets.
atoulme 00:25:27 That's true. And that's the other part. So, okay, so that's the whole discussion. I'm not sure if you're up to speed on the Kubernetes discussion for Injector. Is that something you're looking into as well?
Jack Berg 00:25:36 I'm… like, I just know at a high level, eventually, we want the operator, which is like the Kubernetes story, to work with the injector as well, so we don't have two competing stories, two competing sources of truth for how this works, like, as much standardization as possible, and that's all I know for now.
atoulme 00:25:54 Okay, so, yeah, we do have competing stories, but it's more like there's a legacy story coming from the operator at this point, and then there's this new approach that the operator is taking. So I don't think… none of the operator maintainers are relishing, maintaining the current code, they're not having a good time. So, if I was to.
Jack Berg 00:26:13 So they're not competing long-term, they're competing temporarily until the injector gets its, you know, act together, and then the operator people want to depend on whatever the injector comes up with.
atoulme 00:26:24 Yeah, and then we're lucky that I'm an approver on the operator, Jakobaronov is a maintainer on the operator, so we have a good, overlap between injector and operator people. So it's not like we're two separate communities, we're not trying to… we don't have this audience relationship, we're the same people working on the same things.
So, the story of the operator is that when it started, it started in earnest to try to find a way to inject all the SDKs into pods, as you know. And there was not that many options back then, so what they did is they brought in Go a webhook that intercepts the creation of any pod.
And then based on the annotations on the pod, it will then perform a manipulation of the pod distribution.
To add an additional volume, It wasn't that. It's running an init container, which job it is to copy the SDK of a certain chosen, like, either Java, Python, or Node.js, or whatever, into the actual system.
And then they manipulate programmatically the environment variables of the pod container environment to make it so that it will load up the file, right?
sometimes that doesn't work at all, right? And sometimes we have very interesting surprises because Maybe that container is running more than one type of language. Maybe that container already has environment variables. Maybe it's trying to set environment variables in itself, like it wants to run profiling using some other tool, and now you're completing there are two options on both sides.
Also doesn't work well on Alpine, or it's just ever so slightly more difficult to work on Alpine versus VC, right? So… The operator approach would be to just do something really hamstrung, which is, hey, you want to inject some SDK in here? Let's inject all of them, and instead of just overriding the event variables of your container, we need to override your actual preload.so.
To tell it to load up all the variables according to what the injector sees on the disk.
That's something that Azure is using in the company's product, and they're trying to donate, right? So, pretty much the exact same permit if you see for the host would then become available at the operator level.
And, it becomes a very compelling story, because then we can delete a bunch of code for the operator, which is really difficult to maintain, and which has broken over and over again. Also makes.
Jack Berg 00:28:50 Well, it shifts it.
atoulme 00:28:52 It should be clear.
Jack Berg 00:28:54 Yeah.
Somebody still has to maintain it, but yeah, you know, now there's more people interested in maintaining it, because it's casting a wider net, and so it's more valuable, so…
atoulme 00:29:05 It is. It's also difficult to get a Java guy to… and I'm not looking… sorry, I'm… I just do a Java error, but you can take any SDK person and tell them, hey, how about you go run some Kubernetes cluster over there and reproduce the failure that we see when I do this?
And, Kubernetes? On my laptop? I barely run Docker, right? And I am, like, I'm really, really good at Go routines, and I understand how to do, you know, Python, escalations, or, like, whatever, but you're asking me to understand, like, the Kubernetes concepts, you already lost me.
This is just a… people just don't have the same expertise across the board. It's too much… too much to ask.
So instead, what we would be able to do then is to also isolate failures down to the level of the injector in a much simpler environment.
So, that will allow us to do more testing closer to the metal, and therefore, we can tell people if it works or not. So, we just added that, actually. This is the latest enhancement.
We're already testing for all three languages we support, using some automation, so now we can actually, on upgrade, we'll be notified if anything starts to break.
And then we'll, we'll also do that, we've done that for ARM and AMD.
So, now we're in a much better place, and I think we need to kind of continue to push the envelope in there, adding even more testing for this type of stuff, as a… as a safety net of sorts, that someone's not breaking something in the, in the SDK inadvertently.
You know, we've seen that before.
Jack Berg 00:30:40 How do you see the… how do you see that init container functionality of the operator changing? So right now, it's… there's an init container, it detects annotations on the pod that say, like, hey, the annotations are basically an instruction that the… whoever's you know, setting up that pod has given the operator to install, you know, the Java agent, the .NET agent, the Node agent, whatever it is. And so, you know, it can look at that annotation, download the right auto instrumentation package, and add it to the class path.
And you're saying, like, okay, that's insufficient because some containers run multiple languages. That's insufficient because there's, like, the Alpine versus libc conversation. And that all makes sense, but wouldn't the injector, in order to solve those problems, have to do things like wouldn't it have to download all of the packages, and would it have to download all packages and put them in the file system of the pods for every single pod that started?
atoulme 00:31:41 Yep, that's pretty much what would happen.
Jack Berg 00:31:43 And it would… and is there a way to… I mean, I assume there is, but, like, we have to be able to cache those… those resources that we would be adding to the pod's fi… to the container's file system, because we can't download those over a network every single time a pod starts. That's just…
atoulme 00:31:58 That's too much.
Jack Berg 00:31:59 time to pod, startup time.
atoulme 00:32:01 Yeah, yeah, yeah. So what we'll do is, first, if we were to be close to the existing implementation, we would have a Docker image that is just the injector in all the packages that are vetted for backcour use. So we crystallize version of the injector, known version of all the ATKs that are working together, that are actually tested for the operator that way.
And then, that's your Docker image. And then, when you do the CP, initially, the in-container copy, then you copy all the SDKs and the injector at the same time.
Of course, it's painful and, frankly, expensive to do that, so… We might get smarter about this, but…
Jack Berg 00:32:38 Okay.
But it is cached. It is cached, though, so… because there is a dedicated container that has all these info… these packages pre-downloaded, and then, you know, maybe… that seems like a good starting point, to be honest, is, like, install everything, copy everything, and then if there's user complaints, you can always add some sort of additional syntax or configuration options to be more selective about what is installed and how.
atoulme 00:33:04 Exactly. The other aspect of this is that in Kubernetes, there is a beta filter gate that is disabled by default to mount a Docker image as a volume, so that would remove the need to even have CP present on the box, on the Docker container.
So that would actually make it so lean that we would just ship a Docker image that would just contain the file that we need, and that becomes just a conduit to the packaging of what we have.
But I… I'm not holding my breath for this to go stable. It's been years. I'm actually, at this point, I found someone in Community SIG, I'm trying to ask them, like, what's… what's the way of that?
That's… yeah, there's maybe another thing we could do, we could… we could make it so that we can do a volume definition one time, so that's… that's the uber, like, really well thought through thing that I don't think I've put any… any work into.
Where you define the volume, in your Kubernetes cluster as a whole. And that volume is what you want.
Right, yeah.
Jack Berg 00:34:06 And that volume is mounted to all of your pods.
atoulme 00:34:09 Right. Because you don't need to do as much work in that case. But I'm sure there's a good reason we were doing CP before.
So… I don't know.
Jack Berg 00:34:20 Yeah.
atoulme 00:34:20 True.
Jack Berg 00:34:21 Yeah, yeah. Well, there's options there, so, you know, there's simple ways to, to get started, and then ways to get better over time, so…
atoulme 00:34:32 But, yeah, to also give you a little bit of insight, there's one recurring problem with the operator right now, is that it's fairly slow, in the sense that it's not being optimized at all to use Kubernetes caches for what is called informers.
So it's doing a lot of inefficient calls to, get the list of existing SDKs or other things, like, there's just, like, performance bugs in the code.
So we know for a fact that, for example, if you start to load up and you get 2,000 pods that are in the queue to be created at once, this stuff just blows. It doesn't work up, it takes over the API server, it's just doing kube control type calls all the time, and at some point, this thing gives up. So we know the operator is also, like.
not very efficient right now, and I think it's because, also, you copy bits around between boxes, like, between containers all the time. It's just stupid. So if we can find better ways to do this type of work, that would be really great. We need to, we have customers who are requesting that type of capability at this point.
Jack Berg 00:35:36 Makes sense.
atoulme 00:35:38 Yeah, go ahead.
Jack Berg 00:35:40 what's the config story like with the injector? Like, you know, we talked about things, or I was, you know, bringing up this idea of if you have packages for language… auto-instrumentation modules, that it can help standardize things like config.
you know, while we strive for consistency across languages, like, it's gonna be obvious… there's obviously gonna be cases where you want to, like, diverge and have, like, you know, some Python-specific option or Java-specific option.
Like, do I just need to re… go into the repository and dive into it to figure out how all this stuff works? Like, what the configuration story is?
atoulme 00:36:20 Right now, there's no config, so we just load up whatever's default. You can…
Jack Berg 00:36:26 No, wait, wait.
Okay, wait, so back up on that. You load whatever's default, so all you're going to do is set Java tool options to point to the Java agent, and then that process is going to have to start, and only… its only configuration option is whatever the system default environment variables are, therefore.
atoulme 00:36:44 Yes, correct. That's correct. And, and then… so there, there are a couple things.
the config file of the injector right now is just the locations of the things on the disk. It's like, here is where the Java jar is, right? Okay.
Eventually, I think we support a number of environment variables you can set in a config file as well. But what they translate to is hotel standard environment variables. So we just use it as a proxy to set those environment variables on the process that starts, and that's it.
I think we need to… eventually, we need to be able to just say, this Java… any Java process going to generate from the config file for Java SDK, which is over there. And we, you know, tell us where it's at. And we don't want to get involved into the nitty-gritty of every single toggle of each environment variable or whatnot, because I think that would be madness.
So you could do it today, right? Because I think there's an environment variable to tell you where the config file is. We should support that and make it easy. The injector, as of now, the release of the injector is currently taking a big shortcut, because historically, this is what we did.
Where it's bundling the injector in whatever versions of the Java, Node.js, and Python SDKs are present.
So, you… if you install your RPM for the injector today, you get all those SDKs installed in some well-known places as well.
Because we need something to work, right? Yeah.
Jack Berg 00:38:11 That's fine, that makes sense. Like, later, break them into separate packages, but, like, yeah, that's just a distraction for the time being.
atoulme 00:38:19 So eventually, when we break it down into separate packages, I could see how the Java… the Java RTM, for example, would come with, here's the jar, here's a set of config files by default, and here is a well-known default one that you should load by default, that is the one to… No, right? And the injector should just hook up to that and say, by default, we're going to use this. If you don't like this.
go to the folder with all the config options, like, all the config files that the JavaS SIG decided to ship with, and pick one you like better, and change the config file to, right? We can even leave a bunch of commented-out entries and say, here's the default one, but change, right?
The dev will get you where you need to be.
I think, in general, like, the injector needs to have a least opinion possible so that it can inject and be of use. What I'm looking to do, for example, right now, is, like, how do I add Ruby to the tents? How do I add, like, 5 more languages, so that we can also see the commonality between all those SDKs and have less and less Otherwise, it's very easy for us to say, oh, we really like Python, we really want to spend, like, more time into Python. Before you know it, we started to say, we should shift configuration for Python. Oh, we should have some opinions about what You know, and then before… we'll get ourselves in trouble. So, I think it needs to be wider as a mechanism, and it needs to be very dumb, right? Just…
Jack Berg 00:39:39 The defaults need to be dumb, but then you need the ability to do non-dumb things if you're an operator who cares about that. But out of the box, it should be as simple as possible so that it works across all the languages. And then, you know, you can enhance it from there.
Yeah, like, I can imagine something like… I can imagine something like… so you have an injector config file, right?
And, like, one of the properties in there could be, you know, there could be, variables that are the paths to, the environment variables for each of the languages. So it's, like, Java environment variables, Python environment variables, Node environment variables.
And, like, maybe you ship a default file for environment variables, and all of those language-specific options point to the default file location. And so, you know, if you want to go modify everything across the board for all languages, go modify that default file. Or, you can update the path for Java to a different, like, file.
customize it to suit, and then, you know, you'll get something different for Java than Python and .NET.
Oops.
atoulme 00:40:45 That works. That's… I wouldn't say that's already possible, but you could just, right now, use a config… the declarative config file seems like the long-hanging fruit we would want to latch on as… to re… to avoid creating another config file with environment variables. I'm just afraid of that, if that makes sense.
Jack Berg 00:41:05 Yeah, yeah, yeah, and I'm trying to strike the balance, too, because I'm obviously biased towards declarative config, but, you know, there's… it's like, that's what we should get towards, but we shouldn't let this… that stop us from doing something useful right now, with Injector. So it's like, you know, that… that's the… that's the target, but for now, some languages don't have good support for declarative config, and so it's almost like… what do you do? What do you do? You use environment variables, some really simple representation of environment variables, and then you, you have.
atoulme 00:41:42 I don't know, a plan to migrate that to declarative config once you've reached some sort of critical mass.
Yeah, I mean, the environment variables will always be there anyway, so… and frankly, we could even play a game where the environment variables file for Java is just the environment variable that sets the path to the config file, and then you go there.
Jack Berg 00:42:03 Exactly.
atoulme 00:42:03 That's… it's locally, but it really gets you where you need to be, and then if people have strong opinions about, I really like environment variables better, go at it. No one can stop you, right? So… Yeah, yeah, so in terms of roadmap, right, so for myself, right, I'm eyeing adding Ruby just because I can, and because I want to bring even more of a bigger tent of people who can be impacted by the injector, because I know it's hard to get those esoteric languages instrumented with OpenSimacy today. So, how do we make their life a bit better? I need to continue to build community around this. We want more usage, more people trying this out, we want to get some bug reports from people, like, I tried this, I hate everything you did. What were you thinking? That's great feedback, let's go, right?
And that would be, by the end of the year, that would be sufficient for us to go. In parallel, I know Michele and Dagio folks are adding the operator use case. They're like, this is… this is where the gold is.
This is where we think we're going to have so much more efficiency, and we want to align this to our upstream product, to our downstream product that is from that zero, so that we get more and more people on board of this, we get more usage, we get more maturation.
If we do all this, we're good, and that gets us to, you know, maybe end of Q1. End of Q1, maybe we can start to have a discussion with the SIGs about, hey, maybe we could separate those RPMs into separate places, how do we talk about that? That might be a good discussion for QCon U, or a discussion at Hotel Unplugged that, Teddyong wants to have.
Around this type of scale… of requirements.
And I want this to be a software thing. It needs to be, like, obvious to… right now, like, if you talk to a Python developer or a JavaSig maintainer, they go, they don't know, why do I care about this? Why do you bring this up?
So we need to kind of take the time to communicate, to socialize this as a well-understood, great way to get OpenTemmetry stable as a product.
And so, if I can respond to the Hughton Parker, you know, speed of, I want OpenTimetry to be stable and mature.
That makes everything kind of jive together.
And I… I don't want this to be a forceful thing where I just shove down the throat of some poor Node.js maintainers, hey, you're gonna maintain an RPM now, right? That's… that's not fun.
So…
Jack Berg 00:44:22 Yeah, it's like… it's like OpenTelemetry is a toolkit, and there's a lot of bespoke tools you can pick up, and you can combine them, and you can get something working.
But the injector is, like, the paved path for that thing. And so, like, as a Java maintainer, of course I'm going to continue to maintain all of the tools in the toolkit. You can pick those up, and if you're an advanced user, you can stitch them together to get what you want. But, like.
as a Java maintainer, I also want an easy button, like a one-click solution that allows you to, you know, go down… get a good experience out of the box that is opinionated. So we can have both worlds.
atoulme 00:44:57 Cool. Okay.
Jack Berg 00:44:58 And I hope that's a message that resonates with other maintainers as well. Like, but you're right, it does have to be a social thing.
atoulme 00:45:05 we need to take a walk and sticker and go to every other SIG and start to make this type of announcements and discuss with them, and I think it's… it's just, I would assume that by default, communication is broken, and no one has heard about it, right? So we just made a big… we made, The talk that we made at Holiday KubeCon NA 2025, on purpose, the person who asked for me to make a demo was Tias and Plum, because he's a JavaSync maintainer.
And that lends a lot more credibility on the objective of, hey, here is what we're doing.
And actually, Jason started the demo saying, I'm a Java guy, I have no idea about all that… what did I just inject a thing? Antoine told me to just run those commands and it will work. Let's try this out, right?
And the room was like, yeah, let's actually see this, right? I mean, we wanted to see a real demo of, like, does this actually work? And he made it work in front of them, and he was carrying a lot of weight in terms of credibility. What I wanted was for open semester to be like, oh.
I should be on that train. Why is there no Python app in this demo, right? Why is there no learning app in that demo? Like, how do I get on there? Like, that sounds cool.
That would help me with that. If you had this month about how my installation step didn't work the right way, because I'm on out of time that time, and things don't work the way, this is so painful, can we please make it away? Go away.
So… We're starting the evangelization process. To me, it's so important to do it this way, and, you know, having you in our corner as a TC rep is going to help us as well, so we can strike the right balance.
But to me, this is, this is fine. This is… this is also the speed of open source, right? We go… we go really wide, very shallow, and then we go from there, and we start to depend a little bit, I think.
And I owe everybody more communication on that. We can write blog posts about this day in, day out. We can explain things. This update thing also needs to be well explained so that we don't start to have some sort of miscommunication that would confuse people.
And… and that participates in the grant plan.
Jack Berg 00:47:13 I mean, one way to… Yeah, so I agree with all that.
I'm just thinking about, like, How you connect the dots to… for… you know, we have this section of the docs, OpenTelemetry I.O. Java, and, you know, it tells you one way to install the Java agent. And it says, like, hey, download it from here, and then, you know, set up your Java options to point to it. And, you know, it would go a long way to… To maybe still maintain that, because that's, like, kind of the low-level way to do it, but to also prominently talk about the injector and say, like, hey, look, this is the other prominent path to install the Java agent. And, you know, if every sort of language ecosystems page prominently emphasized the injector as the paved path for how to use their toolkit, like, that starts to create the momentum.
atoulme 00:48:10 That's a super… yes, very valid. And let me have an issue about that right this moment in GitHub before it fails me.
This way, we don't have to rediscover this in 3 months.
Because that's a very good point. And it's also very easy to have to do, like, hey, alpha, trying it over here, here is a new way to do things, would you like to try this?
Jack Berg 00:48:33 Right, and once it's not alpha, maybe you can… you can promote it, and it can be the first thing on the page instead of a footnote on the page.
atoulme 00:48:41 Flip the alpha peak node out, and then start to move it up, and we can… Frankly, yeah, that's a preferred approach.
I have to say we opened an box, like, what's gonna happen is that you do this, and then people go, oh, cool, how about Ansible?
Like, just to prepare yourself, this is happening.
Jack Berg 00:49:01 Ansible to do the same thing?
Like, you know, because we, OpenTelemetry, can be opinionated, and we can, like, come together as a community and say, like, look, our opinionated, easy-button approach for OpenTelemetry is the injector. And we're all going to rally behind that, and we understand there's other ways to achieve automation like this.
And you can talk about those in your other places, but the automation we're going to focus on is the injector, because we need to simplify the story, and we need to have, like, a good, simple story for everybody. That's good for the community.
atoulme 00:49:36 Huh.
Jack Berg 00:49:37 What's going on.
We're just two guys talking, but, like, you know, that's just… that's how we can approach that conversation of, like, you know, why Ansible should not be considered the same. It's because, no, the injector is our preferred opinionated solution for how to install OpenTelemetry easily.
atoulme 00:49:56 That makes sense. I'm half… A main challenge, the reason is because, from a vendor perspective, we do support NCBull Chef, puppets, salts, what have you, all those esoteric ways.
And what they do under the… what we really do under the Ansible install is we actually install the RPM.
It's just that the moment you add convenience, people are like, oh, more sugar, right? I'm just saying, right?
Jack Berg 00:50:24 Yeah, yeah, yeah, yeah.
atoulme 00:50:24 That would be a exquisite feedback for me. It's like, oh, I like it so much that now I want more. It's like, oh, great, oh, you want even more? Like, you want, you know, the easy… the next step will be, I want this bundled in my EC2 images when I install them.
Which is possible in easy-to-image builder, which becomes, like, a play, like, it will… I'm just trying to tell you that the water rises as you make things more easy, people start to eye things like, oh, but this is so easy, why is this coming easier and easier?
Jack Berg 00:50:56 Yeah.
atoulme 00:50:57 Welcome to Utah.
So…
Jack Berg 00:51:01 Well, one step at a time, I guess, and that's a good problem, as you mentioned.
atoulme 00:51:06 That's a very good points you have. All right, so I just opened, The CC, I'll put it in the chat for people who watch the recording.
It's very… it's a very generic issue just to say, add to the Mario to all etiquette supported, a set of installation steps, make it experimental.
Let's get some feedback. If people don't like it, I won't hear. If people use it.
We'd need to start to get some sense of how much usage we see.
So, too bad, we don't have a… we don't have a Debian and RPM site download, because we could then kind of try to see if we're seeing any uptake from the community, but… Maybe that's later.
Anyhow.
Jack Berg 00:51:49 Well, I know it's just you and me. We've spent almost the whole time talking, so I appreciate you taking the time to get me up to speed on this.
So, what you can kind of expect out of me is I'm gonna, you know, start following this repository more, maybe start to tackle a few issues here. You know, in particular, I think I intersect with the Java and the config stuff.
So maybe try to flush out the story there. You know.
OpenTelemetry as a project shuts down for the last two weeks of the year, so that's kind of lame. And also, Grafana, the company I work for, has a hackathon at the first week of December, so it's not like I have a ton of time to go and, you know, to talk with you all and get up to speed, but you know, the last two weeks of the year can be actually good focus time if we can kind of, you know, agree on what we should focus on. Like, if we don't need to collaborate, we can kind of go off and, you know, build stuff by ourselves. And so, I guess.
to flesh out some of these conversations and see if there's anything material that needs to be done, and then I can go focus on them as an individual, so that we can start in 2026 strong, so…
atoulme 00:53:07 That makes sense. I think, I think actually the current set of issues are kind of unique. There's some poignant issues that we need to kind of prioritize, so we have a problem with Renovate. I think I'm too dumb to figure out. I'm sure you know, how to do that. It's, number 73.
Which is that I'm not able, for some reason, to get, Renovate to pick up that we want to update the versions of the ADKs that we use. So we've been on… we're on rather old versions of the ADKs at this point. We need to either We might want to update them by hand, and also to please renovate once and for all, so we're good to go.
everything else, like, there's some to-dos that need fixing, there's, I mentioned Ruby, to me, is just fun, so I would like to do that. The interesting part for Ruby and other languages like this is that you don't know how to test for them. It's actually tough.
They don't have enough testing on their own. So, asking the Ruby guys, like, oh, just run Rails. I'm like, really? I'm gonna run Rails to test if Ruby Automation work well?
That's really expensive. How do I run Rails in a test environment Never.
Jack Berg 00:54:19 I mean, that's what we have to do for all of these, right? We have to do, sort of, like, black box testing.
atoulme 00:54:25 you know, I can pick up Tomcat, and it works, and I know how Tomcat works, but when they say, just pick up Rails and it will work, I'm like, no, I used to be a Rails development.
Jack Berg 00:54:37 So I'm not in the Rails community, but you're saying, like, picking up rails is an order of magnitude more kind of complex than just picking up Tomcat?
atoulme 00:54:46 Yeah, because, I mean, the story, the way it goes is that we've been trying to get Ruby support in the operator before, and they brought up a whole thing of things, a whole setup, the framework. You said Ruby options, Ruby of ETS, exactly like Java two options.
So it actually would be very easy to set up, and this is the cringey part for me, is that the actual mechanism of doing this injection, super simple, no problem, right? Now, how do you test this? Well, you're going to take a application, maybe Ruby, you're going to do the injection, and then you're going to see if you get metrics and traces out of it, right?
Yeah. So I did that with Natra, which is a simple, you know, back from my Ruby days, it's like to do, pretty much the equivalent of a… a servlet, right? And then the machine can take guess and responds Hello World or something.
And I would expect to get some traces, doesn't work. And what doesn't work? Why does… what's going on? And then it starts with Ruby guys, like, no, we don't… it don't really work with those type of applications. You need to run, like, the whole Rails thing. When you do a Rails, by default.
you would want to do, like, Rails init to create a scaffolding of some Rails thing, and then you can maybe create some pages, or… I don't know, like, that was too much work for me. So, we have some work that has been kind of slowing decaying and going to waste, that we need to pick up. We redo the example, make sure the testing works.
Having… having now Java, Node.js, and Python tested properly helps add one more, right? And this is kind of the challenge, in a sense, right? So, we inherit the challenge of the immaturity of any SIG that we depend on.
So… I just want… I'm gonna try to work on this, but this is something I do in my free time, so I'm just for fun.
Jack Berg 00:56:34 Yeah, yeah, yeah. And the issue is, like, you know, once you have enough momentum, you'll create an incentive for the Ruby developers, in this case, to come over and maintain their own examples, but you haven't reached critical mass yet, right?
atoulme 00:56:46 Until…
Jack Berg 00:56:47 You have to help achieve critical mass.
atoulme 00:56:50 Exactly, you got it, right? And so that's painful all over. And I think after Ruby, I would be hard-pressed to find… I need to look at the downloads and the popularity of SDKs, but we need to kind of go for the top ones, and if you have… well, we have .NET as well that is well supported.
Oh, shoot, no, we don't have Python, I'm sorry. We have Java, Node.js, and .NET, I'm sorry, I'm wishful. And then I can add Ruby, we need to add Python, and then we're gonna be, like, 80% of everything that is, running out there will be under our purview, and we'll be good to go.
Jack Berg 00:57:27 Okay.
atoulme 00:57:28 Nothing's been saved, yeah.
Jack Berg 00:57:29 So, like… What's… What are the risks right now? So, you mentioned that you had things that you wanted to achieve by the end of Q1, roughly.
What… what are the big problems that face the project right now?
atoulme 00:57:46 We don't have enough people interested in the project, because it's kind of the duct tape of OpenSemitoring, if that makes sense.
Like, there's glory in working in Java, in building another Kafka integration. Look at the finesse, the promotion path for you. Why, as a developer, you might care? There's no glory in fixing list symbolic links in an RPM package.
It's just absolutely awful all over Sydney.
Jack Berg 00:58:13 That's, like, those are, like, project management type issues. Not, not project management, but, like.
Are there… are there technical issues that still need to be, you know, handled about the project, or are things in a pretty good spot?
atoulme 00:58:27 I would say that, Michaela already did a good job of pointing out that Python SDK is a bit of a pain, and it's immature in places, so we… we have… we're going to have some trouble there, but that's not our problem, that's a Python.
Jack Berg 00:58:40 Right.
atoulme 00:58:41 for the code in the project itself, it's working just fine. It's really great. It's not in any way, shape, or form giving us trouble, and they did all the hard work, frankly.
So, we're good there. No, I think, there is a bit of discussion Michael's been having. He used to work as canonical, he knows well how to do the Debian packages, dependencies, and all that.
So we need to communicate on that and make it more… You know, something that people would want.
And, what else?
We just need to communicate well how we're going to play with Audi in other projects.
Jack Berg 00:59:21 Well, I think I can be useful by getting my hands dirty with this thing, and actually installing it, and using it, and, you know, providing some feedback, and and seeing where that takes us, so…
atoulme 00:59:32 Awesome. Take a look at, what, take a look at our, our, at our demo for the, for KimCon, how it went. Interesting feedback. Specifically, like, there's some Java service, so Node.js service, so you can take a… you can see a bit how things went. And, We might want to have more of this type of demo or examples shipped out, so we have an opportunity right now to integrate with the demo.
For what it's worth.
Jack Berg 00:59:58 Yeah, yeah.
atoulme 00:59:59 So, no, there isn't, like, a huge roadblock, or a technical thing, or we don't know if we're going to be able to make it. The project is, from my perspective, technically done. It's a project, product management, product management, how do you ship this, how do you give stability, how do you give people incentive to use it that really is meaningful to me.
And I'd love it if we had… multiple vendors starting to rely on this. Grafana, being a vendor relying on this would be, helpful. We ourselves, we will be moving to that because we currently have some legacy stuff in C that we're going to deprecate and move over to this instead, but that's going to take some time, right? So… We… we're… we need to see some real-world usage, and gather more feedback about how things are going.
Jack Berg 01:00:43 Okay.
I'll read the blog posts, watch the videos, the recordings, and you know, I'll check in with you after I kind of get up to speed on all this stuff, so thanks for your time.
atoulme 01:00:54 Thank you, Jeff. Everyone, take care.
Jack Berg 01:00:56 You too, bye.
