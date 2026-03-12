SIG: Semantic Convention SIG
Date: 2025-06-16
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/51r49fyS-mcCeNE5P-o2ktiDEtf2HLqEEeZkOrU9Pzpw2WROPURjnN4XHSgGAi9P.k6j7WqdCFNZOyEC1
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:03:24 Hey, folks, we'll get started soon here.
Alright So let's since we don't have Josh or Lyudmila. Let's skip the triage board and go to general topics.
This is pretty messaging semantic convention related.
So probably need Ladmila's. Input.
Let's go to Sam.
You split this off. Okay.
Sam 00:05:55 so this is a much smaller pi, you only have the sequel server content and yeah.
I, I guess we can merge this first, st because I don't feel any objection from the previous sick sick meeting.
Trask Stalnaker 00:06:22 So I think the one open question for this was still how it was going to be.
Oh, I see this is trace parent got it. This is not service.
Yeah, there's nothing about the SQL commenter, gotcha. Okay?
So this would be just a normal
Sam 00:06:53 Use the.
Trask Stalnaker 00:06:54 Propagator.
Sam 00:06:55 Yes, yeah.
I also renamed the context propagation to database context propagation. So to avoid confusion.
Trask Stalnaker 00:07:09 To avoid confusion with.
Sam 00:07:13 To let people think about it is something about W. 3 C. Headers.
Trask Stalnaker 00:07:24 But isn't it about that.
Sam 00:07:27 No, there's.
Trask Stalnaker 00:07:27 Part.
Sam 00:07:28 Because you only have the transparent and the way it propagates it doesn't treat the contacts information as the header. Right? You only propagate the value of that. It doesn't even pop populate the key because he has a well limited lens.
Trask Stalnaker 00:07:48 Oh, I see. So context, info doesn't put transparent anywhere. It's just literally the value of transparent for query, I see. Let's look at your example. Here is helpful.
Right? Right?
So is there value in trying to do, trace, date, propagate
Sam 00:08:43 Is, it only has the length of 128 Byte and trend state is well, the length is variable, right.
Trask Stalnaker 00:08:52 I see. Yes, yes, Gotcha.
and how does this does this get logged by like I'm wondering that the users how users see this on the database side.
Do you like enable something on the database side to capture sequel statements and their context info.
Sam 00:09:30 Yeah, so there is a type of query. We can just run against the database, and it's called query sample in SQL. Server. And so the query, simple result will contain this context with the binary value.
and we could leverage the SQL. Server receiver in the hotel collector to retrieve this value and pass it, the the and parse the trace id or spend id something like that.
Trask Stalnaker 00:10:23 And so for the way that you would implement this, for in like a database instrumentation.
Sam 00:10:33 Yes.
Trask Stalnaker 00:10:34 Would be before each query, you would call.
You would do this before each query that.
Gets called.
Sam 00:10:51 Yeah, so we already have a experiment implementation on Donnet to well to prove this can actually work.
Trask Stalnaker 00:11:09 Do you have? Can you add a link to the prototype.
Sam 00:11:14 Oh, okay, yeah, I can. I can, I can get the link later. I don't have the link.
Trask Stalnaker 00:11:32 Sure.
Sam 00:11:32 Right now.
Trask Stalnaker 00:11:33 Yeah, no worries, no worries. I'm just looking. If there's anything else.
Lyudmila!
I'm not sure if you cut this, if you have any concerns about this sort of narrow scoped?
No, I.
Liudmila Molkova 00:11:59 I don't have concerns about this one. Thank you, Sam, for for working on it. I'll take another look.
Trask Stalnaker 00:12:09 Cool.
All right.
Let's see, Josh, how to the topic. I saw that he was going to be here soonish.
So we're right on time.
Oh, but also we could go back here. Ledmilla, this is kind of a messaging related, so I was hoping to get your thoughts. I think the I think the concern here is basically with the linked spans.
That you don't get baggage propagated over linked spans.
Which seems both intentional and not intentional. I mean mainly intentional, because they're different traces and baggages scope to the trace. But I can also see why somebody would want baggage propagated.
But maybe it's just. I kind of remember there being some language about the link that you could still, parent if you had a consumer span that was Had a single parent, you would. Just. The link is required for consistency, but the parenting is optional.
so it's suspect. Maybe that is enough to address this use case.
You're muted.
Liudmila Molkova 00:14:14 Sorry. So the producer has no idea what consumer will do. So producer should propagate.
Okay, consumer.
Should extract.
But then there's a big question, okay, what if I'm what would I do with this baggage? There are many baggages, and if there is a batch, receive.
Trask Stalnaker 00:14:41 If there's multiple parents.
Liudmila Molkova 00:14:43 It's now, if there is multiple links, so is the question specific to the single case.
Trask Stalnaker 00:14:53 I didn't quite grasp, and I had asked if they could join today to kinda go through. But Let me reply with at least that portion, but because, they're working on updating the Java messaging instrumentation to the latest semantic conventions. So they might have missed that part about the parenting still being optional, that maybe we can add that and see if that's what they want.
Liudmila Molkova 00:15:35 It's just optional. It's also the default. The recommendation is further, remember, let me find the link, and I'll share it in the chat.
Okay.
Trask Stalnaker 00:16:02 We skipped over triage. But now that we've got more folks probably worth taking a look.
So okay, a lot awaiting Sig approval just to check if we've got okay, this one has one approval from the Sig.
Braydon Kains 00:16:55 This one. I think we can. We can leave. I actually have. I added something to the agenda to talk about this a little bit. Actually.
there's a lot of movement here in our group.
Trask Stalnaker 00:17:07 Cool. Thanks.
Just scrolling through quickly to see.
This probably approval was, yeah. This one is approval was a long time ago. Yes, resource quota metric. Looks like we've got a couple approvals waiting for.
Christos Markou 00:17:49 I think. It's that should be ready. I don't know if that would need an early base.
But yeah, we we recently discussed within the Kubernetes working group, that we should at least have 2 approvals from the Sig. And then we can forward Prs to the generic same kind of approvals for maintainers to review and merge if everything is fine.
So yeah, I will take care of this of this later to to move it.
Trask Stalnaker 00:18:22 Oh, okay, got it. Yeah. I hadn't thought about that. That. The you all have triage rights. You can move it.
A state awesome.
Lamila. Josh, is that kind of the general triage that we should follow like is this.
should we be going through this list and checking them or waiting for the Sigs to move, asking the Sigs to move things.
Josh Suereth 00:19:06 So.
Trask Stalnaker 00:19:06 Over.
Josh Suereth 00:19:06 We need to get this sorted out. But I actually think what I wanted to focus triage on was things that are like need, more approvals that have left sick status and blockers checking on status of blockers to make sure that, like, they are getting resolved, and people are aware of what's going on. But the idea is, we like, we have a lot of stuff in the in the hopper all the time. Let's make sure things are making it to merge right.
So the focus, I think, should be on the right hand side of the funnel and work our way to the left, and Sig should be him. If you think of it as a big funnel of Prs right so start on, start closest to submit and work your way backwards, and 6 should be doing their own triaging. Yeah.
Trask Stalnaker 00:19:48 Gotcha.
So we've got ready to be merged.
Looks like Chris fixed the merge conflict. So I'm just going to hit merge.
Let's open.
Alright, so needs more approvals generally means it's Sig approved. But waiting for a sem comp maintainer approval.
Josh Suereth 00:20:51 Yep.
Trask Stalnaker 00:20:57 Let's see.
You just moved that over. Very nice. Thank you.
Gen. AI.
Do you want? Oh, I see. There's just a couple follow up comments.
So does this need more approvals, or just.
Josh Suereth 00:21:29 I think it just needed comments followed up and just internal status. I think Michael might be passing this off to someone else in Google to to finish up the clean up the Pr, he's actually on a another different open telemetry related project now. So he didn't have time to finish this one up.
Trask Stalnaker 00:21:48 Should we move it to ready to be merged.
Josh Suereth 00:21:53 Well, it's not because you can't just click the resolve comments. So we need something that says, like author needs follow up or like merge conflicts or something. But yeah.
we don't have a a triage place for for things like this.
Trask Stalnaker 00:22:09 Okay, so leave it
Liudmila Molkova 00:22:13 We can probably add a comment. Oh, sorry! We can probably have a label for this, so at least when you visually scan.
But it. It will be hard to manage.
Trask Stalnaker 00:22:25 We don't see labels in this view.
Liudmila Molkova 00:22:28 You can filter.
Trask Stalnaker 00:22:32 Ha! Ha!
Liudmila Molkova 00:22:33 So like something that doesn't have a label or something.
Trask Stalnaker 00:22:36 Yeah.
and this one is very old, but it has approvals.
Last week, all right, all right.
Liudmila Molkova 00:23:07 Yeah, I'll I'll.
Josh Suereth 00:23:09 Wanted to merge, but it has conflicts, so I think it just needs to regenerate.
Liudmila Molkova 00:23:14 Okay, I'll resolve the conflicts. Thank you. I also wanted to do some research as a final step. Thanks.
Josh Suereth 00:23:21 Okay.
Trask Stalnaker 00:23:24 This one. Let's see, I think there's follow up. Okay, so this is on me to finish.
Follow up on check that.
Okay, this has not been followed up in a while.
Okay, so they're aware of it.
Josh Suereth 00:24:03 That one, if we have that like author needs to respond. Thing, I think Lydmilla's comments would be, would have been all of my comments on this when I went and reviewed it. So I think those need to get resolved, and then that one's good.
Trask Stalnaker 00:24:17 Okay.
just taking a note.
some kind of kubernetes. Node condition.
Okay? Oh, yes. And you all said you wanted to.
You all wanted.
Oh, no! For system. You wanted to approval. Sig approvals.
Christos Markou 00:24:51 Yeah for kubernetes, actually for kubernetes the one I was mentioning is for kubernetes, sig
Trask Stalnaker 00:24:57 Oh, okay.
Christos Markou 00:24:58 So we need another record. Yeah.
Trask Stalnaker 00:25:00 Got it. Okay? So.
Josh Suereth 00:25:02 So that goes back to sake approval. Then.
Trask Stalnaker 00:25:12 This one has been open for.
Josh Suereth 00:25:16 The latest status is at the bottom. Yeah, 2 weeks ago was basically overwhelmed. Need to delay. Would it be possible to ask for a little more time. I I think the answer is, yes, take as much time as you need, but maybe we should move to. I don't think you can move to draft or anything like that the signal that this is kind of blocked on that but given, it's an area security. Maybe we move.
Yeah, I don't know.
Alexandra Konrad @Elastic Security 00:25:43 I can. I can ping her to ask about like a proper time frame, I mean, if it's like a week or a month.
No, so we can have more.
Trask Stalnaker 00:25:55 Alexandra, do you want to? Does your do you? Wanna dismiss? Maybe dismiss your approval.
and we can move it back to awaiting cigar.
Alexandra Konrad @Elastic Security 00:26:09 I'm waiting. Okay, yeah, let's do this.
Trask Stalnaker 00:26:17 Do you want me to? I can do that.
New York.
I don't know if I'm no ways forget, does that? I don't think that. Oh, I guess it does see that clears this green check. But it actually.
I think if we look at there was another place I thought we could see reviews reviewed.
Liudmila Molkova 00:26:47 I don't think it cleans the the rejection that so you can dismiss the approval, but you cannot dismiss the rejection.
Trask Stalnaker 00:27:01 The Re.
Okay, but where do I dismiss?
There's a lot of times there's a bar here that will show me the recurrent reviews.
Liudmila Molkova 00:27:16 If there are any right, and there aren't.
Trask Stalnaker 00:27:19 Oh, okay. And there are now, okay. So I guess I did.
Alexandra Konrad @Elastic Security 00:27:23 Just yeah, you can dismiss my
Trask Stalnaker 00:27:29 Got it.
Thank you, and awaiting sick approval.
You would think I would have figured that out by now.
Move key name. Aya. This is, I need to fix merge conflict.
This has Sig approval and approval. This probably is, oh, that just recently. Okay, so this one is ready to merge.
Liudmila Molkova 00:28:14 Bye.
Trask Stalnaker 00:28:16 We will just hit merge target. CPU, sorry. I know we're taking longer, but we didn't really have too much on the agenda unless there's more things. Let's see. Oh, Hi, josh one, okay, we do have a lot more things. Okay, so let's let's shortcut out of triage.
And do you want me to do you want to share for the entity modeling.
Josh Suereth 00:28:55 Sure. Give me a sec to pull it up.
Oh, you're gonna share it right? Okay. Good.
Trask Stalnaker 00:29:04 Anyway.
Josh Suereth 00:29:05 Yeah. So if you so we have an empty modeling guide. If you, if you folks go over to to things changed and maybe do. The rendered view of this.
Trask Stalnaker 00:29:25 Alright! What.
Josh Suereth 00:29:26 In the Markdown view, is there?
Bind usually has a button. You can do it in Markdown stuff. Oh, oh, you're you're viewing the you're viewing a yaml file, not the resources in M. 2.
Trask Stalnaker 00:29:39 Oh yes, yes.
Josh Suereth 00:29:40 The markdown file. Yeah, the you were doing the the change log. Yeah.
So here's the modeling guide, and this covers resources and entities. So there's a few things I want to call out for potential discussion just to do it rather quickly. Basically, there's a few important components here to the guide to understand one is, you should not define an entity in open telemetry unless you're going to associate a signal with it, meaning it has a metric. It has a log, or it has an event for which it is the source. That is the 1st thing we're defining in this guide.
the second bit. Here is the notion that you can have multiple entities that mean the same thing. So, for example, we have a Kate's container, and we have a container, and they may be the same thing. We have a Kate's node, and we have a host, and they may be the same thing.
They may not right.
And so we have. This notion of an is a relationship that is kind of loosely defined in this guide to help you understand what that means, for now, if you see the same 2 entities in a resource, you can assume that they are somehow related in that sense. But it doesn't guarantee it's an is a relationship. It just allows you to put them in the same resource. So I can have my Kate's node annotations and my host annotations in the same resource for a signal if they are both of those things.
Okay, so that's like the 2 high level points that matter. Now, there's this weird thing where we have this, when to define a new entity in the fact. Can you click on that link here?
We have 2 scenarios where we think you want to describe new entities.
The one is basically, I'm generating a new signal, and I need a source for where it came from, and I don't have it the future one which I can remove here. But we have it listed because it's part of phase 2 of entities, and we call it out as future meaning. We don't want you to do that yet in Semcov is basically I need to understand the relationships between the things that generate data.
Okay.
I can remove that from here if it's confusing people. But that's fine. The next thing is, if you look at when to define is a relationship versus extending descriptive attributes. It's right below this.
This is the other big question.
There is a use case that we couldn't agree was not needed.
But we couldn't ever define a good use case for it.
So scroll down to the when to define as a Trask. Yeah. The use case is this idea of like. From what we understand the system, semcomp group will never, ever create windows, dot process, entity or process dot windows. They will only use process and attach their data to it is the current plan.
So we had this thing of, okay. Well, what if I wanted to define a subset of things. That process has to denote a windows process. But when I report it in Otlp I will call this thing a process right? So the data in Otlp says process, but I know it's a windows process, and I codegen for windows separately than I. Code Gen. For Linux. Well, we have this notion of extending right, or which is, which is what semcomf calls it.
But that's kind of a bad name, because it's not really inheritance. But basically, you would say, I have a group that I call windows process. It reports itself as a process, but it has customized set of attributes that you know. You get on windows instead of a generic set of attributes which a with conditional requirements. Right? That's the idea behind this.
But it has been confusing everyone who read this, and, to be frank, it confused the Entity Sig for a solid 6 months, as we discussed whether or not this was a real use case, so I think the confusion is real.
This was what we came out as the entity sake explaining.
And I wanted to run it by this group of basically.
I can cut this section I like. We don't know if this is a legit use case yet we think it could be for this windows process thing, but it's a stretch.
Is this something we want to include? Or should I cut it? That's like half of the questions on this guide are about that. So, Ludmila. You did approve the guide with it in, but you also raised the best questions about this section, so I am very curious on your opinion, but I wanted to open up for broad discussion.
Braydon Kains 00:34:21 I think the the process and windows process thing might have been might have been my fault where I thought there was a use case, and then there wasn't. But the question still kind of came up. I think probably the container in Kate's container is a more normal example of this than the process and windows process thing, just because I think in in the end, like at first, st I was, I was concerned that possibly defining like identifying a process on windows might have something different.
But I think the identification that we're running with for process works pretty much on all target platforms. And so we're not worried about identifying. It's just about like descriptive attributes, and maybe on windows. There might be something. If if we do need like actual proof of this. I can take some time and and research like that exact case. If that would help.
Josh Suereth 00:35:22 So from a tooling perspective, you literally can't extend descriptive attributes today. In some comp, we would actually have to do work in weaver to make this allowed.
Because of how we do namespacing. But that's that's a different story.
but yeah, basically, if you wanted to create a group that denotes a windows process. But in Otlp reports as the process entity.
That's the thing we need to know.
Braydon Kains 00:35:50 Yeah, right? That would. That would be like, okay, this section makes sense.
Josh Suereth 00:35:54 We need this, you know, and we're going to expand weaver to support that. And we'd update some comp to allow it. And that sort of thing right?
Liudmila Molkova 00:36:03 Can can we talk about the the how would we do this? So like you would say that the name of this thing is windows dot process.
but you would say it's also a process.
Josh Suereth 00:36:18 The group. Id would be window step process for Cogen.
but the name would be process.
Liudmila Molkova 00:36:27 I see, so Otlp will have no idea that it's a windows process.
Josh Suereth 00:36:32 Yep, we just use it basically to do Cogen. So you get a windows specific code gen, with specific attributes.
Liudmila Molkova 00:36:40 That's the same problem we have from metrics like the Kafka flavor of some messaging metric, is the the would have the same problem.
Josh Suereth 00:36:49 Exactly. Yep, it's it's the same kind of a thing is like, you know, I wanna have Kafka version of general messaging metrics. And I might, you know, take some opt in things, and just not even allow them. I might take some recommended things and make them required for Kafka.
Cool.
Liudmila Molkova 00:37:09 Do we need to define a relationship? Then, like what significance does it have.
Josh Suereth 00:37:21 The yeah, I mean for for entities. We basically.
the whole is a thing confused the crap out of everyone.
And we wanted to define what it is and what it isn't.
And this is us defining what it should not get used for right, because when you define a new entity for real. You get a physical name which shows up in Otlp.
And so then the question was, Is there a use case where you don't want a new physical name. But you want to add, like additional descriptive attributes or something, and we think that answers. Possibly we didn't want to close the door on it.
Liudmila Molkova 00:38:09 And I would say that that the distinction is useful.
The problem is real, and it's more than entities. But maybe we'll find a more clear people, friendly, human, friendly way to describe.
Not right now, maybe.
Josh Suereth 00:38:29 I don't know if you saw my big bug in weaver on the path forward for extending I wanna I wanna actually call this either enrichment or refinement.
And I want to change from, extend to refine as a as a keyword, and just to make it clear what the heck it's doing right.
because I think the extend keyword right now is confusing.
and the fact that it can only you can only extend within attribute groups, and you can only extend from an attribute group, or you get an error is kind of weird, right in practice, because if you extend from a different signal type, and you kept the name the same. Sorry? Then then all hell breaks loose.
Trask Stalnaker 00:39:19 So I was trying to think.
I mean the what Linilla said made the most sense to me of that. It's just like metric.
How we're doing vendor specific metrics and even spans.
And we haven't really had problem.
We haven't tried to define it formally, though.
and so, which makes me wonder how important that is to define formally versus What do we have? Database.
Liudmila Molkova 00:40:03 Can you open cosmos? One. It shows the the ugliness of what we do today.
Trask Stalnaker 00:40:12 Oh, the the massive copy!
Liudmila Molkova 00:40:15 Worse.
So that if you scroll down to metrics.
yeah, this one. So we're saying, Okay, here is the metric. It follows the general convention, but you know it has some attributes, and this is a section for another metric that you should look for, to understand which attributes are actually reported.
Trask Stalnaker 00:40:41 I see I thought we were re-rendering the whole attribute set for all of them.
Liudmila Molkova 00:40:51 We could have, but then it would be misleading, because we have no means to add attributes to it.
Trask Stalnaker 00:41:00 Right because of metrics. Yes, yes, yes.
Josh Suereth 00:41:05 So I'm actually happy to start pushing on this general problem because we also ran into it.
If you want to look at the the link I posted in chat or in the in the docs. There's a there's a general issue in Weaver around the difference between Id and group which is hugely problematic.
And what extends mean. So I actually have a general proposal going forward, which is Id is always kind of what you're looking at here, where I could have an Id that represents the Cosmo dB. Version of a metric versus the raw version of a metric right?
And then we have this notion of refinement where Cosmo dB. Refines the metric semantic conventions. Where there are things it cannot change right? But there are things it can do that we allow in refinement, so that you can have a rendering specific to Cosmo that matches semantic conventions, and we have policies that check it right? So there's the source, and then the refinement and group name should always be like the source name.
So the metric has a name that it gets used, regardless of how many places it shows up. The Id denotes the refinement, you know. Identifier. So is it the source, the original source? Is it the Cosmo dB version? Is it the Mysql dB. Version, you know, whatever that would be the Id. And then refinement is a process that we can track and use to identify things actually already used this to clean up a bunch of code in Weaver. You can see a few Prs associated with it.
There's implications here on what this means in practice in this path forward task that will make no sense to anyone not deep into weaver so like don't feel like you have to dive into that. But anyway.
When it comes back to this, I think what I'm hearing is this notion of is a versus extending descriptive attributes is a general purpose problem we should solve in Semcov, and I can make progress on it. I might leave it in the Entity Modeling Guide, for now, and we can clarify the the language as we improve Semcov. Does that sound reasonable to everybody?
Liudmila Molkova 00:43:28 I approved. It sounds good to me if if nobody else objects.
Josh Suereth 00:43:35 That's it.
Liudmila Molkova 00:43:35 Let's go with it.
Josh Suereth 00:43:37 Okay.
Trask Stalnaker 00:43:38 No objection.
Josh Suereth 00:43:39 Yeah. So I would appreciate everybody taking a look at this and and offering advice on things that are worded oddly just because, you know, you work in a in a domain for a while. And you start using terms that you realize people aren't aware of, or you're not using like loose language, and I want to fix that up so. Yep cool.
I have another one, which is, please review this this actually I had a couple of prs in the queue, and some of them are too big, so I split one in half. This is just the policies and requirements to stabilize entities, to make sure they have identifying descriptive roles on attributes. That is all this does, but it retroactively adds identifying descriptive for the 2 stable entities we have today, which are service and telemetry. SDK, nice?
Yep, okay, that's it.
Trask Stalnaker 00:44:47 Brayden.
Braydon Kains 00:44:51 Yes, we going back to the CPU utilization thing. We've been talking about this a lot in the group, and how you want to handle it. And you know, in in general we are leaning towards not recommending people ever use CPU utilization for a lot of reasons. But we don't want to drop the metric out of Semcon because people seem to expect its presence, and maybe guiding people to use the raw metric and do a bunch of math on it in your dashboards. Maybe they don't like that, and they just really want a utilization metric. But there is a real usability problem with utilization metric. I'm working on a document that explains all this better.
But the the root of the problem is that the CPU utilization is a utilization metric over time.
So when that metric makes it to a back end, this is assuming a collector or something else has already done the utilization calculation over some period of time, that period of time. If you're just calculating it in a dashboard, you've chosen that period of time in your definition of your dashboard, or your definition of your query but when utilization is collected, the point of the period of time used to calculate was chosen at collection time, meaning that the back end has no way to know this. And so we're looking at a way of encoding this information in a metric. Somehow.
in the Prometheus ecosystem. It's quite common to just suffix suffix the metric with the period of time.
but we want a more otlp-esque solution, and the best solution we could think of was for the metrics unit to be like the period of time, so like like CPU, 10 seconds like the the unit, would somehow encode the period of time that was used to calculate that metric.
But there isn't a way right now in semcomf to define a dynamic unit, and I don't really know if there's any other metrics that would surely we have some other utilization over time metric somewhere that would make use of this so like, I don't think this is going to be a unique, isolated case for us, but I don't think this has come up yet. At least I haven't seen anything.
What do people think? Should this be like? Is this even the right direction? This might be an Xy problem. Is this even the right direction for this.
Should the this sort of support be added to Weaver to allow us to define it in Semconv?
Or should we just not have utilization metrics at all in conventions, I guess, is technically another possibility. Right like them, existing as they are right now, is probably not not great. But either we solve this problem of encoding the duration in the metric data somehow.
or we don't have utilization metrics.
Josh Suereth 00:48:08 I mean, the the problem is the it's almost the metric data model.
Right?
I.
Braydon Kains 00:48:17 I think this does represent some kind of problem with the metric data model.
Josh Suereth 00:48:22 So so these CPU utilizations are they gauges.
Braydon Kains 00:48:26 They are gauges. Yes.
Josh Suereth 00:48:28 And they're over a time window.
Braydon Kains 00:48:31 The the collection has to occur over a time window, so like the way that this metric works in the collector right now is you give it the time window that you want.
Josh Suereth 00:48:41 Sample, but the numbers that you collect are your gauge sampling something that was a time windowed value right?
Braydon Kains 00:48:50 Right? So like the, it's like, the percentage utilization calculated over the last 20 seconds is essentially what it is.
Josh Suereth 00:49:00 And the denominators change. So the problem is when we design the metric data model, the denominator is supposed to be in the point.
So that kind of a calculation. The gate should have a start and stop timestamp. That says, you know, the 20 min window is the start and the stop. Or you would be using actually, technically, a up down counter, and the start and stop would be the the thing.
What we have, though, is because of the way CPU system metrics are. And the way people generally observe that would be insane for us to do in practice. It would break many metric systems. It'd be really, really weird and odd. And we don't have a way to represent how CPU works traditionally for that use case, because we just assumed we'd make a metric that told you the sampling rate of the gauge and everything would be gravy. But you want to use the same metric for multiple different sampling rates.
Braydon Kains 00:49:48 Basically like, like for a configurable sampling rate. Essentially.
Josh Suereth 00:49:51 No, I know the the sampling rate that I'm talking about is not your sampling rate the CPU sampling rate like you're you're looking at the the number you get that that like, you know how much CPU percentage was used over 20 seconds. Do you have control over that in your instrumentation? Or is that something you just accept? Whatever the hell the OS does.
Braydon Kains 00:50:10 This is like we, we calculate it so what the the OS provides us, a counter of seconds spent in different States, and so add a 20 second like, let's say it's 20 seconds. At the 20 second boundary we look at the delta of those values over the last 20 seconds and do the this utilization math on it so.
Josh Suereth 00:50:31 Grab the data. You know how many seconds in the past it was.
Braydon Kains 00:50:35 We, we would know like so like, if if you made it 20 seconds, you'd get a new gauge every 20 seconds received. The problem is, if you want to, then sample that like, let's say you're presenting a graph over a longer period of time. You can't just raw sample these gauges because the calculation of 20 seconds, the calculation of it happening over the last 20 seconds doesn't work. If the new window that you're sampling the values at doesn't match up.
So is that like.
Josh Suereth 00:51:14 So the problem here is there's 2 aggregation windows that we're talking about, right? We're talking about the collector aggregating away number of sampled CPU seconds right to make a percent value or something that we think is easier to work with right. But then there's the second sampling window, which is how often you report the gauge from the collector, because you can't just have it sitting there churning on your CPU every 20 seconds. You're going to take down a bunch of systems that's like way too expensive for most people.
Right? Right?
Braydon Kains 00:51:44 So the and then the then the problem ends up being if we don't. But if we don't report it at the exact same frequency as the sampling rate, then that utilization is not actually like the correct number.
Josh Suereth 00:52:00 I see. So are you planning to have the collector run every 20 seconds? Then, to keep this accurate.
Braydon Kains 00:52:05 That is what it does right now. It scrapes every 20, every whatever whatever time window you give it, it's it scrapes that and reports that every whenever and 20 seconds is is pretty aggressive like that probably wasn't the right number for me to use as an example. But that is the idea.
Josh Suereth 00:52:25 Yeah.
Braydon Kains 00:52:25 Alternative being we just, we tell people to use CPU time.
You keep on getting your counter, and you just do your do do this math in the query, this math is doable within the query, within a query.
And that's what we're going. We already know. That's what we're going to recommend people do. We're just trying to think of. If we want to keep the utilization metric around in our semcom, we need a way to represent this. We need. We need a way to represent the sample rate that it was calculated at. Because if you want to down sample later, or is that down sample the right word like if you want to sample it at a longer time window than what you originally calculated it at. You need to do a moving average over a window that lines up with your original calculation.
Josh Suereth 00:53:11 You're building a metrics. Database in the collector is what you're doing.
Braydon Kains 00:53:16 Kind of we, I mean, we don't really want to, but kind of.
Josh Suereth 00:53:21 Right. That's where I think the the reality of what you should do here is just give people a less accurate data and and document. This, as such, basically like this metric is not recommended. Here are the caveats, and how it's how it's calculated and and generated.
which is why we don't recommend it. But if this is the thing that you need, because that's what you're using today, we will give you that same behavior. We shouldn't diverge from the ecosystem with how they do utilization metrics like, I think there's a reason we want to move to usage because it's better to calculate on the back end and get more accurate data, and you can use generally anytime. You can get a counter instead of a gauge. You should always do that because you will get better metrics, better alerts, more consistent data. That's just a foundational properties of metrics thing.
But the reality is like knowing what I know about these systems. I think you're in a hard spot. I don't think you can give people a good model on utilization with the way you're getting data today, I think you have to give them what they get today and put all the caveats around. Why, it's bad.
That would be my recommendation crystals. Your your hand was up. I don't know if you have something you want to add.
Christos Markou 00:54:35 Yeah, yeah, essentially, the question I posted here in the chat for kubernetes, though we get the CPU usage straight from the cube. Let's Api which means that the let's say the delta is calculated against them specific time. Window which is set through kubernetes. So this specific use case is not the same as the plain system. CPU utilization calculation that only relies on the collector scraping period. Let's say so it's a slightly different if that helps.
But in that case I guess it's fine. If we define such a metric, because we can just reference directly from where we get it. So essentially represent pass through what the technology specific Api provides.
Braydon Kains 00:55:33 Yeah, the the way I'm leaning on that sorry, Trask, I'll let you. I just wanna make this comment real quick the the way I'm leaning on that is essentially just to keep it the way like, say, like, we're passing through what we're getting from like when we do have something like that that we can. Just we get it from another system that is doing the calculation. I think it's fine to rely on them. And basically the only caveat like which in which is going to be in the document that I'm working on is talking about just like the sort of the aliasing problem like, if you sample it at the wrong at different times. The graph of how the thing has changed can change, based on the timing of your sampling.
but, like there isn't really a way to avoid that. It's probably better for us to just rely on the CPU usage that comes from Kubelet and note. The caveat most likely is going to be the the way forward.
Trasco's first, st I think.
Trask Stalnaker 00:56:27 To 1st to make sure I understand.
So the window, the window that you're aggregating over, or, you know, taking the difference over. Does. It? Seems like that needs to be a multiple of the collection on the metric collection interval.
Braydon Kains 00:56:49 Yeah, so, if.
Trask Stalnaker 00:56:50 Accurate.
Braydon Kains 00:56:51 If my, the math I've been doing on this is correct. The only way to get this correct, the correct CPU utilization of like directly from a utilization metric in a dashboard that's like sampling the period over a longer period of time than what was originally calculated is to do a move like a moving average calculation, but the window has to line up with the same sample rate, so like if it was calculated at a 20 second rate, you need to do some multiple of 20 seconds for your for your window.
Trask Stalnaker 00:57:27 Okay? So if the collection, if the general metric collection interval was 20 seconds.
In that case.
Braydon Kains 00:57:36 Yeah. So if the if the general metric calculation, the utilization was calculated at 20 seconds, and you want to, let's say, like sample this like every hour kind of thing for your for your long term graph of utilization. You would need to like pick a time window that lines up as a multiple of the original collection window.
Trask Stalnaker 00:57:54 See? So that that's the use case, that is, targeting is fairly long. Windows compared to the The collection interval.
Braydon Kains 00:58:07 Yeah, that was, that was the original case that was brought up in the original issue where we've been discussing a lot of this stuff, which is, you know, if if you just like raw, sample the points and you don't do a cal like a an average calculation, then like that percent CPU utilization that was reported as like this is the utilization over the last 20 seconds. It is not the same as the utilization over the last hour the like. The the number is actually giving an incorrect sense of what the utilization is at that point in time, because you're sampling at a different rate than the original calculation happened.
I'm having a lot. I'm having trouble explaining this in words. This is.
Trask Stalnaker 00:58:46 No, no, I got it. I got it. Yeah, we're running out of time. And I have more comments about this topic. Maybe we can chat more next week. The the piece that I'm interested specifically in is usability from. I wasn't so worried about this gauge piece. That is the long tail. But more what I was. I'm worried about user with the raw, underlying data that users have to be aware of. CPU State.
I feel like I would like to have the same metric. But not have CPU state right? Just have the metric be. It's a counter, but it's a counter aggregating over all of the essentially CPU active CPU states.
Braydon Kains 00:59:45 Right, that's another. That's been another point of contention on this on this topic, too. It's kind of a 2 prompt thing
Trask Stalnaker 00:59:52 That's the one that I have more opinions or more interest in.
Braydon Kains 00:59:56 Yeah, I I'm definitely interested in talking more about that. But we are out of time here. So.
Josh Suereth 01:00:02 So real real quick thought for the group. Think about if you have to report that second interval is reporting that as a metric.
That. Yeah. Report the window as a separate time series. So you you can report the CPU utilization. And then the window of aggregate CPU utilization window or aggregation window as a separate thing, so that you know that if the point comes every hour, but the window doesn't cover the hour, I can see that visually right? I can do calculations downstream. I I still, personally, I think that utilization, the way you're calculating the way it's reported. It's a foot gun, and we should, we should very seriously be dissuading people away from it.
I mean. Look! Look the keys. Api doesn't have it right. They they tell you the window, and they give you usage raw. They don't give you utilization right.
Braydon Kains 01:00:53 Yeah. And I think we're just we're defining that utilization against like against, like the configured limits. It's it's a slightly different use case, too.
Josh Suereth 01:01:01 Yeah, fair fair. But but again, like.
do the best you can, but I think dissuade people against the foot guns would be my recommendation, and give them all the tools that they need to work around them.
Braydon Kains 01:01:17 Yeah, makes sense.
Trask Stalnaker 01:01:20 Thanks, all.
Braydon Kains 01:01:21 Thanks. Everyone.
Trask Stalnaker 01:01:22 I.
