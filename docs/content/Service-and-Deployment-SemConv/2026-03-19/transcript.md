SIG: Service and Deployment SemConv
Date: 2026-03-19
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Ayushi Asthana** 03:03 Hello. Hi, Yoshi.
**Yoshi** 03:05 iOS.
How are you?
**Ayushi Asthana** 03:09 I'm good. How are you doing?
**Yoshi** 03:11 Doing good. I'm not taking the PTO today.
**Ayushi Asthana** 03:16 Oh, shit.
**Yoshi** 03:18 Yeah.
**Yeah, I left AWS last week, so… Ayushi Asthana** 03:24 on your PTO?
**Yoshi** 03:26 What, what? Sorry?
**Ayushi Asthana** 03:28 Yeah, I was saying you're on a call on your PTO, and you should be enjoying your time off today, isn't it?
**Yoshi** 03:34 It's fine, it's fine. Anyway, I need to pick up my kid at, 3 o'clock, so… I had to be at home, and then I was just reading the draft of my… own book.
So… Yeah, it's fine.
**Ayushi Asthana** 03:51 Girl.
**Yoshi** 03:52 Anyway, I had a, I had a question regarding the, the data, data entity.
Draft off. Right.
Of yours, so… I wanted to talk to you, so… that's fine.
**Ayushi Asthana** 04:04 Yeah.
Sure, sure, let's discuss that, yeah.
Let… should I share my screen?
Let me do that.
**Yoshi** 04:13 Yes, please. Yes, please.
**Ayushi Asthana** 04:15 Just open up the dog, share the screen.
Bye.
Right. Yes.
Yeah, so which, which section specifically did you want to talk about?
**Yoshi** 04:35 So, as, as you commented, on the dock, I was wondering if the name of the entity data itself is… Appropriate or not.
**Ayushi Asthana** 04:52 Right, yes, I think we discussed that last time around, about data versus data source as well.
Right, so there were two, two schools of thought on that. First one was, you know, are we tagging the data source, or are we tagging the cargo that's flowing through?
the services and the pipeline, right? So, one of the, instrumentation proposals that I had was, around, basically, tagging the data that's flowing through the pipeline using context baggage, right?
And if we consider this specific use case, we are not actually tagging the data source, we are tagging the data that flows through the pipeline, right? So I think data source in and of itself can have certain properties, right? For example, I think… Location, maybe, or… persistence… I mean, properties that are more, more aligned to what databases are, in terms of, like, for data source, but data… defines the cargo that we have, the data, actual data that's flowing through the pipeline. So, those were basically the two ideas that we discussed.
And so, the general consensus at that point was, let's start with proposing data.
and then see what the community thinks about data versus data source. But, this specific one, for… security-aware mapping and for, you know, tagging data in context bags, these two use cases specifically are more aligned with data as an entity than data source.
**Yoshi** 06:57 Okay, I see.
**Ayushi Asthana** 07:03 So, I would love to hear your thoughts on that. What do you think about, data versus data source, or if you have any, Good arguments that can make a faith for one or the other.
**Yoshi** 07:15 So, is the, data source on the… Alternative candidates for the entity, or has anyone Raised any other possible candidates for the name?
Of this entity.
**Ayushi Asthana** 07:31 Except… Yoshi 07:32 Such as data… data characteristics, or the data attributes, or… anything. Data, like, I don't know, but data sounded… kind of… Too generic to me.
And then, I was wondering… F… Like, there were… there were any other possible… Candidate for the name.
**Ayushi Asthana** 07:54 Yeah, so, there was one other, discussion that we had was around… Entities versus data group, attribute groups.
Also, the question of whether data belongs in a separate entity, or as an attribute group in SEMCON.
Which I felt like was a good point, because… data feels like a logical entity. I think that's where you're also coming from. Data feels like a logical entity.
That we are describing. So, does it make more sense to have it as an attribute group? And then data source can be an entity, much like a service.
So, there was also that, and I was reading about attribute groups yesterday, because I… I honestly do not have a lot of context around when we decide one over the other, right? So, I was just reading up about attribute groups yesterday, and… I will probably extend this document to make an argument.
For whether there should be an attribute group.
or an entity. But I see where you're coming from, where data aligns more, maybe, to an attribute group than an entity, because an entity directly maps to a resource in OTEL, as far as I understand it right now.
And so we want data to align to a resource if we propose it as an entity, but right now it does not.
And so, maybe data makes more sense as an attribute group.
And… Nice.
data source can probably be an entity. Probably, like, and that is… that is where, basically, my head is at right now. So… This is… this is what my current thoughts are. I'd probably put them on paper over here and make it more formal, more articulate, but this is… this is the direction that I'm going in, right now.
So, do you have any thoughts about, like, putting data into… as and into attribute groups that are defined in CENCON?
I don't think it exists right now, there is no data attribute group.
**Yoshi** 10:14 Huh.
**Ayushi Asthana** 10:16 So… Yeah, I'd love to hear your thoughts on that specific, argument as well. I think I have it on.
**Yoshi** 10:24 Yeah, data, data, the, the name, data… Reminds me really broad, like, broad… Namespace for the metadata of, That defines the multiple attributes of the specific data points.
So… Yeah, I was just wondering, Because this label, or this entity, just holds the, Some… some… a couple of important… important attributes for the data, regarding the security and the compliance things, I suppose. So the… the… so the net… so the number of the attributes that this data entity holds would be not that much, right? Not more than like, 5 or 6. Like, at most, it's… the number would be, like, handful of… attributes, so… I was… I was just wondering, like, like.
You know, the data, the naming data.
Sounds too generous.
Yeah, it's just my… just the impression, and not… not from the logical… Like, logical thoughts, so… you know, if everyone else would be okay to have this name, I mean, data for this entity, then that would be fine.
**Ayushi Asthana** 11:58 Yeah, I mean, that's the point of contention, at least, that we closed at, right, last time around in the discussion, was, should it be an entity, or should it be an attribute group? Because… I think… Anthony raised this, or somebody else in the meeting, I don't recall at this point, but somebody raised this point where, we… Entity should map to a resource in the infrastructure that is emitting this metric.
And if we just talk about data, or if we look at the logical, you know, meaning of what we are proposing.
In terms of sensitivity and category, right? These, these two attributes, data category and data sensitivity. We understand that these directly correlate to the cargo, or the data that is flowing through the pipeline.
But data of itself is not a resource. In… it's basically, like, a logical entity that anybody in the pipeline can emit. So, for example, a data might become sensitive after processing. A data might become less sensitive after a service processes it and passes it on after encryption or hashing or redaction or anything, right? So, it's possible for different entities in the infrastructure to emit different sensitivities.
Sort of, sort of like that, right? And, so… which, which made sense to me.
That, okay, this, this looks like something that That seems useful.
So I am leaning towards not proposing this as an entity, and rather proposing this as an attribute group.
As of right now.
So, maybe, maybe I'll rewrite the proposal a little bit, and instead of saying we should introduce this as an entity, maybe we can introduce this as an attribute group. But I agree to your point that probably this attribute group won't have, like, a lot of things.
That we can see, right now.
But, yeah, that's… that's where I'm at. From the entity standpoint, I align with you that it's too generic.
**like, just data.category. As an entity, data is too generic, and probably, as an entity, data source makes more sense. But we don't have a proposal for data source either, just… Yoshi** 14:45 Yeah, yeah, I think, I think these labels as, like, standards.
Attribute set.
would be, would be, would be great. So, yeah, having, having the attribute itself is fine, totally fine to me.
And also the things I wanted to know is that, is there any… conversation, regarding how the backend services utilize these these labels, in a consistent way.
As far as I read the document.
The recommended values are just a kind of recommendation, and it's not the… It's just, like… It's a freeform string value.
slot.
**Ayushi Asthana** 15:35 Hmm.
**Yoshi** 15:36 And then… If, for example, if the user… Puts these labels, like, these attributes into the metrics or anything, then… And then if they'd like to switch Switch their backend from one to another.
Then, and then… If the… like, those backlins don't… Don't, like, treat this attribute in a consistent way.
Then, there will be trouble.
Need to, like… The user needs to… need to change all the meta, like, attribute values.
Based on the backend. So, it would be great if he can Provide some guidance for… for these attributes for the backend services, like, such as, like, Datadog or anyone.
**Ayushi Asthana** 16:37 Okay, so I think we can go about it two ways, right? Either we can recommend some.
**Yoshi** 16:43 this time.
**Ayushi Asthana** 16:44 values, or have an enum… I think how enums generally work in SEMCON, where we provide an enum, which is, like, some standard set of values that you can generate, and then extend it if you want to. So, I think.
**Yoshi** 17:01 Yeah, for example, the… yeah, the example, for example, the example value, PII would be really, like, a good example. So if, say, for example, if the… if the telemetry data… contains holes that… that disattribute with the PII value, then… That'd be great if the backend services can suggest to users, hey, this data includes this this attribute with this PII value, so I… do I have to, like, do I need to… Mask all the data.
For, for, like, for future… ingestions, for example. So that's such, that's kind of… so if the, the, the, all the… the background services can treat this as a… in a consistent way, that would be great. So, yeah, As a standardization organization, it'd be great if we can, like, Navigate the background services to… Like, like, like, suggest… what to follow for the backend services.
**Ayushi Asthana** 18:24 For sensitivity, I think it would be easier for us to, like, say, this is what you can use, but, for categories specifically, Is there… A generally known vocabulary that's used across industry, or should the data.category attribute be freeform string?
**Yoshi** 18:48 Yeah, I am not familiar with the security standards, but for example, in the case of the logs, we have… We have a standardized log-level guidance.
Like, in RFC, for example. Let me see, log level RFC.
So RSC… 5424 is the standard for the log level.
And then that defines the… The importance of the… Each labels, based on the use cases.
So, it'll be great if you can have similar categorization for each body of, data.
Data.what? Data.sensitivity.
**Ayushi Asthana** 19:40 Okay, for data.sensitivity specifically, right, this.
**Yoshi** 19:44 Yeah, yeah.
**Ayushi Asthana** 19:46 Okay.
I have added… I think this is the doc you're referring to, right? The syslog protocol?
**Yoshi** 19:55 This is, yeah, this is… Ayushi Asthana 19:58 you just shared. Was this… Yoshi 20:01 Yes, yes, yes, so your commenter is right. I'm reading your comments, yeah, that's the point I wanted to say.
**Ayushi Asthana** 20:09 Okay, got it. I think that I have taken a note.
We can… I think that's a good point. We can standardize at least this specific attribute.
It makes sense to have more… You know?
Well-known values over here.
**Yoshi** 20:29 Hmm.
**Ayushi Asthana** 20:30 Okay, that makes sense.
**Yoshi** 20:32 Yeah, I'm not a professional of security-related data.
So, maybe she… maybe some security services, such as Splunk or Wiz, people should know more about it, so… Yeah, if he can… it would be great, if he can involve… These kind of people.
**Ayushi Asthana** 20:58 Yeah, I think, I think I, I have a few folks that I used to work with, in… in the security space, security red teaming space, so I… I could reach out to them and get a sense of what… what, they feel about this pool, I think I hear the… hate that. I have noted it down, so we can look into that.
Apart from this, so, any other, any other feedback, Yoshi, around, data?
**Yoshi** 21:38 No, no, I assume there will be other updates on this document, but the overall direction of the suggestion?
Is… is… sounds… sounds good to me.
So… I don't have any other objections or not.
**Ayushi Asthana** 21:56 I think one last thing that I want to confirm before I start the rewrite is, I think, are you aligned with the attribute group direction rather than the entity direction for this? Does that make, more sense logically for data to be existing?
**Yoshi** 22:13 Yeah, I'm leaning towards the, data attribute sets.
Option. Yeah.
**Ayushi Asthana** 22:19 Cool, cool, perfect.
And then we have… And then the two groups are at least soft-aligned on some of the items, and we can start working.
I think this is all I had for today. There's one other thing that was covered last week that I think you can provide your inputs on.
**Yoshi** 22:59 Are you online?
**Yoshi** 23:18 Hi, Aish.
Can you hear me?
-Oh.
Aish… You sh… Oh, you're sh- Alright.
Gosh.
Shtana.
your own life.
Hi, Ayush, can you hear me?
Hello!
**Ayushi Asthana** 25:05 Okay, sorry, there was a random power cut over here.
**Yoshi** 25:08 Oh, that's unfortunate.
**Ayushi Asthana** 25:11 Yeah, yeah, I was just about to discuss, about this business unit proposal.
**Yoshi** 25:18 Yeah, business unit, right? Yeah, yeah. Yeah, yeah.
**Ayushi Asthana** 25:21 So, I think there was some discussion last week about whether we want it to be in service, or does it make more sense for this to be as a subgroup, sub-attribute of owner?
Because, I think we have service.costcenter right now.
I know.
We… yeah.
Does it represent… does it represent the owner?
General was that business unit belongs to who owns the service, so owner.businessUnit was one of the proposals that came up that we should be sure.
**Yoshi** 26:13 Oh… Ayushi Asthana 26:14 unit as a sub-attribute of uma.
**Yoshi** 26:17 In that case, in that case, what kind of sum attributes does the owner attribute has?
**Ayushi Asthana** 26:25 So I think… Aww, and I… Yoshi 26:29 Is it, is it written on, in, on a, on a PR?
**Ayushi Asthana** 26:33 Yeah, yeah. Una… Yoshi 26:34 Oh, shit.
**Ayushi Asthana** 26:35 Also, like, service.owner is also currently proposed.
**Yoshi** 26:41 Right? Oh, okay.
**Ayushi Asthana** 26:42 The lot owner has, like, name, URL, contact.
And we're proposing that owners should also have business units.
**Yoshi** 26:53 Tom… So, service.oner.businessUnit, or service, I, I'm not sure, because this, this attribute is only relevant to the large company or large organization.
Because the small, smaller company In the case of a smaller company, the owner and the business unit should be the same, and then they don't care which they use. But in the case of a large company, say, for example, owner should be the leader of the small Team, or, like, or the owner should be the name of the… name of the team.
Vers the business unit should be… larger one. And then there… and then also, There should be the case, The… the… the… the hierarchy of the… business unit and an owner is opposite. Yeah, so I think… my gut feeling says, the service owner And the business unit should be in the same level.
Yeah, so it… so business unit doesn't… should not… go under… Owner label.
That's… that's… that's my opinion, because the… It doesn't allow, like, it doesn't allow Flexible use cases for using both labels at the same time.
**Ayushi Asthana** 28:26 Hmm, okay.
**Yoshi** 28:29 Should I, should I, should I comment on this PR?
**Ayushi Asthana** 28:32 Yeah, yeah, you can definitely, definitely do that. I think the proposal… you can comment on the proposal as well. Just one thought that I had, though, about your comment on the hierarchy that flips within large companies, right?
If we think about it as a hierarchy, we would want business unit and owner to be at the same level, but if we think about, for example.
business unit.
As being… so, for example, you called it out right, that owner is going to be the team that probably maintains this service, and owns this service from, like, an engineering perspective.
And then the business unit of that team.
of that owner is going to be, like, a single attribute, and it's going to be a property of who owns the service, right? Or it's going to be attached to who owns the service.
I see… I have heard it debated, like, both ways, where we're saying that maybe there is, like.
In larger companies, the owner belongs to the people who maintain it, and then the business unit is something else.
So, right now I'm leaning, like, I don't have a very strong opinion for… It being owner.businessid, or business unit.
it being service.business unit, very honestly. I think you should add… add your comments as well here, and… We're also discussing how this should.
**Yoshi** 30:06 Yeah, tonight.
**Ayushi Asthana** 30:08 Owner is also not formalized yet. Owner is also, like, proposed.
**Yoshi** 30:14 Okay, okay, okay.
**Ayushi Asthana** 30:17 So yeah.
I think on cost center, though, we are aligned. Cost center should be service.cost center, definitely, right?
**Yoshi** 30:24 that's fine, that's fine.
**Ayushi Asthana** 30:27 Yeah. Cool.
Makes sense.
Okay, I think I… you would have this, business unit proposal in the doc.
Yes.
**Yoshi** 30:40 Yes, I see, I see the link to the PR in the doc.
In the, in the, in the meeting platform last week, so, it's fun.
**Ayushi Asthana** 30:50 Cool. Cool, cool.
Okay, I think that is all that we had discussed last time around. There was, I think on data entity, there was a very long discussion, so we didn't get time for much else.
Things that we discussed last time.
**Yoshi** 31:08 Yeah, I… I can easily… I can easily imagine that.
**Ayushi Asthana** 31:12 Yeah, yeah. I think we're getting closer to a more formal proposal that is acceptable to the group.
So, let's see. I think next time around, we would have a consensus on the proposal, and we can move forward. I'm also working on a demo. I will hopefully have it by next week. So, let's see.
**Yoshi** 31:36 Oh, nice!
Is it going to be a public one on, OpenTeametry report?
**Ayushi Asthana** 31:43 Yeah, I'll try to do that. So I'm going to be, like, writing a… I'll try to write a small Cates app, which will propagate sensitivity across the data sources, and I'll try to, like, basically simulate the specific use case that I had shared here about transferring the sensitivity using context baggage.
So… it should demonstrate two things. One, I would want it to demonstrate that using sensitivity, how you can block network egress.
**Yoshi** 32:24 ugly.
**Ayushi Asthana** 32:25 And, second one would be how, using sensitivity, we can target to hash parts of the logs that we emit, or Yeah, I think… I think hash part of the logs that we emit, or redact logs, basically. So set up redaction rules in collection, and redact certain types of logs if they are sensitive, stuff like that. I mean, I'm gonna try. Let's see what I can come up with.
**Yoshi** 32:58 Nice, nice. I look forward to it.
Yeah. Okay. Cool.
**Ayushi Asthana** 33:04 Cool. I think this is all we had, for today.
**Yoshi** 33:08 So, my action item is to comment on, the, the PR for, service. Unit.
Yes. And I also, just a heads up, but, I'm going to take… I won't be… I won't be able to join the next meeting, APAC time for endoing meeting, so two… two weeks after one.
**Ayushi Asthana** 33:31 Right, the one on iTunes.
**Yoshi** 33:33 One on… one on April… April 2nd.
**Ayushi Asthana** 33:38 Second… Yoshi 33:40 Yeah.
**Ayushi Asthana** 33:40 Oh, I… where am I?
Yeah, April 2nd. Quarter 2.
**Yoshi** 33:47 And then, from the next one after that, I will be a part of the Grafana Labs, so… I joined the… yeah, I joined the meeting as the person from Grafana.
**Ayushi Asthana** 34:00 Congratulations. Congratulations on this new chapter. I think, I think… I, I heard, I think… Janvi told me.
yesterday… yeah, we were discussing yesterday. Jamvi told me that, you left AWS.
**Yoshi** 34:17 Yes, I did.
**Ayushi Asthana** 34:20 Great, great. Congratulations. It'd be fun new perspectives from you then, I guess.
**Yoshi** 34:28 Yeah, I suppose, I hope so.
**Ayushi Asthana** 34:33 Nice, nice. Congratulations again, and yeah, looking forward to this continued collaboration on Hotel side of things.
**Yoshi** 34:42 Yeah, definitely. And see you next time.
**Ayushi Asthana** 34:46 Yep, yep.
**Yoshi** 34:47 Alright?
Bye!
