SIG: Specification SIG
Date: 2026-05-05
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/wTXu2vz44QZU4GuArbSmp-Jf-OJcLXtOPYHwil43jyNKJ8wSMr1wEnQT86SA9EUN.m7TXRBBzqWLGsgq8
============================================================

## Zoom Recording Transcript

Reiley 00:03:13 Hello, everyone.
David Ashpole 00:03:18 Hey, Riley.
Reiley 00:03:25 Thank you. Morning.
Liudmila Molkova 00:04:27 Hello.
Trask Stalnaker 00:04:32 Yay.
Reiley 00:04:32 Hey, Lamel.
Liudmila Molkova 00:05:04 Okay, I think it's my turn to… Run this meeting.
Can people hear me?
Trask Stalnaker 00:05:14 Yes.
Reiley 00:05:15 Yeah.
Liudmila Molkova 00:05:15 Awesome. Thank you.
I wasn't sure.
Okay.
So we'll let people one more minute to join. If you have anything, please add the topic to the agenda.
Do we have any, project updates today?
Doesn't seem so.
Ted Young 00:05:59 Maybe I… you know, the stable by default stuff and all of that's a pretty big bugbear, so I'm happy to get through that, but maybe we should start scheduling some more project updates. We probably ran through our original list.
Liudmila Molkova 00:06:16 I think we remember… we wanted to do… the one for logs, one for GenAI. I don't think we'll run through them, but we… Didn't fill up.
Ted Young 00:06:31 Do you want to put them up at the top, maybe? That list you're looking at?
Liudmila Molkova 00:06:35 Yeah.
We didn't do sampling right, Josh, if Josh Monty's here.
Jack Berg 00:06:58 You say we didn't do sampling, or we did?
Liudmila Molkova 00:07:01 I think we didn't.
Jack Berg 00:07:02 We did… Josh, Josh did do it.
Liudmila Molkova 00:07:06 Okay, I missed it. Then we did ABPF.
Jack Berg 00:07:11 We did OBI, yes.
Liudmila Molkova 00:07:15 We didn't do logs, arrow, collector.
table by default on Gen AI.
Ted Young 00:07:21 Cross.
Jack Berg 00:07:22 Correct.
Ted Young 00:07:25 I'll bring this up with our community managers, because I think these are really helpful, and I want to see how maybe we can take those clippings out of the Zoom, or otherwise, like, take these project updates and kind of spread them wider than just this meeting.
Because people seem to really enjoy that content.
Liudmila Molkova 00:07:48 Wonderful, yeah, that's a great idea.
Cool, so let's probably start with the agenda. Do we have Robert?
We don't have… Robert.
Reiley 00:08:06 offline.
So maybe you just need people to read the PR.
Liudmila Molkova 00:08:11 Okay, I'll put it at the end in case he comes back.
And Carlos, I actually added context sculpt attributes. Do you want to talk about them first?
Carlos Alberto Cortez 00:08:24 Oh, sorry, I totally missed that. Yeah, thank you for that.
Yeah, you're right. Okay, so, this is just an update of this one. As you know, there are some reviews there, there are some pending items, that need to be solved.
From the last important thing that I received as feedback, I updated? The first one is that the initial API, calls were two, which is one for setting scope attributes, and the second one is for getting them. Now, instead of set, it's add. So, basically, you append them. And this also aligns with what David Ashbold had in his prototype, especially useful when You don't have a single user of this, but for example, instrumentation libraries want to set something in the context, but also the user wants to set something, so you don't override stuff.
That's the first change. And logically speaking, it should be the same, just making it more flexible. The second one, and more… more important question is that Tyler, Goman Tender was mentioning that for me there, for metrics, this is a little bit different, so when… when do we actually do this? And, I just added a small note mentioning that we should do this.
Right after… you created a meter instrument, and right before you apply views or anything else. I don't know if that's good enough, or we need more clarification, Do we have Tyler here?
Tyler 00:09:56 Yep.
I mean, I could take a look at what you wrote, I don't know, I haven't read it yet.
But going back to your question about the attributes and the overwriting, that was another one of my concerns that I had for you.
So, is the idea that we're just going to be, like, appending onto things at this point, and we're not going to, like, remove any information, and it's just going to preserve all of the attributes that have been set?
Carlos Alberto Cortez 00:10:22 Yeah, correct.
Tyler 00:10:24 And then where does that get resolved? Is that just in the… in the processing pipeline? Like, they have to figure that out?
Carlos Alberto Cortez 00:10:31 Maybe I need to add details there.
But basically, every time you call context, add attributes.
That just… those values, the final state stays in the context itself.
whether you keep a link at least, and you reverse it back, so you give priority to the last… lastly set values, or you just merge them. But once you actually get to span, or log record, or meter instrument creation time, you already have a result.
State of the attributes.
Tyler 00:11:04 Okay, yeah, that's what I'm missing. So, like, I kind of… where is this, like, you say by the time you get to the meter or creation time, it's already resolved? What, like, where is that resolved? Because it sounds like, on one hand, you're saying you just accumulate, and then on the other hand, you're saying, like, they're singular by the time that it gets to the meter and the tracer.
Jack Berg 00:11:25 Let's not think about this in terms of the meter, actually. Let's think about this in terms of the relationship to measurement recording, because that's what matters here for metrics. So, you record a measurement with, like, a value and a set of attributes, and we're trying to determine which aggregator, or which series, to, you know, increment, to update based on the set of attributes that was provided with that value. And, so Tyler, my intuition on this is to like, extend attribute processing, that phase of the measurement recording process, to include merging of the attributes presented, you know, at record time, with any attributes from context, if they are present and context scoped attributes are enabled.
Tyler 00:12:14 Yeah, that was my understanding as well, but I'm not hearing that from Carlos, so I was a little confused. So I want to make sure that, like, we're actually So, on the same page here.
Jack Berg 00:12:23 Yeah.
What do you think, Carlos?
Carlos Alberto Cortez 00:12:28 In that, that works, yes. Doesn't work. If… everybody is aligned with that. I realize, actually, that probably that sometimes the divulging the details I would like to listen from other people involved in metrics, like David Ashbo, Shay McD.
If we can confirm with them that initially this is a good approach, just to be super clear, then we are fine.
Tyler 00:12:52 Yeah, I think I'd like, that sounds good. So, like, if we get that collection of attributes being passed down to the metric processor.
I think that makes sense, but then I think it becomes a little bit more important about, like, that definition of what's going on in the metric, like, world, and, like, making sure that we have a clear vision on that.
So, I'd have to go back, and I'd probably have to read your note on how you clarified what's gonna be happening here. But yeah, I think… that we're on the right path, is what I'm saying, from my perspective.
Carlos Alberto Cortez 00:13:22 Yeah, I think we need more details, which I can add in that regard. But yeah, if you can… if you have time to do, like, a quick pass, especially regarding the last updates, and then, Yeah, I can iterate on that.
But yeah, I will do that in all cases.
Jack Berg 00:13:38 So, Carlos, in the metrics SDK document, there's a specific section that talks about attribute processing.
And, like, in your text, I would recommend, linking over to that, and essentially saying something to the effect that… of, like, we're gonna extend the attribute processing phase of measurement recording to merge the attributes. You know, we have to do… right now, attribute processing just means filtering out attributes according to views.
Now attribute processing is gonna merge the attributes presented at the record time with context, and then filter out for views.
And, like, the resolved set of attributes from those two steps is going to be what's used to resolve the series, or the aggregator. So, that's what I would look for, is the specific attribute processing section.
Carlos Alberto Cortez 00:14:26 Yeah, let's do that. Yeah, I will… it's a good idea to link that with that section.
Tyler 00:14:31 Well, I think link it, but also make sure you encapsulate what, like, the full entirety of what Jack just said. I think is kind of the important thing. Because, like, yeah, linking it there, saying that, like, there's a process, saying that there's, like, some sort of, like, procedural step that's gonna happen is gonna help clarify, as this goes into specification, what the intent is.
Carlos Alberto Cortez 00:14:50 Okay, I will update that later today.
Because now I get some notes, but definitely not enough.
Jack Berg 00:15:01 Whoa.
Carlos Alberto Cortez 00:15:02 Do we have anything else? One last thing that could be done, and I hope that's not the case, is that Because metrics has been, of course, one thing that people are concerned regarding how this feature could interact with metrics. So one potential thing is just to defer implementing this for metrics, and only do that for traces and unlocked first. I would prefer to do the three of them at the same time, but let's see how that goes.
Tyler 00:15:32 No, I don't… I don't think you need to go… that far. I think you're on the right path, and, like, what we've just discussed is addressing these things. I wouldn't pull this out at this point.
Carlos Alberto Cortez 00:15:42 Yep.
Yeah.
Jack Berg 00:15:44 Yeah, it'd be a shame to have to go back and add metrics later.
Tyler 00:15:47 Right.
Carlos Alberto Cortez 00:15:49 Yeah, I mean, this just could be a last resort, yeah, like, very last resort, but anyway, just for your information. Okay, thank you for the feedback, we can do one.
Liudmila Molkova 00:15:59 Awesome.
Thank you, and thank you, Carlos, for driving this.
Next update is about GenAI Semantic Convention Strask, I added your name, do you want to talk about it?
Do you want to share? Do you want me to share?
Trask Stalnaker 00:16:15 Yeah, yeah, I'll talk about it since you've got, lots of other stuff there. Yeah, so we've been, there's a lot of external interest, in the Gen AI semantic conventions, the, Linux Foundations, Agentic AI Foundation.
COSI, Coalition for Secure AI, OCSF, even were back chatting with them.
As well as all of the open inference, open LLMetry, Langchain folks. We've been just… we've been chatting with all of them lately in an effort to try to bring, to… stop the fragmentation in this space, because it's a natural space for it to become fragmented, because everybody's moving fast in their own directions, but that's having, I'm like… Can you hear me?
Liudmila Molkova 00:17:24 Yeah, yeah.
Trask Stalnaker 00:17:26 Okay.
Liudmila Molkova 00:17:27 Stupid jokes, right?
Trask Stalnaker 00:17:28 Yes, I do, like, I do talk with my hands. It is known.
So, our, one of the area… one of the ways we want to bring people together is to have a dedicated repository for the GenAI semantic conventions and, the GenAI Python, instrumentation.
It's… going to serve a few purposes. One is a landing space for everybody to, watch and join and participate in. Another is for the semantic conventions.
We're taking advantage of the federated SEMCOM work that's been going on for the last year. It's really come together nicely and allowing us to split SEMCOM out, pieces of SEMCOMP out.
We'll be doing more of this in the future.
We want to, of course, keep, like, really core, core things that everybody depends on, like.
client, server namespaces, service namespaces, probably… HTTP probably doesn't make sense to, move out of the core repo.
And… But there's a lot of other things that make sense to move out. The core repo can't just grow forever and ever.
So, the SEMCOM folks are pretty excited about being able to, federate these out. Whether it's owned by us, like, in this case, the GenAI Semantic Convention's just a separate repo under OpenTelemetry.
or allowing other people, potentially OCSF, to, working with them, they're looking at Weaver, and if they can federate their conventions, basically use our tooling, to do their, to… Express their existing conventions.
So… Yeah, to tie it back together, we've been working in the GenAI, some, GenAI SIG and Semantic Convention SIG for, a while now, planning this out, and so we just… put up the repo yesterday, and the PR to, remove all of the things from the semantic convention repo.
And so as soon as we… I have a community issue linked in the, meeting notes for, kind of, next steps.
Which include, you know, moving over issues, asking people who have open PRs to the core repo to replatform them to the new repo. We did take this opportunity to update the GenAI SEMCOM to, schema V2, the Weaver Schema V2.
And Lydmilla did some nice simplifications there.
And so, you know, it won't be… It'll be… Yeah, anyway, another, the new repo, it also has really, reference kind of a… this concept of reference instrumentations, which are basically manual instrumentations, all Python.
That allow us to, when you propose a semantic convention, GenAI PR, you would also update these, Yeah, scenarios.
So you would show how the attribute you're proposing actually, can be captured by this library.
And this is just manual instrumentation, but it basically… you… now you can kind of see the correlation between what the attribute you're passing into the library and how we would capture it in these semantic conventions.
Because that has been one of the, big blockers for moving quickly and getting PRs into SEM, the Gen AI SEMCOMs.
Because it's hard to know, like, it's not like HTTP or, you know, RPC domain, where kind of everything is kind of normalized. There's a lot of differences, and one of the key pieces that we look for in new proposals is that this data is actually capturable, supported by, you know, at least two, GenAI libraries.
Yeah.
Any… Questions, that was a lot of me talking.
Ted Young 00:22:34 What can we do to help?
Trask Stalnaker 00:22:37 Join the, GenAI SIG. we need… People who, we need approvers. We need people who will review the PRs. Our goal is really to speed up the, the semantic conventions for Gen AI.
One of the things we're gonna do in this new repo is we are going to do, Fairly frequent, probably major version releases, as often as, potentially every 6 months.
Because we want to… we just know the space is, you know, we can't predict what's gonna happen, and we want to have kind of these… Instead of… people floating across all kinds of versions. We want people to, pin to certain major version bumps. We'll do, you know, minor non-breaking changes, and then we'll do another major version bump as needed.
The Python, there's a bunch of work. You'll see, the next step is, Lyudmila has the Python repo, prototyped right now, so that will be the next thing to land.
And so, yeah, the… we… we need approvers.
People who, you know, can spend some time.
Ted Young 00:24:14 Awesome, thank you.
Liudmila Molkova 00:24:18 There's a question I think we should address, out loud from Antoine. Is there… are there other candidates to split off some conf?
I think… I don't think we want to, like, do an effort of splitting things, if there is a reason, but more like everything new that comes.
would probably come as federated thing.
Trask Stalnaker 00:24:42 We wanna… I think we will probably split out Java.
We want to do that, bring it into the Java repo.
I think other languages, I think that's a really good thing for languages to own.
once we, you know, we're still working out this process and perfecting it, I think this GenAI one is forcing us to, you know, work through the last few, kinks with the Weaver tooling and some of the packaging, reusable packages.
Another one, I know the maintainer, some comp folks are very.
Liudmila Molkova 00:25:23 Mainframes.
Trask Stalnaker 00:25:23 Sorry.
Thank you. The mainframe, some comm folks are very interested in, splitting out theirs, which would make a lot of sense, I think, also.
atoulme 00:25:34 Would that be a separate repository?
As well.
Trask Stalnaker 00:25:40 Sorry, I couldn't hear.
atoulme 00:25:41 Would that be a separate repository, for the mainframes as well, or is that, like…
Trask Stalnaker 00:25:46 I think so.
atoulme 00:25:47 Oh, okay, that's very good to know. Thank you.
Trask Stalnaker 00:25:52 The difference there being that is a… an existing community within OpenTelemetry SIG, so that would be a repo under OpenTelemetry.
versus something like OCSF or GraphQL, these are external groups who have their own communities, and so we would… Really prefer them to own their repos and their semantic conventions.
atoulme 00:26:19 Okay.
Yeah.
We, we do…
Trask Stalnaker 00:26:23 And as new… as new people come in and want new semantic conventions, we will probably, you know, if they have Especially if there are these other standards bodies, like GraphQL or OCSF, it makes a lot of sense for them to own it.
Ricardo.
Riccardo Magliocchetti 00:26:41 Yeah, I have a question from the language implementers. Like, at the moment, we depend only on the one… Semantic package.
So in the future, we will depend on a federated package, or we have, like, one dependency, like, we build one package for every separated repo.
Trask Stalnaker 00:27:09 Yeah, that's a great question. we don't have… I'm not sure we have a super solid answer for that. Limil, I know we chatted Previously, I don't know what… if you had specific thoughts on that.
Liudmila Molkova 00:27:26 Yeah, it sounds like we will need to have an Uber package, but not Uber for everybody, because the Uber package for Python doesn't need to include JMX metrics from Java or collector-specific things, right? So I would imagine that in Python, we will declare an Uber package that includes both OpenTelemetry semantic conventions and GenAI conventions, and it will grow, it will include some Python-specific conventions, let's say runtime metrics that are moved out.
And this will be a small manifest file, a small command to generate the full thing, and then generate code from this full thing.
But there is no prototype for it yet. I would imagine in Python we will hit it the first, and I will need to come up with a specific solution for it. But, how do you feel, Ricardo, about this?
Riccardo Magliocchetti 00:28:18 I don't have strong feelings, my only Both is, like, if GenAI really need Well, since you're moving… we're moving out the… instrumentation, I think, that… as a Python maintainer.
we don't care much? Like, we don't…
Liudmila Molkova 00:28:41 I do.
Riccardo Magliocchetti 00:28:42 internal user?
Maybe.
Liudmila Molkova 00:28:44 You do, because let's say, bedrock of olive is part of body core instrumentation, and yeah, you do. You cannot get away with that.
Riccardo Magliocchetti 00:28:52 Okay, so my doubt is, like, if GenAI want to release more often than the standard ones?
When Nikki…
Liudmila Molkova 00:29:00 be your Yes, hi.
Riccardo Magliocchetti 00:29:08 Yeah, like, if we have an Uber package, that depends on the… Or that contains the GenAI semantic compression as well.
we need to release it at the same pace as the GenAI convention, right?
Liudmila Molkova 00:29:21 I don't think so, because you can, pin the version.
Right? You would have to pin the version of the Jenny, I think, you pull in, or other federated conventions, and… It's your decision how fast to pull if we have a major version bump.
Then that's a separate story.
And then we… we should talk about it as stable by default.
Question after. But you would need to pace, go with your own pace, and decide when to take major changes.
Riccardo Magliocchetti 00:29:56 Okay, thanks.
Trask Stalnaker 00:29:59 Jack.
Jack Berg 00:30:00 Hopefully this will be quick, because I think we're well over the time. But, you know, we got these.
Trask Stalnaker 00:30:05 Oh, we're over the 2 minutes?
Jack Berg 00:30:07 Yeah, we're over the 2 minutes.
We're doing Federated SEMCOMF, you know, we got different groups within the OpenTelemetry umbrella, we got groups outside OpenTelemetry umbrella that are kind of deciding their own things, creating their own processes, and, you know, we got these Uber packages that kind of join them together. So, the Uber packages, you know, the ones that are maintained and published by OpenTelemetry still need to you know, do things like not make breaking changes and minor versions. And so, my question is, like, is the tooling that allows us to federate with Weaver and with these manifests. Does it make it easy to, like, detect and, you know, follow whatever guidance we have around breaking changes in versioning?
If that matters.
Liudmila Molkova 00:31:00 I'm glad you asked.
So, we do have, policies in Weaver that allow to detect breaking changes in each specific version. It's currently off for reasons, but it will be on soon.
And, we have a special package special repo.
called Weaver Packages, and we can use policies from this package anywhere. Anybody who creates the registry.
can add the check, and one of those checks is backward compatibility, and it implements what we have in the spec for telemetry guarantees. So, it depends on somebody setting up the tooling, right? But it's totally possible.
Jack Berg 00:31:50 Nice, thank you.
Liudmila Molkova 00:32:00 Awesome.
Anything else on this 2-minute topic?
Okay, moving on to another… I don't… I couldn't even estimate.
Yeah.
So I brought up some points that we didn't have a chance to discuss last time.
Yeah, Ted, do you want to take over? Do you want to talk about it?
Ted Young 00:32:29 Yeah, I'm happy to. So, you know, there's, Just some quick framing, for those tuning in for the first time. OpenTelemetry has lots of stuff in flight, we're building all kinds of interesting new things, but the other thing we need to do is sort of finish what we originally started.
What we originally promised people were tracing metrics and logs, stable and everywhere, along with, some implicit promises that you could install and manage these things at scale.
When we looked at what people need from OpenTelemetry, they need all of the stuff they're using actively in production to be stable, and they need a way to install and manage it without having to go around and, like, touch each individual component.
And we've got all of the pieces in flight, but we have so many projects up in the air, it's helpful to kind of coalesce all these things into one place.
That turned into this sort of Uber OTEP.
this OTEP was called, you know, stability, stable by default. We could just rename this OTEP to be graduation criteria, and it might be a little bit more accurate as to where this work came from, because it was really some horse trading between us and the feedback we were getting from the CMCF and our end users and elsewhere about, you know, what things they wanted to see to declare OpenTelemetry stable and graduated and all of that.
So that's where these work streams came from. The problem, of course, is it's such a big pile of stuff that trying to actually, like, go to the next step of, like, what are we gonna do about it? It's too big of… a high-level document, to work on that front. So what we're doing now is trying to break this down, into smaller parts.
And the first question is, you know, the work streams that we've identified are they the right work streams? So I think we can go through these work streams maybe as the next step, and just talk about them. Does that make sense to you, Lyudmila, or are there other kind of high-level things you wanted, to discuss in this meeting?
Liudmila Molkova 00:34:53 That's exactly what I wanted to talk about, like, if we restructure the sub, then how do we restructure it?
Ted Young 00:34:59 Right.
I think what we can do is… is mostly leave this OTEP as… as is, as a high-level doc, but… and then we need to sort of move on from it into the lower-level things, but to review these work streams, some of them are sort of like… not… I wouldn't call them nothing burgers, but I would say some of these are things that heavily involve like, a lot of effort across the project, and some of these are more isolated, to individual SIGs.
So, let's start with, the top, experimental features, right? One of the things we got feedback about is it's hard to tell what's stable and what's genuinely experimental versus just hasn't been marked stable.
In practice, I think we do a good job of keeping the genuinely unstable experimental stuff away from the production-ready stuff.
I would actually propose we could eliminate this work stream, because when I look at the problem, it's less about we don't have the ability to keep the experimental things in a box, it's more that we have all of this de facto stable stuff.
So I would propose that if we actually Burn through getting the de facto stable things officially stable.
the resulting clarity, it would be obvious, then, what was actually experimental. And we already have ways of, of… Defining and indicating these to people with, you know, version numbers and config and things like that.
So, I'm curious if anyone has a different take on that particular issue, if they see bigger issues with… Identifying things as experimental and keeping them away from production, other than getting the de facto stable stuff.
Out of the experimental box.
Jack.
Jack Berg 00:37:01 I think it's actually a child of the third work stream, which is, like, this definition of a distribution, because that's where the rubber meets the road on this, like, in terms of, you know, having common ways to opt in to experimental features. That's not really… that's not really relevant outside of the context of a distribution, because if you're talking about consuming individual components, they're already annotated with you know, their, SEMBER, you know, stability, or, you know, alpha, or whatever development suffix that indicates the level. And so it's only within the context of a distribution that things become, like, hazy. Like, what things are turned on by default?
how do I turn on only the experimental stuff, or only the stable stuff? And we've actually made some progress here. In declarative config, there is, There's, a mechanism to, control the, the… The version of all of your instrumentation.
So there's, like, a common mechanism now to say, hey, for HTTP instrumentation, for database instrumentation, for whatever instrumentation, use this version of semantic conventions, where it's either, like, the latest, or the stable, or, I think there's a couple of other options that, Lyudmela's looking over now, or showing on the screen.
So, there's some progress there. The problems are, is that, like, you know, you know.
Do all distributions, implement declarative config such that they could key off of these properties? And two, what about the things that aren't instrumentation?
Right? Because distributions bundle up things other than instrumentations. You know, exporters, samplers in the context of SDKs, in the context of the collector, all the different components, receivers, processors, exporters.
So yeah, I think there's maybe a little bit more work to do for maybe a toggle in declarative config to turn on or off those other types of components that aren't instrumentation in terms of their stability level, but, yeah, I think this… my major point… my bigger point is that this is, I think, wrapped up with this definition of what a distribution is and how it should behave.
Ted Young 00:39:25 Yeah, I think that's great, and I think something we've learned as we've dug into it is it would be helpful to use… basically use declarative config everywhere as the way that We define and configure things, when it's available as an option, as opposed to having packaging-specific forms of configuration.
For example, when we're looking at the system packaging SIG, it was like, are we, as a system… when you install things on Linux, is there some special way that you're using, you know, the Linux packaging tools to manage this stuff for the SDKs and language instrumentations, or… Can the way that we use the way that we define all of these features, just be declarative config, and it sort of doesn't matter how you got the bits onto the box, whether it was the Kubernetes operator getting the bits onto the box, or Linux package management, or you did it by hand, whatever it is, if… declarative config has a way of managing it, trying to just use that everywhere, because that would give users a more universal experience for how to do this. That doesn't solve all the problems is then the question of, you know, which collector distro do you get, and things like that. But for at least the… the language maintainers, maybe just asking, you know, having this effort be focused on… on getting declarative config everywhere.
possibly be a better way of solving it than trying to push it out into all of the different packaging things we're trying to do. Curious what people think about that.
Liudmila Molkova 00:41:14 I wanted to bring up the discussion we had recently in PythonSig, and Ricardo and Aaron would keep me honest here, but I think there is no common understanding of what distro should be.
Yeah. Which, should it be two different artifacts, one stable, one everything? Should it be one artifact with opt-in flags? What should be included by default, and how? And I think… Yeah. It's… Part of the discussion, what should go in the declarative config?
But the first question should be, what is the distro?
Ted Young 00:41:48 So I… based on talking to people, I think I now want to reverse that. Because when we're talking about the distros, let's just say we're talking about bits. Which bits end up on the box? Like.
Regardless of the thing that installed it, the, you know, if we're gonna say you have a distro, that's just this collection of bits.
It feels like… a better thing, or a thing that's more in line with how software actually works, because how you define that becomes very tied to your distribution mechanism. If you go the declarative config route, you're saying, regardless of what bits are on this box.
What bits are we running?
What bits are we trying to run, what bits are we restricting from being run? And that's where declarative config does its magic. If you're defining these things in declarative config, you're saying, this is what I want. Even if you… even if the, unstable, you know, or experimental instrumentation packages are hanging out here.
I'm telling you don't use them. I'm saying just use these. Or turn off these pieces of instrumentation and turn these other ones on.
So, that might flow back into understanding, like, how we distribute the right bits, but it feels like maybe starting from declarative config and a way to… for the operator or the application developer to define and config what they want going on in their application.
Feels like a better starting point.
For the language, implementations. We can put collector and OB and other things into a different box.
Liudmila Molkova 00:43:37 thinking from the user perspective, like, if I have a Python application, do I care about declarative config? This is what I'm thinking about. No, I think, what should I install, and how should I interact with it through declarative config or not?
So I think for users, it's a very important question.
Ted Young 00:43:59 But I guess what I'm saying is, we can think about defaults in terms of declarative config.
and what do we want the defaults to be around what gets run? And if you think about it that way, then you're not worrying about all these different installation and bit delivery mechanisms.
Right? As soon as you start switching it around and being like, the way we're gonna control what gets run is by restricting what bits get put on the box, that, like, becomes, like, a very big packaging problem.
It's not that we shouldn't maybe follow up as, like, a second step by having, like, you know, some way to be, like, dash stable with things.
But the thing we noticed is, like, how you… how you manage that is very packaging management system specific, right? Like, these different deployment mechanisms all have different ways of allowing you to package things up and flag them.
And if we can maybe just focus on… having, like, what should OpenTelemetry run by default in Python, regardless of which bits are available? Maybe that's… that's a more coherent way to tackle this problem.
Jack Berg 00:45:18 So to put into my own words, it's like, rather than trying to… wrestle with.
the distribution problem of, like, hey, should Python have a distribution of stable stuff, and then a distribution of beta stuff, and then a distribution of beta plus alpha stuff? It's like, Python just has a distribution of all of its stuff that makes sense to, like, logically include. Alpha, beta, or stable.
And, you know, the recommended path to initialize the Python distribution is with declarative config, and when you use declarative config, only the stable stuff is turned on until you explicitly opt in to the unstable stuff, which is already there on the box.
Ted Young 00:46:00 Exactly, exactly. Some… for example, something we see from users is they may want to be selective, right? Like, they… they want… stable instrumentation, but it turns out they're using Library X, and the instrumentation for Library X is, you know, at .8. But they may decide they want to use that.
Anyways, after having taken a look at it. And that would be about, you know, enabling and disabling things in a fine-grained way, which is what you would do in declarative config. So it feels like people would want that.
And we already have, you know, concepts like that in declarative Config.
So in terms of going to the different SDK maintainers in every language, and just trying to normalize how we do it at that level.
Seems like a better first step. Later, we could look at people who are, like, have security issues where they're saying, no, we can't have the bits on the machine at all.
The bits can never be on the machine, because that would be bad, and maybe providing Different packages for them.
But if it doesn't matter which bits are on the machine, because you're controlling it through declarative config.
I think that actually solves the stability and security concerns for most of our users.
And it also allows each SDK, each language implementation, to just sort of work through how they manage these things, with declarative config, rather than having to get tied up in 3 or 4 different distribution mechanisms.
Daniel Dyla (Dynatrace) 00:47:37 There are definitely, like, supply chain security concerns, though, because JavaScript and other languages have, like, post-installation hooks that can run code and stuff like that, and if we're installing instrumentations that have any dependencies. We really need to worry about that.
Obviously, that's not… whether they're stable or unstable is not a huge difference there.
Ted Young 00:48:08 Yeah, yeah, I think that gets into, like, our security supply chain… you know, issues, right? Like, I think it's a mistake to assume that the things that have been accepted into Contrib but are unstable are… more of a security risk than the things that are marked as stable. Like, the security risk is someone's able to slip something in at a later date that we didn't catch at an earlier date.
So they seem a little decoupled from each other. Like, stability is more about, will this blow up, in production because the code has a bug in it, or, you know, break in some way?
Which is a little bit separate from how good is our security, and, like, how much is this project working to protect itself.
As being a source of supply chain issues.
So I don't know that we would want to combine those two things, security and stability. I'm curious if other people feel that way, or if they think they are more linked.
Daniel Dyla (Dynatrace) 00:49:15 I think the only point that I was trying to make is that a lot of these contrib packages get less… attention… When they get added, and their dependencies may not be as, thoroughly vetted.
Ted Young 00:49:30 No.
So I think that leads to, a separate, work stream, right? There's, like, experimental features and opting in and opting out, but there's also… actually, and this is where I think we may need to rewrite these work streams, like, our biggest challenge in terms of the amount of labor involved is how do we start managing contribib, specifically instrumentation, going forwards?
And I see there's some stuff in the chat going on, so sorry if I'm skipping over that.
But… the way we've been managing Contrib in general is that's just the community manages it, right? Like, we've accepted a bunch of instrumentation packages from various sources. They have various degrees of you know, maintainer attention, but if something's not getting the attention, and someone wants it in the community, then they can… it's open source, they can pick up a shovel and work on it if they want. It's not the SDK maintainer's responsibility to also maintain all of Contrib.
And that's, like, a typical open-source way of managing a wider ecosystem.
I think the problem, though, with OpenTelemetry is OpenTelemetry is basically only as good as its instrumentation.
Right? Like, if we aren't providing high-quality, safe, secure instrumentation for the software that people… that most people are running, then OpenTelemetry isn't useful in production, regardless of how stable the SDKs are.
So… but at the same time, we can't just snap our fingers and ask SDK maintainers to take on a whole bunch of extra work.
So this actually feels like the biggest challenge out of all of the stability stuff that I've seen so far, is sort of retooling how we approach managing instrumentation in general.
Lyudmilla?
Liudmila Molkova 00:51:44 Yeah, I think some languages, have some good approaches there that maybe we can, Please document and recommend. I don't know how much we can align, but I think Jack mentioned how Java works, and that Java instrumentation is a list of good things, and the contrape is… somewhat, bag of things.
some things.
And we can… learn from each other. I think of Java, if we identify in some languages that think they figured it out.
If we compare this, and we, document this as a recommendation, it would be tremendously helpful to other languages who are struggling with managing contribib.
Jack Berg 00:52:32 Yeah, the distinction in Java… so there's a couple of things that Java instrumentation does well, and I'm not, like, patting my own back here, because I'm not involved in Java instrumentation. I'm just, like, aware of it. It's Trask and Lori and a bunch of other folks that have, you know, been the masterminds over there, but they, the two maintainers and a couple of approvers, managed to keep a handle on an ecosystem of, I think, approaching 200.
distinct instrumentation libraries. It's amazing. And they do this through, you know, a ton of tooling to standardize abstractions for adding those instrumentations, to standardize the testing and verification processes for those verifications, to standardize the documentation of those instrumentation modules.
And so I think… You know, and just, like, you know, the difference between Java instrumentation and Java Contrib is that Contrib is where we put stuff that one of the Java instrumentation maintainers was unwilling to sponsor, so… but they're willing to sponsor a lot, because they've, like, invested in the tooling to be able to handle a lot. It's just, like, for some reason, they're just conceptually disaligned with something in Contrib.
And so, yeah, I don't want to undersell just, like, or discount, you know.
what we can do if we kind of set our minds to managing more, to using tooling, to using, you know, these new tools like GenAI to help us with some of these tasks, or to help us write the tooling that allows us to manage more.
Yeah, I'm really just perpetually amazed at the people in Java instrumentation, so I think we can do that elsewhere.
Ted Young 00:54:11 Yeah, and I would love to focus on that. We've also, in the meantime, through Weaver, like semantic convention tooling, I feel like there's better tooling available now. Also, you know, AI coding, you know, shenanigans and things of that nature, and then potentially testing as well.
if… what I'm wondering is if we can start by basically taking the best practices from Java instrumentation, seeing how much of that we can automate using the new tooling that we have.
And then presenting that to the different language ecosystems. So, you know, the intimidation is it's hard to figure out how to manage it, and it seems like it's a lot of labor and time to manage it. And if we can show… Like, a more consistent way of doing it that's also really reduced the amount of labor involved, because the problem is very constrained.
That would potentially open the door to actually being able to… maybe not everything in Contrib in every language, but, like, what we're doing in Java instrumentation. Take the bulk of the stuff that's heavily used and moving it into this more managed zone.
And it feels to me that talking about stability and packaging for the language SIGs, like, it's almost like there's no point in talking about that until we've solved that problem, because right now, everything is marked as, you know, beta.
And, if we want to just bump it to 1.0 like we were initially talking about, the question immediately becomes, well, who's bumping these things to 1.0 and declaring them stable?
So until we solve that problem, I don't know that we need to be worrying about how we package these, these bits up for the language sigs, other than having a generic package. We can talk about this in terms of, like.
Hector and other things, but… But we… we need to get a… we need to wrangle Contrib in these.
Liudmila Molkova 00:56:20 Different languages for explore.
Ted Young 00:56:21 We just don't have anything that's actually stable.
Liudmila Molkova 00:56:24 We slowly eat?
Ted Young 00:56:26 Yeah.
Yeah, I think…
Liudmila Molkova 00:56:28 We, have 7 minutes left. We only have FYA topics from Robert, but I don't know if we can discuss without him.
The… what are our next steps here?
Ted Young 00:56:44 So, what I would like to do… I think this is what… so far, I've identified as, like, the biggest challenge in all of this stability efforts. A lot of the other things, if you look at them, are a little more isolated.
Or if they do touch all of the SIGs, it's just part of a generic work stream. It's really, like, how do we manage instrumentation in a way where we can provide some guarantees for it, rather than it just being con… community-managed, that seems to be the biggest challenge out of all of this stable-by-default graduation work. So I think that needs to get pulled out.
into its own OTEP.
It's… that's… that's a much larger problem, and then everything else is a little more isolated.
So, I can start working on rewriting this OTEP to reflect that as a next step.
And then next week, we can maybe spend some time going through the other items, in this list.
Cool.
Liudmila Molkova 00:57:55 Sounds great!
Thank you.
Do we have any… anybody interested in the last questions on the stability by default?
Okay, so then, let's see what Robert left us with.
non-ATL cure presentation guidance, nest of any value. Oh, it's essentially… has the approvals.
And… no rejections.
Jack Berg 00:58:39 Before… before we merge this, I… I wanna… I wanna loop Trask in for… to this, and just make sure that this passes his sniff test, because he did some thinking about this, with respect to Java a bit ago. So, I'm gonna… I'm gonna ping him on this, just don't merge right away, is my ask.
Liudmila Molkova 00:59:00 Prime?
Cool, and we'll have a meeting with him and Robert later today on logs, so I'll try to bring it up there.
And the other one… it's related.
And it's probably the same.
ask to wait for Trusk.
Jack Berg 00:59:23 He, he… He's put the most thought about About this.
in OpenTelemetry Java, so I just want to get his… I just want to make sure he doesn't see anything that's blocking, like… Doesn't necessarily have to be, you know, perfectly aligned, but as long as he's, like, neutral or positive about it.
Liudmila Molkova 00:59:57 Cool, so then let's take it offline. You'll pin Trask, if we have a call with Robert and Trask, we'll probably discuss it there.
And that brings us to the end of our agenda.
Thank you, everybody.
See you next time.
Jack Berg 01:00:17 Yeah, thanks.
Reiley 01:00:18 Thank you.
Riccardo Magliocchetti 01:00:18 Thanks.
Carlos Alberto Cortez 01:00:20 See you.
