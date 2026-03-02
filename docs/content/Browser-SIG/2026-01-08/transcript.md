SIG: Browser SIG
Date: 2026-01-08
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze** 00:40 Hey, what's up?
**Benoit** 00:45 Hello?
**Wolfgang Therrien** 00:45 Whoa!
How's everybody doing? Happy New Year!
**Jared Freeze** 00:51 Yeah, Happy New Year!
Can you… can you hear the birds here?
**Wolfgang Therrien** 00:57 No, I can't.
**Jared Freeze** 00:59 Okay, good.
I started… I started feeding the crows, and they're going ballistic, so… Hey, Ted.
**Ted Young** 01:15 Hello, hello!
Feeding the crows.
Dangerous game
Once you get wrapped up in Crowbiz, you don't know where it's gonna end.
**Jared Freeze** 01:29 Well, they have started attacking my enemies, so that's all I really wanted.
**Ted Young** 01:33 Yeah.
Right. Then they bring you shiny objects, then they start bringing money, then they start bringing you fingers, and then it's just really…
Gone too far.
You can't say no to them at that point, they know who you are.
**Jared Freeze** 01:50 They, they're gonna bring beads.
**Ted Young** 01:56 Cool.
**Wolfgang Therrien** 01:57 Do, do folks mind if I take, notes with the transcribe… transcriber?
**Ted Young** 02:04 I don't mind.
**Wolfgang Therrien** 02:06 Thanks.
**Ted Young** 02:08 Yeah.
**Jared Freeze** 02:10 It's already recorded, right? So…
**Ted Young** 02:12 It's already recorded. We've been having… we've at least had a spate of problems of, like, weird AI agents just, like…
like, joining meetings, like, but not having a human associated with it. It's like, someone was too lazy to go to the meeting, they're like, I'm gonna send my agent on my behalf, or…
Or an agent company was like, we're just gonna, like, have this thing join a bunch of Zoom meetings. It got a little weird for a while, so we kinda, like…
**Wolfgang Therrien** 02:38 That's wild.
**Ted Young** 02:39 Our default policy is, like, no AI recording agent things unless there's, like, a person, and it's obvious why it's happening. Because otherwise, it's just weird.
**Wolfgang Therrien** 02:50 Yeah, for sure.
**Jared Freeze** 02:53 I like… I like that policy.
Yeah, there's enough robots in my life.
**Ted Young** 03:00 Yeah.
Humans have this quality where if we know why the camera's on, we're usually fine with it, but if a camera's just recording us, and we don't know why it's there, that's very weird.
Yeah.
Hello!
Martin, would you like to run the meeting today?
Oh, I think you might be muted, Martin.
**Martin Kuba** 03:35 Oh, sorry, because I've been talking this whole time. I said Happy New Year to everyone.
**Jared Freeze** 03:42 Happy New Year!
**Wolfgang Therrien** 03:43 Happy New Year.
**Marco Schäfer** 03:45 Yeah. Okay.
**Martin Kuba** 03:47 Alright, let me, share my screen.
**David Luna Bistuer** 03:51 Hey, everyone.
**Martin Kuba** 04:06 Okay, so I, I, I do have…
I do have a couple of things on the agenda that I wanted to just, bring up, one for discussion, for discussion.
If anyone has anything else, please add it.
The first thing that I have is,
I just wanted to get a sense of…
how far we are from being able to do a release, like, we have…
We have one existing package.
For instrumentation for the user actions.
And, like, there is another PR right now that's for another instrumentation that's gonna be probably ready soon.
I'm not sure, like, how far we are from this.
**Ted Young** 04:52 I think you might be sharing the wrong window, by the way.
**Martin Kuba** 04:55 Am I?
Shoot.
Probably don't share the whole screen, do I? Screen?
Are you… can you see the… the documents?
Yeah.
**Ted Young** 05:29 Yeah.
**Martin Kuba** 05:30 Okay, cool.
Yeah, so I just wanted to bring this up for discussion, so if… if…
Jared, have you thought about this at all?
**Jared Freeze** 05:39 Yeah, definitely. So, I know, with all the NPM changes, I actually don't know what the new process is, because they had this sort of, like, short-lived… or sorry, long-lived token system. I definitely need education here,
as far as, like, who's allowed to publish, and when that happens, or whatever, I don't know if it falls to JS maintainers, but I think before we have that discussion, it's like, we need to figure out how to version on the… on publish.
Because I want to make sure…
I mean, we can do it manually, maybe the first time, or second, or even third, something like that, but figuring out that workflow, I actually have not investigated that from JS repo, so I want to make sure that
we… all agree on what that should be, or where we start. I think 0.1.0 is pretty standard, so…
Maybe we take that to Slack?
If I can jump to the next one, so combining those two, I completely agree. I think that should get refactored before we publish, because WebUutil's going out and then disappearing, and then webcommon existing, and having, like, harsh trace parents or whatever's in it.
You know, we should deal with them, then publish.
**Joaquín Díaz** 06:51 I think what I did with usual stadia was to have it, like, privately for…
the web browser repo.
So it's not actually the same. I don't think… I don't know, this webcommon something that you can use as a user, and there are utilities there that you can import on your project?
**Jared Freeze** 07:16 Yeah, I think.
**Joaquín Díaz** 07:17 Explain.
**Jared Freeze** 07:17 I think it's public. Yeah, I think it's public, so I think we should take the utils, move the functionality, and then bring the whole thing over.
When we need to do that.
**Joaquín Díaz** 07:29 the thing is, the stuff that is now on WebUTILs is just utils that the instrumentation can use themselves, but…
I don't think users will ever need to import that on their own.
If they are doing something with hotel.
that is what it… what is today, right now. Like, that is shared code for share… like, shared instrumentation code that you may use.
if you're writing instrumentation on this repo, but I don't think what it is right now is useful for someone that is not writing code on this repo, that is why
I think there are different packages.
But, again, that is what it is right now. I don't know if we are expecting to add more stuff there that might be useful to export and publish, for instance.
**Martin Kuba** 08:17 But the package would still be published?
Done.
**Joaquín Díaz** 08:21 I, I… it… that's… I mean…
I guess it needs to be published if it is a dependency of the other packages.
But if that's an issue, then we can just… and, like, bundle it together.
Yeah, I thought a lot about that.
**Jared Freeze** 08:43 You'd have to inline the functions if it's private.
So I do think it should be public, and if it is public, I think there's enough overlap with Webcom, and we may want to combine those. That's… that's my feeling about it, but… I think it's okay…
I think it's better to be consistent about everything being public, and not having to think about what is included in line and what's not.
**Joaquín Díaz** 09:06 Yes, sure, that makes… that's fine.
Just wanted to clarify that, like… but I'm okay if it is public or not, just…
**Jared Freeze** 09:15 Wanted to be clear about the reason on…
**Joaquín Díaz** 09:17 Why it is there, but yeah, we can keep adding stuff, and eventually we'll say, now we publish it, or we can publish it now, so it's fine.
**Martin Kuba** 09:30 Yeah, I just, I just think, like, that having, having, like, two packages that are kind of basically similar.
Like, that might be confusing, like, to…
**Joaquín Díaz** 09:39 Hmm.
**Martin Kuba** 09:40 But you just like to know, like, which one… which ones is used for what.
So I can, I want to create some tickets to start moving packages over from JS and JSContrypt over here, but, like, before we start doing that, I wanted to discuss the release workflow, because, like, once we move things over here, like, we want to be able to
To do release, obviously, so… For existing packages.
**Joaquín Díaz** 10:08 So I guess the biggest discussion, as Joe was saying, is the versioning, right?
Actually, publishing it, though.
a hard thing to, like, I think it's something that we can copy from JS.
But, versioning, I think… The last time we discussed this, we said that It is okay to use…
Whatever version we want for instrumentation only.
like, the only thing that has so much is the API, right?
So… I guess, for now, since we only have instrumentation, we can just decide what makes sense to us.
**Jared Freeze** 10:48 I looked at the docs, and Ted, correct me if I'm wrong, but it said there'll never be a 2.0 for API.
**Ted Young** 10:57 Hopefully…
The thing about API packages, the instrumentation API package specifically, is that's the cross-cutting concern that goes everywhere, right? That's the thing that there's, like, a million dependencies on that thing.
And they're all transitive dependencies, right? Like, it's not that I depend on OTEL, it's I depend on some library that depends on OTEL. And if you have some libraries in your app that depend on OTEL 1.0, and some that depend on OTEL API 2.0,
That's an unfixable dependency conflict.
So, we don't really want to ever do, like, a 2.0, because in most languages, that would just be a mess. Even if we did make a new metrics API or a new tracing API, it would probably be a new interface next to it, and we would, like, deprecate the old one.
Rather than a breaking 2.0 change, just because of…
how dependency management works when you're cross-cutting concern. Seems like we would… it would be, like, a huge act of self-immolation if we did that in most languages. So that's… that's the reason.
But for the rest of the stuff, obviously, we're more lax. It's just that API package that goes everywhere.
**Jared Freeze** 12:17 So how does everyone feel about what's in this repo, just matching JS?
I mean, even though it's, like, they don't actually go out together, I mean, we could just start with…
You know, 209, or whatever.
**Joaquín Díaz** 12:31 I think we'd like to avoid that, right? It's hard to follow, like.
When there are breaking changes, it's hard to know, because there is always a minor patch update.
**Ted Young** 12:44 Is it not the same API package?
In both cases.
It is, right?
We haven't forked from them yet.
So yeah, we should just use the latest, right?
**Jared Freeze** 12:59 I think so, yeah.
**Daniel Dyla (Dynatrace)** 13:01 I don't think that was what he was getting at, though. I think, what he was talking about was the version numbers of, like, all the SDK packages.
**Ted Young** 13:10 Oh, the SDKs. Okay, my bad.
**Daniel Dyla (Dynatrace)** 13:13 like, matching the version numbers, essentially releasing with the same version as what the core JS repo is releasing as, or restarting with a new numbering scheme.
**Joaquín Díaz** 13:25 Yeah, I think… I think for these recommendations, we should just restart.
**Daniel Dyla (Dynatrace)** 13:31 the answer.
**Joaquín Díaz** 13:31 Shouldn't know.
**Daniel Dyla (Dynatrace)** 13:33 I'm sorry, I didn't mean to cut you off. The instrumentations in Contrib already are, like, not locked together, they have their own numbering schemes, so… to…
You know, each instrumentation has its own version.
**Martin Kuba** 13:49 Then, you know, is that true for JS repo as well, or just contrib?
**Daniel Dyla (Dynatrace)** 13:54 just contrib, it's mostly… just…
Tooling convenience that anything in the main repo gets released, altogether.
There's no, like, specific requirement that the instrumentations in that repo lock versions,
But that said, it makes everything easier, because, like, when we had one repo, and all of the versions were locked together, you could look at a package JSON and just say, like, all these numbers are the same, therefore I know they're all compatible, and just move on.
And now… It's not quite like that.
That said, instrumentations are different, because they only depend on the API anyway, so you should be able to use any version of the instrumentations you want to without, issue, as long as you're using the latest API.
**Jared Freeze** 14:54 Yeah, and the whole point of this is to release
whenever we want, right? So yeah, so I think starting over is…
Is the move. I'm gonna contradict myself from earlier. Yeah, yeah, yeah.
**Daniel Dyla (Dynatrace)** 15:05 Instrumentation, specifically.
**Jared Freeze** 15:06 instrumentation. Yes.
**Ted Young** 15:10 So, sorry I misunderstood you, Joaquin.
But yeah, I… if we're starting over and it's a totally separate SDK,
then it would kind of make sense to… to just start the versioning over again on those SDK components, but if it's the same SDK, then we want to…
**Joaquín Díaz** 15:31 Yeah.
**Ted Young** 15:32 Keep using the same, you know, stuff.
**Joaquín Díaz** 15:35 No, that makes sense, but it is still not an SDK, like, it's just a cementation.
**Ted Young** 15:41 Right. Or, so far, so, yeah.
And for the instrumentation, the reason why they benefit from having their own separate version numbers is hopefully not often, but we do sometimes have to post a breaking change to an instrumentation package in terms of, like, the data that it produces.
We don't like doing that, but for example, as we stabilize semantic conventions,
you know, you might go through a 1.0 and a 2.0 of a piece of instrumentation. So that's the reason why it's helpful for them to have their own version numbers, is you need to know when telemetry's gonna break.
**Joaquín Díaz** 16:22 That's the other question that I've had before, like… if…
If your semantic conversions are not… are in development, or in, like, experimental.
you can't go to 1.0, right? You have to go 0.1 something until you are, like, stable.
**Ted Young** 16:42 We've changed our mind on this one.
Recently, as part.
**Daniel Dyla (Dynatrace)** 16:47 This is breaking news, like, 2 weeks ago.
**Ted Young** 16:50 Yeah, as part of… as part of graduation, right, we want to graduate, and so we've been doing a lot of user feedback.
And we've been getting a lot of feedback, especially from the sort of, like, across-the-chasm kind of users, more enterprise-y, more brownfield people. They often have, like, hard rules at their organization that they can't deploy unstable things into production.
And so we were doing, this pattern of saying, hey, it's not stable yet because we might break the telemetry one day. But that was actually confusing people, because we weren't saying.
That these packages, like, the code is unstable and you shouldn't run it because it's unsafe.
And so we were running into… we thought we were being helpful, but we were actually confusing people.
Right.
So they were interpreting this to mean that the packages are dangerous to run, and they're not allowed to run it in production. So for this reason.
As part of graduating and, like, cleaning everything up.
We're now saying, like, go back through every piece of instrumentation, if it's, like, code-stable, market-stable.
And Market 1.0. And then if we break the… if we do a breaking change as part of stabilizing the semantic conventions, just go to 2.0.
So, that was a lesson… a lesson we learned recently.
**Joaquín Díaz** 18:14 Yeah, that makes a lot of sense.
**Daniel Dyla (Dynatrace)** 18:18 And in that context.
**Ted Young** 18:19 We just realized we were communicating it using, like, the wrong channel to people.
**Daniel Dyla (Dynatrace)** 18:26 And in that context, code stability just means, like, how do you set up the instrumentation, right? Like, the configuration and whatever. So it's like, if I have an application using this instrumentation.
and I update it, my application should continue to compile and run without problems.
**Ted Young** 18:43 Yes.
**Daniel Dyla (Dynatrace)** 18:43 It's like… Not, like…
**Ted Young** 18:46 just ordinary SimBear, with the extra thing of, like, if you change the data, you also need to do a major version pump, right?
**Joaquín Díaz** 18:53 Oof.
**Ted Young** 18:54 And if you change the data in an additive fashion, there should be a minor version bump.
So we're still using the versions to indicate data changes, it's just, like, we're not…
If the code is stable, if it's not harmful to run this, then… then mark it 1.0.
Because people were interpreting less than 1.0 to mean it's, like, dangerous, like it's gonna blow up on you or something.
**Daniel Dyla (Dynatrace)** 19:16 Yeah, I think people are also more afraid than they should be to go to 2.0. I'm not talking about the API here, but, like, I think people feel like they need to be perfect to get to 1.0 when it's not like that at all. It's like, the instrumentation can go to 2.0, 3.0, 4.0, or whatever if it needs to.
**Ted Young** 19:35 It's… it's hard to have version numbers with different rules around them in the same project.
Right. So I can totally see why…
Maintainers naturally wanting to not break things would pick the strictest rule, and try to stick to that everywhere, also.
I can see people wanting to do that.
**Wolfgang Therrien** 19:56 where is this being, sort of documented for clarity, this, this idea of how we communicate code stability versus data shape stability in terms of our instrumentation, and API? Like, is that going to be…
**Ted Young** 20:11 So…
**Wolfgang Therrien** 20:12 Individual repos? Is that going to be in the semantic, convention?
**Ted Young** 20:18 Right now. If you go into the semantic conventions, we do have docs about this. We need to update them, though. They're probably out of date. And we did just put out a blog post a little bit before Christmas break about stability and graduations. That blog post is the latest up-to-date.
thing about, like, our general plans.
All the stuff we need to do to graduate.
**Wolfgang Therrien** 20:40 Awesome.
**Daniel Dyla (Dynatrace)** 20:45 I just put that blog that Ted was talking about in the chat.
**Ted Young** 20:48 So good.
**Wolfgang Therrien** 20:49 Thank you.
**Martin Kuba** 20:57 Okay, sounds good.
Anything else on this?
**Joaquín Díaz** 21:05 Having said all that.
The decision we have to make is whether we start with zero point something until we feel…
good enough, or we just go with Pompochero.
**Jared Freeze** 21:21 Sorry, are we talking about instrumentation?
Specifically?
**Joaquín Díaz** 21:24 Yeah.
**Jared Freeze** 21:25 So… Martin's PR specifically has semantic conventions that haven't even had discussion.
That feels like it has to be zero.
Like, it… like, for first release, do you agree with that?
**Joaquín Díaz** 21:39 Biff.
**Ted Young** 21:41 I would just reflexively recommend, since this is all very, very new, and we don't actually want anyone to run this in production right now, as far as I'm aware, we don't yet want production users of this.
We should probably mark all the new things as beta until… We actually wanna…
Make a scene and tell people, hey, go, like, use this in production, we're, like, ready for feedback.
**Jared Freeze** 22:07 Do you mean, like, officially do alpha tags?
Like…
**Ted Young** 22:10 Or at least keep it less than 1.0 or something. I don't know, right? Like, we're definitely far away from, like, wanting people to actually run this stuff, so…
you know.
**Joaquín Díaz** 22:21 Yeah, we at Embrace were going to…
Just some guinea pigging, because we… we do want to use some of this.
And, we do have a fair amount of users, so we can let you know if he's happy or…
**Ted Young** 22:34 Oh, okay.
**Martin Kuba** 22:38 And for the existing instrumentations that we're gonna be moving from the other repositories, we're gonna keep the same versions for now?
And then we… maybe we can have discussions about which ones are… have been around for a while, and if they're… if you feel like they're stable enough, you can just bump them to 1.0.
**Joaquín Díaz** 22:57 If. That would be great.
**Martin Kuba** 23:06 Right, I do have one more,
One more quick, just, request for review.
Marco and I have been working on, Marco mostly has been working on, the, a new navigation timing instrumentation.
Thank you for… thank you, Jared, for looking at it already. But, yeah, request for review.
**Jared Freeze** 23:33 And I have quite a few in there, just, like, cleaning up build process, like, just stuff I'm learning along the way, so… I keep posting in Slack. I know, you know.
Just look when you can. Appreciate it.
Oh, also, a quick update. So, I did a bunch of work in the main repo, I don't think in Contra, but in the main, to try to divorce some of the node code, so I inverted a lot of the
code, so it's not, like, if node, it's actually, like, if feature else, which is gonna give us, static analysis boosts. So, like, Next.js will not compile
our SDK, our company SDK, at the moment, because of these issues in some of the other packages. So, I've been slowly pulling those things out. There will be new stuff in two…
10?
Are we on 210? And then…
So, I'll be doing some testing, I'll post in Slack how that's going, but
I'm also gonna push again for that, package PR.new tool, which allows us… like, right now, I'm, like, literally copying and pasting build folders around to try to test, and it's a huge pain. It'd be really nice to send out PRs that have
like, alpha code, or unreleased code in the PR, so we can look together and have it run in CI. So I'm gonna push hard again on that in the JS Slack.
Because I think it's incredibly useful. We've actually had trouble at our company trying to get it through. Everyone has security questions. It looks fine, it looks like it has no perms, and everything we do is public, so it should be okay, but, I'll let you know.
**Martin Kuba** 25:17 Sounds good.
Alright, we've got 5 more minutes, does anyone have any other things they want to talk about?
**Jared Freeze** 25:29 So I, took a ticket to look at Weaver. Does anyone here have experience with Weaver already?
**Ted Young** 25:39 I know of it, I don't… I don't hack on it.
**Jared Freeze** 25:44 Okay, so I think the request was collect absolutely everything, like, every convention that belongs to web, and make, like, a master list.
I'm just gonna do research and figure it out, but I'm just curious if anyone could, pitch in.
It's fine if not, but…
**Ted Young** 26:02 You mean to just help figure out how to feed… feed all of our conventions into Weaver?
**Jared Freeze** 26:08 Yeah, basically. I, you know, if there's anything I need to know that's beyond, just docs or something.
But that's fine, I'll just figure it out and post.
**Ted Young** 26:17 Yeah, I would say my coworker on my team, Arthur Silvacens, has been hacking on Weaver a lot, so if you have questions, like, how the hell does this work?
Ping him.
He's in Brazil, he's in Brazilian time.
**Jared Freeze** 26:33 Cool. Thanks.
**Martin Kuba** 26:40 Alright, cool. I think we're all done. Thanks, everyone.
**Ted Young** 26:43 Good seeing you.
**Jared Freeze** 26:44 Thanks.
**Martin Kuba** 26:45 tune.
