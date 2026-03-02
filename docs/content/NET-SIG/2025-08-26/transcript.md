SIG: .NET SIG
Date: 2025-08-26
Duration: 35 minutes
Zoom Recording URL: https://zoom.us/rec/share/8RgOHIxCaFe79px0vxdvvjizzkIaDpgFsqmQj6DJ4bvhSRvB4b26aAQNLd4spkzA.Yy_EuhxQFQ4K9jxQ
============================================================

## Zoom Recording Transcript

**Rajkumar Rangaraj** 02:30 Hello, everyone.
**Martin Costello** 02:33 Alright.
**Alan West** 03:42 Damn.
**Rajkumar Rangaraj** 03:59 Sorry, my head, my speaker did not work, and I did not hear anything, for some time. Are people able to hear me now?
**Martin Costello** 04:09 Yep.
**Rajkumar Rangaraj** 04:09 Yep.
So, let me share my screen, and then we could start the discussion.
Today, I want to bring up two topics for discussion. I think we have the PRs for both of them, and Martin had created that. I remember Blanche earlier gave me a heads up on one of them.
Was discussed earlier, but, decided to hold on until I returned back.
So we can first go with the .NET 10 release challenges and everything, and then we could have the discussion on the second one. Martin, do you… I know you… even just before
starting this SIG, I saw you pulled, sorry, you pushed some commits to that. So, I just want to understand, are there any challenges, in supporting the .NET, 10?
**Martin Costello** 05:22 Only that with Preview 7, there's a bug that means that the main repo doesn't build.
I reported the bug, it's already been fixed, it'll be fine in our C1.
**Rajkumar Rangaraj** 05:37 So it will be a part of the RC1. Okay, so that's what I wanted to check with you.
… So, do you see any other issue apart from, that?
**Martin Costello** 05:48 There was one… there's one breaking change in .NET 10 that caused the W3C chip tests to fail, but I just refactored the tests so that they don't.
**Rajkumar Rangaraj** 06:00 Okay.
Yeah, tests are not a major concern unless and until, like, if the
the SDK is not impacted, SDK and the other components are… stable components are not impacted, we should be good, I believe.
**Martin Costello** 06:14 Sure, it just might generate questions from users if they update to .NET 10, and they get, the diagnostic source version 10 DLL via us.
And they rely on the W3C…
behavior, then their app will break, but then all we can do is go, here's the breaking change notes from .NET 10, make this change if you don't want it.
**Rajkumar Rangaraj** 06:45 Got it. Maybe in our, release notes, we may need to call this out, saying that that is this change. That would also help.
net is breaking here.
I would say once the RC1 is released, we may also need to plan to release the next version of the SDK with a beta stamp on it, so in that way, the customers could
Like, test it and provide a thumbs up or feedback for us.
So that will give enough confidence for us to ship the support for .NET 10 when… once it's released.
I'll create a milestone for that, and I'll, … I'm going to add this.
Under that umbrella.
**Martin Costello** 07:37 Okay.
**Rajkumar Rangaraj** 07:39 So I don't, … I did not check the RC1 timeframe yet. I'll go and also check the RC1….
**Martin Costello** 07:48 I imagine we'll get it on the 9th of September if they follow Patch Tuesday.
**Rajkumar Rangaraj** 07:53 Okay.
So, by the end of that week, probably we may plan to, merge this PR and then, do a beta release of…
Whatever is pending, till that point.
**Martin Costello** 08:07 Awesome.
The only concern I have with that is if we do that, and we have to release any version of anything.
isn't beta, it'll be built with a… with a non-stable SDK.
**Rajkumar Rangaraj** 08:23 We did last time follow a strategy of having it, you know, we did not break the entire workflow, so we will revisit the same strategy and ensure that the main is not impacted with the RC version that we bring and everything.
**Martin Costello** 08:43 Oh, sure, it's just in case there's a weird bug in the compiler.
that breaks non- .NET 10….
**Rajkumar Rangaraj** 08:51 TFMs, because it's built with a release candidate. That's… that's all I'm saying.
Yeah, I got it.
Cool. I think we can… if there are any other questions around this .NET 10 support.
If not, I think we can move on to the… … Next topic.
Okay, so everyone is quiet, I'm just going to move on to the next one. Martin, I see you have the…
John.
other PR also.
So…
And this requires, proper thought to be put into it, because last time just caused an issue for many people, and we have an issue which tracks that.
So just want to… Here, what's the, like, proposal here?
**Martin Costello** 10:02 the TLDR is the proposal, is that
either… I think… if I remember correctly, it's going to be the second one of the two things I'm going to say, because it's been a while since I've looked at this issue. The proposal either…
the versions of the libraries match the TFM, with one exception, because it's already depended on changes… 8 is already depended on changes from 9, or the proposal is everything gets frozen at the point they are now.
But going forward, they always match the runtime version. So, 10 will stay with 10 forever, 9 will stay with 9 forever, 11 will get 11, etc.
**Rajkumar Rangaraj** 10:44 That does make sense. The reason is, all of these are special framework libraries.
If someone uses… even they have 10 packages, they should not be worried. So in the .NET customer wants, they can bump it, but we should have a test
that covers and ensures that in the .NET 9, if we are using a .NET 9, and if customer bumps the… any of these Microsoft extension packages to
…
10 version, so we need to ensure we don't break anything with that. So that's a test we need to ensure.
**Martin Costello** 11:23 Do we? Because even the .NET Frame teams don't have that big a compatibility matrix.
**Rajkumar Rangaraj** 11:32 I am not sure. If customer comes and complains as saying that, him, I went ahead and, I started using the….
**Martin Costello** 11:40 So if a customer is using 9, they manually upgrade it to 10, and it stops working. Unless they can prove it's open telemetry, then it's Microsoft.net support ticket.
But also, if they upgrade it and it doesn't work, then don't upgrade it.
**Rajkumar Rangaraj** 11:59 Yeah, let me give a scenario here. So, I have an app which is targeted to run only on the .NET 9 version.
So I go ahead and update the Microsoft extension logging configuration
to 10-no, but I'm not bumping any of my framework or anything. So, still, the NuGet allows me to do that. So, if some customer, for some features, if they go ahead and enable that for the additional features.
So, that is not a tested scenario in our case, if we go with this approach.
**Martin Costello** 12:36 That's true, but the person opted in to do that, and just because NuGet lets them do that doesn't mean it will work.
Because people… I've had several issues opened on the Swashbuckle repository of people trying to update Microsoft.openAPI version 2, and it fundamentally does not work. But NuGet will let them try and use it. But that's not my problem.
**Rajkumar Rangaraj** 13:04 But that creates a supportability headache for us, right? It's a maintenance or, like.
**Martin Costello** 13:10 No.
**Rajkumar Rangaraj** 13:11 We've been found.
**Martin Costello** 13:12 If it… it does, but if it doesn't work, it doesn't work.
Because, like, we could test for it, and if it doesn't work, we can't do anything about it, if it's a fundamental issue in the .NET runtime.
I think if you try and test every possible combination, you're going to explode the CI matrix.
**Rajkumar Rangaraj** 13:30 That's also true.
Eleanor Blanche, do you have any thoughts here?
**Mike "Blanch" Blanchard** 13:39 Wasn't paying close attention.
**Rajkumar Rangaraj** 13:41 What was it?
So, the thing is that, there is a plan, like, to align the, these Microsoft extension package versions to the runtime package versions. For example, with the .NET 10
release, like, we will only include the… so for… we will update the Microsoft extension only for the .NET 10, but not for the .NET 9.
Or 8.
So, that's the plan.
So… I want to take your thoughts on, … it looks fine with me, but want to just check.
your thoughts and Ellen's thoughts on it.
**Mike "Blanch" Blanchard** 14:21 I like it. I mean, I think that's kind of what Alan and I originally wanted, but…
We went a different direction.
I don't remember the details of that. I mean, I know, like, Riley talked to the .NET team, Noah…
Like, there's all these little comments in here…
Noting why we have the policy.
So that's really my concern, is just that, you know.
Riley understands why we're changing the direction.
Because this was really something he worked out with the .NET team. So we need to make sure we…
Clearly document, you know, why we're making this change.
I think the fact that the Aspire team also made the same change.
**Rajkumar Rangaraj** 15:14 Yep.
**Mike "Blanch" Blanchard** 15:15 is important. So, like, you know, they did the same thing we did, they rolled it out, their customers gave them whatever feedback, and they adopted this policy. I think it's the right policy. Just want to make sure it's…
You know, it's clearly documented why we're doing this again, because it seems like every couple years we switch this, and, you know, some subset of users
either way we go is going to be angry or dissatisfied, so that's more of my concern. I think the direction is good, I just want to make sure we clearly understand it, the impact, we have it documented, and there's clear understanding why, if that makes sense.
**Rajkumar Rangaraj** 15:57 Yeah, what I was discussing is, like, there will be a one set of people who come and complaining. That's what I was giving a scenario. A .NET 9 customer using the 10 packages of these extensions, and if something does not work.
We may not be able to fix it, because it's…
It could be… issue could be at the .NET or the…
At our level, the SDK level. That's the kind of supportability burden we are going to increase. As you said, we cannot keep, like, both the sides happy, so we need to take a side on it.
**Martin Costello** 16:34 I think… yeah, I think we… we're never gonna make everyone happy, because…
if this change goes as proposed, there'll be a subset of users who are like, hey, there's a security bug, you need to update all your packages, and… but then…
you can just say to them, no, no, no, update yours, you will fix the problem for yourself, but if we leave it the way it is, it is impossible to go backwards, but it is possible to go forwards. So, out of the two possi- ways you can go, always latest or pin.
PIN has more options than Always Latest.
**Rajkumar Rangaraj** 17:13 Yeah.
In this model, the proposed model, the one guarantee we have from the .NET team is, until the .NET runtime is supported, we will have security fixes for that.
For example, if they figure out the logging configuration library as a 90 has a security vulnerability, they will fix and we will have a 901.
So… Yep.
that helps us with this model, like, it won't get impacted, any security issues, we can fix it. And as the .NET support goes… the front-time goes out of support, we can start removing those stuff. So this model looks perfectly fine with me.
**Martin Costello** 17:51 Yeah, also, .NET 9's gonna go out of support next May.
**Rajkumar Rangaraj** 17:56 Yes.
**Martin Costello** 17:56 So, we don't… we won't have to care about 9 for a particularly long period of time.
**Mike "Blanch" Blanchard** 18:05 Yeah, the security aspect is probably the more interesting side of this.
I did have one vulnerability opened.
a while back with, like, system.text.json.
What was interesting about that one is there's a NuGet out-of-band version, and there's also a version that ships with the SDK.
So depending on the SDK you're targeting, if you don't have an explicit reference, you'll get whatever reference the SDK has.
some scanning tools, Whichever one was used to open the vulnerability, Blogged.
Us… Because we were… we had a transitive dependency on system.text.json. We didn't have an explicit one.
So we weren't really opinionated about the version the users had. They would get either their SDK version or the NuGet version. But we went in and added an explicit reference to a safe version of NuGet to sort of elevate
the version regardless of the SDK the user had.
That's a little more questionable, and it's just….
**Martin Costello** 19:20 I believe they're improving that for .NET 10, because there's a new concept
Oh, what's it called again? It's…
I've forgotten the name of the concept, but it… the graph traversal for the dependencies understands
if you're dependent on a version of an assembly… I think it's reference pruning, I think it's called. It understands that
if you build the code with the latest SDK, you'll get whatever version of those libraries come with the SDK when they're part of the platform.
So it shouldn't warn about…
You using, like, in quotes, too old or an insecure version in certain cases, because it knows that the app that's compiling the reference will pick up the secure version when it's deployed.
**Mike "Blanch" Blanchard** 20:14 That sounds good, I don't know if it will take care of everything, because this was some…
Security tool that just didn't have the correct understanding, but….
**Martin Costello** 20:25 Yeah, because I've had tools like Trivi tell me that I'm using, like, 5-year-old versions of net standard DLLs, and I just mark them as false positives, because I'm not actually using them.
**Mike "Blanch" Blanchard** 20:38 Yeah, it's just something to be aware of for the maintainers.
There could be occasional headaches.
**Martin Costello** 20:49 Really, that case of the system.text.json.
**Mike "Blanch" Blanchard** 20:54 We did add the explicit dependency.
to satisfy.
the security vulnerability report, but…
It might have been fine just to close it, I don't know, in that case. We may have made the wrong choice.
**Martin Costello** 21:09 Yeah, because another thing I've done in… you can see it in the .NET 10 PRs, is, the SDK warns about vulnerabilities in some cases.
But, and they make the build fail.
So, you either have to update the reference, or you have to manually suppress it with an MS build item, if you know… if you're confident, and you know that you're not affected by the specific vulnerability.
Yeah, I think we can't do nothing, because the build will fail.
**Mike "Blanch" Blanchard** 21:55 Yeah, I don't have.
anything for this, really. It's sort of a case-by-case thing, we'll just have to deal with.
**Rajkumar Rangaraj** 22:10 Alan, do you have any thoughts to share, or you're good with the discussion?
**Alan West** 22:15 No, I think everybody kind of summed up all the things that, was going through my mind. I agree with Blanche that, I think whatever strategy we land on, I think it just needs to be clearly documented. We're making a change again. That's okay.
I think it's a better change, honestly. Specifically, the… the pinning, if we… if we choose that path, I think that's the path we should choose.
… if I were to go out on a limb, I'd guess that…
you know, we're talking about these two camps, and we're not going to make either of them happy, but I think that the camp of the people that we've made upset by not pinning is bigger.
I don't know, I don't have data on that, but that's at least been my impression, just kind of looking at things anecdotally.
… So, yeah, I think it's a… I think it's a positive change.
And with respect to the security stuff, yeah, that was…
That was a good refresher, Blanche. I… I… it was always a question in my mind when we… when we took that explicit reference on systemtext.json, if that was the right decision or not.
I was inclined to think that, you know, it's not our vulnerability, it's somebody else's, and they need to fix it, but I didn't push back strongly against that, because I… honestly, I don't know what the, what good practice should be for library authors.
In that regard, so…
Yeah, I'd be… I'd be definitely interested in… in learning more about other people's, …
Experience with that, and practices around that.
**Martin Costello** 23:59 typically what I do with my own libraries is I… I update the code so that the tests are definitely using the secure version, because otherwise things don't build. But I leave the references in the library at the lowest
One required to compile the code, because if it's a library.
like, if there's a user out there who is security-inclined enough that it's a problem, they can fix the problem themselves by using features like trans… Central Version Transitive Pinning, or something like that. They can explicitly opt into the newer version.
Because otherwise, you just create huge dependency wave churn. So, you know, it's like, if you're a really important package, and you're at the bottom of the dependency tree.
If everyone updates their reference of everything, then you're creating months' worth of dependable updates.
Of just everyone bumping…
the route up, and propagating that through to the deployed applications, when you could just address it at the… at the leafs.
And do not have that huge dependency chain update.
Because you can sort of see the same similar effects happening with things like NPM.
when things get patched. It's just a never-ending wave of, dependency updates.
**Alan West** 25:32 Yeah, yeah, that makes sense.
**Rajkumar Rangaraj** 25:38 Cool. I think, we'll check if we have any other topic. I added these two, because I see these two are the next release blockers for us, so working on this will help us enable
the next beta release, and then take it towards the GA release, or the next table version with the
NET 10 release.
Are there any other…
**Martin Costello** 26:07 Oh, just on the item we were just talking about, do you want me to create a dedicated issue that's sort of an announcement in quotes?
that summarizes…
what the overall proposed change is, so that then… because otherwise it sounds like this PR is ready to move out of draft.
**Rajkumar Rangaraj** 26:31 That will be awesome, actually, if you can have a career tracking issue to see what are the things spending. That's what… when we speak, on the top of my mind after the scene, I thought I'd think about it, but if you have something already, just go ahead and create one.
**Martin Costello** 26:47 I think, at the moment, the information, excluding what we've just literally discussed that's just in this recording.
**Rajkumar Rangaraj** 26:54 Okay.
**Martin Costello** 26:55 Everything is sort of written in about, like, three different issues in the pull request. So if I create a new issue and summarize it into that, then if the change goes in, then we can just point to that one issue as, like, the canonical
Here's what we're changing and why.
**Rajkumar Rangaraj** 27:14 Definitely, Martin. Just… let's do that, but also, code that this also needs to be documented along with the, changes.
So in that way, the issue tracks both the implementation, what we need to add, and the changes, the documentation update, what we need to do.
**Martin Costello** 27:34 I don't know, I just… I just meant an issue that is effectively an announcement.
So, after it ships, someone can just go look at it and read the rationale, but the PR will have the changelog updated explaining what's been changed, but then that can just point to that, to the new issue for the extended information in more detail.
**Rajkumar Rangaraj** 27:56 Yeah, it's just to track that we don't miss out anything here before the release.
Cool. Are there any other, like, Topics, special topics for today.
**Alan West** 28:16 Not for me.
**Rajkumar Rangaraj** 28:18 Okay, cool. Let me go through these ones here. I had a… I got a chance to meet Trask, and I spoke to him about this renovate, and he…
confirm that Renovate can be used across all the OpenTelemetry repos, so there are no blockers. So, I left a note already in the PR, I think we could go ahead and
Continue the… using the renovate here.
I heard it.
**Martin Costello** 28:49 I opened an issue in whichever the repo is, asking for it to be installed.
Unless it already is installed, but I can't tell.
**Rajkumar Rangaraj** 29:02 Okay
I'll take a look at it and update you, Martin. Probably I might reach out to you over Slack on that, but….
**Martin Costello** 29:17 Sure.
**Rajkumar Rangaraj** 29:20 And I think you got the answer on the last PR that's listed over here also. Blanche provided us.
Feedback on it.
I think we should.
**Martin Costello** 29:30 Oh, yeah, I… yeah, I put a comment on there today. I… I think I understand…
the asserts are trying to, like… the tests aren't using the SDK the way you're supposed to use it, but the way the code is designed.
I don't think you can realistically unit test the code.
Because it's a public type, but it depends on internal types and their explicit behaviors.
And it starts a thread in a constructor.
So, if you have a race condition and the thread tries to do something before that special method gets called, then the debug assertion will fail. So I've changed the PR to make the types non- null able and always have it initialized as an empty array. So it also solves the assertions firing.
But I don't think… I spent an hour even trying to find which tests make the assertions fail, and couldn't.
Because it was incredibly difficult, because…
The assertions fail on a thread, so what made the object that's running the thread get created is not in the stack trace.
**Rajkumar Rangaraj** 30:53 Blanche, any thoughts on this one?
**Mike "Blanch" Blanchard** 30:56 This change looks okay to me. So basically, we set them to empty arrays, and then they get reset to something real when the thread fires.
**Martin Costello** 31:05 No. The way the thread gets started, which, through a very convoluted process, eventually calls the method where the assertions are. It goes to, like, collect
After, like, a wait handle gets triggered, and it goes down through the, like, the class hierarchy and eventually calls the method in the extended metric reader thing.
**Rajkumar Rangaraj** 31:29 But, ….
**Martin Costello** 31:31 to call the method that initializes the arrays to not be null before this PR, you have to create a metric provider SDK, which requires you to give a service provider, which is already populated with a load of objects.
Because it makes lots of internal implementation detail assumptions. So, the only way to unit test certain classes.
and guarantee the assertion never fires, you have to go through the entire SDK like a customer would use it, because otherwise you have the possibility of the method not being called, but the thread running.
**Mike "Blanch" Blanchard** 32:17 So then, what does this change do to fix that issue?
**Martin Costello** 32:21 It makes it so that those arrays are never null , which means that the assertions never fail, because they're never null .
**Mike "Blanch" Blanchard** 32:30 So you have to remind me what these arrays are. These are, like, the results after I collect?
**Martin Costello** 32:36 So, these are the arrays that go into a batch of metrics to get exported.
**Mike "Blanch" Blanchard** 32:43 So we're basically, like, warming up the reader as if…
It performed a collect and just had empty data.
**Martin Costello** 32:53 …
Yes. Because I think what happens, if this happens to happen in a release build right now, it just falls into the catch block that handles the fact it would have dereferenced a null .
And carries on happily anyway.
But now it can't dereference null , because they never know now.
**Mike "Blanch" Blanchard** 33:16 I mean, there's… there's many code smells here. Not this particular change, but, like, the whole convoluted
how we do collect, and how it's, like, resetting. It's a weird, like, pointer thing.
something went awry here in our implementation, but I'm fine with this change, just to… Smooth out the…
The… the core issue here, what, is, like, flanky tests that… Depending on the timing, fails.
**Martin Costello** 33:49 Yeah, that's the main… because the reason I found this in the first place is just doing local development. I have a terminal open, I'll just type .NET test in the root and run all the tests.
And then I get debug assertion pop-up windows that block everything.
**Mike "Blanch" Blanchard** 34:04 Yeah, I'm good with this change.
**Rajkumar Rangaraj** 34:14 Cool.
Is there anything else? The… these two PRs require, like, a review from mine. It's still pending on me to take a look at it.
I'll try to see if I get some cycles, because these are… both are, like, big PRs, or it touches the critical part of the core, so just need to spend some more time on this one.
…
Martin, I think I will unblock you on this one, before the end of this week, in both the repos, so we could merge it.
**Martin Costello** 34:50 Thanks.
**Rajkumar Rangaraj** 34:55 So, that's all we have it here.
Just wondering, one last time, asking any other things to discuss here? If not, I think we could end it now.
**Alan West** 35:12 Nope.
**Rajkumar Rangaraj** 35:13 Cool. Thanks, everyone. See ya.
**Alan West** 35:16 Talk to you soon!
**Martin Costello** 35:17 Bye.
