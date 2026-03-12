SIG: Java SIG
Date: 2025-10-16
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:27 We can't hear you, Trask.
**Trask Stalnaker** 01:34 How about now?
**Jason Plumb** 01:35 Yeah, now we can.
**Trask Stalnaker** 01:36 Fantastic.
A…
**Jack Berg** 01:58 Hi, everyone.
**Jason Plumb** 02:00 Hello.
**Trask Stalnaker** 02:02 Hey, Jack!
**Jason Plumb** 02:31 I know that I've asked this, like, 3… at least 3 times, so I'll ask a fourth. What's the order of instrumentation and contribib?
for releasing.
Instrumentation…
**Trask Stalnaker** 02:46 trip.
**Jason Plumb** 02:46 Okay, thank you.
**Trask Stalnaker** 02:47 Which…
**Jason Plumb** 02:48 It doesn't make sense in either order. That's probably why I can't hold it in my head.
**Trask Stalnaker** 02:55 Yeah, because especially now that we're pulling more Contrib stuff into the instrumentation repo.
**Jason Plumb** 03:01 Yeah…
**Trask Stalnaker** 03:03 But I remember we tried to flip that release Once, and ran into problems. I'd have to go back and look at the history to remember.
What?
So yeah, let's start with that.
Any… releases that… Anything you… anyone wants into the release. I think right now… We've got… This one, I think, is ready to… Okay. Thank you, Laurie. So, we'll hopefully get this one in, but we will see… is… oh, I think the Grafana folks are… Out at something today.
And this one, Laurie, Up to you if you feel free to merge it, if you want it in the release, or if you'd rather wait.
**Lauri Tulmin** 04:13 Oh, I think we can wait with this.
**Trask Stalnaker** 04:15 Okay.
**Lauri Tulmin** 04:18 I just wanted somebody to review it.
**Trask Stalnaker** 04:22 I did, I read… well, I mean, I read through all the code.
And it made… Sense to me.
And the tests all pass.
If we have… do we have, no, Sylvain, or… Jonas.
would be… Good.
I'll CC them.
So, let's remove… Alright, anything on the contrib side?
We don't even have a milestone, so… I'm gonna assume… not… .
**Jason Plumb** 05:47 Yeah, I don't… I don't think there's anything super pressing.
**Trask Stalnaker** 05:53 Cool.
**Lauri Tulmin** 05:54 I think there was this GCP project pull request.
**Trask Stalnaker** 06:03 Yeah, did that end up… I'm not sure, I don't think I'd seen an approval.
**Lauri Tulmin** 06:09 Okay, it's still not appropriate.
**Trask Stalnaker** 06:11 Not yet, yeah.
I thought that there was some progress with it, but… There was, yeah. But I think, We'll need… Forget.
Pranav… All right, let's move on. Jason.
**Jason Plumb** 06:46 Yeah, so this is me trying not to be super dismissive, like, when I first read this, I was like.
get out of here, like, one page with all config? Like, that's a terrible idea, and so I, like, I just, like, flippant, like, that's my, you know, instinct. But then I… after stewing on it, I'm like, you know, it would kind of be cool, because CTRL-F is, like, pretty powerful.
Indexing is pretty powerful, but we don't have, you know, we don't have one page that pulls all the config together.
And then… where do we draw the line? You know? Like, if it's instrumentation config, that's fine. Do we also include all of the SDK config?
Like, I… I don't know. I'm just curious what people think about it.
Is it… is it worth, you know, at least maybe getting started on, or opening an issue to keep that in mind, or… just curious what people think. This person had… specifically, the context here, for those that didn't read the issue, is that this person… had trouble finding out how to turn the specific JMX metrics on for their app server, so I think Tomcat or WebSphere or something.
And, yeah, it wasn't really in the docs, and they ended up finding it in the README, but I think they weren't super technical, and so they were, like, kind of struggling to find it, and we just didn't have it in there. I've since added it, just to the app server stuff, but they were like.
Where is the page with all the config? That was the question they asked, like, where's the page with all the configs in? That's what I just added, that bottom section there, Trask.
**Trask Stalnaker** 08:17 Right, right.
**Jason Plumb** 08:18 Yeah, mostly just cares what people think.
About having a single page with all the config.
In all of its unwieldy glory, and how do we maybe, I mean, automate from the metadata, maybe?
**Lauri Tulmin** 08:34 The only option is if it can be automated. Otherwise, nobody's able to keep it up to date.
**Jason Plumb** 08:39 I know, yeah, it's a really good point.
**Lauri Tulmin** 08:43 I think for the instrumentation options, we are, like, sort of moving it, moving it that way.
But, to really have all the options, we would also need to have some way to get all the options for the SDK.
Put a declarative config into the mix, then that's going to complicate the matters even further.
**Jason Plumb** 09:06 Totally. And all the contribib options, like, for any contribib modules that we pull in that are configurable.
**Lauri Tulmin** 09:13 There aren't that many contrib options, in fact.
**Robert Niedziela** 09:20 So, yeah.
single place is very convenient, I mean, for beginners especially, right? Later on, if you get used to it, you know where to find the information, but at first, it's hard to grasp all this stuff.
**Bruno Baptista** 09:37 So, I will add the link to the meeting notes. Hi, everyone. So, Quarkus has, A page like this?
Sorry.
Well… and, well, it's large. I think there's around 2,000 configs in there.
**Trask Stalnaker** 10:01 Yeah, I think it's very connect… tied to the work that Jay's been doing on, documenting all the instrumentations and all the instrumentation, because… There's the core Java agent config options, which is a smaller set, which, you know, we sh… but then a lot of those config options are instrumentation-specific.
And so… Those are going to be in the registry via Jay's work, all documented.
But, you know, so then the question is, do we… Is that searchable well enough, or do we want to have a distro, like, a distro page that just… Collapses them all together, which… I don't have any… Like, I agree, I'm…
**Jason Plumb** 11:02 Oh yeah, look at this. Wow.
**Trask Stalnaker** 11:05 Yeah, I mean, I… I've… I think it's fairly common to have these larger… I know we've kind of… Split things up, which is nice for browsing, that I've seen in the past, like, Spring and others, tend to have pretty big pages… Then the other question that factors into this is how much… I mean, I have to ask, how much is this… are people going to read this stuff versus… I know with Microsoft Docs, they say that almost, like, almost everybody who lands there is coming from a search, a Google search.
Right, they're… So the question is more about, is it indexed well?
And the future is, of course, instead of asking Google, asking ChatGPT, which is essentially what we have here.
And so, the question is, is this indexed?
**Bruno Baptista** 12:16 So, let me share how I usually use this. Imagine that I want to configure something related with JDBC.
There are multiple places that use JDBC, so I just go here, search for it, and I have all the properties that have that in the name.
Were you…
**Jason Plumb** 12:35 Filter there, there was a filter even, right?
**Bruno Baptista** 12:38 Yeah, there should be somewhere.
Yeah, there's a filter, yeah, built in the page.
Yeah, this kind… and if you don't really know exactly what you are searching for.
And you are just… Trying to find, this is very handy, because it allows you to understand, for example, which extensions might touch what you need, and things like that.
Yeah, it's… it's not just to… to… understand the particular configuration for, something. It's more to have a broad view of what you can use under a certain scope.
Yeah, but that's just for me.
**Jason Plumb** 13:30 Yeah, I think this is… I think this is the kind of thing that that original user was looking for.
And they just got frustrated and hit the feedback button, I think, on the website. Jack?
**Jack Berg** 13:41 I posted a link, there's a related wrinkle to this, so in declarative config.
we have this schema that's defined via JSON schema, and there's this concept that I'm introducing, and it's called the metaschema, and there's bits of information that we want to track alongside our types and properties, but they don't fit cleanly into the JSON schema.
format.
And so, the meta schema would be what we use to track these additional bits of information, and then, you know, one of the things that you can do when you have this JSON schema and the metaschema is you can generate documentation in an easier-to-read human format.
And so this is kind of what I'm sketching out here, and so, like, if you click on any of these types, Trask, there's some, like, interesting features here.
So, like, you know, you see all the properties for a particular type, you can see the language support status at a glance, you can see any constraints or anything that exist on those types, and you can see usages. So it's, like, it's got, like, this infinite, like an infinite linking feature, where you can see, like, where it's used in other types, and what types are used in it, and it just is kind of like a bunch of circular links that go around and around forever, so you can see it. But, you know.
**Trask Stalnaker** 15:01 Java doc.
**Jack Berg** 15:02 Very Javadoc-like, right, exactly. So this is, this is, like a version, a declarative config version of kind of what Bruno was showing, and it'd be cool if we could somehow think more holistically. Like, if we didn't have the system property and environment variable-based schema to begin with, and everything could be defined via JSON schema.
then, you know, it'd be… it'd be easy to see how you could, you know, have one place where all the different types and properties were defined, and all their semantics and descriptions were in one place. I think the trick is going to be, like, what's the cleanest way to present this information when there's multiple configuration interfaces, programmatic.
System properties and environment variables, and then declarative config. That's gonna be a little bit of a tricky thing.
**Jason Plumb** 15:53 Yeah, I think the way I look at it is the config file kind of is its own thing, because it has a schema, because it's formal, and it allows you to do stuff like this, like, more concisely than just a bag of properties.
**Trask Stalnaker** 16:09 But we are doing bag of properties in declarative config, also, for all the instrumentations will sort of… I mean, a structured bag of properties. Yeah.
**Jason Plumb** 16:20 Yeah.
**Lauri Tulmin** 16:21 Planck actually has a page that lists almost all of the configuration options. I pasted the link to the chat. It looks pretty ridiculous.
**Jason Plumb** 16:29 Do we really?
**Lauri Tulmin** 16:30 Yeah.
Scroll down a bit.
**Jack Berg** 16:37 Heh, good.
**Jason Plumb** 16:38 Really?
**Jack Berg** 16:39 It goes and goes.
**Jason Plumb** 16:40 Oh my gosh. Also, it's unusable. Look at how small this table is.
**Trask Stalnaker** 16:45 Yeah, man.
**Jack Berg** 16:46 A bigger resolution?
**Trask Stalnaker** 16:47 scrolling.
**Jason Plumb** 16:51 That's a good list. Wow.
**Robert Niedziela** 16:55 It also shows how complicated, actually, this stuff may become, right? Number of configuration options is huge.
**Jason Plumb** 17:02 Yeah. And most of these are not bespoke.
**Robert Niedziela** 17:05 Do you know… Lori, do you have any idea where this… who made this, or where it came from?
**Jason Plumb** 17:09 Is it from metadata?
**Lauri Tulmin** 17:11 I made it.
**Jason Plumb** 17:12 From metadata.
**Lauri Tulmin** 17:13 Yeah.
**Jason Plumb** 17:14 Yeah, okay.
**Jack Berg** 17:16 By hand, and Lori maintains it by hand.
**Lauri Tulmin** 17:19 Yeah, I manually copy-pasted it from various sources.
**Jason Plumb** 17:24 Sure.
**Trask Stalnaker** 17:27 But it does answer the, you know, CTRL-F JDBC question.
**Jason Plumb** 17:33 It's true.
**Jack Berg** 17:38 You can imagine.
**Lauri Tulmin** 17:38 Sorry, it doesn't include the JMX one that was the original.
**Trask Stalnaker** 17:43 That was the ask, the ask,
**Jason Plumb** 17:47 Is that because that's contribib, or why… just… we just don't have it in there yet?
**Lauri Tulmin** 17:53 Lori ran out of patience. I might have missed some of the properties.
**Jason Plumb** 17:58 Easily doable missing properties here.
Alright, well, I don't think we have to belabor that topic too much longer, I just wanted people to give some input, I appreciate that. Maybe… I'm curious what Jay thinks, too, just because he's in that mindset as well.
**Jack Berg** 18:23 Jason, when you were originally proposing or talking about this, you know.
so there's 3 configuration interfaces. There's the flat system properties and environment variables, declarative config, and then there's, like, the programmatic API. And, like, so… I guess… What's the difference between, like… I think intuitively, we would say that we would only want to present, like, the system properties and declarative config, maybe, or maybe separate those, but those are the things that we're really talking about, but why? Like, why wouldn't you just, like, lift up the programmatic configuration API, like, into this one page? And it's, like, one page to rule them all.
I think…
**Trask Stalnaker** 19:03 Because this is, the page would be scoped to Java Agent users.
**Jack Berg** 19:10 Okay, and most Java agent users aren't building extensions that would in any way interface with the programmatic API?
**Trask Stalnaker** 19:18 Yeah.
**Jason Plumb** 19:19 It's really for operators.
**Trask Stalnaker** 19:23 And the reason I say scope to that, because I think we have different scopes, I think we have… we have to have one of those for Java Agent, we have to have a separate one for the Spring Boot Starter.
maybe a separate one for SDK… And maybe those could integrate the programmatic If it made sense.
**Jack Berg** 19:49 Well, yeah, there's already a page that does that, and that's kind of what I'm referencing, and it's a long page.
Like, so the idea of, you know, merging this super long page of SDK programmatic configuration API with, like, system properties and environment variables, it gets, like, really unwieldy.
**Trask Stalnaker** 20:07 I like them separate myself, because it's two different users. Generally, it's, like, operators versus… developers… For… sort of.
I just wanted to show folks, in case they haven't scene, these metadata YAML files that Jay's been, adding throughout. So these have all of the configuration options for each instrumentation.
So as this… I mean, I don't think… He's made it through all 200, modules yet, but this is, I think, gonna give us that ability to auto-generate Something.
It's just a matter of what that something is.
**Jason Plumb** 21:16 Yeah, do we know… do we know how this accounts for, like, common… Configuration, like, even common instrumentation configs that apply to multiple modules.
**Trask Stalnaker** 21:29 Yeah, let's look at… Say…
**Lauri Tulmin** 21:32 I think currently it's built so that if, like, the common options Are added to the… to each of the instrumentations that's affected.
**Jason Plumb** 21:42 Okay, so duplicated.
**Lauri Tulmin** 21:45 Yeah. In some sense, like, using the YAML files this way isn't, like, ideal, because Like, if, If one of those options changes, then you have to change it in a million places.
**Jason Plumb** 21:57 Yeah, you kinda wanna, like.
**Lauri Tulmin** 21:58 I guess.
**Jason Plumb** 21:58 Lewis.
**Lauri Tulmin** 21:58 Hopefully the co-pilot is able to do that.
**Jason Plumb** 22:01 Yeah.
I mean, an include, some kind of, like, file include, or… External reference would be nice.
**Lauri Tulmin** 22:12 YAML includes stuff, I actually… made a huge Java class that generates a Jumble file, because… That kind of allowed me to more easily change the structure of the Elm file.
And also… Share the common properties.
**Jason Plumb** 22:36 Yeah.
It's probably a reasonable segue into the next topic, which is somewhat overlapping.
Yeah, so I was just surprised about this comment, and I wanted a little more context from the core maintainers.
**Jack Berg** 23:04 Yeah, so, I think it's hard to take that position that declarative config is the only way we should do things while it's still not stable.
If it was stable, I… I don't… If it was stable in the near-term future, which has been my goal for a while, but then parental leave got in the way.
But I think John's right, like, you know, let's separate the programmatic configuration from the property-based one. Like, that's an obvious thing that we should do.
And if you have a programmatic configuration API for setting, in this case, the throttling rate of your OTLP exporters, then you can always write an auto-configure extension, like one of those SPIs, that, like, you know, takes your OTLP exporter, converts it back to a builder, sets your configuration… your programmatic configuration option, and then builds it again.
So it's not that big of a deal, that there's not, like, a system property or environment variable way to configure that at that point.
**John Watson** 24:10 Yeah, my comment here was, basically, I wanted… I want two PRs.
I want a PR that adds the programmatic configuration, and I want a PR that then has… if we want to have A property-based or a file-based, like, let's just separate them.
**Jason Plumb** 24:26 And this is doing both.
**John Watson** 24:28 And this is doing both, and I think they're separate concerns, and I want to separate the PRs, that's all.
**Jason Plumb** 24:33 That's a reasonable request, and I think I didn't understand that, so that helps. Okay, so we're not… I mean, even if declarative config was, set in stone, solid, stable tomorrow.
we… we don't think that we're going to be dropping environment variables or system properties for basic… I'm calling it, like, just kind of standard, basic configuration.
**Jack Berg** 24:56 We can. We can. We're… backwards compatibility requires us to support those indefinitely. The question is, like, will we add new ones, or will we use, like, a more powerful declarative configuration tool as a caret to draw people away from environment variables into declarative config?
**Jason Plumb** 25:12 Yeah.
**John Watson** 25:13 And as far as I understand, there's still a moratorium on adding new environment variables, right?
**Jason Plumb** 25:19 At the school.
**Trask Stalnaker** 25:19 back. Yeah.
**John Watson** 25:21 for the students.
**Trask Stalnaker** 25:22 The spec has already taken this position, so I think it's fairly natural for… the Java SDK to take it as well.
**Jason Plumb** 25:32 I had not heard that, okay.
**Trask Stalnaker** 25:36 Yeah, that's actually been in place for, like, a year and a half.
**Jason Plumb** 25:41 Interesting, okay.
**Trask Stalnaker** 25:43 The idea is… Things that are really important that a lot of people want to configure.
Has probably already been added already.
And at this point, it's more minor configuration options, which… Programmatically, you know, is okay, just to have programmatically, at least.
**Jason Plumb** 26:07 I'm trying to think of, like, some… I mean, a moratorium is fine, I'm just trying to think of, like, Edge Casey stuff, like… I don't know if there was, like, a profiling configuration that applied across the board or something, or op-amp, yeah. These are… Interesting things to think about, but… whatever, that's spec work.
Seems fine.
**John Watson** 26:27 Yeah, this actually, this particular PR, Jack, I… I wanted you to weigh in just on the general bits before we got this into the public API.
**Jack Berg** 26:38 Yeah. It's actually a weird thing. This is, like, the first time that we're exposing public, you know, programmatic configuration APIs for configuring, like, throttling logging, like, internal logging, so…
**John Watson** 26:50 And that's why… that's why I've… I've slowed… slowed this down, because I want you to take a look at it before we commit to it.
**Jack Berg** 26:58 I mean.
**John Watson** 26:58 We have an internal way to set the throttling logger, but it's not exposed as actually official public API surface area at the moment.
**Jack Berg** 27:09 Yeah, and it's like, our internal logging so far is done through Juul, and… you know, the way that you turn logging on and off by a package-by-package basis is using the JUL configuration tools, and so, like, up until this point, internal logging is separate from the rest of our configuration story.
And I'd love to keep it that way. Like, I'd love it if, like, you know, you didn't have to configure two different places to get your internal logging right. Like, you know, one to turn the loggers on and off, and another one to… another place to configure their rates. That's kind of the direction we're going in here.
I'm not sure if that's possible.
**John Watson** 27:48 Yeah, because Juul is not gonna let… Juul does… I mean, the throttling loggers are an internal thing, right? Like, Juul doesn't give us any of that facility.
**Jack Berg** 27:57 Yeah.
**Trask Stalnaker** 27:57 Presumably, you could write a… An appender. I mean, if it was… that… Did the throttling.
**Jack Berg** 28:08 Yeah, with a lot of effort.
**Trask Stalnaker** 28:10 Yeah.
**John Watson** 28:11 Because I know.
**Trask Stalnaker** 28:12 Java Util logging. But if you pipe it, you know, I figure most people are piping Java Util logging to LogBack or Log4J.
And so you can add a log for J or a log back appender that does that throttling.
**Jack Berg** 28:28 I mean, from that standpoint, like, you know, maybe we shouldn't have an internal throttling mechanism at all.
Right.
and just tell users that if they want to throttle, you know, go do it via log back or log for JConfig. But I think in practice, we want to make this easier for users than to go use those facilities. We want to have, like, you know, reasonable defaults.
I wonder if… I wonder if it would be better to just, like… I'm just thinking out loud here, like, we have a… we have an internal throttling mechanism. It's on by default, it's hard to configure. What if our configuration around this was just to turn throttling off?
And if you want to change the throttling, what you do is you turn the internal throttling mechanism off via a simple Boolean switch, and then you go configure Log4J or log back to, you know, do it in the proper way, however you see fit.
**John Watson** 29:29 Do LogBack and Log4J have throttling?
As a feature already?
**Jack Berg** 29:35 I think they do. I'd need to go double-check that, but they have, like, a pretty robust, like, filtering mechanism that I think has, like, throttling built in.
**John Watson** 29:44 Because, like, like you said, we don't… we… if you don't throttle this, and they have, like, a bad exporter or a bad configuration.
It gets super spammy, and… which is the purpose of our throttling, right? Is to keep those… that spam down. And we want to make it… we don't want to hurt the user as much as we possibly can. And if we're telling… if we're gonna have to tell them they have to do something that's difficult.
that's… I think that's a… it's hurting our developer experience.
**Jack Berg** 30:14 Yeah.
So, like, I think we'd have to do, like, a proof of concept.
Of, like, what it would look like to actually use Log4J or LogBack to do this throttling on that side.
**John Watson** 30:26 Yeah.
**Trask Stalnaker** 30:28 Do we understand what, the… User wants here, like…
**John Watson** 30:35 Yeah, they want… they basically… they… they just want to be able to say, rather than logging once a minute, log once every 10 minutes.
Or… hour.
**Trask Stalnaker** 30:48 Or never?
I mean, I'm just wondering, like.
**John Watson** 30:51 No, never… it never is not… they weren't looking for never. There was a…
**Trask Stalnaker** 30:54 Okay.
**John Watson** 30:54 It's a very old… it's a very old issue they log, which is basically them following up I'm working… working on it.
**Trask Stalnaker** 31:02 Here's the issue…
**Jack Berg** 31:09 Because, John, you can kind of see where this is going, right? So, like… there's 2 or 3 new configuration APIs for each of the OTLP exporters.
That they've added. And this is not the only place that we do internal logging with the throttling logger. So, like, if you play this out, every single place we use internal, internal logging with the throttling logger would have similar types of configuration APIs added. And that's a lot of surface area.
**John Watson** 31:37 Yep, absolutely. That's why I have not merged this, because I agree, it is a lot of surface area.
And this, yeah, this only covers exporters at the moment. Doesn't cover spam processors, or… any of the other stuff. I mean, I think exporters are the most egregious, because they're the place that interacts with the outside world, where you tend to get errors that get logged.
But.
**Jack Berg** 32:01 And a subset of exporters, too, not even Prometheus or Zipkin.
**John Watson** 32:06 Zipkin doesn't use a throttling auger?
**Jack Berg** 32:08 I mean, it does, but it's not added here.
**John Watson** 32:09 Oh, it's not added here, yeah, yeah, for sure. Yep.
Well, and Prometheus would be a little different, right? Because that's…
**Jack Berg** 32:17 Hot pole.
**John Watson** 32:18 Yeah, it's gonna be pulled rather than something we're… so they control that already.
**Jack Berg** 32:28 Yeah, I think… I think, you know, I don't… I'm not sure how to communicate this to this person, because, you know, they went and did this work, but… You know, I think if I had infinite time, I would go and do a POC and show them how they can achieve the same effect via LogBack or Log4J, and evaluate just, like, how cumbersome it was. And if it was, like, reasonable, I'd be like, hey, let's close this and just make this our formal recommendation.
**John Watson** 32:56 Although we don't currently have configuration to turn throttling off and just let it go.
**Jack Berg** 33:01 Right, and so that would be the thing that we add everywhere.
**Trask Stalnaker** 33:11 Alright, Jason, was that the can of worms you wanted?
**Jason Plumb** 33:15 No, it's really good, yeah, no, I learned, I learned a few things. I just also want to appreciate that that's, that person is the clam.
Yes. That cracks me up for some reason. The clam. Carl the Clam.
**Trask Stalnaker** 33:31 Alright, I threw this on at the last minute, so, I think this came out of, we have… our metric descriptions in the Java instrumentation, Have diverged from what's in semantic conventions.
And I was going to fix it, but then I'm like, okay, well, that's just going to be a never-ending, like, I guess we can… just updating them.
But it would be nice to… if we had constants, for them, at least we can do what we do in the Java agent, where we inline semantic conventions, and then we use the real semantic convention, Incubating artifact to verify our tests.
And… So, this… let's look at an example, RPC… So this was just throwing all these constants, basically. It's not… super smart. So underscore name, underscore unit, underscore description.
Name, unit description for all of the metrics, basically.
The… other… option here… Which I think is what you were… I think what you were talking about mentioned Jack below.
was, having… creating an API to… create the… That takes a meter builder, or creates a meter builder that automatically populates these constants.
**Jack Berg** 35:28 Yeah, exactly. So, you know, you still do this code generation in here, but you generate the functions.
Instead of generating constants.
**Trask Stalnaker** 35:37 Yeah, so the reason I didn't do that is it doesn't help us in, the instrumentation repo.
Because we don't want to depend on the unstable, the incubating artifact.
And so, we actually need the constants In… separately for our test verification.
**Jack Berg** 36:06 Oh, I see.
Yeah, okay, so… the… you're only depending on the SEMCOM incubating artifact in the test repository, and you're making assertions against the outputted metrics. And those assertions, it doesn't really do you any good to have, like, a long histogram or whatever that is configured properly. You actually need to assert them Output metric against the constants.
**Trask Stalnaker** 36:31 Right.
**Jack Berg** 36:33 Yeah, that makes sense. So I think I agree with that, then. You know, like, I think my… when I was reading this, I was, like, thinking, it doesn't have to be, like, one or the other two, it could be both, and, like, maybe you start with constants and then generate the, the functions as a follow-up.
**Trask Stalnaker** 36:51 Yeah, I do love the… function, the method idea, and I know that's kind of where we want to go with Weaver and with generating spans also, and the metrics would be a good place to start.
with that.
**Jack Berg** 37:12 And, okay, so this… that makes sense to me, I think my other comment, maybe I didn't say this in the actual comment itself, but I think you're generating these for… both the stable SEMCOM and the incubating.
And so, I think probably to start, just because this is, like, new code gen, and there might be some, you know, sharp edges to this, that we'd probably… and I know this is a draft PR right now, but if we were to take this forward, we want to start all incubating, and then, you know, after a successful release and integration into instrumentation, then promote it to the stable artifact.
**Trask Stalnaker** 37:52 Yeah, yeah, you did say that. That makes sense.
**Jack Berg** 37:58 But yeah, thanks for the explanation about that instrumentation piece.
I think that makes sense.
**Trask Stalnaker** 38:04 Cool.
Awesome. We've got time, folks!
If anybody has a topic they want to bring up.
**Robert Niedziela** 38:16 Maybe one, one thing, regarding, environment variables and declarative config incompatibilities. I mean, we had, in Java, we had some extension to specify duration, with time unit.
Which is possible with environment variables, but it's impossible with declarative config, and in this case, the substitution doesn't work.
**Jack Berg** 38:45 Yep.
I mean, we could… we could, this is something to discuss. So right now, the… the Java implementation of declarative config is… Is SPEC compliant?
And in the spec of declarative config, any time units are just interpreted as milliseconds.
So there's none of this, like, you know, 1D or 1H for one hour, that we do in system properties and environment variables. I suppose you could make the case that Java should deviate From, you know, the declarative config spec, it, you know, just for more interoperability with our system properties and environment variables, which, like, we've already kind of gone in this direction of supporting these duration.
Modifiers, whatever you want to call them.
**Trask Stalnaker** 39:42 Oof, but won't that, I worry. Yeah.
**Jack Berg** 39:45 And we're… interoperability across languages.
**Robert Niedziela** 39:48 Yep.
**Trask Stalnaker** 39:48 Yeah, somebody will copy the Java one over to Python, and it won't work.
**Jack Berg** 39:55 Now, same thing is true with the environment variables today.
**Trask Stalnaker** 39:59 Yeah.
**Jack Berg** 40:01 So we could, like, we could rip the band-aid off and be like, okay, you know, Java was inconsistent with other languages previously, and… We view that as a mistake, and so, you know, going forward with declarative config, we are going to be much more spec compliant, much more rigid.
**Trask Stalnaker** 40:22 I feel like… we should… like, I feel like declarative config, like, a big promise of that is this consistency of being able to take the same, at least on the SDK config.
to be able to take the same SDK config and copy-paste it across.
Java, Python, Go.
Maybe not .NET.
**Jack Berg** 40:50 Maybe not, Donette, why?
**Trask Stalnaker** 40:53 Because it's built into… I don't know what their declarative config story is going to be, but you know how everything is different for .NET, because it's baked into the .NET Core.
**Jack Berg** 41:04 I did see somebody from .NET, like, you know, probing around, asking questions about declarative config, interested in, like, picking it up and running with it, so…
**Trask Stalnaker** 41:12 Nice. Somebody's thinking about it. There's hope.
Yeah, actually, probably, because I don't think the SDK is baked in, it's the API that's baked into the… NET Core runtime.
**Jack Berg** 41:27 Yeah, so they'll probably never get the instrumentation Config API.
So, I don't know, any other thoughts on this? How important is this? How many… how many times have users run into this issue? I guess that's, like, a good way to think about it, right?
It has to be someone that's picking up declarative config, that is trying to use the environment variable substitution syntax, and was relying on these duration modifiers that are specific to Java. So it's kind of a series of intersecting circles in the Venn diagram.
**Robert Niedziela** 42:10 Yeah, actually, I faced it because there were some defaults in our code defined with units, and, you know, then it just collapsed with declarative config, and I have this issue, but yeah, it doesn't… seems like something extremely important.
**Trask Stalnaker** 42:30 And if it defaults in the code.
**Robert Niedziela** 42:32 Would you…
**Trask Stalnaker** 42:33 And… conditionally.
Yeah. Handle that.
**Robert Niedziela** 42:41 Yeah, but there's one more question, if we have time, I have, I have one more question here, about handling of known, value, actually, I faced it with, propagators, and in propagators, I started the discussion, John actually took some vote on it, and yeah.
in a coat, It looks like the known value means that we should not create any propagator, right?
What in case if someone specifies known with other value? The spec doesn't say anything about how the code should behave. Java throws exception.
**Jack Berg** 43:32 Yep.
**Robert Niedziela** 43:34 Maybe it would be worth adding to spec how other systems should behave in such a case as well.
**Jack Berg** 43:42 I mean, this is one of those cases where, you know.
edge case, and the spec was not fully, complete in terms of describing all the different beats that are expected, and what I've found with these types of things is that, yes, it's good to add it to the spec, and Because the spec was incomplete, implementations normally go in different directions, and so it's hard to, like, retroactively Things. And so.
You know, if you want to drive this, I would encourage you to, but I would anticipate some… it not to be a straightforward thing. It never seems to be.
**Robert Niedziela** 44:31 Strong resistance, the weaker.
**Trask Stalnaker** 44:33 We could fix… but we could fix it in declarative config.
And specify the behavior.
**Jack Berg** 44:40 Well, native config is actually, an interesting case because, This… the structure of the schema prevents it.
**Trask Stalnaker** 44:50 Nice.
**Robert Niedziela** 44:51 Because there's no none, there's no none.
But this was the next I wanted to go into, because if we consider known as a kind of blow to prevent, for example, customizers to add new stuff into the list.
Then how we can get this behavior with declarative config?
The customizer doesn't know that we want to prevent adding, more stuff to the list.
**Jack Berg** 45:22 So you're saying none is more than just none. None is doing… performing two functions. It's instructing the SDK to say that there should be no propagators, and it's instructing customizers that, you know, the user's intent is to have no propagators, and you shouldn't try to mess with this.
**Robert Niedziela** 45:39 That's how I see it was used.
In few places.
**Jack Berg** 45:46 Oh, that's tough.
**Robert Niedziela** 45:48 Yeah.
**Jack Berg** 45:49 Because the specification does not have any notion of these SPIs, these customizers. That's like a Java-specific thing, so nobody else in the specification conversations will, you know, be understanding of this point of view. They don't care.
**Robert Niedziela** 46:07 I understand.
That's something maybe we should think about, if we can get somehow this behavior also in declarative config.
Maybe… Start some discussion about it.
**Jack Berg** 46:24 Okay.
**Trask Stalnaker** 46:25 issue, and explain to you the use case.
Just… Okay.
Because I…
**Jack Berg** 46:36 I actually think customizers in general with declarative config are, like, sort of suspicious. We added the SPIs, they're there. You can go and customize the user's configuration model, as a… as a distribution.
But, like, one of the core tenets of declarative config is, like, what you see is what you get.
you write your content in a config file, and that's how the SDK behaves, and customizers break that. And so, I think, probably, maybe this is what you're getting at, there… there might be… need to be some thought given to whether there should be, like, you know, general-purpose capabilities for a user just to say that customizers should not play a role here. I want to disable customizers altogether. I really want this what-you-see-is-what-you-get behavior, and I don't want anybody messing with it.
**Robert Niedziela** 47:31 Yeah, it does make sense. The issue might be with… current customers that was used to, for example, specify just one thing, and a lot of stuff happened automatically behind the scene, and now they will have to somehow generate a piece of YAML.
**Jack Berg** 47:56 Yep.
Yeah, I just think, like, you know, it's… with this nun situation, giving an instruction to customizers.
Maybe we're gonna run into that same thing with other bits that the customizers could influence.
Right? So, like, is propagators the only place where somehow there's, like, a hidden contract between the system property and the customizer? Or, you know, will we see that with exporters? Will we see that with resources? Will we see that with processors? And so on?
And if so, like, you know, do we need to think more generally?
But I think… I agree with Trask. I mean, I think the best place to start is just open an issue.
**Robert Niedziela** 48:42 So, there's already some issue, opened that few people made some comments on it.
Yeah, so maybe I'll later on send a link to it.
**Jack Berg** 48:55 Okay.
**Trask Stalnaker** 48:57 In the Java repo?
**Robert Niedziela** 48:59 In, no, it's not in Java repo. Actually, it was about handling known value.
**Trask Stalnaker** 49:06 Oh, yeah, but I think.
**Robert Niedziela** 49:07 in…
**Trask Stalnaker** 49:08 This one, right? It's back, yeah.
**Robert Niedziela** 49:11 Yep.
**Trask Stalnaker** 49:12 But I think the… You're asking about… It's gonna be different. It's two different things, yes, exactly.
**Robert Niedziela** 49:18 But for the collaborative config, I will create another issue.
**Trask Stalnaker** 49:22 But specifically, the question you have about customizers, because as Jack says, customizers are a Java thing, so if you can, like, outline You know, the specific use case of, you know, this is what a user wants to do, this is how they're doing it today, how will they get… achieve the same Effect in declarative config.
**Robert Niedziela** 49:46 Okay, I'll create another issue for Java, yeah.
**Trask Stalnaker** 49:51 Bruno.
**Bruno Baptista** 49:53 So, these customizers, they, they have a useful usage, part… So, when you have a flat configuration with, like, with declarative config, all the configuration has to happen At startup, all at the same time.
if you have these customizers, it allows you to do other things. So, in Quarkus, what we do is, at build time.
we build… Some of these structures, beforehand.
So when, we start the… well, the JVM, we already have bytecode, That uses that.
That's one of the optimizations that we have.
If we don't have these type of facilities, we will have to do some additional magic.
Dude… To build this…
**Jack Berg** 50:52 I don't.
I'm not talking… I don't think we should take away the customizers, just to be clear. I think it's… it is an important facility, it's just… I think at least some users sometimes are going to be confused at, you know, I wrote this content in a YAML file, and that's not how my SDK is behaving.
And so, like, maybe we should have a way to disable them. Maybe that's… the default is that they're enabled, but we should maybe give the users the ability to override that default and be like, no, I really meant it. This is… this is the behavior of the SDK I want.
**Bruno Baptista** 51:28 Maybe the customizers, if you are using declarative config, should be off by default.
And if someone wants to activate them to do some kind of magic, well, they can.
**Jack Berg** 51:42 Right? Maybe, like… It's not clear to me yet.
**Trask Stalnaker** 51:47 So, Jack, for declarative config, I thought that the customizer… was going to just operate on the YAML.
**Jack Berg** 51:58 It does. Right now, yeah. It operates, well, on the in-memory representation of the YAML, so, like, a configuration model is what we call it.
**Trask Stalnaker** 52:05 Yeah.
And so that's… you're talking about, that's what you're talking about when you're talking about Preserving customizers for declarative config, or are you talking about program at the… the existing style.
**Jack Berg** 52:22 Well, so we said… actually, so that's the only SPI that's available right now, or… but there was conversations about adding additional customizers to declarative config, because, Because of this. So, declarative config, despite our best intentions of having every configuration option available and represented in it, there… there are… there's gonna be, like, a long tail of Java-specific configuration options that don't make it in. Like, think about this throttling rate that we just talked about. That would never get added to… the, declarative config specification. And, there's at least one more, one or two more that came up in the context of exporters. So, the idea is, like, hey, maybe we should still have.
**Trask Stalnaker** 53:11 authentication.
**Jack Berg** 53:12 Authentication, exactly, that's the one. Maybe we should still have programmatic customizers, not just the model, but programmatic customizers available as a sort of escape hatch for when the declarative config schema isn't expressive enough.
And, we either discussed it or actually merged a PR that did that, I'm not sure.
I gotta pull it up, I guess.
**Jason Plumb** 53:40 And potentially for distros that are doing, like, wacky things, I guess.
**Jack Berg** 53:46 Like, authentication. Like… It's not that it's wacky, but, like, you know.
**Jason Plumb** 53:51 Yes.
**Jack Berg** 53:51 Maybe you need to have some sort of, like, retry pattern, or, like, you know, dynamic authentication. That's a very real thing, right?
**Jason Plumb** 53:59 Yep, yep.
**Trask Stalnaker** 54:01 I like the, I mean, I like leaning into the YAML, auto customizer, because that partially addresses the what you see is what you get. It's like, at least we can…
**Jack Berg** 54:17 Print it out again, yeah.
**Trask Stalnaker** 54:19 Yeah, and be like, okay, this was the YAML that the user provided, here's the YAML that the resulting YAML from the distro, or whatever.
And then limit other things.
**Jack Berg** 54:35 Yeah, exactly.
So, we did not merge this PR. I was… somebody had opened an issue about this exact thing, I think it was Authenticator that was driving them to… was their use case, and I think I… I invited them to, you know.
you know, add programmatic customizers, and on a case-by-case basis. So don't do the kitchen sink like we have in the auto-configure module today. Just, like, add the programmatic customization capabilities on a need-by-need basis. And, you know, the exporters would be the first thing.
But it didn't get merged, it was just an idea. I just confirmed.
**Trask Stalnaker** 55:16 And hopefully even authenticators should… I mean, authenticators specifically should be supported. We need to get there in declarative config.
There's a spec… there's some spec issues open about… I think, Gregor opened a spec issue about defining an authenticator object at the SDK level that then we could have named authenticators, and you could plug those into the exporters.
**Jack Berg** 55:46 Right.
**Bruno Baptista** 55:50 Just mind that the authentication might be closely related with the clients that we are using in the Explorers.
**Jack Berg** 56:02 The, the senders?
**Bruno Baptista** 56:04 Yeah, the sender.
**Trask Stalnaker** 56:06 I'm working on that, Bruno, by the way.
**Bruno Baptista** 56:09 Thanks very much.
**Trask Stalnaker** 56:10 We hear you.
**Bruno Baptista** 56:11 Yeah.
**Trask Stalnaker** 56:14 Cool, we have hit our… time window, any… Bing… Left that anyone wants to raise?
**Robert Niedziela** 56:27 Just one information for you, Trask, probably. I think I remember why, the, instrumentation is released before country, because there is, JMX… I mean, JMX metrics inside in instrumentation that is used by JMX Scraper in… contribute.
**Trask Stalnaker** 56:51 Yeah.
**Robert Niedziela** 56:51 There was some discussion about it some time ago, and we agreed to…
**Trask Stalnaker** 56:56 We also have dependencies in the other direction, though, too.
**Robert Niedziela** 57:00 Yep.
**Trask Stalnaker** 57:01 alright.
Thank y'all.
**Robert Niedziela** 57:07 Thank you. Bye.
**Jack Berg** 57:08 See ya.
**Jason Plumb** 57:09 Are you…
