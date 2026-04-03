SIG: Java Declarative Configuration
Date: 2026-04-02
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Jack Berg** 02:38 Hey, Gregor.
**Gregor Zeitlinger** 02:45 Hi, Jack!
**Jack Berg** 02:49 I would be surprised if Trask came today, considering he said he wasn't feeling well, so, What are you thinking?
**Gregor Zeitlinger** 02:57 Oh, I didn't, read that, I don't have much, I just wanted to, inquire about some very old PRs, do you have something?
**Jack Berg** 03:12 I have a PR that, I just opened yesterday.
it's in the core repo, and I'm trying to clear the road for, this task of, like, figuring out where the declarative config, components live as, like, their final permanent home, right? Because they live in this SDK incubator module right now, and, that's not the right place.
And, you know, the first step in moving them somewhere else is, is breaking this dependency, where the SDK incubator depends on the auto-configure module, because we use some functionality from AutoConfigure, like SPI Helper and, this other we reused the piece of auto-configure that does resource environment variable parsing, you know, OTEL resource attributes. So yeah, had to break that dependency, and then, you know, that would kind of clear up the next step. So I can point to that PR.
**Gregor Zeitlinger** 04:19 I remember, that I also had some fun, trying to stitch some pieces together when working on, Some parts of the declarative configuration and, I'm sure you have that on your radar, but it was quite difficult for me to get that working at the time. I think it was auto-configured and declarative configuration, and incubator, this combination that made it difficult.
**Jack Berg** 04:50 Yeah, exactly. There's, like, a sort of cyclic dependency between them, where auto-conf… where… Auto-configure depends on, declarative config, or the incubator, using reflection.
**Gregor Zeitlinger** 05:03 Right.
**Jack Berg** 05:04 the incubator depends on auto-configure via, you know, an actual dependency, and, you know, they… we can't… we can't have that. We can't have, you know, both things depending on each other, and, you know, where that kind of shows up most, and I know that you wrote this code, but, There's, like, this incubating utils, and there's a bunch of hoops that we're jumping through.
**Gregor Zeitlinger** 05:26 be able to do.
**Jack Berg** 05:26 do reflection, and we really don't want to do reflection. We really want, like, a compile-only dependency on the incubator stuff, on the declarative config stuff here, so… my PR breaks the dependency and allows Auto-configure to defend… to depend on the incubator with a compile-only dependency, so that all this reflection goes away.
**Gregor Zeitlinger** 05:53 Compile only. And I think I was confused in the past about, if that is, According to our stability, but I think you said it is for some reason, I forgot it again.
**Jack Berg** 06:07 Yeah, we do this… we do this in a couple of places. So, we can take a compile-only dependency, but, the… like, take the SDK, for example. It has a compile-only dependency on the API incubator, but the SDK needs to be able to work completely without the API incubator being present.
And so, you need to kind of jump through some hoops to, sort of at runtime, detect if the compile-only dependency is present, and if so, trigger the additional behaviors. And the way that that shape that that looks like is, like.
is, you know, over an auto-configuration SDK builder, it's like this. You know, we do a little static initialization block where we detect if the certain class is present, and, you know, if it's not, then, you know, this will behave completely fine without that dependency being there.
**Gregor Zeitlinger** 07:01 Oh, now I remember, what I wanted to talk about.
Trask has done some good work in the agent to document those patterns, and now he's trying it out with AI to see if it's really working.
And, I was wondering if you have something like that, too, so that it becomes easier to work with those patterns in the future.
**Jack Berg** 07:27 I don't today, but I am interested in this. Like, I like… I like what Trask has done, maybe it's in…
**Gregor Zeitlinger** 07:37 It's in a different repository, not a directory.
**Jack Berg** 07:41 agree.
It's not example.
**Gregor Zeitlinger** 07:46 Yeah, something with Copilot in the path name, maybe you can look for that.
Maybe under GitHub?
**Jack Berg** 07:56 Yeah, agents, yeah.
**Gregor Zeitlinger** 07:58 Alright.
**Jack Berg** 07:58 It's like this knowledge directory, yeah. I really like this in here, where it's like, you know, he has… He's kind of creating a dedicated, sort of, file for each of the sort of idioms, patterns that you do.
with explicit examples, and I know it's tailored at AIs, and I'm fine with that, but, like, it would also be great for a human trying to understand how this compile-only dependencies work, like, how we justify it and things like that. So, like, in the core repo.
the best, like, we've been getting away with, I would say, like, kind of encoding a limited subset of that knowledge and contributing that MD.
There's a section down here, which is, like, best practices we follow, and.
**Gregor Zeitlinger** 08:46 It's like…
**Jack Berg** 08:47 Like, it's really short, right? It's just a series of bullet points, and we have way more best practices that are sort of undocumented than are listed here.
**Gregor Zeitlinger** 08:55 Alright.
**Jack Berg** 08:56 I like Trask's idea of somehow breaking that out, and maybe having, like, contributing somehow be, like, an index that points out to other files where we kind of elaborate on each of these best practices.
In more detail.
**Gregor Zeitlinger** 09:09 Yeah, if you want, we can also do, like, a… session together, to see how far we can get, or do you want to do it on your own, or should I take a stab at it?
**Jack Berg** 09:26 I'm… I'm in… I don't have opinions on that, like, like, I think there's been some people volunteering in this repo on issues to be like, hey.
can I go take care of this type of task? Like, the documentation of a best practice, and there's, like, it's new faces, new names I've never heard of before, and so, like, I don't think… I don't think it's necessarily the right thing for a complete, newcomer to the project to start doing that, but, like, if you wanted to do that, I'd be… I'd be all… all on board for that.
**Gregor Zeitlinger** 09:59 No, I'm trying to get at something different.
**Jack Berg** 10:02 Oh, okay.
**Gregor Zeitlinger** 10:03 So… I have worked with AI a lot, and I don't know how your mileage is, so what I was trying to offer is, if you want, we can do it together to… so you can see how I work with AI.
**Jack Berg** 10:18 Sure. Sure.
I'd be… I'd be happy to see that.
I think I have an idea, but, like, yeah, I think, you know, we don't, we don't do enough pair programming.
**Gregor Zeitlinger** 10:35 Yeah, cool.
Maybe we have even time now, but I also have another thing that I, Just remember, that I wanted to talk about But let's close first what you were explaining before we start something new.
**Jack Berg** 10:56 So just, just this PR. This is one of the… this is the only thing I have open in the, in the declarative config world right now, is just… I'm starting to set my eyes on finding a permanent home for these components.
So that we can get on the path of, like, having, stable modules that we publish with, you know, stable APIs at some point, so…
**Gregor Zeitlinger** 11:22 Huh?
**Jack Berg** 11:24 This is the first step along that path. That's all.
**Gregor Zeitlinger** 11:28 Okay, yeah, can you just send me the link? Then I don't forget about it.
**Jack Berg** 11:34 Yeah.
**Gregor Zeitlinger** 11:37 I also have, on my… plans for next quarter to do more code reviews, and I want to use the Java SDK as like, the first one, where I want to do that, but I'm still… Finishing up things, so, Until then, it's still good if you send me, It links explicitly when I should take a look.
**Jack Berg** 12:07 Yeah, didn't you say that you, you created or found some good tooling for doing, sort of, kind of workflow tracking or notification management with, like, GitHub.
**Gregor Zeitlinger** 12:18 Yep, I'm actually building that on my own, and I thought I had it in a pretty good shape, like, before my vacation. Then I came back and I saw that it was all in shambles, because, once I fixed a small thing, then more, more broke, so I spent the better part of this week to get it in a good shape, so I delayed my plan to share it more widely until those things are sorted out. But I can show you how it's working for me.
**Jack Berg** 12:56 Yeah, because that's, like, one of the problems I find. I just… I just know you were talking about, doing, kind of, code reviews, is, for me, there's kind of a lot of repositories that I'm a team I'm on a team for, and so, like, I automatically get notifications about them, and I can't… I can't unsubscribe without actually, like, leaving the team.
And so, like, I get a notification, for example, for, like, every single, every single PR in the instrumentation repo, and probably, like, two dozen other repositories. And so, that's a lot of noise, and then there's a lot of noise in, Renovate. Jeez, like, renovate is just out of control.
**Gregor Zeitlinger** 13:39 Yeah, exactly.
Maybe I can show you what the configuration looks like, because that's only a small part, Where is it? Here.
So, it has configuration that's independent of GitHub for this, particular reason. So here I have maintained repositories, which means I want to know about basically everything, and then I have some review repos, and you can see that this is because I want to do more code reviews once this is working.
And then, in addition, it has more, so that it… Also has, like.
I want… oh, see, there's something outdated here, but it also has an expertise filter so that it can also pick A couple of, issues.
from the… Vast sea of issues in, a lot of repositories that I get notifications for, but when it's Prometheus Interop, then I want to know about it.
**Jack Berg** 14:48 Exactly. This is the same type of thing I'm trying to do, and somehow GitHub has not solved this yet, with their notification system. I want to be able to, like, you know, select a set of repos and be able to filter out, sort of patterns for issues or PRs that I know are noise, like, renovate in this case. Like, if I'm gonna do renovate work, I'm gonna, like, do it all at the same time, and I don't want to be, like, notified about it. I want to, like, go… You know, set aside time to go and do renovate.
**Gregor Zeitlinger** 15:22 Yeah, this is all… this is one of the tweaks that I have added there. It groups the renovate things, and you can say, bulk approve, and then, You don't have to deal with every single one.
**Jack Berg** 15:36 Nice. Well, I'll be watching this, I'll be looking out for when you think this is ready to share more broadly.
**Gregor Zeitlinger** 15:43 It is not, but if you want to give it a try, I'm actually looking to have more feedback, so I'll just send you the link for that, and then you can try it out.
**Jack Berg** 15:53 Is it… is it cloud-based, so I just need an anthropic key?
**Gregor Zeitlinger** 15:57 Yeah, actually, it's only for Claude, even though I have in mind that it can be extended, but it has so many features that I don't want to branch out, unless I have to.
**Jack Berg** 16:09 Yeah, yeah, have at least one part of it be, sort of nailed down.
**Gregor Zeitlinger** 16:16 Right.
Okay.
**Jack Berg** 16:19 Thanks.
**Gregor Zeitlinger** 16:20 Let me just send you the link before I forget, There it is.
Hey, we were at, I think you still wanted to talk about the issue, no, I think…
**Jack Berg** 16:44 No, I'm all done with that issue, yeah.
**Gregor Zeitlinger** 16:46 Right, right.
then I think I can show you what I want to have feedback on.
I'm not sure if it's more instrumentation or more SDK, so, Let's just see what your reaction is, There it is.
Is that the right one?
Is that sharing working, or not?
**Jack Berg** 17:35 I, I see it.
**Gregor Zeitlinger** 17:36 Declarative configuration support, okay, the title is not… Maybe it is good. So, this is our distribution, and it does not support declarative configuration.
And I had created a POC Pretty much a year ago, but, the API has evolved, so that it is now based on A declarative configuration, instead of, properties.
And, for… distributions, it also has a right path. At least, I think it should have one.
And that's what I want to discuss.
And let me see where the part is.
Set default, exactly, that is… How it looks like, So, what we are trying to do is we want to set some default values for distributions, and we want to do it only once.
And it should affect both.
Declarative configuration and properties.
And, this is… basically a new API.
could live in Contrib SDK or wherever, that's secondary. First, I want to talk about That's… Good approach, or if there's something simpler that we could do.
**Jack Berg** 19:14 So, like, what's… you have this defaults, you're kind of, like, building up an in-memory representation of, like, a YAML data structure of sorts, or it mirrors the YAML data structure, and it, you know, you're declaring the defaults for different properties.
And so what would be the API for how a given instrumentation kind of consumes the aggregate of, like, you know, the defaults that, you know, are being declared here, plus the… You know, the instrumentation config from the user.
Is it all, like, okay?
**Gregor Zeitlinger** 19:52 No new API. The instrumentations consume it in the same way as now. So, using either config properties, or the, what's it in declarative configuration? What's the object name there?
**Jack Berg** 20:08 Do you mean.
**Gregor Zeitlinger** 20:10 Declaration?
**Jack Berg** 20:11 Good config properties, yeah.
**Gregor Zeitlinger** 20:13 Yeah, exactly. So this is.
**Jack Berg** 20:16 This is opaque to instrumentation. Instrumentation doesn't get a chance to see this at all. This is happening sort of before, and instrumentation is unaware of this.
**Gregor Zeitlinger** 20:25 Yeah, we are using the existing, plugin mechanisms to write it to either the YAML node or to the config properties, backing, HashMap.
**Jack Berg** 20:37 Okay.
So, it needs to be written to the hash map or to the YAML properties based on context, and I guess… you want to be able to write this, like, one time, and, you know, my first instinct is that it's, like, some sort of… there's some sort of SPI mechanism that loads all of these defaults.
That are being declared by, you know, the base agent or distributions of it, and then somehow, like, layers on those defaults onto the users.
you know, YAML, or, like, the hash map of system properties environment variables, but what was your instinct?
**Gregor Zeitlinger** 21:23 You're absolutely right. Now that we're at this, At depth level, I can show you how it's actually implemented.
It's not… That much, I think.
The component provider?
**Jack Berg** 21:43 That's…
**Gregor Zeitlinger** 21:44 No, I think that's something different.
Declarative configuration customizer Provider, right? That's…
**Jack Berg** 21:52 Yep.
**Gregor Zeitlinger** 21:54 This is, called, using SPI, you're right, and it, loads this default object. It's a static, but I mean, that's something that we could tweak. And then it says apply to model, and this is just reading the values From, the structure, and then setting it in the right place.
**Jack Berg** 22:18 Huh.
That makes sense.
**Gregor Zeitlinger** 22:22 fall?
For you.
**Jack Berg** 22:24 Is it… no, no, no, I can see it just fine.
Yeah, that makes sense.
so, yeah, the… the static… how do you make sure all of these Like, the static gets populated before the SPI is loaded. Is there, like, a, initialization block where it's all added to the static?
**Gregor Zeitlinger** 22:50 That I have to look up, I… Cannot remember how that worked, so here…
**Jack Berg** 22:58 Oh yeah, there's an initialization block in the next thing, down in the file below, Grafana distribution config.
**Gregor Zeitlinger** 23:05 Yeah, it's a simple static initialization block, right, yeah. Could probably also be done in a different way.
**Jack Berg** 23:12 But doesn't something have to reference this Grafana distribution config class for that static initialization block to be invoked?
**Gregor Zeitlinger** 23:21 I think that's, this line here.
**Jack Berg** 23:23 Oh, okay, yeah.
Yeah, I see.
That makes sense.
Yeah, so you could do that via SPI instead. So, like, I'm reading this, like, this API is, like, you're sort of, you know, you have this get structured and then set default. And so, it's sort of like… it's sort of like you're kind of traversing a, like, a fake YAML object, like, that doesn't yet exist.
navigating down to a place in the hierarchy, and then, like, you're setting a key value, like, at some point in the hierarchy. And, you know, I guess it's different than declarative config properties, because declarative config properties is always read-only.
And this is sort of, like, a right version of that. You're trying to do a very similar thing, like navigate the hierarchy, but instead of only reading data out, like, inserting it in, and then layering multiple of those together.
Right.
So, yeah, like, where should that type of thing live? You know, it seems like a, It seems like a… sort of… you know, we… it… We have the declarative config customizer that you're leveraging here that has you… allows you to take the model and customize it, and it seems like this is sort of, like, a utility that makes it easier to customize the in-memory model.
And so, maybe it should live alongside wherever that SPI lives, so that if, like, you're taking a dependency on that SPI, if you want to implement the customizer SPI, like, you have this utility method alongside of it to…
**Gregor Zeitlinger** 25:10 But it also, works with the config properties, right? So it's not only for declarative configuration.
**Jack Berg** 25:21 And on the other side of that… On the other side of that, like, in theory, it's also not limited to just… the concept isn't limited to just instrumentation defaults. Like, you could also… extend it to be for, like, SDK defaults as well. Like, if a distribution wanted to customize defaults for, like, the meter provider or something like that… Right. This same concept would apply there.
So that's… like, that's, I guess, a bit of a tricky bit, because, like, you know, you're saying it applies to instrumentation defaults for environment variables and, and declarative config, and that requires some domain knowledge about how instrumentation configuration properties are modeled for environment variables versus declarative config. Like, that's… That's kind of baked in there, is, you know, if you have this property, like, yeah, how does it manifest as a system property?
**Gregor Zeitlinger** 26:23 That's right.
**Jack Berg** 26:25 And yeah, then there's, like, the more, like, if you wanted to not just be instrumentation defaults, but just, like, you know, some utility for layering on SDK and instrumentation defaults, that becomes, like, more just, like, declarative config-oriented, and not just, like, not both things.
So that's kind of a tricky bit.
**Gregor Zeitlinger** 26:47 Yeah, maybe that's, that's the point where… We should stop, because then it gets hard to understand what it's actually doing.
**Jack Berg** 26:56 Yeah.
Yeah.
Or maybe there's, like, maybe there's some combination of it. Maybe there's, like, a, a utility method in declarative config that Makes it easy to layer on defaults onto the declarative config model.
And, and, you know, maybe it's called, I don't know what it would be called, but it does the same type of thing, where you can just navigate, you know, a YAML data structure and sort of create an in-memory representation of that very easily, and then layer that onto the model.
And then, you know, over on the instrumentation side of the world, there could be, like, an instrumentation default version of that, which is, like, specifically tailored to, you know, the use cases you're talking about. So, maybe there's, like.
A bit that's reusable in declarative config, and then an instrumentation specific.
Thing built on top of it.
**Gregor Zeitlinger** 28:02 Sounds like a little bit we should explore both, But not necessarily together, because maybe one turns out to be a good idea, but not the other.
**Jack Berg** 28:12 Yeah.
Yeah. I don't… I don't have any strong feelings about it right now, I'm just thinking out loud.
**Gregor Zeitlinger** 28:19 So what about, the place where we should continue doing that?
**Jack Berg** 28:27 Well, if it's instrumentation-specific, then, that part can't live in the core.
Because it has that domain knowledge about how the instrumentation defaults sort of map to system properties and environment variables. That's, like, you know, squarely in the domain of the instrumentation repo.
But then within the instrumentation repo, there's the question of, like, where should that live? And… I don't know, like, what's a… it needs to live somewhere semi-central.
**Gregor Zeitlinger** 29:03 We have already, project where… The other direction, the red direction, lives.
Maybe we've just added there.
**Jack Berg** 29:16 The redirection of… what? Of…
**Gregor Zeitlinger** 29:19 Of, reading instrumentation properties, so reading it either from declarative configuration or from properties, so that.
**Jack Berg** 29:30 Yeah.
**Gregor Zeitlinger** 29:31 Apparent with the implementation?
**Jack Berg** 29:34 Yeah, and that place… probably… it already has the, you know, the domain knowledge of how config translates to declarative config or system properties, and it's, like, a central enough place that all the instrumentation depends on it already. Or maybe not all the instrumentation, but the key bits of the agent are already wired up.
Into that.
**Gregor Zeitlinger** 30:04 Yeah, that's right. Yeah, that's good feedback. I'll try creating a PR there.
Yeah, good.
**Jack Berg** 30:15 Yeah, and maybe tag me on that PR, Maybe I'll see if I can… like, sketch out something for, you know, a utility for the core, and… You know, basically the idea would be, how can we make it easier to Layer to customize the model.
Right? Like, that's the idea in my head, and that's, like, maybe there's overlap with what you're trying to do. But it's kind of… it's kind of cumbersome to customize the model today.
**Gregor Zeitlinger** 30:50 you have to, write the YAML nodes, I think that's how it works.
I think I have, one or two examples… I think there's one open PR that I have, where we could look at how this is working.
cannot share a different tab, this is a little bit annoying in Zoom.
**Jack Berg** 31:22 You don't just share your whole screen?
**Gregor Zeitlinger** 31:24 Hey, that's what I'm doing instead.
A sharing tab has the advantage that I can also, like, take notes in the background without, Just, flipping around and confusing.
Everyone…
**Jack Berg** 31:39 Oh, you probably only have one screen right now, huh?
**Gregor Zeitlinger** 31:42 Yeah, yeah, I don't want to have multiple, that's… that's confusing me, then.
**Jack Berg** 31:46 Oh, God.
**Gregor Zeitlinger** 31:48 So, no, not clear… Not sure if that was the right one.
No, that was the wrong one.
I think I just have to look for, what was the name? This configuration customizer.
What?
Oh yeah, we have a cup of… I didn't do that.
**Jack Berg** 33:39 Abstract, spans, login customizer Provider.
Huh.
It's an abstract.
**Gregor Zeitlinger** 33:48 You have some navigation here, and… And GitHub now.
No? Not working?
**Jack Berg** 34:00 This took you to the declaration, to the import, huh?
**Gregor Zeitlinger** 34:03 Oh, yeah. Okay.
So here in… If the customize method… You get a model in, and… You return a model right.
That's all about.
Portal with Tracer Provider.
This is, right, this is a built-in method with Tracer Provider.
**Jack Berg** 34:58 Yeah, so that's.
**Gregor Zeitlinger** 35:02 That doesn't look too bad.
**Jack Berg** 35:04 It's… it's a lot of null checking. That's probably the most offensive part.
But yeah, like, they already have… so these are generated classes from the JSON schema, and it looks like they already have the withers with simple widths, you know, that return a new instance.
So that's…
**Gregor Zeitlinger** 35:28 an example of where I think the API is already good.
**Jack Berg** 35:33 But I think it breaks down when you're talking about something that, like, instrumentation, which is, like, the unstructured part of the schema.
And it's just modeled as, like, maps of string objects.
And so, maybe… which is the thing that you're trying to address, so…
**Gregor Zeitlinger** 35:52 Yeah, I was trying to find out if we have a use case for SDK configuration to have a similar set default.
**Jack Berg** 36:05 Yeah, and I think what you're saying is, like, it's probably not necessary, because the ergonomics aren't that bad. And so we can focus on instrumentation.
And I, I agree.
**Gregor Zeitlinger** 36:17 Since it's already structured, I think that's the key insight.
**Jack Berg** 36:22 Yeah, the unstructured parts will be more cumbersome.
I mean, maybe there's, like, a utility… a generic utility method, where it's, like.
You know, the parts of the schema that become unstructured, like, they're called, like, additional properties in the way that the JSON schema to Java class generation, like, works. It's like, whenever you have, like, the unstructured part of the schema, it just says, like, additional properties, and it's, like, a map of a string to object.
And so maybe we could, like, add a utility method to just, like, make it easy to… model, like an arbitrarily structured map that, like, you know, mirrors all the types of things you could do in YAML, and merge that somehow with the model.
**Gregor Zeitlinger** 37:15 Oh, we have an example here.
**Jack Berg** 37:18 There you go.
**Gregor Zeitlinger** 37:18 properties, what is that doing?
That is for detectors.
**Jack Berg** 37:27 Yeah, detectors is an example of where, it becomes… Sort of schema-less.
Because you have a well-known set of detectors, but then you have open-ended nature, so you can have arbitrary additional detectors.
And so this is saying, like, hey.
Find all of the, the, you know, the detector names, which are not part of the formal schema.
**Gregor Zeitlinger** 38:01 So here, this is… Rather simple. It's basically that line. It… it adds an entry to the additional properties.
**Jack Berg** 38:13 Yep.
**Gregor Zeitlinger** 38:15 That's something that would be worth… Simplifying already?
**Jack Berg** 38:23 I don't think the pain's high enough yet. And, and in this case.
It's like, the things that you'd want to… The reasons you'd want to introduce a utility would be, like.
The same thing is happening over and over again, so it's like a lot of instances of the same, toil.
Or, it's, like, error-prone. Like, you know, even if there's only a few examples, it's, like, it's hard to get right.
And this looks correct right now, and unless I saw, like, a bunch of examples, I think I'd feel okay.
**Gregor Zeitlinger** 39:03 I think right now it's, not that much we can check if there's actually any other I think those both are for, resource. No, all of… all are for resource. Okay, so not enough to, really see a need for it so far.
**Jack Berg** 39:34 Yeah.
**Gregor Zeitlinger** 39:40 Okay.
**Jack Berg** 39:43 Alright.
You wanna go, take a quick break before the JavaSig?
**Gregor Zeitlinger** 39:51 Yep, I think that's a good idea. So what do we do about this, AI?
collaboration, do… We could do it in our meeting with, with Jay together.
**Jack Berg** 40:07 That's exactly what I was thinking. Maybe we just, like, just, you know, set aside that, and so, do you want to, like, have a specific target in mind? Like, hey.
like, how can we use AI to sort of refine the contributing guide for the core repo, and, you know, like, help users and agents at the same time?
**Gregor Zeitlinger** 40:29 Yep.
**Jack Berg** 40:30 Sweet.
I'll send a message to Jay and you, and just, like, sort of just say that that's what we're gonna do the next time we meet.
**Gregor Zeitlinger** 40:37 Yeah, cool, thanks. Then, see you in a couple.
**Jack Berg** 40:40 See ya.
