SIG: Semantic Convention SIG
Date: 2025-06-23
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Josh Suereth 00:00:53 Hello! Everybody!
Braydon Kains 00:00:56 Hello!
Trask Stalnaker 00:00:57 Hey!
Josh Suereth 00:00:58 How are we all doing.
Bruno Baptista 00:01:01 Hello!
Trask Stalnaker 00:01:02 Happy. Monday.
Alexandra Konrad @Elastic Security 00:01:04 Oh, yeah. Mike.
Liudmila Molkova 00:01:05 Happy. Monday.
Josh Suereth 00:01:08 I might run the meeting unless one of the other Maintainers wants to, since I haven't done it in a while. And I okay.
Liudmila Molkova 00:01:16 Go for it.
Trask Stalnaker 00:01:17 All your.
Josh Suereth 00:01:17 Take my turn in case I'm missing a few others. Yeah, all right. So let me put next up here.
Let's do attendees, and then.
alright, so feel free to add your name to the agenda or or yeah to the meeting notes can't type today.
Let's get this going. I'm not presenting yet, am I?
Liudmila Molkova 00:01:49 No, you're not.
Josh Suereth 00:01:51 Okay, I got it. One. Sec.
Okay.
Alright. How are we doing there?
Trask Stalnaker 00:02:06 Yeah.
Josh Suereth 00:02:09 Okay.
Cool. Trask.
Trask Stalnaker 00:02:17 Oh, we haven't done this yet. Alright cool and so the Gc. And Tc. Are collecting feedback track.
and to put together sort of a view of what's happening in open telemetry.
and so collecting just some basics from each of the Sigs.
And I know this Sig is a little bit unique in that. It's a general Sig. And most of the work as happening in the semantic convention. Specific Sigs, and we are capturing those sigs separately. But I do think there's, you know, some things probably worth calling out for the general sake.
So I 1st the sort of maybe big things that happened in the last year in this sig.
Any thoughts.
Josh Suereth 00:03:39 From my perspective. There's like way too many. So I'd have to go look.
just because we have so many individual Sigs operating so a question on scope for this right? Do you want us to think about semantic conventions as a whole? Or do you want us to think about like the infrastructure and process around semantic conventions.
Trask Stalnaker 00:04:00 Yeah, I I do think it's tricky for this Sig in particular. Because we are capturing. I mean, I guess we could. At least we could capture from Sigs that have closed down.
So we don't have like we're not.
We should capture the database, semantic convention stability.
We should capture code, namespace, stability.
Liudmila Molkova 00:04:32 Feature flags, not stability, but pretty much.
Trask Stalnaker 00:04:36 Part of it.
Did they do? Rc.
Officially? Rc. Or just kind of.
Liudmila Molkova 00:04:43 So.
Trask Stalnaker 00:04:43 I see.
Liudmila Molkova 00:04:44 Let's see.
Josh Suereth 00:04:50 Pretty sure it's Rc.
Liudmila Molkova 00:05:03 Yeah, they declared. A bunch of attributes as Rc. And events, event.
Trask Stalnaker 00:05:18 So, yeah, and I know a lot of the process. Level stuff is being captured in the weaver. The tooling Sig, specifically.
okay.
Liudmila Molkova 00:05:29 Specific.
Trask Stalnaker 00:05:31 I mean around infra kind of the the semantic convention infra structure work.
Liudmila Molkova 00:05:40 Oh, okay, yeah.
Did we discuss it in the scope of fever? I don't think so. Did did we?
Josh Suereth 00:05:47 There there was a I don't think I don't know if you were on it. There was a a chat message that we all talked about.
Liudmila Molkova 00:05:54 Okay.
Okay, wonderful. Yeah.
Josh Suereth 00:05:56 I think it was with it was in the Gc. Check-in with Maintainers for Weaver, so I do think that your feedback would be valuable as well. I'll add you to the slack chat in case you missed it.
Liudmila Molkova 00:06:11 I'll find it. Don't don't worry.
Josh Suereth 00:06:13 Okay, I think it was in the Weaver Channel.
Liudmila Molkova 00:06:17 Trying to cute.
Trask Stalnaker 00:06:18 I posted. Yeah, I posted it in the the Public Weaver Channel originally. And then I think I went to the Sig meeting. Yeah. 2 weeks ago.
Liudmila Molkova 00:06:31 Right. No, no, I was there. I was just not not woken up. Yeah. Sorry.
Josh Suereth 00:06:36 That meeting is before coffee. That's the problem.
Trask Stalnaker 00:06:39 That's it.
Josh Suereth 00:06:41 One C meeting. You know what I mean.
I think.
Liudmila Molkova 00:06:45 There are new conventions. Maybe we should call out Cicd. It had a lot of feedback, and from the from the industry.
Trask Stalnaker 00:06:58 Yeah, I think Cicd should be getting captured separately.
Okay, since it's a it's a sig on the just confirming on the community. Read me.
Yeah. So Dan is the Gc. Liaison there, so he'll be capturing that.
Josh Suereth 00:07:21 Yes, I I was just looking through notes. I feel like if you look at the goals of the different Sigs, and what what we do as a group. And you look at our charter for our working group. The the goal of this working group. And the reason the tooling kind of split off was, we focus on the process of defining telemetry and like making sure the the ecosystem is healthy, and they can ask general purpose questions and make general semantic conventions. So I think one thing that we could probably call out here. Sorry I didn't. I wasn't rendering one thing we could probably call out, I believe some of our guidance has been updated, and we've been making progress there. I'm just trying to pull up our like, our non normative section has started to flesh out. And I think that's been helpful for everyone. So there's a what do we have? We have code generation guidance we have the migration guidance. For how people do that? We have naming exceptions guidance now, and I think we're starting to like get a better handle on the weirdness and semantic conventions. I don't know if that's worth calling out, but from a process standpoint more is getting written down.
There work in, and I always forget where this is.
But.
Liudmila Molkova 00:08:39 It's in the dogs, General. We probably should move it.
Josh Suereth 00:08:43 Yeah, there's this stuff here, how to how to define semantic conventions, this one, right, this this work, I think we probably want to call out of, like the the business of making semantic conventions. We've had more and more guidance, and and like docs on how to do it.
I I think that should probably get called out because we've made the past year. I think we've actually gotten to the point where I'm seeing less. How do I even do this and more. I have a weird nuance thing we've never heard of versus like I can't do it at all before it was like, Hey, how do I even do this? To begin with? Now we're we're we're really narrowing down so.
I don't remember when this was last month, apparently cool.
Trask Stalnaker 00:09:28 Is that? Are there other things under general there that are worth or sort of is kind of all those sorry I can't see
Josh Suereth 00:09:39 Oh! Like.
Trask Stalnaker 00:09:40 Yeah, lots of.
Josh Suereth 00:09:41 As you mentioned some of the naming stuff we've done some updates to naming around guidance with with stuff we did recording errors, I think, is still in development and needs.
I think Ludmila has work on there that we should probably talk about. That's like that's something that I think the general conventions has.
This notion of semantic convention groups, and what they mean. And stability did this change at all?
Liudmila Molkova 00:10:10 It's a relatively, I think it's past 12 months, for sure.
Josh Suereth 00:10:14 Is it?
Yeah, yep.
in any case like these, these things that we have, we? We now have like process in place to automate this guidance. So it's not just in in words. I think that's that's been the focus. There's a few chat messages. What else do we have?
System has already been asked and provided some items separately as well. Yes, agreed. So so I think that's what I would focus a lot of what we talk about from this group on, for in terms of achievements so.
Trask Stalnaker 00:10:54 I'll take that as a follow up. I'll go through the non normative guide guidelines and those general docs and pull out stuff that's very helpful thanks, I think, in for interest in time. For upcoming 12 months.
I think it's worth putting again.
simcom Sigs, that we don't have the Sigs yet, for so we're not capturing that elsewhere.
Josh Suereth 00:11:23 Okay.
Trask Stalnaker 00:11:25 Tc. Security.
I know we're trying to kind of reboot security.
Liudmila Molkova 00:11:38 There will be again. We were capturing it in the tooling, probably, but I would imagine a lot of automation around code generation and for the the work that Josh called out the Meta guidance. It's it's just started right. There is, I think, half of it is Dbd, so we will keep doing it. I hope so.
Josh Suereth 00:12:06 Yeah.
Trask Stalnaker 00:12:08 Yeah, yeah, there's I agree, that's a good area. Still.
Josh Suereth 00:12:15 And I still.
Liudmila Molkova 00:12:17 Hope that I think there have been conversations about system and process stability sometime soon, and Kubernetes. I hope this, we can put it on the. But again, it's not in this Sig.
Yeah.
Josh Suereth 00:12:32 Yeah.
Trask Stalnaker 00:12:34 I was gonna add.
Josh Suereth 00:12:36 Oh, yeah. Triage is.
Trask Stalnaker 00:12:37 Triage process. We need to.
Josh Suereth 00:12:40 Get some more work there.
Trask Stalnaker 00:12:48 yeah, just calling out that the repo has become very.
It continues to become more and more active.
okay, I think in interest of time. Let's let's move on. I think this is enough for me to kinda pull stuff out from.
Josh Suereth 00:13:21 Alright so let's do So are there any areas or sub projects Gctc. Can help with cross Sig blockers, prioritization, etc. I do think one thing I want to call out is just what one of the things we're struggling with.
that I've noticed is general maintainers and approvers. I think it's a hard job.
Those of us who are general maintainers have a lot of load from semantic conventions, and where there.
where there is a Pr. That doesn't have a Sig or a set of approvers for it. Those Prs take the longest, and I think partly it's just as a general maintainer. You have to have so much that you're like managing and approving that it takes a while to get through. But I I think we need to sort out some sort of a process to move those Prs through or a way to advertise like hey semantic conventions could use more general maintainers or approvers.
Liudmila Molkova 00:14:36 Where we should have a better scope, but a scope defined better and say, Okay, we are not taking the Prs that don't have a corresponding seek for them.
Josh Suereth 00:14:48 I I think that's fine as well. Yeah.
I'm more thinking, like some of the some of the the things that that aren't like directly tied to.
I'm actually thinking of this entity modeling guide, for example, or the Prs where we change policies. It actually takes really long for us to get those through when I don't think they're contentious both when you do it, Ludmila, or when I do it, because if one of us does it, the other one can only be one of the 2 approvers.
Right?
So some of the process related work, I think, takes a while. You like. I think, Joe, you're on the call, too, I think when you've done process work sometimes it's been very, very non-contentious, but by the time I get to look at it.
It's already been like 2 weeks, and it would have been awesome if I had just approved it. Day one, if I knew about it right. I think we need a better process around some of that.
Trask Stalnaker 00:15:46 Yeah, I mean.
I would like to. I'm kinda interested in thinking about the triage process in the next couple of months on.
because the when we're getting so many that I just kind of sometimes I just drown in it.
Versus. If there was a way to like a lot of them don't need my, there's nothing to do on, because they're you know, they're being worked through a Sig, etc. If there was a automated way of like.
Here's the 2 Prs that I should look at today. Would help me to focus on on that.
Joao G. (Dynatrace) 00:16:46 Yeah, I I think that we still I mean, I had this idea. I think somebody posted in the slack channel some some time ago that we we needed to establish some process like for issues and Prs assign labels like the workflow or the the yeah, that they they implemented in the spec, I think, Jack, Jack Burke put something together that I really liked it. I really wanted to establishing in our seat as well.
What I yeah, I've been doing like on and off. I I take some hours during the day to go through the issues and then label them or move them, or assign them to 6 stuff like this.
but like, you know, I think, like Mila said, there's some some stuff that I there's no sync, and like there's no proper way to say No, we're not taking this, I mean, like, this is interesting, but we don't have the bandwidth now, like there was some the other day. There was some issue about cost about estimating cost of requests or something, or some other thing that it's like, it's really cool. But yeah, like, we don't have to benefit. So yeah.
so like, I think all in all, just to say that, yeah, we we could use a more structured triaging process, more strict even.
Josh Suereth 00:18:15 Absolutely agree. Alright, it sounds like in terms of areas and sub projects that we need help with basically triage process. We need to work on it, and we could use advice or help.
or things that work in other ecosystems. Yeah, cool.
Alright, we're well over the 10 min. But I thought that was really good discussion. So it's gonna give it some more. I'm just checking quick to make sure. Yeah, I don't think we're gonna push anything out? Do you have everything you need trust?
Trask Stalnaker 00:18:45 Yeah. Thanks.
Josh Suereth 00:18:46 Okay, so the next one is, basically last minute thoughts on the entity modeling guide. This is one of those guidance documents we're talking about. This one has enough approvals. It has approval from the Sig. The entity Sig.
So I think it's ready to merge. Just wanted to see if anyone had last minute thoughts before merging it. This is mostly an Fyi. I plan to resolve comments that I think are resolved that the author of the comment hasn't gotten back to me on and then merge later. So cool. Let's move on, Alexandra. Question about metric names go for it.
Alexandra Konrad @Elastic Security 00:19:28 Yeah. So I was continued to move hardware related metrics. To the own files.
And like, there was this question about names where we have similar to the one I posted in the chat in the in the discussion. So dot CPU speed and dot CPU dot speed dot limit. So before we had this notion that you cannot create names that collide with namespaces, I have checked and couldn't found it, and it was removed in the pull request I mentioned. So 1st question. Then do we still have it? Because I was under impression that we cannot create the names that collide between altogether. So if we have already speed dot limit, we cannot create name that adjusts speed.
So, and like the 1st question, do we still have that restriction, or it it was lifted in that pull request. Maybe it was just missed out. I'm not sure.
Trask Stalnaker 00:20:40 So from what I remember. There's it was a open question still whether we wanted to enforce that or not.
and in the meantime we sort of were softly enforcing it like to, so that we could Make that decision still.
That, said I. I with the attributes we'd don't want this right. We don't want attributes for CPU speed and CPU speed dot limit, and that's we have a very concrete reason for that which is we want to have a we want.
Does flattened attributes to map, to be able to have a canonical mapping to complex attributes or object style like a Json structure.
And so we can't have CPU speed equals 5, and then have it be an object with a nested limit at the same time.
I don't think we have any. The only reason that I can see for doing it on the met that I'm I'm aware of on the metric naming side is just from a ux perspective, like displaying all your metrics.
A list of all the metrics in a hierarchical form.
and it's kind of nice not to have like nodes sometimes be metrics, and sometimes not but I don't think that's a super strong reason.
Josh Suereth 00:22:35 We have, we have an issue with entities, if this is related at all to them, where, if the CPU speed limits reported on an entity as a attribute, and then we want to turn it into a metric. You now have the issue where, like the metric in the the namespace, could be like broken I need to sort through if I figure out how to describe that better. But basically, like both of these metric names might actually be attributes on an event. Right? And so, if they're attributes on an event, you cannot define them appropriately. So if we do a attribute to metric conversion, where, we say attributes on this event should be aggregated and turned into a metric which is a realistic thing. That we would have this metric name would be broken and so like, yes, we kind of removed it. But we also kind of weren't sure if we needed or not.
This this is exactly the use case that that would break if hardware speed and hardware limit come out as events, we aggregate them into metric. We now violate our own naming principles.
Alexandra Konrad @Elastic Security 00:23:44 It's not the only case there are like multiple metrics with similar product, like similar rule, like we have just the word. And then we have word dot limit until like temperature, for example, limit, etcetera. So there are a lot of metrics in hardware space that are following this. Yeah, this guideline. And I have asked also, but so he is also on the call. So to understand how break it, how breakable it would be if we now will change. Those metrics are already in use like to different names, and I'm not sure what is the base best outcome here.
how should we proceed?
Josh Suereth 00:24:29 Yeah, I'm just going to say that basically, all of those violate the other areas of semantic conventions where we have limits.
So so again, hardware looks different than all the other ones, and I'm not sure how we got into that state. But that's something we will have to figure out and address. But yeah, everywhere else you have dot limit. You have dot something else like dot usage dot request like, if you look at Kate's, so we do not allow this in other places in semantic conventions today, and it does look different than how semantic conventions are. The mill. I jumped in line.
Liudmila Molkova 00:25:03 Yeah, no, I was going to bring up something similar that maybe Brayden can help. We have a bunch of this and system and process where we do think usage or utilization.
or current or something. And I wonder what should apply here. I also think that just from from the reader's perspective hardware. CPU speed, I don't know. Current would be more understandable than just speed.
Yeah, that's it.
Braydon Kains 00:25:44 I don't know if we have any examples of the the namespace clash thing that's going on here. We do have examples of like the We have a dot like a dot usage or dot utilization or dot something or other. But the the actual namespace clash doesn't happen in the in the case of of for hardware hardware dot. The the one i i was looking at was the battery charge. One hardware dot hardware dot battery, dot charge and dot battery dot charge dot limit, I think, and I guess like charge dot current is also fine.
The I mean, maybe electricity is weird, like a chart battery has a current of electricity flowing through it. So is that weird? I don't know. Maybe that's probably an unfounded alright.
I've I feel like hardware dot battery. Dot charge is is a good name.
and same with CPU speed, and the the limitation of like having another metric forces it to be a namespace other than now. I understand that that breakage, that of the attribute metric conversion that I didn't think about before. Like it. It seemed to me like it was a fine name. That's why I suggested. We like revisit the the principal.
Josh Suereth 00:27:21 Oh, go ahead! Who's next? It was either Bruno or Bertrand.
Bertrand (Sentry) 00:27:26 Reno is first.st
Josh Suereth 00:27:28 Okay, go ahead.
Bruno Baptista 00:27:29 Okay, Hi, so I just left a comment on the on the issue because, I was going to suggest that we use, probably, or get some inspiration from the car battery metrics that are used in the canvas from from cars.
They define things in a very precise way, so the capacity, the current capacity, state of charge.
So they always do state of this state of that depending on the current value, and this actually distinguishes between the the factory, the manufacturing values.
In in the specific case of the charge there's also a problem with degradation.
and they have a value for that which is state of health.
which is something that gives you a value in percentage of the amount of current capacity from the the value that the battery was manufactured.
Yeah. So the speed here.
Well, I imagine that this is measured in Hertz.
Thanks.
So this probably should be frequency current frequency, or something like that, because speed is more like miles per hour and things like that.
Yeah, just my 2 cents.
Josh Suereth 00:29:18 Go ahead, Bertran.
Bertrand (Sentry) 00:29:22 Yeah, thank you. Just on the CPU speed is, we already had a discussion in this, and it was you often when it comes to processors, you see, process on speed clock speed is usually used there. That's why we ended up with a speed. In this case frequency would be totally fine as well. Just, you know, having a speed limit. And the CPU was kind of funny.
Then.
Yeah, back to the limit and leaves and namespaces.
I do not understand what you guys are referring to, because I am. I don't know what what it is the attributes to metric conversions.
What is this.
Liudmila Molkova 00:30:27 Josh, you're muted.
Josh Suereth 00:30:31 Yeah, I'll I'll try to demonstrate that a little bit. So pretend I have an event right? That has an attribute on it. So my event looks something like you know. Cpu dot.
what are we calling it? Hardware?
Oh, come on hardware, dot CPU dot speed right is 10, and then I have hardware. Dot CPU dot speed dot limit is a hundred, you know. Let's say 12. Something like this. So this is my event. I'll make it look like Json.
And then what I do is I want to calculate metrics from events. So I have a thing where I have. My events are being fired into an hotel collector which is firing out metrics.
and the configuration for that says, you know, take hardware dot CPU dot speed and hardware dot CPU dot speed dot limit.
Oh, my God!
Come on typing.
My computer is like fried for some reason right now I don't know why, but Zoom has taken a lot out of it.
problem of CPU speed, I guess.
Limit attributes and make metrics. So then, what this does is the collector right? It again. This, this is a component that I don't think exists in open source yet, but this would take these events and say, just calculate a metric from this event, from from this attribute on this event, and automatically aggregate it against the resource that that event associated with. So it's a way for us to take events and turn them into metrics. It's like one of the telemetry transformations we want to allow. The problem is, if if we have things like this is not expressible as an event, because this would conflict, and yet we think we might want to be able to produce events right.
that we can turn into metrics generically where the configuration is just. Here's the, you know. Here's the event. Name. Here's the attributes. Go make metrics out of these attributes right?
Bertrand (Sentry) 00:32:45 I totally understand. It's just what I'm missing is why this is not feasible. You just typed it like the events, includes.
Josh Suereth 00:32:55 This. This here isn't allowed. We do not allow this.
And the reason why is because if you think about this as Json, right, this might become okay.
Now, how do I define speed? Right?
Bertrand (Sentry) 00:33:18 Yeah, no, no. Okay.
It's okay.
Josh Suereth 00:33:21 So this, yeah, this. This is why it? Why it's not allowed right? Because here I need to put those attributes in. This is a flattened representation.
This is the unflattened representation.
Bertrand (Sentry) 00:33:34 Okay, okay, so this is something that is being implemented. The yeah. You know, Json, representation of metrics, because I haven't seen it anywhere. So.
Josh Suereth 00:33:46 This. This isn't Json. Representation of this is of events and the event signal, and I don't remember the current status of the proposal for the wide events.
Liudmila Molkova 00:33:58 I don't think it's being implemented, but I believe it's something we we don't want to close the door 2.
Bertrand (Sentry) 00:34:06 Yeah. But I'm just saying that it feels like we're trying to solve a problem that doesn't exist yet.
Liudmila Molkova 00:34:13 Yeah. But exactly at the same time, my argument for this is more readability than future collisions, because when we, when there is a thing, and there are properties of this thing. It's really weird to so we we treat the namespace as the let's say, the object name and something dot limit is the property of this thing. So then, this thing cannot be a value. It's it's a complex type.
No, you're right.
Bertrand (Sentry) 00:34:46 It's a it's a typical problems, you know, even just, you know, in your file system. Sometimes you don't know how to name things, but.
Liudmila Molkova 00:34:57 Our guidance is to provide the specific property rather than the complex object name. So I find, why is it controversial to call it hardware, CPU speed current or.
Bertrand (Sentry) 00:35:16 So, yeah, okay, that's a good point. So we're going to add current, you know, in many places, just for the sake of you know, adding, maybe later, a yachtical representation of Jason. Because, say, temperature, SW, temperature, it's 1 metric, simple. It's expressed in degrees Celsius. And then you had SW temperature limits which express, you know, some thresholds now to exceed for a given sensor.
Liudmila Molkova 00:35:50 We've already edited. So absolute majority of our metrics have this suffix. So this is the policy we have in this repo.
Bertrand (Sentry) 00:36:02 Sorry I didn't get that.
Liudmila Molkova 00:36:05 So most of our metrics are fully qualified, if you will.
Josh Suereth 00:36:10 So so basically you, the hardware now looks very different than everyone else. We made this decision a while ago where we have like usage. And then we have a limit as well, like even here they have 2 limits. So they even namespace limit. Right? But what the basically hardware now looks different than everything else, I think. Is it process metrics that have usage and limit? You guys just have utilization?
Maybe it's system metrics.
Yeah, usage and limit everywhere. Right? We no longer have like raw. And then dot limit. That's not a thing that we do. So you're saying, Hey, this weird use case around. Namespacing doesn't seem that likely? That's fine. That's not the main concern like that's a subsidiary concern. That's like minor here of one of the reasons why. But the fact that these hardware metrics now look different than the rest of semantic conventions that's actually the major concern we'd want to address first, st like, like, basically, if you want to look different, we have naming exclusions that we write now of like, why, we're named differently. And there needs to be a very good reason.
But now, if you look at how semantic conventions look like for what we're stabilizing for like disk memory. CPU, I think we would probably want hardware to look similar to these metrics.
Bertrand (Sentry) 00:37:32 Totally.
Josh Suereth 00:37:33 Yeah.
Bertrand (Sentry) 00:37:35 Totally so. But so are we going to add current. So it's become Hw, temperature current Hw. Voltage current hw, fan, fan, speed current everywhere. So because there we have a bunch of you of limit matrix.
And it's to me it's kind of silly to add current, because the metric is always current, right? It's never like, you know, from the from when I will go right. It's always a current one.
Liudmila Molkova 00:38:17 So there is current. There is limit. There could be others there could be. I don't know. Average. We probably wouldn't add it, but there could be.
Bertrand (Sentry) 00:38:25 Yeah, but that is actually the row value, right? So plus if you add power, for example, on power current, then it gets current. Being could also mean the electrical current, you know, like Oh, geez!
Liudmila Molkova 00:38:44 You don't need. You don't need to.
Trask Stalnaker 00:38:45 And.
Liudmila Molkova 00:38:45 Current. Yeah. Go ahead. Trust.
Trask Stalnaker 00:38:47 Yeah, is there another word that would be better there. Like, if you look at some of the other conventions, use like dot usage.
Kind of.
Bertrand (Sentry) 00:38:59 It.
Trask Stalnaker 00:39:00 Varies a little bit depending on.
So they I mean.
Bertrand (Sentry) 00:39:03 Actually, if we were to represent things like, you know, in aarchy kind of thing, it would be hw, dot temperature dot temperature. That would be the most proper. In just, in my opinion.
Liudmila Molkova 00:39:17 You can just say value.
Bertrand (Sentry) 00:39:20 Wow!
Liudmila Molkova 00:39:22 Temperature.
The temperature is also not not great.
Alexandra Konrad @Elastic Security 00:39:27 And it's it's the you propose for better charge for the current level and the limit for the limit. Yeah, so we can come up with a good names for every maybe metric that has this collision.
Josh Suereth 00:39:46 So we do. We do have a set of naming here that we recommend. I don't know if any of this applies but yeah, basically, limit and usage tend to go to weather together or limit and utilization or utilization is a ratio against the limit of what you're using. And usage is the like, the raw amount that you're using right of the limit.
one of my questions is based on what you're saying with this like factory lit like a a CPU speed limit would be the fastest. It could possibly go right.
Bertrand (Sentry) 00:40:19 Yeah, or there are several limits. All right. The the nominal speed, the turbo speed, the idle speed, etc. So.
Josh Suereth 00:40:28 Right. You know. Does does this apply, I guess, is the question.
Bertrand (Sentry) 00:40:33 Yeah, not really for temperature. You can say temperature usage.
You know, it doesn't work.
Josh Suereth 00:40:40 Yeah, that's fair.
Bertrand (Sentry) 00:40:43 Same for voltage, etcetera. So.
Josh Suereth 00:40:45 But in in that case limits also kind of different. There, right.
Bertrand (Sentry) 00:40:49 Yeah, I agree, because what limits, when it comes to utilization really refers to a capacity. So you measure the usage of a given capacity, and the limit is for the actual capacity.
And and it doesn't work for other type of metrics which do not represent the capacity. Like, you know, memory disk file systems. You know, they or bandwidth all represent the capacity.
so maybe we should change limit for something else. But we don't have the same problem. I mean, if it's temperature threshold, it's a threshold that shouldn't be exceeded for a given sensor that would work. But then, I mean.
I was a bit reluctant to adapt. You know what you guys were suggesting at first, st saying, I think it was Alexandra who suggested saying, Okay, it was for battery charge. I think that could work for temperature as well like Hw. Temperature and Hw. Temperature underscore limit, you know.
Then it's but then everything is attached to the same, and namespace, which is just Hw. In this case.
I know it's tough.
Josh Suereth 00:42:24 Yeah, I you know, naming is what the hardest problem in computer science.
And then there's also off by one errors.
So anyway, and what we've done.
Alexandra Konrad @Elastic Security 00:42:42 Guidance for this, or like what is the outcome for this.
Josh Suereth 00:42:46 Yeah.
Alexandra Konrad @Elastic Security 00:42:47 Have a lot of those in the hardware.
Josh Suereth 00:42:51 I, I think. Well, hardware, if I recall correctly, still not considered stable. Is that right?
Bertrand (Sentry) 00:42:56 No, it's not.
Josh Suereth 00:42:57 So. So I do think that We should go through here and kind of figure out how to deal with those as as a task.
Alexandra Konrad @Elastic Security 00:43:11 The hardware I have posted in chat the link to old, old metrics like, which is just a Md. File without Yamo.
Josh Suereth 00:43:28 Oh, this one here, this here.
Alexandra Konrad @Elastic Security 00:43:34 Yeah.
So we have here battery fan, CPU, like memory, etc. We have just speed and then speed limit, or maybe some other attribute with dot limit.
Josh Suereth 00:43:54 Yeah. And you also have a ratio, apparently.
Bertrand (Sentry) 00:43:57 Yeah, because it's yeah. We were discussing that we should be using utilization to, you know, to align with the rest of the. But then fan speed utilization doesn't mean anything. So we say, Okay, let's get back to speed ratio.
Josh Suereth 00:44:15 I mean, how does how does utilization not fit? It's how much of the current speed you're utilizing, or how much of the Max speed right? I think I don't understand how that one doesn't work.
Personally.
Bertrand (Sentry) 00:44:28 Okay, well, it was a discussion in the Pr. And in the original Pr that we had for this. So I proposed that actually, and then we were all like, Hmm! It's weird.
Josh Suereth 00:44:42 Okay.
I think we need to reevaluate some of these names. I guess the question is, how do we get these into Yaml? I assume, Alexander, you were trying to get these into our Yaml model, and you were blocked.
Alexandra Konrad @Elastic Security 00:44:59 Yeah, so.
Josh Suereth 00:45:01 It's right.
Alexandra Konrad @Elastic Security 00:45:01 I didn't want to make any factual change. I just want to make a factoring, but it's not possible to make just a factoring, because we need to change names like, I cannot add those names to the Yaml file. And we need to find a solution on how we do this. It's either changing names, or maybe soften the the like. This guideline. But, as you just explained, it will not be good if we do this for the future failing between the events and metrics and in general, and I'm not even sure if you are not having that rule in the viewer, that the namespaces cannot coincide with with values.
Josh Suereth 00:45:48 We have the role for attributes. Yeah, but we don't. We don't have it for metrics.
Yeah, I was just looking. We we thought about adding it for metrics. But we didn't. I I think maybe we do add it for metrics and see see what it looks like. But yeah, I I think here, we're gonna have to ask if if this is all right?
we're gonna have to. Probably redo these metrics to get them in. Why don't you make the Pr. With all the breakages where you move them as is? And let's discuss in the Pr. How to move forward with those breakages. Does that sound reasonable? Because legitimately, what's written in? If if all of our policies for semantic conventions had been applied to hardware metrics as we added them, we would have forced them to change previously.
because they break. You know, our conventions and our policies. And so now that we have manual policies, let's get at least get them a Pr. That tells us how broken things are.
so we can figure out how to resolve it with the policies we have. Now. Let's try to get it in place with our policies, and then we can. We can go from there right? We can. We can discuss different options and figure out what to do with that. Pr, but I don't. What I don't want to do is just have this sit in a state where it's unmaintained, because effectively, you can never stabilize these hardworking until they're in yellow. That is, that is a mandatory thing.
Alexandra Konrad @Elastic Security 00:47:14 So the Pr is there. I just wanted, like, piece by piece, to understand what to do before I do the same. Apply the same change for the for others names. But I can also move all parts of a hardware into one pr, and then we will see, like all those conflicts in one place.
That's not a problem. One question like. So we have removed because we had in the naming this rule that namespace, and shouldn't conflict with the names itself. But we have removed it because we merged metrics, guidance and attributes guidance correct, or because I mean, it was, would be much easier if you already had this at this in place, and now we have removed it.
Josh Suereth 00:48:06 Well, we we removed the the verbal description, because what we're doing is our verbal description always matches. We're trying to make it to the verbal description matches the actual policy that is expressed by like code and rules. We did not have a policy in place for it. And we yeah. So what I can do is I can make a Pr that adds that as an actual policy, I need to make sure that it doesn't break anything, first, st because then we have to have those discussions. But I can add that as a policy where we actually enforce that programmatically.
Alexandra Konrad @Elastic Security 00:48:39 Okay.
Josh Suereth 00:48:40 So yeah, one of the things we want to start doing generally, just to keep things moving smoothly is your Pr. Should break with the policy you're violating, not go read every single document, and keep up to date with all the changes we've made over the past 10 years. Right? That just won't last. So we need to have these things enforced in the Yaml. The fact that you can't even submit your yaml without like getting breakages in the build. That's problematic. That means that there are violations in policy that we have to address for the hardware side.
But if you you know theoretically, if you pass everything there.
then it's a matter of subjective judgment that we have on Prs. But we want to start having less and less subjective judgment for things like, will this break alerts? Will this break dashboards? Will this break users? That's why we have those automated policies?
And and we want to get in there as soon as possible for that.
Oh, so you can do that, Ludmilla. That'd be awesome. Oh, yeah. And event, we need events, too. Yep, cool.
Thank you. All right. I think we should continue to discuss on the Pr. If you want to update the Pr to show whether or not we can migrate at all, and where all the breakages are and have a list of that that'd be ideal, because then we can yeah them out one at a time.
Alexandra Konrad @Elastic Security 00:50:00 Yeah, I will move for all the metrics, then into their own files. They anyway, like in in its own file every metric.
Josh Suereth 00:50:09 Okay.
Cool, alright. Lubella.
This one seems very interesting.
Liudmila Molkova 00:50:23 Yeah. So we have a lot of inconsistencies in call cloud providers and cloud things are recorded.
So I'm doing azure.
And I want to discuss what happens with others. But essentially, we have dated naming guidance. And we've we have more clarity on how we should record, provide their specific things.
And it means we picked azure dot for database for azure cosmos. dB, database was stabilized. Well, we all must stabilize this, but essentially, we came up with this proposal for azure that between azure ad dot and azure underscore, we pick azure dot consistently everywhere.
and it means we're going to update a couple of attributes, some events, and mostly the cloud platform enum this brings us to this. Pr.
this is limited to azure me and trust. Oh, well, it's my trust has approved. So I'm asking other semantic conventions, approvers and maintainers to take a look.
It brings a more interesting question on surrounding things.
First, st we have a lot of inconsistency for other providers, so let's say we have aws dot s. 3 defined somewhere else, and we have aws underscore eks, or whatever their platforms are.
So I think we should rename like I should follow up to rename those as well.
The same story with Gcp. We have gcp.in some places, and Gcp. Underscore in this enum.
but also this enum is a great example of what we discussed previously for hardware. We are not specific enough in the naming of this thing.
and we should probably reconsider with this attribute.
Josh Suereth 00:52:54 Means.
Liudmila Molkova 00:52:55 At all.
But let's let's start small. We'd like to make this change for azure.
I'm requesting the reviews on this and any thoughts on other things.
Josh Suereth 00:53:08 Yeah, this this enum. If you wanted to clean this up, I would be all for it. Because I I yeah, I do not appreciate.
I think this one's rough is all I'll say like it. It's underscores instead of dots.
It looks very different. This is the one you're suggesting. We change. Is that right?
Liudmila Molkova 00:53:30 Right, yeah.
Josh Suereth 00:53:32 Yeah, because I think from a Gcp standpoint, we use Gcp everywhere for Google Cloud, and if we were consistent with Gcp, dot, cloud dot run, and that we could use as a namespace other places that'd be fine with me.
Braydon Kains 00:53:48 It'd be Gcp, dot cloud underscore run right not cloud dot run.
Liudmila Molkova 00:53:53 Gcp, dot cloud underscore run right cloud product.
Josh Suereth 00:53:58 Cloud run is a product cloud functions, a product. Yeah. Sorry. My cat is currently destroying my room behind me, if you hear noises.
Okay, yeah, that that sounds reasonable. Okay? And you just you need general reviewers. Cool.
We have 5 min left, Sam.
do you want to say anything quickly about this. Pr. I'll at least show it.
Sam 00:54:21 And yeah, so I want to remind maintainers to take a look at this here it now has the prototype attach about the set about how set contacts work in instruction code and instrumentation code. And the prototype is also the example you can see how data flows from client to the database. You can see the contacts propagate to the database can be linked to the trace on the yogur.
Well, so I think I provide all the work I need to do. Is there additional blocker I need to work with? Or is there any concern about this.
Josh Suereth 00:55:09 I I think you you did all the work that's required. You just will have to wait for folks to review and approve it.
Sam 00:55:16 Okay.
Josh Suereth 00:55:17 One thing. One thing that I think is interesting here is you're defining a convention around how to declare things in instrumentation to propagate trace context. Right? Normally, I don't think this is something we do in semantic conventions.
That would be. And I don't know where you've had these discussions otherwise, because there might be other things I'm not privy to. But generally propagation context is this thing that we have in our specification.
not as like a semantic convention. A semantic convention is more like, here's the name and label of things. This is kind of new for us. So you should expect this to take a long time for us to figure out in general just to talk about it and and figure things out just to call that out.
Liudmila Molkova 00:56:05 Why, why do you think so, Josh? What? What would be controversial in adding this? Even if it's new.
Josh Suereth 00:56:14 So I guess, do. We don't have a way to enforce this here right in cement. We don't have tooling around this at all, we don't have a way to make sure it doesn't break. It's basically more like a specification. And so that's why my thinking is this, this is more. Something I would see in the specification. It's similar to the work that the Ci CD group just did to have end variable propagation in the specification. And so I actually think, personally, I think this is in the wrong spot.
I think this belongs in our specification, not in semantic conventions, as a way to do transparent propagation in databases that said.
Go ahead!
Liudmila Molkova 00:56:55 Wouldn't. It's very specific to Microsoft, SQL. Server.
And wouldn't it be natural for someone instrumenting Microsoft, SQL. Server to find everything about instrumenting Microsoft, SQL. Server. In one spot.
Josh Suereth 00:57:13 This is why I think we need to have a discussion about it. Yeah, like, I think from from principle standpoint, I think it belongs to the spec from practical standpoint. I understand why you want to put it here. We have to resolve that.
But when I look for context propagation today I don't look in semantic conventions. I look in the spec to figure out what what's possible and how to send things.
Braydon Kains 00:57:36 I think the system group would be interested in the resolution of whatever we decide here, because the way we've been handling like this metric should look this way on this platform and this way or another, is just by like cluttering the descriptions of every metric with like this is what it looks like on Linux is what it looks like on windows. And like we, we can't exactly define the metric without also defying defining specifically how it is expected to be instrumented.
And so it's kind of the same problem here, like we, we can't enforce it as part of semcom. But, like, where are we going to put that stuff, if not in these like metric descriptions like super long metric descriptions? We got.
Josh Suereth 00:58:14 Yeah, that's that's fair. We need a, we need a way to deal with that. I, yeah.
My my personal my personal opinion is when you see things like may and must, which are normative specification things.
I'm trying to limit as many of those in semantic conventions as possible to the point where all of the things that we have are basically defined in our Yaml conventions and automatically enforcement policies and are trivial to put out review, get through when it's things like this, where you have, may and must that are very subjective and need like human validation, or like this, this feels more specification to me than it does a semantic convention.
Liudmila Molkova 00:58:57 There is a W. 3 C context trace context. It's the its spec of its own. There is a propagator described in this spec. This, we need to say how this propagation mechanism works for specific technology.
Let's say, Mcp, protocol or a 2 a.
It will be very weird to have all of these things defined in the spec saying, Okay, for Mcp. Use this property for a 2, a use that property.
It wouldn't belong in the spec, either. It's not a propagation format. It's the weight of the the place specific technology should use for the context.
Josh Suereth 00:59:42 Then it, then it shouldn't be normative.
Okay? So it should not use capital maze, and must. It should just be. It should be a non normative document of, here's how you document. SQL. Server, right? But what like? When I look at this, I see a specification. And when I look at what this is about. I think our specification.
Liudmila Molkova 01:00:01 But we are also specification. We use a lot of non-normative language and semantic conventions.
Josh Suereth 01:00:07 We? We do, and we have a non-normative place for semantic conventions. Right? That's fine. This again, if this gets changed to be totally non-normative and like, here's how to do it in SQL. Server. That's fine. Then I'm reviewing something different. But, like what I saw initially was, here's how we want to enforce context propagation for SQL. Server. That sounds like a specification to me.
If this only ever impacts SQL. Server great, then we don't even need to make this normative. And we can just call this out as like how to do context propagation for SQL server. I don't think this is yeah. We we have other guides for like how to write instrumentation for aws, for example, that this could fit beside, that's fine. But those guides are not normative. Then they're non-normative. Yeah.
okay?
Cool. I need to drop, unfortunately. And apologies, Lydmilla, for the naming guidance. Do you mind taking over the meeting and and running that for the for like 5 min for folks who can stay.
Trask Stalnaker 01:01:15 Christus Trask. I think you were, Joe. You were part of this discussion.
Drop.
Liudmila Molkova 01:01:23 Okay, so let's maybe do it. Offline.
Josh Suereth 01:01:26 Yeah. Sounds good apologies. All right. Thanks. Everybody.
Trask Stalnaker 01:01:29 I.
Liudmila Molkova 01:01:30 Yeah.
