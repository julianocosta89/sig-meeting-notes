SIG: Packaging SIG
Date: 2026-08-06
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Antoine Toulme (Splunk Inc.)** 01:00 Hey, Molly.
**Denys Sedchenko** 01:02 Bonjour!
**Antoine Toulme (Splunk Inc.)** 01:05 How you doing?
**Denys Sedchenko** 01:06 I'm fine. Quite a busy week in How You?
**Antoine Toulme (Splunk Inc.)** 01:11 Yep. Pretty easy. What do we have today, so… Oh… Let me see, got the dock somewhere.
Duck, yeah, here.
Let's go and get started with the dock the way… The way you should be, so… Just paste that stuff… no?
Not today.
**Denys Sedchenko** 01:41 I can copy and paste it.
**Antoine Toulme (Splunk Inc.)** 01:43 I got it.
**Diego Hurtado** 01:44 There you go.
**Antoine Toulme (Splunk Inc.)** 01:46 Very mulling.
Okay, so, agenda… Nope.
Alright, Jess, go ahead and put your name up.
Last week, we didn't discuss one issue I want to talk about.
Go ahead and put your stuff, anything you want to talk about.
Alright, if you don't mind, I'm gonna try to timebox my issue to maybe 5 minutes, and And we go to whatever else you want to talk about.
Good for everybody.
Alright, so, I have an issue up here, which is called Add JMX Cryptor Package. I'll show my screen.
Ba-buh… It's a big screen, sorry. So, There is some history to this. Before the Packaging SIG was started, there was a lot of discussion that I had with people around a piece of software that is currently published by the OpenTeometry Java Country project.
Let me show you exactly where that is.
It's, this particular… piece of software.
Is published on their release.
So you can actually download it from right here.
And it's a very useful piece of software that allows you to scrape the DMX port of a Java process for specific metrics with some YAML files of your choosing, right?
And so, the request I had was that it's great to have a JAR file, but the reality of it is that it's not enough for a sysadmin.
It's good for a ZRA developer, but it's not enough. So, people who work in a capacity of sysadmin would want to have a SystemD init file, that would make it easy for them to kind of manage it.
default config file that would look for a well-known, or at least some element of Java file, Java process being at the… Maybe the port 1337, or whatever is the default JMX port, I forget.
And, kind of leaves that for people to then adapt and work with.
And, nothing got done about it, because one thing that the JavaS SIG was clear about is that they do not know how to make it easy for them to package that. This is not something that they want to own.
Eventually, One of the maintainers… decided that, you know, it said, well, I see that you are opening this Packaging SIG proposal.
We would like to latch onto that, and use it.
And it was marked as not planned.
So I'm reopening this issue now.
Any feedback?
Denny got your hands up.
**Denys Sedchenko** 05:09 Yeah, first of all, what kind of, like, Java version is needed for this to run, because… Different versions of different distros supported, like, where to place it.
**Antoine Toulme (Splunk Inc.)** 05:22 This is a good.
**Denys Sedchenko** 05:22 Any background on this? Because, like, even with Python, like, that we ship, there are hard constraints.
**Antoine Toulme (Splunk Inc.)** 05:31 Yes, so the Java SIG has made the conscious effort of making Java 8, forward.
Vetted? Yep.
It will work with Java 8 and above. We don't have to have a strong recommendation of a GRE for this. I think we can do… we can play with the package metadata to say that we recommend that you install Java.
And it's really going not to be a good ride if you don't have it, but it's complex. The thing that I've learned working with Java developers is that they're very messy, and they like to put Java in weird places.
So, we should not… we should not try to own that too much. We can… we can allow them to sit at Java home, if you want.
Yeah.
I'll get into it.
**Michele Mancioppi (Dash0 Inc.)** 06:22 We need to go and look.
So, first of all, this will require… let me set expectations. This requires a specification process like we did for the system packages.
**Antoine Toulme (Splunk Inc.)** 06:32 Okay.
**Michele Mancioppi (Dash0 Inc.)** 06:33 It's a significant amount of work to make this not suck.
**Antoine Toulme (Splunk Inc.)** 06:37 Yes.
**Michele Mancioppi (Dash0 Inc.)** 06:38 It's not something that I would have when you do APT install open telemetry, so it would leave in the packages, but not be pulled automatically.
With the main open-to-entry thing, it's a very specific use case.
**Antoine Toulme (Splunk Inc.)** 06:50 Yeah, that sounds good.
**Michele Mancioppi (Dash0 Inc.)** 06:52 It's something that we could have as,
**Antoine Toulme (Splunk Inc.)** 06:55 Let me put that…
**Michele Mancioppi (Dash0 Inc.)** 06:56 I'm unclear whether we want to have it suggested.
when you pull in the Java package, because in reality, if you have the auto Java agent, you probably don't need the JMX scraper.
**Antoine Toulme (Splunk Inc.)** 07:11 I'm dead.
suggested by the Java package.
**Michele Mancioppi (Dash0 Inc.)** 07:16 It's a question mark, I'm not sure if it's a good idea.
**Antoine Toulme (Splunk Inc.)** 07:19 Yeah, I mean…
**Michele Mancioppi (Dash0 Inc.)** 07:20 Suggestions and suggestions?
**Antoine Toulme (Splunk Inc.)** 07:21 Christians, you know? You're like, okay, just so you know.
**Michele Mancioppi (Dash0 Inc.)** 07:23 I need to go and check.
So, the last time I tried to figure out what is the default, if there is, a, package in Debian and Ubuntu and RPM that counts as a package interface to say, I have some Java.
I did not get very, very far.
**Antoine Toulme (Splunk Inc.)** 07:46 Oh, okay. How do we know… how do we, check if there is some Java?
Correct.
**Michele Mancioppi (Dash0 Inc.)** 07:55 What you said about Java Home?
**Antoine Toulme (Splunk Inc.)** 07:57 That's the…
**Michele Mancioppi (Dash0 Inc.)** 07:58 worst possible solution.
Because in reality, what people would use is, like, which Java?
**Antoine Toulme (Splunk Inc.)** 08:04 Yes.
**Michele Mancioppi (Dash0 Inc.)** 08:04 So it could work on any JVM you're likely to yank from any Ubuntu version you're likely to use, yeah?
It's gonna work.
That also gives us the equivalent of, like, there is JEM, or these kind of tools to manage multiple versions of the JAM.
The fact, if you go and use which Java.
**Antoine Toulme (Splunk Inc.)** 08:29 I'm dead.
**Michele Mancioppi (Dash0 Inc.)** 08:29 that works Better than, than what we could do otherwise.
**Antoine Toulme (Splunk Inc.)** 08:36 Yeah, there's… there's a whole ecosystem, right, about this type of stuff. I… I thought we would keep it really light and not have a hard requirement for a Java package installation, for the reasons that I shared before, which is Java developers, Java… People who run JI services do a very weird job of installing JVMs on boxes.
**Michele Mancioppi (Dash0 Inc.)** 08:59 You make which Java inside the startup script? It works?
So that's why I'm saying this thing… this thing needs some thinking, and requiring the user after install to go and have to… so we… imagine what you propose is, we install your system, the unit, but it doesn't do fuck all until you go and set Javon correctly. That's not how it works.
**Antoine Toulme (Splunk Inc.)** 09:23 And this is really just a… so the SystemD unit is just to make it a lot easier for people who don't want to understand how SystemD works.
and has, like, some didactic, you know, comments that say, go in that file, set the Java you want, set the process you want to monitor on that port, and now run the magic command that starts SystemD and enable it to start its own startup.
**Michele Mancioppi (Dash0 Inc.)** 09:48 I love the idea, but you need to be more ambitious than this.
**Antoine Toulme (Splunk Inc.)** 09:52 Oh, you think I'm not being ambitious enough? Come on. Just tell me more.
**Michele Mancioppi (Dash0 Inc.)** 09:55 The UX, the UX is not, is not, There's no streaming on it.
**Antoine Toulme (Splunk Inc.)** 10:01 Do you want to do that as part of the, you want to do an interactive install, where you prompt.
**Michele Mancioppi (Dash0 Inc.)** 10:08 No, that's why I'm saying, we need to use things like which Java to figure out what… which one to use to run the jar, and then we can think of an auto-discovery mechanism, because in reality, when you do top, you can't see which processes are there, yeah?
And you can do less of and figure out which ports they have.
**Antoine Toulme (Splunk Inc.)** 10:27 You could do that.
You could definitely do that.
**Michele Mancioppi (Dash0 Inc.)** 10:30 And that is a much better experience, right?
**Antoine Toulme (Splunk Inc.)** 10:32 Okay, so you're getting fancy on me. I love it. That's really nice. That was not in my scope as of yet, but let's…
**Michele Mancioppi (Dash0 Inc.)** 10:41 You clawed it in 10 minutes, come on.
**Antoine Toulme (Splunk Inc.)** 10:45 Sir, I'm a PM.
I just slides for leaving.
**Michele Mancioppi (Dash0 Inc.)** 10:49 I'm a former head of product, and I clawed like a madman. What do you want?
**Antoine Toulme (Splunk Inc.)** 10:54 Alright, let's put that, LSF Java, find…
**Michele Mancioppi (Dash0 Inc.)** 10:58 Because.
**Antoine Toulme (Splunk Inc.)** 10:58 processes.
to,
**Denys Sedchenko** 11:01 Are you kidding.
**Antoine Toulme (Splunk Inc.)** 11:03 Later.
Yeah, of course.
**Denys Sedchenko** 11:04 Ask a question.
**Antoine Toulme (Splunk Inc.)** 11:05 Yeah, please, interrupt.
**Denys Sedchenko** 11:06 I'm not familiar how it's happening with Linux, but, like.
like, on, Debian or, Red Hat, do they, like, provide… like, for example, when you're trying to install Red Hat on Debian on Java, you get, like, one OpenGTK package, or you have, like, a separate OpenGDK 88, OpenGTK 26, OpenGTK 10, and, like, you have to manually choose what.
**Michele Mancioppi (Dash0 Inc.)** 11:29 Yes.
You have, in, in, Debian and Ubuntu, there is a default, JRE package.
which comes with the JRE from main, or JDK, I don't remember if it's JDK or JRE. Plus, you can… you find packages for pretty much every single JDK under the sun. You can install specific versions. And then, when you install multiple ones, you need to manage which one to use with stuff like Jamf.
Which, what it does is effectively patch the path environment variable… It's like convenience.
**Denys Sedchenko** 12:04 in Node.js, basically.
**Michele Mancioppi (Dash0 Inc.)** 12:06 Yes.
**Denys Sedchenko** 12:06 Okay.
**Michele Mancioppi (Dash0 Inc.)** 12:07 It's exciting.
**Denys Sedchenko** 12:08 We can just ship the binary and, like, say that, like, we are… Depending on, like, metal.
OpenGD came with a package, and, like, the customer, like.
**Antoine Toulme (Splunk Inc.)** 12:22 Yeah.
**Denys Sedchenko** 12:23 Handles whatever they want to do.
**Antoine Toulme (Splunk Inc.)** 12:25 That wouldn't be bad. That's not bad. The thing I would like to cross over is that to make this an actual experience for an end user.
To make it so that they can use this thing, because this is pretty much… imagine… You make a ferry, but it's on a dirt road.
To reach the highway, you're going to have to drive the ferry on 500 meters of dirt road before.
**Denys Sedchenko** 12:48 They're optional.
**Antoine Toulme (Splunk Inc.)** 12:49 Anyway.
**Denys Sedchenko** 12:49 Teres in option number two.
Like, if you take a bigger scope.
scraping GMX with, like, for scraping GMX, there are, like, GMX, like.
like, Java-based solutions. And, like, for example, in the project where I work, we're basically just planning to remove the Java dependency by just, like, using, by coding alternative approach, like, I saw, like.
Yeah, some guys do it in Rust, like, maybe it's a better solution just not to ship yet another Java file, and instead, like, ship some, like, native binary.
**Michele Mancioppi (Dash0 Inc.)** 13:25 I'm sorry, I don't think we should go and re-implement the JMX scraper.
**Antoine Toulme (Splunk Inc.)** 13:32 That's the.
**Michele Mancioppi (Dash0 Inc.)** 13:32 Well, maybe we can think that earlier.
**Antoine Toulme (Splunk Inc.)** 13:34 I have time for that.
**Denys Sedchenko** 13:36 Approach number two.
we just, like, bundle some kind of, like, very miniature Java version… Java stuff that, like.
That is enabled, like, enough to run this command.
**Michele Mancioppi (Dash0 Inc.)** 13:46 That will break people. You will be surprised by enterprises, the kind of draconian restrictions they have in the JDKs that they're allowed to install. It's for a number of reasons, but the biggest one is called FIPS.
**Antoine Toulme (Splunk Inc.)** 14:02 Oh, yep.
**Michele Mancioppi (Dash0 Inc.)** 14:02 So, grant you.
**Denys Sedchenko** 14:03 Oh, okay.
**Michele Mancioppi (Dash0 Inc.)** 14:04 specific versions of the GVM with specific versions of cryptographic setups, otherwise, that's the jail.
**Denys Sedchenko** 14:12 Banking, yeah, banking, yeah.
**Antoine Toulme (Splunk Inc.)** 14:14 The only thing I wanted to get from you folks today, right, just in this discussion, is like, first off, are you okay if we pursue this task, or is it out of scope of this SIG?
**Michele Mancioppi (Dash0 Inc.)** 14:22 I… I will very gladly… Review your proposal specification for how this package should work.
**Antoine Toulme (Splunk Inc.)** 14:30 Alright, let's do that.
**Michele Mancioppi (Dash0 Inc.)** 14:32 Provided that you adhere to the spirit of the SIG, which means it's not just curl in a trench coat, you actually build an experience around it.
**Antoine Toulme (Splunk Inc.)** 14:44 Well, you can hold me to that in that review. I'll let… Okay. Let's work to make it really cool.
For what it's worth, and to insert a little bit on this, GMX Craper is the obvious one.
The Java contrib has another, thing they also publish called the IBM MQ Monitoring Solution, which I built.
Now, that one, I also want to make easy to install.
**Michele Mancioppi (Dash0 Inc.)** 15:14 That comes with a lot.
**Antoine Toulme (Splunk Inc.)** 15:15 more guardrails, and some more configs.
**Michele Mancioppi (Dash0 Inc.)** 15:19 We will talk about that afterwards.
**Antoine Toulme (Splunk Inc.)** 15:22 Oh, okay.
**Michele Mancioppi (Dash0 Inc.)** 15:22 I am… I am open to that.
I, think you're gonna have a much funnier time.
To provide an experience built around that thing.
**Antoine Toulme (Splunk Inc.)** 15:34 You're gonna have maybe, like, 0.1% of the population of up and dementia care about that.
But this is the critical use case of OpenTeometry, is to bring…
**Michele Mancioppi (Dash0 Inc.)** 15:45 Yeah, I'm open to that.
**Antoine Toulme (Splunk Inc.)** 15:46 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 15:47 Just make a good job, and I'm open to that.
Cool. By the way, you said in the scope of 3 minutes, I built it myself, and I am a PM.
**Denys Sedchenko** 16:01 I have one huge concern regarding, like, building some experience on top of something.
**Antoine Toulme (Splunk Inc.)** 16:08 Here we go, that's the right concern. Go ahead.
**Denys Sedchenko** 16:11 Classic, classic concern of any packager. When you're trying to submit, like, for example, I recently had a conversation with a homebrew.
I tried to ship some extra shell scripts to basically make our, running as a service more, like, a useful experience, and they said.
We don't care, push that top stream.
So basically, all of that stuff that makes this extra sauce, ideally should be in upstream, and we basically just to manage… we need to manage packaging.
**Antoine Toulme (Splunk Inc.)** 16:43 That's a very nice concern, and I think we should… we should be sitting on that fence.
All the time. So, what do we own versus what upstream should own?
We could even try to make them own the service file, for all I care.
This is what needs.
**Denys Sedchenko** 16:58 It needs to be done.
**Antoine Toulme (Splunk Inc.)** 17:00 if… we can discuss that in the spec. Let's build a spec and have a fight about it, right? It sounds like a constructive discussion to have. I don't know where that's gonna go.
For IBM MQs, there's a lot more of that. For this one, it's actually… this is why I started with this one. It's like, it's a little smaller in scope, so we can talk about it.
**Michele Mancioppi (Dash0 Inc.)** 17:20 A baby package.
Yeah, it's a very laudable thing, and we were going to have much worse than these discussions with the language SIGs.
Case in point, Python has broken the experience for applications with older Elastic clients.
**Antoine Toulme (Splunk Inc.)** 17:35 Yeah, yeah, I saw that muff.
Yeah.
**Michele Mancioppi (Dash0 Inc.)** 17:38 That is part of the stable by default. Now, I personally do not necessarily care about who owns it, as long as the end user has a good experience.
**Antoine Toulme (Splunk Inc.)** 17:47 Yes. Yes.
But…
**Michele Mancioppi (Dash0 Inc.)** 17:49 That is what I care for.
**Antoine Toulme (Splunk Inc.)** 17:52 Yeah, but you guys are… you're gonna keep me straight on making sure we deliver this the proper way, and I just wanted to hear from you first, before I even start working on that. Is it okay if we pursue this? It looks like it's a yes, I'm good.
We can move on to a different discussion.
So… The next one is copper to packages.opentemetery.io proxying versus mirroring.
**Denys Sedchenko** 18:20 Yeah.
**Antoine Toulme (Splunk Inc.)** 18:21 Did you talk about that. Did you hear, Denise?
**Michele Mancioppi (Dash0 Inc.)** 18:22 I, I, wait a second. I actually started, looking into Denise's work and, estimating what it would take to move upstream. There are, like, 5 or 6 changes that we need to upstream for that. Okay. Before I start doing that work for chunking it up and upstreaming.
We really need to decide whether we want to go all-in and deploy it on copper, and the fact that we don't have canonical in the room since weeks worries me.
Because they were supposed to be the ones doing Launchpad.
Prodivia and Ubuntu.
But they disappeared.
**Antoine Toulme (Splunk Inc.)** 19:01 Did we lose them when we moved the meeting? Is that possible?
**Michele Mancioppi (Dash0 Inc.)** 19:05 I think we lost them because of summer, but I'm not sure.
**Antoine Toulme (Splunk Inc.)** 19:10 Okay, so you've had this relationship with Canonico from the start. Is it something.
**Michele Mancioppi (Dash0 Inc.)** 19:14 Oh.
**Antoine Toulme (Splunk Inc.)** 19:14 You want me to kind of take care of?
**Michele Mancioppi (Dash0 Inc.)** 19:16 No, I'll reach out and ask what, what are they… why they're not doing, and where they are.
**Antoine Toulme (Splunk Inc.)** 19:22 Okay.
**Michele Mancioppi (Dash0 Inc.)** 19:23 But, if it turns out that, you know, they, they reprioritized, or whatever.
And, I think we… yes?
**Denys Sedchenko** 19:34 Did you check the Launchpad post that, Sina posted?
The, like, message with the POC, and the source code?
**Michele Mancioppi (Dash0 Inc.)** 19:44 No, where is that? I missed it.
**Denys Sedchenko** 19:46 It's a Nattel Packaging, I can, give.
**Michele Mancioppi (Dash0 Inc.)** 19:49 Really?
**Denys Sedchenko** 19:49 Yes, it was, like, on… it was…
**Michele Mancioppi (Dash0 Inc.)** 19:52 Most of, like…
**Denys Sedchenko** 19:53 I know July.
One month ago, Here is it.
**Michele Mancioppi (Dash0 Inc.)** 19:59 I completely missed it.
**Antoine Toulme (Splunk Inc.)** 20:01 Okay, thanks.
Oh, okay, it's like, Okay.
**Michele Mancioppi (Dash0 Inc.)** 20:25 First code here. Alright, then I have some more work to do.
We'll evaluate.
How easy it is to upstream.
Alright.
But then, So it'll work.
The, I am going to be… on vacations the last week of August and the 1st of September.
And, it's pretty crazy for me right now, at, dollar work.
So I do not really have an ETA.
To… to evaluate this, plus, plus the porting of copper.
**Antoine Toulme (Splunk Inc.)** 21:16 Let's see.
**Michele Mancioppi (Dash0 Inc.)** 21:23 And I really would like to.
I really want to do it, because it sounds like our best bet.
**Denys Sedchenko** 21:30 I also will be… not available since 28th.
of August till 4th of September.
**Antoine Toulme (Splunk Inc.)** 21:38 Okay.
So you're both taking time off at the same time. Okay, good to know.
**Denys Sedchenko** 21:46 So, regarding copper, I checked two approaches, like, we either can just, like, have a proxy pass, Or, Or basically do the mirroring.
I used, like, a Cloudflare, like, Cloudflare Workers as a reference point.
And, like, considering on pros and cons, it will be easier just to basically do the mirroring.
You have, like, a blob store, and you just, like, basically… You have some kind of, like, way to, like, expose it publicly.
I don't have the POC yet, I mostly did the research, and I will do the POC for the next… for our next meeting.
**Michele Mancioppi (Dash0 Inc.)** 22:29 And that way, we effectively gain control of the SSL certificate.
**Denys Sedchenko** 22:34 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 22:35 The signing is still bound to Copper and Launchpad.
**Denys Sedchenko** 22:38 Yeah, and actually one of the side effects Okay, we just… basically, we mirror everything there, but, like, when user will try to import the key.
In the key description, you will see, like, basically the copper… Term will leak in a sign-in key description.
**Michele Mancioppi (Dash0 Inc.)** 22:57 Yeah, okay. But the point is that as long as we can, We can change the hosting.
and keeping the certificate, because the certificate is bound to the DNS name, then we're fine.
Yeah. Exactly, the failure mode for us of a migration is, one.
The user needs to… to… Define the repository anew.
And second, they need to go and delete signatures.
We do not have a solution for go and delete signatures, because if we build them no longer on Copper and Launchpad, we go somewhere else.
New signature, congratulations.
I would like at least to avoid people having to point to a different… to recreate the entire package, because that is something that people miss out on. If you go and update and say, oh, yo, the key changed.
They will press yes and go ahead. They want to replace it. They will press yes and go ahead. If they need to figure out that the DNS name of the repository is different, everything is fucked.
And you lose half of your users forever.
**Denys Sedchenko** 24:03 And also, one of interesting, Interesting, side effects, like, first of all.
like, Fedora, like, the corporate doesn't publish, like, an official SLA, so, like, if it's… get overloaded, We can't actually, like, complain.
And also, like, the copper builds, like, they have, like, a rotation period, so, like.
Like, some bills might get, like, old bills might get removed, deleted, and, like, with, mirroring, we are having an opportunity of, like, before, like, uploading the new artifacts to, like, archive the previous one somewhere.
If necessary.
**Michele Mancioppi (Dash0 Inc.)** 24:43 This actually already came up. Look at the issue from, We had an issue opened, because with the new version of the packages, we removed from GitHub pages the old ones, and that broke, pinning.
He booked in the version, and then that broke because the package was no longer available.
We do not have… a policy.
About, about how to support pinning.
Whether we want to support it, and how to support it, and how long.
What do you want to do?
**Antoine Toulme (Splunk Inc.)** 25:27 Opinion.
**Denys Sedchenko** 25:28 I'm going to investigate that.
Look at this page.
**Michele Mancioppi (Dash0 Inc.)** 25:31 When you actually go, for example, and have packages like these in main or Universe.
And I'm going to use D.
DBN terminology.
You don't pin packages. You get the latest on the release train.
**Antoine Toulme (Splunk Inc.)** 25:47 Yep.
**Michele Mancioppi (Dash0 Inc.)** 25:51 Do we want to support pinning in a scenario like that?
**Denys Sedchenko** 25:57 How do you, like, pin the package, actually? Like, you might have an old repository metadata cached on your system.
**Michele Mancioppi (Dash0 Inc.)** 26:07 Oh, you do it like this.
**Denys Sedchenko** 26:13 You… You mean the… I mean, that way.
**Michele Mancioppi (Dash0 Inc.)** 26:19 Huh?
Because we, the GH pages is not incremental.
**Antoine Toulme (Splunk Inc.)** 26:28 Somewhat of an issue about this?
**Michele Mancioppi (Dash0 Inc.)** 26:30 Yeah, it's beautiful.
**Antoine Toulme (Splunk Inc.)** 26:32 Someone's using our stuff?
**Michele Mancioppi (Dash0 Inc.)** 26:33 Yeah, Marco has also been using the interactor all along.
We met him in, Costa, remember?
No, you were not in Brazil. I met you in Brazil.
**Antoine Toulme (Splunk Inc.)** 26:45 No, I mean, it's great. Okay, so… Right now, we don't have the luxury of having any sort of pinning. We should just publish the latest two GitHub pages, and, you know, if you don't like it, well, come over to a SIG meeting and talk to us about what expectations you want it to have.
And once we have the ability to publish to our release, So… We should have a proper lifecycle discussion about the packages.
It's more than pinning.
It's one of the good.
**Michele Mancioppi (Dash0 Inc.)** 27:20 versioning it.
When do we release new versions? When we decide to update the Java package?
**Antoine Toulme (Splunk Inc.)** 27:26 When do we drop the order?
**Michele Mancioppi (Dash0 Inc.)** 27:27 How long are we going to support packages we publish? Yes?
**Antoine Toulme (Splunk Inc.)** 27:32 Right now, I would set the expectation that we only publish the latest, and we have a very loose policy for any old versions that can be removed at any point in time.
Until such time that there is a recommendation from someone who's got a lot of hard drives and a huge bandwidth, who wants to host, A bunch of old stuff for us.
**Michele Mancioppi (Dash0 Inc.)** 27:54 I am fine with this policy for the GitHub Ages-based repository.
Yeah, of course. And I think we need to think way harder when we move to Launchpad and Copper.
**Antoine Toulme (Splunk Inc.)** 28:07 Okay, that's fair.
We don't have to have the internal, is what I'm also saying, right?
**Denys Sedchenko** 28:13 I have a question.
How did actually hosting multiple old, like, packages of multiple versions, how it actually works under the hood?
Does it, like… instead of, like, regenerating repository metadata, the repository metadata should be append only?
Like, you just append and append and append?
**Michele Mancioppi (Dash0 Inc.)** 28:35 Not sure. The, I'm not sure. I believe, believe, and take it with infinite grains of salt.
That the index is always the latest package.
So there is the version of each package.
And you can reference all the versions by adding the version suffix.
**Denys Sedchenko** 28:56 Interesting, because, like, I'm checking the… I'm checking the structure of, for example, how copper looks like.
Okay, I will need to… I need to investigate that.
**Michele Mancioppi (Dash0 Inc.)** 29:14 Can you, can you, yeah, can you maybe actually investigate and comment on the issue?
So, for the GitHub-based approach, I'll answer, and I'll put something on the repository by saying, hey, until we migrate to something more serious, it's only the latest version, so don't pin.
And, we'll evaluate when we have actually a reasonable hosting.
Mr. Westy.
**Antoine Toulme (Splunk Inc.)** 29:38 Michele you want me to do that? I can do that.
Or you were asking Denys to do that? Okay.
**Michele Mancioppi (Dash0 Inc.)** 29:44 No, I know that I was asking Denis to look in how the index works for the repository.
**Antoine Toulme (Splunk Inc.)** 29:50 My understanding of the indexes is that you recompile the index, pretty much you regenerate the index by taking all the releases that you've had so far in the thing, and it's not an append, it's a meaningful… Yeah, right now we're…
**Denys Sedchenko** 30:03 But now we're generating the metadata, like, the preposition.
**Antoine Toulme (Splunk Inc.)** 30:06 It originally limited of everything you've had so far, which…
**Denys Sedchenko** 30:10 is… Yep.
**Antoine Toulme (Splunk Inc.)** 30:10 Over time, I've seen that take longer and longer, and it's actually a big cramp on some of the packages when you have too many.
I mean, we could talk about… Retention.
And it's good that he's breaking this up. I didn't imagine that we would have that discussion so early in our lifecycle as a SIG, frankly.
Okay, we gotta run.
**Michele Mancioppi (Dash0 Inc.)** 30:35 Yep.
Alright, bye folks.
**Antoine Toulme (Splunk Inc.)** 30:38 Bye, buddy.
**Denys Sedchenko** 30:40 I mean?
