SIG: Java Declarative Configuration
Date: 2026-01-08
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/0VtcY_38CXKe61_Vxv75mjVLKNGdWkfsLBfniiROI-9UdDMY0F9IWykTiluBD8MU.YJTvAHN-n-tXEI3i
============================================================

## Zoom Recording Transcript

GZ Gregor Zeitlinger 00:02:37 Hello?
What meeting did you expect?
Trask Stalnaker 00:12:37 Hey, Gregor!
GZ Gregor Zeitlinger 00:12:44 Happy New Year, Trask!
Trask Stalnaker 00:12:47 Same to you.
Ugh, I slept in today.
GZ Gregor Zeitlinger 00:13:00 Haha.
Trask Stalnaker 00:13:00 So, barely, barely at my desk here.
But I'm ready for this.
GZ Gregor Zeitlinger 00:13:08 So you're starting with the best part in the day.
Trask Stalnaker 00:13:14 8 AM meetings, always the best part of the day.
GZ Gregor Zeitlinger 00:13:21 Did you have, fun over… the… Over the end of the year, using, declarative configuration.
Trask Stalnaker 00:13:33 Oh, yeah, yeah, no, I'm… I'm really excited about declarative configuration.
Yeah, I'm hoping that we can get that in… there's a bunch of things, for 3O that are on my mind right now. I want to get the database stabilization. Rpc is coming quickly.
We're almost done with the RPC semconst, so might be able to, get that, and then declarative configuration.
Hoping that we can get that.
stable.
GZ Gregor Zeitlinger 00:14:19 What time do you have in mind for 3?
Trask Stalnaker 00:14:23 Early this year, like… Hoping… hoping… I mean, basically, it depends on how long it takes us to get… Those… things in, especially, I mean, database is the big one.
But… It's flexible, but if we could do it, like, in April, that would be… Amazing.
GZ Gregor Zeitlinger 00:14:51 Yeah, we are just, starting to lay out what we want to focus on, so… Jay and me.
Basically, for this year. So, if you have one area to pick.
Then I will discuss if we can work on that.
So, for my part, once declarative configuration is done.
Jay is probably, still, also focused on the, metadata stuff, but, if you pick one, then, there's a good chance that I can, get some room. So, you can think about that.
Okay.
Trask Stalnaker 00:15:34 Awesome.
GZ Gregor Zeitlinger 00:15:36 Okay, then, we have, I think two areas. One is, SDK, and the other one is instrumentation. I asked Jack if he can join, but maybe he did not see my message yet.
So I guess, makes more sense that we talk about the instrumentation part, then.
Trask Stalnaker 00:16:04 Yeah, we can sync with him in the… Regular.
GZ Gregor Zeitlinger 00:16:09 Jay just joined. Hi, Jay!
Trask Stalnaker 00:16:13 Hey, guys.
Jay DeLuca 00:16:14 Happy New Year.
GZ Gregor Zeitlinger 00:16:16 Yeah, Trask just said that he wants to do 3.0, like, sometime in spring, I would say, and I told him that if he has one thing on the wishlist, an area where we can help, then we can probably make some room in our team planning.
Trask Stalnaker 00:16:38 I would say, like, yeah, I mean, just in general, like, we have that 3-0 board, right? We've got… The big ones, of course, are database.
I was telling Gregor, RPC SEMCOM is… we've almost finished that, so I think that will be… We'll be able to stabilize that.
Declarative configuration.
But I know we've got a lot of other, kind of, smaller things on the board already that, would be great, that we wanted to potentially wait for, Breaking for the major version.
Jay DeLuca 00:17:16 There's involved.
GZ Gregor Zeitlinger 00:17:19 Yep.
Jay DeLuca 00:17:23 Alright, what's left for database?
Trask Stalnaker 00:17:28 I've got an issue open for that.
Jay DeLuca 00:17:35 Or… I'm sorry, we don't have to talk about that in this meeting. We have other declarative.
Trask Stalnaker 00:17:38 Yeah, just pull up the… pull up the database, Stability tracking issue.
And it's got… a few… remaining…
Jay DeLuca 00:17:56 Okay.
Trask Stalnaker 00:17:57 tasks.
Jay DeLuca 00:18:02 Cool.
Trask Stalnaker 00:18:04 All right, Gregor, you're up. What do we want to talk about? Declar… Instrumentation, declarative config? I saw you got a bunch of PRs up. I will, I mean, we can look…
GZ Gregor Zeitlinger 00:18:16 Yeah, I think we can look at those PRs, and while we are looking at them.
you can check whether this is complete in terms of the big PR that you did. From what I understand, there's nothing missing, so if you see something that is not covered.
Then, yeah, just point it out or create an issue so that I can think about that.
Trask Stalnaker 00:18:43 Yeah, did you see my list down here?
GZ Gregor Zeitlinger 00:18:49 Yep. I looked at that.
Trask Stalnaker 00:18:51 Awesome, awesome.
Cool. I just… I had added it late recently, and it was kind of buried. I wasn't sure if you'd seen it.
Cool, yeah, let's just, let's… go through them. Some of them are probably… Yep.
GZ Gregor Zeitlinger 00:19:08 There are not so many, so we can just go, in any order.
Trask Stalnaker 00:19:13 Cool. Last usage… So… Yes, this was that painful.
Guy.
GZ Gregor Zeitlinger 00:19:26 Yeah, I added that today.
Yeah, this, is different here because of… Because, there's a special mapping in long for discovery delay.
Trask Stalnaker 00:19:47 Yeah.
Okay.
And this is… Just a restructuring, and then a special case for… Oh, the duration…
GZ Gregor Zeitlinger 00:20:05 Yep, this is… this is the only place where duration is actually used. I… I checked… I double-checked that part.
And I'm also falling back to this, thing from the SDK, because it's actually used in our tests, and… It would be a breaking change, and it was easy to edit here.
Trask Stalnaker 00:20:26 Yeah.
And so this whole thing… This whole class is only used when we are bridging, so…
GZ Gregor Zeitlinger 00:20:39 Yeah, that's exactly what we want.
Trask Stalnaker 00:20:42 Awesome, awesome, yes. Okay, oh yes, I see, and we have that special case. Okay. Oh, nice, nice, yes.
Oh, and that was the only place we used duration, okay.
GZ Gregor Zeitlinger 00:20:57 Right.
Trask Stalnaker 00:21:00 And so… .
GZ Gregor Zeitlinger 00:21:10 Oh, there's an… it's… that's a nice trick. You… you… you check the… you check the viewed… buttons.
Trask Stalnaker 00:21:16 Yeah.
Yeah, yeah, yeah.
Yeah, yeah, it was super useful for, Then, you know, when the scroll bar is, like…
GZ Gregor Zeitlinger 00:21:29 Right.
Trask Stalnaker 00:21:30 Super, super long.
So… config delay… Okay…
GZ Gregor Zeitlinger 00:21:44 Yeah, this has become easier, because all the… Heavy lifting is in the… in this part here in the bridge.
Trask Stalnaker 00:21:52 I see, so duration… okay, so we're always returning millis… yes, this makes sense to me. We're always returning millis here.
But we're reading, we're converting internally. Okay.
Nice, so this is always… annuities. And now, yes, yes, it's not duration anymore.
Maybe carry this comment over… Yeah… I'll… okay… Last season. Okay, okay, so this is… Machine… Enabled.
This is… Instrumentation mode… Common, that's the fallback.
Right.
And if not enabled… okay.
for agent… And so before agent… Okay, after agent, we definitely can use declarative config.
Oh, okay, this… we do have the SDK here, so yeah, that's…
GZ Gregor Zeitlinger 00:23:46 Yeah, that's basically what this PR is about, all the usages we're, we're passing around the auto-configured SDK.
Trask Stalnaker 00:24:03 Do we… So, before li- before Agent Listener… Oh, okay, so we do want the whole auto-configured OpenTelemetry SDK passing around here, because we probably use it for resources or something else also.
I was just wondering if we'd just… because we could also just use global Here.
GZ Gregor Zeitlinger 00:24:33 That's a good point, yeah. Add it as a comment. I'll check out if that is possible.
Trask Stalnaker 00:24:52 Package editor… Let's see, runtime telemetry, config, boolean… I kinda like the convention… Where config is this thing.
And then this would be GET… Package… emitter… I think that.
GZ Gregor Zeitlinger 00:25:23 I think… That is not, the majority.
right now.
Trask Stalnaker 00:25:31 Hmm.
GZ Gregor Zeitlinger 00:25:32 So, in most places I've seen config is the, module.
Oh, no, this is what you mean, right?
Trask Stalnaker 00:25:41 Right, right.
GZ Gregor Zeitlinger 00:25:41 Okay, then you're right, okay, got it.
Trask Stalnaker 00:25:58 package.
Jars per second… Inc. 10… Hotel Instrumentation… Config party supplier tests.
So what's… Can you give me just a brief explanation what we added, why these… why we added more new tests?
GZ Gregor Zeitlinger 00:26:36 You actually added that, but the reason is that it tests the base behavior without the override.
Trask Stalnaker 00:26:46 S space behavior…
GZ Gregor Zeitlinger 00:26:50 Yeah, it's easier to see if you see the whole class, so one has a, I think one is setting it to true, and the other one is setting it to false.
Trask Stalnaker 00:27:03 Is this related to… How is this related to this PR?
Is this, like, using config properties or something that we're trying to get rid of?
GZ Gregor Zeitlinger 00:27:23 I… I… I don't know. You added that I'm… I did not…
Trask Stalnaker 00:27:27 Okay. Not answer that.
Okay. Let's… And then this one… Auto-configure SDK… Probably, getting rid of… Looks like probably getting rid of auto-config util, maybe?
GZ Gregor Zeitlinger 00:28:07 Yeah, okay, I'll check.
Trask Stalnaker 00:28:09 Yeah, cause then, I can think more about that in that PR. Cool.
GZ Gregor Zeitlinger 00:28:34 Yeah, this is also, PR that you started, and I basically added my, review comments, and then also, comments from, Laurie from today.
Trask Stalnaker 00:28:48 Oh, cool, I miss… let's… let me look at Lori's comments.
Oh, Laura's comments were on this PR.
GZ Gregor Zeitlinger 00:28:58 Yeah, they're… yeah.
My comments were on the old PR.
Trask Stalnaker 00:29:05 Yes, yes.
GZ Gregor Zeitlinger 00:29:16 Yeah, this is Deny Unsafe, got me, On the wrong path until, Laurie really explained what it's about. And I think you also, got confused, because you deleted the method. I put it back and just changed the comment.
Trask Stalnaker 00:29:35 Okay, okay.
Oh… Okay, yes, yes, okay, I think I understand.
Unspread operation…
GZ Gregor Zeitlinger 00:29:54 Yeah, Laurie found a neat way to avoid the exception, but still have the same fallback behavior.
Trask Stalnaker 00:30:04 Okay, great. Okay, we'll look at that.
So let's start… There, with that fallback…
GZ Gregor Zeitlinger 00:30:24 You can also look at the individual PRs if you find that easier.
Trask Stalnaker 00:30:31 individual commits.
GZ Gregor Zeitlinger 00:30:32 Yeah, yeah, because then you don't have to review your own comments.
Trask Stalnaker 00:30:38 Good point. it's not bad to review my own.
Code.
Especially that… that big PR was mostly vibe-coded.
GZ Gregor Zeitlinger 00:30:54 What did you actually use for that?
Trask Stalnaker 00:30:59 I mean, I use Copilot for everything, but… Like, not… obviously not all in one batch, it was way too big, like, a lot of, kind of, both. Massaging it, telling it what to do.
GZ Gregor Zeitlinger 00:31:13 But what do you mean by co-pilot? Is it a co-pilot in GitHub, or…
Trask Stalnaker 00:31:18 Oh, in VS Code.
GZ Gregor Zeitlinger 00:31:21 And what model do you use?
Trask Stalnaker 00:31:24 Oh, for this, so… I… did I… was Opus out when I did this?
GZ Gregor Zeitlinger 00:31:36 Hmm.
Trask Stalnaker 00:31:36 I think so. When… when an Opus is more expensive, but, so I reserve it for harder tasks, but, it is very… it is worth it for the more important things.
otherwise, I use Sonnet 4-5.
GZ Gregor Zeitlinger 00:31:59 Okay.
Trask Stalnaker 00:32:04 So we've got default… enabled.
Okay, and this caused… Default, let's cause this…
GZ Gregor Zeitlinger 00:32:26 Yeah, unless it's overwritten.
Trask Stalnaker 00:32:30 Unless it's overwritten…
GZ Gregor Zeitlinger 00:32:33 With a deprecated module, that's the idea.
Trask Stalnaker 00:32:38 Okay, and if the… If, somebody… because the deprecat… the… subclasses often call super.
So they would get this and this, but this should map… To this anyways, right?
GZ Gregor Zeitlinger 00:32:59 Correct.
Trask Stalnaker 00:33:06 Seems easy.
GZ Gregor Zeitlinger 00:33:09 Yeah, once you figure it out.
Trask Stalnaker 00:33:10 I'm sure I was, like… I'm sure I tried, like, 5 different ways to make this work.
Trash has loaded before… Experimental config… Okay, okay.
Nicar, yes… Oh, okay, I see. So we are calling… yes, we're calling the deprecated one.
And… Okay, got it.
Calling the deprecated one.
Yes.
That's fine.
Default enabled… Yes.
Actually, I think possibly this should be, one of our, testing… What is our… convention for testing… Only… Properties.
Jay DeLuca 00:34:47 But I've seen any convention like that.
GZ Gregor Zeitlinger 00:34:51 Yeah, I think it's not a convention, but we have some…
Trask Stalnaker 00:34:54 One.
Oh, yeah, I wonder what I thought there was… A Teltas… hmm… The testing… Denial…
GZ Gregor Zeitlinger 00:35:12 Java agent testing, that's what it is.
Trask Stalnaker 00:35:15 I'll tell Java agent, take… thank you, Java Agent testing…
GZ Gregor Zeitlinger 00:35:19 And I think there's no equivalent for declarative configuration.
Trask Stalnaker 00:35:25 Well, it doesn't need to be, right? We don't even want… we don't even want it for declarative configuration, because it's only for our… test RCI usage.
GZ Gregor Zeitlinger 00:35:37 Yeah, okay, then it makes sense to do it that way.
Trask Stalnaker 00:36:03 Okay, and so now we are just in.
equals… So… Why can't we call super?
Yeah.
GZ Gregor Zeitlinger 00:36:30 Because it was just so easy to have this inlined.
Maybe we could, I… I just thought it would be easier to do it this way.
But… I don't really care.
I actually don't like inheritance. That's probably why I did it that way.
Trask Stalnaker 00:36:53 Default enabled… Okay.
Yeah, I… I think I would, and I'm hoping… Colleen's super… Should work here… yeah, yeah.
GZ Gregor Zeitlinger 00:37:20 Could it work?
I guess it would work. Why did you remove it in the first place?
Trask Stalnaker 00:37:44 Okay, because I had that copy super default enabled, do you remember that?
GZ Gregor Zeitlinger 00:37:51 Right.
Trask Stalnaker 00:37:52 Because of the exception that was being thrown, like.
It was part of my twisted… Yeah.
GZ Gregor Zeitlinger 00:38:05 Yeah, okay, got it. Yeah, then… that makes sense to restore that behavior.
Trask Stalnaker 00:38:10 Yeah.
GZ Gregor Zeitlinger 00:38:15 Hey, don't… you don't need to add it in every OK.
Trask Stalnaker 00:38:17 No, no, I won't. I'm just checking if that's the only.
GZ Gregor Zeitlinger 00:38:23 Oh, they're more…
Trask Stalnaker 00:38:26 Yeah.
Yes.
Yes.
Yeah.
Yes.
Okay, right, these are all the same… Logging… Okay, great.
Getting straight agent logging, okay.
Alright, great.
Okay, we looked at that, we looked at that.
This… this… Line config usage… Right, right. Here you're doing that config equals module.
Yep, I like that.
I don't… Config modules… So, maybe… Here, if we want to follow the same, that would be roleconfig.get.
End user…
GZ Gregor Zeitlinger 00:40:27 Oh, so end user, it should be called end user.
Trask Stalnaker 00:40:33 Oh, you want to reuse that, you want end user config here?
GZ Gregor Zeitlinger 00:40:39 Yeah.
Trask Stalnaker 00:40:40 Okay, that's fine.
Cool.
Consistent early initiate.
Yeah.
GZ Gregor Zeitlinger 00:41:07 Okay, there's also a PR that you, created, and then you closed it, But it wasn't really clear to me why you closed it, because I only had some comments on it, and nothing major.
Trask Stalnaker 00:41:22 I was… struggling with what to do, because I… right, I sent that other PR reading from the YAML, trying to, like… I think the early… agent, config, It's gonna be confusing.
I think to have Properties that you can't set via declarative config?
GZ Gregor Zeitlinger 00:41:52 Right, yeah. I spent a long time with Laurie trying to figure out if we could get it to work, and Eventually, we gave up.
Trask Stalnaker 00:42:02 Yeah.
Yeah, so I support giving up for now. I think that we could… There might be ways to reshuffle some of the startup sequence.
I think Hotel J… yeah.
OTel Java Agent Enabled is the one that I know that we can't get into declarative Config.
Because, like, you actually want… don't want to do anything if that one is set.
But the other ones, like logging and extension, and debug… I feel like we could… Possibly shuffle those around.
GZ Gregor Zeitlinger 00:42:45 Oh, the… no… Reason is straightforward, laurie explained that reading YAML with Jackson is the problem.
Once, before you enter, I think, the, some class path, where it's safe to do so. And everything that is loaded before, cannot, use, difficult libraries, and YAML libraries are difficult.
Trask Stalnaker 00:43:17 Yeah.
GZ Gregor Zeitlinger 00:43:18 User also might have them, and then you pollute their class paths.
Trask Stalnaker 00:43:23 So the… the possibility would be to move… so what we need to do is we have to install those, virtual field Instrument… Bike code instrumentation.
early. So that… that's… the problem is that there's some executors and runnable things in the Java library, in the Java SDK.
which, we want to add virtual fields to the.
And… Once those are loaded, you… we can't add fields to classes?
We can re-transform classes, but we can't change their structure by adding a field.
And, we have a fallback mechanism of you having a weak map of the runnable to that field thing.
In cases where we can't… ad where we're stuck in that case. That's why the tests still passed.
on my PR.
GZ Gregor Zeitlinger 00:44:35 Hmm, okay.
Trask Stalnaker 00:44:37 But they were using this low performance… lower performance weak cache map instead of, embedding… being able to embed the virtual field directly inside of the class.
GZ Gregor Zeitlinger 00:44:56 Okay.
Trask Stalnaker 00:44:58 And so the… the possibility there… is for… And I looked, I spent a little bit of time, and it's not… it's not easy, or if I would have done it, I would have tried it, is doing that piece earlier, or delaying the parts of extension… creating the extension class loader, and loading the logging, and those things until after that's done.
And one of the main problems is the logging.
Right, we want to set up logging early, and it means that anything we do before we set up logging, we have to, Log to memory, and then emit those later on, after we set up logging?
So, so it's all a bit painful, and it might require, some loss of functionality, even. Like, right now, the logging customizer is… you can have… an extension?
With one of those logging customizers.
So you can provide your own logging kind of bridge?
But I honestly don't think any… I mean, anybody's doing that. I think that that's only being done by distros.
So I think that loss of functionality could be acceptable.
I don't know. I'll open an issue to track it, but I agree with moving forward without that.
Let me make a note to myself… Okay, earlier, great job… Okay, so what are we doing here? The goal here is to limit that, make it clearer.
So… So another option here… Would be to… Populate declarative config… populate the YAML… With these values from the system properties so that we can still read them via declarative config.
API…
GZ Gregor Zeitlinger 00:48:05 Yeah, the question is whether this is more or less confusing.
Trask Stalnaker 00:48:11 Yeah, I agree.
So I think this is a good step. This makes it… Clear… What? Yeah. I think this is a good step.
So, right, we're not passing it around anymore.
Because… We want to be able to access it statically from a few places anyways, so may as well access it statically everywhere.
GZ Gregor Zeitlinger 00:48:58 Pride.
Trask Stalnaker 00:49:21 Yeah, this is an example of… Can't we have to cache the log messages and log them later?
I think I removed this in a different PR.
I don't know why it's showing as a diff here. Maybe it just needed to be rebased, probably. It's fine.
GZ Gregor Zeitlinger 00:49:51 Yeah, there are some merge conflicts between those PRs.
I'm aware of that already.
Trask Stalnaker 00:49:57 Okay.
Extension… And this is… Do we care about… Breaking change here…
GZ Gregor Zeitlinger 00:50:23 It's in tooling, pooling is not an, is not a library.
Trask Stalnaker 00:50:33 Yeah, I think some distros might be using it, but I don't really care if we break distros, because they have to update. They are synced to specific versions.
Anyways…
GZ Gregor Zeitlinger 00:50:48 That's… that's why we have the Java Agent Extension API.
But that's not in there, it's in tooling.
Trask Stalnaker 00:50:59 Sorry, say that? Say that again?
GZ Gregor Zeitlinger 00:51:02 This class is in tooling, and for, Bistros, we have the Java Agent Extension API, Module.
Trask Stalnaker 00:51:12 Yeah, I'm pretty sure we're using this in our distro.
Let me see… Yeah, we are. But… It doesn't matter if we break distros, because they have to up… it's… the… Extensions, it matters if we break, because they're independent from the Java agent release.
GZ Gregor Zeitlinger 00:51:41 Why are we publishing that? Okay, that is confusing me.
Trask Stalnaker 00:51:45 We've got a… yeah, we've got a couple in things… I would consider it an internal… Yes.
Good break, just does… That's… Okay. I'm not even gonna flag it. I think it's fine.
We use it, because we use LogBack. We have a bridge to LogBack instead of SLF for JSimple.
GZ Gregor Zeitlinger 00:52:26 Yeah, I'm only confused that this class is not in the extension API.
Which sounds more like it would be used.
for that purpose.
Trask Stalnaker 00:52:44 Yeah, I think maybe we just decided… I mean, and I think it's actually a good thing it's not exposed to extensions, because, like I was saying, there was, earlier that… There's some, Currently, we have to set up the… we set up the extension loader first, and then we load the logging implementation.
GZ Gregor Zeitlinger 00:53:04 Oh, okay, yeah.
Trask Stalnaker 00:53:06 It's a special case.
It's… actually kind of… good, if that's… we break that, I'd prefer to load the logging Without having to load the extension loader first.
Too, early, yes?
Yeah, I think this is fine. Because we weren't using it I mean, it's a little tricky now, we're kinda… now we are using this from… instrumentation.
Right, this makes it a little… So we are using agent tooling from… instrumentations.
GZ Gregor Zeitlinger 00:54:41 Okay.
Yep, that's do it.
Trask Stalnaker 00:54:43 So that starts to make that… But…
Jay DeLuca 00:54:48 Is this… is this the only one, though? Because I think when I… when I was doing the metadata for this module, I think Lori called out that, like, this particular config is… really expect… Like, a user on?
Trask Stalnaker 00:55:12 Oh, this Czech class, anyways.
Yeah… I'm just gonna flag it, I wanna think about this a little bit more.
GZ Gregor Zeitlinger 00:56:10 Would it be better if we pass in the instance in that case, or is it… Something else.
Trask Stalnaker 00:56:16 You can't… you can't pass in the instance here.
Because it's.
GZ Gregor Zeitlinger 00:56:23 Right.
We could keep the, the old version of using config property util.
If needed.
Trask Stalnaker 00:56:45 Yeah, I don't feel like that helps us, though.
To keep the odd.
Just kind of hides that dependency.
Let's just look over the rest here.
And then we can… break.
And I'll… re… I'll go back through it.
short logging in.
Okay, yes, we're here… Extension class loader… Oh yes, that's where we were.
Yeah, I think it's… Find two… because potentially somebody could… oh, no, nobody could have been using that, because we had no static access to it.
GZ Gregor Zeitlinger 00:58:19 You would need to call create first.
Trask Stalnaker 00:58:22 Create.
Yeah.
That's okay.
Jay DeLuca 00:58:27 Do you think it's redundant to have OTEL Java Agent in the… the names?
The property names when it's in the class name.
I guess the agent config, is that implicit?
Trask Stalnaker 00:58:42 Yeah, it's a good…
GZ Gregor Zeitlinger 00:58:54 Yeah, good idea.
Does not need to reflect the path exactly.
Yeah, same for the others.
Trask Stalnaker 00:59:16 Yeah.
Mr. Ching.
These are, yes, tests.
Okay.
Alright.
Cool, awesome. Looked like most of those were pretty simple updates, and then I will take a look again and hopefully merge, unless I missed stuff the first time.
GZ Gregor Zeitlinger 00:59:48 Yeah, I think the only one left is about the instrumentation mode enum, and… Maybe if we have time in the other meeting, we can discuss with Laurie, because he also… I think he also has an opinion there.
Trask Stalnaker 01:00:01 Yeah, I… I wasn't… Yeah, this is… Yeah, let's discuss, cause, if we're going to… change, this is kind of connected to… did I not… was it a different one I commented on?
I guess it was.
GZ Gregor Zeitlinger 01:00:24 There's one called instrumentation Mode Enum.
Trask Stalnaker 01:00:27 Which sounds similar. Oh, sorry, I opened the wrong one. Yes, instrumentation. Enum.
GZ Gregor Zeitlinger 01:00:36 This is… it was just intended to be a cleanup, but then it…
Trask Stalnaker 01:00:39 Ha ha ha ha.
GZ Gregor Zeitlinger 01:00:40 Awesome.
Trask Stalnaker 01:00:42 Yeah, yeah, so part of… Like, I'm not sure that… do we really need this in Spring Starter, for example?
And could we just scope it to the Java agent?
Because right now, it had to go into the incubator.
API, I mean, the instrumentation API, which kind of makes it seem like Anyway, it connects to the whole native stuff, and this other discussion.
GZ Gregor Zeitlinger 01:01:12 No, it's… I think that's… that's two different questions.
Native is not the same as Spring Boot, because Spring also wants to have the possibility to have everything disabled.
Or at least that's what I think you want to have.
Trask Stalnaker 01:01:32 Let's… Add this to the, next meeting agenda.
GZ Gregor Zeitlinger 01:01:36 Yeah, okay.
Trask Stalnaker 01:01:37 Alright, see you there.
GZ Gregor Zeitlinger 01:01:39 See you there.
Jay DeLuca 01:01:40 Right.
