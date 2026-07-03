SIG: Packaging SIG
Date: 2026-07-02
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Diego Hurtado Pimentel** 09:36 Hello, Michaela.
**Michele Mancioppi** 09:41 Hello!
**Diego Hurtado Pimentel** 09:42 How is it going.
**Michele Mancioppi** 09:45 Mmm.
I eat a… I eat a blocker.
I hate the black one.
**Diego Hurtado Pimentel** 09:57 Sorry, I need to, connect my… Yeah, it's good.
Here are you now, huh? Hey, hello, how's it going?
**Michele Mancioppi** 10:12 I hit a blocker with the packaging.
And it's… It's about declarative configuration.
So, the, the status is the following.
We have a POC.
in, this branch that I'm working on.
You see in the chat.
The part that, I am not managing To make work yet is a good setup for declarative configuration.
Because the injector… They're not.
Does not know which language it injects.
So it conjects all of them.
And therefore, I cannot set different values for the declarative config file environment variable based on different languages.
Which means that you really need to lean hard on the one configuration file, In the entire system package.
Allowing for overrides done manually by the users.
through, setting environment variables in their system DUnit files.
And the problem with that is that the support for the Experiment for the language-specific overrides in instrumentation configurations.
are currently supported only in Java, with Python on the way.
And that is not a great situation.
**atoulme** 12:08 Good morning.
**Michele Mancioppi** 12:10 I am.
**atoulme** 12:16 So we're stuck on configs.
**Michele Mancioppi** 12:21 I think so.
I think we don't have yet, I mean, the state of the declarative config?
It does not, yet mix well with the limitation in the injector, not to know which language it injects.
Either of the two has to give.
**Bastian Krol** 12:44 Isaiah, just, just… Maybe it's clear for everyone else, maybe just to remind me, is there a specific reason we are tying declarative config with the packaging efforts, we could do this into separate iterations, could we go with a different environment variables?
In the first packaging, Thanks.
**Michele Mancioppi** 13:13 Is that, setting… So… System packaging, it's supposed to work out of the box, right?
And, packaging where you need to go and set environment variables for your processes.
editing your SystemD units or setup scripts, it's not usable.
Like, most of the processes we would inject, they would have nothing to talk to.
**Bastian Krol** 13:43 Right, we… what do you mean, nothing to talk to? You mean the collector endpoint, and…
**Michele Mancioppi** 13:49 The collector is not installed by the system packaging. At some parts of the system yet. So, all the public inject are going to try to talk on local host.
And then the board deport.
**Bastian Krol** 13:59 Right, but OTLP exporter endpoint is supported across all languages.
**Michele Mancioppi** 14:04 Yes.
**Bastian Krol** 14:05 So, that's what I'm trying to get at. UCAT, and also the injectors mechanism for language-specific… Environment variable, or not in languages, but the environment variable overrides.
**Michele Mancioppi** 14:23 So what you're saying is, we could skip the decorative config for now, and just give the flat file that you use for environment variables in the injector, and tell people to configure through that.
**Bastian Krol** 14:36 Yeah, I'm not saying that's the best way forward, but what you described, it sounds to me like it's… The two, declarative config and packaging currently don't go together, and…
**Michele Mancioppi** 14:51 Unfortunately not.
**Bastian Krol** 14:52 Yeah, so I'm just thinking, what could we do in the meantime to… to get something.
It's not ideal, because that's not the standard format that we want to land on, ultimately. That's really ugly.
I, I get that.
**Michele Mancioppi** 15:18 But it's what we have, right?
It's also not something we can make backwards compatible, because the moment That would tell people to, configure through those environment variables.
The version of the packaging that starts relying on declarative configs, the declarative configurations will ignore the environment-based ones.
**Bastian Krol** 15:39 Yeah, and we will need to keep that mechanism forever if we now… Have people use it,
**Michele Mancioppi** 15:48 I mean, purely technically, purely technically.
I believe it would be feasible in a post-installation script to migrate From the flat file to padded configs.
**Bastian Krol** 16:02 Woof.
Okay, that sounds like something we might not want to do.
**Michele Mancioppi** 16:11 I mean, purely technically, I could imagine a very painful way To make this, feature-proof.
Yeah.
**Bastian Krol** 16:20 I mean, the gist of it is declarative config is not ready for prime time, because there's no… so, one… The supported this foils is lacking in a couple of languages anyway.
And two, it's its specific configuration files per language.
**Michele Mancioppi** 16:40 And the injector that cannot tell languages apart when it injects.
Because if the injector could, we could resurrect the idea of having the language.
**Bastian Krol** 16:50 Oh my god.
**Michele Mancioppi** 16:51 file.
**Bastian Krol** 16:52 But I really… I mean, we discussed that a couple of times, it would be handy for a couple of reasons, but I think we… deliberately designed it to not do that, because the only ways to do that would be holistically, and that's always shit. Like, you can take a look at, executable names and magic headers and all that jazz.
**Michele Mancioppi** 17:16 We could do elf symbols, but still…
**Bastian Krol** 17:19 Yeah, right, I mean, there are… but it's always… not error-proof. Never.
**Michele Mancioppi** 17:26 It's… no, and I got scared the moment I saw the variability of ELF symbols across different node builds.
That's gonna be a game of whack-a-mole forever.
**Bastian Krol** 17:38 Yeah, yeah.
**atoulme** 17:39 Okay.
**Bastian Krol** 17:39 Don't do that.
**Michele Mancioppi** 17:42 To be perfectly honest, the idea of going with a single configuration file.
is the one that I prefer.
Because that makes also stuff for OPAMP.
more understandable, and it prevents the user having to edit, well, the resource detector, 5 different files the same way.
But, then, we need help in getting those, config, Decorative support, done.
**atoulme** 18:11 Okay.
So, I like that idea, too. I think this is… from a user experience, having 5 different 6 config files is difficult. At least, I mean, still life can make it composable, too, by the way, but that's a different discussion.
**Michele Mancioppi** 18:26 So… So…
**atoulme** 18:28 What do we need to do?
**Michele Mancioppi** 18:30 good that you're here, Antoine, because the one that is going to be difficult to fix Here's .NET.
**atoulme** 18:37 Okay.
**Michele Mancioppi** 18:39 So, for Python, Diego is, is… there is, Mike from Honeycomb is working on the clarity configurations. Digo will, will support and also make sure that the Experimental option for… Language-specific settings for instrumentation is supported.
Jobball is fine.
Oh, Jess, we can have Matt work on that. Matt, where?
But, other cities, we do not have contributors for tonight.
That's fantastic.
**atoulme** 19:18 So… So, on that one, I have a couple people who work with me. Pyotr is one of them, we can trust that. Paulo Giannotti, also, he's a former maintainer for .NET. So, if we need something done quickly on that, we can push on that pedal.
**Michele Mancioppi** 19:34 It's not going to be quick, I mean.NET needs to… so I attended, a couple of weeks ago, a call in the autoinstrumentation.net.
**atoulme** 19:43 Okay.
**Michele Mancioppi** 19:44 I'm not in… I… Cannot say I understood what the status of the SIG is with respect to supporting the declarative configurations.
**atoulme** 19:53 I could ask.
Are we… did you open any show to them, by any chance, or is it earlier?
**Michele Mancioppi** 20:00 I went there, I asked, they said, oh, we support a file, but it's not exactly the right format.
And, if I recall correctly, Sam, we also don't think of, supporting the official format in the foreseeable future.
I hope my recollection is wrong.
**atoulme** 20:16 Yeah, sauce.
Sounds like a bad idea.
Okay, let me ask them.
**Michele Mancioppi** 20:23 Yes.
**atoulme** 20:31 So… I have a question related to dirtless config.
So, if we were to do that, let's say it takes, Let's say it takes 3 months.
Is that acceptable?
Do we ship with that.net? Meanwhile?
**Michele Mancioppi** 20:53 I would not ship without a net.
**atoulme** 20:55 Okay.
Do we…
**Michele Mancioppi** 21:02 But in that case, if it takes 3 months.
Then, maybe what we should do is to… is to ship, with the, AMP file first.
And then do the automatic migration.
**atoulme** 21:24 Okay, this is starting to impact.
**Michele Mancioppi** 21:27 I think it would be a massive missed opportunity to position the declarative configuration.
in the ecosystem.
**atoulme** 21:39 I think if we ship with off, we're gonna be resolved for 2 years.
Yeah.
That's not exactly ideal either, but maybe that's where we need to go. But at least it works.
**Michele Mancioppi** 21:54 I would really… I would really like the first release to have a… SQLite support for… declarative config, so this is the first where we say, oh, you should try, not the first pre-release.
So, latest, KubeCon.
**atoulme** 22:10 Yep, sounds good to me.
Okay, so I'm asking the question right now. I would get an answer today. I'll make sure to photo up. We… Is there any, any backlog on the… since you're… you were into that, have you looked at some of the backlog for .NET, or .NET authentication?
It's okay if you didn't, it's fine. I'm asking for myself.
**Michele Mancioppi** 22:36 Just like I'm writing down the, in the notes what to discuss.
I'm going to put it on the screen.
**atoulme** 22:44 Okay, so there is something in… Configuration SDK.
Okay, there's some interesting discussion.
**Bastian Krol** 23:02 By the way, that is under the wrong date, but… Never mind.
**atoulme** 23:16 Oh, that's what happened.
Let me fix that.
There's definitely work happening. Like, 2 weeks ago, they have a PR open now.
We're… What's blocking… About 2 days ago, purely for my team started to review.
It's been approved by one person.
It's big. It's 6,000 lines.
I mean, the good news is that someone's doing it.
So, I wouldn't say it's gonna take 3 months as much, maybe a month or two?
If this… This is Phase 1, so, I mean, I'm not sure yet to understand what Phase 2 looks like.
**Michele Mancioppi** 26:00 Yeah, but we're really going to need the, the instrumentation overrides.NET is infamous for having a lot of configuration options on their instrumentations that are actually useful.
**atoulme** 26:15 Steve Gordon is the person working on that. He works at Elastic.
Oh, I mean, it's, it doesn't appear that they're blocked, so they're not… Going to do it.
It's just that it's not something that it's going through.
That is so unreason.
Hmm.
**Michele Mancioppi** 26:54 I mean The last commit is from…
**atoulme** 27:02 For this poll request, it opened 2 weeks ago, and it's got a review as early as late as 2 days ago.
**Michele Mancioppi** 27:10 Okay.
**atoulme** 27:12 I would say it's selective, I'm… I don't know if this implements everything we want. There's no reason to think it would. As he said…
**Michele Mancioppi** 27:28 I, I… I quickly scanned the invitation, it doesn't have the… The bits about the, Experimental options, we need an experimental one.
The one… the language overwrites is experimental, because only one SDK has implemented it.
So, Jack could not fight the fight as, stable yet.
**atoulme** 27:53 Okay, I mean.
At least the… This needs to land before we move on to that discussion, right?
Is that right?
I can tell them.
Is there a particular… so you said, experimental? Where would that be? That would be in the declarative config, work?
**Michele Mancioppi** 28:12 I can… I can link you to the… to the one we need.
**atoulme** 28:15 Yeah, if you can, that would be helpful. Awesome, I can pass that around.
**Michele Mancioppi** 28:37 And it's inside Channel.
**atoulme** 28:44 Thank you.
Alright, so the Experimental General Instrumentation ref.
configuration applied multiple… Okay.
So, Michael, if I was able to unblock that, are we good?
**Michele Mancioppi** 29:52 Yeah, I think so.
I would also need more people to try the packages in their current status.
the, this shortcoming is something that, for example, I… Figured it out trying myself, but, too late.
It's, I've not yet reflected that on the specification.
somehow, I did not remember, I did not tell in my head that I needed different values for the auto-config file until I tried, and I was like, hmm… Excuse me.
**atoulme** 30:26 We need to dogfood this stuff a little bit.
**Michele Mancioppi** 30:28 Yep.
**atoulme** 30:30 Sounds good.
Yeah, and I mean, the PR already has an impressive amount of tests, from what I can tell, so is that something that we would want to iterate with additional tests in that case?
**Michele Mancioppi** 30:45 Yes.
**atoulme** 30:46 Okay.
**Michele Mancioppi** 30:47 I mean, right now, the PR is a fat rate. It's… it's bringing up the, some test applications, see if they get… look at the log, see if they get instrumented. I don't think… something that I was considering doing is to borrow the, OTLP sync approach we have in, an injector.
We're, I did not do it right away, because… kind of hoped we would start the discussions with the OpenTelemetry Collective SIG about bringing the packages together, but that is not… Has not happened yet.
So I'll probably set that up and just check if the entry exists.
**atoulme** 31:32 It sounds like you want to… I mean, it's more code to maintain, but it might be easier.
**Michele Mancioppi** 31:38 That's fine, I mean, at the end of the day, I also very happily came up with a setup that is mostly Go code, also to build the packages.
**atoulme** 31:48 Okay.
**Michele Mancioppi** 31:48 me happy.
**atoulme** 31:50 Yes.
**Michele Mancioppi** 31:51 Oh.
I think it would be liable.
**atoulme** 31:55 Okay, yeah, because the way, the way to go… I wouldn't look too much at how we make releases of the Collector. We're using something called Go Reader Pro, and it's got a lot of opinions bundled in that I'm… Don't really care for.
We should consume the Debian packages, the Debian RPMs from Collector, republish them.
**Michele Mancioppi** 32:17 I mean, the, the reason why I would not be able to integrate the collector today is because there is no interface defined.
And that, I mean, our packaging interface.
Right.
**atoulme** 32:31 the data.
Yeah.
**Michele Mancioppi** 32:32 Exactly, because effectively what, what I would need to do is to declare that the OpenTentry metapackage Depends on a OpenTeentry Collector 1.
**atoulme** 32:45 Yes.
**Michele Mancioppi** 32:45 Because the interface is master versioning, otherwise interface will suffer, and the collector packages do not specify that they satisfy.
**atoulme** 32:54 Yes, that's right, that's right. We need to make that first. You're right.
That is probably just a little tweak in the metadata of the packages before we publish them from the collector.
So, I…
**Michele Mancioppi** 33:07 I couldn't again.
So, the packaging for the collector, yeah, that would probably suffice.
The collector is not publishing to any APT repo.
So, screw it, and we import the existing ones.
**atoulme** 33:22 Yeah, you just have to download it from the release… release portal, like the GitHub release page, right?
**Michele Mancioppi** 33:29 Yeah, that's not civilized.
But we can, we could make it so that we, we have, we import them into our temporary repo.
on GitHub pages.
Which is not, is not published yet.
**atoulme** 33:45 That is fine. We could add… either we could add a step in the publishing of the packages to publish to this additional package repository, or we could have a script that scrapes the GitHub page to download the RPM I would have for you is, I'm a bit of a noob about, like, the way we are signing the current RPMs and Debian packages for the collector.
might be a bit naive compared to what you would want to do with GPD and whatnot in a.
**Michele Mancioppi** 34:15 I've used those packages before, they're fine.
**atoulme** 34:18 Okay, they're good, okay.
**Michele Mancioppi** 34:19 Here we go.
**atoulme** 34:20 We need to do… we could reuse those signatures, is what I'm asking.
If needed.
**Michele Mancioppi** 34:27 Huh.
Oh… well, today, for example, until we figure out how to publish those on repositories.
**atoulme** 34:38 Hmm.
**Michele Mancioppi** 34:38 APT and RPM needs to have the signature validation off.
So that is not an issue.
**atoulme** 34:45 Alright, alright, let's not do that yet, then. Okay, fair, yep.
**Michele Mancioppi** 34:48 Speaking of this, Sina, what can you tell us about Launchpad?
**atoulme** 34:53 Please.
**Sina** 34:55 Yeah, we've been working closely with one of the Ubuntu Archives to set up the PPAs and everything, and hopefully by, next, Thursday, I'll have, something that we can try out.
And, another thing I followed up on about was the CNAME question that you had on whether we could have CNAME records, and unfortunately the answer is no.
Not that it impedes the initial, work on, with the PPA at all.
So, myself and someone else from our team is, we've started working again today, we were… A little bit, distracted this past week.
So, by Tuesday or Wednesday, we'll have something up, so we can look at it on Thursday.
Any other… was that your question about LunchPad?
**Michele Mancioppi** 35:45 So, effectively, when you tell me, can Launchpad use certificates with different CNAM? The answer is no, which means if we use Launchpad, we could not.
be able to expose a URL like packages.openteentry.io.
**Sina** 36:02 Nope.
**Michele Mancioppi** 36:03 That would not work.
That sucks.
And it could also not work, even if we, If we put a proxy in front of it, that also would not work, right?
**Sina** 36:24 I don't know. It could.
Maybe.
Yes, but for a PPA, definitely not, I think.
Right? Because you're always apt adding the PPA address.
Right, that's our lunch bed.
So…
**Michele Mancioppi** 36:43 How about you.
**Sina** 36:44 wouldn't work.
**Michele Mancioppi** 36:45 I mean… We have here multiple packages, so it must… it's… Wait a second, can a PPA contain multiple packages nowadays?
**Sina** 36:57 Yeah, it should. I mean, it behaves similarly to everything else, right? You have the meta package.
So, if the metapackage is depending on multiple packages, like the .NET, instrumentation, everything else.
Then, what is the concern?
**Michele Mancioppi** 37:16 The concern is that we, the URL that people should put in their configuration files It's packages.opendantry.io.
So that it, the installation instructions… work effectively in both ways, and also the CNCF has the policy of Keeping control on the infrastructure.
So, there should be an exit strategy for… in case, for some reason, launchpad is no longer viable.
That would not require the users to… To go and, change their… their configurations.
This is why we were asking, hey, can we use a CNAME? Can we supply our own certificate?
Can we use our own signature?
And those are the questions that, We need to… to answer in order to… To validate whether a launchpad is viable, at least for me.
a sense of perspective.
Then if, it's canonical to put stuff in a universe.
Our main, goes and, takes the package and then thousands of DPA for them, or puts them in, in Ubuntu or DBA Upstream, that's fine.
It's okay.
**Sina** 38:37 Okay.
Alright.
**Michele Mancioppi** 38:44 I would very much welcome.
to, to see you folks try to package the stuff as it is in the POC, and then tell me if, That would make sense in Launchpad, because if it makes sense in Launchpad, it would make sense in Ubuntu.
Okay.
**atoulme** 39:13 Are we gonna go to the next one.
**Michele Mancioppi** 39:15 So, do we put a pin on the discussion about the creative config until we know more about .NET?
**atoulme** 39:21 Yeah, I can get back to you soon.
I just need a good fit, and a good read from there.
**Bastian Krol** 39:33 Okay, bye-bye, see you around.
**atoulme** 39:37 Cheer.
