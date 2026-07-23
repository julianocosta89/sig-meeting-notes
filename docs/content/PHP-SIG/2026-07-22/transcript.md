SIG: PHP SIG
Date: 2026-07-22
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 01:04 Hello?
**Pawel Filipczak** 01:06 Hello, hi, Chris.
**Chris Lightfoot-Wild** 01:08 How are you doing?
**Pawel Filipczak** 01:09 I'm okay. How are you?
**Chris Lightfoot-Wild** 01:11 Yeah, Mario, thanks, yeah. Sorry about that, I was just, went to turn my laptop on, and the battery died, so… Poor planning on my part.
**Pawel Filipczak** 01:20 Yeah, I'm good.
**Chris Lightfoot-Wild** 01:21 I think Bob's off there, isn't? You said Sergey's off as well.
**Pawel Filipczak** 01:24 Hey, yeah, come on, yes.
**Chris Lightfoot-Wild** 01:27 Yeah, unless we get any surprise visitors, I suppose, but probably not.
Told me to… I'll just share the screen, I'll just get it set up.
That was… Many open tops?
**Pawel Filipczak** 01:44 Wow.
It's in Boston.
Bang.
**Chris Lightfoot-Wild** 02:07 Let itself add in on to the,
**Pawel Filipczak** 02:12 Do you want to interfere?
**Chris Lightfoot-Wild** 02:14 Yeah, I'll share, sorry, I just wondered, are you, were you editing the agenda?
**Pawel Filipczak** 02:20 No, I don't have anything except that, but we… I just made a release of the distro, but…
**Chris Lightfoot-Wild** 02:28 Nice.
**Pawel Filipczak** 02:29 Yaw.
I have to check if it passed 10 years, that's… I'll pull it.
**Chris Lightfoot-Wild** 02:39 What are you doing? I'll just get the spin up.
One second… Oh, boy.
**Pawel Filipczak** 02:51 Yes, it was released.
**Chris Lightfoot-Wild** 03:04 What SIG was that?
**Pawel Filipczak** 03:06 Yeah.
Oh, I can put a link into the chat, you can add a link.
**Chris Lightfoot-Wild** 03:16 Yeah, will do.
That's true.
**Pawel Filipczak** 03:20 I put it in the chat.
**Chris Lightfoot-Wild** 03:22 Oh, thank you, sorry.
Did you have anything else you wanted to, tack on? I would introduce…
**Pawel Filipczak** 03:50 So, now I'm… I'm working on OpenTelemetra.io documentation, so I'll copy docs from the distro… to… to the… to the I.O. repository, where the official doc's located.
And… Hopeful… I hope today I will make a PR, and I will add you to the… To the PR, and also I will add Bob.
So… Please take a look Yeah. Maybe… I, woof.
I'm not sure about where to put it, so I… I will include it in the… in the… zero-code instrumentation tree, because there are two places. One is the SDKs.
3 with SDKs, and the second one is the tree with the zero-code instrumentation, so I guess it's a better place.
But if it's… if you have any other ideas, please let me know on the PR, yeah, so… I didn't… didn't make any broker build of the dock, so I didn't test it yet.
But, we'll see.
**Chris Lightfoot-Wild** 05:06 Sounds good. Yeah, I'll, I'll keep an eye out for that.
I noticed as well, sorry, in some of the release notes of 0.6, there was some problems with PHP scope, or… it looks like you've sort of resolved it, I guess, but… Just to understand it myself, like, the… the namespacing.
like, that's in, like, Laravel, auto instrumentation. Also includes like, repetition, I guess, of Illuminate, whatever.
So, did that cause problems? Like, does it need to change, or does it… Does your Sculpa stuff make it work?
**Pawel Filipczak** 05:41 So the scoper is… is scoping everything, almost everything, in the… in the… in the code we are… we are installing with the… with the composer. So, it's keeping… open telemetry.
and SDK, API, and others totally separate, and also all of the country packages, and all of the cross-dependencies. So if any package is getting any dependence, it can be whatever library.
Then, it will be scoped.
So, the, the, the issue… mentioned in, in… in Slack, I guess it was because it wasn't working correctly when the… when the scoper, I mean, the… so we are packaging in two versions. One, the scoped one, and the second one, the classic one, without any scoping.
**Chris Lightfoot-Wild** 06:38 Yep.
**Pawel Filipczak** 06:38 And the issue was that… We don't… We don't have good tests which are covering the option when the scoper… using of the scoped code is disabled.
And it was causing the issues, and I fixed that.
That's, in some comet.
And now it would… it should work.
**Chris Lightfoot-Wild** 07:03 Nice.
**Pawel Filipczak** 07:04 True.
**Chris Lightfoot-Wild** 07:05 Nothing's a change on the instrumentation side, then, you've… No. That's it.
**Pawel Filipczak** 07:10 No, no, no, no, no.
And what we introduced last time, it's… it's the, the bridge, which is actually the set of class aliases.
So, if you… if you want to use OpenTelemetry inside your application, I mean, whatever, add your own instrumentation, use the API, or SDK in your application, so built-in, some dependencies to the OpenTel.
Then, there is a bridge, which is enabling the class aliasing, so we are not adding any additional unscoped code, we are just adding aliases for the unscoped to the scoped code.
In that case, you don't have to install SDK or API on your own. You should, but it won't be loaded anyway.
But you can just reference to, to the… to the… to the scoped code.
The only issue is that the versions may differ, so you can require API version X, but the distro will provide version, B, for example, right? Yeah. In that case, we'll emit a warning.
So it's on… the user mind to keep both versions in sync, so that was the reason why, in the last release notes, we added the versions of the delivered packages for the SDK API and contacts.
some.
**Chris Lightfoot-Wild** 08:52 Which way around is it, then, sorry? So if… if I've got an application with, the OpenTelemetry API and SDK, And then the distro's got those vendors as well.
Which one is used? Sorry?
**Pawel Filipczak** 09:06 So, by default, so that if you will not… if you will not enable that bridge, then your application will load your version, I mean, the application version.
**Chris Lightfoot-Wild** 09:20 Yeah.
**Pawel Filipczak** 09:21 And the distro will use the scoped distro version.
**Chris Lightfoot-Wild** 09:26 Okay.
**Pawel Filipczak** 09:27 So you… but you… then you will get the split on the tree of the… of the span, so you will not build the tree with every span. So if you're part of… if your application will produce any spans.
then it will be separate. They will not include that into the tree. But if you enable the bridge.
Then it will create cluster ASS, to the SDK and API.
and then it will point to the scoped one, I mean, to the scoped context, and it will keep one context, which is created by the distro. Then, your application spans will be included into the tree of the distro.
**Chris Lightfoot-Wild** 10:11 Okay.
Cool, that makes sense.
Thank you. Yeah, I'll have to play around with that.
**Pawel Filipczak** 10:17 And now it's disabled by default. I think we should change it in the future to be enabled by default, because I think it's… It's bringing more value if it is innate, because then everything is… makes sense if everything is in the… in the same context tree, right?
**Chris Lightfoot-Wild** 10:35 Yep.
**Pawel Filipczak** 10:36 But, yeah, let's say it's… we can call that… experimental.
**Chris Lightfoot-Wild** 10:43 Nice.
Cool. I didn't have anything to add on the agenda, so do you want to quickly, sort of, fire through the boards, and…
**Pawel Filipczak** 10:52 Yeah, I'm having a nice,
**Chris Lightfoot-Wild** 10:55 Awesome.
There's links at the top of this feature, isn't there?
Certain session… Oh, we probably need to add your distro link on there as well, don't I?
**Pawel Filipczak** 11:11 Yeah?
**Chris Lightfoot-Wild** 11:13 Might as well.
Although you're maintaining that, so I don't need to… Look at that for now.
Can't manage this anyway, but… oops, Got one PR, which I think I… you looked at, and then I approved yesterday as well, but hopefully you can pick these up when he's back.
OpenTelemetry… Issues, what have we got?
**Pawel Filipczak** 12:02 Yeah, here I ask for the… for the code, which is transformed.
And… I hope he will include that.
Yeah, of course I can create some account and try it on my own, but it's better to… To, to, to, to get it from… From him, but if he will not respond, then I… maybe I'll be registered on that page and generate something on my own.
**Chris Lightfoot-Wild** 12:31 Nice.
Yeah, I do realize I don't still use the Iron Cube.
There you go, I suppose.
Have you looked at this one already?
Probably read through that later, some sort of feature requests.
Usual renovate sperm, Yeah, well, this is one for… I'll need Bob as well. Any way to imagine.
I didn't have to actually, come back to it.
After we go through the PRs for Contra, but a question to flow.
There's a few new ones, and I'll try and have a look at some of these.
Not, much time this week, but try to get on those.
It was around… So, in contrab, obviously we've got that workforce split.
**Pawel Filipczak** 13:52 M.
**Chris Lightfoot-Wild** 13:53 Let's just tug in… at main, but Renovate's come along and decided that it'll try and track the… The commit for men?
But obviously, every time that you accept a new commit, it'll just generate another PR.
With a new harsh, like, and continue on that way.
So, like, the example of that was in, I don't have a drain.
Kafka, right?
Yeah, so that's always gonna change.
And I guess I'd… I wonder what… if you could, offer up your thoughts, perhaps, on the best approach here. Either this workflow stays in Contrib.
But then with TAG, A specific version of it, just so we've got the workflow files, with, like, a more static version.
Or, potentially, move the workflow out into the OpenTelemetry PHP organization.
Which is the one where all the subtree splits end up.
And then it just lives there instead, and then that… We'll just track against, like, main, but it's not gonna have to change that much.
Don't know if you've got any immediate thoughts on that.
Or… I could just,
**Pawel Filipczak** 15:24 But isn't it tagged because it's using reference, which is, you know, to the repository?
But if you will be… if it will contain the… A relative path.
then I guess it should not be tacked with the version.
**Chris Lightfoot-Wild** 15:47 Yeah, it's just that when this does a subtree split, the relative path doesn't work, so that's why it's…
**Pawel Filipczak** 15:53 Okay, so when the split is running, then it's executing the build on the… this return repository, right?
**Chris Lightfoot-Wild** 16:02 That's right, yeah.
**Pawel Filipczak** 16:03 Okay, that's the original.
**Chris Lightfoot-Wild** 16:06 Yeah, so it looks a little funky, because when this runs in this repo, it still has to, like, check out another version of itself.
But, yeah, without doing that.
It wouldn't work on a split, so that's why it's kind of set up that way.
**Pawel Filipczak** 16:24 No.
**Chris Lightfoot-Wild** 16:26 But yeah, it's just to avoid that annoying renovate drift that will always happen.
**Pawel Filipczak** 16:31 I don't think I put up.
I have no idea how to solve that problem.
**Chris Lightfoot-Wild** 16:37 Yeah, I'm not entirely certain myself either, but I could put it on Slack and see if we've got, some collective thoughts on there, perhaps if it comes to you later, then,
**Pawel Filipczak** 16:45 Yeah. Who does? Go take them.
**Chris Lightfoot-Wild** 16:48 Yeah, thank you.
Nothing else, from me, and the PR list, I could do with… have another look through and see what I can, maybe merge in, but I think Bob's already done quite a lot over the last week.
Ahead of the release he was wanting to do, so…
**Pawel Filipczak** 17:05 Yeah.
So, one question about the new workflows. Do you want to solve the renovate issue first?
And then… Move other instrumentation into separate workflows, or just, you know, do… continue work?
**Chris Lightfoot-Wild** 17:24 I mean, I would like to move toward the split workflows if other people are happy with that. I did put a thread up the other week.
on Slack. I can't remember if we got… Much feedback.
Damn.
**Pawel Filipczak** 17:39 So, in my opinion, it will help… it will help to maintain at least those… those PRs we have here. Now they are all, you know, failed, then we have to take a look deeply into what was causing the failure, right? Then we see just… what's going on, so it will be… I think we should move on with that soon.
And then transform everything to the, to the separate workflows.
In mine.
**Chris Lightfoot-Wild** 18:07 to, like, try and push on with that, then, if you think that seems like a reasonable thing. So I suppose, yeah, so each one of the failing ones would instead just show… Two or three failing workflows, rather than 100.
**Pawel Filipczak** 18:19 Yeah, exactly, exactly.
**Chris Lightfoot-Wild** 18:22 Okay, yeah, well, no one objected in the Slack thread, so maybe that's enough that we can carry on.
So I'll just try and do a few more, like, chunk by chunk, I guess.
**Pawel Filipczak** 18:33 We can split and share the work between us, so if you want, we can just choose which packages you want to take care of, and which I should take care, and yeah, I can help.
**Chris Lightfoot-Wild** 18:45 Yeah. Yeah, we can do that, if you want. We could start, like, working one of us from the top, one from the bottom, potentially, and then maybe try and meet somewhere in the middle, but I'm happy to have a crack at that. I've got a bit of time tonight, so I might, I'll open a PR for a couple more of them.
**Pawel Filipczak** 19:01 Good.
**Chris Lightfoot-Wild** 19:02 Yeah, and then I'll just open a thread, saying that we're cracking on with that, and yeah, we'll pick it up from there.
**Pawel Filipczak** 19:09 Nope.
**Chris Lightfoot-Wild** 19:09 Thanks very much.
Cool, well, I guess if, if there's nothing else, we might as well call it for… for the day.
**Pawel Filipczak** 19:16 Yeah, okay.
**Chris Lightfoot-Wild** 19:17 It's your time. Tweet hello.
**Pawel Filipczak** 19:19 thing. See you right away.
