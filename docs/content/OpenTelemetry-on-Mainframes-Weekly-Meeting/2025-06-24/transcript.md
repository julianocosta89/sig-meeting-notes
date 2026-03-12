SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2025-06-24
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/bqGRFsmSzn8FaBXGvOm8EsyOJWTehICYfnwrYyuCwH4SjJuQAVxhuG3zTyilItXZ.dgqGB_7_pLgxPDJl
============================================================

## Zoom Recording Transcript

**Morgan McLean** 00:36 Hello!
**Greg Shriver** 00:40 Hello! Hello!
**Ruediger Schulze (IBM)** 00:41 Hi, Craig. Hi, Morgan.
Okay, probably a small one today.
Let me maybe share my screen.
Where's the share button? Here's the share button.
Okay? 1st of all, I got a question.
And the question is, can we move this meeting by one day to Wednesdays? At the same time?
Reason is family reasons, because it's late here in Germany and moving forward. There's a conflict on Tuesdays.
**Morgan McLean** 01:25 Works for me.
**Greg Shriver** 01:27 Works for me.
**Ruediger Schulze (IBM)** 01:29 Then, you know, let's move forward with it. I think, Morgan, or should we ask, should we? Should we ask on the slack channel.
**Morgan McLean** 01:38 Put, ask on a slack channel, give people a bit of time to respond. And then, when, yeah.
I can change the calendar event and I can change Github.
**Ruediger Schulze (IBM)** 01:45 Right? Yeah, okay, let's let's do that.
Okay, good. So.
**Greg Shriver** 01:58 Can. Can we just ask a regular old question on slack? Or does it have to be one of those fancy polls?
Regular questions? Probably. Fine. Okay.
**Ruediger Schulze (IBM)** 02:07 So alright. Well, then, I'll take the action item to do that.
Thanks, Greg. Okay, good. The next thing is. So. So I came back to the transaction processing system, and I was about to to rebase that and answer to the question, and we got a new question, in which is an interesting one.
That's why I want to discuss this with you. So there is.
I think this is, you know, coming a few times.
Could we harmonize the updates that we are bringing in with Tps with my workflows, Pr, which seeks to achieve this in a generic way, and the workflow Pr, I put it into the into the notes. Here, this is this one.
So and if you look there there is in on this pr, there's a proposal. It's actually quite a, you know, going across various areas of the semantic conventions right now, I only have here what is being newly introduced.
But obviously it brings a couple of new attributes.
My impression is this is still very much driven from.
you know, devops pipelines, for instance, when you, when you deploy have a workflow which is deploying all artifacts across different environments, for instance.
But there are some similarities. Obviously. But also, I mean.
so far, I have seen transactions being completely different than workflows.
And that's a little bit the challenge that I have with trying to align. You know these both concepts.
and and hence was wondering, you know.
1st of all, what do you think? We can also put this on it for a discussion on the on the slack channel?
But I would be interested on your on your perspective, on that.
**Morgan McLean** 04:11 And these are transactions. These are transactions and workflows in the context of like. These are already nouns. These are things already in mainframe.
**Ruediger Schulze (IBM)** 04:20 Yeah. So if if you think what what we you know, we look at these, this is this is transactions which okay, they operate. You know, also on tasks. If you think about it, this workflow concept also has this this concept of of tasks. There is some similarities.
But I think we probably at least from a mainframe perspective, we would not have.
I think there's no use of the term workflow in the context of transactions.
This I never heard that, I think.
And it's let's see.
**Greg Shriver** 05:03 Well, yeah, I don't. I I'm not exactly sure what they're referring to in terms of workflows, but I could see I could see where, where a given Cics transaction could be a part of a larger workflow.
But I don't know if that's the same. If that workflow is, if that's in the same context as what but the suggest, what the person suggested.
**Ruediger Schulze (IBM)** 05:30 Right.
**Greg Shriver** 05:31 Yeah. And and thank you, Rudiga, for putting the the the the link for the workflow proposal in the notes, because when I saw that come across. I wasn't sure what they meant by workflow. I saw the request to try and harmonize this with workflow, but I didn't know what workflow meant.
**Morgan McLean** 05:53 Text.
**Greg Shriver** 05:55 So I I for me. Personally, I probably need to do a little bit of homework to better understand what they mean by workflow.
**Morgan McLean** 06:02 Just to clarify like again. I'm still a bit confused, like Workflow. Here is an hotel concept.
**Ruediger Schulze (IBM)** 06:09 So you are about to introduce this. So.
**Morgan McLean** 06:12 Oh, it's new. Okay. I was gonna say, because I'm not.
**Ruediger Schulze (IBM)** 06:14 Yes, yes, let me let me go back to the pull. Request that.
**Morgan McLean** 06:20 Sure. Yeah.
**Ruediger Schulze (IBM)** 06:22 So the the workflow pull request that came in. It's it's pretty new, so it's a couple of days old.
But what what it suggests is.
And and you know, I to to come just to mention this, to have a final view on this. I mean, this one is in draft state. We definitely would have to go to the semantic sick meeting.
**Morgan McLean** 06:48 We think this is going to get approved. Just a question.
**Ruediger Schulze (IBM)** 06:50 We? I mean.
we need to look at this. Right? Yeah, we need to. We need we need to go to the Semantics Convention, sick meeting to to understand what their position on this is. And then I think the ask here is, can we can we kind of like harmonize? Can we can. We co-create on this.
you know, looking at transactions. And and this workflow concept, I think that's the point here.
Now, when we look at this worst is deriving from it's very much based on on Cicd pipeline concepts.
**Greg Shriver** 07:25 Hmm.
**Ruediger Schulze (IBM)** 07:25 But also function as a service deployments.
So it comes from a completely different angle of technology.
And maybe it touches on some concepts which you have in like, I said in a transaction on the mainframe. You have tasks right? Kind of like metal, but you have unit of work.
So I think the 1st step is here to, you know. Let's take a broader perspective on that. And then we need to have a discussion.
and potentially, you know, join the conversation on the semantic convention sync meeting to you know. Get to a final point of view on on how to handle this. But I think it would be good if if you know you could take a read on this, and maybe also take a point of view of what you think is the best way forward here, or how should.
**Morgan McLean** 08:27 Should match with the stuff we're doing for mainframes. Yeah.
**Ruediger Schulze (IBM)** 08:29 Yeah, right?
If you look at. You know, this, this goes quite across. So it changes quite some areas from from Cicd Kubernetes perspective deprecates couple of things.
and then introduces, you know, to your question. It introduces this new concept of workflow to the semantic conventions.
Right?
**Joe Korchmar** 09:06 Hey, Rudi? It's Joe Korchwara!
How are you?
**Ruediger Schulze (IBM)** 09:09 Alright, good! Good! Hi, Joe!
**Joe Korchmar** 09:11 Hey? So you know, I'm thinking about what you're saying here, and I'm wondering what they mean by con workflow, too. I do.
You'd almost have to talk to them to find out what they mean about workflow, because workflow could be a sequence of events in order right and flown from point A to Point Z, and hitting all the steps in between in a certain order or in different orders. Right?
the the we had, and we proposed long time ago to try to get transaction groups which would be able to do the sequential groupings of units of work that somebody could implement into a business workflow, right? So depending on where they're coming from, a business perspective of what they mean by workflow or a unique flow through a system. I don't know what they're trying to do here and what they're proposing. It looks like it's under the A. K. 8. So that's Kubernetes type workflow.
I don't see where it spans across Gcp from a global perspective of workflow. So I think I'm just as confused as Greg.
**Ruediger Schulze (IBM)** 10:27 Right. I I think it tries to to kind of like generalize on this concept of sometimes you have job execution like you're on Gcp, right?
Right?
And it it it all deprecates or suggests to deprecate those type of attributes specific, you know, namespace specific attributes in favor of the workflow concept which is a good thing. But you know the challenge is to it still needs to fit into the concept and needs to be understandable for for consumer.
**Joe Korchmar** 11:04 So when I went out and I did research. And I suggested, you know, years ago, to elastic, that they implement workflow on top of the open telemetry model. Right? The data model. Because then you could bring in concepts like, Ibm business process server or other. Yeah, the old mq.
Si, well, you know the old workflow type concepts, and it could be applied and abstracted out to where you can actually hook it to anything in your data model.
So they're embedding it deep inside.
So they must have a specific reason on why they're doing this instead of abstracting workflow out and saying you could apply it to any way. Just hook a point A to Point B, and it could be any part of the open telemetry ecosystem.
Maybe I'm going to abstract with it, but.
**Ruediger Schulze (IBM)** 12:04 Let me put a question on the to. I think it's Tom.
Let me put a question to his comments, and then maybe suggest we we meet. I can join the sick meeting next week, the semantic convention sick meeting. So maybe we have a chance to to have a discussion there.
**Joe Korchmar** 12:23 Because I mean, even if they're doing an implementation that we could find useful anywhere else in open telemetry, that that can be abstracted out and it could be applied, implement their use case and pick up any other workflow type. Use case to say, Hey, I got a group of these transactions or tasks that I need to accomplish. And here's the sequence of needs. And here's the data model that I can use to embed workflow into open telemetry. I don't know.
I'm just thinking out loud.
**Ruediger Schulze (IBM)** 12:56 Yeah.
**Joe Korchmar** 12:58 Knowing that I know the mainframe from years ago, right? But they're strictly coming at it from a mainframe space.
But in the K 8 environment. So I'm a little confused.
**Ruediger Schulze (IBM)** 13:14 Yeah, okay, let me take an action.
and try to follow up on this. And maybe if you could read through the, you know proposal as well, and then we can have a discussion next week.
Just wanna also maybe catch up on a couple of other things.
so gse uk tech exchange are coming up.
Greg, I will contact Aaron, or if you see Aaron have a chat with him, I would plan similar like we had it on the virtual Gse Uk joint session, where we talk about the progress of the sick as a as a presentation.
**Greg Shriver** 13:56 Okay.
**Ruediger Schulze (IBM)** 13:57 And then a couple of other things looking here at, you know, as we are approaching the end of sec. 1st quarter, you know what to do in the second quarter.
We still have a to do to publish this survey for the block about the survey. I will put out a draft beginning of of July. Would be good if you could. It should be there by next week. If you could also have a look at this, and if there is, you know anything you want to add, or ingest.
please feel free to to do so.
and then I think we want to continue with systematic conventions for for virtualization also in the context of entities. As we discussed. I think I you know, I updated you on the last meeting that I was on on the entity sick. I think there was one last week when I wasn't available, so but we had a couple of questions also still around synchronity. Or, you know, time aspects of when these entities would have to be reported or recorded.
And then, I mean, a relationship is still being in development or to be defined. But I think we also would like to understand of then, you know, if you can have relationships between entities which have been reported at t 1 and then, other entities being reported at point in time. T. 2. Of how that comes out from a consumption perspective.
I need to follow up internally about chit up actions we discussed about that, I think, 2 or 3 weeks ago. There's a new way of how you can acquire these these chit up action runners. Actually, it should be saying, chit up action runners here.
self hosted, chit up action runners. There's this supposed to be a new way of bringing them, you know, getting them from from Ibm. So need to follow up on this. And then I think we have a couple of use cases where we would want to make use of this telemetry collector, as we said. Also c plus plus SDK.
Here also the shout out again.
If you somehow work with students who have an interest in getting on the mainframe and working on observability.
there's actually opportunity to to get, you know, work work on those topics. Right? I'm I I'm not exactly sure yet. I maybe there might be an initiative on our end again to get a student to look at some of these aspects, let's say, like this.
and then We also started to discuss around the cobol SDK, if you remember the survey that was actually one of the bigger points.
**Morgan McLean** 17:00 I do remember.
**Ruediger Schulze (IBM)** 17:01 And and it would be of interest if we could start a kind of like exchanging design ideas.
I'm not a cobalt person. Not at all but I you know, from discussions that I had with with a couple of cobalt Smes.
There seem to be different approaches in order to make this possible also, maybe relying rather on integration with with more common sdks.
maybe c plus plus even if this, maybe there's a way to do that.
And I think this is something we need, you know, start to maybe work out a proposal, and I think it would be also good to have this discussion.
I will look internally. There's 1 1 person on our end who is obviously very much familiar with with Covid. I will have an internal discussion.
not sure if I manage this today until next week. But I would be looking at this, but would be also, you know, any input that you. We can start together on that as a as a group, I think will help.
**Joe Korchmar** 18:11 Do you? Do you know, what all your customers today are using cobalt 4 other than you know, like a Cics Tp interface right?
Where you we used to create Cics listeners with cobalt, too. And do different things. Do you have custom? If you kind of know what your customers are using cobolt for today.
It might kind of give you an idea around what you need around that area.
**Ruediger Schulze (IBM)** 18:49 I think I need to follow up on this. I think I don't have, you know, sufficient visibility. On this I had a couple of discussions which suggest that customers have been actually.
you know, if they have these these millions of lines of code with cobra, they have also very advanced technology to, you know, have foundation layers to these and what you know, implementations to you know, share functionality and and make efficient use of these these cobol implementations.
But yeah, I think I need to. I need to educate myself a little bit.
**Joe Korchmar** 19:26 Yeah. And and you know, my point was not just internal. And the person there that knows cobol actually get a hold of somebody at Ibm that understands what their customers are doing, because that's gonna be your be your largest target audience for a Cobo SDK, right?
**Ruediger Schulze (IBM)** 19:45 Right.
**Joe Korchmar** 19:46 Their buy in.
Then you'll know the impact of how fast it's needed, right?
And what flows through that open telemetry data flow for the implementation will help you prioritize that. And then your other discussion about pulling in college students.
Ibm in the Us. Is good at that. You guys donate 5, $10,000 to a college campus and get Phds and Masters your students all the time. And I did that. When I was at Ibm I had Phd guys working for me. Right? So there is a way. And you.
**Ruediger Schulze (IBM)** 20:26 Good.
**Joe Korchmar** 20:27 Find that process that you could get some grad students to focus and add it on their board as a senior project or a two-term project or a 1 term project, and tell them that you need these deliverables, and they'll get grad students to work on it.
And Ibm probably contributes to those colleges, so you could probably get some resources for that.
**Ruediger Schulze (IBM)** 20:48 Right.
How you get hooked into that here in the Us. I don't know.
I was actually referring to one of these programs that I'm aware of. So let's let's see, we had somebody last year to to get started on this. But it's also it's a challenging environment, right? If you if you work, bring somebody in who is not a Mainframer at all, and the person that I was working last year with was actually great. No, no mainframe at all, but took the challenge on and actually made some progress.
So yeah, we need to look at this just to mention this on cobolt. There's also it's probably also an area that we can reach out to is the open mainframe project. They have this Cobolt education project. I think there's this this cobol class. I think there are a couple of people behind Cobolt as well. I think we want to pull them in to to also help us with getting a perspective on the SDK work.
Okay? Other topics.
Okay.
**Morgan McLean** 22:06 Nothing for me.
**Ruediger Schulze (IBM)** 22:07 Then what I would suggest. Let's follow up on this Tps workflow discussion. I mean, we have an interest to get this Pr. Obviously off the off the off the table, and sometime soon.
Let's you know. Let's see what we can find out about the workflow discussion and where to go with it. And for the other activities. Then.
you know, let's let's move forward with them. I think the most interesting is still, or most important. One is still semantic conventions to make progress with.
**Morgan McLean** 22:43 Agreed. Yeah.
**Greg Shriver** 22:45 Okay. Sounds good.
**Joe Korchmar** 22:48 Morgan. I met you before. Right? I'm Joe Cornsmark. I I think I met you before on another call. Are you with Ibm.
**Morgan McLean** 22:56 I'm at Splunk.
**Joe Korchmar** 22:57 Oh, you're at Spawn.
**Morgan McLean** 22:58 I'm also on the open subject Governance Committee. It's the main reason I'm here. I actually don't know much about mainframes. To be quite honest.
**Joe Korchmar** 23:03 Okay.
**Morgan McLean** 23:04 But I know they're important. I know what they do, but I don't have any hands-on experience with them, and so I'm a little less useful for our technical discussions.
**Joe Korchmar** 23:10 Hey? It's the the way I look at it is still code running on a CPU right.
**Morgan McLean** 23:15 Agreed.
**Joe Korchmar** 23:16 It's epsodic versus Ascii, that's all you need to know. And all these hardware. It hasn't changed over the year. We're still writing code, and it's still executing in a processor except Gpus. It's a different paradigm in in quantum. But we we don't need to get into that yet. And, Greg, how about you?
**Greg Shriver** 23:37 Hi, Joe! I'm I'm work for broadcom.
**Joe Korchmar** 23:41 Okay.
**Greg Shriver** 23:41 So I'm part of the old computer associates, you know.
**Joe Korchmar** 23:47 Yep. I remember that I worked on Ca products 30 years ago, right.
**Greg Shriver** 23:52 No, and they're still around just like the mainframe.
**Joe Korchmar** 23:56 Yeah. And and you know, I was told they were going away back in the eighties right? But here we are.
**Greg Shriver** 24:02 Not, and here we are, you know.
**Joe Korchmar** 24:04 Yeah, so yeah. And my myself, I work at Wells, Fargo and and but I ex, Ibm I worked there almost 20 years.
and I've been with Wells Fargo, for I'm just starting my 27th year. So.
**Greg Shriver** 24:19 No.
**Joe Korchmar** 24:19 I'm at the end of my career getting ready to retire. But you know Rudiger's doing some fun stuff here in open telemetry, and I actually started. W. 3 C. Tracing before open telemetry was formed.
**Morgan McLean** 24:32 So I was on that. So if you've met, that's that's probably where we met. Yeah, I was one of the editors of that.
**Joe Korchmar** 24:39 Okay. Early days of W. 3 C.
**Morgan McLean** 24:41 Yeah, it's like me and Alois and Bogdan. And there's yeah a whole bunch of us. Yeah.
**Joe Korchmar** 24:45 Yeah, and I could. I couldn't do anything because Wells Fargo wouldn't represent me. So I.
**Morgan McLean** 24:50 Yeah, I had to leave the whole group when I joined Splunk. Same thing. Splunk's not part of the W. 3 C. So off I went.
**Joe Korchmar** 24:57 So, and then, about a year after we got into it. Then Google pushed open, tracing and open census.
**Morgan McLean** 25:03 That was, I was at Google previously. That was me. Yeah.
**Joe Korchmar** 25:06 There you go! There you go. So we've been at it for a while, and I you know I think it's great that it's about time Ibm is going to modernize the mainframe, and it's gonna make it easier on you, Greg, or whoever doesn't know the mainframe Greg. You do. But, Morgan, you don't. I think.
**Morgan McLean** 25:23 Well, when I, when I say we have customers that use it, I was actually thinking of Wells Fargo. So it's quite good that you're here.
**Joe Korchmar** 25:30 Bank of America. Wells, Fargo, everybody, you know, all the insurance industry.
**Morgan McLean** 25:34 I think it's more. Todd, Dicapu, and a few others from Wells are often on my case about mainframe support.
**Joe Korchmar** 25:41 Yeah, yeah, well, yeah, we and I was working with Rudiger before.
**Morgan McLean** 25:46 Oh, cool!
**Joe Korchmar** 25:46 That was joined. So we were pushing to get open telemetry on the mainframe, and I actually did an abstract implementation where I instrumented the boundaries of the mainframe and grabbed the context.
And then I use the the Smf records to get the transaction groups.
And then I associated the ins and outs of it to that transaction group, and then I can create the hotel events and send them into elastic. So I was doing that, you know, 4 years ago I had the prototype, but this is much better. This is what I was pushing and what I needed, but.
**Morgan McLean** 26:24 This is what we want. Yes.
**Joe Korchmar** 26:25 Yes.
**Morgan McLean** 26:26 1, st first, st class, yeah.
**Joe Korchmar** 26:27 1st class, yes.
**Greg Shriver** 26:29 Yeah, we're we're we're we're of the same mind there. I mean, we've been doing a lot of this stuff outside of open telemetry for a long time, and open telemetry is, in my opinion, the way for us to come together on this, and make the mainframe more visible to the rest of the entire ecosystem right.
**Joe Korchmar** 26:50 It's just another processor you dump in the ecosystem. You don't have to worry about it because the data model is defined. So.
**Greg Shriver** 26:57 Exactly.
**Joe Korchmar** 26:58 You know, how can we help Ibm get this faster is what I'm pushing for?
And how do we focus on? You know the highest level and work our way in like me, the SDK. As long as you do the I/O boundaries at 1st and get that flow.
then you can start getting more detailed on the instrumentation of deep inside. People want to drill in deep right away, and I really want to see that end to end flow, and anything coming into the mainframe going out and and going through each components at a top level. And then we can decide which ones we need to drill in and grab more events out and metrics right?
If if we try to do the whole thing and deliver it all at once, it's gonna take years right? So anything we could do to deliver the as much as we can and work our way in. And I think, broadcom, you guys already have. So each layer you could pull back and add the open telemetry and keep doing what you're doing and work your way in. So the broadcom implementation, the dynatrace implementation, everybody's implementation.
If Ibm does this right, I think it can deliver some stuff fast and and Rudiger's delivering fast. So anyway, my soapbox.
**Ruediger Schulze (IBM)** 28:16 Okay, fine. Thanks, Joe. If there's nothing else I would suggest we we close the call because I need to run for another one. So.
**Morgan McLean** 28:23 Same.
**Ruediger Schulze (IBM)** 28:25 See you guys, bye.
**Greg Shriver** 28:28 Thanks guys.
**Ruediger Schulze (IBM)** 28:29 But.
**Greg Shriver** 28:29 Buh-bye.
