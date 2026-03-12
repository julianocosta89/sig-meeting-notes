SIG: Semantic Convention SIG
Date: 2025-07-07
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Josh Suereth 00:04:58 Is Joe on the call yet.
or was he not gonna be able to make it?
Hello, folks! Here.
Alexandra Konrad @Elastic Security 00:05:22 I think he is not there yet.
Josh Suereth 00:05:28 Folks feel free to add your name to the attendees list in the agenda document. We'll get started in just a second. I just saw that y'all had the 1st 2 things. So I was gonna check and see if he maybe put anything in notes here. Oh, he has a conflicting appointment again. Okay, that's what it was.
Right?
So we need to take notes for him. Alright since nobody else started, I'll run the meeting today. Is that cool? Other maintainers awesome should make a rotation. All right.
Here we go.
I'd like to get to discussion topics and then do triage at the end. So I'm gonna try to save 7 min just to make sure we can get through things. So please add your discussion topics. Job is not able to make it today, so he'd like us to take good notes, which I will promise I will do, which means I can't talk and type at the same time.
Anyway.
let's take a look at this OS type discussion. The question is, should we align OS type values with Ecs. Should we deprecate it and rename it to OS base. And he has a suggestion here. So let's take a look at the issue, and we can discuss alright. So define additional operating systems to cater for more use cases and remove overly broad OS things. This is an extension to a particular Ps. About more OS properties is enabled by the deprecation there.
This.
Okay, so let's take a look alright.
Would we rather look at Markdown?
Let's look at Markdown.
So I think the change here is the set of operating systems being proposed. There's more so. That's, I think, the uncontentious part.
And then.
James Thompson 00:07:46 Josh, would you like me to jump in because I've been the one discussing it.
Josh Suereth 00:07:49 Yeah, yeah, please, do.
James Thompson 00:07:51 So originally I had the idea of extending OS type to include the broad OS's like centos, red hat, etc. All those different OS types that you have right. And as part of that process was to deprecate Darwin and Linux because they were overly broad.
Alright, okay.
And then the second Pr introduced the concept of OS families, and that so you could say, I have a red hat based Linux OS, for example.
Okay?
And so that was what the idea is. So if you look at the jaws, comment to my Pr right. These, I think it's the 3rd last comment from him. It provides a good summary of what the current proposal is.
Josh Suereth 00:08:46 Keep crawling down.
Yeah, I was. So his his comment here, okay.
James Thompson 00:08:50 Yeah, yes, I think that's a good summary. And then what I'll come back with after that.
because the question is, do we go with OS type as being Linux unix nt.
which is significantly different to Ecs.
Or do we deprecate it and go with OS based that way? We're making a clear cut about. Oh, your base OS, in this scenario.
That's yeah.
Josh Suereth 00:09:23 Yeah.
I it's a good discussion, I think. What I'd what I'd want to tie this back to is basically use cases a little bit.
James Thompson 00:09:30 Yep.
Josh Suereth 00:09:30 So when do I need to know that something is is different? And when do I want to abstract or aggregate across these attributes like when we think these these are on entities. So it's about aggregation. So when am I aggregating? Is is aggregating just linux unix and nt reasonable?
You know. Are there a set of attributes I expect to get from from Linux that I would get from every Linux family.
And what are those use cases. I think that's kind of the the discussion. I would have let me get over here so I can take notes. Anyone have thoughts or things they want to say I can't see and type at the same time, so please just speak up.
Liudmila Molkova 00:10:15 Yeah, I have something.
I think the key part is whether anything in open telemetry emits those.
So when we've done databases and other conventions, we constantly goes through the pain. Oh, it should be called differently.
This name is different. Should we use Underscore Dot? How does things apply to the system, so I think that the value of adding constant alone is not worth it.
We should be eating the full story, for a specific OS. Would open telemetry ever run on the watch? OS.
If not, then what is the point of? I think something like this.
James Thompson 00:11:06 Oh, oh, but you could have mobile app, for example, running on a watch. OS.
Liudmila Molkova 00:11:13 Does it collect telemetry, open telemetry, telemetry.
James Thompson 00:11:17 It could be, it could be making an Api request to a back end service.
Liudmila Molkova 00:11:22 So once we have the 1st instrumentation that actually works on virtual S, that's edit.
Bertrand (MetricsHub) 00:11:31 Hey?
Do we want you the OS name, I mean, I like the way it's structured, like, you know. OS type OS family OS name. It's actually pretty classical. We've seen that with Dmtf.
so it's it's not something new, right? Well, could definitely replace Nt for windows, because we're not going to support windows and 95 right?
And and then, I think, only OS type and maybe family should be like, you know, enumerated like in the semantic conventions. We say the way to say windows is windows dot ntu. The way to say Linux is Linux, not red hat, and then other property like family and name OS family and OS names are more free, because tomorrow we'll have another one, etc.
Josh Suereth 00:12:28 It's.
Bertrand (MetricsHub) 00:12:28 Much less important to me. I'm not sure we need to specify these.
Really, there are plenty of plenty, plenty of variations of Linux distribution. We're not going to list all of them here right.
James Thompson 00:12:44 Yes, you are.
So if you scroll, if you were to scroll up to comments, you you actually see the audience in this one. No, it's not so. But there is actually a description and a link issue about where to get the OS name from. So so the idea was, it comes directly from the OS release field.
It's the name that comes directly out of that.
Josh Suereth 00:13:10 I think I think that's should ground. The discussion is is back to what Lyudmila was saying.
Where do we generate these? How do we detect them right now in open telemetry. OS. Is.
I believe, used in.
We did this in the Entity Sig. It's used in the resource detector from the collector, and then some sigs have OS detection in them.
And the OS detection might be the OS is reported by like the Jvm. For example, which is very different than like what you're suggesting.
So I think there's there's an exercise here with all of these Prs of when when we have a Pr to open telemetry. We would like to have a prototype that generates that data just to see where the data is coming from, to make sure it can be generated to make sure those names make sense so like. If if this, for example, wants to pull the OS name from a specific location, we should have a bit of code where we can see where it's pulling that name, and we should make sure that that bit that code that we're looking at.
If we're making an abstraction, can abstract across multiple places where you can look up Boa's name. So, for example, OS, I know, I believe there's a Java contrib thing. I can look it up. The open telemetry collector contrib has a resource detector processor that will look up OS name right? So at a minimum. Whatever we define here should be something that that code can construct.
and if we make an abstraction across OS's, we should be able to provide it in that code. If we want to abstract even further, we should have code. That shows that the abstraction works before we commit to it. That's 1 of the goals now. So I really like what has here in terms of proposal. What I want to see is like, what would the code look like in practice. And how feasible is it for us to achieve that leaving? I like the idea of leaving name, for example, to just whatever the instrumentation reports directly, without any kind of manipulation or massaging. OS family might be something we massage if it makes sense. But if there's instrumentation that can provide that directly, just provide whatever comes out naturally, so that semantic conventions doesn't get in the way of new OS is being released, and things what we don't want is every time a new OS is released we have churn and semantic conventions where we have to cut a release to support it. So we need these abstractions to hold their weight.
and I think, having some some prototypes that show this would be good.
and demonstrate what it looks like across open telemetry.
I think I spoke my piece there any any other thoughts from other folks, or, you know, add into the discussion.
James Thompson 00:15:58 The other thing is jazz. Other question was.
do we deprecate OS type and go with a name like OS base, so we can make a clear cut from the change in behaviour in Ecs.
Because if you look at Ecs, they have a type field which is quite different to that.
Only 2 of those values come across from Ecs.
And then if you look at Ecs, they have values like Ios in there.
all right. So that's what the open question was between us.
Josh Suereth 00:16:33 Yeah.
James Thompson 00:16:34 Do we deprecate type and go with OS base? So it's clear or and have that drift from Ecs, or do we somehow deprecate properties and all that.
Bertrand (MetricsHub) 00:16:47 Sorry what is Ecs.
James Thompson 00:16:50 Elastic, common schema.
Bertrand (MetricsHub) 00:16:53 Yeah, thank, you.
Josh Suereth 00:16:56 Is there a link to the elastic common schema in here that we can look at.
James Thompson 00:17:01 I mean, if you scroll, scroll up to the description, the.
Josh Suereth 00:17:05 This one here?
Yeah, let's do it.
James Thompson 00:17:10 Okay.
Bertrand (MetricsHub) 00:17:13 But that was on the West type.
James Thompson 00:17:15 Right. So they've got the only 2 in the current proposal that we come across is Linux and unix Mac OS doesn't. Android doesn't Ios doesn't.
Josh Suereth 00:17:26 I mean, is there a reason not to use these like? Is there a reason this doesn't work at all?
Bertrand (MetricsHub) 00:17:30 It's good.
James Thompson 00:17:32 But but technically, Android is based on Linux.
Alright. So there's a.
Bertrand (MetricsHub) 00:17:40 It's true.
Josh Suereth 00:17:42 That's that's where we need a detector. That's basically, can you detect Android differently from Linux.
Bertrand (MetricsHub) 00:17:48 Yeah. Yeah.
Hmm.
James Thompson 00:17:51 Right right? And that's why we were thinking about splitting it and and having the base as your Linux unix right your windows as your base.
Josh Suereth 00:18:05 As you.
James Thompson 00:18:06 Or you type, or whatever you want, which name we decide to go with.
Josh Suereth 00:18:09 We can also talk to the elastic folks, and I don't know if any of them are on the call right now. So because I can't. I'm I'm looking at this instead, but it calls out, there's a conflict here. It could be that we could just not use the android part here, but use the rest of them. It's listed as there's a conflict. I think if you click on, the conflict is the same sort of that has significantly different semantics is what they say for conflict. Yeah, we. We could talk. They already list this as a conflict. So I think we can.
We can use OS type.
James Thompson 00:18:46 But at the same time we'd be deprecating. Ios we wouldn't be bringing across Android Ios, Mac OS.
Josh Suereth 00:18:54 That's because we want to use Darwin instead of Mac OS going forward.
James Thompson 00:18:59 No. So Darwin's currently there.
Josh Suereth 00:19:03 In in Ros. Type. Yes.
James Thompson 00:19:06 Yes.
Josh Suereth 00:19:07 Yeah, I like again, this is already listed as a conflict in here. So we already know that that there's different semantics. So I don't think I don't think we have to abide by this exactly right.
and we can align with it where we can, which I think makes a lot of sense of, you know, using Linux windows unix ios, if that makes sense and and we can sort that out. But since it's already marked as a conflict. We're already advertising that expected values do not correspond with values and semantic conventions. So that's already a well documented thing. So I don't think that needs to be a blocker for us. Accepting Giawa's proposal, let me write that down in the notes quick.
Alexandra Konrad @Elastic Security 00:19:50 I think it's marked as conflict, because it has different number of values already. So it's a bit deviated from Ecs already. So if you click on the OS time that we have inside the current open telemetry attributes. We have, like 10 of them.
Josh Suereth 00:20:15 What did you want me to click on.
Alexandra Konrad @Elastic Security 00:20:18 If you go to the Ecs description and click on the open on the open telemetry link. Yeah. OS, 5.
The last one. Yeah, you would see that it's probably have different set of fields. I'm not sure. Let me
Josh Suereth 00:20:39 This is where I think we can deprecate. We can deprecate some of these to match the proposal right? So, instead of having these be as robust as they are now, which again, is still in conflict with Ecs. We can go closer to what Ecs has.
So there's less of a conflict. Basically, if we take what what Yao proposed, right and just change nt, to be windows, we're going to be much closer to what Ecs has today.
We already have this as a breakage, because this is different, right than what we had before, and we can deprecate the things that we are no longer going to support in type. And then we can use name and family for yeah, cause we're missing family today. So we could add, family.
I actually really like that proposal going forward. I think that that simplifies a lot of things brings us a little closer to Ecs. And this is not a kind of a stable piece of hotel, but we should make sure that existing implementation that we have can can provide the the data we need. So you know we have we have OS detection right now in in the collector.
and I think, is it Java instrumentation that has it? Some some Java system does OS instrumentation. I think maybe some of the other sdks do so. We should actually do some prototyping to make sure that in the places where we are doing resource detection that we can get the right OS name that we want to match this like, let's make sure the instrumentation matches. But if we're able to provide value similar to this, we should do so.
Oh, sorry I wasn't sharing the right tab. This is the tab I should have been sharing. This is the open telemetry, one.
James Thompson 00:22:34 Yeah.
Alexandra Konrad @Elastic Security 00:22:36 Yeah, I would like also to add that Ecs already has the family.
So I'm not sure why it's not added to the up on telemetry. OS.
Josh Suereth 00:22:50 Oh, so we yeah, you're saying from Yao's proposal, just use family instead of what did he call it?
Alexandra Konrad @Elastic Security 00:23:00 Yeah, I mean, we have already distinguishing, distinguish we already distinguishing basis between the type and the family. And I'm not sure. And and the name. So it's quite similar to what this proposal has. Yeah.
Josh Suereth 00:23:18 Yeah, what's is there any significant difference between this and Ecs outside of just some of the choices of names like in terms of meaning.
James Thompson 00:23:28 I don't remember seeing family there in Ecs. I might be wrong, but I don't remember seeing family there.
Alexandra Konrad @Elastic Security 00:23:36 Yeah, it's there.
Josh Suereth 00:23:39 If you click on that link that you had, Josh.
Alexandra Konrad @Elastic Security 00:23:44 Or like they are at the top. I'm not sure.
Josh Suereth 00:23:46 Yeah. So I'm I'm grabbing a different tab. Here it is.
James Thompson 00:23:49 Hmm.
Josh Suereth 00:23:52 Yep.
right? So OS family would just match kind of the Ecs family. I think that would make sense.
OS name doesn't have version, which is what we'd have. An OS type would be similar to this. I think this makes sense.
Bertrand (MetricsHub) 00:24:17 Yeah.
Totally.
Josh Suereth 00:24:22 Okay.
Liudmila Molkova 00:24:25 I want last note on this, I think we should ask system. Semantic conventions.
Group 2.
Approve it. Whatever we come up with.
Josh Suereth 00:24:37 Yeah.
alright. I think that sounds like a a good path forward. I do like, I said before, I would like to see some prototypes here system would be a good group to talk to, because they might be able to update those prototypes, since they are working on system, semantic conventions and resource. Resource, detection.
So AI is.
Alexandra Konrad @Elastic Security 00:25:06 I have also added a link. This is the old issue from Pablo. He wanted to also change the OS. To have it corresponding to what the kernel, for example, usually gives you as output. So this also similar, yeah, like tidying the OS namespace. So maybe introducing some new values, there makes sense to look into this as well.
Josh Suereth 00:25:35 Yeah.
Alexandra Konrad @Elastic Security 00:25:35 So he wanted just to make it, you know, uniform as he wrote, like using you name on the Mac OS or win version on windows, etc. So that we always have some specific provided information, and not just the set of values.
Josh Suereth 00:25:54 Yeah, I mean, again coming back to, I think Pablo's coming from a how does this work in the collector? How do I implement it. That's that's where I want to ground some of these discussions of like.
If we make an abstraction, we should have 2 things in mind. One is, how do I instrument it to get the values I want, and how hard is it to do that? And second, is, what are the use? Cases of that abstraction, so is the abstraction useful. When I aggregate metrics or aggregate my graphs, or, you know, create alerts on something. So as long as we can answer those 2 questions. That's good.
I like this, I want to move on to the next topic. If that's okay, I'll just let me actually write this as action items, because we are at about 20 min on that topic. So I think to get through the rest of the agenda, we need to move on. Okay, next up clarification on how to populate OS resource attributes. So this is from this issue.
This might be somewhat related. This is an issue from a slack conversation trying to get around clarity and intent of OS. So I think this is actually goes back to kind of my point of in Debian. If you look at things, here's what it says, right?
Where do we fill out what and how do we fill out what and what.
Liudmila Molkova 00:27:14 You are not sharing that.
Josh Suereth 00:27:16 Oh, my God! I'm sorry I did it again.
Liudmila Molkova 00:27:19 Thank you.
Josh Suereth 00:27:19 I clicked the tab that I thought would be the same thing I'm presenting, and it opens a new tab like every time, so I don't know why it's doing that to me. Apologies.
okay, so this is clarifying. OS resource limits for Linux. This is basically saying, Look, here's here's what we find on various. You know, versions of Linux and what it reports.
And this is what I was getting to of. Okay, if Linux is reporting this.
how do we make it? So we can use this information, this data to fill out semantic conventions. And and let's write the code for that. So Yao proposed 2 h ago. The name, description, version.
and thoughts around it. Let's come back to the discussion.
I think. OS name OS description OS version are okay, as they are just need to be better described. How to populate, which I think might be something. We ask the system sem groups to help flush out for us. I saw that issue. CC. To Braden. I don't know if he's on the call or not. I don't remember if he had off today.
anyway, the if we want that, we need to introduce a new attribute, which is how to record the kernel version.
I think that's reasonable. Should we? Should we ask System Simcom, to make decisions here and come back with what they want to do?
Dot net. The recommendation on Linux is to parse at Ceos really makes sense.
Okay, so action. Item, propose this to system of some kind of group as feature work, I think. Let me check this issue quick again. I'm not. I might put here we go.
It is already in Sig issues, and it's in their to do list. So I think we should just track this with them. I'll follow up with you. Offline to say, hey, I think maybe bring it to the Sig and talk through it there. If you want to make rapid progress on this, but that should that should help us, resolve things cool.
All right, let's move on, Alexandra.
Hardware discussion.
Alexandra Konrad @Elastic Security 00:29:37 Yeah. Also to add to the previous one. Ecs also has OS dot kernel field.
so we might use it and make it available there as well.
Josh Suereth 00:30:01 Cool.
Alexandra Konrad @Elastic Security 00:30:03 Regarding hardware as we discussed last time. I have moved all hardware metrics to their own Yama files and we like. I don't have any issues there in the tooling.
because we want, like you proposed to that. I do this, and we check like how many errors we collected.
Josh Suereth 00:30:28 Didn't.
Alexandra Konrad @Elastic Security 00:30:31 but we still. So there is a discussion inside the issue between turnout and I think, James. About this usage of the pure namespace as a field. So in this case, for many metrics, yeah, it could be battery or CPU, or the fan, etc, like, if we are using. Let's say.
what was that temperature? And then temperature dot limit, or we are using the the namespace as a field name.
So yeah, I'm not sure how to proceed, because technically we are. I think we are not limiting metrics.
To to collide, to do not collide with the namespaces. But yeah, this is. This is open discussion for me.
Liudmila Molkova 00:31:25 So the the collision is between the metric name and the metric name is a namespace for the attribute.
Is it the collision.
Alexandra Konrad @Elastic Security 00:31:33 The collision is that we have 2 metrics. One is, for example, like, let me open the issue myself. To have the right names.
Bertrand (MetricsHub) 00:31:45 Yeah, it's hw, dot temperature and hw, dot temperature dot limit. For example.
Alexandra Konrad @Elastic Security 00:31:53 Yeah, for example, or battery dot charge and battery dot charge dot limit. So these are 2 different metrics. And we have quite a lot of them, I would say, like 8 to maybe 10 for most of the hardware metrics we have this collision.
Liudmila Molkova 00:32:14 And I think we talked about it. Maybe last time or a couple of weeks ago.
Alexandra Konrad @Elastic Security 00:32:19 Yeah, yeah, it was, I think 2 weeks ago, and we decided that I like there was only battery. Moved to the yaml files. So we decided that they move all the files to understand all the possible, let's say collision collisions, or maybe other problems. And then we moved from that point.
Let me just put on.
Liudmila Molkova 00:32:46 So the proposal is that since it's already in Markdown, can we define it in Yaml, as is, and then figure out what to do with it?
Alexandra Konrad @Elastic Security 00:32:56 I mean, we already defined it in Yaml. So it is already everything in yaml files, and our tooling currently allows metrics to have this. Let's say, collisions. Yeah, so that we have hv, temperature and and Hv temperature dot limit as different metrics.
And I think Betrand wants to have it this way, this way. But I'm not sure if it's still okay for us to have it this way. And there are more discussions within them issue that maybe it's not the best way to express the metrics. So maybe we still need to be able to make temperature dot, Max, or maybe temperature dot mean or like, add other metrics which is still possible right now we are not restricting it for metrics. We're restricting it only for attribute groups.
Bertrand (MetricsHub) 00:33:54 Yeah, it's a heated discussion between James and I.
Yeah.
now, it's really my concern. Is that really we're trying to find workarounds like adding, Hw. That temperature, that current, for example, to be compared to Hw. Temperature that limit or that threshold, whatever you know.
But if, as you suggested, James, you know, in the future, we have okay, we have several types of limits or thresholds. And then we want to have Hw. That temperature that limits that mean, or that limit that, Max. Well, then, we won't be able, because then that limit will become the names namespace itself. I'm like we're just preventing ourselves from creating new metrics in the future.
Liudmila Molkova 00:34:48 I think the Hv. Dot temperature is a problem on its own, because it lacks clarity.
It's not. It's less of a namespacing problem. It's lack of clarity problem. It can be anything. Since there are a lot of things under temperature.
Bertrand (MetricsHub) 00:35:04 Well, but basically, it's a temperature. So it's nothing else.
Liudmila Molkova 00:35:10 Well, you can measure temperature in many ways, and since it's it's probably gauge, it's the current. If it was a histogram. Well.
it it happens in your discussion, but it it's not right.
Bertrand (MetricsHub) 00:35:24 Well, it's a gauge. Yes, it's a temperature.
Liudmila Molkova 00:35:28 So you need to explain. What is it measuring right? Because without saying, what is it measuring which property of of the distribution it's measuring. It doesn't make sense on its own.
Bertrand (MetricsHub) 00:35:40 I'm sorry I'm I'm confused, so it's measuring the temperature
Liudmila Molkova 00:35:47 Current temperature, right? It's not the distribution.
The main.
Bertrand (MetricsHub) 00:35:52 I understand. But then, system CPU, time. It measures the current time of the CPU and file system. Utilization measure the current by stimulation. And yet we're not adding currents behind each metric name, because we know it's current.
Josh Suereth 00:36:10 We added utilization. So utilization and limit are pairs in in semantic conventions, right? So utilization limit is supposed to be a pair for things where you have a limit, and you have, you know, capacity up to a limit.
Bertrand (MetricsHub) 00:36:23 Agreed. Let's talk about usage.
Josh Suereth 00:36:26 It's the same.
Bertrand (MetricsHub) 00:36:28 Yeah, it's usage.
It's not current usage, it's usage.
Yes, but I don't have any.au.
Josh Suereth 00:36:38 Words here so so like usage, utilization limit, are defined generically for all semantic conventions that have a meaning.
You don't have one of the words in temperature.
Does that make sense like there's temperature is just temperature.
Bertrand (MetricsHub) 00:36:53 Yeah, because whether it's the usage.
Josh Suereth 00:36:57 Like is this a histogram of the temperature? Is this a distribution of the temperature? Usage implies that, like a specific way of measuring it in semantic conventions like there's meaning behind it, so we could do the same for temperature. If we want it's just then temperature limit gets awkward with some of the things we're having. The the other thing I want to call out with these metrics is, I actually am of the opinion that we do a lot in metrics, because we think we we.
The word metric is misinterpreted sometimes in in what we mean by semantic conventions. The way we've defined. A metric system in open telemetry is about aggregating data and reporting it at intervals, where, if you lose a piece of data every once in a while it's not a big deal. If you have a system where you are only reporting gauge based metrics ever you should be using events instead. Generally you like, it's something to kind of think about of like, it might be better and actually more efficient to create a hardware like usage event that has just temperature and temperature limit as fields. In that event that you fire down.
Bertrand (MetricsHub) 00:38:09 Well,
Josh Suereth 00:38:10 And convert that to a metric.
Bertrand (MetricsHub) 00:38:12 Respectfully disagree. I mean, I've been doing hardware monitoring for like 20 years and for temperature, you need to analyze the trend of the different sensors, so they can predict what's gonna happen if you're gonna reach a threshold soon. And because the A/C. Went out, etc. I mean, it's not just events, it's really a metric, and some other metrics are actually measured with gauges. I mean, not gauges, but up down counters. So in this case, by the way. Maybe it's not a it's a gauge, because you cannot. Sum. Temperature. Temperature is degrees, Celsius, right? So you cannot sum any of these metrics and like up-down counters for file system. But it's a current value, right? It's not histogram. It's a stressor temperature. I mean, it's the most basic thing. It's a standard unit, even international standard unit.
In I don't see how different you would like to name it like again. The the best we could come up with is hw, dot temperature, dot temperature.
Then, yeah, if Hw. Temperature is a namespace, then inside that namespace you'll have the current value which.
Josh Suereth 00:39:36 You.
Bertrand (MetricsHub) 00:39:36 Whose name is temperature.
Josh Suereth 00:39:39 The thing that would make more sense would be if it was hardware thermometer temperature and hardware thermometer limit. Because you're talking about the limit on the thermometer. You're talking about the limit.
and you're talking about the value of the temperature on the thermometer. If you wanted to give a name for this thing right.
Bertrand (MetricsHub) 00:39:55 It could. I'm not sure what it what it adds in terms of, you know, clarity, because the temperature is always measured by thermometer. Right. I mean, we don't use. We don't use that for other for other metrics. So.
Josh Suereth 00:40:14 We we've done. We've done similar things in other metrics at times. Yeah, so. But.
Bertrand (MetricsHub) 00:40:22 See battery charge. It makes sense. Right? We put battery because the charge could be something else. It's battery charge.
a temperature. It's so basic.
Oh.
Liudmila Molkova 00:40:35 It's still, it's not basic because there are many properties of this temperature. And the dot limit is one of them. There are plenty of others, and I think we should have a rule. It doesn't mean that it should be enforced immediately, but we should have a policy in semantic conventions that prevents it.
And this is the choice we make in semantic conventions.
It's like a winter you you don't argue with Winter, and I wish it was a winter.
Bertrand (MetricsHub) 00:41:03 Yeah, okay. Well, just saying, you know, I'm sorry I need to leave. I'm not rage quitting on you guys, I have trained cats. It's just that, you know. I've been, you know, again, we've developed a collector that's pure open telemetry, native open telemetry.
monitoring hardware devices, leveraging these metrics that we've defined in. We took the time to define these semantic conventions. So we have product that's actually working. We have dashboards in graph and I in datadog, etc. Leveraging these, and they they work really well and using them And alerting is done very well again in Prometheus that are comparing temperature to temperature limits. And and until now I haven't seen any really any practical issue because of these of these names. And that's why it feels a bit artificial, saying, Oh, we need to add that because and I still don't really understand why. But we can. I mean at some point, if you want, I can show you what we're what we're doing. So we see an act as you were saying, Josh, earlier, you want to see actual, you know data. See how it looks like before we make decisions. You know, if if you if we if you guys want, I can show you for a few minutes the different like queries and stuff that we do with these metrics. So you have. You know, So we're well, at least on the same page. You can see I'm I'm open to change things, the draft or in our software. It will be just replace all in some in some repositories, right? But I just don't want to, you know, create complexity just.
but I haven't. I still haven't clearly understood the the main reason behind that.
Josh Suereth 00:42:55 Yeah, yeah, I think that that's all reasonable. If you have example, code and things. And you have usage like, bring that to us. I think that.
Bertrand (MetricsHub) 00:43:04 Have that.
Josh Suereth 00:43:04 I want. I want all of us to consider real world use cases as our prime rounding function right.
Bertrand (MetricsHub) 00:43:11 All right. So I really need to go. And again, I'm not raised quitting on this.
Josh Suereth 00:43:17 I think.
Yeah, go go ahead and head out, and other semantic convention maintainers who are here.
Are we comfortable merging what it is today, as is because it's already in the markdown, because let's just get it out of the markdown and get it into the yaml as is. And then we can decide on this policy going forward. I do consider this discussion a blocker for stabilizing those metrics. But let's at least just get them in. Anyone anyone have concerns with that.
Alexandra Konrad @Elastic Security 00:43:52 Yeah, I also want to want to point out that this was actually pure refactoring, or should have been yeah, because we had hardware just in the Ind file, and I extracted all the metrics and just put it in the yaml files. And from that point we could do. Let's say, whatever we want to do. Yeah. And for some rules like, update the naming, etc. So it would be great if you have them in the proper way that we should have them for a long time. Yeah.
Josh Suereth 00:44:22 Yeah, yeah, exactly. Anyone have concerns with doing that.
Liudmila Molkova 00:44:28 No, as long as we create an issue. And we mentioned that it's a blocker for hardware stability.
Braydon Kains 00:44:38 Have any of those like open policy agent policies written that will start erroring on this. Do we.
Alexandra Konrad @Elastic Security 00:44:45 Not yet.
No, not yet. Yeah. We don't have it, because we don't have the checks on the metrics.
Braydon Kains 00:44:56 That's probably fine.
Alexandra Konrad @Elastic Security 00:44:57 Like Pr is clean. I'm not sure if we should have that check for the metrics or not like this is a separate discussion.
Braydon Kains 00:45:05 Yeah, we should enforce whichever way we end up. But but yeah.
Josh Suereth 00:45:09 Let's let's move on because we spent a lot of time on this so far, and I think we have some clear action items to take care of, and I don't think we're going to resolve the overall discussion today.
So let's get stuff written down. Let's come back with some practical use cases. Let's move on, Ludmilla.
Liudmila Molkova 00:45:26 Yeah, thank you. So I have a Pr, I'm just advertising it to get some eyes on it. It's approved by the Sig. It renames genai dot system to Jenai dot provider name.
Josh Suereth 00:45:40 It also adds a.
Liudmila Molkova 00:45:45 Break in change, transition plan to experiment from experimental to experimental.
So, Josh, if you maybe can expand it, I think that transition plan is the most interesting to this audience.
Josh Suereth 00:46:04 Sorry I have to wait for my computer here.
Liudmila Molkova 00:46:06 It's okay. So if you open any of the Markdown files you would see that transition plan.
Josh Suereth 00:46:13 Come on, you can do it. Oh, that's the registry! Hold on.
Liudmila Molkova 00:46:22 Oh, sorry. That's the registry. Yeah.
Josh Suereth 00:46:25 Yeah, I I clicked before it scroll showed up. I don't know why, but Github is being really slow for me.
Every once in a while. That happens where my browser just hates it. Here we go.
Liudmila Molkova 00:46:38 Yeah, so essentially, we are utilizing the same environment, variable, a property name that we use for the stability opt-in.
But we're calling a Gen. AI, latest experimental.
So someone who currently implements an instrumentation should not stop doing what they're doing.
They can start supporting this extra state where, if user opts in, they are opting into the whatever. This instrumentation supports latest from gen, a conventions.
This is a moving target. Right? So once you opt in you. When you update your instrumentation, it might introduce additional breaking changes to what you had. But the hope is that since you are opting into into the latest experimental. You are consenting to breaking changes.
We will probably update this plan. Once we actually start stabilizing gene conventions, we will maybe add some additional target or the rob some previous versions. But that's the plan so far.
So I'm kind of asking folks to review. It's approved by the sig. It's been out there for a while.
It's breaking, but we believe it's necessary.
Josh Suereth 00:48:12 I'm glad that environment variable is working out for us so far, that's all I'll say.
Cool. Should we move on.
Liudmila Molkova 00:48:23 Thank you. The other. Pr, I'm again advertising the Pr. That automates schema schema. Next generation.
We'll talk in a sec that we will probably want to go way further than that. But finally, there are no blockers for this Pr to move on so a few changes. You will no longer need to update schema. Next.
it will be generated at the release time.
It only covers the rename. Similarly to what we have today in the schema next.
And you don't do. You no longer need to worry about the proper typing, the right things into the Schema. Yaml. Yeah, that that's essentially it.
Josh Suereth 00:49:16 Given the number of times bugs have shown up from only manual review of that I think this is awesome.
So cool folks, please review, this, I think, yeah.
Liudmila Molkova 00:49:34 Yeah. So 1 1 comment for the reviewers now, the deprecate property is the thing you should pay attention to. I think we did in the past. But this is what drives the schema. Div. So when it's just a simple rename, the attribute acts as rename to attribute y across all metrics, let's say well, across everything.
Right? Then it should be a deprecated with reason. Renamed if it's a split. If, let's say, the metric changes unit along with the rename. It's not the rename, it's the.
but we have uncategorized or obsolete, or something with a note.
so it would not show up in the schema next, because it's not the simple rename from X to Y.
Josh Suereth 00:50:30 Yeah. And that does mean, I think we consider it breaking. For now.
once we remove that moratorium. Yep, cool.
awesome. So action items is, please review.
do you want to talk about Schema? V. 2.
Liudmila Molkova 00:50:51 Yeah, I, yeah.
I hope we can share with this group what's going on with regards to Schema. V, 2, just to give a heads up.
So if you if you have something around, maybe you can share, sir, I'm not. I haven't, added the link.
Josh Suereth 00:51:10 Oh, yeah, let let me. This is gonna be a bit awkward if you but I'll just share a pull request with the initial. Read of Schema. V. 2, so Laudmila proposed a prototype of Schema. V. 2. And what we could do if we start reorienting our schema to actually instead of be based around groups be based around signals. So where would be the best test? Here? I started prototyping it a bit in Weaver.
and I don't know if this is readable.
Others comments on this. Let me view the file raw.
Oh, come on, Github, stop fighting me.
Sorry.
Let's see.
Can share.
You can share
Liudmila Molkova 00:52:11 Send the link of what you were showing, and I will share.
Josh Suereth 00:52:16 Okay? Oh, that's the problem. I don't think I can get you a link.
Okay, here's what I'll do. I'm almost there.
View file.
Why are you not viewing file?
Okay, let me try this again.
Alright. So it is under, I believe, creates Weaver Senkov.
So yeah. Apologies. This doesn't look as good as it should.
Here we go. So we're working on a v 2 version of the specification. And I think, do I have it here. Yeah, so this is basically what your yaml might look like.
So instead of specifying a set of groups, is this readable.
Liudmila Molkova 00:53:19 Yeah, but if you can zoom in a little bit, it would be even more.
Josh Suereth 00:53:22 Okay, how's that.
Liudmila Molkova 00:53:23 Thanks.
Okay.
Josh Suereth 00:53:25 So instead of specifying a set of groups, you would actually and specifying attribute groups directly you actually just directly specify attributes straight up.
And instead of them having an id, they have a key which should match more open telemetry. So just a few things in terms of the goals of this is the names that you see in Yaml should match the names you see in Otlp. That's that's Number One and Number 2 is some of the weird things that we had in semantic conventions will be made more consistent across the board, for example, where stability is now required by default on everything as opposed to being optional with weird errors that show up, and that might be a a weaver thing. But We can actually make the the Yaml schema match exactly instead of have these weird, like optional validations where you have to say, group with type metric has these required things, and a group with Type span has these required things. They're just directly encoded. So attributes are specified as a list of things. Metrics are specified as a list of things. Entities are specified as a list of things. Events are specified as a list of things, and spans are specified.
A few things that this changes, instead of metric, underscore name. You just write name.
There's no Id. The name is the Id of the metric.
Brief stability should be consistent across all of these. So everything requires a brief instability, however, for metrics instrument unit are required, and it looks the same as it did before. But your error, messages and things should be better because of this. For entities, instead of having attributes with role, you actually say, my identity is this set of attributes. My description is this set of attributes.
and you do that by reference.
These signals can only refer to attributes. They can't define them right now. That's something that we might change in the future, but for now I think that has to be how it is, and then for events, you can define your body like before, and instead of event, name it's name. I think it was named before. The oh, the other thing is right. Now, when you define an entity type, you define it in the name field of the group which is awkward as hell. So instead.
you can actually have a type field. If we do this, which makes it a lot nicer, and then spans. The biggest change here is we actually want you to define span name directly of like a template that you would fill out, or some sort of description of how to fill out span names. And the other thing is, we're looking for an identifier. We can use to validate spans on the wire. So we want a type field for span. That would be some sort of name like this is an Http client span. So when we read the span in Otlp, and we want to validate that you are abiding by the specification, we can sync up the semantic conventions to the span. Those are kind of like the big changes.
And then this is our unit test. So today, in this example code, you can see that this turns into what we all know and love. In our existing set of groups, where we have a group for an attribute group with the attributes we have a group with entities where we have refs and roles. We have a group for the event. We have a group for the metric, and we have a group for the span so effectively. This would be start with. We can define inside of semantic conventions with this new syntax right? And then all the code, Gen. And behavior downstream will still be on the raw groups that's like step one step 2 is then published. Resolve. Schema will look like this new format where we will publish schemas in the new format that has attributes, metrics, entities, right, that sort of flavor.
And so anyone who is consuming a published Schema or the schema diff, will use this new structure.
and then step 3 would be inside of Weaver all the way through. Cogen. Everything kind of sees things the same way. But this is the general structure we want people thinking about when they define and when they consume semantic conventions. There's a set of attributes. Oh, sorry double clicked on something. There's a set of attributes, a set of metrics, set of entities, set of events, a set of spans.
The type of the span is identifying. The name of the event is identifying. Type of an entity is identifying name of a metrics identifying the key of an attributes identifying thoughts and questions. There.
Alexandra Konrad @Elastic Security 00:58:07 I have one question regarding the grouping of the attributes, so there will not be grouping inside the semantic conventions as well. Or we just let's say, make it just visualize grouping them. Yeah, as we do. For matrix. For example, right?
Josh Suereth 00:58:24 Yeah, that actually is one of the big open questions I had in prototyping this. So I got rid. So grouping would be done by the file in which they're defined would be the bare minimum.
What I would like, though, is and what we kind of do today is we group, based on the namespace of the key.
Alexandra Konrad @Elastic Security 00:58:46 Yes.
Josh Suereth 00:58:47 And so we could still do that. What we lack, though, is we lack the ability to provide a brief and description at the group level.
Liudmila Molkova 00:58:55 Don't use them actually.
Josh Suereth 00:58:57 We do use them when we generate registry.
Alexandra Konrad @Elastic Security 00:59:00 Yeah.
Josh Suereth 00:59:02 Yeah. So I I discovered that. Yeah. The miller had looked into this. That was the I think I have this as as one of the open questions on the weaver. Pr. But we do use the brief and description in the, in the registry of attributes when we generate it.
It.
The reason I think you say we don't use them is because the brief and description are usually trivial.
Like we don't really say a lot in them.
Alexandra Konrad @Elastic Security 00:59:29 But that's not not always to be honest, like in metrics, for example, we have, yeah.
Josh Suereth 00:59:38 In it. Where? Where do? Where do you see a nontrivial one? We can just take.
Alexandra Konrad @Elastic Security 00:59:41 Yeah, sorry. Not in the metrics in the metrics. That's a bit different. We don't have grouping there.
Josh Suereth 00:59:48 You, you would still have brief and description. So groups go away. But metric is a group, so you would have the name in metric. Where's the registry?
Liudmila Molkova 00:59:58 Actually the grouping mechanism, the groups we extensively use them for other reasons for the common to just copy paste.
So let's say for Http. Server address. We have a special attribute group that is used across spans, metrics, whatever, and it it documents. Http. Specifics around server address, and this.
Josh Suereth 01:00:28 We need. If we also need brief and description, then it's just the the.
Liudmila Molkova 01:00:34 Reinforces that we need some some grouping thing.
Josh Suereth 01:00:38 If if we if we need that. Yeah. So right now, the the brief.
the brief and description we have on group, the only place it's used. And here's an example from Android is when we list. Android attributes right? This is from that attribute group all the attribute groups get pulled out into Android as a thing, and then we look at each attribute group and give them a link with a title.
The title is the the idea of the group which again, in the New World, the new prototype I have is actually the name of the file and then the android attributes here that we get. This is the brief of the attribute group.
And the question is, does having android attributes like this, where we have android and deprecated attributes separate because they're separate groups. Do we think that provides enough value to retain? Or would you rather just see, Android with all the attributes listed in one big table where the deprecated and the undeprecated show up together in order, like in.
Liudmila Molkova 01:01:41 Or we can still break them down into 2 tables.
Josh Suereth 01:01:44 We could still break it down by deprecated manually. Yeah, I think the one. Let's do. Let's try to find one where we actually have more disk again. Disk has one thing, so all it says, the attributes may be used for any disk related operation. It's not particularly useful.
net. I think this document defines.net attributes right that, like none of these are super crazy.
and I'm struggling to find. Oh, here's 1 Gen. AI openai deprecated Gen. AI deprecated Openai. The question I would have is, if Gen. AI. And Openai need to be split.
I think we can actually do so. By where's the opening? I should have just clicked on the link.
We can do so by the namespace, right? Because the Openai attribute group is geni dot openai.
So almost all of the grouping and descriptions that we have, I think we could do by namespacing of keys. We're over time. So actually, I do have a hard stop. I need to go.
Really look forward to more. Yeah. So.
Demo, I'll put. I'll put a link to the Pr. In Weaver. If you're curious, we would really appreciate feedback on this, and please, you know, give us oh, shoot! Give us comments in chat in Cncf. Slack, if you can, on bugs and issues, and we'll give you links to Lumilla has a good issue proposing the format. I need to drop so apologies, Lamila, if you'd like to talk about this, feel free. But I do need to go. Thanks. Everybody.
Liudmila Molkova 01:03:20 Thank you. Let's talk next time.
Josh Suereth 01:03:22 Okay.
Liudmila Molkova 01:03:24 Thanks.
