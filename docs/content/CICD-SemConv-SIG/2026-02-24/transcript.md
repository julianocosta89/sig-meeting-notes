SIG: CI/CD SemConv SIG
Date: 2026-02-24
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/fAEK1XmjSdMx4uSRjZMcqn8sohEI0IPWtCE4nk0_mPJyn_M5VLfJrX5B3WMPVok.rjcpcjAVLtuxF-R_
============================================================

## Zoom Recording Transcript

**Adriel Perkins** 00:15 Good morning.
**Alan Clucas** 00:21 Assuming I have audio.
It's not always a guarantee.
**Adriel Perkins** 00:42 Yep, we can hear ya. Love the…
I say we, but really, I just made me improvement.
**Alan Clucas** 00:50 Well, the balance for you.
Yeah, sometimes when I unplug my laptop and unplug it back in again, it doesn't notice that… like, there's a microphone attached to my… In the same device as my video camera, and it'll notice the video camera's there, but Zoom decides… I mean, it's only Zoom. I haven't got a microphone. It decides the only microphone I've got is my monitor, which doesn't have a microphone.
**neil yashinsky** 01:13 This guy shouldn'.
**Alan Clucas** 01:14 My audio.
**Adriel Perkins** 01:15 Gosh.
**Alan Clucas** 01:15 But I've got 3 other possible microphones, or 3 total possible microphones, and none of them I listed.
**neil yashinsky** 01:23 I love that. Like, after all these years, like, we're still trying to figure out how to get drivers and, like, devices to work easily together. What OS, I must ask.
**Alan Clucas** 01:34 This is Linux, so…
which is Nix OS on the Nix, and it's… it's only Zoom. It's… it's the Zoom…
**neil yashinsky** 01:42 Right, right, right.
**Alan Clucas** 01:43 I restart Zoom completely. I mean, it's gone, and I restart it, and it still doesn't decide that they're existing, but, you know, other things can find them, so…
**neil yashinsky** 01:54 Does anybody have any idea how much, how much, hotel…
Instrumentation, the Zoom package, Zoom client has, out of curiosity.
**Alan Clucas** 02:03 No.
**neil yashinsky** 02:04 type of things I think about now.
Maybe I've been spending too much time in hotel meetings, I probably haven't.
How's it going, Alan, Adriel, Christoph?
**Alan Clucas** 02:15 Ugh.
I'm good. You?
**neil yashinsky** 02:18 Yeah, good, glad to hear it, thanks.
**Christophe** 02:22 Hello, I'm just listening in, I'm commuting.
**neil yashinsky** 02:26 Oh, okay.
No problem, Microsoft. Good to see you again.
Well, metaphorically speaking.
**Adriel Perkins** 02:35 Give everyone a couple minutes to go ahead and enter some stuff into the, the Google Doc, and we'll get started.
All right, it's probably… probably time we can get started. I'm using the coffee-making process as a time gauge, because I had not made one, but now I did, and now it's here, so now we can get started.
**neil yashinsky** 04:56 Genius! I love the natural rhythm of that!
Like, that's…
**Adriel Perkins** 05:01 Thank you.
**neil yashinsky** 05:01 fingers.
**Adriel Perkins** 05:04 Let's see, let me share my screen…
Alright, so first off, we could start with some triage.
Of… of things.
I was not here last week or the week before,
Apologize for not mentioning that earlier. I know I just kind of, like, disappeared.
**neil yashinsky** 05:31 Not at all that happens to the best of us. I feel like this is, like, you know, it's almost like, volunteer work in a specific, weird way, so, like, have… it's good to hold ourselves accountable for stuff, even this, but I feel like we should all give ourselves a little bit of an extra pass for being brave and crazy enough to do stuff like this.
**Adriel Perkins** 05:50 For sure. Does anyone know if there were, like, any mentioned updates on this one?
Over the last couple weeks.
**neil yashinsky** 05:58 Yeah, so I'm kind of… I know Christoph is commuting, but yesterday I sat in on the, what was it? See, too many, too many, hotel meetings, and they all start running together.
**Christophe** 06:12 Yeah, it was the general SUMConf meeting.
**neil yashinsky** 06:15 Yes! Thank you, and Christoph, I feel like you're really a much better position to talk about it, but I know you're commuting, so if you want, I could… I could.
**Christophe** 06:25 I can tell a bit about it.
Carlos was, proposing some stuff the last few weeks.
Okay.
Generally, it was, how can we Send long-running spends using events.
So, in some cons, we call some events.
But it's just structured looks.
**Adriel Perkins** 06:48 Yes.
**Christophe** 06:52 And, yeah, he proposed… to use a span processor.
That way, we could make fast progress.
**Adriel Perkins** 07:02 Oh, correct.
**Christophe** 07:05 But yeah, yesterday, Josh was also talking about it in It's a general SUMCOMF meeting.
And basically, he was saying… That's the direction that hotel is going.
That we can send… Anything using events.
Actually, that we can send spans as events.
So probably there would also be some Spec changes coming here.
**Adriel Perkins** 07:41 Alright.
**neil yashinsky** 07:42 And what was interesting is, I was trying to tell, but just lacked the overall context.
Because I… thank you, Christopher, for chiming in, because I was really… There's, like, a… like…
the language people use to develop semantic conventions, let's say, is new to me, and so I try to really understand
people's intentions as much as their words before I try to make a judgment. It's not… might even say it's not my strongest suit. So you go… but yesterday, I was trying to decide, this… oh, Carlos is here, perfect, perfect. I was trying to decide if… like, what Josh was saying was…
oh, this is a good idea, you know, we as a standards body will get there eventually, good luck on your way, or kind of like my alternate reading was like.
Well, this is a really big change, and it's far ahead of where we are as a standards group.
And essentially had a sort of less supportive…
Than what Kristoff just described, which, again, I have no idea if I'm right or wrong, or, you know, maybe we're both right in certain aspects. But Carlos, we were just talking about the general meeting yesterday, and kind of Josh's reaction to…
your proposal. Which I really kind of thought, down to it, like, I was wondering if Josh really understood in detail what was trying to be accomplished, at least in the CICD group.
In particular. But Carlos, I would love your, your sense of things from yesterday.
**Carlos Alberto Cortez** 09:24 Yeah, so, long story short, I haven't talked to Josh. I did a review of that project, that project probably Adriel and, Christoph and many others have seen already. It's a project that Josh has on, like.
Sending, out-of-band spans, basically, you are mapping a shared section of, memory.
And so, if the process dies, you send those events later on.
Some backend, like, reconstructs them, like, the collector plugin.
**neil yashinsky** 09:53 Okay.
**Carlos Alberto Cortez** 09:54 Yeah, so the interesting part, however, about that, that mostly would benefit us, is that now… so, he started that project, like, one year and a half ago, on his free time, I think. But now, what he's doing is that he's also firing events.
For those, like, for this… exactly for the life cycle of these fans.
And unlike us, he has had more experience testing that against, I'm guessing, some Google backend or prototype or something. So that's when… that's where it becomes interesting, because he was mentioning, like, this amount of data for the hard bits, you may want to send more, but then you have to balance things and configure things.
So, I haven't talked to Josh, but my impression after yesterday's call is that
He thinks that we should work on both, because nobody knows which one will win, because we need that.
And he thinks… I asked him yesterday, like, you think we should instead abandon this relatively simpler approach, where we have the spam processor that grabs another spam processors and report events.
And go for years? And he said, no, not necessarily, especially because what he has may take a long time to be, you know, adopted, and we don't know
Like, how… how, dependent we can be on that approach. Bottom line.
Basically, the idea is that we go, we check what he has been doing, inspect more stuff, learn from that.
And we come back, do the same con group, or the specification, or both, and discuss potential trade-offs there, yes. One of them being, for example, how do we encode stuff,
For example, sorry, what things to encode, what things to live out.
**Adriel Perkins** 11:46 Cool. No, that's a great summary, thank you for that.
**Christophe** 11:50 Yeah, it was also my impression that we should go forward with the Fast approach, no.
And in the long term, George's approach of sending events in a generic way might win out.
And also, Josh… was already aware of the long-running traces issue in CICD, so…
He knew what we were talking about.
**Carlos Alberto Cortez** 12:18 One funny thing, by the way, about his approach, that's just for your information, is that he's using those… he's reporting those events using his own Proto format.
**Adriel Perkins** 12:28 Oh, yeah, okay.
**Carlos Alberto Cortez** 12:29 Which kind of reminds me of the early, client.
proposals about something, they're called, using a custom format, like, derived from, you know, from OTLP, but not quite the same.
So that… yeah, that's, for example, why he's actually sending the trace or span ID of the parent, sorry, span ID and trace flags as, you know, as numerical values rather than the syncs and so on. But still, there's value there, you know? We will just be using standard, you know, logins.
part, yeah.
**neil yashinsky** 13:02 it did kind of make me wonder, like… and again, I'm so new, so there's lots of reasons for me to still be trying to piece this together, but one of them that I was trying to match up with was, from what I know about Alan's use case specifically, or, you know, the CICD context, I just heard most about it from Alan, is that…
there's kind of inner and outer mechanics that are relevant for the task involved. Alan, please correct me if I'm wrong, but I feel like what Josh was talking about was the inner. Super important, you know,
kind of trying to see things from the ground up, and I don't know specifically, but I kind of inferred, because it's what I was doing in that attempt, is understanding CICD, if you will, from the top down. So, like, the, the…
parent…
Span, if you will, the parent job or whatever, and understanding how that's operating on a surface level, you know, from top down.
I think both for the same purposes, understanding observability in the center or whatever, and being able to optimize, troubleshoot.
But I felt like that was… I didn't… you know, I don't have a… it was just novel to me, I think, and Alan, correct me if I'm wrong, but I actually had to ask you directly, like, when you think about this task.
Are you trying to provide visibility into, first, like.
you know, how much time is being spent, you know, where the process is, if you will, versus, like, what the process is doing at any one given time inside, like, kind of Josh's description, right, of, like, mapping memory and, you know, system execution layers.
Or were you both, or… yeah, am I off-base?
**Alan Clucas** 14:50 My initial… problem… The one that needs long-running spans is…
is the… I… I just need them to be very big at the top level. I'm not…
that worried about… lie… I'm not… I'm not… my problem isn't live…
inspection at the moment. I think live inspection is… Sort of useful, but mostly…
If you are live inspecting CICD, you're doing it wrong.
**neil yashinsky** 15:25 Yeah, I mean, maybe there's some exceptions, but okay, good, so yeah, so…
**Christophe** 15:29 quite a few issues where I needed to live inspect.
**neil yashinsky** 15:32 Yeah, so…
**Alan Clucas** 15:35 But I'm not trying to… I'm not trying to use the information from a live inspection to make dynamic changes.
**neil yashinsky** 15:42 Light.
**Alan Clucas** 15:42 to what is executing now. Yes. That, I mean, most CI systems, at least.
almost forbid it. It's…
**neil yashinsky** 15:55 Right.
**Alan Clucas** 15:55 Not… there aren't… there aren't access points to do it. Yes, live inspection is a secondary nice-to-have.
**neil yashinsky** 16:03 Right.
**Alan Clucas** 16:03 I can kind of… you can kind of get there already with…
bits of it, because you can know… you can know your top-level span ID.
**neil yashinsky** 16:17 Right.
**Alan Clucas** 16:18 You just can't look at it because it's not arrived yet, but your low-level spans still have that as their top-level parent, so you can go and query for everything that has that as the trace, you know, the top parent.
Oversimplified.
**neil yashinsky** 16:32 I hit a pit.
Oh, sorry, go ahead, please.
**Alan Clucas** 16:35 No. I was gonna say, to oversimplify it a bit.
**neil yashinsky** 16:38 You're most interested in, like, the where are you in the process, not what is the process doing right now.
**Alan Clucas** 16:46 I'm… no, really, I'm interested in looking at it in the past. Everything has happened, I want to just be a… my primary goal, because I don't have anything at all yet, I mean.
Is, at the end of a run, what went… what happened? Why did it take twice as long as it did yesterday? What went wrong? Why is… why has it failed today when it didn't yesterday? Those are the questions I'm trying to answer, not…
live inspection in any…
**neil yashinsky** 17:17 Retrospective view of sorts, or.
**Alan Clucas** 17:20 Which is… it's how spans… I view spans as being used everywhere, you know. You can't… an HTTP
process span, you know, is all over in a second, and… or hopefully. And it's a really bad website. Yeah, so the original users of spans weren't doing any kind of live inspection.
**neil yashinsky** 17:39 Right, right, right. That's being able to get down and…
**Alan Clucas** 17:43 being able to do that would be a secondary nice… it would be very nice to have, and it would be a problem I'd like to solve eventually. Right. We can solve it along the way for this one, which it sounds like we're going to, potentially. Although…
If what happens with events turned into spans is that
the backend knows nothing about this in this intermediate processor, then the back end doesn't know anything about those resulting spans until we've reached end on the span, so we're… we're not solving that problem. But I'm not that fussed about that from my perspective. But then I… I'm building something that I hope people will like, rather than
Absolutely knowing what people really want out of it, because.
**neil yashinsky** 18:26 Right, right.
**Alan Clucas** 18:26 this has to go. I've talked to a number of people, you know, a number of
Customers and open source users of
About what the needs are, but, you know, you have to then go and build something, put it out there. I'm labeling it as beta, and…
Seeing what happens.
**Adriel Perkins** 18:44 So, Carlos…
**neil yashinsky** 18:45 What would be the next steps, for this? Is it a proposal to use span process, or is it a proposal to look at Josh's stuff?
**Carlos Alberto Cortez** 18:55 Yeah.
**Adriel Perkins** 18:56 what else?
**Carlos Alberto Cortez** 18:57 No, the proposal is, for now, on our side, to keep on working on the spam processor. I already have the PR and the prototype in Java for some days now.
The only thing that is that I didn't want to present that in the spec, because I would like to double-check what Josh has.
And then probably massage that, as a semantic conventions PR. So, this week, I'm guessing today or tomorrow, I will create a draft PR or something like that for, again, same comp.
So the idea, basically, is that we have to, encode, many things there.
Like, and also there was a brief, discussion yesterday, by the way, which was related, regarding, like, what if you want to actually use,
like, trace ID, trace flags, trace, you know, other stuff, like, for your parent context as attributes. So basically, that's, like.
how we want to encode that, you know? Encoding attributes, so that could be the first part. Once we have at least a draft PR that some people have been reviewing for a couple of days, I will open the PR again spec linking to, you know, to that one.
So that's… that's the plan for now, yeah. Okay. One of the… yeah, one of the related things, by the way, just for…
May slow us down, but in the future give us
Give us more velocity is the fact that
Same code now is, like, you are aware of that, probably some of you, that they are trying to federate everything.
So, there's a chance that the stuff that we are doing will be federated, to some incubating part.
That is being discussed, like, it seems.
So, it may take a little while, but once this incubating portion, is ready at some comp, we will be able to move fast, you know.
Yeah, so those things… so that raises a question, like, because this is, like, I have been doing that as a relatively low priority.
But, also George mentioned that we should try to go faster on this one, you know?
To at least have a prototype that works, that can be tested against backends, so probably there's value in trying to spend more cycles there.
**Adriel Perkins** 21:21 Yeah, that sounds good. Awesome.
Do we need a… do we need a prototype at all for, like, a processor within the hotel collector?
resources in Java?
**Carlos Alberto Cortez** 21:30 Let me think…
**Adriel Perkins** 21:35 I guess it would actually be a connector, but.
**Carlos Alberto Cortez** 21:40 Yeah, yeah, I don't know whether there's any value, unless it's only for the internal spans in the collector.
**Adriel Perkins** 21:52 I mean, we could start with internal spans on the collector, but I mean, we could… we could essentially make a log-to-trace connector that turns logs to traces, right? Which are events. So if they have a set of metadata, we can directly turn them into… that's what I was thinking, like, do we need a prototype of that?
If so, I'd be happy to do that.
**Carlos Alberto Cortez** 22:12 No, I don't think we need that for now. We may, based on the feedback, so I could advise against that, especially if you are…
Taiyan Cycles?
Ultimately, we discuss at the specification, and we can call people whether they think this is something they would like to see, you know?
I can't imagine that happening later down the road.
First, we would like… I would like to get an initial betting on this one, so we know that people are not too unhappy with the approach.
**Adriel Perkins** 22:43 Okay.
**Carlos Alberto Cortez** 22:44 So let's perform that for now, yeah.
**Adriel Perkins** 22:47 Okay.
**Alan Clucas** 22:49 I'm assuming it's… it would be the only bit of… if we didn't have a connector.
There wouldn't be a way of achieving this without backends.
**Adriel Perkins** 23:00 Correct.
**Alan Clucas** 23:01 So, it does feel like a thing that would… eventually what I'm doing.
**Adriel Perkins** 23:06 Or direct application, or service handling.
**Carlos Alberto Cortez** 23:14 You know, you know what? Well, go ahead.
**Adriel Perkins** 23:17 No, no, you had, sorry.
**Carlos Alberto Cortez** 23:19 Yeah, Adriel, something that probably is… because it seems that you have something in your mind, it would be for you to describe what you think, how this could be done without even a prototype, but if you have something in mind.
Yeah, I would like to, you know.
To read your notes on that, if you can write them down, or just spend, for example, half an hour, one hour, thinking.
on how you would face these, what are the advantages, disadvantages, it would be great. Prototype, probably not needed.
For now, but it could be nice to have that point, you know, in the horizon for now.
**Alan Clucas** 23:58 I would be interested in seeing that as well, because it's something I've assumed we would end up doing.
And…
I could give you a…
And I'll go workflows that spat out the logs instead of spans, so we could try something.
If we ever get that popped up.
**Adriel Perkins** 24:21 Yeah, no, I mean, that makes sense. Okay, yeah, I'll, I'll spend some time writing that down, and
If, if you have any more meetings with Josh that you, like, would care to not have other people in, I'd love to join, so…
I haven't talked to Josh in a while. I always enjoy chatting with him, so I'm curious to hear and see, like, that prototype.
**Carlos Alberto Cortez** 24:42 Yeah, at the very least, we can chat in Slack, like, or, or, like, for these, yeah.
**Adriel Perkins** 24:49 That sounds good.
Cool. Thank you for all your work on that, really appreciate it. I know it's a lot, a lot to wrangle, because you've got to go to a lot of different places, but certainly appreciate it.
**Carlos Alberto Cortez** 25:00 Yeah, totally, yeah. Let's see, it's coming slow, but, you know, that's better than having no progress at all.
**Adriel Perkins** 25:06 Exactly, exactly.
**neil yashinsky** 25:08 Good, well done.
**Adriel Perkins** 25:09 And it just makes it more durable once it lands, right?
**neil yashinsky** 25:13 Yeah, exactly.
**Adriel Perkins** 25:15 Okay, so Python's been merged, we talked about that. Java has been reviewed and should be merged pretty soon. I don't know why it's not showing up here. Oh, it's showing up here, that's where it is.
So yeah, Java should be merged soon, and I think CPP might be picked up pretty soon. I saw some messages come through there, and I don't…
I don't know where they stand. Actually, CPV might already have, oh.
Okay, look at that! CPP is done. Somebody already did it and merged it. How cool is that?
And Java should be merged soon. So that's 3.
And then we've got a few other in progress, right? We… the GO one's in progress, I think, still.
**Alan Clucas** 26:07 Yeah, yeah, I will pick it up, before next meeting.
**Adriel Perkins** 26:10 Awesome, awesome.
Cool, we're… we're moving along. That's, like, that's pretty… that's pretty cool to see. It's not like it took 4 years to get it into the spec, so, like, you know, it's, it's awesome.
Awesome, makes me happy.
Do we have any updates on anyone picking up any of these to-do items yet?
That would be the, the model of key events within a CI-CD system. Actually, so that, you know, kind of relates to, events that might be turned into traces.
the SimCon mapping of GitHub concepts to SIMCOV, any of this stuff.
Do we know.
I'm guessing not.
But, it… so I guess here's my call-out. If anyone would like to pick up any of these things, please feel free to look at it, comment on it that you want to pick it up, and I'll get it assigned to you.
The other…
thing that I wanted to talk about pretty briefly is the Semantic Convention's 2026 roadmap. I have not, responded to this. They're specifically looking at this in the lens of what
what semantics are on the roadmap, right? Whether or not they're being stabilized, whether or not they're being added, etc. I know we have some things that I think our SIG is focused on a little bit of spec.
a little bit of not spec, a little bit of semantics, so we're kind of, like, a little bit in multiple domains here. But I just wanted to kind of get a gut check that the work on the board here
we're not missing any key things between that and the community, original community PR, that we can add to the roadmap for 2026 for, semantic conventions. So, I was gonna write a little draft of this, but if there's anything that, y'all want to take a look at and, like, comment,
Let's see, where would I want you to comment? Comment in underneath this… this general section here.
Of things that you think should be here?
That would be, pretty helpful.
**Christophe** 28:21 We have an issue for making the CICD someConv.
Release candidate?
**Adriel Perkins** 28:32 No?
What is… what is that?
**Christophe** 28:37 I was thinking, many of the other… 6 are now…
introducing PRs to make their conventions release candidates.
And for CICD, I guess we can wait a little bit until we have One or two more.
prototypes?
And then we can go the same way.
**Adriel Perkins** 29:00 Okay.
**Christophe** 29:08 Yeah, it's sort of… Going this intermediary step instead of going directly towards stable.
What do you think?
**Adriel Perkins** 29:21 Yeah, I haven't… I haven't seen the release candidate stuff,
But sounds good, based off of the description.
I guess the rest of the items would probably be, like.
For… aside from the deployment environment stabilization, which is already ongoing, there's a PR for that that's been approved, you're just waiting on a couple minor changes.
I think the main thing is, like, modeling the CIC system events.
The test, like, a prototype of test conventions.
A prototype of incident conventions, and then…
really the unified semantic conventions for Task Workflows, pipelines, jobs, which is, probably… like, it's on the roadmap to discuss for 26, but I doubt it's gonna happen, because it's talking about names, something that's very…
**Christophe** 30:29 There was how difficult it was to learn the initial
PR for CICD, I guess it will be very difficult.
And we also need to have at least one prototype, or… Probably multiple for this one.
Yeah, I guess it will be difficult.
**Adriel Perkins** 30:56 So, any objections to me putting those things on the roadmap?
Alright.
Anything we miss talking about?
**neil yashinsky** 31:19 I don't think so, but…
I'm not a good judge. But I hear what your question is, and I answered it to the best of my ability.
**Adriel Perkins** 31:27 Awesome. Well, thank you all for attending today. I'm enjoying working with y'all, so thank you so much for coming, and…
And working on all this stuff. We'll see you next Thursday, and offline.
**neil yashinsky** 31:38 your committee.
**Adriel Perkins** 31:39 Right.
**neil yashinsky** 31:39 Good run.
**Christophe** 31:39 See you next week.
**neil yashinsky** 31:41 Helen, Christoph, Carlos.
**Carlos Alberto Cortez** 31:43 Oh, yeah, I can see you.
