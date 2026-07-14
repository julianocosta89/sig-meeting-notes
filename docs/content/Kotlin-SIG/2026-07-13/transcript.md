SIG: Kotlin SIG
Date: 2026-07-13
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 02:36 Hey, Jamie. Hey, David.
**Jamie Lynch** 02:39 How you doing?
**Jason Plumb** 02:48 Well, hopefully I did a reasonable job of keeping the lights on around this place while you were gone.
It's kind of slow going, and I feel like I didn't give it enough attention, but that might always be the case.
**Jamie Lynch** 03:02 Well, I think it's one of those things where maybe it feels like not much is happening, but Coming back to six weeks of notifications, it feels like a lot happened.
**Jason Plumb** 03:13 I bet. I bet.
**Francisco Prieto** 03:15 Hey, Jamie.
See you work.
**Jamie Lynch** 03:18 How you doing?
**Francisco Prieto** 03:21 I'm good.
I do.
**Jason Plumb** 03:28 Definitely screwed up any momentum that we had had about two week releases, but we did get a release out at least.
**Hanson Ho** 03:38 Momentum is what you make of it.
relative slow down versus Continued progress.
Let's pick it back up and we're good.
**Jason Plumb** 03:53 Yes.
**Jamie Lynch** 04:27 I'll just give it a couple of minutes for folks to add more items to the agenda.
**Jason Plumb** 04:35 Jamie, did you see that we have this table in the API README now with stability levels designated?
**Jamie Lynch** 04:44 I did not.
But… is something I'll go away and have a quick look at.
**Jason Plumb** 04:51 Cool. Yeah, so the question was, we might internally have a shared understanding of what components within the API we're done with or that we consider stable. But because the API is versioned as one entire module, like one entire artifact, there's not a good way to send that signal or to track that.
**Jamie Lynch** 05:11 Mmhm.
**Jason Plumb** 05:13 I guess we settled on a table in the README for the API.
And then when everything is moved over to stable, we can get rid of that and remove the alpha suffix or whatever.
But until then, we needed some place to sort of track this. And we could have maybe done it with an issue. I don't know. This felt like a reasonable place to put it.
**Jamie Lynch** 05:35 -h Cool.
Yeah, I'm looking at that now.
**Jason Plumb** 05:51 It's also traditional on SIG meetings for the host to share their screen.
**Jamie Lynch** 05:56 Yes, sorry, out of practice.
**Jason Plumb** 05:58 That's okay. That's why I'm reminding you.
**Hanson Ho** 06:01 6 weeks of, baby brain.
**Jamie Lynch** 06:05 Yes, still going on.
**Jason Plumb** 06:08 Yeah, that lingers.
**Jamie Lynch** 06:19 And no frequency, but okay.
**Jason Plumb** 06:20 Yeah.
**Jamie Lynch** 06:29 Cool.
I will just make a start. I know folks.
Have more items, please do add them onto the agenda, and we'll discuss them as they come up.
So yeah, I guess this one… Has been partially answered.
by that table you just linked me to, Jason. So yeah, the Attributes API was the last thing I kind of remember getting stabilized before I left a few weeks ago, and Yeah, I guess I was just wondering… What should we review next?
What does reviewing it kind of entail, and… how it's best to track that, I guess. So… Yeah, like, we've done attributes. Do we need to do…
**Jason Plumb** 07:20 I think baggage was pretty close. I think baggage was pretty close. I think logging we called out as being also pretty close.
**Jamie Lynch** 07:26 Mmhm.
**Jason Plumb** 07:31 What'.
**Hanson Ho** 07:31 Not mine.
**Jason Plumb** 07:31 What is factory? I don't remember what factory even is.
Should I know what that means?
**Jamie Lynch** 07:39 Yeah. I believe that's just for stuff like in the DSL to initialize.
Yeah, to initialize objects specifically. So, like, if you want to… create a spam context. It's under the factory package, but it doesn't… map onto, like.
Hotel specification, or anything like that.
**Jason Plumb** 08:05 Okay.
Yeah, baggage and propagation would be great kind of as next steps. But I think just from memory, I thought we were pretty close on baggage.
Do we have a milestone?
**Jamie Lynch** 08:22 We… I think it might be under context.
Yeah, I'm also wondering whether it would be worth, like, creating separate issues for all of these, and then we can kind of… maybe, like, create, like, a checklist on each issue or something along those lines, so… Yeah, because, like, to now… now, to me, it's kind of unclear about what needs reviewing and what needs discussing, but maybe if we open that up, it'll become a bit… more concrete.
**Jason Plumb** 08:56 Yeah, yeah.
So looking at the milestone for the context API.
there's 2 issues that are still open, and 11 that are closed, so context looks pretty close. And one of them is B3, which I thought we got the B3 propagator.
**Jamie Lynch** 09:14 Yeah, I think we got PR.
Open for that.
**Jason Plumb** 09:19 Is it still open? Oh yeah, okay.
**Jamie Lynch** 09:22 Yeah, it's just… Waiting on a bit of feedback.
**Jason Plumb** 09:30 Probably for me, yeah.
**Hanson Ho** 09:34 No, I said I was going to comment on this and I didn't. This was two weeks ago.
But there's been comments since, so…
**Jason Plumb** 09:43 I think it's pretty close though.
**Jamie Lynch** 09:44 Yeah, I think it's pretty okay.
**Jason Plumb** 09:48 Cool.
And then the last issue that's open on that milestone is to create a coroutine-based approach for storing the implicit context.
That's kind of a doozy.
**Hanson Ho** 10:02 Mmhm.
**Jamie Lynch** 10:07 Let me bring up the milestone.
Yeah, that could be a… Interesting one.
**Hanson Ho** 10:27 Is this repeating? What like? What do we want at the end here like the one the There's the extension, or… The one that was… Existed a few… for a few years, that… that just puts the, Current contacts on ThreadLocal onto the… onto the, Oh, what aspect of coroutines is this? Anyway, it's the one that's kind of, you can screw it up really easily, but it kind of works as one would expect for a logo to work.
**Jamie Lynch** 11:09 I think… From what I remember.
Yeah, I think it's, like, thread-local based, so that when the co-routine switches on a thread, it will… Basically, updates.
What the current co-eating context is.
Yeah, I think… From what I remember, was it OpenTelemetry Android or OpenTelemetry Java had some sort of In progress.
Or maybe not in progress. Like, there was some idea for implementation on this, but it required bytecode weaving.
**Jason Plumb** 11:50 I think it's Java. I don't think it's Android.
**Hanson Ho** 11:54 I wanna say it's Contribs Repo, too.
**Jason Plumb** 11:56 Oh, really?
**Hanson Ho** 12:04 could be wrong.
**Jamie Lynch** 12:14 Okay, so… I guess for this, more generally, what I can do is I'm happy to go away and just create a few issues or milestones or whatever is needed to kind of track like, how we review the API and get it forward to stability, and… I guess that gives us… something… We can kind of like.
work against.
**Jason Plumb** 12:46 Carlos, do you happen to remember which kind of categorical area in the API we said was kind of next, like, close to being done?
Like, it looks like context is pretty close, and I think we said tracing and logging were also pretty close.
**carlosalberto** 12:58 Yeah, well… I would say context is a big one. It's a big piece.
**Jason Plumb** 13:05 Yes.
**carlosalberto** 13:06 By the way, I started doing, just for your information, some digging, because JavaScript has some similar challenges with context propagation, because they have two versions or layers, let's say, one for node, one for browser.
So I wanted to finish reviewing that and come back with my findings. But I could say context is important enough.
that… This should be, like, it should be, like, really, like, wrapping this up with whatever decisions DC comes with, and before we try to take other stuff. That would be my recommendation. But, if there's something after that, I don't know what's the current status of resources. Is that done? Completely?
Because that could be the other important one, along with attributes.
**Jason Plumb** 13:59 It's a good question. Resources is not even in our stupid table, is it?
**Jamie Lynch** 14:04 I seem to remember we've discussed it before.
We could… Yeah, we could see what the… Historical issues.
Save for that, and… And see what, like, we discussed together, or we can just go over it again.
Like, there's some other point.
**Jason Plumb** 14:29 So the resource doesn't live in the API.
I think that's the challenge.
**carlosalberto** 14:35 Right, it's an SDK component.
**Jason Plumb** 14:38 Yeah.
**carlosalberto** 14:39 So it can be postponed if you want that, but it will be an important sooner or later.
**Jason Plumb** 14:43 Yeah, and we have it, but it's not stable. I think more of the focus right now is trying to get the API stable.
**carlosalberto** 14:52 Yeah, so in that case, context for sure. Logging is… small enough, and I did some login review for JavaScript.
So I can probably do something here.
As well, so I would say, yeah, context.
Would be the important one.
**Jason Plumb** 15:10 Okay.
**Hanson Ho** 15:11 Context is needed for both logging and tracing, right? 'Cause you could set the context on both an event and, well, obviously for a span, so.
Context seems like… The one.
**Jason Plumb** 15:28 Yep.
**Jamie Lynch** 15:28 Cool.
Okay, I think that is enough.
For us to go away and… Yeah.
create something.
Cool. Handsome semantic mentioned artifacts.
**Hanson Ho** 15:46 Yeah, so I spent a bit of time last week spinning up a repo for federated semantic conventions.
And, So, basically, what we have right now in Kotlin is, we build artifacts for consumption in Kotlin for the core hotel semantic conventions. And we basically release versions of hotel Kotlin that will expose some version of the core semantic conventions. So when you say you depend on Kotlin 0.5, that implies a specific semantic convention version.
This is fine if… if all we want to do is kind of expose it in Kotlin. But, Jamie commented, hey, we should… have, the other platforms that we support, JavaScript and iOS, or Swift, also have access to this.
because otherwise we would need another repo to actually expose the Ios version of the extended semantic conventions. Basically.
we've created this additional dimension, versus, you know, whereas it used to be, like, one registry and, one, generated set of artifacts per language.
Now, there potentially are n different registries, depending on how many semantic conventions are federated. Now, do we… ship it all from the Kotlin repo, where we build the KMP platforms? Or is there another way of structuring this so that, okay, the iOS, the Swift hotel semantic convention builder will also build or generate constants for all the semantic convention federated ones? Or do we do it? What Gen. AI does, which is basically have their own registry. And I think sets of artifacts that it generates. So it just becomes this, you know.
issue, like, how do we… how do we structure this going forward? The… the version thing is probably something that's a bit orthogonal we could discuss after, but… How do we want… the continuing relationship between the Kotlin repo and the artifacts generated in Kotlin for semantic convention repos. How do we want that relationship to continue?
**Jamie Lynch** 18:36 Yeah, I think… My take on this is that Probably would make sense for the Kotlin repo to consume the YAML file that defines the semantic conventions.
And then just generate that as a.
Like, as an artifact in its own module, so… I think this is talking about, like, client semantic conventions, right?
So… I think it would make sense to put it in, like, a client semantic mentions Kotlin module.
And then, if you are interested… You can depend on that module.
and I don't see a need to restrict it by the target.
Because I guess… I guess technically you could be using Kotlin multiplatform on Swift in the backend. You're probably not going to be, but… I know that there is Swift backend code out there.
But yeah, that's my thoughts.
Anyone else?
**Jason Plumb** 19:47 It's kind of weird to have the semantic conventions in this repo at all. Like, I'm just drawing parallels to the other repos, or the other languages.
At least in Java, they have always had this, like, second repo where they publish the semantic conventions from, but it's also… a bit of an orphan, like, it doesn't get a lot of attention, it's just, like, minimally maintained. I think there might even be… There might even be some, Oh, whatever. It's there. The conventions are published. People can consume them.
I was looking at the… the… usage of the semantic conventions in the rest of the repository. And it looks like it's mostly through resource attributes.
And I'm not sure what else we would even use semantic conventions for.
It's mostly like service name kind of stuff, right?
**Hanson Ho** 20:49 Well, the SDK…
**Jason Plumb** 20:51 Go ahead.
**Hanson Ho** 20:52 If this repo doesn't contain instrumentation, it really shouldn't be using all the other ones, right? Because the other ones are about, like, emitting instrumentation or emitting telemetry-shaped.
**Jason Plumb** 21:04 Totally.
**Hanson Ho** 21:04 specific implementation. I think initially we put everything in this repo because it's convenient. So, you know, when you want to use, you write, you want to use a Java, sorry, Kotlin API.
you don't have to, you know, include another semantic convention repo and have, like, a different version of that. As you said, generating things in another repo that doesn't really have a ton of attention on it, other than, like, hey, the upstream has uploaded, or has a new version, we need to rev it. It seems overkill to have, like, a separate repo just to handle that. So… ideally, putting something like that in this repo, would be… Good. It's whether or not we build based on the semantic conventions for the end-user client federated one, which includes the base ones. So the change I threw up there basically generates everything. It becomes a superset. So if you want to use Kotlin.
you want semantic conventions in Kotlin, you include that.
But that is implicitly tied to the federated repo. So if someone wants to do, hey, I don't care about the end user client stuff. I just want a Kotlin with the core. That wouldn't exist if we just migrated, you know.
And that could just be fine because technically you don't need to use the repo or you don't need to use the client stuff in order to use the back, the core stuff.
But it just becomes one of those, well, do we generate artifacts for both, just for one? And, you know, how do you want to handle version? So I think the easiest thing would just switch it to… The federated one, when it, when it's out, and, it'll just be, like that. And we may want to change the version so it's not, like.
completely tied to, the API, or the, the repo version. But that's, that's almost like a, for a second discussion.
Do we want one or two?
And do we want to keep it in this repo?
I think doing the simplest thing is the easiest thing right now, and if anybody wants, like, an independent Kotlin scientific invention.
repo that simply takes whatever that is core upstream and generates artifacts.
they could either add it as an additional thing that we generate with a different versioning, or they could create a new repo and, you know, maintain that. But… I don't think we need the structure to do everything at this point.
**Jason Plumb** 23:47 Hanson, I think I still have Monday morning brain, and I'm just not following, like, I think I'm not completely following what you were saying, but I think I might.
Start to be so.
the… the current published conventions, so we have a bunch… we have… we're consuming the… OpenTelemetry semantic conventions in the Kotlin repo right now, and we generate these attribute classes in Kotlin, we generate these event classes in Kotlin, and then during the build, when we publish, those get compiled down to the different platforms, and if you look on Maven, like, we have… We have semantic conventions published for Android, iOS, different architectures for iOS, JS, and JVM. Are you suggesting that we need something else with Kotlin? I'm not sure what… I think I'm not following what you're saying. So we published those all today. They can be consumed. We're currently consuming it in Android.
using this Android publication. It also, I think, affords us, at least in Android, to be able to be using semantic conventions constants that don't have JVM ties, right? Like, we're not encumbered by JVM because of the KMP stuff.
So, what am I missing? Sorry.
**Hanson Ho** 25:05 So I wasn't aware that we're already generating like Swift constants from this repo. I thought we were only generating the Kotlin ones. So if we're generating like JavaScript constant files and Swift constant files.
**Jason Plumb** 25:25 Not.
**Hanson Ho** 25:26 We're not, okay.
**Jason Plumb** 25:27 No.
**Hanson Ho** 25:28 Okay.
**Jason Plumb** 25:31 So a Kotlin user, like any random Kotlin user who's like building a thing could consume any of these and target any of the platforms, right? So they could be using any of the existing semantic conventions and targeting iOS and Swift would not be involved, right? Swift being the language.
**Jamie Lynch** 25:48 Hmmm.
**Hanson Ho** 25:49 Unless we want to use it like, or they want to use it in their Swift specific code in Kubernetes.
**Jason Plumb** 25:57 I don't think that's… yeah, I don't think that's a supported use case. Like, I don't know why we would want to even support that.
**Hanson Ho** 26:04 Okay.
**Jamie Lynch** 26:05 Yeah, great.
**Hanson Ho** 26:07 Okay, so then the question would be then.
Do we then… Take the registry from the federated repo, And just generate artifacts for that.
Which is a superset of the core.
So we basically say the Savantic Convention artifacts generated by Kotlin is going to derive from the client stuff.
**Jason Plumb** 26:35 No, I don't… I don't think so I think we keep those separate. I don't think there's any reason for the Kotlin project to know anything about client conventions.
**Hanson Ho** 26:45 Okay, so… Got it. So then this may be an issue with just the general semantic conventions. How do client semantic conventions get generated artifacts?
So then…
**Jason Plumb** 27:01 Yes, and that's a different problem, but yes.
And then the way that a client would implement this, I think, a client like Android or OpenTelemetry iOS instrumentation, the way that those would consume the two different artifacts coming from different repositories, client-specific stuff and perhaps the well, they'd have to be writing Kotlin to consume the Kotlin stuff. Let's say the Swift stuff. The way that they consume both of those is by consuming both of those, right? They're separate artifacts. And if you're doing client stuff.
then you can depend on the core Swift conventions that are published, presumably. I don't know if they are, because I don't care about Swift, but I assume that Swift is publishing semantic conventions. OpenTelemetry Swift.
It's publishing semantic conventions. So if you were building a Swift app, you could consume those, and if you need the client-specific Swift conventions, you could also consume those, but those need to be published from this new repo that doesn't exist.
Right.
**Hanson Ho** 28:06 Yes. Okay. So, so… Okay, so the artifacts generated can actually be a superset, is the thing. So, We're not saying… Like, I guess… Maybe, maybe that's, okay, maybe we have to figure this out from, from the, from the, from the semantic conventions side. Do we want to generate only for, Iowa, for, for the ones that are defined in that registry? Or do we want to generate everything? Because right now you can generate everything. Like, I don't know.
**Jason Plumb** 28:42 I think you only generate the ones that are available locally, like the small set, not the superset.
**Hanson Ho** 28:49 Oh,
**Jamie Lynch** 28:51 It definitely feels preferable to me to be able to generate just the client semantic conventions, as then that allows you to Yeah, basically just separate it off into an optional module rather than the whole superset.
**Hanson Ho** 29:09 Got it. So what we're saying is that this repo will generate the core. So it'll function as basically the Kotlin analog for OpenTelemetry Java, or sorry, semantic conventions Java.
Which is basically just looking at the core ones. And anything federated, well, they were gonna have to… Generate.
artifacts for each platform in a different way, either as a separate repo or within the repo or whatever it is.
**Jamie Lynch** 29:40 Not necessarily in my eyes, I think.
If we're generating semantic conventions in this repository, I don't see Why we can't do client ones too, it should just live.
In a separate module, if we did that. Or, equally, we could put that into another… Repository, if we want to separate a bit.
The semantic mentions out from The actual SDK, but I'd lean towards not doing that just due to the maintenance overhead right now.
**Jason Plumb** 30:16 Yeah, I think I agree. If and when this new repository exists, I mean, presumably.
There's conventions for each of the platforms, and there's the common client conventions.
And what they publish, though, needs to be able to be consumed by all of the different client ecosystems, including Java, and including KMP, like, Kotlin, people targeting KMP.
And so that's what makes that separate repository a little bit more challenging is because it's going to have a bunch of different targets, I think, that it has to publish.
But, like, Android, you know, Android doesn't need to… like, the conventions that are specific to Android don't ever need to publish into iOS, so that's nice. But the common stuff would need to Anyway, we're getting a little.
**Hanson Ho** 31:03 Yeah, that's fair. I think that answers the question, which is like, you know, this repo will keep using the old one, the core one. Anything new coming from any other federated repo.
We can consider that separately from the core one. The core stuff will not change.
**Jason Plumb** 31:28 Great.
**Jamie Lynch** 31:29 Mmhm.
**Hanson Ho** 31:30 Okay, that makes sense.
**Jason Plumb** 31:31 That's my expectation, yeah.
**Jamie Lynch** 31:35 Cool.
Anything else on that one?
OK. Ben, minimum Kotlin version supported for Cayley platforms.
**Francisco Prieto** 31:48 Yes, pretty much a warning and a decision.
The same Kotlin version we use to compile is going to be the version we request for projects that use iOS and JS platforms.
Do we want to stop pumping the Kotlin compile version? Should we just continue bumping it and Just tell any user of that platform that.
They should bomb, too.
I don't think just no. I don't know. What do you guys think?
We can't do the same thing as we do for JVM, where we… used the latest Kotlin version for compilation, but we expose a Lower version for users.
**Hanson Ho** 32:43 Oh.
**Jamie Lynch** 32:47 That would.
Sorry, go on.
**Hanson Ho** 32:49 Oh, you go, you go.
**Jamie Lynch** 32:52 Okay.
So, I think that was an issue for this.
On the issue tracker.
Do you have… Access to that.
**Francisco Prieto** 33:04 There is an issue in the, at least the one I saw was in the Kotlin repo. In the Kotlin repo, sorry, in Ktrack, I don't know, the Kotlin tracking service. In order to support those platforms, what they do is to create a Klib that it's… pretty much like this. I'm asking Kate.
And they can't use the same things we use with API version and language version, where we said, hey.
we are going to be using features from this Kotlin version, but we are going to be compiling with a Hi, you're Bur They are going. I'm not sure if they are actually going to work on it, because it's been like a year since the last comment in that issue. But this might be a nice topic to ask some of the guys from shed brains that offers to to help.
That's why I brought it here.
**Jamie Lynch** 34:06 Are you able to share the link to that issue?
**Francisco Prieto** 34:10 Yes.
**Jamie Lynch** 34:11 Excellent.
**Francisco Prieto** 34:11 It was on the… I already created a PR for this and it got merged. I added a test in our main… Oh.
Where is this? I have, I have a testing.
our minimum version tests with, the compiled versions, so we actually, every time we run the test, we verify that a project targeting the new… targeting iOS and Javascript also complies with our minimums.
Here is the PR.
**Jamie Lynch** 34:47 This one.
**Francisco Prieto** 34:48 Here is the U-track.
issue.
**Jamie Lynch** 34:54 Okay.
**Jason Plumb** 34:59 Not planned.
Yeah, this would be good to ask them. This would be good to ask.
**Jamie Lynch** 35:07 Mmhm And Jonas Jones.
Do you know if it's just like one version back for BBSU or is it if you.
**Francisco Prieto** 35:19 I tried the tests because the tests are also useful for that. I bumped the version we passed in the test to 2.3 while we were using 2.4 and the test failed. So I think you need to be in the same version.
**Hanson Ho** 35:38 This, this, this seems to be like the analog for having, in, in, in the non-KMP case, targeting a lower version of the standard Libin language, except in KMP.
at least Caleb's, it doesn't seem possible. It's basically saying, oh yeah, if your SDK compiles with 2.4, everybody who uses it has to understand 2.4.
**Francisco Prieto** 36:06 Also, there's a like a new.
flyer in that same issue that they were experimenting with. I tried that flyer, but it didn't work, so I'm not sure if it's still supported in 2.3 so.
Maybe the shed brain folks have more input on this.
**Jamie Lynch** 36:34 Hmm. Interesting.
**Hanson Ho** 36:36 Oh.
**Jamie Lynch** 36:39 Yeah, so I guess… We should probably open an issue to.
track this and make a decision on what to do around this.
Even if it's just documenting it to start off with.
**Jason Plumb** 36:53 Yeah, because right now we don't have a choice, right? It's like, we get whatever it produces, like, whatever And if we don't document that, definitely need to, because someone will be wondering.
**Francisco Prieto** 37:05 Yeah, I think the decision also is in the future. Should we bump Kotlin versions as they appear, knowing that it will affect the possibility of the library working on these platforms. I think probably yes, because we haven't received any complaints so far and it's not that hard to bump a copy inversion for a customer. But I'm. That's not the way we do it for JVM projects. So it's.
It is…
**Jason Plumb** 37:35 Slow.
**Francisco Prieto** 37:35 We should make.
**Jason Plumb** 37:36 And it's a breaking change, right? Like, once we declare stability, we can't just willy-nilly bump up Kotlin versions.
Because that's something that'll break ABI.
**Hanson Ho** 37:47 like, right now it's okay, because no one's using it, probably. But I can imagine, suddenly, we have a new minor version. Sorry, you have to update your Kotlin version in order for this to work. That's not really acceptable.
And having support for super old versions is probably like just an Android JVM kind of, you know, legacy issue.
But this is… it doesn't become a non-issue when we have KPM. It's just probably less… dramatic. We may not be able to bump to 2.4 until, like, most folks, quote-unquote, whatever most is, is using it. Right now, we thought we could do it willy-nilly, because we can just target the older platform, or the older version. But this makes it not the case, and… we might be a year behind, we might be 6 months behind, something like that, but I think it's prudent for it to be somewhat behind. But yeah, definitely tracking… creating an issue, tracking it, and officially having a policy would be… would be good.
**Francisco Prieto** 38:46 Also, if the decision is to not bump Kotlin versions. We should… I can update the test, because right now I'm using the current version, so if we bump it, the test will pass. So we can just set a minimum Kotlin version for… iOS and JavaScript for Klib platforms and just leave it like that. So we know when we bump stuff, if it breaks that minimum version.
If we decide that, hey, from now on, the minimum version we support for these platforms is 2.4, I can do that right now.
**Hanson Ho** 39:30 Have we done the 2.4 merge, or do we have to back that out because of CodeQL here as well?
**Jamie Lynch** 39:37 Yeah, we've bumped it to 2.4. I don't think we run CodeQL on this repo.
**Hanson Ho** 39:42 Okay, okay.
**Jamie Lynch** 39:44 Mmhm.
**Hanson Ho** 39:45 I'm okay with keeping 2.4 since we're not stable yet, but maybe 2.5, we have to be a bit more careful.
**Jamie Lynch** 39:55 Yeah. Okay.
**Francisco Prieto** 39:56 Good.
**Hanson Ho** 39:59 doing the head thing.
**Jason Plumb** 40:01 Yeah, it seems good. Seems correct that we need to be more careful.
I think in this stage of the project, I think.
We can afford to… Be a little bit more breaky than we would want to be later on.
like, the stable by default, I feel like we've got a bit of a… We've got some wiggle room on Stable by default right now in this level of project maturity, I think.
**Jamie Lynch** 40:34 Okay, cool. I will… Create an issue, and we can… Kind of look into that further and decide how we want to document that.
Okay, last issue, Hanson, JetBrainFix API slash repo review.
**Hanson Ho** 40:54 Yeah, I created an issue with the specific APIs that I feel are probably more important, you know, for the JetBrains folks to review. And also looking at the repo itself, whether it's… Because I know they did a whole KMP project. This is the new way of setting up the repo. So I kind of want to know we talked about this, you know, getting them to take a look at this, and specifically what we should do to migrate the repo to make it look, if not exactly like what's recommended, but, like, what are the important things, or reading things? So, I don't have, I forgot what his name is, contact information. I thought he was gonna… come, but I'll reach out. I'm sure it's in the notes somewhere, and say, hey, this is what we want. But if there are additional questions, we can add it to the issue, or we could create a separate issue to take a look at this, especially with the this, this, this Caleb's thing, for instance.
is it okay for KMP SDKs to just basically, update Kotlin? Or… Is there an expectation that they are a little bit slower in adopting new versions? Because we can't pin it to a version like we could.
For a regular column project.
**Jamie Lynch** 42:33 Oh, boy.
**Jason Plumb** 42:34 That would be great to have eyes on to get some input.
**Hanson Ho** 42:38 So I can create another issue, and reach out, if, if… There are.
or if there are additional questions, I could create an issue including that, as well as other ones that we have, if we have any. And if you do, you know, let me know. We'll put it in here.
**Jamie Lynch** 42:57 Yeah, I'm sure I probably have lots of questions.
**Hanson Ho** 43:00 Yeah, in fact, I'm sorry.
**Jamie Lynch** 43:03 Prioritize.
**Hanson Ho** 43:05 Might make sense to talk to you because you probably have a lot more than me.
**Jamie Lynch** 43:15 Okay. So if folks do have questions, please have a look at that issue and just leave a comment.
**Hanson Ho** 43:23 That sounds good.
**Jamie Lynch** 43:27 Cool. Any other topics?
**Jason Plumb** 43:34 No, Jamie, just nice to have you back, and if there's anything that I can even try and help with getting you back up to speed, let me know if there's any questions from things that were done while you were out.
Feel free to reach out direct or whatever in the channel.
**Jamie Lynch** 43:51 Thanks.
I feel like I'm reasonably up to speed.
**Jason Plumb** 43:57 Cool.
**Jamie Lynch** 43:58 Yep.
**Jason Plumb** 43:59 That's.
**Hanson Ho** 43:59 The good and bad thing, the good and bad thing about momentum slowing down is that the delta is not as great as, as, One might hope, or not hope, but you know.
Feature Annabuck. So.
**Jamie Lynch** 44:12 Oh, I don't know how I said this at the beginning, but you should have seen my GitHub notifications when I came back. I think a lot more has happened than you'd realize.
**Jason Plumb** 44:20 Over 1500?
**Jamie Lynch** 44:22 Not quite that bad, but quite a few.
**Jason Plumb** 44:25 I was writing over 1500 for a while.
**Hanson Ho** 44:28 Excuse me.
**Jason Plumb** 44:30 That's right.
And so we just declared debt. You're like, none of that matters. If it matters, it'll show back up again. Yeah.
**Hanson Ho** 44:37 Bankruptcy. Yep.
**Jason Plumb** 44:39 Yep.
**Jamie Lynch** 44:42 Awesome. Well, everyone can get three minutes of their time back.
**Jason Plumb** 44:47 Cool.
**Hanson Ho** 44:47 Right.
**Jamie Lynch** 44:47 Cool. Thanks everyone.
**Jason Plumb** 44:49 Bye.
**carlosalberto** 44:50 See you.
