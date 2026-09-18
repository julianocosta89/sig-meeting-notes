SIG: Packaging SIG
Date: 2026-09-17
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Ted Young (Raintank, Inc. – Grafana Labs)** 04:06 Hey, hey, how y'all doing?
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:10 Good to have you.
**Michele Mancioppi (Dash0 Inc.)** 04:12 Love it.
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:14 Good to see you here, Nikola.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:16 Yeah It's my priority for this quarter, so…
**Ted Young (Raintank, Inc. – Grafana Labs)** 04:22 Yeah, there you go.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:23 more involved.
**Michele Mancioppi (Dash0 Inc.)** 04:25 I thought it was making that happy.
Or maybe it's both, it's the same.
**Nikola Grcevski @ Grafana / OpenTelemetry** 04:33 Yeah, my name is Bro, yeah.
**Michele Mancioppi (Dash0 Inc.)** 04:36 Lots of people.
Damien, welcome! You're back from parental leave.
**Damien Mathieu** 04:48 Yes, thank you.
**Michele Mancioppi (Dash0 Inc.)** 04:51 Nice.
All right, time is of the essence. We only have 30 minutes for the slot, and there is a lot to talk about.
Before we jump… If you have topics, and I, Jerry, I, I know you want to talk about PHP auto instrumentation.
So do I.
Caba, the, DBM packages, Please write it in the, in the meeting notes.
So that we managed to cover all the topics.
Before we start proper with the agenda, let's look at the, open issues.
I'll share the screen, hopefully it works.
Yes.
The first and the last, is, stuff that, Diego is working on to, Like, some concepts of how to evaluate the health of the installation.
And, to, add the mechanic to… make sure that our site customized script in Python aligns with the version of the Python that the SDK supports?
These ones I'm… I'm reviewing.
Antoine wants to add the package for the GMX scraper.
The, I left, comments. I don't think it goes hard enough in terms of improving upon the user experience.
So hopefully Antoine picks it up again.
Issues, I have not seen anything new.
Other than, what I created after, Discovering unrelated issues that, It's maybe time that we start looking into building container images.
Because that is the topic with PHP.
If you don't mind, Damien, I would do first the containers bit.
Jerry, do you want to set the stage?
**Jerry Ting Fung Leung** 07:35 Sure. So, Actually, I… for me, I, I'm working on to try adding PHP support to Kubernetes operator, in OpenTelemetry, and the thing is that they are, pushing back the hosting of the auto-instrumentation PHP image in their repository, so I am right now working in different ways to see if there are any chance to get that image.
or… or the… or the idea to other… other repositories. So, recently, I… I managed to… to put the auto instrumentation under the PHP contrib, but, when… when you say, the OpenTelementary Packaging is also a place that can help To… to set up this container image, I would like to know more about that, and see how… how it works, and to see, what things I can contribute to… to this repository. So that… that's… that's pretty much,
**Michele Mancioppi (Dash0 Inc.)** 08:45 The reason why we didn't call this SIG system packages, but Packaging.
It's because, ultimately, it should be the home of the ways we deliver instrumentation and things. One of the topics that is going to come up later, for example, Damien with the homebrew package.
That's not… that's… okay, technical assistance package for macOS, but nobody will think about it really like that, right?
So, it was always, the intention for the Packaging SIG To, relieve the operator, SIG Of the, distrib… creation, management, and distribution.
Of the container images.
We have not yet invested on creating the infrastructure for it.
But, I have some thoughts on how we could actually Take the repositories that they already have.
on, on GitHub, because there is a GCR.
docker repository, and I also think they published them on Docker Hub.
And move it over under Packaging, because The mechanics… of injecting Node.js, PHP, Java on Kubernetes with the operator are, like, 95% the same.
as doing it on any other Linux.
So, it's, it's just a good match.
**Jerry Ting Fung Leung** 10:20 Actually, I'm not so sure about this point, because, for… for PHP, the… the… we… we need to set up, Various version, or… or different setup.
Because, HP is based on C, and… and you have… you see there's a… GLIPC version, or muscle C version, or… or they… they have different PHP version support, and also the thread safety of PHP, so with thread or without thread. So, this combination, right now, I have to, actually run a script in the application container to… to run some several command, for example, php-something to… to… retrieve, those parameters in order to spot… to… to find out the right, the correct AP… correct… correct APM library to… to install, so I… I don't know how does it disrupt in… in that, because I don'.
**Michele Mancioppi (Dash0 Inc.)** 11:30 You may not be aware of the OpenTeleTry injector.
Which is a little bit of software, which is in the process of being adopted.
by the operator, and that it is the beating heart of the system packages that uses LD preload.
To be able to execute code outside of a process.
Where, for example, the logic that you're describing Could be homed.
And, pick the correct thing to start. We already have For example, both Python and .NET, Need, different binaries.
to be, to be injected, depending on whether the runtime is linked against Blue Lib C or MasoC.
And we do that through introspection of elf symbols.
Both Nikola and I are maintainers also of the injectors, so we can help you with that. For PHP, I know from experience at Instana that it's more convoluted.
It's, I was surprised they did not mention the word sappy in there, because I still get nightmares. But ultimately, those are things that we could put in the injector. And then the packaging would be a little different on the container image.
you need to have all the versions, and then select the correct one at runtime. In system packages, you don't need to put both GLIPC and muscle C, because we do system packages only for, for Debian, Ubuntu, and RAL at the moment. We are not targeting Alpine, because nobody uses that on a virtual Linux host.
So that, at least, that particular… Dimension of your matrix, is not relevant.
something that is important, and the actual mechanics, I would be very interested in jumping with you on a call offline to see what your logic is.
Something that is, really important and you did not mention, is to validate that the version of PHP that you are, your injecting to is compatible, because I know that the PHP instrumentation works only in PHP 8.
And I don't know what's going to happen when you're trying to inject it on PHP 5 or 6 and so on, which is also something that we must check before we actually activate it. I assume you use the PHPRC environment variable to turn it on.
To actually load another extension file, so… That's an additional check that, that you will need to do.
**Jerry Ting Fung Leung** 14:05 Well, for this… for this issue, I think we just need a check before injecting, because, the OpenTelemetry just supports, PHP 8, all up, so, This doesn't.
It's that easy right now.
**Michele Mancioppi (Dash0 Inc.)** 14:22 No, because the… If you go… I'll give you… I'll give you a parallel of what you're saying with Python, right?
Out there, So the Python SDK and instrumentation support, if memory serves, 3.10+.
Yep.
There are people using Python 2.7 out there.
the failure when you inject into Python 2.7 is catastrophic.
You cannot go and say… well, you can, but you should not say, yeah, but the user is responsible to know into which bots to inject, and they need to be sure it's only PHP8 and above.
Because they will say, oh, that is PHP, I'm going to try it, and then it's gonna break. In reality, it should… it should… Stand down seriously by saying, with a message, say, hey.
this PHP is not compatible, we're not gonna do anything to it.
So you cannot really assume that the rantom in which it will be injected is compatible with it.
This is especially true in containers.
Because the people that are… there's always a split, there's usually a split between the platform team that sets up the kind of instrumentation and observability, especially in cases with automatic interaction, and developers, and the developers know which version of PHP it is, and the operators not so much. So you should not assume.
that… the decision of trying to inject PHP is a sound one.
**Jerry Ting Fung Leung** 15:54 I… I see. Yeah, so… So there's a lot of things to… you… you mean there's a lot of things to do in the OpenTelem… OpenTelemetry injector, so as to make sure those steps are correct, and… and then to… to inject the correct… the right extension to… to the… to the… to the environment.
But… but how do we start? So, it is… so, is it more on the injector side, or more on the packaging side?
**Michele Mancioppi (Dash0 Inc.)** 16:30 There are two aspects. One is the contract between the PHP automatic instrumentation and the injector. So what is the injector supposed to do to inject PHP?
That is best discussed in the next half hour.
We could also… something we could do, actually, is, having the discussion, maybe you and I, one of these days.
offline, and we come up with a proposal for what the contract is, and a proposal of how to split the logic between all this detection of threat safety and SAPI and everything else for PHP, and then that is a proposal to the injector team, and then Ideally, the part that is hard-coded about PHP is relatively limited, and we find a way, a good interface for the injector to say, okay, this looks like PHP, I'm gonna run the check to see if it needs to be injected. In reality, what happens, what works very well, and I do not know how to do it in PHP, is actually to have, because I never looked, it's, to have a two-stage load.
where PHPRC is always set.
And then there is something that will check, for example, a small init php script, right? I don't know what PHP can do.
And check whether to continue with the loading of the actual thing.
that you do in Python with a site-customized Pi that you are going to see in the OpenTelemnity Packages repo.
**Jerry Ting Fung Leung** 18:02 Hmm.
**Michele Mancioppi (Dash0 Inc.)** 18:03 I'll… get in touch on Slack, I'll shoot you over my calendar, and I'll drive you through the steps, because it takes a bit of work and a bit of ingenuity to make sure that when we inject stuff, we don't explode people.
**Jerry Ting Fung Leung** 18:19 Sure, sure, yeah.
**Michele Mancioppi (Dash0 Inc.)** 18:21 For this sake, however.
There is the discussion of, folks, do we want to start working on hosting container images?
And taking over the, affiliated maintenance of the container images from the operator.
I am… I am for it.
It's something that I always thought we should be doing.
Anybody, strongly against it?
**Ted Young (Raintank, Inc. – Grafana Labs)** 18:49 I think it's a great idea. I mean, I think we need, you know, we're still at, like, early days in making basic decisions, so keeping that in mind.
You know, while we're choosing things.
Is a great idea.
**Michele Mancioppi (Dash0 Inc.)** 19:04 Anybody committing to seeing the work done?
I, I'll, I, I already have, A proposal in the works on how to do this.
When I saw the movement in the PHP SIG, I got excited.
It's something that we require, agreement with the operator, SIG, because right now they effectively create and maintain unwillingly, I'm told, the images for Java, Node, and the rest, so it's effectively, like, handing over those.
But the contract for injection is… the same in system packages, it's simpler, because we don't care about Mathieu yet. The rest is literally the same, so… It, it, it naturally honed here.
**Ted Young (Raintank, Inc. – Grafana Labs)** 19:53 I mean, we still have some more fundamental things we've got to roll out, but my hope also is, as we get that infrastructure set up.
less taking it off the plates of the operator people, maybe just asking, would they be willing to… to port their work over and continue to maintain it, but just through… through here. It's like a starting point.
**Michele Mancioppi (Dash0 Inc.)** 20:15 Yeah, that's, that's a… as a first phase transition, that's not a bad idea.
In reality, I understand there is not much maintenance going on in those images. It's pretty straightforward. It's more like the fact that they work incidentally, but the fact that nobody has yet had a good reason To unknowingly break the contract.
But there is no contract, right? Yeah. For example, I don't know what's gonna happen with the new node SDK, Which is supposed to change again the injection mechanism there is probably the first time the contract breaks again.
So, Jerry, I'll shoot you over my Calendly, ping me on Slack.
Sitting by my Calendly, and And we've come up with something cool.
**Jerry Ting Fung Leung** 21:04 Yeah, sure.
**Michele Mancioppi (Dash0 Inc.)** 21:05 is the last, big ticket item language that Injector could support and doesn't yet.
Right, just because the Elixir people don't… don't know how to play ball yet.
**Jerry Ting Fung Leung** 21:16 Yeah, sounds great, yeah.
**Michele Mancioppi (Dash0 Inc.)** 21:25 Damien Europe.
**Damien Mathieu** 21:27 Yes, thank you. I guess this should be a bit quicker. So, as was mentioned earlier, when this SIG was kick-started, one of the things that we wanted to do was homebrew packages.
And one that we wanted to do rather soon is for OCB, OpenTelemetry Collector Builder. Right now, to install it, you have to do a GoGet, which is not great, obviously.
I already have a repository that works under my own account, but obviously…
**Michele Mancioppi (Dash0 Inc.)** 22:01 Go to Laser tasks, or with the tabs.
**Damien Mathieu** 22:05 Sorry?
**Michele Mancioppi (Dash0 Inc.)** 22:06 with Go Release or CAIC, I assume?
**Damien Mathieu** 22:09 No, we don't need that, because the collector releases repository already publishes a binary, compiled binary, so we can use that directly from collector releases.
**Michele Mancioppi (Dash0 Inc.)** 22:25 Okay.
**Damien Mathieu** 22:26 I'm going to link my repository right after this, but I'm pressing the space button, so I can't… And so, yeah, basically I have a proof of concept showing it, and, it's kind of just unless there is, an opposition, a confirmation that, I'm good to start the repository.
And, assign this team as owners of it, obviously, and we can start doing, those packages.
**Michele Mancioppi (Dash0 Inc.)** 22:58 Now, the question is, would you put it in… why a different repository? Why do we need it?
**Damien Mathieu** 23:08 Because Homebrew is relying on, repository name for, for separate taps. So this is not a CAIC, it's a tap, because it's a CLI tool. So you do brew, tap, and then you do OCB, sorry, OpenTelemetry.
And that would just add the OpenTelemetry tabs straight away, but in order to do that, the repository needs to have a very specific name, which is under the OpenTelemetry org. It needs to be named Homebrew Tap.
**Michele Mancioppi (Dash0 Inc.)** 23:46 Denise has the hand up.
**Denys Sedchenko** 23:48 Yeah, I have two questions, I was also recently dealing with homebrew packages, so I still have Vietnam flashback. First of all, homebrew is became popular also on Linux, like, it supports Linux, and also became popular on, Immutable distros?
for example, like, Fedora Silver Blue, or, like, if you want to do it on Steam Deck.
Are there, like, plans to support, like, Linux there as well? And the second question, The second question is… Are there plans to eventually, basically.
after, like, to get rid of our, Homebrew tab, and basically upstream it to Homebrew Core. I know it can be a very hard, complicated process, especially, like.
Considering, like, maintainers sometimes reluctant to cooperate, but still, is it, like, in a plan?
**Damien Mathieu** 24:49 So, yes and yes. The Linux one on… if you look at my proof of concept, it's already supported. We built the binary, and in the homebrew configuration, it's just basically telling it where to find the binary, and giving it a checksum.
My proof of concept is also fully automated, so there is a GitHub action that runs daily, and when there is a new version of a collector, it opens APR.
So there is very low toil there, and it does support Mac and Linux. I don't know about, containers or, like, systemless things.
But I would expect it works the same way, and as long as, collector releases builds the… like, the binary properly, it should work fine.
As for going, upstream, yes, it should be the… ideally what we end up with.
But, Homebrew has been very, kind of frightened about having us, because we are writing on our READMEs that we may retag releases, and that's basically an, like, a no, no, like, a stopgap for them.
So we…
**Michele Mancioppi (Dash0 Inc.)** 26:06 It breaks through entirely. You do that, and then people need to reclone it.
**Damien Mathieu** 26:11 So, for the records, we say that in README, but we do never retag for OCB. It's for, more for the, like, collector contribib, I think, that is maybe retagged sometimes. It's frightening them because it's in our documentation.
So that's why it's a bit tricky with them to do so.
**Michele Mancioppi (Dash0 Inc.)** 26:32 My ask is… so I will help you, get this done, I'll be your reviewer.
My ask is that you make a repository structure that we would be able later to use for other packages as well.
**Damien Mathieu** 26:47 Yes, that's always been the plan. Homebrew Tap is a very generic name, so it's always been the plan to, have more than just OCB, yes.
**Michele Mancioppi (Dash0 Inc.)** 26:56 By the way, why do you want to go with TAP and not with CAIC?
**Damien Mathieu** 27:00 Tasks are for UIs, whereas tabs are for CLI tools. So we may need a CAIC later on if we have a, I mean, that's what I understand, reading the difference between them, and that's why we were talking about a tab and not a CAAS.
**Denys Sedchenko** 27:19 Also, one important thing… Although you technically put… you can technically put the CLI binary under the cask.
But the difference also in binary signature requirements.
So, if you… basically, if you put your binary as a regular binary, not as a cache, during installation, Homebrew will remove the quarantine attribute, which is appended to every file downloaded from internet.
And that allows you to run unsigned binaries.
With casks, it doesn't do that, binary has to be signed, it's not going to work.
Also, you would need to put it as a CAQ if you need a special macOS entitlements, like, if you want to deal with For example, with Hypervisor or other, like, system… low-level system-related stuff.
**Michele Mancioppi (Dash0 Inc.)** 28:12 Sandwich.
**Damien Mathieu** 28:13 would not be the case, at least for OCB, and I'm not sure anything else would need a CAIC, actually.
**Michele Mancioppi (Dash0 Inc.)** 28:19 We are unfortunately running long, and this was mostly my fault because of the previous lot.
Let's try to, to knock down the next, the next few topics. So, Damien, reach out to me. I'm traveling next week, but we can find some time to look at it, or just offline, like, you point me at your repo, I'll look at it, and then we organize the migration.
**Damien Mathieu** 28:41 That sounds good.
**Michele Mancioppi (Dash0 Inc.)** 28:44 Next, TED native 5 for, for DNS and blob storage.
**Ted Young (Raintank, Inc. – Grafana Labs)** 28:49 Yeah, so just real quick, this is, you know, one of our blockers is just figuring out where we're gonna put all this stuff.
Looking into what we currently have access to is we use Netlify for managing OpenTelemetry.io. It's also where it seems like we're managing the DNS for that. Seems pretty reasonable to manage the DNS for packages.openTelemetry.io there as well.
We don't currently have an account with Cloudflare. Netlify does offer blob storage, but when I looked into it, it doesn't… it doesn't actually seem fit for our purpose. It seems more like a tool tacked onto the side of their… their web hosting stuff. For example, they charge for egress, and they have some weird API that isn't S3 compatible, so I'm just guessing that's not gonna work.
**Michele Mancioppi (Dash0 Inc.)** 29:38 The charges for ignorance are worrisome. The, I don't think we would expose the API, the bucket as an API where it's 3 anyhow. I mean, if that is, you just do HTTP stuff, we don't care.
**Ted Young (Raintank, Inc. – Grafana Labs)** 29:51 minor detail. The egress is more… it's just more when I looked at it, I was like, this seems more like a tool for people making websites with Netlify and, like, tacking some things on the side, not for what we are trying to do, so… I'm guessing we should go ahead and create a Cloudflare account.
Likewise for, COPR, We don't have any kind of account like that, but, if all that… basically, we could go ahead and create these things, and then, put the credentials in 1Password.
And the GC and everyone's kind of fine with this crew figuring out what they want as, like, a first step, and then… figuring out the ultimate ownership of these things as a second step. But COPR could certainly be maintained by the… owned by this… the maintainers of the Packaging SIG.
**Denys Sedchenko** 30:54 One thing I would also ask, just in case, to also request the credentials for OpenSeus OPS.
Because we might need to have it in the future, because I have concerns about Debian.
Like, for Ubuntu, yes, there is a packaging, like, infrastructure.
Okay, let's not…
**Michele Mancioppi (Dash0 Inc.)** 31:18 Let's talk about Debian, because the… Okay. Maybe you were not there last week, where,
**Denys Sedchenko** 31:25 Yeah, I was… sick.
**Michele Mancioppi (Dash0 Inc.)** 31:26 Yeah, so, Caba, you're up.
**Csaba Gyorgyi** 31:29 Thank you. So, basically, there is the technical pos… so, Ubuntu versus Debian, that is the technical possibility and the practical reality, and since… because from Canonical, only Sina and me are doing this as a side, Quest.
We will only focus on, Ubuntu, and not on Debian. If someone were to put it onto Debian, that would be great, but it won't be seen on me.
**Denys Sedchenko** 32:02 Okay, in that case, I would still like to request the credentials for the OBS as well, because OBS is basically, like, a universal solution in terms of, like, it handles, like, everything.
For building stuff.
It's just to have it an extra… An extra option in case we need that.
And yes, like, I was absent for 2 weeks.
because I was sick, I would like to ask what I missed. Do we have any, like, progress on, like, credentials or infrastructure to basically kick the packaging Ball rolling.
**Michele Mancioppi (Dash0 Inc.)** 32:43 It's, I'm not gonna lie, it's a bit of a letdown, to see, that, Canonika will not invest in, in, help us getting into… into Debian. I… I understand that this is something that… Sub areas on the side, and I appreciate that.
I'll… I'll have work with… words with Mark when I see him next time.
So, that leaves, the discussion of, So, the option for Ubuntu is, do we want to do Launchpad?
I think this SIG needs a little time to… to, recover from, from the, no, actually, we cannot do Damien upstreaming, and to figure out what we want to do there. Having in parallel, like, if we decide, yeah, we want Debian, then put it in Debian, then putting it in Launchpad as well doesn't make so much sense for anybody involved.
The way you see it.
**Csaba Gyorgyi** 33:52 Could you please clarify? So, what do you mean by Launchpad? So, Launchpad is a built form.
So…
**Michele Mancioppi (Dash0 Inc.)** 34:00 Yeah, because on Launchpad, we would have the, effective Ubuntu release trains, right?
But if we go and put it in Libyan, we get Ubuntu release strains anyhow.
Yes?
**Csaba Gyorgyi** 34:14 But if you put it into Debian, that won't… magically appear in Ubuntu, so we will still have to sync it, and it will… so everything that's in Ubuntu is built on Launchpad.
So, if you want to put a package into Ubuntu.
That package must be built from source code on Launchpad.
**Michele Mancioppi (Dash0 Inc.)** 34:38 Okay, I, I thought, that, the inclusion…
**Csaba Gyorgyi** 34:41 because Ubuntu is based on Debian.
Ubuntu, most of the time, takes packages from Debian.
If necessary, makes some adjustments and rebuilds them, but from source.
**Michele Mancioppi (Dash0 Inc.)** 34:56 Okay.
**Sina** 34:57 Yeah, so the packaging itself can remain unchanged, but the building needs to happen again this time, as Chavez said.
**Michele Mancioppi (Dash0 Inc.)** 35:06 I was, the… what I was thinking about is that, what I knew is that, effectively, like, everything that… that there is Most of the stuff in main and universe comes by policy into Ubuntu.
I didn't know that, the decision is done package by package nowadays.
**Sina** 35:27 Yeah, so the coming from Debian to Ubuntu is fine, so it flows from Debian upstream to downstream Ubuntu. But once the packaging, like, for example, the source changes, the source code has arrived in Ubuntu, the building needs to happen again on the Ubuntu site.
So…
**Michele Mancioppi (Dash0 Inc.)** 35:43 No, that I understand this.
**Sina** 35:45 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 35:51 Okay, I do not understand the implications right now. I need to… To think a bit about it.
**Sina** 35:57 Yeah, but the point is regarding your concern, if someone goes and puts them in Debian, and it flows downstream to Ubuntu, it will be in Launch… it will be built… built through Launchpad anyway, right?
**Michele Mancioppi (Dash0 Inc.)** 36:08 It's more like, should we focus then on going directly to Debian, because then it flows on Ubuntu? Because in my head, if it lands in Debian, it will automatically land in Ubuntu. That's how I've always perceived it. You're telling me that actually there is a decision point for that, Denise?
**Denys Sedchenko** 36:27 Yeah, so… I see… like, maybe I'm wrong, but I see personally going right into operating system.
Repositories as a long-term goal, Because right now, it will be much faster to basically prepare our own repo.
And plus, people would still might like to use our own repo, because, like, if you're using, like, Ubuntu, which is, like, previous LTS or LTS to versions behind.
You might be stuck with the old version of packages, and if you want to use, like, something up-to-date.
you would use our own PPA.
Plus, like… every maintainer… every packager of, for example, Ubuntu, Debian, they might want… might have their own different views on how to package.
The package, sorry, like, for repeating the same word.
So, like… They might strip some stuff, or they might disagree with our solution, so it's like… Having our own repo is basically also a safeguard.
In case of some kind of issues, because it's quite often, like, the story of, like, having a bugs.
Of, like, system pa- of a system package.
And, like, when you observe that the package was actually packaged a bit different, that's why you get those bugs, or because the version is very old, it's, like, quite a frequent story.
**Michele Mancioppi (Dash0 Inc.)** 38:10 Yeah, then the question about OBS is very topical still.
**Denys Sedchenko** 38:16 Yeah, I would still have, like, have an OPS, like, as an extra… extra option, because, like, we have Ubuntu, and also we have a Debian.
And, like, Launchpad can handle them both.
**Michele Mancioppi (Dash0 Inc.)** 38:31 Yep.
**Denys Sedchenko** 38:32 I basically just need to count, I assume I, like, we can just reuse all the… all of the stuff that I did for the OBS, sorry, for the Fedora, and the stuff that was done for the launch pad, because basically.
the way you build those packages, the tooling will be the same. It's just, like, the… The place where it happens will be different.
**Michele Mancioppi (Dash0 Inc.)** 39:00 Alright, well, that, clears, the last point.
Preferred, The last point of the agenda.
**Denys Sedchenko** 39:14 So the question, how to speed up this process, do we have, like, a separate SIG, which, like, handles accounts, credentials?
**Michele Mancioppi (Dash0 Inc.)** 39:23 No, to my understanding, Ted and Antoine are working on this.
It was more like Ted saying, because that idea was, was Netify, and Because of the website, but then Ted looked into that and said the glob storage is a bit… Meh.
Yeah, if, Probably Antoine is going to be in the interactive SIG, so I'll ask him for an update there.
Alright.
Thank you, folks. We're running late for another SIG.
See you next week.
Bye.
**Sina** 40:02 Just a small thing, I booked a time with you, with Caba, to speak tomorrow about this post. If I get a chance, I wanted to pitch you a small idea about the Snap I'll just revisit it again, because I spoke to someone who's a bit of an expert in the realm of, at least Node.js and JavaScript packaging, and, for the Node other instrumentation module, and he was trying to… he was saying, go for the SNAP. But let's preserve that conversation for one minute.
**Michele Mancioppi (Dash0 Inc.)** 40:28 Yeah, we can talk about it tomorrow. So, I need to think about what you folks just said. It was a bit of a cold shower.
Okay. Bye.
**Sina** 40:38 Bye.
