SIG: Go SIG
Date: 2026-01-22
Duration: 68 minutes
Zoom Recording URL: https://zoom.us/rec/share/hgIXEWLlI1ix9LJwb90PE_DOvGl-_vYN1CDGAb_V7yqIcuvzpCM0ufEaO5hyMzSM.L6BsJb07JwxffDA3
============================================================

## Zoom Recording Transcript

Tyler 00:02:31 Hey, Damien.
Damien Mathieu 00:02:35 Hey, good evening.
Tyler 00:02:37 Hey.
Hey, Brian.
Are y'all going to that, hotel meetup in, like, Fostem stuff?
Damien Mathieu 00:02:53 I am.
Are you?
Tyler 00:02:56 No, I'm not, no.
There were some other folks from the eBPF SIG that were gonna be there, though. I think they work at CoreLogix, and then…
I'm trying to think… I think Sven… yeah, there's a few other people, so, yeah, they were… they were asking if anybody else was going, but…
Bryan Boreham 00:03:15 ambivalent.
Damien Mathieu 00:03:18 And, Brad, are you gonna.
Tyler 00:03:19 be there?
Damien Mathieu 00:03:20 Norbert, you're going.
Pellared 00:03:26 Hello?
Okay, something?
Damien Mathieu 00:03:29 So, yeah, Brian, you said you're going to fuss them,
Robert, are you going to first then? Okay.
Bryan Boreham 00:03:38 So, forced demand, the hotel unplugged thing on the Monday.
Tyler 00:03:43 Yeah, that's what everyone was a little, like, confused on. They were like, oh, it's, like, the day before. Oh, shoot, like, yeah, so.
Bryan Boreham 00:03:50 day after.
Tyler 00:03:51 Or after, sorry, yeah.
Damien Mathieu 00:03:52 Yes, day after. It's, I mean, I understand it, but it's kind of, having conferences during the weekend is always…
Tyler 00:04:00 Yeah, not really useful.
Like, KubeCon North America this year, right? They had the maintainer's Day, and I'm pretty sure it was on Sunday, and, like, just nobody showed up, because they were just like, I'm not, like…
I'm not gonna do that.
Bryan Boreham 00:04:17 So they've done that again for KubeCon EU, I think.
Tyler 00:04:21 With the Maintainer Summit?
Ugh.
Bryan Boreham 00:04:25 Think so?
Tyler 00:04:27 Yeah, that's…
Pellared 00:04:28 You are right.
Tyler 00:04:30 I mean, I get it.
Pellared 00:04:31 Monday.
Tyler 00:04:32 Because they have, like, the zero days are on Monday, yeah, and so it's like… like, alright.
You can't have it the same day as that, but… man, that's kind of annoying.
Damien Mathieu 00:04:42 Yeah, I mean, it means traveling on the Saturday, and then it's… yeah. I don't think I'll be attending the… if it's on the Sunday, I don't think I'll be attending the maintainer summit either.
Tyler 00:04:52 Yeah, exactly.
Damien Mathieu 00:04:53 Or…
Tyler 00:04:54 Everyone else.
Damien Mathieu 00:04:55 Maybe I'll register and just attend the, the party at the end.
Tyler 00:05:02 Yeah, I mean, that's… that's fair. That's, I think, what a lot of people…
like, they were like, well, they were getting in on Sunday anyway, so it was like, they couldn't… they couldn't make it, so, yeah.
Bryan Boreham 00:05:13 But Fosdam's not really a conference. Right. Fozdam is like a happening…
Damien Mathieu 00:05:20 I mean, it's not a… I mean, there are a lot of talks, but it's not a conference in the same way as KubeCon or many other conferences today, which are more like, lots of sponsor stands and a few talks around it.
Tyler 00:05:36 Yeah, very true.
Damien Mathieu 00:05:39 Which is better, the first demo, in my opinion.
Tyler 00:05:46 Cool. Alright, so we're going on 4 minutes in. I see David's here. I think we're only missing Sam at this point. So, yeah, let's jump in here and get started. If you haven't yet, please go ahead and add your name to the attendees list. I'll start sharing my screen, and we can…
Jump in here.
So yeah, the only thing I had on the agenda so far is just to talk through what I've captured as the goals, and classify them. So, a lot of this stuff from last time
Which was great, we had a lot of great discussion on this, and I've tried to capture these all in some… in a project board, as an action item. Actually, let me double check to make sure I didn't miss something. Yeah. I did forget to ask in Slack, but that's kind of,
Okay.
But, we can talk about this here. So, I wanted to go through the project board here and, talk through what we have.
I also want to classify things to make sure that, like, we have an understanding of size.
And priority, and, one, to help us in, like, retrospectives for the end of the year, but also just to, like, understand our planning and what we're able to accomplish. Based on, like, our capacity from last year.
We have way more than I think we can accomplish this upcoming year, so unless we're planning to, like, double down and, like, you know, commit more time to this project, like, most of this stuff isn't gonna actually get done, so I was also wondering how we want to cull this and how we want to, like, prioritize this.
So yeah, I think maybe just go through this the first way, and we can talk about, priority and size.
I'd love to get assignees for each one of these as well, but if we don't have an assignee, then, that's understandable, and I think afterwards, maybe going through and asking, you know, if we don't have a signee, we have things that are large and low priority, like, are we just gonna remove those from targets for 2026?
Cool. So to start us off, I have the SDK observability, as at the top. This is something that I've taken ownership of, and, acted as a sponsor for. High priority, given the fact that it's a continuation from last year.
I think it's about a medium size, there's, 4 more tasks out of the 18 still to do. It's stalled, I think this just needs more, you know, a reinvigoration of effort to come through here, so…
That looks pretty good.
The release of the Logs API 1.0, I've assigned this to Robert, this is just capturing something that was in a project board prior. This is all the remaining tasks that are there. I still think this is quite large. I classified it as extra large, and a high priority.
Robert, does this track with what your thoughts on this are?
Pellared 00:08:21 Is the size, considering what's left, or everything?
Tyler 00:08:25 What's left?
Pellared 00:08:27 I think it's large, but maybe I'm too optimistic.
But, yeah.
Tyler 00:08:31 Yeah, I mean, they're subjective, so it doesn't really matter. But yeah, I do think that this one is definitely extra large. That's the only one I'm really sure on.
Okay, cool. Then, the release of the Z pages. So, I've got this as a priority medium, it's assigned to, to David, and size-wise, I'm guessing this is a medium or small, David? What are your thoughts on this?
David Ashpole (dashpole) 00:08:55 I haven't looked at this package in more than a year. I would guess it's small.
Cause I would guess the…
API surface that we would be interested in maybe changing, i.e, we probably won't change the output of the ZPages endpoint. I would expect the API service to just be, like.
register or something like that, and not need very many changes. I also consider this low priority from my own personal point of view, but I'm happy to
If other people think differently.
Tyler 00:09:30 No, I think that the only thing around these, like, releases is just that, like, there's a concerted effort in OTEL to try to make a stabilization, but I, don't think…
David Ashpole (dashpole) 00:09:41 that if you think this is a low priority, I don't think anybody else can think it's higher priority, unless they want to step in and start working on it, so… The only thing that might make me think differently is if it was on the collector's list of components they wanted stable. If the collector said, we want it, then I would
Say it's high priority, we should do it to unblock them, but…
If they don't care, then I'm…
Tyler 00:10:01 I haven't heard anything, so, yeah. I don't think they care, but.
David Ashpole (dashpole) 00:10:05 Thank you.
Tyler 00:10:06 That's completely just my thoughts, so, yeah.
Okay, the 1.0 of the AWS Lambda detector?
I… think this, again, is, I think this is bigger than the ZPages, because I do think that the ZPages is more of, like, a output-oriented. The Lambda detector is a package for downstream users, so I'd say something, like, on the medium size, given the fact this is going to require an audit of what's actually there and what we want to do.
Priority-wise, I don't think it can be higher than…
medium. I would say low as well on this one, though.
I'm seeing David shake his head, so I'm just gonna put low. If people think otherwise, go ahead and let me know.
I think I'm gonna say the same thing for the, Azure detector.
And I'm gonna put down medium here as well.
I didn't ask for assignees on this one, because I guess I don't know if the owners of this are… I think this is an Alex Katz thing, that he owns this, so I'd probably want to maybe ask him first, but yeah, I think…
Unless people on the call want to jump in as owners of this, I was just gonna leave this as blank so far.
Okay, moving on to the Jaeger Remote Sampler, stabilization of that, I think, again, is, on the order of a medium. I haven't looked too deep into it, but, like, that's just my gut. We can always change these things, these are changeable.
I would say it's either a medium or a low priority.
And I'm gonna put low, because I'm not hearing anything.
And so, the Open Census propagator, also, David, you had said this was a low priority last time we met, so I'm gonna leave it there. Size-wise, I'm guessing similar medium on this one?
Unless you've taken a look.
David Ashpole (dashpole) 00:11:55 I would expect this to be small, because it just implements the propagator interface, right?
Tyler 00:12:02 Yeah, it should, yeah, and… yeah.
Yep. Yeah.
Okay, then I will put small.
The 1.0 release of the file-based configuration, I think this is high. I think this is still a fair amount of work here. I would say this is probably a size large,
Yeah, just given how much this is gonna require for the back and forth within the SIG, as well as, like, I think there's API design.
Pellared 00:12:29 I have a opinion that it is larger than Log's API.
David Ashpole (dashpole) 00:12:34 overall, I think… I think, like, we're in this weird question where… I think we should just mark this extra large. Yep, it's, like, 80% dish done, maybe, but…
I think there's a lot of things that could come up there.
Tyler 00:12:49 Yeah, I think our API is something we want to really double down on in our approach. I think right now what we're doing is providing a pretty good, like, sanity check for the file-based configuration stabilization, but I'm not exactly sure that we've gone through it and understood, like, what we want to release as a 1.0 is there, so…
I think this is… this is correct.
I'm happy to take ownership of this continuing, going forward, as long as ownership is sponsor, and I am
shepherding things through, and not doing all the work. So happy to do that.
Use of the enable method for synchronous metric instruments. I think this is similar to the SDK observability, because it's just got to go through everything that we already did, plus everything in the,
the Contrib repo as well. I think there's only, like, 3 or 4 instrumentation packages that actually have metrics, so…
synchronous metrics. So I don't actually think this is too much in there, but I would probably say this is maybe a large task, just to go through the whole scope.
I'm also happy to pick this one up. I've done a lot of the SDK observability stuff, so this isn't too bad. I've already seen a PR actually addressing this for, gRPC export or something like that? I can't quite remember. So, like, there… I think this is… from what I've seen, like, this isn't gonna be too complicated, it's more just tracking this down, so… I'm happy to take this unless there are other folks that want to take this on.
I do think it's high priority, because that's, an optimization that we want to include, so yeah.
Release of the Prometheus Bridge. David, you also said this was low, and so I think size-wise, I have no idea on the size on this. Honestly, I haven't looked at the Prometheus Bridge in a long time.
David Ashpole (dashpole) 00:14:24 I would…
I mean, this one's just tricky because it's blocked on the specs being stable, so I…
Tyler 00:14:38 Maybe that in the size.
David Ashpole (dashpole) 00:14:40 Yeah, so I… Just, call it medium for now.
Okay.
But…
Tyler 00:14:50 And should I sign this to you, or should I leave this open right now?
David Ashpole (dashpole) 00:14:52 I will shepherd it if, at minimum, if there's other people who are interested in working on it.
Tyler 00:14:57 Yeah, yeah, absolutely.
David Ashpole (dashpole) 00:14:59 You can do the same for the Open Census propagator as well.
Tyler 00:15:03 Okay.
I will do that then.
David Ashpole (dashpole) 00:15:05 Maybe we could… maybe we should title the… this the sponsor or something.
Tyler 00:15:10 Yeah, that's a good question.
David Ashpole (dashpole) 00:15:13 I don't know, it's fine if we… yeah.
Tyler 00:15:16 Yeah, you know what, I might…
have to do some project board stuff to make that happen, but I think that's a, let me, let me not lose this idea.
Okay.
Cool.
So… based on that, we were here, so the W3C random flag, I think we already have an assignee here. I think this is in progress, so…
That sounds good. I say this is a medium, I think this is a small task, if…
People think otherwise, go ahead and correct me.
Next up is the Optimize the Metric SDK, already, sponsored by David.
high priority, something he's been working on considerably. I…
Don't know where I got medium from, but this, is classified as medium, I don't know if that's correct. What are your thoughts?
David Ashpole (dashpole) 00:16:21 I feel like this is large or extra large, like…
Tyler 00:16:23 I… yeah, okay.
Make the determination, you tell me.
David Ashpole (dashpole) 00:16:30 Just… just call it extra large. I think it's…
it, like, the things… bound instruments would be extra large. The concurrency…
Tyler 00:16:41 Definitely should be included, yeah. So, yeah, okay.
Okay, let's do that then.
Okay, stabilized instrumentation. This is… I think we need a new category. I don't think this is even extra large. So this is the one where we have…
I think, 1, 2, 3, 4, 5, 6, 7, known sub-issues here. Or, sorry, 6, known sub-issues.
And then we had a bunch of other ones that we didn't know if we were going to prioritize for this upcoming cycle, just because of the stabilization of semantic conventions.
So, yeah, this is, like, right now, I've assigned, 3 people that are the 3 people working on the subtasks here, or who have stepped up and asked to run on the work on the subtasks.
And, so yeah, I think size-wise, it's definitely an extra large.
Maybe more. And priority… this I had as high. I don't know if that's the correct priority here, given all of the other stabilization efforts we have. Thoughts on that one from folks?
David Ashpole (dashpole) 00:17:43 I hope… I would almost prefer just removing this issue.
And using the sub-issues to track priority and… And, owners and stuff.
Tyler 00:17:57 Okay. Well, we can do that.
David Ashpole (dashpole) 00:18:01 Otherwise, it's just a summary of all the other ones.
Tyler 00:18:06 Yeah, yeah, sure. I mean, yeah, it is, yes. So we can…
David Ashpole (dashpole) 00:18:14 from the project board. The issue is still helpful.
Tyler 00:18:35 Okay, I can probably clean this up as well. These are the sub-issues of the SDK observability, we don't have to go through that. The other ones, though…
Let's see where we're at.
Oh, no, this is not right, sorry.
My filtering is off. We can just do this for now, I can clean up this board later.
And… go through here. So, RESTful, then? David, this is assigned to you.
Thoughts on priority and size?
David Ashpole (dashpole) 00:19:22 Size? This is gonna be the same size as all the other… Stabilize…
Tyler 00:19:29 So the hotel HTTP, I think, is large. So…
I think we've put for all the other, like, detectors and things, like, mediums or something like that? I mean, I…
David Ashpole (dashpole) 00:19:40 You can put it as medium, then. Hopefully, stabilizing OTel HTTP will just give us a roadmap for how to stabilize
Some of these.
Damien Mathieu 00:19:47 I think Autel HTTP is the big one, and every other HTTP library is going to flow from that.
Tyler 00:19:55 Right, right, correct.
Yeah, the audit HTTP is part of this issue.
Damien Mathieu 00:20:01 Yes, I mean, Audit AutelHTP was kind of created as a release V1, steps before releasing V1, so they are slightly similar.
Tyler 00:20:13 Yeah.
So Damien, maybe I could just ask you, what are your… I mean, I'm guessing this is a large, would you say it's an extra large?
Damien Mathieu 00:20:20 Either large or extra large, maybe in between. I don't know, can we put a medium-extra-large?
Tyler 00:20:27 Extra, extra large?
Damien Mathieu 00:20:28 Yeah, let's pretty large, I guess.
Tyler 00:20:30 Okay, cool. And this is, again, categorizing just for, like, understanding what we expect now compared to, like, at the end of the year when we go back and reflect on this, so,
Yeah, I think it… we can probably change this if we need to, but yeah.
Priority, I think, is definitely high. This is definitely one where we want to try to stabilize it, so I think this is correct. Similarly, then, this becomes similar, the audit is a big part of this task.
So, obviously there's, like, the releasing part, and then there's, like, the other small cleanups, but I would say that this is the majority of it, so I'm just gonna leave this as, like, coupled. We need to probably link these two somehow, or clean.
Damien Mathieu 00:21:05 I agree.
Tyler 00:21:05 Or… yeah, so we'll work on that. But,
Yeah, so let's just leave that… leave it like this. Okay, so then, David, based on the large here, medium seems reasonable, right, for this?
David Ashpole (dashpole) 00:21:18 Yep.
Tyler 00:21:24 I didn't hear you if you said something, but… Oh.
David Ashpole (dashpole) 00:21:26 Yes.
Tyler 00:21:27 Okay. And then, priority-wise, on Rotel RESTful, like, this, you were saying, is used by the Kube API, or something in Kubernetes, and so…
David Ashpole (dashpole) 00:21:36 Yeah.
Tyler 00:21:37 So it seems high, but you're also the person there who would know better how important this is to stabilize for that project.
David Ashpole (dashpole) 00:21:44 I mean.
It's not particularly important, in the sense that, like, breaking it would be not very nice.
But also, marking it one dot, like, nobody's asking for that, at least not yet. Okay.
Tyler 00:22:02 Maybe we just put this as a meeting?
David Ashpole (dashpole) 00:22:03 I honestly consider this medium or even low.
Tyler 00:22:09 Yeah, I'm… I definitely… I think it should be lower than the hotel HTTP based on that, and then… I'm happy to put low as well, if you think low, but…
It's more on, like, you're the shepherd here, you tell me how you want to prioritize people working on this.
David Ashpole (dashpole) 00:22:21 Let's… let's do medium. Medium's fine. I would be very pleased if it…
got stabilized along with all the other HTTP-related things.
Tyler 00:22:31 Okay, cool. Let's do that.
Perfect. So then similar, David, for the runtime, actually, I guess I missed this…
Oh, this is coming from the hotel HTTP.
I don't know if this needs to be classified, this is a part of a…
this other task. Okay, so let's keep going. So the runtime, priority, and then size.
David Ashpole (dashpole) 00:22:53 I actually consider this high priority, and size… Maybe medium.
Tyler 00:23:03 Okay.
David Ashpole (dashpole) 00:23:05 It's fine.
Tyler 00:23:07 And then update runtime instrumentation to new semantic conventions, so this is definitely a part of the runtime stabilization effort, so… Yeah.
David Ashpole (dashpole) 00:23:13 The only thing we haven't done here, this is size low, the only thing we haven't done is remove the old ones, and we're just waiting to have the…
Some replacements for metrics that… People miss when they got the new ones.
Tyler 00:23:26 Right. Okay.
Okay, cool, that sounds good then.
I think this is actually looking great.
Okay, next up is the Hotel Mux. I don't have an owner here. I definitely think that I would say Medium and Medium, based on similar for the Hotel Restful. I don't think that it would be much different than that.
And same for…
Jin and Echo, I'm gonna put the same. And if folks think otherwise for any of these, please let me know.
Okay, and,
We have this deprecate, the probability consistent, sampler. Robert's already taken that, he's already classified it, looks great.
Last one is the exporter for Prometheus, and stabilization of that.
That's, again, a David task.
David Ashpole (dashpole) 00:24:20 I consider that priority to be high, and the size to be… I'll call it large.
Tyler 00:24:29 Okay.
Pellared 00:24:32 large, given this, you know, the specification is all unstable?
David Ashpole (dashpole) 00:24:36 It could be extra large as well, it… yeah, sure. Doesn't matter.
Tyler 00:24:41 Let's do that, then.
Okay, what is this?
Yes.
I think I skipped over this.
So, scarthian environment variable propagation, this was just something that was included.
No owner, we have a priority low,
I'm guessing this is a new propagator, so more than just a small task, and it's gonna add a new package, I'm gonna put medium on this one, here. Okay.
Okay.
This, let me see… Looks like my connection is unstable.
I'm gonna try to filter out, some of this stuff…
I think that is… good…
No, this doesn't have a parent issue either, but it probably should be linked. Anyways, okay,
That being said, I want to maybe just kind of go through this and,
look at assignment of, sponsors here. Obviously, like, the sponsor's not in charge of getting it done, but I think that I just want to, like… I mean, I was kind of noticing this, that, David, you have a lot assigned to you right now,
Including, like, some 1, 2, 3 very large tasks here. Yeah. So obviously, you're gonna need some help on this one, and I… I was just wondering.
Pellared 00:26:27 Based on this.
Tyler 00:26:28 like…
Do you think that we're gonna be able to successfully accomplish all of these things within this 2026, timeframe?
David Ashpole (dashpole) 00:26:38 Let's see… My goal is to get the… metrics, SDK optimization, and…
Yeah, I think I have 3 main things I've focused on. It's the runtime metrics.
Pellared 00:26:53 the…
David Ashpole (dashpole) 00:26:55 Metrics SDK optimization and the Prometheus Exporter are my… the ones I'm, like, actually…
Yeah, so… Yeah, so those are the ones I actually care.
Tyler 00:27:06 I'm kidding.
David Ashpole (dashpole) 00:27:07 The other ones, I'm… Very well may slip, yeah, and not get done without other people being interested.
Tyler 00:27:17 Okay.
Do we want to take them… do we want to take any of these off of our goal list for 2026? The thing that I'm coming to is just, like, these…
Low-priority ones, it seems like something we may just want to remove.
David Ashpole (dashpole) 00:27:34 I feel like low to me just means nice to have.
The only one that I think could be debatable
would be, like, hotel restful, but it feels like it would be nice… I would hope that maybe as part of the hotel HTTP stabilization, that,
Some of the, like, pieces of that end up being done anyways, you know?
Tyler 00:27:55 Yeah, see, the thing is, is I'm with you on the… the mediums feel like nice-to-haves, given what you just said about the top… your top priorities, and, like, their… your capacity. The lows, they don't even seem like nice-to-haves, they seem like,
not gonna happen.
David Ashpole (dashpole) 00:28:11 We can remove them.
Tyler 00:28:12 Okay.
Yeah, I just don't want to, like… the thing is, is that when it's on the board, we commit to it in some people's eyes. I don't think that you're committing to it, is what I'm thinking here, is what I… so I just want to make sure this is kind of communicated, outwardly, that way.
David Ashpole (dashpole) 00:28:25 Yeah, let's remove it then. Okay.
Tyler 00:28:28 Let's remove the project, and I can clean this up afterwards.
David Ashpole (dashpole) 00:28:36 Yeah, I don't know if it's this way at other companies, but it's kind of the, like, P3 means it's not gonna happen.
Tyler 00:28:45 Yeah, it, yeah. It's not P1, because there's about to be more P1s coming in anyways, but yeah.
Yeah, until P0 is developed. Anyways, none of the…
program management jokes. So, next up, Damien, there's two issues assigned to you, and this is all the same issue, so this is the stabilization of the hotel HTTP. This seems like something we should be able to accomplish within the year, right?
Damien Mathieu 00:29:13 I really hope so.
Tyler 00:29:16 Yeah, you also are out on paternity leave?
Damien Mathieu 00:29:20 Yeah, that's kind of the…
maybe that's problematic, but at the same time, most of… like, I'll be away from, like, end of April to September.
Tyler 00:29:30 Okay.
Damien Mathieu 00:29:31 So it's also, like, the summer is a lower time, at least for Europe.
So… Yeah, I don't… Yeah.
Tyler 00:29:42 Okay, that sounds good.
Damien Mathieu 00:29:43 If someone wants to… it's also something that's, that has a lot of first-time contributors making changes, so…
It could also be a question of, like, while I'm away, creating issues and assigning them for good first tag, so that things move forward without necessarily a lot of maintainer, codes work.
Tyler 00:30:07 I, yeah, I agree. I think if we can get a good understanding of where we want to go with the package, and then do a really good job on, like, farming out and, like, identifying issues and clearly scoping each one.
we can get some sourced help, and I think if that's the case, we can also try to find a new shepherd as you go to paternity leave over the summer to see if we can keep progress going on this. So I think there are strategies we can go here. So I think this is a reasonable goal, then, I think, for the year.
Okay.
Flc, I think he's got, or they've got, OTEL Echo, seems reasonable, but they're also not here to talk about it, so…
I'll leave it like that.
Next up, I've got the rest of the SDK observability, the file-based configuration.
And then, working with the enable method for synchronous metrics instruments, I think the only one that is kind of questionable is, like, this file-based configuration, whether it'll actually get done, as we've kind of pointed out how large it is. Otherwise, I do think this is reasonable to get done on my end.
I don't see any problem accomplishing these goals, so I'll leave that.
This W3C random flag, the owner… Is…
not here either. So yeah, then I think we'll just leave that as a task.
Robert, you have 3 tasks assigned to you right now. We have the logs API, the deprecation, and then the support… support the environment variable, propagation, so it looks like you picked up 3 of them. This all seems reasonable to… or does this seem reasonable to you to accomplish within this year?
Pellared 00:31:46 In the last one, I will say that I'm tracking it, because I'm not sure if there's community that means this propagator is in alpha stage in… it's in alpha stage in,
in the specification, so just… I don't think it needs to be on the roadmap, in my opinion.
Tyler 00:32:06 I don't either. That was actually where I was going with this one as well.
Pellared 00:32:10 Yep.
Tyler 00:32:10 So, I was actually happy to remove this. I… you assigned yourself, so I wanted to get your opinion on it. If you think it should be removed, I can remove it right now, though.
Pellared 00:32:17 I think it should be removed, I'm just assigned to myself, just to make sure that someone is, you know, responsible and looking at it.
Tyler 00:32:25 Okay.
I also think that if you don't get to it within this entire year, I think that's fine.
Yep. So just heads up on that, yeah.
Pellared 00:32:33 Okay.
Tyler 00:32:36 Okay. Then…
Pellared 00:32:40 This last one is from another user as well, I'm gonna leave that here. This is a…
Tyler 00:32:44 sub part of the audit HTTP…
I think I figured this out the other day.
Damien Mathieu 00:32:52 Yeah, it's part of HotelHTTP,
I think… yeah, we have a deprecation PR, and we just need to, merge the move on.
Tyler 00:33:02 Okay.
Yeah, so I'm not… I think this is fine. I don't know size-wise, it's not…
It's just a part of, existing issues, so I'm gonna leave it here.
The last up, though, are the OTEMUX, OTEL Jin, the Lambda detector, Azure Detector, and Jaeger Remote Sampler. These don't have owners,
I would say for these last three, we've identified as low priority. We might just want to remove them from the project board. Is there any opposition to doing that?
Yeah, okay. Then, yeah, I'm just gonna do that. Let's just do that. Maybe. See if Zoom lets me do it.
BhupinderSingh 00:33:46 Who do?
Hello.
Tyler 00:33:49 Is someone talking?
Yeah. Oh, Boopinder, yeah.
BhupinderSingh 00:33:53 So I think, can I get, like, the law priority one?
If possible, if this is the right way to go forward. I'm not sure.
Tyler 00:34:03 That all depends on, I think, how familiar you are with Go and our packaging structure and the project. So, it's a low priority, doesn't mean that it's a trivial task, is, I think, what I would make sure that you understand.
you know, this requires you to do an audit of an existing package for the idiomatic nature of Go and our project standards, as well as, like, the usability from a user interface perspective.
And then go through a stabilization process, which is extremely, like, technical and… sorry, not technical, it's extremely sensitive to the correct,
policies and approaches, because getting it wrong means that you're going to break some people. So, I… I'm happy to assign it to you, but it's… don't infer from it being a low priority, meaning that it's a trivial task, if that makes sense.
Damien Mathieu 00:34:51 And.
BhupinderSingh 00:34:52 Oh.
Damien Mathieu 00:34:52 I would add that, not, like, being assignee here means being owner and kind of responsible for the completion of that. It doesn't mean that you cannot work on that if you are not assigned. So, you can also not be assigned, but still look into it and make suggestions, and open PRs.
BhupinderSingh 00:35:14 Got it, yeah, thank you for the explanation, Tyler and Tammy. Okay, I think… looking at the…
points which you have explained, Matera, so I think, let's leave it for a while, then.
Tyler 00:35:26 Okay.
I'm gonna remove these, continue removing these. I would just say, Bupinder, like, if you wanted to take a look at those, like Damien was saying, you don't have to be an owner, but I would probably pick one that is a higher priority. You know, if you wanted to do a review of something that is already even owned by somebody else, like, that's welcomed, that's actually appreciated. Oh, man, I don't know how to get rid of this. Oh, okay.
So yeah, I think that, like.
maybe I would recommend not even looking at these, as this isn't a priority for us, but yeah.
Okay.
Last up are these hotel maximum intelligence. I would say maybe, let's take a look at the owners here.
As I think the last task is just finding an owner to see if they want to work on these, and I think I would say that's based on the code owner.
if the code owner is not able to actually accomplish that this year, I think we should take these off of our priority stack. So…
Damien Mathieu 00:36:22 It's the wrong type, but I think it's…
Tyler 00:36:27 Owners, code owners…
Flc and… where's Mux? Alex Katz. Okay. So yeah, both Alex and, FLC. So we can ask them if they want to also take ownership of these two…
tasks, why don't we just do this asynchronously, so then…
And, let me see, Jin and Moxie…
Okay.
I will… we'll wait on those, but otherwise, I think if they're not able to commit, then let's remove these from the, project board. Otherwise, I think this looks good. So, yeah,
That's a lot. But yeah, I think that we've gone through it, so yeah, we've got a fair amount to actually try to keep working on, so…
Cool. Alright, next steps, I think, is just, jumping in. I'd like to get, some sort of blog post together. In that blog post, I'd like to, like, includes a recap from last year and what we've been able to accomplish. I can take the action item to start working on that. It probably won't be until…
Next week, though. So, yeah, just kind of a heads up on that one.
But otherwise, yeah, I think this is a great goal. Let's just try to communicate this out to the community. I think I'll wait till I hear back from Alex and FLC on these before I publish this, or just announce this in the Slack channels as well, but yeah, this looks good.
Any other topics on this, or is everybody okay if we move on?
Okay, awesome.
David, you want to talk about bound instrument updates?
David Ashpole (dashpole) 00:38:53 Yep, I just wanted to… I've been working on a prototype
wanted to share a little bit of the interesting pieces of it. So I guess the first…
Top line summary is that
I am able to get the performance that I was looking for, or that I expected, based on the other prototype that I did, so…
You can see in the benchmarks section.
Some of the numbers are slightly different. I've found that actually, adding… if you use the defaults for the SDK and don't have an exemplar filter, then checking the context to see if your trace is sampled is more expensive than
Most of the other things.
So, the benchmarks are not as interesting if you have that enabled, but you can get very…
Cheap counter increments with the pre-computed case with bound instruments, as you would expect.
And the other cases are also
In line with the other prototypes I did.
So, overall, seems pretty good. There's some worrying, like, plus a thousand percents here.
don't worry about those, those are just because I didn't bother trying to preserve the existing performance, and if we actually did this, we could
Keep the existing performance of, like, with attributes set.
At least for a while.
So, if you can find the example test, file here.
I think this is the other, like, interesting part that…
People might have opinions on, or at least… be curious about.
Synchronous… there's a few questions. One is…
Should we do this just for synchronous instruments, and view it as a performance improvement, or should we try and have asynchronous instruments support this
Way of passing attributes as well.
I'm kind of ambivalent on it.
It does enable some more interesting,
Patterns within the asynchronous instrument, where you can
so the way I implemented it, it… Because currently you pass attributes.
to the observe in 64 call.
on… you're observable.
I put the bound
or the bind, basically, to attributes function on the observable itself. So, the way it works is you would just bind your observable to attributes and then do your increment, like you see on lines 87 and 88 here.
The other way to implement.
Tyler 00:41:38 But you're doing this in the… in the callback?
David Ashpole (dashpole) 00:41:41 So this is within the callback.
Right.
Tyler 00:41:45 Why would you want to do that, though?
David Ashpole (dashpole) 00:41:48 Sit… I…
just for… so the only reason I was… I was trying to ask a few questions. One is…
Let's see, so one of the other things that's been proposed is doing a… Multi-synchronous measure call.
Where you would want to bind
To a set of attributes once, and then increment, like, dozens and dozens of different counters, for example.
Or histograms, or other things, all with the same attributes, and you would want good performance when doing that.
there's the… if you look… read the issue for Bound Instruments, that's one of the things that GRPC has asked for.
You can go find it. But basically, there are some cases where, for synchronous instruments, we want to be able to bind to
a single set of attributes, and then increment a variety of instruments with it. So, this would be adopting that pattern, but for asynchronous instruments, where the performance doesn't usually matter that much.
So…
I… the example use case I would maybe give is if I was trying to implement, like, C-advisor metrics.
using the Go SDK. I could bind to the container and pod and whatever labels.
And then increment a bunch of instruments, or set them, or whatever.
Observe the memory usage all for the same, and it would be kind of clean.
Right.
But it's more, this is an area of feedback. I can also just exclude this from the proposal if we feel like it's not…
not useful and or confusing. The other option is that you would actually take
the instrument itself, this heap ALEC, or GC count.
And bind that before you pass it.
And that could, in theory, also work just fine. It doesn't… from the API perspective, it doesn't actually matter.
The nice thing about… being able to bind to heap Alec and GC count, the instruments itself.
is that you could do that outside of your callback. So you could bind, and then within the callback, you wouldn't have to rebind, ever. You would just, like.
be able to use… Yeah, I… that's how I envisioned it being used.
Tyler 00:44:09 It just seems like… I think what I'm seeing here is a lot of, like, a pattern
that I'd rather not try to promote, or this is, again, like, this is, again, becoming, like, a user…
A different way for a user to, like, configure attributes here.
David Ashpole (dashpole) 00:44:26 Yeah, so,
Right, right. So, let's… let's maybe find asynchronous example. So these are all asynchronous at the top.
Tyler 00:44:36 Right, and the synchronous is right here, yeah.
David Ashpole (dashpole) 00:44:38 Right, the synchronous is right there. So, with bound instruments, this is what a synchronous one would look like. And so, I think the question is.
Tyler 00:44:46 I think it's, again, like, I think one of those things where, like, I would envision it being something, like, more like this… this API counter would have already been bound to this
Approach here.
David Ashpole (dashpole) 00:44:56 That's the pre-computed case, right? So if you know ahead of time, then yeah, you would have already bound it to it, you would just be doing the add. So maybe I can add an example with that, but in the case where you don't know your attributes ahead of time, this is what it would look like, right? You would do, like, mycounter.withattributes.add, right?
Tyler 00:45:16 Yeah, and I… like, this is… this is, like, my worry, right? Like, I definitely do not think we should be promoting this, right? Because, like, now a user comes along and they go, like, well, why am I not using, like, the with attributes option here?
David Ashpole (dashpole) 00:45:29 Right, I would…
I mean, so this is more performant than with attributes, right? So that's part of the reason, is like, this actually does do better.
but, that is…
Tyler 00:45:42 I mean, but, like, yeah, like, I'm not actually asking you that reason, like, I'm actually… I'm trying to point out the user confusion here.
David Ashpole (dashpole) 00:45:49 Yes, I… my preference would be that
Our regular attributes options are deprecated.
Tyler 00:45:59 Yeah, I'm… I wasn't… I wasn't aware that was the plan, if that was the case. That… that seems like…
Very problematic to me.
David Ashpole (dashpole) 00:46:08 Why is… why do you think so?
We're not removing.
Tyler 00:46:10 Every other instrument that we, like, every other signal that we have, we pass options.
David Ashpole (dashpole) 00:46:15 with, like, the R option pattern.
Tyler 00:46:17 In the metric signal, we also pass options with our option pattern.
David Ashpole (dashpole) 00:46:22 Don't do that.
Tyler 00:46:22 how… What?
David Ashpole (dashpole) 00:46:25 We don't do this for logs, right? With logs, we have the log record that has attributes on it directly.
Right.
Tyler 00:46:32 Yeah, but there's still options that we're passing in calls there. Like, this is definitely something about our policy, like, of how we were passing things, right?
We definitely do not have this, and this was considered a part of the discussion when we talked about, like, configuration methods.
And so, like, I think that, like, saying, okay, if you want to pass a timestamp, you pass it with an option. If you want to pass a link, you pass it with an option. And then if you want to pass attributes, well, if you're in tracing, you pass it with an option, but if you're in metrics.
You need to do some method call to make this happen.
Like, that's… that's, like… That isn't…
David Ashpole (dashpole) 00:47:11 would… Part of me thinks we should extend this pattern to the Trace API as well.
Tyler 00:47:21 Yeah, I don't… I don't… Agree.
I would rather have a clean user interface where users are presented with a single way to configure options, and have an option pattern that is consistent.
Across option types, across option values, and across signals.
David Ashpole (dashpole) 00:47:40 the… So the other… The other pattern that we could…
Right, attributes are kind of special, because… I mean, I guess links are the same way, where if you're passing a slice of links.
It'll always escape.
And that's kind of unfortunate, but… .
Tyler 00:48:17 Like, I think that there's a world where you get some instrument and it has abound attributes to it, that makes sense. But at the call site where you're doing some sort of ad, or some sort of, like, recording of that value, I think that, like, we need to follow
Our existing instrumentation patterns, where we have options that are passed as options.
David Ashpole (dashpole) 00:48:40 So you think we should continue to support both the option version of attributes?
I was hoping that… well, my thinking was, like, this is more performant in all cases, right? And… I… well, hold on, I don't think that's the case. Okay.
Tyler 00:48:56 Because we've already talked about that, right? Like…
This is… this is the discussion we had last time, where, like, I think that there is a case where you can show that this is…
Equally performant, or, you know, within 50 nanoseconds of performance.
If you're talking about bound attributes. If you add a map.
David Ashpole (dashpole) 00:49:12 And yet you manage your own sync map?
Tyler 00:49:14 Sure. Like, there are ways to make the call site as performant as the other one. So, so saying that, like.
we should go this way because of performance, I think, is not the discussion we want to have, right? It's more around your user ergonomics, right? Like, the user ergonomics is around, like.
If you can make it performant while also allowing the extension and the customizability, like.
that's what we want. Like, we don't want users to have to manage external, like, caches and that kind of thing, so, like, if there are options and ways and patterns that we can do that, that makes sense.
But…
To say that, on the other end, users should come along and change how, in this one specific situation, you configure this option that you're passing.
That's also not what we want.
David Ashpole (dashpole) 00:49:59 Say that last part again.
Tyler 00:50:01 So, to say that users have to come along and decide that when they're going to pass this one specific option, namely, like, attributes, they need to use a completely different call pattern than what we've already, like, provided in the API in the past, as well as in other APIs.
David Ashpole (dashpole) 00:50:20 Yeah, I mean… I… I… I see that. I… it…
in some ways, it's like, I don't see attributes as… an option?
like… Hit.
You know, it's like, in hindsight, I might have preferred that attributes just be part of
The function signature, right?
Like, like, we don't pass values or contexts as optional parameters either.
But…
Tyler 00:50:52 Yeah, but those are because you have to actually provide this. Like, you can definitely do a recording without attributes. Like, that still is a valid call, right? And so…
Yeah, like, I don't think that that was the right decision to add those. I do think that, like, what'd be great is if you could do functional overloading, but, like.
I don't know why I'm bringing that up, but anyways, like, I think that there's just, like.
I, I like this idea.
Of having a bound attributes. I do wonder if that should be a part of the instrument, or if this should be a part of the meter. Like, if you ask the meter for some sort of, like, instrument with bound attributes.
I… I do wonder if that's maybe the case. I also wonder if…
But the thing is, is, like, I'm not… I'm definitely not in favor of deprecating what we have.
to promote this. Like, that is… that is, like, a big, hard… issue for me. What? Like…
David Ashpole (dashpole) 00:51:46 Scroll down… scroll down to one… let's see if we can find an example where we had the with attributes.
Call already on there.
Tyler 00:51:55 I think…
David Ashpole (dashpole) 00:51:56 Was there one?
Tyler 00:51:57 Correct me if I'm wrong, like, I'm not…
David Ashpole (dashpole) 00:51:58 It's there, it's the last line.
Tyler 00:52:01 Okay.
David Ashpole (dashpole) 00:52:01 So, you can see, I guess I just didn't wrap… Wrap lines properly, but…
Tyler 00:52:06 Yeah. The…
David Ashpole (dashpole) 00:52:07 like… The ergonomics aren't that different to me.
I understand that one is, like.
With attributes afterwards, and the other one is with attributes before.
Tyler 00:52:21 Yeah, but it's not… it's not actually… Before or after.
Like, to be clear, like, this is an argument passed to a function call, this is a method that is called on a type, and then the return value is then also a method is called from it. So, like, these are completely different call patterns.
And so, yeah, like, I see, like, your point, like, holistically, but, like.
I'm not… I'm thinking about user confusion of this API, right? Like, this… this mixes different attribute patterns here.
Or this mixes different option patterns here.
Damien Mathieu 00:52:57 I tend to agree that it's not really what we've been doing so far. I think the only thing, but I'm not sure it's any use, that would be nice here is that, with David's approach, you can store a bonded metric with, like, statically set attributes, and then you just define the method not caring about the attributes anymore.
later on.
Tyler 00:53:23 Like.
Damien Mathieu 00:53:24 Like, once you…
Tyler 00:53:25 I like that callback.
Damien Mathieu 00:53:27 Like what you have with log contexts, for example.
I'm not sure this is really needed for metrics, but it's the main advantage I see.
Tyler 00:53:36 Well, I think, from David's point, it is needed, because it provides a lot of performance benefits. And I like what you're saying, Damien, around that call pattern, and, like, how we promote it in that way, where, like, you have instruments that are bound.
But I definitely don't think that, like… like… and I'm all on board for all that, like, it's all a yes and. It's the part that you lose me is when you say that, like, we need to deprecate
this method in favor of people just doing this.
Damien Mathieu 00:53:59 We should not… we should not deprec… I mean, we can't deprecate. We're stable.
We can't…
Tyler 00:54:05 deprecate. You just can't…
Damien Mathieu 00:54:06 Yeah, we can't… we can't remove, anyway, and duplicating is…
boring and go, because it's really a lot of warnings.
David Ashpole (dashpole) 00:54:12 is because then we have two ways of doing the same thing, right? And one way is…
is, like, an option that really nobody should ever use, right? Because it has very, very poor performance.
Right? And the other one…
Tyler 00:54:28 Yeah, but that's assuming that everyone sees the worldview.
David Ashpole (dashpole) 00:54:31 Right, wrong.
Tyler 00:54:32 Performance.
David Ashpole (dashpole) 00:54:32 do not care about performance, right? Like, and it's not, like, the only thing that matters, of course.
But, like, in all.
Tyler 00:54:41 So, I mean, I think if that's the case, like, I don't think we can deprecate it based on, like, that.
Is what I'm saying.
Damien Mathieu 00:54:48 I think we can duplicate, just because there are two ways to do something.
David Ashpole (dashpole) 00:54:53 That's right, so my thingy was more, like,
Like, we… we probably…
Yeah, so, like, if I were to write our doc, like, let's say we introduced Bound Instruments, and then we were writing our, like, OpenTelemetry.io documentation, it's like, what are we actually going to use everywhere?
And… like… My assumption was that
We would actually tell everyone to use the bound instrument pattern, because…
from a readability standpoint, it seems about as good, like… And from a… Performance standpoint, it is… better…
by some margin, depending on how performance-sensitive you are, right? That, like, our recommendations would always be to use this new pattern.
And… That led me to the thought of, like, well.
Should we be steering users towards it?
like, more… Like, more clearly, and using the tooling available to us.
I obviously don't think we can remove…
Damien Mathieu 00:56:01 Yes.
Yeah, I agree.
Tyler 00:56:03 I don't agree.
Damien Mathieu 00:56:04 I agree.
Sorry.
Tyler 00:56:06 I agree, that's…
Damien Mathieu 00:56:08 In the sense that, yes, we can change the methods, yes, we can change all docs, so that anyone looking only at the documentation and examples will never know that you can call it that way. I'm not sure it's worth
deprecating, based on the stability of the library and, and…
the fact that it just works, we can probably remove it in V2.
David Ashpole (dashpole) 00:56:36 Right, I mean…
Tyler 00:56:39 So we're not gonna have a V2 of the API. Like, that's definitely not on the.
Damien Mathieu 00:56:42 Yeah, I mean, I'm not saying V2 in V4Card future, like, I don't know, maybe in 10 years.
Tyler 00:56:49 I don't think that's ever gonna happen, to be honest.
like, the API stability is really important. The SDK versioning is definitely a helpful thing. But, like.
Damien Mathieu 00:56:58 Yes, my meaning was more, if one day we have a V2, we can remove it, not saying that we are thinking about V2.
Tyler 00:57:07 Yeah, but what if that never happens, is my point. Consider that. Now we have this API, and we have this deprecation, and this thing is, like, a duplicate way to actually assign this.
Damien Mathieu 00:57:16 is an.
David Ashpole (dashpole) 00:57:17 Yes.
Damien Mathieu 00:57:17 That kind of a fate of, stable projects over time?
David Ashpole (dashpole) 00:57:23 I think that's, like…
Tyler 00:57:24 Stable projects over time can evolve in certain ways that the OpenTelemetry API cannot.
Damien Mathieu 00:57:31 Yes.
Tyler 00:57:31 This is.
Damien Mathieu 00:57:32 What I mean, what I mean is, isn't that, like, the fact that the API is growing, and there are duplicated things, isn't that the, like, kind of fate of things being stable and not being able to remove things?
Tyler 00:57:47 I think that makes an assumption that things are growing. Like, this is the conversation we're having right now, is how this thing grows. And this is what I'm saying, is like…
this needs to… we need to consider this, and it needs to be more important than, I think, is giving weight to it right now.
I think that just saying that we're gonna add a new method to configure attributes is not an appropriate thing to say as a replacement for what we have.
David Ashpole (dashpole) 00:58:13 But wouldn't… sorry.
But the new method would be better, right? From an ergonomic standpoint and from a performance standpoint.
Tyler 00:58:22 No.
This is our… this is our disagreement. I think from a performance standpoint.
I think they're similar. I think you can get similar performance as we've already shown.
I think from an ergonomic standpoint, it's worse. This is the whole point, is that I'm trying to make, like…
All of our code uses this pattern.
This does not use this pattern.
That is a bad ergonomic standpoint.
Damien Mathieu 00:58:45 I think if there is a clear, performance improvement, it's worth it. If there is no clear performance improvement, it's not worth it.
Tyler 00:58:58 Yeah, and I think we've talked about this in the last meeting and the meeting before, and other issues, like…
You can get similar performance from the existing pattern.
It's just that the ergonomics of trying to do that are not conducive to what we want to promote. You have to maintain existing caches and sync maps outside of this.
David Ashpole (dashpole) 00:59:18 Okay, are people on board if this is purely an addition?
If we don't deprecate the old options. Actually, I did have a… Before I get to that.
How do you feel about… attribute.
New set.
Versus with attributes. Because…
Tyler 00:59:37 Yeah, I… I'm… I love that idea. I just…
I've thought about it before. It's a hard one, though, because you still have… like, the attribute.new set, you still have to do, an allocation to make the new set, right?
David Ashpole (dashpole) 00:59:53 Well, so I would actually deprecate attribute.new set and deprecate attribute.set.
As the only deprecations.
Tyler 01:00:03 Hold on, maybe I'm not following this. So, in the attribute package, the new set and the set type itself, you would deprecate, you would replace it with what?
David Ashpole (dashpole) 01:00:16 that you would just pass… you would use the with attributes option. So…
Tyler 01:00:20 Oh, oh, I see what you're saying, I'm sorry. So, in the metric package, you're saying the with attribute set option would be deprecated, and we'd promote the width attribute?
David Ashpole (dashpole) 01:00:29 Here's my thinking, so… without… or… Let's see.
With attributes set, is most useful.
When you are in a performance… today, when you're in a performance-sensitive situation, and you've pre-computed the attribute set.
In all other cases, it's actually equivalent-ish performance, right? Because you have to make the new set each time anyways, and…
Tyler 01:00:56 Right, right, right.
David Ashpole (dashpole) 01:00:57 So… We like with attributes set today because…
it's the most performant option. But if we introduce bound instruments, now we have… if you're actually performance sensitive, this is where you're gonna go. So, the idea would be…
We introduce bound instruments.
And we deprecate With attribute set, and attribute.new set.
And then all of our APIs consistently use with attributes, like…
Or I don't know, I don't think logging does, but…
the Trace API and the Metrics API look a bit more similar then.
And the metrics SDK will still use something that's analogous to an attribute set internally.
But we can make that an internal package, and make it not comparable.
And get some better performance out of it, like, whatever we want to do, right?
Tyler 01:01:51 So, that can just, like…
David Ashpole (dashpole) 01:01:54 We can forget that attribute sets ever exist.
ish.
And then…
Tyler 01:02:00 Journal, yeah.
David Ashpole (dashpole) 01:02:02 We could have, with attributes the option, Which is less performant, but not terrible.
For the dynamic case, and then we have the with attributes, the bound version.
Which is excellent in the bound case, and…
slightly more performant in the dynamic case, but only matters if you're performance sensitive. So that's the other, like, proposal I'll put forward.
Tyler 01:02:29 So I… I… I like that.
I don't know if I've thought all the way through it. I think I'd have to look a little bit more, especially the deprecation in the attributes package. I think that, like.
David Ashpole (dashpole) 01:02:43 Sorry, I also know we're out of time.
API. Yeah, yeah, we're out of time.
Tyler 01:02:46 Yeah, I know, I know.
David Ashpole (dashpole) 01:02:49 Thank you.
Tyler 01:02:51 But I do like that. I'd like to see more on that one, yeah, like, maybe we can talk more on that one, or I can… sorry, I haven't been following too closely, but, like, is there a PR that you have done this?
David Ashpole (dashpole) 01:03:01 where I have… Where I've deprecated attribute.set.
Tyler 01:03:08 Yeah, and the with attribute set method as well.
David Ashpole (dashpole) 01:03:14 I haven't deprecated it. I think the thing that you would need to do to convince yourself that it's the right idea
It's just search for attribute.set, and note that it only exists in the metro.
Tyler 01:03:24 Oh, no, I've already done this. I know exactly… that's why I'm already on board. Like, I've always wanted to do this, because I don't think it ever should have been released in the first place, but I just, like…
yeah, I feel like…
David Ashpole (dashpole) 01:03:36 If you look at any of the prototypes.
There's only one case where the performance of with attribute set and with attributes differs.
And that is in the, and because the new benchmarks have, like, side-by-sides for everything.
And the… so I've done, like, 3 or 4 prototypes now.
they're always the same, except in the pre-computed case, right? So the pre-computed case is where attribute set is super nice to have, and everywhere else it's, like, not relevant.
Or they're usually within about 5 nanoseconds of each other for a, you know, thousand nanosecond.
Tyler 01:04:13 Yep.
David Ashpole (dashpole) 01:04:14 Right, right.
If that's the evidence you're looking for, I can try and dig that up and ping it to you. But…
Basically.
Tyler 01:04:24 No, I think just from, like, from the API ergonomics, though, is more where I'm thinking about it, and that makes more sense to me.
Cause, like, we…
Damien Mathieu 01:04:31 I agree, I actually wouldn't…
Tyler 01:04:32 Yeah.
I like what you're saying in the fact that, like, we would still have an option pattern for users to follow if they wanted to continue to follow from our standard API. It would actually remove the duplicate option pattern, or wouldn't remove, it would unify the option pattern to say, like, use this one, not this one.
And yeah, I think that that makes a lot of sense to me. I do think that the attribute set in the attribute package
We can't ever get rid of it, but it's horrible. So, I like the idea that you just had. Okay.
David Ashpole (dashpole) 01:05:03 Okay.
Tyler 01:05:04 We are…
David Ashpole (dashpole) 01:05:05 Cool.
Tyler 01:05:05 Overtime.
David Ashpole (dashpole) 01:05:06 Yep, thank you.
Damien Mathieu 01:05:07 Yeah, just, one thing to mention about the weave attribute we discussed before, it's going to be very quick, but shouldn't that go through a specification, this kind of API?
David Ashpole (dashpole) 01:05:17 Yes, I… so, I'm doing prototypes, but…
Without the support of other maintainers, it seems like a bad idea to open spec PRs that our SIG would not implement, so…
Damien Mathieu 01:05:27 Okay, okay, so your intent was not to just add it to our API, but to, make it better.
David Ashpole (dashpole) 01:05:33 I have a spec already written, it's in draft, saying I need to get agreement within the GoSig.
Hmm, was there anything else?
Damien Mathieu 01:05:45 So since we're over time, there is one last item. It can be very quick. We have a labeler in HotelHTTP which, allows setting custom metric attributes through the context.
It's a bit of repetition with, with metric attributes error function, and it's been suggested to remove duplicate.
The issue is open and waiting for reviews and opinions, so if you could give your opinion on, deprecation, the PR is ready to be merged, so it would be nice.
Alright, talk to you later.
