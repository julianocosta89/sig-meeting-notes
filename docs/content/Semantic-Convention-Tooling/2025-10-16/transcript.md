SIG: Semantic Convention Tooling
Date: 2025-10-16
Duration: 38 minutes
Zoom Recording URL: https://zoom.us/rec/share/-_CK4Ti44SF_FPydn-kFS5_Fz2zqgsvZVfHQuPeTmJtct_VXmbkOV-qAsdFixp1k.oxFVb8GNPpToiCWQ
============================================================

## Zoom Recording Transcript

**Janhvi** 00:36 Hey, Coyote.
**Yoshi Yamaguchi** 00:39 Hi, John B.
**Janhvi** 00:41 Hey, thanks for joining. How are you?
**Yoshi Yamaguchi** 00:44 I'm good my daughter is just, my daughter is just sleeping in front of my desk.
**Janhvi** 00:52 Oh… Won't she woke up while you were speaking?
**Yoshi Yamaguchi** 00:58 I… I hope so. Yeah.
**Janhvi** 01:04 How, how old is she?
**Yoshi Yamaguchi** 01:06 6 months.
**Janhvi** 01:08 Oh, oh, she's, she's just a newborn then.
**Yoshi Yamaguchi** 01:11 Yeah, yeah, she was born in, in last May.
**Janhvi** 01:15 I see congratulations.
**Yoshi Yamaguchi** 01:17 Thank you.
**Janhvi** 01:19 How was your day? Oh, so you just started your day?
It's lunchtime, so half of the day is already gone.
**Yoshi Yamaguchi** 01:26 That's it.
Good, good.
**Janhvi** 01:29 I wasn't sure if anybody else would be joining. I had another meeting with the rest of the folks last week, and it's actually a festival in India, so I wanted.
**Yoshi Yamaguchi** 01:38 Oh, yeah.
**Janhvi** 01:39 we could kind of wrap up early, but I'll post a message on the group after our meeting, with the AIs, and then I'll ask if anybody's still interested. I'll do another round in the evening as well. But I don't think… I don't know if you know or not anybody from your end who was planning to join.
**Yoshi Yamaguchi** 01:55 I don't think the… I don't think anybody from AWS is joining, because other folks are based in Europe.
So… And then folks in the U.S. is… yeah, folks in the U.S. is…
is not joining, I think so. They're not, they're not joining.
**Janhvi** 02:14 Okay, perfect, then I think, this should be fine. I'll just post the message on the group after this, saying, hey, if anybody wants to join, we can meet again. If not, here are the notes.
**Yoshi Yamaguchi** 02:23 Nice.
**Janhvi** 02:24 Cool. So, maybe I'll give you, like, a run-through of what we discussed last week, and then I'd like to get your inputs and feedback on the same, and if you have anything else, we can discuss that as well. I'll share my screen, just one second.
I'm still new to Zoom, we don't use Zoom as…
**Yoshi Yamaguchi** 02:44 Likewise, I know, I know how you feel about, you know,
We started using Zoom, company-wide.
And then until then, we were using our own, like, VC solution, which is called.
**Janhvi** 02:58 dear.
**Yoshi Yamaguchi** 02:59 Chime, and then before that, I spent a lot of time with the, you know, Meet, of course, because I was in Google, so I'm not, you know, I'm not used to Zoom as well.
**Janhvi** 03:12 Exactly.
**Yoshi Yamaguchi** 03:13 You can.
**Janhvi** 03:13 Oh, yeah.
**Yoshi Yamaguchi** 03:14 Yeah, you can see the green square at the bottom of the UI.
**Janhvi** 03:20 Once again, I'll share the right green hair as well.
Okay, hopefully you can see my screen now.
**Yoshi Yamaguchi** 03:35 Yes, okay.
It'd be great if you can… if you can change the zoom… zoom level.
1% to 200? Yeah, that's, that's the…
**Janhvi** 03:46 Okay.
**Yoshi Yamaguchi** 03:47 That's good, that's good, yeah.
**Janhvi** 03:48 Okay, so I think, the first thing is, the… so I think you know about the SIG, right? We've talked about that. As part of this SIG, what we've decided is that we'll kind of divide this into three phases.
I know earlier when I talked to you, I had a list of attributes that we kind of wanted to add to a tail, but the feedback when I had raised the PR,
the feedback that I got from a lot of, the TC members was that there are too many attributes that you're proposing, so they wanted us to limit
it to a few set, and then take it from there. So what we did was we reduced the set, and we divided it into three phases. The first one being that we'll try to extend the service entity with new attributes.
And the new attributes are owner and criticality. We'll discuss about the namings, all of that, but I'm just going through the phases.
And in this service entity itself.
if… so we want to use service.name, and we… if there are any questions around that, if people have any concerns around that, we'll discuss that. So basically, the service side of things.
Second is, deployment. So, as of now, this is not stable, and people had a few… I think there were a few bugs raised around the naming. So, as part of this SIG, we'd want to discuss that, get feedback, and finally stabilize, the deployment-related entities.
And the third one… so, another attribute that I kind of… we had a use case for, was data sensitivity. So if there's some data residing in a service, what is the sensitivity of the data? Is it, like, very critical, not critical, all of that?
But for now, there is no good… there's no suitable entity for data-related attributes.
So as, like, an extended goal of this SIG, we want to talk about if we want a new entity, or if there's an existing entity that can house these attributes, specifically for sensitivity side of things.
But I think the third one would probably take more discussion, because, what at least Josh was telling me was that this has been brought up earlier, but people have had concerns around it, so we'll have to discuss this thoroughly to see if this sits and where this sits correctly in the OpenTelevatory world.
Any questions on the high-level, phases and the scope of the, group?
**Yoshi Yamaguchi** 06:13 Yeah, the definitions of the phases and then the scopes of those are crystal clear to me.
**Janhvi** 06:19 Okay, okay, sounds good. So I think, first thing that we probably… I wanted to get your feedback, and this is something that we heavily discussed last time, was what would it take to kind of stabilize deployment and service?
So the first thing that we kind of started with was, hey… so if you look at service, right, I'll maybe share it.
Da-da-da…
Yeah, so these are the different attributes that we see under service, right? And then Josh had a list of bugs that had come up around, service and deployment. I'll open that as well.
Yeah, so these have been the different issues that people have raised around these two entities. So, we just wanted to, like, go through them and see if, you know, this kind of makes sense to us or not.
And one of the issues that came up was, in the service entity.
Do we think there is a scenario that you would want to cater where there's a service, and a service is hosting multiple services? Is this, like… so, for example, in GCP, we have a concept like that, that there could be, like, a mega service, and then you could have microservices under it.
But is there something… the current model doesn't really justify that, it's just, like, one service, a service entity. So, do we want to change the model for that service entity, or we think that that kind of makes sense? And I'll tell you what the gist there was, and then maybe you can tell me if, in your place, you know, you've seen scenarios where
A service could have microservices under it or not.
So, if we… if we look at the attributes right now, right.
the namespace is supposed to kind of give you an umbrella. For example, if you're doing, like, a shopping cart app, right? So shopping cart would be the namespace.
And then under shopping cart, you could have multiple instances running, multiple databases running. Now, those could be the actual service instances that comprise of that shopping cart app. So this gives you that logical grouping of multiple services.
And that kind of answers to that question, hey, can a service have multiple services? So the namespace is the umbrella, which kind of has a logical grouping of all services, and then service.name and service.instance.id is the actual instance that is running, which is like a database or a virtual machine.
So yeah, any thoughts around that, or any feedback around that?
**Yoshi Yamaguchi** 08:57 Yeah, I think this is the… this is, really practical, naming for… for current technologies. For example, if we use Kubernetes, for example, service is a service. It's a… it's a… just… it's a set of…
Set up the instances, and then that…
give some functionality to the users, whereas the pod itself is something that actually runs the functions in a specific
a physical… physical machine. And so…
the pod ID would be the service.instance.id, and the service name would be the name of the service. So…
**Janhvi** 09:40 Good.
**Yoshi Yamaguchi** 09:41 That makes sense then, yeah. So this, this, labels… Sounds… sound really…
Fine, sounds… these labels makes sense to me.
In the case of this, you know, serverless service, such as Lambda or, CrowdRun, the same thing applies to it. So, yeah, these labels make sense to me.
**Janhvi** 10:07 Yeah, yeah, and I think that was the major question that came up in the bug triaging as well, that…
hey, you know, could that be, like, a different service? And then we… I think one of the issues is that the current
comments and the description around the service entity doesn't really explain this, that service name could be, like, an umbrella item, and if you, for example, in Kubernetes Word, if it's a pod, that could be an instance.id thing, right? So you can model it with the current labels. So I think one AI that we took as part of the last meeting is that we'll try to rewrite the description so that it is very clear that that model can still fit in with the
The current labels that we have.
**Yoshi Yamaguchi** 10:50 Yeah, yeah, so, the, the, the, the…
the item number 1 also is the one I just came up with as well. So, because the, ID
Is, is under the instance.
**Janhvi** 11:05 Hmm.
**Yoshi Yamaguchi** 11:06 but the service.instance only has ID, so that sounds weird to me, but otherwise, yeah, the… the…
the… the label… The label definitions itself is fine, but… The label,
Like, how can I express that?
So, the labels level… Should be something we should consider as well.
Consider better.
I see. So, do you think…
**Janhvi** 11:40 in future, there could be a use case, for example, if you want to, let's say, name the pod, right? Then service.instance.name, like, could there be more attributes under instance in future? Because I'm assuming that's where that…
naming convention comes from service.instance.id, it could be, like, a unique machine-generated name, and tomorrow, if you want to apply, let's say, friendly name, it could be instance.name in that case.
**Yoshi Yamaguchi** 12:06 Yeah, if… if there's… if there… if there's some plans to expand the… the service.instance,
Category or a label itself.
**Janhvi** 12:18 then that's… that'll be fine, but we should… we should…
**Yoshi Yamaguchi** 12:21 I think we should call out that we are, you know, still, still the service.instances under, like, development.
Because many users will be, confused because of that, like, like what I did.
Hmm.
So…
**Janhvi** 12:41 Yeah. Makes sense.
**Yoshi Yamaguchi** 12:41 That's the only feedback I got, yeah. That's the only feedback I got.
**Janhvi** 12:46 So I think, if I paraphrase what you're trying to say, is we should see how we can make this stable, right?
**Yoshi Yamaguchi** 12:53 I guess.
**Janhvi** 12:53 instead.ib.
**Yoshi Yamaguchi** 12:58 And then once we… once we… once we release the definition of these labels, the users start using those labels for their metrics, right? So, in that case, we cannot change the definitions of each
You know, each labeled, so what we can do is just expand the label.
So as you said, service.instance can be expanded, but we cannot replace the meaning of the service.instance.id, so if we are…
So if… so we… In that case, and then…
as I raised, the service… a service.instance.id can be used for multiple
use cases. So in the case of Kubernetes, that can be, port ID, and then in the case of the, Cloud Run, for example, then that is, you know, the port ID can be, hidden by the service itself, I mean, Google Cloud itself, and then instead.
Google Cloud returns the different type of IDs for the specific instance.
So… We kept… we should… we should… we should detail on…
how this ID is used for in several use cases, and then this is… that… and I believe that that is where…
that each card platformers can contribute to. So in the case of AWS, we can, give some example of, like, ECS, or EKS, or Lambda, or anything that runs on, AWS for, for, like.
scale-out use cases, and then Google Cloud can provide the IDE examples of, like, Cloud Run, or GKE, or, like.
Cloud on… Cloud Run Functions, App Engine, anything.
**Janhvi** 14:56 Yeah.
**Yoshi Yamaguchi** 14:57 Yeah.
**Janhvi** 14:59 I think valid point, because I assume there will be different use cases, right? So we just need to document it in a better way, so that different providers, they know how to use it.
And it could be that it can be used for multiple use cases, like you mentioned, right? In cases of pods, it's the ID, whereas in cases of serverless, let's say Cloud Run, it could be a different name that the GCP platform is generating. But we need to tell very clearly what those use cases are.
Makes sense. So, okay, I think I'll… I can probably take that AI, and in the next meeting, I can talk to the rest of the folks as well, and see… by the way, I think I'll be present in all the meetings, so I'll try to ensure that
whatever we discuss here, or whatever is being discussed here, I try to relay that information to both the groups. So I'll add this to the agenda for next time's call as well, and try to get inputs from other folks on what they think. But I think I agree with you, that the documentation needs to be better, and we need to see how
we can stabilize that. It's in development phase right now. That is something we'll have to do as part of this meeting, of this SIG itself.
**Yoshi Yamaguchi** 16:08 Thank you.
**Janhvi** 16:09 Any other feedback on service side of things, or we can move to deployment?
**Yoshi Yamaguchi** 16:15 That… I think that's the…
And also, do we have any naming convention for, service itself?
Not the service.namespace. ServiceName.
**Janhvi** 16:30 Let me double check… I don't think so.
The value is… it… okay, I'll open the description to what it says.
**Yoshi Yamaguchi** 16:48 Can you, can you, can you send… okay, I'm opening it up on, on my machine as well. So service.name is…
**Janhvi** 16:58 It's the logical name of the service…
**Yoshi Yamaguchi** 17:00 Logical… logical name of the service.
**Janhvi** 17:09 I mean, it kind of…
**Yoshi Yamaguchi** 17:10 to this.
Yeah, I only have the experiences of the, Kubernetes and then, ECS.
So… and also other… Serverless services…
So, in those cases, this definition… applies well.
**Janhvi** 17:31 Yeah. So…
**Yoshi Yamaguchi** 17:32 I… I'm… I'm… I'm… so, as far as I have used those services, I'm confident with this definition, but…
I am not sure if there… if there are any other type of…
naming conventions in other services. So.
**Janhvi** 17:50 As far as I read the meeting notes.
**Yoshi Yamaguchi** 17:55 the people from Microsoft, Google, and then AWS has contributed to the discussion. Of course, DynoTrace one as well, but…
I don't know.
Do you… did you come up with any other…
Like, like, runtime service? Serverless runtime, or container runtime, or any other application runtime?
**Janhvi** 18:21 No, even I don't have experience in that, but I think it should be… at least we can do a quick research to see what all naming conventions exist, right? And then we can see if, kind of, they fit with this category or not. So, I know you already have, like, a bug open for something like this, right? Do you mind adding this
in that bug itself, and then I can add my research there, we can get inputs from other folks as well, and see if this makes sense or not.
**Yoshi Yamaguchi** 18:49 Yeah, at least, at least, for me, this, this definition makes sense to me, and then service, the definition of all attributes in the service entity.
Sounds clear to me, so… yeah.
We can move to, deployment.
The discussion for the deployment.
**Janhvi** 19:08 Okay, okay, sounds good.
I'll open the deployment one.
Oh, what happened?
I don't know, okay.
**Yoshi Yamaguchi** 19:22 It's a… it's a… a dev tool?
**Janhvi** 19:25 Yeah… I'll… Open it from the head.
Okay.
So, yeah, I think in deployment, everything is under development.
And the one that we care about the most, at least as part of this SIG, is the deployment.environment.name. I think what I was hearing from the rest of the folks was that
In general, the rest of the items in here, they were added by CICD folks.
And we've already created a new issue to check with them and see what they think about it. Do they want to stabilize this?
Or not, or if they have concerns.
I'll open up that issue as well, it's added to the meeting notes somewhere.
Second.
Yeah, we're dead.
**Yoshi Yamaguchi** 20:22 Yeah, the government environment name is, is, is clear.
But I'm not sure how we can use, deployment.id and a .name and .status.
Especially the deployment ID is… Not clear to me.
**Janhvi** 20:41 Yeah, I think…
**Yoshi Yamaguchi** 20:42 What's the use of… yeah.
**Janhvi** 20:44 We discussed briefly about this, and I think the same questions came. So, there's an AI on Josh, I think this was added by… from the CICD semantic conventions. I think they have some use cases.
And they'll probably work on adding more description to it, because right now it's not understandable what that ID is supposed to do in case of deployment, right? Like, environment.name is very clear. It could be the different stages, production staging, whatnot, but ID, I think, yeah, even… we don't really understand if it's the actual ID when that deployment is happening.
Or, or what.
I… and there's more documentation around it as well.
**Yoshi Yamaguchi** 21:24 Yeah, for example, in the case of CICD pipeline, ID can be the ID of the specific single run of the pipeline.
Or, like, it can be a single task.
inside a pipeline.
**Janhvi** 21:40 Yeah.
**Yoshi Yamaguchi** 21:40 So, I'm not… and then also, this document doesn't mention the definition of the… the detail of
a definition of the detail of the ID itself.
So, I need more… in order to understand the use of this attribute, I need more…
Like, use cases on… on what…
this ID can be. So in my sense, in my sense, we can put, multiple, attributes for the, for the pipeline itself, like, we can put, deployment.pipeline.buildID, or, like, or task ID,
Or anything like that, but…
if… if the ID is not meant… is not meant to be such kind of You know, large scope.
**Janhvi** 22:33 Yeah.
**Yoshi Yamaguchi** 22:34 Yeah, I'd like to have more clear understanding of
the, the, the, like, Fu, Fu, Fu suggested this, attribute, and then… What?
but are… The, the, the main… use cases.
Of, like, of using these attributes by them.
**Janhvi** 22:58 Yeah. Yeah, I think, valid point, but I think one thing I'd like to mention is, at least as part of this group.
we only want to stabilize deployment.environment.name, because that's more like a metadata of the resources, and it can tell what environment you are in. Like, for example, in GCP, we can say, hey, it's a production resource, or if it's a non-production resource, right? And similarly, other cloud providers also do that. So, I think we can get more data around this, but I don't think we'll keep this in
scope.
for our work, because I think there is more work going around it, and I'll ask Josh as well if he can give more inputs on this.
Specifically for the environment.name, right, which is in scope for our sake, do you see concerns or thoughts, feedback on that?
**Yoshi Yamaguchi** 23:49 I, I…
So, for… for me, the deployment.environment.name is the body to name for… the label name for… for… for these, values.
because environment… Environment should have like, other attributes, like IDs, or instances, and so on?
So, yeah, we should, we should, we should be more detailed on how, how, like, the values, like, staging in the production can be applied to…
And then, in that sense, this attribute name, deployment.environment.name, sounds valid to me.
**Janhvi** 24:33 Yeah, and I think one thing that I had raised earlier was, so as of now, right, if you see the values for this, they're kind of marked as examples, like, staging could be an example, production could be an example, but we've not…
We can even have an enum, because we knew that… we know there are a few values that everybody will use. We can have, like, an open enum saying, hey, these are the recommended values, and if you have something else, you can maybe apply that as well. So, this is something that we kind of agreed on, and in the notes, if you see, right, there's an issue specifically for this one, to get more consensus from everybody, and if everybody agrees, then we can maybe change it to, like, an open enum kind of thing, so that people know
that, hey, this is the recommendation, when to use production versus when not to use staging. Again, to your point as well, that we don't really know and not give guidance.
**Yoshi Yamaguchi** 25:20 Yeah, I agree. And then, for me, as far as, you know, my experiences, the most important thing is that the artifact is deployed to the production or not.
So, if it's possible, I'd like to have some flag that is, is production or not, like, is production, and then true or false. And then, as a sub-label, we can… you can use deployment.environment.name for details, name of…
the environment. Like, some company uses staging, whereas some company uses testing, or, like, development. Yeah, so that… the name can be…
Changed, you know, the company to company.
So, so that's, that's, that's how I, how I felt.
But, basically, I agree with the name of the label.
So, I'm not sure if they have… if the folks in the previous meeting discussed about
The, the flags for the pro… for, like, is production flag or not?
**Janhvi** 26:31 No, I think this point was not brought up, that, should we have another flag which just tells you, like, a binary flag, right, is production or is not production?
**Yoshi Yamaguchi** 26:40 Yeah, yeah, binary frog. And then, in the case…
But the problem… problem of, increasing the label is the cardinality. So, I'm wondering if you can…
add… If he can change the label.
a label value from the arbitrary string value to enum.
So that, like, so that we use…
We use for, log level.
So in many log… in many log libraries, they use the standardized log label, such as, error, warning, information, and then debug.
So he can… if he can set up a similar type of, enum for the deployment name.
deployment environment name, then that'd be great. That's what I thought, but… Yeah.
Yeah, I don't know. So, what was… what was the conclusion from the, previous meeting for… for the name of the environment name?
**Janhvi** 27:55 So I think, people were okay with… The attribute name.
But for the enums, they kind of saw value, that we can see, if we can have, like, an open enum thing. But again, I think they wanted to consult, like, the larger audience, because again, we were just 4 people there, right? So the representation was not that high. So specifically to get more feedback, right, and maybe you should add this point in this
In the other,
this, issue that I think, Hao had raised. He's from Dynatrace. So this just talks about the same thing, the enum thing. So maybe we should, add comments here and see what the rest of the audience kind of thinks about it. But at least there was general consensus that the name makes sense.
An enum is kind of an optional. If there is enough consensus, we can go at it. If not, the one… the way we have values there, that's also fine, but we'll add more description to say what is the usual guidance on things like staging, test, production.
**Yoshi Yamaguchi** 28:58 Yeah.
Yeah.
**Janhvi** 29:07 Yeah, I… comments from folks, which even I have not read through.
**Yoshi Yamaguchi** 29:14 Yeah, we… so, yeah,
Yeah, we can, we can discuss, over, over the, over the issue, ticket. Yeah, this is…
This is hard to… for me, like, In the case…
Of using these labels just in one company, that's easy.
**Janhvi** 29:37 Good thing, like…
**Yoshi Yamaguchi** 29:37 We can, you know, we can just… just set it.
**Janhvi** 29:40 Yeah.
**Yoshi Yamaguchi** 29:40 And then it just… we can go ahead, but… Standardizing
This label is kind of difficult for me, yeah.
Yeah.
**Janhvi** 29:52 I think maybe, honestly, I think, valid point, right? A lot of companies would be using it in a lot of different ways, and then in that case, maybe Enum is not the right way of doing it. You could just.
**Yoshi Yamaguchi** 30:04 Yeah.
**Janhvi** 30:04 Open, free text so that people can use it the way they have standardization in their own companies.
**Yoshi Yamaguchi** 30:11 Yeah.
Though we are, like, listing the name of the environment, in the exa- as examples in the table.
engaging in the production. I think what we can do is to… to list as many environment names as possible in the table as the, like, preferred convince… preferred name for the convention.
So, yeah, as you said, we… what we can do is just to consult
As many companies as possible to collect the name of the environment.
Yeah, and then we can pick… the top… Like, top 90% of those.
**Janhvi** 30:55 Yeah.
**Yoshi Yamaguchi** 30:56 in the preferred, yeah, as a preferred name, and then that's it. So that's my suggestion. Like, because I'm not smart enough. I cannot come up with any good solution to… to… to reduce the number of the label, or, like, the number of the, expected values for this.
**Janhvi** 31:14 Yeah, yeah, I think, yeah, totally valid feedback, and I agree to it. Plus, I think standardization, that's why it's hard, right? There's so many people using it in so many ways. That's why standardization is so hard, but we kind of have to start from somewhere. So yeah, I think we're probably over time as well. I don't want to, waste more of your time, but yeah.
to add comments on this issue as well, and then I think the next meeting, I'll pick this up as a topic, and then I'll get feedback from other folks as well on what they think about it, right? By then, hopefully, folks will respond on this issue as well. So we can take it from there.
I think… so on a higher level, at least for service and deployment.environment.name, I think we have two AIs, I'll follow up on it, but in the next meeting, maybe we can talk about what new attributes you want to add to these entities and see if that makes sense, how you use it in your company, if you've seen other use cases for that.
**Yoshi Yamaguchi** 32:07 So this is the, the, the…
**Janhvi** 32:09 This… so the deployment attribute is just for deployment, right?
**Yoshi Yamaguchi** 32:13 one deployment to the… to some environment. So the deployment of the specific artifact to artifact, that is instrumented with the open telemetry to the specific environment, right?
**Janhvi** 32:25 That's right, correct.
**Yoshi Yamaguchi** 32:26 Okay, okay, yeah, okay.
Okay Yeah, yeah, this… yeah, these four…
at least these four… I'm not sure, how… still, I'm not sure, what the… the detailed definition of the deployment.id yet, but these four is… should… should cover the most cases, most deployment cases, like, I believe. So, yeah.
I agree, definitely. Yeah, I think I was the research before you now.
**Janhvi** 32:56 even I'm not sure about deployment.id, and what I heard last time was that the CICD folks have added it, but I'll try to do more research and see if I can get some data around it. I can take that data.
**Yoshi Yamaguchi** 33:08 Yeah, just what… what just I was wondering is if we can… we should put
the label for, like, release level. So, what… what I mean is, for example, in the case of the canary release, the percentage for the deployment is…
it changes.
As time goes. But… In that case, we cannot change the attribute Half… From, from the outside.
**Janhvi** 33:42 Yeah.
**Yoshi Yamaguchi** 33:43 the artifact, right? So, so for me, it didn't make sense to add such kind of a dynamic value to the label. So, yeah, so, that's what I thought. Just…
So, just, just, just, just ignore it. Yeah. Otherwise, otherwise, everything looks good.
**Janhvi** 34:02 Okay, cool, cool. Alright, I think, awesome discussion, thanks for your time.
**Yoshi Yamaguchi** 34:07 And, thank you for your time, yeah.
**Janhvi** 34:10 Sure, sure. See you again soon.
**Yoshi Yamaguchi** 34:12 Yeah. See you soon, bye. Have a good day.
**Janhvi** 34:15 Jesse, I…
