SIG: Browser SIG
Date: 2026-07-30
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Chris Chestnut** 00:19 Hey, how's it going?
**Jared Freeze** 00:20 Hey, what's up, Chris?
**Chris Chestnut** 00:23 How's it going, Jared?
**Jared Freeze** 00:25 Good, good.
**Chris Chestnut** 00:28 Meet you in virtual life. I think we may have met in Slack already.
**Jared Freeze** 00:32 Yeah, I think so. Did you put something up already? Was that you?
**Chris Chestnut** 00:37 No, no, it was one of my coworkers, Cy, but
**Jared Freeze** 00:39 Okay.
**Chris Chestnut** 00:40 Yeah, I just put up a question, like, semantic convention stuff.
**Jared Freeze** 00:44 Cool.
Yeah, we're really trying to focus on that.
You know, coming up, like… very, very near future. Semantic Conventions is gonna be very important as we align all this stuff.
I was actually looking at… where, you know, where I work, we use a hotel, like, top to bottom, and so our URLs are actually sitting on the old version, and so we gotta do that as well, where, you know, we settled on some new keys and things, so…
**Chris Chestnut** 01:15 Yeah, I'm, like, pretty new to OTEL, in general, so it's, like, that's a lot of learning, and as it's updating, too, it's pretty… it's pretty cool, like, you know, just to see how many people are involved and focused on trying to figure out what's the right thing to do, especially for client-side stuff.
**Jared Freeze** 01:31 Yeah, definitely.
**Martin Kuba** 01:51 Alright.
Hey everyone, as usual, put your topics on the agenda.
**Jared Freeze** 02:07 Whoops.
Welcome back, David.
**Martin Kuba** 02:32 All right, we're 3 minutes over, let's… we can get started. David, you have the first…
**David Luna Bistuer** 02:39 Yeah, this is, I think there is something missing, but there's this, on the Fetch PR, I created long ago. There was a comment from Maxim, actually, a good point that, maybe depending on On the configuration, maybe the… depending on the… on the users, they decide to add some instrumentation and others not.
contacts registered, we might have, my halt.
Many… allocate many, objects, but not free them.
So the idea… Let me check if I see it with the… I've already appeared for that.
The idea is to, have kind of a limit for the contact registry.
So we aren't on looking more than… A specific number of items, maybe configurable, maybe not.
I think my PR could… I don't have it yet, but the idea would be… would be that, so… I would maybe explain a use case. So, fetch, let's pretend that we, we are adding fetch implementation, but not, resource timings.
It means that Fetching simulations will use a context latency to register different contexts.
For later use.
But since there is no one consuming and registering this context.
The recipe will keep growing and growing and growing and growing and growing.
So eventually, having a memory leak.
Here.
The idea that Quentin proposed was to have a limit, a limit on the items on the registry.
I remember that myself did kind of a first approach of having kind of a TTL, time to live, for… for resources, so yeah, for… items I added to the registry, but it was kind of, complex and a bit convoluted.
Maybe that approach is better.
So, I'm just raising here, here the idea.
If you have any thoughts or something you can chime in on in this conversation?
maybe add it here in the… in… in the SIG document?
Or you have something, some opinion right now, just share it.
And I'll be happy to, do any implementation, taking that in consideration.
**Martin Kuba** 05:00 David, I'm curious, how is this, how is this different from how it was implemented in the original… fetch or XHR instrumentations.
**David Luna Bistuer** 05:10 The original fetch actually is using… so, it's using Performance Observer to actually Query their own, resource timings.
So it's kind of, self-contained.
So, here we are using the registry, and there are, two with different instrumentations and interaction. SIG is… Stash in the context, and then Boosters Timings is Pulling out and using that to correlate the lock with the span.
In fact, and XHR disermentations in the co-repository.
They have their own performance observer, they query the entries from the performance observers, and they are… they were… Instead of using logs, they were using span events.
So they were creating the span, and they were… they were sending using span events on the same span. They were keeping the span open the whole time.
Until we get, they get, take out the, the, the resource timings, and then finally the end that span much later than the request finished.
**Martin Kuba** 06:16 Okay, so I think the, the danger is… So, like, right now, like, if a resource is observed, then it gets… it gets, like, it looks into the registry, gets… gets kind of… Decorated with the trace attributes.
And then it unregisters, like, the… The resource instrument… the resource timing instrumentation would then unregister the original.
**David Luna Bistuer** 06:43 Exactly.
**Martin Kuba** 06:44 context, okay.
But, like, if that… if that… thing that never fired, like, if you never got that event, then… There's a danger of not saying…
**David Luna Bistuer** 06:52 So, one of the things that the former instrumentation did was kind of a cleanup, I think that they cut the… the observer open the whole time, and then they were cleaning up the entries after a period of time. So that was kind of the first approach that I used, so I gave a TTL about around A few millil… hundreds of milliseconds.
Which was the approach that the former strategic was doing, but as I said, I think Jared came with a comment that was kind of difficult to keep track of timeout IDs and having timers for the time just for each request.
So, that solution is simple. So, fetch, fetch is just only adding the context in the registry, and then the consumer, which is resource timing, is they keep consuming the context and then unregistering it.
But there are situations that… This may not happen.
Maybe because instrumentation was not there.
Or maybe because of the configuration, because they are ignoring some certain URLs.
**Martin Kuba** 08:09 Okay, yeah.
That makes sense to limit the cache.
**David Luna Bistuer** 08:19 Okay, so I'll follow up with the PR, and send the link into the channel, the Slack channel, so you can have a look. But I prefer… I would prefer to have this in a separate PR instead of this one.
So once we… We merge that, then I'll… I'll sync with this… with this French.
**Martin Kuba** 08:39 Okay.
**David Luna Bistuer** 08:41 And hopefully that will be the lesson.
**Jared Freeze** 08:51 Yeah, just a… we actually are still getting… I think there were two PRs put up for Fetch in Contrib.
Like, just in the last week or two. So, I'm trying to keep an eye on this as well, and I'll… Feed those back to you after this gets merged, because there were some… I don't know, they're not all relevant, right, because we've redone so much, but… Be aware of that as well.
**David Luna Bistuer** 09:16 Okay, thank you.
**Martin Kuba** 09:24 Alright, is maxime here?
Doesn't look like it,
**Jared Freeze** 09:38 Yeah, he had posted… he had posted on Slack. I… yeah, I told him I'd check this on… on Monday, I haven't done it yet. But there was, yeah, merging, merge types for this, for the logs and Traces SDK into the config.
And what it might look like if you're only using one or the other.
It's pretty straightforward, really, it's just an opinion thing, so if you want to chime in here, the link, obviously, is… In the docs, so… Everyone go look.
**Martin Kuba** 10:14 Okay, cool, The next one is mine, so I opened a PR to add a doc for roadmap, kind of high-level roadmap.
If you haven't seen it… I would, ask that you please take a look, it's intended to be a living document, so we can continue making changes. I think I would like to merge it soon, so maybe, like, I'll give it another week, and… If there are no more, comments, then you can just merge this. But for anyone who hasn't seen this, just for awareness.
Any questions, or… If not, then we can move on.
**Jared Freeze** 11:06 Thanks for doing that, by the way. This is great.
**Martin Kuba** 11:14 Okay, let's move on. Chris?
**Chris Chestnut** 11:19 Oh yeah, so… So, yeah, I wanted to, to kind of bring this to the Browser SIG, because we started a thread in Slack about, trying to capture, visibility changes in a browser, whether it's foregrounded, backgrounded, yada yada. But I… and there were a lot of great thoughts in that thread, some of which went a little over my head. Maybe I should be reviewing that roadmap to get more familiar with what's going on.
But, yeah, I was like, I felt like while there were a lot of… good ideas posted. I didn't know if there was, like, next steps, for me to take, or if, if the community, the hotel Browser community was planning on taking some next steps. So, yeah, just thought I'd bring it here to see if, yeah, to see what's next.
**Jared Freeze** 12:15 So, this is… The device app lifestyle… life cycle.
**Chris Chestnut** 12:20 Yeah, yeah, but for Browser.
Like, should I propose something in the semantic inventions repo?
I don't think I have the time to create, like, an instrumentation library for something like this, but is that the next step?
**Martin Kuba** 12:44 I would say, like, maybe just creating an issue, like, where you describe what you're trying to accomplish, and, like, let other people, you know, comment, and… Async, so I think that probably would be the next logical step, Yeah, so it's not just in Slack, yeah.
**Chris Chestnut** 13:04 Cool. Can do. Thank you.
**Martin Kuba** 13:16 Okay, if there's nothing else on this one… Then, Carlos?
**Carlos Alberto Cortez** 13:22 Yeah, hello. I'm coming to, on behalf of the sea, just to try to, You may remember that there's a specification call where, you know, specification stuff is discussed and all that, and we have been trying to get different SIGs.
To present what's their current, you know, Progress, what's happening, what they are doing, and one of the problems is that the entire group of maintainers may not be aware, like Java or Python people, what's happening in other areas, like the collector.
OTLP arrow, etc. And so basically, we would like to get you guys go and present there or something. Eventually, it could be next week, in 2 weeks, in three weeks, something like that, you know? But basically, come and do a presentation. We are thinking about 10 minutes, 20 minutes. It can be a little bit longer if needed.
Also the idea is that, I was talking to Ted Young, by the way, who, you know, who's also involved in the, in the SIG, And there are some things that, sooner or later, this group will need from the specification. So we were thinking, what if at least a couple of people from this group could start attending the specification call. It's one more call to attend, but still, you know, it's very good, so people are in the loop, and whenever the time comes to actually touch something, like, for example, modify resources, or extend resources, or something like that, or even entities.
That happens, just, flawlessly, so to speak, you know? Instead of just trying to come and contact people here and there, and I don't know where to start.
So, yeah, do you have any opinion on this one? Would you like to present anytime soon?
**Martin Kuba** 15:04 So, Carlos, I was planning to do this, and I'm open to, like, do it with other… some… if any other maintainers or anyone else is here interested, like, to doing it together, I'm open to that, but I was planning to do that.
I couldn't attend this week, I had a conflict, but… But I did want to check, actually, I'm glad that you joined, because I wanted to check if, like, we need to schedule that ahead of time, or if it's just kind of impromptu, just put it on the agenda, and show up and put it on the agenda, or how does that work?
**Carlos Alberto Cortez** 15:33 Yeah, I would say that it's easier, for example, next week we only have one topic.
At this moment, so you still… you could go ahead and add it if you… if you are ready to make a presentation next week.
If not, the week after. And probably the best time to discuss that is during a specification call, so we can plan ahead, you know?
if, for example, let's say that you cannot make it next Tuesday, but if you attend, you can… we can briefly talk, like, about whether there's enough time the week after, or something like that, you know?
**Martin Kuba** 16:05 Okay.
And is there a specific format, like… That other, other, presenters have done in the past, or is it kind of… Just, like, where we are right now, and what our roadmap is.
**Carlos Alberto Cortez** 16:18 Yeah, I would say that showing the roadmap, what you have been doing, what you have.
And also, what things you plan to work on, yeah. That's basically what you have done, what you're working on, what you will be doing in the future.
That's it, yeah.
**Martin Kuba** 16:36 Okay.
Yeah, I've seen that, like, other specification SIGs have done this before. I was wondering, like, if other… if actually there have been, like, any language You know, or SDK SIGs.
**Carlos Alberto Cortez** 16:49 Okay, so that's probably a separate conversation, but long story short, even though some of those things, like Java or Python, are mature enough.
People think it would be nice to… so they could tell us what they have been doing, things that are not obvious, you know? Maybe they are working on extending something, or instrumentation problems, that kind of stuff.
So that could be also very useful to have eventually.
Likewise, as I said before, it would be nice to get people from this group attending the specification call, and when you cannot attend, it's still nice to check the notes, see what's happening, stay in the loop.
And I don't know, actually, whether you have a list of, Actual things, let's say top 5 or top 10 things, that you think will be big enough And important enough, specification-wise.
Do you have such a list, maybe?
**Martin Kuba** 17:51 We certainly have some… some areas, like, where we, that are… different from… from other, like, the backend, like, backend SDKs. We have been talking with Ted about this.
And Ted's, kind of take has been that, it's okay for us to diverge from the specification, and I guess, for me, it's not clear, like, if we need to… if it's okay if we just diverge, or if you need to, like, bring it back and, like, document it in the specification.
The decisions that we make,
**Carlos Alberto Cortez** 18:27 Yeah, okay. Yeah, it would be nice to get an idea. So, you know, as I am a this escalating representative, I don't attend most of the calls, but I'm trying to follow the notes.
So it would be nice for me to get a summary of things that you think will be, as before, important. I know that you have a lot of stuff, but let's say the top 3, top 5, so I can go and read.
And, when the time comes, I can provide some feedback, you know, or bring that specification, talk, you know, just get some kind of pre-brainstorming.
**Martin Kuba** 18:59 Okay, yeah, we can do that.
**Carlos Alberto Cortez** 19:02 Okay, so let's think offline, or, or next week, something like that. It's up to you.
**Martin Kuba** 19:07 Nope.
**Carlos Alberto Cortez** 19:08 That's on my side, yeah.
**Martin Kuba** 19:18 And like I said, I can take the lead on this, but if anyone else would like to help out with this, I'm… Would be also appreciated.
**Jared Freeze** 19:28 I'm out next week. We have a company off-site, so not next week, but, the week after, I'll be back normal to, normal.
Okay. Time. So, yeah, I can help out with that, Martin.
Maybe work on it tomorrow.
So, we can see.
**Martin Kuba** 19:46 You can do that. Sounds good. Thanks.
Alright, I think the last topic we have from Rebecca.
**Rebecca He** 19:58 Yeah, hello, I'm from Google slash Firebase.
And… I guess one question I had was, like, is there… do we see the need for, like, an onboarding kind of guide? I've read through the SIG notes, read through various READMEs in different places, but I think as, like, a new person to the community, it feels a little bit intimidating to start. We had another engineer on our team, Sy, who put up… contributed a PR, where it was, like, a very Simple, kind of, copy-paste of the… apply custom log attributes, callback. And that kind of thing is, like, pretty chill to do, but sometimes, like, last meeting, someone asked, like, do you want to migrate this thing to this repo? And I was like, well, that doesn't sound that hard, but… I also don't know the processes and, like, things, and so I was like, that's kind of intimidating to start… start pulling, so… I'm not really sure what the right solution is, but I just kind of wanted to raise that as a… as a thing, and I would love to be more involved, but kind of how can we reduce that, like, barrier to entry a little bit?
**Cleo Schneider** 21:06 I mean, I think… I… I think an onboarding doc would be very valuable, and Rebecca, I think we should write it. We're the newest ones here. Like, I think… we… we should write what we discover, and then… and then have folks contribute back to that.
**Rebecca He** 21:24 Yeah, but I do want to get a pulse on, like, if it's valuable, because if we feel like the information is already out there, then I don't want to, like, duplicate everything.
**Martin Kuba** 21:34 Well, I mean, this is a good feedback. I mean, if it's difficult for you to get up to speed, then that's a good feedback.
100%.
And we definitely need more documentation. Like, there's… we have lots of documentation gaps right now.
**Jared Freeze** 21:49 Yeah, for sure. I mean, everything we have is implementation.
So, as you have found. So, that is the answer. Yes, definitely.
**Rebecca He** 22:00 And it's tough, because documentation gets stale, like, super quickly, as we all know, and if things are constantly changing, that… is more stuff to manage, but yeah, maybe Cleo will take a stab and then share it with this group.
**Cleo Schneider** 22:13 I'm also curious if we have any AI workflows that we run on this repo that, would do that for us, you know? Just sort of look at the incoming PRs and try to keep our documentation up to date for us. I know that's something a lot of folks are doing these days.
**Martin Kuba** 22:31 We're on, we're on a map, yeah.
**Jared Freeze** 22:33 Yeah, I can say we don't have anything like that.
**Cleo Schneider** 22:36 Tough when you don't have a company that's gonna foot the bill for it, you know?
**Jared Freeze** 22:43 I think, yeah, I mean, Trent may be able to chime in on that, but I think we have certain credits, like, because it's open source, but I… yeah, it's for, like.
little pieces here and there. So, not sure exactly what that relationship is, but…
**Cleo Schneider** 23:00 Sweet.
**Martin Kuba** 23:02 Cool, yeah, I appreciate this, Rebecca. Thanks for bringing it up.
Okay, anything else before we… On the call?
**maxime quentin** 23:14 Yeah,
**Jared Freeze** 23:15 I was just gonna mention… oh, go ahead.
**maxime quentin** 23:17 No, no, I was just saying that I'm sorry, I've been late. My topic is not super urgent, so I can bring it for later on the program.
**Martin Kuba** 23:28 So we talked about it, though, briefly, And I think it was pretty straightforward, just asking for some more feedback on this one, maxime.
**maxime quentin** 23:40 Cool.
**Martin Kuba** 23:42 Did you wanna… did you wanna add anything, too?
**maxime quentin** 23:44 No, no, I mean, it was more like, bringing the description to the SIG, so I don't think… Directions that are not super… It's, like, meaningful.
**David Luna Bistuer** 23:52 Maybe… Maybe I'll have one question regarding that PR.
The PR does verification of the URLs, and if one of them fails.
Completely, so completions of the SDK. Returns in our SDK.
do we want, maybe… so if we have, maybe, let's say that we have logs endpoint working, or a valid URL, and Freeze is not.
Do we still want to send logs, or that's fine, just, you know, shut down everything and say, okay, we're not sending anything, because there was just one thing that was wrong in that signal, but not in the other, but sorry.
make everything okay. If not, you're not getting anything.
**Jared Freeze** 24:37 I mean, I would… I would say no, because you're gonna have more than one endpoint, right?
So… I mean, it's still an array, so, like, one could be down, but another one could be up, so I think you kind of do a best effort.
Right. That's… yeah, that's my take.
**maxime quentin** 24:56 Yeah, I agree.
**David Luna Bistuer** 24:57 It's just…
**maxime quentin** 24:58 I'll… I'll do the change.
**David Luna Bistuer** 25:01 Okay.
**Trent Mick** 25:02 I haven't read this thing, is this a liveness check, or is this a, you configured it with something that can't possibly be a URL?
**David Luna Bistuer** 25:11 That's exactly the leader, not the former. It's… it's a bad URL, so you're sending something that is not… it's… it's a string that it's not… cannot be parsed.
**Trent Mick** 25:19 Of the config is screwed up? Okay. Yeah. Alright.
For what it's worth, on the node side and the declarative config setup stuff, if there's any kind of validity breakage in the configuration, I just abort and it's a no-op.
SDK.
**David Luna Bistuer** 25:36 Complete, completely.
**Trent Mick** 25:37 Yeah, if you made a configuration error, you screwed up, you're not getting an SDK.
If this was a wideness check, that's a totally different thing.
totally different story, like, if an endpoint's down, then fine, it'll come up later, so you should keep trying, but… yeah. For comparison. I don't think it's a big deal either way, but that's the approach I'm taking.
And declarative config.
**David Luna Bistuer** 26:00 Thank you.
You know, we have other languages are doing the same.
**Trent Mick** 26:05 The recommendation declarative config is to fail fast on the… So you… you parse the… it's kind of broken into two steps of parsing, that the config is valid according to the schema, and then the next one is creating the SDK components, and the recommendation there is fail fast, too. So if you're… if you can't satisfy the config that was given, then you get a no-op SDK, and… login error, I guess, basically, so… In the create step, I just have it… it'll throw an error, and there's a try-catch at the top of creating the whole SDK, all the SDK objects.
Huh.
**Jared Freeze** 26:44 So is it conservative? So one… like you said, one backed config takes it down, right? So…
**Trent Mick** 26:51 Yeah, yeah, either… either the config doesn't meet the schema, or the schema is describing things that, like, the SDK doesn't implement yet, or… Doesn't support… I suppose there's some nuance in there. So, like, one of the nuances is… declarative config and implementation of is meant to support all 1.x of the schema, so new features can be added, so we don't blow up on a feature that we In the config that we haven't seen yet, we just log a warning for that, but, if it's… Yeah, so, like, for example, if someone asks for a… type of span processor that we don't know about, then we blow up on that one, because it's like, you either fat-fingered that config.
And it should blow up, so you should be made aware of it, or… Or you're trying to use some custom, Spam processor or whatever that, like, we don't know how to load, because… There's no support for extensions like there's in the JavaS SDK or something like that.
I'm not sure if that exactly applies in this case, because I read this PR, and I haven't been keeping up well enough in the browser.
**Jared Freeze** 28:15 Cool. Well, definitely check it out again, Maxine.
**maxime quentin** 28:19 Yep. I'll check. I mean, if you have a typo in your URL or something like that, I feel it's still quite tricky to just drop all the traffic on logs or stuff like that, if you add a typo in the tracer URL. So… I might… I'll look at it and have a proposal.
**Martin Kuba** 28:48 Yeah, sounds good. We're at time, so… Thanks, everyone.
**Jared Freeze** 28:53 Good, yeah.
**David Luna Bistuer** 28:55 with it, right?
