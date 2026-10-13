SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-12
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 03:10 Hello, hi everybody.
**Aaron Abbott (Google LLC)** 03:16 8.
**Liudmila Molkova** 03:24 Yes, let's get… Started… Do we have… Okay.
So, I added some things to the agenda.
Don't know if we need to go here, if people have anything specific they want to bring up.
Please put it here.
Anywhere?
And I was.
I added parts. Erin, I don't know if you want to talk about them, but I was thinking maybe at least we can merge the couple of first ones. I don't think we need more than one approval on those. They are not changing anything for Semantic Conventions.
**Aaron Abbott (Google LLC)** 04:36 Yeah, I think that's what we said on Friday, too. I don't know if Trask was gonna take a look, but… Yeah.
**Liudmila Molkova** 04:45 Let's just merge. We had a chance.
**Aaron Abbott (Google LLC)** 04:50 you.
**Liudmila Molkova** 04:53 And it's… it's non-consequential.
Easy to change at any point later.
**Aaron Abbott (Google LLC)** 05:03 By the way, can you do that from the second one with the stacks? Is it possible to just enqueue both of them?
**Liudmila Molkova** 05:09 It's too late. Or I can…
**Aaron Abbott (Google LLC)** 05:11 Oh, no, it's fine. It's just a question.
**Liudmila Molkova** 05:14 I can remove, or you can remove and enqueue from the second one.
**Aaron Abbott (Google LLC)** 05:18 It's fine. Don't worry about it.
**Liudmila Molkova** 05:20 Okay.
So, I wanted to talk about the CERT one. We had a discussion… I'm not sure if you had a chance to…
**Aaron Abbott (Google LLC)** 05:31 Yeah.
**Liudmila Molkova** 05:31 Okay.
**Aaron Abbott (Google LLC)** 05:33 I was chatting with, some different AIs to see what they think, and I.
I don't know, I… they… it seems like there's a couple… couple ways to do it. I think the not option… I don't know if it was clear what I meant by breaking change, but… I kind of wanted to make sure we have the same assumptions, so, like.
One thing you mentioned was producers, or rather, like, the utilgen AI shouldn't be able to produce the generic fallback, if I understood right?
**Liudmila Molkova** 06:07 Yeah, I think it doesn't make sense to produce it.
**Aaron Abbott (Google LLC)** 06:10 To, to, or, like, to allow or not allow?
**Liudmila Molkova** 06:14 It does not make sense to produce it, so we should not allow it.
Where we… we don't… we don't need to do anything about it, like, at least we should Document that we don't expect anybody to produce them.
**Aaron Abbott (Google LLC)** 06:29 Okay.
**Liudmila Molkova** 06:31 But I think they should be able to produce.
Arbitrary parts.
**Aaron Abbott (Google LLC)** 06:42 Like, Sorry, I was gonna say, so, like, in UtilGen AI, should we allow the escape hatch where they can produce generic, or should we… like, sure, some producers which have their own instrumentation will probably do it, and that's fine.
But, like, say in contrib… sorry, in Python GenAI, we're instrumenting some new provider, and rather than drop the data on the floor, we want to include it. Should we allow and util GenAI or not?
**Liudmila Molkova** 07:11 I think we should not.
The guidance we put in Semantic Conventions should tell them to drop data on the floor for parts.
that are not documented in Semantic Conventions or in the instrumentation. So there could be an instrumentation somewhere outside that uses utils, and I think it should be able to produce its own part.
that it documents in, let's say, its own Semantic Convention Registry.
**Aaron Abbott (Google LLC)** 07:41 Right, right.
Okay. I mean, I think we can make it work either way. I… I kind of liked… so I looked at, like, what Protobuf does for the JSON encoding for Protobuf Any, for example, and I think it's a little closer to what I proposed, because the.
It's, it's actually slightly different so there's, there's like an object and then the key.
The keys in the object are the variants.
And then the, The… any fallback would be a specific variant, kind of like what I said, so it would be, like.
I type here.
**Liudmila Molkova** 08:21 But, like, it would keep the type fixed.
For.
Generic, custom, doesn't matter.
And, when we… Expand semantic conventions to include new parts.
It would technically be breaking.
**Aaron Abbott (Google LLC)** 08:44 Yeah, so here, I don't know if you can see in the notes, but it looks something like this.
Oops.
This would be, say, like, image.
And then for the fallback case.
You could have… It would look something like this.
And then, say it was documented, it would be something like.
that.
Which, this is really different than what we have right now, since we have the discriminated… discriminated union with the type Inside, and then everything kind of flattened.
But I… I think… the benefit… it might… it might be a little bit beneficial to test this out, but I don't want to, like, introduce a ton of breaking changes if we can avoid it. It seems like a more disruptive change.
**Liudmila Molkova** 10:03 No, wait, this is not dis… I don't think it's disruptive at all, but, like, what happens if tomorrow We would add part.
through into Semantic Conventions.
Right?
**Aaron Abbott (Google LLC)** 10:17 Yep.
**Liudmila Molkova** 10:17 It would be breaking to every consumer. Oh, sorry.
Simply because we are saying that the list of types is fixed.
**Aaron Abbott (Google LLC)** 10:29 Yeah, I mean, I don't think we can…
**Liudmila Molkova** 10:32 Why?
**Aaron Abbott (Google LLC)** 10:34 Because then we can't, like, add stuff, right?
**Liudmila Molkova** 10:39 We can add stuff.
And then it means that the… List of types is open.
**Aaron Abbott (Google LLC)** 10:51 I feel like we're probably saying the same thing, to be honest. Like,
**Liudmila Molkova** 10:55 I mean, the generic, like, if we're saying that everything, only the three are allowed.
We're saying it's closed.
I don't expect anything else.
**Aaron Abbott (Google LLC)** 11:12 like, The generic is… the fallback, right? I guess I don't… are you saying if we add stuff to the Semantic Conventions later?
**Liudmila Molkova** 11:21 Yes, if we add stuff to the Semantic Conventions later, it should go into the top level parts. It's a known part, it's not a generic part, right?
**Aaron Abbott (Google LLC)** 11:29 Right, right. So maybe if I was to do TypeScript for this, it would be something like — Sorry, getting confused between Go… Sorry.
Yes.
And then, you'd have to have something like this.
**Liudmila Molkova** 12:12 I don't know TypeScript.
**Aaron Abbott (Google LLC)** 12:15 Sorry.
**Liudmila Molkova** 12:16 attendance.
**Aaron Abbott (Google LLC)** 12:17 Yeah, yeah, the point I'm trying to make is, like, we would allow future things to be added here, as in the consumer's contract would have to ignore values they don't know.
Umm.
**Liudmila Molkova** 12:27 Right, and we need to add it in the consumer contract, and the consumer contract is the JSON schema for now, at least.
**Aaron Abbott (Google LLC)** 12:33 Hmm.
Okay.
Do you think the thing that you proposed keeps it open for consumers with the not enum part?
**Liudmila Molkova** 12:47 I, I think so.
But like me, there could be other ways to say it, I guess.
**Aaron Abbott (Google LLC)** 12:53 Yeah, because my concern there was that The type allowed in the fallback.
has to be not one of the enum things, and when we add a new enum value, like, like, basically what Felix was saying.
If they're producing something today, consumers know to… Ignore it for now, but then when we add it to the Semantic Conventions, there would be like, a key collision, right? Like, say it's document. We add document, and then they already are sending document.
**Liudmila Molkova** 13:24 Oh, they can keep treating it as… if they have the old JSON schema, they can keep treating it as a node. Nothing changes, right?
**Aaron Abbott (Google LLC)** 13:37 Yeah, yeah, that's true.
I guess I'm assuming that… Instrumentations will be out in the wild producing stuff for, like, a long time.
**Liudmila Molkova** 13:47 Yeah, and they will keep producing it, and consumers can keep treating it as unknown stuff.
So there is no, like, default deserialization that would… It's some hand-rolled stuff, however you write it, that reacts to this.
**Aaron Abbott (Google LLC)** 14:04 Right. I think the concern is more like if this is the consumer, right? In this code snippet. Yeah.
**Liudmila Molkova** 14:11 Yeah.
**Aaron Abbott (Google LLC)** 14:11 Yeah, so just taking, like, tool call response as an example. Say there's an instrumentation out there before tool call response was added to the schema. I know it's always been there.
But if it was out there producing something that had, no response.
The response field wasn't set, right?
Because it was produced.
**Liudmila Molkova** 14:34 So it match here.
**Aaron Abbott (Google LLC)** 14:38 there But it wouldn't, it wouldn't though, because the part type could be the same.
**Liudmila Molkova** 14:44 Wait.
Are they aware of this part type or not?
**Aaron Abbott (Google LLC)** 14:47 No, that's what I'm saying is like a producer could produce the part type that gets used in the future in the Semantic Conventions today.
**Liudmila Molkova** 14:56 So, if… If this instrument… if this consumer didn't know about this part type, it would not be here.
**Aaron Abbott (Google LLC)** 15:09 Maybe, I feel like I… or saying the same thing, maybe, but I can just reply on the issue. I think I'm not…
**Liudmila Molkova** 15:15 Okay.
**Aaron Abbott (Google LLC)** 15:16 Yeah, not expressing myself well, sorry.
**Liudmila Molkova** 15:24 Okay, cool.
So I guess there are two principles, right? The first one. Producers should not… produce.
Really.
Generic parts.
That this is only this, the, like, actually… sorry, I don't know what… Put it into my fingers. I think these two parts are the only things that I really care about. How? It doesn't matter. We can just write it in text.
Like, it's just it would be very unfortunate if we cannot express it with JSON schema, but we we should be, it's a common problem.
**Aaron Abbott (Google LLC)** 16:38 Yeah, so just to be clear, what's the difference between the producer should and the producer's may bullet point there?
**Liudmila Molkova** 16:47 so, we could say that you cannot produce any parts that are not in Semantic Conventions.
Or we can say you can produce.
things that are not in Semantic Con… in the Semantic Conventions GenAI.
**Aaron Abbott (Google LLC)** 17:12 I don't know if we should say that, though, right? Like…
**Liudmila Molkova** 17:17 I don't… I don't… I'm not saying we should say, like… This, I think we should say, because it's a guidance to instrumentations.
But… We don't have to say this if we support the types that allow it.
**Aaron Abbott (Google LLC)** 17:40 Like, what's the difference between custom and generic here?
**Liudmila Molkova** 17:48 The generic is generic. You don't know what you're producing.
You just use a generic type and put some crap into the body.
**Aaron Abbott (Google LLC)** 18:00 Hmm.
**Liudmila Molkova** 18:01 The custom is something like you, you care about.
And you know it's not… it just doesn't match what's in Semantic Conventions, and it's special to you. Maybe… Something like this?
**Aaron Abbott (Google LLC)** 18:27 Okay.
Yeah, I think this is maybe the disconnect, because I was thinking these were the same thing.
And, like, an example of a provider-specific part would be, like.
maybe a server-side tool call that's only specific to that provider, and would never be in Semantic Conventions.
**Liudmila Molkova** 18:48 Yeah, we're just down. It's not yet there.
**Aaron Abbott (Google LLC)** 18:53 Okay.
Yeah, I think… I think that's… yeah, I was… I was thinking the same thing. I guess I didn't understand what you meant by generic parts. I was… I was trying to allow the provider-specific parts, or the custom, so maybe… Maybe that's what we can clarify.
So, can you give an example of generic? Maybe just, like…
**Liudmila Molkova** 19:17 Oh, it's… in my mind, it's an abstract class. You cannot instantiate it. But you… we take it in the API as a list of parts.
So it's not… there is no example.
**Aaron Abbott (Google LLC)** 19:31 Oh, I see. So this one is just to allow to keep the enum open, basically.
**Liudmila Molkova** 19:35 Yeah, exactly.
**Aaron Abbott (Google LLC)** 19:36 Okay, okay. I think, yeah, I think we're saying the same thing then.
Cool, I'll, I'll, I'll take a look again with that context.
**Liudmila Molkova** 19:49 Yeah, thank you.
**Aaron Abbott (Google LLC)** 19:50 Yeah.
**Liudmila Molkova** 19:55 Cool. Dylan, spend for cash the bidding call. Can you… Share what it is.
**Dylan Russell** 20:06 Yes, so, like, DSPY… Just like one of these agent frameworks.
Will Cash… Embedding calls.
Like, if you make the same call to the same model, the same list of strings.
And, like, some other parameters.
it will… Cash it.
And the question is… yeah.
**Liudmila Molkova** 20:36 Like fetch response for inference.
**Dylan Russell** 20:45 Like, it's making, like, a… An embedding call.
**Liudmila Molkova** 20:50 Yeah, I mean, the same principle.
**Dylan Russell** 20:58 Do we have something for when there's, like, a cached fetch call?
**Liudmila Molkova** 21:04 So this is the client in France.
So we have inference and fetch response.
And.
It sounds it sounds analogous, but is it like common?
Do we care about instrumenting it at all?
**Dylan Russell** 21:42 Well, we're instrumenting, like, the embedding call.
And they just have a cache around that.
**Aaron Abbott (Google LLC)** 21:51 Billing, you mean, like, the Python code uses, like, the cache decorator kind of thing?
**Dylan Russell** 21:56 Right.
**Aaron Abbott (Google LLC)** 21:57 Okay.
**Liudmila Molkova** 22:00 Oh.
But then there is no operation, it's in memory, right?
**Dylan Russell** 22:04 Right.
alright, there's no, like, network call.
Like… Framework is… You make… the user, for some reason, made the same embedding call.
And the framework cached, and didn't do the network hop on the second one.
**Liudmila Molkova** 22:27 I'm thinking… It's not specific to embeddings at all. We need some central guidance for this. We don't have it.
Do you think it's like something required for some conscious facilitation? Should we bring it up tomorrow maybe?
**Dylan Russell** 22:49 Yeah, it seems kind of more general, yeah, like, it could happen.
But, I mean, it's worth probably bringing up tomorrow anyway, just to see if people have ideas.
**Aaron Abbott (Google LLC)** 23:02 Ludmila, do we do anything for HTTP?
Caching, like, I know, for example, Chrome DevTools, it will show Like, there's… there's no… request response, but it shows, for example, in, like, the Network tab, and it will show served from cache or some string like that.
So I think it's probably a valuable signal in general.
**Liudmila Molkova** 23:25 I agree it's valuable.
we don't do anything, we don't have a convention, or I don't think there is a precedent for this.
I even think it's not the GenAI topic, I think it's General Semantic Conventions topic.
Maybe for now, we can… I don't know, not instrumented, and it created a tracking issue, either in some ConfGen AI or in general, some Conf and postponed it.
**Dylan Russell** 24:11 Alright.
Sounds good.
**Liudmila Molkova** 24:13 Yeah, thank you.
Okay… Very nice.
The next one, we… I think we discussed it… And maybe to limit it to the… Environment variable only.
Did you have a chance to take a look, Don?
**Dylan Russell** 24:52 No, I'll… I'll take another look.
**Liudmila Molkova** 24:57 So.
Okay, I am.
Moving on with the renames and this friend.
Renames, operation duration for embeddings.
To the embeddings duration, and… I'm adding this… for… The histograms.
I… so we have two classes of usage metric, one is counters.
The other one is histograms per operation, and the tricky choice here Is, do we want, Special usage metrics for embeddings.
And I don't want to add them.
R.
It's essentially always prompt today.
There, and it's always text today.
Oh, wait, so sometimes there could be different images.
And video or audio, but they are priced by seconds, and sometimes images are priced by images, and sometimes they are priced by pixels. So, de facto, we only have text.
And we… Only have input tokens.
So… Since nobody is actively asking for.
Anything else? I'm kinda assuming people are fine with the current state of affairs, we can always add things later.
The only minor kind of concern I have is that for someone who wants to build a usage dashboard for embeddings, they would use histograms, and for Inference, they would use counters.
If anybody has strong opinion, I would be curious to learn.
But.
We can also discuss it tomorrow.
**Aaron Abbott (Google LLC)** 27:45 Just to be clear, Ludmila, the specialized metrics.
Did you mean the, the subcounters?
Okay.
I mean, yeah, like you said, I think we can always add it later.
**Liudmila Molkova** 28:04 Yeah, I think there is one thing for embeddings that Kinda makes sense to add.
To… Today?
is apparently There are different types of embeddings, of different input types, and it's kind of… They're slightly different, but also consistent across different providers that Like, when you embed the document, and when you get embeddings for the query.
It changes the characteristics of the operation, it means something for the model.
And then, essentially, it's useful to add this as an attribute on metrics, and because adding attributes on metrics is breaking.
We kinda need to decide, before stabilization if we do this.
I'll… I kind of think we should do it.
But also, if people know more and have thoughts, please post them on the issue.
**Aaron Abbott (Google LLC)** 29:15 Are those… are those input types always, like, one per request?
**Liudmila Molkova** 29:20 Yeah.
Oh, wait, no.
Good question.
**Aaron Abbott (Google LLC)** 29:34 Yeah, I think you see what I'm getting at. It's like similar to the modality issue.
**Liudmila Molkova** 29:39 Right.
Yeah, another tricky part about embeddings is they're usually batched.
And yeah, I'll check.
If not, then easy, we just don't edit.
Okay, we are at time.
Let's continue tomorrow?
**Aaron Abbott (Google LLC)** 30:13 Sounds good. See y'all tomorrow.
**Liudmila Molkova** 30:15 Yeah, see you, thank you.
