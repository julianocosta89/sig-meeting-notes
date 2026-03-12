SIG: Semantic Convention SIG
Date: 2025-11-03
Duration: 57 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:40 Hello, hi everyone.
**Christophe Kamphaus** 00:43 Hi, everyone.
**Trask Stalnaker** 00:44 Ayy.
**Liudmila Molkova** 01:12 Who wants to drive the call today?
Okay, nobody does, so it means I probably should…
**Trask Stalnaker** 01:25 Nobody does. No.
**Josh Suereth** 01:28 Yeah, who did it last, I guess, is the question.
**Trask Stalnaker** 01:30 I know, I think it… I feel like it's my turn, probably.
**Liudmila Molkova** 01:36 I mean, I'm already sharing, and I mean, I can keep going, then next turn will be yours, Trask.
**Josh Suereth** 01:43 Yeah.
I'd be okay to lead if you… if you don't want to, Lyudmila, it's fine.
**Liudmila Molkova** 01:49 I'm fine, it's… yeah.
**Trask Stalnaker** 01:53 Next week, canceled.
for Koop Gunn.
**Liudmila Molkova** 01:58 Right, let's do it right now.
Oh, does anybody coming to KubeCon?
**Trask Stalnaker** 02:12 B.
**Josh Suereth** 02:13 I'll be there We should, we should get together and, and do something.
Yeah.
**Liudmila Molkova** 02:22 Right, yeah.
Okay, so while people are joining, and maybe this is one of these weird weeks with different time zones, I'm not sure.
But…
**Armin (Dynatrace)** 02:37 Not anymore.
**Alexandra Konrad @Elastic Security** 02:39 Until the last one.
**Liudmila Molkova** 02:42 I see. Okay.
**Armin (Dynatrace)** 02:44 Was too good to be true.
**Liudmila Molkova** 02:51 Okay, let's take a look at our trash board.
Okay, there are plenty of… Things that are blocked.
Do we want the raft to be blocked? Should we move it to entriaged or something?
But I think… rough for now, until CIACG Phase 2 launches.
So the… I'd like to move it to entriaged, because this is where the drafts are, or remove it from the project until it materializes, so we don't spend time on it.
**Trask Stalnaker** 03:41 Makes sense. Does it get added automatically when it gets undrafted?
**Liudmila Molkova** 03:47 No, unfortunately, no.
**Trask Stalnaker** 03:49 Okay.
**Liudmila Molkova** 03:50 I mean, I can put it in triage.
**Trask Stalnaker** 03:55 No status, perfect.
**Liudmila Molkova** 03:57 Oh, this is… This is the PR bar, right.
Waste till… So let's take a look at the couple.
New convention for a raid.
I'm sorry.
Jaw blocked it.
It seems there is some discussion.
**Trask Stalnaker** 04:40 This looks like just in the… Sig?
Oh, it has a SIG approval.
**Liudmila Molkova** 04:52 Alright, and this is part of the system SIG.
Okay, so then it seems Ja's comments need to be addressed.
Add more app details.
Okay, so it seems Sig's rejected, and there is a long discussion.
If I remember correctly, this is actually an important discussion that has a lot of prior art.
that app.
prefix. Currently, it's… Specific for the mobile things, mobile apps or browser apps.
client apps.
But people misuse it, and there are tons of, let's say, ab.attributes in AutelDemo that are app-specific.
So I think we either need to change the status quo, which is… clients say I guess strongly against.
Or we need to document it maybe better, that… that, ops are… Only for the client. Yeah, Josh?
**Josh Suereth** 06:16 So, I think the problem we have is Kubernetes has a convention for naming apps in Kubernetes.
So, it's like, us saying that, oh yeah, these are no longer apps, only mobile has apps, is a very open telemetry thing.
And application's very generic, as a name.
So, I do think we need to be careful here, and, like, be very considerate, but I think… we're gonna continue to get pressure, specifically because Kubernetes already tells people to call it an app, and an app name, and dependencies, that, like.
we'll have to figure that out. If you look up, Kubernetes naming conventions, I can find you a link and put it… we talked about this in the service sig.
There's conventions today for application.
So, for application to imply services. There's also what mobile needs, and we need to find a way to unify those two things in a way that doesn't cause just massive conflict anytime someone walks in the community.
So I… I think we should not change app as it is today until we make that larger decision of the direction we want to go. And I agree, like, it would make sense to have the client app side folks discuss with us, but if it gets to a point of contention, like, major contention, we… Probably want to escalate.
So…
**Liudmila Molkova** 07:47 Yeah, I think I don't have the prior art, and Jason is referring to it quite a lot, so I think we've, like, it would be awesome if somebody prepared And learned about the prior art, and I'm happy to do this. Okay, you are… you've added the topic.
I'll try my best to do the research, and maybe in the upcoming weeks or months, we can have a better discussion on this.
**Josh Suereth** 08:19 B.
Yeah, I, I mean… We called things service to start with, because that was the art in Trace, so we also have to deal with that.
Like, Kubernetes calls something an app that we would call a service.
we call things a service because Jaeger called it a service, Datadog called it a service, I don't think Prometheus… Prometheus calls it something else.
What's theirs? Job.
is that our version of service is a Prometheus job, right?
So it's like… And this is one of those things where I think it's a world of gray.
So, it's fine for us to make a decision, but I think we need to make an opinionated decision, probably across the hotel community. Just say, here's the path forward for stupid names, let's go. Sorry, you can tell where I stand on some of these, like… naming issues. Like, let's just pick one and stick with it. But… let's recognize the friction that we will have with people onboarding. So, if our target audience right now is a lot of Kubernetes folks from CNCF, Stealing app to be just mobile is really at odds with our core audience there.
So we need to… I think it is worth resolving that.
**Trask Stalnaker** 09:46 Do we want to invite the… Mobile client folks to this meeting.
Maybe 2 weeks from… Today.
I can do that.
**Liudmila Molkova** 10:17 Okay.
We are out of our triage box.
So maybe we can do the thing we've done last, we'll go through the agenda, which seems light this time.
And we will use the rest of the time to review triage, PRs that we have.
Okay, Taras, you wanna talk about Schema URL?
**Trask Stalnaker** 10:47 Yeah, yeah.
**Liudmila Molkova** 10:47 Sorry, I didn't notice.
**Trask Stalnaker** 10:51 Oh, no worries, so, finally getting around to adding schema URL to Java instrumentation.
And have… just have a… Maybe simple, maybe not. Never know a question about what schema URL we should pick.
My… Thought is that we should pick the most recent schema URL that the instrumentation telemetry is compliant with.
Which… Basically, in practice, Bumping it pretty much each… Time schema, a new semantic convention is released.
the alternative is to… Pick, sort of, the first one, the oldest one that we conform to.
which would mean, say, in practice, like, the stable version, the first version of HTTP that was really stable, and then in one or two instrumentations, we've picked up, http.
template.
No, url.template.
On the client instrumentation, So we would bump, you know, to the version where that was added.
**Liudmila Molkova** 12:20 direct two different beasts, the HTTP, right, and the stable ones, and not stable ones.
And for not stable ones, I think only the latter approach makes sense. You intentionally update the version, because you, like… You never know if… It's compliant with the version that you… Auto increment it, right?
**Trask Stalnaker** 12:47 Yeah, I mean, I don't mean auto… truly auto increment, but, you know, with a manual review. But in practice, since we aren't breaking Stable SEM cons.
I think, effectively, it would be.
auto bumping, until there was a braking change in SEMCON.
**Liudmila Molkova** 13:15 So your question about it is about HTTP.
**Trask Stalnaker** 13:19 Yeah. I'll jail.
Well, let's… let's focus just on HTTP, yeah.
**Josh Suereth** 13:24 So, I think before HTTP stabilized, where we said hold on the previous version, you just wouldn't update the schema your own and stay on that old one until you support both.
And then you would actually have both, depending on the flag. And then after that, if you… keep up… like, keep updating, I think you should be totally fine. Like, that's… we're kind of designing it to work that way in some sense. If we actually used semantic versioning in semantic conventions, we'd be on, like, 1.0.x.
For HTTP, right? And that's kind of the intention. So, you would… you would only lock to, like, the 1.0 series of the… conventions, if you know what I mean. So, if we… if we ever do another change that would be breaking, or… sorry, the 1.x version of changes.
If we ever did a 2.0, you'd have to, you know, change it.
I don't think we need patch fix, or sorry, yeah, bug fix type things in SEMCOV, but, I could be… We can evaluate as we go.
**Trask Stalnaker** 14:31 Cool, so that… I think that answers my question, if, Ludmila, that… Sounds good.
For HTTP, for stable ones, we essentially auto-increment once we're stable to the latest.
for… unstable sound comp, we have to be more careful, essentially.
**Josh Suereth** 14:53 And any time, that isn't a good idea. Like, if you… if it actually breaks users and they complain and open a bug.
report that back here, because it means that we need to update our policy on what breaking changes are. Because it's, like, like, theoretically, this should all be safe, it's just we might have missed something. So if it does end up to be a problem in practice, consider that a bug in our release process, not in Java, right?
**Trask Stalnaker** 15:18 Sure.
**Liudmila Molkova** 15:21 I have a dream that we will actually test the compliance with semantic conventions.
Nci, and then we would know.
Okay.
So moving on to the next topic, we don't have system semantic conventions people here, so I probably should cut it short.
So, there is a rename.
That changes… System Linux memory to System Memory Linux.
And I wanted to discuss it with them, because I don't understand what's the benefit of this.
But… So the discussion we had is that, essentially, they would like to put the important part of the groupings first, like, it's the system and then memory.
And then it kind of breaks the… connection between the underlying properties. But the point here is that the fact that it's Linux is… Less important that it's a memory.
And it's a system memory.
yeah.
But since we don't have system people here. I don't know.
**Trask Stalnaker** 16:55 I saw it, I… I think I'm okay with… I, like, I mean, I agree it would be… would be good to update their doc, where they say that they're going against the general SEMCOM rule here.
But given that they're already sort of doing this for… one level, I don't… See a problem with if they want to do it for another level.
And I… I feel like in this case, kind of, we can justify it a little bit in that it's… really primarily just Windows and Linux as kind of just these two, like, it's not… such a open… I don't know, it's… What am I thinking?
Maybe it's just, like, from… there's so much prior art that we're sort of… Trying to conform to…
**Josh Suereth** 18:07 I think this, this one might be, there's two things to think about here. One is a joke, which is Trask, maybe you can just convince Microsoft to be Linux now, so Windows is just Linux, and then we're fine.
Number 2, though, is, if we think about some systems actually automatically group metrics by the dots, or by, like, punctuation, like slashes, dots, that sort of thing. And so, I was just in, like, a Prometheus brainstorming session where they were talking about, like, grouping by… underscores, where you can say, like, here's, like, a group of metrics, and you'd use the namespace of it, and for OTEL, it would be, like, the dots.
So, having system memory metrics all in a thing, where, like, there's a Linux bundle underneath them, is better ergonomically than having, like, you know, Linux and then system memory metrics, or… so basically all your memory metrics are kind of in the same prefix bundle.
That… that I can understand if that's their justification here.
I don't actually know their justification, though, so I didn't look through the PR. I'm just, calling out that was something that I… caught my attention as, like, oh, maybe we should think about that a little bit, of, like, how should these things be bundled together? That's one of the ideas behind the namespaces, and if a system automatically does grouping and expansion of groups of metrics when you do discovery of metrics or autocomplete, This… this actually makes an ergonomic difference to someone consuming system memory metrics.
**Liudmila Molkova** 19:43 Yeah, I think the autocomplete is the main justification, and I can understand it. The worry I have, that it essentially means that OS appears in random places.
So you do system memory, and it appears there, you do system something else, and it's something else appears there. But, again, there are no awesome decisions here. All of them are… difficult.
Anyway, so…
**Trask Stalnaker** 20:11 It's also different than, what we have, what we've said so far for, like, database And other… Conventions, where we are putting the… But… MySQL at the top level.
And I think for… for attributes, I don't think there's any downside to that, like, from a grouping, because the attributes are always going to be on something.
I can see the argument more for metric Where you have a whole lot, and so some, like, kind of logical grouping helps.
**Liudmila Molkova** 21:00 Yes, assuming there is something in common.
**Trask Stalnaker** 21:03 about.
**Liudmila Molkova** 21:07 So, like… If we think about system metrics, then the memory usage is somewhat similar across different… operational system, but do we want to have something in common for clustering and Elasticsearch and, I don't know, MongoDB? Is there something in common?
That we would put before the database name.
Okay, so it sounds like here… The first task would be to actually write down the principle, because the current guidance does not have this principle articulated. It only talks about root namespaces.
And then there is no, like… No desire to block it.
Yeah.
**Trask Stalnaker** 22:06 Other than using that as… Motivation to get them to write it down.
**Liudmila Molkova** 22:14 Hi, yeah.
Okay.
And this concludes our agenda. We already canceled the call next week for the KubeCon.
Okay, so if anybody wants to stay for the triage session, Please do.
Okay, Josh, I really liked what you did last week, but I don't remember what. Can you remind me what was the thing we've done? We just walked through the PRs?
**Josh Suereth** 23:15 Oh, man, yeah. I forget. I think we walked through PRs in the hopes of basically trying to get as many of them through to the merge process as possible.
we don't have any means more approvals now, which I think is awesome, so we can start on just checking over blocked. If there's anything we think… you already went through a few of those, making sure that all of them… unfortunately, because there's not a status to say, I think this is unblocked.
That people flip to when they make a change. I think we… We might want to add to the triage process, or, like, the PR process of, like, if somebody blocks a PR, great, you mark it as blocked, but when someone responds to the blockage, we need some way to say, hey, go look at this. But in lieu of that, let's just look at all of them and see if there's an update post-block.
**Liudmila Molkova** 24:02 Yeah. Oh, actually, we have Alexandra here. Alexandra, what should we do with this one?
**Alexandra Konrad @Elastic Security** 24:12 The collisions for that…
**Liudmila Molkova** 24:14 and entities.
**Alexandra Konrad @Elastic Security** 24:16 I think one of them, shouldn't be there. I think collision for… Mmm… metric names… we have already, doubling data. I remember from hardware, and I don't think we have changed it, so we have the metrics Which, collision between a namespace and the metric itself. And for, entities, I'm not sure as well.
**Josh Suereth** 24:51 So, entities that collision is by design. We actually might…
**Alexandra Konrad @Elastic Security** 24:55 Truly off.
**Josh Suereth** 24:55 with the policy, so we might actually require entities to namespace their attributes, so the type of the entity would be the namespace for the attributes. That is, that might be something that we end up going towards, at least if you look at where the entity seg has discussed this.
**Liudmila Molkova** 25:12 It reminds me of something.
**Alexandra Konrad @Elastic Security** 25:16 And for the metrics?
**Josh Suereth** 25:18 For metric, you call out a real issue here that we have to figure out what we want to do.
**Alexandra Konrad @Elastic Security** 25:24 Yeah.
**Josh Suereth** 25:24 like, it's not just the hardware ones, it's this hotel SDK Exporter one.
**Alexandra Konrad @Elastic Security** 25:30 Yeah, I think this might be outdated, because I have created it, like, what, a few months ago, so… We need to check… I need to run it on the latest, SEMConf.
But, I mean, it doesn't change the fact that there are collisions.
**Liudmila Molkova** 25:47 I think one of them is deprecated, and it's okay to have a collision with a deprecated thing.
**Alexandra Konrad @Elastic Security** 25:55 Yeah, I think I have updated it to not include deprecated afterwards.
**Liudmila Molkova** 26:04 Yeah, so this friend is deprecated.
And in this case…
**Alexandra Konrad @Elastic Security** 26:13 If you…
**Liudmila Molkova** 26:13 rerun it, then maybe… Most of it for the go away.
**Alexandra Konrad @Elastic Security** 26:22 I can rerun it, it just, again, it will not solve the hardware issue, because, like, I remember we haven't updated anything in the hardware after my, pull request merged.
**Liudmila Molkova** 26:38 So what we've done in the past is that when we introduce a policy, and it breaks something, we put a temporary exclusion in the policy, we say, okay, don't validate those specific ones.
We'll create an issue to follow up on them eventually, so usually it means, like, if this goal is stable, then somebody will go through and decide what to do.
And then it kind of protects future contributions from adding Conflicts, but it keeps status quo on the old ones.
**Alexandra Konrad @Elastic Security** 27:12 I can do this, how exactly you do this in REGO? Like, you add the rule, if it's a hardware, you don't check it, or… What do you mean by excluding it?
**Liudmila Molkova** 27:22 Errh…
**Josh Suereth** 27:32 You're pulling up your example, Ludmila, I was trying to find it, but it looks like you're already there.
That's the exceptions right there, right?
**Liudmila Molkova** 27:41 Right, here.
**Alexandra Konrad @Elastic Security** 27:43 Yeah, exceptions, okay.
This is the…
**Josh Suereth** 27:49 You need the not right under that, too, so basically you define the exceptions that you want as, like, an array, or in this case, I think it's a set. I forget, I think… I think brackets and rego are sets. Anyway, and then the not just says, you only deny if it's not in this list of exceptions. So it's… it's pretty simple to do.
**Alexandra Konrad @Elastic Security** 28:10 All of our…
**Josh Suereth** 28:12 all of our RegO policies have exceptions like that. They're either empty sets, or there's, like, a set of things that you can… we can opt into if we have, like, legacy stuff we have to deal with. And the goal is to reduce that over time to zero.
**Alexandra Konrad @Elastic Security** 28:28 Got it. Yeah, I can update it.
So, if we, like, we need to create two issues out of it, yeah? So we need to update the wording for the integers.
And allow, the collisions on entity names.
And updated for the metrics, too.
And, allow the hardware matrix to be collide… collide… yeah, colliding.
**Liudmila Molkova** 29:24 Wonderful, thank you.
Okay, moving on. Azure Computing Attributes.
I think this is one of the PRs where we don't have, owners, group of owners, and… Oi… Would have declined it at the triage point.
**Trask Stalnaker** 30:04 Is this adding new… I see, this is just adding new things that were… Yeah, I think we should… Close it with no… SIG.
**Josh Suereth** 30:24 Is there an issue for a SIG to pick up on this one?
To say, like, for, like, why these deem to be… added? Like, is this tied to an issue as well, or is it just… Add in a bunch of stuff.
**Liudmila Molkova** 30:40 Let's see…
**Josh Suereth** 30:42 There is an issue linked there.
Okay, cool. So that one we could say that it doesn't have a SIG, and it needs to be in a SIG, and then we can, close the PR. I think that's the right thing to do.
**Liudmila Molkova** 31:01 Oh.
Well… It needs Sikh. Should it be accepted or not? I think this is a fair issue. There are resource detectors that are setting attributes and they're not documented.
So we should define it at semantic conventions, but we need somebody who cares.
**Josh Suereth** 31:23 Yep, and then we can actually… I used this, by the way, when we did the service sig, was I went through all of our issues, and I grabbed all the need SIG ones. They weren't all appropriately annotated, so I had to go then do a broader search where it's, like, a thousand things, because everything says service, and they don't mean… that it's for the service SIG, but still, like, the idea that we can just go in, grab all these neat SIGs, search for Azure Resource, bam. There's, like, your list of queue for a SIG? I think, I think this works pretty well.
**Trask Stalnaker** 31:53 I don't think that accepted here means that it's accepted by the SIG. Like, I mean, the SIG still gets to decide if it's… going… if it's accepted or not. It just means we've accepted it.
**Liudmila Molkova** 32:08 Right.
**Josh Suereth** 32:09 I think it means we don't close it.
**Trask Stalnaker** 32:11 Yeah, yeah, yeah, and it's a low bar for acceptance. It's like, okay, yes.
put it in the buck… the SIG bucket.
Josh, for the Kubernetes app namespace, is this… I just put in chat a link, is this… Essentially, what you're talking about.
I wanna get the… get a… the overview correct when I invite them.
**Josh Suereth** 33:47 Yep.
Cool. That's… yeah, I don't know how… I, I know, I know that some people rely on that, and I think some people make their own version of it, but, I don't know how adopted it is overall, I just know that people who do depend on it are adamant about it, right? So, I don't… what's the thing about the loudest squeaky wheel, right? It is true that it's something that, like, is a convention Kubernetes, though.
**Trask Stalnaker** 34:17 Yeah.
**Liudmila Molkova** 34:24 Okay, moving on to the next one, Good question, how should we mark this? This is the SIG… scope a discussion about having session ID when we're using existing session ID.
But essentially, this is within the SIG, and the SIG tries to define what to do with it.
How much do we care about in the general semantic conventions about this kind of issues?
Should we stay awaiting code owner approval?
And not look at it here.
**Josh Suereth** 35:07 I'm fine having that be a waiting code owner's approval. We can also say, blocked on code owner's approval if we need, like, a new thing for it.
**Liudmila Molkova** 35:19 Yeah, interesting point.
It seems like it's great to have more statuses, but this thing is pretty wide already, so we just would never look at it.
**Josh Suereth** 35:33 Well, yeah, I think, ideally, blocks should be… If we take the approach that awaiting co-owner's approval, there's some other SIG that has their own board that's tracking things, that they would be… that means it's on their board, they're dealing with it.
Blocked would be, we block it.
Or, sorry, maintainers are blocking it.
**Liudmila Molkova** 35:52 Maintainers are blocking it.
**Josh Suereth** 35:54 or general approvers. Not that… I don't know if we have general approvers anymore, but you know what I mean. So that blocked would be, like, we are blocking it as the maintainers of Semcov.
Otherwise, we can put it into a waiting code owner's approval and let the SIG deal with it. I think that seems reasonable.
**Liudmila Molkova** 36:09 Okay, and then it's a manual process, because today, when you reject the PR, for whatever reason, whoever blocks it, it ends up in this blocked.
And then it's the question of manual process to move it in the right place, or is the manual process all the way through?
**Josh Suereth** 36:27 I mean… that a little bit of this is gonna be manual. We can talk to Yao about the automation. The problem, I think, is… my theory for how we would implement this with automation is if a SEMCOM maintainer blocks it, it would go in the block thing. However, you are in the SIG, and you are the one who blocked it, so it would go in the block thing no matter what, even if we automated this.
**Liudmila Molkova** 36:46 Hi, thank you.
**Josh Suereth** 36:48 So…
**Liudmila Molkova** 36:48 stone.
**Josh Suereth** 36:49 Yeah.
**Liudmila Molkova** 36:50 Just for the history, let me write it down, regarding the process, Maybe it'll make me remember it better.
Okay, so there is just one more here in the blocked ones, and we are productive.
Openstack Nova as cloud entities.
**Josh Suereth** 37:48 But this is… this is where we want the… I think the ID just needs to use a dot instead, although…
**Liudmila Molkova** 38:13 So, yeah, so this one would become uponstack.nova, this would become… this would… Depends.
**Trask Stalnaker** 38:27 What is OpenStack Nova… what is NOVA?
Is it an implementation of OpenStack?
In which case, should it be Nova?
OpenStack.
**Liudmila Molkova** 38:43 Component of OpenStack Cloud.
Provisions and manages large. Sounds like that.
**Trask Stalnaker** 38:53 Yeah. Okay. Yeah, it's also known as OpenStack Compute.
**Josh Suereth** 38:57 Which, which one are they sticking with?
Yeah, so it sounds like OpenStack Nova is the, the compute engine. But, see, did they rebrand?
**Trask Stalnaker** 39:11 Yeah.
**Liudmila Molkova** 39:13 This is why we shouldn't own these conventions in general in the bright future, because we don't care, and they don't know, what we end up with. They should own them.
**Trask Stalnaker** 39:29 Is this one of those never-ending enum questions?
**Josh Suereth** 39:35 Yeah, I think, I think people, One thing I've noticed, the value of having a stable name is so important. And rebranding, sometimes there's a reason you do it, but sometimes it just never works.
Anyway, there's a thing called Stackdriver that people still call the Google tool that. It hasn't been named Stackdriver for over 5 years. But yet, that's still how people always refer to it, because the cost of changing a name is so expensive.
Anyway… That's a random aside. Do… should we suggest whether or not this should be called OpenStack Compute, or do we just not care?
**Trask Stalnaker** 40:16 Or do we want to not accept this and just say, hey, you're… it's an open enum, you're welcome to use… Whatever.
**Josh Suereth** 40:27 The only reason we've been allowing these, by the way, we can actually ask this in the thing, is there an OpenStack detector in OpenTelemetry?
**Liudmila Molkova** 40:36 Yes, that's exactly what powers up this issue, this is… yeah.
**Trask Stalnaker** 40:41 Hmm. Okay.
**Josh Suereth** 40:43 So… until we have a solution for that, I think we should allow this, and Well, we as general maintainers have to deal with cloud conventions until we have created a SIG for it.
**Liudmila Molkova** 40:59 Well, the… one of the solutions we can have is that it… we do this, let's say, for JMX metrics, right? We don't document them in SEMconf, we document them where they are instrumented.
if there is a chance that, let's say, this resource detection would exist in more than one place in OpenTelemetry, this becomes fun. This becomes the place where we need to have a centralized documentation for it.
**Josh Suereth** 41:25 Resource detection generally has to be in multiple languages. Just… For OpenTelemetry. I mean, if it's something that can't be in multiple languages, I would… I'd be surprised if it's not needed at some point, depending on what they have, but, particularly things like, if you support serverless, or like a Cloud Run, or a Lambda, you have to have language-specific resource detection at that point.
I don't… OpenStack Nova, maybe not. Maybe it's, only OpenStack needs it?
But I don't know enough about OpenStack to answer that. I just know that generally resource detection and multiple implementations go hand in hand.
**Trask Stalnaker** 42:10 I, I… I mean… Ideally, yes, but in practice, there's so much… Instrumentation in Collector Contrib.
And… that doesn't exist, I mean, that nobody's building out in all the languages, or any other languages?
That precedent sort of sets us up for getting a huge flood of things from collector contrib.
Where I kind of like the… pushing back if it's not a SIG that we have, if it's not, you know.
A priority that we just, say, documented in the instrumentation.
**Josh Suereth** 42:57 I'm fine for now, too, if we just say, cool, Collector is the only place that has it, let's push it to Collector SIG. If it goes past Collector, then we can have a process where it would have to… Come somewhere shared.
That's another option. Because it also could be true that resource detectors and resources around clouds, we don't put in SEMCOM itself, we have some… we have a contribib thing where we can deploy, like, here's…
**Trask Stalnaker** 43:21 crib.
**Josh Suereth** 43:22 What? All the contributors. Everyone knows.
**Trask Stalnaker** 43:25 Semcons can trip.
**Josh Suereth** 43:26 No, that's what I'm saying, yeah, but we could have, like, a section where it's like, cool, here's all the cloud provider things, and it gets released, you know? Or here's just the OpenStack ones, like, yeah. We need to get that sorted out, and I think decomposing a little bit could help over time.
So, I'm a fan of what you both just suggested, of like, let's keep it in collector, move that way forward.
**Trask Stalnaker** 43:51 I like… I like the rule of two.
**Liudmila Molkova** 43:57 Yeah.
**Trask Stalnaker** 43:58 Because that would address, like, we've gotten, for example, the database Enum, people have been wanting to add a lot of things to the database enum.
That are only… have only been instrumented in one Language or one place.
**Liudmila Molkova** 45:10 Would we block it on the stability? So should there be documented somewhere central if it becomes stable?
Because if it becomes stable and it emits something, Then… Well, it can still major version bump, necessary.
Yeah.
I think we need to document it somewhere. I don't know where.
**Trask Stalnaker** 46:13 Yeah.
**Liudmila Molkova** 46:14 Let me take connection, and let me create an issue.
**Josh Suereth** 46:18 This might be one of those OTEPs related to the blog post that Austin put together that we need to sort out, too. Like, I feel like, where does this need to be documented? We need license to do this in the spec, because right now, the spec is way too… pedantic, and we want to open that up a little bit, right?
Well, preserving it. And then there probably needs to be guidance in SEMCOM to say, if you're doing X, don't, don't do it here. Do it over there first.
**Liudmila Molkova** 46:48 Yeah.
Okay, we have… Should I accept this issue right away?
**Trask Stalnaker** 47:01 Yep.
**Liudmila Molkova** 47:02 Awesome.
**Trask Stalnaker** 47:06 Yeah, and I don't think we have to wait for, you know, I wouldn't… we don't need to wait for the blog.
OTAP stuff, we can… Put this out as our recommendation, and that can feed into that the blog, OTEP.
process.
**Liudmila Molkova** 47:26 Yeah, essentially it means we are kindly asking to close this PR.
**Trask Stalnaker** 48:16 Okay, we are super productive, today.
**Liudmila Molkova** 48:19 We still have 10 minutes, we can quickly look into the new issues and try to triage them.
Since I have your attention, I'm just going to… do this.
Okay, so what are we… needs to reass?
So this is the only column we would look into.
And it contains a mix of the old issues and new issues.
So the flow, I could imagine, we'll just take a look at the few.
And then… Triage them.
metric category.
**Trask Stalnaker** 49:36 Sounds like schema?
**Josh Suereth** 49:41 Yeah, maybe this needs to move to Weaver.
Like, I… Yeah.
**Liudmila Molkova** 49:54 What are cutting works?
**Trask Stalnaker** 49:55 Something that would be… Described by the schema, as opposed to… the actual telemetry signal, like, I mean, to add that to the telemetry signal would be… would require spec work, I assume.
**Josh Suereth** 50:18 Yeah, this is just in SEMCOP, so I think this is a Weaver thing now, of, like, what would the… So, this is, this is around, collector mDataGen versus, using Weaver to define things in the collector. I think, They were looking at, like, all the different problems or inconsistencies between the two and trying to shore them up.
Categories is a… a thing that mdataGen had, and I don't know how it's used, so we'd actually have to look at, like, what are you doing with this? Why do you need this? Where is it documented? Where does it show up?
if it doesn't need to show up inside of the metric itself, which I actually don't think it does.
then… there's a question of, like, we could just say, make this a Weaver annotation, for now, if it's a collector-specific thing. And I think that's reasonable.
If it needs to be first class in the model, because it's used in some way, we'd have to understand that. But in either case, I don't think this is a SEMCOM issue, I think this is a Weaver issue.
**Liudmila Molkova** 51:24 I agree. Do you want me to transfer it, or we can just add it to the Weaver project here?
**Josh Suereth** 51:31 I think I would actually transfer… take it off some kind of issue triage in one way or another, but you can just move it to Weaver Project, and then, I would transfer it in the repository as well.
**Liudmila Molkova** 52:11 I'm sorry, I cannot type today, or any other date, Okay, Add the user ID for client, web, mobile, platform, semantic conventions.
Yeah, the end user ID would be the… Unsure.
**Trask Stalnaker** 53:10 Yeah.
Needs more info?
**Josh Suereth** 53:16 Yeah.
**Liudmila Molkova** 54:03 attribute identities and metric streams. Oh, it's something very… no, not old, but it's assigned to… Carlos, how come?
**Trask Stalnaker** 54:14 From the old spec.
Auto-assignment.
**Josh Suereth** 54:19 Oh, wow.
Yeah, this goes into sentinel values. Remember, I think we had this discussion at some point about, like.
It's possible in the Proto to have a label with an empty value, and then you can't tell what the original type was.
So this one is actually, I think, not a semantic invention problem, personally. I actually think this is a spec issue?
**Liudmila Molkova** 55:27 Okay, so, yeah, so this is… it applies to any metric.
And it's the question of how, How to find the time series that you need to… Aggregate ton.
**Josh Suereth** 55:44 Yeah, it's a weird corner case, and it's important for our Prometheus compatibility layer. So basically, this is also where we talk about how you can flatten all attributes to be strings.
And then what… You know, if we're trying to treat true the same as true and false the same as false, but it's frickin' empty.
And how do we make the empty be a false?
**Trask Stalnaker** 56:09 Ludmila, you're in… this is already in the spec repo.
It's just on our board for some reason.
**Liudmila Molkova** 56:14 Oh, wonderful, so let's just remove it.
**Josh Suereth** 56:19 Yeah.
**Trask Stalnaker** 56:20 I was scanning, I'm like, where did it get transferred?
**Josh Suereth** 56:24 And where did it get added to our board? Did one of us do that? Did I do that back in the day?
**Liudmila Molkova** 56:30 Yeah, I did.
**Josh Suereth** 56:32 Oh, no, no, it was in… when we were talking about instrumentation Stability Working Group. That was in 2022, before we split SEMCOV and… Okay.
**Trask Stalnaker** 56:42 Yeah.
**Josh Suereth** 56:42 Alright.
Decisions I made 3 years ago, you can't hold me accountable for. No. I don't remember what…
**Liudmila Molkova** 56:52 Okay, so the last one, and it should be the easy one, we don't have Claudevents SIG, we can just say need SIG.
**Josh Suereth** 57:00 Yeah.
**Liudmila Molkova** 57:10 Yay!
**Josh Suereth** 57:10 he'll…
**Liudmila Molkova** 57:11 Super productive.
**Josh Suereth** 57:12 Just 160.
**Trask Stalnaker** 57:14 Left, yes.
**Liudmila Molkova** 57:16 trash, but maybe one day.
**Josh Suereth** 57:18 If we keep doing a little bit at a time, we'll get there, and we're making progress, so that's the key.
**Liudmila Molkova** 57:24 Wonderful. Thanks a lot. See you around. See you at the KubeCon!
**Trask Stalnaker** 57:27 Yeah, see you next week.
**Armin (Dynatrace)** 57:31 Goodbye.
