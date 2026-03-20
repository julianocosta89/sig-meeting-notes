SIG: Profiling WG
Date: 2026-03-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Ivo Anjo 00:02:16 Hello?
Frederic Branczyk 00:02:18 Hello, hello!
Christos Kalkanis 00:02:24 Hello.
Just a heads up to people, I have some folks here doing electrical work, and I may need to drop, because they will ask me to shut down the power.
If it's not a problem, Felix, maybe I could go first with the updates for the commentation?
Felix Geisendörfer 00:04:05 Yeah, we can, we can definitely do that, so maybe we'll just get started now before you lose power. Let me share my screen.
Christos Kalkanis 00:04:14 I'm sorry, okay, let's do that outside, but I will let you know, you know, it may be… it may be that, yeah.
You know, the cabinet.
Felix Geisendörfer 00:04:20 Cheers!
Christos Kalkanis 00:04:21 I have to disconnect.
Felix Geisendörfer 00:04:23 It's totally fine, don't worry. Let's see… Share my screen, can everybody see this?
Hey, I already populated the, things from the previous action items, so I'm just gonna move this to the top here.
And, Christos, I'll let you take it away?
Christos Kalkanis 00:04:52 So, yeah, I opened the data model pulley requested data as part of the OpenTeLander specification. There was supposed to be a link there, maybe it got cut off during the copy-paste.
Felix Geisendörfer 00:05:02 Yeah, that's true.
Christos Kalkanis 00:05:03 It should be there, yeah.
So that concludes all the planning work that we had for AppStream documentation. The data model is the, you know, the more meaty pull request, and the more important one, I would say.
So please take a look, and review it. I'll let some review comments myself.
Just explaining some decisions that I took.
Like, one of those is… I took some parts from the old profiling OTEP data model, that we first did, that was years ago.
But decided to leave most of the historical information out of the current data model for two reasons. One is because This is a technical document. Technical documents, by their very nature, don't typically read well, so we want to… You know, keep people's focus and attention on the specifics, technical specifics of the current data model, and try not to detract from that.
So then, if we do want historical information, I think it's best we create a separate document, a data model appendix, which is what some of the other signals are doing, and then there we can go into more detail explaining why we made the decisions that we did.
And maybe link the benchmarks, and so on.
So… Yeah, what you're seeing now is currently… it's fully focused on explaining the current data model from an implementation point of view, and trying to outline The, maybe, areas of the specification that we differ, and so on.
Felix Geisendörfer 00:06:42 Oh, looks nice.
I'll try to review ASAP.
Any… anybody got… Get some immediate thoughts, or… Christos Kalkanis 00:06:56 So, there are two open pulley requests currently, both in the review, right? So there is this data model that I opened today, and there was an older one that already has multiple approvals, so that was kind of the general profile specification page that gives the context and links, then, to parts of the specification. Yeah, so that's this one.
So previously I had asked not to merge this, because it links to the data model, and the data model wasn't yet ready, but now that the data model pull request is open.
I think we can push to get this merged, and then, yeah, focus on reviewing and managing the model.
Felix Geisendörfer 00:07:34 I guess this needs at least, one, maybe two TC refers?
Christos Kalkanis 00:07:40 Yeah, I saw Tigran, he's already assigned it to himself. I also pinged him.
Yeah, I think we don't need to get those merged this week, but it would be great if they were merged before the… your, and Florence presentation.
Felix Geisendörfer 00:07:55 Yeah.
Yeah, yeah, I agree. So let's, I think this one… If someone wants to add another review, but I think we have three reviews from the SICK here, which is good. I think most of the effort should be focused on the data model one, where we need, really any, SICK approvals, and once we have a few, hopefully the TC will follow.
Well, thank you so much for all the work on this, Christos.
Yeah.
Yeah, if anybody has… Anything to add, or should we move on?
No, it's going twice. I have one small announcement. I have to drop early today because of a call I couldn't reschedule, so at the 30-minute mark, I hope a brave volunteer will emerge, who will take over.
But I think we have a few nice people here who could do that.
Meanwhile, I will continue my duties and see if Alexei's here already.
Alexey A 00:08:58 Yes.
Felix Geisendörfer 00:09:00 Cool, and maybe you can just… I think I know the status, but you can, for the rest of the group, you can update a little bit about the blog post is.
Alexey A 00:09:08 Yeah, the blog post is reviewed, and I think it was approved by, by the OpenTelemTri IOM maintainers, approvers.
I think it's basically ready to be submitted. The only open question is about, like, what the exact timing of Of, like, where DPR should be merged, and there are two aspects to that. One is… This publication system itself supports, there is a date field in metadata.
And I set it to March 26th.
And until that date, the… even, like, if… even if DPR would be merged now, and the website would be published.
the blog post will not be visible until March 26th.
And apparently… and apparently midnight, in… in whatever time zone, right?
So, like, basically how to make sure That the blog post is published.
on time is one open question, I think we still need to coordinate on that.
One question is, like, how flexible we are, I think, Felix, I think getting it, like, published exactly… like, the more narrow we want the window to be, the more unlikely that to happen, I would put it this way.
Felix Geisendörfer 00:10:35 Yeah.
Damien Mathieu 00:10:36 I think we should expect a window tomorrow, as mentioned. And as was mentioned before, they really are not used to shipping things earlier, and that's just, like, redeploying.
I think nagging folks on Slack a couple hours before, so that they're aware that we're going to need that to be done, and not just last minute, to ensure that we have someone, like, within a couple hours.
Alexey A 00:11:06 Sorry, sir, sorry, there's a lot of background noise.
Damien Mathieu 00:11:09 Yeah, sorry, my bad.
Yeah, I'm saying basically nagging people so that they, can push the merge button.
Within a 2-hours window right here.
Felix Geisendörfer 00:11:23 Yeah, so I still have some small hopes that since Tiffany mentioned that she's going to be at KubeCon, that we can just get her to join the talk and, like, press a button, because I think the merge button, like, would kick off the automated publishing, right?
But if she's not up for that, then as far as I'm concerned, we can just publish it on midnight of the day. I don't think it's… like, basically, it's already ready in the morning.
I think that would also be okay.
I don't know how people feel.
We did, however, like, Florian and I rehearsed the slides this morning. We did have a nice launch button, if we have the chance for somebody to press it, so that would be nice, but… Seems like… seems like we might not have anybody who can operate the patent, so we'll see.
Alexey A 00:12:09 Should… should that slide say Profiles Alpha?
Felix Geisendörfer 00:12:14 I can… I can ask Gemini to fix that.
Alexey A 00:12:19 No, no, no, I meant the… I meant the text, the title at the top.
Felix Geisendörfer 00:12:24 Oh, the… this, sure.
let's be consistent. I think we might have to update some other slides there as well, but yeah, good point, thanks.
But yeah, let's see what Tiffany replies. If she's like, it's going to be difficult, then maybe you can just schedule it to be published the morning off automatically, get it merged in, and we'll just accept that. I think that would be fine as far as I'm concerned. Anybody feel like it's… I don't see huge value in it being, like, 2 hours versus, like, 8 hours before. I think it's all the same to me at that point.
Alexey A 00:12:58 Yeah, I think it's… I think it's roughly, Felix, you, myself, and Tiffany. I think, like, three of us, we should somehow coordinate.
Yeah, maybe… Maybe I can create, like, a chat for 3 of us.
Or something like that.
Felix Geisendörfer 00:13:22 I mean, we can also wait a little bit to see if Tiffany replies on the GitHub issue, but yeah, let's keep chatting about it. We have until Thursday next week, and if Tiffany is not… Alexey A 00:13:37 Yeah. But I don't.
Felix Geisendörfer 00:13:39 potentially the button.
Alexey A 00:13:40 Yeah, but other than that, the review went smoothly, and, yeah.
Felix Geisendörfer 00:13:47 Yeah, thank you so much for all the work on that. I saw that with a lot of review comments and updates.
I was a little surprised to see the pushback on DeathFiler. I don't think you all are making a lot of money with DeathFiler in the last thing, so I think it'll be fine to have a screenshot in there. But, yeah.
Alexey A 00:14:07 The publishing… the publishing system was surprisingly, like, not surprisingly, but conveniently useful. There's a lot of… there's a lot of, like, checks that… I was just able to run locally, and then, like, when DPR was ready, I think it was, like… I was able to fix a lot of things locally, just because there are all sorts of, like, spell checks and thematic.
Felix Geisendörfer 00:14:30 Thank you.
Alexey A 00:14:30 And things like that.
Felix Geisendörfer 00:14:33 Yeah, no, I think it looks great. Go ahead.
Frederic Branczyk 00:14:36 I didn't see any, like, the comments that you were referring to, but, I'm sure, like, there are other… like, I know that Parka definitely, obviously supports it, but Pyroscope as well. I don't know if people want to, you know, reduce bias there or whatever, if that's something people wanted to… Add, you know, I'm sure every open source profiler would be happy to be on that list.
Felix Geisendörfer 00:15:02 Well, so, with StepFiler, I think, like, the difference is that it's, like, not even, like, a serious backend. I think it's more like a… development and people, but I think the other confusion there was Tiffany was saying that there is a marketing guideline against recommending any backend, and as far as I can tell, that's not true. I read some marketing guidelines, there's nothing in there. There's obviously language that we shouldn't make it seem like there's only one backend, and it's, like, one vendor's effort, that's for sure.
But then there's plenty of examples where backends have actually been shown, and Tiffany was like, oh yeah, but Jaeger is CNCF, but I'm pretty sure that Prometheus and Profana is not, and Profana got an excuse because somebody from I think Splunk was writing the article, and he was, like, clear that all the vendors are fine with defuner, so anyway, I think we just… Frederic Branczyk 00:15:50 Just a quick thing, Prometheus is literally the second CNCF project ever.
Felix Geisendörfer 00:15:54 Oh, sorry, my, my apologies. That was wrong for me.
I had, like, a little conflict with Promises and OpenTelem machine in mind, but I think that's more on the protocol layer.
That is true. That is not the overarching foundation layer, sorry, that's my bad, but I think Krafana screenshots have been shown before, so I think we're not even, like, pushing the limits here of what was acceptable on the block before, as far as I'm concerned.
Alexey A 00:16:20 We have, there's what's Next section, and we mentioned there that, for example, a sync profiler already supports.
Felix Geisendörfer 00:16:30 Yes.
Alexey A 00:16:31 OpenTelementary profiles. So, in that What's Next section, if If more, like, if we want to mention more tools that already added support, we can add that. So… like, anyone feel… yeah, like, we mentioned here, like, we say, like, what you can do, like, a call to community in the bullet list, we say, add OpenTelemetry profiles as an export or receive option in your tool. This is already happening, for example, a sync profiler. We can mention other tools, definitely, here, so… I would say comment on DPR, Frederick, maybe this is to you, like, So you said, like, parkas can be in… like, just drop a comment on the… on the PR.
Felix Geisendörfer 00:17:16 Yeah, I think my only worry would be that, like, if we specifically start, like, listing vendors' support, then maybe Tiffany is pushing against it again, we might lose approval.
And we already have some vendors mentioned here, but I'm fine either way. Like, if we want, we can list, like, go broad and list, like, everybody who's working on supporting it, or we can keep it like we have it right now. I'm fine either way, really.
So I'll just follow the comments on that. Frederick, if you want to, like, add something, then we'll probably add something from our end as well, but… Frederic Branczyk 00:17:52 Just to be clear, though, Parka is an independent open-source project, and there are maintainers of Parka that are not employed by PolarSignals.
Felix Geisendörfer 00:18:00 Yeah, but I think OpenTelemetry's marketing guidelines really don't make a distinction between that and, like, vendors, commercial vendors. And obviously, like, it's still, like, a project that's driven by a company.
But yeah, I can see how it's, like… it is a spectrum, obviously, and it's, like, sitting more towards the open telemetry, open side of things. I do agree with that.
Speaking of, just something, if some… we're doing a demo at KubeCon, and some of it is dev file, or some of it is Datadoc. I would love to show other backends there as well, or have a slide for that.
If anybody's interested, ping me, I can give you the data we're trying to show, so we could show off the actual data, or otherwise we could just, like, drop in a screenshot.
From what it looks like to receive eBPF profiles for second, so we have a balanced presentation of that as well.
That'd be great.
Hmm.
Okay, where were we? Blog post. Any, any more thoughts on blog post?
Okay, sorry, I was just catching up on notes. Then if there's no more things to add here, it can take us to the next item, which… which is integrated with the BPF profiler itself.
Florian Lehner 00:20:06 Yeah, here, it's pending on review.
So, feedback is welcome, once this PR is merged.
We will tag a new path profiler, the… P data, proto stuff, dependencies are already updated.
So, this is, already all in place.
Felix Geisendörfer 00:20:36 Okay, great.
Yeah, I'll take a closer look. It seems like you addressed all the stuff that I was… commenting on, so I think I can probably approve it right after this. But yeah, obviously, everybody who has spent with you.
Anybody's thoughts, questions on this one, or moving on?
going once, going twice. Then Florian has another, PR, to release.
the new… oh, sorry, this is… wait, what did I put here?
Florian Lehner 00:21:15 Yeah, this will just be the tagging, so, my agenda doesn't need to involve a lot of people.
Felix Geisendörfer 00:21:22 I think, yeah, this one, right? Oh, okay, so basically just tagging, okay. Okay.
Okay, cool, very exciting.
Yeah, so right now, just FYI, for the… because this is not quite ready yet, we did the demo this morning, using the V1.9 version of the protocol, which… Would be, I guess, okay, but yeah, if we get some of these things done, we can actually demo with V10 as well. Would be cool.
Okay, if there's no more thoughts here, then Alexi has a few more items that I suspect are probably not… don't have updates.
Alexey A 00:22:12 Yeah, no, no progress on those, yeah.
Felix Geisendörfer 00:22:20 And… And then we are at… Oh yeah, I had an issue on opening a GitHub issue for OTLP support.
or having some kind of referencing, I don't have an update on this yet. I've been thinking about it, and, like, we have, like, a little discussion on… There was actually a link for that.
Yeah, there's a link here. So there's… there's some discussion here, but… Not much has happened yet.
I'll just drop that link in here.
Okay, we're doing pretty well for time today. So, Ivo, why don't you talk to us about context sharing for 40 minutes?
Ivo Anjo 00:23:15 No, I… yes, I will try to be, quick as well. So, the good news is we've gotten 3 out of the 4 needed approvals for the OTEP, which I'm hoping it means we're very close.
A few, kind of, questions on that. Florian left a good question, like this one about, like, the protobuf package.
Like, should we, which package should we use for the process context message? Right now, we have… what is the message… the one we have right now? Right now, we put it in under, Sorry.
We put it under OpenTelemetry Proto Common, and Florian was suggesting that we might move this to process context.
Yeah.
I was kind of wondering if folks have, thoughts on this, like, I think the main difference, like, the main difference here is that once, Once people use this proto to generate the… to generate something to parse… to parse.
It's kind of annoying to move packages, so we probably should, like, have one package and not change after this one change, but I think we're still on time to change this, because right now, nobody's kind of pulling from the proto repo.
Florian Lehner 00:24:39 Yeah, when I did review again, sorry for the late comment on this, was like, hey, does it make sense to be in common? As common is usually the package that… where other pro signals pull their messages in, and I think it has the… the complexity size to be an independent package, and I think it would be also make it easier going forward. So, if there will be a change in ProSix context context in this message that might be a breaking change, I think it's easier to have an exception for this package rather than for common.
So, this would be the, the details.
if process context is the perfect name, and I don't know.
If you want to extend on it with the thread context, for example, then process context may be not the best naming.
My idea was just, like, hey, have it in a dedicated, package rather than mixed together with common. That's just an idea. Yeah, I'm curious what, Joshua or Tigran think about this.
If they have any preference on this, but no strong feelings from my side.
Josh Suereth 00:25:57 I'm a bit mixed here. Like, the… we want to dance with two things, right? Sorry, I'm jumping in. The one thing is, this is going to be experimental for a little bit until we stabilize, and so having its own package makes sense. And the other is, you're right, like, right now, resource and things are in common because they're shared across a bunch of different places.
Given that I think that this proto-message is just going to make use of common, and we have other signals in separate packages, I'm inclined to say it's going to be easier for us, with the process and everything, to put it in that V1 experimental package you have, and reference Common.
Just in case there's expansions and things and other things, you know, we could… Make that package be about content which is shared.
Between a process and eBPF technologies?
In general, because I think, Evo, you have another OTEP that expands with more data, right?
Ivo Anjo 00:26:54 Yes, but it adds on this message, but… so it doesn't actually need to change the format yet, but, well, as we evolve on that PR, that might change.
Josh Suereth 00:27:06 Yeah, I guess I just mean the name of it, right? So that we can name it as, like, a signal that is shared between SDKs and external observers of those SDKs. Yeah.
We… we did talk about this in the TC. I don't know if you saw the comment that was added. I think Josh McDonald added it to the OTEP. This is… this is an aside.
One of the things that I want to make sure of with this OTEP, I approved it, and I told the TC, like, I think this is good to go, and good to merge.
And that's why I approved it. The one question they had was, should we get the OB folks to at least approve it as well? Because there was, we checked, and we didn't see anyone involved with OB, actually having… they had commented, and I'm pretty sure you're aligned, because I know you guys are talking all the time.
But we'd like to see the official approval on there before we merge, yeah.
Go ahead, Florian.
Florian Lehner 00:28:01 From the OV part, they are not that much interested in this part of the information sharing. They are more interested in the information sharing on the EVPF map side, and this will not be done via the proto part, so they are more interested in specifying the layout of an EVPF map.
Which then can share spam, trace ID, whatever. So, yeah, I can reach out to them, I'm quite involved in this.
But their focus is not on this topic. They will benefit from this, but, their focus is more for, the, the MBPF map parts.
I think there's also a draft for this… Josh Suereth 00:28:47 That makes sense. I think it'd be… I just want to make sure they know what's going on here, and that they don't build something completely different.
The OTEP says, hey, Obi, if you need this and when you need it, you're going to do it this way, right? Like, this is the way that we're approving for sharing and communicating. So that's all. So, at a minimum, let's just make them aware of it and get them to, like, sign off and say, yep, cool.
Florian Lehner 00:29:15 Cool, yeah, I will reach out to them, yeah, make sure.
Ivo Anjo 00:29:21 Just a quick question, because we mentioned the V1 development package for the… oh, sorry, Alex, I kind of spoke over you.
Alexey A 00:29:32 Hi, sorry, I just raised my hand. Just a quick question, like, should we get some of the… like, at least one… someone from Obi to this meeting going forward?
Josh Suereth 00:29:44 That might be useful.
Yeah, whatever is the best, like, my goal is that this SIG and that SIG have a very healthy communication channel.
I don't care what that is. If that is Slack, if that is GitHub PRs, if that is Evo going back and forth between the two, like, whatever that happens to be, the communication channel has to be helpful. So if you think that you want to invite them here to make sure that it's healthy, great.
Let's do that. Or Florian, yeah. I'm sure that more than one of you are going back and forth between the two, but yeah. Whatever it is to make sure the communication's happening is the important bit, so whatever y'all need.
Alexey A 00:30:30 Yeah, sounds good. Thank you.
Go ahead, Eva.
Ivo Anjo 00:30:35 Yes, so I was going to ask, because we said, like, the V1 development package, so do, for the, so do we… does that mean, like, does that mean we want, like.
context or process context.vone development, or do we mean something else? Because we kind of discussed the, like, the last part of the package, but not the middle part.
Or at least I didn't get it.
Josh Suereth 00:31:03 I'm bad… I'm bad when it comes to bike shedding, because when it comes to names, as long as people understand what your intention is, I… anyway, the community is more strict, so what I would say is think a lot about it.
have a rationale behind it. From my perspective, what I want is… you know how everything has the V1 in it? Keep your V1 development in the place where V1 is, everywhere else it is in OTLP.
And then make sure you have process context somewhere in the name, because I think what we're defining is a process context protocol for how you're going to expose process context via, you know, the mechanism outlined in your OTEP. So, those are the two important things to me to make sure that your name conveys.
The development means we don't have to constantly remind people this is in development and not beta and stable, and then we can follow the process we are doing for the rest of profiling as well to move it into V1 when it goes stable.
Right.
Ivo Anjo 00:32:05 Thank you.
Felix Geisendörfer 00:32:08 As announced at this point, I unfortunately have to drop out, but Ivo, since you're the lucky one whose topic is being discussed right now, I nominate you for continuing the moderation. If you do not want to accept the challenge, you'll have to find somebody else who does.
But meanwhile, thank you, everybody, for all the great work, going into the alpha. I think we're on the home stretch now, and very exciting to… Announce it at KubeCon next week, and see some of you at KubeCon as well. So, awesome! So, I'll give it over to Ivo. See y'all.
Ivo Anjo 00:32:39 I was set up, let me share my screen and pick up where, Wix was living… okay. So, I was set up. So, the, the other quick thing I had was that we now have the PR to add process context, onto the eBPF profiler. This is… this was a draft, it's now been undrafted, and We've already got some good feedback, so if anyone is curious, wants to chime in and, like, add some feedback there, that would be amazing.
And, the next thing I had was that we now have the… we moved, the thread context document that we had to, PR, which is here.
I think what we discussed last week of, leaving this in draft, at least until the process context landed, to make sure that, like, this one depends on that one anyway.
So if that one needs to change, this might need to change, so it kind of makes sense.
And, more from our side, we have, a PR on the eBPF profile to implement it. Oh, go ahead, Alexi.
Alexey A 00:34:06 Quick question on the title of that PR. It says, like, sharing information with eBPF Profiler. How specific do we want this to be? Do we position this, like, as specifically for eBPF Profiler, or do we position this as more, kind of like a more generic protocol?
I wonder, like, for the OTEP, what the name should be, like, should the name be more, kind of like, because I think Josh mentioned, like, oh, we should… we should include Obi Fox as well, but… to include… other folks, do we want to position this OTEP as more… as more general? I'm just curious, what… what kind of… what… what's the framing?
Josh Suereth 00:34:51 I can jump in with some guidance, I think.
So, this is a… there's two ways you can think of this, right? If this is just a communication between you and Obi, and you don't want this to be a specification that folks can depend on.
Outside of the two projects?
You don't need to be in the specification, you don't need an OTEP.
But if this is a thing that we want, like, to answer your question, Alexi, yeah, generally things that are in this OTEP are things that we expect to have the ecosystem engage with. Like, our specification should be all of the language SDKs will engage with this. And so that's your target. My read of your OTEP is that you need the latter.
And so, I do think that what you want to do is frame it as a generic way to expose context to external observers.
And then your primary use case is eBPF, OB, and SDKs, right?
So, that would be, that would be kind of how I'd, update your wording and phrasing.
If you need context for that, you can… the entities one, is a good example of something that everyone was confused about what it was actually trying to solve, and so we have a ginormous section about, like, the use cases, and then we talk about, like, the actual data model we're exposing.
Kind of separately. So the name of it, a lot of people look at the name and don't know what the hell it means, but if you go read through the use cases, it's very concrete of, like, we want to solve A, we want to solve B.
Alexey A 00:36:18 Yeah, and my worry would be that if we frame this too narrowly, then… Like, subsequently.
other parts of the ecosystem could decide, like, oh, I can also have my narrow thing.
And then other participants would have less interest in… yeah, like, you see what I mean? Like, I think, like, if we position it broader, then we can engage with more people from the beginning.
Nayef Ghattas 00:36:52 I think for the process OTEP, we say sharing resource attributes with external readers, and we could probably do the same for the thread level OTEP.
Ivo Anjo 00:37:19 Makes sense. I will, look into plating the title and, looking into the use cases. I think that's a good way of framing it.
Okay, I guess the next, small, the next question we… I kind of had to raise is that.
Since the, the strat context, was kind of, like, derived, a lot, including our… some of our experimental implementations from PolarSignals custom labels, I had one question to kind of ask, like, if people are, anyone has any concerns with us kind of opening a PR that.
imports, this thing into the SQ profiling repo, and then kind of modifies it to match the… to be kind of the reference implementation of the thread context.
To match what… kind of what we had for the process context, where we have, like, the example implementation here, so that people can kind of follow along.
And then we have an OpenTelemetry official spot to have it in, rather than, like, a separate repo.
Frederic Branczyk 00:38:44 I think that's… I think that's fine. Also, I'm… I'm guessing a lot of that question goes to… goes to me, or Polar Signals, but I think… I think that's fine. I think the only thing that I would ask is that, you know, since we did put a lot of work into this, that we're referenced, And that, Brennan and Tommy become maintainers of this.
Florian Lehner 00:39:12 Mmm… maintain might be a problem with Autel, but Codana?
Frederic Branczyk 00:39:17 Okay, I don't know what the right terminology is, but, you know… It would be great if they can… contribute to this.
And maybe even, you know, ideally merge PRs.
Florian Lehner 00:39:31 Contribution can anyone?
Frederic Branczyk 00:39:33 Sorry? Yeah, yeah, of course, everyone can contribute, but I mean, you know, we have full control over this repository today, and it would be great if, you know, when there are bug fixes or whatever needs to happen, that we can actually control that to the same degree that we do today.
Florian Lehner 00:39:49 Yeah, I think it makes sense to… have code owners for this, and name the people that you want to have code owners. At the moment, there are, I think, 4 people that can merge. These are the maintainers, Christos, Felix.
Chris was Felix Jonathan, I think, as well, and Pete from Grafana.
Yup.
Christos Kalkanis 00:40:20 By the way, so SIG profiling is a repository that's meant to not be, I think, the authoritative source of anything that's going to be used in production. It's more like a repository of tooling, benchmarks, things that we refer to, promoters, often design documents, and so on.
So, in that sense, evil… so having Frederick's code there would simplify the… the outer that we're currently discussing, but do you have… do you see this being… Kind of the authoritative source for something else in the future.
Ivo Anjo 00:41:02 I think that's… that's a good question. So I was kind of thinking of it as a bit more… closer to what you were describing, Crystal, like, somewhere where we're putting stuff, because we're kind of evolving it, and so we have, like, a… we change the spec, we change this thing, we change the spec, we change this thing, and we kind of keep them in sync.
I was not thinking of it as the place where things would live after we kind of take them out of half or something like that.
But yeah, I don't have very strong feelings on it.
Frederic Branczyk 00:41:33 Okay, I only care about the long-term thing, wherever it lives.
Ivo Anjo 00:41:48 I guess, so my suggestion is, hmm.
I would kind of, suggest, I will add it there, I will add it in the README, to, like, let me write it down. Add it there, clarify in README that this is just the temporary spot for, while OTEP is in development.
And, is expected to move out once, we retire out of Alpha, or… Or similar.
Does that make sense?
Okay.
Cool. Felix makes this easier. Like, taking notes and talking at the same time is complex. Okay, let me just… So the last tiny item is that we also have a draft PR for the thread context support in the eBPF Profiler.
Since it depends on the process context right now, it kind of duplicates some of the commits. We'll kind of need to keep revising and whatnot.
But… yes, feedback is welcome, and trying it out is welcome.
Okay, so I guess Jonathan is asking if, linking it from where it is, would make sense. We could do that. I think the question is, like, right now.
I guess, like, my version of the way I'm thinking about this is, like, right now, this is something that PolarSignals customers are using, and we are proposing something that is kind of a fork of this, that started from this, but it's different, so… Having it on this repo is actually kind of weird as well, because it's not the thing that is kind of finished that, customers are going to adopt, so that's why I was kind of asking in having somewhere where we have the working version of this fork that evolved, but is still not stabilized.
Jonathan Halliday (IBM) 00:44:20 Yeah, I think forking it only really makes sense if there are going to be changes going into the OTL version that are not going into your own.
Otherwise, I think it makes sense to have one source of truth and just have a pointer to it to say, hey, you might be interested in this thing that's over there.
Ivo Anjo 00:44:38 But I think the point is that, at least… I think… people might not want to adopt the new format while it is, like, work in progress, so it kind of makes sense to have, like, okay, this is… let's call it the stable V1 of this, and then there's the hotel V2 that is.
Jonathan Halliday (IBM) 00:44:56 Well, that's just a tag in the… repo.
You point to the tag, you point to a specific version, and don't bump the pointer until you've got a new stable version.
Ivo Anjo 00:45:06 Yes, I don't… yeah.
Frederic Branczyk 00:45:08 If this makes it easier, I don't know, I think this would also be a bit odd, but we would be fine with contributing this repo, to… to OpenTelemetry, but it's weird because it uses a specification that doesn't exist at the moment, right? At least not in the hotel land.
Jonathan Halliday (IBM) 00:45:26 I mean, part of the reason I'm thinking about doing it this way is that if you… if it does eventually stabilize and you do want to donate it, the process is going to be more like it was for the profiler. There's going to be a kind of formal review of Does Hotel want to adopt this thing?
As part of that, the initial maintainers are… Nominated or set in the same way that the group was for the profiler.
Right now, we don't have any… way of doing that without going through the adoption process. So yeah, we can do code owners, but we can't… Skip the formal… Hotel definition of a, you know, maintainer, which requires that you have a, you know, a history of contributions and whatnot before you're eligible for that status.
Christos Kalkanis 00:46:17 I think, personally, the way I see it is that the version of the Evolve, once you put in seed profiling, is kind of a work in progress.
Changes are probably gonna take place there.
And then, once we coalesce with something that's fixed to the OTEP, and then the OTEP gets accepted.
I think what makes sense then is, yes, what Frederick just described for polar signals to donate their repository to OpenTelemetry, that becomes the authoritative repo. Frederick and his group become maintainers, and then we can all refer to it and use it and promote it and so on.
Jonathan Halliday (IBM) 00:46:56 Yeah, yeah, that makes sense.
Frederic Branczyk 00:47:00 I would be very happy with that. That said, I guess Datadoc needs to be happy with this as well, because effectively, that means that Datadoc is contributing to our repo.
which we're then subsequently donating. I'm cool with this, but, like.
Ivo Anjo 00:47:19 I am cool with, like, doing that and, like, making sure on our side that we're fine. So, yeah.
It's good, it's good as well for me, the plan sounds good.
Okay, so I guess, that takes us into the next topic from Josh.
Possibly raising DC's sponsorship level.
Josh Suereth 00:47:57 Yeah, so this is… this is somewhat new, so apologies if you, aren't aware of, like, what TC sponsorship levels are, but we have 3 different levels listed there. One is escalating, where we're here if you have problems, and you let us know if you have a problem, and we'll help you address it in the ecosystem. Two is guiding, where we are active in your SIG, And helping you navigate the landscape.
And deal with issues directly.
And then 3 is where we're actually leading the SIG.
Right? And so, the TC reoriented itself around these kinds of sponsorship levels across OpenTelemetry. We use this a little bit to know when we're overloaded and all that kind of stuff.
What I think is important here is we were treating profiling as an escalating sponsorship, and I think the past month, that's proven that that's no longer okay, and we should move to a guiding level of sponsorship.
Guiding and leading are a bit flexible. It's just basically if the TC happens to be leading it, we want to call that out, and we're limiting how many things TC can lead, to avoid, basically, peanut buttering the community and not being effective.
I want to propose giving you guys guiding sponsorship, where you will have someone in your SIG ready here, helping you get things done, especially given the momentum we have now, the protocol becoming stable, or we want to make sure that there's more active participation.
The nuance of this is, if you move to guiding sponsorship, I think that means I would have to step down, or drop one of my other SIGs, but I think Tigrin can pick up and become that guiding sponsorship.
I need to verify with him. He's not here today, but I'll check with him. I think you guys need guiding sponsorship, and I want to kind of propose this with the GC and the TC. But I wanted to check with the SIG first, and kind of get a pulse check of how this is going. I would be doing this on your behalf, but if you don't want it.
Then I shouldn't, right? But effectively, how much TC involvement would you appreciate? Would you want us to try to escalate your sponsorship level to get more active engagement?
Christos Kalkanis 00:50:08 Yeah, that sounds good to me, especially since we have the momentum. We probably will need that guidance ASAP. Like, what we don't want to happen is to, you know, lose the momentum that we have. There are important aspects of the profiling signal that we haven't yet started working on. Symbolization is one of them. We're going to need help across the board to get consensus.
So, yeah, it makes perfect sense.
Alexey A 00:50:39 Yeah, I think, I think this sounds good.
I… one thing, like, this is more of, kind of like, how will… exactly will this work, kind of, thoughts or question.
Like, if this… let's say Tigran, for example. Like, Tigran attends every meeting, but maybe not every meeting has something for… that needs kind of like a TC sponsor to pay attention to, like… like, is this more, like, case by case, or is this continuously, and what if they get bored? That… I'm just thinking of that sort of things.
Josh Suereth 00:51:16 Yeah, so the idea behind sponsorship is that we can change the required level over time. In terms of attendance to the meeting, it's not, Guiding doesn't mean you have to attend every meeting, like, we need to take vacations, you get sick, you might have something at work that's a little stressful you have to deal with one-off. It means that they should be a regular attender, not every single meeting is a requirement. Does that make sense?
Alexey A 00:51:42 Yeah, absolutely. Yeah, yeah, that, that makes sense. And also from, like, from the effectiveness, this probably goes without saying, but from the effectiveness point of view, one thing I don't want is become on the, like, become continuously depending on the decision-making from the given TC member, but then I don't get their attention, and, like, and, like, PRs get gusted and things like that, like.
It just needs… it needs to be effective, also.
Josh Suereth 00:52:09 Yeah, yeah, and that's… that's actually good feedback for… I don't know if you all, I think Morgan is your GC sponsor. I don't know how often you're getting those check-ins, but that is feedback we want to get through that… that check-in should be, like, a combined TC and GC.
check-in every month that you're getting with the governance committee and with the technical committee, and that's feedback we want you to provide there. Like, there's… and if you need to do it privately.
you can reach out to the TC member directly in Slack, or you can reach out to the governance committee member if you're uncomfortable. But that is feedback we want, because again, the whole idea behind this is, is, about a year ago.
we started down a whole TC recharger.
to try to get the TC to be more active, more engaged across the ecosystem, and make it clear what we do, and when to escalate, when not to escalate. We ran into a bunch of frictional points, which I think this SIG experienced one of those. So, the idea here is that we're trying to kind of be… ahead and abreast of what's going in OpenTelemetry. Guiding is not supposed to be, like, we're the only ones who can make a decision as well. One of our goals is to increase leadership through OTEL, so hopefully as the SIG graduates, a few of you will also grow in your positions across all of OTEL. Some of these decisions you're making between OB and, and profiling, some of the decisions you're making between SDKs and profiling.
could lead to other positions of authority within the ecosystem, right? So, we're trying to do… we're trying to basically improve the health of OpenTelemetry leadership.
This is one of those aspects of that.
this is me trying to leverage it, of like, I honestly think you guys need more attention from the TC. We did some minor escalations to do so for… prior to KubeCon. I don't know if I can sustain it if I'm still leading semantic conventions and entities at the same time.
Like, effectively, we limited the TC to two things, to try to avoid peanut buttering and not being able to give you enough attention. And just frankly, I don't know if I can give you the attention you deserve. So, that's why I want to upgrade you to guiding, and then we can start having hard discussions of, okay.
maybe we have to shuffle leadership around on SIGs to make this happen.
So, I'd like to kick that off if you're all amenable, but just as a thing, I briefly mentioned it to the TC, I think Tigran was on board. I wanted to check with everyone here and give you an idea what it means. There was a question, or a hand, go ahead.
Florian Lehner 00:54:38 Not a question, but more feedback. Yeah, I appreciate the step, and I think it's a good step forward, for profiling, in the sense that, the group was floating around a little bit, and we reached out to various TC members, and We did put a lot of work on your plates in the last weeks, I would say, and this is definitely acknowledged. And, having these pre-active guidance will probably help us.
keeping the momentum. With the work EVO and Datadog is doing on process context and thread context and the upcoming work on symbolization, this is needed, and yeah, I think it will be proactively, really much appreciated.
Josh Suereth 00:55:29 Well, this'll be our first time trying it in process, so it might take us a while to figure out what it means and how it all works, but I'll kick that off now.
Ivo Anjo 00:55:52 Okay, please do, kick me, if, or, or, just update the notice. I am, if I am grossly misunder representing what you're saying.
And, any more items for today?
Okay, so I guess everyone… Frederic Branczyk 00:56:15 Actually, I… Ivo Anjo 00:56:16 Well.
Frederic Branczyk 00:56:16 quick thing, I… Ivo Anjo 00:56:18 Go for it.
Frederic Branczyk 00:56:18 Just because I saw a conversation on Slack about this, I just want to make extra sure that I understood it correctly. There's nothing happening anymore that a backend would have to change to support once alpha is, announced, right? Like, there's no change that happens to the APIs or anything like that.
Florian Lehner 00:56:36 If you support Wii 110 already, then Alpha will be fine. There is a breaking change between 1.9 and 110, but if you are past this point, that's fine.
Yeah, that's… that's the point.
Frederic Branczyk 00:56:54 That's how I understood it, but I wanted to make extra sure here, thanks for clarifying.
Nayef Ghattas 00:56:58 Yeah, but for extra clarity, we also said that there might be breaking changes between alpha and beta, or whatever state comes after, that we will bundle and do at the same time in the end.
Frederic Branczyk 00:57:10 Yeah.
Damien Mathieu 00:57:13 I have one last question. We discussed with Lauren about switching the P data, so collector, provides, protocol in the collector, from development to alpha.
We probably think that switching P data to alpha makes sense, because we are switching the protocol to alpha.
So I'm going to make that change, unless there are objections. The question is, do we want, in Collector Core, and I think that only applies to Collector Core, to change everything to alpha as well, instead of development?
So, to be fair, the only thing that changes is documentation.
But I want to go with opinions here.
Florian Lehner 00:58:01 maybe just a personal review, but, I think it's good to change it to alpha. It's just documentation show there, so there's no code change at all, and alpha will maybe motivate more people to give profiles and profiling in general, a go and give it a try. So that's why I would be in favor of changing documentation on the various components that touch profiles in the auto collector core.
Damien Mathieu 00:58:32 I, I think it also kind of says, it's not in development in poor collector, it's Alpha, And if we, like, we could also, like, inspect every component that uses it in Core Collector, but that seems a bit heavy for development to alpha.
And again, this is only for core collector. Anything in country will be staying as it is.
Ivo Anjo 00:59:15 Cool.
So… oh, go ahead.
Damien Mathieu 00:59:18 I guess we can take, lack of response as agreement.
Ivo Anjo 00:59:34 Okay, so I think we're on time to declare victory. I am very excited for next week. It's been a long time in the making, so thanks everyone for all of the amazing work.
And Alexei has last-minute note, Paul?
Alexey A 00:59:50 No, I meant to press an emoji, but… Ivo Anjo 00:59:55 Okay, so yes, thanks everyone, this has been very cool so far, and let's, keep on doing more cool stuff.
Frederic Branczyk 01:00:05 Thanks, everyone. See ya.
Florian Lehner 01:00:07 Thank you for leading the meeting, Yvonne.
And see you next week, everyone who is NQCAN.
