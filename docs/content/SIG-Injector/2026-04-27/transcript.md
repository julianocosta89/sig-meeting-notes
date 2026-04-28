SIG: SIG Injector
Date: 2026-04-27
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Nikola Grcevski @ Grafana / OpenTelemetry 00:02:35 Hey, Antoine?
Bastian Krol 00:02:49 Hey, folks!
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:50 Right?
Bastian Krol 00:02:56 Well, Ian, how are you folks?
Nikola Grcevski @ Grafana / OpenTelemetry 00:03:03 Sorry at risk last week. Ted and I were at a conference.
Ted Young 00:03:07 Yeah.
I think Google Next was last week, too, so I think a lot of people were up.
Nikola Grcevski @ Grafana / OpenTelemetry 00:03:14 Hmm.
Bastian Krol 00:03:15 Yeah, I think Michaela was at Google Next.
Ted Young 00:03:26 Let me grab my coffee.
atoulme 00:03:28 can work GitHub again.
It's up status… Nikola Grcevski @ Grafana / OpenTelemetry 00:03:34 Is it down?
atoulme 00:03:36 disruption.
Nikola Grcevski @ Grafana / OpenTelemetry 00:03:37 Right.
atoulme 00:03:37 Oh, man, come on.
up in, like, 3 PRs, and they don't show.
That's the first time this happens to me.
Okay, now it says there's no PRs? That's even better.
Nikola Grcevski @ Grafana / OpenTelemetry 00:03:55 No good to you.
atoulme 00:03:57 You've had this toast. Incredible.
Okay, alright.
That's it for today.
Ugh.
Okay.
Wait, we got?
There's all docs?
You have a dark face.
Bastian Krol 00:04:22 Cool, so should we get started? I see two things at the agenda. I guess we kinda need to wait for Michaela for the one that I just put there under Michael's name, which is, he wanted to… move the meeting, maybe, because it clashes with the, I think, the entity SIC or something?
Ted Young 00:04:44 You know, by 30 minutes, yeah.
Bastian Krol 00:04:47 Yeah, right.
So, he's there, he'll join later, is what he said.
atoulme 00:04:55 Okay, you wanna move it later?
Of course.
Bastian Krol 00:04:58 No, I think we should discuss it later, if we move it and where we move it, when Michael is also around, like, he said he'll join half an hour later, today, and then we discuss a new time slot. How does that sound?
Ted Young 00:05:15 Well, there's no entity SIG meeting today. It didn't happen.
Bastian Krol 00:05:19 It doesn't happen, so it should be here. Yeah.
Okay.
atoulme 00:05:25 I'm sure you'll be here soon.
Yeah, so…
Bastian Krol 00:05:29 Do you want to… Go first.
Nikola Grcevski @ Grafana / OpenTelemetry 00:05:34 Yeah, I just wanted to bring it up to attention. It's one of our graphonistas here that works on net.
That asked to help, with the .NET, checks, so I just wanted to bring up the PR. I reviewed it, I think Antoine is as well.
He's proposing, integration text in the tests in the next VR, so… I don't know if I think that's good.
Wanted to be one.
Bastian Krol 00:06:04 Not sure if there's too much to… so I didn't look at it, to be honest, but I mean, it already has two approvals, so… I guess it's good, Bob.
Nikola Grcevski @ Grafana / OpenTelemetry 00:06:14 Yeah, I think Michaela, put some comments, which they were addressed later. It was the difference between, I think, hotel… full or no-tel APIs should be allowed, so he made that change, and so should do it.
atoulme 00:06:29 You did? Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:06:32 Sweet.
Bastian Krol 00:06:33 Go ahead, Antoine.
atoulme 00:06:35 Did you make the change?
Nikola Grcevski @ Grafana / OpenTelemetry 00:06:36 Yes, yes.
atoulme 00:06:37 Okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:06:38 Yeah, he made the change so that it's only a conflict if it's the OTEL SDK, not.
atoulme 00:06:43 Oh, okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:06:44 the OTL API, so it should be good.
atoulme 00:06:47 Alright, alright.
Yeah, missed that in the first read.
Bastian Krol 00:06:54 If… I don't know the first thing about .NET and how things are built and dependencies are… but I mean, it's all statically compiled into one thing, so it's… that means if, someone builds an app with the OpenTelemetry API baked in for some custom tracing, and then we still inject. What about version conflict? So, if the SDK that we inject and the API version that is already there are not Of the same version that… Could be interesting, could it?
Nikola Grcevski @ Grafana / OpenTelemetry 00:07:33 Yeah, good fail. Yeah.
atoulme 00:07:36 I won't… It's fairly kept compatible, right, as far as I can tell.
I'm like, maybe there's a big change coming, maybe it would break things, but… Nikola Grcevski @ Grafana / OpenTelemetry 00:07:47 Yeah, I don't know how often they break the API versus this.
atoulme 00:07:52 Really try not to.
Nikola Grcevski @ Grafana / OpenTelemetry 00:07:53 Yeah.
Bastian Krol 00:07:55 Right.
atoulme 00:07:55 I've been trying to add, I've been trying to add one method to… to, counters and whatnot for the last 6 months, and some of it is just me being slow, but also, like, there's… and the burden of proof you have to bring to change any of this API is overwhelming. You go through the specifications first, the two PSCs, yeah, it's…
Bastian Krol 00:08:17 Yeah, then it should probably be good. I just… it just came to my mind, because I tried a similar thing with Python instrumentation, like, one or two months ago, where that's still in the Zero operator repository, where we auto-inject Python as well, and… There we also have these, custom site script, I think, that checks if there are any other Python OpenTelemetry dependencies already there, and that did not like if you had a different API package already in the app than… what we would bring, or at least I found some combinations that were not playing well with each other.
But I… I don't super remember the details, and I didn't look into it too deeply. It just sounded like there… if you allow that, then there's still an implicit tight coupling be… between what versions the application brings and what you inject, and that's kind of maybe then not even better than not allowing the API package at all, but if that's not an issue in your sense, then… Nikola Grcevski @ Grafana / OpenTelemetry 00:09:29 Maybe we should ask that on the PR, because the guys that join in on the PR, they would know the best, at least from the people that I know of. Maybe we should ask that question.
Will the… if the AP isn't compatible, will it break?
And is it better to go back to the previous change, where any of the related stuff was disallowed?
Bastian Krol 00:09:56 Yeah, maybe. I really don't know enough. Maybe it's worth discussing, quickly, and if they say that that's At least reasonably safe to do, then… I guess it's fine. I mean, we probably don't need to support, like, somebody bringing in a totally outdated API, or exotic use cases like that, but… but… It's… Nikola Grcevski @ Grafana / OpenTelemetry 00:10:21 Yes, amazing.
Bastian Krol 00:10:23 Yeah, cool, okay.
Ted Young 00:10:26 This is why we don't allow people to break the API in other languages.
Bastian Krol 00:10:34 Yeah, but I mean, even if you… If you'll make… compatible changes, and the API version in the app is newer, and you have an older… I mean, if we always update, then… and release in time, then that should be fine, but it could also be that way around, right? That it just has a newer API with a new method that we don't know yet, or something like that? I don't know.
Ted Young 00:11:07 I… yeah. I mean, I guess that's, like, a packaging issue, right? Like, what… what triggers us to do… To do a release, right? If there's gonna be gaps.
Bastian Krol 00:11:22 Yeah. Usually, new SDK versions should now trigger a PR, at least it worked once so far, automatically, so… I didn't see a new PR for the… agent since then, but it's also not been that long, but it should hopefully work, and then I guess we should also release it relatively soon-ish.
If you merge in new… Our instrumentation versions.
atoulme 00:12:00 New York.
Ted Young 00:12:26 Did anyone ping Michelle?
Bastian Krol 00:12:30 I can ping him.
atoulme 00:12:32 Didn't there.
Nikola Grcevski @ Grafana / OpenTelemetry 00:12:43 That's just a negative.
Let's see what…
Ted Young 00:12:54 We don't have any other injector-specific stuff. I have, Some questions around more at, like, the system packaging level.
If you guys have a moment for that, just throw.
Nikola Grcevski @ Grafana / OpenTelemetry 00:13:07 Trudeau.
Ted Young 00:13:07 get that.
project file. Like, one of the concerns is, you know, how do we… we… how do we, like, design the UI for that? And I think something we settled on is just using the current… what's currently available in declarative config.
And I wanted to see… What kind of limitations people might think are… could come from that approach. So, you know, the general layout would be, you know, you have… A package for each language.
And then you could… Within each language, configure, things using the declarative you know, YAML syntax that's already available in that language.
And we just say whatever's currently supported in that language is what's supported When you install it this way.
And then there's just the question of, like, you could also… have a meta package, open telemetry.
And that could just install the subpackages, but there's certainly things people would want to do that are, like, pretty universal, right? Like, there's the subset Of declarative config that should be… Supported across all the different languages.
So my proposal as, like, a first stab at it would be… like, well… that subset of declarative config you could put in, like, a more generic OpenTelemetry comp file, and it would just apply that to all of the Languages, and then you could overwrite it in each language.
Or fill it out with additional details. But basic things of, like, where is the… where do you want to send… what endpoint do you want to send OTLP to, right? And stuff like that.
It might be annoying to have to… Know which languages are installed in that environment.
In order to write down something that might be more universal and generic.
Does that seem like a reasonable… Starting place to propose For that SIG, or does that seem like kind of a strange way to start it?
Antoine, I know you guys have been doing this for a while at Splunk, so I was just curious how similar that is to, like, how you currently configure things.
atoulme 00:15:40 Yeah, we ship with different configuration as part of our stuff, and we have defaults that are enforceable, mostly.
You know, we're on an older version of the injector, which is based in C, where you have some config files with environment variables, that's how we config things. We… eventually, if the injector gets to the declarative config, it'll be also much more versatile than what you have. We have very limited options. We just open a few config files, and everything is just going to localhost 4317 without any failures. There's no… we use whatever is default. We haven't heard anything from customers complaining about Some lack of support about some configuration or whatnot, because it's… that's also why we think the injector and all those technologies are great, is we think that people are actually pretty happy with the defaults.
Ted Young 00:16:32 Yeah.
atoulme 00:16:32 no one came back and said, I would really want that really weird feature that no one talked about before. I'm like, no, it's never happened.
I would say, though, a little carve-out is… Node.js.NET, and Java. That's what we support in this C variant. We never tried or managed to support Python because of all the the funds that, you know, we… if you look at the zinc code for Python, it's very more involved, like, compared to what you have to do. And so maybe there's some Python features that I'm not aware of that… play. But in the most part, no, we never had to do… deal with any complexity there.
Ted Young 00:17:11 Yeah.
I think what I'm… I'm looking for specifically is, like.
you know, cutting scope from the system packaging SIG in terms of decision making, and it seems like the best way to do it, if we can just say, like, the conf… anywhere you're trying to configure OpenTelemetry, we have, you know, a config format.
that we've defined, and it's implemented to whatever degree it's implemented in whatever version of the SDK you're running in that language, but if all we're saying is, like, if it's system.
you're installing it this way, that… this is just where you put that comp file, and we're not really making any decisions as, like, the starting point. Like, we're not making decisions about what's supported, we're just saying it just passes it on through.
atoulme 00:18:01 Well, on top of that, if you were a vendor, you would want to overlay those config files, because you might want to turn some stuff on or off, based on whatever, like, it says this vendor does not support profiling, turn that off, right? So… We should really stay away from that. We, the point of view I have is that if we were to install the SDK, it should all be default values, which coincide really nicely if you also install the collector on the host at the same time.
So, we might go as far as actually making the collector required for the SDK at first.
error.
But that's… that solves for a lot of… it's, like… It makes for less trouble.
But…
Ted Young 00:18:46 Yeah.
So maybe that's, like, the only place… where we're looking at differences is, like, the defaults. Because I think, like, the defaults for the SDK, one, we don't have defaults for certain things, like, where do you send the data? Or the defaults are, like.
to maybe a different spot. Like, we have defaults, but they might… they're making potentially different assumptions.
than the environment.
you know, then, like, Kubernetes operator, like, where you would be sending…
atoulme 00:19:19 Yeah.
Ted Young 00:19:20 And then also things in terms of, like, timeouts and, stuff like that. I think the defaults in the SDKs kind of presume you aren't running a local collector, potentially.
So, it… That might be a place to explore, like, are the current defaults in the SDKs, like, the right defaults?
Read these days.
If they are, it's great, but…
atoulme 00:19:43 I think, I think… look at the… let me share my screen.
I will find it.
I know that the OTLP stuff is a separate page, and I can't remember what it is.
Jack Berg 00:20:01 Go back, I can tell you where it is.
atoulme 00:20:04 I mean, where it is.
Jack Berg 00:20:05 It's in the spec.
Spec drop-down? No, it's just, you can… you can… no, no, no, no, no, no, it's… it's… you can do it here. Spec drop-down down there.
atoulme 00:20:15 This one?
Jack Berg 00:20:16 Yep, Hotel 156, yep.
It's in… under protocol.
atoulme 00:20:26 Okay.
Jack Berg 00:20:27 And then, exporter.
atoulme 00:20:30 Alright, so, here, default's actually hard-coded to this.
Ted Young 00:20:34 Right.
atoulme 00:20:35 Yeah, it works. If you… if you have a collector, local.
open on that localhost port, you're golden. And this is maybe what we want to be doing by default, is like, you would want to have the collector local, so actually, we're just moving the problem one layer above, which is, yeah, your SDKs can talk to the collector.
And now what, right? What is the collector doing with that data? Drop it on the floor?
Right.
plane, sent to debug. I think we could send it to debug by default, and that'd be good, because that's what we ship in our default configuration, so if you were to look at the releases of the… Collector… Distribution… There is a config.yaml, which I think we store by default.
Now you can see we have receivers where we open all those ports. We're actually very liberal about this. We go to load any network interface, and the default Default pipeline is just doing this.
And I think, for all intents and purposes, if you were to just install everything out of the box, which is just, like, default config of your SDK, default config of your collector, you're going to have SDK talk to collector, collector, drop everything to standardize.
Job's done.
If you had something and you didn't want, and you actually wanted the collector to do something more than that, then it needs to be baked into this default config file.
And that's going to become the default.
Ted Young 00:22:03 And I think that's… I mean, that's sort of the… Where you would send… there is no default, really, for, like, where you would send the data out of the collector.
atoulme 00:22:12 Yeah, indeed.
Ted Young 00:22:12 For anybody.
atoulme 00:22:14 Yeah, unless someone comes up who's like, oh, I really want to have a… Some, you know, minified backend, or some… some… Demo-type thing, or… debug is just not cutting it, I would like to store it into a file, or, we're, you know, obviously open to any idea here.
Either way, the verbosity of the debug is detailed, we can also change that so it's less verbose. And right now, it's just, pretty much, you're going to open standard out of the collector, and you just get an inundation of data, because every possible signal just went from nowhere to being sent to your… to your collector on local.
So, it's not ideal, but it gets you where you need to be, and then the question is, go change the config file.
We could go somewhere.
I think that's fair, right?
Ted Young 00:23:03 Yeah, I… this is… Jack, I don't know how much you caught of the conversation, but I think the… I know your concerns around, like, the system packaging is like, hey, we need to make sure we're not… we're building something that… that people want.
And that's gonna work for everything, and just pointing out that maybe as the first version of this that we present to the community, we're basically not making any decisions when it comes to config. We're just saying we're gonna support the declarative… you write down the declarative config format, and the degree to which that's supported.
In each language, that's what you get out of the box.
For starters. Maybe with some degree of, like.
I don't know, for languages, maybe versions that don't support declarative config yet.
Just converting things into their equivalent environment variables, but… But not… not really… Trying to not put in anything there that looks like us making decisions that would be different from how you would do it in other environments.
Jack Berg 00:24:11 So… So I consider the operator, like, the Kubernetes version of what's being proposed in this packaging SIG for the Uber package.
And I don't find the operator, Working particularly well.
With its current config.
It's, I find… I find the… the design decisions around the config schema for instrumentation you know, they've kind of boxed themselves into a corner. I find that the versioning scheme for, like, how you select which version of instrumentation is going to be used, you know, problematic. They got themselves into trouble with… they were trying to be, like, the gatekeeper of quality and make guarantees that they were not in positions to guarantee.
And, like, largely, what… my concerns are about repeating that process.
for an Uber package called OpenTelemetry, and basically, like, the operator is the OpenTelemetry product for Kubernetes, and it's problematic, and I don't want to repeat those problems.
And so, I think the operator got into those problems because I didn't hear the operator folks coming to the spec sig and surfacing those problems for everybody.
Ted Young 00:25:25 Yeah.
So I guess I'm trying to de-risk this on two fronts. One is, like, all of this should be early and often in the spec sig, and also reaching out to end users and everything, right? Like, we shouldn't be making decisions and shipping them. But also, too, to what degree can… and this would also go for the next version of the operator.
Can it just be the same declarative config?
As much as possible.
everywhere, right? Like, it shouldn't be the case that, based on how the mechanism you're using to install this stuff.
changes the way you configure it. Like, ideally, there's… you can just learn there's one way to configure OTEL, And it… and it just works the same way everywhere. I'm sure there's edge cases and there's stuff that's, like, you get into with larger scale packaging, but…
Jack Berg 00:26:15 Yeah, and, you know, what you all were just talking about, you know, Antoine, what, you know, by the way, am I saying your name right? I'm gonna get that right. Is it Anthony or Antoine, or what do you prefer?
atoulme 00:26:27 My mom calls me Antoine.
he can call me Antoine, and you can put a W in there, and it'll be fine.
Jack Berg 00:26:35 All right, thank you for that. At least… I'll stick to that. I'm not going to get the pronunciation perfect, but at least it's not Antony, because I've heard people say that, and I don't know what to use.
atoulme 00:26:47 They took the I and they put it around. They can't understand why the O and the I are together in the name, and the name will be mispronounced until the end of time. Do not worry about this.
It's not you.
Jack Berg 00:26:58 All right. Well, anyways, like, what you said about, like, hey, the collector has this config.yaml, and it's, like, the reasonable default config, and, you know, we should ship that, and it's gonna be doing something stupid to start, but at least, like, you know.
atoulme 00:27:14 It's not pulling on the floor.
Jack Berg 00:27:15 It's not falling on the floor, and, you know, the process to update what the default is, is you update what's in this config.yaml, and so, like, you know, that's the forcing function to have the discussion for what the default is. Like, that's… that's… that's super reasonable. Like, I don't disagree with that at all.
But, like, you know, there's a variety of decisions of that form that, like, you know, need to take place. And there are things like, hey, what's the default around OBI and SDKs?
when do you install OBI to do the instrumentation versus SDKs, and why?
Profiling.
atoulme 00:27:57 You want both, really.
Jack Berg 00:27:59 You want both, exactly, you want both, but like, you know, I want that declaration of both, and the definition of, like, you know, one SDK and one LBI, it's based on, like, a language basis. I want that to be, like.
like, we're making that decision eyes wide open. Like, we're making the decision to use this config.yaml in the collector repo as the, you know, the definition of what the default is out of the box, to be eyes wide open. And, like, everybody is on the same page that this… this document, config.yaml, now is carrying a bunch more weight than it did before.
Because it's, like, our definition of what the default is for the OpenTelemetry product.
Yep.
atoulme 00:28:38 Yep.
Jack Berg 00:28:39 And yeah, that's… that's it. And, like, you know, so my, my, like, you know, reservations about this is, like, you know.
I just… I just don't see the maintainers of these components rushing to the table.
atoulme 00:28:54 Sorry, yes.
Jack Berg 00:28:57 They don't. They're not rushing to the table, and it's like, sure, I can represent Java, and I can make sure that we're gonna, like, you know, bring this dialogue back to the JavaSig and do that, but if it's not a priority for these other groups, we're gonna end up with You know, it's trying to, like, with this packaging group, trying to backstop, things, just like the operator did.
Ted Young 00:29:19 I think maybe that was the mis… take… going on, or that's the thing we don't want to repeat, like, it's sort of like… like, basically trying to go around the SIGs, right? Rather than go through them. And we want to be like, here it is, it's just using this new universal way of doing it, and if it's not a great experience in this language.
That means going to that language and improving it there, not going around them.
Jack Berg 00:29:47 Exactly, exactly. Like, I would want… I would want to, like, the policy to be, if something's not working in a language, you don't force it through, you stop. And you pause, and you force it, like, at the source, which is with the language, before you proceed.
If that's, like, the… if that's, like, the working model, then that buys us, like, you know, it buys us protection from, like, you know, making promises that we can't keep, and it also forces, you know, the maintainers of these respective groups to be, like, engaged before, you know, progress is made.
Ted Young 00:30:20 Yeah.
But I think it also gets things into people's hands, which was, like, the other part of the chicken egg, which is, like, if we ship a thing that that works as well as it can work without making these additional decisions for these groups, then it gets it in the hands of the maintainers and users, and then if it's missing something, or something's, like, not great, then that That… that creates more pressure on the maintainers to look at it.
And if we try to paper over that stuff and go around them, that's just the thing we don't want to do, right? We want to be like, here it is. It's… it's ex… extensible in each language, according to this standard thing, or if there's something missing from that declarative config, I think that's maybe the last piece, if we're like, oh, we don't have this concept in config, we're not sure how to do that.
Like, maybe around, like, enabling and disabling instrumentation.
For example, or… let's say, like, I have 3 Java apps, and I want them configured differently from each other. How do we do that? Like, we need to start mapping out Even if we're not solving those problems, at least mapping it out and writing it down so it's clear what it is.
What decisions have to be made.
But then trying to go to the right place in the community to make the decisions, not that we're gonna make it for them.
Jack Berg 00:31:50 So, this is the injector SIG, and, like, you know, this is kind of related to the injector, but it's also, like, a broader topic than the injector. Like, one thing that I've been wondering is, like.
what the injector sig really wants from packaging is it wants there to be a Java package, and a .NET package, and a Node package, and a Python package.
The injector doesn't care about an open telemetry package.
So, like, what's that?
atoulme 00:32:23 That is true.
Jack Berg 00:32:23 Yeah, so, like, you know, does this group need to care about the Uber package? Is this group, does it just benefit from just declaring these language packages? And… And, you know, I guess, why do we let ourselves… you know, I know we all wear multiple hats, but, like, with our injector hats on, why do we let ourselves get dragged into, like, you know, what the definition of the Uber package should be?
atoulme 00:32:47 Because our stuff is only useful if it gets installed, and it's really difficult to install the injector without some level of packaging.
Jack Berg 00:32:53 Not true. Everybody's bundling it with operators. So, while it could be used in a Linux capacity, most people are using it in, you know, Kubernetes operators capacities.
atoulme 00:33:02 But on Linux, there's no story, right?
Jack Berg 00:33:05 There's no… not a good story.
Ted Young 00:33:07 Yeah, but I also think this kind of circles back… well, one, the reason we're talking about it is we ran out of injector topics, and I'm like.
While I have Antoine here. While I have these people here, I'm trying to improve our system packaging proposal, so it was like, let me… please tell me I'm not crazy by proposing this is the way forward, because I want to get that stuff done. So that was why we're talking about it here. Once… we've got that SIG started, we can successfully ignore it here, and move all that conversation to the spec SIG.
Jack Berg 00:33:44 you know, just to kind of continue that point I was making, though, so, like, why does the injector care about the Uber package? So, like, you said there's no good story for Linux, and… but, like, if the in… if there are packages for each of the language auto instrumentations, Java.NET, Node, Python, whatever, and there's an injector package, like, sure, you don't have the Uber package story, but, like, if you install the injector package, that's a pretty good story. You're getting… you know, at that point, that, like, you know, you have a story for how you install SDK instrumentation on, you know, processes in a Linux environment. You're missing the collector, you're missing OBI, you're missing profiling or anything else we decide is relevant for the Uber package, but, like, it's not a bad story.
atoulme 00:34:30 Yeah, but now you're responsible for the SDKs you package, right?
Jack Berg 00:34:35 Again, that's why I want the maintainers to be involved.
Ted Young 00:34:39 Yeah, I mean, to be the… Sorry, go ahead.
atoulme 00:34:42 Well, ideally, then, don't… I mean, if… let's… if we dial your logicals away, the injector just installs the injector, and when it starts to say, I can't find any SDKs, so I won't do anything this round. Thank you for coming.
And then you're going to go and install the SDKs yourself, and I… I want to see that.
Ted Young 00:35:01 Yeah.
atoulme 00:35:03 That's the problem.
Jack Berg 00:35:03 Did that happen? I guess I didn't follow that.
atoulme 00:35:06 Following your logic. Let's say the injector says, screw all this packaging thing, this is way too much, let's just do the injector really well. And they make the injector really work well, right? And now we make the injector installable.
however you want, and it works. The problem is, we make the design choice that we're not going to install the SDKs with the injector, because, following your logic, it should not be a problem. It's not in our scope, right?
That means that, when someone installs injectors, then they have to go and install 5 other things by hand as well.
Jack Berg 00:35:38 Okay, no, I was saying something slightly different. I was saying the Uber package, the OpenTelemetry package, is not a concern of the injector. The auto instrumentation packages, the language packages are… and so, like, the injector package would have dependencies on the language packages, and it has an interest, a very clear interest in getting that result.
Ted Young 00:35:58 But still…
Michele Mancioppi 00:36:00 Certainly a dependency in the sense of a system dependency, because we decoupled that?
But there is definitely the need to work together with a shared contract.
Ted Young 00:36:11 And the way I see the Uber package, that's just, like, the default version of it has no special configuration, it's just, I'm lazy.
atoulme 00:36:19 Thank you.
Ted Young 00:36:20 just give me everything. And then, how you install all the different things are just… you know, you go into the different comp files for each bit, and you install it. Like, the only bit of configuration we'd want to look at there is, like, are there things that are universal in declarative config, for, like, the SDKs, for example? Or… It… is it not even useful, like, Antoine was saying, like, around the fact that the defaults just work, so… Maybe that's not even… maybe it's just a nothing burger.
But just, certainly, just having one that's just like, please just install all the bits for me.
That… I see that as kind of, like, the starting point, and then it's just, like.
is it annoying? Are people ending up in a place where they're copying and pasting config into, like, 5 different configuration files, and… Is there a way to eliminate Some of that by having a meta configuration file.
Or is there, like, additional stuff you'd want there?
Michele Mancioppi 00:37:26 The configurations are going to be… Mostly a matter of the, of the languages, and While there is some shared configuration possible in terms of resource enrichment, those, in my mind, they live in the collector to sit nearby.
Ted Young 00:37:48 Yeah.
Michele Mancioppi 00:37:49 most of the things that I would configure at language level they are language-specific, like, the number, like, by far, by far, the most important one is which instrumentations I want to turn on and off.
Right. That are language dependent.
Ted Young 00:38:05 And… and that's something, I think, getting back… Jack… has concerns that I think are valid around the operator SIG essentially front-running the language SIGs and making decisions for how to manage some of these things, and, like, that didn't work out that great, and just… Wanting to say that our approach is, like, we're not going… if… if… a language doesn't have a good way to configure this stuff. It's our job to go to that language and improve things there with those maintainers, not to come up with our own way of doing things that kind of goes around them.
And as long as we're doing that, and then we're, like, being very public early and often with end users and the specsig, I think, to me, that feels like we're de-risking the system packaging SIG from repeating the mistakes of the operator SIG.
Michele Mancioppi 00:38:59 I mean, that was effectively the reason why I was so vocal about asking for serious involvement of the GCNTC, because…
Jack Berg 00:39:07 Yeah.
Michele Mancioppi 00:39:07 This is a moral suasion on the language 6.
Jack Berg 00:39:11 And maintainers as well, GCTC and the language maintainers.
Ted Young 00:39:15 Yeah. But, you know…
Michele Mancioppi 00:39:16 My point is, chances are that GCNTC managed to Be much more listened to.
From the maintainers of the languages than, peer maintainers.
Ted Young 00:39:31 But… but it's… it's about making sure we don't… like, getting open telemetry across the board, even if we had a bunch of GC and TC involvement, like, that's… it's like… that's just, like, not an option that's on the table, right? Because every language is in a different state, has different priorities, it's just… being like, we're all gonna do X this quarter is, like, clearly… it doesn't even matter what X is, like, that's just not… a great model for trying to get things done in such a big project. So we just want to make sure with something like system packaging, we aren't.
atoulme 00:40:06 I didn't come up with a blog post that said we're going to move to a product vision in November last year, right? A GC did. So, what is a GC… freaking, like, why am I talking to you about this? This is not particularly interesting to me. The GC made a commitment, go and deliver. Why am I involved in this discussion?
What are you doing?
Ted Young 00:40:30 What do you mean? What do you mean?
atoulme 00:40:32 I think there's a blog post from November that said that, OpenTemmetry will not work as a product, and will commit to stable stability by default.
Alright, well, how about you guys, you know, go execute, because I'm here trying to help.
And I don't understand.
Ted Young 00:40:51 Well, I think it's what it… we… this is something very important to me and other people in the DC, and it's required for graduation, and it's coming out of what our end users are asking of us, right? Like, they want things to be stable, they want the data cleaned up, and they want an easy way as operators to be able to install and manage these things.
Where they don't have to go in and touch. That is, like, the highest priority from our user perspective. But what we're learning is, like, you can't just go in and be like, we're gonna do this everywhere. So we have to find a way to build the pieces we need, right, like the system packages and the injector and stuff like that, and then find a way to go into each language and kind of help them Do what they need to get that stuff.
Michele Mancioppi 00:41:41 To be fair, the reason why, I felt the time was, was nigh to do system packages is because With the declarative configuration, getting into a stable enough place, That was the biggest hurdle.
To… to deal with the entire shenanigans.
Ted Young 00:42:02 Yeah.
Michele Mancioppi 00:42:03 not… as long as the language has a decent support for the accredited configuration language, I think we're going to do fine. Yeah. And be able to… In the beginning, to… kind of… Make up for the lack of stable by default, with some conservative configurations.
In, the language system packages, and then, use that.
And I…
Ted Young 00:42:30 Yeah, and it's quite clear that the biggest bugbear here, and why stable by default is actually, you know, we tried to use that as, like, maybe a piece of cheese to get people more interested in this, but that backfired, right? Clearly, it's much better to just decouple all of these things.
atoulme 00:42:48 People don't care about that. They just want things to work.
Ted Young 00:42:51 I think the bigger issue isn't even not caring, it's just that, the… we don't… we don't have the labor available to go in and do massive amounts of work in contribib and all the different languages, right? That's actually… so if we're gonna say stable by default is really about the instrumentation packages, that's actually… a trickier thing that I'm trying to work our way through, but in the meantime, we don't want to block this stuff. We want to have this stuff in and available And then, like, you're saying, Michele, like, for each… have something in declarative config defined for, like, how you enable and disable packages, try to get that working in the different languages. And then, at the tail end of all of this, once we've figured out how to wrangle contrib.
Maybe later we could come out with different, you know, maybe you say, install OpenTelemetry-stable, and you get something… for lazy people who don't want to splat in some giant config thing. Or we figure out some other way of doing it, but I'm saying we punt on.
Michele Mancioppi 00:43:56 It's not, yeah, it's not gonna be with a suffix, because system packages have their own tracks to use in these cases, but it will have something to that effect.
Ted Young 00:44:08 Whatever it is, it's like, we have such a bigger hill to climb collectively as a project around getting instrumentation stable that that's… It… that's… just needs to be decoupled from what we're doing in system packaging.
Michele Mancioppi 00:44:24 For example, I can tell you that having stable by default is necessary if you want our packages to land in Ubuntu and Debian Main or Universe.
Probably universe, but still, they need to be default… stable by default.
Okay. I'm not getting phony, otherwise.
Ted Young 00:44:41 Alright. Well, I'm gonna, Try to update that project file to represent and clear up some of this stuff.
Michele Mancioppi 00:44:53 Yeah, I mean, I feel that the projectile is in a rather good shape.
It does say this kind of things, if I recall correctly.
Ted Young 00:44:59 Yeah, I think just getting a little more specific about declarative config, and just making it clear that we aren't… Like, around where we expect some of the decision-making.
to happen, that we're not going to solve these things for the languages, we're going to provide the framework, and then, like, things will work as well as they do for each language, but that's certainly for the first phase of this thing, it's just figuring that out and also mapping out for each language. I think the other thing we want to do in that SIG is actually identify what's missing in each language, and making sure those SIGs know about it.
Jack Berg 00:45:35 I want an overindex on declarative config. So, I was, I was working on a branch to incorporate the injector into the operator, and, like, proposing a new CRD structure for, you know, a centralized definition of what you want to instrument and what its configuration should be, just the ideas that we've been talking about. And, you know, the centralized definition was a series of rules, right? So, you know, each rule has a predicate, like a matching predicate, and then if that matches, what the config is.
And how do you want to express the config? Everyone says declarative config, right? Well.
that's… I think that's, like, overly restrictive. Like, environment variables work just fine, and are, like, really terse in, like, a lot of cases, and meet languages where they are. And so, I think what you ought to do is something like Either or, but not both.
like, you know, just provide faculties to, you know, say, like, hey, I want to configure all the SDKs installed by the injector to, you know, have this set of environment variables declaring them. Or, if you need the richness of declarative config, you know, point to a config file, and, you know, it's stable and supported in a bunch of languages. But I don't know why you kind of take environment variables out of the equation. They work and are good in a variety.
circumstances.
Michele Mancioppi 00:46:55 Let me tell you why, because actually… going and setting environment variables on, for example, SystemD units, other packages. Most of the software installed that is going to be instrumented is going to come through other packages where you do not really have good ergonomics.
To go and modify the process environment, that's a huge no.
Jack Berg 00:47:18 Wait, wait, which types of things are you talking about? Because the injector, we can do this. We have a file where you can set environment variables, which we inject into every process.
Michele Mancioppi 00:47:27 Yes, but it's… it's obscure, it's obtruse, it doesn't feel right. It doesn't feel… The line axe.
We could pull it off like that, but then, what do we do? Go and create templates for all the possible languages of the variables?
Or we actually say, this is for Python, and then you put in there the obvious things, right?
Speaking of the quality config, it feels right.
Jack Berg 00:47:54 Well, so, you know, you're not going to get any pushback from me about declarative config. I'm obviously the biggest champion of it. I just think, like, diplomatically, it's a hard sell to say something like declarative config is the only approach.
Like, there's a lot of people that are still pro-environment variables, and so, like, you get more people at the table if you can accommodate all of them.
Ted Young 00:48:16 I guess what I would like to see is, like, in terms of building new interfa… like, it's… whether it's turned into an environment variable later, you're still writing YAML or some config somewhere, whether it's the operator.
Jack Berg 00:48:30 Yeah.
Ted Young 00:48:31 Or package, right? And I would just like it to be, like, that interface, could we just standardize on what declarative config looks like? And if under the hood, that means some stuff has to get converted into environment variables to work in, like, older versions of things.
Like, I could see us doing that, but I would prefer that over us, like, exposing… The old environment variable stuff.
Jack Berg 00:48:58 I just think if you update the packaging project proposal and say something like, declarative config is the only way, you're gonna get people raising their eyebrows. And you're gonna get… that's gonna be a point of contention. So, like, you don't need any more points of contention.
But it…
Ted Young 00:49:12 But, like, what do you think about saying, like, the structure of these configs is declarative config and… And if, as, like, a temporary measure, you could…
Michele Mancioppi 00:49:23 We cannot, but that we cannot implement declarative config in the chat.
And then map that to the variables.
Jack Berg 00:49:29 No.
Michele Mancioppi 00:49:30 Different SDKs, that's not happening.
Ted Young 00:49:32 That's not happening. Okay.
Michele Mancioppi 00:49:33 It's in public.
Ted Young 00:49:34 Okay.
So then it needs to be a mix, then, of saying, like, declarative config, or you can set Environment variables, and we have to figure out a way to… To… to make that feel not bad.
Jack Berg 00:49:48 It doesn't feel bad. I don't agree with Mikel. Like, I think, you know, you have this file in the injector that you can put key-value pairs of environment variables and values, and those will be injected into every process that's started.
And, you know, it's reasonable to, you know, have a sort of… template file with all the environment variables that you would care to set, like the standard set of, you know, OTEL, you know, OTLP endpoint, and those things, and have those point… set up for, you know, good defaults.
Michele Mancioppi 00:50:22 ETLP endpoints are not necessarily the biggest problem, although… There are inconsistencies in the, in the way that URLs are handled, especially for gRPC, which are going to be mighty painful.
My biggest concern about environment variables is the turn on and off of instrumentations, because some SDKs will break if you tell it to turn off an instrumentation that doesn't exist for them.
Jack Berg 00:50:51 And this… Yeah, and they don't have, to your point, they don't have standard ways to… standard environment variables to do that. So that… that hasn't been standardized yet.
Michele Mancioppi 00:51:03 I mean, my fixation and over-indexing on the graphic config is 99% turn on and off instrumentations.
Jack Berg 00:51:13 And my understanding is that that has only really been embodied in the Java agent.
Have the other auto instrumentations that support declarative config, added capabilities to turn on and off instrumentation in the standard way?
Michele Mancioppi 00:51:29 I… assumed that was the case.
And what I assume, is doing a lot of lifting.
Jack Berg 00:51:35 Yep.
Michele Mancioppi 00:51:36 I mean, the hoop's over.
Jack Berg 00:51:38 You know, to your point, though, they definitely could, right? Because it's Greenfield, you know, that could be, like, a gate, right? So, like, you need to… you need to add support for this.
Bastian Krol 00:51:50 So, we have 9 minutes left. Should we discuss the new time slot? I had to break up the discussion, but if we want to do that this meeting, then we should do that.
atoulme 00:52:00 Good.
Bastian Krol 00:52:01 now-ish.
Jack Berg 00:52:03 But this conversation is open-ended, and, you know, as we've talked about, sort of is beyond the scope of just the injector SIG.
Michele Mancioppi 00:52:10 Yeah, very helpful story.
Ted Young 00:52:12 We're getting the other cig off the ground.
Michele Mancioppi 00:52:13 One last point.
I am unclear on the status of the packaging sick. Is it, yes? When, don't know…
Jack Berg 00:52:23 Ted is your champion here. Ted's trying to, you know, like, hurdle the cat… herd the cats behind, you know, the scenes to try.
Michele Mancioppi 00:52:32 The answer is not yet, but hopefully soon.
Jack Berg 00:52:35 Yeah.
Michele Mancioppi 00:52:36 Good.
Ted Young 00:52:37 Yeah, we're just spread very thin, and a lot of what I'm doing is just trying to make it clear to everything that this project is de-risked, you know, and Jack's been doing a good job of pointing out all of the risks, so hopefully very soon, is all I can say.
Michele Mancioppi 00:52:55 For example, I came up from the core of the CNTC thinking, we kind of made it.
And, but now I understand this, not yet.
Ted Young 00:53:05 It's… it's just… yeah. So… But I think we're… we're on the cusp. It's just… We gotta… get… get some more buy-in, but I also plan, regardless whether this is what state it's in to continue using spec meeting times to… the conversation we were just having, basically moving that to the spec SIG, which is where that conversation should be happening.
Both in terms of getting that SIG off the ground, and even once it's off the ground. That's just… we need to be.
Michele Mancioppi 00:53:38 talking better.
Ted Young 00:53:39 every week.
atoulme 00:53:40 So, so now we know.
Michele Mancioppi 00:53:40 Should we start attending the Spec Sig as well?
atoulme 00:53:45 I mean…
Ted Young 00:53:46 Yes.
atoulme 00:53:47 It is possible, yes, but, you know, your time is… I personally am struggling. The time slot of 8 AM on Tuesday, let me tell you, it's very in demand.
Yes. Yes.
Ted Young 00:54:00 I don't think everyone needs to be there, but I'm just saying we need to be engaging with the broader community and the maintainers, right? Like, we need to be… Not making decisions in a vacuum.
So…
Michele Mancioppi 00:54:16 Let's response attending.
Ted Young 00:54:18 Yep.
Let's start, let's get back to, meeting times for this one. You want to move.
atoulme 00:54:25 So, showing my screen here, you can see that this is the week of calendaring.
every week is a little different, but that's what it looks like. So, right now, we have, conflict with Entity SIG, on Mondays.
Which conflict would you like?
To do is the most.
Michele Mancioppi 00:54:45 Entities is near and dear to my heart.
atoulme 00:54:47 How about, how about, Thursday 8 a.m?
Bastian Krol 00:54:53 good for me.
Michele Mancioppi 00:54:54 What time is it in Europe?
Bastian Krol 00:54:56 It's 9… 9 hours.
So it's 5 o'clock in the afternoon for Europeans, if you, if you say 8 a.m.
Think.
Ted Young 00:55:09 One thing is… By the way, it looks… your calendar looks different than mine. You have entity SIG and the injector SIG starting at the same time, but…
atoulme 00:55:17 Yeah, I'm just playing with different weeks.
It looks like, until now, entity seek was 9, and it just moved it to 930.
For next week.
Ted Young 00:55:29 Oh, oh, oh, I see. I'm looking at an outdated thing on my calendar. Okay, thank you.
Michele Mancioppi 00:55:33 Well, that's fine. I have a perfect overlap.
Yeah.
atoulme 00:55:38 I'm using the web calendar from the community repository.
Ted Young 00:55:42 I see that. Okay.
atoulme 00:55:43 I don't trust anything at this point. So, okay, so I will take on the action item to open a community issue, where I will request that we move this meeting from 9.30 on Monday's PST to 8 a.m. Thursday's PST.
And that will be the ongoing slot starting next week. Is that good for everybody?
Alright, okay, okay, I did, will do. Thank you, thank you for that. Awesome.
Look, for this conversation that we're having that's ongoing, I think we have a lot of disconnects, and I've talked about it with Tigran a little bit, and I would resume the… I would sum up the conversation I had with him was, Tigran said, I do not want to piss off maintainers, and then I told Tigran, I'm a maintainer too. What do you mean?
So I'm not sure, at this point, who is the Zay, we keep on referring to about the poor maintainers who are about to, you know.
do wrong to. Clearly, clearly there are a lot of people around, and I don't know everybody, but no one has come out from the rust siege and say, you know, put their stick on the ground, say, I hate everything you've done so far, and I don't like that you're making decisions for me.
No one has either had the energy, which is Clearly, a possibility for this.
or the where result to say, actually, I have a better way to do it, or I don't want to go throughout this future of how we build this thing for OpenTeometry. So, is the GC, when they build the blog post and the view, and the perspective, and the roadmap towards stabilization and having a product approach.
I believe the GC did a proper job of reaching out to everybody in the community.
The blog post was debated for months.
there were over, like, 100 comments on this thing. Like, it was just on and on and on.
And eventually, it got shipped out, not because we care about it, but because we had to also show to the community in the TOC in particular, and we want to graduate, and it has to be these guarantees in there. Yeah. So, for me, the shape of whether we want to have a product approach to things has sailed a while ago.
I don't understand why we're having those discussions. Now, there's no enforcement from GC, I think I'm catching on to that.
And the GC is a body of people who just… what do you guys do? Like, if you don't have enforcement, and you can… what are you… you're trying to bring the horse to the water?
Ted Young 00:58:04 It's open source, right? This is how open source works, right? We don't pay people, we can't, you know… to some degree, you can fire people, right? But, like, mostly you need to use carrots, not sticks, in open source.
atoulme 00:58:17 There's tons of cards at your disposal, like, making it part of the standard Ubuntu system packages…
Ted Young 00:58:23 Yeah.
atoulme 00:58:23 Whoa, look at you, you're being adopted.
I mean…
Ted Young 00:58:26 The main thing… well, one, maybe using the term product-oriented approach is just confusing to people. Like, I…
atoulme 00:58:35 Like…
Ted Young 00:58:36 It's more that things need to be packaged… things need to be… as I said before, like, what the users really care about right now is they want things to be stable and up to the latest version of the semantic conventions, and not beta anymore, and they want a way to be able… various ways in the different environments where they use OpenTelemetry.
To be able to install and maintain it at scale.
Right? Where you don't have to go in and, like, touch every single thing. You have some way of being able to more broadly do that. I think that's where the product language was coming from, but it's just about trying to get that stuff done.
And the biggest issue we see right now is we don't… maintainers feel like, in a lot of SIGs, like, there just aren't a lot of maintainers.
Right? And especially when you start talking about instrumentation and contrib, that's the places where we're like, well, we don't have, like, this big pile of maintainers for that. We have SDK maintainers, but the SDK maintainers don't want to be told, now you have to go maintain a whole bunch of Stuff you don't have time for.
atoulme 00:59:46 I mean, we can't create capacity out of nowhere, and I think… Exactly.
Ted Young 00:59:50 Exactly.
atoulme 00:59:51 I mean, if you want to take an example of something that didn't work is Collective, for example, had a very small core team, and kept going for years and years, and then eventually failed because they were not able to build a community. So you need to make it installable on people's laptops so that they will feel like they want to help.
Ted Young 01:00:07 Right.
atoulme 01:00:08 And if we're not doing the work of making it available to people, then there's not going to be a virtuous cycle of people adopting it, and there won't be contributors.
Ted Young 01:00:16 Today.
atoulme 01:00:17 Why don't we… what do we…
Jack Berg 01:00:19 I disagree a little bit with that, like.
the, you know, the virtuous cycle creates more contributors. I think I think it's a tragedy of the common's going on, where there's lots of companies that are benefiting from OpenTelemetry, and you know, they're trying to get away with contributing as few full-time maintainers as possible. And so, like, in one sense, approving more projects when the contributor bandwidth doesn't support it, it doesn't… it doesn't… it won't create the more contributors to solve the problem. It just spreads us thinner, increases our WIP, and makes us less effective at, at delivering the things we say we're going to, you could… a different approach is to gate the work in progress and say, we're not going to start new things until we finish what we've already done, and use that as a forcing function for vendors to contribute more maintainers.
Michele Mancioppi 01:01:12 And I can tell you something, something more.
If you think that you… that you now have too little contributors, when… wait until open tele is declared stable.
And then see everybody else.
atoulme 01:01:23 My management's gonna jump on that like hot pancakes.
We're done here.
Michele Mancioppi 01:01:27 No, we don't need to invest anything anymore.
Jack Berg 01:01:30 It's done. Problem solved.
Ted Young 01:01:33 So that's… that's the real thing, like, we're… when… and, you know, I didn't want to say it, but it's like, the contributors we're looking for for this stuff are not end users, right? It's… it's vendors. What?
Realistically.
atoulme 01:01:45 equally.
Ted Young 01:01:46 Long-term maintenance. You can expect long-term maintenance from end users for some of this boring-ass.
atoulme 01:01:52 So, I think the people who are actually having to run this thing are going to care about it a lot more than vendors would.
Michele Mancioppi 01:02:00 No, that's the one. If it's broken, they're going to migrate to something else.
atoulme 01:02:05 Yes, sure, I'll stop running it, yeah.
Ted Young 01:02:08 But… but you're… you are correct that, like, as OpenTelemetry becomes more stable, like, vendors want to… to not replace the resources that they've currently put into it, and certainly don't want to expand that, but, so we have to also look at ways to, like, lower the cost, especially for Contrib.
atoulme 01:02:31 I think vendors are terrible maintainers of open source code. They have no vested interest making things better, they want to keep the status quo.
Ted Young 01:02:39 You want to get more?
atoulme 01:02:40 Oh, you'll lose.
Ted Young 01:02:41 It's garbage in and garbage out, so if the data sucks.
you know, they'll care about improving it. But anyways, we're over time, and this is well out of scope for the poor injector SIG.
atoulme 01:02:57 Alright, bye. Take care.
Ted Young 01:02:59 Yeah.
