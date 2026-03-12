SIG: JavaScript SIG
Date: 2026-03-04
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 01:24 Hello?
**Andrei Borza (Sentry)** 01:29 Blue.
**Trent Mick** 01:35 Bonjour.
**Marc Pichler (Dynatrace)** 01:49 Get started. Welcome, everybody.
First thing here on the agenda is Norilia with updates from contributors' feedback.
**Marylia Gutierrez** 02:09 So yeah, it's been a while since I have been gathering, like, more feedback. So yeah, just want to share. Good. We got, like.
out of 5 stars. Yay! So, a lot of comments. A lot of people don't leave comments, people, when they… a lot of them are just like, everything's good, kind of thing. There were a few about… time for, like, review on PRs. Some of them are taking long, and one suggestion is… so I don't know if we have any idea for this, just to be, like, explicit how to run tests the exact same way that CI does, because I think people are sometimes having, like, different results, but I'm not sure if we have any guide for this, if we have… we can add somewhere. But yeah, just wanted to share some feedback here.
**Marc Pichler (Dynatrace)** 03:00 Thank you. So, I think for this suggestion, there's definitely some stuff that we could do. We do have… A few different test suits, and the normal test suit just runs, the Node.js tests.
the browser tests are left out, if I recall correctly, so maybe we could provide some convenient script or something like that, that people can use to, like, run that.
I guess the thing that people run into the most is the changelog lint check.
So maybe there's also something that we can do to… alert people locally, when they run the Linta, to add a changelog entry or something like that. Not sure if that would be at all helpful, but… Yeah.
running all the tests, I think, would be a good first step to, Get everybody on the same page, and then we can iterate on that.
Trent…
**Trent Mick** 04:09 I just had a comment. There's a… the contributing doc in both of the repos has a, like, here are the commands to get started, which is fine in core repo, but in contribib… Now, if you scroll up a little bit from there, I think it scrolls you down. Yeah, the quick start, those commands.
**Marc Pichler (Dynatrace)** 04:24 That test is gonna fail because it's not running the test services, so…
**Trent Mick** 04:28 I think that's because we changed up test services needs to be a separate run thing. Actually, does that fail, or do things get… I think it just starts failing? I don't know. Anyway… It's a fair point, really.
**Marylia Gutierrez** 04:43 Yeah, I say this, and then, like, even when I am, like, core one, and if I am on, like.
the root folder, and I just run, it just fails for me. It doesn't even run the test, so I have to go by… I still need to think…
**Trent Mick** 04:55 Core, or uncontrib…
**Marylia Gutierrez** 04:56 like, me, for core, it fails, like, a couple of things that I need to figure out. It's a bunch of, like, messes from, like, gRPC, it was, like, every single time, I was like, I need to figure out what is this, and then it's a problem for future Marillia, and I never look.
**Marc Pichler (Dynatrace)** 05:09 the chair PC stuff.
Yeah, it might be… .
**Trent Mick** 05:15 Well, the OpenTelemetry… on behalf of the OpenTelemetry contributors, we would encourage Marillia to open it.
For those of us, if you have details, I know it takes time, so… because sometimes you just figure it, so just, like, clean it up, and then it'll run, but yeah.
But I think that's helpful. I think I'll look at updating and contributing Quick start for control.
grid. I would think for core, that just works as written, but maybe not.
**Marc Pichler (Dynatrace)** 05:43 So the gRPC stuff that you were talking about, I think, is the compile step.
That is required before running the tests. I've seen people run into that quite a few times, because for most of the, For most of the things, I think it works without running compile.
Before?
Because we use TS Node, the tests just work.
But for the OTRP transformer and for the instrumentation gRPC package, we need to generate the source files for the gRPC clients.
End service, so… I think that might be what we were running into, but… I'm not sure.
**Marylia Gutierrez** 06:35 I'm just running out just to see if I missed something, yeah.
Yeah, my compile is the one that fails.
**Marc Pichler (Dynatrace)** 06:45 Hmm.
**Marylia Gutierrez** 06:46 I don't know, maybe, yeah. Well, right now I'm in the middle of… updating stuff, so it's probably gonna break. But yeah, I can take a look later, and I'll let you guys know.
**Marc Pichler (Dynatrace)** 06:57 Yes, it would be interesting to know, what it is, so we can fix it. It must be very annoying to have this happen more of the time.
Alright, Yeah, thanks for, bringing these things up. I think there's definitely some places where we can improve, so we should definitely look into that.
**Marylia Gutierrez** 07:18 Do you want me to open an issue for her?
**Marc Pichler (Dynatrace)** 07:22 Yeah, probably an issue works best, and then… I will probably have a look as well to see if there's anything that sticks out. I think I've run into all the problems that one can run into by this point, so I might be blind to some of them, or I'm for sure blind.
**Marylia Gutierrez** 07:46 Maybe have even, like, maybe having a session, like, troubleshooting could be helpful, because, like, if there are, like, common things that happen, it's just like, oh, if you see this error, this is how you fix it, kind of thing.
**Marc Pichler (Dynatrace)** 07:58 Yeah, ideally, we would just, like, sort all the problems out, so that they don't occur in the first place, but I guess there's some places where we can do a troubleshooting section or something like that, I think would be… would be helpful.
Alright, any… Questions, comments, ideas, thoughts?
Disturst…
**Trent Mick** 08:31 I was just saying I opened that on me, I'll take a look after. For…
**Marc Pichler (Dynatrace)** 08:34 Thank you.
**Trent Mick** 08:35 Second trip, at least.
**Marylia Gutierrez** 08:37 Oh, I like this, this new LLM. I just think, and then Trent opens the issue for me. I like this. How do I…
**Marc Pichler (Dynatrace)** 08:53 Right, let's move on to the next topic here, if there's, no additional… Things, Andre, with some information about, how… Stuff behaves after… EULD of a Node.js version. Thank you for writing that down and, looking that up.
**Andrei Borza (Sentry)** 09:19 Yeah, thank you so much for taking this into… into account.
I can't give you hard numbers, but basically, as you can see.
Within the first 3 months of… Node being end-of-lifeed. About 8% of projects that had at least one project with Node 18, Switched over.
and then within, like, 6 to 10 months, it slightly increased to 30%. I mean, it's still… it's still not great, but… It's a trend in the right direction.
And as I mentioned here, we did not have any announcements around, end of life of Node 18.
This time we will have this as a pinned issue, and I think that's gonna help, drive some agency.
But, yeah, it would be nice if we could delay this a little bit, at least.
**Marc Pichler (Dynatrace)** 10:20 Yeah, so, It looks like the numbers are still very…
**Andrei Borza (Sentry)** 10:29 Yeah.
**Marc Pichler (Dynatrace)** 10:30 very low after even, 10 months of, it being year, which, I guess it's also kind of expected I, see a lot of, a lot of people running even older versions than this at some point. So, yeah, thanks for…
**Andrei Borza (Sentry)** 10:49 Yeah, at the same time, I definitely understand also the, you know, as maintainers, having to… Deal, especially with, upstream libraries, you know, upgrading and that kind of forcing your hands as well. We've all experienced that as well, so I definitely understand.
**Trent Mick** 11:10 And that's for 18, never mind 20.
**Andrei Borza (Sentry)** 11:12 Yo.
**Marc Pichler (Dynatrace)** 11:17 Yeah, I guess, with this new information, we're gonna take some time to, kind of Internalize these numbers and try to come up with a better timeline for this.
So… Yeah. I don't have any… plan in mind right now. Definitely look into these numbers a bit more closely and try to see Which numbers we have here at, Dynatrace 2.
kind of form an opinion about the whole thing. I also see if I can publish these numbers there, so that, we kind of have a good base of information here.
**Andrei Borza (Sentry)** 12:04 Yeah, I'll definitely pin an issue to our repo, that people are… You know, expected to… to get this dropped eventually.
And compare, see if that drives numbers up.
**Marc Pichler (Dynatrace)** 12:19 Yeah, thank you. I think this is a good idea.
**Trent Mick** 12:23 I don't know if there's… this is maybe… a bad idea, but throwing out ideas. Like, is there any kind of open telemetry survey thing?
That's regular, or… Where we could get questions like this on there.
Some way to reach out to… OpenSelemetry users.
I'm looking at Marillie, I'm waiting for her to jump in.
**Marylia Gutierrez** 12:46 No, yeah, because I'm thinking the one that we do, sometimes we have, like, we… we can use, like, the end user SIG for sometimes surveying like this. We did this for, like, Collector and some other SIGs that requested. We do have, like, a general that we want from time to time. I'm just trying to think when is the next one, because we try to not have, like, several at the same time, to not overwhelm people. But I… if you have, like.
things that you want to be interested in knowing, yeah, you can let me know, like, give a list, and I can work with the end user seg to… so we can put it out someday.
**Trent Mick** 13:22 Okay.
**Marc Pichler (Dynatrace)** 13:24 And it would be… I think having some sort of survey would be really helpful. Also, if we can batch that with other things that we would like to know.
**Marylia Gutierrez** 13:34 Yeah, you want to avoid having, like, one and then the other. No, no, no, think about everything that is helpful, yeah.
**Trent Mick** 13:42 What else would you want to know?
**Marc Pichler (Dynatrace)** 13:44 I don't have anything, like, really, planned out right now, but I guess there's definitely some things that we… Could ask while we're at it.
Possibly as an action item for, Us to think about that, So that we have a good list of things we want to know.
So I guess if there's anything you're particularly interested in, either here in the core repo or in the con repo with regards to compatibility.
Maybe also instrumentation compatibility for, oort, package versions might be interesting.
Hmm… Because that's something that we… Keep carrying with us as well is, Very old versions that haven't been published in, 5 or more years.
That we still support in the instrumentations, so… That might also be something that's interesting for us, but yeah, if anybody has anything, Would probably be good to, collect these things on an issue as well.
I'll take some time to type something up, so that we can collect these things on an issue, and then, We could, look into getting a survey like that going.
**Trent Mick** 15:27 I guess… yeah.
My guess is, from the browser developer side, the push would be to move to more and more recent versions of Node, because Mostly in tooling, I guess.
Seems… because obviously they don't really care about the runtime node version as much.
**Marc Pichler (Dynatrace)** 15:46 Oh.
**Trent Mick** 15:46 Yeah. Interesting.
**Marc Pichler (Dynatrace)** 15:49 Yeah.
I guess for tooling… There must be some better way to test all of these node versions without possibly running a full test suit as well.
I wonder if we could, Split up the test suite somehow to… Have a reduced set of… Tests for end of life.
Note versions, but still.
**Trent Mick** 16:22 You're talking about the length of time to run CI these days?
**Marc Pichler (Dynatrace)** 16:27 Yeah.
**Trent Mick** 16:27 Mainly Isegol, yeah.
**Marc Pichler (Dynatrace)** 16:29 It's… it's that, and also, if… The set of tests is reduced, and we use some different test framework for it.
We might be able to get away with not updating it as often.
Yeah, because right now, what we have to do is, like, we have to make sure that everything that we use in terms of dev dependencies works on all Node.js versions, even though that might not be really necessary.
So if we could make a change to that somehow… Then that would already improve things.
Because then we have, like, a main… Set of things where we run the full test suit.
I'd say that those are just the Node.js versions that are officially Supported, and then we have some additional ones where we still make sure that it works.
but we don't run order tests for it.
would be… Pretty big change, though. So… I'm not sure how feasible that is.
**Trent Mick** 17:48 Yeah, I don't know. I haven't thought through.
Those issues.
I mean, if we're talking about just a package that's just browsers, then we only need to run it with one version, right? I guess we already do.
**Marc Pichler (Dynatrace)** 18:00 I think we don't skip the browser… Yeah, yeah, I guess we just run the browser tests with… one Node.js versions, so these we can upgrade.
But… We still compiled the whole thing for all of them.
**Trent Mick** 18:22 Yeah.
**Marc Pichler (Dynatrace)** 18:23 So all the build tooling and everything has to… Be supported on older versions.
I guess just getting rid of the build step.
And just running the tests in other places would already… amplify things in a way that we can support more Node.js versions for longer.
**Trent Mick** 18:48 separate but related question, is node versions supported for the API?
And whether we ever talk about dropping that, or do we tie that together with various talk that we've had for API V2.
**Marc Pichler (Dynatrace)** 19:05 Yeah, with the last, pump. I think we didn't change the supported versions for the API at all. We did not.
Still supports back to Note 8, I think.
**Trent Mick** 19:25 Okay, flood stuff.
**Marc Pichler (Dynatrace)** 19:27 Yeah.
there's lots more to talk about. I guess let's move that to another time. We'll continue the discussion about the… Minimal supported node version on this issue, and then, find some… Things to ask folks on, On a survey, which we then can use to base our decisions off of.
Alright.
Any additional thoughts on this?
But then, move on to the next topic, which is Mobility.
**Marylia Gutierrez** 20:11 Yeah, this is just a really quick one that is just exporting things, because following PRs are all breaking, because… I need those things exported for the meter, exporter, and the trace kind of thing, so yeah.
It's a quick one. And I know that you are all dying to know, and I just tested, and it's working, the test is on core, so you can be relieved.
I don't know, I just went back to man, cleaned it up, everything, and it's working, so the secret is just complaining out loud.
**Marc Pichler (Dynatrace)** 20:44 I'm sorry, I didn't fully get what you were talking about. I thought it was still related to,
**Marylia Gutierrez** 20:50 No, no, no, this is one thing, yeah. The other is, like, the other topic we were talking about before, like, that my… the core, that it was failing for me to compile and the tests, and I just ran it out, and all of them work, so the secret is just complaining out loud and doing it in front of other people, so you can just be embarrassed, and people don't.
**Trent Mick** 21:09 The request, yeah, the request to open an issue on the thing is sometimes two things. One is… forces you to double check, yeah.
The other one is, yeah.
**Marc Pichler (Dynatrace)** 21:20 Yeah.
Regardless. What is this one?
**Trent Mick** 21:23 It just is… Exporting some types that hadn't been exported before.
**Marylia Gutierrez** 21:29 Yeah, because I have the other PRs that are about, like, the meter provider and the tracer provider. I could add the changes from the config to that, but that one's, like, is on the SDK node package.
And I wanted to have, like, the different packages, like, per PR.
**Marc Pichler (Dynatrace)** 21:46 So, that looks… okay to me, but the one thing I was wondering about is this, rename here.
**Marylia Gutierrez** 21:59 That is because there was already a push metric exporter on the… other packages?
But at the same time, the config calls this name.
So, we are generating from, like, the schema. So, yeah.
**Marc Pichler (Dynatrace)** 22:18 Because I'm… I think aggregation also exists.
An instrument type also exists.
I'm wondering if we should just.
**Marylia Gutierrez** 22:32 Because I did call, and there was no… because I can send the link here. This is the other PR that is using all of those, and it's just, like.
well, on the PR, all tests are failing, because.
I need that.
**Marc Pichler (Dynatrace)** 22:52 Yeah, it's just failing to compile, probably, already, right?
**Marylia Gutierrez** 22:55 Yeah, yeah, yeah. It's just, if I… because, like, locally, I have the changes from both PRs and it works, so it's just about having those things so other packages can actually use. This is for the meter provider. I'm probably going to have a similar thing for the trace provider.
I still don't know everything that I need exported, so that's why this one is just focusing on the meter.
**Trent Mick** 23:17 This is naive, because I haven't been following the config stuff very closely, but, like, the whole bunch of types being exported here, are there ones that we want them to follow a pattern, so they're clearly about config and not about other SDK.
types, I don't… I don't really know. The only reason I'm bringing that up is because I had the same question that Mark had is, is aggregation something that's already… that term used for something else from a different package, and does that potentially cause confusion down the road? Just looking, SDK Metrics has an internal type called aggregation. It has exported types aggregation type and aggregation option. So, I mean, there's… there's always potential for confusion on these names and stuff, but I… I don't…
**Marylia Gutierrez** 23:59 Yeah, I can maybe…
**Trent Mick** 24:00 Noelle.
**Marylia Gutierrez** 24:01 I need to… now I need the other challenge of picking up a new name that I can add, like, maybe config to the end of all of this. Yeah, I have to think about it, but yeah, I can… then I can…
**Trent Mick** 24:11 But that… that gets hard, too. We just ran into it. It's… I noticed that… yeah, anyway. Yes, naming's hard.
**Marylia Gutierrez** 24:19 But yeah, I can try to do this today and update this PR with whatever is the new name.
**Trent Mick** 24:26 And I mean, this is… this is an experimental package, so we can always change that name later if we find out it's a problem, so it doesn't… this doesn't have to be a… Dop the world and rename everything just to get this one fixed, and so…
**Marylia Gutierrez** 24:40 Yeah, because I'm only, like, changing the name when it's… when I'm exporting, I'm not changing the name on the package itself.
Because that is the name of… use it on the schema, so that is… I really don't want to change, because we are actually having one of the things that are… from the scheme itself, generate and create the classes and interfaces here, so we would keep those names. But when I'm exporting, then yeah, I can add something here, and then…
**Trent Mick** 25:07 I mean, the generator could… again, this is a naive question, the generator could… Presumably have a common term used as a prefix or a suffix for all of the things being generated, right?
I don't know if that's gross, because naming's hard, but…
**Marylia Gutierrez** 25:22 Yeah, because I'm thinking, like, if you go back, you want to look, like, documentation, you want to compare with other, like, SDKs… might be, like, why it's not exactly the same. I don't know, it's just… and I'm not… I might not be exporting everything, so… I don't know, yeah.
**Marc Pichler (Dynatrace)** 25:44 Yeah, I, approved this for now. We can probably defer the naming question to a separate issue and discuss it there. But at least this way, it's unblocked for now.
Okay. So… Yeah. I guess we would definitely wanna figure that out sooner rather than later, though, because, Changing names of types can be difficult as soon as people start using stuff, and we've run into that quite a few times already, that it's difficult to change it later, so… Even if it is experimental, it's… Thank you, sometimes.
**Marylia Gutierrez** 26:25 Now, I'm gonna try even for, like, this open PR rename when I'm exporting, which name I'm gonna use, so this way.
Yeah.
**Marc Pichler (Dynatrace)** 26:34 Alright, thank you.
**Marylia Gutierrez** 26:35 Cool.
**Marc Pichler (Dynatrace)** 26:42 Alright… I guess we could also have some naming discussion here still, since there's not much more on the agenda today.
Anybody have anything else?
Wanna talk about?
remote. Then, I guess we can move on to bug triage.
haven't been very active for the past week or so, so I'm not… Fully up-to-date on what's going on.
Let's just see if there's anything new. I did look into, this one here, which I was assigned to.
I tried to reproduce what they're seeing here, and I think this is mostly related to Missing the, import in the middle.
Thing.
But they also say that they bundle their, their lambda here, so I'm not sure if I can suggest any good way for them to, like, keep the… Instrumentation package around. They would have to do the registration somehow.
But they can't do it in the… bundle that they produce, because then won't be able to hook itself.
So that's kind of, the problem that, they're running into here. I guess this would be solved by… OpenTelemetry instrumentation, doing the modular.
register thing, I think that was what it was called.
instead of.
**Trent Mick** 28:51 That doesn't help with bundling.
**Marc Pichler (Dynatrace)** 28:55 I think for the Lambda instrumentation, it should help, though, right? Because it just instruments the Lambda handler.
**Trent Mick** 29:02 Oh, so it'll help with the… having the… having the… Yeah, the module loader active, so it can pick up on ESM.
**Marc Pichler (Dynatrace)** 29:12 Me.
**Trent Mick** 29:13 Yeah.
I was going to look at… the README for this instrumentation, and whether I could use an update to point out that There's a lot of docs on it, though. I haven't really… Used to read this one.
**Marc Pichler (Dynatrace)** 29:31 And, README, I think it works well for… 22… There's that up at the top, yeah, that section. I wonder if that one could really point out that it also.
**Trent Mick** 29:50 Because that's saying that you need to change your handlers to only do wrong-space ones, but it does note that you need the… Importing the middle hook active, so… I think it would be fair to have an issue.
That we should update that README thing to make it a bit more obvious.
Assuming that's the issue that the user's running into. There's also the bundler question.
**Marc Pichler (Dynatrace)** 30:15 Yeah.
I think… What they are running into is really just missing the… Input in the, the input in the middle hook, and then, Probably the bundling thing would also be good to point out here.
I write that down after… The car today, to make sure that, We know what's next for this.
But I'm pretty sure that that would then serve the problem here.
**Trent Mick** 30:50 Oops.
**Marc Pichler (Dynatrace)** 30:54 Alright, and this one is, somewhat related, but not really.
Is that, gonna need to confirm… This was last week, so… you can still leave this open and wait for them to come back. If they don't come back within a month, we can close this one.
Right, that's it for… triage… And then we have, Core PR triage.
Since there's 50 PRs still.
select there, the… amount of PRs that are coming in is, equal to the amount of PRs that we close on March right now.
So, the first few here… Api… Logs still blocked on stabilization.
And… This one I haven't had time to look into yet.
This is Dan's entity prototype.
Which he… Opened the second one.
I'll just, put the comment here.
What's this one in favor of?
That, and then we can continue on.
Here, I was meaning to open an issue for that one, too.
propose API extensions packages, but didn't get around to it yet.
This here is, generating types from the config.
JSON schema thing.
**Trent Mick** 33:48 Has something happened there, Marilla, since… Jamie opened that issue, because Jamie was away for a while, she's back now, but… Slowly.
**Marylia Gutierrez** 33:57 So, yeah, so I think, actually, someone else… I don't know, let me check. Are you here? No. The person… there's someone else that he's been picking up.
the things that she was working on, so I think that is one of them. Mike, or someone, I think.
Yeah.
So he said that she was out, and he was gonna pick up her thing, so he is actually picking up this one next. So I don't know if he's gonna look from what already was here or not, so yeah, just leave it there in case he wants to reference.
**Trent Mick** 34:28 Great.
**Marc Pichler (Dynatrace)** 34:29 Alright, that sounds good.
Yeah, probably, but also… And solve the question about, like, what we're gonna name things if the tool just spits out.
The thing here, so… Yeah, interesting. But, yep.
One of the things that I ran into in the past with generated types is that they're often not as, easy to extend when you regenerate them. It sometimes is a breaking change.
in the types that you generate, but it's not a breaking change in the JSON schema.
So that might be something to be aware of, which can be tricky.
In case any of us, is doing the review and the follow-up PR for that, something to look out for.
**Marylia Gutierrez** 35:26 The good thing.
**Trent Mick** 35:26 Terry, what was the comment?
**Marylia Gutierrez** 35:27 It became stable, so hopefully we're not having also, like, a lot of changes, so yeah.
**Marc Pichler (Dynatrace)** 35:41 Sorry, Trent, you were saying something, didn't…
**Trent Mick** 35:44 Yeah, I missed the gist of what you were saying on the compatibility thing.
**Marc Pichler (Dynatrace)** 35:47 It's a scheme.
**Trent Mick** 35:48 changes, then we run into stability issues, or…
**Marc Pichler (Dynatrace)** 35:51 Yeah, exactly. I think it was QuickType that I used in the past. I'm not sure if that's true still, but, I think that one generated different types.
in different versions, but I think it was still experimental back then, so that's to be expected.
And I think there were some ways that you could modify a JSON schema that weren't breaking to the JSON schema itself, but were breaking to the types.
Which… can be, once you figure it out, it's usually too late, so I just wanted to call it out.
Who cried touch before.
Alright.
This one must I haven't gotten back to yet.
as well as 3 weeks ago, let's wait for one more week, and then, close it. I might just… open another PR tool.
To do the justice, yeah, to address this when… I close it.
Seems to be simple enough of a change.
This one here has one approver.
It's about to warn you on preloaded.
**Trent Mick** 37:28 Oh yeah, I'll give that one. I'll follow up afterwards. It needs to resolve a conflict in the changelog to move it, presumably to move the entry to the top, and then I'll merge that later.
**Marc Pichler (Dynatrace)** 37:38 Brilliant, thank you.
I guess why we're talking about changelogs, I've seen other repos in… .
**Trent Mick** 37:51 the OpenTelemetry org used this.
**Marc Pichler (Dynatrace)** 37:55 changelog tool.
I think it's from the Gold Build Tours thing. Is there any appetite for us to switch to that?
I could look into… Making the…
**Trent Mick** 38:09 Is this the one that has the dot?
Chluggen…
**Marc Pichler (Dynatrace)** 38:13 directory, so that they're separate entries, so that you never get this issue of out-of-date ones. Yeah.
**Trent Mick** 38:18 Exactly.
**Marc Pichler (Dynatrace)** 38:20 I also, like, tried making my own smart, Script that handles these changelogs, but if we could reuse whatever the other repos are using, it might be better.
To use that instead.
handling the change. Yeah, it might be the…
**Trent Mick** 38:39 Yeah.
**Marc Pichler (Dynatrace)** 38:42 Sorry.
**Trent Mick** 38:43 No, no, no, it's fine. If the… if… if… Yep. I mean, we have lots of changelogs, and they're different how we do it between the two repos, so if it's… if he can get it to work smoothly.
**Marc Pichler (Dynatrace)** 38:57 I can…
**Trent Mick** 38:58 consider that.
**Marc Pichler (Dynatrace)** 38:58 Yeah.
I can open a PR with my prototype script. It's actually fairly simple to manage change logs this way, because you just have a Yammer file, and you write yourself in there, and then you generate the changelog entries from that.
So… We can see if we wanna take that or use the… Solution that's already implemented there.
**Trent Mick** 39:26 So I vaguely remember seeing it, I think, in the SimConv repo or something, and there were… there's a whole lot of boilerplate in that YAML, I don't know if it's got a bunch of features that… aren't generally needed or not, but that's fine. If it solves this issue, that's kind of nice, because we have had the odd case where we merged something, even though the changelogs.
**Marc Pichler (Dynatrace)** 39:45 Mmm.
**Trent Mick** 39:46 now in the wrong… in an already released section or something, but… so yeah. Yeah, I think that'd be worth it.
**Marc Pichler (Dynatrace)** 39:52 Yeah.
It would… I saw… Probably help if we can have the type of change in the changelog file, then we can automatically determine on the release which version pumps are needed.
so when generating the PR, To release a new version, we won't have to choose.
Which pump we want.
Probably still want to override it if needed, but… For the most common case.
Probably be fine to just use the default.
**Trent Mick** 40:33 Oh, you mean the query repo, because in the config repo, that's.
being done in a police place, right? So, okay.
**Marc Pichler (Dynatrace)** 40:40 Yeah, in the country repo, it's already served. It's just unfortunate that in the core repo, we… Can't use release, please, because our specific case is not supported by it.
**Trent Mick** 40:52 Yeah.
Also, grumpy curmudgeon solved with air quotes. If you get it wrong, then all of a sudden you're stuck, and you can't do a release, you have to do a fake.
Here are merged to get it to go. But, yeah.
**Marc Pichler (Dynatrace)** 41:03 Yeah.
**Trent Mick** 41:06 Because you can't override that one, as far as I know, with release, please.
**Marc Pichler (Dynatrace)** 41:10 you, you actually can do it. You can overwrite.
Ugh.
I think there's this… Going on.
**Trent Mick** 41:22 Do you do it with the begin, commit, override comment? Is that…
**Marc Pichler (Dynatrace)** 41:25 Fair enough.
**Trent Mick** 41:25 for doing it. I thought that that wasn't… Enough to change the, like, the type of bump selection.
I did the same process going to look for one. You had one, and then you added it for release, and then you removed the begin commit override comment from the description, so it.
**Marc Pichler (Dynatrace)** 41:46 Isn't there.
**Trent Mick** 41:46 anymore if you go searching for it. You have to… you have to work hard to find it, but don't worry about it. I… I know what you mean. Maybe that's it. Okay.
**Marc Pichler (Dynatrace)** 41:54 Yeah.
So this, I think, should work, and you can also put multiple different… Things in there. So you just stack them, below.
Then, it would take all of these, but it will still use the same change set from… the PR. So, you can't do… if you change two packages, you can't say, this is for one package and this one is for the other, it will just apply to both.
Which can be annoying.
So, that's something, too.
Look out for, but… Yeah, this should… to it, I think… It might also use the PR title.
not the commit message, or determining which pump to make, so sometimes renaming the PR after the fact can also help.
But I haven't done it in a while, so I might be completely wrong about this.
Right.
Moving on to… These two, I haven't looked into these yet, Then we have this proposal here for the create instrumentationfactory function.
I guess we haven't talked about this in a while, to be one of… Nope.
**David Luna Bistuer** 43:42 That's fine, that's fine, that's fine.
I think it's… maybe it's a… it's a… Too big of a change, though.
To try to push it into this, Maybe it needs more work and maybe more conversation with the browser, so the idea is to, yeah, to have a different function, so… So then we split better the… and it's more… friendly for 3 shakers, but… It's, I guess it's not in the scope or the target for this new release of the SDK, so… It's fine, just, if you prefer, just for not annoying you, maybe I'll close it and… I'll revive it, after the SDK 3.0.
**Marc Pichler (Dynatrace)** 44:30 It's, it's not too… too annoying, I just, like, knowing what the status is is sometimes helpful, and if the process leak still has some input on that, I think it's okay for us to just wait and… and have it there.
I also was meaning to look at this at some point, but it just keeps… disappearing from the first page of PRs, so I'm sorry about that.
**David Luna Bistuer** 44:55 No worries, no worries.
**Marc Pichler (Dynatrace)** 45:02 Alright, Speaking of things that I was meaning to do, this PR is adding the always record sampler from the spec, which would be the last prototype, I think.
It links the spec issue here.
Which… was completed, and I think we talked about it.
Last week, that there was going to be an issue to stabilize this as well, because it already has… Two qualifying prototypes.
3, so there's… Enough of them to… Continue the stabilization process.
I'll assign this to myself to make sure.
It ends up in my… Good to hear.
And I'll have a look there.
is… is also related to, renovate changes and other things. There's this, CLO monitor.
The problem here seems to be that we do publish an artifact that, is… Picked up by this… CLO monitor thing.
Oh, and we get a bad score for… Doing bad things.
I guess.
That's probably this one, then.
Artifact… Artifact Hub Batch…
**Trent Mick** 47:18 What is CLO Monitor?
**Marc Pichler (Dynatrace)** 47:31 I think it just aggregates a bunch of, A bunch of scores together.
Because we have this, OpenSSF.
Scorecard thing?
Oops.
Where we get… Scores based on, what we do here.
and so it does things like, statically check the workflows, and then… there are… there's this warning about release artifacts. This is, because they're not signed, but we don't actually publish any code by it. It's the, bill of materials that we publish. There's a bunch of different other things that, give us a bad score, and there's, I think CLO Monitor just aggregates all of these together.
As opposed to this artifact, pup.
is… Probably also not happy about the… We love materials that we publish.
I'll look into this a bit more, But it seems that, just adding, file here.
or an extension feels a bit more like just hiding things, and I think, It doesn't support JavaScript packages, that's, And that's the reason why we're getting a bad score, and that looks more of a problem Or Artifact Hub, to me, rather than… Problem with our releases, but… I don't know, a bit difficult to figure out what's going on here, actually.
Or let's assign this to myself.
**Trent Mick** 50:10 computers.
My first reaction is like, meh, tail wagging the dog here, but CLO Monitor is a CNCF.
projects, so I don't know if… That means it carries any weight?
**Marc Pichler (Dynatrace)** 50:24 And I think, one thing that we should… Definitely look at this, any sort of… Security score.
For the others, I think these are less important, but, security scores, they do ask for some things that I think are… make… make a lot of sense, and so… I think at least for that, we should look into it.
**Trent Mick** 50:58 Okay.
**Marc Pichler (Dynatrace)** 50:58 And, I'm not sure if it, carries any implications for the… Graduation.
of… OpenTelemetry as a project, so… That might be worth looking into then.
If that's the case.
Alright, so, that's see a low monitor, then… there's, fetch Instrumentation, PR, With a bunch of comments on here.
**Trent Mick** 51:39 I think we can close this one, because we did 6341.
**Marc Pichler (Dynatrace)** 51:48 Huh, yeah.
**Trent Mick** 51:49 I think there are, like, 4 PRs that came around this that are similar, so no, I don't…
**Marc Pichler (Dynatrace)** 51:55 Hmm.
Yeah, this looks… Like, it's the same thing, so… .
**Trent Mick** 52:09 I can… I'll follow up, because I was working on Anna.
**Marc Pichler (Dynatrace)** 52:13 Thank you.
Alright, moving on to the next one is… Approving the… guidance on gRPC insecure connections, looks like the person we're… Ping me once they're done, so this is in progress.
Then there's this… Fetch later transport, I think the… Browser maintainers on this one.
But I guess, no progress on this. If there's no interest in this, then I will, just close it after a month.
**Trent Mick** 53:14 This was discussed at the last browser SIG.
**Marc Pichler (Dynatrace)** 53:18 Oh,
**Trent Mick** 53:19 And I think Jared was saying, like, mmm, no, maybe not, because for two reasons. One, it… I think it wasn't… Like, it would only activate when you browsed away from a page, so it added complications… Or reliability of sending stuff, so while it seems nice, maybe not. And also, it's not in… Widely supported, or whatever the…
**Marc Pichler (Dynatrace)** 53:44 in his…
**Trent Mick** 53:45 support levels are, it's only in Chromium browsers, so… Really, that's not something that… It meets the criteria that you'd expect to have in poor thing.
if… the… export system allowed people to plug in their own transport from a third-party library, then sure, sounds like, you know, people could do it that way, and we'd encourage them to publish their own That could be out of a configuration, but otherwise, probably not.
So, I think it would be nice… maybe we could… we could ping.
Overbalanced had his thoughts here, because I guess those didn't get through.
Or didn't get added.
**Marc Pichler (Dynatrace)** 54:23 Or…
**Trent Mick** 54:27 I can…
**Marc Pichler (Dynatrace)** 54:28 I'll take it. Oh, thank you.
Right. So that's it for Fetch later.
This is my… draft, I guess we can still, leave that open, then also follow up with a deserializer.
This is good to keep as a reference for now.
The actual PR is also linked.
Here, in case, anybody's interested, this is the…
**Trent Mick** 55:11 Yes.
**Marc Pichler (Dynatrace)** 55:12 Wing to them.
**Trent Mick** 55:12 dot, but… Priorities.
**Marc Pichler (Dynatrace)** 55:15 Yep.
It's… it's not, super urgent or anything, it's just, performance improvement thing, so… There's other things that we can prioritize for now.
Like, the logs SDK and stuff like that.
This one is also still… Still, I guess, I will, leave this open for a bit longer, and if they don't get back to us, I will close this one.
I think this one also had a few different PRs open for it, if I recall correctly.
And… the ECCLA thing is also not signed, so that's probably why it didn't get… Picked up by any reviewers.
Our soul… Put a note here… For me to get back to this one and, put a comment on here, what the next steps would be.
**Trent Mick** 57:13 Wow, that's a pretty heavy is request check.
**Marc Pichler (Dynatrace)** 57:20 Last one, you mean?
**Trent Mick** 57:22 Yeah, the instance of request. Sorry, I was looking at the code for that, Hmm.
**Marc Pichler (Dynatrace)** 57:31 Oh, no, that's on the wrong PR again.
This was the one that I was… Trying to open here.
**Trent Mick** 57:40 One of the utils.js. Yeah, well, it's right there.
**Marc Pichler (Dynatrace)** 57:43 Yeah, it's, the… is request, thing is, doing a lot of stuff.
I feel like this part of the quote has been causing us problems.
Since forever.
**Trent Mick** 58:04 Is this, like… I don't do the front end as much, but is this, like, a browser world? So, my website has 37 scripts from different people that are doing 17 overrides of the fetch and request, and every other global officer, so instant sub-checks are, like, a nightmare. I don't know. Boy, it feels like a… Pretty dangerous world to be trying to instrument, but… Anyway.
**Marc Pichler (Dynatrace)** 58:30 I see.
**Trent Mick** 58:31 Again, asking the browser sig it, that's all everyone's, like, just all these battle-hardened guys with scars.
All over their body.
**Marc Pichler (Dynatrace)** 58:40 This, sounds very much like the browser work to me, but… Duh.
**Trent Mick** 58:46 There you go.
E2 is… That's one of those people.
Do you have scars, TJ?
**t2t2** 58:57 Yes.
**Trent Mick** 59:00 I was… okay, I can't…
**Marc Pichler (Dynatrace)** 59:02 See you.
**Trent Mick** 59:02 I can't claim it now, but I was gonna say that the other reaction you get from these people is you suggest doing something, and just you get the adult… old folks just give a sigh. Like, yes, that sounds like a nice thing to do, but… you're gonna run into all these problems, but yeah. Anyway, okay.
And I've run us out of time, so we're not doing any more peers.
**Marc Pichler (Dynatrace)** 59:25 Alright then, thanks everybody for joining. See you next week. Have a nice week.
**Andrei Borza (Sentry)** 59:31 Thank you.
**Trent Mick** 59:31 Thanks for joining.
**Andrei Borza (Sentry)** 59:32 Right.
**Trent Mick** 59:33 Bye.
