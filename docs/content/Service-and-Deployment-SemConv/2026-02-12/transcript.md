SIG: Service and Deployment SemConv
Date: 2026-02-12
Duration: 54 minutes
Zoom Recording URL: https://zoom.us/rec/share/7R-pxPOKDaisS1y9CMHa2dKQZIpTciLtB3YgZJwMM3vo_nP5S7buGYVCdBLZ_krw.xJNZJ6Q7nReXNxVF
============================================================

## Zoom Recording Transcript

**Josh Suereth** 02:20 Hey, everybody.
**Ankit** 02:24 Hello. Good.
**Josh Suereth** 02:53 I was gonna wait a little bit for Trask to see if he's gonna show up. If you have any agenda items, please add them here. This… I was looking earlier, and I think this has everything we need to talk about right now. I don't know if there's anything else going on, but please add an agenda item if you have a new one.
**Jina** 03:11 Hi folks, I'm here for the Kubernetes, service name proposal.
**Josh Suereth** 03:21 Okay.
Alright.
Cool.
Let me, is Trask gonna be here? Let me just ping him quick, cause I think it'd be helpful to have… his viewpoint… Oh, you guys, can you see that I'm presenting the, Kate service name thing?
**Ankit** 03:56 No, your dog is visible, not used.
**Josh Suereth** 03:59 Okay, alright, give me a sec, I'll fix that.
**Ankit** 04:02 Yep.
**Josh Suereth** 04:04 Yeah, where's service, so come sync?
Sorry, I have too many open tabs.
Cool.
Okay, cool.
Let's get started with, this discussion, and we'll see if Trask joins later. Alright, so I have… I have this open. I think this is the comment in question, is that right? You wanna tell us more, Ginger?
Regina? Is that right?
Yeah, I do now. Okay.
**Jina** 04:47 So, I'm trying to, like, add a Kubernetes service entity, and, you know, when I talk about Kubernetes service, I literally mean the Kubernetes service object.
And to me, that seems like it's a completely different sort of, like, you know, you're talking about, like, a network abstraction for Kubernetes users versus the logical, service stuff.
So I think, like, these are two different entities, and if you look at the link, to the supplementary, you know, guidance we have for Kubernetes.
We have a very well-defined sort of, like, process, for how to… look up the service.name for a pod running in Kubernetes, or a, you know, application running in Kubernetes. And, that supplementary guide, it… it kind of… it doesn't touch upon the Kubernetes service itself.
the object, the network object, I mean. We try to get the name from, either from, like, the workloads controller name, or the pod name, or something like that.
We keep away from Kubernetes service, and that's very intentional, because you can create 5 different Kubernetes services pointing to all the same pods, or pointing to different pods. You can do anything. You can slice it, you know, any way you want.
So, I think it is, like, these are not… overlapping to me, but if you feel like it might become, down the line, it might become, like, confusing for users, what escape aservice, and why does it never match my service.name, from the application, we can, you know, we can discuss further.
**Josh Suereth** 06:28 No, I was gonna… I was gonna jump in. I'm in agreement with that. Like, it's telling that the default from the hotel operator for service.name is the workload identity. Like, it is the deployment, it's the stateful set, it's the job, like.
service.name and KateService are different things, foundationally. Yes, they share the same name, but I actually think OpenTelemetry's in the wrong here, with calling it service.
as opposed to, like, the Kubernetes version. So, I'm with you here. I would make… I'll make the same comment myself, but I wanted to open it up for other debate here, yeah.
Workload controller. Let's see… service that beam.
I think, service, openings, name tree.
represents evil.
Workload.
More than anything delivers a network service.
Indeed.
Kate's not service.
It's a very different thing.
We're trying to wait.
You need the same.
Really. Users.
more.
period.
Let's to try to rename?
Service.
To be simpler.
It's never a key.
Okay, that's going to be my statement, but I want to hear from other people in the SIG.
Trask, I know you jumped in late, I don't know if you have anything to say here.
**Trask Stalnaker** 08:30 No, not really. That looks like a great statement. That's all I was kind of looking for in terms of escalating it.
**Josh Suereth** 08:40 Okay.
I didn't say that on behalf of the whole SIG, but I can… I can, if you want.
**Trask Stalnaker** 08:50 No, no, not needed.
**Josh Suereth** 08:52 Cool.
**Jina** 08:55 Thank you.
**Josh Suereth** 08:56 Cool.
Yeah, by the way, did you have any other topics you wanted to talk with us here around service stuff in general? If not, feel free to drop. If so, like, feel free to stay. I was just curious. We could prioritize them.
**Jina** 09:09 No, that's… yeah, this is it. Unless I am adding a bunch of, like, Kubernetes entities. I'll keep in mind if it feels like something is more appropriate for this sig.
So, cool.
**Josh Suereth** 09:22 So, just for context, when it comes to entities.
The view on entities is actually, like, service is a boundary.
Around things that users have drawn.
Kubernetes entities are a boundary that Kubernetes enforces implicitly.
And they may be the same, they may not, but it's fine to have two entities, because the plan with entities is we'll be able to, like.
say that they're the same. So if you get this complaint in the future, feel free to say that, of like, we are modeling the Kubernetes entities as is. Where there's overlap, there will be some way in the entity world to say these are the same. But, we don't want to implicitly force… like, even if there's a notion of workload in OpenTelemetry, we don't want to force Kate's workload and OpenTelemetry workload to be always exactly the same thing, because in this SIG, we're drawing kind of general boundaries that may or may not match Kubernetes. Does that make sense?
**Jina** 10:21 Yeah, no, that makes a lot of sense. Cool.
**Josh Suereth** 10:24 Right.
Thank you. Thank you.
Awesome. Next one, Trask, Stabilized Deployment Environment.
**Trask Stalnaker** 10:36 Yeah, so I'm excited to stabilize this.
But, Yao brought up, excellent… Question, that… I think we need to decide on, before stabilizing.
And that's whether it should be an enum.
It certainly feels like there would be some benefit to having standard values for… Basic… Test, staging… prod… Hom… Otherwise, people will… Invent their own.
Enums, for folks who don't… aren't aware, enums in OpenTelemetry are open, meaning… You can always add your own Values… I don't know how people have been using this in practice.
But I guess my initial thought is, I mean, it makes sense to me for it to be an enum, but, very open to… Hearing more thoughts from people who may have been using it.
more.
**Josh Suereth** 12:20 I don't know if you wanna say anything, Ankit, here, if you have any thoughts. I was gonna just add to what you were saying, Trask, of, like, enums are open.
And so, I think this is… kind of a non-breaking change, too, to some extent. I mean, it's breaking in that we're going to define meaning for production, staging, development.
If we go with this proposal, but I'm… I'm a fan of moving towards an enum. Like, I think it… we still have the flexibility of… of… of having additional things, but we also have some good semantics, which is the whole goal.
**Trask Stalnaker** 12:53 Exactly.
**Josh Suereth** 12:53 that something's production. So yeah, I would… I'd be a fan of, like, let's… let's switch this to be a new name, let's add production, staging, deployment, yeah.
Yeah, I can make that comment here as well, but I'd be a fan of doing that before production. Enkid, I know that you were, I think it's your PR. Do you have anything you want to say?
**Ankit** 13:13 Yeah, I think I agree with you, Josh, on this. Adding it as an enum would add more significant value in terms of, semantics.
**Trask Stalnaker** 13:26 Cool, and yeah, I agree, Josh, like, if this meant we were breaking the whole ecosystem again after Deployment.environment to… deployment.environment.name.
I would… I don't know what I would do, but it would suck. But yeah, I don't… I feel like this shouldn't break… People… existing usages.
And give them kind of a forward-compatible path to getting better semantics.
**Ankit** 14:20 When you say enums are open in OTAL, does that mean, like, you can't send anything, irrespective of whether we are defining it as an enum or a raw string? Then it is functionally the same, right?
**Josh Suereth** 14:35 Open means that, we define some values, but you can send other values.
So the values we define have a specific meaning.
But if you want to send other values, that's totally fine.
The backend might not be able to interpret the meaning of them, but it shouldn't crash. That's the idea.
**Ankit** 14:54 I see, yeah. Then definitely it makes more sense than three-form springs, because we actually have some predefined values and are still open to more, yeah.
**Josh Suereth** 15:24 Okay, cool. I'm gonna make this comment, and I think we changed the stability PR to do… to be a switch to a new PR. Let that… let that kind of marinate, and then we can stabilize.
Sound good?
**Trask Stalnaker** 15:38 Yeah.
**Josh Suereth** 15:39 Great.
Man, if… this is the most efficient SIG I think I'm a part of right now.
Cool. Stabilize service peer name and service peer namespace.
Trask, tell us more.
**Trask Stalnaker** 15:57 Yeah, so I thought, Michelle did a good job of justifying this.
the change from peer.service to service.peer… well, I mean, to… Not in the making that change, but in terms of justifying these attributes as being useful.
Both in, primarily, for pipelines, where you're doing some span to metrics, work, where you have access to the peer service name, and you can stamp that onto metrics.
We also have an implementation of this. We have support in this in the Java agent.
Where users can… Set up mappings of certain host names that they know, what the service peer name and service peer namespace are.
I… Don't… I think there's gonna be, a lot of other SDKs, sort of, that, instrumentations that support that at the client side.
it's a little annoying to set up on the client side. I'm not sure if it provides enough value. I think.
that was kind of historically in the Java agent added, because… I think LightStep had, needs for it at the, Oh, I also think Zipkin had that.
**Josh Suereth** 17:42 Zipkin needed it, yeah.
**Trask Stalnaker** 17:44 Yeah.
**Josh Suereth** 17:45 Used it, yeah.
And I… it might be… I haven't looked at Apache air walking in a while, but I think they might use it, too.
Their paper required it. Like, the paper of why airwalking's amazing, if you read that.
**Trask Stalnaker** 17:58 Boom.
**Josh Suereth** 17:59 Yeah.
**Trask Stalnaker** 18:02 So yeah, so my interest in this is, we are planning to take a major version bump in the Java agent in the first half of this year.
And so… I've already added, sort of, an opt-in where people can switch from peer.service to service.peer.name.
And so we would like to enable that by default in… The major version bump, So, I'm gonna.
**Josh Suereth** 18:34 throw one complication at you, Trask, which we briefly mentioned on the PR, but the more I've thought about it, the more it seems inconsistent with our previous guidance for not like, like, I… I don't know if I buy the rationale enough.
We have http.
You know, client requests, or request client, or whatever, right?
And we have HTTP server requests.
Right.
And so, when it comes to service, and those match with span types.
We have a client spin, we have a server span.
Right?
For attributes. So, there's what? Is it server… server.client.address and server.
res… Now, how does… network. Server.
**Trask Stalnaker** 19:26 What are the kid.
It's server.address. On the client side, it's server.address. On the service… server side, it's client.address.
**Josh Suereth** 19:35 Client.address, right.
**Trask Stalnaker** 19:36 But we also have the network.peer.address, which is, your immediate peer, low level.
**Josh Suereth** 19:45 that you're talking to. Okay, so we do have precedence for beer.
Okay. I was just… I was looking at it, and it felt inconsistent when we have client and… server, but, like, inconsistently, do you know what I mean?
**Trask Stalnaker** 19:58 Hmm, I see what you're saying. I see server.
**Josh Suereth** 20:02 Like, if I'm on a client span, I look at the client attribute. If I'm on a server span, I look at the… sorry, if I'm on a server span, I can look at the client attribute. If I'm on a, client span, I look at the server attribute for who I'm talking to.
**Trask Stalnaker** 20:16 That's what.
**Josh Suereth** 20:16 We do it for half of our conventions, and then the other half are here.
Like, we made a decision to switch to client-server for a reason.
**Trask Stalnaker** 20:24 Yeah.
**Josh Suereth** 20:24 Why does that reason not hold here?
**Trask Stalnaker** 20:27 That's a good question. I do think that this one here is more aligned with the logical connection, which would be server.
and client dot.
**Josh Suereth** 20:42 As opposed to the immediate…
**Trask Stalnaker** 20:45 network. The low… the network.peer is more like a low-level, And… It was designed to be more like a cover, also.
Low-level networking use cases where you don't necessarily have a client and a server, or you don't know who the client and server are.
**Josh Suereth** 21:07 Well, I'm thinking of this, so… For context, I'm thinking of this in the use case of Alright, so I think… let's… let's classify the world into three types… actually, let me move to notes so I can write this down.
Alright, so I'll put… Threat concerns.
network.peer… Versus client.
server.
When do we decide one versus… Another. Alright, so let's divide the world, a taxonomy of telemetry type, alright? So, I'm gonna say that we have… You know, Common, you know, single… source, which is, like, I have a resource.
Of, like, you know, my service.
And I have a signal, which would be, like, my JVM memory usage, right?
It's about me.
Then we have an edge.
From source.
or destination, right? So this would be, I have a resource, which is my service.
and I have a signal, Which is a client span.
Has the, server you know, service thinking. Something like that, right?
So, basically, I have a client span that would have the service name, or I would have a… Let me show you examples this way.
I could have a server spin.
That has the client service name in it, right?
So, I have edges that are traces from, like, both sides.
But I can also have another edge, from the middle.
Okay? So this would be, I have resource, the middleman.
And then I have a signal, which could be, like, a log that has the source service and client… and, destination service are listed, right?
Because I might be able to put both of them there.
And so this is why I kind of liked the consistency of client and server, because it scales to all three types, right? If I'm talking about myself, I don't have client or server, I just have raw.
If I'm… if I'm one of the edges, I talk about the other edge.
And then if I'm in the middle, I can talk about both edges.
So, I kind of… I'm not a fan… like, the more I've thought about it, and the more we've kind of gone through this, I'm not a big fan of using peer for that reason, because it makes it then really awkward to express this third category when we get to it.
**Trask Stalnaker** 24:10 I like that, I'm glad you have thought about it.
I like…
**Josh Suereth** 24:14 Hey.
**Trask Stalnaker** 24:15 Agree that client and server fit.
better here. I will… I will… Put up… put together a proposal for that.
**Josh Suereth** 24:26 Okay. I mean, the key is we'd have to, like, actually… I think we should document this as a, as a, like, why we pick client server, right? So that people understand the rationale behind it.
Yeah.
**Trask Stalnaker** 24:43 Yeah, awesome.
**Josh Suereth** 24:44 Hi. Cool.
**neil yashinsky** 24:45 I just had one thought on that. I think it's a great point, Josh, and I was just wondering, like, client-server is, if you will, two-tier?
And… and… is… is that… is that enough tiers, I guess, was the one thing I'm wondering. I couldn't think of a specific situation, and again, I'm so… really still very new to the service, deployment SIG, but the one thing that did pop into my mind is, like, how would this represent, or could this be of value?
in determining, because I think this is part of it, is like, is this a dev, is this a test? Is this a prod? And I… but forgive me if this is not, like.
Part of that discussion.
So, is it dev, is it test, is it product? That's an orthogonal concern to this.
**Josh Suereth** 25:29 Yeah, this is more about, like, so… I think you're raising an… I'm gonna rephrase your concern to be, like, what I would be concerned about with.
**neil yashinsky** 25:41 Right, right, right, please.
**Josh Suereth** 25:42 Yeah, so this is about, like, networking connections and connections between services, right?
And a lot of networking connections today are kind of TCP-ish connections, where there is a source and a destination. What this doesn't handle in OpenTelemetry, and I don't think we have anyone working on something like it, is UDP broadcast.
or broadcast-like connections, where, you know, there's someone sending data to many locations. Right. In my, I think that if we were to model that, I don't think we would… we would use… I… we… internally, we call this edge-like telemetry, this… this thing where there's an edge, and you're trying to represent… you're either this… in the, you know, on one side, on the other, or you're in the middle, right?
**neil yashinsky** 26:29 Huh, huh.
**Josh Suereth** 26:30 But for UDP, you're… you're an edge, but you're… it's not a single cyclic kind of graph, it's… it's like a… it's a splat, you know?
And I don't think we have represented that at all in semantic conventions. That's… that's the only thing I'm concerned about with this, but for what we do have, and, like, our predominant use case, I think this model actually works pretty well. And I hear what you're saying. This is only meant to capture edge information.
Got it. And, like, the connections. All that other stuff should be, like, you were talking about deployment?
That should be captured in resource.
**neil yashinsky** 27:09 Resource, okay, okay, thank you.
**Josh Suereth** 27:12 And if you look at examples of where service name is used, like the ones Michelle's has, or the one Trask is talking about, this is, like, where we're constructing Almost a graph of who's talking to who.
And we're using these edges to understand, you know, this span can tell me that A talks to B.
**neil yashinsky** 27:30 I see.
**Josh Suereth** 27:36 Thanks so much.
Cool.
awesome.
So Trask, you're gonna take an AI to write up some thoughts here?
**Trask Stalnaker** 27:46 Yep.
**Josh Suereth** 27:47 Cool. Let's move on to, I think, Inkit, you had a bunch of stuff in chat.
That is now in GitHub.
**Ankit** 27:57 Yes, I had created a GitHub issue for this, just like you requested. I have attached the proposal doc here in the issue itself.
If you want, we can go over the talks. A short summary, maybe? Yes.
**Josh Suereth** 28:12 Yeah, go for it.
Is there anything you want me to call attention to here, or do you want to present? That's what I'll ask first.
**Ankit** 28:19 I can present, that's fine.
**Josh Suereth** 28:21 Okay, yeah, why don't you walk us through it?
**Ankit** 28:30 Just a second.
Is the screen visible?
Do let me know if I'm going too fast. I think we are, yeah, almost at times. I'll try to cover this.
Yeah. So the problem is we don't have any unified standard for defining financial ownership of the technical resources. Different cloud providers, Kubernetes ecosystems, they all rely on a different kind of mix of Cost center tags, they are mostly similar, but minor differences here and there in terms of cases, or in terms of using underscore, hyphens, etc. But almost all of them are already using it, we just need a common, unified standard for defining them. So that's why I'm proposing to add a cost center attribute to a tell.
I have provided a table here for different leading cloud providers, their tagging mechanism, what are their recommended keys, and what is their impact on billing as well. So, like, if you take an example for AWS example.
They have a cost allocation mechanism, wherein you need to go to… the cost allocation console, and explicitly enable cost allocation tags. But then, once you enable them, you can you are mostly supposed to define cost center as cost-center, and this is then reflected in the billing reports. Same goes on for GCP. Here, there's no different type of cost allocation tags with the general tags.
The recommendation is… there's no explicit recommendation as such, but more or less in the documentation examples and stuff, you will find cost underscore center, and these are then propagated to the BigQuery billing exports.
Same… kind of similar thing for Aziov and Alibaba as well.
There are some nuances to, things like AWS's manual activation, and cost sensitive as well. So, for example, in AWS, the tags are case sensitive, so if you define capital C, like in camel case, and then in kebab case, then this will come as two different line items, so that is a common nuance.
And then the observability platforms have to then normalize those tags and try to unify them together to get the right data out.
In terms of Kubernetes and infrastructure convention, I don't think there's a native field for cost distribution, so mostly there's third-party tools like KubeCost and OpenCost. They mostly gather information from all these arbitrary labels, normalize that information, and then provide the unified views.
I have done an analysis on how the… observability platforms use this cost center attribute, and if this is being used, so it is widely being used, I guess, across Datadoc, Splunk, Grafana, and then, we… I had a comment from Zhao that this is also in Dynatrace, where you can use own labels for cost allocation.
So, if you take the example of Datadog, for example, there's already a standardized cost certain… What was the rule here? Yeah, herein you can have… Dashboards built out of using attributes Sorry, I forgot. I added this last week, I forgot.
Yeah, so, here the tags can come from providers, and they explicitly take, take the cost center attributes, and then Datadog can also enrich your dashboard based on their internal attributes.
Splunk also has filter keys for their chargeback dashboard, and you can filter your traces by cost, like high CPU or memory, and then group them by the department who is paying for them by using the cost center attribute. You can also use this for spam tags, so for each of your requests, you can Filter them by which call center has higher latencies, for example.
So, yeah, going on… I feel these are the benefits of standardizing the attribute. We will get financial accountability for FinOps. You can see directly which cost center is utilizing more CPU resources, or… Where do you see more latency across switch requests? Then you can do policy enforcement based on cost center attributes.
Or you can do resource optimization as well. The SREs can prioritize optimization efforts based on what are the budgets of the cost center and where are more optimizations needed.
Yeah, that's the overview. I have provided an example specification. I will trace the PR if everything looks good.
**Trask Stalnaker** 33:28 Ankit, can you go, scroll back up?
to the.
**Ankit** 33:32 Section 5 there.
Section 5, yes.
**Trask Stalnaker** 33:41 So, the only question I had, Is if there's any connection between, cost center and the various types of ownership.
That we were discussing the other week.
Or if… we… or… or not. I… I don't have a… I could see cost center is pretty standard, like, every kind of tool you use, there's, like, Cost Center.
So I could see it not being tied to these other forms of ownership, but maybe…
**Ankit** 34:28 Right. I don't think I remember exactly what we were discussing last week. Was it related to, like, service.owner?
**Trask Stalnaker** 34:35 Yeah, and the different types of owners, like, whether it's, the… billing owner, or the, kind of, the SRE, like, live site owner, or the product Manager, product owner, business unit owner.
**Ankit** 34:59 I think in that sense, from what I can gather, I feel this is leaning more towards the FinOps side of use cases, whereas the owner side of things would help more with things related to access and security policies and those kind of things. Feel free to correct me.
Yeah, that's what I think.
And then, like, also, the next step here is to also introduce an attribute for a business unit, so that will be more of a thing that can be used for, like.
like, multiple cost centers can, belong to a business unit, and a business unit is more human-readable. Cost center are usually just IDs, so that will also be more, like, financial… finance-oriented.
**Josh Suereth** 35:53 I think, Tras, to your question about, like, is this a type of owner, like, where we were talking about different owners, I think… I… I will say two things, Drew. One is, yes, I think it is a type of owner, but I think it would be called a call center, right?
So, what this tells me, what we see with this research of, like, the number of people tagging cost center as cost center, is we should not try to force cost center to be called owner.
That's… that's kind of more what I'm taking away from this. But… but I… like, to your point in that discussion, yeah, I think this is a type of owner, but it's better named as cost center. It would be my… you know, interpretation of what I'm reading here.
**Trask Stalnaker** 36:41 And, Ankit, is the proposal that it is a… just a flat attribute, cost center, like, there's nothing else that we would want to model under cost centers, such as, like, contact person. I mean, that's kind of where I'm thinking of, like… I guess that's more the connection I'm trying to draw to the owner discussion, is if we decide on If we have kind of a standard… because we're going to have different types of owners, so there's a pattern there, and what kinds of things do we want to capture for other owners, and do we… Want to apply that here.
**Ankit** 37:22 I personally couldn't see any examples, like, any usages for those kind of, like, in any of the examples, I couldn't see that, if people are using it, like contact number, for example. So… But yeah, I'm open to taking an AI to see again if there's any potential use case for that.
What do you think, Josh?
**Josh Suereth** 37:48 Yeah, I mean… Reading through the document, I… I don't know, I still see kind of the… Like you were saying, some folks just use an ID.
You know, I'm not… I don't think Cost Center is super sophisticated in usage now. I don't know if it will be.
Like, that… there's part of the question is, if we make this capability better and easier, would people do more than just an ID?
I don't know. I think the value of cost centers is in the simplicity, to some extent. Like, the tagging, the fact it's an ID, the fact that you can, you know, divide quickly by it. The flat attribute nature of it, too, I'm a little bit… how do I want to phrase this? I'm a little bit, nervous about tenancy in OpenTelemetry?
So, right now, we're tying cost center to service.
If a service is operating on behalf of another service.
and you want to say, I have a metric that's divided by services it's serving.
Is cost center gonna show up there?
That's not a question I really wanna, like… How do I… I don't think we solved that by putting, like, service.cost center in the metric. I think we solved that by cost center being a thing that we can put in the metric.
But it'd be, like, a different cost center, it'd be like a tenant cost center or something. You see what I'm saying? But in all of the cases I'm imagining with cost center today, I still see it… Having a lot of value as just a straight string identifier and not much else.
Except, okay, let's go to the fundamental question, Enkit. Where do I get my cost center from? What's the source of truth?
**Ankit** 39:33 That's an interesting question.
I mean, I was talking to my team's product manager, I was also discussing whether we should have business unit as a different attribute from cost center, because ultimately, like, if I am a cloud manager, like, I'm managing the resources, I probably have a mapping somewhere where the database, like, you are mapping cost center to your business units, so… I… I am assuming there exists someplace for that organization, where they are maintaining all the mappings of cost centers, in terms of readability. They are maintaining their exact owners, their POCs, the contact information.
So, I think that's a different, like, database that exists, and it should be up to each organization to decide that.
So, yeah, that should be the source of truth, I guess. So here, if we just have the IDs, then people can map them back to the exact owners and use cases.
**Josh Suereth** 40:35 I do think Trask maybe convinced me, though, that we should call it service.costcenter.id.
Or costcenter.id.
And then, we have room… Where if we start pulling cost centers in as a signal, and there's more information we need, we're not… Backed into a corner.
Do you know what I mean?
I don't know, I'm on the fence now, like, thinking through it more. Should we just put a dot ID, so that if we have to do dot anything else, it works? Do you know what I mean?
And with business unit, do you think business unit, like, cost center's a function of business unit, or do you think business unit's a owner of cost center?
**Ankit** 41:22 I think it's the latter, but I'm not 100% sure, yeah.
**Josh Suereth** 41:29 What are you thinking, Trask? You threw the… you threw the grenade.
**Trask Stalnaker** 41:34 I… I know at one point we, Lyudmila had thrown out sort of a general naming convention of… domain.
something.property, I forget what, like, it was, But for the most things, we have done that sort of three-tier We definitely have some exceptions, though. Even recently in RPC, we have a Couple that are just two levels.
So it's not, like, a strict something, but… It does give us… room. That said, I mean, shorter is… has its advantages. Simpler has its advantages.
Do we have a… have we fleshed out the owner… the other owner proposals?
Because that's… Like, would we have, like, business, say, business unit?
Would that have… I guess a dot name… So I… it doesn't feel like something we would… you would stamp on… like, you would probably, on your telemetry, you would only stamp cost center, right? You wouldn't stamp these other descriptive things, probably.
But, because you have that Table in your backend where it maps cost center to all those other things.
But I don't know if that means we shouldn't, like… Has… if you were enriching your telemetry in a pipeline and stamping those things on, I don't know.
And this is a resource, so the… It's not, like, extra… Nor… it's not as much of a… Verbosity problem.
Might be worth bringing… raising in the, SEMConf meeting on Monday, just to get, I would be interested in Lyudmila's thoughts, from the… That… pattern that should… kind of described.
Before.
**Josh Suereth** 44:29 Yeah, I… I'm leaning towards just adding a .id myself to it, like what it is now, for… for intuition reasons, of like… It kind of matches that pattern. It gives us, like, room to be wrong.
Mostly… mostly what we want is if we made a mistake, and cost center isn't fully unique, and we want something else there.
We have… so Enkit, for context, we have a rule where if you have service.costcenter as an attribute, you can't put dots after it. You can't do service.costcenter.nameLater.
That breaks other things in OpenTelemetry around flattening attributes. So, it'd be better to put the .id now, and then if we ever find out we need something new, we're there. It's similar to what we did with deployment.environment.name.
If we ever have anything else with the private environment.
We don't know of anything. We don't think there's anything, but just in case, we have… it's called .name, so we can add later, right?
**Ankit** 45:29 So, like, I'm new to these meetings, but, like, usually when we are introducing attributes, does it usually always go like that? So, you always want to keep it open, or do you think there are In this particular case, Do you think there's more of a chance of having more… like, dot contact number, for example, trust mentioned.
there's more probability of that kind of thing happening, that's why you are leaning this way.
**Josh Suereth** 45:55 Yeah, so we're saying that cost center is possibly a big concept versus an annotation-y small concept. Like, if this was, like, what is my IP address?
you know, there's lots of things with IP addresses, but have it as a reference.
Another way to phrase what I'm saying, if we were to say service.cost center is, like, the identity of cost center, but we think there's going to be eventually a cost center object somewhere.
in OpenTelemetry that we can talk about, that has more than ID, We don't have to solve the no-till today either, which is, how do I have service, say, here's my cost center?
And have something else say, here's my cost center, and they're different things?
So it could be that we're facing one of those scenarios where cost center is the identifier, service.cost center is an identifier for some other object.
Similarly, like, you know, peer service name is an identifier for service.
Where we know that the peer is only gonna have, like, the name and none of the other information about the service.
But the resource will have all the information about the service, and that's okay.
Cost center might be in that realm of attribute, and I could… I could buy that argument. It could also be that we think cost center needs to be modeled, and it should be modeled inside of service, in which case we need the .id.
I'm now convincing myself again that it should just be .cost center, and if we have to model cost centers generically, we would have a, literally, a cost center domain name for, like, any other cost center things.
Right?
Actually, no, it would still be cost center ID, because if we make a generic cost center name, it would be… there'd be service.costcenter.id to represent the cost center the service is part of, but then if we have new attributes, they'd be under costcenter.stuff.
And there'd be a costcenter.id, and we'd report cost center separately from services.
**Ankit** 47:55 Right. Right.
**Josh Suereth** 47:56 Like, there'd be a thing that would go read through your cloud cost centers and fire the data at you, or whatever.
Okay.
I'm talking myself in circles here, but you get, like… I'm trying to figure out the rationale for why we are making decisions.
**neil yashinsky** 48:11 Yeah, I feel like…
**Trask Stalnaker** 48:11 Yeah, not.
**Josh Suereth** 48:12 You denigrated, walking in circles, because sometimes you can learn a lot from walking in circles, or talking in circles.
Okay.
**Trask Stalnaker** 48:21 I found the, sort of Lydmilla's… Rule of thumb for attributes name… attribute names.
Domain. I put it in chat, domain.thing.property of the thing.
So this was also, like, kind of our justification for, like, db.system to db.system.name.
Right, we've kind of done this in a lot of cases, where it's not super clear that The… that we're gonna use that… namespace.
But it's just being abundantly cautious and forward-looking.
So, I think it probably aligns well with the rest of the SEMCOM repo to do the .id.
**Josh Suereth** 49:21 Cool, we're at time. We're a little bit over time. Should we… I think… I think the AI would be, I… I think there's enough information here that I thorough believe cost center should exist.
should we propose… service.costcenter.id with the description you have, with the backing you have, and just put the PR out there and get people to comment. I think that… that would be my… I'd be a big fan of us, just… let's move forward with that.
**Trask Stalnaker** 49:52 Yeah, notch.
**Ankit** 49:55 I'm aligned with that, because I think there's no downside of doing the .id thing. I can't see of any cons, so yeah.
**Josh Suereth** 50:02 And your description literally says identifier, so, like, it's gonna tie right into it, right? Yeah.
**Ankit** 50:08 Yeah, yeah, yeah.
Yeah, just gonna have to see if I need to do the same thing for business unit. I'll look into it.
**Josh Suereth** 50:15 Okay.
Sounds good. Awesome. Thanks, everybody.
Have you seen it?
**Ankit** 50:21 Thank you so much. Same. Have a good day. Bye.
