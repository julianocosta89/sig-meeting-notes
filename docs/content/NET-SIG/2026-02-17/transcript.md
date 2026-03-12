SIG: .NET SIG
Date: 2026-02-17
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Rajkumar Rangaraj** 01:34 Hello, Matthew. Hello, Jack.
**Zach Montoya** 01:39 Blue.
**Matthew Hensley / Grafana Labs** 01:40 Millard.
**Rajkumar Rangaraj** 02:07 Let's wait for a few more minutes to see if anyone else joins. If not, we can just… Take a look at the… Agent does.
**Alan West** 02:42 Hello, all…
**Julius Koval** 02:45 Hey.
**Rajkumar Rangaraj** 03:01 Okay, let me go ahead and, stunt.
Welcome to Charlie.
Can someone acknowledge if you're able to see my screen?
**Alan West** 03:27 Yep.
**Rajkumar Rangaraj** 03:29 I don't see any agenda for the day. Does anyone have any topic for discussion for today?
**Julius Koval** 03:39 Yeah, hi. So… A few weeks ago, I came here to ask about the Lux Bridge API, and I think Raj asked me to ask Alan.
about it, and I… So, Alan, I pinged you on the… on the issue related to the rich API, I don't know if you saw it.
**Alan West** 04:02 No, sorry, I'm afraid I didn't.
**Julius Koval** 04:04 Oh, okay. Well, basically, I guess… Do you have any thoughts on what the future of the API might be, and if and when it might get stabilized?
**Rajkumar Rangaraj** 04:15 Yeah, let me ask that question to Alan, because I… Alan, I know, like, Blanche had worked earlier and added an experimental logs bridge API, to the repo.
Just want to check if you have any background about that work. If you need to do the, remove the experimental feature from the LuxBridge API, is it just making the, like, all the internal as public and making it available, or do you think it's much more involved? Just want to take your thoughts if you know anything about that.
**Alan West** 04:50 Well, it's been a long time, so, my memory is a bit fuzzy, but yes, when… when Blanche was… working through all that, I was… Collaborated with him, and… We were bouncing ideas off of each other, so… What I recall is that, as you said, some of the stuff is… out there, and their internal APIs.
And so that's part of the work, but what I don't recall is if there's still stuff that didn't land, because he had a… he had a long… he had a big branch that did a bunch of work, and I want to say, like.
There were elements of it that… never did land, but I'd have to go in and kind of, like, you know, review the state of that to really Be able to answer your question.
Super clearly.
**Rajkumar Rangaraj** 05:45 Okay, the question has arised, like, like, this is a topic that has been coming for a very, very long time, and we… we thought, like, it's the right… because we don't have any other big feature that we are working upon now.
And we felt it's a good time to get this onto the list. So, if you also agree, I think, Julius said earlier he has bandwidth to help us out. Julius, is that correct?
**Julius Koval** 06:14 Yeah, sure, if there's something I could help with, then I would.
**Rajkumar Rangaraj** 06:18 Yeah. So, if people are interested, is it fine to Do you feel… think, Alan, the community will also benefit? Maybe your past experience, I want to take into consideration when you are doing things out, how many came and shown interest to have this as a part of the SDK?
**Alan West** 06:39 Yeah, I personally was always in favor of landing the work.
A couple of the components that definitely never landed, but that are out there, probably on a branch somewhere, that Blanche had worked on, were… Log appenders for… I want to say, I think, serial log, and also, event source.
And the idea was that those appenders that he had prototyped they're built on top of the LogBridge API, right? So they're, like, the LogBridge API is a prerequisite for.
for landing those… those appenders, so… I think that full, like, end-to-end story, would be of benefit to the community, right? Like, first.
getting the LogBridge API into a state that we can ship, and then… Shipping the appenders, that we've… Probably, like, in the instrumentation repository, or the contribib rep repository.
shipping the appenders that are then built on top of that API is kind of like that full… Completing the full story.
**Rajkumar Rangaraj** 08:00 Yeah, I have some context on that. Right now, from our SDK, these Lox Bridge APIs are available in the… not in the stable version, but in the beta version or the RC version that we release. And the experimental version of LogsBridge is available in that.
And, if I understand correctly, I blocked the PR's work earlier. He, he built up under… he took the code from the, branch, earlier branch, and he proposed a PR also, to create two appenders. One was Serilog, and another one, I don't recall correctly, what was the name of that. He tried creating a component based on this experimental API. So, I think, given he did that, everything worked as expected, and there were no challenges at all. So, the only thing is that we did not want it to give a false promise on those the contrary packages, that's why we hold on to that work, and wanted to get into it, when the logs API becomes… the Logs Bridge API becomes stable. So, the end-to-end have been evaluated, and it… Seems to help.
Right.
**Alan West** 09:20 I think all Peter did was… was to simply… basically leverage Blanche's original work to…
**Rajkumar Rangaraj** 09:27 Yes.
**Alan West** 09:27 Yeah.
**Rajkumar Rangaraj** 09:28 Yeah, I also say this, like, recommend the same thing.
Julius, like, if you are planning to start the work, I know Blanche is not involved too much in the .NET area right now. He's mostly in the… working on the different area, but he's still an approver in this report. Just try to reach him out to check where it is this, and how you can take it forward. But from a community standpoint, like, from a maintainer, you have the complete support if you're ready to work on this.
**Julius Koval** 10:00 I'm not gonna go about it?
**Alan West** 10:02 Just to say, like, what could help to kind of kick this off is… just to see if Blanche had some time. You know, it could be… it could be this meeting, or it could be, like, a one-off meeting that we schedule.
But just get all of us together in the room.
And, if Blanche had a, you know, an hour to spare to just kind of… hash out.
where things were at, I think that that would… would bring a lot of, structure, too.
**Rajkumar Rangaraj** 10:31 I can try and reach him out internally to see, but next week would be very difficult, because people have been asked to come to office for the first week next week, so maybe the week after that would be a good time to bring Blanche there for a discussion.
Sure. I mean, and I can ping him too, you know. He and I still talk from time to time.
does it make sense, like, two weeks from now, we can reconvene and create a plan on how to move forward, and so on.
March 3 in the sink. We can decide. We will have a concrete plan at the end of the meeting, because Blanche knows most of the things as he Implemented already a lot of things in there.
**Julius Koval** 11:17 Yeah, okay, I'll… I'll join in 2 weeks.
**Rajkumar Rangaraj** 11:20 Yep.
**Alan West** 11:22 I think… I think some part of that, and this is where I could really use Blanche's help to kind of, like, re-refresh our memories of… of where things were at, because there were things that were not yet solved, as far as the bridge API was concerned, like, for example.
How to deal with, like… object values in logs, or, like, map values, I guess is what the, with the spec.
calls them I don't think we'd landed on a solid solution for that. So, in any case, like, there were still some things that he had not even worked through yet, and were open questions, so… identifying those, I think is something that he could help out with a lot.
**Rajkumar Rangaraj** 12:27 Cool, then. I think, we both can reach out to Blanche and see, his availability for March 3rd.
And… If we can get to the SIG, it would be helpful for us.
Okay. Are there any other topic apart from this one?
**Alan West** 12:46 Not for my end.
**Rajkumar Rangaraj** 12:48 make new notes.
Okay.
Let me move on to the other one, like, Last week, there was a discussion, there are some smaller bugs we identified, and we fixed that, and this is also one of them. Like, Martin was saying, like, once all this… was proposing last week, if we merge all this, we can do a, like, a patched version.
So, we're inclined about that, only releasing the SDK part of that.
So probably by, we should get all this merged by the end of this week and plan for the patched version of the release, because we don't have any major changes, in it, apart from these, smaller fixes.
**Alan West** 13:44 Sounds good.
**Rajkumar Rangaraj** 13:49 I don't think there are any other big… things that's pending here, apart from the last one, because it needs a very dedicated time to look into it and take it forward. But apart from that, we are in a good state over here. No major things.
The top ones are all the tests or the, infra steps.
So… And no new issues also, like, if there was issues, I think Martin already responded to them, and we cleared those off.
So, health-wise, it looks… Good, no.
That's all I have it now. Like, there are no other topics, I think we can end early.
**Alan West** 14:43 Sounds good.
**Rajkumar Rangaraj** 14:44 Thanks, everybody.
**Alan West** 14:45 Thanks, Raj.
Thanks, Al.
**Julius Koval** 14:47 Bye.
