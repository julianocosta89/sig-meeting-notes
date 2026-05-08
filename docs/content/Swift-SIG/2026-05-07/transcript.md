SIG: Swift SIG
Date: 2026-05-07
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 05:50 Pretty natural.
And if…
**Vinod Vydier** 05:55 It goes.
**Bryce Buchanan** 07:18 Okie dokie.
Nope.
Did not show drop?
**nacho** 08:04 Hello?
**Bryce Buchanan** 08:05 Hello.
**nacho** 08:06 Yeah, totally.
Zoom in this laptop and with headphones, sorry.
Yeah, I don't know. The other day also had some.
Probably it's a, you know, still an Intel Mac.
Okay.
**Bryce Buchanan** 08:27 Alright, shall we get started?
**nacho** 08:34 Yeah, probably, probably both.
**Bryce Buchanan** 08:37 And since we didn't get to talk about these last week, I'll bring them forward.
**nacho** 08:42 Yeah, that's right.
**Bryce Buchanan** 08:45 So… Release 2.4.1.
**nacho** 08:51 Yes, we have not done that. We should probably do that.
That we weren't.
**Bryce Buchanan** 08:57 Core, or for the memory phone?
**nacho** 09:00 For the main package, we updated core.
I think it's already on release?
I mean… In core… I think core version was updated and also unreleased, and the nightly builds are happening using that since then.
**Bryce Buchanan** 09:19 Cool.
**nacho** 09:22 Check it.
But… Yeah, I think the core version is already updated.
**Bryce Buchanan** 09:34 Okay.
**nacho** 09:35 And… tickled.
**Bryce Buchanan** 09:38 So, core is at 241, or…
**nacho** 09:41 I think core is true for one.
**Bryce Buchanan** 09:43 Okay.
**nacho** 09:44 I think.
**Bryce Buchanan** 09:50 Oh yeah, look at that, okay. Yeah, so you can bring that in and… Yeah, that's right. Okay.
**nacho** 09:58 So I… I think it was already added.
I will, I will keep the number.
**Bryce Buchanan** 10:17 We don't want to keep the number.
**nacho** 10:19 Yeah, I think… I think it's better, right? Keep in sync.
The numbers, because we are…
**Bryce Buchanan** 10:25 Keeps things a little bit warm. Yeah, that's fair.
**nacho** 10:28 I think I… And I think we also released, 2.4.0, and we removed that, or was only on-core? I don't remember.
**Bryce Buchanan** 10:35 Okay, okay.
**nacho** 10:38 yeah, I think that… It's already pointing through 2.4.1, the project.
So the truth is that it should only be creating a release.
from… the source code.
**Bryce Buchanan** 11:10 Alright, so let's look at this other one, then.
the upgrade to Swift 6… Last week, verified on emulator, looks like it just needs to get reviewed now.
**nacho** 11:27 Okay.
**Bryce Buchanan** 11:30 And so I'll… I'll take a look after this meeting.
Lot of file changes.
But it looks like most of them are rather small, mmm, unchecked.
So we're just… I guess, okay.
**nacho** 11:44 Yeah, that the… Yeah, that's what they asked for, right? One of the issues that… yeah, one thing is building with Strip6, and another is that we are…
**Bryce Buchanan** 11:57 Supporting, yeah, supporting the new, things.
**nacho** 12:01 We are… we are concurrency, yeah, ready for everything. Yeah, but that's… that's another word.
But yeah, I think we should… Yeah, that will come, probably in a new… probably a new version, when we do… probably go into a 3.0, something like that would be great.
**Bryce Buchanan** 12:21 Yep, yep, sounds good. Alright, so let's see here. So, Ari started to work on… This changed the package to incorporate these changes in the spec, deprecating span events. Oops, that is not what I wanted to do.
I'll add Ari to this.
And… Oh my god.
Cool.
Okay, so, I'll start a, release… For the main repo.
Or at least, create a PR that updates the… the core version.
**nacho** 13:25 Oh, I think that's merged already.
**Bryce Buchanan** 13:26 Oh, is it? Okay, cool.
**nacho** 13:28 I think so, yes, yes, I think we matched that in the…
**Bryce Buchanan** 13:35 I'll verify that.
**nacho** 13:37 Yeah, I think in the packet it suits so already.
Pointing to the… to the new one.
So it should… if it's that, it should just be a… Yeah, at a release.
**Bryce Buchanan** 13:55 Okay.
Alright, any, any other topics that you want to discuss today?
**nacho** 14:12 Yeah, not much. Yeah.
**Bryce Buchanan** 14:16 Okay.
**nacho** 14:17 Yeah, let's, let's review what…
**Vinod Vydier** 14:20 So, so we were gonna have some, warning, right, for the AI… PR's… AI-generated PR, are we gonna add that?
**Bryce Buchanan** 14:31 Say what now?
**Vinod Vydier** 14:33 We… we were… last couple of weeks, we were talking about, you know, PRs that are… AI-generated, or there's, Some kind of sort of a… Notification, at least.
They'll clean it up before they send it.
**Bryce Buchanan** 14:57 I mean, yeah, I don't know, like, I feel like it's just a… it's, I don't know if there's really any need to make any notifications about it, or anything like that. I think it just, you know, just when you review stuff, just, you know, if there's… a bunch of… I don't know, if it's a messy PR, it's a messy PR, right? So just… Give the feedback.
That it needs to get cleaned up.
Hey, Billy.
Alright, so let's just, Let's just go through the, the issues in the main repo here.
So, support recent updates from Swift Log.
Reason versions of SlithVlog have, changed the API for a log handler.
What is SwiftLog?
Is this, Is this our instrumentation?
For Swift Long.
Yeah, this one here.
And find my way back to where I was.
Okay.
**nacho** 16:34 Yeah, dude… This is the same problem we have with versions of third parties, right?
About the Swift versions that they support. That's the… That's my main concern about that.
Updating Apple libraries usually means… Many new things.
But yeah, it… It must be taken with care.
**Bryce Buchanan** 17:07 Okay. Does anybody want to take a look at this?
I know it's going twice.
**nacho** 17:20 I can, I can, I can take a look.
**Bryce Buchanan** 17:22 Okay.
**nacho** 17:23 I will try to take a look, yeah.
And save that.
**Bryce Buchanan** 17:27 It's more like a, yeah, kind of like a triage, right? Figure out what needs to get done, if it's feasible in the current state of things, that sort of thing.
**nacho** 17:37 Yes.
**Bryce Buchanan** 17:40 Okay, alright, crash.
**nacho** 17:46 Yeah, this is the one that… it has a PR fixing.
But, yeah.
And I asked for documentation in English, because my Chinese is a bit rusty.
Yeah, and he didn't answer, so, yeah.
**Bryce Buchanan** 18:07 Yeah, apparently.
**nacho** 18:09 Apparently, he… Yeah.
If he had asked his, his… He's AI in English, probably will document in English.
**Bryce Buchanan** 18:18 Isn't there another… there's two… there's two crash fixes, right?
**nacho** 18:22 Yeah, the same crass.
Fix it.
I mean, we have two… PRs that fix the same crash.
Yeah, this is the other.
Yeah, and it fixed the… And he fixed the documentation.
**Bryce Buchanan** 18:44 Okay, cool.
**nacho** 18:44 hint.
Two? So maybe we can… merge this, and have you… yeah, did this… This basically changed the way that the information is preserved from the system, and just catches that value. And… and until the system calls, it's not updated, because the thing was that It was a risk condition there.
So it's good for me, it's good, so we can… we can approve and merge if we want, but I don't know if we want to do that before the release or not.
It could be.
**Bryce Buchanan** 19:20 I think we should, I think we should.
**nacho** 19:22 Yeah, it's a fix, and yeah.
If at least two different persons are reporting this crash and fixing it, it's because there are users of this, definitely.
**Bryce Buchanan** 19:33 Yup, yeah, so let's… Let's approve this then and merge it.
**nacho** 19:54 And we can close the other.
If we want…
**Bryce Buchanan** 19:58 Yep.
**nacho** 19:59 And, say, fixing another, or something like that.
He was the first to create a PR, so I was waiting him to update his documentation so he will be there, you know?
**Bryce Buchanan** 20:21 Yeah, but…
**nacho** 20:22 the…
**Bryce Buchanan** 20:22 Did not respond.
**nacho** 20:23 He didn't respond, so yeah.
**Bryce Buchanan** 20:26 Yep.
Okay.
Alright, so hopefully that'll close once that's merged.
Okay, so change to the package to incorporate, okay, so…
**nacho** 20:50 I think this is the ordinary.
**Bryce Buchanan** 20:51 Yep. Cannot assign values of type 64.
**nacho** 20:59 Isn't this…
**Bryce Buchanan** 21:05 Seems like Ari's working on this one.
**nacho** 21:08 Yeah, this is the 2-4-1. This is fixed with the new release.
Yeah, this will be fixed with this release. The thing is, the monotonic clock that… Had a different type.
**Bryce Buchanan** 21:27 Yeah, yeah.
**nacho** 21:28 Needed, yeah, so that will be fixed with the new release.
**Bryce Buchanan** 21:32 Okay.
**nacho** 21:34 And the rest, I think, are… quite old.
**Bryce Buchanan** 21:39 Okay.
And January. Okay, let's, let's go to core… oops.
**nacho** 21:46 And, and Pierre, have you… have we checked Pierre here?
**Bryce Buchanan** 21:49 Oh yeah, let's check the PRs too, okay.
**nacho** 21:51 Or, or…
**Bryce Buchanan** 21:52 Alright, so, move… Yeah. Okay, yeah.
**nacho** 22:04 Yeah, we can probably remove hosting.
Hmund.
But even…
**Bryce Buchanan** 22:09 Is this a, oh, it's a bot. Okay, alright, well…
**nacho** 22:13 Yeah, it was about… yeah. About, are we putting Alolita as a…
**Bryce Buchanan** 22:20 Should we remove… should we put her in there?
**nacho** 22:22 Yeah, I don't think this is the proper place, but yeah.
And yeah, and we are not…
**Vinod Vydier** 22:32 So the bot created this automatically?
**nacho** 22:34 Yes, it's fun. Yeah. Probably the vote doesn't know that Talolita is in the committee.
**Bryce Buchanan** 22:46 Should this be removed here, or…
**nacho** 22:48 Yes, I think we should remove outstanding.
**Vinod Vydier** 22:50 Yeah, he's not being.
**nacho** 22:51 I don't know why he was still there.
We have VNOT, and… and I think Billy is not there either in… I think.
He was… oh, sorry, yeah, he's there, sorry.
**Bryce Buchanan** 23:04 Yeah, he's there. Yep, yep, yep, yep.
**nacho** 23:05 Okay.
**Bryce Buchanan** 23:06 That looks good to me!
**nacho** 23:09 Yeah, that looks good.
**Bryce Buchanan** 23:10 And… Oh, there it is.
**nacho** 23:24 Oh, what do we have? Okay, yeah.
**Bryce Buchanan** 23:33 I will approve my own PR.
Okay.
Okay, so update… OTel log handler, okay, so this is, related to that issue.
**nacho** 23:46 Okay.
**Bryce Buchanan** 23:46 Wait, it looks like there's already a.
**nacho** 23:49 There is happier. Okay, then I can take a look here.
**Bryce Buchanan** 23:51 Yeah, cool.
Oh, here, let me, oh, it is a, it is a… Draft, it looks like.
Swift metrics… I think this is fine, we could probably approve this one.
Oops.
**nacho** 24:23 Yeah, I don't know, yeah, the thing… Yeah, I know.
**Bryce Buchanan** 24:31 It doesn't seem like there are any issues with the build.
And then just a bunch of chores that need to get…
**nacho** 24:41 Yeah, that, yeah, that's right.
**Bryce Buchanan** 24:42 Yeah.
**nacho** 24:44 And we have the Swedish rooted tracing bridge.
who…
**Vinod Vydier** 24:50 So, so chores, chores did need to be just reviewed and approved as for the two… So this creates appears, yeah.
**Bryce Buchanan** 25:02 Yeah, this makes… this makes sense. Because yeah, this is something that we've not really concerned ourselves with since we've been focused on front end, and now that Zwift is being used in the back end, this makes more sense to add.
So…
**nacho** 25:18 Exactly.
**Bryce Buchanan** 25:19 Yes.
**nacho** 25:19 He's working on… on that, yeah, he… he had a problem that, in Apple's… tracing library, he could add links after the spam was created.
**Bryce Buchanan** 25:34 Right.
**nacho** 25:35 I think he… and I told him that he could just update the API for that, because we checked there were no limitations in the spec about adding span links.
**Vinod Vydier** 25:47 After cleaning.
**nacho** 25:47 it has been created. Okay. So, probably that changed since it was created. I don't know. Maybe the spec changed there. But yeah, so I asked… I told him to do that, and I think he created a PR in the core for that.
**Bryce Buchanan** 26:03 yeah, cool.
So that's… gosh.
Alright, I can go through this after the meeting and get these all merged, at least the ones that make sense. Like, these Prometheus and, like, Collector things are not critical, they're not in, like, critical paths or anything.
**nacho** 26:24 Yeah, most of these are just for that pace, right?
**Bryce Buchanan** 26:27 Yeah, yep.
And the, the, demos.
Alright, let's go over to SwiftCore now.
**Billy Zhou** 26:33 It, for this, I also updated the 76 on PR.
**nacho** 26:40 Yep.
**Bryce Buchanan** 26:41 Yeah, we saw that. Is it on here? There it is.
**nacho** 26:46 It's, yeah.
**Bryce Buchanan** 26:47 Yeah, we actually, we actually already looked at it. We just need to review it.
**Billy Zhou** 26:51 Okay.
Yeah, he needs another pass, but, it's, like, working and stuff.
**Bryce Buchanan** 26:59 Yeah, it's quite, quite a big, big change.
But I think, I think what we'll do is we'll, try to get that one into the next release, Billy, because we got, some stuff queued up.
for the, 2… what is it, 2.6.1 or 24.1? 24.1.
**nacho** 27:22 Yep.
**Bryce Buchanan** 27:22 And so we're gonna… we're gonna get that one out, and then we'll get that merged.
**Billy Zhou** 27:27 Okay.
**Bryce Buchanan** 27:35 Okay, so, This is, a nitpick.
I'm gonna just close this one.
**nacho** 27:49 Yeah, I think so.
**Bryce Buchanan** 27:56 And Swift concurrency migration… Yep.
**nacho** 28:08 Yeah, basically it's the concurrency thing, right?
**Bryce Buchanan** 28:11 Yep, yep.
**nacho** 28:12 We asked Swift Six… Buildable, but not, concurrency.
**Bryce Buchanan** 28:17 Concurrency, compatible, yeah.
**nacho** 28:19 Yeah.
**Bryce Buchanan** 28:20 Or at least, I guess… .
**nacho** 28:24 Yeah, but…
**Bryce Buchanan** 28:24 particularly, you know.
**nacho** 28:26 Yeah, we need to go step by step. I'm making many things send double as much as possible on that, but… We cannot change everything.
Yeah, he wants to put Alolita.
**Bryce Buchanan** 28:48 So they bought.
Okay, okay, that's the entity one that I added.
I don't think… that this will hurt anything, necessarily. We could potentially merge this. I'll have to… I don't think there's any tests for it, so maybe I'll add some tests and then, And then.
**nacho** 29:20 Yeah, because it's yes, additive, right?
**Bryce Buchanan** 29:23 Yeah.
**nacho** 29:23 So maybe, yeah.
**Bryce Buchanan** 29:25 I'll double-check to make sure that the spec hasn't changed at all. I think that's why I didn't really want to merge it, because it was still kind of up in the air.
Okay.
But, yeah, maybe I'll get that done by next week.
Okay, allow adding links, okay, that's that.
PR, So, add link, add link on the propagated span… I had… That as a API method, looks good.
span SDK, add link… Has a lock… Yep, yep, yep, yep.
Which… which is using a span data link…
**nacho** 30:20 One thing there is… one thing that… The internalist recording.
**Bryce Buchanan** 30:27 Hmm?
**nacho** 30:28 If not internalized recording.
**Bryce Buchanan** 30:31 Internal is recording. I don't know.
**nacho** 30:34 What's that about?
Internally recorded.
So it cannot add… I mean, because if it… I don't know what that value is, because it… he wants it to work while… started? Isn't they recording what?
Keeps that the span is active, or what?
**Bryce Buchanan** 30:58 I mean, it's… I think it's just the… the variable that we use to check if it should record spans or not.
Yeah, see, it's used in the set attributes as well.
**nacho** 31:20 Oh, okay, okay.
**Bryce Buchanan** 31:21 So…
**nacho** 31:22 That makes sense, yes.
**Bryce Buchanan** 31:23 Yeah, I think that it's… if it's… if it's ended, then it doesn't want the span to be updated.
I think, essentially, that is what dictates that, although it's weird that it's not… in here somewhere.
Oh, it's because I haven't gone far enough up. There we go.
There it is, yep.
**nacho** 31:48 Okay.
**Bryce Buchanan** 31:49 Yeah.
Yeah, so that makes sense to me.
**nacho** 31:53 Yeah, that, that, that makes total sense, and the…
**Bryce Buchanan** 31:56 And then some nice tests.
Fabulous. This looks good to me.
If you wanna… I'm gonna… I'm gonna approve it, but if you wanna take a look through it, as well…
**nacho** 32:08 I think it… No, I think that that works perfectly, yeah.
**Bryce Buchanan** 32:13 And…
**nacho** 32:14 It makes sense, and it passes it.
What's it.
**Bryce Buchanan** 32:17 some issues here.
**nacho** 32:19 Hmm, okay.
Yeah, but this is the… but this is the other. This is not the…
**Bryce Buchanan** 32:29 Oh, how did this happen? Yeah.
Oh, I see what happened tonight.
**nacho** 32:34 Yeah, he did… yeah.
**Bryce Buchanan** 32:35 How can I get over here?
**nacho** 32:37 This was related.
**Bryce Buchanan** 32:38 Oh, I see, I think I might have accidentally clicked one of those or something, okay.
**nacho** 32:42 Yeah.
So, if it passes the test with…
**Bryce Buchanan** 32:46 Approve and run. There we go.
**nacho** 32:49 Then it can be merged, yes.
**Bryce Buchanan** 32:50 Hmm.
Cool.
Apply default view when no user view matches.
But I don't know if that's what we want to do.
Right? Like, the whole point of views is you want to be able to configure it to filter out metrics you don't want.
So… If no view matches.
**nacho** 33:19 You are not.
**Bryce Buchanan** 33:20 then… then you don't… Yeah, that implies that you don't want that metric to be… to be recorded.
Rather than automatically recorded.
**nacho** 33:31 Okay.
But it says the instrument default registered view.
**Bryce Buchanan** 33:39 Okay, well…
**nacho** 33:42 There is, like, a default viewport in your setup, or something like that, maybe?
**Bryce Buchanan** 33:47 Well, the default… well, I'll have to look at this a little bit more closely, but that was my interpretation of it. If it has no view, take an instrument and apply the default aggregation based on the instrumentation kind.
I'll have to… I'll have to double-check this.
**nacho** 34:11 Yeah, I think he meant, you know, something about it having a default one.
**Bryce Buchanan** 34:17 Oh, yeah, yeah, maybe… yeah, maybe that's the problem, is that, like, if there's no… well, hmm… I'll have to look at it. Yeah, it'll require some digging in.
**nacho** 34:27 Okay, yeah.
**Bryce Buchanan** 34:35 Okay.
Okay, this improves our invars. Again, something that we have neglected, because invars don't really work on iOS.
Yeah, okay.
**nacho** 35:05 Yeah, I'm… Yeah, I'm not sure about that. Yeah, I…
**Bryce Buchanan** 35:12 Yeah, I mean, this is… this is for, yeah, server-side, which, you know, server-side stuff.
**nacho** 35:19 No, you…
**Bryce Buchanan** 35:20 bars.
**nacho** 35:21 Yeah, you can also use that, for example, if you are doing testing, or something like that.
**Bryce Buchanan** 35:26 Testing, yeah.
**nacho** 35:27 In a, in a simulator.
**Bryce Buchanan** 35:29 Well, the…
**nacho** 35:29 Something like that.
**Bryce Buchanan** 35:30 Yeah, well, the scary thing is, though, is that if you… You know.
configure your system to run with NVARs, and in tests, it depends on NVARs, and then those NVARs don't exist.
**nacho** 35:46 Yeah, I mean…
**Bryce Buchanan** 35:46 You're gonna run into problems.
**nacho** 35:49 Yeah, you just use… I mean, yeah, I use mbars for running in Xcode and testing, because mbars, you can set them in Xcode for that, yeah, but… And it's you.
Maybe, also, you can now run suit process?
I don't know how that works, but maybe you can run some sort of process with MBARS?
And it will work also?
**Bryce Buchanan** 36:13 Yeah, maybe.
**nacho** 36:14 Because if…
**Bryce Buchanan** 36:16 Yeah, it looks.
**nacho** 36:17 But you can't run some sort process in an app.
**Bryce Buchanan** 36:19 do.
**nacho** 36:21 By the end.
**Bryce Buchanan** 36:26 Lots of reviews to do.
Billy, did you see this minor nitpick from Ari on this… on this issue?
I think that's…
**Billy Zhou** 36:53 Why does the OpenGR3K is crashing this, just trying to find time to do all this, since I'm not stuck on iOS anymore.
**Bryce Buchanan** 37:04 Where's it at?
Precisely, just right.
I don't actually know where it's at.
**Billy Zhou** 37:14 Yeah, this week I'll, clean up both, KS Cache and this PR, since it'll only take, like, a couple minutes each. Cool. And then, yeah, and then this FP6 thing probably just, just needs a revision or two, but, I was just glad it was, like, working end-to-end.
**Bryce Buchanan** 37:30 Cool.
Yeah, we'll try to get a… or I'll try to get a review on that Swift 6 stuff as soon as I can.
**Billy Zhou** 37:38 Thanks. Yeah, and then, I also just need to test it on some physical devices, too.
Yeah, so if anyone else wants to do that too, then please…
**Bryce Buchanan** 37:47 Okay. Thank you. Yeah. I'll try to… I'll try to get that done.
Alright.
I think that… pretty much covers everything, or did it… yeah, those were… these are all the PRs here.
And we went through the issues already? Yeah.
Boba, this is… This is the main repo again.
Oh yeah, there are only a couple of issues, yeah.
It's currency migration… alright, I think that's everything.
Alright.
Review those PRs. Chop chop.
**nacho** 38:26 Yes, true.
**Vinod Vydier** 38:28 Good.
Yes.
**Bryce Buchanan** 38:30 Alright, bye everybody.
**nacho** 38:32 Right.
**Billy Zhou** 38:32 Right.
