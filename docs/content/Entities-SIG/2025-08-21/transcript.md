SIG: Entities SIG
Date: 2025-08-21
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/f-dxoBvYFn5aXTl5CoRmXH3CbnqW6ILb5mnix3-TQGEJKWTDp19cAJYxhYZKsVfa.4d8K65HvIDPz0l-7
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:50 Hey folks, I'm Loli.
How are we doing?
**Daniel Dyla (Dynatrace)** 01:56 Good, how are you doing?
**Dmitrii Anoshin** 01:57 ….
**Josh Suereth** 01:59 Not bad, I, … My AC died, and when I went to go, when we went to go look at it, there were vines all over the, like, extra panel box, and … yeah, they were poison.
So… Little distracted. Little distracted.
….
**Daniel Dyla (Dynatrace)** 02:19 Is your AC at least working now?
**Josh Suereth** 02:21 No.
They had to order a fan, so tomorrow, my AC will be working.
So, it's, it's, … I mean, it's only a Pittsburgh heat wave, so it says it's about 75 in the house right now. That's, that's actually pretty chill. But it was, it was 80-something when the, 85, I think, when the AC died.
Sorry, I… for those of you who speak Celsius, I don't even know what it is, I don't know, like, 25 or something?
I don't know.
Somewhere around there. Alright, … let's get start… oh, I'm not presenting, am I?
**Daniel Dyla (Dynatrace)** 02:59 I added the first topic here. It was from the… spec call on, Tuesday.
We talked about the Prometheus info metrics.
Which is obviously very entity-related. I think long-term, that's kind of the… the plan. … I added it here because I didn't know whether we would have more discussion from that or not. I mean, it was a fairly well-covered topic on Tuesday, and… There's only 3 of us here, and I think we were all there.
**Josh Suereth** 03:31 I do think we need to talk about… what we want to… whether we want to block things in CENCOM for now or not. I think the decision was to block.
SimConf until we sort out relationships, is that right?
**Daniel Dyla (Dynatrace)** 03:49 Yeah, I mean, so, are the info metrics… Our relationships, … A prerequisite for that?
**Josh Suereth** 04:01 It's….
**Daniel Dyla (Dynatrace)** 04:02 Maybe to fully cover the whole use case, but….
**Josh Suereth** 04:05 I don't think… it didn't seem that way to me.
we need the mapping, I would say, is the important bit, right? So, like… Where's our document? Up here?
I think this one.
So, I put together a tentative one back in the… back in the day, whenever this was, because we don't… I don't remember.
… of… yeah, so there's, like, both state and relationship in cube state metrics that we want to be able to model converting into, … into metrics. So the question would be, like, state. Is this a descriptive attribute on the entity?
And then what is the actual mapping that you would have from an entity type to a metric that describes a particular aspect, right? So… I was thinking that the entity itself is an infometric, right?
Information about the entity.
If there's a particular state that we don't generally report on the entity, but we report sometimes, you can also have, like, you know, slap descriptive attribute on the end.
And you can report a particular descriptive attribute changing.
… And then relationship was the one that's fun, of, okay, if I have a job that has a relationship of owner.
you know, what does that look like? But is owner a relationship, or is that a descriptive attribute?
We haven't sorted that out yet fully, either.
… Yeah, because I think annotations, owner, and labels were the ones that showed up.
**Dmitrii Anoshin** 05:52 Before, yeah. For the owner, it will be problematic to make a descriptive attribute, because owner can be different based on the entity type.
The job, it will be cron job for, like, a replica set to be deployment.
**Josh Suereth** 06:10 Right.
So that one definitely feels like a, … Feels like that's a relationship, right?
**Dmitrii Anoshin** 06:16 Right, right.
Semantically, it made more sense as a relationship.
**Josh Suereth** 06:21 Yeah.
I'm sorry, I didn't… I either didn't fully hear or didn't understand why would representing owner as a descriptive attribute cause problems?
**Dmitrii Anoshin** 06:33 Because for different entities, owners are different, for different entity types. Job is… only for the job as a cron job, but owner for replica set as a DIM deployment.
**Daniel Dyla (Dynatrace)** 06:46 Okay, yeah, so I see what you're saying, like, the owner type may vary based on….
**Dmitrii Anoshin** 06:51 Right. Okay.
**Josh Suereth** 06:52 Yeah, owner is a relationship, but it might have different entity types on both sides.
And… what is it? Is it CronJob, where you have, like… a cron job owns a job, and a job owns a pod, or something crazy like that? Yeah. Yeah.
So… Anyway, this is my tentative thinking for the mapping.
But the thing that we're missing… is I don't think we actually defined the relationship signal at all. Like, what it means, what it is, right?
… This assumes that the relationship signal, basically, you have an entity on the left, an entity on the right, and then a name for the relationship.
Is it a name and a set of labels?
… what do those look like? So that's where… to unblock the infometric, I actually think we could unblock this dead simple info metric of just, if you take an entity and post it as an infometric, good, you're fine.
That's something we'd allow.
If you wanted to do something more complicated of these, like, relationships of owner, right, or a state one, that we want… might want to, like, spend some more time thinking through.
**Daniel Dyla (Dynatrace)** 08:10 What that looks like, or at least define….
**Josh Suereth** 08:13 The relationship data model, and then we can unblock the metric that matches the mapping.
**Dmitrii Anoshin** 08:18 Yeah.
And it's not only a relationship model, we also need to… like, start… working on the NTT signal itself.
Like I said, channel.
**Josh Suereth** 08:34 Okay.
Cool.
So….
**Daniel Dyla (Dynatrace)** 08:39 On Tuesday, I think we were only really talking about the info metrics.
… So I think we can get… You know, start working on that mapping.
What do we want to tell them about the other metric types, though? Is it just, like, weight? Or… Because we probably don't want them to define semantic conventions for, like, I don't know, a labels metric, for example. But we also don't want them to not be able to represent that stuff in the meantime.
**Josh Suereth** 09:15 Yep.
I… I mean, in an ideal world, we'd say, hey, if you care about this, come work with us in the SIG and start making some proposals, so we can move forward and agree, like, this is the way forward. But here's the shape of, like, here's the scope we want this to be in, not just your scope. If you solve it at this scope, you can move forward, right?
So help us do that.
If that works. That doesn't work with a lot of people, though.
I think the three of us are… actually, a lot of people in the spec are exceptions to the rule. A lot of times, it's like, no, I just want to solve my one problem.
Yeah. But for Christoph, I think he might be willing to help us here, if he has time.
**Daniel Dyla (Dynatrace)** 09:54 Okay.
**Josh Suereth** 09:59 Okay, cool.
**Dmitrii Anoshin** 10:01 I just want to mention that we already have implementation of the entity signal itself and the collector in a log pipeline representation, so if they start working on that, they can use that as a reference.
**Josh Suereth** 10:14 Oh, that's good. Does it do relationships?
**Dmitrii Anoshin** 10:17 No, it doesn't, it's just the entity signal itself.
**Josh Suereth** 10:22 It's just, like, here's the entities that we found.
**Dmitrii Anoshin** 10:24 Right? Entity descriptive attributes, so, like, identifying attributes, etc.
**Josh Suereth** 10:29 Project.
Alright.
Cool. … That makes me wonder if entity relationships are even a separate signal from entity, or a separate event, if you will.
**Dmitrii Anoshin** 10:44 Right, right now it's actually a log event, and I believe that's something… probably we can stick to… because introducing new signal just for AMPT, I mean, personally, at this point, seems like an overkill.
But it's definitely something that we have to discuss broadly, like, in more detail.
**Josh Suereth** 11:05 Yeah, yeah, yeah. I… I'm fine using events for that. Okay.
Cool. I think that, that, that, solves that question there. Dimitri.
**Dmitrii Anoshin** 11:18 Yeah, I updated DPR, based on your suggestions. I… Made it.
Like….
**Josh Suereth** 11:26 I updated the, the….
**Dmitrii Anoshin** 11:28 README of the NGTS, … section itself.
And, like, introduced to a separate way to how… Entity B.
set by SDK, whether it's, … push or break… pull… pull model. So, if you… if you go to… File changed.
**Josh Suereth** 11:54 Yeah, sorry.
Okay.
**Dmitrii Anoshin** 11:59 Go to README first?
So here, I put, like, the distinction between two models, how it would be… instantiated.
And then, like, second… Bush-based model we have.
the same additional… I added overview, like, some common scenarios.
**Josh Suereth** 12:32 This is cool, yeah.
Well written, man. This is exactly what I think we needed to describe why this is useful to people.
**Dmitrii Anoshin** 12:40 And everything else is pretty much the same.
**Josh Suereth** 12:44 Yeah, like this, because this was already really good, yeah.
Okay.
Cool.
I think, given that, I can actually just approve this right now.
Cause I don't… like, you didn't make any changes to this, right?
**Dmitrii Anoshin** 13:03 Yeah, sure.
**Josh Suereth** 13:04 Yeah, okay. And this… this actually is exactly… I… I don't think we… I think being short and sweet is better here, right?
So, cool.
**Dmitrii Anoshin** 13:14 And then we can expand on the… Pool-based model as well, which will be more details about.
entity provider, I guess, and all of those things.
**Josh Suereth** 13:25 Yep.
We should probably, if you haven't, update some of these.
**Dmitrii Anoshin** 13:32 I actually addressed all of them, I just haven't pressed resolve conversation, because, I don't know, maybe there is additional… From… Carlos resolved his comment, but let me know that.
**Josh Suereth** 13:45 Sweet. This is exciting. Alright.
Do you need, you… Do you need implementations of this in SDKs?
**Dmitrii Anoshin** 13:55 Right, this is something that we actually put as a requirement, then SDK would need to implement that.
**Josh Suereth** 14:02 Yep.
Yep, like, I'm, I'm ha- I can, … I'll take a crack in my prototype and add this, … I had been, the past week has been hellish for me time-wise, because I had a bunch of other things I had to deal with.
as evidenced by my AC9. Apologies. Yeah, I think, I think I can implement this in the Java prototype, … Daniel, do you think you have time to implement any of these things, or… I guess it's.
**Daniel Dyla (Dynatrace)** 14:34 I do, yes.
**Josh Suereth** 14:35 Yeah?
**Daniel Dyla (Dynatrace)** 14:37 I have a block of time set aside this afternoon. Yeah, I apologize, I've had less work, or less time to work on it over the last couple of weeks, but I specifically set a block of time this afternoon to work on this stuff, so I do have time to do this. The JS prototype is… I think still behind the Java prototype, … Specifically, it's missing, like, the entity provider.
… But I don't think that that's a massive body of work. It shouldn't take a huge amount of time.
Mostly because you've already made all the decisions.
**Josh Suereth** 15:16 Yeah, I… the thing that I want to do next, I want to push the Java one. We need a Go prototype, and I'm willing to do that if no one else has time, but we also have to write the spec, so… or the OTEP, like, update the OTEP. So I was going to… I have that PR open against, Ted's OTEP repo to, like, update his OTEP on entity provider. I was gonna go through and finish flushing that out from the Java prototype.
So that your prototype can influence as well, and we can get that through?
**Daniel Dyla (Dynatrace)** 15:50 Yeah, I think your PR onto his branch is important, because it's way more clear about the distinction between the API and the SDK, in my opinion at least.
I….
**Josh Suereth** 16:02 Yeah.
**Daniel Dyla (Dynatrace)** 16:02 have time to update the GIS prototype this afternoon. I… Would, also work on… the OTEP if you want me to, unless you want to just do that, … but I'd wait until I finish my prototype first, so that I can get all my own thoughts in order.
**Josh Suereth** 16:20 Yeah, in terms of prioritization, I think Dimitri's spec PR looks ready to go, so I would say make sure we have an implementation of that to drive that spec work through.
Then the OTEP?
Although, the OTEP takes longer, so you can decide. This is my guess, is… I'd like to get Dimitri's in quick. I think the OTEP, getting the prototype done so you have feedback is the most important thing from the prototype.
Because we need to find out if there… we need to know our unknowns. So… exploring there is most important. Writing the OTEP would be last, in my opinion. That's why I'm trying to figure out if it's more important to write a Go prototype, or finish the OTEP spec work?
Right.
**Daniel Dyla (Dynatrace)** 17:09 Yeah, unfortunately, I don't have the expertise to, … to volunteer to do the Go prototype.
**Josh Suereth** 17:17 Oh, that's fine. I don't really know if I do either, and I'll find out when I make a prototype how ugly it is, but I….
**Daniel Dyla (Dynatrace)** 17:24 If I had… if I had a lot more time, I would volunteer for something I don't necessarily have the expertise for, but I don't. I don't… if… with a lack of time, I think expertise would be… Yeah. Preferred, ….
**Josh Suereth** 17:36 Well, in a lack of both, you just ask, let Code Assist, or Gemini, to do it for you. See how it goes.
Anyway, I have a bunch of stories about that, where… The quality of code is always consistently at a particular level.
And the things we're doing, when they're interesting.
It's bad, but if you're doing something that is not particularly interesting, it's really good. It's an accelerator.
I just… Given the amount of concurrency I had to do in the Java prototype, I would not recommend that right now.
**Dmitrii Anoshin** 18:20 Sometimes you need to spend more time, too.
Improve it and remove the code generated by the AI.
**Josh Suereth** 18:27 Your prompt will be longer than the code you write, is what I found with some of the threading stuff.
**Dmitrii Anoshin** 18:34 Right.
**Josh Suereth** 18:35 ….
**Dmitrii Anoshin** 18:35 Or you would need to spend more time to remove the necessary written code than you write it from scratch yourself.
**Josh Suereth** 18:42 Yeah. But actually, having it write a, a concurrent test was actually pretty helpful.
**Dmitrii Anoshin** 18:49 Yes, yeah, for sure.
**Josh Suereth** 18:50 It's a verbose test, but honestly, like, they're all kind of verbose anyway, so as long as it tests the right things, it was… that was good. Alright, cool. This is… this is all… thank you, Daniel. We have 10 minutes left.
I didn't put a link here, but we have a bunch of host and VM-related PRs in SunCloud.
**Dmitrii Anoshin** 19:12 I actually have another one pretty much related, so if….
**Josh Suereth** 19:16 Go for it.
**Dmitrii Anoshin** 19:17 If you click on the second bullet, link at the second bullet.
**Josh Suereth** 19:21 This one here?
**Dmitrii Anoshin** 19:22 Yes.
So, we have this PR, right? It doesn't open here, for some reason.
**Josh Suereth** 19:28 … why… where did this op- oh, here it is.
**Dmitrii Anoshin** 19:32 Okay, so… Yeah, I'm just trying to understand, like, if you go to a file, change… Like, it doesn't… like, the new definition for the entity doesn't have any distinction between descriptive and identifying attributes.
And I believe that this is the limitation of the….
**Josh Suereth** 19:53 No, it should, it could. We can actually… I can actually ask for that, yeah.
**Dmitrii Anoshin** 19:57 So, in this particular range that you just… just… they missed, identifying… instead of identifying the GPUs, right?
**Josh Suereth** 20:05 Yeah, you see, there's a, … we have it in the code gen to yell at you. So, warning! This entity contains, attributes without a role. Stable entities must have attributes with a role. So you have to pick, the way that works is here you add, under ref, you would say role identifying role descriptive.
**Dmitrii Anoshin** 20:24 Oh, I see. I was under impression that it would be two separate sections.
We're in.
**Josh Suereth** 20:31 It, it is when it, when they, when it's done correctly, identifying or descriptive. So, I'll, I'll show you.
**Dmitrii Anoshin** 20:37 Yeah, I know, I saw that. I, I, I just think it, it, it, it… The current approach would, actually make this, like.
**Daniel Dyla (Dynatrace)** 20:49 Error… make this user error more frequent.
**Dmitrii Anoshin** 20:54 Unless if we had, like.
**Josh Suereth** 20:57 behavior.
**Dmitrii Anoshin** 20:58 For identifying a descriptive attribute.
**Josh Suereth** 21:00 So, so two things here. Yes, the current approach is just how we got it to work now. This is what we have so that we will not make these things stable until this is there. We actually have a policy where if you try to mark it stable, it will fail the build.
**Dmitrii Anoshin** 21:15 Hmm.
**Josh Suereth** 21:16 So, you literally physically cannot stabilize without picking a role today. That's what we've done in SEMConf. If you're not familiar with some of the things we're doing in Weaver, we have a new syntax in Weaver.
Okay. That we are experimenting with. This is a… it's… you get a warning when you try to use this… oh, wrong thing. You get a warning when you try to use V2 syntax, but we're creating a V2 syntax, which is much… better. Lyudmila made this proposal, I love it, I'll show you an example.
… In the new syntax.
for entities, this is what it looks… instead of saying groups with type entity, and then name is the entity type, you would now just say, I have an entity of type my entity, here's the identity as a bunch of references to attributes, here's the description.
**Dmitrii Anoshin** 22:04 references to attributes, brief instability. Oh, I see, that's cool, that's cool.
**Josh Suereth** 22:07 We're trying to get this out as quickly as we can, but, this is… this is why I haven't… if you want to know why I'm not making progress on entities, it's because I'm working on Weaver, and if you want to know why I don't make progress on Weaver, it's because I'm working on entities. So I like….
**Dmitrii Anoshin** 22:26 Yeah, but this is cool, yeah, that's how I would envision the interface.
**Josh Suereth** 22:31 Yeah, yeah, yeah. The syntax for… the syntax for semantic conventions, you know, we started with something that made sense when it was first created, and then 5 years in, or I guess, maybe 4 years in or whatever, we're like, okay, we have beat to death the current syntax. Now that we know what this should really look like, let's make something better.
**Dmitrii Anoshin** 22:51 Okay. Sounds great.
**Josh Suereth** 22:54 Cool.
And if anyone wants to… oh, the other fun thing I'll say, right now, this syntax, if you wanted to see what it looks like when it's compiled, here's the entity. It compiles back to the old syntax, so that's why, if you say ref role is identifying, ref role is descriptive.
That's what you would do today.
And we have policies that afford you to do that.
**Dmitrii Anoshin** 23:17 And then, going on in future, we would probably remove this one, right?
**Josh Suereth** 23:22 Yes, yeah, so for now, we're gonna… yeah, we have… we have a three-stage approach. The… first, you can use the V2 syntax for inputs.
The second, which is what I'm working on next, and I'm taking a hiatus from that to work on entities, but the second would be you can use v2 syntax for outputs.
Right? So when I do code generation, all of that will use this V2 syntax, because we're currently doing crazy-ass JQ expressions to create things in the shape of V2 anyway, so we're just gonna generate that to begin with in Weaver. And then the middle, this resolution engine where we do dependencies and references and import from different files.
that all gets cleaned up in Phase 3. So, Phase 3 might be a year away.
But, Phase 1 and Phase 2 are the ones that we need to actually move off of it as a community. So, that's the goal.
Cool.
… right.
So… yeah, there's a lot of host cloud and VMSEM kind of PRs right now.
I think the one I'm most worried about is, cloud.
So, I can… let me see if I can find this, because it's related to that. We have….
**Daniel Dyla (Dynatrace)** 24:41 Worried as in high priority, or worried as in it may be trend… going the wrong direction?
**Josh Suereth** 24:47 Worried as in, the things we've discussed in this group are not generally well known to everybody, and we're having the same discussion 30,000 times.
There was one… there's one that I got pulled into because it's related to GCP, GCE.
… what is it? Maybe… Yeah, here. So we have a instance labels for GCE, right?
So someone wants to define instance labels, and … Let me see if I can find the comment. So, instance labels in GCE are… I basically said, hey, you have to put this in the entity if you're gonna add it, but instance labels are labels that you can attach to, like, VMs via our resource metadata server in GCB.
And someone wants to attach them to resource, which is awesome! We should be able to do that.
The comment is, I'd prefer to see this in the host namespace, so that we can reuse them.
So now the question is, is labeling a host A general thing we want to model?
Or are we gonna have, like, an AWS instance label tag thing, a GCP instance label tag thing, an Azure instance label tag thing separately, right? And then it goes back to, what is host.id, and what is GC instance ID? Because this same comment here.
was on whether or not host ID is the GC instance ID versus whether there's a GCP instance entity.
So… … When it comes to host and cloud.
I think we need to make a firm boundary of who owns what.
So that we could have, like, cloud cement convention owners.
**Dmitrii Anoshin** 26:44 Right, yeah, and based on our previous discussions, host ID, as a value, can contain anything, and typically, as we already have in semantic conventions, we would prefer cloud, because it's like it's pushed from the outside, right?
Yeah, but all the labeling and everything related to cloud should be separate entities.
**Josh Suereth** 27:10 Yeah, it's possible, though, that we have, like, a cloud resource tag thing going on. There's a whole… there's actually a proposal, the semantic tags proposal is that, by the way, of, … trying to get, like, Amazon, Microsoft, and Google to agree, when you tag things in our APIs, that, like, this is how it shows up in OpenTelemetry.
… So, there's a piece of this where I kind of would like to… not have GCP be a snowflake with labels, and figure out if there is a common convention, we share it.
But the whole cloud namespace, the last time we talked about it, if we look at it again.
It's… it's a little bit awkward, in the entity model, so… Where are we? Cloud… Right? If we look at the entities in here, there's a cloud entity.
Yeah. And it has a bunch… it's provider, account ID, region, resource ID, availability zone, and platform, right?
**Dmitrii Anoshin** 28:14 Yes.
**Josh Suereth** 28:14 Yes.
**Dmitrii Anoshin** 28:15 And we discussed that it's not the right… entity itself, so it's, like, we called it… we made it an entity because of the way we were, like, kind of requirements, but it's not really an entity, it's a set of descriptive attributes, right?
**Josh Suereth** 28:32 Yes, yeah, yeah.
And this is where I think… One of two things is true.
One is, we might need the ability to define descriptive attributes that can get added to any entity.
And the other is, we might need to get a group together to define cloud entities and actually stabilize something.
You know, and what's the boundary between what's in here and what's in hosts? Yeah. Right.
**Dmitrii Anoshin** 29:03 And cloud entity would be, like, different, not just cloud. It would be cloud region, for example, cloud….
**Josh Suereth** 29:10 Cloud region might be an entity, cloud resource might be an entity, like, this right here, when you see, like.id.
That makes me think maybe Cloud Account is an entity?
**Dmitrii Anoshin** 29:22 Right, Cloud Account sounds like an entity, sure.
**Josh Suereth** 29:25 Yeah.
So, yeah, I think we need to go through and model this. That's all I'm calling out. So, I guess the question would be, when you look at semantic conventions, there were, like, 4 or 5 PRs around host and cloud and this kind of stuff.
Should we be pushing for a group to do that? Or should we take… my thinking is the semantic tag group, the stuff that they're looking at, that proposal? What do they call it? They call it Resource Metadata, is the name of the SIG.
**Dmitrii Anoshin** 29:58 Yeah.
**Josh Suereth** 29:59 Of actually calling them, like.
I think they're trying to drive service of, like, what should be descriptive attributes in service, and maybe get them to handle cloud.
and kind of push for them to own that. What do we think?
**Dmitrii Anoshin** 30:16 on earth.
Yeah, I believe… which particular, like, decisions they made for system, they likely can be applied to the cloud, but at the same time, it's a different field, completely, like, different expertise, but….
**Josh Suereth** 30:36 Yeah.
**Dmitrii Anoshin** 30:36 Not much.
**Daniel Dyla (Dynatrace)** 30:37 who sponsors that.
**Josh Suereth** 30:39 I'm one of the current sponsors. I think if you look at the… Right now, they're going after Environment Application Owner, and I know… I know the internal GCP team, so I've been working with them.
On what they want to do. … Like, basically, they want to stabilize this. I don't know if you know, tons of people rely on it, it's not considered stable.
deployment environment. So that's like, hey, could we… could we figure out what this needs to be as an entity and stabilize it? … This did not render.
**Dmitrii Anoshin** 31:13 Did we… Did we rename it back from deployment.environment.name?
**Josh Suereth** 31:20 … I… I forget where it's… it might be… it might be in the middle, yeah.
This might be using an old, the website, I think.
Where we renamed it to deployment.environment didn't get published on the website, so I think this is what was on OpenTelemetry.io.
That's another fun problem with SunConf. Yeah, so service name, we already have this one, it exists, but they wanted to add service owner to service name, service cost center, service business unit, and data sensitivity would be another one. This is like a, The overlap of open telemetry and security a little bit, like, knowing if a thing deals with sensitive data.
**Daniel Dyla (Dynatrace)** 32:04 I have to go.
**Josh Suereth** 32:05 Okay, alright, we'll see ya.
**Dmitrii Anoshin** 32:07 This is a good example of a descriptive attribute that's shared between different entities, data criticality, data sensitivity.
**Josh Suereth** 32:15 Exactly, exactly. So do we need a way to represent that and describe it?
**Dmitrii Anoshin** 32:19 I think we should, yes.
**Josh Suereth** 32:21 Yes.
**Dmitrii Anoshin** 32:22 Something like that.
**Josh Suereth** 32:24 Okay. That's kind of what I wanted to walk through a little bit. So it sounds like we need to do some more thinking here. In terms of sponsors, by the way, it's, it's Trask and I.
So… Okay.
Cool, let's go back to… the notes quick. We're out of time, I gotta jump to the profiling seg, … We should look into a mechanism.
define descriptive attributes… Could be on any entity. Okay.
… Project status update. Basically every week what I want to do is look at our project board.
**Dmitrii Anoshin** 33:06 Okay.
**Josh Suereth** 33:07 This is now getting used to track status of projects and things. For context, the on-track status is just the deliverable of Phase 1.
So phase one is Entity Manager OTEP and Resource Entity Mapping, and all the in-progress work we have. Do we still feel like we're on track for, I believe this is end of the year, delivering that body of work? I think… I think we are.
**Dmitrii Anoshin** 33:30 I think we are.
**Josh Suereth** 33:31 Okay.
Cool. Alright, that's it. Thanks, Ben. I will see you.
