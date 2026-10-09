SIG: Swift SIG
Date: 2026-10-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Nacho Bonafonte** 04:37 Hello, good afternoon.
**Bryce Buchanan** 04:39 In a nutshell.
**Nacho Bonafonte** 05:07 Okay, so yeah, the document is okay, I will add myself.
Are you driving it, Bryce, or…
**Bryce Buchanan** 05:22 Would you, would you mind running in Nacho? I, I'm not.
**Nacho Bonafonte** 05:25 answer.
**Bryce Buchanan** 05:25 Any of the… Yeah, correct.
**Nacho Bonafonte** 05:28 Okay.
You know, my English is not very good, but I will do as best.
**Bryce Buchanan** 05:32 laughs.
**Nacho Bonafonte** 05:33 So, yeah.
So, yeah, You can see the screen with it, right?
Okay, so, Let's go with topics from last week.
So, yeah, I don't… You can see my screen.
**Bryce Buchanan** 06:13 Yeah, we can.
**Nacho Bonafonte** 06:14 Oh, okay, sorry, yeah.
**Billy** 06:15 Yeah, I can see.
**Nacho Bonafonte** 06:16 you I'm not seeing you.
Yeah, no, I see. Now I don't know what it was doing. Okay.
So, Yeah, from last week. First of all, we we talked about moving open telemetry shift core. I'm sorry, sorry.
And.
First thing is we have, 2.6 0 version, for core and… And the main library, did you have time to test if it was working?
Any… anyone?
Oh.
Anyone could try it, that release specifically?
**Ben Joseph** 07:01 I… I did test out the 260.
**Nacho Bonafonte** 07:04 Okay.
**Ben Joseph** 07:04 Seemed okay. Yeah.
**Nacho Bonafonte** 07:06 Okay, yeah, great. Then I think we… I mean, because the release is created as pre-release.
Bryce, so I think we can, yeah, after this meeting, we can put it into release officially.
And that… I… I created the versions.
Bryce, but I'm not sure if I created the pod spec or the pod spec process properly.
I don't know how that was.
**Bryce Buchanan** 07:31 Okay, I can take a look at it after the meeting.
**Nacho Bonafonte** 07:34 Okay, yeah, great. But yeah, that… That's done.
The next topic from last week is the OpenTelemetry Swift core back into main library. I already created the PR. I moved everything into OpenTelemetry Swift.
This week.
The PR is done.
But it's failing.
some test on Mac OS. I don't know why.
I think there are some baggage tests.
that are failing on the CI. I have been… I have spent more time now trying to find the issue.
More than, more than it took me to… to… to… well, almost.
To port everything to the main repo again.
I think it's a baggage thing, I think it's some.
It was working on previous version on the core library, all the tests, and here I think it's failing because some Other test is polluting the… The… the… the baggage?
So, when we check in the… in the baggage tests that the buggage is empty when the test ends, it fails. And I think it's because there is some buggage.
But I couldn't find it.
But apart from that, at least on my… and only fails on CI.
In my… in my laptop.
Which may be because it's still an x86, an Intel machine, instead of.
of ARM, sorry, ARM, which, you know, behave a bit different with threads, something like that. Maybe it's… Yeah, something is failing, I don't know why, but I will continue trying to address that. But if any other can take a look.
and find the issue in that PR, it will be great, and we can, merge that when it's approved. Basically, it took everything from, core.
I also updated minimum iOS versions as we talked last week. I posted in the channel.
about using a minimum iOS 15 version.
So, I think we can move to Xcode 26 as a minimum supported version, so I also changed the package.
That's Swift to 6.2.
Which is the version that came with Xcode, 26.0.
And iOS 15, I think it also allows us to use.
from the OS fair lock on Mac and iOS by default, which is much better than the locks we are using from Pthreads.
That's also ideas for improving the code from now on.
And probably… Maybe, you know, API and SDK, the templates and protocols have more options now, better allow using.
some or any in the types, so maybe we can also clean up the API and SDKs.
with those changes. But yeah, that's for the future. Basically, this PR does that.
Just bring this and update a minimum version and sweet version.
But as I said, still something failing only on Mac tests.
on the CIA.
So yeah, that's the only thing apart from approving. But yeah, that's the only thing missing.
So yeah, that's the second point, the minimum iOS 15. I opened the thread in… I mean, we are still have not merged, and we have not released with that, so… We can always go get back to something older if needed, but yeah, I think it's all benefits for us, just simplify as much as we can and just, You know, our resources are not very high, so yeah, let's… Let's continue.
Trying to reduce our maintenance as much as possible.
For now, I don't… I have not created any change for OpenTelemetry Swift Core.
Because we plan to only As was talked, just copy the code.
that we have in OpenTelemetryShift there, keeping a simple package and not having anything more there. No actions, no nothing, no tests, no nothing, just… Yes, the… The code, dumped, but we will only need that whenever we release.
Or even then, we can wait a bit more whenever we release a new version of the three brands… of the three versions that, yeah, that will be the new number we will use with everything integrated.
are stocked. If anyone has any issue or any problem with that, just… Raise your hand, or ping me, or just stop me talking.
Yeah, so apart from that is the integration test for iOS and sample app that was a B-list PR with a sample app that tests Pentalameter Swift.
what's… The status of that, I think you have updated things recently, Billy?
**Billy** 13:03 Yeah, I think there was some, like, rebasings or something since last week, Anyways, I've updated it all.
Should be ready to, merge in.
I've, like, put together, like, a quick plan, which I've listed, you know, the new topics of, like, stuff I'd want to contribute in October.
Long story short, I kind of just want to finish up streaming everything I did for AWS to kind of like close this.
Out, and, obviously, like, update it for, like, everything that's, like.
Also, like, been, all the new stuff that's come out since, you know, end of 2025, there's all these new iOS versions, there's, like, new versions of KS Crash, so I've been updating that PR, and incorporating all the new features there. I have a short list of, like, instrumentations that I want, and obviously, like, we need the intake tests, like, all set up so that, like, all those can be, like, contributed in kind of smoothly.
So yeah, if you could take another look at the Intech test PR, that'd be great.
**Nacho Bonafonte** 14:15 So it should be ready right now, right?
**Billy** 14:18 Yeah, yeah, definitely.
**Nacho Bonafonte** 14:21 Okay.
So, yeah, if you can… Oh.
Yeah, talking about approving things. Yeah, there are also PRs, I think they have not been copied around. About, adding a progress access for Ben Joseph on this one.
Who… yeah, Yeah, we, we, we, I told last week that we still had not, taken, you know, we had not had time to, to talk about that.
Yeah, Bryce is also here. I have feedback from From… also from, Probably not who's not here, but yeah, you have been collaborating, helping with with the project lately a lot, and coming to the meetings, and doing a lot of work. So, yeah, the idea… And this is approving.
You can see Bryce is also nodding.
nothing is Is that right? I'm not… using the wrong word, yeah, okay. Yeah, so that, that, that, that's also something, congrats, to… Then you have progress.
Yes.
Okay, so yeah, if you have… time, not only the new approvers, anyone, and want to… now we have to approve that and do that, so it will take some time, but yeah, that… That's just a matter of time now.
**Vishwan aranha** 15:55 sounds.
**Nacho Bonafonte** 15:55 Of the process of approving.
**Vishwan aranha** 15:57 Yeah, when you get a chance, like, I just wanted to bring it to attention. I think Benz has one approval. I was out the week when, Ben, I was given instructions how to do it, but I added my PR, so when you guys get a chance as well.
**Nacho Bonafonte** 16:10 Okay.
**Ben Joseph** 16:12 Yeah, thank you guys.
**Vishwan aranha** 16:14 Thank you.
**Nacho Bonafonte** 16:16 Yeah, I mean, it's not… Thanking anything, it's like… You know, you have been really… helping in the project, doing lots of work. It's, you know… All that can help the project is more than welcome.
So, yeah, that… That, that's… I mean… That's it. So yeah, the PR, from… I think it has been already addressed, lots of feedback.
I need… is now working… All checks have passed. 617, that's a lot of checks.
Congrats, really.
So yeah, if you want to take a look, any other feedback there, just to… to get some more approvals. If not, we can land it. It's not production… I mean, it doesn't impact on production, so… do you want to take a… Further look, or do you prefer to merge it and let it You know, review after Merge and improve in the future.
**Bryce Buchanan** 17:26 I think it's fine to merge in.
**Nacho Bonafonte** 17:33 Okay, then.
I will remove all this.
Okay.
So, one thing less than,
**Billy** 17:50 Thank you.
Nice.
**Nacho Bonafonte** 17:59 Just taking the notes here of what we have done.
Oh, sorry.
Sorry for capitals.
**Billy** 18:32 Yeah, in that case, the KS crash PR should be updated shortly as well.
**Nacho Bonafonte** 18:41 Yeah, the… okay, we can… is that here in the topics, the PR?
**Billy** 18:46 Oh, yeah, yeah, sorry, I was jumping the gun a little bit.
**Nacho Bonafonte** 18:48 If you can bring… it's just easier for… I can search for it if you want.
Oh.
**Billy** 18:56 Yeah, we can go over the whole plan if you want, if you want. I just wrote down a list of things, for October. Okay.
**Nacho Bonafonte** 19:03 Yeah, okay, this is your instrument… okay, this is… Your plan of developments, right?
**Billy** 19:11 Yeah, I just dropped it all in that comment since that's like what people have been asking. I can like separate it into like different issues and stuff.
But.
And there's also, like, probably other things that I'd want to, just, like, include, but, Long story short, the first part is just getting the intake test set up, and we also have, like, the, The thread sanitizer test from the week before, or something like that.
Most of this stuff I already did once before for AWS, so, like, I linked all those PRs from before as, like, what I did previously, and then… Obviously, those need to be upstreamed.
For, like, events, like, the main things, I think, that would have the most value add are, like, obviously crashes, but then app launches, app hangs, and then views, specifically for, like, SwiftUI and UIKit.
And then for attributes, I think CPU, memory, battery, and user ID are the most important ones to include.
there's, like, some miscellaneous stuff, like, I noticed that, just, like, the batching logic can be kind of bad, like, out of the box if you don't, like, set it up correctly. I don't know if I was, like, just, like, not doing it correctly, but, that's a pretty important feature. Session sampler, I think someone else is already working on this, so I just, like, referenced the other person's PR, and also what I did for… Aws, or is that a couple things that are out of scope, like user journey and, like, jitter, and I think there's, like, some other things that… I wanted to… I forgot to include here, but yeah, this is, like, the rough outline, if, like.
we're good with this, or if people, like, you know, want to, you know, address the, the scope, feel free to just drop a comment, and then I can start, like, separating into different issues and stuff.
Any any thoughts, guys?
**Nacho Bonafonte** 21:17 Yeah, it's Julia.
great set of features to add to the project. Yeah.
**Billy** 21:24 Nice.
**Nacho Bonafonte** 21:25 Really useful. Yeah, all of them, I mean.
**Bryce Buchanan** 21:30 They work really well.
**Nacho Bonafonte** 21:30 All the behavioral, all the events for the behavioral of Swift to UI, UIKit.
And I've… Lantern House, I think that that's really… really useful for… or RAM users.
A room, or… I don't know how to… Yeah.
**Billy** 21:52 Yeah, I guess it's still called Rome. Thanks.
**Nacho Bonafonte** 21:54 Yeah.
So.
**Billy** 21:56 Yeah, I mean, a lot.
**Nacho Bonafonte** 21:57 suffice.
**Billy** 21:57 Oh, thanks. I mean, like, there was, like, tons of people at AWS working on this, like, last year, so it was, like, a lot of people, you know, contributing.
A lot of this has changed in the last year, so I'll have to, like, review one by one, and, like, I'll raise issues if I see them.
Yeah, like, I'm just, like, randomly doing this, like, I'm taking a short career break for, like, October, and just wanted to get this out of the way. Like, I'm, like, full, you know… Transparency, I'm literally just, like, attending culinary school in Beijing right now, so I don't have, like.
All the time in the world, but I figured I should get this done.
**Vishwan aranha** 22:34 Congrats.
**Billy** 22:35 Get back to work next month, yeah.
**Bryce Buchanan** 22:38 Right on.
**Ben Joseph** 22:41 Yeah, this is very interesting work, especially, was very much looking forward to the CAIS CAT reporter work, being revived. So, yeah, looking forward to it.
**Billy** 22:52 Yeah, no worries. I'm, hoping to wrap up a decent version of it. It's, like, some… I think there's, like, a lot of new changes in, 2.6.0.
Which is, like.
So, as I was, like, rebasing it, I realized there's all these features that, like, we didn't even touch on. I don't know if Alex Cohen is, like, still around, but I should definitely like to chat with him again on some of this stuff.
Okay, yeah, feel free to, you know, drop me a message. I think, like.
Yeah, GitHub or Slack are both good.
**Nacho Bonafonte** 23:30 Okay.
**Billy** 23:34 Okay, sounds good.
Thanks.
**Nacho Bonafonte** 23:35 Yeah, really good.
So, next topics we have here… Yeah, these are… this one, Ben, these are PRs from These are the oh sorry.
**Vishwan aranha** 23:51 the.
**Nacho Bonafonte** 23:51 This is one.
Yeah, that's right.
I don't… Oh.
**Vishwan aranha** 23:57 Oh, I also added one.
**Nacho Bonafonte** 23:59 Already approved.
Oh, Bryce West.
Peter.
Yeah. Sorry.
**Vishwan aranha** 24:05 For the approver PR, we need, like, two… maintain.
**Nacho Bonafonte** 24:09 Yeah, to maintenance, I know, I know, yeah.
But now we do have the actual rate.
And the other.
**Vishwan aranha** 24:22 And I also brought up 1185, it's, like, session persistent work that I was working on, and there's one merge config, I'll just fix it and push.
And the idea is to give, like, traces, logs, and metrics more, like, like, shared sampling decision for a session, rather than, like, having them make, like, unrelated decisions and, like, losing parts of the picture, so it's… It's, I think, one of my last PRs for session, so…
**Nacho Bonafonte** 24:51 Okay.
**Vishwan aranha** 24:51 Yeah, if you guys have a chance, I'd appreciate any feedback on that API and, like, whether integration responsibilities are clear. Happy to answer any questions there.
When you get a chance.
**Nacho Bonafonte** 25:02 Yeah, I approved it already, but there were some merge conflicts here. Yeah, probably.
**Vishwan aranha** 25:09 Yes, yes, it just popped up from another merge. I guess I will just update that.
**Nacho Bonafonte** 25:13 Yeah, that's right, yeah. We have… in fact, we have currently Lots of, lots of PRs that have merged conflicts between them. We have many for URL sessions.
from the same user, Tomer Haven, I think it's his name.
that all of them have conflicts. One of them just made all the rest conflict, and he has not come back to update those. I tried to update one, and I failed.
So, yeah, sometimes you can… and some of them are not.
Change our… So, yeah, let's…
**Vishwan aranha** 25:55 Are those users active, actively updating or?
They just forgot.
Open key.
**Nacho Bonafonte** 26:02 He has not updated in a long time, I think. I don't know why. He dropped, like, lots of URL session, fixes, or… Not only fixes, but features.
But yeah, they are still under review. We can take a look now. Now we have only one project, right? We only… I already, we only have to take… One repository history, and… An issue. So, instead of 2.
In fact, for the core… Project just… I… I have not blocked PRs, I don't know if we can block PRs directly.
Of what was… Yeah.
**Bryce Buchanan** 26:52 You forgot the OpenTelemetry path.
**Nacho Bonafonte** 26:57 Oh, really?
which is this… Okay.
Yeah, we yeah, we added with the help of Ben. We added a note here.
to the README of Core.
Where it basically sees that we are integrating into the library, this… the main library.
We asked to all the development here.
And I changed this a bit from what Ben wrote, because I think it… is more friendly, that we plan to release, this as code dumps of the other, so that clear… clarifies a bit. That we plan to do that, that's true, and we plan just to be a code dump, but I think… you know, would allow them to really have their expectations properly. So that's it. For the PRs, there were some, I think.
Some of those PRs were from I don't have you have one here, and I.
**Vishwan aranha** 28:15 I just know.
**Nacho Bonafonte** 28:15 Both I didn't… I didn't drop.
But I answered in both to change the PR to the other repository.
**Vishwan aranha** 28:23 Yeah, I can update, yeah.
**Nacho Bonafonte** 28:26 Yeah, here, updated here, so yeah, that's right. I don't know if we can block this.
New pull request somehow.
But I can continue answering everyone, but I think just a note here will… should be enough, right, for people to notify.
So, yeah, let's go with… With the main library?
Do you prefer start… we can review, issues first.
From… Yeah, there are many old here.
But… I think all of them.
Oh.
are related.
These from one month. Okay.
I think they have a related PR.
No.
Stable HTTP error metadata.
Okay.
So, ProLab… So this is about the semantic conventions? Okay, yeah.
Yes, we are… a bit outdated on the semantic conventions, I think, and they have changed the way the semantic conventions were created.
But now that we are in a single repository once we… I mean, that's something we can wait for the… or the… Core libraries to land, because semantic conventions were in the… in that.
They were in the car.
So we must wait for that, but yeah, we should update The semantic conventions, and once that Probably address, Some of these, inconsistencies with the semantic convention.
Probably it's using the semantic convention first version that it had, because it was implemented so long ago.
The semantic conventions itself is a bit newer, but… Probably missing many things, especially for user client.
okay, this is, again, out conventions, so that… Needs a bit of time.
Exporter metrics can record multiple terminal outcomes from one HTTP export attempt.
Okay, this has a… This has appeared that was already merged.
Yeah, okay, so this is done, right?
Or was not fixed.
Okay, yeah, yes, yes, relation, yeah.
Okay, so… Okay, so probably he's addressing it himself.
Great.
Yeah, so let's… go to the… Yeah, he usually opens issues and fixes with a PR, just to explain the issues.
He's working on… Okay, so, pull request.
For this project, There are a bunch of them.
Yeah, this is the… Open Telemetry Core.
Transition.
Yeah, I'm… Many files changed, as you can see.
So basically, these are moving from the other project.
The thing here should be… It was just a copy, except… As I said, the packets on the minimum version.
So, yeah, the only thing it's… Currently, they release… Oh… It passed.
Last test I did passed.
The test.
Come on.
Really.
Yes, it's filling on Linux, okay.
Oh, but it… yeah, sorry.
It seems I fixed the last comment I did.
This morning here, before starting my work.
it looks like it'll work. So that's good news. So only reviews needed now. Once that is done, everything semantic conventions related could work. So, yeah.
I don't know why Linux is failing.
Probably… We should track that.
But I would like to, if possible, to be another.
Yeah, in another PR.
We are not releasing currently, so we can probably have that.
Without a proper… Working.
Ping.
Yeah, that's right.
Okay, yeah, this was another, PR, it's about… yeah, this is the one that came from the… This is about, yeah, using the active span, the new way for detecting that on the Swiss tracing bridge.
Okay, so yeah, it needs review.
Yeah, if you… this is for the AutoSwift tracing library from Apple.
Yeah, so, yeah, probably getting the active span.
Should be.
Nice thing to have also there, with the new changes.
This is a fit PR. It's about 17 decisions, right? This is an anthabe PR.
Any status here?
Do you need any… thing from… oh, he left the meeting. Yeah.
Okay.
So, yeah, probably… Yeah, it has a conflict here also, yeah. It's… He, I think he has some fears with Currently with conflicts.
So, yeah.
These are Renovate Bot.
Lots of Renovate bots.
Yeah, this is… One that has change requested.
I think this is the… Wasn't this the issue that it was, that it appeared?
But yeah, it was reviewed by Robert Northman.
Or Northmine?
And Bryce asked for some changes here.
So, yeah, I… yeah.
Once that's… Reviewed or approved, we can merge.
And yeah, and here there are lots of… Url session… Piers from Tomeri.
This, for example, has a change requested.
But… Most of them are.
Oh, it's much, but many of these URL session PRs here, have conflicts, because we merged some of them, and it started conflicting with the rest.
So, yeah.
And some things are not building. So, yeah, I think that's the review for all the PRs.
Currently. Do you miss any other?
The KS cast reporter, right, this is your Case traffic reported, yeah.
**Billy** 37:38 Yeah, I'm, doing the finishing touches here.
**Nacho Bonafonte** 37:42 Okay.
**Billy** 37:43 Hopefully I've addressed all the feedback, but, Yeah, I think there's just one more commit that has to go out, and then I can make it ready for review.
I was just getting the, the grouping and the, exception… the grouping resolved by using the, like, native KS crash message.
feature, and I was also adding the exception dot type.
thing from them, which actually doesn't seem that useful when I was using it, but I don't know, I think Alex mentioned last year that it was, like, important to them, so I'll just add it, If there's, like, other stuff… I guess, like, one thing we can discuss is that, like, the only, The schema of the crash is, like, pretty simple.
I think I didn't change it at all. If you go, if you scroll down, it's, and I just keep at this conversation.
I'll go back to conversation, please.
If you just scroll down to the example log, in the original description.
At the very… at the top.
**Nacho Bonafonte** 38:53 I'm sorry.
**Billy** 38:55 Yeah, it's in the original description, Just go down, below implementation section, I added, Just a little bit, yeah, below tests… Yeah, right here, if you go under, the normal attributes.
Yeah, I think the only things I added were exception.type.
exception dot stack trace.
And, not include… and an exception.message.
So, in here, so just… those are… that's, like, literally the whole full schema for it.
For exception.message, that's… changing from, like, this janky thing that I wrote last year for the native Chaos Crash thing.
Exception.type will just go to also their native feature for it.
And then Stack Trace is just exactly what it sounds like. I turned off their on-device symbolication.
Because there was, like, some feedback about it, but you can obviously opt into it. I think those three should cover most of it. If there's, like, other stuff, then please let me know, and then… Someone also caught last week that the… like, the string truncation was… logic was broken, but that was a good catch, whoever did that, so I fixed that as well.
Yeah, just one more commit, and then I'll just, drop a message in the Slack, and yeah, please take a look. Thanks, thanks guys.
**Nacho Bonafonte** 40:35 Okay, yeah, yeah, it looks very good. You know, you… At least on my view for for these kind of things is and you have. You've got my approval.
Early… Oh, thanks. I mean, long ago, before you added some of these things, even when there were some feedback, is that, at least for me.
Landing new, functionality into the project, even if it's not 100% ready.
We just notified that on the README of the project, or sorry, on the README of that instrumentation, configuration, whatever.
We say the limitations, we say this is beta, this is testing, and… and… and… And maybe we can iterate faster, right? Probably it's easier for you just, you know, have something landed and just fix small things, and iterate faster there, to… until we have something that's You know, accessible for everyone and production ready.
But if it's faster just having something early that still has some issues, but it can be useful, and it can help other people just improve your PR or fix their things. I think that that adds a lot of value. I mean, we are an open source.
project?
We are open and clear with what we have, so if we say this is still not production ready.
We don't mind having that there, right?
People will use that under their test and their use cases.
But if it helps us iterate faster, I am totally.
supporting landing things early. I think Bryce has a similar view there.
Because it helps a lot. I mean, maybe some people just.
**Bryce Buchanan** 42:24 the.
**Nacho Bonafonte** 42:24 having.
**Bryce Buchanan** 42:25 frequently.
Crashing anything.
**Nacho Bonafonte** 42:27 Yeah, yeah, that's right.
That's why I said new functionality, right?
**Bryce Buchanan** 42:32 It doesn't need to be complete, but if it's, yeah, if it has, you know, some useful features in it, it should probably get merged. I think that's good.
**Nacho Bonafonte** 42:41 I mean, if it's good enough to be useful.
let's land as soon as possible and make it production-ready later, with different iterations. Because, you know, right, for you, merging or conflicts now is much more difficult than if you just had to fix your own library. Those kind of things is what… what, yeah, let's make it.
Easier, than, you know, probably working on a… on a company that needs production-ready code only on the repository. We don't have those.
**Billy** 43:13 Yes.
**Nacho Bonafonte** 43:13 But we must document.
That… that's my take.
**Billy** 43:17 Yeah, I totally agree. And I think the improved test coverage that we introduced over the last month will help with that as well.
I think before it was, like, really easy to introduce crashes, but, Now we have… now we have TSAN, so… Hopefully it's gonna be better.
**Nacho Bonafonte** 43:41 Okay, yeah, you link this… He…
**Ben Joseph** 43:43 Yeah.
So, I don't know if everybody's aware, so there is this new, client-side repo being set up, that is kind of.
For Android, iOS, and browser.
So, the basic idea is that, like, any semantic conventions that is more client-side.
When we… when we want to try to merge something in the… into the core repo, it's already very established, and, like, it's difficult to merge or, like, get their approval. They probably don't understand the client-side semantics as much.
So the, the community has come up with the concept of federated semantic conventions.
essentially federated means that, like, there will be different levels. It's sort of, hierarchical, or, like.
model, where we will still have the, core or the original semantic conventions, and then, like, the client side will be maintaining a separate list. This way, like, they are not very much fragmented, but.
Still, still separate enough so that, like, there is flexibility and freedom to introduce new semantic conventions.
So that's basically the idea with the new, new client-side repo.
yeah, so I… they have been asking for some feedback related to some of the existing semantic conventions, how do we want to migrate them. I think there was… I'm not sure who was part of this discussion on renaming some of these things. I think there is also this idea that, like, we shouldn't be using any platform-specific names. Like, instead of iOS, we should try and probably use.
device, or app, or something like that, instead of platform-specific naming. So there is this effort that's going on, and I think they are asking for some feedback. So I think if you can take a look and provide some suggestions, that would be great.
**Nacho Bonafonte** 45:57 Okay.
**Ben Joseph** 45:59 So, in the future, I think, like, the expectation is that, like.
Instead of consuming just the core semantic conventions, we will be referring to this library, this project as well, for semantic conventions, and any new semantic conventions, we should support, raise a PR to this repo instead of the core semantic conventions library.
**Nacho Bonafonte** 46:21 Yeah, that makes a lot of sense for, yeah, quicker iteration.
on semantic comments. We… yeah, as I said before.
the semantic conventions process for our project is currently, I think, outdated, because they have changed, I don't know how many times, the way the semantic conventions are generated for each platform, and I think we didn't move from I don't know if the last one or the Previous to last one.
So yeah, we'll.
**Bryce Buchanan** 46:51 I've been relatively recently.
**Nacho Bonafonte** 46:54 Oh, really? Really?
**Bryce Buchanan** 46:56 mean.
**Ben Joseph** 46:56 Not the ocean bomb.
**Bryce Buchanan** 46:57 And then, like, the last year.
**Nacho Bonafonte** 46:59 the.
**Bryce Buchanan** 47:01 Yeah.
**Nacho Bonafonte** 47:02 They have had time to change method twice, at least in that year.
**Bryce Buchanan** 47:06 Yeah, I guess that's true.
**Nacho Bonafonte** 47:09 Yeah, it's very crazy how they… I mean, you… once you had a process with all the scripts and everything just more or less automated to change, and you had to rework everything again, install a new Docker images, and yeah, it was a bit… Yeah, it has been a bit crazy.
So I don't know if it works now, to be honest. I think Vinod was gonna also do something around that, but I don't know if he did that.
I don't know. Yeah.
So yeah, I don't know how that situation is. But once we merge the core library there, we will only have one repository to do everything.
That, that, you know… That's gonna be like heaven again.
**Ben Joseph** 47:57 Yeah, I can watch this and, like, you know, bring any more specific discussions that might be there, or any inputs.
**Nacho Bonafonte** 48:07 Yeah. Otherwise, I don't think…
**Ben Joseph** 48:09 Yeah.
**Nacho Bonafonte** 48:10 You, you… I think you are currently working.
on this, on production code, you are having these problems currently. Also, Billy, I don't know if you are also working on that, I think so.
So you probably… If you want to provide the feedback, totally open to… to you giving that feedback and solving the problems that you find every day or using, you know.
Your criteria for adding FinFactor.
At least from my side, it's totally okay.
You're gonna probably give better feedback than I will.
I've not been doing… drama stuff.
Oh, yeah.
I have never done it, to be honest.
I was in other kind of observability areas. So yeah, that.
Probably your feedback there will be more valuable than mine.
**Bryce Buchanan** 49:11 I'll take a look at this, too.
**Ben Joseph** 49:15 Yeah, I think it's testing.
**Nacho Bonafonte** 49:17 Experience that.
**Ben Joseph** 49:19 Yeah.
It's specifically targeting some, I think, maintainers, so that's why I brought it up.
I mean, maybe just some input here. There is nothing that we need to change in our repo at this point.
So, yeah.
**Bryce Buchanan** 49:37 Yeah, I think I proposed the original.
spec for the… for this, semantic convention, so I kinda… I'll have the context, and it… I mean, it looks fine to me, I think it makes sense, just based off of what's here, but I'll take a closer look at any feedback, or just give a thumbs up if it looks fine.
**Ben Joseph** 49:59 Okay, perfect, thank you.
**Nacho Bonafonte** 50:05 Okay, any other topic?
No.
Everything okay?
Yeah, so… Great, just, yeah, let's review… The PRs that are missing, Yeah, you can then ping Aranjave.
About the conflicts there, just for a minute.
**Ben Joseph** 50:35 Yeah.
**Nacho Bonafonte** 50:36 It's not that.
**Ben Joseph** 50:37 Yeah, I see.
Sorry, he had to drop for another meeting.
**Nacho Bonafonte** 50:39 Right now. Yeah, no, no worries. I mean, it's not… it's just…
**Ben Joseph** 50:42 here.
**Nacho Bonafonte** 50:43 That, yeah, at least some of them are just waiting for the conflict to be solved and re-emerge.
**Ben Joseph** 50:49 So.
**Nacho Bonafonte** 50:50 On the new library, so that's right. And, yeah.
And please, if you can, review.
The core library merge.
That will be… that will be awesome, and we can just continue with, yeah, with newer stuff there.
**Ben Joseph** 51:08 Okay.
**Nacho Bonafonte** 51:08 Great. So, yeah, 10 minutes back for you.
Have a nice weekend. See you all next week.
**Ben Joseph** 51:18 Thank you all. Bye.
**Bryce Buchanan** 51:20 Bye-bye.
**Billy** 51:21 See y'all. Thank you. Bye.
