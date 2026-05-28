SIG: Packaging SIG
Date: 2026-05-27
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/MC-w6V494OZdEr_qLsDPRyFoxNVNiesuVg6t_fFdja5RG1-TOAGd0MYI65Kv4uRR.1SBzzCeXnrYVfNSA
============================================================

## Zoom Recording Transcript

Denys Sedchenko 00:00:35 Hello, how are you?
Michele Mancioppi 00:00:37 Hi, how you doing?
Denys Sedchenko 00:00:39 Finding you.
Michele Mancioppi 00:00:41 I'm getting pretty confused about some stuff, like… how the hell do we end up integrating OPA and OPAMP in our designs, but for the rest.
We're doing some progress.
Denys Sedchenko 00:00:59 Hmm.
On my side, I was quite busy.
on my… Main work, but… I have some news regarding research.
Michele Mancioppi 00:01:13 Interesting.
Denys Sedchenko 00:01:15 Let's see… Of course.
Michele Mancioppi 00:01:16 Let's see if Anton can join us, just a second.
They came down to him.
Here he is, the man of the hour.
atoulme 00:01:56 Hey, folks.
Denys Sedchenko 00:01:58 Cody.
Michele Mancioppi 00:01:59 Hi, Hart.
atoulme 00:02:00 Struggling to find the Zoom link today.
Okay.
Michele Mancioppi 00:02:09 Before we start, we start properly, there was, other people signing up for the, for the SIG, and, they got… Here's some, somebody else is coming in, good. Maybe, Antoine, have you, considered reaching out to the… to the other people that, applied for Staff Wanted?
And see if they can join us, or if not, why not?
atoulme 00:02:31 Yeah, I think that's a fair ask. I actually was about to push to the channel, the link to the doc, and say, hey, please join.
Or me tea, east, stomach.
Please join… Seasons a link at the top.
Little duck here.
So do an ad hat here, let's just do it.
Michele Mancioppi 00:03:01 Sinai is… are you a Douglas from, Curologix, or…
Sina 00:03:07 So, hey, no, I'm, hi. Yes, Sina, I… sorry if I didn't say hi, my mic was a little bit acting up. I'm, Sina from Canonical, SimSense UA.
Michele Mancioppi 00:03:18 Oh, no, private.
Hi there.
Sina 00:03:20 Hello.
atoulme 00:03:21 Okay. So.
Michele Mancioppi 00:03:23 Antoine, we're missing, we're missing Douglas from CoreLogix, and, Damien from Elastic, who signed up for… From India.
atoulme 00:03:32 I mean, I know he's on parental leave.
Michele Mancioppi 00:03:34 Oh, okay.
atoulme 00:03:35 And he's mostly interested in the Homebrew tab, so he's back in August timeframe, and he would work on homebrew mostly, so it's kind of a… phase, like, it's… to me, it's like a side project, it's kind of nice to have, but we don't need him for… for Douglas, I think, yeah.
Michele Mancioppi 00:03:54 I must have the results, right?
atoulme 00:03:56 Hi, Dad.
Ted Young 00:04:01 How's it going, y'all?
Michele Mancioppi 00:04:05 I've been delayed.
atoulme 00:04:06 That's on the… on the spread, on the… on the channel.
Okay, so, looks like, the PR that you opened, Mickey is getting, like, some attention, right?
Michele Mancioppi 00:04:19 Oh yes, it's a significant amount of attention. Do we want to set up an agenda? Because I think there are multiple topics.
atoulme 00:04:29 Alright, so… sure. Let's go to the dock. You got the thing…
Michele Mancioppi 00:04:34 So, Dennis had an update on, on the research.
For hosting?
I assume.
I have an update on, on the Meta Package PR.
We have, Sina from Canonical, who, they also have been interested, interested in, packaging the injector.
I am… I used to work with them in the observability team, so there are common interests.
The, I think that, we should start with the packaging and so with the hosting.
Which is also where, Canonical probably has a skin in the game because of Launchpad.
atoulme 00:05:25 Okay.
Michele Mancioppi 00:05:26 Dennis, do you want to start?
Denys Sedchenko 00:05:29 Yeah, basically, on last meeting, we agreed to basically, first of all, contact Kubernetes team regarding the feedback.
of their setup, and also contact Alex Botem.
who participates in Collector SIG.
So, first of all, I contacted Alex Bogdan regarding how they… Sign their packages.
So he pinpointed me to one of the, like, one of the tools they're actually using.
So, they're using a tool called Cosign.
I checked a bit what it is on the internet, basically cassain.
Allows you to submit certain, like, blobs, some certain artifacts, and it does a signing for it.
In order to sign it, it needs a certificate of authority.
It should be an external certificate on authority, And, the… like, the certification authority that it's, it recommends, it's FULCO, F-U-L-C-I-O.
It's, like, designed to work in tandem, and you need to somehow to authenticate to Full CO with OpenID Connect, so it will authenticate the request, and it will stamp the artifact.
Alex doesn't know how, like, how they use Fullsia, whether it's cloud or self-hosted. I need to dig deeper, ask a question about, like, about it in, collectors seek.
So, and regarding Kubernetes… I was looking to what Sig should I address this question. I initially went to the InfraSig, because it's what's basically… the InfraSig manages the pkg.io subdomains. They forwarded me to the release sig, which wasn't mentioned on the Kubernetes documentation website.
And, at the moment, I have two… Proposals that they implemented that actually They use to release that described the release process, how it works.
I didn't check the documentation yet, because I spoke with them just yesterday.
It's evening!
And also, I asked the question in a SIG release about, like, their feedback, whether they're happy or not with the current workflow, and I didn't get any feedback yet from them.
My findings on the Kubernetes Are attached as a comment to the issue.
And regarding what collector actually use, I will add details when I get more info.
Michele Mancioppi 00:08:22 What is your first take about cosign and Fulzio?
Denys Sedchenko 00:08:28 So… I don't know if it will be usable… if it will take OBS, because OBS also handles signatures.
And currently, I'm not able to basically take a look how the signatures are working, because I needed access to OBS, and I had problems actually signing into OBS in order to create any repo to test.
this.
So, like, cosign is useful when you basically have your own CI, and you build your own packages, and you stamp them manually.
Like, in that case, cosine definitely will be necessary Because we don't want to have GPG case expired or lost, we don't want to leak our GitHub secrets.
And delegating it to external entity is good. The question is whether there is, like, a cloud version of FullSeo, because, like, as you mentioned, we don't want to self-host stuff.
Michele Mancioppi 00:09:28 If we can avoid it, we shouldn't.
Okay, cool.
Denys Sedchenko 00:09:32 Did you check LECOBS? Did you have any time?
Michele Mancioppi 00:09:36 I've been, The amount of time it took me to further all the comments on the Meta Package PR was significant.
Denys Sedchenko 00:09:44 Yeah, I sold.
Michele Mancioppi 00:09:45 to have, I'm not complaining, it's great.
Denys Sedchenko 00:09:49 Maybe Sina knows anything about, open build series from Prince USA.
It's, like, technically adjacent projects.
Sina 00:10:03 Yeah, so I'm not too familiar at this point.
So…
Michele Mancioppi 00:10:08 Maybe I can give you, Sina, a, a status of where we are. So, when I spoke, with, John Seeker, who's the director of, VP of Engineering at Canonical, and Sima Ronson, who's the team lead for the observability team at Canonical, that was some time ago, and I was saying, hey, we should work together on packaging the injector and auto-instrumentations.
In the meanwhile, we have succeeded in starting this SIC, so it's an official OpenTelementary project.
And, it is pretty important for the, for the open territory story post-graduation.
the, when I spoke, way back with the canonical people, RPM was not in the picture. It was like, if there would… there hadn't been an official Potential project, and having somebody in Ubuntu, that is something where I would have applied myself, but now, since it's an official Potential project, we need to cover both dev and RPM.
the… we have gotten a, a lot of good feedback from, Christian Falsa, from, no, Earhart.
From, from, Canonical to, to which we're very, very thankful, because we did our review.
The biggest problem that we're having at the moment is, the building and hosting of the packages themselves.
the, canonical would be a good place to do PPAs.
But, Launchpad specifically, do PBAs. But, to the best of my understanding, it does not support RPM.
Is that correct?
Sina 00:11:51 Yeah, I'll double-check with you on that, but I kind of got the update when you sent an email yesterday, and I think we… I was under the same impression as you, that I think the PPAs will help with the packages, but not with RPM.
Unless I'm missing something and I have to get back… do my homework to live.
Michele Mancioppi 00:12:08 Yeah, that, that would be a… so since, given the fact that nothing… it's not really the building process, the problem, it's designing.
More than anything else, and to some… Let's expand the hosting.
If something like Launchpad would turn out to be able to serve for us for Deb and RPM, that would be amazing.
Sina 00:12:34 Got it.
Michele Mancioppi 00:12:38 The, right now is where, the, Of course, more eyes from Canonical on the packaging, especially the dev aspects. That would be very welcome.
And Christian did a pretty good job.
Having another set of eyes going over and asking questions, like, hey, are you sure that you want something to work with this? That would be very, very useful.
Effectively, the goal that we have is to… Provide a, a… Set of packages.
One for the injector itself.
one per language, so Node.js, Java, Python, etc.
Where the, We let the language system packages, they come in with the SDK, the auto instrumentations, and they're activating the process by the interactor.
And then we put on top of it a metapackage called OpenTelemetry that effectively has dependencies on all of these, and you install OpenTelemetry, it pulls everything else.
That is the kind of experience that you are envisioning.
Sina 00:13:51 Right.
Michele Mancioppi 00:13:52 BPR to look at, to see what, what our current, thoughts are.
I'm going to put it in the chat.
It's this long.
Sina 00:14:22 Okay, perfect.
Michele Mancioppi 00:14:26 There are still some comments to address, for example, the one by Christian about not needing… they are not technically virtual packages anymore.
Needs to do some minor cleanup, but the, the overall concept seems healthy.
Of course, the more eyes, the expression more eyes that are, that are experienced in terms of, Debian container ship, the more bugs we find.
Sina 00:14:55 Crits.
Michele Mancioppi 00:15:05 Do you have any questions?
Sina 00:15:08 Yes, I think this was very informative, so thanks for that. I was speaking to Simen around some a couple of days ago.
And… I think many of the questions that we had, you answered here, but… We were wondering, what was mostly expected from us, whether we could help with the packaging itself, or… The concern is mostly the hosting, especially since now you have not just that, but you have RPM, and it looks like… it looks like that, the packaging is less of a concern for you at the moment, and where you need a little bit of help is whether the Launchpad can.
Michele Mancioppi 00:15:52 defining the packages and building the packages, I think are in good shape.
I mean, we put in a large amount of time in designing the thing by now.
Sina 00:16:02 Of course.
Michele Mancioppi 00:16:03 more eyes to make sure that we're not missing something, something that's gonna bite us down the road. That's super welcome.
The signing, and the hosting are something where we need help.
And, we are not afraid of building the packages ourselves.
So that we could do in the GitHub CI, that's not a problem, but the signing and the… the signing is the biggest pain in the… As we have, and to some extent, the hosting afterwards. We could also use help in a topic that is not in the first phase. So the first phase, we want to put out a version of the packages people can start experiencing with.
I think, something where Canonical's expertise is really gonna help a lot.
Is, discussing the ins and outs of… ins and outs of, versioning schemes.
the, when, when you define packages for Linux distributions, you usually have tracks, although I'm not sure it's the right term, so each major release of Ubuntu, every LTS, every release has its own track, and you're supposed to get updated.
different tracks, or at least different versions of Ubuntu, you start having different tracks, like nightly, snapshot, security updates, stuff like that.
That is a part of the story we have no thoughts about yet.
the, we need to find a way to effectively square the circle with, the versioning of OpenTelemetry packages, the kind of things that we are going to pack into the system packages, like Instrumentation 1, 2, 3, 4.
And, where we push them in terms of tracks.
We do not foresee to have, hard dependencies on, specific Ubuntu LTS releases. Nothing that we're doing, for example, depends directly on a particular version of libc, or has external dependencies.
So, it… chances are that a, So the goal is to have a Fatria repository for different tracks that would work with any… supported.
version of Ubuntu, for example.
Sina 00:18:18 Okay, great.
Michele Mancioppi 00:18:22 But, of course, the more help we get in defining that, the better it is, because There are 50 million things to think about.
Sina 00:18:30 Yes, Anand, that was kind of part of something else I wanted to ask, because I… very casually, based on the limited understanding that I had a few days ago, brought it up to someone who had a little bit more knowledge about how the ins and outs outside the archives and launchpad And they were wondering if.
you… if this versioning scheme that you wanted to use had to have a direct relationship with the Ubuntu release cycle.
Right? But, okay, great. If that's… I think that simplifies things a lot.
And so…
Michele Mancioppi 00:19:01 The target idea would… would be not… not to have that.
Of course, we would positively love it if these packages landed in universe, or main. I mean, that would be amazing, right?
But, it's not something that, I don't think we're gonna have any hard dependence on a specific version of Ubuntu.
Sina 00:19:22 Okay, great.
And, I think we don't need to discuss too much this question. I think the ship must have sailed past this point, but… is there any way what you're trying to achieve can be achieved using snaps?
Rather than depth, or PR.
Michele Mancioppi 00:19:40 Nope.
It's, I mean, it would need to be classic snaps with effectively no security whatsoever.
Makes no sense.
It could be, for example, with an extension mechanism on snaps.
a completely different packaging, we'll be able to bring these auto-instrumentations to Ubuntu Core, but that's not in the scope for this project. That's something that, given the fact that To be perfectly honest about it, nobody has ever asked for snaps.
in OpenTelemetry, that's not something that we would do in the foreseeable future in the SIG. Same, we wouldn't do Flatpack, we wouldn't do other stuff, and we want to keep you at the level of system packages, because they are reasonably universal, and they're going to work both on the main goal, that is host-based.
Linux systems, as well as in containers.
Because, for example, the kind of packages that we're thinking of, they would, including the injector, would work equally well.
on an Ubuntu container image.
Sina 00:20:42 Hmm.
Right.
Right, and more importantly, like, that's… probably that's, like, makes it clear SNAP probably won't work, because you don't even get SystemD in most of the containers.
Michele Mancioppi 00:20:55 We would need to go and define a new type of interface and snaps, and then have the usual… I don't know if there's still the handshake mechanism, I was never a super expert in snaps, but… it would be a significant amount of work, because ultimately what you need to do is to have a snap.
The one with injector and instrumentation is be able to modify the content of another snap.
Sina 00:21:18 That's…
Michele Mancioppi 00:21:20 That's an adventure.
Sina 00:21:22 Hmm, right.
Okay, great.
Michele Mancioppi 00:21:25 Probably doable, not in scope for this project.
Sina 00:21:28 I understand.
Okay.
Alright, then, from my side, I guess I'll take some of the things that we discussed, and I'll take it back.
To some people who are more familiar with the archives and the team, see what they think.
Michele Mancioppi 00:21:45 We can expect to see you again next week.
Sina 00:21:48 We'll try. I think we have another person who's going to try to be involved in this work.
So, myself or him.
between the two of us, we'll try to be more involved, I think.
Michele Mancioppi 00:22:00 Who's the other person, in case I know them already?
Sina 00:22:03 No, they're, you probably don't know them, they joined recently to the observability team, but, we'll be… I'm trying to help out there.
Michele Mancioppi 00:22:13 Well… Thanks for the help, we appreciate that.
Sina 00:22:17 Yeah, my pleasure. We're very interested, just need to understand from the team what exactly we can offer in terms of help, and then we'll see.
More specifically, what we can help exactly with.
Michele Mancioppi 00:22:32 That's cool.
I guess we continue with a status of the massive PR.
atoulme 00:22:43 Yep.
Michele Mancioppi 00:22:44 The one for the meta packages?
I think we are in a, good place. I still have some work to do. I think the biggest and most, The most controversial point is the one that Thomas brought up about whether we want to have a different configuration file per language by default or not.
There are… It interseides in complex ways with support for OPAMP, So now OpenAmp is, the… it's a thing in OpenTelemetry where, effectively, you can deliver configurations over a remote RPC server.
So, imagine that in HTC, you would have basic configurations, like go and get stuff from that remote endpoint, and then it unloads the rest afterwards. And it's a… it's a way for adopters of OpenTelemphony to sidestep having to manage via system packages or GitOps the delivery of configurations.
atoulme 00:23:44 Yeah, it's fleet management at scale.
Which is kinda neat. And so you're saying we could have multiple files if we'd have one file?
And opam could probably play better with one file instead of multiple, maybe?
Michele Mancioppi 00:23:59 Yeah.
I'd be, I'm terrible with names.
Tom or something, right? James. James brought, brought, in, in the, in the, In the thread.
the fact that, in reality, in the schema for the declarative configuration, there are provisions to have, overrides the level of single languages, which is something that I did not know about.
It's experimental.
atoulme 00:24:38 Oh, okay, okay, that's fine.
So you could have, like, a base file, and you could have multiple files, and it would compound on top of it, is that what you're saying?
Michele Mancioppi 00:24:49 I… No, that's not what I'm saying, no. The, so here, in experimental instrumentation, and I have no idea of Which language has… I just saw this earlier today.
Here, there are… overrides for specific instru- for specific languages? Yep.
the, despite the… so, this… If this was a thing we could rely on, my biggest concern that originally led me to propose one file per language Would be satisfied, so the possibility to define, effectively, allow and deny lists of instrumentations per language.
My intuition says that if we go with the one single file.
We will still have to allow people to provide language-specific files as an opt-in, instead of being the standard mechanism, because people are just like that.
There will always be an excellent idea to exclude op-amp support for Python, because reasons, yeah?
Oops, cool.
But, but, if we could, if we could go with, one single file, Bye.
Default, it does make the first version support for OPAMP easy.
Not easy, but not easier, but not easy, but easier, I think.
And then we need to revisit entirely the way that we think system packages are contributing configuration.
atoulme 00:26:31 Understood.
Michele Mancioppi 00:26:31 The injector, we did the comfy approach because we thought it would be best to have each single system package provide configurations for itself.
to the injector.
If we end up with one single file, I do not know who's supposed to deliver that.
It would make it very easy, like, a package called OpenTelemary OpAmp, just deliver just that, like, talk to OpAMP on that particular thing.
But then again… But then again, since the language, since the configuration file would be at best a template.
Because you are not going to hard-code their enterprise-specific configurations.
and, and, passwords for the OPAM server, then, I'm still not sure exactly.
How far it got?
atoulme 00:27:22 Here's a tidbit, right? So we're trying to use the injectors ourselves in our distribution.
And, recently, we have one engineer, Paulo, come back and say, what we found out is, it's not so much the injector we're using, we want to also combine it with declarative config, so actually trying this approach, which is great.
the engineer who's looking into this, who's also a .NET maintainer, was looking and found out that the declarative config will not allow you to have, to use the default of your SDK. So, it used to be that there were some same defaults baked into your SDK?
With declarative configs, if it's not in a file, then it doesn't apply.
Michele Mancioppi 00:28:04 Oh.
atoulme 00:28:04 And that's really interesting, right? Because that changes a little bit. So you could say that we could ship with a set of sensible defaults.
And communicate that in one file.
And if you could, on top of that, overlay additional configuration per things that would override what is default.
then…
Michele Mancioppi 00:28:25 The overlay is not at the level of declarative configs, because if I recall correctly, that flew out of the window.
Now it has to be one single file. There is no… there is no overlay of YAML declarative configuration files.
atoulme 00:28:38 So, we…
Michele Mancioppi 00:28:39 Ted, keep me straight on that, am I right?
atoulme 00:28:46 And, I'm not sure, let me… let me re-read again what Paulo said on our end.
I can probably share that publicly, that's… There's nothing… So, I think we published that, Yeah, let me put it in the chat, so this will be recorded inside this meeting. It seems that the declarative config is all explicitly explicit slash opt-in.
We can't rely on the defaults of each instrumentation. At minimum, this may require some auto-generation for the declarative config file from each instrumentation.
to preserve each SDK default.
So, maybe you could have one file that has sensible defaults.
In the absence of any other file, this could be the configuration file that is used that has defaults, because if we have nothing, it doesn't work at all. It will just fall flat on its face.
That's interesting, right?
Michele Mancioppi 00:29:43 This presents an opportunity, because that means that the language system packages, they still can deliver their own configuration, their default configuration, tailored for the SDK.
atoulme 00:29:56 Yes.
Michele Mancioppi 00:29:56 And then, we, depending on what else happens, we need to go and get something else somewhere else.
atoulme 00:30:03 That is correct. I think… If we cannot overlay, at least, we should be able to swap config files and point to a different file.
Michele Mancioppi 00:30:10 Which means that we need to actually build the selection of which declarative configuration file to activate in the injector itself.
atoulme 00:30:19 Yeah, so that would be the injector config would then become the place where we… we switch off, we route, yes.
Michele Mancioppi 00:30:27 Which, technically, that's the reason why we did it in the first place.
atoulme 00:30:31 That's… well, that's why the injector has to do a bit better and have this overlay mechanism with conf.d-type folders, where you can… Manipulate this type of things, and you can do better.
Okay.
Michele Mancioppi 00:30:44 Yeah, but for example, we also discussed in the injector sig to have, So today, we can inject environmental variables, but we cannot select by language.
So that is… at the moment, you do not have a mechanism to go and say, for Python, do that.
We have a mechanism that tells us, find the Python SDK there, but not find the Python configs there.
Which is not an insurmountable problem by any stretch of the imagination, but it's a functional gap.
atoulme 00:31:18 Yeah, I think the injector's the right place to play there, right?
Michele Mancioppi 00:31:22 Yum.
Although, something else we need to keep in mind is that if we put too much intelligence in the injector.
Then, we need to replicate that in OBI too.
atoulme 00:31:36 Yeah.
Michele Mancioppi 00:31:37 Because eventually, OBI should come in as another member of the happy family of our packages to cover C++, Rust, Go, without instrumentations.
atoulme 00:31:50 Yeah.
Yeah, and the injector is kind of a… common conduit for configuration of the AI.
Okay.
Michele Mancioppi 00:31:59 Which means we should go and talk to Nicola, and And Mario, about the plans in OBI for declarative configuration, and specifically, which declarative configuration to activate for which process.
atoulme 00:32:13 Yep. Yeah, we want to be aligned, so that we don't create more work for ourselves down the road.
Michele Mancioppi 00:32:18 Okay.
atoulme 00:32:20 Okay, so… I'm not sure if this, okay, so we're a little, getting a little bit of direction there, where… We should have a default config file that comes with the package of each instrumentation language.
Michele Mancioppi 00:32:35 So that doesn't change. I need to adjust the wording of the spec, but that doesn't change.
atoulme 00:32:40 Alright? Then we will allow some overlay situation where the injector can take a different config file that could be dictated by a vendor package, for example.
Michele Mancioppi 00:32:50 No, the vendor pack… oh, wait a second, oh, this is interesting.
atoulme 00:32:55 Yup?
Michele Mancioppi 00:32:56 A vendor package would literally replace the entirety of the same language package, so you won't have on the same system a Java declarative configuration from Elastic and one from OpenTermil, because the two packages are then incompatible.
They declare a conflict and replaces relationship in terms of DAB and RPM, so you do not install both.
In the same machine.
atoulme 00:33:19 Don't… you don't, but… I don't know if I… so, yeah, okay, because of the way the packages are installed anyway, that's unlikely that it would happen. So we're good, okay.
Michele Mancioppi 00:33:29 We can model in the packages a guarantee to have one configuration file per language as defaults.
atoulme 00:33:37 That's fair. I mean, is there a situation where you would have a vendor just want to override the config file, not the jar?
For example.
Michele Mancioppi 00:33:46 That's a question that James also asked, and in my opinion, the answer is no. And if you did that, you wouldn't do it with System Package. They would go and edit the file in HTC.
You are.
atoulme 00:33:57 Yeah, it's.
Michele Mancioppi 00:33:57 so that you are allowed to modify configuration files in HTC, that's the whole point of that.
atoulme 00:34:03 Or you can create a new leaf package, or new leaf Debian package that depends explicitly on the OpenTeametry package.
in… in… does additional things.
Michele Mancioppi 00:34:13 Yeah, but honestly, I mean, I, I… I've met maybe one organization in my life that Packaged configurations as a system package.
atoulme 00:34:23 Yeah, that would… that seems unlikely, you're right, because… What exactly, what flags exactly would you even trigger in these instrumentations just because you're a vendor?
That's all.
Michele Mancioppi 00:34:32 I do not… like, vendors, don't create distros for configuration. Think trade distros to… for bug fixes, for… for other stuff. Configurations come along with the ride, but it's never the focus.
atoulme 00:34:43 Yeah. Okay, alright, so let's make that… let's actually close that door, in that case, right? That's not even… Let's not discuss it.
Michele Mancioppi 00:34:51 Yeah, but then OPAM kicks the door open again, because that is exactly the use case where the only thing that you actually do want Well, no, technically, OpAMP is supposed also to be able to add packages, although I don't think we should allow to mix system packages, I know I'm delivering more instrumentations, because that… that's becoming a mess.
atoulme 00:35:13 Yep.
Michele Mancioppi 00:35:13 The, battle bank deals first and foremost in configurations itself.
atoulme 00:35:19 That's right. So, OpenApp is actually a good companion to the injector, because it… if you wanted to manipulate your injector config.
you would want to drop stuff there, right? That's what op-amp is going to really apply itself. It's not so much… At the level of the… I mean, these plantations might drop some files in some places, but… It needs to go and play with the injector configure.
Michele Mancioppi 00:35:41 And potentially the supervisor.
atoulme 00:35:44 Of course, yeah, yeah, yeah, for… For, yeah.
So…
Michele Mancioppi 00:35:49 And I would really wish for somebody in the OPAMP SIG to join our SIG until we sort this out, because I don't feel I have nearly enough expertise to design that.
atoulme 00:36:00 I mean, we can be sensible about this, but… We're trying to square that circle as well, on our end. That's a really big endeavor. There's a lot of cringey moments, because we have discussions about effective config versus all those things as well, because then the agents can also re… anyway.
Michele Mancioppi 00:36:25 I'm not even going to open the can of worms, that is, the fact that only some languages have dynamic reloading of configurations.
atoulme 00:36:32 No, I think, listen.
Michele Mancioppi 00:36:34 I'll do that, but…
atoulme 00:36:35 We could do a demo… we could work towards a demo of Open plus Injector. Very simple, just change the config files of the injector.
and make it work, and that would be a sensible moment of, like, here is Eureka, right? Coming together, this value magnified by the ability to change on the spot. For example, turn on profiling for your Java applications in this fleet using OpenMP.
Michele Mancioppi 00:37:01 Yep.
Ted Young 00:37:02 I thought there was a… yeah, the discussion yesterday in the spec SIG was really good. You know, people are… definitely see that there's different… different pieces to this puzzle, and, like, different architectures, and it… it feels like maybe, like, a spec doc, something written down somewhere.
or a way for people to propose different plans would probably be helpful. You know, we can have, like, discussions, we can have people come to this SIG meeting, but… but until it's, like, written down into… Maybe not even, like, like, almost like a problem statement, right? Like, would be probably the first step, right? Here's all the things we're trying to solve, here's a couple different architectures that might solve it, but, you know, not jumping straight to solutionizing.
Michele Mancioppi 00:37:52 Excellent.
Okay. So here, I created earlier today this, this issue.
Ted Young 00:37:58 Yeah.
Michele Mancioppi 00:37:58 Do we want to adjust the wording for it?
Ted Young 00:38:04 I think probably there just needs to be a more detailed doc somewhere that explains the… The whole problem statement, right?
atoulme 00:38:14 Okay.
But in my view, The way I've been envisioning this is that Our system packages have best practices to install things in default paths that are well understood and allow compatibility and overlays using convottype.
Ted Young 00:38:30 composition. Yeah.
atoulme 00:38:31 And vendor packages.
And then, on top of that, open plays by adding additional files.
That can be in conv.d type packages, conv.d type folders, that would override the default behavior to… Dude.
Whatever we want.
Ted Young 00:38:50 Right. But, you know, one thing, I wonder about is, like, like, something like that is good, that focuses on using, you know, the file system very heavily, and, you know, hot reloading would be, like, monitoring and re-triggering on the file system. I'm sure there are examples…
Michele Mancioppi 00:39:12 That is a solved problem also for the collector, because, Unless you're running in containers where there are issues, you can have watchdogs in, in… on any Linux host that looks at the inode. The file changes, issues a sync up, for example, to the, to the collector, and that triggers configuration reload.
It doesn't work in containers, but I don't think anybody's thinking of using OpAMP in containers.
I hope nobody's thinking of using components in single containers.
Ted Young 00:39:45 I mean, but, like, do you have rollouts where you're running op-amp as, like, a daemon… you're running the collector as a daemon set, you know, and you're trying to control your, remote, That, you know, you're trying to do, like, remote sampling and things like that.
Michele Mancioppi 00:40:03 No, no, I'm thinking about the collector, because the collector has internally configuration reload capabilities. I'm thinking, like, you are adding the Java jar to the container, and you want to use the supervisor of OpAMP to go and reload the configurations in the Java virtual machine.
I am honestly confused about the extent of where PAMP is going to go. So, for example, it was news to me.
that now there are extensions to have the OPAMP, serve… the OPAMP client in, in the JVM.
And I don't know where… in the, sorry, not your JVM, in the, Java agent.
atoulme 00:40:40 Yeah.
Michele Mancioppi 00:40:41 And, where that is going to go, and I'm a bit confused about where does… is the supervisor going to stop, and when is the client in the SDK going to start? I don't know.
atoulme 00:40:52 Yeah, I think you need to compare… break this problem in two, right? Where fast system, normal system packaging, expected things, that's great.
anything live, live reload, changing of configuration, runtime, these type of things, to me, that's a completely separate set of problems that requires, indeed, a live connection, where the agent somehow is able to get instructions from a remote server that say, turn this on, change the logging level.
From error to debug for the next 5 minutes is a valid instruction that can be sent.
But to me, that's, frankly, I would like to separate those problems in two different sets, so we can…
Michele Mancioppi 00:41:32 They're not entirely orthogonal, unfortunately, because the configurations of, please go and do use OPAMP is something that must play nice with the system packages.
atoulme 00:41:47 You can, you can propagate the change to the config file.
and have a different path where you propagate that change to the running Java applications, but you don't have to do both.
And especially, like, the part where the live reload and all the changes in memory are happening.
are a well-known, like, rat nest that, if you talk to Java maintainers right now, Jason Plum, who works with me, is, you know, up and angry at this… at years. It's like, this is defined…
Michele Mancioppi 00:42:19 is the best language that there has ever existed to do a hot reload configuration of instrumentations. No other language is closed.
atoulme 00:42:26 And yet, and even him is like, I don't like this idea, because I don't want… I want to understand the scope of change and how much we're going to allow, and there's a lot of ways this can cut, so can you please be… can we be very educated and good about this? And he's kind of… angling that discussion. And I would like that discussion.
Ted Young 00:42:45 See you on me.
We're… like, I mean, the JavaSig is very strong, but just the, like you said, the fact that Java is much more dynamic than other languages, you know, like, it would be helpful for us all to have, like.
a plan written down somewhere about, like, how we kind of expect this to… rather than, like, Java just going out there and, like, building a bunch of stuff that just works for them, you know, it would just be helpful for us to… Understand what we're all building.
atoulme 00:43:17 playing with all that stuff. So, for example, right, so I think for files and hosts, I think using system packages, using the proper way of op-amp where you write things down on disk, is the way. We want to do that. It needs to be well done, understood, no problem. On containerized environment, in Kubernetes in particular.
op-amp needs to actually play nice with Kubernetes, and will need to make control type changes, or issue config map changes this way.
Ted Young 00:43:47 Are there situations where there's no file system available, and people want to, like, literally get… like, they never look at the file system, they're just using op-amp to contact a local collector, and that thing's giving it… That Thanksgiving.
Michele Mancioppi 00:44:05 You're not dead.
Ted Young 00:44:06 Hey, I know, you're making noises, right? But I'm like, is this, like, like, requirements gathering, right? Like, do… are there users out there who… where they're, like, the file system, they're in a heroic.
Michele Mancioppi 00:44:15 Purely technically, purely technically, it is trivial.
to mount either empty deer volumes or configuration maps as file in Kubernetes.
Ted Young 00:44:27 Trivia.
Michele Mancioppi 00:44:28 What doesn't work well, because of the issues with, effectively, the lack of watchdogs on iNotes, because of the file system used by the runtime, container runtime, blah blah blah, to actually say, hey, there is a new version now reload.
That is usually the gap.
atoulme 00:44:42 Yeah.
Ted Young 00:44:43 But if you've got, say, a supervisor running as a daemon set, and it's the thing loading those files, right? You're sending your configuration out from some central managed system. It's loading the files, and then it's, like, poking the app, right? Like, if the app has a connection…
Michele Mancioppi 00:45:02 It's not a demon set, because you cannot go… it's on the demon side, usually, because unless you're very lax with the security context, you cannot poke a process inside a different container.
Ted Young 00:45:12 Or a sidecar, but…
Michele Mancioppi 00:45:14 More likely, yes. A sidecar inside the podium.
Ted Young 00:45:18 Yeah, it, it would… I think we… yeah, let's… I'm gonna poke Tigrin, he's the primary… op-amp maintainer, but I'm gonna poke both of the maintainers, and we should just figure out where… to some degree, I feel like these are docs that should be in the spec, given that we're talking about how we, you know, weave together declarative config and Kubernetes and… system packaging and op-amp and all this stuff, it feels like there needs to be some kind of.
Michele Mancioppi 00:45:50 Wait a second, wait a second. Are you suckering me in moving the PR for the meta packages to the spec repository?
Ted Young 00:45:58 I don't know about that, but I'm just saying, to some degree, if we're talking about not just system packaging, but we're talking about, like, hey, what is… what is the general plan around all of this stuff? It probably makes sense for that to be in the spec repo, but…
atoulme 00:46:16 Yeah.
Ted Young 00:46:16 I mean, we can always keep moving forwards with our own repo and being like, these are our plans, come here and have a look at these, but… Yeah, I think we could…
Michele Mancioppi 00:46:26 I would feel very comfortable doing what you proposed, which is very sensible to put in the SPAC, if Antoine and I could pair with the Open people to actually write down a joint thing about it.
atoulme 00:46:39 Yeah, I was going to propose, right? So, my colleague, And Chadhari, is on OpEmp, and that's his job, like, agent management is life, so we can make sure that this gets enshrined into the spec.
I would also say that for this factory packaging initiative, I can actually write off and explicitly put out of scope any containerized solution, and any of those, concerns right now, so we can ship something this year.
No.
Michele Mancioppi 00:47:06 Purely, purely technically, containers, Like, using the system packages in containers was never a main focus of the project.
It's a target of opportunity, because it uses the same mechan… if you're using Ubuntu, the container image, it works the same way.
atoulme 00:47:21 But we must be using Catch, I mean, I… yeah, we can talk about it.
Michele Mancioppi 00:47:25 No, there are people like that.
Ted Young 00:47:26 More specific and say Kubernetes rather than containers, right?
atoulme 00:47:30 I think you need to be careful about something, and I'm sorry, this is really not a good time to discuss this, but there's the classic Kubernetes, and then the OpenShift Kubernetes. On the OpenShift Kubernetes discussion with OpenApp and all that, we'll go over with the cluster controller that we are pushing.
And, most recently, Red Hat, an employee from Red Hat, made a contribution saying, I would like a good best practice on OpenShift, which is always going to be the same. We do always the same thing on Kubernetes and OpenShift, because people want a guided experience. And then you patch on top, meaning you add fragments of configurations that are going to change the OpenShift behavior in a particular setup for this. So, hey, I want that particular Collector to have one more processor.
Here is how you're going to apply this patch inside this.
different way of doing things, because OpenShift and Kubernetes are completely different ecosystems with different people, with different needs.
Fun, right? Anyway.
Ted Young 00:48:37 But you're still talking… it still feels… it's like there's Linux, but there are your… jailing something in a container or not, like, whatever, right? But it's more about, like, Kubernetes is, like, specifically the thing we're calling out as, like.
Michele Mancioppi 00:48:51 I, I think… Right now.
Ted Young 00:48:53 I'm saying, like, don't use this for Kubernetes, use the operator, and we're gonna try to improve the operator experience and all of that.
Michele Mancioppi 00:49:01 I think a healthier demarcation line is not container… other container runtimes versus Kubernetes or OpenShift orchestration, but is, do you want to use this to build a container image or not?
And what they're saying is, no, we are not targeting right now using these system packages to build a container image.
atoulme 00:49:22 Yes, Court.
That's my view, yes.
Ted Young 00:49:24 Yet.
I mean, it's just… I feel like there's…
Michele Mancioppi 00:49:28 Who would do it.
Ted Young 00:49:30 There's, like, fuzziness there, right? Just in terms of, like, I want to kick the tires on OpenTelemetry on my Mac, right? So I'm using Docker, and it's, like…
Michele Mancioppi 00:49:41 And funny you could say that…
Ted Young 00:49:43 containers, but it's really VMs in the background, and like, blah blah, you know, like, it's just, people get confused.
Michele Mancioppi 00:49:48 Funny you should say that, because there is a devil at Dynatrace that actually made a very nice video about the injector, and guess how it used it? How they used it.
They put it in a container image.
Ted Young 00:50:00 Yeah, that's…
atoulme 00:50:01 Oh, ugh.
Ted Young 00:50:02 That's why it's, like, to me, it's more about, like, if you're trying to orchestrate these things in Kubernet, if you're using some kind of distributed operating system, an orchestration platform.
it, like, those things happen to use containers, but it's more about, like, hey, if you're trying to use this with an orchestration system, this is not designed for that. This is designed for Linux environments that are running on their own.
atoulme 00:50:28 Actually, I think the root decency in the relationship here is stronger on the Open side, because I think what OpEm needs to do is to be a good citizen of the ecosystem it's in. So, for example, if it's on a Linux host, it needs to talk to SystemD properly. If it's in Kubernetes, it needs to talk to Kubernetes APIs.
Michele Mancioppi 00:50:43 That's a very spicy take. I like it.
Ted Young 00:50:46 You can absolutely see people wanting to use bare metal Linux with the supervisor, some kind of control plane, you know, pushing these things, so we…
atoulme 00:50:56 You don't… you certainly do not contaminate an OpenShift story with some SystemD discussion that we're having over here, because otherwise…
Michele Mancioppi 00:51:07 Wait a second, wait a second, wait a second. OpAMP can play really nicely with SystemD units.
atoulme 00:51:12 We want that, right?
Michele Mancioppi 00:51:13 You just need to change the configuration file that is mentioned in the unit file. I, like, I would really love to see a design that makes sense without contributing system to units, but I don't think it makes sense.
atoulme 00:51:26 I want OpenM to integrate at the level of the demarcation of a system disservice. Meaning, yes, go change that file, we're good. That's the expectation, there is nothing else, you don't just send, you don't send kill signals to collectors, you don't do anything fancy, that SystemD does it for you.
Michele Mancioppi 00:51:42 Wait a second, wait a second. You're talking about OpAMP delivering the entire SystemD unit specification, or just one of the configuration files pointed by it?
atoulme 00:51:53 No, I want clear demarcation between what Open does and what our system packages do, and system packages should be running system disservices, and Open's going to go talk to files.
Michele Mancioppi 00:52:01 Thank you.
atoulme 00:52:02 And we're good. But in some cases, I've heard discussions about, well, what if the supervisor gets in there and then sends some kill signal? And I'm like, no. You're going to please use SystemD, and you're going to use it the way it was entertained, and it's going to be done the proper way. And we will be inside these boundaries, and if you don't run the collector, for example, with SystemD, or if you don't do the right things.
That, you're outside of the supported…
Michele Mancioppi 00:52:26 Wait a second, do you… do you, do you want sys… opam, supervisor, to trigger sysctal reload?
atoulme 00:52:35 No, I don't want to, right?
Michele Mancioppi 00:52:36 Thanks, Ed.
atoulme 00:52:37 Yeah, but I think this.
Ted Young 00:52:39 This is a dock that would be… rather than just saying, we're only doing this, we don't do Windows, we don't do, you know, this or that, just having a doc where we just start… we just start listing out all the different environments, right? Like, all the ones where it's, like, OpenStack, like, we know for each one of these, there's gonna need to be specific advice. And even if some of them we're like, we don't know the answer yet, it can be fine. Like, Windows, we don't know the answer yet. Mac, we don't know the answer.
elite.
atoulme 00:53:07 It's more than that. Knowing all the difference.
We are not doing it. We're not doing it this year.
Ted Young 00:53:13 No, no, no, no, no, I, but I'm…
atoulme 00:53:14 First case, done this.
Ted Young 00:53:15 See what I'm saying, it's not just about, like, Linux system packages, I'm just saying, like…
atoulme 00:53:20 Do what you're saying.
Ted Young 00:53:21 one of these environments, how do we expect configuration to be managed and loaded?
atoulme 00:53:27 And then I want to be sure, and I will be very direct here, it's like, we will say to people that we are not taking care of Windows this year, it's not in scope.
Michele Mancioppi 00:53:35 I don't know how to write that injector for Windows.
Ted Young 00:53:38 Totally fine to be like, we have… we don't know what we're doing here yet, right? But just being able to know that, like, OpenStack's a thing we need to think about. Kubernetes we have to think… do we have to think about meds.
Michele Mancioppi 00:53:49 OpenStack, OpenStack, there is nothing special, just Linux. OpenShift, that's a different pair.
Ted Young 00:53:55 Yeah. And OpenShift, actually.
atoulme 00:53:57 Red Hat's…
Ted Young 00:53:58 Like, Cloud Foundry? Like, do we need to, like, have a…
Michele Mancioppi 00:54:02 You're gonna be way back.
Ted Young 00:54:05 I…
Michele Mancioppi 00:54:06 No, that is a solution, and that's Buildpacks. You put it in buildpacks.io.
Ted Young 00:54:10 Yeah, yeah, exactly.
Michele Mancioppi 00:54:11 Olympian.
Ted Young 00:54:12 Who wants to do that? Not me, like…
Michele Mancioppi 00:54:14 I did it, and I enjoyed it.
Ted Young 00:54:16 impacts are fine, the marketplace was the part that was…
Michele Mancioppi 00:54:19 Luckily, that is the…
atoulme 00:54:21 Yeah, so, I mean, that's a… if we could attract someone from Broadcom who wants to participate in those meetings.
Ted Young 00:54:27 Yeah.
atoulme 00:54:28 own disintegration, by all means, because they're working on that, and know that much. They are trying to make the collective work well for their stuff, and they have.
Ted Young 00:54:35 I actually wrote the orchestration system for Cloud Foundry was, like, the last major thing when I was actually in…
atoulme 00:54:47 You lived. You lived the life.
Ted Young 00:54:49 That was the thing… That's awesome.
Michele Mancioppi 00:54:50 Even a pivotal?
Ted Young 00:54:52 Yeah, I was at Pivotal, yeah. So the Diego… the Diego backend was, like, the last piece of, like, major engineering I did before decamping for… for LightStep. But… so, like, I know Matthew Coker and all of those people, and there's still, like.
I mean, I don't… they keep repackaging it as Tanzu and Pivotal, Cloud Foundry, and all these things, but there's, like, a bunch of big companies that are, like, still on there.
Michele Mancioppi 00:55:18 I built the most automated Tanzu tile that ever existed within Stana Agent.
added to the thing, and I would go use Bosch deployments to go and create the Instana agent, every single VM. Gig or not, I did not care. The Instana agent was everywhere.
Ted Young 00:55:37 Yeah, man, Bosch. I tried to help Dimitri do a rewrite of Bosch, and I gave up. That was… that was a hill I could not conquer.
atoulme 00:55:45 I saw a demo of Bosch at LinkedIn headquarters by Dr. Nick in 2011.
And he was showing us a screen where he was just installing system packages on a bare VM, and showing us, like, this is the future. I'm like, what are you doing?
Why are you recompiling everything from source? What is wrong with you? What have you…
Ted Young 00:56:07 Bosh was such a chainsaw.
Michele Mancioppi 00:56:10 Don't make me… don't make me talk about the fact that the average Cloud Foundry Foundation had twice as many VMs for the control plane than the data plane.
Ted Young 00:56:20 Yeah.
Michele Mancioppi 00:56:21 That's a talk about that, don't go on record. Dear listener, you never heard this, yeah?
atoulme 00:56:26 Yep, yep, nope.
Ted Young 00:56:28 Diego is the only part that, that… I was happy with, let me say that.
Michele Mancioppi 00:56:34 Ugh.
Speaking of, since we'll be talking about OpenShift.
Can we get somebody from Red Hat in this sig?
atoulme 00:56:44 Yes, Benedict Bongart would be a great guy to have, if not Pavel. I will… I mean…
Michele Mancioppi 00:56:49 I am… I'm much more knowledgeable in dev and APT that I mean, RPM or DNF, or YUM, and by that, I barely know the existence.
atoulme 00:56:58 Alright, so to be fair there, what's happening also is that neither Benny nor Pavel are RPM experts, because they're on the OpenShift side, and so you might not get transferable skills from them to be able to explain to you how to tune in a nice RPM package, they don't know.
They can tell you about the innards of, like, how OpenShift is dealing with, like, whatever load and whatnot, but… I haven't been particularly.
Michele Mancioppi 00:57:24 14.
atoulme 00:57:24 kind of articulate that. I've tried to work with the PM, so I've… I have a contact if you want, Jim Parker. I'm actually going to talk to the Ansible PM right after this, so I can try to get him into this type of discussions.
Michele Mancioppi 00:57:39 I honestly need… we need somebody really knowledgeable in the RPM ecosystem to do the same kind of auditing of the metapackage document that the canonical guys did.
Because Christian, he found a couple of things for RPM, but I don't know what else is going there.
atoulme 00:58:00 Okay, so I'll use the carrot of the fact that the canonical is in there. Where are you guys? Is it good?
Michele Mancioppi 00:58:06 Chronicle did a great job.
Red Hat, did you hear me?
atoulme 00:58:11 Okay, let's do… it's just that.
Done.
Okay.
Let me, let me ask them.
And, the money.
Michele Mancioppi 00:58:22 That's still…
atoulme 00:58:23 to join directly, because I think they would be actually getting a lot of value of those discussions, too.
Michele Mancioppi 00:58:28 Absolutely.
Both, in terms of, alternatives to Kubernetes that we shall not name, and RPM itself.
So, one last thing.
How are we going to proceed on this issue?
atoulme 00:58:50 Oh, for a pen?
So, I think, that you kind of nailed a little bit the direction we want to take, which is we want to have a general direction document that explains how we're going to correlate OpEmp use cases, packaging use cases, and make them come together so we're not having a mess in the end.
Ted Young 00:59:10 Yeah. And Kubernetes operator as well, right? Because they've started to go their own way, you know, they already have some established work on how they configure things and stuff, but we want to kind of…
Michele Mancioppi 00:59:23 I mean, we can talk to Jacob. Last time, we spoke about, you know, yesterday I mentioned that I had spoken with him, and I think that what they want to do, or at least what Jacob told me they want to do, is very much aligned.
atoulme 00:59:37 Okay.
Ted Young 00:59:38 Yeah.
Michele Mancioppi 00:59:38 Antoine, tomorrow I will not make it to the injector's sake, but maybe you can poke Jacob to be there, and maybe we can have the discussion.
atoulme 00:59:47 Yeah, okay, that's great. Also, I think the operator needs to start to take the injector for a spin, right?
Michele Mancioppi 00:59:52 Yeah, that's exactly what Jacob is doing.
atoulme 00:59:54 Okay, cool, alright.
what he's up to these days. He's been doing a lot of… different work.
Michele Mancioppi 01:00:01 Antoine, should I, should I left-click?
Ken, we need this issue with you.
atoulme 01:00:05 Yeah, you could… you leave it with me, I will bring it up and make it a bigger one, I will work with Ted on making sure we correlate all those things together. But one thing I will do is I won't start with things we need to do, I will start with things we are out of support, we are not doing, or we have no plan to do at this time, because.
Michele Mancioppi 01:00:21 The moment you write in a document that people are going to say something they disagree with, that's when they engage.
atoulme 01:00:27 Yes.
I know.
Michele Mancioppi 01:00:28 Go for the, somebody's wrong on the internet, Michael.
atoulme 01:00:32 4. That's my only move.
Thank you.
Okay, I gotta run, but, nice discussion. I think we're…
Michele Mancioppi 01:00:41 That's okay.
atoulme 01:00:42 Trust.
Ted Young 01:00:43 Yep.
