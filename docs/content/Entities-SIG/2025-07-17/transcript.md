SIG: Entities SIG
Date: 2025-07-17
Duration: 56 minutes
Zoom Recording URL: https://zoom.us/rec/share/Ks7hULPamyyALL6So6LIA4TiBj2IquYRrUiLN82cUENCAptdmwcQ-mJbYst3qzI5.nAQCL1X0Lg5IbtMB
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:51 Morning or other times of day.
**Nathan Smith @ Elastic Observability** 00:57 Oh, it's it's morning.
**Josh Suereth** 01:03 I'm just updating the agenda quick apologies. I'm a bit behind because I did not. I was trying to finish a pr for us to review, and I did not get it done. So it's gonna be kind of an ugly review here.
**Nathan Smith @ Elastic Observability** 01:20 I had. I had a question about like
**Josh Suereth** 01:25 So.
**Nathan Smith @ Elastic Observability** 01:26 For weaver and stuff like, I think I'm in those channels, and I think there's meetings.
Is there like a weaver sig, or like
**Josh Suereth** 01:38 The semantic convention tooling is the weaver.
**Nathan Smith @ Elastic Observability** 01:40 Convention tooling. Okay, that's.
**Josh Suereth** 01:42 Yeah, that's it's on Wednesdays, about an hour before this.
Okay, so I don't know if if Ted's here yet, he has a couple of topics he and I talked a little bit about the alright. So actually, you know what, I'm not gonna put my normal name he and I talked a bit about some of the directional shift, because he made a bunch of comments on our Pr. And I I definitely agree with him. But basically, I want to talk about that first.st So we we decided that when we were looking at our our prototype for the SDK, that we want an Api right?
And I I believe that this is actually a shift in scope from the previous Otep.
it, and it opens a set of complications and challenges we'll have to sort out. And so Ted and I talked, and we'd like to update Ted's current Otep to resolve the things that we have all the complications around having an Api, and also add in all the things that were in that Otep originally, because they we know we need to build that out in the future. But I think to build an Api at all for the Api discussion we've been having. We need to sort out those issues to begin with, like, I think it's all tangled.
We tried to untangle it. We looked at what we built, and I we didn't like it. So I think we need to go more aggressively into the Api notes app. So I just want to talk. I think there's a a the more I've been looking at it, the more I've been updating the prototypes because the Java prototype is now updated to do more of the entity Otep. It actually implements it as it was written, and I have some additions to it. Now, I think we need to. This is like a scope increase for our initial work.
And we, I'd like to spend this meeting kind of talking through that scope increase and some of the important decisions.
If there's anything that is kind of unrelated or urgent that we should talk about before that, let us know. But letting folks know. I think we're on a fun journey now any concerns like anyone who's like I. Before we we embark on the we have to have an Api. I'm still looking to understand if anyone has any last minute hesitations or reservations around having an Api.
It's my understanding that we don't cool.
All right. With that I'll kick it off to Ted to talk about it.
**Ted Young** 04:38 Yeah, I mean, I think the main development that I've seen is we tried to break out the entity provider specifically to see if we could.
you know, like, just get a piece of the elephant eaten but Jason Plum Martin Kuba. Other people who took a stab at prototyping that noted it was just very easy to implement it, but what was hard was as soon as they looked at using it. They realized, like the code changes and the implications for the SDK are actually pretty substantial.
And so my suggestion was.
we need to identify those pieces. That kind of surround the entity provider and actually prototype them out.
Before putting anything into the spec.
Because my concern is like that that stuff. It's like the entity providers basically glue code.
It's a way to transmit information asynchronously to a bunch of independent components within the SDK and elsewhere.
But, like what that does to the SDK. I think we should figure out before we start putting any of this into the spec.
Dan.
**Daniel Dyla (Dynatrace)** 06:10 Yeah, when when you say it requires substantial changes, the SDK, do you mean the entity provider that you proposed in your Otep? Or do you mean the entity provider that Josh proposed in his spec pr. Or both.
**Ted Young** 06:24 Well, I'm saying that we should combine the 2 things.
**Daniel Dyla (Dynatrace)** 06:30 I realize that. But the the specific comments from Jason Plum, and whoever else you mentioned.
**Ted Young** 06:36 I believe that they were implementing the one in the Otep.
But some of the differences in terms of their Apis relate to stuff that we learned when we tried to implement a session manager to drive it. For example, wanting to make sure that the state in the entity provider is always coherent. You always wanna be replacing the entire entity. Essentially, when you're changing it.
you wouldn't want to do a series of mutations on on that entity to get it into from like one correct state.
It's another correct state.
So you have a 3rd party like a session manager that's keeping track of all of that information.
So that's like a slight difference, like in Josh's model, he was thinking, oh, the entity provider would be like.
you know, the actual like data source that things were using. And it's more like just a transmission mechanism.
Essentially.
**Josh Suereth** 07:44 Actually the prototype was kind of the same Ted. It didn't change much. I can. I can walk you through. But I that's not necessarily the important point. I think the important point is, we should work together. And what I did is, I updated the tasks for the entity sig. So I this was listed as phase one entity. Otep was unlisted as a phase. It was something we would pick up after phase one. I'm calling this phase one B now.
and trying to expand out tasks that we need to flush out what we do here so that we can get this stuff done. And I think, like Ted, you, you called out. I think the the really important ones of we need to figure out. SDK startup.
I actually think I'm calling it SDK startup. I mentioned this to the Tc. Yesterday. We have an implicit SDK startup in our specification.
That is not kind of explicitly defined, but, like there are pieces the specification that put requirements on SDK startup, particularly resource. Detection is called out.
and every piece of the SDK is required to have a resource. But the way it's constructed is kind of left open to sdks, and it makes it awkward for people who are trying to provide this, so they were amenable to us, like not amenable. They were in agreement that, like we should if we go in and sort that out. That's an improvement to open telemetry. So what I have listed is basically we need to understand how SDK startup will work.
We need to prototype and define what startup initialization works in the context of entity provider. I have already started that within Java, and I can talk about some of the details there, but this is an effort that we need to do in a couple of different languages, and I think Javascript, Java and go are kind of my targets, because Javascript gives us browser sessions.
Java is just interestingly tricky for its own right and Go has always traditionally had trouble implementing a specification when we don't implement it. First.st So let's let's do that right.
**Ted Young** 09:44 Yeah.
**Josh Suereth** 09:44 Okay with that said, just to walk through a few of the things you have, Ted. The task you're putting in the in the thing. Let's get them here, so we can continue to track them and make sure we're making progress. The 2 that, I added were the startup specification and prototype being startup specification.
and then the existing tasks we have, I think, are still relevant to all of this work. So we still need to make progress on those as well.
Okay.
**Ted Young** 10:12 I think the one other task you might consider adding, is on the other side of the fence from Startup is exporting data. That's the other place.
**Josh Suereth** 10:25 That change.
**Daniel Dyla (Dynatrace)** 10:26 Shut down.
**Ted Young** 10:28 Shut down.
**Josh Suereth** 10:29 That.
**Daniel Dyla (Dynatrace)** 10:29 Particularly in the browser case. Shutdown is extremely frustrating.
**Josh Suereth** 10:39 I don't understand why. Yeah, it's it's so clear in the browser. Everything's just happens.
Sorry. That was, that was sarcasm in case you couldn't tell.
**Daniel Dyla (Dynatrace)** 10:50 Yeah, I mean, the browser isn't even the worst Js target for shutdown.
Believe it or not.
**Ted Young** 10:57 Yeah, okay. And And then there was one final final thing, and I don't know how we actually record this. But this is like.
**Josh Suereth** 11:07 And.
**Ted Young** 11:08 Example of 2 birds, one stone.
We noted that messing around with startup in particular, makes us kind of yearn to have startup. Be kind of like wrapped up inside of something that encapsulates all the providers and everything that need to get booted.
And at the same time we have like a new config file config language we're trying to implement. So it's just notable that if we.
if all of that provider startup stuff was wrapped up, then changes around now having to create like an entity provider, and stuff like that would be less noticeable to end users.
**Josh Suereth** 12:03 This is.
**Ted Young** 12:04 Seems like something that kind of dovetails a little bit with the work we're doing.
**Daniel Dyla (Dynatrace)** 12:10 Yeah.
**Josh Suereth** 12:11 Good.
**Daniel Dyla (Dynatrace)** 12:12 Yeah, we Javascript started doing something similar already. In order to prepare for the file config stuff.
and moving like. Right? Now, we have a lot of our environment. Variable config is spread all over the place, and we're trying to centralize a lot of startup related things. So that is something that we've already been thinking about, and I'm sure other Sigs are probably having similar discussions.
**Ted Young** 12:41 Yeah.
**Josh Suereth** 12:42 One thing I'll call out the Java Sig, the configuration component of the Java Sig is taking the entity prototype that I have based on entity manager spec, and using that to change initialization for configuration, because I had to solve that temporarily. And they like the direction it was going. So they're actually going to use that now for configuration. So I, IA hundred percent agree. This is a major problem in open telemetry. And I think it needs to get specified. And it's gonna I think that discussion will have to go into the spec Sig fully like like we'll have to be kind of working back and forth. And I think we should prototype and and be advertising what we do here.
Cool if if you want. If anyone wants to go through and update this to like Ted. The thing you're mentioning this is meant to be the task that captures it and advertises it to the rest of Oaktel feel free to update the description.
**Ted Young** 13:36 Great.
**Josh Suereth** 13:37 Okay. Cool.
**Daniel Dyla (Dynatrace)** 13:38 I'm interested in the details of what you just mentioned, but I don't think we should block the meeting, for it. Is there a Pr. I can look at, or something.
**Josh Suereth** 13:45 Yeah. The entity prototype which I think was linked last week. It's linked to from the Spec. Pr. The Java prototype has a extended open telemetry. Api. So Java has a notion of a bundled Api with where it starts up together.
and I showed how you can actually have a prototype that will extend it and basically do new things and experiment. So that's they might be moving forward with that.
Okay.
**Ted Young** 14:13 Yes.
**Josh Suereth** 14:15 Cool.
Let's move into some of these questions. We have entities, glue code. We understand, how do we? How do we start.
**Ted Young** 14:27 Just went over this, yeah.
**Josh Suereth** 14:29 Yeah.
I think the next question you have is the naming bike shed? Should we move into that.
**Ted Young** 14:36 Yeah, I have to go at 8 30 over to the browser Sig. So I got.
**Daniel Dyla (Dynatrace)** 14:41 I also have to go.
**Josh Suereth** 14:42 Yeah.
**Ted Young** 14:43 I don't know how important that is, but I think naming bike sheds probably work better at a meeting than on Github.
but I just wanted to flag. Maybe we don't spend time on it right now. But, Josh, you mentioned resource provider like Java was willing to hand that back or stop blocking us from using it.
Yeah.
**Daniel Dyla (Dynatrace)** 15:06 I'd I'd rather talk about Josh's topic here, since I think a naming by like, regardless of which way it goes, is is fine for me. I have a weak preference for entity provider although it was pointed out to me that it is consuming entities and providing a resource which contains them.
so maybe resource provider is better, anyways, but I think.
**Ted Young** 15:32 I.
**Josh Suereth** 15:33 Given, limited time.
**Daniel Dyla (Dynatrace)** 15:34 Time I'd talk about Josh's topic.
**Josh Suereth** 15:37 Given. Given how budgets work. I would rather talk about the principles we care about. So a let's not confuse users like, let's make a litmus test, for whether name's good a. It doesn't confuse users. And B. It's not awkward to describe in help and onboarding guides like we can introduce the concept and people get it quickly.
Those should be our 2 litmus tests. I don't care what the name is. As long as those 2 things are true people don't get confused, and we can explain it very quickly in an elevator pitch. What the hell it does and why it exists.
**Daniel Dyla (Dynatrace)** 16:09 Yep.
**Josh Suereth** 16:10 Okay, cool And Ted, we we can. We can defer some of this.
**Ted Young** 16:16 Yep.
**Josh Suereth** 16:16 Okay, defer actual bike shedding cool. And it's gonna be a purple bike shed.
All right. What are the right primitives for entity provider in doing the prototype, and in looking at the the previous Oteps, our Oteps, and our thing, I actually think.
And again, this is from trying to write some instrumentation with it that we have 3 use cases.
We have an ad or update where the way add or update works. If the entity doesn't exist, you add it. If it does exist, you update only the description, and if you're the identity of what you're trying to add is different than the one that was previously reported. We consider conflict, and you don't change identity. So this is the safe way to update descriptions on entities during the lifecycle of a resource.
You can't change service. Instance Id. This way, for example.
but you might be able to change like a service descriptive attribute if those start to exist.
so that that's that's that use case the second one is replace. This is where I have a source of truth that is always correct, and there's only ever going to be one and only one, and I want to make sure that this wins. And so like. Let's say I have something checking, for when browser session id changes it would it would. When that browser session Id is detected to change like at the start of a page load, I would go blast out and replace the entity right now, what this implies for events would be if I, if replace is called, and the state of the entity hasn't actually changed. You don't send an event notifying that things have changed. But this is just, hey, I'm I'm giving you. Here's the current state. I'm the owner.
You know that sort of thing. The last is to delete an entity, and this would be kind of like a tracing use case where I have a I have something that has a lifetime that I can subscribe to.
and I can say, cool. I get a session, start event, add or update session, remove event, delete right? And so I have those 2 types of instrumentation. I have one which is basically a I need to pull every once in a while to see if something changed and blast it away, and the other one is, I add it. When I see it I remove it when it's no longer relevant.
I do want to prototype these with session in browser to make sure that this fits, and I do want to prototype it with other types of things that we might want to do like if we want to report IP address on host, and we want that to change when the IP address changes, we'd have to sort out what that looks like as instrumentation. But that's that's the current proposal. So I'm throwing that out there.
How do we feel.
**Ted Young** 19:08 I think it's good. The one thing I might note a bit of nuance around update.
Should it be that you have to swap out the entire description block versus being able to partially updated without grab it.
It first.st
**Josh Suereth** 19:36 Yeah, so go ahead.
**Daniel Dyla (Dynatrace)** 19:38 If you, if you make it so, it swaps out the entire description. Then any descriptive attributes that were previously added, that you don't like. If you have, say, 2 detectors.
one is detecting descriptive attributes, and it doesn't know about descriptive attributes from the other one. You would lose those, I think, because they're descriptive. I'd rather have them merged than than fully replaced.
although maybe that's a flag like a, you know. Get rid of everything if we need to, but I think that's the the add or update and add or replace. You just have 2 different methods. One is like merges it, and one blows away the old one, because the identity has to be the same.
**Ted Young** 20:21 Right, and I think that gets to the heart of it is like is the point of entities here, that there is one single source of truth that knows everything, and then is updating all of this? Or is this thing a mixed bag of information coming from like multiple sources.
**Daniel Dyla (Dynatrace)** 20:40 At least in go the way that they have their resource detectors implemented they detect like a single attribute at a time from like a bunch of different components, make up.
**Josh Suereth** 20:52 Except I'm actually planning to to deviate that prototype from what Tigrin did. So I actually. So I know that this is going to be annoying to people and go. But there would be the previous resource, detection. Api, that works and would continue to work. Entities would actually be a different thing like. If you look at what configuration is doing where you can say, detect host altogether as a block.
I honestly think we have to be a little more aggressive with the Go prototype, and there'll be a A versus B, right? If you're using provider. You're not using that that fine grain resource detection anymore.
**Ted Young** 21:27 Great.
**Josh Suereth** 21:28 And that's the like for Ted and and Daniel. I think the thing we've talked about in this group a lot.
Does it make sense to have a piece of instrumentation that can only describe entities. It just adds descriptive attributes. And that's what it does.
Does that make sense? If so what? How do we handle it? Go ahead.
**Daniel Dyla (Dynatrace)** 21:50 Yeah, I was. Gonna say, I guess it depends. Like, is there a use case for that? Because they both have to be configured in the same SDK, maybe, instead of having a you know, I don't know a Kubernetes detector and a Kubernetes details detector. You have, you know, a just a single detector, and then possibly we would have a multi entity detector that you could that could take sub detectors if you did have 2 that you wanted to use. Because that's a to me. That's a deployment thing, right? Like if I have.
if I am as a user consuming a module that has an author that has opinions about which attributes should be included.
and I want to add some different ones. I might want to just like tack on some descriptive things that I care about, that the author of this module didn't care about.
and that's to me the main value of merging the descriptions. But if we provide like a multi entity detector, or like an entity merge detector, or something like that. Where you say, take the module that's like this author that had his opinions, and then this smaller one that I also made merge them together, and then, from the sdks perspective, it shows up as just one entity. It simplifies the SDK to not have to like worry about doing those merges.
**Ted Young** 23:21 It it, but it goes deeper than that. It's not just that it simplifies the SDK. It makes sure that the entity contained within the entity provider is in a coherent state.
right? Like the thing about the current model of like updating one resource attribute at a time is one. If anything that was like listening to this thing would get like a stream of notifications which isn't what you would want. The other thing is like, you have this period in the middle, where these things are going in, where you now have, like an incoherent state.
essentially.
**Daniel Dyla (Dynatrace)** 24:01 Yeah.
**Ted Young** 24:02 Partial state, and if we box it all up the way you're describing, then, and each entity is managing its own state collection, and then, when it's ready, it's like, here's the complete.
And so everything downstream is only ever dealing with complete, coherent things.
**Daniel Dyla (Dynatrace)** 24:25 Yeah, you're talking about essentially like atomic or transactional changes.
**Ted Young** 24:32 Yeah, yeah, it's.
**Daniel Dyla (Dynatrace)** 24:34 Probably without using those words, because people get mad.
**Ted Young** 24:37 No, but I know but I we're we're speaking the same language like if you, if you make it an interface that's more like. And this is the funny way we've been using immutability around resources has actually, in part, I believe, been to kind of like guide users to doing the right thing. So if your interface is like, you can only replace the description as an entire block, right like, we don't give you like a merge function that that kind of tells you as a developer that you're supposed to. You're not supposed to poke this Api 5 times in a row to change 5 attributes.
**Daniel Dyla (Dynatrace)** 25:27 I think there's also a different type of conflict that we haven't really talked about. Josh. You've had your hand up before I bring up a different thing.
**Josh Suereth** 25:34 That's that's actually what I might be. We might be seeing the same thing. There's a conflict of detection. So let's say I write a detector. Here's the solid example. The Aws detector might report a host entity. A host detector might report a host entity. How do users control which one wins? And so.
**Daniel Dyla (Dynatrace)** 25:54 Yeah, they may have different ids.
**Josh Suereth** 25:56 Exactly. Our original Otep was 1st to report wins.
Because and that's why add or update pays attention to the identity. So you can only update an entity if you have the right identity that was registered 1st users would give us like resource detectors in order that they want. And so, if host detectors first, st it gets reported first, st the the aws one would get dropped right. And and that's a way to preserve the ownership of it. So that's why I'm actually a little bit nervous about replace myself. My prototype did not have replace
**Daniel Dyla (Dynatrace)** 26:30 I don't either.
**Josh Suereth** 26:33 But it. But like allowing Delete, I think, is okay, because we would assume that you're doing things in order. So like, add or update delete. Maybe we go with just those 2 first.st And this identity conflict thing, Ted, that's like to know you're you're you. We can make it so it essentially swaps out the the entity. But you have to be the one who owned the Id, so that we can deal with a conflict of like, hey? Somebody, you know. Yes, is reporting a host. Id. That doesn't match the host detector user wants host detector to win Key post detector. Right?
**Ted Young** 27:04 I, yeah. And I think, I think replace has value.
I I will say that like, there's definitely gonna be situations where where I think it's going to be very helpful is on the other end of this. When you're trying to segment batches of data, you're gonna really want replace rather than a delete, followed by an ad for the situations where that's happening. So.
**Daniel Dyla (Dynatrace)** 27:35 Terms of making it transactional. Yeah, exactly.
**Ted Young** 27:37 So you're gonna want to.
**Josh Suereth** 27:39 It's gonna make your life a lot easier.
**Daniel Dyla (Dynatrace)** 27:41 We do want to make sure that we're careful about like, if we have a replace option or a delete, whatever it is.
I want to avoid the situation where I'm gonna pick on aws. But it's not because aws.
I just have to pick something. If if they create an entity detector. They may be like, well, we always want to win. So we're just gonna use this replace method, no matter what like. We're gonna delete anything and replace in our detector. And I think we want to make sure to be careful to to make that not possible, to make it so that the user has to specifically configure whether it's a replace or an ad.
because I think we will end up. You know, we could possibly end up in situations where entity detector authors are like, well, I always want to win. But that's not necessarily what the user always wants. So we need some way to override that by users.
**Ted Young** 28:49 I think it. It wouldn't work as long as the user gets to pick the order that these.
**Daniel Dyla (Dynatrace)** 28:56 No! But if.
**Ted Young** 28:56 Replied.
**Daniel Dyla (Dynatrace)** 28:58 Yeah, I guess.
**Ted Young** 28:59 Because they they wouldn't be deleting each other's attributes right like. If if you have a host, Id and I have a host id, and you say, delete all my crap right. It wouldn't delete the host id hanging out in my entity.
and then, when that all gets collapsed into like a single set of resources like my entity would.
**Josh Suereth** 29:21 Win, no.
**Daniel Dyla (Dynatrace)** 29:22 Think we're talking about.
**Josh Suereth** 29:24 Ted is, they would both be reporting the same entity like they both say I'm reporting host, because again, remember, we have semantic conventions. Say there's a host. It has host Id. They both say I report hosts right right.
**Daniel Dyla (Dynatrace)** 29:37 And aws, says Delete, a previous host, if it already exists.
**Josh Suereth** 29:40 Yeah.
**Daniel Dyla (Dynatrace)** 29:43 Because I know better than whoever I I don't mean to pick on aws if anybody from aws.
**Josh Suereth** 29:48 I saw.
**Daniel Dyla (Dynatrace)** 29:49 Watching the recording. I just had to pick a name.
**Josh Suereth** 29:51 You pick on Google Cloud, like, I'm from Google Cloud, you can pick on us, I added up, because we also might like we have a detector for Gce, right for Google compute engine. And so do we report Host Id in our thing. You know, I I don't know like we will have to sort this out right now. We don't report this Gcp gc, instance Id. And people want it to be host Id. Anyway, if we report there. It's the same problem. So any cloud provider that would want to report a host might have.
**Daniel Dyla (Dynatrace)** 30:18 I think, making it so that users have the the control over. That is important. However, we design the Api, the second the the other conflict that I wanted to talk about was or not. I guess it's the same conflict, but if you have conflicting ids right now, it's 1st wins, the second is dropped. Do we want to do something with those dropped ids to alert the user? That something is potentially going wrong emit some like failed. Entity, detection, event.
**Ted Young** 30:49 You do.
**Daniel Dyla (Dynatrace)** 30:49 Some kind.
**Josh Suereth** 30:50 Ye- yeah, the prototype does this. If you take a look, I have to.
Yeah, I.
**Daniel Dyla (Dynatrace)** 30:55 My daddy.
**Ted Young** 30:55 Here. But one thing you may also want to do, as far as detection there, by the way, is, there's some kind of initialize event it seems inevitable. This thing has right. And then there's some of these entities that we probably want to have, like an allow or deny, like an alert list. If you, if someone comes in and tries to mech with some of these things that we think should never be changed, you probably want an alert because it's probably some out of order code like, if someone drops in and wants to change service, name after initialization, you'd want an alert because something weird is happening.
Anyways, I gotta run.
**Josh Suereth** 31:37 Yep.
**Daniel Dyla (Dynatrace)** 31:37 I have to run to the same thing. Ted is running to.
**Josh Suereth** 31:41 Okay.
**Daniel Dyla (Dynatrace)** 31:42 Dimitri, is your hand raised specifically for something that I raised? Or is it good for me to go.
**Dmitrii Anoshin** 31:48 I believe it's a good way to go. I was. I wanted to add something, but it's not really important, so don't don't worry about it.
I'll watch the recording when I get back. Then, okay.
**Josh Suereth** 32:02 Go ahead, Dimitri.
**Dmitrii Anoshin** 32:04 Yeah, I just want to add that in our specification or semantic convention for the host, entity or host resource attribute, currently we say that cloud identifier cloud host Id wins.
So just want to add to the previous discussions. And that means that we have to allow, let's say, aws detector to override the entity.
**Josh Suereth** 32:36 Interesting like, we need to find a way to have a host detector and cloud detector work together.
**Dmitrii Anoshin** 32:42 Right? Like, yeah. As my. My point is that I believe they all said that we don't want to allow Ws detector to overwrite anything, but it's actually not the case, according to our current semantic conventions, saying like clouds, should know better than whatever you have on the host.
**Josh Suereth** 33:09 Yeah, I I think that this comes down to prototyping a bit like we. I think we need to start we should include cloud and host detection in our prototypes for the SDK. For, like Java for go, and we should make sure that we can deal with that conflict.
**Dmitrii Anoshin** 33:28 Yeah, I'm also wondering if we can somehow model it around entity types instead of particular detectors.
My point is that, like we define host detection.
and then we say sources for the host somehow.
and then we define service detection somehow, and then we provide like sources for, or we have default sources, default sources being, if you put something from the outside for the service being service service, name.
environmental, variable, or something like that.
So I believe that will actually can help us deal with the conflicts when we build detectives around entity types instead of for the purpose.
**Josh Suereth** 34:20 That's my phone.
Yeah, my yaml sucks here. But I'm trying to write down what you said in like a you know.
**Dmitrii Anoshin** 34:30 Implementation example. Yeah, that's correct. Yes.
**Josh Suereth** 34:34 Yeah, yeah, that I you know, I like that this again. You're you're making me think that we need to. We need to go in and prototype this and code right like. So let's let's go see what works. And let's design an interface. We have not yet in any of our spec work defined. What a entity detector interface does granularly like like before my entity detector was just. Yeah. You have one. It reports entities cool.
We should probably go in and and like flush that out, because I think that these are these are good ideas for us to prototype. I don't know if anyone has time. I can add some more tasks around that. But yeah, beautiful. Dimitri.
do. Should we move on from this topic? I think we had a really good discussion. We have a lot of good work going forward on this.
**Dmitrii Anoshin** 35:26 For sure I don't have anything else on my side.
**Josh Suereth** 35:30 Well, no, I just mentioned. We move on to your your next topics.
**Dmitrii Anoshin** 35:33 Yeah, yeah, that's what I'm saying. I don't have anything to add to the current topic.
**Josh Suereth** 35:38 Alright! Go ahead! Should I open these.
**Dmitrii Anoshin** 35:40 Yeah, let's go ahead. So essentially, it's just the Prs for the task that get assigned to me last last meeting. 1st one is adding, yes.
just mentioning that type should not change like kind of guarantees. I'm still not 100% confident about this, because entity is still in development. But yeah, as you suggested, I submitted this Pr to just close close the task.
**Josh Suereth** 36:14 Yeah, I, I honestly think this is fine.
yeah, yeah, this this matches what we did.
**Dmitrii Anoshin** 36:21 Okay, sounds good.
And the second one is much more complicated. It's actually about how we pass entities, information injected in the sdks via environmental variables.
**Josh Suereth** 36:39 Okay.
Am I sharing this? No, I'm not. Here. We go.
**Dmitrii Anoshin** 36:44 There we go.
So yeah, I just put a reference here to this environmental variable. But then I added, the new SDK and file under entities given that you also created this one. So whenever it's merged first, st we can just combine them together.
Because I believe this still goes to SDK.
Why not so.
**Josh Suereth** 37:12 Yeah, the only thing I'm not sure of here, Dimitri is, should we?
And I hate to say this because I think it really Fs this up. But Schema URL.
**Dmitrii Anoshin** 37:24 Yeah.
**Josh Suereth** 37:25 Should. Should Schema URL be here somehow.
**Dmitrii Anoshin** 37:28 It is. Actually, if you scroll up you'll see it scroll scroll to the top.
**Josh Suereth** 37:34 Okay.
**Dmitrii Anoshin** 37:35 Yeah, you you see the Schema URL. So.
**Josh Suereth** 37:37 Oh, up there. Okay. Got it cool.
Do you? Wanna do you wanna walk us through the the proposal? So this is.
**Dmitrii Anoshin** 37:49 It's just like human, readable, kind of simplified way to encode like this.
whatever we have for the entity information. So 1st of all, we have, like each entity, is split by semicolons.
and every entity at least has to have type and set of identifying attributes with minimal. One identifying attribute and descriptive attributes are separate, like super within square brackets, they would be optional. You can define them as well that pretty much it. And all this SDK. It also talks about the conflict, resolution.
and the parson, like guidelines of this string.
**Josh Suereth** 38:44 Can can you make it? I know this is dumb, but can you make it so? That semicolons at the beginning or the end are ignored and multiple semicolons are ignored.
Do you know why.
**Dmitrii Anoshin** 38:55 Why?
**Josh Suereth** 38:57 One of the goals I have for this. So so there's there's 2 things I have concerns about that are unrelated. I think this is beautiful.
having semicolon in the beginning. Let's say I, naively, don't know if someone already set the end variable. So what I do is I do a append semicolon something I'd like that to work right.
And then, if I append semicolon something like, and I end bind with a semicolon to make sure people can append afterwards, and we don't deal with shenanigans. But basically, I think starting with a semicolon would be ideal, so that we can say, Hey, if you're a provider of entity, just add semicolon your entity to this variable. Don't take it over. Just add semicolon, your entity, and you'll participate with the ecosystem. You're totally fine, the other concern I have. Oh, go ahead! Go ahead!
**Dmitrii Anoshin** 39:45 Just want to say, Yeah, that's no problem. I would probably make it optional whenever how many problems we had. And I just say that SDK should trim them that pretty much. It.
**Josh Suereth** 39:55 Yeah, yeah, that's that's beautiful. The other concern I have is there are length limits on it and variables cool.
Do, do we think we're going to run into them. So so like like, let's let's take my Holy Grail. Here right now, is the Kate's entities.
If we can have the operator inject those via n variables.
so that our resource detection for Kate's is just pulling the end variable.
And it works. And and there's no startup issue like calling Apis or anything like that. It's just right in the end.
That's wonderful, right.
If I put in a deployment and a pod and a container and a and a cluster, or whatever the heck we decide.
Do I blow out with with the Schema, URL? Right?
How big is that? I think, and variable limits are more of a issue on windows than they are in Linux. So it might actually be fine from like a Kate's perspective. But that that's that's the other thing I'd be concerned about.
**Dmitrii Anoshin** 41:08 Do you remember what was the limit on windows.
**Josh Suereth** 41:12 I only remember I ran into it.
**Dmitrii Anoshin** 41:14 Okay.
**Josh Suereth** 41:15 That's let me take a look.
**Dmitrii Anoshin** 41:19 Okay, anyway, this this is gonna be one option of of providing
**Josh Suereth** 41:25 Okay.
**Dmitrii Anoshin** 41:25 So.
You're saying that we potentially can split it and saying like hotel entity underscore, something would be a separate like, let's say, one environmental, variable per entity.
**Josh Suereth** 41:48 Oh, sorry I just got the limit. It's so the theoretical limit is 32,000 characters. But the practical limit is 1024.
**Dmitrii Anoshin** 41:57 9, 24.
**Josh Suereth** 42:00 It. Yeah, there's anyway.
if you if you're using set and set end on like a docker image in windows it it 1024 is like a standard limit to end variable length.
**Dmitrii Anoshin** 42:13 So potentially we can.
**Josh Suereth** 42:15 Good.
**Dmitrii Anoshin** 42:16 Moves the service type to oh, environmental, variable name.
It'll be a bit more complex. But so it will be. Hotel underscore entity underscore. Let's say service, and then you just define this service that.
**Josh Suereth** 42:34 Yeah, you could even go with both, maybe, if you wanted. But that's kind of what I was thinking is, I think the the way to solve that is to have more than one end variable, and you'd have to like look through n variable keys to figure out which ones to pull in.
But yeah.
you could go with hotel hotel underscore entities underscore, and then the name of the entity. I don't know how you get dots in that, though.
**Dmitrii Anoshin** 43:01 Yes, that's the problem.
**Josh Suereth** 43:03 Which is why I was thinking more hotel entities.
works, and hotel entities underscore whatever.
**Dmitrii Anoshin** 43:13 Would also work.
**Josh Suereth** 43:15 Right.
**Dmitrii Anoshin** 43:16 Wow! I don't really go ahead.
**Josh Suereth** 43:22 Just sounds, weird, yeah, go ahead.
**Dmitrii Anoshin** 43:24 Yeah, I just wanna say that I would. Typically, I would prefer not introduced to many options because it increases the complexity all the times, and we have to deal with the different, even more conflicted resolution, scenarios, etcetera. So if we are certain at this point that this, we will run into the limit that this is gonna be a problem. Maybe we will start with the separate environmental variable to retire from the beginning.
**Josh Suereth** 43:54 No, let's let's do. Let's in the sense of keeping it simple. Let's start with just one end variable. Because again, I'm hoping that let's do one in variable.
Let's try it out with Kate's right like. Do you think it's possible for us to get a prototype? Talk to the Kate's folks and see if we can get a prototype end variable in the operator for this.
**Dmitrii Anoshin** 44:17 But it would be just the state when we pass them. But we would also need like Sdks, to actually understand that first.st
**Josh Suereth** 44:30 We, I mean, we need both. But for a prototype there's 2 pieces to it, one is, can the platform generate the end? And then can the SDK read it? Given your what you've defined here? I'm not worried about sdks reading this.
**Dmitrii Anoshin** 44:44 Okay.
**Josh Suereth** 44:44 Honestly like, I think that that's if you need a prototype of that, I can probably put that together this week and get you one in Java. Right? Because that's that's the current prototype I have. If I if I had finished my other prototypes, then I could do it in that language, too, like this is, this is good enough for us to get started. But I do think you know, allowing the optional semicolon, I think, is more urgent. And then let's make sure we can actually generate this. And and the target piece of hotel infrastructure I have right now is the hotel operator.
And then we can go from there. Go ahead, Nathan.
**Nathan Smith @ Elastic Observability** 45:21 I was wondering you mentioned the the Kubernetes attributes earlier with environment variables.
But I I know that sometimes we specify research attributes with annotations.
Instead of environment variables. So do we have a way to do entities or plan to like to do it with annotations.
**Josh Suereth** 45:48 Do you mean annotations on your own resource?
**Nathan Smith @ Elastic Observability** 45:52 Yeah, like, there's a There's a there's a link in the.
There's a non normative doc there about yeah, adding, like, Pod, I think it's pod annotations, or I guess it's any annotations where, if you do resource dot opentelemetry dot I/O slash servicename equals x like so that we have that for resource attributes in Kubernetes, with annotations which is, looks like it's that doesn't use environment variables.
**Josh Suereth** 46:30 So so this does. And it's confusing. What is happening is the hotel operator is reading the annotations on your resource, and then it's setting the hotel resource attributes and variables.
**Nathan Smith @ Elastic Observability** 46:43 Okay, yeah, yeah, I guess that was kind of my question is like, is that an implementation detail? Is this an implementation? Yeah.
**Josh Suereth** 46:51 I. What what I would like to do is the move, the key? So if we're successful, and Demetrius thing gets, you know, done and all the SDK supported. Then, at some point in the future the operator will update. This would remain, I think, similarly or the same, even right?
And and what would happen is, the operator would construct the entities and variable from that data, when for your containers, right?
So it it. It's the same mechanism. All of this stuff will continue to work. It's just instead of it, creating hotel resource attributes. It would create hotel entities right.
**Nathan Smith @ Elastic Observability** 47:32 Right? Okay, that's kind of what I was looking for. Thank you.
**Josh Suereth** 47:35 Yeah, exactly. It's a good question, by the way, because this this is this is what led to me, wanting the end. Variable usage of like, Hey, we have to solve this. We have to give people a way to interact with entities. Because if we make entities work in SDK, and this never works.
That's a problem. Right?
It's like a critical piece of our ecosystem. So, okay, cool.
Yeah, I I really, I really like this Pr. Dimitri.
**Dmitrii Anoshin** 48:06 Cool. Thank you. So I'll update it to make semicolon optional in any place, and then we'll talk to operator folks.
**Josh Suereth** 48:18 Yeah, we we we might want to.
Do you think we're going to get pushback making an SDK document that only specifies the environment variable format like, do you think we should make an SA. Environment, variable entity, environment, variable document. That is just what you have here. So instead of calling this SDK, we call it. Yeah.
**Dmitrii Anoshin** 48:44 Sure I can do it.
**Josh Suereth** 48:46 Yeah.
Cool, beautiful.
Okay. Let's come back I don't wanna hold us all too long. Then let's see on end.
possible concerns around size?
No, for now keep it simple and then make it so.
Append to end works in event conflicts.
Well, let's see, semicolon. Okay?
Beautiful and then prototype this hotel operator.
All right. Triaging next steps I want to get into. I think I already have it open, so I don't have to do that.
Want to get back into tasks we have here so, Dimitri, those 2 Prs that you have?
Are they in our in progress section, or should I add them to it?
**Dmitrii Anoshin** 49:54 All of them are in progress. Yeah.
**Josh Suereth** 49:56 Okay.
cool. My Api SDK, specification is, gonna be on hold until we finish the Otep and get people aligned around like the new startup stuff country resource identity attributes. I believe that that Otep is now merged so we can have that discussion next week when Daniel's here or next in 2 weeks, and support for new resource entity references. Proto message.
How's that work going? Dimitri.
**Dmitrii Anoshin** 50:30 Yeah, no, no, not not much. Updates from from my set. I'm gonna work on this one specifically by by the next.
**Josh Suereth** 50:37 Okay?
You did the resource model version, update specification variables to provide Keats. You got that one done cool. So in progress is pretty good. Anything on entity resource mapping entities should be supported by schema files.
This one, the progress towards updating telemetry schema is moving in the semcav tooling Sig for context, we are trying to create a version, 2 of Semcav Yaml files. That is just easier to read and matches Otlp. So instead of calling things groups. We're going to call them metrics. We're going to call them spans. We're going to call them attributes. I'm working on a prototype of that. So I'm doing a lot of foundational work here that's not directly related. So I'm not going to move it to in progress. But I'm on that resource. Dimensions need to be more stable. I think we have all the policies in place in Semcov, and we have enough of our understanding how we want to model entities that I think these are unblocked.
Dimitri. From this the system, Semcom and Host group. Does your group feel comfortable marking host stable in the future? Or do they need any more work from us?
**Dmitrii Anoshin** 51:53 No, I don't think so.
**Josh Suereth** 51:55 Beautiful.
I might mark this one complete then, or I kind of want to wait for the 1st major thing to be stabilized. So either Kate's or host.
Once those have stabilized, I'm going to mark that one done.
**Dmitrii Anoshin** 52:12 Make, sense.
**Josh Suereth** 52:15 This fine grained detector logic. Actually, Dimitri, your proposal today, I think I might explore that in a prototype. I'm gonna yeah. Anyway, I think that's what that would be.
Does anyone have time to work on a go prototype for entity provider? I should ask that first.st
**Dmitrii Anoshin** 52:37 Not.
**Josh Suereth** 52:38 Because I think that's what this is needed.
**Dmitrii Anoshin** 52:39 I might be, but not not like within, not this one.
But I believe we need to still resolve all the discussions we had before today in the beginning, before we can proceed with this one right.
**Josh Suereth** 52:56 I, I yeah, I think the other discussions are higher priority. So this one, I think it's tasked to you. But maybe let's put that on hold until we resolve some of the other things.
Can collector processors differentiate remote versus local. That's something I think you're on, and you're working through it with some other things. So we'll leave that there entity semantic conventions for hosts. This is the semcom work that you're doing already. Right.
Okay.
**Dmitrii Anoshin** 53:28 I'm not sure how like this is probably would be part of stabilization of the host.
Yeah, this is going to be part of system, semantic system, semantic convention working group.
**Josh Suereth** 53:42 Yes. Now this thing about whether service and service instance are different entities.
I think I think there, I wish there was a group in semcom that dealt with system and service.
or dealt with service. I should say, I think, that there is a proposal to do service related things that got accepted. I can show you what what that one is, but there's a new project that's spinning up in some kind of around it that might work on this. I'll see if I can get them to take this after we see after they get through. Startup.
Okay, but there might be a group that will own and make changes to service in open telemetry going forward. So we have clear owners right now. It's kind of a No Man's Land of everyone gets broken if it changes, and we, the owners, are really the Tc, which is not going to make changes frequently at all.
So okay, and then these related things. I think we need a prototype. SDK startup. I have actively started that right now with the Java stuff.
If anyone has time to do that with going, and with go, or we'll see if Daniel has time to do that with the browser. I think we have absolutely need that.
The startup initialization system for entity Provider Demetri, your like suggestion for how we do entity detection. I would like.
I think this is where we need to basically brainstorm to prototypes and come back with what that looks like. That's the weakest part of the Otep, and we need to sort it out. So this one I'm not moving it to in progress yet. But this is the thing that I plan to kick off into in progress by next week, and I'll update you on chat with like what what happens?
prototyping data shut down and in the browser, I think with this one we can wait on. I think this. Honestly, I think this is the most important thing for us to do next. Does anyone disagree.
**Dmitrii Anoshin** 55:47 That's reasonable. Yes.
**Josh Suereth** 55:49 Okay, cool. Talked a lot. Any last minute questions or concerns before we call it.
**Dmitrii Anoshin** 55:58 Oh!
**Josh Suereth** 56:01 Alright! Thanks, everybody.
See you all in 2 weeks.
**Dmitrii Anoshin** 56:04 Yeah, bye.
