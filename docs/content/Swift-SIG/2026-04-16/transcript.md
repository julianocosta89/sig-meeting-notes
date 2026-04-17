SIG: Swift SIG
Date: 2026-04-16
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**vvydier** 02:20 Hello, Nacho, how are you?
**nacho** 02:24 Hi, Vincent, how are you?
**vvydier** 02:25 I'm good. I'll read only once.
Attending the call today.
**nacho** 02:32 Yes, it looks so.
**vvydier** 02:33 Okay.
**nacho** 02:35 Yeah.
**vvydier** 02:35 How are you doing?
**nacho** 02:38 Fine, fine.
Yeah.
**vvydier** 02:41 Yeah, so… Let's see… Yeah, it's me.
Yeah, since… Price is gone, I think we are lacking some…
**nacho** 02:55 Yeah, some hands. Definitely. Yeah, I hope he comes back soon.
**vvydier** 03:01 Yeah.
**nacho** 03:01 Okay.
**vvydier** 03:03 Okay So, what are we discussing today? Let's see…
**nacho** 03:08 Yeah, okay, yeah, that's true.
**vvydier** 03:10 They're already 5 minutes… Oat.
**nacho** 03:13 Yeah, we already have 5 minutes, so everyone is already here, I suppose.
Yes. Okay.
So let me… I… Let me share screen.
I'll wait back off.
**vvydier** 03:39 I might… I might come to Europe this summer, so…
**nacho** 03:42 Oh, really?
**vvydier** 03:43 Yo.
**nacho** 03:44 But Europe is quite big, right? I know.
**vvydier** 03:48 I did Spain or France, so I'm married.
**nacho** 03:51 Okay, yeah, great.
Yeah, let's see if we can meet in person. It would be great. Yeah, yeah. To be in… Okay, so, yeah, I think these are the topics from last week.
And… From last week, it was merged, so this is removed. Yeah, basically, we have the release to… for one.
**vvydier** 04:19 Oh, we didn't?
**nacho** 04:21 We didn't release that.
Okay. I mean, we released… we released it, But only… On the core site, but only, without public… access. So, I would say that On the Swift project, we are already using that in the tests, in the nightly tests.
So, if we go to action, we can validate that it's working.
Okay, this is not working, but we should have… This is the nightly integration.
No, that was a branch I created. That's not a good one. Yeah, that's the one that I failed doing, and this is what… I think it was Bryce, who did it correctly. So it looks like it's working.
I would like to check eats, really.
Taking main… Right?
So it should be running with the latest thing we have there.
So I think we could already go and release this as, none previously bursts, yeah.
**vvydier** 05:45 So this is a, okay, so this is…
**nacho** 05:49 This is Coral, yes.
**vvydier** 05:51 Okay, okay, so it's all… the pre-release already went and fine.
**nacho** 05:55 Yes.
You know, it… And it has been billiona stable on the other, which was running with this.
So I think there was also a… appear here, about 2 for 1.
Oh, but this was just, an update… That he didn't update.
So I think I'm gonna change this.
Caribbean?
So we can match this one.
I'm product with a personi.
**vvydier** 07:05 So this is based on the… Okay, so this is.
**nacho** 07:12 Yeah, this is the… the core is updated now, and we must now update the library, which… Once this is merged, I think we can…
**vvydier** 07:22 you know.
**nacho** 07:22 finally create that. I can create that privilege.
**vvydier** 07:25 There is no way, there's no way to have an automated, you know, like, a dependency.
**nacho** 07:29 Yes, there is, but… We are fixing the… I think the… we need to fix the dependency in order to be sure we are building what we want.
And this one, yeah.
I think we need to watch this.
Yeah, we need to be sure that we are doing this. Apparently, we'll take the newer one, right?
But we prefer to… force this here to be sure that there are no catches in between that could fail, and that fixes an issue. So, yeah, I will… now that it's merged, I will wait for that to finish.
**vvydier** 08:11 Medicine, no.
**nacho** 08:13 Yeah, okay, so, let's go… You have updated it.
No, okay, yeah, that's right. So, released, core… Okay, yeah.
Yeah, the other was, we were talking about the span events getting deprecated.
**vvydier** 08:55 Oh, that is, that, I think, yeah, let's…
**nacho** 08:58 We talked about the.
**vvydier** 08:59 Ari, yeah, Ari was gonna look into it, but yeah, let's see, yeah.
**nacho** 09:05 Yeah, lit.
Okay, so we have no more new topics, I think we… so we can follow on the… on the PR side, have done some… peers and reviews before this meeting.
So, we still have this… documentation from Willy, But… East.
has been awake for a long time. I don't know where… We have this, syncowit API for exporters, but I think we talked in the past.
So, what I… he agreed with the changes I proposed last week.
That was adding the asynchronous support to export methods.
**vvydier** 09:55 Yeah, but not new.
**nacho** 09:56 But he said… Yeah, but I think the changes he was doing was more on having a different name for them, and I am asking him to keep the same name.
Because they… even if they have the same name, the signator is different. One is a sink, the other is not, so they can come back, they can leave.
In the same position, and if you call from an Async way.
If you call it with await, it will use the async method, which is, I think, preferred.
**vvydier** 10:26 Which is what we need, yeah, yeah.
**nacho** 10:28 Yeah, and that's what Apple does with their libraries. Also, you have an async version, and if you call with await, the compiler directly uses the await one. So I think that's the way to go. So I asked that to him.
More, we have this environment propagation carrier.
**vvydier** 10:50 This one's a big one, right? Yeah.
**nacho** 10:53 Yes, that's a big one, and I am not sure I like what I have seen here.
I have been taking the.
**vvydier** 11:03 Is it… is it adding additional, like, environment variables, Like, is it, like, a configuration thing that.
**nacho** 11:13 Yeah, I don't know why…
**vvydier** 11:13 excited.
**nacho** 11:17 He decides to replicate it.
To a new setter and getter.
I done… understand very well.
Why they don't use this… Exactly.
And the sale state…
**vvydier** 11:40 Did you add that comment, or… Or not yet.
**nacho** 11:44 Yep.
So I'm not sure why this changed.
Yeah, I am starting to think that, yeah.
We are starting to see many AI.
Initiation here, in this… not only in this PR, because I think… The, the, yeah, implementation is, is… Extremely complete, which is a bit surprising, to be honest.
**vvydier** 12:29 So…
**nacho** 12:29 I mean, it…
**vvydier** 12:30 When you have such a clean documentation, you know that it's someone else's…
**nacho** 12:34 Yeah, that's right. No one really does that. I mean, you can be very, usually, yeah, maybe this is an exception, but okay.
I am not sure we want this. I don't know why we are… changing this exactly, so I really have to think about.
**vvydier** 12:53 Jesus.
**nacho** 12:54 they have had, like, a… I don't know, something that surprised me is… have been introduced from people. That is not him.
To these changes.
so they don't know exactly why they are moving this, so we need to… Think about this, because… I think it makes it a bit more complex.
**vvydier** 13:21 Nope.
**nacho** 13:22 Okay, yeah. So, yeah, I need more time for that.
And also probably someone who uses it.
to review properly.
Maybe when Bryce comes later.
Yeah, and the other was this, results we seek to send emulations in some tests.
I, it… they made sense, total sense, so I approved that, before, so… and now I see it's… That's who I am.
Yeah.
**vvydier** 13:59 Oh, so this did not go through in the previous… Oh, this… okay, this is not, release, right? Yeah, you'll have to make it as part of the pre-release test and all of that, and then…
**nacho** 14:10 Yeah, and it's also a test only, so the only change that was happening here was a test.
So I don't mind, and it made sense, so that… That was really easy.
to… to decide. So, and the other issues we have here, and I think that we have reviewed recently.
Is the Ashenkaway APIs for exporters, that… that's the branch we have.
Adi, which was going to add… Specklind.
And some questions that have appeared recently about swift concurrence immigration.
Yeah, this is, I mean, that we… Built with Swift 6 doesn't mean that we are… concurrency. Ready, there are many things to happen here, and yes, I'm questioning Yeah, the synchronization gap is exercised.
Yes, yeah, that's true. That it has never been… that it builds with Shift6, that doesn't mean that we are approved the…
**vvydier** 15:25 Yeah.
**nacho** 15:26 That we are concurrency.
Aware, and there are many changes that… We'll need to drop.
Yeah, yeah, before we can really say that.
So, this one for the core.
**vvydier** 15:40 That should be, like, in a branch or something, right? So that way… Can work on it parallelly.
**nacho** 15:46 Yeah, there is a rant, for Swift 6, for core, and there is another for OpenTremetry.
Or they mean laboring. But the thing is that I mean, we build with Strive6. That doesn't mean we are… That we can be a strict con… strict concurrency.
**vvydier** 16:07 Works.
**nacho** 16:07 with us. It doesn't.
And it's gonna take a lot of effort. I mean, just building with Shift 6 was a big effort, so changing all the rest, it's gonna be probably a lot of time.
Not easy, with, with low-level stuff as we… Yeah. So, yeah.
It's gonna… I mean, it needs a lot of resources that I don't think we can provide.
**vvydier** 16:35 Good morning.
**nacho** 16:37 So, yeah, for the main library, You have a pull request.
These are old ones, the… these are old ones, also?
This one I answered last week.
About the…
**vvydier** 16:57 Oh, there's.
**nacho** 16:58 in the Apple library for Sweet Distributed Tracing.
But no feedback, more, more feedback there. Here, there was a crisis that I answered the other day.
Basically, it provides a fix for a crash.
And this is one of the examples I said about the AI.
doing, things.
Because he doesn't provide any description and say, cross-fix. Okay, yeah, that's… that's great. And you… you check the code.
And you see that?
**vvydier** 17:36 Oh, so he probably just asked, AI…
**nacho** 17:39 Yes, and he has the AI in… Chinese, I don't know what language those can be heard from.
**vvydier** 17:48 Yeah, yeah.
**nacho** 17:48 So probably, yeah, probably use this… Yeah. If you speak with your AI in a language, he answers in that language.
**vvydier** 17:56 language, yeah.
**nacho** 17:57 That's what you get with code, so yeah, I also have to… talk with mine in English, in order to get comments properly done in English, so yeah. So the thing is, this… task?
I, I, I obviously ask.
Provide a description across the stack, also the comments in the call should be in English.
**vvydier** 18:20 English.
**nacho** 18:20 That's why, yes.
**vvydier** 18:21 Yeah, yeah.
**nacho** 18:22 But, yeah, and I was thinking, but probably when we are more… I was thinking that we… if anyone is having AI… PRs already that they should sit in the committee.
**vvydier** 18:35 Yeah.
**nacho** 18:36 Because, that, that, that's a different…
**vvydier** 18:39 Makes it… makes it easier to, yeah, review, because then you know, right?
Yeah, or they should just clean it and resend it, you know, instead of just sending it.
Yeah.
**nacho** 18:52 Yeah, I set this up, but no more feedbacks for it, I don't know.
So, Mark, but that… That has, now you will see… We have a fixed threat safety crashing network status status. If you remember, What crash it was.
Changing?
This was him.
Network status.
Right? So, it looks like…
**vvydier** 19:20 Somehow?
**nacho** 19:22 Everyone is trusting TML. I don't know why. This has been here for… a long time. This was a, project that Bryce added, like… 3 years ago, probably, around that?
No one… we had one crash in the past with that, but no one more… and now we have this other… PR, which speaks a threat safety class in network status.
And as you can see, he also… took a lot of time to fill the summary with all the… the information.
He also doesn't say that the AI created this.
**vvydier** 20:05 No.
**nacho** 20:06 But there is one thing that really Shows that. That is when you go there, it changes.
You see that the comments are cut here.
You see that? Not only that they are long, but they have very short That's cloud code. When you write it with cloud code, it… the comments… he takes this limit of the lines.
We can see that we have longer lines, but for comments, it always cuts very early.
**vvydier** 20:36 Yeah, really.
**nacho** 20:37 So, yeah, so basically, he's doing a, like…
**vvydier** 20:43 Yeah.
**nacho** 20:44 It's a… it's registering for a, for a, for a delegate, and using what the delegate provides with this.
But I would like Bryce to take a look here, because he wrote it, so I would wait for that.
And also, I… I will… the same thing, I mean, if an AI did this, I don't know if I should add some comments, but if the AIs did this, they should say.
**vvydier** 21:10 Yeah. And they should.
**nacho** 21:13 And so we probably should have, like, a policy.
written somewhere about that. Say, please, which AI and which version you use for it.
Yeah. because… it's not… the same. And also, he's using an NS log here, which… To be honest, it's quite outdated.
And also the documentation is… Extremely verbose. Do you know what I mean?
**vvydier** 21:53 Yeah, yeah, yeah. Our documentation?
**nacho** 21:57 We'd like to documentate.
document research everywhere, but we are not so verbose, because it… unreadable.
**vvydier** 22:05 Right. You spend more time reading documentation, right?
**nacho** 22:10 Yep, then… Why do you need this?
It's because it's explaining.
This is because the AI is explaining, and sometimes users comments to explain why the changes, and that's not what we want.
We… we want to know what a method does, not what it fixes.
To be honest, so yeah, I will… I was thinking about adding some comments here. I don't know if you agree with me, or…
**vvydier** 22:41 No, no, I completely agree. I think we should even have this as, I don't know, if OpenTelemetry itself should have some sort of a policy, or at least some sort of a banner saying that, okay, you know, when you contribute, you don't just… well, it's so easy to create PRs with you.
**nacho** 22:59 Yeah, I mean… AI is a really great tool.
**vvydier** 23:02 Yeah, yeah.
**nacho** 23:04 Agreed, but…
**vvydier** 23:04 Spend some time to clean up and, you know…
**nacho** 23:07 Yes, that's right, and make things that… Unlike the rest of the… the…
**vvydier** 23:13 Nicole.
**nacho** 23:14 I'm… Yeah, and follow the style that… There was other things, huh.
**vvydier** 23:21 Yep, yep, yep, yep.
**nacho** 23:23 So yeah, I will keep this for the future. I think Bryce should be back, Soon, right?
**vvydier** 23:30 Sweet.
**nacho** 23:30 Oops.
**vvydier** 23:31 Okay, one month he'll be off.
**nacho** 23:34 Okay.
So this is… these are all the pull requests, the rest are the… Updates for third-party libraries that They add more noise than to them.
I really don't like this, because these are only used on tests, right?
So why… I don't mind if… The tests are using old… Mercia.
**vvydier** 24:08 Yo.
Exactly, so they just.
**nacho** 24:13 They… they… they… for example, for me, I am not… I mean, the updates that I get on email, they are…
**vvydier** 24:21 They, they, I wish, I wish it also, does it also recommend what is the latest that you should update to? Because if it is doing… You know, then we can just, Because it might have some links to the collector repo and, you know… Yeah, that is… because it is generating PR and creating more work, it's not really doing…
**nacho** 24:48 Yeah, it's so much noise that… that my email… Client decided automatically to move that into… That's true. I am totally honest. They are… because I was deleting all of them, because I am not interested in these updates, but on real PRs, and my email decided to move all of them to the trust directly. Even the good ones, which shouldn't happen. So, yeah, I am a bit… blind, and I don't know how to fix, it's my phone, right, which did that. I don't know why mail on the phone did that, but it's putting all of them to the trust.
**vvydier** 25:24 Yeah.
**nacho** 25:25 automatically, all the… GitHub messages I receive, so that's not good.
So I am a bit… Yeah, I don't… I don't check that very often.
**vvydier** 25:35 Sometimes AI is, doing good stuff, so you don't get too much of…
**nacho** 25:42 Yeah, my problem is with all these updates that are not meaningful at all.
**vvydier** 25:47 Yo.
**nacho** 25:48 So, so those for the PRs, for the issues… We have… Cool.
Oh, this was the… okay, yeah, I have not checked this.
**vvydier** 26:07 Good guy.
**nacho** 26:09 So he added, this is the college tag, And this is his no words, just this.
Come on.
**vvydier** 26:32 Oh, this is a crash fix, PR, yeah.
Yeah, this is becoming…
**nacho** 26:41 We're doing basically the same, right?
He's doing basically the same as Shinokad said, probably that… that's what…
**vvydier** 26:47 Beautiful.
**nacho** 26:48 what… what clothes is now.
Apparently, that's a good solution. I don't… I don't… I am not.
**vvydier** 26:55 No, but he can validate it, validate it, he should validate it, then he should just clean it up and send it, you know? If it's not a test, and Without doing that, it's just, like, posting it is what really, creates more noise.
I mean, hopefully he can get your comment and then clean up and send it… update it.
**nacho** 27:21 Yeah, I hope so. I mean, both were fixing the same thing, so the first who committed, If it's good enough.
But yeah.
**vvydier** 27:33 Oh, I thought he linked that in the issue, right? Isn't that the…
**nacho** 27:36 Yes, healing that in the issue, I don't know. Yeah, I just… I have not checked this, it just appears.
**vvydier** 27:42 Yeah.
**nacho** 27:43 Because this is the only new one, all the rest are old, and I had not realized this was here.
So yeah, I don't know. Yeah, that's, that's all, I think.
I will try to find some time and create a release, two-for-one for the main library, now that we have the core fixed with that issue that it was the monotonic clock, I think?
And see if we can… At least release that.
**vvydier** 28:25 Okay.
Sounds good, it must be, like, late in the evening for you.
**nacho** 28:30 Yep.
**vvydier** 28:31 I will let you go.
Enjoy your evening, enjoy your dinner.
Oh, yeah, not dinner time yet, right?
So yeah, okay.
**nacho** 28:41 Bye.
**vvydier** 28:42 Bye.
