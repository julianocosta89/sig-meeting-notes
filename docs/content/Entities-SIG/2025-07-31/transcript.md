SIG: Entities SIG
Date: 2025-07-31
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/Z7uun2g12t8FNpj4Bj6xVWbqSqoobO7M61_rd0Cl0G25m_2ER8NUAQT67L1m9PM.qCb1pPfpKQjG5LzW
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:37 Hey? Everybody? Sorry. I'm a little late.
**Ted Young** 01:44 Hey! Hey!
**Josh Suereth** 01:46 How are we all doing.
**Ted Young** 01:49 Busy.
**Josh Suereth** 01:53 I hear you there, I hear you there.
Alright feel free to add some things, agenda. I have a few that I added, that I think are worth talking through.
all right, right, and I know folks have to leave for the browser sake. So let's get started.
1st I want to talk about the entity. N variable proposal is Dimitri on the call yet?
No.
so we'll have to do some feedback offline. I didn't have a chance to review this. So first, st I want to apologize a little bit. We've been doing refactoring the core of weaver. So I've been a bit distracted with like gutting and and replacing a lot of code. And so I did not have a lot of chance to work on the prototype for this week. So apologies there.
So I'm a bit behind. But we do have a few things to talk about that, I think are critical.
I'm not presenting yet, am I?
**Ted Young** 03:14 The.
**Josh Suereth** 03:15 Okay, so Dimitri has a specification here, for where is it the entity?
Right here we have entity references and stability guarantees, which I think this one.
We'll cover this. We'll cover this quickly, because I don't think this is contentious.
It looks like we have approval from Sig.
Just mark down. Link check is broken.
Daniel, did you have anything you wanted to say about this? Aside?
**Daniel Dyla (Dynatrace)** 04:00 Yeah, it's it's about a a line that was in the.
So if you if you look at the files that are changed, yeah. So the the heading for this says, semantic conventions defines the set of fields. Do we mean to say the set of stable fields here? Because there are other fields that semcom defines like? Is this the list of stable fields? Or is this the list of fields.
**Josh Suereth** 04:28 Okay, that's a good question.
**Daniel Dyla (Dynatrace)** 04:33 Think it's supposed to be the list of stable.
Well, I mean, like it's it's hard to say.
It's it's supposed to be the set of fields in L. 2 P. That semcom will have stability guarantees about.
Yeah. So maybe we should say.
Yeah, I guess defines a set of fields is fine, because then some conf also defines the stability of those fields. So it's probably fine, as is.
**Josh Suereth** 05:01 Okay, cool.
Right? So that was one that just I think that one's actually pretty good to go the other one that I just wanted to talk through. We had we discussed this briefly in the in the specification, Sig. I think the main concern I need to respond to to mark here. The main concern about this is the whether the this is a configuration, environment, parameter or not, which which it is not. So we have to make that clear. So the fact it's listed under SDK environment, variables and configuration. I think this should be removed because it's not actually configuration. This is an environment variable for passing entity. Id from like ownership systems.
Right? So
**Dmitrii Anoshin** 05:53 But that was one of the things we, Dimitri, were you at the spec meeting?
No, but this is just a reference we added, to that reference to all of the other environmental variables, definitions. So I didn't add anything in the configuration, anything new.
The the biggest part is written in specifications, slash entities, SDK environmental variables.
**Josh Suereth** 06:20 Yes.
**Dmitrii Anoshin** 06:22 So we.
**Josh Suereth** 06:22 But so so I think.
**Dmitrii Anoshin** 06:25 As a whole, like all the definitions of environmental variables, if we want to move it somewhere else, not for.
**Josh Suereth** 06:31 Yeah, I think I think this thing has to be somewhere else. So the the reason I think it this confused people is this, is in the configuration spec. And so people thought it was about configuration.
But it's not about configuration. It's about how to pass entity id when you're like a Kubernetes right.
**Dmitrii Anoshin** 06:48 Yeah, but everything else is also here. All the other environmental variables are here as well.
**Josh Suereth** 06:52 I know, I know. Like, that's the thing we have to clean up in the spec at some point like we, we probably need to sort that out. I think that's the main blocker to your Pr.
**Dmitrii Anoshin** 07:02 But why is this blocker for this? Pr, and I don't understand, because, like, I'm adding environmental, variable to the existing place where every other environmental variables are defined. We can have an issue to address like everything here separately.
But how is that related to this? Pr, that's that's my.
**Josh Suereth** 07:25 So so the the reality. We put a moratorium on this file.
We're not adding environment variables on this file until the configuration Sig is done. And you're right that this is where we list other environment variables. But it's not quite where we list other environment variables. When we do environment, variable context, propagation. Right? So when we spend trace ids over environment variables for process forking that environment variable is actually not listed here because it's not a configuration environment variable. It's a propagation mechanism for data.
**Dmitrii Anoshin** 07:57 What you're specifying is a propagation mechanism for data as well. So I think similarly, it should not be in this file.
I see what you mean. Isn't it similar to hotel resource attributes in the.
**Josh Suereth** 08:09 I think re hotel resource attributes. I think also shouldn't be in that file because I.
**Dmitrii Anoshin** 08:13 Don't!
**Josh Suereth** 08:13 It's configuration. It's a propagation mechanism. But.
**Dmitrii Anoshin** 08:15 Hotel service name in that case as well. Right.
**Josh Suereth** 08:18 Also, what.
**Dmitrii Anoshin** 08:20 Hotel, service, name.
**Josh Suereth** 08:22 Yes, yeah, I think honestly, hotel service, name and hotel resource attributes. Both really are about propagating information as opposed to like a configuration. But you know this is this is a already exists that's already considered a piece of configuration. So.
**Dmitrii Anoshin** 08:41 Okay.
**Josh Suereth** 08:41 We can move on. But you like. You can imagine the config file has a way for you to specify a service name right?
**Dmitrii Anoshin** 08:50 Yeah.
**Josh Suereth** 08:51 But the environment variable we're trying to create is like, how do I, as Kubernetes, or as a cloud provider, give you an identity that you can use in opentelemetry that tells you who you are and what you are, instead of you making an Rpc. Or inspecting a bunch of other stuff like I want to push it to you in an end. Variable.
**Dmitrii Anoshin** 09:10 Okay, I see on what you're saying. You're saying that that is where all of the confusion comes from. From the other people who are commenting that? Why is this environmental, variable? Not a configuration on the SDK.
**Josh Suereth** 09:24 So I think if you remove it from here. And if we call this basically instead of calling it just SDK, I think instead of calling it an SDK environment variable, if we call it like a specifying entity information via environment variable. That might work. But it's it's like the other thing that's missing here from the Otep. That confused people is, you know, there will be a way to configure whether you use this environment variable which is independent of the environment, variable itself. Right? So the the fact that we have a entity detector called environment variable entity detector and you can configure that that's missing from the Pr, but I think we can just put that in the description and move forward that way.
Yeah. So those.
**Dmitrii Anoshin** 10:09 Through, the.
**Josh Suereth** 10:09 2 things. Go ahead.
**Dmitrii Anoshin** 10:10 And another question, do we still want to have an option to configure it through the Yaml for the Sd. Keys?
**Josh Suereth** 10:17 I I think we should configure when and how it's interacted with. So if someone wants to disable it, they they can just don't list it right.
**Dmitrii Anoshin** 10:25 No, no, I mean like hard code and like entities in the config, instead of passing the environmental variables.
**Josh Suereth** 10:37 That's a different question. Yeah,
**Dmitrii Anoshin** 10:41 That's what people are commenting about like. Hey? Why are we coming up with this new like Schema to define entities if we can pass it in as a yaml instead.
**Josh Suereth** 10:56 Yeah, I I don't know how people here feel. I I am.
Personally, I'd prefer if we didn't have that initially. But I think there's probably a use case for it that we'll have to have it.
**Dmitrii Anoshin** 11:12 Yeah, just, I believe people don't like that. We we're coming within with a new language, essentially, to to encode this information instead of using Yaml.
**Josh Suereth** 11:24 Yeah, I think if if we if we walk through the bugs in the description, I think people understand when we describe what it's used for. But if you come at this thinking, this is configuration, then it's like, Why are you defining new configuration? Just use the existing Yaml one.
**Dmitrii Anoshin** 11:38 But if you.
**Josh Suereth** 11:38 Come at this thinking. This is a way to propagate identity between a a owning system and a system that's running.
It looks. It's a very different problem. Right?
**Dmitrii Anoshin** 11:50 Yeah, but but you still can propagate it through the configuration. Yaml. Right? For example, in Kubernetes you would attach another config map and reference that.
**Josh Suereth** 12:02 So so yeah, think about someone who doesn't own the program pushing this through. Right? So like, let's say, let's say, a Kubernetes operator wants to push this this environment variable down right?
Or let's say, a Vm, even so, I don't know if you've seen some of the like Dasho stuff where they they trick. Vm, startup to pass information down. How do I safely say, hey, I discovered identity, and I want to run this python system. I don't know anything about the python system, but if it's using open telemetry, I want to tell it. Here's your identity.
So so like, we want a way to do that. That is kind of independent and and hard to blow away what the user intended.
which is why I think it needs to be separate from config. So if the user says, I don't want to interact with that identity, ever they can figure it away if they want to interact with it. They say, yes, I want this environment detector for for resource information, right?
If they have the environment detector for resource information, things like the Kubernetes operator things like dash, O, just flush out the environment variable and go forward.
Being able to provide an actual file that you read. Not all environments can really do that. But most have environment variables. So it's kind of like a I don't know. That's that's kind of why, I'm thinking environment variables the the better way to go here. But there's there's obviously trade-offs, and we can talk through it. It's just I. I don't think this should be config, and I don't think this should be a file.
but happy to hear other thoughts.
**Dmitrii Anoshin** 13:49 Okay, maybe this is, we can start with this, because likely it's unavoidable. We cannot have any other solution that covers all the use cases. And later, if we can figure out something layers, we can provide as an option.
**Josh Suereth** 14:06 Ye, yeah. And I think everyone's already using and variables to do this passing today.
It's just we're giving them an option that has less chance of conflict. So like it's, we're basically trying to make it safer to do so.
**Dmitrii Anoshin** 14:22 I'm good.
**Josh Suereth** 14:23 Yeah, okay.
so, and by the way, I didn't comment on this. But I did review the syntax and grammar. I think the I have that one comment which I'll add, which is, I think, we need to allow, preceding semicolon, but otherwise this looks great.
**Dmitrii Anoshin** 14:39 Okay, I did that preceding semiconds. I addressed that feedback from you from the last call.
**Josh Suereth** 14:47 Where is the preceding one?
**Dmitrii Anoshin** 14:50 Oh, in oh, okay, okay. I didn't update the grammar. But I did. Working around that.
**Josh Suereth** 14:57 Oh, okay, yeah. Okay. Yeah. Yeah. Yeah. I see that. There. Yep.
Gotcha skip. If it's empty, yep, perfect. Cool. Any any other thoughts or concerns around this. This. Pr from folks.
All right.
So clearly disambiguate from config clearly denote use. Case for passing id via env system ownership.
Okay.
alright, I'm gonna just just because we don't have a lot of time. I'm actually gonna skip to this one quick. This is kind of a heads up.
There's a Pr from some of my coworkers here where they actually want to expand semantic conventions around a kind of kind of descriptive attributes for service if you will. So this would be understanding, like application, understanding an owner for that application, understanding the sensitivity of data that application works with. That's more of a security use case. That kind of is bleeding into observability and then like deployment environment. So what they're looking at is trying to form a sig that would own to some extent the service, entity, the deployment, entity, and other entities around that kind of venue and define, like what those semantic conventions are, and kind of resource detectors that could pull those from different systems of record.
You can take a look at the proposal, but I wanted to kind of call that out to make people aware of that. I think it's it's kind of related to discussions we've had, and I think there'll be some interesting topics that they bring up with some of the things they want to do. I think if we look at the proposal, it calls out some of the yeah deployment environment service name. They want to have a notion of an owner, a cost center, a business unit.
data sensitivity data category and criticality.
So yeah, I I've been kind of talking to them and guiding them and explaining to them like what what's going on with the Entity Sig, and how how this works in open telemetry. So far, there's there's a couple of folks interested. You can see the names here, but I wanted to make people aware of this.
It's a it's another interesting use case for us. Right?
Cool thoughts.
Anyone interested in.
**Dmitrii Anoshin** 17:44 Was the status with deployment dot environment. Was it renamed to deployment.environment.name or.
**Josh Suereth** 17:53 I believe it is either currently renamed deployment.environment.name, or it was renamed back to deployment. Anyway, that one is kind of unstable right now. So I think it. The key is, it has to be stable.
I also, if I remember talking to them, deployment that environment might have name and something else in it. So they're they actually want to stabilize the set of attributes. Not just the one.
Yeah, anyway.
**Daniel Dyla (Dynatrace)** 18:21 This seems extremely broad to me.
like I I guess I haven't read the proposal in detail, but like deployment, environment and service name seem like they're like. Those are already handled by other groups like service names in the spec, isn't it? And.
**Josh Suereth** 18:40 Yeah, yeah, did you?
**Daniel Dyla (Dynatrace)** 18:41 It seems like an extremely broad group like the, and the name of it like resource metadata standardization makes me think that like that there's it's not scoped to anything really.
**Josh Suereth** 18:59 So I can cover that a little bit. The the. There's a document that I don't know if it's linked to from here that I read that was shared with a few hotel folks. Where the proposals actually to have service dot owner service dot cost center service dot business unit is the initial proposal that will probably come out. What they're calling out is, so this list is, they looked at the set of tags that people actually have on Gcp.
right? Like the like, you can, you can tag a Vm and say, here's a a user base tag. And then, like data that accumulates around that has that tag on it?
What were the common set that they had? And what do they want in open telemetry? So that, like, if we produce data. We can attach those tags to it.
That's that's kind of where this is coming from.
So this is just the set of hey? Here's the things that we see that we think people want and want to share. Can we make a standard around it? What should it be? An open telemetry. The actual names and open telemetry will be okay. Owner, is that service owner? Or is there like a whole entity for owner that has, like a cost center business unit, that kind of thing that we that we have, that we attach to resource.
You know. What what should that be? They they need to go through like a kind of a scoping design phase there.
But they they saw in in this tag system that we have that like users are doing this today. And we want to be able to express this in open telemetry. So people can use that data.
I don't know if you've seen like. I think for Amazon and azure.
We have resource detectors that will actually pull custom tags from their storage systems of like tags that exist on vms. And there's this notion of like kubernetes, annotations that people can add like specific labels.
that the Kubernetes Sig just has blanket. All of the tags get dumped with Kates dot annotation dot whatever in resource.
Right?
So they're trying to ask the question of if you are labeling resources. Should there be specific names for those labels, for things that are important enough for us all to agree on the name.
I think it's an interesting question, but that's that's the scope of that Sig.
**Daniel Dyla (Dynatrace)** 21:14 Okay.
**Josh Suereth** 21:15 Yeah, I'm raising awareness, because I think now that I described it from my point of view.
We'll get much better feedback on that. So please take a look.
I think it's highly relevant to entities and would love to get people paying attention. I think it's probably the most aggressive entity based. Sig, that I am aware of. I think the Kate's 1 is a lot simpler and well well scoped. Yeah, go ahead.
**Hunter Sherman (SolarWinds)** 21:45 Is that the link that you dropped here in the doc on the screen.
**Josh Suereth** 21:48 Yes, yes, that's the link here.
**Hunter Sherman (SolarWinds)** 21:50 Great. Thank you.
**Josh Suereth** 21:52 Yeah.
**Ted Young** 21:53 I mean, I think my only comment is, I think the term resource is getting used in like multiple different ways in this.
Pr, a little bit right? Like, I think sometimes we're talking about hotel resources, and sometimes they're talking about cost center stuff.
So like, I think part of the confusion is calling stuff like resource. Metadata, like resources, are already metadata. So maybe just the only suggestion, I would say, is like maybe just refactoring this proposal, and Sig to be like focusing on cost, center or business, something right like like, pick a pick a domain like that and say, we want to figure out this domain.
**Daniel Dyla (Dynatrace)** 22:33 Yeah, that's kind of what I was getting at, too. It's just like it. Seems like they're trying to eat the whole elephant all at once.
**Josh Suereth** 22:39 Yeah, and.
**Ted Young** 22:41 And we just prefer in general to, especially with Simcom 6 to be like, just pick one domain. And when you're done with that one, you can move on to the next one. There's no excellent.
**Josh Suereth** 22:49 Make a make a sig. That's yeah all encompassing.
**Ted Young** 22:53 You know, long running kind of thing.
**Josh Suereth** 22:55 Yeah, yeah, I'm I'm happy to give them that feedback. I will say that basically, they're relatively new to open telemetry. So some of the like. What is a resource? What is metadata? They just know people are asking for this and don't understand open telemetry. So we've been kind of teaching them so feel free to make comments like that like they're very responsive. Yeah.
cool.
Awesome.
Alright. Let's talk about the Api SDK proposal and discussions. I I think I think we showed this. I had a let me copy it from last time is this.
That's the specification. Pr, that's not it.
I have a pull request against Ted's repo that I'll pull up.
**Ted Young** 23:43 Hmm.
**Josh Suereth** 23:43 Of changes, open telemetry specification.
So yeah, the the main problem we're running into with the prototyping if you haven't seen this, I thank you. Thank you, Daniel, for reviewing this. Basically, what we do is this is expanding the initial proposal to only have an SDK to have an SDK and Api.
This is prototyped out in Java.
It adds an entity provider Api that has add or Update, add or replace and delete.
We talked a lot about that last time and about ownership. What what was added. And this is where things start to get awkward is the SDK.
Has a listener interface to kind of tell the SDK, hey? Things have started. Things are stabilized. Here's what things are. So this adds a resource initialize event. So the idea would be at startup. People are modifying entities and resource instrumentation is, and it's an open ecosystem. So like there's there's a set of things that go at some point. In time. We push an initialization state and that is the signal to all SDK contributors.
You're good to go. You can start exporting data.
Resource has been initialized. Okay, that works how we actually decide when to fire. That event is where hell breaks loose and things get kind of awkward.
I spent I spent way too many hours chasing down concurrency not necessarily bugs, but documentation differences between how Java's completable result thing works versus how it's documented. Because It was like it was.
It was returning after everything failed instead of after 1st failure, for example, and I couldn't figure out what was wrong. And then I realized the implementation's broken or sorry the implementation works as it was designed. The documentation was updated without the implementation matching it. That's actually what happened.
That kind of thing, and it's it's it's getting awkward.
Go ahead, Ted.
**Ted Young** 26:01 Yeah, I I just had a question. I feel like, I mean, every SDK today has a solution to this problem in the way they want to do it right like like sdks have some set of like, you know, resource detectors, and some you know, way of like scatter, gathering them to know when they're all done.
**Josh Suereth** 26:26 The the way this is done today for most Sdks is they have. They have a notion of a resource object or some kind of resource thing. They fire off these resource detectors right? And those resource detectors kind of like, build this object and then push it into the SDK. So like for Java. No SDK can start until the entire resource is done today.
which means it, and it's a completely different Api than like one that would be exposed as an Api, so like the entity provider Api you'd use at Runtime could not be part of this, because you can't actually construct a provider until resource is complete in the way Java works. Daniel, I assume your hands up to explain some Javascript things.
**Daniel Dyla (Dynatrace)** 27:12 I can if you want me to. I was gonna say, did what what Ted said is true. But I think with the entities. It's fundamentally different, because we now have to distinguish between with resource. We knew we always wanted everything, and the 1st data point that was emitted needed the full resource.
Now with entities that's not necessarily true. An entity could be modified after startup or added after Startup. And when you have an entity detector that detector needs some way to let the SDK know like this, entity is important and needs to be resolved fully before any data points are exported.
But this entity is like, you know, an asynchronous entity, or whatever it is you want to call it, where it's like. It's added after the fact. And potentially the 1st few exports don't have it or possibly like some descriptive attributes even aren't required on initial export. So now we have to distinguish between initial export entities and asynchronous entities.
the the Javascript specific part of it I I wasn't going to get into, but since you mentioned it, we handle it slightly differently. The SDK fully starts up, everything is just potentially resolved, and then on export, we resolve. We wait for the export until the the resource is fully resolved.
So the SDK itself is started up. But if any SDK components read from the resource they're reading potentially unresolved resource attributes.
**Josh Suereth** 29:08 Hmm.
I mean this. This would make it explicit with the way this works of basically, there would be an explicit event that you'd fire to people to say, hey entities. Now, initialize, you can read it.
The main. The main problem we have is.
I guess it's it's it's like a set of decisions we have to make one is, should SDK startup use the same entity provider api that you use at Runtime.
because now we have this dependency problem of the Api has to be the provider and see provider has to be available before the rest of the SDK, right? So I need the the ability to construct a provider, pass it to instrumentation that will do resource, detection.
**Ted Young** 29:54 Yeah. And then eventually fire out. Okay, everything's done.
**Josh Suereth** 29:58 The prototype I did in Java was when you construct the entity provider, you give it a list of functions that return a promise or a future.
and it will, it will pass into those functions. Hey! Here I am. Go, start! And when all of those features are done it will fire the entity initialize event.
Right? That's how I found the failure problem.
But and and that that works. It's a little interesting. And I was able to make that work all the way through the Java SDK.
I am not certain how that scales into other sdks like Javascript, and it's kind of interesting looking, but like, if we're comfortable moving forward with that, I from a from a listener standpoint. This made sense to me of okay, the SDK has a like entity provider has some magic.
Where, when you construct it, you're going to say, here's the things you do at Startup that you're going to register with it. When you create an entity provider.
it's going to have a phase that it goes through, and it will have a a tracker to understand when all those things are done.
and when those things are done it will fire the entity initialized event. Any listener that's registered during that phase doesn't get any information until that phase is done. Then you get a initialized event.
If you add a listener in the future, the initialized event comes out immediately of here's what I have right now.
Yeah. So that that's all implemented. That's that's that's relatively easy to do. And then we get state and delete events on changes.
Are we comfortable with that? As like a startup proposal going forward as we start prototyping like, I, I wanna do this and go unless someone else has time to do the go, please, cause I think we have to figure out. Go early for this Sig. First, st because that's always when we wait for go. We run into all sorts of problems. So I want to do go early.
I think what I've defined will work in Java. From what I understand of promises in Javascript. And Daniel correct me if I'm wrong. Does this sound reasonable for Javascript.
**Daniel Dyla (Dynatrace)** 32:09 Yeah.
**Josh Suereth** 32:10 Okay.
So I think I want to try this out and go in their concurrency model and see how it works there.
But yeah, that's that's the big open design question here that I have of like, do we? Is this what we want to commit to and move forward for? SDK startup?
**Daniel Dyla (Dynatrace)** 32:27 So does this depend on the user configuring the SDK to say, these are the set of detectors which are important for startup rather than the detectors themselves, saying, I am a detector that's important for startup.
**Josh Suereth** 32:42 Yes, exactly. The user has to have a configurable list in the SDK, that says, here's my startup detectors. Anything else is not a startup detector.
**Ted Young** 32:53 Yeah, I totally agree with that.
**Josh Suereth** 32:57 Okay.
**Ted Young** 32:58 It. It kind of circles back to this thing, being a little bit more like glue code and a messaging system.
Then there's like all inclusive thing.
I think that will help given the fact that every SDK currently has its had to figure out its own way of dealing with that initial set of resource detectors. I think it will probably work better in most languages for it. This proposal to not have a lot to say about that other than you know. The SDK figures out how to resolve all those things first, st you know, and then it tells this thing that it's done doing that.
**Josh Suereth** 33:40 Okay, I mean cool. I mean, if we're if we're agreeable, I need to do a little bit of cleanup on the prototype to fix some of the tests, and I might be making some.
I need to go to the Java Sig to ask them about the concurrency stuff to see if they're willing to support. Some of the patterns we want here. But yeah, I think I think we can move forward. With that I can update the spec. I'll update the prototype and we can start working on. Go.
**Ted Young** 34:09 As as a just a small aside Josh, I can totally see in some languages. You know, synchronous convenience methods getting added to this thing as well. But I also think there's like a foot gun there, especially when it comes to like data access methods having both listener patterns. And you know, synchronous patterns for getting stuff. So I just want to call that out. That's that's a situation in the past where I've seen stuff potentially get out of order issues. We've got 2 different.
**Josh Suereth** 34:47 What I what I created, Ted, and don't hate me. But I created a listener that just stores the latest resource and blows it away when it gets a new one and serves it up to that part of the SDK, that's like, that's literally how I implemented the Java side. So there's just a thing.
It has an atomic reference to a resource. When it gets a, when it gets the event, it blows away the atomic resource with the updated one, and it just anytime you ask for resource across the job. SDK, you get it from this thing. So that's like the baseline. Yeah.
**Ted Young** 35:16 Right. If you joined later you would get that initialized event. But the thing that popped out of it would be the latest resource if a bunch of things that happened since then. Yeah, totally.
**Josh Suereth** 35:27 Yeah. And there's there's a and there's a fun wait condition. So that's the other part is how to defer SDK, startup successfully.
The big question we need to answer next. And if you guys want to drop for the browser sake feel free, because I know that you have that.
**Ted Young** 35:41 Oh, shit! We're like, Yeah, we're already late. I gotta go.
**Josh Suereth** 35:44 We'll see you guys so we can talk about that with the rest of us here. But the the next big problem is, what do we do in the SDK?
If resource like like, how long do we wait for resource to complete is another way to phrase it.
you know. Is it a like? If somebody tries to export data, some of our exporters? It's like, when I get to a buffer I try to export. How long do we delay before we say you know what resource detection broke? I need to report this data. Is that a thing we allow is that a thing we crash. How do we want to handle failure? There.
**Daniel Dyla (Dynatrace)** 36:21 Yeah, it's required, I mean, so we have the sit, because.
in most languages you have the convenience of being able to just block startup in. Js, we don't. So we already have this problem. And right now we and we have a timeout where we just like we call it, and we say, sorry if you resolve after this point, like or crash, or fail, or whatever nothing happens like they, because the resources defined as immutable. We just have a timeout. So you have to finish. And it's it's not very generous. Because it affects startup time of like export and like in lambda functions, and and stuff like that, like the whole process from start to end, may be measured in milliseconds. So having a generous timeout is not is not conducive to that But most resources, I mean almost all of them honestly, are synchronous anyways, or are calling like a local asynchronous endpoints like they're almost all really fast. And I know that that's an enormous generalization to make for the few like moving forward into the future.
**Josh Suereth** 37:35 I actually think we should make it a requirement like if if your observability startup it could. Where's what the most important observability in my mind, there's 2 pieces right startup and crashing.
The second, most important is basically your steady state. What's your saturation? Your latency, that kind of crap, right? But startup and crashing are very important, and if we cannot handle them, it's a problem. So I think, having an extreme limit there of like, okay, this all has to complete here, or we can't provide good observability. That's reasonable to me.
**Daniel Dyla (Dynatrace)** 38:07 We also have now with entities. We have an escape hatch that we didn't have with resources, which is to say, they'll just be added later, like if they take too long. So if you have an initialization entity, like whatever important for whatever we want to call them.
and it takes more than I don't know half a second. Whatever we define our ungenerous limit to be, then it's like sorry you're just not included as a part of the initialization process. But you'll be tacked on later as a new entity.
**Josh Suereth** 38:41 Okay, yeah, yeah, that sounds good.
Cool. So.
**Daniel Dyla (Dynatrace)** 38:48 The browser, saying.
**Josh Suereth** 38:49 Yeah. Let me type up the straw man here. So we have this straw man SDK entity provider will have a registration of startup entity detectors.
When these complete the fire initialization events defers sending data until this completes.
give it a hard time limit on completing and force initialization.
After that limit. Okay, cool. Anyone have concerns with that going forward.
Nope, alright beautiful. What is? Does anyone else have any other topics that was like the big thing I wanted to talk through and and make some decisions on for the proposal.
If not, I'm going to open up our to do's, and we can go through those quickly. Sound good.
Alright. Where do I have that? That is Project Board.
Is this readable? By the way, I have, I'm I'm in a new location. So my laptop is in its tiny mode. Are you? Are you guys able to read what I'm showing? Or do I need to zoom.
**Dmitrii Anoshin** 40:24 That looks good to me.
**Josh Suereth** 40:26 Okay.
cool. All right. So in progress. Contradiction between resource and see attributes. I think Daniel's on that that has merged. We'll follow up with him later support for new resource and see references and proto message in the collector. Any updates here? Or do you need any help? Dimitri?
**Dmitrii Anoshin** 40:45 This, this is collector work. Yeah, I not much progress. I updated one exporter and like looking through others. But there's no other like interest or help from any anyone else. So yeah, get us slowly getting through this essentially.
**Josh Suereth** 41:03 Okay. And each of these things here, like somebody could sign up for.
**Dmitrii Anoshin** 41:08 Right right, and I put some labels when applicable. Someone signed up, but haven't done anything for one exporter. So.
**Josh Suereth** 41:17 Yeah, I do that myself.
Okay, anyone here who's interested in doing any collector work.
Oh, hey, we have someone else who wants to work on it. So let's let's take some people up on this.
**Dmitrii Anoshin** 41:34 I'll I'll reply to to that person.
**Josh Suereth** 41:38 Yeah. And if there's if there's ones that are ideal, anyone here in this meeting who's interested like, please please do. Because this is this is important for us to kind of move this across the finish line.
**Dmitrii Anoshin** 41:50 The one thing I want to discuss with. Maybe I'll discuss with maintainers, maybe with Bogdan. It's unclear to me how we do the like the recipe data interface right?
And the pdata interface. It's just a wrapper or Protobuff. Essentially.
I'm thinking, if we should, we have like interface for mutating the resource. So I'm thinking, if we should update current resource interface to like, whenever is, it's been updated in a way that it removes an attribute and something like that or renames the attribute it. That change is reflected in the entity.
Like, we don't have anything like that in the P data. So P. Data is very straightforward, but maybe we can have it in in like for entity. I don't know to keep like the data consistency, right?
So whether we do it in Pda, or we introduce some other like helpers on top of it.
**Josh Suereth** 42:58 This is, yeah, I at at a minimum. I think any Ottl function has to do that.
**Dmitrii Anoshin** 43:05 Yeah.
**Josh Suereth** 43:06 But that's also expand expanding ottl to like handle aggregates in addition to keys is really exciting.
I can share with you a whole bunch of dead prs I have to ottl, but
**Dmitrii Anoshin** 43:27 What aggregates do you mean.
**Josh Suereth** 43:29 So like, can I refer to the entire pdata metric as a thing in Ottl? Or do I have to go into a key of something underneath it?
**Dmitrii Anoshin** 43:43 It's based on context. Right? If you have a context, you in metric context, you operate on the whole metric right?
**Josh Suereth** 43:52 Yes, yes, but it's inconsistent with when that's allowed and when it's not like it's really inconsistent. So it's like unclear when you can and when you can as a user. So I went through and tried to like update everything to allow contextual based work. But then all the functions don't work because they're hard coded to specific getter types.
Yeah.
**Dmitrii Anoshin** 44:12 Have a discussion if you can. If you have an issue against that, that would be that would be great. I'm not. I'm not working on Htl. But there are people who are actively working on that like.
**Josh Suereth** 44:22 Yeah, yeah, I should. Probably I don't have. The problem is, I don't have time to meet with the collector folks, because of all the other things I do.
**Dmitrii Anoshin** 44:31 You don't need. You don't need to meet. You can just file an issue and.
**Josh Suereth** 44:34 Oh, yeah, I filed issues like, 2 years ago.
**Dmitrii Anoshin** 44:38 Sure. Okay.
**Josh Suereth** 44:38 Yeah, I I can show them to you. It's fine. Yeah, it. It's anyway.
We can talk about that later. But I think I think the main thing we'd want is like at a minimum. Ottl should handle that at a maximum. If P data ken, I think that would be ideal. Yeah.
**Dmitrii Anoshin** 44:57 Yeah, I believe any mutation of the attribute. We have other processors that do that. So all of them, I believe, needs to have consistent state of the entities of the resource and entity.
Yeah, so I'll probably create another helpers and helper and apply it to transform processor and others.
**Josh Suereth** 45:24 That that sounds awesome.
Yeah.
and I think you finished the resource model for version stability. We already talked about the environment variables which is making good progress. So I think everything here is making good progress.
The prototyping around entity Manager Otep, that's the other thing we talked about so deciding how entities should be supported by schema files. I have not.
we for context. I think we're going to defer this a little bit.
semantic conventions. The tooling Sig is actually creating a version, 2 of schema.
So the file format will likely change.
and when we do that we can account for entities, because entities are part of the V 2 schema in semantic conventions. So just for reference, I think this is going to be deferred and and we'll handle it over in that Sig.
marking semantic conventions resources as stable. This is, basically, can we mark like the Kate's entity? Semantic conventions is stable. I personally feel like we talked about this a few times, and I think this is done. I'm waiting for one of them to mark themselves as stable before we close this.
should we just close it? So we don't talk about it, or have it there in the future, or like, how close do we think the Kate's folks are to being to stabilizing their their entities? The set of entities they have in the resource attributes.
**Dmitrii Anoshin** 46:58 I believe. There it's it's on the roadmap, but it's not something very close. The whole sick. The whole goal of the sick and working group is to have semantic conventions stabilized for the whole branches.
**Josh Suereth** 47:15 Yeah, yeah, no, no. I know what this was about us, unblocking them and being able to be able to mark them as complete, and have all the capabilities we need in place.
**Dmitrii Anoshin** 47:27 Oh, okay.
**Josh Suereth** 47:29 So.
**Dmitrii Anoshin** 47:31 I think we can move it to done.
**Josh Suereth** 47:33 Yeah, I think I'm gonna do that because I I don't think we're planning to do anything else here. I'll denote this. Yeah.
submit to conventions.
Resource.
Okay, cool.
Can collector processors differentiate, remote versus local. This was a draft. Is this still needed?
Dimitri.
**Dmitrii Anoshin** 48:23 And I, I mean, there are yes, some, like different processors, implicitly differentiate themselves by remote or local. The I believe Tigran is asking whether we need to do it explicitly, and that's something that we can do, I believe, and probably should. So let's give it for now.
**Josh Suereth** 48:53 So we should do it. Okay, good. That's what that's what I want to know is like, should we keep it? Should we get rid of it. Entity, semantic conventions for hosts.
I think we moved this over to Is this is this something that should be in the system? Simcov. Now this is about, what should Host Id be.
**Dmitrii Anoshin** 49:19 Right, we can probably remove it from Project.
**Josh Suereth** 49:25 Yeah, let me let me take it off of entities. And you guys have, you're under.
**Dmitrii Anoshin** 49:34 If you go. If you look for system, I believe we should have it.
**Josh Suereth** 49:37 Yeah. Why is it not showing up for me.
**Dmitrii Anoshin** 49:39 Okay.
**Josh Suereth** 49:40 Systems, semantic convention working group. There we go.
You're in the same repository, but we'll go there.
It's the same one. Okay? And then we'll take this out of entities. For now.
Okay, cool and then service. Instance this one, this one I based on, based on other things. And I'm thinking, we don't have anyone in semantic conventions who owns the service namespace basically, only the general maintainers do. Which means when we want to make changes to it. It's really high friction.
That's, I believe, as intended, because of how important services to like the Prometheus ecosystem to all the observability vendors and that sort of thing.
But this, nominally, I think we're at the point now where this decision of should service and service instance be different entities. I should probably open a bug for semantic conventions and talk about this in that Sig. I think that's no longer in the domain of this Sig. Does that sound right?
**Dmitrii Anoshin** 50:52 Yeah, if we have that sick that can handle that. But it's not clear which seek is gonna handle it.
**Josh Suereth** 51:02 Well, this goes to who owns service in open telemetry like what sig
**Dmitrii Anoshin** 51:09 Yeah, I still think it's probably better to keep on our side, for now, at least because it's a. It's a good example of how we model.
and it's going forward. I would say that in service, instance and service can should be different.
**Josh Suereth** 51:25 I, I would agree. Honestly, yeah, okay. That will be a fun, a fun thing to make. I'll leave it here, and we'll leave it on a to do we're at 8 min I don't. So everything else we're working on is related to this entity manager. Otep. About getting SDK startup, for example.
which we already talked about ad nauseam. So I think we covered what's important there. So good, we're making progress. And all the things we need to do. Let's do a quick discussion on time.
When can we meet, I'm thinking. Given the browser Sig is highly dependent on what we need, and we have a lot of crossover between the 2.
I'm thinking about moving back to weekly.
but with a 30 min meeting.
How do folks feel about that?
**Dmitrii Anoshin** 52:26 That sounds good to me.
**Josh Suereth** 52:28 Okay. The problem I have is this is at the same time as the profiling Sig, which is at a stage where I need to be attending to help guide their protocol.
I'm the I'm the Tc delegate to profiler. So are we okay with doing this like this time every other week for 30 min, and then I'll put a like vote for the 30 min every other week. So we would actually change what time we meet every other week.
Is that okay? But by everybody.
**Dmitrii Anoshin** 53:05 That's gonna be complicated.
**Josh Suereth** 53:09 Yeah, I know. Okay. The other thing I can do is I'll talk to the profiling sake, and maybe I just skip the 1st 30 min every week, and come here, and then go, and only give them 30 min for their thing that might work out too.
**Dmitrii Anoshin** 53:22 Yeah.
**Josh Suereth** 53:23 Cool.
Alright, I'll put. I'll put some stuff in chat, and we'll talk about it there. In the meantime. Thanks. Everybody. Does anyone else have topics before we call it.
**Nathan Smith @ Elastic Observability** 53:37 Real real quick, since we were just looking at it. The I notice now in in the model for service we have, I think it has. Yeah.
it has. Everything is identifying except for service version. I think.
**Josh Suereth** 53:57 Yeah.
**Nathan Smith @ Elastic Observability** 53:59 So I mean, I guess that's the the point of that issue is to to sort that out.
Since you, I guess each service instance would have to be a different entity.
According to this definition.
**Josh Suereth** 54:18 Yeah, yeah. So there would be one entity which would be service where the name is identifying.
And the namespace is identifying.
And then there'd be a second entity called Service Instance, where that Id is identifying.
**Nathan Smith @ Elastic Observability** 54:38 Is there work to add the attribute role to these tables?
**Josh Suereth** 54:44 Oh, yeah, sorry. There's work to. And this, this is something that if somebody wants to help me with, that'd be awesome. We're moving all the entity stuff to a registry. We just have to figure out how to get how to get the data from the Markdown into this registry before we fully commit and move.
But we do have the data of whether it's identifying and whether it's descriptive.
**Nathan Smith @ Elastic Observability** 55:09 Oh, I see. I see it there. Okay.
**Josh Suereth** 55:10 Yeah, it's. And and this, this, all of this is auto generated. And if somebody wants to like, change the mark down and make it look pretty, please do. We did the bare minimum to get it all there, and to make sure the models correct, and we can reformat as we go. But this, this one will show you what's yeah? Name namespace. Yeah.
**Nathan Smith @ Elastic Observability** 55:29 I think this one just has so many footnotes that it makes that it makes it confusing that those 2 tables are right next to each other.
**Josh Suereth** 55:36 Yeah, agreed if there were a way in Markdown to put them side by side, that'd be cool.
**Nathan Smith @ Elastic Observability** 55:44 Okay.
**Josh Suereth** 55:45 But or we could put on, we can actually, one thing we could do is we could update the template to put all the footnotes at the bottom.
so like we can, we can just collect all the footnotes and put them below both tables. If you look, I can show you the the template it's easy to modify.
There is an entity readme.
And right now is that the right one? Or is it entity namespace? It might be entity namespace.
Yeah, right now, we do identifying attributes, and we generate the table. And then we do descriptive attributes, and we generate the table. If you look at this table generation, Macro, it basically makes the table makes footnotes. We could use a higher level macro where we don't write the footnotes immediately, and then just put the footnotes at the bottom.
**Nathan Smith @ Elastic Observability** 56:35 Yeah, it's probably fine as it is.
**Josh Suereth** 56:39 I mean, it's it's better than nothing. This is the problem. It's better than nothing. And my theory, with all Ui design is, I'll get something working that's ugly enough that someone hates it and makes it look pretty, because I know that's not me. I'll try, and I will get really infuriated at how bad what I make is, but if I make it ugly enough, someone else will make it look pretty. So that's usually my strategy. Just fy, if you ever see ugly uis for me, that might be why.
they're functional, and I need someone to help me make them pretty cool any other thoughts or topics.
Alright, thanks, everybody.
I'll check check chat on hotel entities for possible times next week. If I can't find a good time, we'll just run at this time.
Okay, we'll see you.
