SIG: Packaging SIG
Date: 2026-11-19
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Diego Hurtado (Dash0)** 03:36 Hey, Denise.
It's go on.
**Denys Sedchenko** 03:40 Hi, how are you?
**Diego Hurtado (Dash0)** 03:42 Wait.
What's everybody else?
**Denys Sedchenko** 03:54 I don't know. Michele should be available, because he responded me today.
**Diego Hurtado (Dash0)** 04:01 Yeah.
Should be joining us on this.
Ta-do Where are you at, KubeCon?
**Denys Sedchenko** 04:12 No, I wasn't.
Fortunately.
You?
**Diego Hurtado (Dash0)** 04:19 Oh, no.
Stay home.
**Denys Sedchenko** 04:45 Mmm… What's agenda? Let's fill the agenda.
In case anyone joins… I have a question regarding Python instrumentation.
Are there any plans to support Python 3.9.
**Diego Hurtado (Dash0)** 05:30 Nine.
Nope.
I don't think, but, okay, so… In the Python SIG, If I remember correctly, we have this policy of dropping support for all the versions of Python.
And, to add support for new versions of Python. So, we have been doing that for years, as far as I know, and 3.10 is the… oldest, we support, but, but I don't know, maybe I can talk to them. What do you need, Denise?
**Denys Sedchenko** 06:06 So… Yeah, so basically… like, there are the cases where, like, people bring their own versions of Python with UV or whatever.
But if people are using the system Python, And they're using some… Red Hat Enterprise Linux 9.
Which is still supported.
The system version of Python is 3.9 there.
Right. So, basically… They are going to install our out-instrumentation, but it's going to have zero effect.
**Michele Mancioppi (Dash0 Inc.)** 06:48 And this is exactly what I want.
end users to go and scream at the language SIGs, because, quite frankly, the policies for support of SIGs like Python, like .NET, are shit.
**Diego Hurtado (Dash0)** 07:05 Right, Michele, just to keep in mind that the decision of dropping all the versions was taken years ago, I mean…
**Michele Mancioppi (Dash0 Inc.)** 07:12 Oh.
**Diego Hurtado (Dash0)** 07:13 24…
**Michele Mancioppi (Dash0 Inc.)** 07:14 It's completely unrealistic.
In relation with how people actually use something?
**Diego Hurtado (Dash0)** 07:21 Okay, alright, let me…
**Michele Mancioppi (Dash0 Inc.)** 07:24 I was thinking years ago, tells me nothing.
**Diego Hurtado (Dash0)** 07:27 No, what I'm trying to say is that it was years ago before… Packaging or anything.
**Michele Mancioppi (Dash0 Inc.)** 07:33 individuals, I even understand why the current maintainers would like to keep it like that, because it's an awful lot of work, and it's very long CI times to actually test across a bunch of different things, and you cannot play with the new toys, like F-strings and stuff like that.
I guess.
**Diego Hurtado (Dash0)** 07:49 Not only that, I think I remember years ago, we had this awful problem, because one of our dependencies was, import lib, and We had to make… like, really… Crazy things to support.
What we needed to… to use in PortLib, because there were, like, some breaking changes in this library, so we had to do, like, weird stuff for 3.9, and less weird stuff for 3.10, and some other weird stuff for.
**Michele Mancioppi (Dash0 Inc.)** 08:27 And now you know that the problem was actually having non-vendor dependencies.
**Diego Hurtado (Dash0)** 08:35 Import Lib is part of the standard library.
**Michele Mancioppi (Dash0 Inc.)** 08:39 Huh. Then… okay.
Madison.
**Diego Hurtado (Dash0)** 08:43 So, yeah, it is, I mean, it… There are situations where we… I mean, what I'm trying to say is that I don't think people… is dropping support for old versions, just because they want to mess somebody up?
**Michele Mancioppi (Dash0 Inc.)** 09:00 No, it's, it's not, it's not malicious, it's just, a trade-off.
That optimizes for the wrong people. We should not optimize for ourselves, should optimize for end users.
**Diego Hurtado (Dash0)** 09:13 Yeah, I mean, I guess that's the moral responsibility of the software library, right?
In any case, I can bring this topic to a Python SIG, let's revive 309.
Oh my god.
Just to imagine how the reaction they're gonna have, but…
**Michele Mancioppi (Dash0 Inc.)** 09:30 I haven't read that.
**Diego Hurtado (Dash0)** 09:33 for you guys. I'll do anything for you guys.
**Michele Mancioppi (Dash0 Inc.)** 09:35 I don't know. Have a Red Hat.
Come and say that.
**Diego Hurtado (Dash0)** 09:41 Well, I don't know.
**Michele Mancioppi (Dash0 Inc.)** 09:42 They're the ones shipping 3.9, right?
**Diego Hurtado (Dash0)** 09:45 Do you have a Red Hat number? I can call them and tell them.
**Michele Mancioppi (Dash0 Inc.)** 09:49 There is actually a PM for Packaging, for packages at TrattAs that should join us at some point.
Okay.
She could speak to that.
Buddite.
**Diego Hurtado (Dash0)** 10:02 Yeah.
Actually, something that is probably gonna come up during this, Python… Sorry, just a sec, please, I'm trying to put on my shirt.
So I don't…
**Michele Mancioppi (Dash0 Inc.)** 10:17 The… our version… Our versioning schema is something that we could backfill with older versions of Python.
For example, so the… our version of schema has the version of the upstream.
And we could say, hey, if you want to use Python 3.9, still package up to version X.
Now, unfortunately, I don't think there is a combination of, Python packages.
With declarative configuration that go far enough.
**Diego Hurtado (Dash0)** 10:49 Hmm.
**Michele Mancioppi (Dash0 Inc.)** 10:50 But in principle, we could, I mean, the packages do not disappear.
The moment the new one is released, we just need them to keep track of Documenting the packages, which version dropped, Support for which runtime?
**Diego Hurtado (Dash0)** 11:08 Huh.
**Michele Mancioppi (Dash0 Inc.)** 11:09 Which is actually something that, in some cases, we can put as constraints.
in the metadata of the packages, at least for the system runtimes, like Python.
**Diego Hurtado (Dash0)** 11:21 Okay, something else, I think if this situation with 309 is gonna push… Harder and harder.
for… this OpenTelemetry agent.
Solution that will fender pretty much everything.
And I think, because I think there's… there is this, inescapable conflict.
conflict between what us packaging slash injector need, right?
Which is, vendor dependencies, support for all Python versions, and so on.
And, the… I mean, the… The rest of the… the project, right? So we…
**Michele Mancioppi (Dash0 Inc.)** 12:20 I don't believe so. We make that tension more visible, but end users are having a hard time upgrading hotel libraries all the time.
**Diego Hurtado (Dash0)** 12:31 That's true. The, admit, what I'm… Let me, let me… how do I say this?
Okay, what I'm trying to say is that there is an immediate need now.
because of this… the existence of this project, right? There is an immediate, hard, need… To get a solution soon.
And I think, people are gonna turn towards… the old OpenTelemetry Python agent thing.
Because it allows them to separate Things, and… and just give us… Something that works now, without Kinda affecting everything else in the project?
So, I'm just forecasting, like, doing this mental experiment, that I think, this, this new need that we have for support for all Python versions is gonna… push forward.
Towards this solution.
**Michele Mancioppi (Dash0 Inc.)** 13:48 Boom.
**Diego Hurtado (Dash0)** 13:49 If it works, it works, I mean, it's gonna be great, right?
**Michele Mancioppi (Dash0 Inc.)** 13:51 Hi, India!
Let's see. I mean, yesterday, ideally, my PR for the, the PR versus Jack helped a lot.
For the specification with the requirements for injectable.
As the case should have been merged, so at least that was the idea.
And it was… So now, we have a language in the specifications about what a library So, agents should do.
**Diego Hurtado (Dash0)** 14:23 Good.
**Michele Mancioppi (Dash0 Inc.)** 14:26 Which we can use, to help with these discussions.
**Diego Hurtado (Dash0)** 14:31 Oh, by the way, the Python SIG is happening in less than 2 hours, so… Better.
**Michele Mancioppi (Dash0 Inc.)** 14:39 Yeah, be gentle.
**Diego Hurtado (Dash0)** 14:42 I'm always gentle.
**Michele Mancioppi (Dash0 Inc.)** 14:45 Agent.
Let's look at the open PRs. Do you need help in finding where in the specification we have the new language, or…
**Diego Hurtado (Dash0)** 14:56 For what?
**Michele Mancioppi (Dash0 Inc.)** 14:57 Do you need help to find the new language about injection?
In… the specification.
**Diego Hurtado (Dash0)** 15:07 No, I, I read that PR, I know what you're talking about.
**Michele Mancioppi (Dash0 Inc.)** 15:12 Yeah.
But you can use it as a sledgehammer.
**Diego Hurtado (Dash0)** 15:15 Oh.
You just said you wanted me to be gentle. I mean, how heavy is that metaphorical sledgehammer?
**Michele Mancioppi (Dash0 Inc.)** 15:22 It's a metaphorical switch summer, of course.
**Diego Hurtado (Dash0)** 15:25 Yeah, I know, I just want to know how heavy it is.
**Michele Mancioppi (Dash0 Inc.)** 15:29 I don't know, maybe start with the one that's made of plastic that clowns use in the circle.
**Diego Hurtado (Dash0)** 15:34 The one that makes a sound when you hit someone.
**Michele Mancioppi (Dash0 Inc.)** 15:38 It's… it's a park.
**Diego Hurtado (Dash0)** 15:40 Alright.
**Michele Mancioppi (Dash0 Inc.)** 15:41 Let's look at the open PRs, because we have way too many for my taste.
Thanks, Denise. I merged, too, as we were talking. You would have been thinking I was merging.
Excellent.
**Denys Sedchenko** 15:54 Can you please merge wine as well?
**Michele Mancioppi (Dash0 Inc.)** 15:57 Which one do you want?
**Denys Sedchenko** 15:58 The first one.
**Michele Mancioppi (Dash0 Inc.)** 16:01 I'm terrific.
Now, let me review it. I will actually review it.
**Denys Sedchenko** 16:09 Ricky.
**Michele Mancioppi (Dash0 Inc.)** 16:11 So this one, I'll assign to myself.
**Diego Hurtado (Dash0)** 16:15 Hmm.
**Michele Mancioppi (Dash0 Inc.)** 16:16 And I will even put the eyes here.
**Diego Hurtado (Dash0)** 16:20 Let's review something else here.
**Michele Mancioppi (Dash0 Inc.)** 16:22 Now, now it's official.
did you hear anything about, Netlify and,
**Denys Sedchenko** 16:37 No updates, nothing. As far as I understand, we just… We need someone from Cloudflare to actually give us access, but Cloudflare doesn't care about us at all.
**Michele Mancioppi (Dash0 Inc.)** 16:57 I think I might be very nasty on Twitter.
**Denys Sedchenko** 17:01 This is going to help if you're, like, influencer.
**Michele Mancioppi (Dash0 Inc.)** 17:05 No, I'm not. On Twitter, I have, like, 100 followers.
They have been nasty on LinkedIn, I don't know.
This one, this PR, keeps going back and forth.
I did some additional work, because some of the pieces broke stuff.
It's an unto one to have a look at it again.
So let me… Send it back to him.
**Denys Sedchenko** 17:42 I have a question. So, basically, after we fully moved to OBS, It will be the source of truth for the way we actually build the packages.
**Michele Mancioppi (Dash0 Inc.)** 17:52 Yep.
**Denys Sedchenko** 17:52 And after this happened, does it actually make any sense to keep any package-building infrastructure in our repo?
**Michele Mancioppi (Dash0 Inc.)** 18:04 Because…
**Denys Sedchenko** 18:04 like, what we're using in code to build DEP and RPM.
It's a totally different way from how we're actually, like, building the packages on OBS.
**Michele Mancioppi (Dash0 Inc.)** 18:16 That's a good question.
I think that from the point of view of OpenTentra itself, the answer is no.
From the point of view, for example, at DeSero, we are building our own packaging infrastructure, like I'm sure you folks at Grafana are doing as well.
I don't know that Drastic is doing.
I don't know if… And we forked off, of course, from what the packaging did.
So I don't… I don't know.
**Denys Sedchenko** 18:46 I mean, like, you basically can just use the same thing that we use for OBS, Basically, like, the Packaging repo compiles this pack.
And you just feed the spec to that build or RPM build program, that's all.
So we can have just one source of truth.
**Michele Mancioppi (Dash0 Inc.)** 19:04 Let's say that if you open the PR for the deletion of all the stuff you don't need.
Then we can put it in the, in the channel and say, folks.
Let us know if you want to maintain the open for your own package, vendor package, otherwise it goes.
**Denys Sedchenko** 19:19 Okay.
**Michele Mancioppi (Dash0 Inc.)** 19:25 Let's have a look at this one, because I don't remember where it is.
**Denys Sedchenko** 19:30 Yeah, I pinged you there because, like, I remember you made a separate PR saying, like, hey, we don't update Ubuntu for a particular.
**Michele Mancioppi (Dash0 Inc.)** 19:41 Yeah, exactly.
And this is where we need to decide where we want to test on No, the run zone was not an issue. It was a test matrix.
The thing, right?
Because these are not running the tests.
This is just building it, so I have no problem with this.
the PR, like, when the PandaBot was actually updating the test metric, I was like, Oh, nope.
You add to a test metric, do not subtract it.
We don't do, like, those things that drop support for a version of the US, just because the new one is out, right?
**Diego Hurtado (Dash0)** 20:24 Sorry, Dirty, did you say something?
**Michele Mancioppi (Dash0 Inc.)** 20:27 I was being, cated.
Good.
This, I think, we don't need in OBS, right?
**Denys Sedchenko** 20:43 Yeah, yeah, that's actually why I raised the question, because, like, we have some PRs which update our goal.
Quote to compile packages, but we're not using it at all.
And for a context, people are still able to build their own packages without any problems, it's just like we just… Using a different tool.
**Michele Mancioppi (Dash0 Inc.)** 21:46 Yes.
This is still waiting on Ruby to add support, for, some of the configuration.
Some of the providers in the configuration.
Not sure. No punch.
**Denys Sedchenko** 22:32 I have a question, do we have a plan on adding a collector?
As well.
**Michele Mancioppi (Dash0 Inc.)** 22:37 We have a plan. I mean, we know that we want a plan, and people are asking us to have a plan.
We actually opened a new shoe.
On the, GitHub releases repository.
Hello.
And, it went, precisely and over.
Nobody's working on this.
**Denys Sedchenko** 23:26 Initiative beats the initiator.
**Michele Mancioppi (Dash0 Inc.)** 23:29 Huh?
**Denys Sedchenko** 23:30 like, there is, like, an old Soviet proverb saying, like, initiative bees the initiator, which actually means if you have initiative, you will be the only person who will be able to do it.
**Michele Mancioppi (Dash0 Inc.)** 23:41 Yeah, but it's conference season, I'm very, very busy, so… That's why this has not happened.
So I also don't think we should do it until we actually have a bloody place where to put the packages, you know?
So… Let's do it after the first version.
**Denys Sedchenko** 24:00 Bing.
**Michele Mancioppi (Dash0 Inc.)** 24:01 The answer is yes.
But… Oh my god, infinite commits.
Touching 27 files.
**Denys Sedchenko** 24:23 Oh, you agree?
**Michele Mancioppi (Dash0 Inc.)** 24:25 Diego.
**Diego Hurtado (Dash0)** 24:29 Yes.
**Michele Mancioppi (Dash0 Inc.)** 24:32 Can you, please have a look at this PR at your earliest convenience?
And, see what the state is. I mean, it definitely needs to be rebased and fixed, so some, some conflicts.
**Diego Hurtado (Dash0)** 24:45 161.
We'll open that.
**Michele Mancioppi (Dash0 Inc.)** 24:49 Who's that?
**Diego Hurtado (Dash0)** 24:51 bye.
**Michele Mancioppi (Dash0 Inc.)** 24:53 That bloody guy.
**Diego Hurtado (Dash0)** 24:55 Alright, I'll take a look.
**Michele Mancioppi (Dash0 Inc.)** 25:02 That bloody guy, I can… This one, this is a discussion for the TC, but, like, with the collector packages, Zero bandwidth.
**Denys Sedchenko** 25:15 The question is, are we actually the people responsible to… like… we should just deliver this BOM, or we have to generate this BOM, because usually the task of generating this BOM is on package builders, like on someone who creates the product, like the collector maintainers, not us.
**Michele Mancioppi (Dash0 Inc.)** 25:33 I agree.
I absolutely agree. The, So, if we decide we want to do it.
And we decide which one we want.
which are the formats we want, because I am still stuck on which of the formats makes sense.
Then, it makes sense to see how much we can do, and how much is coming from upstream, right?
**Denys Sedchenko** 26:03 Yeah, because usually, like, upstream… like, usually upstream is going to generate as a BOM and usually publish it to some kind of third-party service, so, like, it's available for everyone else. And if that's actually done.
Considering that, like, most of the packages we're building, they're basically, like, Like, they self-containable, let's say so.
So, if that's actually done on a maintainer's side, I don't know what actually have to be done on our side, because we're basically just taking Whatever style they built, and just package it and provide it.
**Michele Mancioppi (Dash0 Inc.)** 26:40 entirely correct.
we, for example, if we did the SBOM for, the, Python, Package.
We will put in their stuff, attach the SIP.
Because we don't ship CRPC.
Pride ownership.
So I…
**Denys Sedchenko** 26:58 In that case, true. Yeah, in that case, we have to publish as well as well.
**Michele Mancioppi (Dash0 Inc.)** 27:05 In reality, the fact that we know what we're going to put in the packages.
us doing the SBOM will not be a problem.
I think.
It's more like, which format do we want, and do we actually want to do it? Is it worth doing? Because on that part, I'm not sure.
I mean, I mean…
**Diego Hurtado (Dash0)** 27:31 do both.
**Michele Mancioppi (Dash0 Inc.)** 27:33 Or we can do neither until somebody really says they need it.
the fact that no OpenTentra SDK that I know of Has an S-bomb.
his signal.
**Denys Sedchenko** 27:53 Let's wait until the Zero gets some enterprise customer who is very noisy about security and is going to poke you, Michele directly.
With a knife and say, give me S-bones.
**Michele Mancioppi (Dash0 Inc.)** 28:06 Or Grafana.
the fact that, I mean, you folks have a lot of customers, and apparently they're not screaming for this, right?
**Denys Sedchenko** 28:16 They start to scream.
**Michele Mancioppi (Dash0 Inc.)** 28:18 Oh, they start to scream, excellent, then I'm looking forward to your peers.
**Diego Hurtado (Dash0)** 28:23 Hey, Michele, what about we… buy some Grafana products and demand S-bombs from them.
**Michele Mancioppi (Dash0 Inc.)** 28:32 I don't know, I don't trust those Brafana guys.
**Diego Hurtado (Dash0)** 28:42 Or maybe we can do the same with Dash Zero. Can we be Dash Zero customers, too?
**Denys Sedchenko** 28:48 Why not? By the way, in addition to SBO, We also have to think about facts.
Which is basically, like, you have Google Check JSON file where you, like, describe, hey, this doesn't affect us, but fax is, like, a standard.
For that kind of thing.
**Michele Mancioppi (Dash0 Inc.)** 29:07 I don't even know how to send it. Can you put a link in the chat?
**Diego Hurtado (Dash0)** 29:15 Hey, guys.
So, Cloud just finished, and… Right. Just… Just to let you know.
The Python 3.9 thing… is… is what I suspected.
It is the… it was, I mean, dropping 3.9, gonna… relieved Python of a huge problem that had been running for years.
And I… And this was so… it was the kind of issue that you remember years afterwards, because I remember it, yeah. So, I'll do it. I'll do it. Don't… I just hope that they are gentle with me.
**Michele Mancioppi (Dash0 Inc.)** 30:13 Denise, you know what waxing means in English?
**Denys Sedchenko** 30:18 Oh, sorry.
**Michele Mancioppi (Dash0 Inc.)** 30:19 I see.
This is very vexing. I find the name of the format excellent.
It is vexing.
**Diego Hurtado (Dash0)** 30:32 Vexing. What's vexing?
**Michele Mancioppi (Dash0 Inc.)** 30:34 Vaxxing, is the… it's a word in English to… to speak of something that is very annoying. Like, for example, the flickering of the red punching bag behind you is waxing mirror now, Diego.
**Diego Hurtado (Dash0)** 30:47 Yeah, yeah, sorry about that.
**Michele Mancioppi (Dash0 Inc.)** 30:50 There are also magic cards with that. The Vex, the Vexing Arcana.
It was an artifact that would mill your deck, and I loved playing it, and now this is waxing me.
Alright.
**Diego Hurtado (Dash0)** 31:05 3… the 309 thing?
**Michele Mancioppi (Dash0 Inc.)** 31:07 No, the, the… having yet another security-related format.
To support them.
**Diego Hurtado (Dash0)** 31:12 Okay.
**Michele Mancioppi (Dash0 Inc.)** 31:13 Very vexing.
All right. Well, I'm looking forward for somebody to scream and put in some work.
Cold.
Alright, that's all the time we have.
I'll see some of you in the injector call.
**Diego Hurtado (Dash0)** 31:33 I…
