SIG: Configuration WG
Date: 2025-08-18
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:21 Hello!
Already more people than last time!
**Tyler Yahn** 00:38 Hey, Gregor.
I like your background.
**GZ Gregor Zeitlinger** 00:43 Thanks!
That's a Voyager.
**Tyler Yahn** 00:46 Yeah, yeah, yeah. Are you a fan?
**GZ Gregor Zeitlinger** 00:49 Yeah, kinda.
**tristan** 00:54 Alright, Tyler's bringing back the stash.
**Tyler Yahn** 00:58 Yeah, must have been a while, Tristan, I haven't seen you in a while then.
**tristan** 01:02 Yeah, I haven't.
**Tyler Yahn** 01:03 Yeah.
**tristan** 01:04 Well, you're usually, yeah, you're not on camera in, like, the spec meetings and stuff, so….
**Tyler Yahn** 01:10 Yeah, that's also fair. Good point.
I see Alex is back as well.
**Alex Boten** 01:21 Lou.
**Tyler Yahn** 01:21 Oh, excuse me.
… Yeah.
I don't see… I see some stuff from the template board for next time?
Did somebody here put the… hmm… I'll just copy this over.
**GZ Gregor Zeitlinger** 01:41 I… think I might have.
**Tyler Yahn** 01:43 Okay.
**GZ Gregor Zeitlinger** 01:45 Forgot to add my name.
**Tyler Yahn** 01:49 Oh, okay, yeah, yeah.
**GZ Gregor Zeitlinger** 01:51 Yeah, I recognize the second one.
Oh yeah, right, I also added the first one.
Oh, I know.
Yeah, that's actually the… Even more interesting.
**Tyler Yahn** 02:17 Well, cool. …
We can… we could probably jump in then, if you want. We've got the triage, but maybe we can just talk about the first issue there.
Gregor, and we can do a triage at the end.
**GZ Gregor Zeitlinger** 02:32 Yep, also works for me.
**Tyler Yahn** 02:35 Okay, cool. Go ahead.
**GZ Gregor Zeitlinger** 02:38 So, apparently there has been a discussion about, the declarative configuration,
stability guarantees, because the hotel collector
is already using declarative configuration, and is declaring itself as stable. Which means, that development Is…
kind of stable right now. This was the result of the last spec meeting. I added it, actually, to the spec meeting, because I thought this would be the right forum to take a decision, and now I want to also put it here to first inform, and then…
If we don't like it, then we can also, …
Go back and, try to, challenge, but…
It is a change. Right now, development means you can change anything, and for,
At least until now, it was, …
Quite important to be able to have this liberty.
**Alex Boten** 03:51 I'm curious, was… Were people from the collector at this spec meeting to discuss this?
**Tyler Yahn** 03:58 No, I think that's kind of where this is coming from. This bled over into the GoSig as well, so I'm sorry, I'm just double checking, because there's, like, some other things. So, yeah, it was…
it's around the Prometheus exporter itself, which is, like, defined as development there, and it was said that, like, the Prometheus exporter and the collector was stable, and that doesn't seem to be the case, actually, now that I'm looking at the collector as well. And so, I think the concern was that, like.
the… they wanted to change the way that they're doing the translation strategy, there's a PR for it, and the problem is, is that, like, how do you handle that migration from one configuration to the other?
They were under the impression that it was stable, so that, like, that kind of thing wasn't gonna work for the collector, because they exposed this configuration there. And I was, like, very confused about a lot of that, stuff.
But I think, to the point of, like, it's being stable, one of the things that did kind of, get brought up was that, like, people like, Josh Sirth were pointing out that, like, things that are, like, de facto stable are stable in some sense. There's, there's, like, a reliance on it.
And so, I think that that's also maybe, like, something that is applicable here. I don't think that, like, technically that… a lot… I think a lot of the
details were a little missing in the spec meeting last week. But yeah, that's kind of the backstory on that one, Alex.
**Alex Boten** 05:22 Okay. So as… as a person who implemented this in the collector, I… I can tell you this is….
**GZ Gregor Zeitlinger** 05:29 Not stable?
**Alex Boten** 05:30 In any way, in fact, we, I spent a bunch of time
supporting migration from V2 to V3, and I'm going to have to do the same thing to support migration from V3 to 1.0 or whatever. And the way that the…
The way that… configuration changes happen in the collector is that we'll… One, a config change.
Want to config…
parameter has to change, we'll enable it behind the feature gate, we'll make that feature gate available for end users for X number of releases, I think it's 2 releases, maybe more.
At some point, we flipped the feature gate to go from, you know, disabled to enabled by default. At that point, end users still have, like, a number of releases where they can go off and use that feature gate to disable it.
And then, eventually, we make that feature gate stable, which means that it can no longer be disabled. And at that point.
You know, then we can, like, deprecate the old code or whatever, but there is that process for migrating things, even….
**GZ Gregor Zeitlinger** 06:32 even….
**Alex Boten** 06:32 Even in, like, the stable configuration aspects of the collector.
**GZ Gregor Zeitlinger** 06:38 Yeah, it's a different definition of stable.
**Alex Boten** 06:41 Sure, yeah, and the collector's also not at 1.0, and that's something that we've said, we want to achieve at some point, but it's been…
5 years now of trying to achieve 1.0 in the collector, so eventually we'll get there, but it's not there yet.
**GZ Gregor Zeitlinger** 06:57 So, I guess for this group, it would be interesting to know, which,
Areas of the declarative configuration.
… Are, exposed in the collector, and where we have to be more careful than for the others.
**Alex Boten** 07:17 Yeah, I mean… the…
I think the same scope of what we plan on declaring stable for 1.0 is what we shouldn't, just go off and break.
moving forward anyways. Like, I don't think anything has to change from the 1.0 RC1 candidate, or whatever. I don't think there's any areas that the collector relies on that aren't already, like, planned to be stable with the 1.0 release, I guess.
I guess maybe the Prometheus exporter, depending on what changes are coming down the pipeline there, but…
that seems to be an ongoing struggle with the Prometheus export pipeline, so….
**GZ Gregor Zeitlinger** 07:56 Okay, so we don't know exactly which parts are,
are affected, we would have to check one
One by one, if we have another change,
**Alex Boten** 08:09 Yeah, I mean…
you know, an example of something that broke recently with the Prometheus exporter, and I'm only calling it out not to pick on Prometheus, but because it happened, was the library started emitting metrics in a different name format, like the prefixes, or the suffixes it was using ended up getting tacked on two times, or whatever, because of an issue.
And, like, that didn't include any changes from the configuration standpoint, right? Like, it just… we pulled the latest change in the library, and then that got thrown out, or whatever, so…
I guess….
**GZ Gregor Zeitlinger** 08:43 The scope info labels that got added?
**Alex Boten** 08:47 I think so, maybe. I… there was… there was 2 different issues that kind of dragged on for 3 or 4 weeks, so I can't quite remember the details.
… But, I guess… I guess what I'm trying to say is that I don't…
I don't exactly know the stability guarantees we can provide for libraries like the Prometheus Experter will be in the future, and I don't know how we can scope that down.
And I don't think that this group will specifically be able to make any claims other than, like, we promise not to change the configuration options that are available in a backwards incompatible way.
moving forward for, like, the Prometheus Expert or whatever, and I feel like that's kind of the scope of what we can guarantee.
**Tyler Yahn** 09:35 Yeah, I think if that makes sense.
to me, that's kind of what my understanding of our existing policy is. I also know that, like, the Prometheus exporter is, like, listed in, like, this development, like, classification as well, and so I think that there's a little bit more flexibility there.
from what our definition is, and so I don't know. It seems like there's a lot of… ….
**GZ Gregor Zeitlinger** 09:58 I think there's a lot of genuine….
**Tyler Yahn** 10:00 … desire to not hurt users here from the Prometheus folks working with that. It's the…
Prometheus Translator, thing is what's sparking all this, and I think, like, that's great, and I think they're being very cautious about trying to not break this configuration as well, is the thing.
I think talking with them on Thursday in the GoSig as well, like, there was, I think, a little bit more confusion than… I think… they were very certain about not trying to break things, and I think that, like, it may be…
… Yeah, I don't know if it's as drastic as it's been made out to be.
Yeah, exactly.
And so the Prometheus being in development and running on prod is something that Josh also kind of was…
pointing out is, like, you know, at some point, like, it is becoming more stable because of that, and so I think it, like, it's… it's…
I think it's good to have caution. I think it's good to also have a migration path, for that kind of thing, but I also think that, like, it can't be something that can't ever go away, like, if you have config that you don't want to have for the long term.
But what you described, Alex, seems fine.
Like, it seems like the appropriate amount of caution to get this over.
**Alex Boten** 11:17 Yeah, I mean…
I guess if there was… if there was a bunch of changes in the underlying library, you know, I would have expected some kind of major version bump to prevent users from accidentally upgrading to it.
That… that's… that's what major versions are for? Like….
**Tyler Yahn** 11:34 Well, I mean, I'm guessing you didn't see the….
**Alex Boten** 11:35 But….
**Tyler Yahn** 11:36 yeah, the catastrophe that was, like… I don't know if you saw, but, like, they didn't actually have any release tagged version, and everyone was just depending on a commit hash. And then, of course, they changed something on main that broke the API, and everyone was very mad about that. I was surprisingly mad about that.
So, yeah, right now they have a version, so that's a step up. They definitely don't have a 1.0, but yeah.
Yeah, so that's… it's… yeah.
It's comical in some sense, but…
Okay, I mean, I don't know… to answer your question, Gregor, I don't think that there's any… …
there's definitely no restriction yet on, like, these development things that we've imposed. I think that there's a de facto one that we've tried to, like, help, but I think as we're getting closer to stability, like, that sort of thing of, like.
Things that are going to be listed as stable.
and that are not in development are going to be stable. But otherwise, I don't…
Yeah, I think that's something to keep in mind.
**GZ Gregor Zeitlinger** 12:34 Okay, yeah.
Yeah, good from my point.
**Tyler Yahn** 12:41 Cool.
Also, next up, Gregor, you wanted to talk about the config provider, is…
Can also be based on environment variables?
**GZ Gregor Zeitlinger** 12:50 Yes, Maria, and I had talked last week, and she's experimenting.
kind of experimenting, implementing the config provider that is based on environment variables, and I noticed that this is different from Java, where the config provider is only based on the configuration file, and it just has a different object called config properties, if not
I just, wanted to, yeah, basically share that and ask If, … The…
Configuration specs has anything about that, …
I think Maria didn't find anything, so probably it doesn't.
**MG Marylia Gutierrez** 13:37 No, yeah, so I can't even share how exactly I'm doing, and, well, parts that I've already done, and my goal. So my goal is to have, like, …
basically right now, how it works on the JavaScript, a lot of places are just, like, reading environment variable all over the place, or, like, some parameters, flags, feature flags, or whatever.
So the first step that I did was actually create, like, a config provider, and every time that somebody needs some value like this, they always go to the config provider.
So the first step is basically not breaking the current existence, so the config provider can read environment variables and return that says. So that is what I have so far working. And then the next step is, if you pass
like a file, they actually… the config provider then is going to read from the file, and populates the values and return that instead. So this way, your config model is always the same, doesn't matter if it is, like, environment variable or config file, and you can use whatever, just deciding which one you want to use.
**Tyler Yahn** 14:45 Yeah, that's cool. How do you plan to, deal with, like, interpolation of, like, environment variables in the config file?
**MG Marylia Gutierrez** 14:56 Yeah, that would work no matter… it's more, like, for example, I have one….
**GZ Gregor Zeitlinger** 15:00 Config provider that is just, like, an interface.
**MG Marylia Gutierrez** 15:03 And then you can say, am I calling the file or the environment variable? And the one that reads the file can read environment variables from the file, if you have it there.
**Tyler Yahn** 15:16 Yeah, that's… that's cool. So, essentially, you centralized, like, all configuration into one thing, even environment variables, yeah.
**MG Marylia Gutierrez** 15:22 Yeah, so it's basically, like, a new package that is, like, called configuration, so it is responsible for all configuration, doesn't matter which type you want, and then you can just select what is the… that makes sense for you.
**Alex Boten** 15:37 Yeah, I think that's… I think that all makes sense.
…
I kind of want that in all languages, to be honest, because then it would make finding where… where that parsing of environment variables lives much more, …
Accessible.
**MG Marylia Gutierrez** 15:54 Yeah, it's pretty much, like, early stages, because right now, the code is still, like, reading all over, like, the environment variables. So I actually just got merged, like, 10 minutes ago, the… my basic config provider that is just reading environment variables and returning, and then I can… I'm gonna pick one of the package to use, like, as a proof of concept. And then the next step is actually parsing a YAML,
And reading from that.
And then… but I don't think… just checking, because my goal also is have the, like, the model itself based on the specs. So right now, I only pretty much, like, copy the parameters that we are reading. My…
goal at the end is to have something, like, similar to, like, semantic conventions, that you can just, like, have a script that generates based on the specs, at least is what we do on the JavaScript, and generate a file that is equivalent. Is anyone doing that on the other… any other languages?
**GZ Gregor Zeitlinger** 16:56 Java is, generating,
the Java files based on the JSON files.
So that's new.
**Tyler Yahn** 17:05 schema, yeah.
**GZ Gregor Zeitlinger** 17:07 Schema, yes, thanks.
**MG Marylia Gutierrez** 17:08 Okay, yeah, cool. So yeah, I'm… I have that as one of the tasks as well.
**Tyler Yahn** 17:14 Yeah, I've seen JSON schema generated into JavaScript before. It seems pretty…
should work pretty well. I mean, I'd be very interested if it doesn't. That's definitely something we'd want to know.
Gregor, I think you're sharing your screen. Is this something you want to talk about next?
**GZ Gregor Zeitlinger** 17:36 Exactly, I'm now trying to share just one window instead of the entire screen. Is that working?
**Tyler Yahn** 17:44 I only see the, configuration issue 257 on the screen.
**GZ Gregor Zeitlinger** 17:48 Yeah, that's what I was trying to do.
Cool, so that worked.
Yeah, I forgot to add that before, but this is a missing feature.
…
And I discussed it only in the Java declarative configuration working group, but this is actually not Java-specific, so it's…
something that we should decide here before proceeding in Java.
However, it is based on a feature that was possible in Java before, and I don't know if it was possible anywhere else.
And this is the ability to, …
configure authentication headers dynamically, and this is currently used for GCP.
Like, in this code snippet here.
Oh, sorry, not in this code snippet, this is the alternative. Okay, but it is possible right now. And, …
There is no… Way how you can get this done with the set of,
plugins that exist in Java, and I think that is
Also, a one-to-one relationship to the to the, …
instantiation path that is laid out in the specification, and that is… first, …
you parse the YAML file, and then…
You can do some modifications on the in-memory.
representation of the YAML file, and then this gets transformed into the actual objects that do the work, exporters, and so on. And in this case, it's actually an exporter that needs this header.
And… This doesn't.
**Tyler Yahn** 19:41 So is this….
**GZ Gregor Zeitlinger** 19:42 partner.
**Tyler Yahn** 19:43 Is this kind of like a resource detector? In that, like, what you're doing in the configuration is saying, use this resource detector at runtime to go find these values?
**GZ Gregor Zeitlinger** 19:52 It's not a resource detector, you want to set a secret so that you can push your telemetry data to GCP.
**Tyler Yahn** 20:01 Yeah, no, I know it's not a resource… I'm asking if it's like that, though, where what you're asking for the configuration to do is be set up so that it runs some sort of, like, runtime code, so, like, it's defining that runtime code, or is it something else?
**GZ Gregor Zeitlinger** 20:15 Exactly, it can be best seen in this, in the second proposal, which I actually like better, as, that,
This exporter OTLP already exists, and the suggestion is to add here this authenticator. Authenticator, it has a name, and then can also have properties. And, based on this GCP name.
it will, load the Java object for GCP, and then this can do
Things at runtime, such as setting authentication headers.
**Tyler Yahn** 20:55 So I think that makes a lot of sense. I think there is a spec issue for this as well. I might…
I don't think it's as specific as…
like a GCP authenticator, I think it's more of a…
being able to set some sort of auth client for HTTP at the spec level, which I… but I… I think that this is… this is great. It's, … it's gonna exceed the scope of the configuration, though, right? Because you need to have these authenticators defined somewhere else to say this is what it's being configured.
So I think this is something that would have to be defined at the specification level, though.
Before we can….
**GZ Gregor Zeitlinger** 21:33 No, I don't think so. So, I'm coming from the Java… sites, so, …
try to bear with me. In Java, you have, … The ability to, …
create your own things, and the thing can be an exporter, so instead of OTLP, I can, for example, create a, …
save on disk exporter, or, Grafana using YAML exporter, or whatever. And then this will,
Search your code using some reflection magic for an object with that name.
And this is… the same idea that I'm proposing here. So, all we need to,
Define as the… concept of an authenticator. But GCP is nothing that has to be specified. This is implemented
as an object that just happens to have the name GCP.
**Tyler Yahn** 22:36 Yeah, I… I still think that needs to get specified, though, because things like Go, where they're statically compiled binaries, don't have dynamic runtime, like, interrogation. Like, you would have to have already, like, imported this into your package, and imported the… whatever authenticators you actually want.
I think that this makes sense, like, where you may want to be able to, like, extend it beyond, …
you know, maybe you have, like, you know, your internal authentication scheme that you want to actually set up here. I think being able to configure that makes sense, but the concept of an authenticator is not something that's a part of…
the specification right now, and I don't think that you can add configuration for it if, like, it works in Java, but it doesn't work in any other language, because the concept itself doesn't exist.
**GZ Gregor Zeitlinger** 23:24 Yeah, the concept of an authenticator has to exist. Yeah, I agree on that. Maybe it was just a misunderstanding.
**Tyler Yahn** 23:31 Oh, okay. Yes, I mean, I think if we can get that concept
Accepted across languages, then having some configuration like this makes a lot of sense to me.
**GZ Gregor Zeitlinger** 23:40 Okay, cool, … Van…
If you can find the existing issue that, and tag me there, that would be great. Would it be in the configuration or in the specification repository?
**Tyler Yahn** 23:55 It's in the spec repository, …
And it overlaps. I don't think it… it doesn't have a concept of authenticator, but it does have a concept of, like, dynamic authentication, so I think this might actually be…
a better proposal. But yeah, I, I can… I can take a look, …
Okay, you have the issue here. Yeah, I can… I don't know, I don't want to waste your time in the meeting. I will… I can find it afterwards, though.
**GZ Gregor Zeitlinger** 24:20 Yeah, that would be great. …
The collector already has this concept, I don't know if this, …
is based on a specification or not, but I copied it for reference, below here. This is an actual working code.
That I copied from somewhere.
**Tyler Yahn** 24:42 Oh, they have a concept of authenticator, huh?
**GZ Gregor Zeitlinger** 24:45 It's in the configuration, I don't know if it's based on a specification or not.
**Alex Boten** 24:50 It is not based on specification, it's just an extension in the collector.
**Tyler Yahn** 24:54 Okay.
**GZ Gregor Zeitlinger** 24:58 Okay, so we could just….
**Tyler Yahn** 25:00 I was gonna say, there's two places that are already using it, I think that's a great motivation to have it be more universal across hotel, so, yeah.
Yeah, I, I agree. …
Yeah, like I said, I'll try to ping you in the issue, and maybe even put it in this issue, the related spec issue, but it might be worth just bringing up tomorrow at the spec meeting as well, the concept itself.
Alex might have already found it.
**GZ Gregor Zeitlinger** 25:26 Okay, cool, yeah, I will do that.
**Tyler Yahn** 25:34 Yeah. Thanks, Alex.
Gregor, do you see the, … issue that Alex posted?
**GZ Gregor Zeitlinger** 25:45 Yep.
**Tyler Yahn** 25:46 Perfect.
Okay, cool. …
I'm looking at the meeting agenda, so we still have the triage. We can go through the triage board. I haven't looked at this since Jack hasn't been here, so…
I have no idea what the state of this is.
**GZ Gregor Zeitlinger** 26:08 You know when Jack will be back?
**Tyler Yahn** 26:11 I don't. I know he's on paternity leave, so I…
I… I hope not soon. I hope it's going well, and I hope he's enjoying every single minute he's gone.
**GZ Gregor Zeitlinger** 26:21 Of course.
**Tyler Yahn** 26:22 rough.
Okay, cool. So…
let's see, tracking language implementations is something we're still actively working on. I think this is…
Definitely in the Go world, still an active, piece that a lot of people who are on vacation as well are, working on, so I can only speak in the Go sense, …
Looks like C++ is pretty far. Java, definitely, you all are cranking along. Php…
I know that JavaScript, is getting there, based on today's meeting. So yeah, I think maybe, …
How about Erling? Tristan, has there been any movement there?
**tristan** 27:08 Yeah, I added the link to the pull request at the end of this issue.
**Tyler Yahn** 27:14 Perfect.
**tristan** 27:15 Just to do this, yep.
Before this meeting.
So it's… yeah, it's going on… Based on 1.0, but then…
It's got a little ways to go.
**Tyler Yahn** 27:28 Cool. ….
**MG Marylia Gutierrez** 27:29 I don't know if you also want to update, so I do have a project board for the JavaScript one. I just shared the link here.
**Tyler Yahn** 27:39 Sure, I can take a look at that one.
**GZ Gregor Zeitlinger** 27:43 Yeah, for Java, there's also project board. Maybe we want to add, like, a new column or something?
**Tyler Yahn** 27:49 Yeah, I think that's a great idea. …
The project board… sorry, we're, …
Marlena, where did you add the project more?
**MG Marylia Gutierrez** 28:01 I just shared the link here on the chat. I can put it on the.
**Tyler Yahn** 28:05 Oh, oh, okay.
Yeah, me and Zoom are not the most, friendly when I'm sharing screens. Let's see if I can find it.
**GZ Gregor Zeitlinger** 28:18 Okay.
**MG Marylia Gutierrez** 28:18 Cool. I added to the notes as well.
**Tyler Yahn** 28:21 Perfect.
… I can just add to the notes section for now, ….
**MG Marylia Gutierrez** 28:38 We probably can add this development as well, the second column.
**GZ Gregor Zeitlinger** 28:45 I also added the Java.
Or to the notes.
**Tyler Yahn** 28:50 Okay.
To the notes here… okay.
Okay.
Cool. Alright, so… I think with that…
JavaScript, and JavaScript, your target… well, I… yeah, you should target 1.0. ….
**MG Marylia Gutierrez** 29:28 Okay.
**Tyler Yahn** 29:30 They'll target, the other versions, yeah.
Cool. Alright, so there's definitely, I think, a fair amount of,
Movement right here, so this is… this is in progress still, but definitely worth checking in.
Okay, ….
**MG Marylia Gutierrez** 29:51 There's a typo on the JavaScript.
On the development. Oh, sorry.
**Tyler Yahn** 29:57 Yeah, that's not the first time I've misspelled things.
Thank you for finding that.
Look good?
Kim.
Okay, then next up is tracking stabilized declarative configuration. So this is still an open issue in the specification. I think that there's a…
There we go.
…
PR that is still actively being worked on. I think, Robert is the person from the GoSig who is evaluating the Go implementation right now.
So, it's, it's still working in progress, and I think that there's still some things he wants to touch base on. He is out this week, though, so I don't think there's gonna be an update from Go. I think I saw, Tristan, you had responded here as well.
**tristan** 30:55 Oh, right.
Because it does the, initialization at boot, and that's not…
Defined yet, but it's used in the… Spec for the config.
**Tyler Yahn** 31:11 Okay. Yeah, that's definitely something we should probably lock down then.
That seems… that seems reasonable. Yeah, okay, thanks for pointing that out. I think there's a lot of things like that are…
Robert's also finding… it just… The spec itself needs to get cleaned up.
Okay, I think that we can… I don't know if we can make an issue out of that.
**tristan** 31:36 There is an issue, I linked to it.
**Tyler Yahn** 31:39 Oh, it already is. Okay, perfect. Okay.
I don't know if we put it in this project board.
Yes.
Okay. We've added that then. Any other issues, Tristan, that you know of, or any other folks on this one?
Okay.
then maybe we can just go through the no status one. So the requirement of distribution
Distributions for configuration requirements.
**GZ Gregor Zeitlinger** 32:35 Yeah, I think I'm… that is still on me.
**Tyler Yahn** 32:39 Okay.
**GZ Gregor Zeitlinger** 32:40 Quite an old one.
**Tyler Yahn** 32:42 Yeah, no worries. I don't know… is this… this isn't required for stabilization, right?
**GZ Gregor Zeitlinger** 32:48 No, I don't think so. At least that's what, Jack said last time we talked about.
**Tyler Yahn** 32:56 It doesn't seem the case to me, but, okay.
Maybe that's why they're in this no status instead of having… yeah, I probably would need another project board, but don't want to lose track of it.
How to add additional exporter config parameters? This is kind of what we were just talking about, with this authenticator.
This would be one.
Yeah, I think this has… yeah.
I think this is similar to what you've already done, Gregor, and your implementation in Java, is what we could do here for language-specific
Values, but… That doesn't seem like it's a blocker.
**GZ Gregor Zeitlinger** 33:42 It's already done what?
**Tyler Yahn** 33:44 So your authenticator and how it's working there, and, like, in the config, or, sorry, in the collector, how there's already, like, a way to extend the configuration for an exporter? I think that's what this is asking for.
**GZ Gregor Zeitlinger** 33:53 Okay.
**Tyler Yahn** 33:55 Yeah.
**GZ Gregor Zeitlinger** 33:56 Because it sounds more general. Additional parameters is quite… General….
**Tyler Yahn** 34:03 I… Yeah, it is.
But I think that you already have kind of a general thing, like, in the collector, similarly, like, I think that you could define something for an exporter like this, that you need to….
**GZ Gregor Zeitlinger** 34:20 So you can have additional properties for an exporter, but it has to be primitive types, and this is what was holding me back for the authenticators.
**Tyler Yahn** 34:30 Yeah, I agreed. And I think you're right, like, I think that's… this is just looking for primitive types, I mean, as far as my read on this is.
So, I think, yeah, yours is even further beyond, so, yeah.
Okay.
… configuration SDK, create to accept programmatic SDK options.
**GZ Gregor Zeitlinger** 35:01 Oh, this is very much like authenticators, programmatic SDK options.
**Tyler Yahn** 35:09 Hmm. Yeah, I think you're… yeah.
**GZ Gregor Zeitlinger** 35:14 This is just the issue in a more general sense of…
But I have no idea how that could be supported. If we have an answer to that, then authenticators.
Might be a byproduct.
**Tyler Yahn** 35:27 I don't either. That's a good question.
…
**GZ Gregor Zeitlinger** 35:37 But here, this has a prototype.
**Tyler Yahn** 35:41 I… Yeah, so I think this is… this is a little bit different than…
Yeah, so this is specifically asking to throw in…
Yeah, in the create method for the config provider, yeah, this is… this is something that's outside of the configuration.
Is what this is doing. So this is saying, like, additional to whatever you get from the configuration, also provide these programmatic options on top of that.
So, it's not defined in the config.
**GZ Gregor Zeitlinger** 36:12 Hmm, okay, but we could decide that we want to support this.
**Tyler Yahn** 36:17 In the configuration, is what you're saying?
**GZ Gregor Zeitlinger** 36:19 Alright.
**Tyler Yahn** 36:21 Yeah, I mean, I think that's… that's fair.
I don't think that's what this is asking for. I think this is asking for a more generalized way to do exactly what this is doing, but I think that what you're saying is we could maybe try to extend the configuration to support this, and then this wouldn't even be needed in the create method.
**GZ Gregor Zeitlinger** 36:41 I think that's what I'm saying, but not 100% sure.
**Tyler Yahn** 36:49 This is also very… Go-specific right here. …
These options are very, like, defined.
in a way that are very… they're very go… like, I'd be very surprised if a lot of these options are universal.
Especially the way that they're named. So, that might not make a lot of sense to put this in the config.
I don't know if this actually needs to exist.
Cause I don't know if we want to… require…
Our programmatic setup of this configuration, …
Create method to actually accept these, but… Yeah.
That's a good point. That's a good question. It's a little different.
Than just having them to the… adding them to the configuration.
**GZ Gregor Zeitlinger** 37:34 It would certainly open a whole new can of worms if we did go down the drought.
**Tyler Yahn** 37:41 I… I think you're right. I don't know if we want to do that either.
**GZ Gregor Zeitlinger** 37:45 I added a new issue, which I forgot to do before, just for your information.
**Tyler Yahn** 37:54 … to the pressure.
**GZ Gregor Zeitlinger** 37:56 No, no, to our meeting notes.
**Tyler Yahn** 37:59 Oh, okay.
Alright, well, maybe we can just finish this up really quick, and then we can take a look at that.
So, missing environment variable for cardinality limits, this is another one I think Robert opened.
No, this is one that, EFJ has opened.
Yeah, I mean, I think the idea is to use configuration files for this, so I'm not exactly sure. This… I don't think this is blocking stability, again.
So, maybe we'll just… I think it's gonna leave in the no status.
**GZ Gregor Zeitlinger** 38:53 Yep.
**Tyler Yahn** 38:55 And then last up, the Add MTLS, client key password and certificate revocation configuration options for OTLP exporters.
Yeah, this looks very similar to what we were just talking about as well for this, additional exporter configuration parameters.
**GZ Gregor Zeitlinger** 39:20 I see.
**Tyler Yahn** 39:21 It looks like there's already a configuration and environment variable that we don't actually support.
Oh, wait, this looks weird. I don't think this is a defined….
**GZ Gregor Zeitlinger** 39:31 I would say it's different. This is something that can be based on primitive types.
And especially if there are environment variables for it.
**Tyler Yahn** 39:41 Wow.
Somebody really wants to put a password in their environment variable?
….
**GZ Gregor Zeitlinger** 39:51 I mean, you can, you just have to protect it, ….
**Tyler Yahn** 39:58 Yeah, …
Okay.
Yeah, alright, I think this is… this is another idea.
I…
I'd be very… I'd be very cautious about doing this, but … okay. I don't think this is blocking the stable release as well, so…
I don't think we need to discuss it further here.
Okay, Gregor, you wanted to talk about other… Issue, or another poll.
**GZ Gregor Zeitlinger** 40:39 Yeah, I just remembered, because you were saying stable, and I think this, … M.
Might, be needed for… stable. So the… the general, …
general section of the instrumentation section does not have known HTTP methods.
But, those are available environment variables, and I think we want to support everything that environment variables
support today.
**Tyler Yahn** 41:15 Yeah, that makes sense.
**GZ Gregor Zeitlinger** 41:18 Yeah, my first… my first, try was just, to add it directly here, and then, I discussed with, Trask.
to, make… a pull request to the SEMconf to add,
This setting and all of the other settings that are currently not specified
And the semantic conventions, so… For example, … Capture client, headers, …
Has an environment variable, and we have it in the… configuration schema, but…
We don't have anywhere where it's explained how the environment variable maps to the schema, and…
This is, what should be added to the…
semantic conventions. This is what Trask suggested, and I think it makes sense. Just wanted to get your feedback on that.
**Tyler Yahn** 42:23 It seems reasonable to me. Yeah, is there an issue in the semantic conventions for that?
**GZ Gregor Zeitlinger** 42:28 Yeah, I… I have… I think it's linked there, …
And it is currently only for the new setting, and… what I…
We'll do is add all the remaining ones there as well.
Yeah. And then, continued the discussion in the semantic convention.
… issue, and then also in the guild.
**Tyler Yahn** 42:56 The guild? We have guilds now?
**GZ Gregor Zeitlinger** 42:58 A semantic convention? No, that's a spec meeting, no, is it?
That's like… Working groups, sorry, not skills.
**Tyler Yahn** 43:07 Yeah, I… idea.
No, I… yeah, …
Okay, yeah, sorry, that sounds good. To me, I think that makes a lot of sense, yeah.
**GZ Gregor Zeitlinger** 43:19 Okay, court?
**Tyler Yahn** 43:24 Well, cool. Alright, I'm gonna stop sharing my screen here.
… looks like I'll get a drop.
**GZ Gregor Zeitlinger** 43:30 But….
**Tyler Yahn** 43:31 I'm still….
**GZ Gregor Zeitlinger** 43:31 To, to the, to our board as well.
Cause I think it's not on there right now.
**Tyler Yahn** 43:38 The issue that you just, mentioned? The ad node? Yeah.
Yeah, I just added it. Okay, cool. Alright. Yeah, I… yeah, sorry, I was doing that while you were talking. Yeah, yeah, it put it in progress, yeah.
**GZ Gregor Zeitlinger** 43:53 Correct.
**Tyler Yahn** 43:55 Cool. Any other topics people wanted to talk about?
Well, if not, I think we can end it here.
Thanks everyone for joining. Good to see you all. I will see you all in, I guess, two weeks' time.
**GZ Gregor Zeitlinger** 44:13 Have a great day!
