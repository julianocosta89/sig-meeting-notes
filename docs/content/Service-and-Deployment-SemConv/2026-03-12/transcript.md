SIG: Service and Deployment SemConv
Date: 2026-03-12
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Ayushi Asthana** 02:11 Should we get started, or wait for a few more minutes for more folks to join?
**Josh Suereth** 02:26 I think we can probably get.
**Ayushi Asthana** 02:31 Let me share my screen. So, John, we had a conflict, so she might be joining us in the second half.
In the meanwhile, let's get started.
So we had a meeting with Yoshi last week. I gave him a quick rundown of what we're proposing with the data entity.
And what, and his thoughts were basically to involve a few folks in the data security domain to get some initial feedback.
And he has offered to reach out to his network, in order to get some initial thoughts.
Besides that, we also briefly talked about the deployment.environment PRs that are up, and Yoshi is mostly aligned on what we're proposing now.
So, that was about last week.
On this week's agenda, we only have two items, so if there is anything else anyone would like to add, please feel free to do that now.
We… last… last time that we met, we discussed about the data entity proposal, and there were concerns about how the instrumentation would work for the different attributes that we are proposing.
And there was also some discussion about what the name of the entity should be, so maybe we can conclude on that today.
Ankit also has an item for service.businessUnit.
So, I think before we dive into discussing about instrumentation for data entity, maybe, Ankit, you want to go ahead and talk about, your item first?
**Ankit (Google)** 04:12 Sure, works for me.
So previously I had proposed a proposal for Cost Center as well. That one was, I think, mostly agreed upon in our ways to PR. This is along similar lines, a task to GitHub issue, and there's a proposal doc inside it.
The link is in the GitHub issue. Should I just go over the proposal? Maybe I'll take 5 minutes.
**Ayushi Asthana** 04:36 Yeah, I have stopped sharing, you can share your screen and… Talk about the proposal.
**Ankit (Google)** 04:44 Thanks, just a moment.
Isn't that screen visible?
Yeah, alright. So, while the cost center thing, it handles financial accounting, I wanted to introduce this business unit to handle the functional or the operational hierarchy of an organization. For example, retail versus industry banking.
I have introduced businessunit.id as an identifier for the business unit, similar to the cost center ID that we previously discussed.
I have here, attached its usages across, the platforms like AWS, Azure, GCP, so while there's no standard guidelines here on what tags to use.
The documentation do mention here and there some examples of what you can use, and based on these, it's like either business unit, or business underscore unit, or some other… or division, or some other combination of these.
So… Having a standard… attribute here would help unify these… all these stacks. You can go over the links offline.
Coming to Kubernetes and infrastructure conventions. So, I see that, based on my research, most multi-tenancy models, they use business unit as the highest level boundary, and usually map it one-on-one with namespaces or clusters. So, having a standard attribute would help here as well, and then the admission policies can also probably rely on This, can also utilize this so that all resources have such labels or tags.
The observability platforms as well. I have attached some references for ServiceNow, Datadog, and Splunk on how they currently utilize this. So, since this is not standard right now, usually this is fragmented, but most of them utilize it in one way or the other.
You can't go over them offline for details.
So overall, I see the benefits of standardizing here would be in showback reporting to the leadership, for example, what business unit is generating how much revenue, or how much is spent on that business unit. In terms of governance, it can help in terms of data residency, for example.
a particular business unit might, prevent data export outside the EU.
Or you can also have role-based access control based on a business unit membership. Then operationally as well, it will become easier for reporting SLOs, or why is a particular business unit going down, that sense.
So here's the repose specification, servicetrustbusinessnoop.id. It should be a string, I have included some examples as well.
Do you have any questions? Anyone have any questions?
in the GitHub issue that I had.
created for this. I could see one comment from Thompson. I will respond to this on GitHub, but mostly I think it is about whether we should include this in service.owner or service.instance.support instead. I kind of feel like service.owner should be related to the ownership of the code, rather than the business or financial aspects of it.
Service.instance.support also doesn't sound very good for including business in it, because it is related to support for that instance, so… I feel… I still strongly feel to introduce this as a different attribute. Please feel free to pitch in if you disagree or agree.
Any thoughts?
**Josh Suereth** 08:39 Yeah, I responded to, James. I think, like, this is a question we asked ourselves as well, like, his question. It's just, we asked it, like, I don't know, 3, 4 weeks ago? But the… and for all the reasons you say, I think having an owner Is a bit generic.
And it's hard to know what that ownership means. A business unit and, like, a team are kind of different.
And I think that it makes sense for us to have cost center, might be different than business unit, might be different than team, for… especially in large companies like ours.
But… I think having those, those three things makes sense, and for owner, we still need to… there's still an open question, like, there's a PR for us to review about ServiceNet Owner, where we need to refine the description. So, as we progress here, you know.
we added cost center, we're adding business unit. We need to figure out what owner really means, and yeah, I don't know if it's the team that owns the code, or the team that owns the service. Like, if you're in an SRE, you know, DevOps-y thing.
you know, should it be the folks who are actually managing that service in Kubernetes? If that's… if that… yeah. I want to get a good definition for that. I don't think it blocks what you're proposing here, though, because I do think they're orthogonal.
That was, like, my primary point. Second point is, Is there a relationship between… Business unit and cost center and owner that we need to track.
Or we're just gonna… again, this is what we do in entities today for OTEL, is just the fact that they would be in the same bundle of data would tell you they're related in some fashion.
**Ankit (Google)** 10:28 Right. Thank you for sharing your thoughts, Josh. I definitely agree with the first one. We definitely need a more heartbound definition for the owner side of things.
on that part, like, I'm not sure if SRE and devs should be considered different in that sense, because usually there would be some, relation between the two of them anyways. I'm not sure if you can control it at this level.
Coming to the second point.
differentiating between cost center business in it and owner. I mean, the usages do exist across platform for all these.
So… Of course, there is a relationship, but overall, all three of them serve a different purpose.
So it would make sense to have different attributes for them.
I mean, I don't know, how would I go tell someone, like, use business unit instead of cost center, for example?
**Ayushi Asthana** 11:38 I, I think that… that would become… A primary… concern or question down the line, though. Because, I mean, I understand that all three of them might be used interchangeably when it comes down to implementation and usage by, organizations, but we want to have, like, a very hard line, or at least a clear line between the three of them. Like, what at least we mean in ODEL, what are the semantics for these three attributes?
In terms of usage, though, it… I mean, I see that as becoming a thing where they might be used interchangeably. So that is why the guidelines need to be very crisp and clear on what each of these attributes mean, and how it's intended to be used.
safe.
**Ankit (Google)** 12:33 Right, I agree with that, Aisha, yeah.
**Josh Suereth** 12:37 So, one… one other suggestion here, because we've been… we've been doing this more. I think this is a good survey of existing use cases.
what would… an open telemetry implementation look like and do, right? Like, so if we were to say we add business unit I think if you scroll down… you call out… you call out where it's used and how people are tagging it today, and, you know, annotating telemetry. Is there… is there, like, a demo we'd put together, or a block of code where we could, like, show, here is business unit in action, you know, and what does that… what does that look like?
Yeah, so this is here where you're talking about how people make use of it and the kind of graphs they have. Should we have, like, an example graph of that same sort in… in, the OpenTelemetry demo? Like, what… What's a good output of this work?
**Ankit (Google)** 13:40 Right, yeah, I think we can do that. I'll take Ayushi's help, as she's more well-versed, with the open television.
And I think you can come back with a demo in that case. What do you think I should be?
**Ayushi Asthana** 13:59 We definitely would, want a demo to showcase directly how this would be used, so yeah, we can work on that. I've taken a note of it, and maybe we can work on it.
In the next week, and see if we can come up with a good use case in Notre.
Yep.
**Josh Suereth** 14:21 I do want to open up to other folks who are here to see if they have any… I mean, it's mostly… it shouldn't just be Google talking to Google. I'm just curious what other… what other folks are thinking.
**Anthony Mirabella** 14:30 I'm kind of still trying to wrap my head around the service owner or service instance support kind of distinction. It seems like those are describing teams that have an ownership responsibility or a support responsibility.
And business unit would be a good attribute of a team that has such responsibilities.
It… that seems to make more sense to me than business unit being an attribute of the service itself.
**neil yashinsky** 15:01 Yeah, I… just to answer your question, Josh, I mean, I forgot who… that was a good point, what they made. It's… it's… it's somewhat pers… What's it… what's the word I'm looking for, sorry, Relational, it's a, it's a, like, what's the Einstein thing? It's relative. It's relative to what we're saying, because as someone who's consumed a lot of Google services, you know, I certainly see the point of this and the use of this, and sorry, the last speaker kind of posed an interesting question, which I… I'm here for the discussion more than the answers, like.
Is this… service owned by a business unit, or does the business unit own the service? It's, you know, and it's, it's, it's whatever it is, your perspective is, of course, I think. But back to this specifically, I feel like… In the operator context, a service is owned by… business unit. Like, that's the natural relationship, especially if we're talking from a costing perspective, rather than having, you know, a… Sir, you know, a business unit belonged to a service.
I thought, if that was the part of the question.
**Josh Suereth** 16:19 So if I can rephrase this, it… and I think, Anthony, thank you for raising that, like, maybe this makes sense that we figure out service owner first.
And that business unit is a aspect of the owner.
Right, so it'd be like, you would represent the service owner, and then inside of the service owner, you can tag the owner with the business unit. Is that… that's the feedback from both Neil and Anthony, right?
**neil yashinsky** 16:45 Yeah, you said it much better than I did, but yes.
**Anthony Mirabella** 16:48 Yeah, that kind of aligns with… How service owner would read to me is a property of the owner would be what business unit it's in.
**Ankit (Google)** 17:07 Josh, would that open the question again for call center as well?
IPL… I think along the same lines for cost.
**Josh Suereth** 17:22 I don't know if my internet's bad or not, but that broke up for me. I couldn't actually.
**neil yashinsky** 17:27 Same.
**Anthony Mirabella** 17:28 Yeah, it sounded like he was asking whether that reopens the question of cost center, and if cost.
**Ankit (Google)** 17:35 included.
**Ayushi Asthana** 17:38 Yeah.
I think Ankit's breaking up.
But, yeah, I, I think, I think, Ankit, can you, can you.
**Ankit (Google)** 17:52 Am I audible now?
**Ayushi Asthana** 17:55 Better, yes.
**Ankit (Google)** 17:57 Yeah, I was saying that would open the question along the same lines for cost center as well. Should we include that as well in Owner?
Instead of having a different one.
Because if we are including business unit inside owner, then probably cost center would make sense inside owner as well.
I think the thing I'll pull out…
**Josh Suereth** 18:18 Yeah, the thing I'll call out, it's a good question. In practice, It's… it's… Big companies do stupid things.
So, like… You would think that there would be a clear tie between an owner and a cost center.
you would think there'd be a clear… and I actually want to find out if this is true for Owner to business unit as well.
But there are times where that is not true. I think it's a simple model, and it's decent for us to look into and investigate it. For cost center specifically, man, there's shenanigans that go on, right? Where, like, one team could actually have multiple things that are paying for their stuff.
or you might actually be running a SaaS-type service, where you're dividing things in weird ways. So, I've seen a lot of crazy things that make me think that, The owner and the cost center might need to be divided, because it could be the ownership changes, but the cost center does not.
of a particular component, I've seen that a lot.
Which is weird, but yes.
So… from my perspective, I think it's fine for cost… like, I think the decisions we made in cost center.
Are independent of the decisions we're gonna make about business unit.
Right? I think we can use them as a reference.
But I don't think they're exactly the same. And I am inclined with Anthony and Neil about maybe… maybe… You know, we'd have to really think if there is a divide between owner and business unit.
**Ayushi Asthana** 19:57 And to add to Josh's point about cost center, there is often use cases with services that serve as a platform, where they derive Or attribute cost center to specific I mean, I've seen them wanting to do cost allocation by their customers also. So, it's possible for platform, especially services that serve as a platform for other entities to want to keep this attached to the service itself, so that they can control, the entity or the service instances that are assigned to different… while the owner of the service is, like, the same, the cost center could be different based on deployments, so that… that is, like, a use case that Businesses might have.
So that is, like, another point Dubai cost center might… not belong in owner.
So, yeah.
My two cents on that matter.
**Ankit (Google)** 21:06 Awesome, I think that clearly concludes the decision on why we should not touch call center and keep moving as it is, so we can just discuss, further on business unit once we have more data points on how it relates to owner.
We can take that AI.
**neil yashinsky** 21:22 Yeah, it's a really good discussion, and I think, this is, what's the word I want to say? There's two separate perspectives on this that I think are well represented in OTEL. There's, like, you know, the cloud service providers, if you will, and then certainly the… telemetry observability companies, because they… they need to, like, shift the pricing responsibility for the services people are consuming, which is slightly different, but I… I… I'm really curious to see, actually, how our kind of business abstraction grows from hotel.
Or not, I guess. Because it sounds like you're specifically trying to accomplish one thing, which is like, hey, who do we charge for this service running? But also, there's like, hey, this thing went down, who owns it, you know? Who's responsible for it? Which I think is a separate… property or whatever than that we're discussing here, but I guess you could use them the same way if you… Talk to.
**Ayushi Asthana** 22:24 Yep. Yep.
Ulf, I think, then, now we can discuss the… data entity proposal. So there were two points last time we talked. Let me just share my screen first.
Right.
Okay, so there were two points last time that we discussed this. One was, what do we call this entity? Should it be data or data source?
There were, like, I, I… Sort of align with… data source, why this should be called data source. Data in itself is quite abstract.
And instrumentation that I've proposed right now, it sort of aligns with that, so I will talk about the instrumentation first, and then maybe we can conclude on naming, so that we can have a formal proposal in the SEMCON.
Oh.
So, yeah. Here, in the instrumentation considerations last time we talked, the concern was how does this entity or this attribute flow through the pipeline, or flow through infrastructure. And the use cases that were proposed sort of look like, wanting to do, maybe, like.
auditing on this attribute, controlling data access based on data sensitivity that's defined, wanting to do some data categorization and controlling data storage, right? So all these… all of these, basically use cases were proposed.
And so, one of the possibilities for this attribute to be propagated throughout the infrastructure was through the context baggage.
So, basically, what will happen is we will tag the data source.
With either data category or data sensitivity.
And all of the services that connect to this source will consume this attribute from the datastore itself, and propagate it in its context.
And so, wherever the data flows from being consumed here, it will carry the context of sensitivity or category. And so, some of the use cases from this being stored in the baggage context is… context baggages. For example.
in ingest, where if we detect any data-sensitive, high data sensitivity, payload, we automatically hash. For example, in API gateways, where we can control egress.
or in auditing, where we can control compliance use cases, right? So this was one of the proposals that I could think of for how this instrumentation for this specific attribute would look like.
I am trying to work up a demo as well that we might be able to review in the next meeting.
But this, this is basically the proposal, so I'd like to hear thoughts from the group.
On what, what, do you think?
**Trask Stalnaker** 26:01 As far as using baggage, do you intentionally want it to propagate Downstream… to downstream services?
**Ayushi Asthana** 26:12 That is a call that I keep… I think those users can make.
When they use this attribute, or when they integrate with this attribute, but the full extent of having, like, a… security-aware infra, or cargo-aware infrastructure would be if they propagated. So, like, They can choose not to.
And only tag their data stores, and have some benefits from tagging the data store with sensitivity and having a category for it.
But if they choose to propagate it via context baggage, they can do a lot more with, you know.
having more secure measures, having more stringent network protocols, for auditing purposes, etc. So, this is, like, one of the possibilities that is out there, if we have this attribute, and if we choose to, you know, have it in context package.
**Trask Stalnaker** 27:20 I see, so the… the proposal… the proposal isn't necessarily tied to baggage or anything, it's just that it would be user… Choice to, where they put it and how they propagate it.
Yeah. Makes sense. Thanks.
**neil yashinsky** 27:42 Yeah, no, I think this is smart, and I think that there's a need for this, you know, how it gets adopted, I think, is always kind of the to-be-determined, But I've seen this requirement a bunch of times, and actually the one thing that I was wondering about, Aishi is, for Table 4, and maybe this is, said somewhere else, so forgive me if I'm, you know, repeating something you've already said, but, like, I actually think the first thing, the first impact should be, like, don't ingest this data point.
Rather than hash it or encrypt it or whatever.
**Ayushi Asthana** 28:15 Yeah. And… I think that's a valid point, and that will be an implementation choice that.
**neil yashinsky** 28:23 Right, okay.
**Ayushi Asthana** 28:23 So we'll be able to make if they have this data, that they will be able to block ingesting this data, they will be able to block storing this data in auxiliary storages, caches, memory, etc, right?
**neil yashinsky** 28:38 Right.
Great, thanks.
**Ayushi Asthana** 28:45 Okay, I think I have posted this, proposal in the chat already.
If we can conclude on what entity we want to propose exactly, is it going to be data or data source? I can whip up a formal proposal, and then we can start working on it, creating a demo, getting buy-in from maybe the entity SIG on this.
Oh.
Any, any thoughts on that?
**Josh Suereth** 29:20 Yeah, I… I like to… I want to make sure when you make the proposal to make sure you include this use case, because I think, again, getting people to understand why is actually important.
In terms of data versus data source, initially, I was thinking, you know, when we… when we say it out loud, data source actually feels a little bit better, of saying, like, the source of this data was sensitive. It is more verbose, and if you're sending it over baggage.
That's exciting.
So, I do want to take a little bit of time to think about the baggage thing. I don't know if I'm going to have any answers, but just things that we send over baggage, we want to be a little sensitive to the size and length of them.
Since that's in the hot path on the data plane, and it causes overhead everywhere.
But, that said, I think for OTEL SEMComp, like.
just from my perspective of what you're talking about, what we're seeing here, data source seems to make more sense. It's interesting, though, because you're tagging almost the… with the baggage thing, it's kind of cool, you're tagging the payload of a response and saying, hey, this has sensitive data, make sure you handle it appropriately.
**Ayushi Asthana** 30:36 Right. I think… I think it… it was a powerful use case to talk about, and it showcases… so we can tag data, and it also has some cool consequences, but this is… I felt like this will be very powerful to be able to do, to tag your payloads and control who sees what.
In fact, you can control services from serving it, if they don't have the clearance, so something like that is also possible. So I… I think this… this will make for a very good demo if I'm able to pull it off, so I'll try my best.
**neil yashinsky** 31:16 Have you pondered, like, a hierarchy of, like, the top one would be something like resources, and then one of the children could be data, one of the children could be data sources, one of the children could be… some other valid example that escapes my mind. I don't want to overcomplicate it, but I… I feel like there is a lot of value, as Josh was highlighting, like, the data source is something that's… has sensitivity as well as the, you know, the data that comes from that source. And if, you know, maybe that's boiling the ocean, and maybe it's just better to start with the data first and see how that works. So, I was just… not a specific suggestion, just, like, a thought I thought would be worth… Sharing aloud.
**Anthony Mirabella** 32:01 Yeah, I was kind of wondering the same thing. It seems like sensitivity and category can apply to both a data source and data that's actually being moved.
And perhaps some of your telemetry is about interactions with a data source that has some certain category and sensitivity, but some of your telemetry, and where baggage would come in, I think, most appropriately is When the data you're actually moving that that baggage is attached to has a sensitivity and a category that needs to be respected.
**neil yashinsky** 32:35 Yeah.
Both are valid, neither is wrong, or whatever, you know, good places to start. Both are good places to start.
**Ayushi Asthana** 32:43 Yeah, that's an interesting thought, actually. I was, thinking very binary, it's going to be either data or data source, but now that you've said it.
I'm just thinking if… Like, both of them have their utility, and at some point in the future, we're seeing both of them existing in hotel, and so… Maybe we could think along those lines as well.
**neil yashinsky** 33:06 Yeah, cause I feel like… Oh, sorry, I was just gonna say, I feel like there's probably A-to-A, like, agent-to-agent, implications of this as well.
But, again, not to boil the ocean, but just, like, consider how… The downstream consumers of this might…
**Ayushi Asthana** 33:23 Relate to the data.
Right, right.
I think for starters, Josh, what do you think about this, since you had proposed data source initially? What do you think if we propose it as data entity and see what the response from the group is about these use cases?
And if we see people, like, leaning towards having it as data source instead of data.
What do you say to that?
**Josh Suereth** 33:55 Yeah, I'm fine starting with that, particularly with this baggage use case. Like, I think, you know, to ground everything, if we pick what we think is the number… you know, the key, like, usage that we want to go after, the key things we're unlocking, and we ground against that. Let's target that. It just helps semantic conventions run much smoother if it's like, cool, here's a thing we're trying to build and do.
So, given, given what you're showing as this… this demo, if this is the thing we're targeting, yeah, I think let's start with data, and let's… let's go from there.
**Ayushi Asthana** 34:30 Cool, cool, got it. Okay.
**Trask Stalnaker** 34:33 Have you… sorry, I had a question. Have you… thought about… I mean, data seems… Very, generic, For hotel, like, what, Have you… what about just being, I mean, sensitivity as… the top level… I mean, you're essentially stamping that telemetry record with some… sensitivity… thing. I mean, it kind of gets back to the data source versus data, but I guess I'm viewing it as what really matters is the telemetry that's being captured is sensitive.
**Ayushi Asthana** 35:25 So, the only con… sort of… I think the problem, or rather concern that I see with that popping up is There's no, like, control that we'd have over who dictates sensitivity. Then everybody's dictating sensitivity for themselves, and then, what is treated as sensitive, and how do, for example, services Infer sensitivity.
And how do, for example, observability platforms infer sensitivity? There is then no centralized meaning of what is sensitive. Is it sensitive to view? Is it sensitive to transfer?
Services are setting sensitivity for And we also have, like, the criticality attribute in service at this point, which… I… I don't know. If we are talking about sensitivity, is it either service sensitivity, or is it… like, the data that the service is handling, and that is sensitive. So it kind of boils down to data, right?
Right. So, it boils down to the telemetry that you're sending.
**Trask Stalnaker** 36:49 That you're ingesting, right?
Is my understanding.
Or do you want to distinguish those two things? One is… The platform is sensitive.
The data source is sensitive, the other is that the telemetry is sensitive.
**Ayushi Asthana** 37:08 Oh… So, what, what would make a telemetry sensitive?
like, I would probably pose that question.
What would make a telemetry or a signal sensitive?
**Josh Suereth** 37:26 I'll jump in, and I think, Trask, the answer to your question is this is about the data itself, not the telemetry.
Like, this proposal.
And so.
Yeah, this is more about tagging, like, hey, this… this database has sensitive data in it. And then, if we tag the observ… so, the baggage thing is interesting, because that has non-observability CUJs all over it, right? Like, but, if you know that the data… the data source was sensitive, like where I got the data, or the data that I'm transmitting, then I can actually take action on the telemetry, because the telemetry may also be sensitive. But that's like a, like a poisoning, or a.
**Trask Stalnaker** 38:10 I see.
**Josh Suereth** 38:11 Okay, okay. Yeah.
Now, correct me if I'm wrong, Ayushi, because I, you know, I'm not in the weeds here, so I'm talking from, like, a 10,000-foot level.
**Ayushi Asthana** 38:23 No, no, I think… I think you helped me understand that as well. I… I was misunderstanding the question, and now, now I understand. Yes, you're… you're absolutely right. So, this is basically inferring if, inferring it from the data that is being handled by services and by networks. So yeah, we're basically going to be tagging data that is being handled.
**Trask Stalnaker** 38:48 And so this is different than, like, service sensitivity?
**Ayushi Asthana** 38:55 Yes, and to that, I think service criticality will serve the same purpose, right? Or are… I mean, if we are calling a service, like, sensitive, we might be calling… ultimately saying that the data that this service is handling is sensitive.
Right?
trust?
**Trask Stalnaker** 39:19 I mean, I can see criticality being a, kind of… some overlap, but, I mean, orthogonal to the sensitivity question. I guess, so, what I was trying to understand is the, How do you… so you would be, like, you have a service, And… It might not be… you don't care that the service itself is sensitive, like… I guess I'm trying to see why… why wouldn't you just tag that service as sensitive?
Like, that it has sensitive data flowing through it.
**Ayushi Asthana** 40:00 Right.
But that would, like, label a whole service as sensitive, while it might be serving, you know, multiple endpoints that have multiple purposes, and not all the data that's flowing through that service is, in fact, sensitive.
So that, that'.
**Trask Stalnaker** 40:19 I see, so certain endpoints.
May be sensitive, like a login endpoint.
**Ayushi Asthana** 40:28 Right?
Right? Or something that just sort of discloses some, Restricted attributes to the user, for example.
some personal information or something, right? And only that aspect of that service is sensitive. But other than that, you are just seeing your preferences and stuff, and it's just, like, fine, you can view it.
So there is, there is also that.
**Anthony Mirabella** 40:56 But if it only applies to some of the telemetry that's coming out of the service, because, say, it only applies to a login endpoint, or something like that, then it doesn't seem to fit into an entity or a resource, right?
Would that then be more…
**Ayushi Asthana** 41:11 Like, in metrics, a data point attribute, or a log record attribute.
It does tie back to the data source itself, right? You can… you would be… so this… the way I sort of see this playing out is, people going ahead and tagging their, buckets and DBs as and propagating data.sensitivity or data.category at that point, and not at the service service Can sort of infer it from the data it receives from these endpoints.
But not all of the service will have, or all of the telemetry that the service generates will have these attributes, or this specific label, so to speak.
**Anthony Mirabella** 42:04 I guess maybe my mental model might be a little bit behind, because I'm… haven't had a lot of experience with entities. I'm still thinking of resource attributes as a fixed set of attributes you create at startup doesn't change over the lifetime of the SDK. And it seems like if these attributes, though, would only apply to some subset of The operations that a service performs, and thus only get added to telemetry that's coming out of those operations.
resource and entity don't really seem like a good fit. Am I missing something there?
**Ayushi Asthana** 42:36 I, I think my.
**Josh Suereth** 42:38 I can respond tremendously. So, first of all, We have an open question of whether or not an entity shows up in non-resource-related things, but that's… let's put that aside. Your notion of resource is correct, but I also think if you look at what this is, this is a persistent volume, right? So if the service is using that persistent volume, I guess the question would be, should I always be annotating the service with these labels?
Because I'm using that persistent volume. Like, is this a tainting, poisoning kind of relationship, where if I have something that's labeled as sensitive, I… you know, attach with that. I think… I think that there's an aspect of this that is with the sensitive thing. With the baggage, where it starts flowing through service to service, that's where it would no longer be on resource. That's where, like, the request itself is now saying, hey, this thing is dealing with… with, sensitive data.
And unless somebody actively says, cool.
I have removed the sensitive data, I'm gonna remove that bit and pass it on, the whole system can know I'm dealing with sensitive data, I need to take whatever controls I need here. So, I think there's two aspects to this, Anthony, and the one I can see being attached to resource. I also think we should talk about the entity thing. You might not need an entity we might just do this as straight-up annotations and attribute groups. We don't have those modeled well in SEMCOMP. We actually… we have had lots of discussions about what they are, when to use them, when you have a good… like, when is something a signal? When is something just a group of tags, and what the hell does a group of tags mean?
How does it attach, where does it attach, all that kind of stuff. You might be a use case of that thing that we don't have well defined, and in which case you can use what we call an attribute group to define all these, and you do not need a signal, because you're just attaching to other places.
That is… we're running out of time, so I think that's a can of worms we need to open and discuss.
I think, from… just to answer some of that question, Anthony, you're right. There's a piece of this that I don't think ties to resource. There's a piece, when I look at the Kubernetes example, that I think does.
And I want to confirm that, yeah.
**neil yashinsky** 44:56 Yeah.
**Anthony Mirabella** 44:56 Yeah, and I think that also helps feed into the data source distinction as well, because it seems to line up pretty smoothly with that. The one question I would ask that we probably need to consider in the future is, does there need to be more than one data source classification… classification category bit that could be attached, because if you've got multiple data sources, and one's restricted and one's public.
How do you communicate that?
**Josh Suereth** 45:23 Or do we collapse them into, you know, worst wins, right?
**Anthony Mirabella** 45:28 Right, maybe there needs to be a total ordering, and whatever is the highest value gets attached. But categorization isn't really comparable like that. Categorization seems like tags that you have to be able to support multiple of.
**neil yashinsky** 45:42 I'm excited to see the demo, if you… when you get around to building it, because I think in some ways that'll be very clarifying, too, Ayushi's, like, you know, how did it… turn out for this use case that you were trying to do, and that'll be a great way, I think, to expose the surface of the other areas of, well, complexity or management or whatnot. And how does… I think… I think the other question is, how does it… how does that fit into your overall… for lack of a better word, like, CICD pipeline, where is this getting populated would be an interesting question to see in practice, not just in theory.
**Ayushi Asthana** 46:12 Right.
Also, I've noted the discussion that we were just having about entities versus attribute groups. I am not well aware of what their definitions need to be in OTEL, so maybe I will also read up a little more about it and have some More concrete thoughts about that, the next time we discuss on this.
But I think we are out of time.
So I'll stop sharing.
Thanks, everyone, for joining. This was a good discussion.
**Trask Stalnaker** 46:45 Sushi.
**neil yashinsky** 46:46 Yeah, thanks, Ayushi, thanks so much.
Thank you.
