SIG: Go SIG
Date: 2025-11-20
Duration: 37 minutes
Zoom Recording URL: https://zoom.us/rec/share/m768H4XkiVNCe1NmOM5SDsDG4OowZhvMmBoTpPwV3N-fxl2Hp685ph7T5NhmLC7h.89X62ieeRaHxYHMW
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:39 Hey, Owen.
**Owen Williams (he/she)** 00:44 Hello.
**Tyler Yahn** 00:45 How's it going?
**Owen Williams (he/she)** 00:46 Pretty good.
**Tyler Yahn** 00:48 Nice.
just getting things loaded up here. But yeah, I don't know how many people are gonna be able to join today. I guess we see Sam. I see Robert's added a bunch of things to the agenda.
Hey, Sam.
**Sam** 01:12 Hey there, though.
**Tyler Yahn** 01:14 going.
**Sam** 01:15 Okay.
**Tyler Yahn** 01:17 Yeah, good. Long time no see.
**Sam** 01:19 Yeah, it's been a while. 2 months, right?
**Tyler Yahn** 01:23 Yeah, I guess it's… yeah. Did you have a good vacation?
**Sam** 01:27 It's basically, kind of, back to China and request a new visa.
**Tyler Yahn** 01:33 Oh. It's been a while.
Yeah, it's, kind of a forced vacation, right? Yeah.
Yeah.
Well, yeah, good to see you. So you're back in, the Bay Area?
**Sam** 01:46 Yeah.
**Tyler Yahn** 01:47 Nice.
Yeah.
Ready to get after it then, huh?
How often do you have to, renew the visa? Is that, like, a 6-month thing?
**Sam** 01:58 Mmm… it really depends. So, based on my visa type, it's kind of like 3 years or 2 years.
**Tyler Yahn** 02:05 Oh, okay, that's, it's way better in 6 months, but still, yeah.
**Sam** 02:11 Yeah, I agree.
**Tyler Yahn** 02:12 Yeah, that would really stink, yeah.
Well, cool, yeah, we can, jump in here in just a second, maybe I'll look on Slack to see if Robert's able to make it. He has a lot of the, Agenda items.
Looks like he might not be able to make it, okay.
Okay, yeah, we can… we can jump in here in just a second, then.
Well, cool. Yeah, if you haven't yet, please go ahead and add your name to the attendees list. If you have agenda items you do want to talk about, go ahead and add them.
To the list, and then we can jump in here.
So the only thing I did want to ask is, our next release. We talked about this last time, we were gonna hold on the 1.0 for the RSC support for OTELConf. It looks like that PR is still in a work in progress. Robert met with Alex Bowden about it, and so it looks like it's making some progress, but yeah, I don't think there's anything… Other than… er, actually, there may be one other thing that I saw. Let's double-check the milestone.
Yeah, so there's this open question here that I think Robert was still planning to work on. I don't know, it was assigned yet. It was assigned to Robert, so that's something he's working on. The OTLConf, we've added it here.
I think that there was a merge of the deprecation of the default client, for OTel HTTP, it's a issue that I think we need to also include, A fix where we're gonna deprecate the post and get functions and that kind of thing.
Right now, the POST and GET functions, you can't… the client that it uses is the default client, and without, some sort of access to it, I think that you may have, like, the functionality here becomes limited.
I don't know why there's not another… Damien just opened another PR for it, let me see if I can find it.
Yeah, here it is.
So, yeah, this, I think, also needs to be included, Okay, so I think those need review, if I'm not mistaken, so that, and then this, PR here, this is something I think you could probably still review at this point, there's been asked to remove things from the API, but I think, like, if you want to take a look and see if there's anything else you can provide feedback on.
In the interim, I think that'd be helpful.
So, yeah, I think that looks good there. Maybe we check, the main repo… Yeah, so this also has observability, work being done here, so there's a self-observability for metrics for OTel GRPC, I haven't seen movement on this one in a while.
There's more here… I thought there was… yeah, okay, there's two more here, I think, that use… Review, this one looks like there's changes requested on it.
Okay, I don't know why that's not loading. Oh, there we go. Okay, so it looks like, yeah, I've asked for some changes.
Wow.
**Alex Boten** 06:42 Hey, can I just, add a quick note about the hotel comp PR that you mentioned.
**Tyler Yahn** 06:48 Oh, sure, yeah, sorry, I didn't see your.
**Alex Boten** 06:49 I joined just as you were, like, scrolling over it, and my only comment on the chat was, please review, but, I talked to Robert about this yesterday, and we, he had agreed on the call that, like, the changes that he requested doesn't have to be in this PR, so we can… We could merge this, because the module will still be at, like, a 0.whatever, version, so… We can…
**Tyler Yahn** 07:13 If we, if we merge this, is the idea to remove these from being exported, and then, like.
cause a breaking change, though?
**Alex Boten** 07:22 Maybe. I mean, the module is not marked as stable at this point anyways, so, it's just implementing an RC, like a release candidate of the schema.
So there's still… there's still going to be breaking changes regardless. The one thing that merging this would allow me to do is to implement it in the collector, because right now, I'm moving the implementation of the collector along through the use of this PR, and that's causing other problems, so, it might unblock me to… Have this thing merge, if at all possible.
**Tyler Yahn** 07:56 Yeah, I definitely like the idea of trying to get this through. I am hesitant to just, add public API that we know that we're going to be removing, like, immediately, is kind of my concern.
And this is the only thing that really is blocking the, the next release, so essentially when this goes in, it's going to get a tagged release at that point.
So, I would say we want to probably… be conservative and remove things that we know we aren't gonna, like, need right off the bat, and then add them, I think, after the fact? Is that something… like, are there… are there… parts of the API here that you need for the collector implementation?
**Alex Boten** 08:33 There is parts of the API that is not stable in the schema, specifically the Prometheus exporter.
Configuration.
That is necessary for the collector to be able to utilize this package. So, one way or the other, we… we're gonna need to have those, experimental APIs included.
I… I haven't solidified how that's going to look like yet, but… Anyways, I'm open to discussing this further on issue. I just wanted to bring it up.
**Tyler Yahn** 09:03 Yeah.
Yeah, is there… so it looks like Robert was saying we could add some sort of, like, option feature here? Is that… Something you want to explore, or is that something you're just planning on going with?
**Alex Boten** 09:17 I… I wanted to explore it. I don't know how feasible it is. So right now, the collector implementation handles the migration from one schema version to another, so that our end users aren't impacted as schema changes.
That currently relies on being able to access the members of the struct directly, so all of the exposed surface area is being utilized.
I started looking at alternatives to doing this, but I… I don't know if I'm gonna be able to get this, like, buttoned up in the next day or two here.
**Tyler Yahn** 09:52 Hmm. Okay.
Yeah, it's kind of unfortunate Robert's not on. I think his input here would be important.
To understand, like.
He said that he wasn't thinking this should block, but I'm also confused why he'd be asking for these changes, then.
**Alex Boten** 10:12 I think… So the way that he explained it to me yesterday, the way I understood what he was asking, was he had these thoughts and he wanted to share them.
Not necessarily to block the effort here, but to… suggest that maybe we can do things in follow-up PRs?
But, like, before we mark this module as, like, a 1.0 module, but we're not anywhere near marking this as a 1.0 module anyway, so…
**Tyler Yahn** 10:40 Yeah.
I do think this is a good time, though, to figure out how we want to support These… these features.
Just given it's… it's, like, it doesn't seem too challenging.
To add an option thing here.
So if you added an option that was like this with experimental features, it would just accept a struct?
**Alex Boten** 11:03 Maybe?
But then, where do you define the struct? And then you still end up having to expose something to the end user.
Of the API, so…
**Tyler Yahn** 11:14 So it's… well… Yeah, that's why I'm kind of confused, because I don't think it really wins you much.
**Alex Boten** 11:23 I don't know that it does after investigating it yesterday for, like, an hour or two, but…
**Tyler Yahn** 11:29 Yeah.
Like, I can definitely see, like, our other pattern where we use, like, environment variables, because it's kind of like, it's magic, right? And, like, it actually… it just skirts, like, stability guarantees, because there's, like… I don't know. It uses an out-of-band way to configure things, right? But I agree with you, like, having an option here, even if it's, like.
what's the thing he's interested in? Yeah, with, like, this instrumentation, like, option? Like, all of these things, it's, like, with instrumentation, so then… like, that's a part of a stable API that you're gonna be releasing, right? Like, you're… that option then becomes cruft if it ever, you know, gets released as stable.
And you have to deprecate it, or something like that, like… Yeah.
Okay.
Yeah, okay, I think I see what you're saying. So, because of that, like, you may not actually be winning anything with this other approach, and so it's more maybe just about, like, thinking through what's provided here, and then going forward with that.
**Alex Boten** 12:30 Yeah.
Yeah, and again, I, you know, happy to get your feedback on the PR, and that's… we can…
**Tyler Yahn** 12:35 Yeah.
I do feel like this is a good situation where you may want to have, like, like, a sub-module called, like, X or something in here that would hold, all of the experimental things that are just… it's just never expected to stabilize.
**Alex Boten** 12:52 Yeah, and this… this would kind of align with the, kind of the general effort in OTEL to disable things that are experimental by default.
So, you know, I could imagine… I can imagine having one option that says, with experimental features, or whatever, like, at the very top level when you're trying to part… unmarshall, the struct, or whatever it is.
That would allow someone to opt in to this, and then, you know, on the collector side, we would just always opt into it, and it would be hidden from end users at that point.
But Yeah, I don't know. There's probably a few ways that we can address it. I think an X module would probably be a good way to go about it, and that way we can have a way to handle it moving forward, because we're gonna keep running into this with the schema, bringing in more experimental stuff, so…
**Tyler Yahn** 13:41 Yeah, okay. So maybe, actually, what… can you create an issue just to track this? I think that that might solve the problem.
And then we can put that in the 140, milestone, essentially. Just saying, like.
re-evaluate the experimental, like, API structure for this, and then we can just say, like, this is how we're gonna do it for now.
**Alex Boten** 14:04 Sure.
That sounds good.
**Tyler Yahn** 14:06 Okay. Yeah, I think that that sounds like a great… Because then we won't lose track of how we want to, like, you know, block on this before we do 1.0, so, yeah.
**Alex Boten** 14:14 Yep.
**Tyler Yahn** 14:16 Okay, cool. And then, so, others on the call, please take a look at this. Like, the synopsis there, I think, is we're gonna move forward with what the API is presented here, so, yeah, just use for view.
Okay, and then, this, looks like all of our… Milestones for the main repository are not blocking, they're all observability-based, so these things can all get moved.
Except for the sync map, atomics for fixed bucket histograms and, exemplars. Yes, the reservoir here. This is also two things that are not the, observability, so I think, I've… started looking at this again this morning. Sorry, I just got back and started working again this morning, but Yeah, David, is there anything… I can't remember, we were trying to block on these for this release, or is this something that we didn't…
**David Ashpole (dashpole)** 15:14 need to… No, they can be pushed to the next one, it's totally fine. If they get in, great, if they don't.
No fuss.
**Tyler Yahn** 15:22 Yeah.
Okay, yeah, so I've definitely… I'm happy to review. I know Brian's also reviewed these as well, but we need another, GO approver, to review them, besides David, and myself. So, yeah, if you're on the call or listening to the… Recording of this, please take a look at these, two PRs as well.
Okay.
Otherwise, yeah, I think maybe within the next week, let's try to get this other release out, but, yeah, we know it's blocking, at least.
Let me double-check to see if Robert's on still.
Okay, so the next step, Robert wanted to ask the question about stabilizing new attribute value types, in the spec.
I think it's more of just, like, do we have a clear path forward on how we want to implement these?
There's a prototype.
Heaven.
looked at this more than I think… yeah.
Yes, I mean, I think it's just about looking at these things, attribute limits… Oh, okay, I'm guessing it's talking about these byte arrays, any values… Yeah, this is gonna be a disaster, but Yeah, okay, I think it's maybe just asking for review of these, so… Probably something we need to take a look at.
Also, Barbara wanted to talk about a proposal to move enable method from the filter processor to the processor interface.
**David Ashpole (dashpole)** 17:34 Has this already been proposed and accepted by the spec? Or is he just looking… Do we have flexibility?
Or does the spec give us flexibility on how this is implemented?
**Tyler Yahn** 17:48 I think that it's… How it's implemented, yeah, I think the spec gives us flexibility. I think it's stabilized in the spec. We had always not included it, because it wasn't a stable part of a processor definition, but the specification has been updated to allow, this method on the processor, and if it's defined, it's defined in this way. It's been stabilized, the signature of it.
So I think that was, like, our… always our… concern if we added a method here, and then it gets stabilized in a different format, but it looks like it has been stabilized. Obviously, I think we need to validate that it conforms with the specification, but yeah, I think that the idea here is that, like.
all processors then should be including this enabled. Yeah, Yeah, I think that might be one… yeah, this is definitely one of the downsides, if there's a processor that is, like, always enabled.
And you have to enable, or add this method just to say return true, It's just more boilerplate, I guess.
But, yeah, I mean, I mean, there's nothing, I think, blocking this. It is a… it is still a work in progress, so I think that, like, Yeah, I don't see too much of an issue against it, but… I do think that we want to, like, consolidate and make sure that, like, it's, I like having it in a single API, because then you have a clear definition of what the interface is, you know, what you're gonna expect, and you don't have to, like.
document or read through documentation to find out if this actually exists, or if it doesn't, or, like, you know, before you call this processor, enabled method, do a, some sort of, like, typecasting, but yeah.
**David Ashpole (dashpole)** 19:30 I, I… I now remember what this is all about.
**Tyler Yahn** 19:34 Yeah, yeah.
So, yeah, I mean, I think that this seems fine.
I think, probably worth taking a look at. I'm guessing we could probably talk about it at the next big, SIG meeting, just to see, if people have taken a look at it, and… Wanna go forward with it?
**David Ashpole (dashpole)** 19:51 I think this…
**Tyler Yahn** 19:53 What's that?
**David Ashpole (dashpole)** 19:54 I think the change makes sense. I remember what it was.
**Tyler Yahn** 19:57 Yeah, fuck it.
Okay, cool.
Also, I wanted to ask about support for… Otlp insecure.
Yeah, I'm not exactly following what's going on here. Pr applies to St. Jesus.
It looks like this is adding something to the logs, package to support insecure.
**David Ashpole (dashpole)** 21:28 What's the, it's only for gRPC. Yeah, I think that makes sense.
**Tyler Yahn** 21:36 Yeah, I think you're right.
Yeah, I mean, I think that… HTTP one was always kind of, like, a hard, issue to resolve this.
Because if, like, the endpoint… is used. I think that it, like, handles it one way, if the host is defined.
Another way, if it's defined in, like, the… There's, like, 4 different ways to configure if insecure is actually, like, used. One of them was, like, an option with, like, this environment variable.
I don't… I don't know. I do know that, like.
If there's going to be a resolution, I think it needs to get cleared up in the specification if there's, like, confusion here, but I haven't looked at this in a long time.
So, I don't… Know how to resolve this.
**David Ashpole (dashpole)** 22:32 Did Tyler, or did, sorry, did Robert say what he wanted from the SIG meeting? Just like… Like, cause… It sounds correct that we can't implement this, right?
**Tyler Yahn** 22:44 Well, it sounds like we do implement it in, traces and metrics.
**David Ashpole (dashpole)** 22:49 I think is the idea.
**Tyler Yahn** 22:51 And, And so it's not implemented in the logs, if that's what this PR is trying to, like, support, and then… Robert's pointing out that it actually isn't defined in the spec, is what my understanding is here.
**David Ashpole (dashpole)** 23:04 Just now looking at this. Sorry, go ahead.
If we have some traces, then I probably vote. Let's add it for logs.
**Tyler Yahn** 23:13 Yeah, I think that seems fair, right?
**David Ashpole (dashpole)** 23:17 Yep.
**Tyler Yahn** 23:21 Yeah, I don't know if removing the support for these environment variables is a great idea. Nope.
But yeah, I mean, I'm fine adding it to the logs. It's, again, like, it kind of skirts our stability guarantees, because it's not… it's more of a documented feature.
But yeah, maybe adding it to the spec is also something to be helpful, so that all implementations can do this, in all languages, so that seems reasonable.
**David Ashpole (dashpole)** 23:44 So, moratorium on environment variables.
**Tyler Yahn** 23:49 Yep.
Okay. That's probably why it's not in the spec, actually. That's a good point.
**David Ashpole (dashpole)** 23:53 What? I think we just do the right thing for our users and add it, and don't worry about the spec.
**Tyler Yahn** 23:58 Yeah, I think you're right.
Okay.
Cool. Alright, that is the end of the written agenda.
I could pause here. Any other topics people wanted to talk about? Or, cool projects?
**Bryan Boreham** 25:10 I could, I think I've spoken in the past about, the Protobuff Code?
And, about 3 weeks ago, the hotel collector lost its dependency on Google Proto.
**Tyler Yahn** 25:28 Oh, wow.
**Bryan Boreham** 25:31 See, that's interesting. I wondered how many people knew about this. Let me find the PR.
**Alex Boten** 25:35 I don't know if lost is…
**Sam** 25:38 Are they manually read Protopath?
**Bryan Boreham** 25:43 I'll post the, so, yeah, it's… As far as I can see, it's all being done by a tool called PDataGen.
Which was already inside the repo.
But got substantially changed in that PR.
But, I mean, the Goggle Proto is gone from all the go.mod files, so lost to the dependency in that sense.
**David Ashpole (dashpole)** 26:19 I assume this is Bogdan's handiwork? Yes, yes.
The one and only.
**Tyler Yahn** 26:27 Yep. Yep.
**Alex Boten** 26:28 Ogden, and a lot of, A lot of trust.
**Tyler Yahn** 26:32 Yeah, I was gonna say, 27,000 lines of code, And then 43,000 lines are removed. Yeah, that's… that's quite a lot of… Well, a lot of work for 1PR, but yeah.
**David Ashpole (dashpole)** 26:44 Still only counts as one.
**Tyler Yahn** 26:51 Yeah, okay. Well, Alex, you, you work over there, how's it… how's it been going since then?
**Alex Boten** 26:57 The… The benchmarking that Bogdan had provided seemed to indicate that things are going much better.
I can't remember the exact numbers that he had suggested, but I… I want to say there's some places where I think there was something like close to 15-20% less memory allocation in some parts, if I'm not mistaken.
I could be wrong, I'm going off the top of my head here.
There was one… I think one or two interoperability issues.
That were found as the work was being released. So this, this is work that took, I think, 3 releases to actually complete, because there was different parts to it.
I think this first release caught an issue where Something in the .NET implementation wasn't quite… Following the spec in the proto.
But other than that, I think it's been mostly… mostly good.
But we also have… Like, a lot of testing in this area, so it's…
**Tyler Yahn** 28:05 It's helped us a lot, I think.
Is, so I'm guessing, Brian, the question maybe is, like, if we could start looking similarly here.
But, do you know if the Protogen stuff is, in an internal package, Alex?
**Alex Boten** 28:23 I can't remember where…
**Bryan Boreham** 28:25 I don't know if there is any other here. I mean, I'll… I think all roads lead to that code in… everything Utahl that I'm aware of, I'm… I mean…
**Tyler Yahn** 28:41 It does look like the… the Protogen… ProtodataGen, PDATAGen, sorry, command is in an internal package.
**Alex Boten** 28:53 Although, I'm sure if you talk to Bogdan about it, he'd be more than happy to make it available, if it would mean that the Go implementation would also use it.
**David Ashpole (dashpole)** 29:03 Yeah, I mean, we'd have to put it in the upstream, the.
**Tyler Yahn** 29:08 The… whatever, the PData library, but I think we could, yeah, maybe look into that.
**David Ashpole (dashpole)** 29:15 Would we end up with a dependency nightmare if we… Took a dependency on P data.
**Tyler Yahn** 29:22 We already have a dependency on P data in the exporters, actually.
**David Ashpole (dashpole)** 29:26 Oh, really?
**Tyler Yahn** 29:27 Yeah, that's something, because we do translations there using PData.
But I don't think you'd actually have, like, so you can have cyclic dependencies of modules, you just can't have cyclic dependencies of packages, in Go.
Okay. So that actually works, just based on, you know, because it's actually, like, copied code, but yeah, Yeah, that's an interesting thing to maybe look at, as well.
I'd love to see some more, like, benchmarking, obviously, like, there's probably a lot of conversation that's not included, here that… more context is needed in that PR, but yeah.
That's really interesting, though.
So, Brian, yeah, like, is that kind of, like, what you're looking at still? Is this, like, that implementation, and maybe looking at…
**Bryan Boreham** 30:17 Whoa… Yeah, I have to say, it's pretty intermittent.
For me, although I have a colleague who's maybe looking at it more strenuously, Yeah, so it's some other code that has a dependency on that code that I'm really interested in.
I… yeah, I just… I don't have a lot more detail at hand. I'd sort of… I'd sort of observed the general territory, and then was kind of doing some research.
And then… 27,000 line PR.
landed, and I have not caught up with what changed.
**Tyler Yahn** 30:59 Yeah.
**Bryan Boreham** 31:01 I mean, the huge step forward to not have that dependency on an unmaintained upstream.
**Tyler Yahn** 31:10 Yeah, and I know upstream… er, our PData library that we use, sorry, like the, The proto-library that we use is the maintained, the name's escaping me right now, but, like, the maintained version of, like, the Google Pro debuff libraries. But, like, obviously there's a lot of inefficiencies there, especially around things that we probably want to, like, optimize for, so I'm guessing, like, this… Protogen stuff may be… may be helpful and something we could start trying to leverage, and maybe worth looking into there.
But, yeah, that's… that's interesting. Yeah, but yeah, that's cool.
Yeah, I guess maybe it's worth taking a look, going forward, so if folks have some time and wanted to take a look further at that PR, I think it's worth maybe exploring.
Yeah, thanks for bringing that up, Ryan.
I don't know if I'm gonna read, every single line there, but yeah.
Well, cool. Any other, interesting PRs that people have seen, or topics? I know we're also just coming back, this is, I think, the first SIG meeting since KubeCon. If folks were there or saw interesting talks, maybe? I think it's… you know, bring them up here. If you're watching the recording, I think… The videos should be coming out soon. I haven't seen any videos yet of Talks, but maybe we could also post them in channel, that'd be cool. I'd love to know more about what was interesting, for people.
But yeah, if that's it, and no other topics we want to talk about, we could probably end the meeting here.
Cool. Alright, everyone, well, thanks for joining. Good to see you all. I will see you all in a week's time, or asynchronously.
Period.
