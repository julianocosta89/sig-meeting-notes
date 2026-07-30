SIG: Technical Committee
Date: 2025-07-30
Duration: 35 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang** 00:46 Hello, Tigler!
**Tigran Najaryan** 00:51 Hey? Ronnie! Good morning.
**Reiley Yang** 00:53 Hey! Morning!
**Josh Suereth** 01:49 Hey!
**Reiley Yang** 01:50 Hi! Josh.
**Tigran Najaryan** 01:53 Hey? Good morning.
You do start, or maybe one arm in spec.
**Reiley Yang** 03:20 Possible reason for Carlos.
**Josh Suereth** 03:24 Yeah, it was Carlos. Gonna be 5 min late again.
I didn't check our slack.
**Reiley Yang** 03:34 I don't see any message from him.
**Armin (Dynatrace)** 03:39 Not from the others. I think, Utmia said. She's on vacation or posted in the past.
**Josh Suereth** 03:47 I was just in a meeting with her, so if she's on vacation, then she should not be coming to open telemetry sync meetings.
**Carlos Alberto Cortez** 03:57 Little miller you mean.
**Josh Suereth** 03:58 Yeah, blue Miller. Yeah.
but you're right, Armin. She did say she was gonna be on vacation. So maybe we give her a hard time about not having a long enough vacation.
**Carlos Alberto Cortez** 04:10 I think she's starting next week, so probably she's taking week off.
**Liudmila Molkova** 04:16 And I know I'm here.
**Carlos Alberto Cortez** 04:17 Oh!
**Liudmila Molkova** 04:17 Sorry.
**Carlos Alberto Cortez** 04:18 Hello!
Shouldn't you be taking holidays.
**Liudmila Molkova** 04:22 I should should have. I took them last week. No holidays for me anymore.
**Carlos Alberto Cortez** 04:26 Really, okay.
**Josh Suereth** 04:28 Are. Are you saying Grafana doesn't give holidays? Is that? Is that what I'm hearing.
**Liudmila Molkova** 04:33 Not yet, because I'm still at Microsoft, and I need to wrap things up. But it's my. Tomorrow is my last day.
**Josh Suereth** 04:41 Wow! Well, congratulations, I guess this is public now. So yeah.
**Liudmila Molkova** 04:48 Yeah, thank you. It is public.
**Carlos Alberto Cortez** 04:53 Nice.
Okay, thank you so much. Sorry for being late. By the way, I totally forgot that. Now I have to try, like you know as part of rotating process. The person in charge has to drive these discussions, too. Okay, so let's start. Yeah, we have some items. Let's go over them, and then maybe private meeting after.
**Reiley Yang** 05:14 Yeah, so I have a pr I I mentioned it last week. So this is a follow up, and please help to review and comment the main point here you you see there is. I'm I'm trying to give a list what the maintenance should take care of from the security perspective. And instead of just focusing on security advisor is there. There are other things, and they should put it holistically and try to prioritize that as a single pane of glass.
That's a key point. I think the current problem is many maintainers. They might realize a certain aspect like they might take care of the supply chain security, or they might take care of the security advisory, but they ignore the other parts, which is considered as a serious gap.
That's all.
**Tigran Najaryan** 06:10 3 years on this right. Friday.
**Reiley Yang** 06:13 Yeah, just take time to review and comment.
**Tigran Najaryan** 06:16 Good.
**Carlos Alberto Cortez** 06:18 Yeah, it's kind of long. So I don't think there's enough time to review it here. Well, we could, but probably it's better offline.
**Liudmila Molkova** 06:25 It would be nice like, how do we want maintainers to know about this.
**Reiley Yang** 06:31 So 1st we review the Pr. And and we take comments from the Tc. And the 6 security, and once we align we should merge it, and then this will be a proposal. We share that in the Tuesday Maintainer and Spec meeting, and see if there's any outstanding concern from the maintainers. If not, we'll start by pushing for execution, and then take feedback and improve.
**Armin (Dynatrace)** 06:56 Sounds perfect. We might also consider to to put it in the in the community repository later, if we have a broad agreement also by maintainers on it.
**Reiley Yang** 07:10 Yeah.
**Carlos Alberto Cortez** 07:19 Okay, yeah. So let's review that offline. Thank you so much for that, Josh, it's pick my point.
**Josh Suereth** 07:27 So yeah, this is this is something I wanna 1st apologize for not making quick progress on this, because I think this is. This was meant to be done quickly as part of like the Tc. Responsibilities. But 1 1 thing that I want to make sure we don't lose the Tc structuring document was about and the the sponsorship is about making sure. Tc. Are active leaders in the ecosystem.
However, domain experts are still required.
and a domain expert might not actually be an active leader, but still be someone who can provide valuable insight.
And you know, understanding of our specification. And so I want to start accelerating the Spec Maintainer idea.
where basically, the Tc of today would also be spec maintainers.
And we might be able to promote people into spec maintainership like Josh Mcdonald comes to mind immediately as an Xtc. Member. Sergey Conchloe may be a spec maintainer. We could ask. I doubt he would have time to to like, participate Yuri would also be an ideal spec maintainer, right of like they have domain expertise, and we want to preserve that they are not able to commit the time to be in active leadership roles. But we're trying to divorce those 2 things.
And so I. What what I don't want to have happen is because we focused on one, we lose the other.
So this would be like a a way of of us acknowledging folks who have critical domain expertise or important to the open telemetry project. Give them the ability to to have, you know, approver rights on the spec or merge rights on the spec for critical domains, but not have the requirement of sponsoring across the ecosystem. You know they're able to be a domain expertise in an area and and continue to provide that as a valuable thing.
I wanted to basically run that past everyone again and make sure this is still a priority, or if I'm kind of thinking too broadly or overly nervous, one of the 2.
So how do we like? How do we feel about creating a spec Maintainer position that would be independent of the Tc.
**Tigran Najaryan** 09:45 Josh, do we? We have the spec sponsors now? Right?
Do they all become automatically spec maintainers?
Is that.
**Josh Suereth** 09:54 My, my initial thinking is they all become spec approvers, general purpose spec approvers. We still call it a sponsorship role, because they're expected to sponsor people through the specification.
and that and the the whole, like contributor to approver, to maintainer.
In the specification it is contributor to sponsor, to maintainer is, is the the hierarchy.
**Tigran Najaryan** 10:17 And the sponsors. They they, I think they are already approvers, right? They have the approval rights today, so that essentially they, they will be approvers, slash sponsors and maintainers is a level above that. You're saying.
**Josh Suereth** 10:31 Yes, yep. So maintainers would be able to release the spec actually merge things. And and that's.
**Tigran Najaryan** 10:38 Be responsible for maintaining essentially.
**Josh Suereth** 10:41 Yes.
yeah, it. It's the same as any other maintainer role. It's just they they actually have the maintainership of the specification. And we would have.
**Tigran Najaryan** 10:49 Makes sense.
Yeah.
Makes sense. For. For again, it will be consistent with what we do elsewhere in other repositories, makes sense to me.
**Josh Suereth** 10:58 Okay.
I think that does. So. There are a few concerns that were raised. We can talk through. That does mean, you know, right now the the predominant thing the technical committee was doing was actually spec maintainership.
Like, if you think about it on a day-to-day basis, we were active leaders in the project, but we were also predominantly being spec maintainers. So I think it does dramatically change the the scope of the Tc role.
do we require Tc members to be spec maintainers. Yeah, Riley, Riley wants that to be true. So I think we have a few concerns. One is, Do yeah, do Tc members have to be spec maintainers.
A second concern is, do we have the same set of specification maintainers for the protocol and the specification? Or are those different groups of people.
**Tigran Najaryan** 11:51 Can be different doesn't have to be the same right?
They're separate repositories. So we have a I guess that there's a natural opportunity for us to split those responsibilities. If somebody wants to be a maintainer in both, that's great. They can be no problem with that. But we don't. We don't have to make everybody who doesn't want to have anything to do with the protocol details and intricacies to also be a Maintainer. There.
I think that's fine.
**Josh Suereth** 12:21 Okay, let's go back to the should Tc members be required to be spec maintainers.
Carlos and Riley, you want to talk through your thoughts. There.
**Reiley Yang** 12:33 So when we started the technical committee, I think number one like Job for the Tc is to maintain the spac.
And in case like there, there's like someone has to establish how people take care of the spec repository.
I I still feel like Tc. Has the ultimate accountability. So unless Tc. Can define a rule and hold the Maintainers accountable. It shouldn't give away that accountability.
So I I would say, at least, for now, and the Spec Maintainer is like. Together with all the Tc members.
they can figure out how to move forward. So by default is Tc. Member must be spike maintainers and work with the other spec maintainers to reach agreement. If you want to make the change later.
**Tigran Najaryan** 13:31 I think the thinking here is that the the spec is essentially the spine of open clarity mistakes there are amplified everywhere else.
So and if you're oblivious to to the spec.
you probably you probably can't be very efficient as a as a Tc. Member. Right?
can be varying degrees of of, I guess, understanding of the spec, particularly of specific areas of the specification. We're not expecting everybody to be to be experts of everything in in the spec.
But there is. There has to be some level minimal level of understanding and feeling of responsibility for for the spec. That, in my opinion, is something that we expect the PC. Members to have so as much as I would say that I mean no, I don't even want to say that I think we should be, we all should be maintainers of the spec.
**Reiley Yang** 14:29 Yeah. Or, in other words, if you're a Tc. Member, but you're not a spec maintainer, then someone else is a spec maintainer. But they're not the the Tc. Member. Then I I would say, if there's a conflict on the open telemetry overall design. Whoever has a spec Maintainer role should have the ultimate call.
**Carlos Alberto Cortez** 14:53 Yeah, I just want to add that in the worst case, in case, let's say, hypothetically speaking, that she is too busy with other stuff. I. That at the very least I could say half of the Tc. Should be maintainers of the spec. Worst case the best would be that all of us are maintainers, but at least worst case have the Tc. At least.
**Reiley Yang** 15:15 Yeah, my my main doubt is being a Tc. Member, but not a spec maintainer. Comparing to someone being a spec Maintainer, but not a Tc. Member who has like, who has demonstrated more knowledge about open telemetry, overall design.
because in the way of a technical conflict happened, someone needs to make the the final call, so there will be a Tc vote. But if we have a Tc. Member who is not good at the spec.
then how would they? How to vote?
They can probably help on some like logistics. But then, essentially, it's like Pm. Job, or like Gc. Job.
**Carlos Alberto Cortez** 15:58 What's your opinion on this one? Yeah.
**Josh Suereth** 16:01 Oh, I I my! My opinion is an unformed a bit here. That's why I'm trying to like elicit our rationale behind it. The thing that I've been focused on is what I said at the beginning. Like we have expertise, this expertise is incredibly valuable to our ecosystem, but the time commitments to be a visible leader in open telemetry are high.
And how do we preserve technical leadership where we don't have that time? Commitment?
Is something I want to make sure we have a spec maintainers. And then starting to ask the questions around it. So I'm more focused around. I was more focused around the inverse of like.
what's the spec maintainer position? What does it mean? What's the value of it? Why would someone do it? And what's the time? Commitment for it. Right and ideally. The time commitment is, you're in the repo. You're reviewing issues that come in. You're reviewing Prs, and you're offering your opinion advice, and you're merging or blocking Prs based on your expertise. Right? The same way we think of maintainership and other repos.
So I want to make sure we we preserve that the notion of the the future shape of the Tc. I'm still trying to understand how we accommodate things that aren't in the specification. I think, just frankly, the collector.
I don't think, has a lot of things that are in the specification, even when it should and I think there are aspects of the collector that maybe need to be specified, or maybe need to be part of that and I'm trying to understand how to bridge the gap there a little bit. There are also, like, areas of our ecosystem that might never participate with a specification that are important areas of leadership that Tc has to be aware of, like the the open telemetry operator. Right? Maybe that does belong a piece of it in the spec. Maybe it doesn't.
Let's let's look at a world where it never participates in the spec. The collector, the operator, you know, some of this Bela Ebpf stuff, some of this auto instrumentation capabilities. There are people that are active and technically aware of how open telemetry interrelates that aren't in the spec.
you know, having them participate with the Tc. Makes sense. I like what you're saying, Carlos, around. I think worst case would be, you know.
at least half the Tc. Has to be spec Maintainers. I think the spec gives you grounding. You need to work in the space. Is it a requirement or not? I'm I'm undecided personally.
that's the problem. I see that I want to see if we can address. I would prefer, if we could get those communities to engage with the specification, but if they never have a need to engage with the specification, but they are engaging with library sdks with the collector, with, like other parts of open telemetry, the profiling Sig, the Sam Sig. If they're in the community embedded.
I still think they can do a good job without being a spec maintainer. They just never had a reason to push a spec.
Do I have a name of a person like that? I do not, and that's why the question is, am I? Am I dealing in a theoretical that doesn't exist? But I think could. And so I'm you know I don't want to let perfect be the enemy of good for now, if we were to say we require spec maintainership to be on the Tc. I'm comfortable with that, because I can't think of a name of somebody who operates at that level across all the ecosystem. That that isn't isn't in the spec right?
And I do think we want to encourage more engagement.
like from the collector into the spec, for example.
But that's anyway. Go ahead, Luma.
**Liudmila Molkova** 19:49 Yeah, I have some thoughts on the thing you mentioned earlier on the responsibilities. So there is a maintain main maintainership in terms of, we are responsible for the spec integrity and making good technical decisions in a lot of cases. This is not what we do like. Anybody can release this pack, or almost anyone can drive this pack call. Carlos is doing amazing and does a lot of groundwork, but somebody else, not who is not in this call would do the same.
And we could have a maintainer role.
It does not remove Tc responsibility for the overall thing, but it allows us to share the responsibility. Some of the responsibilities with others who are ready. There are plenty of people who can be ready to do some of the maintenance tasks.
Also it creates a letter for people, right? And for some reason it's important for for some of them.
That's it.
**Tigran Najaryan** 21:01 So I I was. I was trying to think of some arguments that that support the idea that the Tc. Member shouldn't be a, I guess, is not required to be a spec maintainer. And this is not, I guess, an argument that supports it. But the way I'm thinking about it is that what we call a Maintainer implies 2 actually distinct things. One is actually maintaining the reports repository in the sense that I don't know you you make sure it builds the Github actions work that you do, the releases. All the logistics associated with having a Github repository.
and the other second part is being knowledgeable.
being an expert of of that repository. And to me it's it's quite obvious that if you're a Tc. Member, you have to be knowledgeable right. There's like there's no escaping that. If you don't understand, you don't know the spec, or at least I guess a portion, a subset of it. You're not an expert on that.
You can be very efficient as a Tc. Member.
The the 1st part of those responsibilities, though.
technically speaking, if I don't know how to release the repository doesn't probably make me less valuable in in being a person who who can be effective at at working with the rest of the community and bring the the spec perspective into that right. That, said I. I'm not sure I want to make that separation right. I want to say that.
Oh, I am a I'm a i'm an expert in the specification. I can be efficient as a Tc. Member.
I don't want the responsibilities of maintaining it. I don't know if I want that to be honest with the I guess with that.
if you will, it's a cliche. But with that knowledge and that that position comes the responsibility also, maybe right. Unless we see some sort of an evidence to the contrary, I would say, suggest that we we go with that right? You're a Tc. Member.
You're supposed to do the I guess the the Maintainership part right. The Literal Maintainership part as well, for now we can change that if we find some evidence of the opposite necessary of being, of having the the opposite being the case. But for now it's I think that's my opinion. We should just do that.
Be maintainers.
**Josh Suereth** 23:39 I let me take what you're saying a step further.
What if? What if the requirement was? You had to be a maintainer of one or more open telemetry projects.
Is that reasonable? Or does it need to be the specification? By the way, I'm still unformed. So I'm just challenging every idea I'm playing devil's advocate. I'm not suggesting that I believe this. I just want to challenge. So like, if you are a Maintainer or something you've committed right to responsibility?
Does it have to be the specification.
**Reiley Yang** 24:14 It has to be some sort of specification, not necessarily strictly the specification repository. For example, I consider semantic convention the same as the specification repository. Actually, they were in the same place. And then we split them because there's a natural like separation of of interest. So Proudhoe is the same. So I consider a proud Hall semantic convention. The current spec report. Those are very cross cutting, and they serve as a foundation for the entire project. If we need some spec, for, for example, like for Collector or Beta.
we can decide whether that should go to the Semantic Convention repository. Maybe they have some semantic convention, or maybe even later, we can say, now we have more and more configuration that should go to their repo. But I consider this type of things are the same power as a spec.
So my answer is, yes, they. They need to be maintainer of a spike report, but not necessarily the only like the the specific name, open telemetry, specification.
and the Tca. Probably need to call that out like there, there's certain subset of repositories that we consider as the cross cutting foundation for the project. So, as a Tca. Member, you have to be at least a maintainer of one of these repositories.
**Tigran Najaryan** 25:39 I think what's implied a bit here is that as a Tc. Member, you probably have an obligation to apply yourself in a place where, where your radius of influence is, is the is the largest on the project.
and there's no other place like that than the specification repository, which is, I guess, which impacts most other most other things in open telemetry. That's what the what's implied here in a way. Right? So if I go and do my work in some.
I guess.
quite distant corner of open telemetry. I do. O. Pump, go! And and I'm a Maintainer there. That's valuable, but less impactful than maintaining the the specification. That's that's, I think, the the point here. Right? So.
volume wise. You may be spending the same amount of effort and then hours and something. But the outcome of what you're doing. The impact of what you're doing is a lot less pronounced elsewhere.
And so I see it's sort of a duty, if you're a Tc. Member, to to spend your time, if you will, to waste it less on things that have smaller impact radios and spend it more on things that have large impact radios.
That's this is my way of thinking which which doesn't contradict to what you're saying, Riley. If there is other places with that large impact radius. Maybe that's that's what you what you work on, right, the same con board. Whatever else we designate as being of similar impact level as the Specification Repository.
**Liudmila Molkova** 27:23 So maybe it's both. So the let me explain the spec, unless it's some emerging area like profiling where we had a lot of discussions on logs. The spec is somewhat quiet lately. Right?
There are some caveats here and there.
but there is very little feature work on, let's say, tracing core metrics.
And If it continues, we would run out of work, and the the only things in the spec, and it's a great shape for the spec right to be the small caveats here and there.
plus rare spikes of new areas. So as a CC. Members, I see at least my responsibilities are that okay? I'm paying attention to what happens in the spec, that it does not break.
that we address the issues that arise. But you should also be involved into something else, something new, something evolving.
Otherwise you just have no interest in driving any anything new, or you don't know what what's going on out there.
**Tigran Najaryan** 28:46 To add a bit on this, I guess continuation of what you guys were saying as an example, the the product repository. I think it's no less impactful than the spec. For example.
if you look at the profiling.
the entire profiling seeds work of the last year, or even more than the year has been all about the data model and the product, all of that right, that they've been spending all of their efforts virtually on that. Not all. But the the significant part of their effort was on that it has a lot of consequences. The way that you design the first, st the data model, then the the I guess, what, together with the with the protos.
is, in my opinion, no less impactful than the definition of the Apis, and how the Sdks are supposed to work.
**Carlos Alberto Cortez** 29:51 So what do you think, Josh? Is that in all feedback? Or you would like to discuss some further points.
**Josh Suereth** 29:58 This. This is awesome. I so I think there wasn't a lot of contention on the idea of a spec Maintainer role.
So as a straw man. I'm going to put together a proposal to have a spec Maintainer role, a proto maintainer role.
If there's we already split out. Semcov, I'm not aware of other things that we will need to split out. If you're aware of something else that we are maintaining, that we need to fragment, let me know. But like, basically, there'd be proto proto maintainers and spec maintainers. Initially, they would be seated with all of us.
and we can change the shape of it as it goes right that and then we can evaluate. If we want to raise people into the Maintainership role. Like, I think we have some names we could actually reach out to that could be maintainers.
but that that would be priority number one. The second bit. This longer discussion about.
What about maintainership on the Tc. My, my argument for now would be, let's let's keep the current requirement that spec sponsors are candidates for Tc.
right? And we look for people who are active in the spec. But let's continue that conversation. I I heard a lot of really good arguments I need to think through. But I haven't actually formulated a strong opinion here. I could go either way. Right? But let's let's preserve status quo for now, and let's keep the discussion going. Does that sound reasonable as a straw man.
**Reiley Yang** 31:31 Sounds good to me. I have a quick question, Josh, so maybe like, give heads up to the Gc. And and make the changes as soon as possible. So we have maintainers, approvals, and triagers for every single repository opentelemetry. There's no exception. And then, like currently, if you look at the spec. It's kind of maintainers are directly tied to Tc triagers are tied to Gc. Which I consider as bug. So we just have those groups. But that that group would just mirror the existing members we already have. And then you can work on the Pr to give a proposal. We can see, how do we? How do we add or remove members.
**Josh Suereth** 32:18 That that makes a lot of sense. So sorry.
in terms of getting to the Gc. Should I send them a chat with a quick outline, like we did here or I was actually gonna write up the proposal and send it to them directly. First, st right? So like, put make the proposal, get it to them for evaluation. Get it to you all for evaluation simultaneously. Is that reasonable? Or do you think we should be faster and more urgent than that.
**Reiley Yang** 32:48 Not urgent, but I feel that conversation, deciding which members should be there, might take time while changing the group and making sure we have consistency and can start to enforce it. So if there's a new repository.
we can have a daily scan in the Admin repo, making sure that all the repositories follow the same pattern that part can help immediately. So it's not for you.
**Josh Suereth** 33:14 No, no, and and we do want to move quickly. I just the there's this is a task I'm taking as a long term improvement task. I cannot move fast unless I drop something else that I'm doing. So like my plan was to get this proposal out, probably end of the week or early next week, so that by the time we have the Gctc. Meeting we can discuss this with them, and that it gives us time to review.
But I like I just frankly, I can't move fast on this. I don't have the bandwidth to move quickly. I'm just trying to make sure it moves because I think it's important.
So if somebody else wants to take it like, feel free, because I think the discussion we just had was was awesome. I think we all understand what we want to see. I'm happy to do the driving of it. That's fine, but if it like, if I'm doing the driving. It's it's gonna take a little while, just frankly.
**Reiley Yang** 34:08 I can work with the Gc. A specific like trust, because 2 of us are super active on the Admin repository. So we're trying to enforce consistency, and this might be an easy change.
**Josh Suereth** 34:20 Yeah, yeah, if you can do that on the admin stuff that'd be awesome. I'll get the proposal out as quickly as I can. But it's probably going to be next week at earliest.
Yeah. And I think it might be time to go to the private topic. Now, if that's amenable to everybody.
**Carlos Alberto Cortez** 34:35 Yeah, that's what I wanted to ask, because we only have 25 min. I don't know how long that is, but we can do that.
**Josh Suereth** 34:43 I think we should use at least 20 min for the private topic, and then we can.
We can decide if we need more time. Next week.
Okay.
**Liudmila Molkova** 34:53 Is there a link for a private topic.
**Josh Suereth** 34:56 It. It's in the. It's in the slack channel.
**Liudmila Molkova** 34:59 Okay.
**Josh Suereth** 34:59 So in the bookmarks there's a.
**Liudmila Molkova** 35:01 Yeah.
**Josh Suereth** 35:02 Armin gave us a bunch of nice links.
Oh, thank you.
**Armin (Dynatrace)** 35:05 There!
