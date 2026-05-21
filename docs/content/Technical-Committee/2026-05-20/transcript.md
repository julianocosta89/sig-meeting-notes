SIG: Technical Committee
Date: 2026-05-20
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**Armin (Dynatrace)** 00:16 Peter.
**Jack Berg** 00:19 Hey, Armin.
**Tigran Najaryan** 00:34 It goes…
**Armin (Dynatrace)** 01:04 Interesting, do you check, you just opened the spec inbox, right?
Do you get the same error message on top for an invalid label?
**Jack Berg** 01:17 But it doesn't seem to be actually invalid. I'm getting… I'm getting results, at least in the community inbox.
And it's the same type of filter warning.
I don't know what that's all about.
**Armin (Dynatrace)** 01:33 Yeah, even if I follow the UI built-in link, so not typing in the query myself, but clicking the link, it shows the same message, so maybe just some hiccup.
Alright, so spec inbox is empty, and community, I know that we should have at least one.
Right, the other one, from the… the… Person did recently.
surface deal… I put that one in there.
Community.
**Jack Berg** 02:24 I'm asynchronously assigning unassigned spec issues right now.
For ones that are uncontroversial.
**Tigran Najaryan** 02:32 I think we should discuss the 3435.
I have doubts that… That's a good project proposal, unless… It's led by a TC or a GC member.
And, the current proposal is that it is not led by a TC or GC member.
**Armin (Dynatrace)** 03:02 I haven't followed up on the latest there. Have they requested one, actually?
Will be confirmed during…
**Tigran Najaryan** 03:16 Can we do the other one and wait for more people to join before we discuss that? Because I think that one is probably important.
**Armin (Dynatrace)** 03:23 Yeah, that makes sense.
**Tigran Najaryan** 03:25 We can look at, Ted's, open issue person.
**Armin (Dynatrace)** 03:30 I think that one is…
**Tigran Najaryan** 03:31 That's one. Yeah.
**Armin (Dynatrace)** 03:33 I put that one first, then.
**Tigran Najaryan** 03:44 He talked about it yesterday, right? That's the same one, the same issue that he was presenting yesterday.
**Armin (Dynatrace)** 03:50 Yeah.
And I don't see any GC engagement on it yet.
Maybe I… but I think they have their meeting on Wednesdays as well, right? So maybe they will discuss it right today.
So far, it's just… situa and Tigran on it, I think.
**Tigran Najaryan** 04:20 Yeah, I just made a superficial comment, doesn't really matter that much. I'm not seeing the… this is, this is formulated as an… is this a project, right? This is not an OTAP.
**Armin (Dynatrace)** 04:32 It's not.
**Tigran Najaryan** 04:33 the stuffing, yeah. Is there a staffing section here? There's supposed to be, right?
There is no starting section.
**Armin (Dynatrace)** 04:42 There would be one in the template, I…
**Tigran Najaryan** 04:45 Yeah, there isn't anything in the text, but I'm not seeing anything.
**Armin (Dynatrace)** 04:50 It's not really following the template.
**Tigran Najaryan** 04:55 Okay. I would expect it to be there at some point, like, supposedly Ted is going to lead it, but he doesn't say anything about leading, or who is going to be contributing, or anything like that, so we should… We can either wait for the GC to chime in, or we can maybe begin Asking those questions there.
the… I guess the general sentiment seems to be, after the discussions we had for so long, is that since Ted is going to lead it, we seem to be okay with the project. Is that the consensus, or people have different opinions on this?
**Armin (Dynatrace)** 05:38 Yeah, when it was brought up yesterday, I did not… find any… any dissent there, or no dissenting statements were voiced, but I also don't know If all the maintainers were exactly clear on… on what's… Coming on to them and what it means for them.
It might need some more time. I think that's…
**Tigran Najaryan** 06:00 That is to be defined yet, right? That's not yet clearly known. That is work… for this project.
To define what exactly the… It's not stable anymore, it's called general availability. What does that mean?
This is just, maybe, kind of.
What we have in this proposal is essentially the concepts, the idea, but not specifically what exactly they are aiming for.
And that's okay, right? They can go and define it.
But I still would like to see… Maybe some stuffing listed here, who is doing what.
what is the… I also don't see the… any timelines, as far as I can tell.
Yeah, I don't see the timelines either.
So.
We can either wait for the GC to chime in, or we can do it in parallel. I think it's okay if we do it in parallel.
And I can ask those questions there.
**Jack Berg** 07:03 I think better to start early and stay on top of it, given the recent feedback we've had with other project proposals. Communicate… over-communication is preferable, I think.
**Armin (Dynatrace)** 07:15 Yeah.
**Tigran Najaryan** 07:19 I guess most importantly, we do not think that we should be blocking this or objecting, or anything like that. That's the thing that probably is the important decision we need to make here.
**Armin (Dynatrace)** 07:31 Yeah, I think to some extent it also stems from, the CNCF Technical Oversight Committee.
Requests or suggestions to… After, like, independent of the… of the maturity process, independent of the gradation, to catch up on that.
That's the next step.
**Tigran Najaryan** 07:53 So this must be done, essentially. It's not much of a choice, I guess. It has to be done. We need to find ways to do it.
Okay.
**Armin (Dynatrace)** 08:05 call it a non-blocking recommendation, but of course, it's there for a reason.
**Tigran Najaryan** 08:11 I think it also makes sense, right, independently from that even, right? So… I personally think this is a good idea.
We just need to find The right way to do it, the staffing, who's leading it, what the work streams are, and etc, all of that, right?
So, shall we maybe, I guess, people can… review it. We don't have to do it right now, and comment on it. Is that a good way to move forward with this one?
**Jack Berg** 08:46 I just want to make one comment to us here. So, like, the… the TOC, you know, has a comment, this non-blocking comment that says, like, hey, you know, it's not blocking, but the OpenTelemetry should seek to complete this stable by default OTEP that Austin opened.
And that's getting closed, and this is sort of the replacement. But, you know, with each sort of step, it's like a game of telephone, and information and, like, original intent is, like, lost or changed a little bit. And, like, let's go back to the TOC's actual recommendations of what they want.
or what they recommended, and make sure that that's reflected in here, because I'm noticing a few things that are, like, changed from the OTEP, for example, and aren't included in the TOC's recommendations. The TOC is focusing on things like You know, standard metadata for indicating whether something is stable or experimental. Mandatory programmatic barrier for opting into experimental features. Formalized contrib versus core.
Those are the things that it focuses on, and in this project proposal, I'm seeing things like OpAmp 1.0 and Packaging 1.0, and packaging was, like, just something that came onto our radar, like, weeks ago, and so I'm… I just want to make sure that, you know.
We're not losing sight of the original ask too much in this.
**Tigran Najaryan** 10:18 Yeah, sounds good. And like you said, project… what is it? A packaging project is just a new thing. Seems like a scope crypt to me.
We don't necessarily have to add that here.
**Armin (Dynatrace)** 10:33 Is that one in… in the current GA proposal?
**Jack Berg** 10:38 Yes.
**Tigran Najaryan** 10:39 Is there a list of work streams, like, if you look at it, yeah, it includes op-amp packaging, operator, all the stuff there.
**Armin (Dynatrace)** 10:46 1.0, I believe that yesterday, when they presented their timeline for packaging, they said that By the end of the calendar year, they want to have an idea of where they want to go, and they will report back on a quarterly base, so I think the… the timeline there will Will, like, spread way.
Way out, right?
So if that was part of the scope, then this would be, I don't know, 2028?
2029 proposal.
Not sure if that's the intent there, actually.
Riley?
**Reiley** 11:27 Well, slightly, unrelated to what you were talking about, Henry. So I remember, like, Jack probably mentioned, like, we should just GA once instead of, like, we keep GA, like, every month or something.
So, I searched the Kubernetes, and their GA is… on individual features. They will announce this feature is GA and be done with it. They will never come back and say this feature will GA again. When I look at the PR from TED, I'm very confused, because it sounds like we're trying to put OpenTelemetry as an entire thing GA. That reminds me, like, what do we do when we call Kubernetes GA?
I don't think that's the right approach, so I have this semantic concern. I'm not sure what's the right forum to discuss that.
I'm done.
**Jack Berg** 12:18 Yeah, and just, like, I would have… I think we've previously essentially said that open telemetry has GA'd at different points. You know, originally it was when tracing first went stable. It's like, that was the GA. And then it was when we had all three signals stable. That was the GA. And I think OTLP, when that went stable, that was the GA. It's like, we're moving the goalposts on ourselves.
Definitely.
**Reiley** 12:44 And it's really confusing. I think we're trying to invent a lot of new terms, and also the version is very concerning. I know there are components which are already at 2.0. When we talk about 1.0, I think it's super confusing, and I'm afraid that we're going to make the situation even worse.
But I don't want to be a jerk and block that PR or anything. I just have this general concern.
**Jack Berg** 13:08 I think it's fine to hold it to, like, a high standard, that the language should be precise, that the versioning schemes that are mentioned there shouldn't be, like, conflict with things that are there. I think we struggled with the prior PR, the OTEP, In part because, Austin was struggling to find capacity to actually work and drive that. If Ted is work… is working on driving this, then, you know, he has to be responsive to comments that are reasonable requests, so…
**Reiley** 13:37 Okay.
Thank you.
**Armin (Dynatrace)** 13:46 Alright, so the next steps there are PR review by us, discussions by the GC probably today in that GC meeting, and then we'll regroup in two weeks in the GCTC meeting anyway, where we will most likely tackle that as well, right?
As this seems to be primarily also coming from the GC.
Any further comments on this topic, or should we move on?
We don't have too many things on the agenda, so we can also spend some more time on that one, if you please.
Alright, then, let's move on with the next one. I think, Tigran, you wanted to discuss that one in a bit more depth, right?
**Tigran Najaryan** 14:45 Yeah, this one is, proposing a maturity model.
or, for any software, I guess.
at how well it meets the maturity from OpenTelemetry perspective.
And they're suggesting some dimensions there, like instrumented.
aligned with OpenTelemetry, or whether it's native OpenTelemetry, optimized for it, at least in four levels here.
The concern I have here is that they are… they're saying explicitly this is not a certification initiative, this is not Trying to, label things in a way that ranks the, I guess, the technology, I think it inevitably is going to do that. There's no way around that. You're defining certain standards, you're publishing your opinion about how Other software meets those definitions.
it sort of is going to end up some sort of a publicly visible ranking for… for others to align with. And I think there's a danger for this to become Opinionated, and not necessarily in a good way.
So, while I think it may be a good thing to have something like this for the end users of a particular software to make a decision about, look at it, and how well it supports OpenTelemetry, so the intent I think it's a good intent there, right? Execution, I think, is going to be… They may be controversial, right? So I would be reluctant With having this being executed by by… a non-TC or non-GC member, let me say it this way, because I think this is… There's all those dangers there, right? So… I would suggest that if we want to go ahead with something like this, that there is a lead from a TC or a GC.
That's all I have.
**lmolkova** 17:07 I'm curious why, why is it not part of end-user SIG?
It sounds like something that can be a sub-seq project. Does it need to be its own project?
**Jack Berg** 17:24 A good call out.
**Tigran Najaryan** 17:27 It could be.
And it doesn't really matter where exactly it is. I don't like the idea of us labeling others arbitrarily. It doesn't seem like a generally nice thing to do.
what's the… I guess if… unless it's formally, like.
specified somehow, you… you have a An actual code that runs and says, Here's the compliance… Findings from your software.
there's a test suite, right? We're testing your software against it.
Which would be sort of objective.
But… this is not bad, right? They are suggesting that the labels will be… who's going to choose the labels? Who is going to decide whether this particular software is at level 0, or 01, or 3, or… who's doing that?
And why are we deciding that that's a good idea for us to label others?
Anyway, I have concerns with the whole idea of us doing that, to be honest.
**Carlos Alberto Cortez** 18:36 But if I may say so, I think that this is something that the GC can probably, you know, provide feedback on, because I think it's not only technical, as you said, it's, like, we allowing other people to put labels.
Sorry, we're putting labels on other people's, you know, stuff, and probably this is… this requires some GC involvement, or feedback.
**Tigran Najaryan** 18:59 That's the thing, right? We're going, essentially, to label someone else in a particular way, and you're opening up a possibility for disputes and discussions, and they will come and say, why did you label me this way and not that way? I'm actually doing this and not that.
do we really need that? I mean, what's… I don't like it anyway, so I'll shut up now.
**Jack Berg** 19:22 I agree with you, Tigrin. Like, if you leave a comment to that effect, I definitely support it. I can't articulate it as well as you just did. I haven't read this proposal deeply, but, like, you know, my reaction is that I agree.
**Josh Suereth** 19:41 It was like… Oh, go ahead.
**lmolkova** 19:44 And just a quick thought that we were… going… we are doing some conformance, and there are some objective criterias that will exist from semantic conventions. If we will become more friendly with instrumentation Square, we can use their criterias as well. So we are going to put objective labels, and this is a big part of The scope of this proposal.
**Tigran Najaryan** 20:11 That would be a good one, by the way, Ludmila, if we can actually… if there's an output that is automatically evaluated and assessed by Weaver, let's say, right? It says there's conformance with semantic conventions or non-conformance, that I can understand.
Right? But this is suggesting a lot of subjective evaluations about what is happening there. That's the part that I don't like.
**Josh Suereth** 20:34 Yeah, I think we should push on getting rid of subjective, but I think there is a real problem this is solving, right? So problem number one is people say they're OpenTelemetry compatible.
And what they mean is they send OTLP, right? But sometimes the OTLP they send is degenerate. It literally won't… like, if you use the OpenTelemetry data model, their OTLP won't work. That's like what happened with FluentBit. When they first supported OTLP, they ignored half of our spec and just weren't filling out resource, ever.
And so, you got, like, degenerate data that would actually break an open telemetry ecosystems. I don't know how… like, that's a hard line to say, but I would say, like, we have a maturity model, we know there's two things that we have. One is, do you just write the protocol? Can we change it, send it around, right?
There's this subjective thing of, you know, will the default exporters and processors and things in the collector work with your data?
That's… that's… I don't know, like, there is an objective thing we could make for that, but that's like, you know, if you don't work with our batch processor because you're filling out OTLP in a horrible way.
Are you really?
open telemetry friendly? Like, that would be question number one. But then the second part is now, we have this notion of semantic conventions, which is like a higher level conformance of not only do I instrument and I can send you the data, but your system can interpret my data because I'm using the same names and words Right, that OpenTelemetry has. So I actually think, like, the way I would phrase this would be, let's get concrete measurements. Like, I speak OTLP, and that OTLP is usable in the ecosystem. Great. That's one.
Two should be, I use schema URL. I might not use semantic conventions, but I use schema URL, and you can validate it, you can see what the hell I'm sending you.
Right? Number 3 would be, I'm using semantic conventions. And I don't know what number 4 is, I actually don't care. But right now, we're building number 3, And a compliance test around number 3, number one is the thing that I think we… we could make something legit here. Like, we… I think we could, but your point is 100% valid of, like, let's remove subjectivity from it.
The question that's being answered, though, is the important part to me, of, like, if you send me OTLP, can I even use it as a system? Are, like, will the interact with you.
**Tigran Najaryan** 22:51 Yeah, what you described.
I'm on board with that completely. I would want that, right? So, because that can be automated, I can have the software run, or the payload evaluated, and there's no subjective element in that, right? So it will give you exact results.
And I don't think we even need to publish the results. We need to give the evaluation tool to everybody. They can run it themselves. Why do we want to go into that area of, oh, I'm publishing the results, and somebody comes and complains you did the verification incorrectly? Do we even need that fight?
Yeah, Jack, go ahead.
**Jack Berg** 23:29 So the… one thing that strikes me is, Josh, all the examples that you gave of being able to have deterministic verifications are all about OTLP sources, not OTLP destinations.
Right? Like, how do you… how do you say that… how do you verify that, like, a vendor that accepts native OTLP, first of all, accepts it, and not just 200, but, like, puts it in a database somewhere such that it can be retrieved without being, like, mangled? What's the definition of that?
And, like, how do you… how do you, like, verify that they do things, you know, with semantic conventions? Like, these are all platform-level choices, and I think… I think they're part of this conversation, and part of what vendors are trying to do when they say, like, hey, we're open telemetry friendly, they're making, like, assertions about how their platform accepts OTLP data and what it does with that, and that just seems like a black hole of subjectivity.
**Tigran Najaryan** 24:27 And I think we shouldn't even be in the business of verifying that. That's not… that's not our job.
We can at most be in the business of defining the criteria and leave it at that.
the vendors can self-evaluate, or whatever they want to do. I don't want to go there and begin very validating vendor implementations and publishing results, and then going into fights with vendors because the evaluation was done incorrectly, in their opinion.
**Josh Suereth** 24:55 I'll add one caveat, okay? So, I agree with you, Jack, that, like, that is a line we don't want to cross. However, if the vendor's re-exporting OTLP, and they do it in a way that they're breaking all of our conventions and forcing people to match whatever the hell they're doing with that export. That… that is… that is, like, ecosystem breaking, but again, we should be able to validate that. So, like, so, like, if we consider our bounds, OTLP, And we say, are you sending OTLP that works with the ecosystem?
Are you sending an OTLP that matches our conventions? Like, I think that's how we would define our maturity layer. And if your vendor takes something in and sends something out, and the thing that comes out doesn't match conventions.
we can score that, but we wouldn't be like, oh, do you support SQL against OpenTelem? Like, we're not there. We've never been there, we have explicitly excluded that, and I agree, that should not be part of anything we do.
**lmolkova** 25:53 I actually read this proposal initially as targeted for us to, like, to evaluate our components.
And a conformance program we would have would start with open telemetry instrumentations. I also read that there's something very similar to stable by default, where we apply this maturity model to ourselves first.
would this proposal make sense if it's scoped down to just open telemetry things, and it evaluates open telemetry things as such, and maturity of the SDKs and instrumentations and country, and whatnot?
**Tigran Najaryan** 26:32 I'm, by the way, totally fine with us evaluating ourselves. That's fine, we can do that. I just won't want to extend it to others, to third parties, where it can become really messy. But the proposal includes exactly that, right? It's not just about us. If you read it, like, I'm… copy-pasting sentence from there.
against real projects by applying to cloud-native projects, other cloud-native projects, right? Ingress controllers, etc, etc. That's the piece that I think can become messy.
**lmolkova** 27:07 Yeah, it's… it's on me. It's just Amy's right, yeah, thanks.
**Jack Berg** 27:11 Honestly, there's a lot of words in this proposal, and I don't think it needs half as many words. Like, I'm reading that sentence you posted here, Tigran, and I don't know what they mean by it.
**Tigran Najaryan** 27:24 what they are saying is they are going to take some other software, ingress control fairness meshes, like Istios and stuff like that, right, and begin evaluating them against that model, how well it confirms to our definition of open telemetry-ness.
Whatever that means. And then we're going to publish those results somewhere, if I understand correctly.
That becomes visible.
And I don't like the entirety of it, to be honest.
doing it to our own SDKs and languages, I'm fine with that. I don't have a problem with that, right?
And the maintainers should be doing that, again. Not the TC, not the GC, we can give them the tooling.
Weaver or other tool like that will be there for maintainers to evaluate their implementations. That's great, right? We can have that. Evaluating other projects in CNCF, or evaluating vendors, I don't like that part.
**Jack Berg** 28:33 Do we want to leave a comment on this project proposal?
**Tigran Najaryan** 28:38 Yeah, I think, yeah, I'm happy to do that.
Or maybe, I don't think if GC had a chance to look at it.
I don't see any… any comments from the GC members.
**Carlos Alberto Cortez** 28:53 Oh, probably we should mention that to them, or put that even in their agenda.
Or something like that, yeah.
**Tigran Najaryan** 29:01 Okay.
I can make a comment, tell what my opinion there is.
I'm fine with that.
**Jack Berg** 29:10 Thanks for doing that.
**Tigran Najaryan** 29:13 Okay.
**Jack Berg** 29:18 The next topic, proto-maintainers. That's you, Josh, right?
**Josh Suereth** 29:25 Yeah, as you know, I'm planning to step down, but I would like to still be a proto-maintainer.
And I'm actually thinking about, when I don't have to attend this meeting, spending those hours doing proto-maintenance. If you remember, I did a triage a while ago. There's a ton of low-hanging fruit.
In the protorepo that is just annoying work that has to be done. Need to rebuild the frickin' Docker image that builds all the C++ painful, hellish crap.
For Proto. I'd like to spend time on that. So, this is just a, hey, before I leave, could we set up a proto-maintainers list of who's gonna be Proto Maintainers, and can I be on it? If not, I'm still gonna do the work, just I'll be annoying you guys.
**Tigran Najaryan** 30:08 We have the product maintainers, team, and you're on it, I think, from what I see.
We should also make you a spec sponsor, so you have the spec approval rights and all of that, if you're not already.
**Josh Suereth** 30:21 Yeah, I'm planning… I'm planning to send all those PRs probably next week, of, like, removing myself from the TC and moving me to wherever you guys want for approval, so…
**Tigran Najaryan** 30:32 Yeah.
**Josh Suereth** 30:33 With Protos, like, are we officially having a separate proto-maintainers? If you look at the Proto repo.
I don't think, let me take a look. I don't think…
**Tigran Najaryan** 30:44 I can see the team, the team is there. There's a team called Proto Maintainer.
**Josh Suereth** 30:47 I know.
**Tigran Najaryan** 30:48 Sign it.
**Josh Suereth** 30:49 I didn't finish the work. Are you guys comfortable if I finish the work of making proto-maintainers? We don't call it out right now, and the maintainers list… I can show this.
If you look at the Proto Repo.
**Reiley** 31:02 shared a link.
**Josh Suereth** 31:04 What?
**Reiley** 31:05 I shared a link in the chat. Okay, so we already have the maintenance group, we just need to update the README file and clean up the group.
**Josh Suereth** 31:14 with that.
if you're comfortable with that, I can start pushing those changes before I step down. I just wanted to make sure that we're… again, like, I don't want to be that lame duck, you know, do a whole bunch of things and leave the TC. I just want to make sure we're all okay with this. Okay, cool. Awesome.
**Jack Berg** 31:33 Is there anybody else that would be a good candidate to invite to proto-maintainers outside of the TC?
**Josh Suereth** 31:40 Yeah, I'm actually thinking, some of the profiler group that actually spent a lot of time doing… like, they now know the care that we take with the pro… with the protocol, they've done a lot of evaluation on things, like, I think it might be useful to pick one or two. Tigran, I don't know if you have, Anyone in, like, specifically you're thinking of, but there's two in my mind.
That we could at least… like, if not add them now, we could, have them in a queue that we could pull them in.
**Tigran Najaryan** 32:09 We could add people from profiling. Also, Robert may be a good candidate. He has done… some amount of work recently, he has PRs there.
In the pro.
**Jack Berg** 32:21 Yeah, I just… I just suggested that because I think it would be good to further, sort of, decouple proto-maintenance from the TC, and Josh is one example, and if there was another, that would be good as well. And on that same front, if there's anybody on the TC that isn't interested, or doesn't feel like they, you know, they, you know, are sufficiently engaged with Protos to be a maintainer, we could step down as well.
**Reiley** 32:49 Yeah, Jack, you noted. I suggest that when we start the maintainers group.
we assume that you only want to be there if you explicitly ask for it. For example, like, I inherited late, I got put there, but I don't feel I've ever done any significant work on the protocol itself.
So, it's a shame for me to be there. I should be removed. And that will also send a great signal that we're opening up opportunities for others.
**Jack Berg** 33:18 So, Josh, do you want to open up an issue like that, that says, like, hey, you know, create a new dedicated maintainers group that isn't purely seated by the TC, and, you know, use that to explicitly list every TC member and require them to opt in to being a proto-maintainer?
**Josh Suereth** 33:35 Yes, yes, I will do that, and then, I'm actually thinking, if you look just at contributions, we have opportunities here, but, Florian's the one who I was thinking about from profiling, by the way.
We also have, and I don't think, this is, armin, Alexi, but I don't… like, I can talk to Alexi, because I work with him, but I don't think he has enough time, so I don't think he would be interested. And then Robert is on here. I don't know if we want to talk to Emily S, I don't know if she's still, working on things, like, like with the pro… No, I don't think so. Yeah, okay. That's kind of what I thought. But yeah, like, I think the folks not on the TC in this list we can reach out to. Sergey has moved on, as you know, he's, he's working on something where he's not gonna have time, but… I can reach out to those folks and see if any of those are interested as well, and I'll open the issue, and yeah, TC can opt themselves in.
Sound good?
**Tigran Najaryan** 34:33 I think, I think realistically, it's going to be Florian and, and Robert, I think.
**Josh Suereth** 34:39 Yep.
That makes sense to me, yep.
**Tigran Najaryan** 34:41 Yeah, yeah.
**Josh Suereth** 34:42 Cool.
Awesome. I have a private topic next. Apparently, we have lots of private to… oh man, all the private topics. Alright, should we switch to the private room?
**Tigran Najaryan** 34:55 Yeah. See ya.
**Jack Berg** 34:56 over there.
