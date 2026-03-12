SIG: JavaScript SIG
Date: 2025-08-20
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/cULQZDduO-OMCCLtiqd7AFzmqihn0nys926TObKHO5BOjrRkOOm5soSPtInXiQiw.nZljYcxnXUEMFs6_
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:53 You know?
**Trent Mick** 00:56 Nope.
You don't like the power of running this meeting every time, Mark?
**Marc Pichler (Dynatrace)** 01:04 every time it's a bit too much, I think. It's kind of difficult to, … To focus on what's being said when you're… Kind of on the spot running the meetings, so….
**Trent Mick** 01:16 I can't at all, my brain.
Completely shuts down when I'm talking.
I'm running a thing, I am… I have zero intelligence to provide that yet.
**Marc Pichler (Dynatrace)** 01:28 I always have zero intelligence, so… For me, it's fine.
I can't share the screen here.
Speaking….
**Trent Mick** 01:57 Yes.
**Marc Pichler (Dynatrace)** 02:09 Expect for… One more minute, and then we can get started.
Alright, yes.
You can, stick well.
So the first topic on the agenda today is, one of my own topics, basically just asking if Yeah, we should do PR triage from now on, based on which repo has the more, open PRs, has gone trip.
we've, kind of cleared out a bunch of the old PRs now, and, there's actually fewer now than in Core, so I think Core could also use some attention there.
I see, Marilla, you have already put your thumbs up there, so I guess you're… On board with it.
**MG Marylia Gutierrez** 03:27 Yeah. ….
**Trent Mick** 03:30 Yep, sounds good.
**Marc Pichler (Dynatrace)** 03:31 excuse me.
**Raphaël Thériault** 03:31 Yeah, thumbs up.
**Marc Pichler (Dynatrace)** 03:32 smarter.
**Raphaël Thériault** 03:32 Me too.
**Marc Pichler (Dynatrace)** 03:34 Okay, sounds good. Small meeting today, so… Easy to get maturity, I guess.
… Alright, then, let's do it this way today, and then, we see how it goes. The next one is Marilla, about the… BioConfig PR.
**MG Marylia Gutierrez** 03:56 So yeah, I've been able to break down the other PRs quite small. This one looks scary because it's, like.
a lot of things, but it's very straightforward. It's just because there are a lot of, like, parameters that we need to add to the object, but they made it available now, like, emigration, like, if you use environment variable and want to start using declarative, those are the first things that you should do, so I want to focus on those ones first.
So I added all of those there, so it just… it just looks really big, but it's just adding the environment variable, and I have a test for every single one of them to make sure that they are setting up properly.
**Marc Pichler (Dynatrace)** 04:36 Awesome.
… One question about this, thing, is it, supposed to be… Like, feature complete already for, the environment variables, or is there still some stuff that might be missing here?
**MG Marylia Gutierrez** 04:54 So, I need to check, because from the… That is, like, a weird one, because I check all the list of existing environment variables, and there are a few that are not part of this migration.
But some of them just don't exist on the declarative config at all. So I'm gonna bring up on the next call with them, just to see, like, can I just add those as extra, like, specific for JavaScript? Or what is the plan? Is something, like.
like, the trace exporter, we… we can have, like, the value OTLP. There is just assume it's OTLP. Or there is some specific for, like, Prometheus and Zipkin… None of them are anywhere there, so those are the ones that I haven't added there, because I need to find out exactly what to do. But the majority should be there. And I was even considering if I should mark this one not as private anymore after this.
Because if anyone wanna start replacing any… environment variable, like, reads, they can start using this one as well.
**Marc Pichler (Dynatrace)** 06:04 Yeah, one of the, … things here that I was, wondering about is… … Like, right now, if we were to start using that to… package size will probably become a lot larger. So if we were to, like, take this and then just use the chunk for, the OTLP exporters and, like, take a dependency on that, then we, will probably pull in, like, quite a large package, right?
For just configuring that subpart, which I'm kind of worried about.
… Yeah.
But… There's also smaller things that I have noticed, which is that, There seems to be just the, … the, the signaler-specific, environment variables here. … But there's also a non-Signer-specific one, which is, OTR export or OTRP compression without the traces in between that it falls back to. I'm wondering if that is, … If we can use that as it is right now, without having the far back, because it's kind of a… … Widely used thing at the moment.
So yeah.
**MG Marylia Gutierrez** 07:42 What do you mean, like, fall back from that one to what?
**Marc Pichler (Dynatrace)** 07:45 So if this, … where was it? Oter… exporter OTRP traces compression, environment variable is not set, then it would fall back to auto-export or OTRP compression.
And then after this, it would actually fall back to the default.
And there's different things where, like, some odd merging goes on. So, if you go to the code of the exporters, you will see a bunch of configuration code that, like, tries to handle that somehow.
**MG Marylia Gutierrez** 08:22 Yeah, so for this one, I use basically the… So for the object, we have a few cases that say, like, the default should be this one.
And I also checked the environment variables that would also have defaults.
So, this is why, for example, the config model itself is the one that creates the default with all the values. This is why it's, like, the backup of everything. And then the, like, environment is, like, if you have the value, then you replace whatever is the default for this one.
But I didn't see anything about order, like, for example, this one falling back to another one, then another one. I didn't see anything related to this, but if I'm missing… Yeah.
**Marc Pichler (Dynatrace)** 09:07 It could be that it's, … Let's see… very quick, there's this, … Some of the environment variable config specs are kind of all over the place, so they are sometimes a bit difficult to find.
So, there's this, OpenTelemetry exporter, OpenTelemetry protocol exporter specification.
….
**MG Marylia Gutierrez** 09:44 And there it lists all of these, ….
**Marc Pichler (Dynatrace)** 09:49 Environment variables, for example.
… And Yeah, I'm not sure where the fallback thing is now specified, but pretty much every SDK does it somehow, so… I'm not sure.
**Trent Mick** 10:15 So the… this… Not up to speed on the config work, so this might… … being naive comment, but the top of the… so the… PR that you have is linking to an example migration config.
And that thing has a comment at the top saying that it's not currently handling the… the… Environment variables that don't have the signals in them, so….
**MG Marylia Gutierrez** 10:44 Yeah. Like, I don't know if this is an indication that this isn't….
**Trent Mick** 10:47 Doesn't necessarily cover the right Way to gather all these things, it's… I don't know, it's meant as an example for people to… Migrate from using environment variables to whatever, so… or to using a declarative config.
**MG Marylia Gutierrez** 11:04 Yeah, so that's why I was saying, like, this one, all the ones that I created are not the ones on top of that file, so there are still… I need to figure out how to handle those cases.
**Trent Mick** 11:16 Yeah.
**Marc Pichler (Dynatrace)** 11:28 Oh, Yeah, I guess we probably have some more discussion on this PR during review, as there's quite a lot of stuff to go through anyway.
**MG Marylia Gutierrez** 11:41 … Yeah, so if you look, like, look at the PR description that has a link for the migration.
Yeah.
So this PR only handles, like, see, like, the ones on top is not handling all of those.
And then… It's not, like, doing, like, different, and then the rest is, like, example of how you should do the migration.
So, all the things that is on the bottom is the one that I added to that file.
So if you look for the compression, it's gonna be some… there somewhere.
Yeah, so I set it up like those values on the one that had… A migration path.
**Marc Pichler (Dynatrace)** 12:42 Oh, that's, really interesting.
Alright, yeah, I will have a read through this one. I'm, kind of not fully up to speed on how to handle these things, but, yeah.
It's interesting.
Alright.
**MG Marylia Gutierrez** 13:00 And the good thing is that I also showed them how… because I noticed some of the other SDKs were doing slightly different from my approach, so I brought it up.
And they actually liked the way that I was doing, so like, oh, I wish you were doing this on the other SDKs. I was like, yes. Yeah. I got good feedback on the way….
**Marc Pichler (Dynatrace)** 13:22 That's good.
Alright, … Yeah.
I guess I will, … I should have a look at this one, because I was kind of… digging into the… all the old config stuff, in the Xbox already, so it's… permanently burned into my mind. It's like… ….
**MG Marylia Gutierrez** 13:47 And kind of related to this, I don't know, because we kind of, like, said that, oh, every component should have, like, two code owners. Currently, I am the only one for this.
I don't know if anyone else wants to… I'll also be a co-owner, but just….
**Marc Pichler (Dynatrace)** 14:02 We don't really have the concept of code owners in the core repo.
**MG Marylia Gutierrez** 14:06 Okay.
**Marc Pichler (Dynatrace)** 14:07 It's, just owned by everybody, usually, and that, has worked fine for the core repo, because, It usually just contains stuff that is, applicable to pretty much everybody, so, … Yeah.
It's a bit easier to, … Yeah, deal with components that are, supposed to be used by everyone. It doesn't just affect a subset of users.
So I think that, could be fine. Yeah.
As for the, marking it, marking the package from private to public, I would wait for that until, like, we change one of the core packages to use the configuration package.
So once we actually start using it in one of the core packages, we can, have a look at, actually publishing it, because that's when it will Be necessary to publish it.
I guess….
**MG Marylia Gutierrez** 15:20 Yeah, because my next step was… I just picked the SDK node to be my proof of concept, so I was planning on replacing, like, all the calls for environment variables to this thing instead.
**Marc Pichler (Dynatrace)** 15:35 Heck.
Yeah, I think, for SDK nodes specifically, it, Would be good, then, if… that CR is opened, and we actually start using it, then we can market as public, and then we can also publish it with the first version that actually uses it.
In SDK node.
Right?
Does anybody have any… Questions… comments, or just PR here.
If not, then I will definitely have a look at this one, and we can move on to the next topic, which happens to be mine again.
So, yeah, if anybody is interested.
in, moderating the Sikh meeting, and you're an approver, And you're interested in doing so, please feel free to reach out.
Yeah, it's, good to have, like, deeper rotate, that… that are moderating the SIG meeting to, … yeah, kind of share the load a little bit, and, it's always a bit difficult in, to participate while, moderating the SIG meeting, so, having, More people, always helps, kind of share the load there a little bit.
**Trent Mick** 17:15 I can try it sometime.
**Marc Pichler (Dynatrace)** 17:18 Thanks, that sounds awesome. Yeah.
But… we can, we can just see, how it goes, and… Yeah, just looked into it.
Right.
If there are no more comments, then we can move on to bug triage. As always, if you have any topics that you would like to bring up, please put them on the agenda, and then I will go back to, looking at that.
Alright.
Looks like there's no… new home.
new activity there, … Looks like they're awaiting the… -oh.
Attributes, no.
On the top level, which… sorts out the problem, which is kind of expected anyway, because there was this, Oh, what was it called?
Temporal, ….
**Trent Mick** 18:44 temporal platform, yeah.
**Marc Pichler (Dynatrace)** 18:46 Hmm, thing. So… Yeah.
Looks like they have a workaround. I think I signed this to myself last week, but I haven't gotten around to doing what I wanted to yet, which is adding the… Actual stack trace to the, diagnostics log that we write, so that we can see where this is coming from, usually.
And then… Help people in troubleshooting? What's wrong.
would also help.
us, I guess, to figure out, if it's a problem in the SDK or, somewhere else.
But I guess this one is… is not really an… SDK problem at the moment, so I will put this at P4.
I'll remove the triage labor, and I will, … Also, remove needs of the response… I'll go from there, adding this… In… What is it called? Adding this log stack trace thing, and then, … I'll be able to see if… New issues will, also report, … problem with our SDK, or if the issues go someplace. … Alright.
Going on to contrive, we have the, MongoDP TP client connections using usage metric, not decreasing idle value.
On connection closed events.
Dang.
Seems to… There's just some, issue in keeping… keeping metrics aligned with what is happening, so I will put the E2 on here, because it looks like that the… Metrics are incorrect, and that is for… Instrumentation, MongoDP, it seems… I wasn't even aware that we already had, … metrics here in MongoDP.
Let's see where that link goes… Answer.
Let's put this label on here, and then, see who is… A code owner for that.
Right. … That's it for contract now.
So, I guess we go on to… would core PR triage, … This one here, there will be… pull requests.
That will… supersede this one, so I will, put a comment here. … That… that's the new one, and I will close this one, actually. … Alright, so… that one is closed. Then… This one here is… actually approved.
Seems to be some conflicts here.
… So these need to be reserved, but… Needs some attention, later on.
Then we have… the delegating node meter provider. I think I had a comment here a while ago that stated that, we not only need to proxy the, The actual meter, but we also need to proxy the instruments, because, … Otherwise, people… like, whenever people create a meter, it's also normal to also immediately create the instruments themselves.
So, it wouldn't actually completely alleviate the issue.
I'm not sure if that has changed now already.
Looks like this still does.
We're accumulating some… Boxing mechanism for delegating instruments.
So I guess this is, still a work in progress. There was some updates to… Thing, but it seems that there's… those were just minor things here.
… So, I guess this one's still in progress, and this one here is… … Also, not actionable right now, I think. … there's… This one, at least, that is a blocker for doing that.
… So… I'll put the comment here.
Worked on this, and some other issues from this milestone here.
We can go ahead and merge the logs API into, … Open Telemetry API package.
Alright, some update provided here. … Then, there's this… it… Section handling implementation… Seems to have had some… activity recently… Alright, looks like this is still in progress, and … folks form, I guess they are attached to the process, SIG, are looking into this PR.
….
**Trent Mick** 29:01 Yeah, I think so. I wouldn't be diving into the browser ones right now. They seem to be.
**Marc Pichler (Dynatrace)** 29:06 Okay.
**Trent Mick** 29:08 Going on in their cycle.
**Marc Pichler (Dynatrace)** 29:11 Alright, yeah, I will see that I can join tomorrow again, … It's been out of office for, quite a few Thursdays recently, so… Not too up to speed on what was happening there.
some… I guess we also have, like, a target browser.
That was actually in the, contract repo, so I'll leave that, as it is for now.
… Right.
This one here… I seem to remember that this was actually targeting the next branch, but that one doesn't exist anymore now. ….
**Trent Mick** 30:10 Oh yeah, this is one that Jamie and I were back and forth on.
Not back and forth, sorry, but there was… Some complication on this.
No, I think it's… I think it's something that we want, but it needs an update, right?
**Marc Pichler (Dynatrace)** 30:24 Yeah, it's a breaking change, I think. … If I recall correctly, it's still… it's changing this ad span length, attributes. It was supposed to be a cleanup from another PR that added a kind of a weird flag, … So, what we would need to do here is actually create a follow-up issue, and… Then, basically, … Move that issue into… or label that issue in a way to indicate that this can only be done on the next, … next major version that we release.
Or the PR needs to be changed to be, … Hang on breaching.
It seems to be non-breaking right now.
This is add span length attributes.
That's banded works events… Or one of the difficult things with this one is also that we have these utility functions in the SDK Trace web package when they should actually just be duplicated across, the… Boom.
XHR and fetch instrumentations.
**Trent Mick** 32:23 Yeah, I think we agreed to do that. I think the original argument for having a single one was to be… A smaller bundle, but… Seems… To be premature optimization, probably.
**Marc Pichler (Dynatrace)** 32:39 … Let's do this. I will put, … I don't want my to-do list to create a follow-up issue for this, and then I will close out this PR, so that… It's clear that this one's likely not getting merged, right now, and then, remark the follow-up issue as, for grabs.
where we move the code, basically, from the SDK Trace web package to the instrumentations, and then deprecate the one from the SDK Trace web package.
**Trent Mick** 33:24 Okay.
**Marc Pichler (Dynatrace)** 33:33 Right, I moved it down, and then… Let's move on to the… Next one.
my own PR.
Probably… Perfect. Have to go get in and repaste this one. … This is actually one of the… last PRs to be able to mark OTRP transformer as stable. So, yeah.
The conflicts that are in there are probably… Only related to the, package.
Locked.
Or changelog or something.
If anybody has time, I would appreciate a review on that one.
**Trent Mick** 34:29 If you have a chance to deal with the resolve conflicts, then….
Can you shout in one of the channels, and I can probably take a look.
**Marc Pichler (Dynatrace)** 34:37 Yeah, will do. Thanks.
**MG Marylia Gutierrez** 34:39 Oh, and I just add another topic that I forgot that I was gonna ask.
**Marc Pichler (Dynatrace)** 34:43 Oh.
**MG Marylia Gutierrez** 34:43 So, about adding a package, because there's, like, several packages that just parse YAML, and I was looking to, like, the most popular, but I don't know what type of license that we can add package. So, one seems to be, like, more recently published and maintained.
And it's one type of license, and the other is MIT, what I think is more popular, but last published, like, 4 years ago. So I don't know what are, like, requirements to… pick a package.
**Trent Mick** 35:14 Yeah, we've been down this road a couple of times recently, I have to go find the links again. ….
Where are I?
**Marc Pichler (Dynatrace)** 35:22 I think what we, ended up at was that IC license is compatible with MIT, and therefore acceptable to, use that one.
**Trent Mick** 35:35 There was a specific list somewhere, though.
**Marc Pichler (Dynatrace)** 35:38 Yeah, it was somewhere at the CNCF, … Licensing guidelines, or something like that.
**Trent Mick** 35:47 There we go.
Nope.
**Marc Pichler (Dynatrace)** 35:52 I would, very much prefer to have the… the package that, … Yeah, like, last 12, yeah, last 15 days ago, then the others, like….
**MG Marylia Gutierrez** 36:02 Four years ago, I was like, oh….
**Marc Pichler (Dynatrace)** 36:05 Yeah, I think the oldest that we had was, like, 10 years ago. I'd like to not go down that path, if at all possible.
Okay.
**MG Marylia Gutierrez** 36:15 Pink Strip.
**Trent Mick** 36:18 So I see Skid.
**MG Marylia Gutierrez** 36:20 Is there, okay.
**Marc Pichler (Dynatrace)** 36:22 Awesome.
**MG Marylia Gutierrez** 36:22 Okay.
Thank you.
**Marc Pichler (Dynatrace)** 36:27 Wait.
**Trent Mick** 36:28 I have scars with YAML.
Oh, so….
**MG Marylia Gutierrez** 36:32 I don't know.
**Trent Mick** 36:32 Let's be… let's be careful what we… Merch. I don't know. Maybe it's not gonna be as bad as the Ruby YAML library would execute code in YAML files at one point. I assume.
Modern world is past that kind of stupidity, but….
**Marc Pichler (Dynatrace)** 36:54 world, … Sir, put this… I don't know, it's not the right… I lost the… I lost a link here.
**MG Marylia Gutierrez** 37:11 Coffee here, yeah.
Oh, I just put it up.
**Marc Pichler (Dynatrace)** 37:16 Right.
**Trent Mick** 37:19 Sorry, your library has no dependencies, that's awesome.
**Marc Pichler (Dynatrace)** 37:23 Yeah.
No dependencies is what we like.
It's not the typical, NPM package that,
**MG Marylia Gutierrez** 37:35 In stores half the word work.
Yeah, I like that… that stat that is, like, oh, like, 20% of all network is used by streaming, like, services. The other 80% is just by NPM install.
**Marc Pichler (Dynatrace)** 37:52 Oops.
every time I look at the download numbers on NPM for the OpenTelemetry packages, I remind myself that I NPM install, like, 50 times a day, and that's probably all me.
… All right, guess the questions are answered then, yeah, and then we also have as a reference here the link, if anybody else is interested in Having a look at what's… Proofed there.
… Alright.
Oh, where did we stop?
Hmm… refactor in the API to fix some ESLint warnings, … Looks like this went stale… I remember looking at this… Quite a few times already, and it's, not really doing all that much.
So, I would actually… … Proof this one.
I've also looked into that in detail already, the, … Like, that should also be fine, and then we don't need this, unshift thing.
And there was recently also some change to the API, in a similar manner. It doesn't do exactly all of these things anymore. A few of these have already been fixed, like the one in the component logger, this was another PR. So, the diff is now a bit smaller than it was before.
So we can merge this in.
Right. … And we have… Another one, which is… Clarify text map propagator API requirements, … Yeah, I seem to remember that there was some, difficulty with how the type looks like right now on the text map propagator that makes it kind of annoying to work with.
… also has a comment here for a possible API 2.0 change, which is unlikely to happen at this point.
**Trent Mick** 40:52 Sweet.
**Marc Pichler (Dynatrace)** 40:55 … Yeah, that requires a lot more time to review this one. I'm not sure if we will get anywhere on this today.
… Looks like Hector reopened this.
… But this is definitely not just docs that are so… Make some, … Alright, factorings here.
… Okay.
Nothing that we can fix on this, … Or today.
Fixing ESLint warnings.
… A lot of changes here.
And it is in the async Hooks Context Manager, which, is used pretty much everywhere, so we want to make sure that we get this right.
… Looks like Dan assigned himself here.
… labor is not on it yet. I guess it's also not something that we can… Immediately.
Have a look at… this one, though, has… Failing change lock, … thing, and… Some conflicts here and there.
There's also quite a few changes.
… I think that's enough changes to… justify having a changelog entry, so I will always leave that as it is right now.
This one has changes requested, but I guess there has been no activity.
Mute.
I didn't publish my review here.
So… I guess I'll post it, … I remember doing this reveal. It was… so the test is actually incorrect, which, … makes it.
kind of difficult to, figure out what's going on, which is probably why this PR has starred, … Okay.
But… Posting the review Hypes Hub footage. … This has two approvers already.
Six comments and conflicts, … Won't be doing that now. But… There's these two things, … I guess we could just apply them if needed.
Boom.
**Trent Mick** 45:13 I can take a look at that one again later.
**Marc Pichler (Dynatrace)** 45:17 Okay, thank you. … Yeah, guess there's not a lot missing for this one to get merged.
**Trent Mick** 45:26 F.
**Marc Pichler (Dynatrace)** 45:28 And we have a similar one here.
… Wants a few more comments.
Yeah, it looks like they didn't have time to get back to this one, but the sale… sale labor has been removed.
**Trent Mick** 45:51 That also seemed to be….
**Marc Pichler (Dynatrace)** 45:55 Some conflicts on that one.
….
**Trent Mick** 45:58 instance.
**Marc Pichler (Dynatrace)** 46:05 Alright, this one is actually my own PR. … This is updating the, OTOP export example quite a bit.
I didn't have time to… work on this, though, so I will, … close this PR for now, and if anybody, wants to pick that up again, please feel free to do so.
There are quite a few… comments here, … That's… make a few, basically request a few larger changes here. … Actually, I will keep this one around, everything.
do another pass on, because I think there's not much missing at the moment, and if we merge that in, then it will improve the… … The quality of the example a bit, and then we can iterate later on making the requested changes here.
… I'll put that also on my list, and … We'll ask.
Jamie if she is okay with, deferring these, Changes to later.
I actually started.
Trying to combine the Traces and metrics apps.
To make the example a bit simpler, but, … Turns out that it's a bit more difficult to read that way, so… A comment here for myself to follow up on that one.
Alright.
There's this work-in-progress entities prototype, … Which is in draft.
**Trent Mick** 48:16 So….
**Marc Pichler (Dynatrace)** 48:27 I guess… Dan's still working on that one.
worked last on… 11th of July… Better leave that open still.
… Let's skip the renovate block PR.
And this one's also draft.
as conflicts.
… Let me close this PR.
This one here, I think I reviewed earlier… So yeah, that's actually applying my last suggestions, so we should be all good on this.
On here… Yep.
So that's approved by… Me. And we can just merge that in, and… Another PR of the list.
and renovate Bot PR again, ….
**Trent Mick** 50:54 It's… wait a second, is that one a braking change?
**Marc Pichler (Dynatrace)** 50:58 the custom HTTP agents one.
**Trent Mick** 51:01 Yeah, it's okay.
**Marc Pichler (Dynatrace)** 51:02 Yeah.
**Trent Mick** 51:03 Sorry, I just noticed the changelog entry doesn't have the bang in it, but I don't think that matters.
That's what the PR title does, yeah. Okay, never mind.
**Marc Pichler (Dynatrace)** 51:13 Yeah, I think the, … where is it here?
The changelog is in breaking changes anyway.
**Trent Mick** 51:20 in the race section, yeah. Yeah. But, what I usually do to clean this up is on,
**Marc Pichler (Dynatrace)** 51:27 the release PR, since that is opened by… by the OpenTelemetry bot, I can just put my suggestions in there, and apply those in the UI, and then,
**Trent Mick** 51:39 Great.
**Marc Pichler (Dynatrace)** 51:40 Yeah, I can just clean those up. So it's usually not that big of a deal, as long as they're in the correct, … In the correct category, is usually all fine.
… Right.
then… Renovate schema URL.
Yara. ….
**Trent Mick** 52:03 It got bumped out of the merge queue, by the way.
**Marc Pichler (Dynatrace)** 52:06 Oh.
**Trent Mick** 52:07 A minute after you put it in.
I don't know why.
**Marc Pichler (Dynatrace)** 52:16 Did I put this into the merge key already? I think it was just….
**Trent Mick** 52:22 So did you put it in a merge queue a minute ago?
Wait, not this one, the previous one. The support customized HP Agents.
5719.
Is there a EZCLA still broken?
**Marc Pichler (Dynatrace)** 52:40 Was it broken? I didn't, notice, actually.
**Trent Mick** 52:49 Out of the UCLA check, just totally borked.
Secretary.
**Marc Pichler (Dynatrace)** 53:00 again. There was recently some change to the ECCLA to also, check for… Co-author… … authorization, but I think I'm the only… Person here that reviewed… with changes… That were accepted.
**Trent Mick** 53:31 Thank you.
**Marc Pichler (Dynatrace)** 53:41 That doesn't get merged in our, follow-up.
Tomorrow, … To see what's up there.
Boom.
That's in the queue for now.
… yes, here, just need to approve the… Workflows again.
And then this PR should also be good to merge.
So I'll also put it into the merge queue here.
… Right, this one, … So, renovate… And the next one… Slightly a larger change, looks like Jackson has done a few reviews on this one.
Oh, it seems there's some confusion as to where to put the validation, but it is, … Best to put that in the, … into the SDK package.
once that has moved, I guess we can give it another, look and, see to get this one merged. That is also one of the, … Last few items for the, … blocks, API and SDK stability, … Promotion, so….
**MG Marylia Gutierrez** 56:39 And that PR got out of the merge queue again.
**Marc Pichler (Dynatrace)** 56:42 Okay. Is… is it still the, ….
**MG Marylia Gutierrez** 56:45 Celia, yeah.
**Marc Pichler (Dynatrace)** 56:51 Let's see if there's some… some output here.
Okay, I guess I won't log in right now on the car, but….
**MG Marylia Gutierrez** 57:18 password.
**Marc Pichler (Dynatrace)** 57:19 to them next time.
Boom.
Right, this one has a triage accepted labor on it.
The interest requested by me… Add us two extra examples here.
that I found to be a bit excessive for, … The feature which basically just… Changes this to this.
… Facebook.
Alright, … Let's see, … Sweet.
get an update to this one, otherwise I'll probably just go in and commit the changes myself and merge this in.
… This one is approved, probably, by me. … So let's see if RenovateBot can… get through the merge queue. … And then there's a whole bunch of other PRs that we'll probably not be able to cover today, because we're out of time.
Alright.
**Trent Mick** 59:36 Boom.
**Marc Pichler (Dynatrace)** 59:40 Thank you, everybody.
Have a nice week, and see you next week.
**MG Marylia Gutierrez** 59:46 Thank you.
**Trent Mick** 59:46 Sure. Thank you.
**MG Marylia Gutierrez** 59:47 Bye.
**Marc Pichler (Dynatrace)** 59:48 Again. Bye.
