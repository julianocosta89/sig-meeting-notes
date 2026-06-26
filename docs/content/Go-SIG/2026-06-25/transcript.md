SIG: Go SIG
Date: 2026-06-25
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Pellared** 01:54 Hello, can you hear me?
**Tyler Yahn** 01:56 Yep.
**Puneet Singh** 01:57 Yes.
**Tyler Yahn** 01:57 gone.
**Pellared** 02:00 Good.
It's extremely hot here, how about you?
It's only Europe, or not only?
**Tyler Yahn** 02:08 I mean… no, it's not hot here, no. Puneet, how about you?
**Puneet Singh** 02:15 I'm good, thank you. It's been 9.30 for me in India, so I'm done with dinner and all, so yeah, pretty good.
**Pellared** 02:23 How many?
**Tyler Yahn** 02:26 No, no, he said it's after 9.30 there.
**Pellared** 02:29 I heard you. Okay.
**Tyler Yahn** 02:32 Yeah.
**Pellared** 02:33 For us, like, in Poland, it's going to be, like, more than 100 Fahrenheit.
extraordinary here.
**Tyler Yahn** 02:44 Yeah, I was gonna say, you guys don't have a lot of AC over there, right?
**Pellared** 02:47 No.
**Puneet Singh** 02:51 Yeah.
**Tyler Yahn** 02:51 I'm not tempting.
**Puneet Singh** 02:52 that the European countries and also in UK also, they're just starting to realize that, you know, those homes which are built for heating, they might have to, you know, adjust a little bit, actually, for air conditioning also.
**Tyler Yahn** 03:08 Yeah, I feel like that…
**Pellared** 03:10 Just… hopefully just be… it'll be just two weeks or something.
**Tyler Yahn** 03:16 Even, like, 2 days sounds like a lot to me, but yeah.
**Pellared** 03:21 Just run away to a forest.
**Tyler Yahn** 03:24 I was gonna say, we're gonna see Robert next week, and he's just gonna be, like, in a tank top, and, like, sweating, and, like…
**Puneet Singh** 03:31 It's, it's 35 degrees Celsius here.
Right now, so I'm not sure what's the weather… I mean, temperature right now. Yeah.
**Tyler Yahn** 03:43 what's… Robert, it's probably, like, like, 21 here. So, yeah.
**Pellared** 03:50 Very nice temperature.
**Tyler Yahn** 03:52 Yeah, very nice, yeah.
Cool.
Awesome. I think we could probably get started here. This is probably Quorum for the day. If you haven't yet, go ahead and add your name to the attendees list. If you have agenda items you wanted to talk about, go ahead and add them there as well. I'm gonna… Start sharing my screen, and we can, jump in here… Oh, my name's already on there. Okay, cool.
Awesome. Alright, so I wanted to start us off by talking about the Semikov, changes coming down the pipeline. So, there's this push to do, federation of semantic conventions. Well, I guess it's always existed. It's just more of a push to do that internally to the hotel semantic conventions right now.
Which means that things like the Gen AI and, like, a bunch of other, semantic conventions are gonna get pushed out of, essentially, like, the default, like, schema URL. It's going to be… it's like its own… generated package, so, I guess that's the question, is like, how does that become its own thing?
distribution for us, and what does that look like? So, like, right now, One thing that really can't happen is just regeneration, and trying to just shoehorn in, like, say you take the GenAI semantic conventions, which you can't do yet, because they haven't been released, the new ones haven't been released. The old ones have been deprecated, but say you take the new ones and you try to just, like, generate them in place for what the old ones used to be, they have a different schema URL. So, like, you couldn't do that. Like, the… using the schema URL that exists in that package is going to be wrong.
the versioning is also gonna be wrong. The Gen AI are not gonna be of the 144, whatever the number comes out to that they get released at, they're gonna be their own release versioning cycle. And so, like, there's… there's a need to readdress, like, how I think this SEMCOG package looks, because of this.
I think that there's a lot of… there's still, unfortunately, like, I think a fair amount of open questions to me, probably to others, Around, like, what this actually is gonna look like.
I asked a bunch of questions here.
I still wasn't 100% sure, but, like, I think the…
**Pellared** 06:19 I think this is also important. I also changed the mainframe seek, which also is the second one, which is, like, in a separate repository, but they just haven't started, you know, getting, you know, things in. So one of the things that they… we were concerned, we were discussing it.
It's like, how, how you will reuse the attributes from the main SEMCOND in the second federated, you know, in the second federated, SAMCon. Will you also… how will you keep the versioning between those? Is it already under Styler, or not really?
**Tyler Yahn** 07:00 No, I don't…
**Pellared** 07:01 Dependencies.
Yeah, because, for instance, you know, the main friends, IBM, is heavily reliant on databases.
So, most probably anything you'll do on the mainframes is also doing something in databases, you know, like a DP2. So, even if you make a change in the tile, it's usually a change also in the database, so it can be rolled out, rolled back, etc. So… this is also something how we'll generate a code, if you want to have, you know, an instrumentation, or… so, I don't say we, but someone who wants to have, you know, attributes from database and from, from mainframe in a single instrumentation library.
**Tyler Yahn** 07:42 So that, I think there is, like, recommendation on that one. That one was something that was discussed in the semantic conventions and in other parts of the meeting, and that goes back to, like, this idea of, like, what is the atom of semantic conventions? And, like, it is not an attribute in a lot of people's, view on this. It's the span.
So essentially that comes… that traces back to, like, to have it in the same instrumentation package is not a problem. It's just you would use a separate tracer, a separate meter, or a separate blogger in the process of generating whatever those, like, records are, right?
But the more important thing that kind of, like, you're working at here is that, like, attributes actually are kind of the atom, because, like, how are they, like, represented in a resource? Like, they're represented as attributes, right? Like, and semantic conventions covers resources, And I think, like, it's not entirely clear even, yeah, like, I mean, like, yeah, we have HTTP transportation that emit you know, spans that have attributes of all of these different types, like HTTP, URL, server, network, error type, like, all of these different, like.
namespaces, I don't know… yeah, I don't know the answer to that question. I don't know how this needs to get structured, like, is there, like, like, going to be still, like, a centralized SEMCOM dependency, like, place that we just have, like, a catch-all? Are they just gonna get regenerated, like, and duplicated all over the place? Like… Yeah, I don't know, I don't know that answer.
I do know that, like, what we have doesn't… isn't gonna work, though, with what's getting pushed on the pipeline.
I guess is my question.
So yeah, I'm not… sorry, like, I don't mean to be that guy, but I'm also not coming to the SIG meeting with a solution here. I'm just coming with a problem, unfortunately. And that's more just, like, to raise the issue and say, like, hey, like.
if you are interested, or… I don't know, if you're a maintainer, you need to be interested in, like, what we're gonna do here, because I don't know what the answer is, and I don't know that the semantic conventions themselves know… our pain points right now, is kind of the problem. I've tried to, like, add a comment here, if folks would like, also comment, maybe comments on this, like, Federation… pull request here, I think that that might be helpful in, like, understanding, like.
what their, their, understanding is, and, like, I would ask, like, if you have… You know, you come away from this with a clear understanding of how to, like, solve this problem.
like… I would appreciate that, like, I'd love… I'd love your insights on how we could solve these things, and, like, maybe get a proposal together, get some sort of proof of concept together, Yeah, because otherwise, I'm not exactly sure how some of these issues, like Robert's talking about, are gonna get actually resolved. I do know that, like… we can split out this package, and, like, I think there's a lot of really good design things of, like, how we could address, like, a different semantic convention package, and packaging structure, and, like, that kind of thing, like, I think that there's a lot of, like, I think it's maybe even an opportunity, we can clean things up and, like, redo things, but, like.
If we go and release that, and then, like, we're still not compliant, and, like, we still have these edge cases, and, like, we have these, like, dependency problems, then, like, that's not gonna be… that's not viable, either. So, yeah.
So, yeah, As a heads up on that one, I don't know the solution. I haven't got any response on this yet. I don't expect it to be that fast. It's kind of… it's a big PR.
But if other folks could maybe also take a look… maybe I'm asking dumb questions, and, like, there's just, like, super obvious ways to, like… resolve some of these questions, but, like, these are kind of, like, the big things that, like, came to mind for me when I was looking at, like, how am I actually going to implement this?
And so, yeah.
Review would be… be helpful.
**David Ashpole** 11:51 I know Josh has told me that, or I feel like one good thing that could come out of this is having, to go… Runtime semantic conventions just live in the Go Runtime package.
**Tyler Yahn** 12:05 Yeah, like, so… that was another thing that Daniel Dyla had also said, was just, like.
**David Ashpole** 12:13 We can move out.
**Tyler Yahn** 12:15 Yeah, like, instead of actually having, a semconf package, like, they would just… like, every instrumentation package would generate their own semantic conventions that they would want to use.
It'd be kind of, like, I think that'd be awkward. It'd be kind of a burden to put on instrumentation authors to be like, you know, I think we could try to build tooling, but still, it's just like, okay, cool, like, I need you to, like… first understand semantic conventions, and then all of the syntax and format there, and then pass it to some sort of tooling that we have, and then we'll give you some Go code, and then from there, you should be able to go and, like, run your things.
like… That would be complicated, but honestly, it still doesn't solve all the problems, right? Because, like, what Robert was just saying, like.
like, just, like, what's a dependency graph look like there, right? Like, so say you want to go generate HTTP instrumentation, like, does that automatically pull in the net, the URL, the error type, all these things? Like, what version does it pull in? Does it, like… Like, these are all…
**David Ashpole** 13:12 The one thing I do remember from the proposal, and I apologize, I haven't reviewed it in a month or so, but is that All of the… You always reference a single version of the core semantic conventions.
In… in your, your.
**Tyler Yahn** 13:30 But what happens when you don't?
What do you mean? Honestly, like, the diamond dependency becomes a problem then, right?
**David Ashpole** 13:38 Yeah, well… Diamond meaning cyclical, or diamond meaning…
**Tyler Yahn** 13:46 Diamond meaning that, like, you take a dependency, on something.
And then those two different dependencies that you have have different conflicting versions of the core semantic conventions.
**David Ashpole** 13:58 Then you can't depend on them, right?
Because you don't actually… I guess in the model that I remember Reading, you actually only take a dependency on the core one.
But I guess there is a question of, like, how do you…
**Tyler Yahn** 14:12 Yeah, give it.
**David Ashpole** 14:13 salt.
**Tyler Yahn** 14:14 Yeah, like, I take a dependency on the core one, I import the mainframe, I import GenAI, they both take a dependency on different versions of the core one, like, alright, so now I've got 3 different versions of the core, like, what am I using here?
**David Ashpole** 14:26 You are restricted, I guess, to only versions of those other dependencies that use the same version of the core. I have to go re-read.
But…
**Tyler Yahn** 14:36 Yeah, but I mean, like, what if they don't exist? Like, that's, like, that's exactly the diamond dependency problem, right? Is, like, what if the Gen AI have not upgraded to the latest, but mainframe has, right? Like, so this is, like.
I think this is, like, still very important to, like, get a resolution here. It's also still not, like, immediately clear, like.
what happens with conflicting schema URLs? Like, like, you go and you're providing a resource detector, like, I don't understand how… I provide a resource detector that has, like.
two schema URLs. Like, I guess the suggestion right now is you just drop them, but like… Is that really?
I don't know, like… I guess that's, I think, my ultimate question, is, like, there's still a lot of, like, attribute resolution problems here, not necessarily, like, packaging structure problems.
Like, I… I think that it's great, it'd be great to, like, have these independent versionings, but, like, splitting it out is causing actual problems, and implementation is the problem.
So… Yeah, I mean, if you have more insights, David, I'd love to hear them.
**David Ashpole** 15:49 I don't… yeah, I haven't… haven't paged this back in yet.
**Tyler Yahn** 15:53 Okay.
Okay, well, then maybe we could follow up next week, I imagine we're gonna keep following up.
it's already split out, the Gen AI stuff, so… I was told that, like, it's gonna take, like, a few months for us to actually land, but… like, I think we need to get ahead of it, because, like, just not having versioning support for Gen AI stuff is, like.
I don't know. It's one thing, but not being able to support semantic conventures in general is gonna be kind of a problem.
But no reason.
Moving on. So, the next thing, I wanted to discuss was, this improved GitHub release notes by publishing module-specific releases. I totally forgot I, like, opened this.
So one of the things that, like, I had… I've had multiple conversations with multiple people over years at this point, And the question that they always have is, like.
Let's see, I'm using the, Petrix SDK, package. Cool, I've got this one bug, let's see if it's resolved in, like, this upcoming release.
I have no idea, right? Because all of these release notes, like, are for everything that has ever been produced in all of the versions and all the mod sets that are existing here, right? So, It's not really helpful to users, So, the thing that I'm thinking is, is, like, there's nothing really stopping us from building some tooling around, just doing different releases by module.
the… I think our versioning policy… just to be clear up front, like, I don't think our versioning policy should change. I think we should still, like, in lockstep, publish, like, stable, you know, 145 or 146 releases, that kind of thing.
It's more about, like, once you publish, like, them to, like, a Go proxy or something like that, how do you represent that in GitHub, for users to easily parse?
essentially a very dedicated change set. So it comes back more around the question of, like, can we improve our changelog?
And then… and then plumb that into a release process. So really, like, at its core, is, like, a changelog question.
Yeah, so I wanted to just, like, kind of, like, go through some of these, like, things that I was thinking through, and, like, trying to resolve this. At the end of the day, like, my goal is that users can come to the repository, they can find, like, some sort of release stream for a particular module, look that up, and then they can find all the changes that they actually want.
even maybe, in the changelog itself, I would probably say maybe just at the beginning, just keep the root changelog the same format, just for, like, continuity, but, like, the releases would be, like, the partitioned ones, at least for now.
That means that, like, we're gonna need some way to, like.
compose changelog entries. I would… I would suggest, So, GitHub releases, I think that… sorry, go ahead.
**David Ashpole** 18:47 I mean, the collectors… A couple miles ahead of us on this, right?
**Tyler Yahn** 18:51 Yeah, so, let's just jump… let's jump to that, yeah. Then, I think, yeah. So, yeah. I agreed, they are. And, like, the… there's really nothing stopping us from using the CH log gen, other than the fact that, like, we use a completely different format.
there's nothing stopping us from updating SageLoggen to use, like, this, keep a changelog format. So, I think that… I think you're right, and I think we should start to, like, look into adopting this tooling.
I think this tooling becomes, like, the key that helps us, like, unlock things. We could just recreate this, like, or we could try to just, you know, extend this to make it work for us as well. I think this is kind of my goal here.
But yeah, my goal here is essentially, like, take chloggen and update it so that it, like, supports our format.
but also make it module-aware, because, like, that's another thing that it is missing, is, like, right now, it's kind of the same thing in the collector, where it's just, like, there is a changelog entry per everything, right? And so it'd be really cool, like, you can start splitting that up by, like, putting different subsets of the changelogs, but, like.
It's, you know… Yeah, I think there's different ways to do this. One is just putting chloggen, like, files in every module directory. Another is that you could have, like, the actual entries for the chloggens include, like.
other modules, you know, a module, like, list that it applies to. So these are things that, like, maybe it's worth taking a look at.
all of these things can be automated, all of these things can be put into some sort of, like, PR, validation. You know, that's also my other goal, is that, like.
Right now, there's a lot of burden, I think, on users to write, changelog entries.
It'd be cool if you could just get it to do some of them, you know.
maybe not completely hands-off, but, like, provide a little more automation around, like, this is the format that we would expect, these are the places that it will apply, and that kind of thing.
But yeah, David, I think to your point, like, adopting CH logjam would be great.
Yeah, and so then, from there, once you start building out changelogs that… or changelog entries, at least, if you can get not only what they are, but, have them be modular aware, then it's just about tooling, and building that tooling out into building the changelog, release automation.
I guess artifact signing is kind of an important one, because, like, right now, we are using, we developed the, GPG signatures for our artifacts, which was great. It's a manual check, right? Cosign… I don't know if it came out right when we were doing it, or at least we weren't aware of it, but, like, that also exists. I think we should probably start moving to COSign, just because it can be built into the automation pipeline. We don't have to, like, manually go in, do verifications, and then do the signatures. So, yeah, I think that that's kind of… kind of what I would say we'd want to do. Yeah. And so, yeah, I think… go ahead.
**David Ashpole** 21:36 I was gonna say, it would be really cool if, releasing was as simple as, like… triggering a GitHub action or something.
**Tyler Yahn** 21:43 That's what my goal on this process is, exactly what you just said, yeah.
**Pellared** 21:46 I think the only reason we did it this way is that it was, like.
gave us an example on some Apache recommendations taken from OpenSSF or something like that, when we were trying to, you know, have the… just go with the checklist. And I think we just, you know, went… we just selected this one as recommended, and we agreed that we can follow up on this.
This is what I remember, like, 2002. One year ago, or something like that, or even more.
And I'm pretty sure that it can be improved to use cosign.
**Tyler Yahn** 22:18 Yeah, I don't think there's too much contention there. Yeah.
Yeah, but David, to your point around the release automation, that's also my goal, is that, like, I'd rather it not be, Yeah, essentially, like, the whole, like, building process, like, obviously, like, the tagging and pushing process, I think, might still need to be a manual thing, but, like, at least the release generation stuff, just because, like, it needs to get signed, those tags need to be signed, And so…
**David Ashpole** 22:46 But… I guess. What's up They have to be signed, like, by private keys on our various…
**Tyler Yahn** 22:53 Yeah.
**David Ashpole** 22:53 Right, essentially, yeah.
**Tyler Yahn** 22:54 And I would… I'd probably want to keep it that way.
**David Ashpole** 22:57 Yeah.
**Tyler Yahn** 22:58 Just for, yeah, keeping a human in the loop kind of thing.
But then, the actual generation of the release itself, like, we have this in Obi where essentially, like, we can build tooling, it will automatically draft a release, it puts it in a draft mode for us, and then we just go in and we go, like, yeah, this looks right, maybe change some wording if it needs to, the artifacts are already uploaded for us.
we just go in and verify it all there, and it just goes from, like, okay, publish, and, like, that's all we have to do.
I'd like to get it to that point for here as well, especially if, you know, each release is going to be 10, 15 releases, right? Like… that's not really something that I would want a maintainer to go and have to draft each one of those releases, right? So, like, I'd rather it just be they review those releases, and say, like, yeah, this looks good, there's the artifacts, like, go ahead, publish. Or even having, like, tooling, where it's just like, I've already reviewed them all, just publish all of them, kind of thing. Like, that seems fine to me, too.
So yeah, I agree, like, I really want to, like, to release, or relieve, like, a little bit of the maintainer burden on this, as well as trying to provide user value at the same time.
But… Cool. It's not…
**Puneet Singh** 24:09 That's priority.
One question. Is the current release process already documented somewhere?
**Tyler Yahn** 24:15 The existing release process? Is that what you said? Yeah, it is. Yeah, it's in releasing.empt.
**Puneet Singh** 24:22 Okay.
**Pellared** 24:26 Just one question to the goal.
reasons. You want to have one change lock, because… because of the precedence that we had it this way so far, and just not, like, you know.
Change and split it, and not to have this burden, and just to have it, you know, easier, instead of splitting a changelog for each module.
Okay.
**Tyler Yahn** 24:50 Yeah, yeah, I mean, and I'm not, like, yeah, like… My thought on that is that, like, if there's somebody out there who subscribes to that file and, like, is actually reading it, If we have tooling that is, like, automatically, like, able to just keep on generating it, then, like, just… just keep generating it, yep.
I don't know if I would generate it on every single, like, PR. I'd maybe just say, like, at the time that you do a release, just regenerate the whole…
**Pellared** 25:15 Yeah, release.
**Tyler Yahn** 25:16 Yeah, four different things.
**Pellared** 25:17 200 degrees.
**Tyler Yahn** 25:18 And I'm fine if, like, People are like, that's kind of just, like.
just… just cut it out, like, we could just stop publishing it? That's fine too. Like, I don't… I don't have strong preferences there. I was just doing it more for compatibility, yeah.
**Pellared** 25:32 Yeah, I think it… I think it makes sense. I will think about having a separate new changelog for each module, but I think we can be also addressed later, let's not put too much on the plate, you know, let's just… Yeah.
**Tyler Yahn** 25:44 I think the changelog per module could be helpful, like, if somebody comes to us and they're like, I'd rather there's a file here or something like that, like, that's fine, but, like, if we're already parsing it into each release, like, there's nothing stopping us retroactively from going and saying, like.
go through every single release and just pull out all the ones here. The only thing is, is, like, there's a demarcation between, like, when we start this new process and when the old one exists, because we can't go back.
beyond that, right? Like… Not without a lot of… pain and effort of years of archaeology there.
So, yeah, I think that, like… Yeah, I think that was kind of just my thought.
I'm not too critical on, like, what the changelog files are themselves, because, like, all the feedback I got from users is not, like, hey, I went to your changelog, and I couldn't figure it out from your changelog. It's, like, I went to the release, and I couldn't, like, I couldn't tell on this release if it solved my problem or not, yeah.
So… Okay.
If you have comments, thoughts, ideas, please take a look at the linked issue, and then, yeah, we'll… we'll try to prioritize that in the future. I don't have, like, a timeline on that, it's not included in our, like, yearly goals either, so I'm not trying to, like, push this through, but, I do think, like, it'd be valuable, and I wanted to run it by folks.
Okay, next up, Puneet, you wanted to ask about clarification on adder norm versus adder dedupe package?
**Puneet Singh** 27:11 Yeah, so I think this was, issue raised by Robert. This was regarding, a truncation check for the attribute.
For the slice part, which need to… I mean, the existing logic, it, copies the slice, so it does kind of allocation before telling that whether we need truncation or not.
And the… the alternative was to use the unsafe pointer approach to look into the… to look into the structure.
part of it already exists in the D2 package. So, I think Robert's, angle was to reuse that logic. My concern was more towards that I was looking a lot of touchpoints towards truncation, which could be moved to a single package.
So the idea came that, you know, if these two things should be consolidated into a single package, Robert, can you, I mean, feel free to, you know, pitch in if I'm… No, at some point.
**Pellared** 28:14 describe it probably better than I was.
**Puneet Singh** 28:17 Yup.
**Pellared** 28:18 Like, in between, like, the deduplication and the attribute limitation is basically, you know, the normalization that the SDK does when it, you know, processes the attributes, and it's then at the same time. And, you know, the code that tries to make it, you know, efficiently.
using, using unsafe code, etc, is kind of, the same. So I just propose to, you know, have it in utter attribute normalization, instead of for attribute, which is basically only a legacy of the stuff that I did recently when I was introducing map slices, etc. It's just a follow-up refactoring.
Yeah. So, you said the same, right? I think.
**Puneet Singh** 29:02 Yeah, yeah. So, I think based on what Tyler suggested, I realized that, keeping the things… I mean, duplication is better compared to sharing the stuff between modules.
And what I was thinking of is to move the truncation into its own package within the… I think this is… Okay, I made the change in the trace. So yeah, move the truncation logic into a dedicated package, and let it, you know, evolve, as in the more duplication we have, the better it makes the case for moving to a template-based, package like, ATTR dedupe is. I've not decided whether we can merge, ATTR norm, or, you know, consolidate both these packages, the deduplication and the truncation part together, actually.
I think the truncation part, I'm not… still not sure that it has enough duplication to come at the template table. That is my opinion here.
Does that make…
**Tyler Yahn** 30:08 Yeah, so just, like, my point is that, like, I don't think what I'm hearing is that this isn't supposed to be the end state, but, like.
This… this package can't get reused anywhere else in the SDK, is the problem. It can't get used in metrics, and it can't get used in logs.
That's gonna cross a module boundary.
**Pellared** 30:27 And… yes.
This one, yeah.
**Tyler Yahn** 30:30 So… The only place it can get used is in here in the spins. Like, if we wanted to… provide some sort of reusable package that is of this form, that's fine, I'm interested to see that proposal.
It would need to be a template, and you would need to go through, like, the templating process here.
**Pellared** 30:48 So that's what I suggested, the actual dedupe, because it's already done this way. So what I propose is just to rename…
**Tyler Yahn** 30:56 Hold on, hold on just a second. So, like, I'm open to that, but, like, if… if the templating is going to turn into, like, an OTel gRPC sort of thing, where there's, like, all these edge cases that are handled in… in, like.
yeah, I'm not into that. Like, I would be way more into just keeping the dedicated dedupe and truncation, or whatever packages, like.
Copying where you need to, kind of thing, and addressing bugs where you need to, like… Yeah, that's, I think, what I would say. If it isn't, like, and there is, like, core, actual, like, logic that is going to be, like, just one-for-one and everywhere, like, sure, let's look at the templates, but yeah, if it's going to have all these branching configurations, like, I just… I would not do that.
**Pellared** 31:43 I totally agree. It's supposed to be super simple, and just, you know, get the, you know, like, the limit, the attributes, and no more, you know, no logic connected to, you know, no, like, bull flags that I initially put, and stuff like that.
No control flags.
**Tyler Yahn** 32:02 Yeah, yeah, definitely no control flags. Yeah, exactly.
Does that… does that make sense? I don't know… I don't actually know the full problem set, but, like, just from the solution space that I'm seeing, like, that's… that's my feedback on this.
**Puneet Singh** 32:17 Yeah, I'll just to start with, I'll keep things separate, and in the specific modules, and if it comes, you know, if it starts to duplicate enough, then we'll think about the template approach, actually.
**Tyler Yahn** 32:31 Okay. Yeah, that sounds good. Like I said, like, I'm happy to evaluate it, but yeah, that's going to be my immediate feedback if I see things that are just, like, these parsed logics, right? But, like, yeah, there's definitely good use of the template as well, like, as you can see in our repos, like, we definitely use it, so, yeah.
**Puneet Singh** 32:47 Got it.
**Tyler Yahn** 32:49 Yeah, yay to monorepos.
Okay, cool. Puneet, does that make sense? Do you have a path forward on this one?
**Puneet Singh** 32:57 Yes, yes, I think this, yeah, it's sorted, I would say.
**Tyler Yahn** 33:01 Cool. Next up, you also wanted to ask about detector PRs.
**Puneet Singh** 33:08 Yeah, there are a bunch of them. I mean, some of them are, like, waiting for a while, so have a look if I've… you know, this is, like, take 2 minutes, so have a look and, you know, if you have any feedback, let me know.
**Tyler Yahn** 33:21 Yeah, thanks for raising these. I actually… was a little lost on this, I was looking at some of these yesterday and didn't know what was needed, the only… Yeah, let's maybe take a look really quick here.
The only thing is, is, like, I was noticing… I took a look, like, a week ago, I think, something like that, and I noticed a lot of them were using context backgrounds.
In places that… I don't think… would have been.
**Puneet Singh** 33:50 I think you suggested that feedback in one of the places I saw, actually.
**Tyler Yahn** 33:55 Okay.
**Puneet Singh** 33:57 Let me have a look and come back, you know, I'll, you know, make… just, try to include that change as well, and then I'll come back.
**Tyler Yahn** 34:06 Yeah, that's the only thing, like, I took a look, and then I got lost as to where I'd taken a look, And so, like, yeah, like, if all of them are using a passed-down context, like, let's keep doing that. Like, I'm totally on board for what we've got going on here. Like, all of these are great, and all of these are great, like, additions. It's just, yeah, that was my only, universal feedback, and I just, am overloaded. But yeah, if you could take a look.
Maybe just, like, ping me in Slack or something like that, and And let me know, and I'll take another look once you have.
**Puneet Singh** 34:39 Sure, sounds good.
**Tyler Yahn** 34:40 Okay.
Okay, cool. Next up, Robert, you wanted to talk about, this… Oh, this PR, yes.
**Pellared** 34:54 Yep.
So, first of all, Tyler, I think it's worth addressing. I think we just… we just, you know, meet some common agreements, whatever, which will be… we can always change it later. So, My concern with just, you know, not accepting major versions.
For direct dependencies is that we had this policy that we try to, you know, keep up and bump as much as possible to have, you know, security fixes and, you know, other fixes.
So, I initially thought doing it, you know, for the major, even just to have… even, you know, we know that the renovate PR will be unmergeable, because the import path changes, etc, but I thought about having this just a notification, but I saw that, I think, from us.
Send there is some way to configure it instead of disabling.
Probably there's something that it will be shown on the dashboard.
I have not checked in the renovate, how it will look right, but as far as I understand.
I guess it's, like, a third status, like, that you can, you know, go to… and probably it will just show up that you can… that it will, yeah, probably as you can do it manually. So, I think that's fine.
**Tyler Yahn** 36:16 Yeah, I mean, I'm fine with that, as long as you understand that, like, I'm not going to be looking at that dashboard, and that's something that is being done for you, right? Like… like, I'm not… I don't… like, that's not… I don't know what policy you were talking about, like, keeping it up to date, like, I'm fine with…
**Pellared** 36:31 You're welcome.
**Tyler Yahn** 36:32 merging minor releases, but, like, doing a major version, like, upgrade, I need, like, an actual reason to do that. I'm not… I'm not just going into the code and upgrading for upgrade's sake.
**Pellared** 36:40 Estacia.
**Tyler Yahn** 36:41 But if that's something that you're… you're looking to do, I'm fine including that. That's… I'm not opposed to that. I would… the only problem I have is that, like, I do a lot of these dependency PRs, and this is noise for me. Like, I spend a lot of time on these, and, like, I just have to go in and go, like, okay, close it, because…
**Pellared** 36:59 I see so…
**Tyler Yahn** 37:00 We're not touching this major upgrade.
**Pellared** 37:02 I would… okay, so what you say that, just to try to rephrase it, you think that, what you say that, It's the effort of making a major on your own is not worth the effort.
**Tyler Yahn** 37:17 No.
**Pellared** 37:17 There's not…
**Tyler Yahn** 37:19 it's not by default justified. Yeah, right. So, like, the effort on my part is definitely, like… like, if the effort is because, like.
that old major version, does not have a feature that we need. It has severe security vulnerabilities that, like, we've identified and need to move away from. Like, all of these things, like, that can definitely motivate me to get that, but, like.
Just because there is a new major version does not mean that, like, I need to upgrade to it.
**Pellared** 37:46 physical thing?
**Tyler Yahn** 37:47 That, that, it needs justification, is my idea.
**Pellared** 37:51 I think I'm fine with that. I'll just need to double-check what are the… non-V1 versions or dependencies.
I think it's only the backup, or have you checked if there's anything else that we use in.
**Tyler Yahn** 38:04 I sent you a link in that PR of the three that I found, that… that was the core. I didn't check contribib. Contrib, there's a lot more. Again, in the dashboard for dependency updates, you can also take a look at all of the ones that have been closed, Most of the ones that have been closed, you can see in the titles, whether it's, like, minor versus… or major versus major, and so you can find all those major upgrades there as well.
You have to click through them to find out if they're, indirect dependencies, or if they're direct dependencies. That's something, you have to filter through.
**Pellared** 38:36 I was just worried about direct. Indirect, I don't care because, you know, unsolvable.
**Tyler Yahn** 38:42 To be clear, like, I do look through the security advisory panel in GitHub, the one that tells you, like, you have a vulnerability.
**Pellared** 38:49 That's true.
**Tyler Yahn** 38:50 Those are the ones that, like, if I see there's a vulnerability with, like, a V4 that needs to go to a V5, that's the motivation I find. That's the dashboard I look at.
So, like, the renovate just opening these PRs is just noise for me, is why I was submitting this.
**Pellared** 39:07 By the way, one of the dependencies you also linked was just for GitHub Actions, so it will be still there.
Because you only disable it for Go modules.
**Tyler Yahn** 39:19 Okay.
**Pellared** 39:20 Yeah, and the other ones are, yeah.
Yeah.
Pardon.
**Tyler Yahn** 39:25 Yeah.
But again, like.
I'm fine if we want to put it in a dashboard, that's… that's… that sounds good to me, too. If you want to find a suggestion for that, like, I definitely would be up…
**Pellared** 39:38 I'll take a look.
**Tyler Yahn** 39:39 Welcome to updating it, yeah.
**Pellared** 39:41 I'll take a look.
**Tyler Yahn** 39:42 Yeah.
Cool.
It's also not, like… the end of the world for me if this PR just gets closed. Like, it's just a minor amount of noise. Like, I don't… It's just annoying. That's why I opened it, but it's not, like, I'm gonna quit the project.
**Pellared** 39:59 You'll need two like this, right? But you can have two peers like that.
Okay, yeah.
**Tyler Yahn** 40:08 Okay.
Cool. Last up on the agenda.
is the next release. So, I did want to ask a question on this one, like, what's… what are… what are we doing here? So, I think it's over a month, since our last release, I'm wondering if we've thought through what is needed here. The SDK observability is so close, there's, like, one PR, which I think actually is rating on my feedback on this one.
But what else are we waiting on here?
**David Ashpole** 40:44 My goodness, did that never get implemented? Okay, I will go ahead and implement the Prometheus one.
How are we on attribute types? I'm excited for that to land.
**Tyler Yahn** 40:55 I think we're done, actually. I think this can get closed.
Robert?
**Pellared** 41:02 I'm muted, sorry. The one which are here… the ones which are here, I think they can be moved out of scope. I don't think there's, you know, the duplication Should be really included here.
So, yeah, and we can move it out. Yeah, I will move it out and clean it up and close this one.
Cool. This will be not blocking the release, for sure.
**Tyler Yahn** 41:26 Do we have, log tracking issues that we were resolving here?
**Pellared** 41:33 It's already closed.
**Tyler Yahn** 41:34 Okay, cool.
**Pellared** 41:36 First one.
**David Ashpole** 41:37 Do we have, do we want to add deprecation warnings or anything to the old log types?
In this release.
**Pellared** 41:46 Removed because they're unusable.
**David Ashpole** 41:49 Okay, I mean, right, that's also fine.
**Tyler Yahn** 41:53 Yeah. Okay.
**Pellared** 41:55 What else?
We also make the resource… the resource PR on the go to country, or only on the main repo?
This uncond pump.
**Tyler Yahn** 42:10 Oh, I see what you're saying. So we release the new SEMCOM, we need to upgrade… update, contribib as well, is a blocker?
**David Ashpole** 42:19 Did we update?
**Pellared** 42:20 Yes.
Tyler.
**Tyler Yahn** 42:22 Yeah, yeah, core has been updated, yeah.
**David Ashpole** 42:25 Yeah.
**Tyler Yahn** 42:26 I, yeah, I totally forgot about that. Yeah, I can… I can tackle that then. Let me… Yeah, I totally forgot about that.
**David Ashpole** 42:38 you can move the Prometheus one to the next release, actually. Well, it depends on how much time. If it's, like, another week, then I can get it done, but…
**Tyler Yahn** 42:46 Oh, okay, it doesn't have to get done this release, though?
**David Ashpole** 42:49 I mean, it would be nice to have, but I haven't even started yet, so… And it's a feature, so…
**Tyler Yahn** 42:57 Yeah, okay.
What is that?
Okay, cool.
then I will… I'll keep it in here, but, it isn't… I think, like you're saying, it's not blocking, this release, so… And then this support HTTP JSON, I think that probably also… there looks like there's changes requested?
**Pellared** 43:33 I think I did.
**David Ashpole** 43:33 Oh no, okay.
**Tyler Yahn** 43:36 Well, huh.
It has two approvals, but these look really old. Oh, it's January 18th, yeah, this is really old.
Oh, I did it.
**Pellared** 43:49 There was also a second HTTP JSON, I'm not sure if it's by the same person, I think it is, or maybe this one, and also there were some comments which were just unresolved.
**Tyler Yahn** 44:01 Yeah, I thought it was, like, a trace one as well, or something like that, but.
**Pellared** 44:04 Yeah.
Okay. I'll see this today.
**Tyler Yahn** 44:10 I need to take another look at this, then. It looks like it's kind of waiting on me. Well, plus merge conflicts.
It's needed for the following?
Yeah, well, that's definitely gonna be needed for the following. Okay.
Yeah, I mean, I think it'd be great. I… I think it's, it's worth trying to get this in. I don't know if it's a blocker for this.
We only have 16 things done.
well, obviously we don't have 16 things done, there's probably a lot more. I just have to update the milestone. Okay.
I will also try to update the milestones with all the things that I've actually merged, so… Yeah, I was just kind of asking the question, I don't know if there's actually anything… outside of, I think, the attribute stuff, I'm pretty excited for that and the log stuff.
So I think that that kind of motivates, to me, getting this release prioritized, I know, an OB release is imminent… hopefully I'm trying to get it out tomorrow, so maybe this is a more of a next week thing for me, if it's gonna be me doing this. So, if there's another person that's really wanting to push this through, then… I think that maybe we could drop some things, but otherwise I could probably wait.
**David Ashpole** 45:23 Nope, no rush from me.
**Tyler Yahn** 45:24 Okay.
Okay, cool.
Alright, that looks like, the end of the written agenda. Any other topics folks wanted to talk about?
**Puneet Singh** 45:38 I just wanted to add one more thing. I'm falling on a spec… related implementation on the meter configurator, so this is for David. I created one initial approach, but that had a public API on the SDK, so that was… I mean, I understand that it is not considered a good approach, so I've added, followed another approach, which Kind of registers, callback within the meter provider.
And, advertised in the, in the, in the PR. So, David, whenever you have a time, have a look.
**David Ashpole** 46:19 Yep, yep. I saw your comment. I will definitely take a look. And just… like… I know Tyler commented on the tracer configurator one, so I just want to make sure that you know, like, this is an experimental feature in the spec. I would also say it's, like.
we haven't had any requests from users necessarily for it, so, if it turns out to be really hard, like, it's definitely not, like, I think a SIG priority or anything. But I'm happy to take a look at your changes, and I think… Like, in general, it's not a bad thing for us to have implementations of the in-development features so that we know what they'll look like if and when they land.
I don't know, Tyler or Robert, if you have different opinions about that.
**Tyler Yahn** 47:05 No, I'm not, like, opposed to getting shape and order and possibility.
Yeah, the configurator stuff, though, is a little bit of a thorn in the specification side. It's kind of… yeah. It's a duplication of ways to actually configure things, and it's a different worldview. It comes a lot from, like, the Java world.
I'm very… Hesitant, maybe even resistant to accepting that, for the trace, specifically, given we already have the similar configuration mechanisms, and, like, it just overloads and confuses, I think, users.
When you have two things, especially if they start fighting against each other, So, yeah, I, I'm not opposed to, like, PR showing, like, it's possible.
And you should not… not do these things.
if you're going to drive the stabilization of them in the specification, I will probably make sure that I ask for corrections, that these are not required things in the specification.
But they are not currently.
**Pellared** 48:12 It's world.
**Tyler Yahn** 48:13 Alright, thanks in the presentation.
**Pellared** 48:14 I think it's worth calling out, I think it landed in this pack.
I think we had, together with Tyler, we had a pushback to the spec that we want to call out that this functionality on the SDK is optional.
I'm not sure if it's there that it may provide, because we thought that, you know, the configuration stuff, which is done, you know, is an abstraction, then it could be implemented using the processors.
**Tyler Yahn** 48:40 Yeah, it's not explicitly called out as optional, but it also isn't, like, anything, explicitly called out as optional in the specification. It is experimental right now.
That's… that's why.
**Pellared** 48:52 Listen to…
**Tyler Yahn** 48:53 I only have so many hours in a day, kind of thing.
**Puneet Singh** 48:59 Well, I mean, it certainly was… maybe I'm doing it for first time, so it felt challenging trying to figure out that… how to work around this limit of experimental features, and not affect the stable side of the API and SDK, so… so, yeah. But, for me, it's hard to measure, you know, what is the relative The struggle of implementing such feature, actually, because I haven't implemented a lot.
**Tyler Yahn** 49:26 Yeah, you're not alone. That doesn't go away. Like, we have to be very careful, and I think that's just a part of the Go language, unfortunately. It's not like Java or Rust or something like that, where you can just kind of, like, annotate as you're going along, in, like, a particular package, so… Yeah, it's a… Yeah, you're not alone. It does take some thought and consideration.
**Puneet Singh** 49:51 Yeah, I think that was it from my side.
**Tyler Yahn** 49:54 Yeah.
**Pellared** 50:01 So, I think this was the language.
**David Ashpole** 50:08 I think updating is optional.
**Pellared** 50:11 I see.
**Tyler Yahn** 50:12 Yeah.
**David Ashpole** 50:12 That's always been the case.
It would be a required parameter.
**Pellared** 50:19 Okay.
Excellent speakers.
**Tyler Yahn** 50:27 Yeah, and I'm… I don't know. I'm not touching this until, like, there's a push to stabilize it, Because…
**David Ashpole** 50:33 You wouldn't, like, open up PR to remove it?
Just nothing.
**Tyler Yahn** 50:37 Well, I… like, I'm not… definitely, I don't want to remove it, like… .
**David Ashpole** 50:43 configurator?
**Tyler Yahn** 50:44 No, like, no, like, Java uses it. Like, I think that, like, having a specification for if you're gonna provide a configurator, what that looks like. I completely think that's valid. I think it's just, like, telling every SDK that they need to do configuration in this way is the incorrect, specification.
**David Ashpole** 51:05 I see.
**Tyler Yahn** 51:06 Yeah. Like, I definitely… no, I actually support, like, partial coverage at the specification, because, like, that's the problem, is, like, if Java does configuration with a configurator one way, and, like.
Python does it with the configurator in a slightly different way, like, that's way more of a problem, I think, than, than just not having any specification, would be. So, yeah.
Yeah, no, I like… I think that, like, having it specified is great, just saying that everyone has to use it is… A worldview that I don't share, yeah.
**Puneet Singh** 51:40 Mario?
**Tyler Yahn** 51:40 I mean, in this kind of… yeah, sorry, go ahead.
**Puneet Singh** 51:42 I was, like, I mean, slightly different, but I was, like, quite confused initially that what part of configuration this configurator represents versus what comes from the one that you used during initialization, and I just… I'm thinking right now that some text which could differentiate with these two would be helpful in the spec. I don't know what others feel about it.
**Tyler Yahn** 52:04 Well… That is a great question. So, maybe we don't… I don't think we have enough time to fully, like, get into this, but, like.
Since the beginning of, like, the tracer provider, there was always this question. In fact, like, the original Go prototype had a dynamic configuration update.
pipeline, where we would take a tracer provider, and we would take, like, the ability to do that. Like, we realized, like, it was way too complicated to try to, like, resolve these things dynamically, and, like, those exact questions of, like, who wins, and there's, like, race conditions and things, so we just said, like, you know what? Cut it out.
That's where the language that Robert was pointing out, where there's, like, it may dynamically update configuration, like, that has always been there, actually, in spec, like, since, like.
before the Sable release, even. It's just that we don't ever support that, like, because we were like, this is too complicated. And then for that exact reason, what you just described, we found that, like, actually, it's probably better if we don't, because users have a very deterministic view of what the tracer provider configuration is, if you have it from the start, right?
The only downside there is that there are things like enablement, which is what the configuration… the trace configuration is… the only thing that it configures right now is enablement, right? And that is problematic because, like, say you have a span processor that does not… it's not going to do anything with a particular pipeline of things, right? Like… or you have a backend that doesn't want any of this trace information, right? Like, you don't want your trace provider to be providing that anyways. Like, you don't… you really want to, like, optimize your tracing pipeline to say, like, hey, this is off.
do with that information what you will, is kind of the idea. And so what we've done is we've plumbed that back all the way through with this enable method, and so that's where that kind of comes in, right? So, like.
The tracer configurator does the same thing, like, you can just say, here's this, like.
this configuration, and you can look at that and say, like, hey, this is disabled by default, and you can do it from the top down. We've done it from, like, the back end up, essentially. Like, we've gone and said, like, hey, like, in our processing pipeline, we know this is to be true, so therefore, you know, expose it this way. The JavaSig was the other way. They were like, from the top down, go ahead and configure your observability.
From the tracer provider, and say, like, it's disabled this way. So… like, there's definitely… it comes back to this enablement, like, the idea then becomes, like, yeah, if you want to dynamically start setting things with your configuration, I think that that's… that becomes way more problematic. It doesn't exist right now, And I'm… I'm… I think it doesn't exist because of that exact reason that we were… we originally ripped it out. It's because there's just some super hard problems there, none of which that you probably aren't already seeing. Like, when you have config resolution.
what applies to a startup configuration? What applies to dynamic configuration? How do the… how do you merge them when they conflict? How do you deal with race conditions? Like, all these things, like… are just problems that we don't have. Like, we've just engineered away the problem by just saying, provide the thing, and if you want a different thing.
instantiate another thing, right?
So, yeah, I… I think from the specification point of view, like, that… yeah, I mean, if you wanted to go there, there isn't really a need right now, because the configuration and the configurator don't do anything besides enable.
like, that, that is done, pretty, pretty straightforward, right? But, like, the moment that changes, then, yeah, these are open questions. I would maybe talk to the JavaSig as well, because, like, if… they're the ones that use this. They're the ones that introduced it, they're the ones that have, like, strong opinions about it, and maybe they already have additional configuration there, and so they could have some prior art for you, but… Yeah, from the Go side of things, like, we've chosen not to do that.
With, like, as an explicit choice.
**Pellared** 55:41 I see that the locks.
**David Ashpole** 55:42 Sweet.
**Pellared** 55:43 There's also two more fields, which is immune severity, and trace-based, but all of the rest is just an A.
**Tyler Yahn** 55:49 That's true.
**Puneet Singh** 55:51 But yeah, thanks a lot, this is very useful info.
**Tyler Yahn** 56:00 Cool. Well, we're running up on the end of the hour here. Any other topics folks want to talk about?
Any cool projects people are working on?
Well, cool. Alright, if not, we can probably end the meeting earlier here.
It's good seeing y'all. I will see you all in a week's time, and otherwise stay synchronously. Till then, bye.
**Puneet Singh** 56:33 Who knows?
