SIG: Service and Deployment SemConv
Date: 2026-05-21
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

**Ayushi Asthana** 05:37 Hello? Hi, folks.
**Urjita Sharma** 05:41 Huge.
**Ayushi Asthana** 05:51 Yeah, I have a couple of things today… A lot.
We'll wait 2 more minutes before we get started.
I think in the meanwhile, folks can art.
Oh.
Okay, I think we can get started now.
Win… a minute.
So, the first thing on the agenda today is the service.owner proposal. We had discussed this a while back, that we will probably attempt to define service.owner in more detail.
And Urjata had picked up that item for us to work on this definition. Ujita, do you want to present your screen and talk about the proposal?
**Urjita Sharma** 07:54 Yeah, sure.
**Ayushi Asthana** 07:56 I'll stop sharing.
**Urjita Sharma** 08:17 Pure. Is my screen visible?
**Ayushi Asthana** 08:23 Yep.
**Urjita Sharma** 08:28 Okay, so, starting with this, this is a proposal for service.ownerentity.
And its associated attributes for, open telemetry.
So, starting with the problem, like, currently, the organizations, they struggle with, like, a highly fragmented landscape of tags.
So they… these are used to basically define who owns this particular technical resource.
But, like, when there's a major incident, and the engineers need to contact someone, there's this classic, who do I ping at 2AM problem. So we need, like, a unified, basically, attribute.
to assign this So now, we have service.namespace, so there's one thing that we might argue, adding owner to service.namespace itself.
But, the issue here is, there are, like, mainly there are 3 different reasons why we don't do this.
So basically, we don't want to mix the ownership, like the logical architecture and the organizational structure.
And then there are microservices in this namespace itself.
So, each of these might be having different operational owners, and we do not want to club them into the single, like, under the single service.namespace.oner. So, that might be misleading.
And, so this basically isn't granular enough for the automated alerting, so we'll be using service.oner.
Now, looking at the current landscape.
So, each of these providers, AWS, GCP, Azure, all of them have their own, kind of, tags for this owners that they have defined, like AWS has owner contact projects, GCP has owner team contact, and so on.
So, basically, this is, like, really inconsistent, and cloud providers, they rely on this user-defined tags.
And their keys vary significantly.
So, this basically forces the platform engineering teams to maintain, like, complex normalization rules just to figure out who owns what.
And, then even, like, if we see for Kubernetes.
They don't, really… they'll act like a native standard field, which is dedicated to the organizational ownership. So, again, the teams are forced to rely on custom labels or separate catalog files.
So, to resolve this, we are proposing three, new standard resource attributes. So, it's service.owner.name.
Let me get to that.
Yeah, service.owner.name, service.owner.url, and contact.
So, basically, the service.owner, the complete entity, it explicitly identifies the operational owner of a service. So, to be clear, this is not the financial owner, the infrastructure ownership, but this is the team that is accountable for day-to-day operations, reliability, and incident response.
So, the owner.name, it's like a string for the team's name.
or how we identify that team, the owner.url is a link to the source code, a repository, or documentation, anything providing, like, a reference on, like, the code that has failed.
And, so owner.contacts, it's basically, like, a communication channel, it could be an email or a Slack channel.
So, this… this is the main thing, and the three main outcomes for this.
It's basically, we are provided with a direct routing.
So these direct contact attributes, using this, the tools can automatically map, like, their telemetry alerts directly to the on-call, like, without having to go through the manual mapping tables and everything.
And then, the operational discoverability is improved, the teams can get context, like, they can get context with the documentation links alongside any of the telemetry data, and they can, like, any, any of the services can easily be identified using this.
And also, the multi-cloud Unity, which is, like, the main benefit that we will eliminate the need to manually normalize all these different cloud tags, and the OTL collector can basically translate those specific tags into the unified service.orner entity.
So this is it. Any questions?
**Josh Suereth** 13:03 Yeah, I think… well, so this isn't a question, but I think the most important thing here is that we, the decision is that owner is the operational ownership of the software, right? Like, that… the most important piece is that.
Right, and that's how we differentiate it. Okay, so then, URL and contact… this is interesting. I'm, So for owner, URL, and contact, we're expecting someone to configure this in a way OpenTelemetry can get access to it, and those use cases you had.
Do we… do we have, like, a demo of doing that? Is that a thing, like… Attaching it to telemetry, is that a thing that people do today?
**Urjita Sharma** 13:50 Like, the basic use case for this is so that the tickets or any incidents could be automatically routed to that particular team which is responsible, like, whenever an incident has occurred. So we need to have this, contact, which will be helpful for that. And this URL is for getting context into which component has failed.
**Josh Suereth** 14:11 Yeah, yeah, yeah, like, I get that. So basically, we're adding it to the base resource.
An entity, so that when we have something that does anomaly detection, like alerting or whatever, or even looking for, like, bad logs, we could say, okay, we're going to open.
**Urjita Sharma** 14:26 in particular.
**Josh Suereth** 14:27 It's this…
**Urjita Sharma** 14:28 Great.
**Josh Suereth** 14:32 Yeah, I'm just trying to think through… think through that. Like… like, the use case makes sense, I'm just trying to think through, do we have… do we have a demo of that at all? Or is that, like, something we're thinking about creating after this?
**Ayushi Asthana** 14:48 Yeah, I think I was coming to that, I was going to ask if we should have a demo, because I think that would make how this would look like… On collection, or how this would look like actually playing out.
Better where, where these attributes are going to live, and where these are going to be attached.
Oh.
Also, I had a question on, So, this is something that I want to clarify with the SICK, what is the purpose… is service.name purely a descriptive attribute that we don't want to extend to have owner? And as… or is it possible for… so basically, my main concern was that a single namespace can have different services, right? So service.name is going to be different for each of them, and so a single namespace can have multiple operational entities.
Every single service.name entity is going to be operationally different, and so should owner be Service… dot name.owner, or does service.oner by itself make sense? Is there, like, a hierarchical, flavor to it, between namespace and name?
**Josh Suereth** 16:06 Yeah, so there is a hierarchical flavor between service and service namespace. The names of those are a little bit awkward, awkward, like.
If you look at Kate's, it's a little bit easier to see what the hierarchy is, because we have Kate's dot and then the entity name.
Which is, you know, a Kate's convention. Service, we are, we're grandfathering in to not break everyone. So… We have service.namespace is the one entity, which is, like, its own thing. Anything in service, though, is a child of service namespace, so if you wanted the organization to have an owner, you could have service namespace owner and service.owner.
as, like, things, and they would be, like, within the hierarchy. Like, that would be fine to do, but the way we've defined that hierarchy is service.namespace is the top, service.service is the middle, and service.instance is the bottom, right? And they form a hierarchy, where there's an ownership relationship between those three.
In the entities. So, like, to… to your question a little bit, we could actually, instead of making Service Owner an independent entity.
We could actually have it be a descriptive attribute of service.
So we could have a set of descriptive attributes and say, okay, service.owner.name is descriptive of the service, and you're always going to tag a service with its owner name, and that's how it works. We could also have it as an entity, which means you can report it independently.
And you can report the relationship independently. So we could have, like, a system could be designed where the telemetry doesn't include service owner.
in the data, and later on, we can actually look up the relationship between service owner and service, and start attaching these things downstream. Like, that's the idea behind entities, is that you can do those attachments later, as needed.
So you don't have to do them right away, and when you have systems that, like, you know.
You have a system that can explain to you this service has these relationships We can go collect that data, feed it to something else, and do these joins.
At ingestion time, we can do it in the database, like, you have more flexibility.
So hopefully that explains the entity side of that. Like, like, you have options here. And I think there's the open question of.
do we want service owner to be an entity, or do we want it to be a descriptive attribute of a service? You could go either way. Like, there's pros and cons. Go ahead, Anthony, sorry.
**Anthony Mirabella** 18:38 Yeah, and I think I kind of wanted to extend that question a little and ask, should owner or contactable Entity of some sort be an object of its own type that can be attached to a service, or to a namespace, or to an instance.
In that same way, you're talking about correlating entities, even if the data's not necessarily in the telemetry. Like, can we say that I know that this service namespace has this entity that owns it? Not OTLP entity, but, you know, this unit of people or organizations.
And it has a name and a URL and a contact mechanism, and a service has the same, which may or may not be the same as the namespace, because of that kind of containment Hierarchy that you were talking about.
**Urjita Sharma** 19:29 I get your question, but, help me understand, like, what would be the use case when, like, if a service.namespace has a particular owner, and the service has a different owner.
Why would we… like, in which scenario would you want to contact the owner for the namespace rather than the service?
**Anthony Mirabella** 19:51 For escalations, like, maybe you've got 5 services in the same namespace that are all throwing alarms. You probably want to contact the owner of that namespace in addition to the owner of each of those individual services. Or maybe a service has been in alarm for, you know, 6 hours, and you want to escalate that to the namespace owner to make sure they've got visibility.
**Urjita Sharma** 20:13 Okay, but, like, the operational teams, if the operational teams for each of the services, or some of the services are different.
Like, they would be the primary contact to basically, like, de-escalate the issue.
So, shouldn't the escalation go up from their end, rather than… directly contacting the…
**Ayushi Asthana** 20:37 Yeah, go ahead. I, I think… Sorry, I… Yeah, finish your thought, I'll go after that.
**Urjita Sharma** 20:44 Yeah, no, it's done. You can go.
**Ayushi Asthana** 20:47 Anthony, correct me if I'm wrong, but you mean that, service.oner or owner as, Attribute or an entity can be attached to namespace, as well as to individual services. So if we sort of model it as an entity independently, we would have that flexibility to attach, owners to either namespaces or individual services. Is that… am I… am I understanding that correctly?
**Anthony Mirabella** 21:16 Yeah, correct.
And I'm just kind of wondering if that has value. It seems like it's a pretty straightforward modeling choice.
We've got that containment structure of namespace, service, instance, and each of those can have an identifiable owner.
I don't know that it has necessarily direct utility immediately, but it also seems like the sort of thing where it might be useful to build the capability if we If we need to build it for service anyways, but it can then be also applied to namespace and instance, then if people have a use for it, they will be able to use it.
**Ayushi Asthana** 22:03 I think it would make sense for us to have, like, a demo for this one, and see how it plays out in real scenarios, specifically for multiple services under a namespace, how this plays out.
Okay? Okay.
I think we can, we can do that. We can have… yeah, Josh, get something.
**Josh Suereth** 22:27 I just want to say, the thing I think we should all agree on, which I think we do implicitly, because no one has said anything.
But the fact that owner will be operational ownership.
I want to lock that in, right? Like, like, does anyone disagree with that? Because I think that's the most important decision here, and then figuring out, like, demos and things, great, like, like, that's follow-on work, but as long as we can commit to that and then move forward, anyone, anyone have concerns with, like, tying owner to operational ownership? Like, we have… Cost owner, which is cost ownership.
I think this makes sense, and then if there's other types of ownership, we would find other names, right? I think… I just want to make sure we're committing to that, so that we can keep making, you know, progress.
**Anthony Mirabella** 23:11 Yeah, I fully support that, and I think that's another plus in the column of treating an owner, you know, the name, URL, contact info kind of tuple, as a unit that can be reused in multiple places, like the cost owner, the operational owner, the, you know, whatever other owners we might have.
Should have similar structures.
**Urjita Sharma** 23:34 Yeah, I agree, Anthony.
**Ayushi Asthana** 23:41 I think we already have, proposals out for cost center and business unit that take care of, ownership from, like, billing or business perspectives. So, locking down this specific definition would be useful, so that we don't keep confusing Between the three of them.
So, for this one, I think the next step is to have a demo.
For this playing out specifically with multiple services, I will… I don't? Okay.
Can I share my screen now?
**Urjita Sharma** 24:31 Let's stop making sure.
**Ayushi Asthana** 24:34 Okay, so the next thing on the agenda is, Anthony, I'm not sure if you're aware, but we met with the, semantics Working Group on Monday to discuss this data attribute group proposal. And the main concern that came up at that point was data being too broad.
And being too… Reusable as an entity, so that we cannot define it. We cannot exhaustively define what this group can contain.
And this can get confusing fast.
Although I'm… not entirely sure, what future-looking, semantics we can propose at the moment, but data by itself, or at least what semantics we're proposing, have value. At least we were, I think, aligned on that they have value, but, the main thing that we might want to solve is, calling it data, probably. Josh, you can keep me honest here, but I feel like the most of the confusion or concern was arising from Calling this attribute group data, right?
**Josh Suereth** 25:57 I, you know, I don't know if it was confusion, it's more concern around the scale of the project.
So, we kind of briefly mentioned this when we had our project spec here, but basically, the way I'd phrase it, maybe to put it more concretely, this is the service and deployment sake, right? And so.
in our scope.
I think initially it mentioned data, and then it said, we're gonna cut that out of our initial scope, and that would be, like, follow-on work. I think one of the things is, if we're going to have data.
they, you know, if we had a whole project proposal that got people around and aligned, and what will it impact, and who are the experts, that… they're kind of seeing it as that big, right? So that would be a new SIG.
If you will. A new area of ownership. So their concern about data is not necessarily that they don't understand it, I think it's more that they… their intuition is it's going to be a big, major effort to actually Outline that, and that, you know, this is a good… like, nobody disagreed that this first use case is useful, and that the prototype demonstrates it.
But it's more, what is our commitment from there? Like, can you take… to some extent, if you're familiar, slippery slope fallacy, it's a bit of that, of, can we take the first step without taking the rest of the steps?
So I, I think what they're looking for is a way to… Comfortably take the first step without, like, forcing us to take all of the steps.
So, I was gonna talk with him a little bit offline as well, but I still think We had a bunch of discussions around data.
I don't know if there's a better term. I mean, we went back and bike-shedded a good bit, so…
**Ayushi Asthana** 27:45 Yeah.
**Josh Suereth** 27:46 My personal thinking is, I want to talk to the maintainers to be like, could we put a caveat around it that says, we're going to introduce data for this use case only, expanding off this use case requires a SIG?
Right?
And so, that way, it's clear what the data namespace will be, what the ownership model is, when we can stabilize what we have, that kind of thing.
that might not fly. It might be, like, I think… Independently, we should also look for, is there a way we could design or name this so that it is targeted at services and deployments? You know, so it's somehow within that scope, and obviously within that scope, and not broader.
That's what I think the major concern was there, that I… like, from my read of the discussion.
**Ayushi Asthana** 28:42 Right.
I think I got the sense of the first part, at least, where this feels like too big of a commitment to make, because of the broadness, at least, of what it could turn into.
So, I think I… I sort of got this idea, from… I think Shermishta is on the call, and so she helped us come up with probably something like classification, because that's what we're trying to do. We're classifying data that the service is handling. We're not trying to do a lot more with this, we're not trying to define sources or anything, we're just trying to classify data at this point on, category sensitivity and, like, a bunch of other factors. So instead of calling this just data. If we append the term classification, it makes it very clear that we are just talking about, how do we classify this data? Is it sensitive? What category does this data belong to? Instead of just talking about Data in general, and opening it up for debate on what this attribute group should or should not have.
So that was one of the things that I wanted to bring up here. If Data classification seems like a better or I mean, more specific terminology for this use case.
**Anthony Mirabella** 30:15 So I'm kind of wondering whether we should go the opposite direction and prepend with service to make it clear that this is about the service's data.
And so we're not stepping on, you know, any general data categorization that there may be. I think, you know, making it clear that it's about classification is also perhaps good. So service data classification category and sensitivity kind of fit well into that.
But kind of to Josh's point, if we can constrain it to the service by putting it within the service namespace, that may help.
I have kind of similar concerns about the enumeration of, category and sensitivity, because those are… going to vary wildly from place to place, and the way our spec talks about enumerations, like, if we've got an other category, like, then nobody can come up with their own additional names.
So, I think whatever we can do to ease into it, kind of as Josh said, of, you know, find some first steps that we can take that don't necessarily commit us to more, but also don't foreclose future options, would be good.
**Ayushi Asthana** 31:35 The only… the only thing I might have with service.data is I… I would get confused by… what… what does this mean? Like, service data, as in… Is it… is it data… is it data that the service is emitting or consuming?
Or… is it… Telemetry that is being generated by this service.
**Anthony Mirabella** 32:03 Right, or what level of data is it cleared to handle? Like, can it handle sensitive data? Can it handle confidential data? Can it only handle public data?
Or is it, this service is handling confidential data?
**Ayushi Asthana** 32:18 Great.
Right, right. So that is… that is… that is a thing. When I… when I hear… basically, this might… might be, like, just a… a preemptive bias, but when I hear service.data, I get, like, a bunch of questions on what does this mean in… in relation to… Well, the service.
Okay?
So, there was that. I'd like to hear more thoughts from people on what they think about both of these options, or a third option that we could have that… that Might make our lives easier.
**Josh Suereth** 32:56 So, the… it'd be… it'd be not just service.data, though, it'd be service.data.criticality, right?
**Ayushi Asthana** 33:03 Right, yes.
but I think the same question stands. Is it handling this data? Is it emitting this data? Or…
**Josh Suereth** 33:16 Probably.
Yeah, I mean, we… that's… that's what our… our job is, is to define what, you know.
**Ayushi Asthana** 33:22 Yeah.
**Josh Suereth** 33:23 To actually give it a definition, and define what the attribute is in the… in the YAML.
So it's machine-readable, so people can figure that out, and… because again.
you know, there's always ambiguity with words. You know, people can misinterpret things real far. And people do. Even when we have attribute definitions, there's, like, ambiguous ways of reading them. That's why the English language grammar is just as important as the definition of it.
Is it… it was… yeah, it was sensitivity and… and criticality, were those the two, or was there something else?
No, where is that?
**Ayushi Asthana** 33:58 Yeah, it was kind of good.
**Josh Suereth** 33:59 Category. Sorry, yeah, I used the wrong C word. Okay, yeah. See, that's also… my brain doesn't work there sometimes, right? Anyway, yeah, so we have, like, category and sensitivity, and that's… I still kind of like that suggestion, Anthony. Like, I feel like that actually limits the scope Sufficiently enough that it's within our… group's charter. I also think you can misinterpret it, but I think it's not… Crazy, like, if you're confused and you're not sure.
I think that's where the docs will help you. Like, my question would be, do you think someone would implicitly assume the wrong thing and use it the wrong way going forward?
Or do you think they'd be confused as to what it actually means, and then go read the docs? The second thing is not too bad. The first thing is really problematic.
**Anthony Mirabella** 34:54 Yeah, I think we probably have to get out and ask people about that. Get in front of users and say, hey, if you saw this, what does this mean to you? And just kind of get their first impression, because we're all going to have our own assumptions that we come to this with.
**Josh Suereth** 35:11 Yep.
**Anthony Mirabella** 35:13 I unfortunately have another meeting and I need to drop, but I think, you know, my general feedback here is anything we can do to constrain the scope of the initial effort, especially to our specific service, is good.
That gives us a chance to kind of trailblaze and give feedback to a broader SIG if we do want to have a general data classification entity or group of entities.
**Josh Suereth** 35:37 Yeah, and to… I know you have to drop, so feel free to drop now, but I think the… if we put it in service, we could actually make these experimental attributes and start testing them out in front of users, you know, throw the demo out, like, add it to OpenTelemetry Demo if people want to see it, get people interacting with it now.
And go through, like, that cycle of getting people to try it before we, you know.
stabilize. I… like, we could go almost immediately, because again, it's in service, so…
**Ayushi Asthana** 36:07 Right.
And I, I also want to make… so, I want to ask if this is, like, a one-way thing for us, where, for example, we introduce it in service, and we, You know, have enough… Feedback or enough evidence that this, warrants attribute group by itself. Would we, in future, be able to split this out? Or this is a one-way street?
**Josh Suereth** 36:36 It is not a one-way door. So there's two things that are true. So one is, Until you mark it as fully released.
we can change things in OpenTelemetry. Now, I am trying to be more conservative there in semantic conventions, and force this to be a little more structured, but effectively, you should be able to change it. But, even when it's released, you can deprecate it and move to a new thing.
The caveat will be service.dataCategory will remain always in semantic conventions and deprecated fashion.
like, if that makes sense. So, like, because we're, like, building a standard and we don't know where instrumentation is, we're kind of like the HTTP spec here, right? Once we stabilize something.
It will always be there, but we can mark it deprecated and kind of reserve that name, so you never, ever reuse service.data.category to mean something different, ever again.
But we can start moving the instrumentation and the ecosystem to the non-deprecated thing, which would be, like, a baseline, right? So… It's not a one-way door, it's just, you know, there's still… a cost, it's just not… I think it's a reasonable cost. And it's the cost of pretty much any standard that you see out there, you know. I don't know if you've ever seen the HTTP header standards, and, like, the number of deprecated headers that are just no longer used. It's pretty high.
But it works, right?
**Ayushi Asthana** 38:09 That makes sense. I think if we can get some, input on what users are going to think about service.data, that is a very, I think, easy direction for us to take.
For introducing these attributes at this point.
So…
**Josh Suereth** 38:27 Absolutely, yeah, and the other thing I'll suggest is, because we're going to get out, like, a prototype and have an experimental for some time, and get user feedback.
**Ayushi Asthana** 38:37 Hmm.
**Josh Suereth** 38:38 You have the opportunity to change to data without keeping service data.
Prior to release candidate, right?
**Ayushi Asthana** 38:46 Right.
Makes sense. Makes sense, actually. Okay.
I'll… I'll probably raise a proposal for this one and see if we can get some… some insights.
Oh.
**Sharmistha Rai** 39:01 One question, so I wanted to ask, like, if we have to release service.data and get it tested within the community, how much time would it take for us to actually launch it just in the preview mode?
**Josh Suereth** 39:18 Oh, you mean, like, the… where it's marked as experimental and you can see it?
**Sharmistha Rai** 39:23 Yeah, correct.
**Josh Suereth** 39:24 within a month. I mean, like, as soon as it's mer… we're supposed to be cutting a release of some kind of every month, but we keep forgetting.
So, once that is merged, just ping the semantic convention channel on Slack and say, hey, can you guys cut a release? We'll cut a release. Like, it should be very, very low effort.
Right? Okay. So, the maximum amount of time should be a month if you… if we merge you right after we cut a release. But, you know, it should be within some reasonable bounds.
**Sharmistha Rai** 39:52 Yeah, actually, I think, like, it would make sense to actually just release it and get the community's feelings, because when we read it, it… we automatically assume it's talking about the data of the service.
And not data of the customer. So, that's where the confusion arises from. So, if the customer data is able to influence us to keep it data.category, then that works in our favor. And if this one itself works, then best for us.
**Ayushi Asthana** 40:24 Right, makes sense. Then I think we will try to release this one.
**Sharmistha Rai** 40:33 Maybe we can start with one of those and see how it goes.
**Ayushi Asthana** 40:37 Yeah.
Okay, makes sense. Taken in the eye for this one.
I don't think we have anything else on the agenda, so if you want to drop… Can do that now.
Excuse me.
**Sharmistha Rai** 41:10 Bye.
**Urjita Sharma** 41:12 Thank you.
**Ayushi Asthana** 41:13 Thanks.
