SIG: Kotlin SIG
Date: 2026-03-30
Duration: 18 minutes
============================================================

## Zoom Recording Transcript

**Hanson** 00:13 Back from Amsterdam!
**Jason Plumb** 00:16 Hot off the presses.
**Hanson** 00:20 Is this the first day?
**Jason Plumb** 00:21 First day back at work, yeah.
**Hanson** 00:25 Are you, off of the jet lag? Did you get back, like, yesterday, or did you get back, like, on, like, Friday or something like that?
**Jason Plumb** 00:30 I got back yesterday.
**Hanson** 00:31 Oh!
So, this is, this is the… did you get up at regular time today?
**Jason Plumb** 00:39 I did, I think I woke up in the middle of the night one time, and I was, like, kind of awake, and I was like, I'm forcing myself to go back to sleep, and… it was, like, 3.30 or 4, and I was like, I'm going back to sleep, so I made it work.
Ask me again at, like, 4PM how I'm doing.
**Hanson** 00:55 You might be okay at 4pm.
**Jason Plumb** 00:57 God.
**Hanson** 00:58 It's only 12. But 6? 7?
**Jason Plumb** 01:02 Yeah.
**Hanson** 01:03 exponentially difficult. Hey, Jamie.
**Jason Plumb** 01:07 Ayy.
**Hanson** 01:08 Are we in… we're in British summertime now, right?
**Jamie Lynch** 01:12 Yep, it's officially summer.
**Hanson** 01:14 All right.
So, Jason, you were there a few days before, right? So you took in the city and stuff?
**Jason Plumb** 01:27 I went on a little 3-day bike tour of the Netherlands.
I did 210 kilometers on a really heavy bicycle.
And got down to Rotterdam, went out to the Hook, went up the coast, saw the Hague.
It was really nice. The weather was great for it.
**Hanson** 01:46 It's only 200 kilometers?
**Jason Plumb** 01:49 Yeah, so Amsterdam down to Rotterdam, and then out to the hook, and then up the coast. Well.
Sorry, over to The Hague, then the Hook, and then up the coast to Amsterdam, 210, yeah.
**Hanson** 02:00 I guess everything's really close?
**Jason Plumb** 02:02 Yeah, and I mean, I didn't cover the whole country, you know.
**Hanson** 02:05 Sure.
**Jason Plumb** 02:06 some of the big cities, I didn't get Utre.
**Hanson** 02:09 Well, you wouldn't even make it all the way to Seattle with 200 kilometers.
Maybe.
**Jason Plumb** 02:17 Portland to Seattle is about 200 miles.
**Hanson** 02:19 Oh, okay, well, I guess not the two-thirds.
**Jason Plumb** 02:22 Yeah.
Anyway… Yeah, I've been completely ignoring it. I'm so far behind on everything right now, but…
**Hanson** 02:32 Me too.
**Jason Plumb** 02:34 Yeah, I have a good… I have a solid week and a half before I go on a vacation.
**Jamie Lynch** 02:44 Cool. I'll just leave it open for a couple of minutes if anyone… Wants to add in items, and… Yeah, then I guess we can start talking about it.
**Hanson** 02:56 I haven't… yeah, I… I haven't added anything. I… I think I sent in that, the, span exporter PR. You might have even merged it, like, before you left on vacation, but that's the last time I looked at it.
**Jamie Lynch** 03:14 Yeah, I think last time.
Yeah, I don't have a massive amount to discuss either this week, I've been on holiday too, so it might be a short one.
Cool.
Yeah.
**Jason Plumb** 03:29 I really just need… I need… I just need to catch up on PRs and everything else, and it's… Yeah.
Very far behind.
**Jamie Lynch** 03:41 Yeah, so first item, I just thought we could maybe chat about when we close milestones, because I've noticed that… the logging API… Kind of has… All the issues that were associated with it are done.
I think there's probably more features in the OpenTelemetry spec that are in development, or not marked as stable yet.
So… Yeah, I was curious to hear people's thoughts on… When we should consider, like, a milestone like this done.
Whatever.
What are the criteria for that, really, and do we want to close it, or just leave it open?
**Jason Plumb** 04:25 I have an opinion on this. I think that as soon as all of the… all of the items, all the issues in a milestone have been closed out, then the milestone should be closed, but I think there's one that's currently missing in this one, and that is to mark the logging API in Kotlin as stable.
And so, if we add that one, that's kind of like the gating issue that would then prevent the milestone from being closed.
If that makes sense.
**Jamie Lynch** 04:50 Yeah, fair.
**Jason Plumb** 04:53 And that can just be, like, a placeholder issue that says, You know, market stable.
**Hanson** 04:59 Yeah, I would generally agree with that, especially if we could take a look at the… like, once everything is closed, we say, hey, do we have to add anything? And if the answer is no, then we should close it. It doesn't have to necessarily be, we've 100% finished everything listed in the spec. It's almost like, is this good enough to be something that is useful independently, and doesn't have any major contradictions with the compatibilities that we've listed out?
In terms of declaring something stable, I don't know… Do we have the power to do it?
**Jason Plumb** 05:32 Yeah, we do.
**Hanson** 05:33 then… then I think, then I think we should take a look at that and declare that stable, if… if we think it's… it's good enough.
**Jason Plumb** 05:40 Yeah, we just have to do our diligence, you know, like, Carlos was, going over the tracing API with a fine-tooth comb. I think we'd want to do something similar for the logging API, and… Is there, in the… in the… I think that in the… In the spec repo, there's that compatibility matrix. Does it have all the detailed logging API stuff in there? And do we have an entry that we can… do we have an entry in there yet?
**Jamie Lynch** 06:05 Yes, we do. So we can cross-reference against that.
**Jason Plumb** 06:12 Cool.
**Jamie Lynch** 06:13 So yeah, that's potentially an issue, but we could… Add, to close out the milestone.
**Jason Plumb** 06:20 Cool.
Yeah, I mean, I think if we've got all green checks down that list of APIs, and we've looked at it, and maybe spent an hour going over it and just making sure there's no glaring gaps.
Seems like we could mark it stable. We have that authority, I mean… now, if we missed something glaring, it's gonna come back and bite us, and we're gonna have to do a major revision, but like, you know… That happens, it's part of software development.
**Hanson** 06:47 All we can do is be… do our due diligence, it's never going to be 100%.
**Jason Plumb** 06:51 Exactly.
**Hanson** 06:52 The major version is also not a huge deal at this point, so…
**Jason Plumb** 06:55 and also just get, like, getting… I feel like this is a… a… like, a broad problem across a lot of open tele is, like, being too cautious. I feel like it's a little… I mean, there's a lot of people looking at this stuff, and it… I mean, everyone's using this stuff now, and so, yes, it's important, but for a new language, for a new offering, I think it's okay to go a little faster.
And then slow down once you… once you've approached… once you've hit stability, then, like, start easing the brakes or whatever, but, like, right now, we shouldn't be touching the brakes at all.
**Hanson** 07:26 I… I think my bias is always slow, so I would be the… I would be the, let's… let's slow down. So when I say, hey, let's just do it, I'm not saying it's always this way, but… It would be like… Yeah.
**Jason Plumb** 07:43 It might be weird, too, to have… I don't know that this matters, but, like, I'm pretty sure all of the other languages that were kind of grandfathered in or started earlier stabilized tracing before they stabilized metrics, before they stabilized logging. And that's just kind of… that was the evolution of those signals, but coming in kind of… clean room, fresh start… well, not clean room, but, like, coming in, you know, fresh start. I guess the order probably doesn't matter. It might seem weird to people to have logging stable before tracing, but…
**Hanson** 08:12 Logging is so simple, like, compared to… Like, frankly, like, the events API, like, are we declaring that stable? Like, I don't even know if events has a separate block.
**Jason Plumb** 08:28 Business does not have its own API.
**Hanson** 08:31 No?
**Jason Plumb** 08:32 gotten this back. No?
**Hanson** 08:33 Not in the spec, but it is called the event… the Events API is referenced as a thing.
**Jason Plumb** 08:38 Where? Show me.
**Hanson** 08:40 Oh…
**Jason Plumb** 08:42 It's all…
**Hanson** 08:43 No, no, you're right, not in the spec, but… I, I believe folks have referenced the Events API, which is basically the logging API with init, and also setting the, the, the, the, the…
**Jason Plumb** 08:57 ending at all. That's it.
**Hanson** 08:58 Yeah.
**Jason Plumb** 08:59 Yeah, that's the only… that's the only API related to events.
**Hanson** 09:03 Yep.
**Jason Plumb** 09:04 And it's a sub… it's a… it's part of or a subset of the logging API. And we… there's been years, like, literally years of discussion on that topic, on whether or not events should be a separate API.
And… I didn't fight that battle very hard, but Watson fought it pretty hard and lost.
And by lost, I mean whatever, he, like, conceded. He finally conceded and was like, fine, doesn't matter.
**Jamie Lynch** 09:33 Cool.
**Jason Plumb** 09:34 Carlos, DeFrancisco.
**Carlos Alberto Cortez** 09:36 Hey, hey! Sorry for being late.
I am, yeah, reading the notes now, Yeah, it's interesting to know that, if I understand correctly, logging Teams that will be ready to go before tracing.
So, I would say that, even if we want to declare the API stable, I think we should probably ask somebody from the TC to do that, you know? Besides me, to do a full review on that one.
Just in case.
**Jason Plumb** 10:11 Oh, the logging API?
**Carlos Alberto Cortez** 10:13 Yeah. I would argue that's less important, it's less user-facing.
Yeah.
**Jason Plumb** 10:21 We can see if Jack has, cycles for it, right?
He knows that API very well, and he's on the TC.
**Carlos Alberto Cortez** 10:29 Correct, yes. Yeah.
I can do one round myself first.
To double, triple check, just for the sake of sanity, let's say. And then, if I am, like, if I, yeah, like, once that is on, we can ask to see. I will mention that to Jack, so he gets… some cycles ready in the following weeks, hopefully. I don't know how busy he is, but yeah, hopefully he has time for that.
**Jamie Lynch** 11:00 Cool. That'd be super helpful.
**Carlos Alberto Cortez** 11:03 Nice.
**Jamie Lynch** 11:04 I think, another… thing, but we've not discussed yet is… We also have the option of just, like, waiting, like, a little bit of time after we've done all these tasks before declaring it stable, so we could know that it's stable ourselves, but… Maybe leave a month or so.
**Jason Plumb** 11:24 Yep, I think that's totally fine.
**Hanson** 11:26 we can then maybe create a new milestone that's, like, stability, and just put the various API stability in that, and then basically close off the logging milestone.
As, like, DevComplete or something like that.
If we were to do that.
**Jamie Lynch** 11:47 Cool.
I will try and co-action some of these things.
Yeah, I guess next topic, is really just an update. I'm continuing on with the API spec compliance milestones, I think.
Fair, pretty much… all either done or have a PR open for them.
And… the Tracing API was up next. Which… Has a few more things.
**Hanson** 12:25 Oh, sounds right.
**Jamie Lynch** 12:28 And if anyone else has topics, please feel free to add them, because for the last… One on the agenda so far was whether we should release or not.
So, we released on March 11th. Do you want to release this week, or wait till next week?
**Jason Plumb** 12:47 I'm sorry, what did we say our cadence would be again? I think we were trying to go every, like, more than once a month?
Is that right?
**Hanson** 12:55 I think we said standard once a month, but if there's reasons, we will release more frequently. I guess the question is, is there something that's compelling, for us to release, since the last time? Is it individually useful, or, you know.
**Jamie Lynch** 13:16 I'm not aware of anything that's super pressing, I thought I'd just put it out there in case folks wanted to… Ship this week.
**Hanson** 13:26 I think next week is fine, unless… It's super compelling.
I thought for the sake of completeness, if we're done with the previous topic, Jamie co-wrote a blog post, in the OpenTelemetry website, announcing the column SDK and call-up contributions. I don't know if this made any, headway, at KubeCon. I think it was done just before then. So, Yeah, this is official official.
Not that it's not official before, but now it's, like, blog post official.
**Jason Plumb** 14:13 Yeah, this is great, this is awesome.
I am probably the only one on this call that was at KubeCon, so I… I didn't hear a single person mention Kotlin at all, but also, we didn't have a dedicated observatory space like we had in prior years.
**Hanson** 14:28 Whoa!
**Jason Plumb** 14:28 We had… we had the, the Project Pavilion, like, little stand, and then there was, like, some SIG meetings that spilled over into some tables that were nearby, but it was way… it was way less of a community space.
**Hanson** 14:42 Hmm…
**Jason Plumb** 14:43 I can maybe talk to you about that, Hanson, asynchronously, or not on this recorded call.
**Hanson** 14:49 Sounds good.
**Jason Plumb** 14:50 Yeah.
Yeah, this blog post is awesome.
**Hanson** 15:00 This is exactly the type of thing we need to… keep going. It's not necessarily people looking at it real time, but people searching for it, like, once they hear about it, this will add legitimacy and, you know, plans of action, and even when the, the, times for the SIG is, so…
**Jason Plumb** 15:18 Yeah.
So, following up on this, maybe I'll put a couple of notes in the document here, too. I don't have it handy, but there's a couple of other channels that we can leverage to get word out about this, especially as it's becoming more mature, as people start adopting it and getting stable. A couple of channels, like OpenTelemetry-based channels, for, like.
getting, like, a short discussion on the YouTube channel, or whatever, like, there's other marketing approaches that we can take to get the word out there.
So…
**Hanson** 15:50 once…
**Jason Plumb** 15:50 Cool.
**Hanson** 15:51 Once things are stable, then there's, like, another reason to, like, reach out and do that.
So it's like, hey, last one was that it exists, and the next is, oh, you know, we've declared the tracing and logging API stable, so it's just another excuse to kind of get the word out, and maybe we'll use different channels at that point.
**Jamie Lynch** 16:13 I'd definitely be interested in knowing more about it, what all the channels are, and… Yeah, just knowing that they're there, like, we can choose whether to do it now or later, I don't know where they are right now.
**Hanson** 16:28 Yeah, so Jason, if you have a list in your mind.
**Jason Plumb** 16:31 I will, yeah. Let me… I'll link to stuff. There was a cool discussion… at Observability Day from the, the… SIG, I'm not awake yet, and I'm still jet-lagged, but this… the SIG that handles, like, community engagement.
**Hanson** 16:49 End user's sake?
**Jason Plumb** 16:50 End users say yes.
There's good discussion from them and some of the efforts they're doing, so…
**Hanson** 16:58 Yeah, they didn't take my talk this year, so I think it's a cram in.
Android Kotlin client stuff.
**Jason Plumb** 17:08 Yeah, it was a weird year.
As far as, like, talks being accepted.
Yeah, I'll add those, it's gonna take me a second to find stuff.
And Jamie, I did see some messages from you about the security stuff, and I haven't looked at it yet at all. I'm sorry.
**Jamie Lynch** 17:39 Yeah, that's fine. Yeah, I think… Well, we can chat about that asynchronously on something where it isn't recorded, I guess.
**Jason Plumb** 17:52 Yep, that sounds fine.
**Jamie Lynch** 17:56 Cool. Any other topics?
**Hanson** 18:08 Fort WayM.
**Jamie Lynch** 18:09 Probably cool about.
**Jason Plumb** 18:11 Sounds good.
**Hanson** 18:12 Hey, friend.
Go ahead.
**Jason Plumb** 18:17 Alright, bye!
**Hanson** 18:18 Bye.
**Francisco Prieto** 18:19 Yeah.
