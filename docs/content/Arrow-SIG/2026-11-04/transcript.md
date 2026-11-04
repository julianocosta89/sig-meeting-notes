SIG: Arrow SIG
Date: 2026-11-04
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Joshua MacDonald (Microsoft)** 01:41 Hello.
Here we are again, man.
**Laurent Querel** 01:53 Hi, guys!
**Joshua MacDonald (Microsoft)** 01:56 Hi.
**Jake Dern** 02:00 Hello.
**Joshua MacDonald (Microsoft)** 02:02 Just about to share the screen. Here it is.
It is November 3rd.
Sure, I'll just, do this, and, we can get started.
In my large fonts.
Okay… That'll… that'll be better.
Go ahead and enter your names. We have no agenda here, we can copy the, plan from last time.
Very good. Okay. It's been 4 days, work days since the last time, and I did look at the new issues, there are not very many of them.
How large is my… there it is.
That template has an extra W character.
Today we have 3 items listed, One of them we discussed last week, and I don't know if anything new has happened.
I… will encourage us to go look at this one. I don't want to discuss it right now, since it's 3 weeks old at this point.
There was APR open, and I see 5 of us here, so let's just, move to something we want to talk about.
This… issue I filed after last week's meeting. We talked with Nev quite a bit, as you recall, and he, wants quite a lot of things, and it was, discussed, this feature that we… that I was able to sort of isolate from one of his larger PRs, which, talks about RFC 7239, I didn't know details on this RFC before, but I did read up on it, and this is how a sort of W3C spec for the forwarded header, which includes, aspects like FOR, and by, and host, and proto.
And this is really important in the browser space. This is what Nev works on all the time, so, his knowledge on this is actually very valuable, and I wanted to, file this as an issue somehow to extend, header capture.
This would be an example that I wrote here, And that's what I have. Any comments?
**Laurent Querel** 05:05 Yeah, sorry, I was feeling the agenda. I didn't follow, so sorry to ask you to repeat that. So, what was the proposal here?
**Joshua MacDonald (Microsoft)** 05:17 So… There's a special syntax of header that is specified in the RFC, and it is pretty common for proxies, and it matters a lot for browser instrumentation, because it may pass through many proxies.
**Laurent Querel** 05:32 Mmm.
**Joshua MacDonald (Microsoft)** 05:32 And this was, roughly speaking, one of the aspects that Nev was looking for in his PR.
if you recall, last Thursday, we were talking about how, he had made a PR that was Quite large, but combined the ability to, first of all, extract this type of information.
From the forwarded header, and then in the attributes processor to take those values and put them into telemetry attributes, so that you can have telemetry that says which proxy you passed through using these criteria.
**Laurent Querel** 06:10 Yeah, sounds good. So that's basically an extension of the… Extraction, or capture, header capture.
**Joshua MacDonald (Microsoft)** 06:18 Exactly.
This would be fully isolated within header capture.
**Laurent Querel** 06:22 Oh, okay.
**Joshua MacDonald (Microsoft)** 06:23 conceptually outside of that, I think. But that we would have a way… To filter, or maybe this adds a way to take subsprings of a header, for example.
That you might want to extract and take apart.
**Laurent Querel** 06:42 And, yeah. But that will be backwards compatible with the previous, capture mechanism that we have. It's mostly an extension of what was existing before, right?
**Joshua MacDonald (Microsoft)** 06:54 That's right. That's the idea, at least.
**Laurent Querel** 06:57 Okay.
Good for me.
**Joshua MacDonald (Microsoft)** 07:00 And this last one, I don't see Drew. I was gonna ask him to discuss it. I know, Saroj filed it, and he also is not here in meeting, but basically, we're looking for some, improvements in the admin console, and, for showing receiver rates.
And exporter rates, and success rates. Drew asked for generic support, and it makes sense to me.
**saroj** 07:29 Yeah, I'm here in meeting.
**Joshua MacDonald (Microsoft)** 07:31 Oh, hey, sarosh.
**saroj** 07:32 Hi.
**Joshua MacDonald (Microsoft)** 07:32 Yeah, want to discuss?
**saroj** 07:36 Yeah, I mean, the Pierre I have created, maybe that is not a generic one, but the issue that I've raised here… So this is regarding an enhancement, where we can, where in the… in the OTAP admin dashboard, we can see the… you can scroll up, I can show you the screenshot they're talking about.
**Joshua MacDonald (Microsoft)** 07:57 screenshot.
**saroj** 07:58 They're just screenshot I'll say ad here in this case.
Yeah, this is the one, yeah. So, if you… if you go… at present, if you go to this page, basically, you can't find what is the EPS in a receiver site. We just see that what receiver sent to batch.
So, I am making enhancements so that in receiver, it will show the EPS.
**Joshua MacDonald (Microsoft)** 08:20 Okay, events per second.
**saroj** 08:22 Yeah.
And similarly, for the exporter side, how many events are uploaded, so those information are not there, so as part of this, this announcement, I'm trying to populate those information.
**Laurent Querel** 08:35 And this event persoaded, so yeah… I think we are talking about item inside the internal telemetry.
Is it something that you…
**Joshua MacDonald (Microsoft)** 08:49 I think this is batches in our terminology.
**Laurent Querel** 08:54 Oh, okay.
**Joshua MacDonald (Microsoft)** 08:58 And it says messages here as well, that would be good to clear up.
**Laurent Querel** 09:03 Yeah, I just want to make sure that we are talking about the same thing. So, if we are talking about batch, I'm okay. If we are talking about item, like, events.
Oh, Matrix?
What we discussed before is… It should be an option… an option, because there is a cost behind it.
Depending on the protocol and the codec use.
It's not always, free in terms of, override that.
So I just want to make sure that we are talking about the right thing there.
So, can you validate that you're talking about batch per se gold, or are you talking about… Really, an item, like an event, a metric that happened, or a spam.
**saroj** 09:54 Now, I am looking into, the how many messages per second they received from the receiver side.
So, you can see that, the… in the under… in that receiver, box, you can see that they received has 29,675 requests per second, right? So it was not earlier there, so it might change this…
**Laurent Querel** 10:18 Okay.
**saroj** 10:18 Yeah, those informs are getting populated.
**Laurent Querel** 10:21 Okay, okay.
**Joshua MacDonald (Microsoft)** 10:23 And we are duplicating the number 430 here, so this is requests, and it is messages. I think you mean OTAP messages, or request batches, as we call them.
**saroj** 10:35 Yeah, so I think I'm talking about, Whatapp messages.
**Laurent Querel** 10:41 Okay.
**saroj** 10:44 So, similarly, for the exporter side also, yeah, at present.
Well, we don't know that how many events are uploaded successfully, either in failure, nothing is showing there, so I'm just trying to populate this information here.
**Joshua MacDonald (Microsoft)** 10:56 I was gonna ask Drew to comment, because it seems like we could use the flow metrics that we've already computed and just illustrate them on the dashboard. In other words, whatever flow metrics you configure, you get to see, and that way you don't have any extra cost.
**saroj** 11:13 Okay, yeah, so let me go through the documentation or the code once again, and I will replace the Pierre that I created earlier, yeah.
So adapt, yeah.
**Laurent Querel** 11:26 Can you spend a little bit more time on this thing? Because… so first, this information was already there, but not inside the topology.
If you click… I mean, before this PR, if you click on the receiver or the exporter.
And you are, in the view where you can see the values matrix.
Attacht to the corresponding node that has been selected, you can see all the metrics.
The question is, what is the additional value of having this number of messages Or request per second.
when… Like, in this example, it's purely redundant with the… The information that we have on the edge.
And what… because, I mean, then next, what will be the next metric that you want to add on the receiver, and then this box will grow More and more, when we already have a space where If you scroll down, you can see all the metrics attached to this receiver.
My question is, why… why… what is the requirement to put this specific metric Part of the node representation.
**Joshua MacDonald (Microsoft)** 12:44 Hmm.
**saroj** 12:46 Okay, so, At present, if you click on this receiver or exporter boxes here, it doesn't say anything. So, it is not clickable, actually. At least, that's what I observed, in my experiment.
**Laurent Querel** 13:01 Oh.
**saroj** 13:01 it, yeah. I recheck it immediately.
**Laurent Querel** 13:03 That's very strange, because we should… Okay, so, For me, if you click on any node in the topology.
**Joshua MacDonald (Microsoft)** 13:14 Does anybody…
**Laurent Querel** 13:15 Question, then, sarj,
**Joshua MacDonald (Microsoft)** 13:17 engine they want to bring up, we could test this out. I don't have one handy.
**Laurent Querel** 13:22 Yeah, me too, but I suspect one thing. You were… maybe you… You were in, Full screen mode.
for the topology.
And then, in that ca- in that case, in this configuration, you hide All the other, part of the dashboard.
And you can't see anything when you click on, on any node. But when you are not in the full Screen mode for the topology.
If you click on any node, you should see At the bottom of your screen.
something scrollable, where you see all the metrics attached to this node. Same thing for any edge.
Between nodes.
**saroj** 14:16 I have the portal open now, can you share my screen?
**Joshua MacDonald (Microsoft)** 14:20 Yes.
**Laurent Querel** 14:21 Yes.
**Joshua MacDonald (Microsoft)** 14:22 Let me unshare.
**saroj** 14:24 Are you able to see my screen?
**Joshua MacDonald (Microsoft)** 14:25 Oh, you got it.
**Laurent Querel** 14:26 Yes, yes.
Yeah, click on Receiver, and you.
**saroj** 14:30 acidic.
**Laurent Querel** 14:31 Selection detail node.
No, no, no, right-click on the receiver.
No, the receiver, yeah, this box, yes.
**saroj** 14:42 Nice.
**Laurent Querel** 14:43 Scroll down, scroll down, scroll down.
**saroj** 14:45 Oh, okay, you're talking down here…
**Laurent Querel** 14:48 Yeah. They are, oh, they are.
**saroj** 14:52 Okay, so let me go through this, then. But it is all coming zero at present, you can see here.
Let me go…
**Laurent Querel** 15:01 Maybe because there is no traffic, but what I mean is… This information is only available And we have much more than this metric, And my concern was, yeah, you see there is no traffic, so that's why it's zero.
**saroj** 15:21 Okay, so then let me go through this once again. Yeah, if we're not required, then I can, close this case.
**Laurent Querel** 15:28 Yeah.
Yeah. Okay.
**saroj** 15:29 Thank you.
**Joshua MacDonald (Microsoft)** 15:40 Okay, I haven't looked at that console in quite a while, so that was good for me to remember.
There are some details if you scroll down.
Thank you.
**Laurent Querel** 15:53 Yeah, definitively, we can improve a little bit this, this UI, but, I think we have to keep… We have to find the right trade-off between what we display in the topology and what we want to keep in the detailed mode, because otherwise we will add more and more and more information, and the topology Representation will become, unusable, in my opinion.
So, Yeah.
**Joshua MacDonald (Microsoft)** 16:24 Let's, ask Drew to comment offline as well. Thank you, saroj.
I'm gonna bring back the notes.
Okay… Well, I think we went through all the discussion. This is our blast to the past.
6 months ago… Victor joined us and wanted to talk about Control Plane. He is still with us, working about Control Plane.
But not here today.
**Gokhan Uslu** 17:05 I think I can comment on that.
**Joshua MacDonald (Microsoft)** 17:07 Oh, please.
**Gokhan Uslu** 17:08 Yeah, so that was needed for something Back then, that we already have a solution for, so that's… But I don't think this is necessary anymore.
For our needs.
But if it is a valuable addition nonetheless, we can look into it.
**Joshua MacDonald (Microsoft)** 17:32 All right. I like that. We can close it. We'll see if it comes back.
And, albert has one… We definitely have some scalar functions now, so this might be partly done.
But I bet this has a list.
Very long.
Oh, jeez.
**Laurent Querel** 18:00 Yeah, I think they are all, changed.
**Joshua MacDonald (Microsoft)** 18:02 They all look good, all merged.
**Laurent Querel** 18:05 Yeah, it was probably an umbrella task for multiple subtasks.
Yeah, I think we can close it.
**Joshua MacDonald (Microsoft)** 18:16 Alright, I love it.
**Laurent Querel** 18:18 Seems good.
**Joshua MacDonald (Microsoft)** 18:20 And… okay.
Deciding… I actually… these are all gonna be old because I went through the new ones.
Any ones that we want to talk about?
**Laurent Querel** 18:40 Yeah, so, let's see… Yeah, we, we… Maybe, do we have Jake? Yes, we have Jake.
Either Jake or myself, we can talk about the entity ID, so we are trying to… to have, a unique ID per… what we name entity into the system, an entity being something like, a node, a pipeline, a pipeline group, Where we have.
**Joshua MacDonald (Microsoft)** 19:20 p-value sets, I believe.
**Laurent Querel** 19:23 Sorry?
**Joshua MacDonald (Microsoft)** 19:24 Abstractly, the entity as a key-value set.
**Laurent Querel** 19:29 Yeah, the entity is identified by a set of attributes, but we'd like to have a unique identifier.
An easy one that we can use to… To attach entities together, or to attach some additional information.
So, making sure that we have for each of those entities, when they are created, a unique ID, I think that's what we are trying to achieve there.
**Jake Dern** 20:00 Yeah, I can add just a little bit, more information. I think there's, like, a couple, orthogonal thoughts in here. One is, it's like, we don't have a way to disambiguate between entities that have sort of been deleted and then came back, for example.
So, like, if, you know, you delete a pipeline, and then you recreate the same one, those are kind of logically two different entities, and there's not really a way to detect that you did that.
And then the other one is, yeah, this idea that, you know, it's kind of annoying or difficult to compare, like, a very lengthy composite key that's identifying something.
And so maybe in some cases, it would also be useful to have a GUID for that, but I understand there's other techniques for that as well, like, you know, hashing the values and that kind of thing.
And then just a little additional commentary is I've been, attending some of the entity SIG meetings.
And something else we might want to consider in this design is kind of the ongoing work there. They're talking a lot about, sort of hierarchies of entities, and this concept of entity-identity scope. That's really fun to say, entity identity.
And, yeah, there's this idea or notion of global versus local scope entities, which are, you know, globally unique, those that have, like, a GUID or something like that, and those that are only unique within the context of another entity.
And then determining, you know, sort of from that, you know, what is the full set of identifying attributes, and how this relates to the concept of resource, and how this is communicated across signals, and that kind of stuff. So… All things, I think, to be taken into account for this issue.
**Joshua MacDonald (Microsoft)** 21:41 Gotcha.
Yes, today at the Spec SIG this morning, there was some discussion about that same topic. I learned about it as well, so I'm following you.
J… are we… And it's good that we mean the same thing by the word entity here, as the OTEL entity.
I do also worry that when we go to add entity support at the hotel level, that we might end up confused about terminology.
**Jake Dern** 22:11 Yep, very possible.
**Laurent Querel** 22:14 Dune.
And that's why I asked Jake, basically, to… To go deeper into the… this entity, workgroup, and various other documentation inside OpenTelemetry, just to make sure that we… We could align at some point.
Because… until now, I think the entities are at the OSUS level only.
I remember a discussion with, Joshu Race.
For a long-term vision, where entity could be at the scope level.
That's what we do.
So I… yeah, the idea is to see how we can, Follow a pass where… We can get the benefits of what we have today, which is, in my opinion, a moral… Precise, refined, way of using this concept of OTT Not only at the resource level, but also to represent internal components.
And how they interact with each other.
And see how we can, integrate that with the… the entity model that, OpenTelemetry is following progressively.
**Joshua MacDonald (Microsoft)** 23:34 Somewhat related to that, Jake, I've… I felt an issue a while back about how the ITS logging interface does not Treat entities very well, and there's a vector of contexts, or entities from the context that are… Printed, but they print with, like, a numeric identifier that means nothing.
And I found the issue saying, one day it'd be nice if we could fix that. And I think having a identifier that was, stable would at least address much of the problem for me, and the way I like to think about it is that when you start your process, you are going to build your entities, which means creating those handles that we call entity key.
And when you create the entity key, you know the full details there, and you also are going to assign an identifier.
So, in the sort of history of your application, you've logged everything about all of your entities at one point in time. So, first you created the entity, you logged the identifier, and now, when you refer to that in your log, you can just log the identifier, and somebody who wants to can join that, and that's what I would like to see for our ITS logs.
**Jake Dern** 24:47 Yeah, absolutely. This is also something that's discussed, in the, the entity SIG, I believe… oh, I'm gonna get the term wrong, I wanna say they call it something like telescoping Identity, something like this, But the idea that you sort of have a choice in terms of how much, information you're including, when you describe your entity, and that, like, you know, the extreme, like, example that's, like, very efficient is to, is to do what you said, which is assign it an identifier and then do a join and only omit the full attributes at once.
Versus, you know, having and… or omitting all the attributes every single time, and… or recording them every single time, and not having to do the join, but at least having a little bit more of a description to look at.
**Joshua MacDonald (Microsoft)** 25:30 Right, and I think that I like to think of saving those bytes more than I like to see easy, like.
Extrapolation of entities or whatever. In some cases, at least.
I'm thinking of debug logging, basically, like… The logs would be too expensive if we put everything in there, and… So at least it's a choice.
**Jake Dern** 25:56 Yeah, and there's interesting, questions as well in terms of how we actually want to emit the information about entities then. Not just represent it internally in the engine, but also then omit it. I think an aspect to the entity work that's kind of odd to me, but I think makes sense, is that There's, like, a set of documents describing what an entity is in the, like, abstract, and, like, not taking into account, sort of, the resource model at all.
And then there's the actual, like, okay, well then, how, using the existing resource model and signals, do we communicate information about entities? And there's sort of competing ways to do that. So, we'll… yeah, more investigation to be done about how to best align, I think.
**Joshua MacDonald (Microsoft)** 26:40 And do you see yourself leading us towards having more OTAP support for entities?
**Jake Dern** 26:47 I think that's a totally separate thing.
**Joshua MacDonald (Microsoft)** 26:50 Okay.
**Jake Dern** 26:50 It also scares me.
**Joshua MacDonald (Microsoft)** 26:54 Okay.
Very good. Well, I guess onto the agenda.
And I know we have Gokhan, and Laurent wants to speak about 4581.
**Laurent Querel** 27:10 Yeah, so I started to review it, Gokhan, I think we… I think we are taking some risk there by introducing too much in this Pierre.
the… I think the original idea was, in 4303, To share the same… Behavior of the same code, at least, for, reconciliation.
Tyler configuration and, the initial startup.
That, I think, is definitively interesting to do, so we… We have less, similar logic in different places.
But this gate, mechanism that you also introduce, in my opinion, is… is problematic.
So, I can give some example of why I think it's… so first, it's inconsistent, in my opinion, because… we… If the goal is to have the same reconciliation mechanism.
I use either during a live reconfiguration for a running system versus The same system when we… we start the… the server.
Then, when we update live on Configure.
if one pipeline fails, we are not stopping the server. It will be, problematic. That will be even a security issue, in my opinion.
But that's what we… that's what you propose to follow in the… with this start gate approach when we start the system.
So there is an inconsistency between the live reconfiguration and the initial start. They are not behaving exactly the same way.
When there is a pipeline that doesn't start properly.
And the other problem I think I see behind that is… let's imagine that you have A big configuration.
with 100 tenants. Each tenant has a specific pipeline configuration. Potentially, they are in different groups.
And… We just need one pipeline configuration.
that fail.
To have the server not able to start at all, which is, again, in my opinion, a big problem.
We should not be in such situation.
Because a pipeline can fail for many reasons.
And we are trying to have isolated, isolated, Pipeline configuration as much as possible.
So one failing should not impact the others. We could have a special, startup configuration.
Or some case where we really want to make sure that every pipeline needs to To be, okay, or nothing.
But I don't think it's, it's a default behavior.
But I'd like to get your feedback on that.
**Gokhan Uslu** 30:23 Okay, so, yeah, my initial approach to this PR was I just took it from NOAA, and I tried to address the issues there, which one was to subscribe before we publish, and wait for all pipelines, all pipelines to be ready for that. So… But I had a similar… some of the questions in my mind that you already answered, so I think I'll just go back to the drawing board, and I'll try to take the spirit of what Noah wanted to do, and then we'll take this feedback and see if I come up with something new.
**Laurent Querel** 30:57 Okay, great. Please, ping me if you want also to maybe interact over Slack, or have some, Yeah, design… design brainstorming together, don't hesitate.
Maybe that could, accelerate the review and making sure that we… We are going, together in the same direction.
**Gokhan Uslu** 31:23 Okay, yeah, will do. Thank you so much.
**Joshua MacDonald (Microsoft)** 31:27 Thank you. Yeah, I misinterpreted what that gate was doing. I remember thinking it was about… topic correctness. Like, if you couldn't get your topics initialized, then the startup gate would fail, which would be a more grave condition than one pipeline failing.
But it looks like I misread that as… misread it as well.
**Laurent Querel** 31:51 Yeah, and if you… can you click on the 4303?
Yeah, there is, there is one comment I left, one or two weeks ago.
With an illustration somewhere… yes, there. Okay.
So that, that was a feedback, I… gave to Noir, about some… something that should work, and was no longer working in this PR, so… I think we should also take into account the comment… especially when we create a new PR, which is based on another PRR, My recommendation will be to make sure that when you have into your description of this new PR, You are addressing… or if you are not addressing, at least you are mentioning What you decided to do, Based on previous comments that were… that were not addressed.
In the initial PR.
Because then, otherwise, I have to go, go back to the implementation, make sure that what I already interviewed 3 weeks ago is correctly addressed. If not, I'd like to understand why, and so on.
So, I think it's a good practice to make sure that when you create a new PR from an existing one that was not merged.
You make sure that everything was noised.
**Gokhan Uslu** 33:23 Okay.
**Joshua MacDonald (Microsoft)** 33:24 Thank you.
Yes, this… this diagram also matches what I've… what I read about topic orderings, but I will let Gokhan expand on that, and thank you very much.
**Gokhan Uslu** 33:39 Thank you.
**Laurent Querel** 33:41 But I definitely agree with the… I don't… I just want to make sure that my message is properly, perceived.
I really like to see the… The system improve in terms of consistency and, and reducing… code duplication.
At the same time, that's the kind of thing that is so deep into the engine that we have to be very careful on what we are doing, because we can basically break, either what we do inside Microsoft or what we do inside F5, and that's definitely an example of where we have to… To be very careful.
**Joshua MacDonald (Microsoft)** 34:24 Thank you.
**Laurent Querel** 34:27 Yeah, the second topic is, something, observer extension. So… Today, we have… And same for Gokhan, by the way. We have many extension types.
I also introduced, a few months ago, this concept of controller extension.
And this Querel extension was a way, for example, for us to expose a support for OPOMP.
And we could imagine, using the controller extension for Other type of, controller integration with this telemetry data plan.
So the observer extension is, like, a follow-up of that.
Maybe, I could use, for the… one of the first time, maybe the… the whiteboard.
to explain, because I didn't prepare the, a proper RFC or a GitHub issue, but I'd like to talk about this idea just to Maybe to get some feedback, and then I will take the time to create a corresponding RFC.
Except if we have other topics to discuss.
**Joshua MacDonald (Microsoft)** 35:50 This looks… looks great.
**Laurent Querel** 35:52 Yeah, okay, so… Let's see.
What I'm trying to achieve is the… the following.
So, today we have, this, metric or history.
We have, we have the… Even Q.
or I should say, internal email queue.
We have… What we name the observed to have states.
All of that are basically, internal constructs.
internal telemetry of some kind. The first one is about… So, it's about, metric set.
So we have this notion of metric set, which is… Something more… more optimized for the engine, as opposed to what we have in the open telemetry project, where we have, what I name, evaluate metric. So, one metric, time theory with a set of, attribute… Qui value per… A metric set is a collection of metrics that are connected together, they share the same attribute set, and when we We are in a collect phase. We collect the metric values at the same timestamp.
Attached to the same attribute set.
So this metric set registry, I should say metric set registry, is an internal representation of all the metric set that we capture regularly, or periodically.
For every pipeline instance.
Internal, event queue is the shared queue that every… so we have, euro.
Pipeline on time.
And we have, potentially hundreds of them.
And they are all connected to this, internal event queue.
The Utks state?
Or, is a specific representation that is, used also by the pipelines to report internal events representing Okay, this pipeline is up and running, this one is in a draining mode, or shut down, or whatever. So that… that's the… The kind of internal event that the engine now captures automatically, there is no need for any kind of intervention of the… another implementation.
Those events, internal events, are the events that are produced by, custom nodes.
So I will say… I would say, custom… events… And that is more system events.
And here, we have… We have snapshot… metric set.
So that's the current situation, snapshot matrix set, just to reuse the… WLG used already in the project.
This entire thing represents, what I will qualify as internal telemetry object.
And then we have the ITS.
an ITS is like any pipeline here, except that it's a pipeline that is dedicated for internal telemetry processing, internal… telemetry system, the ITS, Is, in fact.
A specialized pipeline, configurable by the configuration file.
And… and inside this thing, we have… So I… Where… where can I define… oh, that's here.
Okay, so inside, do you think we have the… Something named the internal… Internal, receiver.
I think it's something like that, and then… We can have as much as processor, exporter.
Connected to this internal receiver.
Processor A… Whatever, VC, so let's say processors.
Bi… il… blah blah blah, and and how much, I mean, as many has exporter you want for your specific need.
And this internal receiver is currently, behind the scenes, connected to this, stuff.
And the role of this internal receiver is to convert The internal representation of the subject into… Open telemetry, object.
So, events, it's fairly easy, because we… internally, we have, we don't, have a very specific stuff. In fact, it's already OTLP-based for the internal event queue.
That has been integrated and implemented by Joshua.
The metric set is a special case, where, yeah, we have a better internal representation for metric set, for the reason I mentioned before.
And the internal receiver is… Because right now, OTLP and OTAP don't support metric set, or multivariate matrix. We have to… to basically convert multivariate matrix into a set of univariate matrix. So we duplicate the attribute, we duplicate the timestamp, and so on.
Right now, we don't have a link, between observed state Which is unfortunate, but, Jake will work on that soon.
With the idea of, Basically, entities, like pipelines and groups and so on.
They will report their internal status.
Which is something that is known here.
And that will be directly exposed as, Something like a status event, sorry, a non-city event, or something like that.
Still to be defined, but that's the idea.
So, long introduction to say where we are… what we already have, and… and… basically something where we are going in terms of future development to get all the internal telemetry fully connected with the internal telemetry system. So now, this idea of observer extension is One step further.
And, so, let's see how I can do that.
Like I said before, we have this concept of controller extension.
In fact, it's controller extensions, that will be extensions, will be more correct. We can have multiple of them.
Like that.
And this controller extension is able, already, to interact with… The pipeline controller.
Which is an internal component.
pipeline controller, obviously, is able to start, stop, doing some different type of tasks on, On the pipeline's runtime themselves, and the controller extension is just… An abstraction with a well-defined interface that you can extend.
in the binary application that, you create on top of the set of libraries that we have. So, for example, we created this controller extension. So now the idea is, let's do the same thing, but with… Something like that.
So the observer extension will be something that is able to access Everything there, but with their, optimized internal representation, not the one that we publish here.
Because here, we… we destructure a metric set into really varied metrics.
Or into… into a set of unified metrics.
The observer extension will be something that is only Understood by our own engine, able to access to any of those internal representations.
And we'll be able to do two things. One.
Generate, new metrics, or… event that will be, directly published to this internal receiver. So if we… if we want, for example, to… to derive some metrics, metric set, or if we want to derive some event.
From an analysis of various things.
That's where the… you could do that with this observer extension.
But, the second aspect of this, observer extension Will be to create a feedback loop.
between… this internal observer extension, the controller extension. So, when, for example, we observe that a pipeline runtime, is… Let's say you want to implement an auto-scaling mechanism.
Adding a new core for a pipeline, so you start with 2, And you observe that it's way too, Too busy, you want to create another deployment for this pipeline, there is still core available. That could be done with this kind of thing.
So that's the goal of this observer extension.
Long explanation, so, sorry for that, but let me know what you think about that.
**Joshua MacDonald (Microsoft)** 47:25 So, Pierre put a question in the chat.
Any P. I would like to… Ask himself.
**Pierre Mariani** 47:32 Hey, folks. Yeah, I was… I was trying to understand, which thread runs the observer extensions that you're proposing more?
**Laurent Querel** 47:42 Oh, that's… that would be an independent spell.
**Pierre Mariani** 47:44 In the bathroom.
**Laurent Querel** 47:45 So, yeah, the… that's definitively a good question. So the… Sishh.
Yeah, we… for… for pipeline runtime.
Let's say for a specific configuration, we have one… Pipeline Insta… one pipeline runtime instance.
Fair call.
And because we have this, and we have, so we have… Per thread, that will be more pinned to… To, a dedicated core.
Educated core.
So, if we have a configuration, what I name a pipe… I will make a difference between a pipeline configuration, pipeline instances.
So, a pipeline instance, is… In fact, a thread with an asynchron time.
Running into this thread, pinned to a core.
Configured.
from a pipeline configuration.
The same pipeline configuration could be deployed on multiple core, multiple threads.
Depending on the number of core assigned to this pipeline configuration.
We also know that we could have different pipeline configurations deployed Either on independent core, or in overlap with other core, with other pipeline configuration, the system allows that.
Now, the… the threads that are… Where those scenes?
And, everything that is not pipeline runtime, and those things.
They are… running in independent threads.
So the internal telemetry system is running into a dedicated thread.
that, if I remember well, we have one spread per controller extension in order to make them independent and not having any Potential impact to each other.
And, same… same approach for that.
We have, one thread per… we should have one thread per observer extension.
And, the goal is to isolate them as much as possible. Now, where they are pinned, it's still an open question.
I think we… Right now, they are not… those things are not specifically pinned to a dedicated CPU, and there is no way to specify it.
I think that's something we will, progressively, Integrate into the system, either something manual that we can specify, or… More… in my opinion, the best way will be The pipeline for the controller mechanism, the engine controller, engine slash pipeline controller.
Should be smart enough to know… What are the core that are fully dedicated to pipelines sometimes?
And maybe decide that one core will be used specifically, or maybe two. We need to think about that.
But at the minimum, one core will be dedicated for some… Internal, internal work, like the controller extension, observer extension, and so on.
So this work is not fully defined right now, and I think the… Depending on the nature of the architecture, sometimes when you have a… a newer architecture. We could imagine that, we, we have, we take into account this new architecture, and we have, Some redundancy, just to minimize the… the communication across the manhood.
That's something we discussed a long time ago. Right now, it's not implemented.
I hope I answered your question, Theo.
**Pierre Mariani** 52:11 Yeah, I think so. So the ITS is one thread that's guaranteed.
**Laurent Querel** 52:18 Yes.
**Pierre Mariani** 52:18 central large rectangle, I forget its name, but it's kind of the shared queue, the shared 11 queue there, is also one thread.
However, controller extensions are today on multiple threads, and so it makes sense, because observer extensions control, controller extensions to a degree. It cannot make sense to, to also have them run multiple threads. That's… that's what I want to.
**Laurent Querel** 52:45 Yeah.
Okay. Yeah.
Yeah.
**Joshua MacDonald (Microsoft)** 52:50 And you mentioned NUMA. I know that one of the things we've talked about is having observability happen one per NUMA region. Would you imagine this observer becoming one per NUMA region?
**Laurent Querel** 53:03 I think, once we… first version, no, but I think, when we start to be… More than you nowhere.
I think we should, yes, start to think about how can we optimize the communication across Node?
Or minimizing those communication across Node.
And sometimes that will require to have a full separation. We could consider a multi-numanode system as multiple servers.
And and deploying, basically, the various internal mechanism, one per lumenode, would make sense.
**Joshua MacDonald (Microsoft)** 53:54 Gotcha.
Very good use of the whiteboard here.
**Laurent Querel** 54:01 Yeah, I'm a big fan of the Zoom whiteboard, it's very effective, and and by the way, it's attached to the… To the session, so you can go and retrieve the… the whiteboard, and you can export the whiteboard also in this… I don't remember if there is multiple formats, but, yeah, PDF, image… There is a comma separated.
What you will do with that, but, yeah.
**Joshua MacDonald (Microsoft)** 54:29 That's…
**Laurent Querel** 54:30 definitively interesting.
**Joshua MacDonald (Microsoft)** 54:34 Very good.
**Laurent Querel** 54:35 Okay.
**Pierre Mariani** 54:35 It sort of.
**Laurent Querel** 54:36 Oh,
**Pierre Mariani** 54:37 Gokhan.
**Laurent Querel** 54:39 Yes.
**Pierre Mariani** 54:40 So… So right now, the ITS internal receivers, have their own custom format, which is derived from the state of the shared queue, the shared observed state, internal event queue, and metrics at registry.
Would you move, that processing code, that, that, you know, format transition code, into an observer extension in this case?
**Laurent Querel** 55:10 No, I think they are playing two different roles.
This one is… Because basically here we are representing, I mean, we… That's the… the… Let's say the configuration piece… Where a user can compose a pipeline with reusing any kind of processor and exporter available.
for what we have here, so if you want, for example, use OPL to To do some processing on internal telemetry.
if you want to export the internal telemetry to, I don't know, KlikaOS, or to TLP, or TAP, you just… it's just configuration.
So the ITS really is giving you the same kind of capability that you can leverage here, but for internal telemetry.
So the internal receiver is just there to adapt this internal telemetry we have.
Into something that is consumable by, standard pipelines.
As opposed to the observer extension, which has a deeper integration.
Does not limit the observer author to something that is purely open telemetry.
So the metric set is an example. Observe state is another, because observed state is like a topology.
Of the different pipelines and how they are interconnected.
And, with, status and condition. So when you do the slash status, for example.
the, the status endpoint. What you get is… A subset or a view of the observed state, system.
So the observer extension will be something that… Really, we'll have no constraint on what you can… you can see.
and, and leverage… There is no transformation between this internal system and the observer extension.
**Joshua MacDonald (Microsoft)** 57:25 For the record, the login code path does have an intermediate representation that is sort of along the lines of metric set, which is partially encoded OTLP, but we only partially encode what we have to, absolutely, in order to get off the current lifetime of.
**Laurent Querel** 57:41 Yeah.
**Joshua MacDonald (Microsoft)** 57:42 arguments to the log statement. Everything else, like timestamp, metadata, like call site information, is all still raw, and the logTap extension… I wouldn't call it extension, but log tap is a mechanism that gets to see that raw encoded log record, and I assume the observer extension might have a reason to do that as well.
One of them was, we've… I'm at least pushing us to have Kind of plain old logging statements for… Some of the special observability signals that we have, we… a few months ago, we added this… a few weeks ago, we added this diagnostics package that sort of rate limits logs from the receivers or the exporters, and those could also be viewed as internal events, which have Call sites, but are effectively the same as the log statements we see from ordinary code.
And you would see them In the observer extension as these log records, which are half-encoded, again.
**Laurent Querel** 58:44 Yeah.
**Pierre Mariani** 58:46 Okay, thank you for sharing your spread, Jessa.
**Joshua MacDonald (Microsoft)** 58:51 Cool.
**Laurent Querel** 58:52 I think that that will, that will give, people integrating the DFE engine very deeply into their infrastructure.
Nice way to extend The engine itself with more advanced control.
That could be, yeah, this feedback… internal feedback loop, for things like the auto-scaling, I was mentioning, is an example, but we could imagine many other things.
**Joshua MacDonald (Microsoft)** 59:23 Very good. Okay, we're at time. Everybody, thank you for being here, and we'll see you next time. Next time, however, is going to be during the week of KubeCon, and a bunch of meetings are not happening, and I have to think about whether Thursday morning is gonna work, but let's see next week. I may not be here.
**Laurent Querel** 59:43 Yeah, and yeah, same thing for me. We, we, let's discuss that, definitely.
**Joshua MacDonald (Microsoft)** 59:50 Great.
**Laurent Querel** 59:51 with the…
**Joshua MacDonald (Microsoft)** 59:52 Thanks, y'all. Good week. Thanks, y'all.
**Laurent Querel** 59:53 Bye.
**Pierre Mariani** 59:54 Thank you.
**Jake Dern** 59:55 Thanks, everybody. Bye.
