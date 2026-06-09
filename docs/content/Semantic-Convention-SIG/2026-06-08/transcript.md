SIG: Semantic Convention SIG
Date: 2026-06-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Sarah Hsu 00:00:59 Hey, Ross!
Russ Trow (GSF) 00:01:00 Okay.
Hi, Sarah!
Sarah Hsu 00:01:03 No worries.
Jamie Cowan 00:01:14 Hello?
Josh Suereth 00:01:17 Hello?
Russ Trow (GSF) 00:01:19 Okay.
Liudmila Molkova 00:01:47 Hello, hi everyone.
Sven Cowart 00:01:50 Hey.
Good morning, or good afternoon, wherever you are.
Liudmila Molkova 00:01:56 Yeah, no, I know.
Jamie Cowan 00:01:57 Name.
Josh Suereth 00:02:00 It can feel like both, right?
Sven Cowart 00:02:02 Yeah, that's true that.
Sarah Hsu 00:02:06 Can tell from people smiling or not smiling. Smiling towards the end of the day.
Josh Suereth 00:02:13 I wish that were true Alright.
Liudmila Molkova 00:02:32 I… Probably it's my turn to run the call. Give me a sec to…
Josh Suereth 00:02:37 I think I haven't done it in a while, but no, I can do it.
I was, I was actually typing in the notes, so that's my bad. I forgot to present while I was doing that.
Alright.
Cool, I think this is all set up now.
Let's, let's get started.
Is Sylvain here?
No.
Okay.
Oh, can folks read this, by the way? Let's make it bigger.
There, HTT request response body capture arches. Oh, should we do triage first?
We've been doing that, right?
Liudmila Molkova 00:03:29 Yeah.
Josh Suereth 00:03:30 Okay.
Armin (Dynatrace) 00:03:32 Not last week, I think, but usually we do.
Josh Suereth 00:03:37 Okay.
Alright, let's do… Do we have any stability blockers? Do we… we don't have a query for that yet, do we?
Liudmila Molkova 00:03:51 No, I think we don't.
Josh Suereth 00:03:54 We do have, promote process to RC.
in the queue. I saw that this morning. I think this one needs another… No, this one looks ready to be merged. I think I even clicked the merge button, didn't I? No.
Yeah, this one looks ready to merge. Anyone have any… Concerns with this?
Christophe Kamphaus 00:04:19 Which has the question.
For entities, we are moving them towards stability as well.
Josh Suereth 00:04:26 In this one, yes, yeah.
Christophe Kamphaus 00:04:29 Okay, because I remember from way back.
That we said we wouldn't stabilize entities.
Josh Suereth 00:04:37 No, we don't… you don't… we're saying you don't need to stabilize entities.
Christophe Kamphaus 00:04:41 Oh, okay.
Josh Suereth 00:04:42 Yeah, for Kates, there were still some questions around, identifying and descriptive attributes. They're not planning to change the attribute names, but they might change what constitutes identifying descriptive.
So, that was what that exception was about.
Christophe Kamphaus 00:04:59 invoices.
Trask 00:05:00 It's a little confusing that entities aren't stable.
in the spec.
Josh Suereth 00:05:08 Alright, we can… we can work on getting those stable then.
Trask 00:05:11 Yeah.
I'm fine with.
VR, by the way.
Josh Suereth 00:05:17 I mean, so there are some entities which are stable in the spec, and are stable here, just for reference. Service… service is in the spec, and is considered stable.
But that's kind of, like, our hand was forced to some extent, if you remember, like, the specification. Stable parts of the specification relied on service before service was considered stable.
Trask 00:05:39 Yep, it's just as a… instrumentation author. Like, we can't actually do anything about this at this point.
Josh Suereth 00:05:49 Oh, I see. I'll phrase this another way, though, for semantic conventions. If entities never makes it into the SDK spec, it's still useful to model them here.
In the way that we're modeling them.
And we will have Weaver support to, like, verify them with what is already being modeled.
Trask 00:06:07 Okay.
Does that… Makes sense.
Josh Suereth 00:06:09 Yeah.
Trask 00:06:10 Yeah, yeah.
Josh Suereth 00:06:12 Yeah.
So, like, if you want Weaver to actually automatically enforce that these attributes exist on metrics you're producing, these entity annotations need to be included, so… for that reason, I think this makes sense, but I hear what you're saying.
Christophe Kamphaus 00:06:33 I saw one other thing as well in the markdown for the entities registry.
So we still have a big warning. The following registry overview is a work in progress.
Josh Suereth 00:06:45 Oh.
Christophe Kamphaus 00:06:46 Is that something we should update?
Josh Suereth 00:06:49 We… I think we have that for both of our registries, don't we?
Where is… where's the registry entities? Right here.
Christophe Kamphaus 00:06:58 Yeah, is that fine?
Josh Suereth 00:06:59 Yeah, give me the whole thing. Where's the button to give me the whole thing?
This right here, Yeah, I mean, this was, This is actually just about the registry con- like, format changing, so, like, we could change the table if we don't like what the table looks like.
it was almost a cry for help to get people who could make things look prettier work on it, because I think I did the initial version.
So I think we could remove that. Like, I don't think that… if we… if we're comfortable with how this generates and what this looks like.
you know, this particular table, then I think we're fine.
What this is supposed to be about is basically don't rely on this table to look exactly the same way it does today, going forward.
How do you feel, like, do you want to stabilize the… like, do you want to just remove this warning?
Christophe Kamphaus 00:08:00 Yeah, I always think… The mention about relationships and signal associations, I think, makes sense to keep that one.
That's the overview itself, I think we can say it's fine.
Josh Suereth 00:08:14 Okay.
Yep, let's do that.
Do we still have the warning on the attribute registry, too?
Or did that one get removed?
I'm gonna check real quick, even though it's not related.
And we're going down a rabbit hole, so I'm gonna, sorry about that.
Christophe Kamphaus 00:08:35 We have a warning there as well.
Josh Suereth 00:08:38 We have a warning on that one, right?
Come on, not issues… Yeah, so if we look here, and we look under Registry E, I think everything has a warning in this directory. This is automatically created.
Yeah, there's a warning that this is a work in progress.
So, we can probably get rid of, these warnings for now, because I don't think we're gonna get rid of the registries, right? Like, we're… Alright.
We'll add that as a to-do.
Let's go back to triage. We're well over our 7-minute time box.
Because I took way too long, but I think this Promote Processed RC looks ready to merge, it definitely has enough approvals, please take a look.
Oh, looks like it just merged.
I'll mention there's, like, 3 more that I think were ready to be merged, but had conflicts when I looked at them this morning.
Here's an AI usage disclosure. This might be a good one to talk through just briefly, in case folks haven't seen this.
Liudmila Molkova 00:09:50 I think we talked through this, and I think I've got some feedback later in the call that I didn't address.
And I… yeah, I'll get back to it.
Josh Suereth 00:10:00 Okay, so this one's still… I'll move this, then, to… something else, right? Where do we put that?
Liudmila Molkova 00:10:08 I don't know.
It needs work. We don't, we don't have a column for, like, needs work or something.
Josh Suereth 00:10:19 Or, like, waiting for more approval, or whatever. Okay. I'll leave it there for now.
Alright, let's go into the agenda, then. Apologies.
Was a bit slow. But let's get through these, and then we'll go back to triage if we have some time.
Alright, so here is… HP request body capture attributes of PR about this.
I have some context on this. Does anyone else have context that they'd like to talk through?
Liudmila Molkova 00:10:55 So, I think we, had a couple of, rounds on the SPR. I didn't see the last changes, unfortunately.
So… It's a… it's a kind of tricky thing, because we don't know how much of a body, response body, we can capture, so I wanted to make sure That, language there is accurate.
But yeah, I'll just take another look.
Josh Suereth 00:11:28 Okay.
Cool.
this, this does get into… I know there was a proposal a while ago about, Having a way to off-board large attributes into a different, like, reporting system and structure, and have, like, a reference link to them.
I know that that is what we do internally for attributes like this, Does it make sense for… Do we have a stance from semantic conventions on that, where, like, we allow the attribute to be defined, and we expect some other system to handle that?
That, in the future.
Or are you trying to put, like, bounds on it now, you know, in terms of size, in semantic conventions?
Liudmila Molkova 00:12:23 I think there was some proposal here to truncate But I think we discussed that we have a string truncation.
Configurable in the SDK, so this is opt-in.
And I think that currently the shape… in the shape of this PR, it suggests to… just to rely on the SDK attribute valuel lens limit.
In other places, I think in databases, we put some limit on the… some attributes.
Because we expected them to be short.
But… I think we don't have anything generic, like, what do we do? How do we… mark attributes as long.
Or how do we… if we set any configurable options?
in the instrumentations.
Josh Suereth 00:13:18 Right, I'm just worried about death by a thousand cuts here.
Liudmila Molkova 00:13:22 Hmm.
Josh Suereth 00:13:23 That's all.
Liudmila Molkova 00:13:25 So…
Josh Suereth 00:13:25 The more we see things like this, the more we need something more general.
Liudmila Molkova 00:13:32 We can… Come up with an annotation.
That would tell this attribute is expected to be long.
Josh Suereth 00:13:43 I actually like that, because that gives us a lot of flexibility in the future. If we ever get direct SDK support for large attributes or whatever, we could leverage that annotation, but from a semantic invention perspective, we just… we have it documented for people.
Liudmila Molkova 00:14:00 Yeah, let me, create an issue, but also can… can you leave a comment, or I can leave a comment?
Josh Suereth 00:14:08 Yeah, where… where's the best spot to leave a comment with the size restrictions? Should provide… okay, I'll put it here.
Boom.
Christophe Kamphaus 00:14:40 Such a mechanism would be general, so… I guess it would also be useful for other cases, like GenAI, request responses.
Liudmila Molkova 00:14:50 Yep, exactly.
Christophe Kamphaus 00:14:58 We did have a proposal, I think it was a year ago, where we could have a reference So it would not, the value would not be… In the attribute value itself, but it would point to somewhere else.
Liudmila Molkova 00:15:12 Yeah, I think it didn't come through for Gen AI, because… we couldn't decide whether it's an attribute or something within the attribute, in JSON value.
But there was a general proposal To, like, a soft convention that instead of recording an attribute, you can record the same attribute with underscore rough suffix.
And it would mean, in general case, that it's, it's… it's uploaded somewhere else.
Maybe it's a good idea… it's a good example of why we should do this, because For complex attributes, there could be a debate if it's a specific part of the attribute that's uploaded, but for string attributes, in a general case, it seems we need to have this type of convention.
Josh Suereth 00:16:08 Yeah.
Christophe Kamphaus 00:16:10 Yep.
Josh Suereth 00:16:14 Yeah, I think for now, though.
we know there's some hard decisions to make, and until someone drives all those hard decisions, I really love just, let's put annotations on these so we know how big the problem is. We can use that to help figure out when to solve the harder problem, you know?
If we have a thousand of these, I think it's… we should solve it really quickly. If we have five.
It's not quite as bad, but it's starting to get there, you know?
Liudmila Molkova 00:16:41 Yeah, I think it's, it's a handful, yeah.
Josh Suereth 00:16:44 Okay.
Cool. Next… Suggesting a new release, yes, we should cut a release. Christos.
Are you here?
Liudmila Molkova 00:17:00 This month's release will be fun. Well, not fun for… for semantic conventions Fund for people who generate semantic conventions artifacts.
Because we deprecated a bunch of Gen AI stuff.
And it means that the code that they generate will not be broken, but will have a lot of deprecated annotations.
We posted something in the maintainer's channel and in some kind of channel, but that's expected.
We'll provide guidance on how to generate GenAI stuff, but so far, we realized that generating different artifact for GenAI would be helpful, because it's, will be versioned differently.
So we're well… Give people guidance on how to generate an AI, but probably it's a separate artifact.
And in case of Python, we're going to merge it into Gen AI OTLs that we have already.
Josh Suereth 00:18:09 This'll be the real test of how much people like Weaver, I think.
Cool. So… Do you… is the guidance a blocker for the, release?
Liudmila Molkova 00:18:26 No, it's inevitable, right? So people need to do something, extra anyway.
Josh Suereth 00:18:32 Right, and with the deprecation, if I understand correctly, we can just cut a release of Semcov maintainers, and everything should be gravy. It'll just look weird to everybody that all these things are deprecated, and we'll have guidance around what to do. Okay. Should we… we should probably put that in the release notes, right?
Liudmila Molkova 00:18:50 Yes.
Yeah.
Let me send a PR.
Josh Suereth 00:18:55 Okay.
Cool.
Any other questions about the new release? Oh, and who of the SunCom maintainers wants to cut the release this week?
Is this where we all touch our noses and say, not it? Or…
Liudmila Molkova 00:19:14 Okay, since I volunteered just to update the release notes, let me do the release as well.
Josh Suereth 00:19:19 Okay. If that's… if that's too much, don't worry, like, I'm happy to cut a release as well, if needed. Just let me know, okay?
Liudmila Molkova 00:19:28 It shouldn't do that much work, that's fine, thanks.
Josh Suereth 00:19:31 Okay. Oh, related… I think I merged all of the broken links, but just so you know, there were, like, two broken link… PRs. There was one from, Patrice, and another one I think they're both merged, but I know that they were both approved.
So, if you see any other broken links, that might kill our release.
And just ping and chat if you need quick approvals. Alright, next, new working group.
I don't know who added this, but this is fun.
Networking, alright.
Sven Cowart 00:20:05 I don't know if it's necessarily new, but maybe just a revival of the existing network SIG?
I don't know if this was brought up yet in this call last week, but this came about last week at some point in either this call or OBI's call. I don't… I wasn't on those calls, so I'm not sure, but I just wanted to bring it up again to see if there's anything that we need specifically from this group to move forward. I think it makes sense to have a Gigov call on the regularly scheduled network SIG meeting, and… I… I… I need to… I… I just… I'm not convinced that, like, system.network and network both need to exist as areas. Like, it feels like an either-or type of situation, but I think that's, like, some of the details we need to figure out, because there seems to be some uncertainty around where some of these things should even live.
So I just wanted to bring it up again to see if there's anything we need to discuss here regarding that.
And how to move it forward, because everyone seemed like they volunteered, and now it's just sitting there, so I don't want it to die.
Josh Suereth 00:21:12 I'd suggest two things. Well, first of all, I don't know if you're on the OTEL entities discussion chat, but someone was asking about modeling SNMP.
Recently.
Sven Cowart 00:21:21 Oh.
Josh Suereth 00:21:22 And so…
Sven Cowart 00:21:23 our alley.
Josh Suereth 00:21:24 I want to throw them your way, yeah, yeah. Like, I'm happy to support them in entities for how to model the entity piece, but they're like, oh, and what about general SNMP and networking? What's the status on that? I'm like, oh, well… That's harder. Okay. Anyway, so the next step here, first of all, the interest is there, I think it's always been there, and I said this in the entities, chat.
Which is, we need someone who… with some strong leadership, to just go forward, make the proposal, and muscle through all the open source work. Again, this is sweat equity, really, right? Like, there's… There's a lot of people interested, so it's basically taking that, putting the proposal together, getting the people in the room to make decisions.
as you need to move forward. So I would say your notion of what's in scope and out of scope is the most important decisions you're making now. Take that… PR. I know that Brayden is happy to help and sponsor this. I don't know if he's on the call, so don't have me speak for you, but this is from when he and I talked previously.
like… I… make the proposal.
decide what's in scope, decide what your first milestones are gonna be, and then get people to sign up to, like, sponsor the SIG.
And then we can keep making progress. I'm also happy to vicariously sponsor you, I don't think I can be an active participant, but if you have any questions or anything, just ping, because I do think this work needs to happen, I think it's a really important missing part of OTEL, and what we're just looking for is someone who is willing to kind of corral the networking experts, and kind of corral the discussions and make decisions, right?
Sven Cowart 00:22:59 Okay, good. I think it would be great, by the way, for that group to handle anything SNMP-related, and not deal with that in entities that… that's the right move.
Josh Suereth 00:23:11 Yes, yeah, well, we weren't… Entity 6 was not going to be defining semantic conventions for SNMP, but we might help brainstorm with the networking folks what those entities might be. That's fine. But yeah, yeah, I totally agree with you, yeah.
Sven Cowart 00:23:26 Alright, sounds good. I… I can… I… what was unclear about this for me was if I was hoping Braden would be here. I didn't know if he was trying to be the one to push it forward, or more be a sponsor and, like, manage the projects around it, because he has certain rights within the, the, GitHub organization to assign approvers and so on and so forth.
Josh Suereth 00:23:47 I think… does he have an official proposal here?
Sven Cowart 00:23:52 Not really, I don't think.
Liudmila Molkova 00:23:55 I think last week we discussed that we are not sure if we need the full SIG and the full project.
And then maybe we can do the lightweight approver group in semantic conventions.
And I think he was operating under this assumption.
If the scope is big enough, then we can… Ask to send a formal proposal.
Josh Suereth 00:24:23 I think when we look at the scope, that really depends on the scope of things, right? So… If the scope is we're gonna solve these 5 issues, that's one thing, but if the scope is actually, like, we want to start addressing general networking observability, and I think that's where we keep running into some issues, right?
Oh.
Sven Cowart 00:24:43 Just so you know, from our end and my end, when I say our Elastiflow's end, like, we would like to address the larger network problem, right? Like, we have plans to open up S&M… all the SNMP-related semantic conventions necessary, all the SNMP trap-related ones, and all the flow ones, and that's gonna take significantly work. We're working on those proposals right now, but we're not quite there yet where we can add them to this list.
But that's… that's the intention, anyways, because we… I agree that there's a big hole right now in hotel.
Josh Suereth 00:25:18 My expectation is that, we have some problems we know about now, so if we were to think of a SIG, this would be, like, your Phase 1 milestones, right? And maybe SNV traps is Phase 2, maybe Flow is Phase 3, like, it, you know, it depends on how you want to phase it out, and those decisions would need to be made, but I, Yeah, so the Miller folks who were on the previous discussion, sorry if I missed that. What was the rationale behind making this, I still think this is a SEMCOM SIG, not, like, a general-purpose SIG, but what was the rationale behind trying to fit it in this meeting? Was it just, like.
Trask Stalnaker 00:25:51 I don't think we understood the scope, the… how large… the scope is looking larger now than… At least I was thinking last week.
Josh Suereth 00:26:03 Okay.
I do think that if you take the scope of basically what SystemsMCOM needs and eBPF-based instrumentation needs, it isn't super big, but it's still I would say of equivalent size of most of our other sigs.
Even with that reduced scope.
Trask Stalnaker 00:26:29 Yeah, like, I, I… networking is… certainly has a big enough scope. What I didn't understand, was the… how much things that, the ElastaFlow folks had wanted to contribute.
to that. Like, if it was just some small things, or this is looking… more like a, fit… would fit a regular SIG.
Josh Suereth 00:26:59 Yeah.
I do think that we probably want to… we might need to break up networking into smaller pieces.
you know, like, literally modeling SNMP might be an entire focus group.
EVPF-based solutions and doing, like, proxies, that might be a thing that we want to model as, like, an effort as well, you know? So I think, to me, the hardest problem here is figuring out what the initial scope is. I think Braden was really focused on, system… like, the actual system networking monitoring that happens in the collector.
And kind of driving that, and then bridging that gap with eBPF-based instrumentation we have. So… even then, I… Yeah.
I think it's fine to have the SIG embedded in this meeting. We tend not to run out of We tend not to run out of time for the topics we have recently.
But, yeah.
Next step, I would say, let's actually put together what the scope is actually going to be.
very acutely. This is… I think this is a decent scope for, like, Phase 1. If you need more with networking, we can actually put together, like, what Phase 2 and Phase 3 will be in separate proposals, or we could… try to put together the bigger SIG.
if these folks are interested in the larger set of proposals, I think I personally prefer having the long-term ownership of a full SIG here.
for networking. Does that sound reasonable to the other SunConf maintainers?
Liudmila Molkova 00:28:38 Yep.
Josh Suereth 00:28:39 Okay.
just the cost of building a SIG is really expensive, so I think we should pay it once, if we can.
Okay, cool. So, we need to sort out scope.
Phases in Portugal.
No.
Sven Cowart 00:28:57 Josh, I can help with that, by the way. Put together, like, ideas around the future phases.
Josh Suereth 00:29:04 Awesome, yeah, yeah. Please, please do. And, like, comment on the bug, actually. I think, like, let's, let's put our, our, all of our comments… I think you already did. Yep. But let's put our comments and documentation on the bug.
Sven Cowart 00:29:16 Sounds good.
Josh Suereth 00:29:17 Cool.
Sven Cowart 00:29:18 Thank you.
Josh Suereth 00:29:19 Yeah, awesome. It's really exciting to see that starting to make some progress. Alright. Software carbon intensity.
I don't know who added this.
Sarah Hsu 00:29:31 That's me, Jamie, and Ross.
Josh Suereth 00:29:36 Do you want to tell us about it?
Sarah Hsu 00:29:38 Sure, so, so I… I will let Jamie or Ross introduce GSF in a bit, but I can give a quick, quick mini, like, 3-minute pitch on why we put ourselves on the agenda. So, software carbon intensity specification is something that built out of the Green Software Foundation. Green Software Foundation is quite similar to the CNCF, it's under the Nestilinx Foundation umbrella.
and is working with, different members. And again, Jamie and Ross will explain it much better than I do. And I'm Sarah, I'm from Goldman Sachs, I'm an SRE. I… I do talk about Oltao maybe 50 times a day, but more from a user perspective. And I'm also, a green software practitioner, I've been with the GSF, since its funding day 5 years ago, I'm also the co- it's the first time I ever have to do this, can you see?
You can't see it. I've also wrote a book with O'Reilly on building green software.
So it's really about mirroring two of my interests. So, SEI is an ISO standard for measuring a piece of software's carbon.
footprint. And then that's something that's been in ISO standard for a while, and there's loads of different toolings popping around around the world on how to actually measure SCI. And from my day-to-day job, right, I work with OTEL, I deal with telemetry, I'm really seeing a gap. Why am I… why do we not see SCI inside?
hotel ecosystem. So that is sort of the proposal. We're trying to marry the two standards, so bringing the SCR, and SCR has different components, right? You can see, it's, it's, it's, If you scroll down a little bit, you can probably see the formula. SEI includes energy includes hardware, includes operational, includes, like, carbon intensities as well. So, the way that we envision it, we will then hopefully propose Addition to the cementing conventions, with a breakdown of all the different SEI components, and then hopefully an SEI score. And that's sort of the first phase, what we're thinking. And hopefully the second phase, we are then thinking about the instrumentation side of things. We… actually just had a chat, with, Kepler.
one of the maintainers from Kepler, and Kepler is an eBPF way of measuring the energy intensity, so we are hoping, like, Kepler will be a receiver side of things we use, and then OTEL, we will then have, like, a processor to actually calculate the SCS score, and then we will use the off-shell exporter from the ecosystem to export SEI to various different backends. So that's sort of, like, how we envision this. Yeah, that's probably why we wanted to talk to you guys today. We do have chatted with a few different folks from OTEL, and they all suggest we come and talk to you guys.
But yeah, I will let Jamie and Russ talk a little bit more about GSF and how they envision us Working with you guys.
Jamie Cowan 00:32:30 Russ.
this is way beyond my technical pay grade. I understand about 1 in every 7 words that have been said today, but I'm really happy to talk to you a little bit about the GSF, who we are, what we do, SCI, But when it comes to the specificities of OTEL and what we're trying to do, I'm gonna… I'm gonna kindly pass over to Russ to give a high-level overview. However, if any of you want to know… about the GSF, for who we are, what we do, please feel free to raise your hand, and I'll… Bore you to death with it.
But, Russ, I don't know if you want to give a quick high-level overview.
Russ Trow (GSF) 00:33:17 Yeah, absolutely. So, the GSF is… we're a member-led consortium, so we're 60-plus member organizations who all come together primarily for the reason of developing new specifications around environmental impact of software.
And Sarah has been a, sort of, software champion for a few years now, and we're looking at how do we, sort of, drive the adoption of this ISO standard.
So, I'll drop in a link in the chat to… I know there's a previous initiative, within OTEL to integrate sustainability metrics. This was, I think, a couple of years ago now.
And, I think a few of us were involved, aware of that initiative. Unfortunately, that initiative stalled, didn't progress, just of, I guess, delivering, I think. We're now really keen, and we have a group of people who are also very keen on developing these semantic conventions.
And the reason I say we're a member organization is similar to the CNCF setup. We have volunteers who engage with our work, we have a number of organisations on our side who are very keen to see this progressive the SCI be integrated into OpenTelemetry.
So this is it. We spoke to, Dan from New Relic, who I think was previously on the governing board, Photo, we spoke to Mike Goldworth, from Honey Badger.
Jamie Cowan 00:34:40 I need to go ahead.
Russ Trow (GSF) 00:34:40 And as Steve said, we wanted to come and speak to you about how do we progress this? How do we go about initiating a project to develop these semantic conventions. We've got people on our side who are very keen to do this, we have a process That sort of allows us to develop specifications and standards very quickly. So we're looking for what might be the starting point. Is there still appetite within hotel, within, sort of, this area, for doing something around sustainability? And if so, where do we start on collaborating?
Josh Suereth 00:35:16 Take a crack first, if that's alright, with everyone else. So, is it that, in terms of appetite, we have lots of appetite for various things. I guess the question I would have would be, if you're defining new metrics, one thing that we're trying to do at semantic conventions is provide instrumentation where folks can kind of leverage them initially. And so we're trying to tie a lot of our semantic conventions to actual instrumentation that produces them, so that people can try them out, and we make sure we're solving real-life use cases and all that kind of stuff. So, my question to you would be, how much of our existing instrumentation are you planning to reuse, and how much do you need to build that's, like, fresh and brand new, and, like, you know, that you're bringing with you? If you're bringing a lot with you, and it's a lot of new.
That's a much easier thing for us to take in. If you're taking our existing stuff and using it mostly as is, that's also pretty easy. If you need to significantly change where things are today, it's just a question of, can we get you hooked into the right places to make those changes? But if you're asking for us to make a lot of changes without a lot of additional folks joining, that's where basically things stall, because, it's really hard for us to take on, especially with a volunteer, you know, open source group, it's hard to take on work that you're not anticipating, if that makes sense. So that's… anyway, feel free to answer. It was, like, 5 questions in one, but feel free to answer.
Sarah Hsu 00:36:42 Ross, which one you want to take, and which one…
Russ Trow (GSF) 00:36:45 I'll start with the volunteers and the process, and I'll let you do the technical, if that's okay. So, yes, totally agree, because we operate under the same model. We are a member organization, everybody… all our work is supported by the volunteers.
We've developed a, sort of, a methodology for helping organizations and groups of people reach consensus.
So, we develop standards, what we say, quickly, at quality. So, we develop an ISO standard within… what do you want to say, Jamie? It's like, within… was it 3 years? I think we went from a blank sheet of paper to an ISO standard, which is unbelievably fast. It doesn't sound like it.
But it's unbelievably fast, and so we are geared up for developing things quickly from a diverse audience, where people have day jobs and are time poor.
So we are going to… we are proposing to apply that process to developing this. So we'd run the project, essentially, within the GSF, so develop the semantic conventions using our… our process, but that would be open to all.
So, Sarah mentioned some of the people we've had conversations with at the moment. It would be an open invitation to anybody who is interested, does have some enthusiasm for this area to engage with our process to develop these semantic conventions. So we want to, I guess.
Reduce the burden on you, obviously, to do that initial development, given you've already got plans, you've already got a roadmap, already got a lot going on.
we were very conscious of that and seeing how we can do the bulk of the work and produce something that we can go, hey, look, we've put in all this effort, we've produced something, now how do we go about integrating? I think that… I think we recognise that's probably going to be the most… most effective way of doing this.
Sarah, do you want to talk to the…
Sarah Hsu 00:38:28 Yes.
Russ Trow (GSF) 00:38:28 Later, because I think it's all about proxies and lacks of disclosure, I guess.
Sarah Hsu 00:38:33 Yes, so, really good questions in terms of, like, how we envision instrumentation. I do want to say I don't know whether everything I say is going to be 100% truth. I should have done a little bit more homework, but I didn't.
So I think, again, that SEI made a lot of different things, right? There's the, the carbon intensity data, we need the energy data, and we need hardware data. So I envision that maybe, energy data and hardware data, that's something we can use out of the box from the OpenTelemetry ecosystem already, but, carbon intensity data, maybe that's a receiver that we will have to build from scratch. So it's quite composite.
And maybe when we have a little bit more different, a bigger group, we can then decide, hey, actually, we also need to have instrumentation there, to prove the usefulness of integrating SEI into OpenTelemetry. Maybe we'll then… why don't we do… carbon intensity first, and then we move on to hardware, and we move on to, energy, instead of, like, doing all the cementing conventions first, and then doing instrumentation. So, I guess there's a few different ways of doing it, and I think it's probably a combination of what you suggested, Josh, but I think it really largely depends on, like.
Which one we decided to pick as a group, if that makes sense.
Josh Suereth 00:39:49 Yeah, absolutely, absolutely. I just… looking at your methodology and things, I'm thinking about how you're going to measure these, and thinking about, you know, are there features you need in OpenSometry to do this, that kind of stuff. Like, I… anyway, super supportive of this. I think this is awesome, and if, like, again.
coming in, focusing on getting, like, you know, actual implementations of this, where we can show people how to onboard quickly and kind of provide, you know, out-of-the-box instrumentation, that's really a focus we have. So, I think you answered all my questions.
Is there anyone else who wants to ask or have any other kind of onboarding things they want to discuss? You know, Ludmela, Trask, I think Armin, and… Kristoff… I think those are our other maintainers here.
Liudmila Molkova 00:40:41 I'm thinking, like, lately, and thanks for the great intro, it's super interesting, and I was also looking into Kepler and open, sorry, open costs, and trying to understand, like, how… how much we can do together. I'm thinking if… We should, have it in the core semantic conventions, or would rather, recommend you folks to create your own registry, because you don't need to be part of this repo to, have a standard, and obviously it would be an easier approach for you to just go ahead and, Come up with something that's, people will use.
Without, like, blocking on us, because we, like, I'm not an expert in the… current software foundation and all the awesome things you're working on, I have no ability to give you good quad reviews, right? But you will be blocked to some extent on my and other maintainers' ability to understand.
If, if you folks are part of this group. So I think it would be awesome, For you to evolve your own registry of semantic conventions, and evolve your own set of instrumentations, and if there are, like, places where we can work together, that would be exciting.
Russ Trow (GSF) 00:42:13 Yeah, wonderful. Yeah, I think this is… that was sort of the feeling we got from speaking to people, because we're… we're going to convene… we've got the SCI experts, we've got the measurement of the environment on our side, and we're trying to find, the people with the hotel expertise for that conversion. How do we transform our formula, our… our attributes into that. And this is… this is the point we're at now, which is there's interest and there's convening these people.
to actually bring that expertise together. But that was sort of the guidance we'd had, was think about how do we do this sort of self-contained piece as well, because we have all the, the infrastructure to do this. We develop standards, we do… we do sort of some of our work out in the open through our public GitHub.
Some of it happens behind closed doors, but we already have all the infrastructure to, to do something like this, I think.
Liudmila Molkova 00:43:05 Awesome.
Josh Suereth 00:43:08 Yeah, so my technical nerdism is basically the R in your equation.
Where you're trying to divide by some rate.
That, I think, is where there's going to be the most amount of overlap with us, because, again, from what I know, you saw the previous attempts at trying to understand carbon emissions and energy consumption. That is probably completely independent instrumentation for what we provide today, and so you guys can race ahead.
Totally. Where you want R is where I think all the fun discussions will occur, where we'll have to be like, hey, let's talk about what we have today, and how you can create R, and how you can divide the data. That's the part that is the most exciting and scary to me at the same time, and, like, this is the right place to come and talk about it. So, like, you know, please come back, but for the, for getting your carbon emission rate and getting that instrumentation out the door, like Ludmila said, Federated SMCOM is going to be the fastest way for you to make that happen.
And if you need an example, we just did it for GenAI instrumentation, which is why our release is weird, which is what we're just talking about. So, you know, if we want to talk about federating so you guys have a place and we can kind of deprecate the existing hardware energy.
things to move into a federated location? Like, that's something we can talk about as well.
Sarah Hsu 00:44:27 One thing, I don't know whether Jamie and Ross wish you also mentioned, last time, the, the previous attempt didn't really go anywhere. I think because it got kicked off over the summer, and, and then sort of, like, it really just fizzled out. So I think Ross, Jamie, and Kosha from GSF is really trying to make sure to kick the assembly, the project off in a right time, so that might be in a few weeks to a few months. So we might be a little bit quieter for a few weeks, and you might not hear from us, but we're hoping to kick things off Very soon, when everyone is back in holiday, and not really, like, mess up anyone's summer holidays.
Josh Suereth 00:45:04 Sounds awesome.
Okay.
So to recap, we're probably going to be looking at a federated proposal.
Please take a look. We actually have, the… there's an OTEP. We're experimenting with this OTEP right now with GenAI SemConv. We're starting to use it more and more. Please take a look at the proposal for what it looks like and kind of the features. If you need an example of how we're actually doing this mechanically, like for the engineers.
Is it OpenTelemetry GenAI SEMCOM? Is that what it is, or Semantic Conventions Gen AI?
What's the name of the book?
Liudmila Molkova 00:45:40 semantic conventions Genie A.
Josh Suereth 00:45:42 So there is semantic conventions, Oh, I put… first put an AI in it. There we go.
This is… this is an example repository where we have things fragmented out, that we're kind of working on.
So this is, like, the place to watch, because this is the template that you would be following to kind of get all of the carbon emission instrumentation kind of, you know, out and defined. There is a corresponding repo for instrumentation, which… I'll have to ask you, Lydmel, what's the name of that one?
I'll put this in the notes.
Liudmila Molkova 00:46:20 Which one?
Trask Stalnaker 00:46:22 Telemetry, Python, Gen AI.
Josh Suereth 00:46:24 It's opentelemetry-python-genai? Okay.
So this is then, OpenTelemetry Python. This is then the corresponding consumer of that semantic convention that gives you Python instrumentation to produce the data.
So, like, if we're taking a similar approach here, we could actually look at doing, you know, have your instrumentation repo and have your semantic convention separate. We could think about having them the same, like, that's an option too, that we can talk about, but basically it's a way to kind of accelerate these things in our ecosystem, so you can move very quickly.
Especially when you get all the right domain experts in the room, and it sounds like you already have all of them in your foundation, so… perfect. Yeah.
Jamie Cowan 00:47:10 We could always use more.
what I would say is, I'm gonna, I'm gonna plug my vested interest. You know, if any of you do know about people that may have a particular interest, please do, you know.
pass them our way, and we can, explain the process, how we work, and get them, hooked into what we call an assembly. This is our process of doing this, so please feel free to, to reach out to myself.
all of ourselves, Sarah, and, we'd be more than happy to, to explain how, And… and when we've got a… finally got a date, when it's kicking off.
Russ Trow (GSF) 00:48:00 Is there, sort of a best way of getting the message out to other people as part of the hotel community? Is there a place we should be raising an issue, or starting a discussion, or… something… I say formal, more formal, just to sort of demonstrate our intent.
Josh Suereth 00:48:21 I think opening… opening an issue in community with the proposal and what you're trying to do is a good way. Like, this… this previous attempt, that's, like, one way that you can attract the attention of, like, people who are really plugged into the OpenTelemetry ecosystem.
so there's two other ways that I'm aware of that I think work. Like, one is we have a Slack channel that you can reach out on,
Russ Trow (GSF) 00:48:44 Yes.
Josh Suereth 00:48:45 a set of Slack channels, so you could actually kind of ping on those, to see if folks are interested that follow that. That's also for people super plugged in. And the last is actually conference talks.
That is your, you know, if you think of a marketing funnel, you know, coming in, conference talks is the big, like, hey.
you know, we're thinking about this, here's all the cool stuff we've done, and we do, like, a bridge talk at, like, an observability section to, like, catch people interested in observability who are interested in the crossover. Then there's, you know, the actual Slack channel chat, and then there's actually the community issue. So, go ahead, Christoph.
Christophe Kamphaus 00:49:22 There's also another one that's, writing a blog post.
We had some, good experience with that in CICDSIC.
That when we kicked off the project, we also wrote a blog post, and we got some new people from that.
Jamie Cowan 00:49:42 Good advice, Crystal. Thank you.
Russ Trow (GSF) 00:49:43 Yeah, thank you.
Josh Suereth 00:49:46 I think there's also… isn't there a podcast now, Trask? Like, the GC and the end user SIG, didn't they start a podcast?
Trask Stalnaker 00:49:53 What's new in Hotel?
Where's a link to that? I don't know.
Josh Suereth 00:50:01 I was interviewed on the podcast to try to advertise Weaver, our, like, semantic convention tool that lets you do federated things. So then we got a little more interest from that, and we have more people paying attention, so that's another option as well. But that's, you know, our broad funnel things are still… they're still a little haphazard, so blog posts, conference talks, podcasts, if there's anything else, we should get you links.
Russ Trow (GSF) 00:50:27 Yeah, brilliant, thank you. Yeah, things we're always familiar with, we have our own podcast, Meetup Program, champion, yeah.
We spoke to, Nikki Man Delucky, who, so there's a… is it FubeCon? FubeCon North America? She recommended, yeah, she's submitting a lightning talk there, as a way of raising, visibility.
Josh Suereth 00:50:51 Yeah, yeah, absolutely. And if you're trying to specifically bridge into observability, like, make sure you propose it for observability days.
Because that's… you get a lot of really dedicated, like, invested people on the observability side at that. Kubecon General, you know, there's obviously more people there, but, you know, if you want to… if you want to, like, bridge into our the people who contribute. Observability days, I think, is pretty powerful.
Russ Trow (GSF) 00:51:16 Great, thank you.
Josh Suereth 00:51:21 Cool.
Trask Stalnaker 00:51:22 Latin?
Josh Suereth 00:51:22 We'll have to know.
Trask Stalnaker 00:51:23 wanted to mention on this topic was that there's two options for federated SEMCOM. One is living within the OpenTelemetry organization, and the other is for living outside of the OpenTelemetry organization.
And so both, the tooling and, you know, the semantic convention ecosystem, the federated concept works equally well, whether it's hosted inside of the org or outside of the org.
In some cases, different things make more sense. In your case, since you already have a… organization, you know, not… You know, that could… may… like, at least you have a place, you have a good place to hold it under your organization and your org's control, and you have, you know, your own governance already. So some of the things about moving it into OpenTelemetry aren't as… Sort of needed.
kind of maps what we're doing with, we're working with the OCSF Cybersecurity Foundation. They have their own Semantic conventions, and they're going to be… they're working on federating, but hosting it within their, foundation themselves.
But I do think all of these, either way you go, all of these things about advertising within the OpenTelemetry community are still beneficial as far as, you know, seeing if you can pull people in.
Russ Trow (GSF) 00:53:07 Yeah, brilliant, thank you. Yeah.
Christophe Kamphaus 00:53:11 or the KubeCon North America Observability Day, just be aware, the call for papers closes on June 21st.
So it's still open, but you don't have much time for that.
Russ Trow (GSF) 00:53:24 Yeah, that was… we had a call earlier today where they flagged up we need to get organized quickly if we want to, try and get involved in that one.
Josh Suereth 00:53:33 Awesome.
Cool. Well, I think that was a great discussion. Thanks for… thanks for joining.
I believe we're out of, things here. We only have about 7 minutes left, so, I'm gonna do one issue triage.
And then call it, because, I'm a little slow in the decision-making, so the triage takes a while. Alright, Cool.
So, I think we have… needs info, we can take a look at those later. Needs triage, let's go through these. I'm gonna start at the one… The ones at the very bottom.
And we'll just take the most recent.
Come on.
New working group networking.
We did just talk about this.
Sven Cowart 00:54:27 A different screen, we don't see it.
Josh Suereth 00:54:31 Oh, oh, oh, hold on. Here we go. New working group networking is in the needs triage thing. This is that issue.
I think… we can accept needsig, or… we discussed today, isn't it alright if I move this into need sig?
This is about producing a SIG, so it's a little awkward and kind of meta.
What do we think?
Liudmila Molkova 00:54:56 Yeah, let's do need SIG.
Josh Suereth 00:55:01 Cool.
Then, let's see… Define VCS span conventions.
Trask Stalnaker 00:55:10 And Sen, all those, things that we talked about for, the GSF? Is that what… did I get the acronym right? apply to… Networking, getting other people interested in networking as well.
Sven Cowart 00:55:30 Oh, yeah. Yeah. We've, actually submitted a ton of CFPs to KubeCon, And other things already.
Josh Suereth 00:55:38 Cool.
Sven Cowart 00:55:40 And.
Trask Stalnaker 00:55:41 Consider a blog post, that's a really for… on the OpenTelemetry blog.
Sven Cowart 00:55:47 Oh, okay, yeah. I would love to do that. That sounds good. We also have a podcast, and we shout you guys out all the time. We don't have a big audience, so, but would be happy to participate in any podcast that's officially CNCF.
Fact.
Josh Suereth 00:56:05 Cool.
Christoph, do you mind.
Christophe Kamphaus 00:56:10 Yeah, just accept it. I will go through the VCS and CICD once.
Josh Suereth 00:56:17 Okay, so this is in progress, and this is, just accepted, right?
Christophe Kamphaus 00:56:21 Boom.
Liudmila Molkova 00:56:22 Oh, by the way, Christoph, I've seen a couple of PRs to move, So I see this stuff to RC? Yay!
Christophe Kamphaus 00:56:31 Yeah.
Liudmila Molkova 00:56:32 I think they were waiting for the codonur's review last time I checked.
Christophe Kamphaus 00:56:36 Yes, and we had one… I saw some notifications today, so I need to follow up on that.
Liudmila Molkova 00:56:44 Awesome.
Josh Suereth 00:56:47 Alright, we'll do one more, and then we'll call it. This is a agent workflow.
It is a GitHubusercontent.com link. These seem shady as hell to me, I'm sorry.
Liudmila Molkova 00:57:02 Yes, I think I even… I'm not sure if I opened it, but it also looked shady to me. Should we just close it?
Josh Suereth 00:57:10 Yeah, like, basically, if you want… To get a feed, Of what's happening.
I'm literally looking at the notes. This doesn't even look like it has anything specific to our repo in it whatsoever.
Yeah.
Feel free to use your… workflow, That's outside the scope of this repository.
Trask Stalnaker 00:57:45 So this, this GHAW, that's… it is a semi-official from GitHub.
Josh Suereth 00:57:53 Yeah.
Trask Stalnaker 00:57:54 actually using it in the Java instrumentation repo, just kind of playing around with it for a couple of… for one thing.
Yeah, it's fine to click on it, it's legit.
Josh Suereth 00:58:09 Do you… I mean, I did, and I was reading through it.
Trask Stalnaker 00:58:11 Oh.
Josh Suereth 00:58:11 Is this something that you think would be useful for us to have? And where does it push the content?
Trask Stalnaker 00:58:17 there's not really enough detail in the issue for it to be useful. It's basically just a generic, very generic… way to run Agentic, like, any kind of agentic workflow, and it's… you actually define your workflow in Markdown.
Instead of YAML, and then you run this tool that generates the YAML, the GitHub YAML, so it's not totally native to GitHub at this point, because you have to run this tool to generate the YAML from the Markdown, which is, I've found, annoying because, the renovate updates the… the real YAML and not the Markdown files, so… Anyway, I… I'm a little cool on bringing this to other repos at this point until I have a better understanding of how to make it work.
Josh Suereth 00:59:15 This is being prototyped… And open syllableTree Java…
Trask Stalnaker 00:59:21 in Dash Instrumentation.
Josh Suereth 00:59:23 Nope.
instrumentation, We're going to… oh gosh, I used a dash. These have entered my everyday right now.
We're gonna hold off on, implementing… This in semantic conventions until, warts.
And rough edges have been sorted out. Okay, does that sound reasonable?
Trask Stalnaker 00:59:51 Yeah.
Josh Suereth 00:59:52 Now, should I leave it open, or just close it?
Trask Stalnaker 00:59:55 I would just close it, because it doesn't have any… it's not really proposing Yeah.
Josh Suereth 01:00:01 Right, like, it's not proposing a specific workflow.
Trask Stalnaker 01:00:04 Yeah.
I mean, kind of, it's, like, once a daily report, but I'm not really… We are, we have a pretty… If you want to go to the GenAI, SEMCOM GenAI Repo?
Josh Suereth 01:00:18 Alright.
Trask Stalnaker 01:00:19 time.
Josh Suereth 01:00:19 Yeah, we're out of time. I actually have to… I have a hard stop, so I gotta go. We can talk about that more. That daily workflows, I have a ton of skills that make me a daily feed of everything from OpenTelemetry, right? Like, I feel like… maybe we make something for OpenTelemetry that does it generally, but I don't feel like there should be a specific per-repo version of this that seems a bit… Crazy to me.
Versus a general skill that people use. Alright, I got you, Jabail. I'll see y'all.
Trask Stalnaker 01:00:47 Bye.
Russ Trow (GSF) 01:00:48 Thanks, Phil.
