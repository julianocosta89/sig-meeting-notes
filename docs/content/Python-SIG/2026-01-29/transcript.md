SIG: Python SIG
Date: 2026-01-29
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Aaron Abbott** 06:58 Hey everyone, how's it going?
Alright, we can, give a few more minutes for people to join, but it doesn't look like Ricardo's here, so maybe I'll drive.
Does anybody have any agenda items? We don't have anything, for this week so far.
**Yazdankhah, Mani** 07:44 I think I still need a review for my PR.
I had a look, and he deferred to Ricardo, but I still haven't heard back.
**Aaron Abbott** 07:58 You mind just dropping the PR?
Sure.
**Yazdankhah, Mani** 08:02 I'll add it to the… yeah, yeah.
**Aaron Abbott** 08:07 Yeah, if y'all could also, But you're naming the attendees, if you like.
I was muted.
Alright, we can get started.
Manny, do you have the… a link to the PR, you want to share your screen.
**Yazdankhah, Mani** 09:22 Unfortunately, I can't throw myself… it's the last one from the last, meeting.
The very last PR.
Or alienate, I'm sorry.
I can copy-paste it as well. Sorry, I'm just filling out the form.
**Aaron Abbott** 09:42 So, did you say you wanted to share, or do you want me to…
**Yazdankhah, Mani** 09:44 No, no, no, you share, I can't share. It's… I'm just copying it from the last…
**Aaron Abbott** 09:52 This one?
**Yazdankhah, Mani** 09:55 Correct, correct.
**Aaron Abbott** 09:56 Okay, yes, I think I owe you a review. I think Ricardo was asking me to take a look. I can do that.
Anything you wanted to call out here?
**Yazdankhah, Mani** 10:06 Yeah, Lucas wasn't sure, so I broke it up into two commits. One of it was the changes he wanted me to make, and one of them is the potential of removing the… meter… metric readers attribute from SDK Config, something like that, yeah.
**Aaron Abbott** 10:25 Okay.
Cool. I will take a look at this. It looks nice and short, which is always great.
I saw there were some open questions, but yeah, thank you all for reviewing. It's always good to have.
Overview.
Anything else you wanted to call out here?
**Yazdankhah, Mani** 10:46 No, I think that's it.
**Aaron Abbott** 10:49 Okay.
**Yazdankhah, Mani** 10:50 Thank you very much.
**Aaron Abbott** 10:52 Yeah, you're welcome.
That's the end of the agenda.
I don't know if anybody else has anything.
Be a really short meeting.
**pabcolli** 11:07 Hey, just wanted to say hello, this is Pablo. I'm back from a 3-month leave of absence.
Apologize for, for, not saying anything about it. I actually got locked out of my, account.
Before my absence got approved.
But, I just wanted to mention that there is some… Interest… In my organization for, a JSON HTTP exporter.
I know there are… there have been a couple of attempts at that, like, multi-thousand line PRs.
I think maybe the way to attack that would be… To… do some refactoring in the OTLP exporters, and break… break that up into a bunch of small PRs. You know, I just wanted to sort of gauge, What the community thinks about that.
**Aaron Abbott** 12:14 Yeah, I mean, first of all, welcome back.
Good to see you.
**pabcolli** 12:18 Thanks.
**Aaron Abbott** 12:19 Yeah. I think this came up again in the last 3 months, There was, And also, I think it's important to kind of clarify the requirements, because I'm assuming the goal here is to avoid protobuf dependency, right?
**pabcolli** 12:34 Yes, that's one of them.
**Aaron Abbott** 12:36 Yeah.
So, my… my personal preference, like, I've… I've heard also asked for this, to reduce package size, and somebody offered, I think, like, a Rust implementation, if I remember right.
Somebody was offering to send it, but they just ended up putting it in their own repo.
But yeah, I think if it's possible to do it with generated code, either, like, running your own part of plugin or something like that.
That would kind of be my preference, because… from some of the implementations I've seen, it's a bit… manual, like, somebody will go through, and when new things get added to the protobuf, they'll update the JSON Encoding stuff to… to do what's expected, so… I don't know if that…
**pabcolli** 13:25 No.
**Aaron Abbott** 13:26 feasible to you?
**pabcolli** 13:28 Yeah, yeah, definitely.
I… in looking at this, it seems like there is a quite significant lift before I even get a chance to think about that stuff.
Because… Of just the way the exporters are protected with mix-ins, So I think, I think, if I were to take this on, it would be… it would be a big, multi-week, probably multi-month, refactoring… Effort. If, you know, maybe, like.
On the order of 10 PRs.
First.
Before I actually do any of this, JSON exporter stuff.
**Aaron Abbott** 14:18 Okay. And that's mostly just… Like, refactoring of the mix and stuff.
**pabcolli** 14:25 Yeah.
**Aaron Abbott** 14:28 Yeah, that sounds good to me.
I think making the code cleaner is always appreciated, if it's… if it's mostly stuff like that, and not… not enough new features for those first, first couple PRs.
I am curious, like, is that a blocker? Is there a reason we can't, do it without refactoring.
**pabcolli** 14:53 I think you can.
It's just… I think… We would be… Maybe digging ourselves… A little bit further into a… into this hole that we'll… Would be nice to dig ourselves out of.
Long term.
I mean?
And I think that's maybe one of the reasons why the… Several or multiple attempts at this effort have kind of not succeeded.
Come on.
**Aaron Abbott** 15:27 Gotcha.
Okay, well, I'm, I'm all up for cleaning it up, I'm not a big fan of the mix-ins myself, so… Probably looking for kind of an agreement from the SIG that you could go ahead with this, or…
**pabcolli** 15:43 I just wanted to, like, gauge, you know, first of all, what… what folks thought about this, and whether or not anybody else was already Undertaking this effort for him.
Considerably.
**Aaron Abbott** 15:58 Yeah, I can try to find the thread from a couple months ago, because I think… Unless… does anybody know, off the top of their heads where that one was?
I think Ricardo could probably point you to it, if he's not around.
**Dylan Russell** 16:24 There's a PR someone opened, like, 6 hours ago.
**pabcolli** 16:29 Really.
**Dylan Russell** 16:30 the… Yeah, and it was… they said it was, like, AI-generated.
By the way.
**pabcolli** 16:39 Okay, what, what, have you guys discussed AI-generated or AI-assisted PRs? Like, is there a policy around that?
**Aaron Abbott** 16:51 So there's, like, an hotel-wide policy around it. I can… I can try to dig it up. I think, like, AI assists, I don't know, maybe my two cents, totally fine. We've definitely gotten, like, spam.
you know, kind of garbage PRs that don't make any sense, or missing context. Like, obviously we don't really appreciate that, but… you know.
Vibe coding with some human intervention is great, but you should be the one reviewing the code, not us, right?
**pabcolli** 17:22 Yeah.
**Aaron Abbott** 17:23 Yep.
**pabcolli** 17:25 Okay, cool, I am… I'll probably… I'll look into, do initial PR. I intend to keep these PRs as small as possible.
Yeah.
So that's… that's it from Emkeep.
**Aaron Abbott** 17:44 Yep, of course. I think this is the PR, right, Dylan?
**Dylan Russell** 17:49 Yeah…
**Aaron Abbott** 17:52 Yeah, I mean, Paula, if you could take… yeah, I mean…
**pabcolli** 17:56 So, 5,000 lines, yeah.
Yep. I wonder if… if we should, or maybe this already exists, put in something in contributing guidelines? This probably already exists, about keeping PRs under some… reasonable limit.
Like, you know, 500 lines or something like that.
**Aaron Abbott** 18:21 Yeah, I don't… I don't think we've written anything down like that, but… Yep.
If you don't…
**pabcolli** 18:30 Yeah, I was gonna say, just because the previous attempts at this also produced multi-thousand line PRs, and I kind of feel bad for the people who did that, because… they… I think some of them were not 5-coded, they were actually Coded by hand. And, you know, these contributors did not We're not, you know, well-versed in the practices of working in a community.
And they did all this work, and then their PR didn't get reviewed, and then they just kind of, like, moved on.
**Aaron Abbott** 19:06 Yeah, that's a good point. Do you mind taking that, Pablo?
PR for updating that. I agree, like, they should definitely come to the SIG first, anything that's a really, really significant change.
**pabcolli** 19:20 Okay, great.
**Aaron Abbott** 19:22 Yeah, but I think I do have the PR open here, like I was gonna say. I think… Even if this is vibe-coded.
And somebody went through and they, like, you know, checked everything's correct, like, this is obviously not great for maintainers, like.
when there's updates in the protobuf, I'm gonna have to come in here, whoever's updating it's gonna have to come in here and look and check these hard-coded strings, etc, so… I… I personally would love to see it generated from…
**pabcolli** 19:49 Yes. Again, yeah.
Yeah.
**Aaron Abbott** 19:54 Okay.
**pabcolli** 19:58 Excellent.
**Aaron Abbott** 19:59 Cool, thank you.
Keith?
I think you're up?
**Keith Decker** 20:05 Just a reminder for the events PR for GenAI.
Utils, Sirilla had made an update this week for some feedback, so just to summarize on it would be great.
**Aaron Abbott** 20:20 What was… can you… can you give, like, a high-level overview?
**Keith Decker** 20:23 It's adding events and logging for inference types for GenAI utils, because right now we have spans and metrics, so just adding events.
**Aaron Abbott** 20:33 I see. Awesome.
**Keith Decker** 20:35 And then we had a discussion around, like, you know, how to do, like, the flags around events versus logs, and so I think that's the… The, change he made.
**Aaron Abbott** 20:48 Okay.
**Keith Decker** 20:50 Yeah, he's, he's Asia at the time, so I'm…
**Aaron Abbott** 20:52 Yeah, yeah.
**Keith Decker** 20:53 Keeping this a reminder in the meeting for…
**Aaron Abbott** 20:57 Awesome, thank you.
I'm gonna put you on the spot, Dylan. It looks like you took a previous pass, I don't know if… If your comments are addressed, you wanna… What proof?
**Dylan Russell** 21:09 Yeah, I can take another look.
**Aaron Abbott** 21:12 Anyhow.
Still.
**Keith Decker** 21:15 Thank you, sir.
**Aaron Abbott** 21:19 Was the… all the feedback on, like, the environment variables resolved with the, the opt-in stuff?
**Keith Decker** 21:29 I believe so. I will take another stab at it. I looked at it a few days ago, so…
**Aaron Abbott** 21:37 Awesome, thank you, Keith.
Josh.
You're up?
**Josh Winerman** 21:46 Yeah, hey, Aaron, I can sort of talk about that. So, as an organization, we've been… are sort of pushing to get more involved in the community besides just the GenAI interests we've had.
And, with Pablo back, that'll be a little easier. But I've just been specifically looking for action items to help out. Been scanning through the blog a little.
Looking at some open tickets, I was just wondering if there's anything the SIG had in mind that the community might be interested in, especially what we're now deep into January, but, in 2026, specifically.
**Aaron Abbott** 22:23 Yeah.
Great, thank you, I'm glad to see that.
I can turn the floor over to other people if they want to say anything, but we are… we've been, like, working a lot towards the log stabilization. I think Ricardo's Probably got the most up-to-date knowledge on, like, what's open still there.
But there was… there was definitely a lot of backlog items for that. Some of them we… we said we could do after… After making things stable, and… but there were just some, like, you know, potential breaking changes we wanted to do before.
The log stabilization, so… I think there is a project board and an issue for that. I can try to… That's fun.
But yeah, if anybody else has, you know.
Work that you want some help with.
Feel free to jump in.
Yeah, so you can, you can look at this board, and kind of look at things that are… that are here. There should be some discussion, and I think this issue from Ricardo has… this one.
There's a different one somewhere where he, he wrote down, kind of, the project plan, but…
**Josh Winerman** 23:45 Okay, cool.
**Aaron Abbott** 23:48 Cool. Yeah, and thank you. Feel free to always, like, reach out on Slack, too.
**Josh Winerman** 23:56 Yeah. Probably will do, so look out for a message from me. But thanks, Aaron.
**Aaron Abbott** 24:01 Yeah, thank you.
All right, that's the end of the agenda, folks. Anybody else have anything?
**Marcelo Trylesinski** 24:10 Yeah, I have a question. We talked about the MCP instrumentation stuff, the context, thing.
Yup. Yep.
How are you instrumenting it, though? Like, do you have something special, or if you… so, for background for the others, Aaron has a possible pull request in MCP itself to fix how… streams work in NEIO?
and context varies fast, right? Something like that?
**Aaron Abbott** 24:41 Yep.
**Marcelo Trylesinski** 24:41 Yeah, so, if we fix that, does that already solve?
your problems?
**Aaron Abbott** 24:49 Yeah, so it's this one here. I know this is not our repo, but for context, this I think this unblocks monkey patching for most people.
Which, there's, like, several instrumentations out there, so I know Open Inference has one. I… does… I think maybe Logfire has something? Or Pydantic AI?
**Marcelo Trylesinski** 25:07 Yeah, we have something. Lockfire has something.
**Aaron Abbott** 25:11 Right, so I think you might already have, like, a kind of hack to work around this, but this would make it so that, at least within the MCP SDK, The context is passed down properly so that if you monkey patch at different layers, you can see the same context at both layers.
But… Yes, I would love… even after this, I would love to see, actually, like, native instrumentation in the MCP SDK.
Marcel, if you're the right person for that, or how you feel about it, but… Any thoughts?
**Marcelo Trylesinski** 25:45 Yes, I am pushing stuff in this repository.
So… What's your opinion about native against… in the contrib repository.
**Aaron Abbott** 26:01 Yeah, so I mean… One thing that comes to mind is the semantic conventions are, like.
Are not stable for this.
I think we could… could start pretty small.
But at a minimum, I would love to see, like, the context propagation implemented in MCP, which I think… I'll pull up the spec, but it's basically to put the standard trace parent and baggage headers into, the underscore meta attribute in MCP.
**Marcelo Trylesinski** 26:29 Right, so you'd have that on the client and on the server, and then you do the… Yeah.
**Aaron Abbott** 26:34 Yes, yeah, and I think there's also a SCP in the MCP, like, spec open to basically copy whatever we did in OTEL into the MCP spec.
**Marcelo Trylesinski** 26:48 So it's duplicated?
**Aaron Abbott** 26:50 Yeah, I wasn't super sure on that. I can dig it up. Give me a second.
**Marcelo Trylesinski** 26:59 You said that one of the SDKs already have it native, right?
**Aaron Abbott** 27:03 Yeah, I don't know if Ludmila's here.
But I believe the C Sharp one has it natively instrumented already.
**Marcelo Trylesinski** 27:10 Okay, so I'll probably ignore everybody, and if you want to open a request, we can stop merging stuff.
**Aaron Abbott** 27:18 Okay. Cool, we can, we can definitely start small, like, Tool calls and context propagation, right?
**Marcelo Trylesinski** 27:25 Yeah, there is one thing that's very important, is that, we are doing a big refactor on the… on the whole package.
So… I'm all… I'm breaking everyone, like, everybody's gonna be break… like, broke.
all the instrumentation packages are going to be broken when V2 is released.
So, I mean, maybe it's a good moment to have that native, anyway. Yeah, so what I meant is that maybe we can wait, a week?
where I think the API was going to be more stable, and then we can add it.
**Aaron Abbott** 28:06 Yeah, no problem. And, I mean, would it be helpful to see, like, a prototype to kind of inform the refactoring, or just… just wait?
**Marcelo Trylesinski** 28:14 Oh, to be fair, if you can open just a request, it's just… that's the minimum stuff, I don't think we're gonna… like, it's internal anyway, I don't think… I don't think the API's gonna change that much that the pull request will be… not valid. So… you can create and post a reference to the C-sharp.
what they're doing, so I don't need to argue with anyone that that's a valid request.
**Aaron Abbott** 28:48 Okay.
Yeah, sounds good.
The only other suggestion I would possibly make is, would you prefer, like, an indirection layer? I know sometimes, You might get, like, a… Kind of middleware or something, interface that you can implement to do the instrumentation to kind of decouple things, but…
**Marcelo Trylesinski** 29:07 That's… that's a good point. We are going to implement a middleware mechanism on the SDK.
So… I guess that'll be the right place, and then we can create, like, the OpenTelemetry middleware or something like that.
**Aaron Abbott** 29:27 Okay. Yeah, I would love to still see that, like.
as an extra or separate package in MCP, like, some way to get it, kind of out of the box as an official supported thing, like in C Sharp, but… Makes sense to me.
**Marcelo Trylesinski** 29:41 Okay, you want native. That's what you're saying.
**Aaron Abbott** 29:44 Yeah, yeah, I mean, I think that precludes middleware necessarily, but… What do you think?
**Marcelo Trylesinski** 29:49 No, but I mean, I'm… oh, I see. No, no, no, I meant… I meant a mirror, but, By default, included middleware.
**Aaron Abbott** 29:58 Yeah, yeah. Okay.
**Marcelo Trylesinski** 29:59 Yeah. You know, like, in Starlets, you have server error middleware? When… something like that?
**Aaron Abbott** 30:05 Yeah, yeah, that makes sense.
**Marcelo Trylesinski** 30:06 Yeah, that's Stadia.
**Aaron Abbott** 30:09 Okay, cool, thank you for bringing this up, that way we can avoid a new contrib instrumentation.
**Marcelo Trylesinski** 30:15 Here.
Thank you. Alright.
**Aaron Abbott** 30:18 Cool.
Anybody else have anything?
Alright, nice short meeting. Thank y'all for joining, thanks for the topics.
See you next week.
**pabcolli** 30:32 Thanks, bye.
**Marcelo Trylesinski** 30:33 See you, bye.
