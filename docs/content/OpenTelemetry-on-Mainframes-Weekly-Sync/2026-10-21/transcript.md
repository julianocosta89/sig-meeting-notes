SIG: OpenTelemetry on Mainframes Weekly Sync
Date: 2026-10-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Rüdiger Schulze (International Business Machines Corporation)** 00:49 Hey, Jim, good to see you.
**Jim Porell (Rocket Software, Inc.)** 00:53 Back in the car.
**Rüdiger Schulze (International Business Machines Corporation)** 00:55 It's one to go for sports.
**Jim Porell (Rocket Software, Inc.)** 00:57 Yep.
**Rüdiger Schulze (International Business Machines Corporation)** 00:59 Okay, good. Are you in Atlanta next week, eventually?
**Jim Porell (Rocket Software, Inc.)** 01:02 I am. Are you?
**Rüdiger Schulze (International Business Machines Corporation)** 01:04 Yes, I am. Okay, very good.
**Jim Porell (Rocket Software, Inc.)** 01:05 Alright, cool.
**Rüdiger Schulze (International Business Machines Corporation)** 01:08 Okay.
**Jim Porell (Rocket Software, Inc.)** 01:10 Yeah, we have a Customer Advisory Council on Monday.
**Rüdiger Schulze (International Business Machines Corporation)** 01:13 Right.
**Jim Porell (Rocket Software, Inc.)** 01:14 But Tuesday and Wednesday, I basically am free the whole time, so if you've got certain times you want to get together, we can figure it out.
**Rüdiger Schulze (International Business Machines Corporation)** 01:22 Yeah, let me check the calendar, and I send you some times that will work.
**Jim Porell (Rocket Software, Inc.)** 01:28 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 01:29 Tuesday, actually, I think looks good, but I haven't done my agenda yet, so…
**Jim Porell (Rocket Software, Inc.)** 01:33 Yeah, but I haven't looked at it, so…
**Rüdiger Schulze (International Business Machines Corporation)** 01:36 Okay, let's give it a few more minutes, maybe Richard is joining, I think Matt is traveling, so…
**Jim Porell (Rocket Software, Inc.)** 01:43 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 01:45 I put some notes in our, Meeting minutes, Couple of things for awareness, and a couple of other things just for… You know, logistics.
Did you have a chance, maybe in the meantime, I mean, I know this PR20 with virtualization and mainframe is large.
But did you have a chance to… to maybe take a… take a look at that one?
**Jim Porell (Rocket Software, Inc.)** 02:15 Not in terms of splitting it up, no. Yeah. I just… I've got 150 charts right now for the CAIC meeting. I'm doing the whole thing for 4 hours. Okay.
I've been just like, oh my god, I gotta squeeze this down, so… I'm writing like crazy.
**Rüdiger Schulze (International Business Machines Corporation)** 02:32 So what I will do is, also put it in the notes, you know, I think I will split the PR, you know, in the first week of November, making it smaller, and maybe it makes this then also easier for us to go through this, and It will be approximately 20, I did already some exercise, so, that should actually help. But… what I think, you know, and we had this discussion, right, would you put everything via hotel or not? It's actually, to some extent, what this exercise does is it helps to find, then, the names that we need, maybe for other layers where it's more relevant. So… I want to go through this, and, you know, and then, like we discussed, it's actually up to providers what they want to implement, it's also up to customers what they want to use, right?
I think at some point, might be not yet there, but at some point, the best is actually if you would just describe How to do the naming from a mainframe point of view, so that if somebody comes up with, you know, some arbitrary metric or telemetry, then kind of, like, can follow the schema and derive of how it should be named.
**Jim Porell (Rocket Software, Inc.)** 03:57 Yeah, I think the interesting aspect of that is, Like, we did that with our experimental stuff, is we tried to use what was coming out of the SIG and say, you know, this is what we would recommend, but for the moment.
most of the products, and I don't care which one you use, and Stana included, you know, now, since Robert joined, I'll say Splunk, you can do custom dashboards on your own.
But if you can get close to the naming conventions, when the analytics platforms adopt the naming and include them in their built-in dashboards, then it's not traumatic change.
**Rüdiger Schulze (International Business Machines Corporation)** 04:41 I just realized, Robert, I put the notes that I wanted to discuss today to the wrong day. Last week, obviously, we didn't… Didn't do much.
So, now the notes are complete. So this was kind of, like, just an excursion into… You know, some topics around semantic conventions, how to do that from a mainframe point of view.
So, the first thing to be aware of, this is, the PR4201 from the semantic conventions.
Maybe I can share my screen here, makes it maybe easier.
D, you can see this, right?
**Jim Porell (Rocket Software, Inc.)** 05:25 Yep.
**Rüdiger Schulze (International Business Machines Corporation)** 05:26 Okay, so, and if I click now on this, this should actually open.
So this was something that Miller from the… from the… semantic convention Sync has been working on, and she also posted this to the Slack channel.
But the important point is that the COS entities and also the few attributes that we had so far for CUS, they are now deprecated or removed, actually, from the base semantic conventions.
And what that implies is also that we need to introduce this in the… to the… Essentially into the federated semantic conventions.
And, I would do that in the week after, in the second week, or first week, actually, in the week of the 2nd of November.
To put this forward.
And then, this is something which we… probably wanna… A process with some priorities so that there's, again, an equal state.
**Jim Porell (Rocket Software, Inc.)** 06:25 Right.
Yeah, that week, I could probably help you,
**Rüdiger Schulze (International Business Machines Corporation)** 06:30 Yeah.
**Jim Porell (Rocket Software, Inc.)** 06:30 Because, like, you know, we both are at the Tech Exchange next week, so I'm, like, kinda… Killing myself trying to get ready for that.
But I think I'll have a lot of free time after that.
**Rüdiger Schulze (International Business Machines Corporation)** 06:42 Okay Sounds good. And then, Robert, what we discussed, and, I don't know if you had a chance to look at this PR20, which is a huge one. If you haven't done yet, it might be actually worthwhile to take a look also from your perspective. It's covering… Virtualization, which we… Have not in the basement conventions today.
And, it also covers the base concept of the HMC API, so building on each other from a mainframe point of view.
And that's why it's a lot. And we will split it up. We will split this in approximately 20.
PRs to be more digestible. This is happening in the… also in the first week of November.
But from a con… to get the concept, actually, having everything in one place is actually not so bad, because it's kind of, like, allows you to better digest the concept. So, yeah, and we are looking for feedback, right? And we probably also want to put this forward to the semantic conventions Sync just for feedback at some point, but probably it's also good if we have an initial view on this.
before.
**Robert Pająk (Splunk Inc.)** 08:02 from other things, what I often do, because it's a very common practice that you make this one PR, which is, you know, capturing a lot of things, and then you split, but having this one, even as a reference, when you create the little ones, can sometimes help to, you know, go back and forth.
I usually put, like, a kind of a label, like a prefix, do not merge, or sometimes also POC, and sometimes in the first line, then this is, like, the end-to-end visualization that it will be split up to, you know, more PRs. It helps.
the people who are reading it, to make sure that they should intend to capture on the high level. Also, maybe AI as well.
**Rüdiger Schulze (International Business Machines Corporation)** 08:41 Yeah, okay, that's actually a good point. I would put that into the PR, actually labeling it, and then… actually, we can do this right now.
So,
**Robert Pająk (Splunk Inc.)** 08:59 You're not logged in, that's why.
**Rüdiger Schulze (International Business Machines Corporation)** 09:01 I'm like, oh, yeah, okay, then delete this now, otherwise I'm in trouble.
Okay, fair enough. Let me go back to the… to the notes. I have the… problem is now I have the Zoom window in front here, right? So, okay, yeah, but that's a good point, actually, to… to make things easier.
And the last thing is, this is probably really more for the mainframe community, and Jim, as you are on… The Opleano project, we want to kick this off with a technical community, as we discussed earlier, and it would be good to find a common date I'm suggesting, actually, Mondays, and would, like.
to propose to 16s, but I will send an email to those who have been involved and asking if this will work, or if there's any other better date that, you know, people would like to have.
**Jim Porell (Rocket Software, Inc.)** 10:05 I'm just looking, yeah, Mondays are pretty good for me, so not a problem.
**Rüdiger Schulze (International Business Machines Corporation)** 10:11 Okay, good.
Yeah, so, Robert, this way, the meeting is probably short, but I see, actually, that we are making progress. There is, semantic conventions out there. There's a few other things, This is unrelated to Mainframe, I have to make this disclaimer, but as we may still have a little bit of time, and you're also actually both in this space, we received a proposal from some… somebody who… works with MQ and messaging, but in the end, it's actually unrelated to this. What, the proposal is, is to consider introducing gap spans, and a gap span would be… If you have, for instance, certain processing happening, and there is a delay.
So what you see in your observability backend is, essentially, you see the two spans and you see a gap, but you can't react, really, on this gap unless you have an indication of this.
And the question was if, actually, it would be… reasonable to introduce these gap spans, and potentially you could do this with the collector and the processor.
To detect such a situation, if you have full visibility to the trace.
You have the kind of, like, sequence of the traces, and you could determine where gaps… in your sequence are, and you could fill them Potentially with a span in between, and then you can actually… so it's an outer… kind of, like, auto-generated span.
That would fit between what you get from your application.
But it would help to get alerted on if the span is, for whatever reason.
growing. So it's not about the execution, it's actually the wait time that is growing that you are measuring with this.
**Jim Porell (Rocket Software, Inc.)** 12:12 I'm kind of wondering, because you mentioned MQ, is it like a store and forward queue, and it just hasn't been popped off the queue yet, so it's sitting there, idle?
**Rüdiger Schulze (International Business Machines Corporation)** 12:21 Yeah, that would be a scenario, right? It's sitting… kind of like, it's sitting forever on the queue.
**Jim Porell (Rocket Software, Inc.)** 12:27 Wouldn't you identify it, though, as still being within the MQ… Sphere.
**Rüdiger Schulze (International Business Machines Corporation)** 12:33 Yeah, you would have different ways of… I think the, you know, things like growing Q counts and things like this, they could tell you.
But, this is really specific for… that you'll see this from a trace perspective.
**Jim Porell (Rocket Software, Inc.)** 12:49 Yeah, I kind of get what you're saying, but I was wondering, even on the trace, though, wouldn't… the MQ to fill that gap, you know, because it hasn't left the queue and gone anywhere else.
**Rüdiger Schulze (International Business Machines Corporation)** 13:02 MQ itself, at least when we look at the CS implementation, it wouldn't… you would only have the MQ put and DMQ get, but if there is a, whatever time spent, elapsed time in between. You would see the elapsed time, right? But you would not see.
**Jim Porell (Rocket Software, Inc.)** 13:17 Yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 13:17 education… where that comes from. And the MQ kind of, like, kind of, like, case is maybe more obvious, because there's this clear concept of put and get, but maybe there are other cases where you have that.
Yeah, so, Robert, we would be interested in if this is… we were also thinking to talk to Antoine about that, if this is something of interest.
We would, look at, maybe.
kind of like prototyping an exporter and bringing this to the collector's sick at some point.
**Robert Pająk (Splunk Inc.)** 13:55 I think it's actually more to the specification repo, even than the collector, because it needs to be, like, defined, like, anything which is also on the profile level.
**Rüdiger Schulze (International Business Machines Corporation)** 14:07 You were right.
**Robert Pająk (Splunk Inc.)** 14:08 I think, at least, and I think it will be also, you know, like.
In theory, it could be only something artificial on the collector side, but the risk is that then nobody really understands this, it's totally artificial, and the question is, do we want to have some, you know, added some… do we want to make it, you know, on the specification, some higher thing?
Do we want to think about it holistically?
or just, like, personally, I'm always afraid of adding any artificial things like that, because it often means that for instance, some components will need to remember what's going on and, you know, keep it in the memory, for instance. Oh, I have created, you know, something new, and I need to keep this kind of span which created this message.
Until I, you know, until something fetches it. And it can grow if something goes wrong with I don't know, with the queue, or with the thing who's receiving it, then you're just going out of memory.
So, actually, it can even hurt your observability and can hurt your application, and it can, you know, it can make more problems than benefits, and from my experience so far, usually just backends try to detect those things when they happen.
**Rüdiger Schulze (International Business Machines Corporation)** 15:29 Yeah.
Well,
**Robert Pająk (Splunk Inc.)** 15:33 So, also one thing, I think there are also different ways how people implement messaging. I think right now… I think right now the semantic conventions are… but I also may be wrong.
are trying to push towards… we have a span which is a producer, and a separate which is, receiver.
Or… Or processing, or whatever, and there are two separate traces that are just linked together.
So, you do not have this very long, long spanning thing, and then it's up to the backend or whatever to correlate them in their database or whatever.
**Rüdiger Schulze (International Business Machines Corporation)** 16:11 Do you… I haven't… I haven't followed this… do you maybe have a link to… is there… is there any OTEP or anything, or any issue for that, eventually?
**Robert Pająk (Splunk Inc.)** 16:23 for the… for the gap spans? No, I never…
**Rüdiger Schulze (International Business Machines Corporation)** 16:26 No, no, not for the gap spans as such, but what you just described of linking the…
**Robert Pająk (Splunk Inc.)** 16:32 Could you open… could you open the semantic conventions repo? Maybe I'll find it quickly.
**Rüdiger Schulze (International Business Machines Corporation)** 16:44 I mean, are you just… I mean, I'm aware of links, generally, but I wasn't aware for using this from a messaging point of view.
**Robert Pająk (Splunk Inc.)** 16:55 Could you just remove the ending, the suffix?
**Rüdiger Schulze (International Business Machines Corporation)** 16:59 Oh, yeah, this is… we are in the wrong one, yeah.
**Robert Pająk (Splunk Inc.)** 17:04 And I think if we go to the docs, Probably, we'll just find…
**Rüdiger Schulze (International Business Machines Corporation)** 17:08 Oops, sorry.
**Robert Pająk (Splunk Inc.)** 17:10 No problem. And I think it's messaging?
**Rüdiger Schulze (International Business Machines Corporation)** 17:14 Yeah…
**Robert Pająk (Splunk Inc.)** 17:17 I'm not sure if it's… and the message expands.
**Rüdiger Schulze (International Business Machines Corporation)** 17:20 Let me see…
**Robert Pająk (Splunk Inc.)** 17:22 And here, I think there are a lot of examples, and there are these consuming spans, groups, etc, and there are a lot of patterns here, and I think there are even mermaid diagrams, which are rendered here, if you slow… if you just scroll down quickly through the whole document.
Scroll, scroll, scroll, and I think there should be diagrams, unless something trains substantially.
Maybe it was sitting at the bottom?
Oh, here are some examples.
**Rüdiger Schulze (International Business Machines Corporation)** 18:02 Okay.
**Robert Pająk (Splunk Inc.)** 18:02 links, and I think there… and there are even, you know, this is like a general guidance for the con… for the messaging, and also then, depending on the tech… the messaging technology, sometimes you have different suggestions how to link the spend when you're using SQS, when you're using Kafka.
etc. So, depending if it's a queue or with some notification system.
Yeah, I think there may be even some different semantics here.
**Rüdiger Schulze (International Business Machines Corporation)** 18:34 Yeah, so…
**Robert Pająk (Splunk Inc.)** 18:35 Usually, there's, like, usually there's a gap, you know, that's what you tell, usually there's a gap between, and yeah, so far, we just live with the gap, because tracking the gap was, you know, some… someone would need to pay this cost, and for sure, we do not want the instrumentation applications to pay this cost. Maybe it could be the collector indeed?
But, yeah, it could be difficult.
And you mentioned a scenario where someone may want to collector, but then… you can… you can just have problems with your collector if it actually happens.
**Rüdiger Schulze (International Business Machines Corporation)** 19:09 Yeah, Are you… just, out of curiosity, I haven't really checked this, are you saying you would be able to detect spans in the product that you are working for?
You know, you have two spans, would you be able to detect if there's a gap?
**Robert Pająk (Splunk Inc.)** 19:34 Probably.
**Rüdiger Schulze (International Business Machines Corporation)** 19:34 It's growing.
**Robert Pająk (Splunk Inc.)** 19:35 Yes.
**Rüdiger Schulze (International Business Machines Corporation)** 19:35 That's kind of like the use case here. I mean, if this is covered by… and I really haven't looked at this, if this is covered by the observability tools, then there's probably no need to do this.
**Robert Pająk (Splunk Inc.)** 19:47 We will need to ask Antoine for this.
**Rüdiger Schulze (International Business Machines Corporation)** 19:49 Yeah, I do.
**Robert Pająk (Splunk Inc.)** 19:50 Thank you, though.
**Rüdiger Schulze (International Business Machines Corporation)** 19:52 Yeah, okay. But anyway, this is good input, yeah, I've… I think our implementation is actually a parent one, a producer to consumer… I wouldn't know a different… I think it's parent-child, what we implemented in this way, but, yeah.
Good, this is good reference. Let me also copy this over.
Okay, good.
Anything else for today?
**Robert Pająk (Splunk Inc.)** 20:33 So, action item for me is to review the PR. That's the…
**Rüdiger Schulze (International Business Machines Corporation)** 20:37 Yeah, that would be… yeah, and if you could shoot any comments, that would be really great.
**Robert Pająk (Splunk Inc.)** 20:43 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 20:45 Okay, very good. Thanks a lot.
**Robert Pająk (Splunk Inc.)** 20:48 Thanks, see you, have a nice day.
**Rüdiger Schulze (International Business Machines Corporation)** 20:49 Alright. James, see you next week. Bye.
**Jim Porell (Rocket Software, Inc.)** 20:51 Yeah, see you next week, Rudiger. Bye-bye.
