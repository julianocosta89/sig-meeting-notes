SIG: Event WG
Date: 2025-07-08
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/YphQmY7MMZgpmdQlcz8NpUFyNej-07xm4tJ6Hsp3Mth4vD3ILFel5cvAKEkLJOyF.jOrT7RP_VZt5cs7j
============================================================

## Zoom Recording Transcript

**Robert Pająk** 00:25 Hello, Steve! Nice to see you.
**Austin Parker** 00:28 Good to see you.
**Trask Stalnaker** 01:04 Hey folks.
**Austin Parker** 01:06 Can't! Trask.
**Robert Pająk** 01:14 Hello!
**Trask Stalnaker** 01:17 Yeah, right.
**Robert Pająk** 01:18 Creating the agenda into the Doc.
No judge, and that is peeling.
**Trask Stalnaker** 01:30 Thanks. I may have to step away. It's a bit at some point. We've got somebody working on the the water softener at our house water pump problems.
I'll ping Laudmila here.
Ha!
**Liudmila Molkova** 02:19 Hello!
**Trask Stalnaker** 02:22 Hmm!
I was just saying I might need to step away at some point. So if one of you all could drive, that would be amazing.
**Liudmila Molkova** 02:36 Drive. Let me start sharing.
Go.
This are our logs discussion, and thank you for someone who updated the agenda. I only have one topic you can guess.
Oh.
so to ask. You were not in the call last week. But essentially you're caught up.
On the discussion. Apparently we got back to the should we have them everywhere or not?
And I can see arguments in either direction.
Alright.
but my preference stays the same. I think we do more harm, that good, not allowing them on metrics or.
**Austin Parker** 03:55 No.
**Liudmila Molkova** 03:56 Entities.
**Austin Parker** 03:58 We were all in spec this morning, right.
**Liudmila Molkova** 04:01 Yeah.
**Trask Stalnaker** 04:01 Yeah.
**Austin Parker** 04:03 I just pick up from where we left off.
**Trask Stalnaker** 04:06 Yeah.
**Austin Parker** 04:12 I don't. I do not want to increase the scope of this Sig or this. I want us to be like. I think that it would be very bad for us to like.
go off in the corner and say, like, Okay, well, first, st we need to do this other thing. But I do think it's I. I'm increasingly convinced that, like we really do need like a really we, we need to figure out this sort of like pointer or bound instrument, or whatever like some generalizable.
This thing points to this other thing like a a Uri for keys and values, and get it at the protocol level and then use that for this. And maybe like.
I guess my problem is is like, I want us. I I don't think we should block this on, hey? We need to go invent some completely new thing right?
But I do want us to say A.
We really think you should use this other thing that doesn't exist yet for this.
**Trask Stalnaker** 05:40 Do we? Though, like, I mean, a lot of people, we've heard a lot of people really value these things being in the same payload being, you know, easily. Like.
like we're introducing a whole extra complexity of indirection for just embedding a simple, complex, a simple, complex attribute like I get it, for, like log bodies, like something that's we expect to be very big. That's where I see the pointers being useful is for big things, big.
**Robert Pająk** 06:21 Patrick, but I at the same time, I think it has value only if it's the data is being repeated right.
**Austin Parker** 06:28 Yeah.
like, I, I think I mean, I I see it in both, Kate, like, I do think there's like, really. So just 2 2 data points, right? Like one is to the sort of like body to the large content object.
I've had people come to me recently that are working in Gen. AI that are like, Oh, I have like 250 plus kilobytes of data that I want as an attribute or potentially unbounded sizes of that like potentially unbounded in terms of kb.
data that they want to be as an attribute, or I have binary. I have a binary object, or I have a binary stream, or something that I want to be an attribute right.
**Liudmila Molkova** 07:17 Yeah.
**Austin Parker** 07:17 And in both those cases.
**Trask Stalnaker** 07:20 Yeah, we've we. We have discussed this previously in this group specifically around that those pieces of data supporting.
**Austin Parker** 07:30 I know.
**Trask Stalnaker** 07:30 And large objects. Okay, right?
**Austin Parker** 07:33 Let me let me finish with what I'm saying first.st Sorry that that's the case we know about right right.
But the other case so like a good example of this is, let's let's take the resource case. So when I boot up an Ec 2, instance I get this very large Json object effectively, of instance metadata, and that instance, metadata is static like it doesn't change, for that instance. From the time the instance comes up to the times destroyed.
Those are all you know, resource attributes.
and rather than encoding those into the same payload every single time, I should just be able to have a single thing that points to that resource metadata potentially on a network share, potentially something that gets ingested through a side channel and goes and live somewhere else, potentially something that a collector or some downstream consumer of Otlp could take and then switch together. Right?
We need the same pointer type for both right. That's what I'm saying. It needs to be sort of at a protocol level thing, so that downstream consumers and view that pointer and do something with it right?
And say, so if I am a consumer that really wants everything to be on the same payload, then I say, Okay.
I'm gonna go fetch this. I'm I'm going to fetch this pointer document for this pointer dictionary and flat map its attributes back onto everything that matches this before it goes down before it is actually written to my observability store.
Right?
**Liudmila Molkova** 09:21 Wouldn't.
**Austin Parker** 09:21 It also solves the like.
It also now. But I could also say, I'm not going to do that. And my observability store has some sort of stream processing that's happening, and it looks at those, and it does something, or it does query, time joins right, or whatever like. We don't need to over specify that. But what we do need to say is.
here is this pointer type that exists, that satisfies the Api, and also satisfies, like Otlp. Requirements of you know, or whatever, being something that we can assume, exists in P data.
You know.
**Liudmila Molkova** 10:08 I would imagine that this pointer does not have to be visible to the end. Users.
**Austin Parker** 10:14 Right? It's correct.
**Liudmila Molkova** 10:15 It should work, it should not affect the public. Api. Your back end ideally makes it transparent at the query time.
And then it's a pure optimization and addition.
You provide whatever you provide. Then.
Yes, symmetry. Yeah.
**Austin Parker** 10:30 The SDK needs to be aware of it, though, because you need to be able to have.
like a resource processor or an entity processor, or an attribute, or something that is capable of saying. I want to take the thing you have given me and turn it into a pointer.
**Liudmila Molkova** 10:50 Right, and if your backend does not support it, it goes as is.
**Austin Parker** 10:56 Yes, with some.
Yes.
**Liudmila Molkova** 11:03 And in this, and sorry I I love this idea of the pointers.
I, we can talk about this. But in the context of this setup. It's an optimization. It's.
**Austin Parker** 11:16 Yes, no, I I'm agreeing with you that for this Otep. Yes, we should say the Api can accept that. That extended attributes are universal like. I'm agreeing with you there.
And the actual web term. What? What makes them? Whatever is something that is at the SDK, not the Api.
**Trask Stalnaker** 11:42 We already have. Oh, sorry! Go ahead, Robert.
**Robert Pająk** 11:47 You just wanted to say that I remember that I think the auto template there was something like the future future future future future possibilities. I think you have it even in this Ulta.
So I just would maybe just having a small sentence.
just not to, you know, over complicate the otap, and just to put it there.
**Austin Parker** 12:10 I like. I like that as a solution.
**Liudmila Molkova** 12:22 Yeah, I really don't understand how we can make progress since we have tastes conflict, and some people actually prefer it to be the same, and some that this have extended attributes everywhere, and some people are pushing back against it.
Under how much this agreement we are ready to take here, and how we make those people also talk to each other like Tigren and Dan.
**Robert Pająk** 12:59 Right now is to not make any. Do not use anywhere, must or must not at this point of time to make it optional.
I think it's currently like that.
Yeah, but I'm not sure. For example, if right now, the Api doesn't something like Must or the I do not remember just to make sure that all of these things are just, you know.
At least, that's my proposal.
**Liudmila Molkova** 13:34 We are very.
**Robert Pająk** 13:35 They must support settings.
**Liudmila Molkova** 13:38 On spans, logs, profile, span links. Well, those are non controversial, right? Nobody disagrees. We should provide them. There.
**Robert Pająk** 13:49 Yeah, you're right. You're right.
**Trask Stalnaker** 13:51 Oh, so it just didn't get changed. Based on the discussion based on Tigran's feedback like this.
This note I put in here is still there of basically allowing dynamically typed languages to do something different.
**Robert Pająk** 14:10 Yes.
**Liudmila Molkova** 14:13 Right.
**Austin Parker** 14:13 Is, should less, no should is more than may right.
**Robert Pająk** 14:21 Yeah, recommendation.
Could you go further and maybe try to find a must?
SDK must support.
**Liudmila Molkova** 14:31 To match this.
**Robert Pająk** 14:32 Yes, same.
**Liudmila Molkova** 14:45 So this, this is the actually, what also done wearing his Gs hat doesn't like that. It bloats. It increases the number of code that is actually used and not erased at the compilation time.
**Austin Parker** 15:11 Is it?
I mean? Is it worthwhile to.
**Robert Pająk** 15:24 To me. I do not understand this argument. You could say that you cannot accept nothing, because you can say that it increases the package size. You can say to the measurement processor that you do not want to add it to the SDK, because it will increase the SDK size and things like that that, for example, for the browser stuff, I kind of understand that the you know the Maintainers may just implement some part of the specification, you know some light version.
but saying that you cannot implement, you know, equality and things like that because it will increase the SDK size like. Personally, I do not understand it.
**Austin Parker** 16:12 Kaiser people are weird. I mean.
when making the should a may here satisfied.
**Liudmila Molkova** 16:24 Maybe we can do this, that presumably some of especially Javascript, and maybe some other languages would expose different types or type aliases for standard and non standard attributes.
and they would or end up restricting met like restricting, using extended attributes and metrics. Right or yeah.
instrumentation scope, identifying entity attributes. We can say here that if you are exposing.
and if you are allowing complex attributes on metrics, or identify an entity attributes here this guidance applies to you. If not, it doesn't.
**Austin Parker** 17:21 It doesn't. I like, I think, that might be a good compromise cause that actually, that makes sense. Because if cause realistically.
the any value. Diva quality follows from the may use case.
**Trask Stalnaker** 17:39 Right.
**Austin Parker** 17:40 It doesn't follow from the must use case.
so if you have the may, you, if you have the May use case, then you should make you should support deeper quality.
If you don't do that, then you don't need to, because it's not really relevant to you at that point.
**Liudmila Molkova** 18:41 Sorry I didn't learn how to type yet.
Okay.
**Trask Stalnaker** 18:49 Yeah, where's the microphone button here in Github? You.
**Liudmila Molkova** 18:54 The problem is, I didn't learn how to speak yet, either.
Okay, So I I don't believe we will get an approval from Dan. I think he was.
Explicit that he doesn't really enjoy the spirit of it, but he doesn't want to block it either.
I wish we still had some. Go ahead, trust.
**Trask Stalnaker** 19:29 I think it's okay. I think what we, this group.
should just come back to the spec and say, you know, we've discussed, this is our final answer. This is our final recommendation from the log. Sig.
I would like to probe Josh Offline a little bit more. Maybe you and I, with Miller, can have a even a chat with him to see.
I would love to get his approval if we can.
**Liudmila Molkova** 20:07 Yeah.
**Trask Stalnaker** 20:08 We just, we merge it, and we move forward.
**Liudmila Molkova** 20:17 Yeah, that's what I was. I was also thinking about that Josh, check in with Josh. If he has any anything that high level oh, Tiger, and approved, that's wonderful.
Okay.
So.
**Trask Stalnaker** 20:37 Yeah, and we can. I can ping Dan, just to see if that note that, I added, because I added that note kind of to explain that I'm curious if that note addresses, or if it's like you said, it's more like the spirit of then why.
yeah.
**Liudmila Molkova** 21:01 Yeah, I it would be wonderful if you reach out. I I last time on the spec call. I asked. If he is.
if his feedback is more on the Gs side or the spec sponsor side.
and his point was more that the general wider than Javascript. But maybe you're always more convincing than me.
**Trask Stalnaker** 21:24 Right.
Wish me luck.
**Liudmila Molkova** 21:29 Bye, yeah.
cool. I I can reach out to Josh and see if he's interested in talking through things where he would make another pass.
**Trask Stalnaker** 21:41 Awesome.
And then, yeah, let's just plan. On closing it down next Tuesday.
**Liudmila Molkova** 21:53 Yeah. Sounds good.
cool last point on this, just a small update. I got a bunch of comments that attribute limits need to be reworked, extended their discussions, and I move them away from the adapt because they are. All these questions need to be answered, regardless of whether this adapt lens.
**Trask Stalnaker** 22:28 Yeah, I think that was good idea.
**Liudmila Molkova** 22:31 Yeah, thanks, Robert, for suggesting it. In the 1st place, cool.
Then I guess that's it. We'll try to finalize it edit comments in the Add Up Robert, I think you added this one.
**Robert Pająk** 22:55 Yeah, mostly, Domira. I wanted feedback from you, but I can trust as well. So I'm just sometimes not sure what our one thing is, I think you're okay with this proposal.
So the only think here is to how to refine the policy so base. Basically, there is a conversation already regarding the policy.
But also there are some comments from the Primitives Maintainers which I'm not sure if I understood correctly, to be honest.
So even double checking my conversations. If I'm answering, the questions will be helpful. To be honest.
**Liudmila Molkova** 23:47 Yeah.
**Robert Pająk** 23:50 Oh, I see, there was a comment when I was driving.
**Liudmila Molkova** 23:57 So I I know we had this discussion at the spec, and I'm sorry if I'm given the conflicting answers I still don't get why we need. We need this prefix, and I think it does not.
**Robert Pająk** 24:13 Okay.
So this prefix is needed. So, for instance, if you have a backend or something which processes and uses the still uses the auto model, even though it understands the protocol. For instance, you have the Prometheus receiver.
Then, thanks to this attribute, you're able to distinguish a metric attribute from a scope attribute. So then, when you're processing later and you're exporting it, using, for example, Otlp, you're exporting it properly as a scope attribute and not as a metric attribute.
**Liudmila Molkova** 24:49 I see. So then, the source of data is up in telemetry. It has scope attributes. There is Promedius in the middle.
**Robert Pająk** 24:56 Yeah.
**Liudmila Molkova** 24:57 Then it's almost over to Otlp again.
**Robert Pająk** 25:02 Yep, and such. I know that such weird things happen in the wild.
**Liudmila Molkova** 25:09 And it hurts everybody who uses hotel. And then Prometheus.
**Robert Pająk** 25:16 What hurts do you mean?
**Liudmila Molkova** 25:18 So let's say I had an attribute, let's say.
in development.environment.name set to prod right. It was my resource attribute.
Now I am scraping hotel metrics right or receiving them. This Promedius.
**Robert Pająk** 25:40 Resource attributes are a totally different thing, because there's a separate, I think targeting for metric, which is only about yeah.
**Liudmila Molkova** 25:49 Oh, okay, okay. So okay, there isn't. Some, some scope attribute that has a well defined up in telemetry, meaning, I don't know.
Gcp service something that describes what service I'm talking to like I don't know. Storage.
**Robert Pająk** 26:07 Yep, it hasn't its place in the scope.
**Liudmila Molkova** 26:11 It has a semantical meaning now.
**Robert Pająk** 26:14 Yay!
**Liudmila Molkova** 26:15 It's the name is changed to hotel dot scope dot something.
and there is nothing that transforms it back. If I'm just stopping at the Prometheus. Now, instead of well-defined semantic attributes, I have something else.
**Robert Pająk** 26:33 Correct.
**Liudmila Molkova** 26:36 But it helps that if, after the premiers, there is also another auto that would remove our telescope.
**Robert Pająk** 26:45 Yep.
**Liudmila Molkova** 26:46 And we need to pick who who hurts more.
Also the if it's the collector case, then collector can have access to the semantic conventions, and in theory it could know that it was intended as an instrumentation, scope, attribute.
**Robert Pająk** 27:05 Yeah, but they can be also custom, scope attributes.
**Liudmila Molkova** 27:09 And then they can define like maybe a year from now they will be able to define their own semantic conventions, and collector can download it.
**Robert Pająk** 27:18 I see.
**Liudmila Molkova** 27:25 At the same time, I'm not worried about it because nobody uses instrumentation, scope attributes, as far as I know.
**Robert Pająk** 27:45 Maybe it could be optional.
I'm not sure if, yeah, the problem here that I see reasons for both solutions like you said.
especially if it will be something like, I don't know Zipkin, or something which probably you cannot really.
You know, transfer further.
So yeah, I'm.
**Liudmila Molkova** 28:15 I have.
**Robert Pająk** 28:15 Do hip right if you have any proposals how to drive further, I'm just open.
I kind of. Also.
I think it's also acceptable that the premiums you know, compatibility will differ from the general non otlp compatibility guidelines. I think it can be acceptable as well right that we are creating a specific guidance, which is a little bit different at the same time. Why.
it will going to be different. So yeah, I'm puzzled.
**Liudmila Molkova** 28:56 What is there any anything in the practice bad that would happen if we don't like? I totally agree with the Schema, URL. I think it makes total sense to to translate it into a telescope. Schema URL it has a special meaning. It can be singled out, and you can support it regardless.
when it comes to attributes, let's say we don't prefix.
Okay. If somebody added instrumentation scope attributes. If they manage to do it, wow.
then they will be translated into metric attributes instead of the instrumentation. Scope is the 10th of the yes.
**Robert Pająk** 29:48 I think I think, for the primitive compatibility sick. It was kind of end of the world. I think you can see the 1st comment from David.
just control F, David, yeah.
Or the the ash, the ash. Yeah.
**Liudmila Molkova** 30:09 Right.
**Robert Pająk** 30:11 Dash I will.
He even thought about adding this arter which is even stronger. But yeah, I think we we we all convinced that the other is even more than but I think you can go into, took his further comments when he tried to explain why this here.
**Liudmila Molkova** 30:39 Sheriff domestic structure to be able to distinguish scope attributes from data likelihood of collisions it so there are 2 points, the collisions which I'm happily to argue with. And the second point is the prisoner
**Robert Pająk** 31:11 I think it's more about distinguishing rather than collisions.
**Liudmila Molkova** 31:18 Right, and Rob means to distinguish, and you're away.
It could be done through. I don't know. You could put this whatever metric metadata. What? What is there in the Promedius, where you can dump some random stuff to help you distinguish? There could be, say channels, the semantic conventions.
**Trask Stalnaker** 31:48 We've one thing that related that we've never really addressed. Is the around scope attributes is.
can we cause we've thought about? Well, can we just our scope attributes the same, just like as regular attributes like, can we take a semantic convention?
Db, dot system and bump it up to a scope, attribute and is it the same thing? And if we had answered that question of saying that, hey, it's it's the same thing at the end of the day semantically.
Then, we would have an answer. Here.
**Robert Pająk** 32:33 Yes, I agree.
**Austin Parker** 32:35 Isn't it, though?
I mean, I'm just surprised that we need that clarified.
**Trask Stalnaker** 32:45 Support that clarification for what it's worth.
**Austin Parker** 32:51 I'm not saying that people might not realize it, but my understanding, I mean I I thought that was one of those like accepted as true things, where scope attributes are the same as any other attributes, except they apply to all children of the scope.
**Trask Stalnaker** 33:07 I think the discussion on this Pr. Proves that it's not a.
**Austin Parker** 33:11 That's good observation.
**Robert Pająk** 33:13 Who are not.
**Austin Parker** 33:14 A good signal is this one of those nobody actually uses? Scope attributes so so nobody knows how they work.
Cool.
**Liudmila Molkova** 33:29 So if we were to change it.
and it would be something in this pack saying that you can populate scope attributes for the things that you know, that apply to everything instrumented with. Let's say this tracer or a Med. Peter.
**Austin Parker** 33:51 Yeah, I mean, I think that's the clarification I can't imagine.
Okay, let me track myself. I can imagine that people have not been using it for that, but.
**Liudmila Molkova** 34:04 That's great, actually.
**Austin Parker** 34:08 How is it breaking.
**Liudmila Molkova** 34:11 So let's say you look very your data, and your backhand does not do this pullback for you.
Then you query the regular attributes. But what you're looking for is not in them. It's in the instrumentation scope ones most expensive.
Then record them.
**Austin Parker** 34:41 Okay. Well.
**Trask Stalnaker** 34:43 Same with that collector transformer. I see.
**Robert Pająk** 34:46 Yes, all the.
**Trask Stalnaker** 34:47 Oh, sir!
**Robert Pająk** 34:48 So the only problem I see is that if you have this kind of processors and stuff like that, then if there is something which needs to look for an attribute, then should look for both Scott attribute and like leaf attribute right?
And then, because it's not specified anywhere, nobody really does it, and there's probably no, no things which make it easier to handle it this way.
**Liudmila Molkova** 35:20 Kind of feel we should call it a day on instrumentation scope of attributes. They they've been out there for a while. Nobody actually made use of them because we we didn't give any to link to make use of.
**Austin Parker** 35:38 Suppose that's true, although I mean what you would replace it with is logical scoping? Right? You would just say that.
yeah, that would suck. But yeah, you could just say that you should infer the scope of an attribute based on its position in the hierarchy and the namespace.
**Liudmila Molkova** 36:10 We would replace them with pointers. Right? We would say, okay, for this data structure.
**Austin Parker** 36:19 Yeah, I mean, I guess that would also work.
Actually, yeah, no, that would be the way to do it is, you would just say, like.
I mean, you aren't changing the definition of scope attributes. In that case, what you're changing is you're changing where they appear in the Otlp envelope.
**Liudmila Molkova** 36:39 And we're changing
**Austin Parker** 36:41 Yeah, it's on.
**Liudmila Molkova** 36:45 Yeah, things are changing the granularity. Right? So you're saying, Okay, there's this scope. It's not per meter. It's just an arbitrary thing that user up controls. Let's say your instrumentation controls.
**Austin Parker** 37:00 Yeah, yeah, I mean, it's yeah. It's just it's anything emitted by this tracer. For example.
when I create a tracer, I hey, when I created tracer, I initialize it with an attribute bundle.
The SDK transforms that attribute bundle into something and replaces it with a pointer to the kind of location of those values.
**Liudmila Molkova** 37:43 Or you say, Okay, I've got this incoming request. Here is the metadata. I want to be associated with which, with each telemetry item emitted in the scope of this request.
And it's no longer the per tracer, perimeter granularity. It's per I don't know her.
**Austin Parker** 38:05 Or, yeah, it's per.
yeah. That would actually make a life a lot easier on the front end if you could do it in a lightweight way, because then you could say you could just easily associate back to it. He could just have a a key or something.
and the key is your session. Id.
And then that key just constantly points to whatever.
wherever you're putting all that shit, it makes some things a lot easier. It makes the Sdks significantly harder, though.
**Liudmila Molkova** 38:46 Yeah.
**Austin Parker** 38:47 I guess the sdks are already pretty hard.
**Liudmila Molkova** 38:51 Oh, I it's also very far fetched. I'm thinking how we can make progress on on this year. I'm thinking, okay, what we cannot do is, we cannot say that the telemetry item attributes can also appear in the instrumentation scope.
Right? We can say the opposite, though.
**Austin Parker** 39:13 The opposite is true things that are. Yeah, we, we can say that they will either appear once in the scope they will appear repeated. They will appear repeatedly on leaf leaf items.
**Liudmila Molkova** 39:26 Right, but things like you don't need to fall back when you query for for this.
but you can dub double pump as well.
**Austin Parker** 39:36 Yeah.
I mean, you can definitely. I think you could. I think we could. Maybe. Would that be a non breaking clarification, then that if they appear, they appear in only one.
**Liudmila Molkova** 39:54 If.
**Robert Pająk** 39:54 What does it mean?
**Liudmila Molkova** 39:55 If you, if you can populate instrumentation, scope attributes, you should populate them. If you right, populate the per item, it is.
**Austin Parker** 40:06 Right, if you yeah, exactly. So if you, if you can put them on, if you can put things that should be on the scope on the scope, then put it on the scope, and if you do, put them on the scope, then they don't appear on the on children. If you cannot, then they only appear on the children and they, and it is an error for them to appear on the scope, so you can't double up which would make this which would solve this problem right?
**Liudmila Molkova** 40:39 Right, assuming that.
**Austin Parker** 40:41 No matter.
**Liudmila Molkova** 40:41 Of course.
**Austin Parker** 40:43 But we're we're saying it would be an error for there to be a collision.
**Liudmila Molkova** 40:48 Oh, we can't even allow the collisions, and you probably say that I mean, if they happen by accident, it's not nothing breaks. Actually, if there is a collision.
**Austin Parker** 40:58 Right. I think we just say like.
**Robert Pająk** 41:01 We'll leave. Live takes precedence. Probably.
**Liudmila Molkova** 41:04 Okay.
**Austin Parker** 41:05 Yeah, like, I think we would just like give a precedence. And say, I, I think you would just say, like, 1st one wins like you check scope first, st and then if scope if it checks scope first, st if it doesn't, and if it appears in scope, then scope wins.
Or maybe.
Yeah, I don't know which which way is right. There.
**Trask Stalnaker** 41:30 That's like that.
More specific sensive wind. Yeah.
**Austin Parker** 41:37 Yeah.
I'm just thinking, if we're trying, are we trying to optimize for correctness? Are we trying to optimize for not having to process, each leaf node, or do we care.
**Liudmila Molkova** 41:56 Think we're doing damage control.
**Austin Parker** 41:58 Lipstick.
**Trask Stalnaker** 41:59 Okay, then, in that case, yeah, just say more. The most.
**Austin Parker** 42:05 Say it's an error for it to appear on both.
**Trask Stalnaker** 42:09 Least surprising.
**Austin Parker** 42:11 Yeah. But if it does, then last thing.
last thing most specific thing wins.
**Liudmila Molkova** 42:21 Okay?
And then it sounds like something for the pack, right?
**Austin Parker** 42:33 I think that is the spec clarification. Yes.
**Liudmila Molkova** 42:39 We recently moved the instrumentations.
Oh, here, right!
And would be another sentence here.
**Austin Parker** 42:54 Under instrumentation. Scope. Yeah.
**Liudmila Molkova** 43:01 Okay, I can capture this discussion in the comment, maybe in the issue on the spec and link to the so this 1! 0, sorry!
This one!
**Austin Parker** 43:20 To the the issue is only semantic convention, semantic conventions. But I'm not sure if it matters.
I mean, it's gonna mostly come up at same calls right?
**Liudmila Molkova** 43:38 There is no nothing about instrumentation scope, and the some conf, so we can document stuff there. But I don't think it will be discoverable or.
**Robert Pająk** 43:47 Yes.
**Liudmila Molkova** 43:48 Right place. I think the some sentence here is saying this would be.
**Robert Pająk** 43:56 Below optional attributes. Some. Yeah.
**Austin Parker** 44:00 Yeah, I think.
**Liudmila Molkova** 44:00 I think you need it. Both places, I think.
**Robert Pająk** 44:03 Okay.
**Austin Parker** 44:04 Because I think the other thing that this interacts with is like weaver, quite a lot.
**Liudmila Molkova** 44:11 If only we had instrumentation scope ever defined in semantic conventions, it would.
**Robert Pająk** 44:20 Ultimate. I just think that even this example here which says about the system name.
it's kind of an example. Why, it can be instrument issue scope and not just, you know. For example, a span attribute right?
Example number 2. Right now, here.
**Austin Parker** 44:38 Yeah, like the fact. Yeah, like nobody. Just because nobody read. This doesn't mean it doesn't exist.
**Robert Pająk** 44:44 Yeah.
**Liudmila Molkova** 44:46 It's actually would go against semantic conventions to put it in the instrumentation scope.
**Robert Pająk** 44:52 So yeah, we'll.
**Austin Parker** 44:53 Okay.
Okay. Well.
**Liudmila Molkova** 44:57 But it's it's actually a good thing to clarify.
No.
**Austin Parker** 45:02 Then we yeah. Then then some companies.
**Robert Pająk** 45:05 Yeah. So now the question is, do you think that it will be good to add the dB system name or to the instrumentation scope. If you're, for example, using SQL. Server library that you're instrumenting.
**Liudmila Molkova** 45:20 No, but only because we already documented, as the let's say, span attribute in semantic, in database semantic conventions. Let's say, tomorrow we have a full Bar system name.
If we could put it in the instrumentation scope, it would be more optimal. And we can say, Okay, put it into the instrumentation scope where you can.
**Robert Pająk** 45:43 I see.
**Liudmila Molkova** 45:44 And if you cannot, you put it into the attributes.
But then, okay, so.
**Austin Parker** 45:50 It wouldn't be breaking for this specific thing, but it would force backends to actually.
**Liudmila Molkova** 45:57 Implement, the fallback.
**Robert Pająk** 45:58 So. So if for the backends it's something different, then I think, adding, this prefix is also good for the backends, and I think that's the reason why people want this prefix autoscope. For the same reason.
**Liudmila Molkova** 46:13 Out prefix helps.
**Robert Pająk** 46:17 Because they'll know that that it is an instrumentation scope, attribute, and not a regular attribute, so same as here, instead of you know. So if there's a back end which understands the distinction between a scope attribute and you know a leaf attribute.
then it can use this kind of information when parsing the model.
so if they know that they can expect only the dB system, name only on the instrumentation scope.
then they will parse differently.
**Austin Parker** 46:49 Let me see how we handle this.
**Liudmila Molkova** 46:54 And the backends know the otlp compatible backends know already. They don't need a prefix to know. Only non Otlp backends don't know.
**Robert Pająk** 47:06 Yes.
But, for example, what about the what about the collector?
Through collector receivers? Yeah. Collector receivers.
**Liudmila Molkova** 47:18 It's up to the logic on top of the receiver to explore instrumentation, scope attributes at all right.
**Robert Pająk** 47:29 Yeah. So basically, that's why this auto school prefix has been added to make it working for the collector receivers. So it was done for.
**Liudmila Molkova** 47:38 Yeah.
**Robert Pająk** 47:39 So basically, this kind of autoscope was being added just for for the sake of receiver. So then, it can be translated to something other.
**Liudmila Molkova** 47:53 Right, but having the hotel scope inside, instrumentation, scope, structure, and Otlp doesn't make sense.
**Robert Pająk** 48:03 Yes.
Correct.
**Liudmila Molkova** 48:09 And when you query, if you're the end user, you don't, you probably don't care.
You don't want to know about hotel dot scope same, Peter.
The only good solution at this point, I see, is we just nuke attributes from instrumentation school and say they are deprecated. We couldn't find a way to use them, or they conflict with everything we've done so far.
Or, yeah.
**Austin Parker** 49:01 So they have to see how we translate them.
or if we do it all, I'm pretty sure we do.
**Liudmila Molkova** 49:09 You're probably the minority, I think. Jaeger drops them. I think Grafana drops them.
**Austin Parker** 49:16 Everyone jumped up a bridge, would you?
I get what you're saying.
**Trask Stalnaker** 49:29 Where are we at?
**Austin Parker** 49:31 Talking about instrumentation, scope attributes.
**Trask Stalnaker** 49:34 Oh yes!
**Austin Parker** 49:39 Let's see, we map scope, name, library, name, map, scope, version, library version merges any custom scope attributes.
So yeah, we use flatmap. The weirdly enough. We don't do that for metrics.
However, we do what you are supposed to do with them, which is, when we see a scope attribute. We not only merge, we we flat map it down to all the child. All the child spans, so it works exactly like setting tracer level attributes did, and open tracing where you would create a tracer.
**Robert Pająk** 50:20 I'm on it.
**Austin Parker** 50:21 Or when you created an open, tracing instance, you would say, Here's the things I want all these children to have in common, and then you would write them once, and then it would get added to the attribute body for the or you added to the attributes for the children. So it's actually kind of surprising to me that Jaeger drops them, because Jaeger, to my knowledge, also did that.
or it should have at least
**Robert Pająk** 50:49 Also do not think they dropped them. Yeah.
**Austin Parker** 50:52 Yeah, I'd be surprised. They dropped the room.
I'd have to go, I would have to go look and then I might bye.
**Robert Pająk** 51:00 Think also that the collector components started adding some instrumentation scope attributes when they are adding some information about the components themselves.
I think.
**Austin Parker** 51:14 Yeah.
**Robert Pająk** 51:14 That.
**Liudmila Molkova** 51:18 So what is, yeah.
**Austin Parker** 51:20 Oh, yeah, I mean, I don't think we can. I mean, I don't.
I don't think we can get rid of them. I think.
like, I think, a clarification of like, hey, you can do this this way. You can do this that way. Right? You can either.
It is correct. It is okay to take things. And if you have all these shared attributes for all children of a tracer, it's okay for you to put those on the spans directly.
It is better if you have attributes that are shared between all children of span to put those in the instrumentation scope.
What is not okay is doing both at the same time with the same attributes.
And if you do that.
then the only guarantee we are going to make is that the most specific thing actually counts.
and it is a and and for the purpose of this, like non otop export thing, that it is okay for that to be a lossy conversion, because ultimately either is fine, right? Like it's fine if they're under the scope, and it's fine if they're on the children directly. So we don't actually care if you lose that information on export or converging to non otlp.
And here's what happens if you do that.
But then, and also, in addition to all this, go, make sure that Semcom is aware that, hey?
Did you read this part of stable spec.
Maybe have that factor into your deliberations from here on, out.
**Liudmila Molkova** 53:00 Yeah, I'm thinking, we kind of need to.
Eventually, we need 2 separate recommendations that that work together. One is for the end users or for instrumentations.
so you can put them either in either place. But maybe instrumentation scope is preferred.
**Robert Pająk** 53:20 Yes.
Question. I have a question.
I do not say that we need to do it, but just for sake of discussing multiple options. I think we can have a preference to emit the instrumentation scope attributes. You know the keys as they are, but I think we may allow an option to, you know. Add this kind of prefix. If someone wants to have this you know loss
**Austin Parker** 53:49 If they want a non lawsuit. Yeah.
**Robert Pająk** 53:51 Because I think it might be important, probably not for the, you know, destination for the endpoint backends. But I think it might be important for some processing pipelines. When you know someone is basically, you know, converting and using primitives and not otop. Yeah.
this is, I think, the worry of the Prometheus seek.
**Austin Parker** 54:11 I think it's fine to say. Hey, here's an option for you.
**Robert Pająk** 54:14 Yes, exactly, and some asterisk note. It's possible also to add this auto scope.
**Austin Parker** 54:20 Yeah.
**Robert Pająk** 54:21 It's also fine.
**Austin Parker** 54:23 But there's also, so I guess my other. My, my one question is there, are it? See?
Like name and library version can't collide right like there are dedicated scope attributes.
**Liudmila Molkova** 54:41 There are for properties, not attributes.
**Austin Parker** 54:46 Oh, correct, sorry!
Are they happy to?
So in this issue? Are they also looking to normal to normalize those properties with this hotel dot scope prefix.
**Liudmila Molkova** 55:02 Oh, I already have them.
**Robert Pająk** 55:03 Yes, we just don't have the scheme.
**Austin Parker** 55:09 Okay.
**Robert Pająk** 55:10 But yeah.
**Austin Parker** 55:16 Actual span ultra component ultimate name.
Oh, this is a different one.
Yeah. Oh, telescometric. Okay?
**Liudmila Molkova** 55:25 So this 2 are new, that Robert is adding this, 2 are old.
**Austin Parker** 55:29 Okay?
I mean, yeah, I guess I would say it's optional, but it's a lot optional. But allowed.
**Liudmila Molkova** 55:41 But I don't want to add this in semantic convention, so I don't.
**Austin Parker** 55:45 No, I I would agree. I don't think this should be in some com, because I think that because again.
all of those keys can be present on either. And the pro where they are is not an end user concern.
Right? Like.
if I'm an end user and I know my, and I want to query for all of my, you know.
database name equals sequel. It should. I shouldn't have to specify like, where was that defined? It should just exist.
**Liudmila Molkova** 56:22 It should be transparent. Yeah.
**Austin Parker** 56:24 Exactly, and back ends have a choice of how to do that. They can either do the they can either splay those out on ingest they can do that through joins. They can do whatever the fuck they want. I don't care. But yeah, like I'm I'm in agreement that we don't want that leak, that that is a detail that we should not leak into some conv.
This felt productive.
**Robert Pająk** 57:00 So do we have some. So do we have some non otlp exporter specification that we want to put in, or this was migrated for the specification. This kind of things and options.
**Liudmila Molkova** 57:14 I it.
I am super supportive of the Schema URL. I think there are key.
**Robert Pająk** 57:21 Yeah, yeah, I know. I just thinking about attributes.
If we where we should add this portion of the language that scope attributes can be, you know, added, as attributes.
**Liudmila Molkova** 57:37 I would imagine it's done up to the specific exporter, like the Premier's compatibility, may find them, but I would not.
**Robert Pająk** 57:48 Could you try to quickly check the specification and try to find a file? Non, non, I think no, I think there's also some.
**Austin Parker** 57:58 It's under. I thought it was under Otlp.
**Robert Pająk** 58:02 Specification compatibility. I think there's also something dedicated for non tlp, here on the same level mapping to non into a OP. I think it could be put here.
Yep.
Probably this is the place.
**Liudmila Molkova** 58:21 And that then it would be that you probably want to record them as is. But you may for some reason.
**Robert Pająk** 58:32 Yes.
**Liudmila Molkova** 58:35 Okay. I'll work on that.
**Robert Pająk** 58:37 I think I know what? What is the path? So just maybe 1st adding the scope, URL in the cementing conventions, and here, here and there because it is not controversial at all, and then creating a separate information about instrumentation, scope attributes probably only here.
**Austin Parker** 58:55 Yeah, that sounds good.
**Liudmila Molkova** 58:57 Yeah.
**Robert Pająk** 58:57 May. The only reason why it may be good to have is semantic conventions. If someone wants to opt in, he can use weaver to have, you know, kind of this helper methods, for instance.
**Liudmila Molkova** 59:09 And Dave can't, because weaver does not support instrumentation, scope, nothing.
**Robert Pająk** 59:13 Oh, okay. Yeah. Okay. Okay. Yes. It doesn't matter.
**Liudmila Molkova** 59:19 I'll create an issue. I'll try to capture the the this discussion. I think it's helpful for Instrumentation school going forward.
**Robert Pająk** 59:27 Okay.
Thanks.
**Austin Parker** 59:30 Yeah, sounds good.
**Liudmila Molkova** 59:32 Yeah, thank, you.
**Austin Parker** 59:33 Alright!
**Trask Stalnaker** 59:34 Thanks.
**Robert Pająk** 59:35 On time.
**Liudmila Molkova** 59:37 Oh, yeah. Have a good day.
**Trask Stalnaker** 59:38 Okay.
