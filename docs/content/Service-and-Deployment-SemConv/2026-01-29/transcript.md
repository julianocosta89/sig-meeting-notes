SIG: Service and Deployment SemConv
Date: 2026-01-29
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Eimear Foley** 01:34 Hi!
**Trask Stalnaker** 01:38 A…
**Eimear Foley** 01:41 Good evening, slash good morning.
**Trask Stalnaker** 01:43 if… Same to you.
**Josh Suereth** 02:35 Hey, everybody.
**Trask Stalnaker** 02:39 Hey, Josh.
**Janhvi** 03:10 Hey, everyone.
**Trask Stalnaker** 03:19 Hey, John V.
**Janhvi** 03:21 No.
Till the time we wait for other folks, feel free to add things to the agenda. I've added a few PRs where, what I wanted to discuss, but yeah, if there's anything else, please go ahead and add it to the notes doc.
I see Dota is now going to join, I think he's unavailable. Should we get started, then? I think we have Corum.
Am I audible?
**Trask Stalnaker** 05:11 Yeah, yeah.
**Eimear Foley** 05:12 Yes.
**Janhvi** 05:14 Okay, sounds good. Okay, I'll, hope you guys can see my screen. I'll just go through the agenda.
I think this we discussed, last time as well, and I wanted to discuss again with the group and see if you guys have any opinions.
So, the TLDR is, we're trying to add a new attribute called owner to the service namespace.
And we wanted to discuss if the way we are modeling it right now, do we have any feedback around that? Are we good with it or not? So, I can go first, and feel free to, add feedback on top of it. So, I think I was looking at the PR, I'll open it as well.
my major concern with the PR was that, for now, it felt like the structure that we're defining is very generic and flat in the sense that if you're saying service.owner, just by looking at the owner, I don't know what that owner means. Is it the…
organization that's owning it, is it the team that's doing the development, or there's, like, business owner attached to it? So, owners could be of multiple types, right? So, I don't know if…
Having one generic field for owner.
Would help us satisfy the use cases that we have with other observability vendors or not.
So, I mean, for example, I think I was looking in Google Cloud, the way we have defined owner here is we have, like, 3 types of different owners, depending on
what they're… what they're owning, for example, development owner, operator owner, and business owner. I mean, obviously, we can discuss what type makes sense here, but I think my main concern was that it's too flat and generic and may not give us the value that we kind of are looking into.
**Eimear Foley** 07:01 Yeah, I was… I was looking into this as well, and, like, I would echo those comments, like, in…
within AWS, and also our customers who use our tooling, like, they tend to have a hierarchy of ownerships that they apply to their resources and applications. So, like, there's a tendency of…
The user, like, what user in the service is, like.
publishing these metrics or logs, which, like, really goes to that billing use case. They want to know who's caused the spike in billing. And then you have which development team owns the service, which business unit or department
has to, you know, be responsible for capacity planning and funding for that service. And then, sort of separate, and maybe not part of the service entity, is something like a billing code or a cost center.
I think billing code is what GCP use, but internally in Amazon it will be cost center, so…
I think, yeah, similarly, it's too flat based on, like.
Customer usage tends to be around almost a hierarchy of ownership.
**Janhvi** 08:05 Yeah, yeah, I agree.
Trust Josh, anybody else, any comments, thoughts on that?
**Josh Suereth** 08:16 I… this is also kind of what I… I made a comment on the PR to that extent, that I think we need to…
account for that. The other thing I wanna,
But, like, my fear with some of this, and specifically everything we're doing in the SIG, is where is the source of truth coming from?
Like, where do people define it, where we pull it? And owner's interesting, right? If we have multiple owners, do we have multiple places where we look for the owner to report against it? Are there multiple places where that's recorded?
I'm kind of thinking about, you know, what's the system of record that defines this relationship, and where do we get access to it to define that? And then what do I use that information for as things flow through?
So, you know, John B, what you listed here, and I'mart, you… the, if I tie correlations between the two things you've written, right? Business owners and financial owners.
kind of feel… or billing owner. Is that the same? You list billing and business ownership separately. Are they different? Incident response, I think, is what we call operators.
Versus developers. So I think there's a lot… the development team, like, I think there's a lot of pairing between those two, so it seems like we have…
The classes that we need as, like, a first step here of… there are 3 types of owners.
or at least there's n types of owners, and we have, you know, reasons for them. I'm still looking for what do I do with the data? Like, like,
business owner and or financial owner, I get you can…
understand who is spending all your money, or like, you know, what cost center is this associated with? Developer-owner, I get you can reach out to a team responsible for coding to say, here's a problem I have with your system. Operator-owner, I get you could use this for, like, here's where the alert goes. But I…
knowing what we have for owner and knowing how it's going to be used, I really do want to keep pushing on those use cases.
And part of that would be, for me, Where does this get defined?
Right? Like, OpenTelemetry needs these… Attributes to send them.
So where do we get them from? What's that system of record, and how does that system of record model it?
If we're going after existing, you know, owner things in GCP and Amazon, great. If we're going after existing owner things… I looked in Kubernetes.
Sorry, I'm getting ranty here, so I'll finish in a second. I looked in Kubernetes to see if there's, like, ownership recorded by default in Kubernetes, and that's something that is layered on. Like, that's not an out-of-the-box thing, you know? So…
Yeah, this gets into use cases, to examples, and, like, where we expect this to be produced. I have no concerns whether or not owner is useful.
I just have concerns that I want to make sure we're solving the use cases we intend to.
**Trask Stalnaker** 11:22 Two things that resonate with me are,
Billing owner, because that seems very clear.
As opposed to this business owner, the team responsible for quality and business expectations, feels like I'm not sure what.
What the action is there.
Or it doesn't seem too clear. And the other is the operator-owner
as Josh said, the… where the alerts go, basically. So those two things. Where do the bill… where does billing go, and where do alerts go?
Seem like they have pretty… well-scoped definitions.
**Eimear Foley** 12:03 Just in favor of, kind of, the business owner, or trying to differentiate it to the billing owner.
more often than not, I see that in a, like, a compliance perspective, where it's things like.
these systems are not compliant with, say, like, FedRAMP, or GDPR, or, you know, there's a Log4J vulnerability, and they track that not at a team level, because these tend to be, like.
campaigns or policies run company-wide, they tend to track that at the business owner level, so that's probably one of the bigger ones I see for that use case.
**Janhvi** 12:50 Yeah, makes sense. I think… so what we are saying is, I think the TLDR is we need more use cases for all of them, right? I think we are all aligned that owner makes sense.
But then…
What different categories of owner make sense in the hotel world is something we still need to work on.
Josh, I think I see your hand raised. Go ahead.
**Josh Suereth** 13:11 Yeah, yeah, like, what you're just saying there, reminded me of, like, for business owner, right? Like, a use case, you just mentioned compliance. So, why would I want business owner attached to telemetry? Cool, if I have something that detects you're out of compliance with FedRAMP or something, I can grab that business owner and report against it.
Is that, is that, like, an example that you're looking for here?
Is that a good example, I should say? Like, does… is that what you mean?
**Eimear Foley** 13:39 Yeah, that is a fair point. I think it probably also ties in with the DevOps use case of, potentially, I want to see
like, potentially, I emit metrics of, you know, my services are, you know, have this TLS termination
cipher, etc, and then I want to graph or visualize those metrics.
By my business unit.
Something like that.
But again, I see your point. That's not necessarily something you interact with in telemetry, but more like there are tools built for those purposes.
**Josh Suereth** 14:20 Sure, yeah, I… what… I don't mind modeling it in our model, it's just I'm trying to understand, like, where does that interaction come from? Where does that association happen, and what are those…
like, if we could say here, types of owners, developer owners, team responsible for coding and development. Example use cases include blah blah blah blah blah blah blah, right? Business owners, team responsible for quality, business expectations, compliance, conformance. Examples include…
blah, blah, blah, blah, blah. You know, that's… that, I think, could really, nail down what these are and how they're used for folks to help us understand. Again, this gets back into the point of.
I really want to get more use cases around this, so we kind of understand what's the best way to model at NoelTel, and what's the best way to get the data from A to B, you know?
**Janhvi** 15:15 Yeah, I think at least from my side, I need to do a more… I need to look into more use cases. I don't have a lot of them other than the billing and the cost center example that we discussed. I'll try to find some more, and if I get them, I'll either directly comment on the PR, or I'll send it on the Slack so that we guys can take
that discussion forward, but yeah, I think rest of Emer, if you have more examples, feel free to add them, and then we can, kind of comment on the Keeper PR as well.
Okay, cool. Let's move ahead. I see a couple of PRs that are open, and I think I wanted to ask everybody to kind of review them. They're more… they're all around the service namespace.
I don't know, I think for criticality, if I remember, we did… alright, let me quickly double check.
I don't know which one is this.
What is opt-in? I'm not sure of what opt-in is. Josh Rask, would you know that?
I think we added this in development mode, right? Is there, like, a different step after this that we need to follow?
**Josh Suereth** 16:25 Yeah, so, I can speak to this. Basically,
Optin means that the user has to take action to include it, versus it's automatically included by OpenTelemetry instrumentation.
So this would mean there's a flag or something that the user turns on to say, include criticality.
Otherwise, it's not included by default.
The reason this PR exists is, if I recall correctly, this was added to service, and service is actually already considered stable.
And we have a rule that, like, a stable service shouldn't add,
Shouldn't add new attributes that aren't opt-in.
Now, I actually… I should comment on this, because I actually think we don't…
This is a descriptive attribute. Descriptive attributes do not need to be opt-in. You can add them at any point in our data model.
This is more a concern for metrics. So, basically, the identity of the service is used in the identity of a metric.
if you change the identity of a metric, you can actually break all alerts and dashboards and tooling around that metric. So, we have a bunch of things that, you know, generally, we ask you to use an opt-in when you add a experimental feature to something that's stable.
for the purpose of descriptive attributes, because they're a new thing in SimConv.
we can be a little more lenient here. At least I'm comfortable with that if we wanted to. If we wanted to say, cool, actually, no, we think this should be recommended, and we'll stabilize it later.
I'm fine with that, but I think the general discussion of
you know, should criticality be required, recommended, or opted? We briefly talked about it when we merged it. Probably worth discussing on here. There's the overall concern about, is it… would it be a breaking change if this was added as an experimental attribute? No, because all descriptional… all descriptive attributes don't have to be included.
by default. Like.
one of the goals of entities was that we can drop descriptive attributes if needed to reduce payload size. They're all kind of optional.
The opt-in versus recommended versus required is what a default instrumentation author should do.
So if I'm writing something in OpenTelemetry.
should I include service criticality by default if I have access to it, or should I require the user give me a flag to say include it? That's the decision there.
Trask, do you have anything to add from SEMCOM, like, general SEMCOM there?
**Trask Stalnaker** 18:58 No, that makes sense to me, that the difference between… that descriptive attributes could be added. It sounds like the difference between spans, where we do allow attributes to be added, versus metrics, where we don't.
**Janhvi** 19:18 Josh, on the part where you were mentioning that should this be mandatory, recommended, or optional, I'm just trying to understand, right, if the user has this information, why would they not send it by default? I'm just trying to think of the other way. Why would you kind of make it…
like, an opt-in thing for them, given this is descriptive. If they don't have it, they can just ignore to send it. If they have it, ideally they should.
**Josh Suereth** 19:44 Yeah, I can, like, generically, where we've made opt-in decisions previously are, if the cardinality is incredibly high.
Like, we think the metric actually, or it's sensitive. So, for example, I think request response logging, at one point, some of those were optional.
So, the… whether or not you include, like, information about a request that's coming in might be optional. Whether or not include, like, IP addresses might be optional, an opt-in thing, as opposed to, like, a default. It's…
That's the difference between opt-in and others, is basically, if we think there's a reason why, from a technical standpoint.
This data either isn't used that often.
is somehow sensitive, and needs the user to say, yes, I want it, or,
is kind of like a potential architectural pain to deal with, like high cardinality data. Then we mark it as opt-in to require the user to say, no, I really want this. It's not, you know, something that,
Yeah, I wouldn't say it's not really important, I'd say it's not a common use case for people observing data, right? So it could be there's some…
company that really, really, really cares about, you know, how many, locks you're touching in the file system. But 90% of companies don't care, they just want to know if they're out of file system space. So we might mark that part, like, that metric to be opt-in, as opposed to required or recommended.
For example.
I… I'd agree with you that I don't think criticality actually fits the opt-in model. I think it…
I… at a minimum, I think it's recommended. Like, if you have access to it, you should probably provide it.
That'd be my take on it.
**Trask Stalnaker** 21:42 It's also kind of just de facto opt-in, because users have to specify it. There's not, like, an automated data source, if I understand correctly.
**Josh Suereth** 21:55 Yeah, exactly.
So, I can, I can actually take a response to this PR about the general entity data model and opt-in.
We… I think right now it's… is it… is it required or recommended today?
**Trask Stalnaker** 22:16 recommended today.
**Josh Suereth** 22:17 recommended, yeah.
That's… that's what I thought. Does anyone… does anyone think it should be not recommended and instead required? Because our options are…
required… recommended opt-in.
And we can also add a note about, like, how it's required or how it's recommended.
That's… that's it. We have those three options. Anyone feel that it needs to be different?
**Janhvi** 22:42 Go ahead. Yeah, required as you're saying, I mean, don't send any data if you don't have it. You can only send data for that specific instance if you have this attribute as well. That's… is the definition of required.
**Josh Suereth** 22:53 Yeah, required means, like, if you're going to send this semantic invention, you need to also provide this. You might get errors if you don't. So that's why I don't think it's required.
**Janhvi** 23:03 Yeah, yeah, I agree. I think recommended makes sense here. If you have the information, you might as well send it, but I don't think it should be required.
**Josh Suereth** 23:13 Okay.
Alright, I will… I will deal with that PR then. I'll respond back with, how the entity model works, why this is fine, and things going forward, and we'll probably just mark that as closed.
**Janhvi** 23:25 Okay.
Sounds cool.
Thanks. Okay, I think we have 3 more PRs. They're all… we discussed them last time as well when we met. They're all different attributes which need stabilization. I think for some of them, we have…
approvals, Josh, from you, but I'd request everybody else to also review it, and just wanted to discuss if there's any feedback
Or any, if you guys think this should not be stabilized, any conflicts on that area.
**Josh Suereth** 23:55 So, John V, you can also approve these, by the way.
**Janhvi** 23:59 I think… Yeah, I did them just before the meeting, did I not?
**Josh Suereth** 24:03 too early, yeah.
**Janhvi** 24:07 Yeah, I've… okay.
Yeah, I think Imar Trask, whenever you get time, please review it.
Okay, moving on to the next topic. I think this, Arnav, we have Arnav here, I know, Arnav, you sent this on Slack. Maybe we can take 2 to 3 minutes, go through the proposal really quick.
This is specifically for the deployment.environment attribute, we wanted to stabilize it, and I think Arnav has done the analysis of what all use cases are there for this, how does this make sense?
Yeah, but before that, any… if you guys have already taken a look, any feedback on this, or should we just do, like, a quick overview of this proposal?
Okay, enough. Let's maybe take a few minutes and do a quick overview.
You're on mute enough.
**Arnav Bansal** 25:06 Can I, can I share my screen, John? Or maybe you can, directly open the doc.
**Janhvi** 25:12 Yeah, go ahead, share your screen.
**Arnav Bansal** 25:25 Yeah, I think, this is, this talks about sta- talks about stabilizing the deployment environment semantic in OpenTelemetry. So, deployment.environment is, like, one of the most basic attributes we use while defining any service or, database or stuff like that, so…
We all know that it is used for defining access policies, and then monitoring and alerting systems, and then doing some cost analysis, and stuff like that.
So most, cloud providers, like AWS, Azure, GCP, etc, provide basic tagging support, and most of the clients use this tagging support as a way to define the deployment environment, like, tags like environment equal to prod, or environment equal to staging.
And apart from this, AWS Proton and GCP AppHub also provides in-house support for these attributes. Like, they treat,
The environment type as a first-class citizen, in one way or the another.
So, if I talk about Kubernetes, Kubernetes also does not have an in-house support, but we do use labels, and most big companies, when they are defining Kubernetes.
clusters. They basically, use, OPAs or gatekeepers, to define, to mandate that there are certain labels, like environment equal to production or environment equal to staging, to, their clusters.
I'll quickly talk about the downstream consumption platforms like Datadog and Splunk, etc. Basically, they all have integrated with this attribute in one way or the other.
For Datadog, it has a reserve tag known as environment, and the OpenTelemetry collector automatically maps the deployment environment name to this tag.
It serves as a primary key for them to… for service maps and trace analysis, and so if the mapping fails, the data will not be populated to the native environment filters.
Similarly, for Splunk, Splunk also uses this field as index dimensions. Basically, it's a zero latency filtering method where you can directly,
Use that filter to split the service map topologies, and ensuring that our service has different types of data from staging and
Production and stuff like that, based on your attributes.
Similarly, Grafana. Grafana application observability also has mandated to use the deployment.underscore environment label. Again, they use it for base… they use it as a primary filter for distinguishing between various environments where we define R.
jobs.
Yeah, I think, as we all talked about, this is one of the most basic fields that we use, and it is used for different alerting and,
Regression detection, because we don't want pages to come to alert our on-callers for non-critical jobs, and it is using cost analysis, as well as, applying security governance methods.
Yeah, I need questions regarding this?
I think, yeah, that is all I had.
**neil yashinsky** 28:49 You know what I mean?
**Janhvi** 28:50 Yeah, I think…
**neil yashinsky** 28:50 Oh, sorry, go ahead.
**Janhvi** 28:53 No, no, I was saying at least I am aligned with stabilizing this. I think there are a lot of use cases that are powered with environment today, and the way we have it makes sense to me, but I just wanted to understand from everybody else if you guys are aligned or see any concerns with it.
**neil yashinsky** 29:11 Yeah, I always…
basically saying, I don't see any issues, and I am broadly aligned. I don't have a tremendous amount of background, and, you know, much less should, you know, be listened to as a source of authority, but, like, yeah, you know, Arnav asked the question, and, you know, give an answer, I'm listening, I'm paying attention, I'm not ready to say I'm an expert who should, you know, you gotta listen to me, Arnav, for the love of God, anything like that. But no, this is a good, I think
This is,
given where it is, and the… you know, I've seen… I'm no longer with Grafana Labs anymore, but it added tremendous value, to the customers who were using it, so…
**Arnav Bansal** 29:48 Excellent.
**Josh Suereth** 29:51 Yeah, I know.
**Arnav Bansal** 29:51 Thanks a lot, man.
**Josh Suereth** 29:52 I want to thank you for doing the research, because this is awesome. The only question I have, doesn't have to do with stabilizing name, is, should we add tier? Because…
It looks like there's… tier is a separate thing in Cates, am I getting this right?
**Janhvi** 30:13 What do you mean by, in this case, Josh?
**Josh Suereth** 30:16 You have case locks environment, teams create custom labels, ENV and Tier. Oh, is tier the same thing as ENV? Is that what you're saying? Got it. Got it, never mind.
Never mind. Okay. Yeah. I have… I have no concerns, like, this covers all the use cases, why it's used, all that kind of stuff. The only question I have, and I'll mention the broad question, was we have development.environment.name.
Is there ever going to be something else in the dots? Like, development.environment.blah.
I think the answer's no.
But I.
**neil yashinsky** 30:51 I was phoning…
**Josh Suereth** 30:53 What?
**Eimear Foley** 30:53 That is the only thing that maybe is a concern for me. So, like, I was just spot checking a few of our own public documentation in the background, and we do have a feature called Application Signals, which collects hotel instrumentation, and one of the things we collect
is, a custom attribute on, deployment.environments. Let me just share, maybe.
I'm…
this one, that was my, my only kind of question. It says, if services are not running on Amazon ETS, you can specify an optional custom value for deployment.environment in the hotel attribute resources parameter.
I don't know if that could introduce any clashing, or if someone is setting a custom attribute, does that have any impact?
**Trask Stalnaker** 31:52 I think that is a historical remnant that, deployment.environment.name used to be deployment.environment.
Josh, so you're… you're asking if we should change it back?
**neil yashinsky** 32:09 I thought he meant… He…
**Josh Suereth** 32:10 No, I'm not… no, I don't… I think that…
**neil yashinsky** 32:13 Let me ask if there were gonna be other values than that. Forgive me.
**Josh Suereth** 32:16 Yeah, I'm asking if there are other values, and I think the answer is no. What I'm trying to get at is, if we do deployment environment name, is that the identifying attribute?
Like, I'm fine if other attributes would be descriptive later, if we say, cool, this is… Oh, the entity. Yeah, that's what I'm trying to tease out, is, like, is the name sufficient and identifying for…
deployment environment. And I think, like, when you look at this research and look at how everyone's using it, yeah, like, there's… this is what everyone's doing, this makes a ton of sense. I don't see any blockers, I just wanted to ask the question to make sure.
And it's the question I asked when I first saw the paper, but I, you know, it's been how long, and I don't have an answer, so I think the answer's no. But I just wanted to check with others.
**neil yashinsky** 33:02 You know, it's funny, Josh, I will say that when you… when you raised your rhetorical question, I immediately, immediately, immediately thought you were gonna say yes, not no, which I just… But the thing that I did wonder is, because we've already seen this change once.
And, like, abstraction as, like, a core principle just to, like, computing, right? I almost feel like if you support a name, that it almost implies the existence of supporting a label, for lack of a better word.
Just given how, like, we already saw that change once, right? And, you know, environments seemed like, well, that's perfect. Who's ever gonna need a name besides environment? And like, oh, well, actually, yeah, environments may have need for, if you will, multi-tiered naming. And so…
It's almost like if we just have a single field as name, it's like, well, it's…
should support one value besides a string of name, at least, you know, going forward. Like, label, I think, seems like, you know, something that, honestly, maybe it's time to consider something like that, because label could have some really useful disambiguity properties. I'm not advocating for it today, pardon me, just the
Describing how… to answer your question in the future, how that might be you.
**Josh Suereth** 34:23 Right, right, right. But, cool. So to clarify, though, if we were to add, like, a label, that would be descriptive, which is totally fine.
what we can't change in the future is the identity of a deployment, right? So a deployment would be set, stage, whatever. Yeah, so.
**neil yashinsky** 34:40 Agree to that point, sorry, if I wasn't clear. Yeah, yeah.
**Josh Suereth** 34:43 No, no, no, yeah, yeah, yeah, yeah, cool. So yeah, to wrap that up, I think we should stabilize deployment environment name.
**Janhvi** 34:57 Sounds good. I think the next step would be to then create a PR, with that, and we'll add the doc in there. Anuf, maybe you could take that AI, create a PR, and…
Let's end.
**Arnav Bansal** 35:08 I'll actually have the PR, I'll just share it with the group in the Slack.
**Janhvi** 35:12 Oh, okay, let's add it to the notes as well, in here.
**Arnav Bansal** 35:16 Sure.
**Janhvi** 35:19 Okay, alright. I think the last thing on the agenda that we have is… I saw a message on Slack from Lydia, I think, she just wanted to understand, what we have in plan for 2026. I'll try to summarize what we started with from the SIG milestones perspective.
But yeah, feel free to add, guys, if you have anything else that you would want to…
get added in this, the charter of the SIG. I think there's a link that she's added in the Slack group where we can go ahead and add ideas for that.
Okay, I think that's all. A few things for next time, and we… there are a few more proposals that we are working on. I'll try to send them on the Slack. I know when we started this SIG, we also talked about
the data entity, which is, like, a new entity that we wanted to introduce. I know, I think there's going to be a lot of discussions around that, but I at least want to start seeding that idea. We have a proposal, I think Ayushi has that. I'll try to send that on Slack in the next few days, so that all of us can review it offline, and the next time when we meet, we can discuss more on it, around the use cases, how that
Makes sense in the whole hotel, world.
Cool, that's all from my end. Anything else? Anyone?
Okay, then, I think we can wrap it off. Thanks, everyone.
**Eimear Foley** 36:47 Same.
**Trask Stalnaker** 36:48 Have a great day.
**Arnav Bansal** 36:49 Thank you.
**Eimear Foley** 36:49 I…
