SIG: Semantic Convention SIG
Date: 2025-07-14
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/_W961WtVTIvpAUP3P6RRql8m_qWQt_wxLVG0cuY0-hJAgXdo2ybo_3EvtX8giIat.iVPwGRBXrkfYwz4F
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:02:01 Hi! Everyone.
Josh Suereth 00:02:04 Hello.
so other simcom maintainers. I my Internet went out today and my power went out. And so I've had spotty Internet. So someone else can run the meeting. That would be ideal. Today I was gonna offer
before 1030 when my Internet went down. But I seem to be on. I think you can hear me.
Liudmila Molkova 00:02:26 Yeah, I can watch if you if you want.
Josh Suereth 00:02:28 Yeah, thank, you.
Liudmila Molkova 00:02:31 Course, so let's get going.
Please add your name to the agenda. If you have anything to discuss, please set your topic. It would be wonderful if we had some time slots
be pessimistic. We usually run out of time.
So let's take a quick look at the project.
4, th we don't have any pull requests to merge. They're ready.
I have a bunch of them that are blocked.
R.
So let's take a look. I think. Do you have anything from the client's sake? I always wonder.
What should we do with the client per requests?
Clay, does anybody know why? Why is it blocked.
Josh Suereth 00:03:39 Unfortunately meets the same time as the profiling Sig, so I haven't been able to check it out.
But it's it's interesting because Ms. Nev and breed X. Sorry I should actually say Jason and nev
have approved it, so that that is the client's sake.
Daniel Dyla (Dynatrace) 00:04:06 Yeah. The the browser started up. A couple of weeks ago, and we've had only 2 meetings so far, and the 1st meeting was more of just like an introduction. So we we really only had one meeting with substance. We we brought some of these Prs up
to to
as like, what's the current ongoing work? But we didn't really talk about the status of them in any detail, so I'm I'm not sure what the status is. I was just looking at the participant list here. It doesn't look like anybody else from that
group is in this meeting right now. So sorry I don't have anything specific to say about it, but I suppose I'm the only one that
is active in that Sig, so
I can try to find out more at the meeting this week.
Liudmila Molkova 00:04:57 Yeah, that would be wonderful. I I added a comment. So it would be nice to understand if if there is a consensus within the seek, and we can review from the Simco site.
Daniel Dyla (Dynatrace) 00:05:08 It's my understanding that the client Sig it is the client Sig
replaced with the browser sig, or is it in addition to I think it's replaced with it right.
Liudmila Molkova 00:05:21 Okay, then it would be a great thing to do to take a look at the contributors.
and oh, sorry for donors, and we have a couple of groups here, I think mobile and client.
Hmm.
right?
And we would do there need to update the group, name or create a new group. Update this file. You see what I mean.
Daniel Dyla (Dynatrace) 00:05:53 Yeah, I do.
Okay. I'll try to find out more.
I could just be wrong about that last thing. So
probably don't do anything until until we confirm it.
Liudmila Molkova 00:06:07 Yeah, appreciate it. Thank you.
Daniel Dyla (Dynatrace) 00:06:09 Yep.
Liudmila Molkova 00:06:11 Okay, let's spend a few more minutes on the blocked Prs.
I, does anybody know what's wrong here?
Okay, I blocked it.
A bunch of additions
we are almost of time on our triage block. But if anybody here wants to discuss any of the specific Prs, please send them to the agenda, so we definitely would have a chance to look at them.
So I'm just going to take a look at this one.
James, why do you think it's blocked.
James Thompson 00:07:03 There's still ongoing discussions, right? Like couple of files needed to be deleted after the last round of changes.
etc, all right, because the namespace was updated
alright, and the old auto generated file was not deleted.
Liudmila Molkova 00:07:24 Okay. So that seems that, like the Sig is still working on their review.
James Thompson 00:07:29 Yeah, it was updated a couple of hours ago.
Liudmila Molkova 00:07:32 Okay.
okay, so we are
out of our time. Box as A is is if there is something in the block section that needs immediate attention. Please add it to the agenda. We will
get through it then.
And if we were, if we still have time after, let's go through the blocked Prs and see.
okay to rusk.
Do you want to go about dots.
Trask Stalnaker 00:08:12 Hey?
Yes, yes, oh, yes, the ever important So I raise this because it's come up in Dr. Reviews a few times in Java
metric descriptions sometimes end with their sentences and end with the period, and sometimes they don't and
some people think they should, and some people think they shouldn't. And so I would like just a consistent answer. And I'm happy to make the changes one way or another.
For some reason I thought that they were supposed I thought they were supposed to be sentences. I thought I remembered that from way back, but
I couldn't find. I went looking, and couldn't find any existing markdown about that.
So I'm probably just wrong.
Liudmila Molkova 00:09:10 Is this just a question of Dot, or it's a question of how people write this sentence.
Trask Stalnaker 00:09:24 Yeah.
Liudmila Molkova 00:09:25 If the tooling just appended normalized it, and appended.to everything, would this become resolved.
Trask Stalnaker 00:09:33 I think we would want to do it in the yaml.
Liudmila Molkova 00:09:38 To someone who writes it should end it with a dot.
Trask Stalnaker 00:09:41 Yeah, if we choose that route.
just so that other people consuming that Yaml also get the same variant.
Liudmila Molkova 00:09:55 Yeah, I mean, we can normalize the yaml and all the tooling could append dots.
Trask Stalnaker 00:10:03 Yeah, either way. I I honestly don't care. I just want a consistent answer.
Armin (Dynatrace) 00:10:10 Yeah, plus one on consistency. I think if we always append it up, it might look a bit odd if it's a 2 sentence description, and the 1st one ends with a dot, and the second sentence by definition
would need to not end with one, because the tooling appends it.
So maybe if their email was
the final outcome straight away, I think it will.
Liudmila Molkova 00:10:36 So you're saying that it, that the
we would not end things with that and and the tooling would just append. But it can normalize right? If that is.
Trask Stalnaker 00:10:49 No, we're saying Armin and I are saying the opposite that they
person writing the yaml would put the.at the end, and the tooling would just
validate that there is a.at the end.
Liudmila Molkova 00:11:05 I see. So the the yaml and check of some sorts.
Trask Stalnaker 00:11:08 Right, right.
Josh Suereth 00:11:20 I think it's reasonable for us to just put a.in our policies in the yaml, and then have everyone add a.as long as it's automatically count
like, how do I? I think we should not spend more time on this
personally, let's just pick one. Let's enforce it with the tool.
and then, if you don't like it, change the tool
and make sure that you automatically can fix everything with a tool as long as it's automatic.
I don't care which one. It is so quick.
Trask Stalnaker 00:12:00 Alright, I will send the Pr.
Liudmila Molkova 00:12:12 Okay, James, can we spend a few minutes adding time boxes to your topics? How much time do you think they would take.
James Thompson 00:12:23 It depends on how long Josh and I, like Josh, has gone through and reviewed the documentation registry.
Alright! So that was a hard one to get time. But the span kind should be relatively quick, and the second one's just an update on last week's discussion.
Alright, the 4th one.
Yeah.
Alright.
Liudmila Molkova 00:12:41 I'm going to to spend 5 min just because
and you're saying this one would take longer 10 min.
James Thompson 00:12:51 Yep.
Liudmila Molkova 00:12:57 On this one.
James Thompson 00:12:59 Less than 5 min.
Liudmila Molkova 00:13:06 I'm just trying to understand. This is 20 min, 30, 40. Okay, we should have.
James Thompson 00:13:12 Okay.
Liudmila Molkova 00:13:13 Okay, do you want to talk about span kind.
James Thompson 00:13:15 Yep. So, looking at the documentation in a lot of cases.
the description of the spankine is should be
what internal? All right, consume server, client, etcetera.
a couple of scenarios, I think there was like 2 scenarios where it's been changed to required
alright must be server. Must be client right?
Do we actually even support changing the span kind from the standard definition?
Is there a use case for that?
Right for me? If a if a span should be a server or a client that should be 2 different spans.
Liudmila Molkova 00:13:56 The should and mast are used in a sense that in Http we use must, we cannot change it.
James Thompson 00:14:03 Yeah, right? But so.
Liudmila Molkova 00:14:05 Because there are, there could be variations.
James Thompson 00:14:09 And yep go you go.
Liudmila Molkova 00:14:12 So, for example, for databases
there is a client span usually use client, but if you know that you instrument in memory database, you might want to use
internal. And it's not. It's allowed. It's fine.
James Thompson 00:14:28 Yeah. But when the
in memory database have a lot less fields in it because it doesn't have the networking information, all that. So that should be a separate definition of a span.
Liudmila Molkova 00:14:41 Yes, but sometimes you don't know that it's an in memory database, really? Well, so, or it, it might be difficult to split this plans. Yeah, we we can split them.
But we shipped stable, database, semantic conventions which should.
And now we cannot really change it.
James Thompson 00:15:05 Yeah, you know. But so I'm I'm just interested is
but everything is shipped as should, except for like 2 scenarios.
Alright, if right, there's 2 musts
all right. Everything else it should be.
Liudmila Molkova 00:15:22 Okay.
James Thompson 00:15:22 And there's.
And so I'm wondering, do we actually need that delineation between the should and the must and the span kind?
Trask Stalnaker 00:15:36 Can I? Sorry I'm trying to follow? Can you give some context for this.
James Thompson 00:15:43 So. So when you, when you look at a span definition right most of the time this is, should be right. Server should be client. For example.
right? There is 2 cases where that's been changed to must be. Server must be client.
Trask Stalnaker 00:16:03 And there's 1 of.
James Thompson 00:16:04 Can you? Can you add a link to those places.
Trask Stalnaker 00:16:09 Are those pr, open prs.
James Thompson 00:16:12 Yep.
Trask Stalnaker 00:16:14 Cool.
James Thompson 00:16:15 Yeah, but it's just about understanding.
Is it like for me, it's very much like an instrument type. The span kind. Is it a server, or is it a client.
you know, because it's something you need to sit up front. So you know
what definition of a span you were to follow?
Yeah.
Trask Stalnaker 00:16:35 So. Certainly. I mean, I agree that, like, I don't think
I'm having a hard time thinking of use cases where something could be either a client or a server.
But internal is kind of weird.
and we don't have a really clear definition. Well, maybe we do but like something that's a server span like in Java. Serblets
like there can be nested. Serve, lead.
and if we you might have instrumentation capturing a server span that's not
actually at the outermost call, but it's still, you know, capturing that stuff. So it's certainly
it feels arguable whether that is a nested server span, or
which is how we model it currently. And I think we've generally said that nested server spans are okay and nested client spans are okay.
But I could see somebody preferring that those nested ones are marked as internal.
Josh Suereth 00:17:46 So I just want to add that we should. We should think about how these things are consumed.
like the one of the expectations behind client and server is that the resources will be different between them. And you can identify. Okay, here's a client talking to a server, and you can use that to discover the edge
right? So I know that this resource is talking to this resource. I have a client talking to a server
for example, our internal system that does spans. We actually create a synthetic half span and a synthetic half span on both sides, and we only have one span to denote the entire edge.
That's that's how our internal system works in open telemetry. We create a client, a server span, and then the downstream trace system has to understand that this is one conceptual connection, right
for those in memory databases. I think we could go either way here. And this is a decision. I think we should probably provide guidance for a sem conf. But that would be, and I like what was done in the current database thing of hey?
You only need one span. You don't need both sides to do both connections, so use the client side, call it internal.
and you know that you're talking to a database because of the database convention, and you know that you're not crossing a network boundary because your resource isn't different. So if I see client and server. I know I'm crossing some kind of a resource boundary where I will have different resources. I will have to construct an edge of some fashion.
But if I'm talking to an internal database, it's a kind of a library boundary using internal with the current semantics kind of makes sense to me.
In that sense, right? But I think we just need to be consistent with what we recommend. So tooling knows how to interpret our spans.
That would be my suggestion here. But I I think
when you look at how open telemetry is done like the span metric processor and some of the other span processors in the collector.
having this notion that a client and a server can connect and and be an edge between 2 resources is a thing that we should try to preserve
like. That's a use case where is well known and well understood.
James Thompson 00:19:54 Yeah, I agree. And, like my concern, more about is having the delineation should be this, or must be this right, having that difference between the 2 different categories.
That's
because at the moment everything is should, unless we override the notes, comment, notes field with a custom message for it.
Josh Suereth 00:20:16 One thing we will say when you see, should, in open telemetry specification.
most open telemetry. Sorry in semantic conventions, semantic convention implementers should treat that as a must like. We generally, in our own instrumentation from opentelemetry, treat it as a must.
and the should is to account for non open telemetry instrumentation authors who might not be able to abide by all of our restrictions.
Go ahead, Daniel. Sorry I jumped in front.
Daniel Dyla (Dynatrace) 00:20:47 No, that's fine.
I don't think you did, anyway. I was just gonna say the the way that I typically think about like client server internal is is always like.
I I think about the context propagation, like, if if something calls the inject, then it's typically a client span. And if something calls extract, it's typically a server span, as just like generally a rule of thumb that also I it doesn't
a hundred percent map to everything. Because, like for database calls, for example, you may not have the inject call
but that's just because there's no real mechanism for it, not because we don't. We haven't chosen not to inject context. There just isn't a way to do it.
so that that's generally the way that I think about it. I've always been a little bit I've always thought that this was a confusing place
for our users, and I actually just ran into a situation last week where I was working with a user that was confused by the difference between internal and server spans, and when to use them
and because
at dynatrace, we do some slightly different interpretation based on that type. It was causing it to show up weird in some cases.
and I, I think that we should have more
specific guidance on this. You know, for example, I
are nested server spans allowed like what Trask was just saying, I think in some cases we certainly do it. But nobody ever said, Yes, this is a good idea. It's just that nobody ever said also that this is not a you know this is a bad idea. Nobody ever made a distinction one way or the other, and it kind of leaves it open to what people are just doing.
And it results in situations where people don't know what to do, because we never told them.
Trask Stalnaker 00:22:53 Just a quick addendum on that, Daniel. What we've done in the Java instrumentation is
we have a setting basically for people who want don't want to create those nested server and nested client spans.
Cause. Yeah, some back ends don't love that.
Yeah.
Daniel Dyla (Dynatrace) 00:23:18 Yeah.
Trask Stalnaker 00:23:19 But I agree it's something that.
Daniel Dyla (Dynatrace) 00:23:21 How do you tell your users? How do you tell your users how to decide what to set that setting to? I assume most people leave it as a default, and just wait for their telemetry provider to tell them they've done something wrong, and you have to go change this setting, assuming they know the setting exists, and assuming they notice that their telemetry is wrong, which only happens when you're looking into a problem, and you find you have wrong telemetry. And now you have no way to go back and fix your existing data.
I think the whole situation is is
convoluted. And also murky at best. Yeah. And I think it's also related to something that I know. Josh Mcdonald has worked on in the past. That never really got traction, but that it's like the
I don't know what to call it collapsing spans, I guess. Like, if you have nested server spans like, say you have some instrumentation that creates a span. That's an incoming Http call. And then you have a more like user, friendly
Http framework built on top of that, and they both create Http spans. Did those be merged together? Should those both be server spans, it's probably more common on client Http spans. But
those frequently result in like extremely confusing looking traces. If you don't know what you're looking at already, not like technically, semantically incorrect, it's not like the trace is wrong.
But when somebody looks at it and is like, why is this like this?
I don't really ever know what to tell them. It's because
of historical reasons, I guess historical baggage. But I think when everything's experimental, we don't necessarily want that to. Not everything experimental. That's not fair.
I think you guys know what I'm saying?
I think that there should be clarity here, and there isn't right now.
Liudmila Molkova 00:25:33 Yeah, Dan, do you mind if you want to create? I think this is the spec issue. If you maybe want to create one
that'll do one.
Daniel Dyla (Dynatrace) 00:25:44 Yeah, I can create a spec issue. I'd be shocked if there wasn't already one, since I know Josh Mcdonald was working on it, but I can. I'll look through what we have, and and if we don't have one, I'll create one.
Josh Suereth 00:25:58 We? We talked about that for like 3 to 6 months straight, there might be more than one issue, like I remember.
Liudmila Molkova 00:26:04 Like this is, I think there's on this.
Josh Suereth 00:26:06 Yeah.
Trask Stalnaker 00:26:09 It's a little while back. Yeah.
Liudmila Molkova 00:26:11 Yeah.
Okay. For the sake of time. We have a packed agenda. Let's move on, James. Do you want to talk about hardware vendor?
James Thompson 00:26:22 Yep, so so which? So there's an attempt to try and move the last of the hardware metrics across to being fully Yaml driven
right. One of the points that have come up is hardware vendor.
Should it be hardware dot vendor.
right or hardware.vendor.name alright.
There's 2 trains of thought, and it's the same for model.
Should we be delineating it by adding the.name on it alright?
And then, once we have decision that can close out the last of the open questions for those migrating, those hardware
metrics.
Liudmila Molkova 00:27:03 2 thoughts on this 1st one. This Pr.
I think we agreed last time that it's not
adding anything substantial or changing anything. It's just taking what we have in Yaml.
Sorry in Markdown and putting it to Yaml.
and I would be worried if we add any new scope to this Pr.
The second.
Alexandra Konrad @Elastic Security 00:27:30 Alright, that's what we that's what we discussed. And this like, I think what James against or like wants to
change is that we will have, let's say, just a model. And then we decide of the discussion that we would have model.name, and we will need to duplicate one and create another one. So I mean this direction. But from my perspective we should really not introduce any materials changes here, because this should be just the refector.
Josh Suereth 00:28:05 Yeah, I I'm gonna jump in. This is exactly what we talked about last week, and for the sake of moving quickly.
this Pr is not putting anything in a worse state than it is today. We have normative specification for the existing attributes as they are that should be considered normative and part of the spec. What you want to do here, I think, is it's good like, let's propose that. But make an issue, and let's do that in a follow up, not block this Pr, because the Pr is just right. Now we have a piece of our specification for semcom that is not in Yaml.
And so it's invisible to all the policies and things we do. And it's incredible tech debt right now if we leave it there. So let's get it into the yaml. So we can start actually having these conversations with the tools that we have. So that's what we want to have. So let's not block this. Pr, let's get the Pr. Through.
Liudmila Molkova 00:28:56 And the the second thought that I had is.
we have a group of people that seems to be interested to work to work on hardware, but we don't have a sig for it, and it would be
interesting to try and form a Sig. If if people are ready to commit to working on it, and then you can have those discussions. You can come, present
them to the general semantic conventions.
We have a process on establishing a seek it should be in the contributing guide.
Sorry it's there should be a link in the contributing guide.
right it stands for the Pod project management. You would start the project and the community. You would need some sponsorship
and we might need somebody from semantic conventions, from the Maintainers, at least to sponsor this effort.
So I think the hardware scope was large enough
to for us to have a group working on it.
And I wonder what other people think.
Okay, so I don't hear any disagreement.
I wonder if we should.
Say that we are not going to work on the hardware except basic refactoring. Sorry except basic
moving things to Yaml. Unless we have a group formed.
Alexandra Konrad @Elastic Security 00:30:52 Yeah, let's let's finish this one. And I think
Bertrand was also interested in to updating it. At least he wanted to have some follow up. Prs.
so, yeah, this could be done if the people would organize the new community like New group
for hardware. But my point was, I just wanted to finish up. This was the last piece from our yeah
work to move things to the yaml file.
Joao G. (Dynatrace) 00:31:30 Yes, I I I saw that. There's the
I didn't in the agenda about the prototyping requirements. Yeah, thanks for putting that together. I just 1st I I didn't see that was in the
agenda before I merged, but I I saw there was many approvals, anyway. But about this thing about the hardware and defining Sig. I think that's I mean what we have been discussing this triage issue management for quite a while, and I I put together a proposal share with
with the group tomorrow. Once I clean things up but that's the direction that I I wrote more or less that we will.
we should probably block or not working. I don't know infinite amount of work streams and not get anything done.
so I support that we
don't. Don't, don't do anything new, and just maintain it, for now, until there is a proper see established.
Josh Suereth 00:32:32 Cool. So it sounds like we all agree that we want clear ownership for hardware before we start to make changes. But changes like this should be put into a set of issues that that group could execute on that sound like a path forward.
Cool. Let's move on.
James Thompson 00:32:49 Yep.
So the
the next one alright. So I've started trying to create more automated, generated documentation. Right? So the 1st one I've looked at is events.
right? Because currently the events example is scattered all over the place.
All right.
So if you just open open the top top one in pretty view, please.
Alright, so similar to Josh's page. But if you click on the namespace on the left hand side
alright, say, for example, Gen. I. Gen. AI.
The left hand column, please.
Liudmila Molkova 00:33:32 Do you want to present? Maybe.
James Thompson 00:33:33 I'm on my ipad, so I can't. It's hard to present.
Alright. So if you, if you just click the namespace on this page here.
Alright. So what you have here is a list of all the events with the summary okay.
and that events section be can be collapsed as well.
right. So the 1st question is.
do we see benefit of having this page here, with a section for events.
your entities all grouped together? Right? So that you can go. Gen. AI. You can see what entities there are, what events there are, rather than having them as 2 separate big, long lists.
Alright. And then, once you go here, then you can drill down to the details about the individual item.
That's a that's probably the main thing.
Alright.
I'm interested in getting feedback on.
Josh Suereth 00:34:30 So I I commented on your Pr, I'm gonna jump in quick. Thank you for pushing forward registry because I think we do want to build a registry for all the signals over time.
The, I think there. There were 3 things that in this one that I think I called out. The 1st one is what you mentioned, which is like having one, each event, an individual markdown file. I actually think, looking at it, I like how that looks so. That's number one is like understanding that the second piece it's it's in the over. If you want to see my comments with Mella there, at the very bottom. The second one is basically we want to make sure this is linked to from the top level registry as well. That's a minor thing.
But the 3rd one is this is looking for things that start with event, which one of the things that I saw with the the several Prs that you had around registry work was splitting events and logs. We do not want to do that. That's like a thing in semantic conventions. We want all, all logs or events to be find as events right? So
we need to find a way to have a registry of things that come out. The Otlp log channel.
and that's something that I'd like for us to kind of sort out. I think I understand why you have like events and log events kind of split. And this is something, maybe, that I'd like to spend a little bit of the 10 min here discussing within this group. You know, if we're going to have registry, how do we want to handle in semantic conventions a registry for the log signal? Right? Do we want? Do we want to have it by event, name.
And then what do we do about things that don't have an event name because they are a traditional log? Are those defined in some from my understanding. We're not defining anything like that anymore. Right? Okay.
James Thompson 00:36:19 We currently do have some examples of that.
Josh Suereth 00:36:23 Right? So so what do we need to do with those examples is, then, is the next question. So do you want to walk through those examples.
James Thompson 00:36:30 Yep. So I think the the clearest example would be the cloud events example, all right.
If you look at the specification out. That's currently defined as a span.
But there's no span name, no span kind, none of that. It's just a group of attributes that you can put on your messaging span or your Http span.
Right? So that's a clear case of a group of attributes which can be added
to a log event. You can add it to your trace, etc.
Liudmila Molkova 00:37:01 And that's not a telemetry item definition. And I think that's intended this way. We don't have logs in semantic conventions. We cannot define a log in semantic conventions.
James Thompson 00:37:14 Alright, but if you have a look at the cloud events, example right? All right.
Liudmila Molkova 00:37:21 Yeah, we have a bunch of attributes that you can record anywhere. There are code attributes. Cloud events are one of this. Let's talk about what we have as logs and semantic conventions today.
James Thompson 00:37:34 All right, but when you description says, for cloud events, all your feature flags. It says that this can be a log
right. These can be recorded on your log as attributes or as a log event.
Liudmila Molkova 00:37:48 Then the the event is not defined in semantic conventions for cloud events.
James Thompson 00:38:01 Alright. So the the question comes, how would we describe this scenario here?
Alright!
Liudmila Molkova 00:38:07 We don't residents yet until somebody does.
James Thompson 00:38:10 But but this wouldn't be an event.
Josh Suereth 00:38:13 Right. It's it's not an event today, though, in semantic event, like again, this is not modeled as an event. Semantic conventions. This is modeled as a set of things that you would use to take cloud event like information and throw it into a span.
James Thompson 00:38:26 Yes.
Joao G. (Dynatrace) 00:38:27 No.
I can give more context because I wrote this part. So this this is this is basically how to model cloud event spans. So it's like a layer on top of anything else. And there's some instrumentations that generate cloud events and send cloud events.
Vhtp, and these are basically meant to stamp the spin or or those those spans coming from that. Those instrumentations with these attributes.
So those those are not meant to be events or anything. It's just
attributes to put on this PIN. They, they even are, are classified as the the fires, as called events touch spins, and so on. So
no log, no, no hotel event
just attributes to put on the skin like like we have for other things as well. Yeah.
Josh Suereth 00:39:23 Right. So if we had a span registry, this would show up in the span registry. Right, Joe.
Joao G. (Dynatrace) 00:39:28 Exactly. Yes, correct.
James Thompson 00:39:30 But would we really be creating a span for each time we get a cloud event rather than just adding that to the Http span those attributes.
Joao G. (Dynatrace) 00:39:41 Yes, it depends on what the instrumentation wants to do right. So at the time when I wrote this, there is a instrumentation for go for Http, which we're already generating the
spans and attributes. And this was basically only to form for formalize the the attributes are defining conventions.
That was the goal of this document, basically but then, at the moment we started at the moment we started, the messaging sick was basically at the same time. And
I believe that at some point these will probably merge with the messaging conventions because they're
pretty much most of the time tied together. So maybe this will even go away. This entire page, for example.
it might be like we have rabbit, and so on. We might have another another.
let's say, messaging provider, or something that
these attributes are stamped on messaging spends, for example, not on as standalone spends or Htp, whatever yeah.
James Thompson 00:40:47 But cloud events works across your messaging your Http and your Grpc.
Joao G. (Dynatrace) 00:40:53 Exactly. Yeah. So that's that's why they are like this today. Maybe we will change. I don't know. Yeah.
Liudmila Molkova 00:40:58 Can can we park this discussion? I think the event registry is orthogonal to cloud event, specific story. I'm going to create an issue to update some spans like the the span terminology we use around it because it's an attribute group today. So let's just.
James Thompson 00:41:13 We can have a separate discussion about that.
Alright.
but I think the key thing I'm looking for feedback on is, if you look at the example page, do we see benefit of having one page for the namespace which lists the events and the entities, and then click, being able to select which event or entity you want to look at.
Josh Suereth 00:41:36 So I also asked this, why is entity in here? Entity has its own registry.
James Thompson 00:41:41 Yeah, right? So that's coming to this question here.
should we? So if you look at the page that listed
all right, so can you click on Gen. AI on this page.
Josh Suereth 00:41:55 Yeah, yeah, I I like this page. I think this makes a lot of sense what it was. I don't understand where entity is coming in here.
James Thompson 00:42:02 Yep. So where you have the events option above that have an entities option. So you can go to the Gen. AI. Page, and you can see your entities, you can see your metrics, you can see your events.
That's where it's coming.
Josh Suereth 00:42:15 You want like a namespace registry that would be across all signals. So like entities, events, spans, they would all show up in that. Read me. Okay, that's fair.
I think.
where that belongs. Then, because I don't think that should be in the same directory as all of the events. Necessarily but these are all detail. Okay, I I understand what you're going for now, we
we some of this, we can take onto the onto the Pr itself. So I think the main thing to to ask right now 1st of all, is like, do we want a an event registry? I think the answer, probably resoundingly, is, yes, because we're working towards registries. The second thing is, in the event registry. What should you include in the event registry? And and my argument would be for this Pr, it should include everything we're group type
or or is event. Every single one should go into this.
James Thompson 00:43:06 Yep.
Josh Suereth 00:43:07 Cool. So then the 3rd question would be the structure and shape of this, and I think that we should take that on to the Pr. Because I think that we don't have time to really go into details here. Does that sound fair.
James Thompson 00:43:18 Yep.
Josh Suereth 00:43:18 Cool! Go ahead, Lumilla.
Liudmila Molkova 00:43:20 I have a big question we would. With this we would have duplicate definition.
One definition is in the corresponding document, let's say, Jenny I.
And another one is here, and those are duplicates. But as we know, we don't do everything we can today to define things in yellow. So, for example, events have requirement level
and we don't write it here because it's not in the ammo, but it's somewhere inside the
semantic conventions for genes.
and those 2 are the same, but they are somewhat conflicting or incomplete. In one place I hope we
have some means to not duplicate stuff.
and I can see a few options. Either we will define things in the registry, and then we will
put a link into the original place in the original semantic conventions where it's defined.
or we will figure out something else.
But duplication is not perfect.
James Thompson 00:44:43 If if I understand you correctly, I think the key thing is when we start releasing more registries, we need a way in which the old pages can be deprecated. Is that is that effectively? What you're saying.
Liudmila Molkova 00:44:55 No what I'm saying that
we should not have duplicated definitions. Now we have definition rendered here, and another definition rendered in the Gen. AI. Docs.
Josh Suereth 00:45:09 Yeah, for for some added context, one of the one of the tasks I'm working on now from the entity registry is to start moving all of the content from the resource folder into the entity Yaml. So we can get rid of the resource folder
right? Because today entities and resource are duplicative of each other, and the real source of truth for the data is the resource folder with Markdown, because there's so much additional content in the Markdown that we're using for normative language, that we have not fully moved into the Yaml for the auto-generated language, and we are moving towards auto-generated language. But this is like back to that discussion around hardware things right?
The the source of truth is not the Yaml, it is the markdown.
That's where all of our normative language is today in semantic conventions. We want to get it into the yaml and get it automated. But it's not fully there yet. And so with this pr
of making the registry right. And that's 1 reason why we have the. This is a work in progress, and things might change. We also need a whole workflow to start moving. This content here, like what Ludmill is showing of shoulds and musts find a way to get it into the yaml, so we can register it. So, making the like that would be like in my mind.
and what we did for entities. You can. You can use this as a template. It's just there's more work for events.
we create the registry. We make a list of the differences in some sort of tracking bug, and we start executing against that tracking bug in an ongoing basis. So it's not just we make the registry, and we're done. It is a journey right? So. I'm fine personally going on that journey, and I hear your concern, Lydmilla, of like. If we make the registry.
there's a question I think you're asking here that I'm going to explicitly say of do we have enough
in the Yaml
that the differences between the Markdown and the Yaml won't confuse people if the registry shows up today. That is a question I don't know. The answer to. I'm sure you do is like working on more of the event stuff, but that's the thing we'd have to sort out before we we commit to like merging the Pr. But I still think we should work on the Pr expand the Pr and start making changes based on what we see in the Pr. Is that fair.
James Thompson 00:47:36 That's fine with me.
Liudmila Molkova 00:47:39 Sounds good.
Josh Suereth 00:47:44 Do you want to walk into specifics with Mela like, do do you want to go into any specifics of things? We need to move or.
Liudmila Molkova 00:47:51 So the the 1st step, I think we should do.
we should go through the places which define events, and to remove the duplication. So instead of doing this, we should say, Okay, it's actually defined in the registry. Here is the link to the registry.
James Thompson 00:48:08 I think that's good.
You happy for that to be in the same Pr.
Would that make things clearer? So that way you can go to the Gen. AI. Events page. And you can see, okay, this information's been removed. It's already in the registry. Would that make things easier to to review.
Liudmila Molkova 00:48:25 I think it would demonstrate the completeness of the.
James Thompson 00:48:28 Yep.
Liudmila Molkova 00:48:29 Story.
James Thompson 00:48:32 That's fine!
Liudmila Molkova 00:48:33 And then it would still be. There would still be a small pieces. So, for example, there is the
the giant note. Here we have plenty of them in semantic conventions.
Should we put them in every place where, let's say Gen. AI, or we have similar? Not, let's say, and the messaging is defined. We talk about span registry
we now control where the things go.
But was the span registry? We would need to define where to put this blurb
and find a way to put it in the.
We're just 3.
James Thompson 00:49:16 Yep. But I think that also applies to entities. But yeah.
we we as Josh and that's have said we need a way to work out what content needs to be migrated. And that's a project, right? And that's fine.
Liudmila Molkova 00:49:29 Yeah, the problem is that today, when people interact with this, they go to Jenny events.
And this is, they know that if they are implementing instrumentation. There are some additional concerns they need to think about.
James Thompson 00:49:44 Yep.
Liudmila Molkova 00:49:45 If they just go to this document, sorry wherever it was.
they will not know that there are some problems and constraints that they need to be aware of, and we have no means to express them.
so they might get confused, and they might not understand what's going on.
So we need to, I think in. I would
would rather us 1st figure out how we work through this, and then work on the Pr. Than the opposite.
And we can. We can absolutely keep working on the Pr. But we should consider the draft.
and I think we should start with one either events or spans or metrics, but not those 3 at once.
James Thompson 00:50:41 Yeah, it's it's only events. Events, is a events, is a standalone Pr.
Liudmila Molkova 00:50:46 Okay.
So let's consider the draft, and let's actually work through the details of what is not there. But and it's confusing. I think this pieces of text
are important. One of them says that you have to guard this events with a feature flag. You cannot renew them by default, and things like this should be there.
James Thompson 00:51:11 Yep.
Josh Suereth 00:51:15 Quick question. Do you think metrics is in better shape? Because I I don't. I think all instrumentation spans, metrics and events all need that header. So I don't think I actually don't think there's a better one to start on
from my perspective. Yeah, okay.
Liudmila Molkova 00:51:32 There is a worse one. The spence is the worst one right?
Metrics and events are pretty much events are smaller, so there are fewer events that we have. So probably events is the best thing to start with.
Okay, James, do we? Does it sound like a plan? Do you feel we can make progress like this.
James Thompson 00:51:58 Yeah.
Liudmila Molkova 00:51:59 Wonderful
I'm going to write a few notes Josh, do you wanna talk about this change? Do you want me to present. Do you want to present.
Josh Suereth 00:52:11 No, this is this one's kind of dead simple. I don't think we even have to present. So basically, it's a, it's a pull request where we're going to try to create a new directory called how to contribute, and so contributing Md. Would link to that how to contribute will have the like
how to create semantic conventions. Guide. It'll have some of the guidance around how to think about making semantic conventions, how to approach abstractions like the need for prototyping requirements. All of that would kind of be in there. Apparently.
I mean this. This Pr already has enough approvals. So I'm going to let people know. James raised a good question of like, what should the name of this be? I want it to be something I did some research into what Github recommends for documentation of this sort, and they actually recommend either putting everything in contributing Markdown
or creating a Docs folder with all this information is, but we already have a Docs folder, which is our normative guidance, and we want to put it somewhere else to be more explicit and kind of in your face. So right now, it just proposes how to contribute the reason I'm advertising it. Here is we're moving how to contribute out of General Semantic Directory into this new how to contribute directory.
And I want to start putting more guidance for people on how to think about writing semantic conventions. So those of you who have stabilized like the Http folks. Database folks feature flag folks. I want to get the like. The the
business of defining semantic conventions into this directory over time we put the resource and entity modeling guide in here. The readme is the file that used to be called how to write semantic conventions, and I'd like to kind of expand this over time. So this is kind of a hey?
This Pr is approved. I'm planning to merge it relatively soon, and I'd like to get more content into it. I, personally don't really care what the name of the Directory is outside of that, people see it and find it. So right now, it's where Github basically recommends it's in contributing. Md. Has links to it.
And then it's in the Docs Directory, which is where Github recommends having contributing docs. So.
James Thompson 00:54:24 Josh. My actual question was about putting it on the open telemetry dot I/O website under contributing folder.
Josh Suereth 00:54:32 Oh, I see.
But that's why I put the links to the open to telemetry website in the comment.
I'm happy to actually add it there the way the way open to pulls in content. We'll have to talk to them about whether or not we can get them to pull it from us. I
the source of truth. For this content I want us to own as a group and approve a semantic convention. Maintainers put in an open telemetry. I/O
is good for discovering, but bad for the approval standpoint, because the the content and ownership now becomes the the web folks, which is fine, except I want us to prove we've agreed to it first.st So I think that's a good idea. But we'll open a bug to do that the way they pull in semantic conventions is they actually pull in our repo and move things around into the opens on trial. We can open a bug to see if they can do that for contributing as well.
James Thompson 00:55:23 Yeah, that's where I was actually heading. Because currently, it's buried under specs and all that.
Josh Suereth 00:55:29 Oh, yeah, like, like, where I see.
Yeah, I absolutely agree. I'm more worried about like, open to lunch. I always see someone consuming semantic conventions. Github is where I see people contribute semantic conventions. So I'm more focused on the Github
based thing. But it's a fair point. Anyway.
I think I took.
I'm trying to stay under 5 min, please. If you have contributed semantic conventions, if you have guidance and things you've learned, let's flush this out together. Let's feel free to make Prs in this Directory feel free to expand sections. Actually, Lamila, there is one thing I do want to show
which you showed, I think, 6 months ago. If you if you open the Pr
and you open the how to contribute readme.
This sec. This readme, I did not change the document. If you expand it.
you will click on defining spans. For example, see how it's Tbd.
Liudmila Molkova 00:56:32 Yes.
Josh Suereth 00:56:32 Metrics is Tbd, it was Tvd before this. It's TV. After this. Pr, this is where I'd love help. So that's why I'm advertising like. Let's let's get the business of writing semantic conventions written down and guiding people. So those of you who've done spans, metrics, events. If you'd like to propose things here. Let's get stuff written down to help people.
That's the end of my spiel. Thanks, everybody.
Liudmila Molkova 00:56:58 Thank you for doing this.
We are almost out of time. I wanted to get
thanks for Joe for merging it. So we've been discussing a lot of things recently, the new things.
and one
practical aspect of what we've seen in the past, that defining conventions without actual and writing. Actual instrumentation is difficult.
It's very theoretical, and it needs some reality check.
So what we have merged, and I wanted to share it before we merged it. But anyway, it's there. So
we have now a new section in the pull request template
that asks for links to prototypes or instrumentations.
and we strongly recommend coming with new additions, with new features, new conventions especially new areas with prototypes.
Looking at the change log, we had very few contributions recently that didn't come from the prototypes that were not trivial. So this should not change the practice. It changes the rules, though.
and you. The rule was that we required prototyping for stability. Now we are going to strongly recommend it for the
initial stages of semantic conventions implementation.
And that's the change
we don't really have time to discuss this. But if folks have any concerns with this, or if you see Pr, that need that is now not following this requirement. Bring them on. We can discuss it. But the
general
idea is that you probably should start working on the prototype. If you want to merge things to semantic conventions.
cool. Thanks a lot. We are out of time. We haven't got to the 2 things on the agenda folks. If you wanna ping us on slack share some thoughts go ahead and let's make sure we get it into the agenda next time
or unless it's resolved. Before that, I'm going to put it here. And let's see.
Okay, thank you. Talk to you later.
Trask Stalnaker 01:00:02 Bye.
