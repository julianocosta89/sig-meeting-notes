SIG: Packaging SIG
Date: 2026-07-30
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Denys Sedchenko** 02:00 Hello?
**Diego Hurtado** 02:17 Hey.
How's it going?
**Denys Sedchenko** 02:20 Fine, and how are you?
I hope this is.
**Diego Hurtado** 02:24 You're right.
**Denys Sedchenko** 02:25 Boom.
Yeah, I hope this is a regular.
**Diego Hurtado** 02:27 And…
**Denys Sedchenko** 02:28 room.
**Antoine Toulme (Splunk Inc.)** 02:30 Hey, everybody.
**Diego Hurtado** 02:35 A lot more people are joining.
**Antoine Toulme (Splunk Inc.)** 02:36 Yup.
**Diego Hurtado** 02:37 Antoine.
**Antoine Toulme (Splunk Inc.)** 02:38 Sorry, I got a really slow start to my computer.
I don't know what's going on, it's just very slow. Yeah, new, new place, right?
Do you want to put your stuff, put your name in the thing?
Yeah, that… You'll type it every time?
Okay.
Can we talk about… can we go through the agenda, or should we wait a minute?
Let's wait.
**Denys Sedchenko** 03:14 Okay, 2 more minutes.
**Antoine Toulme (Splunk Inc.)** 03:16 I'm gonna put a thing here, say, we are getting started.
The newsroom link works.
It's on the notes.
G-Duck.
Alright, let's wait 2 minutes.
**Denys Sedchenko** 04:02 Antoine, are you in the office, or this is a home… are you at home, or this is a home lab behind you?
**Antoine Toulme (Splunk Inc.)** 04:11 I'm in a garage.
This is actually a garage.
This is a standing desk in the back of a garage, and I got… 3D printer, woodworking.
I got a Dell server here.
I used to have more equipment making, starting to take my stuff away.
And then I have a couple more things going on here.
Yeah, it's,
**Diego Hurtado** 04:37 always… always been curious about that Pac-Man…
**Antoine Toulme (Splunk Inc.)** 04:42 It's a vending machine.
**Diego Hurtado** 04:45 Does it work?
**Antoine Toulme (Splunk Inc.)** 04:47 Oh, yeah.
Except when someone turns on…
**Michele Mancioppi (Dash0 Inc.)** 05:11 Oh, well, people.
**Denys Sedchenko** 05:13 Nice.
**Diego Hurtado** 05:16 That's cool.
Hey, Michele, we, Antoine is showing us the arcade machine.
**Michele Mancioppi (Dash0 Inc.)** 05:24 He's showing golf, isn't he?
**Antoine Toulme (Splunk Inc.)** 05:28 That's right.
**Denys Sedchenko** 05:29 We have one more extra member today of a Packaging SIG, my cat.
**Diego Hurtado** 05:34 Everybody has something to show, you know?
I gotta show something. I have, foam nunchucks. I'm learning to do this thing.
**Antoine Toulme (Splunk Inc.)** 05:45 Nice!
**Diego Hurtado** 05:47 It's great to start, Mr.
**Antoine Toulme (Splunk Inc.)** 05:48 room.
**Diego Hurtado** 05:49 Yeah, it's a good idea, because you're gonna hit your… the back of your head.
**Michele Mancioppi (Dash0 Inc.)** 05:53 And the nose. And the nose.
**Diego Hurtado** 05:56 Yeah, exactly.
**Antoine Toulme (Splunk Inc.)** 05:57 Cheers.
**Diego Hurtado** 05:58 What about you, Michele?
**Michele Mancioppi (Dash0 Inc.)** 06:00 Oh, I, I live in a, in a white, in a white room, there's nothing.
**Diego Hurtado** 06:05 Sounds as well.
Next time.
Bring something next time.
**Michele Mancioppi (Dash0 Inc.)** 06:11 No, I, I don't need instructions. All the fun I need is system packages.
So… We have an influx of new issues. I… yesterday, I went to the, OBI SIG, and I was like, folks, we have finished Phase 1, except for you.
And, that picked up a hornet, a good hornet nest.
**Antoine Toulme (Splunk Inc.)** 06:44 I'm here, I'm…
**Michele Mancioppi (Dash0 Inc.)** 06:46 I'm going to put on screen the, the open issues.
**Antoine Toulme (Splunk Inc.)** 07:06 Sorry.
Yep.
Yeah, I saw that you had some stuff going on.
What's happening there?
**Michele Mancioppi (Dash0 Inc.)** 07:12 I went there and, more or less stated them a bit.
**Antoine Toulme (Splunk Inc.)** 07:16 That's cool.
Are they open to having a Debian RPM package?
**Michele Mancioppi (Dash0 Inc.)** 07:21 Mario said it was anyhow in his personal goals to do that.
Tyler jumped in, asked a bunch of questions, read our documents, started opening issues, we will get to that.
**Antoine Toulme (Splunk Inc.)** 07:35 Kit.
**Michele Mancioppi (Dash0 Inc.)** 07:36 What is this?
**Antoine Toulme (Splunk Inc.)** 07:40 It says Renovate. Renovate is always going to have that open.
So it's how you talk to Renovate. You don't talk to it. If you check any of the boxes next to it, you can make it do stuff.
It's my understanding, at least. I'm not the best at renovating that, I don't have the time.
**Michele Mancioppi (Dash0 Inc.)** 07:59 Okay.
**Antoine Toulme (Splunk Inc.)** 08:00 Yeah, just, so this issue will be… Always there.
**Michele Mancioppi (Dash0 Inc.)** 08:05 Alright.
This one, denis, do you have any updates?
**Antoine Toulme (Splunk Inc.)** 08:13 Yeah, yeah.
**Denys Sedchenko** 08:14 Yeah, yeah, yeah, I have, I have some good news.
Maybe I can share a screen.
Don't you let me.
Okay… Where is it?
Here is a… So, we actually… Do you see this?
**Michele Mancioppi (Dash0 Inc.)** 08:41 I'm playing the Majesty of Antoine, and now me, and that's not all the.
**Denys Sedchenko** 08:45 Oof.
Sorry.
Maybe it's the wrong screen.
One moment.
Where is that?
No, no. Does he? No?
**Michele Mancioppi (Dash0 Inc.)** 09:00 I see the notes, yes.
**Denys Sedchenko** 09:02 Okay, so… We got the copper build, So, I ported… the new… The new implementation to copper, I had to tweak some stuff.
But the repo is here. I would like to test, like, see if someone can help, like, test and check how it's going.
**Michele Mancioppi (Dash0 Inc.)** 09:27 Okay?
**Denys Sedchenko** 09:28 So, we have builds… For… for distributions.
Including Fedora, I stumbled upon some problems, it was harder than last time.
So first of all, we are, so, like, our packaging is downloading, the… like, the Python modules for Python 3.11, but, for example, Fedora ships Python version 3.14, for example. So, like, if you have a global site packages, and using, like, the… system-provided global Python, You might have, like, might have some problems.
Also,
**Michele Mancioppi (Dash0 Inc.)** 10:19 Really?
**Denys Sedchenko** 10:19 Regarding Node.js, we have some files that are shipping Node.js shebang prefix.
Like, Ipell ships very old, ancient Note 16, but our agent depends on at least Node 18.
This also needs to be considered.
a plus… Because of NRPM package that we use in our Go tooling.
We are depending on goal 126.
Which is, like, set in our go mode.
And, for example, Fedora might ship GO125, and, like, if you will try to…
**Antoine Toulme (Splunk Inc.)** 11:01 Like…
**Denys Sedchenko** 11:02 build it.
without internet, it will not work because, say, like, sorry, like, your Go version is too old.
I had to enable internet on build, on builds.
But, and also, I had to introduce one worker, one… workaround, so, like, Fedora, by default, disables automatic Go, go tool chain downloads. I had to re-enable it back. Basically, Go has a feature that if it sees that package needs to be built with a newer Go version, it will automatically… Go automatically will download a new version.
So, changes are in my fork, which is basically here, and also, as a proof of concept, I attached the GitHub Actions integration. The job itself is dispatched manually right now, because I don't want to create the text to trigger it, but it's working.
Also, if you will check my branch… you might check this file. OpenTelemetry Packaging, Packaging Builder, OpenTelemetry Packaging Spec Template, which is a SRPM template.
for reviewing, I recommend you to take a look at that.
Also, as I mentioned previously, that, like, Excel ships old version of Node, or my, my, or, like, the version of Python might be old.
In order to prevent the generated package to, like, to specify Node.js or Python as a dependency.
I had to add a… this workaround.
And basically, like, saying that, like, it will be in recommends, but the package itself will not… will not have a hard dependency on it.
This is… this is basically it.
So, like, check the… check my fork, check the repo, copper repo, and also one interesting thing about, signatures, PGP signatures. I have a good news, Copra handled this for us. It automatically assigns the packages, it manages the key management, and also it automatically manages, key extension, like, if the key time, key expired time needs to be extended, it handles this for us. We don't need to think about that.
The only thing I needed to do, the only kind of secret we're going to need to manage.
is, API token for the… the copper repo, so in the workflows, I added copper build.
Also one thing, in the recent Ubuntu runner.
Ubuntu ships, by default, both Podman and, Docker, and Ubuntu had some problems, it's used the Podman by default.
So, in this build YAML, which existed before, I had to pull a workaround to basically use Docker, basically fix that problem.
**Antoine Toulme (Splunk Inc.)** 14:18 That's.
**Denys Sedchenko** 14:19 In Copper Build, workflow which contains, like, the trigger of copper build, this is the workflow.
The copper itself, under the hood, checks out the branch and runs and, like, do the build, so the only thing I need to do is just to basically trigger the build, and there is a secret.
with a copper config, which contains my username and my API token. That secret needs to be managed, maybe ideally we can move it to Vault or something like that.
Because, there were, like, incidents, like, where people were able to steal your secrets.
By, like, triggering some jobs.
**Michele Mancioppi (Dash0 Inc.)** 14:59 Interesting.
**Denys Sedchenko** 15:00 So… So… that's all on my site.
**Michele Mancioppi (Dash0 Inc.)** 15:04 The, so in Copper, the, is the build running inside, Docker on the, on the machine, or not?
**Denys Sedchenko** 15:13 I'm not sure about, whether I'm using containers or VMs, but for us, it's basically, like, a dedicated environment. When I, like, created, Project.
I… in the settings, I'm… so basically… oh, yeah, basically it's like a container, it's called Siege Root.
I select what kind of environments I want to run my builds and build for. Also, I can automatically add an option to automatically add new Fedora versions as a new Fedora versions.
Come?
So yeah, they're running in selected environments.
**Michele Mancioppi (Dash0 Inc.)** 15:57 That means… that… So that… would it be possible to put the build process inside copper.
on top of a Docker container we control, so that we don't need to do workarounds left and right for Go version, Python version, Node version.
**Denys Sedchenko** 16:19 Hmm…
**Michele Mancioppi (Dash0 Inc.)** 16:21 Because that is going to be a maintainability headache, if I've ever seen one.
**Denys Sedchenko** 16:26 I'm not sure if you'll be able to utilize Docker, it basically uses, like, it's not like a container is basically, like, an actual distro inside.
And it uses the actual distro toolchain to build your package.
**Michele Mancioppi (Dash0 Inc.)** 16:41 I see.
**Denys Sedchenko** 16:47 But, like, in your build instructions, you can, like.
probably you can, like, if you need to build some dependency, for example, I need to run our Go tool in order, like, to build a project inside, like, our GoTool, we can… we might need… we might call other tools.
To build a project by the… but the package, like, the packages that are available during the build process to install are limited to what distribution you're running.
In your SIG route.
**Michele Mancioppi (Dash0 Inc.)** 17:19 About you enabling internet, I mean, you need to do it anyhow to download the Java agent, the injector.
**Denys Sedchenko** 17:26 Yeah, yeah, builds cannot be Hermetic.
There's, like, a dedicated option to do that.
Which is enable internet access. This is not a problem for us.
But if we will decide to upstream this to actual, like, Fedora repos.
The requirements there can be stricter.
And they might require hermetic builds.
For now, it's not a problem for us, because we are managing the repo itself.
**Michele Mancioppi (Dash0 Inc.)** 17:56 And, this one is triggered… So the, you need…
**Denys Sedchenko** 18:06 Right now, I basically trigger it manually in GitHub workflow, so it's like a workflow dispatch here.
This can be replaced to triggered when you create a tag, or whatever you want.
It basically, under the hood, uses Copper CLI, which is, like, yeah.
**Michele Mancioppi (Dash0 Inc.)** 18:23 I see now, line 65.
Yes.
Yeah, it makes sense. Okay, so effectively copper goes, clones our repository, and then builds from there.
**Denys Sedchenko** 18:35 Correct.
**Michele Mancioppi (Dash0 Inc.)** 18:36 Alright.
Can you start upstreaming the fixes in PRs?
to the… To the, to the repo?
The… the changes you need to do.
**Denys Sedchenko** 18:51 It's a fork, so you can make a PR, you can take a look and review.
**Michele Mancioppi (Dash0 Inc.)** 18:55 Yeah.
**Denys Sedchenko** 18:58 Maybe I can do that right… no… Moment, contribute, open, request… I will make a draft PR for now… I'll show you.
**Michele Mancioppi (Dash0 Inc.)** 19:21 So this would give us a path to… effectively.
published on copper and point something like, packages.opentelemetry.io slash RPM.
To the cop proposal.
**Denys Sedchenko** 19:39 Yeah, it's possible.
**Michele Mancioppi (Dash0 Inc.)** 19:44 And there, the only thing we need to do is to put a proxy in front.
**Denys Sedchenko** 19:49 One moment.
I'm not sure how it's going to work.
With, like, a proxy.
Because right now, if I need to enable the copper-specific repo, I'm using a special subcommand, like DNF copper enable.
And it, like, knows under the hood.
how to, like, find this copper repo and how to use it.
**Michele Mancioppi (Dash0 Inc.)** 20:11 I see.
Can you look into if that has a special source except of just knowing how to build a URL?
**Denys Sedchenko** 20:21 Sure, yeah, I will do that.
**Michele Mancioppi (Dash0 Inc.)** 20:23 There is, there is, of course, the equivalent for YAM and ENF to just add the repo.
And, I would like to know if, We can use a copper repo, like, if it were… Any other? You have a record?
Interesting. Okay.
Cool. Good job.
**Antoine Toulme (Splunk Inc.)** 20:51 Yep, that's pretty cool.
**Michele Mancioppi (Dash0 Inc.)** 20:52 So… What type of risks do we… would we run into by adopting copper as the place to store our RPM packages?
**Denys Sedchenko** 21:09 I mean… Mmm.
**Antoine Toulme (Splunk Inc.)** 21:11 They can get hacked.
**Michele Mancioppi (Dash0 Inc.)** 21:14 Can Fedora yank it from under our backsides? Yes, right?
Are they likely to?
Probably not, I would like to say.
**Antoine Toulme (Splunk Inc.)** 21:25 No, it's not the play.
**Denys Sedchenko** 21:28 Regarding infrastructure, it's sponsored by AWS and IBM as well, so they have actually a pretty fast infra, even my builds.
On, copper. We're running much, much faster.
Then, what's the name of it?
than the previous service I was mentioning.
**Michele Mancioppi (Dash0 Inc.)** 21:55 OBS.
**Denys Sedchenko** 21:56 OBS, yeah, like, with OBS, like, even page load times took quite a long time.
But with copper, like, everything is faster, and the tooling feels much more mature.
**Michele Mancioppi (Dash0 Inc.)** 22:10 And, can people use, copper positives from, But what are the names of the, so from RAL? Can they use it from RAL?
**Denys Sedchenko** 22:22 I assume yes, because it's, like, just a DNF subcommand.
**Antoine Toulme (Splunk Inc.)** 22:34 So…
**Denys Sedchenko** 22:36 And, so, like, if you take a look at the repo.
on the main page, there's, like, build section. Besides Fedora, there is an EPAL repo. EPAL repo is extra packages for Enterprise Linux.
So it's for… it's head enterprise Linux. So I assume, yeah.
**Michele Mancioppi (Dash0 Inc.)** 22:57 Yeah, that's a good assumption, yeah.
And now, if we only knew whether LaunchPod works, Then, we would, Have a path by publishing, building it in both for the two different families of distress?
**Antoine Toulme (Splunk Inc.)** 23:14 Yep.
That would be good enough.
**Michele Mancioppi (Dash0 Inc.)** 23:17 That would be a start.
**Antoine Toulme (Splunk Inc.)** 23:19 I like what you said about having the proxy in the front, though.
I think… I think we need to continue to hold that, because that's gonna be our key.
in… We could have some level of telemetry as well, to understand how people are downloading, what patterns are we seeing.
Is there, are there any stats from Copper?
I mean, that might be.
That might be a good way also to see.
How people are using it.
**Denys Sedchenko** 23:45 You can upvote or don't vote the package on the main page, but… I…
**Antoine Toulme (Splunk Inc.)** 23:56 And, you know…
**Denys Sedchenko** 23:56 No, I don't see.
I didn't see any visit stats.
**Antoine Toulme (Splunk Inc.)** 24:01 Okay, no worries. So… Yeah, there's some stats, but it's at the whole… They must be collecting some stats, of course. It's just not super… it's just, like, local… the whole copper service.
**Denys Sedchenko** 24:22 from what I see, like, available to me, I see nothing. Like, I only see, like, build statistics, but real statistics, I don't see.
**Michele Mancioppi (Dash0 Inc.)** 24:33 And,
**Antoine Toulme (Splunk Inc.)** 24:34 Good.
**Michele Mancioppi (Dash0 Inc.)** 24:35 Of course, there is no… copper cannot build a DEB.
**Denys Sedchenko** 24:40 Oh, no, wait, wait.
It's, like, their UI is also… but… Inactive releases.
I can see the number of downloads.
**Antoine Toulme (Splunk Inc.)** 24:50 Well, I'll take it. I can show you.
**Denys Sedchenko** 24:52 We can show you if you want.
**Antoine Toulme (Splunk Inc.)** 24:54 Okay.
**Denys Sedchenko** 24:55 It's, like, hidden, not where we…
**Antoine Toulme (Splunk Inc.)** 24:58 That is amazing.
Actual downloads.
Oh, that's cool.
**Denys Sedchenko** 25:04 Yeah.
This… this thing.
**Antoine Toulme (Splunk Inc.)** 25:07 Okay, so this is more, like, for end users who'd be interested to find out if this stuff is popular?
**Denys Sedchenko** 25:12 Yeah, like, people could vote here.
**Antoine Toulme (Splunk Inc.)** 25:15 That's fine.
Okay.
I feel that's good enough, like, we could live with that for a little while. If there is no other options, we can always just put a tracker on the stats of the proxy to see what paths are being triggered.
**Michele Mancioppi (Dash0 Inc.)** 25:32 We're using some observability tool across web telemetry, right?
If I go and look at, at the source of the website, I will see the, AJS SDK, right?
**Antoine Toulme (Splunk Inc.)** 25:46 Good question. I think so, but do we put any of those results anywhere?
**Michele Mancioppi (Dash0 Inc.)** 25:52 I dearly hope we will.
**Antoine Toulme (Splunk Inc.)** 25:55 I am not the guy, I don't know. Magic.
Mmm… Where's it going?
**Michele Mancioppi (Dash0 Inc.)** 26:17 Yeah, I'm not sure we're using the browser SDK on the OpenTrantry website.
**Antoine Toulme (Splunk Inc.)** 26:24 He tries to go to send something to hotelwebtelemetry.com slash V1 slash traces, And he gets to 400.
Maybe it's a discussion for another people. We can ask the committee people.
Interesting to find out about that dot-com site.
Let me see… is it discussed anywhere? Anyway, it's pretty cool. We should… we should try that, and see where it goes.
**Michele Mancioppi (Dash0 Inc.)** 26:53 There is, there is a few things. In order to try this, there is a few things we need to do. First is to validate whether we can set packages.opentry.io slash rpm, and have it redirected to copper. I'm not worried about the fact that DNF or YAM can cope with that. I'm more worried about whether the way we host the website allows us to do that.
Because, ultimately, that retaract.
Could be.
Either… yes?
**Denys Sedchenko** 27:25 Prerequisite. Before actually doing any kind of, forwarding, we need to check, like, something should exist that needs to be forwarded, so, like, we would need an official, OpenTelemetry account on Fedora Copper, and, like.
**Michele Mancioppi (Dash0 Inc.)** 27:39 Yeah, yeah, but that is, that is… that is paperwork. That doesn't worry me. It's, the technical feasibility of, forwarding that benefactory managing the, Just a second… People just start huddling me without checking the camera.
So, the, The technical feasibility of the proxying doesn't worry me.
We, we can have our own, I assume we can have our own certificate.
No, I'll take it back, it worries me.
Antoine, who's the person that deals with the web infrastructure of OTO?
**Antoine Toulme (Splunk Inc.)** 28:30 Lustin Bucker.
I'm actually looking at this, and between Severin Newman and Austin Parker, you got probably most of the brain trust.
I'm a little worried about that, because I'm looking at what they have done for pentometryweb.com, and it seems like it's using Honeycomb?
**Michele Mancioppi (Dash0 Inc.)** 28:51 That does not surprise me in the list.
**Antoine Toulme (Splunk Inc.)** 28:55 Yeah, I mean, you would, right, you would want that. It's a public dashboard, actually, but the dashboard shows… Weird data, I don't know what to make of it.
Anyway, yeah, I think, Austin Parker, Severn Newman, Trask, to some extent, will probably know where the bodies are buried. These are the people who've been most responsible for some of those… you know, end goals. We could just, if we have a way to just run a proxy, and… Is there not, like, an AWS service we could use for that?
Of course.
**Michele Mancioppi (Dash0 Inc.)** 29:31 We could do water…
**Denys Sedchenko** 29:32 I have a fallback.
In case… Like, in… just in case there is no… let's assume there is no way to proxy that. Let's assume that copper is… an exotic thing in its own. We still have a Plan B, like, Copper generates all of the package metadata, the repository metadata.
It can be then, mirrored, re-uploaded to, like.
S3 or R2 bucket to blow up storage.
**Michele Mancioppi (Dash0 Inc.)** 30:08 Yes.
**Denys Sedchenko** 30:08 So we will still get our own managed URL in both cases. So it's available, like, it's achievable in both cases. I will just check whether I can use prox directly, proxy directly, or I will play With, mirroring stuff.
We discussed, actually, like, possibility of using blob storage in the previous call, so yeah, this is in the plan as well.
**Michele Mancioppi (Dash0 Inc.)** 30:31 Yeah, it's more like the one thing that I don't think we can replace with copper is the ownership of the key, right?
The moment, for some reason, we don't want to any longer build on copper, or copper kicks us out.
That's a breaking change for users, because their configurations for YAM and RPM are going to expect a certain key that we can no longer use.
**Denys Sedchenko** 30:56 True.
**Antoine Toulme (Splunk Inc.)** 31:00 We have to go to our next meeting, so… sorry.
This is great. Denys, can you please open the PRs? Let's see. Let's get this and this right out.
**Denys Sedchenko** 31:09 Actually, I published, like, the link to the draft into Hotel Packaging channel.
So you can check and take a look.
**Antoine Toulme (Splunk Inc.)** 31:17 Thanks. Yeah.
**Denys Sedchenko** 31:19 It's a draft, because it's, like, just a dump of my work.
**Michele Mancioppi (Dash0 Inc.)** 31:25 Alright.
Cool. Then, next week, we'll, talk more about… actually, Antoine.
please go and talk to, to Severin, or to Austin about, the,
**Antoine Toulme (Splunk Inc.)** 31:38 Okay.
**Michele Mancioppi (Dash0 Inc.)** 31:39 the proxy.
**Antoine Toulme (Splunk Inc.)** 31:41 Just make it real.
**Michele Mancioppi (Dash0 Inc.)** 31:42 Look at…
**Antoine Toulme (Splunk Inc.)** 31:43 Thank you.
**Michele Mancioppi (Dash0 Inc.)** 31:43 Alright, thank you, Denise. Bye.
**Denys Sedchenko** 31:45 Have a good day.
