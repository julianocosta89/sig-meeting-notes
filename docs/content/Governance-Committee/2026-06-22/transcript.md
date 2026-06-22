SIG: GC Project Management (EU)
Date: 2026-06-22
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Severin** 00:06 Hey, Pablo, good morning.
**Pablo Baeyens** 00:09 Hey, good morning! How's it going?
**Severin** 00:12 Good, and how about you?
**Pablo Baeyens** 00:14 Oh, I'm doing fine, too hot, I guess… I don't know about Germany.
**Severin** 00:21 Yeah, a lot of places in Germany are really hot. We are semi-lucky right now, because it rained yesterday, and it's still very cloudy, but I think give it a day or two, and then, like, humidity will kill us.
**Pablo Baeyens** 00:35 Right.
**Severin** 00:36 Because, like they said, like, at the weekend, we have 36, 37, something like that.
But I enjoy it as long as it is going, so… I don't know.
Yeah, it's 20 right now, so this is really, really cold compared to the last few days, right? So…
**Pablo Baeyens** 00:57 Right, here, it's… must be around, yeah, 32.
**Severin** 01:02 Okay, you have an AC, I hope?
**Pablo Baeyens** 01:05 Yeah, yeah, I do, I do. Luckily, I do.
**Severin** 01:07 Germans don't, so this is still a thing, like, we have to figure out.
**Pablo Baeyens** 01:13 Right.
**Severin** 01:16 Oh, I have not been in those calls now for a little longer, so I'm not sure how we are doing on that end. Did you meet on a semi-regular basis, or…
**Pablo Baeyens** 01:25 Not really, no. There's, quite a big backlog, but I was talking with people that maybe we could automate some things, I… I don't know, I mean, maybe, for example.
SIG issue could be applied if the area is a particular one.
**Severin** 01:48 Yeah.
**Pablo Baeyens** 01:50 Things like that. We could try with LLMs, I don't know, like, I think it's worth trying, I don't know how good that would be.
Oh, f-.
**Severin** 01:59 Yeah, okay, okay, okay, okay, okay, that's… that's a little bit of work in front of us.
**Pablo Baeyens** 02:07 odd…
**Severin** 02:08 Do we want to… should I share my screen and we just go over it one by one?
**Pablo Baeyens** 02:14 Yeah, let's do that. I was just marking a few, save issues, because they are Prometheus-related. There's quite a few of those. But, yeah, if you can share your screen.
**Severin** 02:24 I need…
**Pablo Baeyens** 02:24 too good.
**Severin** 02:25 Zoom sharing permissions. It could be that I need to rejoin. Let's see… yeah, we'll be there in a second.
**Pablo Baeyens** 02:33 Okay.
**Severin** 02:56 Okay, now let me try it again… that looks better.
I need to find the right browser window.
Okay.
You see that?
**Pablo Baeyens** 03:16 Yeah, I can see it.
**Severin** 03:17 Oh, so let's go… Bottom to top again, I guess?
**Pablo Baeyens** 03:21 Yeah.
**Severin** 03:25 Allow adding a prefix to metric.
names… Oh, that's an old one that was just active.
**Pablo Baeyens** 03:33 Yeah.
**Severin** 03:36 Seems like a simple change across all languages, and would be really hard useful.
So let's do the triage first. This is triage community…
**Pablo Baeyens** 03:51 Yeah, I would say it's community.
**Severin** 04:03 should we tag someone, or should we tag the TC and say, like, hey.
Thoughts on that, or something like that?
I don't want to put it in their inbox, but still get, like… I mean, this is now, again, like, a month ago that, like, that person wrote to that, and… And I can recommend them, like, to go to this Sikh meeting and maybe get some attention back on that, so…
**Pablo Baeyens** 04:30 I think that is probably… best? Like, it's… Yeah, recommending that to embrace it on the spec painting.
**Severin** 04:50 What did I write? What do you… hoping you join this bank meeting on Tuesdays.
2… Bring this to… Everyone's attention, something like that.
**Pablo Baeyens** 05:10 Yeah, that makes sense.
**Severin** 05:11 Yeah, cool.
Cool, one less.
ECS service name attributes… that's also an old one.
**Pablo Baeyens** 05:22 I think this one, probably, we want to transfer to the semantic conventions.
**Severin** 05:26 Yeah, yeah. Oh, wait, here's, like, hey guys, I'm wondering, and it might be… Okay, yeah, let me transfer it.
to semantic conventions… in SEMConf, is there anybody who would own that? Like…
**Pablo Baeyens** 06:04 don't think there's a specific SIG that would own this, so I would put this.
**Severin** 06:12 SPAC sponsors, or just move it here and just leave it like that?
Or I can, again, like, say, hey, If you… 1, 2…
**Pablo Baeyens** 06:27 Yeah, I guess that's… That's part of this, yeah.
**Severin** 06:57 Apply attribute limits globally.
That's from Bert.
Okay… Is this… are you assigned sick issue to it, and then removed?
**Pablo Baeyens** 07:29 I think that was a mistake. Yeah, I was looking at that, but I'm not sure… I don't remember, but I think it was a mistake.
**Severin** 07:35 Hmm… But it seems to be something… That's been working on, right?
**Pablo Baeyens** 07:42 Yeah, I would say this is accepted.
**Severin** 07:47 Does it need a sponsor, or is it, like… Ready?
**Pablo Baeyens** 07:58 I guess this is… Ready? I… It doesn't seem like it's… too complex. It's…
**Severin** 08:10 Okay, then let me put it under ready, and not… Give it any more thought.
Should OpenTelemetry configuration be merged into SPAC?
Okay, community feedback… I mean, I can write a comment to bump it up, but on the other hand, I also don't want to take… responsibility for it, so I just triage it.
**Pablo Baeyens** 08:42 Yeah, I think we just triage it, and especially these ones that, it's been a while since.
**Severin** 08:47 Yeah.
**Pablo Baeyens** 08:48 They entered here.
**Severin** 08:50 Tracking issue for stabilizing, suggesting… prototypes…
**Pablo Baeyens** 08:56 I think this is…
**Severin** 08:58 Ready?
**Pablo Baeyens** 08:58 Yeah.
**Severin** 09:00 ready with sponsor, and I… I give it to Jack, or… Just ready.
**Pablo Baeyens** 09:07 We can put ready, and yeah, Jack can modify it if he wants to.
**Severin** 09:14 Ensure metric view config matches declarative configuration.
**Pablo Baeyens** 09:23 just deciding, and we ping Jack again, it's been…
**Severin** 09:34 Anything how we triage this just seems to be… Just signed in… Needs info in that case, right?
But not the authors, it's like… I give it community feedback.
**Pablo Baeyens** 09:51 That would put, yeah, good money to keep up.
**Severin** 09:58 Just give me a sec.
Cool.
community feedback… Matrix data model description of sum does mention that data points have values.
What does this even mean?
I can put, again, community feedback on it.
**Pablo Baeyens** 10:35 Yeah.
**Severin** 10:36 And then again, recommended, like.
**Pablo Baeyens** 10:42 Yeah, raise it on the… Spec.
I was wondering if we should move this to the proto, given that… Huh?
Well, now there's a data model for metrics in the spec.
Let's leave it here.
**Severin** 11:16 Is it called hotel-specification, or has this… Or is it hotel-spec? I always…
**Pablo Baeyens** 11:24 The… tunnel?
**Severin** 11:26 specific case.
**Pablo Baeyens** 11:27 Thing, yeah, specification.
**Severin** 11:30 Cool.
Then, let's go on. Attribute ordering is not declared in the specification.
Community Chief… Feedback, right?
**Pablo Baeyens** 11:45 Huh.
**Severin** 11:45 Oh, there's a lot of thumbs up.
**Pablo Baeyens** 11:52 Maybe we can ping Robert on…
**Severin** 11:53 No.
**Pablo Baeyens** 11:54 decide.
**Severin** 11:59 Bomb thing is just pumped.
Bring this up, okay.
fallback, fallover endpoint, support for OTLP exporters… Exists in Java… I would say also community feedback, and again, so like, hey…
**Pablo Baeyens** 12:39 Yeah.
**Severin** 13:12 I mean, now it's far from perfect to recommend people to attend the meetings and go to SPAC meetings, but, like, yeah.
**Pablo Baeyens** 13:20 I think it is the best to say it here, you know?
**Severin** 13:22 Yeah, yeah, but I mean, technically we say, like, hey, this should not be the case, but it's unfortunately very often reality that, like, if people are not Okay, there's a little bit of conversation going on on that.
Let me… community feedback… That allows… Always stack trace, and you never stack trace.
Those reasons, okay… Community… And span lifecycle operations to span processor.
So, just write something again, like bumping this up.
**Pablo Baeyens** 15:37 Yup.
**Severin** 15:48 Something like that.
Cool.
add built-in support for hotel event name attribute and log STA.
And let me… it's Unity Feedback… And, Just tagging people along, so… And build event routing.
Lock.
Processor… Hidden as off-topic.
Okay.
**Pablo Baeyens** 16:36 Hmm.
**Severin** 16:38 Community feedback?
**Pablo Baeyens** 16:41 Yo.
Most of these same.
**Severin** 16:43 I mean, I can ask Robert if this is still relevant, or… Mmm… Improve composability of metrics.
Here's… Your chief.
Just bumping it up, just not tagging anyone up.
call it a thing we have now done… Page 1.
**Pablo Baeyens** 17:41 Of? Yeah.
**Severin** 17:46 Yeah, I need to go.
That's broken.
Cool!
entities information from this year on how we solve some merging. I mean, this is a sick issue for entities, right?
**Pablo Baeyens** 18:07 Yeah, I would say that's a stick issue.
**Severin** 18:09 Do they have a board? Yes, they have. Okay, cool.
**Pablo Baeyens** 18:13 Yeah, it's already on the group. Okay.
**Severin** 18:17 Clarify recovery… semantic for oversized… to P, Export Requests… Yeah, that's something that we maybe really could automate. Yeah.
Mmm… Cool.
stabilize… This is a sick issue for CIDC DSIMConf.
Isn't this actually… Something that should live… Just happened.
Okay.
**Pablo Baeyens** 19:58 What happened?
**Severin** 19:59 My light turned on and off again, off and on again. I'm not sure why.
Okay… Is this a… no, it's not, because it's like… kind of specific to the CICD, but it's not, so… I give it a community feedback, and then…
**Pablo Baeyens** 20:33 Oh, sorry, I was muted. I will put it as ready, based on that last comment.
**Severin** 20:36 Oh, okay, yeah, ready.
Oh my god, bye.
I'm just copying… Like, the people rubber-tacked here, and… Retack them.
Publish specs at specs.opentelemetry and Exploratory proposal.
I like this a lot, I like… Yeah, I remember that we talked about this at some point.
Like this a lot.
Let me put it that way. I think… Right?
progress.
GitHub Copilotte code review instructions…
**Pablo Baeyens** 22:20 deciding…
**Severin** 22:22 Isn't that something that TC should definitely look into?
Your response?
**Pablo Baeyens** 22:33 My impression is of this hard.
support from the TC, but I… I don't know. Let me check if there's…
**Severin** 22:41 So I put it on community feedback, and just… bump it up.
Cool.
Something like that? I'm just doing it, I mean, I…
**Pablo Baeyens** 23:01 Yeah, I mean, I think that's fine, yeah.
**Severin** 23:04 start defining what is and makes a distro… I mean, that is defined, right? Like…
**Pablo Baeyens** 23:10 Yo.
**Severin** 23:45 I mean, yeah, it's kind of like, but…
**Pablo Baeyens** 23:54 I'm… I would put it as deciding. I think, in the end, it's… Not going to be necessarily something that only happens on the spec, but…
**Severin** 24:08 I mean, my point of view is also, like, sure, we could do a little bit of that on the spec.
But… I mean, at the end of the day, it can also be extremely language-specific, right?
**Pablo Baeyens** 24:23 Right, yep.
**Severin** 24:24 And the definitions that we have are not bad, right? They just say, like, hey, you can do less, you can do more, you can do different things, but… Here's some basics on it, right?
**Pablo Baeyens** 24:35 Yeah, yep.
**Severin** 24:36 I just triaged it, I mean, I can also comment on it, but, like, yeah, let's leave it like that for the time being.
**Pablo Baeyens** 24:42 I would leave it like that.
**Severin** 24:43 The problem is, like, this is a rabbit hole. We had these discussions in the past, so… Defined resource detector API? But we have a resource… don't we have a resource detector API?
I thought we added something like that.
**Pablo Baeyens** 25:01 I don't think that is defined… in a language-agnostic way, like, different languages do have.
**Severin** 25:24 Yeah, I mean, yeah… I don't know.
Let me give it a community.
And then just say something about… All right.
triage, if he can join the spec meetings on Tuesdays.
You can't… Issue.
24.
Also, sharing… Done.
Many more to go. 13, okay, cool.
Clarify default values for optional parameters.
That's, feedback, right?
**Pablo Baeyens** 26:32 Yeah.
**Severin** 26:33 Robert knows how to make things moving, so I don't need to… Had a comment.
**Pablo Baeyens** 26:38 Yup.
**Severin** 26:39 Yes.
Discovery of instrumentations, for dynamic… creation. It feels like that's very related to the other one.
I just triage it. I mean, I… I gave James, like, a comment on one of his issues, so I think it's just fine to know.
I did every time, right?
What do we have? Per protocol alternatives… Let me do it that way, community feedback… Those are the people that interacted, right? So, yeah.
Span flag to indicate metric exemplar references… back.
Should I write any comment below it, or… I mean.
**Pablo Baeyens** 28:14 No, I think…
**Severin** 28:15 I mean, Josh knows his ways, right, so…
**Pablo Baeyens** 28:18 Yep. Yep.
**Severin** 28:20 declarative call.
per component, huh?
That's a… Big issue for config, right?
**Pablo Baeyens** 28:29 I… Yeah, but there's no… the class configuration sake anymore, so I would put it as deciding community feedback, and yeah, I would encourage… Roger to go to… This is a state call, yeah, to a spec call.
**Severin** 28:52 Okay.
I'm hanging right down.
**Pablo Baeyens** 29:20 Yep.
**Severin** 29:21 Finding the words every time. Get all applicable instrumentation level settings.
Again… giving you the community feedback. I mean, I said to James already on another issue that he should join this back meeting, so I don't think there's… And there's another one… And another one… and supplementary guidelines for SDK, self-observability, community… I need one egg.
I mean, CJoy also knows what he needs to do if he wants more attention to that, right? So…
**Pablo Baeyens** 30:22 Yep.
**Severin** 30:26 Consider cross-language guidelines for instrumentation library authors.
Oh, that's like… I mean, don't we… it's just, like, not related to this thing that… Like, the whole project from… from… From Casper.
The maturity model thing.
**Pablo Baeyens** 30:52 Awww.
**Severin** 30:53 Maybe? I mean, it's like guidelines for cross-language Instrumentation library authors.
**Pablo Baeyens** 31:00 My reading of Cats per project was more, like.
For things not necessarily within the project.
**Severin** 31:08 Yeah, yeah, but instrumentation libraries, I mean, are also not necessarily inside of the project, but I get your point. I mean, there's some… There's some relationship to it, but, like, But also the question is, like, does this need to live in the spec, or should this… Be it docs.
thing.
**Pablo Baeyens** 31:33 Yeah.
I would… ordered us… deciding community feedback, and let CJO do his thing, his…
**Severin** 31:48 Okay, yeah, cool. Then, like… I just leave it like that.
3 more to go… deprecate text map extract keys… Okay… I just label it Community Feedback. I mean, it's 2 weeks old, so it's not like maybe people have just missed it, or whatever.
**Pablo Baeyens** 32:19 Yeah.
**Severin** 32:20 write something about, like, joining the SPAC meeting.
I leave it like that for the time being, I mean, I'm just like… Same for Ruby, that's also community feedback, and it is active, so I would… Unity to feed back… That's sampling, actually, right? Isn't it a stick issue, sampling?
**Pablo Baeyens** 32:56 Yeah, there's the something sick.
**Severin** 32:57 I have a dashboard.
Simpler.
Yeah.
Cool.
At least we… Yeah, to that point.
Trina, follow up.
That will look horrible. Oh, 11, that's okay. I was much more worried. Cool.
providing a way for knowing when the context is made current, Okay, I will just… Possibly.
**Pablo Baeyens** 33:35 Yeah.
**Severin** 33:36 And again, and… yeah.
Follow up.
Let me actually… Open all. Yes.
Cool.
Support configuration, SDK, batch size, declarative configuration items or bytes.
Feel free to make a PR with prototype prefix so that it can be referenced, commented, etc.
Just remove and check for updates.
**Pablo Baeyens** 34:20 Yo.
**Severin** 34:29 add pretty print config options to OTLP file exporter… Yeah, this is, Looks like this still needs… more… Community Feedback bumping.
Period.
Gosh.
Define a clock interface… oh, I remember that one.
back.
sponsors.
**Pablo Baeyens** 35:15 Yep.
**Severin** 35:20 Isn't there… wouldn't that be, like, neat spots?
**Pablo Baeyens** 35:23 sponsor, yeah.
**Severin** 35:36 Like it now?
**Pablo Baeyens** 35:37 Yep.
**Severin** 35:39 Introduction of metric links.
Okay… Any… My orders on that.
I mean, I still think it's a… Cool idea to have links between metrics, but yeah.
I think that's just, like… Not really.
**Pablo Baeyens** 36:07 Yup.
**Severin** 36:07 Everybody's, like, from all the things that we probably need to be doing, this is, like, not the most important one, unfortunately. Oh, this one is closed.
That's cool. I think I just… it was just closed while we were talking about it? No, it was closed while.
**Pablo Baeyens** 36:24 No.
**Severin** 36:25 Oh, it still has.
**Pablo Baeyens** 36:25 That's weird.
**Severin** 36:26 Follow-up label, that's, cool.
**Pablo Baeyens** 36:27 Oh, okay.
**Severin** 36:29 Okay, okay, okay, let's remove that.
This is still… Removing follow-up again… Empty string attributes… oh, this is closed, so we can just remove, or we can… Should we put a rejected on it, or like a… it looks like it's rejected.
**Pablo Baeyens** 37:16 Yep.
**Severin** 37:19 What's the reason?
Language specifics are out of scope.
Cold.
Add guidance against using that.
And even if it's rejected, right, or they say, okay.
Remember that there were a few people not happy with it, but anyways.
host… Accepted, whatever.
Ready?
Just to have it.
triaged correctly… Change schema version for mine.
I support this idea… Clarify the timestamp in our metric collection systems.
Starting… Oh, yeah.
can ask.
I need info…
**Pablo Baeyens** 39:18 Yo.
Unravel the follow-up.
**Severin** 39:38 Schema transformation process should be able to perform original attributes… Huh? What did I do? Did I forget to… Oh yeah, I forgot to remove… 50… Follow-up thingy.
I think… Okay.
Now it should be gone. Cool!
I think I would appreciate it if we just leave it like that. I mean, of course, we could also spend some time on the community repo, but…
**Pablo Baeyens** 41:18 I think it's fine for today, yeah.
**Severin** 41:20 I…
**Pablo Baeyens** 41:21 It's been plenty already.
**Severin** 41:23 Yeah, I think that that was a… was a good run.
**Pablo Baeyens** 41:28 Yep.
**Severin** 41:30 Cool. Daniel, let's continue on that next week.
**Pablo Baeyens** 41:36 Yep.
**Severin** 41:38 And thank you once again.
See you on Wednesday, I guess.
**Pablo Baeyens** 41:43 Yep, see you.
**Severin** 41:43 Right.
**Pablo Baeyens** 41:44 Bye.
