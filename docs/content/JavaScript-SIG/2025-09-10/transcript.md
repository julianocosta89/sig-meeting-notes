SIG: JavaScript SIG
Date: 2025-09-10
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/VVCYMKbP9o0ECXJWWKz3L_07UROX-e_7eZMPum-7MBzXu0yBZGc_8qfsrTyX87R3.jYkhRy6dpAI62ndl
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:55 Boom.
**Trent Mick** 01:06 The X-Files poster makes me laugh.
**Marc Pichler (Dynatrace)** 01:13 People around the office also love it when they walk past here. They sometimes, Come in and talk about the expires, which is fun.
**Trent Mick** 01:28 Despite it being shot around here, I never, never got into X-Pets.
**Marc Pichler (Dynatrace)** 01:41 I'll share my screen real quick.
Windows sold.
Seems to be the right one.
Okay.
Yep, and that's… It already started with, Marilla, some results from, the survey in the main repo.
**MG Marylia Gutierrez** 02:15 Yeah, so I usually wait… waiting, like, a little to get a few responses, so otherwise it's not super identifiable on what he's saying. So yeah, we got quite a few for the couple months on the main one, that's why I put it also on the contrib, now. But the… basically, the average score is, like, a 4.8 from 5. The majority of people Giving a lot of compliments on… responsiveness, and how easy to understand things from the contribc on how to set things up and run, and things like that, so that is, like, general comment that I see all around. There were a couple comments on, like.
hard to understand steps for creating and pushing a branch, which is not as specific for this repo, so I just want to share here, but I don't think that's nothing we should be doing about that. It's… I don't know.
general learning of the tools. There was one specific for the contrib, that is the, basically.
talking about the run tests that didn't have the browser test, and the person, I think, was testing things on browser, but it was not running, and it was not clear that it was not running, so I'm not sure if it's expected for that, the main one to also run the browser, or they have to do something, so… there's an issue there about, like, or updating the contrib repo to make that clear, or… I don't know, update the script itself? I don't know what is the… what… It's the solution here, but yeah, just sharing.
**Marc Pichler (Dynatrace)** 03:48 Yeah, I think, we actually mentioned that, in the contributing MD, it's just not, not very visible. Like, the quick start just gives these steps, which doesn't run the browser tests.
But, yeah, down here we have the… test browser and test web worker. But, yeah, might be worth it to just move these up here, and then it's very clear to everybody that that's How to do it, and… I guess most people.
Read this here, and then don't go too much further.
**MG Marylia Gutierrez** 04:30 Yeah, especially because the next one is, like, pull requests, merge guidelines, so they think.
this is the test, the next day, it's like, I already know how to do a PR.
**Marc Pichler (Dynatrace)** 04:38 Yeah, I guess some reorganization of the whole thing, would probably be good, and there might be some info that isn't too applicable to, everybody, where… We could just rearrange some things to make it a bit easier to understand.
**Trent Mick** 04:59 I, for one, have never run TestWeb Worker.
Or test back and pad I just found.
**Marc Pichler (Dynatrace)** 05:06 I think these, the back compatibility tests, we have removed.
Because they weren't really doing anything anyway. And, the web worker tests, they should run in, on each PR, but you usually don't need to run them, Hey.
I have to say, also.
only run them every once in a while, when I remember that they are there. But they never fail, when… When the browser tests are… are passing, or almost never fail when the browser tests are passing, so, it's not too much of a… Problem, usually.
All right, yeah, thanks for bringing the, survey results to us. I would have expected the average score to be kind of lower based on the interactions that I usually have with people, but.
**MG Marylia Gutierrez** 06:15 This survey is only for new members, so if you're not yet a member, so… Because that was kind of, like, the go-to, like… what is the blocking people from starting to contribute? So that is what we're gonna gather that experience.
**Marc Pichler (Dynatrace)** 06:35 Alright, next to you.
Does anybody have any questions, comments?
this… If not, then, yeah, guess we can move on to the next one.
Which are, I guess, the config PRs, right?
**MG Marylia Gutierrez** 06:56 Yeah.
**Marc Pichler (Dynatrace)** 06:58 Sorry, I still haven't gotten to those.
Oh, we…
**Trent Mick** 07:01 Same.
**Marc Pichler (Dynatrace)** 07:02 Yeah.
**MG Marylia Gutierrez** 07:05 And one of them got the comments from the, like, heard from, like, the other TC, and he… said pretty much a thumbs up for the way that I did it, so…
**Marc Pichler (Dynatrace)** 07:18 Alright, that sounds good. Yeah, my review list is, getting, getting almost to a point now where these are the next ones on my list, so… fingers crossed, hopefully until next week I will be able to, dig a bit deeper into those and, do some more in-depth reviews. And I also encourage everybody else to please have a look at the PRs here. The best way to speed up a PR review, times is also to review other people's PRs. So, if anybody has time to review a PR, it's always very much appreciated.
Yeah.
Any, questions or comments for Marilla about the configuration?
Thanks.
If not, then, I put just a little heads up here, yeah, just some info.
the 2.1.0 and 0.205.0 are released now. The 0.204 contain the bad OTP browser exporter.
There was a park that, prevented you from building with, Webpack, so… 0.205 is what contains the fix for that. Needed to do some larger shifting around with some of the types to make it work.
But now the, browser and… Node.js exporter types are a bit more decoupled from each other, so it should be easier to add things to the Node.js exporters that shouldn't go in the browser exporters.
And the contrib release for these has also been published, so, the latest version, hopefully, fingers crossed, will, work now. Yeah.
Any questions or comments about the recent release?
And, yeah, I guess we can move on to bug triage. As always, if you have a topic that you would like to discuss, and we're doing bug triage, then please just interrupt me, and then we can go back to the agenda and talk about your topic.
Alright, the first one here is… Note pipes leaking to browser environment when importing OpenTelemetry Core.
Types not automatically get added to the global scope, which isn't fun.
Oh, mmm… And it seems to be exporting it from… or taking it from this… Note.
thing here… I wonder if there's just something that we can do in the package JSON to tell it not to?
Look at this.
But this is definitely a park that… doesn't really… causes problems in user app, not related, or not related to correctness. I think P3 is the one that we want.
And I guess this wouldn't just affect this package, but also a few others, so… we might have to check that as well.
I'll remove the triage label and add the core package label for this.
Yeah, we'll also need to… Make a little reproducer to see if whatever… Picks we come up with actually does what we're looking for.
solving.
Yeah, so that's the first one.
Then the second one is also, browser… Async context gets lost after… Second to wait, yeah.
Oops.
kind of expected, I would say, with the status that we have here.
6 thumbs up. Yeah.
I guess this is, kind of blocked on the, CC39 async context, proposal. That is still a proposal, unfortunately.
We definitely need some more documentation around this, and probably pine paper.
Into a direction that… Makes sense.
I'm not aware of any, Any place where we have documented the challenges around this.
But… There's also… This issue, and I guess there's probably… More than these two that we need to, need to deal with. I will leave that at triage for now, and… We're trying to figure out if there's, some doc that we can bind people to, and it would probably also make sense to add it to the FAQ section.
Yeah, I can see that looking like a bug, and also, like, having all the characteristics of a bug, but I'm not sure if that's… Something that's fixable right now.
Alright, moving on to Chrome Drip.
SQL's process hook no longer available to augment spans per message.
**Trent Mick** 14:14 That was intentionally removed in a recent breaking change to the AWS instrumentation.
Because… And recalling on the fly here the spec for messaging.
Doesn't have processing spans anymore.
Since years, and we finally caught up to that, at least.
I guess that's by design. If you want, I can reply.
**Marc Pichler (Dynatrace)** 14:42 That would be great, thank you. I'll put the… AWS SDK label on here.
And I guess that probably will be closed then, otherwise we can just get back to… Let's skip next week… Alright.
And I guess that also was it for… Pong group.
people… Yep.
Alright.
Then we can move on to, CR triage.
We said that we are going to do the… repo with more pull requests that are open, but I think we haven't done… On trip last time, so just, it's just… 2 quadrip today, and then, if there's still time, we can also go over to… Core repo.
The first one is the React Native, instrumentation that hasn't had any, any movement, I guess.
I guess in the long run, this probably would make sense to also have it converted over to… events, I guess.
It's probably the closest that, slow system, that makes sense.
But I guess there's not much to do right now for this one.
Then there's page view instrumentation.
Semantic conventions apply changes to semantics in Conf.
Looks like… The conflicts here are preventing… Current workflows to run.
Right.
And we can move on to the next one.
adding the SQLized instrumentation, SR versions.
Yammer is still missing.
Guess we're still waiting for that, here, so also nothing to do.
Then the next one is web exception instrumentation, changes requested. I did request changes.
For the two component owners, and where to add them.
And in person for… Or else we'll work on this.
Looks like no changes to the component on this.
Yet, so we'll just wait for that to be added.
Than this one I had a look at earlier, Thank you, Hector, for working on this, yeah, it's… looks good, just missing the execute permission on the script, I think, which is why it fails.
**Hector Hernandez** 19:47 Okay, I will take a look.
**Marc Pichler (Dynatrace)** 19:49 Thanks. We're very close to marching this. Sorry about that, I had… Put the approval on here, and the workflow runs when there's an extra approver, not just any review, and then I saw that it failed, and then I had to, request changes again. But… Hoping we can get in… get… can get that in soon. Alright.
**Hector Hernandez** 20:18 Yeah, thanks for Ruby.
**Marc Pichler (Dynatrace)** 20:21 So… Alright, then we have, AWS SDK, Bedrock Invoke Model with response stream instrumentation, I can try and revisit this… Finally getting back to this.
**Trent Mick** 20:48 That's totally on me, isn't it? Unless it's moved in the last little bit?
**Marc Pichler (Dynatrace)** 20:52 I think it's moved a little bit.
Yeah, you also did a review on this one. If you have some time, Would also appreciate you having another look.
Yeah.
Not too much, move into the, petrock stuff, so… My review is not too helpful in that case.
**Trent Mick** 21:25 I'll take a review again.
**Marc Pichler (Dynatrace)** 21:27 Thanks.
Alright, the next one is GraphQL. This is on its way to actually be an unmaintained component, because… Obviously, he hasn't… been reviewing this, I added a workflow recently in the core repo that will also, then check for component owners, once I have the time to update the script.
To do that this way.
And then we might see a bunch of, components marked as unmaintained, unfortunately.
If anybody, on the call here is interested in becoming a component owner for this instrumentation, then please go ahead and open, PR to add yourself as an owner.
And, yeah.
And hopefully we could get this merged soon.
Alright.
The next one is… That is for, auto-instrumentations note. I think I have said, like, 3 times now that I will take some time to review this.
But I didn't.
Didn't get pivot yet, so… I'll put this on my list once again.
This was the next one.
Yes, so those next two ones are related.
**Trent Mick** 23:32 And we still need to…
**David Luna Bistuer** 23:33 Yeah.
**Trent Mick** 23:34 discuss and pick a path at some point. I kind of… so, I had it on my list to go have an opinion, because I haven't… read them carefully enough to form my opinion. But, I then also kind of wonder if we're going to be want to be stuck waiting a little bit to see what the hotel browser side guys would do to… Great stuff, because if there's ever intention of… Moving instrumentations that they're creating back in here, we'd want to have basically the equivalent, right? Or at least, if we're going to be changing our… ESM and ES Next, I don't know, you're… you're bobbing your head. David, I don't know if this seems sane, but we would want… Maybe at least their opinion on it, I guess. So we form an opinion and then ask in the… in the browser sig if… the setup that we're proposing seems sane for them, I guess, I don't know.
**David Luna Bistuer** 24:27 I think it's a good idea. I can bring it up in the next processing.
**Trent Mick** 24:31 Yeah.
Well, maybe once we form an opinion, but yeah, I don't know. I mean, my biases are still towards having… yeah, I don't know. Not doing the bundled ones. I still like having all the multiple files there in the build tree, and leave the bundling towards, like, whatever the end app is, but, I don't know.
Let's a lot of the pros and cons.
**Marc Pichler (Dynatrace)** 24:56 Yeah, I, I think I had one opinion that I forgot which one it was.
I think it was towards… Something similar to this, but yeah, either way, bundling it up, or, Lot is probably fine.
I kind of like the idea of bundling it up, because, it just… Seems like a very clean output, But I don't have a strong opinion either way.
But yeah, I guess for these, for, for Undici, I think… Probably doesn't matter too much which, tooling stuff we use, because it's just gonna be used in Node anyway. But for the shared packages, I think we should align with whatever the browser folks have. And then, if we can use the same tooling across both, I think that also makes sense. Like, also, if we do Node.js and We can reuse the same tooling that the browser folks want to use. Then that's just great, because we… we'll save ourselves one more dependency, or whatever. So, let's the plan.
**Trent Mick** 26:29 Any of those things.
Yeah, if when they get merged, because they're creating a separate repo to work in.
**Marc Pichler (Dynatrace)** 26:35 Yeah, I've seen that, would be, interesting.
Going forward with, one more repo to look out for, but, yeah.
As I don't really have an opinion either way.
the creation of the new repo, so I didn't really comment on it.
Alright, then I guess we will leave that for now, and if there's… If there's some outcome from the prolific, then we can still get back to… Back to this.
Who cares?
Then we have here…
**David Luna Bistuer** 27:24 It's eligible for Qual 3, but I did interview this afternoon.
Yeah, so we decided to sponsor it and give my suggestions on changes on that.
**Marc Pichler (Dynatrace)** 27:38 Awesome, thank you.
**David Luna Bistuer** 27:40 Basically, it tries to do the support, but actually it's removing the… All the braces, all the… all the braces is just only testing 3 and up.
My suggestion is to test everything, so to test person 2, and also test person 3.
**Marc Pichler (Dynatrace)** 27:58 Yeah, that makes sense.
**David Luna Bistuer** 27:59 No.
**Marc Pichler (Dynatrace)** 28:04 Sorry, Ed.
I guess, 3 years, probably.
Somewhat new, so dropping support for 2 is, not… not an option right now.
Alright, and then the next one is renovate.
**David Luna Bistuer** 28:29 Okay, yeah.
**Marc Pichler (Dynatrace)** 28:30 can be then taking a look at once this PR here is merged. Thank you, David, for looking into the core one. It's been sitting for a while, so it's good to have it.
Have it move along a bit.
Alright.
The next one is Renovate, we're also skip that.
Then there's a draft for… Switching from header to license header is a new plugin.
I guess we can also skip that one, since it's craft.
And yes, AWS Lambda… So… Two days ago.
So… Looks like, this is well on its way.
And we have a PR for… Instrumentation AMP… and reviewed this one, so I think we are so good on that.
**Trent Mick** 30:12 I did that last month. It's a while ago.
**Marc Pichler (Dynatrace)** 30:14 Yeah.
**Trent Mick** 30:21 I guess we see if we get a response.
**Marc Pichler (Dynatrace)** 30:24 However… If you want, you could change your, review to changes requested, and then… It becomes clearer that, Something needs to be done.
And this Pierre.
I've seen that, sometimes, just, the… number. No status reviews. It lost.
Boom.
Bit more, more, consistent in putting in changes requested, for PRs.
Recently, and I think it has made a bit of a difference in responses that I got.
But thank you for looking into this one.
So, where, where are we?
Let's… Mqp… Vendors… SQS context propagation… Hopefully, quite a bit of discussion on here.
Looks like there's a question for you, Trent.
Not sure if you can answer this right away.
**Trent Mick** 32:05 I'll put it on my list and come back and look. Yeah, I think we should also probably drop processing spans there, but… Perfect.
**Marc Pichler (Dynatrace)** 32:12 It's the same one as with the other one we talked about.
It's the same concept, yeah.
Right, yeah, that makes sense. Thank you for looking into it. But yeah, it looks like there was quite a… Bit of discussion.
Alright.
**David Luna Bistuer** 32:32 Yeah, this one.
Maybe, maybe I forgot to put something on the agenda. Could you open this? I, I'm…
**Marc Pichler (Dynatrace)** 32:40 Yep.
**David Luna Bistuer** 32:40 There's the common at the bottom.
Since that now… so there was a PR that was blocking this one.
But now we're hitting another… Hatter.
Which, it seems that Smithy, Smithy Core package is now using TypeScript 5.8.
Which includes some generic types that classes with previous versions.
So it's a breaking change for TypeScript, and TypeScript, has decided to not give backwards compatibility. It's on the… on the TypeScript issue.
And we'll see that.
So…
**Marc Pichler (Dynatrace)** 33:19 I mean…
**David Luna Bistuer** 33:20 I don't know. So I'd ask your opinions on that.
maybe, I don't know.
Couple of things could be… one thing we could do is just spin the dependencies, but maybe it's not desired.
Another option that we can have, maybe it's just, for that package, just skip, enable the option, skip lip check.
So, with the compilation, and we, at least for the libraries that we depend on, we are skipping the type checking.
**Marc Pichler (Dynatrace)** 33:53 I think we've tried to avoid skip lip check, before, but that was mostly because there was always another way to serve the problem. Oftentimes, there was, a package where, like, some of the dependencies just ended up being weird, and, like, removing a dependency that wasn't needed elsewhere, was fine. And then, we… Went back to, having a smooth, smooth run of the workflows again. I think for this… particular thing, we can… go either way, skip lip check is probably the better option, because in that case, we won't be stuck with the old dependencies, at least. Because if we pin it now, we'll… probably be stuck with it until, we are able to pump TypeScript to… version that supports this, so I think I'm leaning towards the skip lip check option. I put a comment here.
**David Luna Bistuer** 35:01 Okay.
**Marc Pichler (Dynatrace)** 35:02 So, indicate that.
I guess we can just do that in a separate PR, to add skip lip check, and then we run this here again, and yeah.
See if that solves the issue.
I support using Skip check here, so that we're moving a lot.
workshop.
D.
There's not.
Excellent.
Yeah, thanks for, looking into that. The… the log file maintenance PRs that are being opened, they are sometimes very adventurous in, The places that one goes to figure out why it's not working.
Boom.
Alright.
Boom.
Let's move on to the next one.
Actually, this is just moving things, and I… Seem to remember actually having to… having reviewed this one.
This is, just a… Moving it, And then also incubating, the incubating package, which we had, or the incubating directory, which we had discussed.
I think in a previous SIG meeting, goes away here, and then I think there should be… BR.
Boom.
G.
That's weird, I thought I had… At least.
taking a look at this, like, 3 times before, but looks like I just didn't post a review in the end.
It is a very… Sync change after, just moving it to be actually published.
Alright, where did we stop?
Historic versions in parallel.
I guess this was somewhat related to the changes that, you were making, David, right? I think the person was just trying out some things?
**David Luna Bistuer** 38:59 Yeah, exactly. Actually, what he's doing is, Getting the Tesla versions?
copying it at the root, and then doing some changes. What it does is…
**Trent Mick** 39:12 Instead of sinistering.
**David Luna Bistuer** 39:14 packages directly into Node modules. What it does is just creates a temporary folder.
installs the package there, and then gives, uses a SIM link.
This way, we're not… the process is not messing with non-modules, and we don't have a… This kind of surpasses that we, found, badly.
**Marc Pichler (Dynatrace)** 39:37 The idea thing that.
**David Luna Bistuer** 39:39 The author actually commented to try to upstream that in desktop versions.
So maybe this, this way we can, work with monolipos.
**Marc Pichler (Dynatrace)** 39:49 That would be… Really cool, actually.
like, not running into the issues that we had in the recent, on the recent, dependency update PR would be, Would be just great, actually.
**David Luna Bistuer** 40:05 Yeah.
Well, actually, it would be very good for Tesla versions, so… because you are just, you know, for each package, you know that… for each instrumentation, you know that you are installing different packages.
And not, you know, doing anything else, so it's, you know, it's safe to run them, test environment, but yeah, we'll see.
Maybe I'll ping the author and check if there is an open issue in test all versions.
**Trent Mick** 40:30 He did open a PR there.
**Marc Pichler (Dynatrace)** 40:33 Okay.
**Trent Mick** 40:36 Was PR an issue? I can't remember. He was… yeah, to start.
**David Luna Bistuer** 40:40 that one.
**Trent Mick** 40:40 Disgusting to see if Thomas would take it, but yeah.
**Marc Pichler (Dynatrace)** 40:48 Alright, then I guess this one is, still in progress, not having to… market here, I guess that's what… what they did here, is just take the code from Tesla versions.
**David Luna Bistuer** 41:06 If everything's also okay, it's just… it would be just a matter of updating the SL versions. I use it in…
**Marc Pichler (Dynatrace)** 41:12 In contrary.
Yeah, I've… having it upstream, probably something that I would, prefer, but, yeah, let's see where it goes, and then, yeah, having some more stability in these things is always, always good.
Especially with a repo that's always growing like ours.
It can be, that'd be difficult.
Alright.
I mean… this PR here, I think the person talked about… 2 weeks ago, what, two weeks ago?
And it seems that they also have, like, the instrumentation skeleton.
Which is just a package, probably.
That makes things a bit easier to reveal than later. I much prefer the approach of adding this catapon first, and then filling in the code here.
Leaving.
**Trent Mick** 42:29 Is that just because it was monstrous, or was there another reason?
**Marc Pichler (Dynatrace)** 42:32 it… -Oh.
I think it wasn't all that large, but it's way easier to review a PR when there's the package merged in first, and then the second PR is just the actual, thing that's happening. I don't know, I feel usually it's a bit easier to deal with.
**Trent Mick** 42:56 One thing I think I'd noticed before, where I'd seen line chain instrumentation I think externally, when I was on the NAICSIG. And then I see it here, too, the usage case and the README there has a manually instrument step, which is… not something we have for any instrumentation, so I'm… I'd be curious to dive into the reasons why that's still necessary, and if we can improve that story.
You'll look at the README, I think?
Hell yeah. Yeah.
**Marc Pichler (Dynatrace)** 43:33 I think the… the reason for that is… I also feel like I've seen that before somewhere somewhere on, some Lambda instrumentation package.
Where people usually bundle their, their apps, and because you can't hook, that.
They have this, manure step, where you say manually instrument, and then use whatever, you have here.
So that you don't, need to use a plugin or something like that.
Yeah, but it is, curious.
**Trent Mick** 44:15 Think.
**Marc Pichler (Dynatrace)** 44:15 Probably better to have this aligned with…
**Trent Mick** 44:26 And this is bringing in Jest, too. That'll get exciting.
**Marc Pichler (Dynatrace)** 44:31 That's the sleeping page.
Yeah, I think just… Doesn't work very well with Altar, anyway.
Yeah, need to dig deeper into this one, guess it would be… Won't be as easy as just, marching decision.
But with the skeleton, here.
I guess.
We can discuss dependencies first, and then move on to the actual code.
Alright.
Yeah.
And I guess we can move on to the next one.
Seems to be a draft. I sponsored this one because we need to upgrade.
at some point. I had looked into it briefly, but, These… these tooling updates, they are for sure a way to keep… Keep being busy with things.
This one here, I also have…
**Trent Mick** 46:01 Oh, sorry. I was gonna say, on the ESLint upgrade, I might try to help on that one, too.
I had a comment on the thread, but… Because, yeah, it'd be nice to get over the hump.
**Marc Pichler (Dynatrace)** 46:11 Yeah, thanks. And then if we do this here, then we can just take the same approach in the core repo, because I think there we also are still at ESLint.
8.
Boom.
Alright.
This is approved as owner approver, so I'm gonna merge this in.
And the release is also published by now, so, we're not interfering with anything.
And then we're already at PRs opened last week.
Instrumentation, I already… Looks like we didn't have a runoff.
Run of workflows for this one yet.
Proof to run here, and then we can see if the test was later on.
This is what we just have a look at.
Return underlying modules from Redis instrumentation.
At a modest definition.
We had this person on a sick car, in the past, and they were looking to actually… contribute there.
Handler plugin.
to us.
So… I'm actually curious where this… get modular's definition is actually defined.
It's on the instrumentation abstract, and I guess the new instrumentation… Oh, I lost where I was.
The new instrumentation for… Redis that just packs two instrumentation into one doesn't have this Because it's just implementing the… Instrumentation base.
Or extends the instrumentation base.
So, I guess this looks fine.
**Trent Mick** 49:19 If you like, I can review this later.
**Marc Pichler (Dynatrace)** 49:22 Yeah, that would be great, thank you.
I don't think this is too controversial.
They're just overriding these modular definitions, so we need to make sure that Nothing gets lost, should be there.
But I think we had something similar happen to the gRPC instrumentation a long time ago, where we also had two instrumentations in one, because gRPC used to be two different packages that were, widely used at the time.
It's not only to a PC.js.
Thank you, lots of the proof workflows here.
And the next one is renovate.
Don't skip that, and this is… Upgrade TypeScript.
I did put a comment here to let them know that this is often a breaking change.
Yep.
That seems to be quite a large… move here.
as always with these things, I very much would like to upgrade all the packages to whatever is latest, but… Sometimes it ends up breaking users, which isn't great, so… Need to figure that out somehow.
Renovate PR. As usual, I will… Go through these, in my own time, so that we don't… Spent too much time here today looking at… Yours.
Thumbs… I have the first PR in the list, I opened it.
**Amir Blum** 51:44 like, 2 hours ago, I can give a bit of a context.
So one of our users, of, Odicos users, they got, like, the node application killed by an exception coming from OpenTelemetry.
And the reason is that I don't know why, like, I really tried to follow the code all over and try to reproduce it, but I wasn't able, like, I don't have access to the source code of the replication.
But somehow, it's, We got a non-integer value in agile time, which crushed the replication. So already it did a fix in our distribution.
like, I, published another hotel transformer with this fix, and it, since then, there was no caches of this type, so I believe it is safe, and anyway, the hotel transformer should be, like, generic, it should not assume that the values are coming from an OpenTelemetry core, like, somebody can use it in other ways, so… I really support adding it.
**Marc Pichler (Dynatrace)** 52:52 Okay.
I guess HR time just has… Hr time type is… from the API, if I recall correctly.
And that probably just has number…
**Amir Blum** 53:09 So, it's being populated… yeah, it's being populated in many places, specifically in OpenTelemetry Core, there is, Like, functions that can populate it from a time, or from a self timer, or, like, I don't remember, there's a lot of options, but somehow, someway, one of these pathways caused, like, float.
Yeah.
**Marc Pichler (Dynatrace)** 53:43 I think, given that the type definition is this here, and we can have loads in there, I think this makes sense, to… Frankly, like, this, we should probably… specify here in the API docs as well to… Say that we expect all the integers to be in there.
But either way, I think this, looks good here.
So… fairly uncontroversial, I think.
the type, say, number, and we don't deal with it like a number, we deal with it like an integer, so… We should be doing the correct thing here.
**Amir Blum** 54:49 Now I'm using, like, folk, version of Autel Transformer, which, just for this fix, so… Really happy to go back to upstream.
Once it's…
**Marc Pichler (Dynatrace)** 55:02 Yes, yeah, let's, leave it open for a bit longer, and, I usually go through PRs that are approved, once a day, and merge them in, so, we can then… get this in, quite quickly, I think.
If anybody, has, anything, they would like to.
voice their concern at with this PR, please, feel free to go ahead, otherwise I'll just merge this tomorrow.
Alright.
Yes, starting by orders again.
And then we can… Goes for these, this one… Still blocked on some things in the, SDK.
Block stabilization, milestone.
And this one here, I actually approved that one.
I got one more comment.
And I'm waiting for this… Conversation here to be reserved.
And then we can also go ahead and merge that one.
This is my LPR. I did, we solve conflicts every once in a while, but, they just keep coming back, to bite me. So, What do we want to defer it now? That's a bit.
to mess that up, and then, I need to… do it in the IDE anyway. But… yeah.
Other than the conflicts in the, change log, this is ready for rebuild.
And this is, API docs update, which is… Data right now.
Have to see him.
almost never touching the propagators, so, very… usually takes me a lot longer to actually review PRs that touch these.
No.
If anyone is, serious around, around, peace.
things, then, I think that would be a good way to, like, dig into something and, Like, get into the details of… How that stuff works.
It's probably a good learning experience to, check this PR out, if anyone's interested.
And I guess now we're already out of time anyway. Thank you, everybody, for joining.
since… since Dan's not here today, I'm gonna say his line, which is, review PRs, and I will see you next week.
Speaks for you.
**David Luna Bistuer** 59:22 See an example.
**Jackson Weber** 59:24 Have a good one.
**David Luna Bistuer** 59:25 Bye. Bye.
**Amir Blum** 59:26 Right?
