SIG: Client Instrumentation SIG
Date: 2025-07-08
Duration: 34 minutes
Zoom Recording URL: https://zoom.us/rec/share/J2uBNhl8J_nOA3qhYX_EAF2aIOBz8QuzRdNc_KW8eQ-bF3R7bq0fs-0avDuLxTwi.BwrtknvoBwHrg5lq
============================================================

## Zoom Recording Transcript

**Hanson Ho** 01:18 Hello!
**VP Valentin Pertuisot - Datadog Mobile SDKs** 01:21 Hello!
**Hanson Ho** 01:28 How's it going.
**VP Valentin Pertuisot - Datadog Mobile SDKs** 01:29 Good, and you.
**Hanson Ho** 01:32 Bad.
**VP Valentin Pertuisot - Datadog Mobile SDKs** 01:33 This group.
**Hanson Ho** 01:36 So 1st time joining Valentine, or is it Valentine? Valentine? Okay.
**VP Valentin Pertuisot - Datadog Mobile SDKs** 01:40 Yeah, that's fine.
**Hanson Ho** 01:41 Sorry. I
yeah, we're in a bit of a transition. This meeting is being We were doing this every once a week. Full hour. Now it's every half an hour every other week, because a large part of the the work is spun off to a different sig. So this is from a cross platform kind of stuff.
**Dan Gomez Blanco** 02:03 Hello!
**VP Valentin Pertuisot - Datadog Mobile SDKs** 02:05 No.
**Hanson Ho** 02:06 Hey?
Sure.
**Maryam Saeidi @ Observability** 02:25 Hello!
**VP Valentin Pertuisot - Datadog Mobile SDKs** 02:26 Hello!
**Hanson Ho** 02:27 Hey?
Martin can't attend today.
And there's no topic so far. So you better run this.
I suppose I can, because there's no topic, so it'll be easy.
Can't always volunteer Jason right? So wait. What what?
Martin isn't around so? I'll I'll just project and and run this agendaless meeting, for now so.
**Jason Plumb** 03:18 Thank you. Yeah, cool.
**Dan Gomez Blanco** 03:26 I just add it up.
Topic.
**Hanson Ho** 03:29 Cool.
**Dan Gomez Blanco** 03:29 More of a reminder than anything.
**Hanson Ho** 03:35 Alright I just lost my screen. Fantastic.
Oh, well, whatever I don't need to see y'all alright.
Alright cool. So 3 min after we'll start we got one topic. Thanks for fixing the formatting. Whoever who's doing it appreciate it.
1st topic, could everyone who is working on any provider session manager, prototype post, a link in the Otep.
Those are 2 different things, I believe. Right?
Unless someone's working in session manager that builds off of any provider. Is that? Is that what you're working on? Jason?
**Jason Plumb** 04:23 No, I mean, I have.
I have a straw man implementation, and Josh does as well. So there's a lot of there's a lot of chat about that. I also do that one of the android that I abandoned.
So yeah, I mean, this is ongoing work that Ted is doing a lot of
the heavy lifting with. I guess I can click this. I'm back button. Okay?
but those those 2 things are related. Yeah, entity provider session manager session manager, not the same thing as entity provider. I assumed he was meaning entity provider. But
the cause. If you click that link you'll see that he's linking to the hotel.
**Dan Gomez Blanco** 05:05 Yeah. The entity provider. One.
**Jason Plumb** 05:07 Yeah.
not. I don't think it has anything to do with such, I hope. Can you look for the word session manager in here or session in this page. I don't think it's part of this, is it?
**Dan Gomez Blanco** 05:16 Well as it talks about sexual management. I don't think it it does, is the.
**Hanson Ho** 05:23 Yeah, it it feels. Oh, this is back in December. This is, I think,
**Jason Plumb** 05:28 Sorry. Yeah, so this does relate in that. We might be able to do sessions with a entity, with an entity or entity provider instead of just attributes. Okay, that's how they're related.
**Dan Gomez Blanco** 05:41 Is it my correct understanding that the session manager
could basically then build on the resource provider or the entity provider? Basically.
**Jason Plumb** 05:53 I'm nodding because I think that's true.
**Hanson Ho** 05:56 Yeah, right now it. I think the session Id is being added at the with the span processor for for android but in theory that could all come from the entity, or we could all put it in the resource and as the events change, the provider changes, so we should be able to remove the the actual attribute being added
to the to the signals themselves. But this would be a bit of a change, since people will be expecting session. Id. Or had been getting session. Id from the actual signal, will now have to get it from the resource, so
it might be one of those things that we do both for a while, and then we kind of deprecate and then kind of move on. But certainly this would be a way of getting what is effectively a mutable resource that's not identifying into the the resource without
needing to like, do weird hacks and stuff. So.
**Dan Gomez Blanco** 06:54 So so certainly session manager could be a 1st consumer of entity provider.
yeah, I saw there is a is it? Was it. A prototype from Josh, of the resource provider in Java is that.
**Jason Plumb** 07:08 Yep, Dan, you're a little quiet, by the way.
**Dan Gomez Blanco** 07:12 I might. Is it better now.
**Jason Plumb** 07:14 Yes.
**Dan Gomez Blanco** 07:15 Cool.
**Jason Plumb** 07:20 Yeah. Josh has had at least one. I think he might have 2,
and he's definitely more involved in them than I have been with mine, so
I think there were 2 different Oteps at some point right.
**Hanson Ho** 07:35 Yeah, there's the the Otep, and there's also the he posted the prototype for the SDK as well.
**Dan Gomez Blanco** 07:41 Yeah.
**Jason Plumb** 07:42 Okay.
**Hanson Ho** 07:43 So this should add, I can post the I can find the SDK implementation website.
**Dan Gomez Blanco** 07:51 Yeah, so.
But I'm not. I'm not too sure. Maybe if Ted just joined.
**Ted Young** 07:56 Yeah, yeah.
Sorry. My last meeting went long. How's it going? Y'all.
**Dan Gomez Blanco** 08:00 No, I was gonna ask of the. So what's the relationship there between the work that the entity sake or doing provider and the old tap that I just well, I just linked your message here related to the.
**Ted Young** 08:13 So it seems like the entity Sig is like back at it at this subject, which is fabulous.
Because we need this stuff for sessions.
but I feel like Josh Serif.
Is trying to kind of portion out just like the Api for like creating entities.
and had like was trying to be like, let's punt on like how things like receive updates for these things and stuff like that. And I would like to kind of like, push back against that. My concern from working on this Otep is like
how you like deal with these changing entities ends up affecting your Api for like how
you want to. How you want to create them.
Right like his Api, for example, is a bunch of fine grained like, add update delete methods. And the idea is this, entity provider is like the source of truth.
But I found that like, if you do it that way, and you have things responding to changes. You create a situation where they're getting hammered by a bunch of individual changes. And that's not what you want, right? You want the whole thing to get updated, which means, like the session manager or some other thing, is like the source of truth, and the entity provider is more just like a communication
mechanism. So for the I think it's important for everyone who's interested in session management to kind of lean in to the entities. Sig and pay attention to the stuff Josh is working on right now.
And I would like to push back a little bit on us like putting anything into the spec until we've actually sorted out
the stuff that we want to see here in the client, Sig, which is like consuming this data when it's changing out out from under us. I think we're the I don't know that there are other people with that problem right now. There will be in the future. But it's kind of on us just to make sure that this is going to work out the way we want.
**Jason Plumb** 10:31 When is the entity sig meeting.
**Ted Young** 10:33 So it meets every other week. So it's not meeting this week. It's meeting next week, and I wasn't able to go to the last one.
because it was holiday season.
So so I was a little surprised when this thing popped.
**Jason Plumb** 10:50 8 am.
**Ted Young** 10:51 Yes.
**Jason Plumb** 10:52 Right.
**Ted Young** 10:53 Yeah. So it's actually like, you know, for people who go to the browser. Sig, it's sort of like
1st
30 min of the entity Sig, we can hit up, and then we can go to the browser, Sig.
But the most important thing I would say is, is, if people have prototypes right? That's really what we need right now. Is
is prototypes on this stuff. And even if we just had it in Java, I think it's fine, but I just don't want that work to
get too far out there without thinking about all of the
the extra problems that we have.
**Jason Plumb** 11:33 So.
**Ted Young** 11:34 I am. I am happy. They're looking at it, though, like it was, I was more frustrated when they were ignoring this than them, trying to move quickly on it.
**Jason Plumb** 11:43 The the thing, I concluded pretty quickly. In both implementations. The Android one, the Kotlin Android one, and the Java one is that
it's all of the other wiring, that is, the challenging part, like building the entity provider and swapping out like the concept of a resource, is fine, but unless that is reflected in every other place that touches the resource. You're going to have inconsistent data around
what the resource is in different in different components, and that that to me is yes, challenge.
**Ted Young** 12:15 Right, and that's the pushback. I would like people not just me to point out to Josh, is he is trying to say, Let's that looks like a hard problem. Let's punt on that. And I'm saying, like, I feel like that the chances that that problem comes back to the Api, for how we interact with this thing is like.
**Jason Plumb** 12:36 Yeah.
**Ted Young** 12:37 Likely, so.
**Jason Plumb** 12:38 I agree with you on that one. Ted, yeah.
**Ted Young** 12:41 Yeah, this is like.
and there's like some inconsistencies that we might. We, I think we have to live with. Actually.
you know, right like
like, you can't have some kind of synchronous stop the world, change kind of thing
occurring here. You have edge cases around like, what if you have a span that starts on one side and ends on another side
like which batch does it go in?
And there's like some of those answers are like easy to implement. And some ways you might want to answer that turns out to really complicate exporters.
so I I would advocate that we. We have some kind of end-to-end prototype with session management, and like doing all of this stuff in there before we we get any of this stuff into the spec.
**Jason Plumb** 13:38 Cool on the flip.
**Ted Young** 13:40 Side. We now have other people to review our shit, and, like hit, approve and put it into the spec once we're ready. So let's also jump on this opportunity.
**Jason Plumb** 13:48 Yeah, it's gonna I mean, at least in Java. It's gonna touch a lot of code.
**Ted Young** 13:55 Okay, yeah, yeah, it's
it it. I can see why he would want to punt on that stuff. But
like, you just said, it's like
this thing is just like glue between a couple of hard problems. And we need to solve the hard problems to understand what the glue should look like.
**Hanson Ho** 14:20 Are, are we thinking that this should be solved in one or the other part of the existing concepts that's been spec'd out, or like a 3rd thing that's kind of in the middle. That kind of does, you know, deduping, debouncing, and and you know all this consistency management.
**Ted Young** 14:39 So I've I've like put a lot of that work into this Otep right like. And one of the conclusions I had is like there are not just a deep dive on this a little bit doesn't seem like we have like a lot of other things on the
on the agenda, like one question we have is like, how much should the entity provider be doing generic things and entities are a generic concept, and one of the areas you hit are, you know, deduplication things like back off right thrash were things that came up. And the conclusion I came to when I looked at that is like, we don't actually have any generic answers to these. These do not seem to be
like generic
problems. They seem to be like the degree to which there might be some thrash happening, for example, seems like pretty specific to different
entities or resources, right? So like the kind of thrash that might result from like, an entity manager.
looking at like network resources is going to be different from the kind of thrash you might get from like sessions or something.
And
so in that sense, something I put in, the Otep was saying. Like, I think we actually want to push a lot of the logic into the entity managers. Right? So Josh is saying, this thing should be the brain. This should be the source of truth.
and what I'm saying is like with the whole concept of an entity is there's like this one source of truth out there
that you're pulling all of this information from. And you're getting all of that information as a block, if that's like the whole concept behind. An entity is like all of these attributes came from one
source of truth at one moment. Then there is this like manager that knows how to do that.
and knows how to manage the thrash and the back off, and the nonsense. And then just like, push out a new version of this entity. So rather than going in there and like fussing with this thing and updating it and thinking about it as like the memory manager, it's like the entity manager for each entity
like. So you have a session manager, and that thing keeps track of everything to do with the session.
and whenever it's time for, like
the session changes to look like, go out there and trigger a bunch of stuff. It is like replacing the session entity in the entity provider.
So that is pushing quite a bit more of the like logic and management into each one of these managers, and that feels reasonable to me, because each one of these domains is like pretty different from each other.
like if you had another, like a network manager that was looking around at like, Oh, we're swapping around between cellular and Wi-fi, and like all of this other stuff, and like whatever kind of changes I wanted to get there, and then pushing that out
to all of the sdks to like trigger batching, and all of this other stuff
that thing would probably have like a lot.
It's just got a different problem to deal with.
The only problem the entity provider would need to care about is like.
are so many of these changes happening all the goddamn time that it needs to be like batching up
changes to independent entities.
And the conclusion I came to at the time is like that does not seem to be true.
but that could be wrong.
**Jason Plumb** 18:23 That also seems like a performance optimization question like we can. I think, if anything, that's the kind of question we might be able to kick down the road. It's like
we have so many components everywhere that from for the last 5 years have have relied on the knowledge that the resource is immutable, and so they can hold a handle to this immutable thing forever.
**Ted Young** 18:43 Right.
**Jason Plumb** 18:44 Right, and those are all of the places that need to change.
And that's, I think, what what the real hurdle is.
**Ted Young** 18:51 But here's the rub. Here's the rub. The way that you would batch up these changes. Right? If you let's say we do have a scenario where it's like, you know, what actually happens in mobile devices is they wake up, and then, like
4 entity managers, go to work figuring their shit out, and then they all come back in. And they're like, here's the new network stuff. And here's the new session, and whatever the hell else we're talking about, and you get slammed by like 4 or 5 of them at the same time, and you don't want to trigger 4 or 5 batching operations.
The way you would do that is, you would like have some kind of delay where you would like, pack a couple of these things in before you push it out right like you'd buffer a little bit and then push this stuff out.
Don't do that.
**Jason Plumb** 19:45 Yeah, that that sounds over complicated. To me. It sounds for 4 or 5 things.
**Ted Young** 19:50 It does right, but like on the one hand, triggering 4 or 5 batches on
right, like mobile networking.
flushing on a mobile network is its own nuanced little thing where we care quite a bit about how that works.
So that that's all I'm trying to point out. And if you do say like, try to batch these things up. If the
the more the energy provider tries to batch these things up.
the more it introduces a delay, so that when you get your on change notification, you are now like actually kind of off center from when the change actually happened to when
you triggered your your batch segmentation. And so you're increasing the likelihood that something
so there actually is a a mess there, I guess, is what I'm not proposing a right answer, but I actually think
we would do ourselves a favor by trying to game some of this out in the real world.
Because I think as like people working on mobile like, we just have more problems than anybody else has because of the the trickiness of the domain that we operate in.
And this is kind of like our opportunity to like get it right in the spec.
**Hanson Ho** 21:15 So maybe we'll learn a bunch if we just start prototyping like a session manager and like a network entity and kind of just see how things work. you know. See if there are like weird race conditions, you know, batch chunks ordering all that, all that, all that good stuff.
**Ted Young** 21:33 Yeah, all that good stuff. And I don't. And I think, like, we probably want to get a leg up on that. If we want the entity. If we want to go to the entity Sig and say like, Please, please wait for us to prototype all this stuff out, you know, before
we shove anything into the spec
like, I think we need to to kind of like, get a jump on it and and show them
some of the problems that we're we're dealing with.
The answer could be like, it's just kind of sloppy, and we don't care. And whatever
you know what I mean like, like, for example, batching
and the the batches of data associated with entities, and like
the flushing of data over the network, could just be separated from each other.
So you flush multiple batches like there might be like simple ways to solve this.
I want us to have simple ways to solve this, but I it? I would feel better if we had a prototype that
actually like banged against these problems before we put anything into the spec.
**Hanson Ho** 22:42 So if the spec is just a bit under specified, does it open up the possibility of adding to it? Once we figure this out? Or or do you think there are things that we might be painting ourselves into a corner with? If if the spec kind of goes in the way, it is.
**Ted Young** 22:57 My concern is, you never know. Right? Like, I mean.
this is like the thing about software design is
one thing we don't like to do in open telemetry is break things by mutating things, adding things is fine.
right? But if what we discover is like.
we've created a crud interface for entities.
But then decide like, Oh, that's actually terrible.
because you want the entity manager
to be in charge of all of that data, and you want it to be. You want to have, like a replace interface. Replace this interface, this entity?
With this new one. Not, you know.
update little bits of this entity. That's an example of a
situation where, if we're just like, yeah, seems fine. And then we prototype it. And we're like whoops. So let's make a breaking design change and create a lot of thrash
for people.
I don't.
**Dan Gomez Blanco** 24:07 I don't see why we would need to do that like. Why don't we just like move fast on prototyping this thing, and just see if we can get.
**Ted Young** 24:15 The 1st version to be based on experience instead of like speculation.
**Dan Gomez Blanco** 24:21 Do we have any experience on how? I guess other solutions are currently handling
this problem. I'm just thinking, like, you know, the concept of a resource is, you know, a bit like hotel specific. But the concept of like, you know, setting con, like attributes in context. And then I'm just thinking of all the solutions that I know of that would handle this. But like.
let's say, for session, Id is like whatever is in the moment that you push data out.
That's what the session Id is. It's not great. But this solves the problem of like, I don't care what happened before is like, you know, there's a contextual property in there. That's a session. Id, and I will only attach it
when I push. When I export data at a regular interval.
So I'm
probably it has its downsides, I guess, but like I don't know if if that's a common pattern
of you know how all the client side
tooling is currently working, or if we have experience on that front that could help.
**Hanson Ho** 25:25 I mean, if if the update is Async.
you know if if you can kind of serialize them and serialize as in like making the run in serial. Then then you can have some sort of coordination between transitions between sessions and what telemetry goes into to which side? That is a you would do. It's a bit problematic. So it's almost like
for the really important ones. You can have some guarantees, but for a lot of things that are effectively external or or frankly delayed, because sometimes things happen and and the the changes get propagated because it takes time to actually pull it out and stuff like that are expensive.
Sorry, it's just gonna be a bit wrong sometimes. On the margins
**Ted Young** 26:08 That that is the bit of research I've done is like
there's, there's 2 kinds of things you're trying to do. One is like, generate some kind of replay of what happened, which is like very event, based and timestamp based, and stuff like that. And when you're doing that, then none of these problems really like matter. Right? You're just recording when all these things happen. And then you're kind of splatting it out where
the extra bit that I think we're open. Telemetry differs is the other thing we are using resources for is we're using them as indexes. Right? We are trying to create aggregates out of this stuff.
You know. Metrics, dashboards, alerts, finding correlations, and blah blah! Blah! Blah! And that's the situation where, if like
something ends up in the wrong batch of data. Maybe you're skewing?
All of those things.
The question is like, is that a big fucking deal or not? Or is it like is like, like.
Generally speaking, when these things are changing, is the system like doing a bunch of work was like a bunch of work mid flight? And is that like happening all the time?
Or is it like these? Changes are rare? Usually, if you're kicking off a session or ending a session, it's because nothing's going on.
etc, etc.
But I don't know. I just want to make sure we don't end up with like
fence post off by one errors right where we like.
I mean, and resources have this problem right? Like the whole reason resources were mutable to begin with, was because when you're booting up an application. There's a bit of asynchronous
stuff around gathering these resources, and like you would end up in this situation, where very consistently, your 1st batch of data, which is a very valuable batch of data like the boot of the application, would not be indexed properly.
because a couple of these you had this race condition with some of these resources not being resolved yet.
and so we went. Had to go back and say.
No, you have to solve this like tricky ordering issue on boot around like resolving these resources before you kick off the SDK, so I'm just sensitive to the fact that, like this problem does show up
already in resources around getting these little race conditions in there.
**Jason Plumb** 28:48 So Ted has. I have not ever joined the Entity Sig, and I I think I understand some of the history of like what, where the motivation came from. But was there ever any?
I feel like we're also just like bringing the entity Sig like to this meeting, which is fine because the agenda is pretty light. But
Was there ever any consideration given to
another like other ideas, such as having
a resource which is immutable, which it is today, but also introducing a mutable resource, or like an ephemeral resource, anything along those lines that can sit parallel to it. And so all of your changes are at least constrained to this one little area.
and if people care about that they can care about, and if they don't, then they don't, and I don't. I mean, I'm saying parallel. Maybe you nest one and the other. I'm not sure but you know there's there's some data modeling that has to happen there, but
the idea of having another resource, or something analogous to that which can mutate without changing
the existing usages of resource.
**Ted Young** 29:54 Very great question. And yeah, we totally looked at that back in the day, and the answer is like it does. You don't get anything out of that. You've complicated your data model without
solving any problem, because the thing about the immutable resources right like is like they don't change because they don't change, they don't change. It's not because we said they were immutable, and that it's like the thing you're observing. Just the service name just doesn't fucking change.
**Jason Plumb** 30:28 Yeah, okay.
**Ted Young** 30:30 And and in whether it's an ephemeral resource or like one that's immutable. Your data race problems
are the same.
**Jason Plumb** 30:41 Yeah. But I think I think there's a then a discussion to be had about whether or not a certain field like service name
according to open telemetry, is ever changeable during the lifespan. Right? And then you decide which bucket it goes in. Does it go in resource, or does it go in immutable resource.
**Ted Young** 30:58 Right, but but it doesn't it
from the perspective of like anything downstream. None of these things care
right? Like like the big question there was like, is there anybody out there who is taking this resource object, and just like making a hash out of that whole thing blindly and saying like this fingerprint is like the Id. For this application I'm just gonna assume nothing in here ever changes. And the answer was like, No, except for, like Jaeger. And they can just change that.
And that's just. And then in practice, we discovered that users are already doing this, what they okay
today to get these resources to change is they just reboot the SDK mid flight.
**Jason Plumb** 31:48 But.
**Ted Young** 31:49 So that they can change the resources. And so back ends today actually do if they're being coherent, have to deal with these things. So it's just anyways we did look at that. It just it turns out to be kind of a nothing Burger.
**Jason Plumb** 32:03 Okay.
**Ted Young** 32:04 The one thing I will add, the one piece we looked at potentially, adding.
which we could bring back was just the concept of like a validator or like a freeze function. If what you're trying to do is make sure that you aren't handing out a foot gun
where? Because we say, now, you can update entities. People are now going back and accidentally updating.
like resolving service name or some other resource late and like this, you're back to this like 1st batch of data missing things.
You could add a validator like you could have a moment where you call freeze on this thing.
or or like boot, or some some some checkpoint.
and you have like, and a, you know, like in a a list of like
keys of like the immutable or like service lifecycle thing. So you could at least warn someone being like.
I noticed that you are adding, you know, a a service name, or, you know an application id to this thing after it has booted. That is probably wrong.
and you should like fix your your boot code.
So that was.
**Hanson Ho** 33:21 So.
**Ted Young** 33:21 That that we looked at earlier.
**Hanson Ho** 33:24 So we're 3 min after the the half an hour we can continue.
**Jason Plumb** 33:29 Forgot. This was a half an hour meeting.
**Hanson Ho** 33:31 Yeah, this is half an hour now, so we can continue the discussion. I think, on the slack. But I think what? What Ted. What you're talking about is we want prototypes soon to discover any like, you know, ferret out any you know, potential issues in the spec asap. So if if there's some, you know anybody who could do this, it'd be great, you know, on.
**Ted Young** 33:50 This is our chance to go get involved in the entity Sig, because they care about our issue. Currently. So let's let's pile onto that.
**Hanson Ho** 33:58 I have a couple of things mentioned, but I'll do it in the slack, because, yeah, if I'm the police today, then I need to police myself.
Alright! See, y'all in 2 weeks, and on slack.
**Dan Gomez Blanco** 34:09 Thanks. Everyone.
**Hanson Ho** 34:11 Bye.
