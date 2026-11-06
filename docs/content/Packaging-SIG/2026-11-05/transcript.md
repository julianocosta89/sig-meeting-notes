SIG: Packaging SIG
Date: 2026-11-05
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Antoine Toulme (Splunk Inc.)** 02:39 Hey, you made it.
Okay.
**Denys Sedchenko** 02:43 Bonsai Antoine.
**Antoine Toulme (Splunk Inc.)** 02:46 Bujour.
What we got? What we got? Where is it?
The hell?
Oh.
Well, wrong link.
Denise, so… The date is wrong, it's for the 5th. Okay, so… Denis, you want to talk about this?
Interesting.
See if someone else joins.
Me too.
**Diego Hurtado (Dash0)** 03:37 Hey, how's it going?
**Denys Sedchenko** 03:38 Michele should be in Fermint.
**Antoine Toulme (Splunk Inc.)** 03:44 Okay.
While we wait for him to join us, Where are we on a discussion with Austin and, Jeff to… Where are we on that? Netlify changes for Packaging.
Chatted with LFIT this morning, because they're worked on, so expect updates soon.
Yeah, no updates, so… great.
Let me try logging to Cloudflare.
Maybe.
**Denys Sedchenko** 06:03 I checked yesterday, yesterday didn't work.
**Antoine Toulme (Splunk Inc.)** 06:06 Yeah.
I have… So busy with stuff.
I don't have time to keep… to keep pinging people to do stuff, no. It's too much.
Yeah, nothing.
Nothing.
Awesomeness.
**Michele Mancioppi (Dash0 Inc.)** 08:08 Hello!
**Antoine Toulme (Splunk Inc.)** 08:13 Hey.
Alright, let's get… let's get going, then it's got a bunch of stuff in the dark.
So, Denise, you want to talk about open build service for the Debian, and eventually for.
**Michele Mancioppi (Dash0 Inc.)** 08:25 I would like to start from the current OpenPRs, because there is a good amount of.
**Antoine Toulme (Splunk Inc.)** 08:30 Correct.
Let's take a look.
**Denys Sedchenko** 08:34 One of them is actually my dependency.
**Antoine Toulme (Splunk Inc.)** 08:37 Okay, which one do you want stuck with?
**Michele Mancioppi (Dash0 Inc.)** 08:41 Give me a second.
**Antoine Toulme (Splunk Inc.)** 08:45 Dang. Yeah, you're right.
**Michele Mancioppi (Dash0 Inc.)** 08:47 So, this one, me and Diego still need to sit about it.
This one, still no, discussion at the level of the, technical committee about which way we want to go.
This is still blocked on, Ruby not having support for declarative config. So the mat has been doing progress with, the tracing and meter, configure… metrics configuration. If I recall correctly, locks not yet.
This one, Antoine, is it stuck on me or on you?
**Antoine Toulme (Splunk Inc.)** 09:27 So, you approved it, I said maybe I'd like to get one more review for someone else, because you made particip… you actually were actively changing the PR, so I said, okay, maybe, you know, proper etiquette is that we have one more review for someone else.
**Michele Mancioppi (Dash0 Inc.)** 09:44 I'd like to have, Jason.
To look at it.
**Antoine Toulme (Splunk Inc.)** 09:47 Yeah, you're right.
**Michele Mancioppi (Dash0 Inc.)** 09:48 Comment.
**Antoine Toulme (Splunk Inc.)** 09:48 Let me ask him.
Let's see.
I like Jason because sometimes he puts me in my place. He goes, no, I'm not doing that.
**Michele Mancioppi (Dash0 Inc.)** 09:57 I thought that was my job.
**Antoine Toulme (Splunk Inc.)** 10:00 Oh no, it's not your job.
I think you do this as a hobby. You do this for free.
It's, it's,
**Michele Mancioppi (Dash0 Inc.)** 10:06 PSA.
**Antoine Toulme (Splunk Inc.)** 10:06 You're not drawing any revenue from that, man. I mean, let me tell you, you're not making a paycheck out of this.
**Michele Mancioppi (Dash0 Inc.)** 10:12 I am… I am paid in satisfaction.
**Antoine Toulme (Splunk Inc.)** 10:15 That's right.
Will you please review?
Bye.
**Michele Mancioppi (Dash0 Inc.)** 10:21 This one, the establishing tool, needs, another set of eyes, so, Jack and I have been going back and forth.
To the extent where, somebody needs to have a, huh.
Well, it, Denise just did, so…
**Denys Sedchenko** 10:42 Yeah, I really need this PR in main, because I need changes from it. I will, like, I will touch this.
**Antoine Toulme (Splunk Inc.)** 10:49 Dig it up.
**Denys Sedchenko** 10:50 my status.
**Michele Mancioppi (Dash0 Inc.)** 10:52 So, do you think it's ready to merge? You said in, you voted for yes, but is it ready to merge?
Because otherwise it causes conflicts, or what?
**Denys Sedchenko** 11:04 Okay.
Basically, it uses a very interesting approach to track updates for the packages, and I would need this approach.
for the stuff that I'm going to be… to do, like.
let you… I will let you, Michele, finish the PR reviews first, all of the overview of all the PRs, and then I will… Tell what they actually mean.
**Michele Mancioppi (Dash0 Inc.)** 11:30 So this one is something we could consider merging.
**Denys Sedchenko** 11:33 Yes, please.
**Michele Mancioppi (Dash0 Inc.)** 11:35 This one is, something absolutely terrible that, the Node SIG did, and, Matt, I, I opened the… so, effectively, they, they broke the path.
In a way that breaks every single injector out there.
**Antoine Toulme (Splunk Inc.)** 11:51 Oh, man.
**Michele Mancioppi (Dash0 Inc.)** 11:52 Which I hate with the passion of a thousand sons, and then they said, yes, but we are pre-1.0, so of course we can do that.
**Antoine Toulme (Splunk Inc.)** 12:02 Yep.
Nice to pull.
**Michele Mancioppi (Dash0 Inc.)** 12:04 The answer is the fact that you can get away with murder doesn't mean you should murder.
**Antoine Toulme (Splunk Inc.)** 12:10 Nope.
**Michele Mancioppi (Dash0 Inc.)** 12:12 So there, it requires some gentle morration, which is, of course, not my forte, so…
**Antoine Toulme (Splunk Inc.)** 12:19 Totally.
I told them, look, this is not cool, and you broke my stuff, and they said, that's, that's regrettable. We'll do something about it in the future.
**Michele Mancioppi (Dash0 Inc.)** 12:30 Oh, no, this is terrible. So I think that… so I opened a PR for backwards compatible change. Matt is going to talk to them. Antoine, you and I should also go and talk to them at KubeCon.
I'm sorry, this is not okay. I mean, it's sloppy.
**Antoine Toulme (Splunk Inc.)** 12:52 Huh? Yeah, I mean, it's sloppy. Why did they make those changes such a way that It's kind of interesting.
**Michele Mancioppi (Dash0 Inc.)** 12:58 I mean, I understand why this would appeal to TypeScript people, but, I mean…
**Antoine Toulme (Splunk Inc.)** 13:04 What are you doing?
**Michele Mancioppi (Dash0 Inc.)** 13:08 I understand the appeal, but maybe you could have thought about it Before releasing 10 versions of this thing, right?
**Antoine Toulme (Splunk Inc.)** 13:17 I don't think they've had that far, but this is an interesting point in the first place. So, the whole reason this is breaking our stuff is because they're dropping major versions of Node.js support, right?
Because these themselves…
**Michele Mancioppi (Dash0 Inc.)** 13:27 Breaking because of the pie.
**Antoine Toulme (Splunk Inc.)** 13:30 What? Oh, that's even worse.
**Michele Mancioppi (Dash0 Inc.)** 13:32 What the path.
**Antoine Toulme (Splunk Inc.)** 13:33 To change the fucking thing, okay.
I thought the problem was the web support for versions of Node.
**Michele Mancioppi (Dash0 Inc.)** 13:40 No, they literally changed the bloody path.
**Antoine Toulme (Splunk Inc.)** 13:44 Okay, sorry, I got the screen sharing. Okay.
basically.
**Diego Hurtado (Dash0)** 13:49 Can I ask a question?
**Antoine Toulme (Splunk Inc.)** 13:51 You can do… it's a free country again. Go ahead.
**Diego Hurtado (Dash0)** 13:56 It's a free country. I mean, we're in different countries.
**Antoine Toulme (Splunk Inc.)** 13:59 I know, I know, okay, fine.
Don't rub it in either, okay? Cool.
**Diego Hurtado (Dash0)** 14:04 Right, hey, should, should we provide everyone with CI tests that test if their changes will break?
**Michele Mancioppi (Dash0 Inc.)** 14:15 Yes, yes, yes, and this is contingent on, this PR being merged.
**Antoine Toulme (Splunk Inc.)** 14:25 Yeah, you… It's a valiant effort.
**Diego Hurtado (Dash0)** 14:29 Yes.
**Michele Mancioppi (Dash0 Inc.)** 14:30 I mean, we don't… we don'.
**Diego Hurtado (Dash0)** 14:30 That's the kind of effort we need. Sorry.
**Michele Mancioppi (Dash0 Inc.)** 14:33 Yeah, we are almost there. Jack is helping out, because it's one of those things that got sandbagged a bit.
So this thing is something that we should just bloody merge. I'll fix the changelog and read the comments, but the moment that this is in, then the next step is, yo, let's sit down and write this injection contracts, shall we? And they come with PRs in your repo.
So, it's… it's gonna… this is, folks, this is a cultural change in the way that… auto-evolves. Right now, it's very wishy-washy, because site-loading things is not, is not something people, consistently have in front of mind. There is also a hilarious thread about it in… about the demo app.
We will get there.
It's gonna be a painful learning curve.
**Diego Hurtado (Dash0)** 15:26 on the other hand, This kind of shows us the difference between They being technically correct about.
They haven't made any API changes that require some.
**Michele Mancioppi (Dash0 Inc.)** 15:39 It did. It's, but the problem is that the contract is not final, it's not,
**Diego Hurtado (Dash0)** 15:45 is that they are stealing Mail version series.
**Michele Mancioppi (Dash0 Inc.)** 15:49 I don't care.
**Diego Hurtado (Dash0)** 15:50 They can do whatever they really want.
**Michele Mancioppi (Dash0 Inc.)** 15:52 No, zero.
**Antoine Toulme (Splunk Inc.)** 15:53 I mean, they should move to one, right?
**Diego Hurtado (Dash0)** 15:55 No, they should have moved, because that's… that's one of the worst things about semantic versioning, is the fact that someone decided that zero… allowing people to stay at zero forever, it was a good idea.
**Michele Mancioppi (Dash0 Inc.)** 16:08 I'm sorry, I don't care. Like, if your package is in zero-point-something.
For more than 6 months? Yeah, no.
**Diego Hurtado (Dash0)** 16:16 Yeah, it should not be in zero. Right, I agree. Now, the… Anyways, behavioral change, we should add stuff in their… in everybody else's CI.
**Michele Mancioppi (Dash0 Inc.)** 16:28 Anyhow, long story short, this requires moral suasion.
there is a PR, we are going to talk about it with them, hopefully get serious about it, and then eventually get to a point. I'm also writing a proposal for the contract.
injection contract for Node.js, We'll get there, eventually. Right now, I don't know what the hell to do here.
Interestingly enough, we can fix the packaging ourselves.
So, in packaging, we can add an additional script if you want.
That does, does the fallback.
**Antoine Toulme (Splunk Inc.)** 17:02 I mean, the punishment seems fitting to me.
**Michele Mancioppi (Dash0 Inc.)** 17:06 The problem is, the injectors are there.
So…
**Antoine Toulme (Splunk Inc.)** 17:12 Nope.
**Michele Mancioppi (Dash0 Inc.)** 17:13 We can…
**Antoine Toulme (Splunk Inc.)** 17:13 The issue.
**Michele Mancioppi (Dash0 Inc.)** 17:14 around.
But, so we can fix it with, the Node.js package. Injectors out there that have those… that hard-coded path, they're… they're broken.
Wait, wait a second. Is it actually hard-coded, or is it a configuration option?
**Antoine Toulme (Splunk Inc.)** 17:36 the injector path for the Node.js autoload, let me check… I'm pretty sure it's hot-coded, but… Hope… Hope Springs Internal.
**Michele Mancioppi (Dash0 Inc.)** 17:53 No, there is a default, probably, but it should be on file.
**Antoine Toulme (Splunk Inc.)** 18:02 Yeah, maybe. See.
**Michele Mancioppi (Dash0 Inc.)** 18:09 Wait, can it be that we… Literally…
**Antoine Toulme (Splunk Inc.)** 18:14 Node.js autos notation agent path.
**Michele Mancioppi (Dash0 Inc.)** 18:17 Yeah, we need… oh, cool, it's not even hard-coded.
Oh, that's actually nice.
Then, then we maybe don't break anybody and ship, for now a workaround in the, In the packages, We can even…
**Antoine Toulme (Splunk Inc.)** 18:35 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 18:36 Okay, I'll think about it, I'm sure there's a solution. Cool.
This one, I'll get it sorted out, by end of the week.
On Packaging side.
**Antoine Toulme (Splunk Inc.)** 18:49 Cool.
Appreciate that, Ben. Let's see…
**Michele Mancioppi (Dash0 Inc.)** 18:55 Here I need Diego to look at it.
**Diego Hurtado (Dash0)** 18:59 Where… where?
**Michele Mancioppi (Dash0 Inc.)** 19:01 I'll assign you.
**Diego Hurtado (Dash0)** 19:02 171.
**Michele Mancioppi (Dash0 Inc.)** 19:05 Yeah, there is a PyTest nonsense, they broke something.
And,
**Diego Hurtado (Dash0)** 19:14 Pinterest benchmark?
**Antoine Toulme (Splunk Inc.)** 19:18 Yeah.
**Diego Hurtado (Dash0)** 19:19 Why are you running benchmark on CI?
**Michele Mancioppi (Dash0 Inc.)** 19:23 No, it's a depen… it's a test dependency.
**Diego Hurtado (Dash0)** 19:26 Oh, okay.
**Michele Mancioppi (Dash0 Inc.)** 19:27 What is your GitHub user again?
**Diego Hurtado (Dash0)** 19:29 Jose Lotl.
**Michele Mancioppi (Dash0 Inc.)** 19:31 O se lo.
**Diego Hurtado (Dash0)** 19:33 With an L at the end.
**Michele Mancioppi (Dash0 Inc.)** 19:34 No, it doesn't exist.
**Diego Hurtado (Dash0)** 19:36 Well, well, I don't know, I've got an identity crisis now, and who am I?
**Michele Mancioppi (Dash0 Inc.)** 19:41 Diego is a figment of our imagination, according to the age.
**Antoine Toulme (Splunk Inc.)** 19:45 Plato sardines, anything like that?
**Michele Mancioppi (Dash0 Inc.)** 19:47 I'll delete the card.
I'll put in the chat.
**Diego Hurtado (Dash0)** 19:51 How comes I don't show up there?
Wow.
**Antoine Toulme (Splunk Inc.)** 19:55 Probably, like, provision the project to avoid, like, rendos to do stuff.
**Michele Mancioppi (Dash0 Inc.)** 20:02 Either way, I feel we should, we should offer Diego an approver position.
**Antoine Toulme (Splunk Inc.)** 20:08 I'll move for it.
The simple fact that you're attending those meetings willingly.
I would applaud your presence for the last few months, thank you.
No, no.
**Diego Hurtado (Dash0)** 20:18 Oh, sure.
**Antoine Toulme (Splunk Inc.)** 20:19 Well, not less, so…
**Diego Hurtado (Dash0)** 20:20 Oh, thank you, thank you, Aye.
**Michele Mancioppi (Dash0 Inc.)** 20:22 You're more present than simultaneous, who have.
**Antoine Toulme (Splunk Inc.)** 20:24 Yep.
Actually.
We should have, there's an automation in place now, so maintainers who don't participate in projects, well, there's a PR that comes out, there's no drama to be had, and people will be recycled out when that.
**Michele Mancioppi (Dash0 Inc.)** 20:37 But then, it happened before that they approved one renovate PR.
**Antoine Toulme (Splunk Inc.)** 20:44 Okay. Well, I mean… Thank you. You know?
**Michele Mancioppi (Dash0 Inc.)** 20:50 So, Antoine, you take it upon yourself to open the, the PR for the approver thingy?
**Antoine Toulme (Splunk Inc.)** 20:56 Okay, yeah, maybe it's better if it comes for me, right?
**Michele Mancioppi (Dash0 Inc.)** 20:59 I need a review on this one. There was an unspoken dependency with GMake.
It's a… it's a small thing.
It's later updating the contributing.
**Antoine Toulme (Splunk Inc.)** 21:17 Alright, so, I can't take a look.
I'm out. Okay, fine.
**Michele Mancioppi (Dash0 Inc.)** 21:23 And, Denys, you're up?
**Denys Sedchenko** 21:26 Thanks, thanks. We don't have much time left, but this is a big topic.
So, basically, I was working on OBS, We have an OpenTelemetry project there.
Unlike Kubernetes, it's not sponsored, they actually, like, have some kind of agreement with OBS.
But they've basically been a really huge source of inspiration. I basically, like, heavily copy-pasted what they actually do.
And, eventually.
**Michele Mancioppi (Dash0 Inc.)** 21:59 Which license do they have?
**Denys Sedchenko** 22:02 I copy-pasted the approach, not the code.
**Michele Mancioppi (Dash0 Inc.)** 22:07 Can you please answer my question?
**Denys Sedchenko** 22:11 I will tell you, I will tell you.
**Michele Mancioppi (Dash0 Inc.)** 22:14 Okay.
**Denys Sedchenko** 22:17 Okay… So, they released Repo.
**Michele Mancioppi (Dash0 Inc.)** 22:21 Heavy enough.
**Denys Sedchenko** 22:26 Apache 2.
**Michele Mancioppi (Dash0 Inc.)** 22:28 Oh, you… well done.
That is the correct way.
**Denys Sedchenko** 22:33 So, basically, the first of all, I will be moving out from Copper to having OBS as a source of truth, because it handles all of the repos, all of the configurations, and everything.
The second thing, regarding runners.
All of our packages are basically, like, Quote-unquote, let's say, static.
So, I will be doing builds on a Debian and one tool, but I will take, like, the old, like, Debian 12 and 1220 as the host machines.
And the repos will be, like, basically one repo for Ubuntu and one repo for Debian. We can merge them both into one Debian repo, because maybe it wouldn't make, like, wouldn't make any difference, but for now, I'm keeping it separately, just because maybe in future there will be some, like.
divergences.
The second thing, as the OBS will be a source of truth for building all the packages, I think eventually, after the… all the things I'm working will be done.
We could retire all of the stuff that builds the packages.
Debian and RPM packages all of the code for that in our repos.
But the tooling to generate SRPM specs will be left in place, because SRPM specs and assets is… this is what actually gets submitted to the builder.
So Builder basically just packages all of that.
If you're familiar with virtual Linux.
basically, or AUR, in AUR you have source packages and you have binary packages. This is going to work like binary packages in AUR.
So, also, as we package… basically, as we're just doing packaging.
It means every package we ship is going to have a separate version.
And it needs to be updated separately when an update from upstream comes. That's why, like, I really like the approach of Jack, what Jack actually did, where basically he checks if the upstream packages did, like, is changed, it creates Renovate PR and updates the packages.
What I'm planning to do is to basically reuse his approach to create a PR to update the package, basically Debian or RPM package.
Also… as this becomes live, like, after my changes will become live, I think his part of updating Docker images can also be tweaked, so he could just basically pull those packages from our repos.
**Michele Mancioppi (Dash0 Inc.)** 25:12 I don't love the idea.
I truly do not love the idea of having a direct dependency to the packages from the building of the images.
To me, they are two different building processes that start with similar starting artifacts, but should not have a direct dependency.
**Denys Sedchenko** 25:33 Do you mean you don't like a dependency on our repositories?
**Michele Mancioppi (Dash0 Inc.)** 25:37 No, I do not like the idea of building an image by unpacking a package.
**Denys Sedchenko** 25:43 No, no, no, no, you don't unpack the package.
you basically, like, do apt-get install. That's all.
**Michele Mancioppi (Dash0 Inc.)** 25:50 Yeah, I don't like… that is unpacking a package, I don't like it.
**Denys Sedchenko** 25:54 Okay, it's optional, I just, like, just was discussing that it's actually a possible option.
**Michele Mancioppi (Dash0 Inc.)** 26:01 The reason why I'm saying that is it introduces, it effectively, defines the images.
In a way that depends on an opaque definition of the packages.
And it's much harder to understand and debug that way.
**Denys Sedchenko** 26:18 Okay, it's just an idea, just, like, how we can, like, reduce stuff that, like, how to say, code reuse for infrastructure use, but, it's just an idea.
The main thing what I wanted to discuss is to basically… okay, so each individual package has its own individual version. That is, like, clear. I basically see if the version changes, I update a particular package in our repo.
But we have an OpenTelemetry meta package.
Which doesn't have its own version.
The meta package It's going to change quite rarely.
Basically, every time you add a new sub-package, like, for example, like GMX, The metapackage needs to be updated.
And I need to put some kind of version of it.
I could take just, like, a date point time.
of, when the, basically, job is running, or we can have a release.txt file the same way as we do with other packages, but I'm up to… any ideas, but I would like to discuss this now, because this will be in, like.
This is one of the open questions I have in my implementation.
**Michele Mancioppi (Dash0 Inc.)** 27:39 The, so, effectively, the versions for the packages are built of two things. One is, the version of the upstream. So, for example, the no-alto instrumentation something, which the meta package does not have.
and then a suffix of, the revision based on the same thing. For the metapacket.
The metapackage doesn't have an upstream, so it has its own revision thing. For the meta package, having a version number Checked in as the release, great idea, go do it, excellent.
I am wondering if we should have the same to keep track of the revisions of the package Within the same auto-instrumentation version.
For the other packages.
Doesn't.
**Denys Sedchenko** 28:31 Mmm.
Can you elaborate a bit, please? You mean, like, the suffix? The packaging suffix?
**Michele Mancioppi (Dash0 Inc.)** 28:39 I'm not talking about interface, I'm talking about the packaging suffix in the version.
**Denys Sedchenko** 28:46 This opens up question how to, like… Suffix usually touches whether, like, he repackaged the package in a different way.
But… We need some way to distinguish, like.
Okay, a new package was added to a meta package, or, like, something basically affected the… like, the way you bundle the, for example, auto-instrumentation, or injector.
**Michele Mancioppi (Dash0 Inc.)** 29:13 Yep.
**Denys Sedchenko** 29:14 Right now, we have… for them, like, for the actual packages, we have Realist.txt, and we can, like, manually bump it, or, like, manually tweak it.
It's not a problem.
**Michele Mancioppi (Dash0 Inc.)** 29:26 No, but, I'm talking about this, right?
**Denys Sedchenko** 29:33 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 29:35 This thing here, where do we track it?
**Denys Sedchenko** 29:39 Right now?
**Michele Mancioppi (Dash0 Inc.)** 29:40 Package, it's just this.
Yep.
This one, having a file checked in, Great, to that. Excellent idea.
My question is, do we… do we put in the repository?
the tracking of this, or is it something that the build process needs to figure out based on the existing packages?
**Denys Sedchenko** 30:05 Currently, I'm just using release.txt, and now all other tools are using release.txt, the contents of release.txt.
Which is basically…
**Michele Mancioppi (Dash0 Inc.)** 30:16 I can leave it that, I like it good enough.
You have that?
**Denys Sedchenko** 30:22 And for Manpackage, should I… can I just use Release 60 as well?
**Michele Mancioppi (Dash0 Inc.)** 30:25 Yes, I think so. I, please, do, open, do write a document, however.
about how we do the versioning and open a PR to adding it into Docs Design.
**Denys Sedchenko** 30:42 It's a whole can of worms I'm afraid to open. I'm just trying to figure… to finish what I do at the moment.
**Michele Mancioppi (Dash0 Inc.)** 30:49 You can make a, make a proposal.
**Denys Sedchenko** 30:51 Okay.
**Michele Mancioppi (Dash0 Inc.)** 30:52 And, I promise you the review process is not gonna be as sandbaggy as the specifications.
**Denys Sedchenko** 31:01 Okay.
**Michele Mancioppi (Dash0 Inc.)** 31:03 What do you think? Do you, shall we, just, merge?
This one?
**Denys Sedchenko** 31:12 Yes, please, I need this!
I need this, I really need this. I'm going to be doing stack PRs.
To basically simplify life for everyone else.
the first PR in the head of the stack is available for review. This is the latest PR where I basically just add a… Spec generation.
Unlike, like.
I'm not doing the Debian folder thingy, because it's, in my opinion, it's more complicated. I'm going to be using Debbuild, which can consume SRPM specifications, the same file we use for Fedora. This is what Kubernetes does as well.
So at least we're going to have a similar format of specification But, like, two files, but in the same format.
Which is also, like, makes our life easier.
**Michele Mancioppi (Dash0 Inc.)** 32:07 Yes.
Please write it down for posterity.
And, I will give you as quick a review as I can.
**Denys Sedchenko** 32:16 Thanks, thanks.
So…
**Michele Mancioppi (Dash0 Inc.)** 32:20 Can you give me the, the fun email address of Jack, so that I can, I can credit him in, here? Sure.
And then we merge it.
**Denys Sedchenko** 32:30 Sure, sure, sure, give me a second… This is… Mmm… It's hard to copy text on a laptop.
Here… Here's the PR.
**Michele Mancioppi (Dash0 Inc.)** 33:09 So, this is merged.
And this one… I'll have a look. I actually already skimmed it.
But I need to do some proper testing.
All right, cool. Folks, progress. Unfortunately, we are not gonna have, the packages at KubeCon for the official launch with the URLs, because… We are still in, in, in, I'll just storage hell with Cloudflare.
PT.
Could have been cool, since Antoine and I have a talk.
To observability Day, but… Okay.
Yeah, we're gonna, we're gonna say it's gonna be soon enough.
Denise, are you going to be in Salt Lake City?
**Denys Sedchenko** 34:04 Unfortunately, no.
**Michele Mancioppi (Dash0 Inc.)** 34:06 Okay, never mind that.
Then, folks, I think we are probably going to skip the next week, since more than half of the SIG is going to be at KubeCon.
See you in two weeks.
Goodbye.
**Denys Sedchenko** 34:24 Bye.
**Diego Hurtado (Dash0)** 34:27 But…
