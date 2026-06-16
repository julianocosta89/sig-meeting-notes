SIG: Kotlin SIG
Date: 2026-06-15
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 00:30 Hello Hey, Juan.
**Juan Vega** 01:12 Nice to meet you.
**Jason Plumb** 01:15 You too, are you based in Barcelona, or where are you based out of?
**Juan Vega** 01:19 Yes, well, no, I'm based in Spain, but in Canary Island.
**Jason Plumb** 01:23 Okay, cool.
I just asked Barcelona, because I know when I worked at New Relic 6 years ago, they were building up a big Barcelona presence.
**Juan Vega** 01:31 Yeah, but we are actually remote, within Spain, so in Barcelona, it's, like, maybe half of us, and then the rest of us are all across the country.
**Jason Plumb** 01:40 Cool. Awesome.
Well, it's exciting to have you joining us, I think that's great.
We'll give it another minute in case Hanson's gonna show up.
I, Francisco, which I think I've heard Hanson use a shortened form of your name, do you prefer that?
Yeah. Yeah.
**Francisco Prieto** 02:06 I'm usually called France.
**Jason Plumb** 02:09 Fran, okay. I'll try and remember that.
**Francisco Prieto** 02:13 Never wrote him.
**Jason Plumb** 02:16 Cool, so we have a pretty light agenda so far, so if you have something you want to talk about, please feel free to add items.
Otherwise, we can kind of cruise through this, and then maybe peek in on any new issues or PRs, and kind of focus on… What we want to be doing.
So, I'll start us off. I was… pointing something… from the community page, like, I think I went, like, community, and then I looked for Kotlin… And then I was like, oh, I noticed that they have GitHub discussions here, and I'm like, I'm pretty sure we don't use those.
And just visually, you know, a few other teams still have them enabled.
But I think most of the other stuff I work on doesn't really use GitHub discussions, and I personally am prone to just, like, not seeing them, so if someone comes into… the repo, and just, like, goes into discussions and, like, creates one. Like, fortunately there are none, but I would probably miss it. I probably would get notified and just not really think about it, so… I'm inclined to… Not, like, to turn them off, and just not have them, and favor issues.
Cause it's kind… like, there's really not much… of a benefit of discussions over issues, and I think… Many users are comfortable just using issues.
**Juan Vega** 03:44 In other communities, like, you go to these classrooms to either announce leads or ask.
questions or proposed features, no? But in our case, or in OpenTelemetry war.
That's going to be issues, because it's following the spec, maybe bugs, or… improvement, no? But it's more like issue style. Like, discussions are more like… I mean…
**Jason Plumb** 04:10 Yeah, like, for questions, too, yeah, like, even… even, like, these categories, right?
Hey, here's a cool, like, let me show you a cool thing I did, or like, what's the best way to do this? Like, I get that.
But I feel like… I feel like you can still just do that in an issue, and it's not a problem.
You know? Just to… just to cite other art, and kind of where I'm coming from, is, like, Java… No dis… They do have discussions, but I think people don't use them.
Alright, so this is 2021.
**Juan Vega** 04:43 Yeah.
**Jason Plumb** 04:44 Oh, there are… there is some stuff in here, I had no idea they were still using these.
Well, gross. Okay, well, instrumentation… They still haven't enabled.
Okay. I think I'm proving myself wrong.
Android, it's still here.
Well, although…
**Juan Vega** 05:11 Yeah, but it's empty, no?
**Jason Plumb** 05:12 Yeah, this screen looks different, like, it's not actually… I think you have to… I think this is what it looks like when it's not enabled.
**Juan Vega** 05:18 Okay.
**Jason Plumb** 05:20 Okay, so that's Android. I was kind of surprised about instrumentation.
**Juan Vega** 05:27 I wonder how many of these could be an issue, because how to set Java log… I mean, this is an issue, no? Like, are you going…
**Jason Plumb** 05:34 Yes, yeah, exactly.
**Juan Vega** 05:36 Are you asking Slack, maybe, no? Like, or, well, I don't know.
**Francisco Prieto** 05:41 But would you open an issue if you had, like… because this looks like a question, I'm not sure if I would open an issue.
**Juan Vega** 05:48 Hmm.
**Jason Plumb** 05:52 Okay, well, maybe, maybe my… maybe, okay, so I think… I think we're maybe split, and I don't… Like, without Hanson here, without, you know, Jamie here, maybe we don't have consensus to do this, and it's… whatever. If we took it down, we could still put it back, it's not a big deal. But maybe the short-term solution is just to remove it from the community page.
I think that's probably… like, if I can just get this removed, that'll be the shortest. I think that will ease my… my twitch a little bit, because that's how I got in this whole thing to start with.
**Francisco Prieto** 06:28 I think it's… if the idea is to drive people to Slack, I think removing that makes sense.
But I personally, like, if I was… not really a part of the OpenTelemetry community, if I didn't know anything about OpenTelemetry, and I just bumped into the repo, or I was told by my team, hey, implement it, and I do have a question.
**Jason Plumb** 06:51 Yeah.
**Francisco Prieto** 06:52 expect to find a Slack channel. Like, in my mind, I wouldn't have a Slack channel in mind, and if I solve issues and discussions and I had a question, I will go to discussion, I think.
**Jason Plumb** 07:04 You think you would? Okay.
Okay.
**Francisco Prieto** 07:06 But I do think that removing it from here makes sense, so…
**Jason Plumb** 07:11 Maybe what's also funny is, like, the fact that there's not a link to the actual repo.
Like, these are all just place… like, these are all just, anchor links.
**Juan Vega** 07:23 Yes. But from to the row, it's an ankle into the row.
**Jason Plumb** 07:28 Yeah, which is interesting, because it's not even… there's no link to the repo.
So I will… I'm gonna PR a change, which is gonna link… the name to the repo, and I will… I will remove discussions, because I… I don't want the… I don't want people to go… I don't want people to use discussions.
So there's the compromise. We'll leave it enabled, and just discouraged from the community, at least. Okay, I will take that on.
Okay, I think that's fine.
Alright, Juan, I… Appreciate you being here, and I'm stoked that you want to help, and I think you have a very good question. What is the best way that you can help out right now?
**Juan Vega** 08:38 Yeah, like, I started by implementing… well, I started by changing the contributing. Like, actually, David made, Uncommon, but…
**Jason Plumb** 08:46 Yeah.
**Juan Vega** 08:47 I don't have enough context, actually, to know if… That's right or not, like, And then I have a beer, like.
Someone else implement. Okay, great. Anyway, I will pick any other task.
Which one? The always, always record sampler.
**Jason Plumb** 09:07 Yes, yeah.
Where is that?
**Juan Vega** 09:12 Because we have so many PRs, no, you have so many PRs that maybe it's like, yeah. I didn't know if open more PRs is actually…
**Jason Plumb** 09:20 So, I think the short answer is for a lot of projects, including Kotlin, we need reviewers. Like, we need people who are able to come in, and I've seen you… I've seen you already do this on a couple of other PRs, which is actually really helpful.
But we need people who can look at, you know, these 137 lines of the Always Record sampler.
Actually understand what it does, and then, you know, give a review or provide feedback.
Much like Fran has done. So that's really helpful. First and foremost, getting reviewers is, like, the biggest thing we can use help with.
And then… That, I mean, yes. In short, that's the next thing. And then also, we do have a ton of, like.
kind of more bite-sized API and spec issues that we could use implementations for.
So, PRs. But, as you pointed out, you know, we have a good chunk of PRs right now, but it's not… I think this is not unbearable.
A bunch of these are things that we should just close. Like, we're not ready to do Kotlin 2.4 yet.
**Hanson Ho** 10:23 We, we're not… We're moving.
As, as runtime, not… obviously not as, not as language version, but, we may be. I'm spending this afternoon on some of this stuff, so…
**Jason Plumb** 10:34 Okay.
Killer. Nice to see you, Hanson.
**Hanson Ho** 10:38 Yeah, sorry, it took a while.
**Jason Plumb** 10:40 No, you're fine.
Monday morning, 9am. I get it.
And, what else? So, we have… some milestones related to working towards stability for various API components, and I think I just merged this, so… We now have this matrix.
of which parts of the API are stable and which are in development. The idea being that when something goes stable.
because the API is one module, we can't stabilize, like, we can't, sort of properly make… each of these things stable, but we can at least declare them in the matrix here as, like.
when all of these are stable, we will mark the API as stable, basically.
So we have PRs related to all of these, and I think we have milestones related to all of these.
And what… if there are open issues that are bite-sized to implement, that would be great. We're kind of starting with attributes.
Because all of… many of these other components depend on attributes, and so getting attributes internally stabilized first before, stabilizing these other ones, I think, is the way to go, and I think we're really close, so to show you where that is… Under milestones, right, we have a bunch of these, and attributes, for example.
Has 8 that are closed and none open.
So I think that there's nothing… I don't think there's any work remaining, actually, on attributes, short of probably moving that little marker over. Like, that's probably… I think we're ready to do that after having talked about it for a couple of months.
And not really having any other changes. Hanson, are there any changes left on the…
**Hanson Ho** 12:41 Yeah, removing the experiment API, experiment API, annotation. I think we decided last week, that, when, when a particular, file is ready,
**Jason Plumb** 12:55 Yeah.
**Hanson Ho** 12:55 we removed that, and by virtue of… because we're not doing any of the versioning alphas and stuff like that, so by virtue of a particular API being free of public API that has that marker, it is, by convention, stable.
**Jason Plumb** 13:14 Okay, so we… we need a PR in that, In that milestone then, and then we can close it out.
**Hanson Ho** 13:22 Yeah, unless there's a milestone that says stabilization or something like that, there may be one, because I know you can't have milestones include milestones, or…
**Jason Plumb** 13:29 I know, it's so… Let's see…
**Hanson Ho** 13:33 If there isn't.
**Jason Plumb** 13:34 Here, No.
**Hanson Ho** 13:39 If there isn't, it makes sense to actually put it in the actual API milestones, so…
**Jason Plumb** 13:45 Let's just do this. Yeah. Let's just say… remove… You would think, since I clicked new issue from the milestone page that it would have already defaulted to milestone, but… Kinda asking a lot.
**Hanson Ho** 14:34 Well, I guess, technically, that's just a regular filter, and the milestone doesn't know the filter is for particular milestones.
**Jason Plumb** 14:42 Yeah, okay, so there's just a placeholder, a little silly issue for someone to pick up.
And then if we… so, coming back to Juan's question, like, what's… what can he help with, what's, you know, what's helpful, Within each of those milestones, there will, except for attributes, because we're almost done with it.
there should be other issues, because Jamie did a really good job of, like, going… Jamie and Carlos, like, did a really good job of going through spec stuff, and just, like, picking out 1, 2, 3, like, this needs work, this needs work. I think logging is our next one.
6 closed, 1 open, so this is… this is remaining.
And Carlos did a really thorough job, I think, on the tracing API.
Which we don't have a milestone for? We do, okay, I just needed to scroll.
So there's a bunch of work left to be done on tracing, and then also… I think… Resources probably needs to happen sooner than some of the other signals as well.
And that's pretty close.
Yeah.
Alright, I'm gonna open that up for Juan to ask follow-up questions.
Is that specific enough? Is that helpful?
**Juan Vega** 16:02 Yeah, what I noted is I will try to review open PRs.
share what I can share, and then I may jump to any of the milestones, and I try to… to push for mixing issues, maybe, or… Or… yeah, I guess not, like… any issue? I can… or do you have any way of periodizing issues?
**Hanson Ho** 16:27 So there's a bunch that's… that is, listed as, like, good first issues. I know this wouldn't be your first issue, but, I would scan those, and if there are ones that are, like, fairly, seemingly important, and perhaps, like, you know, fairly simple to do, because I remember there were a few.
**Jason Plumb** 16:42 There are none of those. Oh, what?
**Juan Vega** 16:44 That, help wanted, none of them are good for issues or help wanted, that's why I'm asking.
**Jason Plumb** 16:51 Yeah. I think that we don't yet have a good way to communicate prioritization to new contributors.
That's a shortcoming.
Also, we're down a maintainer right now, just for what it's worth. Like, Jamie's off on leave, so we're just kind of… we're making progress, but it's slower than it would be, because Jamie has been a real force of nature here.
So…
**Hanson Ho** 17:14 There's a… there's a bunch in… sorry, in the tracing API, just, I'm just looking at this right now. they seem… they seem, like, fairly bite-sized and almost, like, buggy. So, I think… I think some of these could probably be taken, even if they're not… they're not labeled.
Because tracing is probably the most important one. Tracing and logging, obviously, the two APIs we want to stabilize the most. So, getting, tracing, stuff done, would be, would be super helpful.
**Juan Vega** 17:45 Okay.
**Jason Plumb** 17:47 Yeah, I think… I think you're free to choose anything under the milestones that have an end in API here. Those are going to be the important ones. Like I said, attributes is almost done. Context, I think, is also starting to wrap up. There's a few left, but we've, you know, made some progress on it.
After each contact resource are kind of like the precursors to maybe stabilizing metrics, logs, and… and traces, so… getting those first would be awesome.
And, just as far as, like, process goes, if you want to pick up… B3… Because that's really exciting, we still support B3. If you wanted to pick that up, then you could just leave a comment that says, please assign me, or I'm working on this, just so that other people know, and that there's not overlap with two people working on the same issue.
**Juan Vega** 18:34 Okay, yeah, I should have done that with the… with the other sample.
**Jason Plumb** 18:40 Yeah, just exactly because you saw that someone built it already, so… I'm not sure if they, I think they might be in Asia and can't join, if I remember, is that true?
Yeah, they're in Japan. So, I don't know that they did that process. We're also not strict about it, but… Yeah.
**Juan Vega** 19:00 Hmm.
**Jason Plumb** 19:02 But it would help. And also.
I would say, rather than saying, can I work on this, just say, I am working on it, and then if a maintainer or someone can assign, then when we get to that, we will. But at least that sends a strong message that, you know, don't duplicate.
Agreed.
Cool.
Yeah, we don't have a great way of communicating that priority, so I'm just gonna put it here for now.
I will call attention to… this… PR… Oh, that got approved, probably, like, on this call.
Or close to it.
**Francisco Prieto** 20:34 Yeah, there's just one comment, that I think… The event should be experimental, and you put, opt-in instead of…
**Jason Plumb** 20:45 Good, okay, I like that. Yeah, that's… that's a mistake. Awesome.
Thanks for looking at that. So… I'm kind of excited about this, because… Selfishly, I want to use this over in Android. So this uses the OpenTelemetry Weaver to generate these, events.
in Kotlin language, right? So, for example, let's just pick on the session event. So, session starts… Auto-generated file… And… you pass it, the session ID is required, right? So you can only create one of these when passing a non-null session ID.
And previous session ID is optional.
And it has one… so it does adhere to an interface that has one method called emit.
You pass the logger, which will generate the event.
And optionally, any additional attributes via Clojure.
So, I don't know, I think it's kind of nice to be able to use this, because then the user, like, specifically in Android, when we call sessions, we don't have to hard code these strings, these come directly from the semantic conventions. These classes then kind of nicely encapsulate the event, and then also communicate to the user, like, what attributes are required, right?
So I was kinda… I was kinda happy with how this came together.
**Hanson Ho** 22:05 So basically, you have an event that points to, constants that are attributes set on the event, and not directly on the attributes, that are… that are generated.
**Jason Plumb** 22:20 I… Maybe I'm not following your question.
**Hanson Ho** 22:23 Oh, so these attributes should be individually referenceable, correct? Like, under…
**Jason Plumb** 22:30 attributes. Like these? Like, session ID?
**Hanson Ho** 22:33 Like, yeah, session ID and session start and things like that.
**Jason Plumb** 22:36 Oh yeah, these, these come from… Oh, and that's a… I mean, that's a pretty good call-out, actually. These should refer to existing other constants.
Yeah. But the fact that this is auto-generated.
I think it's kind of moot, because these come from the same YAML anyway, so you could imagine this code being restructured to refer to this via constant import, but that seems a little more… fragile?
**Hanson Ho** 22:59 Yeah.
No, no, and…
**Jason Plumb** 23:02 Good.
**Hanson Ho** 23:03 I think it's fine the way it is, but I was just wondering if, like, this is, like, the first thing, and then you're gonna, like, you know, do something to modify this, but as you said, they come from the same source, so, you know, they cannot have different values. They're just kind of just reified in various.
**Jason Plumb** 23:18 Yeah.
**Hanson Ho** 23:18 You know, so…
**Jason Plumb** 23:21 Yeah, it might be nice to have that refer to the constant, because then you're… it sort of gives an assurance that they're using the same value, and that they haven't drifted, but… Yeah, guaranteed these do come from the… The weaver.
**Hanson Ho** 23:36 But yeah, it's nice.
**Jason Plumb** 23:38 Yeah.
Okay, cool. Thanks for the review on that one. I will make that change, -Oh.
Still in Google's hands, yeah, okay.
**Hanson Ho** 23:54 All y'all have been at are… oh, shit, no, never mind, this is the wrong sig.
Sorry.
**Jason Plumb** 24:03 Let's see here.
**Hanson Ho** 24:03 Yep, that's… sorry, mix it in.
Monday morning, sorry.
**Jason Plumb** 24:11 I don't… I don't know, I thought I'd have it… oh, is it here? No, dang. I forget where… yeah, we can talk about it tomorrow.
**Hanson Ho** 24:17 Yeah, don't worry about it. Not bad.
**Jason Plumb** 24:21 It's alright.
Yeah, so we're still getting, like, these Renovate PRs. You know, we… the stuff that we absolutely need to be… Manual about, maybe we need to just block list these temporarily.
**Hanson Ho** 24:43 Yeah.
**Jason Plumb** 24:44 So that we don't get… keep getting these PRs.
Because this upgrade from 8 to 9 needs to be very intentional, right?
**Hanson Ho** 24:53 Yeah, it should probably be, like, 8.0.2 or something like that, but, but it's definitely not that. This will require… this'll… yeah.
**Francisco Prieto** 25:04 I think in order to be comfortable merging those, we do need those tests that verify that we are embracing on our minimum version.
If I get some time this week, I will try to start that, but… It's been… a mess.
**Jason Plumb** 25:22 Is there an issue for that?
**Hanson Ho** 25:25 I want to say Jamie either started it, or… or has… has made an issue for it, I'm not sure, but, that would be… it would be good.
Basically, a sample project that's got all the minimum requirements, And then build to, To local, and then try to build that.
**Jason Plumb** 25:51 I think we don't have an issue for that, do we?
We definitely talked about it in a previous SIG, and that would be a helpful thing to have, is, like, tests that verify the min… the min versions.
**Hanson Ho** 26:06 can probably create a milestone for testing and add that in there, because I think there's a lot of things that we can improve.
**Jason Plumb** 26:15 Yeah, something that's kind of open-ended like that, to me, seems more like a label, where it's just, like, testing.
Because there's not, like, a… there's not, like, a delivery milestone for testing.
**Hanson Ho** 26:25 Yeah, fair enough.
**Jason Plumb** 26:27 I think, it would be nice to have a list of which, dependencies we want to sort of lock down.
like, this, like, min AGP version, we will need to, like, constrain that to only… to not automatically upgrade majors.
Do we know what other things we should probably lock down? Like… Like, is this one gonna be okay to merge? Even though, I don't know, like, why is it broken?
**Hanson Ho** 26:56 So, the… we can't exhaustively list them all, because basically any dependency could potentially pull in a dependency, so what we do need, actually, is the test that verifies the MIN requirements are adhered to.
**Jason Plumb** 27:10 This one… even this one screws us up, right? Like, we can't do this just yet, because it… yeah. Yeah.
**Hanson Ho** 27:15 I'm creating an issue right now, so, it'll be there in seconds.
**Jason Plumb** 27:21 Okay, so you think we can't do it comprehensively, but there should be… we should at least be able to pick some… As they come up.
**Hanson Ho** 27:28 Yeah, so, Kotlin, JDK, AGP, Gradle, Android, there's a hand.
**Jason Plumb** 27:39 Beautiful.
Okay.
**Hanson Ho** 27:43 And usually it's like, you know, when a library moves that, it moves one of those, and that's gonna break, so…
**Jason Plumb** 27:50 Cool.
That is helpful.
And I don't know if everybody on this call is aware of it, I know that half of you are, but, we are now using the… Generated semantic conventions from this repo.
So these… semantic conventions, these constants. This is prior to my event PR. These constants are now used in Android, so we do source these, even though, Android is… we have… Instrumentation in Android is not yet stable, and so therefore the telemetry emitted by those modules is not considered stable, but we do use these semantic conventions, whether they're stable or not.
So, like, these constants, for example, are used by the Android project, which means that we have one fewer Java dependency from… From Android.
Just kind of aligned with what this project is doing, so…
**Juan Vega** 29:01 this is… this pro… this, module is mixing… incubating, stable semantic conventions, because in Java, there are… there are two… Modules, no? But here we only have one.
**Jason Plumb** 29:13 It's true, because we were leveraging this instead.
**Juan Vega** 29:16 Okay.
**Jason Plumb** 29:17 So rather than… and Java doesn't have a good way of expressing that, so we've chosen to do it this way. I did a little stupid PR to see what it would look like to split them.
So this is more, like, aligned with what the Java repo is doing in terms of having separate modules, and look, this is absurd.
The line count.
But it just kind of shows that we… it's possible to do this, you know, we could publish them separate, but since we have… I think since we have the annotation, we… we've talked about this previously, but it's like, I think we like… I've come to terms with it not being the same, and I feel like that annotation is more Kotlin idiomatic.
So…
**Juan Vega** 30:04 Okay.
**Jason Plumb** 30:05 I'm okay with that.
**Juan Vega** 30:06 Yeah, because then you have to enable in the compiler, I think, no? Or… I don't remember how… Like, calling allows you to enable any… Once you enable incubating, you can use any… Incubating thing, or… This is a question, like, I have an idea how this works.
**Jason Plumb** 30:27 Yeah, you have to use an opt-in, so I think I can show you in, Android.
like, in the PR that did that.
**Hanson Ho** 30:36 You can opt in entire modules, files, line, class,
**Juan Vega** 30:44 Nice.
**Jason Plumb** 30:47 Yeah, I'll just show you an example of this, like… So this is the very first thing I came across. So, the HTTP endpoint conventions are not yet stable, or at least some of them are not stable, so we just opt in the whole thing to incubating.
Like that.
**Juan Vega** 31:03 Nice.
**Jason Plumb** 31:07 Cool.
**Juan Vega** 31:09 Didn't notice.
**Jason Plumb** 31:11 That is a, you know, this… this specifically, like, this warning around incubating is… this incubating is an Android.
Like, it's one of our annotations, but this is what we check, I think, at build time.
It's all wired up.
**Hanson Ho** 31:25 Yeah, there's a Kotlin, annotation that you can say, you can use this annotation to basically, warn or make errors. So it's a… it's an annotation that's leveraging an existing Kotlin annotation, so…
**Jason Plumb** 31:40 Yeah.
**Hanson Ho** 31:42 I created the testing issue, and also a milestone, so, you know, we could use it.
**Jason Plumb** 31:49 Cool.
That's the testing one. This one.
No, this one.
Oh, we just talked about it, we didn't… there's no notes on it. Okay, perfect.
Alright, what else?
Okay, well, I'm hoping to carve out some time today and just work through these issues. I'm gonna start bottom to top and try and make some progress.
in this direction, a few of these that have been stuck like this, I'm just gonna close.
**Hanson Ho** 32:44 Oh, you can sign it to me, because I had an action item last week, to… to… to basically sort this out, so… I just have not gotten to it, so… All the Kotlin 2.4s…
**Jason Plumb** 32:54 Alright.
Then I won't close it, I'll wait.
And I'll assign them to you if they're not.
**Hanson Ho** 33:01 Yep.
**Jason Plumb** 33:02 Okay, cool. Thanks for… thanks for doing that.
Okay, well, if there's nothing else, we can stop a little bit early.
Any other remaining topics of interest or questions?
Thoughts?
**Hanson Ho** 33:30 I remember, so last week, someone from the Kotlin Compiler team came and wanted to see if we could, you know, use their help in anything.
And we said we're going to go back and think about what we could use help on. So we may want to think about that and come back next week, I think, because he's going to come back, or something like that. I think this is an excellent opportunity, because I think some of the goals in the future would have this project be used, you know, in JetBrains.
by the folks who are contributing to OpenTelemetry, working on Kotlin. But at this point, I think there's almost so many things that they could help with. It's about what… what… what is best. I don't know if it's, like, you know, Kotlin idiomaticness, project setup, just, like, things that are, that are, like, second nature to them, and for us, is a little bit out of our comfort zone. So in terms of declaring, like, we're doing some things already that they, they're, that they're gonna recommend in terms of, like, specifying target language and, and, and, let's see how… language and standard lib, lib, compatibility, but are there anything else, that we could perhaps, get their, input on?
**Jason Plumb** 34:49 Yeah, I agree with the… kind of just cruising through and making sure we're not doing stuff that's not very Kotlin-like, or, like, that's not aligned with the future direction of the language and compiler.
I don't think we're using any special… I mean, aside from… aside from multiplatform being… a ton of compiler trickery. I don't think we're using anything that's, like, sort of custom or weird or fringy around that stuff, right? It's all… We're just leveraging what's out there.
But I… yeah.
I… I don't have a good answer as to how we might best leverage the Kotlin team's input, but having a review of some stuff to make sure that it's not… Not zany, not… not… not crazy.
That would be helpful.
**Hanson Ho** 35:43 So I know, I know they… they did a recent change in how they want KMP projects, to be, structured, or, or, like, if you start a new KMP project, it'll be structured in a little bit different way. I want to know if… if what we're doing is… is okay with that.
You know, or there's some somethings we should, like, reorganize in terms of, like, folders and stuff.
Just, you know, in the source code, so… things like that. It's like, they would know best, and I would not know.
**Jason Plumb** 36:11 They might also have some inputs on… Like, compatibility testing, like, best… like, how we might… best go about that, or if there's, like… if they know where some of the rough edges are, and we would want to make sure that we have coverage on those.
Because I don't know… I don't know where those rough edges are.
If they're… just as a, for instance, if they're like, oh yeah, iOS is adding all of this, like, weird stuff, and we covered it, like, but it's barely covered, or, like, it breaks in these few areas, we would want to make sure that we have those tested. They might have better input or insight into that stuff.
**Hanson Ho** 36:52 Cool, I'm sure we'll discuss a little bit more next week, so.
**Jason Plumb** 36:55 Yeah, yeah. Like, right now, I don't know that any of our… I'm just showing my… lack of knowledge around how this project actually works, but we… we don't actually run stuff on iOS in any of our builds, do we? We compile to iOS, but do we run stuff?
**Hanson Ho** 37:15 We have tests, for.
**Jason Plumb** 37:18 They run natively.
**Hanson Ho** 37:19 Yes. Well.
**Jason Plumb** 37:21 Including iOS.
**Hanson Ho** 37:22 Natively is, yes. So if, you can, if you don't have, Xcode, the right version, certain, certain tests will fail, just because it tries to launch the, the simulator and stuff. So…
**Jason Plumb** 37:37 It does, okay, okay.
**Hanson Ho** 37:38 Yep.
**Jason Plumb** 37:38 Can you, just since we have time, and I don't… I'm happy to learn more and to talk about this, can you, let me share again.
Can you show me where those tests are?
**Hanson Ho** 37:51 I would have to go and look and find it.
**Jason Plumb** 37:56 Putting you on the spot, so…
**Hanson Ho** 37:57 Okay.
**Jason Plumb** 37:59 I'm not being a jerk about it, I'm just like, I don't know where this stuff is.
**Hanson Ho** 38:03 No, yeah, I'd have to find it, too. It is…
**Jason Plumb** 38:10 alert.
**Hanson Ho** 38:12 So I would probably think…
**Juan Vega** 38:14 I think you have to search for EOS, because I… iOS, because I… I put in the contributing, like, to run certain tasks.
Yeah, you see the examples, a lot of the… I don't know about you, yeah.
**Jason Plumb** 38:30 Yeah, the examples are good, but these don't run automated, do they?
**Hanson Ho** 38:34 So, in core, I think.
**Jason Plumb** 38:37 Okay.
**Hanson Ho** 38:38 My thing is just refreshing right now, so it's not liking it.
I would look for, like.swift, because I think there are, like, there are .swift, like, test classes.
**Jason Plumb** 38:52 Examples, and then…
**Hanson Ho** 38:59 This is not.
The example app… no, that's not it.
**Jason Plumb** 39:08 I mean, these are great, I love that we have examples, but if they don't… run, then there potentially could still be problems, right?
**Hanson Ho** 39:17 This was a couple… this was a couple months back, but I definitely… I wasn't able to, like, build things fully, until I had, like, the latest, Xcode, in the simulator. So, It's… it's there somewhere.
**Juan Vega** 39:32 It is doing something, because when I set up the project, I had to install, iOS stuff, I have never used, like Xcode, platforms, emulator, and all of that.
**Hanson Ho** 39:44 Yep.
Like, it, it runs off of, yeah.
**Juan Vega** 39:49 the task is at all defined on the contributing, I have the task name. If you check the con… the changes…
**Jason Plumb** 39:59 Yep.
**Juan Vega** 39:59 like, Maybe not… maybe next, You see, EOS Simulator, EOS… that… that…
**Jason Plumb** 40:14 this thing.
**Juan Vega** 40:14 task for Graydon. Those are running something with Xcode, iOS stuff.
**Jason Plumb** 40:22 Okay, that's cool, so look for this string.
Probably.
**Hanson Ho** 40:28 Yeah, under source, there should be, a folder called Apple Main, where this stuff lives.
So I think anything that's got, Apple MAME will have, specific, iOS, implementations, and though we should have tests that are…
**Jason Plumb** 40:49 as their Apple test.
**Hanson Ho** 40:52 Yeah, I'm trying to…
**Jason Plumb** 40:54 Common test.
It says, JVM test… There's Common Test.
And then there's mains for Apple, mains for JS, but we don't have the equivalent test modules, so it seems like maybe there's a gap there, huh?
**Hanson Ho** 41:12 Yeah, the tests would mostly for, modules that have Apple-specific.
Export persistence, there's, an Android or Apple test.
**Jason Plumb** 41:26 In where?
**Hanson Ho** 41:27 Under exports dash persistence, there's an Apple test.
**Jason Plumb** 41:32 Okay.
That's probably just for exporter stuff.
**Hanson Ho** 41:36 Yeah.
Because not every module has an Apple-specific code, a lot of it is just, like, Kotlin.
**Jason Plumb** 41:47 And then, I guess we're relying on KMP just to do its thing, and we're assuming that if it compiles, it'll run.
**Hanson Ho** 41:55 Yeah.
**Jason Plumb** 41:58 Okay?
Yeah.
**Hanson Ho** 42:01 because there's… Well, I mean, this is where the integration tests would be nice, where we're…
**Jason Plumb** 42:06 Totally.
**Hanson Ho** 42:07 So we should probably… we can probably add a task to, the testing, milestone, for, end-to-end integration tests, for, well, or… and integration tests for, the non, Kotlin platforms, or sorry, non-Android platforms.
**Jason Plumb** 42:27 I think that's worth doing.
Like, having… having, just a sample app, like a test app that… Gets created with a resource and generates metrics, traces, and logs, and maybe does a little bit of propagation?
and then we, like, verify that the data looks the way that we think it does on every platform, that would be killer, but that's a lot of work, right? Like, that's… Maybe?
We're close, it sounds like.
**Hanson Ho** 43:00 Like, common test here, like, I'm… like, if you go up there, I think there's… there might be, like, an android.
**Jason Plumb** 43:08 To testing… Or common.
**Hanson Ho** 43:13 Oh, no, just where you were before, but there's a parallel project?
**Jason Plumb** 43:16 in… Here?
**Hanson Ho** 43:19 A smoke test source.
**Jason Plumb** 43:21 Okay.
JVM stuff.
Yeah…
**Hanson Ho** 43:27 Open those came out smoke tests, so…
**Jason Plumb** 43:33 This is cool.
Yep, so fire up an OTLP server, throw some traces and some logs at it. We don't have metrics built yet.
And then… make sure we can get a spam back, and a log back. That's cool.
**Hanson Ho** 43:52 Like, none of this should be, none of this should be… super, like, Android JVM-specific. So.
**Jason Plumb** 44:02 But this probably exists because we want to run it on the JVM?
**Hanson Ho** 44:05 Yeah.
**Jason Plumb** 44:07 Which means that, is there, like, build stuff that handles this, then?
Like, how do we specify? How do we make sure?
I don't know.
I don't know how this stuff is wired.
**Hanson Ho** 44:22 Yeah.
**Jason Plumb** 44:23 That sounds like a problem for future Jason to understand.
And not mourning Jason to understand.
**Hanson Ho** 44:29 I would just create an issue for now, like… Chances are, it just needs a bit of work, because in theory, there is a sample app, and at one point, it would have worked. So, if anything about it not working, it would be, you know, something has changed. So, I would imagine… Cool. Getting that working is hopefully not that bad.
I'll create an issue in the testing thing.
**Jason Plumb** 44:59 Thank you.
Alright, let's do it again next Monday.
**Hanson Ho** 45:06 Alright.
**Jason Plumb** 45:07 Bye, everyone.
