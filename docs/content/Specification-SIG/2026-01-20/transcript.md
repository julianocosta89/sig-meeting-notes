SIG: Specification SIG
Date: 2026-01-20
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Josh Suereth 00:01:08 Peyton.
Armin (Dynatrace) 00:02:26 Is it really 419 weeks of OTIL already?
It seems like… a lot.
Jack Berg 00:02:37 Where are you getting that? From the meeting notes?
Armin (Dynatrace) 00:02:40 Yeah, I just, like, backfilled the missing, meeting node instance counter.
It turns out to be 419. I wonder if… That's accurate.
Jack Berg 00:02:53 Wow.
I believe it.
52 a year?
Maybe, maybe 48 a year? Trask, I think you were muted.
Armin (Dynatrace) 00:03:04 maybe more frequently in the beginning, I don't… remember, actually. Might be.
Trask Stalnaker 00:03:14 What is the counter there for?
Armin (Dynatrace) 00:03:18 Toneful, Fred.
Trask Stalnaker 00:03:19 buddy? No, but I mean, like, is it useful?
Armin (Dynatrace) 00:03:22 I think it's just a… Tradition. I think that's all.
Trask Stalnaker 00:03:30 Good enough reason.
Thank you.
Armin (Dynatrace) 00:03:32 And it's fairly easy to maintain, that's why it hasn't undergone The scrutiny that we have for other things.
But it looks like we're fairly complete, and… I think we'll be starting with you, Trask, before we wrap up with you as well, Trask.
Get off, please.
Trask Stalnaker 00:03:54 Sure, yeah, I'll go ahead and share.
I, yes.
Let's see who we've got here… Jack… Cool, so there was one… Open question here, For… this is adding the, exception parameter to emit log record.
There was one question about precedence. If somebody sets an exception.
And also sets, explicitly sets, like, exception.message.
attribute.
Which should take precedence. And I think there's two… solid options.
One is, last right wins, so if you set exception.message first, and then you set the exception. Paul said exception… then that's gonna override it.
The other, is to say that the, user intent, if you're setting exception.message explicitly, is most likely to override that, The auto-generated exception.message from the exception, and to make that take precedence.
I think both… both are implementable. I sent a prototype to, currently the Java's implementation of this Follows the last right winds, but this prototype shows Basically, how it would look like with, conditionally setting Only setting attributes that weren't there already.
Jack Berg 00:06:11 So, Trask, in this case, the user setting, exception.message, the user's doing it in, like, a log record processor?
Or something to that effect, because, like, in the… in the actual API, it's not like Span, where, like, you know, Span's, you know, wraps some sort of unit of work, and, you know, instrumentation can… add attributes, and then transition over that span to user space, and then the user can add their own attributes to that span. Like, in the log signal, you know, recording a… remitting a log record is like an atomic thing.
you know, when you call the API, you just call emit, and so there's not really, like, an instrumentation user overlap there, so I think it would have to be, like, the conflict would have to arise from processors.
Trask Stalnaker 00:07:01 Well, I guess there's two… things. One, with, like, Java's implementation of a builder, Right? You do have that… ordering… You can call set… attribute.
First… And then you can call set exception second.
Jack Berg 00:07:22 Yeah, I… I think that's, like, a Java… Java-specific… A Java thing. Yeah.
Trask Stalnaker 00:07:28 Then, back to explicit spec language, where it's an atomic emit.
I think we… yeah, there… That's a good point. As an atomic, like, this just group of… bundle of parameters, there isn't really an inherent ordering, and so maybe that's even a stronger, reason to say in the spec that We should… there is no last-right winds there, and we should… Explicitly say that… User attribute has precedence.
Jack Berg 00:08:07 So basically, there is no problem.
Like, there is no ordering problem that you have to consider, because… You know, the API emits an atomic log record with all of its attributes set, and then the only chance for a user to intervene with that is in log record processors, where, of course, log record processors overwrite the data of the log record.
Trask Stalnaker 00:08:31 Right. I guess emit still needs to make a decision, though, if there's an exception.message attribute.
Oh, I see. And an exception object set.
Jack Berg 00:08:44 That's true.
Okay, I understand now.
Trask Stalnaker 00:08:49 Luna.
Liudmila Molkova 00:08:49 And a lot of these problems come from just users doing the wrong things, and yes, it's atomic, but also it's subtle attributes that you cached somewhere.
Or just, you can build log records in multiple places, and the only place where it actually would come up is the, just bugs in user code.
And, where… If we don't want said except exception to overwrite attributes, then we also don't want said except exception to overwrite previously set exception.
Right? So, like, you can call said exception multiple times. It's just all variations of invalid Code that somebody would write.
And I don't feel like it… like, we should have a predictable behavior.
But regardless of what we pick, It doesn't matter.
But if we decide that said exception does not overwrite previous call to said exception, then we should give it a different name.
Probably. Just from API design perspective.
Jack Berg 00:09:56 Yeah, because set kind of implies last.
Liudmila Molkova 00:09:59 Yeah.
Jack Berg 00:09:59 Right wins. Like, you're overriding the previous value.
So, that's a different question, though. So, like, there's… SetException, you're setting the exception object, and, you know, the name of the methods is setException. You know, I… like, I don't think that there's… people would argue that if you call set exception twice, that the second one wins. But the question is, like, should any exception set, how should that How should the attributes from that be prioritized against attributes that were explicitly set by the user?
Liudmila Molkova 00:10:39 I think both are… we should expect both to be explicitly set by users, and if somebody sets attributes on the unsat exception, it's a bug in the user code. We should handle it as gracefully as possible, but we should not think it's a valid Case, by any means.
Trask Stalnaker 00:10:57 Wait, what… I mean, the valid case that I am imagining is… So you don't think it's a valid case to want to override the exception.message to something different than what automatically Gets extracted during set exception.
Liudmila Molkova 00:11:20 In the processor.
Trask Stalnaker 00:11:23 Oh, no, in the… Forget processors, I don't really care about processors, because that's… I don't think that's… the… API here is just about emit, this spec, at least.
So, from a user API, a user… Wants to admit a log record, and they attach an exception to it, and they attach a set of attributes.
And one of those attributes is exception.message.
Liudmila Molkova 00:11:59 So they, like, okay, we don't know what said exception does, but let us make sure we set the attributes, as well.
And they… they would expect the attributes they said explicitly to be preserved, no matter what.
Trask Stalnaker 00:12:13 That's my thinking.
Jack Berg 00:12:21 I agree, it's kind of like a weird niche case, arguably a bug.
So, I like how Ludmila framed it. We want to be as graceful as possible as this, but maybe she didn't say this part, but I also don't want to overthink it too much, because it's such an odd niche case. So, if you want to… If you were to say that, like, you know, the recommendation here where attributes always take precedent over Exception? That sounds fine to me.
Because… Like, because I think it's a niche case that I don't want to encourage.
Liudmila Molkova 00:13:04 And then, if somebody sets exception to times different ones, we would take the last one.
the objects.
Jack Berg 00:13:12 I mean, technically, that's not a… that's not a.
Trask Stalnaker 00:13:15 Oh, yeah.
Jack Berg 00:13:15 happens, because… In the spec?
In the spec.
Trask Stalnaker 00:13:21 Where there's no builder.
Where it's an atomic, you can't set the exception twice.
Jack Berg 00:13:28 Right, so Java has a builder, so we actually have a set exception method, so, you know, that can actually happen in Java, but for every other language and how the spec is written, it's just, like, all the fields of a log record are recorded in one atomic unit, so there's no opportunity to set multiple times.
Trask Stalnaker 00:13:49 Alright, I feel good about that.
Let's move on… To a more complex discussion.
So in attribute… complex attributes, we're, starting… we're… stabilizing that in Java right now, and… Coming across a, question here, so… We have this line in the spec that says protocols that don't natively support value types, some of the value types, for example, complex attributes, complex values.
should JSON encode them.
So, I've got two… So there's two, kind of, I think semi-obvious options?
for how we should JSON encode them?
One is OTLP JSON.
Obviously.
The other is just… Simplified.
JSON encoding.
So, I know that, I mean, I am… I prefer this. I think the default for backends, for users querying their backends, this is probably gonna be more natural for them.
there's… I kind of wanted to query this group for, because I haven't been part of the OTLP JSON discussion, what are… possible downsides to this. The two that jumped out to me are, I mean, you lose… Versus double.
And you lose, string versus, bytes. Inverse and double, I guess, don't really care that much about. String versus bytes is a little weird, but I guess my thought is that users querying would kind of know what they're querying.
And I don't know how you query bytes anyway, Yeah, let's go to Hans. Tigran.
Tigran Najaryan 00:16:20 Yes, I actually, wanted to talk about the downsides. What you're suggesting there is to essentially use the… whatever is the native whatever is the native JSON representation, but you don't have the bytes, and And the 64-bit integers, obviously, there.
Are we… so there's two options here, right? One is we say this is a LUSI representation. We'll list some of this data. I don't know if that's a great approach, but it's a possible approach. The other would be that we define Sort of a variation of that, which is loose, which allows you to represent 64-bit instead of the bytes.
It would be… it would start looking a bit like the protobuf JSON encoding.
Without some of the weirdness that it has for the… for the key value maps.
if you eliminate that, I think it would be fairly… nicely looking representation, because the rest are… are not that bad, right? It's the… it's the key value lists which are weird in protobuf JSON format.
So I think we would need to, first of all, make the call. Is this going to be a losey or loseless representation? If it's loseless, then I would… then the choice would be between the the protograph Jason.
as is, and a simplified version of that, I'm guessing.
I don't, from the top of my head, I don't know how to make this code, but it seems to me that's the choice we're facing here.
Okay.
Ted Young 00:18:07 Yeah, I guess a question I have is just, how much does, like, you know, the policy of lease surprise, factor in here?
you know, in terms of… we're just talking about data that the end user is sending. By changing it into OTLP format, are we changing it far enough away from what they would kind of expect to see that that would be confusing or creating problems for people?
I don't know if it does or not, but that's… That's one thing to think about.
Trask Stalnaker 00:18:38 Daniel.
Daniel Dyla (Dynatrace) 00:18:39 Yeah, I… I agree with what, Ted just said there. Like, if I… if I'm querying some… some non-OTLP data storage, backend, I don't know why I would expect to see OTLP details in there.
This seems like it's imposing… protocol-specific restrictions on other protocols and other backends, where, like, if they don't have those, the distinction between, you know, say, int and double, for example, it's not… I guess I don't really see what the advantage is of… preserving OTLP in a lossless way to send it to a backend that we already know doesn't necessarily support these complex types. Otherwise, you know, if they did, you would use their native format for that.
Trask Stalnaker 00:19:39 That's a good point.
How about these are for non-OTLP backends?
Lydmilla.
Liudmila Molkova 00:19:49 So, two points. I think the JSON representation… It's a… it's… it was in the spec even before complex attributes.
We already used it, and even if we wanted to.
We wouldn't be able to change it.
But, to the technical side.
the bytes, so we, we use complex attributes in GenA, and we currently, say, put them in JSON if you, if you're… OpenTelemetry API doesn't support complex attributes. And we… explore the string versus bytes, most JSON serializers, this serializers, just… happily convert bytes to Base64 string and back.
So, it's essentially… not… It's not a lossy part, this one, it's just weird, but it's, it's like it's handled by the world defaults.
Trask Stalnaker 00:20:53 So… somehow, I guess I didn't understand, I didn't know that, when unmarshalling JSON data that deserializers will sort of auto-detect a string as being a base64 encoded string and convert it to bytes.
Liudmila Molkova 00:21:15 If they know the model, they know its bytes.
Trask Stalnaker 00:21:19 Oh, if they know the model, but in this case, they wouldn't know the model.
Liudmila Molkova 00:21:24 They wouldn't know the model, and for somebody who doesn't know the model, Base64 string looks, like, much better than the array of bytes.
So I'm… I'm on the side that it should be just plain JSON, it's shorter, it's… it's obvious, and it is lossy, slightly.
Trask Stalnaker 00:21:49 Jack.
Jack Berg 00:21:50 So, let's say I'm sending complex attributes to a native OTLP backend, and then I'm querying out for that data.
I would not expect to see the data represented in the OTLP JSON format.
I would expect the backend to accept the more verbose OTLP JSON format, convert it to its internal representation, and then show me a condensed representation back.
And, so I think that's related to something that people were saying about, like, hey, when I send data to a backend, and then I query it back, I would be surprised to see OTLP JSON. And the point is, even with native OTLP backends, like, you know, you don't expect to see OTLP JSON.
And, you know, this question about, what do we do here? Is it simplified JSON or OTLP JSON? It's actually a really narrow scope that this applies to right now, because we got rid of the Jaeger exporter.
the Zipkin exporter is deprecated, and this advice is for, like, what to do if you are an exporter, and you encounter, you know, an attribute type, these complex types, which you didn't previously have support for. And Zipkin and Jaeger are deprecated.
And so, if you're a custom exporter that's not one in the spec, of course you can do what Daniel Dilla has said in the chat, which is, like, you know, do what's best for your backend. You can add explicit support for the any value type and serialize however you want. This is, like, the fallback.
Of what to do. So, I guess, like, my inclination for the fallback would be to be lossless, to be as precise as possible, because I don't think it matters that much. I don't think this actually applies to many exporters, and an exporter that it does matter to can always do something better.
Trask Stalnaker 00:23:43 Let's take, I mean, the one exporter is Prometheus. I mean, if we want to take a concrete example, how would we apply this to the Prometheus exporter?
Jack Berg 00:24:01 So… The… so the Prometheus exporter, yeah, it would be… that's… I guess that's the third one that I didn't consider. It would… it would have to use whatever we do here, or the Prometheus exporter, as part of its compatibility document, could describe an alternative conversion.
Trask Stalnaker 00:24:19 Yeah.
Jack Berg 00:24:19 It's nice for it to lean on, like, whatever the common advice is, though. I'll acknowledge that.
Trask Stalnaker 00:24:26 Okay, yeah, and I… I think it's beneficial, given that we have Prometheus, so I think it's beneficial to put something in the spec.
because of that. And then, I think that… that becomes, hopefully, a tooling, like, if we're, something that other backends can leverage easily, other exporters could leverage easily if they are not supporting OTLP.
Even maybe, like, a logging… maybe a logging exporter, I don't know if that how that applies to Logging Exporter.
I guess it's logging… OTLP JSON is our official logging exporter.
Jack Berg 00:25:17 We have multiple. We have the console logging exporter as well, which is like a no-specified format, and for the console logging exporters that are not OTLP JSON, I'm with you. It seems surprising that you'd get this super verbose, messy serialization.
Not something that's simplified. Maybe there's, like, maybe it's, like, both. Maybe it's, like, the SDK should offer mechanisms to do either a lossless, full serialization, or simplified JSON. Choose what's right for you.
Trask Stalnaker 00:25:54 Ted.
Ted Young 00:25:56 One thing to maybe note is this, because, Jack, you mentioned, like, well, the backend could get one version of JSON and just transcribe it into something else, but it seems like these exporters are only for backends that are, like, totally OTEL unaware.
Right? It seems like if the people are working on the backend to, like, make it more compatible with OpenTelemetry, they should just accept OTLP and… and do the right thing with it, and not put JSON converters into the exporter.
So is… I guess it's like a question. Is this advice really just for backends, where, like, we can't touch the backend, right? Like, this is just going to some data source, and we have to deal with how it currently works, and so how do we convert to JSON, because it just doesn't know any better? And if that's the case, I think regular JSON would be the right… approach.
If we're limiting our advice to just that scenario.
It's like a funny middle ground.
Jack Berg 00:26:55 And to add to that argument, just to take, you know, that side for a second, is like, you know, we could say that the guidance is to do this simplified JSON, Acknowledge the downsides of it.
And say, hey, if you need a lossless transport, then you should think about better integration with OTLP.
Ted Young 00:27:16 Yeah.
Another way of putting it is, like.
Prometheus, this… this stuff shouldn't be applying to Prometheus, because we have a lot of Prometheus people, like David, working on this, and we're, like, in communication with that. So if, like, there… it's totally fine to be like, when converting to Prometheus, we write into the spec, like, this is just how we do it. It doesn't have to be… we shouldn't be using Prometheus as… Our… our signposts for what to do here, because we're connected with that community.
Maybe.
I might be wrong about that.
Trask Stalnaker 00:27:50 I'm kind of curious, the… I am kind of curious what we would do in Prometheus, because that kind of… like, what would Prometheus want… Because that kind of… it's just a… it's… it's just a point of… like, comparison.
could help.
David Ashpole (dashpole) 00:28:11 I think we've just told everyone, please, please, please, Don't use, like, maps.
as your, attribute values. Please don't do it. And so we haven't worried too much about The representation, because… If you need it, you need it, and I guess that's that.
As far as, like, which representation?
I could easily imagine the simplified one being slightly… preferential for, like, looking at it in the UI, so that it's, like.
A little bit of scrolling instead of a lot of scrolling somewhere.
But neither one is going to be, like, A particularly good experience, and… Probably you'll have cardinality issues or other things.
If you do try and send, like, maps with things, unless you're very, very careful.
Trask Stalnaker 00:29:08 I was thinking, like, resource attributes in particular…
David Ashpole (dashpole) 00:29:12 Yes.
Trask Stalnaker 00:29:13 if somebody… Which wouldn't have the cardinality problem.
David Ashpole (dashpole) 00:29:19 Right? Like, the command line args, I think, is the one that comes up most often.
I could definitely see that being, like, more readable if it was… If it didn't have all the, like, string… prefixes.
Trask Stalnaker 00:29:39 Thanks. Tigran.
Oh, by the way, I'm going to retroactively… Yeah, go ahead.
Tigran Najaryan 00:29:49 What are you doing retroactively?
Trask Stalnaker 00:29:50 Oh, retroactively, in bumping my time.
Tigran Najaryan 00:29:54 All right, all right, that's good. So, I was just looking at the collector codebase. We have a bunch of exporters there as well, right?
And yes, strictly speaking, this… this is about spec, this is about SDK exporters, what we have in the spec. But, we have, the same logic, I was just checking the collector in the collector core codebase.
When we want to convert the, any value to a string.
it has exactly this fallback. If it… if it's a pipe that is… Anyway, one of the types that you… that the spec recommends to use the JSON encoding for, that's exactly what it does there, and that is used by some of the exporters. The simplified.
Trask Stalnaker 00:30:41 one here.
Tigran Najaryan 00:30:42 No. I mean.
Trask Stalnaker 00:30:44 the OTLT.
Tigran Najaryan 00:30:45 pulls the JSON… the regular JSON encoding, and tries to, yes, map the… I can maybe look up the exact codebase, but what I'm saying here is that We'll have to make a call in the collector as well.
And I think it needs to match whatever the SDK exporter is doing. So, it's not just about the Jaeger and Zipkin, which we no longer use, or the Prometheus, where we can prescribe something differently. It's likely going to be… applicable to some of the collector-exporters, so I would take a look at the codebase, I just did a couple minutes of exploration. Somebody needs to go and take a closer look at what is happening there, because this decision likely is going to impact the collector-exporters as well.
Trask Stalnaker 00:31:38 Makes sense. Thanks.
Daniel?
Daniel Dyla (Dynatrace) 00:31:43 Okay, I'm back. I guess I was just gonna say, I… thinking about the use cases that we have for this. We have Prometheus, which, as was already mentioned, doesn't really want this at all. We have… OTLP backends that have not been extended with complex attributes yet as potentially a compatibility, layer.
And we have… other exporters that we don't necessarily control that are encountering complex attributes and don't know what to do with them, and we need to provide guidance for those people. And in all of those cases.
I can't think of any possible scenario where this super complex representation is a better user experience for the user when they're querying their data in their backend, because By definition, with this problem, we already know the backend doesn't… like, natively support this data format. If they did, they would be encoding it properly. So, do we want our users to be putting into their queries, like, all of this, like, KV list like, protocol-specific garbage, I think the answer's no. I don't… I can't think of a single scenario in which I would rather have that.
Losing… the difference between, like, an integer and a float, I kinda get that, but, like, that just seems like a way more minor problem to me.
When we already… like, we know that one… Version of this is bad in almost every case.
The other version is possibly bad in some small subset of cases. To me, it seems very clear that we go with the simplified version.
And recommend, if you need complex attributes, you should have proper support for it.
I can't think of a single scenario in which case this super complex representation I would be happy seeing that in a query. I think I'd be very upset if it ever was returned.
In any query result, ever.
Trask Stalnaker 00:34:11 Seems like that's where we're going here. Thanks.
Dead.
Ted Young 00:34:17 Yeah, I can think of exactly one scenario, which is a backend that knows they're gonna support this stuff, and wants the lossless format, so that when people upgrade the backend, they don't have to go around upgrading all of their collectors and everything.
But that's, like, an edge case. I would… I think the only suggestion I would have is, like, to make sure there's just a lot of shoulds around this in the spec, just to clarify, like, you should follow this if you don't have a better plan, but if you have a plan that works better for your backend, don't feel locked.
Don't feel shackled by this advice.
Like, do what makes the most sense for your own product development plan.
Daniel Dyla (Dynatrace) 00:35:00 I think even that edge case doesn't work, though, because you do have to go around and update your collectors to stop exporting this stringified version and start exporting, like, proper, complex values.
And then, are you gonna, like, reprocess all of your historical data to then convert it? Very unlikely, like… exceedingly unlikely. Like, it's an edge case that I think… has edge cases built into it. It's a contrived example.
Ted Young 00:35:31 Edge cases all the way down. For sure. I think my point was more like.
probably we should just make sure to write in the spec that this is a fallback that we're describing. If you know what's gonna work best, just do that.
Like, we aren't saying don't do the thing you prefer, we're just saying, if you don't know what to do.
Daniel Dyla (Dynatrace) 00:35:53 do this normal thing of converting it to regular JSON.
I think the only thing we have to specify is what does Prometheus do, because we want our SDKs to be consistent there, and… do we want to have a fallback behavior for exporters in case you know you're exporting to an OTLP backend that doesn't yet have complex attributes? So we have to define it for that as well. In both cases, I think simplified is better.
Everything else, like, if somebody says, I'm writing an exporter for my own backend, they should know what their own restrictions are, and if they don't, and they're relying on our guidance for that, then… Oh, maybe they shouldn't be writing an exporter. You know… it seems, like, too back-end specific to me. So I think we make the decisions that make sense for the two targets that we care about, and move on.
Trask Stalnaker 00:36:50 I'm gonna give the last word to Jack here.
Jack Berg 00:36:54 Just on the point, Daniel, you made about, OTLP exporters to backends that don't yet support complex types.
I thought we talked about that in the OTEP, and that the conclusion was that Like, yeah, we could… we could have exporters where this is an option, and you can now configure your OTLP exporter to, you know, stringify the complex attributes, or to send them as is, and we waited this 6-month period before adding them.
specifically to allow those backends to adapt, and because all they really need to do is what we're talking about here. When they see complex attributes, stringify it on the backend before storing. And, yeah, I guess, you know, I see Trask nodding, but I thought that we accounted for that with the 6-month wait period.
Trask Stalnaker 00:37:45 Yeah, I don't think we have to do that, it's…
Daniel Dyla (Dynatrace) 00:37:49 We go down from two targets that we care about to one target that we care about, and it… still, the answer's the same.
Jack Berg 00:37:56 Yep.
Tigran Najaryan 00:38:00 By the way, I think the way that the spec is defined right now.
There's no way to… we're not… We're not requiring that the strings, for example, are encoded as JSON.
Right? There's a specific representation for strings in JSON, but that's not what we do, right?
Strings are written as is.
So if you're string… looked like a JSON, you've got a problem. There's no way for you to know whether that's a JSON, And you should be decoding it as a JSON, or that's the literal stream that you should be using.
it's already losing. There's no way for you to… Directly know how to, exactly to decode the data.
Because we don't specify the type to be JSON.
It goes as a string, right?
And so you have no way of knowing whether that's literal string, or if it's a JSON encoded value.
If we accept that, then… it is what it is, right? It's going to be losing anyway, it's going to be worse with additional data types.
And we may as well just accept the fact and say that this is what it is, it's just for human readability, and if you want precise representation, just use OTLP, and that's it.
Trask Stalnaker 00:39:22 Awesome. Thank you all. I think, I will… I will send a PR, and we can discuss any more edge cases upon edge cases.
There, as needed, but sounds like we have a simple, path forward. Simple-ish, as far as spec things go.
who is leading this meeting? I already forgot.
Armin (Dynatrace) 00:39:49 I started it off, but you had the first items on it. Carlos is next, right?
Carlos Alberto Cortez 00:39:55 Yeah, correct.
Okay, by the way, Armin, could you share for me, please?
Armin (Dynatrace) 00:40:04 Yeah, sure.
Just to share.
Carlos Alberto Cortez 00:40:06 Yeah, some issues, etc. Thank you.
This is about hotel resource attributes that I discussed last week, briefly.
Basically, I came with a small table showing, like, roughly, very roughly, and maintainers, feel free to correct me, but this is how I was checking things work regarding the handling of that part.
As I was mentioning before, currently in the spec, it says that we are following the electricity baggage format. That includes that.
the allowed number of… the allowed, set of charts is, limited to Bagash-Octer, which is a subset of ANSI.
And this is how it looks currently. They fail fast, the first column there that you see is basically whether, there are different ways, like, how to handle, like, whether you get an invalid chart, or invalid input, or whatever. So, you can see that Java and JavaScript are the ones that currently, they fail fast.
the others try to recover in different ways, you know? The second column is about whether… as part of the spec, it's like, any char that is outside this Bagashoktet?
should be person-encoded. So most of them, they try to do that, you know, they try to use, some, library.
to, to basically to, to parse this. There's C++ and ROS, they don't do that, you know? So they should be doing that, probably, because that's the expected… that's an expected input. The other thing is that, in theory, you should be, And this is part that is not very clear in the spec, but basically, it's like, you should be checking for unencoded charts, you know? Chards that are outside this package octet, they should… they must, according to the spec, they must come person encoded.
And I think that most of the SIGs, they don't do any kind of check. I don't know whether actually this is super required or not, but this is what it is in the spec. And finally, whether it comes to trimming white space.
both at the end… this is not in the middle, just at the end. At the beginning, most of them do this kind of stuff, with the exception of C++, which is, like, more, like, raw string.
So, given these different kind of behaviors, I would like to get what's… what do people think about changing this?
Yeah, I think that we have kind of different behaviors. I don't know whether we should update the spec appealing to what mostics have currently, or what we would like to see. I am also a little bit concerned about things that users may be doing already, and we're just… and, you know, in the sake of correctness, we break them, you know?
Trust.
You're muted.
Trask Stalnaker 00:43:07 I don't know, understand this headset. if I recall, this came from… this question originally came from the JSG.
And I think the… Main reason why it was raised was because of spaces in the middle of values.
Which is basically, I think, this column?
Carlos? Is that correct?
Carlos Alberto Cortez 00:43:43 No, actually, spaces in the middle, that's not considered… well, I could say the closest is that, there… well, basically what they tried to do, it's something funny, but yeah, I would say it's not any of these four columns, long story.
Short.
Trask Stalnaker 00:44:01 Because a space… a space would be an unencoded character.
Right?
Carlos Alberto Cortez 00:44:08 It's…
Trask Stalnaker 00:44:08 Technic…
Daniel Dyla (Dynatrace) 00:44:10 Space is allowed in the baggage, it's an allowed character.
Carlos Alberto Cortez 00:44:23 I think it should come… it's valid, but it should come in person encoded. Let me double-check. Yeah.
Trask Stalnaker 00:44:29 Yeah, that's… Daniel, that was my understanding, was it's not an allowed character, it has, like, technically… It should be percent encoded.
Daniel Dyla (Dynatrace) 00:44:40 I'm looking right now.
baggage octa, US ASCII characters excluding controls, whitespace, yeah, so it excludes whitespace, you're right. So yeah, that's just an unencoded character.
Carlos Alberto Cortez 00:44:58 Yeah, correct.
Trask Stalnaker 00:45:00 And so I think the problem… the reason why it was raised by the JS books was because, spaces in the value was… Not, getting… was… was being checked?
to be, I mean, valid, and then it was failing fast.
And so, I guess my question is, the original problem that raised this whole discussion Would that be solved by just changing this to no and following all these… all the other… languages.
Jack Berg 00:45:46 What… so, don't fail fast, so that… that is… means you have to be prescriptive about what to do when you come across unencoded characters.
Daniel Dyla (Dynatrace) 00:45:55 Yeah, it's no different than coming across, like, an emoji, like a smiley face or something like that. You know, I don't… I think what we would say is, if you don't have unencoded characters, that's not… I would argue JS is the only one following the specification properly here.
Trask Stalnaker 00:46:14 I agree. The problem is that that's leading to… to user, complaints.
Jack Berg 00:46:25 Wait.
I wa… I don't understand this, like, why… Why is checking for unencoded characters the behavior that is desired according to the spec right now?
Carlos Alberto Cortez 00:46:40 So that's because, in theory… yeah, go ahead, Danil.
Daniel Dyla (Dynatrace) 00:46:44 Yeah, any characters outside of what's allowed are supposed to be percent encoded. I think the core of the issue here is that we took a format that was… conceived for… Different restrictions. Like, it's meant to be used in an HTTP header, which has different… restrictions than environment variables do, so now… and typically are not generated by end users. They're, you know, they're expected to be generated by… you know, a system that is aware of the restrictions, and then we're just reusing it for environment variables, which end users are just copy-pasting garbage into, and they expect that garbage to work. Which is not necessarily an unreasonable expectation, because that's the way everything else works.
But when we said, let's use the baggage format for this, we're using a format that was conceived for a completely different purpose.
Jack Berg 00:47:46 Okay, I might be under… misunderstanding the check for unencoded characters column. What does JavaScript do when it encounters an unencoded character?
Trask Stalnaker 00:47:57 Fails fast.
Jack Berg 00:47:57 Right.
Tigran Najaryan 00:47:58 Okay, surely fail fast, right? That's what a check means.
Jack Berg 00:48:03 Okay, so all these other languages are encountering unencoded characters and proceeding, giving the thumbs up, and it's only JavaScript that, when it encounters an unencoded character, fails fast.
Okay.
I would have hoped that that was the behavior of the Java implementation, by the way, what JavaScript is doing.
Tigran Najaryan 00:48:27 By the way, that's a good situation to be in. You can change the behavior to allow unencoded characters, and that's okay, nobody supposedly is able to use them today, because it's a fail-fast.
And if you allow them.
Sure, they can start using them, but nothing… nothing is going to break as a result of allowing that.
So I would be in favor of saying, let's allow unencoded characters, the one that Can be properly written down, let's say, in a terminal.
I don't know if you do… if you allow backspaces and stuff like that, it's still going to be a restricted character set, but… Restricted in a different way than the baggage octet says.
And then I would be generally in favor of, doing the fail-fast approach for every… everything here.
I don't know why the languages chose not to, because this is an… There's an input that you evaluate at startup.
And it's a config, so failing fast, it just gives you quick feedback that something is wrong with your configuration.
Carlos Alberto Cortez 00:49:33 I think that this is because some sticks, they consider that probably you have… may have a long list of attributes, and some of them may be invalid, but you want to be as nice to the user as possible, so you try to recover some of them, like, even if one is badly, but anyway, that's just the reasoning, it seems.
Jack Berg 00:49:50 It's, it's misplaced kindness. You're not actually being nice to the user. Yes.
Tigran Najaryan 00:49:54 Yes, agreed.
Carlos Alberto Cortez 00:49:57 Anyway, I guess the question is what… oh, yeah, go ahead, Trask.
Trask Stalnaker 00:50:01 In retrospect to Daniel's point that, I mean, if we… the only thing that these are failing fast for is invalid percent encodings.
or, say, Java, for example, that's the only thing to fail fast on. And ideally, like, I'm not sure percent encodings have any place in environment variable values.
And that's just because we reused the baggage spec.
Ideally, like, I think environment variables would… should just take the value as is.
But that's… well, I guess in this case, because it's a map, that's maybe the argument there, is you want to be able to encode.
Jack Berg 00:50:47 Comma's an equal sentence.
Trask Stalnaker 00:50:49 Yeah, yeah.
Daniel Dyla (Dynatrace) 00:50:51 You need to be able to encode characters that are meaningful to the format itself.
Which space is not one, for the record? Well, depending on how you define meaningful, I guess. There's optional white space that… Is defined in the format.
Jack Berg 00:51:17 A more precise spec definition would have been that, like, equal signs and commas, the characters that are meaningful to the encoding need to be percent encoded, but we missed the boat on that.
Carlos Alberto Cortez 00:51:28 Yeah, actually, that's kind of the problem now, because currently we have a spec that has, like, the last line of that section says, all attribute values must be considered strings, and characters outside the baggage of that range must be person encoded. So, for me, it's like, how do we change the spec in a nice way that, you know.
Tries to, improve the situation without breaking people, you know?
Trask Stalnaker 00:51:52 To Tigrin's point, though, we can't… we can relax conditions, we just can't make conditions more restrictive.
Carlos Alberto Cortez 00:52:02 Yeah, I would approve that.
Jack Berg 00:52:12 Specifically, we could say that, characters outside baggage octet should be percent encoded.
And define what is the behavior when they are not percent encoded.
Carlos Alberto Cortez 00:52:27 So that could mean that currently you would have to go from a mosque in the spec, to a shoot. Is that okay?
Jack Berg 00:52:33 That's okay, you can relax.
Tigran Najaryan 00:52:37 I see a problem with the CPP and Rust implementations, so… because they don't decode percent encoded.
And I think it's a must, because otherwise there's no way to represent unrepresentable characters, right?
Carlos Alberto Cortez 00:52:50 Yep. But if you make that change.
Tigran Najaryan 00:52:52 It's possible that you break something, because it was… it was… they were literally using a percent character somewhere there, and now you're starting to interpret it differently.
Which is a problem for these two languages.
Jack Berg 00:53:07 Yeah, and that's… that's a problem for any language that sort of, I think, misses the mark on interpreting the spec, especially around these… these strict areas of the spec where there's musts.
And, you know, they're gonna have to have the conversation of, do we call this a bug and fix it?
Pellared 00:53:25 Also, one thing, if I remember correctly, present is a special sign which has special things for… on Windows, for environmentalists.
Which makes it even harder.
Tigran Najaryan 00:53:41 Or you're saying it's even worse on Windows, because there's no way for you to specify on the command line?
Pellared 00:53:47 I'm not sure… Yeah, yeah, basically, I think if you set something inside percent, it's basically, like, a variable expansion, so it's like…
Tigran Najaryan 00:53:58 Dollar sign on, on, on Unix. Yep. I see.
Pellared 00:54:01 Exactly.
Daniel Dyla (Dynatrace) 00:54:02 It's escapable, but it's not convenient.
Tigran Najaryan 00:54:07 Yeah.
So that's a pretty bad choice for an escape character for what we need to do here, I guess, but it's… Perhaps too late now.
Daniel Dyla (Dynatrace) 00:54:19 I mean, I think you can always think of, for any escape character that you use.
If it's a commonly used escape character, you'll be able to think of a situation in which it doesn't make sense.
Or in which it's already used, and now you have to escape… escape characters.
not to pile on, I guess.
possibly meaningless history at this point, but actually, even in the W3C baggage format, This format was aped from… another previous format, which had different restrictions even than headers did. It was taken from the, the set cookie, header format, originally.
So that we're just, like… we inherited so much more history, I think, than we ever meant to.
By trying to… I think, purely out of convenience, say, oh, this already exists, it's already implemented in OTEL, let's just reuse this code.
I think nobody necessarily was thinking about how much history was being inherited there.
Carlos Alberto Cortez 00:55:51 I guess that, we only have 5 minutes, and, probably… so I guess, the path forward that Tigran described in the comments, I think that's a good, approach.
Basically, trying to relax the conditions.
And then, we will have to bring that discussion to the C++ and Rust communities, see what they say, you know?
Daniel Dyla (Dynatrace) 00:56:12 Yeah, I'm fine with that. I think it's easier for JS to relax the restriction than it is for others to add new ones, because we don't want users to update their SDKs and then have applications that were working suddenly start to fail.
Yeah, I guess for… for Rust and… C++, I'm not sure.
how they… Fix it, but…
Jack Berg 00:56:41 I don't love the precedent, though, like, of, you know, a bunch of languages didn't do the thing that the spec specified, and it's JavaScript that is… has to meet in the middle, just because the masses all did the wrong thing collectively.
I owe…
Daniel Dyla (Dynatrace) 00:56:58 I also don't love that. I was almost going to say that, but then… the reality is that it is a lot easier for us to change. And it's not just because we're the only one, it is because that is the easier direction to make the change.
Jack Berg 00:57:14 Yeah, yeah, I'm with you. I said it for you, on your behalf.
Daniel Dyla (Dynatrace) 00:57:18 Yeah.
Thanks, I appreciate it. I also had maybe an unfair advantage in that I wrote the baggage specification, too.
Jack Berg 00:57:28 You're very…
Trask Stalnaker 00:57:29 More important… more important to me, though, is the practicality argument of, what is best for users.
Right, like, if it was best for users that we… like, it is best for users that we loosen the restriction anyways.
So I don't feel bad about…
Carlos Alberto Cortez 00:57:55 Yeah, I'm…
Trask Stalnaker 00:57:56 using JavaScript.
Daniel Dyla (Dynatrace) 00:57:59 Yeah, I think Jack wasn't saying that it… that we chose the worst for users option, it's that we followed the spec. Yeah, because…
Jack Berg 00:58:07 Think about the incentive structure that provides. Like, a language implementation could just, like.
disagree with the spec and go off in a different direction, and then, like, if enough other implementations follow suit, then all of a sudden, the spec is in a crisis and has to figure out how to get itself out of the crisis. And it might not always resolve so elegantly as it's going to this time, where JavaScript can just, like, relax its restrictions and be aligned with everybody, and it's also best for users.
Trask Stalnaker 00:58:42 I hope that is a theoretical concern.
Daniel Dyla (Dynatrace) 00:58:45 Well, it's obviously not, we're running into it right now.
Carlos Alberto Cortez 00:58:48 But I hope that it is, like, an isolated case. I don't… I really hope we don't run into this in the future in other parts of the spec. I really hope that.
Trask Stalnaker 00:58:58 I mean, we've definitely had… it's non-theoretical in that languages have done things not aligned with the spec, and the solution has always been to align those languages with the spec. It has not been to Change the spec to align with the languages.
This… in this case, the only reason we're making a different choice is because of benefit… explicit benefit to users.
Daniel Dyla (Dynatrace) 00:59:27 Yep, which is why I agree, it is the correct choice. It is unfortunate that… the specification chose incorrectly, or however you want to… Yeah.
Trask Stalnaker 00:59:38 Yeah.
Daniel Dyla (Dynatrace) 00:59:39 But, yeah, I see Jack's argument, too.
of… You.
Once something's in the specification, it should be treated as specification, and if you need to change the spec, then, you know, we're making a specification you know, I guess in this case, we're not making a specification breaking change because we're relaxing a restriction.
But… Yone.
Jack Berg 01:00:05 I think intent matters a lot here, like, if we find that we have language implementations that are intentionally ignoring the spec, then that's a problem. I think in this case, it was almost certainly just, like, oversight, and that's a different type of situation.
Daniel Dyla (Dynatrace) 01:00:19 I agree.
Given that I think we're through that topic, I want to point out a related thing, which is that the fail-fast column of that chart is very inconsistent language to language.
Carlos Alberto Cortez 01:00:33 Yep.
Daniel Dyla (Dynatrace) 01:00:34 And I think we possibly need to come up with some, more, unified… guidance on whether SDKs should be failing fast on invalid specific… or invalid configuration or not.
Because that seems like another underspecified area.
Trask Stalnaker 01:00:59 declared it.
Carlos Alberto Cortez 01:01:00 Thank you.
Trask Stalnaker 01:01:01 to the win.
Daniel Dyla (Dynatrace) 01:01:02 Yeah, I agree.
Carlos Alberto Cortez 01:01:05 Okay.
Trask Stalnaker 01:01:06 out.
Carlos Alberto Cortez 01:01:06 And we go up on Twitter. See you.
Armin (Dynatrace) 01:01:09 But…
Daniel Dyla (Dynatrace) 01:01:10 Bye.
