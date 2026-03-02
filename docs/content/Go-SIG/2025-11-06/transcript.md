SIG: Go SIG
Date: 2025-11-06
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:55 Hey, Andrew.
**Andrew Wong** 01:03 Hey, Tyler, can you hear me?
**Tyler Yahn** 01:04 Yeah, I can hear you.
**Andrew Wong** 01:05 Oh, cool. Nathan, how's it going?
**Tyler Yahn** 01:07 Going well, how are you?
**Andrew Wong** 01:08 Good.
**Tyler Yahn** 01:10 I'm just looking over the meeting agenda notes, and it looks like you've maybe added an item to them?
**Andrew Wong** 01:17 So,
Full disclosure, this is my first time here, ever. I don't think I added anything, but my, someone on my team, might have added something. His name's Basker, is it on there?
**Tyler Yahn** 01:31 This is Andrew, but maybe they ask.
and a half.
**Andrew Wong** 01:36 Okay, so I can't see the document myself, but I think I know what he's asking for. I'm kind of on… here on behalf of one of my teammates who put down my name, but
Yeah, I, I, have something I want to bring up.
**Tyler Yahn** 01:50 Yeah, sure.
We can… we can just jump. I don't expect, high attendance today, so… Okay. Yeah, we're already, like, 3 minutes in, so…
Yeah, it's probably just us hanging out. So if you wanted to just… yeah, we could just jump in. It looks like you're asking about OTLP, like, feature stability?
**Andrew Wong** 02:05 Yeah, so, okay, from what I understand, a,
Oh, sorry. The, the hotel spec put out, some new stuff surrounding the…
Ex- console exporter?
Namely for, for hotel traces, metrics, and logs, the standard out exporter. I think now is… there's a spec out there for it to…
be able to export those 3 signals in JSON format?
And so now, like, my team's super interested in this capability. We've been going around to the other SIGs,
and seeing what's going on in the respective languages, in terms of this feature, is there plans to support it? Are there PRs already out there? Sounds like, for example, like, Java already has the support, completed. Python's working on it. So, for Go.
I'm curious if this is on the radar or not, if there's anything out there already, if someone's tackling it. Myself and my teammate
our… BASCAR are willing to take a stab at it if no one else has kind of picked it up. But yeah, so we're just here to kind of check on the status of this,
exported.
**Tyler Yahn** 03:24 Yeah, good… good question. So, there isn't any work on this currently. We do have, like, a standardized exporter, but that's not this. That standardized exporter is… is not an OTLP format, it's a… it's essentially a development server for just finding out if things are happening.
But, to your point, like, I'm guessing is that, like, that's not really helpful, because it's not really a standardized format, and, like, there's no interchange guarantees, which is…
intentional, like, we did not want to make an interchange guarantee there, but this would be a different, format here, right? Like, the OTLP output would be, like, some sort of ability to output directly to a file. Yep.
Yeah, there isn't any work on this,
currently slated, but there's nothing, I think.
stopping adding some sort of, development on this. I think that sounds… that sounds great. How this would…
how this would work, I think, is an interesting one, because, like, the hotel traces exporter thing, like, this is something that is not going to be included in the SDK, just because this is something… like, our SDK is set up by, passing in explicit definitions in, like, code itself.
If you wanted to, this can be added to the auto-export package, which is in Contrib. Take a look at that.
Essentially, there, there's a way for you to just, you know, ask it for an exporter, and it will use that environment variable. That's the place where we actually have it.
**Andrew Wong** 04:56 That's different.
**Tyler Yahn** 04:57 So, like, if somebody wanted to just support it that way.
That's… that's what it would do. Another place this would be used is in this OTelConf package.
This is also still a common… er, this is a tract issue to support, this console exporter, if I remember correctly. I'm trying to remember where it was.
Yeah, maybe it's just here.
Yeah, I guess we have the console. It's,
Yeah, OTLP file at the moment, that's what it is. Yeah, so there is this issue here, we can take a look at this.
So this is for the log one, it's weird that it links to that, but
Yeah, I mean, so I think that this is, this is, what we're talking about, though. Protocol file exporter… yeah, this is, I think, the definition that you're also talking about. Like, what we were looking at originally was the configuration for this in the environment variable, but this is the actual specification for the exporter itself.
I don't know why this is waiting on…
the stabilization of the spec. So, I think that, like, we could try to get something here that would be, an unstable release, like an experimental, module that would be added.
I guess the question is, is how it needs to get added?
Yeah. Because, yeah.
That's a good question, actually. Maybe we could take a look… let's take a look at the existing OTLP exporters.
Yeah, let's see…
I mean, these are all their own modules.
Yeah… huh.
So I'm not exactly sure why we wouldn't do something like add and…
I don't know… I don't know what to call it, so just, like, keep that in mind. This could change, but, like, another package here that'd be, like, OTLP log file.
Or… or OTLP… I don't know. OTLP log standard out, or something like that, and
And that would be its own module. It'd be an experimental module. Like, we don't have to release it as stable until it's stabilized in the spec, but it could be something that we could implement here.
And then, very similarly for, you know, the other signals, the metrics and the traces, traces might be a little bit harder.
But…
It's not that hard. The problem with this is the module structure's a little different. The module is at the actual OTLP trace level. We just have to add another module here that would be different,
No, actually, these are all their own modules as well. So, yeah, I think it's the same thing. So we would essentially add new modules into each one of these exporters through whatever file format we want to come up with there.
**Andrew Wong** 08:14 Okay.
**Tyler Yahn** 08:15 So yeah, I mean, like, if you're looking to work on this and, like, develop it, I definitely think that checking out…
this issue, but there's gotta be… there's gotta be more. Maybe there needs to be a bigger, broader issue?
Looks like, I don't know if Thomas is… your coworker…
**Andrew Wong** 08:37 No.
**Tyler Yahn** 08:43 Yeah, I mean, looks like the job wasn't… so I don't see why we couldn't add something like this. I don't know where we'd want to start. I'd maybe say recommend starting on the log one, and then we could, you know, look at adding it for the others.
**Andrew Wong** 08:54 What's that?
**Tyler Yahn** 08:55 So maybe, yeah, I'd say, like, take a look at this issue. If you could put port… put forward, like, a plan to add this prior to the stabilization to the specification, meaning… meaning very explicitly that, like.
If the specification changes, like, this module would need to change with it, and if the specification decides, like, this is not something we want.
There's a possibility it could go away, I don't know if it would go away if the specification's not there, but,
I really don't see that happening, I just see that the specification changing, so, like, it needs to be clear that whatever proposal is put here, it needs to be, like, isolated in a module, that module needs to be in a version that's not a 1.0.
And that, you know, it needs to have explicit versioning and compatibility guidelines that it could and likely will change in its API.
And then, of course, proposal for, API design.
likely following what we already have for other OTLP exporters, you know, very similar, structure.
**Andrew Wong** 09:49 Okay.
**Tyler Yahn** 09:50 But yeah, otherwise, I don't see why we wouldn't want to add something like this. I don't think it needs to be stable in the spec before we add it, especially if it can be a prototype to support the stabilization of the spec. There's always, like, this chicken and egg problem here, so, yeah.
**Andrew Wong** 10:04 Okay, yeah, that makes sense. So, yeah, it doesn't look like… and I haven't gone through the issues, honestly, but it doesn't look like there's anything specifically tied to this JSON file serializer out there yet. So basically, yeah, we can go ahead and make an issue, and…
Sounds like there needs to be a broader organizational plan also implemented, too, not just the functionality itself.
**David Ashpole (dashpole)** 10:25 So…
**Andrew Wong** 10:26 That makes sense.
**Tyler Yahn** 10:28 Yeah, and like, the JSON serialization is an interesting one, because I think we've looked at this for HTTP as well,
Specifically for OGLP.
And I think that if you get something working for, like, a file-based export, like, there's nothing stopping us from also then adding it to the HTTP as well, so this is actually probably a benefit overall, because I don't think we have JSON support in HTTP currently.
**Andrew Wong** 10:51 Gotcha, okay, yeah. Okay.
**Tyler Yahn** 10:53 So, yeah, I mean, it could be a very big, important, move forward, so…
**Andrew Wong** 10:58 Interesting.
**Tyler Yahn** 10:58 But, yeah, it definitely would require some… some engineering effort, to get this moving.
**Andrew Wong** 11:03 Yeah, totally makes sense. Okay, sounds like this is,
Something… something that's pretty new. So, okay, yeah, I mean, we're happy to… we're happy to…
Try and tackle it. Yeah.
**Tyler Yahn** 11:16 I think… I'll leave a comment in here that we can maybe just say that we talked about this, and that, like, there's a possibility for a proposal, and then I would just comment in here what you wanted, like, you know…
Just start the conversation here, I think it's a good place.
**Andrew Wong** 11:31 Yep.
**Tyler Yahn** 11:32 That makes sense, good.
**Andrew Wong** 11:33 I will… okay, so this is open issue 5408, okay, yep.
**Tyler Yahn** 11:37 Yeah. Yeah, and I've added it to our, document… oh, yeah, you said you can.
**Andrew Wong** 11:41 Yeah, my org is blocking me.
**Tyler Yahn** 11:43 Yeah, okay.
**Andrew Wong** 11:44 No worries.
**Tyler Yahn** 11:46 Well, cool. Yeah, and then, please feel free to come back to these meetings as well if you need more feedback or want to talk. I think,
One of the items we're gonna talk about is probably canceling next week's meeting, because KubeCon is going to happen, and then the week after, it'll be the same time.
which probably means that Robert, who is the person who opened this issue, isn't gonna be here, but the week after that, so maybe sometime…
at the end of the month, or December, he'll be here, and we could talk a little more, if that… if that works for you as well.
**Andrew Wong** 12:15 Yeah. That is perfectly fine, yeah, no rush here. Okay. It's on our radar, though. Yeah, cool. Thanks for checking this out.
with me, yeah. I'm gonna… I'm new to the project overall, so I'm…
getting my bearings, too. But yeah, thanks for explaining, how this might look. Yeah, we'll open an issue, I'll… I'll comment on this one that you've shown, and I'll bring it back to my team and see what we wanna…
Try and do.
**Tyler Yahn** 12:41 Yeah, okay, that sounds good. Yeah, I mean, I think if we… we definitely welcome any contributions, so if you would like to work on this, we would appreciate it. I think that that's a great feature set, so yeah.
**Andrew Wong** 12:50 Yep, I think we are open to do it, because I think there's a need for it for us coming up soon, so, yep.
**Tyler Yahn** 12:57 Yeah, awesome. Thanks, Andrew.
**Andrew Wong** 12:59 Yeah, thank you. That's all for me.
**Tyler Yahn** 13:01 Cool.
**David Ashpole (dashpole)** 13:02 Quick question. So, wait, why… why'd you say they should start with logs?
**Tyler Yahn** 13:07 Because there's an open issue for it, and it's not a stable… like, the other ones aren't stable as well, so, like, if we did need some structural changes, but…
I mean… There's an open issue for it. Yeah, that's really it.
**David Ashpole (dashpole)** 13:22 Okay, yeah.
**Tyler Yahn** 13:24 I mean, I don't think it needs to be logs, like, if you really have a strong desire to do tracing or metrics or something like that, I don't, like, yeah, like…
**Andrew Wong** 13:31 Yeah, I think… Again, Teresa's Metro's probably first, but,
Yeah, we can… let me read over what's in this… this, this issue first.
**Tyler Yahn** 13:41 Yeah, that sounds good.
**Andrew Wong** 13:43 Thank you.
**Tyler Yahn** 13:46 Anything else, David?
**David Ashpole (dashpole)** 13:48 Nope.
**Tyler Yahn** 13:49 Well, cool.
Alright, so jumping out on the agenda, I was wondering if we wanted to do a release, given Kukon is next week,
maybe… I don't think there's any, like, big features, like, you know, the logs API stabilization happening, but I figured it might be worth, checking to see if what we have is something we want to release, and anything else is,
Can be bumped, which… I think we talked about this last time, I think that was a pretty…
Open question about whether we can bump things, let's see… Okay, so…
Yeah, observability, so the metrics observability, there's definitely some PRs for the… this looks really old, I don't know if this has actually been updated.
There's still a work in progress on the simple spin processor, and the… I don't know.
**David Ashpole (dashpole)** 14:50 Epic Reader one that just got merged, which is nice.
**Tyler Yahn** 14:53 Yeah, and there's a periodic metric reader as well, maybe it's just not tagged appropriately. Standard out, exporter, yeah, standard out, exporter, okay.
Maybe I'll go find the periodic one.
Oh, no, we merged that. Yeah, okay, yeah, sorry.
Yeah, so the readers are there as well.
I guess it's closed.
So the only thing, I guess, not observability is this, optimize the histogram reservoir, which… and they optimize the atomics.
What's that?
**David Ashpole (dashpole)** 15:26 Optimize everything.
**Tyler Yahn** 15:27 Yeah, yeah, exactly.
let's see, these are something I've been saying I was gonna review for, like, 3 weeks now.
**David Ashpole (dashpole)** 15:39 You know, I was trying… decide if I should, like, try and split it or something, but…
**Tyler Yahn** 15:44 That's the thing.
**David Ashpole (dashpole)** 15:45 it's okay to do a release. We're not gonna get all the optimization PRs in, for sure.
**Tyler Yahn** 15:50 Okay.
**David Ashpole (dashpole)** 15:51 It's fine to do a release.
If anything, then if I broke something, For counters, someone will… Notice.
Before we…
**Tyler Yahn** 16:01 Yeah.
**David Ashpole (dashpole)** 16:02 Muck with histograms, but… I'm not…
it's okay if they get split across releases, I think.
**Tyler Yahn** 16:10 Okay.
Yeah, I mean, that… yeah.
I think that might have to happen if we wanted to try to get a release out, because even if I reviewed these today, it's still missing another review.
**David Ashpole (dashpole)** 16:20 Yeah. I… I kind of think…
Yeah, I think everyone's waiting for your review. I don't think anyone else is gonna stamp it, because I think you and I are the most familiar with the Metrics SDK.
Okay. So, not like… I'm not blaming, I'm just, like, I think that's the reality, is that, yep.
Not all the maintainers understand the metrics well enough.
**Tyler Yahn** 16:47 Yeah, it is what it is. I like living in a world of, real…
You know, real world, yeah. So, yeah, okay, I will… I'll prioritize taking a look at these. I think that we could bump them, though, to the next, release. I don't think there's anything wrong with that. I think that makes sense, like you're saying.
Actually, I think all this stuff can get bumped to the next release. I don't see anything specific in here. David, do you?
**David Ashpole (dashpole)** 17:10 No, I mean, I… honestly, the… Optimized histogram Reservoir PR is… almost trivial?
**Tyler Yahn** 17:19 Yeah.
**David Ashpole (dashpole)** 17:20 What?
It also has zero impact until the other histogram PR, but it's more like… you know.
It hasn't gotten reviewed in a few weeks, so it's… it's probably fine.
**Tyler Yahn** 17:32 Yeah, I mean, I took a look at it, I was still thinking through it, just, I keep getting hung up on the partial, updates, and I just gotta convince myself that that's fine.
**David Ashpole (dashpole)** 17:43 Not trivial.
**Tyler Yahn** 17:44 What's that?
**David Ashpole (dashpole)** 17:45 I said, maybe it's not as trivial as I'm thinking it is.
**Tyler Yahn** 17:50 I… I… well, yeah, I think maybe you're… yeah, like, code changes-wise, it's actually pretty easy, but
The behavior changes, I think are fine.
I think are fine, but I'm just trying to convince myself that they're fine, and every time that I spend, 5 minutes away thinking about it, I move on to the next thing, so I just need to spend some time thinking about more.
the impacts of this, because I think, like, these kind of performance improvements are worth the consistency issues that this is… it's not really even issues, it's, you know…
Exemplars are not necessarily
they're not metrics, right? They don't need to be, in the correct value that you're reporting. They need to be associated with, like, something that was in a cycle that a trace can then link to, and I think that that's…
that's fine to spread across collection cycles. It might be a little confusing if it happens, you know, your collection cycles are, like, hours, but…
I don't… I think, like, you're kind of, like, already asking for it if you're doing something like that. So, yeah.
So I don't think there's any issue here, but I just have to…
I guess I just have to approve it. So, yeah, maybe I'll prioritize that right after the meeting, and then we can…
Try to get that in the, this next…
release, however, like you said, like, it's not as critical to have it if this one isn't merged, and I don't think this is… oh, actually, this needs another review anyways from somebody else, so…
**David Ashpole (dashpole)** 19:15 It does. Well, it has Brian's review, and it has your review, but it needs another approver.
**Tyler Yahn** 19:21 Sorry, yeah, that's true, yeah.
Yeah, correct. Okay, well, I will try prioritizing reviewing that anyways, because like you're saying, like, there's likely people just waiting on my review here.
I don't know why I can't just move these to the next milestone.
I don't know if GitHub changed recently.
**David Ashpole (dashpole)** 19:43 I don't know.
**Tyler Yahn** 19:44 Well, alright.
**David Ashpole (dashpole)** 19:46 Just ask Copilot and it'll work.
**Tyler Yahn** 19:49 Or maybe not.
Yeah, or maybe it'll just put it in the void, who knows, right? Yeah, alright, I will… I think we can move these. I think the only other one that, was standing out was the one that Robert's planning to work on, but he's planning to work on it next week, so we also talked about this before.
I don't think we need a resolution right away, and this is just on the,
error, reporting from OTEL HTTP, if I may… if I remember correctly.
**David Ashpole (dashpole)** 20:15 Yeah, I…
Actually, the biggest thing that comes to mind is OTELConf 1.0. So it's like, the core, I don't think there's any…
But…
**Tyler Yahn** 20:27 Yeah, that's actually a good point.
**David Ashpole (dashpole)** 20:28 Big, actually chunky feature that…
we might want to hold a release for. It seems like he's blazing ahead,
Yeah. So I'm not sure how much is left.
**Tyler Yahn** 20:39 I can… I can actually ping Alex after this, but yeah, actually, that's a really good point. I think maybe that's worth holding it, like you're saying.
**David Ashpole (dashpole)** 20:48 It would be cool to have it at KubeCon, be like, it's here, go use it, write it on the whiteboard, you know?
**Tyler Yahn** 20:54 That might actually be one of, like, the features we'd be proud of to talk about, you know? So, yeah.
I'm gonna… yeah, I'll add it to the milestone so we don't forget about it, and then…
**David Ashpole (dashpole)** 21:05 I will ping Alex afterwards.
**Tyler Yahn** 21:07 We could also try to do the release, like, Monday or Tuesday next week, in the middle of KudCon. That's also something we could do.
**David Ashpole (dashpole)** 21:13 Hit the button, yeah. During this meeting or something.
**Tyler Yahn** 21:17 Yeah, right? That'd be great, actually, yeah.
Okay, so let's, let's hold off on that then, and then in that time, maybe there's also some movement on these in the next day or two, so we can try to get these in.
But otherwise, yeah, let's, let's,
Let's just put in a holding pattern, then.
**David Ashpole (dashpole)** 21:35 The one that you were… you just had up is basically, like, the…
Giant one that's getting slowly split, right?
**Tyler Yahn** 21:42 Oh, the hotel, yes.
**David Ashpole (dashpole)** 21:45 So that's… that PR isn't actually ever gonna merge, it's…
**Tyler Yahn** 21:48 Right. I just wanted to put something here so I can see it.
Cause I forget about it if it's not here, right? So, like, I just… like, I think you're right. Like, I don't think this is actually going to exist here, but until there's one that says, like, this is… this is the final hotel conf, I'll put that in here, but, yeah.
Yeah.
Yeah, and I'll ping Alex, he… I owe him a response anyways for something he asked me earlier. So, yeah, I'll try to get a timeline on that, and maybe, maybe he'll be done today, and then tomorrow we can get something out, that'd be great.
In theory, I'm flying Saturday to get to the maintainer's meeting on Sunday.
But, the US flight system is a little… Wonky right now.
So…
**David Ashpole (dashpole)** 22:29 Did I not know about this? I didn't have this on my calendar. Oh well.
**Tyler Yahn** 22:33 The Maintainer Summit?
**David Ashpole (dashpole)** 22:34 It's on Sunday?
**Tyler Yahn** 22:36 Yeah.
**David Ashpole (dashpole)** 22:37 Oh my goodness.
**Tyler Yahn** 22:38 Wait, are you… oh, no. Are you not gonna make it?
**David Ashpole (dashpole)** 22:42 I'm not gonna make it. I mean, I can look at changing my flights.
It's… what time's Sunday?
**Tyler Yahn** 22:48 Like, 9am or something, 8.30am or something like that, yeah, it's…
It's a… it's a day negative one, is what they're calling it, which is kind of ridiculous, but…
Yeah, you're not alone, you're… like, a lot of people are not attending because it's on Sunday, and they're like, this is insane, but…
**David Ashpole (dashpole)** 23:10 I don't know if I can, like…
Anyways, I'll figure it out on my end.
Thank you for letting me know.
**Tyler Yahn** 23:17 You don't have a talk schedule, do you?
**David Ashpole (dashpole)** 23:20 I hope not. I don't think I do.
**Tyler Yahn** 23:22 Okay.
Yeah, I mean, if you do make it, we're giving a panel discussion with, like, hotel, design people, the people who put up OTEPs, so it's worth attending if you can make it, but yeah, I…
I'm also not sure if I'm gonna make it, given, flights are getting
Rerouted or canceled or things, so, yeah.
**David Ashpole (dashpole)** 23:43 Yeah.
**Tyler Yahn** 23:44 Yeah.
Okay, the next question would be our next meeting, which is next,
Thursday, which I don't expect anybody going to KubeCon's gonna be there, so I know…
Myself, Robert, David, I'm guessing you're gonna be there as well.
So, I guess technically… I don't know if Sam's back yet, but Sam and Damien would be the only people attending, so I guess I can post in channel and ask if they want us to hold the meeting. But otherwise, we do have that,
meeting scheduled at the observatory. We did have something on the books last time I checked there.
So, yeah, I think we can just plan on meeting in person with, you know, other folks from the community and cancel the online one.
**David Ashpole (dashpole)** 24:36 I think we should do that. Yep.
**Tyler Yahn** 24:38 I will ask in Slack as well on that one, but otherwise, yeah, I plan on canceling it.
Yeah.
Cool, alright.
Well… awesome.
Any other… Topics?
**David Ashpole (dashpole)** 25:08 I'm excited to see HTTP SenConf going stable. I…
I guess we have time. Do you… Do you know…
anyone who has tried out the new Go runtime metrics, have you… Played with them at all.
**Tyler Yahn** 25:22 I mean, I played with them, but, like, just, yeah, more…
No, not in a serious fashion, just locally and, like, trying to check them out, yeah.
**David Ashpole (dashpole)** 25:33 I need to…
**Tyler Yahn** 25:33 Like, I haven't deployed them at, like, I haven't even deployed them in, like, a sample app, I just deployed them locally on my system kind of thing, and just tried running them there, but…
No.
**David Ashpole (dashpole)** 25:46 Maybe I'll,
Maybe I'll go bug the collector and see if we can get them included in the collector's default set.
So that we get some… Feedback on them, but…
**Tyler Yahn** 25:56 Yeah, I think that's a great idea, actually, yeah.
**David Ashpole (dashpole)** 25:59 Because I… From a ergonomics perspective, they seem nice.
And they seem useful.
And… You know, with all the pushes towards stability, seems like an easy win.
**Tyler Yahn** 26:14 But…
**David Ashpole (dashpole)** 26:15 I also want to make sure we're actually… and they're what, like, the Go team has recommended, and they're not very far from what Prometheus uses, right? So it's not like…
There.
This new, you know, Unexplored territory in terms of content, but…
It would be good to make sure we get real usage before we mark them stable.
**Tyler Yahn** 26:35 Well… I'm looking at the, the Godox page, 278 imports of them right now.
**David Ashpole (dashpole)** 26:44 Is that good?
**Tyler Yahn** 26:47 I don't know. It's more than… more than one, right? So.
**David Ashpole (dashpole)** 26:52 the Prometheus Bridge.
**Tyler Yahn** 26:54 What's that?
**David Ashpole (dashpole)** 26:57 Can you see the imports?
**Tyler Yahn** 27:00 On the Prometheus?
**David Ashpole (dashpole)** 27:01 In the contributor repo, or in.
**Tyler Yahn** 27:04 A different repo.
**David Ashpole (dashpole)** 27:06 In Contrib.
**Tyler Yahn** 27:10 Yeah, we can take a look at that.
**David Ashpole (dashpole)** 27:11 Yeah, can… Can everyone see this? Imports. Okay, yeah, the Prometheus Bridge has 13 imports, so…
**Tyler Yahn** 27:18 Oh.
**David Ashpole (dashpole)** 27:19 the Go runtime metrics is pretty… Pretty solid, then.
**Tyler Yahn** 27:23 Looks like, we got Datadog here.
Yeah, I mean, they're… Datadog's using it.
**David Ashpole (dashpole)** 27:33 Wait, oh, imported by is what I'm looking for, yeah, yeah.
**Tyler Yahn** 27:43 Trying to see if I can find some… more recognizable Folks on here.
I mean, I don't… these all look, like.
**David Ashpole (dashpole)** 27:53 Yeah.
**Tyler Yahn** 27:54 Yeah.
I mean, I think that there's actually quite a lot of use, to be honest.
**David Ashpole (dashpole)** 28:01 But… yeah, they must all be using…
the latest one, right? Because we bumped it to default to the new ones.
**Tyler Yahn** 28:08 Yeah, yeah.
**David Ashpole (dashpole)** 28:10 No? Okay.
**Tyler Yahn** 28:11 And then, like, actually, that's a good question. So, if I go back to, like… so 278?
Oh, no, it still says 278. Maybe 2… maybe this isn't filtered by… what version they're using? Okay.
But…
I mean, I guess we could… we could do, like, a sample check here, too, like, if you… let's see…
**David Ashpole (dashpole)** 28:37 Anyways, I think that that would be a good…
Maybe not, like, end of year, but maybe KubeCon next year.
You know, trying to have the runtime metrics stabilized. But I think focusing on HTTP Is it good?
thing for our SIG to be doing right now.
**Tyler Yahn** 28:55 Yeah, I agree. Actually, maybe that's…
worth checking out, like, what's the hotel HTTP, look like?
**David Ashpole (dashpole)** 29:08 13,000? Yeah. A few.
**Tyler Yahn** 29:10 No, this is.
**David Ashpole (dashpole)** 29:12 Yeah, yeah.
**Tyler Yahn** 29:13 Yeah, hold on, what's this?
**David Ashpole (dashpole)** 29:15 contrib, instrumentation, net HTTP.
**Tyler Yahn** 29:18 Yeah, that's right.
**David Ashpole (dashpole)** 29:25 On the bottom.
**Tyler Yahn** 29:28 Oh, here we go.
God, we also need to clean some of this stuff up.
Yeah, 2,353.
**David Ashpole (dashpole)** 29:41 Yeah.
**Tyler Yahn** 29:43 So, 10X factor on that one. But,
Yeah, so it looks like the… at least the Datadog ones are using 63, which is the default, new stuff, so yeah, I mean…
It's there, right?
**David Ashpole (dashpole)** 30:06 Yep.
**Tyler Yahn** 30:07 Yeah.
Yeah, I mean, I'm on board for stabilizing these. Is… are the runtime metrics stabilized in the semantic conventions, though?
**David Ashpole (dashpole)** 30:17 No, but it… We're… we're the only implementation, right? So we… we just go to this… it's just…
It just requires two PRs to stabilize instead of one, right?
**Tyler Yahn** 30:26 Yeah.
**David Ashpole (dashpole)** 30:27 It's not like we have to go debate this with… Yeah, I see.
We decide we're happy, and then we stabilize them.
At the same time.
I think.
**Tyler Yahn** 30:38 I mean, I think that that's… that's fair.
It might also just be worth, like, you know, maybe in a little bit, like, when we get back from KubeCon or something like that, like, opening an issue to stabilize, and then pinging some of these, if we can find more vendors in that import list, and ask if their opinion on that, like, is worthwhile.
But, yeah, I mean, I like the idea. That sounds great.
I like getting to a 1.0,
instead of being de facto stable, actually committing to being stable, that'd be great. So, yeah.
Well, cool.
Yeah, any other topics?
**David Ashpole (dashpole)** 31:12 Nope, nothing from me.
**Tyler Yahn** 31:14 Awesome.
Well, yeah, I'm excited to see you next week, and everyone else come to QCon. Hopefully we all make it in time.
But yeah. Alright, I'll talk to you later.
**David Ashpole (dashpole)** 31:28 See you, Tyler. Bye.
**Tyler Yahn** 31:29 Right.
