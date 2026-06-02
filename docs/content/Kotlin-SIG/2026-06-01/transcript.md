SIG: Kotlin SIG
Date: 2026-06-01
Duration: 48 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 03:44 Let's give it another minute or two and see if Hansen or Jason or anyone else shows up.
Maybe VRL.
**Hanson Ho** 04:15 Hello?
**Jason Plumb** 04:18 Hi, hi!
**Hanson Ho** 04:22 Oh, last week was canceled. Cool, perfect.
Hey, Fran.
**Francisco Prieto** 04:31 Hey, everyone.
**Jason Plumb** 04:32 Hey…
**Francisco Prieto** 04:34 I'm back.
**Hanson Ho** 04:36 Nice.
**Jason Plumb** 04:37 Welcome, welcome.
**Hanson Ho** 04:39 Jamie's not here, because he's on pat leave. He'll be gone for… 6 weeks or so, so…
**Francisco Prieto** 04:47 Nice.
**Jason Plumb** 04:55 Well, go ahead and add yourself to the agenda here, and any topics that you wish to add.
I've preloaded a few things that came up during the week.
Apparently, I was just having a lengthy conversation with myself, but I think there were some talking points here.
Alright, so while we're getting started here, I'm just gonna jump into the first one. So, my question was, why do we publish… separate artifacts for each platform into Maven, right? So, four semantic conventions, right? This is the main thing I care about. So.
for the SEMCOMF, we have all of these, right? So we have different platform targets for each of these. So my first question was, why do we do that? And also, what is this?
Like, this is the one that's not… this must be, like, the API or something. Anyway, I… I found it confusing when I… when I stumbled across this.
And then… Follow-up questions are, is it really necessary Do we… is it just… when you do KMP, is this, like, what you have to do? Like, you have to publish separate artifacts for each platform? I… and I think I convinced myself the answer is probably yes, but I would love some help in understanding that. And then, the other question was.
do we even need to publish these? Like, who… who do we expect to use these, right? Because these are coming out of the same… project, so for publishing them, I think we kind of have to assume that we will have users that are consuming them.
But do we need to? Because if these only serve the rest of the project and instrumentation, then maybe we don't need to. But then I'm like, oh wait, yeah, I actually want these from Android.
So… Let's start with that.
**Hanson Ho** 06:51 I think they do need to be published, just because if they're going to be consumed even internally by… by the existing modules within this, they need to be published. Now, I have no idea…
**Jason Plumb** 07:03 I do.
**Hanson Ho** 07:04 Yeah, so I don't know any… I don't know anything about… whether or not, especially if there isn't platform-specific things in there, whether or not there needs to be a different module, or, sorry, artifact for each, implementation, or for each, platform, because I don't think… I don't think everything is duplicated, right? Like, there's… there's a bunch of ones that don't have native code that don't or sorry, only, only, Kotlin. Kotlin being native, only if Kotlin, code, don't have parallel artifacts. I just don't know about KMP enough. Like, if you take a look at the directory, like, are there… are there ones, the published artifact directory? Like, is it, is it… Potentially only, an issue, that we forgot to exclude, the SEMCOM one from publishing additional stuff. Like, is… is the API module, for instance, I think, have any… have, like, ARM64, ISO… iOS…
**Jason Plumb** 08:10 Yeah, I mean, we have all of these, right?
**Hanson Ho** 08:13 Every single one?
**Jason Plumb** 08:16 Well, these are… okay, so API… it's… API is what you asked about, so it's these, right?
**Hanson Ho** 08:20 Yep. Right.
**Jason Plumb** 08:21 Yeah, and Android. They're just not… they're in alphabetical order.
**Hanson Ho** 08:24 Yeah, yeah, yeah.
So I guess that's it.
**Jason Plumb** 08:34 So, help me understand why we need to publish it, because if there are modules in here.
Oops, that's a typo.
If there are modules in here that are using… This, like, as a dependency.
Shh!
GradleCon, that's the one I wanted. So, like, if there's a… yeah, so, like, if Core is depending on SEMCOM, right, that doesn't have to be published for that dependency to work, right?
So that was my question, is like, why do we have to publish these at all? And if the answer is because we expect people to use them.
Right, this doesn't mean that it has to be published.
to Maven.
**Hanson Ho** 09:22 No, no, but… If it's not published to Maven, at build time, this should be included. Is… is that what you're… what you're saying? That people just can't indirectly… sorry, without, referencing core, reference Semconf?
**Jason Plumb** 09:43 So, if there are places in core that reference SEMCOM, then yeah, I mean, through… through… like, they need to be… available, right? So if it's a separate module, then they would either need to be I don't know, I guess shading is a Java concept, so, like, KMP is breaking my brain a little bit here.
**Hanson Ho** 10:05 I, I think… I think… I think I need to… research world.
**Jason Plumb** 10:14 though, Hanson, if they weren't published, and this declares an API dependency, somebody depending on core would still need to somehow resolve that as a dependency, and if they weren't published, they couldn't do that. So I think it's simply that simple. Okay, so I'm content with that being yes.
Yes.
**Hanson Ho** 10:36 I think, I, I think I… so, so… them needing to be published at all, I think I'm convinced that that is true. Each platform, having an artifact, I'm more or less convinced, given that API, is that way. If there's a whole bunch of.
**Jason Plumb** 10:55 Yeah, that way.
Yeah…
**Hanson Ho** 10:59 It's just super messy, like, another thing to do would be to look at a KMP library, or rather… well, yeah, a KMP library, that, like, is it always gonna be like this? Where, like, this is not super, I guess it's quite a mess. Like, you can't even, like, because of the alphabetical sorting, you know, sometimes you can't even tell that, oh yeah, there's Android there, just because of the way things are. I would take a look at, like, another KMP project, and then see if it suffers from the same, unsortedness, or rather, unorganizedness, as this. I know recently in KotlinConf, they announced, a restructuring of, projects, for KMP, but that's projects, that's not, you know.
Maven. So, I don't know if they're, like, kind of aware of the problem, and they're just kind of, like… Figuring out how to solve it.
**Jason Plumb** 11:59 Yeah I mean, definitely this is hitting… the edge of my understanding. KTOR, just to pull up one of them, All of them too, right?
**Hanson Ho** 12:11 Yeah.
**Jason Plumb** 12:14 Okay, so maybe this is just the… The way that you do it, and when you're… when you're targeting for a specific platform, that's kind of… your dependency tree is all within that platform, and that's… how everything's happy. I guess I'm also okay with it, I just wanted to check in and make sure that it's absolutely required, and it looks like it, so I'll just make a note about KTOR doing the same thing.
Okay.
**Hanson Ho** 12:51 Might rope the other Jason into this, so he can help, answer some of these questions. He may be more familiar with this than I am, certainly.
**Francisco Prieto** 13:02 Cool. If we did want to publish that same government module, we could try with compile only, if we only use it on compile time, but I'm not sure if that would… Work in this case.
Instead of using implementation or API.
**Hanson Ho** 13:23 We do need it at runtime, so, it has to be packaged somehow. So, when the AP… so when we build it, certainly we need it, but when we run it, I think it's… I think it's referenced. I don't think… I don't think the references are inlined. Are they?
**Francisco Prieto** 13:40 isn't just… Values, like, const val… I'm not sure what's in that module, I don't remember from.
**Jason Plumb** 13:48 It is mostly just const… constant values, but let's go look.
**Hanson Ho** 13:58 I'm pretty sure it's… it's mostly just that, but at the same time, there's no… nothing structural in the module declaration that says everything might be in line if you were, you know, using something that does that. So these are all.
**Jason Plumb** 14:15 generated right from Weaver, so if we just pick one like Cassandra… Yeah, these are what they look like. They're just a bunch of constant strings.
But yeah, I don't know that there's any sort of inlining, and then it gets more complicated by, like, some enums, right?
**Hanson Ho** 14:28 app.
Yeah.
I think it's fine, like, even in theory, you don't want to include core and you want to include the SEMConv to do some validation or something like that. That's… possible. That's obviously a made-up use case, but I don't see the downside of publishing these. Like, these aren't, like, test artifacts or something like that, that we really, truly want to keep internal. These are… these are public. In fact, in other platforms, they'd be in a separate repo. It's just more convenient for us to have them in the current repo, so…
**Jason Plumb** 15:05 So it was a surprise to me, but that's just me being kind of inexperienced and naive around KMP stuff, so I'm just making a note that I think we're mostly okay with it.
**Hanson Ho** 15:14 And in fact, having it completely dec… well, not having it decoupled from, core and API means that, like, in Android, if we want to use it, we don't have to bring an API, we can just bring this in, and it'll be, like, super safe, because all we're doing is referencing, well.
I guess this has an API dependency, doesn't it?
If it does, okay, never mind, forget it. I was thinking these were just strings, but I think they have, like, like, attribute key and things like that, right?
**Jason Plumb** 15:45 Not in Kotlin, we don't have attribute key, it's all just string keys right now.
**Hanson Ho** 15:49 Okay.
**Jason Plumb** 15:50 But what's… I think we need to leave room for an API because of… well, the enum thing's a little bit weird, but I suspect that eventually, with complex attributes, there might be object structures that get created from Weaver.
**Hanson Ho** 16:04 Oh, yeah.
**Jason Plumb** 16:05 So, I think we need to leave room for it.
I just don't know… That we have it today. So, like I said, I think I'm okay with it.
Yeah. I'm not gonna lose sleep.
**Hanson Ho** 16:17 I, I, I think it, I think it, it, it, it, cement… I think it should be public, like… So if it weren't, actually, I think we… I would say, hey, we should make it, like, public, independent.
**Jason Plumb** 16:30 Yeah.
So, selfishly for Android, I was working on… Android takes dependency on the Java semantic conventions. I recently did an exercise to see what it would be like to depend on these, right? Because we're moving Android in the direction of being more Kotlin first, and… I think we all like that idea, and so I did the… and as part of that, I was like, oh, it's interesting, because all of the Java stuff is packaged I'm jumping ahead a little bit, but all of the Java stuff is packaged in a separate Java package called incubating, so anything that's not stable Is in an incubating package, and then the class names in which the constants live also have incubating in the name.
**Hanson Ho** 17:20 Hmm…
**Jason Plumb** 17:20 So when you're referring to, like, the Cassandra, just to pick another contrived example, right, all of these we annotate in Kotlin with the incubating API, And that's because none of these are stable.
And if they were, we would, in Colin at least, the weaver would just drop this, it would no longer be incubating. In Java, they get generated in a completely different package, and it drops the name incubating from the class name.
So that's one thing that we differ, and I just wanted to call that out as a difference and say, do we like it better? Like, do we think that this is enough of a signal to the users that the… that the CENCOM that they're using is not stable.
**Hanson Ho** 18:05 I don't think so, especially since we have a lot of the APIs right now that are under the same… well, we have to, like, say, hey, you know, it's cool, it's incubating. I like the explicitness that we basically have two packages, one that is, ones that are stable, ones that aren't, could be called out by… in the file. So I… I do like the split in the packaging, personally.
**Jason Plumb** 18:35 I think that's where I came from originally, too. I did want to call out the negative in that It does clutter up the Gradle that you have to have two separate dependencies in your Gradle script.
And… sometimes, if you're only using stable, and you… you want to pick one up, you have to, like, go and add it, and then if… if eventually you're only using stable, you have to go back in and remove the incubating, and… you know, it's a little… it's a little bit tedious that way, but in Java, yes, super obvious when something stabilizes.
I don't know what this link is.
**Hanson Ho** 19:08 So the… we could still theoretically package everything in the same, module, right? It's just the… the package that's gonna have a different… or a package or a class name, or something that differentiates it. So hopefully, none of the Gradle… like, you take in SEMCOM, you get both the incubating and the non-incubating, Or is Java the other way? It's like two separate, modules.
**Jason Plumb** 19:34 It's two separate modules.
**Hanson Ho** 19:36 Or at least they're…
**Jason Plumb** 19:37 Sorry, I think there… it's complicated in a job, I think there's only one module, but I think they publish separately.
Let's find out. I forget.
**Hanson Ho** 19:49 So you can have, like, version 1 is stable, and version.
**Jason Plumb** 19:52 No, there are two separate modules, I take it back, there's two.
They treat them as completely separate. And then the build tooling that generates them from Weaver just knows where to target these.
**Hanson Ho** 20:04 I'm less excited about having two separate modules.
**Jason Plumb** 20:07 Yeah.
**Hanson Ho** 20:08 just because we're all… I think we're always gonna have tons of incubating stuff, just because of the stability, what you call it? The life cycle to this is quite long.
**Jason Plumb** 20:20 Yeah.
**Hanson Ho** 20:26 I feel like this is something we could improve on in the future, but it's something… not something that we need to do now, now.
Since nothing is stable, for…
**Jason Plumb** 20:36 Oh, this… I didn't realize this got merged 9 hours ago, I've only been awake for a few hours, let's see.
Okay, so.
**Hanson Ho** 20:41 Oh, I didn't merge it.
**Jason Plumb** 20:44 You approved it, though, huh?
**Hanson Ho** 20:46 I did! I did, but…
**Jason Plumb** 20:50 I was like, I don't know if we're ready for this. I mean, I didn't mark it draft, to be fair, so… YOLO. But, Just to give people a sense of, like, what it looks like to make this change, right? So, I did have to add in… this incubating annotation.
And for each of these, where we each… and this is just a test class, but for any class… Like, let's pick, like, this one.
Any class that does use these annotations, you have to opt into it.
Right? So you have to say, I'm aware that this is incubating, and I wonder if there are any that are not. Like, some of the HTTP stuff, probably.
**Hanson Ho** 21:32 you could opt in at a higher level. Like, you could opt in for a class, a file.
So, if it's, like, reducing clutter, we could certainly do it at a higher level.
**Jason Plumb** 21:43 Yeah, like, the usage of the sanitation can move up to the class level, totally.
And I tried to pick the most narrowly scoped one. Like, when I was doing this, I was just like, I want to put it at the closest to where the usage is, that way it's not just a blanket, like, we'll take anything.
But I don't know what best practice is there, honestly.
**Hanson Ho** 22:04 I remember looking at this, it doesn't… we're not bringing in, like, Everything in the repo, right?
We are relying on the fact that this is… this is public, to only reference, the SEMconv.
**Jason Plumb** 22:20 What do you mean?
**Hanson Ho** 22:23 Like, are we adding, we're not pulling in, like, the Kotlin API and stuff, right?
**Jason Plumb** 22:29 No, not yet, no, only the semantic convention, so…
**Hanson Ho** 22:33 That's, that's what I thought.
**Jason Plumb** 22:34 It looks like this, right? We're dropping… we're dropping the dependency on OTel SemConf Incubating, which is the Java version, and instead we're getting libsemconfKotlin.
**Hanson Ho** 22:47 Does incubating include, like, the stable ones? Is that why… No.
So we are still referencing the Java stable semconf.
**Jason Plumb** 22:56 No, in fact, so you'll see some where we had them both.
Maybe.
**Hanson Ho** 23:02 Okay, okay.
**Jason Plumb** 23:04 Like, here's the stable one, the non-incubated one.
**Hanson Ho** 23:07 Some of them are just using incubating. Okay, got it, got it.
**Jason Plumb** 23:10 Yeah.
**Hanson Ho** 23:11 Cool.
**Jason Plumb** 23:12 I thought there was at least one that had both of them, but… I don't… I can't see it right off.
But yeah, there were definitely two separate dependencies that we take in some different modules, and we just… this collapses it now to one, which, again, kind of nice, actually.
And I was surprised by this, because, like, this I thought was pretty decent, and this makes it easy to find all of the places that are not yet SEMCOM-stable, right?
You can just look for this opt-in incubating.
It's a little bit weird to call it an incubating API when it's not really an API. I wish we had, like, an incubating Senconf.
Like, this is… is this our… this is our annotation, right?
**Hanson Ho** 23:58 Yeah, it must be ours. I wonder if it's the same one as the one… it must be, I doubt there's two incubating, I mean, it is API in the sense that, It is a dependency that can break, and can break your code.
**Jason Plumb** 24:17 It's true. The fact that this exists in SEMCOF makes me want to rename it.
**Hanson Ho** 24:23 Hmm… I don't think so.
**Jason Plumb** 24:26 I don't think about that.
**Hanson Ho** 24:27 Yeah.
**Jason Plumb** 24:28 Yeah.
Okay, I'm gonna make a note of it, though, just because we talked a little bit.
is a little bit… not Kotlin, it's more of an Android question, but do we think that there's any risk in Android depending on these now?
like, because Kotlin is pretty young, do we think there could be Thrash, and maybe we… Feel pain later on because of that choice.
**Hanson Ho** 25:03 I mean, these are generated from… from, excuse me, the YAML. So, if there's Thrash, it'd be things like, you know, package names and things like that. And I think that that would be internal to, our code, so if we have to, like… if there is thrash, it shouldn't affect, users of this. Unless they reference this as well, which in case… in that case, they are explicitly saying, I'm opting into this perhaps thrashy, API, or…
**Jason Plumb** 25:42 But if we did a package split, then Android would have to… It would be a breaking change for Android, which is fine, we would just have to recompile before we… yeah.
**Hanson Ho** 25:51 The thrash is managed by the Android… Android people who maintain the Android project, which is us, so it's… it's left-hand, right-hand kind of thing, so…
**Jason Plumb** 26:01 Yep.
Okay.
Alright, I'm feeling… I'm feeling better about this now that we've talked it through a little bit. I want to make sure there's room for Francisco or David to say any words about this.
Or Carlos.
Whatever.
Before… Okay, well, so you brought this up earlier, Hanson.
attribute Q, you know, we just have these opaque strings right now as part of our API.
And it does make it difficult to generate these attributes that are strongly typed.
And just by looking at… I don't know, if we just pick any of these… it's unclear to tell what the type of these are, like, these are all names, so they're gonna be strings, but, like, is the result an integer or a string? Like, I don't know.
And then… if you wanted to do anything fancy with, semantic conventions in Weaver, if you don't have the type as part of our interface.
It's a little… clunky.
So, I was just asking if we've thought about any ways of making it You know, clearer, better.
**Hanson Ho** 27:16 So…
**Jason Plumb** 27:17 I should have been more… I should have been clear about this example, because it… At 9.30 in the morning, I don't remember what exactly I was looking at, but there was something in Java that's, like, very clear with the types, and there's a… there's something that isn't in Colin.
**Hanson Ho** 27:32 So, I think what we defined are the key names, and not the keys.
I think what we need are… if we want typed, we would be wanting key name, or sorry, wanting keys. So, I do think that's something that we should have, because as you said, if all we're looking at is the key… all we have is the key name, then we don't know how to actually put it in there. We could use the same key name, for… different keys, you know, specifically. Like, foo could be both a boolean and a string.
And… for SEMCOM, they are mapped to a type. So, I do think either we're missing a layer, like, like, the key names being strings, that's fine, but there may be a layer that is effectively, keys that use that, and probably that's already in Weaver. Like, we could generate, like, typed keys. I assume the Java ones are typed, right? Or… Or are they…
**Jason Plumb** 28:46 Java… this is, like, already almost 6 years old now, but Java went through a lot of effort to sort of make a very… type-enforced API, which is not necessarily Java's strong suit, which is why… I think that's why the attribute key exists. I don't think that class or that concept of a typed attribute key, I don't think that exists in the spec.
I think that it's something that Java chose to do.
Because at the end of the day, all attribute names are strings, right? Like, if you go to any backend or any collector, what you're seeing there are strings.
And… the way it's manifested in Kotlin right now is that we've taken the types and put in the setter names of the mutators.
Which I don't think is the worst thing, it's just, you know, it's a little bit redundant, and you can't remove these. Like, I don't know of a clever way of overloading setAttribute with different types and doing it uniformly.
**Hanson Ho** 29:45 I wanna say we… I want to say we tried.
**Jason Plumb** 29:47 It falls down here. Yeah, yeah, it falls down here because it was type erasure, at least in the JVM world.
**Hanson Ho** 29:54 So, if key is typed, Instead of a string.
**Jason Plumb** 29:59 Yes.
**Hanson Ho** 30:00 Then we could figure out the type based on that.
**Jason Plumb** 30:04 Yeah, but even with… even with generics, I don't know that you can do that. But that's… I think that's why AttributeKey in the Java world came.
**Hanson Ho** 30:10 to exist.
**Jason Plumb** 30:12 Is to work around that generics problem.
**Hanson Ho** 30:15 I wanna… maybe Fran might remember this, but I wanna say we tried to make it… completely… like, not having… because obviously specifying, like, 10 different, you know, set attributes with the explicit name in the… in the type, in the fun… that's not… that's not ideal. I think getting here is no accident. I want to say getting here… there was a reason why we needed to do this. I don't know, maybe it was backwards compatible with Java or whatever, but actually, I doubt that.
But… yeah.
**Francisco Prieto** 30:51 I think I remember a PR that added every single, type, functions, but I don't remember why. I think we started with a…
**Hanson Ho** 31:03 Give me a task to look this up, in the history. It's probably gonna be in the old repo history, so I have to go dig back into the, the Embrace, The origin, and basically do some archaeology.
**Jason Plumb** 31:19 That's cool. That works for me.
**Hanson Ho** 31:21 There's no way that's deliberate. Like, there's no way that's something that we want.
**Jason Plumb** 31:27 I mean, I also ask in the context of wanting… we're wanting to stabilize the attributes API, and I think we're pretty close, but it does mean that we're stabilizing this, right? Like, this is the API.
**Hanson Ho** 31:39 Yeah.
**Jason Plumb** 31:41 I wanted to raise that again. After kind of doing the working exercise of putting these to use, I want to… just… I wanted to raise some questions and make sure we're on the… we're… we think we're on the right track. And I… I think we are. I think it's fine.
**Hanson Ho** 31:56 I would like this not to be that way, but I suspect that… We ended up here because we had to.
**Jason Plumb** 32:04 Yeah, okay.
Alright, well, I think let's move on. Does anybody have anything else to say about SEMCOMF?
**Hanson Ho** 32:13 Oh, I'm really happy to see it be in… it's the first thing that's in… That's in Android, so I'm really happy to see it.
**Jason Plumb** 32:21 It's terrifying.
**Hanson Ho** 32:23 Yeah.
**Jason Plumb** 32:23 did a prototy… I think Jamie did a prototype with one of the APIs that was out there. That was also really nice, yeah.
Okay, so… AGP813.2.
So this build is broken.
And I think I spent some time tracking it down. It's because… 8.13.2 requires, of the Android library, requires an update to… Android Gradle plugin 8.13.2.
So for Kotlin, are we okay upgrading to 8.13.2? I think was my question.
It's the min-supported Gradle, that's what the problem is. So, min-supported Gradle…
**Hanson Ho** 33:06 Yeah…
**Jason Plumb** 33:09 He's right.
Great.
**Hanson Ho** 33:10 I don't think we can.
I think that the men support it.
We'd have to be dropping… older Kotlin versions, or something like that.
**Jason Plumb** 33:23 Huh?
**Hanson Ho** 33:24 Or, or, or, or Gradle or AGP, or, or something. Well, obviously, AGP, we're dropping a whole bunch, or rather, upping a whole bunch. I want to say that, I don't want to say we can't do this, because of a reason, but we should make sure the reason is apparent, because somebody will go look at this and be like, hey, why not?
**Jason Plumb** 33:47 So, 8… so the version that we're using to compile, I believe, is 9-something.
**Hanson Ho** 33:54 Yup.
6.94, 9.5, or some super new one.
**Jason Plumb** 33:58 Yeah. Which is fine.
Which… which I think all the… I don't know, like, that doesn't propagate… downstream, right? That's just for our build.
Like, if we did bump this up to min-supported Gradle 8.13.2, which is what this requires… Then it compiles, like, this build would no longer be broken, but what's the implication there? That someone who checks this out… What?
**Hanson Ho** 34:26 someone who has to… who wants to compile, or include, hotel Kotlin in their project, previously they were able to use, Gradle 8.0, and now they have to upgrade to 8.13, and that probably has a bunch.
**Jason Plumb** 34:42 That does propagate downstream, then?
**Hanson Ho** 34:44 The min, the min, yes. The one we compile with doesn't. Unless we are overloading what this variable is, in that we are both using it to compile.
As well as, using it as the minimum. Got it. I know Fran's looked at this a ton before with AGP, so…
**Francisco Prieto** 35:07 everything that you upgrade ends up breaking something else. It's usually you need to just bump your minimum.
Require version, and hope for the best.
**Jason Plumb** 35:18 So we're over 3… we're over 3 years old on Gradle 8. What's the other… the thing is, Lost track here.
**Hanson Ho** 35:29 I think for Embrace, we also have this requirement for the min version, and I don't remember what's… what this is allowing. It could be, like, a min SDK, Could be a certain… I have to take a look.
It feels like going from 8.0 to 8.13, like, there's a reason why we weren't on 8.12 or 811 min.
**Francisco Prieto** 35:56 So… We had a detailed document stating, like, why every requirement was.
Worcester. Let me check if I can find it.
**Jason Plumb** 36:06 Oh, congratulations, Public Archives!
Is this the right repo?
**Hanson Ho** 36:14 Yes.
**Jason Plumb** 36:16 Let's see, am I spelling it wrong?
**Hanson Ho** 36:18 Oh, it's min-AGP, it's probably Min AGP.
**Francisco Prieto** 36:21 Oh, no, but we had it on the Embrace SDK, not on Embrace OpenDeremetry.
**Hanson Ho** 36:27 Right.
**Jason Plumb** 36:27 Oh, the SDK.
Let me find it. Since we're on this topic and the agenda's late.
**Hanson Ho** 36:39 Unless, David or Carlos has any agenda topics that have been added and we haven't looked.
**Jason Plumb** 36:44 This one?
Yeah.
**Francisco Prieto** 36:46 Yes.
**Jason Plumb** 36:47 Okay.
I can't find it.
**Hanson Ho** 36:55 It's probably, like, min-AGP, let me check…
**Jason Plumb** 36:58 I'm just gonna look across the entire org.
No, I'm not poke.
**Hanson Ho** 37:05 It's Min AG… it's Min AGP version.
**Jason Plumb** 37:08 Is it this thing?
**Hanson Ho** 37:12 I'm looking at our source code right now.
**Jason Plumb** 37:19 802 in the Android SDK?
**Hanson Ho** 37:24 Yeah, it's 8.02. Okay.
I remember it was that specific one because there was some… some bug.
In the earlier ones that we don't…
**Jason Plumb** 37:33 Yeah, so you're… but you're basically, you're selling 8, so… I guess the question is, it sounds like… It sounds like we haven't yet answered this. Like, are we ready? And if the answer is… Yes.
then we bump this, and we merge this PR, and we move on. If the answer is no, then we close this PR, but then my question is, when do we decide that we're ready? Like, do we have a policy yet on when we bump these min versions?
Because we need something to prevent us from just going stale.
**Hanson Ho** 38:03 Yeah, the… so, again, put something on my to-do to find out, but, The reason that this is that low is to support… Something else that's low. so somebody's build chain being, not completely up-to-date.
it's probably, like, JDK, or, or, or Gradle, like, they want to use Kotlin 2.0 or something like that.
I suspect it's, it's, like, Kotlin 2.0. Like, I think if we go…
**Jason Plumb** 38:44 Yeah, I would love to understand what that chain is, first of all, and then once we understand it.
Like, when do we decide to bump up?
Yeah. Because I don't have a sense of that yet.
**Francisco Prieto** 38:56 We had a document on Embrace, I don't know where it was, but we pretty much stated, hey, we want to support, two years of that has Kotlin, and that forces us to support, like, Gradele 8, and that forces us to support, like, our main dependency, I think it was Kotlin, and then from Kotlin, everything else.
pretty much triggered. I don't know where the document is.
**Hanson Ho** 39:21 Yeah, I'll find the document, but I suspect it's Kotlin, because for a long time we were in Kotlin 1.8, because, and that required, like, Gradle 7.4, or something like that, an AGP similar version. So it's whether or not, this is something that we need to do.
Because forcing every… like, forcing everybody to be on Kotlin 2.2 or something like that, or 2.3 is… is… is… is a lot.
**Francisco Prieto** 39:54 Also, do we have something like the test harness in the OpenTelemetry repo, where we test against different customers with different Gradle versions?
**Jason Plumb** 40:03 I think Jamie… Jamie had a PR that was similar to that, though, or starting down that direction, I thought.
**Hanson Ho** 40:08 I want to say, it wasn't a Gradle.
test harness, I think it was a, a build project test harness, so, or not test harness, I think, like, it'll test against the Android build using those ones, but… Or, like, different apps. Well, I'll… I don't know, I should say.
**Jason Plumb** 40:34 Yeah, I don't remember either.
**Francisco Prieto** 40:37 I think I will need to do something like that for my current show, so I might just do it for both.
OpenTelemetry, and… because it's probably going to be pretty much similar.
**Jason Plumb** 40:49 Oh yeah, we could use that for sure.
Yeah, if you could take that.
**Hanson Ho** 40:52 task, I'd be a great friend. I'll take a look at… see if Embrace, we have that document internally, and that'll just be… Easier.
**Jason Plumb** 41:01 Cool.
**Hanson Ho** 41:06 Yeah, we should have a… we should have a similar doc. By the way, we should have a similar doc for… for, explaining, Our policy for updating dependencies.
Cause we should… it should be… Pegged to something, or something.
**Jason Plumb** 41:22 I thought we had something in…
**Hanson Ho** 41:26 Yeah, I think we, for Android, we want to support the min API, that, like, I want to say Google Play Services supports, or something like that.
**Jason Plumb** 41:38 We, yeah…
**Francisco Prieto** 41:44 Here it is, I found it.
**Hanson Ho** 41:49 Oh, sweet.
**Jason Plumb** 41:53 Yeah, we kind of bury this in versioning, but here it is in Android.
**Francisco Prieto** 42:16 That's pretty similar to what we had in Embrace, and… Yeah.
In Embrace, we are listing, hey, we are going to support four versions.
Behind the latest one for Kotlin, and then…
**Hanson Ho** 42:33 like, we're forced to move up as Kotlin moves up, so Kotlin, I think, is only backwards compatible for, 4 versions. It's current plus, like, 3. So when Kotlin releases 2.5, I think 2.1 stops working and things like that.
**Jason Plumb** 42:50 Got it.
**Hanson Ho** 42:52 So we will be forced to go a certain cadence. But, we don't necessarily have to use that. We could always go faster, or rather, require a higher Kotlin version, and therefore higher AGP and whatever, newer. But I… I think I… that's too fast for me. Saying, yeah…
**Jason Plumb** 43:21 unreleased quarterly? Like, is that a one-year cadence?
**Hanson Ho** 43:25 not quite quarterly. I wanna say… Almost yearly.
But we could take a look at the… what? Like, 2.3, I don't think is officially released yet. So…
**Jason Plumb** 43:42 Cool.
I was just seeing how that might map over to the calendar, but it sounds like it really doesn't.
Cool.
Well, I know that Hanson and I have both been pretty busy on reviews. We got some stuff in last week, but it's been slow going, so anybody who likes to review some of these open PRs, there are plenty right now, and the help is appreciated.
**Hanson Ho** 44:10 I'll be taking a look at… the rest, or the ones that have not been looked at today, at least, if not all of them. Or the reviews by real people, not, not, not, not, Renovate.
**Jason Plumb** 44:23 Yeah.
**Francisco Prieto** 44:23 I did that, and I think it's… most are already approved. The only one I didn't approve is the… 551, it's Variable Precision Threshold encoding, because it has a comment by Jamie, and… I didn't think my review was needed, but… Cool. Jimmy pretty much approved, but yeah, maybe it would be nice if I just approve it, because I think it's hanging there. This is just, Some changes that haven't been made, so… Yeah.
**Hanson Ho** 45:01 I'll take a look as well.
**Jason Plumb** 45:07 Sounds good. I had looked… I had forgotten that I even did this little exercise, and we didn't I forgot I did this.
So yeah, this is… this was a re… yeah, look at this.
**Hanson Ho** 45:19 Woof.
**Jason Plumb** 45:20 Yeah, I know, but it's just repackaging, so…
**Hanson Ho** 45:23 Yeah.
**Jason Plumb** 45:25 Yeah, so this is… this is… yeah, so if we wanted to mimic Java, this is what it would look like. You get incubating attributes, and… they're in an incubating package. That's the real difference, yeah. We talked about this, but I forgot that I had done sort of a demo for… Colin as well.
**Hanson Ho** 45:48 I wouldn't mind if it's in the same module, but, again, I'm not…
**Jason Plumb** 45:53 Make a new module.
Yeah, I mirrored it, you know, new module.
But we can decide, you know, we don't have to do this anytime soon. I'm… I think I'm warming up to the incubating API annotation. The more I see it, the more I sit with it.
And, you know, it might be a little bit more idiomatic in Kotlin to do that as well, versus always trying to mimic or mirror what Java does. And in cases like this, I don't know that it buys us a whole lot.
Other than it makes it very clear.
**Francisco Prieto** 46:27 I figured that adding a separate gradient model will make people more… cautious about using incubating stuff, and I don't think we want that.
**Hanson Ho** 46:39 I'm definitely against having a separate module, but having a separate package, I may even prefer, but I also think my taste may be not representative, so I don't want to be like, yeah, that's what I like, therefore everybody should have durian for breakfast.
**Francisco Prieto** 46:55 I think a separate package might be good, especially because you… when you look at the imports, you know, like, what… they get grouped together, and incubating is probably going to be at the end, so I'm not sure if… a separate package might be… Even better.
**Hanson Ho** 47:13 And it also means that, promotion, causes a bill break, which is actually probably a good thing. So we were… because it would be trivial to fix, because it's just a different import. But it will also be…
**Jason Plumb** 47:27 annotation does that. I wonder if you… if you say, it wouldn't, right, because it's scoped, and so you wouldn't know that something went stable.
**Hanson Ho** 47:36 I mean.
**Jason Plumb** 47:36 Yeah.
**Hanson Ho** 47:37 If you… even if you scoped it, that was this.
**Jason Plumb** 47:40 point. Yeah, exactly.
Yeah, hmm. Cool.
Alright, we hit time, I think. This is 45 minutes, right?
**Hanson Ho** 47:50 Yep.
**Jason Plumb** 47:51 Okay.
**Hanson Ho** 47:54 Thanks, folks!
**Jason Plumb** 47:56 Yep, thanks everyone.
**Hanson Ho** 47:57 broke.
**Jason Plumb** 47:58 Bye.
**Carlos Alberto Cortez** 47:59 Beautiful.
**Jason Plumb** 48:00 Steve.
