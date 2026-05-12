SIG: Semantic Convention SIG
Date: 2026-05-11
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:06:16 Hey, folks, how are we… Debating the, the eternal question of what to do with the note-taking bots.
Daniel Dyla (Dynatrace) 00:06:26 We're not debating anything. I'm… I'm commenting on… The confusing wording of the messages that they post.
And the implied… agreement to privacy policies that I'm not even planning on reading. I… I'm more annoyed by that than I am by the recording.
Trask Stalnaker 00:06:47 Yeah.
Daniel Dyla (Dynatrace) 00:06:48 But, yeah, the policy is we should kick them, so I think if somebody has the permission, we should just do that.
If nobody's logged into the account, then… whatever, I don't feel that strong about it. If somebody else does, then great.
Trask Stalnaker 00:07:03 Does this… is this not one of the newer variety that you can tell it, like, FF leave or something?
Daniel Dyla (Dynatrace) 00:07:10 You can, that's what the comment says, but it says, stop recording. By continuing, you agree to some link that I'm not gonna click on.
Trask Stalnaker 00:07:19 Oh, okay.
Daniel Dyla (Dynatrace) 00:07:20 So, if I ask you to leave, is that… It's not clear.
Trask Stalnaker 00:07:26 Let me try.
I've… I've told it to leave enough times that I've…
Daniel Dyla (Dynatrace) 00:07:33 Trust me.
Trask Stalnaker 00:07:34 opted… I've opted into whatever it says already, so… no…
Daniel Dyla (Dynatrace) 00:07:39 Yeah.
Trask Stalnaker 00:07:39 harm done.
Daniel Dyla (Dynatrace) 00:07:41 Yep. Well, I did leave, and I suppose that's… They should all probably implement some feature like that, because that's much better than… Having to kick them.
We can move on with the meeting.
Trask Stalnaker 00:07:55 Oh, it's fine. Yeah, having to kick them is such a pain to go and find the… figure out what… which room we're in, go and find the right… code… Yeah.
Alright, since I am talking and awake, I am happy to drive this Meeting…
Josh Suereth 00:08:23 I was gonna say, you seem more awake than me, and it's… it's actually 11am here.
I should be late.
Trask Stalnaker 00:08:33 Awakeness doesn't have to be a time of day thing.
Let's see, we've got no topics under next. We've got no topics here. Let's start with triage, and we'll see if topics emerge.
Pr Triage Board… So, hopefully y'all saw that… All the GenAI PRs are gone now.
They have… Moved.
To the new repo.
So that's… I think kind of cool for this repo.
Blocked, oh, except this one. This one is, I need to… I'm going to…
Ludmila Molkova 00:09:49 There is a comment on it to move it.
Trask Stalnaker 00:09:52 Yeah.
This one also… So I lied, they're not all gone, but they're… they're in… I'm going to go ahead… did we… did this one get… No, I don't think I've seen this one.
Alright, and I will leave this open for myself to, I'll chat with, Natkumar, About that… Process… Entry point… to replace Process EXE, okay, it looks like this is… just needs SIG, approval.
Oh yes, let's… Look at ready to be merged.
Remote process… oh, this has a lot of… Green check marks… let's see, what do we got here?
Go for a Bradunct review…
Ludmila Molkova 00:11:20 Oh, I think there are… The only reason I didn't merge it was that we were discussing if we want to stabilize or see attributes without entity, and I think Braden replied, but I didn't see his reply.
Trask Stalnaker 00:12:12 Josh, since you're… Closest to entities, do you have any… But…
Josh Suereth 00:12:23 I think we should require this to stabilize with ANST, yeah.
I mean, particularly these metrics, Braden calls it out, which is just, they are… The entity is as important as the metric name. I mean, they're, like, really tight at the hip.
If you've used the process metrics and the new host metrics receiver with how that works, It… I… I don't see how you can stabilize one without the other.
this is different from, like, many other metrics where they rely on service, which is basically the state, right? This is, like, legitimately, this is not relying on service. This is… has to be against a process, and that ID is really important to the metric, or the metric falls apart. So, the most important attribute you would have here is that process ID. You should stabilize the entity that has it.
When you stabilize the metric.
Ludmila Molkova 00:13:33 Oh, I… they… I don't think they're stabilizing metrics yet, they're only stabilizing attributes.
Josh Suereth 00:13:43 Oh, they want to stabilize process PID, but not the entity where it's used or reported?
Ludmila Molkova 00:13:47 Yeah.
Josh Suereth 00:13:49 Yeah, no, I think… I think we should… we've been… we've been trying to do both at the same time.
Trask Stalnaker 00:13:58 So…
Josh Suereth 00:13:59 Like, what is the release candidate… like, are… does it make sense to have a release candidate with just attributes and no… if they're not stabilizing the metrics and they're not stabilizing anything else, what is the release candidate?
Trask Stalnaker 00:14:09 purpose, yeah.
Daniel Dyla (Dynatrace) 00:14:33 I think it doesn't have no value.
For it to be stable, because it's currently… Like, it's used in… Resources, even if those resources aren't stable, and we say it may be removed from this entity or added to that entity.
the definition of process PID could be stable itself. Like, it's definitely used today.
I don't think it has no value at all, but I see both.
Trask Stalnaker 00:15:10 As a res… just as a resource at… just a… not thinking entities, but just as a standard resource.
Daniel Dyla (Dynatrace) 00:15:16 Yeah, exactly. Like, I'm an SRE looking at monitoring data, I want to know what this process.pid means.
I want to be sure that it's always going to be an integer and not changed to be a string, you know, whatever I… whatever it is that you're hoping to get out of stability.
Ludmila Molkova 00:15:47 At the same time, the… Resource attributes, if they are said explicitly.
They don't even need to come through.
Semantic conventions, they don't need to be there, they are not changed without user Changing it in there.
Whatever, declarative config or other config.
I'm… I'm thinking, if there is… If host metrics, or if resource detection, processor, and collector.
Emits these attributes automatically is just attribute stability is a blocker for that component stability.
And then it makes sense.
Josh Suereth 00:16:33 Yeah, we've been updating the… we, I mean, Dimitri, but the entity SIG has been updating that component in the collector to be entity aware, and to, like, have these actually use the entities, so I… you know, I don't know where you are with that, Daniel, but I, I think we should set a standard of basically, putting these models as release candidate, because I… again, I don't really see it changing significantly, and if it does, I think it will be breaking in some fashion.
So… I'd… I guess… There's a question of, like, why would we… do this, it's because you can use a resource, but why wouldn't we stabilize entity at the same time? Just because we don't understand it, or we don't like it? I don't know.
Daniel Dyla (Dynatrace) 00:17:27 I mean, you could use it in resource, you could also use it in, like, I don't know, if you're logging system events, and you want to know what process something happened on, I think just having the attribute in the registry has value on its own, even if it's not in any specific semantic convention model.
Josh Suereth 00:17:46 kind of. The problem is we don't have any enforcement right now. Like, that's one of the things we've been trying to figure out. Like, I don't know if you saw, Weaver can now, there's a… there's a PR where we can now enforce resource attributes.
And we can make sure the entity association is linked correctly.
So, it's doing it vicariously, where it's, it's, Weaver is only using the model, but we can actually enforce for process metrics, for example, that, the… Process attributes are on the resource that are required for the process metrics to work correctly.
But that relies on the entity.
And it relies on the entity association and the model.
It doesn't rely on it in OTLP, but it relies on the entity association in the model, which means it would rely on this, like, theoretically, you should have this be stable, so that we have the links be stable and all that kind of stuff, like, I… I understand what you're saying, and I think… if we play devil's advocate, we could say it's not that there's no value, like, having these attributes defined as stable is great.
But in practice, until we actually have them aligned around, like, a resource bundle or something.
we run risks as well, right? Like, I think…
Daniel Dyla (Dynatrace) 00:19:06 I think you and I are talking about two different That… like… two different practitioners, I would say. You have… person A, who wants to do everything exactly the right way, and is following, like, the semantic inventions and Weaver, and has very advanced infrastructure.
And you have person B, who has, like.
is logging something in their system, doesn't really know that much about OpenTelemetry, and they're just like, I need to know what name to use, because I want to log which process I did this on. And they look up the semantic invention, they find an attribute called process PID, and they're like, that sounds right, and they just tack it on.
And both of those people you know, it… it's two different ways of working, for sure, but I think they both exist. And this… I don't see any reason not to… promote attributes. They're not… like, the process PID is not… inherently only a part of the entity. It could also be used in other places.
So waiting for an entity to… to stabilize it, I don't think is necessarily…
Josh Suereth 00:20:24 Yeah.
Daniel Dyla (Dynatrace) 00:20:25 deal.
Josh Suereth 00:20:26 the counterargument to that, is usually we rely on having real instrumentation that produces these things, and that's why we rely on the signals. So, for example, you shouldn't just be… going through and stabilizing a crap ton of attributes unless there's real instrumentation out there that provides those attributes. That's true of any signal. That's also true of the resource, right? The reason we can stabilize process attributes is because we have resource detectors that provide that attribute.
We have resource, we have the, process, attribute processor thing.
sorry, resource detector processor in the hotel collector that makes these, but, like, you know, one of the things we want to avoid is… having a whole bunch of crap here that's theoretical that doesn't have instrumentation. So that's… that's why we went with the… you have to have a signal associated with an attribute before you define the attribute.
To kind of ground things on real-life use cases. What we're saying here is, like, the process… yes, there's a lot of real-life use cases around process. My thing is, we have a real-life use case, and we have a real-life entity, so why wouldn't I do both at the same time?
I'm not saying we don't stabilize these, I think we should. I think we just stabilize the entity at the same time, too. I don't see any… I have no concerns with that myself.
Right?
Daniel Dyla (Dynatrace) 00:21:44 Yeah, I also don't have concerns with that.
Josh Suereth 00:21:46 Yeah, so I'm saying, like, we should stabilize this, but I don't understand why you would not stabilize all the places where the attribute's used when you stabilize the attribute, because we're trying to ground on real-life use cases here.
Trask Stalnaker 00:22:02 Have we stabilized, we stabilized the service as an entity, right?
Josh Suereth 00:22:07 Yep.
Trask Stalnaker 00:22:09 I was just wondering, because we… we haven't stabilized entity as in the specification, Yet, or… Did we stabilize it in Proto yet?
Josh Suereth 00:22:22 No, the proto's still… it's still experimental, but it's also, it's in a place in the proto where we can't make changes to it. Basically, if we wanted to make changes, we would have to kill what's there now and make a new thing.
Sorry, we can't make… significant… like, we're very limited with what changes we could make, would be the way to phrase it, yeah.
Trask Stalnaker 00:22:52 Okay, why don't I just ask any reason not to stabilize… Cool.
Thank y'all.
Odd… Support for file system locks.
Ludmila Molkova 00:23:41 The last time I checked, there were some open discussions.
Trask Stalnaker 00:23:44 Yeah.
Alright.
Let's… Oh, it's a good triage session. We… did get… A… a topic? Josh?
Josh Suereth 00:24:05 Yeah, so, I just want to talk about, I think, we federated SEMCOM, Or we're federating it. Jenna is the first kind of experiment. We have an OTEP that, again, I encourage everyone to read. Lyudmila has one, I have one, they depend on each other. Lyudmila's first, then mine. Please read those and review them.
But what I wanted to talk about now is, like, the purpose of general SEMCOM as we start to federate, and kind of how we think about ourselves.
If you want to go through the OTEPs quick and cover them, maybe, Ludmila, is there any… are there any open questions on the OTEP we should talk about here?
Ludmila Molkova 00:24:43 Not really, I was going to add it to the agenda and ask you if we're ready to merge. I've been asking some other folks to… take another look, but I think it's ready.
Trask Stalnaker 00:24:57 I… yeah, I was… that's why I was pulling it up, was to ask if we can merge it.
Ludmila Molkova 00:25:03 Let me bring it up on tomorrow's, spec call, and give people a few more days to finish, and then let's… let's try to merge it by the end of the week.
Trask Stalnaker 00:25:14 Awesome.
Josh Suereth 00:25:15 Awesome.
Trask Stalnaker 00:25:16 Alright, back to you, Josh.
Josh Suereth 00:25:18 Well, can you pull up mine then, too?
Trask Stalnaker 00:25:20 Oh, yeah.
Josh Suereth 00:25:21 Because I don't think there's been pretty much any comments in, like.
Trask Stalnaker 00:25:25 Well, yours is still in draft, if I recall.
Josh Suereth 00:25:27 Oh, I'm gonna pull it right. So, if we merge the Melas, I'll pull mine out of draft and remove the stale label.
Ludmila Molkova 00:25:33 Okay, there are 59 comments on it. No comments.
Josh Suereth 00:25:38 Well, no, I think I commented on a lot of those, but there's some recent ones.
Yeah.
I also… GitHub has the thing where sometimes you respond to a comment, and it, like, shows your response, but then it doesn't show the response to your response in the thread. It's been doing that a lot. Anyway… There's a lot.
Trask Stalnaker 00:26:00 I bet.
Josh Suereth 00:26:01 Here.
Trask Stalnaker 00:26:01 If you do the whole, like, on files change tab, if you reply over here, Yeah.
You're basically, starting a review.
And then you go, go, go, and you submit it, and it submits all of yours as, like, this bundle down lower, which is really confusing.
So I avoid that, and I just do… The more noisy reply, reply, reply separately.
Josh Suereth 00:26:31 I'll have to do that going forward. I do… I do the other option.
Trask Stalnaker 00:26:34 It feels right, like, I understand, like, you want to create less noise and bundle up your thing and just… send it, but yeah, I… GitHub doesn't render that super amazing.
Josh Suereth 00:26:48 Nice.
Okay, well anyway, back to the other topic. I think, so we're federating semantic conventions, which means we're going to have… yeah, somehow we destroyed tabs for me, I couldn't make tabs work. Anyway, we're going to have, a bunch of small repos outside of General SemConf. And so, you know, what does the General SemConf do? We're kind of the core… group around SEMCOF and making sure this whole ecosystem hangs together.
Like, the way… the way I see this group working is we want to make sure that folks are successful at defining, their… This has always been true, but folks are successful defining their little aspect of telemetry, that things that need to get elevated into general so that people can share them can do so successfully.
That we have a notion of what stability means to keep the ecosystem healthy, that we have a notion of what schema means that can be shared, so we can all share these things, evolve them, all that kind of stuff, right? Like, I think that is… kind of what core becomes a little bit, and we need to have good judgment on when something should be federated, when something needs to be core.
evaluate that, but the thing that I also want to make sure we're doing is providing guidance to these subcommittees as they go, and as the subcommittees go, bring back the knowledge and lessons that they have from their time writing conventions.
Where does that live? That lives in our How to Write Senkovs. If you think about, Sorry, this is going to be a tangent, because I'm a little tired today, so my brain is all off on weird things, but, you know, when you work with agents and you tell them to write a skill, you're teaching them how to do something, right?
Our How to Write SEMConv is basically both an agent skill and a human skill.
all in one, like, how to do the judgment aspect of SemConv, how to think about writing SEMCOV. So I just want to call back, like, I think with this group, as things start to shift into federated, we might have less and less things to do in this meeting, we might be able to drop the frequency of this meeting, that's great.
But I would love if, as a group, we could come together and try to make sure this guidance is getting written down and captured in a way that people can use it, that they can understand how to federate, and that we're kind of setting everyone up for success.
So this is kind of a call to action.
But I don't know, would it be useful to look through what we have now and kind of identify weak parts that we think we could improve?
Trask Stalnaker 00:29:27 Sure.
Josh Suereth 00:29:30 Okay.
Trask Stalnaker 00:29:39 This is the non-normative…
Josh Suereth 00:29:42 It's under Doc's How to Write Convention, so I was pulling it up. I'll put it in chat, I guess?
Yeah, there you go.
So if you look through here, the, you know, we set this up early with a bunch of things, and there's a couple sections and best practices about when to define new conventions, and then if you just search for to-dos.
you'll see, how to stabilize existing conventions. We have a to-do about how to make a migration plan.
Which I think is actually a big part, that we need for SEMCOMF. We have a to-do for how best to define metrics. We have a to-do for how best to define events or logs, right? We added the entity modeling guide, and I think the span guidance is really good here, but there's still some to-dos that we kind of need to come back and bring in.
Maybe this relates to our earlier discussion about how do you stabilize a convention? And should you stabilize the entity at the same time? But these are kind of two big ticket items that I see needing some help and needing some folks to write. Go ahead, Christoph.
Christophe Kamphaus 00:30:58 For metrics, I saw that in the general sumconf, We had some guidance already.
Maybe it's just a matter of moving it over.
Ludmila Molkova 00:31:09 Or naming, probably.
Christophe Kamphaus 00:31:12 Yeah, I guess so.
Josh Suereth 00:31:14 Yeah, we have naming guidance. This is about how, like, the process of writing semantic conventions. Like, when do you add a metric, what purpose do metrics serve, how to think about it, that sort of thing.
Like, if you look, there's a stat… there's one specific to status metrics, so if you click on status metrics there.
On the left, in the navbar? Yeah.
This one talks about, like, what is a status metric, what does it mean? You know, how is it different than an entity? How to name this thing. We put this together to help with, specifically for Kubernetes, because there were a ton of status-like metrics with, like, kubestate.
As guidance for people to think about how to define metrics in that way. Does that help, Christoph? Like, I think we need more things like this.
Christophe Kamphaus 00:32:05 Yep.
Ludmila Molkova 00:32:09 I think the metrics one is the trickiest one.
For events, for logs, I think we can take an action item in the log seek to write this one, and I think we… It would be an easy one to do.
Josh Suereth 00:32:32 Cool, would… are you, I don't want to overload you, but is that something that you could add to the agenda for the log sig, and see if we can get someone to sign up to do it?
That'd be awesome.
We don't have a metric, SIG, but maybe I'll add Maybe we can talk about it.
tomorrow, too. We'll see. I think this is the right place to talk about it, honestly. The metrics part.
Trask Stalnaker 00:33:07 On the agenda.
Josh Suereth 00:33:11 The other big one, is actually this notion of how to stabilize and do migration plans. I guess one question, maybe this is for Trask and Ludmilla, do you think that that… guidance is something that will kind of evolve as we do the Gen AI, federation, that we could write down as we do it, or… Should we try to kick off, like, somebody writing that now ahead of time?
Trask Stalnaker 00:33:37 So, do you mean, by migration, you mean from, like.
de facto stable to stable, stable to stable, like, breaking changes, how to deal with breaking changes.
Josh Suereth 00:33:50 Yeah, like, this would be guidance around, you know, you have de facto stable, so how do you deal with de facto stable? We already know how we want to do it, we have a template, we could write that down, but now with Federated, let's say we come out with, like, a 1.0 of Semcov for GenAI, and then you decide a year from now you need a 2.0, what… you know, what is the criteria we want for that? What kind of consideration should you think about, and how… what's… what's our process, if you will?
Ludmila Molkova 00:34:20 We didn't have any, any major version bump.
And some confiat.
We can write the theoretical.
Trask Stalnaker 00:34:30 I mean, I kind of considered the de facto stable to stable.
Ludmila Molkova 00:34:35 Yeah.
Trask Stalnaker 00:34:35 HTTP, what we did with HTTP.
Josh Suereth 00:34:40 Yeah, I'd call that a major version bump, honestly.
And I think the lack of major version bumpability of SemConv is why we're federating. Like, it's just… it's a huge problem.
Ludmila Molkova 00:34:57 Yeah, I mean, we can write it, we even have the configuration options written down in the semantic conventions, so we can make it very simple.
Trask Stalnaker 00:35:04 Oh, yeah.
Yeah, I don't know if you saw that, Josh, in, I can find the snippet… Or some… And… So… Yeah, so we've got… so this is the old style, here, just for backward compatibility, but now you can… break it down, and so DB… some comp, what version you want, whether you want to dual emit, and I think there's one more option. Oh, if you want to opt into experimental stuff.
Josh Suereth 00:35:53 That's cool, I like it.
Yeah, so it sounds like we could write… We could write the, how to do… de facto stable-to-stable releases. And then, I do think that if we ever need to do a 1.0 to 2.0, That it would be the same process, basically.
Ludmila Molkova 00:36:21 We don't have an issue created for this one, right? We have issues created for how to write signals?
I'm going to go ahead and create an issue for… How to stodilize, or how to measure version bump.
Trask Stalnaker 00:36:45 Oh yeah, that's another, benefit of the GenAI split out. We moved 70, 80 issues over.
Although, man, there's a lot of issues here in this repo.
Someday.
Josh Suereth 00:37:05 I should show you the proto-repo, and how I triaged all of them, and I still haven't fixed more than two.
Trask Stalnaker 00:37:14 Yeah.
Josh Suereth 00:37:15 It's not so much about…
Trask Stalnaker 00:37:17 Yeah, I feel like it's not so much about fixing Actually making changes as much as just Going through the backlog, and… Cussing out things that are… we're not gonna do.
Josh Suereth 00:37:31 Yeah, we have a lot that are… needs triage, right?
I guess the next question is, since we have 30 minutes left in the meeting, or 25 or so, You know, should we start triaging bugs in this meeting, too?
Just do, like, one or two a week to start on it.
Ludmila Molkova 00:37:53 By bugs, you mean ischeous, in general.
Josh Suereth 00:37:56 Yeah, well, the ones that are triage where you don't know what they are. Yeah. Is it a feature request, is it a bug? We could basically immediately say, this is a feature request, we'll ignore it for now, but if it's like a… there's an issue with this Zemconv, I feel like we should find a way to prioritize those.
Ludmila Molkova 00:38:13 Yeah.
Trask Stalnaker 00:38:18 Sue, I mean, I just wanted to share what… we're doing in the Java instrumentation repo that I kind of like is… Just, we are scaling issues at some point.
And saying that, you know, we're closing it, just to maintain our backlog. Anyone who would like to work on this is still welcome to do so. We can reopen it at that time.
I just think it's… probably unrealistic.
Or… To go… to get… for us to get through.
The backlog, unless somebody, you know, ends up having a lot of time.
Josh Suereth 00:39:07 I… I think that's a one-person-rips-through-it task, or… Yeah, that could be a… you try to do a first pass of, like, categorization with AI, like, hey, is this a bug, or is this a feature?
And then you just validate the list it comes up with instead of doing the whole thing? Yeah.
Trask Stalnaker 00:39:27 That would be… Interesting, yeah.
I mean, kinda, there's a lot of stuff that… Oh, this was actually commented on in the last year.
There's… there's a lot of things that… I just… I don't know what… The value of having them in… semantic dimensions could be different.
Value of having things in… when we have so many issues.
what is the value? I guess it's that people… I guess we've got so many different areas, is maybe the thing that… There's certain people who really do care about.
Josh Suereth 00:40:20 Yeah, actually, that 3705 one, we probably do need to talk about. If you… I think that one was recent, I remember this in chat.
I don't know if you guys talked about it last week when I wasn't here.
Trask Stalnaker 00:40:38 3705.
Josh Suereth 00:40:40 Yeah, this one.
this is… this is one where, basically, the code gen broke.
If I recall correctly, because of metric naming issues.
Because it turns out… The features that we added to prevent metric naming breakages didn't check metric name… or, sorry, to prevent attribute naming breakages, maybe didn't check metric names, or, like, the code gen hints that we have to try to avoid them didn't apply. Yeah, this is another dot underscore issue, but with the metric names, and then the constants of the metric.
So, it's the exact same thing, I think it has the exact same solution, but it… this is something that, like, it says triage needed. Yeah, we… we absolutely should fix this, and we absolutely should triage it. Like, we… you know, we need to fix our policy if it's not already there, we need to add the code hints if it's not already there, and we need, the helpers and weaver to, like.
Automatically do this for you, right?
Ludmila Molkova 00:41:39 Yeah, I didn't notice it. It's a pretty nasty bug.
Josh Suereth 00:41:43 Yep.
But that's… that's the thing that, because we have 680, this is urgent, we should address it. I keep freaking forgetting about it, so, I don't know, that one, I think I'm… I don't know if I'll have time this week, but I might… if nobody else wants it, you can assign it to me, and remove triage, and just say accept it, or whatever we put, because that one… that one needs to get fixed soon.
Ludmila Molkova 00:42:08 I'll try to fix it right now.
Josh Suereth 00:42:10 Okay.
Ludmila Molkova 00:42:12 And I think we need a new release of semantic conventions.
Josh Suereth 00:42:16 Yeah, we're gonna have to cut another release, yeah.
I think that was reported Friday, so I had kind of forgotten about it.
Trask Stalnaker 00:42:28 Daniel submitted a bug, let's talk about.
Daniel Dyla (Dynatrace) 00:42:31 Yeah, I submitted two. I wasn't entirely sure whether either of them would be considered bugs, but now that I've thought about it more, I think, kind of, they both are.
RPC is release candidate right now, too, so it's probably a good time to… talk about these things. So, open…
Trask Stalnaker 00:42:46 Just to clarify, the streaming stuff is not our… is not going to be part of initial stability.
Daniel Dyla (Dynatrace) 00:42:54 Oh, perfect. That's excellent news, because it's pretty broken.
Trask Stalnaker 00:42:57 I would still like to hear… yeah, we would still like to hear your thoughts on it.
Yeah, so… Yeah, we had a lot of questions about streaming. We were very… too nervous to make it stable, but we do want to make sure we have a path forward so that could affect things.
Daniel Dyla (Dynatrace) 00:43:14 Open feature uses server streaming as, like, a notification mechanism, so each SDK connects to a server called FlagD, and when the configuration changes on FlagD, a event is sent back over the stream to each client, telling it, here's the new configuration.
The way that the current instrumentations all work.
is when the stream is created, the span is started, and when the stream is ended, the span ends. Which, in the ideal case, is never, because that stream should last the lifetime of the process. Now, in the Flag D-specific case, they're actually using deadlines, which it could be argued whether or not they should be doing that anyways, but they use a 10-minute deadline that restarts the stream every 10 minutes, because… the request ends with, like, deadline exceeded, it… the span is shown as a failure. So every 10 minutes, you get a failed span.
And… with no children. Like, that's the whole… it's a very weird experience.
The… the modeling of that I guess, like, I… I… suggested… one particular model, but I can't say that I have spent a lot of time thinking about it, but essentially, it is to… End the span when the stream is established, and then treat messages over that stream as some other telemetry type, whether it's a new span or whatever.
That's… Just in order to… Have… Any telemetry at all.
Because if you never end the span, it'll never get exported.
And then in the flag D case, which I don't know how well this generalizes, but it's essentially being used as, like, a reverse request. Requests are being sent from the server to the client.
Like, the causal relationship there.
those… Operations happening on the client are children of server operations.
And it's possible that modeling it that way might make more sense.
Obviously, that's a big, big change over what we currently have, so… It would take some additional thought and prototyping and some stuff like that.
But certainly, there is a lot of… and the other one that I opened is more about the failures. There's a lot of guidance in the GRPC community saying to use deadlines for everything.
It does not specify that Streaming is exempted or anything like that?
It's… it's unclear whether it's a good idea to use deadlines with streams, but the reality is that People definitely do.
And you end up with these deadline exceeded errors and non-okay, spans all the time when you're using streams.
So, possibly there should be a configuration to say, this is not an error.
bleed y'all.
Trask Stalnaker 00:46:34 Miller.
Ludmila Molkova 00:46:37 Yeah, I'm thinking, like, from… RPC conventions, the… In a generic case, right, we don't know anything about the use case, what can we do for streaming?
And representing the whole thing as a span sometimes makes sense, sometimes doesn't.
Maybe we should mention that, like, the streaming spend should be… Enablable or disablable.
Independently from the client's pens.
But for… like… the fact that these spans are long, and they should end at some point, right? If you gracefully shut down everything, they should end at some point. They are long, they're useless, if they are too long, right? But they should end at some point.
At the same time, we should probably, eventually, when we do the next phase of RPC for streaming, we should have Stream started, stream ended, number of active streams, or number of messages.
And so on, and maybe events would be a better representation of it. Maybe we should have a request ID instead of the trace ID and span ID for the whole operation, or some form of correlation that's not a very long span.
Daniel Dyla (Dynatrace) 00:48:07 Yeah, I agree with everything you said. And I mean, yes, the stream will eventually end, but if it starts at the start of the process, and it ends at the end of the process.
It certainly doesn't provide any value.
Christophe Kamphaus 00:48:25 You could use, trace.
To propagate the, Trace ID to the, Stream has started and stream has stopped.
And for all the metrics.
And the individual, stream events.
Daniel Dyla (Dynatrace) 00:48:45 I don't know what… Can you rephrase that? I'm not sure I understood what.
Christophe Kamphaus 00:48:49 Sure.
So you could have a long-running trace.
From when you started the stream to when it ends, and still emit events When it has started, when it has ended, and for any message, to be able to correlate them.
Daniel Dyla (Dynatrace) 00:49:07 Yeah, you certainly.
Trask Stalnaker 00:49:08 Of a span for the… the long… Peace.
Christophe Kamphaus 00:49:12 Yeah.
But I think you could use it just to correlate the other events.
Daniel Dyla (Dynatrace) 00:49:20 But if you have a server that's running for, you know, you have an SDK, Connected to the server, and that… Is running for days or weeks.
You'd be emitting spans that reference a… you'd be emitting events that reference a span that's not in your backend.
And won't be.
Trask Stalnaker 00:49:38 Mmm…
Daniel Dyla (Dynatrace) 00:49:39 for weeks.
Potentially.
Because we don't export until the end of the span.
Christophe Kamphaus 00:49:47 Yeah, the events you would still, export, I think.
Daniel Dyla (Dynatrace) 00:49:52 Yeah, you'd get the events, but it would say, like, reference this trace ID, and then when you went to look in your tracing system, there wouldn't be one.
Christophe Kamphaus 00:50:01 Yup.
Ludmila Molkova 00:50:02 It's still fine, Ricky, if you can correlate them, even if you don't have a span. Like, you're… what you're saying, the span is useless anyway.
Daniel Dyla (Dynatrace) 00:50:11 Yeah, I think the span… And this is… I mean, you have similar problems with, like, server-sent events.
I think at least in the client streaming case, or the server streaming case, where you're streaming stuff back from the server.
ending the span when the stream is established. Like, if you look at the stream operation as a… That the operation is establishing the connection and the stream.
That operation is ended when the stream is established.
And then you would have events that reference that.
as the… You know, each message comes down the stream, and then an end… a stream end message, maybe.
Ludmila Molkova 00:50:57 Ideally, you have both. So, for example, for our PC, we scope them to logical things.
And there is also a physical aspect, let's say if you do both your PC over instrumented HTTP, the HTTP span would be the one that Implements the original request, and it hands when the stream is established.
if it's not over HTTP, I think gRPC folks have the physical part of the… the, protocol instrumented, too. So, and then it's… you kind of see this as a transport level thing.
And going down, it can be the socket, connect, instrument, DNS, and whatnot.
Daniel Dyla (Dynatrace) 00:51:45 Yeah… But in gRPC, multiple streams are multiplexed over a single HTTP connection, so creating and ending streams doesn't always do that.
Ludmila Molkova 00:51:57 It's still a request.
Well, anyway, so the mental model is that the RPC conventions are logical, and there is a physical part, and you would see this if it's… this part is instrumented.
currently not in scope of RPC conventions to define it, because it's protocol-specific.
I think the action item for RPC conventions is to document that Aw.
The streaming spends, or… Not required, recommended. You should be able… instrumentations may provide option to disable them.
Daniel Dyla (Dynatrace) 00:52:46 Disable the streaming spans entirely.
Ludmila Molkova 00:52:51 Yeah, if you're saying they're useless.
Or they are useless or harmful. If they are harmful, we should disable them. If they are useless, I don't know.
Daniel Dyla (Dynatrace) 00:53:02 I'm not sure where you draw the line between useless and harmful, but I… I linked… when I created the issue, I linked an issue in the flag D repo, which was originally created by an OpenTelemetry demo developer.
that raised it with them. There's… It's just creating, like, 10-minute long failed spans.
Constantly, one after the other. That's all you get.
So, yeah, I would say harmful.
Ludmila Molkova 00:53:39 And if they were not failed, Would they be harmful?
They show the reality, right? They show that you're establishing a stream, and then you're establishing a stream again.
This shows the reality, and maybe this reality is not super useful, but it tells you if you were able to even start a stream, and how it ended.
Daniel Dyla (Dynatrace) 00:54:01 Yeah, and that's why in the issue, I just asked for a way to… not mark those as failures. Like, in the streaming case, it should be okay. It… deadline exceeded.
Maybe as an opt-in… you know, I don't know what the default behavior would be, but for streams, exceeding a deadline is, like, an expected case a lot of the time.
So it's not a failed operation.
Ludmila Molkova 00:54:30 Trust, can you check of what we do for a deadline? I think for clients, it's an error by default.
Daniel Dyla (Dynatrace) 00:54:36 It is definitely an error. It's, it's… if you look at… Footnote 2 there. It just says anything non-okay.
Ludmila Molkova 00:54:44 Right, and for servers, maybe.
It's… different.
I think it's in the response code, the classification of what an error is.
Daniel Dyla (Dynatrace) 00:54:58 Yeah, sorry. Number 4.
Ludmila Molkova 00:55:07 Oh, so we… it's in the GRPC for a general, we don't…
Trask Stalnaker 00:55:12 Oh, right.
Yes.
Ludmila Molkova 00:55:23 Bizarre clients.
Trask Stalnaker 00:55:24 for client.
Daniel Dyla (Dynatrace) 00:55:25 There you go, yeah.
Trask Stalnaker 00:55:26 Everything except OK… And for server… so for server, deadline exceeded is fine.
Ludmila Molkova 00:55:36 No, no, no, it's.
Daniel Dyla (Dynatrace) 00:55:37 No, that's an error.
Trask Stalnaker 00:55:39 Oh, the following… oh, okay, thank you.
Okay.
Ludmila Molkova 00:55:43 We took it from… Somewhere… Anyway…
Trask Stalnaker 00:55:49 A7… A66?
Ludmila Molkova 00:55:53 So we're 72?
Trask Stalnaker 00:55:55 Yeah, one of those two.
Oh, this is the metrics. I think it's A72.
Ludmila Molkova 00:56:10 Oh, I think we, we, the, the tracing is quite a… yeah.
So, what we're saying that These are the defaults for instrumentations.
That don't have a better idea.
And instrumentations can… Mark something as error.
Based on whatever additional context they have.
I can probably make it more specific and say that it should be configurable.
And then, in theory, we can say.
It probably applies to any other conventions, that instrumentations should support the default configuration mechanism that classifies Certain error codes.
In a certain way. I don't know if we can come up with generic configuration story, but it's pretty generic in general.
Trask Stalnaker 00:57:11 Yeah, I mean, we get this request even on HTTP. Some people want… 404 is to not show up as… errors.
But I think the interesting question to me is whether… It's… standard enough practice in GRPC to… just… Make deadline exceeded on streaming spans.
Not an error.
by default.
Daniel Dyla (Dynatrace) 00:57:50 Yeah, that's where it becomes kind of a tricky story, because… if you start looking into deadlines and keep-alives and the… recommendations of the GRPC community, they very strongly and consistently recommend deadlines.
But never anywhere do they mention anything about streams or unary. Everything is kind of… The way everything's worded, if you read the whole blog post, is usually… makes me think that they're talking about unary requests.
But they never say that specifically. So you end up with people like the open feature community that… Are like, okay, we should use deadlines everywhere.
and… The streaming is not exempted in any of that advice, even though if you closely read the article.
It is arguable whether they're talking about streams or not.
So, is that the advice of the maintainers? Maybe? Maybe not? But certainly, it's one reasonable interpretation of the advice available in the wild.
Ludmila Molkova 00:59:04 Yeah, the tricky question is, how do you distinguish deadline exceeded because of server never replied, to deadline exceeded because server replied, and… It's just you had a long stream.
Daniel Dyla (Dynatrace) 00:59:18 Right, a long stream where you're like… you're running a backup process that's expected to end at some point. You're like, I want this to finish within 24 hours. You may set a 24-hour deadline.
totally reasonable. If you're streaming… A video camera that is just, like.
you know, a constant 24-7 rolling, then that operation is never expected to end. Why would it have a deadline?
Ludmila Molkova 00:59:49 No more like a client started the request, and I never got to reply from server at all, versus I've got a reply, and then the stream ended abruptly.
Like, on the instrumentation level we operate, we cannot distinguish one from another.
Well, we can, probably. It's just part…
Trask Stalnaker 01:00:15 I feel like whatever we do with streaming.
the… I mean, there's just so many creative use… use cases built around streaming.
But… Not gonna work for everybody.
Daniel Dyla (Dynatrace) 01:00:30 Yeah, so that was more the crux of the other issue, is, like, is span, as we have it today, even the… The appropriate telemetry abstraction for streams. I think it would… probably look more like the messaging SEMConf than the HTTP semconf, if you built a streaming semantic convention from the ground up.
It's much more similar to messaging than it is to, like, a transactional anything.
Ludmila Molkova 01:01:04 Well, it's different from messaging, because in case of messaging, we have the carriers that have context. In case of our PC streaming, we don't, and it's just arbitrary. So I think the… Solution for this long-running special cases is to disable generic instrumentation and write protocol-specific application-specific instrumentation from scratch and invent.
Context into their message payloads.
We can probably write it down. We can make it part of the convention to say that.
Trask Stalnaker 01:01:52 Cool! This was really good to have discussion around that, and… and timely, because, we are, we are… I think we're… Lamila and I are chatting with the GRPC folks later this week, as we try to… get the RPC SEM comp to stable, and this… Does look like… I know I said earlier that Streaming wasn't part of stability, but… I think… It… is based on… I think we just didn't go into anything more, we just said.
We would capture that one outer span… So, probably… we probably do need to think…
Daniel Dyla (Dynatrace) 01:02:43 I would recommend splitting streams out as specifically not a part of the RC, because… I think it needs a lot more thought.
I'm not sure that there are any streaming use cases… beyond, like, I'm just streaming a file over the network real quick here. I'm not sure there are many streaming use cases that are well covered by the existing semantic convention.
Ludmila Molkova 01:03:19 I think this is the question, do we not instrument them at all?
Trask Stalnaker 01:03:23 Yeah.
Ludmila Molkova 01:03:24 to provide at least something, and I think something… That is, disablable makes sense.
Trask Stalnaker 01:03:35 I like the idea… I like the idea of… or thinking about… more about the event.
Option.
At the same time, I mean, this spans… a span over it. It makes so much sense, and yet… When you, like, There's… Yeah, all these use cases.
I don't know. Yep, we're… we've hit our time, but yeah, we will.
Ludmil and I will chat more about that.
Try to make some public comments there.
Thanks for…
Daniel Dyla (Dynatrace) 01:04:14 Yep, sounds good, thank you.
Ludmila Molkova 01:04:15 Thank you.
Armin (Dynatrace) 01:04:17 Thank you.
Trask Stalnaker 01:04:18 Fiat.
Christophe Kamphaus 01:04:19 See you.
