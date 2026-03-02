SIG: JavaScript SIG
Date: 2025-08-27
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/isGJAuvBh1UTmH7j2pU8vMo2NFA3TtloPeLf7Uyol9JuHltpn-I8LAtkv0tCQl7z.fD4eFEl5FCEoWl-n
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:00:53 Hello?
MG Marylia Gutierrez 00:00:55 Hello!
Yeah, for a second, no one's showing up. I was like, am I on the wrong place?
Marc Pichler (Dynatrace) 00:01:10 Yeah, looks like more people are trying to go. Looks like we're both in the right place.
MG Marylia Gutierrez 00:01:16 Yeah, because I, I have a…
basically a tool that I use that is on my Mac that is just always, like, on top
alongside with, like, the hour and stuff, and it just shows me what is my next meeting. So I don't have to go to my calendar and open whatever it is. So, if I click already opens for me, sorry, if it is Zoom, or whatever is already open, but if I have, like, two at the same time, it picks one, and sometimes I already went to the wrong one. So this is why…
The right place, right?
Marc Pichler (Dynatrace) 00:01:44 Just pick a random meeting when, … Yeah.
MG Marylia Gutierrez 00:01:48 Today, there's one. There's… yeah.
Marc Pichler (Dynatrace) 00:01:58 Right.
So I'm gonna share my screen.
And then we can get started.
Great.
Okay, you're welcome, everybody. Let's kick it off with… David's topic.
David Luna Bistuer 00:02:41 Hi, everyone. Just, comments, or…
Questions, rest here in the, to see what's, what's your, what's your opinion.
So, I remember that you told me, Mark, in the PR, that you were asking about how to do, tap testing for specific packages, that there is a workflow that you can run manually, and so on.
So, I had to look at that, and…
I know that the coordinate status tag is… we are running, … Unitest, and…
the desktop versions went for PRs.
And then, again, we run only test all versions for push, when we are pushing on main.
Okay.
And then, we have this workflow that we can run manually on a specific branch, and we can just specify a specific, well, specify, all this stuff.
of packages, and then run the test versions.
…
with this workflow, I think that we could actually reuse it for both things, so we can run NPRs and also push.
My question would be… If, …
The coroner… in the corner state, pushing on main doesn't upload the… the coverage reports.
Because we're already doing that on VRs.
So… yeah, my question would be, we can… so, the opportunity is that we can reuse that, that workflow for…
Toll request and push.
Do we want to have everything for both? So, testing, test all versions, and then uploading coverage reports.
Or do we prefer to have similar to what's going… what's working right now?
Marc Pichler (Dynatrace) 00:04:29 Oh, I'm actually not sure, like… Right now, we're…
When we actually push, we do upload the coverage reports, but only from the unit tests, right?
David Luna Bistuer 00:04:45 Yeah.
Marc Pichler (Dynatrace) 00:04:46 Yeah, and I think….
Yeah, I think if we can, kind of repurpose, the changed CR workflow.
That you added here, to also run on main, that would probably be ideal, because then we get the full coverage whenever we merge to main.
I think I put the comment here, I'm not sure if you've seen it already, …
It's this one here. Just published that today, so, it's kind of new.
So… I think we still always have to upload some form of coverage on main, right? ….
David Luna Bistuer 00:05:30 Yeah.
Marc Pichler (Dynatrace) 00:05:30 So that we don't get out of sync, and also if we… like, since we always squash merge everything, it will get a different commit, ….
David Luna Bistuer 00:05:39 Okay.
Marc Pichler (Dynatrace) 00:05:39 ID, and then….
like, the coverage reports that we generated on the PR won't be associated with that new squash commit.
So I think regardless of
what we're doing, we always have to run some sort of coverage upload on main, if I understand that correctly, right?
David Luna Bistuer 00:06:01 Okay, yeah, that's good, then that's good. So, I have, also something in progress right now. I'm going to put maybe in the next comment, so the idea would be that this workflow
we'll just… if it's a PR, so we can have conditions on the steps, and we can do, just…
compile and testing the affected packages on PRs.
But then do a full, test everything and upload coverage of everything on Push on May.
Marc Pichler (Dynatrace) 00:06:30 Yeah, I think we don't even need to do the full one on push, right? If we also just do the diff there, we should…
be fine as well.
David Luna Bistuer 00:06:44 Okay, …
That deal was because, as you said, running the unit tests, made people do the coverage, and right now, it's like we're normally doing unit tests for everything.
Marc Pichler (Dynatrace) 00:06:59 Sorry, I think I, …
a little bit of a problem understanding. Yeah, right now, so, when we're pushing on… when we are pushing on mainfront, then unit test runs on every packets.
David Luna Bistuer 00:07:11 We're running a unit test on node 18, and then we're uploading everything.
Okay, yeah, I'll do a first change, and I'll add the push… the push event, and also in this PR, and…
Excellent, thanks.
Yeah, we'll use it for that. The test operations workflow is still the same?
It's untouched, so you can use it whenever you want, and… Whatever branch we want.
Marc Pichler (Dynatrace) 00:07:39 Yeah. I think, actually…
the comment that I had earlier was… earlier was just some confusion about, like, how, NX would figure out which thing to run.
But I think the, the need to actually have something like that, where we run test or versions, for all packages kind of goes away. I think…
you mentioned in one of the comments that I had on this PR here.
Let me see if I can find it, that, like, if there's some…
change in the top-level package JSON, or if there's a change in the package log JSON, then it will run everything anyway, and that's basically the only… the only case where we want to run everything, …
So, I think we should be good to just remove the workflow as well, the second Tesla versions workflow that is still there.
I think you deleted the one for the pull request.
And we can likely also get rid of the one from push if we also add, like, a push, ….
David Luna Bistuer 00:08:49 Okay.
Marc Pichler (Dynatrace) 00:08:50 trigger here, so, yeah. Then there's everything in one, and we don't have to worry about that anymore, and everything is…
Nice and tidy.
David Luna Bistuer 00:09:00 Okay, good. So, I'll do that. So, yeah, I'll make some updates in that PR, and…
And I'll ping you for another round of reviews.
Okay?
Marc Pichler (Dynatrace) 00:09:11 Okay, yep.
David Luna Bistuer 00:09:12 That's good. So that's it, and then the next topic, well, it's also related here. There is a comment in this PR as well that, from the coverage, it pointed that it was forgetting the incubator package.
But I found out that incubator wasn't included in… in the workspaces.
So, it's like, we are not running it, we are not compiling, so when we… the CI, world…
when the CI was working, it's not taking that in consideration, so my question would be, should we add
Incubator as… also as a part of the workspaces.
Marc Pichler (Dynatrace) 00:09:52 I think we can leave that out for now. So, if I recall correctly, the incubator, subdirectory was only added for, the AWS…
-Oh.
forgot what it was, some AWS package, and ….
David Luna Bistuer 00:10:09 I think.
Marc Pichler (Dynatrace) 00:10:09 Yeah, and …
the reason… I don't exactly know the reason for that anymore, but there's currently a PR to add that
Into the packages directory and actually publish it.
David Luna Bistuer 00:10:22 Okay.
Marc Pichler (Dynatrace) 00:10:22 So incubator will go away anyway. So you don't need to add it right now. I think that should be fine. So if we skip that.
For now, …
That's good. And then, the problem will go away on its own once we merge the other PR.
David Luna Bistuer 00:10:42 Okay, good.
Marc Pichler (Dynatrace) 00:10:43 Okay, so then that's it. Thank you very much.
Okay, thank you.
Alright.
Does anybody have… Questions or comments?
So this topic… If not, then thank you, and we can move on to Maribet's topic.
MG Marylia Gutierrez 00:11:10 Yeah, both PRs for the declarative config, so one is that big one that I mentioned the other week, and the other one is a new one that is…
Basically, parsing the config file using the package that we discussed, but this one is still very basic, because the majority of
parameters on that other PR that is not merged, so I cannot add them, so this one is just adding the ones that I had created by default.
But yeah, he's mostly to show the…
how it works with an actual file, and I use the ones that the SPAC use, so this kitchen sink is the one that they are using on the spec to do all the testing, so I just copy as is. And I have a few examples of things that they don't quite test there, but it's just, like, an invalid one from an invalid, and a one that is really short, so it would use the default stuff.
But yeah.
Marc Pichler (Dynatrace) 00:12:08 H.
Yeah, thank you for working on this. I was, planning to review this, but I, … Yep.
started, …
like, finishing up the pull requests that I had already started reviewing, so, there's, like, I'm trying to make more of a queue now,
MG Marylia Gutierrez 00:12:29 Yeah. Rather than….
Marc Pichler (Dynatrace) 00:12:30 stack-based reviewing, which is probably not the best in, like, getting toward PRs. But I, I think I posted one review here.
already with just some preliminary comments. But yeah, anybody who, if anybody has time, please also go in and review, review this PR. Having the declarative config and everything would be really, really good to have at some point.
… Yeah.
There's one question that, maybe we can, ….
MG Marylia Gutierrez 00:13:01 Oh, you just didn't like.
Marc Pichler (Dynatrace) 00:13:02 Right, well….
MG Marylia Gutierrez 00:13:03 Because, like, I saw this morning, okay.
Marc Pichler (Dynatrace) 00:13:07 Yeah, it was, … I just had some time in between meetings, and then I gave it a quick look.
So, there are these component providers.
In the specification, I'm wondering if…
Is that something that we want to migrate the code that you added now here over to this interface, or what is the plan for that?
MG Marylia Gutierrez 00:13:33 Yeah, so it's not quite there yet, so there is a part, like, the… for example, all the issues that I created.
is based on the final table of things that it needs to specify. So they want the parsing to return
a thing that they call a config model. So this is why I call it config model. So the model itself then can also return component attributes. So this is, like, on top of this thing. So this thing, the way it is, is not gonna change. It's gonna be like this.
And then those extra things are extra functionalities or extra functions that you can return. Just the objects. We have, like, some things like just the trace exporter, so you can break down on just that component and so on, but the basic of the model itself, it is like this.
Marc Pichler (Dynatrace) 00:14:23 So everything would be in the configuration package.
MG Marylia Gutierrez 00:14:27 Yes.
So yeah, the part that I still don't know what it is, because they use it a lot of, like, the Java to make some of the decisions, and it works a little different for us in several cases, so…
there are a few things that I haven't decided yet how to do it, and I might not put on the configuration, because, like, some of them is, like, return, for example, the trace exporter, like, the whole components. I don't think we should move the trace exporter to the configuration.
I think you should continue existing on the… whatever is the package that exists now, but I need to be able to pass the configs required to create this, so I might have, like, an interface of…
returning this, but leaving the actual implementation to some of those packages. So I think that would be the only part that would do slightly different, but it's gonna take me a while to get to that point. So, when the time comes, I'm gonna check with the, like, the group itself, the spec, if that is a good approach.
Marc Pichler (Dynatrace) 00:15:34 Yeah, so the reason why I'm asking is I'm mainly worried that, like, the OpenTelemetry configuration package would be, like, a very large package that has to be modified every time when we add new features to, let's say the Trace SDK or something like that, then every, …
every change to that would come with a new configuration and would modify both the packages. I feel like it could be…
It could become quite difficult to manage, if…
like, every change touches the same part of the code at some point, so the…
configuration, the component provider's interface approach.
Sounds to me like something that is…
They are to help alleviate that issue a little bit, because if you can have a component provider for all the trace configuration in
the SDK trace package, for example.
Then, … It would.
have, like, you would just modify the SDK trace package, right? And, then…
Combine all of these together in one of the config providers.
And, let's say, SDK node then just pieces together, like, the config provider for that.
And, … Yeah.
It's basically the same as all the…
Plug-in interfaces that are being implemented by all the different, sort of, packages.
MG Marylia Gutierrez 00:17:11 Because the way that I was taking, like, the configuration one is…
basically responsible to, like, parsing the file and returning the values. The actual creation of whatever is need is up to whatever is the package that is using that. So I'm not going to use the configuration to create any of the things. It's pretty much focusing on… because the… I don't want to have…
for example, if I'm gonna say, okay, like, one of the exporter, you have to be the one parsing and editing, but that is gonna have, like, might change the formats of the file, we might have to change, for example, the…
If it is using, like, the actual value, or if our environment variable, so this is why I want the configuration to be the one handling all of that. And this is the configuration model. It's just the object that returns whatever is the value that was parsed.
And then the actual creation is up to whoever is using that.
I don't know if that helps?
Marc Pichler (Dynatrace) 00:18:12 Yes, …
I'm still trying to figure out if there's anything that we can do to move some of the stuff to the actual packages, themselves.
MG Marylia Gutierrez 00:18:22 Who's my concern?
Marc Pichler (Dynatrace) 00:18:24 Similar.
MG Marylia Gutierrez 00:18:24 This, like, because we… if we would say, okay, the… one of the exporter, whoever's using it is the one that have to, like, read the files, and you might call, like, the functions, but imagine that we actually change the format of the file.
You would have to go and change all the packages that were using the configuration file anyway, but you would have to, like, or add the function or stuff, but if I just always return, like, the interface of the config model, I don't have to think about how the parsing is done.
Or, like, because even, like, if you see, the first line shown is always, like, the file format, so this is, like, current is an RC, so that is the thing that might change. And I don't want to… whoever's using it have to think about that.
Marc Pichler (Dynatrace) 00:19:12 Yeah, there's, … I'm currently trying to think of how they're doing it in the Otar Collector. …
I think some of the config stuff is still in… … in the, …
Up for the sport, the extra… components, right?
MG Marylia Gutierrez 00:19:41 Yeah, so that was one… that was what I brought, like, on the save, because I noticed, like.
they were doing different on different places, like, Collector was doing away, the Java was doing a way, and they have, like, if you want to use environment variables, follow this path, if you want to file, use this, and some places are reading that, and I was telling them.
I'm having all of them in that same, like, package, and all of them that agree that this was the best way, because they are having currently issues with the way that they implement it.
And they say, like, it's being really difficult, like, to maintain. They cannot easily find… if they have to make a change, like, what are all the configs that are getting affected? And they have to update every single place. And they were saying, like, oh, I wish we had done this on a single package that is just parsing and returning, we don't have to think about it in other places.
So this is why I kept with this approach.
Marc Pichler (Dynatrace) 00:20:40 All right, I think I still have to check maybe some other places as well to see what… what trouble they are running into, but yeah, I would definitely give another round of reviews. Thanks for, walking me through it, here.
MG Marylia Gutierrez 00:20:55 ….
Marc Pichler (Dynatrace) 00:20:57 Yeah.
Yes, … Does anybody have any… Additional questions… Or comments about this?
… If not.
then, yeah, I encourage everybody to have a look at this. It's likely gonna shape a lot of the, …
changes to…
some of the packages, like, the SDK packages and how they are configured, and it's probably gonna play a very large role in things going forward, so it's good to have as many eyes as possible on these PRs, so if you find some time, please head on over and have a look at this.
MG Marylia Gutierrez 00:21:47 Next one.
well, it's not actually me, but I put it there, just because I see there is a new instrumentation that is adding new code owners, and I just want to check if they are here, because that is an issue happening with a lot of
repost, and then… because I'm part of, like, the contribut experience that we are trying to address, and I see happening here as well, that a lot of code owners, sometimes they become a code owner, but they stop replying. And we can see, like, from our review, from week to week, tagging sometimes the same people over and over.
So I just wanna… I just put it here just to check if the people who created it here is… are here, and understand what is in tile of being a code owner.
Anyone here from this PR?
Let's what it looks like, yeah.
Marc Pichler (Dynatrace) 00:22:41 ….
Eric Han 00:22:44 Hey, yeah, that's me.
MG Marylia Gutierrez 00:22:46 Okay, cool.
But yeah, don't want to talk a little what is this package, and yeah, I just want to bring this concern that
because you were, like, are now gonna become, like, the co-owner for this, we expect you to, like, help with reviews, and be the one, like, probably gonna tag automatically for PRs coming up from this, and if you actually have the bandwidth to actually do reviews.
Eric Han 00:23:19 Oh yeah, I… I think I will, yeah.
Or, if not me, … the other assignee… the other assignee, Michael, should be able to….
Marc Pichler (Dynatrace) 00:23:37 And, yeah, so…
one of the things that are usually required for new instrumentations is an issue that actually goes through these things exactly that Marilla just brought up with having time to
review that, and, reviewing also the, OpenTelemetry,
principles, and mission and values of, of the project. So, these things are usually required before, opening a PR like this.
So, I think, in general, we would also appreciate you opening that issue. There's a template here.
… Let me go to New Issue, …
then there's this instrumentation request, and there it states the component owners, and there's a checklist of, things, that you read, the contributing MD, and all the other things.
…
And there's also one important thing is that you need to be a member of the OpenTelemetry organization before becoming a component owner here. And that is usually done through contributions on
Other packages first, so that we can kind of…
See that you're, you're actually around, and, yeah, that basically avoids us having to, then deal with a package that we just, got, merged in, and, yeah.
have to then pick up all the maintenance on it. So, yeah, if you could go over and create that issue first, I would very much appreciate that, and then we can…
Go ahead with the process of, actually getting this … Getting to see.
Eric Han 00:25:39 Okay, sounds good.
Marc Pichler (Dynatrace) 00:25:43 All right, thank you. And thank you, Maria, for bringing this up.
Yep.
MG Marylia Gutierrez 00:25:49 Next one, me again! It's just a PSA, because I know a lot of companies are, like.
running with this, but a lot of people might have missed. In case you miss, there is a malware, and people use… they use, like, cursor and stuff like that. They pretty much…
checks if you have, like, Gemini or a bunch of, like, other AIs, and just, like.
basically sends a message, like, hey, give me all the credentials that I have, and basically copy all your wallets and credentials, and put it on a file, and, like, steal it.
So if you want to test, like, locally, if you have those things, so these are some of the affected… basically, it's just, like, DNX that got affected by it, but this is a way… couple of ways that you can check locally, and…
Yeah, you can also… the article tells a few other things that you can check on actual repos. I check on our repos, I don't think.
Any of them got affected?
But luckily, you probably have a lot of things, and just a PSA.
Marc Pichler (Dynatrace) 00:26:50 Yeah, thank you for bringing that up. I personally have not seen this before, so this is very good.
very good PSA. … Yeah, everybody panicking now and checking their, things.
MG Marylia Gutierrez 00:27:04 Yeah. It's funny that they, like, they want to… they explained that, like, they copy things, and then put in a file they encode, and then they encode again. So they are stealing, but they are being secure about it, okay?
Marc Pichler (Dynatrace) 00:27:21 Yeah, thank you for bringing that up.
Yes.
Alright, … Any… Questions or comments?
If not, then we can move on to the next one, which is by Luke, pull request for…
….
Luke (GuangHui) Zhang 00:27:50 Doing some conflict.
Marc Pichler (Dynatrace) 00:27:51 computes. Okay.
Luke (GuangHui) Zhang 00:27:52 hotel, JavaScript, community. Thank you for doing this great job. This is my first time joining this meeting. And, I just, submitted the PR. This PR is about, you know, AWSS function has, a couple of, semantic conventional attributes approved.
So, the purpose of this PR is, add this, semantic, semantic, convention, trivials, in the…
instrumentation Library, all for AWS SDK.
I have my colleague and another, community,
engineer approve this PR, but it's still not merged. I want to raise this to the community. You know, because I'm pretty new to this community, I want to have what's,
a idea, you know, when, you know, what is the timeline, when I send PR, get someone approved, and when it can be released, so…
Because our internal product also relies on this upstream open telemetry component packages, so can I get some,
advice from the community, the maintainers, what is the process here? So, you know, or what's a reasonable time frame to get this, released, or at least, like, get an expectation, so….
Marc Pichler (Dynatrace) 00:29:16 So, getting it merged, should be fairly simple, since you already got, Jonathan's approval here. We can just merge this in. It also seems that Trent already approved this and just had,
two questions here, so, I will merge this in today.
And, getting it released, we can cut the release just tomorrow, if that's okay with you.
Luke (GuangHui) Zhang 00:29:46 Yeah, yeah, definitely. So the cadence is that we have a monthly release.
Or do we have a cadence, a radius cadence here, or…?
Marc Pichler (Dynatrace) 00:29:55 …
We don't have a release cadence here. It's basically just an on-demand thing. Whenever there's a need for a release, we cut the release here. One thing that you can do, if you're actually interested in getting a new release out.
There's this release main request that, is being opened, …
periodically, so after one release is out, and at least one PR has been merged, then this release main PR will be opened.
And if you go on over and approve this one, then that signals to us that there's people interested in having another release, and we will then make sure to cut the release in a timely manner.
….
Luke (GuangHui) Zhang 00:30:41 Gotcha. Gotcha. That helps. Yeah, I want to get more involved, contribute more to this community.
Ping me if you have, you know, you want someone to have some task to do.
Marc Pichler (Dynatrace) 00:30:55 Marshall, thank you. One, thing that, … I'm not sure if you… …
I guess you work with, Jonathan, as well? Yeah. Yeah, one thing that you could ask him, since he, has triage permissions, actually, on the repo, is to add the has…
owner approval labor here, on the PR, once he approves the, PR, so that we can, …
like, it shows up in the filters, so if there's PR that has been approved by a component owner, we see that, and then we'll have a look a bit quicker, because we usually rely on the component owners to actually do the review for
the packages, and if we see that an owner has approved, then we just give it one quick look and merge that in. But if the label is not there, then, usually it's a bit more difficult to actually find these. So, yeah.
Gotcha. Do you have a… do we have a list?
Luke (GuangHui) Zhang 00:32:02 for… for contributors to pick up, do you have, let's say, bug list or technical debt list, so… ….
Marc Pichler (Dynatrace) 00:32:09 We don't have, like, a specific list, there's a bunch of issues usually everywhere, but, …
Yeah, on the repo, there's… there's probably always a few packages that are more interesting to some people than, to others, and we usually try to label, anything that's,
let's say, related to the AWS SDK with these labors, so if that is something that you're interested in working on, you can just pick one of these. There's usually quite a few bugs, here, just
lower priority ones, but, still important to work on. So these, …
These, things, are always appreciated if you, pick these up.
And yeah, stuff like updating dependencies and things like that is also massively helpful, because the repo is so large, that, it's almost a full-time job to keep these things up to date. So…
If you find yourself with a few minutes here and there, that's also something that's always appreciated.
Luke (GuangHui) Zhang 00:33:22 Gotcha. So this second meeting covered both the contribute repro and the API SDK repo, is that correct?
Marc Pichler (Dynatrace) 00:33:29 Yeah.
So we do both, here, here in this SIG meeting, we just combine it all together. So any questions that you have, you can also, come on that meeting and, ask questions here, or, creating issues, to…
generate discussion is also, fine. We also have, the…
CNCF Slack, so if you sign up for that.
there's channels, Author.js dev and AutoJS, that you can join, where the dev part is mainly, PR, reviews and, questions around developing, whereas AutoJS is more around,
like, questions about usage and stuff like that. So a user would go into the AutoJS channel, and somebody working on a project would go into Auto.js dev. It's usually good to follow both, just to get a feeling of, what's going on right now. But, yeah.
Luke (GuangHui) Zhang 00:34:35 Yeah, I am there. This is really helpful. Thank you, Mark.
I appreciate it.
Marc Pichler (Dynatrace) 00:34:40 Thank you.
Wait.
I guess we can move on to…
bug triage. Yeah, as always, if you have any topics that come up while I'm talking through the bug triage, please feel free to just interrupt me, and we go back to the agenda and talk about your topic.
… Alright.
The first one here is HTTP connections not released after OpenTelemetry integration? …
Using FLV.js to play video streams.
Guess it's happening in the browser.
… HTTP connections remain active and are not properly released.
Seems to be using Instrumentation fetch.
And which versions are they actually using that's…
newest one, so this should be fine. I seem to remember that there was some issue in the past where
… These long-running connections, like streaming stuff in, would cause…
some trouble, but I thought we had fixed that already.
… Let me just check.
Here, real quick.
simulation fits… … Infinite fetch request residing in a memory leak.
That seems to be somewhat different. So that is definitely a P1 bug. … belongs to Instrumentation. Bitch.
It seems that there's just something that, …
Not correctly… doing something, so… let's labor that as P1.
And, yeah, if anybody has time to look at this one, would very much appreciate it. I guess it's…
bit more… Difficult to reproduce this one, but… …
So… There's some steps for reproduction, but I'm not gonna…
put the reproducer-provided thing on there without actually trying it out.
Yes.
probably won't exist.
That needs some more.
looking into.
And moving on, …
Still no response here.
So, nothing to do for this one.
And we can move on to Contrip.
Where we don't have any new bugs, which is nice.
And then we can move on to, old PR triage.
…
Looks like this one is actually already, … Proofed.
We did ping Jonathan a few times, the client gave this a review, so I'm just gonna update the branch here and merge this in.
MG Marylia Gutierrez 00:39:25 It looks like it's still waiting for the approval code on her.
Because, yeah, I see the requested it already.
Marc Pichler (Dynatrace) 00:39:32 You re-requested the review, yes, but I think, …
Actually, Brent made some changes himself, …
But he just regenerated some files.
I think we should be good to merge this in regardless without, Jonathan's approval.
There was enough time to have a look at this one.
I wouldn't feel too bad for actually, … And then this one.
Yeah, I wouldn't feel too bad for merging this one in without, Jonathan's approval here.
I think we've been… Trying to get ahold of him for… A few months, so, …
You can't.
But you're removing my name from this one, because I just updated the PR and didn't do anything.
Alright, … We've lost the… Thing here, so this one's gonna get merged.
The next one, didn't have any activity, and, is probably still stale.
Then there's this… thing for the page view instrumentation plugin.
…
I might do conventions… Still… blocking this one, so I guess we'll wait for that.
Then there's this… Equalize instrumentation that's being added. …
This one is missing the tester versions Yammer, so if we run the tester versions here, it will actually, …
Just fail, so that's the thing that…
I requested changes for, and just this knit here, …
So, still waiting for that overall.
Looks good, though.
So this one here has also two changes requested on it, …
Component owners file's still missing, so, … Person nothing to do here.
And there is this…
Barcelona still has changes requested, the explicit permissions are now, … Required, since, the security…
sequined through and made sure that everything has explicit permissions. We should also add it to this.
….
Hector Hernandez 00:43:03 Yeah, thanks.
Marc Pichler (Dynatrace) 00:43:03 This action right here.
Hector Hernandez 00:43:05 This is in my queue. I will take, addresses, today or tomorrow, so… but thank you for….
Marc Pichler (Dynatrace) 00:43:12 Thank you. Yeah, overall this one looks good already, so once the changes are made, I can just merge this one in and we can see it in action.
Hector Hernandez 00:43:22 Thank you.
Marc Pichler (Dynatrace) 00:43:23 Thank you for watching, I'm just… Alright, …
Then the next one is, adding something to… the AWS, SDK.
Instrumentation, … Seems like quite a few comments addressed already 3 weeks ago. … And… been…
There have also been a few more changes.
That still need to be revealed. I actually put this on the list of, …
CRs to reveal, and I guess, …
We'll also need a review from… …
These three here.
…
Because these are the component owners for this batch, if I recall correctly.
Trent just assigned himself, to not forget about it, if I…
Recall correctly from the last few.
times we stumbled upon this PR.
Yes.
It's click.
Okay.
Then the next one has an owner-approver already. … It's the AWS detector…
I did the owner approve her labor yesterday?
Just giving this a quick look to see if there's nothing…
out of the ordinary, and then I can proxy approve this one.
or Jonathan?
We're gonna run the workflows again, and then merge this in later.
David Luna Bistuer 00:46:25 This is not one.
Marc Pichler (Dynatrace) 00:46:26 And the next one, yeah, we just discussed this one, and the next one is…
Yeah, this one I actually wrote myself a note already that we will have to…
deal with, inactive component owners somehow. Unfortunately, I myself don't have a lot of,
a lot of experience with GraphQL, so…
It's very, time-consuming to review, but I…
put this on my list again, so that I don't forget about it, and hopefully we'll have some…
outcome for this, the next time. …
David, thank you for, also saying to Luke that you will look into this, appreciate it.
…
Great.
Then the next one is… Actually, also already approved, so… … Yes.
I'm just gonna… Update this, and also merge this in.
I'll merge… I didn't do anything for merch.
… Then the next one… E-Sport.
The package auto-instrumentations node.
… no reviews yet, and the maintainers assigned, because we maintain the auto instrumentations node package. I will…
Give this a look, more…
It's kind of very difficult to get this right, because the things have to be merged in, like, a specific order, and we have this, other node disabled instrumentations and other node-enabled instrumentations, and the way that they work is…
Fundamentally different.
And they override each other and whatnot.
So, … yeah.
impossible to make a car here right now, but I will have a look.
Later.
I'm right.
Then, we have… this PR, which does tees up for, … Comment.js and ESM output.
Bum.
David Luna Bistuer 00:49:47 Yeah, maybe we want to talk about this, but maybe in the next… next week.
Because there is this PR, and also there is another one. This one is using TSOP and ESPL under the hood.
to actually, output both formats, CommonJS and ESM.
A side effect of that is that it bundles everything on just one file.
Which is… could be good, for performance reasons.
I don't know, it's maybe… it's a better test. And the other PR, it's on the same implementation, it's on Ditchie, but instead of using this app, it's using the same approach that Jamie did a long time ago.
Using TypeScript and, and, different forms, so using the, the, the, the existing tooling.
for having both formats. The difference is… is… basically, the main difference is that
This app bundles everything in one file, one common GS file, and one ESM file with all the instrumentation code.
and… and the…
approach with the current tooling is just, well, it emits as many files as we have, so one JS file, one common JS, or ESM file.
burned TypeScript file.
Okay, that's the main difference.
ESBuildBuild… ESBuild is faster, but it's too slow. It almost does not touch up anything.
So maybe, as a… A safety net, we should… if we go that path.
We should add a compilation without emitting anything.
Just for type checking. So, I don't know, we have to discuss that and see what's the approach that we like best.
If we continue to, … the current tooling, or using AdSenseBuild to our tool chain?
Marc Pichler (Dynatrace) 00:51:33 Yeah, I think, …
I, myself, I kind of lean towards using ESBuild, and then, doing the roll-up thing, …
I would prefer not to use the TSUP directly. I did.
David Luna Bistuer 00:51:50 HD.
Marc Pichler (Dynatrace) 00:51:51 look into this PR, and then went to, … what package was it? …
open future SDK, which is also CNCF,
project, and I checked how they do it, and they, actually use the ESBuild, and,
roll up.
directly, to accomplish the same thing. So they're basically doing, as well what you're doing here. But, instead of using TSUp, just using the tools directly.
And the reason why I would prefer it is because there's one less dependency, that we have to worry about, like, …
For, first things….
David Luna Bistuer 00:52:35 Like, it's true.
Marc Pichler (Dynatrace) 00:52:35 the thing that happened with NX, that we just saw earlier.
So, ….
David Luna Bistuer 00:52:42 Yeah, we could try those, so let's, let's first decide on what…
But we choose, and then maybe we can… this could change, and then using directly ESBuild and rollout, I don't know.
Marc Pichler (Dynatrace) 00:52:55 Yeah, let's discuss this next week, as you suggested earlier.
David Luna Bistuer 00:52:59 Okay, I'll put the item on the agenda.
Marc Pichler (Dynatrace) 00:53:03 Yeah.
…
And then hopefully we'll have your other PRs crossed off the list already, and we can focus on these.
Alright.
… then we can move on to the next one, I guess. …
And according to action, if anybody has, like, strong opinions one way or the other, please comment it on the PR, or just join the SIG meeting next week, and then we can…
Continue discussion there.
Alright, here we have… pull request for instrumentation COA to add support for COA3.
… Steam… Seems to have… Ruth the PR, but he's not an owner here.
Bum…
Some changes that were requested are already applied.
Let's just see how large this PR is, actually. It seems to be fairly straightforward.
… and also seems to do some changes for…
HTTP… Exibutes.
Yeah, seems to be fairly straightforward.
So, I will…
put this on my list of PRs to review as well. If anybody else has time, please also have a look. This is actually an unmaintained package, but we can easily add support for COA3.
I guess there's nothing that speaks against merchant's PR as well.
Moving on…
This one is approved, …
Looks like… I'm here… Didn't have time to have a look, probably, so, …
Or so just merge this in.
…
workflows, so that… This… oh.
Make sure you'll run and dis…
Actually gets merged, because two of the checks are actually required.
… renovate PR. I guess. We can skip these.
So now, … then… And open the draft PR, so we'll skip this one as well.
There's one for, … Instrumentation AWS Lambda. Support streaming handlers.
-Oh.
We're silent, being… Owner of one of the most, …
the packages with the most traffic, and the AWS one, I always feel bad, like…
Bing, because he has so many, …
so many PRs to have a look at.
This is probably one of the most well-used packages here, so, …
Yeah, it's a lot more workload than for some of the others.
…
Alright, next one is renovate, … Instrumentation AMQP.
It was fairly recent, 3 weeks ago, Trent reviewed this one.
Just one, …
Was actually blocked on semantic conventions.
So, I'm gonna check real quick what the current status is, because I'm also not up to date on this. Oops, no, that's not the correct place to have a look.
…
It's actually still in development. So, guess this one is still blocked.
What is it actually? Once is it actually changing?
Controlled by the messaging environment, however.
So, that's actually… Doing a bunch of messengery things, …
Or just need to wait. And see if that is actually part of the effort to get something stabilized, or if they just misunderstood something there.
… This one we were just talking about earlier.
… Seems that there are some conflicts now.
…
And the person's not on the call anymore. I will try to find them on Slack and ping them about it, but, …
Yep.
Anyway, we are out of time. Thank you, everybody, for joining, and…
Have a nice week, and see you next week!
David Luna Bistuer 01:00:04 Okay, bye.
Jackson Weber 01:00:06 Yep, have a good one, guys.
Marc Pichler (Dynatrace) 01:00:07 Thank you, bye.
