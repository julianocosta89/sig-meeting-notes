SIG: Java SIG
Date: 2026-07-02
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Gregor Zeitlinger** 03:41 Hello!
**John Watson** 03:45 Hello, hello.
**Jason Plumb** 03:47 Hi.
**jberg** 04:07 Is Trask out of town?
**John Watson** 04:10 Yeah, he's on vacation until after the 4th.
**jberg** 04:14 Alright, Adam.
Forgot about that, I'll share my screen.
Alright… We got a light agenda today.
If you have any topics, please add them. Also add your name to the attendees list.
**John Watson** 04:51 But clearly, only if your name starts with a J.
**jberg** 04:55 Huh.
What are the odds of that?
**Jason Plumb** 05:12 In this demographic, pretty high.
**jberg** 05:18 Apparently.
**Gregor Zeitlinger** 05:19 If it doesn't fit, then it will be made fit. Well, that's… Something in German.
**jberg** 05:31 He can't fit a square peg in a round hole. Yes, yes.
**Gregor Zeitlinger** 05:34 Oh, okay.
**John Watson** 05:36 Just takes a hammer.
**jberg** 05:38 Yeah.
**Jason Plumb** 05:39 Or a smaller pig.
**John Watson** 05:42 a bigger hole.
**Jason Plumb** 05:43 Or a bigger hole.
Look at the creativity among this group, oh my gosh.
We came up with 3 solutions to the impossible problem.
**jberg** 05:56 I like the hammer.
Oh, I have a… I have a one, just because we have a light agenda.
Her ripping out Jackson.
**Jason Plumb** 06:10 That's exciting.
**jberg** 06:15 You might like this, Jason, because you're one of the fans of OTLP JSON support.
**Jason Plumb** 06:27 It would be nice…
**jberg** 06:35 Okay, so the… let's get started. We're 4 minutes over. So, the topics here, are under the context of the Java Instrumentation V3. We're missing Laurie, we're missing Trask, we're missing, Sylvain.
**Jack Shirazi** 06:50 I'm representing Sylvain.
**jberg** 06:53 Okay, do you think there's anyone that you can represent Sylvain's opinions to that can meaningfully act on them?
**Jack Shirazi** 07:00 I mean, essentially, all of this just says that the only thing that's left is that one, on the bottom line.
Which it says, when, when that one is merged, Not, not that one.
Yeah, that one. When that one's merged, that's the only thing that needs to be done for 3.0.
And I think it's just pending Laurie to review.
Or Trask?
But probably a lorry.
**jberg** 07:29 That's great.
**Jack Shirazi** 07:32 And everything else just either is closed or removed from the milestone, so… That's the only indie relevant.
Wonderful.
**jberg** 07:47 And Lori is already engaging on that, so that's good.
Anybody else have topics for 3.0 that they think are worth talking about, given their attendance?
Going once, going twice.
**Jason Plumb** 08:06 There are still 20… no, there's still 9 open items in the milestone.
**Jack Shirazi** 08:13 Dude.
**Jason Plumb** 08:14 Yeah.
**Jack Shirazi** 08:15 So, two of them are going… one of them should be done… If… if it gets approved.
I think several of those, Gregor said it has to wait until… the last release, right? Not this release, but the one after.
**Gregor Zeitlinger** 08:31 That's right, and I think we're making one before 3-0.
Did I remember that correctly? I'm… I'm sure… I think so.
**Jack Shirazi** 08:47 Yeah, we've got a 2.30 to come.
Around 2.29, right?
**Gregor Zeitlinger** 08:52 Right, and after that, we can do the removal stuff.
**Jack Shirazi** 09:00 So I think it's in pretty good shape. It's… I don't think we need to… Worry about it.
**Gregor Zeitlinger** 09:07 But we could make it less confusing if we reassign the items to 2.30, then it's clear what we want to get in there.
**jberg** 09:20 You want to go ahead and do that? Is there a 2.30 milestone?
**Jason Plumb** 09:24 there is…
**Gregor Zeitlinger** 09:32 If… if you tell me which ones, then I can do it.
Is it all the ones, Except the ones that have to go to the 30?
**Jack Shirazi** 09:52 No, I'm not sure…
**jberg** 09:53 context.
**Jack Shirazi** 09:54 I'm not sure that's a productive use of our time.
**jberg** 09:57 Alright, I can do.
**Gregor Zeitlinger** 09:58 that. I just wanted to have feedback that if you have anything that I should keep as 3.0, which I don't know about yet.
I'll just do it.
**jberg** 10:19 Alright, yeah, let's… Let's move on.
So, I added two quick agenda items that I just wanted to share. So one… This was based on an issue opened by Bruno. Bruno alerted us that Jackson 3 is coming out. And, you know, my first thought was that this was going to be a toxic dependency.
And I think that they're taking steps to make that not the case, actually. They are going to publish to… I think they're going to publish to different artifact coordinates, and maybe a different package, so if version 2 and 3 are both on the class path, they don't conflict.
But, you know, regardless, I think, you know, there's still this question of.
which version should we use when we're going to use it? And even if it's not toxic, there's, like, decisions to be made that I would rather avoid. And so what this PR does is, you know, we have a dependency on Jackson for our OTLP JSON serialization. It's used in two places.
On the OTLP… you know, HTTP and gRPC exporters, the network exporters, they have, like, package private support for JSON. Some people opt in, even though we say we don't formally support it, and, you know, there's an issue that says, like, hey, let's support it, and I think we agree that we can support it, and that there's, like, a use case to support it.
And it's just, I think, a matter of somebody picking it up and doing that, so I think we do have to think about HTTP and gRPC JSON as, like, you know, part of, part of, you know, our real support path, even though it hasn't been done yet. And then the other thing is, for the OTLP JSON logging exporters, so the ones that just, like, log in this JSON representation just to standard out, or wherever you point them to.
You can point them to files now, as well.
And, so those both use Jackson to do JSON serialization, and it turns out to be really trivial.
Like, what they're doing is not a lot. Like, I find what Jackson does to do the, like, the POJO stuff, where you deserialize, and then you map it to a POJO, or you convert from one POJO to, like, another. I find that to be, like, beyond the scope of what I want to hand roll, but actually just, like, serializing JSON is not a difficult task.
And, yeah, this is close to, like, a one-shotter with, an LLM. So, yeah, 500 additional lines, and what this looks like practically is we have this one class, JSON serializer, that wraps our dependency on Jackson, and, Yeah, we just switch it out from using a JSON generator, which came from Jackson, to using a new JSON writer, which is our version of that contract we were getting from Jackson. And, it does a fairly simple thing, you know? You know, when we tell it to start an object, it's, you know, it writes an open curly brace. When we tell it to end an object, it writes a closed curly brace. And, you know, same thing with arrays and the other parts about JSON.
And, yeah, I think it… I think it makes sense, and it was, you know, pretty simple. Gregor left a good comment on here that, you know, we need some more edge case testing. I support that, so I'll go back and add some more testing for this, but, you know, I think we should go forward with this.
**Jason Plumb** 13:59 Yeah, that's cool. I will try and give that a review today.
That's awesome.
**jberg** 14:07 And then, while we're here synchronously, this other topic that I have… so… Maybe you noticed, there's, there's 46 open PRs in OpenTelemetry Java, and that didn't used to be the case. We were always, like, hovering around 25 or so. And this one person… Has opened a bunch of PRs.
the SWLSQS, I don't know how…
**Jason Plumb** 14:33 And they're all draft.
**jberg** 14:34 comments.
there was, like, 5 that were actually open, and I merged all of them, because they were all very small, and, like, you know, decent little well-scoped changes, like, to fix typos in Javadoc and things like that.
And the remainder of these, which is, like, an additional 20 or 25 or so, they're, again, like, small, well-scoped changes that I want.
But they're all in draft, and the person is unresponsive.
**Jason Plumb** 15:04 Hmm…
**jberg** 15:06 And so I can manually do stuff like, I can mark it ready for review, and even though they say, hey, this isn't ready for review, I can mark it ready for review.
And I can also push to these branches, so if there's any, like, small tweaks that need to be made before merging, I can… I can, you know, just deal with this unresponsive author, and, you know, then we can approve and merge, without them in the loop.
I can close all of these PRs. I can just say, like, hey, even though this is all good, like, stuff that I want, you know, the author has become unresponsive, so just close. And, you know, somebody can either recreate them, or we can abandon them, because they're not that important. They're just, like, small little typo-like changes.
So, yeah, I wanted to get your feedback on How we could move forward.
**Peter Findeisen** 15:55 It looks like the author was commenting last week. Is this the person who wrote those?
**jberg** 16:04 I have responded.
**Peter Findeisen** 16:05 She was active last week, maybe, maybe this person is on vacation without access to internet or something.
**jberg** 16:14 So, I have responded to 2 or 3 of these PRs, and not heard anything in response.
And I haven't heard anything in response since, like, they did this initial flurry of activity. It's like, they started opening the first PR on a Friday, and by Monday, that's, like, when their activity had stopped.
**Bruno Baptista** 16:36 So, this, this, sorry, this to me seems like, some… but creating random PRs.
Yup. And… For safety, even if the changes are kind of trivial and, Kind of okay.
I would advise to close everything, because he might be gaining karma.
And at some point, send us something that is not that trivial and not that harmful.
**jberg** 17:08 So…
**Jason Plumb** 17:09 It is the way of the world these days, unfortunately.
**jberg** 17:12 I definitely understand that people are trying to harvest reputation, and then, you know, use that maybe for nefarious purposes in the future. But we're never going to emerge a PR without thoroughly understanding its contents.
So I don't care if someone has, like, all the reputation in the world, like, we're still gonna understand their contents, especially if they have some binary blurb in there that looks super suspicious.
**Bruno Baptista** 17:43 Yeah, it's just because even, PRs that seem harmful, they sometimes include things like, changes in… things that run on the CI, You don't notice it?
It's…
**Jason Plumb** 18:00 Yeah, I mean, yeah, like, attackers have snuck stuff into PRs that's non-obvious, that looks harmless, but… so if it were me, I think the approach I would take on this is I would try and give it, like, 2 weeks, like, I would comment and be like, hey.
Thanks, this is cool. Is it ready? And if you don't hear any… like, I want to merge this. If you don't hear anything in two weeks, I would just mark it ready and merge it.
**John Watson** 18:21 I mean, we could put… don't we have a tag, like, needs author feedback, or something like that?
**Jason Plumb** 18:26 Then it'll get closed.
**John Watson** 18:28 And then it'll get closed automatically, right?
**Jason Plumb** 18:30 But then that's counter to what Jack wants, which is wanting these to be merged.
**John Watson** 18:34 Well, but if they feed… if they provide feedback, then we go forward.
**jberg** 18:39 You know, it's like, I've done these sort of, AI scans of the codebase, looking for bugs and security vulnerabilities, and they come back with this big list.
And it's hard for me to unsee that list. Even though nothing on the list is, like, super urgent, they're all still small, tiny, little bugs. And that's what these PRs are to me. It's just, like, little typos, little things that it's gonna be hard for me to unsee. Like, I do want to fix these, even though, Even though they're, like, trivial. Even though they're not, like, you know, that important to get in, and the world will keep spinning without them.
**Jason Plumb** 19:15 Oh yeah, I want this Kotlin one. Let's do that.
**Jack Shirazi** 19:18 Give it two weeks, like you said. If there's no response, then just get the LLM to scrape them all into one separate PR for yourself, close them, and then merge it in your separate PR.
**jberg** 19:34 I can do that. Do you all think I should cherry-pick the commits, or do you think I should, like, just copy the changes?
**Gregor Zeitlinger** 19:41 Yeah, don't worry too much about cherry picking. I mean, if they are unresponsive, then… Doesn't matter.
But in my repos, I actually don't care if people have draft PRs. There's just an automation that I… I don't know, after 4 months, PRs are closed automatically, so I don't… I don't care about having those draft PRs around.
**jberg** 20:07 Well, I don't care about them, but I want the changes.
**Jason Plumb** 20:10 Yeah, okay.
**Gregor Zeitlinger** 20:11 Then I agree, just, do it in one PR, and…
**jberg** 20:17 Okay, I think that's, that makes sense. So give them another two weeks, and when all these are on the verge of light closing, then, you know, close them and just, you know, grab the changes and open a PR on behalf of the person. Not on behalf of the person, but embodying all those changes.
Okay.
**Jason Plumb** 20:37 Jack, there was… there was some other new change that, It might have been in community that limits the, like, allows maintainers to limit the number of, like, concurrently open PRs? Did you see that? Yeah, I'm sure you saw that thing.
**jberg** 20:49 Yeah, let me…
**Jason Plumb** 20:52 And are you using that yet on Java?
**jberg** 20:55 I think it's installed everywhere, and, I think it just makes the distinction between draft and open.
Let me track that down, though.
**Jason Plumb** 21:05 Cool.
And then did you see what David said in chat? This user is just like… Roaming the internet with a bot in hand.
**jberg** 21:14 Oh yeah, they got their, Clawbot.
**Jason Plumb** 21:17 Yeah.
**jberg** 21:21 Poop and claw.
**John Watson** 21:26 I mean, honestly, this is actually a really good use of… like an AI bot. Like, these little tiny fixes are great, like Jack said. Like, these are positive changes, and they're small, and they're easy to review, and there's… the scope is very limited. I think it's honestly a good use of of AI.
**Jason Plumb** 21:50 But there's some upper limit of the number of concurrently opened.
**John Watson** 21:53 Yes, yeah, I agree.
**Jason Plumb** 21:55 Where it becomes a burden, yeah.
**John Watson** 21:56 For sure, for sure.
But I wouldn't want to necessarily punish somebody for going to, even if it's a small amount of effort, to go and actually do this cleanup work. Like, it's good work.
**Jason Plumb** 22:07 Oh, yeah.
**jberg** 22:10 Okay, so, yeah, so John, I think where that breaks down is if, like, they abandon their work.
**John Watson** 22:16 No, no, no, 100% agree. I mean, I'm just agreeing with you, Jack, that I think these are good changes.
And I don't want to punish somebody for putting in the changes, but if they're abandoning it, then that's their… that's… I mean, what can you do?
**jberg** 22:30 I think what I would do if I was, like, running this LLM, and I was trying to do something like this, just, like, go around the internet and find little bugs and fix them, and let's say I wasn't doing it for nefarious reputation farming purposes, like.
I think what I would do is I'd, on the PR description, say, like, hey, I'm gonna just note myself out of here. I won't be around anymore. Feel free to do whatever you want with this, like, update, close, do whatever, like, you know, the ball's in your court. To just make it clear that, like, you're not gonna offend me if you modify my changes.
**John Watson** 23:02 No, I agree, I agree.
**jberg** 23:05 So, okay, going back to Trask, what Trask was mentioning about, like, the default limit for number of open PRs in a repo. So there's a new option in GitHub, it can be set by maintainers without admin permissions, and… I think Trask closed this, because we don't need it… there is no organizational default, because all maintainers have access to it, just like, you know, each maintainer can go set what makes sense for them. So, I need to go and set this for OpenTelemetry Java.
What do you think, John? Does 5 seem like an appropriate amount?
Yeah, I like, I like 5, like you said.
**John Watson** 23:45 Yeah, seems good.
**jberg** 23:52 Alright, I think we've belabored this little topic enough, so thanks.
That takes us to the end of the agenda. Anybody else have anything they want to talk about before we part ways?
**John Watson** 24:05 Yeah, there was a new issue that was logged this morning in OpenTelemetry Java that I was trying to find. It's about, post-quantum cryptography in Java 27.
That they would like an easy way to enable that, and right now it's a, like, something like 130 lines of boilerplate code to get it done, and they would like a little, like, just an additional little small change to support.
Which seems reasonable to me, but I just wanted to bring it up, because I thought it was, probably a good request and worth talking about.
**jberg** 24:38 Yeah, so we have this escape hatch, and… in our OTLP exporters for when the, you know, the built-in, you know, paved path for configuring TLS doesn't work for you. And so, like, let's just bring it up for reference.
And I know a lot of people know this, but I'd just like to be… explicit, so we're all on the same page. So, the paved path for configuring TLS is like, you know, you call setTrusted Certificates.
And, or if you're doing MTLS, you do set client TLS, and… And I think you have to call something else as well.
And maybe set trusted certificates, you have to call both of those. But the escape hatch is right here. So, like, if… If you don't like what we're doing, this is how you configure the underlying SSL context in X509 Trust Manager we're going to use on all these requests. And the boilerplate that they're referencing is, like, they have to manually configure these and call the setSSL context.
And so, like, I can think of a couple of different ways that we could provide, like, helpers for this. We could provide, like, a helper that, you know, spits out this pair for another common configuration, like a post-quantum, you know, configuration.
whatever it is, I don't know whether it's, like, an encryption algorithm or whatever, we could get feedback on what actually they want to see in an SSL context.
or X509 Trust Manager. Or we could have, like, you know, something like new… a new helper method like these. Like, these are helper methods that accept certificates that ultimately manifest in SSL context and X509 Trust Manager. So.
**John Watson** 26:29 I thought there were.
**jberg** 26:29 I think I'd have to see the shape of the data.
**John Watson** 26:32 I thought their request was just to expose putting the parameter, SSL parameters on.
**jberg** 26:39 Accepts SSL parameters.
I need to look at what SSL parameters is, and what its relationship is to SSL Contacts and X509 Trust Manager.
And, like, see what the API is for things like gRPC and, and OKHTTP, because that's the complexity we're trying to manage here, is, like, these builders are, you know, the least common denominator amongst all the different sender implementations we have.
**John Watson** 27:13 Yep.
Well, also, the question is how much of what they want to do is Java 27 specific?
If any of it.
**jberg** 27:24 Right.
So… I guess… research on my part is needed. I agree with this in principle, though. Like, let's make it easier to do post-quantum TLS with our OTLP exporters.
And honestly, they should probably… the speckled me.
**John Watson** 27:47 Yeah, well, that's also true, yeah.
Anyway, I just wanted to bring… just highlight it, because I thought it was, probably a… High-quality requests that we should consider how to deal with.
**jberg** 28:00 I did see it, but I'll make a note to go back to it and actually give it some proper attention.
Any other issues?
Topics.
All right, y'all. Well, it's a holiday in the U.S. coming up, so I assume some people are going to take a long weekend. I'm out next week, so, and also the release for OpenTelemetry Java Core is next week as well, so I'll figure that out asynchronously.
Other than that, have a good weekend, stay cool out there if you're experiencing one of these heat waves, and I'll talk to you soon.
Bye-bye. Bye.
**Peter Findeisen** 28:51 Bye.
