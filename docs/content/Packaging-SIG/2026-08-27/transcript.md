SIG: Packaging SIG
Date: 2026-08-27
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Diego Hurtado (Dash0)** 00:17 Hey, how is it going?
**Csaba Gyorgyi** 00:21 Thanks, everything is great.
**Diego Hurtado (Dash0)** 00:24 Awesome. This is the… this is the packaging.
Meeting, right? Yeah.
Okay.
**Csaba Gyorgyi** 00:29 Is it your first time here?
**Diego Hurtado (Dash0)** 00:32 This is my nth time here, I don't know.
the same here?
**Csaba Gyorgyi** 00:39 Yes, this is my first time.
**Diego Hurtado (Dash0)** 00:42 Right, So, we may not have a meeting today, I'm sorry to disappoint you.
**Csaba Gyorgyi** 00:48 Yeah.
**Diego Hurtado (Dash0)** 00:49 Oh, Denys is there. Because, hello, Denise. I think a few of the usual Suspects.
Out of, vacation.
**Csaba Gyorgyi** 01:01 Yeah, Sina will be also coming.
My conical canonical.
**Diego Hurtado (Dash0)** 01:09 Oh.
Okay, okay, okay.
Oh, Denise, are you gonna run this meeting?
Denise?
Then it's a little bit quiet today.
Well, there's a Google document.
Hmm… Yeah, no section for today, so… Not sure if.
Today… Denys, we cannot hear you.
You're still muted.
Nope.
We can't…
**Denys Sedchenko** 02:21 And now?
**Diego Hurtado (Dash0)** 02:23 Oh, much further, yeah, yeah, loud and clear, yeah.
**Denys Sedchenko** 02:25 Got you.
Oh my god… Zoom selected the wrong microphone.
**Diego Hurtado (Dash0)** 02:31 All the samples.
**Denys Sedchenko** 02:33 Okay…
**Diego Hurtado (Dash0)** 02:38 So… I was just telling Caba that we may not have a meeting today.
But, I don't know if, there's something you want to discuss.
**Denys Sedchenko** 02:52 There's stuff I want to share.
**Diego Hurtado (Dash0)** 02:56 Right, Mikel is on vacation, and I think Antoine is on vacation too.
But,
**Denys Sedchenko** 03:02 Something.
**Diego Hurtado (Dash0)** 03:02 you… sorry, if there's something you want to… share, I can definitely listen, and I can share it with Michele when he comes back.
**Denys Sedchenko** 03:14 Yeah, so, on my side, first of all, I started decoupling the PR for Fedora Copper.
Into, like, different mergable chunks.
And the first chunk, which builds, brings SRPM specification building.
to build, like, the package on the copper side, that's actually merged.
To continue, I basically need the infrastructure.
Also, I've been looking into Fedora… sorry, into the changes, that was done by, that, Sina did.
And, like, the GitHub repo actually doesn't contain change, like, it's… GitHub repo is incomplete.
Because the publishing job on GitHub repo doesn't work, but the package was published.
Also, the GitHub repo contains only the injector, but But the actual launchpad repo contains, like, everything.
So, like, drugs, like, totally big difference.
**Diego Hurtado (Dash0)** 04:24 I need to… Sorry, when you say GitHub repo.
You refer to the OpenTeleventure Packaging Repo?
**Denys Sedchenko** 04:33 No, okay, so basically, what Sina did, he created a separate repo To package stuff for, for lunch, but it's not a fork.
I can give you the link.
Yeah, booster.
**Csaba Gyorgyi** 04:52 I can maybe also clear up the confusion, because we worked on it together with Sina. Basically, we tried to investigate how to get the injector and the plugins into Ubuntu, and our first Let's say, prototype was that instead of building front cores.
we downloaded the pre-built binaries, from the official release. And obviously, just packaging the binaries into that package wasn't hard, and this is why, in the, Launchpad PPA, you can have everything, because that's an outdated thing, but eventually we gave up on packaging the plugins for this Ubuntu release, because there are just so many missing dependencies that it would have been impossible.
So, yeah, but for this release, we only plan the injector.
**Denys Sedchenko** 05:51 Yeah, and I checked out the GitHub repo. Thanks for explaining why there is, like, the difference. In GitHub repo, I saw there was a… basically an infrastructure to build the Debian source packages for the injector, and then after that source is prepared, I assume it's, like, it's something like the… it's something kind of similar to Fedora SRPM spec, but you also, like.
push the sources as well. And then that's pushed to the launchpad, which actually, like, does all the build process.
But I assume it doesn't work, because I couldn't find any successful job on GitHub Actions.
**Sina** 06:32 Yeah, that's cute.
**Denys Sedchenko** 06:32 Either he's missing, yeah.
**Sina** 06:35 Yeah, sorry, Vince, go ahead.
Yeah, just to… The CI, we haven't fully set it up yet, but the way it works right now is you build… we build the packages, and then we use Depo to put them into the PPA.
we just didn't give the CI yet the permissions that are needed, so at this moment, just Caba and I can put on, or upload to the PPA, but once we're ready.
will, ensure that the CI can do that as well.
**Denys Sedchenko** 07:06 I have a question, how do you want to approach this?
further, because, like, for example, we are going to have our own Fedora Copper package.
And then after it's built to Copper, I'm basically going to download the repo into our blob storage.
And, for Canonical, do you plan, like, to keep the infrastructure in your own repo, or you want to upstream this to OpenTelemetry?
Because on one side, like, we can have this in OpenTelemetry.
Or we can just mirror your Launchpad repository, like, you can basically can, like, download it.
Periodically. How do you want to approach that?
Or maybe we should, like, postpone this question until Michaela returns.
**Sina** 07:55 Yeah, I mean, it's… it's a good question, and honestly, I'm not too sure. We just… We asked that casually a while ago, and we decided to keep it under the canonical namespace until we are done with experimenting.
And I think, Cabo, we were planning on moving it even to Launchpad, right?
Where are we gonna fill in GitHub.
**Denys Sedchenko** 08:14 Also, as far as I know, there are two GitHub organizations, Launchpad and Ubuntu. Ubuntu one is kinda open source.
And canonical is kind of internal. Am I wrong, or right?
**Sina** 08:29 On GitHub?
**Denys Sedchenko** 08:30 Yeah, like, in terms of, like, open sourceness.
**Sina** 08:34 Yeah, I think they are both, like, more or less the same. I'm not too familiar with the Ubuntu namespace, because we… most of our work is under the canonical namespace, but… It… there are both internal and fully public things under Canonical.
So, like, if you have something that needs to be private, we can probably make that happen, too.
**Csaba Gyorgyi** 08:56 And we even have external contributors even in, under the canonical, org in Ubuntu.
So…
**Denys Sedchenko** 09:08 In any case, if it's possible, I would… I personally prefer this to be upstreamed to the packaging.
Ready, Paul?
Contributions are welcome. I have just one question.
I'm not really… I didn't work with Launchpad before.
But as far as in… so, like, as far as I know, Launchpad signs the packages themselves.
But still, if you want to push the sources, the sources also needs to be signed, but this is, like, an authorization key or something like that. Can you, like, a bit explain how it works?
**Sina** 09:44 Yeah, For example, with this PPA, as you see right now, it's under the observability team, and the observability team on Launchpad has about 12 or 13 members, and, for example, Caba and I are a part of it. So, we upload our PGP… our public PGP keys to Launchpad.
So, there… therefore, when we are… when we build the package locally, we sign it using deep, for example, the dev site.
And then when we push it to Launchpad, as long as the key that has signed the dev is belongs to someone who's under that namespace, it accepts it, otherwise it will reject it. When, when it becomes a regular Ubuntu package, I think the way it will work is there will be some people who will have the upload rights, for example, people who are archive admins or multi… or masters of the universe, and as long as they sign it and they upload it, their Launchpad will recognize them as having… as the key that signed the package to belonging to someone who has general published access, or published rights.
**Denys Sedchenko** 10:47 It's like identity management. Thanks.
I have a question about Ubuntu, sorry, like, about Debian. As far as I know, Launchpad does not support building for Debian, it builds only for Ubuntu.
And if this is right, we still would like to support, to support Debian.
And, like… What would be the best way, like, to actually, like, approach that?
**Csaba Gyorgyi** 11:20 I think one important thing that should be highlighted, that if we put… if we want to put this directly in the Ubuntu archive.
then it must be compiled from source on Launchpad. So this is one of our main challenges with Sina. This is why we cannot just package everything, even though there are already dev packages upstream that were both on Debian and Ubuntu.
So, this is a main challenge, that if we want it in the Ubuntu archive, then we have to build it from source on Launchpad.
So, this is the… The main, challenge.
That we are facing.
As far as… I know Debian, I mean, I am sure it can be… hacked together, but you know, because Ubuntu is based on Debian, why don't we just put it in Debian, and then Ubuntu can just sync it?
**Sina** 12:22 Yeah, I don't know how long ago it was when we discussed this in the SIG, but essentially the… like Chawa said, Launchpad will build a Debian-compliant package, so technically that package that it builds will be installable… it could be installable on Debian as well, format-wise, but, dependency-wise, it may not necessarily work, right? And it will be in the wound. Once Launchpad builds it and it's uploaded, it will be in the Wound archives. So, technically, like Caba said, you can hack Debian to go to the Etsy app sources, for example, to install from Ubuntu, there's just no guarantee that it will work, it's… It's not something that's, recommend it, right? Because you never know how the dependencies will work.
**Denys Sedchenko** 13:10 That's true. Let's assume the binary is… Portable static?
Because, like, for example, the Python instrumentation is basically a huge blob of files.
I will skip the question of Python versioning for simplicity.
But, like, if it's just a blob of Python files, there is no, like, glibc, dependencies, something like that, yeah, technically it can work on Ubuntu.
But… sorry, on Debian, but… on installation instructions for Debian users, it would be strange to ask them to put in Etsy app sources list.
the path plus you know that suffix for, like, every Kubuntu code name, to put the suffix for Ubuntu code name into LinkedIn, the instructions to be stretched a bit. And in order to, like.
in order to, like, move it, like, let's assume I want to copy-paste that into, like, a separate Debian path.
I'm not sure if, so, like, as the, as the launchpad is a source of truth for signing repo metadata, I'm not sure whether it will not break the repository, like, it will not… it will preserve the signature if it will just, like, copy the directory with a different name.
**Sina** 14:36 Yeah, it's a good question.
What do you think, Caba? Not too sure.
**Csaba Gyorgyi** 14:49 I'm not sure I clearly understand the question, so basically you want to… mirror the Ubuntu archive, but under a different name, or what would be… deploy, or added to a Debian system that point your Debian system that, okay, from now on, you also use this,
**Denys Sedchenko** 15:11 Okay.
**Csaba Gyorgyi** 15:12 The packages as well.
**Denys Sedchenko** 15:14 My question is about repository metadata signature, when it breaks.
So let's assume… Let's assume the ideal situation that the packages we put that they are, like, binary compatible with Debian. You have basically nothing to break. I will skip the question of dependency versions intentionally. Let's assume we don't have that problem.
We've built… Launchpad builds for us, for Ubuntu… for Ubuntu, like, the last… latest Ubuntu LTS version.
And like… I want to, like… it's not… it's going to work on Debian 100%, but I want to avoid, like… a confusion that, like, person puts in, like, in Etsy sources list, it puts the URL which mentions Ubuntu.
And I want them to basically give the Debian Debian path, Debian URL. Plus, like, in case we would like to introduce some Debian-specific hacks, like, it's better that person already uses the Debian-specific path.
On CI side, after the LaunchBot finishes building the package.
What I'm going to do, I'm basically going to download the whole, repository and mirror it to the blob storage, to S3.
And in S3, I can technically create a directory for Adobean releases.
And just copy-paste the repository metadata and the… from the… from the Ubuntu releases.
So, and, like, I have a question, whether this operation will bring, like, After I copied the in-release file.
And release files, those two files that have metadata.
And if I copy them into a new directory, Will this break?
like, the… the path for the Debian.
In that path, will the repository… sorry, like, the repository signature, will it be broken or not?
**Csaba Gyorgyi** 17:31 I don't want to take a wild guess. I think… We should just try it out.
That seems like…
**Denys Sedchenko** 17:38 sense.
**Csaba Gyorgyi** 17:38 way of doing it.
But this really raises the question that if we really want to put it in Debian in a way that it feels native to Debian, why don't we just put it in Debian? And then we also solve the Ubuntu problem, because Ubuntu can sync it from Debian.
Why are you trying to do it the other way around?
**Denys Sedchenko** 18:05 Hmm, because… Although it will… the package will be Debian, but… There is a lag.
between, like, open telemetry releases and, like, what's available on Ubuntu or Debian, especially considering what release of Debian or Ubuntu you are using. So we still would need, some, we still would need, like, an upstream repo. For example, if you want to install Docker, you have two ways to install Docker on Ubuntu.
And, like, Docker.io package you get on Ubuntu, and the Docker Engine package you get on the Docker PPA are, like, different… versions.
Thanks.
My only concern is, like, I cannot build for Launchpad, like, for Debian on Launchpad.
And also, like, I can do it myself, but I need to own GPG signing key. But okay, nevermind. I will figure this out.
**Sina** 19:05 Denys, I haven't, followed the developments with copper, how's that going?
Like, do we…
**Denys Sedchenko** 19:12 Yeah, so basically, I had the POC, It works.
I asked other people to try.
What right now I'm doing is basically one huge POC PR, trying to slice it into chunks and downstream them. The first chunk that builds the source RPM package.
is merged.
Now I'm basically waiting for the infrastructure I need.
organizational Fedora Copper, like, efficient one, not my personal one.
I need the blob storage, because we will need our own domain, so, like, we'll mirror that stuff to the blob storage, and also, like, basically infrastructure.
And we're hoping to do the same with Launchpad.
Similar way.
**Sina** 20:02 But, that's great, and so the RPMs are already available on Copper, or are they stored in the releases of,
**Denys Sedchenko** 20:12 Cop… they are available on copper, but on my personal copper.
**Sina** 20:17 Oh, okay.
Yeah.
**Denys Sedchenko** 20:21 Yeah, I suggest you to check the Packaging Sync channel on Slack. There are some multiple posts from me mentioning the progress.
**Sina** 20:32 Nice.
**Denys Sedchenko** 20:43 Do we have anything else to discuss today as well?
**Csaba Gyorgyi** 20:46 Well, maybe I will just shore.
Quick idea, not strictly.
Important.
But basically, we were wondering that, okay, this Ubuntu archive and the packages come with many constraints, and whether, could we do it with a snap or not? And we had concerns whether it has the same expressing power. And basically, this is a proof-of-concept solution that does nothing, but takes the upstream packages that are already there in the release page, and wraps them in a snap, and in the install hook, it just installs those dev packages, and in the remove hook, it just uninstalls them.
So, basically mimicking a manual install.
But the main point would be that a SNAP package can also make those changes that we need.
And… Yeah, it mainly come up because we were wondering that, if we cannot put things in a timely manner in the Ubuntu archive, what other options we have, and this is something that came up.
**Denys Sedchenko** 22:03 what… what value does Snap brings, besides, like, the workaround to install the package? Because, you see, confinement is classic, basically no isolation.
will be… will it, like, so I assume it basically installs the packages on the host system itself?
**Csaba Gyorgyi** 22:22 Yes, that's exactly what it does. The install hook is one command, apt install those dev packages.
Obviously, it… you know, it's not like a proposal, it's just more something, To show, and maybe give some ideas.
Because intuitively, snaps are not well suited for this, because snaps usually focus more on confinement and everything, and what we are doing is the exact opposite of confinement. We are modifying other processes and giving them observability feature.
this is just a demonstration that, even though many Snap features are unused.
It can still be a useful means of delivering the binaries.
**Denys Sedchenko** 23:22 In that case, it's very… Very sophisticated way to run Coral, in my opinion.
Oh.
**Csaba Gyorgyi** 23:32 You know, the… You know, it's just an idea.
something to keep in mind. I can also imagine other uses, not just the curl, but yeah, obviously, if you are fam… if you are comfortable running in a curl in… the shell, I mean, of course it can be done.
**Denys Sedchenko** 23:56 So, if we're talking about, like, the practical concerns, like.
I will skip the question that it's the snap and etc.
Security stuff, like… This package is essentially curling free files.
Like… in whatever min that will be done, I don't care, but we need at least some kind of, basically.
Signature, package check. Ideally, signature check.
I'm not sure if… whether those files are, I'm not sure if those files have cosign signature, but if we have cosigned signature, we need to certify it. Plus, we need, Cassand check as well.
Pinning.
**Csaba Gyorgyi** 24:41 But, so this is just a proof of concept. This is… I am not saying we should just drop the BM packages and opt-install them. The… what I wanted to demonstrate with this is that Snaps can also do the modifications that the devs do.
if we whenever decide that maybe it's a comfortable way for Ubuntu users.
Then, obviously we can, build those, binaries As different snap births from source, and Make it, more, let's say, pack… Packaging best practice, friendly solution.
**Denys Sedchenko** 25:28 books.
You're a very, very rare guest here, unfortunately.
Will you be able to join on the first or the second week of September, when all the team will be in place?
**Sina** 25:46 Sure. I think so.
**Denys Sedchenko** 25:48 It will be very great. I will be very grateful.
**Csaba Gyorgyi** 25:51 Hmm.
**Denys Sedchenko** 25:53 Because right now, here is just Diego and me.
**Csaba Gyorgyi** 25:59 Regarding, with this, SNAP packaging.
Besides then showing that, yeah, this can be done, if you have, any… Concerns or potential challenges that we might face.
If we want to go down that road, that feedback is also welcome.
**Denys Sedchenko** 26:23 Strength.
**Csaba Gyorgyi** 26:24 Again, this is, just something that came up.
It's, not a decided future direction or anything, this was a side experiment.
**Denys Sedchenko** 26:38 In snobs.
a question in snaps, like, are they, like… I know it's, like, one Snap, we can automatically install it on the multiple one, two versions.
It's, like, one of the advantages of snaps.
And, under the hood, they are also, like, working like a container where, like, under the hood, you actually have your own virtual distro that your image is using, like Fathub, basically, yeah?
**Sina** 27:06 Just the next question for us. Yeah.
**Denys Sedchenko** 27:08 Okay.
**Csaba Gyorgyi** 27:14 But if you have classical confinement, then… Yeah, thank you, Tao.
Jess.
**Denys Sedchenko** 27:20 This is called IDE score.
Okay.
Let's wait for the rest of the team to take a look at this.
**Sina** 27:32 Alright.
**Denys Sedchenko** 27:33 Everybody can, like, share it on the channel.
It was 6 strong.
Oh.
If there are no more topics, let's conclude the meeting.
Thanks for coming, guys, I hope to see you again.
Seymour?
**Sina** 27:54 Sounds good.
Thanks a lot, then.
**Denys Sedchenko** 27:56 Thank you.
**Csaba Gyorgyi** 27:56 Thank you guys.
**Diego Hurtado (Dash0)** 27:58 Right.
