SIG: System Sem Conv Stability WG
Date: 2025-09-18
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/DThWWOuGTVF7wzD3mq6O0jApbm3clDdS6tR_xZCr-QVpHElpUlPAaLhpEejkTbjs.I6yg8W2q6ELpC7Mg
============================================================

## Zoom Recording Transcript

**Christos Markou** 01:00 Okay?
**Pablo Baeyens** 02:01 Hey.
**Christos Markou** 02:05 8.
**Pablo Baeyens** 04:08 We start.
**Fraggle Rock (ca-wat-brt3)** 04:10 I guess so.
**Christos Markou** 04:13 Yes.
I, I did mostly heads up.
on the agenda from my side, I… Started looking into… This guidance issue about,
Deciding which metrics should be recommended, and which should be the… should be… marked as opt-in.
Yeah, probably across the areas like system process,
Kate, containers, and so on.
So, and I think, from the quick search I did.
There are some JVM.NET-specific ones, but…
Yes, the same rules apply there.
Yeah.
My first impression is that… We should… Move forward with… Only… having CPU time as recommended.
And the rest of those.
since they are quite controversial, we spent, like, one or two months in the summer discussing about CPU utilization, and again, and also CPU usage is also, can be problematic, or at least not really straightforward.
And, david Asbold also, also shared a very interesting…
insight from the Kubernetes node.
special interest group, where they ended up considering the CPU usage
as, like, like a mistake. It was introduced for convenience, but it was, confusing in the end. So, based on this, I think, our best bet here is to go with CPU time and, leave the rest as opt-in.
**Fraggle Rock (ca-wat-brt3)** 06:12 Yeah, I think that makes sense.
That's… that's kind of where I'm landing, too.
Whatever we do end up… end up writing here.
Should definitely explain…
why you should use CPU time, and how you should use it in your scenario to get the same things as utilization would, and explain, like, why that's better than
Then the, usage and utilization metrics themselves, because people who don't know better, they just think they want, like, odd percentage, and…
realistically, they don't actually want that. You want to calculate the percentage eventually, but you don't want
The percentage to come in to your system, basically.
**Christos Markou** 06:57 Yeah. Is this… I… I wonder,
How easy that would be to create such a, like…
straightforward explanation, because utilization can be calculated, or at least, yeah, again, if that was easy to provide the guidance on how to calculate it, then we would be able to standardize this through a metric, right? So…
I'm still struggling to… but probably…
Oh, I can think of something.
**Fraggle Rock (ca-wat-brt3)** 07:32 Yeah, I… I had… I had that gist for a while, that it needs… it does need some work again.
But what I ended up doing was, at the bottom, I showed how you'd use PromQL on a CPU time, a cumulative CPU time metric, to get
A utilization on whatever window you want.
That was… I just used PromQL for that, and also, I'm not sure my PromQL was 100% right, so I needed to test that, but…
Probably something like that.
Would be… would be best.
**Christos Markou** 08:05 Yeah, okay.
**Fraggle Rock (ca-wat-brt3)** 08:06 I don't know where that lives and, like, how we make that authoritative, but…
**Christos Markou** 08:11 Yeah. My confusion comes from, like, for example, in Docker, I was checking the API, and they have a different way to, calculate this.
she'll… Yeah.
I can share this, here.
**Fraggle Rock (ca-wat-brt3)** 08:28 I guess the difference was… because Docker actually provides a point-in-time usage metric, right?
It's like a usage in cores or something.
**Christos Markou** 08:39 That's Kubernetes, that's…
**Fraggle Rock (ca-wat-brt3)** 08:41 David mentioned, so… Yeah.
**Christos Markou** 08:44 Like, a mistake one.
I share the Docker API here.
It seems they… Calculate CPU usage.
Should they take the delta first?
And then they divide this with, system CPU Delta.
And… Which I'm not sure what is it.
The system CPU.
And then… the… I think the normal… it's normalization.
Multiplying with number of SPUs. So, yeah,
It's a different thing. Maybe it's the shame, or… It's equivalent, but.
**Fraggle Rock (ca-wat-brt3)** 09:43 Yeah, what did mine do? Mine did, the… in PromQL, it was the… the rate of CPU time.
Over a 5-minute window.
divided by… The number of seconds that Occurred in 5 minutes.
**Christos Markou** 10:06 Okay, so… You jump from the cumulative to the…
Delta thing, and you divide by the window.
Okay.
It's more or less what the kubeletStats thing does.
They have a fixed range of 10 seconds, and…
**Fraggle Rock (ca-wat-brt3)** 10:27 Right.
**Christos Markou** 10:28 calculator.
the diff, but… okay. Yeah, if you have any comments, any immediate comments, feel free to add them there on the issue. Otherwise, I will try to put something, together.
**Fraggle Rock (ca-wat-brt3)** 10:42 Yeah, if I… if I had more time, I'd try to touch up the gist that I have. You can use anything out of it if you'd like. I'm not… probably not gonna have…
Any capacity to… to clean this up, unfortunately.
**Christos Markou** 10:57 No worries, I can, can work on it.
And, yeah, I see two other… I don't know, from… Cool those are.
Yeah, I suppose, Pablo.
**Pablo Baeyens** 11:16 those there, yeah, just so that we go through those PRs and… Decide what to tell… Thompson…
I guess on the first one, maybe, Christos, you can explain your comment?
**Christos Markou** 11:43 Yeah, right, about the attribute.
I'm not sure, yeah, this is a rename, right? So, when we do renames.
Do we completely remove the attributes from the The metric, or we're still…
To me, it makes sense to completely… Replace them directly.
there's no… easy way… I think there is no way to… Mark them as deprecated.
on the metric itself. They are deprecated in the registry, but they are not deprecated.
The metric, right?
**Pablo Baeyens** 12:24 Right, I don't know if… precedent on how we've done this? Like, have you…
done this on the Kubernetes metrics, for example?
**Christos Markou** 12:35 I don't have an example… a recent example, but, yeah, I could check. Or, yeah, I don't know if we can raise this with, maintainers or approvers, in case they are…
Oh.
It's easier for them to… Cover it.
**Fraggle Rock (ca-wat-brt3)** 12:52 Yeah, I thought… I thought renames replaced it. I thought if something…
Was renamed, and the attribute in the registry was marked as renamed, then on the metric, it gets…
if the metric's not stable, then it just gets changed, but I don't know… 100% what…
the intention is. What the intended route is.
**Pablo Baeyens** 13:22 How many of you both agree, Eden?
like, maybe we can test a little bit. I don't know if… Josh, you have an opinion?
**Josh Suereth** 13:36 I'm having trouble hearing you, Pablo. I think I heard my name there.
**Pablo Baeyens** 13:40 Yeah, We are discussing this comment and wondering if we need to…
Remove the old name on a rename, or… Cheers.
keep both… At least.
**Fraggle Rock (ca-wat-brt3)** 13:56 When we rename an attribute.
what should we do with the usage of the deprecated attribute on the metric? Just remove it and replace it with the new name?
**Josh Suereth** 14:05 Yeah, so you mark the old attribute as renamed to the new one, and you remove it from the old metric.
So, like, what should happen is there's a deprecation on the previous attribute that we can use to migrate it to the new one.
I think you can also do that just, like, directly on the notch. I'd have to look at the details of what that is, but,
Yeah, the diff, the diff, capabilities are crazy. Anyway, so in the previous one, market is deprecated, say it was renamed to the new one.
And so schema, if it's working, will just move everything from A to B.
So then, the metric just has the new name, and you're compatible, because you haven't broken anything there. What I don't know, though, is,
I think… it's possible.
That our policies will actually consider that a breakage.
You're not stable yet, though, right?
**Fraggle Rock (ca-wat-brt3)** 15:10 Yeah, this is on… this is on a development metric.
**Josh Suereth** 15:12 Okay, yeah, you're fine. We… We are… once you're stable, you won't be able to do that.
**Fraggle Rock (ca-wat-brt3)** 15:20 Yep.
**Josh Suereth** 15:21 just yet. Like, it's a thing we want to eventually enable as, like, a technique.
Because you have, like, gone through the work to explain to users how to make this not breaking. It's just, right now, our stability rules are way more constricted because we can't rely on diff.
So the way to do it is to define the diff, to define the deprecated move things. It's just, once you're stable.
since people aren't engaged with diffs as strongly as we want, we're actually not allowing even diff-based breaking changes for these things. You'd actually have to create a completely new metric.
In the future. For now. Until we get, like, the diff ecosystem built out and working.
**Fraggle Rock (ca-wat-brt3)** 16:05 Okay.
**Pablo Baeyens** 16:21 Yeah, so the… the PR does have… does have the deprecated reason renamed… renamed too, so… I guess.
**Fraggle Rock (ca-wat-brt3)** 16:31 Yeah.
**Pablo Baeyens** 16:34 It should be removed.
I can add a comment. And then on the other PR…
So… I'm just not sure what Thompson is saying here.
**Fraggle Rock (ca-wat-brt3)** 16:58 He's still digging his feet in about briefs.
He made the brief longer and said it was more detailed, but it doesn't actually add any details.
**Josh Suereth** 17:09 Which, which one is this, is this.
**Pablo Baeyens** 17:13 So it's a PR known only about briefs, but, it does include some briefs.
Related changes.
I just had it on the Zoom chat.
**Josh Suereth** 17:25 2706, is that the one?
**Fraggle Rock (ca-wat-brt3)** 17:27 Yeah.
Yep.
Was there something else to talk about on this one?
**Pablo Baeyens** 17:36 No, just… I… I think I can still push back, it's just… I…
I don't understand the very last comment on…
The member brief has been extracted from the attribute brief.
Thing.
I don't…
**Fraggle Rock (ca-wat-brt3)** 17:51 Yeah, I don't know… he… he seems to be, like, super laser-focused on getting briefs in, and he says he made it… he…
So, providing additional value?
**Josh Suereth** 18:02 For context, Lyudmila has blocked almost all of the ad briefs to Inums.
PRs in SemConf, because we think it's going to add a significant overhead for low value. When the brief comment is just the same thing as the value, but capitalized, that's something we'd rather provide in our doc generation, as opposed to make everybody write that manually. So,
In previous things, we said if briefs don't add a lot of value over,
Over just taking the thing and making it be capital, like, then we shouldn't have briefs.
If you think this brief provides value to understand what it is, feel free to take it on merit there, but just for context, we've been blocking a lot of the brief-based, like, things that just add brief.
It looks like this PR is two things, though. One is to merge two attributes into one, in some fashion.
What, system paging fault type and process paging fault type are now…
the same thing, is that right?
**Fraggle Rock (ca-wat-brt3)** 19:09 Basically, we had… we had… I opened this issue, like, a super long time ago, but, like, there isn't much reason for those two metrics to be different, because… those two attributes to be different, because they're just saying the same thing. It's just that one was being used in process, and one was being used in system.
**Josh Suereth** 19:23 Hmm.
So, my recommendation with this,
is, you know, look at it… I would focus on, when it comes to the brief thing.
you can push back on briefing. If this actually advances the goals, those systems sound kind of cool, like, evaluate on merit there. But…
if you're… if you're questioning it, like, feel free to push back. Feel free to wait. There's… there's, I think, about 75 open PRs from this individual, with similar comments and similar pushback, so, it's fine to continue to push back.
**Pablo Baeyens** 20:05 Okay, I can… I can push back. I don't… Okay, like, it adds value.
**Fraggle Rock (ca-wat-brt3)** 20:12 Yeah, it doesn't add that much. The only… the only devil's advocate thing I can say is that we… we chose the verbiage of major and minor for the paging fault type, but in some contexts, it's called a hard or soft page fault.
So it could add value to say, like…
Major, major page faults, sometimes called hard page faults, or something like that, make it very obvious that it's, like, the same thing.
I still… I don't think it has, like, that much value, but it's not as bad as, like.
every other day.
brief. It's like, it is saying something, at least.
**Josh Suereth** 20:48 Yeah, so, so just ask for that directly then, Braden. Like, just, like, on it, say, here's, like, this is the PR we would accept. If you want to add a brief that just says this is, you know, this is annotated as this, that's fine. Your other option is you could just open a PR that does it.
And say, here's what we wanted to see. But at this point, I would… what I'd recommend with this is basically show, don't tell.
A little bit, like, I think we're past the tell and wait. We're into show, don't tell.
So…
**Fraggle Rock (ca-wat-brt3)** 21:34 I'll put them in as, like, as PR suggestions, and then… If they're still fighting it.
I feel like they won't, because I'm just rewording what they want to say anyway.
**Josh Suereth** 21:49 Yeah, I'm… one thing that I'm… I'm a little nervous on here, because I see this again,
is where there's a new attribute added that has a very similar name as an old attribute, but the metric now has both of those attributes, if I'm reading this right.
So, under.
**Fraggle Rock (ca-wat-brt3)** 22:06 No problem.
**Josh Suereth** 22:08 Yeah.
So in model system metrics YAML. Yeah, so if we're going to rename the metric to be fault type and reuse it across everything, system paging type and system fault type, you know, basically both shouldn't show up.
So, I think that's fixable.
But that's another thing to call out on this PR.
That's true.
**Fraggle Rock (ca-wat-brt3)** 22:34 I'll leave the review on this one, since I opened the issue he's addressing.
**Josh Suereth** 22:38 Yeah, yeah, just make sure that the thing that you wanted is actually resolved.
Which I can't tell, right, because process paging fault still exists and is still on metrics, and system paging type is still… exists and still in metrics. So if we're trying to move to one, I think you have that opportunity now
To make that braking change.
And if I recall correctly, you guys all have the header that, like, don't use SystemSemCom until we stabilize thing that we did for HTTP? Is that correct?
**Fraggle Rock (ca-wat-brt3)** 23:10 Yeah.
**Josh Suereth** 23:10 Okay. Actually, do we? I don't remember if we put that anywhere.
**Pablo Baeyens** 23:14 Bye.
What do we have?
**Fraggle Rock (ca-wat-brt3)** 23:18 Okay.
**Pablo Baeyens** 23:19 But let's… let's… let me check.
**Josh Suereth** 23:21 It's been so long since I remember looking at it that I don't… I just wanted to verify. Cause I think you guys did that a while ago.
Let's see…
System…
**Pablo Baeyens** 23:37 Yeah, so, for example, on the system metrics, right after the…
table of contents, it says,
Existing instrumentation should not adopt record changes until Danbrook steeple.
**Fraggle Rock (ca-wat-brt3)** 23:56 Makes sense.
**Josh Suereth** 23:57 Cool. So yeah, I think you're totally fine to make that change then, if you want. We just would need to make sure, like, the…
The rest of the cleanup happens.
Cool.
**Christos Markou** 24:40 Seems we're good for today.
**Fraggle Rock (ca-wat-brt3)** 24:44 Yep, I think so.
**Christos Markou** 24:48 Okay.
**Fraggle Rock (ca-wat-brt3)** 24:49 Anything you want to bring up, Josh, while you're here?
**Josh Suereth** 24:52 Just checking on what y'all need to stabilize. So, I'm gonna try to pay more… when I have time to attend, I'll try to pay more attention and make sure things are moving smoothly, because it looks like y'all are very close to marking these things as stable, right?
**Fraggle Rock (ca-wat-brt3)** 25:09 Yeah, we're making an effort on the process namespace specifically, since it's the closest, so we're gonna try and push it.
**Josh Suereth** 25:17 Sweet. I think you'll be the first ones to use the stability level of release candidate, because that did not exist previously, when we stabilized things. So,
The other thing I want to make sure of is if you run into tooling issues, where our tooling doesn't handle the move from experimental stable to, you know, alpha, beta.
release, all that kind of crap that we have now. I'm here to help fix that, too. So, if the tools don't work, let me know. Ping me in chat as soon as you can, but also I'll try to attend so I can catch if I see something going broken that would…
cause problems.
**Fraggle Rock (ca-wat-brt3)** 25:54 Cool. Sounds good.
**Christos Markou** 25:56 Are we targeting the whole process namespace, or,
We don't know yet. Or just specific metrics, initially.
**Fraggle Rock (ca-wat-brt3)** 26:04 I don't think… I don't think it necessarily has to be the whole process namespace, but from everything I've seen, like, most of… most of the process namespaces…
is pretty close anyway, but it doesn't have to be the whole one. We can sort of make a decision on the most important ones.
**Josh Suereth** 26:20 Are you planning to do the entities in process? Or the entity?
Because I think that one is lacking…
Descriptive versus identifying split, if I recall correctly.
**Fraggle Rock (ca-wat-brt3)** 26:32 Yeah, I think we… I can take an action item to finalize that, because I think we know what we want to say for what's identifying and what's descriptive, and we just haven't written it down, so…
**Pablo Baeyens** 26:44 Yeah, we have the issue here, and that is part of the geopuckers, so…
**Josh Suereth** 26:52 Yeah, my recommendation would be,
to actually flow from the signals. So, you know, if you have a metric that says it's annotated, that it's associated with an entity.
Take the metric and all the attributes it references, take the entity and all the attributes it references, stabilize all those. You don't have to stabilize all of the things in the process namespace.
But if you try to stabilize something that doesn't have a metric or, like, resource attribute that you're providing with it, which would be the process entity,
we're trying to make sure everything is actually implemented, that is in SEMCOM, that is stable, that actually produces a signal.
So, that would be the way that I would go about this, of like, okay, we're gonna stabilize these 5 metrics. To stabilize these 5, I have to stabilize these 5 attributes. And our tooling should be at the case where if you do, make file check, or check policy, or whatever it's called.
It will warn you of all the attributes you rely on that are not marked stable, so if you just try to mark the metric as stable, it'll tell you all the things you have to go fix.
I don't think we check entities yet, but that… that's one reason I'm here. I'm gonna make myself a note to go add a stable entity check for stable… for stable metrics.
So that we make sure that, you know, the whole kit and caboodle is… stabilize together.
**Fraggle Rock (ca-wat-brt3)** 28:16 This is a… this is a just upwards check, right? Like, if we mark a metric as stable, the entity it refers to has to be stable, and not, like, all of the metrics that use the entity have to be stable.
**Josh Suereth** 28:28 Yeah, yeah, yeah, this would be just an upwards check. If I… if I add one, which I'm… which I think I'm going to do, but I need to think through it. Yeah. Right now, that check isn't there, but I would recommend that you stabilize the entity, too, because you're… you have a dependency, right?
**Fraggle Rock (ca-wat-brt3)** 28:42 Yeah.
**Josh Suereth** 28:44 Yeah, the check that is there is the upwards attribute check. So if you stabilize a metric, all the attributes that it uses have to be stable.
**Fraggle Rock (ca-wat-brt3)** 28:52 Unless it's opt-in, in which case you can have opt-in attributes that are not stable.
So we… for descriptive… have we made a decision on whether adding opt-in descriptive attributes is considered breaking or not?
**Josh Suereth** 29:07 It is non-breaking.
**Fraggle Rock (ca-wat-brt3)** 29:08 Okay.
Because that's the main thing I expect to change. For process, we're pretty set in our identifying attributes, I'm pretty sure. There kind of is just kind of one way to identify a process on a system anyway.
the… but it's, like, adding descriptive attributes is the kind of thing I expect to change over time.
Especially as, like, different systems decide they want more detailed things that only exist on Windows or Linux or something like that. As long as that's not breaking, then I think we can… I feel pretty good about stabilizing the entity once we've nailed down.
**Josh Suereth** 29:45 Yeah, we've written everything down.
That's the big reason we have descriptive attributes, is so that we can consider adding things non-breaking, yeah.
**Fraggle Rock (ca-wat-brt3)** 29:53 Yeah.
**Josh Suereth** 29:54 Yeah.
Cool.
I gotta jump to the entity SIG, but, if you need any help getting things stable, let me know, and I'm, I'm just, again, great work pushing through. Here to help, let me know what I can do.
**Fraggle Rock (ca-wat-brt3)** 30:07 Thanks, Josh.
**Pablo Baeyens** 30:08 You…
**Christos Markou** 30:09 See you next week.
Talk to you later.
**Pablo Baeyens** 30:10 the year.
