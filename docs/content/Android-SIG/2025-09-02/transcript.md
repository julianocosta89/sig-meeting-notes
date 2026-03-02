SIG: Android SIG
Date: 2025-09-02
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:36 Hello?
**Jason Plumb** 00:38 Hello, good morning.
Still getting set up over here.
**Cesar Munoz** 01:10 Hello?
**Jason Plumb** 01:12 Good morning!
**Cesar Munoz** 01:16 Good morning.
**Jason Plumb** 01:20 The universal greeting everywhere across the globe at any time.
Okay, I'm still getting set up here. One second.
Thank you for your patience.
**Hanson Ho** 01:43 Hello.
**Jason Plumb** 01:45 Hey, Anson.
**Cesar Munoz** 01:46 Hello?
**Jason Plumb** 01:57 Okay.
All right.
We have one topic who does not have anybody attributed to the… to the topic.
I'm gonna reshare, because I forgot to tear off a tab.
And I just find it easier that way.
Okay.
Is anybody who's on the call, did you type this, agenda item?
Maybe I did. I'll put my name on it.
I know that there were several of us talking about this, so,
Yeah, seems like a good, a good idea. Okay, and Tyler's here, that's great. Okay, so let's talk slow rendering listener first of all.
So, I, opened this issue based on this comment.
Based on this PR…
And I think, you know, this is something that has been around for a while in this project, it's not something that I introduced in this PR, or is necessarily new, but we had been holding onto a map of activity to listener.
And that's as part of the…
part of the, jank detection and venting stuff.
And, yeah, there was, like, some call-outs here, which are pretty… pretty legit, which is, like, yeah…
If, for some reason, this listener gets deregistered.
Before it can do its cleanup.
then we would leak references to activities. And…
I think that the short… the skinny of it is, is that, like, I don't know how that can happen, given the current structure. Like, it's… it's trying to… because it's registered as a listener, it should get notified when an activity's being torn down, and be able to free all those references, which it has this, like, teardown code to do that.
But in principle, I mean, I agree that, like, holding these references does seem like…
potentially a bad idea. So, you know, I love this issue, I don't know what we want to do about it, there's a little bit of discussion.
**Hanson Ho** 04:13 I think a weak reference is gonna be fine. The max it could leak is maybe one activity, it's just that we should do our best to try to clean it up. As long as that's not the last reference, then, you know, we're good to go.
**Jason Plumb** 04:28 Yeah, so I looked into this, Cesar, and there is… so, right now, it's a concurrent map, I think we showed that, right? So, any implementation that's using a weak…
what is it called? A weak map with weak references as the keys. That approach would need to also be concurrent.
In which case, Cesar's like, well, we could use this thing here. And it's funny, because the, upstream repo uses a copy of a code from that class, I believe. A copy of a class from that codebase, I think. Well, let's verify. I think it's called…
We concurrent… Yeah, this one.
And there's, like, a, you know, it's, like, definitely from that project.
Yeah, so here.
**Cesar Munoz** 05:16 Oh yeah, definitely.
I'm curious why they copied it instead of using the library, but that's…
That's part of the extreme reboot.
**Jason Plumb** 05:24 Yeah, probably just to continue, like, reducing dependencies. And this thing doesn't have any other dependencies, it's, like, self-contained, and so it's a trade-off between, like, adding one class or adding a dependency.
We could do the same, or we could take the dependency, and then I think the implementation is pretty straightforward then.
But that was the initial complexity. So we still think it's a good idea.
Does anybody think it's a bad idea to try and migrate to… a reference.
**Cesar Munoz** 05:58 I think it… I think it's a good idea. Well…
The thing is that I'm not sure how the…
My understanding is that the modern Android developments
I think it should mostly rely on a single activity, That has, you know, Composables and stuff in it.
But back in the day, You… you will…
You usually will have an activity per screen, and then if you… if you hold
Held a hard reference to it than when you switch to another screen,
You know, that memory won't… wouldn't get released.
And, you know, those phones didn't have much memory either, so…
it's probably not such a big of an issue right now, but it's still… I mean…
I'm pretty sure there are plenty of apps
with legacy code, using multiple activities, because I've actually worked in a company with something like that.
**Jason Plumb** 07:05 And maybe…
**Cesar Munoz** 07:05 So, so…
**Jason Plumb** 07:07 There could also be teams that use activities as, like, a grouping for composables.
I mean, I'm assuming that people do that, I also don't know.
**Hanson Ho** 07:18 Yeah, or there could be other activities for… depending on modes and stuff, so… I think this is… this is probably…
I don't… think the implementation requires depend… taking on dependency. I mean, this…
I think this could just be done,
even, even, you know, supporting concurrency, although I don't even know if we need to do that, to be honest. But…
**Cesar Munoz** 07:42 That's a… that's a good point, because all of the UI handling will be done in the single thread, so… so maybe we don't need concurrency
Safety.
Woody? Yep.
**Hanson Ho** 07:58 the underlying map should be thread-safe. Like, that's important, but I don't think… like, I'm pretty sure we could do this with a few lines of code without a tendency, so… I can take a look, leave this issue kind of open. Like I said, in practice, it's not going to be a huge deal, but it ought to be
easy to make this work the way it ought to. So.
**Jason Plumb** 08:23 Yeah, so I scratched at it with a weak map, and then weak references to an activity as the keys. I think that was the suggested approach.
And to make that concurrent requires either, you know, having synchronized blocks on some kind of lock, or using concurrent locking structures.
I attempted it at first with a lock, and there's, like, just a lot of places where this activities map is, like, kind of…
messed with.
You know, like, here…
And, here… and these are… these are in listener methods, so callback from the framework.
And then… I think there's another one in here somewhere. Yeah, this one. So, it's not… it's probably not too bad.
**Hanson Ho** 09:10 Yeah,
yeah, I think we could do this without… but.
**Jason Plumb** 09:19 Okay.
**Hanson Ho** 09:19 Whatever works, whatever works, but.
**Jason Plumb** 09:27 Okay.
**Cesar Munoz** 09:27 I agree, but what's clear is that we definitely shouldn't… Whole references to activities.
**Hanson Ho** 09:33 Yeah.
**Jason Plumb** 09:35 Yeah, and I haven't done, like, any sort of audit of the project to see where else we might be doing that sort of thing. I think that work would also be welcome if anyone wants to take that on.
I'm just gonna say, feel free to file an issue.
With those other references.
Okay, I think this will be an exciting topic coming up after this. I do, in advance, owe both Tyler and Cesar an apology for not getting around to reviewing on Friday before the 3-day weekend. I said I would, and I ran out of time and got nerd sniped on something else, so… my apologies.
But for those who may not have seen some of this.
Discussion before, let's… let's switch topics to disk buffering.
Which Tyler asked about in the JavaSig, and I said it was a welcome thing to bring up here, since we are probably the primary or only existing user of…
disk buffering code, but it looks like Tyler's also looking, or currently using this, and so…
Let's open this discussion up.
**Tyler Benson** 10:57 Yeah, thanks for the introduction. I mean, yeah, I totally get that Android is the original intended user of this, and I get the reasons for creating that for Android, so I totally get that… and I also understand that there might be, reasons or arguments for various,
differences of opinion because of it being Android, and I'm just not familiar with Android, so…
The… the use case that I'm trying to go for is, so I'm working in a server environment where the memory of the server is rather constrained relative to a lot of servers. And…
We want to collect metrics, that have relatively high cardinality and, do so more frequently than what we actually want to send to,
the upstream provider. So we wanted to be able to buffer locally, and then send less frequently, to the upstream, vendor.
And so this disk buffering seemed like a good solution for that, but in my investigation.
I identified a couple of pretty glaring inefficiencies associated with it. I addressed one of those already in a previous PR, where…
we,
I made it so that it, it didn't buffer… it didn't serialize the whole byte array in… all at once, and then flush it to disk, but instead it uses the, the hand-coded
optimized, serialization from the Java SDK, and, writes those bytes in chunks, as opposed to all at once.
And,
I wanted to continue on, that similar kind of process on the reading from disk part. The first step of that would be to, was to,
remove the, reserialization, which I find very inefficient.
I understand why it's necessary for the goals of being able to reuse the existing,
APIs, that the SDK provides. But I feel like…
for some edge cases, and maybe it's… I don't think it is a significant edge case, but it should be a fairly common case, where the destination that you're sending to is also OTLP protobuf.
then whatever you write to disk, in theory, should be able to be read from disk and effectively sent straight to the backend, without having to deserialize and then reserialize all over again.
So that was the first step. And then a follow-on I would like… that's not addressed in this PR, but I would like to try to address, is not reading the full byte array directly from disk, but effectively streaming directly from disk through to the network I.O.
So that way, It… it doesn't have to, be so… Memory chunky, so to speak.
**Cesar Munoz** 14:43 Yeah. Hey, Tyler, thanks for all the, all the context.
So… It's… I understand, I understand the need for… for… for your use case.
I'm trying to balance feature and, maintenance.
I need… I need a balance, because…
as I, as I was mentioning in the, in the, in the issue.
Or in Slack, I don't remember anymore.
I have a couple of…
stuff right now in my plate, and I… if I want to commit to something, I want to know that I can do a good job, so… so…
The thing is that what you're asking is a new feature.
Because it's like, it's not… And it's focused on performance.
Which, it's always good to have better performance.
But I'm also kind of like… Not sure, I mean…
I'm usually trying to be conscious about not…
Doing premature optimizations or stuff like that.
You know, unless… unless we, like, really have a problem. With that, definitely the case that you mentioned is something that
So, if I understood correctly, The optimization that you're talking about.
is to… take the data that has been stored in Protoborf.
In that, in a file. And then…
Read it, and send it directly to the network request.
without going through deserialization or anything like that. That's my understanding.
**Tyler Benson** 16:39 Yes.
**Cesar Munoz** 16:40 Am I correct?
Then that's gonna be great for performance.
what I would like to know is…
If you think it's possible for you to accomplish that use case.
You know, with the…
Current states of the… of the… of the library, but, like, of course, writing, you know, some custom code.
To make it work.
Or, I mean, I guess my question is.
What is the reason why this feature needs to be
Supported as a first-class citizen feature for this module right now.
**Tyler Benson** 17:29 So, to answer your question, I think the PR I've presented does a decent job of balancing maintaining support for existing users by, you know, shifting that deserialization
To the builder class, and allowing people that use the builder and passing in a standard exporter, just like they would currently.
it still maintains that support. So I feel like I…
the current API does, give affordances that allow me to make this, reasonably compatible.
The issue I have is in the new proposed API that you've, that you're trying to, encourage me to use, I don't think it gives me that same affordance.
Jason, if you want to go to, like, the, the FromDisk Exporter Builder up at.
**Jason Plumb** 18:35 Yeah.
**Tyler Benson** 18:37 I think this is the main one where it kind of shows that. So here, instead of, setting the exporter function directly onto there, it, shifts things around a little bit. So that way, if you use that exporter.
If you're passing in that export function, then it does the deserialization and reserialization that it allows.
But it gives, if you scroll down a little bit, it gives a couple other options. If you set an HTTP exporter or a gRPC exporter, which are both public APIs in the SDK,
Then it, allows for sending that data via a marshaller, which is defined in the next class down.
Oh, that's actually that new one, that protobyte array, yeah, that one. So, here, it just passes in this marshaller, which is reading those bytes, and sending them straight across the wire.
**Jason Plumb** 19:42 With the unfortunate internal usage.
**Tyler Benson** 19:45 And I could fix that, by just using the public marshaller, and defining the size.
**Jason Plumb** 19:52 Yup.
**Cesar Munoz** 19:55 Got it. Yeah, this is fair enough. I mean.
You came in also in a quite interesting time, because,
**Jason Plumb** 20:03 Yeah, that's… yeah.
**Cesar Munoz** 20:05 the, the, the… the old API, has limitations, and has…
It's… it's also difficult to…
To maintain, because it's a bit cumbersome.
And it doesn't allow for… for much… Flexibility in terms of Different use cases as…
Well, the ones that I've… that I've been…
hearing about since I created this library.
**Tyler Benson** 20:36 So I think you…
**Cesar Munoz** 20:37 So, they…
**Tyler Benson** 20:37 Things like, compression and encryption, correct?
**Cesar Munoz** 20:43 And somebody also mentioned that they wanted to store the data in a relational database.
Which is, I mean, it's fair, it's like…
I guess my point is that…
What I'm trying to do with the new API is to transform it from
A specific class into an interface, you know, an abstraction, so that people can come up with their own.
Stuff if they need it. And then the current behavior will be just kind of like the default behavior.
I'm trying to keep the existing behavior. The stuff that you're talking about that I'm changing, it's all internal.
So, it shouldn't affect the people who just use the current API.
You know, based on why it was public.
Now.
**Tyler Benson** 21:39 As you can see, I'm a Java agent developer by trade, and I have a hard time following what is internal versus externally defined classes. I just blur the lines and do whatever I want, generally, so…
**Cesar Munoz** 21:55 No, and that's fair enough.
**Tyler Benson** 21:56 As is tradition for Java agent developers.
**Jason Plumb** 21:59 How could… Senate, yeah.
**Cesar Munoz** 22:01 I think we've all been in that position, no worries. And the thing is that…
And that's why… that's why I wanted to make it… And, and an abstraction.
Because… so that people like you, who are, like, advanced.
Developers can do whatever they want without having to expect the library to support different use cases who might or might not be…
**Tyler Benson** 22:26 I totally get that, and I understand, your goals there. I think I mentioned in the PR, my main concern with that is, you are, in your API, you are, pushing
what seems to be the boundary of that serialization deeper into the interface, such that it makes it harder for me to achieve what I was trying to do.
And I think you're removing some, nice functionality in those, from-disk exporters. All you're doing is creating this, this, iterable that people then have to kind of create their own abstractions around that.
**Cesar Munoz** 23:11 our own… Our own what, sorry?
**Tyler Benson** 23:15 Around your interval.
**Cesar Munoz** 23:18 No, there's actually an implementation for that.
At least in this PR.
Or you mean, if somebody creates their own signal storage, they also have to create an interval?
**Tyler Benson** 23:30 Cool, right?
**Cesar Munoz** 23:30 what I mean?
**Tyler Benson** 23:31 So you're kind of, and maybe I misunderstand this, but I thought that you're getting rid of, like, the whole, exporter pipeline, and kind of shifting everything to this iterable so that, now instead of, this exporter pipeline, it's all around this iterable. Am I…
Wrong there?
**Cesar Munoz** 23:54 I think I see what you mean. It's because of… well, it's a bit of a long explanation, I don't know if…
Maybe we can go…
**Tyler Benson** 24:02 I think Hansen's.
**Cesar Munoz** 24:03 I see, I see it has on, yeah, your hand, if you, if you want to go first.
**Hanson Ho** 24:08 Yeah, I'll…
I have to, so, preface this by saying I haven't looked at the… I also, you know, meant to look at this last week, but, you know, ran out of time.
So, I'll take a look at both of these so I can be a bit more well-informed, but I think…
What you're asking for, Tyler, is doable. There's actually probably two, optimizations here. One is the reading from a stream, and the other is directly taken from disk and sending it to, you know, the exporters without reserialization.
I think those could be achieved in a generic way, you know, from the implementation, also exposing, you know, just streams, instead of saying, hey, here's a chunk of data to do this.
So… but I'm not gonna go too deep into it, because I haven't seen the actual code. But, at Embrace, we…
you know, we use Stream, Seride, and write, for the same reason. The payloads, we, we also cache
pretty big payloads, and things can get pretty ridiculous, pretty fast, and doing it via streams, doesn't change anything, it just makes it a little bit, well, less memory intensive.
**Jason Plumb** 25:23 That's not nothing, though.
**Hanson Ho** 25:25 No, no, that's… it's actually… yeah, that's… that's… yeah, no, in terms of the benefits, this is totally worth doing. Instead of having, like, objects that you're basically going…
Like that. So I'm wondering… so I'll take a look and maybe make some suggestions, but I think… I think this is doable, without changing the nature of what you're trying to do, Cesar, with the simplified API, and without removing the functionality present… present in the previous API.
I think reading.
**Cesar Munoz** 25:54 Vienna, and…
And that's a fair point, and I think it's also one of the stuff that we've discussed. It's like, we might extend the new API to
Somehow allow people to get Streams out of it that just get the raw data.
But, like, right now, I really just want to focus on migrating to the new API with the existing behavior.
And then try to figure out a way so that people can
like, we can also define, like, a default behavior. I want to really focus on default behavior in a way that, okay, let's say that the default behavior for whatever the extension we decide in the future
Cool, cool, could make it work for… for this new use case.
to be… to return protocols, with OTLP format.
And that would be the default behavior, but what I would like
the… for that part of the API, To… to enable is…
for people to say, well, I don't want to use Protob, I want to send JSON, so this, implementation doesn't work for me.
And I, in that moment, I would like to be able to say.
Tyler. I would like to be able to say
Here's the interface, you know, you can…
you know, create your implementation that works with JSON instead of ProBuff.
and not having to maintain that new use case, too, you know? It's like, that's… that's what I'm trying to handle here, but definitely…
at least, at first, I need to, you know, settle the new API, which
I know it's gonna enhance a lot of what the old API used to do.
But it's kind of like…
it seems like we're gonna… we're getting ahead of… of… of even the new API implementation, which…
It's been a couple of days since, I added some comments answering to
to Gregor's concerns, I still haven't gotten an answer, so it's moving slowly. So, I mean, I'm not saying that we shouldn't add this, but if we add this, I would like it to be done in a way that people can create their own implementations, and that the
Probably something that you need would be the default, and that's pretty much it, because it's about maintenance.
**Jason Plumb** 28:21 Says our TV.
Sorry, can I… can I jump in? Can we be specific about, what… when you say, people can provide their own implementations? Implementations of which… which interface?
**Cesar Munoz** 28:32 We don't have it right now, because it's not part of the API. Got it. But, like, if we extend the API to allow for this kind of
I don't know, as Hanson said, you know, to provide a strength of data, then we should do so in a way that people
Can also create their implementations.
maybe by, you know, making this new part of the API return the… the… the MIME type?
M-I-M-E type, so that they can check if that's what they need, and if not, then…
they will have to create their own, or things like that. But I know the moment that this library adds first citizen support for this use case, somebody's gonna come up and say, I need JSON, because I don't like prototypes. I know that's gonna happen.
**Jason Plumb** 29:18 Yeah, totally.
**Cesar Munoz** 29:19 you know.
**Jason Plumb** 29:20 I agree with that, yes. I mean, there will be people that want JSON, and they want to do all the marshalling, and they don't care.
**Tyler Benson** 29:25 And that's why I wasn't trying to break that exporter pipeline use case for that. I was just doing this as mainly, here's an optional optimization that if you use this, then it's more efficient. But, yeah, no, I get that.
Not everyone wants Protobuff, although…
I would be surprised if, it's not the majority that wants Protobuff.
**Hanson Ho** 29:52 On Android, the Protobuff library is enormous, so most people don't use Protobuff. Yeah, it's almost a non-starter.
**Tyler Benson** 30:01 comment on Android?
**Hanson Ho** 30:03 Yeah, but, I mean, I think…
I'll take a look at the details, but I think this could just be… this may be a case where the API is changing, and a new implementation, you know, is coming in. It's one of those classic, you know, two things modifying the same thing, and there's a bit of a, you know, coordination necessary.
I think… I think we could do this, I'll take a look and see where it is. Especially the reading part, the reading from a stream. Like, that should be separate from the whole protobuf thing. Like, that we should just build in, because it is just…
better. And, you know, the next part is the pipeline aspect of it, of getting from disk to thingamajig, and there's gotta be a way that we could easily swap one with the other, and then use streams to do that. So, I'll take a look, but,
**Jason Plumb** 30:55 Yeah, do we think that maybe there's some middle ground with this interface, this span storage, right? So, in this PR, if this landed, or when in this lands, you know, the way to read stuff back off of disk, in whatever format there is, is to ask for an iterator from your span storage.
Do we think there's room to maybe have other methods on span storage, or a sub-interface of span storage?
But then I mean…
**Cesar Munoz** 31:17 I was thinking… yeah, I was thinking about sub-interfaces.
**Jason Plumb** 31:21 So instead of hearing…
**Cesar Munoz** 31:22 I mean…
**Jason Plumb** 31:22 Instead of iterator for, like, a collection of typed stuff that requires demarshalling, you could have an implementation that's just like, give me the file, give me a block, give me a stream, whatever that might look like.
**Cesar Munoz** 31:34 That's what I was thinking, like, as an extension. Actually, I've been thinking about it, and if you scroll down.
To the image that I share about the current API.
**Jason Plumb** 31:47 I will. I just wanted to jot that down. Okay, so we're… Here.
**Cesar Munoz** 31:52 Yeah. Just to the comments.
**Jason Plumb** 31:55 Yeah.
**Cesar Munoz** 31:56 a bit more.
a bit more.
**Jason Plumb** 32:00 Bitwarden.
**Cesar Munoz** 32:00 The tires come. Yeah, there. So, what I was thinking is that maybe…
Signal storage might just be for writing.
And then…
We can remove that arrow that points to the iterable of collation, and then the iterable of collation can be one way of reading it, one sub-interface, and then we can create another sub-interface.
And then the default will have to support both, probably, but only for product buff. I've been thinking about this, but definitely, you know, it's…
It's an interesting timing.
**Hanson Ho** 32:36 If the interface could just be a stream of the collection, rather than the collection itself as an object, and you provide the default implementation, I think that'll just work.
**Jason Plumb** 32:47 Tyler, since you've reviewed this PR, and I haven't yet, what's your take on this being extensible enough to introduce the optimization? Is it a little bit harder?
**Tyler Benson** 32:58 Yeah, like I was saying previously, I think that, having the storage be, be typed specifically to, the, .
**Jason Plumb** 33:10 Signal.
**Tyler Benson** 33:11 Yeah, the signal is what really scared me, especially when you look at, like, readable result. Previously, readable result was, just internally a byte array, and I felt like that was something I could still work with a little bit better, even though it had the downside of, you know, reading everything in at once.
instead of streaming it, at least I could then avoid the reserialization. But by pushing that type down into storage, it removes that ability to do that, because the deserialization is implicit, in storage.
**Jason Plumb** 33:47 Yep, okay.
**Cesar Munoz** 33:48 Yeah, I was gonna… If we separated from the right.
**Jason Plumb** 33:52 Sorry, sorry, sir.
If we separated read and write, then maybe that helps with that, but go ahead, sorry.
**Cesar Munoz** 33:58 I want to emphasize that what Tyler is mentioning about the reading being a byte array, it's all internal.
So, that's not… Part of what users… we're using.
So far.
I, I, I get the point.
Listen, really, I was trying to… make the…
Operations of what you will need to do with this buffering.
quite clear.
And to me, there is no…
There's no way to make it clearer than have
an interface that says, well, you can write stuff, and then you can read stuff. And that's all it is. That's really the whole refactorization that I'm doing here. It's just defining a contract that allows you to write and read stuff. Right, but that…
**Tyler Benson** 34:47 Writing serialized data and reading serialized data.
**Cesar Munoz** 34:50 But that's the thing, it's not trying to force serialization or deserialization, because the contract
doesn't handle that concept. It's just, if you write a type of object, then you must read the same type of object. That's all the contract knows. It doesn't know what goes behind the scenes, if there's serialization or not, you know?
**Hanson Ho** 35:10 But the contract is stuff, and the specificity of stuff.
is, I think, you know, what's at issue. If the word stuff could be fairly generic as a stream of bytes. And then the actual API we layer on top, or rather, we expose the fact that it is just a stream of bytes that we're reading in and reading out. And on top of that, the default, we have these serializers and deserializers to basically pull it and turn it into what it's supposed to be.
save it what it's supposed to be. And if Toddler can then replace that layer, so basically
detach the layer that translates into concrete stuff, from the layer that just does reading and writing a stream of bytes on disk. I think this will be… you'll… we'll be able to accomplish what we all want to accomplish.
**Cesar Munoz** 36:02 Yeah, that's fair enough, that's a possibility. If you take a look at signal storage.
It's really just an interface, oh, it's not defined here, but it's in the comment that I… that I…
**Jason Plumb** 36:16 It's over.
**Cesar Munoz** 36:17 tighter.
**Jason Plumb** 36:17 I mean?
**Cesar Munoz** 36:19 Signal source is an interface
That just has right and clear, and then it extends each level, because that's the way we, so far, have read the signals in an iterative way.
So, it was… it was actually to make it easier, because the way we iterate right now from this was kind of awkward.
But anyway, we can do, if I understand what you're saying, Hansen, is just to, like, decouple signal storage, to put an example, from the reading, in this case from each variable.
And that would be pretty much it. What I was suggesting to Tyler at the beginning was, well, this is an interface.
Because it extends iterable, you can just not implement the iterator.
function that comes with eTurbo.
And then you can create your own function, public function, for your own implementation, that returns you a, you know, a stream of stuff that you need.
That could be a way, because it's an interface. Again, I'm not trying to force anything here, it's just writing and reading stuff.
And, you know, presumably just reading the stuff that you write, because you shouldn't be aware of serialization or anything like that. So…
What we could do is that, I mean, decouple, just not make it a standard iterable.
And then, having that option to be the default.
And then in the future, have another way of reading.
that's… You know, will have this way of injecting data straight into the network, in a way.
That could be it, but I mean…
**Tyler Benson** 37:59 I mean, if there's a way for storage to give me just either a file or a series of bytes, or a stream of some sort, and then I can just go with it from the public API perspective, I would be fine. I would be happy.
**Cesar Munoz** 38:16 Yeah, I mean, there are a lot of… there's the folder manager, all of those are internal classes that you can use for your implementations that are… even storage is an internal class you can.
**Tyler Benson** 38:29 But I'd like to point out, though, that I do believe that the functionality I'm proposing would be broadly beneficial to most people.
And by going that approach, you're making every individual re-implement that same thing, as opposed to providing it as core functionality.
**Jason Plumb** 38:52 Like, make it…
**Cesar Munoz** 38:53 funny.
**Jason Plumb** 38:53 make it less internal, I think, is the idea. Like…
**Cesar Munoz** 38:57 To… to make work less internal.
**Tyler Benson** 38:59 The ability to send data directly from disk, instead of, having to provide everything after the storage.
Basically, what I implemented in my PR, I think would be generally beneficial to include in your system. If you don't want to include it in the system, I understand that. I'm not going to argue on that. You're the maintainer of it, so… but I do think that it's beneficial.
**Jason Plumb** 39:29 No, I agree with that for sure. I don't think that aspect of it is contentious, Tyler, it's, I think, how we get there. I think having implementations that allow for direct protobuf, serialization, I think, yeah, I think we would include that in the distribution.
I don't think that's contentious, is it?
**Cesar Munoz** 39:49 No, it's not. I just would like to be in a way that we don't have to…
Add support for other formats.
In the future, because people will be able to do that by themselves. That's… that's the way I would like us to somehow manage it.
**Jason Plumb** 40:06 Yeah, we think…
If protobuf covers 80%, then protobuf and JSON probably covers 95, and then, you know, from there, maybe let that be custom after that, but…
**Tyler Benson** 40:16 But honestly, one thing I'd like to point out is that if JSON is really, like, that common of a thing, then I think that there would be a strong argument for allowing the serialization process to write to disk as JSON, specifically to allow sending straight from disk instead of reserializing all over again.
I think that new serialization is very problematic, in my opinion.
**Cesar Munoz** 40:45 That's fair enough. The… Reason why… it's… well…
It makes sense to have it deserialized right now.
Just to… just to make it clear, is so that people can just forward this data to their favorite exporter.
it doesn't have to be a protobov OTLP exporter, it can be a JSON OTLP exporter, it can be a Zip King exporter.
**Tyler Benson** 41:10 I understand that. I'm not arguing that that's an invalid use case.
But I feel like…
**Cesar Munoz** 41:16 about this use case is that it's generic. It's like, it might not be the most…
**Tyler Benson** 41:21 Omnipotent cost.
**Cesar Munoz** 41:22 garments.
Yeah, it's not the most performant, for sure.
But it definitely covers all of the cases. Now, we're talking about performance specifically.
And that's a valid point.
But when it comes to… I mean, I don't like…
I definitely don't like, and I try to avoid 100%,
to… to obsess about performance before we even get in trouble regarding performance. I really would like to avoid that.
And, in your case, it's not…
It's not obsession, because you do need it, and that's fair enough.
What I'm saying is that, if you're saying, well, maybe if JSON is also very needed, because people like to have JSON,
That's fair enough, but what I'm saying is that let's just wait. Let's wait for people to ask for that, to have some relief, because to be honest, most of the people should be using Protocol.
There are some caveats.
in Android, for example, with Protob and size libraries and stuff like that, and that's fair enough, but at the end of the day.
you know, I just wouldn't want to support stuff or add features.
that I'm just not sure are needed right now.
Because that's just something… whatever it's added there, it's something that I will have to maintain. Forever. So…
Let's just wait, and in the meantime, I would just like to merge the new API, and then think about ways to extend it so that there can be this new feature.
New functionality, where you wouldn't have to deserialize stuff.
All of that should be possible.
before that, because I'm not removing the classes, the internal classes that you are using, you can still use them. And in fact, I know that this is something that has been proposed in the core upstream repos as well.
They're asking for some features that
The core maintainers were not willing to maintain at the moment, and they just told me, we'll just add it as an internal method, or something like that, that you can use.
If there's… if it doesn't work for you right now, and then use it for your use case. So I'm just trying to go, you know, step by step with this, and…
it's an interesting timing, because it's not like I'm trying to block you, Tyler, or…
**Tyler Benson** 43:47 No, I understand.
**Cesar Munoz** 43:48 your… your plans, or something like that. I just… just trying to make it easier to maintain.
**GZ Gregor Zeitlinger** 43:54 Go ahead. Sorry, go ahead.
Yeah, I've been listening, so far, because I just wanted to get a feeling.
As I'm also a maintainer of that component, I think Tyler has made A good use case, for…
his use case, or maybe for the component in general. So…
I think it would be a mistake if we go ahead and merge a new API
that, does not consider this use case. I would be very unhappy with that.
Now, we probably cannot figure out every detail in this meeting, but I think that the use case is…
Very well, and we should continue discussing it.
Offline.
**Cesar Munoz** 44:40 That's what I'm proposing.
**GZ Gregor Zeitlinger** 44:42 Damon.
But…
**Cesar Munoz** 44:44 It doesn't, but it's like a perfect step.
**GZ Gregor Zeitlinger** 44:46 Sorry, I'm not… I'm not happy with, that we are trying to,
change the API in a way that we already know is going,
To make some use cases impossible, because then let's just wait until we get this right.
**Cesar Munoz** 45:05 I know you explained that Tyler.
**GZ Gregor Zeitlinger** 45:08 with this PR.
**Cesar Munoz** 45:09 But let me explain, the use case that Tyler is mentioning was also…
**GZ Gregor Zeitlinger** 45:15 For a very long time, Cesar, already.
**Cesar Munoz** 45:17 But let me explain, because I need to, like… I mean, that's why we're here to discuss it. The use case that Tyler is mentioning is also not possible with the current API, unless you tinkle with the…
With the internal classes, which is what he did.
And it's fine, we can do it with the new API as well. What I'm trying to do is add the existing public use case that we have with the current API to be easier to handle.
And to maintain, because right now it's not. And it's actually… I explained in my first PR what are the benefits of this new API. It's not taking into consideration what Tyler is mentioning, because that was not a use case so far.
But what I'm saying is that let's try to enhance what we have right now, and then expand it. That's…
That's pretty much it.
I'm not… I'm not removing anything from the API, if you take a look at the polling stuff.
And if that's the case.
**Tyler Benson** 46:16 Did you delete all of the from disk exporter stuff?
**Jason Plumb** 46:19 I mean, there… yeah, that is… that is true, like, this all goes away.
**Cesar Munoz** 46:23 Yeah.
Which, at the end, what it did was to iterate
Over the stuff, and then it was in a kind of, like, a black box way.
Where, you know, people didn't control what will happen inside that, and they would just pass an exporter function, and now it's… it's more flexible because you get the data, and then you can do whatever you want with it.
**Jason Plumb** 46:46 So, I wanna… I wanna see if we can find some pragmatic, middle ground to move this thing forward. So, we've talked about the idea of…
using the storage as an extension point, and maybe splitting read and write interfaces. If that could be done, even if there's a new interface method that is not implemented in this PR, because the size is already pretty big.
But if we could at least introduce that change as a starting point in this PR, and get agreement that that would work for future use cases for Tyler, is that a way forward for us?
**Cesar Munoz** 47:20 Yeah, the stuff that we discussed with Hansen about decoupling the iterator from the divs, yeah, we can do that.
**Jason Plumb** 47:28 Taylor, are you open to that? If that lands in this PR, would you give it another look, and we can maybe think about going forward?
**Tyler Benson** 47:34 I mean, I'm happy to give things another look, but I think that the… in my opinion, I think that, this, PR,
It is… is problematic because it's saying, hey, let's change how users are using this to give them more power to do things that they want.
But the previous API, in my opinion, already did that by giving the ability to provide whatever exporter that they want. An exporter is a standard, open telemetry interface that
and maybe I'm not understanding things, but,
for example, the, the serialization to, the… what's it called? The…
the database, I believe, could have been handled with an exporter. Unless it's completely bypassing the disk storage, then what's the point of even using this API in the first place?
And then the other comment around encryption and compression, I feel like those are better handled at the byte level array anyway, and that also is made more difficult by this change.
As opposed to made easier.
**Cesar Munoz** 48:54 I'm not sure I understand how this change makes those things difficult, because that's not… that's not what this change is.
is suing. It's… okay, so…
Okay, we're running a bit out of time.
**Jason Plumb** 49:12 It's true.
**Cesar Munoz** 49:12 Tyler, can you please… Putting that…
I wanna… I want us to focus, because we're… it seems like we're talking about different stuff.
Can we at least… list the stuff that was public in the old API.
that…
provided users with functionalities that are no longer possible with the new API. And I'm talking about the public API.
**Tyler Benson** 49:43 Not the, you know, whatever.
**Jason Plumb** 49:46 Yeah, so these interfaces happen to be an internal, so they were not considered a public extension point.
So it was not expected that other implementations would implement these in a.
**Tyler Benson** 49:56 That one's not, but the metric, the log, and the, those ones are.
**Jason Plumb** 50:04 The serializer or the deserializer, or both?
**Tyler Benson** 50:08 Those ones right there.
**Jason Plumb** 50:09 These exporters, or the serializers?
**Tyler Benson** 50:13 the exporters.
**Jason Plumb** 50:14 Okay.
**Tyler Benson** 50:14 So there's the, the log record from disk exporter, for example.
Oh, cool.
So those ones are in the public API.
**Cesar Munoz** 50:24 Yeah, and please have a look at their implementations.
And… what they did, and what is it that they allowed that the new API
for bits, in a way. I would like to know more details about it, because to be honest, I'm really not understanding what… what is the new API constraining.
You know?
So if you can add those details in the PR, I'll have a look.
**Tyler Benson** 50:56 If you have an idea on how to make this extensible for the use case that I'm asking for, I… just let me know. I don't need to quibble about this API, personally.
as long as it supports, you know, streaming directly from disk, I'm good with that. So whatever is more comfortable for you.
I,
**Cesar Munoz** 51:22 Yeah, we've been…
**Tyler Benson** 51:23 I still don't fully understand how you intend this API to be used, is, I think, what I'm trying to get at.
**Cesar Munoz** 51:30 It's in the… an example, it's in the… in the current PR.
**Jason Plumb** 51:34 Yeah, but it's in the README or the main description.
**Tyler Benson** 51:37 It provides the iterable, but in terms of the extension point that you're referring to, I don't understand.
**Cesar Munoz** 51:44 Well, it's just an interface, right? You can do whatever you want.
**Jason Plumb** 51:47 I mean, Tyler.
**Cesar Munoz** 51:48 You didn't.
**Jason Plumb** 51:49 You could say use the API, and I think you mean extend the API, and it's nitpicky, but those are two different use cases, right? What's described here, I think, is how a user user would use this, right? And what you're talking about is how to make it extensible, or how to add functionality.
**Tyler Benson** 52:04 How is he suggesting… Cesar, how are you… could… maybe you could help me understand how you're proposing that I extend this API to allow for my use case?
**Hanson Ho** 52:18 I, I think.
**Cesar Munoz** 52:19 That's fair enough.
**Hanson Ho** 52:20 I think this PR actually reduces the extensibility and increases the ease of use by a user just dropping in. So I think… I think…
**Jason Plumb** 52:27 True. I think, I think…
**Hanson Ho** 52:30 But I think we could do both.
**Jason Plumb** 52:32 Yeah, I think we can get there, but I think that's also Tyler's point, is like, this reduces extensibility, and it makes it easier to maintain and easier to use.
**Cesar Munoz** 52:40 That's fair enough, but really, because I changed all of that.
I really would just like to understand what is it that it's reducing? Exactly. I mean, based on the… because we were talking about the from this exporter that had been removed.
if you take a look at their code base, what is it that is inside there that was done that is not possible with the current API? That's what I would like to understand. And I'm not saying that we…
She'll allow for more use cases.
But if we do so, it should be done in a way that people can, you know, create their own extensions, and not having to rely on whatever it is on this source code.
That's my whole point.
**Hanson Ho** 53:23 I think we can take this offline. I'll do some more research, I'll make some suggestions, but I think this is doable.
**Jason Plumb** 53:30 I just do.
**Cesar Munoz** 53:31 Yeah. Excuse me.
**Hanson Ho** 53:32 A little bit open, basically, a different layer. If the goal, Cesar, for your API is for users to make it easier, I believe we can crack stuff a little bit more open at the correct layer, so that Tyler can do his thing. And I think what would be doubly interesting is, in the future, build in the API, the coupling of the input and the output, because right now those are decoupled.
So it's really hard to say, you know what the input is, I know what the output is.
If you…
are able to couple those and have an interface that basically assumes that the format for input and output is the same, then you could, like, built in, you know, without doing resialization. But that's probably a secondary step on top of that to make it nicer. But I believe we can crack stuff open in a way that Tyler can do what he wants, and the API can maintain the usability goals that the intention was there for.
So, I'll educate myself by looking these PIs.
**Cesar Munoz** 54:27 It should be definitely possible. So yeah.
Let's have a look, you know, let me know.
**Jason Plumb** 54:38 Okay, I'm just taking some final notes. I appreciate you all taking this, this topic, you know, the whole hour, because it is… it's detailed, it's complicated, and sometimes it's hard to convey why a specific approach…
makes your thing challenging, especially when it's complicated, so… thanks for… thanks for keeping it civil as well. I do think there is a path forward here. We'll have to see what that looks like, and it might take several iterations, which is probably not what Tyler wants to hear.
**Tyler Benson** 55:07 I understand how these things go. I've been involved in OpenTelemetry long enough.
**Jason Plumb** 55:13 Yes, you have. Well, I don't mean long enough, but long… even… long enough.
**Tyler Benson** 55:17 I've been around long enough to know that this is how it goes.
**Jason Plumb** 55:20 It's true, it's true. For those who maybe don't know this history,
**Tyler Benson** 55:26 Tyler worked at New Relic long ago, and also at Datadog, and helped facilitate the donation of all of the instrumentation code from Datadog.
**Jason Plumb** 55:33 So, into the instrumentation repo. So, yeah, Tyler's been around for a minute.
**Tyler Benson** 55:37 Yeah, if you look back at the Java instrumentation repo history, you can see a lot of… Trask finally surpassed me as the primary contributor, but I was up there for a long time.
**Jason Plumb** 55:49 Yeah, yeah.
**Cesar Munoz** 55:50 Yeah, I've seen you there. So, it's been a while.
**Jason Plumb** 55:56 Okay.
Yeah, any sort of experiments or straw men that people want to hack up, I think is also welcome, but also, you know, if we need to take a step back on that PR and do it as smaller units or separate units, or if you want to augment that one, I think we're all happy to review that, and I'm sorry I haven't gotten to it yet.
**Cesar Munoz** 56:14 Please let me know if you think the PR is too big. I've asked that question a couple of times there already.
**Jason Plumb** 56:22 Fair enough.
**Cesar Munoz** 56:22 and a clear answer. So, please let me know. I mean, we can work around this stuff.
Let's try to keep the communication and, and…
Please bear with me, I'm just trying to maintain a lot of stuff.
**Jason Plumb** 56:35 No, it's good.
**Tyler Benson** 56:36 I wanted to call out, Cesar, I understand, or I believe, you're the original author of this contribution, correct?
And I think there's a lot of good bones in here, and that's ultimately why I am, you know, presenting these arguments. If there wasn't something for me to build off of, I'd go and do it myself. So, I want to commend you for the work that you've put into it, and the effort that you've done to maintain it, so…
Thank you.
**Cesar Munoz** 57:05 Thank you for that.
And we'll figure out your use case.
as Hanzo said, I think it should be possible.
They're done in a right way, I really…
**Hanson Ho** 57:15 I don't want to support too many stuff.
I don't think we need to support it. I think it's just busting open an interface at a certain level, and everything underneath is all not us up to support. I think this is very doable. I think this is very doable.
**Jason Plumb** 57:31 And I'd like to remind everyone, next time, make sure to wear a band shirt. Cesar and I clearly got the memo, no one else did, so next time…
**Hanson Ho** 57:39 See, I normally would not… It's either soccer jerseys or band shirts. I just picked soccer jersey today.
**Cesar Munoz** 57:46 Nice.
**Jason Plumb** 57:47 Alright, I appreciate it, appreciate everyone. Let's do it again in a week.
**Tyler Benson** 57:51 Thank you. Bye.
