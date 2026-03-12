SIG: Technical Committee
Date: 2025-09-17
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/xvQb6oUFUmf0r-XPnAM1aQxx4dcYFuySMGocNXrh9jb57SeAwSijGhFKEdDUYWan.U6w-a58e9e795_SH
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 00:28 Hi, Carlos.
**Carlos Alberto Cortez** 00:31 Hey, hey!
**Josh Suereth** 01:14 Hey, everybody.
**Carlos Alberto Cortez** 01:17 Hello.
By the way, Armin, weren't you supposed to be on holidays?
**Armin (Dynatrace)** 01:23 No, do I still have the… status on.
That might be.
I was out last Friday, this Monday, and upcoming Friday.
**Carlos Alberto Cortez** 01:36 Oh.
**Armin (Dynatrace)** 01:38 So just scattered around a bit.
**Liudmila Molkova** 01:44 Hi, folks.
**Tigran Najaryan** 01:48 Whoa.
Did we skip the TC call last week?
I don't see any meeting notes.
**Armin (Dynatrace)** 02:06 Or with the…
**Tigran Najaryan** 02:08 With the GC, okay.
**Josh Suereth** 02:14 By the way, you feel better, too.
**Tigran Najaryan** 02:15 We… So, sorry, I think we didn't do the… New member election stuff, anything related to that last week?
**Josh Suereth** 02:25 It was in a private call.
**Tigran Najaryan** 02:30 Okay.
**Josh Suereth** 02:31 Yeah, I think we have a private topic today related to that, unless you want to talk about it publicly?
**Tigran Najaryan** 02:37 That's fine.
**Carlos Alberto Cortez** 02:39 I also have a private topic, by the way.
**Josh Suereth** 02:42 Okay.
I have two topics, and hopefully they're very quick. Who's running the meeting this week?
**Carlos Alberto Cortez** 02:48 I mean, by the way, I hope that my connection is nice. I… there was some drilling in my building again. So, let me second.
That's fine.
Nice.
Perfect, okay.
**Josh Suereth** 03:12 Okay, so this is a proposal to stabilize service and deployment semantic conventions. This is actually coming out of a team in Google Cloud that I've been advising.
So I was planning to provide sponsorship of this. Currently, we think that this would be escalating sponsorship from the TC, because it's a semantic invention SIG, and it needs semantic invention maintainers. There are actually 3 semantic invention maintainers signed up to sponsor this right now. Trask, myself, and Yao.
So I think that from a TC standpoint, this is only escalating sponsorship.
But I wanted to confirm with everyone.
**Armin (Dynatrace)** 03:55 That's very reasonable, I think.
**Tigran Najaryan** 03:59 Yeah, sounds good to me. I think… is the plan that there will be new attributes introduced? That's what I see there.
**Josh Suereth** 04:07 there are… there's plans to add a few new attributes and to stabilize the concepts, totally. So the, you know, understanding the ownership of a service, understanding the criticality, that's two that they want to add, but also just getting, like, right now, instance ID isn't stabilized.
but service name is, so it's kind of awkward where the ID isn't stabilized, but the grouping is, so that's one thing. And then deployment environment name, we know a lot of people use this, and so what we want to do is stabilize it, which means taking a look at it, taking a look at what it needs to model, what it needs to look like, getting it up to date, and stabilizing, Either stabilizing it as is, or making changes based on what the group decides the model should be overall, for what deployment means.
**Tigran Najaryan** 04:58 Okay, sounds good.
The service owner thing… Isn't… if that's the theme… That's… there's an overlap with the… I think we say namespace can be the theme, right?
It's probably not the place to discuss it, just a quick comment.
**Josh Suereth** 05:16 Yeah, yeah, we can discuss it there. Namespace is also not stable. So we need to stabilize it. So if owner belongs in namespace, great, but let's make sure that's clear and stabilize it. It could be that owner is actually something orthogonal to namespace as well.
So, that's… anyway. I will update the thread and declare that. Second thing I wanted to talk about briefly, just because I think we need to talk about this in the specification meeting, complex attributes and empty values. So, when we added complex values or attributes to the SDK, We… Have in the specification, a thing that says, basically.
If you express a numerical value, like an empty string, an empty array.
or zero. These are meaningful and have to be stored and passed to processors and exporters. The problem with this is.
You should not do this in protocol buffers, and more importantly, the default protocol buffer libraries will not do this.
And so Java ran into a problem where they were using the protocol buffer library to serialize something between a processor and an exporter.
and deserialize it, and the attribute value was getting lost. In the proto-definition of the specification, we actually say that, the empty value is meaningful if something doesn't exist, but we also say that, like, you know, we don't serialize empty strings, basically implicitly by using Proto.
So, in Proto, an empty string is not serialized. But we call out this special thing called empty.
Of an any value that doesn't have a field filled.
**Tigran Najaryan** 07:02 So… Empty any value is not the same thing as an empty string. I'm surprised that people actually chose to implement it that way.
**Josh Suereth** 07:12 It's not that they chose to implement it, they don't have a choice, is what I'm saying. If you use protocol buffers, and you put an empty string into a field, by default, the protocol buffer library will drop the field completely, and it will just be empty.
So it turns it into an empty any value.
It's the same as if you set an integer to zero. Integers that are zero or the default, are not serialized by default. They just don't go over the wire.
**Tigran Najaryan** 07:43 Okay.
That's… that's a protoft library implementation.
May 3rd, right?
**Josh Suereth** 07:52 That, that…
**Tigran Najaryan** 07:53 The wire format doesn't… doesn't… doesn't preclude that. You can easily include a zero-sized string on the wire.
**Josh Suereth** 08:02 You can, but when… but then we don't work the way the rest of protocol buffers work. So Java has a test, for example, where they use the out-of-the-box protocol buffer serialization framework, they use our serialization framework, right?
They serialized a protocol buffer.
And if we follow this convention of serializing empty strings, they look different on the wire. The bytes are different, the size is different.
And so compatibility is awkward in that case.
**Tigran Najaryan** 08:31 I mean, yes.
**Josh Suereth** 08:32 People that you have to write your own proto-definition.
Your own code to serialize.
**Tigran Najaryan** 08:40 I will need to check what the collector does. I'm very surprised to hear this.
Because I don't think that's the default behavior of Google Proto, but I may be wrong on this one.
**Josh Suereth** 08:51 It was the default behavior. We had to go through shenanigans to get optional to work in the past, to make sure that that was serialized.
**Tigran Najaryan** 08:59 Okay.
**Josh Suereth** 08:59 Like, the collector is not a good example, because the collector customizes its serialization, and actually does a lot of customization. My argument here is, you know, somebody who naively uses the protocol buffer libraries would not abide by OTLP if we make this the case.
**Tigran Najaryan** 09:17 Okay.
**Liudmila Molkova** 09:19 Why do we even care? Why is it meaningful?
If it's actually very hard to make it, Even visible to the consumers.
**Josh Suereth** 09:29 Right, that's… that's why I'm escalating this. I think when we talked about the protocol, It wasn't meaningful.
Like, we allowed empty, And, like.
things that are empty strings and things, I would not have expected to show up at any value. I think we have this concept of empty, which is… and apologies if I use language nerdism, it's a bottom type to represent empty values. Meaning, empty could be a string, could be a list, we don't care.
Whoever's reading the attribute value can interpret it as whatever type they need it to be interpreted as, and empty means the same thing in all those types.
**Tigran Najaryan** 10:10 Empty is the equivalent of Nelson and stuff like that that you get in many languages, right? So…
**Josh Suereth** 10:17 Similar to null , but not quite, yeah. Like, because it turns into an empty string, it turns into an empty array, which technically is, like, a null pointer, but in some languages, but not others, etc, yeah.
**Tigran Najaryan** 10:31 I'm not sure I understand what you're saying. It doesn't turn into an empty array. What do you mean by that?
**Josh Suereth** 10:37 So, if I interpret a attribute as an array, and it has an empty value.
**Tigran Najaryan** 10:44 If you interpret it, why do you do that?
The type of the… of the any value is empty.
**Josh Suereth** 10:51 You don't… you shouldn't interpret it as an array.
I see what you're saying. You're saying, like, we should… it becomes a different type.
**Tigran Najaryan** 10:59 Yeah, it's its own distinct type, right? The empty value is a different type of an any value.
**Josh Suereth** 11:05 Yeah, but then you can do that, but we can also say it's a distinct type, but it's a bottom type, which means an empty type is interpretable as a string, and it would be the empty string.
**Tigran Najaryan** 11:18 Absolutely.
**Josh Suereth** 11:19 It's evaluatable as a list, and it's the empty list.
**Tigran Najaryan** 11:22 Okay, one of type in Protob is the union type.
Where the known type is implicitly included. There's no way not to have it.
This is just the recognition of that fact, that that known type is part of the protobuf's one-off concept.
And because it exists.
we said that we may as well use it, because in languages, you also have a similar concept, NAS or NIOS, or whatever is it, right? You mop it to that. That's what this is all about.
**Josh Suereth** 12:02 Kind of, but not, not quite.
So… We have a data model.
For attribute value, in the specification.
We have a protocol buffer encoding of that data value.
The way that we have allowed the data model to evolve, if we think the type is important, then our protocol buffer structure is fundamentally broken, because you lose type tags on empty values, by default, in protocol buffers.
**Tigran Najaryan** 12:32 I disagree with the formulation that you have. You don't lose the type tag on empty values. Empty value is its own type.
It's a type. The emptiness is the type.
**Josh Suereth** 12:43 Sure. But that means, like, if I provide an empty string, what I'm really doing is I'm providing the empty value.
**Tigran Najaryan** 12:52 No. The empty string should be encoded as an empty string. I think what you're saying is that the… the regular protobot implementations just make it hard to do, which, okay, that I understand.
**Josh Suereth** 13:05 It's… it's not… yeah, it's… you could say it makes it hard to do, or you could say the way we design our protocol buffers, what you're saying isn't true in the way we design our protocol buffers.
And empty… because by default, right, empty things are not passed around, so our one of… we no longer know what the 1 of is in the protocol buffer, the way it's designed.
And so, initially, when I came into OpenTelemetry, I thought that was by intention. And when I read this phrase here in the proto-definition, I thought that was also by intention. Of, okay, cool, we just have this special thing called empty.
Because of how we've defined this. It could be… it could be that that wasn't the intention at all in the protocol, in which case we'd have to restructure OTLP foundationally to change that, so that it works with native protocol buffer instrumentation. But I, you know… I… what I want to understand is… is… is this… this tight… like, what do we want to do now, given the scenario we're in?
**Tigran Najaryan** 14:02 Yeah.
Okay.
Yeah, this leads a bit… a bit… a bit of thought, I guess.
What do we do? The null part is the important part.
**Josh Suereth** 14:13 Yeah, so I wanted to print, like, have this discussion here of just, like, think about this issue, I want to talk about it in depth on Tuesday in the public meeting.
But, I don't think this is one we can come into without, like, some prep and some thought.
So my current intuition is that we basically have conflicting parts of the spec, and so we have to treat this as a bug and figure out what to do.
**Tigran Najaryan** 14:42 Okay, cool.
**Josh Suereth** 14:44 That's it for my public stuff. Should we, does anyone else have anything they want to talk about publicly before we move into private topics?
**Carlos Alberto Cortez** 15:03 I think we can go.
See you in one unit.
