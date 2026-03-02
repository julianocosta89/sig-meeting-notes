SIG: Event WG
Date: 2025-10-14
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Robert Pająk** 01:19 Hello, how are you doing?
**Trask Stalnaker** 01:20 Hey, Robert!
Pretty good.
Fantastic.
How about you? I see you were… I'm looking at the notes from last week.
You've been… oh, do you live in Warsaw?
**Robert Pająk** 01:36 Yeah, in Krakow.
**Trask Stalnaker** 01:38 Okay.
**Robert Pająk** 01:38 like, two and a half an hour train ride, so I would even manage to go back and forth one day. Nice. I didn't need to reserve a hotel, etc.
Poland is very small, you know, compared to the US.
**Trask Stalnaker** 02:38 So, yeah, let's see what you ended up with here.
Index, okay, I brought this…
Good point, yes.
Appendix.
Okay.
So, yeah, I didn't really… Wasn't sure what Daniel.
**Robert Pająk** 03:32 He was Daniel.
**Trask Stalnaker** 03:34 Yeah.
**Robert Pająk** 03:34 China's proposal, basically.
**Trask Stalnaker** 03:37 So he wanted to change it to must for all.
**Robert Pająk** 03:40 Yes.
**Trask Stalnaker** 03:41 Okay. Because he said that if some languages will do it.
**Robert Pająk** 03:45 they'll have requests on JavaScript anyway, even if… even though he doesn't like it, he knows that it will be a better user story.
**Trask Stalnaker** 03:53 Okay.
So, at your value text.
Hey, Lena!
**Liudmila Molkova** 04:08 A, it happened to me, I joined the wrong call for the first time. I joined Ruby's C call.
**Trask Stalnaker** 04:17 I haven't done that. Not the Ruby thing in particular, but…
**Robert Pająk** 04:22 Are there many people there, obviously?
**Liudmila Molkova** 04:24 Yes, they were surprised to see me there. I was surprised to see them in the log sequence.
**Trask Stalnaker** 04:46 Does this one need… Change, pinning… Oh, you've got a comment.
No.
Robert.
**Robert Pająk** 05:09 Yes, we need to change, because right now there's no anchor for Taipei.
**Trask Stalnaker** 05:16 Beautiful.
Okay, and since it's, OTEP, okay, got it, makes sense. Yeah, yeah.
Use standard attributes.
**Robert Pająk** 05:30 Thank you.
**Trask Stalnaker** 05:34 What did this mean, anyways?
**Robert Pająk** 05:36 You can… you can check, in the…
I think it was an ADNPA part of the specification. I think I removed the whole section.
about,
Leave this open, maybe this one.
And scroll down…
No, no, I mean, scroll down to other files, yeah. So, I think it's not in common with me. It's in locks…
Probably it's LOX API, if I remember correctly.
No, it's not in the common, because it was reusing standard attributes for the logs API, I think.
**Trask Stalnaker** 06:28 Oh, I see, this was reuse standard attributes. Oh, this was under logger. Yes, okay, I understand that.
And so now we're explicitly…
Okay, so now that's basically not…
Do we need something to replace that? I guess is my…
**Robert Pająk** 06:51 No, I don't think so.
**Trask Stalnaker** 06:53 Okay. What about supports?
complex attributes.
**Robert Pająk** 07:00 They should be there anyway, according to the logs data model. So for logs, it should be already there.
**Liudmila Molkova** 07:06 Should we have it for the other signals?
**Robert Pająk** 07:10 That's what maybe we should… consider.
question if we need to do it in this PR or separate PR, just do not.
For me, it doesn't matter. I'm just worried about, you know, heat picking. For instance, the name that I will edit, just now go back into circles.
That's my only worry, just to not scope group this.
**Trask Stalnaker** 07:40 Okay. I'll just mention as a follow-up.
**Robert Pająk** 07:44 Yep.
There's also a second follow-up, I think, from Tigrant's commenting.
And I plan to create issues when this emerged.
**Trask Stalnaker** 08:28 Okay, so all the attribute limit stuff is new…
So, attribute.
Collections.
Contain a collection of attributes.
I like the language neutral.
And we never were able to…
Land on something that worked for everybody.
**Liudmila Molkova** 09:18 I think most of this content is actually just copy-paste, right? It's not the new… Content.
**Trask Stalnaker** 09:25 Oh, I see, it's from… just from there, yes.
**Robert Pająk** 09:29 already here, but I think maybe one section, maybe I have taken from… I think one recent section I have taken from the logs data model, but the reason is that it was basically better defined, just a better wording.
**Trask Stalnaker** 10:31 Cool, yeah, I will… -
go through this today, but yeah, I don't think I have any… question… any… questions, really.
We have no topics.
So what's on our… what's… I think we've made a list somewhere before.
**Robert Pająk** 11:09 ghosts?
I'm not sure if there was an agreement when the blog post should be landed.
after this is merged with Omiwa, I think you have discussed with the TC.
**Liudmila Molkova** 11:19 Da… as soon as we are ready. So, the RTAP has landed, so we can…
write the blog post and publish it whenever we feel like it. It's not like… like, we've discussed it to the full extent, and it's not like we're changing the direction, right?
But we definitely… it would definitely take time to accumulate any feedback.
And it doesn't matter. We should be able to merge things and publish whenever we're ready. So, I didn't have a chance to work on the blog post and the feedback I've got. I will do it this week, and I'll share the PR once I have it.
**Trask Stalnaker** 12:13 And so this is all… With the… okay, the goal of… getting events… to… stability.
**Robert Pająk** 12:28 What do you mean?
**Trask Stalnaker** 12:31 What's our… What's our… mean… what's our goal? Like, what's the… Yeah.
what's our goal right now? Like, these are pieces… like, these are pieces… these are puzzle pieces.
**Robert Pająk** 12:48 implementing… I think we'll need to double-check in the OTAP what is still missing. I remember that this is one piece, the other piece is the blog post, other piece is the changes in OTLP.
To have these extended attributes in all signals.
And then probably the next pieces will be,
I think we semantic conventions for events. I remember that there were some things about should we use body or not, or should we use attributes? I think the next part will be stabilizing this part of documentation in semantic conventions. So this common…
common guidelines for events. I think that this is the important part, which will be next step.
**Liudmila Molkova** 13:33 Yeah, I also wanted, like, overall, I think our general goal is to implement the EventVisionOut app, right?
**Robert Pająk** 13:40 Yep.
**Liudmila Molkova** 13:41 And this is one piece, another piece, we had another tab that's got closed about the errors, right?
**Robert Pająk** 13:50 Yes.
**Trask Stalnaker** 13:50 Yeah…
**Robert Pająk** 13:51 I also thought about it, yeah.
Basically, semantic conventions around events, you should start working on them as well.
**Liudmila Molkova** 14:04 Yeah, and we have a doc. That's effectively one line, like, a few lines that mostly duplicate the spec at this moment.
**Trask Stalnaker** 14:15 Yeah, like, I think we have… we have clarity. Whether we've written it down or not is different, but I think we have clarity on, like, body versus attributes, and…
The… the one place where, yeah, I think we're lacking… And now, with the…
The complex attributes is a big… Peace there, bringing clarity.
I think the recording errors is…
Still, yeah, there's… I don't think we have clarity ourselves.
**Robert Pająk** 14:50 I think also we should make something in the README, and maybe in specification regarding user-facing.
APIs, because I think for Java and maybe other languages, they may want to not use the Lux API directly, but something which looks
More like a logging library.
But this can go in parallel, basically.
**Liudmila Molkova** 15:17 Or, like, event name attribute, if you don't interact with login API,
we should have a VIN. Do we care about it being stable, this flow?
**Robert Pająk** 15:29 Which… what's table?
Which one?
**Liudmila Molkova** 15:32 The thing you were talking about, is it, like, if I don't use a telelogin API, but I use event name.
As the attribute to represent the event name.
Were you talking about this case?
**Robert Pająk** 15:46 No, no, no, this case is noted, even if it's already stable.
I'm mostly talking about the ergonomics of the API, that someone could literally implement the logs API. And you're right, you're kind of right, this is about it, because someone can use the existing library, and could just, yeah, use this event name attribute.
Yes, you're right, this is also kind of part about it. So, if someone… if we stabilize this attribute in the semantic convention, that may be good enough for a lot of applications. But still, there is this thing that,
So, we have… We are using Weaver to generate the semantic conventions, you know, packages, helpers, And… basically.
If people have logging, like, a library, login library, which accepts attributes from the, you know, open telemetry package.
you know, the any value, basically, implementation. They can simply use the semantic convention-generated code to create events. We could even produce, like, almost ready event records that people could emit using this API, which…
But if people use, like, Log4J or things like that, they'll need to come up themselves to basically, you know, find a way to
to emit using Glock4j, for instance, the stuff which is, which is, you know, in semantic conventions. But, yeah.
I think we are not there yet. I think that there are a lot of experiments. People can also, you know, use Weaver to generate code for other logging libraries than Autel, so…
**Liudmila Molkova** 17:31 Yeah, I mean, it would be nice to stabilize event name. I don't think it's stable, I'm looking for it.
**Robert Pająk** 17:36 Not… it was deprecated, and now it goes back, or something like that. So, no, it's not stable, it's development for sure.
**Liudmila Molkova** 17:44 I, I, like, I mean, if we're sure the SIP API can be extended, And we are…
I wouldn't want to block us on stabilizing this.
**Robert Pająk** 17:58 Yep.
A senior can even work.
I think we can work on stabilizing event name. Already, we can start working on it.
**Liudmila Molkova** 18:07 We can, but do we have to? Like…
What… what depends on it, on advanced table? There's the… the… the SIG scope, is it in the SIGS scope? Is it required in the SIG scope?
**Trask Stalnaker** 18:24 I don't think it's required to get event… To be stable.
And I think because, like, even Java…
has decided, like, is more comfortable with using the log API, the existing log API, recommending that
for emitting events.
You know, we are… we are already supporting event.name,
from via, like, our Log4J and… and LogBack wrappers or appenders?
But I don't think any of that… I…
I don't think any of the ergonomic or user-facing questions are…
**Robert Pająk** 19:16 If you're… so you're saying that you're right now, kind of.
Implementing the semantic conventions for event name attribute.
That the logo bridge, if it has an event name field, it converts it to an event name.
**Trask Stalnaker** 19:30 Yeah.
**Robert Pająk** 19:31 That's… that means that we should stabilize this part, in my opinion. I think we should.
**Trask Stalnaker** 19:36 I mean, I don't think it's required for…
like, to Lynn Mila's point, but I'm… I'm all in favor of just…
**Robert Pająk** 19:45 Yeah, I don't… Marking it.
**Trask Stalnaker** 19:46 table.
**Robert Pająk** 19:47 confidence that people are using it. I know that a lot of people are complaining from the community that, you know, things are working, and they are not stable, and people, you know, are just feared that, you know, it will change in the future, and then you can use, you know, Log4J, and they are not sure if
if this, you know, pattern will remain, I think the more we give people the confidence that this will not change, the better for the users.
**Liudmila Molkova** 20:13 I'm creating an issue to stabilize it.
**Robert Pająk** 20:19 So… We have a nip…
**Liudmila Molkova** 20:21 Huh?
**Robert Pająk** 20:21 We have a processor, log processor in the example in Go. I can share it here.
That's 2000.
**Liudmila Molkova** 20:35 Should also be on Controversial.
**Trask Stalnaker** 20:38 I think so. I'm pretty comfortable, I would approve.
a PR right away for marking that.
table, just… We've got the event name at the proto level.
It just… I think maybe the only question worth
Discussing is sort of what the scope of event name
should be used for? Like,
being clicked. Can you put the… that attribute on a… well, people get confused that you can put that attribute on a log, like one of our logs, instead of calling setEventName?
But at least as providing that as a stable point of entry for… appenders… Yeah.
Hey, Austin.
**Austin Parker** 21:45 Hey, sorry for being late.
**Trask Stalnaker** 21:48 No worries, thanks for joining.
**Robert Pająk** 21:54 I'm trying to fix the hyperlink for the events in the meantime.
**Austin Parker** 22:04 We're talking about… Isn't, isn't the… rationale that… Event… That when you have a…
Log record with an event name, it's an event.
Yeah, I don't… I think it's something we'll just be clear about and document, but I don't…
**Liudmila Molkova** 22:38 So we would need to, as a part of the stabilization, probably need to answer the question, so if it… what appenders should do? If they get event name, they should populate event name property.
Do they keep the attribute?
Or… no, they don't.
**Austin Parker** 23:03 conf…
Sorry, so if you are using the… if you're using an appender… if you're using the bridge, and you have an appender hooked up, and it receives a message with an event.name…
It should populate event.name… Or are we saying the appender, or the bridge should try to…
I guess this is a practical question. Do we anticipate, like, if…
If we see… if you see event.name, is there effectively going to be type checking?
Like…
Are you… when you see event.name, does that mean you're constructing an instance of an event, and then all fields that are not on that event are dropped?
**Trask Stalnaker** 23:52 No.
You're not doing schema checking. I mean, we're not doing any schema checking on the client side anyways, though.
**Austin Parker** 24:01 Yeah, but like… But… We are theoretically saying that
If something match… if something has an event.name, that means it is an instance of… X.
Right? So, the guarantee that we should be making to downstream consumers is that all fields that are part of that
exist.
And… da-da-da-da-da, right?
**Trask Stalnaker** 24:36 Sure, but that is, I think, independent of the bridging. That same thing applies if you're just using our log API directly to emit events.
**Austin Parker** 24:49 Right, I think… I guess my question is…
Remove that question, but my concern is that if you…
It's collisions with typed events that we… like, if you have…
You have some application, and it's emitting Structured logs…
with event.name as a property, and those names happen to collide with the…
With a semantic event that we define…
**Liudmila Molkova** 25:25 So you either set the event.name.
If you use a bridge, if you use a top-level API,
It's a good question, right? I would imagine that if you use the log API, and you didn't set event name, but you said the attribute.
the API and SDK wouldn't do any effort to save you from this, and it wouldn't be an event.
But should they?
**Austin Parker** 26:00 I mean.
**Trask Stalnaker** 26:00 Both… I think you might be talking about different things, both of you.
Maybe. My point is…
**Austin Parker** 26:07 that if… If you're using the
I guess, what's the alternative here, right? That if we get event.name through a bridge, then we don't set it to event.name, because we can't guarantee that it's actually an instance of the event.
All we can guarantee is that
someone at some point said, I want a structured log… I want a log with event.name as a field on it.
Whereas…
**Robert Pająk** 26:37 Basically, we were also worried about these collisions somehow in Go, that someone may already use it. That's why I decided to not put this translation into the bridges.
because then all… everything will be mapped. We decided that it's the lock… the SDK processor work to do it, so then people, if they're confident, they can translate everything. But if they have a collision, then we can have a processor which manually deals with it, if they need it.
So, instead of, you know, also implementing this feature in all bridges, if they see an attribute like this, yes, we propose to implement it once on the processor level.
**Trask Stalnaker** 27:22 Right, I still think we're talking about… I think… still think you're.
**Austin Parker** 27:25 We were talking about different things.
**Trask Stalnaker** 27:26 Because, Robert and Lyudmila are talking about the difference between the event.name attribute and the event name protofield.
And Austin, I think, is talking about event schema validation.
**Robert Pająk** 27:41 I also…
**Austin Parker** 27:42 So to… to your all… to… to the event name versus event.name.
I would say the bridge should not set event name.
Because… From a schema perspective, we have no way to tell… If it's actually… An event, right?
**Liudmila Molkova** 28:06 We don't have any means either way.
**Trask Stalnaker** 28:11 Same problem with the log API.
**Austin Parker** 28:13 Well, but… no, not necessarily, because with…
Semantic events, we could public… we could have a schema, or we could have, like.
It's similar to, like, a constant for… SemConv…
you could have an event SEMCOM that you would create new whatever, you know, you would new up whatever, and that would be…
taped, so you won't…
**Trask Stalnaker** 28:41 have the underline… you can still always use the underline OpenTelemetry Log API to emit events in any shape that you want.
**Austin Parker** 28:51 Right, but it wouldn't… But that would just be… that would be a, like… Yes, but that would be…
you would just call it a… you would have a whatever, right? You still have… you have to be able to create…
events, and you… if you're using the underlying API, yes, you could give it an event name.
but you'd be constrained by what the… by the API. It would be a…
it might not be a semantic event, but it would be semantic… it would guarantee that it would meet the requirements of, like, the event API, or the log API, right? Because it would be structured in a way we expect it. It wouldn't have, like, weird or unexpected fields, or whatever.
Whereas, if it's through the bridge, we don't have any of those guarantees.
So we shouldn't treat anything that comes to the bridge as, like.
A semantic event, because we can't guarantee that.
**Robert Pająk** 29:57 Maybe, Austin, what you're talking about is, .
**Liudmila Molkova** 30:02 something on top of Logs API that provides type.
safe events, that when you meet an event, you actually meet a specific
Hype that describes all the events.
**Austin Parker** 30:16 Her properties.
Yes.
**Liudmila Molkova** 30:19 Logs API does not provide… HotelLogs API does… would never provide these guarantees, right?
**Austin Parker** 30:26 Correct, but, but, if you just take the Logs API and you create an event through the Logs API,
Structurally, we would still be able to say that it meets… it might not be typed, it might not be a semantic event, but it would still meet all the other criteria of the event, right?
**Liudmila Molkova** 30:43 There's just one criteria.
**Trask Stalnaker** 30:45 Rich.
**Austin Parker** 30:47 Because with the log bridge, we can't guarantee that.
Unless we're coercing… unless the log bridge is coercing everything… to…
**Trask Stalnaker** 30:58 But to Lyudmila's point, our… the only defining characteristic of an event is that it has event name.
**Austin Parker** 31:06 But what about, like… attribute types, like, what about buying, like…
I have no clue this is even something people would do, but…
What happens right now when you have a… if you had a structured log, That had a binary field.
**Trask Stalnaker** 31:26 valid.
**Austin Parker** 31:29 Is that also valid through the log API?
**Trask Stalnaker** 31:32 Yep.
**Austin Parker** 31:33 Really?
**Trask Stalnaker** 31:40 I mean, you're right, though, there is some coercion, right, of types, but that's… the log bridge has to do that anyways, so anything that it's… it's got a…
have some… Definition of mapping there anyways, so…
**Austin Parker** 31:58 Yeah.
**Trask Stalnaker** 31:58 not give the convenience to users, because otherwise, people using Log4J Have no way to…
**Austin Parker** 32:07 to create events.
**Trask Stalnaker** 32:08 Create an event.
And we're locking them into our logs API.
**Robert Pająk** 32:14 just trust, but because of these reasons, we thought that people, probably, that want to probably use, you know, the auto APIs, and people who just use regular logs will use the bridges. That's why we think we thought that the processor
We do it to set, you know, event name from the event name attribute as a processor, so if people, you know, want to do it this way, they will just use the processor to set the event name.
Also, the other reason is that they are able to… yeah, these are trade… there are trade-offs, basically.
**Trask Stalnaker** 32:50 And I'm fine with the Go, you know, ecosystem deciding something…
**Robert Pająk** 32:55 And I don't know if it needs to be specified. I think we just need to give freedom. If people want to do it in bridges.
Or, you know, yeah.
**Liudmila Molkova** 33:04 I think it should be something predictable, so if one bridge in Go ecosystem would do one thing, and a different bridge in Go ecosystem would do another thing, that would suck.
**Austin Parker** 33:16 M.
**Robert Pająk** 33:17 Yeah, but we chose controls, open source stuff.
**Austin Parker** 33:20 Well…
**Trask Stalnaker** 33:22 We can specify.
**Austin Parker** 33:24 Here's a potentially useful question.
From an end-user perspective, what's the difference?
like… Because ultimately… Let's pretend that,
Let's pretend we have someone that just installs stuff with the defaults.
So, no… no fancy processing, no pipeline stuff in the collector. They just install stuff, they install the log bridge.
Send it in to whatever backend.
what is the principle of least surprise for their existing telemetry data? Because if… I would assume…
Well, I don't know, I don't know if anyone actually has implemented special handling for event name.
Right? Because that's really what it comes down to, is… is… does the backend handle the top-level event name field, and if so, how does it?
**Trask Stalnaker** 34:28 So, I agree that it's a breaking change, which is why in Java, for now, it's opt-in, and we're gonna flip that switch and 3-0.
To make it default, on by default.
ProcessingEvent.name.
Yeah, it's definitely a breaking change, because people…
Especially given our history of having event.name previously, already around for a while.
I suspect that there are people using that.
**Austin Parker** 35:09 So… So the question is…
What's…
Trying to think how people would handle this now.
Let's assume that somebody… let's assume that the backend receives it, flattens, and then flattens, or doesn't flatten, but…
now they have two event.names, right? Like, if… if they were…
Assuming that, like, the answer is we set event name, but also we pass the field through. Or I guess it would be… it would be body.event.name?
**Trask Stalnaker** 36:03 B, as an attribute, event.name.
**Austin Parker** 36:05 But not in the body, it would just be in the attribute bag.
**Trask Stalnaker** 36:08 Yeah.
**Liudmila Molkova** 36:10 And if somebody did it, we probably shouldn't touch and do anything with this thing. We shouldn't update the top-level event name property.
**Trask Stalnaker** 36:20 I don't think we can in the SDK, because we don't want a major version bump.
And that would be breaking, but we could semantically, say, give guidance to backends that
the event name protofield has priority over.
**Austin Parker** 36:39 Yeah.
**Trask Stalnaker** 36:40 the event.name attribute.
**Austin Parker** 36:43 Yeah, I'm just trying to think, is it… because the… if you assume people… I don't know what our current guidance is, but the kind of lazy implementation here is that you just… is either A…
You assume that already, and you just pick…
So if you see event.name as an attribute, then you pick that. If event name is filled in, you pick that.
And if they're both filled in, you say event name has higher specificity, like, I think we should probably just encode that, and we should just, like, put that in the spec or something, and just say, like, hey, this is the order.
And then, if people aren't doing that, And it collides… Dunn…
it's… whatever their collision logic is, right? Like… Last one, William.
**Trask Stalnaker** 37:34 Back to, kind of the initial question of what… or one of the initial questions, which is what's the scope of event.name attribute?
Cause one option is to say, this is… Only applicable to log bridges.
And it should never… we are not blessing this as a semantic convention for…
over the wire, back-ends, anything else, it's explicitly for… bridging.
**Liudmila Molkova** 38:10 kind of like…
**Trask Stalnaker** 38:11 And that was why, I think, Robert, one of your PRs, maybe even, like, you had hotel.event.name.
like, mimicking the… what we do for Zipkin, where we have these…
**Robert Pająk** 38:25 confused.
**Trask Stalnaker** 38:26 Yeah, we have these special… Semantic convention attributes that are just for this purpose of mapping
Something that's a native open telemetry field into somewhere that only has key-value pairs?
But that is a worry about event.name seeming so… generic, that, like.
It could be confused easily that…
**Robert Pająk** 38:56 I think I added to the chat, this kind of stuff in specification. Maybe we should also kind of do something like this also, here in the specification, because it may be, you know, important piece to make sure that it is only for compatibility reasons.
**Liudmila Molkova** 39:16 We kinda already have EventName, right? So, that's the reason…
I pushed back on introducing hotel event name.
And… it… it… If we didn't have event name, I would agree.
The problem already exists,
**Trask Stalnaker** 39:40 Does it have… does Event Name have another purpose outside of that? Because we… we had it.
Because we didn't have the proto-field.
Now that we have the protofield.
And I kind of like event.name, for the bridges, because it feels very natural, instead of hotel.eventname.name, but, like, the explicitness of hotel.event.name
Does solve some of the… Worry about abuse.
Unless we think event.name has more… General… usage.
**Austin Parker** 40:22 I can just see a lot of people with event.name as an existing field.
**Liudmila Molkova** 40:29 Right, so…
**Robert Pająk** 40:30 It's about the same.
**Liudmila Molkova** 40:31 Yeah.
**Trask Stalnaker** 40:37 So maybe hotel.event.name after all.
**Austin Parker** 40:42 I mean, I think if we're trying to make a very
If we're trying to say that… OTEL events are this…
Bucket of things over here, or an hotel event is something that…
Although, oh, no, I just talked myself out of it, because I could also see us wanting to… because OTEL is a reserved namespace, and I could see us wanting to use this for meta events.
I could see us wanting to have hotel.event.name and reserve that for, like, span start, span end, like, other sort of…
Like… Span, like, attribute added, things like that, that we keep talking about.
And I'm not sure I really want to burn it on… this.
**Trask Stalnaker** 41:41 event.
**Liudmila Molkova** 41:42 The event name would be probably start with hotel.spensed.
**Trask Stalnaker** 41:47 Yeah.
The event name would be the same.
**Liudmila Molkova** 41:51 Forget a…
**Austin Parker** 41:53 Oh, oh, okay.
No, you're right, I'm stupid.
**Trask Stalnaker** 41:58 You're definitely not, but…
**Liudmila Molkova** 42:00 Absolutely not.
**Austin Parker** 42:03 Oh, my brain is stupid today. Okay, yeah.
I guess, okay, so, talking myself back into it. So the thing about saying hotel.event.name would be specifically the key, like…
Distingu- to distinguish for bridge consumers…
The difference, basically, it's the difference between, like, hey, this is a legacy event, or this is something that was bridged in, and we have no gear, and it's effectively opaque to us, other than matching the type guarantees, versus, hey, this is someone creating a hotel event
The… Through a bridge API.
**Trask Stalnaker** 42:49 Yep.
Yep. I mean, it keeps it very narrow.
**Austin Parker** 42:53 Yeah.
**Trask Stalnaker** 42:54 And avoids us, like, re-litigating, like, a lot of event.name versus…
**Austin Parker** 43:01 Yeah.
**Trask Stalnaker** 43:01 same…
**Austin Parker** 43:03 It… it seems like the least bad option.
**Liudmila Molkova** 43:06 Well, but…
forget about bridges. We already have the past with event name. Whatever questions we're trying to answer with event.name.
Oh, sorry, with hotel.event.name.
They are the same with deprecated event.name.
Why do we want to have different answers for them?
**Trask Stalnaker** 43:32 The deprecated one, though, got replaced by event name protofield.
**Liudmila Molkova** 43:40 Right.
**Austin Parker** 43:41 Yeah, this would just be an attribute.
**Liudmila Molkova** 43:44 So, this attribute would… Be converted to the top-level property, by something?
**Austin Parker** 43:53 No.
**Liudmila Molkova** 43:54 For a huge pro…
**Trask Stalnaker** 43:56 Yeah, by the… the appender.
**Austin Parker** 44:01 Well, I thought it was that the appender would…
not translate it. Like, the appender would not translate it to hotel.event.name.
That if it saw… if the appender sees otel.event.name, then it will turn that into the top-level event name.
If it doesn't see that, then it doesn't set the top-level event name, it just leaves it as event.name.
**Liudmila Molkova** 44:26 But if I used to have
If I used to use an appender, and I set the event name property.
Ow…
Where would it be to ask users to change this event.name to whatel.event name, and what would be the benefit of this?
**Austin Parker** 44:48 I mean, my argument is… Again, going… to…
the event schema validation stuff, and sort of the generic guarantees we make about anything that we semantically… anything that shows up in SimConv, we…
I would argue that we… Try to guarantee to consumers that
you know, something in SEMCOM, if it says it's supposed to be there, it's there.
And we can't necessarily guarantee that without doing this.
**Liudmila Molkova** 45:30 I mean, I used an appender.
And a set event.name.
on my appender. It emitted The valid event so far.
**Trask Stalnaker** 45:42 event.us using emitted event.name attribute over proto.
**Liudmila Molkova** 45:48 Right. I mean, we… it's a recent change that we introduced, the top-level property, right?
**Trask Stalnaker** 45:53 Yeah, so event.name used to flow all the way through to the backend.
**Liudmila Molkova** 45:59 Yeah.
So the part we're changing, that it's a top-level… oh, so…
What you're saying, that you would rather keep this behavior and the event name
would flow all the way through. Yeah. The auto event name would not.
**Trask Stalnaker** 46:18 Right.
**Austin Parker** 46:19 Right. Yeah, if you set hotel event name, that gets replaced
that gets dropped and gets turned into proto-event name, right? It's basically, we want to be able to give people that are using the appender, or using bridges, to create
Correct.
Hotel events.
without having to use our API. And to do that, we need to give them a way to specifically, mechanistically say, hey, I am putting this into the official event box over here, and from, like, a mechanistic perspective, and yes, today, maybe that is…
just a statement of intent, but from a, like, forward-looking perspective, we have to… I think we have to be able to…
Give people the, you know, the notion that
events are things… like, hotel events are specific-typed things, and opting into this…
Means that there may be consequences And so…
That's why you need to be very specific in saying it. And you don't have to do this, But…
Like, I think this is just, like, a general, sort of, hotel thing that…
We have to be able to…
Give all of these… this completely disconnected and uncoordinated consumers guarantees, at least soft guarantees, about the shape of data they receive.
And I think it would be… really challenging… if we said that, oh…
You can receive event, you're gonna receive events, and you have to look in these two places to see if it's…
you know…
Like, we need to be… it should just be as simple, is the proto-event name field populated? Yes? Cool. Then it's…
Then it is some type of hotel event.
And go from there. And if it's not, if it's not populated, then it is…
Some sort of non-OTEL event, and go from there.
**Trask Stalnaker** 48:50 Alright, so are we moving on to hotel event?
Dot name versus hotel event underscore name.
Debate.
**Liudmila Molkova** 48:58 Yeah.
**Austin Parker** 48:59 I mean, I'm fine with whatever.
**Liudmila Molkova** 49:01 I mean, the name is the property of the event, so from SemConf perspective, it should be separated by dot, and if you're in doubt, always use dot. That was our SEMCONF decision-making tree.
**Austin Parker** 49:16 I like thoughts.
I like dots, I don't like mixing dots and dashes, or dots and underscores, so…
**Liudmila Molkova** 49:30 So I tell.event.name, and we're going to introduce it, and then stabilize it.
**Austin Parker** 49:36 Yeah.
**Trask Stalnaker** 49:38 Introduce it first, for starters.
**Liudmila Molkova** 49:41 Yeah.
Okay, I'll update the issue.
**Trask Stalnaker** 49:59 Wondering if I can still,
To avoid would… this is only… In the upcoming release.
Event name… in Java, so, I may… Tried to…
Do something to avoid changing it twice in success… in… Successive releases.
But also, the hotel.event.name makes it…
Now, not a breaking change, which is nice.
So we can turn that on by default right away.
**Liudmila Molkova** 50:48 Can you repeat?
**Trask Stalnaker** 50:49 Yeah, you… Having this, so with event.name.
We didn't want to turn it on.
By default, capturing that, because that would be a breaking change for users.
Who were already emitting event.name.
**Liudmila Molkova** 51:13 Okay, yeah, so a total flow, yeah.
**Trask Stalnaker** 51:16 But I'm presuming that nobody is using otel.event.name.
And so, we could…
**Robert Pająk** 51:25 safer.
**Trask Stalnaker** 51:27 Turn that on by default right away, and not consider it a braking change.
**Austin Parker** 51:32 Yeah, because it's additive, so I like… I like it even more now.
**Robert Pająk** 51:41 I just want to say that I supported this proposal. This was my origin.
**Liudmila Molkova** 51:45 Sorry for…
**Trask Stalnaker** 51:47 I think it's a while to catch up to you.
**Robert Pająk** 51:49 Bro!
**Trask Stalnaker** 51:49 Oh, wait!
**Robert Pająk** 51:50 No, to be honest, this is when you feel that you have more confidence.
**Austin Parker** 51:57 No, I think this'll… I think this… this makes sense.
**Trask Stalnaker** 52:01 Oh, this was a good discussion!
**Austin Parker** 52:04 Yeah.
**Trask Stalnaker** 52:05 Something I thought was… obvious to… Throw in event.name.
**Robert Pająk** 52:13 I have a question. Who has right now time to have just an action item to all reopen this issue or create a new one? Just as a follow-up?
**Liudmila Molkova** 52:23 I just…
**Robert Pająk** 52:23 I cannot do it right now.
**Liudmila Molkova** 52:25 I've created this shield, and I'm updating it as we speak.
**Austin Parker** 52:29 Fantastic.
**Robert Pająk** 52:30 Cool.
**Liudmila Molkova** 52:30 The link is in the agenda on the top level, I think.
Yeah.
I'm updating the… the… everything.
**Robert Pająk** 52:50 Alright. What we… what we want to do with this event name attribute?
The current one that we're back.
**Trask Stalnaker** 52:57 deprecate it back.
**Robert Pająk** 52:58 Yeah. So… so maybe…
If you have time, maybe even consider reverting my… the commit, which was introduced by… by… by… by myself.
I think it could be easier that way.
**Liudmila Molkova** 53:13 We still need to introduce the new attribute, right? And maybe it would be…
**Robert Pająk** 53:16 Okay, but we can first… we can first bring it back to deprecation by reverting mine and create a separate PR which adds it.
Yeah, I think it would be easier if we revert this one and add a separate PR, adding the one, instead of changing this one.
**Liudmila Molkova** 53:33 Is there anything that you would like to keep in this PR?
**Robert Pająk** 53:37 Probably for the new PR, just steal this wording, so use the… the stuff which… the description from here in this new… in this new attribute.
**Trask Stalnaker** 54:02 I would just rename this.
Well, no, no, we need to deprecate it and introduce a new one.
**Robert Pająk** 54:08 Yes.
**Trask Stalnaker** 54:08 Renaming would be bad here.
**Robert Pająk** 54:11 Exactly.
**Trask Stalnaker** 54:15 But I'm okay with it being in one PR.
**Robert Pająk** 54:18 size, I am not sure if this attribute should not be defined in this autocompatibility registry, not in the event, because it is not an
Even somatic per se, this is just for the sake of compatibility.
Yeah, somewhere here, but I think in semantic conventions, we have the same, like, almost copy-pasted, if I remember correctly.
I have… we have a lot also group in semantic conventions.
So probably I will edit the…
Not entity… And the street, it was the 50s, or…
Maybe it wasn't, it is? Yeah, it was here.
Because, basically, at least there are attributes about mapping from…
**Trask Stalnaker** 55:17 Yeah, this makes… I mean, I think it would naturally fall in here anyway, now that we're putting it under hotel.
**Robert Pająk** 55:25 Excellent.
**Trask Stalnaker** 55:36 Alright, we have… Hit our 5-minute window.
**Liudmila Molkova** 55:43 Yeah, and we thought that event.name would be uncontroversial.
**Trask Stalnaker** 55:46 I know! I know, man, I was wrong about that.
**Austin Parker** 55:51 Oh, yes.
**Liudmila Molkova** 55:54 Okay.
**Trask Stalnaker** 55:55 Cool.
**Liudmila Molkova** 55:56 Thanks.
**Trask Stalnaker** 55:56 Thank y'all.
**Liudmila Molkova** 55:57 The CEO?
**Trask Stalnaker** 55:57 Bye, everyone.
**Robert Pająk** 55:59 Too late there.
**Liudmila Molkova** 56:00 Thanks.
**Trask Stalnaker** 56:00 Bye.
