SIG: Python SIG
Date: 2026-07-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Aaron Abbott** 02:35 Lil, how's it going, everyone?
**Tammy Baylis** 02:40 Hey, Erin!
Figured I would share screen since I'll start with the triage, and then I can pass it over to you later.
**Aaron Abbott** 02:50 Oh yeah, sure. That's great, thank you.
**Tammy Baylis** 03:31 And today's meeting notes in the chat as usual.
See, just a few familiar faces today. We'll wait a couple more minutes, and then I'll run through the triage real quick.
**Aaron Abbott** 04:31 Yeah, we'll probably have a lighter agenda today, because I think both late… yeah, both Leighton and, Ricardo or not around, so feel free to add any topics if you folks have them.
I added one, just figured we could chat about it, but yeah, I guess we could go ahead with the triage now, Tammy? What do you think?
**Tammy Baylis** 04:50 Yeah, thanks, Erin, sounds good. I'll stop around 9-10.
I believe I have the same sorting as last time.
Or do I, ugh, let me just double check.
Sort by… no, hit reset, so… Not priority, I'm so sorry, y'all.
Date, oops, updated.
Okay, I think that's correct.
There we go. Okay, first one. Reconfigure, renovate by Emidio.
And I… Think… I think this was discussed on Slack?
For a second… So there's no linked issue.
**Emídio Neto** 05:44 Yeah, this is, yeah, hey, this is a configuration Tony I'm doing.
to the renovator we just merged yesterday. I noticed that there are some issues with the pip compile manager.
**Tammy Baylis** 05:58 Mmm.
**Emídio Neto** 06:00 Yeah.
**Tammy Baylis** 06:00 Okay, so we definitely need this then.
Is this already Emidio?
**Emídio Neto** 06:07 Yeah, There's already a review from, Yeah.
**Aaron Abbott** 06:18 Yeah, I'll probably just stamp this one, and we can iterate quickly, because I feel like… How those things… these kind of things usually go.
**Tammy Baylis** 06:26 Thanks, Erin.
**Emídio Neto** 06:28 Yeah.
**Tammy Baylis** 06:31 Next, oh, another… Thompson Tomo again, related.
**Emídio Neto** 06:36 Yeah, this is the same thing, We both opened in the same PR with the… But, the one I'm working, it contains more…
**Tammy Baylis** 06:48 Hmm.
**Emídio Neto** 06:49 rules for Python monorepo.
**Tammy Baylis** 06:53 Okay.
**Aaron Abbott** 06:57 Should we just close this one out, then?
**Emídio Neto** 07:00 Yeah, we can close it.
**Tammy Baylis** 07:08 Nice.
Okay… Fix a SyncIO two-thread instrumentation.
Actual function execution.
Hmm.
Also from 2 hours ago, new issue.
Current main, so on dev, not released, I guess?
Yeah, steps to reproduce.
Yeah, that's ready.
Thank you for contributing.
Propose issue management requirements for PRs.
There you go.
28 days ago.
**Diego Hurtado** 08:20 Oh, that one.
Yeah.
**Tammy Baylis** 08:25 Yeah, I think… I think my main… yeah, I didn't comment during the meeting yesterday, but I followed up with some comments, oh, 2 weeks ago, actually, and I think this is great. It'll also mean we'll have to change our triage process a bit, which we'll need to continue to think about and probably iterate on.
And I guess this is… Definitely at least first steps to put this in place, is that correct?
**Diego Hurtado** 08:58 Right, sorry, I… I missed, And is that last comment from you, and should, reply there.
Yeah, I'll, so… I don't know… How… What is the consensus on this, topic?
So far, I haven't heard any… Like, strong blocking objection?
But, I would also like to know if, If people are really on board on this.
**Emídio Neto** 09:39 Yeah, I totally agree.
like, this week we received almost 15 PRs.
**Diego Hurtado** 09:47 So, you agree with this?
**Emídio Neto** 09:49 Yeah, I agree.
**Diego Hurtado** 09:50 I agree with the statement that people are not eligible.
**Emídio Neto** 09:52 I agree that we need some way to tell people.
They need to talk with the community first, before they start doing things.
**Diego Hurtado** 10:06 Good, good, excellent, yeah.
So I can take a look at, at Yurishi, Tammy, and, And, reply there, make sure that everything's in place.
And, and yeah, maybe… we can… Introduced this, this, process.
If, unless there is… Some strong objection.
I think, well, it's unfortunate that Leidon and Ricardo are not here.
**Tammy Baylis** 10:45 I couldn't…
**Diego Hurtado** 10:46 This topic next week.
So that we can get the opinion of more maintainers.
On this topic.
**Tammy Baylis** 10:53 I think that's a great idea.
**Aaron Abbott** 10:57 Yeah, let's do that. And then, just for the PR, like, just to get it out of the… that triage column, Do we know what to… what to do there?
It sounds like we probably don't need to review the PR yet, we should just discuss on the issue for now.
**Diego Hurtado** 11:11 Exactly, yeah.
Go ahead.
Because we should not open PRs just like that, we should open an issue first.
**Tammy Baylis** 11:23 Great.
It's 9-10, so I think we'll cap it at that today.
Over to you, Erin, thank you.
**Aaron Abbott** 11:36 Yep, sure, I can share, and Again, I think we just have one agenda item right now. It's pretty slow.
Around here right now, but Oh, we've only added one, too. So, sorry, Dylan, I added…
**Dylan Russell** 11:54 Where is…
**Aaron Abbott** 11:56 Sorry.
I have too many tabs, give me one sec.
I'm sharing the notes, right?
Yeah, okay, good.
Yeah, so I added this complex attributes one, it's… I added a lot of reviews, so thank you, Dylan, for your patience. And I think, just, I want to… I want to get this one right, because it's a… Pretty big change.
I think, for the most part, everything looks good. There's… it's had a lot of scrutiny. It's got 153 comments, which is… Maybe not a record, but pretty good.
And yeah, I think one of the only things I want to discuss was, about the potential for this being a breaking change, and I think… There was a comment from Mike, I don't think Mike's around right now, but… It was basically raising that, you know, we're changing… most exporters do something like.
They loop over the attributes, and they check if it's an instance of something to try to figure out from this big union which, how to serialize the attributes.
And I think… Most of them, at least the ones in our repos, they have Like, an else case that handles the fallback, so they don't just, like, you know, explode or whatever, but… Let me see if I can find the comment.
**Dylan Russell** 13:23 Alright, I think I get what you're saying.
**Aaron Abbott** 13:26 Yeah.
So…
**Liudmila Molkova** 13:30 Let me see if I understand, so the concern is that Duh.
There are some exporters out there.
that… check instance off, or, his instance.
And… They do something terrible in the fallback.
That could explode.
**Aaron Abbott** 13:56 What is…
**Liudmila Molkova** 13:57 that that they could do that would explode. Like, the string should be fine, JSON dump should be fine.
What would they do with this unknown type that could explode?
**Aaron Abbott** 14:10 Okay, I'm trying to pull up the comment, and I think… I think I agree, like, we have to make this change.
I was just… I can't… there's something wrong with this GitHub.
**Dylan Russell** 14:22 Yeah, I also had issues doing that.
**Aaron Abbott** 14:25 Yeah, just completely breaks everything.
**Dylan Russell** 14:28 That's just, like, the code review tool. Like, you go… Fits it.
Yeah.
That's a good comment thread.
**Aaron Abbott** 14:37 Yeah, I think that's okay, we can just discuss it. Ludmila, I think… I think to your point, I don't have, like, a single concrete data point of something bad that one of them does, but just for example, they might have, like, a… Raise an exception if they get a type that they weren't expecting, because they assumed You know, the signature wouldn't change because it's a stable component.
**Liudmila Molkova** 15:03 Then they violate the design principles, like the error handling of open telemetry.
**Aaron Abbott** 15:13 Yeah.
**Liudmila Molkova** 15:13 Well, we have it documented in the spec, you shouldn't fail, and if you add it, well, you did it to yourself, I… how can we help?
**Aaron Abbott** 15:23 Yeah.
Okay,
**Diego Hurtado** 15:33 Add a message in the exception error that says, that will teach you.
**Liudmila Molkova** 15:39 Sorry?
**Diego Hurtado** 15:39 Be it to yourself.
Yeah, you should…
**Liudmila Molkova** 15:41 Yeah.
**Diego Hurtado** 15:42 that to the exception message. You did this to yourself, and that will teach you a lesson, you know.
**Lukas Hering** 15:51 I was able to expand the fold.
Conver… it's just, if you go back to the conversation, it's the first… Comment, if you wanted to view it.
**Aaron Abbott** 16:03 Do you have a link?
**Lukas Hering** 16:06 It's in the PR, like, click open, like, 135, like, go to… go to conversation.
**Aaron Abbott** 16:14 Oh, okay, okay, and then open all these.
**Lukas Hering** 16:17 And then it's the top one from Mike, I think.
**Aaron Abbott** 16:20 I don't know.
**Lukas Hering** 16:22 Yep.
**Aaron Abbott** 16:27 This one. Okay, awesome, thank you.
Gotta work around the new UI.
Yeah, and I think… I think you said the same thing.
**Lukas Hering** 16:35 Actually, no, I said that I didn't realize what he was saying. I was like, if you expand the types, it should be fine, but yeah, you're right, if it's doing its instance of checks, then they will change the behavior.
**Aaron Abbott** 16:50 Yo.
I mean, I don't think we can't make this change, but I was hoping to go poke around at some of the other, implementation, so, like, for example, I imagine in Go, the attributes is… There's an interface, and then you either are expected to do, like, type matching type assertions, or They might have, like, an as, whatever, as int, as, map, as whatever.
And then they would have had to expand the… you know.
the… the function signature, which I guess… we don't need to get into, like, the semantics for each language, but yeah, I think we have to make this change and maybe just call out, like, loudly. I wish Mike was around, but… Yeah, I can't really defend it either, I just… Don't want to upset people, that's all.
**Liudmila Molkova** 17:42 Okay, I think that it's… the ball is on my side, and you mentioned me, and I never came back. I was going to check what Java does, and… I can… I'll finally do this, and I'll leave a comment. We bat this to death in this pack, like, the aspect of it breaking, and, like… the… alternatives are terrible. We would have a different… alias for extended types. We would need a different, whatever, load or union.
And I don't know how to handle it in Python, but people tried it in Java, and they… like, one of the reasons we allowed extended attributes everywhere is because, like, the need to maintain two different types and to convert between them.
is very difficult.
**Aaron Abbott** 18:39 Yep.
I agree, and I think that's why this PR removes, like, I think 600 lines is pretty… Pretty nice from that, aspect.
What was I gonna say?
Yeah, and then one other comment I was gonna make was, like, this change is pretty much just mechanical now. I think there's no instrumentation out there that sets complex attributes for, span attributes or for metric attributes, so… It's kind of a no-op for this first release, hopefully, and the exporters would fail once people start sending data that, would run into these issues, so I think… From that perspective, it's like, The onus is on the exporter to support their users, so… Yeah.
**Liudmila Molkova** 19:32 Now, the other alternative approach we could explore, if we want to be really cautious, which I don't think we should be, but we could, is that it's enabled with some flag.
And, it's just these attributes don't go through, or are we to JSON, like, JSON dump them, or string them, something?
**Aaron Abbott** 19:58 Yep.
**Liudmila Molkova** 19:59 And then, in the whatever… If it ever happens.
the future major version is that we do this, but also, yes, as I mentioned, that it's handled by instrumentations.
And instrumentations can control whether they Start emitting them with feature flag, or major version bump.
**Aaron Abbott** 20:29 Yeah.
Okay, so maybe… I think that's all we really need to say right now. We could follow up with, like, I can… I can book around and see if Go did it, I think… I could check with Robert, one of the maintainers there, and Yeah, I know also, obviously, JS and Java have done SDK major version bumps, so I don't know if they coupled this with that, but I'm hoping we can avoid that for this specific change, and
**Liudmila Molkova** 20:55 Java didn't do a major version bump, they exposed it on the API without major version bump.
**Aaron Abbott** 21:06 Okay, yeah, and I'm not… to be clear, I'm not concerned about the API, I'm just concerned about the SDK components that people implement.
**Liudmila Molkova** 21:12 Like that. Right.
**Aaron Abbott** 21:13 Yep.
Okay, cool. Does anybody else have thoughts on that, or we'll go on to the next one?
Okay, cool.
Ludmila.
**Liudmila Molkova** 21:31 Yeah, so I… we talked about it.
multiple times, and I don't think we've ever… Proceed with removal of Gen AI packages from this repo.
So, or deprecation.
So, unless there is some work in progress that they didn't notice.
I'll just send a couple of PRs. The first one is to completely remove things that we never released from Contrib.
And Dan… The second one is to deprecate the packages that we release.
Released, but, they moved away.
Check in if anybody is, or if you heard anything, because I think somebody else wanted to do this.
Cool, then I'll just send FPR.
the first PR I post in the GenAI… And then Python, Slacks.
And we'll see if anybody complains, or… has it in flight?
**Aaron Abbott** 22:43 I want to say that Surya was asking about this as well.
I don't think…
**Liudmila Molkova** 22:50 Kim.
**Aaron Abbott** 22:51 Yeah, yeah, maybe just ping everybody.
**Liudmila Molkova** 22:54 Yeah.
**Aaron Abbott** 22:56 To be clear, though, is this about just deleting the code, or is it about, like… because the package names for some of… for most of these are different, so we would be, like, what would deprecating them mean? Like, do you want to add… Deprecated annotation, and then do another final release of them.
**Liudmila Molkova** 23:12 Yeah, so there are 4 that were never released from this repo. For them, I will just remove the code.
And now, like, we have a README in Instrumentation Gen AI folder, and for this, I'll, just leave in the README that they have moved.
there are also four that we did release.
It's, to your OpenAI friends.
One Google Gen AI and one Vertex.
Victor's didn't move, so I'm thinking… maybe it was a special PR, too, and we can polish it, but since the original library is deprecated, we should probably deprecate instrumentation for it as well.
And, I don't know if you need to do my final release… Hmm, not sure.
For OpenAI France and Google Gen AI, Sorry, Google Gen AI is also special because we didn't change the package name, it's just the… the code has moved to a new place.
And for this one, well, we can make a final release, we can say that… I'll see, okay, because I'm not sure, because it's just the continuous from the new version from the new repo.
But to OpenAI friends, I think we have to make a final release for them. We will point to the new place, we will mark them as deprecated. I'm not sure if we can do this from the code. I'll check, maybe I'll need some help with the PyPy, if it happens there.
**Aaron Abbott** 24:59 Yeah, so that you can… we can do this, it's gotta work. There's, like, an at deprecated… You'll probably find some examples in the code, and then it at least alerts people who are importing it.
There's no way to deprecate on PyPi, unfortunately. We usually just, like, update the README, and then, Yeah, update the README, and then do a final release.
**Liudmila Molkova** 25:24 Awesome. Yeah.
**Aaron Abbott** 25:27 Yep.
Yeah, that all sounds great to me. Thank you.
**Liudmila Molkova** 25:39 Of course, excited.
Removing cod is so amazing.
She did it all the time.
**Aaron Abbott** 25:46 Yeah.
I think we actually did… we talked maybe, like, 2 weeks ago, I think… There was an old elastic instrumentation that we're removing as well, so… I think it's the right direction, and maybe Ricardo already sent that, we could probably just copy whatever he did.
**Liudmila Molkova** 26:05 I'll check. Thanks a lot.
**Aaron Abbott** 26:11 Alright, cool. Anybody else have topics?
**Dylan Russell** 26:15 I just posted a PR.
I think this was, like, Gen AI… generated, but… I'm curious how we would do… This the right way.
If you go into, like, Files Changed.
Yeah, so it's trying to update this bootstrap script to get the… like, GenAI instrumentations from the other repo into it.
**Aaron Abbott** 26:52 Hmm.
Right.
**Dylan Russell** 26:56 Right. But I just did it by, like, hard-coding them.
**Aaron Abbott** 27:02 Yeah, so one thought… let me see if this works… Peace.
So some… some of them, I believe.
Yeah, so a lot of the contrib ones, they have, like, a pinned version, and then we update this file every time we do a release.
And I think That makes sense for the ones that are in, like, the lockstep, Modern repo release, and then… I believe for the ones that… some of the Gen AI ones, like this one, I thought was already in here.
Maybe it wasn't already in… yeah.
Well, I guess what I would propose is something similar to this. We can just leave, like, a… version constraint and manually edit it. I don't think… Because they're versioned separately, it seems reasonable to me.
**Dylan Russell** 27:55 Sorry.
Yep.
**Liudmila Molkova** 27:57 Go ahead.
**Dylan Russell** 27:58 So every time we do a release, just come and manually bump.
the version here.
I guess that's not too bad.
**Aaron Abbott** 28:09 Well, no, I would propose just like… like this, like, leave it at greater than… greater than equal, and then… If we do a major version bump, we could come in here and update it, if we decide to.
**Dylan Russell** 28:21 Oh, okay. So we don't need to upgrade the miner version? Like, it'll… There's no reason to do that.
Okay.
**Aaron Abbott** 28:30 Yeah, I mean, some… somebody keep me honest here, but I think… It literally will just run pip install with whatever version string we put here, if you do… when you do the OpenTelemetry Bootstrap script, so… We could do, like, any… constraints we want. If there's, like, bad releases or something.
We could obviously yank them, but we could come in here and update it here as well if we wanted. So just whatever… Requirement string we want should be okay.
**Dylan Russell** 28:59 Okay, yeah, that seems okay then.
**Aaron Abbott** 29:04 Yeah.
**Liudmila Molkova** 29:04 This is the script that lists all instrumentations that would come with the distro.
**Aaron Abbott** 29:14 Sort of. It's like… there's this OpenTelemetry bootstrap command, and it… Edits your… it looks at your installed libraries, and it tries to find instrumentations for them, and then install them for you at runtime.
**Liudmila Molkova** 29:31 Okay, nice.
**Aaron Abbott** 29:35 Yeah.
Maybe a more interesting one is actually this one, so there's this contrib… I did it.
This one.
So this one is, like, a meta package. It just, like, lists all the contrib ones, and we also update this every release, because it's using all the pin versions, but… This one is, like, you know, we… sometimes people will just install everything.
And then the… when they run OpenTelemetry Instrument, it goes through and it looks that the… instrumented libraries installed, and if it is, it will… it will run the .instrument for the instrumenters, so… is a good question if we would add these here, or maybe we could just add in the GenAI repo, like, another similar one that's, like, a meta package that has all the Gen AI.
packages.
**Diego Hurtado** 30:32 Don't you think we should actually deprecate this, too?
Considering the fact that, Significant instrumentations are moving away.
So… we will… We're just not adding them into this list, so it's kinda… Pointless to try to maintain these lists.
significant.
Right?
**Aaron Abbott** 31:02 I don't know if I got the first point, Diego. You said… Something's going away.
**Diego Hurtado** 31:07 I mean, my point is that, if… if… If other instrumentations are gonna… leave outside.
this repo, right, and Does it really serve any purpose, this… this package.
**Aaron Abbott** 31:33 You mean, like…
**Liudmila Molkova** 31:34 to use… Sorry.
**Aaron Abbott** 31:37 Go ahead, Liudmila, please.
**Liudmila Molkova** 31:39 Is this what users… so, like, I would imagine that users that install Python destroy?
They would… Get a set of libraries that's, like, orthogonal to repos.
It could be some labor is from GenAI repo, or from whatever, if another OpenTelemetry Python instrumentation thing happens.
Where… Is it not the case?
That… We want things from different tripos to converse into the distro, or it's unrelated to distro at all, sorry.
**Diego Hurtado** 32:26 Aaron, were you about to say something?
**Aaron Abbott** 32:29 No, no, please, go ahead.
**Diego Hurtado** 32:32 Yeah, I just don't understand, well, the point of having a package that installs all the instrumentations, if… If we… when we had all these fermentation in the same place.
Alright, maybe that was the point, but… Now that they're moving away, does… Really making sense to try to keep this.
Package.
**Aaron Abbott** 32:59 What do you mean by moving away? Are you just talking about the Gen AI ones, or are you talking about the general, like, project vision to have people maintain their own instrumentations?
**Diego Hurtado** 33:09 Yeah, both cases.
**Aaron Abbott** 33:13 Yeah. I mean, I think, practically, it's… it's kind of useful. I think Emidio said 200… it has 251,000 Was it per month?
Downloads per month, yeah.
So, I think… I think people use it, and I've also seen this kind of pattern, and I think JS has a really similar package that installs all the contrib instrumentations. And honestly, like.
This seems more useful to me than the bootstrap one, because The instrumentations don't depend directly on much, so just pulling them all in and then waiting to, you know, see what happens at runtime seems better than… Trying to have the bootstrap thing look at the virtual environment, and then derive which instrumentations to install, so… That's my two cents, but… Yeah.
**Diego Hurtado** 34:03 Yeah.
That's fine. To be honest, Neither of those are required by the spec, right?
**Aaron Abbott** 34:16 I mean… I don't think the specs says anything about, like, auto-instrumentation.
In general, right?
**Diego Hurtado** 34:24 Yeah, the first OTEP is our documentation. It kind of defines the intention, the mechanism, but I think we tried to make something useful for users here, and in Bootstrap.
And I don't know, maybe we just, produce something that, With the good intention of making lives easier for users, but we also ended up Making something that is… Not practical to support, in a complete way.
Because limitations can exist anywhere.
Just made two sense, I mean, I guess it doesn't hurt to To keep it, but If, anyone thinks, we… we could… Stop supporting it or removing, and I wouldn't oppose.
**Aaron Abbott** 35:26 Okay.
Cool, maybe… yeah, discussion for another day, or if you want to file an issue, but I… I think I prefer to keep this one for now, and could chat with other people, but… I don't know, Dylan, does that… Help with your original question at all?
**Dylan Russell** 35:45 Yeah, yeah.
I'll propose something similar to what the GenAI CL did.
And… Yeah, I think… Sounds good.
**Aaron Abbott** 36:03 Cool.
Alright, and I think that was it for today, so… A nice half-hour meeting.
Unless anybody else has anything, we'll call it there.
Alright, see y'all next week, thank you.
**Diego Hurtado** 36:21 There you go.
