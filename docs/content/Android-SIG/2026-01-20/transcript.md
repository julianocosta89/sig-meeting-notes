SIG: Android SIG
Date: 2026-01-20
Duration: 55 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:23 Hey, Jamie.
I am outdoors.
**Jamie Lynch** 00:35 Oh, yeah.
**Jason Plumb** 00:37 And it's cold.
**Jamie Lynch** 00:38 It looks cold. Yeah.
**Jason Plumb** 00:40 I'm gonna try and make it an hour, I think I'll be alright, but, Oh, how do I… I should probably just unblur my background, let's see. There we go.
That's the Pacific Ocean.
**Jamie Lynch** 00:53 Oh, well.
**Jason Plumb** 00:54 Yeah, I got a… we are at this little camping spot. It's pretty fun.
But I didn't make it back home in time, so we're gonna drive home after this meeting.
**Jamie Lynch** 01:03 Oh, nice. Is that nearby?
**Jason Plumb** 01:06 It's about a 2-hour drive, so… I don't know how far that is in distance, but… .
**Jamie Lynch** 01:12 Go.
**Jason Plumb** 01:12 Yeah, it's not bad, it's, like, 2 hours.
Paces aren't.
**Cesar Munoz** 01:16 Hello!
**Jason Plumb** 01:20 I train the.
**Cesar Munoz** 01:20 Nice, nice background.
**Jason Plumb** 01:22 Yeah, so you can get a nice view of the Pacific, okay. And I also didn't bring my correct glasses, so I'm having a hard time seeing the computer, but we'll make it work.
Hey, Francisco.
**Cesar Munoz** 01:33 Goddess.
**Francisco Prieto** 01:35 Hey, everyone.
**Cesar Munoz** 01:38 Hello?
**Jason Plumb** 01:39 Well, the agenda's light if you want to put anything on the agenda.
share my screen. I'm also less efficient with this trackpad, because I never use it.
**Cesar Munoz** 01:58 Actually, Jason, if you want to, I can share today.
It's easier.
**Jason Plumb** 02:05 Yeah, would you like to drive? That would… that would be cool.
**Cesar Munoz** 02:09 Yeah.
**Jason Plumb** 02:11 Sweet.
That's great.
**Cesar Munoz** 02:14 I'm not as good as you are, but, you know…
**Jason Plumb** 02:17 Practice makes better.
**Cesar Munoz** 02:19 Same. Yeah.
Let's see, share… Yeah, this is the one.
Okay.
**Jason Plumb** 02:34 Race.
Jamie, did I miss the, Kotlin meeting yesterday?
**Jamie Lynch** 02:55 Yeah, it was all pretty last minute, though, like, with the invite going out, so no worries about that.
**Jason Plumb** 03:02 Sorry about that.
**Jamie Lynch** 03:04 No, it's absolutely fine. I think we'll probably try that time again as a regular thing, assuming that's okay with you.
But yeah, it was just kind of housekeeping stuff and how to set up a sig and everything.
**Jason Plumb** 03:18 Okay, so that would be Monday at 9. I think that can work. Okay.
Cool.
**Cesar Munoz** 03:27 Okay.
It's probably a good time to start.
So, we've got a few items. Where's this highlighted? Okay.
A few items on the agenda.
So, Andre Grailer Plugin 9.
was recently… Released in the stable.
Channel.
Who, who added this, sorry?
**Francisco Prieto** 03:56 I added it. I added the first two items.
I took a shot at upgrading OpenDimage Android, so it's… so it works with HTTP9.
I have a PR, I haven't upload… loaded it yet, because before uploading it, I was thinking, hey, how does this affect the main requirements that the OpenTelemetry Android repo has?
And I didn't find any place to actually test that.
So I went and created an app, and then I found out that the mine requirements, at least in that app, weren't working, so… First, I wanted to know if anyone has tried that. What do you think about the mean requirements? Then I will… later this day, I will… upload the PR with HCP9, and an issue with, open… with, my desktop, and why it doesn't, comply with the minimum requirement versions that they… they are in a file called versioning.md.
**Cesar Munoz** 05:06 Got it, so the… Okay, so I understand correctly, you're… the… you were doing a test locally, and your app didn't compile because of the existing requirements that we have in.
**Francisco Prieto** 05:23 I created an app with Kotlin 1.8 and HCP 7.4, Gradle 7.5, I think that's the whole requirement.
And it's, like, there's no way for… for me to make it work. I think the main blocker is that HCP 7.4. It doesn't… sorry, my gut wants to… I think the main issue is that, HCP bundles, R8, like, as part of what is compiling, and… HCP 7.4 doesn't really understand the bytecode that's outputted by the OpenTelemetry Kotlin repo.
I'm not sure which dependency we have on the Open Directimetry Android is causing everything to go up, because we are trying to expose Kotlin 1.8 and compile with Kotlin 2.2.
So, there are many ways to address this. We do have a way in embrace, like… I'm not sure, like, what you guys think about these mean requirements, if this is what we should go for, if we should discuss bumping them.
**Cesar Munoz** 06:45 if… if I understand correctly, I think… Well, I haven't checked the details, but probably the… The thing that's… breaking stuff the most right now, it's Kotlin, the latest Kotlin versions, which I think Jamie already addressed In a PR, if I remember correctly.
But we haven't… I think we haven't merged it.
**Jamie Lynch** 07:10 Yeah, I think… Hmm.
Yeah, I think… Kotlin 2.3 only supports targeting Kotlin 2.0 compatibility.
**Jason Plumb** 07:24 Which makes that a breaking change.
Yeah, which is why I didn't merge it. I think it's a good change, but… We collectively have to decide what we want to do with this.
**Jamie Lynch** 07:34 But I don't know if that would address, like, de-sugaring issues. There is one de-sugaring instruction in the repo.
So, I guess it would be good just to double-check that that works. Otherwise, we can, like, have, like, a VOM message and find out what's failing and example that…
**Cesar Munoz** 07:57 Got it.
If it works, this reminded me, a while ago.
there was an issue with OKHTP.
Because I didn't have support for Kotlin bytecode.
Like, all their Kotlin by code.
And I even created an issue in that repo.
Asking for at least to… for them to add… you know, that there's a way that you can add the API compatibility or something like that in the Kotlin compiler options.
And I think they didn't… they didn't do it.
And their, their, response was something, around the lines of.
you know, if some people want to use an older version of Kotlin, then they should use an older version of OKCDP as well.
So… so… Probably we can do a similar thing, I wouldn't be opposed to that approach.
If we go down that route, probably… What I'm not sure about is what to do with security fixes.
But, but definitely, I don't think we can hold Users from, you know, getting the latest stable versions.
We should try to, you know, keep stuff working with the latest versions, always, because I know a lot of users like to, you know, stay on… on the edge, so… Yeah, that's my opinion. I'm not sure about the security updates.
That's the only thing.
**Jason Plumb** 09:38 Yeah, so I think the way it's handled elsewhere is, if there's a necessary security fix that needs to go in, you do a patch release. So if we decide that, like, 0.8.0 is the latest version that supported whatever, and a version that needs that supported version of whatever also needs a security fix, then we make 0.8.1.
And we just keep a release branch off of that minor version, but, you know, that's not sustainable long-term.
And what I feel like we're trending toward, like, This… this, compatibility… problem is, like, it seems like it's way more complicated and frequent in Android than it is in other projects like Java.
And I think… I'm gonna throw out one idea. It seems like, like, we're trending the way that other projects who have faced the same problem have also trended, and that is, we're gonna have a compatibility matrix somewhere. We're just gonna have to say.
This version supports this version and this version. And if you want to use Android, if you want to use this version of AGP and this version of Kotlin, you know, here's your compatible versions of Android. OpenTelemetry Android.
And keeping that, you know, maintained is a little bit of a pain. We do have some flexibility in how quickly we can roll stuff off, and we can say that we only support Certain older versions for 6 months or something, but… I don't know, other ideas on how we handle this? Because it seems to be changing frequently, and breaking frequently.
**Jamie Lynch** 11:08 Yeah, I think a support table, or compatibility matrix.
Feels like quite a good idea.
Yeah, it's tricky, because we need to support the newest stuff.
But we also want to go as far back as possible as… like, it's an SDK, so it still needs to be fairly conservative.
I would lean more towards supporting newer stuff, and if people are on a really old version, we can tell them to use Like, an older release.
**Cesar Munoz** 11:49 Sounds good.
I would like to add, in my experience, I think it's difficult… I think Google makes it difficult for users to stay on old versions.
**Jamie Lynch** 11:59 Like, I know…
**Cesar Munoz** 12:01 like, for regular Java projects.
I think some people are still using Java 7, for example.
But… in, in, in Android projects.
there's… there's always a way for Google to force you to upgrade, so it's like… If you, you know, download the latest Android Studio version, then it will complain that your project's old, you know, something like that, so you will have to update stuff.
But if you upgrade the undergrad plugin, then it will complain that you are using an older Kotlin version, or something like that. But actually, right now, with the, One of the things I noticed with the new Android plugin version 9, is that it complains if you manually add Kotlin.
to your project. So it's like… You no longer have to add coupling manually. Any… any… And it's not a warning, it's, like, it halts the compilation because of that. And until you either disable that warning, or error, or… you know, just remove the line where you're adding coffee. So…
**Jason Plumb** 13:12 So they want to manage what Kotlin version you're using?
**Cesar Munoz** 13:15 It seems like, yeah.
**Jason Plumb** 13:17 I mean, that's kind of cool, I guess.
**Cesar Munoz** 13:21 Probably that will remove the… this issue for… for ourselves in future versions, right? Because it's like…
**Francisco Prieto** 13:30 That's a big part of the HCP9 migration. Now it comes built in… the Kotlin version comes built in with HCP, so you don't really need to apply the KCP plugin anymore.
**Jason Plumb** 13:43 Interesting.
I miss that.
**Francisco Prieto** 13:51 Oops.
**Cesar Munoz** 13:51 Like, is that another approach?
**Francisco Prieto** 13:53 I just got lunch, so I had to go fetch it. So…
**Cesar Munoz** 13:59 It's okay.
**Francisco Prieto** 14:00 I am going to create the issue and explain a bit better, like, which errors did I get, but mainly for it to work, I think… like, I especially wanted to know what were your views on, like, which versions we wanted to support.
if Shami already added, PR, bump into Kotlin 2.0, and you think that's okay, I think that's going to make things easier.
Because we really have Embrace as a reference, that we are supporting, Kotlin 2.0, and we are building with the latest Kotlin, and this same example I created, works correctly with Embrace.
So… And maybe for the next SIC, or as a next step, it would be nice to add some kind of validation in CI, or maybe periodically, so we know that our minimum required versions are… Are actually being, that you can build with them.
**Cesar Munoz** 15:05 Yeah, yeah, I think the general idea is that we want to keep Supporting the latest versions.
It's just that we're not sure what to do when, you know, somebody wants to use older ones. But again, I'm not sure how often we'll… find that kind of issues, so… Another approach I was gonna propose is to just leave it as is, and just, you know, update everything, and keep supporting on the latest stuff.
And broadly only work on the matrix.
When somebody complains about it, if that happens?
It's kind of a lazy approach, I know, but, you know.
**Jason Plumb** 15:50 Yeah, so it looks like AGP93 brings Kotlin 2.
According to a compatibility matrix.
on the Gradle site.
Just to say it out loud so that we are all on the same page.
**Cesar Munoz** 16:06 Got it. You have the link?
**Jason Plumb** 16:08 Yeah, just pasted it in the doc.
**Cesar Munoz** 16:14 Within of… okay.
Thank you.
**Jason Plumb** 16:20 Yeah, it's hard to run the meeting and take notes at the same time, isn't it?
Yes, definitely. I actually haven't taken any.
I've been taking some.
**Cesar Munoz** 16:29 Oh, thank you.
**Jamie Lynch** 16:31 I think one distinction, I'm not 100% sure, and this fan might know a bit more, but I think this relates to the Kotlin version that is used at build time within the Gradle plugin, and if you're accessing like, the… DSL using colon Gradle script.
I believe it's separate, like, the actual runtime dependency.
**Jason Plumb** 16:59 So you're saying this is a compile time… language version.
And not the run… Yeah, it's for one verb to be…
**Jamie Lynch** 17:08 plugin and Gradle use.
Rather than, so… Rather than calling code that gets compiled into your APK.
**Francisco Prieto** 17:20 Yes, it uses this version to… just for the Gradle tasks, like, for Gradle stuff, not really for the app.
It comes embedded with Cradle.
**Jason Plumb** 17:34 Okay.
So I'm confused, though. I'm confused, then. If AGP is now bringing its own version of Kotlin, that's only for itself, it's not for the… What it's compiling?
**Francisco Prieto** 17:52 No, I think the one it brings… the one HCP brings, like the HCP9, now also runs for the project.
Like, I think you can still select which Kotlin version you're using, but that's also through HTTP, extension functions. You see, in the place, I think it was compiler options or something like that, you choose the language level that bytecode that you're going to target, I think you can select which Kotlin version your project is going to use through HCP. But also, this is all quite new, so I don't really know how it works, like, under the hood, or what it really means for projects and for libraries. So, yeah.
**Cesar Munoz** 18:40 But I'm confused, because if it's only used at compile time, then why will… You know, it will… why will it… show this error saying that you shouldn't add on Kotlin manually.
**Francisco Prieto** 18:52 Is… .
**Jamie Lynch** 18:56 As part of… as the migration.
**Francisco Prieto** 19:00 I think the main issue is that It tries to… Added to the same class path, the same classes that applying the plugin manually does, and that causes conflicts. So, if you… there is a migration guide, that migration guide tells you, hey, you're going to find this message, and the message is something like, you already added Kotlin… this Kotlin grader plugin to the class path, and it's kind of, like, conflicting.
That's why you need to remove, like, every place where you apply that plugin.
**Cesar Munoz** 19:38 Got it.
Also, just to keep… keep in mind that well, at least last time I checked, just by adding the Kotlin plugin to a project.
it will automatically add a runtime library, which is the, standard Kotrin library, so… Like, it adds both the compilation tools and also a runtime library.
So… I'm not sure if it's gonna cause issues for users at… by code level, unless the standard library uses some new… Fancy bytecode.
Maybe.
**Jason Plumb** 20:28 Okay, Francisco, have you opened a bug for this yet? Or an issue for this yet?
I think it's worth having, that way we track that, like, what we're documenting in versioning does not match reality. You can't actually compile with those min-versions anymore, and so we can at least use that as a reference going forward as, like, stuff's broken, we need to make it better.
We should probably have an issue as well to figure out… Some kind of, like, compatibility matrix or table.
And get started on that, so that we… that way we can upgrade.
at least documenting the last known versions where stuff worked, like… Android 1.0 is compatible with this version of Kotlin, this version of AGP, like, this is our recommended… And if you want to go older, then you probably have to go older in the Android version as well, the OpenTelemetry version as well.
**Francisco Prieto** 21:19 Yes, I will, and we can also discuss, like, next steps in that issue, so we know, like.
**Jason Plumb** 21:26 Okay.
Thank you for doing that.
**Cesar Munoz** 21:29 Thank you.
Okay, so the next one is the minimum required versions. It's… this is the same as, it's kind of related, right, to the… okay.
**Francisco Prieto** 21:40 Yeah, so…
**Cesar Munoz** 21:41 Got it. Thanks. So let's move on to the… Last one, skate, hatch.
Following folks to configure OpenTelemetry via the initializer.
**Jason Plumb** 21:53 Who wrote this one?
**Jamie Lynch** 21:55 I wrote this one.
**Jason Plumb** 21:56 Okay.
**Jamie Lynch** 21:56 So, this is… kind of just giving us time to discuss what Hanson mentioned last week. I think he was suggesting some way of exposing like, the OpenTelemetry Java, like, API for creating via… The OpenTelemetry, like, SDK object.
And whether it was worth… exposing that.
as an escape hatch for various, like, things. Like, I think folks have wanted to add, like… Custom, like, processors and deal with, like.
I think there have been, like, several issues, where the option is either to create a custom API within OpenTelemetry Android, or just… rely on the Java APIs.
**Jason Plumb** 22:58 Yeah, I thought this… I thought this or a very similar topic came up in one of the PRs or issues.
And… there was a question on whether or not we should expose this… this API from the SDK.
as one of our… as an API class that's exposed through our API, To which I said, I think it's… I forget which one it was, because I'm not quite awake yet, but I think… It was something that had not changed in, like, the better part of 3 years.
And so, to me, it seemed like a safe thing to expose. I think it was already marked as stable and upstream. And even if it wasn't, like, it really hasn't changed.
But it might… it might have been an education. If I can remember which class that was, it would be more helpful, but, like, so the way that we build… the OpenTelemetry instance is with the OpenTelemetry SDK Builder.
**Jamie Lynch** 23:51 Hmm.
**Jason Plumb** 23:52 So, potentially, we could expose that build… that SDK builder. Yeah.
As an API. Is that kind of what this is leading toward?
**Jamie Lynch** 24:01 Yeah, that'd kind of be the gist of it. And I can see, like, there's potential downsides in that, in that.
It's not strictly from an API package.
But it does… allow… End users to do things… But don't seem to be possible with the APIs today, and… We might have not… But it feels like we don't want to write dedicated APIs for every single one of those use cases.
**Cesar Munoz** 24:34 I think this, could be done in different ways, meaning, like, it could be done I think if I understood correctly, what Jason mentioned was to essentially Expose the… the whole… API, which is the builder that receives everything.
Another approach, I think, would be what we do in Core, which is to expose Parts of the stuff that we add to the builder, so that, you know, the tracer provider and stuff like that.
My concern with… I mean… I'm not opposed to adding it, but my concern will be… Users who… Like, how are we gonna merge the stuff that the initializer already sets, you know, with whatever users…
**Jason Plumb** 25:33 Yeah, we'd have to pick an order, and maybe… maybe do the sort of more basic one, either first or last, and I haven't thought it through yet, but probably… first, because it's the biggest hammer, and then the other stuff is smaller, but I haven't thought it through.
But yeah, certainly somebody doing both would then be possible, and it also feels like a mistake. Like, someone shouldn't be… specifying initializer configurations that they've then overridden by hitting the builder directly. That seems like a mistake.
**Jamie Lynch** 26:04 Hmm.
**Jason Plumb** 26:06 But we can't… we can't prevent someone from doing that.
If we, if we expose it.
**Cesar Munoz** 26:12 There's also one… yeah, I agree. That could be one way to… We'll have to decide the order, and… probably we can… probably we should create an issue to discuss more… more details. But the… the… other thing that I… that comes to my mind right now is that I remember at some point, somebody wanted to add a… Kind of, they wanted to chain exporters.
For example, they wanted to change Span exporters.
So that, you know, they will add some… Like, enriched data or something right after.
Our exporter, you know, handed it over.
Something like that, which is something that… Well, you can also do it with processors, and I think it's easier.
But, the thing is that the way they… Java SDK currently works is that you… at least for adding, you know, new exporters, you cannot, as far as I'm aware.
like, append them into a single processor, because the exporter is tied to the processor, so if we add a processor.
on our side, They cannot change it.
Just by getting the whole… Opentelemetry SDK Builder object.
**Jamie Lynch** 27:34 Yeah.
**Cesar Munoz** 27:35 So… I guess in that case…
**Jason Plumb** 27:38 Yeah, sorry, are we talking processors, or are we talking exporters?
Congrats.
**Cesar Munoz** 27:43 See what we're talking.
**Jason Plumb** 27:44 Exporters, exporters you can already customize.
You just have to use the OpenTelemetry Realm Builder, not the initializer.
**Cesar Munoz** 27:52 Yes.
That's true.
But, like, if we… if we decide to expose more Autel Java APIs in the initializer, that… At the same time, it's something we haven't discussed.
But now that you're touching it, at the same time, that will essentially, that will supersede the core.
API. Wouldn't it?
**Jason Plumb** 28:20 It would.
Yeah, do you…
**Cesar Munoz** 28:30 And I waited.
**Jason Plumb** 28:30 Do you remember… sorry to jump in, when Hanson brought this up, do you remember what specifically he was targeting, or what the need was? Because this might be something we can address on, like, kind of a per-as-needed basis.
They're trying to blanket it. My gut… my instinct is that we will also probably need a way to expose the kitchen sink. Right now, that is the… with the OpenTelemetry Run Builder, and we don't expose much of the core APIs.
But my instinct is that, you know, just to make everyone happy, we kind of have to at some point.
**Jamie Lynch** 29:06 I don't remember the exact issue, I think it was something to do with customizing, like, an exporter, or potentially adding in Like, I think there's one where someone wanted to change headers dynamically.
**Jason Plumb** 29:21 Oh, or was it the… was it the, authentication? Like, there was a bearer token?
**Jamie Lynch** 29:26 Yeah.
**Jason Plumb** 29:28 Yeah. Okay.
**Jamie Lynch** 29:29 The, I think maybe a good step forward would be to… just write this down as an issue, and, yeah, we can take Hansen on it, and he'll have his thoughts.
**Jason Plumb** 29:51 Yeah, it was 1482, I'll put a link to it in the notes, that's what it was.
Yeah, so I think in that specific case, I… this seems like a common enough request that we should probably do this.
Yeah, I mean, Jamie, you were saying the same thing, yeah, okay.
**Cesar Munoz** 30:22 Okay, sorry.
I don't know how to do it, Jason. I know that you tend to, like, take notes and also listen.
**Jason Plumb** 30:29 Listen.
**Cesar Munoz** 30:29 stuff to what people are saying.
**Jason Plumb** 30:32 I'm trying.
**Cesar Munoz** 30:32 that right now, so… I actually do a pretty good job, but I couldn't do it. The… Okay, so this is… this is one of the reasons why we would like to expose AutoJava APIs.
to provide… okay. And this is one of the things that I… I think it kind of makes… It kind of goes back to what I was mentioning, that So, let's say that we… right now, we provide an HTTP exporter.
We provided via the… process, or… That we are setting internally.
So… if we expose the Java SDK, just the Java SDK builder. I don't know how people will be able to… Kind of modify the headers.
of the exporter that we created, you know? Because I don't think that's possible based on the current Java SDK.
API.
**Jamie Lynch** 31:38 Yeah.
**Cesar Munoz** 31:39 In that case, this issue wouldn't get solved if we exposed the whole thing.
**Jason Plumb** 31:46 Yeah, I see where you're coming from. I'm also not convinced that that solves it for this case yet.
**Cesar Munoz** 31:54 But, like, we can enhance this API so that…
**Jason Plumb** 31:58 I think so.
**Cesar Munoz** 32:00 It allows for, I don't know, a function… parameter.
**Jason Plumb** 32:07 Yeah, whenever we're doing stuff like this, we have to make… we have to be careful that we make sure we, build it as a supplier and not anything static. People always want the supplier.
Because these bearer tokens change over time.
They expire.
Yeah, exposing that is still a big hammer, and I think our… our guidance right now is to keep that… like, not pull that hammer out of the toolbox unless we really have to, and let's… I think let's try and take it case by case.
And if we think it's something that more than a handful of users will want, then let's put it in the initializer. Like, let's build DSL for it.
**Jamie Lynch** 32:55 Yeah, I'm happy with that approach. I guess we can always revisit in a couple of months if, like, loads of other stuff crops up that could be solved by accessing that.
**Jason Plumb** 33:06 Yeah.
**Cesar Munoz** 33:20 Okay… Targeted, so we have a… a decision here. It's like, we'll just try to address case-by-case scenario in the meantime.
**Jason Plumb** 33:34 Yeah.
**Cesar Munoz** 33:37 maybe there could be a way, and this is tangential, but maybe there could be a way we can update this DSL to allow for a… I know I say supplier, and it's not the same exact thing in Kotlink, but, you know, supplier-like.
Functionality.
Without, you know, breaking this… in a way that it's still this, you know, static header setter, it's still… it still works, it's just that if you provide a function, then it… Goes… falls back to the other.
Setter, for a supplier.
**Jamie Lynch** 34:13 Yeah.
**Jason Plumb** 34:14 Yep.
**Jamie Lynch** 34:16 Yeah, I think the nice thing about Kotlin is, well, one nice thing about Kotlin… is the deprecation notice. You can basically provide a string to replace the old API with a new one, and then you kind of get the IDE.
Automatically suggesting, a replacement, so we could take that sort of approach.
**Cesar Munoz** 34:46 Sounds good.
Okay.
Is there anything else?
You would like to add to this topic?
**Jamie Lynch** 34:58 But it's covered in my perspective.
**Cesar Munoz** 35:01 Sorry?
**Jamie Lynch** 35:02 Oh, that's it from my perspective.
**Cesar Munoz** 35:06 Thanks.
Is there any other topic… what is it, usually, that you do here, Jason? Just take a look at the issues, right?
**Jason Plumb** 35:15 Yeah, if we have time and people are still interested, we can look at the issues. There was one about GRPC exporter…
**Cesar Munoz** 35:22 Yeah.
**Jason Plumb** 35:23 Which I'm like, I don't know why you're doing that to yourself on mobile, but, you know, if you… if you want that, I guess you could do it.
**Cesar Munoz** 35:32 Yeah, I think this is what we discussed last week, that we probably can add another… you know, function to the DSL for gRPC.
**Jason Plumb** 35:44 Yeah, there's also an issue from back in the early December about min SDK, so that ties back into our compatibility situation.
**Cesar Munoz** 36:07 So, right now, we're still… mentioned 21 as a mini stick.
**Jason Plumb** 36:13 I think so, let's double check that, but I think we do… I think when I looked earlier… It's in the versioningMD.
**Cesar Munoz** 36:24 Yeah.
You know, technically speaking, That's still true.
even though the upstream Java SDK says 23, Because of the de-sugaring.
However… I'm a bit hopeful… well, a bit not, I'm a lot hopeful about the, OpenTelemetry Kotlin SDK, because… In theory, it should, you know, make… this kind of, min SDK compatibility issues go away, because Kotlin should compile everything in a… JVM bytecode compatible You know, output.
So…
**Jason Plumb** 37:18 I'm not sure if I'm following that, I'm sorry, Cesar.
**Cesar Munoz** 37:21 So, no, that's fair enough. So… so my understanding is that the Kotrin compiler will create JVM bytecode that it's… compatible with, I don't know, Java 7.
So… it's fine.
like, the issues we have with Hotel Java is because it is using Java 8 APIs that are not available in this version of Android.
**Jason Plumb** 37:52 Got it.
**Cesar Munoz** 37:53 But my understanding is that Kotlin will create Java 7-compatible bycode.
So… if we swap the Java SDK by the Kotlin one, then we wouldn't have JVM issues. That's my understanding.
**Jason Plumb** 38:11 We're a ways away from that, though, right?
**Cesar Munoz** 38:17 But yes, I'm following you.
**Jason Plumb** 38:19 Yeah.
**Cesar Munoz** 38:20 Now, like, well, okay.
But I guess in the meantime, it makes sense that people might get confused, because they see 21 here, and then 23… upstream.
Is that what you're… yeah.
**Jason Plumb** 38:41 Yeah, I don't even think I was considering Upstream when I wrote this.
I forgot that… I always forget that they even publish… Kotlin compatibility requirements, like… Or Android compatibility requirements, rather.
**Cesar Munoz** 39:00 Yeah, last time I checked, yeah.
**Jason Plumb** 39:02 Android. Oh, they publish both, yeah.
So…
**Cesar Munoz** 39:11 Because technically speaking, if this reads 23, we should… We shall sync with that.
**Jason Plumb** 39:20 Yeah, we should just do this, right? We should just bump this up.
I'm willing to get… I'm willing to take that grief from the less than 1% of the users still using 21.
I think that's a reasonable.
**Cesar Munoz** 39:34 Good point, too. Yeah.
Probably we can go back in the future.
once we swap to the Kotrin SDK. But yeah, I guess for now.
At least it makes sense to keep in sync with what… auto-Java rates here.
So, okay, yeah, that sounds good for me.
**Jason Plumb** 39:55 Since our agenda's a little bit light, I was thinking about something Francisco was saying earlier about having CI that would… Build against our minimum requirements, and… that's fine if we have an app that is intentionally built using the minimum requirements and doing a compile using the OpenTelemetry Android, like, nightly or something, that's totally fine, I can see us doing that. If we end up expanding that to a matrix, though, of what versions support what versions, that gets a little bit… trickier. Does that suggest that we have multiple applications, then, that we need to compile against all these different versions, or do we have one app that has different templated configurations. Either way, it sounds complicated to manage.
CI compatibility for a matrix.
Or maybe we say we just always tar… maybe we just CI the latest one, and the other ones we said they used to work, they probably still work.
We haven't gone back and redone anything in the old versions of Android, so they should still be fine.
But… It just seems complicated.
**Cesar Munoz** 41:02 Hey, Joss.
I will go with the latter.
**Jason Plumb** 41:08 Yeah, just test the… the current.
Like, whatever we say in tip is the minimum version.
**Francisco Prieto** 41:15 Yeah, and you will end up with a matrix of sorts, because as long as you keep upgrading both at the same time, you can, like, look back and say, hey, this was the state of the app when it compiled for this version.
**Jason Plumb** 41:30 Yeah.
That's cool, so as part of our release process, then we could have a step in there that's like, go update the matrix, make sure that it's up to date, or eventually build automation that does that for us, but… okay, cool.
That seems less gloomy than I thought.
Apparently these birds have some opinions on this. I don't know if you can hear them, but they're loud.
**Francisco Prieto** 42:07 It looks amazing. Where is it?
**Jason Plumb** 42:09 This is at the, Oregon coast.
**Cesar Munoz** 42:13 It is pretty cool.
**Jason Plumb** 42:20 Yeah, it was nice to come out here, it's just, it's pretty cold right now.
**Cesar Munoz** 42:28 So we'll talk about this one, this one…
**Jason Plumb** 42:32 And the TLS one is kind of related to… Did we talk about that one?
Like, that's kind of the same as the other one.
**Jamie Lynch** 42:39 Hmm.
**Jason Plumb** 42:40 Someone wants to specify their TLS provider or whatever.
This is, like, about configuring exporters.
**Cesar Munoz** 42:59 Is that even, yeah, I think it is, isn't it? Like, configurable via the AutoJava SDK, or is it a…
**Jason Plumb** 43:06 It is.
**Cesar Munoz** 43:07 Sylvania.
**Jason Plumb** 43:07 Yeah, if you scroll up just a little bit, I'm like, there's a setClientTLS method there that I mentioned. If you scroll the other way, the other up… Apple reversed our brains on all this stuff, so what's up with.
**Cesar Munoz** 43:18 Oh, here it is.
**Jason Plumb** 43:19 Yeah.
Yeah, so they definitely have that method on there where you can specify that, but we don't expose it directly.
Fine.
**Cesar Munoz** 43:29 And this is a setter per exporter, right? So…
**Jason Plumb** 43:33 Yeah.
So I was like, you can do it today, but you have to use the OpenTelemetry Realm Builder, you can't use the initializer.
It seems to me that this falls in the same kind of category, where people are going to want to do this sort of thing.
Because they're gonna ship their app with client certs.
Like, that's a way that people are going to… secure their endpoints, secure, loosely, I'm using that, like… You know, they're gonna… they're gonna ship client certs in their app.
**Cesar Munoz** 44:02 In their app, yeah, that's not… that doesn't sound good.
Fair.
I mean, it… Well, this is… I think this is easy to expose. Well, maybe not the… like, we could have, like, a grabber that just receives the exact same stuff.
And, you know, Delegates it to this setter.
Yeah, that's the…
**Jason Plumb** 44:25 That's kind of where I concluded here. I was like, this seems like a good idea, I think we should build this. I marked it as enhancement, right? So that kind of sends a signal that this makes our stuff slightly better.
I didn't put Help Wanted on it, because… I think we know what happens nowadays when you put help on it on that.
You get a 4,000-line AI-generated PR, is what happens.
**Cesar Munoz** 44:48 Oh.
Got it.
**Jason Plumb** 44:51 this is open for anybody to work on, I mean, I feel like this is a good idea, we should have this in the initializer.
**Cesar Munoz** 45:02 Yeah, sounds good. So, we now have these two issues that, you know.
We're looking for help. Or, you know, of course, we can take them .
**Jason Plumb** 45:15 As soon as we get the time.
**Cesar Munoz** 45:17 TLS? Yeah, I'm not…
**Jason Plumb** 45:18 I'm not discouraging people from putting Help Wanted, like, please feel free to go ahead and put Help Wanted on there, I'm just being snarky. Like, the help is always welcome.
It's just different.
**Cesar Munoz** 45:29 I do remember, I do remember some… Kind of like AI-generated PRs.
**Jason Plumb** 45:34 There's, they're still alive.
**Cesar Munoz** 45:35 I didn't know it was because of that. I didn't know it was because of this, label.
**Jason Plumb** 45:41 I'm being a little snarky, says Aaron.
**Cesar Munoz** 45:43 Let's see this.
Gonna do the test.
Okay, sounds good.
Let's just go through.
Stop here.
**Jason Plumb** 46:03 I guess we should look at.
**Cesar Munoz** 46:04 Oh, backyards.
**Jason Plumb** 46:04 We should look at the PRs before we look at issues. Like, there might be something contentious that we've forgotten about. I feel like there was something last week that, after the call, I was like, oh, I've… we forgot to talk about something.
Do you remember this, Jamie? It was, like, from… I think it was from one of our issues.
Did I mention it in Slack?
**Jamie Lynch** 46:24 It was.
**Cesar Munoz** 46:26 Is that an issue or a PR?
**Jason Plumb** 46:28 It was 1462… And… that's already been merged. Okay, we're good. We talked about it. Okay, we figured it out.
**Cesar Munoz** 46:40 I mean, there's a lot of the… I was gonna say it depends about PRs and stuff, but, you know… I don't think we… have we defined, like, how should we go about it? Like, check VR first, then check the users, or it doesn't matter? Depends on…
**Jason Plumb** 47:03 I think it depends on the agenda and how full it is, but I… I mean, I think checking PRs first is pro- I mean, new issues, and then PRs, and then back to other issues, I guess, is kind of what I've been doing.
**Cesar Munoz** 47:15 Got it. Well, I don't think we have it written down or anything.
**Jason Plumb** 47:33 Yeah, where did this one leave off?
Yeah, they haven't responded, everything's broken, so they dropped it, and have they said anything after this?
Do they engage at all with this PR?
**Cesar Munoz** 47:49 We can add… What was it? Waiting for an author?
Yeah, it needs outdoors for the back.
There you go.
**Jason Plumb** 48:03 Did they engage on that one for a little while?
**Jamie Lynch** 48:07 They reached out to both me and Hanson before we raised it.
**Jason Plumb** 48:11 Really?
**Jamie Lynch** 48:12 So…
**Jason Plumb** 48:12 Okay.
**Jamie Lynch** 48:13 Yeah.
**Cesar Munoz** 48:16 Okay, after your comments, Jamie, they didn't… They haven't come back once, okay.
**Jamie Lynch** 48:23 Yeah, I think originally it came in as a really big PR, so we asked if it could be split up, and barely asked was the next round of comments, and we haven't heard anything since.
**Jason Plumb** 48:34 Okay.
Well, hopefully they see that notification that the label got added, and then they engage, and we can move it forward, because I think having some session stuff would be great.
**Jamie Lynch** 48:44 Hmm.
**Jason Plumb** 48:49 I think every time I've looked at that PR, I'm like, Jamie's already asked a bunch of questions, and they're not answering, I'm not going to look at this.
**Cesar Munoz** 48:59 This is related to this buff brain… I think they're waiting for… For you here.
**Jason Plumb** 49:11 Okay, sorry.
Yeah, what are the.
**Cesar Munoz** 49:13 No, it's fine, just to let you know.
Sounds like they're proposing some changes to the Java doc, the Kotlin doc.
**Jason Plumb** 49:26 Oh yeah, this relates, because they also put up PR and disk buffering in Contrib, right? In Java Contrib? It's the same person, I think.
**Cesar Munoz** 49:34 I think so, yeah.
**Jason Plumb** 49:35 Okay, have you reviewed this one yet, Cesar? Because I think it's pretty good. I think it's good to go, mostly.
**Cesar Munoz** 49:40 Yeah, I think I approved it. Yeah.
**Jason Plumb** 49:43 Okay, okay.
Okay, that's on me to respond to, thank you.
**Cesar Munoz** 49:47 Got it. Thank you.
**Jason Plumb** 49:49 We should get them merged.
**Cesar Munoz** 49:52 There's 10 minutes left. I wanted to, Unless there's something that you would like to check here.
I just remember I wanted to quickly mention this issue that I created.
Which is a very, loosely describe, because I didn't have an exact idea of… like, I remember that you… that you mentioned that when the first GA stable release was created, there was issues with the CI tools.
My understanding, or at least what I remember, is that the script wasn't aware of the patch version or RC version bump.
Is that… it was… was that the whole issue, or maybe… something? Okay.
**Jason Plumb** 50:40 No, that is the whole issue.
So, there's ways… there's code in place as part of the release pipeline that looks at the current version, and it compares it with the previous version. And it's able to get the current version from the Gradle properties file, and that's fine. And then the previous version is computed because it's expected to follow, like, normal SEMVR, and there's no, like… we're not using any sort of… complicated libraries to do that calculation. It's just, like, splitting the thing into its constituent components, which normally is just major, minor, patch.
And in our case, when I see, it, like, kind of doesn't… I don't even know what to call that little suffix or whatever.
**Cesar Munoz** 51:21 There's a little bit of code that we added to sort of account for that suffix, but it doesn't do the computation right, like, it doesn't know how to…
**Jason Plumb** 51:27 turn RC… 2 into RC1, and it doesn't know how to take RC1 and pull that off, right? Like, if you have 1.0.0-RC.1, what's the previous version?
**Cesar Munoz** 51:40 Yeah. I don't know. Got it. I can't even tell you…
**Jason Plumb** 51:43 version is looking at that, so… that's… it's… it's complicated, And maybe we don't deal with RCs, but I think we do need to figure out patches.
Because we are going to have to have patch versions. Like, something will come up, and it'll be broken, and we want to release a 1.0.1 or 1.0.2.
It's gonna happen.
**Cesar Munoz** 52:05 Sounds good, and I think it's great that we also touched on the RC stuff, because I was also wondering if it's something that we will want to do in the future. Like, I understand that it was needed based on… because of the major version bump, but I'm not sure if it's still needed.
Unless we're gonna, you know, release version 2.
**Jason Plumb** 52:26 I mean, we will in a year, right? That's the expectation, I think, is that we'll… we'll lead toward a 2.0 release early next year.
**Cesar Munoz** 52:35 Yeah, that's true. Okay, so I'll try to see if we can… make them both work. I just wanted to make sure I understood correctly. Okay, looks like that's the issue, so… Okay.
**Jason Plumb** 52:47 And then… Since we're talking about releasing, it looks like instrumentation did go out on Friday… 4 days ago? Was that Saturday?
Friday or Saturday.
**Cesar Munoz** 52:58 I know it's been recent.
But I have… I don't know the exact date.
**Jason Plumb** 53:01 Yeah, so we need to match that. Have we… if we… Have we… My brain is not working. Have we merged, any renovate PRs that bump us to the latest instrumentation yet?
Are we on 2.24 now?
**Cesar Munoz** 53:20 This country… collector, no, this is something else. What about closed?
Yeah.
**Jason Plumb** 53:28 He goes, okay, it got merged, okay.
So, that's cool. So, we should think about doing a release. Are there any PRs that are currently open that we want to have in this next release, which is gonna be… 1.1.0.
**Cesar Munoz** 53:47 Like, not that I think it's urgent.
**Jason Plumb** 53:49 Maybe the disk… what about the disk buffering one, that exported batches one? That's probably the one, right?
**Cesar Munoz** 53:57 Yeah, this could be one.
**Jason Plumb** 53:59 Okay, what else? Is there anything else?
**Cesar Munoz** 54:03 I was thinking about the Kotlin one, but it's a… since it's a breaking change.
Not sure if we want to discuss it a bit further.
**Jason Plumb** 54:12 Yeah, I don't want to force that into this week's release.
**Jamie Lynch** 54:16 Yeah, it's also… I think, like, Code UL CI checks are failing, because they don't support calling people.free yet.
**Cesar Munoz** 54:28 I think that would be the one for now, at least for me. I don't know if somebody else… sees PR that they would like to have to include.
**Jason Plumb** 54:40 Okay, sounds good. I can get that started probably later today or tomorrow.
By that started, I mean I will get the release process started.
**Cesar Munoz** 54:50 Got it. Thank you.
**Jason Plumb** 54:52 Yeah.
**Cesar Munoz** 54:54 Well… I think that's it for today.
**Jason Plumb** 54:57 Cool. I'm… if anybody's joining the Client SIG, the client SIG meets after this, I'm gonna skip it today, just cause I'm out here.
**Cesar Munoz** 55:15 Okay, well, if there's nothing else, then… Thanks for joining.
**Jason Plumb** 55:21 Appreciate everyone.
Thanks.
**Cesar Munoz** 55:23 Right?
**Jamie Lynch** 55:24 Right.
**Jason Plumb** 55:25 Right?
