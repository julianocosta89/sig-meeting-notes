SIG: Kotlin SIG
Date: 2026-03-09
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/avu0aBGeM5dCVfrAjNHUZc5gO6J77Lx5ORDudy71zq3JCW5egoy0sWQm6JL0mbyi.XfI1FUp98YLJzVVC
============================================================

## Zoom Recording Transcript

**Hanson** 00:17 Hello, my world.
**Jason Plumb** 00:18 I need more of me.
**Hanson** 00:21 Say you need more review?
**Jason Plumb** 00:24 Yep.
**Hanson** 00:26 Yeah, that fork… human fork hasn't happened yet.
I feel the same.
**Jamie Lynch** 00:39 If you're in it?
**Jason Plumb** 00:42 What's up with, what's up with our other approver?
Do they exist?
**Jamie Lynch** 00:50 That's a good question, I won't ping him.
About whether he's able to make this SIG.
**Jason Plumb** 00:58 Have they been very active?
I feel like I'm not as active as I want to be, and I feel like they've been less active than me.
**Jamie Lynch** 01:07 They've not been active over the last couple of weeks, yeah.
**Jason Plumb** 01:11 Okay.
**Jamie Lynch** 01:12 We did get a couple of contributions at the start, and a couple of reviews, so… Okay. Yeah, maybe I can just ping them and see.
Let the variance, continue.
**Jason Plumb** 01:23 Cool.
**Hanson** 01:25 I'm hoping that when this gets off the ground a bit more in terms of usage and stuff, more people come in and be more active, and hopefully then the…
The people who should be approvers and maintainers would be more apparent, so…
**Jason Plumb** 01:40 Totally, and I mean, I think there'll be a good…
swath of user base that will just use this on Android. They're like, I don't need all this instrumentation, I just want to make some spans sometimes, or I want to emit some events, like, that's…
I think there's gonna be a lot… a good chunk of the existing user base is just doing that. And there's people that are gonna be coming from Java. There's people using the Java SDK, I'm sure, who are like, oh, Kotlin's available? Yes, and they're just gonna, you know, just be manual.
instrumentation users.
**Hanson** 02:09 Somebody, already talked about being that, on the.
**Jason Plumb** 02:12 Yeah.
**Hanson** 02:13 the Android group, so…
**Jason Plumb** 02:17 And I'm gonna, I'm gonna duck out at 9.27, so in 25 minutes.
**Jamie Lynch** 02:22 Cool.
Have to. Okay.
Cool, then I guess we'll make a start quickly then. If folks have items they want to add to the agenda, please add them in.
So…
First item is, should we release this week? Because it's been about 3 weeks now since we shipped something.
There'd been quite a few changes.
Under that?
**Hanson** 02:52 Yeah, I think so, especially if we could, get to the bottom of the, the API compatibility issues. I think if the only one… I think there's…
Well, we should release regardless. Period. I'll say that.
**Jason Plumb** 03:11 Do we take any dependencies on instrumentation? I think the answer is no. Java instrumentation?
**Jamie Lynch** 03:17 No.
**Jason Plumb** 03:18 Okay, but we do… we do take one on the SDK still for a while. Okay, and so they released last week, I would just make sure that we're up to date. Like, I think they released on Friday, and we probably got Renovate for it already.
But we would double check.
Otherwise, I think, yeah, I think it would be good to release.
**Jamie Lynch** 03:36 Cool.
**Hanson** 03:38 Yeah, I guess with the compatibility stuff, it kind of forces the compat implementation to release,
pretty close to Java release, so this monthly cadence is probably forced upon us as a baseline, or at least keeping up with Java. So, if we want to have releases in between for API updates and stuff, we can do that, but,
This makes sure that we will be behind if we don't release monthly, so…
**Jamie Lynch** 04:07 Cool. I'm happy to take that on. I'll probably aim for midweek.
**Jason Plumb** 04:14 Cool. That's great. I would love to run through the paces as well sometime, but not this month. Nope.
**Jamie Lynch** 04:19 So…
**Hanson** 04:24 I can try the next slide.
**Jamie Lynch** 04:28 Cool. I'll hold you to that.
Cool. Next item, just to make folks aware, basically, I've opened up… A APR…
Come folks see us, okay?
**Jason Plumb** 04:45 Yep.
**Jamie Lynch** 04:45 Yeah, okay.
So it basically just adds an initial guide on how to get started for the Kotlin SDK on the OpenTelemetry I.O. website.
So… pretty straightforward, just kind of listing out what platforms we support, what caveats there are around that, how to install it.
And, yeah, basically, how you would use it in an application.
So…
yeah, I guess if folks get the time to look at that, that would be helpful. And I guess maybe a broader question.
There's…
My personal take is I'd quite like the website, OpenTelemetry.io, to be the source of truth for most of our docs, rather than the README. So, I was thinking, once this is merged down, and a few other pages are in, we can still tell my README.
But I want to know what other people think around that.
**Jason Plumb** 05:47 That's good, I think it's consistent with the other repos.
**Hanson** 05:51 It's never good to have two sources of truth, so might as well force everything here, and then link to it, and the other one being a soft link, so we don't have to deal with it.
**Jason Plumb** 06:00 I just think it's a bummer to be separate from the code, you know? It's like, and you can actually have real, working, compilable examples in other repos, and it's much harder in the I.O. repo. But I think it's good. It's consistent with everything else, I think.
**Hanson** 06:13 I mean, if we want to have, like, a separate breakout simply for instructions about the sample project and compiling that, we could have that.
But that's more of, you know, this is the repo, so hopefully that doesn't really change.
Like, the details about the sample will be on the website, but, like, basic instructions, you know.
We could probably include that.
**Jason Plumb** 06:40 Yeah, I mean, keeping the examples that are in the docs up to date as we make API changes is gonna always be a challenge, too.
**Jamie Lynch** 06:49 I don't know if there's other…
**Jason Plumb** 06:51 There might be… I definitely know that there are other areas that have…
Dependency automation, so, like, after a release, it'll go and update the versions that are listed in various docs repos.
But I don't know if there's anything that actually tries compiling. There might… Java gets pretty fancy with some of this stuff, so they might have examples that compile, I'm not sure.
**Hanson** 07:14 if they are different projects, like Dependabot or something like that, or Renovate, we'll… should, you know, release an update and say, hey, your SDK has been updated, so… I don't know that…
**Jason Plumb** 07:26 Lendabot will check in Markdown files, though. If it's just docs, I don't know that it can update that.
**Hanson** 07:32 Got it. No, no, yeah, you're right, you're right. I was more thinking about the, the project.
Nope. Yeah.
there are ways… I think the validation part's the hard part, like, I think Markdown could probably reference something that is updatable, but if we say, hey, we updated, and the Markdown's updated, but it actually doesn't compile, then, you know, then that's not great, so it's almost like.
**Jason Plumb** 07:58 Right.
**Hanson** 07:58 The two-step thing.
**Jason Plumb** 08:00 I know, yeah.
**Hanson** 08:02 there's always a GitHub action we could run, like, after validation, that we could, like, say, hey, go and replace this variable, which is referenced, or something like that.
**Jason Plumb** 08:13 Yeah, all this stuff seems, like, so forward-looking and should not block, like, the first PR, you know? Like, yes, let's keep doing the good work, and then, you know, when we're bored one day, we can come back on this stuff.
**Hanson** 08:24 We could create an issue in the repo and say, hey, let's somebody do some automation for updating versions or something like that.
**Jason Plumb** 08:36 And I'd rather have a broken example than no example.
And at least if someone…
grabs the example, and they try it, and they get frustrated, and they'll open an issue, or not, but at least if they open an issue, we're like, yes, someone's looking at it and trying it. Like, we have some amount of testing from users.
Great.
**Hanson** 08:56 So, are you advocating for just a blind update of the version, and just YOLO, and if it's broken, then somebody will report to us?
Or we'll go and fix it, if the.
**Jason Plumb** 09:06 Down the road? Yeah, down the road? Sure, yeah, yeah.
I would do that, yeah. I don't think those two things… like, updating a version number that's in a copy-pasteable example, I don't think that has to be coupled with actually, like, compiling.
**Hanson** 09:20 Examples as automation. Yes.
**Jason Plumb** 09:23 But I think, like, I think in Java they have…
some sources that are in the docs that come from actual sources that do get compiled. I think maybe that's how they do it. But they don't live in the… they don't live in the docs repo. I think they live somewhere else, and then they get snippetized in or something. I… I can't remember, but…
**Hanson** 09:42 I bet we can change, with GitHub Actions, chain, a compile task that updates the version, and then basically, conditionally, if that runs, create a PR that updates the docs in the repo as well. So that's probably doable.
**Jason Plumb** 09:59 Yup.
**Hanson** 10:04 For later.
**Jamie Lynch** 10:05 Lots of… Yeah, true.
Okay, cool. Yeah, so next topic, I think I might have mentioned this last week, but… basically…
I was gonna look at the PRA open for spec compliance and matrix, and create some issues based on that, so that it's fairly obvious what features are missing from the repo.
So… I guess before I go and create dozens of issues, would everyone be happy with that approach? And…
Is there anything… Or any particular way that we should do that. Like, I was thinking…
It might just be helpful.
for folks looking to contribute to see, oh, I need to implement this function named foo on this interface, and it's clearly defined in this spec.
**Jason Plumb** 11:05 I think that's good, as long as they… especially if they can be grouped, by label, even. If it's spec compliance, that's cool. If there's, like, spec compliance matrix, that's also fine, like, new label. But if they were scattered and couldn't be pulled together, then I think that might be a problem, but I think this is a really great idea. I love…
Seemingly small-scoped issues.
**Hanson** 11:31 Yeah, a label would work.
**Jamie Lynch** 11:39 Cool.
Well, maybe what I'll do is I'll take all the things that are missing from one API, enter those in, see…
How folks feel about how that looks, and then do your best.
**Jason Plumb** 11:55 Yeah, do you have a sense of the scope? Is it probably, like, a dozen or a couple dozen?
Hard to say.
**Jamie Lynch** 12:05 In terms of… I guess it depends on how you want to group, features.
Bye.
Looking at the spec compliance matrix, there's probably, like, 100 plus rows of things that we need to change, but some of those are covered
Bye.
Yeah.
Some of those you could cover by… you could cover multiple of them with one issue.
**Jason Plumb** 12:29 Yeah. Okay.
**Hanson** 12:31 Yeah, if we could somehow get this into, like, 5 or 6, like, that number, like, if there's, like, 5 or 6 missing rows, then we can have one issue per row, but if it's, like.
20, if we could somehow collapse that, especially things that…
you will likely deal with one if you deal with the others, that would be ideal.
**Jamie Lynch** 12:55 Okay, cool. I will, take that
Okay, next topic…
was this one. This was raised by, a guy who I think works for Gradle.
So, he pointed out that the library only supports JVM, Android, JavaScript, and iOS, and he was interested in using
this on… Loads of different platforms, basically.
So I think… Yeah, there's a little bit of discussion around this, and…
Yeah, by the sounds of it, like…
he'd be happy with just having, like, the core packages, basically build for all the targets, because then, even if you need to build your own export, so it's better than starting off with nothing.
So… Yeah, I guess what were people's thoughts on this?
**Hanson** 14:08 Is he volunteering? Oh, go ahead.
**Jason Plumb** 14:10 I was just gonna say, this sounds like a perfectly fine long-term goal, it sounds like in the short term, it's gonna be more of a distraction for a team that is resource-constrained, but…
I think it's a good idea, I'm not opposed to this at all. I think having support for all kinds of targets would be amazing.
**Hanson** 14:29 I would want someone like him or somebody to come and do the work. I mean, there's gonna be some amount of maintenance on our end to make sure all the compilation works. A bit extra friction when we're, like, you know, compiling, you know, locally and running tests.
I don't mind if he's got a contribution rate ready to go, but,
I… this would be fairly low on my list to do if I compare it to the other things that are on the list of to-dos right now for us, so…
where… where did it end up? Like, is he… is he saying he'll do it, or is he saying, we should do it, or…
**Jamie Lynch** 15:16 I think enhancement and help wanted labels were added.
**Hanson** 15:21 Got it. But.
**Jamie Lynch** 15:23 Yeah, I think…
That's similar to where I feel on this. I think I'd take it if it was a PR.
Assuming it didn't blow up completely times.
Or Fixed compilation times.
But yeah, I think… It's not top of the sack, right now, for me at least.
**Hanson** 15:51 I think getting things P0s done, like, this is usable for a platform, and then saying, let's compile for other platforms. I think that's a reasonable, tiering of work.
**Jason Plumb** 16:06 Was there any discussion of native in that thread? I didn't see it.
Have we talked about native at all, anywhere?
**Jamie Lynch** 16:18 We haven't, but.
**Jason Plumb** 16:20 AMP supports some amount of, like, native compilation, right?
**Jamie Lynch** 16:24 Yeah.
And… I think the iOS target, basically.
Relies on native to some extent, but we don't have a just native target.
**Jason Plumb** 16:36 Okay.
**Jamie Lynch** 16:36 Yeah, I think the use case for this was basically all the targets.
Which, I guess, if it's, like, for internal tooling for Gradle, that probably runs on a load of…
Different targets.
**Hanson** 16:53 They said Tier 1, is there, like, a list that says, like, what the tiers are?
**Jamie Lynch** 16:57 There's a list on JetBones' website, so they… Tier 1 targets are, like, Android and iOS, where they run tests against it, and then there's different tiers where…
Well, it compiles, and then it's kind of thrown out into the wild.
**Hanson** 17:19 Yeah, I would like this, but, you know, let's get it working for one platform first kind of thing.
**Jamie Lynch** 17:23 Yep.
**Jason Plumb** 17:25 the native tiers are kind of hilarious, because Tier 1 is, like, macOS ARM64. Like, really? Okay.
**Hanson** 17:34 Mac or Expo.
**Jason Plumb** 17:35 Linux… there's no Linux in Tier 1, it's all Tier 2 before you get to Linux.
For native compilation.
**Hanson** 17:43 It's whatever they think people use, or they themselves use.
**Jason Plumb** 17:48 Yeah, and developers all use Macs.
**Hanson** 17:51 So…
**Jamie Lynch** 17:57 Cool. I will… Respond to that issue after this.
Okay, next topic, Hanson, discussing the read API again.
**Hanson** 18:12 Yeah, so I just basically wrote down what I was talking about previously, in… in an issue, so we can talk about it more in the open. The reason why we want readable span, or span to be readable, I proposed an alternative, basically saying span could have an interface, like, get readable span, so it's not directly on an interface, it's a little bit of indirection.
We can also warn there, say, hey, only use this for these cases, don't, whatever. Ergonomically, it's one extra call, but it allows us to basically warn.
So it bypasses all the boilerplate necessary for us to… for others to basically fish it out of the processor and have reference to it, and yet still not make it completely, easily, and perhaps, mistakenly referenced, if folks aren't
literally needing it for a very specific reason. So, I think…
I'd be okay with that compromise of…
having span, have get readable span, or get readable, or whatever.
So we'll see what others think.
**Jamie Lynch** 19:26 Yeah.
I think I'd be… Okay about that too, although… I'm…
Maybe we could put it in, like, the API extension module, or…
Something like that, because I would…
Yeah, but I guess for my base hat, I want…
I definitely want to be able to read these attributes, but from very.
**Jason Plumb** 19:49 And so I…
**Jamie Lynch** 19:50 Thanks.
**Jason Plumb** 19:50 I mean, I haven't gone deep on what you all are doing with this yet, but I don't have a great…
use case for this in my brain yet. I'm sure if I looked at some example code or some of the Embrace code, I might be able to divinate something, but I don't… like, I… and I'm also, like, strongly biased toward Java, and I've been involved in the Java APIs for so long that, like.
Like, when… why do you want to be able to read anything about the span?
While it's still in flight.
**Hanson** 20:20 So, I documented, I think, the most important one, which is the long-running span, and not being able to have access to it via Snapshot, so that we could, you know.
when the app process crashes, we have, like, a record of the span existing, what the state of it is.
**Jason Plumb** 20:37 So, hold on, so there's something that was persisting the span details, like, as it's in flight, like, periodically?
**Hanson** 20:44 Yeah, we would, we would, snapshot the span, every, like, 2 seconds or whatever, so we have a record of spans that are ongoing.
**Jason Plumb** 20:53 Okay, and so that… that thing that's… that thing that's persisting the…
point-in-time representation of that span needs to be able to read the… the detail. That's what you're getting at, okay. Yep. Okay.
**Hanson** 21:09 we can create additional friction. So I agree with Jamie's,
implementation suggestion, which is putting it the, as an extension function. So it's just as available as long as you import it. So, that's another degree of separation. So if you look at the interface, it's not there, but hey, it's actually there if you look in the right spot.
**Jason Plumb** 21:32 Yeah, so doing something like that is mostly…
an internal implementation… like, this specific use case is an internal implementation byproduct, it's not something that users would typically want read access for.
**Hanson** 21:48 And…
**Jason Plumb** 21:49 Make, like, providing read access… Has some performance implications.
I think… I don't know, I would like to give some consideration to how we…
Might design this in a way that doesn't encourage users to be monkeying around the spans.
**Hanson** 22:06 Well, another option that backs it up a little bit is basically implement a snapshot function. So basically, we will get… give you a state of the span at this current point, and by definition, that's readable, because it's span dated.
**Jason Plumb** 22:25 That is interesting. Yeah, it's almost like, oh man, that's almost like the third method on span processor.
Right? You have start, you have end, and then you have, like, checkpoint, or… yeah, interesting. Current state. Yeah.
**Hanson** 22:37 And, and that, that…
it's… that's good, because that's, like, primary use case. And also, it kind of sidesteps the mutability issue, because it's… from the interface, it's still mutable, because what you get is a copy. So you would have to manage your own, kind of, synchronization, if that's as important to you.
People who misuse this, could potentially create a lot of snapshots, but that's kind of…
almost by design. We don't want… if we don't want people to, like, look at that as a reference, and they basically have to pay a penalty if they want to do that, or they have to do a wrapping, and, you know.
**Jason Plumb** 23:14 Yeah, yeah, that's interesting. So, what if… yeah… I mean, you've put some thought into this, which I think is great. I haven't, I'm winging it on the fly here. What if,
I have to go, and this is a bad time to, like, start solutioning, but I'm imagining a world in which, start, like, you know, span start.
Had a callback, and maybe a period, or a duration, or something, and then the internals could provide a read-only representation to that callback periodically.
I don't know, I'm just… I'm riffing here.
And then… and that, you know, doesn't necessarily impact the span processor API at that point, it's just, like, it impacts the start API, which is maybe worse, I don't know.
Or it's an extension. It could be an extension.
**Hanson** 24:02 That seems like a lot of boilerplate. I'd rather initially just stick something in there to be, like, ad hoc.
**Jason Plumb** 24:08 So, I could… I could add to this. I'll add a comment to the issue and say, hey, we discussed this, and…
**Hanson** 24:15 We have some ideas around this,
The performance disadvantage could be an advantage, simply because, you know, It's more friction.
**Jason Plumb** 24:26 Okay.
I'm sorry, I have to drop.
**Hanson** 24:29 No worries.
**Jason Plumb** 24:30 It's good to see you all.
**Hanson** 24:31 See you tomorrow!
**Jason Plumb** 24:32 Take care.
**Hanson** 24:33 I…
So I think… if…
if we're looking at this as an extension function, or something that's an addendum to span, we can probably proceed without the readable portion, and basically have the readable portion be something to be added on, via this issue.
Which would basically clear the hurdle of compatibility for read-only.
**Jamie Lynch** 25:04 Yeah, I think also if we made it an extension function that is isolated in one place, and we could remove that in future
for another solution. It makes it a lot easier to remove than the current readable interface.
**Hanson** 25:20 It's kind of cheating, but hey, it's… it's… it works, so… I'll take it.
**Jamie Lynch** 25:29 Okay, are you okay to summarise what we just discussed on the GitHub issue, and I'll…
Then probably take a look at it.
**Hanson** 25:39 Yeah, sounds good. I'll do that.
**Jamie Lynch** 25:50 Cool.
**Hanson** 25:50 The other… the other two issues, we could take it, when there's just more than me and you, I think. But, to quickly go…
**Jamie Lynch** 25:58 So we'll, leave those for next time, man.
**Hanson** 26:01 Okay.
**Jamie Lynch** 26:04 Cool.
**Hanson** 26:05 Alright.
**Jamie Lynch** 26:06 More than…
**Hanson** 26:07 Cool. Yeah, I think I've… I'm going through your PRs, right now,
Yeah, I'll probably do all that, and then I will,
work on the… I'll update the issue right now, and then I'll probably get some… get the embrace stuff done, and then I'll go back to, adding additional tests to that last PR, which will hopefully be ready for you to look at tomorrow morning, so…
**Jamie Lynch** 26:33 Nice. Sounds good.
**Hanson** 26:34 Alrighty.
**Jamie Lynch** 26:35 Oh, yeah.
**Hanson** 26:37 Right?
