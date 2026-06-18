SIG: Packaging SIG
Date: 2026-06-17
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Sina** 06:53 Hello?
**Michele Mancioppi** 07:07 Hello.
Let me check if… Antoine is going to show up today, because there is… There was a discussion about changing the time of the, Now, he's off for the next 2 weeks.
So, Antoine, based on feedback from, from… Douglas?
Was… Trying to move… this meeting to, combine with the slot of the open terminal injector, because in reality.
It's most… it's to some extent, the same people.
I don't believe it has happened yet.
So, until that happens, we continue with this lot.
So… What is the status?
The PR for the matte architecture is, I think, as ready as I can make it.
There is one point of discussion that, it's still, To some extent, ongoing, and it is whether we want to have multiple Oh, hi Tad.
Did, didn't want to open the issue to change the time, the time of the SIG meeting to overlap with the injector?
**Ted Young** 09:08 Huh? I'm not sure. I'm just getting back.
**Michele Mancioppi** 09:11 I don't think it is, but it will make sense, because, for example, Douglas.
Cannot. He says that it's very difficult for him to join us.
Container, but he has never made it to the… to the… to seek yet.
Is it something that you can help with, in opening the tissue to move to the slot?
**Ted Young** 09:32 Yeah, you guys just want this issue… the meeting time changed to…
**Michele Mancioppi** 09:37 To a further detect, we shortened the one for the injector.
So it's like…
**Ted Young** 09:41 30 minutes, 30 minutes?
Yeah, yeah.
**Michele Mancioppi** 09:45 Sina, Dennis, is something that works for you?
**Ted Young** 09:51 I mean, we can… if the SIG's fine with changing that, we can just change it, yeah, and all.
**Michele Mancioppi** 09:56 Does that make sense?
**Ted Young** 09:57 Okay.
Sure.
**Michele Mancioppi** 09:59 So, I was talking about the status of the PR for the, the, metapackage architecture. I think it's, it's ready.
The, I spent time validating whether we want to use separate configuration files per language, per technology, so one for Java, one for .NET, one for… Python. And, the reason why I went through the discussion is because, from the OPAMP side.
It would be easier to have one configuration file.
But in reality, the status of the implementations of the configurations decays are there.
does not support.
But what you would need in terms of having language-specific overrides in a single file?
The only ones that do support it is Java.
and all the others today, for example, I went into the net auto instrumentation SIG, and they are starting now to implement the SDK, but it's gonna take a while. So, I'm thinking that… We should go ahead with, One configuration file per technology.
It's not the best it could be, ideally one file.
So that we would be able to… the user would be able to set the resource attributes only once, but… Unless I'm missing something massive, I do not see it viable in the foreseeable future.
Anybody has anything to comment on the matter?
I'll take it as a yes.
So the next step becomes the, so I'll merge the PR.
Feel free to go and vote plus one if you want, otherwise I think I can merge it regardless.
The.
**Ted Young** 12:15 A link in the meeting notes to… Yes.
**Michele Mancioppi** 12:19 Yes.
**Ted Young** 12:20 I posted the meeting notes in the chat.
**Michele Mancioppi** 12:25 It is… This, glorious PR.
So the, I've not managed to get any construction with the Open people to do next steps.
To some extent, I was distracted by the stuff going on in other places. To the other, I think that there is some significant gap in what we can achieve today with the declarative configuration.
And what op-amp would ideally have.
Ted, how do you suggest I should proceed?
**Ted Young** 13:21 So, where does that… which direction does the gap need to get closed? Like… On the op-amp side, supporting more of what we can do in declarative config.
**Michele Mancioppi** 13:33 I think, in the best scenario, we have one configuration file.
With language-specific overrides, because that… leads to a better, more unified UX for the end user of the system packages.
It also, incidentally, makes it simpler.
for op-amp, as I understand.
But my understanding of a PAMP is still rather rudimentary, and the discussions about how to go forward with that with Tigran have not taken place.
**Ted Young** 14:07 Yeah, I mean, that would be the next step, I think, would be just to get… get a proposal that Tigrin and the other op-amp maintainer can review.
And get buy-in, and post that, you know, as an issue in the OpApp repo.
Would be a good next step there.
And we can also, I think, bring this up on the… to raise awareness for it, once we have that bringing up on the spec call, and then, like, the spec Slack.
Right, because this feels like a… not just us and OpAMP, right? Like, we kind of want the community to be thinking about…
**Michele Mancioppi** 14:54 I mean, the op-amp is the one piece of the puzzle that I cannot yet fit in my mind.
Yeah. In the case, we know that there are significant gaps, but… Especially the clarity configurations.
**Ted Young** 15:11 The other piece is, you know, the Kubernetes operator, Helm charts, things like that, you know.
The degree to which all of them can have a similar feel for how they work.
**Michele Mancioppi** 15:26 Yeah, I said… I did say I would reach to… to Jaco, reach out to Jacob, but I didn't.
**Ted Young** 15:32 Right.
It's fine. I'm also putting it on our roadmap to try to just make it clear that we're… Trying to come up with a coherent deployment and management.
strategy for open telemetry. Not a bunch of separate little projects.
**Michele Mancioppi** 15:56 I actually went and investigated the… different, the status of the different SDKs in, In terms of, single… like, whether it would be feasible for us for single package or multi-package?
I have it documented.
Here.
The answer is, not great.
To a Java, would work.
The rest.
No.
They require significant work.
And, I am getting the… the vibe that… We shall be holding our breath on this matter.
**Ted Young** 16:49 Okay, yeah.
**Michele Mancioppi** 16:53 I think it would be, Having the decorative configuration files sorted out and implemented properly versus the case.
That would be massive to advance the status of stable by default, but I am… I'm not seeing the urgency in other 6.
**Ted Young** 17:13 Something that we're seeing is just, you know, all the SIGs are in different places, in terms of… where they're at. And for some of them, config can be the top priority. For other SIGs, they feel like they have to chew through other things. But I think something that… Would help, is everyone feels like they're just sort of… Feeling part of the elephant.
And the degree to which we can get buy-in on, like, a higher level design of, like.
how this should work across OpenTelemetry. I think that helps then get buy-in from the individual SIGs.
Even if they all can't get to it today, you know, at least having everyone agree that, like.
This is where it should all go.
**Michele Mancioppi** 18:00 Something that I was thinking, since I have Claude churning through an implementation of the spec right now.
What if in, the, this, like, the next maintainer call.
or as soon as I have a reputable implementation.
**Ted Young** 18:17 Yep.
**Michele Mancioppi** 18:17 We show it out.
**Ted Young** 18:19 Yes.
**Michele Mancioppi** 18:20 And I say, hey, you see here in the tent, it feels a bit wonky.
Here, we need to edit the same file five different times, or 5 different files in the same way, because we do not have the language-specific. I think that could be… I'm more powerful.
I broke.
**Ted Young** 18:40 People work better as, like, editors giving feedback on a proposal, so the degree to which we can get this, you know, into some kind of coherent proposal.
**Michele Mancioppi** 18:50 I'm thinking something even more than a proposal, just to see what we could do, and how much better it could be if we just did X.
Yeah. There is technically a lot that we can do.
But still, it's missing, like, Let's mention a couple of layers of polish.
**Ted Young** 19:07 Yeah.
You think you could have that ready to present next week?
**Michele Mancioppi** 19:12 I hope so.
Okay, yeah.
**Ted Young** 19:14 Let's put it on the agenda, and let's… let's do it.
**Michele Mancioppi** 19:17 Before I put you on the agenda, let me sure that I will have it by then, so… I… I am under enough.
So I will, I will shoot for, for this, maintainer call, if possible. If not, it's gonna be the one after.
**Ted Young** 19:34 Yeah.
**Michele Mancioppi** 19:35 And I think showing some early results.
could, wake up the appetite of, of Parallel 6.
**Ted Young** 19:44 Yeah, yeah, and… Yeah, letting them know, like, seeing where all the other SIGs are at, I think will help, so, cool. Okay.
**Michele Mancioppi** 20:01 I guess the next topic on the agenda is what Dennis wrote about the package hosting.
**Denys Sedchenko** 20:11 Guys, do you hear me well?
Sorry, I'm outside.
No noise in the background.
So, couple of updates. First of all, what, basically, Ophel Collectors did. Basically, they used to sign.
But cosign, like, a sign, is not the same as, like, we need for ABM and RPM repos. Cosign is a K-less signing.
So, basically, how it works.
So there is, like, a design tool.
there is, Basically certificate authority that performs signature, and then with the third service, which basically does a verification, so, like.
Later, the person who consumes the package can verify itself.
That, like, that particular file was produced by a particular entity during, like, CICD stage.
So, what the server does, it creates a temporary 5-minute-long Private key, creates public key, thus assigning, throws away the private key, gives you back the public key and the signature, and then the person who consumes this package can download the public key in a checksum.
Asides along the… with the prior question, then verify it manually within… using the sign tool.
like… this doesn't work for the PPA and… sorry, for the Debian RPM packages, which actually relies… require a normal GPG key.
So… This will not work for us, unfortunately.
I got an access, what, from my personal account on OBS, Also, I skimmed through the Kubernetes, basically proposal, which explains the deployment and build process, and the OBS basically handles the GPG management for you.
Like, signing fees are generated automatically.
And they are basically stored in an encrypted way on the OBS server. So basically, the encrypted key does not leave the OBS server at all.
So at least on the key management side, we're safe.
So, besides the having OBS, we'll be manage… basically, we'll be doing the build process, and providing the runners.
We might need still a separate, some kind of storage bucket.
So we can have our own custom CNAME, custom domain, and plus for load balancing, because if you basically serve packages from the DS itself as the repo, as basically as a CDN, it will not be able to handle the demand.
**Michele Mancioppi** 23:03 And, Let's run a hypothetical.
Sina, you have your hand up.
**Sina** 23:17 You can go ahead. My question was mostly regarding, why is this a concern? I assume it would be for self-hosting.
your RPM packages, because if we're going through the universe and letting Launchpad, I think that's the direction that we were thinking on our side, is if everything is going to be hosted on Launchpad, then we'll let Launchpad and the machinery that's in place handle the signing and everything.
But I assume…
**Michele Mancioppi** 23:41 Indeed is, is the fact of also wanting RPM.
But I am starting to think that maybe, just maybe, we could have the first version to be on Debian, and then maybe that… Makes, that provides a comparable level of help.
So, to make a PPA on launchpad, Because the infrastructure is there.
I no longer remember which part would run on Launchpad, which part would run on no… on our build process, so I will need some help there.
But I'm thinking maybe we start to launch pad then, because the, the, OBS, with having to build those additional infrastructure for mirroring.
And all the difficulties that Denise has been having getting access Doesn't exactly spark trust.
I know.
Let me list.
**Denys Sedchenko** 24:41 One of the benefits of OBS is basically that it provides, so I didn't have, like, many difficulties, it just had a delay for, like, a couple of days before my account got activated.
The benefits of OBS is basically, instead of having two separate places.
Where you build packages that have just one, basically.
plus key management. And also, we probably might need to support much more infrastructure than MD64 and AM64. We might need to support others as well, like PowerPC.
And OBS provides them.
We don't.
**Michele Mancioppi** 25:19 I am, I'm skeptical about it.
I mean, the, I can buy, I'm sure somebody will come up from IBM and say, hey, well, why don't you support ZyOS and PPC?
To which I can say…
**Denys Sedchenko** 25:35 our goal.
I thought that's a requirement for us.
I didn't know that they just have to support just two mainstream architectures.
**Michele Mancioppi** 25:44 I think it would be nice, but I don't know how feasible it is, to be honest.
The, for example, the… I'm trying to think what… I had some thoughts about you in the mentor.
the, the injector should work.
Well, the point is, we never tested Injector on anything that was not ARM64 and AMD64.
**Denys Sedchenko** 26:15 I assume the injector already supports all of those synthetic architectures.
We know.
**Michele Mancioppi** 26:21 We never… I've never had access to a ZOS mainframe since… Installer was bought by IBM, that was 10 years ago, 5 years ago, it's…
**Denys Sedchenko** 26:31 This is so much.
the support surface.
**Michele Mancioppi** 26:35 No, I fully expect at the moment that, for example, the injector goes upstream into the OpenTentry operator.
Some people will come up with that.
But honestly, I would prefer Red Hat to help out with that, because maybe they want to use it also in OpenShift.
So, right now, I don't think anybody dies if we don't go out to support for PPC or ZOS.
**Denys Sedchenko** 27:03 And if the package will be on Launchpad, basically, the customer, like, the person who will use it needs to basically add that Launchpad repo and.
**Michele Mancioppi** 27:14 That is, that is the way I remember it, yes.
**Sina** 27:17 And the milk…
**Denys Sedchenko** 27:18 process a little bit happened outside, so basically Launchpad is just a storage.
Right?
**Michele Mancioppi** 27:24 I'm not sure. I think there are two ways of doing it, right, yeah?
**Sina** 27:29 It depends, yes. Regardless of whether you put it into a PPA or it goes into the archives itself, meaning, universe, meaning whatever.
the build will happen inside the Launchpad machinery, right? So, from there, the signing and hosting are Launchpad's concern.
**Denys Sedchenko** 27:49 And… Our bills are static.
So we are basically shipping static binary.
But as far as I remember, like, in Launchpad, I need to create, like, a separate correct me if I'm wrong, a separate directory for each would want to release. Is it possible to have one single directory? Because, like.
We have no concerns about, like, external dependencies. Just have one repo for all, like, Ubuntu, and Debian… Distro… distro version.
**Sina** 28:25 Yeah, I guess, That's a good question, but I guess that leads to another question of mine before I can, have a more confident answer. The thing is, I spoke to some people, some archive admins, Abu Buntu and John Seeger also.
And what we were thinking is that, initially, what we could help with is hosting the packages inside the universe. And for that to happen, what we were thinking is we handled the packaging ourselves. Now, the way I understand it is you already have some built packages, some built binaries yourself.
Pthers are great, you can continue to use them.
But, the packaging that we would need to do will go through a separate process, right? All the… according to the DBM standard and everything, and we'll maintain those packages inside the archives.
So… That's one part of it, and the other part would be that initially that we're thinking that we're not going to put stuff into DBM and then have them be cloned inside Ubuntu we start with.
Ubuntu itself.
So… With that said, regarding Dennis' question, I think… How… Debian, at least the way I'm seeing it right now, is probably… a secondary concern. Now, we can talk about this a little bit more, Michaela, but I didn't mean to.
**Michele Mancioppi** 29:52 I agree that DPN is a secondary concern, to be honest.
**Sina** 29:55 Oh yeah, that was a bad choice of words, but in terms of the packaging.
for Ubuntu, I think that's where we are thinking a little bit.
**Michele Mancioppi** 30:06 I mean, the, the packaging, so the, the entire, the, the PR, that, that monster PR with the structure.
That is… 90%.
Of, what you would specify for a package.
So… I have a preferred, instead of you going off and making your own packages in-universe.
To work together and… We published that, that specification instead.
I do like the idea of having the build process running on Launchpad.
The foreseeable future.
I think it will also help with, upstreaming this into Ubuntu Universe.
Could work as a starting point, but the packages should also make their way into Libyan.
So that's really going Debian first, and then… and then Ubuntu, that is the way… For me, it would be best.
Yeah, I mean, the bits about, oh, we would create our own packages, I don't think it's that simple.
there is a lot of OpenTelemetry knowledge that is largely encoded into PR, and stuff needs to be published where I… Don't think you would be too successful by yourselves.
**Sina** 31:29 Yeah, yeah, that's not… I didn't mean to intend that. What I… I think the… Point here is, it looks like… things, at least, I don't know, speaking to John, it looks like we want to ensure that things are inside universe. And for that to happen, obviously, with the DBN policy and everything, you know, it's not really… I completely confer, like, I will, I think you're… I'll defer to you. Anything that has to do with the design of the packages, what you have in the PR is completely what we're gonna go with. It's the more administrative things for LaunchPass perspective, like the control files, ensuring that the packages are In the correct order for it to go through all the… Steps down to checks that there are.
what?
John's idea was we… get things into universe, and if someone is interested in taking them to Debian.
They can go ahead with it.
don't know if we need another convo on this, but that's what I'm thinking at the moment.
**Michele Mancioppi** 32:38 I guess that would be a start.
the Canada… Remind me, is it possible from Debian to add a Launchpad PPA repository and just pull it in?
Additionally, So, let's say this land… let's say this lands in universe, in Ubuntu.
If I want to, can I use those packages from Debian as well?
**Denys Sedchenko** 33:03 Good night, Smart.
**Sina** 33:04 App sources, yes, if you update your app sources, because you're always using apps, regardless of whether you're on Debian or you want to. It would just include on Debian distros, it would include an additional step of updating Etsy list sources, D.
**Michele Mancioppi** 33:21 I would like to see how that works.
Would be, if you can show… if you can show us how… how that would work, and then from PPA, we… we have a… somewhat clear path to also cover Debian, that would be really interesting.
**Sina** 33:38 Yeah, I could prepare something else, send it on the hotel packaging channel, once I have it prepared.
**Michele Mancioppi** 33:43 Denise, you have your hand up.
**Denys Sedchenko** 33:46 Yeah, I have a couple of concerns, so first of all.
If, like, okay, we push the practice to the, to the universe.
But you cannot just, like, basically take Ubuntu Universe repo and add it to the Debian.
Your packages might be replaced by Ubuntu ones, and it looks in the two distros, it will be, like, a nightmare, plus it will sound very suspicious.
Other people, it's okay to mix, like, Debian and Ubuntu. Besides that.
If we basically ask some other disco to package our include our software, first of all, we have no control over when the new version is released. We have no control about packages… how packages are actually packaged. There were numerous instances of issues where, like.
Package was packaged very differently by the distro maintainers, and project maintainers got backlog reports, and that reports were caused by how the package was actually distributed.
And, like, there wasn't, like, a package work between distro maintainers and, like, project maintainers for us.
Peaceful maintenance, please stop.
packaging our apps, because, like, we don't want to maintain those unsupported ways of running our software. And, like, plus… Who was working on, packaging architecture, how you actually package stuff, what the name of the layers.
And have no guarantee… we have no guarantee that every bistro to what we actually ask to package our software, they are going to follow this convention. They might run their own convention, so, like, we're basically losing the control. We're delegating the whole meaning of the whole SIG, To each individual distro.
**Michele Mancioppi** 35:44 I, I think this is a valid concern in case this gets, directly in universe, then yes.
I think going to universe is a series of steps.
So, using Launchpad to make our own versions of the packages together with economical folks to help us out.
It's something that I think will be workable. It would be way too early to push these directly into Universe, because there is a lot of stuff we need to figure out on OpenTelemetry's side.
And, I don't think anybody here means to imply that just can't go and run off and do their own things and no longer participate in the SIG, because that, I'm sure, is not the case.
But I think there are a few steps before we get into Universe, both at the level of the quality of the packages, as well as the level of the stable by default initiative in OpenTelemetry, so it's, it's more a journey than maybe what, the way Sina put it, made it sound like.
**Sina** 36:47 I agree, Venice's concerns are very valid. As Miguela said, the point will be that we wouldn't be running off with the packages, but rather, you maintain control over what they should look like, right?
what configuration files there are, how… what depends on what, what pulls what. All of those… anything that is workload, OpenTelemetry-specific, is… remains that way.
we ensure that, things are staying up to date, that they're moving correctly between the different Ubuntu suits. When a new release comes out, that things are there, they're working, they're installable. So we'll help… so, I guess… Anything auto-collect OpenTelemetry-specific, you're concerned? Anything as far as things download.
are secure, they are tested.
All the machinery is compatible with them.
That would be… Where we come in.
**Michele Mancioppi** 37:47 I, personally would like to try.
to… to make a PPA together.
And, and see it work across different Ubuntu versions, see whether we can also expose it to Debian, instead of… through Universe, to make it as a separate repo.
That would give us a clear path, if that works, to a first release that works on Debian derivatives.
And for an RPM, then we see where we land.
**Denys Sedchenko** 38:24 Her question, though… As we are basically landing on Launchpad.
**Michele Mancioppi** 38:31 By the way, we could try in parallel OBS as well.
**Denys Sedchenko** 38:36 Okay.
Then… what?
Needs to be… like, done on a BS site. Right now, I have my personal account, but we'd need, like, a normal account.
Loss…
**Michele Mancioppi** 38:50 The first thing that you would do is that, implement this patch in your personal account, see how it feels.
Try it out from, from… multiple distros, and then compare the pros and cons with Launchpad. So, this is the kind of… this project is… complex enough.
That I don't expect to get it right the first time around.
**Denys Sedchenko** 39:12 Okay.
**Michele Mancioppi** 39:13 I go to the.
**Denys Sedchenko** 39:13 Do we have all the necessary, basically, scripts to build the packages?
So, something that I can, I can work on.
**Michele Mancioppi** 39:23 I'm, I have the implementation that I'm working on. I will open a PR in the next couple of days. I… the code is there, I need to validate it with a few scenarios borrowed from the injector.
And, then I open a PR, and then you take it and try to know BS.
Sina takes it, tries it on Launchpad, see how to make it fit, and then we see where we land.
The, the local repo that I can build with my PR is enough for me to show the concept of the packages and the UX in the maintainer call, and then we see where we land in terms of actual package The build and, distribution.
**Denys Sedchenko** 40:04 Yeah.
**Michele Mancioppi** 40:06 I mean, we always knew that the package build and distribution was the most complex part in the beginning.
Then when that more or less lands, it's gonna become more a discussion about the content of the packages, and that is where it gets, again, very intense. Open telemetry side about Declarative config, and qualitative instrumentations, and which instrumentations we turn on and which not.
But that was always… it was always, like, a second step. The basics that we can get done with Java, Node.js, Python.
Even a rupee, maybe, it's… It's going off.
To get the idea out.
Cool, then let's record it in the… Minutes?
No. So when the PR is open, I will link it in the channel.
In, in the SIG, in the SIG channel.
I am going to target end of the week.
But if, for some reason it slips, then it's gonna be end of the week after.
And, and then we see where we land, with the first home of our packages.
By the way, Sina, does Launchpad allow us to make our own CNAME and certificate for distributing the packages?
**Sina** 42:25 I don't know, But, at least for Launchpad's perspective, it probably doesn't make any, make any difference. Are you… Why would you need to do that if Launchpad handles all this?
**Michele Mancioppi** 42:39 We loved the idea of having something like packages.opentry.io.
slash APT, slash… RPM.
And to be able to… To point it around to different places, because the, build and distribution infrastructure is… by far the biggest question mark of the first phase of this SIG.
So we thought that controlling the C name and the, SSL certificate will give us a way to move around.
Without breaking early adopters.
**Sina** 43:18 Okay, yeah, let me get back to you on that.
I know I've seen examples where people do things like that, like, for example, a lot of the packages that are related to ESM are all on ESM.uguntu.com, other… instead of archives.ubuntu.com, so…
**Michele Mancioppi** 43:36 Yeah, the ESM packages are internal canonical stuff.
I don't know if third parties or less canonically dependent groups can actually control that.
**Sina** 43:48 I'll get back to you on that.
**Denys Sedchenko** 43:53 Having something like, Proxy, like, proxy, like, proxy pass in front of the launch pad. Is it, like, acceptable?
**Michele Mancioppi** 44:06 There will be a bunch of infrastructure to maintain ourselves.
Not impossible, but undesirable.
So it could work, but it's another point of failure.
I mean, we had in the evaluation criteria for the hosting solution the fact that ideally, we would not run any infrastructure ourselves.
As much as possible, right?
At least my opinion on that matter has not changed.
I'm still very skeptical of running solder.
Cool.
That's progress.
We have a… we have a path forward to… Going for it to very… V1, Alpha 0.
version out there.
**Ted Young** 45:04 Nice.
**Denys Sedchenko** 45:09 Let's assume both OBS and PPA are not allowing to, basically.
attaching your CNAME. Yes, we can basically make a small lambda, which basically just returns forward to a target place, or we are taking the, for example, some proxy pass, or, like, anything else. At least some kind of info will be required.
What we can use.
As a worst-case scenario.
**Michele Mancioppi** 45:38 I said a number of times in that case, the seller would happily pay the bill for that infrastructure. It's not, it's not a matter of the money, it's a matter of the complexity of setting it up and keeping it running.
That was always the question, right?
Good. Boom.
Susina, you need to talk to slow down a little bit, John, and About the universe stuff, because we have some things to sort out before then.
But, yeah, I'm looking forward to see if that works out.
Do you know what is the launchpad equivalent for, for RAL?
**Denys Sedchenko** 46:28 proper CCOPR.
**Michele Mancioppi** 46:38 Copper?
Google's.
**Denys Sedchenko** 46:41 and work.
Pandora OPR.
So I'm telling…
**Michele Mancioppi** 46:46 Thank you.
**Denys Sedchenko** 46:51 Here we hit!
Normally, oh, check… This one.
**Michele Mancioppi** 47:03 Very interesting.
Let me share the screen.
So there is nothing in terms of auto here?
As expected, I would say.
**Ted Young** 47:40 I mean, there was, like, an NGINX thing.
Hanging out, that's it.
**Michele Mancioppi** 47:52 And so the launchpad, is… very well integrated in Ubuntu.
Does, this federal copper, is it equally well integrated in Realm, or… Because rel… Fedora as a container is seldom run.
Riley, on the other hand, the, especially the small ones.
That's more… more like it.
**Denys Sedchenko** 48:23 Basically, it's still a repo. We are basically hosting your old BNF repo, and you need to add with DNF repo. If you're dealing with Fedora Silver Brew, you still need to deal with RPMLS3 and all the consequences of it.
**Michele Mancioppi** 48:40 Do you think you… you could try, the same way that Sina is going to try the launch pad to try copper?
To see… How it could work?
**Denys Sedchenko** 48:53 I can play with copper as well, I just need… To something to play with.
**Michele Mancioppi** 48:59 You could actually, both of you, you could actually go and use the current implementation that is in the injector.
project, and take it, and see how it feels. In reality, the specification that we have is much larger, many more packages, and different relationships, but I would say the hard part is already done in the injector packages.
I'm talking about…
**Denys Sedchenko** 49:34 Can you please throw me a link?
**Michele Mancioppi** 49:36 Yeah, I'm looking for a test.
It's actually, I closed that PR, I'll, put it in, in the chat.
So that VR was, it covered, like, the previous concept without, diverto packages, without, interface names, so it was, like.
Very, very early.
But there isn't so much that changes at the fundamental level, so… If one could make a PPA with those and it works well.
Then, we can probably do the same with a more complex implementation.
That is in the PR number 10 on the packaging repository.
At least the spec, the rough.
And in that way, you're not… you're not, dependent on me to make the first version available in NPR.
Cool.
Anything else?
**Ted Young** 51:23 Adam's good.
I'll try to get the meeting time changed, quickly, and… Yeah. I feel like we can do a 30-minute meeting going forwards, right? Like… Does that feel… feel fine for you? We did, like, 30 minutes injector, 30 minutes of this.
**Michele Mancioppi** 51:44 the injector tends to be… tends to be shorter. The, it is… It feels pretty mature, to be honest, as a project already, which is cool.
This one, I suppose that when we start talking about details of the implementations.
We can use the full hour, but we're not there yet.
**Ted Young** 52:06 Okay.
**Michele Mancioppi** 52:07 So we could, we could move to the injector, and then if we see that the packaging always runs long, then we extend.
So we put… we keep the injector first, then packaging, so the packaging can bleed into the… into the next one.
when I look at the, when I look on the calendar, like, the injector stick is, Followed by in a slot with the Kubernetes operator SIG, the JavaSig, Python.
Swift, so there is potential… there is maybe some overlap between the attendees of the injector and, And, the slot after, but not so much from the attendees of the packaging SIG and the slot after, so going longer, half an hour, I don't think it kills anybody.
**Ted Young** 52:57 that… that time slot, just for me, overlaps with the browser SIG, which I'm also helping out with a lot, so I'll have to kind of bounce between both, but… I'm not that important, so it's okay.
**Michele Mancioppi** 53:10 It is, it is, like, we have, like, this sort of ladyhawk… Zone of 2 hours, they're thick as plutonium.
**Ted Young** 53:17 Yes, yes, yeah. When… the time when it's equally annoying for Europe and the West Coast of the U.S. to meet with each other.
**Michele Mancioppi** 53:28 That is the correct phrasing, yes.
It's democratically annoying.
**Ted Young** 53:35 Yep.
Yeah, and then all of my… it's like, when you combine that with work as well, it's the same. It's kind of ridiculous.
That's the way it is.
Anyone who thinks the Earth is flat has never tried to schedule a conference call.
Across three continents.
**Michele Mancioppi** 53:53 I think that anybody who believes that the Earth is flat has… is gonna have their brains bought by the concept of time zones.
**Ted Young** 54:04 Cool.
Alright.
I will see you all on Slack.
**Michele Mancioppi** 54:08 None. See you next week. Bye.
**Sina** 54:11 Thank you, bye.
