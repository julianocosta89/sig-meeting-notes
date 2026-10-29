SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-10-28
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:29 Hi, folks!
Sorry, I didn't see you notice. Use, I did notice you came.
Let's give people a few more minutes to join.
Great.
Let's see what we can do today.
And we are… Adventist stabilization… Happy Halloween, people! Oh, we'll see each other on Friday, hopefully.
The… I think Max is not here.
I reviewed the PR, I left some comments, it looks good with some… Cosmetic changes… Nothing, like, important to call out.
But maybe there's… there's some discussion?
We'll see.
And I was going through… Hey, Trask.
I was going through the PRs that we have, and, like, categories we defined in the tracking tab.
and matching the PRs to… What we listed there.
So, I think there is an… Interesting one.
Oh, so, there is this one… That, I think… Aaron should take a look at?
But… This… I think we have a… The problem was… The tool call result?
object, it's not a part, but it's the JSON schema.
that… We are saying it's an object.
But actually, it can be an array, and it can be anything.
And I don't remember how… we talked about it with Aaron, and I don't remember where we landed.
on this.
I think this is what, as this proposes, is that… We would have always an object.
And if it's the… an object, it would have the type value, and we could add type array.
And then, at least for the… somebody who tries to deseralyze.
this. They always can't deserialize it into an object and don't need to.
Like, have it sometimes an array and sometimes an object.
Yeah, it just needs reviews.
**Trask Stalnaker (Microsoft Corporation)** 06:07 You're saying the, the content then would be an array?
**Liudmila Molkova** 06:15 So, if type is value, then I think… I didn't read through this PR, but you should expect some property. I would imagine it would be a value.
Though.
Or the type can be an array, and it would have something else to describe the array.
**Trask Stalnaker (Microsoft Corporation)** 06:40 Okay, but the problem the PR is trying to solve is that it might be an object or an array, and so far, we've assumed it's an object.
**Liudmila Molkova** 06:51 Yes.
**Trask Stalnaker (Microsoft Corporation)** 06:52 Okay, thanks.
**Liudmila Molkova** 06:55 The other option is to just say it can be either of them, and it's just a little harder for the consumers to work with it.
But okay.
This one, I thought that maybe we should take it over, and it's related to another thing. Oh, sorry, the… Erin is not here, so maybe we postpone this.
He brought up that the… the… Maybe we should make everything optional, and nothing is required?
And then the… Blah part content optional. Makes sense.
I still don't agree with the stripped reason proposal, but we can always set it later.
**Trask Stalnaker (Microsoft Corporation)** 07:47 The idea being that at least you can see there was… A blob… there.
**Liudmila Molkova** 07:57 Yeah.
And this… Or maybe.
the thing Dylan brought up, that if we upload individual parts, or the individual contents somewhere, that instead of the content, we would have content ref here.
**Trask Stalnaker (Microsoft Corporation)** 08:21 Oh, I see, so we would need it to be optional anyways.
**Liudmila Molkova** 08:24 Right.
**Trask Stalnaker (Microsoft Corporation)** 08:24 Sure.
**Liudmila Molkova** 08:25 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 08:30 And that would only apply to the blob part.
**Liudmila Molkova** 08:35 At least that one.
Right? Because, like, maybe we should have a different approach for other parts, but this one, it makes sense.
**Trask Stalnaker (Microsoft Corporation)** 08:44 Makes sense. Yeah. Makes sense to me.
Thanks.
**Liudmila Molkova** 08:49 Yeah, I'll leave another review on this PR and see maybe other will be relink to just market optional as a separate PR, or swap this one down.
So, this is another PR that we have.
And I… I didn't have a chance to look through.
But I'm thinking… Duh… what we have today in Blob Part, let's see.
This… the format is binary.
And it works fine, because JSON schema, in our case, it's not actually the… How we expect it to be serialized.
But… How we want complex attribute type to look.
And then, how it's serialized on the wire is the OTLP concern and the spec concern.
or the exporter concern, not the GenAI Semantic Conventions.
Right.
**Trask Stalnaker (Microsoft Corporation)** 10:02 Meaning, we… we can still… put binary… because we're representing it as any value. We're not actually sticking JSON, we're using the OpenTelemetry, any value.
Well, in the future.
**Liudmila Molkova** 10:17 Yeah, so this brings us to another interesting question. It's probably the instrumentation problem, again, not necessarily semantic conventions. I think we still have the language.
in… Our attributes, saying that you should serialize.
**Trask Stalnaker (Microsoft Corporation)** 10:37 Hmm.
**Liudmila Molkova** 10:39 Let's see… Hmm.
Or maybe not.
**Trask Stalnaker (Microsoft Corporation)** 11:24 What's the type? Do we actually… That's… Demotype is… any…
**Liudmila Molkova** 11:34 It is angry.
**Trask Stalnaker (Microsoft Corporation)** 11:35 Okay.
**Liudmila Molkova** 11:39 Maybe. Oh, we probably have it in spans.
No?
Okay, so… How come we removed it?
Okay, then maybe we should have it in the schema?
Awesome. Anyway, I'll take another look, and if there is anything that we need to change, I'll propose it.
I'm thinking of the instrumentations.
We could use… any value today in Python, and we should start Using it prob- probably.
**Trask Stalnaker (Microsoft Corporation)** 12:58 Certainly solves the binary problem nicely.
**Liudmila Molkova** 13:02 Yeah.
Okay, let me… Quest changes, let's see…
**Trask Stalnaker (Microsoft Corporation)** 13:33 Yeah, I think it is in that GenAI spans, When recorded, like, output messages, when recorded on spans, it may be recorded as a JSON string if structured format is not supported.
**Liudmila Molkova** 13:49 Okay. Mind, creating an issue to remove it? Sure. Yeah, thanks.
Okay.
And this is another… PR that I didn't have a chance to look at.
But it seems to be something that… Related to the stabilization effort.
Let's see what it solves.
Oh, I think we… Oh, I see, maybe our modeling is not great, and I'll probably need to spend more time understanding the problem.
Because it sounds like we require, or at least we… our examples show that the role is 2.
But turns out there could be mixed messages, and maybe… event.
We should either… Have multiple messages.
Or… Half.
Two calls under assistant role.
Okay, and it came from… by the KI, yeah.
Okay, I'll take an action item to dive into this more, and probably present next time.
**Trask Stalnaker (Microsoft Corporation)** 17:04 Cool.
**Liudmila Molkova** 17:16 Okay.
There are a few more things that I wanted maybe to go through in our tracking thing, and see where we are, and what's next.
So, for the content capture, Seems we are done, right?
**Dylan Russell** 17:47 I think so.
Because we decided not to do declarative config.
Yeah, this PR should still go through.
**Liudmila Molkova** 17:57 Yeah.
Okay.
I'll need to help it, maybe, but yeah.
Yeah, Ankit?
**Ankit Singhal** 18:07 Did you also cover the point about capturing content on events and… And I think there was a configuration which says Either both, or just events, or just spends.
I can pull that up, I think it was in one of the Python… One of the instrumentation memory, somewhere I saw that. I can pull that off.
**Liudmila Molkova** 18:31 Yeah, Kent, can you please send the link?
**Ankit Singhal** 18:34 Yeah, let me find this.
**Liudmila Molkova** 18:45 So this one, remember… This one, we merged.
This one… We all submerged.
Yeah, so this one is, something I wanted to chat about, because… I think, Dylan, you… you had a concern that if we capture, like, megabytes of binary content.
It's probably not always what users want when they just want to capture text content. Maybe we should have a separate Opt in for the binary.
**Dylan Russell** 19:30 I think we need some… Maybe general, like, size limit thing.
And then… Figure out what to do when the size is… Like, any attribute or… or part exceeds that size.
And we could do stuff with, like, the upload hook, perhaps.
**Liudmila Molkova** 20:02 And if, let's say, upload hooks are not configured, we just truncate.
**Dylan Russell** 20:12 Possibly. I mean, if it's just, like, 1%, is that useful?
It's like…
**Liudmila Molkova** 20:20 Better.
**Dylan Russell** 20:21 Yes.
Yeah… Trying to think what else would be useful to do.
You could record the size.
I don't know if that's that useful either.
Could, like, hash it.
Compress it.
**Liudmila Molkova** 20:46 Yeah, I'm thinking more like, let's say I have an application.
And in this application, I have all sorts of content, text and binary.
And I'm kind of fine with text going to my tracing database.
But… or a login. But not for the video-generated stuff.
Hmm. Maybe… At least what we can do today.
is to… Provide a configuration option.
To control the binary content versus Like, text content.
So that I can at least say that I want one, but not the other.
**Dylan Russell** 21:34 Binary content being, like.
**Liudmila Molkova** 21:36 The blog part.
**Dylan Russell** 21:40 Because right now, we just convert all, like, audio, video, image, all just gets converted to, like, binary.
**Liudmila Molkova** 21:49 Or URL, yeah.
**Dylan Russell** 21:52 Hmm…
**Liudmila Molkova** 21:56 Yeah, Emil?
**Emil F** 21:59 Yeah, so, I know this is kind of a tough nut to crack, but, truncating is not great, especially if you're transmitting, either, let's say, compressed content, which breaks it completely, or you're transmitting a big JSON blob, which just happens to be big, which also breaks it completely. It cannot be deserialized later on.
And on the binary versus text part.
Given that both are presumably inputs and outputs of the LLM, I think if you want a trace, you… and you want content, you'd want the whole thing, at least that's my… Understanding of how people are doing… doing stuff.
So, you should… I don't think that there should be discrimination between I want to capture just binary versus I want to capture just text. You either capture content or not.
And then it could be either.
**Liudmila Molkova** 23:00 Why shouldn't there be?
**Emil F** 23:05 Well… If you're trying to understand what happened in those LM calls, which is presumably why You want tracing.
What's happening would be affected by Both the binary and the text content.
Like, if you… if you throw on, an… an image, maybe, to the LLM, and ask it to tell how many kittens are in that image. The trace would not make sense without having the image, right? It wouldn't help with that.
**Liudmila Molkova** 23:41 It would. It would. It's just it wouldn't have all the information, but it never does.
**Emil F** 23:48 So, like…
**Liudmila Molkova** 23:49 Between the having nothing and having everything, there is the whole spectrum of, cost control.
And what my backend is able to ingest.
**Emil F** 24:04 True, but that's… Kind of on the backend to decide, right?
**Dylan Russell** 24:11 I also know a lot of backends will, like, reject it if, I guess, an attribute value is too big.
They'll just, like, reject it.
**Emil F** 24:21 Oh, absolutely, there always are limits, but, I don't… I don't know if… I don't feel confident that the limit should be… Dependent, or if there should be a switch for binary versus text.
So, for sure, limits are going to be there.
**Liudmila Molkova** 24:41 I mean, the limit would solve the problem to a certain extent, right? And, if we apply a limit on this.
Thing?
It would not truncate any structure.
And there are already probably limits in the spec.
And maybe we can just rely on them, or we can say that There are GenAI-specific limits for the blob part content.
And maybe… All the other contents.
**Emil F** 25:17 So, I'm…
**Dylan Russell** 25:18 Not our.
**Emil F** 25:18 I'm arguing with pitch limits definitely needed.
**Dylan Russell** 25:22 We just base64 encode, like, all audio, image, video.
Right now, that's what we do.
**Liudmila Molkova** 25:33 I think so, but, like, what we've been talking about, that we don't even need to base 64 in code, because any value should understand bytes and would encode on the exporter level.
So we would apply, like, just the length of the bytes.
The limit would apply to the length of the binary content.
**Dylan Russell** 25:54 So we would just… Get bytes out of whatever format the content is in.
**Liudmila Molkova** 26:01 Yeah.
**Dylan Russell** 26:02 And don't encode it, or… Or encode it using the whatever way it's encoded already.
**Liudmila Molkova** 26:10 We would give bytes to the exporter, and the exporter would decide what to do with them.
Okay, so if we were to introduce limits.
Do we need separate limits for GenAI?
Like, specifically this.
Or, we should be fine with whatever spec has for, like, the leaf nodes in this.
Any value And… if… if spec defines it, I don't remember. Trask, do you remember if we ended up putting it in the spec? I think we did.
**Trask Stalnaker (Microsoft Corporation)** 27:03 Which?
**Liudmila Molkova** 27:05 The any value leaf node.
Limits.
**Trask Stalnaker (Microsoft Corporation)** 27:10 Limits… The leaf nodes, yeah, I think we… do, I think it's just… it's the cumulative… That we don't have, I think.
**Dylan Russell** 27:26 I don't think that exists in Python.
Maybe it's in the spec.
**Ankit Singhal** 27:35 One question here, are we talking about the limits for the content size?
on these attributes.
**Liudmila Molkova** 27:43 Yeah.
**Ankit Singhal** 27:43 Yeah. And those, sounds like, from the discussion, it's more like a back-end… This could be a backend.
limitation support or backend limits, right? That kind of dictates this.
So should that be something that Semantic Conventions showed?
kind of enforced, or… Just leave it to the backend implementations.
**Trask Stalnaker (Microsoft Corporation)** 28:14 Enforcing the limit.
Currently, there's, the SDK has a configurable option to limit it, which is what Liudmila's highlighting there.
**Ankit Singhal** 28:29 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 28:31 It's a very coarse-grained limit, right? It's one limit that applies to all your telemetry values.
**Liudmila Molkova** 28:45 It kind of makes sense, right? Because you would set it for any telemetry.
That you have.
If we need separate ones, we can add, later.
Okay, so then the… the TLDR here seems to be… that… The problem with binary is more of a size.
Then the desire to configure them separately?
At least.
That's the… there's definitely a problem.
And maybe we can solve it with limits.
And then, if we… we can rely on SDK limits for now.
At least, until we get more feedback.
I want to think a little bit more about Do I want to pay for the binary content?
Even though if it's within the limits.
Because… It's probably… Something that affects my Agentic flow a little bit less than.
Like, the text, at least in most common scenarios.
**Trask Stalnaker (Microsoft Corporation)** 30:08 Oh, I see, so a double opt-in, one opt-in to get the… Input-output messages, and a second To actually get the binary.
Additionally.
**Liudmila Molkova** 30:20 Or combined, because it's already an opt-in flag, we can make it part of the enum, yeah.
Or we can make it part… Go ahead.
**Emil F** 30:35 I was saying, so an opt-in and an opt-out, that's what you're thinking, right?
Opt in for content, and then opt out of the binary content.
**Liudmila Molkova** 30:47 Yeah, I didn't.
**Dylan Russell** 30:48 Opt out of binary content.
**Liudmila Molkova** 30:52 So this is the… Ankit, this is what you sent, and yes, this is the… the… what we have in the… Conventions now. But here, we could say… This is the one environment variable, let's say, to… opt-in into text, and another one to opt-in into binary, or it can be one environment variable, and the values here would include some indication whether you want binary as well.
But maybe we don't need to solve it with environment variable, we can solve it with declarative config, where it's much easier to have, like, multiple properties.
**Dylan Russell** 31:31 Yeah.
I don't… because I don't see why you would want to just say all binary off.
like… I feel like you'd want to be more coarse-grained with, like, oh, I want images when they're less than some size, I don't want any audio.
I don't know.
**Liudmila Molkova** 31:51 Yeah.
I'm totally fine saying it's solved with declarative config, we will define the structure, it will be much more expressive than environment variable, and it will be experimental feature until the config gets stable.
**Ankit Singhal** 32:08 Can the SDKs consume the declarative context, right? That's my guess.
click button.
**Liudmila Molkova** 32:15 Yeah.
**Ankit Singhal** 32:17 This is…
**Liudmila Molkova** 32:17 Yeah.
And it is experimental, though, I think, but it works.
**Ankit Singhal** 32:31 This is…
**Liudmila Molkova** 32:31 Awesome.
**Ankit Singhal** 32:32 any SDK which is already using, like, these instrumentation libraries from OpenTelemetry.
We'll have to start supporting declarative config. Would it be, like, in addition to this environment variable, or replacing this environment variable?
**Dylan Russell** 32:51 Perfect.
**Ankit Singhal** 32:52 Yeah.
**Dylan Russell** 32:54 Sorry, I missed the question.
**Ankit Singhal** 32:56 So, my question was, like, we're talking about declarative config, right? Right now, a number of SDKs, they do already use this environment variable to figure out if they want to capture the content, right?
So the new declarative config that we add would be in addition to this, or would be replacing this, because that has different consequences based on what decision we make here for the existing SDKs who are already leveraging this environment variable.
**Trask Stalnaker (Microsoft Corporation)** 33:22 So, SDKs themselves for the, properties that are baked into the SDK, so that's not us, we are Instrumentation, but, just that the SDK has a clear answer to your question, which is that, environment variables are ignored if users opt in to the declarative config, because Nobody wanted to deal with how to merge them.
**Ankit Singhal** 33:51 those things.
**Trask Stalnaker (Microsoft Corporation)** 33:51 together.
For Instrumentation, That, I think, is probably a Python probably a Python-specific question. I know for, like.
in, like, Java, in Java instrumentation, What are we… We… So we automatically map, properties into declarative config, if the user's not using declarative config, so that we only have to read declarative config, we don't have to read both.
But… If the… I don't think we merged them.
So, I think if somebody's using declarative config, we would ignore the environment variable.
So that would be the best. That would probably be the most, it's… It's an awkward stance, From a evolution perspective, that people are using environment variables, and as soon as they adopt declarative config.
All their environment variables are ignored.
But that is the stance that we are taking.
**Ankit Singhal** 35:24 I see. So, if I'm not using the relative configs… then I can still continue using a non-material, right, as is. Right.
**Trask Stalnaker (Microsoft Corporation)** 35:34 Right.
Yeah, so it's kind of like… that's why it's not technically a breaking change, because users have to opt in to using declarative config.
**Ankit Singhal** 35:47 Got it. Okay. Sounds good.
**Dylan Russell** 36:00 Another thing here is, like… Do users maybe want to, like, convert?
Like, if they're uploading lots of images in, like, different formats.
Would they want us to, like, convert them all to, like, a standard format?
for them.
**Liudmila Molkova** 36:18 I hope not!
**Trask Stalnaker (Microsoft Corporation)** 36:22 Collector problem.
**Liudmila Molkova** 36:23 Yeah.
**Dylan Russell** 36:25 Okay.
**Liudmila Molkova** 36:26 Nobody from Collector here, so let's make it there.
**Trask Stalnaker (Microsoft Corporation)** 36:29 Yes, yes.
**Liudmila Molkova** 36:34 Awesome. So, we probably should put it… To post Stability there.
And… it seems like… This is… Mostly done unless we discover something new.
Fair?
Okay.
We are, out of time?
Let's talk.
**Trask Stalnaker (Microsoft Corporation)** 37:05 Very, very briefly about the naming… Because I think there's, like, a bunch of follow… like, the one that is basically unlocked… unblocked, but we have a lot of follow-up.
PRs to do.
**Liudmila Molkova** 37:19 Yeah.
So, these friends are done. This is the… what we have, the PR, already.
For 2 calls.
I think we're good.
Mostly, but, the span type, we have the internal suffix.
And based on the other discussion we had in the semantic conventions.
That the span type should align with metric names, we probably should remove the internal suffix.
So… and this is the minor… Thing.
I… I'd like to take connection… Take an action item on this one for now.
For the client invoke Agent.
Because we need a new metric for this, the span type stays, maybe we need something else.
And everything else, I don't know if it's in the scope of stability.
**Trask Stalnaker (Microsoft Corporation)** 38:28 Right.
**Liudmila Molkova** 38:29 But yeah, we should follow up, it's just maybe lower priority.
I can also take a look at this one.
and as a part of the rename, so I'm also moving them into… their own files.
So, like, the inference is its own file, the client inference, the… the invoke agent should be its own file.
For two calls.
I think it's also its own file, but we have links from inference and from agents to the corresponding metrics and spans.
Yeah.
What was the issue for the naming this friend, right?
**Trask Stalnaker (Microsoft Corporation)** 39:37 Yeah…
**Liudmila Molkova** 39:43 So we're good with this front.
From… we will be good with the… This friend's… I'll prepare something for this, too.
I think we… we need to do something about memory, but I don't know what yet.
And the retrieval is probably the borderline there.
like… Is it stability or not? Is it part of stability or not?
**Trask Stalnaker (Microsoft Corporation)** 40:24 We left it in the gray zone.
**Liudmila Molkova** 40:27 Yeah, so I probably should convert it, and it's not, like, a big deal. And I would love to deprecate the operation duration metric completely, so nobody uses it.
**Trask Stalnaker (Microsoft Corporation)** 40:38 Yeah, that makes sense.
**Liudmila Molkova** 40:45 Okay.
Cool.
Should we talk about anything else?
Ben, okay, thank you all.
See ya.
**Trask Stalnaker (Microsoft Corporation)** 41:00 by…
