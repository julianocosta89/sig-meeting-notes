SIG: Specification SIG
Date: 2026-04-21
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

Reiley 00:00:25 era.
jmacdonald 00:02:03 We have way too much on the agenda today.
And I am going to propose shortening the 20-minute OBI updates, just for the record.
Okay, people, we're… we're two, three minutes in. I'm gonna keep waiting. I will run this meeting.
We are going to start by talking about stable by default, just so you're all ready for that. I would like you to have your… comments prepared, I suppose.
However.
I note that it's just a standing reservation. Someone's gonna have to remember where we were last week, if they'd like to continue stable by default.
And in the minute that I have, I'm gonna figure out who has an interest in speaking first.
Carlos Alberto Cortez 00:04:14 I think Robert had a few comments that were not resolved, and they are still not resolved, so Robert, you're around.
jmacdonald 00:04:22 I'll see Robert in a moment.
Pellared 00:04:25 below.
I'm not sure if there's anything that I want to add, apart from the stuff that I mentioned, so someone can take over.
I don't know if Teddy's here or not.
jmacdonald 00:04:39 Let me pull up the PR, so we can look at what…
Pellared 00:04:44 Add it here, okay?
jmacdonald 00:04:48 Pr was 4318… I'm coming.
Josh has a hand up. Alright, well, we're gonna start this meeting right now. Go ahead, Josh.
Josh Suereth 00:05:06 I'll make… I'll make a comment about stable by default. So if you look at… if you look at the PR, At the time, one of the reasons, like, I myself am uncomfortable merging it, even though I think it has enough approvals to merge. Robert blocked it, but I also don't see… Maintainer approvals here.
And so that's why we wanted to talk about it in this meeting, is to try to understand, like, is it a, You know, I think, like, Robert, thank you for being honest about, like, I agree with the direction, I think some of the specifics aren't good. That, I think, has been the feedback on this PR overall.
And I made the same comments myself.
And I think, like, from my standpoint, it started to address them, and I approve it now. But, like, from my perspective, the thing I want to see is just, are the maintainers of OTEL comfortable with this direction, and where we're going?
And I think maybe, like, we need to work on the OTEP possibly to remove details out that are not directional, because this is meant to be the directional OTEP, that we all agree we're moving this direction so we can start moving forward.
But the lack of maintainer approval is the thing that, that, like, I wanted to kind of dig into in this meeting, if maintainers are comfortable expressing their concerns, and are comfortable expressing, like, what they're worried about with us.
Pellared 00:06:27 So maybe just to probably say the second time, like, Josh, exactly what you told. I'm not against the idea of working, you know, stabilizing things, making, and stabilizing in a very broad word of what stabilization means. I was just not… I was just finding that some of the things, what was written in OTEP was too much, like, I need to drop. I have a phone, it's important. Sorry, but the thing is that it was… it was suggesting already some implementation, which I didn't… I was not sure about.
And there was not, like, context info, end user information, services, stuff like that, but the direction, I totally agree with it. Okay, I need to draw for a second.
jmacdonald 00:07:20 Did Robert just drop off the call?
Josh Suereth 00:07:23 He had to take a phone call, I don't know if you heard the phone in the background of his…
jmacdonald 00:07:27 I… somehow I didn't, Well, we're looking at his remark right here, and he was sort of saying, something. Josh, I'm handing it back to you.
Josh Suereth 00:07:40 Okay, cool. So yeah, if you read Robert's remark, I think this is… this is what a lot of us thought when we first read it, was like, agree with the direction, but there's a lot of specifics in here, and we need to get the specifics sorted out. And so, if you re-read the OTEP, though, with a, here's the direction.
and here's a set of projects that will need to figure out the details, I think that it reads a bit differently. And that's kind of, I think, the intention of this OTEP now.
But what I wanted to make sure of is, again.
the OTEP is only going to be successful if the community is behind it, and I… I don't see many maintainers… actually, I don't see any… like, outside of TCGC, I don't see, maintainer approvals on this.
So that's why I just wanted to take a little bit of time in this meeting to see if folks wanted to escalate, like, maybe things they're not voiced, or things they felt were already commented but not addressed. Like, what do we see? You know, what would it take to… have folks actually approve this PR? Is it that there's too much detail and not enough room for the areas to be explored? Like, what, you know.
what would you want to see here? And I just want to hear from, you know, thank you, Robert, you're a guinea pig, because you actually made a comment, and so we're picking on you. But, like, any maintainer at all that wants to raise, like, hey, here's the concerns I have, here's why I haven't approved it, that's kind of what I'm looking for.
Just, again.
part of that's for me personally, like, I would be uncomfortable merging this with zero maintainer approvers on it, you know what I mean?
jmacdonald 00:09:11 Thank you. I know what you mean.
Robert's back. Maybe, Robert, you'd like to continue.
Pellared 00:09:19 I can continue for a sec. So, I think… this is my perspective, but I think it could be shared with others.
I think that, They think of the tension, maybe because the maintainers are aware how hard and how much responsibility is making something stable.
And, like, personally, me as a maintainer, I'm scientist, I'm angry how many things are getting to specification, and how much there is going in open telemetry, because as maintainers, we are not able to keep up.
And, and I think end users are angry about it, because there's so many stuff in specific areas, so many things on the fly, and we are just not able to keep up, and maybe that's the reason that maybe this, like.
stable by default.
like… it will be not making anything, like, by default, you know? It's kind of… maybe the term is kind of, you know, kind of also scary for us.
It's… I want to say that I think most of the maintainers are probably looking and work hard on stabilizing things, but it's just freaking hard, and yeah, that's my take on here.
jmacdonald 00:10:37 Figuring.
Tigran Najaryan 00:10:40 Yeah.
So… I guess what I'm gonna say is gonna be a bit meta.
This… this proposal, when I read it, it requires a lot of work during a prolonged period of time by many SIGs.
And… I guess one of the ways I think these types of projects.
Can be successful is… By having a leader who owns it long-term.
who can campaign for the project, go and speak to the SIGs.
Make sure that they are both in, they are aligned.
They are on board with the idea.
And then relentlessly pursue the execution of it for… For many, many months.
Unfortunately, I'm not seeing that person right now, and I'm not seeing that campaign happening.
And that explains why we do not see maintainer feedback on the OTEP, in my opinion.
There's probably other ways this project can be successful, that what I'm describing is just one possible approach.
But… I'm not sure I've seen… A systematic way to try to… To make sure that this is a successful proposal.
So, I'm not commenting on the specific ideas proposed here, so I do agree with many of the things that these are good things to do.
I'm just not seeing how these are going to happen.
And that, in my mind, is a problem. Merging the OTAP is not going to solve that.
jmacdonald 00:12:25 Fair point. Josh.
Josh Suereth 00:12:27 Yeah, I think that's well said, Tigran. So, I have… I have a question about that. Like, we are starting on this, federated SEMCOM thing.
Which is motivated by the idea of stable by default, and we think is going to independently be a good idea and, like, you know, improve velocity for SEMCOMF.
And that's something that, you know, Lyudmila, Trask, myself, SemConf maintainers, Weaver maintainers, we're pushing on that, and we're looking for support from the ecosystem on it. Do you think that work is blocked, and those OTEPs are blocked by the stable by default, or, like, should we just keep making progress? Like, my opinion is we should just keep making progress on that.
independently.
Tigran Najaryan 00:13:05 I think that's fine, that's totally fine, and if there is individual pieces of this OTAP that There's a person willing to lead.
They are passionate about. They want to do that part.
There's nothing wrong with that. I think that's the good thing. It should move ahead. The whole thing… I think there's… if we want the whole thing to be successful, there needs to be that one person who is… taking the lead on it. I'm… I'm not seeing that person at the moment.
So, a possible approach forward could be kind of what you were describing, Josh, that there's a portion of it Where people are already interested in, they… there's a person who's leading it, sure, yeah, let's make it happen.
It doesn't necessarily mean that we have to… we can merge the OTAP, I don't think it makes a whole lot of a difference there, right? Or we could split it up into separate OTAPs, where we do have that, like, in the same comp, we have that Readership and the alignment of the participants to move forward.
jmacdonald 00:14:26 Oh, a hand went up and down. Well, I won't call on someone whose hand's not up.
I would make my own remark on this topic, for me, you know, thinking with my maintainer's cap on, which I don't have a language SIG maintainership right now, but I have in the past, and I've done this work, I don't feel confident that I know what I would do in my own languages to get through a migration of this sort. I don't think that we have a story yet.
I'm looking at metrics in particular, you know, I… I've… we've all been involved in code projects that kind of spawn up from nothing, and then, like, a lot of code gets written, and then, like, a lot more code gets written, and then suddenly you look at your instrumentation, and it's like, oh, this is not right, this is not good. How do I get from version 0 to version 1 of my own instrumentation? And I don't think I have the answer, even in the code that I'm super comfortable with. I just don't think we've done that. And so we have metric views, but I don't know how to use them to get from version 0 to version 1, or whatever it is. So I don't truly believe we've solved the stability problem.
and I think maybe I'm just agreeing with Tigran, like, this needs leadership in a… and there are technical problems ahead, as well, is my opinion.
And I think that we should do them, but it's a matter of… the time and the pressures that we have. So, as just an example, to tease you all, I'm in the Otel Arrow repo, we are looking at exactly the disaster I just described. We have a lot of code, a lot of new instrumentation, it's not good instrumentation yet. It's not… but if I start breaking it, I am… I am… earning stability for the people that are starting to use it, including my own company, you know, essentially. So, like, I already have a stability problem. Brand new codebase, I have a stability problem, and I don't know what to do about it. I am starting to think about it. I think Federated SEMCON will help us, but I also think we need some sort of you know, major initiative for the SDKs to help the instrumenters understand what they need to do, I don't think we've done it yet.
That was my remark. If anyone else has a comment on this one, we may continue.
Kayla Reopelle 00:16:40 Just one small thing. I knew a discussion about stable by default was happening during the discussions in this meeting, but I wasn't aware that this document existed.
Or if I was, I forgot about it a long time ago. So, I might recommend, like, posting it in the maintainers channel and asking people for review, or possibly, like, tagging maintainers, you know, like, the groups of maintainers and their GitHub handles to try to get more feedback with, like.
Perhaps even, like, a deadline or a goal of when you're hoping to merge it by, so that people can prioritize it.
Tigran Najaryan 00:17:14 And that's indicative of what I was talking about. There needs to be a campaign.
To begin with, right? So, whoever is leading the project has to go and talk to people, to all the maintainers, make sure that they are aware.
But they provide feedback.
There are parts they disagree with. There needs to be an iteration of what this looks like. We need to come up with more details, because this is very high level, in my opinion, and not directly actionable.
This is a lot of work, really, that needs to happen there, and I don't see who is doing that work at the moment.
jmacdonald 00:17:56 It's curious that Austin is not here. I wish he were, because he's the one who was pushing this as, as well. I guess he is sort of hoping to find another leader for this, effort.
And… My position, I guess, is that we don't quite have the… the lead yet. No one has a lead on this.
Tigran Najaryan 00:18:15 Yeah, yeah, just to be clear, I wasn't criticizing Austin. My understanding was that, indeed, he didn't think he has time to do this himself.
I may be wrong, last time we talked, I think that was… that was… he was… what he was saying, that he won't be able to lead it himself.
Correct me if I'm wrong.
jmacdonald 00:18:39 I think that's fair. I don't think we should lean on Austin for this.
My best answer goes back to what Josh was saying about federated SEMConf. I… I, I strongly believe that that is the path forward.
For any…
Trask Stalnaker 00:18:55 Ted's… Ted's, I think we don't have the Grafana folks this week, or some of them, because of their conference, but, I know Ted was starting to get engaged in this, so it's probably worth Raising next week, when Ted's back.
Tigrin, I think your, concerns were right on. We're, as a community, like, it's pretty hard to… I don't know, there's some phrase for it, but, there's… yeah, we're… There's no… it needs a… somebody who's driving it.
jmacdonald 00:19:43 Okay, well, I think there are no further comments on this one. I've been taking some notes, and we will continue now, I think.
unless, sir. Any more remarks on that topic? I would like us to move to the OBI project update, and I'm hoping it's not completely 20 minutes, but is Nicola here?
That might change our plans.
Okay, so Nikola is not responding, and that means, I think… is anyone here to speak for OBI at all?
Tyler 00:20:20 I mean, I'm here, I'm not… Planning to give you an overview of it.
jmacdonald 00:20:26 Okay. This was the… the plan is that we were going to just review projects every week. I still didn't get my update from last week in, so, without a person ready to present, we should move on.
Next in the agenda, Carlos, could you give us, something on the Contact Scope Attributes Project?
Carlos Alberto Cortez 00:20:45 Yeah, that's gonna take 10 minutes instead of 5, sorry about that. I'm gonna try to go to the point. I know, I don't know, whoever is sharing, would you mind sharing, some of the stuff there at the agenda?
jmacdonald 00:20:57 That's me, I'll get… hang on a second.
Carlos Alberto Cortez 00:20:59 Yeah, no worries. In the meantime, I can start talking. Basically, sorry for spamming you every other week about this OTEP.
But I feel like there's always a big risk with this OTEP that we will never get merged, that that's why I'm trying to bring attention to this. And actually, that's what happened with the previous iteration of the OTEP that Christian had in the past. So sorry about that.
So let's jump into the actual stuff, just for your information. The first one is that I feel like we are going around in circles at some points. If you could open the doc, actually, like, of the document… I mean, this is.
jmacdonald 00:21:32 this one.
Carlos Alberto Cortez 00:21:33 The actual document, the specification, Wait a second…
jmacdonald 00:21:40 Am I in the right place?
No.
Carlos Alberto Cortez 00:21:42 Well, yes and no. Sorry, I just posted the dog, you know, the standard… Specification Agenda doc here, so it's easier for you to open.
jmacdonald 00:21:51 Sorry, I'm trying to take notes and share a screen, which is really hard for some reason.
Yeah, that's true.
Carlos Alberto Cortez 00:21:57 Correct.
jmacdonald 00:21:58 Oops.
Carlos Alberto Cortez 00:21:58 Sweet.
jmacdonald 00:22:02 You guys, I don't know how to find anything on the internet. Here we are.
Carlos Alberto Cortez 00:22:07 Here we are at the work, yeah. Otherwise, I could do that. Okay, thank you so much for that. Yeah, anyway, so… The first one is that I feel like we're going around circles, like, stuff, but… and you may remember that there was a discussion regarding, like.
10 or 8… 12 or 8, even, alternatives, and that's the problem, that people keep coming in circles. And one of the things is that, now it's, like, we already discussed why processors, we are not doing that. Now it's, like, another discussion regarding processors, like, why don't we support the idea of context scope attributes via processors? And one of the reasons is that there are no processors for metrics, and then It's like, we're waking up that, we can add them. Like, no, the previous OTEP took a year, and it was never merged. So that's why I'm preferring to stay the way this OTEP goes. Like, no processors. Processors could have, in a way, we will have to modify that interface.
But I don't want to, you know… I think it would be sad to depend on processors, and then having no matrix processor, and then probably by 2028, we have that ready, you know? I hope that makes sense. Do we have any comments on the processor's alternative?
Pellared 00:23:13 I think, regarding the measurement processor, I think, Tyler, had the PR, or, how it could be implemented on views, instead of creating another component, but… and I think that the author of the OTEP just didn't have time to follow up.
But I think that was the last time we were discussing the processing and the metric side. Because there was, like, the implementation as a separate component, and I think Tyler implemented… showcased that it could be implemented by a view.
Carlos Alberto Cortez 00:23:49 Yeah, I would say that there's also the question about whether, like, doing that via processors is the best thing or not, is, like, a good approach. There are always trade-offs.
And I don't want to, you know, halt the current approach because of that, you know.
Josh.
Josh Suereth 00:24:10 Yeah, I made this comment just today, but, like, reading through everything, I think, like, let's focus on the use case that's important, as opposed to the way that we do it, which is just.
Carlos Alberto Cortez 00:24:20 ship.
Josh Suereth 00:24:20 What's the interaction between these metrics?
Carlos Alberto Cortez 00:24:23 The next bullet.
Josh Suereth 00:24:25 Yeah, so, so, like, that's, that, like… let's just come up with something we all agree is fine for V1, because I, like, to your point.
We need to make progress here. We know that these things are needed. We know that we've wanted them for, what, 5 years? So, I think, like, let's start to make progress. Let's figure out the right initial interaction there. I think there were a lot of great proposals.
And then the second thing for me was the… there was a bit of stuff around, like, not allowing, instrumentation.
to provide these by default. I actually think, like, one of the things we're seeing with some of the instrumentation, I don't think we want that to be our default story, but I also think, Carlos, you can just delegate that to the folks writing the instrumentation and say, hey, we need a best practice, leave it as an open question.
We'll figure it out as part of, like, the folks who are engaging with it first, so we say, like, be careful with these… for now.
But, like, you can delegate that, like, you don't have to solve in the OTEP either, you know? So that…
Carlos Alberto Cortez 00:25:24 Yeah, actually, Yep, yeah, that's a good point, and actually, that was my initial, like, and this is, one part of the third bullet that I had in the docs, is, like, I would like to provide, like, some initial guidance or suggestions on how, like, people creating instrumentation should act.
And that's what we do from the specification for now. And this means that This will be an opt-in. Like, if you want context scope attributes from the instrumentation library.
it's an opt-in. The user has to enable them, like, enable that part explicitly, and it's really heavily recommended that whatever you add is low cardinality, in case it touches metrics, So, if that's fine, then I think we can make that change. I haven't made that change in the tab itself, but I think it's a good trade-off for now.
Jack.
Jack Berg 00:26:14 Yeah, I'm sorry I haven't reviewed this recently, Carlos. I do intend on reviewing it, and just glancing over it now, I think I'm… probably just going to approve it as is, because, like, I don't want perfect to get in the way of good.
And there is still… like, one thing that I want to call out is, like, the thing I've been thinking about most from this is, like, a configuration standpoint. Like, what is the… what's the user API for how you opt into this, and to what degree do you have, like, fine-grained control over whether you're opting into this? And this has, like, this has implications for things like whether or not instrumentation should be allowed to contribute to context-scoped attributes, because if it's only the user, then, or the application owner, then, you know, they're essentially opting in by recording these things, and so you need less granular controls at the SDK level, because, you know, you've already kind of ruled out instrumentation doing things that they shouldn't.
And so… but, like.
you know, so, you know, the question in my head is, what does the config API look like, and how granular should it be? And I actually… I don't think it matters that much right now. I think what you've proposed is, like, top-level broad controls. Like, you can opt in or opt out.
for all context-scoped attributes at the span level, the log level, and, like, the meter level, right? So… we can always add finer-grained controls later, right? So, it doesn't matter that we're starting out broad. If we encounter issues with those controls being too broad, we can add finer-grained controls later. So that's why I'm supportive of this, even though I think it's, like, it's potentially imperfect. It solves a problem, and we can evolve.
Carlos Alberto Cortez 00:28:02 Yeah, correct. I think that we can start with something, and that… well, actually, well, that's probably one of the things that we don't have to disclose right now, is what would be the default value, but the idea is that, at the very least, you can control it by signal. So basically, you… like, in case you want to… you want to be super sure that you don't want that in metrics, you disable that for metrics.
or for traces, or for logs, or you enable the three of them, or a mix of those combinations. That could be the start, and it's a complete configuration story, but I think that's… Enough for the… for the first version, yeah.
And that takes me to the next point, which is the second one that, to David Sashpole, a prototype.
on that… basically, David, like, he has this idea, I think David is in the call, that when you're upgrading, like, when you're adding context scope attributes, you know whether that attribute you're adding is an optional thing… is an optional attribute for a metric, or it's something that you really want to go in. If it's optional, you… maybe you want to put that You know, and you don't want it to be affecting cardinality, you put that in the exemplars attributes, you know, instead.
And, that's part of that. Like, in that case, one… If everybody agrees with that.
I think that, basically, what I could be massaging… the way I would be massaging the tab is that you have the context and you have scope attributes.
Which are, like, the standard activities you add to everything, and then optional.
In the prototype of David, he has that in two separate… let me see, it's up… It's, I think a little bit down. Yeah, that one, that's a part, yes. That part. Context attributes dropped. Basically, he's separating them into, like, metric would be the ones that every signal would be using, and exemplar is, like, the optional ones. And then, in the future.
metrics users could configure, like, basically, like, even the attributes you are using as an exemplar, they could actually go into the actual metrics, you know?
Sorry.
So in that case, it's a… This is basically taking advantage of this possibility that the possibility of the user knowing when they set the context group attributes, whether You want them, like.
Always, like, to go to the main set, or it's something that you can, like, forget, you know?
Or go to exemplars, you know? Sorry for…
David Ashpole 00:30:28 Yeah, to be clear, these… it's basically… If you were to add… A… an attribute to your context?
And say that you don't want it on your metrics.
Then it would still show up in the same way that filtered-out attributes show up.
On your exemplars as filtered attributes.
And users would still be able to, at runtime, like, say, via declarative config.
Opt back into those attributes if they really needed them.
So they would behave just the same as other default disabled attributes behave.
Carlos Alberto Cortez 00:31:08 And correct me if I am wrong, David, but when you say a runtime configuration, you're talking about views, correct?
David Ashpole 00:31:14 Yeah, yeah, yeah.
Carlos Alberto Cortez 00:31:15 Okay, yeah.
Jack Berg 00:31:18 I think… I think in the… in terms of this cardinality issue for metrics.
I think we should… I get the feeling we should not try to address this in the initial scope.
And the reason is, like, I want to make sure we can evolve to, like, solve for cardinality problems in the future. And so, like, if we foresee issues with the design and its evolvability.
Great, go tackle that. But we have other conversations that could be potentially related. Like, we've talked about wanting to potentially include things like unit on attributes, and maybe some description of its cardinality is part of, like, an extended attribute definition that should be handled, like, kind of holistically with this unit extension.
And so, like, if we're going to capture additional metadata on attributes and allow the SDK behavior to potentially change based on those attributes, I want to think about a big picture. And so, like, that's what kind of steers me in the direction of, let's punt on this for now, if we can get away from… with it.
David Ashpole 00:32:19 I… I agree, wholeheartedly. I think the sticking point is just gonna be defaults.
If we say, we're not, we're not gonna put any knobs on this right now, then the question is, okay.
How does… Like, do these attributes that you stick in the context end up in metric?
Attributes by default, or do they end up… As, like, basically filtered attributes, and you have to go use views to put them on.
Jack Berg 00:32:48 Well, right now, the knobs are just true-false based on signal.
And so…
David Ashpole 00:32:52 So that exists?
Jack Berg 00:32:54 So that's in the current proposal. Yeah, so there is a knob, it's just, like, the knob is overly broad. So it's, like, you're either opted in for all metrics, or, you know, it's disabled for all metrics. And that's where I talk about evolution, because you can take that broad brushstroke and evolve that to be, like, you know, either configurable at the view level, or configurable at the scope level, or configurable At the global level for meter provider, but, like, with an include-exclude list, so you have, like, control over the individual attributes.
And I don't think that having a Boolean for now, like, excludes those options.
Carlos Alberto Cortez 00:33:36 And regarding that, that's… there was one more point I think I forgot to put, or it got lost, about… oh, actually, what CEO was mentioning, that in his opinion, because of the potential, not only the cardinality explosion risk, but also the allocation and performance impact Like, he could prefer, as a maintainer, that this feature is disabled by default.
So, that's the other thing, you know?
Jack Berg 00:34:05 Well, it is disabled by default, because it only gets turned on when you start using these new APIs that do not exist yet.
Carlos Alberto Cortez 00:34:13 Yeah, but I think that in his case, he would like to even go one step beyond, and it's like, okay, like, even if nobody's using that, you're not even going to be checking anything from the context, you know? Yeah. And that's the… I don't know, that's the initial thing that I had in my mind.
Which probably seemed, like, kind of paranoid, but that also put us on the safe spot, you know?
Jack Berg 00:34:34 Yeah, and if it's easy enough to opt into with declarative config at the global level, I don't actually see it being that big of an issue if it's disabled by default.
Yeah, if it's hard to opt into, that's, like, a different… that's a different story, so, I would not argue or split hairs over CJO's point there.
Carlos Alberto Cortez 00:34:58 And we're over time, but do we have a last comment, maybe from David, since you were the person taking the list, or you're fine?
David Ashpole 00:35:07 Oh, I… I think my… the main requirement that I'd like this to have is that someone, if they don't set any knobs in declarative config.
Is able to use the feature, but provide, like, a default experience that's safe. So I… I feel like if… If I use context attributes somewhere in my code.
and I ship a binary with that?
Like… It feels like a bad case to be in, where the user has to make sure that they provide a declarative config that turns something off in order to, like, not have performance or cardinality issues.
Carlos Alberto Cortez 00:35:46 Yep.
Jack Berg 00:35:47 Wait, so just to clarify your point there, so, declarative config is built on top of the programmatic APIs, so there would have to be equivalent programmatic config APIs to do these, and so you're saying, like.
Like, it's insufficient if we ship a binary, which, when you use the programmatic config APIs to turn this thing on, it is unsafe by default.
It is unsafe once you turn it on, like, because that's not by default, you've already opted in.
David Ashpole 00:36:18 it's almost like I'd prefer if just using the context the new API that's being added?
doesn't automatically opt it into all signals. Like.
Jack Berg 00:36:30 Okay.
I think it does. I think you're aligned with CJ, then.
Carlos Alberto Cortez 00:36:34 Yeah.
Jack Berg 00:36:35 So that, yeah, like, you record, you call this new API, which doesn't exist, and nothing happens by default. And it's only once you call the programmatic config API, or declarative config, which is built on top of that, that things start getting opted in at a signal level.
David Ashpole 00:36:50 I'm maybe less restrictive than CJO. I'm happy if spans or logs are opted in by default. I just really… like, don't love the idea that metrics are opted in by default. Like… that a user would need to go set something. Or I guess I can use… I can do it via programmatic config, you're right. But in this brave new world where everyone is just supposed to put new SDK in there.
You know, in their initialization thing, and get all their config via, via, declarative config.
I would like, like, for that experience to be safe for metrics.
Yeah, that's all.
Carlos Alberto Cortez 00:37:30 Okay, yeah, I think that's enough feedback for now. I will go and massage. Please don't treat the tap till tomorrow. I will. Otherwise, it can be a loss of time, because I need to, message what, you know, what this group provided as feedback. Yeah, I will probably just, yeah, just need liquid today. Yeah, and then, yeah, let's, thank you so much for that. I think we have, like.
path forward.
And we're over time, sorry for that. Thank you so much for, spamming you again, but this has been really, really, really helpful. Thank you.
jmacdonald 00:38:02 Thank you, Carlos.
Okay, folks, I, see the next item on the agenda is David's point about mergeable metric views.
David Ashpole 00:38:13 Yeah, so I'll… I'll try and be quick here. It's… it's a kind of hairy topic, so I'm mostly… like, trying to solicit feedback here, but I'll give a brief overview.
So, a while back, I talked a bunch about trying to add opt-in metric advisory parameters, and now I'm one level further down the rabbit hole, and I'm trying to make an adjustment to views So that they're more useful, generally.
In order to, be able to Make changes, say, at the scope level, or make changes at the meter provider level.
Right now, because views don't merge.
They're very useful if you want to change a single instrument.
But once you start saying that you want to do things like update one instrument, you know, say change the name or change the description, and then also make some broader policy change, like Enable a couple of opt-in Things, or enable everything within a scope.
Or change all the histograms to exponential… Or things like that, then views start to be very problematic, because they don't merge, they just… Throw warnings, and then give you duplicate information.
If you wouldn't mind popping over to the… the issue. So this… this is the… the inspiration for it, that I've put on hold for now.
No, go back to the… Go back to the.
jmacdonald 00:39:44 Alright.
David Ashpole 00:39:47 So, click on the second… yeah, so this is the… the issue I'm currently working through. Oh, no, did I… No.
jmacdonald 00:39:54 No, they were the same link. I think this is the issue.
David Ashpole 00:39:58 Nope. Nope. Scroll down to the very bottom of the PR. I'm so sorry about that.
jmacdonald 00:40:01 Okay, the PR.
Is this Steve Sharp?
No.
David Ashpole 00:40:08 No.
jmacdonald 00:40:09 This is an issue, David. This is the PR. Sorry. Why? I can't run meetings, you guys. Okay, I'm opening the PR again.
Am I in the right place?
David Ashpole 00:40:26 No, let me find it. I'm sorry.
jmacdonald 00:40:27 Would you like to share?
David Ashpole 00:40:29 It's Issue 5013.
Huh.
Okay.
jmacdonald 00:40:43 Alright, here we are.
David Ashpole 00:40:45 Okay.
So, the basic gist is that, I actually consider it a bit of a spec bug.
Now that I've had time to go through it, which is that If you provide a view.
And the name collides with the name of another view, which is the case if you're doing anything other than renaming a metric.
Ben… instead of trying to merge the two views together and say, oh, the user asked for two modifications to this metric, I should make both of the modifications. Instead, we give you one view with one of the modifications and a separate metric with the other one, right? And throw a big warning saying, what are you doing, user? So, I, you know, in a perfect world, I would go and fix this, maybe in a V2, but, I think for now.
the best way to approach this without making a huge splash is to try and find some way to make… to declare a view that should be merged with other views. And so it doesn't generate its own stream, it just modifies the existing views that match.
And there's a few different ideas for how to do that here. One is… an opt-in to… Better view behavior, and another would be… Just adding… Like, a field on it that just says, this is a view that should be merged.
Jack, you've had your hand up. I'll let you…
Jack Berg 00:42:18 No, I want you to finish your thought, because, I… this… this issue has been, like, eternally frustrating for me.
David Ashpole 00:42:25 dinner.
Jack Berg 00:42:25 The semantics and views.
David Ashpole 00:42:28 I think almost all the solutions end up doing the same thing. I feel like mostly… There may be differences in terms of how it's expressed.
In config, and how readable, and how easy it is, maybe, to get yourself into some weird corner cases. But I… having thought about it, I don't think there's a lot of… I feel like the answers as to what users probably want with this is obvious, and it's mostly a question of how to do it cleanly while preserving backwards compatibility.
Jack.
Jack Berg 00:43:00 So, in the comment that I left on your PR that's been converted to a draft, I talked about, you know, kind of two broad families of solutions for this, and one of them is, you know, if there's multiple matching views, merge them together somehow.
The other way is, like, a first match wins semantic.
So, like, I lean towards first match wins.
Because it's really simple to reason about.
It's really easy to, like, craft, like, catch-all rules at, like, the bottom that say, like, hey, you know, configure this specific instrument, but if it doesn't match, then, you know, have a catch-all rule that catches, like, all histograms and chooses exponential histograms for them, or something like that.
And, like, the idea… that… the current semantic is based around, which is like, hey, I want to match one instrument two times and produce two different metrics from that original one instrument. It's such a far-fetched idea, it's like, I can barely wrap my head around it, like, when that would actually be useful to do. Like, take a… select against a counter, and instead of having one thing come out, have two things come out.
Who wants to do that, and why?
It's a very silly thing. So, yeah, I'm… I really agree with fixing this.
I prefer a first match wins semantic, because I've seen lots of systems all over technology that employ this, like, you know, an array of rules where, you know, the first match is… dictates what happens.
And then, how you do this in a backwards compatible way? So, in declarative config, we have this meter provider, and meter provider views. Views is where you configure, like, your array of views within meter provider. We could have another property that's a sibling of views that would just be, like, view semantic.
And ViewSemantic defaults to what it is currently, but it could have another option, which would be first wins.
And, like, that would keep everything the same, and all it would do is change, like, the matching semantics. So, you know, that's kind of my two cents on how to solve this.
David Ashpole 00:45:17 Awesome. Yeah, I had something. I think I… I was heavily inspired by your comment, so a lot of the options listed here are me trying to flush those out. I think I did last wins, but we can do first wins instead. I don't… I'm not that opinionated.
Jack Berg 00:45:33 First wins is a pattern that we've already, like, employed in declarative config in places, so I don't know, sort of.
David Ashpole 00:45:40 Look at Proposal 1 here, and…
Jack Berg 00:45:42 Okay.
David Ashpole 00:45:43 So, if you scroll up, I think this was, like.
Composable views enabled true, so… but we could have an enum there instead.
Jack Berg 00:45:51 Yeah, something like that, exactly. And that keeps it backwards compatible.
I owe you a review on this, I will take it.
David Ashpole 00:45:59 Thanks. And anyone else who's interested, please?
Happy to hear other ideas.
Thanks. My time is definitely up.
jmacdonald 00:46:07 Cool, and we've updated the notes with the proper links. Thank you very much.
Okay, please follow up. I also have felt uneasy about views for years and years, and Jock just touched on some of the reasons why.
Okay, well then, I am next on the agenda, and this was, the idea was that sometimes we have extra time in this meeting, and there are sort of minutes to spare, and, I volunteered to give an update from a SIG that I am a part of. I've been a part of the sampling SIG for years now.
So I'm going to do that. Does anybody have any problems with me doing that?
Okay. No, you have a problem. Okay, so, what I'm trying to tell you today is, kind of an update from SamplingSig. This is a long timeline that I'm showing here, and I brought it up for a reason.
you know, you… we can… we can all… some of us can remember the start of OpenTelemetry, and… how it kind of evolved out of OpenCensus and other things that were happening at the same time.
But also, there was a tremendous amount of work that went before OpenTelemetry, including the Google Dapper project, Zipkin, and Jaeger, and so on. So by the time we got to 2020 or so, and we were trying to stabilize OpenTelemetry, there was a great push to just accept what we had written.
And the thing is that we hadn't finished something about sampling. And so this, this PR number 611, like, from 6 years ago, puts in a big to-do.
Which said something like, review and specify the algorithm for consistent probability sampling.
And that to-do stayed for 5 or 6 years. So this is my update. We've been working in sampling SIG for some years to try and fix that to-do.
And, you know, like, where I come from on this is that, if you're a vendor selling tracing support, and you don't have some kind of sampling story, many of your users are going to find it to be too expensive. And the reason why I put the timeline I borrowed from somewhere else to have this Dapper thing at the top is that that's kind of where I started. I was on that team long, long ago.
And one of the most important parts of that system was that it did sampling. And so if you read the paper, you know, it starts out with 1 in 1,000 sampling by default, or something like that.
Okay, so years… years later, we were in the open tracing world, and Jaeger had a lot of, like, clout, and we were… everyone was sort of, like, starting to use Jaeger remote sampling.
Jaeger remote sampling was an innovation that gave us the ability to, like, remotely configure a sampler. However.
if you go back to what we were doing back there at Google way back when, it didn't have anything about probability sampling built in, so the question kind of coming into the world of Jaeger then was, well, how do we do probability sampling? Well, the answer could be just flip a coin, just do your probability sampling. But the thing that we were looking for when we when we ask for sampling is not just to be able to do sampling, but to know after the fact how much was this sampled? If the span was counted 1 in 1,000, sampled one in a thousand, you should count it for a thousand spans, and that's, like, the big idea. So… and this big idea was sort of lost by the time we got to open telemetry and the initial specification.
So… 1413 was the issue, saying we should fix this to-do. It stuck around for a while, and then the sampling state kind of booted up, and we wrote some OTEPs, 168 and 170, Just describing history, talking about why we think probability matters, talking about how we want a span to metrics pipeline. Like, many of us want to be able to count spans after sampling them.
That led to, what we call the experimental specification here in 2047, so this is still several years old. This is now gone. This is the original experimental experiment, sampling proposal, which is no longer with us, except it did introduce something we call the trace state. So OpenTelemetry trace state is now a thing which we specified back then in this earlier draft. OpenTelemetry TraceState has, a syntax for expressing probability.
But the initial specification was not really very good, and it focused on… only supporting powers of 2, which… power ability sampling, which is feasible, but not good enough for many of our users. So, this didn't really land. So then, another year or two later, we started again.
OTEP235 is the one that really changed everything for us, and that's what's currently in the specification. OTEP 250 adds a little bit on top of it for what we're calling composable samplers, but let's just start with the basics, because the point here is that we started OpenTeometry tracing, never solved sampling, and if we don't get here, we aren't finished.
So… Trace Context Level 2 came around, this is what we were waiting for.
This is a way for the trace context to embed a bit that says, I am a random trace ID, because much of what we want to do requires us to have some randomness that we all agree to. So Trace Context Level 2, became part of the OTEL specification last year, about a year ago.
Not quite a year ago. And what this does is says that we should upgrade from our W3C Trace Context Level 1 to level 2, and that gives us this random bit.
The random bit says, I promise you, or I declare, these 56 bits, the least significant 56 bits.
of every trace ID should be random.
56 bits was chosen with the industry, like, if you look at the Amazon X-Ray Trace ID, that has 56 bits. They all have 56 bits, so what we're doing is we're presuming that traces are random at this point. We're not going to wait for W3C Trace Context Level 2. They've always been random. Now we're just presuming they're random, and we're following up with a bit that says they're random.
So, we now have trace context level 2. We've specified that OpenTelemetry should set 56 bits of randomness and set a bit saying they are random.
That's just the start. We need to have that randomness in order to do anything afterwards. So then, we added a thing called Probability Sampler, and this was merged again about a year ago, some point last year, and this introduces something that… well, in the… in the, in the, In the interim moment here, it's called trace ID ratio. We tried to change the definition of trace ID ratio. Eventually, that was sort of, like, rejected, and we went back and we renamed it. So it's now called Probability Sampler. It's a new sampler.
And the idea is that trace ID ratio is just going to stay the way it's always been, we'll let it, we'll sunset it, it'll be gone, and forevermore.
So then… We now have… specification for randomness, how you manage the OpenTelemetry trace state to say what randomness is, and to say what tracing probability you have. The last piece of this came from OTEP250. I don't think we should dwell on it.
But it gave us the ability to compose probabilistic samplers. So you can have a rule-based sampler, you can say, I want my parents' threshold if I… if they're there, you can say I want to have if the page matches something, I want this probability. And there's a lot of rules for composing probability that we're baking into the specifications so that the… so that you get it right. Like, if you compose two probabilistic samplers, you need to know the probability when you're done. So that's what this work is doing.
And now we have all this written in specification, so we're kind of waiting for it to, to land in all the SDKs.
I'm gonna give you a brief… brief description of this new thing called OpenTelemetry TraceState, which has been spec'd for years now, it's just that now we have definitions for these variables in the trace state. So there's two variables now, one is called TH, one is called RV. TH is the major feature here. This gives us the ability to say, what's my sampling threshold?
And if you're familiar with, like, probabilistic algorithms, you know, what we're imagining here is that you take those 56 bits, construct a random number out of them, now choose a threshold, and you're gonna say, I'm gonna… sample above or below that threshold. The rule that we ended up with here is to say if the threshold is below the randomness value sample. So threshold zero turns into 100% sampling.
Threshold 0 says, I have… I will… I will select any trace that has a randomness larger than 0 or greater than or equal to 0. So, then if you… you have to be familiar with hexadecimal notation to kind of read this very well, but… so if I say OT, that's OpenTelemetry trace date, equals TH8 colon 8, What I'm saying is that this starts with 8, and 8 is obviously a 1 followed by a bunch of zeros, right, in binary. So, this is a 1 bit, and then a bunch of zeros, 55 of them.
And what we're doing is we're padding with zeros to get to 14 hex decimal characters. 14 hex decimal characters is 56 bits. So I can leave off all the trailing zeros so that I can have a compact representation of my sampling probability.
If I say ODTH equals F, I'm saying 1 16th have been sampled. So it's, there's a little bit of an inversion here. So 0 is 100% sampling, and all Fs is the smallest probability sampling you can get. We're looking for trace IDs that fall below the randomness value.
So there's… specification gives us rules for how to implement this stuff. There's this other feature here called Randomness Value, and I don't think we should dwell on it, but it gives you the ability to override. Like, if you don't like your 56 bits of randomness, or you want to choose new 56 bits of randomness for any reason.
If you think that the trace ID is not random because of a legacy, again, you have the ability to put your own randomness in the trace state instead of in the trace ID.
And there's some rules that are pretty particular about how to manage that, so that when we get to the end of a pipeline, you get spandom metrics that are correct.
So this is where we are right now. The three PRs, the four PRs that I merged last year… last year, are all now kind of waiting for SDKs to do them. We have work going on in some of the SDKs, and I'm familiar with the work in Go right now. I know there has been work in others.
But let's see. So we have… the first thing we want everyone to do in the SDKs is to implement that random flag, upgrade to W3C… W3C Trace Context Level 2.
Then we want to implement a new probability sampler, which is… which is following this new algorithm.
That's spec'd out in the… in the… in the tracing spec.
And the next step, which is sort of, like, I think this can be further out, is to implement composable samplers. Composable samplers is when you start to be able to say, I have a rule, I want to, like, look at my URL or something, and change my sampling probability.
It… from there, we'll… then the next step would be to go for declarative configuration.
So, what's on the roadmap?
Jack Berg 00:57:00 is done.
jmacdonald 00:57:02 I know, I know, I know, Jack, we were waiting for declarative config to be done so that we could start adding stuff to it. No, no, no.
Jack Berg 00:57:08 Oh, no, composable Sampler is in declarative config. Anorog added it.
jmacdonald 00:57:13 Okay, sorry, I'm out of date on that one. I thought we were waiting for, like, a 1.1, so I stand corrected. We have some composable sampler, features And I think no one's implemented them.
That's where we are.
Jack Berg 00:57:27 Galva has.
jmacdonald 00:57:28 Java has. Okay, Java's always ahead. So, so Java, JavaScript, Go have some of this work done. Java's way far ahead, because all the, sort of, sampling experts started there as well. We have a couple of heavy Java users in the sampling sig.
Okay, so… so I spoke incorrectly. We have the configuration model, because Peter, from our sampling SIG, was working on it all along. One of the things that we want, that everyone kind of wants, is, like, an adaptive sample, or some way to say, just… just, like, no more than 20 per second, or whatever, no more than 100 per second.
But with probability, like, if you just say 100 per second and don't give a threshold, you're gonna get 100 per second, and you'll have no idea how many there were. You need a probabilistic solution to be able to count how many there were.
And I think that the holy grail for us, I think everyone in tracing kind of wants to get back to where Jaeger remote sampling was 10 years ago, basically, where the system, the collector, someone who's monitoring the stream of traces is able to say, I see too many traces, I'm going to turn down specifically these traces for these users to be able to have, essentially a feedback loop. That's the kind of, what everyone's after, and OpenTelemetry can't really do that, and that's why we're still doing this work.
So if you're familiar with some of the other vendors who have, kind of, built-in tracing sampling solutions, that's what we, the community, would like. And eventually, we'll get to doing exactly what Jaeger Remote Sampling could do, but with OpenTelemetry conventions and OpenTelemetry semantics in place.
I think that's my quick update. I see some chatter in the chat. I would like to open the floor to comments.
Tigran.
Tigran Najaryan 00:59:12 Yeah, sorry, this is a bit more tangential.
The trace IDs, as they are 128-bit random values, they… they don't compress well. Does your SIG have any opinion about what the other 72 bits are… should… should look like? They are still random today.
jmacdonald 00:59:29 Right.
Tigran Najaryan 00:59:30 I know, with most generators.
jmacdonald 00:59:33 I am familiar with…
Tigran Najaryan 00:59:34 And way of generating those.
jmacdonald 00:59:36 Yeah, I'm familiar with requests to use UUID 7, so that there would be temporal,
Tigran Najaryan 00:59:43 Yeah.
jmacdonald 00:59:43 similarity, I guess?
That has come up. It has not been… directly addressed in sampling, though. It's like, we're aware of that, and I've seen people, like, DM me questions about that.
Tigran Najaryan 00:59:56 Yeah.
jmacdonald 00:59:57 But accepting this standard here does give us a way to, begin saying, we don't really care what's in those other 72 bits, you could choose more stable values, you could choose, if it's not timestamp, you could choose some other sort of host-based uniqueness, maybe, and put them in somewhere.
Yeah, that's the idea behind choosing those 56, was that we're free now.
All right.
Tigran Najaryan 01:00:25 Thanks.
jmacdonald 01:00:26 Yep.
I'm gonna make a few notes based on what just came up, but I think we're ready to move on, unless there are any more questions?
Jack Berg 01:00:37 Quick comment, Josh.
So do you have tracking issues for stabilizing these components?
jmacdonald 01:00:43 Maybe.
I can get ya, I can… I'm not sure if I do.
Jack Berg 01:00:50 I would recommend adding those if they don't exist. They're a great tool, to be able to detect when you have the three implementation requirements, and when you can propose going stable.
jmacdonald 01:01:01 Okay.
Yes, thank you, I will… I'll make that note, and check what we have.
That's true.
You're welcome. I will, hand it over to Robert, who has 1, 2, 3 small items ahead.
Carlos Alberto Cortez 01:01:22 We're… we are on time, by the way.
Pellared 01:01:24 Yeah, so just…
jmacdonald 01:01:26 Oh, we're out of time, wow. Yeah, yeah, I will not hand it over unless Robert wants to say two words. Next time.
Pellared 01:01:33 Just look. Excellent. Thank you.
jmacdonald 01:01:35 Thank you, yes, three links for Robert, and we have two topics that we didn't get to. Braden, I'm sorry we didn't reach you, and then we have to come back to the OBI update for next time. We're getting to be out of time every week now. Great.
Could be worse. Thank you all, see you next time.
Reiley 01:01:51 Thank you.
Pellared 01:01:51 seconds.
