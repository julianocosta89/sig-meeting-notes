SIG: Service and Deployment SemConv
Date: 2025-10-23
Duration: 39 minutes
Zoom Recording URL: https://zoom.us/rec/share/VJG8-GUF_afsn2W0B2Or26jyMVVzOZVFBmgDQkiZVDaw8khX7ECBmABBQnxciumi.Q1_oQl7OwKuNW1Of
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:04 Hello, can you hear me?
**Dotan Horovits** 01:09 Hey, Josh, can hear you loud and clear.
Can you hear me?
**Josh Suereth** 01:15 Yeah, good, good, good. Yeah, I can hear you.
**Dotan Horovits** 01:17 Great.
**Josh Suereth** 01:18 Alright, I know that, John V wasn't able to join us today, so we'll have to see, who else was able to make it.
**Dotan Horovits** 01:29 Sounds good.
**Josh Suereth** 01:30 I was gonna give folks, like, another minute or so to join, but anyway, do you have any topics you wanted to talk about?
**Dotan Horovits** 01:37 No, actually, it's my first time, because I couldn't join, the last couple of times. I guess maybe more… Procedurally, I had some confusions myself, personally, and also my… the other folks that I wanted to join the call about the calendar and things. Like, I had an invite, and then for some reason I got cancellation, and then I saw that the meeting did take place, and… So, I'm just… and then also, I… there was a decision to, to, alternate between time zones, but on the CNCF calendar, I still see it as a, the same, like, North America, first, at least last time I seen a bit has changed since, just procedurally.
**Josh Suereth** 02:17 to make…
**Dotan Horovits** 02:17 Make sure that people don't miss the meeting because of these, these things.
**Josh Suereth** 02:22 Yeah, let me, let me just show… so the way… the way this works, there's two different meeting invites, but what you want to do is you come in here to the OpenTelemetry Community Board, and then for any special interest group, there is an invite group.
And so there is one for us, where is it? Right here. If you join this calendar group.
Here.
You will get an invite to all the meetings from the OpenTelemetry Google account.
So, there's… there's, like, an open telemet… so the problem… the first invite you got was not from the OpenTelemetry account, which means it was owned by a single person, and no one else can move it around or change it. And so, the governance committee has a Google account.
That we make these meetings against. And then, once you join that group, we have the ability to give you edit access to it, where you can move it around.
So, like, people who run the SIG can move the meeting, anyone. And that group will send you invites, and so there's actually two separate calendar invites you'll get. You'll get one for… and if someone shares you an invite.
without you joining this group, you won't get updates. You get a copy, which is… this whole thing is annoying, honestly. Like, the way Google Calendar does this.
It's what it is.
**Dotan Horovits** 03:41 Yep.
**Josh Suereth** 03:41 I won't speak too much ill of my own company, but the workaround is, you join that group, and you'll get both of the different invites, and they're both on Thursdays, but at different times.
**Dotan Horovits** 03:53 Okay.
Gotcha.
Okay, I'll circle back, because for now I have, like, anyway, on my calendar, both the CNCF and the auto ones, so I just turned them on, but then, you know, you get everything. Everything is covered by all the SIGs and tags and working groups and whatnot, and then you need to… to pick… so I picked this one, but I wanted to make sure that I, I followed the right one, and I… for some reason, I didn't see on the bigger one, I didn't see the other there you should see the two occurrences as well, I assume, and I couldn't see the other occurrence, I saw only the one that is on this time, so…
**Josh Suereth** 04:27 I'll circle back and see what I missed.
It might be that that one is not, Not well-defined yet, so we'll have to take a look at that.
**Dotan Horovits** 04:38 Okay.
**Josh Suereth** 04:39 Yes.
**Dotan Horovits** 04:40 So, I don't know if.
**Josh Suereth** 04:40 Okay.
**Dotan Horovits** 04:41 document that as part of the agenda, just to check, I don't know if it's you or whoever is leading that from the lead, just to check that at least ones that work with the hotel board calendar.
**Josh Suereth** 04:55 can see.
**Dotan Horovits** 04:57 That that path also converges to the two, Two ones, and not just, what you said. Anyway, just a feedback for, double checking, because I… I know that I had, specifically, I wanted to bring a few colleagues of mine, and they reported the same, like, one said that he got cancellation, the other one said that they joined, but they weren't admitted into the call, and I don't know, it's like… and I'm… my concern is not just my call, it's just that we're not missing on interested parties, they just get, confused, because we want the folks, especially as a… I'm also a SIG lead on the CICD semantic convention, so trust me, I know all the hardships of kicking off a SIG, I'm just saying from experience.
The beginning is actually the one that you want the smoothest, because you want to really get people… anyone who's interested, just join us, and that's the message to be, and then you don't want the friction to stop them from joining.
**Josh Suereth** 05:53 I absolutely understand, yeah.
It… because that can kill all the momentum, right?
**Dotan Horovits** 06:00 Exactly, exactly. You have, like… and I shared also on my LinkedIn, everything, and people actually responded very positively, like, people are seeing the value and are interested, and then I direct them to the calls. Hey, come join the calls, and, you know, so I'm just saying, let's… as you said, the momentum, let's garner the momentum. Yeah.
Yeah. I see we have, Joan as well. Hey, Jo.
**Josh Suereth** 06:23 Hey, welcome!
**Joao G. (Dynatrace)** 06:25 Right.
**Josh Suereth** 06:27 I think… I think we have enough… it's been… it's been 10 minutes, so I think we should probably get started. I'm sharing the wrong, tab, sorry. That was a tab I have to do another… that was the meeting before this one, so let me… I need to do…
**Joao G. (Dynatrace)** 06:41 I'm doing stuff.
**Dotan Horovits** 06:42 Now it's the right one. Now it's the October 23.
We can see it.
**Joao G. (Dynatrace)** 06:45 Sure, you're all.
**Josh Suereth** 06:46 That's right.
**Joao G. (Dynatrace)** 06:49 robotic.
**Josh Suereth** 06:51 Yeah, I'm on my cell phone because my computer audio died, so apologies.
**Joao G. (Dynatrace)** 06:58 No worries. I thought it was the wrong mic or something.
**Josh Suereth** 07:02 Yeah, no, I had it too far away. It was over here, and instead of over here. So, I will talk closer to the mic.
Yeah, you're on speaker, though.
**Dotan Horovits** 07:14 Trust me, see only your lower part of your body.
We're missing the famous beard, so.
**Josh Suereth** 07:28 Can you zoom in on only the beard?
**Dotan Horovits** 07:30 The trademark.
But we can't hear you if you're.
with that.
No, not… now you're muted on the Zoom?
**Trask Stalnaker** 07:43 Can you hear me now?
**Dotan Horovits** 07:44 Yeah, now I can hear you.
**Trask Stalnaker** 07:45 Fantastic.
**Dotan Horovits** 07:47 Cool.
**Josh Suereth** 07:49 All right, so, I looked at the notes from la- I didn't… I wasn't able to attend last time, and unfortunately, John V won't be able to make it, and I think this is a bad time zone for Yoshi. So, there was talk about service instance ID, what do we have to do to make it stable, and then something about a flag for resource prop. We'll, weather resources brought… we'll talk about this in a little bit, but I wanted to… take that discussion and link it to the one that we had two weeks ago on this notion of service namespace, service, and service instance, right? So this is formalizing the entities on service and their relationships. What I did was I took our discussion last time and I created a PR, So this is the PR, if you want to take a look at it, make comments. This is still in draft form for us to kind of talk through it, of what it means, what it looks like, but this creates a new… service resource markdown. I haven't updated the previous markdown, I mean, it is updated because I changed service things in it, but I haven't updated the previous markdown to figure out where we want to live, but this is a dedicated, like, what does service mean?
And this is supposed to match our discussion from last time, and with definitions. A service is a logical component of an application that produces telemetry data, events, metrics, and spans. In modern distributed application architectures, a service namespace is the entire set of components that you've designed, to give to end users an application. It's like a… it's like a group. A service itself is one of those distinct components, like a database, an HCP server, that kind of thing. And an instance is an instance of a component, like.
If I'm running several HTTP servers in a pool, then they all are one instance of that component.
Right? And so these are the definitions that I have. I'm not super happy with the definitions, by the way, I think that's what I want to talk through. And then I put together just a diagram of, cool, we have a service namespace of, this is my blog site, we have a service name of, this is the database, and here's an instance for that database.
We can have a service name of an HTTP server, and there's two instances underneath that.
And this is the mental model we want you to have of Service instance, service name, Service namespace.
Then what I did was I went into the attributes we have and just moved them.
So we have an entity called service, where the name is the identifying attribute, and the version is descriptive.
Actually, why are both, I need to… I need to update the thing that… so identifying descriptors show up here. Service instance has an instance ID, which defines it, and it uses the existing definition we have, which we can talk through all of that craziness, then, if you want.
That is the current state of Service instance ID today, and there's a lot of thought behind what that is and what that means. And lastly, we have a service namespace, which is this, we're trying to take namespace and make it be this overall thing.
Okay, so last time we talked about this relationship, and that's kind of, or 2 weeks ago, and this, this is the… formal description of that. Now, what I put in the notes was.
I'm still not super happy with the notion of namespace. And so, I actually just asked Gemini, again, I work at Google, so someone can do this with ChatGPT, feel free. I'm curious what the answer is. But I said, what's the definition of service for OpenTelemetry? Because theoretically, what this does is it takes all the writing we've done on the internet.
and coalesce it into a, you know, what the common understanding of it would be, theoretically, if the LLM's doing its job right. So what are the semantics that we have? And this is an interesting baseline, and I kind of like what it came up with. So… Service is a logical component of an application. Bam. Done.
Right? It's a logical grouping. An application is the entire system that you've designed for either an end user or an application, and a service is one of the distinct components that make it up.
The problem we have, by the way, with application service is people want a mobile application to be an application.
That said, I do think this definition kind of fits it.
But we can… we can continue on.
The key characteristics that they talk about, there's a logical name, which is service.name, which is the logical name of a component. You need to understand that there's unique instances, which we talk about, and then it goes into LLM slop, I think, when it hits resource attributes.
Like, yes, of course. We, like, this is not a necessary thing to write. We know what resource attributes are in OTEL, and distributed tracing context, I don't know where that comes in, but great, cool. We can trace between services in the system.
So, in summary, OpenTelemetry Service is a fundamental unit of deployment and operational concern for telemetry data you're collecting and analyzing. I like… I like this split here of application service instance.
And I like that better than namespace service instance, because namespace just feels… I know that application is still just as generic, but namespace feels too generic, like we've crossed the bar.
In any case, it matches what we were talking about. Yeah, the two things that are important. This matches what we were talking about before, of there's a grouping of components, a service is a component that could have multiple instances, and then an instance is a specific instance of a component.
Where, logically, all of the instances with the same service name should be the same thing.
Right? But they're different instances that you might be bouncing between.
So if I have multiple instances of a database, somehow they should all be correlated or part of a cluster or something where I, you know, I'm treating them similarly.
If I have multiple instances of a server, it's because they should all be the same you know, thing, conceptually.
So it's logical grouping.
Okay, so going back to what I wrote, you can see I'm heavily influenced by this definition, because I liked it, which is, service namespace is a set of components designed for end users or other applications to leverage.
Service is a distinct component that makes up an application.
Typically running as a separate process or microservice, and an instance is a distinct instance of a component. For example, a specific Kubernetes container that is part of a Kubernetes deployment which offers a service.
how do we feel about this? Thoughts, concerns, you know, Open discussion.
**Dotan Horovits** 14:33 I like the use of logical, Which I… I'm missing here, and I saw in the definition. I think that it's important that the service is a logical entity, whereas instances are, to a large extent, not logical. They're just, mechanism.
to scale, to create redundancy, for, I don't know, depending on the architecture. So, I think separating between the logical entity, so you will, or the end user, the client, let's say if that's a server… the service is a server side, the client will interact with the service as if it were a single unit.
Not knowing that ultimately it's fanned out into, it's… the request is fanned out into multiple instances, depending on sharding logic, or redundancy logic, or whatnot. So, I would incorporate that into the definition.
And, yeah, I think it's worthwhile considering whether service namespace or application. It's… I understand definitely what your… the points that you're making. On the one hand, like, service, so it's nice, service namespace, service, and service instance.
sort of, service semantics, but I understand the value of maybe application as a more common term. The thing is that namespace is overloaded also, maybe last point, and happy to hear others. Namespace bears meaning also on the Kubernetes side, so I'm trying to think if it's… conducive to the situation, or confusing to the situation, using the term namespace. So, I'll stop here, happy to get other thoughts around the table.
**Trask Stalnaker** 16:15 Yeah, we discussed that last time a little bit about, Josh brought that up, the… Kubernetes namespace, being mostly the same, but not quite the same.
**Dotan Horovits** 16:29 Yeah.
**Trask Stalnaker** 16:31 I… I… I'm not sure I like application.
Just because I… Like, the… From a terminology perspective.
It doesn't quite, and maybe because I'm influenced by mobile, but also… We do, I mean, it… service.namespace is pretty widely used, so I think… Did we not Stabilized service namespace?
Josh?
**Josh Suereth** 17:08 No, service instance ID, service namespace, yeah, the two of those are not stabilized. So, like, that's… that's one of the things. And also, service… service name?
has interaction in the SDK.
Right? Service, version, service instance ID, and service namespace all are completely opt-in.
There is no… there's no, like, thing in OpenTelemetry that forces you to have those, or, like, provides those. It's kind of an opt-in thing.
**Joao G. (Dynatrace)** 17:49 The thing that I think about, that I think about when, when, reading all this and think about it is that, like, in reality, the service part doesn't really exist, right? Like, we have this logical grouping.
in the diagram, for example, where you had a service and then the service instances, but in reality, you only have the instances, right? So, like, when sending the… telemetry data or something. Yeah.
I don't know, that might… I don't know, that might be confusing for people.
To understand the model. I'm not sure if I'm… able to express what I… what I mean, but… .
**Dotan Horovits** 18:33 Yeah, I think that's what I tried to say about the logical, maybe I didn't explain myself for it, but I think what you just said, maybe you said it better than me, is exactly why I think describing it as a logical entity, which doesn't, as you said, it doesn't manifest in something that you can see tangibly in production, in actually running.
Whereas Ita says E is the physical, physical entity, or the… so, that's why I suggested using this terminology of logical versus.
**Joao G. (Dynatrace)** 19:02 Yeah, because, like, for example, if you bring to Kubernetes, Kubernetes, there will be a service, for example, like a thing that is deployed as a service, and then you have the, you know, instances of that service, so you can see it.
But in our model, service is just, like, a logical grouping of things, so… It's the same thing as we would think, like, a process group and a process group instance. I think a group instance of processes.
**Josh Suereth** 19:28 So to make things more complicated, or less, I guess, I agree it's logical, but are you familiar… so, you know, most observability vendors have a way of drawing an application or a service boundary.
And so service name from, like, Jaeger is like, cool, I want to look at a service and see what's going on with the traces of that service, and that's… that's a logical boundary that someone's defined via OpenTelemetry Config.
Our operator will actually fill out the service.
On your behalf, the service name.
flag, to give you that logical boundary, where sometimes that boundary is exactly like the Kubernetes boundary.
So, like, Kubernetes has a physical object which says this is a service, but actually what we call service is a deployment in Kubernetes, and so we fill service name with a deployment name, because a deployment can have multiple services in it, in Kubernetes, but it's the same concept, right, of what we want.
And so we tie that. But have you seen, like, the… let me find this… Kubernetes recommended labels?
Here's another fun one, if you haven't seen this. Kubernetes has this notion of recommended labels, right? Of an applicat… it's literally app.kubernetes.io slash name.
And you can have an application and a component.
And you can describe that your application is part of something else, and that there's a managed buy, that, like, here's the thing that is managing this application, and, like, controls its… you know, definition. We're… we're actually… There's a place where it's defined.
Okay? And this is a thing I want us to start thinking about with service and open telemetry, is, like, most… there's some systems that are naive, that are starting out, where, like, okay, cool, open telemetry might be the source of truth for what is a service.
But at some point, that might be Helm. That might be a Helm chart that I drive that actually defines crap in Kubernetes, and there's a CRD in Kubernetes that tells me what the service is, and I want to tie to that.
And that's… there actually is a physical thing somewhere that I can go ask, what services do I have? And it will give me a list.
Right?
So, like, at some point, we want to tie to something that owns it, possibly, but theoretically, it's a logical grouping. Yeah, there might be a system that does the logical grouping, but for us, it's just like, it's a logical grouping.
And this is the observability logical grouping that we need. Most observability systems just reflect the data they get back to the user, as opposed to define and own that model.
So, from our perspective, someone tells us it's service X, we don't care, cool, it's service X.
you're… the downstream system will figure out how to, like, tell us what services are talking together and all that kind of junk. We're not going to be the owners of that data. We just need to reflect it back to you.
But when you look at stuff in Kubernetes like this, and it's kind of recommended labels, and, like, what some systems do, should we engage with this, right? Kubernetes literally calls it an application.
And a component.
I think it's too late for us to change service name.
But it's possible…
**Trask Stalnaker** 22:35 For example, based on the data, it's looking like, app name in Kubernetes is service… maps to service name.
**Josh Suereth** 22:47 Yes.
Yes, exactly.
**Trask Stalnaker** 22:54 As opposed to the service namespace.
**Josh Suereth** 22:57 Well… It… it may or may not be. The component thing is where I get… it gets a little funky.
So, like… In this case, MySQL is a database, and the part of where you're saying, hey, I'm part of a higher-level application, remember, we specifically said we don't want to have a relationship between services?
In this case, WordPress would also be an application.
**Joao G. (Dynatrace)** 23:23 I guess the, the component…
**Josh Suereth** 23:25 OS would have a database component, yeah.
**Joao G. (Dynatrace)** 23:28 I guess the component there, based on the… on the… on the example, looks like more like a type, right? Like… what this component is, or what this application is. It's a database. It could be, like, a web server or something.
**Josh Suereth** 23:45 Yeah, yeah.
**Joao G. (Dynatrace)** 23:48 So, like, what… look for the… from the list, what kind of matches, the service namespace that we have today is the part of, right? Because it's like, that will be the WordPress.
like, you're a part of the WordPress, and you have a, you know, like, a website, a database, and… Whatever else.
And then they call it a higher level?
They use application in multiple places.
**Josh Suereth** 24:13 Applications of applications, yeah.
**Trask Stalnaker** 24:17 It's…
**Josh Suereth** 24:18 They do have examples here of, like, a simple stateful service would be, like, okay, I have my service with an instance, and then a web application with a database. I would have WordPress that has an instance here that's managed by Helm, that has a server component that's part of the WordPress application, but then I could also have that database that we talked about, right? So, this is where the… they're actually annotating all the different CRDs in Kubernetes as being part of the application.
So again, like, the application itself is the general thing, and the component is, like, this is the… I'm describing what this particular CRD in Kubernetes is.
**Joao G. (Dynatrace)** 24:58 Yeah. I guess this example is not… maybe not very happy, because the WordPress thing is used in… it's… it's confusing in itself, right? WordPress is also the app, but it's also, like, the… you know, the grand… the grand thing, because it's… yeah.
**Josh Suereth** 25:15 Yeah, it's used for both, and that's a little awkward, right? Because, like, here, now the database is also part of WordPress, but this component… is the database, which is called MySQL, which is part of WordPress, but WordPress is the bigger thing. Yeah, like, it… anyway, I guess… I want us to kind of look at this and understand it a little bit, and, like, understand… like, the two important things I have here are, first of all, you know, people are doing this crap outside of observability.
It's not an observability-only thing, service.
Second, there is an owner, even if it's logical. Someone will own this.
And we need… we need the ability of whatever we've defined to allow OpenTelemetry to be the owner, where people specify those resource attributes wherever.
And that's how they configure it, or we need the ability to interact with some other system that tells us what the service name is, and that could be Kubernetes annotations.
Where we say, cool, if you're running in Kubernetes and you're using these annotations, here's how they map.
Those are kind of, like, the… the two points I wanted to make there.
But I think we can also get inspiration. I guess, third point, we can get inspiration on our model from here to see if our model is going to handle what's going on elsewhere.
**Joao G. (Dynatrace)** 26:41 I think, honestly, it's not so far apart, I think it matches. It's just the example with the WordPress is a bit weird, but if you understand it… if you look at it a little bit more, it's already, like, yeah.
We don't have the type thing, like, to say what component is, or the type of it, but I think the rest matches pretty much one-to-one, right?
**Trask Stalnaker** 27:00 Yeah, the three layers, the…
**Joao G. (Dynatrace)** 27:03 Yeah, exactly, yeah.
**Trask Stalnaker** 27:05 namespace… Oh my god.
**Joao G. (Dynatrace)** 27:07 Well…
**Trask Stalnaker** 27:09 instance ID.
**Joao G. (Dynatrace)** 27:12 When you set up.
**Josh Suereth** 27:13 Yeah.
**Joao G. (Dynatrace)** 27:13 mapping, Josh, do you mean? Like, that… that's just, like, a curiosity now. The… is your vision that… like… backends would, for example, would in that case not… the limit not have the service name, but, react the same way if this other Kubernetes matching attribute is there? Is that what you… Envisioner.
For example, if…
**Josh Suereth** 27:39 What I, what I wonder…
**Joao G. (Dynatrace)** 27:40 to my backend. Yeah, go ahead.
**Josh Suereth** 27:43 Yeah, so what I want to avoid is if somebody has gone to length to configure The notion of service.
In one system. That we don't force them to redo it.
**Joao G. (Dynatrace)** 27:58 Yep.
**Josh Suereth** 27:58 That we can engage with it in some fashion, and like, you know, observability uses OpenTelemetry Service to denote these boundaries.
And so what I want us to think about is, cool, the actual definition of that boundary is an important part of the journey that we're on with semantic conventions. Like, we're not just saying what's the right abstraction for service, namespace, service, and instance. We're saying, cool, if I'm trying to build a successful observability solution.
where do I define service? What do I use? And can we engage with that in a way that's healthy and works? So, you know, This Kubernetes is an example. People might use these annotations as recommended for defining service.
we should make sure, in, like, one of the prototypes that we provide, we would provide a mapping from those two service, and say, cool, if you run in Kubernetes, and you're using these annotations as they're defined.
Here's your observability experience you get in OpenTelemetry.
So… but we need to be flexible, because we don't want it to just be the Kubernetes show.
And we don't want it to just be, like, optional recommendations from Kubernetes show. We need to be successful even if you're not using that, right? So, it's kind of like a bring-your-own-service definition.
Make sure we're flexible enough to handle those, and then make sure that if you're using, like, standard practices in Kubernetes, you get a really good experience.
**Joao G. (Dynatrace)** 29:31 Yeah, because, like, with the Kubernetes example, another example that I bumped the other day is, with Istio, if you use the hotel tracer in Istio, so if you configure the hotel tracer in Istio, it adds an attribute called service.istio.io. slash canonical name.
It is a canonical service as well.
Yeah, and… For example, those we, in our, in our, in our backend, we, like, when we receive such sort of things, we use that instead of the service name, for example.
So that, like, there's other mappings out there as well for these things.
And I think this canonical service from Istio takes from all of these labels that you mentioned, you showed before with this standard recommended Kubernetes.
**Josh Suereth** 30:34 Yeah.
**Trask Stalnaker** 30:35 Josh.
it seems to me, and maybe I'm just naive, that as long as our definitions align with the… as long as we define the semantic conventions, that our definitions align with what the Kubernetes definitions are.
**Joao G. (Dynatrace)** 30:53 That…
**Trask Stalnaker** 30:54 that mapping can happen later, I mean, in other way, I mean, that this group doesn't necessarily need to build out those mappings. We just need to provide This is what the mapping would be.
from Kubernetes land.
**Josh Suereth** 31:13 I… yeah, this is in line with all of the other, like, SEMCOM work we have. I think we could make a prototype that just says, here's one way that this could map from Kubernetes that gives you good observability. We don't have to make that stable to stabilize our conventions, but we should be reasonably certain it's possible, and that it fits well.
Is that…
**Trask Stalnaker** 31:37 I guess, I mean, in the… for other semantic conventions, we haven't necessarily said we need to build mappings from other systems.
We just need to implement… have some implementation, like, for namespace and, detector, or a…
**Josh Suereth** 31:59 Whoa…
**Trask Stalnaker** 32:00 Oh, like.
**Josh Suereth** 32:00 Okay, but this is… so this is where resource detection is different than other instrumentation you've written before?
I consider this a resource detection problem, right? Of, when you've instrumented before, you go in and make sure that this HTTP implementation can make spans.
Right.
Resource detection's subtly different. It's saying, if I am running in X, Can I figure out who I am? So this is basically, I'm OpenTelemetry, I'm running in Kubernetes, can I figure out what my service name is, and how does that work?
Right? And so, we have a spec around service names specifically. We don't have one for namespace.
And the instance… and we don't have one, for instance. Well, I should say we don't have a stable one, for instance.
So, that's… that's kind of what I'm… when I… when I see this semantic invention, instrumentation, it's literally resource detection in OTEL.
of… Can an SDK figure out what to fill out service name with? Can it fill out what to fill out service namespace with? Can it determine what to fill out instance ID with? Where else do we have resource detection?
**Trask Stalnaker** 33:10 From the SDK resource section, like, isn't this the same problem as getting, like, container ID?
from Kubernetes, which is something we… haven't been able to do on the SDK side, we scrape, like, proc mount info, something… But there's not, like, we're running in the pod.
I… not sure… I don't know how to get the… that information from inside the pod. Like, the collector can get all that information.
**Josh Suereth** 33:46 Yeah, well, what do we do today? We do two things.
One is, we have an environment variable that we engage with to get that information, which, by the way, the entity SIG is trying to stabilize a new environment variable that we can use for this purpose, with a resource detector that would be guaranteed to pull things from the environment, and the OpenTelemetry operator injects that environment variable.
**Trask Stalnaker** 34:07 Okay.
**Josh Suereth** 34:08 or document how users inject it, so that they can use the Kubernetes thing. That's our form of instrumentation here.
**Trask Stalnaker** 34:16 Prototype. Okay, that make… that makes sense to me.
**Josh Suereth** 34:18 Yeah.
Yeah.
I should write this down in the notes of…
**Dotan Horovits** 34:25 By the way, I have to stay with the, with the SIG, with the CACD SIG, we also had to wrap our heads around how to map, for example, I don't know, GitHub terminology to the attributes, or GitLab terminology to the attributes, and In some occasions, it wasn't one-to-one, and we needed to find the mapping, and one of the things that came up is that maybe to offer it as a… some sort of a documentation, so it's a separate doc. It won't be part of the attribute itself, but maybe a way to relay for users coming from GitLab how… what would be the equivalent So I think this is a more common challenge than you'd expect.
Whether it should be part of, as I said, the core definition should include that, or is it a side cheat sheet of sorts of something. This is a separate discussion. And by the way, there it was also challenging when it wasn't just, emitted already with the appropriate attributes. Sometimes we needed to actually create receivers that then did the translation from the, whatever, protocol and information model to the… to the canonical information model. So here we have the privilege of assuming that the emission will already be in the right, and by the way, it… it sometimes screwed up everything when we couldn't allocate, for example, in the receiver said you couldn't allocate a consistent ID for, I don't know, trades or something like that, so… some things you can't do when you're already on the collector side. So I'm just saying, it might not be as unique to this specific resource case than you'd expect.
**Josh Suereth** 36:05 Yeah, some of that instance ID thing. When we start talking about instance and instance ID, the, we talked about this a lot in the entity SIG, about we have, like, a multi-observer problem, which is, if you're outside of a process and inside of a process, you need to get the same ID.
In some fashion. You have to find a way to do that in various mechanisms. And so, Yeah, the… this actually hurts our Prometheus story a little bit, because Prometheus wants the ID to be completely external to you.
And in OpenTelemetry SDKs, our instance ID, what we were proposing was generating a UUID.
Well, how do you observe the UID remotely unless I can talk to you and get it somehow, right?
So that… that makes it rough, and I think CICD had the same problem. Alright, we're… we're down to 5 minutes left, so for next steps, what I'd love is if folks could take a look at this PR, What I want us to focus on, this is a draft.
I want us to focus on the definitions of… so first of all.
Are we still comfortable with service name, service namespace, and service instance as the three components in this… in the hierarchy we're going to define?
I want to make sure that we're all comfortable with there will be 3.
They mean different things, and then the definitions of those things. So, and literally, like, what you were saying, Doughton, with, we need to make sure it says logical? Absolutely.
let's be real nitpicky on the definition. What I'd like to have the next time we meet is, in this PR, the three things, whatever names we want to call them.
And the definitions for what those things are, that we're comfortable with.
in the context of what we just discussed, right? Of, like, there might be some external sources of this data that we need to map it to, and we need to be adaptable with that. We know Kubernetes has some conventions we can map to. We know, by default, we can use Kubernetes namespaces and deployments, because that's a reasonable thing people do.
Great. Let's make sure our definitions are shored up, and that we can move forward from there. Does that sound good?
Sounds great. Okay.
Awkward Right?
**Dotan Horovits** 38:25 on the Slack, so make sure that the wider circle has more eyeballs on the definition, so.
**Josh Suereth** 38:34 Absolutely. Next week, I want us to start thinking about the relationship between this and deployment.
Because that's the next thing I want to… I'd like to tackle. So, because I think once we have this shored up, I honestly think we're so close to stabilizing all of this, it's just a matter of… Are we comfortable with the model? Do we have some examples where we feel like this model's useful? I think they all exist, it's just writing it down.
deployment and how it interacts is the next thing I want to think about, of, like, is there more than just a name for deployment? Because right now, we have environment name. Everybody relies on that. We know we need it.
Is there anything more to it than just the ability to find a name?
That's your question for next week, besides, let's shore up these, definitions. Okay, so there's the two things.
Short-term, long-term.
Sound good?
Awesome. Thanks, everybody.
Yeah, thank you.
**Joao G. (Dynatrace)** 39:34 Thank you. Thanks, Mike. Bye.
